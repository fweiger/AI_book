# H10｜2026-11-10通胀公布前预测→FedWatch期望→美国美债：一次有PIT锚点的事件研究（2026-11-14）

> **这是一条首次有可靠公布前经济预期节点的链条，不是已识别CPI的独立因果效应。** 核心事实：11月9日经济学家预期整体/核心CPI环比0.3%/0.2%，11月10日BLS公布0.4%/0.3%，分别正向surprise +0.1个百分点；Cboe当日记录FedWatch对12月25bp情景概率由上周一的84%升至90.5%、另外50bp情景9.5%；US Treasury官方当日2Y+17bp、10Y+10bp。多条同日Fed发言混杂，不是严格CPI-only shock。

## 1. 证据节点与观测先后

| 事件 | 实际值 | 来源级别及时间 | 解释边界 |
|---|---|---|---|
| 11/09公布前headline和core CPI预测 | **0.3% / 0.2% 环比** | [FXStreet 2026-11-09 22:31 UTC公布前前瞻](https://www.fxstreet.com/analysis/us-cpi-preview-moderation-on-the-horizon-but-underlying-pressures-linger-202611092231)；[Reuters公布前报道镜像](https://d2233.cms.socastsrm.com/2026/11/09/us-consumer-prices-expected-to-have-risen-at-slower-pace-in-october/)再次引用0.3/0.2；两家不一定有独立调查样本 | 这是可以证实时间先于实际发布的专业预期**二手资料**，不是Reuters/Bloomberg逐个经济学家原始问卷或可还原到08:29前的原始分布 |
| 11/10 BLS CPI官方首次公布 | headline **0.4%**、core **0.3%** | [BLS CPI 2026-11-10原始发布](https://www.bls.gov/news.release/archives/cpi_11102026.htm)，08:30美国东部标准时间 | headline/core各比公布前预测高 **+0.1 个百分点**；按新闻稿一位小数口径计算，**不是指数点数差/不是同比** |
| 11/09对12月政策定价 | 25bp情景概率 **84%** | [Cboe 11/10交易所研究文章](https://www.cboe.com/insights/posts/hot-cpi-report-puts-fire-under-interest-rate-hike-possibilities/)转引上一个周一的CME FedWatch | 后一天报道的前一日数据；**未取得原始CME历史快照与精确分钟时间戳** |
| 11/10对12月政策定价 | 25bp **90.5%**、50bp **9.5%** | 同一Cboe文章，均为11/10时点该作者读到的FedWatch情景 | 可算25bp情景概率+**6.5个百分点**，但**无法确认前一日50bp情景精确为0，也不能计算所有政策情景的净变动或CPI唯一因果** |
| 11/09→11/10 US Treasury官方日度收益率 | 2Y **4.56%→4.73%：+17bp**；10Y **4.88%→4.98%：+10bp** | [US Treasury 2026官方日度par收益率XML](https://home.treasury.gov/resource-center/data-chart-center/interest-rates/pages/xml?data=daily_treasury_yield_curve&field_tdr_date_value=2026)，全交易日变化 | 日度收盘并非11/10 08:29→08:35分钟反应，其他政策讲话/财政新闻可在全天起作用 |

这一表内行包括 pre-release dated as-of、official release、reported pre/post pricing、official rates、独立供核指标标记，见[15条数据CSV](../data/h10_20261110_cpi_consensus_fedwatch_rate_event.csv)及[纯标准库数据一致性脚本](../analysis/recompute_h10_20261110_cpi_pit_anchor.py)，Ubuntu MCP从GitHub读取CSV实际运行`PASS`。

## 2. 为什么此前两家“CPI指数预测”竟然方向相反？

同一11月10日有两种不同的通胀指数新闻日历：
- **BLS官方季调CPI-U `CUSR0000SA0`**：2026-09指数**336.298**、10月**337.476**。MetaTrader公开历表实际**337.476**并显示预测**338.683**，若做指数点减法是**−1.207**。但**网页没有提供可核11/10 08:30之前的forecast版本/来源，不能计入真实PIT预期**。[MetaTrader日历](https://www.metatrader.com/en/economic-calendar/united-states/consumer-price-index?period=all-time)
- **BLS官方未季调CPI-U `CUUR0000SA0`**：2026-09指数**336.940**、10月**337.511**。CRTLAB公开历表显示实际约**337.5**、预测**337**，按该页展示值减法约**+0.5指数点**。这是未季调值的数量级与上期口径；**预测原始采集时间与完整精度未验证，不能与季调指数直接对比**。[CRTLAB CPI历表](https://crtlab.pro/economic-calendar/us-cpi)
- 这两种“正/负 surprise”**不是同一物价指标或同一个发布前统计口径**，再加上预期值的来源与采集版本不明，**不应把这种差异当成市场有两派预期相互冲突，或任选一个回测**。
- **本轮唯一可用作正向公告意外值的量，是公布之前正式刊出的季调headline/core月环比专业预测0.3/0.2 vs BLS首次新闻稿0.4/0.3。** 它可以构成一个单事件研究的预期差锚点，但不足以做46次历史系统性前瞻回测。

## 3. 这条链已经得到什么、缺哪一步

**已真实观测的节点**：公布前预测、较热CPI发布、同日报告的FedWatch更鹰派情景变化、2Y与10Y的官方日度上涨。它比“46次公布日交易收益率绝对变动”多了真正**方向性surprise**节点，且同日变化方向相符。

**尚不可验证的边**：`CPI意外本身→FedWatch概率变化`需要11/10 **08:29和08:35纽约时间**的原始概率或FF期货成交/报价，且要将当天Waller、Logan、Schmid等Fed官员讲话及其他数据分开；`FedWatch概率变化→2Y上涨17bp`还要期限结构、预期未来更多会议/期限溢价归因。**Cboe同日汇总不是高频独立因果样本**。

因此可以将VIEW-S001-C07、C08、C09从只有观点的状态提升为**“单次发布前预期与事后市场重定价方向一致，观察边存在”**，而不能将H10正式认定为政策必然加息或50bp决议已发生。Cboe显示50bp情景存在9.5%，**不是已实施或确定会实施50bp**。

## 4. 可执行的下一步

- 冻结CPI官方首发与公布前专业调查的一致单位`SA headline/core MoM`，先按这个严格口径补充**2023—26至少更多历史月份**，不能混入未季调价格指数forecast。
- 以每个数据发布时间为锚，寻找可公开/合法使用的FedWatch历史Excel或FF期货价格，同源冻结08:25/08:35事件窗，考虑同时新闻；没有高频就继续标`NO_CAUSAL_IDENTIFICATION`。
- 对之后的政策会议再比较**实际FOMC决议**与预期修订，不把11/10 Fed讲话视为12月委员会决定。
