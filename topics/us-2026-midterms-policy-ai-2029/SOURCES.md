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
