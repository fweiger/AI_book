# CASE-ESP-001 — M2h：1790年银行资产质量与分红资本分母审计

日期：2026-11-14。规范 Issue：https://github.com/fweiger/AI_book/issues/32 。沿用 Draft PR #36。

**状态：** ARCHIVE_BASED_PUBLISHED_PDF_PAGES_15_18_VISUALLY_READ / ARCHIVAL_ORIGINAL_ITEM_LOCATED_NOT_OPENED / BANK_1807_ORIGINAL_NOT_ACQUIRED / CAUSAL_TEST_NOT_RUN。

## 1. 新来源及证据等级

Rafael Moreno Fernández (2012), El Banco de San Carlos: la sustitución de los directores en 1790 y el principio de prudencia en el destino del beneficio repartible, AECA VIII Encuentro de Historia de la Contabilidad:
https://www.aeca.es/old/viii_encuentro_trabajo_historia_contabilidad/comunicaciones/003.pdf

本轮通过 web PDF screenshot 成功查看**原出版第15、16、17、18页**。作者追溯当时银行1790年股东大会及财务汇报和Santillán(1865)的重建数据；这是**对历史原账的研究转录**，不是本项目亲自读到的1790年银行原始账本。作者在Banco de España(2014) Estudios de Historia Económica no.67又使用同一批史料，两部文章**不是两套独立原始账**：
https://www.bde.es/f/webbde/SES/Secciones/Publicaciones/PublicacionesSeriadas/EstudiosHistoriaEconomica/Fic/roja67.pdf
本轮2014大型PDF的 screenshot 尝试超时，但可检索原出版文本和脚注。

## 2. 1790年7月6日：340.791百万雷亚尔账簿中已有不可用或高风险项目

作者报告新管理层1790-07-06切账时，四类名义雷亚尔：

| 类别 | 名义雷亚尔 | 占报告总额 |
|---|---:|---:|
| 正常流动及经营项目 | 134,769,661 | 39.54613% |
| 列示损失项目 | 47,017,489 | 13.79658% |
| 可疑汇兑债权 | 18,170,226 | 5.33178% |
| 暂时不能动用的项目 | 140,833,645 | 41.32552% |
| **发表的总额** | **340,791,022** | 100% |

四类原文数字实际加总 **340,791,021**，比源表总额少**1 whole real**。把三类潜在问题项目合并只得到**60.45387%的账面分类占比**，绝非1790年60.45%真实已核销损失，更不能视为现代不良资产率。实际列示损失项目占13.80%，此外有可疑债权和冻结用途的项目，未来收回率未核实。

重要识别意义：至少有一种银行治理与供货合同信用脆弱性在**1793年法国战争之前**就存在，但1779—1783年英西战争等更早军事融资影响仍在，不能从这一天宣布所有战争因素无关。

## 3. 精确账面“亏损—抵补”桥及政府利息的非现金性

原研究第17页列三项（全部名义雷亚尔、历史十进位下1 real=34 maravedís）：

- 已分配十分之一相关亏损：4,901,938 whole reales +20 maravedís；
- 银行自身股份回购溢价损失：5,284,027 whole reales +26 maravedís；
- 军粮/海军补给合同相关损失：36,831,522 whole reales +32 maravedís，作者还注明其中包括向国库**索取但未证明已收取**的利息 7,426,560 whole reales +13 maravedís。
- 逐项计算的损失合计：**47,017,489 whole reales +10 maravedís**。

第18页列用以抵补的四类“利润/资产”：
- 1789年未分配经营利润13,278,117 whole reales +15 maravedís；
- 菲律宾公司股份账面价值21,000,000 whole reales；
- 辅助基金253,106 whole reales +23 maravedís；
- 经王室批准/仲裁的国库应计利息一半3,713,280 whole reales +6 maravedís。
- 逐项加总：**38,244,504 whole reales +10 maravedís**。

按这些明细严格扣除，余额缺口 **8,772,985 whole reales整**，而作者在第18页明确报告**1790经营年度末的资本缺口为8,772,984 whole reales +33 maravedís**，两者相差**正好1 maravedí**。保留 published value + derived value + 1-maravedí mismatch，不擅自修改史料某项。来源全表分类总额还有上述1-real mismatch。

