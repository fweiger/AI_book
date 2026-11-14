# AI_book 索引自动审计（只读）

权威实施任务：[AI_book #62](https://github.com/fweiger/AI_book/issues/62)。原始索引：[INDEX.md](../INDEX.md)。Task Center 只保存该 Issue 导航，不复制研究进度。

## 目标与日程

- GitHub Actions 定时触发：每天 **UTC 01:30 / 北京时间 09:30**（GitHub 不保证精确执行时刻），还可以手动 `workflow_dispatch`。
- PR 触发只运行 Python 单测和现有知识库结构校验，**不会误把 PR 分支的文件当成 main 上已正式入库**。
- 工作流进入 `main` 后，定时/手动运行才会通过只读 GitHub API 获取 `main` SHA、完整文件树、全部 Issues 和全部 PR（按 100 条分页）。
- 报告位置：每次 Action 的 **Step Summary** + artifact `ai-book-index-audit-<run_id>`，包含 `report.md` 和 `report.json`，保留 30 天。
- 工作流仅申请 `contents:read`、`issues:read`、`pull-requests:read`；**不修改** INDEX、Issue/PR 状态，不自动创建新 Issue，不自动合并 PR，也不恢复已迁出的公开内容。

## 检查范围与分类

| 代码 | 解释 | 操作 |
| --- | --- | --- |
| `missing_main_topic` | main 已存在知识图谱，但 INDEX 的 MAIN 专题表遗漏 | 审核后补入索引 |
| `incorrect_main_claim` | INDEX 的 MAIN 专题不存在对应 main 图谱 | 判断是错误归类还是迁出 |
| `missing_root_issue` / `missing_root_pr` | 顶层专题 Issue / 未合并 PR 没有索引链接 | 审核是否需纳入研究表；子级 H、CASE 不按顶层计 |
| `stale_pr_state` | 已合并、已关闭或从 Draft 变成 Ready，但索引仍声明 Draft/Open | 更新文本；不得直接变更研究结论 |
| `possible_topic_id_collision` | 同一 TOPIC 编号有多个不同的顶层 Issue 或多条活跃研究 PR | **仅人工审查**：可能是一个项目的多条 PR，也可能是编号冲突 |
| `duplicate_main_topic_id` | main 下不止一份图谱使用同一 TOPIC ID | 检查重号，修复时保留历史映射 |
| `migrated_topic_reappeared` | INDEX 明确标注迁出，但 main 又出现同号图谱 | 暂停恢复行为，先确认迁移授权 |
| `broken_local_link` | 仓库内 Markdown 的相对路径不存在/逃逸仓库根 | 修复链接或删除坏引用 |

这些是**索引结构审计**，不验证外部 HTTP 地址是否仍可访问、论文原文内容、历史史实、医学结论或 PR 内尚未合并的文件链接。

## 本地使用

```bash
# 在 AI_book 仓库根目录；GitHub CLI 不必安装。
python3 -m unittest discover -s scripts/tests -p 'test_audit_topic_index.py' -v
python3 scripts/validate_library.py

# 可联网/有授权 Token 时，建议从 main checkout 执行
GITHUB_TOKEN="${GITHUB_TOKEN}" python3 scripts/audit_topic_index.py \
  --root . --repo fweiger/AI_book --out-dir dist/index-audit

# 离线模拟：fixture.json 必须包含 main_sha、tree、issues、pulls 四项
python3 scripts/audit_topic_index.py --root . --fixture fixture.json
```

### 失败与审查约定

API 403、超时、分页过多、主分支树截断、checkout SHA 与 main 不一致或 JSON 格式异常时，脚本退出码 **2 / AUDIT_INCOMPLETE**；此时不可称作“没有问题”。完整报告存在，但发现待审核差异时，退出码仍为 **0**，避免阻止本应由人工判断的警告项。必须阅读 `report.json` 中的 `status` 与 `findings`。

涉及多分支编号冲突（如 TOPIC-004）只列证据、不擅自分配新编号；明确迁出的 TOPIC-009 不因历史已合并 PR 被重新恢复。首次上线时，优先人工复核扫描基线，之后再考虑通知提醒或安全自动创建索引修复草稿 PR。

### 回滚

上线前：关闭本 Draft PR；上线后：移除或禁用 `.github/workflows/index-audit.yml` 即停用定时扫描。脚本与 Action 没有索引写权限，既有研究内容不受影响。
