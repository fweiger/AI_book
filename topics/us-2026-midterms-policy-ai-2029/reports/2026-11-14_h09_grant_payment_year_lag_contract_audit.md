# H09｜Travis County 对Tesla项目的绩效年→支付年两年错位：合同机制和资金对账（2026-11-14）

## 本轮真正新增的发现

直接复核[Travis County×Colorado River Project LLC原签署协议](https://tctransparency.traviscountytx.gov/Reports/EcoDev/TeslaAgreement.pdf) Section 1.22、1.23、5.2、7.4、7.5、7.7、8.1—8.5、9：**Performance Year 与 Grant Payment Year不是同一年度**。项目每个履约年度的年度Compliance Report在**次年3月31日**到期，已支付财产税证明在**再下一年3月31日**到期，在没有估值上诉且满足条件时县通过ACH一般于**支付年度10月31日前**支付净补助。估值诉讼/行政上诉可能导致更长延迟，报告不完整/未完全履约也可被县暂停付款；终止后的已付款追缴属于独立程序。

| 合同履约年度 | 通常履约报告截止 | 正常付款年度 | 合同有条件付款目标日 | 实际已付金额 | 2026年决议 |
|---|---|---|---|---|---|
| 2020 | 2021-03-31 | 2022 | 2022-10-31 | **NA** | 9%符合资格补助扣留 |
| 2021 | 2022-03-31 | 2023 | 2023-10-31 | **NA** | 同上 |
| 2022 | 2023-03-31 | 2024 | 2024-10-31 | **NA** | 同上 |

这里的日期是**合同条件允许时的正常计划时间**，而不是经核实的实际打款日；没有公司缴税证明、估值争议结束文书和县ACH支付数据时，不能直接推断任何款已付或未付。

## 不能混同的四个现金概念

1. `GROSS_ELIGIBLE_GRANT`：在符合条件的已缴县级M&O财产税基础上按70/75/80%优惠率计算的理论补助（Section 7.5）；**不是**Tesla全部德州税收或集团收入。
2. `NET_APPROVED_GRANT`：扣除协议7.6行政费和相应不完全履约的减额后的**可能应付**净补助（Section 7.7）。
3. `UNPAID_GRANT_WITHHELD`：Section 8合同赋予县在资料不足/上诉/其他违约等情况下暂缓原本可能支付的资金，与[2026-04-07正式议案Item26](https://traviscotx.portal.civicclerk.com/event/3609/files)通过的**9%合格grant扣留**相关。
4. `POST_PAYMENT_RECAPTURE`：Section 9规定的符合条件时**已支付后终止或追缴**，须独立有实际付款/返还记录。**2026-04-07议案表述为withhold，不是证明之前已发款现已追缴**。

## 本轮的事实层约束

- 县书记官正式2026-04-07 Item26 4票通过（另1弃权）的9%扣留针对2020—22三个**履约年度**，不是2026年发生的同期补贴现金，也不是Tesla营业收入9%。见[一手核验](2026-11-14_h09_official_minutes_primary_confirmation.md)。
- 县2026-04-07 Item6还批准2025、2026社区投入方案，证明不能概括为整项优惠协议当场终止。
- 州级[Texas Comptroller 381协议0005328登记](https://comptroller.texas.gov/economy/development/search-tools/ch380-381/economic-development-agreements-details.php?agreement=0005328)的总金额未填，最新登记时间为2022-05。没有年度已发金额，不能以2020年新闻所估计的“前10年约1400万美元”代替这三个履约年度的合格grant基数。
- [县2022协议摘要](https://www.traviscountytx.gov/images/planning_budget/Docs/Summary_of_Economic_Development_Agreements_1-31-22.pdf)记录的是合同条件与项目投资/就业要求，不是已核实的年度ACH付款。

## 可以复算的真实数据契约

[逐履约年和支付年映射CSV](../cases/musk-2026/travis_grant_payment_cohorts_2020_2022.csv)保留`performance_year,annual_report_due,tax_statement_due,conditional_payment_year,actual_ACH_date,eligible_grant_usd,net_approved_grant_usd,withheld_usd,recaptured_usd`。后四项目前**全部NA**，不构造伪金额。

下一步从Travis County Auditor/PBO取2020、2021、2022各年的`Annual Compliance Report`、`Statement of Ad Valorem Taxes Paid`、县Grant Calculation Worksheet、approval/reduction/appeal记录、付款/ACH日期与金额、2026-04-07决议执行文件。按`legal entity + performance year + tax payment year + grant payment year + actual cash date`关联。财务透明门户2026-11-14远程TLS访问失败，不代表没有付款。

## 对H09和专家观点的改变

H09已经证实：选举前存在可执行的县级补助合同、正式不完全履约扣留决定和明确的付款/扣留/追缴机制。**但“2026选后新州政府改变政策→实际Tesla税惠现金流减少→债务危机”任何一条关键新增因果边仍未证实。** 本研究不把档案欠缺误写成零，也不把合同一般日期误写成真实支付。
