# CASE-ESP-001 | M2o：Franch(2016) 第217与236页的来源交叉审计、45%占比恢复

2026-11-14。规范Issue https://github.com/fweiger/AI_book/issues/32 ；同一Draft PR https://github.com/fweiger/AI_book/pull/36 。

**证据状态：ORIGINAL_PUBLISHER_INDEXED_TEXT_P217_AND_P236_VERIFIED / ORIGINAL_PDF_IMAGE_NOT_READ / MUNICIPAL_FONDS_OFFICIAL_HTML_VERIFIED / EXACT_1797_BOX_CONTENTS_NOT_ACQUIRED / WAGES_ARREARS_AND_CAUSAL_TEST_NOT_RUN。**

## 1. 发现上一轮过度隔离、立即更正

Ricardo Franch Benavent, *Salario y condiciones de trabajo en la industria de la seda valenciana del siglo XVIII*, *Obradoiro de Historia Moderna*, 25 (2016), 207–242, DOI https://doi.org/10.15304/ohm.25.3202：

- **印刷217页正文**明确写，1797年瓦伦西亚港口工程雇用的**202名peones占全部人员约45%**。同时列出18名普通工日薪5reales、163名4.5、21名4，引用Franch（2007）pp192–194。
- **印刷235—236页衔接文字和236页脚注**补充**78名amasadores日薪5reales**，并提到23名技术泥瓦工工资7–8.5、均薪约7.7及另外两名高级工种；脚注给出档案定位 **A.M.V., Documentación Lonja, caja 56, exp. nº 19**。
- 两页均来自**同一篇论文，不能算两位独立原始档案研究者**。但上一轮只在236页没看到45%，就把整篇学者的45%比例标成UNVERIFIED_QUARANTINED，**方法上错误**。M2o正式恢复“2016论文p217报道约45%”的来源等级。
- p217并不是全面错误页码：它确实是原有202人和工资分组、45%比重的来源。p236则是新增78人及档案号的原文所在位置。旧 M2m 和 M2n 需要分别指向对应命题页码。

**原论文官方URL**：https://revistas.usc.gal/index.php/ohm/article/download/3202/3966 。web搜索引擎对出版者PDF返回了实际页217、236及引文全文，可核实文字；尝试web直接打开仍HTTP503、无法截图，**不是直接人工查看原页图像**。

## 2. 金额与分母界限

| 源文/模型 | 人数 | 条件性名义日薪总额 | 证据级别 |
|---|---:|---:|---|
| 2016 p217，三档peones | 202 | 907.5 reales | 人数与单价为出版原文，乘积为假定全体同日工作的模型 |
| 2016 p236，另78名amasadores | 78 | 390 reales | 同一来源，不是实际工资支付记录 |
| 四组 peones+amasadores | **280** | **1297.5 reales** | 已核算模型，非欠薪余额 |
| 另23名albañiles | 23 | 约23×7.7=177.1 reales | 平均日薪7.7是作者取近似值，乘积不精确 |
| 另1名maestro+1名capataz | 2 | 不在精确总额中 | 可检索正文未建立精确日薪 |
| 显式列出的工种人员（若各组无重叠） | **至少305** | 不计算精确全体工资 | 不能当作全港全部工人数 |

**恢复45%不等于“449人为实测总人数”**：202/0.45=约448.89。若且唯若历史作者将真实比例四舍五入到**最近整数百分点**，则202/N在[44.5%,45.5%)，整数N可为**444到453**。这是带清楚假设的敏感性区间，**不是直接从原档读出的员工总数**。若45%只是口头近似，区间也不能当作真实置信区间。见 [port_1797_workforce_denominator_sensitivity_m2o.csv](port_1797_workforce_denominator_sensitivity_m2o.csv)。

## 3. 原始档案仍未读取

瓦伦西亚市政府官方网站 [Archivo Histórico Municipal](https://www.valencia.es/es/-/archivo-hist%C3%93rico-municipal) 明确列有 Documentación Lonja 官方查找目录（官方HTML的第33行）。本轮尝试从官方链接点击、大型PDF直接打开均超时；本地Python请求因DNS错误失败。**仍没有读到Caja56 Exp19在现存官方目录中的具体条目，也未读到1797原始工资簿**。学术文章p236的档号需要由现馆确认现存与可复制状态。馆方既有官方咨询邮箱archivo@valencia.es（未发送邮件）。

尽管元数据等级提高，1797实际出勤、工资应付/支付/拖欠、2月11日工人骚动对应手稿、银行vales贷出与工地现金流账仍NOT_ACQUIRED。**债息挤占军事财政、战争导致地方工资拖欠的因果实验均NOT_RUN**。

## 4. 方法学纠偏与接续

M2m、M2n的错误，不是历史学者数据有假，而是研究方未按**不同论断分别定位同一文献页码**。这轮正式将三个命题各自登记为：

1. 202名peones和45%：PUBLISHED_AUTHOR_ASSERTION, PRINT_P217, NOT_PRIMARY_ROSTER_VERIFIED。
2. 78名amasadores及档号：PUBLISHED_SCHOLAR_FOOTNOTE, PRINT_P236, NOT_ORIGINAL_BOX_READ。
3. 907.5、1297.5和隐含约449：DERIVED_MODELS，前二为条件性日工资、最后一个为四舍五入比例的反推近似人数。

这三种状态不得互相替代，尤其不能通过假设所有280人都同时劳动去反推1797工人工资债务。

**下一唯一动作**：向市立档案馆确认 A.M.V. Documentación Lonja, Caja56, Exp19 的现行馆藏题名、年代、页码、复制权限，取得允许的最小范围原始雇工名单/工资付款页；再另找1797-02-11骚动原始文书以连接银行与港务Junta的实际现金流。Issue #32 OPEN、PR #36 DRAFT、不合并。


---

## M2p 2026-11-14 archival ACCESS STATUS UPGRADE — replaces former catalogue download blocker

The actual city-published 375-page DOCUMENTACIÓN LONJA finding-aid PDF was supplied by the researcher in this conversation and directly opened and page-rendered. PDF p321, catalogue entry742, **confirms A.M.V. Doc Lonja Caja56 nº19 is the January1797 Valencia Grao port employees roster, 30 manuscript folios, olim28–1**. This is now **FIRST_PARTY_OFFICIAL_FINDING_AID_PAGE_IMAGE_VERIFIED**, stronger than the M2n/M2o "only scholar-cited exact box and catalogue download timed out" statement; those earlier statuses are historic stage-specific blockers, not current status. The 30-folio original worker roster itself remains **NOT_ACQUIRED**, and actual wages unpaid cannot be inferred from inventory.

The same city catalogue p319–321 has #735, #738, #740, #741 earned-versus-paid payroll record titles for Dec1795–Oct1796, #736/#737 uncertain-era wage accrual notebooks 11+25, and separate bank loan vales receipt/treasury records pp27–31. Hence these are **legally requestable primary-source targets**, not original internal accounts or wage debts actually read. See [M2p direct city original catalogue audit](M2P_USER_UPLOADED_LONJA_375P_PRIMARY_CATALOG_AUDIT_20261114.md), its [21-item source lookup matrix](lonja_1792_1798_primary_archive_targets_m2p.csv), and [binary source manifest incl. exact SHA256](source_manifest_valencia_lonja_m2p.csv). The entire original PDF binary has NOT been pushed to the public repo (redistribution permission not verified).
