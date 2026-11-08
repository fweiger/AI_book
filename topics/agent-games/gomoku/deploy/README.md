# 31.5 Ubuntu · GAME-001 协调器部署手册

## 已完成的只读验收（2026-11-08）

- 31.5 Ubuntu 上 Python 3.12.3、systemd、GitHub HTTPS 联通可用。
- Codex CLI 0.159.0 已通过 ChatGPT 登录；Python 协调器已从 GitHub 克隆到 `/home/fweiger/ai_book_gomoku_coordinator`。
- 现有五子棋规则 5 项单元测试全部通过；协调器在真实 GAME-001 v3 棋盘上调用 Codex CLI，白方实际返回候选落点 `H7`，**未发表评论**。
- 尚未配置 GitHub 写入凭证，因此**没有开启自动落子常驻服务**。

## 角色分工

- 两个棋手：由 31.5 使用 Codex CLI 启动两次独立的 `--ephemeral` 调用，分别扮演黑白方；无自建模型 API，但两个角色目前使用同一个已登录 CLI 模型。
- Python 协调器：每 10 秒检查最新 `state.json` 的版本、轮次与待裁判评论；若轮到某方，启动一次 CLI 判断。
- GitHub Issue：存放双方的 `MOVE 身份码 坐标`；创建评论即触发 GitHub Actions 裁判。
- GitHub Actions：维持唯一权威状态；仅当评论超过 45 秒未处理时，协调器才选配一次 `workflow_dispatch` 补救。
- 人类观众：GitHub Pages 使用同一份 `state.json` 自动更新，无需北京或 31.5 再开 HTTP 服务。

## 只读测试

```sh
cd ~/ai_book_gomoku_coordinator
python3 -m unittest discover -s topics/agent-games/gomoku/tests -v
python3 topics/agent-games/gomoku/scripts/coordinator.py --model-timeout 90
```

第二条命令没有 `--play`，只输出候选棋步，不会修改 GitHub。

## 写入授权：须由用户在 31.5 本地设置

为 `fweiger/AI_book` 创建一个 Fine-grained GitHub PAT，至少授予 Issues: Read and write；如果需要补触发裁判 Actions，则再授予 Actions: Read and write。建议 Contents: Read-only。不要把 Token 发送到聊天或 GitHub 仓库。

```sh
install -d -m 700 ~/.config/ai-book-gomoku
${EDITOR:-nano} ~/.config/ai-book-gomoku/github-token
chmod 600 ~/.config/ai-book-gomoku/github-token
```

只有私有文件存在、用户明确准备切换全自动模式后，才启用以下服务：

```sh
mkdir -p ~/.config/systemd/user
cp ~/ai_book_gomoku_coordinator/topics/agent-games/gomoku/deploy/ai-book-gomoku-coordinator.service ~/.config/systemd/user/
systemctl --user daemon-reload
systemctl --user enable --now ai-book-gomoku-coordinator.service
systemctl --user status ai-book-gomoku-coordinator.service
journalctl --user -u ai-book-gomoku-coordinator.service -n 50 --no-pager
```

停止：`systemctl --user disable --now ai-book-gomoku-coordinator.service`。

**重要**：启用前暂停原有 ChatGPT 黑方每小时任务，以免与新协调器同时为黑方落子。目前黑方任务仍有效，白方 ChatGPT 任务未创建。

## 行为与局限

- Python 仅读取 GitHub 状态；在 `--play` 模式下，会主动用已授权 Token 发送 Issue 评论。CLI 决策使用当前机器的 ChatGPT 登录态。
- GitHub 官方建议优先使用 Webhook，10 秒轮询需通过认证、条件请求与限流；调用间隔不等于实际 10 秒落一手。
- 只有正常新评论时裁判已经自动触发；不需要每 10 秒再 `workflow_dispatch` 一次。
- `workflow_dispatch` 只启动 GitHub Actions，不会唤醒普通 ChatGPT Scheduled Task。
- 服务目前未启用；Python 是已部署、可只读验收状态。
