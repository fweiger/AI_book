# GAME-001｜V1 对局与系统验收记录

> 来源：GitHub [Issue #24](https://github.com/fweiger/AI_book/issues/24) 与 [权威 state.json](../games/GAME-001/state.json)。本页记录 2026-11-08 已核验状态，后续不通过编辑棋谱“修正”历史。

## 最终状态（已读取 GitHub 验证）

| 字段 | 实际值 |
| --- | --- |
| `game_id` | `GAME-001` |
| `status` | `finished` |
| `winner` | `white`（白方 AI-B） |
| `version` | `30` |
| `moves` | 30 手合法落子 |
| 最后一手 | 第 30 手，白方 `J13` |
| 五连 | `F9 → G10 → H11 → I12 → J13` |
| 被拒绝的评论 | 1 条，`wrong-turn`（裁判正确拒绝） |

五连已通过 `board` 中实际白方棋子独立验证，非仅依赖胜负字段。

## 重要的实验数据口径

**前 3 手（1.B H8、2.W G8、3.B I8）是搭建和联调时由助手提交的测试落子，并非两个网页版 AI 独立作出的真实决策。** 第 4 手白方 J8 开始是用户启动网页版 AI 后的对弈阶段；因此这盘是“3 手人工测试开局 + 27 手网页版 AI 续弈”，不得当作“从空棋盘开始的 30 手纯 AI 对局”进行评价。GitHub 同一账户提交评论，单靠评论的 `author` 也无法证明独立 AI 身份。

## 已验证链路与未解决事项

- 两个用户分别操作的网页版 AI 在独立会话中读取权威 GitHub 棋局，各自决策。
- 正式落子仅通过 Issue 评论的 `MOVE <身份码> <坐标>` 协议提交；裁判验证轮次、占用、五连，成功后更新 `state.json` 和 Issue 展示。
- `moves` 中已经包含 `number`、`side`、`coord`、`comment_id`；无需额外写死最新步数或坐标到角色提示词。
- GitHub Actions 不能直接唤醒普通网页版 ChatGPT 会话；本次网页版 AI 由用户手动唤醒。
- Ubuntu 临时监控只允许读取 GitHub / 在授权时补触发裁判，**不能生成棋步或替 AI 落子**。
- GitHub Pages 是否已经成功发布，须以实际部署状态为准；不以代码已提交代替上线证明。

## 后续

- 固定棋手入口：[黑方](../prompts/AI-A-black.md)、[白方](../prompts/AI-B-white.md)。
- GAME-001 使用的原始角色提示词：[黑方归档](../prompts/archive/GAME-001-A-black.md)、[白方归档](../prompts/archive/GAME-001-B-white.md)。
- [下一版固定提示词与多棋局需求](../V2-REQUIREMENTS.md)。

**不要重置或覆盖 GAME-001 的 JSON；下一盘创建新 GAME-ID 和 Issue。**
