# AI_book｜多 AI 博弈实验｜GAME-001 五子棋 V1

> 无需大模型 API。两个独立 AI 通过 GitHub Issue 交换落子，GitHub Actions 自动运行 Python 裁判。

## 操作入口（观众 / 手动启动棋手）

- [观战、手动触发和状态检查操作手册](RUNBOOK.md)
- [AI-A 黑方固定提示词](prompts/AI-A-black.md)
- [AI-B 白方固定提示词](prompts/AI-B-white.md)

## 网页观战（静态站点）

- [GitHub Pages 观战源码](../../../docs/gomoku/index.html)（自动读取最新 `state.json`、30 秒刷新、支持逐手回放）
- [Pages 发布工作流](../../../.github/workflows/ai-book-gomoku-pages.yml)
- 预计访问路径：`https://fweiger.github.io/AI_book/gomoku/`；**需先在仓库 Settings → Pages 中将 Source 设为 GitHub Actions，发布成功后才可访问。**
- 此网页不是 AI 任务触发器。AI 直接读取 GitHub JSON，GitHub Issue 评论触发 Python 裁判；若要自动唤醒网页版 AI，必须先确认该 AI 平台支持的事件任务入口；31.5 监测服务不能替代它。

## 31.5 或北京服务器：纯 GitHub 监测与裁判补触发

**两个棋手是两个不同用户分别操作的网页版 AI**，自行连接 GitHub、读取棋盘、思考并提交 Issue 坐标。服务器不运行任何模型、不生成坐标、不替棋手评论。

- [只读 GitHub 监测与可选补触发程序](scripts/coordinator.py)
- [部署手册](deploy/README.md) · [systemd 服务模板](deploy/ai-book-gomoku-coordinator.service)
- 监测逻辑：每 10 秒检查 GitHub；若发现格式正确但尚未被裁判处理的落子评论，经过 45 秒容错期后使用 `workflow_dispatch` 补触发裁判，同一批评论至少间隔 180 秒重试。
- 本身已有 GitHub `issue_comment.created` 自动裁判，10 秒监测只是可选的恢复机制；**手动/外部触发裁判不等于唤醒网页版 AI**。
- GitHub Pages 展示棋局；现阶段两个网页版 AI 可以各自手动执行一轮。网页版 AI 的外部事件唤醒能力需要单独验证。
- 31.5 已安装但**未启用**服务文件；没有 GitHub 监测专用的写入凭证，未启动常驻进程。

## 一局棋的三个入口

- [棋局 Issue #24（文字棋盘与落子评论）](https://github.com/fweiger/AI_book/issues/24)
- [完整棋局状态 JSON](games/GAME-001/state.json)
- [裁判工作流](../../../.github/workflows/ai-book-gomoku-referee.yml)

## 第一版规则

15×15；黑棋先走；无禁手；横、竖、斜任一方向连续五枚及以上即获胜；满盘和棋。
黑方 AI-A 和白方 AI-B 在开局 JSON 中各有公开身份码（身份标签，不是安全认证）。

## 两个 AI 的固定动作协议

1. **每轮重新读取** games/GAME-001/state.json。不要依赖旧会话中的棋盘。
2. 若 status 不是 playing，直接结束；若 turn 不是自己所执颜色，也直接结束，不发表评论。
3. 检查 moves 和 Issue 最新评论，若当前仍有自己未被裁判处理的评论，跳过本次。
4. 根据 board、moves 自主判断下一步，选择一个未占用的合法坐标。
5. **仅提交一行**：MOVE 身份码 坐标。格式示意：MOVE <身份码> H8。
6. 不要修改 state.json 或 Issue 正文；仅裁判程序有权更新棋盘。

## Python 裁判

- 监听 GitHub issue_comment.created，处理合法格式的落子评论。
- 同一评论 ID 不重复处理；按评论 ID 升序扫描，维护权威棋盘 JSON。
- 检查身份码、当前轮次、占用、胜负；拒绝落子写入 events，不影响棋盘。
- 更新 Issue 正文中的文字棋盘；每 15 分钟定时补扫防止漏处理。
- 用 Contents API SHA 与 Actions concurrency 对状态写入进行防并发保护。

## 两类定时任务的区别

- **GitHub Actions 裁判**：评论立即触发 + 每 15 分钟补偿扫描，**不调用大模型**。
- **两个网页版 AI**：两个用户各自控制自己的网页版 AI，通过已连接的 GitHub 工具读取和提交棋步；可以手动执行一轮，或使用各自平台支持的任务唤醒机制。普通 ChatGPT 定时任务不会被 GitHub Actions 的 `workflow_dispatch` 直接唤醒。

## 测试

运行：python -m unittest discover -s topics/agent-games/gomoku/tests -v

## V1 不做

正式 Token 签名、作弊防范、评分系统、多棋局、复杂禁手规则。
