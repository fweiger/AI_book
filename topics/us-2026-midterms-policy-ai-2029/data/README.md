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
