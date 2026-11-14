# CASE-ESP-001 | M2i — 1790王室决议、1791股东大会数字原件、1793补偿与股份回购金额冲突

日期：2026-11-14。唯一研究Issue https://github.com/fweiger/AI_book/issues/32；原有Draft PR https://github.com/fweiger/AI_book/pull/36。

证据状态：ARCHIVE_CATALOG_METADATA_VERIFIED / 1791_BNE_DIGITAL_ITEM_ID_FOUND_BUT_SOURCE_IMAGE_403 / AECA_2012_P19_PDF_IMAGE_VERIFIED / BANCO_2014_SOURCE_TEXT_CHECKED_PDF_IMAGE_TIMEOUT / ORIGINAL_1790_1791_AGM_NOT_READ / CAUSAL_TEST_NOT_RUN。

## 1. 新定位的三个同时代原始印本，不要只查1790年厚书

**格拉纳达 Archivo Histórico Facultad de Teología (AHFT)** 官方 AtoM 页面真正提供了以下书目和数字文件元数据，均不是本项目已阅原书影像：

| 源 | 历史时期 | 确认的原始文献馆藏号 | 电子母本（网页标记） | 研究作用 |
|---|---|---|---|---|
| AHFT1790大会 | 1790年4—6月会议，目录出版1792年 | ES 18087 AHFT 7-FSAAVEDRA_C25_007 | AFT_FSAAVEDRA_C025_007.pdf；**216页、322.8MiB** | 1789年度5%股息被否决、王室利息请求、购回股份讨论 |
| AHFT1790王室决议 | 1790年4月28日银行请求、5月28日在股东大会公布 | ES 18087 AHFT 7-FSAAVEDRA_C25_010 | AFT_FSAAVEDRA_C025_010.pdf；**72页、108.5MiB** | 财政大臣Lerena报告及王室对供应合同损失、利息和股份回购的正式处理 |
| AHFT1791大会 | 1791年10月17—25日会议，1792年印本 | ES 18087 AHFT 7-FSAAVEDRA_C25_008 | AFT_FSAAVEDRA_C025_008.pdf；**362页、511.1MiB** | 核对1790利润年度1200万/5%股息批准，及银行有效资本分母 |

AHFT源页：
- 1790会议 https://archivo.jesuitas.es/index.php/acta-de-la-octava-junta-general-de-accionistas-del-banco-nacional-de-san-carlos-celebrada-en-la-casa-del-mismo-banco-en-los-d-as-21-22-23-y-28-de-abril-28-y-31-de-mayo-7-9-10-14-y-30-de-junio-de-1790
- 王室决议 https://archivo.jesuitas.es/index.php/reales-ordenes-y-resoluciones-de-s-m-sobre-la-representaci-n-de-28-de-abril-de-1790-hecha-por-la-junta-general-de-accionistas-del-banco-nacional-de-san-carlos-comunicadas-a-la-misma-junta-y-publicadas-en-la-celebrada-el-d-a-28-de-mayo-
- 1791会议 https://archivo.jesuitas.es/index.php/acta-de-la-octava-junta-general-de-accionistas-del-banco-nacional-de-san-carlos-celebrada-en-la-casa-del-mismo-banco-en-los-d-as-17-18-19-20-21-22-24-y-25-de-octubre-de-1791

此外，**Biblioteca Nacional de España（BNE）的Iberoamericana Digital/BDPI元数据明确登记**：1791年**第九届**股东大会，1792年印本，BNE索书号 **HA/8649(7)**，数字条目 **hd0069882062**，可进入
https://hemerotecadigital.bne.es/issue.vm?id=0069882062 。
本轮实际点击数字对象**返回403**；所以BNE **DIGITIZED_ITEM_CONFIRMED** 与 **ORIGINAL_PAGE_NOT_READ** 必须分开。BNE目录称1783—1790和1792—1827同一报刊其他年份尚未数字化，这是BNE自身馆藏的状态，不能推断其他博物馆、AHFT或央行均未数字化。

### 严重书目序号差异

