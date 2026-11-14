# CASE-ESP-001 | M2j：1793年银行股东大会原始公告、1795—1839港口贷款与1884国库债务裁决

日期：2026-11-14 ｜ 唯一Issue：https://github.com/fweiger/AI_book/issues/32 ｜ 同一Draft PR：https://github.com/fweiger/AI_book/pull/36

**状态**：PRIMARY_1793_GAZETTE_PAGES_487_488_IMAGE_VERIFIED / PRIMARY_1884_HACIENDA_RULING_PAGE_224_225_IMAGE_VERIFIED / HISTORICAL_MONEY_INTERNAL_GAP_300_REALES / 1829_SETTLEMENT_PAID_LATER_OFFICIALLY_ATTESTED_NO_DIRECT_VOUCHER / 1790_1791_ORIGINAL_AGM_NOT_ACQUIRED / FISCAL_CROWDOUT_CAUSAL_TEST_NOT_RUN.

## 0. 对前轮工作的推进边界

M2i 仍无法打开格拉纳达 AHFT C25_010 108.5MiB 1790皇家决议或 BNE hd0069882062 1791股东大会（原件存在，但BNE 403）。本轮尝试通过 web 正式链接读取 C25_010，返回 **HTTP400 Content length is too large: 113756771**；原始文本仍没有实际阅读。央行2014年 EHE67 大PDF可取索引正文，要求截图时失败；不靠重复检索给未读原稿抬高证据等级。

但是另找到并实际通过官方原始扫描页**直接检查了两份不同年份《马德里公报》**，从银行治理和债权的*债务人身份*两个方向提升证据链。

## 1. 1793年5月28日同时代银行自刊公告：投票门槛及代理限制

