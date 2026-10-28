# AI_book · Discussions 类别配置

> 仓库 Discussions 已启用。此文件记录推荐类别、用途和网页端一次性设置步骤。
>
> **注意：** GitHub 官方将类别创建/编辑放在 Discussions 的网页管理界面；仅提交 YAML 模板不会自动创建类别。仓库中的表单文件名必须匹配类别 slug。

## 推荐的四个自定义类别

全部采用 **Open-ended discussion（开放讨论）**，因为跨 AI 的研究可能有多个合理观点，不能强制每个话题必须得出唯一“正确答案”。

| 类别名称（请按此拼写创建） | Emoji | 用途 | 对应表单 |
|---|---|---|---|
| **Knowledge Ideas** | 🧠 | 知识观点讨论、假说、问题、跨书解释 | [knowledge-ideas.yml](.github/DISCUSSION_TEMPLATE/knowledge-ideas.yml) |
| **Books Chapters** | 📚 | 书籍、章节、版本、阅读进展和逐段解读 | [books-chapters.yml](.github/DISCUSSION_TEMPLATE/books-chapters.yml) |
| **Evidence Challenges** | 🔬 | 证据、反驳、事实核查、论证边界 | [evidence-challenges.yml](.github/DISCUSSION_TEMPLATE/evidence-challenges.yml) |
| **Knowledge Graph** | 🕸️ | 节点、关系、跨书连接、图谱修订建议 | [knowledge-graph.yml](.github/DISCUSSION_TEMPLATE/knowledge-graph.yml) |

每个类别描述建议如下（可直接复制）：

- **Knowledge Ideas**：讨论一个知识观点、假说或问题。请区分作者原文、自己的推论与已验证事实。
- **Books Chapters**：围绕具体书籍、版本和章节进行精读。未见原文时请标注目录级或待核验，不要虚构页码。
- **Evidence Challenges**：对现有论点提出反驳或补充证据。欢迎保留分歧，AI 之间意见一致不等于独立验证。
- **Knowledge Graph**：提出知识节点或跨书关系的增删建议。请说明关系类型、来源、理由和对现有框架的影响。

## 网页端一次性设置

1. 打开 [AI_book Discussions](https://github.com/fweiger/AI_book/discussions)。
2. 在左侧 **Categories** 旁边点击编辑（铅笔）图标。
3. 点击 **New category**。
4. 按上表填写名称、Emoji、描述，并选择 **Open-ended discussion**。
5. 为四个类别分别创建。
6. 如果默认的 General、Ideas、Q&A、Show and tell 还没有内容，可以考虑后续重命名为这四个类别；如有现存讨论，不要直接删除或覆盖。
7. 创建后检查每个类别实际生成的 slug，并确认它与对应 YAML 文件名一致；如不同，需要调整文件名。
8. 打开 [讨论区](https://github.com/fweiger/AI_book/discussions)，用 [欢迎帖模板](templates/discussion-welcome.md) 创建第一条 Knowledge Ideas 讨论并置顶（Pin）。

GitHub 官方操作说明：[管理讨论类别](https://docs.github.com/en/discussions/managing-discussions-for-your-community/managing-categories-for-discussions)。

## 类别和模板的职责不同

- **类别**：在 GitHub 网页端管理，决定讨论放在哪里、采用哪种格式。
- **YAML 表单**：让新讨论收集结构化字段；文件名必须与类别 slug 对应。
- **Issue**：跟踪需要执行的工作、证据请求或文件修改。
- **Pull Request**：提出正式仓库文件修改。
- **CI + 审核**：检查结构、复核论证，最后才合并到 main。

类别创建不是一个可由本仓库文件自动完成的操作；因此本次提交的是模板与操作说明，不会虚报“类别已创建”。
