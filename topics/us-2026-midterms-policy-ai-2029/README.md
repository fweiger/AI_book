# TOPIC-011｜2026美国中期选举→2029政治财政AI投资与市场路径

> **研究状态：FRAMEWORK_READY，H01—H08均UNTESTED。** 版本 0.1.0；基线/资料截点 2026-11-14。研究起止：2026-11-03—2029-01-20。总入口：[Issue #41](https://github.com/fweiger/AI_book/issues/41)。本专题是**可证伪、多路径共存、多AI长期研究**，不是为任何一个预言找证据。

## 核心问题
民主党在2026年中期选举赢得下届国会两院控制权以后，2027-01-03新国会履职是否引发立法对抗、财政支出重配、AI监管/能源约束，进而影响企业投资、增长、金融市场和2028选举策略？各环节能否用真实数据确认？特朗普本届任期于2029-01-20结束，2028选举不是研究终点。

## 五层模型
`P政治权力与选举 → L立法/行政/州县政策 → M财政冲量、金融和电力许可约束 → E实际财政/私人投资和增长 → Y市场及选举反馈`。
**每一条箭头是不同的待检验假说，且允许反向反馈、跨国家对照和链路游走。**

## 研究导航
- [整体假说与机制 FRAMEWORK](FRAMEWORK.md) · [H01—H08详细注册表](HYPOTHESES.md) · [路径状态 PATHWAYS](PATHWAYS.md)
- [可量化指标 METRICS](METRICS.md) · [数据源与PIT事实底座 SOURCES](SOURCES.md) · [审计与识别规则 PROTOCOL](PROTOCOL.md)
- [多AI独立工作合同 COLLABORATION](COLLABORATION.md) · [下一轮 NEXT](NEXT.md)
- [研究问题](questions.md) · [正式论点状态](claims.md) · [知识地图](knowledge-map.md) · [可机读图谱](knowledge-graph.json) · [阅读路线](reading-path.md)
- [CSV数据合同](data/README.md) · [版本记录](CHANGELOG.md) · [过程会话](sessions/README.md)

## 9个可直接接手的AI任务
| 工作ID | 核心研究 | Issue |
|---|---|---|
| H01 | 制度对抗与行政阻断 | [#42](https://github.com/fweiger/AI_book/issues/42) |
| H02 | 财政冲量与支出重配置 | [#43](https://github.com/fweiger/AI_book/issues/43) |
| H03 | AI监管、能源与数据中心许可 | [#44](https://github.com/fweiger/AI_book/issues/44) |
| H04 | AI投资指引与实际CAPEX | [#45](https://github.com/fweiger/AI_book/issues/45) |
| H05 | 外交、关税、国防重心迁移 | [#46](https://github.com/fweiger/AI_book/issues/46) |
| H06 | 2028选举激励 | [#47](https://github.com/fweiger/AI_book/issues/47) |
| H07 | 金融市场与宏观传导 | [#48](https://github.com/fweiger/AI_book/issues/48) |
| H08 | 非政治AI周期与全球对照 | [#49](https://github.com/fweiger/AI_book/issues/49) |
| DATA-00 | 数据源、PIT与统一证据账本 | [#50](https://github.com/fweiger/AI_book/issues/50) |

## 明确边界
- AP已宣布民主党赢得2027年参众两院多数，但选举认证/席位细节应动态更新；民主党并非在2026-11已经开始控制新一届国会。
- 新国会能制约总统，**不能自动强迫其执行所有政策**；否决权、党内分歧、参院程序、司法审查均重要。
- FY2026财政赤字是**选举前结束的财年**；企业AI投资的2027预测**不是实现值**。
- 起点为用户提供的非公开视频文字分析；本仓库只保存**原创假说摘要**，不公开其本地音频、转写全文或设备路径。
- [TOPIC-008 NVIDIA/Megaspeed #27](https://github.com/fweiger/AI_book/issues/27)保留为独立可核验政商案例；不能自动推断为本研究的政治因果。

## M0真实数据（2026-11-14新增）
- [第一轮H02/H04定量观察](reports/2026-11-14_m0_readout.md)：财政部API的2015—2026年12个10月、FY2026相对CBO基线差异、五家大型科技企业选前CAPEX。脚本：[recompute_m0.py](analysis/recompute_m0.py)。**仅描述统计，尚不能认定政治因果**。

## H03州级政策、电网预测及联邦法案（2026-11-14）
- [H03第一轮政策→电力负荷报告](reports/2026-11-14_h03_policy_grid_baseline.md)：Virginia已经生效的数据中心用电税、100MW新建选址规则、PJM 2026-01选前预测修订、选后旧国会BAAJA程序投票。附[来源级事件表](data/h03_policy_events_2026.csv)、[PJM预测修订CSV](data/h03_pjm_forecast_revisions_2026.csv)、[税率敏感性CSV](data/h03_va_electricity_tax_scenarios.csv)、[离线复算脚本](analysis/recompute_h03_m0.py)。**已生效法律≠已证明建设延期**。

## PJM 2025实际负荷与不同版本预测的首次数值对照（2026-11-14）
- [H03第二轮PJM真实兑现偏差与预测版本分析](reports/2026-11-14_h03_pjm_large_load_realization.md)：PJM 2025实际大型负荷、2025版预测误差、四区可比覆盖97.8%、Dominion差异、2026版对2027和2035大型负荷的反向修订。数据：[2025分区](data/h03_pjm_2025_zone_observed_vs_forecast.csv)、[历史2019–25](data/h03_pjm_historical_july_2019_2025.csv)、[版本修订](data/h03_pjm_2025_to_2026_vintage_revisions.csv)、[独立校验](analysis/recompute_h03_pjm_accuracy.py)。
