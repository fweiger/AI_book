# CASE-PRT-001｜M2 葡萄牙历史GDP Excel 数据资料包

唯一任务：[AI_book #34](https://github.com/fweiger/AI_book/issues/34)；审查分支：[Draft PR #38](https://github.com/fweiger/AI_book/pull/38)。本目录不是正式main知识图谱。

## 原始数据（公开引用，不镜像原始 Excel）

- 原始学术论文：Nuno Palma & Jaime Reis (2019), *From Convergence to Divergence: Portuguese Economic Growth, 1527–1850*, Journal of Economic History 79(2), 477–506, https://doi.org/10.1017/S0022050719000056
- 作者公开工作簿：https://drive.google.com/file/d/17M1nrjx-6B7fIMJGNTJ6tle6TtWNkLA7/view
- 另一公开登记版本：https://zenodo.org/records/13254210 （未比对二进制，不能认定与作者Drive文件完全一致）。
- 本轮实际校验版本：palmareis_JEH_2019.xlsx，83,313 bytes；SHA-256：ee80439059ebfa3f67f870430671098fe6c853000be64d2605111285ee63045c。
- 本目录上传的是从作者原文件计算的重点年份、十年均值、增长率、指标字典与可复现方法。原始Excel版权/再分发许可未确认，**不在公开仓库镜像完整原始工作簿或全部324年度逐条原始值**。

## 数据文件

| 文件 | 内容与统计口径 |
|---|---|
| [gdp_benchmarks_m2.csv](gdp_benchmarks_m2.csv) | 14个重点年份GDP、人口、CPI及2025论文的发表表格对照 |
| [gdp_decadal_aggregates_m2.csv](gdp_decadal_aggregates_m2.csv) | 1527—1850年按日历十年分组的34行算术均值；1520s/1850s不是完整10年，参看n_years |
| [gdp_window_changes_m2.csv](gdp_window_changes_m2.csv) | 9个阶段的人均GDP、人口与真实GDP端点百分比变化 |
| [gdp_rolling_sensitivity_m2.csv](gdp_rolling_sensitivity_m2.csv) | 1/5/11/21年中心平滑口径的阶段对比 |
| [gdp_source_variable_dictionary_m2.csv](gdp_source_variable_dictionary_m2.csv) | GDPs及CPIs两个工作表13个字段的单位、来源和解释边界 |
| [gdp_source_manifest_m2.json](gdp_source_manifest_m2.json) | 原作者文件hash、来源、输出hash、已验证与未执行状态 |
| [reproduce_gdp_from_author_xlsx.py](reproduce_gdp_from_author_xlsx.py) | Python标准库复算，须自行从作者链接取得原始工作簿 |

## 独立核验结果（2026-11-14）

作者Excel的GDPs、CPIs各有1527—1850年连续324个年份记录，无重复年份或关键指标空值。逐年核对pcGDP × population_millions = real_GDP_millions，以及CPI_silver × silver_price_index / 100 = CPI_reis，结果在浮点误差内通过。这是内部**会计一致性**，并非独立原始档案验证。

重要的跨发表数值冲突：作者工作簿1700年人均GDP为987.2047714，2025年Kedrosky & Palma *The Cross of Gold* Table 1却展示830；而1650年作者工作簿约829.951。先前按830计算的1700—1750年+65.30%不适合作为2019作者工作簿的增长率；本资料包同口径结果为+38.95%，1750—1800年为−33.22%。这提示展示层面潜在转录问题，**不能直接推定2025 ASCM模型输入错误**。2025论文：https://doi.org/10.1017/S0022050725100764。

指标边界：作者Excel中的CPIs为总体价格指数（银价计价/货币reis计价），**不是贸易品/非贸易品相对价格或实际汇率**。不能直接用此工作簿复算荷兰病价格机制。十年均值为各年算术平均，并非人口加权；增长率为两个端点之比，不能与2025 ASCM反事实约−40%混同。

## 复算

首先从作者公开链接下载相应xlsx，执行（Python 3.10+，不要求第三方Python库）：

~~~bash
python3 reproduce_gdp_from_author_xlsx.py --source /path/to/palmareis_JEH_2019.xlsx --output-dir ./reproduced
~~~

脚本默认校验作者工作簿SHA-256并验证全部年度日期范围、GDP和CPI恒等式，然后输出本目录的五份CSV及来源清单。只有检查不同版本时，才可显式使用 --allow-new-version，结果必须另外存放，不能混入已审核版本。

研究状态：M2作者原始工作簿取得PASS；数据一致性PASS；跨论文1700年差异OPEN；2025年ASCM因果复现NOT_RUN；完整年度财政/军费/债息NOT_ACQUIRED。下一项工作是取得ICPSR 209481的完整实际运行输入，验证其1700年取值和1694干预点，再重跑模型：https://doi.org/10.3886/E209481V1。


## 2025年黄金论文官方附录：新增M2数据（2026-11-14）

来源：Kedrosky & Palma（2025）Cambridge University Press官方35页附件 [S0022050725100764sup001.pdf](https://static.cambridge.org/content/id/urn%3Acambridge.org%3Aid%3Aarticle%3AS0022050725100764/resource/name/S0022050725100764sup001.pdf)，**1,110,168 bytes，SHA-256=6209adcdc8628d8be011e74838f6e156987bebd4b684f083691dce007b115aac**。本目录只提交转录的数据表与原创核验说明，不镜像官方PDF。正式核查报告在 [上一层目录](../OFFICIAL_SUPPLEMENT_GOLD_FLOW_ASCM_WEIGHTS_M2_20261114.md)。

| 新增文件 | 表格及边界 |
|---|---|
| [gold_remittances_fiveyear_b1_1720_1804_m2.csv](gold_remittances_fiveyear_b1_1720_1804_m2.csv) | 附录PDF第31页B.1；1720–1804 17个五年段，私人/公共×名义/不变1720年réis金额及公共比重；**绝非国库净现金流或每年总产金量** |
| [ascm_donor_weights_b3_b4_m2.csv](ascm_donor_weights_b3_b4_m2.csv) | 第33页B.3/B.4；6国基准与4国剔除西荷方案×CPI/GDP/人均GDP共10行。负权重合法，归一求和测试PASS；**不是重跑回归得到的权重** |
| [commodity_price_coverage_b5_m2.csv](commodity_price_coverage_b5_m2.csv) | 第33页B.5；11种商品×4个年份段的作者公布覆盖率。1701–1800年Soap=62、Candle=88、Linen=91；价格插值敏感性仍NOT_RUN |

B.1名义数总计私人211,080、公共59,965、合计271,045，单位均百万réis；公共占比22.1236%。B.3/B.4各指标权重的绝对归一误差不超过2e−9。**作者官方附录已取得**，但ICPSR 209481可执行完整复现包仍**NOT_ACQUIRED**；不会以官方表格归一测试代替论文ASCM因果检验。


## M2 Gold × GDP同期对接与数据复算（2026-11-14）

- [gold_to_nominal_gdp_fiveyear_bridge_m2.csv](gold_to_nominal_gdp_fiveyear_bridge_m2.csv)：新增17行（1720–1804连续17个五年段），将官方附录B.1的五年私人/公共黄金名义汇款对上Palma–Reis 2019作者Excel `GDPs!H` 的**五个年度名义GDP之和**，均为百万réis；含公共/私人分项的GDP比率、五年平均人均GDP和双重来源标记。
- [reproduce_gold_gdp_bridge_m2.py](reproduce_gold_gdp_bridge_m2.py)：标准库+既有[reproduce_gdp_from_author_xlsx.py](reproduce_gdp_from_author_xlsx.py)读取作者Excel，校验原始SHA256、时间连续性及公共/私人汇回量，再从原始文件运行生成桥接CSV。
- [完整审计与ICPSR 2026年平台迁移说明](../GOLD_REMITTANCES_TO_GDP_BRIDGE_AND_DATA_ACCESS_AUDIT_M2_20261114.md)。

实际运行命令（需从作者公开链接自行取得原始XLSX；本仓库未镜像）：

```bash
python3 reproduce_gold_gdp_bridge_m2.py \
  --source /local/path/palmareis_JEH_2019.xlsx \
  --gold-file gold_remittances_fiveyear_b1_1720_1804_m2.csv \
  --output /tmp/gold_bridge.csv
```

复算输出CSV SHA256 `bbf1d77cbe014f22ed5d0ffbf1bd311cad253ee956911e83266ca12d62f3b162`，脚本 SHA256 `ccd49e95c5d25b1f51884f38cb772e6eca901ee0d81e6b83e06d4b738038a157`，两个GitHub blob哈希均已确认与本地运行验证文件**逐字节一致**。黄金对同期GDP的累计名义强度：总2.9298%，公共0.6482%，私人2.2816%。这是历史数据的**描述性比率**，不是财政税收率、国内价值增加或黄金负面因果效应。


## 2026-11-14 M2 新增：DEBT.PT原始Excel和债权人分布

来源：[DEBT.PT — Sovereign debt and private credit in Portugal, 1640–1800](https://debt.pt/)（PTDC/HARHIS/28809/2017），官方 [Documentation](https://debt.pt/pdf/DOCUMENTATION.pdf)，以及[Palma–Reis 2019作者GDP](https://doi.org/10.1017/S0022050719000056)。**全套原始工作簿仅提供官方链接与SHA-256，不在本公共仓库重新发行二进制源文件或原始具名债权记录。** 详见 [DEBT.PT审计报告](../DEBTPT_PRIMARY_DEBT_COFFERS_CREDITORS_AUDIT_M2_20261114.md)。

| 新文件 | 内容与边界 |
|---|---|
| [debtpt_annual_debt_gdp_ratios_1641_1800_m2.csv](debtpt_annual_debt_gdp_ratios_1641_1800_m2.csv) | **160年**(1641–1800)长期/可记录短期债务**存量**、偿付**流量**÷同年名义GDP的百分比；历史重建不等于完整现代国债普查 |
| [debtpt_decadal_annual_ratio_means_m2.csv](debtpt_decadal_annual_ratio_means_m2.csv) | **17个**十年时期的*年度比率简单均值*，1640s和1800s样本不足10年有明确标记；非十年总额比值 |
| [debtpt_creditor_categories_1641_1682_m2.csv](debtpt_creditor_categories_1641_1682_m2.csv) | **13类**原书债权人本金分布汇总（469债权人、700份juros），保留未分类占比；只代表1641–82样本，不可外推到1750年全部债权人 |
| [reproduce_debtpt_annual_ratios_m2.py](reproduce_debtpt_annual_ratios_m2.py) | 实际执行的Python标准库XLSX解析/核验程序；严格校验来源A与2019 GDP Excel各自SHA-256，输出连续160年债务率和偿付率，运行状态`PASS` |
| [sousa_2008_manifestos_5year_m2.csv](sousa_2008_manifestos_5year_m2.csv) | Sousa 2008原论文铸币局登记五年总黄金汇款17行；末期1800–1807 |
| [gold_manifestos_2008_vs_2025_reconciliation_m2.csv](gold_manifestos_2008_vs_2025_reconciliation_m2.csv) | 与2025 Table B.1逐期匹配，最后一期1800–07 vs 1800–04标记不能比，1780–84差额−1,726 contos |
| [sousa_2008_decadal_gold_private_public_m2.csv](sousa_2008_decadal_gold_private_public_m2.csv) | 2008 Table 2九组按十年公布公共/私人**年均**汇回金额，不能当作十年合计 |
| [sovereign_debt_2024_crosscountry_benchmarks_m2.csv](sovereign_debt_2024_crosscountry_benchmarks_m2.csv) | 2024论文Table1国债存量/GDP原始发表基准（荷兰指Holland省） |
| [sovereign_debt_service_2024_benchmarks_m2.csv](sovereign_debt_service_2024_benchmarks_m2.csv) | 2024 Table2偿付/国家**支出**，不是偿付/GDP或偿付/收入 |
| [audit_gold_sources_and_debt_m2.py](audit_gold_sources_and_debt_m2.py) | 已从当前GitHub分支**重新下载六个文件并执行EXIT 0**的历史表格算术审查器 |

### 原始来源版本清单（本轮实际下载）

- [A DEBT 1529–1557 & 1641–1800.xlsx](https://debt.pt/pdf/DEBT_%201529-1557%20%26%201641_1800.xlsx)：45,111 B；SHA256 `b2024474a20442b5577ca4667067edf22ffdf71a30faad01971f5a8d13104d17`。
- [B FISCAL COFFERS](https://debt.pt/pdf/FISCAL%20COFFERS_%20debt%20service%201529-1557%20%26%201641_1800.xlsx)：35,399 B；SHA256 `48727613d6463b990842b7098a5b5c25aeaf9235ced3bb142634b591af5b6850`。
- [C CREDITORS](https://debt.pt/pdf/CREDITORS%20_%201641_1683.xlsx)：78,444 B；SHA256 `5e277c7f512babefa5427ec5995946e6cb91ecd9a13f447b82a3c55df452b667`。
- Palma/Reis作者GDP XLSX 83,313 B；SHA256 `ee80439059ebfa3f67f870430671098fe6c853000be64d2605111285ee63045c`。

### 复算160年比率

```bash
python3 reproduce_debtpt_annual_ratios_m2.py \
  --source-debt-xlsx /local/path/DEBT_PT_A.xlsx \
  --source-gdp-xlsx /local/path/palmareis_JEH_2019.xlsx \
  --output /tmp/portugal_1641_1800_debt_gdp.csv
```

官方工作簿A的`Debt stock!D/E/F`与`Debt service!D/E/F`单位réis；GDP H单位百万réis，分母必须乘100万。`PASS years=160 stock_err=0 service_err=0`，派生CSV SHA256 `bdda94a8ce33f806f5adf10b23472ded1d1c68c8de12c59509f04b48e3a905ea`。2024债务论文1748年9%与该版本复算8.15225%存在**待核验来源分母冲突**。**ASCM模型NOT_RUN，国库年度总收入与军费面板NOT_ACQUIRED**。


## M2 2024财政能力 × DEBT.PT债务偿付 × 2008/2025黄金流量

| 新增文件 | 核验与口径 |
|---|---|
| [fiscal_revenue_with_without_empire_2024_table3_m2.csv](fiscal_revenue_with_without_empire_2024_table3_m2.csv) | 同行评审2024论文Table3，3个半世纪分期含/不含帝国中央收入/GDP，**作者分期基准重建**，不提供年度收入值 |
| [fiscal_revenue_vs_debt_service_periods_m2.csv](fiscal_revenue_vs_debt_service_periods_m2.csv) | 上述公开分期收入指标 vs DEBT.PT逐年偿债/GDP在对应50年的**算术平均**，最后一列是**两种分期概括比率之比，非真实“偿债占国家收入”** |
| [public_gold_vs_debt_service_matched_periods_m2.csv](public_gold_vs_debt_service_matched_periods_m2.csv) | 1720–49、1750–79和1780–99按**同年份及同单位百万réis**汇总2025 TableB1公共黄金及DEBT.PT债务偿付金额；附以Sousa2008修订敏感性 |
| [reproduce_fiscal_capacity_gold_debt_bridge_m2.py](reproduce_fiscal_capacity_gold_debt_bridge_m2.py) | **实际运行通过的**版本锁定程序，需分别从DEBT.PT和Palma–Reis作者官网下载源XLSX，读取本仓库历史短表并再生两份CSV |

报告：[帝国净财政贡献与公共黄金/债务偿付审计](../FISCAL_CAPACITY_GOLD_REMITTANCES_DEBT_SERVICE_BRIDGE_M2_20261114.md)。2024 fiscal Table3 DOI https://doi.org/10.1093/ereh/heae003；作者Footnote9说明帝国贡献扣除帝国相关费用，但该口径并非全部殖民长期经济净回报。运行输出CSV SHA-256：`8766845fc79226c7a84d79d0c215fe94283d4e786ddd57122126a0a52aeb6a8a`、`5c22f41dc7106590c36061f939af2f6363063193d6dfe8aea4fe972de1abb57e`。严格标注：财政研究完整年度原始收入/支出 **NOT_ACQUIRED**；1694黄金ASCM模型 **NOT_RUN**；1748债务率发表冲突 **OPEN**。


## M2后续｜财政附录A1真实日期基准、黄金税率制度和1748局部版本敏感性

数据源：Costa–Henriques–Palma (2024)官方在线Appendix（[OUP主文与Appendix入口](https://academic.oup.com/ereh/article/28/4/453/7667247)），不是ICPSR198143完整运行数据；DEBT.PT年度偿付来源的原始A XLSX已SHA锁定。

| 新文件 | 内容／口径及实际检查 |
|---|---|
| [fiscal_nominal_revenue_benchmarks_appendix_a1_2024_m2.csv](fiscal_nominal_revenue_benchmarks_appendix_a1_2024_m2.csv) | 官方附录Table A1 **36行**1367—1844年名义中央收入（contos）和原参考文献；其中1762–1777、1834–1844均属时期年均值，不是某个“年度实收” |
| [brazilian_gold_tax_institutions_appendix_a2_2024_m2.csv](brazilian_gold_tax_institutions_appendix_a2_2024_m2.csv) | 附录A2 **五阶段**黄金税制（`quinto`、`capitação`交替），显式保留1735–1751与1750-12-03改革日期文字重叠疑点 |
| [fiscal_a1_explicit_years_vs_debt_service_m2.csv](fiscal_a1_explicit_years_vs_debt_service_m2.csv) | 可按确切日期匹配的**7行**1645、1656、1660、1681、1716、1730和1762–1777均值；所得比率不等于所有国库年度收入／全部债息口径 |
| [debt_1748_published_vs_current_source_window_m2.csv](debt_1748_published_vs_current_source_window_m2.csv) | **15行**1743—1757年版本锁定的债务/GDP；2024 Table1 1748=9与复算1748=8.152251无法用通常整数取整解释，未验证的原因仍OPEN |
| [reproduce_fiscal_a1_debt_service_m2.py](reproduce_fiscal_a1_debt_service_m2.py) | 实际在研究Runner下载源DEBT.PT A及GitHub文件重新执行，`PASS appendix_a1_rows=36 matched_revenue_entries=7 debt_local_window=15 year1748_table_conflict=OPEN` |

详情：[官方财政附录日期级审计](../FISCAL_A1_DATED_BUDGETS_1748_DEBT_VERSION_AUDIT_M2_20261114.md)。源原始DEBT.PT未镜像；两个生成CSV的SHA-256：`c9f97912cf00d876868450d956ca41634f653f721f119fade21f588dae507881`，`616dff3b7361257124c35aab6e2e0c38a16718675498f1625929edcb8e5067af`。**严格财政因果识别／ASCM均NOT_RUN**。


## 候选M3增量：DEBT.PT年度存量变化与净发行的账务质量审计（2026-11-14）

| 文件 | 数据、单位、历史与核验边界 |
|---|---|
| [debtpt_issuance_vs_stock_delta_1642_1800_m3.csv](debtpt_issuance_vs_stock_delta_1642_1800_m3.csv) | **159行**相邻年度DEBT.PT `Debt stock` D/E/F/H/I，单位百万名义réis；记录存量变化、`juros`净发行、短债净发行、残差及0.01百万réis阈值异常标记 |
| [debtpt_1740s_net_issuance_comparison_m3.csv](debtpt_1740s_net_issuance_comparison_m3.csv) | 4组十年净长期债务发行、短债净发行与存量变化的对照；1743年占1741–50长期净发行53.430639%，非总财政收入占比 |
| [reproduce_debtpt_issuance_stockflow_m3.py](reproduce_debtpt_issuance_stockflow_m3.py) | 已实际执行：严格验证官方原始DEBT.PT A Excel SHA256，逐年唯一/连续及长期+短债存量的算术一致性，**不假设整个159年Δ存量=发行**，显式保留1640—1660年代20处发行/存量残差；生成两份派生CSV |

官方DEBT.PT A源：https://debt.pt/pdf/DEBT_%201529-1557%20%26%201641_1800.xlsx；源SHA-256 `b2024474a20442b5577ca4667067edf22ffdf71a30faad01971f5a8d13104d17`；生成全年CSV SHA256 `ff06b830cc0106eb7c82a8d14e2047f1c0df0144c43cc164e539278cdd88e604`，四组十年CSV SHA256 `477c18897359e5970ec72ea633a8e39018518ce029fbb92a3e3ec28a4e01eaf9`。同源净发行数据只是历史债务会计记录，**不是独立证据证明巴西黄金实际支付了当年发行的现金**。完整报告：[1743年发行与债务存量/发行时间错位审计](../DEBT_1743_ISSUANCE_STOCKFLOW_ACCOUNTING_AND_1748_SOURCE_CONFLICT_M3_20261114.md)。阶段仍为业务Issue #34 OPEN，Draft PR #38未合并。


## M3证据：1743降息债务转换与帝国税源抵押金库

| 新文件 | 可核查内容和限制 |
|---|---|
| [debtpt_selected_fiscal_coffers_debt_service_changes_m3.csv](debtpt_selected_fiscal_coffers_debt_service_changes_m3.csv) | 读取DEBT.PT官方B workbook `Long-term debt`原始工作表八个特定金库；J/K是1722—1761**净债券数量/偿付余额变化**，M/N是1762—1800净变化，不是累计税收或1743单年度账目 |
| [reproduce_debtpt_colonial_coffers_m3.py](reproduce_debtpt_colonial_coffers_m3.py) | 源哈希锁定、按原始工作表行号核验的标准库复算器；**已实际执行PASS selected_coffers=8**，源行32包含`1% tax on gold from Brasil after 1716`且J=516、K=50.983813百万réis；不对八个来源无条件加总 |
| [juro_1743_1749_debt_conversion_evidence_m3.csv](juro_1743_1749_debt_conversion_evidence_m3.csv) | 精确日期、1947年历史著作原文引用与1752年Pombalina馆藏定位，以及2021/2024转述的**旧债转移≈5,000 contos**；它不等于DEBT.PT 1743净新增≈507.943 contos，更非新现金净流入 |

完整研究报告：[1743年降息/宗主教座堂转债与殖民黄金税偿债金库](../1743_JUROS_CONVERSION_GOLD_EARMARKED_COFFERS_PROVENANCE_M3_20261114.md)。官方B XLSX网址 https://debt.pt/pdf/FISCAL%20COFFERS_%20debt%20service%201529-1557%20%26%201641_1800.xlsx；源SHA256 `48727613d6463b990842b7098a5b5c25aeaf9235ced3bb142634b591af5b6850`；8行派生CSV SHA256 `d7285cf22af3716211f2ed12cf62bb4d7009c319fcd92b2e2a45c696316429c5`。底层法律/1752手稿以及直接券级新融资证据仍`NOT_ACQUIRED`，不应视为已完成殖民财富→财政收入→产业损失因果链。


## M3补充｜AHU债券手稿目录及Misericórdia一二级市场审计（2026-11-14）

| 文件 | 内容及证据等级 |
|---|---|
| [archival_locator_juro_cash_financing_1743_1753_m3.csv](archival_locator_juro_cash_financing_1743_1753_m3.csv) | **9条**精确法令/账簿/档案目录：AHU Cod.2003（1743–1753宗主教座堂/海外委员会）、Cod.491（1742–1752印度战争商人融资）、1744-08-29补偿性债券（AHU_CU_Reino Cx.125 pasta32）、1753-06-14殖民管辖权换债（Cx.60 pasta65），及葡萄牙财政部历史债券目录、旧法令和晚期慈善会真实收息账簿；**所有未读的历史手稿仍`NOT_ACQUIRED`** |
| [validate_archival_locator_and_cash_claims_m3.py](validate_archival_locator_and_cash_claims_m3.py) | **实跑PASS**：9条来源ID不重复，日期/URL合法，档案原件未取得时不可宣称已读取，标明1744/1753为非现金法律对价；只是元数据QA而不是原始档案验证 |
| [reproduce_juro_primary_secondary_2019_m3.py](reproduce_juro_primary_secondary_2019_m3.py) | Lisbeth Rodrigues (2019) Table5的**日期、金额、是否交给王室国库**的有限转录及统计核算；20笔中19笔有本金，源论文对照[DOI](https://doi.org/10.4000/lerhistoria.4730)，CC BY-NC 4.0署名，未镜像论文或全部买卖私人记录 |
| [misericordia_2019_bond_primary_secondary_reconciliation_m3.csv](misericordia_2019_bond_primary_secondary_reconciliation_m3.csv) | **7项**作者表4和表5会计口径对照：已知19笔本金179.853941 contos，五笔国库直付106.773748、已知14笔二级市场73.080193；Table4发表总额195.509941，`Table4-Table5_known=15.656000` contos为**未对平源差**；不能把缺项直接填成差额。

研究报告：[1743—1753债券档案与1775后国债/私人信用分配](../AHU_1743_1753_BOND_MANUSCRIPTS_NONCASH_ISSUANCE_AND_2019_CREDIT_ALLOCATION_M3_20261114.md)。2019复算CSV SHA256 `9aa0202054679039f4fadd783b4c67ad2037589e910928ae02d7683b27ba5236`。官方AHU两册的**手稿未读/目录原版访问受阻**；第三方目录镜像与作者复现不视为原始凭证。1775年禁贷有1768先行限制、1769私人放贷已停止、1755地震及坏账等混杂因素，`CAUSAL_EFFECT_NOT_RUN`。


## M3附加审计：黄金繁荣前糖税/海关抵押 + 1760年代王室金储备和国内借贷

| 文件 | 内容及审计边界 |
|---|---|
| [pre_gold_tax_collateral_1743_1749_1750_edict_coinage_source_audit_m3.csv](pre_gold_tax_collateral_1743_1749_1750_edict_coinage_source_audit_m3.csv) | **9条史实/出版文本主张**：1647年商业借款20万cruzados与糖税抵押、1662年步兵融资、1704–06年480contos海关收入抵押、1743降息与1743–44铸币4,196contos/旧债处理5,000contos、**1749 vs 1750年3月16日**降息法规日期来源冲突；**1704–06这笔具体贷款利率未确认** |
| [validate_pre_gold_credit_collateral_and_edict_dispute_m3.py](validate_pre_gold_credit_collateral_and_edict_dispute_m3.py) | 实际运行`PASS rows=9`：逐条审查货币单位、出版来源、税源范围、1775之前债务传统及法律日期两种主张；绝不把铸币和旧债转移当可相抵的财政现金流 |
| [sousa2003_1763_1798_treasury_gold_mint_deposit_loans_m3.csv](sousa2003_1763_1798_treasury_gold_mint_deposit_loans_m3.csv) | Sousa(2003)公布的**8条**1763/1766国家铸币、1763/1765/1767国库金币持有存量、1766→1777公共存款贷款未偿余额、1777全部借款人未偿额、1798国库借款报告量，源作者引用ANTT Ministerio do Reino具体馆藏盒号，**未直接调阅原始手稿** |
| [validate_sousa2003_treasury_royal_mint_deposit_loans_m3.py](validate_sousa2003_treasury_royal_mint_deposit_loans_m3.py) | 实际运行`PASS rows=8`：校验**371.4/673=55.2%**，保留1765/1767未知月日、贷款/黄金存量对铸币年度流量的不相容性，1798记录数额不视为当年新增贷款 |

研究报告：[1743铸币/旧债、前黄金糖税和1760年代国库流动性跨档案核查](../PRE_GOLD_CREDIT_COLLATERAL_1743_COINAGE_1760S_TREASURY_LIQUIDITY_AUDIT_M3_20261114.md)。来源：1841 [《O Panorama》印刷148页](https://hemerotecadigital.cm-lisboa.pt/obras/opanorama/1841/N210/N210_master/N210.pdf)和[2003年Sousa原论文印刷788—790页](https://revistas.rcaap.pt/analisesocial/article/download/35368/24541/156638)。两份CSV来源文件SHA256分别是`326a50d242e0450ca0dfad2efcfb6b95bad9a72d2d1ded7e6dab9a2c37739d0a`、`360172f1baf149a4c84d63e48c281e8bffbcd18d44d17f5ec8a67dda052e6219`。**原始贷款契据、国库现金流水、降息法令原件和ICPSR因果复现仍NOT_ACQUIRED/NOT_RUN**。


## M3资料取得再升级｜审计法院官方1763—1777年原始国库账簿卷号和1765会计重建

| 新文件 | 真实来源与审计边界 |
|---|---|
| [ahtc_1763_1777_treasury_original_ledger_requisition_inventory_m3.csv](ahtc_1763_1777_treasury_original_ledger_requisition_inventory_m3.csv) | **21条**官方1977历史账簿检索号：**10册**指定半年收入/支出总账、**6册**现金簿、**5册**命令/税收欠款/士兵旧欠饷账。属于**官方档案目录元数据**，不是已经取得对应手稿原件；2024移库后当前`cota`待馆方核实 |
| [treasury_1765_cash_accounts_vs_gold_coin_stock_provenance_m3.csv](treasury_1765_cash_accounts_vs_gold_coin_stock_provenance_m3.csv) | **7条**2019 Rodrigues博士论文原文1765年复式记账重建与2003 Sousa国库黄金记录：`two Caixa accounts 2765 contos`与`gold coins 76.8 contos`不属于同日同实体可直接对账的统计；**会计收益2690≠财政余额或税收**，发表约数的1 conto残差不得伪称底账错误 |
| [validate_ahtc_ledger_requisition_and_1765_cash_specie_scope_m3.py](validate_ahtc_ledger_requisition_and_1765_cash_specie_scope_m3.py) | 实际运行`PASS AHTC_archival_locator_rows=21 ... ACCOUNT_AND_ASOF_NOT_COMPARABLE ... original_manuscripts=NOT_ACQUIRED`，审查历史账簿编号、来源访问状态和库存/流量不同口径 |

官方馆藏目录：[AHTC Inventário (1977)](https://erario.tcontas.pt/pt/arquivo_biblioteca/instrumentos_pesquisa/Inventario_Adenda_Erario_Regio.pdf)（216页，SHA256 `fd31975695bfbc0c5299e5eed2dda24c6b21c976eadd43528e7ff79baaef6739`）；[馆藏机构与预约状态](https://www.tcontas.pt/pt-pt/TribunalContas/ArquivoBiblioteca/Paginas/Arquivo-e-Biblioteca.aspx)：2024移存ANTT，联系`dadi@tcontas.pt`申请原件查看或数字副本；[2019 Rodrigues博士论文](https://repositorio.iscte-iul.pt/bitstream/10071/19808/1/PhD_Manuel_Benavente_Rodrigues.pdf) 339页，SHA256 `ca8b83728950b1746440baad2ac522b9dd5010f4237ebb5a8a6e3b6c528b565e`。两份派生CSV SHA256：`32d4458e84298ac6772cc22d3ba9a73409c1d0c92907fba851fbea3d35d40150`、`c5b1a40a0626d9700f65198eddef0054bb92e1d97019f9327cac9f914f4992ac`。完整报告：[国库原始账簿卷号及1765现金与金储备不同口径审计](../AHTC_1763_1777_ORIGINAL_TREASURY_VOLUME_MAP_1765_CASH_VS_GOLD_SCOPE_M3_20261114.md)。


## M3 1765年四个Contadorias：发表收入/战争结转/税源统计口径及同作者版本审计

| 新文件 | 可重复核对的信息与限制 |
|---|---|
| [rodrigues2019_1765_royal_treasury_revenue_expense_war_m3.csv](rodrigues2019_1765_royal_treasury_revenue_expense_war_m3.csv) | 2019 Rodrigues大学博士论文Table5.7 **10类**账面收入、Table5.3 **6类**账面费用、Table5.5 **6类**战争费用子项，共22行；总额恰好满足收入-支出=收益；战费为军事支出内部**子集**且涉及1762战事的迟延记账，不能另行加到支出合计 |
| [rodrigues2019_1765_revenue_collection_vs_origin_region_m3.csv](rodrigues2019_1765_revenue_collection_vs_origin_region_m3.csv) | 2019原文Table5.9/5.11 4个地区，税收在征收地海外约15.6857%、商品原产地重分类海外约55.8579%；出版地区重分类收入和报告总计有**70,000 réis残差**，不可擅自填补 |
| [rodrigues_1765_master2011_vs_phd2019_account_edition_audit_m3.csv](rodrigues_1765_master2011_vs_phd2019_account_edition_audit_m3.csv) | 2011硕士Table3.33 vs2019博士Table5.1 5项对照；4项精确借方/贷方/前期收益/当期收益一致，两类`Caixa`合计却分别写**359.525124 contos**和**约2,765 contos**，现金范围或修订原因未证实 |
| [reproduce_1765_royal_treasury_fiscal_functional_bridge_m3.py](reproduce_1765_royal_treasury_fiscal_functional_bridge_m3.py) | **真正执行通过**的标准库整数réis检查脚本：22行分类、4区域、2版本、战争费子集、内部会计两条恒等式、70,000 réis地区源差及现金版差必须显式保留 |
| [rodrigues1765_royal_treasury_derived_fiscal_identity_m3.csv](rodrigues1765_royal_treasury_derived_fiscal_identity_m3.csv) | 程序实际生成的16项会计总额、比例、来源口径与未决冲突状态；**非AHTC原始手稿逐笔审计** |

大学公开原文：[2011年硕士PDF](https://repositorio.iscte-iul.pt/bitstream/10071/4540/1/Tese%20Manuel%20Jos%C3%A9%20Benavente%20Rodrigues.pdf) SHA256 `533d24ceb52b53a4e8994f1a72739b04feb36f162304a3f28c13173f6bd7b3e5`；[2019年博士PDF](https://repositorio.iscte-iul.pt/bitstream/10071/19808/1/PhD_Manuel_Benavente_Rodrigues.pdf) SHA256 `ca8b83728950b1746440baad2ac522b9dd5010f4237ebb5a8a6e3b6c528b565e`。已真实复算的16指标派生CSV SHA256：`1141284907ff7149b9bf20f25a785292c100854b36701de19847818add81a138`。研究全文：[1765年收入、战争支出、税收地域与现金账两个版本审计](../RODRIGUES_1765_ACCOUNTING_WAR_ARREARS_TAX_ORIGIN_2011_2019_CASH_AUDIT_M3_20261114.md)。下一原始目标：AHTC FGER Livros Mestre 537、2699、3976、4154，尤其2699 fólio 10对应的1765军费结转和`Caixa`原页。文件中的手稿`NOT_ACQUIRED`，2025黄金ASCM`NOT_RUN`。


## M3来源继承与1766军费旧账结转（2026-11-14）

| 文件 | 来源、真实验证及限制 |
|---|---|
| [rodrigues_1765_regional_reclass_2011_2019_persistent_70k_m3.csv](rodrigues_1765_regional_reclass_2011_2019_persistent_70k_m3.csv) | **8条**2011 Table3.31 vs2019 Table5.9四地区双口径收入逐数比较：两版源行一致、原产地重分类合计各比公布总数少**70,000 réis**，不能把两版算作独立原账验证或自行增补某一地区 |
| [rodrigues2019_1765_1766_first_contadoria_account_rollover_m3.csv](rodrigues2019_1765_1766_first_contadoria_account_rollover_m3.csv) | **8条**2019 Table4.5第一Contadoria余额及损益累计借贷：1765/1766损益累计借方**441/4080 contos**，会计结账受1762—66军费既有财务官约**1564 contos旧账转款**影响，不能当作国家年度战争现金支出 |
| [reproduce_1765_1766_archival_account_rollover_and_editions_m3.py](reproduce_1765_1766_archival_account_rollover_and_editions_m3.py) | 标准库QA脚本，实跑PASS验证**70,000 réis跨版本继承**、8条余额、1564 contos历史叙述的来源和非现金警告；档案手稿并未实际取得 |
| [rodrigues_1765_1766_edition_and_war_rollover_summary_m3.csv](rodrigues_1765_1766_edition_and_war_rollover_summary_m3.csv) | **11项**派生量，发布SHA256 `acc4d0a70a243f053fee0dc650e10522db6b419930d6875677f840190cab6ad3`；需以标准库脚本与当前源CSV再构建验证；含非当期现金提示 |

完整分析：[1766财政军费历史旧账结转与1765地区税源表两版继承差异](../1766_MILITARY_TREASURER_ROLLOVER_2011_2019_REGIONAL_TABLE_LINEAGE_M3_20261114.md)。**最小档案获取目标**是AHTC/FGER **Livro537 fólio36和fólio274**；另一组军费账为**Livro2699 fólio10/15**。这些馆藏尚未获得原稿图像，不能声称已完成1762/1766实际现金流时间戳或资源诅咒ASCM复现。
