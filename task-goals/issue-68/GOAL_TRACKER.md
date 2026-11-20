# GOAL_TRACKER.md｜TOPIC-015「哲学是什么？」（唯一 L 级动态目标追踪）

> 本文件按 AI_tasks V1.2.2 试点创建。规范 Issue #68 是已批准 Goal/Scope/AC 的权威来源；本文件仅维护执行路径、检查点与唯一下一步。**M1 八定义、M2 中西原典与边界反例、M3 三条竞争立场和单篇综合答卷 V0.5 已具可审查稿；独立审稿和最终 AC 仍未完成。**

## 任务身份

- 任务 ID：`AI-BOOK-TOPIC-015-WHAT-IS-PHILOSOPHY`
- 规范 Issue：https://github.com/fweiger/AI_book/issues/68
- 唯一源仓库：`fweiger/AI_book`
- 项目研究目录（已创建且内容 GET 回读）：`topics/what-is-philosophy/`
- 唯一 Tracker：`task-goals/issue-68/GOAL_TRACKER.md`
- Tracker 工作分支：`topic/TOPIC-015/what-is-philosophy-20261121`（不将未经审查研究内容合并至 main）
- 当前阶段：M3 综合答卷 V0.5 + C01–C08 证据—异议对照 + A-01–A-12 内审已产出；下一阶段为 PR 级来源核验与独立审稿交接，不代表已审过
- 创建日期：2026-11-21
- 最近更新：2026-11-21（M3 完整答卷、内部一致性审计及 Draft PR #69 文件回读）
- 批准需求修订号：`r0-20261121-user`
- 协议导航：`fweiger/AI_tasks@experiment/task-center-v1.2.2-continue-goal-guard-20261119:task-center/v1.2.2/ENTRY.md`
- **锁定执行协议 commit SHA**：`f0e5ccb90c54265dcd07abb9a975c903eb031ccf`
- 最近核实的执行协议版本：`f0e5ccb90c54265dcd07abb9a975c903eb031ccf`（**此为协议锁定 SHA，不是 AI_book 工作分支 HEAD**；业务分支 HEAD 以最新 PR 读取为准）
- 最新 Issue 读取：2026-11-21，Issue #68 OPEN，已 GET 回读 Goal/Scope/AC；后续须重新核对
- Tracker 当前 blob SHA：首次创建后由 GitHub 回读获取；不在文件内自引用
- 目标偏差：D0（本轮将前四轮材料收敛为直接回答原 Goal 的单篇文稿与可反驳证据矩阵，增量支持 AC-05/06；未偏离至四论/AI 教育）
- 状态一致性：CONSISTENT（Issue #68 r0 Goal/Scope/AC 未改；正文/README/来源账本 GET 回读；更正历史遗留的“研究目录未创建/协议 SHA 误标分支 HEAD/旧 CLAIMED”状态描述）
- Issue 同步状态：SYNCED（本轮综合答卷 Issue 事件 #7047225995 的唯一稳定键经 GET 回读只出现一次；前四轮均已 SYNCED；不表示学术验收）

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

| 阶段 | 交付 | AC | 可追溯证据 | 状态 |
| --- | --- | --- | --- | --- |
| M0 受理 | 唯一 Issue #68 与 Tracker 双向回链 | G0/G1 | 初始 GET 回读记录 | complete |
| M1 解释竞争 | 八定义、四边界、四种论证单元 | AC-01/02/05 | definition-matrix.md；boundary-and-arguments.md | partial_review_pending |
| M2 跨传统与边界 | 三组中西原典；科学/宗教/文学/AI 反例 | AC-01–05 | three-paired-text-readings.md；boundary-stress-test.md | partial_review_pending |
| M3 三路钢人化 | E1/E2/E3 的最强论证/反驳及 H2 限定 | AC-01/02/05 | metaphilosophy-positions-review.md | partial_review_pending |
| M3 综合交付初稿 | **answer-to-what-is-philosophy.md**；C01–C08 主张映射、A-01–A-12 内审、J1–J6 独立审稿问题 | AC-05/06 | 文档已 GET，README、sources S01–S38 互引核验；PR #69 OPEN/DRAFT/UNMERGED | partial_review_pending |
| M3 独立审查 | 外部研究者源证据复核、逻辑异议处理、验收/合并判断 | AC-03/05/06 | 当前未发生专业独立审稿或 main 合并 | NOT_RUN |

## 4. 当前检查点

