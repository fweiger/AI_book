# AI_book · 版本管理协议 v1.0

> **AGENTS.md 是指令与协作约定，Git 才是可回退的版本历史，GitHub 检查/分支规则用于可执行的约束**。提示词并不自动成为硬性权限控制。

## 1. 两种不同的版本

### Git commit（实际文件状态的唯一来源）

每次提交都有唯一 SHA，可查看差异、追踪贡献者、回滚。不要把“AI 表示已更新”当作成功，必须检查仓库的实际 commit。

### 专题语义版本 topic_version（表示知识结构的变化）

在每个专题的 `knowledge-graph.json` 保留 `topic_version`（例如 `0.1.0`），按 MAJOR.MINOR.PATCH：

- **PATCH**（0.1.0 → 0.1.1）：修正错别字、补出处/页码、完善已有论点的解释，原则上不新增或删除节点/关系。
- **MINOR**（0.1.0 → 0.2.0）：新增书目、重要知识节点、跨书连接、问题路线，兼容现有节点 ID。
- **MAJOR**（0.x → 1.0、1.x → 2.0）：变更核心语义/数据契约或需要迁移既有引用；必须留下旧 ID 的映射和迁移说明。

`schema_version` 是机器读取 JSON 的**文件格式**版本，独立于 `topic_version`。内容更新不应随意改变 schema_version。

## 2. 每一轮 AI 更新的要求

1. 定位专题 `TOPIC-xxx`、问题 `Qxx`、书籍 `Bxxx` 和现有论点 `Cxxx`。
2. 先检查现有内容及其来源，再决定新建还是修改；稳定 ID 不重复使用或重编号。
3. 缺少完整原文时，只允许“目录级/待核实”的知识描述，不虚构原文已验证。
4. 修改 `claims.md`、`knowledge-graph.json` 和 `knowledge-map.md` 时，保持语义一致，解释新增/变更的理由。
5. 当改动影响专题主张或结构时，更新 `topic_version` 与专题 `CHANGELOG.md`（记录日期、变化、证据级别）。
6. 每次有实质新发现，写入专题 `sessions/` 的讨论决议：AI 不同意见、来源、已达成/未达成共识、下一轮问题。
7. 更新后执行 `python3 scripts/validate_library.py`，通过后再提交 Git（代码测试不代表书籍结论为真）。
8. 非必要不重写、清空既有文件；如果需要推翻旧论点，保留修订历史和原因。

## 3. 推荐的 GitHub 工作流

- `main`：已发布/当前参考的知识库（并不保证所有论点都已实验证实）。
- `topic/TOPIC-002/2026-10-29-Q01`：某轮研究变更分支。
- 发 Pull Request，让用户/另一个 AI 对比改动与检查结果，再合并 `main`。
- 检验由 `.github/workflows/knowledge-validation.yml` 执行，调用 `scripts/validate_library.py`。
- **要真正阻止未经检查的直接推送**，还需在 GitHub 网站设置分支保护或 Ruleset：要求 PR、要求 CI 通过、禁止强推；这些不是 AGENTS.md 能自动启用的。
- 使用 GitHub commit SHA 标记每次实验快照；专题版本只用于阅读阶段的语义区分。

> 当前仓库处于初始化阶段，前几个文件直接提交到了 main。以后可按上述 PR 流程逐步收紧。

## 4. 可以自动检查 / 不能自动检查

| 自动检查可覆盖 | 不能单靠自动检查证明 |
|---|---|
| 文件是否存在、相对链接是否可解析 | 作者观点是否被正确理解 |
| B-ID / TOPIC-ID / 图谱节点唯一性 | 物理学或市场理论是否成立 |
| JSON 结构、节点与边引用 | AI 讨论是否真的形成新知识 |
| 章节状态与元数据字段的形式约束 | 文献是否有高质量、独立的实验支持 |

## 5. 来源权利

不要将本地/其他仓库的电子书批量复制到 AI_book：登记书目、原书版本、合法公开来源、短引文与原创解读即可。用户已存的书目仓库只作为索引线索，不能据此推定具有公开再分发权。

## 6. 外部投稿与讨论不等于版本更新

- GitHub Issue 的新观点、补充证据、反驳评论属于**公开讨论记录**，不是 Git 正式知识版本。
- 不要求每个 Issue 立刻生成节点/文件；长期未决的观点可以仅保存在讨论区。
- 候选通过审查后才准备 PR；PR 被成功合并后，才更新专题语义版本、记录合并 SHA 和来源 Issue。
- 外部贡献者可通过自己的 GitHub 账号发布 Issue 或使用 Fork + PR，而不是获得主库写入凭据。
- 只有聊天能力且无外部发送能力的 AI 可输出标准 Markdown 投稿包，交由用户/可信中继代发。
- 状态与审核模板详见 [CONTRIBUTING.md](CONTRIBUTING.md) 和 [discussion-review](templates/discussion-review.md)。

## 7. Discussions 类别与模板版本

- Discussion 本身是开放讨论记录，不等于正式知识库版本。
- 类别创建由 GitHub 网页端管理；仓库中的 `.github/DISCUSSION_TEMPLATE/*.yml` 只是表单配置，必须匹配类别 slug。
- 新增或修改表单时要通过 CI 的 YAML 语法检查；这只验证文件格式，不代表讨论内容已被验证。
- 类别未完成网页端创建时，必须在 [DISCUSSIONS_SETUP.md](DISCUSSIONS_SETUP.md) 中明确标记为“待手动设置”。
