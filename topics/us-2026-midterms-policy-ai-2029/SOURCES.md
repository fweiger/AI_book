# TOPIC-011｜官方数据源与初始事实

| source_family | 入口 | 用途 | 认识论限制 |
|---|---|---|---|
| AP-RESULT | https://www.ap.org/the-definitive-source/behind-the-news/calling-control-of-congress-in-the-2026-midterm-elections/ | 2026中期选举后两院多数归属，AP于11-03/04宣布 | AP判定非所有席位正式认证；新国会2027-01-03就职 |
| CONGRESS | https://www.congress.gov/ | 法案原始文本、审议状态 | 提交≠通过≠签署≠生效 |
| SENATE | https://www.senate.gov/legislative/votes_new.htm | 唱名投票与程序 | 记录参院门槛 |
| CBO-BASE | https://www.cbo.gov/publication/62105 | 2026-02预算/经济前瞻，**选前可得** | 不可用2027修订倒填2026-11-02 |
| CBO-FY | https://www.cbo.gov/publication/61986 | 2026-11-09公布FY2026赤字约$2.0万亿、同比+12% | 财年2026-09-30结束，**不是选后执政效果** |
| TREASURY | https://fiscal.treasury.gov/accounting/monthly-treasury-statement | 联邦财政月度收支 | 季节性/修订/会计定义 |
| BEA | https://www.bea.gov/ | 实际GDP和固定投资 | 信息设备投资不等于全是AI |
| CENSUS | https://www.census.gov/construction/c30/release.html | 月度建筑支出发布时间 | 分类不能无依据替换成AI数据中心 |
| SEC | https://www.sec.gov/search-filings/edgar-application-programming-interfaces | 公司正式CAPEX/资本化、财报发布 | 会计年度/指引与实现区分 |
| EIA | https://www.eia.gov/ | 发电、电力需求/电价 | 用电并非纯AI |
| FERC | https://www.ferc.gov/ | 并网、电力监管 | 联邦/州/县权限区别 |
| FEC | https://www.fec.gov/ | 2028竞选融资 | 竞选激励只能做代理指标 |

## 竞争性分析（只是预测）
1. **选前2026-10-05** Reuters引述Goldman将2027年底美国数据中心容量预测调整至约90GW：https://www.reuters.com/business/goldman-sees-us-data-center-growth-intact-despite-opposition-2026-10-05/ 。GW容量≠CAPEX美元。
2. **选后2026-11-12** Reuters引述Goldman预期2027年底AI硬件+IP投资**年化**约1.4万亿美元：https://www.investing.com/news/economy-news/ai-to-stay-dominant-force-behind-us-business-investment-in-2027-goldman-says-5020672 。**预测不等于实际经济投资**。
3. **2026-11-13** Reuters关于2027年民主党立法优先级：https://www.reuters.com/legal/government/us-congress-democrats-plot-must-have-victories-2027-2026-11-13/ 。政策计划不等于通过法律，也为“财政必缩”提供竞争解释。

## 来源级别
L0仅标题线索；L1机构、发布日期和链接已确认；L2直接核查所述段落与定义；L3多个**真正独立**一手源比对；L4复算量化结果并报告负结果。转载/同一匿名来源的多篇报道不能充当多份独立证据。预测必须记录“当时已可知/未来才发布”的PIT标签。