**法律与金融含义**：四类抵补中包含菲律宾公司股份和虽被认可却未核对实际兑付的政府利息，因此这不是38.245百万雷亚尔可用金属现金。该线索提供早期“国库利息应收被用于证明利润/资本完整性”的会计机制，但不能证明1790—1807年为同一连续债权或现金从未支付。

**不同时间截点**：1790-07-06四类账户分组，和1790经营年度末报告的资本缺口不是同一天资产负债表；仅做各自期内来源核算，不做无审计的日期拼接。

见 bank_1790_assets_m2h.csv 和 bank_1790_losses_and_non_cash_bridge_m2h.csv。

## 4. 两届分红不可混为一次：历史资本240m的含义更清楚了

2012年论文第15—18页的决议年份：

| 会议 | 审议利润年度 | 12百万雷亚尔/5%提案 | 状态 |
|---|---|---|---|
| 1790年召开的股东大会 | 1789经营年度 | 1200万雷亚尔，所称5% | **31赞成、210反对，否决**，故不能宣称已付1789年度股息 |
| 随后1791年股东大会 | 1790经营年度 | 相同的1200万雷亚尔，所称5% | 作者记载**获得批准**；本项目未拿到大会原扫描与现金支付凭证 |

两个提案的**隐含可参与分红基数**均为12,000,000/0.05=**240,000,000雷亚尔**。1782章程设计150,000股×2,000=300m；经济上若减少30,000股×2,000=60m，剩120,000股/240m，与隐含分红基数一致。历史出版研究还提到购回30,628股，但**超过30,000股的628股是否另行入账、是否注销、何时注销尚未由原股东簿复核**。

这说明“**1790年代初分红有效基数240m**”可以和“**Fundación BBVA 2005表9.8直到1794仍列账面Capital=300m、1795列240m**”同时存在，而不是强行用某一个年份覆盖另一年份。它使不同资本口径的存在更为可信，但尚不能证明1795恰是法律核销日期。

股息政策变化与1790财政资本缺口同时出现，形成治理风险的新假说；现有发表资料只能证明提议/决议，不能证明同年度真实现金付息或分红已流出。

见 bank_1789_1790_dividend_policy_m2h.csv。

## 5. 档案追查取得可用于实际申请的卷页编号

本轮核实以下**原始来源书目/签号**，均为学者脚注或馆藏元数据，**未直接打开原始银行书页**：

- **1790-04-20**：Banco de España Archivo Histórico, Secretaría, Actas Junta de Dirección (AJD), **Libro 145, folios 289–291**。AECA 2012论文p17脚注19。
- **1790-05-21**：Archivo Banco de España, Secretaría, **Caja 984**；Banco de España 2014历史研究p77脚注111记载国王批准继续购买银行自身股份的相关文件。签号是Caja级，还要请馆员确认具体卷件。
- **1794-07-05**：AHBE, Secretaría, AJD **Libro 154, folios 271–274v**，2014研究p119脚注327—329，涉及30,000与附加628股回购亏损争议；原页未阅览。
- **1790年八届股东大会**的原始印行本：Archivo Histórico Facultad de Teología de Granada 收藏 **ES 18087 AHFT 7-FSAAVEDRA_C25_007**，目录称印本出版1792年，文件**AFT_FSAAVEDRA_C025_007.pdf (322.8MiB)**。独立馆藏网页的主文件元数据已检索到，单件网页访问超时、未实际看见原书影像：
https://archivo.jesuitas.es/index.php/informationobject/browse?genres=14173&onlyMedia=1&places=185456&sort=endDate&sortDir=asc&topLod=0&view=card
- 1790年王室就28 April 股东会请求做出裁定的原始印本已获University of Valladolid 经 Cervantes 的数字馆藏目录定位；实际点击受到Anubis访问限制，故不能引用其未经亲阅的具体命令内容：
https://cervantesvirtual.com/obras/autor/banco-de-san-carlos-espana-94044
- 1808股东大会财务折页的Ateneo de Madrid **A-Caj.179/5**继续作为平行路径，但尚未取得影像。

