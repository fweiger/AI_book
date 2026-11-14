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
**Texas已取得2020正式合同及2026年4月地方新闻的选前扣减记录**；下一步优先取得2026-04-07县书记官正式会议记录、2020—25补助应发及实付美元，以及2026-12-09 Starbase未来听证完成后的真实结果；国会正式监督仍待一手程序文件，明确它们实际是否改变某个法人项目的权利/义务；其次按SEC明确截面财务数据构建行业对照；若找不到需要标`NO_EVIDENCE_FOUND`并保存搜索时点，不作结果暗示。


## H09首轮真实政策与报表核验（2026-11-14）
- [Travis County正式签署合同与选举前审查反证报告](../../reports/2026-11-14_h09_travis_texas_incentive_preelection_control.md)：Colorado River Project LLC公司法人、2020–2041合同、70/75/80%按合格县级M&O财产税grant计算；2026-04-07 **据地方KUT现场报道**对2020—22有关返利扣减9%，并非已查明追回多少现金。
- [政策事件六行时间账](policy_event_ledger.csv)：2025年地方合规审查已存在是2026-11选举后因果判断的**负对照**；Tesla 2025 SEC年报称相关2023—25 county grant在合并报表中不重大；Starbase SpaceX约240亿美元为计划投资、12/9为未来税惠听证，不是已经获得补贴。
- [真实合同台账3行](incentive_contracts.csv)：缺少原始实际兑现金额及具体县级4月表决最终会议纪要时标`NA/REPORTED`；国会/赦免程序表仍仅表头，不推断已强制作证或签赦免。
