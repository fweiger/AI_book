# CASE-NLD-001 | M2E 1992–1997史料冲突与重复费用的定量审计

日期：2026-11-14；规范Issue https://github.com/fweiger/AI_book/issues/33；继续原有Draft PR #37，未修改main。

## 取证层级
- 本轮直接重新打开并截图核对由F. S. Gaastra撰写的荷兰国家档案馆1992年《INTRODUCTION TO THE ARCHIVES OF THE VOC》英文导论，PDF第4页（0索引p3）：https://www.nationaalarchief.nl/sites/default/files/afbeeldingen/toegangen/NL-HaNA_1.04.02_introduction-VOC.pdf
- 直接截图核对同一位作者Gaastra (1997), *The Dutch East India Company: A Reluctant Discoverer*, *The Great Circle* 19(2), 印刷第111、112、113页（PDF索引p3/p4/p5），表1与表下注释：https://dutchaustralianculturalcentre.com.au/wp-content/uploads/2026/04/Gaastra-VOC-Australia-4155533235.pdf
- 官方NA Jacob van Ghesel 1.10.31档案目录印刷p10（PDF索引p9）再次截图核验，原第15号档案是1640—1770年六商会equipage、return收益记录；**只取得目录，未获取实物账页**：https://www.nationaalarchief.nl/onderzoeken/archief/1.10.31/download/pdf
- 1872年的《Kroniek》27卷仅有影像扫描，DBNL官方确认公版；49.56MB PDF实际点击出现HTTP400 `Content length is too large: 51971261`，故**NOT_ACQUIRED**并未复录第40—41页。检索网址：https://www.dbnl.org/tekst/_kro004187101_01/。没有合理基础宣称金额冲突已解决。

## 六项同一作者出版物比对——新增可机器复算结果
1992导论对1640—1700、1700—1795三个指标给出百万荷兰盾整数；1997表1对16个区间给出十分之一百万荷兰盾。根据各期间相加并以绝对最大通常四舍五入误差(1992整数近似±0.5百万，1997每行小数一位±0.05百万)进行敏感性审查。**误差界只代表常规舍入，不排除作者泛称‘约’或会计口径变化。**

| 期间及指标 | 1992档案导论 | 1997表1重加总 | 差额 | 单纯按表格精度四舍五入解释？ |
|---|---:|---:|---:|---|
| 1640-1700 equipage | 370.0 | 465.7 | +95.7 | 不能 (±0.8) |
| 1640-1700 imports | 205.0 | 207.0 | +2.0 | 不能 (±0.8) |
| 1640-1700 sales | 577.0 | 576.8 | -0.2 | 可能 (±0.8) |
| 1700-1795 equipage | 1608.0 | 1607.7 | -0.3 | 可能 (±1) |
| 1700-1795 imports | 667.0 | 679.9 | +12.9 | 不能 (±1) |
| 1700-1795 sales | 1633.0 | 1623.8 | -9.2 | 不能 (±1) |

单位：百万历史名义荷兰盾，来源重建而非VOC直接手写原账。

**核心量化判断：** 1640—1700 equipage差95.7百万盾，远大于六行加总与1992汇总的常规舍入界±0.8百万；1700—1795 imports差12.9百万、sales差-9.2百万，也远超十行舍入界±1.0百万。1640—1700销售576.8与577以及1700—1795 equipage1607.7与1608可由舍入解释。数据差异*不是*‘十年项浮点加总问题’。

比率465.7 / 370 = 1.258649，接近1.25轻币／重币关系但**不等于能证明换汇错误**：将465.7/1.25得到372.56，距370仍有2.56百万，超过通常0.8百万误差界；同列1700—1795汇总则几乎精确一致（1607.7 vs 1608），不能对两个世纪都用统一1.25倍率修正。更重要的是Gaastra表1 `equipage` 是荷兰六商会支出、非明确的亚洲轻币采购值。币制必须逐账页追踪后才能裁决。

详见 [voc_1992_1997_six_metric_reconciliation_m2e.csv](voc_1992_1997_six_metric_reconciliation_m2e.csv)，包含六行、原源URL、Δ、相对Δ与舍入容许界。

