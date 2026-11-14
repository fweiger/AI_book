# CASE-ESP-001｜西班牙殖民帝国研究（M0 初始证据 + M1 深化史料）

**权威Issue**：[AI_book #32](https://github.com/fweiger/AI_book/issues/32) · **上位**：[TOPIC-010 #30](https://github.com/fweiger/AI_book/issues/30) · **Draft PR**：[ #36](https://github.com/fweiger/AI_book/pull/36) · **状态**：M0结构通过；M1来源与已发表十年均值新增；M2马德里逐年原始数据尚未取得；M3因果识别未运行。

## 第一轮结论（不是最终因果判决）

**“殖民美洲白银支持帝国财政，而连续战争支出快于收入”得到非常直接的经济史档案研究支持。** Marichal的《Bankruptcy of Empire》指出，1780–1800年波旁王朝提高本土及美洲税收，但1779–83英西战争、1793–95对法战争、1796–1801及1805–08对英战争逐渐推高开支，政府开始以税捐、赠款与债务融资；[1784–1807马德里国库原始手稿研究](https://ideas.repec.org/a/cup/jechis/v41y1981i02p315-339_04.html)认为殖民收入受战争威胁，传统税基缺乏足够弹性。**我们尚未取得这些原始账本，因此不能宣布财政成本收益已经逐年复算。**

## A 科技：并非所有矿业都来自同一个“低技术奴隶开采”机制
- 波托西（今玻利维亚）和萨卡特卡斯（今墨西哥）银矿，以及冶炼、燃料、**汞齐法**与秘鲁Huancavelica的汞供应构成技术与资源链。
- 反例：冶炼技术、汞供应及劳动力可得性共同决定成本；不是简单将强制劳动视为零成本。〔[Oxford Research Encyclopedia](https://academic.oup.com/edited-volume/61800/chapter-abstract/546349390)〕

## B 人口劳动—银矿—全球贸易
- 波托西1572—1576矿业改革后的mita强制轮役动员规模，研究估计每年约**12,000—14,000名成年原住民男性**。这是劳动力调配流量，不是当地奴役人口总存量。〔[IRSH同行评审史料研究](https://www.cambridge.org/core/journals/international-review-of-social-history/article/women-in-the-silver-mines-of-potosi-rethinking-the-history-of-informality-and-precarity-sixteenth-to-eighteenth-centuries/DDD6EAB29255C2C34F189A6A83129200)〕
- 美洲白银与全球贸易的货币需求有关，但不等于“北美银矿由非洲奴隶普遍开采”；墨西哥与安第斯的劳动制度不同。

## C 军事与外交：存在英国压力，但不是英国单方操纵整个欧洲
- 乌得勒支和约改变商业权利；1780—1808战争中西班牙与英国/法国结盟关系发生反复变化。
- **最强反例**：西班牙对英作战的1779—1783年，实际上与法国及北美反英独立力量形成合作；不是所有西班牙战争都由英国单方面挑起。

## D 财政债务：直接验证假说的候选案例
- [Marichal](https://www.cambridge.org/core/books/abs/bankruptcy-of-empire/imperial-wars-and-loans-from-new-spain-17801800/A949A388DF0ED83E906CA22EBE8730A9)总结：加税增长，但战争支出快于税收，进而借款。
- [Barbier与Klein](https://ideas.repec.org/a/cup/jechis/v41y1981i02p315-339_04.html)还发现：殖民地来源税收波动对马德里中央国库尤其危险。**暂不将其学术判断伪装为本项目重算过的财务序列**。

## E 本土产业和殖民退出
- 需要另查西班牙本土制造/贸易品出口、货币供应、实际汇率，以及1808后帝国各地独立过程。财政压力不必是全部退出的唯一原因。

## 假说与反证
- **H1（财政过度延伸）**：军费和债息增长率高于王室可用财税流量；识别变量 `military_spend/treasury_revenue`、`colonial_treasury_remittances`、`debt_service/revenue`；优先原始来源Madrid Treasury 1784–1807。
- **H2（资源与治理危机）**：当地劳动强制、矿产资源质量、货币与跨洋交通冲击，加上1808拿破仑入侵，造成财政和殖民政治同时失稳。
- **证伪**：若军费增速未超税收、偿债成本未恶化但殖民政治仍崩溃，军事财政机制不能单独解释。

## 数据与审查状态
[12条事件](events_m0.csv)、[10项来源](source_registry_m0.csv)、[2个候选指标（其中一项有发表区间）](metrics_m0.csv)。格式与年份可按CSV检查；原始王室财政年度表 `NOT_ACQUIRED`，因果识别 `NOT_RUN`。

**下一项唯一任务：** 逐表取得Marichal和Barbier–Klein对1780—1807的收入、军费、殖民汇款与贷款明细，统一银比索/里亚尔/法定币、国库本土与新西班牙会计口径后再做趋势与支出收入比例。


---

## M1 实质性增量（2026-11-14；仍属Draft，不是最终结论）

- [M1深入研究、反证与史料审查](M1_SOURCE_AUDIT_20261114.md)：帝国资源汲取—财政转移—战争融资—地方精英政治反弹的分层解释；明确没有运行因果复算。
- [新增来源登记](source_registry_m1.csv)：7项机构史料、已发表数据集和最新工作论文，标注实际阅读层级。
- [1720—1799年新西班牙境外财政汇款十年均值](remittance_decadal_m1.csv)：8行已发表表格转录，分汇往卡斯蒂利亚与其他殖民地situados，逐行做加法校验；并非年度原始账本或王室净利润。
- [M2财政数据字段及核验要求](fiscal_data_dictionary_m1.md)：UK Data Service ESFDB 3104 / g104spd3.tab 1784—1807年（24行、16列）代码簿，CHKTOT和MREVTOT不一致、MREGION缺失、INDIES及LOANS含非税收项的限制。
- [2026-11-14研究session](sessions/2026-11-14-spain-m1-fiscal-audit.md)与[变更日志](CHANGELOG.md)。

### M1阶段性定量观察

- 1780—1789年新西班牙每年平均向卡斯蒂利亚汇款 **1,655,605比索**，向其他殖民统治区以situados形式汇款 **6,170,565比索**，合计 **7,826,170比索**。
- 1790—1799年同口径相应为 **4,317,453 / 4,748,523 / 9,065,976 比索/年**；总体汇款提高，但两个目的地的构成改变。来源：Martínez López-Cano（2022），Cuadro 8，引用Marichal与Souto（2012）。[原始发表PDF](https://museosdelbancocentral.org/wp-content/uploads/2022/03/Monedas-Medios-de-Cambio-y-Espacios-de-Circulacion-en-America-Latina-y-Espana-1500-1900.pdf)。
- 2025年Chiovelli等论文使用85所王室国库的历史档案数字化资料；Table 3基线样本为79所国库和1,959个国库-年度观测，报告改革收入效应0.290 log points（约33.6%）。这是**作者的工作论文估计，不是本案例的独立复算或整个帝国税收增长率**。详见M1报告。

**当前唯一下一项工作：** 获取获准使用的ESFDB Spain `g104spd3.tab` 年度记录，核对1784—1807年24行数据的缺失、汇总差异和财政分类，再开始M2可复算年表；未获数据不作债息占比、军费占比及净收益估计。


---

## M2 年度重建数据（2026-11-14，仍属Draft）

由[Prados de la Escosura (2024) 开放获取第6章](https://doi.org/10.1007/978-3-031-60792-9_6)获取**已发表的**1778—1820年连续年度重建数据43年（表6.2财政）+43年（表6.4贸易），且原章采用[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)许可。该突破意味着不再只能依赖M1十年均值；**但原始AGS手稿及ESFDB 3104的底层TAB仍未取得，也未完成因果复算**。

- [M2年度数据审计与竞争性解释](M2_YEARLY_RECONSTRUCTION_20261114.md)
- [财政年度43行](fiscal_annual_prados_1778_1820_m2.csv)：汇往本土的Indies款项、海关收入、总国库收入及1808年不变价格值；分拆王室汇款与私营贸易，年度财政总额不能直接当净税收。
- [贸易年度43行](trade_annual_prados_1778_1820_m2.csv)：西班牙本国产品与转口出口按西班牙美洲/其余世界分类；作者对目的地份额含估计假设，1808年前后不完全可比。
- [M2新增资料与许可](source_registry_m2.csv)、[M2研究session](sessions/2026-11-14-spain-m2-annual-reconstruction.md)。
- 统计读回/结构性验证：两个CSV均43个唯一连续年份1778—1820；表内四舍五入分项加总允许百万reales的±2差异；6个窗口均值与份额已实际计算。GitHub结构CI与史学因果审查必须分开报告。

**代表性结果（百万名义reales/年）：** 1784—1792 Indies年均85.56、对美洲本国产品出口205.11；1797—1801降至47.20和54.40；1802—1804反弹至268.00和279.67；1805—1807再降至31.33和43.67。1815—1820出版表所列Indies款项为0，但对美洲本国产品出口仍年均106。**政治财政关系与商品市场关系并不等同**；不能以同期波动替代战争或独立的因果检验。

**M2唯一待办：** 获取ESFDB 3104 Madrid Treasury g104spd3.tab的获许可24年年度行，与该已发表序列逐年比照；否则标记底层数据未取得，不虚构借款、债息、军费或国家净利润。


---

## M2b：海军财政成本与史料口径交叉审计（2026-11-14）

新增[海军开支及帝国财政收益边界报告](M2B_NAVAL_FISCAL_AUDIT_20261114.md)、[1784—1805年中央国库与本土海军支出分期衍生数据](naval_spending_periods_m2b.csv)、[1760—1789年加的斯殖民相关收入/海军支出五年期比较](cadiz_indies_naval_quinquennia_m2b.csv)、[独立史料来源与授权状态](source_registry_m2b.csv)、[研究session](sessions/2026-11-14-spain-m2b-naval-audit.md)。原文数据来自 Barbier (1984) Table II–IV 的合法重印预览，已进行原表图片与公式核查；不将受版权保护的整张原始年度表复制进仓库。

- **分期结果（海军/西班牙中央国库总支出，名义支出加权）：** 1784—92年25.03%；1793—96年31.51%；1797—1801年14.32%；1802—04年11.13%；1805年7.66%。海军占比下滑不能自动证明债息挤出、军事能力下降或帝国净收益为负；哈瓦那等海外海军支出不在分母口径内。
- 1791年 Marichal 广义“Indias”构造为229.686百万雷亚尔、占普通收入34%；Prados 直接汇款为161百万、占其重建总收入20.13%。**这不是两套独立估计的同一变量，Marichal将烟草和贸易税部分归入美洲来源财政收益。**
- 1760—79与1780—89加的斯表的收入分子定义在1778自由贸易改革前后发生变化，故不能把五年期“覆盖率”拼成可比单一趋势，也不能把超过100%的局部海军覆盖率宣称为整个殖民帝国盈利。
- 数据许可：[UKDS ESFDB #3104](https://doi.org/10.5255/UKDA-SN-3104-1)要求合法注册账户及EULA流程；本轮**未取得** g104spd3.tab 24条逐年数据，没有绕开权限。已发表Marichal论文PDF正文可检索，但原PDF截图返回403，本轮仅标注文字阅读不声称完成图表扫描复核。

**下一唯一工作：** 通过获准访问流程取得 UKDS Spain g104spd3.tab，按CHKTOT/MREVTOT与INDIES/LOANS口径核对1784—1807年马德里国库收入、海军支出与逐年军费及债息；未经复核不作因果判决。


---

## M2c：1808年国家债务、应付利息与圣卡洛斯银行债权核查（2026-11-14）

- [M2c官方一手债务清单与银行双边口径审计](M2C_PRIMARY_DEBT_AND_BANK_RECONCILIATION_20261114.md)；[1808债务与年度应付利息分类CSV](debt_inventory_1808_cortes_m2c.csv)；[1794/1807银行债权与议会债务口径交叉表](bank_treasury_crosscheck_m2c.csv)；[资料与读取分级](source_registry_m2c.csv)；[研究session](sessions/2026-11-14-spain-m2c-debt-bank.md)。
- **新增一手史料**：1811年3月30日议会公布的1808年7月31日债务清单，报告总债务 **7,194,266,839雷亚尔又33马拉维迪**，列示年度利息义务 **219,591,473雷亚尔**。注意：**应付利息不等于实际支付利息**；1784—1807逐年实际利息支付仍未取得。
- **计量修正**：西班牙文化部货币辞典定义1个real de vellón为34 maravedís，原表33马拉维迪绝不是小数0.33雷亚尔。已在债务CSV中分开整数货币单位，并进行合计核验。
- **债权人一侧的新证据**：Banco de España历史研究指出，1794年王室欠私营特许银行Banco de San Carlos约107百万雷亚尔，1807年约217百万雷亚尔，包含**超过43百万拖欠利息**；1811年官方政府债务分类对该银行则列约125.653百万。两种余额的时间、认可范围、应计利息不同，尚未完成双边原账逐项对账。银行史学研究另认为1807年王室债权约占该银行资产70%；仅支持银行资源配置压力，而非已验证的民间信贷因果挤出。
- **阻断**：议会原件可检索文字但网页截图HTTP403；原始AGS及银行会计账与UKDS原始数据仍未取得；债息造成海军经费减少的因果分析NOT_RUN。

**当前唯一下一项工作：** 寻找并合法获取圣卡洛斯银行1807年原始资产负债表、债务利息拖欠清单与马德里国库1784—1807年原始数据，核对银行账面217百万与政府账户约125.653百万差异；再按同一会计主体测算海军/陆军实际支出与债务利息实际付款。


---

## M2d 银行资产集中、1807余额冲突与原始档案定位（2026-11-14）

- [M2d 银行/王室债权及口径冲突审计](M2D_BANK_SOVEREIGN_EXPOSURE_AUDIT_20261114.md)、[6个历史分期的银行资产集中指标](bank_concentration_windows_m2d.csv)、[1807年资产负债表选定分项与衍生风险指标](bank_1807_balance_diagnostics_m2d.csv)、[来源及档案准入登记](source_registry_m2d.csv)、[研究会话](sessions/2026-11-14-spain-m2d-sancarlos-risk.md)。
- **公开发表的完整1807历史重建表**：Banco de España（1994）Table I.1，银行总资产313.4百万名义雷亚尔，王室债权217.3百万（69.34%），账面现金9.3百万、其中金属币仅1百万（约总资产0.32%），拖欠股息40.1百万。不能将金属货币现金少直接解释为银行必然资不抵债。
- **长时段支持**：Fundación BBVA（2005）Table 9.8，1784—1808年银行账面数据有23个观察年份，1792—93缺失且未补插；1784—89年王室债权/总资产约12.11%，1805—08约68.84%，但这是存量比率非新增贷款、非民间信贷实际挤出。1994与2005原表均依赖Tedde 1988，不能算真正独立原账核验。
- **重大口径冲突保留**：Banco de España（2010）p.130将1807年王室债务记为41.6百万后设比塞塔，按4雷亚尔/比塞塔折合166.4百万雷亚尔、53.10%资产；Banco 1994较宽资产项目217.3百万/69.34%；**差50.9百万雷亚尔、16.24个百分点，未对账**。此外1994账面现金9.3百万，而BBVA 2005为9.2百万，保留原始版本。
- **官方档案定位**：Banco de España Archivo Histórico **Section 17，代码 ES.28079.AHBE/01.17**，包括原始总账、日记账、存货清单与资产负债表；此为**分类层级而不是1807账本单件签号**。先通过[历史档案咨询表](https://app.bde.es/gnt_seg/es/contacto?a=mQu9Z4vk9LSJC8SkUvOnjVopPY9f1i2B)问具体签号，再通过[数字化文档申请](https://app.bde.es/gnt_seg/es/contacto?a=ZYflMv2MBhSQkmfsPzzxr9OWoBgKTZ9s)按身份、用途授权取得影像。未填写用户身份，**未实际发送申请**。
- 1994、2005、2010 PDF截图尝试超时：源可检索文本核验，但没有原始图像复核；原银行账/UKDS原表未取得，债息对海军/私人贷款的因果挤出**NOT_RUN**。未将受版权保护的原完整表和PDF复制入公开库。

**下一唯一动作**：取得银行 1807 年资产负债表、Real Hacienda 总账及拖欠利息分账的精确档案单件签号和获许可数字影像，核对217.3、166.4与政府1808年约125.653百万三种余额差异，再继续债息实际付款/军事支出比较。


---

## M2e：1807银行原始财务附页的实际馆藏线索与收入结构复核（2026-11-14）

本轮并非获得原件，而是把取证目标缩小到**某一届股东大会的具体馆藏册**：

- [M2e新证据与会计核对设计](M2E_1807_PRIMARY_PRINTED_BALANCE_AND_CREDIT_INCOME_AUDIT.md)：马德里古籍联合目录确认Ateneo de Madrid藏1808年银行股东大会本，**馆藏号A-Caj.179/5**。古籍目录描述第26届股东大会于1808-04-20召开、1815年印行、80页，末尾附折叠的1807年银行总表。**目录及实物描述不等于我们已取得并读过该折页**。
- [原始银行账册定位表](original_bank_source_locator_m2e.csv)：另从会计史研究获得**1783年（不是1807年！）**的实际银行账册号：年度余额Libro 471，日记账67/353、总账129/238，作为查询相同类型1807年账本的模板。
- [银行业务累计收入结构](bank_income_composition_m2e.csv)：西班牙央行2010年历史研究报告1791—99年“王室预付款及其他投资”占银行收入52.2%、商业票据贴现5.3%；1800—08年相应80.2%、0.3%。**这是银行收入构成不是信贷余额及挤出回归**。
- [M2e新增来源台账](source_registry_m2e.csv)、[待研究者本人发送的西班牙语档案咨询文本](ARCHIVAL_REQUEST_ES_M2E_20261114.md)、[本轮session](sessions/2026-11-14-spain-m2e-primary-source-acquisition.md)。
- **来源核验状态更正**：本轮成功看到1994年Banco de España表I.1出版页的PDF截图，确认资产10项与负债6项各合计313.4百万雷亚尔，王室债权217.3百万，现金9.3百万（含金属币1.0百万），因此**已发表1994年表格图片PASS**；**银行1807年原始总账及1815年股东大会附页仍NOT_ACQUIRED**。相应更正已补入前一份M2d报告。

**下一项唯一工作：** 通过馆方许可获取Ateneo **A-Caj.179/5**中1807年财务折页，核对217.3/166.4/125.653百万雷亚尔和其利息/本金构成；若折页不能拆分，再向西班牙央行历史档案请求1807年Real Hacienda原始Mayor及利息分账的单件签号。未经授权不发送含身份信息申请、不上传受限影像。


---

## M2f 白银贸易利润冲击、1808银行治理连续性与档案获取阻断（2026-11-14）

- [M2f 深度来源审计](M2F_SILVER_BANK_REVENUE_AND_1808_ARCHIVAL_CONTINUITY_20261114.md)、[银行白银出口与业务利润历史观察](bank_silver_export_profit_m2f.csv)、[1808年银行董事会时间线及原始卷/页号码](bank_1808_board_archival_chronology_m2f.csv)、[M2f来源注册](source_registry_m2f.csv)、[研究session](sessions/2026-11-14-spain-m2f-silver-board.md)。
- **新增竞争性机制**：Banco de España Tedde（2000）公开PDF原出版页截图核查显示，Banco San Carlos白银出口1790–94年均约120百万名义雷亚尔、业务利润约3百万，1801–07分别约14百万及0.3百万，**1799和1800年均无白银出口**。相应按来源近似数估算出口量约下降88.33%、白银出口业务利润约下降90%；此为不等长度历史时期的已发表估计，不是原始逐年报表或因果识别，不应把“没有白银出口”当“银行其他业务利润为零”。
- **新的原始档案卷页线索（仅1808董事会，不是1807银行总账）**：Banco de España（2009/2010）作者脚注列ABE Secretaría AJG **libro 204，fols.251及以下（1808-04-09）**；**libro 194，fols.42–45v（09-10）、53–56（09-17）、66–66v（10-05）**。仅定位原档案卷/页，原页未获准阅览；不得将其当成1807债务本金或利息账册。
- **极强说法的反证**：历史研究记录1808-05-02马德里动乱后，银行董事会1808-05-09和14日仍有会议；这反证“银行行政机关立即完全停止活动”，但不足以证明商业贷款或银行资金流恢复正常。
- **原始1807财务附页仍受限**：[马德里自治区联合馆藏目录](https://bibliotecavirtualmadrid.comunidad.madrid/bvmadrid_publicacion/es/consulta/registro.do?id=63115)对Ateneo A-Caj.179/5确认1808实物馆藏、明确写**Sin objeto digital asociado**；[Ateneo官方馆方联系页面](https://ateneodemadrid.com/biblioteca/)明确列馆藏及复制服务邮箱 **biblioteca@ateneodemadrid.es**。已在[未发送西班牙语申请文稿](ARCHIVAL_REQUEST_ES_M2E_20261114.md)补全收件人和卷页咨询问题；**没有发送邮件、没有提供身份、没有获得扫描件**。
- **因果与数量边界**：政府融资/银行账面集中、白银出口利润消失、vales贬值、内部控制风险及1808政治冲击是多个并行机制；须取得对应年度原始现金流、账册和民间贴现余额才可定量识别。既有217.3/166.4/125.653百万雷亚尔债权口径差异仍未对清。

**M2f唯一下一项工作**：在身份与复制使用条件获合法授权后，向Ateneo请求其1808股东大会馆藏A-Caj.179/5是否有完整1807财务折页、其阅览及数字化影像许可；同时向Banco历史档案查询1807原始Real Hacienda总账及拖欠利息簿的具体卷号。拿到并逐项复核影像后才能继续双边对账。


---

## M2g：1829银行—国库债务和解原始法律文件和股本记录冲突（2026-11-14）

- 新增[1829年原始合同/股本年份/数字化原账路径研究](M2G_1829_PRIMARY_SETTLEMENT_AND_CAPITAL_DATE_AUDIT_20261114.md)、[债权和解数据](bank_1829_primary_settlement_m2g.csv)、[银行股数和账面资本时间冲突表](bank_share_capital_dating_conflicts_m2g.csv)、[官方数字会议簿目录与1808印本访问清单](bank_original_record_access_m2g.csv)、[来源台账](source_registry_m2g.csv)和[交接记录](sessions/2026-11-14-spain-m2g-1829-bank-settlement.md)。
- **取得原版扫描一手证据**：西班牙[1829年9月3日《马德里公报》官方原文](https://www.boe.es/gazeta/dias/1829/09/03/pdfs/GMD-C-1829-122.pdf)刊载银行与王室财政的1829年6月29日协议、7月9日批准令：协议当时列示国家债权**309,475,983雷亚尔+20马拉维迪**，谈判对价**40,000,000雷亚尔**，并将这笔资金投入新的圣费尔南多银行。按列示债权面额，名义对价比**12.925074%**，名义让步**87.074926%**。**这是1829年合同条款，不是1807银行资产损失率，也未证明全部现金即时交割。** 该合同包含部分未确权债权和其他将来待结项目，不能跟1807银行账面217.3百万或1808国库125.653百万直接串接。
- **官方档案的独立新路径**：西班牙央行[数字化原始治理会议簿合集](https://www.bde.es/wbe/es/punto-informacion/contenidos/servicios/archivo-historico/colecciones-digitalizadas/)覆盖圣卡洛斯银行原始董事会和股东大会记录；西班牙Hispana政府资料索引确认**1790年原始董事会簿**具体签号 **ES.28079.AHBE/01.01//000147**、276页、标注CC BY-NC-ND 4.0。**1790这份影像及1808年目标财务折页均没有成功打开**，银行资料库网页访问HTTP400。前轮Ateneo馆藏登记“Sin objeto digital asociado”仅指Ateneo自己的目录，不等于西班牙央行原始会议簿没有数字化，M2f报告已作追补更正。
- **核查出年份矛盾**：1782设立敕令为150,000股×2,000雷亚尔=300百万；西班牙央行2017年历史著作称1790年股本缩至240百万；然而BBVA 2005年原表9.8显示**1794年末账面资本仍300百万、1795年才转为240百万**。1785—89年购回30,628股及1806年120,000股流通的历史叙述支持有资本收缩，但回购、决定、法律注销、账面确认的各年份未由原账核实，**不能自行为冲突选择年份**。
- **现有限制**：UKDS g104spd3仍未获得，1807银行Real Hacienda原账及原1815出版财务折页未读。银行/财政借款及债息造成陆海军或私人贷款挤出的因果实验尚未运行。已有已发表出版物的账表不等于原始年报。

**唯一下一步**：从官方数字化会议簿平台找到1808年股东大会和1790—1795股本回购决议的永久原文编号；门户不可访问时向档案馆索取影像及1807原账签号，再以原件完成217.3、166.4和125.653百万雷亚尔会计口径对照。


---

## M2h 1790年的真实账簿分类、非现金应收利息与分红资本口径（2026-11-14）

本轮实际逐页截图核查 R. Moreno Fernández（AECA 2012）历史会计论文第15—18页，补齐了 M2g“1790有效资本240百万、1795账面资本240百万”两种年份差异的**分红分母**和**更早的银行资产质量**证据：

- [M2h来源审计与风险机制报告](M2H_1790_BANK_ASSET_QUALITY_AND_DIVIDEND_CAPITAL_AUDIT_20261114.md)、[1790-07-06银行资产四类分拆](bank_1790_assets_m2h.csv)、[损失与抵补项目及马拉维迪级差额](bank_1790_losses_and_non_cash_bridge_m2h.csv)、[1789及1790两个不同利润年度的分红票决](bank_1789_1790_dividend_policy_m2h.csv)、[1790原始书/卷/页精准定位](bank_1790_original_access_m2h.csv)、[来源登记](source_registry_m2h.csv)、[研究session](sessions/2026-11-14-spain-m2h-1790-capital-dividends.md)。
- 1790-07-06历史来源列示银行资产总额**340,791,022名义雷亚尔**，分正常业务134,769,661、损失47,017,489、可疑汇兑18,170,226、暂时不可动用140,833,645；四部分合计**340,791,021**，源表有**1雷亚尔差**，保留而非篡改。列入风险/冻结三类占总账约60.45%，**不能称为实际损失率或现代不良率**。这说明晚期殖民战争与1807国库集中债务之前，银行已承担供应合同和自身股票回购损失。
- 史学论文还列当时抵补项目38,244,504雷亚尔+10马拉维迪，包括**菲律宾公司股份和被认可但尚无项目内现金兑付证明的国库利息3,713,280雷亚尔+6马拉维迪**；详细损失减抵补严格复算资本缺口8,772,985雷亚尔整，而原文报告8,772,984雷亚尔+33马拉维迪，**差1马拉维迪**。1790-07-06的分类与1790年度末资本缺口**不属于同一切账时点**。
- **重要会议日期更正**：1790年召开的股东大会对**1789经营年度**1200万雷亚尔（5%）股息提议，以**31赞成、210反对否决**；随后讨论**1790经营年度**的相同名义提议，在**1791年下一届股东大会**获作者记载的批准。不能误报1790股东会已批准或已现金分红。两个提案都隐含**1200万÷5%=240百万雷亚尔的分红基数**，支持其与BBVA报表1794年度账面Capital=300百万属于可能不同的计量口径，但**正式股份注销或总账确认时点未知**。
- 精确来源：1790年原始董事会AHBE秘书处**AJD Libro 145 fols289–291**；1790年股份回购许可**Caja984**；1794年董事会**AJD Libro154 fols271–274v**。此外格拉纳达AHFT目录提供1790股东大会印本的数字母本**7-FSAAVEDRA_C25_007**（322.8 MiB），**实际大文件及图像尚未成功读取**；[西班牙语定向咨询文稿](ARCHIVAL_REQUEST_ES_M2E_20261114.md)已补充这一馆藏及具体卷页请求，**NOT_SENT**。
- **证据层级**：2012 AECA与2014西班牙央行研究同一作者、多处复用1790原始账，不能视为独立两次历史原账核验。1807原银行账、UKDS马德里24年原表和因果债息挤出继续NOT_ACQUIRED/NOT_RUN。

**下一唯一工作**：合法取得格拉纳达 AHFT 1790原始印本指定页及西班牙央行1790/1794 AJD相关原卷页，核对实际股份分母与1790—1795资本账面确认流程后，再返回1807王室债权/债息账的跨时点核对。


---

## M2i 1790王室决议、1791大会原印本数字条目及1793九百万雷亚尔赔偿（2026-11-14）

- [M2i来源与会计审计报告](M2I_1790_1793_ROYAL_ORDERS_AGM_AND_PREMIUM_CONFLICT_20261114.md)、[1790—1793原始股东大会/王令数字档案标识](original_bank_AGM_1790_1793_locator_m2i.csv)、[1790—1793国王财政指令和补偿时间线](bank_1790_1793_royal_compensation_m2i.csv)、[银行股份回购溢价不同历史口径的2万雷亚尔冲突](bank_buyback_premium_crosssource_m2i.csv)、[资料分级台账](source_registry_m2i.csv)、[session](sessions/2026-11-14-spain-m2i-royal-orders-original-agm.md)。
- **新定位的三个原始印本（目录不是原文已读）**：格拉纳达AHFT **C25_007**（1790年大会216页、数字母本322.8MiB），**C25_010**（1790年王室处理银行请求及财政大臣Lerena报告72页、108.5MiB），**C25_008**（1791年10月大会362页、511.1MiB）。AHFT把1790与1791两次大会都标为*octava*；BNE与Banco2014把1791年标为*novena*，应取原印本扉页核对。这些大型原件的图像**尚未成功取得**。
- **国家图书馆已有1791年数字化原件**：BNE/BDPI明确列**1791年10月第九届股东大会、1792年印本、索书号HA/8649(7)、数字文件编号hd0069882062**。实际链接[hemerotecadigital.bne.es/issue.vm?id=0069882062](https://hemerotecadigital.bne.es/issue.vm?id=0069882062)返回403；**DIGITIZED_NOT_READ**，并非没有数字化。
- **1791年资本口径新锚**：Banco de España EHE67（2014）第64页转述1791-04-11王室命令：回购30,000股后可用于投资的资本**240百万名义雷亚尔**，与1790/1791股息名义240百万的计算分母一致；BBVA历史账面1794仍300百万、1795才240百万。**授权投资资金/分红分母不是同一账面Capital字段**，具体法律注销年尚不能宣称已证实。
- **新增国家财政承诺**：AECA（2012）发表页第19页截图实际核验：王室1790-05-19先提出补偿银行供应合同亏损，经专员1793-08-07核查后于**1793-08-24决定补偿900万雷亚尔**，引原始AHBE **AJD Libro153 fols139v–145v**。这仅是**批准补偿额**，不是现金实际兑付记录，不得与1790年已认可利息重复计入现金财政收入。
- **跨论文账目差异**：同一作者2012年报告1790年30,628股超额回购账目损失5,284,027雷亚尔尾数26，而2014年讨论1794诉讼中30,000股5,175,849尾数14和额外628股128,178尾数12，相加5,304,027尾数26，**差20,000雷亚尔**。源别、账期、尚未冲销款及余额口径可能不同；保留双源值不自动纠正。
- **阻断仍在**：实际未打开AHFT1790/1791原印本、BNE影像403、2014出版PDF截图超时、未取得1807银行原账/UKDS g104spd3，未运行私人信贷或债息挤出因果检验。[原先的西班牙语咨询稿](ARCHIVAL_REQUEST_ES_M2E_20261114.md)已增加上述精确馆藏请求，**未发送**。

**唯一下一步：** 合法获得 AHFT 的 **C25_010**（1790王室决议）及 **C25_008**（1791大会）指定页或BNE数字原件0069882062，先核对会期、股本口径、1790利润股息、补偿确认，再追同业账户里900万是否实际结算；继续保留Issue Open、PR Draft。


---

## M2j：1793年原始银行股东大会公告与1884年地方港口贷款/中央国库债务界定（2026-11-14）

- [M2j双原始公报扫描取证、银行治理与债务人身份审计](M2J_1793_AGM_RULES_1884_VALENCIA_DEBT_AND_SETTLEMENT_AUDIT_20261114.md)、[1793银行股东参会与代理规则](bank_1793_AGM_governance_primary_m2j.csv)、[1795—1839港口工程借款与1884国库裁决](bank_1884_valencia_loan_and_1829_payment_m2j.csv)、[源账历史货币精确加总及争议](bank_1884_primary_source_arithmetic_checks_m2j.csv)、[来源台账](source_registry_m2j.csv)、[研究session](sessions/2026-11-14-spain-m2j-valencia-state-debt.md)。
- **直接看见1793年当时官方原文扫描第487—488页**：[《马德里公报》1793-05-28](https://www.boe.es/gazeta/dias/1793/05/28/pdfs/GMD-1793-43.pdf)公示银行1793-07-20拟召开的股东大会审议1792财年。个人参会至少**25股**，按1782官方章程面值2000雷亚尔/股计算=**50,000雷亚尔名义持股门槛**；新规禁止多个小股东合并凑足25股取得一票（原1782章程曾允许），但未观察真正参会投票人数、股权结构或现金分红。
- **直接看见1884年财政部原始行政裁决扫描第224—225页**：[《马德里公报》1884-04-26](https://www.boe.es/gazeta/dias/1884/04/26/pdfs/GMD-1884-117.pdf)：圣卡洛斯银行于1795年10月与**瓦伦西亚格劳港工程委员会**签约，并在1795-11至1797-03以 **vales reales政府纸币**分批贷出**8,363,895雷亚尔+12.5马拉维迪**；1839港口工程账目列余欠**4,503,006雷亚尔+10马拉维迪**（其中本金3,680,113+33mrs，利息822,892+11mrs，算术PASS）。**1884财政部拒绝将该贷款判为中央国库需要承担的“carga de justicia”**：地方公共工程获政府许可融资，不能自动作为国王/中央国库直接举借的债务。不可把全部银行公共工程资产混入国债统计。
- **重要源文本算术问题**：1884原件所列1795贷款本金与长期合同利息相加为**12,968,575雷亚尔+4又5/6马拉维迪**，却把预计债务总额写为**12,968,875雷亚尔+同一尾数**，**恰差300雷亚尔**。以1雷亚尔=34马拉维迪=204个1/6马拉维迪单位复算；只记录差异、不能自称修正1795原契约。
- **1829和解状态更正（新史料）**：1884年财政裁决明确指出国库已**履行**对圣卡洛斯银行约定的4000万雷亚尔和解款。因此证据从「仅见1829原协议」提升为「**1884年官方事后履行认定**」；然而**1829—31银行实收凭证、具体款项支付日、支付工具和新银行权益入账依然未取得**。1884追述的协议日期**1829-06-23**与1829原版法令**1829-06-29**不一致；保留时间冲突。已在[M2g原报告](M2G_1829_PRIMARY_SETTLEMENT_AND_CAPITAL_DATE_AUDIT_20261114.md)追加证据状态更正。
- **未获得的资料**：1790 AHFT C25_010原本太大（平台报HTTP400）、1791 BNE原件此前403；1795港务委员会原始公证借款合同、1839地区港口账、1829清偿实际票据、1807银行Real Hacienda总账及UKDS马德里资料尚NOT_ACQUIRED。未运行海外财政/军费或私人信贷因果研究。

**唯一下一动作**：查找1795-10-06及22日瓦伦西亚格劳港工程委员会与圣卡洛斯银行的**原始公证合同或独立誊录文本**，确定同一债务人的利率、金额分项及1884官方转引中的**300雷亚尔差额**，再判定该贷款是否绝不可混入中央国库债务；同时保留原1790/1791馆藏的授权访问阻断记录。


---

## M2k 1887年最终司法判决、融资抵押税源及港口贷款实收证据（2026-11-14）

- [M2k司法原始公报与财政—银行会计审计](M2K_1887_FINAL_JUDGMENT_PORT_CREDIT_TAX_AND_BANK_RECONCILIATION_20261114.md)、[1791—1887贸易授权/财政税源/银行贷款及司法时间线](port_1791_1887_legal_finance_timeline_m2k.csv)、[港口贷款名义本金利息与1862认证累计还款](port_loan_nominal_repayment_m2k.csv)、[王室许可、国库税款代收与最终债权消灭责任矩阵](port_loan_legal_attribution_matrix_m2k.csv)、[1794原始税款指令及1836档案转存路线](port_original_archive_chain_m2k.csv)、[M2k来源台账](source_registry_m2k.csv)、[研究会话](sessions/2026-11-14-spain-m2k-1887-final-court.md)。
- **正式司法结论首次直接核查原版扫描**：[1887-11-26《马德里公报》第557—559页](https://www.boe.es/gazeta/dias/1887/11/26/pdfs/GMD-1887-330.pdf)，1887-10-24摄政王太后颁令依据最高行政诉讼法院/Consejo de Estado意见：**驳回银行请求，维持1884年财政部拒付决定，基于1829年全银行—国家债权和解消灭请求权**；**政府的反请求仅因诉讼程序不合而不予受理，并非银行必须实际退款的实体判决**。全三页 web PDF 截图成功读取。
- **银行1780年代后期融资方式更加复杂**：1887法令列1794-10-07王室推动银行资助港口，1795-09-28批准贷款操作，1795-10-06/22银行同港口Junta签署、追认契约；担保包括**指定征收的领事税、丝绸税和1,237股Propios y Pósitos权益**。**1795初始合同主体为地方Junta**，王室授权≠国库直接借款人；但**1802年税款改由王室官员代收、1817—1818年王室就税款拖欠及潜在银行本金利息负担发布命令**，不能据1884行政拒付断言国家从未参与或可能承担风险。
- **1887引用的1862年财政证明**：1797—1807、1813—1821和1826—1836期间银行从港务项目累计收到名义**13,703,208雷亚尔**（资本及利息合并），但1839港口财务账也列约**4,503,006雷亚尔＋10马拉维迪**未清请求。由于*vales reales*面值与实际兑现价格、偿还项目和账期均未调和，**不能由13.703百万大于银行最初8.364百万就认定银行获利，不能仅做现金流净额**。
- **M2j 300雷亚尔差额得到第二份公报对照但尚未解开**：1884原文所列总额**12,968,875雷亚尔＋4⅚马拉维迪**，而本金和利息精算为**12,968,575雷亚尔＋4⅚马拉维迪**；1887原文p558似写作**2,968,575雷亚尔＋5马拉维迪**（疑似漏前导“1”），其“968,575”尾部更接近分项加总。**两份公报不是1795原始公证契约，不擅自纠正文书**。已在[M2j原报告](M2J_1793_AGM_RULES_1884_VALENCIA_DEBT_AND_SETTLEMENT_AUDIT_20261114.md)添加司法终局与账目口径更正。
- **原始档案传承与更高效的获取目标**：1887原版诉讼文件指出，1862银行索赔卷附**1795-10-22贷款契约追认的公证誊本、1862-11-13瓦伦西亚财政证明、1839港口清算资料**。1836原港务Junta会计文件移交瓦伦西亚 **Gobierno Civil** 档案；[现存瓦伦西亚省议会官方 Gobierno Civil 基金](https://arxiu.dival.es/es/guia-del-archivo/content/gobierno-civil-valencia)仅证实主题和年份，尚不能确认1795借据现代具体盒号。此外[瓦伦西亚数字图书馆1794税费指令原印本 XVIII/4279(28)](https://bivaldi.gva.es/es/consulta/registro.do?id=8776)10页、Public Domain Mark，数字入口超时，**目录已读但正文未读**。[未发送档案询问草稿](ARCHIVAL_REQUEST_ES_M2E_20261114.md)已加入准确询问1795契约、1862证明及司法案卷的西班牙语请求，NOT_SENT。
- **官方港务局历史资料** [2018展览第8页](https://www.valenciaport.com/wp-content/uploads/Exposicion-La-Darsena-historica-1.pdf)截图核对：1791年对美贸易准许国内货品、1794年扩展、1792港口工程开建、泥沙淤积及战争导致长时间施工受阻。自然条件与财政/战争因素并存，不能单凭港务融资债务识别帝国衰落因果。
- **仍未获得**：1795原始银行/港务借款契约、1862支付表原页、银行1807 Real Hacienda原始总账、英国数据服务g104spd3；未运行银行信贷/王室债息挤占海军经费因果模型。

**唯一下一步**：向实际保管1887 **Consejo de Estado** 诉讼案卷（Banco de España v Hacienda）或瓦伦西亚 **Gobierno Civil历史基金** 的档案机构定位1862卷内1795-10-22契约誊本及1862财政师支付证明的**原始签号与获许可影像**，以原合同区分税收抵押、实际 Val­es 现金价值及300雷亚尔刊印差异；Issue #32继续Open、PR #36仍Draft。


---

## M2l: confirmed current archive custody route for 1887 Banco loan case (2026-11-14)

- [M2l original-document custodian and access report](M2L_1887_COUNCIL_ARCHIVE_CUSTODIAN_AND_1795_DEED_REQUEST_20261114.md), [8 official/referenced archival sources](source_registry_m2l.csv), [7 prioritized historical loan casefile document requests](port_1795_casefile_acquisition_matrix_m2l.csv), [research session](sessions/2026-11-14-spain-m2l-consejo-custodian.md), and revised [UNSENT Spanish library/archive request](ARCHIVAL_REQUEST_ES_M2E_20261114.md).
- Official [Consejo de Estado archive](https://www.consejo-estado.es/actividad/archivo-y-biblioteca/) says historic fonds includes around 130,000 cases from1833 to1939 and institution documents generated since1850. This makes **Consejo's own archive** the first logical custodian for the 1887-10-24 Banco de España versus Hacienda lawsuit, but **NO SPECIFIC EXPEDIENTE ID OR SURVIVING ANNEX VERIFIED**.
- The Consejo's [Memoria 2023 printed page84](https://www.consejo-estado.es/wp-content/uploads/2024/07/Memoria-2023.pdf) official text describes researcher inquiries answered remotely, with pre1987 opinion file searches requiring manual catalogs; PDF text read but screenshot attempt403. Specific verified scholarly archive contact **archivo.biblioteca@consejo-estado.es**, +34 915166356/357. **No message actually sent**.
- [Valencia Provincial Archivo Gobierno Civil](https://archivo.dival.es/es/fondo-documental/fondo-gobierno-civil) official live HTML verifies fondo **ES.462508.ADPV/Gobierno Civil (1739–1958)** and **GC:c.1 (1739–1924)** references to Banco San Carlos shares. Verified contact **archivo.general@dival.es**, +34 963882587; **no original 1795 deed or 1839 ledger item number established**.
- Precisely request the **1887 court case item ID**, its evidence index, **1795-10-22 notarized loan ratification testimonio** (in 1862 bank petition), **1862-11-13 Valencia public accountant individual repayments certificate**, 1836 Junta archival transfer inventory and 1839 local loan settlement book. Biblioteca Valenciana 1794 original ten-page port tax instruction **XVIII/4279(28)** remains CATALOG_ONLY; Cervantes reprints its bibliographic record, not a second original content read.
- **Financial conclusions unchanged**: 1884 contract total and components off300 reales, 1887 printed total suspicious, 1797–1836 bank receipts13,703,208 nominal reales cannot equal verified profits, actual original 1795 contract and Banco1807 subledger NOT_ACQUIRED, interest/credit/Navy crowdout causality NOT_RUN.

**Single next action:** obtain authorized local librarian retrieval of **1887 Banco-Hacienda litigation case signatura and the archival annex inventory**, via the officially verified Consejo archival address; upon failure/transfer, fall back to Valencia Gobierno Civil holdings. Issue #32 OPEN, PR #36 DRAFT; no merge or external inquiry performed by assistant.


---

## M2m · 1797年格劳港口工人工资拖欠、银行融资与工程施工现金流（2026-11-14）

- [M2m劳动—财政—银行融资研究审计](M2M_1797_PORT_WAGE_ARREARS_AND_CREDIT_STRESS_20261114.md)、[1797年202名普通工人工资档次及条件性日工资复算](port_1797_wage_labor_snapshot_m2m.csv)、[1792—1798信用/工资机制与替代解释表](port_1792_1798_credit_wage_mechanism_m2m.csv)、[5项出版物/史料来源等级与共同底本登记](source_registry_m2m.csv)、[研究session](sessions/2026-11-14-spain-m2m-1797-wages-credit.md)、[仍未发送的1797工资档案咨询稿](ARCHIVAL_REQUEST_ES_M2E_20261114.md)。
- 瓦伦西亚大学史学者 Ricardo Franch Benavent (2009大学库论文pp306—307；2012《Revista de Historiografía》)：格劳港1792-03-26开工，1795年工程计划预算约**1,500万名义雷亚尔**，Bank San Carlos贷款史料约**836万雷亚尔**；**1797-02-11港口工人因欠薪发生骚动**，1798-02-16王室成立新工程Junta，地方税不足、机构移交争议、战争及自然泥沙风险共同扰乱施工。若以M2j/M2k官方历史贷款名义本金**8,363,895雷亚尔**对约15m预算算术比为**55.7593%**，但**不是银行已支付工程费比例或实际现金支持比**。
- 2016同行评审论文 Franch, *Obradoiro de Historia Moderna* 25，DOI **10.15304/ohm.25.3202**，**原刊印刷p217**明确列202名peones及全员占比45%，**p236**补充78名amasadores和 A.M.V. Documentación Lonja Caja56 Exp19 原档号；相关引用均追溯作者2007年港口专题史pp192—194：18人×5、163人×4.5、21人×4名义雷亚尔/工作日，精确复算**907.5名义雷亚尔**，即**假如202人同日全部工作才有的理论当日普通工人工资账单**，不能认定实际欠薪金额、全体工作人员工资成本或已实际支付。原刊p236同段还列**78名amasadores（和泥工，5雷亚尔/人日）**，四组共280人、条件性同日工资**1297.5名义雷亚尔**；**M2o跨页复核**现确认2016原刊**p217**明确称202名peones占全体工人45%，恢复为**作者出版物的近似比例**；由此反推约449个总工人只是条件性估算，不可当作原始名册精确总数。另23名熟练泥瓦工平均约7.7雷亚尔是近似数据，独立标注不精确。
- **来源深度限制**：2009及2012瓦伦西亚大学机构PDF有可检索正文，但本轮web PDF截图两份返回**403**；2016期刊原版PDF链接503，正文数字由期刊搜索引擎索引给出，官方文章 DOI/书目可核查；2007核心章节目录表明原文不可公开下载。**三篇均为同一位学者基于自己2007港口史反复使用的历史材料，非3次独立原始账簿复验**。目前没有1797工资名册原稿、骚动记录或工地逐日收付账。
- **新可证伪层级**：1793专项港务税→1795银行政府票据贷款面值→地方港务Junta工地实际现金→工人工资拖欠→1798机构重组/施工风险。主要竞争解释包括银行 *vales reales* 折价、指定税源未到账、工程技术超支、承包管理争议、1796英西战争/海路阻塞；**从时间顺序不能推导哪个是已证实因果**。
- **所有原始银行与财政阻断仍保持**：1795贷款公证誊本、1862逐笔还款证明、2007原研究的1797劳动名册出处、1807银行王室债权总账、UKDS g104spd3未取得，未运行海军债息或私人信贷挤出因果估计。

**唯一下一步**：先获取 Franch(2007) *La fase inicial del puerto de Valencia a finales del Antiguo Régimen* **pp192—194及引述注脚**，查明1797港口劳动名册与1797-02-11工人薪资骚动的一手档案号；再与M2l已定位的Consejo de Estado 1887案件原件查询连接银行逐笔放款与工地工资现金流。保持Issue #32 OPEN、Draft PR #36 未合并。


---

## M2n：1797年实际档案号已锁定，劳动工种遗漏和2016出版页码已纠正（2026-11-14）

- [M2n直接档案签号/工资统计审计](M2N_1797_ORIGINAL_PAYROLL_SIGNATURA_AND_TRADE_WAGES_20261114.md)、[10条1797年劳动工种、工资范围和条件性统计](port_1797_complete_trades_wage_m2n.csv)、[5项具体原档及研究窗口检索清单](port_1797_exact_archive_request_m2n.csv)、[5个分级来源](source_registry_m2n.csv)、[研究会话](sessions/2026-11-14-spain-m2n-1797-lonja-signatura.md)、[仍未发送的西班牙语精确查询稿](ARCHIVAL_REQUEST_ES_M2E_20261114.md)。
- **核心新增真实来源定位**：Franch Benavent（2016）*Obradoiro de Historia Moderna*原刊**印刷第236页**的可检索PDF原文（此前M2m误写p217，已更正）直接引用**A.M.V. Documentación Lonja, Caja 56, Exp. nº 19**，为其1797年港口工人名册的原始馆藏号。**学者引用不是我们已阅原件**；2016期刊PDF直接打开返回503、截图不可用。2007先前研究印刷pp192—194仍未取得。
- **当代保管机关独立核实**：[Ayuntamiento de València Archivo Histórico Municipal](https://www.valencia.es/es/-/archivo-hist%C3%93rico-municipal)官网列独立**Documentación Lonja**档案目录375页PDF。官网HTML和目录首页索引文字已读，但该大型PDF指定条目find/screen超时，**没有独立从目录确认Caja56 Exp19的现实案卷标题/页数及在库状态**。政府正式咨询邮箱**archivo@valencia.es**，预约**citapreviaarchivohco@valencia.es**，访问窗口在Palacio de Cervelló，Plaça Tetuán 3；未发送邮件。
- **修正遗漏的一类工人**：2016原文同时列**78名amasadores ×5雷亚尔/日=390**，另外202名peones按18×5、163×4.5、21×4精确小计**907.5**。**四组280名人员的假设同日工资1297.5雷亚尔**；比仅202名普通工的小计多42.9752%。原文还涉及23名熟练泥瓦工（平均约7.7仅是作者近似值）和两名管理/高级工种，合计**至少305个显式人员岗位**，**不是全港口雇员统计或真实日付薪**。**M2o纠错：45%实际见2016原刊p217正文，不能因p236未重复便隔离整篇论文的该项数据**；比例恢复为学者出版近似值，449人只是一项计算估算，不是原始雇工清册总数。
- **只解决来源与计算，不解决因果**：原1797年Caja56Exp19未读，工地真实出勤、工资应付/实付及1797-02-11工资骚动原始记录未取得；银行*vales reales*贷款、地方港务税款现金转付和战争/工程自然条件竞争解释仍未核实。此前M2m报告、CSV与来源台账已回补页码、增加遗漏工种警示、在M2o复核后恢复p217的45%近似比例、同时不将反推449人伪报为精确统计。

**下一唯一动作**：依据精确文献引用 **A.M.V., Documentación Lonja, Caja56 Exp19**，先由馆员确认现实卷件和合法获取工资名册少量页面的方法，再独立定位1797-02-11欠薪骚动原始文书；只有拿到工资应付和实付的真实流水，才能和银行贷款交割时序对账。Issue #32维持Open、PR #36维持Draft。


---

## M2o：2016原论文第217/236页交叉复核纠正M2n的45%过度隔离（2026-11-14）

- [M2o跨页史料与方法论审计](M2O_1797_P217_P236_WORKFORCE_SHARE_RECONCILIATION_20261114.md)、[7条来源页码—统计命题矩阵](port_1797_journal_crosspage_provenance_m2o.csv)、[10条样本占比反推假设与工资敏感性情景](port_1797_workforce_denominator_sensitivity_m2o.csv)、[5项证据等级与PDF访问状态](source_registry_m2o.csv)、[研究会话](sessions/2026-11-14-spain-m2o-crosspage-percent-audit.md)。
- **纠正M2n的错误隔离**：Franch Benavent（2016）原期刊PDF的出版社可检索文字**印刷p217**明确记载：1797年202名peones占瓦伦西亚港工程全部工作人员约45%，并列18×5、163×4.5、21×4名义reales的日薪；**印刷p236**则另列78名amasadores及明确原始档号 **A.M.V. Documentación Lonja Caja56 Exp19**。旧M2n只看p236而未检索p217，误判45%无来源；已经按命题更正历史报告、CSV及来源台账。
- M2m原有**202名peones的907.5名义reales条件性共同日工资**保持不变；M2n增加78名amasadores后，四组**280人、1297.5名义reales**保持不变。45%为**学者对原始用工名册的近似比例**而非本项目已阅一手账本；202/0.45≈**449**为粗估。如果额外假定原文45%是最近百分点的四舍五入，则全员整数可能为**444—453**，但该假定本身并未得到历史作者确认，绝不能称已确定全体工人数或出勤人数。
- **市政府当前原档查找仍受阻**：[官方Archivo Histórico Municipal](https://www.valencia.es/es/-/archivo-hist%C3%93rico-municipal)页面第33行列Documentación Lonja PDF约1.2MB，可合法访问的馆藏门类得到独立核实；本轮点击其官方链接及直接下载该PDF均超时，本地容器网络DNS解析失败，**未实际读到其Caja56 Exp19现代馆藏目录条目、更没有读1797工资名册/工资支付原页**。2016期刊PDF全文打开也返回503，实际论断核实来自出版者PDF搜索索引，不能声称影像检查。
- **历史事实验收界限**：202名peones占45%、78名amasadores以及档号是**同一学者同一文章不同页的发表命题**，不是多重独立原始史料。未取得员工逐日出勤、实际工资发放、1797-02-11骚动原件、1795–97银行vales放款到工程实际现金及地方专项税款明细，**没有债息→港口工资或战争冲击的因果检验**。

**唯一下一步**：向已核实官方入口 **archivo@valencia.es** 定向询问现存 **A.M.V. Documentación Lonja Caja56 Exp19** 的档案题名、页码与合法部分影像获取方法；按真实原始工资付款页与港务Junta账簿复算已付/应付/欠付，再另找1797-02-11骚动原始记录。Issue #32 OPEN，Draft PR #36不合并。
