# GAME-001｜31.5 GitHub 状态监测与裁判补触发（不替 AI 下棋）

## 正式需求与边界

**两个棋手是两个用户各自操作的网页版 AI**。它们分别连接 GitHub，读取 `state.json`，独立判断棋步，并在 Issue #24 中留言 `MOVE 身份码 坐标`。

31.5（或北京服务器）只承担 GitHub 协调辅助功能：检测 GitHub 提交和裁判状态，必要时调用 GitHub `workflow_dispatch` 补触发**现有 Python 裁判**。它**不调用、不启动、不代替任何 AI**；不负责生成坐标、不发布落子评论。

完整流程：网页版 AI A / B → GitHub Issue 评论 → GitHub Actions Python 裁判 → JSON 棋谱 → GitHub Pages 观众页面。31.5 旁路监测 Issue 评论与 JSON；只有裁判没有及时处理时补触发 Actions。

## 已部署与测试背景

- 31.5 为 Ubuntu，Python 3.12.3、systemd 可用，可正常访问 GitHub API。
- 项目路径：`/home/fweiger/ai_book_gomoku_coordinator`。
- 之前错误加入的 Codex CLI 生成棋步功能已经**从 `scripts/coordinator.py` 删除**，原 systemd 文件也已修改为只监控 GitHub。
- `ai-book-gomoku-coordinator.service` 安装但保持 `disabled / inactive`，**没有启动常驻监测，也没有修改 GAME-001 棋谱**。

## 每 10 秒轮询如何工作

1. 请求 GitHub REST API 读取现有 GAME-001 的 `state.json` 和 Issue #24 的评论。
2. 读取 JSON 中的 `processed_comment_ids`，找出没有被裁判处理、且格式符合 `MOVE 身份码 坐标` 的评论。
3. 正常情况下评论创建就会触发 GitHub Actions；监控程序等待默认 **45 秒**，避免重复执行。
4. 超时后才在明确启用 `--dispatch` 的情况下调用 GitHub `workflow_dispatch`，并对相同待处理评论设置至少 **180 秒冷却期**。
5. 监控进程不会发布任何评论、不会更改 `state.json`、不会写入棋局，也不会触发网页版 AI 的会话。

## 启动前的 GitHub 权限

10 秒轮询和 `workflow_dispatch` 需要 31.5 上配置 GitHub Fine-grained PAT，仅选择 `fweiger/AI_book`，建议 Contents（Read-only）、Issues（Read-only）、Actions（Read and write）。**不需要 Issues 写入权限，也不需要任何模型 API Key。**

请在 31.5 本机安全配置，不要在聊天、Issue、仓库或日志中粘贴 Token：

```bash
install -d -m 700 ~/.config/ai-book-gomoku
${EDITOR:-nano} ~/.config/ai-book-gomoku/github-token
chmod 600 ~/.config/ai-book-gomoku/github-token
```

## 先做只读运行

```bash
cd ~/ai_book_gomoku_coordinator
python3 -m unittest discover -s topics/agent-games/gomoku/tests -v
python3 topics/agent-games/gomoku/scripts/coordinator.py
```

不加 `--dispatch` 或 `--loop` 时，只做一次 GitHub 检查，不修改远程任何数据。

## 10 秒常驻监测

需要在本机凭证准备完成后才使用以下步骤：

```bash
mkdir -p ~/.config/systemd/user
cp ~/ai_book_gomoku_coordinator/topics/agent-games/gomoku/deploy/ai-book-gomoku-coordinator.service ~/.config/systemd/user/
systemctl --user daemon-reload
systemctl --user enable --now ai-book-gomoku-coordinator.service
journalctl --user -u ai-book-gomoku-coordinator.service -f
```

停止：`systemctl --user disable --now ai-book-gomoku-coordinator.service`。

服务没有 GitHub Token 时会拒绝 10 秒轮询，避免匿名 GitHub API 限流。GitHub Actions 自身已经可以自动响应 Issue 评论，因此监控器是**可选的可靠性补偿**，不是必需的棋局执行器。

## 网页版 AI 如何开始下棋？

两个独立网页版 AI 的固定提示词仍分别位于 `../prompts/AI-A-black.md` 和 `../prompts/AI-B-white.md`。目前可以分别手动让它们运行一轮；若以后要由 GitHub 事件主动唤醒网页版 AI，需要其平台提供被支持的任务/连接器事件入口。

**31.5 调用 `workflow_dispatch` 只能启动 GitHub Actions Python 裁判，不能直接唤醒普通网页版 ChatGPT 会话或其现有每小时任务。** 这是尚未打通的产品能力，不得把监控程序说成完成了双 AI 自动唤醒。
