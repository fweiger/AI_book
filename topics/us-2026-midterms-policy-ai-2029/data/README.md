# TOPIC-011｜M0机器注册表

- [hypothesis_registry.csv](hypothesis_registry.csv)：H01—H08，初始状态UNTESTED。
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
