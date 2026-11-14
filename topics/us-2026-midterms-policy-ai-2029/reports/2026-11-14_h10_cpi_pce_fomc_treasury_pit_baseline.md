# H10 首轮真实数据与时间顺序：BLS CPI→BEA PCE→FOMC→Treasury（2026-11-14）

> **已实际读取美国BLS公开API的22个月季调 CPI 指数、Treasury官网的467个真实交易日2Y/10Y收益率，直接核对BEA两个不同时点的官方PCE公告与Fed两次2026会议正式声明。** 使用Ubuntu MCP运行本专题纯标准库复算脚本，结果PASS。本报告只证明可重现数值与披露时间，**并没有证明宏观数据对美联储、市场或企业融资的因果效应**。H10保持UNTESTED。

## 1. 实际取得并复算的数据

| 数据范围 | 当前实物 | 来源与观察日 | 缺口 |
|---|---|---|---|
| BLS CPI-U SA指数：headline/core | [22个月CSV](../data/h10_bls_cpi_sa_monthly_2025_2026.csv)，2025-01至2026-10，两个序列各21个月非空 | [BLS CPI官方API](https://api.bls.gov/publicAPI/v2/timeseries/data/CUSR0000SA0?startyear=2025&endyear=2026)和[核心CPI](https://api.bls.gov/publicAPI/v2/timeseries/data/CUSR0000SA0L1E?startyear=2025&endyear=2026)；2026-11-14取得 | 2025-10原值缺失(“-”)，**不作补值、不能计算2026-10同比** |
| US Treasury每日名义par收益率 | [467交易日2Y/10Y CSV](../data/h10_us_treasury_2y_10y_daily_2025_2026.csv)，2025年249日、2026截至11-13共218日 | [Treasury 2025年XML](https://home.treasury.gov/resource-center/data-chart-center/interest-rates/pages/xml?data=daily_treasury_yield_curve&field_tdr_date_value=2025)和[2026年XML](https://home.treasury.gov/resource-center/data-chart-center/interest-rates/pages/xml?data=daily_treasury_yield_curve&field_tdr_date_value=2026)；2026-11-14取得 | 休市日(例如11-11)不填息率，不用前一交易日的值充当天数 |
| BEA 2026年核心PCE | [4条官方发布版本观测](../data/h10_bea_pce_release_vintages_2026.csv) | [2026-09-30公告](https://www.bea.gov/news/2026/personal-income-and-outlays-august-2026)和[2026-10-29公告](https://www.bea.gov/news/2026/personal-income-and-outlays-september-2026) | 仅本次关键版次样例，非完整2025–26原始PCE序列 |
| FOMC政策 | [2条正式决策](../data/h10_fomc_official_decisions_2026.csv) | [2026-09-16 Fed statement](https://www.federalreserve.gov/newsevents/pressreleases/monetary20260916a.htm)和[2026-10-28 Fed statement](https://www.federalreserve.gov/monetarypolicy/files/monetary20261028a1.pdf) | Fed speeches/目标预期未构建连续时序；Waller讲话不是决策 |

## 2. 可计算的观察结果（严格区分环比、同比、指数与年化）

BLS当前公开**季调指数快照**：
- 2026-09 headline指数336.298→2026-10指数337.476：`100×(337.476/336.298−1)=0.3503%`，发布稿按一位小数显示 **+0.4%**。
- 2026-08 headline 334.131→2026-09 336.298：`+0.6485%`，发布稿 **+0.6%**；月指数回算的小数与新闻稿公布的一位小数一致，不应该将0.3503当首次发布更精确百分比。
- 2026-09 core指数338.896→2026-10 339.900：`+0.2963%`，发布稿 **+0.3%**。
- 2026-07 core指数336.789→2026-10 339.900：近三个月复合增长按4个相同季度折年 `100×((339.900/336.789)^4−1)=3.7464%`。**这是按当前季调指数计算的近三个月折年化，不是过去12个月同比，不是BEA核心PCE，也不意味着未来会维持此速度。**
- 2025-10 BLS指数返回缺失，因此2026-10 CPI headline/core同比计算必须是**NA**；不得用视频单句或第三方估计代替缺失的官方当期同比。
- **统计口径**：此CSV为2026-11-14查询到的当前指数版本，并非过去每月的首次公告历史档案。未来要研究“当时美联储可知什么”，必须使用发布时版本/历史公告而非事后当前季调版。

### BEA 真实修订显示为什么PIT必不可少

| 参考月 | 首次发布日/值 | 下一版本 | 机制解释 |
|---|---|---|---|
| **2026-08 core PCE月环比** | 2026-09-30：**0.2%** | 2026-10-29对8月修订为**0.3%**，+0.1个百分点 | 2026-09-30作出的判断不可能提前使用10-29修订版 |
| **2026-09 core PCE月环比** | 2026-10-29：**0.3%**，同比**3.1%** | 未来才发布下一修订 | 2026-10-28会议召开时，此份9月报告**尚未发布** |
| **2026-09 headline PCE** | 2026-10-29：月环比**0.5%**，同比**3.6%** | 后续待观察 | PCE ≠ CPI；headline PCE ≠ core PCE |

数据来自BEA官方两个历史发行公告而非后验从FRED推断各版时间。

## 3. 已实现的 FOMC→Treasury 日期与数值检验

| 时点 | 事实名义政策/收益率 | 为什么不应直接解释为因果 |
|---|---|---|
| **2026-09-16** | FOMC正式加息25bp至3.75—4.00%，12比0通过 | 9月30日才发布的8月PCE不能当9月16日已公开依据；但当时还有其他旧信息 |
| **2026-10-28** | FOMC正式维持3.75—4.00%，10比2；两名异议者倾向加25bp | 10月29日的9月PCE与11月10日的10月CPI均**尚未发布** |
| 2026-11-09（周一） | 官方2Y=**4.56%**，10Y=**4.88%**；10Y−2Y=**32bp** | 观察值不是具体政治/通胀消息的净效应 |
| 2026-11-10（周二） | 官方2Y=**4.73%**，10Y=**4.98%**；10Y−2Y=**25bp** | 对上一交易日2Y **+17bp**、10Y **+10bp**、斜率**-7bp**；新闻报道的“盘中约18bp”与每日收盘口径不同 |
| 2026-11-11 | **Treasury官方时序无此休市日观察** | 不作前填值，不把未观测视为真实收益率不变 |
| **2026-11-13** | 2Y=**4.88%**，10Y=**5.15%** | 不能把11-10→11-13变化全部归因于11-10 CPI或Waller讲话 |

因此视频中“CPI降温但加息预期上升”是一个**有数据时序支持、但需要真正计量预期惊讶和利率分解才可检验**的市场解释。只有已观察到利率变化，并不能判断是Waller、BLS、资金需求、美债供给、期限溢价还是其他因素。它也不是已经确定12月FOMC结果。

## 4. 必须逐边验证的H10机制

1. `BLS/BEA公告日期/修订版 + 公告前一致预期`：目前CPI和PCE真实值有了，**公告前的专业一致预期数值缺失**，不能算真实surprise或识别通胀消息独立冲击。
2. `预期→FOMC决议`：目前得到9月加息、10月不动两个结果，**没有连续Fed基金期货/隔夜隐含政策路径**，个人官员讲话作为不同表记录。
3. `FOMC/利率路径→UST/信用利差`：已得到467个官方2Y/10Y每日值，**没有同日即时利率期货/信用利差和期限溢价分解**；不能用10Y=FOMC预期率。
4. `信用/新债定价→企业利息/到期债务和FCF`：尚无同法人同期间SEC面板，**没有公司层面的量化结果**。H09×H10的交互仍不可估计。

## 5. 离线复算及已做的验证

- [Python标准库复算脚本](../analysis/recompute_h10_open_data.py)检查4个真实CSV：月份22且Oct2025缺失、数据未f-fill、Treasury 467行无重复、11月9日/10日17bp与10bp、BEA8月0.2→0.3修订、两次FOMC真实决策和公布先后。
- Ubuntu MCP在本轮实际将GitHub分支CSV全文送入该脚本运行，返回 `validation: PASS`；核心3M折年化3.7464%、Treasury spread32→25bp均由脚本计算。**校验的是算术及时间关系，不是未来命中率、统计显著性、政策因果。**
- 部分FRED CSV请求在Ubuntu出现超时，最终**改从BLS直连公开API和Treasury官方XML**获取CPI和收益率；BEA核心PCE使用官方不同时点的公告版本。此轮不把未下载的全量PCE写成已取得。

## 6. 下一轮具体计算优先级

从BEA原始NIPA数据/可合法获取的历史归档新增2025—26核心PCE完整指数及可核首发版本，联动每次FOMC决议和Fed Watch/期货**公告前**价格。将CPI发布窗口内 `1h/1d` 的2Y收益率变化分成预期利率、期限溢价和信用利差（仅在市场高频数据真正取得时）；加上PIT和同日其他新闻做对照。公司的债务期限结构与浮动利率暴露必须来自SEC或债务附注原件，未披露的私人公司保持NA。


## 33个月BEA连续月度PCE（后续2026-11-14同日补齐）
- 已从[BEA Section2All官方NIPA Excel](https://apps.bea.gov/national/Release/XLS/Survey/Section2All_xls.xlsx)直接下载并读取`T20804-M`，对`DPCERG`整体PCE与`DPCCRG`核心PCE做了**2024-01—2026-09共33个月季调指数**，含月环比、12月同比及原始SHA： [完整33行CSV](../data/h10_bea_nipa_pce_headline_core_2024_2026_snapshot.csv)。
- 2026-09按2026-11-14版本指数复算headline月环比0.4908%、core月环比0.3165%、headline同比3.6489%、core同比3.1212%；与BEA官方10-29公告分别+0.5%/+0.3%/+3.6%/+3.1%吻合。
- 2026-08核心PCE后见指数复算0.2620%，**不是9月30日首次公开的0.2%版本**；保留历史首发记录表不覆盖。新[离线验证程序](../analysis/recompute_h10_bea_snapshot.py)已用GitHub CSV实际在Ubuntu执行PASS。研究仍缺宏观预期冲击、高频利率和公司债务数据，不允许宣称H10因果验证。
- [独立BEA系列与数据版本详细报告](2026-11-14_h10_bea_pce_monthly_series_and_vintage.md)。