AHFT在同一档案库把1790年4—6月会议**和**1791年10月17—25日会议标题均写作“octava”（第八届），而BNE目录及Banco de España（2014）参考文献把**1791年10月会明确列作“Novena”（第九届）**。2014的参考文献又列出一个日期为**1790年10月17—25日**的“Octava”出版记录，与AHFT写的**1790年4—6月**八届日期不一致。

**不可将两个同名“八届”自动合并为一场会，或直接宣称哪个目录是假的。** 可能反映封面、会议续会、年度财报年份与实际召开年份、书目抄录等差异；必须查阅**原书扉页、印刷日期及会议第1页**。研究登记采用 event_date、accounting_fiscal_year、meeting_ordinal_by_source、print_year 四套字段，而非一个“年份”。

详见 [original_bank_AGM_1790_1793_locator_m2i.csv](original_bank_AGM_1790_1793_locator_m2i.csv)。

## 2. 1791年4月11日王室指示：有效资本240百万的时间锚点

Rafael Moreno Fernández（Banco de España，**2014，Estudios de Historia Económica no.67，第64页**）依据原始资料转述**1791-04-11的Real Orden**：在买回**30,000股**以后，银行可重新安排投资的本金是**240,000,000名义雷亚尔**。这与此前1790/1791股息所称 **12,000,000/5%=240,000,000** 完全同数。

官方出版（PDF正文可检索，web PDF screenshot因超时没有显示该页）：
https://www.bde.es/f/webbde/SES/Secciones/Publicaciones/PublicacionesSeriadas/EstudiosHistoriaEconomica/Fic/roja67.pdf
文本镜像（同一出版，**不是独立学者验证**）：
https://cdi.mecon.gob.ar/bases/doc/bde/ehe67.pdf

这比单纯的现代2017年“减资发生于1790年”叙述更接近银行当时投资法律依据，但仍是**历史作者转述原指示、不是项目直接核读原1791指令**。其存在支持投资/分红有效资金可按240m规划；但不能反推**正式注册资本在1791年已会计冲销**：Fundación BBVA（2005）表9.8的账面Capital在1794年仍300m、1795年才240m。

**测试性机制：** 授权股票回购、回购后的可投资资金与年末会计股本确认可能发生于不同阶段。这是更有证据力的解释候选，不是已结案的制度事实。

## 3. 1793年国王决定补偿900万：应收与实付的识别关口

**AECA Moreno Fernández（2012），第19页已通过 web PDF screenshot 直接看到出版页面**，作者报告：
- **1790-05-19**：关于银行国家供应合同损失的王室赔偿承诺/调查，后有 **1790-06-03** 皇家命令补充；
- 两名专员在**1793-08-07**递交经三年核查后的结论；他们甚至认为银行管理不当扩大了原本的亏损；
- 国王决定**补偿900万名义雷亚尔**，于**1793-08-24的Real Orden**对银行通知。论文脚注21给出真正可请求的银行董事会原始档案：**ABE, Secretaría, AJD (30.8.1793), Libro 153, folios 139v–145v**。

这是1790财政资产问题继**银行债权请求—王室利息仲裁—官方财政补偿决定**后的另一个可审计节点。原材料目前证明**批准或命令支付**，不证明银币已全部划拨到银行、实际现金到帐日或每年财务收入确认时间。与1790年已承认的部分政府利息不得未经分类而简单加总为独立补贴。更不能把1793的900万除以1829的和解债权来推导回收率。

见 [bank_1790_1793_royal_compensation_m2i.csv](bank_1790_1793_royal_compensation_m2i.csv)。

## 4. 2012和2014同一学者关于自身股票回购亏损出现20000雷亚尔差异

AECA（2012）第17页出版物截图直接显示：1790年7月6日损失账中**30,628股自家股票的超价损失** 5,284,027 whole reales +26 maravedís。

Banco de España EHE67（2014）第128页出版PDF正文可检索，历史作者讨论1794年的旧管理层索赔意见，列出：
- 30,000股相关损失 **5,175,849 reales，原文尾数14**；
- 额外628股相关超价 **128,178 reales，原文尾数12**；
- 相加 **5,304,027 whole reales，尾数26**（在尾数为可直接相加的同一单位前提下）；
- 比2012年7月分类 **5,284,027 whole reales，尾数26** 多 **20,000 whole reales**。

