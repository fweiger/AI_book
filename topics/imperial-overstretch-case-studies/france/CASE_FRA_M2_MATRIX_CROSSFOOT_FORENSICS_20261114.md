# CASE-FRA-001｜M2：1788商品税与外商贸易表“双向核账”取证（2026-11-14）

**权威任务：** https://github.com/fweiger/AI_book/issues/35  
**现有Draft PR：** https://github.com/fweiger/AI_book/pull/39  
**对象：** 1804年法国殖民外商贸易表与2005年历史论文中的1788出口重量表。  
**状态：** `DOUBLE_ENTRY_MATRIX_ARITHMETIC_PASS`，`SPARSE_OCR_REPAIR_HYPOTHESIS_NOT_VERIFIED`，`PRIMARY_PRINTED_IMAGE_NOT_READ`，`METROPOLITAN_CASH_NOT_ACQUIRED`，`CAUSAL_NOT_RUN`。未改写历史来源原值。

## 一、实证突破：1804年外商进口表的两轴差额可以同时定位

原文：*Statistique générale et particulière de la France et de ses colonies*, tableaux (1804), **État des importations faites aux colonies françaises d'Amérique par le commerce étranger en 1788**。来源PDF https://upload.wikimedia.org/wikipedia/commons/f/fa/Statistique_g%C3%A9n%C3%A9rale_et_particuli%C3%A8re_de_la_France_et_de_ses_colonies_..._%28IA_b2201763x%29.pdf 。本轮通过可搜索PDF索引文本读取全6×7国家—殖民地矩阵，PDF页面视觉截图再次失败。**原表币种页眉未核实**，所以本报告沿用“印刷值单位”，不与1788年殖民地里弗尔或法国本土法郎机械合并。

[42个交叉单元原样保存的CSV](atlas_1788_foreign_trade_matrix_raw_m2.csv)；[14条行列边际审计](atlas_1788_foreign_trade_margins_m2.csv)。

### 1. 先只核对原索引值，原表存在四个边际差额

| 边际 | OCR可见分项求和 | 列示总额 | 列示总额减分项求和 |
|---|---:|---:|---:|
| 瓜德罗普行 | 3,444,000 | 3,424,000 | **−20,000** |
| 多巴哥行 | 2,122,000 | 2,127,000 | **+5,000** |
| 丹麦商人列 | 192,000 | 172,000 | **−20,000** |
| 荷兰商人列 | 1,450,000 | 1,455,000 | **+5,000** |

其他列和行均能加总到已见的边际；已列全部原始表格非空单元合计 **23,679,000**，但作者印刷的行合计总和、列合计总和以及grand total均为 **23,664,000**；差 **−15,000**。对于表格破折号/空值，复算只累计可见非空项，**不将空格自动当成经审计的零**。

### 2. 两格最小稀疏修正假说

如果假设**全部边际总数正确，且尽可能少改变单元格**，那么：
- 瓜德罗普×丹麦商人：原数字化索引 **56,000** → 候选 **36,000**（减少20,000）；
- 多巴哥×荷兰商人：原索引 **53,000** → 候选 **58,000**（增加5,000）。

这两个交叉点恰好分别处在**同幅度异号的行/列残差交点**。将它们作为非破坏性的候选值后，**全部6个岛屿行合计、7个国别列合计及总额23,664,000都严格闭合**，可检查 [候选修复证据](atlas_1788_two_cell_candidates_m2.csv)。

**方法严格边界：** `mathematical_candidate != historical_value_verified`。这并不能证明原书一定是36,000和58,000；错误也可能在印刷的某个边际，或有多格OCR/排版混合误读。只有高清印刷页逐格复核后，才能把这两个候选升级为验证读数。原始`atlas_1788_foreign_trade_matrix_raw_m2.csv`完全不被改写。

**不会受这两格候选影响的观察：** Saint-Domingue本行已列六项进口金额合计仍为7,038,000，其中美国5,922,000，即**84.14%**仅为该行的外商进口来源份额，绝非美国占圣多明多全部商品进口的比例。葡萄牙空格仍保留`NOT_REPORTED_DASH`而不是确认为0。

## 二、2005年Manuel出口重量统计：新发现并非只有税额冲突

Keith Anthony Manuel, *Slavery, Coffee, and Family in a Frontier Society: Jérémie and Its Hinterland, 1780–1789* (University of Florida MA thesis, 2005), printed **p.25, Table 2-4**, https://ufdcimages.uflib.ufl.edu/UF/E0/01/16/50/00001/manuel_k.pdf。论文原PDF的搜索提取文本可核对数字，但页截图无法获取。表注说明**出口物量以千磅**、`customs duties`以**千殖民地里弗尔**列报。

按PDF搜索表格列出的五个产品数值（为避免OCR错位，CSV仅按`product_1..5`列标记，**尚不擅自固定法文商品的真实列标题**）：

| 对象 | 五商品加总（千磅） | 原表重量总额（千磅） | 残差（总额减加总） |
|---|---:|---:|---:|
| 北部 | 91,196 | 91,196 | 0 |
| 西部 | 110,377 | 110,377 | 0 |
| 南部 | 38,244 | 39,279 | **+1,035** |
| 全殖民地 | 239,817 | 240,852 | **+1,035** |
| Jérémie港 | 5,138 | 6,212 | **+1,074** |

**双轴验证：** 北/西/南三个地区在每一个单独商品列的纵向加总，都恰好等于殖民地该商品列；同时，三个地区的**列示重量总额**也恰好等于殖民地总重量。唯独南部商品项目横加不等于地区总重量，使全殖民地横加也出现同样的1,035缺口。Jérémie的1,074是另一行级异常，**不能直接认定与1,035同源**。

这可以由PDF数字解析遗漏商品分项、错误合并列标题、个别数字错读或原论文表格印误造成，但在拿到p.25原页图像前不能判定。原论文数据没有因此推导出真实贸易量下降，更不能把1,035千磅自动定义为未登记的走私量。

相关[逐行原样读取与复算CSV](manuel_1788_weight_crossfoot_m2.csv)。

## 三、与既有法国财政研究的边界

- **同一历史年度**不能保证同一科目：Manuel地区出口商品税6,917,000殖民里弗尔与Marbois地方`octroi`6,924,167 l19s11d的差7,167 l19s11d继续保留为**税种/范围未核同口径**，不能称财政损失。
- **外商贸易总额**不能与法国本土TOFLIT18的所有殖民贸易金额直接比较，且1804汇编单元币种仍未通过原页确认。
- **数学修复**不能替代历史来源验证；后续可以在审计版单独计算`hypothesis_adjusted`，但原始档案数值始终应可追溯。
- **帝国财政因果假说**仍需1788年法国本土`AN G¹46*/44*`实际税收到账、跨洋汇票最终支付、海军成本分摊及可比较年度材料。当前`NOT_ACQUIRED/NOT_RUN`。

## 四、唯一下一项工作

**对原页做最小范围核查：** 1804年外商进口表的「Guadeloupe×Danois」和「Tabago×Hollandais」两格，以及Manuel p.25「Sud地区、Colony total、Jérémie」全部商品列及重量总计；给原页扫描/图像位置、逐格截图、抄录双人复核状态。若图像不可得，则保留候选假设，不得自动改写历史账。

检验通过后再回到王室财政收款凭据，不在跨来源口径未解决时估算殖民帝国的净利润或财政回报率。
