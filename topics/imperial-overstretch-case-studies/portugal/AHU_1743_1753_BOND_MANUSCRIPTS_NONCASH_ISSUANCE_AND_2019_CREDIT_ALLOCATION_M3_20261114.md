# CASE-PRT-001｜M3 1743—1753王室债券原始档案定位、非现金发行反例及1775后债权市场分层审计

> 2026-11-14；唯一权威业务 Issue [AI_book #34](https://github.com/fweiger/AI_book/issues/34)；沿用[Draft PR #38](https://github.com/fweiger/AI_book/pull/38)与现有分支。  
> 本轮状态：**9_ARCHIVAL_LOCATORS_REGISTERED / TWO_OFFICIAL_NONCASH_BOND_CONSIDERATIONS_CATALOGUED / 2019_PRIMARY_SECONDARY_ACCOUNTING_REPRODUCED / 15_656_000_REIS_INTERTABLE_GAP_OPEN / ORIGINAL_MANUSCRIPTS_NOT_ACQUIRED / CAUSAL_IDENTIFICATION_NOT_RUN**。

## 1. 研究问题：1743年国家发行净增加 ≠ 皇室新获得可自由支配现金

前轮DEBT.PT A原始年度工作簿(1641—1800)中1743年`juros`长期净发行`+507.943005`百万réis、总债务存量净增`+492.843005`百万réis。后继文献中约5000百万réis债权转移至Sé Patriarcal，涉及1743年6.25%票息债改5%，属于不同的**债券所有人/息票置换**。两者不可相加，也不能由净发行推回当年国库的新增现金收款。

2024年 Costa/Miranda/Nogues-Marco 著作与1947年 Azevedo (原书印页375)都引用1743-02-04法令及宗主教座堂—`Junta dos Três Estados`转款；但法令原件、1752年`Colecção Pombalina, cód.459, f.130`尚**未取得**，不能把多位后继作者重复援引Azevedo当作多套独立档案证据。

**本轮从“文献引用”升级为“档案精确定位+明确的非现金替代案例”**，但未假装看过未下载的档案原件。

## 2. 官方档案馆目录提供的两组核心原始账簿

已登记 [archival_locator_juro_cash_financing_1743_1753_m3.csv](data_m2/archival_locator_juro_cash_financing_1743_1753_m3.csv)，共九条，均含唯一ID、托管机构、真实年代、馆藏号、公开目录URL、史料证据等级、原稿是否取得和用途限制。

**AHU 2003（1743—1753）**：
- `AHU_CU_PADRÕES DE JURO, Cod. 2003`，海外事务委员会(`Conselho Ultramarino`)的债券登记簿；现存公开的*官方目录转录*说明其收入为债券抵押税源，同时与`Real Fábrica da Santa Igreja Patriarcal`支付命令有关。目录行称一卷、51叶，其中14叶空白；亦标该卷**有缺页**，但当前第三方转录将缺失叶号的终点渲染为无法识别链接，不能自行指定缺失页范围。
- 官方旧目录原始发布地址：[actd.iict.pt catalogue PDF](https://actd.iict.pt/eserv/actd:CUF006a001/AHU-CatalogoGeralCodices.pdf)；目前网页工具报cache miss，远程研究环境访问报SSL EOF；本次只能核查[该目录的可检索文字镜像](https://pt.scribd.com/document/415239932/AHU-CatalogoGeralCodices-pdf)。**这是档案元数据，不是1743年逐债券手稿的真实读取**。
- 下一步是调阅手稿页的`padrão`号、金库、票息、债权人和`conhecimento`/支付凭证，对1743年净发行进行现金与换券分解；缺页引起的*missing not at random*风险要记录。

**AHU 491（1742—1752）**：
- `AHU_CU_CONHECIMENTOS DOS JUROS DA ÍNDIA, Cod. 491`，同一目录将其描述为向**王国与印度据点商人**借入生息资金以支付**Estado da Índia战争开支**的登记簿。
- 这是葡萄牙帝国的`海外军事费用 ↔ 商人融资 ↔ 公共债务`非常直接的原始档案定位；但**仅有目录，不存在本项目可验证的战争借款总额、现金收款或偿还率**，不得据此发表不存在的军事预算年度面板。
- 两卷不是同一账，不能把印地战争借款一律归于巴西黄金税收抵押。所引用的目录信息均属`CATALOG_ONLY / PRIMARY_MANUSCRIPTS_NOT_ACQUIRED`。

## 3. 巴西国家图书馆官方公开档案清单：债券用于非现金权利补偿的两个案例

**可核对的元数据来源是巴西国家图书馆（Fundação Biblioteca Nacional）公布的AHU Project Resgate清单**，不是第三方博客：
[Documentos do Brasil na Série Reino — AHU](https://www.gov.br/bn/pt-br/central-de-conteudos/projeto-resgate/novos-instrumentos-de-pesquisa/documentos-do-brasil-na-serie-reino-ahu)。

| 文书日期 | AHU精确馆藏号 | 官方目录中债券的法律功能 | 证据限制 |
|---|---|---|---|
| **1744-08-29** | **AHU_CU_Reino, Cx.125, pasta 32**，清单编号635 | D. João V王室法令副本记载：发行面额**70,000 cruzados、票息5%**的一项`padrão de juro`，作为与**印度殖民官职相关的债权/权利转让**补偿；说明某些债券由非现金请求权置换形成 | 70,000单位是**cruzados**，不能直接与DEBT.PT的**réis**相加；原始副本未查看 |
| **1753-06-14** | **AHU_CU_Reino, Cx.60, pasta 65**，清单编号466；并参见`AHU_ACL_CU_003, Cx.13, D.1158` | 王室与Francisco de Albuquerque Coelho de Carvalho交换**马拉尼昂Cumã、Cametá地方辖治权**，对价包括一份`padrão de juro`、王室财产某项终身权利以及Outil领地权 | 明确是**混合非现金交换对价**，不能将整份合约视作债券换取新增国库现金 |

此外官方清单**1743-11-07** `AHU_CU_Reino Cx.125 pasta 30`记录`Junta dos Três Estados`秘书与`Conselho Ultramarino`秘书就里约一项官职估价的行政往来。**仅证明机构联系，不是债券支付证据**。

这些案例与1743年的操作在历史时段上相近，能**反驳“所有发行都等于新现金借款”的通用分类规则**；但**不能证明1743年507.943百万réis净发行有多少属于非现金补偿**。这是明确的外推边界。

## 4. 其它一手档案检索线路

1. 葡萄牙历史财政档案`oai:badigital.sgmf.pt:ARQ/682226`：`Listagem com juros reais desde 1406 a 1754`，葡萄牙国家档案门户条目标注该表包含各券的设立依据、授权法令、利率及支付方式。**目录已找到，原表图像未取得**。来源：[国家档案聚合检索](https://portal.arquivos.pt/search?archive.id=SGMF&image=true&page=114&timestamp=1654889568613)。
2. 葡萄牙 Torre do Tombo 官方馆藏书目[公共债券史及法律文献PDF](https://antt.dglab.gov.pt/wp-content/uploads/sites/17/2008/10/Junta-de-Credito-P%C3%BAblico.pdf)，确定1883年`Collecção de leis da dívida pública portugueza`第I卷**馆藏索书号SV94/96、SV1235/96**；但 **1743法令p317与1749转换p318的印刷页未取得**。
3. **史料日期冲突仍开放**：Azevedo (1947 p375)把第二份转换公告写作`Edital 16 Março 1749`，而当代的1841年《O Panorama》[原始期刊文字](https://hemerotecadigital.cm-lisboa.pt/obras/opanorama/1841/N210/N210_master/N210.pdf)提`16 Março 1750`。不能单凭二次引用宣称作者有错；优先查Gomes1883 p318原文以及对应实际法规公布日。
4. 里斯本慈善会[AHSCMLSB GF/RC/03/001](https://arquivohistorico.scml.pt/index.php/livro-de-registo-da-cobranca-de-padroes-de-juro-reais-da-nova-administracao)：**1767—1776**年真实债券收款/欠息记录的官方档案目录，可作为后来`已指定税源 → 实际收款、欠款`的单券级核查路径，**时间不覆盖1743，不能直接证明1743实际偿付**。

## 5. 独立作者证据：慈善会在1775年后如何将钱投向公共债券（2019）

Lisbeth Rodrigues (2019)，[*Os padrões de juro da Misericórdia de Lisboa, 1767–1797*](https://doi.org/10.4000/lerhistoria.4730)，`Ler História` 74:137–160，**在线原文及Table4/Table5已阅读核对**。在线文章明确许可**CC BY-NC 4.0**；本仓库只保留数据源引用、有限日期-本金摘要与原创派生统计及程序，不镜像原论文PDF或包含原表全部文字。

2019研究的现金/债务投资概念与1743机制高度相关，同时**不是Costa/Miranda/Nogues-Marco一组作者的同一稿件版本**：

- 1775-01-31王室`alvará`禁止**里斯本Misericórdia慈善会**以利息向私人放贷；但先前**1768已有规制，且其新增私人放贷在1769后已基本停止**，加之私人贷款高违约率及1755大地震，严禁把1775当作无混杂的自然实验。
- 作者Table5列**20笔**债券购买或过户记录，其中**一笔本金显示横线缺失**，不能记0。其余19笔已知本金由本项目有限原表数值转录算得 **179,853,941 réis =179.853941 contos**。
- 其中**5笔注明资金直接交入国库用于偿还旧债权人**，本金合计**106,773,748 réis =106.773748 contos**，占已知19笔本金**59.366922%**；另有**15笔私人二级市场交易，其中14笔本金已知合计73,080,193 réis**。
- **1790**两笔直接国库转款加总**84,814,724 réis**；它们是替代王室旧债持有人的融资/再融资，不应未经国库净额核算就说增加相同金额的国债余额。
- 作者另一张Table4的**财政年投资总额**为**195,509,941 réis =195.509941 contos**。`Table4Total - Table5Known=15,656,000 réis`，**目前无法对平**。前述59.37%以Table5金额已知记录之和作分母；若用Table4发布总额分母，同一五笔国库转款占比为**54.612951%**。
- 作者Table4依据慈善会月度金库账`AHSCMLSB GF/AC/02/lv001-03`，Table5依据`AHSCMLSB CT/09/01/lv004`的契据登记，**源账类型不同、登记金额与时点也可能有区别**。目前不可认定15.656m差额完全来自Table5其中唯一破折号本金，也不可写作学术作者的必然算错。
- 文内另报告1766–67持有216张债券、18世纪末持有358张债券，这两数是**特定时间存量**；20笔是期间购买流量，既不能直接加到216，也不能用两张快照的差额代替20笔。

独立数据：[misericordia_2019_bond_primary_secondary_reconciliation_m3.csv](data_m2/misericordia_2019_bond_primary_secondary_reconciliation_m3.csv)，真实运行的复算代码：[reproduce_juro_primary_secondary_2019_m3.py](data_m2/reproduce_juro_primary_secondary_2019_m3.py)。代码仅含文章Table5的**日期、名义金额及国库直购/私人交易分组**，不复制原论文全文或历史个人的详细数据。程序可验证20笔中19笔金额、5笔国库、15笔二级、1790两笔84.814724m及15.656m未对平值；**对公开出版数值的算术PASS ≠ 原档案重审或计量因果PASS**。

### 研究解释：财富流向机制比单纯债务存量更加可证伪

`私人信用市场 ──禁贷/违约/风险偏好──> 慈善法人资金 ──购买新债/赎旧债/二手券──> 王室税源抵押债券 ──> 国库实际新现金?`

从制度上可能产生两种相反效果：
- 王室利用高信用机构替换旧债权人，**降低再融资成本/改善债券持有人结构**；
- 原本可用于私人生产信贷的资金转入债券资产，产生**民间信用挤出**。但如果私人贷款在1775前已停止、且违约导致借款供给难以持续，所谓挤出的实际反事实规模可能很小。

这属于**机制设计与历史观察**，而非验证因果。今后若比较其他葡萄牙慈善会1775前后的各类贷款及债券购买，必须审查`1755地震→档案损失`、`1768先行规定`、`1769已无新私人贷款`、`本地违约与宗主国风险`；没有对照机构和充分预趋势，不应报告处理效应系数。

## 6. 实跑与文件验证状态

新增来源登记[archival_locator_juro_cash_financing_1743_1753_m3.csv](data_m2/archival_locator_juro_cash_financing_1743_1753_m3.csv)（9条）；标准库源分层审计[validate_archival_locator_and_cash_claims_m3.py](data_m2/validate_archival_locator_and_cash_claims_m3.py)从当前GitHub分支直接下载CSV重新执行**PASS**：9个来源唯一、有合法日期与来源URL、所有`original_record_status=NOT_ACQUIRED`，不冒称已查看档案手稿。原始档案目录全文官方直链遭遇访问错误时，保存真实的镜像及访问状态，不编造可达扫描图像。

2019资金分层实跑脚本`reproduce_juro_primary_secondary_2019_m3.py`从当前GitHub分支下载在研究Runner执行**EXIT0 / PASS**，新表派生CSV SHA256 **`9aa0202054679039f4fadd783b4c67ad2037589e910928ae02d7683b27ba5236`**；19已知本金求和、五笔国库直购、两笔1790国库转款、Table4已发表总额与未对平值均通过算术检查。

**仍未验证**：AHU2003和491手稿、Gomes1883 p317–318法令原文、1752 Pombalina 459 f130原件、1775该政策对私人融资的因果净挤出、1743是否有来自黄金税的某笔新现金、ICPSR 198143财力模型与ICPSR 209481黄金ASCM（均`NOT_ACQUIRED/NOT_RUN`）。1748债务/GDP发表**9%**与已锁定数据**8.152251%**来源冲突仍OPEN。不得基于本轮单独宣称葡萄牙帝国衰落原因已被唯一证明。

## 7. 下一项独立可验证目标

**优先向AHU取得`Cod.2003`可见页（缺页说明同时取证），逐笔关联1743—1753年债券出票、已抵押海外税项、宗主教座堂支付及是否有新现金；同时调阅`Cod.491`核实印度战争商人融资，与巴西黄金税抵押分开。** 对2019慈善会样本，直接用AHSCMLSB`GF/AC/02/lv001-03`金库流水与`CT/09/01/lv004`契据账查明15,656,000 réis差额究竟是破折号所藏交易、额外未上市记录还是财政年错位。原分支继续Draft，不改变main。
