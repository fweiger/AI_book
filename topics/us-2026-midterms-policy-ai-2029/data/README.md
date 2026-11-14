# TOPIC-011｜M0机器注册表

## 第十七轮：政策条款、CBO预算估算和实际执行分层
- [h02_round17_policy_section_budget_actual_2008_2026.csv](h02_round17_policy_section_budget_actual_2008_2026.csv)：16条源记录，覆盖法定授权、后续修改、真实支付/净成本、CBO相对不同预算基线的未来赤字估算、Medicaid覆盖预测及2027旧法规的执行日期。空值绝不填0，2700亿EIP是严格下界，CBO -3660亿与+3.4万亿来自**同一法律但不同基线**。
- [h02_round17_gpo_bill_to_law_6files_sha.csv](h02_round17_gpo_bill_to_law_6files_sha.csv)：GovInfo的三份初始提案与三份最终成法原HTML文件的SHA/字节、法案ID及日期，已逐字节联网验证。
- [复算校验](../analysis/recompute_h02_round17_policy_section_budget_actual.py) · [方法、强反例及2027旧法负对照报告](../reports/2026-11-14_h02_round17_policy_section_budget_baselines_and_legacy_2027.md)。该样例提供H01→H02/H03的来源链，但不证明2027新国会因果，所有H仍UNTESTED。


## 第十六轮 H01官方逐案全量计算
- [h01_round16_billstatus_funnel_110_116_118_119.csv](h01_round16_billstatus_funnel_110_116_118_119.csv)：四届×9类36行GovInfo官方普通H.R./S.议案逐案累计，按第二年11/14截止。56,777项涵盖2008/2020/2024/2026同观察时点；立法动作可能在两个议院之间重复，不许将House和Senate通过数相加。
- [h01_round16_govinfo_source_manifest.csv](h01_round16_govinfo_source_manifest.csv)：8份govinfo BILLSTATUS ZIP的URL/SHA/字节数、全部XML数与截断数，历史重刊是后来取得的版本，并非当时PIT原字节；[纯stdlib复算](../analysis/recompute_h01_billstatus_funnel_round16.py)。
- [h01_round16_bill_status_audit_examples.csv](h01_round16_bill_status_audit_examples.csv)：77条可复核特征例；[h01_round16_bill_vehicle_policy_drift_examples.csv](h01_round16_bill_vehicle_policy_drift_examples.csv)：H.R.1424/748原案对最终法律的财政政策标签漂移。报告：[H01 56,777条明细背景及结论](../reports/2026-11-14_h01_round16_govinfo_56777_bill_stage_funnel.md)。
- 数据QA：原委员会活动字段比GPO真实报告动作码少186条，已按GPO报告动作码5000/14000加并；全部四届成法的议案都具备House与Senate动作码；119届为未完结旧国会，104届不在相同GovInfo数据源。因果状态仍UNTESTED。


## 第十五轮 H01国会历史参考类
- [h01_congress_104_119_historical_laws_20261014.csv](h01_congress_104_119_historical_laws_20261014.csv)：16届（1995—2026）Pew选举日前实质/纪念法律手工转录、NARA104—118完整成法及4届正式参院否决/推翻。**Pew实质分类非官方、119截止2026-10-14且尚未完届、NARA整届和Pew选前口径不可混比、107参院中途变权。**其他届没有逐项收集的否决留空而非零。
- [离线校验程序](../analysis/recompute_h01_congress_historical_comparison.py) · [来源、结果与因果限制报告](../reports/2026-11-14_h01_round15_congressional_productivity_veto_historical_baseline.md)。跨届简单均值仅为描述性历史底座，不是2027财政/AI投资的处理效果。


- [hypothesis_registry.csv](hypothesis_registry.csv)：H01—H10，初始状态UNTESTED。
- [causal_edges.csv](causal_edges.csv)：候选有向机制边，绝非已确认因果。
- [evidence_events.csv](evidence_events.csv)：**少量**确实有公开来源的事件样例，事件日与发布日期分开；不是完整数据库。
- [path_states.csv](path_states.csv)：P-A至P-D各自UNKNOWN；后续按asof追加快照。
- [forecast_registry.csv](forecast_registry.csv)：当前仅空表头，**尚未注册可量化预测**。

