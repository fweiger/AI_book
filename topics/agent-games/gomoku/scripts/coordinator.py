"""AI_book GAME-001 external GitHub watcher; NEVER runs or decides moves for an AI.

Two independently operated web AIs write Issue #24 comments. GitHub Actions is
the only referee and state writer. This process only detects unprocessed MOVE
comments and optionally dispatches that existing referee workflow as fallback.
"""
from __future__ import annotations

import argparse
import base64
import hashlib
import json
import logging
import os
import re
import stat
import time
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

REPO = "fweiger/AI_book"
ISSUE = 24
STATE_PATH = "topics/agent-games/gomoku/games/GAME-001/state.json"
WORKFLOW = "ai-book-gomoku-referee.yml"
MOVE_RE = re.compile(r"^MOVE\s+([A-Z0-9-]{3,64})\s+([A-O](?:[1-9]|1[0-5]))\s*$", re.I)
LOG = logging.getLogger("ai-book-gomoku-monitor")


def token_value() -> str:
    """Read only a GitHub API credential, never a model credential."""
    value = os.environ.get("AI_BOOK_GITHUB_TOKEN", "").strip()
    if value:
        return value
    filename = os.environ.get("AI_BOOK_GITHUB_TOKEN_FILE", "")
    if not filename:
        return ""
    file = Path(filename).expanduser()
    mode = stat.S_IMODE(file.stat().st_mode)
    if os.name == "posix" and mode & 0o077:
        raise RuntimeError("GitHub token file must be chmod 600")
    return file.read_text(encoding="utf-8").strip()


class GitHub:
    def __init__(self, token: str):
        self.token = token

    def api(self, method: str, endpoint: str, payload=None):
        headers = {
            "Accept": "application/vnd.github+json",
            "X-GitHub-Api-Version": "2022-11-28",
            "User-Agent": "AI-book-Gomoku-Monitor",
        }
        if self.token:
            headers["Authorization"] = "Bearer " + self.token
        data = json.dumps(payload).encode("utf-8") if payload is not None else None
        if data is not None:
            headers["Content-Type"] = "application/json"
        request = urllib.request.Request(
            f"https://api.github.com/repos/{REPO}{endpoint}",
            method=method, headers=headers, data=data)
        try:
            with urllib.request.urlopen(request, timeout=20) as response:
                raw = response.read()
                return json.loads(raw) if raw else None
        except urllib.error.HTTPError as exc:
            # Never display token values or potentially sensitive response headers.
            raise RuntimeError(f"GitHub {method} request failed: HTTP {exc.code}") from None

    def state(self) -> dict:
        path = urllib.parse.quote(STATE_PATH, safe="/")
        raw = self.api("GET", f"/contents/{path}?ref=main")
        state = json.loads(base64.b64decode(raw["content"]))
        if (state.get("game_id") != "GAME-001"
                or state.get("issue_number") != ISSUE
                or not isinstance(state.get("processed_comment_ids"), list)
                or not isinstance(state.get("version"), int)):
            raise RuntimeError("Unexpected GAME-001 state")
        return state

    def comments(self) -> list[dict]:
        result: list[dict] = []
        for page in range(1, 11):
            batch = self.api("GET", f"/issues/{ISSUE}/comments?per_page=100&page={page}")
            if not isinstance(batch, list):
                raise RuntimeError("Invalid GitHub comments response")
            result.extend(batch)
            if len(batch) < 100:
                return result
        raise RuntimeError("Too many comments (>1000); refusing incomplete scan")

    def dispatch_referee(self):
        """Only GitHub Actions; no ChatGPT or model task is started here."""
        self.api("POST", f"/actions/workflows/{WORKFLOW}/dispatches",
                 {"ref": "main"})


def pending_moves(state: dict, comments: list[dict]) -> list[dict]:
    """Only comments that could be processed by the current Python referee."""
    done = set(state["processed_comment_ids"])
    pending = []
    for comment in comments:
        if comment.get("id") in done:
            continue
        match = MOVE_RE.fullmatch(str(comment.get("body") or "").strip())
        if match:
            pending.append(comment)
    return sorted(pending, key=lambda x: int(x["id"]))