一手材料：**《Gazeta de Madrid》1793-05-28，第43期，印刷第487—489页**，官方原件扫描 [BOE](https://www.boe.es/gazeta/dias/1793/05/28/pdfs/GMD-1793-43.pdf)。本轮 **web screenshot PDF zero-index page10＝487页，以及 page11＝488页** 已实际查看；第489页文字从官方PDF索引读取、没有单独图像核验。

- 银行董事会原公告将下一次股东大会排定在**1793-07-20**；议程先处理上一届尚未解决事项，再由管理层说明**1792财年**银行经营。注意：公布“拟召开”不等于亲见了后来会议的签到和决议。
- **个人参加大会的持股门槛为至少25股**；按1782发起章程每股面额2000名义雷亚尔，代表 **25×2000=50,000 nominal reales FACE VALUE**，不代表1793二级市场价格和实际财富门槛。
- 同期新的大会规章明确**多个小股东不得合并持股凑够25股获取一个投票资格**，公告还特意指出当初《Real Cédula de erección》原本允许此类集股代表投票，这项权利已由后续股东大会规章第4章废除。治理制度出现了**实际可直接观察的代表权收缩**。
- 股份或委托文件需在**1793-06-10至07-09**办理，股东的股票与代理凭证需核实，国外股东需经过西班牙使领馆认证代理。设有权利身份审核，不能说“所有小股东都丧失持股权、利润权”。
- 大会将来若批准分红，则须再宣布支付日期，受益人在银行总库凭券实际领取。**这是一套未来付款程序，不是已经支付1792财年某额股息的凭证**。

**可证伪治理假说**：高额面值参会门槛与禁止小股东集股可能让决策更偏向少数大持股人，并影响亏损披露、管理层替换、1790年代分红政策；**NOT IDENTIFIED**：没有1793持股分布、现场票数、代理股票数、表决实际影响，也不应套用现代一股一票规则。具体见 [bank_1793_AGM_governance_primary_m2j.csv](bank_1793_AGM_governance_primary_m2j.csv)。

## 2. 1884年原始财政裁决：贷款是地方港口公共工程债，而非自动等同中央国库债

一手材料：**1884-04-26《Gaceta de Madrid》第117号，印刷第224—225页，3月18日西班牙财政部Real Orden裁决**，官方扫描：
https://www.boe.es/gazeta/dias/1884/04/26/pdfs/GMD-1884-117.pdf

本轮 **web screenshot PDF index1＝印刷第224页、index2＝第225页** 真实呈现并检查；官方文本可复核。1884裁决作为**后来的第一手行政证据**，其中对1795、1839、1829的描述属于**政府的追溯事实认定**，并不自动变成原贷款合同及付款流水的原始复印件。

### 2a. 贷款发放及现金工具

- 借款人 **Junta de Comercio y Agricultura de Valencia**，用于瓦伦西亚 **Grao 港口工程**（港口工程专设Junta）；贷款方 **Banco de San Carlos**，**中央财政不是1795两份合同的直接签字贷款方**。
- 合同签于 **1795-10-06马德里**，瓦伦西亚 **1795-10-22**承认/追认，约定借款本金 **8,363,895 whole reales +12.5 maravedís**，按5%年息安排长期摊还，合同所涉利息历史预计 **4,604,679 whole reales +26⅓ maravedís**；最后期限 **1816-12-31**。
- 1884财政部援引1862年瓦伦西亚财政证明：银行从**1795-11-01到1797-03-01**分批向该港口工程实际交付上述本金，支付工具为**政府纸币 vales reales**，16次各500,000雷亚尔，另1次363,895 whole reales+12½ maravedís。这里**“实际上以 vales 交付贷款”是银行资产变为港口贷款债权，不等于王室现金金属币流出或国库直接借款**。

### 2b. 1839清算仍列历史债权，但须严格区分债务人

1884财政部称1839年10月24日地方工程账房对截至1839年6月底结算，仍列：
- 本金 **3,680,113 whole reales +33 maravedís**；
- 利息 **822,892 whole reales +11 maravedís**；
- 合计 **4,503,006 whole reales +10 maravedís**（算术可精确核验：44 maravedís＝1 real+10mrs）。

这里“账面未结”是**港口工程委员会债权**，不能因其是公共工程，也不能因历史皇家许可其收费/借款，就默认为中央国库直接承诺。**1884原裁决正是拒绝继承银行业务的 Banco de España 将该账款认列为国家的所谓 *carga de justicia***：旧合同只是银行对特定港口建设组织，中央政府不是签约当事人；后来国家管理或改组该机构本身不创造未曾承诺的国债本金。

这个判定大大削弱未经审计就把**帝国时期银行所有公共工程资产全算作王室财政拖欠**的做法。历史银行账目中的 *Obras Públicas* 项目、*Real Hacienda* 项目、民间贷款和地方贸易/港务融资，必须在同一历史实体及追偿路径下分别记账。

### 2c. 1829和解的事后履行信息（纠正 M2g 的证据状态）

此前M2g基于1829年9月3日官方协议原件，仅能确定**4000万雷亚尔的合同对价**，并写明**没有实际现金付款证据**，这仍对“1829年签约当天是否即时到账、支付工具、账户入账日期”成立。

然而1884原始行政裁决第224页明确表示 **中央国库已经使先前约定的金额生效/付给旧银行**（原文含 *"el Tesoro hizo efectiva al Banco de San Carlos la cantidad convenida"*）。因此现在可以升级为：

- **PASS：LATER_OFFICIAL_GOVERNMENT_ADJUDICATION_ATTESTS_SETTLEMENT_PERFORMANCE**（1884裁决认为1829约定金额确已履行）；
- **NOT_ACQUIRED：FIRST_PARTY_1829_1830_TRANSFER_VOUCHER / BANK_LEDGER_EQUITY_SUBSCRIPTION / PRECISE_CASH_OR_EQUITY_INSTRUMENT / PAYMENT_DATE**；
- **不能因1884政府认定已付，就说4000万名义雷亚尔在1829年6月29日全部转为可提现金，也不能作为银行1807资产减值率。**

此外1884的追述把1829协议日期记为**6月23日**，而已读1829原版法律附件以**6月29日**为协议日期；这是原版/后世追述的日期差异，尚未检查是否为不同阶段签署、抄录或追认，不要自动修正。

## 3. 原始1884公报自身还存在一个300雷亚尔的可检验加总差额

货币最小单位采用**六分之一马拉维迪**，原因是源文件明确出现**半马拉维迪**、**三分之一马拉维迪**、**4又5/6马拉维迪**。1 real=34 maravedís=204 sixth-maravedí integer units。

| 原版1884公报文字（p224） | 雷亚尔整数 | 尾数马拉维迪 | 是否相容 |
|---|---:|---|---|
| 本金 | 8,363,895 | 12又1/2 | 源文 |
| 预计利息 | 4,604,679 | 26又1/3 | 源文 |
| **两者精确合计** | **12,968,575** | **4又5/6** | 项目计算 |
| **1884公报声称合同总额** | **12,968,875** | **4又5/6** | 源文 |
| 差额 | **300** | 0 | **SOURCE_INTERNAL_MISMATCH_UNRESOLVED** |

该300雷亚尔差额通过**1884原出版p224的截图**核实，并非现代电子CSV表的计算错误；也不能轻率断定原来的1795合同有误——1884是距1795已过89年、转引过去契约的文件，可能出现后世文字转录或某个分项遗漏。下一步应该找**1795-10-06及10-22原合同**或第二份独立打印/抄录核对。

同时，**1839未付总数**由两个分项精确加总，没有该300差额；银行1795—97实际发放的16笔×500,000再加末笔，也能重构836.3895万雷亚尔本金。这两条验证分别标记PASS。

详见 [bank_1884_primary_source_arithmetic_checks_m2j.csv](bank_1884_primary_source_arithmetic_checks_m2j.csv) 及 [bank_1884_valencia_loan_and_1829_payment_m2j.csv](bank_1884_valencia_loan_and_1829_payment_m2j.csv)。

## 4. 对西班牙帝国过度延伸机制的影响

### H-DEV01：中央国库拖欠银行款

1807银行年度资产表 *Real Hacienda* 217.3百万；2010银行史另有166.4百万；1808国库对银行约125.653百万；1829全政府债权名义309.476百万统一和解。都属于**不同阶段/不同确认范围/不同利息合并规则**，不可仅凭表面金额构成因果时间序列。

### H-DEV02：国有许可的地方基础设施项目融资

1795港务银行融资8.364m真实**以 vales reales 放款**，当时中央政府批准港务特别税费和借款权限；但1884裁决认定**原合同非国库直接债务**。风险归属、偿付来源和国家担保要逐级确认。不能把所有 *Obras Públicas* 当国库“战争债务利息”。

### H-GOV01：银行内部股权治理代表性

1793正式公告个人最低25股并禁止小股东合并达标，能够支持股东治理权/实际参加权受到制度性限制的假说；不能仅凭规则预测大股东投票获益或商业信用挤出，仍缺1793原始股东名单、持股分布和投票结果。

### H-SET01：1829重组“履行程度”

1829原始合同证实规定40m对价、1884国库原裁决**事后认定已经履行约定金额**。但必须得到银行1829—1831通用账、股份认购清算账及清偿凭证，才可按日期/支付工具认定实收现金及最终实现损益。把法律履行和会计现金回收分开是本轮的具体证据升级。

## 5. 执行结果、权限与唯一下一动作

**PASS：**
1. 1793原始公报扫描第487—488页实图核验25股门槛、联合小股东不得凑25股投票；第489页数字文字查核实际红利拨付程序；
2. 1884原始公报扫描第224—225页实图核验1795合同、1862证明、1839账余额、1829合同已执行的官方认定，以及**拒绝认列中央国库负债的最终裁决**；
3. 本项目整数化1/6马拉维迪计算：本金、利息按原版文字合计，发现**300雷亚尔源文本不平**；1839余额分项精确加总；借款16笔及末笔与本金合；
4. 同时记录原1829协议日期“29六月”对1884重述“23六月”时间冲突。

**BLOCKED/NOT_ACQUIRED：** 1790 AHFT C25_010原始王室决议官方PDF尝试失败（超113MB，平台拒绝）；1791 BNE原页403；1795港口贷款原始公证书、1839港口工程结算原件、1829银行清偿会计原始凭证、1807 Banco Real Hacienda 资金账、UKDS g104spd3等均未获取。

**NOT_RUN**：控制战争、英国海上封锁、政府债务与银行自营投资风险的因果模型、私人信贷被主权信用挤占、中央债息实际支付对西班牙海军投入的挤出；不把政府已付40m等同战时债息。

**唯一下一动作：** 优先通过合法开放的**1795年瓦伦西亚格劳港工程委员会原始借款合同、国库/港口结算簿或独立正式印本**复核1884转引的 **300雷亚尔合同总额差异**，并锁定其中原债务人和王室是否直接承诺保证；有此同一主体的债务链后，才能把银行 *Obras Públicas*、*Real Hacienda* 项按可核口径勾稽入1829最终重组账。1790/1791已定位原始会议簿继续作为平行受阻材料，不另建任务、不发送无授权的私人档案请求。保留 Issue #32 OPEN 和 Draft PR #36。


---

## M2k corrective adjudication addendum (2026-11-14): FINAL 1887 judgment now read

**1884 Treasury's initial refusal was NOT the last legal decision.** The official original [26 November1887 Gaceta, printed pp557–559](https://www.boe.es/gazeta/dias/1887/11/26/pdfs/GMD-1887-330.pdf) has now been VISUALLY CHECKED through actual page screenshots. The Regent's **24 October1887** decision for Consejo de Estado administrative-contentious court **upheld the 1884 refusal** of Banco de España's *carga de justicia* claim, and **declined the Government counterclaim on PROCEDURAL grounds**. Its core holding was **1829 bank–Crown settlement extinguishment**; not a factfinding that sovereign finance/tax administration never participated.

**1887 adds key earlier exposure:** 1794–95 royal orders solicited and approved the bank-funded port works contract (still signed by Bank and separate Valencia port Junta), with earmarked port consular and silk levies plus **1237 pledged Propios y Pósitos shares**; 1802 royal revenue agents collected assigned tax proceeds for onward transfer to Junta and 1817/18 orders addressed arrears and possible conditional Treasury responsibility. Thus M2j's accurate **DIRECT_1795_BORROWER_IS_PORT_JUNTA** finding must not be overstated as **NO_POSSIBLE_CROWN_CONTINGENT_OR_TAX_PASS_THROUGH_LIABILITY**. Conditional duty and state tax collector default require original orders and account books.

**1887 certified repayment details:** the case cites the 1862 public accountant certificate recording **13,703,208 nominal reales received by Bank over 1797–1836**, while 1839 local Junta still listed 4.503m arrears. Those are different cash/paper/period dimensions, not one subtractable bank P&L series.

**1884 source 300-real mismatch is still UNRESOLVED:** 1887 printed p558 visibly gives *2.968.575 reales y 5 maravedises* for the contract total, apparently dropping leading '1' from the 12m expected amount. Its last component digits align with derived **12,968,575** more than 1884's printed **12,968,875**, but neither court publication is the original **1795 notarized contract**. Don't silently fix 1884, 1887 or historic legal loan fields. See the full [M2k source audit](M2K_1887_FINAL_JUDGMENT_PORT_CREDIT_TAX_AND_BANK_RECONCILIATION_20261114.md), [legal responsibility matrix](port_loan_legal_attribution_matrix_m2k.csv) and [nominal repayments](port_loan_nominal_repayment_m2k.csv).
