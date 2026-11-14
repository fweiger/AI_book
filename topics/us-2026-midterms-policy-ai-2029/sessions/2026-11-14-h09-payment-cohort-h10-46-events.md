# TOPIC-011｜2026-11-14 H09合同现金支付时间差与H10四年CPI公布日反例

## 研究起点
延续大湾区老姚对美国2027—2029政治、德州特斯拉优惠、CPI→Fed→债务的观点库。上一轮H09只确认2026-04-07县9%扣留决议但没有2020—22应得/实发美元；H10只有2025—26 22次CPI发布日和近期单日异常，缺更长历史。用户指示“继续”，本轮以历史数据和真实原始文件推进而非新建空理论。

## 阅读与远程取证
1. [Travis County 2020原始签署协议](https://tctransparency.traviscountytx.gov/Reports/EcoDev/TeslaAgreement.pdf) Section 1.22/1.23/5.2/7.4/7.5/7.7/8/9：Performance Year 2020/21/22分别对应条件性的Payment Year 2022/23/24；每年报告次年3月31日、税款证明再下一年3月31日，合规且无税务上诉时ACH通常在Payment Year 10月31日前。**日期不是实际付款证据**；withhold和对已付现金recapture不能混为一谈。
2. [Travis County CivicClerk官方2026-04-07 Packet fileID12961](https://traviscotx.api.civicclerk.com/v1/Meetings/GetMeetingFileStream(fileId=12961,plainText=false))：Ubuntu MCP**完整下载103437809字节PDF，255页**，SHA256 `e93233825a52768bf0ee3860b8ade8d86f32618d71d1f62e0c827eb9ae7dd1bb`；`pdftotext -layout` 全文件提取598620字节，按页重新核对**第15页Item6、253页Item26**均为`Attachments: None`、`Fiscal Impact and Source of Funding:`空白，未列2020—22款项实际美元。**这仅表明本次公开议案包未附计算表，不意味着县机构没有内部资料**。既有County Clerk正式会议纪要仍证明Item26 4-0/1弃权通过扣留9%合格grant，而不证实已经实付后追回。
3. [BLS 2023](https://www.bls.gov/schedule/2023/home.htm)/[2024](https://www.bls.gov/schedule/2024/home.htm)真实公布日各12次；2025 11次、2026至11-10 11次官方日历（2025-10 CPI报告因停摆没有发布）已核，合并46日。美国财政部2023 250个交易日、2024 250日官方XML（原文SHA：2023`7b30333f8ae255688b163f421227ee6e733f642f28a0ebd8c76dca3efd9f0cf5`；2024`acf0b2af87aeda2143365fedd044fe6a254d2916b62588ee9500113b3a8d1764`）及已有2025 249+2026 218日，共967个交易日；按日差966笔，CPI事件46、非事件920。
4. **真实复算**：用GitHub现有两份Treasury CSV和本轮新标准库程序，在Ubuntu MCP `--stdin-json`跑20,000次同月份非CPI日随机安慰剂，并拆2023/24、2025/26、剔2026-11-10，`verification=PASS`。2Y平均绝对bp：2023/24=8.875 vs安慰剂5.4851(p0.00195)，2025/26=5.2727 vs3.9781(p0.04930)，全46=7.1522 vs4.7640(p0.0004)；最近两年去11-10后p0.1387；全46去11-10仍p0.0016。10Y全46p0.00125，2025/26单独p0.20894。方向：2Y全46次21上涨/22下跌/3不变，均值+0.065bp。**这是探索性非因果公布日关联，且子样本强度迁移，不是CPI surprise或可交易收益。**

## 产物
- [Travis合同支付年度条件性队列](../cases/musk-2026/travis_grant_payment_cohorts_2020_2022.csv)及[报告](../reports/2026-11-14_h09_grant_payment_year_lag_contract_audit.md)
- [完整官方Agenda Packet来源审计](../cases/musk-2026/travis_20260407_agenda_packet_documents.csv)、[255页公开资料缺金额报告](../reports/2026-11-14_h09_agenda_packet_255pages_no_grant_figures.md)
- [官方Treasury 2023/24原始日序列](../data/h10_us_treasury_2y10y_daily_2023_2024.csv)、[46次CPI事件CSV](../data/h10_cpi_release_ust_46events_2023_26.csv)、[离线可复算](../analysis/recompute_h10_cpi_release_treasury_2023_26.py)、[四年历史检验报告](../reports/2026-11-14_h10_cpi_release_ust_46event_historical_robustness.md)
- [VIEW-S001-C04/C09新增观点反证两行](../views/claim_reassessments_2026-11-14_round3.csv)保持原作者原始主张和之前版本不覆盖。
- 事实/证据层新增E097—E099、指标层新增Signed 2Y/10Y公布日方向指标，H01—H10完整因果UNTESTED。

## 尚未完成
- H09: 一手县Auditor/PBO的2020—22 eligible/approved/ACH paid/withheld/previous-paid-recouped金额仍缺，州381`totl_agmt_am`为NA，财政透明平台远程访问超时；不能把2020新闻预计十年约1400万美元套9%当实际扣款。此次案卷Item6/26没有附表，已实证排除这一入口，但不能判断县是否藏有/另有记录。
- H10: 2023—26发布前Professional CPI consensus和Fed Funds futures分钟历史数据未取得，分期差异可能与总体市场波动率/利率水平/其他同日信息有关，没有控制因果。p值未做多重检验调整，不能因p0.0004宣称确定性价格效应。
- 未来用户希望“历史样本验证优先”，因此下一研究可先用2021/22甚至2015—2026多个历史利率制度开展同方案对照，但先锁定日期、预期数据与失效/负对照，再做预测，不要为了统计显著性无限延长样本。
