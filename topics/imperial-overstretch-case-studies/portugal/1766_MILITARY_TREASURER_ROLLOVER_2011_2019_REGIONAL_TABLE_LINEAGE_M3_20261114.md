# CASE-PRT-001｜1766年军费旧账转入损益与1765年税源表2011—2019跨版本继承问题（M3）

> 2026-11-14。权威业务Issue：[AI_book #34](https://github.com/fweiger/AI_book/issues/34)；现有[Draft PR #38](https://github.com/fweiger/AI_book/pull/38)。本研究核验的是作者公开发表论文的文字、数据和所引档案定位，**未直接取得AHTC原始会计手稿**；财政黄金与军事现金流的因果识别仍未执行。

## 1. 真实核验的公开学术来源

- Manuel José Benavente Rodrigues (2011), ISCTE硕士论文：[学校PDF](https://repositorio.iscte-iul.pt/bitstream/10071/4540/1/Tese%20Manuel%20Jos%C3%A9%20Benavente%20Rodrigues.pdf)；156页，21,217,438 bytes，SHA256 533d24ceb52b53a4e8994f1a72739b04feb36f162304a3f28c13173f6bd7b3e5。**Table 3.31/3.32，PDF第99/100页，正文第91/92页**。
- 同一作者Rodrigues (2019), ISCTE博士论文：[学校PDF](https://repositorio.iscte-iul.pt/bitstream/10071/19808/1/PhD_Manuel_Benavente_Rodrigues.pdf)；339页，17,464,337 bytes，SHA256 ca8b83728950b1746440baad2ac522b9dd5010f4237ebb5a8a6e3b6c528b565e。**Table 4.5 PDF第109页/正文97页、Livro 537财务官结转PDF第99页/正文87页、Table 5.9/5.11 PDF第152/154页**。两版属于同一研究者修订链，绝非彼此独立的原始数据。
- 外部行政制度佐证：[Arquivo Histórico Militar 档案元数据 PT/AHM/FG/5/J1](https://ahm-exercito.defesa.gov.pt/details?id=41254)：列1763年7月9日撤销旧军事审计机构Vedorias和Contadorias da Guerra，改设Tesourarias Gerais das Tropas直接向王室国库交账。其8本馆藏手稿未被本项目调阅。

## 2. 1765年70,000 réis地区收入归类残差不是2019新错误

2011论文Table 3.31、3.32与2019论文Table 5.9、5.11两版打印的四个地区数据**完全相同**：

| 地区 | 征收所在地收入（réis） | 商品来源地重分类（réis） |
|---|---:|---:|
| Corte e Estremadura | 2,583,307,266 | 810,285,413 |
| Reino e Ilhas | 1,149,449,290 | 1,143,901,917 |
| Rio Janeiro、东非及亚洲 | 656,340,260 | 924,921,442 |
| 西非、Maranhão、Bahia | 38,095,805 | 1,548,013,849 |
| **四行合计** | **4,427,192,621** | **4,427,122,621** |
| **两版原文所印总计** | **4,427,192,621** | **4,427,192,621** |

**原产地重分类表残差70,000 réis＝0.07 contos，2011和2019两版均存在。** 对应行是否错印、手工重分类差额、附表漏项或底层数据原因仍无法辨识；不能擅自分配给任一地区，不能宣称某个版本独立证实另一个版本的数据正确。此项状态 SOURCE_REGIONAL_70K_PERSISTENT_ACROSS_EDITIONS_OPEN。

本轮建立[两版8行追溯CSV](data_m2/rodrigues_1765_regional_reclass_2011_2019_persistent_70k_m3.csv)，锁定每一行的原论文、页码与原文PDF版本SHA256。

## 3. 1766年1,564 contos从财务官暂记余额转为军事损益

2019论文**PDF第99页／印刷87页**明确讨论第一Contadoria（Corte e Estremadura）负责军需的财务官 **Luís Gomes Peixoto**。其在**1762—1766年**累计借方责任余额约**1,564 contos**，用于军需承包商、瑞士军团付款、军事医院以及军官支出等，后在**1766年一次性转入“Ganhos e Perdas → Despesas Militares”**。作者精确引用原始档案 **AHTC, FGER, Livro Mestre 537, fólio 36**，同时怀疑部分款项可能此前已付给最终收款人、只是在国库账上延迟清算。

因此，该1,564 contos是**作者报告的历史会计结转金额**，而不是本项目已核验的1766年新增军费现金付款。既可能先向财务官拨款、延后向军需商结算，也可能发生借方账户延迟销账。没有原账与最终收款人签收单，不能判定实际付款日期、财政授权日期或全部是否实际支用。

2019论文另定位**AHTC FGER Livro Mestre 537, fólio 274**为1766年12月31日该Contadoria资产负债余额，并说明各本账簿临近用尽时，部分历史责任会被集中调整。这里仍只是原作者所述的原账目录与转录，本项目**没有取得fólio 36或274的手稿扫描**。

## 4. 1765—1766年同一Contadoria的损益借方规模变化

2019 Table 4.5（PDF第109页/印页97）：

| 项目：第一Contadoria | 1765年 | 1766年 | 统计定义 |
|---|---:|---:|---|
| 余额账户借方累计 | 8,176 contos | 7,147 contos | 资产/责任账面余额，不是现金收支 |
| 余额账户贷方累计 | 481 | 248 | 账面负债/贷方余额 |
| 损益账户累计借方 | **441** | **4,080** | 书面记账费用，不能直接对应当年现金付款 |
| 损益账户累计贷方 | 2,583 | 3,284 | 书面记账收入，不等于当年完整可用财政资金 |

4,080÷441＝**9.251701倍**，表示**该单一Contadoria的累计损益账户借方记录**量级变化，不是国家军费支出增长九倍。前述单个财务官1,564 contos的转账，数量级相当于1766年损益借方4,080 contos的**38.33%**。**仅是规模比较**；因缺少对应原始账户逐笔映射，不能宣称38.33%的新增军费得到了确证，更不能相加或从1766账面费用中直接扣除1,564当作真实现金开支。

这还解释了为何不能把1765军事费用约占国库登记费用59.66%的结论向1766做未经时点对齐的年度回归：1762—1766年军务、军需官机构改革、财务官预付和一次性结账可能使不同年份的当期账目不可直接比较。

本轮建立[8行1765—1766第一Contadoria表](data_m2/rodrigues2019_1765_1766_first_contadoria_account_rollover_m3.csv)，明确不混入其它三Contadorias、也不擅自拆为当年战争现金流。

## 5. 可复算计算与局限

新建[Python标准库复算程序](data_m2/reproduce_1765_1766_archival_account_rollover_and_editions_m3.py)和实际生成的[11项派生数据CSV](data_m2/rodrigues_1765_1766_edition_and_war_rollover_summary_m3.csv)。真实从GitHub现有研究分支下载源CSV+代码后执行**PASS，EXIT 0**：两版各4行相同且各差70,000 réis，8项账余额数值与来源一致，重分类1,564 contos的来源及解释限制保留，11项派生值按源生成，SHA256 **acc4d0a70a243f053fee0dc650e10522db6b419930d6875677f840190cab6ad3**。

**未完成**：1766实际军费现金流水与1762战事之间的跨期账实核对、对1564 contos付款凭证的查验、2011 vs2019两类Caixa余额359.525124/约2765 contos差异解释、1748国债/GDP来源冲突及2025黄金论文ASCM真实复现。网页PDF图片截图通道出现cache miss，作者论文PDF文件在研究Runner直接下载并以文字层逐段核查，但原始财务账簿页面仍NOT_ACQUIRED。

## 6. 下一项唯一可验收目标

优先申请合法查阅或获得**AHTC/FGER Livro Mestre 537 fólio 36（1762—1766 Peixoto暂记余额与1766军事损益转账）和fólio 274（1766-12-31余额）**，结合**Livro Mestre 2699 fólio 10/15（1765军事Vedorias结账）**，逐笔抽取至少四个日期：费用发生日、国库付给财务官日、最终军需受益人收到款日、转入Ganhos e Perdas日。另取得两类Caixa余额原卷及附表，严格按同一账户范围解释2011与2019发表值。以上原始账仍NOT_ACQUIRED，M3经济因果识别NOT_RUN，现有Draft PR不关闭不合并。
