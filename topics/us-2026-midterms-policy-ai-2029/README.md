# TOPIC-011｜2026美国中期选举→2029政治财政AI投资与市场路径

> **研究状态：FRAMEWORK_READY，H01—H10均UNTESTED。** 版本 0.2.4；基线/资料截点 2026-11-14。研究起止：2026-11-03—2029-01-20。总入口：[Issue #41](https://github.com/fweiger/AI_book/issues/41)。本专题是**可证伪、多路径共存、多AI长期研究**，不是为任何一个预言找证据。

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
- **新统一研究层**：[专家档案/作品库](experts/README.md) → [观点来源池](views/README.md) → [观点×假说映射](hypotheses/view_hypothesis_links.csv) → [H01—H10](HYPOTHESES.md) → [因果链及逐边检验](chains/README.md) ↔ [统一指标目录（以catalog实时条目为准）](metrics/README.md) ↔ [事件数据/反证](data/evidence_events.csv)。
- **案例专线**：[马斯克Texas/国会/赦免/现金流](cases/musk-2026/README.md) · [H09研究任务 #55](https://github.com/fweiger/AI_book/issues/55) · [CPI/PCE→Fed→融资H10研究任务 #56](https://github.com/fweiger/AI_book/issues/56)。
- [外部财经评论者/UP主观点池（独立观点与事实分离）](views/README.md) · [大湾区老姚2026-11-14观点核查卡](views/2026-11-14-dayawanqu-laoyao.md) · [可机读主张表](views/claim_register.csv) · [观点池长期跟踪Issue #54](https://github.com/fweiger/AI_book/issues/54)

## H09/H10第一轮真实数据（2026-11-14）
- [H09 Texas县签署合同、选前9%优惠扣减与SEC财报审计](reports/2026-11-14_h09_travis_texas_incentive_preelection_control.md)：已取得**2020 Travis County签署原件**，2026-04据KUT报道已扣减部分2020—22应得补助9%，**发生在2026-11选举前**；Tesla SEC披露2023—25相关grant不重大；SpaceX Starbase新税惠仅是2026-12-09未来听证，拟投240亿美元≠获批补贴。具体的实际美元损失、县正式4月会议纪要、2027新政府新增因果仍NA。
- [H10 22个月BLS CPI指数、467交易日UST、BEA修订与真实Fed决议](reports/2026-11-14_h10_cpi_pce_fomc_treasury_pit_baseline.md)：Ubuntu执行[离线复算脚本](analysis/recompute_h10_open_data.py)PASS；2026-11-09→10两年期UST+17bp，十年期+10bp；BEA八月core PCE后验修订0.2→0.3说明必须按发布版本PIT，勿将后续数据当此前FOMC已知。无独立因果回归或企业融资结果。

## H09县议案一手确认与H10 BEA连续月度数据（2026-11-14补核）
- [Travis County县书记官2026-04-07官方Minutes/Transcript](reports/2026-11-14_h09_official_minutes_primary_confirmation.md)：**议案26 4票赞成0反对1弃权，扣留2020—22合格grant的9%**；同日**议案6**亦以4-0、1弃权批准2025—26社区投入方案。县政府原始文书PDF、SHA与逐议案台账均已核到[H09县级原始表](cases/musk-2026/travis_official_votes_20260407.csv)；这一行为早于选举、尚未取得扣留绝对USD与实际追回款，不能称2027政治效应。
- [BEA NIPA官方连续33个月整体/核心PCE季调指数](data/h10_bea_nipa_pce_headline_core_2024_2026_snapshot.csv)：2024-01至2026-09，2026-09核心PCE环比0.3165%、同比3.1212%；[BEA来源版本说明](reports/2026-11-14_h10_bea_pce_monthly_series_and_vintage.md)及[离线复算脚本](analysis/recompute_h10_bea_snapshot.py)已在Ubuntu实际运行**PASS**。2026-11-14取回版不是每个月原始首发PIT。

## H10 18个月CPI/PCE环比实证对照（2026-11-14）
- [CPI和PCE同月变化的描述性统计](reports/2026-11-14_h10_cpi_pce_alignment_18_month_sample.md)：2025-01—2026-09共21个月，因CPI起始和2025年10月缺值，只有**18个月有效配对**。整体月环比Pearson `r=0.946129`，核心月环比`r=0.553099`；这意味着核心两种通胀指标并非简单替代品，**并不证实美联储因果或加息预测**。[21行含缺失CSV](data/h10_cpi_pce_aligned_monthly_2025_2026.csv)和[离线复算PASS](analysis/recompute_h10_cpi_pce_alignment.py)。

## H09州级协议与H10 22次CPI事件（v0.2.3）
- [H09 Texas Comptroller官方381协议登记与金额缺失审计](reports/2026-11-14_h09_texas_381_registry_missing_cash_audit.md)：确认协议0005328唯一匹配Colorado River Project LLC/Travis County，但州数据库`totl_agmt_am`是**NA不是$0**、last_update停于2022-05、州截止日2041-12-30与县原签合同12-31不一致；2026-04决议9%金额尚未核算，不能用2020签约时估算10年优惠$14m来乘9%。
- [H10 BLS 22个CPI发布日对US Treasury 2Y/10Y波动及强反例](reports/2026-11-14_h10_cpi_release_ust_22_event_robustness.md)：2Y发布日绝对变化5.2727bp vs同月随机日3.9813bp，探索性未校正p=0.0483；**排除2026-11-10后p=0.1389**、分年不达0.05，说明初步统计不稳健，不能直接宣称CPI因果/交易策略。附[22事件CSV](data/h10_cpi_release_treasury_2y10y_2025_2026.csv)与[离线复算程序](analysis/recompute_h10_cpi_release_ust_events.py)。

## 四年46次CPI事件研究与县拨款支付年度拆解（v0.2.4）
- **H09**：[2020—22履约年→2022—24有条件付款年度的合同审计](reports/2026-11-14_h09_grant_payment_year_lag_contract_audit.md)：正常时间表与实际现金分开，不把withhold扣留当成已付后recapture。另实读[2026-04-07县议会103MB/255页官方Agenda Packet](reports/2026-11-14_h09_agenda_packet_255pages_no_grant_figures.md)，页15(Item6)与页253(Item26)明确附件None/财政栏空白，未有真实eligible grant/ACH美元；[原始文件SHA与两项审计CSV](cases/musk-2026/travis_20260407_agenda_packet_documents.csv)。不能把缺失当0或2020签约多年度估算当实付。
- **H10**：[2023—2026共46次CPI发布日、967个Treasury真实交易日的历史扩样](reports/2026-11-14_h10_cpi_release_ust_46event_historical_robustness.md)：2023—24 2Y当日绝对波动8.875bp vs同月安慰剂5.485bp，2025—26仅5.273 vs3.978bp；四年46次有符号2Y变化21涨22跌3不变。完整20,000次随机化、异常日剔除及分期结果[可复算PASS](analysis/recompute_h10_cpi_release_treasury_2023_26.py)；**因果仍UNTESTED**，这不是加息概率预测或策略收益。

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

## H03第十轮｜2025原版与2026勘误原版的B9/B9b修订分解（2026-11-14）
- [完整原始来源实证报告](reports/2026-11-14_h03_b9b_vintage_decomposition_2025_2026.md)：PJM同目标2027 RTO额外调整B9 **13668→10785MW**(−2883)，总量B9b **17721→15856MW**(−1865)，差额部分B9b−B9 **4053→5071MW**(+1018)。Dominion总上修+740，AEP−902，PPL−1134；同源数据覆盖2026—2035共60条区域/年份，并独立核对2026 Accuracy RTO存在9—10MW未解版本差。2026 **B9明确有2026-02-06修正**，不能宣称初版2026-01-14数值；**预测不是实际AI数据中心投资或政治因果**。附[60行机器面板](data/h03_pjm_2025_2026_original_b9_b9b_revisions.csv)、[7区域分解](data/h03_pjm_2027_original_zone_revision_contributions.csv)、[回顾差异](data/h03_pjm_2026_original_vs_accuracy_rto.csv)、[标准库复算与三原始源校验](analysis/recompute_h03_b9b_vintage_decomposition.py)。

## H03第十一轮：2026 B9b初始附件、PSA削峰项及EKPC 21年来源差闭合（2026-11-14）
- [官方四XLSX逐格来源审计](reports/2026-11-14_h03_ekpc_jan_vs_feb_release_reconciliation.md)：1/14独立B9b（Excel元信息1/13）、2/6订正后的独立B9、当前合并B9/B9b和五月Accuracy交叉核验。2026—2046 **23一级zone×21目标年两组对照**中，只有EKPC与RTO出现差异；独立表EKPC=0、合并表EKPC=-10/-9/-8，数值严格解释RTO偏移，5月Accuracy RTO与独立1月B9b全21年一致。PJM月度附件明确**不含PSA削峰调整**；该负值不是纯DC需求取消。2025原版报告确认**B9b首次引入2025**，所以2023/24原版无同源B9b并非文件漏找。2026**2/6订正前B9**仍未找到，不计算修正量。

## H03第十二轮：2/6前原B9来源门槛与RTO预测修订对照（2026-11-14）
- [原B9尚未取得的证据资格审计](reports/2026-11-14_h03_uncorrected_b9_source_gate.md)：PJM 2026-01-14主报告PDF共36页、SHA固定，正文没有完整B9数据附件；独立Jan B9b只能确认Total，2/6以后独立B9与合并Excel都已更正。**不能计算Feb6嵌入负荷修正量（NA）**，并不等于历史版本确实不存在。[来源登记](data/h03_pre_correction_b9_source_availability.csv)、[2027—30整体RTO峰值 vs B9b总量修订规模](data/h03_rto_2025_2026_summer_vs_b9b_revision_magnitude.csv)与[复算脚本](analysis/recompute_h03_pre_correction_source_gate.py)。两组修订规模比2027—29约46—50%，只是绝对值对照，**不是可加的因果份额**。

## H03第十三轮｜FERC诉讼专家EN1的2023“负荷调整”行高度疑似引用了PJM太阳能B8a（2026-11-14）
- [官方双PDF六格对照及完整审计报告](reports/2026-11-14_h03_ferc_en1_solar_table_mismatch.md)：Exelon 2026-11-03向FERC EL27-11-000提交EN1的2023版`Load Adjustments`六目标年**全等于PJM2023原B-8a Distributed Solar（2888/3269/3566/3841/4035/4185MW）**，却**全不等于官方B-9 Above Embedded（2231/3393/4654/6594/8300/9866MW）**；两份官方源SHA已实测。2023版第五年目标2028大型负荷占PJM峰值应为**6.336%**，而诉讼附件误列仅**2.688%**；2026版第五年相对2023第五年的占比倍数从表面**8.079倍**修正为**3.427倍**。这是**诉讼附件来源误引疑点**，不评价当事人动机/诉讼胜负，也不否认真实大型负荷增长。2017—22旧版仅留附件二手数据，未全部核原表。数据见[六格CSV](data/h03_ferc_en1_2023_solar_vs_b9_six_years.csv)与[标准库复算](analysis/recompute_h03_ferc_en1_table_source_audit.py)。
