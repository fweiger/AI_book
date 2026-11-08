"""五子棋 V1 纯 Python 规则；黑先、无禁手、15x15、五连及以上胜。"""
from __future__ import annotations
from copy import deepcopy
import re

SIZE = 15
COLUMNS = "ABCDEFGHIJKLMNO"
MOVE_RE = re.compile(r"^MOVE\s+([A-Z0-9-]{3,64})\s+([A-O](?:[1-9]|1[0-5]))\s*$", re.I)


def new_game(game_id, issue_number, black_token, white_token):
    if black_token == white_token:
        raise ValueError("双方身份码不能相同")
    return {
        "schema_version": 1, "game_id": game_id, "issue_number": issue_number,
        "rules": "freestyle-15x15",
        "players": {
            "black": {"name": "AI-A", "token": black_token},
            "white": {"name": "AI-B", "token": white_token}},
        "status": "playing", "turn": "black", "winner": None, "version": 0,
        "board": [[0 for _ in range(SIZE)] for _ in range(SIZE)],
        "moves": [], "events": [], "processed_comment_ids": []
    }


def parse_submission(body):
    m = MOVE_RE.fullmatch(body.strip())
    return (m.group(1).upper(), m.group(2).upper()) if m else None


def has_five(board, row, col, stone):
    for dr, dc in ((0, 1), (1, 0), (1, 1), (1, -1)):
        count = 1
        for sign in (-1, 1):
            r, c = row + sign * dr, col + sign * dc
            while 0 <= r < SIZE and 0 <= c < SIZE and board[r][c] == stone:
                count += 1
                r += sign * dr
                c += sign * dc
        if count >= 5:
            return True
    return False


def submit(state, comment_id, body, author=""):
    s = deepcopy(state)
    if comment_id in s["processed_comment_ids"]:
        return s
    parsed = parse_submission(body)
    if not parsed:
        return s
    token, coord = parsed
    side = next((k for k, p in s["players"].items() if p["token"] == token), None)
    reason = "accepted"
    if side is None:
        reason = "unknown-token"
    elif s["status"] != "playing":
        reason = "game-finished"
    elif s["turn"] != side:
        reason = "wrong-turn"
    else:
        row, col = int(coord[1:]) - 1, COLUMNS.index(coord[0])
        if s["board"][row][col] != 0:
            reason = "occupied"
        else:
            stone = 1 if side == "black" else 2
            s["board"][row][col] = stone
            s["version"] += 1
            s["moves"].append({"number": s["version"], "side": side, "coord": coord,
                               "comment_id": comment_id, "author": author})
            if has_five(s["board"], row, col, stone):
                s["status"], s["winner"], s["turn"] = "finished", side, None
            elif s["version"] == SIZE * SIZE:
                s["status"], s["winner"], s["turn"] = "finished", "draw", None
            else:
                s["turn"] = "white" if side == "black" else "black"
    s["processed_comment_ids"].append(comment_id)
    s["events"].append({"comment_id": comment_id, "author": author, "side": side,
                        "coord": coord, "result": reason})
    return s


def board_text(state):
    lines = ["    " + " ".join(COLUMNS)]
    for i, row in enumerate(state["board"], 1):
        lines.append(f"{i:>2}  " + " ".join(".XO"[v] for v in row))
    return "\n".join(lines)


def issue_body(state, state_url):
    code = chr(96)
    fence = code * 3
    turn = state["turn"]
    status = ("进行中，轮到黑方 AI-A" if turn == "black" else
              "进行中，轮到白方 AI-B" if turn == "white" else
              "已结束，胜方：" + str(state["winner"]))
    trail = ", ".join(f"{m['number']}.{m['side'][0].upper()}:{m['coord']}"
                      for m in state["moves"][-40:]) or "尚无落子"
    rejects = [e for e in state["events"] if e["result"] != "accepted"]
    recent = ", ".join(f"#{e['comment_id']} {e['result']}" for e in rejects[-5:]) or "无"
    return "\n".join([
        f"# {state['game_id']}｜AI A vs AI B｜文字五子棋 V1",
        "", f"**状态**：{status}",
        f"**版本**：{state['version']}，合法落子：{len(state['moves'])} 手",
        "**规则**：15×15、黑先、无禁手、五连及以上获胜",
        f"**黑方 AI-A 身份码**：{code}{state['players']['black']['token']}{code}",
        f"**白方 AI-B 身份码**：{code}{state['players']['white']['token']}{code}",
        "", "## 最新棋盘", "",
        "X=黑方，O=白方，.=空；列 A-O，行 1-15。", "",
        fence + "text", board_text(state), fence, "",
        "## 落子协议", "",
        "只有轮到的棋手可以提交一行：MOVE 身份码 H8。格式不匹配不处理。身份码仅为实验身份标记，不是安全认证。", "",
        "## 历史与机器读取", "",
        f"- [完整 JSON 棋盘]({state_url})",
        f"- 最近合法落子：{trail}",
        f"- 最近拒绝记录：{recent}",
        "- 全部历史保存在 JSON 的 moves 与 events 字段。",
        "- 两个 AI 只读 JSON、在本 Issue 提交一行落子，不能直接修改棋盘。",
        "- GitHub Actions + Python 负责验证、记录与更新本页。", ""
    ])
