# CASE-FRA-001｜M3-A4：所有“200万”是同一笔资金吗？美元授权、法郎殖民汇票和巴林预付款的分账（2026-11-14）

**唯一权威任务** https://github.com/fweiger/AI_book/issues/35 ｜ **Draft PR #39** https://github.com/fweiger/AI_book/pull/39 ｜ 前序 [M3-A3 费城殖民融资](CASE_FRA_M3A3_PHILADELPHIA_COLONIAL_CREDIT_1803_20261114.md)。本轮只提出**来源与资金身份对照**，不声称取得实际结算额，不生成第二个Issue，也不改原AC。

## 一、核心发现：两个“200万”单位不同，并发现第三条未标币种档案

### A. 美国国会 **USD 2,000,000** 外交支出授权（1803-02-26）：原始法律

[US Statutes at Large 第2卷 p202, Chapter VIII](https://www.govinfo.gov/content/pkg/STATUTE-2/pdf/STATUTE-2-Pg202.pdf)（GovInfo美国政府正式法条）确立：
- 特别授权 **two millions of dollars** 用于美国与外国交往的额外开支；支付和记账由美国总统负责；
- 同一法案Sec 2允许总统选择借贷全部/部分额度、最高6%年息，**法定预算授权不等于已借入、付款或对法转账**；
- [LOC Louisiana Purchase立法时间线](https://guides.loc.gov/louisiana-purchase-legislative-timeline/1802-1803)列出美众院1803-01-12讨论、正式法案1803-02-26通过之区别。

该法律本身没有把该USD 2m写成已经支付法国、或已购买路易斯安那证券的现金流。**会计等级：`US_APPROPRIATION_AUTHORIZED`，法国实收：`NOT_ACQUIRED`**。

### B. 美国国务卿 Madison **1803-07-29** 的同期指示：USD 2m拟用于减价/加速

[美国国会图书馆馆藏原文转录PDF](https://tile.loc.gov/storage-services/service/mss/mjm/25/25_0781_0784.pdf)，文本页第4页的外交通信（注意PDF开头另有一封7月30日私信的引言）写明本想将 **two millions of dollars in cash** 用于**reduce the price or hasten delivery of possession**，并对实际约定的债权处理和美方国库额外负担表达顾虑。

这能确认美元预算授权与谈判初始计划有联系，**不能证明这笔款在1803年7月已经支付**，也不能凭Madison对合同的不满断定后续担保绝未履行。

[Monroe 1803-08-21致Joel Barlow签署信的拍卖目录](https://www.christies.com.cn/zh/lot/lot-1060463)基于一封原始历史信及同代抄本说明，Monroe希望为**$2m**提前款做担保，Livingston对签字和授权表达异议。来源等级`ORIGINAL_AUTOGRAPH_AUCTION_EXCERPT`；不能把提议、担保和银行现金支付混为同一层。

### C. 法国 **FRF 2,000,000** 费城殖民支付汇票（1803-09-13）：NYPL EM2249

[NYPL Thomas Addis Emmet Collection MssCol927 `EM.2249`](https://nyplorg-data-archives.s3.amazonaws.com/uploads/collection/generated_finding_aids/mss927.pdf)，作者Barbé-Marbois、日期1803-09-13、收信地址费城。机构目录写明 **2,000,000 francs** 由Hope/Barings安排在费城融资，Marbois向收信人出票请求确认，资金拟用于**法国殖民地及Saint-Domingue军需出纳官对驻费城Pichon开出的汇票**。

**这是法郎融资的出票/承兑请求，和美方2百万美元预算授权在币种及法律性质上不同。** 原始两页法语扫描未直接阅读，不能判断它是否是美方USD2m预付中的一部分，或与其存在任何合同关系。

按1803年第一付款公约的`60m francs = USD 11.25m` **仅作同口径数学示意**，USD2m约等于**10.67m法郎**，而NYPL所写2m法郎约等于USD375,000；二者相差约5.33倍，**不能写成同一个200万，也不能把这些估算数字视为新成交汇率记录或真实结算**。参见 [NARA原始条约](https://www.archives.gov/milestone-documents/louisiana-purchase-treaty)。

### D. Baring Brothers → Marbois **“Two millions advance”**（1803-11-14）：币种未知，原信待读

[1902年美国官方《Calendar of the correspondence of James Monroe》原书印刷第23页](https://upload.wikimedia.org/wikipedia/commons/8/82/Calendar_of_the_correspondence_of_James_Monroe_%28IA_calendarofcorres00monr%29.pdf)明确登记：
**1803-11-14，Baring Brothers to Barbé Marbois，Two millions advance, payment for the purchase of Louisiana；[Copy in French], 4°, 2 pages。**

[国会图书馆另一份按日期列举Monroe原始手稿的目录第28页](https://upload.wikimedia.org/wikipedia/commons/a/a2/Papers_of_James_Monroe_-_listed_in_chronological_order_from_the_original_manuscripts_in_the_Library_of_Congress_%28IA_papersofjamesmon00librrich%29.pdf)亦列出11月14日`Baring Brothers to Marbois`。两者描述同一函件，**不是两笔独立付款或两个独立原始收款来源**。

现有目录**未写货币单位**，没显示收款方银行进账，更没有明确说这200万是USD、FRF，或是10m法郎预付款中的分批金额。因此必须将其保留`AMOUNT_2M_UNIT_UNSPECIFIED`和`ADVANCE_PAYMENT_EXECUTION_UNKNOWN`。不应该为填补历史假说把它自动归入NYPL的200万法郎或Monroe的200万美元。

### E. 其他金额相似但是绝不能重复加总的合同项目

[巴林官方史料馆](https://baringarchive.org.uk/exhibition/the-louisiana-purchase/)记述Hope/Baring承诺购买票面60m法郎美国公债，对法付款总额52m法郎，首期6m，此后**每月2m法郎、共23期**；另记1803年7月两家银行同意10m法郎预付款安排。**定期2m是52m合同内付款期，不是第三笔200万独立融资；10m预付款是另一个可能与保证/提早变现相关的事件，但实际拨款及是否抵扣合同价尚待原账。**

**重要制度问题**：银行、外交使节及国库使用相同的资金融通网络，但**同一支付系统中出现相同/相近金额，既不证明同一交易，也不证明现金已经到账**。

## 二、统一资金事件与责任主体矩阵

| 来源事件 | 金额 | 货币 | 主体 | 类型 | 不能推断 |
|---|---:|---|---|---|---|
| 2月26美国法律 | 2m | USD | 美国国会/总统 | 授权支出及可借贷 | 法方实际收到2m美元 |
| 7月29 Madison信 | 2m | USD | 美国外交与国库 | 谈判用途/对合同的评价 | 事后实际付款时间 |
| 8月21 Monroe信 | 2m | USD | 美方外交使节 | 提前付款担保争议 | 担保已经银行兑现 |
| 9月13 NYPL EM2249 | 2m | FRF | 法方国库/费城票据 | 开票及殖民支出用途 | 是否抵扣路易斯安那交易 |
| 11月14 Baring信 | 2m | **UNKNOWN** | 银行与法方国库 | 预付款通知/安排（目录） | 币种、承兑/付款均未知 |
| 银行52m股票购买合同 | 2m×23 | FRF | 法方与两家银行 | **合同内分期** | 新增46m法国现金以外的收入 |
| 巴林1803年7月垫款安排 | 10m | FRF | Hope/Baring/French Treasury | 提前融资同意 | 与USD2m或NYPL2m一一对应 |

结构化原始档案相对映射：[louisiana_two_millions_crosswalk_m3.csv](louisiana_two_millions_crosswalk_m3.csv)（9条独立记录，包括一条同日不同收件人信函的防误并提示）；[关键身份审计问题](louisiana_two_millions_audit_questions_m3.csv)（7条）。

**禁止加总**：这些9行既包括法条、指示、同一美元额度相关外交讨论、银行合同和另一批合同内分期，并不是9个现金账目。若研究者用数据框直接`sum(amount)`会严重重复计账。必须以明确`fund_family`及`evidence_status`，并拿到互相独立的收据后才能建立真实流量表。

## 三、四个可能解释，均须以票据编号与真实收款推翻或支持

- **机制H1：USD2m担保、FRF10m垫款存在跨境转换关系。** 历史协议粗算USD2m约10.67mFRF，接近但不等于银行馆方记载的10mFF。**接近不是同笔支付证明**；若合同未明确实收汇率、费用或抵扣关系，此案保持`UNKNOWN`。
- **机制H2：NYPL FRF2m是独立的殖民地军事结算信用额度。** 原件馆方目的描述支持该解释的方向，但也可能为大额银行安排的子账户，须见实际出票、收款、银行账。
- **机制H3：11月14 Baring的两百万是Monroe保证金额在银行端的回应。** 目前只有目录，无币种和正式付款条款，属于`TESTABLE_HYPOTHESIS`。
- **机制H4：银行每月2m法郎的合同分期被后人错误归入“军事预付款”。** 除了数字相等，无本轮来源证明二者相同；审计时优先检查收款账号、票据序号和日期。

**否证方式**：如本应相同的两笔数字显示不同付款方向、受款人、到期日、货币、转账账号或领款授权，禁止合并；如以同一汇票号在两个账中出现，应按双重记账进行对应匹配而非两次求和。

## 四、可证实与不能证实的事实

**验证为真实来源记载**：美国国会USD2m拨款法条；Madison及Monroe同期对USD2m使用和保证争议；NYPL EM2249明确FRF2m殖民地出票安排；1902官方目录确有Baring Nov14“Two millions advance”两页法语抄本条目；NARA与Baring财政合同总体条款。部分PDF文字经网页索引/文本检索确认，原页截图工具仍失败时不升级为`PAGE_IMAGE_VERIFIED`。

**仍为未知**：Monroe Baring Nov14实际单位及付款；NYPL EM2249两页原件准确字词及收件商号拼法；法国2m法郎汇票是否承兑、是否收付/抵销；美方2m美元预算是否实际支付及如何入账；10m法郎预付是否相同或部分重叠；法国最终收到的现金合计；1802–1803 Saint-Domingue战争真正支出；帝国衰落因果实验。

## 五、下一项唯一优先行动

取得**1803-11-14 Baring Brothers→Barbé-Marbois 法语副本的原始两页**，首先确认`Two millions`究竟何种币种、双方是否已汇付及其合同/汇票编号；同时把 NYPL EM2249 的2页原件并列核对。确认前不准把两个200万合并，也不能以“接近银行10m法郎”认定款已支付。

**本阶段只有来源—会计口径审计取得增量，现金到账和军事因果仍为`NOT_ACQUIRED / NOT_RUN`。保留PR Draft，Issue继续开放。**
