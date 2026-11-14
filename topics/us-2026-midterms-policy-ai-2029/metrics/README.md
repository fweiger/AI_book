# TOPIC-011｜统一指标层（I Layer）

**设计**：原有 I01–I14 和 H03 文档中的命名指标**保持旧ID不变**，以 `catalog.csv` 做单一可检索目录；新增 I15–I54 聚焦通胀/Fed、公司融资、国会程序、Texas政策优惠。将所有口径集中管理，不让某个 H 在本地再私设同名不同义指标。

## 输入与查询
- [指标总表](catalog.csv) 共 94 个**指标定义/指标族**：14个原 I、37个历史 H03 命名指标、40个H09/H10新增指标、3个近期H03数据定义指标。**目录存在≠历史时序已完成采集**。
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