生成者不得用“没有数据”填0；要保留NA/空白、来源族、来源版本、事件日、披露日和取得时间。记录以[审计协议](../PROTOCOL.md)为准。

## 已落盘的M0实测/选前基线
- [treasury_october_2015_2026.csv](treasury_october_2015_2026.csv)：美国Treasury API原始报告当前FY的Oct 12组数据、全部2026-11-14提取（历年月报值是不同版本）。
- [fiscal_baseline_m0.csv](fiscal_baseline_m0.csv)：2026-02-11 CBO前瞻、FY2026事后结果、2026-10 MTS；PIT前/后标记。
- [capex_pre_election_2026.csv](capex_pre_election_2026.csv)：5家企业8项选前资本开支来源，严格区分现金/租赁、全年/单季、2026/2027财年。
- [离线复算脚本](../analysis/recompute_m0.py)。这些是描述统计，不是对政治因果的验证。

## H03新增：政策与真实电网预测数据
- [h03_policy_events_2026.csv](h03_policy_events_2026.csv)：8条选前州级已生效政策/选后联邦提案与程序投票，法律生效与出台日分开，项目延期MW统一标UNKNOWN。
- [h03_pjm_forecast_revisions_2026.csv](h03_pjm_forecast_revisions_2026.csv)：6个预测年份的PJM全RTO夏季系统峰值2025→2026版本下修/上修，绝非数据中心独有负荷。
- [h03_va_electricity_tax_scenarios.csv](h03_va_electricity_tax_scenarios.csv)：3种MW×3种负荷率的**假设情景**，不是项目实际成本。
- [H03离线复算](../analysis/recompute_h03_m0.py)及[观察报告](../reports/2026-11-14_h03_policy_grid_baseline.md)。

## PJM官方2026-05-29 XLSX测量值（严格源校验）
- [h03_pjm_2025_zone_observed_vs_forecast.csv](h03_pjm_2025_zone_observed_vs_forecast.csv)：23个分区/子区、2024/2025预测与历史实际、误差及空值；源SHA256在每行。
- [h03_pjm_historical_july_2019_2025.csv](h03_pjm_historical_july_2019_2025.csv)：RTO/DOM/AEP/COMED/PS五区2019—2025的大负荷历史峰值，避免缺值叠加。
- [h03_pjm_2025_to_2026_vintage_revisions.csv](h03_pjm_2025_to_2026_vintage_revisions.csv)：同目标年预测版本修订，部分主区与子区仅做分开比较不求和。
- [标准库源验证与离线复算](../analysis/recompute_h03_pjm_accuracy.py)。源XLSX未复制进GitHub；需从官方URL独立合法获取，SHA变更时另开版本。

- [h03_pjm_2026_july_macro_only_revisions.csv](h03_pjm_2026_july_macro_only_revisions.csv)：5个总区与4个规划年度的2026-01 vs2026-07总系统峰值预测，选前且仅供参考，来源SHA逐行登记；[校验程序](../analysis/recompute_h03_pjm_july_macro_update.py)。

## H03新增2026年秋季真实申请表（非实际投产）
- [h03_pjm_2026_sep_submission_capacity_demand_zone.csv](h03_pjm_2026_sep_submission_capacity_demand_zone.csv)：PJM官方XLSX两sheet 29条行对象×2027-2031=145行，容量和折算需求并排，保存Excel物理行、父/子角色和SHA。
- [h03_pjm_2026_sep_rto_submitted_pipeline.csv](h03_pjm_2026_sep_rto_submitted_pipeline.csv)：五年RTO申请及DOM/AEP浓度；切勿把D/C当成审批或实际兑现。
- [h03_pjm_2026_sep_source_discrepancy.csv](h03_pjm_2026_sep_source_discrepancy.csv)：Exelon FERC Nov3引用值 vs PJM Oct12会后值，暂不相同口径。
- [recompute_h03_autumn_submission.py](../analysis/recompute_h03_autumn_submission.py)：标准库复算RTO、DOM子区，并可附原XLSX SHA校验全部145行。

