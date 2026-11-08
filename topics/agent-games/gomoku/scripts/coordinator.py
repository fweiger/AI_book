"""外部主机五子棋协调器：GitHub 状态轮询 -> Codex CLI 决策 -> Issue 落子。

不调用自建大模型 API。GitHub Actions 裁判仍是唯一状态写入者。
默认只运行一轮且不发表评论；--loop --play 才允许常驻真实落子。
"""
from __future__ import annotations

import argparse
import base64
import json
import logging
import os
import re
import stat
import subprocess
import tempfile
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

REPO = "fweiger/AI_book"
ISSUE = 24
STATE = "topics/agent-games/gomoku/games/GAME-001/state.json"
WORKFLOW = "ai-book-gomoku-referee.yml"
COLUMNS = "ABCDEFGHIJKLMNO"
COORD = re.compile(r"^[A-O](?:[1-9]|1[0-5])$")
MOVE = re.compile(r"^MOVE\s+(\S+)\s+([A-O](?:[1-9]|1[0-5]))$", re.I)
LOG = logging.getLogger("gomoku-coordinator")


def token_value():
    raw = os.environ.get("AI_BOOK_GITHUB_TOKEN", "").strip()
    if raw:
        return raw
    file = os.environ.get("AI_BOOK_GITHUB_TOKEN_FILE", "").strip()
    if not file:
        return ""
    p = Path(file).expanduser()
    if os.name == "posix" and stat.S_IMODE(p.stat().st_mode) & 0o077:
        raise RuntimeError("Token 文件权限过宽，请 chmod 600")
    return p.read_text(encoding="utf-8").strip()


class GitHub:
    def __init__(self, token):
        self.token = token

    def api(self, method, endpoint, body=None, etag=""):
        headers = {
            "Accept": "application/vnd.github+json",
            "X-GitHub-Api-Version": "2022-11-28",
            "User-Agent": "AI-book-Gomoku-Coordinator",
        }
        if self.token:
            headers["Authorization"] = "Bearer " + self.token
        if etag:
            headers["If-None-Match"] = etag
        data = None if body is None else json.dumps(body).encode("utf-8")
        if data is not None:
            headers["Content-Type"] = "application/json"
        req = urllib.request.Request(
            f"https://api.github.com/repos/{REPO}{endpoint}",
            data=data, method=method, headers=headers)
        try:
            with urllib.request.urlopen(req, timeout=20) as resp:
                content = resp.read()
                return json.loads(content) if content else None, resp.headers.get("ETag", "")
        except urllib.error.HTTPError as exc:
            if exc.code == 304:
                return None, etag
            # Avoid printing headers, tokens or full authentication responses.
            raise RuntimeError(f"GitHub {method} failed: HTTP {exc.code}") from None

    def state(self, etag=""):
        path = urllib.parse.quote(STATE, safe="/")
        item, next_etag = self.api("GET", f"/contents/{path}?ref=main", etag=etag)
        if item is None:
            return None, next_etag
        data = json.loads(base64.b64decode(item["content"]))
        if data.get("game_id") != "GAME-001" or len(data.get("board", [])) != 15:
            raise RuntimeError("Unexpected GAME-001 state")
        return data, next_etag

    def has_pending_move(self, state, side):
        comments, _ = self.api("GET", f"/issues/{ISSUE}/comments?per_page=100")
        if len(comments) == 100:
            raise RuntimeError("评论数已达 100，请添加分页处理")
        seen = set(state["processed_comment_ids"])
        role_token = state["players"][side]["token"].upper()
        return any(
            c["id"] not in seen
            and (m := MOVE.fullmatch(c.get("body", "").strip())) is not None
            and m.group(1).upper() == role_token
            for c in comments
        )

    def post(self, role_token, coord):
        reply, _ = self.api(
            "POST", f"/issues/{ISSUE}/comments",
            {"body": f"MOVE {role_token} {coord}"})
        return int(reply["id"])

    def recover_referee(self):
        self.api(
            "POST", f"/actions/workflows/{WORKFLOW}/dispatches",
            {"ref": "main"})


def draw(state):
    header = "    " + " ".join(COLUMNS)
    return "\n".join([header] + [
        f"{row+1:>2}  " + " ".join(".XO"[int(v)] for v in line)
        for row, line in enumerate(state["board"])
    ])


