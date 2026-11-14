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
