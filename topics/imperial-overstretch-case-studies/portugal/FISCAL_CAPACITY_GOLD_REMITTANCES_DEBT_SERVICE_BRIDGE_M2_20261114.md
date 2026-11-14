# CASE-PRT-001｜M2 帝国财政净贡献、黄金公共汇款与债务偿付的跨来源桥接

> 2026-11-14；权威 Issue [#34](https://github.com/fweiger/AI_book/issues/34)；现有 Draft PR [#38](https://github.com/fweiger/AI_book/pull/38)。状态：**PUBLISHED_FISCAL_PERIODS_RECONCILED / MATCHED_GOLD_DEBT_SCALE_REPRODUCED / REVENUE_ANNUAL_PANEL_NOT_ACQUIRED / ASCM_NOT_RUN**。该报告是公开历史重建材料的**描述性证据桥接**，不提供未经证实的帝国财政净ROI或1694黄金效应因果估计。

## 1. 关键新来源：2024年《Anatomy of a Premodern State》表3及财务定义

Costa, Leonor Freire, António Henriques & Nuno Palma (2024), *Anatomy of a premodern state*, **European Review of Economic History 28(4):453–474**, DOI: https://doi.org/10.1093/ereh/heae003 ，出版方 HTML https://academic.oup.com/ereh/article/28/4/453/7667247 ，里斯本大学开放版PDF https://repositorio.ulisboa.pt/bitstreams/038f2e91-c16f-4ff0-be74-da8edbd72ab2/download 。

Table 3给出历史**中央政府收入/名义GDP**的若干50年期间指标，分别为有/无帝国财政收入。作者**Footnote 9**专门说明本土财政收入按**gross national revenues（本土总收入）**，但帝国贡献以**在帝国相关费用支出后留给宗主国的净财政收入**计入。由此：
- `Net imperial fiscal increment`不等于黄金税总额、各殖民地营收合计、私人资金跨洋转移，也不等于“葡萄牙整个殖民帝国的财务净投资回报率”，因为该口径仅反映宗主国中央财政收入可用性，未合并长期机会成本/海外战略投资。
- **作者原文承认缺少完整连续年度收入序列**，依靠若干重建基准年份形成长期比较；Table 3结果不能反填成完整`1650–1799`每一年的真实预算。
- 2024财政研究的正式代码和数据包登记在 [ICPSR 198143](https://www.icpsr.umich.edu/sites/icpsr/view/studies/198143/versions/V1)，2026新平台实际可下载的原始年度文件尚**NOT_ACQUIRED**。本文不从图像逆造不存在的年度值。

新建表：[data_m2/fiscal_revenue_with_without_empire_2024_table3_m2.csv](data_m2/fiscal_revenue_with_without_empire_2024_table3_m2.csv)；作者发表比率：

| 50年分期 | 中央收入含帝国/GDP | 不含帝国/GDP | 发表指标差额 |
|---|---:|---:|---:|
| 1650–1699 | 2.2% | 2.0% | 0.2个百分点 |
| 1700–1749 | 5.2% | 4.1% | 1.1个百分点 |
| 1750–1799 | 4.7% | 3.6% | 1.1个百分点 |

两列差值是**公开呈现的一位小数**的差值，并非超过这个精度的真实测量，也不是各年“帝国收入比例”的算术平均。18世纪两个半世纪段的净帝国财政贡献均表现为约1.1个百分点，但作者正文显示在更细年份它发生显著变化，不能误称每年恒定1.1个百分点。

## 2. 同期DEBT.PT债务偿付/GDP：跨来源**分期比率的量纲对齐**

原始DEBT.PT A工作簿 `Debt service!F`（年份1641–1800、单位réis）以及 Palma–Reis（2019）`GDPs!H`（名义GDP百万réis）由上一阶段实际下载、版本锁定和复算，160行数据在 [data_m2/debtpt_annual_debt_gdp_ratios_1641_1800_m2.csv](data_m2/debtpt_annual_debt_gdp_ratios_1641_1800_m2.csv)。

新表 [data_m2/fiscal_revenue_vs_debt_service_periods_m2.csv](data_m2/fiscal_revenue_vs_debt_service_periods_m2.csv) 明确使用**同一个50年分组**，对160年年度`debt_service/GDP`取各段50个百分比的**算术平均**，并与2024发表的分期`central revenue/GDP`并列：

| 时间 | 发表中央收入含帝国/GDP | 年度债务偿付/GDP的50年算术平均 | **解释性**两种分期比率之比 |
|---|---:|---:|---:|
| 1650–1699 | 2.2% | 0.445916% | **20.27%** |
| 1700–1749 | 5.2% | 0.422072% | **8.12%** |
| 1750–1799 | 4.7% | 0.457349% | **9.73%** |

**极重要的审计禁令：最后一列不是实际“债务偿付占国库年度收入的比重”。** 它只等于`mean(annual debt service/GDP)/published period revenue/GDP`：公开收入是历史基准点汇总并经**一位小数取整**，而DEBT.PT债务偿付是另一个来源的160年重建，二者**不同样本、可能不同时间权重、覆盖范围和误差分布**。不能把计算结果写成精确的债务偿付/收入。也不能把它冒充2024债务论文Table 2的**偿付占国家支出**（1680=22.9%，1766=7.6%），因为后者的分母是国家**支出**而不是收入或GDP。

解释：在这些版本锁定的长期平均材料上，1700–99的债务偿付/GDP约0.42%–0.46%，相较含帝国中央收入/GDP约4.7%–5.2%并非大到支持无条件的“国债利息吞没大部分财政能力”的叙述。然而这**不能证实财政挤出不存在**，因为未观察到战争时段的财政现金流/滚动贷款/逾期及海外战略支出反事实。

## 3. 1720—1799：同一名义货币、同一时间窗口的黄金公共汇款对已记录债务偿付

这里不使用分期重建收入，而是严格对接**真实年别**：

- 分子：Kedrosky & Palma (2025) 官方 Supplement Table B.1 的私人/公共名义黄金汇款，单位`百万réis`，每个五年块是该段累计汇款。
- 分母：DEBT.PT A `Debt service!F` 的**逐年名义réis**，按照完全对应的30/20年累计后÷100万转成百万réis。
- 同时将Palma–Reis 2019 `GDPs!H` 的年名义GDP（百万réis）逐年累计作量纲控制。
- 数据清单：[data_m2/public_gold_vs_debt_service_matched_periods_m2.csv](data_m2/public_gold_vs_debt_service_matched_periods_m2.csv)。

| 完全匹配时间 | 2025版公共黄金汇款（百万réis） | 已记录债务偿付（百万réis） | 公共黄金/债务偿付 |
|---|---:|---:|---:|
| 1720–1749（30年） | 26,973 | 12,372.994 | **218.00%** |
| 1750–1779（30年） | 26,690 | 15,434.742 | **172.92%** |
| 1780–1799（20年） | 4,933 | 10,737.258 | **45.94%** |

由同样窗口计算债务偿付/GDP分别是**0.462838%**、**0.486924%**、**0.410266%**；公共黄金汇款/GDP分别为**1.008983%**、**0.841997%**、**0.188488%**。**最后一段只有20年，不能用原始累计金额与前30年作横比**；这里跨期强调的是相同窗口内两种流量的比例。

**1780年代已知来源冲突的稳健性**：

Sousa (2008), *Brazilian Gold and the Lisbon Mint House (1720–1807)* Table 2公布十年期公共汇款**每年平均**（整数contos）。先以各十年平均×10形成**近似十年累计**，在同一分期对照：
- 1720–1749：2008版约**26,890**，公共黄金/同段债务偿付**217.33%**（2025版218.00%）；
- 1750–1779：2008版约**26,030**，比例**168.65%**（2025版172.92%）；
- 1780–1799：2008版约**6,660**，比例**62.03%**（2025版45.94%）；相差**1,727 contos**，与此前识别的1780–1784年公共类别差异对应。

**含义**：两个出版版本都显示晚期黄金公共汇款相对债务偿付显著下降，且1780–1799年比例仍不足100%；但2008年十年平均**已四舍五入**，而2025年5年汇款原表的分类可能经修订，不能将2008的近似累计当作未舍入的独立主账。未取得2013书`O Ouro do Brasil`及1780–84铸币局具名底账，因此版本原因仍`SOURCE_CONFLICT_OPEN`。

### 重要：规模关系≠账目资金追踪

本节**并不声称这些黄金专门被用于偿债**，也没有证明王室发生了现金流缺口：
1. 公共黄金汇款是在巴西端可能扣除部分地方军政费用后汇抵里斯本的类别，不能直接等同全帝国税收净额。
2. 2024财力表“净帝国收入”包含多来源、不同分期与费用口径；既**不能用2025公共黄金代替2024净帝国收入**，也不能将两者直接相减当作非黄金殖民利润。
3. DEBT.PT `debt service`包括长期与可观察/重建短债偿付，不等于“纯利息”；债务结清与偿付时点可能与黄金到港不一致。
4. 国家内地税、海关、地方金库、现金储备、再借债等资金还需要独立账户；本研究没有做历史记账分录追踪。
5. 单纯规模比例下降的同时人均GDP也可能下降，**不能由同向变化确证黄金/财政对工业化的因果影响**，更不能当作2025论文ASCM的独立复现结果。

## 4. 可复核程序、下载和状态

本轮新增可独立运行的源版本锁定程序：[data_m2/reproduce_fiscal_capacity_gold_debt_bridge_m2.py](data_m2/reproduce_fiscal_capacity_gold_debt_bridge_m2.py)。需要在同一目录内保留Github前述年度债务CSV、2024 Table3小表、2025 Table B.1黄金表、2008 Table2十年均值表，并从**官方站点自行下载**DEBT.PT A与2019作者GDP两个Excel文件。

运行：
```bash
python3 reproduce_fiscal_capacity_gold_debt_bridge_m2.py \
 --debt-xlsx /path/DEBT_PT_A.xlsx \
 --gdp-xlsx /path/palmareis_JEH_2019.xlsx \
 --source-dir ./data_m2 \
 --output-dir /tmp/case-prt-fiscal-bridge
```

- DEBT.PT A来源SHA-256：`b2024474a20442b5577ca4667067edf22ffdf71a30faad01971f5a8d13104d17`；
- Palma–Reis 2019作者Excel来源SHA-256：`ee80439059ebfa3f67f870430671098fe6c853000be64d2605111285ee63045c`；
- **实际运行PASS**，`published_table3_periods=3 matched_gold_periods=3 ratio_definitions=EXPLICIT`；
- 输出`fiscal_revenue_vs_debt_service_periods_m2.csv` SHA-256：`8766845fc79226c7a84d79d0c215fe94283d4e786ddd57122126a0a52aeb6a8a`；
- 输出`public_gold_vs_debt_service_matched_periods_m2.csv` SHA-256：`5c22f41dc7106590c36061f939af2f6363063193d6dfe8aea4fe972de1abb57e`。
- 本轮以 GitHub raw 下载当前分支**全部脚本、源CSV及两个公共Excel**，在只读临时目录实际执行后，将两份输出的原始字节提交回同一分支。脚本输出不是凭图手填；但仍然**无法独立验证原始史料各项分类的历史真实性**。

**仍未取得**：新ICPSR 198143的2024财政研究正式可运行年度输入；ICPSR 209481的2025黄金ASCM代码及输入；2024债务论文1748=9% vs DEBT.PT当前锁定版本≈8.15225%口径差异；2013铸币局黄金1780年代公共分类更正依据；原始王室完整收入/军费/债务现金账。以上分别记`NOT_ACQUIRED / SOURCE_CONFLICT_OPEN / NOT_RUN`。

## 5. 跨Agent下一步可证伪工作

优先获取**ICPSR 198143**财政研究的实际输入/代码与确切基准财政年份，重新计算 Table3 的发表平均与**真实年度国家支出/债息份额**；由此决定该报告的“分期均值比率”可否升级为原始财政会计恒等式。另以`1748 debt stock 8.15 vs published 9`核对DEBT.PT修订及历史GDP分母版本。2025黄金ASCM 209481单列为另一个尚未完成的因果复现实验。Draft PR #38保持OPEN/DRAFT，不合并main。
