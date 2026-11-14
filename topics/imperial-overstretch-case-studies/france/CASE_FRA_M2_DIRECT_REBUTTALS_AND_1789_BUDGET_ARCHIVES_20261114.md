# CASE-FRA-001｜M2：1790年财政官员同期答辩与1789预算原始档案路线（2026-11-14）

**权威Issue：** https://github.com/fweiger/AI_book/issues/35  
**既有Draft PR：** https://github.com/fweiger/AI_book/pull/39  
**阶段**：M2原始材料**发现、馆藏核对与方法设计**，并非已经读取纸本总账、预算数值或验证政治指控。本轮**没有为任何新发现的档案捏造财政数值**。  
**关联记录**：[finance_originals_queue_m2.csv](finance_originals_queue_m2.csv)

## 一、新证据链：1789—1790年财政争议有官员的同期连续答辩

法兰西国家图书馆[官方复合书目条目](https://catalogue.bnf.fr/ark:/12148/cb45564768s)记录了多份关于Marbois殖民财政管理的**当事人一手印本文书**：

1. **第一次质询的答复**，题为 *Réponse à la motion faite à l'Assemblée provinciale de la partie du Nord, sur les finances; et détails sur cette partie de l'administration de M. de Marbois*，BnF复合书目**子条目[1]**约1790年、25页。另在[BnF Gallica馆藏选择目录](https://gallica.bnf.fr/selections/fr/html/bibliotheque-de-moreau-de-saint-mery)记录该标题的一份印本后有 **《État sommaire des dépenses à faire à Saint-Domingue pendant l'année 1789》**（25页正文+1页预计开支摘要）。**不能在不同藏本之间未经核对就确定两者所含附件相同。**
2. **第二次质询的答复**，**Étienne Pierre Charles Wante**签署于 **1790-01-09**，25页+附页；BnF子条目**[13]**。Wante是财政局官员、伤残军人基金司库，和Marbois同属殖民财政管理体系；并非中立审计裁判。
3. **第三次质询的答复**，Wante著，BnF子条目**[31]**，45页，印于Port-au-Prince，**1790-03-13**（馆藏编目）；Gallica目录将原本某日期记作**1790-02-13但有手写修订为三月**，所以应记录`1790-02-13_printed_or_catalog`和`1790-03-13_hand_corrected`两个日期，等待核查书内末尾印刷页。第三次答辩的Gallica定位：https://gallica.bnf.fr/ark:/12148/bpt6k9788760w/f498.item。书目还记录该册附有Wante与Torris **1783年商业债务延期申请**及王室相关裁定。这构成**利益关联的审查线索**，不构成答辩内容不真实的证明。

**严禁提前升级的断言：** 目前核实的是这些文书的**出版存在、作者身份、日期、篇幅、Gallica馆藏定位**；尚未可靠取得其**45页全部正文和会计表**。不能声称Wante在具体第几页已经证实或否认1789省议会关于“超过二百万殖民地资金转往法国”的控诉；也不得把已定位预算页误记为已取得1789实际支出数据。

## 二、更强的官方档案线索：SHD的1789年财政预算原表

[法国国防历史档案馆 Service historique de la Défense（SHD）官方《Catalogue des manuscrits》](https://www.servicehistorique.sga.defense.gouv.fr/sites/default/files/2019-04/201601_NP_DBIB_Manuscrits-MS.pdf)，**MS 142（海军历史手稿/图册）第99件、印刷p.100**，明确登记：

> *Saint-Domingue. Récapitulation générale des dépenses à faire à Saint-Domingue pendant l'année 1789.*

这是一项**1789年未来支出预计表（dépenses à faire）**，不能当成1789实际支付。它可以与上述Wante第一答复所附的**1789年预计开支概要**作同账期、同会计项目比较，但**目前不知道是否来自同一财政表格底稿**，在获得文件图像/日期/签章/科目以前，不能称两套数据为独立交叉来源。

该官方目录（2015年版）前言说明馆藏现存于**Vincennes SHD图书馆**，MS系列档号应按馆藏索引申请；本轮通过PDF可搜索正文检查MS142 No.99，但网页截图工具返回cache miss，未确认原件图像，状态`OFFICIAL_CATALOG_TEXT_VERIFIED / ORIGINAL_BUDGET_SHEET_NOT_READ`。

## 三、两项直接延伸殖民财政传导链的SHD原档案

**SHD MS 338**（目录印刷**p.176**）：Louis-Honoré-Alexandre Puget de Bras，1784—1787年圣多明各背风群岛法国海军驻地资料，包含42封1784—1787年海军大臣Castries致信及**1785年外国船舶驶入圣多明多各港的进出口货物和所征税额报表**，还包括1785—1786年王室船只必需品价格。**这是港口级、外国船舶流量与税务记录候选**，不是1788年法国海关全国商品统计，也不能提前认为它覆盖全部殖民地贸易。

**SHD MS 353**（目录印刷**p.182**）：波尔多商人/船东**Magnac兄弟**1787-06-20—1791-10-08的约**1,200封信件抄录**，涉及欧洲、安的列斯群岛与圣马克亲属、糖咖棉贸易及奴隶贸易和革命。馆藏562页，其中**第1—8与539—542页缺失**，末附收件人索引。这是**私人商业信用、货款、汇票与宗主国贸易冲击**值得筛查的材料，但目录仅说明书信范围，并未证明其中一定存在与1788地方海军金库105.31万汇票相对应的单据。**1,200是约数，不是1,200条已完成金融数据。**

**为什么这两类材料有价值：** MS338提供了1784年后外国直接贸易和实际征税的潜在地方视角；MS353可以追踪私人P账户中真实的跨洋支付、付款延迟与政治经济冲击。它们分别能扩展以前的TOFLIT18国家进口统计与圣多明各地方财政F账户，但**不会自动把私营信用流变成法国王室国库现金流**。

## 四、证据层级/可比规则

| 类别 | 这轮已确立 | 未确立 |
|---|---|---|
| 1790 Wante答辩 | BnF馆藏、财政官员身份、第二和第三次答辩日期、45页/25页结构 | 具体指控的证实/驳斥及原始付款金额 |
| 1789预计开支 | Wante相关印本附件及SHD MS142 No.99有馆藏记录 | 两原表是否同一底稿、预算科目、预算金额 |
| 1785外国船舶贸易税 | SHD MS338原始文件组存在，含外国船贸易货值和征税记录 | 实际数字、港口覆盖、税率与1788跨年增长 |
| 1787—1791私人书信 | SHD MS353存在且有缺页说明 | 真实汇票金额、到期、谁实际付款、王室净收 |
| 1788实际账 | 已有Marbois1790数字化文本和地方octroi未缴库项 | NIII/NXI折叠页高清视觉核验、法国王室实际到账 |

**账期一致原则：** 1788年`actual_outlays`和1789年`planned_outlays`不能做简单同比增长。必须把每条记录保留`record_year`、`budget_or_actual`、`account_scope`、`currency`和`source_image_verified`，另核支出主体及上一年度结算。

## 五、下一项唯一动作

优先向SHD Vincennes申请**MS142第99件1789年预计开支原表高清扫描**，同时从BnF Gallica对应的首次Wante财政答辩附页提取相同年度的`État sommaire des dépenses`。核实是否同一底稿后，才能建立**1789预算预计支出字段字典**；不把预算当实际支付。

后续依次提取MS338的1785外国船舶港口税额、MS353中可识别信用票据、Wante第二/第三次答辩关于具体财政指控的原文，再与原有Marbois地方金库、法国王室G¹46*/44*档案对接。历史主结论仍属于`M2_PARTIAL / CAUSAL_NOT_RUN`。
