# TOPIC-011｜2026-11-14 H09官方州级金额缺失审计 / H10 CPI公布日美债事件回测

## 起点与来源
用户要求沿H09/H10继续推进真正实证，优先县级财政实际支付美元与美国通胀公告→利率传导的市场历史检验，而非继续建立空的候选假说。先读取了GitHub PR #51最新分支，保留了并行H03数据与已存在指标。

**H09**：Ubuntu MCP下载Texas Comptroller公开[Chapter380/381 CSV](https://assets.comptroller.texas.gov/open-data-files/ch380.csv) 3,969,329字节（SHA `490d64ee6426910aff16eefefc9a3c6b208ad40f18643549465dafe51d3791d7`），解析43字段和唯一协议0005328（Travis / Colorado River Project LLC）：effective 2020-07-14，备案Active但last_update=2022-05-01，`totl_agmt_am`空白，funding field空白，州登记截止2041-12-30与县签署原件截止2041-12-31有一天差异。不能把县级2020–22实际支付、扣留、已付后追缴金额推出来。[单行审计数据](../cases/musk-2026/texas_comptroller_0005328_registry_snapshot.csv)。2026-04-07县正式Minutes对三个履约年度**eligible grant的9%**扣留决议仍已证实，但金额未得。另有[KUT 2026-04-08新闻](https://www.kut.org/austin/2026-04-08/austin-tx-tesla-travis-county-tax-rebate-agreement)2020签约初期估算前10年优惠约1400万美元，是多年预测，**不能乘9%冒充被扣美元**。创建2020/21/22三个年份多字段空值账本。财务公开平台访问出现TLS超时，**不是零笔付款证据**；如需后续PIR，记录正式请求清单而不擅自寄邮件。

**H10**：借[BLS 2025/26 CPI实际发布档案](https://www.bls.gov/bls/news-release/cpi.htm)、[2026已更新发布日历](https://www.bls.gov/schedule/news_release/cpi.htm?lv=true)与已有美国财政部2025–26日度2Y/10Y共467个交易日（来自官方XML）配对。22次CPI公布日、非公布日444个有相邻收益率变化值。2025-10无CPI实际报告，2025-09在10-24发布，不能按通常规律填日期。
- 2Y绝对变化：CPI日均5.2727bp，所有非CPI日均3.8806bp。同月非公告日每次随机抽22天、20,000次固定种子20261114；安慰剂均3.9813bp，未调整探索性右尾p=0.048298。
- 10Y：公布日4.3636bp，同月随机安慰剂3.8729bp，p=0.208240。
- **强反证**：2026-11-10两个收益率分别+17/+10bp，剔除该天后2Y事件均4.7143bp、同月安慰剂3.8952bp、p上升0.138943；2025年11个事件p=0.152642、2026年11个p=0.082996，均未达到未调整5%阈值。全样本“显著”并不稳健。
- 无CPI公布前一致预期、Fed基金期货或公告后分钟级价格、同日事件控制，故这些p值仅统计**日度相关性**，非独立CPI冲击与FOMC政策因果；多种检验未做多重比较调整，不能用作交易规则。
- CME [FedWatch公开历史用户指南](https://www.cmegroup.com/tools-information/quikstrike/cme-fedwatch-tool-user-guide.html)允许在公开工具中查看/下载历史概率，但其[专用FedWatch REST API](https://www.cmegroup.com/tools-information/webhelp/data-services-portal/Content/CMEDataServicesPortal.pdf)有许可与月费，不声称免费自动取得历史概率。

## 产物
- [H09州级金额缺失审计](../reports/2026-11-14_h09_texas_381_registry_missing_cash_audit.md)与[2020-22县级年度美元空值账本](../cases/musk-2026/travis_2020_2022_grant_cash_reconciliation.csv)。
- [H10 CPI发布日22次Treasury变化CSV](../data/h10_cpi_release_treasury_2y10y_2025_2026.csv)、[Python标准库重算脚本](../analysis/recompute_h10_cpi_release_ust_events.py)、[极值删除及分年稳健性报告](../reports/2026-11-14_h10_cpi_release_ust_22_event_robustness.md)。
- 主evidence账本新增E091-E092；指标层新增H10两个可复用事件日绝对bp定义，引用映射加入H10。H09/H10因果状态仍UNTESTED，不新增正式已证因果C-ID。

## 下一轮
1. H09向Travis County Auditor/PBO取得2020-22 grant eligible、approved、paid、withheld、recovered实际USD，按付款年与绩效年分离；若县公开端不提供，再通过公开资料申请。学区Ch313属于不同法人/法域，不能用来填县Ch381金额。
2. H10优先CME历史可合法免费Excel或完整许可期货行情，以及每次CPI**实际公布前**专业一致预期，完成真实surprise→政策概率→2Y市场反应的同时间戳前瞻检验；不能过度解释单日日收益率。
