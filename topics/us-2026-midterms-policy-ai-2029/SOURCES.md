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
