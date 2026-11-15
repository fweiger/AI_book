# CASE-FRA-001｜M2：历史财政来源依赖审计与Manuel商品栏命名（2026-11-14）

**权威 Issue** https://github.com/fweiger/AI_book/issues/35 · **现有 Draft PR** https://github.com/fweiger/AI_book/pull/39

## 1. 关键问题：跨刊本加总一致≠独立交叉验证

此前建立的Marbois1790/ Laborie1798/ Manuel2005之间有数值相等与相近，并不能据此推论三份统计独立：**Manuel Table2-4直接以Marbois的1788–1789《État général des Cultures et Manufactures》为数字来源**；Laborie1798虽然独立出版，但很可能引用同一殖民行政账，直接复制来源尚未证明；Ardouin1853也是后期回顾史著。要区分：
- `crossfoot_independent_calculation`：将同书行列、货币分位重算，可查算术错误；
- `cross_publication_transcription`：另外一本书引用同一行政底稿，可查转述或刊本差异，**不能当两次独立测量**；
- `independent_primary_account`：真正不同会计主体/账户（例如地方收税员原日记账与法国王室Trésor实际收款单据），需逐项证据和同期间对账才可能支持交叉证实。

详见[八条来源依赖和独立性CSV](source_lineage_dependency_m2.csv)。最重要的原始独立账簿 **AN G¹46*** 仍然只定位了目录，未拿到1788原始款项，不能让Marbois→Laborie→Manuel的反复引用替代它。

## 2. Manuel2005 Table2-4：可以确认列名但不能保证PDF OCR小数正确

[佛罗里达大学官方PDF](https://ufdcimages.uflib.ufl.edu/UF/E0/01/16/50/00001/manuel_k.pdf) **PDF第33页（0-index，阅读器第34页），论文印刷p.25的Table2-4**，可搜索PDF文本已明确显示商品列：
1. `White/Clayed Sugar`（白砂糖/成型糖）；
2. `Raw Sugar`；
3. `Coffee`；
4. `Cotton`；
5. `Indigo`。
重量栏为 **thousands of pounds**，税额为 **per 1,000 colonial livres**。原PDF页面的截图请求失败，文本标签是`PDF_EXTRACTED`而非`PAGE_IMAGE_VERIFIED`，不把这些历史pounds未经核对换算成现代avoirdupois或公斤。

[重新带商品列名的5行CSV](manuel_1788_commodity_labeled_m2.csv)严格保留先前数字：北91,196/91,196；西110,377/110,377；南五项38,244/列报39,279差1,035；殖民地五项239,817/列报240,852同差1,035；Jérémie五项5,138/列报6,212差1,074（单位千磅）。三地区按每个商品列纵向求和均与殖民地单商品列一致；**不能将差额擅自填到靛蓝、棉花或其他商品**。需要原页确认究竟印刷有错，还是搜索文本抽取有漏列或错列。

## 3. 新发现同一1804图册另一份独立影像保藏地点

美国David Rumsey历史地图收藏的**同一《Statistique générale et particulière ...》1804年图表册**，有：
- **No.IX / 编目4003.014**：*Denrées coloniales, portées en France en 1788, par 686 navires jaugeant 219.122 tonneaux*。标题上的686艘和219,122登记吨位只是**法国接收殖民商品的全体船舶**，非Saint-Domingue单岛，也未获得每种货品金额；
- **No.X / 编目4003.015**：*Commerce des colonies en général*，有进出口表格，可作为不同扫描母本的**视觉对照入口**。

来源：https://www.davidrumsey.com/luna/servlet/view/all/who/Poirson%252C%2BJ.B./?sort=Date%2CPub_Date%2CPub_List_No，同作品的[另一数字化复印件](https://upload.wikimedia.org/wikipedia/commons/f/fa/Statistique_g%C3%A9n%C3%A9rale_et_particuli%C3%A8re_de_la_France_et_de_ses_colonies_..._%28IA_b2201763x%29.pdf)。两者是同一历史统计作品、不同馆藏/数字扫描，**不是独立历史税收数据**。当前仅有Rumsey馆藏元数据，未获得4003.014/015的高清单元格；不能据此宣布上一轮数学候选值56,000→36,000和53,000→58,000已被证实。

## 4. 验证门槛及交接

- 取得Manuel PDF P33表的清晰图片，核准五种商品和南部/Jérémie重量残差；
- 取得1804年Rumsey版 No.X 与另一版本的同一跨国贸易表，视觉确认版式是否包含此前Guadeloupe×Denmark、Tabago×Holland残差；**No.X未被确认就是此前逐国籍表，需要先目视匹配标题**；
- 独立于Marbois体系的法国本土 **AN G¹46*** 1788实际收付账本，及美国1803路易斯安那原始条约文书属于**不同的财务/法律事件和期间**，不可自动拿来交叉校正1788单岛收入。

**状态：** 来源依赖关系和商品栏文字`VERIFIED_AS_TEXT`；原PDF/atlas高清页像`NOT_VERIFIED`；现有差额`OPEN`；王室1788可用现金`NOT_ACQUIRED`；历史因果`NOT_RUN`。
