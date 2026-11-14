# H09 一手政府会议记录核验：Travis County 2026-04-07 两项独立表决

> **2026-11-14首次完成正式Travis County Clerk Minutes（8页）与官方会议Transcript（23页）的直接读取。** 原H09报告只取得地方媒体KUT对4月7日9%扣留的报道；本轮将其升级为**官方决议已确认（F）**。H09“2027权力变化导致企业优惠净减少、现金流恶化”的完整机制仍然UNTESTED。2026年4月决议发生于2026年11月选举之前，是必须保留的负对照。

## 资料与可复核性

- 官方CivicClerk公共会议：[2026-04-07 Commissioners Court Voting Session / 事件ID 3609](https://traviscotx.portal.civicclerk.com/event/3609/files)；通过 `/v1/Events` 官方 OData 查询同日会议记录，返回agenda ID 2294。
- [官方 Minutes PDF（fileId 12979）](https://traviscotx.api.civicclerk.com/v1/Meetings/GetMeetingFileStream(fileId=12979,plainText=false))：2026-04-09 15:25:12（CivicClerk资料记录）公开，8页。SHA256 `ff8a5ae05d5ab704c6a11363d1d3cd18fcd5646b4e113b16c4afac23df02435e`，213,354字节。Ubuntu MCP实际取回PDF、提取文本，核对议案、票数、弃权人。
- [官方 Transcript PDF（fileId 12974）](https://traviscotx.api.civicclerk.com/v1/Meetings/GetMeetingFileStream(fileId=12974,plainText=false))：2026-04-09 10:44:25公开，23页。SHA256 `0d7a5a89dca7d178a281b603d473ddd0b46e618f1569b5081a6f58fc8f7636c5`，596,636字节。对照现场发言、动议措辞与结果。
- **来源独立性**：Minutes 与 Transcript 都源于**同一场政府会议**，是两份相互对照的官方记录，**不可将它们计为两次独立政策事件**；此前KUT报道可作当时新闻线索，但正式结果以此处原始会议纪要为准。未将整份PDF/长篇转录复制到公开仓库。

## 已确认的两项正式表决

| 项目 | 官方状态 | 实际内容 | 经济含义限制 |
|---|---|---|---|
| **议案26** | **PASSED，4赞成、0反对、1弃权** | 因Colorado River Project LLC对协议部分要求未完全履约，Travis County决定**扣留2020、2021、2022各履约年度符合资格的grant资金的9%**，授权县法官签署必要文件 | 9%是针对所列年度的合格应得拨款，不是Tesla销售额的9%，也未证明追缴已经实付的款项；实际USD扣留数额未在Minutes给出 |
| **议案6** | **PASSED，4赞成、0反对、1弃权** | 同一会议批准该公司的**2025与2026履约年度 Community Involvement 方案**（涉及合同Section 4.10.2.4） | 这是对未来/当年社区项目方案的批准，**不是**保证未来全部税惠、不是这些投资已实际完工，更不是拨款数额 |

两项赞成者均为 County Judge **Andy Brown** 与委员 **Jeffrey Travillion、Brigid Shea、Ann Howard**；委员 **Margaret Gómez** 弃权。Minutes属于Travis County Clerk制作的正式记录，第26项与第6项分开追踪。

## 直接出自官方转写的额外变量：社区投入义务

2026-04-07政府Planning and Budget Office发言人在审议第6项时说明，合同要求相关法人在社区投入达到其每年县级 **Operations & Maintenance (M&O) 财产税额至少10%**；她对2025和2026履约年度分别给出**约200万美元和约320万美元**的*投入义务量级*，而非政府支付给公司的税收优惠。另有涉及排水设施和水务等项目的投入提案。**不能直接用200万/320万美元充当县财政拨付、Tesla现金补贴、已完成CAPEX或“9%扣减”的分母。**

这个信息提醒H09应并行核算**政府支付的grant现金流**与**公司履约投入的成本及条件**，否则只计政策优惠而不计附带义务，容易高估净经济收益。

## 因果判断更新

1. `正式地方履约审查→正式扣留部分grant` 的**事件节点与行政程序已证实**；这条路径开始于 **2026年11月选举之前**。之前KUT的报道在决议层可从`REPORTED`升级为`OFFICIAL_F`。
2. `协议已整体终止` 不成立：同日第6项继续批准后续社区项目方案，因此至少不能将这次行为描述为整份协议统一撤销。
3. `9%扣留→Tesla现金流恶化` **尚未验证**：缺2020–22分年合格grant核定金额、原计划发放与实际到账、法官签署的最终执行文件、后续年度报表；另外2025 Tesla SEC报告称相关2023–25州县grant对**合并报表不重大**，不等于项目层面无成本。
4. `2027新州政权导致上述2026-04扣留` 在时间顺序上**不可成立**。未来若出现额外政策改变，须冻结原合同及2025–26监管基线，验证**增量**作用。
5. 该案例依然没有证明更广范围的政治关联会引发国会正式传票、赦免法律效果或SpaceX不同法人现金流变化；不能以单一协议推断所有政商关系。

## 机器数据和接续任务

- [原始决议双行台账](../cases/musk-2026/travis_official_votes_20260407.csv)；两个决议同一event ID 3609，书面原始文件与SHA作为可复核身份。
- [原H09合同/政策时间线](../cases/musk-2026/policy_event_ledger.csv)保留媒体发布事件，**另新增正式决议的源级事件**而不覆盖历史报道。
- **下一轮硬任务**：进一步查该公司2020–2022 Performance Report / County M&O税缴款及合格grant分年核算；确认**应得总额、实际发放、9%扣留的USD绝对值、是否已支付后追缴**；核对最终县法官签署文件以及2023–26持续合规。没有金额不能计算企业净现金冲击。
