# TOPIC-011 H03 第十一轮｜2026-01总量附件、2026-02订正B9、合并表与五月回顾的EKPC/PSA来源差异精确溯源

> **审计结论（2026-11-14）**：此前未解释的PJM2026 Accuracy v2026 RTO数值比当时可下载2026合并原版B9b高9—10MW，现已**精确定位为EKPC区域是否包含负向削峰计划(peak-shaving adjustment)项**，而不是数据中心需求新增加9—10MW。检验了2026—2046共**21个目标年、23个一级区域**，两组不同工作簿对比中**只有EKPC与聚合RTO两行出现差异**，其余21个一级区域在21个目标年全部相等。重复两组B9/B9b对照、再与五月Accuracy数值比对，双层差分均闭合。**仍未取得2/6订正前B9完整原始版本字节，不能计算本次勘误本身造成多少MW变化。**

## 1. 四个不同发布的数据来源（逐档SHA固定）

| 来源与时点 | 官方文件 | SHA-256 / 大小 | 检验到的含义 |
|---|---|---|---|
| 2026-01-14官网列出的独立B9b总量附件，XLSX内修改于**2026-01-13 16:17:25Z** | [Total Load Adjustments Breakdown](https://www.pjm.com/-/media/DotCom/planning/res-adeq/load-forecast/total-load-adjustments-breakdown.xlsx) | `ee3b682929db0b59a043c8ab6d1c9776f697ab10fc86fe603a6d0d724893c4ba` / 18,904 bytes | RTO目标2027=**15,866MW**，EKPC=0；文件内部日期只是最后修改元信息，结合官网1/14目录日期支持早期发行，但不等于独立第三方档案记录其每个公开时点 |
| 2026-02-06**经embedded算法修订**的独立B9额外调整表 | [Load Adjustment Breakdown for Capacity Obligations](https://www.pjm.com/-/media/DotCom/planning/res-adeq/load-forecast/2026-load-adjustment-breakdown-for-capacity-obligations.xlsx) | `990e2cb82d02a6c689a9e21b5c7ccb13944613f960dcc2f6eb3109e51a49d6a1` / 19,177 bytes | B9表第3行确写`updated 2/6/2026 to correct for an error calculating embedded`；XLSX修改于2026-02-06 13:00:15Z。目标2027 RTO=**10,795MW**，EKPC=0，**不是更正前的1/14 B9** |
| 2026**当前可下载合并工作簿**，B9仍写明2/6订正 | [2026 Long-Term Load Report Tables](https://www.pjm.com/-/media/DotCom/planning/res-adeq/load-forecast/2026-load-report-tables.xlsx) | `59a62facf819962e430101c96dd1335229d8173fb6886dd8045ced325443f607` / 371,564 bytes | B9b目标2027 RTO=**15,856MW**，B9=**10,785MW**，EKPC在两表中都为**-10MW** |
| 2026-05-29准确性报告回顾工作簿 | [2026 Accuracy XLSX](https://www.pjm.com/-/media/DotCom/planning/res-adeq/load-forecast/2026-accuracy-report.xlsx) | `e0f24fe03a79af016826089c653b2c2e15e55edcb04a7bd4be5fa643136425fc` / 50,175 bytes | 对2026版`Forecast July Peak`的RTO序列，在**2026—2046共21个目标年全部与1月独立B9b RTO相等**；不等于新实际用电 |

数据： [21年RTO与EKPC一致性表](../data/h03_pjm_2026_ekpc_source_reconciliation_2026_2046.csv) · [23个区域的全时段对照摘要](../data/h03_pjm_2026_ekpc_zone_source_match_summary.csv) · [发布版本、SHA及元信息清单](../data/h03_pjm_2026_jan_feb_publication_manifest.csv)。

## 2. RTO恰好差一个EKPC的负向削峰项：21个年度全部验证

对2026—2046逐个目标年（**这里的年份是未来负荷预测的目标，不是该年已经发生的结果**），两个独立附件和合并工作簿之间全部满足：

`Jan B9b standalone(RTO) − Combined B9b(RTO) = − Combined EKPC(B9b)`

`Feb-corrected B9 standalone(RTO) − Combined B9(RTO) = − Combined EKPC(B9)`

`Jan B9b standalone(RTO) = 2026-May Accuracy(v2026) RTO`

`Jan B9b standalone(RTO) − Feb B9 standalone(RTO) = Combined B9b(RTO) − Combined B9(RTO)`

按照每年所包含的EKPC负数项目，全部差值为：

| 未来目标年 | 独立附件EKPC | 当前合并表EKPC | 独立附件RTO－合并RTO |
|---|---:|---:|---:|
| **2026—2031（6个）** | 0MW | **-10MW** | **+10MW** |
| **2032—2037（6个）** | 0MW | **-9MW** | **+9MW** |
| **2038—2046（9个）** | 0MW | **-8MW** | **+8MW** |

不仅RTO相符，而且两组文档比对的**23个顶层zone**中，恰好只有EKPC和RTO在21年各有21次差异；其他**21个zone×21年=441个比较点在每组都完全一致**。故此前源差是**已精确定位的负荷计量边界差**，不能再标为`UNEXPLAINED_SOURCE_DIFFERENCE`。

**官方语义证明**：
1. PJM的[2026年1月Total Monthly Load Adjustments附件](https://www.pjm.com/-/media/DotCom/planning/res-adeq/load-forecast/total-monthly-load-adjustments.xlsx)，原工作表**第2行**明写`These values below do not include Peak Shaving Adjustments (PSA) Adjustments`，原始SHA `d9e547c71e4176776028b1c323759830f9fcd5ed908af142be783464aae9a2ff`（59,187 bytes）。虽然它是**月度**源而非独立年度表的逐字政策说明，但支持相同附件类别对PSA的排除。
2. [PJM官方2026-01-14预测说明](https://insidelines.pjm.com/pjms-updated-20-year-forecast-continues-to-see-significant-long-term-load-growth/)公开标注**EKPC为自2023交付年度起运行的削峰计划**，而其他区域含数据中心/工业/港口或电压优化。依据此背景，合并表EKPC负数最符合PSA调整。
3. **精确可证的事实**是`EKPC 0 vs −10/−9/−8 + RTO相同数值偏移`。至于为何不同发布附件选择不同PSA包含规则，PJM没有在这些工作簿中另行发布正式错误归因声明，故不擅自定性“PJM算错10MW”或“原文件被篡改”。

## 3. 对2027版本修订有实际意义：不同来源得出-1,855/-1,860/-1,865MW

将**2025原版B9b**目标2027 RTO预测**17,721MW**作为历史基线，对2026两个来源分别计算：

| 同目标2027RTO比较 | 旧版基线 | 2026版 | 总预测修订 |
|---|---:|---:|---:|
| 2025原版B9b → 2026**1月独立B9b** | 17,721 | 15,866 | **-1,855MW (-10.468%)** |
| 2025原版B9b → 2026**当前合并B9b（含EKPC）** | 17,721 | 15,856 | **-1,865MW (-10.524%)** |
| 2026五月Accuracy表中的**2025回顾版与2026回顾版** | 17,726 | 15,866 | **-1,860MW (-10.493%)** |

三者差10MW的主要原因已经明确到EKPC是否纳入；另一处差5MW源于之前已查到的**2025原版与2026 Accuracy回顾中对2025预测标签的不同数值**，不属于本次EKPC审计解决的同一个问题。

**这三种都只是模型预测版本的变化，不能当成真实2027发电缺口、已撤销的数据中心容量或政治因果结果。**

## 4. 2023、2024缺乏B9b原版的原因，不再无止境搜索“同一表”
[2025年1月24日PJM原始Long-Term Load Forecast报告第4页](https://www.pjm.com/-/media/DotCom/library/reports-notices/load-forecast/2025-load-report.pdf)明确写明：**2025报告新增首次发布`Total Load Associated` Table B-9b**。因此2023与2024原版文件只有B9 Above Embedded而没有该同名B9b表，是**历史公开体系的实质性改变**；不能假装2023/24当时已有可下载的官方同名B9b原版数据。

这使前一轮对2023/24的`original B9 vs June2025 retrospective Total`差额必须永远保留`CROSS_PUBLICATION_PROXY_NOT_SAME_RELEASE`，即使该差额多年份较稳定，也不能升级为同版精确已嵌入部分。严格的B9/b9b同原版统计序列从**2025年**开始。

## 5. 未解决的唯一关键数据缺口与H03因果边
**仍缺**：2026-01-14发布时、2026-02-06之前**真实未修订B9表的旧字节**或PJM官方更正差异记录。现取得的2/6独立B9与当前合并B9的差异只在EKPC，**不能据此推算2月勘误影响了多少MW**。通过互联网归档元数据接口的测试曾出现超时，未取得满足SHA/原值的公开快照，不能报勘误影响为0或为10MW。

**已经关闭的研究缺口**：
- 2026-May Accuracy RTO比2026当前合并B9b高9—10MW的来源差异：已在21年全量验证归因到EKPC负向削峰调整差；
- 2023/24“为何没有同原版B9b”——PJM 2025原报告明确该表当年新引入；
- 2026-01-14对应的独立B9b早期公开总量及SHA：已取得且元信息支持发布日期，不再只能用事后回顾数值。

所有观测均为2025/26、2026中期选举前已经存在的模型定义/发布数据，不说明2027新国会导致AI投资取消；H03与H08政治因果继续`UNTESTED`。

## 6. 复算及验收
[标准库离线/源四工作簿逐格核验](../analysis/recompute_h03_ekpc_source_reconciliation.py)：CSV模式验证21个目标年、23个zone汇总、来源SHA及版本敏感性；使用`--jan-b9b`、`--feb-b9`、`--combined`、`--accuracy`附上从PJM官网取得的原始文件，会同时检查**23×21×两个对照的区域格子**、January B9b与May Accuracy整个21年RTO曲线一致、两个附件与合并表的EKPC差、Jan13和Feb6文件元数据、以及2026 combined B9的2/6注释。

这次研究从“未解释的回顾表差异”升级为**具体分区EKPC负荷削峰项的来源行级审计**，同时保留未获得修订前B9的真实缺口。
