# TOPIC-011｜H03第十二轮：追溯2026年1月原始B9修订前字节的证据资格与负荷预测修订规模对照（2026-11-14）

> **核心判断：本轮取得PJM 1月原始报告PDF的可验SHA，并确认其36页正文没有可恢复的修订前B-9数值表。现存所有已核官方B9表都含2月6日勘误；独立1月B9b仅包含总关联负荷，不能替代原始B9。故Feb6修订前后“改变多少MW”当前仍无法计算（NA），不可推定为0、8/9/10或1,018MW。**
>
> 本轮另做一个新的描述性对照：2027—2029目标年`B9b关联总负荷预测修订绝对值/全RTO夏季峰值预测修订绝对值`约46%—50%。**这不是严格的因果贡献率，更不是2027国会政策/AI实体取消份额，因为B9b与模型基础量重叠，且混有非数据中心大型负荷**。

## 1. 可核对的2026年1月报告PDF：没有B9数值附件

本轮从[PJM官方2026年1月14日Long-Term Load Forecast PDF](https://www.pjm.com/-/media/DotCom/library/reports-notices/load-forecast/2026-load-report.pdf)直接读取完整原始字节，文件**8,750,526 bytes**，SHA256 `9f2826cfc39357c54d6e6203e60946b6ce9ea627cfceeeaf4d4cd343066c6bc8`，共**36页**，PDF元数据CreationDate为`2026-01-12`，报告封面写**Posted Date: January 14, 2026**。本轮逐页检索`Table B-9`、`Adjustments Above Embedded`及总负荷表格，没有发现完整原始B9数值表。报告在Executive Summary明确表示**所有详细表格改由Excel提供**，PDF仅引用B9/B9b外部表。

**重要：这只证明当前官方PDF不包含该附表，不证明2026-01-14历史上从未公开过单独B9 XLSX。** 单独原B9可能存在于被覆盖/归档的历史字节，不应因为当前官网404或未找到就称其历史上不存在。

[PJM官方2026预测发布索引](https://www.pjm.com/planning/resource-adequacy-planning/load-forecast-dev-process.aspx)明确把1月14日主报告/表格与2月6日`Load Adjustment Breakdown for Capacity Obligations`分开，且独立B9的原文件备注`updated 2/6/2026 to correct for an error calculating embedded`。

## 2. 严格的“源文件是否真的足以计算勘误”判别表

| 输入 | 状态与原始证据 | 可否算2/6纠正MW？ |
|---|---|---|
| 2026-01-14主PDF，创建2026-01-12，36页 | 正文无原版B9数值，SHA固定 | **否** |
| 2026-01-13修改、PJM1/14归档的独立B9b | SHA `ee3b682929db0b59a043c8ab6d1c9776f697ab10fc86fe603a6d0d724893c4ba`，2027 RTO总关联15,866MW | **否，B9b不是B9** |
| 2026-01-14之前或当天未订正B9 | **尚无真实原文件SHA/逐行数值** | **不可计算** |
| 2026-02-06更正后的B9 | SHA `990e2cb82d02a6c689a9e21b5c7ccb13944613f960dcc2f6eb3109e51a49d6a1`，原文件确有2/6日期注释 | 仅更正后数值，**否** |
| 当前合并B9/B9b | SHA `59a62facf819962e430101c96dd1335229d8173fb6886dd8045ced325443f607`，包含2/6注释且EKPC削峰项 | 不能替代1/14原B9 |
| 2026-05 Accuracy同标签回顾 | SHA `e0f24fe03a79af016826089c653b2c2e15e55edcb04a7bd4be5fa643136425fc`，RTO等于独立1月B9b而非原B9 | **否** |
| 2026-01-23 LAS建模说明 | [官方会议演示](https://www.pjm.com/-/media/DotCom/committees-groups/subcommittees/las/2026/20260123/20260123-item-03---pjm-2026-long-term-load-forecast---presentation.pdf)仅确认历史DC剔除和B9的no-removal敏感性模型 | 算法足够解释定义，但没有可核的更正前B9逐年数值 |

**检索强度及限制**：本轮还检查公开GitHub上已提交的2026 PJM官方工作簿SHA，能找到的2026年10月外部研究镜像也同样是**更正后combined SHA**。尝试Wayback/CDX访问Jan—Feb 2026旧文件，远端访问超时；**超时不能解释为Wayback没有该档案**。不能按猜测填补修订前B9行。

[原始来源完整台账及其缺口状态](../data/h03_pre_correction_b9_source_availability.csv)。

## 3. 新的定量对照：2027—2029年B9b修订规模与整体峰值修订规模不同

PJM 2025/2026两个Forecast对相同目标年的RTO夏季峰值变动，来自[PJM 2026年1月14日官方历史对照](https://insidelines.pjm.com/pjms-updated-20-year-forecast-continues-to-see-significant-long-term-load-growth/)；B9b总关联负荷则使用**PJM2025原版XLSX**和**2026-01-13修改的独立B9b XLSX**同目标年值，保证来源分开。

| 目标年度 | 2025→2026 RTO整个夏季峰值预测变动 | 2025→2026 B9b总关联预测变动 | 两组修订绝对值的比值 |
|---|---:|---:|---:|
| 2027 | -3,735MW | -1,855MW | **49.665%** |
| 2028 | -4,414MW | -2,128MW | **48.210%** |
| 2029 | -4,564MW | -2,112MW | **46.275%** |
| 2030 | -875MW | **+1,765MW** | **201.714%（符号相反）** |

**不是贡献分解**：这个比例只是同目标年`abs(ΔB9b)/abs(ΔRTO夏季峰值)`的**规模对比**，在B9b与基础模型有嵌入重叠、EV/天气/经济/模型重估及其他大型负荷存在时，不能据此说“AI造成2027峰值下修49.7%”。2030反向说明整体模型仍可能下修而大型负荷总关联上修。该量不代表实现率或政策效应。

本轮同时说明为什么更合格的分解应优先采用PJM公布的官方水瀑图以及B9额外调整敏感性模型；没有修订前B9，不能强做精确分解。

[四行同目标年度对照CSV](../data/h03_rto_2025_2026_summer_vs_b9b_revision_magnitude.csv)和[标准库离线验算](../analysis/recompute_h03_pre_correction_source_gate.py)。

## 4. 对TOPIC-011研究的方法修订及下一步数据入口

研究的截止日期仍为**2026年11月14日**。H03/H08的政治因果**UNTESTED**。有证据的明确状态是：

1. **已证实**：2026独立B9b初期总关联数据、2/6更正后B9和当前combined之间的区别；旧EKPC导致8—10MW的来源差已解释；B9核心算法是剔除历史DC后的模型敏感性。
2. **已排除**：仅靠2026-01-14主PDF或2026-01-23模型PPT恢复“修订前B9精确值”的可能性；两者不是数字表源。
3. **仍不确定**：原始2026Jan B9发布时的字节及逐区/逐年数值，Feb6勘误真正改变了多少MW、哪些区受到影响，以及初始B9是否另有独立归档。
4. **未来检索最小验收标准**：真实PJM/第三方存档2026-02-06**之前**的B9 XLSX，明确下载URL/文件SHA/修改及首次获得时点，表头及各区域/年目标都能提取；需与现存订正版在**同一B9定义**下逐行相减。没有真实旧字节，就让`Feb6 correction_delta_MW = NA`，绝不代数倒推。
5. 新版业务机制还需要项目真实ESA/供电/计量用电。任何“政治导致AI建设延期”的结论仍不能由预测修订比率推出。

**本轮实际增量**是将“继续寻找文件”的模糊任务变成具有SHA、PDF存在性、原始发布时间、版本资格门槛和可复核数值比较的明确数据合同；停止在缺原版数据时不断臆测“纠错量”。
