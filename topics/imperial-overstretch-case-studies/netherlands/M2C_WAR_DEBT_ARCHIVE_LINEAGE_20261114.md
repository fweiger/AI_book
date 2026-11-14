# CASE-NLD-001 — M2C战争债务与原始账册来源链（2026-11-14）

唯一权威任务：https://github.com/fweiger/AI_book/issues/33 ；复用Draft PR #37，不合并main；M2尚未完成原始年度账册复算。

## 1. 新增可核查的战争债务估计
荷兰《新海事史》作者 Henk den Heijer, Han Jordaan, Karel Davids 在第2卷第3章1780—1784年战争章节，注146明确引用J.P. de Korte (1984)附录14。
来源：https://beta.nmgn.huygens.knaw.nl/nmgn2025/d2h3-de-tijd-van-de-grote-handelscompagnieen-koopvaardij-buiten-europa-in-de-zeventiende-en-achttiende-eeuw.html
- 战争开始时VOC债务超过2900万荷兰盾，结束时超过5100万荷兰盾；文字概括战时债务增加近2200万荷兰盾。
- “超过”的两个近似数不是精确端点，不可用51/29计算精确增长率；2200万是该来源报告的近似增量。
- 当前证据级别是学术二级转引，而非de Korte原始附录读数；后者仍未取得。公司债务不得改称荷兰国家债务。
- 同一研究注150说1788年承诺3100万荷兰盾信用额度，另有此前500万支持；授权/承诺额不等于当年实际拨款，不可误计为政府现金支出。
- 同一研究注148称战前精品香料占亚洲回航商品采购价值约3.1%，占荷兰销售回款约24%；两个比率的分母、地点不同，不是净毛利率或殖民投资回报。

## 2. 一个尚需解决的1760与1780数据比较问题
de Jong, Jonker和Röell (2013), Maandblad voor Accountancy en Bedrijfseconomie 87(5), 印刷页227，记录1760年VOC债务约3230万荷兰盾，主要为短期债务。
PDF：https://pure.rug.nl/ws/portalfiles/portal/82569222/De_ontwikkeling_van_de_naamloze_vennootschap_in_Nederland_tot_1850.pdf
该数值表面上大于1780年“超过2900万”的下界；但这不是1780年债务确切金额，且两篇文献会计科目和计量口径尚未并核。不得宣称1760至1780年债务单调上升或单调下降，更不能在不一致口径下拼接年度曲线。

## 3. 真正新增的原始档案目标：1.10.31 / inv. 15
荷兰国家档案官方库存《Jacob van Ghesel, 1.10.31》印刷第10页（PDF页10）的档案15号明确是：VOC全部商会船只1640—1770年的装备成本和回航收入名单；部分发表于1872年《Kroniek van het Historisch Genootschap》pp40–41。官方库存PDF：https://www.nationaalarchief.nl/onderzoeken/archief/1.10.31/download/pdf
这是对1640—1700年装备成本370m（1992档案导论）与465.7m（1997 Gaastra分期表加总）冲突的直接检索线索，优先级高于继续在没有科目定义的二手总表间猜测。
同档案的8号为1711和1756—1772年余额，9号为1638—1770年VOC荷兰本土财务汇总，16号为1736—1768年商品与价格，172号为1753—1768年亚洲财务状态。库存描述已读，但这些**原件或实录数据尚未读取**。
1872年刊物已在DBNL发现，扫描PDF约49.56MB，尝试打开返回HTTP429；目前是PUBLIC_DOMAIN_SCANS_LOCATED_NOT_READ，没有抄写pp40–41的任何金额。DBNL：https://www.dbnl.org/titels/titel.php?id=_kro004187101

## 4. 1780—1784战时原档路径及数字化阻断
既有VOC档案1.04.02 4596（1771—1780）和4597（1781—1790）确实包含六商会的年度汇总、债券及拍卖预支款。官方目录：https://www.nationaalarchief.nl/onderzoeken/archief/1.04.02/beschrijving/content_and_structure
NA官方技术文档还给出EAD XML中dao/METS链接、METS图像文件地址的替代路线：https://www.nationaalarchief.nl/onderzoeken/open-data/archiefinventarissen-digitale-objecten-en-scans-van-archieven
但本轮尝试XML返回不支持类型或下载失败，未获得上述两卷的METS UUID；此前扫描查看器地址HTTP404。不可把“数字化状态”写成“原账影像已阅读”。

## 5. 本阶段机制评价
| 命题 | 新证据 | 反证或未知 | 状态 |
|---|---|---|---|
| 1780战争显著加剧信用压力 | 学术研究转引de Korte称债务近增22m | 战前资金压力已存在，尚无可识别单年现金数据 | DESCRIPTIVE_SUPPORT |
| 战前债务持续上升 | 1760 32.3m；1780 >29m | 科目及下界不同，不可比较趋势 | UNIDENTIFIED |
| 亚洲军事治理费用是利润衰退主因 | 公司史叙述 | 未分项重建原始年度军政账 | NOT_RUN |
| 香料垄断带来高净利润 | 3.1%采购占比对照24%欧洲销售占比 | 不同分母，需扣强制治理和航运成本 | NOT_IDENTIFIED |
| f370m/f465.7m差异源于币制 | 旧M2有light/heavy币种风险 | 未取得Van Ghesel inv15及de Korte原始表注 | SOURCE_CONFLICT_OPEN |

## 验证状态和唯一下一步
- 二级学术资料、原始档案库存定位及来源层级：PASS_PARTIAL。
- de Korte(1984)附录14、1.10.31原账15、1.04.02账页4596/4597：NOT_ACQUIRED。
- DBNL 1872印刷表：NOT_READ_HTTP429。
- 财务因果模型及独立史学评审：NOT_RUN。
- **唯一下一项取证**：先取得1.10.31 inv.15或1872 Kroniek pp40–41的真实表格，检查1640—1700装备支出的计量主体和币制；同时通过正式EAD/METS查到VOC 4596/4597影像并核对1780战前与战后债务定义。
