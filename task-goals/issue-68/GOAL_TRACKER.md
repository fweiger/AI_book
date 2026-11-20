# GOAL_TRACKER.md｜TOPIC-015「哲学是什么？」（唯一 L 级动态目标追踪）

> 本文件按 AI_tasks V1.2.2 试点创建。规范 Issue #68 是已批准 Goal/Scope/AC 的权威来源；本文件仅维护执行路径、检查点与唯一下一步。**M3 V0.7 逻辑修订与 H2 六案例定性压力测试已写入 Draft PR #69，正式独立哲学史审稿和最终 AC 仍未完成。**

## 任务身份

- 任务 ID：`AI-BOOK-TOPIC-015-WHAT-IS-PHILOSOPHY`
- 规范 Issue：https://github.com/fweiger/AI_book/issues/68
- 唯一源仓库：`fweiger/AI_book`
- 项目研究目录（已创建且内容 GET 回读）：`topics/what-is-philosophy/`
- 唯一 Tracker：`task-goals/issue-68/GOAL_TRACKER.md`
- Tracker 工作分支：`topic/TOPIC-015/what-is-philosophy-20261121`（不将未经审查研究内容合并至 main）
- 当前阶段：M3-04 V0.7 概念层次修订及六案例 H2 定性压力测试已提交并通过文件一致性核查；真正独立学术 Review 仍 NOT_RUN / 局部阻断
- 创建日期：2026-11-21
- 最近更新：2026-11-21（M3-04 V0.7 内容修订、六案例反论、来源和链接核查；正式独立审稿 0）
- 批准需求修订号：`r0-20261121-user`
- 协议导航：`fweiger/AI_tasks@experiment/task-center-v1.2.2-continue-goal-guard-20261119:task-center/v1.2.2/ENTRY.md`
- **锁定执行协议 commit SHA**：`f0e5ccb90c54265dcd07abb9a975c903eb031ccf`
- 最近核实的执行协议版本：`f0e5ccb90c54265dcd07abb9a975c903eb031ccf`（**此为协议锁定 SHA，不是 AI_book 工作分支 HEAD**；业务分支 HEAD 以最新 PR 读取为准）
- 最新 Issue 读取：2026-11-21，Issue #68 OPEN，已 GET 回读 Goal/Scope/AC；后续须重新核对
- Tracker 当前 blob SHA：首次创建后由 GitHub 回读获取；不在文件内自引用
- 目标偏差：D0（围绕上位哲学定义、必要/充分条件、六案例反论与如何辨认哲学推进 AC-01/02/05/06）
- 状态一致性：CONSISTENT（Issue #68 的 r0 Goal/Scope/AC 保持原样；V0.7 主答卷与六案例文件已回读；PR #69 仍 Draft/Unmerged；独立审稿 NOT_RUN；本轮 Issue 事件待同步）
- Issue 同步状态：ISSUE_SYNC_PENDING（正在以唯一 Writer 发布 M3-04 事件；不冒称已同步或正式独立审稿完成）

## 1. 批准目标基线（原文摘录，批准来源是 Issue #68）

## 1. Goal｜真正要回答的上位问题

**哲学是什么？它是否具有跨时代、跨文明、跨思想传统的共同本质？如果无法给出唯一且排他的定义，我们还能通过何种方法辨认、理解和评价哲学？**

不能先把哲学规定为一门学科、四论分类、单一推理方法或“爱智慧”的口号。应开放检验互相竞争的回答：哲学可能是一种求智慧的精神和气质、一种提问与反思的实践、一组特殊问题与论证方法、一系列历史形成的思想传统、作为知识体系的学术活动，或者这些观点的某种组合。**“难以定义”本身是研究对象，不可作为免于论证的结论。**

### 与 TOPIC-014 的层级关系（重要）

