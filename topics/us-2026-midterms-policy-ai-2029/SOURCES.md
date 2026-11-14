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
