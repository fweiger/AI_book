# AI_book｜双网页版 AI 五子棋协作实验

> 系统边界：两个用户各自在独立网页版 AI 会话中思考与落子；GitHub Issue 传递落子，GitHub Actions/Python 裁判判定并写入权威棋谱。**不调用大模型 API，不用 Ubuntu CLI 模型替棋手下棋。**

## 最新状态

- **GAME-001 V1：已完成，白方 AI-B 获胜。** 30 手有效落子，最后一手 `J13`，五连 `F9 → G10 → H11 → I12 → J13`。第 1–3 手是系统联调测试落子，不能计入纯网页版 AI 从零对局的统计。
- [对局 Issue #24](https://github.com/fweiger/AI_book/issues/24) · [最终 state.json](games/GAME-001/state.json) · [结果与验收记录](results/GAME-001-ACCEPTANCE.md)。
- **没有正在进行的正式新对局**：`games/active.json.active_game = null`；不应再向 GAME-001 发送落子。
- **V2 进行中**：固定角色提示词和注册表已经建立；新的多棋局裁判路由、开局器及终局自动归档**尚未实现**，不能仅修改活动游戏 ID 就直接玩 GAME-002。

## 两个网页版 AI 的长期固定提示词

每轮仍由各自用户在对应网页版 AI 会话中执行固定提示词，不需要每次修改“第几步、落在哪里、轮到谁”。

- [黑方 AI-A 固定提示词](prompts/AI-A-black.md)
- [白方 AI-B 固定提示词](prompts/AI-B-white.md)
- [V2 需求说明与验收门槛](V2-REQUIREMENTS.md) · [观战与操作手册](RUNBOOK.md)

两份提示词只固定角色，不写死下一盘的 Issue、身份码、游戏 ID、步数或坐标，统一从 [当前对局注册表](games/active.json) 获取权威游戏入口。

**运行流程**：当前用户唤醒自己对应的网页版 AI → 读取 `active.json` → 读取对应 `state.json` 和 Issue 评论 → 检查回合、版本、历史及未处理评论 → 自主选空位 → 在指定 Issue 只提交一行 `MOVE <身份码> <坐标>` → Python 裁判接受或拒绝 → 用户唤醒下一位网页版 AI。

目前尚无新的活动棋局，两个角色提示词会按其规范安全退出，而不是在已经结束的 GAME-001 上落子。

## 棋谱与裁判：V1 已实现

- 15×15、黑先、无禁手，横、竖、斜五连及以上获胜，满盘平局。
- `state.moves[]` 每步记录 `number`（第几步）、`side`（颜色）、`coord`（坐标）、`comment_id`；`version` 随每步合法落子递增。
- 最新一步为 `moves[-1]`；下一手是 `len(moves)+1`，不应硬编码到提示词。
- AI 不编辑棋盘；只通过 GitHub Issue 评论提交 `MOVE 身份码 坐标`，目前裁判只接受此格式。
- `issue_comment.created` 触发 GitHub Actions/Python 裁判；按评论 ID 顺序幂等处理，检查轮次、身份码、空位和终局，更新 JSON 和 Issue。
- 裁判现阶段仍按 GAME-001 的 Issue 绑定运行，下一盘需要独立实现多棋局路由及生命周期管理。

[裁判工作流](../../../.github/workflows/ai-book-gomoku-referee.yml) · [裁判程序](scripts/referee.py) · [棋盘规则](scripts/game.py)

## 观战与监控

- [图形观战页面源码](../../../docs/gomoku/index.html) · [GitHub Pages 工作流](../../../.github/workflows/ai-book-gomoku-pages.yml)。是否已经上线以 GitHub Pages 实际部署状态为准。
- [Ubuntu 临时监控程序](scripts/coordinator.py) · [临时运行说明](deploy/README.md)。监控只读 GitHub 状态；经授权可在裁判延迟时补触发 Actions。**不能计算落点、发布棋手评论、唤醒普通网页版 AI**。
- **本次 GAME-001 使用的 Ubuntu 临时监控 Job 已终止（`timeout`）**，无需保留系统服务。用户未要求就不得改成常驻 systemd。

## 历史资料与测试

- [GAME-001 黑方原始提示词](prompts/archive/GAME-001-A-black.md) · [GAME-001 白方原始提示词](prompts/archive/GAME-001-B-white.md)
- [完整 V1 对局结果](results/GAME-001-ACCEPTANCE.md)
- 本地验证：`python3 -m unittest discover -s topics/agent-games/gomoku/tests -v`

## 下一步（V2）

1. 新建 GAME-002 独立 Issue、独立棋盘与玩家身份码。
2. 先扩展并测试裁判按 `game_id + issue_number` 正确分发，确保不能串局，再将 `active.json` 指向下一盘。
3. 用两份不变的固定提示词，分别启动两个网页版 AI，从空棋盘独立对弈并进行端到端验收。
4. 对局结束后锁定历史，并清空 `active_game`。网页版 AI 由用户手动唤醒，外部事件自动唤醒仍属待验证方向。
