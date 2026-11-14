# H10｜BEA官方NIPA月度PCE指数：33个月的真实数据与发布版本边界（2026-11-14）

## 已实际取得的原始文件
- BEA [National Income and Product Accounts Section 2 All官方Excel](https://apps.bea.gov/national/Release/XLS/Survey/Section2All_xls.xlsx)，通过 Ubuntu MCP 用Python标准库下载并解压XLSX；使用Workbook `T20804-M`（Table 2.8.4 Monthly Personal Consumption Expenditures Price Indexes），表内`DPCERG` headline PCE和`DPCCRG` PCE excluding food and energy。读取时段**2024年1月至2026年9月**，每月一行，共33个真实月份，没有人为缺值补齐。
- 原XLSX SHA256: `f5037feeafb3bee0718acd3214a30e8e777b3110ee2d7b7698beb14084485391`，取得日期**2026-11-14**，保留在每条数据行中。按期间和发布日期区别，**该2026-11-14快照不是2024/25年各月的首次公开版本**；经济数据可能经历多次修订。
- [33行headline/core PCE月度机器表](../data/h10_bea_nipa_pce_headline_core_2024_2026_snapshot.csv)，每行保存月份、headline/core季调指数、相邻月环比及12月同比、SHA、来源链接及 `CURRENT_BEA_NIPA_FLATFILE_NOT_ORIGINAL_MONTHLY_RELEASE` 来源标签。

## 实际复算

| 2026-09同口径最新BEA指数 | CSV计算 | 官方2026-10-29公告一位小数 |
|---|---:|---:|
| Headline PCE 环比 | 0.490840% | 0.5% |
| Core PCE 环比 | 0.316502% | 0.3% |
| Headline PCE 同比 | 3.648874% | 3.6% |
| Core PCE 同比 | 3.121160% | 3.1% |

公式：`100*(I_m/I_(m-1)-1)` 为月环比；`100*(I_m/I_(m-12)-1)` 为同比。2024年1—12月同比因没有2023年月度值，在本次定界窗口内写空值，不凭空推算。官方核对：[BEA 2026-10-29 Personal Income and Outlays September 2026](https://www.bea.gov/news/2026/personal-income-and-outlays-september-2026)。

**尤其重要的版本差异**：2026年8月Core PCE按本快照指数复算月环比约**0.2620%**，对应后期修订后的约0.3%。但BEA [2026-09-30首次8月公报](https://www.bea.gov/news/2026/personal-income-and-outlays-august-2026)曾公布0.2%；10月29日下一次公报修订为0.3%。**研究2026-09-30时的美联储可知信息必须使用0.2%首发版本，不得用0.2620%的后见指数倒填。**

## 可检验与不可检验边

- **已成立**：月度PCE连续序列存在、官方截止版本能够抓取；September 2026计算与公报四项数值对应；可明确记录修订后的回溯值。
- **待验证**：真实历次发布版本/交易日前专业一致预期、Fed基金期货事件内市场预期、美国Treasury高频收益率与企业债务/现金流传导。仅有PCE指数与FOMC日历不能估计“政策加息/降息概率”或联动因果。
- **验证**：[recompute_h10_bea_snapshot.py](../analysis/recompute_h10_bea_snapshot.py)，标准库离线读取CSV/可接受`--stdin-csv`，逐行计算环比同比、验证33个月、期间跨度、SHA一致和September一位小数口径。GitHub Actions结构检查仅查链接/图谱，不代替这个数值复算。

## 对H10后续实验的贡献

现可将BLS CPI指数（2025-01—2026-10、2025-10缺测）与BEA核心PCE（2024-01—2026-09）按**经济指标期间**对齐，再根据**发行日**分别形成决策前的信息集；与2026-09-16 +25bp、2026-10-28维持的实际FOMC记录和467个交易日Treasury 2Y/10Y收益率核对。下一步应增加真实的发布前预期与Fed基金期货价格，才有能力判断从新闻冲击到利率变化的传导强度，暂不做不具备识别条件的回归。
