# CASE-FRA-001｜M3-A3：1803年费城200万法郎殖民融资与路易斯安那结算时序（2026-11-14）

**权威 Issue：** https://github.com/fweiger/AI_book/issues/35 ｜**现有 Draft PR #39：** https://github.com/fweiger/AI_book/pull/39 ｜在前轮 [M3-A](CASE_FRA_M3_LOUISIANA_BANK_SETTLEMENT_AUDIT_1803_1804.md)、[M3-A2](CASE_FRA_M3A2_RECEIPT_AND_GUARANTEE_SOURCE_AUDIT_20261114.md)之上增量审计；不新开 Issue，未关闭历史因果或收款 AC。

**核心增量**：找出一件比1804年最终收款更早、直接把 **Hope & Co. / Baring → 费城信用网络 → 法国国库 → 圣多明各军需汇票** 联系起来的**具体同期档案**。目前唯一能准确陈述的是 **1803-09-13法国公库部长已通过上述关系安排在费城筹措200万法郎，并向对手方开票要求承兑，拟用于殖民地及圣多明各出纳官授权汇票**。不能直接推断银行实际付款、法国收到账款、某一1802年远征具体军费已由该笔支付，更不能把该200万直接记为路易斯安那债券出售的已收回现金。

## 1. 原始档案标识及来源层级

纽约公共图书馆（NYPL）**Thomas Addis Emmet Collection, MssCol 927**，**`EM.2249`**：**Barbé-Marbois于1803-09-13从巴黎致费城收信方的法语签署信函，两页folio**。纽约馆方目录明确记载：
- Hope & Co. Amsterdam 与 Alexander Baring 安排在 Philadelphia 筹集 **2,000,000 francs**，名义用途为 French Treasury；
- 法方已向收信人**开出票据（drawn on）并要求对方 acknowledge drafts**；有出票和承兑请求 ≠ 已承兑 ≠ 到期支付；
- 款项**拟用于法国殖民地**，以及清偿 **Paymaster of San Domingo**获准向 **Louis André Pichon**（驻费城法国代表）开出的汇票；
- 在Pichon不能办理时交由收信人处理。

