# CASE-NLD-001 — M1财务证据复核（2026-11-14）

状态：`SOURCE_TABLE_REPRODUCED` / `SOURCE_CONFLICT_OPEN` / `ORIGINAL_LEDGER_NOT_ACQUIRED` / `CAUSAL_TEST_NOT_RUN`。
权威任务：[AI_book #33](https://github.com/fweiger/AI_book/issues/33)；同一已有 [Draft PR #37](https://github.com/fweiger/AI_book/pull/37)。不改动main、不合并PR、不关闭Issue。

## 1. 本轮实际获得什么

- 直接阅读并截图核对了 Femme S. Gaastra (1997), *The Dutch East India Company: A Reluctant Discoverer*, *The Great Circle* 19(2), pp. 109–123，**印刷页112 Table 1**。此表是学者根据 Bruijn等 *Dutch-Asiatic Shipping* I:190 与 J. P. de Korte (1984) 的重建，**不是VOC原始账页**。URL：https://dutchaustralianculturalcentre.com.au/wp-content/uploads/2026/04/Gaastra-VOC-Australia-4155533235.pdf
- 逐行重录16个时期（1640—1795），将 equipage、回航货物进货票面价值、欧洲销售额存入 [voc_trade_decades_m1.csv](voc_trade_decades_m1.csv)，单位均为**百万名义荷兰盾**，末期1790—1795只有五年，不能作完整十年比较。
- 直接阅读并截图核对 Gaastra, *The Amsterdam Capital Market and the Dutch East India Company*, **印刷页108、111–112** 对公司债券与anticipation money/银行贷款/政府担保的描述。详见 [voc_credit_observations_m1.csv](voc_credit_observations_m1.csv)。URL：https://dwc.knaw.nl/DL/publications/PU00010584.pdf
- 荷兰国家档案馆 `1.04.02`历史背景及1992年英文导论已核对（属于**档案目录/重建叙述，不是原始VOC收支账本**）：https://www.nationaalarchief.nl/sites/default/files/afbeeldingen/toegangen/NL-HaNA_1.04.02_introduction-VOC.pdf
- 荷兰财政面板新线索：Huygens Instituut 的 **Provincial Finances of the Dutch Republic 1572–1795** 包含多个省份的税收、借款及支出。官方目录可读；旧数据接口返回403，**数据文件尚未取得，不得称已经完成省级年面板**：https://www.huygens.knaw.nl/en/resources/gewestelijke-financien-ten-tijde-van-de-republiek-der-verenigde-nederlanden-1572-1795-2/

## 2. 分期数据复算（Gaastra 1997 p.112 Table 1）

| 期间 | equipage | imports invoice | Europe sales | sales-equipage |
|---|---:|---:|---:|---:|
| 1640–1700（6行合计） | 465.7 | 207.0 | 576.8 | 111.1 |
| 1700–1795（10行合计） | 1607.7 | 679.9 | 1623.8 | 16.1 |
| 1770–1780 | 186.5 | 78.1 | 199.6 | +13.1 |
| 1780–1790 | 212.3 | 55.6 | 145.9 | -66.4 |

*以上金额均百万名义荷兰盾。差额 `Europe sales-equipage` **不是利润、现金流量表净额，也不是殖民帝国净收益**，因为地域、时间确认、存货、亚洲当地收支和融资等项目没有在该两个量之间完全配平。作者在印刷页111主动警示这一点。*

对1770–1780 vs 1780–1790：
- 欧洲销售额变化：`(145.9 / 199.6 - 1)*100 = -26.90%`；
- equipage变化：`(212.3 / 186.5 - 1)*100 = +13.83%`；
- 销售额/equipage：`1.0702 -> 0.6872`；**描述性比率，不是profit margin**；
- 英荷第四次战争1780–84与销售回款中断同窗，但十年累计数据无法将战争、竞争、价格和库存时间效应单独辨识，`CAUSAL_TEST_NOT_RUN`。

## 3. 重要数据冲突；不能静默修正旧M0

| 观察值 | Gaastra 1997 p112十年项加总 | 国家档案馆1992导论 | 状态 |
|---|---:|---:|---|
| 1640–1700 equipage | 465.7 | 370 | **SOURCE_CONFLICT_OPEN**（差95.7） |
| 1640–1700 imports invoice | 207.0 | 205 | SOURCE_CONFLICT_OPEN（差2.0） |
| 1640–1700 Europe sales | 576.8 | 577 | rounding compatible |
| 1700–1795 equipage | 1607.7 | 1608 | rounding compatible |
| 1700–1795 imports invoice | 679.9 | 667 | **SOURCE_CONFLICT_OPEN**（差12.9） |
| 1700–1795 Europe sales | 1623.8 | 1633 | **SOURCE_CONFLICT_OPEN**（差9.2） |

两个来源作者和二级引用均指向de Korte / Bruijn，**尚不能确定口径差异还是某个版本的转录/统计错误**。必须取得其原始表的表头、表注及统计边界再裁决；M0旧记录不擅自覆盖。
附带内部一致性警报：Gaastra同篇印刷页111的例子把1770–1780 equipage近似写作198百万，但其印刷页112表列 **186.5** 百万；198.9是**1760–1770**所在行。做数字分析应以明确表格行、注明该处文本不一致并向底层原始统计表追索。

## 4. VOC债务及1780冲击：不可混加的项目

| 时间 | 项目及金额（百万名义荷兰盾） | 会计约束 |
|---|---|---|
| 18世纪初至1780年前 | 约7.6：VOC bond loans | 债券余额近似水平，不是全部负债 |
| 1765 | 22：anticipation money峰值 | 拍卖预收融资，不是利润 |
| 1780 | 18：anticipation money余额，其中5.1来自阿姆斯特丹Wisselbank | 5.1属于18的**子集**，不能相加 |
| 1782 | 相关5.1银行债权由阿姆斯特丹市接管，预支款转化为有荷兰省支付担保的3%债券 | **同一债权的转移**而不是新增5.1 |
| 1796年3月 | VOC债务 **well over 100** | 数值为严格下界（本研究保守登记100），与早期债券科目不同 |

以上均来自Gaastra《Amsterdam Capital Market and the Dutch East India Company》印刷页107–112，URL https://dwc.knaw.nl/DL/publications/PU00010584.pdf；尚未回到de Korte 1984的原始年度账页，不能当作已完成逐年融资序列。省政府担保既不等于立刻现金支出，也不能自动并入中央国库债务。

## 5. 机制与反证（A—E五轨承接M0）

- **A 技术/组织**：VOC早期融资制度和跨洋商业能力确实强，但不自动导出煤—蒸汽工业领先；英荷相对能源价格需要独立面板。
- **B 殖民贸易/劳动**：本文件仅复核VOC欧洲—亚洲贸易，不代表WIC、奴隶贸易运输流量或殖民被统治人口；后续三张表必须严格分开。
- **C 军事**：1780–84第四次英荷战争令回航/拍卖显著中断，但1780–1790这一跨战时及战后十年口径不能是纯“战争处理组”；战前结构变动必须保留。
- **D 财政**：存在战前anticipation borrowing和1782债务支持链，证据强于只比较“公司亏损”，但年度VOC利润/现金/军费/国库支出尚未取得。
- **E 衰退/退出**：VOC公司法律终止不等于荷兰亚洲殖民统治当年退出，亦不等于荷兰国内总产出同幅度下降。

**H1 过度扩张**：若1780年前单位贸易收入对应的亚洲军政支出持续上升、且排除价格下降，可增强支持；若只在海上封锁后出现现金恶化，则H1并不充分。

**H2 短期流动性冲击**：若拍卖量、回航吨位和anticipation余额在1780–84出现同步断裂，且战前营运现金流已紧张，则战争可以是触发器而非长期停滞唯一原因。

**H3 市场竞争与产品结构变化**：如果咖啡/茶叶/棉织品毛利和出口品价格在战争前下降，即使军政费用未明显增长，仍可解释边际收益减弱。

**H4 治理与高分红**：需将股息、账面盈余、营运资本抽取、董事会政策分开检验，不能据董事动机的二手评论直接下结论。

**否证事件与反例**：1692–1702亚洲账务损失并未立即导致整个VOC公司破产；Gaastra 1997印刷页113明确指出当时亚洲亏损部分有过去账目调整因素，且来自欧洲销售的资金能维持集团流动性。故“亚洲亏损=必然破产”无效。

## 6. 下一项最小验收工作（M2）

1. 获取 de Korte (1984) `De jaarlijkse financiële verantwoording in de VOC` 表格原版（尤其Appendix 1、债务Table 4及1780–96账目），优先消除本文件3节的冲突。
2. 取得Huygens `Gewestelijke Financiën` **实际可下载**的荷兰省税收、军费与利息序列及附带解释，标注缺口（Gelderland等）及省级/Generaliteit边界。
3. 保留 1770–1790 的时间冲击检验和 VOC-EIC负例比较为 `DESIGN_ONLY`，直到得到一致的逐年观测再计算；不先运行伪事件研究。

## QA记录与边界

16行逐期CSV、加总及百分比在提交前经代码复算；已审阅相关PDF表格截图和档案导论相应页。原始VOC账册 `NOT_ACQUIRED`；Huygens在线原始数据库 `NOT_ACQUIRED`；历史学同行复核 `NOT_RUN`；因果检验 `NOT_RUN`。