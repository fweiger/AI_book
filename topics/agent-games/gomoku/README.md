# AI_book｜双网页版 AI 五子棋协作实验

> 系统边界：两个用户各自在独立网页版 AI 会话中思考与落子；GitHub Issue 传递落子，GitHub Actions/Python 裁判判定并写入权威棋谱。**不调用大模型 API，不用 Ubuntu CLI 模型替棋手下棋。**

## 最新状态

- **GAME-001 V1：已完成，白方 AI-B 获胜。** 30 手有效落子，最后一手 `J13`，五连 `F9 → G10 → H11 → I12 → J13`。第 1–3 手是系统联调测试落子，不能计入纯网页版 AI 从零对局的统计。
- [对局 Issue #24](https://github.com/fweiger/AI_book/issues/24) · [最终 state.json](games/GAME-001/state.json) · [结果与验收记录](results/GAME-001-ACCEPTANCE.md)。
- **GAME-002 已正式从空棋盘启动**：独立 [Issue #25](https://github.com/fweiger/AI_book/issues/25)，`version=0`、`moves=[]`、`turn=black`；由黑方网页版 AI 自行走第一手。GAME-001 仍为历史封存。
- **V2 基础路径已实现**：固定角色提示词、活动注册表、裁判按当前活动对局的 Issue/状态文件路由、终局自动清空注册表，已通过隔离测试。单次活动对局的 GAME-002 已创建；从零盘开始的真实网页版 AI 端到端对弈尚待验证。

## 两个网页版 AI 的长期固定提示词

每轮仍由各自用户在对应网页版 AI 会话中执行固定提示词，不需要每次修改“第几步、落在哪里、轮到谁”。

- [黑方 AI-A 固定提示词](prompts/AI-A-black.md)
- [白方 AI-B 固定提示词](prompts/AI-B-white.md)
- [V2 需求说明与验收门槛](V2-REQUIREMENTS.md) · [观战与操作手册](RUNBOOK.md)

两份提示词只固定角色，不写死下一盘的 Issue、身份码、游戏 ID、步数或坐标，统一从 [当前对局注册表](games/active.json) 获取权威游戏入口。

**运行流程**：当前用户唤醒自己对应的网页版 AI → 读取 `active.json` → 读取对应 `state.json` 和 Issue 评论 → 检查回合、版本、历史及未处理评论 → 自主选空位 → 在指定 Issue 只提交一行 `MOVE <身份码> <坐标>` → Python 裁判接受或拒绝 → 用户唤醒下一位网页版 AI。

当前注册表指向 GAME-002，轮到黑方 AI-A；两个角色提示词自动从 GitHub 获取最新状态，无须再次修改。若对局结束或注册表为空，双方按提示词安全退出。

## 棋谱与裁判：V1 已实现

- 15×15、黑先、无禁手，横、竖、斜五连及以上获胜，满盘平局。
- `state.moves[]` 每步记录 `number`（第几步）、`side`（颜色）、`coord`（坐标）、`comment_id`；`version` 随每步合法落子递增。
- 最新一步为 `moves[-1]`；下一手是 `len(moves)+1`，不应硬编码到提示词。
- AI 不编辑棋盘；只通过 GitHub Issue 评论提交 `MOVE 身份码 坐标`，目前裁判只接受此格式。
- `issue_comment.created` 触发 GitHub Actions/Python 裁判；按评论 ID 顺序幂等处理，检查轮次、身份码、空位和终局，更新 JSON 和 Issue。
- 裁判现在按 `games/active.json` 路由到活动游戏的独立 Issue/JSON；GAME-001 不再自动执行；目前设计是**一次仅一局活动对局**。

[裁判工作流](../../../.github/workflows/ai-book-gomoku-referee.yml) · [裁判程序](scripts/referee.py) · [棋盘规则](scripts/game.py)

## 观战与监控

- [图形观战页面源码](../../../docs/gomoku/index.html) · [GitHub Pages 工作流](../../../.github/workflows/ai-book-gomoku-pages.yml)。是否已经上线以 GitHub Pages 实际部署状态为准。
- [Ubuntu 临时监控程序](scripts/coordinator.py) · [临时运行说明](deploy/README.md)。监控只读 GitHub 状态；经授权可在裁判延迟时补触发 Actions。**不能计算落点、发布棋手评论、唤醒普通网页版 AI**。
- **本次 GAME-001 使用的 Ubuntu 临时监控 Job 已终止（`timeout`）**，无需保留系统服务。用户未要求就不得改成常驻 systemd。

## 历史资料与测试

- [GAME-001 黑方原始提示词](prompts/archive/GAME-001-A-black.md) · [GAME-001 白方原始提示词](prompts/archive/GAME-001-B-white.md)
- [完整 V1 对局结果](results/GAME-001-ACCEPTANCE.md) · [GAME-001 逐手棋力复盘与 31 条提交审计](results/GAME-001-MOVE-QUALITY-REVIEW.md)
- 本地验证：`python3 -m unittest discover -s topics/agent-games/gomoku/tests -v`

## 下一步（V2）

1. ~~创建 GAME-002 独立 Issue/空棋盘/身份码、配置裁判路由及注册表~~：已完成并经模拟测试（16 项）。
2. 使用两份**不变的网页版 AI 提示词**：先由黑方 AI-A 从空棋盘执行第一手，再轮流由白方 AI-B 执行。
3. 每一手由 GitHub Actions 自动裁判，确认棋局版本及轮次；直至终局验证自动将 `active_game` 置空。
4. 下一盘应先核验历史不可变、双方来源与新局配置信息。事件自动唤醒网页版 AI 仍未验证，不应以 CLI 替代。
