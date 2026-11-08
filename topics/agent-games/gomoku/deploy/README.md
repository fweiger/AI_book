# Ubuntu MCP / 31.5｜临时 GitHub 棋局监测（不作为系统服务）

> 用户约束：**仅允许临时启动、完成后关闭；不创建或启用 systemd 常驻服务，不通过 Codex CLI 等工具替网页版 AI 落子。** Ubuntu 不是两个网页版 AI 的宿主。

## 职责与限制

- 两位棋手分别是**两个用户各自操作的网页版 AI 会话**，读取 GitHub 并独立选择棋步。
- Ubuntu 上的 `scripts/coordinator.py` 仅轮询指定 GitHub Issue / 状态，用于检查裁判是否处理评论；经过授权时可以对 GitHub Actions 的 **Python 裁判**执行 `workflow_dispatch` 补偿。
- 不调用外部模型、不产出坐标、不发布任何 `MOVE` 评论、不直接修改棋谱或 Issue 正文。
- 监控不是必要条件：Issue 评论本身已配置 `issue_comment.created` 自动裁判；裁判另有 15 分钟补扫。
- GitHub Actions 的调度 API **不能唤醒普通网页版 AI 会话**，两位棋手仍由各自用户唤醒。

## GAME-001 本次临时监测的真实结果

- 既有临时 Job（`ce5c816c-44e7-4ca4-b2b6-783a0f8ec51e`）已结束，终态为 `timeout`，没有作为服务继续常驻运行。
- GAME-001 已白方获胜，`status=finished`，30 手。当前无需再运行 GAME-001 监控。
- 原来错误添加的 `systemd` 方案已被用户明确否定；以后不应将临时棋局监测改造成服务。
- 当前 `coordinator.py` 仍针对 GAME-001 的固定 Issue 路径；**V2 多棋局监测适配未实现**，不能直接用于 GAME-002。

## 如需临时诊断（一次性，只读）

在 Ubuntu MCP 上执行：

```bash
cd ~/ai_book_gomoku_coordinator
git pull --ff-only
PYTHONDONTWRITEBYTECODE=1 python3 topics/agent-games/gomoku/scripts/coordinator.py
```

一次只读检查不会修改 GitHub；已结束时会正常退出。

## 临时轮询（必须明确要求才运行）

不配置 GitHub Token 时，为避免 GitHub 匿名 REST 限流，可按较低频率人工临时启动，**不得后台自启或注册系统服务**：

```bash
PYTHONDONTWRITEBYTECODE=1 python3 -u topics/agent-games/gomoku/scripts/coordinator.py --loop --interval 180
```

结束时在当前终端按 `Ctrl+C`，或停止对应的 Ubuntu MCP Job。超过设置的临时任务运行期限也会自行退出。**不添加 `--dispatch` 时只读监测**。

若未来确需 10 秒检测和有权限的 `workflow_dispatch` 故障补偿，可单独配置最小权限的 GitHub Token（Contents read、Issues read、Actions write），再经用户明确批准以临时 Job 运行；不得把 Token 提交到仓库或日志。监测功能与模型对弈仍然完全分离。

## 双方固定提示词及 V2

- [黑方固定提示词](../prompts/AI-A-black.md) / [白方固定提示词](../prompts/AI-B-white.md)
- [当前对局注册表](../games/active.json)（目前 `active_game=null`，无进行中新局）
- [下一版对局路由与验收需求](../V2-REQUIREMENTS.md)
