# AI_book 五子棋｜网页版 AI 对弈操作手册（V1 完成 / V2 规划）

## 当前实情（2026-11-08 验证）

- **GAME-001 已结束**：`status=finished`、`winner=white`、30 手，详情见 [验收记录](results/GAME-001-ACCEPTANCE.md)。棋局不能继续提交 MOVE。
- 目前 [active.json](games/active.json) 中 `active_game=null`，表示无已启动的新对局。
- 新版固定提示词文档已落地，但**GAME-002、裁判多棋局路由、活动棋局自动切换仍未开发**。本页不能当作已开新棋局的证明。
- GAME-001 的 [Issue #24](https://github.com/fweiger/AI_book/issues/24) 和 [权威状态](games/GAME-001/state.json) 永久作为本次实验历史。不要重置。

## 双方网页版 AI 的统一操作

在两个**用户分别操作的独立网页版 AI 会话**中，一次粘贴各自的固定提示词，之后每次要走棋只需说“按固定提示词执行一轮”：

- [黑方 AI-A 的正式固定提示词](prompts/AI-A-black.md)
- [白方 AI-B 的正式固定提示词](prompts/AI-B-white.md)

两份文档的角色不同，但读取、验证、提交过程一致：

1. 重新读取 `games/active.json`，确认存在已创建并登记的 `active_game`。
2. 从注册表读取 `game_id`、`issue_number`、`state_path`，获取权威 JSON 和该 Issue 的评论；**不能使用旧会话的步数或落子位置**。
3. 检查棋局 `status=playing`，`turn` 等于己方颜色，且己方没有尚未处理的 MOVE 评论。
4. 从 `moves[-1]` 得到最新一步（`number / side / coord`），从 `len(moves)+1` 得到下一手序号；再分析空位、进攻、防守，**由该网页版 AI 自己决定落点**。
5. 发评论前重新检查活动游戏、版本、轮次和空位；仅在当前游戏 Issue 发表一条 `MOVE <身份码> <实际坐标>` 评论。身份码来自 JSON 的 `players.black.token` 或 `players.white.token`，不在提示词中写死。
6. Python 裁判接受评论后，JSON 版本递增、轮次切换；由用户手动唤醒另一方网页版 AI，直至终局。
7. `active_game=null`、游戏已结束、没轮到自己、评论未处理、GitHub 数据异常等情况必须停止，不下棋。

**固定提示词不需要随每一手编辑**。需要改变的仅是下一局启动时的对局注册表和裁判配置；对局中的步数、位置、轮次和身份码均为 GitHub 动态数据。

## 下一局创建步骤（当前属于 V2 未完成）

在实际使用固定提示词玩下一局之前，必须先实现并通过测试：

- 新建独立 GAME-ID、Issue、空棋盘 state、双方身份码；不可复用 GAME-001 的棋谱/Issue #24。
- 完成 Python 裁判 / GitHub Actions 对新游戏 Issue 与 state 路径的绑定与正确路由，具备严格的防串局校验。
- 再更新 `games/active.json.active_game` 指向新游戏。一次仅允许一个活动棋局时，必须保护注册表变更的一致性。
- 用户验证 Issue 与棋盘无误后，才分别启动两位网页版 AI。
- 结束后裁判写入 `finished` 并由生命周期控制完成结果归档、注册表清空，确保不再对已结束棋局提交。

上述是需求和交付检查清单，**不是声称已经实现新对局自动创建**。详见 [V2-REQUIREMENTS.md](V2-REQUIREMENTS.md)。

## 观战

- [GAME-001 历史 Issue](https://github.com/fweiger/AI_book/issues/24)：文字棋盘、棋谱、评论和裁判记录。
- [网页观战源码](../../../docs/gomoku/index.html) 与 [Pages 工作流](../../../.github/workflows/ai-book-gomoku-pages.yml)：网站是否已发布必须从 Pages 部署状态核实；静态页面不是 AI 唤醒器。
- [GAME-001 当时使用的原始黑白提示词](prompts/archive/) 单独归档，可以核实历史操作，不应当作为下一局模板。

## 裁判与监测的区别

- GitHub Issue 的 `issue_comment.created` 事件直接启动 **GitHub Actions Python 裁判**，扫描评论、校验落子、更新状态；已有每 15 分钟兜底扫描。
- 手动 [Run workflow](https://github.com/fweiger/AI_book/actions/workflows/ai-book-gomoku-referee.yml) 只能运行裁判，不能启动 AI 或创造棋步。现有裁判仍绑定 GAME-001。
- Ubuntu 临时监测可只读检查 GitHub、必要时在授权范围内补触发裁判；不得调用模型或代替网页 AI 落子。**不启用 systemd 常驻服务**；既有临时 Job 已结束。
- GitHub / Actions / Pages 无法凭空唤醒普通网页版 ChatGPT 会话；若将来要求事件自动交接，必须研究实际受支持的产品触发方式并单独验收。
- 黑方此前存在每小时定时棋手任务的历史配置；如果将来从空棋盘重开，应核实该任务当前是否启用，避免与两个网页 AI 手动测试产生重复动作。本文不擅自修改任何定时任务。

## 快速复现本次历史对局

1. 读取 [GAME-001 最终 state.json](games/GAME-001/state.json) 及 Issue #24，确认 `finished`、30 手、白方五连。
2. 核对胜方实际五连 `F9-G10-H11-I12-J13`，以及前 3 手是系统测试而不是双方网页版 AI 从零开始的决策。
3. 阅读 [验收记录](results/GAME-001-ACCEPTANCE.md)；不要用历史棋盘重新落子。
4. 如需重新对弈，请按 V2 新开 GAME-ID，先通过裁判与注册表的联调再激活。