- 最近完成一轮：2026-11-21 M3-02，“哲学是什么”完整综合研究答卷与内部一致性审计。
- 真实完成：新增 `topics/what-is-philosophy/answer-to-what-is-philosophy.md`，11 个 A–K 主题段落；从教授“爱智慧”到中西六个原典指定段、四领域边界反例、E1/E2/E3、H2、四论关系的直接回答；C01–C08 八条来源/论证/最强异议/信度审计，A-01–A-12 十二项内审，J1–J6 独立审稿问题；README 索引、sources 账本与 S33 2019刊期/2020网页日期差异明确更新；3 个文件全部 GET 回读，现有 PR #69 仍 OPEN/DRAFT/UNMERGED。
- 实际内部校验：文档 A–K/Claims/审计编号全部存在；引用的 Markdown 文件路径均能解析至本分支；C01–C08 引用的 S01–S38 编号均存在来源账本；对易错原典/元数据抽检：柏拉图《申辩》21d、SEP Wittgenstein §3.4、SEP Mohism 标准、SEP Experimental Philosophy 以及桑兵期刊官方摘要；**这不等于逐 URL 验证 38 个来源或专家同行审稿**。
- 本轮主结论：哲学可被工作性理解为反思世界、知识、判断与生活根据的多样思想实践。描述性/规范性/制度性含义须区分；哲学与科学、宗教、文学可能重叠，“爱智慧”解释动机而非排他界限；E1/E2/E3 和 H2 仍是竞争性解释/比较协议，**跨文明唯一本质 OPEN**，不能宣称不可定义已证。
- 修正实证状态冲突：旧身份区曾错误写“目录规划尚未创建”及把协议 SHA 写成“观察业务分支 HEAD”；§4 历史语句“CLAIMED/待回读”不再适用于上一轮已 SYNCED 事件。本轮已纠正，历史事件仍在 §9 留档。
- 对 Goal/AC：原批准 Goal/Scope/AC 未变，AC-05/06 形成显著可审查初稿，AC-01–04 沿用前四轮有来源证据；**AC-01–06 依然 PARTIAL，独立审核 NOT_RUN**。
- 本轮目标偏差 D0；状态 CONSISTENT；Issue 事件按 §10 单 Writer 原子文件 SHA/CAS 声明后唯一发布。
- 主要未完成：独立哲学史/逻辑审稿、逐来源精度深抽检与原语言/古籍校勘、印度/非洲等更多传统代表性、对反论的外部评判、最终验收/合并。

## 5. 阻断与未受影响工作

| 阻断/未验证处 | 真实范围 | 所影响 AC | 当前可继续工作 | 处理决定 |
| --- | --- | --- | --- | --- |
| 原典有多语翻译与传本问题 | 未完成古希腊/德/拉丁/俄原文语文学以及先秦古籍版本校勘 | AC-03/05 终审可信度 | 已标 A1/A2/B/C/R 的内部引用、源精度抽检 | 明示 NOT_RUN，不以英译等同原语校勘 |
| 桑兵论文 S33、道家批评哈多论文 S38 仅见摘要 | 只支持摘要级陈述，不能推断其正文具体论证 | AC-03/05 的个别来源 | 综合答卷仅引用 S33 摘要所述译名/历史区分 | 保持 B-ABSTRACT-ONLY |
| 案例有意选样，且未有印度/非洲等高质量原典对照 | 无法推广成跨全球的共同哲学本质 | AC-01/03 | 结论限定为已研究中西若干文段与争议 | 标 GENERALIZATION_BLOCKED，不虚报普遍定论 |
| 缺少真正外部独立哲学史/逻辑审稿 | 项目完整验收不能 PASS | AC-05/06 | 准备好 J1–J6 的审稿清单与主张—证据—异议表 | 只称内部核查，不称独立审稿/合并 |
| 旧 Tracker 元信息失真（目录尚未创建、协议 SHA 误标业务 HEAD、旧 CLAIMED） | 治理状态文本与 GET 已核真实文件不符 | 管理状态一致性 | 本轮以同一 Tracker SHA/CAS 更正 | 修复后回读，历史 §9 不擦除 |

## 6. 执行路径调整记录

| 日期 | 原唯一下一步 | 本轮实际完成 | 重决策的新动作 | AC/Goal 对齐 | 需求有无变更 |
| --- | --- | --- | --- | --- | --- |
| 2026-11-21 M2-01 | 三对中西原典 | 已形成三对指定段研究稿 | H1 边界压力 | AC-03/05，Goal 不变 | 否 |
| 2026-11-21 M2-02 | H1 四领域边界审查 | 已得严格定义尚无证据、非排他性与逻辑限定 | E1/E2/E3 钢人化 | AC-01/02/05 | 否 |
| 2026-11-21 M3-01 | E1/E2/E3 最强论证/反驳 | 已形成钢人化三路线全文与来源 | 单篇综合答卷+内部审计 | AC-05/06 | 否 |
| 2026-11-21 M3-02 | 单篇答卷与来源一致性 | 新增 V0.5、C01–C08/A-01–A-12/J1–J6、README/sources 回读，PR 未合并 | **PR 级高风险主张独立复核准备包** | AC-03/05/06，直达审稿而非无限搜集 | 否 |

