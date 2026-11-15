# CASE-FRA-001｜M3-A2：1803–1804预付款争议、法方收款函与债券交割数字异常（2026-11-14）

**规范 Issue：** https://github.com/fweiger/AI_book/issues/35；**保留 Draft PR：** https://github.com/fweiger/AI_book/pull/39；在已有M3-A合同审计基础上仅做证据增量，不重复建立研究任务。

**最高新发现：** 1902年美国官方出版的James Monroe通信目录（据当时在Department of State收藏的原件编成）列出1803-07-31、09-09、09-11的**提前付款承诺及其授权争议**，以及1804年4月Barbé-Marbois致Hope & Co.确认领土转让款项收讫的**法语书信副本**。这提供新的**原始函件定位**，但**只读到目录摘要，没有取得原函、签名和收款面额；不得称已验证法国实收金额**。

## 一、对应前一轮10m预付款的关键外交信件（目录摘要，不是原信全文）

来源：[1902美国政府出版《Calendar of the Correspondence of James Monroe》Library of Congress bibliographic item](https://www.loc.gov/item/06037999/)；相关原书 **印刷p134**在两个馆藏扫描中均有搜索索引：
- **1803-07-31 Robert R. Livingston→James Monroe**：目录称Marbois提及Monroe关于提前支付的允诺；Livingston反对但不准备否认Monroe先前做出的承诺。**只可证明预付款承诺存在的档案线索，不能确认银行真的垫付**。
- **1803-09-09 Livingston→Monroe**：目录说明Livingston担心提前支付保证的责任与对美政府的约束性。
- **1803-09-11 Livingston→Monroe**：目录说明他怀疑美方使节是否有权签署该保证，但曾提出签署及修改文本。

这揭示**法律/授权层面和金融结算层面之间的关键区别**：法国政府若希望提前收到资金，美国使节做过何种担保，银行承兑条件和美国财政部证券交割怎样衔接？它绝不是已经给法国收款的证据。三个摘要来自**同一1902年编辑出版物，扫描两次不产生独立证据**。

参考： [1902扫描A p134](https://upload.wikimedia.org/wikipedia/commons/8/82/Calendar_of_the_correspondence_of_James_Monroe_%28IA_calendarofcorres00monr%29.pdf)、[1902扫描B p134](https://upload.wikimedia.org/wikipedia/commons/7/7b/Calendar_of_the_correspondence_of_James_Monroe%2C_prepared_from_the_originals_preserved_in_the_Department_of_State_%28IA_cu31924032751665%29.pdf)。原始逐封书信应由 Monroe Papers / US State Dept. 卷宗核实。

## 二、新的法方收款原件线索：April 22 / April 28 冲突尚未解决

同一原书**印刷p164**关于 `MARBOIS BARBÉ — to HOPE & Co.` 的记录：
- 一份搜索索引显示 **1804-04-22**，内容为路易斯安那割让资金收款确认，法语副本一页；
- Cornell数字扫描索引却显示 **1804-04-28**，标题及页数相同。
- [美国国家档案馆《Jefferson Buys Louisiana》](https://www.archives.gov/publications/prologue/2003/spring/louisiana-purchase.html) 亦记录 **1804-04-28** Barbé-Marbois向Hope & Co.出具`quitclaim`。

目前**不能判断是否OCR把28误作22、原刊字样存在差异、或这封法语收款函是否就是NARA所指quitclaim**。原书的网页PDF截图不可取，故仅标记`DATE_CONFLICT_OPEN`。虽然4月28因NARA有另一路来源而更值得首先核查，**本轮不擅自改写4月22/28冲突，也不将两者计作独立收款记录**。

最重要的是，目录只说“acknowledging receipt of funds on account of”而非“full settlement”。**缺少收款面额、到账日、收款账户和清偿范围，仍不能以此证明法国收到50.35m法郎**。

## 三、美国原始债券交割文件出现需严查的面额冲突

[NARA官方实施史](https://www.archives.gov/publications/prologue/2003/spring/louisiana-purchase.html)记载美国财政部1804-01-16发出共`$11,250,000`的6%公债，其中`$3,750,000`给Baring、`$7,500,000`经Nicholson/Leonard运往巴黎，并说明1804-02-13由Leonard出收据。

但是[NARA网站另一份标为1804-02-13的单页收据PDF](https://www.archives.gov/files/historical-docs/doc-content/images/louisiana-purchase-receipt.pdf)**网站文本抽取**反复显示`Seven Millions six hundred thousand Dollars`，即`$7,600,000`。若照字面相加，`7.6m + 3.75m = 11.35m`，比NARA公开的批准总额及契约票面`$11.25m`多出**$100,000**。

**证据级别是`INDEXED_TEXT_CONFLICT_NOT_VERIFIED_IMAGE`，不能推定历史真正超额发行**。PDF截图工具和当前容器访问失败；需要实际目视原始签收手稿、附件证券编号清单，以及NARA展览提到的**Livingston于1804-04-25签发的股票收据**。仅从数字矛盾不可推断欺诈或挪用。

此处的USD是美债票面本金，不是银行向法国支付的法郎，也不是另一笔法国财政收入。

## 四、未取得的档案如何打开

[Baring官方Northbrook收藏说明](https://baringarchive.org.uk/the-archives/northbrook-papers-business-papers/)确认整套NP1 Business Papers已数字化，直接指向 [Preservica数字馆](https://baring.access.preservica.com/)；本轮网页访问遭403/robots拒绝，**无法声称已读取`NP1.A4.34`和`NP1.A4.48`手稿**。按照 [Baring官方访问指南](https://baringarchive.org.uk/about/how-to-access-the-archive/)，馆方开放以预约为主的原件研究；数字门户无对应可访问文件时，可按具体档号向档案管理员申请电子副本或咨询浏览权限。

最优先原件：
1. **Monroe原件**：1803-07-31、09-09、09-11三信；区分财政部有授权的担保与使节的个人允诺。
2. **Marbois→Hope**：1804年4月（22/28冲突）法语收款确认副本，明确票据金额/是否终局。
3. **Baring NP1.A4.34 / NP1.A4.48**：10m预付款归还与1804资金计算；相互对账。
4. **NARA RG58**：1804-02-13 Leonard收据及附表、1804-04-25 Livingston收据，确认7.5/7.6差异。

## 五、严格的时间先后约束

即便最终证明法国在1804年4月完成大量收款，这笔**1804年收款不能在无早期过桥融资证据时直接用来解释1802年Leclerc远征已经发生的开支**。1803年上半年、秋季军事资金来源应独立对账；合同价格与事后收款不能倒灌至此前战争支出。

**新增结构化证据**：[louisiana_receipt_guarantee_source_leads_m3.csv](louisiana_receipt_guarantee_source_leads_m3.csv)（12条；含日期冲突及面额冲突）。原M3-A的21条现金/证券事件表保持不动，以防把新增**目录索引**混入历史**实际支付**事件。

**验收结论**：目录及来源定位`PASS`；存在日期/面额候选冲突`OPEN`；法方收款函原件、预付款实际支出、银行垫资核销及法国国库净现金`NOT_ACQUIRED`；帝国财政因果`NOT_RUN`；Draft PR 保持开放。
