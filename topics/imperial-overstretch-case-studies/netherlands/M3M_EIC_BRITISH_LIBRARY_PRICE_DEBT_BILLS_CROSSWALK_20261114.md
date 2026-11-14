# CASE-NLD-001 · M3M：英国东印度公司独立原始账簿来源、1786印度债务汇票与1772证券价格对照设计

> 2026-11-14。唯一规范研究[AI_book Issue #33](https://github.com/fweiger/AI_book/issues/33)，保留原[Draft PR #37](https://github.com/fweiger/AI_book/pull/37)。本轮并未拿到证券交易或现金账簿的实际数据行。状态：`ORIGINAL_ARCHIVE_SHELF_MARK_VERIFIED`、`PUBLISHED_DATA_GUIDE_READ`、`BRITISH_COMPANY_CAPITAL_HISTORY_FROM_GUIDE`、`DATA_FILE_BYTES_NOT_ACQUIRED`、`EVENT_STUDY_NOT_RUN`。

## 1. 从仅有历史价格文献转向可实际核对的第二套英国证券档案
上轮M3L新资料称1772年英国东印度公司(EIC)股票从6月高点到12月下跌约27%，该数字**仍未由本研究独立重算**。本轮找到独立于 Larry Neal 的第二项明确价格收集体系：英国图书馆印度事务原卷`IOR/L/AG/14/7/1`，目录名 *Prices of East India stocks and bonds on each day from 1 Oct 1732 to 28 Feb 1838 and the rates of dividend paid from 1709*，[英国图书馆馆藏记录](https://searcharchives.bl.uk/catalog/040-000967914)。原始卷档案范围1732—1838，作者Bowen将其复核编辑成可量化的1755年1月至1838年2月**998个当月最后交易日股价**，每份名义£100 EIC股票报价以英镑表示；同日有价格区间，则采用**最低报价**。[Bowen UK Data Service Study5690 官方18页方法指南](https://doc.ukdataservice.ac.uk/doc/5690/mrdoc/pdf/guide.pdf)原印p16 Spreadsheet25。

精确完整性预期是：`(1838−1755)×12 + 2 = 998`个**日历月份**，与指南公布的**998 entries**相符；但这只是日期范围与发表条目数的一致性，并不等于本轮已经检查998行均有数值、无缺失或无重复。

**关键事件研究口径陷阱**：M3L的`英国EIC股票1772年6月高点→12月底约−27%`不能用Bowen单纯的`6月最后交易日价格→12月最后交易日价格`直接替代，因为前者基准是**6月盘中/月内高点**，而后者在最后交易日取**区间最低价**。未来需查看原始英国图书馆1732–1838日度股价卷或Neal当代印刷报价的6月峰值与12月逐日记录，再核对股息发放日、名义资本变动和伦敦—阿姆斯特丹交易时差，才能真正复现跌幅与保证金触发。

另一路 Larry Neal [ICPSR1008](https://www.icpsr.umich.edu/web/ICPSR/studies/1008/summary)为现成的当代印刷 *Course of the Exchange* 与阿姆斯特丹新闻价格文献数据，ICPSR官方明确称此版为**public use一般公众可访问、无需会员机构归属**；而同一Neal资料的旧英国分发版本[UKDA3211](https://doc.ukdataservice.ac.uk/doc/3211/mrdoc/UKDA/UKDA_Study_3211_Information.htm)历史文档则要求英国居民或英国机构身份。**两种平台的分发权限不同，不是两个价格研究样本**。本轮实际网页下载受JavaScript/账户界面限制，两个研究项目价格数据文件均`NOT_ACQUIRED`；不得传输或私自复制受限制数据文件。

## 2. 英国EIC数据库UKDS5690：27个真实有编号的历史来源工作簿
H.V. Bowen *East India Company: Trade and Domestic Financial Statistics 1755–1838*，UKDS SN5690、DOI[https://doi.org/10.5255/UKDA-SN-5690-1](https://doi.org/10.5255/UKDA-SN-5690-1)，根据大英图书馆**贸易簿Commerce Journals** `L/AG/1/6/14–29`、**现金簿Cash Journals** `L/AG/1/5/17–34`、**总账General Ledgers** `L/AG/1/1/20–31`、股权转让登记 `L/AG/14/5` 与股价卷 `L/AG/14/7/1`，构建了**27个Excel 2003工作簿**。数据指南网页PDF文字内容完整可读，其中印刷p3截图已成功目视确认账年与原目录的核心说明，其余相关页按工具文字提取审阅、未宣称全部图片目视核对。

工作簿结构完整录入[voc_ukda5690_eic_27_workbook_schema_m3m.csv](voc_ukda5690_eic_27_workbook_schema_m3m.csv)。核心工作簿：`Stock_Prices` (998 month-end observations documented); `Stock_Transfers_Monthly`（月度笔数与转让名义股票价值，**不是市场成交金额**）；`Income_Sales`（伦敦公司自营商品**销售的毛现金收入**）；`Income_Total`（伦敦总现金流入）；`Payments_Bills_of_Exchange`（海外汇票**已兑付本金及利息现金**）；`Payments_Dividends`（已经支付给股东的股息）；`Payments_Duties`（包含为获许可私商代收代付税费）；`Exports_Total`与`Imports_Total`（**历史invoice账面价而非现金实收**）。

**最大会计口径纠偏**：1760—1814年EIC出入货物invoice一般在实际采购价基础上加入约**10%**的名义运输和整备成本；发票价与收货卖价不是同类交易。Bowen特别说明 `Income_Sales` 是销售收款、尚未扣除关税、运费及附加成本，而且不含由私人商人委托公司代售货物的现金；`Income_Total`是现金流入也不是公司利润。不能用`British invoice price - VOC Asia cost`解释成本优势，不能把英国EIC公司销售当英国国库财政收入。详见 [官方指南印刷pp4, 12](https://doc.ukdataservice.ac.uk/doc/5690/mrdoc/pdf/guide.pdf)。

**重要会计年度边界**：1813年前英国EIC以**7月1日至次年6月30日**为财务年；因此‘1780年度’在这套表中实际是1779-07-01到1780-06-30，早于第四次英荷战争于1780-12-20正式开始。荷兰VOC本土记账年常为4月中旬结账，阿姆斯特丹汇兑银行为1月中旬结账，BGB亚洲账为8月31日结账。以上不是同样的`year=1780`样本；不可直接拼成年份相同的双差分。股票转让与股价月份按**自然月**，与财务年不一致。

## 3. 同为殖民贸易公司，英国EIC从1786年也开始把海外债务转为伦敦兑付汇票
本轮直接由Bowen指南 **Spreadsheet21（印刷p14）**确认：EIC在加尔各答从**1786年**起签发有息`India Debt Bills`，以向英国伦敦转移印度本地**卢比债务**，后来马德拉斯又发行`Carnatic Debt Bills`。这与VOC在1782—1783年通过阿姆斯特丹汇兑银行延展和债券化银行贷款的经验形成新的机制比较：**两家东印度公司均面临跨币种、跨地域、跨期限的殖民债务筹资问题**，区别在于融资机构、债权人、法律关系及担保方式。

**范围特别注意**：Bowen的专门`Payments_Bills_of_Exchange`第二工作表只在**1790—1834年**单列更多债务/非贸易票据的实际伦敦兑付款项；不能以第二表1790年才开始推断债务票据也是1790年才开始发行。指南明确承认，某些贸易汇票与债务汇票无法完全分离，**1809年后部分未偿India Debt Bills已按普通汇票处理**。因此单一账项付款既不一定是贸易支付、也不一定代表新殖民地资本流入或净增债。先取得实际年度表及原伦敦兑付凭证才可能计算跨洋债务转移现金额。此机制存于[voc_eic_debt_bills_and_accounting_regime_m3m.csv](voc_eic_debt_bills_and_accounting_regime_m3m.csv)，不编造未读金额。

## 4. 英国EIC股本扩张的真实历史数额：不能与VOC银行借款相加
Bowen指南**Spreadsheet22 印刷p14**给出英国EIC已缴股本：

| 时间 | 英国EIC名义已缴股本（英镑） | 相较前次增加 | 比例 |
|---|---:|---:|---:|
| 1786年之前 | £3,200,000 | — | — |
| 1786年后 | £4,000,000 | £800,000 | +25% |
| 1789年后 | £5,000,000 | £1,000,000 | +25% |
| 1793年后 | £6,000,000 | £1,000,000 | +20% |

1786年前到1793年后的名义已缴股本合计**增幅87.5%**，**不是公司盈利率，也不等于同期英国国库获得的收入**。这与VOC 1782年在阿姆斯特丹银行重组的765万**银行弗罗林贷款本金**分别是英国EIC公司股本**权益存量**和荷兰银行**债权存量**，计价货币、借贷主体和债券性质均不同。不能直接两者相除说英国融资能力比荷兰高出x倍。

同一指南记录，在1793年7月以前EIC年度股息率约在名义股本的6%—12.5%之间浮动；**1793年7月以后法定固定10.5%**。这说明制度安排可能影响公司现金支出，**不能把10.5%直接作为实际资本回报或经营利润率**。数据与事件表[voc_eic_1786_1793_paidup_capital_events_m3m.csv](voc_eic_1786_1793_paidup_capital_events_m3m.csv)、[债务汇票与记账制度事件表](voc_eic_debt_bills_and_accounting_regime_m3m.csv)。

## 5. 已建立七个VOC↔英国EIC关键变量的跨案例对齐表
[voc_anglo_dutch_source_comparability_m3m.csv](voc_anglo_dutch_source_comparability_m3m.csv)逐一映射(1)1772 EIC股票与荷兰追加保证金；(2)股票转让笔数与抵押债样本；(3) VOC亚洲出发货物采购价值与EIC伦敦进口发票价；(4) VOC银行贷款重组与英国EIC已兑付海外汇票；(5) VOC按1800年不变价计商品交易额与EIC名义销售现金收入；(6) EIC 1786—93名义已缴股本扩张与VOC债务重组；(7) 独立价格原始簿 vs Neal当代印刷报价。

每条明确注明：**经济主体、真实货币、计量性质（存量/流量/价格）、财年、史料等级和未来实证所需的额外对账**。英国EIC原账并不能无解释地充当荷兰VOC的反事实实验组，两家公司在东印度殖民治理、货物组合和国家政治关系上存在结构差异。

## 6. 原件与数字化阻断以及复现入口
[voc_eic_market_prices_archive_access_m3m.csv](voc_eic_market_prices_archive_access_m3m.csv)说明两套具有不同许可条件的EIC历史报价路径、英国图书馆实体原卷、Bowen 5690与Neal ICPSR1008；[source_registry_m3m.csv](source_registry_m3m.csv)记录五个有来源定位的证据等级。Bowen研究的数据指南**可公开下载与阅读**，但UK Data Service的实际27份Excel文件下载可能需登录或接受许可，**本轮未获取文件字节或验证该数据集每份工作簿的开放级别**。ICPSR说明研究1008的public-use文件一般公众可获取，但是网站依赖JavaScript、当前网络读取接口无法取得真实文件；UKDA3211旧版分发可能限英国居民及机构，不能擅自绕过其单独许可。

所有27工作簿名属于**指南已发表表目录**而不是我们创造的数值数据。998月末价格是指南声明，实际从**1755年1月到1838年2月**；不存在任何本轮推造的1772年股价观察、月收益率、英国EIC年度净债务，也没有真实运行相关性/因果回归。`BOWEN_DATA_GUIDE_READ=PASS`、`EIC_NUMERIC_FILES=NOT_ACQUIRED`、`1772_PRICE_FALL_INDEPENDENTLY_REPLICATED=NOT_RUN`。

## 7. 下一项唯一工作与反证
优先从UKDS SN5690合法取得**`Stock_Prices`和`Stock_Transfers_Monthly`两份工作簿**，或通过独立公共访问路径取得Neal ICPSR1008同期间数据，核对**1772年5月至1773年3月**的公司股价月末低价、股本转让笔数/名义金额与M3L荷兰公证保证金、汇票拒付日期；若要重算原文27%‘6月高点→12月底’跌幅，则必须取得英国图书馆IOR/L/AG/14/7/1 **1772年6月每日行情**，不能把月末值伪装为月内峰值。之后再对VOC银行借款月度数据进行严格时间/货币对齐。