# TOPIC-011｜2026-11-14 H09正式县2022零返利基线与H10真实PIT通胀意外值方向检验

## 任务目标
沿用户的H09企业政商政策现金流和H10 CPI→Fed→融资历史研究线继续实际取数，优先区分原始PIT与事后财经日历以及2025新闻与2022官方记录的来源等级，不能简单重复专家观点。

## H09 本轮新增原始资料
- [Travis County官方2022-01-31经济发展协议汇总（2页）](https://www.traviscountytx.gov/images/planning_budget/Docs/Summary_of_Economic_Development_Agreements_1-31-22.pdf)：Tesla/Colorado River Project列**Zero rebates paid, performance year 1 verification pending**；其他协议也存在未发款，不能视此为独有政治靶向。
- [2025-11-26 KUT/Statesman相关报道](https://www.kut.org/text/austin/2025-11-26/austin-tx-tesla-tax-rebate-deal-travis-county)当时仍未发放县税返利，只按媒体归属，不当县Auditor付款账；2026-04-07正式会议第26项9%合格Grant扣留发生在中选之前，2026年底现金支付是否后来发生仍UNKNOWN。
- 旧[现金状态表](../cases/musk-2026/travis_rebate_disbursement_status_asof_2025.csv)增补F级2022官方历史基线；新增[专项报告](../reports/2026-11-14_h09_county_official_2022_zero_rebates_baseline.md)。

## H10 真实历史来源工作
- 在既有[46次2023—26真实CPI公布日](../data/h10_cpi_release_ust_46events_2023_26.csv)基础上，Ubuntu MCP访问同日历日期前一天的[TradingCharts历史页](https://forex.tradingcharts.com/economic_calendar/2026-11-09.html?code=USD)：46个可读页面，有headline与core各28个非空actual/forecast；因实际值已事后回填，**历史URL的日期不等于预测的真实公布前版本日期**；所有行在[46行非PIT供应商存档](../data/h10_cpi_release_ust_46event_vendor_archive_not_pit.csv)上标记`RETROSPECTIVE_PAGE_UPDATED_AFTER_RELEASE_NOT_PIT`。
- 另外核到**10个真正有公布前日期和URL**的独立财经研报/新闻（Reuters转载、MNI、InvestingLive、Calculated Risk、Continuum、FXStreet）；包含机构单方forecast和市场预期，二者标签分开，不能混作一个survey。[10个日期的预测/BLS首发实际/2Y及10Y当日signed bp](../data/h10_cpi_pre_release_dated_forecasts_10events_2023_2026.csv)，所有匹配BLS首发公告，缺headline的一个月保持空值。
- [Python统计脚本](../analysis/recompute_h10_pre_release_cpi_surprise_10_events.py)在Ubuntu基于**最新GitHub源码及数据**经stdin实际运行PASS：core surprise非零8个日期，其中2Y signed move非零7次，**6次同向、1次反向**（2025-03-12 surprise-0.1pp但2Y+7bp），另2026-06-10 2Y持平。双侧精确二项p=0.125；剔2026-11-10变为5/6 p=0.21875；headline6个非零同幅匹配5/6 p=0.21875；core 10Y同向5/7 p=0.453125。**便利样本不可当样本外命中率**，2024-06-12同日有FOMC会议，Treasury为全日变化非CPI-only 5min。
- [历史供应商vs有日期提前预测来源冲突独立脚本](../analysis/audit_h10_dated_vs_archive_forecast_conflicts.py)从Github两CSV实际运行PASS：存在7次同日期两表的headline/core预测比较，`2026-03-11`和`2026-11-10`事前Core0.2、Vendor历史Core0.3，相差0.1pp。可能因机构预测与共识、更新版本或不同定义，**并非证明供应商篡改**。因此Vendor历史预测不得直接用于正式PIT回测。
- [完整10事件与非PIT供应商对照报告](../reports/2026-11-14_h10_pre_release_forecasts_10_pit_vs_vendor_not_pit.md)。

## 汇总与下一阶段
- 主证据账本新增E109—E111；统一指标层新增H09县官方截至时点已支付状态、H10 Core CPI surprise与2Y方向一致情况；观点层新增[VIEW-S001 C04/C07/C09后验核查](../views/claim_reassessments_2026-11-14_round6.csv)，不修改原发言。
- 尚未获取2026县Auditor真实ACH、差额或已付后追缴美元；H10的2023—26各月**同源**Reuters/专业调查事前共识、FF期货/美债08:29—08:35历史报价仍缺。先把真实首次发布版本与对应forecasts的entity/mean/median统一，再做用同一制度期、同一数据钟的冲击识别，当前H09/H10完整因果仍UNTESTED且不新增正式C-ID。