详细见 bank_1790_original_access_m2h.csv、source_registry_m2h.csv。**本轮即使找到了1790源印本数字母本和原始AJD卷号，也不能把“来源定位”升级为“已经阅读原银行账本”**。

## 6. 反例检验与保留状态

| 机制或判断 | 本轮新增的实际支持 | 仍需证据 |
|---|---|---|
| 帝国战争导致银行全部风险从1797才开始 | 1790已有明显冻结账户、供给损失和回购溢价 | 控制更早战争/新政企合同，用统一会计口径重建1783—1795 |
| 全部银行问题来自政府拖欠利息 | 1790还有军粮供应合约、股份回购溢价及其他不良往来 | 对王室本金、实际应计/已付利息、非主权私人贷款分别审计 |
| 1790资本应直接用240m替代所有账面300m | 分红名义基数240m，但BBVA账面Capital仍300m至1794 | 原始股份登记、实际注销/重分类与1795账簿 |
| 1790已派发1789年度股息 | 同期1790大会以31对210否决 | 1791批准后现金支付凭证 |
| 1829债务协议折让87.07%等于1790或1807的减值 | 会计期间/权利范围/主体均不一致 | 不得倒推，需历史存量与债息逐年勾稽 |

**PASS（发表资料层）**：实际打开AECA PDF四页截图核查；四类资产的1-real差额、详细损失/抵补的1-maravedí差额、12m/5%=240m分母和1790投票结果复算。**BLOCKED**：1790股东大会原印本页、银行总账和1794原始AJD会议簿、1807银行原账、英国数据服务许可原表。**NOT_RUN**：国债利息直接挤占海军或银行对商户贷款的定量因果。

**唯一下一动作**：从AHFT获得其1790股东大会原印本 7-FSAAVEDRA_C25_007 的可阅读页影像（尽量限缩相关1789—90资本/政府利息议题页，遵守许可，不搬运大体积版权原件），并利用已精确定位的AHBE Libro145、Libro154与Caja984查询对应原始卷页，最终核实“分红有效资本240m vs账面资本300m”的制度/入账桥，再继续1807原账和实际债息挤出研究。


---

## M2i follow-on source-critical correction (2026-11-14)

The earlier M2h statement that "we still lack primary 1791 AGM original" remains true for **page images**, but a BNE digitized **original 1791 October ninth AGM issue has now been pinpointed: HA/8649(7), digital item hd0069882062, https://hemerotecadigital.bne.es/issue.vm?id=0069882062**. Actual web access returned **HTTP403**, so no original financial/meeting page read. AHFT also has printed original **C25_008** (1791, 362pp, 511.1MiB digital master) and a focused **C25_010** (1790 King/Lerena orders, 72pp, 108.5MiB), likewise cataloged NOT read. AHFT currently labels 1791 octava while BNE and Banco2014 call it novena; historical author 2014 bibliography also calls October1790 octava while AHFT lists April–June1790 octava. Consult original title pages; do not silently resolve or collapse.

**Additional historical money/credit evidence:** AECA 2012 PDF **p19 screenshot** directly checked, reporting royal indemnity award 9m nominal reales **24 Aug1793** after 7 Aug1793 auditors' submission, original Banco book AHBE AJD **libro153 fols139v–145v**. Royal order award ≠ verified actual paid cash, and could overlap earlier recognized interest categories.

**New 20,000-reales definitional conflict:** AECA2012 PDF screenshot p17 **5,284,027 whole reales+26 maravedis** for total 30,628 shares' buyback overprice at 1790 balance. Banco2014 EHE67 p128 source text describes 30k shares **5,175,849 suffix14** +628 shares **128,178 suffix12**, sum **5,304,027 suffix26**; 20,000 whole reales difference. Different vintage and litigation/balance account scope unproved comparable, do not call either an audited typo. See [M2i report](M2I_1790_1793_ROYAL_ORDERS_AGM_AND_PREMIUM_CONFLICT_20261114.md) and [data](bank_buyback_premium_crosssource_m2i.csv). M2h historical conclusion about 1790 prewar financial fragility remains, original books NOT_ACQUIRED.
