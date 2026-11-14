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