## 7. 下一步（唯一动态权威）

- **唯一优先动作**：围绕 `answer-to-what-is-philosophy.md` 的 **C01–C08、J1–J6** 完成一份 **PR 级独立审稿交接与高风险来源核验包**：逐主张列关键引用、版次/证据级别、最强反论、抽样核查结果、明确哪些需要外部专家；针对 C02 中西语义等同、C03 译名/历史论文仅摘要、C05 维特根斯坦家族相似的非原文类比及 C04 逻辑边界优先复核。文件准备可以直接做，但**独立专家审稿必须真实发生才能标 PASS**。
- 对应未完成 AC：AC-03（代表性/文本定位抽检）、AC-05（竞争性论证的独立可核查性）、AC-06（审稿交接和正式验收准备）。
- 价值：当前已经给出直接回答与跨材料审计；与其继续堆更多哲学家，不如让审稿者能精确追溯八条主张、针对四个高风险点提出反对意见，从而决定是否修订 H2 或仍开放定义问题。
- 预期交付：`independent-review-handoff.md`，核心 claim→来源类型→异议→核查任务→责任/完成证据的审稿核验包；独立审稿栏保留 `NOT_RUN` 直至实际审稿意见/身份/时间/原典比对可回读。
- 必要先读取：Issue #68 Goal/AC、本 Tracker 最新 blob、锁定协议、PR #69 与综合答卷/S01–S38 来源账本。
- 不得自动扩展：另建 Issue、重复四论模块、邀请未经授权的外部人员、改写已批准 AC、在未核原文时声称“专家认同”或直接合并 main。
- 止损/阻断：某一私有/收费论文打不开，记录摘要级别而转向现有开放原典，不在局部 403 死循环；一轮之后如无实质独立审稿权限或源可读性，交付准备包并明确阻断。

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

## 10. 最近状态一致性检查（动态）

- active_event_key: none（AI-BOOK-TOPIC-015-WHAT-IS-PHILOSOPHY__M3__INTEGRATED-ANSWER-20261121 已发布、回读、结束）
- writer_owner: none（本轮完成并清理）
- write_state: SYNCED（事件 #7047225995 单一稳定键经 GET 回读；GitHub 评论接口本身不保证 exactly-once）
- last_completed_event_key: `AI-BOOK-TOPIC-015-WHAT-IS-PHILOSOPHY__M3__INTEGRATED-ANSWER-20261121`
- last_issue_event: https://github.com/fweiger/AI_book/issues/68#issuecomment-7047225995
- last_claimed_tracker_sha: `59869c69161457c4f1c4316c315440a5732f07be`
- previous_completed_event_key: `AI-BOOK-TOPIC-015-WHAT-IS-PHILOSOPHY__M3__E1-E2-E3-20261121`
- previous_issue_event: https://github.com/fweiger/AI_book/issues/68#issuecomment-7046983730
- 旧 Writer fencing：不适用；本轮与历史 Writer 均已回读完成，没有活动 Writer；未来若出现未知写入结果仍须按协议核查和 fencing，禁止自动抢占。

| 检查项 | 可回读证据 | 状态 |
| --- | --- | --- |
| 批准 Goal/Scope/AC | Issue #68 r0 未修改；TOPIC-014 #66 仍独立 | CONSISTENT |
| §3 实际研究文件 | 综合答卷/README/sources 均 GET，PR #69 当前 OPEN/DRAFT/UNMERGED | CONSISTENT |
| §4 结论与证据 | C01–C08 来源编号、A01–A12 内审；无外部学术审核 | PARTIAL / INTERNAL_CHECK_PASS |
| §5 阻断范围 | 桑兵等仅摘要、原语校勘/印度等未覆盖；不阻断下一 PR 级审稿包 | CONSISTENT |
| §6 路线与 §7 下一步 | 单篇答卷已完成，下一步为审稿包，避免重复“继续写答卷” | CONSISTENT |
| §9 历史建议 | 历史内容只能作恢复参考，§7 唯一当前动态动作 | CONSISTENT |
| 本轮 Issue 同步 | #7047225995 经 GET 回读单一 event_key；当前活动 Writer 清理 | SYNCED |
| 独立哲学史审核与最终验收 | 尚未执行，无合并、无外部审稿 | NOT_RUN |

> Tracker：https://github.com/fweiger/AI_book/blob/topic/TOPIC-015/what-is-philosophy-20261121/task-goals/issue-68/GOAL_TRACKER.md
