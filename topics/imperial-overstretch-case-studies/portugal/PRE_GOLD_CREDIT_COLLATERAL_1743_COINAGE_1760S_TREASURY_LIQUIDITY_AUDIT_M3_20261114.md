# CASE-PRT-001｜M3 黄金繁荣前的税收抵押信贷先例、1743—1744铸币/旧债转换与1760年代国库流动性审计

> 日期：2026-11-14；业务权威Issue：[AI_book #34](https://github.com/fweiger/AI_book/issues/34)；研究分支`topic-010/case-prt-001-portugal-20261114`，沿用 Draft [PR #38](https://github.com/fweiger/AI_book/pull/38)。  
> **状态**：`PRE_GOLD_CREDIT_PRECEDENT_PUBLISHED`；`2003_SOUZA_TREASURY_MINT_AND_DEPOSIT_VALUES_READ_AND_RECONCILED`；`1749_VS_1750_LEGAL_DATE_CONFLICT_OPEN`；`CASH_ACCOUNT_CAUSAL_BRIDGE_NOT_RUN`；`PRIMARY_LOAN_DEEDS_AND_1883_LEGAL_PAGE_NOT_ACQUIRED`。本轮没有把历史作者二次引用当作1647或1743王室原始文书已经逐件查阅。

## 1. 新的关键反例：税收抵押支持的债务在巴西黄金之前就已存在

葡萄牙1841年《O Panorama》卷V，第210期第**148**页刊有公共债务史文章`Fundos publicos`，其葡萄牙部分**明示引述Agostinho Albano da Silveira Pinto于1839年出版的《A Dívida Pública Portugueza》**。本轮独立下载期刊原PDF：
- 官方葡萄牙里斯本数字报刊馆：https://hemerotecadigital.cm-lisboa.pt/obras/opanorama/1841/N210/N210_master/N210.pdf
- 8页，2,366,661 bytes，SHA256 `d30297e0388d8ac9ab9a8010aef4106ca199fd3f4c4730dc0e47ca1e3bac938d`；**本文仅阅读185年前公共印刷刊物，不等于1647或1704年的合同影印件**。

期刊引述1839研究列举：
- **1647年**：商人以约**200,000 cruzados**、**6¼%**利率向国家提供舰队装备贷款，指定**糖税（`direito do açúcar`）收入**暂时作为还本付息的抵押。
- **1662年**：为步兵费用存在另一笔贷款；期刊此处**没给可定位的本金、票息或单一税源**，不得补造。
- **1704—1706年**：国王D. Pedro II通过以里斯本海关税收为担保的债务安排取得**480 contos de réis**。期刊段落结尾关于`8%`的表述是对较广泛税收抵押养老金/利息的概括，**不能明确归于这一笔480 contos贷款**；本轮已将该笔的独立票息纠正为`NOT_IDENTIFIED`。

**因果后果：** 即使未来证明18世纪巴西黄金与公共信用扩张有密切关系，仍不能说黄金`首先创造`了税收抵押国债。更强且可证伪的命题是：在1647年糖税/1704—06年海关抵押已存在的前提下，黄金是否改变国债规模、票息、持有人、可转让性、再融资方式与帝国战略支出安排？1647单位是`cruzados`，**不得在无当年汇率/兑换口径时与1704、1743年`contos de réis`直接加减或同比**。

新的原始发表量值与史料等级CSV：[pre_gold_tax_collateral_1743_1749_1750_edict_coinage_source_audit_m3.csv](data_m2/pre_gold_tax_collateral_1743_1749_1750_edict_coinage_source_audit_m3.csv)（9条）；[类型与冲突检查程序](data_m2/validate_pre_gold_credit_collateral_and_edict_dispute_m3.py)，已在Runner实际运行PASS。

## 2. 交叉使用DEBT.PT原始年度净发行：不能硬接1841年的历史融资额

独立再次下载[DEBT.PT A原始Excel](https://debt.pt/pdf/DEBT_%201529-1557%20%26%201641_1800.xlsx)（45,111 bytes，SHA256 `b2024474a20442b5577ca4667067edf22ffdf71a30faad01971f5a8d13104d17`），核对`Debt stock`列C=年，H=长期`juros`**净发行**，I=已记录短债净发行：
- **1647年**：H≈**+1.563435 contos**；I≈**−95.591647 contos**。与1841转引所说的1647年约**20万 cruzados借贷**完全不属一个数据范围/货币单位：前者是历史研究团队**净发行**、后者是具体记述的**贷款面额**，且早期1643–1660年本项目之前发现`Δ债务余额−净发行`多处记账时点异常。**不一致不证明1647年那笔贷款是假的**。
- **1704—1706年**：H三年加总≈**+400.885700 contos**；I≈**+151.203793 contos**；两类相加≈**+552.089493 contos**。1841所述**480 contos里斯本海关贷款**可能是同期多个来源中的一项，不能把552.089与480的差额自动记成“其它借款=72.089 contos”，因为不同债种、老债转换、时点及统计覆盖无法对齐。
- 本项目已发布159年年度净发行与库存对账表：[debtpt_issuance_vs_stock_delta_1642_1800_m3.csv](data_m2/debtpt_issuance_vs_stock_delta_1642_1800_m3.csv)，因此没有伪造一条新的年度现金收入表。

## 3. 1743—1744年铸币4,196 contos与所谓“处理旧债5,000 contos”：账务对象不相等

独立来源：Rita Martins de Sousa (2003), *Moeda e Estado: políticas monetárias e determinantes da procura (1688–1797)*，*Análise Social* XXXVIII(168):771–792；原文正式全文 https://revistas.rcaap.pt/analisesocial/article/download/35368/24541/156638。实际下载22页、106,063 bytes，SHA256 `bb31354d0d00c1c1f70234e0670a5ef1bdadd91780fc24ecd67d3f9f1b39123d`；关键文字在**印刷790页/PDF第20页**，同时作者有明确2001年先行工作论文版本。

Sousa列：
- **1743—1744年由王室主导的黄金铸币金额≈4,196 contos**。其计量对象是贵金属铸币/货币发行，不是`quinto`税额、财政可用收入、净铸币税、海上黄金汇款或存款变化。
- 同期所谓**5,000 contos债务`amortização`**系**再次转引Azevedo**，而历史原文把其中部分描述为`amortização fictícia`（经济上旧债仍存在，只是债权人/票息转换）。所以不能假设所有5,000 contos真正以现金偿还并从王室账面消失。
- **同一时期、数值量级接近只能作为研究线索**：`4196-5000=-804 contos`**不是**经核验的王室资金缺口、铸币能力不足或融资约束强度。货币铸造与清偿可能循环/跨账且非独立可比较费用流。
- Sousa2003使用Gomes1883描述1743降至5%、1749降至4.5%的债券票息，亦不能冒称直接读到了1883年官方法律汇编该页。

## 4. 新发现的“1749/1750年3月16日”版本矛盾

目前有两组独立可检索的印刷说法：
- **1749-03-16**：Azevedo，1947年第二版《Épocas de Portugal Económico》印刷375页的脚注，标注源自Gomes (1883)债务法律汇编**p318**；Sousa(2003)也记1749并引用Gomes，但其与Azevedo共享**1883书的二次引用链**，不可算作两份直接原件。
- **1750-03-16**：1841年《O Panorama》印刷148页以公共债务史内容明确列出1743年2月4日与**1750年3月16日**两个日期。这里的1841来源早于1883/1947/2003，但也不是法令原件，不能因为更早就自动裁定为正确。
- **原件候选**：葡萄牙政府1883年`Collecção de leis da dívida pública portugueza`第一部债务法汇编第I卷，已经有葡萄牙国家档案馆Torre do Tombo馆藏目录和**1883年12月19日国会记录确证出版并分发120本**（https://debates.parlamento.pt/catalogo/mc/cd/01/01/01/102/1883-12-19）；**但p317–318本轮仍NOT_ACQUIRED**。精确裁决需要看到汇编原文日期、法令/公告编号及可能的颁布/实施/公布不同日期，不能补造。

此项日期冲突在新CSV中**同时保留1749和1750**，并由检查脚本强制`SOURCE_DATE_CONFLICT_OPEN`。这属于**有待原件核实的史料差异**，不是已经证明某位史家犯错。

## 5. 1760年代财政压力更接近资产存量/政府借款的实证链

同一Sousa2003论文**印刷788–789页/PDF第18–19页**，根据葡萄牙国家档案馆材料，公布了国家铸金币、国库已有金币、里斯本公共存款机构对各借款人的债权：

| 时间 | 原文重建值（contos） | 正确计量性质 |
|---|---:|---|
| **1763** | 国家黄金铸币 **1,794** | 年度**铸币流量**，非国库净税收 |
| **1763-12-31** | 国库黄金**835** | 明确截至12月31日的**资产存量** |
| **1765** | 国库黄金**76.8** | 资产存量，但具体月日未说明 |
| **1767** | 国库黄金**67.2** | 资产存量，具体月日未说明 |
| **1766** | 国家黄金铸币 **1,073** | 年度货币发行流量 |
| **1766→1777** | 里斯本公共存款金库贷给国家、至1777仍未偿**371.4** | 由1777年资料回顾的**未偿国库贷款**；不是1777年新增借贷 |
| **1777** | 同金库所有借款方未偿贷款总额约**673** | 包括国家、商业公司、市政和个人的**多借款人债权存量** |
| **1798** | 对国库的贷款所报告数额升至**1,616** | 原论文未允许在本轮区分是累计支用、账面余额或某年新发贷款；**不得标为1798年贷款新增额** |

作者明确引用底层档案：
- 1763后国库黄金：**ANTT, Ministério do Reino, Erário régio – papéis diversos (s.d.), maço 610, caixa 712**；
- 1766国家借用公共存款及1777未偿额：**ANTT, Ministério do Reino, Junta do Depósito Público de Lisboa – Consultas (1754–1783), maço 360, caixa 481**；
- **1755地震后的档案完整度、战时舰队中断、对西班牙战争军费和公共存款周转**都是可能混杂因素；不能由两三个黄金存量基准年份做有统计显著性的因果识别。

与论文所印百分比独立核对：`371.4/673 × 100 =55.185736%≈55.2%`，只表明**1777年该机构未偿贷款存量中有较大的国家债权组成**，不能把它加到1766年铸币或1763年国库黄金上。

新增 [sousa2003_1763_1798_treasury_gold_mint_deposit_loans_m3.csv](data_m2/sousa2003_1763_1798_treasury_gold_mint_deposit_loans_m3.csv)（8条），将`stock`/`flow`/`retrospective loan stock`分成不同类别；[validate_sousa2003_treasury_royal_mint_deposit_loans_m3.py](data_m2/validate_sousa2003_treasury_royal_mint_deposit_loans_m3.py)拒绝把1765/1767余额误记为12月31日，标出原始档案状态`NOT_ACQUIRED`。

### 可证伪的研究假设

`18世纪国家铸币/国库金储备与税源现金流发生变化 → 战争财政压力与储备动用 → 公共存款机构提供国内融资或再融资 → 帝国军事费用或本土制造业投资决策受约束`。

逐个箭头必须用可匹配的日期及会计凭证，检验战争费用、储备期初/期末、税收现金入账、国债净发行、公共存款贷款分配和欠息，而不是凭历史事件发生顺序归因。英国/荷兰跨国公债比较应当严格匹配存量/GDP分母，不能拿`1647 cruzados`与`1743 contos`做未经折算的国际成本估值。

## 6. 真正运行的QA与缺失项

本轮从**当前GitHub研究分支重新下载**两份CSV及Python验证程序，在只读研究环境中实际执行：
- `validate_pre_gold_credit_collateral_and_edict_dispute_m3.py`：**PASS 9条**，单位/日期/出版文献/原始凭证缺失标记严格分离，禁止1704—06未核利率、1647货币混算、1743铸币减去5000债务、裁决1749/1750争议。CSV SHA256 `326a50d242e0450ca0dfad2efcfb6b95bad9a72d2d1ded7e6dab9a2c37739d0a`。
- `validate_sousa2003_treasury_royal_mint_deposit_loans_m3.py`：**PASS 8条**，校验1763/1765/1767国库余额、1763/1766铸币、1766→1777未偿贷款、1798未经辨别的余额性质，并核对55.2%。CSV SHA256 `360172f1baf149a4c84d63e48c281e8bffbcd18d44d17f5ec8a67dda052e6219`。
- 两篇历史论文官方PDF实际取得：1841 *O Panorama* 8页**2,366,661 bytes** SHA256 `d30297e0388d8ac9ab9a8010aef4106ca199fd3f4c4730dc0e47ca1e3bac938d`；Sousa2003 22页**106,063 bytes** SHA256 `bb31354d0d00c1c1f70234e0670a5ef1bdadd91780fc24ecd67d3f9f1b39123d`。源PDF不镜像入公共仓库，作者/馆藏链接与页码、数据派生摘要可查。
- 研究Runner对官方DEBT.PT A XLSX（源SHA256 `b2024474a20442b5577ca4667067edf22ffdf71a30faad01971f5a8d13104d17`）另行抽取1647与1704—06年度H/I净发行并报告上述数值；未宣称能与1841提到的具体合同金额独立对账。
- 网页PDF截图`web.run screenshot`多次遭遇Cache miss，不能谎称图像级核验通过；原论文PDF文本在远程读取、出版机构页面索引在web工具核对。

仍为`NOT_ACQUIRED`：**1647糖税舰队借款原始合同、1704—1706海关抵押合同、Gomes1883 p317–318法令正文、1743宗主教座堂逐笔债务资产转换、ANTT Erário régio maço610 caixa712与Junta Depósito maço360 caixa481原始手稿**，以及2024财政研究ICPSR 198143和2025黄金ASCM ICPSR209481复现包。本轮经济因果实验`NOT_RUN`、1748公开债务率9%与原始数据8.152251%的差异`SOURCE_CONFLICT_OPEN`。项目仍在原有Draft PR，不合并main。

## 7. 交接下一唯一目标

**直接按作者已经给出的`ANTT Ministério do Reino, Erário régio maço610 caixa712`及`Junta do Depósito Público de Lisboa Consultas 1754–1783 maço360 caixa481`调阅底层金储备、借款转入、债务偿还凭证，构造1763—1777“国库现金、军费、借款”的日期级三表对账**；并继续独立读取Gomes1883 p318以解决1749/1750法令日期。若原始手稿不可获得，保持`NOT_ACQUIRED`并比较已有发表证据的解释边界。
