# CASE-NLD-001 | M2B 运输资金与历史会计单位核查 | 2026-11-14

**权威任务** [AI_book #33](https://github.com/fweiger/AI_book/issues/33)，沿用 [Draft PR #37](https://github.com/fweiger/AI_book/pull/37)。阶段 `M2_PARTIAL`，不是完整VOC财务结论。

## 一、为什么本轮需要单独验证现金的“指令”与“执行”

Arent Pol (1985), `Tot gerieff van India: Geldexport door de VOC en de muntproduktie in Nederland, 1720-1740`, *Jaarboek voor Munt- en Penningkunde* 72, printed pp. 65 onward; key appendix III printed pp. 140–146. 在线全文PDF：https://jaarboekvoormuntenpenningkunde.nl/jaarboek/1985/1985d.pdf

实际从原文PDF直接读取并核对了导论（p65–67）、附录III方法说明（pp139–143）、阿姆斯特丹商会的分年金额表（pp144–146）及总结（p121）。使用的是作者根据原始荷兰商会及亚洲账簿重建的**学术原始研究表**，并非本轮独立阅读了VOC原始手写账页。

作者指出：VOC董事会Heeren XVII的`toebedeling`是规定各商会应运送的资金分配量，而`verzonden`才是重建出的实际装船运送额。不能用决议记录替代单年实际现金运输。更不等于亚洲实收、贸易收入、净现金流或帝国税收。

### 经过PDF表格截图核对的阿姆斯特丹商会案例

| equipage会计年 | 董事会分配额 (f) | 实际运送 (f) | 报告差额(f) | 证明边界 |
|---|---:|---:|---:|---|
| 1720/21 | 2,000,000 | 2,000,000 | 0 | **总额相等但货币种类有变化**；印刷页144 |
| 1721/22 | 3,412,500 | 3,412,499 | -1 | 论文原表有1盾之差；印刷页144 |
| 1722/23 | 3,537,502 | 3,222,303 | -315,199 | -8.91% 的年度差额；印刷页145 |
| 1723/24 | 3,446,745 | >3,449,557 | >+2,812 | **明确下界**，不能当精确年观察；印刷页146 |
| 1724/25 | 3,709,500 | 3,726,131 | +16,631 | 组成货币部分含约数；印刷页146 |

所有金额为史料表中**阿姆斯特丹商会运出现金**的历史荷兰盾，不是整个VOC六个商会总额。可机读：[voc_amsterdam_specie_allocated_vs_shipped_m2b.csv](voc_amsterdam_specie_allocated_vs_shipped_m2b.csv)。四年数值为作者重建，不可错误解释为逐张原账单已独立复算。对1723/24保留下界符号，避免伪精确。

### 机制启示

- 1722/23年的数额差异 -315,199f / 3,537,502f = -8.91% 是**资金运送执行偏离**，不是VOC利润损失，也不等于货物运输被英国封锁造成的损失（该年距1780战争尚远）。
- Pol总结指出：在1720–1740约20年的总体水平上，各商会累计执行金额大致满足董事会的分配；**单年或币种组成偏差可能显著**。因此年度高频分析不能把董事会决议直接用作实际现金运送观测。
- 作者也解释部分出发船遇难、获救后又重运而重复入账、不同商会代运、绕开巴达维亚直航中国/锡兰/好望角等行为，会使商会账本、亚洲到账以及贸易货值产生跨账册口径差异。

## 二、货币换算与会计年度：本轮最重要的识别边界

根据Pol印刷pp140–142：
- 欧洲商会的`equipage`账务年通常为 **6月到次年5月**；巴达维亚亚洲账务年通常为 **9月1日到次年8月31日**。同一个标签年份的两套账并不自动同一现金流量期间。
- 亚洲收款有`zwaar geld`（重币，按作者说明与本土同数额）和`licht geld`（轻币，名义盾金额通常高25%）。例如同等基础币值可能出现`100本土/重币盾 = 125亚洲轻币盾`，**这是计价制度示意，不是任何一张VOC原始账页的直接发现**。
- 论文指出，某些实际账页对轻/重币的**文字标签也可能误写**，需要结合货币种类、枚数与稳定兑换比例复核。
- 数字落地时必须有字段：`cash_flow_event`, `book_owner`, `actual_or_instruction`, `currency_regime`, `account_year_start_month`, `account_year_end_month`, `originating_chamber`, `original_archive_inv_folio`, `missingness`。
- 即使原始 de Korte (1984) 附录到手也不能把亚洲轻币数直接并入荷兰本土盾的现金账。之前1640–1700 equipage **f370m vs f465.7m** 差异尚未查明；**两者比率接近1.25不是其由汇率造成的证明**，因为装备出支表具体账户主体和换算规则仍待查证。

## 三、原始档案的可核实定位，以及访问失败

荷兰国家档案（NA）`1.04.02`：“generale staat”汇总：
- `inv. 4596` 1771–1780（战前）；`inv. 4597` 1781–1790（战时/战后）；`inv. 4600` 1786–1796相关财务委员会决议。目录链接：https://www.nationaalarchief.nl/onderzoeken/archief/1.04.02/invnr/Deel%20I%7C%7CF.09?page=72
- 当前可在档案目录网页查询到 `DIGITALIZED` 状态；但点击4596、4597影像链接时均返回**HTTP 404**（`.../archievenoverzicht/1.04.02/invnr/@4596/file/NL-HaNA_1.04.02_4596_0001`及对应4597）。**所以账页数字`NOT_ACQUIRED`；不能因目录显示已数字化就写“原账已读取”**。
- `de Korte (1984) De jaarlijkse financiële verantwoording...`：本轮找到国家经济历史档案NEHA系列目录，列有1985版本和2000年英文版 *The Annual Accounting in the VOC Dutch East India Company*；没有取得两版完整可核算附录。资料目录：https://www.neha.nl/wp-content/uploads/2021/08/neha-reeksen.pdf ，仅书目级证据。

## 四、独立的早期财务对照与反例

Gelderblom、de Jong与Jonker（2012）工作论文 *The Formative Years of the Modern Corporation*：https://repub.eur.nl/pub/32952/ERS-2012-007-FA.pdf 。文献正文和附录以现存各商会账簿重建1602–1623年的融资，指出VOC在1604–1605年便用私人借款预先筹资，资本制度在成立后约20年中逐步形成。

因此：`借款融资`并非1780年突然出现，亦不构成VOC破产充分条件。1780年危机的识别需要关注**信用供给、船货中断与债务到期压力的共同变化**，并和早期正常融资时期比较。这篇2012工作论文不是de Korte 1984原始附录，也不是1780财务账簿。

## 五、当前研究判定

| 子目标 | 状态 |
|---|---|
| 1720—1725阿姆斯特丹商会指令/实际现金运送的5条来源量化观察 | `PASS_PARTIAL`（作者重建表截图复录、数值QA） |
| 1723/24严格下界处理 | `PASS`（不伪造准确值） |
| 1640—1700累计equipage f370m vs f465.7m | `OPEN_SOURCE_CONFLICT` |
| NA 4596/4597真实原始账页下载/复算 | `BLOCKED_HTTP_404` / `NOT_ACQUIRED` |
| de Korte 1984/2000完整会计附录 | `NOT_ACQUIRED` |
| 1780—1790 VOC年度净利润 / 借贷 / 国家财政挤出 | `NOT_RUN` |
| 独立历史学者审查 | `NOT_RUN` |

**唯一下一步**：打开NA`1.04.02/4596`和`4597`的可用原始影像或申请档案导出，分别记录1779与1781的财务委员会报表、预支款、未销商品、已发行债券和币种/期间，并审查de Korte原书的原始表注。在此之前只使用已复核的Pol商会现金样本建立`instruction->shipment`观测，不把它错配到1780战争回归。