## H03 Firm合同→项目接入→实际收入来源台账（2026-11-14）
- [h03_dominion_contract_stage_history.csv](h03_dominion_contract_stage_history.csv)：2023/2025/2026三份Dominion ELOA/CLOA/ESA阶段储备，不等于投入运营。
- [h03_dominion_completed_campus_and_sales_share.csv](h03_dominion_completed_campus_and_sales_share.csv)：2024/2025新园区数量、规划最终MW及DC电力销售份额。
- [h03_dominion_highload_revenue_quarters.csv](h03_dominion_highload_revenue_quarters.csv)：同SEC分类下2025/2026 Q1–Q3高负荷销售实际收入。
- [h03_aep_evidence_scope_matrix.csv](h03_aep_evidence_scope_matrix.csv)：AEP PJM 2025近端ESA与2026全区域含ERCOT合同类型对照。
- [h03_maturity_scope_crosswalk.csv](h03_maturity_scope_crosswalk.csv)：明确何种分子分母可比较，防止错误“兑现率”。
- [H03合同/收入离线复算](../analysis/recompute_h03_firm_operating.py)。

## H03第五轮：队列、州级2027旧法规与真实MWh（2026-11-14）
- [h03_dominion_scc_queue_cohort.csv](h03_dominion_scc_queue_cohort.csv)：Dominion SCC原申请~70GW，其中25GW预计接入日期已分配、45GW在分批研究；不是实际接入和Firm合同。
- [h03_virginia_scc_pre_election_tariff_and_queue_rules.csv](h03_virginia_scc_pre_election_tariff_and_queue_rules.csv)：2025批准的GS-5费率及2026 interim匿名队列要求，含生效日期、案卷状态及豁免口径。
- [h03_dominion_actual_delivered_mwh_2024_2026.csv](h03_dominion_actual_delivered_mwh_2024_2026.csv)：真实Delivered百万MWh的全年/Q2/Q3/YTD同周期数据（全客户范围，非DC专属）。
- [h03_dominion_dc_sales_share_annual.csv](h03_dominion_dc_sales_share_annual.csv)：DC占Virginia Power电力销售比例，单列不同分母。
- [h03_dominion_weather_2025_2026.csv](h03_dominion_weather_2025_2026.csv)：冷暖度日数供真实电量控制，尚未做模型去天气效应。
- [h03_gs5_minimum_billed_demand_scenarios.csv](h03_gs5_minimum_billed_demand_scenarios.csv)：15种假设100/25/300MW合同计费底线（MW不是美元、非实际用电）。
- [h03_aep_pre_election_security_and_tariff_status.csv](h03_aep_pre_election_security_and_tariff_status.csv)：2026前已审批/未决收费机制及Texas ERCOT金融担保与初期申请。
- [标准库复算脚本](../analysis/recompute_h03_queue_and_physical.py)。



## H03第六轮：公司DC专属实测/预测与两个监管登记路径
- [h03_dominion_dc_only_physical_and_forecasts.csv](h03_dominion_dc_only_physical_and_forecasts.csv)：2025纯DC约4GW实际同时峰值+2026Jan原信函的2026—46共21个DC-only预测，不当成2026Nov独立本团队预注册。
- [h03_dominion_firm_capacity_stages_backtest.csv](h03_dominion_firm_capacity_stages_backtest.csv)：CLOA+ESA公司Firm，ELOA非Firm，2025Jul/Dec及2026Sep，保留**历史快照实际披露日**。
- [h03_pjm_real_load_trip_events_2024_2026.csv](h03_pjm_real_load_trip_events_2024_2026.csv)：2024/25/26三次PJM负荷转换事件，非实际数据中心全年峰值增长。
- [h03_pjm_2026_july_22_load_trip_balance.csv](h03_pjm_2026_july_22_load_trip_balance.csv)：2026-07-22 PJM实时整体净下降3779MW与公告“约3800MW”。
- [h03_state_federal_large_load_registry_status.csv](h03_state_federal_large_load_registry_status.csv)：VA SCC拟议100MW DP队列仍待审 vs FERC接受PJM >=50MW登记，2027-03初始报送，公开仅可能为区域汇总。
- [h03_data_discrepancies_and_controls.csv](h03_data_discrepancies_and_controls.csv)：5-12 vs5-25官方日期、PJM网站过期Pending、2025纯DC实际4GW与DOM区域LLA5563MW不能混比。
- [纯标准库复核](../analysis/recompute_h03_matured_dc_baseline.py)，以及[第六轮报告](../reports/2026-11-14_h03_registry_and_dc_peak_baseline.md)。历史原始信函公开2026-02，研究归档2026-11。