## M0新增已读取数据与时间戳
- [Treasury MTS Table 1 API](https://api.fiscaldata.treasury.gov/services/api/fiscal_service/v1/accounting/mts/mts_table_1)：在Ubuntu MCP执行官方请求，`record_calendar_month:eq:10`返回204行，每年报告里当前FY/上FY有两个October，必须选**当前财年**。保存[12年快照](data/treasury_october_2015_2026.csv)，所有值美元十亿，截到3位；提取于2026-11-14。2026-10财政记录**11-12才发布**，非选前可知。
- [CBO 2026-02-11展望](https://www.cbo.gov/publication/61882)为PIT预测，[CBO 2026-11-09 FY总结](https://www.cbo.gov/publication/61986)解释FY2026实际/基线差异；本研究将预测与事后数据分开。
- 选前企业原始业绩：[Meta](https://investor.atmeta.com/investor-news/press-release-details/2026/Meta-Reports-Third-Quarter-2026-Results/default.aspx) / [Alphabet](https://abc.xyz/investor/events/event-details/2026/2026-Q3-Earnings-Call-2026-Ujou16CTw9/default.aspx) / [Amazon](https://ir.aboutamazon.com/news-release/news-release-details/2026/Amazon-com-Announces-Third-Quarter-Results/) / [Microsoft](https://www.microsoft.com/en-us/Investor/events/fy-2027/earnings-fy-2027-q1) / [Oracle](https://investor.oracle.com/investor-news/news-details/2026/Oracle-Announces-Q1-Results-Driven-by-Triple-Digit-Growth-in-Cloud-Infrastructure-Revenues/default.aspx)。Oracle FY27 90—95bn来自[非官方电话会转录](https://stockanalysis.com/stocks/orcl/transcripts/689425-q1-2027/)，尚需官方音频复核。
- 详细观测与误判边界见[2026-11-14 M0报告](reports/2026-11-14_m0_readout.md)。

## H03：已核一手法律、程序与电网资料（2026-11-14）
- Virginia[2026预算税项](https://budget.lis.virginia.gov/item/2026/2/HB30/Enrolled/3/3-5.24/)明确`0.011 USD/kWh`、2026-07-01至2028-07-01前；HB153[法条](https://lis.blob.core.windows.net/files/1218748.PDF)于4-13获批准，100MW新建用地评估；HB507[法条](https://lis.blob.core.windows.net/files/1217630.PDF)规定新空气许可对备用发电机排放要求；州长[2026-08-05公告](https://www.governor.virginia.gov/newsroom/news-releases/2026/august-releases/name-1122057-en.html)说明电网专用升级成本分担，但SCC原始裁定待读。
- PJM[2026-01-14发布](https://insidelines.pjm.com/pjms-updated-20-year-forecast-continues-to-see-significant-long-term-load-growth/)：2027/28/29全区域夏季峰值预测相对2025版下修3735/4414/4564 MW；不能误写为数据中心负荷本身下修。
- 美国参议院[2026-09-30 BAAJA提案](https://www.energy.senate.gov/newsroom/press/lee-capito-heinrich-and-whitehouse-introduce-bipartisan-american-affordability-and-jobs-act-of-2026-2/)、[11-07修正案](https://www.energy.senate.gov/press/rep/lee-capito-heinrich-and-whitehouse-release-substitute-amendment-to-bipartisan-american-affordability-and-jobs-act-of-2026/)和[11-09投票73:25](https://www.senate.gov/legislative/LIS/roll_call_votes/vote1192/vote_119_2_00257.htm)、[11-10进入审议动议62:21](https://www.senate.gov/legislative/LIS/roll_call_votes/vote1192/vote_119_2_00258.htm)是不同状态，不能写成法律已经通过。
- 完整核算与信息边界：[2026-11-14 H03报告](reports/2026-11-14_h03_policy_grid_baseline.md)。

## H03新增PJM官方历史/预测同源可比数据（2026-11-14）
[PJM 2026-05-29 Load Forecast Accuracy Report PDF](https://www.pjm.com/-/media/DotCom/planning/res-adeq/load-forecast/2026-load-forecast-accuracy-report.pdf)与[XLSX官方数值源](https://www.pjm.com/-/media/DotCom/planning/res-adeq/load-forecast/2026-accuracy-report.xlsx)，SHA256 `e0f24fe03a79af016826089c653b2c2e15e55edcb04a7bd4be5fa643136425fc`。两台云电脑独立取得同一版本。字段：每个zone的`Historical July Peak`、`2024/2025/2026 Load Forecast July Peak`，数量单位MW。未报告实际的zone留空，DOM subzone不可重复累加，**大负荷调整不能代表纯AI数据中心建设**。见[研究报告](reports/2026-11-14_h03_pjm_large_load_realization.md)。

### PJM July2026宏观预测负对照（非真实电力消耗）
[PJM官方2026-07-24 Mid-Year Update XLSX](https://www.pjm.com/-/media/DotCom/planning/res-adeq/load-forecast/2026-mid-year-update-informational-only.xlsx)；SHA256 `8c2ed5a594c501718dc29755cb044b9d6bcbeac48fc751a6c25014ae1f99a94c`。原表自称For Informational Purposes Only，模型结构与其他假设按原文维持2026-01，仅使用Moody's Analytics June 2026经济预测。指标是**Total Summer Coincident Peak MW**而非Data Center或Large Load Adjustment。见[专门解释](reports/2026-11-14_h03_pjm_july_2026_macro_negative_control.md)。

## 2026年9月PJM大型负荷申请，2026-10-12会后版本
- PJM LAS [官网当日会议记录](https://www.pjm.com/committees-and-groups/subcommittees/las)：2026-09-29会议，10-12公布[官方Informational Only Capacity and Demand Requests XLSX](https://www.pjm.com/-/media/DotCom/committees-groups/subcommittees/las/2026/20260929/20260929-post-meeting---informational-only-capacity-and-demand-requests.xlsx)，SHA256 `211c1f69bfbb52e4e6499b5aa2f42004a65c7def4471d9e84a581e77970d7d51`，28,419字节（北京/武汉MCP独立一致）。两表分别为CAPACITY、DEMAND，各包含DOM子区、PENLC下级与RTO总计；不是最终正式采纳。分区与目标年数据见[第三轮H03](reports/2026-11-14_h03_sep2026_pipeline_capacity_vs_demand.md)。
- Exelon [2026-11-03 FERC投诉档案](https://www.pjm.com/-/media/DotCom/documents/ferc/filings/2026/20261103-el27-11-000.pdf)引用Sept大型负荷请求量与10-12会后表不一致；该文件是**诉讼当事人提交的材料而非PJM最终认可的新预测**，具体数值分歧先进入[冲突台账](data/h03_pjm_2026_sep_source_discrepancy.csv)。
- PJM[ODEC Data Center Demand Forecasting Process](https://www.pjm.com/-/media/DotCom/planning/res-adeq/load-forecast/odec-documentation.pdf)：可核查Firm ESA/CC、LOA或study request不计入、74%计量需求因子和三年爬坡；只针对该公用事业，不当作PJM审批率。

## H03公司合同与业务落地：新的原始资料（2026-11-14）
- [Dominion 2026-10-30 Q3原始投资者演示](https://s2.q4cdn.com/510812146/files/content_files/2026-10-30-DE-IR-3Q-2026-earnings-call-slides-vTC.pdf)：2023-07、2025-12、2026-09签约阶段ELOA/CLOA/ESA；公司报告总量四舍五入而分阶段和可能相差0.1GW。同公司ESA占比不是PJM项目投产率。
- [Dominion 2026 Proxy](https://www.sec.gov/Archives/edgar/data/715957/000119312526115180/d-20260319.htm)：2024/2025分别新接入15/11个园区，园区最终规划容量977/744MW。MW不是当年已实际计量负荷。
- [Dominion 2025 10-K](https://www.sec.gov/Archives/edgar/data/715957/000119312526063120/d-20251231.htm)：数据中心占Virginia Power电力销售2024 26%、2025 28%。
- Dominion 2026 SEC 10-Q [Q1](https://www.sec.gov/Archives/edgar/data/715957/000119312526200275/R16.htm) / [Q2](https://www.sec.gov/Archives/edgar/data/715957/000119312526327487/R36.htm) / [Q3](https://www.sec.gov/Archives/edgar/data/715957/000119312526440697/R16.htm) 的High Load regulated electric sales：含部分非DC/AI客户，美元收入不等于MWh。
- [PJM官方AEP近端负荷与Firm定义](https://www.pjm.com/-/media/DotCom/planning/res-adeq/load-forecast/aep-documentation.pdf)：2025-09同批次11,182MW近端增加，其中>8,600MW签ESA；仅是特定PJM运营范围的历史合同下界。
- [AEP 2026-10-28 Q3公告](https://www.aep.com/news/stories/view/12347/)：新增15GW签约及全区域至2031 84GW的ESA**或**LOA；[AEP SEC Q3](https://www.sec.gov/Archives/edgar/data/73986/000000490426000072/aep-20260930.htm)涉及Texas/ERCOT签约与当地流程暂停，**不能当PJM接受/投入使用**。
- [完整分析与原始数据口径交叉表](reports/2026-11-14_h03_firm_operating_reconciliation.md)。

## H03第五轮：弗吉尼亚州2025批准、2027生效的规定与项目队列（时点反证）
- [Dominion于2026-02-02向SCC提交PUR-2026-00011原申请](https://www.scc.virginia.gov/docketsearch/DOCS/8%40%23101%21.PDF)：约70GW大型接入点请求，25GW已有直至2031预计接入日期、另45GW截至2025-12已分批研究日期；申请非正式批准或已通电，数据发生/报告时间略有差别。
- [SCC 2026-05-12 interim order](https://www.scc.virginia.gov/docketsearch/DOCS/8c5b01%21.PDF)：修订流程须纳入匿名公开项目请求数据库每年至少更新2次、县名/EDC/申请时点/状态/MW，**截至本次未定位该官方库上线网址，也不能把中间命令当最终批准**。
- [SCC 2025-11-25 GS-5决定](https://www.scc.virginia.gov/about-the-scc/newsreleases/release/scc-issues-order-on-dev-biennial-review-2025/scc-rules-in-dev-biennial-review-case.html) / [2026-02官方问答](https://www.scc.virginia.gov/about-the-scc/scc-facts/)：2027-01-01生效，最低14年合同、85%输配电合同需求计费、适用时60%发电、担保最高至最低合约收费60%。这均是**选举前已决定的州监管措施**。
## H03实际交付电量及反证
- [Dominion 2025正式年度报告](https://www.sec.gov/Archives/edgar/data/715957/000119312526115192/dei-ars-12312025.pdf)：Dominion Energy Virginia实际Electricity Delivered 2024=94.5百万MWh、2025=100.2百万MWh。
- [Dominion SEC 2026-09-30 10-Q](https://www.sec.gov/Archives/edgar/data/103682/000119312526440697/d-20260930.htm)：2026Q3实际29.4 vs2025Q3 27.0百万MWh，2026 YTD 80.6 vs2025 76.1百万MWh；同页2026Q3制冷度日1313 vs2025Q3 1066，天气变化需要控制。
- [Dominion 2025公司10-K](https://www.sec.gov/Archives/edgar/data/715957/000119312526063120/d-20251231.htm)：数据中心占Virginia Power电力销售份额26%→28%；尚未验证与Electricity Delivered完全一致的分母，不发布乘积为DC专属MWh。
- [AEP 2026第三季SEC 10-Q](https://www.sec.gov/Archives/edgar/data/73986/000000490426000072/aep-20260930.htm)：2026-09止8个辖区大负荷特殊费率提案已有6个批准，2个待决；ERCOT Batch Zero约45GW请求在2026-07获得约$2bn不同形式的金融担保，**不代表项目投资或通电**。
详细口径分层见[第五轮报告](reports/2026-11-14_h03_queue_tariff_physical_delivery.md)。



## H03第六轮：2026-11-14核实的原始PJM/DC实测与监管文档
- [Dominion 2026-01-06三页给PJM的Data Center Load Adjustment信函](https://www.pjm.com/-/media/DotCom/planning/res-adeq/load-forecast/dominion-documentation.pdf)（[PJM官方2026-02-02 Forecast Adjustment文档入口](https://www.pjm.com/planning/resource-adequacy-planning/load-forecast-dev-process.aspx)）：2025DC专属计量同时峰值约4000MW、2026—46全部公司未来DC同时峰值预测；ELOA不Firm，CLOA被公司视为Firm，ESA近端签约。**公司DC计量值不是DOM整区LLA历史值**。
- [Dominion公司2026-10-30 Q3投资者材料](https://s2.q4cdn.com/510812146/files/content_files/2026-10-30-DE-IR-3Q-2026-earnings-call-slides-vTC.pdf)：2025Dec与2026Sep ELOA/CLOA/ESA同公司阶段库存（历史快照发布日期是2026-10，避免数据泄露）。
- [PJM 2026-08-11大型负荷转移真实事件](https://insidelines.pjm.com/pjm-dominion-review-large-load-transfer-event/)：2026-07-22 07:56北弗吉尼亚230kV线路故障后约3800MW DC/计算负荷切换备用；PJM即时总负荷99984→96205MW，净差3779MW。**这是实际事件观察而非DC总峰值或合同进度**。
- [SCC PUR-2026-00011 2026-10-23官方最新Order](https://www.scc.virginia.gov/docketsearch/DOCS/8fc501%21.PDF)（doc261060105）：案件**continued**，未正式批准Dominion队列标准；[SCC 2026-05-12原始Interim](https://www.scc.virginia.gov/docketsearch/DOCS/8c5b01%21.PDF)与10-23回顾称May25存在**原始日期冲突**，保留而非覆盖。
- [FERC ER26-3515 2026-10-09官方命令](https://elibrary.ferc.gov/eLibrary/docinfo?accession_Number=20261009-3055)、[PJM 2026-11-09 ER26-3515-002合规文件](https://www.pjm.com/pjmfiles/directory/etariff/FercDockets/9976/20261109-er26-3515-002.pdf)：接受≥50MW大型负荷登记并拟10-12生效、**IRAS被驳回**。RAA Schedule 11载明2027-03-01初始报送、公开端仅按区域可能提供汇总并保护商业秘密；未验证项目级公开源上线。[PJM门户](https://www.pjm.com/markets-and-operations/large-load)仍显示旧`Pending`文字，法律状态以FERC为准。
- [第六轮完整研究与历史源冲突审计](reports/2026-11-14_h03_registry_and_dc_peak_baseline.md)，机器状态见[对照表](data/h03_data_discrepancies_and_controls.csv)。

## H03第七轮：PJM历史预测准确率和CRA正式独立场景（2026-11-14）
- [PJM 2026-05-29 Accuracy Report XLSX](https://www.pjm.com/-/media/DotCom/planning/res-adeq/load-forecast/2026-accuracy-report.xlsx)，官方文件SHA `e0f24fe03a79af016826089c653b2c2e15e55edcb04a7bd4be5fa643136425fc`。北京MCP逐Sheet提取2023/24/25版Forecast July Peak和2023/24/25历史Actual July Peak，共31条。原版发行日来自[PJM LAS历年索引](https://www.pjm.com/committees-and-groups/subcommittees/las)：2023-05-22、2024版2023-12-27、2025版2025-01-24。**2026统一回溯表不是本项目当年已预注册**；数据是Large Load Adjustment而非纯DC计量。
- [PJM 2026-11-02 LAS CRA数据中心预测研讨文档](https://www.pjm.com/-/media/DotCom/committees-groups/subcommittees/las/2026/20261102/20261102-item-03---charles-river-associates-review-of-data-center-forecast.pdf)，发布于11月3日中选前一天，采用自下而上项目Firm/许可/预计投产和自上而下AI/芯片/供电等方法，划Tier1—4及移除高风险项目；对2030硬供电约束给出**约11.5GW潜在缺口**，是未来情景、不是事实/政治因果；当前PJМ在全美运行DC电力份额39.9%为模型假设，不应当成长期不变常数。此CRA报告受PJM委托，不能等同于不同利益相关方完全独立的两次验证。
- [历史误差与CRA完整解读](reports/2026-11-14_h03_vintage_backtest_cra_competing_path.md)、[定性/定量CRA假设](data/h03_cra_nov2026_scenario_assumptions.csv)。

## H03第八轮：PJM 2025-06与2026-05出版版本数值不一致
- PJM [2025年6月LAS大型负荷透明度讨论第7页](https://www.pjm.com/-/media/DotCom/committees-groups/subcommittees/las/2025/20250613/20250613-item-03---large-load-adjustment-process-improvement-discussion.pdf)，印发日为2025-06-10（网址目录20250613）。记录2014—2024 RTO Large Load Adjustments History整MW，以及2023/24/25预测版本对同目标年2023—2030的21个数值。这是**2025年当时发布的汇总PPT**，包含后来指标口径不完全一致的可能。
- PJM [2025原版Load Report Tables XLSX](https://www.pjm.com/-/media/DotCom/planning/res-adeq/load-forecast/2025-load-report-tables.xlsx)，SHA256 `a9a797f2d3cf34154db466b74e045d1334dfebede87ec6dc3739805093474ef5`，Table B9b `Total Load Associated with Adjustments to Summer Peak`：RTO 2025预测7729MW，和2025-06 PPT吻合；也存在于[PJM历年资料ZIP](https://www.pjm.com/-/media/DotCom/planning/res-adeq/load-forecast/previous-load-forecast-reports.zip)中，ZIP中央目录实测20项（2007—2025）。
- PJM [2026-05-29准确性XLSX](https://www.pjm.com/-/media/DotCom/planning/res-adeq/load-forecast/2026-accuracy-report.xlsx)，SHA256 `e0f24fe03a79af016826089c653b2c2e15e55edcb04a7bd4be5fa643136425fc`，RTO `Historical July Peak`和各预测标签`Forecast July Peak`。2024历史旧PPT5829 vs新XLSX6135.627MW，2025原版预测7729 vs2026回顾同标签7735MW，**不应把不同“Summer Peak/July Peak/EDC范围”的数值直接解释为真正的历史修订或新增投资**。
- 2025 PJM [预测方法与避免大型负荷double counting的官方说明](https://www.pjm.com/-/media/DotCom/planning/res-adeq/load-forecast/2025-long-term-load-forecast-supplement.pdf)确认需要对历史DC负荷从商用数据、模型输入中剥离和修正，可能影响跨年口径。**它说明存在机制，但尚未直接解释上述每个数字差异。**
- [源版本审计](reports/2026-11-14_h03_publication_vintage_bias_audit.md)严格区分2025-06公开资料、2026-05回顾来源、2025原版报告，而不是一条“唯一正确历史值”。

## H09/H10一手来源及事实与情景界线（2026-11-14）
- [Texas Tribune 2026-11-04](https://www.texastribune.org/2026/11/04/gina-hinojosa-texas-democrat-governor/)及[Houston Public Media 2026-11-11](https://www.knkx.org/2026-11-11/how-the-midterm-election-results-could-impact-elon-musks-many-business-interests-in-texas)：报道Texas新政治格局与Musk企业的潜在政治风险。**这不是州财政部门合同撤销文件**；Texas Comptroller和各市县官方合同待独立核查。
- [Reuters 2026-11-08](https://www.reuters.com/legal/government/democrats-eye-musk-miller-probes-after-midterm-rout-2026-11-08/)：政治人物准备监督，**不是正式传票原件**；后续优先Congress.gov及委员会/法院官方公告。
- [BLS 官方10月CPI原文（2026-11-10发布）](https://www.bls.gov/news.release/archives/cpi_11102026.htm)：headline SA MoM 0.4%，Sep 0.6%；core 0.3%、food 0.5%、energy 0.7%（Sep 5.2%）、shelter 0.3%。严格区分已公布时点与样本月，按指标`I15—I19`进入[七行官方数值种子](metrics/observations_seed.csv)，所有美国同比缺口按[BLS政府停摆FAQ](https://www.bls.gov/cpi/additional-resources/2025-federal-government-shutdown-impact-cpi-faq.htm)逐系列标NA，而非编造。
- [Fed Waller 2026-11-10讲话原文](https://www.federalreserve.gov/newsevents/speech/waller20261110a.htm)：明确个人偏好12月25bp以及高于预期时考虑50bp的条件性发言；其中个人意见不同于委员会投票/宣告。
- 宏观长期：`I20/I21/I54` BEA [PCE指数](https://www.bea.gov/data/personal-consumption-expenditures-price-index)、`I23/I24` [FOMC声明会议](https://www.federalreserve.gov/monetarypolicy/fomccalendars.htm)、`I26/I27` [美国财政部收益率](https://home.treasury.gov/resource-center/data-chart-center/interest-rates/pages/textview?type=daily_treasury_yield_curve)、`I31—I36` SEC/IR公司披露。不把FRED第三方转录自动当发行人SEC原文。


## H03数据定义审计：2023/2024原版与2025同源B9/B9b
- [PJM 2023原始Load Report](https://www.pjm.com/-/media/DotCom/library/reports-notices/load-forecast/2023-load-report.pdf)的`Table B-9 ADJUSTMENTS ABOVE EMBEDDED` RTO目标2023=2231MW；2023文档封面印`January 2023`，LAS索引另列2023-05-22，**原PDF首次可得日期仍待确认**，不是2025六月`Total`的同指标原值。
- [PJM 2024原始Load Report](https://www.pjm.com/-/media/DotCom/library/reports-notices/load-forecast/2024-load-report.pdf)的`Table B-9 ABOVE EMBEDDED`目标2024=2664MW，PDF封面标`Revised 2/1/2024`但LAS目录标2023-12-27，**当前PDF内容不能未经历史版验证就标记在2023-12-27已知**。
- [PJM 2025原版工作簿](https://www.pjm.com/-/media/DotCom/planning/res-adeq/load-forecast/2025-load-report-tables.xlsx)：同一SHA `a9a797f2d3cf34154db466b74e045d1334dfebede87ec6dc3739805093474ef5`中Table B9和Table B9b的2025 RTO分别3591/7729MW，DOM1684/4970，AEP1412/1761；可**逐行直接差分、分区汇总闭合**。已复用北京/武汉MCP双端验证该SHA。
- [PJM 2025六月LAS Total回顾材料](https://www.pjm.com/-/media/DotCom/committees-groups/subcommittees/las/2025/20250613/20250613-item-03---large-load-adjustment-process-improvement-discussion.pdf)对v2023/v2024分别记录RTO首年3957/5682MW，分别与**不同发行文件**的B9差1726/3018MW，只是跨出版物`proxy`，不能冒充精确的“已嵌入MW”。
- [PJM 2026五月Accuracy XLSX](https://www.pjm.com/-/media/DotCom/planning/res-adeq/load-forecast/2026-accuracy-report.xlsx)与2025六月Total是另外的July-vs-Summer/历史覆盖源，2025目标RTO同标签2024/2025预测均不一致；[来源版本与排序敏感性报告](reports/2026-11-14_h03_embedded_bridge_and_original_vintages.md)保留未解决的定义问题。


## H09/H10真正取得的数据源（2026-11-14）
- **H09一手协议**：[Travis County×Colorado River Project LLC 2020合同PDF](https://tctransparency.traviscountytx.gov/Reports/EcoDev/TeslaAgreement.pdf)（阅读合同生效日、grant比率、报告、合规扣减及追索条款），[县政府官方目录](https://www.traviscountytx.gov/planning-budget/projects-compliance/economic-development-incentive-agreements)，[Tesla 2025正式SEC 10-K](https://www.sec.gov/Archives/edgar/data/1318605/000162828026003952/tsla-20251231.htm)（2026-01-29备案、2023—25县税Grant金额不重大）。
- **H09选前真实行动的报道原始来源**：[KUT 2025-11-26](https://www.kut.org/austin/2025-11-26/austin-tx-tesla-tax-rebate-deal-travis-county)及[KUT 2026-04-08](https://www.kut.org/text/austin/2026-04-08/austin-tx-tesla-travis-county-tax-rebate-agreement)：4/7委员投票9%扣减仍缺正式county clerk纪要；报道不能升级为F类会议原件，实际现金数未知。
- **H09反向政策项目**：[Starbase市政府官网Public Notice](https://www.starbase.texas.gov/)公告12/9**未来**SpaceX税惠议程，[Texas Tribune](https://www.texastribune.org/2026/11/10/texas-spacex-data-center-power-plant/)报道约240亿美元为计划投资，非政府已支付/批准现金奖励。与Tesla不同法人与法域，不叠加。
- **H10历史原始数字**：[BLS Public Data API CPI-U](https://api.bls.gov/publicAPI/v2/timeseries/data/CUSR0000SA0?startyear=2025&endyear=2026)及[core CPI](https://api.bls.gov/publicAPI/v2/timeseries/data/CUSR0000SA0L1E?startyear=2025&endyear=2026)直连读取当前季调索引，2025-10缺值，2026-10同比NA；[Treasury官方2025 XML](https://home.treasury.gov/resource-center/data-chart-center/interest-rates/pages/xml?data=daily_treasury_yield_curve&field_tdr_date_value=2025)、[2026 XML](https://home.treasury.gov/resource-center/data-chart-center/interest-rates/pages/xml?data=daily_treasury_yield_curve&field_tdr_date_value=2026)共467交易日，缺休市日绝不填。
- **H10 PCE发行版次与Fed原文**：[BEA 2026-09-30 August PCE](https://www.bea.gov/news/2026/personal-income-and-outlays-august-2026)及[BEA 2026-10-29 September PCE](https://www.bea.gov/news/2026/personal-income-and-outlays-september-2026)分别显示8月core首次0.2与后验0.3；[Fed Sep16 +25bp](https://www.federalreserve.gov/newsevents/pressreleases/monetary20260916a.htm)及[Oct28维持区间](https://www.federalreserve.gov/monetarypolicy/files/monetary20261028a1.pdf)。真实发行/决议日不同，不能倒填。
- [H09报告](reports/2026-11-14_h09_travis_texas_incentive_preelection_control.md)、[H10报告](reports/2026-11-14_h10_cpi_pce_fomc_treasury_pit_baseline.md)，及可复核CSV。没有获取完整公司级融资和高频期货，仍不足以声称政治/利率因果。

## H03：PJM原版2025与2026订正预测B9/B9b来源层
- [PJM 2025年原始Long Term Load Forecast Tables](https://www.pjm.com/-/media/DotCom/planning/res-adeq/load-forecast/2025-load-report-tables.xlsx)：2025-01-24索引版，409854 bytes，SHA `a9a797f2d3cf34154db466b74e045d1334dfebede87ec6dc3739805093474ef5`，原始Table B9和B9b可同书相减。
- [PJM 2026年当前可得Long Term Load Forecast Tables](https://www.pjm.com/-/media/DotCom/planning/res-adeq/load-forecast/2026-load-report-tables.xlsx)：371564 bytes，SHA `59a62facf819962e430101c96dd1335229d8173fb6886dd8045ced325443f607`，其中B9第6行明确`updated 2/6/2026 to correct for an error calculating embedded`，它并非可以追认为2026-01-14首个版本字节。PJM表头仍分别是Above Embedded（额外调整）和Total Associated（关联总量），两层都**不是数据中心专属已实现值**。
- [PJM 2026-05 Forecast Accuracy XLSX](https://www.pjm.com/-/media/DotCom/planning/res-adeq/load-forecast/2026-accuracy-report.xlsx)，SHA `e0f24fe03a79af016826089c653b2c2e15e55edcb04a7bd4be5fa643136425fc`；v2026 RTO 2026—31比上述当前原始B9b均高10MW、2032—35高9MW，DOM/AEP/COMED/PS/PL同年数值相符。**尚无来源解释RTO差9–10MW的原因**；不能强制将其当某项目取消或投入。
- [2026—2035年度与区级定量桥接](reports/2026-11-14_h03_b9b_vintage_decomposition_2025_2026.md)，机器文件保存各workbook原始SHA、文件发布时间与2026B9更正说明。

## H03 B9双模型敏感性方法一手来源（补充2026-11-14核实）
- [PJM LAS 2026-01-23 2026 Long-Term Load Forecast预测程序第28页](https://www.pjm.com/-/media/DotCom/committees-groups/subcommittees/las/2026/20260123/20260123-item-03---pjm-2026-long-term-load-forecast---presentation.pdf)：有历史DC的区域先从EIA月度商业数据和PJM小时负荷历史剔除DC，再加入final total accepted large load；对无历史DC的区域直接加入accepted load；B9通过“**不剔除历史DC的模型敏感性**”与最终模型比较产生Above Embedded。该程序证实B9是模型差异，**B9b−B9不能解释为客户真实计量DC MW或个体项目数量**。这是一手方法来源，不能证明2026-02-06勘误的具体数值。

## H03第十一轮：2026-01/02两独立XLSX、月度PSA注释和真实来源版本闭合
- [PJM独立年度B9b Total附件](https://www.pjm.com/-/media/DotCom/planning/res-adeq/load-forecast/total-load-adjustments-breakdown.xlsx)（官网2026-01-14目录，ZIP核心元信息Modified`2026-01-13T16:17:25Z`），18,904B，SHA`ee3b682929db0b59a043c8ab6d1c9776f697ab10fc86fe603a6d0d724893c4ba`。2027 RTO=15,866MW，EKPC=0。**元信息不是不可伪造的首次上线时间戳**。
- [PJM 2/6独立B9容量义务附件](https://www.pjm.com/-/media/DotCom/planning/res-adeq/load-forecast/2026-load-adjustment-breakdown-for-capacity-obligations.xlsx)，19,177B，SHA`990e2cb82d02a6c689a9e21b5c7ccb13944613f960dcc2f6eb3109e51a49d6a1`，ZIP Modified`2026-02-06T13:00:15Z`，表第3行明示修正Embedded计算错误；2027 RTO=10,795MW、EKPC=0，**不是1/14更正前B9**。
- [PJM当前合并原工作簿](https://www.pjm.com/-/media/DotCom/planning/res-adeq/load-forecast/2026-load-report-tables.xlsx)，371,564B SHA`59a62facf819962e430101c96dd1335229d8173fb6886dd8045ced325443f607`：EKPC在B9及B9b都为-10(2026—31)、-9(2032—37)、-8(2038—46)MW，RTO相应比两独立附件低同值。**23×21全区域值比对只有EKPC和汇总RTO不相同**。
- [PJM 2026May Accuracy XLSX](https://www.pjm.com/-/media/DotCom/planning/res-adeq/load-forecast/2026-accuracy-report.xlsx)，50,175B SHA`e0f24fe03a79af016826089c653b2c2e15e55edcb04a7bd4be5fa643136425fc`，2026版回顾RTO整个2026—46 **21年都与1/14独立B9b一致**；其与当前合并版差8—10MW对应EKPC被计入与否，不是模型新MW。
- [PJM 1/14独立月度总调整表](https://www.pjm.com/-/media/DotCom/planning/res-adeq/load-forecast/total-monthly-load-adjustments.xlsx)，59,187B，SHA`d9e547c71e4176776028b1c323759830f9fcd5ed908af142be783464aae9a2ff`，原工作表第2行**明确排除Peak Shaving Adjustments**；[PJM 1/14官方说明](https://insidelines.pjm.com/pjms-updated-20-year-forecast-continues-to-see-significant-long-term-load-growth/)把EKPC列为始于2023 Delivery Year的**peak-shaving program**，而非数据中心项目。两者支持PSA统计口径差解释，**但文件无单独声明差值是否为有意发布范围差异**。
- [PJM官方2025-01-24预测报告第4页](https://www.pjm.com/-/media/DotCom/library/reports-notices/load-forecast/2025-load-report.pdf)写明**New to the report this year: Table B-9b**，因此2023/24原始预测文档没有同版Total B9b；历史跨源proxy不等同于原版同一测量。
- 21年EKPC来源差及PIT优先级参见[H03第十一轮专项来源报告](reports/2026-11-14_h03_ekpc_jan_vs_feb_release_reconciliation.md)。


## Travis County Clerk正式2026-04-07会议纪要与BEA NIPA新连续指数（2026-11-14）
- [Travis County官方CivicClerk事件#3609](https://traviscotx.portal.civicclerk.com/event/3609/files)，[8页正式Minutes fileId12979](https://traviscotx.api.civicclerk.com/v1/Meetings/GetMeetingFileStream(fileId=12979,plainText=false)) SHA256 `ff8a5ae05d5ab704c6a11363d1d3cd18fcd5646b4e113b16c4afac23df02435e`（2026-04-09公开）；[23页Transcript fileId12974](https://traviscotx.api.civicclerk.com/v1/Meetings/GetMeetingFileStream(fileId=12974,plainText=false)) SHA256 `0d7a5a89dca7d178a281b603d473ddd0b46e618f1569b5081a6f58fc8f7636c5`（同日公开）。Ubuntu MCP逐份取回并进行文本核验：议案26扣留grant9%获4-0+1弃权，议案6批准2025/26社区方案亦4-0+1弃权；两份来自同一场会议，不重复计事件族。[专项审计](reports/2026-11-14_h09_official_minutes_primary_confirmation.md)。
- 该会议主持和官员提到公司社区投入义务至少为县级O&M税额10%，2025约$2m/2026约$3.2m，仅属**公司对社区的履约负担预估**，不能当县支付grant。至今没有取得实际扣留绝对USD或者已付现金追回的官方支付账本，均留NA。
- [BEA官方NIPA Section2All Excel](https://apps.bea.gov/national/Release/XLS/Survey/Section2All_xls.xlsx)中的`T20804-M`（headline`DPCERG`、core`DPCCRG`），原始文件SHA256 `f5037feeafb3bee0718acd3214a30e8e777b3110ee2d7b7698beb14084485391`；33个2024-01—2026-09真实月份已转为[可复算CSV](data/h10_bea_nipa_pce_headline_core_2024_2026_snapshot.csv)。**只是2026-11-14官方回顾版，不能反填历史每次首发版**，相应BEA已披露历史修订另表保存。

## H03第十二轮：2026年1月原报告PDF与勘误前B9源资格
- [PJM2026-01-14官方报告PDF](https://www.pjm.com/-/media/DotCom/library/reports-notices/load-forecast/2026-load-report.pdf)，已实际下载SHA `9f2826cfc39357c54d6e6203e60946b6ce9ea627cfceeeaf4d4cd343066c6bc8`，8,750,526 bytes，36页，CreationDate=2026-01-12；正文只引用B9/B9b并说明全部数据表另置Excel，**PDF不含修正前B9逐年数值**。这不证明独立首版B9从未发布。
- [PJM官网发布日期与2/6附表索引](https://www.pjm.com/planning/resource-adequacy-planning/load-forecast-dev-process.aspx)，[1月独立B9b Total](https://www.pjm.com/-/media/DotCom/planning/res-adeq/load-forecast/total-load-adjustments-breakdown.xlsx)与[2/6订正B9](https://www.pjm.com/-/media/DotCom/planning/res-adeq/load-forecast/2026-load-adjustment-breakdown-for-capacity-obligations.xlsx)不同统计量、不同日期。1月完整B9原始字节仍未获得，Wayback查找超时不是证实历史无档。
- [PJM1/14官方整体夏季峰值修订](https://insidelines.pjm.com/pjms-updated-20-year-forecast-continues-to-see-significant-long-term-load-growth/)与2025原版、2026Jan独立B9b总量对照见[报告](reports/2026-11-14_h03_uncorrected_b9_source_gate.md)：2027—30两个预测修订规模比**仅描述性非因果贡献**。原PDF及可取得源的SHA和缺失状态见[来源登记](data/h03_pre_correction_b9_source_availability.csv)。


## H09州Chapter381原始CSV与H10 CPI日历（v0.2.3）
- [Texas Comptroller官方Chapter380/381全表CSV](https://assets.comptroller.texas.gov/open-data-files/ch380.csv)，2026-11-14经Ubuntu MCP读到3,969,329字节/43字段、SHA256 `490d64ee6426910aff16eefefc9a3c6b208ad40f18643549465dafe51d3791d7`。只一条符合Travis County×Colorado River Project LLC的`0005328`记录，`totl_agmt_am`空白、last_update`2022-05-01`、截止2041-12-30与签署合同12-31不一致。[正式登记详情](https://comptroller.texas.gov/economy/development/search-tools/ch380-381/economic-development-agreements-details.php?agreement=0005328)。**不等于县级财政现金支付账。**
- [BLS CPI原始发行存档](https://www.bls.gov/bls/news-release/cpi.htm)、[BLS 2026更新发行日历](https://www.bls.gov/schedule/news_release/cpi.htm?lv=true)、[2025历史日历](https://blsmon1.bls.gov/schedule/news_release/cpi.htm)：2025 CPI由于停摆没有2025-10数据/公布，2025-09 CPI实际2025-10-24公告；2025-01-15至2026-11-10共22个真实发行日用于[日收益率统计报告](reports/2026-11-14_h10_cpi_release_ust_22_event_robustness.md)。BLS真实发行日与Treasury日度par yield组合并不能单独识别通胀意外冲击。
- [CME FedWatch工具历史下载说明](https://www.cmegroup.com/tools-information/quikstrike/cme-fedwatch-tool-user-guide.html)表明其公共工具含历史概率下载；[CME FedWatch官方付费REST/API说明](https://www.cmegroup.com/tools-information/webhelp/data-services-portal/Content/CMEDataServicesPortal.pdf)须有许可/订阅。本轮没有付费或未经许可抓取完整概率序列，避免假定免费endpoint可用。

## H03第十三轮｜FERC2026-11-03当事人专家EN1原始表引用冲突
- [PJM 2023原始87页Load Report](https://www.pjm.com/-/media/DotCom/library/reports-notices/load-forecast/2023-load-report.pdf) 7,479,191 bytes，SHA`cf4ce845c13d75d06320360f9db985bc94633cdc06aabcd639c39bb11795e1b0`：**PDF零索引59**原B8a分布式太阳能RTO 2023—28=2888/3269/3566/3841/4035/4185；**零索引61**原B9超嵌入大型负荷RTO对应2231/3393/4654/6594/8300/9866。前者与后者不同且不能互相替代。
- [Exelon FERC EL27-11-000 2026-11-03主诉及专家EN1](https://www.pjm.com/-/media/DotCom/documents/ferc/filings/2026/20261103-el27-11-000.pdf)，3,554,494 bytes SHA`599ea60395437889244791717260949dc9bdb33ab57c16470f549ddcce5b56c0`，PDF**零索引92**的2023 Forecast Load Adjustments 6格等于B8a、0格等于B9，但EN1脚注引用B9。为诉讼方提交材料而非监管已采信历史结论，可能存在**错误源表选择**，不推断故意误报。
- [PJM 2024-02-07官方方法课件](https://www.pjm.com/-/media/DotCom/committees-groups/committees/mic/2024/20240207/20240207-item-09a---forecast-adjustment-education.pdf)，SHA`5e437e2e2273149fb5bf6611569ed284eeee19cabb4e75a58fedabde0ad909e1`，另证2023 DOM B9 2068/2988/3926/5678MW；加强官方B9定义和附件误引排查。历史主要风险及10版Y0+5表见[完整研究](reports/2026-11-14_h03_ferc_en1_solar_table_mismatch.md)。


## 2023/24 Treasury历史与Travis 2026县大附件逐页核验（v0.2.4）
- [Travis County 2020签署合同PDF](https://tctransparency.traviscountytx.gov/Reports/EcoDev/TeslaAgreement.pdf)第1.22/1.23、5.2.1/5.2.3、7.4、7.5、7.7、8、9条规定PerfYear→合同PaymentYear有2年常规滞后及申报/上诉条件；[合同时间差报告](reports/2026-11-14_h09_grant_payment_year_lag_contract_audit.md)保留实际付款仍未知。
- [Travis County 2026-04-07官方Agenda Packet](https://traviscotx.api.civicclerk.com/v1/Meetings/GetMeetingFileStream(fileId=12961,plainText=false))由Ubuntu实际下载**103437809字节/255页**、SHA256 `e93233825a52768bf0ee3860b8ade8d86f32618d71d1f62e0c827eb9ae7dd1bb`，第15页Item6、第253页Item26分别核实`Attachments: None`及`Fiscal Impact`空白。[PDF来源/页面审计](reports/2026-11-14_h09_agenda_packet_255pages_no_grant_figures.md)，原议案Minutes已有4-0确认，附件不存在不等于县无ACH信息。
- [2023 US Treasury年XML](https://home.treasury.gov/resource-center/data-chart-center/interest-rates/pages/xml?data=daily_treasury_yield_curve&field_tdr_date_value=2023)（250日，SHA256 `7b30333f8ae255688b163f421227ee6e733f642f28a0ebd8c76dca3efd9f0cf5`）与[2024年XML](https://home.treasury.gov/resource-center/data-chart-center/interest-rates/pages/xml?data=daily_treasury_yield_curve&field_tdr_date_value=2024)（250日，SHA256 `acf0b2af87aeda2143365fedd044fe6a254d2916b62588ee9500113b3a8d1764`），[2023官方BLS发布日](https://www.bls.gov/schedule/2023/home.htm)、[2024](https://www.bls.gov/schedule/2024/home.htm)。[46次历史事件及统计](reports/2026-11-14_h10_cpi_release_ust_46event_historical_robustness.md)由这些资料和原2025/26数据组合，数据版本均截至2026-11-14；事件日交易市场日变动不等于CPI惊讶的高频因果冲击。


## 2025-11尚无Tesla县返利与2026-11-10真实预期锚点（v0.2.5）
- [Statesman 2025-11原报道公开版本](https://eedition.statesman.com/infinity/article_popover_share.aspx?guid=6a71809c-9b1b-45f5-be6e-729aa32495f3&share=true)和[KUT 2025-11-26全文](https://www.kut.org/text/austin/2025-11-26/austin-tx-tesla-tax-rebate-deal-travis-county)明确记录**截至2025年11月县尚未发放本项Tesla返利**，按媒体引用官员信息`R`而非Auditor官方付款总账。KUT指向Statesman，**同源报道不计多份现金事实**；不由2025状态外推2026状态，避免把既有9%扣留叫作已付资金追回。
- [FXStreet 2026-11-09 22:31 UTC预告](https://www.fxstreet.com/analysis/us-cpi-preview-moderation-on-the-horizon-but-underlying-pressures-linger-202611092231)明确市场预计当月headline CPI SA MoM0.3%、core0.2%；[Reuters公布前经济学家预期报道](https://d2233.cms.socastsrm.com/2026/11/09/us-consumer-prices-expected-to-have-risen-at-slower-pace-in-october/)亦为0.3/0.2，但不是独立计两份调查。[2026-11-10 BLS官方首发新闻稿](https://www.bls.gov/news.release/archives/cpi_11102026.htm)为0.4/0.3，两项**+0.1pp**（新闻稿一位小数）。
- [Cboe 2026-11-10专业市场点评](https://www.cboe.com/insights/posts/hot-cpi-report-puts-fire-under-interest-rate-hike-possibilities/)引述CME FedWatch十二月会议+25bp概率**周一84%→周二90.5%**，周二+50bp **9.5%**；无原始CME精确分钟quote、不能认定纯CPI影响。Treasury官方两年期收益率同日+17bp、十年期+10bp也是整日变动。
- BLS官方v2两种**不同的美国CPI-U序列**：季调`CUSR0000SA0` 2026-10=337.476（Sep336.298），未季调`CUUR0000SA0` Oct=337.511（Sep336.940）。[MetaTrader公开日历](https://www.metatrader.com/en/economic-calendar/united-states/consumer-price-index?period=all-time) actual337.476/forecast338.683为SA指数口径，[CRTLAB日历](https://crtlab.pro/economic-calendar/us-cpi) actual约337.5/forecast337对应NSA口径，且两个预测网页缺真实公布前时间戳，故**不可拿它们计算或对比同一pre-release惊喜度**。详见[15行PIT节点表](data/h10_20261110_cpi_consensus_fedwatch_rate_event.csv)和[审计报告](reports/2026-11-14_h10_cpi_20261110_true_preconsensus_fedwatch_rate_anchor.md)。


## 2022县官方零返利与2023—26真实事前CPI预测（v0.2.6）
- [Travis County Jan31 2022 Economic Development Agreements Summary 2页](https://www.traviscountytx.gov/images/planning_budget/Docs/Summary_of_Economic_Development_Agreements_1-31-22.pdf)当时`Colorado River Project (Tesla): Zero rebates paid, performance year 1 verification pending`，属有日期的官方F类历史状态；其他协议也在县汇总有零返利。**不是截至2026年的付款报告**，同2025-11 KUT媒体记录不同来源级别。[H09历史状态分析](reports/2026-11-14_h09_county_official_2022_zero_rebates_baseline.md)。
- H10真正提前公布的10次专业CPI预测来自[InvestingLive 2023-11](https://investinglive.com/centralbank/us-cpi-will-be-eyed-ahead-of-the-december12-13-fomc-meeting-20231114/)、[Reuters 2024-02前瞻](https://ca.finance.yahoo.com/news/us-inflation-looms-large-asia-053650734.html)、[Reuters 2024-05](https://ca.finance.yahoo.com/news/morning-bid-us-inflation-every-050331355.html)、[InvestingLive 2024-06](https://investinglive.com/news/preview-eyes-will-be-on-every-detail-of-the-may-cpi-report-20240611/)、[Reuters 2024-07](https://ca.finance.yahoo.com/news/dollar-firm-powell-caution-kiwi-010519538.html)、[MNI 2024-09预期](https://media.marketnews.com/USCPI_Prev_Sep2024_66514cfe2d.pdf)、[CalculatedRisk 2025-03](https://www.calculatedriskblog.com/2025/03/cpi-preview.html)、[Continuum 2026-03](https://continuumeconomics.com/a/5d88223a/preview-due-march-11-us-february-cpi-a-moderate-gain-but-inflation-not-yet-defeated)、[Continuum 2026-06](https://continuumeconomics.com/a/da75be83/preview-due-june-10-us-may-cpi-energy-and-air-fares-to-lead)及[FXStreet 2026-11](https://www.fxstreet.com/analysis/us-cpi-preview-moderation-on-the-horizon-but-underlying-pressures-linger-202611092231)。**按原发时间核实，但来源包含单机构与专业共识，不能当同一原始问卷。**实际CPI用各次BLS首发公报，UST使用[已核2023—26官方日度收益率](reports/2026-11-14_h10_cpi_release_ust_46event_historical_robustness.md)。[10例数据/方向/来源报告](reports/2026-11-14_h10_pre_release_forecasts_10_pit_vs_vendor_not_pit.md)。
- [TradingCharts事后历史财经日历2026-11-09链接示例](https://forex.tradingcharts.com/economic_calendar/2026-11-09.html?code=USD)网址即便是公告前一日，正文中的Actual已经是公布后回填，**无初始Forecast历史快照及发表时间**；已读46个日期，28个headline及28个core有两列，但不能直接作为真实PIT预期。与独立时间证实的两期core预测相差0.1pp，来源/机构/修订不同可能解释，不能证明恶意修改。[来源冲突审计程序](analysis/audit_h10_dated_vs_archive_forecast_conflicts.py)。
