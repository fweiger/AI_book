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
