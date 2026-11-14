# CASE-MUSK-2026｜德州—国会—赦免—财务：四条可分开证伪的研究线路

**研究期**：2026-11-03—2029-01-20。**Parent** H09 [Issue #55](https://github.com/fweiger/AI_book/issues/55)，同时挂 H01、H06、H07、H10。**状态 UNTESTED**，不是指控马斯克或旗下公司存在违规事实。

## 一、已核时间边界（2026-11-14）
- 德州2026选举后，新当选州长Gina Hinojosa及其盟友的州政治权力预期发生变化；**选举胜利/表态不是州优惠合同自动失效**。[Texas Tribune 2026-11-04](https://www.texastribune.org/2026/11/04/gina-hinojosa-texas-democrat-governor/)；[Houston Public Media/NPR 2026-11-11](https://www.knkx.org/2026-11-11/how-the-midterm-election-results-could-impact-elon-musks-many-business-interests-in-texas)。州长/州议会正式履职和分权权限、法律与协议条款须向正式机构核。
- [Reuters 2026-11-08](https://www.reuters.com/legal/government/democrats-eye-musk-miller-probes-after-midterm-rout-2026-11-08/)报道民主党准备在**2027新国会**开展监督；目前视频指称的“已经签发正式传票”未由本研究找到可确认的原始文件，**不能升格为已立案或已定罪**。
- [BLS 2026-11-10](https://www.bls.gov/news.release/archives/cpi_11102026.htm)及[Waller同日个人讲话](https://www.federalreserve.gov/newsevents/speech/waller20261110a.htm)属于独立宏观链；FOMC真实决议须看正式委员会公告，不可把Waller个人建议直接当结果。

## 二、CASE-MUSK-TX（政策优惠）七段核对
1. **法人主体**：Tesla Inc / 旗下厂房项目和其他公司（SpaceX、X、xAI等）各自建立 `legal_entity_id`；Musk作为个人的捐款不能直接计入Tesla财务；非上市公司财务未公开部分一律NA。
2. **法域**：联邦税收抵免、Texas州级激励、县市减税、地方开发协议、采购、贷款、能源费率逐项分拆。**没有“马斯克一个总补贴余额”可直接相加**。
3. **合约**：真实合同签署日、生效日、原计划结束日、兑现条件、返还条款、州长/州议会/地方政府各自是否有修改权限。
4. **政策变化**：竞选主张→新法/行政命令提案→有效法令/裁定→合同修订生效→实际现金流/税负变化。每一步以原始公文与日期验证。
5. **财务反应**：实际现金税、补助/贷款现金流，若能与SEC同一法人对应再计算I39/I40/I45；名义税收优惠上限不等于实际已获得。
6. **受控比较**：Tesla同业与Tesla不同工厂地区；政策依赖高低、当地需求、汽车价格、制造业资本开支和能源成本控制。受影响项目的先期趋势不可倒填。
7. **市场变化**：只在具体事件公告时点计算异常收益/信用利差；同时检验市场大盘与2Y/10Y UST，避免“政治新闻当天股价跌→因政策清算”的倒置因果。

## 三、CASE-MUSK-CONG（国会监督）
`新届多数/委员会人员→调查倡议→正式函件→听证通知→签发/送达传票→法庭或院方执行→财务披露/合规实际成本`。
- 记录 `committee, legal_authority, subject, action_date, publication_date, notice_served_date, document_url, company_entity, actual_cost`，分开监督政治评论、程序动作与违法裁决；联邦与州级调查分开。
- 反例：没有实际传票；涉及的是政府行政行为而非某家公司的经济利益；法院限制范围；受审企业经营没有明显变化。

## 四、CASE-MUSK-PARDON（赦免及第五修正案）
这是**单独的法律机制场景**：是否真实有赦免令、赦免范围是否涵盖特定既往联邦行为、是否尚有州/其他未覆盖刑事风险、传票质询的具体主题及强制程序。一个已经赦免的事项在某些条件下可能使拒绝自证其罪的理由减少，**绝不等于对任何问题都失去第五修正案保护或不答就自动犯藐视国会罪**。州法犯罪通常不受联邦总统赦免消灭；判定需要法院、CRS/司法分析而不是视频里的绝对断言。

无实际签署文件时`pardon_status=NO_VERIFIED_ORDER`、`legal_cashflow_effect=NA`。法律程序独立走到何种程度，不意味着政府优惠已受影响，也不能无证据推断特朗普政府内部动机。

## 五、CASE-MUSK-FINANCE（政策×资金成本双冲击）
- **截面/面板**：上市公司 SEC 财务公开的同业及政策暴露匹配组；私人公司若没有报告数据只能做案例叙事/合同端研究，**不能拿集团私人子公司未披露的债务构造伪造数值**。
- **事前冻结**：2026-11-02以前的政治暴露/税惠协议、债务到期、现金流和部门固定利率比例；避免按选后表现倒选处理组。
- **指标**：I31–I36（债务/现金流）、I37–I46（合同/财务/法律）、I47（政治履职状态）、I49（Fed个人评论非决定）、I50（候选交互因子）。
- **模型候选**：在样本与平行趋势允许时，以 `policy_exposure_pre × debt_due_24m_pre × post_legal_policy_event` 解释同业调整后融资成本/FCF/CAPEX变动，加入行业×时间固定效应和共同利率事件控制；不是在案例里挑盈利/股价线图对上就算证明。
- **强反证**：政策正式不变、企业利息费用未增加、浮息暴露低且现金储备高、同业普遍下滑、资本开支因需求周期而非监督缩减。
- **禁止过度识别**：2027新国会并不自动改变2026年已有效的Texas法律；2026年经济数据并非2027国会政策结果。

## 六、具体可填写的审核台账
- [Texas政策优惠/合同台账](incentive_contracts.csv)——**已录入3条法人/方案（其中1份Travis County 2020签署合同直接核验；DVISD为SEC披露未取得原合同；Starbase只是未来税惠提案）**；
- [国会与赦免程序台账](oversight_pardon_ledger.csv)——目前只有表头，未伪造传票和赦免；
- 已有观点与新闻线索请以 [Issue #54](https://github.com/fweiger/AI_book/issues/54) 和 [VIEW-S001](../../views/2026-11-14-dayawanqu-laoyao.md) 为主。
- [逐边检验](../../chains/chain_edges.csv)、[统一指标](../../metrics/catalog.csv)、[新H09/H10正式假说](../../HYPOTHESES.md)。

## 下一轮最小可验收项
**Texas已取得2020正式合同及2026年4月地方新闻的选前扣减记录**；2026-04-07县书记官正式会议记录已经取得；下一步优先取得2020—25补助应发及实付美元，以及2026-12-09 Starbase未来听证完成后的真实结果；国会正式监督仍待一手程序文件，明确它们实际是否改变某个法人项目的权利/义务；其次按SEC明确截面财务数据构建行业对照；若找不到需要标`NO_EVIDENCE_FOUND`并保存搜索时点，不作结果暗示。


## H09首轮真实政策与报表核验（2026-11-14）
- [Travis County正式签署合同与选举前审查反证报告](../../reports/2026-11-14_h09_travis_texas_incentive_preelection_control.md)：Colorado River Project LLC公司法人、2020–2041合同、70/75/80%按合格县级M&O财产税grant计算；2026-04-07 **据地方KUT现场报道**对2020—22有关返利扣减9%，并非已查明追回多少现金。
- [政策事件六行时间账](policy_event_ledger.csv)：2025年地方合规审查已存在是2026-11选举后因果判断的**负对照**；Tesla 2025 SEC年报称相关2023—25 county grant在合并报表中不重大；Starbase SpaceX约240亿美元为计划投资、12/9为未来税惠听证，不是已经获得补贴。
- [真实合同台账3行](incentive_contracts.csv)：县级4月决议已获官方Minutes和Transcript确认（F），但缺原始实际兑现金额时仍标`NA`；国会/赦免程序表仍仅表头，不推断已强制作证或签赦免。


## H09一手官方决议补充（2026-11-14，县级文件）
- [官方Travis County 2026-04-07 Commissioners Court会议记录](https://traviscotx.portal.civicclerk.com/event/3609/files)：**Item26 4赞成、0反对、1弃权正式通过**，扣留Colorado River Project LLC **2020—22三履约年度合格grant的9%**，属选前地方行政决议。原先KUT报道作为历史证据保留，不再将是否有正式会议纪要列为缺失。
- 同日Item6也以**4赞成、0反对、1弃权**批准2025及2026的Community Involvement方案，**并不是所有未来税惠都终止**。政府工作人员说明公司社区投入义务最低为每年县级M&O税约10%，并估算2025约200万美元/2026约320万美元；**不是政府实际支付的grant或实际已完工项目**。
- [正式Minutes/Transcript及SHA的逐议案台账](travis_official_votes_20260407.csv) · [官方证据专项报告](../../reports/2026-11-14_h09_official_minutes_primary_confirmation.md)；原始8页Minutes和23页Transcript源自同一场政府会议，不能当两个独立政策冲击。
- **仍缺**：2020—22各年度eligible grant的原定USD、已发付与实际扣留、后续执行文件，不能据9%推Tesla现金损失绝对值、追回已付现金或盈利变化。


## 官方州级381登记协议金额仍缺（v0.2.3）
- [Texas Comptroller官方登记0005328行](texas_comptroller_0005328_registry_snapshot.csv)来源是州级公开[Chapter 380/381 CSV](https://assets.comptroller.texas.gov/open-data-files/ch380.csv)，文件SHA已冻结。州备案总金额和资金来源列是**空字符串/NA**，最后更新时间2022-05-01；不能据此声称2026状态为Active或县已支付0美元。州截止日记2041-12-30、县签署原件记2041-12-31，冲突待审。
- [2020—2022逐年度eligible/approved/paid/withheld/recaptured现金对账表](travis_2020_2022_grant_cash_reconciliation.csv)：县级2026-04-07正式扣留9%已核，但实际核准与美元拨付尚未取得；不能使用签约时十年约1400万美元估值直接推2020—22扣留额。[完整缺口审计](../../reports/2026-11-14_h09_texas_381_registry_missing_cash_audit.md)。


## H09合同付款年错位与103MB议案Packet排除（v0.2.4）
- 原合同Section1.22/1.23、5.2、7.4—7.7和8规定2020/21/22三个履约年度**正常分别对应2022/23/24付款年**，条件包括履约审查、实际缴税及估值上诉结束。[计划与实际现金严格区分的3行队列表](travis_grant_payment_cohorts_2020_2022.csv)及[合同解读](../../reports/2026-11-14_h09_grant_payment_year_lag_contract_audit.md)；9%扣留是`withhold`，不能自动等同`recapture`既付现金。
- [2026-04-07官方Agenda Packet 103437809字节/255页实读](../../reports/2026-11-14_h09_agenda_packet_255pages_no_grant_figures.md)，第15页Item6及第253页Item26均有`Attachments: None`和空`Fiscal Impact`，这份公开packet未有年度grant或ACH明细。PDF SHA见[审计CSV](travis_20260407_agenda_packet_documents.csv)。**没有公开附件不等于县预算/审计部门不持有真实付款凭证**。


## 2025-11报道尚无实际县返利发放（v0.2.5，R来源）
- [Statesman 2025-11与KUT 2025-11-26对县政府履约审查的报道](travis_rebate_disbursement_status_asof_2025.csv)记录**截至2025-11尚未向Tesla发放此项Travis County grant**；原报道与转述同源不能重复计为两笔独立县付款审计。[历史时点分析](../../reports/2026-11-14_h09_no_rebates_reported_2025_cash_status.md)。
- 正式[县2026-04-07 9%扣留](travis_official_votes_20260407.csv)在之后发生，但2025-11→2026-11之间的实际`paid/withheld/recaptured USD`仍待County Auditor/PBO原始账；不能用2020签约时十年预测约$14m替代。官方VPR/VPD只反映部分已付款明细，查询页面无法访问不代表零支付。


## 2022年县级正式Zero rebates paid与履约审核尚未完成（v0.2.6）
- [Travis County官方2022-01-31经济发展协议汇总](https://www.traviscountytx.gov/images/planning_budget/Docs/Summary_of_Economic_Development_Agreements_1-31-22.pdf)明确Colorado River Project (Tesla)当时**零返利支付、首绩效年度核验待完成**，是F类官方历史状态；其它县合作项目也曾零返利，需对比合同开始时间与审批年，不推断Tesla独有政策待遇。 [三时点现金状态CSV](travis_rebate_disbursement_status_asof_2025.csv)现有2022 F、2025-11 R及2026-04 F项26表决记录。[独立审计](../../reports/2026-11-14_h09_county_official_2022_zero_rebates_baseline.md)。
- **2026实际付款或追回USD仍UNKNOWN**，不能拿2022的零付款和2025新闻推断2026也未支付。需Travis Auditor/PBO 2020—26已核准/实付/扣留/追回原始账核实。
