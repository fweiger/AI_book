# TOPIC-010｜工业革命为什么首先发生在英国？

> **状态：RESEARCH_DRAFT / M0-P0 首批史料时间线**  
> **权威任务：[AI_book #30](https://github.com/fweiger/AI_book/issues/30)** · **等级 L** · **研究总体：1450—1850年，重点1600—1765年**

这个研究专题不把“工业革命首先发生在英国”直接归因于殖民财富、英国优越制度、和平环境或某一发明。目标是同时检验葡萄牙、西班牙、荷兰、法国与英国在航海技术、人口/殖民贸易、政治战争、财政军事四线中的相互作用，识别工业化的**创新、采用、规模化和持续生产率增长**。

## 本轮可核查研究产物

- [事件表：33条，1492—1765（CSV）](data/events_m0.csv)——四线主类别与次类别、年份/区间精度、来源、限制条件。
- [来源登记：25条（CSV）](data/sources_m0.csv)——官方档案/博物馆/机构资料，以及资料类型、数据范围说明。
- [大西洋奴隶贸易承运数据：1601—1775（CSV）](data/slave_carriers_m0.csv)——来自SlaveVoyages，不能代表殖民控制人口。
- [财政来源准入矩阵：12条（CSV）](data/fiscal_source_admission_m0.csv)——五国财政数据的已知范围、口径与未下载状态。
- [财政来源核查说明](data/fiscal_admission_m0.md)——OBR、Karaman–Pamuk、葡萄牙论文与数据仓库。
- [M0/P0 字段定义、准入与因果边界](data/SCHEMA.md)——风险、口径、缺失、下一步。
- [五国历史财政实数V1及方法审计](data/fiscal_cross_country_v1.md)——三张公开发表统计表及一份OBR历史基准，明确差异口径。
- [财政GDP占比表（Costa 2024 Table 3）](data/fiscal_costa2024_table3_gdp.csv) · [标准生活篮子表（Costa 2024 Table 2）](data/fiscal_costa2024_table2_baskets.csv) · [白银人均财政表（Broadberry 2026 Table 5）](data/fiscal_broadberry2026_table5_silver.csv) · [OBR英国债务基准](data/fiscal_obr_2023_uk_benchmarks.csv)
- [跨国财政比率计算与来源记录](data/fiscal_comparison_derived_v1.csv)
- [英国及欧洲跨国军费融资机制](data/fiscal_military_mechanism_v1.md) · [论文兵员占比估计](data/fiscal_military_literature_ranges_v1.csv)
- [英国财政与战争年度数据核验V2（1689—1850）](data/boe_annual_fiscal_audit_v2.md)——实际解析年度公开CSV、债务/GDP双分母敏感性及10个战争/相对和平窗口。
- [BoE年度财政基础序列162年](data/boe_millennium_annual_fiscal_1689_1850_v1.csv) · [债务/GDP 1700—1749](data/boe_debt_gdp_1700_1749_v1.csv) · [1750—1799](data/boe_debt_gdp_1750_1799_v1.csv) · [1800—1850](data/boe_debt_gdp_1800_1850_v1.csv) · [10段战争/相对和平统计](data/boe_war_peace_windows_descriptive_v1.csv)
- [英国BoE官方Excel原始收入、GDP和国防支出审计V3](data/boe_primary_annual_fiscal_audit_v3.md) · [1700—1799财政年度表（98年）](data/boe_official_1700_1799_tax_receipts_v3.csv) · [1900—1950国防支出占比表（51年）](data/boe_official_1900_1950_defence_share_v1.csv)
- [TOPIC-010 × TOPIC-005：1688—1956英国战争融资与霸权变迁机制桥](data/cross_era_war_empire_bridge_v1.md) · [2026-11-14本轮研究会话](sessions/2026-11-14-war-strategy-cross-era.md)
- [1569—1815皇家海军军费学术数据准入和原始档案线索](data/naval_expenditure_source_audit_v1.md)——LSE实证论文及图形核实，作者原始军费年度序列尚未取得。
- [战争与殖民收益机制转换：1688—1967比较报告](data/empire_war_payoff_regime_shift_v1.md)——早期战争—贸易税基反馈、二战海外英镑负债与殖民地财政援助及反例。
- [跨时代帝国收益／成本证据台账：23条CSV](data/empire_war_payoff_evidence_v1.csv)——国家／时间／数值口径／来源等级与不可推断事项。
- [帝国边际收益递减与战略过度延伸假说 IMR-01](data/imperial_marginal_returns_overstretch_hypothesis_v1.md)——Kennedy/Tainter/O'Brien、西班牙/荷兰对照、3类阈值和5个可证伪预测；不预设帝国整体现金流已转负。
- [2026-11-14 初始研究会话](sessions/2026-11-14-M0-P0.md)——已读/未读、反例与阶段进展。

## 四帝国独立案例研究（M0首轮）

以下是TOPIC-010的独立国家工作流，与英国本体研究共用[五轨史料与可比性协议](data/FOUR_EMPIRE_COMPARISON_PROTOCOL_V1.md)，各自保留单独Issue与Draft PR，并非主议题复制的第二份进度：
- [CASE-ESP-001 西班牙 #32](https://github.com/fweiger/AI_book/issues/32) · [Draft PR #36](https://github.com/fweiger/AI_book/pull/36) — 美洲白银/原住民mita、王室战争税与借款。
- [CASE-NLD-001 荷兰 #33](https://github.com/fweiger/AI_book/issues/33) · [Draft PR #37](https://github.com/fweiger/AI_book/pull/37) — VOC贸易扩张、亚洲军政成本、第四次英荷战争与信用崩溃。
- [CASE-PRT-001 葡萄牙 #34](https://github.com/fweiger/AI_book/issues/34) · [Draft PR #38](https://github.com/fweiger/AI_book/pull/38) — 巴西糖/黄金、奴役劳动与英国进口竞争、贸易正收益与资源诅咒。
- [CASE-FRA-001 法国 #35](https://github.com/fweiger/AI_book/issues/35) · [Draft PR #39](https://github.com/fweiger/AI_book/pull/39) — 科学院/海军、种植园经济、七年战争、财政冲突与海地独立。

首轮各国合计50条历史事件、39项来源登记、20条数值与待获取指标记录；这是**来源准入与结构化第一轮**，并非已完成跨国因果回归。各案工作文件分别在独立PR中，不直接修改本Draft PR的已提交主研究数字。

- [英国—荷兰1600—1765技术采用、工资能源与H1—H7竞争解释审计](data/TOPIC010_UK_NLD_TECH_ADOPTION_WAGES_ENERGY_1600_1765_20261114.md)——严格区分风力机械锯木、煤炭/蒸汽采用、产业组织及1750后增长；以荷兰高财政动员和便宜泥炭作为反例，复用Costa源表比较3个50年窗口；[15条证据](data/britain_netherlands_evidence_1600_1765.csv)、[7项假说反证](data/britain_netherlands_hypothesis_falsifiers_1600_1765.csv)、[3期财政同源对照](data/britain_netherlands_fiscal_comparator_1600_1749.csv)。因果识别尚未运行。
- [2026-11-14 四国案例第一轮阶段出口与研究重定向](data/TOPIC010_CROSS_EMPIRE_STAGE_GATE_AND_REFOCUS_20261114.md)——四国M0/M1来源/事件/数值记录结构已达到首轮门槛；暂停与上位假说无关的原始汇票或小额账表深挖。上位P1—P4转向英国与荷兰技术采用、高工资/能源、棉纺品贸易变迁、五国最小财政可比面板；阶段出口不等于历史因果已通过。
- [四国首轮机制比较：50事件、39来源、20指标](data/FOUR_EMPIRE_M0_SYNTHESIS.md)——西班牙/荷兰/葡萄牙/法国各自独立Draft PR，五轨检验与反例。
- [美国地缘屏障、产业规模与对外战略对照](data/USA_GEOSTRATEGIC_CONTROL_V1.md)——1898殖民扩张、1913制造业领先与1941租借法的类比边界。

## 核心比较问题

- A 航海／导航／船舶／火炮、冶金的技术积累，是否实际外溢到工业制造？
- B 殖民控制、强制劳动、跨洋贸易网络与市场规模如何改变经济激励？
- C 英国内战、英荷海战、英法全球战争和王室更迭如何影响相对竞争？
- D 财政收支、国债利率、战争金融与海军投入中，英国相对优势何时出现？
- E 高工资、能源价格、农业及知识网络能否作为独立竞争性解释？

## 研究规范

不得把书籍简介当作原文精读；不将不同AI的一致意见视作史实；不把历史事件的同一时代出现判为因果。**Issue中的 H1—H7 都是待检验假说。** 本草稿未经独立审查，尚未正式合并入知识库。

[另一个独立专题TOPIC-005｜英国霸权如何衰落](https://github.com/fweiger/AI_book/issues/20)。


## 2026-11-14阶段门与研究方向纠偏：四国停止无边界财政下钻

[四帝国国家研究阶段门审计：回到英国率先工业化的比较因果问题](data/TOPIC010_FOUR_EMPIRE_STAGE_GATE_REFOCUS_TO_UK_INDUSTRIALIZATION_20261114.md)：按原始Issue #30的P0—P5和H1—H7核对四国研究，实际GET其首轮数据为**50事件、39来源、20初始数值/缺失条目**。四国M0/M1证据基线**可冻结供横向比较**；各国M2/M3财政子研究暂停无限档案下钻，不改变史料未取得/因果未运行标识、不关闭各国Issue或合并Draft PR。高优先级转向**英国工业化结果、棉织品/原棉国际流向、跨国技术采用与煤价/工资、国家财政可比口径及H1—H7反例矩阵**；IMR-01仅是竞争假说而不是整个研究的替代目标。

---

## 2026-11-14 | TOPIC-010阶段门：从四国财政档案回归英国工业化比较

- [**完整阶段审查与下一阶段研究优先序**](data/TOPIC010_PHASE_GATE_REFOCUS_FIVE_COUNTRIES_20261114.md) · [原始AC-01—08覆盖检查](data/topic010_original_ac_coverage_stage_gate_20261114.csv) · [四国M0来源与研究暂停门槛](data/four_empire_case_stage_gate_20261114.csv)。
- 直接回读原始[总任务#30](https://github.com/fweiger/AI_book/issues/30)与四国唯一Issue/独立Draft PR，核查四国 **50条初轮事件、39条来源、20条数值或缺失指标记录**。四个M0**首轮来源/事件/竞争机制研究可阶段收束**，但国家M2原始现金账与独立因果研究**未完成**，不宣称全部验收通过；保持五个Issue及五个PR的原有开放/Draft状态。
- **优先级纠偏**：TOPIC-010真正目标是解释“为什么英国先实现持续的煤—蒸汽—纺织机械化工业化”，四国是反事实对照；IMR-01帝国收益递减和TOPIC-005后期霸权衰落不是该目标的替代品。停止按默认流程无限追瓦伦西亚1797军饷/荷兰银行单周余额/葡萄牙1766单笔贷款/法国1803单张汇票。**只有能改变H1—H7的跨国工业化解释，才重启个案微观调卷**。
- **尚未完成的原需求**：五国殖民人口/商品流向、产业资本配置和技术外溢，尤其“印度棉织品进口欧洲→英国机械化→原棉进口/工业品出口”的时序闭环；荷英工资能源对照、英法制造技术采用差异、英葡资源价格/制造业挤出比较；七类假说证据反证矩阵与独立史学评审。
- **单一下一步**：继续总任务#30，从已经可公开获取的工业史、贸易、工资/能源和生产率系列搭建英国纺织机械化前中后三阶段，与荷兰、法国、葡萄牙、西班牙配置强反例；暂不创建重复Issue或按档案号无限深挖。

---

## M3-A — 2026-11-14：第一次直接检验英国棉织业竞争优势转换

- [**完整五国工业化竞争机制 M3-A 报告**](data/TOPIC010_M3A_COTTON_MARKET_MECHANIZATION_FIVE_COUNTRY_HYPOTHESIS_20261114.md)、[英国1697—1849原棉与棉纺出口双时期数值](data/cotton_uk_consumption_exports_periods_m3a.csv)、[印度EIC/VOC棉布输入8时期](data/cotton_indian_piece_goods_eic_voc_m3a.csv)、[英印当期价进出口8时期](data/cotton_britain_india_piece_trade_current_prices_m3a.csv)、[H1—H7五国比较/反证矩阵](data/uk_industrialization_h1_h7_discrimination_m3a.csv)。
- 直接目视核对LSE广受引用的Broadberry—Gupta作者PDF表1–5（印刷pp32–35）：英国原棉年均消费**1750年代2.8→1800年代59.6→1840年代526.3百万磅**；英国棉织出口历史固定官方价同窗口86→8352→85947千英镑；当期价英国制造棉织品出口1784—86 **797千英镑** → 1804—06 **16,339千英镑**；**不可混合当期价和1697官方价**。
- 首轮关键机制：印度棉布跨境贸易和英国进口竞争先于1771英国Cromford机器工厂应用；技术商业化和生产率提升后出口逆转，英国对印度本土市场1831—35的估计份额仍仅3.9%。与Allen高工资利润模型、Raman实物纱线密度、Crafts反对性评论、MIT美国奴役劳动生产原棉后期供给作证据分级。**不是已完成H1—H7因果裁决或五国产业同口径面板。**
- 四个子国案例M0已阶段收束；暂停无边界财政档案追踪。下一步用英荷英法的机器采用/要素价格建立同一工业化结果的判别性对照；保持本Issue #30与Draft PR #31开放/草稿。

## M3 方向纠偏落实：五国H1—H7证据矩阵及英印棉纺技术竞争（2026-11-14）

- [五国H1—H7综合研究：技术、工资能源、全球棉布贸易、工匠技能与殖民资本](data/TOPIC010_FIVE_COUNTRY_H1_H7_EVIDENCE_MATRIX_COTTON_TECH_COMPARISON_M3_20261114.md)：**回到“英国为什么率先持续工业化”**，使用原Issue七假说并以四个已冻结首轮殖民帝国案例作对照；区分**制造技术首次出现、企业采用、实际规模/生产率、出口竞争力**，不给主权财税数据的数量研究取代产业因果研究。
- [五国×七假说=35条支持/反例矩阵CSV](data/five_country_H1_H7_industrialization_competing_hypotheses_matrix_m3.csv)：每条含英国结果定义、对应国家、历史对照、最强反例、来源URL、证据级别、因果未运行和不可比标识；**不是35票的AI投票**。
- [原棉年均使用、英印棉布进出口、技术前沿劳动工时18条原值](data/cotton_india_britain_1700_1850_trade_skill_adoption_source_observations_m3.csv)与[8项可复算指标](data/uk_cotton_trade_technology_comparative_bridge_derived_m3.csv)，来源Broadberry–Gupta(2005) CEPR作者原稿Table1/3/4/8、与2009同行评审文章明确**同作者相关版本**，原稿PDF实得SHA256`9a63fff33030510ae2da94fa1384bc8c93c157e0b93d162c3c6c0753409e3638`；原始19世纪海关簿与机械史原账**未独立重新取得**。
- [35格和18项源数据标准库验证器](data/validate_five_country_hypotheses_and_cotton_outcome_bridge_m3.py)，已在当前研究分支重新下载实际运行，`PASS matrix_cells=35 cotton_anchors=18`、派生8行CSV SHA256`8a8a71286312400f56b4b3051ca58a508b1bc453d5eb14fecc84b45873e28f9b`。核心判别冲突：**Allen(2011)跨国高工资廉价煤** vs **Kelly–Mokyr–Ó Gráda(2023)英国郡级低起始工资/高机械技能**，两种估计量不同，不能直接按谁对谁错投票。棉纺产出原料规模放大、最佳实践纺纱工时下降 ≠ 全国人均生产率/奴役资本的单因果结果。
- **下一步唯一方向**：不重新打开国家财政档案逐叶工作；从[Warwick/CAGE Broadberry等英国历史GDP及产业数据](https://warwick.ac.uk/fac/soc/economics/research/centres/cage/data/datasets/17-01-22-british_economic_growth_1270_1870/)与英国/荷兰/法国同业工资能源和设备采用来源，建立产业因变量及国家可比性桥，针对H2/H6/H7进行竞争性预测检验；未取得这些原始数据仍标`NOT_ACQUIRED`。


## M3-B — 2026-11-14：英国棉纱出口地理分布与法国后发采用

- [M3B实证补充报告](data/TOPIC010_M3B_COTTON_YARN_EXPORT_GEOGRAPHY_FRENCH_ADOPTION_20261114.md)及[Hansard 1839棉纱出口三年份×六分项源表](data/cotton_yarn_export_destinations_hansard_1839_m3b.csv)：英国议会1839-03-12公布1818/1830/1834棉纱出口地理数据，逐年份五地区求和均与公布总计一致；1834年英国棉纱出口81,335,559磅，其中德国/比利时/荷兰合并地区占**48.2556%**，印度/中国合并占**6.7381%**。这些是**棉纱（中间品）出口重量**而不是全部棉纺成品/殖民地市场份额，也不等于原海关账本已独立复核。
- [Juhász（2018）American Economic Review](https://doi.org/10.1257/aer.20151730)法国1803—1815贸易封锁准自然实验发表结果：法国不同地区的相对保护提升了后发棉纺机械技术采用；是**作者的因果研究**，本项目尚未获取复现数据或重跑。为原H2/H5/H7提供英国以外的重要产业化反例。
- 对既有[M3A棉纺贸易和机器机制报告](data/TOPIC010_M3A_COTTON_MARKET_MECHANIZATION_FIVE_COUNTRY_HYPOTHESIS_20261114.md)提供**新来源家族、非重复时间段/地理维度**，不再扩展四国微观财政档案；英法同年代机器采用比较和复制论文识别仍NOT_RUN。


## M3-C — 2026-11-14：英法工资×纺纱机价格×采用条件

- [M3C聚焦报告](data/TOPIC010_M3C_UK_FRANCE_CAPITAL_WAGE_MACHINE_ADOPTION_20261114.md)：以Crafts (2014) Table9 实际PDF第20页为依据，英/法纺纱珍妮IRR模型**38.0%/2.5%**，仅将法方机器价由1450便士等价降至英国840、法国工资不变则为**24.0%（模型反事实）**；对应[8项可复算情景CSV](data/uk_france_spinning_jenny_irr_counterfactual_m3c.csv)与[标准库重算程序](data/validate_uk_france_jenny_irr_m3c.py)。此结果否定“仅靠高工资即可解释英法采用差异”的过强版本，不否定工资的联合影响。历史利用率、资本市场门槛和技术取得成本仍不确定。
- 英国Maw等（2022）Table1给出1784/1787/1789各类机器纱锭存量**34.7万/194.1万/241.0万**的当代混合估计；法国Juhász 2017作者稿给出1803/1812约38万/140万纱锭的历史重建，法国2018 AER刊出地区贸易保护—后发技术采用的研究结论。**年份/地区总体/插补/机器类型不可直接并表估计国别因果差距**，AEA replication [openICPSR 113114](https://www.openicpsr.org/openicpsr/project/113114/version/V1/view) 已定位但文件登录阻断。
- 2017法国作者稿“38万→140万增长约370%”的表述和端点约值算术差异保留为待核，不擅自修改论文原表；本轮独立内部IRR程序按四个出版表情景±0.25个百分点准则通过，并加入非史实利用率敏感性；**官方机器微观数据与跨国识别回归NOT_RUN**。
- **下一步唯一动作**：基于现有M3A/B/C和35格五国H1—H7假说矩阵，生成统一“机制通过/被削弱/无法区分”综合研究结论，停止继续为单个历史账页或单一机制创建新项目。

---

## M3-C｜英法纺纱珍妮机投资门槛与H6/H7敏感性复算（2026-11-14）

- [M3-C研究报告与四国对照边界](data/TOPIC010_M3C_SPINNING_JENNY_PROFITABILITY_CRAFTS_ALLEN_SENSITIVITY_20261114.md) · [Crafts 2010 Table 1原发表/复算12格](data/jenny_crafts_2010_4x3_irr_published_vs_replication_m3c.csv) · [英法四种现实参数和反事实场景](data/jenny_allen_crafts_counterfactual_utilization_m3c.csv) · [Python标准库计算校验器](data/validate_jenny_profitability_m3c.py) · [研究日志](sessions/2026-11-14-spinning-jenny-allen-crafts-irr-m3c.md)。
- **同一模型**：英国工资6.25d/日与设备价840d→IRR38.03%，法国工资4.66d/日与设备价1450d→2.50%；若法国工资+英国机器价840d则模型IRR23.79%，或法国原价但300日×50%使用率则模型IRR17.86%，均超过论文假设15%门槛。**后两项是反事实不是实际历史投资回报**。
- **最大证据增量**：作者发表12格IRR与本地Python等价原型独立计算最大差0.476个百分点；在法国原工资、基准使用率和15%阈值下，机器最高容许报价1038.14d（较法国推算1450d低28.40%）。H6必须拆工资/机器价/使用率，H7工匠/规模与知识依旧待实证；Kelly等2023英国郡内低工资高机械技能与Allen英法投资模型属于不同估计量。
- **诚实状态**：原研究和Crafts批评PDF文字可读但web截图CACHE_MISS；Allen机器24锭价格等为作者推断，历史工厂账及荷兰同款机器价格未取得；**原始行业因果与独立源复查NOT_RUN**。不修改四国已阶段结束的M0财税档案任务，不创建重复Issue。

## M3-C — 2026-11-14：英国—法国纺纱珍妮机的工资/设备/市场需求反事实

- [**H2/H6/H7可复算研究报告：固定产量 vs 扩大产量**](data/TOPIC010_M3C_SPINNING_JENNY_H2_H6_H7_COUNTERFACTUAL_20261114.md)：此前M3-A已覆盖印度棉布贸易与英国棉纺出口时序，本轮直接测试**机器为何值得采用**。复核Allen(2009)、Crafts(2010)、Gragnolati等(2011)与Allen(2011)的公开模型争论，固定产量时英法纺纱珍妮IRR约**38.03%/2.50%**；在假设额外产出全可销售时约**138.79%/53.54%**。两者皆**作者模型假定情景**，不代表真实企业利润或已完成工业革命因果识别。
- [36条论文Table2工资/开工强度/生产率模型验算](data/spinning_jenny_published_model_m3c.csv) · [4条工资与机器价格交叉替换](data/spinning_jenny_wage_capital_cross_m3c.csv) · [Python3纯标准库可复现脚本](data/spinning_jenny_h6_counterfactual_model_m3c.py)。英法原币种只在各自国家计算，跨国交叉使用Crafts历史圆整币种等价值；复算公布IRR与本轮计算最大差约0.27个百分点，保留差异而非静默修改。高工资既非唯一因素，也不能脱离设备价及市场需求。
- 原主题#30仍在研究“**英国为什么率先持续工业化**”；四国财政档案暂时冻结。下一步不是新开国家Issue，而是核查**1780年代英法可销售的纺纱产量、机器价格和使用强度**，用可否证的需求边界审计H2/H6/H7。荷兰珍妮机历史价格`NOT_ACQUIRED`、工业因果回归`NOT_RUN`。保持原Draft PR。


## M3跨机制阶段裁决与葡萄牙首轮退出（2026-11-14）

- [**M3统一裁决：五国反例、H1—H7过强命题的削弱范围、工业化转化链和国家研究停止规则**](data/TOPIC010_M3_STRATEGIC_MECHANISM_VERDICT_AND_COUNTRY_EXIT_20261114.md)：整合已有M3A/B/C、英荷比较与葡西荷法四国成果，不新增财政账目或跨国回归。**结论**：葡萄牙殖民贸易正贡献与巴西黄金的资源诅咒估计可并存；荷兰航运/财政/机械能力、法国科研/后发采用分别削弱单一充分条件叙事。英国可能更早形成“国际商品学习×机器采购/相对要素价格×工匠制造技能×企业采用规模”组合，仍是待验证机制。
- **真实状态**：四国首轮 `FIRST_PASS_FROZEN`；H1—H7机制证据综合 `PARTIAL`；跨国因果权重 `NOT_IDENTIFIED`；独立历史评审 `NOT_RUN`。四国Issue继续开放、PR继续Draft；**下一个唯一动作**是针对已完成的机制裁决做独立历史因果复核，暂不恢复国家财政微观档案无限下钻。
- **M3宏观因变量补证（不新增重复裁决报告）**：[工业与GDP实际产出同源四期表](data/uk_industry_gdp_real_growth_macro_anchor_m3.csv)；已将原PDF Table7视觉核对的英国工业年增速 **0.58%→1.04%→2.01%→2.97%** 对应年代窗口补充到既有[M3裁决报告第7节](data/TOPIC010_M3_STRATEGIC_MECHANISM_VERDICT_AND_COUNTRY_EXIT_20261114.md)，并将“前置非农就业结构转型”与“机械化驱动后续行业产出加速”明确分开。历史增长率不是实际劳动生产率或因果系数；2013结构就业源与2011作者重建属于相关学术谱系，独立审查仍未通过。

## M4-A｜2026-11-14 法国贸易封锁的因果识别审计

- [**Juhász (2018) 发表准自然实验的识别与竞争机制审查**](data/TOPIC010_M4_FRENCH_BLOCKADE_CAUSAL_IDENTIFICATION_REVIEW_20261114.md)：首次将法国1803—1812部门层面的连续双重差分（88部门、176个部门—时点、每千人机械纺锭数）与**战前趋势、毛纺/皮革安慰剂、资本—劳动比率、机器质量、路网/交通成本**等原论文检验接入原H2/H5/H6/H7。作者预发表稿基准系数33.47是`每千人纺锭数/ln有效距离`，**不是产出增长33.47%**；作者的强短期识别与较弱长期提示分开。与Allen英法设备IRR及Kelly–Mokyr–Ó Gráda英国41郡技能研究按**国家/地区/时间/因变量**严格区分，不宣称互相推翻或自动相互复制。
- **审查状态**：出版论文、作者稿及在线附录文字检索完成，PDF页截图工具失败；作者的规格与稳健性是**作者已做的检验**，本项目**没有拿到AER复现包、没有跑88部门数据回归、没有独立史学专家外审**。暂停四国零散财政账追踪，下一步只在可合法取得原始复现数据时重跑具体识别规格，否则进入上位AC-06/07验收而不扩张档案搜索。


## M3｜H2/H6/H7原论文来源级红队审查（2026-11-14）

- [**H2贸易学习、H6机器采用经济性、H7机械技能：原论文因果边界与阶段判定**](data/TOPIC010_M3_H2_H6_H7_SOURCE_CAUSAL_REDTEAM_20261114.md)——复核Raman(2022)棉布实物样本选择与质量学习的外推限制、Gragnolati等(2011)纺纱珍妮固定产量/扩大产量互斥情景（P=3,D=0.4时IRR分别英38.0%/法2.5%与英138.8%/法53.5%，均为模型而非实际回报）、Kelly等(2023)英国内部郡级技能相关与Juhász(2018)法国后发采用识别的适用范围。**高工资单一充分条件降级；H2/H6/H7可能相互中介，不能相加为独立因果份额。**
- 本轮是**同一AI对原论文的来源级红队复核**，不是独立历史学者或外部Agent终审；原Issue AC-07仍 `NOT_RUN`，本研究的真实跨国因果权重 `NOT_IDENTIFIED`。保持葡西荷法首轮阶段冻结与所有原Draft PR。下一步仅在总Issue组织可交接的阶段性结论，不复开国家微观财政档案。

---

## M3-D｜H2/H6/H7跨研究设计审查：市场、资本投资与采用后工厂生产率（2026-11-14）

- [M3-D方法学与史料审查报告](data/TOPIC010_M3D_H2_H6_H7_CROSS_DESIGN_CAUSAL_AUDIT_20261114.md) · [5项发表研究的因变量/样本/识别方法矩阵](data/industrialization_h2_h6_h7_estimand_provenance_m3d.csv) · [法国珍妮机新增销售/单位净贡献四情景](data/france_jenny_h2_sales_absorption_threshold_m3d.csv) · [方法学审查会话](sessions/2026-11-14-h2-h6-h7-method-audit-french-factory-learning-m3d.md)。
- **2024 JPE新增关键桥梁**：Juhász–Squicciarini–Voigtländer利用法国机械棉纺厂企业数据指出，采用新技术之后仍有低生产率、组织学习和低效企业退出过程；2020作者对外总结称1806–1840厂级劳动生产率增长约82%，**该数值非2024最终版表格本项目重新核算**。与Juhász2018法国贸易保护→更快机械采用和Kelly等2023英格兰郡初期低工资/高机械技能研究，是**时间窗、地理单位与因变量不同的三关**，不能把系数加总为英国工业化因果权重。
- **理论门槛检验**：以法国Allen–Crafts珍妮机参数为基础构造额外产量销售/边际贡献模型；在纯假设边际贡献实现系数1/0.75/0.5/0.45下，满足15%模型IRR所需新增最大产量的比例19.84%/31.74%/79.34%/>100%不可行。**全部是新构造反事实，不是法国历史订单**，用于说明H2需求吸收与H6机器经济性共同决定工厂采用。
- **研究审查状态**：本AI的方法学红队完成部分，**不满足AC-07的独立审查**；JPE2024复现数据字节、五国实际生产率同口径面板与因果权重仍NOT_ACQUIRED/NOT_RUN。四国案例首轮保持暂停一般性档案扩展；总Issue#30和PR#31保留OPEN/DRAFT。


## M4｜阶段性综合答案与独立评审交接（2026-11-14）

- [**五国工业化比较：阶段答案、H1—H7判定、原始P0—P5/AC01—08缺口与独立审查任务**](data/TOPIC010_M4_STAGE_SYNTHESIS_AND_REVIEW_HANDOFF_20261114.md)：不再重复M3细节研究，将葡萄牙/西班牙/荷兰/法国保留为四个有差异的反事实对照，区分商品市场需求、机械投资经济性、工匠技能对英国先行工业化的共同影响。英国实际工业产出分期增长（0.58/1.04/2.01/2.97%年均）有已发表重建数据支持，但不能与产能、劳动生产率或因果权重混淆。
- [本轮阶段决议与真实验收状态](sessions/2026-11-14-TOPIC010-stage-review-handoff.md)：**四国首轮冻结，TOPIC-010上位机制叙述可交审；完整跨国因果未完成，独立评审AC-07仍NOT_RUN**。保留原Issue、Draft PR、未取得来源与证伪机会；下一项唯一工作是由**非本轮主要写作者**的独立审查者复核，非继续逐笔财政档案追查。