## H03第七轮：31条历史预测版本回测与CRA电力供给竞争解释
- [h03_pjm_load_forecast_vintage_backtest_2023_2025.csv](h03_pjm_load_forecast_vintage_backtest_2023_2025.csv)：历史31个zone×target_year×vintage匹配，2023/24/25版本，采用2026-05事后汇编的真实LLA，记录SHA及发布时间，不等同于纯DC或独立项目建设真实兑现。
- [h03_pjm_2025_paired_vintage_scorecard.csv](h03_pjm_2025_paired_vintage_scorecard.csv)：共同DOM/AEP/PS三区、同2025目标、2024与2025版本各一行，WAPE和MAPE权重分明。
- [h03_cra_nov2026_scenario_assumptions.csv](h03_cra_nov2026_scenario_assumptions.csv)：CRA 2026-11-02场景机制、未来2030约11.5GW供电缺口，且明确场景≠已实现。
- [recompute_h03_vintage_calibration.py](../analysis/recompute_h03_vintage_calibration.py)：纯标准库重算；附`--input`与原XLSX SHA和31条单元格比对。原XLSX未作为仓库附件上传，需从PJM官网下载保留原始文件。

## H03第八轮：跨公开版本的数据质量与PIT审计（2026-11-14）
- [h03_pjm_rto_2014_2024_cross_publication_history.csv](h03_pjm_rto_2014_2024_cross_publication_history.csv)：11个共同历史年份的PJM 2025-06整数MW和2026-05六位小数值、出版差与比例；定义一致性尚未验证。
- [h03_pjm_rto_2023_2030_cross_publication_forecasts.csv](h03_pjm_rto_2023_2030_cross_publication_forecasts.csv)：21个同标签RTO预测版本/目标年跨公开文档差异；2025版有原版B9b可复核，2023/24版目前只来自2025-06汇总PPT。
- [h03_pjm_rto_2023_2024_error_definition_sensitivity.csv](h03_pjm_rto_2023_2024_error_definition_sensitivity.csv)：同一出版物内部的3对历史误差率用于展示来源敏感性，非统计显著或实体电量变化。
- [recompute_h03_source_vintage_audit.py](../analysis/recompute_h03_source_vintage_audit.py)：纯标准库复算，可使用`--accuracy-xlsx`检查2026原始全RTO历史/预测数据，用`--original-2025-xlsx`核查2025官方原版B9b，共享来源SHA；2025六月PPT为原文表格人工转录，证据深度如实保留。

## COMMENTATOR VIEW与事实交叉核验（2026-11-14）
- [VIEW-S001外部评论者来源与研究协议](../views/README.md)；[10条观点主张登记](../views/claim_register.csv)。**VIEW主张≠独立事实证据**。
- [evidence_events.csv](evidence_events.csv)已新增 **E061—E067**：议员计划调查、德州采访、BLS CPI、Waller讲话、同期市场行情、CRS法律备忘、捐款媒体估计。严格区分来源类型 F/R/P 及选举前后PIT；这些是**事件或报道存在**，不是原评论者完整因果链的证明。
- 债务期限、FCF、利差的样本级企业面板尚未建立，不能生成政治暴露×融资压力的实测交互系数。

## 统一指标层v0.2.0（定义扩容，不是已完成时序采集）
- [指标总目录](../metrics/catalog.csv)：原I01—I14 + 历史H03的37个独立指标名 + I15—I54 40个新宏观/公司指标；所有既有ID不改，历史旧源不强制迁移。
- [官方BLS CPI7行样例](../metrics/observations_seed.csv)：period与publication timestamp分开，9月值仅作为2026-11-10发布文稿的回顾值，不冒充最初9月发布PIT。
- [专家EX/作品WORK](../experts/README.md) → [观点VIEW](../views/README.md) → [观点×H](../hypotheses/view_hypothesis_links.csv) → [CHAIN](../chains/README.md)。
- [H09 Texas/监督/赦免的空合同与程序表](../cases/musk-2026/README.md)：**没有真实合同/传票/赦免原件之前只保留表头，缺失不是0**。


