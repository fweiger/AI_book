# 帝国扩张边际收益递减—全球防务成本加速模型（IMR-01）

> **提出背景**：TOPIC-010 [AI_book #30](https://github.com/fweiger/AI_book/issues/30) 与后期衰落 [TOPIC-005 #20](https://github.com/fweiger/AI_book/issues/20) 的跨时代讨论。  
> **研究状态**：假说已形式化，已检索代表性同行评审研究及反例；**没有完成跨帝国因果识别、完整净收益核算或统计显著性测试**。此文放在TOPIC-010 Draft PR #31，不能覆盖TOPIC-005既有R4审查意见。

## 1. 用户原命题与必须修正的事实边界

**用户命题**：大航海后的欧洲殖民帝国可能靠战争取得新据点、人口控制与贸易网络，增加税基和融资能力，形成正反馈；但随着殖民范围扩大、竞争者增多，新增收益慢于全球海军/驻军/治理成本及债息增长，终致财政和战略不可持续，走向退出、相对衰落。

**重要修正**：
- 英国不是每次都为主动“搅乱大陆战争”而参战；各次同盟义务与安全动机需当时外交档案确认，战争获利≠发动战争本意。
- 不必假设税基停止增长；如果新增维护成本增速或融资成本高于新增税基，帝国压力就可上升。
- 不必假设英国整体帝国投资现金流转负；单个地区边际净收益转负、全球战略维持不可持续、国家相对权力下降，是不同结果和拐点。
- 被殖民地及奴役人口所承担的损失不能从仅宗主国的净收益推导其社会总福利。

## 2. 理论结构：可分辨的三个阈值

令 `E_t` 为有效殖民控制与海外战略承诺强度（多个维度，不能只用km²），`R_t(E)` 为英国可归属的当期财政和经济收益，`C_t(E)` 为维持网络的防务、行政、资本、融资和殖民政治成本。

**阈值A：边际扩张不再合算**  
`∂R_t/∂E < ∂C_t/∂E`，可以在`R_t(E)>C_t(E)`时出现。**边际回报下降≠现有帝国全部净收益为负**。

**阈值B：财政/外汇可负担能力不足**  
`DSCR_t = (regular_tax_receipts_t + available_external_financing_t) / (defence_commitments_t + imperial_admin_t + debt_service_t)`。这只是候选财务风险比率，现金流税基+新增借债不宜机械混为经常收入；实际模型必须拆`fiscal_primary_balance`、`gross_refinancing_needs`、`sterling_external_liability_service`和`FX_access`，识别融资禁运或信用利差突变。跨国比较要统一公共部门与税负口径。

**阈值C：战略地位的相对能力突破**  
`CommitmentLoad_t / DeliverablePower_t`上升；后者包含相对工业生产率、可征税经济规模、海军有效吨位/航程、盟友支持、美元等国际结算货币可得性和殖民政治合法性。此阈值可能先于`R-C<0`出现。

**实验上优先使用离散增量**：`ΔV(colony_i, t)=PV(UK treasury incremental fiscal receipts+private net gains that can be attributed to imperial control - military/administrative/debt/FX incremental burdens)`，对照**不再直接统治但仍可进行贸易**的反事实；不得把殖民地全部商品贸易税收直接视为因控制而新增的税收。

## 3. 可与之对照的既有理论及证据层级

| 研究 | 已发表的核心判断（准确限定） | 对IMR-01的价值 |
| --- | --- | --- |
| Paul Kennedy, *The Rise and Fall of the Great Powers* (1987)；[相关历史学研究综述](https://www.cambridge.org/core/journals/itinerario/article/abs/comparative-history-and-the-colonial-encounter-the-great-war-and-the-crisis-of-the-british-empire/E0E5C3376BC65999ED6BB0375380C72D) | 相对工业/商业基础与全球军事承诺的长时段不匹配，可形成帝国过度延伸（imperial overstretch） | 建立“经济基础—军事承诺”的可负担能力模型，**不是对殖民地净利润的直接估计** |
| [Joseph Tainter (1995), Sustainability of Complex Societies](https://digitalcommons.usu.edu/envs_facpub/1315/) | 复杂系统持续投入问题解决资源可能出现边际回报递减 | 对象是各类复杂社会，**不能自动用来证明英国帝国发生特定年份崩溃** |
| [Patrick O'Brien (1988), Costs and Benefits of British Imperialism 1846–1914](https://doi.org/10.1093/past/120.1.163) | 讨论帝国收益与防务支出、负担在国内纳税人和殖民地之间的分配；认为庞大公费对1846–1914英国经济增长非必要/充分条件 | 英国帝国规模壮大时仍可能由国库/纳税人承担不成比例成本；**是最直接的早期过度延伸候选检验** |
| [O'Brien (1999), Imperialism and the Rise and Decline of British Economy](https://newleftreview.org/issues/i238/articles/patrick-o-brien-imperialism-and-the-rise-and-decline-of-the-british-economy-1688-1989) | 1865–1914英国本土居民人均帝国防务税负显著高于自治领和多数殖民地负担（依Davis/Huttenback重建）。该比值反映不同公共财政支出定义，不能直接转成跨帝国“战争ROI”。 | 政府付出与私人/海外受益主体分离，存在制度性自由搭便车 |
| [Jurado Sánchez (2010), Spain vs Britain military fiscal](https://www.cambridge.org/core/journals/revista-de-historia-economica-journal-of-iberian-and-latin-american-economic-history/article/abs/military-expenditure-spending-capacity-and-budget-constraint-in-eighteenthcentury-spain-and-britain/3B1A39BFABD6CD8E851478C1E19CB9D3) | 18世纪英国财政开支动员高于西班牙（陆、海军及债务服务），1688后融资制度是重要条件；论文以此解释多次英西战争英国相对军事优势 | **支持“能够为扩张融资”比“原本税收总额高”重要**，不能推论西班牙所有征税能力低下 |
| [Carlos Marichal (2007), Bankruptcy of Empire (1780–1800)](https://www.cambridge.org/core/books/abs/bankruptcy-of-empire/imperial-wars-and-loans-from-new-spain-17801800/A949A388DF0ED83E906CA22EBE8730A9) | 西班牙18世纪末虽然积极提高本国及新西班牙殖民财政收入，反复战争支出仍增长得更快，迫使增加借债 | **更接近用户“收入仍增长但成本超增量”的西班牙反例** |
| [Dutch and English Fiscal-Naval States (2023)](https://www.cambridge.org/core/books/abs/war-trade-and-the-state/dutch-and-english-fiscalnaval-states-a-comparative-overview/B8131FA5C932F5387B4B950A99BCA9CF) | 荷兰与英格兰均在17世纪发生大规模海军财政动员，需要比较造船、国家财政与海军机构 | 荷兰不是没技术/没税收/没海军，而是非常关键的同类型控制组 |
| [British Overseas Military Commitments 1945–47 (2013)](https://doi.org/10.1080/13619462.2013.796884) | 经济约束促使英国减少海外承诺，但不能独立决定撤出印度、巴勒斯坦、希腊的具体选择/日期 | 直接否定“只需财政亏损一个指标，就能准确预测独立年份” |

## 4. 三个跨时代实证反例约束

**R1 早期局部非单调**：1763英法战争胜利扩大北美控制，但随后又丢失十三殖民地（1783）；不能声称英国每场战争都净赚海外领地，或早期持续正回报。

**R2 1815高债务但延续霸权**：高债务/GDP伴随着英国随后国际海权与贸易优势，帝国运转依赖可再融资的公共信用及工业能力，不能以“债务高”作为霸权下滑的充分条件。

**R3 1918—1947分段变化**：一战后英国取得国际联盟委任地，殖民领土并非立即减少；英国的外币约束、海外英镑余额与1947年减少对希腊土耳其援助的政府文件，可支持二战后**经济约束推动某些全球承诺缩减**；同时殖民地独立运动是独立政治机制。

## 5. 明确区分四个研究账本

- 英国国库 `F`：国库实际税收/帝国转移、海军与驻军/殖民拨款、利息与到期续债需求。
- 英国私人企业 `P`：净商品利润、航运保险、投资收益，避免税款和利润重复计算。
- 对外资产负债 `X`：海外英镑余额、美元对外债务、海外资产出售、可兑换性及期限；存量与流量分别测。
- 殖民政治/防务成本 `S`：地方独立运动、实际有效控制、治安/战争成本，以及被殖民群体的社会损失（不能粗暴地以宗主国成本收益视角折算）。

**净利润/净财政**还需要**反事实**：没有正式殖民统治时仍可取得的正常国际贸易与税基，不能归为帝国的增量收益。若无法获得，报告部分现金流和识别区间，严禁制造总净现值。

## 6. 待检验预测与证伪条件

| ID | 可检验预测 | 更强反例/替代解释 | 数据及方法 |
| --- | --- | --- | --- |
| IMR-H1 | 同一帝国扩张到后期，新增控制区的直接国家税收净回流增速低于前期，海外支出更高 | 新控制地资源禀赋变化造成构成效应；维持成本不是单调随面积增长 | 地区/年度双向效应、港口战略重要性与控制方式分组 |
| IMR-H2 | 竞争者海军技术及吨位提高，会显著抬升英国全球海军维护单位航线成本 | 英国本土工资、造舰成本与通胀才是驱动 | 海军军费/船吨、实际防务航程、敌我吨位及海军技术 |
| IMR-H3 | 帝国持续财政税收增长仍可能出现更大再融资压力，尤其外汇可兑换受限时期 | 战后福利国家及国内财政扩张导致差额，与帝国无关 | 现款支出/债息/海外英镑余额与汇兑管制分别建模 |
| IMR-H4 | 高维持成本的殖民地更早退出英国直接治理，经济/贸易往来未必同步崩溃 | 民族自治运动及外交承诺决定先后，成本是内生结果 | 殖民独立时间风险模型、独立运动/领地价值/美元约束 |
| IMR-H5 | 相对工业生产力优势和高信用能力能缓冲同等战争负担对战略承诺的损害 | 战争胜负、地缘制度和联盟网络才是决定因素 | 英/西/荷/法国跨国差分＋结构断点与竞争性机制 |

**不能使用五个帝国中“谁最后失去殖民地”简单拟合一个单调衰落曲线**；历史帝国有多种退出方式（合并、独立、非正式经济控制、共同体）。并非每个帝国都必然崩溃，部分可能通过自治、退出昂贵驻军等方式主动降低复杂度、维持经济优势。

## 7. 当前证据、实施状态与下一动作

- 已研究并登记 Kennedy—Tainter—O'Brien—Jurado Sánchez—Marichal—荷英财政海军比较—1945–47撤军研究等代表性文献。
- **理论结构：已提出；英国实际帝国平均和边际净利润转负年份、断点及因果系数：NOT_IDENTIFIED；统计回归：NOT_RUN。**
- 关键的可直接核查的早期税收及1940s英镑负债、1951殖民援助资料在[既有帝国收益机制证据报告](empire_war_payoff_regime_shift_v1.md)，不要重造第二套数据账本。

**唯一下一项工作：** 对西班牙1780—1807财政战争及英国1846—1914帝国防务成本挑选**两组同主体同口径的税收/军事支出/借款数据**做边际成本方向检验，再与英国1940s外币债务建立概念上可比但来源独立的风险指标；仅在数据能明确分配的局部，才计算经济/财政增量净值。
