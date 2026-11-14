# CASE-FRA-001｜M2：1788年圣多明各各金库与财政包税链审计（2026-11-14）

**唯一研究 Issue:** https://github.com/fweiger/AI_book/issues/35  
**沿用 Draft PR:** https://github.com/fweiger/AI_book/pull/39  
**目的：** 将圣多明各1788年地方金库账户、早期法国西印度税、1781年王室预算口径拆开，审查「殖民商品→当地财政→宗主国税收→军事维持成本」是否可归属或因果检验。

## 1. 本轮关键纠错：1781年410万里弗尔不是实际收到的年度税款

Jacques Necker 的1781年 *Compte rendu au roi* 原始说明写明：Ferme générale 为国王管理 Domaine d'Occident，**在和平时期**该项目约为 **4,100,000 livres tournois**。它是在**普通年度财政陈报中使用的和平时期预计收入**，不是已核验的1781年实收、不是1788年海关进口的一定比例、更不是整个殖民帝国的净收益。

原始说明（比单看汇总表更关键）：https://fr.wikisource.org/wiki/Compte_rendu_au_roi_par_M._Necker_ed._1781/%C3%89tat_raisonn%C3%A9_des_recettes_port%C3%A9es_au_Tr%C3%A9sor_royal  
历史证据状态：**PRIMARY_TEXT_VERIFIED / ESTIMATE_PEACETIME / ACTUAL_CASH_NOT_ACQUIRED**。

前轮 [财政桥报告](CASE_FRA_M1_M2_FISCAL_BRIDGE_20261114.md) 与 [证据表](fiscal_evidence_m1.csv) 已作增量修正，并保留历史更改轨迹。410万/263,784,000≈1.554%只反映当时表内两项陈报值的**形式比率**，非1781年法国全部税收或殖民收益占GDP。

## 2. 1788年圣多明各原书第XI表（N.º XI）：地方金库分账

**史料：** François Barbé de Marbois, *État des finances de Saint-Domingue*, Paris, Imprimerie royale, 1790, « N.º XI. Récapitulation générale des Recettes & Dépenses des diverses Caisses de la Colonie, pendant l'année 1788 ». 
- 原书扫描入口：https://archive.org/details/tatdesfinances01barb
- 原书扫描PDF（Wikimedia）：https://upload.wikimedia.org/wikipedia/commons/7/78/%C3%89tat_des_finances_de_Saint-Domingue%2C_-_contenant_le_r%C3%A9sum%C3%A9_des_recettes_%26_d%C3%A9penses_de_toutes_les_caisses_publiques%2C_depuis_le_1er._janvier_1788%2C_jusqu%27au_31_decembre_de_la_m%C3%AAm_%28IA_tatdesfinances01barb%29.pdf
- 可机器索引的PDF表格摘录与原始单位：见 [saint_domingue_1788_caisse_m2.csv](saint_domingue_1788_caisse_m2.csv)。

**验证状态的重要限制：** 本轮从公开扫描的**搜索索引抽取**了账表项目，但网页/PDF逐格视觉截图获取失败。不能声称完成原表图像的独立逐项视觉审计；因此条目均标记 **PDF_INDEX_TRANSCRIPTION_VISUAL_NOT_VERIFIED**，只有内部算术另外标记 ARITHMETIC_CHECK_PASS。必须在可以显示扫描页面的环境里对「l./s./d.」与标题二次核对。

### 海军金库（Caisse de la Marine）1788年的新增流水

| 账户行 | livres | sous | deniers | 类型 |
|---|---:|---:|---:|---|
| 当年普通收入 | 7,821,858 | 7 | 0 | 当年收入 |
| 当年特别收入 | 2,081,332 | 7 | 11 | 当年收入 |
| 当年普通支出 | 7,246,852 | 4 | 0 | 当年支付，含以前年度费用 |
| 当年特别支出 | 2,201,636 | 3 | 8 | 当年支付 |
| **上述两项收入−两项支出** | **454,702** | **7** | **3** | **算术差额，不是财政利润** |

换算规则：1 livre = 20 sous，1 sou = 12 deniers。由原表转录条目重算：收入合计 **9,903,190 l. 14 s. 11 d.**；支出合计 **9,448,488 l. 7 s. 8 d.**；差额 **454,702 l. 7 s. 3 d.**。当年普通支出文本明确含以前年度的款项；该差额也不证明对巴黎存在同额净汇款。

### 为什么不能把第XI表「收入合计=支出合计」当作盈亏为零？

第XI表检索转录显示「总收入」与「总支出」均列为 **13,444,854 l. 4 s. 5 d.**，但是它还将**期初未结清资金、保管金、期末现款与追索会计人员的资金**等用于账务平衡。比如海军金库期初未结资金 **933,160 l. 5 s. 5 d.** 并非1788年新增税收；存放金库（Caisse des Consignations）1788年120,000 livres保证/寄存款并非殖民地财政利润。不能直接取第XI表平衡后的数值作为「1788年度营业收入」或者「法国王室维持殖民地的成本」。

**OCR 索引质量异常**：索引中海军金库现金 **960,787 l.16 s.8 d.** 加会计人员追索款 **429,374 l.12 s.8 d.**，按 l/s/d 运算应为 **1,390,162 l.9 s.4 d.**，而同一索引展示的小计为 **1,390,162 l.16 s.4 d.**，相差 **7 sous**。不判断是原印刷笔误还是机器转录错误；须查看扫描图像核实，未解决前不可自动用于期末余额复算。

### 不能忽视的非商业化财政条目

