# H10｜固定2025全年11次CPI公布日、同一个事前共识发布者：方向规则复核（2026-11-14）

> **比此前跨年、跨机构的10次便利样本更有辨识力的负对照**：预先固定2025年全部11次真实BLS CPI公布日，只使用**Calculated Risk网站在公布前带原始发表时间的同一类市场共识**；可取得7次、4次保持数据缺失，不从事后供应商历史日历、单机构预测或其它发布者回填。结果：**整体CPI正/负surprise与2Y美债同向2/5，核心2/4；双侧精确二项p均为1.000**。这说明此前10个跨年精选样本的核心6/7同向结论对**样本构建/不同年份和来源的选择**很敏感。该新检验同样不能归因CPI纯冲击，因为市场端只有Treasury全日收益率。

## 1. 冻结样本和可用性

2025年实际CPI公布日共**11次**：[BLS官方归档](https://www.bls.gov/bls/news-release/cpi.htm)。其中2025-10的数据因政府停摆未发布，2025-09数据实际于10-24发布。固定2025-01-15、02-12、03-12、04-10、05-13、06-11、07-15、08-12、09-11、10-24、12-18，不因研究结果反向决定保留哪天。

在全部11次中，从同一个提前发布市场共识的来源 [Calculated Risk](https://www.calculatedriskblog.com/) 找到7篇**有具体发表时间且早于BLS首次发布**的文章：
- [2025-01-14 08:12 EST](https://www.calculatedriskblog.com/2025/01/cpi-preview.html)：12月headline CPI SA MoM预期0.3%，core0.2%；当次[BLS首次公布](https://www.bls.gov/news.release/archives/cpi_01152025.htm)0.4%/0.2%。
- [02-11 14:13 EST](https://www.calculatedriskblog.com/2025/02/cpi-preview.html)：预期0.3/0.3，次日[BLS公布](https://www.bls.gov/news.release/archives/cpi_02122025.htm)0.5/0.4。
- [03-11 14:51 EDT](https://www.calculatedriskblog.com/2025/03/cpi-preview.html)：预期0.3/0.3，次日[BLS公布](https://www.bls.gov/news.release/archives/cpi_03122025.htm)0.2/0.2。
- [06-10 11:55 EDT](https://www.calculatedriskblog.com/2025/06/cpi-preview.html)：预期0.2/0.3，次日[BLS公布](https://www.bls.gov/news.release/archives/cpi_06112025.htm)0.1/0.1。
- [07-14 14:31 EDT](https://www.calculatedriskblog.com/2025/07/cpi-preview.html)：预期0.3/0.3，次日[BLS公布](https://www.bls.gov/news.release/archives/cpi_07152025.htm)0.3/0.2。
- [08-10 08:42 EDT](https://www.calculatedriskblog.com/2025/08/cpi-preview.html)：预期0.2/0.3，次[BLS公布](https://www.bls.gov/news.release/archives/cpi_08122025.htm)0.2/0.3。
- [09-09 13:01 EDT](https://www.calculatedriskblog.com/2025/09/cpi-preview.html)：预期0.3/0.3，次[BLS公布](https://www.bls.gov/news.release/archives/cpi_09112025.htm)0.4/0.3。

**没有找到同一发布者、符合事前源日期标准的四次**：2025-04-10、05-13、10-24、12-18。它们在11行机器表中为空，不用Reuters/Continuum单机构值、事后网页或零替代。Calculated Risk文章当前可读且元数据有发表日期，**并非独立网页快照证明文章文本完全未被事后修改**；结论应保留这一版本风险。

## 2. 真实同来源逐月表

| CPI公布日 | Headline预期→实际 (%) | Core预期→实际 (%) | 2Y收益率全日变化 | 惊讶与2Y方向的观察 |
|---|---|---|---:|---|
| Jan 15 | 0.3→0.4 | 0.2→0.2 | **-10bp** | Headline偏热、收益率反跌 |
| Feb 12 | 0.3→0.5 | 0.3→0.4 | **+7bp** | 两项偏热、收益率上涨 |
| Mar 12 | 0.3→0.2 | 0.3→0.2 | **+7bp** | 两项偏冷、收益率反涨 |
| Jun 11 | 0.2→0.1 | 0.3→0.1 | **-7bp** | 两项偏冷、收益率下跌 |
| Jul 15 | 0.3→0.3 | 0.3→0.2 | **+5bp** | Core偏冷、收益率反涨 |
| Aug 12 | 0.2→0.2 | 0.3→0.3 | -4bp | 两项与预期一致，**不纳入非零surprise检验** |
| Sep 11 | 0.3→0.4 | 0.3→0.3 | **-2bp** | Headline偏热、收益率反跌 |

原始Treasury各日的两年期有符号变化来自[2023—26官方967日Treasury基线](../data/h10_cpi_release_ust_46events_2023_26.csv)，这只是从上一交易日到公布日的**整日观察**，没有单独分离08:30数据公布、Fed发言或当天债券供给因素。

## 3. 完整固定来源样本结果及与前轮对比

| 指标 | 同源2025有效非零surprise | 2Y方向非零 | 同向 | 双侧Exact二项p |
|---|---:|---:|---:|---:|
| **Headline CPI** | 5 | 5 | **2/5** | **1.000** |
| **Core CPI** | 4 | 4 | **2/4** | **1.000** |
| Core剔除Mar12反例（事后敏感性，不作为主结论） | 3 | 3 | 2/3 | 1.000 |

与此前[跨年跨机构10日期样本](2026-11-14_h10_pre_release_forecasts_10_pit_vs_vendor_not_pit.md)中核心**6/7同向、双侧p0.125**不同。两组样本重合但不等价；不同年份的利率环境、样本入组选择、预测提供者和机构与共识口径均可能造成明显差异。**同源2025结果表明不能外推出“核心CPI惊讶→2Y日收益率同向概率约86%”**。样本仍小且非完整，但我们**没有**为了提高命中率将缺失4期强行填入，也没有拿单机构优于/劣于市场共识的预测替代同源共识。

## 4. 识别强弱和具体结论

- 该实验“来源更统一、固定2025年完整公布日作分母”提高了**选样透明度**，但选择只覆盖7次的同一个发布者仍会有**可获得性偏差**。没有真正全体经济学家预测问卷及各页Web Archive当时字节，仍不能叫严格机构共识PIT数据库。
- 大部分月度CPI一位小数舍入为`±0.1pp`阶梯，不能提供微弱真实意外值的连续幅度。真实市场利率还可能定价同比、住房/服务分项、上一期修订和其它新闻；未获得分钟或期货数据就不能估计因果。
- 本轮仅足以否定“拿之前跨源6/7的历史命中当作已获验证的市场交易规则”这类强表述，**不否定更严谨的核心通胀意外值在高频债券市场中可能存在反应**。H10完整`CPI/PCE→Fed预期→FOMC真实政策→企业融资`仍`UNTESTED`。

## 审计资产
- [固定2025所有11次发行、7份事前来源、4次空缺的CSV](../data/h10_cpi_consistent_publisher_2025_pre_release_cohort.csv)。
- [Python标准库可运行复算](../analysis/recompute_h10_2025_consistent_publisher_cpi_direction.py)，Ubuntu MCP将GitHub最新源码/CSV执行 `--stdin-csv`，获得 **validation=PASS**、headline2/5、core2/4、exact p=1.000。没有构造收益/交易规则。
- 后续必须先取得**同一家真实发布前预期源对2023—2026全部事件的完整序列**或另一套真正存档的问卷，加上08:29/08:35 Treasury/FF期货行情，再计算真正 surprise-response 的宏观状态模型。
