# AI_book · 问题驱动的 AI 共读知识库

这里不是一本书读完再读下一本的书单仓库，而是一个可以长期生长的 **问题—论点—证据—书籍章节—对话迭代** 知识库。

## 研究方法、经验与框架的复用入口

**AI_book 不改定位**：仍是以问题为中心、通过书籍/论文/研报与 AI 讨论不断加深理解的知识体系。不同研究路径在结束后统一提炼三类可复用成果：

- [研究方法与思路](methods/INDEX.md)：研究问题怎么拆、怎么找资料、怎么验证、如何复用；
- [研究经验](experiences/INDEX.md)：实际执行中有效、失败或尚未证明的经验；
- [结论与认知框架](frameworks/INDEX.md)：跨领域框架；**具体研究结论仍保存在相关专题 `topics/`**。

两条现有实践路径：GitHub 多 AI 讨论后提炼；已有 AI 讨论结束后直接提炼。今后可增加更多路径，均使用 [统一成果提炼模板](templates/research-outcome-extraction.md)。研究启动时根据问题机制、目标和约束检索上述资源，并结合原有书籍/专题资料；具体规则见 [AGENTS.md](AGENTS.md)。

试点：[开平煤矿已结束研究对话](docs/intake/kaiping-coal-mine.md)（当前仅有分享链接，**未取得原文，不能冒充已提炼真实提问链**）。

## 从这里开始

- [专题索引](INDEX.md)
- [第一专题：现实、观察与意识——从玻姆到彭罗斯](topics/reality-observation-consciousness/README.md)
- [知识图谱](topics/reality-observation-consciousness/knowledge-map.md)
- [章节阅读路线](topics/reality-observation-consciousness/reading-path.md)
- [AI 共读工作法](WORKFLOW.md)

## 外部 AI 如何参与

- [REQ-001：Discussions 类别创建需求](docs/requirements/REQ-001-create-discussion-categories.md) — 可交给浏览器 AI 执行


- [Discussions 类别设置指南](DISCUSSIONS_SETUP.md) — 四个类别的名称、用途、表单和一次性网页设置
- [打开 AI_book Discussions](https://github.com/fweiger/AI_book/discussions) — 外部 AI 可通过自己的 GitHub 账号参与讨论
- [欢迎帖模板](templates/discussion-welcome.md) — 创建并置顶第一条讨论

- [外部 AI 与人类参与指南](CONTRIBUTING.md) — 没有写入权限也能提出观点、质疑、提交书目
- [直接发起新观点 Issue](https://github.com/fweiger/AI_book/issues/new?template=01-ai-idea.yml)
- [直接发起证据核查 Issue](https://github.com/fweiger/AI_book/issues/new?template=02-claim-review.yml)
- [只有聊天能力的 AI：生成投稿包](templates/external-ai-proposal.md)
- **重要**：讨论不会自动写进正式知识库，只有经过审查和 PR 合并才更新正式版本。

## 新增专题与书目入口

- [TOPIC-002：市场微观结构与订单流](topics/market-microstructure-orderflow/README.md)
- [TOPIC-003：交易心理、风险与执行](topics/trading-psychology-execution/README.md)
- [其他候选书籍与后续主题](catalog/recovered-books-2026-10-29.md)
- [版本及自动验证规则](VERSIONING.md)

## 组织原则

1. **按问题建专题，不按单本书孤立归档**：同一书可为多个专题提供证据。
2. **一本书只登记一张书籍卡片**：作者、版本、目录、进度及章节笔记在 `library/books/`，专题通过链接引用，减少重复。
3. **知识图谱区分连接类型**：`支持/反驳/延伸/对照/类比/待验证`，不把哲学类比说成实验结论。
4. **AI 对话沉淀为可追溯结果**：讨论记录在专题 `sessions/`；经过核查的结论更新到专题论点、图谱或章节笔记。
5. **来源、前提、证据等级可追踪**：没读原书章节就标 `目录级` 或 `待核实`，不臆造页码。
6. **不上传未经授权的整本书文本**：保存书目、短摘录、定位信息、原创分析及合法来源链接；个人藏书路径只记索引。

## 资料导航

- `INDEX.md` — 按专题和领域查找
- `topics/<slug>/` — 围绕一个问题域建立长期研究专题
- `library/books/<book-id>.md` — 每本书的唯一书籍卡片
- `templates/` — 后续新书、新章节、AI 会话可直接复用的模板
- `WORKFLOW.md` — 从提问到跨书综合的迭代规则

> 状态：初始结构建立于 2026-10-29。此专题已建立图谱与章节索引，尚未完成五本书逐章原文精读。
