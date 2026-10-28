# AGENTS.md — AI_book 的共读规则

本仓库用于长期积累**问题驱动**、**来源可追溯**的跨书知识图谱。修改前优先阅读 `README.md`、`INDEX.md`、`WORKFLOW.md`，再阅读当前专题的 `README.md`、`questions.md` 和 `claims.md`。

## 工作原则

1. 从专题 Q-ID 开始，不强制读完一本书再切换问题。新书在 `library/books/` 注册唯一 B-ID；同一书不要在多个专题重复复制。
2. **没有原始章节就不能声称“已精读”**。公开目录、二手转述和原书亲自阅读必须分别标注来源级别。
3. 对原文的解读应包含作者问题、概念定义、前提、论证步骤、反例/反对意见、结论局限和定位来源。禁止虚构页码、引文、定理细节或实验结果。
4. 观点的“支持/反驳/发展/类比/对照/待验证/禁止直接推断”等图谱关系需要显式类型。尤其不可把量子纠缠、心理观察者、哥德尔定理、微管假说混合成已验证的因果证明。
5. 提炼出来的新结论先落在 `claims.md` 的稳定 C-ID，再同步更新 `knowledge-map.md` 和 `knowledge-graph.json`。现有节点 ID 尽量稳定，不随意改名或删除。
6. 每轮有实质结果时写入 `topics/<slug>/sessions/YYYY-MM-DD-<主题>.md`：起始问题、阅读来源、证据级别、新旧判断差异、更新的文件和未解问题。
7. AI 模型之间意见一致不能算独立实验验证；有争议的观点需保留最强反对解释，避免空泛讨论。
8. GitHub 仓库是公开的；**不得上传私有地址、个人设备路径、凭据、受版权保护的整本书或大段未经授权原文**。保存书目、必要短引文、章节定位、原创分析及合法访问链接。

## 启动当前专题

- 专题：[TOPIC-001](topics/reality-observation-consciousness/README.md)
- 下一轮具体任务：[NEXT.md](topics/reality-observation-consciousness/NEXT.md)
- 章节模板：[chapter-analysis.md](templates/chapter-analysis.md)
- 对话模板：[ai-session.md](templates/ai-session.md)

结束一次阅读任务时，请明确报告：**读了哪些原文 / 没读哪些原文；改了什么文件；改变哪些 C-ID/节点；下次从哪里继续**。