def comment_age_seconds(comment: dict, now: float) -> float:
    created = str(comment.get("created_at") or "")
    if not created:
        raise ValueError("GitHub comment missing created_at")
    stamp = datetime.fromisoformat(created.replace("Z", "+00:00"))
    if stamp.tzinfo is None:
        raise ValueError("Comment created_at has no timezone")
    return max(0.0, now - stamp.astimezone(timezone.utc).timestamp())


def should_dispatch(pending: list[dict], cursor: dict, *, now: float,
                    grace_seconds: int, cooldown_seconds: int) -> bool:
    if not pending:
        return False
    oldest = min(comment_age_seconds(c, now) for c in pending)
    # Grace lets issue_comment.created execute normally before we recover.
    if oldest < grace_seconds:
        return False
    fingerprint = hashlib.sha256(",".join(str(c["id"]) for c in pending).encode()).hexdigest()
    if (fingerprint == cursor.get("fingerprint")
            and now - float(cursor.get("dispatched_at", 0)) < cooldown_seconds):
        return False
    return True


def save_cursor(path: Path, data: dict):
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(".tmp")
    tmp.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")
    os.replace(tmp, path)


def run_once(gh: GitHub, cursor: dict, *, dispatch: bool,
             grace_seconds: int, cooldown_seconds: int, cursor_path: Path):
    state = gh.state()
    comments = gh.comments()
    pending = pending_moves(state, comments)
    now = time.time()
    signature = (state["version"], state.get("turn"), tuple(c["id"] for c in pending))
    if cursor.get("last_observation") != repr(signature):
        LOG.info("GAME-001: version=%s turn=%s status=%s pending=%s",
                 state["version"], state.get("turn"), state.get("status"), len(pending))
        cursor["last_observation"] = repr(signature)
        save_cursor(cursor_path, cursor)
    if pending and should_dispatch(pending, cursor, now=now,
                                   grace_seconds=grace_seconds,
                                   cooldown_seconds=cooldown_seconds):
        if dispatch:
            gh.dispatch_referee()
            cursor["fingerprint"] = hashlib.sha256(
                ",".join(str(c["id"]) for c in pending).encode()).hexdigest()
            cursor["dispatched_at"] = time.time()
            save_cursor(cursor_path, cursor)
            LOG.warning("Pending MOVE comment(s) detected; dispatched referee workflow")
        else:
            LOG.info("Unprocessed MOVE found; monitoring only (no dispatch)")
    return state


def main():
    parser = argparse.ArgumentParser(description="GitHub-only GAME-001 referee watchdog")
    parser.add_argument("--loop", action="store_true", help="repeat until stopped")
    parser.add_argument("--dispatch", action="store_true", help="allow workflow_dispatch recovery")
    parser.add_argument("--interval", type=int, default=10)
    parser.add_argument("--grace", type=int, default=45)
    parser.add_argument("--cooldown", type=int, default=180)
    parser.add_argument("--cursor", default="~/.local/state/ai-book-gomoku/monitor.json")
    args = parser.parse_args()
    if args.interval < 10 or args.grace < 0 or args.cooldown < 60:
        parser.error("interval >= 10, grace >= 0 and cooldown >= 60 required")
    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
    token = token_value()
    if args.dispatch and not token:
        raise RuntimeError("--dispatch requires a GitHub token with Actions:write permission")
    if args.loop and args.interval < 60 and not token:
        raise RuntimeError("10-second polling requires a GitHub token to avoid anonymous rate limits")
    gh = GitHub(token)
    path = Path(args.cursor).expanduser()
    cursor = json.loads(path.read_text(encoding="utf-8")) if path.exists() else {}
    while True:
        try:
            state = run_once(gh, cursor, dispatch=args.dispatch,
                             grace_seconds=args.grace, cooldown_seconds=args.cooldown,
                             cursor_path=path)
            if state.get("status") == "finished":
                LOG.info("Game ended: %s. Watchdog exiting", state.get("winner"))
                return
        except (OSError, ValueError, RuntimeError, KeyError) as exc:
            LOG.error("Monitor iteration failed: %s", exc)
            if not args.loop:
                raise
        if not args.loop:
            return
        time.sleep(args.interval)


if __name__ == "__main__":
    main()
