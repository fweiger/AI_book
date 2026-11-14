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
