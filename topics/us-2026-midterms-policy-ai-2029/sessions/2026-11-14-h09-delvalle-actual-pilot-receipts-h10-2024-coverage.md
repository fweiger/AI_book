# TOPIC-011｜2026-11-14 H09 Del Valle财报PILOT实收与H10 2024同源预测覆盖再审

## 实际新增原始来源/分析方法
- 取得EMMA所载Del Valle ISD FY2022、FY2024、FY2025三份原始年度财务报告PDF、按字节计算并验证SHA（分别a4f60f7208a36affd9baed1f647a06d575ce7e44c4f9268e9db1f3dfaafcdd32；1671cbc7b922df1b6dad519bc2b56f8cef9857f97ba643874c1b99f9ee6b194b；dc5909585a8e84d06e60a669fa2cb9c1f331f745f98831b8bb5213afb84cffae），实际用pdftotext搜索协议附注及财务报表比较列。FY2022正式Tesla PILOT $999609，FY2024 Tesla PILOT $17946611及上年比较FY2023 $9543964，FY2025 Tesla PILOT $23002842，合计四财年 $51493026。FY2023来自FY2024财报比较而非独立FY2023原报，后续需核。
- 从官方Texas Comptroller Del Valle ISD Ch313 #1496 2025年CDR原XLSX (SHA a0d3dcc7a071bd8400081a427acb78887bacad9cf8cd1d69ed96a5026556a432)直接按税年读取Revenue Protection与Supplemental Payments。候选映射FiscalFY t -> TaxYear t-1 时FY2022/23/24财报PILOT与两项CDR合计完全对平；FY2025财报PILOT $23002842 vs税年2024 CDR合计 $22025967，**差$976875未经对账**，绝不能手工抵减或声称公司净税惠。这些全部是学区Ch313不同方向的流量，绝不可填写Travis County Ch381那笔9%扣留base。
- 本轮H09的CSV [四个FY学区报表收款记录/候选TaxYear对账](../cases/musk-2026/delvalle_school_afr_pilot_FY2022_2025_vs_ch313_cdr.csv)、[自动下载PDF/CDR检验SHA/财报注释/候选分年对账的可复算Python程序](../analysis/recompute_h09_delvalle_school_pilot_afr_reconciliation.py)、[全证据报告](../reports/2026-11-14_h09_delvalle_school_afr_pilot_receipts_and_cdr_crosswalk.md)已由Ubuntu实际运行PASS。
- **H10源级测试**：在2025同发布者Calculated Risk七条有日期的市场预测样本后，冻结2024完整12次BLS CPI实际发行日并逐月核精确“CPI Preview”网址，只有2024-Apr和2024-Dec两个月相应页面可读；其他10个月**仅缺该固定slug，不能证明发布者当月无预测**。2024-Apr09同发布者15:50的CPI Preview是BofA/Goldman**单机构**headline/core预测，另19:43同日“Wednesday: CPI, FOMC Minutes”专用日程才有**市场共识headline0.4/core0.3**。BLS04-10首次headline/core0.4/0.4，与市场共识对应surprise0/+0.1pp，当日UST 2Y+23bp、同日下午2点还有FOMC纪要。不应把银行0.3/0.2误当市场共识，亦不能归因全天收益率纯CPI效应。Dec11已取得同站前瞻consensus0.3/0.3，BLS首次actual0.3/0.3、core惊讶0；因此**2024两事件不足以检验显著性**。
- [H10 2024同源覆盖/预测类型12行CSV](../data/h10_2024_calculatedrisk_cpi_preview_source_coverage.csv)和[来源类型报告](../reports/2026-11-14_h10_2024_same_publisher_cpi_preview_coverage_and_source_types.md)已归档。

## 源等级与H状态
- EMMA区财政报告描述“received a PILOT”，是学校记录的收入/付款，不是银行原始流水，FY2023须另核单年财报；学区实收恰是企业的相关履约义务，不能归成企业获得现金补助。
- CDR学区毛税差、学区财报PILOT、县级Chapter381现金grant是三种不同的金额/方向/财务时钟。2025财年976875差额没有真实调整科目，保持UNRECONCILED，正式净优惠UNTESTED。
- H10同发布者不代表同预测owner，数据必须有Market Median/Specific Institution标识，且缺Minutes级美债/FF期货及其它同时宏观冲击，核心利率因果依旧UNTESTED。

## 本轮登记及下一任务
主Evidence E120—E123、统一指标新增校财政FY PILOT和财报-CDR未对平差额两项；[VIEW第八轮C04/C10/C07后验评估](../views/claim_reassessments_2026-11-14_round8.csv)只追加观点不改原作者言论。下一步找学区原始FY2023 AFR及FY2025差额调整/实际支付明细，另搜Travis县2026 grant付款凭证；H10优先同一专业机构原始历史全序列+公布前后5分钟利率报价，而非拿2024两次“CPI Preview”推统计显著。