同一原表记载 **Caisse des Libertés** 一项收入来源为1788年「297名被奴役者获得法律解放所缴纳的款项」，合计 **547,892 l. 10 s.**。这是奴隶制下征收的财政款项与社会制度记录；**不是人的经济价值，也不能当作一笔正常商品收入或据此估算任何人的市场价格**。该账户尚有其他收入和社会支出，不等于王室国库税收。

## 3. 财政包税制度的跨期线索（非可直接拼接的年度面板）

Marie-Laure Legay (2023), *Dictionnaire numérique de la Ferme générale*, « Domaine d'Occident »：https://fermege.meshs.fr/notice/120

| 年份/时期 | 证据中的金额（livres tournois） | 会计口径 | 严格含义 |
|---|---:|---|---|
| 1675 Oudiette合同 | 350,000 /年 | 包税合同定额 | 特许租约应付租金，不是实际征税总额 |
| 1685 Fauconnet | 500,000 /年 | 包税合同定额 | 合同口径，不能与货值相除算实际税率 |
| 1697 Guigues | 550,000 /年 | 包税合同定额 | 高战争风险阶段变更包税合同 |
| 1707 合同调整 | 420,000 /年 | 包税合同定额 | 西班牙王位继承战争中下调合同价 |
| **1716** | **2,445,954** | 群岛相关毛税收，含殖民地现场及法国本土 | 历史重建值，不含加拿大 |
| **1716** | **2,007,526** | 同批税收扣除记录费用后的净额 | 不是可核实的巴黎王室最终实际入库 |
| **1775** | **8,815,031** | 研究者估算的Domaine d'Occident对美洲贸易征税（不含另类的traites税） | 不能直接与1781年王室和平时期预算值比较 |
| **1781陈报** | **4,100,000** | 「和平时期」王室国库正常年度估计 | 非实际年度现金，不能与1775毛税收简单同比 |

1716年的 **毛净差额438,428 livres**（约毛额17.92%）是*该次历史重建核算*中列支费用的差额；不能泛化为整个法国税务机关的征管效率。1775年估值的档案线索为 **AN H¹ 1686**，以及 Legay 提到的 **AN G¹ 31, G¹ 82, G¹ 84** 等，尚未取得原始手稿全文。

**因果含义（设计，不是已证明）：** 同一「西印度税」标签可能在不同时期指：包税合同租金、征税机关毛收、扣费净收、王室普通预算估计；未经账户同一性检查，不能把这些数字拼出伪造的税收增长曲线。

## 4. 货币换算——法属圣多明各 livres coloniales ≠ 法国 livres tournois

研究：R. Richard (1954), « À propos de Saint-Domingue : la monnaie dans l'économie coloniale (1674–1803) », https://www.persee.fr/doc/outre_0399-1385_1954_num_41_142_1201。历史名义计价关系在18世纪中期已出现约 **1 livre tournois = 1.5 livres coloniales** 的安排；实际私人市场比价及交易媒介可能偏离官方记账关系。它不是现代汇率，也不是把所有殖民支出按不变比例换成王室钱款的依据。

**本轮统一原则：** 殖民地账册原值与王室账册原值各自保存；跨账户只允许在有确切来源的换算规则、币种定义、时期与税款归属时生成衍生字段。1788年octroi **6,924,167 livres coloniales** 仍为前轮转录、尚未在本轮通过原扫描逐项复核，保留 UNVERIFIED_PREVIOUS_ROUND。

## 5. 对原研究命题的增量约束

- 法国确实能够从殖民贸易征税，但**贸易货值、地方税收、包税毛额、包税净额、王室入库预算**不能互换。
- 圣多明各地方海军金库可以在1788年记录正的年度收支算术差额；这并不能证明法国国库获得净收入，也不能覆盖全球海军与海外战争成本。
- 将1789法国财政崩溃单因归结为「殖民地不赚钱」或「已无商业收益」都没有充分依据；政治组织、战争融资及海地革命等机制需独立检验。
- **1775征税估值高于1781和平时期王室预算估值，尚不构成税收断崖或财政挤出证据**，因为两笔数的收款主体、费用扣除、范围和年份不同。

## 6. 未通过与下一项唯一动作

| 项目 | 当前状态 |
|---|---|
| M2局部财政表的原始PDF索引数据 | ACQUIRED_INDEXED_NOT_VISUAL_VERIFIED |
| 1788海军金库年度收支的 l/s/d 加总 | ARITHMETIC_PASS |
| 第XI表「7 sous」余额冲突 | BLOCKED_PENDING_SCAN_VISUAL |
| 1788地区货币实际交易价 | NOT_ACQUIRED |
| 1716/1775包税史料的原始 AN 档案 | NOT_ACQUIRED（已定位档号） |
| 巴黎王室1781/1788实际收到Domaine d'Occident金额 | NOT_ACQUIRED |
| 海军共同成本归属与全殖民财政净收益 | NOT_ACQUIRED |
| 因果检验/回归 | NOT_RUN |

**唯一下一行动：** 对1790年Barbé de Marbois扫描PDF第XI表进行视觉逐格核查，校正期末余额7苏索引差异，分别合并各地金库年度新增现金收支与结转/保管资金，并寻找AN H¹ 1686及1780年代王室 Domaine d'Occident 真实入库表。

## 7. 同源回顾史料的存量/流量调节说明

[1788财政来源冲突与存量—流量审计](CASE_FRA_M2_STOCK_FLOW_RECONCILIATION_20261114.md) 根据Ardouin(1853)对Marbois的后期摘述，记录了收入约15m、支出约13m、应收款约9m存量及年底储备超1m。它并非1788年原始扫描的独立复核，且全殖民地方账与海军单一金库、新旧款及汇总平衡表口径未统一；另有180m与193m出口价值估计未调节。**7苏视觉核验继续 BLOCKED，不擅自修正。**
