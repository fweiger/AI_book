# CASE-PRT-001｜M3 葡萄牙1763—1777年王室国库原始账簿精确调阅清单、1765年会计现金与黄金币存量异口径审计

> 执行日期：2026-11-14；唯一权威业务Issue [AI_book #34](https://github.com/fweiger/AI_book/issues/34)，继续既有[Draft PR #38](https://github.com/fweiger/AI_book/pull/38)及`topic-010/case-prt-001-portugal-20261114`。  
> 实证状态：**AHTC_OFFICIAL_INVENTORY_ACTUALLY_ACQUIRED / RELEVANT_VOLUME_LOCATORS_21_PASS / RODRIGUES_2019_AUTHOR_PDF_ACTUALLY_ACQUIRED / SOUSA_2003_PREVIOUS_PAPER_CROSS_SCOPE_GAP_EXPLICIT / ORIGINAL_TREASURY_LEDGERS_NOT_ACQUIRED / TRANSACTIONAL_RECONCILIATION_NOT_RUN**。

## 1. 本轮核心突破：不再只有“maço 610 caixa 712”之类二级转引

**第一层机构公布的原始档案检索工具**：

- Tribunal de Contas, Arquivo Histórico, Alzira Teixeira Leite Moreira，*Inventário do Fundo Geral do Erário Régio*（1977），官网完整官方清单PDF：[Inventario_Adenda_Erario_Regio.pdf](https://erario.tcontas.pt/pt/arquivo_biblioteca/instrumentos_pesquisa/Inventario_Adenda_Erario_Regio.pdf)。本轮实际获取 **216页、3,738,870 bytes，SHA-256 `fd31975695bfbc0c5299e5eed2dda24c6b21c976eadd43528e7ff79baaef6739`**。
- Tribunal de Contas，[Erário Régio官方基金说明](https://erario.tcontas.pt/pt/arquivo_biblioteca/conjuntos_documentais/Erario_Regio.pdf)；本轮实际获取 **4页、44,059 bytes，SHA-256 `12e4de922f9b145dfd8d73850bef4b702bd304c41675db3b41461c15d4197d23`**。该馆藏包含1762—1833年约5457本账簿，且官方明确**并非该机关留下的全部记录**。
- **原件目前的存放状态**：[Tribunal de Contas 官方档案服务页面](https://www.tcontas.pt/pt-pt/TribunalContas/ArquivoBiblioteca/Paginas/Arquivo-e-Biblioteca.aspx)明确，依**2024-07-05协议**，AHTC历史档案移存Arquivo Nacional da Torre do Tombo (ANTT)馆舍，所有权及服务管理仍由Tribunal de Contas维持；**原件查阅需事先预约**，现有数字化材料的复制亦应通过`dadi@tcontas.pt`提出。没有实际预约、发送邮件或取得原账扫描；别把官方目录PDF误称原账影像。

### 本轮源文件可重现的新索引

[21条精确卷号CSV](data_m2/ahtc_1763_1777_treasury_original_ledger_requisition_inventory_m3.csv)从官方1977年目录按可核对的`Tesouraria-mor`卷号转录，覆盖：

| 案卷系列及1977年书号 | 真实年代或半年 | 本研究的检验目标 |
|---|---|---|
| **Tesouraria-mor, Livros da receita e despesa** `2–3` | 1763上、下半年 | 逐日期黄金/其他现金收入、军事支出与结余；对接1763-12-31黄金余额835 contos |
| **同系列`5–6`** | 1765上、下半年 | 对接Sousa2003黄金币存量76.8 contos与Rodrigues2019四Contadorias合并现金账户 |
| **同系列`7–8`** | 1766上、下半年 | 搜`Junta do Depósito Público`贷款真正借入日期、收入入账、支出转拨和支付命令 |
| **同系列`9–10`** | 1767上、下半年 | 对接1767黄金存量67.2 contos的记录日期与资金科目 |
| **同系列`29–30`** | 1777上、下半年 | 查1766旧贷款是否仍列王室应付、未还本金和利息差异 |
| **Tesouraria-mor, Livros Caixa `155–156`** | 1762—63／1763—64 | 日期级现金账 vs 收入／支出登记，查是否另有转账或物种转存 |
| **Livros Caixa `157`** | 1765 | 检验2019博士论文的`2,765 contos`会计现金账户重建 |
| **Livros Caixa `158–159`** | 1766／1766—67 | 查贷款/换汇/储备时点、是否存在金属货币以外的现金 |
| **Livros Caixa `169`** | 1777 | 查1766公共存款贷款余额及回款（不确保借据一定在此） |
| **`399`：税收追收额、欠款与税权** | 1762—1768 | 追收税源和公库收入并非同一指标，禁止混淆 |
| **`405–406`，以及`410`：王室命令/财政指令** | 1761—64、1764—68、1775—78 | 查借贷、军费、换券与划拨的法律日期与批准文本 |
| **`5351`：Tesouraria Geral das Tropas债权借贷账** | 1763—1793 | 记录1763年开始支付的**此前军人欠饷**，不是所有战争经费总账 |

索引共**10册半年度收入支出+6册现金+5册补充账=21册/条**，每项保留官网目录URL、目标时间、源状态`OFFICIAL_INVENTORY_ONLY_NOT_MANUSCRIPT`。**1977年号须由馆方核实与2024年搬迁后的当前`cota`是否一致**；不能把馆藏目录中卷号当作已签发的电子扫描资产编号。

这些是与过去仅有 `ANTT Ministério do Reino, Erário régio – papéis diversos, maço610 caixa712`、`Junta do Depósito Público – Consultas (1754–1783), maço360 caixa481`相比，**新增加的两条互补同年档案视角**：
- `AHTC Erário Tesouraria-mor` →王室总账及收付的**财政机关本账**；
- `ANTT Ministério do Reino/Junta Depósito` →公共存款机构向王室放贷的**对方机构债权账**。
- 它们不一定彼此都记录了同一笔现金，也可能存在净额与毛额、关账日与过账日的区别；需单笔共同编号与日期才可配对。

## 2. 1761年会计制度断点与其真实限度

官方档案说明记载**1761-12-22法令创建Erário Régio**（实际1762年开始运行），要求通过四个地域`Contadorias`统一国库管理并引入**partidas dobradas（复式记账）**。

该制度改革并不意味着从1762开始突然出现完全覆盖全王国、可与现代政府预算表直接相等的财政年度数据：官方资料明确该基金并不包含该机关全部文件，另有其它基金；还有一些国库以外的金库未纳入。尤其**Santa Igreja Patriarcal的财产和租金行政管理在1769-03-29才正式转入Erário**（官方馆藏说明），**1743的宗主教座堂债权重组账不可因此倒推为1765总账中已经统一管理的一项金库余额**。

重要的会计识别原则：`跨部门往来账户（contadorias互抵）`、`总出纳会计现金余额`、`黄金货币实物储存`、`皇室财政金税净收`、`票息/债券应付款`分别是不同的**资产负债/收入支出维度**。年终对账应同时检查各分账与跨账抵消分录。

## 3. 2019年直接研究王室财政原账的博士论文：两组现金账户合计2765 contos

Manuel José Benavente Rodrigues，(2019)，*O Erário Régio: as contas e o poder 1762–1833*，博士论文，ISCTE–Instituto Universitário de Lisboa，正式[大学机构全文PDF](https://repositorio.iscte-iul.pt/bitstream/10071/19808/1/PhD_Manuel_Benavente_Rodrigues.pdf)。本轮实际直接下载**339页、17,464,337 bytes，SHA256 `ca8b83728950b1746440baad2ac522b9dd5010f4237ebb5a8a6e3b6c528b565e`**；正文**印刷130页／PDF第142页**明确：

- 对1765年的四个`Contadorias`合并重建（作者称四个研究年份1765/1798/1816/1823中只有1765这次部门间汇总完全对平）；
- 两个会计`Caixa`账户在四个部门的**余额合计约2,765 contos**；
- `Deve`（会计借方/资产侧）约**17,725 contos**；
- `Haver`（贷方/负债侧）约**6,790 contos**；
- 1762—64累计会计收益约**8,244 contos**；
- 1765当年重建会计收益约**2,690 contos**，并非国家整个财政的预算盈余、也不是年可用黄金。

根据作者**报告的约数**做可审查算术：
`17,725−6,790−8,244=2,691 contos`，与其报告的`约2,690`相差1 conto；由于全部来自重建后的近似表示，不得假设原账相差1 conto，更不能**为了凑平强行改动原始表**。这只是`PUBLISHED_ROUNDED_VALUES_RESIDUAL=1`。

**作者还明确警告**：Erário账目不能被当成全葡萄牙王国所有账户，因为一些金库不属于Erário及账务技术约束，且现代意义上的损益账户在当时从属于`Caixa`账户的运作。2011年作者早期研究版与2019博士版是**同一研究者研究链**，不能当作两个独立历史实证复制。

## 4. 与Sousa2003国库黄金余额76.8的真正关系：不存在已证实的矛盾

此前Rita Martins de Sousa（2003）依据**ANTT Ministério do Reino, Erário régio papéis diversos, maço610 caixa712**，报告1765年国库黄金币约**76.8 contos**（原文未指明当年月日）；1763-12-31黄金币**835 contos**。

本轮[7条不同会计维度表](data_m2/treasury_1765_cash_accounts_vs_gold_coin_stock_provenance_m3.csv)将Rodrigues2019`两类Caixa账户余额2765`与Sousa2003`黄金货币余额76.8`明确标为：
- `accounting_basis`不同：**整个四Contadorias中两类会计`Caixa`余额** vs **一项黄金硬币存量**；
- `asof`不保证相同：**Sousa的1765数值具体月日未交代**；Rodrigues是年度合并账重建。
- `economic entity`与账本覆盖范围可能不同：2019整理四个区域Contadorias，2003引用ANTT特定国库黄金余额，无法提前证明包含关系；
- 即使均名为`Erário`，**绝不能把2765与76.8当成同日“全部现金 vs 黄金占比”，也不能据差额推断政府藏匿金银或财政破产**。
- `revenue/gain vs balance`也不同：2019会计当年收益2690并不对应硬币入库年新增。

这同样意味着，**1763→1765→1767金储备下降**仍仅是一条已发表的窄口径资产余额描述；其对政府综合流动性约束的因果解释仍依赖**实际现金流账本**。

## 5. 数据与可运行核验脚本

新增：
1. [data_m2/ahtc_1763_1777_treasury_original_ledger_requisition_inventory_m3.csv](data_m2/ahtc_1763_1777_treasury_original_ledger_requisition_inventory_m3.csv)：**21条**官方档案卷号及年份、候选审核目标、2024移存后的馆藏号风险。
2. [data_m2/treasury_1765_cash_accounts_vs_gold_coin_stock_provenance_m3.csv](data_m2/treasury_1765_cash_accounts_vs_gold_coin_stock_provenance_m3.csv)：**7条**作者发表重建数据、不同会计性质和实际来源页码。
3. [data_m2/validate_ahtc_ledger_requisition_and_1765_cash_specie_scope_m3.py](data_m2/validate_ahtc_ledger_requisition_and_1765_cash_specie_scope_m3.py)：原创**Python标准库**核验；从仓库读取21条检索号、7条发表值，检验年份连续类别、官方来源状态`NOT_MANUSCRIPT`、金储备与现金账户不可混合，及1765发表约数的1 conto余额残差。

本轮**实际执行`EXIT0`**，完整结果：
```text
PASS AHTC_archival_locator_rows=21 receipt_expense_half_year_books=10 cashbooks=6 supplementary_books=5 Rodrigues_1765_cash_accounts=2765.0 Sousa_1765_gold_coin=76.8 ACCOUNT_AND_ASOF_NOT_COMPARABLE accounting_rounded_gain_residual_contos=1 original_manuscripts=NOT_ACQUIRED transaction_causal_effect=NOT_RUN
```

源CSV哈希：
- 21条档案卷号CSV SHA256 `32d4458e84298ac6772cc22d3ba9a73409c1d0c92907fba851fbea3d35d40150`；
- 7条1765异口径数据CSV SHA256 `c5b1a40a0626d9700f65198eddef0054bb92e1d97019f9327cac9f914f4992ac`。

**核验范围只是馆藏元数据与已发表数值的完整性和分类正确性。** 本轮实际上未得到上述21本账簿或`maço 610`、`maço 360`手稿的任何扫描图像，不能宣称核验已进入逐笔现金入账；脚本也**未运行任何殖民黄金影响产业的因果模型**。

## 6. 已准备好的原始档案调阅说明（未发送邮件，不假装馆方响应）

根据[Tribunal de Contas当前官方程序](https://www.tcontas.pt/pt-pt/TribunalContas/ArquivoBiblioteca/Paginas/Arquivo-e-Biblioteca.aspx)，应从`dadi@tcontas.pt`要求AHTC在ANTT馆舍的账簿当前`cota`、可用数字副本、缺页情况、复印和调阅流程，并**先以以下最小集合请求书目确认，而不是一次性索取21本全量原件**：

1. `Tesouraria-mor, Livros da receita e despesa n.º 5–10`（1765—1767每半年共6册）；
2. `Tesouraria-mor, Livros Caixa n.º 157–159`（1765—1767共3册）；
3. `Livros de decretos/ordens n.º 406`（1764—1768）；
4. 需要核验1766公共存款借款时，附上`ANTT Ministério do Reino, Junta do Depósito Público de Lisboa, Consultas 1754–1783, maço 360, caixa 481`（**不同馆藏系列，并非AHTC目录的第360号账簿**）。

请求优先提供**1765年现金账户收盘页、1766年公存机构转入国库的入账页、与相邻借款命令日期相连的页图**。取得时应记录来源原卷编号、实际页码、照片/扫描文件哈希、历史货币单位、记账日期、借贷方向、资金所有者、是否过账重复和缺失页，再提取匿名或可合法公开的重建数值到GitHub；**未授权原件不应直接复制到公开AI_book**。

## 7. 下一次研究的真正验收门槛

- **GOLD_CASH_RECONCILIATION**：同一现金库、同一日期、同一货币：现金期初 + 实际入账 − 实际付出 = 现金期末；隔离黄金实物币种及跨机构转账避免双计。
- **DEPOSIT_LOAN_MATCHING**：1766金库向国库发出的贷款与国库对应入账同时能在双方账找到金额、币种和日期，之后1777账面偿还/未偿金额可按债权人一致性复算。
- **WAR_FINANCE_AND_PUBLIC_CREDIT**：军事/海军费用、私人资本配置必须有独立来源和对照时期，否则只标`HYPOTHESIS`而不称`CAUSAL_IDENTIFIED`。
- **仍未解决**：1749/1750债息下降法令源日期、1748债务/GDP 9% vs 8.152251%、2019慈善会Table4-Table5差额15.656contos、ICPSR198143与209481完整源码。