def decide(state, side, timeout):
    history = ", ".join(
        f"{m['number']}.{m['side'][0]}:{m['coord']}" for m in state["moves"])
    prompt = "\n".join([
        f"你是五子棋独立棋手：{side}。无禁手，15x15，五连及以上获胜。",
        "仅负责根据棋盘决定一手棋，不要联网，不调用任何工具，不写文件。",
        "优先考虑本手取胜、阻止对方下一手取胜以及有效攻防。",
        f"棋局版本：{state['version']}；轮到：{state['turn']}。",
        "列 A-O，行 1-15，X=黑，O=白，.=空。",
        draw(state), "历史落子：" + (history or "无"),
        "只输出一个合法的未占用坐标（例如 H8），不要输出其他任何文字。",
    ])
    with tempfile.TemporaryDirectory(prefix="ai-book-move-") as tmp:
        answer = Path(tmp) / "answer.txt"
        cmd = [
            "codex", "exec", "--skip-git-repo-check", "--ephemeral",
            "--sandbox", "read-only", "-o", str(answer), "-"]
        env = os.environ.copy()
        for key in ("GH_TOKEN", "GITHUB_TOKEN", "AI_BOOK_GITHUB_TOKEN",
                    "AI_BOOK_GITHUB_TOKEN_FILE"):
            env.pop(key, None)
        result = subprocess.run(
            cmd, input=prompt, text=True, capture_output=True,
            cwd=tmp, env=env, timeout=timeout, check=False)
        if result.returncode != 0:
            raise RuntimeError(f"Codex CLI failed: exit={result.returncode}")
        coord = answer.read_text(encoding="utf-8").strip().upper()
    if not COORD.fullmatch(coord):
        raise RuntimeError("Codex 没有只输出合法坐标")
    row, col = int(coord[1:])-1, COLUMNS.index(coord[0])
    if state["board"][row][col] != 0:
        raise RuntimeError(f"Codex 返回已占用位置：{coord}")
    return coord


def save(path, obj):
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(".tmp")
    tmp.write_text(json.dumps(obj, ensure_ascii=False, indent=2), encoding="utf-8")
    os.replace(tmp, path)


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--loop", action="store_true", help="持续轮询")
    p.add_argument("--play", action="store_true", help="允许真实发送落子评论")
    p.add_argument("--interval", type=int, default=10)
    p.add_argument("--model-timeout", type=int, default=180)
    p.add_argument("--dispatch-fallback", action="store_true")
    p.add_argument("--cursor", default="~/.local/state/ai-book-gomoku/cursor.json")
    args = p.parse_args()
    if args.interval < 10:
        p.error("轮询间隔不能少于 10 秒")
    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
    token = token_value()
    if args.play and not token:
        raise RuntimeError("缺少 AI_BOOK_GITHUB_TOKEN 或 AI_BOOK_GITHUB_TOKEN_FILE")
    if args.loop and args.interval < 60 and not token:
        raise RuntimeError("10 秒轮询需要认证以避免 GitHub 匿名 API 限额")
    github = GitHub(token)
    file = Path(args.cursor).expanduser()
    cursor = json.loads(file.read_text(encoding="utf-8")) if file.exists() else {}
    etag = ""
    state = None
    while True:
        try:
            updated, etag = github.state(etag)
            if updated is not None:
                state = updated
            if state is None:
                raise RuntimeError("Unable to fetch game state")
            pending = cursor.get("pending")
            if pending and pending["id"] in state["processed_comment_ids"]:
                LOG.info("评论 #%s 已完成裁判处理", pending["id"])
                cursor.pop("pending", None)
                save(file, cursor)
                pending = None
            if pending and args.dispatch_fallback and args.play:
                if (time.time() - pending["since"] > 45
                        and time.time() - pending.get("last_dispatch", 0) > 180):
                    # issue_comment should have triggered referee already;
                    # workflow_dispatch is only a recovery path.
                    github.recover_referee()
                    cursor["pending"]["last_dispatch"] = time.time()
                    save(file, cursor)
                    LOG.warning("裁判超时，补触发一次 GitHub Actions")
            if state["status"] != "playing":
                LOG.info("对局结束，结果：%s", state.get("winner"))
                return
            key = f"{state['game_id']}:{state['version']}:{state['turn']}"
            if not pending and cursor.get("last_attempt") != key:
                side = state["turn"]
                if side not in ("black", "white"):
                    raise RuntimeError("Unknown turn")
                if github.has_pending_move(state, side):
                    LOG.info("%s 已有待裁判棋步，不重复发送", side)
                else:
                    coord = decide(state, side, args.model_timeout)
                    LOG.info("v%s %s 选择 %s", state["version"], side, coord)
                    if args.play:
                        latest, _ = github.state()
                        if ((latest["version"], latest["turn"], latest["status"]) !=
                                (state["version"], side, "playing")):
                            LOG.warning("思考期间棋局已变化，放弃旧棋步")
                        elif github.has_pending_move(latest, side):
                            LOG.warning("已有棋步提交，放弃本次")
                        else:
                            comment_id = github.post(latest["players"][side]["token"], coord)
                            cursor["last_attempt"] = key
                            cursor["pending"] = {"id": comment_id, "since": time.time(),
                                                 "last_dispatch": 0}
                            save(file, cursor)
                            LOG.info("已提交 Issue 评论 #%s，交由 GitHub Actions 裁判", comment_id)
            if not args.loop:
                return
            time.sleep(args.interval)
        except (OSError, ValueError, RuntimeError, subprocess.TimeoutExpired) as exc:
            LOG.error("本轮失败：%s", exc)
            if not args.loop:
                raise
            time.sleep(max(10, min(args.interval, 60)))


if __name__ == "__main__":
    main()
