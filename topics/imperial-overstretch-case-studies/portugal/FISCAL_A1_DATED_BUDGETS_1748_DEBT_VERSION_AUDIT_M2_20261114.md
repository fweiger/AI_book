# CASE-PRT-001｜M2 官方财政附录A1/A2日期级复核、名义债务偿付与1748年发表冲突

> 研究日期：2026-11-14；权威任务：[AI_book #34](https://github.com/fweiger/AI_book/issues/34)；现有[Draft PR #38](https://github.com/fweiger/AI_book/pull/38)。  
> 实际状态：**OFFICIAL_APPENDIX_A1_A2_READ / 36_PUBLISHED_REVENUE_BENCHMARKS_REGISTERED / 7_FISCAL_TO_DEBT_CHECKS_EXECUTED / 1748_ROUNDING_CONFLICT_CONFIRMED / ICPSR_198143_AND_209481_RAW_CODE_NOT_ACQUIRED**。发表附录中的数据点是作者据历史档案与前人研究重建的资料，不等于本项目取得并审阅了原始王室会计账簿影印本。

## 1. 为什么本次突破此前“半世纪财政均值”限制

新读入 Costa, Leonor F., António Henriques & Nuno Palma（2024）, *Anatomy of a premodern state*, *European Review of Economic History* 28(4):453–474，DOI [10.1093/ereh/heae003](https://doi.org/10.1093/ereh/heae003) **官方在线发表Appendix**，附录的**Table A1 (Nominal revenues, contos de réis)**给出完整的**36条观察行**，跨1367–1844，绝大多数是离散年份，1762–1777和1834–1844则为名义年均值。资料入口：[Oxford Academic全文（点击Appendix）](https://academic.oup.com/ereh/article/28/4/453/7667247)。该官方附录的Annex A/B还逐个指明早期的印刷史料与馆藏手稿。

已实际转录入库 [fiscal_nominal_revenue_benchmarks_appendix_a1_2024_m2.csv](data_m2/fiscal_nominal_revenue_benchmarks_appendix_a1_2024_m2.csv)，包括每条原文引用来源、时期属性、明确的资料限制。

关键观察：
- **1681**：中央名义财政收入1,702.2 contos，Dias (1985)；
- **1716**：4,342 contos，原作者将缺少的`décima`估自1681与1730基准，**不能说是完整1716实缴现金账**；
- **1730**：6,356 contos，Humbert (1730)、Carrara (2011)；
- **1762–1777**：5,222.9 contos，Thomaz (1988)提供的**跨16年名义年度均值**；作者注明论文其他结果采用未平滑的年度已平减数，但本次**并未取得作者这16个未平滑年度财务收入输入**；
- **1804**：11,045 contos，Macedo (1982)；**DEBT.PT A逐年偿付序列仅到1800，因此不把1804同1641—1800的债务数据强行拼接**。

统计层级约束：2024正文Table3是`central state revenues/GDP`分期百分比，Appendix A1是作者若干日期的**名义中央财政收入重建**，两者不能直接充当某年王国**全部财政支出**，更不能认定“中央收入−偿债＝军费”。2024文章所定义的帝国财政贡献是**支付相关殖民地费用后实际抵达葡萄牙本土国库的资金**，不能包含在巴西已被花掉的税款，亦不等于全帝国经济净ROI（正式文章Footnote 9和附录A1定义）。

## 2. A1特定年份与实际DEBT.PT债务偿付的一对一名义对照

本次使用**已下载、来源哈希锁定的DEBT.PT A官方XLSX** `Debt service!F` 年偿债流量（单位réis，除以100万后=contos），与官方Appendix A1中相同日期的`revenue`记录对齐：

`descriptive_service_to_revenue_pct = 100 × (DEBT.PT debt service in contos per year)/(Appendix A1 nominal state revenue in contos)`。

对于1762–1777，**分子分母均为16年内的名义年度均值**，绝不是一个具体年度的现金实际偿债率。A1中只有七个观察段落可与1641—1800债务资料对齐；其他时间段不凭空插值。

| 年份/观察段 | A1名义中央收入（contos） | DEBT.PT已记录债务偿付年额/年均（contos） | 描述性同币种比率 |
|---|---:|---:|---:|
| 1645 | 1,266.1 | 204.073 | **16.12%** |
| 1656 | 1,466.7 | 198.352 | **13.52%** |
| 1660 | 1,788.9 | 322.173 | **18.01%** |
| 1681 | 1,702.2 | 196.864 | **11.57%** |
| 1716 | 4,342 | 337.018 | **7.76%** |
| 1730 | 6,356 | 402.579 | **6.33%** |
| 1762—1777（16年均值对均值） | 5,222.9 | 526.502 | **10.08%** |

**这些是本项目首次基于两个具体来源的日期级计算**，比前一轮的`债务偿付/GDP半世纪均值 ÷ 发表财政收入/GDP半世纪均值`更接近同年份会计比例。不过，由于A1重建中的个别年度本身有补项或不完整估值、DEBT.PT的`short-term`偿付并不穷尽所有债务及现金流，我们**仍不能称之为经过全额国库审计的精确国家债务偿付/当年收入率**；也**不可与2024其他论文的债务偿付/国家支出混为一谈**。对应发表短表：[data_m2/fiscal_a1_explicit_years_vs_debt_service_m2.csv](data_m2/fiscal_a1_explicit_years_vs_debt_service_m2.csv)。

方向意义：前述7个对照中1716和1730债务偿付低于名义财政收入一成，1762—1777名义均值比率约一成。**尚无证据把葡萄牙18世纪制造业相对落后直接解释为债务偿付“吞没全部财政能力”**，但依旧不能否定特殊战争年份财政挤出或信用发行约束。

## 3. 单独证伪“1748年论文9%只是8.15%正常取整”的说法

已发表 Costa & Henriques (2024), *Different Indeed: Portuguese Sovereign Debt from 1500 to 1796*, Table 1 **明确列1748葡萄牙债务/GDP为9%**；其Table 1来源指`DEBT.PT`，论文Fig.3进一步写GDP基础是Palma/Reis（2019）。官方原文：[Brill开放PDF](https://brill.com/view/journals/ejph/22/1/article-p5_2.pdf)。

本项目从锁定DEBT.PT A XLSX（45,111字节，SHA256=`b2024474a20442b5577ca4667067edf22ffdf71a30faad01971f5a8d13104d17`），用Palma/Reis公开2019历史GDP XLSX（83,313字节，SHA256=`ee80439059ebfa3f67f870430671098fe6c853000be64d2605111285ee63045c`），对1743—1757连续15年逐年复算：

| 年份 | 实际版本锁定值 | 按最近整数取整 | 已发表Table1 |
|---|---:|---:|---:|
| 1743 | 8.652586% | 9% | 未单列 |
| **1748** | **8.152251%** | **8%** | **9%** |
| 1749 | 8.395834% | 8% | 未单列 |
| 1755 | 8.756698% | 9% | 未单列 |
| 1756 | 9.094161% | 9% | 未单列 |
| 1757 | 8.666638% | 9% | 9% |

**因此普通四舍五入不足以解释1748年：论文展示9%但当前源版本算出8.15%→8%。** 差异为**0.847749个百分点**，若分母不变、要使精确结果恰等于9%，需要比当前记录债务大约**10.4%**的分子；若分子不变，则要求相当于目前约**90.58%**的名义GDP分母。这些只是代数敏感性而非可证实的历史修订。

目前`1748_DATA_SOURCE_CONFLICT_OPEN`。可能原因包括2024表格取自历史版DEBT.PT、发表值取了附近年度、分母GDP版本或覆盖范围不同、单个转录错位。**不选取任何一项当作事实**；在获取2024 Table1生成表或历史版本前，保留公开原表与当前可再生版本两列。对账短表：[data_m2/debt_1748_published_vs_current_source_window_m2.csv](data_m2/debt_1748_published_vs_current_source_window_m2.csv)。

## 4. Appendix A2税制变迁：为什么不能按一个20%黄金税率贯穿1694—1800

2024附录A2明确指出“quinto”不是历史上始终统一的黄金产量20%固定税率：

- 1697—1713年，名义按矿产量五分之一，早期征收执行存在限制。
- 1713年12月7日—1724年9月30日，改为按奴隶及商业场所等征收固定`capitação`，并设30 `arrobas`最低税收目标。
- 1724年10月—1735年7月，恢复铸币局体系的五分之一，并要求黄金在铸币局转化、限制金粉运输。
- 1735年后再度采用`capitação`；原附录文字称持续“至1751”，**同时又明确写1750年12月3日恢复铸币局五分之一**，因此后期过渡日期本身存在用词/会计年度重叠，需要据更早的法律档案确定日期。
- 1750年12月3日起恢复铸币局税制，公布最低100 `arrobas`征收标准，延续18世纪余下时期。

规范化为[data_m2/brazilian_gold_tax_institutions_appendix_a2_2024_m2.csv](data_m2/brazilian_gold_tax_institutions_appendix_a2_2024_m2.csv)，对1735—1750的终止日期显式标记为**研究者依据1750年12月3日改革反推的边界，非原文独立确认**。

经济含义：1694年的黄金处理冲击、实际征税执行、1720—1804年的私人/公共汇回及1750后财政能力**属于不同事件与现金流**。不应把每一期`gold remittances × 20%`当作公共黄金税收，也不能将2025年ASCM的1694处理点解释成1694年正式颁布了同一种黄金税制。

## 5. 实际执行与复算说明

新增Python标准库脚本 [data_m2/reproduce_fiscal_a1_debt_service_m2.py](data_m2/reproduce_fiscal_a1_debt_service_m2.py)，依赖同目录之前已执行通过的`reproduce_debtpt_annual_ratios_m2.py`。从GitHub原分支**实时重新获取代码、36行A1 CSV、160行年度债务CSV和DEBT.PT官方原始A XLSX**，严格检查DEBT.PT源SHA后运行：

```bash
python3 reproduce_fiscal_a1_debt_service_m2.py \
 --debt-xlsx /path/to/DEBT_PT_A.xlsx \
 --source-dir ./data_m2 \
 --output-dir /tmp/case-prt-a1
```

**实际运行PASS**：
- `PASS appendix_a1_rows=36 matched_revenue_entries=7 debt_local_window=15 year1748_table_conflict=OPEN`；
- 7行日期财政/偿债对照 CSV SHA256：`c9f97912cf00d876868450d956ca41634f653f721f119fade21f588dae507881`；
- 15行1743—1757年的1748疑点相邻序列 CSV SHA256：`616dff3b7361257124c35aab6e2e0c38a16718675498f1625929edcb8e5067af`；
- 两份程序输出已逐字节提交同一GitHub研究分支。对照原始发表材料的史料真实性、历史债务范围及完整财政总账仍未逐笔独立审计；CI结构通过不等于经济计量模型复现。

## 6. 当前研究断点与唯一下一步

- 2024 `Anatomy` 的复现研究 [ICPSR 198143](https://www.icpsr.umich.edu/sites/icpsr/view/studies/198143/versions/V1) 显示Public，但实际下载仍被平台验证/列表错误阻挡，源代码、发表Table3生产过程与全套年度财政收入/支出输入**NOT_ACQUIRED**。
- 2025 Kedrosky–Palma黄金ASCM [ICPSR 209481](https://doi.org/10.3886/E209481V1)源数据/模型**NOT_ACQUIRED / NOT_RUN**；其1700年表格GDP数值与2019作者工作簿的矛盾仍待实际模型代码确认。
- 本次**只解决了**“有多少个财政基准年份”“这些基准能否和真实出版债务资料按年计算”及“1748是否只因整数取整”三项。**未解决**数据生成脚本的版本冲突或财政挤出的因果性。
- **下一项**：获取ICPSR 198143的`data and replication package`、确认1762—77原始年别收入是否完整并复算Table3；同时寻找Costa–Henriques 2024 Table1使用的1748债务版本/分母计算源，判断9%是否稿件调整或不同版本计算。另行保留1780年代黄金公共汇款1750/1713税制口径的跨档案异议。

资料出处：
- 2024主论文：https://doi.org/10.1093/ereh/heae003 ，在线Appendix A1/A2可由论文网页打开。
- 2024国债论文：https://doi.org/10.1163/16456432-20040019 。
- DEBT.PT官方债务数据：https://debt.pt/ 。
- Palma/Reis 2019历史GDP：https://doi.org/10.1017/S0022050719000056 。
