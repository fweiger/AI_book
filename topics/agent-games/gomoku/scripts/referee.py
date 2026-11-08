"""GitHub Actions 自动裁判：处理 Issue 评论、更新 JSON 和文字棋盘。"""
from __future__ import annotations
import base64
import json
import logging
import os
import sys
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path
from game import issue_body, submit

STATE_PATH = "topics/agent-games/gomoku/games/GAME-001/state.json"
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


def run():
    logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")
    repo = os.environ.get("GITHUB_REPOSITORY", "")
    if "/" not in repo:
        raise RuntimeError("缺少有效 GITHUB_REPOSITORY")
    path = urllib.parse.quote(STATE_PATH, safe="/")
    state_file = request("GET", f"/repos/{repo}/contents/{path}")
    state = json.loads(base64.b64decode(state_file["content"]))
    issue = int(state["issue_number"])
    if os.environ.get("GITHUB_EVENT_NAME") == "issue_comment":
        event = json.loads(Path(os.environ["GITHUB_EVENT_PATH"]).read_text())
        if (event.get("issue", {}).get("pull_request") or
                int(event.get("issue", {}).get("number", -1)) != issue):
            LOG.info("非 GAME-001 Issue，跳过")
            return
    count_before = len(state["events"])
    for comment in comments(repo, issue):
        state = submit(state, int(comment["id"]), comment.get("body", ""),
                       comment.get("user", {}).get("login", ""))
    new_count = len(state["events"]) - count_before
    if new_count:
        new_content = json.dumps(state, ensure_ascii=False, indent=2) + "\n"
        request("PUT", f"/repos/{repo}/contents/{path}", {
            "message": f"gomoku: process {new_count} comment(s)",
            "sha": state_file["sha"],
            "content": base64.b64encode(new_content.encode()).decode(),
        })
        LOG.info("处理 %s 条请求，棋局版本 %s", new_count, state["version"])
    url = f"https://github.com/{repo}/blob/main/{STATE_PATH}"
    request("PATCH", f"/repos/{repo}/issues/{issue}",
            {"body": issue_body(state, url)})
    LOG.info("同步 Issue #%s 文字棋盘完成", issue)


if __name__ == "__main__":
    try:
        run()
    except Exception:
        LOG.exception("自动裁判失败，等待后续定时补扫")
        sys.exit(1)
