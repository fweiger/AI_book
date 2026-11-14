# H09｜Travis County税收返利的“截至2025年尚未支付”历史证据与2026现金缺口（2026-11-14）

## 新增关键事实

2025-11-17 [Austin American-Statesman 文章公开转引版本](https://eedition.statesman.com/infinity/article_popover_share.aspx?guid=6a71809c-9b1b-45f5-be6e-729aa32495f3&share=true)报道，县委员在解释Tesla县级优惠审查时指出，**当时尚未向Tesla发放返利**。之后[2025-11-26 KUT 记者报道](https://www.kut.org/text/austin/2025-11-26/austin-tx-tesla-tax-rebate-deal-travis-county)再次明确，Travis County “so far” 未发放这项返利，并引用县发言人解释履约验证流程。

**证据等级 R（新闻采访记录/县官员言论），不是县Auditor全量ACH支付审计**。而且KUT文章指向Statesman原报道，两者很可能依赖同一批县级信息，`source_family=STATESMAN_KUT_COUNTY_REBATE_REPORTING`，**不能计为两份独立零付款的官方记录**。[带发布日期、认知状态与独立性说明的3行表](../cases/musk-2026/travis_rebate_disbursement_status_asof_2025.csv)保留这一时点观察。

## 和正式2026-04-07决议如何同时理解

已取得[Travis County Clerk2026-04-07官方Minutes](https://traviscotx.portal.civicclerk.com/event/3609/files) Item26 **4赞成、0反对、1弃权**：扣留Colorado River Project LLC **2020/21/22履约年度符合资格的县级grant 9%**，同日Item6批准2025/26公司社区投入方案。两条记录时间相隔约4.5个月：

1. **截至2025-11-26未发放（新闻记录）**：能否在2025年11月之前以现金取得县财政grant是独立问题；按新闻资料该节点尚未发放。
2. **2026-04-07县正式批准扣留合格grant的一部分**：这是不同日期的法定决定。没有取得2025-11-27—2026-04-07期间的县付款流水，也没有2026-04-08—2026-11-14的流水，所以**不能说2026年同样没有支付，更不能说9%已经从此前付出的现金成功追回**。
3. 2020签署的[县经济发展协议](https://tctransparency.traviscountytx.gov/Reports/EcoDev/TeslaAgreement.pdf)本来要求先满足绩效/纳税与审核条件再核发补助，[绩效年度→正常付款年度](2026-11-14_h09_grant_payment_year_lag_contract_audit.md)通常存在两年滞后和可能的税务估值上诉/资料延迟。此处不能将`withhold`与`recapture`混为一笔。
4. 州级[Texas Comptroller协议0005328](https://comptroller.texas.gov/economy/development/search-tools/ch380-381/economic-development-agreements-details.php?agreement=0005328)数据库总金额`totl_agmt_am`为空白，不能用2020签约时“前10年约1400万美元”预测乘9%当实际扣留美元数。

## 当前H09定性判断

- **县正式有协议/履约审查/部分扣留**：已建立事实证据；**都发生在2026年11月选举之前**，否证“这些程序全部是新州长上台后开始”的极端叙事。
- **此前已经发放大量现金后又追回**：与2025-11时点的媒体报道不符；**至2026-11的最新实付/追回情况仍UNKNOWN**，不能定性为绝对没有。
- **现金重大性**：Tesla 2025 SEC 10-K称2023—25年相关县财产税grant对合并财报不重大。项目级金额尚可有实质意义；但未取得县Auditor付款明细就不能断言损失规模或集团债务压力。
- **政策暴露交互**：国会可能调查、总统赦免议题、联邦融资与州县优惠是不同法域的不同事件，不可拿Travis县程序当联邦调查已导致Tesla现金危机的证据。

## 公开付款数据的具体局限与取证任务

[Travis县官方Vendor Payment Details](https://tctransparency.traviscountytx.gov/VPD)提供按Vendor查询并导出报表的入口。[官方VPR/VPD帮助](https://tctransparency.traviscountytx.gov/Help/WhatIsVpr)说明付款明细覆盖支付发票而非所有县支出，且VPD的同一笔支付可因多张发票/科目分成多行，不能简单求和重复计算。此公开网站在Ubuntu MCP访问仍出现TLS/下载超时，故**既未取得2026公司付款明细，也不声称查出零笔**。

下一步如可访问门户，应首先按`Colorado River Project LLC/Tesla`和2022—2026付款日期、基金/科目筛选，核对**Vendor Number + ACH/Check # + Payment Date**去重；还需核对县PBO `Grant Eligibility/Approval`，因为公开VPD未必覆盖所有grant转账。若仍不能获得，向Travis县Auditor/PBO申请这五类字段，**本轮并未发送申请**。县级条目独立于Del Valle ISD学区税惠。

H09完整`2026选后权力变化→取消优惠→现金流恶化`因果仍`UNTESTED`，不因历史R级“未支付”升级现金流推论。