## H03原版预测的B9/B9b统计层桥接（2026-11-14）
- [h03_pjm_original_above_embedded_vs_total_bridge_2023_2030.csv](h03_pjm_original_above_embedded_vs_total_bridge_2023_2030.csv)：21个`vintage×target_year`，2023/24跨文件proxy、2025同原始Excel差额，严格分类。
- [h03_pjm_embedded_bridge_vintage_summary.csv](h03_pjm_embedded_bridge_vintage_summary.csv)：三个版本差额均值/范围/CV，用于观察相对稳定基础项但不宣称项目真实容量。
- [h03_pjm_2025_within_workbook_zone_bridge.csv](h03_pjm_2025_within_workbook_zone_bridge.csv)：2025原版B9和B9b，RTO/DOM/AEP/other四级×2025—30共24行、来源SHA，RTO汇总不重复算子区。
- [h03_pjm_rto_2025_forecast_ranking_by_publication.csv](h03_pjm_rto_2025_forecast_ranking_by_publication.csv)：相同后验actual、两组出版源的2024/25版预测APE排序反转，仅表明来源敏感。
- [h03_pjm_original_document_revision_manifest.csv](h03_pjm_original_document_revision_manifest.csv)：2023原PDF、2024修订PDF、2025原版XLSX、2025六月回顾及2026五月准确性XLSX，记录实际可知日冲突和metric定义。
- [标准库校验脚本](../analysis/recompute_h03_original_bridge.py)可附`--original-2025-xlsx`直接验证官方同源2025 B9、B9b各RTO/DOM/AEP的6年度数值。


## H09/H10本轮真正取得的实物数据（2026-11-14）
- **H09**：[Travis County/SpaceX法律实体优惠合同登记3行](../cases/musk-2026/incentive_contracts.csv)及[事件六行](../cases/musk-2026/policy_event_ledger.csv)。包含2020原始Travis County合同、2025县级审查、2026-04据地方KUT报道的9%预期返利扣减、2025Tesla年报的合并财务不重大披露、2026-11 Starbase未来税惠申请；**KUT扣减的正式书记官会议记录和绝对美元尚未拿到，不能标经官方直接核查**。[原始协议核查报告](../reports/2026-11-14_h09_travis_texas_incentive_preelection_control.md)。主事件账增加E073—E077，其中新政府影响还未被识别。
- **H10**：[BLS CPI/月度22行](h10_bls_cpi_sa_monthly_2025_2026.csv)、[Treasury 2Y/10Y 467交易日](h10_us_treasury_2y_10y_daily_2025_2026.csv)、[BEA PCE发布版本4条](h10_bea_pce_release_vintages_2026.csv)、[FOMC真正政策两条](h10_fomc_official_decisions_2026.csv)；[离线脚本](../analysis/recompute_h10_open_data.py)在Ubuntu真实运行PASS，报告见[H10第一轮](../reports/2026-11-14_h10_cpi_pce_fomc_treasury_pit_baseline.md)。**2025-10 CPI缺值NA，2026-08 BEA PCE数值存在后续修订**，不能视为首次公示时已可知；未抓全量核心PCE指数/期货预期/企业债务面板。

## H03同口径原版预测年度分解（2025原版 vs 2026订正版）
- [h03_pjm_2025_2026_original_b9_b9b_revisions.csv](h03_pjm_2025_2026_original_b9_b9b_revisions.csv)：6个互不应重复加总的RTO/主要区域×2026—2035年共60行，保存2025与2026各自B9、B9b、差额和总修订三部分及源SHA。
- [h03_pjm_2027_original_zone_revision_contributions.csv](h03_pjm_2027_original_zone_revision_contributions.csv)：2027 DOM/AEP/COMED/PS/PL/其他六个不重叠分区与RTO总计，额外部分/已嵌入相关部分/总量皆能对账。
- [h03_pjm_2026_original_vs_accuracy_rto.csv](h03_pjm_2026_original_vs_accuracy_rto.csv)：10目标年原版B9b vs2026 May Accuracy回顾RTO+9/10MW差，状态`UNEXPLAINED_SOURCE_DIFFERENCE`。
- [标准库复算](../analysis/recompute_h03_b9b_vintage_decomposition.py)：可附三档原始官方XLSX与SHA实现单元格对账；2026 B9含2026-02-06更正，2025/26`B9b−B9`为统计构造非实际运行MW。

