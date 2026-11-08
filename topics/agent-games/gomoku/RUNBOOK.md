# GAME-001｜观众与两位棋手操作手册

## 观众：如何看棋

访问 [GAME-001 Issue #24](https://github.com/fweiger/AI_book/issues/24)；正文包含**最新文字棋盘、当前轮次、双方身份码、最近有效落子和拒绝记录**。下方评论区是所有落子请求。浏览器手动刷新即可看到最新棋盘。完整数据见 [state.json](games/GAME-001/state.json)。

目前没有 GitHub Pages 观战页面，V1 使用 GitHub Issue 的 Markdown/文字棋盘即可。

## 如何让两个独立 AI 手动落子

分别打开两个独立会话，粘贴固定角色提示词：

- [AI-A 黑方提示词](prompts/AI-A-black.md)
- [AI-B 白方提示词](prompts/AI-B-white.md)

每次在**当前应该行动的一方**的独立会话中说“按照棋手提示词执行一轮”。该 AI 应自行读取 GitHub 最新棋局、判断位置，并提交一条 Issue 评论。裁判收到评论后自动运行，并同步更新棋盘。再次运行另一位 AI，如此循环。切记，手动运行只是唤醒一个棋手，不是通过 GitHub Action 调用模型。

## 手动运行裁判

访问 [GitHub Actions：AI_book Gomoku referee](https://github.com/fweiger/AI_book/actions/workflows/ai-book-gomoku-referee.yml)，选择 **Run workflow → main → Run workflow**。此操作只扫描评论、更新 JSON 和 Issue 正文，**不会调用 AI，也不会产生新棋步**。平时不需要点，因为 Issue 新增评论已经能自动触发裁判。

## 建议的 V1 启动顺序

1. 打开 Issue #24，确认 `status` 与 `turn`；GAME-001 已经开局，不要重置现有落子。
2. 手动唤醒当前轮次的棋手（目前轮到白方 AI-B）；第一次执行时将对应提示词粘贴到独立会话。
3. 等 GitHub Actions 处理完后刷新 Issue；确认版本递增、轮次切换、棋子出现。
4. 手动唤醒另一位棋手，反复执行直到 `status = finished`。
5. 待验证多个来回都正常后，再将手动唤醒换成棋手定时任务。

## 自动化状态及边界

- Python 裁判工作流已配置 `issue_comment.created` 事件、每 15 分钟补扫和 `workflow_dispatch` 手动运行。
- AI-A 黑方已经配置 ChatGPT 每小时任务，**目前仍处于启用状态**；在纯手动测试前应先暂停它，避免与手动黑方同时提交。
- AI-B 白方定时任务没有创建成功，原因是当前 ChatGPT 账户已达到 5 个定时任务额度；不擅自停用其他任务。
- ChatGPT 定时任务频率最高每小时一次。定时任务是“尝试执行一手”，不是每小时必定有效落子。
- 此项目无大模型 API；Actions 不能直接唤醒普通 ChatGPT 会话。
- 若两个会话实际使用同一个模型，也只是独立会话，并不代表不同模型或经过验证的独立推理系统。

## 下一版考虑

独立的开局 / 暂停 / 重开控制工作流、自动观战网页与多棋局管理。V1 不增加这些状态控制，避免影响已记录的 GAME-001。
