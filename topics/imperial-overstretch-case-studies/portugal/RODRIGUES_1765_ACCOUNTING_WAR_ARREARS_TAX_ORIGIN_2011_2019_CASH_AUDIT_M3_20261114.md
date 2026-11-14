# CASE-PRT-001｜M3 1765年王室国库收入—军事支出精确恒等式、税款征收地与商品来源地双口径、2011/2019现金余额冲突审计

> 研究日期：2026-11-14；唯一权威业务Issue：[AI_book #34](https://github.com/fweiger/AI_book/issues/34)；沿用既有[Draft PR #38](https://github.com/fweiger/AI_book/pull/38)；分支`topic-010/case-prt-001-portugal-20261114`。  
> 状态：**PUBLISHED_1765_REVENUE_SPENDING_ACCOUNTING_IDENTITIES_EXACT_PASS / 1762_WAR_COSTS_BOOKED_IN_1765_NONCAUSAL / REGION_RECLASSIFICATION_PRINTED_70K_REIS_RESIDUAL_OPEN / 2011_VS_2019_CAIXA_BALANCE_SCOPE_CONFLICT_OPEN / ORIGINAL_AHTC_LEDGER_SCANS_NOT_ACQUIRED**。本轮取得并核对两版同一作者公开论文，不是已取得AHTC底层手稿或真实年度全王国现金预算。

## 1. 本轮确实取得的独立历史发表材料：同一研究者的2011及2019两版，而不是两组独立样本

核心研究：Manuel José Benavente Rodrigues，*O erário régio e as contas do reino no ano de 1765: o poder e a contabilidade*，2011年ISCTE历史学硕士论文，学校[公开原文PDF](https://repositorio.iscte-iul.pt/bitstream/10071/4540/1/Tese%20Manuel%20Jos%C3%A9%20Benavente%20Rodrigues.pdf)，本轮实际从大学仓库取得**156页、21,217,438 bytes、SHA256 `533d24ceb52b53a4e8994f1a72739b04feb36f162304a3f28c13173f6bd7b3e5`**。

后续扩展研究：**同一作者**，*O Erário Régio: as contas e o poder 1762–1833*，2019年ISCTE博士论文，学校[公开原文PDF](https://repositorio.iscte-iul.pt/bitstream/10071/19808/1/PhD_Manuel_Benavente_Rodrigues.pdf)，本轮实际重新取得**339页、17,464,337 bytes、SHA256 `ca8b83728950b1746440baad2ac522b9dd5010f4237ebb5a8a6e3b6c528b565e`**。

两版研究都直接以**AHTC, FGER, Livros Mestre nº 537, 2699, 3976, 4154**为1765年四个`Contadorias`总账的原始史料。原作者读过底账并重建历史账目，**本项目尚未调阅原始四卷**。这四本`Livros Mestre`与前轮AHTC官方1977目录中`Tesouraria-mor receita/despesa vols 5–10`及现金簿157–159是**不同档案系列/账册**，不准因为同年份便误认为同一卷次。

此轮《PDF》真实取证方式：可检索论文文本及关键表格金额经大学论文PDF文字层核查，2011原始PDF第101页、2019原始PDF第141、142、144–146、148、152–154页。网页图像截图通道返回cache miss，**不把截图检查虚报为通过**；所有来源对应学校原始文件URL及SHA，原PDF未镜像入公开GitHub。

## 2. 核心新增：1765精确账面收入与支出形成两个一致的会计等式

来源2019博士论文**Table 5.3（印页133/PDF145）**、**Table 5.7（印页136/PDF148）**、**Table 5.1（印页129/PDF141）**，所有金额原单位**réis**，本报告除标注`réis`外用contos＝百万réis。

```text
1765年财政登记的收入（Gain & Loss, credit）       4,427,192,621 réis
1765年财政登记的支出（Gain & Loss, debit）        1,736,357,637 réis
1765年会计净收益（非现金预算盈余）                  2,690,834,984 réis
```

**逐réis精确恒等式#1**：

`4,427,192,621 − 1,736,357,637 = 2,690,834,984`。

而两版论文的**1765年重建资产负债结转**又均报告：
`Deve/借方合计=17,725,700,642 réis`；`Haver/贷方合计=6,790,262,297 réis`；`先前年份累计收益=8,244,603,361 réis`。

**逐réis精确恒等式#2**：

`17,725,700,642 − 6,790,262,297 − 8,244,603,361 = 2,690,834,984`。

上一轮依据作者的**近似整数contos摘要**计算出1 conto偏差，本轮已从原文提供的精确réis数据**完全对平**：这属于`PUBLISHED_ROUNDED_1_CONTO_RESIDUAL_RESOLVED`。**不能把精确算术一致性等同于历史所有真实国库支票或所有全王国收入都已核验**；这里严格说是**出版研究表的内部会计一致性**。

## 3. 1765军事支出约占国库登记支出的59.66%，但主要与1762年战争旧账有关

**2019 Table 5.3（印页133）六类功能费用**：
- 军事（`Despesas Militares`） **1,035,933,367 réis**；
- 王室家用（Casa Real） **288,337,457 réis**；
- 外交（Negócios Estrangeiros） **60,592,623 réis**；
- 职员薪酬（Ordenados） **46,495,793 réis**；
- 布拉干萨家族（Casa Bragança） **35,716,840 réis**；
- 其他（Outras） **269,281,557 réis**。

六项恰好合计`1,736,357,637 réis`，军事比例**59.661290%**。

**Table 5.5（印页134）另从军事项里抽取六类与战争有关的已记录支出**，分别为Alentejo军需官554,723,270、城防建设241,436,971、Trás-os-Montes军需官61,014,934、Estremoz军需官59,000,000、陆军服装25,585,183、Alentejo炮兵军需官7,980,485 réis。**六项合计949,740,843 réis**，相当于全部登记支出的**54.697306%**，或军事项的约**91.6797%**；这949.74是**1,035.93军事金额的子集**，绝不能再加到支出总计上。

论文解释了极关键的**会计时点断点**：
- 1762年葡萄牙参与七年战争末期的军事动员，历史战事导致先前发生的费用；
- **1763-07-09**颁布法令撤销`Vedorias`（地方军事费用审计官机构）及既有战争`Contadorias`，职责转交`Tesouraria Geral das Tropas`；
- 相关账户后来被移入`Ganhos e Perdas`，因此1765年账上部分数额是**此前战争和组织改革的历史账务结转/清算**，不一定对应1765年新增费用或当期现金付款；
- 作者具体以**1765-12-31/1766-01-02**军需官账结转分录为例，引用**AHTC, FGER Livro 2699 fólio 10**（论文PDF第147页，印页135）。原账尚未由本项目取得。

**红队结论**：本轮可以说`1765年王室国库表列军事费用占所登记支出的约60%`，**不能说葡萄牙1765年实际军事现金流占全国财政60%，或因此挤出工业发展**。需要实际`1762—1766`的费用发生日、支付日、归属年度、收款人和旧账冲销分录才能支持财政挤出因果链。

新表：[data_m2/rodrigues2019_1765_royal_treasury_revenue_expense_war_m3.csv](data_m2/rodrigues2019_1765_royal_treasury_revenue_expense_war_m3.csv)：源论文Table5.7十类收入、Table5.3六类支出、Table5.5六类战争分项，共**22行**，各行标注表格、来源页、是否军事子集和原账未取得状态。

## 4. 黄金税只占1765登记收入10.44%，这不是整个殖民帝国贡献

2019 Table 5.7按**财政税种**对1765年登记收入进行十类分解，原值全部可查：

| 1765登记税收类别 | 数额（百万réis/contos） | 占同一出版收入总额 |
|---|---:|---:|
| 进出口海关与领事税（Alfândegas e consulados） | 1,161.952 | 26.25% |
| 烟草专营（Contrato Tabaco） | 893.275 | 20.18% |
| `Décima`直接税 | 706.724 | 15.96% |
| 黄金税（`Quintos do Ouro`） | **462.010** | **10.44%** |
| `Sisas` | 399.996 | 9.03% |
| 其他税目 | 803.232 | 18.15% |

表格中的黄金税462.009750 contos是**1765账面税项**，并非巴西年产矿金的20%、不是巴西政府所有财政收益、不是铸币额、不是公共黄金汇入量，也**不等同**2024 Costa/Henriques/Palma论文Table3的**宗主国净帝国贡献**。

更加重要的是，**同一研究显示大西洋商品烟草与糖的税源和专营收入不小于黄金税**。因此，“研究殖民财政”不能只追黄金税；但是否存在制造业挤出仍须单独验证。

## 5. 1765税源“征收地点”与“商品原产地”两种合法而截然不同的统计范围

2019 Table 5.9与5.11，作者将税款**实际入账/征收所在地**和**应税商品来源所在地**进行重分类。四个区域金额均已从PDF原表转录：

| 地区 | 按税款征收地（contos） | 按应税商品原产地重分类（contos） |
|---|---:|---:|
| 首都与Estremadura | 2,583.307 | 810.285 |
| 王国其它地区和海岛 | 1,149.449 | 1,143.902 |
| Rio de Janeiro、东非及亚洲 | 656.340 | 924.921 |
| 非洲、Maranhão和Bahia | 38.096 | 1,548.014 |

- 按税款收缴地区定义，后两区合计**694,436,065 réis**，占发表1765全体登记收入的**15.685698%**。
- 依作者把贸易税收重归于应税商品**原产地**的规则，后两区合计**2,472,935,291 réis**，约占**55.857865%**。
- 这并非从16%“增长”到56%的真实历史变化，而是**同一1765年在两个统计口径下的一次分类转换**。同时商品原产地≠宗主国净收益：若含有本土进口货物海关税，需另按源国及实际费用口径审查；这也不证明殖民地实际上承担了收入的全部经济税负。
- **新发现的印刷表格残差**：四个重分类收入原值合计**4,427,122,621 réis**，而作者在Table5.9和5.11旁边印出`总计=4,427,192,621 réis`，**相差70,000 réis，即0.07 contos**。两个位置显示一致的区域数值，仍不能确认是重分类输入漏项、历史原始簿错误还是发表排版/转录误差；本研究以`SOURCE_REGIONAL_RECLASS_70K_REIS_OPEN`**保留原值不修表**。四个地区在**征收地**的收入合计及两套支出合计均恰好与发表总额一致，残差仅出现在**收入来源地重分组**。

2019 Table 5.8用更宽泛的`Impostos ultramarinos`商品税种表，加总**2,775,711,513 réis≈62.69%**的相关类别，其中包括未逐项按商品原产地清理的`Alfândegas e consulados`大类。这是又一个**不同的原作者分类**：不能直接替换为Table5.9/5.11约55.86%，亦不能当作净殖民财政ROI。

新表：[data_m2/rodrigues2019_1765_revenue_collection_vs_origin_region_m3.csv](data_m2/rodrigues2019_1765_revenue_collection_vs_origin_region_m3.csv)，四行包括两套收入和两套支出、各统计法、表格来源及70,000réis误差。

## 6. 同一作者2011硕士与2019博士版共同的精确会计值，及现金账户重大悬案

2011硕士**Table3.33，PDF第101页／印页93**与2019博士**Table5.1，PDF第141页／印页129**：
- 借方合计 **17,725,700,642 réis**：**两版精确一致**；
- 贷方合计 **6,790,262,297 réis**：**两版精确一致**；
- 先前收益 **8,244,603,361 réis**：**两版精确一致**；
- 1765会计收益 **2,690,834,984 réis**：**两版精确一致**。

**而两版紧接着在解释两类`Caixa`现金账户余额时写法不一致：**
- 2011硕士正文明确写 `359 milhões 525 mil 124 réis`，即 **359.525124 contos**（有个位精度）；
- 2019博士正文写 `cerca de 2.765 contos`，即 **约2,765 contos**（近似金额）。

虽然4项精确的核心收益/资产负债数据一致，**现金余额表述却存在数量级差异，且均指“四个Contadorias、两类Caixa账户”**。不能简单称其已被2019版订正；可能涉及选取现金账户子集、净额对冲、期末与期间合计、复制错误或重建修订。**尚无能够证明其中任何一种原因的同账逐笔来源**。

**注意**：上轮Sousa2003的`1765黄金币余额76.8 contos`是第三个更窄的金属货币种类，且观察日期未明；绝不与上述2011/2019两种`Caixa`总额擅自形成连环比例。上述都来自不同源定义下的历史记账，**不能由一张表推出1765国家实际现金充裕或财政枯竭**。

版本核对表：[data_m2/rodrigues_1765_master2011_vs_phd2019_account_edition_audit_m3.csv](data_m2/rodrigues_1765_master2011_vs_phd2019_account_edition_audit_m3.csv)；原始四本`Livros Mestre`及对应`Caixa`页应成为下一阶段优先目标（在前轮已定位的Tesouraria-mor vols 5–10、Caixa 157–159之外）。

## 7. 源数据、标准库复算、真实验证及边界

本轮新增4个数据/代码主件与1个派生输出：
1. [rodrigues2019_1765_royal_treasury_revenue_expense_war_m3.csv](data_m2/rodrigues2019_1765_royal_treasury_revenue_expense_war_m3.csv)：22条源表分类；
2. [rodrigues2019_1765_revenue_collection_vs_origin_region_m3.csv](data_m2/rodrigues2019_1765_revenue_collection_vs_origin_region_m3.csv)：4个地区收缴地/商品来源地双视图；
3. [rodrigues_1765_master2011_vs_phd2019_account_edition_audit_m3.csv](data_m2/rodrigues_1765_master2011_vs_phd2019_account_edition_audit_m3.csv)：同一研究者2011/2019两版5个核对项目；
4. [reproduce_1765_royal_treasury_fiscal_functional_bridge_m3.py](data_m2/reproduce_1765_royal_treasury_fiscal_functional_bridge_m3.py)：**无第三方依赖**的精确`réis`整数核算程序；检查22条分类和战争费用包含关系、同一年两条会计恒等式、两类地域分类的70,000 réis残差，以及两版同作者`Caixa`争议；输入全部来自本仓库源表并附上学校原版论文URL；
5. [rodrigues1765_royal_treasury_derived_fiscal_identity_m3.csv](data_m2/rodrigues1765_royal_treasury_derived_fiscal_identity_m3.csv)：由上述程序**实际执行**生成的16项检验指标，含来源和禁止错误解释标识。

实际执行的程序从GitHub当前研究分支重新下载4项源代码/CSV运行**EXIT0**：
```text
PASS revenue=4427192621 expense=1736357637 gain_exact=2690834984
military_pct=59.661290 war_subset_pct=54.697306
overseas_collection_pct=15.685698 overseas_goods_origin_pct=55.857865
regional_total_printed_residual_reis=70000
2011_2019_Caixa_conflict=OPEN original_ledger=NOT_ACQUIRED
output_rows=16
```

派生16行CSV由程序生成并上传到现有GitHub分支，SHA256 **`1141284907ff7149b9bf20f25a785292c100854b36701de19847818add81a138`**，没有拿所谓历史底账的模拟输出冒充原始实测。**程序内的具体已发表金额属于手工核对后转录的研究源表，数字一致性不等于已逐笔审计1765四本真实原账。**

## 8. 研究机制的变化、阻断和唯一下一步

**研究已经从**`黄金下降 → 国债规模可能变化`**推进至**`1762军事活动 → 1763军事会计机构终止 → 1765历史战争支出进入国库损益账户 → 1765殖民税收入的征收地点 vs 贸易商品产地重新分类 → 王室公共信用与财政承诺`。

这一因果结构至少包含三个竞争解释：**真实黄金可用收入衰退**、**历史军事费用的迟后报销与计量时点**、**会计制度改革导致的账目覆盖和归属变化**。各解释并非互斥，仅凭1765一年的表不能识别哪一个占主要比重。

**下一项最低可验收目标**：确认并取得AHTC/ANTT原始`FGER Livros Mestre 537、2699、3976、4154`中**1765年账面军费及`Caixa`专门页**，尤其`Livro2699 fólio10、15`的旧军费机构移交；对同一现金账户复算2011**359.525124 contos**与2019**约2765 contos**为何不同，并核查地区税源重分类70,000 réis差额。与之前的Tesouraria-mor半年收入支出册5–10及现金册157–159按历史日期联查；只有取得**真实记账日期与支付凭证**，才可重建财政实际现金流和战争债务的时间路径。以上原账都尚**NOT_ACQUIRED**，2025黄金ASCM 209481及2024财政ICPSR 198143均**NOT_RUN/NOT_ACQUIRED**，1748国债/GDP 9% vs 8.1523%仍`SOURCE_CONFLICT_OPEN`。本报告不改变#34既定任务验收范围，不合并Draft PR。
