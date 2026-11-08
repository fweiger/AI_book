"""GitHub Actions Python 裁判：按 active.json 分发当前五子棋对局。

仅裁判，不运行 AI、不计算棋手决策。不会重新写入已完成的 GAME-001。
"""
from __future__ import annotations

import base64
import json
import logging
import os
import re
import sys
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

from game import issue_body, submit

ROOT = "topics/agent-games/gomoku"
ACTIVE_PATH = f"{ROOT}/games/active.json"
API = "https://api.github.com"
LOG = logging.getLogger(__name__)


def request(method, path, payload=None):
    token = os.environ.get("GITHUB_TOKEN")
    if not token:
        raise RuntimeError("缺少 GITHUB_TOKEN")
    data = json.dumps(payload, ensure_ascii=False).encode() if payload is not None else None
    req = urllib.request.Request(
        API + path, data=data, method=method, headers={
            "Authorization": f"Bearer {token}",
            "Accept": "application/vnd.github+json",
            "X-GitHub-Api-Version": "2022-11-28",
            "User-Agent": "ai-book-gomoku-referee",
            "Content-Type": "application/json",
        })
    try:
        with urllib.request.urlopen(req, timeout=25) as resp:
            return json.load(resp)
    except urllib.error.HTTPError as exc:
        LOG.error("HTTP %s %s %s: %s", exc.code, method, path,
                  exc.read().decode(errors="replace")[:1000])
        raise


def contents(repo, path):
    quoted = urllib.parse.quote(path, safe="/")
    raw = request("GET", f"/repos/{repo}/contents/{quoted}")
    if not isinstance(raw, dict) or not raw.get("sha") or not raw.get("content"):
        raise RuntimeError(f"无效的 GitHub 文件响应: {path}")
    return json.loads(base64.b64decode(raw["content"])), raw["sha"]


def put_contents(repo, path, state, sha, message):
    quoted = urllib.parse.quote(path, safe="/")
    data = json.dumps(state, ensure_ascii=False, indent=2) + "\n"
    return request("PUT", f"/repos/{repo}/contents/{quoted}", {
        "message": message,
        "sha": sha,
        "content": base64.b64encode(data.encode("utf-8")).decode("ascii"),
    })


def validated_active(registry):
    if not isinstance(registry, dict) or registry.get("schema_version") != 1:
        raise RuntimeError("active.json schema_version 无效")
    active = registry.get("active_game")
    if active is None:
        return None
    if not isinstance(active, dict):
        raise RuntimeError("active_game 不是对象")
    game_id, issue, path = (active.get("game_id"), active.get("issue_number"),
                            active.get("state_path"))
    if not isinstance(game_id, str) or not re.fullmatch(r"GAME-[0-9]{3,}", game_id):
        raise RuntimeError("active_game.game_id 非法")
    if type(issue) is not int or issue <= 0:
        raise RuntimeError("active_game.issue_number 非法")
    expected = f"{ROOT}/games/{game_id}/state.json"
    if path != expected:
        raise RuntimeError("active_game.state_path 非法或与 game_id 不匹配")
    return active


def comments(repo, issue):
    all_items = []
    for page in range(1, 100):
        batch = request("GET", f"/repos/{repo}/issues/{issue}/comments?per_page=100&page={page}")
        if not isinstance(batch, list):
            raise RuntimeError("GitHub 评论响应不是数组")
        all_items.extend(batch)
        if len(batch) < 100:
            return sorted(all_items, key=lambda item: item["id"])
    raise RuntimeError("评论超出分页扫描上限")


def event_matches(issue_number):
    if os.environ.get("GITHUB_EVENT_NAME") != "issue_comment":
        return True
    event_path = os.environ.get("GITHUB_EVENT_PATH")
    if not event_path:
        raise RuntimeError("issue_comment 事件缺少 GITHUB_EVENT_PATH")
    event = json.loads(Path(event_path).read_text(encoding="utf-8"))
    if event.get("issue", {}).get("pull_request"):
        return False
    return event.get("issue", {}).get("number") == issue_number


def state_matches(active, state):
    if (state.get("game_id") != active["game_id"]
            or state.get("issue_number") != active["issue_number"]):
        raise RuntimeError("权威棋盘 game_id/issue_number 与 active.json 不一致")
    if state.get("status") not in ("playing", "finished"):
        raise RuntimeError("棋局状态非法")
    moves = state.get("moves")
    if (not isinstance(moves, list)
            or type(state.get("version")) is not int
            or state["version"] != len(moves)):
        raise RuntimeError("棋谱版本与步数不一致")


def finalized_registry(registry, active, state):
    next_registry = dict(registry)
    next_registry["active_game"] = None
    next_registry["last_completed"] = {
        "game_id": active["game_id"],
        "issue_number": active["issue_number"],
        "state_path": active["state_path"],
        "status": state["status"],
        "winner": state["winner"],
        "version": state["version"],
        "moves": len(state["moves"]),
    }
    return next_registry


def run():
    logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")
    repo = os.environ.get("GITHUB_REPOSITORY", "")
    if "/" not in repo:
        raise RuntimeError("缺少有效 GITHUB_REPOSITORY")

    registry, registry_sha = contents(repo, ACTIVE_PATH)
    active = validated_active(registry)
    if active is None:
        LOG.info("没有活动对局，无需裁判；历史棋局保持不变")
        return
    if not event_matches(active["issue_number"]):
        LOG.info("不是当前游戏 %s 的 Issue 评论，跳过", active["game_id"])
        return

    state_path = active["state_path"]
    state, state_sha = contents(repo, state_path)
    state_matches(active, state)

    previous = len(state["events"])
    for comment in comments(repo, active["issue_number"]):
        state = submit(state, int(comment["id"]), comment.get("body", ""),
                       comment.get("user", {}).get("login", ""))
    new_count = len(state["events"]) - previous

    # Guard against a human concurrently switching the active game.
    current_registry, current_sha = contents(repo, ACTIVE_PATH)
    if validated_active(current_registry) != active:
        raise RuntimeError("执行中活动对局改变，拒绝写入旧棋局")

    if new_count:
        put_contents(repo, state_path, state, state_sha,
                     f"gomoku: {active['game_id']} process {new_count} comment(s)")
        LOG.info("%s 处理 %s 条请求，棋局版本 %s",
                 active["game_id"], new_count, state["version"])

    url = f"https://github.com/{repo}/blob/main/{state_path}"
    request("PATCH", f"/repos/{repo}/issues/{active['issue_number']}",
            {"body": issue_body(state, url)})
    LOG.info("同步 %s Issue #%s", active["game_id"], active["issue_number"])

    if state["status"] == "finished":
        # Only clear registry after publishing the final board. If this PUT
        # fails, the next scheduled referee run safely retries finalization.
        next_registry = finalized_registry(current_registry, active, state)
        put_contents(repo, ACTIVE_PATH, next_registry, current_sha,
                     f"gomoku: archive finished {active['game_id']}")
        LOG.info("对局结束，注册表已清空：%s 胜方=%s",
                 active["game_id"], state["winner"])


if __name__ == "__main__":
    try:
        run()
    except Exception:
        LOG.exception("自动裁判失败，等待后续定时补扫")
        sys.exit(1)
