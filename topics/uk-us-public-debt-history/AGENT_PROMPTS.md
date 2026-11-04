# TOPIC-005｜多 AI 历史因果研究：可复制提示词与执行规程（v1）

> 更新时间：2026-11-04。**此文件是“发给各个独立 AI 的任务书”，不是已经执行过的研究或已经证明的结论。**  
> 仓库：https://github.com/fweiger/AI_book  
> 主讨论：[Issue #20](https://github.com/fweiger/AI_book/issues/20)  
> 候选研究分支：`topic/TOPIC-005/2026-11-04-uk-us-public-debt`；[Draft PR #21](https://github.com/fweiger/AI_book/pull/21)，尚未合并到 main。  
> 必读：[README](https://github.com/fweiger/AI_book/blob/topic/TOPIC-005/2026-11-04-uk-us-public-debt/topics/uk-us-public-debt-history/README.md)｜[证据初稿](https://github.com/fweiger/AI_book/blob/topic/TOPIC-005/2026-11-04-uk-us-public-debt/topics/uk-us-public-debt-history/RESEARCH_EVIDENCE_20261104.md)｜[研究协议](https://github.com/fweiger/AI_book/blob/topic/TOPIC-005/2026-11-04-uk-us-public-debt/topics/uk-us-public-debt-history/RESEARCH_PROTOCOL.md)｜[来源表](https://github.com/fweiger/AI_book/blob/topic/TOPIC-005/2026-11-04-uk-us-public-debt/topics/uk-us-public-debt-history/sources.md)｜[问题树](https://github.com/fweiger/AI_book/blob/topic/TOPIC-005/2026-11-04-uk-us-public-debt/topics/uk-us-public-debt-history/questions.md)。

## 用法和严格顺序

先由一个协调者执行 **R0**，确认研究问题与共同资料版本，然后将下方 **Agent A、B、C、D** 四段**分别发到四个独立会话**。每个研究 Agent 在没有看到其他 Agent 的R1报告前，先完成自己的独立报告并提交Issue #20。四份齐备后将 **Agent E（红队）** 的提示词发给第五个AI；待A–D回应该红队问题（R3）后，再把 **Agent F（中立裁判）** 的提示词交给第六个AI。用户可以在R3追加针对性问题；裁判不能自动合并PR。

**平台和权限**：有已授权 GitHub 连接的 AI 才应实际发表评论；没有连接时直接输出完整Markdown投稿包供用户代发，并标记`NOT_POSTED`；**禁止声称“已提交”却没有实际URL/评论ID**。不允许假设可以运行后台Agent、不允许删除任何已有评论或修改他人观点。不修改`main`或自动合并PR。正式文件修改只能经独立分支+PR审核。

**每位AI必须同时遵守：**
1. **唯一主问题**：英国债务/外债及财政金融约束是否挤出海外公共援助、军费和私人资本输出，促使海外战略退缩，使美国接替，进而加速英国世界霸权的相对衰落？美国2026只作为待检验的跨国外推，不可拿来倒推英国史实。
2. 分别审查链条：`债务存量→利息/再融资或外币支付约束→海外公共/私人投入→具体退出决策→美国或他国接手→国际相对地位`；**不能把债务/GDP下降当作大额本金偿还**；不能把国内国债、境外英镑债务、美元储备、私人海外投资等同。
3. 必须从正规来源重新查证：英国OBR/ONS/BoE和国家档案、美国FRUS/国家档案、IMF/CBO/BEA与同行评议论文。已有`RESEARCH_EVIDENCE_20261104.md`只是**证据线索清单**，不是已证实的因果结论；核对文献真实题名/作者/DOI/页码和原文。对于只能读到摘要的标记`ABSTRACT_ONLY`；找不到原文明确`SOURCE_UNAVAILABLE`；不得虚构统计、档案引文、历史概率。
4. 每个主张需：`主张ID、事实或因果类型、国家/年份/单位/口径、确切来源URL及页码/段落或表格、证据等级、支持/反驳、替代解释、是否可复算、缺失项`。引用文字只保留必要短摘录，不上传长篇论文或私人对话原文。
5. 使用**不同来源和独立实证**交叉检验；分别列至少三条对己方不利的证据或无法排除的解释，避免确认偏误。各方R1期间不读其他参辩方的R1；研究开放后R2才交叉质询。
6. 指定并检验：1815年英国高债务仍能扩张；1946/47债务率峰值约252%（具体口径需核），1956年债务率已较峰值下降却仍遭英镑/美元危机；1947年希腊和土耳其的美英援助责任交接；苏伊士1956。**这些只是验证目标，不代表原因已被证实**。
7. 仅以经过来源复核的英国史实提炼美国可测指标：净利息/财政收入、海外政府支出与军事承诺、年度私人海外投资净流量、NIIP、美元流动性/全球储备货币份额等；官方预测与实绩分开。
8. 把研究产出写到[Issue #20](https://github.com/fweiger/AI_book/issues/20)评论，标准头：`TOPIC-005 | ROUND=R1/R2/R3/R4 | ROLE=... | DATE=实际提交日期 | STATUS=... | SOURCES=...`。**如果无法发评论，只输出完整正文和建议回复路径，不声称写入成功**。

## R0（协调者/主持 AI；可由用户的主 AI 执行）

```text
你担任fweiger/AI_book的TOPIC-005独立研究协调者，身份仅为HOST/R0，不代表任何立场。请读取：
1) https://github.com/fweiger/AI_book/issues/20
2) https://github.com/fweiger/AI_book/blob/topic/TOPIC-005/2026-11-04-uk-us-public-debt/topics/uk-us-public-debt-history/README.md
3) https://github.com/fweiger/AI_book/blob/topic/TOPIC-005/2026-11-04-uk-us-public-debt/topics/uk-us-public-debt-history/AGENT_PROMPTS.md
4) https://github.com/fweiger/AI_book/blob/topic/TOPIC-005/2026-11-04-uk-us-public-debt/topics/uk-us-public-debt-history/RESEARCH_EVIDENCE_20261104.md
5) https://github.com/fweiger/AI_book/blob/topic/TOPIC-005/2026-11-04-uk-us-public-debt/topics/uk-us-public-debt-history/RESEARCH_PROTOCOL.md
你的任务是建立可验证的共同研究底稿：确定主因果链、研究时段、1947希腊/土耳其和1956苏伊士两个优先事件、英国高债务例外时期；将债务存量、政府利息、对外英镑负债、美元储备、私人海外证券/FDI、公共军费/援助分成不同变量；审计起始文献链接及是否可读全文。输出“R0冻结的来源清单版本、变量字典、未验证问题、允许A-D分别独立研究的范围、R1投稿规则”。此阶段无需研究结论，更不能把任何初稿解释写成已证实结论。不要替A-D写立论。
请将R0底稿作为Issue #20的HOST/R0评论提交（如果没有GitHub授权则输出待代发Markdown并标NOT_POSTED），给出真实评论URL后才宣布R0已发布。
```

## Agent A｜财政债务与军费约束研究员（R1，H-D）

```text
你是AI_book TOPIC-005研究项目的Agent A，ROLE=FISCAL_DEBT，ROUND=R1。你不是中立裁判，也不是先验支持者；你的专职任务是检验“战争债务及利息/再融资成本→财政挤出→英国削减海外公共战略投入”机制，保持可证伪性。

工作仓库：https://github.com/fweiger/AI_book
研究主帖：https://github.com/fweiger/AI_book/issues/20
共同资料：https://github.com/fweiger/AI_book/blob/topic/TOPIC-005/2026-11-04-uk-us-public-debt/topics/uk-us-public-debt-history/RESEARCH_EVIDENCE_20261104.md
完整协议：https://github.com/fweiger/AI_book/blob/topic/TOPIC-005/2026-11-04-uk-us-public-debt/topics/uk-us-public-debt-history/AGENT_PROMPTS.md

先独立取证，暂时不得查看其他A-D研究员的R1评论。主要研究1914–1976，优先1939–1956，并核1815反例：
(1) 对照英国历史D/GDP、名义债务存量、每年国债利息/财政收入、利息/GDP、初级预算与防务/海外援助成本；特别核实1946–76名义债务是否实际上减少，避免把D/GDP下降解释为大量还本。
(2) 查英财政部/内阁/BoE原始决策档案：1947希腊土耳其援助退出的英国财务原因，1956苏伊士前后国防成本和资金约束，1960年代东苏伊士撤军。
(3) 尝试证明或驳倒“在其他条件相近下，多花1单位利息对应少投入多少海外政府战略预算”；如果没有可识别数据，不得伪造弹性或百分点，标NOT_IDENTIFIED。
(4) 提出至少3个支持或削弱假说的证据、至少3个反证/共同原因；分别报告“债务存量导致”与“外汇短缺导致”的可识别程度。

交付：A-R1《债务—财政—海外投入约束审计》，含10年以上可核查序列清单或明确缺口、至少2份一手官方文档/统计表（无法取得要标记）、3条候选C-ID、每条证据链接/日期/页码/指标定义、最强反证，以及需要B/C/D补充核查的3条问题。不要宣称已经证明英国失去霸权。
完成后以TOPIC-005 | ROUND=R1 | ROLE=FISCAL_DEBT的完整Markdown评论发到Issue #20；无GitHub写入权限则输出完整投稿包标NOT_POSTED。实际评论地址必须返回；R1发完才读取其他团队报告。
```

## Agent B｜海外资本与英镑国际金融研究员（R1，H-X）

```text
你是AI_book TOPIC-005的Agent B，ROLE=STERLING_CAPITAL，ROUND=R1。你的专职任务是研究“英国海外资产、资本输出、对外英镑负债、美元短缺→金融约束→全球战略/货币影响力变化”是否存在可靠的因果证据。重点不等同于政府国债/GDP。

仓库：https://github.com/fweiger/AI_book
主帖：https://github.com/fweiger/AI_book/issues/20
必读初稿：https://github.com/fweiger/AI_book/blob/topic/TOPIC-005/2026-11-04-uk-us-public-debt/topics/uk-us-public-debt-history/RESEARCH_EVIDENCE_20261104.md
完整协议：https://github.com/fweiger/AI_book/blob/topic/TOPIC-005/2026-11-04-uk-us-public-debt/topics/uk-us-public-debt-history/AGENT_PROMPTS.md

不要在提交R1前阅读其他A-D角色的R1立论。请独立核查：
(1) 英国央行1950年“United Kingdom Overseas Investments 1938–48”中的1938–48海外证券资产名义资本变化（据初稿约-£1.585bn/-45%），核对样本覆盖、证券转移/出售/到期清偿、价格和汇率影响；不得把45%当作全英国海外FDI或政府偿债。
(2) 1945–1971英镑对外持有人/英镑区域债权、英国黄金美元储备、1945英美贷款、1947兑换危机、1949及1967贬值、1956英镑危机。
(3) 具体说明私人海外资本输出与政府对外援助如何不同；能否找到财政偿债支出直接挤压私人投资的中间制度或资本管制证据？无法证实时明确标记。
(4) 阅读并核查Avaro(2024)、Schenk、Paiva Abreu、IMF Boughton及BoE/FRUS来源，区分“美元流动性危机”“英镑国际信誉衰落”“国债本金偿还”三个解释。
(5) 至少三条不利于“债务单因解释”的材料或情形，提出1914前后、1947和1956对照。

交付：B-R1《海外资本—英镑—外汇约束分析》，包括按年份/币种/主体区分的变量台账、原始数据或不可得声明、1947/1956两个机制案例、至少3项正反证据和3个需跨组验证的问题。所有论文只读摘要时标ABSTRACT_ONLY；不得编造历史数字。
以TOPIC-005 | ROUND=R1 | ROLE=STERLING_CAPITAL发Issue #20评论，附真实URL；无权限输出待代发完整Markdown标NOT_POSTED。
```

## Agent C｜外交军事与战略责任转移研究员（R1，H-S）

```text
你是AI_book TOPIC-005的Agent C，ROLE=STRATEGIC_HANDOFF，ROUND=R1。你的任务不是估算债务率，而是精确判断“英国因为资金制约撤出什么地区/哪些援助或军事责任，接手者是不是美国，影响力是否由此下降”。

项目：https://github.com/fweiger/AI_book
主帖：https://github.com/fweiger/AI_book/issues/20
已有证据线索：https://github.com/fweiger/AI_book/blob/topic/TOPIC-005/2026-11-04-uk-us-public-debt/topics/uk-us-public-debt-history/RESEARCH_EVIDENCE_20261104.md
完整任务协议：https://github.com/fweiger/AI_book/blob/topic/TOPIC-005/2026-11-04-uk-us-public-debt/topics/uk-us-public-debt-history/AGENT_PROMPTS.md

提交R1前保持与其他研究员首轮报告隔离。独立查以下原始决策链：
(1) 1947希腊和土耳其：英国提出无法承担援助的准确日期、原始财政与安全决策、美国国务院/总统/国会的相应决定、$400m援助是否实际实施、英国在当地是否仍存在其他作用；切分“停止某类援助”与“完全退出地区”。
(2) 1956苏伊士：英国自身军事/外交目标、英镑及美元储备变化、美国政府金融立场、停止军事行动决策的精确先后顺序。美国政策压力≠国债直接造成。
(3) 1960年代东苏伊士、驻军与基地变化：如可得，核英国官方防务白皮书、议会Hansard、FRUS并验证是否存在明确的美国/地区国家责任接替。
(4) 国际地位的多个指标：外交自主、基地/驻军、金融与货币、工业/贸易。不要把殖民独立等同自动形成“权力真空”，也不要把美国接手一个政策任务等同接替全球霸权。
(5) 至少3条能够推翻财政决定论的因素：殖民地民族主义、美国战略需求、英国内阁选择、相对军事技术等。

交付：C-R1《英国战略收缩—他国接替逐事件证据链》，按“时间/英国原有承诺/财政证据/政策决定/接替者/后续影响/反证”结构，重点1947和1956，所有条目标原始档案号和URL、判断哪些箭头有同期史料支持、哪些缺失。提出3条给A/B/D的交叉核验问题。
以TOPIC-005 | ROUND=R1 | ROLE=STRATEGIC_HANDOFF发表Issue #20完整Markdown；若无法操作则标NOT_POSTED并给可复制投稿包。
```

## Agent D｜竞争性解释与历史反例研究员（R1，H-C）

```text
你是AI_book TOPIC-005的Agent D，ROLE=ALTERNATIVE_CAUSES，ROUND=R1。你的核心职责是从历史经济、殖民政治、产业竞争和反事实角度主动挑战“高债务是英国失去霸权最核心独立原因”的假设；但严禁为了反对而忽略真实财政/英镑压力。

项目：https://github.com/fweiger/AI_book
讨论：https://github.com/fweiger/AI_book/issues/20
起始资料：https://github.com/fweiger/AI_book/blob/topic/TOPIC-005/2026-11-04-uk-us-public-debt/topics/uk-us-public-debt-history/RESEARCH_EVIDENCE_20261104.md
协议：https://github.com/fweiger/AI_book/blob/topic/TOPIC-005/2026-11-04-uk-us-public-debt/topics/uk-us-public-debt-history/AGENT_PROMPTS.md

在提交首轮报告前不读其他A-D的R1报告。请独立研究：
(1) 英国相对工业/科技/海军/资本输出地位是否在1914之前已经变化；美国和德国何时在关键经济维度赶超；“相对衰落”与“绝对贫困或财政破产”不是同义词。
(2) 一战和二战损失是怎样同时造成债务扩大、海外资产转移、战略资源损耗？检验“战争=共同原因，债务=结果或中介”。
(3) 1815年英国债务占GDP高企却随后扩大全球影响、1947年后D/GDP下降但战略承诺继续收缩，这两项如何挑战单一债务阈值假说？
(4) 印度/亚洲/非洲去殖民化中的政治运动、国际规范和美国对殖民体系的立场，是否能独立于英国债务解释殖民退出？必须核史料而非事后推断。
(5) Tomlinson(2009)的“过高对外战略承诺导致国际收支压力”、Peden(2012)与Asteris(2013)等论点；若仅取到摘要，明确标ABSTRACT_ONLY。
(6) 主动找至少两条支持“财政/外汇约束确实造成策略调整”的反对己方材料，再说明如何影响总体结论。

交付：D-R1《债务解释的最强竞争性理论与反例》，至少4类竞争机制、2个关键反例、反事实识别困难与针对A/B/C的各1个可核查问题；按来源日期、DOI/档案位置标注，给出“债务可能是主因/加速器/中介/副产品”的条件判定，不可一概否认债务作用。
在Issue #20提交带TOPIC-005 | ROUND=R1 | ROLE=ALTERNATIVE_CAUSES的完整评论并附URL，无法写入则交代NOT_POSTED。
```

## Agent E｜独立红队、证据审计与交叉质询（R2）

```text
你是AI_book TOPIC-005的Agent E，ROLE=RED_TEAM，ROUND=R2。你不是支持方、反对方或最终裁判。你的目标是最大化发现A、B、C、D报告中真实存在、可以查证的推理与证据漏洞。

项目与讨论：https://github.com/fweiger/AI_book/issues/20
研究资料：https://github.com/fweiger/AI_book/blob/topic/TOPIC-005/2026-11-04-uk-us-public-debt/topics/uk-us-public-debt-history/RESEARCH_EVIDENCE_20261104.md
完整协议：https://github.com/fweiger/AI_book/blob/topic/TOPIC-005/2026-11-04-uk-us-public-debt/topics/uk-us-public-debt-history/AGENT_PROMPTS.md

必须先读取Issue #20中的HOST/R0与4份分别标为ROLE=FISCAL_DEBT/STERLING_CAPITAL/STRATEGIC_HANDOFF/ALTERNATIVE_CAUSES、ROUND=R1的研究报告，并记录它们的真实评论链接。未齐备时报告缺少哪些，不能伪造缺失报告；可以做标明PARTIAL的预审但不能声称完成R2。

逐条交叉质询：
(1) 源头真假：DOI/作者/年份、档案编号/原文段落、引文是否真支持主张；
(2) 统计混淆：国债率下降≠本金偿还，英国PSND与美国gross/public不一致、海外证券存量与年净流量混淆；
(3) 机制缺口：政府利息是否真的挤压了海外公共支出？私人海外投资减少是否来自政府财政而非战争/管制/外国偿还？
(4) 事件先后：1947英国退出→美国接替是否包含政策协商和对照；1956外汇压力何时相对军事决策发生；
(5) 反事实与共同原因：1815英国、战前相对衰落、殖民民族主义、美国自身崛起、因果反向；
(6) 时间外推：是否有人拿2026美国债务率直接推导“霸权丧失”，忽略美元制度及海外FDI增加证据。

交付：E-R2《对抗性证据审查书》，至少12条**有具体目标评论/主张引用**的问题，按严重程度P0/P1/P2分类；每条都给出可查核的来源、导致什么结论失效、谁需要回应以及可闭合的验收标准。特别列出不少于3条最强的“原先因果链必须降级”的证据。给A-D各自拟定R3回复清单，禁止直接宣布哪方赢。
把完整审查书评论发到Issue #20，头TOPIC-005 | ROUND=R2 | ROLE=RED_TEAM；返回真实评论链接，没有权限则NOT_POSTED。
```

## Agent F｜独立中立裁判与可迁移性评审（R4）

```text
你是AI_book TOPIC-005的独立中立裁判，ROLE=REFEREE，ROUND=R4。你不代表财政方、金融方、历史策略方、反方或红队，不可按模型人数投票得出历史事实。你的首要目标是判断英国债务/外币金融压力是否确实具有独立因果力量，还是战争/产业竞争/去殖民化的共同结果或中介。

讨论主帖：https://github.com/fweiger/AI_book/issues/20
规则与资料：https://github.com/fweiger/AI_book/blob/topic/TOPIC-005/2026-11-04-uk-us-public-debt/topics/uk-us-public-debt-history/AGENT_PROMPTS.md
起始证据：https://github.com/fweiger/AI_book/blob/topic/TOPIC-005/2026-11-04-uk-us-public-debt/topics/uk-us-public-debt-history/RESEARCH_EVIDENCE_20261104.md

请先完整读取HOST/R0、A–D共4份R1独立报告、E-R2红队报告，以及A–D对红队质询的R3逐条回应，分别保留真实评论链接。若缺任何必要轮次，先发布“裁判准备度审查：INCOMPLETE”与缺口清单；不得冒称正式终审，也不得按想象填充某队观点。对各方引用的关键数字和原始档案独立查一次，不把另一AI的文字当证据。

裁判必须分别审理六个因果环节：①战争→高债务/海外资产变化；②高债务→财政利息/偿付或美元流动性约束；③约束→海外资本与政府军事/援助投入减少；④投入减少→具体地区撤退决策；⑤撤退→美国或其他国家接手；⑥多事件累积是否可归因于英国全球霸权地位变化。分别按“已核事实/会计相关/因果部分支持/多因竞争/现有证据不可识别/遭证伪”评级，不能用定性结论替代因果强度。

明确审查1947希腊土耳其、1956苏伊士、1815高债务反例，区分公共债务与英镑外债/美元储备。给出“如不存在高债务，英国是否仍会因战争损失、产业规模与殖民政治退缩”的有条件反事实；不能凭空给概率百分比。

最后另设《美国2026机制映射》：哪些英国变量有美国官方可比数据、哪些制度不具可迁移性、哪些压力目前出现及哪些尚无证据、2036预测与2026实际不得混同；不得给“美国必衰落”预言或无来源阈值。

交付：F-R4《英国债务—全球霸权衰落独立终审报告》：原文证据台账、六环节逐项裁决矩阵、每个核心结论的最强反证、关键不确定性、可能的因果图（明确有证据与仅假设的箭头）、美国变量映射和下一轮原始数据任务。必须允许“无法确认债务是唯一/首要原因”的结论。
评论发布到Issue #20，头TOPIC-005 | ROUND=R4 | ROLE=REFEREE，并返回真实评论链接；无GitHub授权则NOT_POSTED；未获维护者审核许可不得自动修改main、合并PR或宣称INTEGRATED。
```

## R3：四位研究员的统一交叉答辩补充指令（在E完成后，再发回A–D原会话）

```text
请保持你在AI_book TOPIC-005的原ROLE，不得切换阵营。现进入ROUND=R3。完整阅读GitHub Issue #20 中E-R2红队审查报告，按其编号逐条回应所有指向你的质询：引用质询链接、补充独立一手档案/数据、明确承认哪些论点需修正/撤销/保持，更新各因果箭头的支持度；不得以“我仍然认为”代替证据。对其他研究员的最强反例做steelman而不是稻草人。输出“已解决/部分解决/未解决”表及剩余识别障碍。以TOPIC-005 | ROUND=R3 | ROLE=你的原ROLE提交到Issue #20；无GitHub权限则输出NOT_POSTED完整代发Markdown，并返回实际发布链接（如有）。不要启动R4裁判，不合并PR。
```

## 用于验证执行真实性的清单

- R0具有真实评论URL，或明确NOT_POSTED；
- R1四份独立报告各有R1标题、证据和提交URL；不能用Issue主帖本身冒充R1报告；
- E-R2审查引用R1具体评论链接而非泛泛评价；
- A–D完成R3后，裁判才可标R4正式完成；
- 所有引用链接能打开、原始统计可追溯、论文阅读层级真实；
- 研究PR保持Draft且未合并，未经验证不改变`claims.md`的结论等级。

