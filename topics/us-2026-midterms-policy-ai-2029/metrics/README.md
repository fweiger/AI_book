# TOPIC-011｜统一指标层（I Layer）

**设计**：原有 I01–I14 和 H03 文档中的命名指标**保持旧ID不变**，以 `catalog.csv` 做单一可检索目录；新增 I15–I54 聚焦通胀/Fed、公司融资、国会程序、Texas政策优惠。将所有口径集中管理，不让某个 H 在本地再私设同名不同义指标。

## 输入与查询
- [指标总表](catalog.csv) 共 **118 个指标定义/指标族**（以catalog实际行数为准）：14个原 I、37个历史 H03 命名指标、40个H09/H10新增指标、3个近期H03数据定义指标。**目录存在≠历史时序已完成采集**。
- [2026-10 BLS官方已知观测种子](observations_seed.csv)：严格按样本期间/披露日/是否季调/单位记录；只是单次官方公告的部分数字，**不是回测结果，也不是完整月度序列**。
- [指标—假说—观点引用表](linkages.csv)：一条指标可被多个假说与观点共用，关联本身**不是证据权重**。H01–H10的历史指标仍可从旧METRICS.md查到解释，新增以catalog为主。
- [原本 v0.1.11 METRICS 长文](../METRICS.md)：保留历史审计和H03详细公式，避免无证据迁移破坏已复算数据/代码。

## 数据质量契约（每条真实数值均需）
`metric_id,period_start,period_end,event_date,published_at,observed_at,source_url,source_family,source_version,entity_id,region,frequency,value,unit,methodology_status,revision_of`。
- 经济指标期末不等于发布时间，**不能按观察期间作为当时可知时间**；同一指标/时期/地区不同发布日期算不同vintage。
- 国家级与Texas州级、公司级不可直接求和；Tesla上市实体与Musk其他私人公司严格区别；同比缺数据写NA。
- 官方统计值/公司披露/第三方预测与评论者看法分层；`source_family`去重。
- 历史H03来源重复/不同出版版本误差须保留原始可重现口径，不能覆盖或合并已存在的CSV。
- 对样本外预测另见 `../data/forecast_registry.csv`：预注册阈值和实际数据**不是**同一表。

## 两条显式检验链
**H10 货币政策**：
`I15/I16/I20/I21/I22/I54` CPI/PCE与意外值 + `I48`就业 → `I25`市场利率预期 / `I49`官员个人条件言论 → `I23/I24`FOMC真实决议 → `I26/I27/I29/I30`利率和信贷 → `I31–I36`公司再融资/现金流。**CPI环比改善不单独确定加息或降息**。

**H09 Texas与政治资源**：
`I47`选举/就任 → `I41`正式国会程序、`I38/I39/I40`具体合同优惠 → `I37/I44/I45`政府实际收益与依赖 → `I31–I36/I46`现金流、债务、合规支出 → `I12`事前窗口收益。赦免`I42`只是法律状态变量，需法律文书证明其商业影响。

## 现阶段尚未交付
**没有**完整FEC逐笔捐款、Tesla/Texas历史合同全表、实际传票记录、SEC企业匹配财务表、公司级债券面板，也没有完成统计显著性和因果识别。未来填充时保留 `NA` 和真实来源，不得以0冒充缺失。


## H03原版PJM大型负荷统计口径校验
- I55（MW）原始同版`Table B9b Total Associated−Table B9 Above Embedded`；2025原版B9/B9b同一个XLSX来源，跨2025—2030 RTO/DOM/AEP/其他RTO已闭合，**不是DC实际投产或取消的MW**。
- I56（%）在同一版本上的这个差额 / B9b，总2025目标RTO为53.539%，DOM占差额79.410%。2023/24跨报告相减必须标`PROXY_UNCONFIRMED`。
- I57（%）同一个真实后验目标下使用两组不同公开预测定义的APE排名；2025六月Total与2026五月July Retrospective对v2024/v2025模型给出不同的相对排名，**仅为量化来源定义敏感性**。
- 数据：[五个CSV与可复算脚本](../reports/2026-11-14_h03_embedded_bridge_and_original_vintages.md)。此指标属于“来源/PIT可比性先验检验”，不是新增政治因果边，也不应并入未来预测F-ID。