**这不是已经证实某一本书印错了20000。** 1790和1794是不同日期，2014的5.176m属于特定诉讼/待冲销损失的分类，2012的5.284m属于当年账户分类；部分超价或摊销可能是不同口径。此外2014还给出**买回30628股总支付67,531,599 reales尾数24**及与某一名义金额比较的折价账项，这个总支付数与30628×2000的机械差额不等于作者另一行给出的7,531,599同尾数；须分别核对对应的30,000还是30,628股的参照本金。不可因数值接近就把两笔钱等同为原始全年实际损失。

**优先原始材料**：2012脚注 *BNSC Memoria 1790 p255*；2014源脚注 *AHBE Secretaría AJD Libro154 fols271–272*，及 *BNSC Memoria 1790 p110*。只有同时核读原始账期/科目才能解决差异。详见 [bank_buyback_premium_crosssource_m2i.csv](bank_buyback_premium_crosssource_m2i.csv)。

## 5. 科研方法：把“原始印本是否可获取”与“原始内容是否已复核”拆开

| 原始材料 | 存在/定位 | 实际查看内容 | 状态 |
|---|---|---|---|
| AHFT 1790股东大会（216页，322.8MiB） | 确认 | 未看原印本 | CATALOG_LOCATED_NOT_READ |
| AHFT 1790王室/财政大臣决议（72页，108.5MiB） | 确认 | 未看原印本 | CATALOG_LOCATED_NOT_READ |
| AHFT 1791股东大会（362页，511.1MiB） | 确认 | 未看原印本 | CATALOG_LOCATED_NOT_READ |
| BNE 1791第九届大会，HA/8649(7)，hd0069882062 | **数字对象编号已确认** | 数字影像403 | DIGITIZED_NOT_READ |
| AECA 2012第17–19页 | 已取得 | **实际截图核读** | PUBLISHED_SCHOLARLY_PAGE_IMAGE_PASS |
| Banco de España EHE67 2014 | 已取得全文正文 | 指定页截图超时 | PUBLISHED_SCHOLARLY_TEXT_PASS_IMAGE_NOT_VALIDATED |
| 1793 AHBE AJD Libro153 fols139v–145v | 原始卷页索引已确认 | 未读原原稿 | PRIMARY_BOOK_REFERENCE_ONLY |

**版权及访问**：AHFT载有“Acceso libre. Sujeto a las condiciones del documento”，大PDF仍可能因技术而无法获取；图库元数据并不授权无条件镜像转载。BNE返回403不可绕过。此项目不上传大型原始扫描或复制受限文件，不冒充已经获得原件。

## 6. 结果边界与下一唯一行动

**PASS**：原件馆藏、BNE数字ID、具体1790与1791出版日期和数量、学术发表的1793 900万赔偿决定、第19页实际图像、2014转述的1791年240m资金指令、同一作者前后20000雷亚尔回购亏损定义冲突的程序算术。档案“octava / novena”序号与1990年日期冲突保留。

**BLOCKED**：AHFT原PDF母本3份均未亲阅，BNE 1791数字影像403，1790/1791王室和股东大会的原件内容未核读，1793 900万赔偿实际现金付款仍未取得。1807 Banco Real Hacienda总账、UKDS 3104原始表同样缺失。

**NOT_RUN**：债息对海军/陆军挤出、商业信贷占用的因果实验，1829和解归因至1790或1807同一会计贷款的账龄分析。

**单一下一动作**：优先要求AHFT档案持有人提供 **1790王室决议 C25_010、1791股东大会 C25_008**的少量可读页（股份购回/2.4亿资本、政府利息仲裁、1790利润股息批准，务求封面和原始会议日期），同时利用 BNE 已确认的**数字对象hd0069882062**通过正规访问方法获取1791原扫描；拿到原始文件后核对1791 Royal Order 240m、股本回购的20000差异及1793赔偿9m是否实际收到。既有 Issue Open、PR Draft，不关闭项目。