**来源**：[NYPL官方馆藏总入口](https://archives.nypl.org/mss/927)；[NYPL官方完整finding aid PDF, `EM.2249`](https://nyplorg-data-archives.s3.amazonaws.com/uploads/collection/generated_finding_aids/mss927.pdf)。本轮是**馆方目录文字解读**；官方目录PDF原页截图工具失败；原始两页法语手稿**尚未亲自逐页辨认**，虽然[NYPL该封信影像的公开索引入口](https://picryl.com/media/letter-to-thomas-willing-and-francis-banquier-philadelphia-07ee42)已经定位；不把影像索引当成全文原件已查。

**重要会计限制**：
1. 同一200万存在至少`FUNDING_ARRANGEMENT`、`DRAWN_BILL`、`INTENDED_COLONIAL_SETTLEMENT`三层描述，**均为同一信用链，不能加成600万**；
2. 目前不知道汇票编号、承兑银行、票据期限、兑付日、实际受益人和是否实际资金汇至Saint-Domingue；
3. 巴黎国库、费城银行、驻费城法国代表和圣多明各殖民地出纳官分别为**不同财务主体**；筹措名义上给法国国库，可能实际对殖民地债权人在费城支付或轧抵，最终现金落点尚未知；
4. 1803-09融资意向在1804-04证券集中交割之前，故可检验**过桥信用支持殖民付款**；但此时没有任何记录证明这200万属于路易斯安那`52m`证券转售款或`10m`预付款的子项；
5. 不能把1803年融资用于解释1802年已发生的成本，除非找到**偿还1802欠款**的具体证据。

## 2. 收款银行实体识别：NYPL索引`Francis Banquier`可能是解析错误

NYPL题录呈现`Letter to Thomas Willing and Francis Banquier`，并将`Banquier, Francis`列为个人名称。这里**存在源数据实体歧义**：18–19世纪费城确实有**Willing and Francis**商业行，其历史收藏由宾夕法尼亚历史学会（HSP）`Collection 1874`保存；HSP确认合伙人 Thomas Willing、Thomas Mayne Willing 和 Thomas Willing Francis。[HSP独立机构馆藏指南](https://hsp.org/sites/default/files/legacy_files/migrated/findingaid1874willingsandfrancis.pdf)；[宾州司法系统Thomas Willing生平材料所列1794–1807年Willing and Francis合伙关系](https://wwwsecure.pacourts.us/Storage/media/pdfs/20220505/193111-willing.pdf)。

待原文核查，法语收信人也许是`Messieurs Willing et Francis, banquiers`（“Willing和Francis，银行商”），而不是存在一个正式姓名为`Francis Banquier`的自然人。**这是备择实体解析假说，不是已从原手稿证实的法文原句**。后续本项目一律暂用`Willing/Francis addressees (identity pending primary scan)`，严禁用`Banquier`作已核定姓氏。

HSP Collection 1874 多数保存1805—1822中国贸易的业务资料，不能因为有馆藏就声称拥有1803年此张汇票结算底稿。需要独立查询其他1803账册或收发信。

## 3. 同时取得银行股票发运延迟的同期外交信件新证据

[Christie's 2025年Lot 658目录](https://www.christies.com/en/lot/lot-6519114)销售一页**1804-03-18 Robert R. Livingston致Talleyrand的签名原信/本人留底**，部分录出他认为美债证书将很快抵达巴黎的原话；这并非股票已收到的证据。该拍卖商研究说明中还据 Madison Papers 引用了两封未在本轮直接取得全文的信：
- **1804-04-14 Livingston→Jefferson**：股票仍未到巴黎；Hope银行代表正在安排法国国库的现金化；法方希望提前获得托管汇票第一批资金。
- **1804-05-03 Livingston→Jefferson**：股票抵巴黎后，Livingston述称摆脱代持银行汇票的压力，银行准备承接票据。4月25日到货与美国国家档案馆原件目录相互一致，但**银行承接不等于法方国库已取得特定金额的兑现现金**。

这些展示了一个**跨境交易结算延迟与法国国库流动性急迫性**的可信研究机制。来源分类必须严守：3月18日是**拍卖目录有签署手稿并摘录其文句**；4月14日/5月3日则仅为拍卖商**引用Madison Papers的摘录**；不是本轮直接审计了三封完整原件。

[美国国家档案馆 2003官方回顾](https://www.archives.gov/publications/prologue/2003/spring/louisiana-purchase.html)进一步确认：**1804-01-16**美国发行两批6%公债，总计`$11.25m`，其中`$3.75m`交给银行，`$7.5m`送往巴黎；运输延误直至**1804-04-25**，对应 [NARA展品原件说明](https://www.archives.gov/publications/prologue/2003/spring/louisiana-purchase-sidebar.html)。**200万费城融资档案与这两批股票交割是不同货币、不同来源且不同日期，不能无独立合同编号就建立从属关系。**

## 4. 1849财政部追溯账与先前7.5m / 7.6m读数差异

[1849年美国财政部向众议院报告（Ex. Doc. No.67）](https://www.govinfo.gov/content/pkg/SERIALSET-00543_00_00-016-0067-0000/pdf/SERIALSET-00543_00_00-016-0067-0000.pdf)仍记录1803年公债依法发行`USD 11,250,000`，全额承销主体为Hope & Co.和Baring & Co.。这是一项**19世纪官方财务历史核算**，可支持总票面与银行承销人，但不能鉴定[上轮 M3-A2](CASE_FRA_M3A2_RECEIPT_AND_GUARANTEE_SOURCE_AUDIT_20261114.md)所述1804-02-13收据网站文本`7.6m`是否为原始笔误/OCR错误；本轮没有取得那张手稿目视原页。并不据此推断实际发行多了10万美元。

## 5. 会计实证：把银行工具与殖民地支付分成可回溯链条

| 链条环节 | 本次证据 | 准入等级 | 必须追加的原始证据 |
| --- | --- | --- | --- |
| Paris Treasury融资需求 | NYPL EM2249 2m法郎安排 | `ARCHIVE_CATALOG` | 国库授权编号/会计科目 |
| Hope/Baring调配流动性 | EM2249馆方摘要明确两银行名 | `ARCHIVE_CATALOG` | 银行账户对应付款分录 |
| 费城金融机构开票承兑 | Marbois说已draw并请求acknowledge | `ISSUED_BILL_NOT_CASH` | 票据正背面、承兑日期 |
| San Domingo军需付款 | 原目录称目的为结算paymaster汇票 | `INTENDED_EARMARK` | Pichon与殖民军需出纳官实际支付收据 |
| 法方国库入账或账内轧抵 | 无原件 | `NOT_ACQUIRED` | 法国公库1803年度账与银行对账 |
| 与路易斯安那债券出售的相关性 | 人物与银行网络部分重合 | `HYPOTHESIS_NOT_PROVEN` | 2m凭证合同号与52m银行采购/10m预付凭证交叉 |

原始资料追查顺序应改为**NYPL EM2249 2页原件→HSP或对应费城机构收兑账→Pichon驻费城公款账及San Domingo paymaster汇票→银行NP1.A4.34/48对应抵销**。这条路径比孤立追逐路易斯安那单笔“最终现金”更接近法国财政-军事机制，但是否同一笔资金必须最后凭账号识别。

结构化档案：[11条原始来源与结算等级CSV](philadelphia_1803_colonial_credit_evidence_m3.csv)。每行含会计类别、账户主体、source family和dedupe group；原有M3-A 21条金融事件表**不增加虚假现金**。

**本轮状态：**`EM2249_ARCHIVE_DESCRIPTION_VERIFIED`；`DIGITIZED_SCAN_LOCATED_NOT_TRANSCRIBED`；`BILL_DRAWN_NOT_ACCEPTED_OR_PAID`；`2000000_ACTUAL_CASH_NOT_ACQUIRED`；`FRENCH_TREASURY_CASH_NOT_ACQUIRED`；`SAINT_DOMINGUE_WAR_SPENDING_NOT_ACQUIRED`；`CAUSAL_NOT_RUN`。

**本轮最重要的新研究问题**：1803年圣多明各军需出纳官能否通过费城银行承兑汇票解决殖民地财政缺口？若这一信用链有效，法国的海外军事能力便不只取决于巴黎现金储备，还取决于欧洲—费城—加勒比的**信用支付网络**。此命题目前只有档案目录支持网络存在，尚无资金交割及军事效果证据。
