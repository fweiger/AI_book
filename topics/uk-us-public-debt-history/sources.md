# TOPIC-005 来源登记与核查边界

## 2026-11-07 R5 原始来源补充及阅读级别（裁判记录，待人工复核）

> 来自[Agent F-R4](https://github.com/fweiger/AI_book/issues/20#issuecomment-6691211843)的材料审计；此处是来源**索引**，不表示本次R5逐页重新下载核影。关键来源的正文、原表图像、目录和摘要必须分级；`CATALOGUE_ONLY`不能证明档案内容。

| R5来源ID | 原始档案/官方表 | F报告使用范围 | 阅读状态与限制 |
|---|---|---|---|
| R5SRC01 | [ONS NMFX](https://www.ons.gov.uk/economy/governmentpublicsectorandtaxes/publicsectorfinance/timeseries/nmfx/pusf) · [ANBV](https://www.ons.gov.uk/economy/governmentpublicsectorandtaxes/publicsectorfinance/timeseries/anbv/pusf) | CG净息/全部当期收入 | PRIMARY_DATA；日历年/回溯版、非税收分母 |
| R5SRC02 | [FRUS1947 d24](https://history.state.gov/historicaldocuments/frus1947v05/d24) · [d25](https://history.state.gov/historicaldocuments/frus1947v05/d25) · [d36](https://history.state.gov/historicaldocuments/frus1947v05/d36) | 希土外币援助与英美协议时序 | PRIMARY_TEXT；不等于同额拨款已结算 |
| R5SRC03 | [Hansard1947-03-14](https://api.parliament.uk/historic-hansard/commons/1947/mar/14/assistance-to-greece) | 英方政策备选与议会表述 | PRIMARY_TEXT；决策边际债息未识别 |
| R5SRC04 | [FRUS1956 d516](https://history.state.gov/historicaldocuments/frus1955-57v16/d516) · [d519](https://history.state.gov/historicaldocuments/frus1955-57v16/d519) · [d525](https://history.state.gov/historicaldocuments/frus1955-57v16/d525) | 苏伊士11月停火、金融通话争议 | PRIMARY_TEXT / 时间戳冲突；即时IMF通牒NOT_IDENTIFIED |
| R5SRC05 | [英国CAB195/15官方转录](https://cdn.nationalarchives.gov.uk/documents/cab-195-15-transcript.pdf) | 内阁笔记1956-11-06/07印刷p.174–175 | TRANSCRIPT_VERIFIED；非原手稿影像 |
| R5SRC06 | [IMF基金官方历史](https://www.elibrary.imf.org/display/book/9781451955255/ch016.xml) · [Boughton研究](https://www.elibrary.imf.org/abstract/journals/001/2000/192/article-A001-en.xml) | 12月IMF已提款/未提款备用融资 | OFFICIAL_LATER / RESEARCH_FULL；不是11/6当日IMF收发件 |
| R5SRC07 | [Hansard1968-01-16](https://api.parliament.uk/historic-hansard/commons/1968/jan/16/public-expenditure) · [FRUS1967 d269](https://history.state.gov/historicaldocuments/frus1964-68v12/d269) | 东苏伊士撤退加速与国际收支制约 | PRIMARY_TEXT；预算方案/实支需桥接 |
| R5SRC08 | [澳DFAT1966内阁记录](https://www.dfat.gov.au/about-us/publications/historical-documents/volume-27/Pages/059-minute-of-cabinet-defence-and-oversea-policy-committee) · [FRUS1968 d150](https://history.state.gov/historicaldocuments/frus1964-68v21/d150) · [FPDA](https://www.fivepowerdefencearrangements.org/history) | 地区利益、美国非普遍接手、1971联防制度 | 公开原文/官方后期历史混合；按具体条约校核 |
| R5SRC09 | [BoE1950原始PDF](https://www.bankofengland.co.uk/-/media/boe/files/archive/uk-overseas-investments/1938-1948.pdf) · [BoE1970统计摘要](https://www.bankofengland.co.uk/-/media/boe/files/archive/statistical-abstract/number-1-1970.pdf) | 海外证券/英镑负债分项 | TABLE_TEXT_READ / TABLE_IMAGE_PENDING，原表未逐格核影 |
| R5SRC10 | [OBR2013战后债务](https://obr.uk/box/post-world-war-ii-debt-reduction/) · [OBR300年财政史](https://obr.uk/docs/dlm_uploads/300-Years-of-public-finances-Accessible-PDF.pdf) | 战后名义债务端点、1815反例 | OFFICIAL_LATER；历史口径不等于各年PSND |
| R5SRC11 | [NBER/FRED历史工业指数](https://fred.stlouisfed.org/data/A01181GBA324NNBR) · [FRUS1947印度](https://history.state.gov/historicaldocuments/frus1947v03/d91) | 1914前相对/绝对与殖民政治反例 | 史学估计/PRIMARY_TEXT |
| R5SRC12 | UK CAB128/9、CAB129/128/2、T236/4188–4189、BoE G1/124、US Treasury RG56、IMF当日通讯 | 尚需取得的英国/美国/IMF同日档案 | **CATALOGUE_ONLY / SOURCE_UNAVAILABLE**；档号不是内容证据 |

后续补档任务与验收条件：[OPEN_GAPS.md](OPEN_GAPS.md)。用户若希望比较美国，只能迁移研究变量、不能凭英国历史固定阈值预测美国结局。

---

| 编号 | 来源 | 目前已核实的范围 | 待补问题 |
|---|---|---|---|
| UK01 | [英国上议院经济事务委员会，*National debt: it's time for tough decisions*（历史PSND）](https://publications.parliament.uk/pa/ld5901/ldselect/ldeconaf/5/504.htm) | 表述1947年附近PSND峰值，历史图数据：FY1945/46约246.8%，FY1946/47约251.8% | 下载机器可读官方数据、核对最新修订 |
| UK02 | [英国预算责任办公室 OBR，*Economic and fiscal outlook*, 2026-10](https://www.gov.uk/government/publications/october-2026-economic-and-fiscal-outlook/economic-and-fiscal-outlook-october-2026) | 二战后约250%债务，战后三十年下降的概述 | 精读相关债务段落、核对当代数据 |
| UK03 | [英国议会：*Some total*（历史国债）](https://www.parliament.uk/business/publications/research/olympic-britain/the-economy/some-total/) | 记载二战后峰值约252% | 与UK01数据版本比对 |
| US01 | [美国国会预算办公室CBO，*The Budget and Economic Outlook: 2026 to 2036*](https://www.cbo.gov/publication/61882) | 2026公众持有联邦债务/GDP预测101%；1946年历史峰值106%；2036年基线120% | 机器可读时间序列、政策基线修订 |
| US02 | [美国众议院预算委员会2026年2月CBO基线摘要](https://budget.house.gov/imo/media/doc/cbo_baseline_february_2026.pdf) | 报告当时总联邦债务/GDP约123.1%，2036约136.4%；二次摘要 | 优先取得CBO原始表复核，区分当前值与财年终值 |
| US03 | [美国政府问责局GAO，2026-06财政健康报告](https://www.gao.gov/products/gao-26-108610) | 2026年4月公开持有债务约31.3万亿美元，与GDP规模接近 | 确认时点和分母，不与US01年度基线混用 |

## 来源层级

A：英国OBR/ONS/UK DMO、美国CBO/Treasury/OMB/BEA等原始统计文件、完整方法说明；B：议会/GAO政府报告及原始文档引用的统计重述；C：学术论文及机构研究（有数据和可重复方法）；D：新闻、视频、二次观点。层级只是待审查工作分类，不代表材料自动正确。对论文要区分全文已核、摘要级与未读全文。

## 数值差异与尚未审定项

- 早期私人研究里英国1946/47约251.7%；英国议会所列约251.8%。差值不能直接解释为错误，需核原数据/舍入/修订。
- 早期私人研究美国2026约123.6%；US02对应约123.1%，US01公众持有口径101%。是否同一时间点、分母和机构定义仍待核。
- 任何新序列应保留来源页面、下载时间、统计发布日期、版本、财政年度、债务定义和链接。
- 目前未取得此前ChatGPT原始会话真实ID，故不提供无法核验的私人会话链接。


## 2026-11-04 新增：英国霸权衰落的债务/资本/地缘研究（优先）

| 编号 | 学术/原始资料 | 支持方向 | 阅读级别 |
|---|---|---|---|
| UK04 | [OBR战后债务率下降：名义国债£27bn→£64bn](https://obr.uk/box/post-world-war-ii-debt-reduction/) | 反驳债务率降=大规模本金归还 | 官方文章 |
| UK05 | [英国央行：UK Overseas Investments 1938–48（1950）](https://www.bankofengland.co.uk/-/media/boe/files/archive/uk-overseas-investments/1938-1948.pdf) | 涵盖证券海外资产1938–48减少£1.585bn、45%；新增投资少 | 原始档案PDF文字可读，截图验证受缓存故障限制 |
| H01 | [Asteris 2013：英国1945–47海外军事承诺](https://doi.org/10.1080/13619462.2013.796884) | 经济约束迫使缩减，但不是具体撤退选择的唯一决定因素 | ABSTRACT_ONLY |
| H02 | [Tomlinson 2009：战后国际收支与战略过度伸展](https://eprints.gla.ac.uk/81167/) | 反向因果/政策过度伸展解释 | ABSTRACT_ONLY |
| H03 | [Peden 2012：苏伊士与世界实力衰落](https://www.stir.ac.uk/research/hub/publication/521896) | 高国防支出、相对规模、1959后政策选择 | ABSTRACT_ONLY |
| H04 | [Avaro 2024：Zombie International Currency, 1945–71](https://www.cambridge.org/core/journals/journal-of-economic-history/article/zombie-international-currency-the-pound-sterling-19451971/7B7C31079FB943B4971CD4B9257013AB) | 英镑区域外债、控制及储备货币信誉 | OPEN_TEXT_READ |
| H05 | [Abreu 2017：印度英镑余额，1940–53](https://ehs.org.uk/article/britain-as-a-debtor-indian-sterling-balances-1940-53/) | 外债/战时英镑余额而非国内政府本金 | ABSTRACT_ONLY |
| H06 | [Boughton 2002：苏伊士与IMF](https://www.elibrary.imf.org/view/journals/024/2002/001/article-A001-en.xml) | 汇率/美元储备约束 | PUBLIC_TEXT_PARTIAL |
| H07 | [Schenk 2010：英镑国际货币地位撤退](https://eprints.gla.ac.uk/29894/) | 国际合作、外债与储备地位 | BOOK_ABSTRACT_ONLY |
| H08 | [Schenk 2004：香港及1967英镑贬值](https://doi.org/10.1111/j.1468-0289.2004.00288.x) | 外部金融关系逆转 | ABSTRACT_ONLY |
| F01 | [FRUS美国国务院1947-02-24](https://history.state.gov/historicaldocuments/frus1947v05/d31) + [1947-02-26](https://history.state.gov/historicaldocuments/frus1947v05/d36) | 英国财力不足，退出希腊土耳其援助 | 同期外交档案 |
| F02 | [美国国家档案馆《杜鲁门主义》](https://www.archives.gov/milestone-documents/truman-doctrine) | 美国随后提出$400m援助希腊/土耳其 | 官方档案机构 |
| US04 | [CBO 2026-02基线](https://www.cbo.gov/publication/62105) | FY2026净利息/GDP3.3%、公众持有债务/GDP101%（预测） | 官方预测 |
| US05 | [BEA 2026Q2 NIIP](https://www.bea.gov/data/intl-trade-investment/international-investment-position) | 对外资产$46.97tn、负债$69.39tn，净头寸-$22.42tn | 官方实绩 |
| US06 | [BEA 2025海外FDI](https://www.bea.gov/news/2026/direct-investment-country-and-industry-2025) | 2025末海外直接投资存量$7.14tn、年度增加$438.1bn | 官方实绩 |
| US07 | [IMF 2026Q2 COFER](https://data.imf.org/en/news/imf%20data%20brief%20september%2030) | 全球官方外储美元份额56.70% | IMF官方统计 |
| US08 | [SIPRI 2025军费](https://www.sipri.org/publications/2026/sipri-fact-sheets/trends-world-military-expenditure-2025) | 美国2025军费$954bn、全球份额33%，与财政国防不同定义 | SIPRI统计 |

完整提炼与竞争证据见[RESEARCH_EVIDENCE_20261104.md](RESEARCH_EVIDENCE_20261104.md)。
