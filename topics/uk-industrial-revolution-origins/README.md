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

## 核心比较问题

- A 航海／导航／船舶／火炮、冶金的技术积累，是否实际外溢到工业制造？
- B 殖民控制、强制劳动、跨洋贸易网络与市场规模如何改变经济激励？
- C 英国内战、英荷海战、英法全球战争和王室更迭如何影响相对竞争？
- D 财政收支、国债利率、战争金融与海军投入中，英国相对优势何时出现？
- E 高工资、能源价格、农业及知识网络能否作为独立竞争性解释？

## 研究规范

不得把书籍简介当作原文精读；不将不同AI的一致意见视作史实；不把历史事件的同一时代出现判为因果。**Issue中的 H1—H7 都是待检验假说。** 本草稿未经独立审查，尚未正式合并入知识库。

[另一个独立专题TOPIC-005｜英国霸权如何衰落](https://github.com/fweiger/AI_book/issues/20)。