## H03第十一轮｜Jan/Feb附件、EKPC/PSA来源差异（2026-11-14）
- [h03_pjm_2026_ekpc_source_reconciliation_2026_2046.csv](h03_pjm_2026_ekpc_source_reconciliation_2026_2046.csv)：21年RTO、EKPC的1/14独立B9b、2/6更正独立B9、合并B9/B9b、5月回顾比较，四原XLSX SHA逐行登记；1/14 B9b与2/6 B9属于混合日期，差不能冒充同版初稿勘误。
- [h03_pjm_2026_ekpc_zone_source_match_summary.csv](h03_pjm_2026_ekpc_zone_source_match_summary.csv)：23顶层zone×21年两组比较的不同值数量，仅EKPC/RTO不同，其他21个zone全年份一致。
- [h03_pjm_2026_jan_feb_publication_manifest.csv](h03_pjm_2026_jan_feb_publication_manifest.csv)：独立B9b、订正B9、当前合并、五月Accuracy、2025引入B9b说明的原始URL/大小/SHA和PIT边界；另[1月月度PSA排除附件](https://www.pjm.com/-/media/DotCom/planning/res-adeq/load-forecast/total-monthly-load-adjustments.xlsx)见来源表。
- [h03_pjm_2027_rto_baseline_publication_sensitivity.csv](h03_pjm_2027_rto_baseline_publication_sensitivity.csv)：2027在三个不同RTO forecast来源比较的-1855/-1860/-1865MW，**不能混日期当实体损失**。
- [标准库4原始文件核验脚本](../analysis/recompute_h03_ekpc_source_reconciliation.py)、[完整报告](../reports/2026-11-14_h03_ekpc_jan_vs_feb_release_reconciliation.md)。


## 2026-04-07正式县书记官Minutes + H10 BEA连续33个月（补充）
- [Travis County 2026-04-07 Item26与Item6官方决议台账](../cases/musk-2026/travis_official_votes_20260407.csv)记录4-0+1弃权的**9%合格grant扣留**、同时2025—26后续社区项目批准、原始PDF/Transcript SHA及发布日期，主证据E083—E085；**实际扣留USD未确认**。[原始会议专项研究](../reports/2026-11-14_h09_official_minutes_primary_confirmation.md)。
- [BEA官方NIPA 2024-01—2026-09共33个月headline/core PCE指数](h10_bea_nipa_pce_headline_core_2024_2026_snapshot.csv)，来源原始Excel SHA，完整环比/同比；[复算PASS脚本](../analysis/recompute_h10_bea_snapshot.py)；[数据版本报告](../reports/2026-11-14_h10_bea_pce_monthly_series_and_vintage.md)。2026-11-14后见修订不能伪装作历史每月首发版本。


## H10：18个有效月份的CPI/PCE同月相关性（截至2026-11-14）
- [CPI与PCE按月对齐CSV](h10_cpi_pce_aligned_monthly_2025_2026.csv)含21个日历月份，明确保留2025-01、2025-10、2025-11的CPI缺失，**只有18个有效同比源中同月环比配对**；并非两组全时段都有有效数据。 [Python标准库复算](../analysis/recompute_h10_cpi_pce_alignment.py)在Ubuntu实际运行PASS：headline r=0.946129、core r=0.553099。 [完整分析](../reports/2026-11-14_h10_cpi_pce_alignment_18_month_sample.md)。该关联仅为同月数据描述，不代表Fed因果/市场预测。

## H03第十二轮：勘误前B9原始字节门槛
- [h03_pre_correction_b9_source_availability.csv](h03_pre_correction_b9_source_availability.csv)：10个来源状态，含Jan原PDF的页数/字节/SHA、Jan独立B9b、Feb订正B9、当前合并与五月回顾，Wayback访问超时和外部镜像情况；未获得的bytes、SHA保留**空字段**而非数值零。
- [h03_rto_2025_2026_summer_vs_b9b_revision_magnitude.csv](h03_rto_2025_2026_summer_vs_b9b_revision_magnitude.csv)：2027—2030两个模型预测总量修订的绝对幅度比，**B9b含已嵌入模型成分，不可当政治/数据中心实际贡献率**。
- [离线复算及PDF可选SHA核对](../analysis/recompute_h03_pre_correction_source_gate.py)，[完整研究报告](../reports/2026-11-14_h03_uncorrected_b9_source_gate.md)。


## H09州官方380/381记录+H10 CPI事件日稳健性（2026-11-14）
- [Texas Comptroller公开380/381 CSV单条登记及SHA](../cases/musk-2026/texas_comptroller_0005328_registry_snapshot.csv)：Travis County×Colorado River Project LLC编号0005328，州备案2022-05最近更新、总货币值空白非零、截止日期与县签署合同差一天。[来源/不能算9%实际美元的报告](../reports/2026-11-14_h09_texas_381_registry_missing_cash_audit.md)，[2020/21/22独立年度金额空值记录](../cases/musk-2026/travis_2020_2022_grant_cash_reconciliation.csv)。2020签约新闻十年估算不能乘9%冒充官方实际现金扣留。
- [22个真实CPI公布日×Treasury日度2Y/10Y CSV](h10_cpi_release_treasury_2y10y_2025_2026.csv)，2025-01—2026-11与非公布交易日444个对照；[同月20,000次随机化+去异常稳健性](../reports/2026-11-14_h10_cpi_release_ust_22_event_robustness.md)，[标准库计算脚本](../analysis/recompute_h10_cpi_release_ust_events.py)。该统计结果是日度关联，未取得当天预发布CPI一致预期/期货分解，不能认定利率变动由CPI造成。

## H03第十三轮：FERC专家附件EN1引用错表的源级实证（2026-11-14）
- [h03_ferc_en1_2023_solar_vs_b9_six_years.csv](h03_ferc_en1_2023_solar_vs_b9_six_years.csv)：2023版2023—28六个目标年，EN1与原PJM B8a Distributed Solar完全相同，但与B9 Large Load完全不同；逐年误差MW和占RTO夏季峰值%。
- [h03_ferc_en1_y5_adjustment_share_audit_2017_2026.csv](h03_ferc_en1_y5_adjustment_share_audit_2017_2026.csv)：10版每版第5年比较；**2017—22只有诉讼附件二手尚未逐年核PJM原件**，2023做B9纠正，2024—26有先前原版来源支持；不当作十年完备PIT回测。
- [h03_ferc_en1_pdf_source_mapping.csv](h03_ferc_en1_pdf_source_mapping.csv)：诉讼原件与PJM2023官方B8a/B9、2024方法课件的源PDF SHA和零基页码；不因诉讼提出便当FERC批准监管规则。
- [标准库六格自动验证和可选双PDF SHA校验](../analysis/recompute_h03_ferc_en1_table_source_audit.py)及[研究报告](../reports/2026-11-14_h03_ferc_en1_solar_table_mismatch.md)。


## 2020—22县Grant绩效年→付款年与2023—26 CPI扩样（v0.2.4）
- [Travis County原合同2020—22履约年与正常付款年2年错位映射](../cases/musk-2026/travis_grant_payment_cohorts_2020_2022.csv)及[合同分段审计](../reports/2026-11-14_h09_grant_payment_year_lag_contract_audit.md)，正常2022—24的10月31日目标日期均为**有条件应付款日，未核实际支付/9%扣留USD**。
- [正式2026-04-07县Agenda Packet 255页两项议案CSV](../cases/musk-2026/travis_20260407_agenda_packet_documents.csv)与[文件SHA及页面核验](../reports/2026-11-14_h09_agenda_packet_255pages_no_grant_figures.md)，公开Agenda Item6/26皆Attachments None，Fiscal Impact栏空白。不能把“公开文件没有附表”当县本身没有付款记录。
- [2023/24美国Treasury官方2Y/10Y 500交易日](h10_us_treasury_2y10y_daily_2023_2024.csv)合并[2025/26 467日](h10_us_treasury_2y_10y_daily_2025_2026.csv)，以BLS实际日历形成[46事件日表](h10_cpi_release_ust_46events_2023_26.csv)。[完整分期结果及非因果限制](../reports/2026-11-14_h10_cpi_release_ust_46event_historical_robustness.md)，[完整标准库复算](../analysis/recompute_h10_cpi_release_treasury_2023_26.py)已运行PASS；未获得发布前市场共识/分钟收益率时不评价Fed决策因果。


## 2025-11县级无已发返利报道和2026-11-10 CPI预期差（v0.2.5）
- [Travis County县级税惠2025-11没有发放的媒体纪实](../cases/musk-2026/travis_rebate_disbursement_status_asof_2025.csv)（Statesman与KUT同源，不是Auditor原始付款账）；[报告](../reports/2026-11-14_h09_no_rebates_reported_2025_cash_status.md)。**不能外推到2026/11无付款**，不可用报道的“零已发”填合同总金额或Grant eligible基数。
- [2026-11-10单事件15行数据源/时间戳/季调口径表](h10_20261110_cpi_consensus_fedwatch_rate_event.csv)、[完整报告](../reports/2026-11-14_h10_cpi_20261110_true_preconsensus_fedwatch_rate_anchor.md)、[离线检查脚本](../analysis/recompute_h10_20261110_cpi_pit_anchor.py)已由Ubuntu基于GitHub真数据运行PASS。Pre-release预测0.3/0.2月环比、BLS实际0.4/0.3，各+0.1pp；Cboe引用周一/周二FedWatch +25bp情景概率84→90.5%、周二+50bp9.5%，仅为报道级日度快照，不是前后5分钟独立因果。BLS SA与NSA指数以及未校时间的两家日历forecast不能混用。


## H09正式2022支付基线与H10十次可核事前预期（v0.2.6）
- [Travis County2022官方项目汇总对应的有日期状态](../cases/musk-2026/travis_rebate_disbursement_status_asof_2025.csv)：2022-01-31零返利已支付、绩效年1验收待完成（F类官方概览），与2025新闻引用无已付、2026正式9%扣留分日期；[事实与局限报告](../reports/2026-11-14_h09_county_official_2022_zero_rebates_baseline.md)。不将历史零付款外推到2026实付。
- [10次有真正事前日期的专业CPI预测/BLS首发/UST有符号日变动](h10_cpi_pre_release_dated_forecasts_10events_2023_2026.csv)与[46份事后供应商日历（均非PIT）](h10_cpi_release_ust_46event_vendor_archive_not_pit.csv) **分别留在两个数据库**。前者10例中8例核心surprise非零、7例2Y非零、6例方向一致，双侧p0.125；后者46日期headline/core各有28例可见预测但源时间不明，不得计算专业前瞻命中。[专业报告](../reports/2026-11-14_h10_pre_release_forecasts_10_pit_vs_vendor_not_pit.md) · [方向二项检验](../analysis/recompute_h10_pre_release_cpi_surprise_10_events.py) · [来源冲突验证](../analysis/audit_h10_dated_vs_archive_forecast_conflicts.py)，两个程序经Ubuntu基于Github实际CSV跑通PASS。


## Ch313 Del Valle税基限制与2025同发布者CPI事前预测样本（v0.2.7）
- [H09 Texas Comptroller Del Valle ISD #1496 Chapter313 两版CDR×税年14行](../cases/musk-2026/delvalle_ch313_1496_2023_vs_2025_vintages.csv)，含两份原始XLSX URL/SHA、正式posted日期、税年是否未来预测、学区税负差及Revenue Protection/Supplemental Payments，和[版本差解释](../reports/2026-11-14_h09_delvalle_ch313_official_tax_saving_vintage_comparison.md)。**与Travis县381返利实际支付完全分开**，两次Excel读取/恒等式/差额已Ubuntu实际运行PASS。
- [H10 2025年全部11次真实CPI发行中同一来源Calculated Risk仅7条提前时间戳的专业共识及4条NA](h10_cpi_consistent_publisher_2025_pre_release_cohort.csv)；[固定来源方向反证报告](../reports/2026-11-14_h10_2025_uniform_publisher_cpi_surprise_direction_falsification.md)，[独立复算脚本](../analysis/recompute_h10_2025_consistent_publisher_cpi_direction.py)运行PASS：Headline非零surprise同向2/5，Core2/4，双侧Exact p皆1.0，不复现此前混源10事件Core6/7。**历史完整性只有7/11且Treasury是整日波动，不能推断预测胜率和CPI独立因果。**