## H10首轮真实序列新增（2026-11-14；复算PASS）
- [BLS官方CPI-U headline/core 2025-01—2026-10月度SA指数22行](../data/h10_bls_cpi_sa_monthly_2025_2026.csv)，各21行有效，2025年10月BLS原序列缺失、2026年10月同比NA；季调指数现版并非历史每月首发版本。
- [美国财政部官方2Y/10Y历史收益率467交易日](../data/h10_us_treasury_2y_10y_daily_2025_2026.csv)，2025年249日、2026截至11-13 218日。2026-11-09→10：2Y+17bp、10Y+10bp；无11-11休市日数据，不作前填。
- [BEA核心PCE首次与修订版次](../data/h10_bea_pce_release_vintages_2026.csv)：2026年8月核心水平月环比首次0.2%，10月29日公布修订为0.3%；[FOMC正式会议事件](../data/h10_fomc_official_decisions_2026.csv)：9/16加25bp，10/28不变。**这些都是发布时点不同的节点，不能倒填预测。**
- [详细报告与时间线](../reports/2026-11-14_h10_cpi_pce_fomc_treasury_pit_baseline.md) · [标准库离线复算脚本](../analysis/recompute_h10_open_data.py)，Ubuntu实际执行`PASS`。只是数值与日期校验，尚无Fed基金期货一致预期、企业债务、信用利差/因果回归。

## H03：B9/B9b源分层的同目标年修订指标
- 原版同指标的`ΔB9 (I58)`、`Δ(B9b−B9) (I59)`、`ΔB9b (I60)`三层恒等；2027全RTO分别−2883/+1018/−1865MW，属于**2025原版对2026当下修订版的前瞻模型对照**，绝不是已完成的DC实物资产。
- `I61`处理2026当前B9b与2026May Accuracy回顾同标签之间RTO+9/10MW差，关键区域相符，但原因尚未识别；同一来源内部区域聚合与回顾出版口径要分别标记。
- [完整H03第十轮来源及计算报告](../reports/2026-11-14_h03_b9b_vintage_decomposition_2025_2026.md)，对所有模型和状态边继续标UNTESTED。


## BEA NIPA月度PCE 33个月（2026-11-14新增）
- [官方BEA月度整体+核心PCE季调指数33个月](../data/h10_bea_nipa_pce_headline_core_2024_2026_snapshot.csv)，2024-01至2026-09，`DPCERG`/ `DPCCRG`，含计算得到的环比与同比；原始Section2All Excel SHA每行记录。
- [PCE官方源及版本核验](../reports/2026-11-14_h10_bea_pce_monthly_series_and_vintage.md) · [离线复算脚本](../analysis/recompute_h10_bea_snapshot.py) Ubuntu实际运行PASS；此表是2026-11-14**当前版本**，非各月最初发布值，不能覆盖BEA历史版次记录。


## CPI/PCE同月配对初步检验（H10，18个月）
- [21个月并表、其中18个月双侧有环比](../data/h10_cpi_pce_aligned_monthly_2025_2026.csv)，[分析报告](../reports/2026-11-14_h10_cpi_pce_alignment_18_month_sample.md)。当前季调版Pearson整体`r=0.946129`、核心`r=0.553099`，只是2025-02至2026-09非连续月份间的描述性共动指标，**不是政策变量或独立Fed因果效应**。[离线复算](../analysis/recompute_h10_cpi_pce_alignment.py)已真实执行PASS。

