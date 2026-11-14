# TOPIC-011｜可追踪的知识图谱
- ROOT：问题“2026中期选举后到2029任期终点，美国政治/财政/AI/市场的路径怎样动态变化？”
- P（权力/选举）→ L（立法/行政/地方政策）→ M（净财政/融资/电力/许可）→ E（实体投资/增长）→ Y（市场和选举反馈），每条边待证。
- H01—H10为研究分支内稳定UNTESTED假说；新增H09企业政治暴露和H10通胀/Fed传导，正式数据验证仍待完成。
- P-A—P-D为**非互斥**路径，按时点/国家/企业状态可同时发生。
- K01：H01→H02→H07，财政线；
- K02：H01→H03→H04→H07，AI政策线；
- K03：H01→H05→H06，国际政治线；
- K04：H08→H04→H07，非政治竞争机制；
- K05：H06→H01，选举激励反向反馈，尚未验证。
- 实证所需指标与证据源：[METRICS](METRICS.md)、[SOURCES](SOURCES.md)、[data](data/README.md)。**不能由一件事件证实全条因果链**。

## 外部评论者观点源（非正式因果节点）
- [VIEW来源池](views/README.md) → [VIEW-S001｜大湾区老姚](views/2026-11-14-dayawanqu-laoyao.md) → [10项主张表](views/claim_register.csv) → [事件账本E061—E067](data/evidence_events.csv)。不同评论者相同叙述不能计为独立验证。
- **重要编号修复**：原K07/K08/K09在[因果边CSV](data/causal_edges.csv)已有其他用途；观点层三条候选子链正式改用 `CHAIN-MUSK-TX-01`、`CHAIN-FED-01`、`CHAIN-MUSK-INTERACT-01`，与新增正式H09/H10联合但均UNTESTED。[全部链图](chains/README.md)。

## 新增研究层 v0.2.0
- [EX专家](experts/README.md) → [WORK作品](experts/works.csv) → [VIEW观点](views/claim_register.csv) → [VIEW×H关联](hypotheses/view_hypothesis_links.csv) → [H假说](HYPOTHESES.md) → [CHAIN逐边验证](chains/README.md)。
- [91项统一指标层](metrics/catalog.csv)横向贯穿全部假说；[BLS 2026-10观测样例](metrics/observations_seed.csv)是原始公布数字，不代表已完成时间序列。
- [H09 Texas—国会—赦免案例](cases/musk-2026/README.md)、[H10 CPI/PCE→Fed→融资](chains/README.md)；所有候选因果边状态仍未检验，不因新增节点就成立。
