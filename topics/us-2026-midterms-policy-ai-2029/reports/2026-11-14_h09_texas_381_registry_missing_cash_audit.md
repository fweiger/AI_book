# H09｜Texas Comptroller官方381协议：金额字段确认为空，不能用签约估值算9%扣留（2026-11-14）

## 一手官方备案查询
通过Ubuntu MCP下载并解析 [Texas Comptroller Chapter 380/381官方CSV](https://assets.comptroller.texas.gov/open-data-files/ch380.csv)：全文件3,969,329字节；SHA256 `490d64ee6426910aff16eefefc9a3c6b208ad40f18643549465dafe51d3791d7`；43个字段，找到**唯一**对应记录 `agreement_id=0005328` / `Colorado River Project LLC` / `Travis County`。
官方[项目详情](https://comptroller.texas.gov/economy/development/search-tools/ch380-381/economic-development-agreements-details.php?agreement=0005328)能复核登记主体与字段。

| 字段 | 真实州登记值 | 正确处理 |
|---|---|---|
| 合同生效 | 2020-07-14 | 2026选举以前 |
| 州CSV结束日期 | **2041-12-30** | 县原始签署合同记载**2041-12-31**，日期有1天源冲突，保留待查 |
| 州CSV登记状态 | Active | 同行最后更新时间是**2022-05-01 12:22:00**，不可据此证明2026最新状态 |
| 总合同金额`totl_agmt_am` | **空白** | NOT_REPORTED、不是0，也不是县级实际发放额 |
| 资金来源`srce_fund_tx` | **空白** | 不能把县合同计算口径当州数据库真实付款记录 |
| 历年grant实付 | **没有该列** | 必须取得县Auditor和PBO分年付款凭证 |

[单行审计记录](../cases/musk-2026/texas_comptroller_0005328_registry_snapshot.csv)，保留源SHA、版本日期与差异。该州数据库主要保存**协议登记**，不是县级每笔财政支付台账。

## 9%的USD金额仍缺
2026-04-07县书记官正式[会议Item26](https://traviscotx.portal.civicclerk.com/event/3609/files)已确认：对于**2020、2021、2022履约年度符合资格的grant资金扣留9%**，4票赞成、0反对、1弃权。**但没有取得上述3年每年的eligible grant美元、核准款、实付现金和是否已经发放后再追回**，所以绝对损失`NA`，不能人为填0。

当地[KUT 2026-04报道](https://www.kut.org/austin/2026-04-08/austin-tx-tesla-travis-county-tax-rebate-agreement)转述2020签约时县预计前10年优惠**约1,400万美元**，这是多年**原始预测**，并非实际2020—22应发款。绝不能用`14m×9%=1.26m`冒充扣留金额。已建[2020/21/22逐年五类资金账本](../cases/musk-2026/travis_2020_2022_grant_cash_reconciliation.csv)，原始金额未知则留空。

**学区税基限制是另一条法域**：[Texas Comptroller Del Valle ISD Chapter313 #1496](https://comptroller.texas.gov/economy/development/prop-tax/ch313/agreement-docs-details.php?id=1496)，与此Travis County Chapter381不能求和/复制数据当一份现金补助。

## 数据路径与未执行的官方申请
[Travis County Financial Transparency](https://financialtransparency.traviscountytx.gov/)提供Vendor Payment Details与Economic Development统计，但本轮Ubuntu访问出现TLS超时，**没有获得可核验的公司支付清单**；不得据此称支付为零。若官方门户无记录，按照[县审计办公室公开记录申请说明](https://financialtransparency.traviscountytx.gov/Mist/OpenRecords)申请：

- Agreement `0005328` / Colorado River Project LLC的`Performance Year 2020, 2021, 2022`各自的税款实缴、Grant Eligibility计算、审批、县支付日期/金额、已扣留或追回金额与凭证；
- 2026-04-07 Item26通过后执行的County Judge文件和付款调整分类；
- 2023—2025对应监管/支付版本以供选举前趋势对照。

**没有发送申请邮件或表单**，这只是已登记的研究取证任务；避免未授权对外发送。

## 初步判定
H09的“确有2020原始合同、2026-04有正式9%扣留动作”属于核实事实；“2026选后政治转向导致扣留”“已经追回多少美元”“这些优惠直接造成Tesla集团偿债困难”等因果或财务主张**没有成立的证据**。H09仍UNTESTED。