# TOPIC-011｜2026美国中期选举→2029政治财政AI投资与市场路径

> **研究状态：FRAMEWORK_READY，H01—H10均UNTESTED。** 版本 0.2.0；基线/资料截点 2026-11-14。研究起止：2026-11-03—2029-01-20。总入口：[Issue #41](https://github.com/fweiger/AI_book/issues/41)。本专题是**可证伪、多路径共存、多AI长期研究**，不是为任何一个预言找证据。

## 核心问题
民主党在2026年中期选举赢得下届国会两院控制权以后，2027-01-03新国会履职是否引发立法对抗、财政支出重配、AI监管/能源约束，进而影响企业投资、增长、金融市场和2028选举策略？各环节能否用真实数据确认？特朗普本届任期于2029-01-20结束，2028选举不是研究终点。

## 五层模型
`P政治权力与选举 → L立法/行政/州县政策 → M财政冲量、金融和电力许可约束 → E实际财政/私人投资和增长 → Y市场及选举反馈`。
**每一条箭头是不同的待检验假说，且允许反向反馈、跨国家对照和链路游走。**

## 研究导航
- [整体假说与机制 FRAMEWORK](FRAMEWORK.md) · [H01—H10详细注册表](HYPOTHESES.md) · [路径状态 PATHWAYS](PATHWAYS.md)
- [可量化指标 METRICS](METRICS.md) · [数据源与PIT事实底座 SOURCES](SOURCES.md) · [审计与识别规则 PROTOCOL](PROTOCOL.md)
- [多AI独立工作合同 COLLABORATION](COLLABORATION.md) · [下一轮 NEXT](NEXT.md)
- [研究问题](questions.md) · [正式论点状态](claims.md) · [知识地图](knowledge-map.md) · [可机读图谱](knowledge-graph.json) · [阅读路线](reading-path.md)
- [CSV数据合同](data/README.md) · [版本记录](CHANGELOG.md) · [过程会话](sessions/README.md)
- **新统一研究层**：[专家档案/作品库](experts/README.md) → [观点来源池](views/README.md) → [观点×假说映射](hypotheses/view_hypothesis_links.csv) → [H01—H10](HYPOTHESES.md) → [因果链及逐边检验](chains/README.md) ↔ [统一91项指标目录](metrics/README.md) ↔ [事件数据/反证](data/evidence_events.csv)。
- **案例专线**：[马斯克Texas/国会/赦免/现金流](cases/musk-2026/README.md) · [H09研究任务 #55](https://github.com/fweiger/AI_book/issues/55) · [CPI/PCE→Fed→融资H10研究任务 #56](https://github.com/fweiger/AI_book/issues/56)。
- [外部财经评论者/UP主观点池（独立观点与事实分离）](views/README.md) · [大湾区老姚2026-11-14观点核查卡](views/2026-11-14-dayawanqu-laoyao.md) · [可机读主张表](views/claim_register.csv) · [观点池长期跟踪Issue #54](https://github.com/fweiger/AI_book/issues/54)

## 11个可直接接手的AI任务
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
| H09 | 企业政商关联、Texas优惠/国会监督与财务后果 | [#55](https://github.com/fweiger/AI_book/issues/55) |
| H10 | CPI/PCE→FOMC预期/决议→再融资成本 | [#56](https://github.com/fweiger/AI_book/issues/56) |

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

## H03额外负对照：2026-07仅供参考的宏观输入更新
- [PJM七月经济输入更新分析](reports/2026-11-14_h03_pjm_july_2026_macro_negative_control.md)：2026-07**仅供参考**同一模型结构、经济输入更新的PJM全系统峰值预测，对2027/28 RTO较2026-01上修593MW(+0.370%)，发生在选举前。附[CSV](data/h03_pjm_2026_july_macro_only_revisions.csv)和[复算脚本](analysis/recompute_h03_pjm_july_macro_update.py)。

## H03秋季负荷申请：容量、需求折算与项目兑现分离（2026-11-14）
- [PJM 2026-10会后官方容量/需求实测结构报告](reports/2026-11-14_h03_sep2026_pipeline_capacity_vs_demand.md)；[145行分区与年份](data/h03_pjm_2026_sep_submission_capacity_demand_zone.csv)；[5年RTO汇总](data/h03_pjm_2026_sep_rto_submitted_pipeline.csv)；[跨来源口径冲突](data/h03_pjm_2026_sep_source_discrepancy.csv)；[双重校验脚本](analysis/recompute_h03_autumn_submission.py)。提交量≠最终接受≠实际投产。

## H03第四轮：Firm合同、数据中心园区接入与收入（2026-11-14）
- [Dominion/AEP签约到运营三层研究](reports/2026-11-14_h03_firm_operating_reconciliation.md)：2026选前ESA合同储备、2024/25实际新增园区及最终容量、2026高负荷客户收入、AEP全国/PJM/ERCOT合同范围对照。附[五份来源范围CSV](data/README.md)及[复算脚本](analysis/recompute_h03_firm_operating.py)。**合同签约、园区带电、计量需求、公司收入不可互相直接作为分母；H03政治因果仍待检验。**

## H03第五轮：70GW队列分层、2027生效的2025州法及真实交付电量
- [Dominion Queue/GS-5/实际MWh一手资料分析](reports/2026-11-14_h03_queue_tariff_physical_delivery.md)：2026-02应用中70GW大型接入点，25GW已有预计接入日期但不是已通电；2025批准的GS-5 2027-01-01生效；Dominion 2026年前三季总交付80.6百万MWh vs2025同期76.1百万（+5.91%，**非数据中心专属**）；天气等混杂另记，数据+代码见[DATA](data/README.md)。

## H03第六轮：DC专属实际峰值、未来纯DC预测、双登记制度（2026-11-14）
- [PJM数据中心4GW实测与2027–29预期及SCC/PJM登记状态](reports/2026-11-14_h03_registry_and_dc_peak_baseline.md)：Dominion 2025纯数据中心同时峰值约4GW、2026-01锁定的2027/2028/2029预测4933/5448/5980MW；公司CLOA+ESA Firm阶段占比2025-12 43.71%→2026-09 40.07%，虽绝对规模21.2→22.0GW；2026-07 PJM约3800MW真实负荷转移事件。SCC 2026-10-23**仍继续审理**，PJM 50MW Registry **被FERC接受**但只要求公开区域汇总。数据源、可比性和[标准库复算](analysis/recompute_h03_matured_dc_baseline.py)。[SCC项目数据追踪Issue #52](https://github.com/fweiger/AI_book/issues/52)。


## H03第七轮：31条历史预测版本真实回测 × 2026-11-02 CRA供电约束竞争路径
- [完整预测误差及CRA反事实报告](reports/2026-11-14_h03_vintage_backtest_cra_competing_path.md)；[PJM31条forecast-vs-actual](data/h03_pjm_load_forecast_vintage_backtest_2023_2025.csv)、[同批三区WAPE/MAPE](data/h03_pjm_2025_paired_vintage_scorecard.csv)、[CRA机制与情景](data/h03_cra_nov2026_scenario_assumptions.csv)、[离线+SHA源校验脚本](analysis/recompute_h03_vintage_calibration.py)。**相同2025目标三地区MAPE改善，但WAPE恶化**，说明模型版本修订/区域规模权重会影响未来政治归因；CRA估计2030硬供电约束可能造成约11.5GW缺口（非已实现，也非政治已造成）。


## H03第八轮：历史值和预测值的公开版本漂移（2026-11-14）
- [完整数据来源审计报告](reports/2026-11-14_h03_publication_vintage_bias_audit.md)：PJM 2025-06公布2014—24历史RTO值，与2026-05回顾报告中的`Historical July Peak`在11个共同年份都不一致，后者高约2.34%—5.26%、中位3.966%。同2023/24/25预测版本的21个同目标年数值在不同来源亦有差异；**未核实是定义、月份还是历史更新，不得直接称为已发生的新增负荷或政治因果**。附[11年历史表](data/h03_pjm_rto_2014_2024_cross_publication_history.csv)、[21个预测差表](data/h03_pjm_rto_2023_2030_cross_publication_forecasts.csv)、[3个误差敏感性情景](data/h03_pjm_rto_2023_2024_error_definition_sensitivity.csv)、[离线及双原表校验](analysis/recompute_h03_source_vintage_audit.py)。


## H03后续实证｜原版Table B9与B9b不同计量范围的精确审计（2026-11-14）
- [完整数据分析报告](reports/2026-11-14_h03_embedded_bridge_and_original_vintages.md)：2025官方原版**同一Excel**中2025 RTO B9“Above Embedded”3591MW、B9b“Total Associated”7729MW，差4138MW；其中DOM3286MW(79.41%)、AEP349MW(8.43%)、其余503MW。2023/24原版B9与2025六月Total跨文档对照约分别差1726/3018MW，但**非同一份发行文件，不可直接当精确嵌入MW**。不同出版物还会反转2025预测版本的误差排名（原始口径未严格对齐），见[数据明细](data/h03_pjm_original_above_embedded_vs_total_bridge_2023_2030.csv)、[同源zone桥接](data/h03_pjm_2025_within_workbook_zone_bridge.csv)、[标准库复算](analysis/recompute_h03_original_bridge.py)。
