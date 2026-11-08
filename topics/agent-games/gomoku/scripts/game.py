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
    move_count = len(state["moves"])
    latest = state["moves"][-1] if state["moves"] else None
    latest_text = (
        f"第 {latest['number']} 手，"
        f"{'黑方 AI-A' if latest['side'] == 'black' else '白方 AI-B'} "
        f"{latest['coord']}" if latest else "尚未落子（空棋盘）"
    )
    next_text = (
        f"第 {move_count + 1} 手，"
        f"{'黑方 AI-A' if turn == 'black' else '白方 AI-B'}"
        if turn else "对局已结束，无下一手"
    )
    trail = ", ".join(f"{m['number']}.{m['side'][0].upper()}:{m['coord']}"
                      for m in state["moves"][-40:]) or "尚无落子"
    rejects = [e for e in state["events"] if e["result"] != "accepted"]
    recent = ", ".join(f"#{e['comment_id']} {e['result']}" for e in rejects[-5:]) or "无"
    return "\n".join([
        f"# {state['game_id']}｜AI A vs AI B｜文字五子棋",
        "", f"**状态**：{status}",
        f"**版本**：{state['version']}，合法落子：{len(state['moves'])} 手",
        f"**最新落子**：{latest_text}",
        f"**下一手**：{next_text}",
        "**规则**：15×15、黑先、无禁手、五连及以上获胜",
        f"**黑方 AI-A 身份码**：{code}{state['players']['black']['token']}{code}",
        f"**白方 AI-B 身份码**：{code}{state['players']['white']['token']}{code}",
        "", "## 最新棋盘", "",
        "X=黑方，O=白方，.=空；列 A-O，行 1-15。", "",
        fence + "text", board_text(state), fence, "",
        "## 当前 AI 的待回答问题（网页版 AI 各自处理）", "",
        ("**请 AI-A 黑方执行下一手**" if turn == "black" else
         "**请 AI-B 白方执行下一手**" if turn == "white" else
         "**对局结束：两位 AI 不要继续提交落子**"), "",
        "你的任务：读取最新 state.json 和本 Issue 最近评论，确认确实轮到自己且没有未处理的己方评论；结合棋盘和历史，判断对方的威胁、自己的进攻机会，选择当前最有价值的一个**空位坐标**（A–O / 1–15）。思考过程保留在各自网页版 AI 会话中。", "",
        ("**本轮仅接受白方 AI-B：** " + code +
         f"MOVE {state['players']['white']['token']} <坐标>" + code
         if turn == "white" else
         "**本轮仅接受黑方 AI-A：** " + code +
         f"MOVE {state['players']['black']['token']} <坐标>" + code
         if turn == "black" else "本局已结束，任何落子均会被裁判拒绝。"), "",
        "## 两个网页版 AI 的任务入口与提交模板", "",
        "- [AI-A 黑方完整提示词](https://github.com/fweiger/AI_book/blob/main/topics/agent-games/gomoku/prompts/AI-A-black.md)",
        "- [AI-B 白方完整提示词](https://github.com/fweiger/AI_book/blob/main/topics/agent-games/gomoku/prompts/AI-B-white.md)",
        "- **提交方式**：两个 AI 在自己的网页会话中使用已连接的 GitHub 工具，在本 Issue 发表一条评论。正文必须且只能是一行 `MOVE 身份码 坐标`（示例：`MOVE 身份码 H8`，其中身份码必须取自当前棋盘）。不得在评论中添加解释。",
        "- **提交后**：GitHub Actions 的 Python 裁判自动检查身份、轮次、占用、五连或平局；更新 JSON、本 Issue 和观战页面的数据源。另一个用户再手动唤醒他自己的网页版 AI，按同样方式执行下一手。",
        "- **服务器职责**：31.5 / Ubuntu 只监测 GitHub 和必要时补触发裁判；**不调用模型、不代下棋、也不能自动唤醒普通网页版 AI 会话**。",
        "- 双方身份码当前公开，仅作为 V1 的角色标签，不构成安全验证。", "",
        "## 历史与机器读取", "",
        f"- [完整 JSON 棋盘]({state_url})",
        f"- 最近合法落子：{trail}",
        f"- 最近拒绝记录：{recent}",
        "- 全部历史保存在 JSON 的 moves 与 events 字段。",
        "- 两个 AI 只读 JSON、在本 Issue 提交一行落子，不能直接修改棋盘。",
        "- GitHub Actions + Python 负责验证、记录与更新本页。", ""
    ])
