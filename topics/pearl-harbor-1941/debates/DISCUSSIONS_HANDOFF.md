# 将 DEBATE-001 正式发布为 GitHub Discussions 的操作说明

当前GitHub连接支持建立Issue、评论、文件和PR；**未暴露`createDiscussion`发帖动作**。因此已先创建真正可供两个AI讨论的 [Issue #18](https://github.com/fweiger/AI_book/issues/18)，两份领题评论与裁判规则已发布；**不冒称原生GitHub Discussion已创建**。

## 已就绪的原生Discussion材料

1. [完整辩题、共享史料链接和比较边界](DEBATE-001-brief.md)。
2. [正方领题](PRO-FIRST-STRIKE.md) 与 [反方领题](PRO-LIMITED-WAR.md)，两方可直接分别复制发言模板。
3. [裁判流程](REFEREE.md) 和 [证据卡](EVIDENCE_LEDGER.md)。

## 在GitHub网页直接发布一次（有账户权限的用户或授权浏览器代理）

1. 打开 [AI_book Discussions](https://github.com/fweiger/AI_book/discussions)，选择 **New discussion**。
2. 类别优先选择已有的 **Evidence Challenges**（如果列表中没有，则选择 General 或开放型类别；类别是否已实际创建需要网页确认，不要凭YAML模板假定存在）。
3. 标题：`[DEBATE-001][TOPIC-004] 1941南进战略：先对美开战 vs 只攻英荷｜双AI史料辩论`。
4. 正文：复制 [DEBATE-001-brief.md](DEBATE-001-brief.md) 全文，添加 [Issue #18](https://github.com/fweiger/AI_book/issues/18) 作为R0已有讨论/证据档案的双向链接，保留所有原始资料链接。
5. 发帖后在Discussion下分别添加正反方任务书；再将**真实**Discussion URL贴回 [Issue #18](https://github.com/fweiger/AI_book/issues/18) 和本文件。未经创建，不预填虚构URL。
6. 双方R1和R2在**一个实际指定的讨论主帖**继续，避免Issue和Discussion同时收集不同版本的立论。记录迁移时点，保留原Issue作为历史痕迹。

## 通过GitHub CLI / API代替网页（仅在环境具备已授权认证时）

GitHub CLI 2026年起提供 `gh discussion create`：[官方文档](https://cli.github.com/manual/gh_discussion_create)，例如使用 `--repo`、`--title`、`--category`、`--body-file`。也可调用已授权的GitHub GraphQL `createDiscussion(repositoryId,categoryId,title,body)`：[官方文档](https://docs.github.com/en/graphql/guides/using-the-graphql-api-for-discussions)。

**不要向任何外部AI提供GitHub个人令牌**；使用各自授权的账户/最小权限App。当前会话连接的GitHub操作不包含这一mutation，因此这里仅提供公开的受权操作路径，不声称已执行。

## 人类/AI身份管理

从ChatGPT/Codex/其他AI将立论带到GitHub，必须由模型自己已连接的授权GitHub接口发布，或由用户**明确注明代贴**。评论显示的是Github登录者，不自动证明AI作者身份；保留 `MODEL / RELAYED_BY` 元数据。