## H03来源门槛与规模比
- `I63`真实2026年2月6日前B9原文件存在性/同源SHA校验门槛，当前false，准确勘误增量必须NA，不能将缺失记作零。
- `I64`各目标年B9b总关联负荷预测修订绝对值与RTO总夏季峰值预测修订绝对值之比。2027—30约49.665/48.210/46.275/201.714%，**不属于可加的因果贡献**，且2030修订异号。见[原始数据与证据](../reports/2026-11-14_h03_uncorrected_b9_source_gate.md)。


## CPI公告日美债收益率绝对变动（v0.2.3探索性）
- `H10_CPI_RELEASE_2Y_ABS_BP`与`H10_CPI_RELEASE_10Y_ABS_BP`已纳入[统一指标目录](catalog.csv)，定义BLS实际CPI发布日同日Treasury收益率相对**上一有观测交易日**的绝对基点变动。**不是**直接CPI Surprise或美联储加息预测概率。
- [2025—26共22次真实公布日CSV](../data/h10_cpi_release_treasury_2y10y_2025_2026.csv) · [随机化稳健性报告](../reports/2026-11-14_h10_cpi_release_ust_22_event_robustness.md) · [标准库重算](../analysis/recompute_h10_cpi_release_ust_events.py)：2Y完整样本未调整p=0.0483，剔2026-11-10之后p=0.1389；说明结果对单个异常日敏感，整条政策传导仍UNTESTED。

## H03第十三轮：源表身份交叉审核的治理层指标
- I65：诉讼EN1标Large Load的2023预测版6格与官方B8a Solar 6/6相同、与B9 0/6相同，是**来源错表疑点**，防止把太阳能对负荷的调整当数据中心新负荷。
- I66：纠正2023版Y0+5的负荷调整占RTO峰值`9866/155703=6.336%`，而EN1`4185/155703=2.688%`；2026版Y0+5比例21.714%，相对倍数由8.079纠正为3.427。不代表实际需求已建成。
- I67：2017—22 FERC投诉附件的其他版本尚未独立核PJM原件，标`LITIGANT_EXHIBIT_ONLY`；这一处错误不能推广为所有法律证据均错。见[源报告](../reports/2026-11-14_h03_ferc_en1_solar_table_mismatch.md)。


