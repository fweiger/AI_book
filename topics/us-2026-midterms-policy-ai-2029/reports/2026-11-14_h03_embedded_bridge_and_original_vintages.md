# TOPIC-011｜H03第九轮：从原始 Table B-9 到 B-9b，识别数据中心大型负荷的“已嵌入基础负荷”统计桥接（2026-11-14）

> **研究发现**：此前PJM跨年度数字不一致的一个确定原因，是原始预测报告的`B-9 Adjustments Above Embedded`与后来`Total Load Associated with Adjustments`（总关联负荷）**不是同一指标**。2025年原版工作簿含两张表，能够在**完全相同的原始文件**中独立验证两者关系：2025年目标RTO额外调整**3591MW**，总关联负荷**7729MW**，相差**4138MW**，**不能将4138MW当作被取消或延期项目**。2023/24旧版本的类似差额在不同公开文件之间也存在、且跨未来年份近似稳定，但严格标为`CROSS_PUBLICATION_PROXY`，不是已经证明的同源精确分解。政治因果继续UNTESTED。

## 1. 三个版本原始来源与信息时点
| 预测版本 | 原始表格 | 原始载体和状态 | 2025-06的总负荷数据来源 |
|---|---|---|---|
| 2023 | Table B-9（above embedded） | [PJM 2023报告](https://www.pjm.com/-/media/DotCom/library/reports-notices/load-forecast/2023-load-report.pdf)，封面写“January 2023”，LAS网页列为2023-05-22，真实首次公开时点尚需独立确认 | [PJM LAS June2025历史追踪第7页](https://www.pjm.com/-/media/DotCom/committees-groups/subcommittees/las/2025/20250613/20250613-item-03---large-load-adjustment-process-improvement-discussion.pdf)记录“2023 Load Forecast”总调整量 |
| 2024 | Table B-9（above embedded） | [PJM 2024报告](https://www.pjm.com/-/media/DotCom/library/reports-notices/load-forecast/2024-load-report.pdf)，封面“January 2024，**Revised 2/1/2024**”；LAS网页记录2023-12-27，**不等于这份已修订的内容于12月就可知** | 同一PJM 2025六月追踪稿记录“2024 Load Forecast”总调整量 |
| 2025 | **Table B-9与B-9b** | [PJM 2025原始XLSX](https://www.pjm.com/-/media/DotCom/planning/res-adeq/load-forecast/2025-load-report-tables.xlsx)（SHA `a9a797f2d3cf34154db466b74e045d1334dfebede87ec6dc3739805093474ef5`）**在同一文件可精确相减** | Total使用原版B-9b，可与2025六月回顾表交叉核对 |
| 2026后验 | Retrospective`Historical/Forecast July Peak` | [2026年5月准确性XLSX](https://www.pjm.com/-/media/DotCom/planning/res-adeq/load-forecast/2026-accuracy-report.xlsx) SHA `e0f24fe03a79af016826089c653b2c2e15e55edcb04a7bd4be5fa643136425fc`，这不是上述原始B9/B9b定义的自动替换 | 定义/月份/覆盖差异需另查，不能并表 |

**保留前轮未解决的时点风险**：2023 PDF内部“January 2023”与LAS网站文件发布日期2023-05-22不一致；2024当前PDF则显式于2024-02-01修订。故当前2023/24 Table B-9与2025六月回顾`Total`之间不仅指标定义不同，原始版本时间也不同。**只有2025原版同一工作簿B-9 vs B-9b能够确证精确差额**。

## 2. 21条目标年桥接：差额近似一个年度不变的基础项
数据：[2023—25三个版本21条桥接CSV](../data/h03_pjm_original_above_embedded_vs_total_bridge_2023_2030.csv)与[版本统计](../data/h03_pjm_embedded_bridge_vintage_summary.csv)。

| 预测版本 | 覆盖目标年 | 首年额外调整 B-9 | 首年总关联负荷 | 差额 MW | 差额占总量 | 跨年份差额范围 | 差额变异系数 |
|---|---|---:|---:|---:|---:|---|---:|
| 2023 | 2023—2030（8年） | 2231 | 3957 | **1726** | 43.62% | 1616—1726 MW | 2.10% |
| 2024 | 2024—2030（7年） | 2664 | 5682 | **3018** | 53.12% | 2937—3035 MW | 1.16% |
| **2025** | **2025—2030（6年）** | **3591** | **7729** | **4138** | **53.54%** | **4053—4255 MW** | **1.52%** |

从数学形态看，每版所覆盖未来数年`total−above`差额近似常数（变异系数约1—2%），与一个在预测基线中已有的相对稳定负荷存量相容。**但2023/24的两个来源年份不一致，不能直接认定真实嵌入MW恰等于这组proxy。** 同时，各年度这些都是多个大型负荷种类的统计，不能自动叫纯AI数据中心MW。

## 3. 2025年**同一原始XLSX**精确分解到主要区域
通过Table B-9与B-9b同一行目标年2025—2030的原值逐年核算，并以PJM RTO作为整体、DOM与AEP作为两个不重叠区域、其他RTO取差值；没有把父区加到汇总后重复计算。

| 2025年目标 | B-9 Above Embedded | B-9b Total Associated | 差额 | 占RTO差额 |
|---|---:|---:|---:|---:|
| DOM | 1,684 | 4,970 | **3,286** | **79.41%** |
| AEP | 1,412 | 1,761 | **349** | **8.43%** |
| RTO剩余其他区域 | 495 | 998 | **503** | **12.16%** |
| **PJM RTO** | **3,591** | **7,729** | **4,138** | **100%** |

各区域和年份计算见[2025原版按区分解的24行CSV](../data/h03_pjm_2025_within_workbook_zone_bridge.csv)。后续2026—2030每一年`RTO = DOM + AEP + OTHER_RTO`在B-9、B-9b及差额三项上均成立。**这只是两张表所统计的负荷定义差，**不是所有DOM数据中心已运行或需要增加的资本开支。B-9b中的Total Associated是2025年年度大型负荷关联总量，B-9仅对基础预测额外增加的量，因而原始数据直接相减具有意义。

## 4. 原本“2025新版预测更差”结论：换原始公开总量源，排序竟能反转
评价对象仍使用**后来2026五月报告的同一个2025 RTO历史实际值8,167.174MW**，但选择两种不同的**预测来源公开版本**，得到：

| 预测来源/版本 | 用于2025的预测MW | 同一后验实际MW | 绝对误差/实际 |
|---|---:|---:|---:|
| **2025六月LAS Total**，标记2024版 | 7,642 | 8,167.174 | **6.430%** |
| **2025六月LAS Total**，标记2025版 | 7,729 | 8,167.174 | **5.365%（新版更准）** |
| **2026五月Accuracy Retrospective July**，标记2024版 | 7,939.180 | 8,167.174 | **2.792%** |
| **2026五月Accuracy Retrospective July**，标记2025版 | 7,735 | 8,167.174 | **5.292%（新版更差）** |

**关键边界**：
1. 此评价是**混合后验实际定义的来源敏感性实验**，不是合格的历史PIT策略回测；2025六月材料的2024版总量并未核对为2024 PDF原始发行的严格同定义总量。
2. 2026五月的July Peak回顾表和2025六月的Summer/Total都可能存在月份、项目群、嵌入量重估等统计差异，不能称同模型预测性能真的反转。
3. 但它定量证明：**当历史数据口径没有被先验锁定时，研究者可以仅通过“换一个看起来同名的来源版本”得到完全相反的模型好坏叙述。** 从这一步起，不能再拿“预测比上一版低”直接证明真实数据中心投资减速。

全部源数：[四行排名敏感性](../data/h03_pjm_rto_2025_forecast_ranking_by_publication.csv)。

## 5. 对此前研究体系的增量改造
- **先区分数据层**：合同企业/ELOA-CLOA-ESA → PJM数据中心专属表 → PJM Above Embedded B-9 → PJM Total Associated B-9b → PJM2026 Accuracy July Peak历史/预测，各层单独来源键。尤其禁止跨部门把B-9与B-9b直接叠加或混用。
- **显式来源版本**：键至少包含`target_year,forecast_vintage,source_document,publication_date,revision_date,zone,load_scope,measurement_basis`。2024原始报告现有PDF明确Revised 2024-02-01，与LAS列表“2023-12-27”不能合并为一个无歧义PIT。
- **版本化回测**：用原始文件分别冻结B-9和B-9b；只在真正同定义/同目标/同区域下做跨年时间序列。缺原始TOTAL的2023/24只给跨来源proxy，不得编造精确嵌入量或新指标显著性。
- **实际效应**：到2027以后，必须匹配真实DC客户同时峰值、预计/实际送电日期、项目Firm状态与真正新增政策生效事件；2026选前已有电网/合同/宏观限制，不把真实负荷下修自动归因于新国会。

**H03政治因果仍UNTESTED**。本轮完成的是把之前一类“历史版本漂移”从纯未知升级为**已证实的统计定义差别**（2025同源B9/B9b），并把依然未知的跨文件定义差保留，未擅自宣布历史预测欺诈、真实项目取消或2030供电缺口实际发生。

## 6. 可重复核算
- [纯Python标准库复算](../analysis/recompute_h03_original_bridge.py)：离线读取21条预测版本桥接、3个版本摘要、24条2025同工作簿区级分解、4条排名敏感性、5条原始版本档案，断言数值与分区汇总。
- 带`--original-2025-xlsx /path/to/2025-load-report-tables.xlsx`可直接**校验SHA并抽取Table B-9/B-9b全部6年RTO、DOM和AEP共36个格子**，与CSV逐项比对。
- 2023/24B-9来自原版官方PDF，2025六月Total来自官方LAS材料，因跨文件而无法用上面的2025原版XLSX校验开出“单一原版精确嵌入”结果；这正是来源审计应保留的限制。
