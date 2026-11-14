# CASE-NLD-001 · M4A-01：1772—1773年复现数据获取审计与Clifford融资到期链

> 日期：2026-11-14；规范研究Issue [#33](https://github.com/fweiger/AI_book/issues/33)，沿用[Draft PR #37](https://github.com/fweiger/AI_book/pull/37)。阶段状态 `PARTIAL`。**本轮只独立复算已发表表格的算术，不是获取18世纪原始价格/公证/银行账，也不是战争因果估计。**

## 1. 新发现：作者正式发表的可下载复现包入口

[Berre & Kosmetatos (2025), Economic History Review, DOI 10.1111/ehr.13345](https://onlinelibrary.wiley.com/doi/full/10.1111/ehr.13345) 官方 Supporting Information 明列：

- `ehr13345-sup-0001-Appendices.docx`，出版社标注62.7KB；[官方直接链接](https://onlinelibrary.wiley.com/action/downloadSupplement?doi=10.1111%2Fehr.13345&file=ehr13345-sup-0001-Appendices.docx)；
- `ehr13345-sup-0002-Replication.zip`，出版社标注1.9MB；[官方直接链接](https://onlinelibrary.wiley.com/action/downloadSupplement?doi=10.1111%2Fehr.13345&file=ehr13345-sup-0002-Replication.zip)。

同一页面 Data Availability Statement 称复现包包含 **five spreadsheets**，来源由各表内部标明。**网页上的文件名、文件大小和说明已经核实；当前执行环境直接获取均返回HTTP403，ZIP/DOCX字节 `NOT_ACQUIRED`，五份表及其数据粒度尚未检查**。附录可能使1772年EIC事件时点可更精确复核，但未取得前不能使用任何未经实见的单日股价数字。使用受许可数据需尊重其访问条件，禁止绕过认证、也不把论文配套研究数据冒充18世纪原始手写账。

次级路径：[ICPSR 1008](https://www.icpsr.umich.edu/web/ICPSR/studies/1008/summary) Neal伦敦/阿姆斯特丹市场价格；[UKDS 5690](https://doi.org/10.5255/UKDA-SN-5690-1) Bowen `Stock_Prices`、`Stock_Transfers_Monthly`；英国图书馆 `IOR/L/AG/14/7/1`。三者的**实际价格数值文件均未取得**。

## 2. 已完成的数值复核：论文Table 1公证拒付汇票样本

已发表[Table 1](https://onlinelibrary.wiley.com/doi/full/10.1111/ehr.13345)将1772Q4至1773Q1抽样拒付票据（单位 **current guilders**）列为：

| 指标 | 1772 Q4 | 1773 Q1 | 此轮重算 |
|---|---:|---:|---:|
| 英国起源拒付面额 | 178,822 | 1,345,057 | **+652.1765%** |
| 所有起源样本拒付面额 | 1,693,324 | 4,161,887 | **+145.7821%** |
| 英国面额占当季总面额 | 10.5604% | 32.3184% | **+21.7580个百分点** |
| 公证样本记录数（所有起源） | 158 | 78 | **减少80条** |

在 **Q4→Q1样本总拒付面额增加2,468,563盾** 中，英国起源拒付面额增加 **1,166,235盾**，数值上占增量 **47.2435%**。这只是作者样本的金额构成分解，**不是可归因于英国的危机因果占比**；不同季度抽样记录数发生变化，不能机械将面额变化推广为所有市场汇票拒付发生率，也不能依该聚合样本做显著性推断。原表Q2 1773英国数值为破折号，保留 `NOT_REPORTED`，不等于历史0。M3L已经核对的单季逐地区合计±1盾出版物差异继续保留。

此外，原文Tables 2/3各注明1766—73年obligatie公证抽样 `n=795`；正文III段另记1772年6—12月Seppenwolde财团3.25m盾、**796**份EIC支持的obligaties。**两处不应未经样本定义核对便当作同一总体，也未证实作者错误**。需用官方Appendices和Replication ZIP确认调查总体、公证记录筛选、观察单位、时间范围与可能的分母差异。

数值重算程序：[`voc_m4a_published_table_validation.py`](voc_m4a_published_table_validation.py)，在本轮本地Python实际执行，所有既定算术断言PASS；未运行价格因果模型。

## 3. Clifford的跨市场资金到期链：可见证据与严禁加总的事项

根据论文III节：1772年春夏AWB获得的银币转为银行货币资金流约520万银行弗罗林，其中Clifford存入83万，由其向银币交易商借助汇票融资；1772年9月末至10月，新债权人帮助Clifford向旧债权人支付 **340万银行弗罗林**，并再筹得 **40万**，其中 **25万**拨给财团应付EIC抵押融资追加保证金。按作者叙述，25万/40万=**62.5%**，只是新筹得40万这一款项的用途占比，**不能对340万支付额再求和推算净融资或同时期账户余额**。

另据论文：obligatie期限通常6—12个月，而新签短期汇票约90天，9—10月借入到12月底集中到期。Clifford AWB余额1772年12月初跌至**低于10万银行弗罗林**；12月15日Dreyers要求Clifford支付171,000 **current guilders**汇票并被拒付，12月28日Clifford失败，拒付事件激增。**银行弗罗林与普通荷兰盾严禁直接相加**；付款日期、签票日与公证拒付记录日应分别建事件列。

BOE在1772年6月据作者估计通过贴现和紧急贷款提供约£650k，涉及无法收回票据/担保损失约£93k，两者的**简单金额比14.3077%仅是来源报道金额之比**，不是银行同口径违约损失率、净财政成本或与AWB贷款本金可直接比较的指标。需原BOE档案核对期间与计量范围。

作者还描述1772年9月丹属西印度群岛飓风消息传至荷兰，ter Borch抵押证券拍卖价格约面值80%，低于先前90%的抵押放款比例；这提供了**与EIC价格不同的殖民抵押品风险通道**。但它不识别整场金融危机的唯一触发因素。

## 4. 数据准入、样本争议与下一项动作

| 指标/判断 | 当前状态 |
|---|---|
| Wiley正刊复现包与附录**存在的链接** | `SOURCE_LINK_VERIFIED` |
| Wiley ZIP及DOCX实际文件与哈希 | `NOT_ACQUIRED_HTTP403` |
| 1772Q4→1773Q1出版表算术 | `PASS_PUBLISHED_TABLE_ONLY` |
| 795公证样本 vs 796 obligatie观察范围 | `UNRESOLVED_SAMPLE_SCOPE` |
| EIC 1772 June高点至Dec约−27%独立报价重算 | `NOT_RUN` |
| 1772逐笔追加保证金与公证档案原页 | `NOT_ACQUIRED` |
| VOC银行与英国EIC跨主体计量对齐/战争ATE | `NOT_RUN` |

下一项 **M4A-02**：从期刊附录和ZIP先提取文件目录、工作表名、来源字段、时间/币种/数据许可，记录SHA256、原始表行数与缺失；优先针对1772Q4—1773Q1重新校对样本范围及每日日度拒付/价格时点。若期刊渠道持续受阻，再经授权走作者数据请求、ICPSR1008或UKDS5690的合法登录路径。保留PR草稿、不合并main，历史因果结论不升级。

本轮新增文件还包括[观察与逻辑边界表](voc_m4a_1772_funding_cliff_observations.csv)与[下载访问审计](voc_m4a_supplement_access_audit.csv)。
