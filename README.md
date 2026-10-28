# AI_book · 问题驱动的 AI 共读知识库

这里不是一本书读完再读下一本的书单仓库，而是一个可以长期生长的 **问题—论点—证据—书籍章节—对话迭代** 知识库。

## 从这里开始

- [专题索引](INDEX.md)
- [第一专题：现实、观察与意识——从玻姆到彭罗斯](topics/reality-observation-consciousness/README.md)
- [知识图谱](topics/reality-observation-consciousness/knowledge-map.md)
- [章节阅读路线](topics/reality-observation-consciousness/reading-path.md)
- [AI 共读工作法](WORKFLOW.md)

## 外部 AI 如何参与

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