## 2023—2026四年CPI公布日回溯（v0.2.4）
- [US Treasury 2023与2024官方2Y/10Y每日500行](../data/h10_us_treasury_2y10y_daily_2023_2024.csv)与[原2025/26 467行](../data/h10_us_treasury_2y_10y_daily_2025_2026.csv)组合，按[BLS真实历史发布日期](https://www.bls.gov/schedule/2023/home.htm)构建[46次发布日CSV](../data/h10_cpi_release_ust_46events_2023_26.csv)，包含**signed和absolute两种不同指标**；新增共享`H10_CPI_RELEASE_2Y_SIGNED_BP`、`H10_CPI_RELEASE_10Y_SIGNED_BP`，旧ABS指标保留。
- [四年分时期/异常值稳健性](../reports/2026-11-14_h10_cpi_release_ust_46event_historical_robustness.md)：2023/24与2025/26公布日波动强度不同；2Y总计21次上涨22次下跌3次不变。Ubuntu对967真实日数据运行[离线脚本](../analysis/recompute_h10_cpi_release_treasury_2023_26.py) PASS。公布日大幅波动的强度≠走势方向≠CPI意外值≠FOMC因果。


## 2026-11-10真实发布前CPI预期与FedWatch同日重新定价（v0.2.5）
- 统一[指标catalog](catalog.csv)新增`H10_HEADLINE_CPI_MOM_SURPRISE_PP`、`H10_CORE_CPI_MOM_SURPRISE_PP`：**BLS季调环比新闻稿实际值－公告前明确发布日期的专业预测值**，11/10实例均+0.1pp；不能用网页事后未校验发布时间的CPI指数forecast替代。
- `H10_FEDWATCH_25BP_OUTCOME_PROBABILITY_CHANGE_PP`把同一会议+25bp情景概率按同源前后日期比较，Cboe转引周一84%、周二90.5%，但**缺CME高频原始快照，不是纯CPI效果**。
- `H09_COUNTY_REBATE_DISBURSEMENT_REPORTED_STATUS`为有日期、独立性标记的媒体`REPORTED_NONE/REPORTED_PAID/UNKNOWN`状态变量，不是Auditor真实美元账。分别见[H10事实锚点](../reports/2026-11-14_h10_cpi_20261110_true_preconsensus_fedwatch_rate_anchor.md)与[H09历史状态](../reports/2026-11-14_h09_no_rebates_reported_2025_cash_status.md)。


## 正式2022县现金源和10次PIT核心CPI方向检验（v0.2.6）
- `H09_OFFICIAL_COUNTY_REBATE_PAID_STATUS_AT_SOURCE_DATE`以[官方Travis 2022-01-31协议汇总](../reports/2026-11-14_h09_county_official_2022_zero_rebates_baseline.md)作F级有日期状态输入，**不可等价为2026支付USD、也不替代报道级状态指标**。
- `H10_CORE_CPI_SURPRISE_2Y_SIGN_CONCORDANCE`在公告前有已核日期的市场或机构预测、BLS首发实际值及美债有符号日变化均存在且非零时，才定义方向是否一致；其他写NA。[10事件原始数据](../data/h10_cpi_pre_release_dated_forecasts_10events_2023_2026.csv)与[报告](../reports/2026-11-14_h10_pre_release_forecasts_10_pit_vs_vendor_not_pit.md)显示核心6/7一致、二项双侧p=0.125，**不具有样本外规则或CPI因果的证明力**。[事后46日历](../data/h10_cpi_release_ust_46event_vendor_archive_not_pit.csv)不能混入该真实事前数据组。


## 学校毛税负差及固定2025事前预期来源（v0.2.7）
- `H09_CH313_DELVALLE_GROSS_SCHOOL_TAX_SAVING_USD`、`H09_CH313_DELVALLE_CDR_VERSION_DELTA_USD`、`H09_CH313_DELVALLE_REVENUE_PROTECTION_REPORTED_USD`分别追踪学区Chapter313毛税收节省、同税年不同报告vintage差、另列补偿科目；**不是Travis县Chapter381的grant实付，也不是企业净收益**。[两版本14税年行](../cases/musk-2026/delvalle_ch313_1496_2023_vs_2025_vintages.csv)。
- `H10_UNIFORM_DATED_CPI_CORE_SURPRISE_UST2Y_DIRECTION`用于当CPI首发、**固定同源真实提前发布的专业共识**及两年期真实有符号日变动都可观察且surprise非零时，才计算1/0；缺项写NA，不把事后历史财经日历的预测补入。[2025固定11次发行与7条预告](../data/h10_cpi_consistent_publisher_2025_pre_release_cohort.csv)及[检验报告](../reports/2026-11-14_h10_2025_uniform_publisher_cpi_surprise_direction_falsification.md)说明同向仅Core2/4、Headline2/5，不是未来预测胜率。


## 学区PILOT财报确认与CDR跨税年核对（v0.2.8）
- H09_CH313_DELV_ISD_FY_TESLA_PILOT_REPORTED_RECEIVED_USD 为Del Valle学区年报报告收到/确认的Tesla Chapter313相关PILOT财政年度收入，FY2022–25分别$999,609 / $9,543,964 / $17,946,611 / $23,002,842，**它是学校的收入、企业的合同支出方向，不是政府给Tesla的现金**。
- H09_CH313_DELV_ISD_FY_PILOT_VS_CDR_RECON_RESIDUAL_USD 为上述学区财政年度PILOT与候选前一Ch313税年报告Revenue Protection+Supplemental之间的算术差额：FY2022/23/24恰好0，FY2025 **+$976,875未对平**。这种跨财年/税年的配对必须在实际税单和资金流验证后才可上升为净效益。 [原始数据/合同区分报告](../reports/2026-11-14_h09_delvalle_school_afr_pilot_receipts_and_cdr_crosswalk.md)。