- **本专题 TOPIC-015**：研究“哲学是什么”这一**上位的元哲学问题**，不预先接受四论为哲学的完整定义。
- **既有 [TOPIC-014 #66](https://github.com/fweiger/AI_book/issues/66)**：研究本体论、认识论、价值论、方法论如何组织古今中外哲学知识及其内部关系；四论是回答本专题的**一条结构化解释路径**。
- 另可走哲学史、概念史、问题意识、哲学实践、跨文明比较、哲学与科学/宗教/文学关系等路径。它们是候选路径，不提前排成唯一层级。
- **互相引用、独立推进**：不修改或重新解释 #66 已批准的 Goal、Scope、AC；不把本专题悄悄并入 #66；不复制第二套 #66 的进度。

## 2. Scope / Non-goals

**Scope**:
1. 元哲学（metaphilosophy）与“哲学”的多重含义：词源、学科、活动、方法、生活实践、气质、历史传统。
2. 哲学与科学、宗教、文学、政治实践、日常智慧的边界及边界案例；区分描述性定义与规范性评价。
3. 跨时代、跨文明的具体原典与学术诠释：古希腊、先秦中国、近现代及必要的印度等传统；先尊重各自原生语境，再提出可比的研究问题。
4. 竞争性定义、支持论证、反对意见与难以归类的案例；研究“哲学是否需要共同本质”。
5. 从用户提供的 2026-11-19 艾维奇Vic哲学教授访谈提取**待检验问题**：爱智慧与承认无知、政治哲学与共同生活、哲学气质、内在/工具价值、技术对人类的塑造、AI与教育。此为**口语转写材料**，未经独立校对，不能冒充原著或学术定论。

**Non-goals**:
- 不用 O/E/V/M 四论预先封闭哲学定义；不替代 #66 的四论思想体系工作。
- 不把“中哲重感性/西哲重逻辑”概括当作历史定论；不预设任一文明或学派为哲学定义的唯一中心。
- 不把 AI、升学、儿童睡眠作为本题的主要经验研究或政策项目；仅在有助于澄清何为哲学时作为例子。
- 不以 AI 多数票、单次访谈、二手转述定哲学本质，不复制未经授权的访谈全文至公开仓库。
- 不未经审查直接把草稿确认为 `main` 正式知识。

## 5. AC｜可核验验收标准

- **AC-01 定义竞争性**：至少四种有明确代表来源的哲学定义/理解路径；每条包含适用对象、一个困难案例或反驳。**验证**：检查定义—来源—反例矩阵。
- **AC-02 分类与边界**：明确区分“哲学的本质”“做哲学的活动”“哲学知识分类”“学科制度”四种不同问题。**验证**：对至少三个边界案例逐一判别且列出争议。
- **AC-03 跨传统证据**：不少于三个不同时代/文明的原典样例，其中至少一个中国传统；标注版本、章节及直读/译本/二手/待核级别。**验证**：来源位置抽检，不虚构原文。
- **AC-04 多路径与旧研究隔离**：四论明确作为候选路径，与至少两种非四论路径比较；#66 Goal/AC 不改变、不重复建档。**验证**：路径矩阵和 Issue 引用回读。
- **AC-05 争议透明**：核心研究命题记录“立场→论证→反对意见→未解决点”，可保留多种竞争性答案。**验证**：至少三个完整争议单元，可由第三方复核。
- **AC-06 可持续交付**：形成有 README、问题清单、来源账本、定义/路径对照、研究结论状态的审查草稿。**验证**：PR、文件与合并状态逐项核对；不得以创建 Issue 代替验收。

**初始 AC 状态**：AC-01~AC-06 均 `NOT_RUN`；M0 的具体创建及 Tracker 状态须以真实工具回读为准。

初始 AC 状态：AC-01 至 AC-06 均 **NOT_RUN**。后续改变这些标准须由用户明确批准并更新原 Issue；不能只编辑本文件绕过批准。

## 2. 对项目的目标贡献

- 为什么值得做：避免把某套知识分类（O/E/V/M）误认为哲学的充分必要定义，保留哲学本质/定义的竞争性问题。
- 对 AI_book 的贡献：为各类哲学知识研究提供上位问题入口，按问题意识、实践、定义、方法、文明传统比较；不替换 #66 的四论工作。
- 可观察结果：多种定义及其反例、哲学边界、跨传统原典、四论与非四论路径比较、可审查论证链。
- 不可被局部替代的主线：**哲学是什么、为何难定义，以及如何审查竞争性回答**，不退化成“四论详细解释”或泛 AI 教育评论。

## 3. 当前执行路径

| 阶段 | 交付 | AC | 实际证据与核验 | 状态 |
| --- | --- | --- | --- | --- |
| M0 唯一受理 | Issue #68/Tracker | G0/G1 | 初始双向回读 | complete |
| M1 八定义与边界 | 八路径矩阵/反论 | AC-01/02/05 | definition-matrix.md 等 | partial_review_pending |
| M2 中西原典/四领域 | 六个指定原典/四边界 | AC-01–05 | three-paired-text-readings.md / boundary-stress-test.md | partial_review_pending |
| M3 元哲学立场与主答卷 | E1/E2/E3 / 综合答卷 V0.5 | AC-01/02/05/06 | metaphilosophy-positions-review.md / answer-to-what-is-philosophy.md | partial_review_pending |
| M3 独立审稿交接准备 | V0.6 四项 P0、C01–C08、J1–J6；定向来源/逻辑核验、PR 审稿通道只读核查 | AC-03/05/06 | independent-review-handoff.md、README、sources GET 回读，PR 目前 0 reviews / 0 comments / 0 threads | handoff_ready_review_not_run |
| M3 V0.7 逻辑校准/六案例 | [review-revision-v0.7.md](../../topics/what-is-philosophy/review-revision-v0.7.md) 与主答卷 V0.7；E1/E2/E3 分层，T01–T06 反向审查 | AC-01/02/05/06 | 六个文件/链接回读，原典/二手对应核查；不报告分类准确率 | content_revision_complete_review_pending |
| 独立审稿及最终验收 | 外部学术/哲学史与逻辑审查及目标验收 | AC-03/05/06 | **无实际独立审稿记录**，PR #69 DRAFT/UNMERGED | BLOCKED_EXTERNAL_REVIEW（局部阻断） |

## 4. 当前检查点

- 最近完成：2026-11-21 M3-04，新增 [V0.7 审查回应及 H2 六案例](../../topics/what-is-philosophy/review-revision-v0.7.md)，同步修订综合答卷、README、三路历史稿、V0.6 交接文件及八路径名称。
- 具体修正：L01 共通本质/必要性/充分性/排他性各自独立；L02 E1/E2 概念结构竞争与 E3-weak 历史约束、E3-strong 构成主张分层；L03 六案例含两个正例、两个构造性通常非哲学对照、两个跨界争议，H2 的独立归类能力未证明。
- 证据：PR #69 head fba94c0793a31f2c1052279f29a7e3412ddf8c62（此为 M3-04 文稿已提交时的快照；后续 Tracker 写入将更新 HEAD），V0.7 与主答卷/README/历史文稿等六份相关文件均逐项 GET 内容回读；Markdown 本地相对链接检查没有发现失效。
- 当前结论：AC-01/02/05/06 获有界实质进展，但仍 PARTIAL；AC-03 原语/文献版本校勘和印度/非洲代表性仍需外部审查；PR OPEN/DRAFT/UNMERGED；正式 PR Review=0，不得称已经完成独立同行审稿。
- 独立性：GitHub 登录 `fweiger` 与 PR 作者相同；本轮 AI 复核与内容修订不是独立 GitHub 学者审稿、没有赋予新 reviewer，也没有修改批准目标或 #66。
- 目标偏差 D0；状态一致性 CONSISTENT（Issue 原批准基线未改；进度事件本轮先 CAS 声明后同步）。

## 5. 阻断与未受影响工作

| 实际局限/风险 | 影响范围 | 受影响 AC | 能继续的工作 | 当前决定 |
| --- | --- | --- | --- | --- |
| PR #69 0 submitted review / 0 comments / 0 inline threads | 外部审稿缺失，不能宣称独立专家通过 | AC-03/05/06 最终验收 | 审稿资料与定向源校验已形成，可直接交接 | BLOCKED_EXTERNAL_REVIEW，仅阻断真正依赖外部审查的部分 |
| 审稿者指派与邀请权限未证实 | 未经授权不可邀请第三方，不能臆测有 reviewer | 外部审稿阶段 | 未来只读检查权限/审稿请求；取得授权后才提交审稿包 | REVIEW_ASSIGNMENT_UNKNOWN |
| S33/S38 仅摘要与多语原文未校勘 | 部分引文与翻译解释不具最高可信度 | AC-03 专业校勘 | 保留 B-ABSTRACT-ONLY 与 A2 分级，标明需核版本 | SOURCE_LIMITED，不重开宽泛搜集 |
| 中西精选文本和跨文明代表性不足 | 不能由六个文本断言全世界哲学的本质 | AC-01/03 | 现有结论限定为研究工作定义；未来外部审稿提反例 | GENERALIZATION_BLOCKED（外推），不阻断局部研究 |
| 只读 Spot Check 不是第二研究者独立意见 | 不能把本轮抽检打为第三方验收 PASS | AC-05/06 研究终审 | 保存详细核验动作与未完成清单 | INTERNAL_ONLY / REVIEW_NOT_RUN |

## 6. 执行路径调整记录

| 检查点 | 前一唯一优先动作 | 实际证据 | 重选的新一步 | Goal/AC 改动？ |
| --- | --- | --- | --- | --- |
| 2026-11-21 M3-01 | E1/E2/E3 钢人化 | 三路线交叉论证完成 | 单篇综合答卷 | 未改 |
| 2026-11-21 M3-02 | 主答卷/来源映射/内审 | V0.5 主答卷、C01–C08、A-01–A-12 | V0.6 审稿交接包与 P0 高风险来源复核 | 未改 |
| 2026-11-21 M3-03 | 独立审稿交接与定向源核验 | V0.6/README/sources GET，PR #69 0 submitted reviews/comments/threads | 审稿通道/授权状态确认 → 若可用才实际独立审核并回读；否则维持局部 BLOCKED | 未改 |
| 2026-11-21 M3-04 | V0.7 概念与 H2 定性测试 | 新旧文本/PR 修改可回读 | 下一步转交获授权的独立反向审稿；不继续自行重复交接包 | 未改 |

## 7. 下一步（唯一动态权威）

- **唯一优先动作**：取得已有**真实授权的独立审稿渠道/人员**后，提交 **V0.7 的 T01–T06 六案例判别、E1/E2/E3 分层与 J1–J6 原典问题** 进行第二研究者的**反向复核**，记录 `CLAIM-ID × SRC-ID × 章/版本 × 最强反例` 及真实审稿记录，并逐条评估可否修订。当前无授权/人员证据时仅保持 `BLOCKED_EXTERNAL_REVIEW`，不发外部邀请，不伪装同作者编辑为独立通过，不反复制造自审文档。
- 关联未完成 AC：AC-01/02（H2 不具备已证明的判别力）、AC-03（代表性/原文释义）、AC-05（强反例）、AC-06（独立可回读审核）。范围仅限同一 TOPIC-015，非新任务。
- 为什么优于旧下一步：用户已要求独立批判性审查，现完成 V0.7 有内容的反论修订；继续自我提议无增量，实际独立审查是当前真实依赖。不得用 PR Draft 或评论数 0 替代审稿人权限判断。
- 验收证据：与 PR/head 绑定的外部独立评审记录及对 T01–T06/J1–J6 的具体修订意见；没有则保持所有 AC 的最终验收 PARTIAL，下一动作仍等待可确认的独立渠道。

## 8. “继续”恢复检查

- [ ] 按锁定协议 SHA 读取 v1.2.2 ENTRY 与必要的同版本细则；检查是否有已有固定分配，不自动升级。
- [ ] 读取规范 Issue 的最新 Goal/Scope/AC 和评论，比较本文件基线。
- [ ] 读取唯一 Tracker 的实际 blob SHA、状态与最新分支。
- [ ] 核对 M1 定义/边界文档、原典、任何 PR 的证据与实际状态。
- [ ] 评估 D0/D1/D2/UNKNOWN 和 CONSISTENT/STATE_CONFLICT/UNKNOWN。
- [ ] 不机械继承历史建议：重新挑选最推进未完成 AC 的一个动作。
- [ ] 有实质进展时按协议单 Writer/CAS + 稳定事件键同步与回读，不能声称 exactly-once。

## 9. 追加历史

| 时间 | 真实结果 | AC 贡献 | 证据 | 状态 | 历史建议动作 |
| --- | --- | --- | --- | --- | --- |
| 2026-11-21 M0 | 独立 Issue #68 与唯一 Tracker 创建且完成双向 GET 回读 | G0/G1 建档完成，研究 AC 未运行 | https://github.com/fweiger/AI_book/issues/68 | D0 / CONSISTENT / 初始化互链 SYNCED | M1 竞争性定义及边界对照 |
| 2026-11-21 M1-01 | 八定义、四边界、四论证链、来源账本，四文件 GET 回读，Draft PR #69 创建 | AC-01..06 PARTIAL（独立审核 NOT_RUN） | https://github.com/fweiger/AI_book/pull/69 ; https://github.com/fweiger/AI_book/issues/68#issuecomment-7046201012 | D0 / CONSISTENT / SYNCED；ctext局部403不阻断其余原典 | 三对中西原典语义差异复核 |
| 2026-11-21 M2-01 | 三对中西原典按 TEXT/CONTEXT/差异/异议复核，新增三对原典文稿及 S15–S20 来源记录，均 GET 回读 | AC-03、AC-05 实质增量；全项仍 PARTIAL / REVIEW_NOT_RUN | https://github.com/fweiger/AI_book/blob/topic/TOPIC-015/what-is-philosophy-20261121/topics/what-is-philosophy/three-paired-text-readings.md ; https://github.com/fweiger/AI_book/pull/69 ; https://github.com/fweiger/AI_book/issues/68#issuecomment-7046452094 | D0 / CONSISTENT / SYNCED；语文学/独立审稿未做 | H1 四类边界反例压力测试 |
| 2026-11-21 M2-02 | H1 科学/宗教/文学/AI 四类边界压力测试；新增 H2、E1/E2/E3，来源 S21–S29；文档与账本回读 | AC-01/02/05 实质增量、AC-06 新草稿；整体仍 PARTIAL | https://github.com/fweiger/AI_book/blob/topic/TOPIC-015/what-is-philosophy-20261121/topics/what-is-philosophy/boundary-stress-test.md ; https://github.com/fweiger/AI_book/pull/69 ; https://github.com/fweiger/AI_book/issues/68#issuecomment-7046780800 | D0 / CONSISTENT；没有得出严格逻辑证伪、独立审稿 NOT_RUN | E1/E2/E3 的钢人化元哲学论证评审 |
| 2026-11-21 M3-01 | E1/E2/E3 三路钢人化，针对同一批中西原典/边界案例审查；新文稿及 README、S30–S38 来源记录 GET 回读 | AC-01/02/05/06 PARTIAL，有实质增量；独立审稿 NOT_RUN | https://github.com/fweiger/AI_book/blob/topic/TOPIC-015/what-is-philosophy-20261121/topics/what-is-philosophy/metaphilosophy-positions-review.md ; https://github.com/fweiger/AI_book/pull/69 ; https://github.com/fweiger/AI_book/issues/68#issuecomment-7046983730 | D0/CONSISTENT；桑兵文章等仅摘要，不宣称共同本质已证明 | 汇总“哲学是什么”的一份可审查答卷与证据审计 |
| 2026-11-21 M3-02 | 综合研究答卷 V0.5：A–K 11段、C01–C08 8项主张—证据—反论、A-01–A-12 内审、J1–J6 独立审稿问题；README、来源账本更新及 GET 回读 | AC-05/06 实质增量；AC-01–06 均 PARTIAL、独立审稿 NOT_RUN | https://github.com/fweiger/AI_book/blob/topic/TOPIC-015/what-is-philosophy-20261121/topics/what-is-philosophy/answer-to-what-is-philosophy.md ; https://github.com/fweiger/AI_book/pull/69 ; https://github.com/fweiger/AI_book/issues/68#issuecomment-7047225995 | D0 / CONSISTENT；修正旧元数据描述；结构与来源编号内审 PASS | PR 级独立审稿交接包与高风险来源抽检 |
| 2026-11-21 M3-03 | V0.6 独立审稿包（H01–H04/C01–C08/J1–J6），指定来源与逻辑 Spot Check；PR 正式 Review/评论/行内线程各 0，未邀请外部审稿者 | AC-03/05/06 可审查性实质增量；最终 AC PARTIAL、独立审稿 NOT_RUN | https://github.com/fweiger/AI_book/blob/topic/TOPIC-015/what-is-philosophy-20261121/topics/what-is-philosophy/independent-review-handoff.md ; https://github.com/fweiger/AI_book/pull/69 ; https://github.com/fweiger/AI_book/issues/68#issuecomment-7047445821 | D0 / CONSISTENT；独立审核部分 BLOCKED_EXTERNAL_REVIEW | 审稿授权/真实 reviewer 路由核验；无授权不得外邀 |

| 2026-11-21 M3-04 | V0.7 三个逻辑修订及六案例 H2 定性压力测试，主答卷/README/旧稿提示/八路径矩阵回读 | AC-01/02/05/06 内容实质进展；整体 PARTIAL，外审 NOT_RUN | https://github.com/fweiger/AI_book/blob/topic/TOPIC-015/what-is-philosophy-20261121/topics/what-is-philosophy/review-revision-v0.7.md ; https://github.com/fweiger/AI_book/pull/69 ; Issue 事件待同步 | D0 / CONSISTENT / ISSUE_SYNC_PENDING；没有准确率或专家 PASS | 获授权独立审稿者复核 V0.7 的非循环识别与历史跨传统反例 |

## 10. 最近状态一致性检查（动态）

- active_event_key: `AI-BOOK-TOPIC-015-WHAT-IS-PHILOSOPHY__M3__V07-LOGIC-H2-STRESS-20261121`
- writer_owner: `ChatGPT-GPT6-TOPIC015-V07-REVIEW-20261121`（GitHub 认证用户 `fweiger`；本轮逻辑事件单 Writer，非正式独立学术 reviewer）
- write_state: CLAIMED（事件发布前的 CAS 声明；GET 回读后才允许向 Issue 发布）
- tracker_sha_before_claim: `f7bd01521800e74c1c88448c1fdc2c3a3df41d78`
- pr_head_before_claim: `fba94c0793a31f2c1052279f29a7e3412ddf8c62`
- requirements_revision: `r0-20261121-user`
- protocol_commit_locked: `f0e5ccb90c54265dcd07abb9a975c903eb031ccf`
- last_completed_event_key: `AI-BOOK-TOPIC-015-WHAT-IS-PHILOSOPHY__M3__REVIEW-HANDOFF-20261121`
- last_issue_event: https://github.com/fweiger/AI_book/issues/68#issuecomment-7047445821

| 检查项目 | 实证 | 状态 |
| --- | --- | --- |
| 批准 Goal/Scope/AC | Issue #68 r0 不改；#66 不改 | CONSISTENT |
| 研究材料 | V0.7 + 主答卷/README/历史稿逐文件 GET；PR 仍 Draft | PASS_FILES |
| H2 六案例 | 两构造对照、两真实学科交叉；无盲评真值标签 | PARTIAL / NO_ACCURACY_CLAIM |
| 独立正式审稿 | PR 正式 Review = 0，未邀请外部审稿者 | NOT_RUN |
| 本轮进度事件 | `AI-BOOK-TOPIC-015-WHAT-IS-PHILOSOPHY__M3__V07-LOGIC-H2-STRESS-20261121` 正在 CLAIMED，Issue 尚未发布 | ISSUE_SYNC_PENDING |
| 唯一下一步 | 等真实获授权独立复核 V0.7；不可自授审稿资格 | D0 / BLOCKED_EXTERNAL_REVIEW |

> Tracker：https://github.com/fweiger/AI_book/blob/topic/TOPIC-015/what-is-philosophy-20261121/task-goals/issue-68/GOAL_TRACKER.md
