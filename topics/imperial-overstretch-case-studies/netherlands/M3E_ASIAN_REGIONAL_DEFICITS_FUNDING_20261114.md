# CASE-NLD-001 | M3E 亚洲财务赤字与董事会跨洋资金渠道 — 2026-11-14

权威研究任务：[AI_book #33](https://github.com/fweiger/AI_book/issues/33)；唯一既有[Draft PR #37](https://github.com/fweiger/AI_book/pull/37)。本轮取得两组**已出版的历史财务重建**，并非原始18世纪公司现金账页。状态`PUBLISHED_FINANCIAL_RECONSTRUCTION_REPRODUCED` / `ORIGINAL_LEDGER_NOT_ACQUIRED` / `CAUSAL_MODEL_NOT_RUN`。

## 1. Huygens 2025的新轴：VOC亚洲业务真实分期收入／支出，而非欧洲sale−equipage
研究作者Henk den Heijer、Han Jordaan、Karel Davids，*Nieuwe Maritieme Geschiedenis van Nederland* II.3, **Tabel 1 'De financiële resultaten van de VOC in Azië in guldens (1621–1790)'**： https://beta.nmgn.huygens.knaw.nl/nmgn2025/d2h3-de-tijd-van-de-grote-handelscompagnieen-koopvaardij-buiten-europa-in-de-zeventiende-en-achttiende-eeuw.html

将全部17期出版数值逐项保存为[voc_asian_regional_financial_results_m3e.csv](voc_asian_regional_financial_results_m3e.csv)，单位**百万荷兰盾历史名义值**，分期长度不等（8、10、12年）。17行`income-expenses`与原表profit/loss在公布精度0.1m下**全匹配**。这是**亚洲公司商站的整体收支平衡／局部经济结果**，不等于VOC合并净利润、不等于本土Heren XVII的现金余额、不等于荷兰共和国国库收益，更不能把公司亚洲亏损直接称作殖民军事成本。

| 历史分期 | 收入百万盾 | 支出百万盾 | 亚洲盈亏百万盾 | 时间长度（仅根据区间标签推算） | 每标签年的亏损百万盾（描述性） |
|---|---:|---:|---:|---:|---:|
| 1661–1670 | 57.9 | 41.5 | +16.4 | 10 | — |
| 1689–1700 | 58.7 | 69.0 | -10.3 | 12 | 0.858 |
| 1731–1740 | 54.2 | 74.9 | -20.7 | 10 | 2.070 |
| 1741–1750 | 70.0 | 81.8 | -11.8 | 10 | 1.180 |
| 1769–1780 | 58.4 | 88.5 | -30.1 | 12 | 2.508 |
| 1781–1790 | 50.0 | 100.4 | -50.4 | 10 | 5.040 |

**可证伪结论边界：** 亚洲负利润早在1689–1700出版分期便已出现；其后至1781–1790的各分期均为负，**因此“1780年英荷战争首次造成VOC亚洲亏损”在这组重建数据中不成立**。1769–1780合计赤字30.1m，1781–1790合计50.4m，按标签暗示年数简单除以12与10，年度均值亏损分别2.5083m及5.0400m，约后者/前者=2.0093倍。**这不是逐年观察，不是战争ATE**；前期包含1780年且具体巴达维亚会计年界限未在原始账页确认，后期包含战争后；缺少价格通胀、所有账务科目调整和未观察年份结构。

Huygens历史叙述进一步区分：亚洲当地贸易收入、从爪哇／锡兰征收的税与通行费、军政费用；亚洲领土扩张同时推升征税能力和军事行政开销、英方竞争和私人贸易又挤压传统商贸收益。**总的亚洲收入/支出无法直接识别军费占比或殖民税净利润，仍需BGB原始每商站账目**。

## 2. Gaastra 1976最早发表的20期董事会贵金属运输决定、16期汇票分配量
Femme S. Gaastra(1976), *Geld tegen goederen. Een structurele verandering in het Nederlands-Aziatisch handelsverkeer*, *Bijdragen en Mededelingen betreffende de Geschiedenis der Nederlanden* 91，DBNL直接可读出版全文、Table II（pp253–254）及Table IV（p259）与关键脚注13、17、26、29、30： https://www.dbnl.org/tekst/_bij005197601_01/_bij005197601_01_0018.php

- [voc_specie_director_resolution_allocations_m3e.csv](voc_specie_director_resolution_allocations_m3e.csv)：20期向亚洲配置贵金属、以**荷兰本土购入价、荷兰币面标准**计价，金额原表四舍五入至千盾。**脚注13声明数据依据Heren XVII的季节船队派遣决议，属于‘应随船发运的贵金属额度’**；在没有原始船货到港核查时不能当成`ACTUALLY_SHIPPED_ARRIVED_CASH`。1623年前realen按48 stuivers兑算，轻币加价不应在这份已经使用荷兰币面的表内再次乘1.25。作者注明部分1750年后相关统计尚在处理中/有不确定性。
- [voc_assignation_resolutions_m3e.csv](voc_assignation_resolutions_m3e.csv)：16期由Heren XVII分配给六商会的`assignaties`预期兑付/分配额，按千盾舍入；**不是已付现金、外部融资存量，也不是本国税款**。1976脚注30详述1640–60由阿姆斯特丹商会约一半的分配额估算、1660后Hope收藏和董事会决议、1758后董事会决议复核，且**包括好望角汇票**。过去文献对1750–60记23.619m或26.262m存在另一笔作者明确指出的统计冲突，不要把换用来源表格当成真实资产变动。
- 1770–80与1780–90，Table II决议贵金属配额**47.726m→48.042m**，仅变动约0.662%；Table IV公司分配`assignaties`额度**35.878m→40.015m**，+ 11.531%。这些与亚洲赤字两个不相同定义、非完全同会计年区间的系列**绝对不能相减定义跨海资金缺口**，更不能证明1781–90实际货币流抵达数额。
- 1976文章直接记录1760年VOC为了减少集中向阿姆斯特丹Wisselbank提取现金造成的市场压力，改变`assignaties`兑付安排：**三分之二在秋季商品拍卖后、三分之一在春季商品拍卖后**。这表明拍卖—信用付款时点联系在1780大战前已经存在；M3D的1792 Cohen拍卖保底是同一资金链受冲击后的制度应对，但不能证明1792单项合同有效或必然造成破产。
- 该文还指出1785–86年VOC试图把部分汇票支付期限延长30个月，或改为战争结束三年后才付款；属于融资**提议或制度措施**，不是‘成功偿还’。

## 3. 对二次转载资料的查错，避免伪造“独立印证”
[voc_asian_finance_secondary_transcription_errors_m3e.csv](voc_asian_finance_secondary_transcription_errors_m3e.csv)：Dagomar Degroot (2009) course report *The Weather Gage*, Appendix 11 Table18（https://www.pastmasters.org.au/uploads/2/6/7/5/26751978/voc_wesel_etc_logs.pdf）也是从Gaastra与de Korte历史重建二次转载：
1. **1661–1670亚洲盈利**：2009文为16.3m，Huygens 2025为**16.4m**；由57.9−41.5=16.4直接核验。
2. **1741–1750亚洲亏损**：2009文为11.0m，Huygens为**11.8m**；81.8−70.0=11.8。
3. **末行期间标签**：2009文为`1780–1790`，Huygens为`1781–1790`；数据表既不能据此认定有11个自然年，也不能把'1780–1790'作为1780年战前当期亏损。

**真实复核层级**：2009 PDF的Web文字提取确认Table18，但截图接口返回`cache miss`，故不能声称逐页视觉复核；Huygens官方网页表格由web抓取直接确认，且17项收入−支出全通过精确0.1m算术。Huygens 2025与2009共享Gaastra/De Korte学术来源链（但具体拷贝路径未独立证明），不当作彼此独立的两份VOC原账。de Korte原始附录10/14和BGB相关原始账页依然`NOT_ACQUIRED`。

## 4. 现金链的新可检验思路
亚洲商站收支赤字(运营成本/税/贸易) → 公司欧洲总部为亚洲配置贵金属（董事会决议） + 亚洲私人汇款/汇票到欧洲支付责任（assignation） → 欧洲拍卖收入与实际银行清算期差异 → 到期短债再融资/政府担保 → 1792拍卖保底措施与1793定向财政支持。

**新增设计H8**：在同一货币标准、账务分区和会计年之下，检验`Asian_net_account_result`是否领先于`company_authorized_specie_dispatch`、`assignations_facevalue_due`及欧洲实收款项，而不是直接对跨时期公布的十年合计作回归。作为负对照，晚17世纪的亚洲赤字长期存在但集团继续经营，说明**亚洲亏损本身并不足以导致公司立即解体**；需检验银行信用成熟期限、商品销售价格、战时回航、政府兜底的变化。

## 5. QA，阻断和唯一下一项工作
- Huygens 17期亚洲收支表：`REPRODUCED_FROM_PUBLISHED_TABLE`、`ARITHMETIC_17_OF_17_PASS`、`NOT_PRIMARY_LEDGER`。
- Gaastra 1976论文两项原始学术发表数值序列20期和16期：`PUBLISHED_AUTHOR_SOURCE_READ`、`POLICY_APPROVAL_NOT_PAYOUT`；与1792–94拍卖真实现金账尚不可联结。
- 2009课程研究转录3处差异：`SECONDARY_TRANSCRIPTION_DISCREPANCY_RECORDED`，不是学术原书历史账目真伪裁决。
- **没有**读取1780前后BGB原始现金日记账、de Korte实际期末利润帐、Cohen私商实付票据、荷兰省政府现金提款、历史独立史学专家意见：`NOT_ACQUIRED`、`NOT_RUN`。
- **唯一下一项**：优先取得VOC私商`assignaties`历史到期与实付列（特别是1760拍卖后清算、1780战争后追索）、和`3.02.33/25/3`协议对应的1792–94实际拍卖到账及服务费票据；将17期亚洲原始财务账本的年限/币种重建与Gaastra（1976）基于董事会决议重建的贵金属配额序列连接，先做同年定义与存流审计，而不是进行没有数据的回归。
