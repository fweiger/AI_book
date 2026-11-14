# CASE-PRT-001｜M2 铸币局黄金登记簿跨版本红队与葡萄牙主权债务反证（2026-11-14）

> 唯一权威Issue：[AI_book #34](https://github.com/fweiger/AI_book/issues/34)；现有[Draft PR #38](https://github.com/fweiger/AI_book/pull/38)。   
> 结论状态：**TWO_PUBLICATIONS_READ_AND_TABLES_CROSSCHECKED / SOURCE_DISCREPANCY_OPEN / DEBT_PRESSURE_MECHANISM_WEAKENED / ASCM_NOT_RUN**。历史数据表与其算术可核对，不等于铸币局原始账簿已由研究员逐册核验。

## 1. 核查动机：区分资源收益、公共转移和主权债务机制

上一轮已经在本目录发布2019年作者GDP工作簿的再计算、2025年Cambridge官方附录的黄金汇款和ASCM权重、以及1720—1804年黄金汇回与葡萄牙名义GDP的17段桥接数据。但要检验“殖民财富→财政约束→战略收缩/衰退”，至少还必须区分：

1. 黄金矿山产量与跨洋**已经汇抵里斯本**的资金/金属（生产 != 汇款）。
2. 汇抵私人和国家公共机构的款项（private != royal exchequer）。
3. 国家**汇抵后的净转移**（有些当地军政成本在巴西已扣）与葡萄牙**整个帝国项目全成本净ROI**（后者还要算其它殖民地、舰队、行政、国债、战争和外部性）。
4. 主权债务**存量/GDP**与偿付负担**流量/年度支出**；低国债也可能反映难以形成高度流动的债务市场，不能反推充裕财政能力。

## 2. 新增公开权威来源及阅读深度

**A. Sousa (2008)**，Rita Martins de Sousa, “Brazilian Gold and the Lisbon Mint House (1720–1807)”, *e-Journal of Portuguese History* 6(1) (Summer 2008)：原作者研究基于里斯本铸币局的`Livros dos Manifestos do 1% do ouro do Brasil`登记簿，并对荷兰公报、领事信函和里斯本公报来源逐期比较。**本轮实际下载Scielo原论文PDF 22页**，大小**2,078,425字节**，SHA256 **cad61abdd45d608a5380e2d3f87dfb42607e1093c39df055d642bb56ca87b090**；第12页Table 1、第15页Table 2可逐表核对。来源：https://scielo.pt/pdf/ejph/v6n1/v6n1a03.pdf 。来源等级：**同行评审历史研究+明示原始铸币局档案基础；本轮查阅的是2008研究而非原始手稿影像**。

**B. Costa & Henriques (2024)**，Leonor Freire Costa & António Castro Henriques, “Different Indeed: Portuguese Sovereign Debt from 1500 to 1796”, *e-Journal of Portuguese History* 22:5–28，2024-08-07在线发表，DOI https://doi.org/10.1163/16456432-20040019，公开全文 https://brill.com/view/journals/ejph/22/1/article-p5_2.pdf 。**本轮阅读全文Table 1、Table 2与相关文字**；Table 1债务存量/GDP数据标注来自 **DEBT.PT** (https://debt.pt/) 以及对英荷史料的整合；Table 2来源Costa, Henriques & Palma (2024)《Anatomy of a Premodern State》Figure 4。该工作并非与2019/2024其他同作者系列完全独立的方法论复现。2024债务学术论文说明国债水平较低，而持有人集中、抵押/财政信用条件及利率管制等可能限制借贷扩张。

**C. Kedrosky & Palma (2025)**，*The Cross of Gold: Brazilian Treasure and the Decline of Portugal*，JEH官方附录B.1第31页，来源 https://static.cambridge.org/content/id/urn%3Acambridge.org%3Aid%3Aarticle%3AS0022050725100764/resource/name/S0022050725100764sup001.pdf 。附录明确注明其名义汇款数据来自**Costa, Rocha & Sousa (2013)**，经Costa, Lains & Miranda (2016)转引。**2008 Sousa与2025所用2013/2016整理有相通的历史登记基础，严禁称为彼此独立的档案原始复现。**

## 3. 2008 vs 2025 两版黄金流量：16个完全对齐期间的实证核查

公开仓库新增：
- [sousa_2008_manifestos_5year_m2.csv](data_m2/sousa_2008_manifestos_5year_m2.csv)：2008 Table 1登记簿17组名义金额（contos；即百万réis）。
- [gold_manifestos_2008_vs_2025_reconciliation_m2.csv](data_m2/gold_manifestos_2008_vs_2025_reconciliation_m2.csv)：与2025官方B.1逐行匹配；**最后一行标记不可直接比较**。
- [sousa_2008_decadal_gold_private_public_m2.csv](data_m2/sousa_2008_decadal_gold_private_public_m2.csv)：2008 Table 2九组按十年公布的私人/公共**年平均**contos（最后1800—1807为8年）。
- [audit_gold_sources_and_debt_m2.py](data_m2/audit_gold_sources_and_debt_m2.py)：**本轮实际运行**的五源CSV算术审查器，输出清单式结构断言结果。

| 五年段 | 2008原文Table 1（contos） | 2025附录B.1（contos） | 2025−2008 | 解释 |
|---|---:|---:|---:|---|
| 1720–1724 | 15,344 | 15,408 | +64 | 差异0.42% |
| 1740–1744 | 28,267 | 29,456 | +1,189 | 差异4.21% |
| 1765–1769 | 19,210 | 19,712 | +502 | 差异2.61% |
| 1775–1779 | 11,060 | 10,712 | −348 | 差异−3.15% |
| **1780–1784** | **8,727** | **7,001** | **−1,726** | **差异−19.78%，匹配期间绝对差额最大** |
| 1785–1789 | 1,653 | 1,653 | 0 | 完全一致 |
| 1795–1799 | 4,928 | 4,982 | +54 | 差异1.10% |

**严格时间窗限制：** 2008 Table 1 最后一行是**1800–1807（8年）7,683 contos**，2025 B.1最后一行是**1800–1804（5年）7,672 contos**。不得因两值近似就认为两行同窗口，也不得把这11 contos 当作同期数据差异。两表总和2008逐项为**270,804**（文章正文写270,803，差**1 conto**，疑似原文合计取整/印刷误差，原因待核），2025为**271,045**，但**全表期间不一致，不能直接比较合计**。

只合计**完全相同的前16期（1720–1799）**：2008 = **263,121 contos**，2025 = **263,373 contos**，总差**+252（+0.096%）**。**总体合计接近并不意味着逐期可靠：1780–84一个区间就有1,726的负差，其它时期正负抵销。**

### 关键定位：1780年代差异几乎全部集中在公共汇款渠道

2008 Table 2公布**1780—1789年平均每年**公共汇回**482 contos**、私人**556 contos**；乘十年对应公共约**4,820**、私人约**5,560**（Table 2数值按整数取整）。

2025 Table B.1经1780–84与1785–89两行求和：**公共=2,313+780=3,093**，**私人=4,688+873=5,561**。

- **公共类别：2025相比2008低1,727 contos（−35.83%）**。
- **私人类别：2025相比2008高1 conto**（原文十年年均已取整）。
- 这与1780–84总汇回额差−1,726完全相符。由此将待查对象限定为**1780–84期间的公共汇款分类/汇总版本**，而不只是“整个黄金序列变动”。

**不作无证推断**：无法确认这一差额来自2013版对2008稿的后续更正、税种/运输线路分类改动、单纯印刷誊录，或别的来源；必须查询**Costa, Rocha & Sousa (2013)《O Ouro do Brasil》原页及Lisbon Mint登记簿**才能确定。2008 Table 1和Table 2彼此在1780年代可以复核，但**也不代表2008必然正确**。

## 4. 王室汇回款究竟是不是“净收益”：对前述研究的细化纠错

Sousa (2008)原文第15–16页明确说明：里斯本收到的王室款项**已在殖民地端扣除军费及殖民行政成本**，所以该作者把它称为对葡萄牙本土的**净汇回（net income received in Lisbon）**；其覆盖也包括铸币收益（seigniorage）、海关、各类承包及税收，**不等同征收黄金五分之一税（quinto）的金额**。研究还指出1%登记/护航费用与黄金五分之一税是不同税种，且1765年舰队护航制度变化影响记录机制。

本项目此前“公共汇款不是净额”的笼统表述需**严格细分**：
- **成立**：它不能等同于**王国+殖民地全系统、覆盖所有军费/债务/殖民扩张成本的帝国净投资回报率**，也不能直接等于国库总税收。
- **需更正**：按2008原研究解释，它已是**扣除一部分当地军政开支之后、汇抵里斯本的国家净汇款额**；因此将其机械视为尚未扣除任何地方军费的“毛收入”同样错误。
- **仍未验证**：2008与2025 B.1的public定义、扣费规则是否完全相同；必须查阅2013/2016后续资料及原始记录。

这个会计口径变化意味着：若研究战争财政“挤出”，我们需要找到**巴西本地留用的税款与驻防费用**以及葡萄牙本土后续开支，才能建立`税收 → 当地留用/军政成本 → 汇抵里斯本 → 王室支出/债务`的完整资金桥。

## 5. 主权债务与公共信用：对“高债务挤出→殖民帝国衰退”提供反例

新增两份同源定位清楚的2024年数据表：
- [sovereign_debt_2024_crosscountry_benchmarks_m2.csv](data_m2/sovereign_debt_2024_crosscountry_benchmarks_m2.csv)：Costa & Henriques 2024 Table 1，国债**存量**÷GDP（百分比），荷兰仅指**Holland省**而非整个联合省共和国。
- [sovereign_debt_service_2024_benchmarks_m2.csv](data_m2/sovereign_debt_service_2024_benchmarks_m2.csv)：同文Table 2，债务**偿付**÷**国家支出**（百分比），为稀疏观测，不得插成年度连续曲线。

| 年份 | 葡萄牙债务/GDP | 英格兰/英国文献标签债务/GDP | 荷兰省债务/GDP |
|---|---:|---:|---:|
| 1690 | 7% | 38% | 100% |
| 1720 | 8% | 90% | 200% |
| 1748 | 9% | 109% | 233% |
| 1763 | 9% | 177% | 无观测 |
| 1783 | 8% | 245% | 无观测 |

葡萄牙公布债务偿付/支出：**1680年22.9%，1766年7.6%**，相差**−15.3个百分点**。这是两个历史预算点、不同财政环境，**不是1766年前后的债务利息年度趋势，也没有直接测出殖民驻军被挤出金额**。

### 红队进一步查到2024文内统计口径不统一

2024文章Table 2表头是**“Debt service as a share of the state expenditure”**；相邻正文却使用国家**revenue（收入）**描述债务偿付份额，还概括其“不超过五分之一”，但Table 2中**1680年=22.9%已超过20%**。本项目必须优先采用**原表头/上游2024 EREH Figure 4的支出结构定义**，不得误写成利息/收入，更不能用这句话自行背书全部年份都不超过20%。正式结论应为**支出结构中1766年偿付比例低于1680年，仍需要核实预算覆盖范围和条目定义**。

这项反证**削弱“18世纪葡萄牙是被不断攀升的主权债务利息直接压垮”机制**；但**低存量可能反映融资市场不够广泛，战略能力受到“不能借”而非“借太多”的约束**。后一个机制仍需债券持有人分布、发行成交量、市场利差、借新还旧、战争年份财政资料验证。不能简单说债务低就说明财政充裕。

## 6. 史料相互独立性、潜在偏差与下一步

| 链条或待验证命题 | 当前状态 | 最直接否证/核实动作 |
|---|---|---|
| 2008铸币局Table 1 17行、2025 Table B.1 17行对齐与加总 | **PASS（发表表格算术）** | 已编写和实际运行审计脚本 |
| 1780–84公共汇回差1,726/1,727 contos | **SOURCE_CONFLICT_OPEN** | 查2013《O Ouro do Brasil》对应表页、原始`Livros dos Manifestos`汇抵分账 |
| 黄金公共汇抵款的净额性质 | **PARTIALLY_SUPPORTED_BY_SOUSA_2008** | 查巴西地方留用、海军护航、殖民军政账户，避免将部分净额误叫帝国总净收益 |
| 1760年代国家公共款与黄金总流量不同步 | **DESCRIPTIVE_SUPPORTED** | 细分税种和资金来源（黄金税/铸币/海关/合同） |
| 1690–1783葡萄牙国债/GDP相对英荷很低 | **PUBLISHED_BENCHMARK_SUPPORTED** | 检查DEBT.PT原始债务合同的样本与GDP估算版本 |
| 1766偿债/支出=7.6%（非偿债/收入） | **PUBLISHED_TABLE_SUPPORTED** | 取得对应1766历史预算原始影印和2024图4上游数据 |
| 2025论文“1694黄金→约−40% GDP/person”ASCM模型独立复现 | **NOT_RUN** | 合法取得ICPSR 209481可执行输入/代码 |
| 葡萄牙长期殖民净ROI、债务利息挤出海外支出 | **NOT_IDENTIFIED** | 年度完整双边财政账目、军费与债息数据 |

### 研究优先级建议

**M2下一项最有价值的原始史料定位**：在继续获取ICPSR 209481的同时，找到2013年`Costa, Rocha & Sousa, O Ouro do Brasil`汇款表格及Lisbon Mint档案中**1780–1784王室款项**的栏目定义；因为这项差异直接影响新建的公共黄金汇款—GDP系列局部数值，而且已证明差额集中于公共渠道。不要因为单个异常值否定整个2025年ASCM，也不要因16期总和相近而忽略局部来源问题。

### 本轮可复查执行证据

1. 使用网页论文PDF及另一只读运行环境，实际获取Sousa (2008) PDF（22页、2,078,425 bytes、SHA256上述），对照Table1 p12与Table2 p15；2024文献依赖出版方官方全文Table1/2与同作者上游2024论文对应说明。
2. GitHub脚本`data_m2/audit_gold_sources_and_debt_m2.py`在只读研究Runner中通过HTTPS下载**同一研究分支的六个文件**并实际执行，**EXIT 0**；总额、16同窗口比较、1780差额及2024债务口径全部断言通过。该Runner测试仅是**出版数据算术及GitHub文件完整性**，未运行任何历史因果模型或拿到原始账簿。
3. 文献2008与2025的样本期不完全一致；无法核实2008全文270,803与其Table1各项合计270,804之间一conto差异的原因，标记 `MINOR_SUM_CONFLICT_OPEN`。
4. 研究目录仅入库独立的摘要和有限数量原始发表数值、可运行QA脚本；**未把原作者PDF原文或尚未明确再分发许可的完整数据文件复制至GitHub**。

## 参考文献入口

- Sousa (2008)：https://scielo.pt/pdf/ejph/v6n1/v6n1a03.pdf
- Costa & Henriques (2024)：https://doi.org/10.1163/16456432-20040019
- Costa, Henriques & Palma (2024)，上游开支口径：https://doi.org/10.1093/ereh/heae003
- Kedrosky & Palma (2025)：https://doi.org/10.1017/S0022050725100764
- 论文正式在线附录：https://static.cambridge.org/content/id/urn%3Acambridge.org%3Aid%3Aarticle%3AS0022050725100764/resource/name/S0022050725100764sup001.pdf
- DEBT.PT原始债务数据库导航：https://debt.pt/