## 新的内部一致性检查：1997正文1770—1780 equipage '198' 可能串行
Gaastra 1997印刷p111写1770—1780投资约198百万盾、'赚'13百万盾；同篇印刷p112表1实际列1770—1780 equipage **186.5m**、sales **199.6m**，两数差**13.1m**，与正文'13m'一致，而**198.9m实际属于1760—1770**上一行。这是内部交叉验证支持p112表中1770—1780的186.5，而不是正文的约198；但并不证明底层原始VOC账册必然是186.5。应标注`LIKELY_PROSE_ROW_MISALIGNMENT`，不做默写修正。

## 防止融资成本重复计算：equipage并非狭义军费或运营费
1997表1印刷p112脚注明确指出equipage覆盖造船装备、送往亚洲的商品及贵金属、荷兰本土支付的工资以及**interest payments**等。研究中的`equipage + interest`若未经科目核对，会把已包含于equipage的利息重复计算。其组成还混有固定资产/营运资本等，不能当军政支出，亦不能用`Europe sales-equipage`命名为VOC利润或自由现金流。

在获得原账前严格采用：`VOC_cash_uses = equipage_components_at_source - internal_transfers - already_recorded_interest + separately_verified_extra_use`仅作为**账务桥接示意**，不填伪数字；所需字段包括期间、商会、原始记账币种、资本性支出、商品、现金、工资、债息、总额与是否被前项包含。

## 新的更近时期的战争负对照：1672
1997印刷p113明确记载，VOC经历了1672年共和国被英法和德国诸侯同时攻击期间的财务危机，后来仍保持公司经营。作者还称其与英国东印度公司在纺织品欧洲市场的竞争获得有利结果，至1702年总体财务健康。
因此1672作为1780年第四次英荷战争的**同一公司、跨战争的潜在负对照**，比1606年早期公司融资本身更接近，但时代差异（亚洲产品组合、财政国家和组织规模、市场竞争与债务期限）仍很大；**不是可直接放入回归的同质对照**。
另有1692—1702年亚洲账务名义损失约18百万盾，其中1696附近数据受前期会计更正影响，VOC整体到1702未破产；证明亚洲账面亏损不能在无桥接下等同公司整体经济亏损。四项历史案例已编排入 [voc_mechanism_negative_cases_m2e.csv](voc_mechanism_negative_cases_m2e.csv)，均保持`CAUSAL_TEST_NOT_RUN`。

## 不等期间长度：只做年度均值的描述性归一化
为防止把1790—1795五年与整十年的名义总额直接比较，新增 [voc_period_annualized_descriptive_m2e.csv](voc_period_annualized_descriptive_m2e.csv) 将1997表1的十年累计按10、末期五年累计按5相除，并明确`NOT_OBSERVED_ANNUAL_DATA`；绝不伪造每个自然年的金融时间序列。均值可比较名义量纲，但仍受物价、产品、航期及仓储时间影响。1780–1790十年包含战争与战后，不能单凭窗口差异推出战争ATE。

## QA与阻断状态
- Source PDF original printed table/narrative screenshot verification: `PASS`（仅出版物页，而非原始账簿）。
- Six source-window reconciliation rows, rounding thresholds, 16 window annual averages, and 4 evidence-bound negative cases: `PASS` subject to GitHub readback.
- 1640—1700 equipage 370m vs 465.7m source conflict: `OPEN`；1997正文'198m' vs表'186.5m'：`PUBLISHED_INTERNAL_INCONSISTENCY`。
- Van Ghesel inv15 raw ledger and 1872 Kroniek 40—41: `NOT_ACQUIRED / BLOCKED_WEB_CONTENT_LENGTH`。
- de Korte1984 original Appendix1/14, VOC 1.04.02 inv4596/4597 raw images, Huygens annual fiscal database: `NOT_ACQUIRED`。
- Independent historian review, group-level net P&L, 1780 event-study, country matched causality: `NOT_RUN`。
- **唯一下一步**：取得一份经过清晰标注的Van Ghesel inv15原页或1872第40—41页局部影像，并取得原de Korte附录1的统计定义；将六商会 equipage 项逐类核对再定案，不继续用不相容统计模拟VOC真实收益。
