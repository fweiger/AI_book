# CASE-ESP-001 · M2l — 1887年国务委员会原案卷保管机构与1795合同附件访问协议

- 日期：2026-11-14
- 权威研究任务：[AI_book #32](https://github.com/fweiger/AI_book/issues/32)
- 原有开放 Draft PR：[AI_book #36](https://github.com/fweiger/AI_book/pull/36)
- 前轮：[M2k终局行政司法裁决和港口债务统计](M2K_1887_FINAL_JUDGMENT_PORT_CREDIT_TAX_AND_BANK_RECONCILIATION_20261114.md)
- **证据升级性质**：**CURRENT_OFFICIAL_ARCHIVE_CUSTODY_SCOPE_AND_CONTACT_VERIFIED**；**CONSEJO_1887_SPECIFIC_CASEFILE_SIGNATURA_NOT_ACQUIRED**；**1795_DEED_1862_CERTIFICATE_NOT_READ**；**M2K_NOMINAL_MONEY_CONFLICT_UNCHANGED**；**CAUSAL_TEST_NOT_RUN**。

## 1. 本轮新确认的关键事实：1887年诉讼的候选保管主体就是Consejo de Estado自身的历史档案

西班牙最高咨询机关 Consejo de Estado 官方“Archivo y Biblioteca”明确写明：

> 「El Archivo ... custodia todos los documentos generados por el Consejo de Estado a partir de 1850」；其历史基金约**130,000宗案卷**，覆盖**1833—1939**。

官方页面：https://www.consejo-estado.es/actividad/archivo-y-biblioteca/

因此 **1887年10月24日行政诉讼裁决**在这个时间范围内，优先联系 **Consejo de Estado Archivo Histórico（历史档案）**，而不是从主题词相近就假设 Archivo Histórico Nacional 已保存该卷。历史上数批旧档转存 AHN，**不等于1887的具体案卷也在那里**。

这是**机构层面收藏范围（fonds-level）核实**，不是个案**卷件号（item-level）**核实。法院1887官方公报第557—559页仍是目前唯一已亲自阅览的该案一手全文。**截至本轮没有真正找到1887这宗诉讼的现代馆藏号，也没有取得1795契约誊本。**

司法一手原件：
https://www.boe.es/gazeta/dias/1887/11/26/pdfs/GMD-1887-330.pdf

本项目此前 M2k 已成功通过 web PDF screenshot 显示第557/558/559页：Banco de España起诉Hacienda，争议1884-03-18 Royal Order，1887-10-24判决维持1884拒付，银行因1829和解而不得再次向国库请求支付。同案记载**Banco于1862-12-27提交过1795-10-22贷款契约的公证誊本、1862-11-13瓦伦西亚财政部门的账务证明、1839地方港务清算明细**。这些附件曾在诉讼证据链中被提及，不意味着1887司法档案卷宗今天一定仍附完整实物。

## 2. 研究者能否合法访问旧案卷？官方服务信息直接确认

Consejo de Estado的《Memoria de 2023》（2024年6月批准）**印刷第84页**“3.1.2 Consultas”说明：

- 历史档案向**学术研究人员**提供咨询；
- 许多资料咨询**可远程办理**；
- 对**1987年以前的咨询意见相关案卷**，因为未数字化，馆员可能使用**人工目录及馆内检索**，如必要并有研究理由可获准查阅原卷。
- 本轮 web 实际获取官方PDF文字，第84页文本检索命中；网页 PDF **截图尝试返回HTTP403**，所以状态定为 **OFFICIAL_PUBLISHED_PDF_TEXT_CHECKED / PAGE_IMAGE_NOT_VERIFIED_THIS_SESSION**。**不得声称已拿到1887案卷影像或1987年前所有档案一律无数字化。**

机构正式年报：https://www.consejo-estado.es/wp-content/uploads/2024/07/Memoria-2023.pdf

Consejo de Estado官网“Transparencia”正式公告（网页通过官方搜索结果读取；直接 web open 遇403）列：

- **档案及图书馆邮箱**：**archivo.biblioteca@consejo-estado.es**
- **电话**：+34 915 166 356 / 357
- 主机构：Calle Mayor 79, 28013 Madrid, España。
- 官方联系方式：https://www.consejo-estado.es/transparencia/

这些是真实**公开保管机构工作渠道**，但**无人已经以研究者身份发送咨询**；用户个人身份、联系方式、法律证明与复制权限均未征集。

## 3. 第二条实际可用保管路径：瓦伦西亚 Gobierno Civil 历史基金

[Archivo General y Fotográfico de la Diputación de Valencia / Gobierno Civil](https://archivo.dival.es/es/fondo-documental/fondo-gobierno-civil)本轮实际打开 **官方HTML并读到对应行**：

- 档案基金：**ES.462508.ADPV / Gobierno Civil**，总时段**1739—1958**，25线性米；
- **GC:c.1 Expedientes generales**，时段**1739—1924**，目录明确提到“*acciones del Banco de San Carlos*”等信息；
- **正式档案邮箱**：**archivo.general@dival.es**，电话 **+34 96 388 25 87**，馆址 Calle Beato Nicolás Factor 1, 46007 Valencia；
- 1836年港务委员会撤销后，旧账房资料应移交 Gobierno Civil 的记载出自当时1887财政司法公报；不是本轮已经见到**1836交接清单**或**1795借据保管箱号**。

因此这是**历史移交事实 + 现存相关机构档案群 + 正式咨询窗口**三项相互独立的定位线索，但**无法把3项乘起来当作“1795原件必然完整在GC:c.1”**。

## 4. 检索请求按会计证明力排列，不再模糊索要所有历史资料

见 [port_1795_casefile_acquisition_matrix_m2l.csv](port_1795_casefile_acquisition_matrix_m2l.csv)，7个任务目标分别指出**保管者、索取年月、精确案名、需要的关键页、最终可验证的会计命题**：

| 优先 | 历史原始文件 | 若获原件可验证什么 | 未核实事项 |
|---|---|---|---|
| 1 | Consejo de Estado 1887-10-24诉讼案卷 *Banco de España contra Administración/Hacienda, contra RO 18-03-1884* | 卷件编号/证据附件目录及由哪个法庭保管 | 案件是否完整保存、馆藏号 |
| 1 | **1795-10-22贷款契约追认的testimonio**，1862-12-27银行请愿随案提交 | 原总额**12,968,575 vs12,968,875**、借款人姓名、国家担保和税源抵押、政府票据估值 | 原始书页是否在卷内 |
| 1 | **1862-11-13 Contaduría Hacienda Valencia还款证明** | 核对**13,703,208雷亚尔**累计还款的年份、流量、币种、实际现金及票据换算 | 逐年表不曾被本项目阅览 |
| 2 | 1836港务Junta账册移交后的 Gobierno Civil 旧卷件 | 1795契约另本、1839未结本金/利息及征税款的实收情况 | GC:c.1含银行股票不等于含此借据 |
| 2 | 1839-10-24账房结算表 | 核对3,680,113+33mrs本金、822,892+11mrs利息是否同一债务人及付款期限 | 后世判决只引用二手旧账 |
| 3 | 1794-04-10港口税源规章原印本，BIVALDI **XVIII/4279(28)** | 核对哪项地方港务丝绸/领事税可以被银行视为抵押税源 | 10页原版正文尚未打开 |
| 4 | 若原保管机构找不到案件，请求AHN或原财政档案转移去向 | 验证历史案卷与原始契约是否移交其他机构 | AHN并非默认1887案件保管方 |

**重要区分**：1996年关于Consejo de Estado档案史的独立研究和 Archivo Histórico Nacional 官方“Estado”档案索引，主要说明早期国家咨议文书转存历史。它们**不能否定现存Consejo官网对1850年以后文件的保管声明**，也不能替代本案准确卷件号。

## 5. 1794年港口税费原始印本出现独立书目转引，但未解开正文

BIVALDI [Biblioteca Valenciana原始书目记录8776](https://bivaldi.gva.es/es/consulta/registro.cmd?id=8776)确认：Real Junta Particular de Comercio y Agricultura de Valencia **1794年4月10日**写成、约10页的税费征收规章，书号**XVIII/4279(28)**，数字影像/完整作品入口及 Public Domain Mark 存在。

本轮又核实 **Biblioteca Virtual Miguel de Cervantes/Joan Lluís Vives**对该原始印本的**数字书目复现**，并明确链接回同一BIVALDI图像，而不是提供一份可以独立读取的替代正文：
https://www.lluisvives.com/obra/instruccion-acordada-por-la-junta-particular-de-comercio-y-agricultura-de--valencia--celebrada-el--1793-con-asistencia-del-senor-conde-zanoni-su-presidente--para--la-percepcion-de-los-arbitrios-y-conclusion-de-la-obra-del-puerto--texto-impreso/

因此不能把Cervantes网站“镜像索引”误当作**第二份独立原始合同**，也不能依据书目名称推测1794各项税率数值或他们在1795年实际被银行全部抵押。

## 6. 金融研究的验收阻断仍然存在

本轮**没有增加任何新历史年度现金流、国债利息或者港口税征收额**，故不应机械生成新相关系数、回归系数或银行利润结果：

- 1884印刷的**300雷亚尔合同总额与分项加总差额**依然保留未解释；1887印刷文本疑似漏首位数，也不能反推原1795公证书正确金额。
- 1797—1836期间银行**13,703,208名义雷亚尔的收入**依然来自1887公报对1862财政证明的追述，尚无实际按年收款表；不等于银行净利润。
- 1887终局法院**不准再次向国家追偿**与1817/1818王室“有条件承担代收税款拖欠”这两种法律概念仍需各自原始债务科目判断。
- M2a—M2j的1807银行王室原始总账、财政应计/实付利息、UKDS 3104 g104spd3均未取得；债息对民间信用和帝国海外陆海军费用的**因果检验 NOT_RUN**。

**实际新增**：既有1887一手判决已确认的原始附件路径，现被升级为**明确的当前候选保管机构、正式联系方式、1987年前档案如何进行人工检索的馆方协议、7项最小所需原始文件清单**。不是“又查了一次1887判决”。

**单一下一动作**：由研究者通过已验证邮箱 **archivo.biblioteca@consejo-estado.es** 向Consejo de Estado申请**1887-10-24诉讼案卷的准确signatura及其中1862-12-27银行申请附件目录**，先核实1795-10-22 original notarial loan testimonio、1862-11-13 accountant certificate是否保存在案，再依馆方许可逐页取得核心文书；如官方档案确认案卷不在馆内，才改查 **archivo.general@dival.es** 的历史港务Junta转存档案。此轮**未实际寄送、未征集用户身份**。

保持 Issue #32 OPEN、PR #36 DRAFT；不得仅凭官方档案藏量宣布已经取得原案或完成殖民帝国资金—战争因果研究。
