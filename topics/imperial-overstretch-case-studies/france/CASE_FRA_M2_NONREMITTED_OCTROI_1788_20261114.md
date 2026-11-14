# CASE-FRA-001｜M2：1788年 Marbois 第XI章已征未缴款与未耗用资金

**权威 Issue**：https://github.com/fweiger/AI_book/issues/35 · **现有 Draft PR**：https://github.com/fweiger/AI_book/pull/39

**本轮新发现（1790年原著第36页及N.º XI说明文字）**：Barbé de Marbois明确把截至1788年末未耗用的地方财政资金分为三类：地方金库现款、承包商预付款余额、地方出口税征收官已经收取但拖延缴入金库的款项。全文见[原书扫描PDF](https://upload.wikimedia.org/wikipedia/commons/7/78/%C3%89tat_des_finances_de_Saint-Domingue%2C_-_contenant_le_r%C3%A9sum%C3%A9_des_recettes_%26_d%C3%A9penses_de_toutes_les_caisses_publiques%2C_depuis_le_1er._janvier_1788%2C_jusqu%27au_31_decembre_de_la_m%C3%AAm_%28IA_tatdesfinances01barb%29.pdf)。本轮阅读的是该**原书的搜索引擎提取文本与结构化表格说明**，获取PDF本体和页面截图失败，**没有完成原书折叠表高清逐格视觉审核**。

## 1. 原币种（livres / sous / deniers）三项准确加总

| 年末项目 | livres | sous | deniers | 会计属性 |
|---|---:|---:|---:|---|
| 各金库现有资金 | 1,082,001 | 7 | 6 | 当地现金存量 |
| 承包商已预付但未耗用余款 | 604,502 | 18 | 2 | 预付/请求权，不是现金 |
| 出口税征收官已收但延迟缴库 | 429,374 | 17 | 8 | 收款员手中尚未缴库的税款 |
| **三者合计** | **2,115,879** | **3** | **4** | 混合资产，不是年度利润 |

计算规则：1 livre = 20 sous；1 sou = 12 deniers。三项换算成整数deniers后加总，严格等于原文的 `2,115,879 l 3s 4d`，验证 `ARITHMETIC_PASS`。相关[数据表](marbois_1788_unconsumed_funds_m2.csv)保留原小单位，不使用小数近似。

**重要机制：** 作者明确责备 `Receveurs de l'octroi` 迟延将所得税款交给 `trésor`。这直接支持**殖民地内部“征收→地方缴库”存在滞留**。作者没有在此证明这笔429,374 l17s8d原应直接交给**巴黎王室国库**，也未提供最终结清日期。不能从此推出法国中央财政同金额损失。

## 2. 与既有数据的冲突仍保留

- 旧[1790年N.XI表格OCR转录](saint_domingue_1788_caisse_m2.csv)记 `429,374 l12s8d`，本次原书**说明文字**记 `429,374 l17s8d`，相差 **5 sous**。原始表格图片没取得，不能覆盖旧记录或称哪一版原书排印错误。
- 各金库现金与本轮未缴octroi形式相加：`1,511,376 l5s2d`，对照1798年Laborie四基金期末结余 `1,511,376 l6s11d`，相差 **1 sou 9 deniers**。两组数字可能是类似的基金期末余额，但定义、账户集合及OCR仍有疑点；不可强行补平。
- 若把旧海军金库结余明细 `960,787 l16s8d` 与**本轮**429,374 l17s8d相加，得 `1,390,162 l14s4d`，比Laborie所列海军金库期末结余 `1,390,162 l16s4d` 少 **2 sous**。前轮“7苏”异常因此获得了具体OCR/分项验证方向，但**仍未消除**。

三笔余额之和是**现金+非现金预付+已征未缴款**，不等于“法王财政盈余2.115879m”；与1788年已征出口税毛额6.924m也不一定来自同一税务期间，不能擅算正式逾期率。

## 3. Proisy 1789账本获取进展（未读取数值）

- [Geneanet书籍馆藏](https://www.geneanet.org/bibliotheque-genealogie/doc/1651254/etat-des-finances-de-saint-domingue-contenant-le-resume-des-recettes-depenses-de-toutes-les-caisses-publiques-depuis-le-1er-janvier-1789-jusqu-au-31-decembre-de-la-meme-annee-par-m-le-chevalier-de-proisy-commissaire-de-la-marine-faisant-fonctione-d-intendant-des-isles-francoises-sous-le-vent)列出1790年Proisy编《1789年圣多明各财政报告》88张影像，但全文可能需订阅；
- [Gale缩微卷清单](https://assets.cengage.com/gale/psm/2033000R.pdf)列在Reel 199、Vol.755、Item 4，51页及12张图表；都是目录验证，不是1789年账表数据已获得。
- 2024年学术论文 [Kongomania and the Haitian Revolution](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/F7527BEF0462BEC2D7FD720B094B36FC/S0003161523000858a.pdf/kongomania_and_the_haitian_revolution.pdf)注释50称Proisy表10关于被奴役人口统计有排印/算术错误，作者做了修订；这是**针对表10的质量警示**，不能泛化为整本1789财政账的错误。

## 4. 验证状态与下一项唯一行动

- 原书**说明文字**三项金额、总额与整数算术：`PRIMARY_PRINT_INDEXED_TEXT_CROSSFOOT_PASS`；原PDF**高清表页图像**：`BLOCKED`。
- 旧N.XI小单位差额：`OPEN`；法国王室1788税收**实际入库**：`NOT_ACQUIRED`；汇票最终承兑与清算：`NOT_ACQUIRED`；完整财政净收益/因果推断：`NOT_RUN`。
- **唯一下一步**：取得1789年Port-au-Prince原刊或1790巴黎版N.XI折叠表的高清扫描，直接核对`429,374`税款及`960,787`现款的苏/德尼，按原表账户性质对齐1798年Laborie的结余。
