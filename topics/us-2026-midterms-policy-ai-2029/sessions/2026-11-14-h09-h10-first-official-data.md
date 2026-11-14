# TOPIC-011｜2026-11-14 H09/H10：首次真实官方数据、前置反例与发布时间审计

## 任务续接
在EX/VIEW/H/I/CHAIN结构v0.2.0建立以后，不再只设计架构；直接为H09取Texas企业真实优惠协议、审查与公司披露，为H10取2025–26 CPI/美债历史数据和BEA/FOMC政策原始发布记录，并实际执行离线算术及时间顺序校验。

## 实际访问与来源深度
- 直接阅读 [Travis County 2020 Colorado River Project LLC Economic Development Performance Agreement](https://tctransparency.traviscountytx.gov/Reports/EcoDev/TeslaAgreement.pdf)：合同当事人、生效2020-07-14、期限2041-12-31、70/75/80%合格县级M&O税grant、投资/就业/本地工资要求、Sections7/8/9审批支付、扣减及条件性recapture；并查看合同相关原始PDF页面。属于一手原始合同F。
- [Travis County政府协议目录](https://www.traviscountytx.gov/planning-budget/projects-compliance/economic-development-incentive-agreements)说明Tesla项目与其他公司独立协议。2026-04-07据[KUT 04-08现场报道](https://www.kut.org/text/austin/2026-04-08/austin-tx-tesla-travis-county-tax-rebate-agreement)县委员4-0通过对2020–22补助扣减9%（1弃权），[2025-11-26报道](https://www.kut.org/austin/2025-11-26/austin-tx-tesla-tax-rebate-deal-travis-county)此前已有审查。**未直接获得县Clerk最终正式会议纪要，故该动作source_type=R不是F，扣减绝对美元及是否曾实际收回已付现金仍NA。**
- [SEC 2025 Tesla 10-K](https://www.sec.gov/Archives/edgar/data/1318605/000162828026003952/tsla-20251231.htm)（2026-01-29备案）说明2023/24/25上述grant资金对合并报表均immaterial，非零、非2026未来数据。一家公司集团报表不得用来推断SpaceX/xAI未公开现金流。
- [Starbase市官网2026-12-09未来税收优惠听证公告](https://www.starbase.texas.gov/)（官网当日可见）及[Texas Tribune 11-10](https://www.texastribune.org/2026/11/10/texas-spacex-data-center-power-plant/)：SpaceX约USD24bn是**计划投资/多阶段项目**而非已批准补贴，12/9是未来审议，非既成事实。
- Ubuntu MCP调用 **BLS官方Public Data API**：CUSR0000SA0 / CUSR0000SA0L1E月度SA指数，2025-01—2026-10合22个日历月，各21个有效指数，2025-10确实返回缺失；2026-10同比因此不能用当前官方指数算。
- Ubuntu MCP通过 **US Treasury官方XML** 逐年获取2025年249个、2026截至11-13的218个交易日，共467个2Y与10Y实际每日收益率，未对2026-11-11休市日补值。
- 直接核对BEA [2026-09-30八月PCE首次公告](https://www.bea.gov/news/2026/personal-income-and-outlays-august-2026)和[2026-10-29九月公告](https://www.bea.gov/news/2026/personal-income-and-outlays-september-2026)：八月核心PCE环比0.2→0.3是不同公告版次的真实修订，后者9月核心0.3月环比、3.1同比。9月PCE发行于10/29，比10/28 FOMC晚一天。
- 美联储 [2026-09-16加息25bp正式声明](https://www.federalreserve.gov/newsevents/pressreleases/monetary20260916a.htm)与[2026-10-28利率不变的正式声明](https://www.federalreserve.gov/monetarypolicy/files/monetary20261028a1.pdf)已核；不能将Waller个人有条件讲话当FOMC决定。

## 两条子线的实物文件
- H09：[Travis真实协议与选前负对照报告](../reports/2026-11-14_h09_travis_texas_incentive_preelection_control.md)、[合同级CSV](../cases/musk-2026/incentive_contracts.csv) 3行、[政策事件CSV](../cases/musk-2026/policy_event_ledger.csv) 6行（含12-09未来日程）、主事件表 E073—E077。
- H10：[22个月CPI](../data/h10_bls_cpi_sa_monthly_2025_2026.csv)、[467交易日UST](../data/h10_us_treasury_2y_10y_daily_2025_2026.csv)、[BEA发布版次4行](../data/h10_bea_pce_release_vintages_2026.csv)、[正式FOMC会议两行](../data/h10_fomc_official_decisions_2026.csv)、[报告](../reports/2026-11-14_h10_cpi_pce_fomc_treasury_pit_baseline.md)、[离线标准库复算](../analysis/recompute_h10_open_data.py)。
- Ubuntu真实执行离线脚本 `--stdin-json`，四份GitHub CSV经远程运行校验 **PASS**：BLS Oct headline0.3503%、core0.2963%、core三月折年3.7464%；Treasury11-09→11-10 2Y+17bp、10Y+10bp、曲线斜率32→25bp；BEA八月PCE修订0.2→0.3；FOMC 9/16 +25bp、10/28 0bp，公告日排序正确。

## 与前一轮相比新结论/反证
1. H09不能写“新德州选举后才开始审查Tesla”。Travis县2025已有审查、2026-04已据KUT报道扣款，这些构成**选前负对照**，未来2027-2028的增量才可能与政治变化有关。
2. 2025SEC10-K明确Travis县财产税补助对Tesla上市公司2023-25合并财务不重大。公司业绩与补助风险不能由某位评论者夸大成现金流危机；但不意味着所有政府优惠均不重要。
3. Starbase新申请与Travis既有合同方向相反，须分公司与辖区；$24bn只是投资提案、12/9未来 hearing，不是补贴金额。
4. H10已有真实月度CPI与日度市场共同运动，**没有预发布一致预期、期货高频与企业SEC债务面板**，还不能给Fed因果系数。8月BEA PCE 0.2→0.3说明PIT发行版次本身会改变研究者对当时信息的估计。
5. 两条H仍UNTESTED，原有竞争解释保留，正式因果C-ID不增加；本轮属于事实/数据层PATCH更新。

## 下一步可验收
- H09：县书记官2026-04-07正式动议与2020—25兑现额、2026后报表；Starbase 2026-12-09听证完成后才核实际投票/协议/受益主体。私企的财务不得编造。
- H10：BEA 2025—26完整PCE原始发行版次、Fed期货**发布前**市场隐含政策、信用利差和SEC同业现金流/到期表，预先冻结窗口后再回归；当前只有BLS与UST的后验同版历史快照，不是逐日PIT系统。
