# CASE-FRA-001｜M2：1788年出口税地区汇总与外国供应依赖的跨来源核账（2026-11-14）

**权威 Issue** https://github.com/fweiger/AI_book/issues/35  
**原有 Draft PR** https://github.com/fweiger/AI_book/pull/39  
**资料** [regional_export_duties_1788_m2.csv](regional_export_duties_1788_m2.csv)、[foreign_goods_origin_1788_m2.csv](foreign_goods_origin_1788_m2.csv)、[secondary_trade_table_quality_m2.csv](secondary_trade_table_quality_m2.csv)。  
**结论类型**：新数据源定位、不同边界的数据勾稽及来源质量审计。**PDF原始页像截图请求失败**，数字层面为`SEARCH_ENGINE_PDF_TEXT_INDEXED`和`ARITHMETIC_PASS`，不能标记`ORIGINAL_TABLE_IMAGE_VERIFIED`。1788王室实际殖民税入库、国库净收入、汇票清偿、因果关系仍`NOT_ACQUIRED/NOT_RUN`。

## 一、1788年出口税的地区级二手整理，与官方国库表还差一步

Keith Anthony Manuel, *Slavery, Coffee, and Family in a Frontier Society: Jérémie and Its Hinterland 1780–1789*, University of Florida MA thesis 2005, **printed p.25, Table 2-4**，直接归引 Marbois 1790书内「État général des Cultures & Manufactures ... 1788–1789」；PDF https://ufdcimages.uflib.ufl.edu/UF/E0/01/16/50/00001/manuel_k.pdf。表内区域出口税按**千殖民地里弗尔**列示：

| 地区 | 对应原文数值（千殖民地里弗尔） | 占区域加总 |
|---|---:|---:|
| 北部 | 2,845 | 41.13% |
| 西部 | 3,043 | 43.99% |
| 南部 | 1,029 | 14.88% |
| **合计** | **6,917** | 100.00% |

整数加总 `2845+3043+1029=6917` 为 `ARITHMETIC_PASS`。论文同表给出货物净出口重量区域加总**240,852千磅**，它是**物量**而不是贸易金额。

此前我们独立保存 Marbois 1790 **N.º III** 1788当地`octroi`毛额 **6,924,167 l. 19s. 11d.**，与Manuel的6,917,000名义汇总差 **7,167 l.19s.11d.（按Marbois金额为分母约0.1035%）**。**这一差异不能直接解释为走私、失税、债务损失或稿件错录**：两书均源自Marbois资料，引用的具体统计表/科目不同，千位取整也不能自动说明全部差额。必须核对Marbois原书N.º III与「Cultures & Manufactures」表的图像、年份、地区和`droits`定义。原扫描来源：https://upload.wikimedia.org/wikipedia/commons/7/78/%C3%89tat_des_finances_de_Saint-Domingue%2C_-_contenant_le_r%C3%A9sum%C3%A9_des_recettes_%26_d%C3%A9penses_de_toutes_les_caisses_publiques%2C_depuis_le_1er._janvier_1788%2C_jusqu%27au_31_decembre_de_la_m%C3%AAm_%28IA_tatdesfinances01barb%29.pdf。

**特别的来源疑点：** Manuel表内Jérémie行的税额为**113（千殖民地里弗尔）**，但1790原版N.III verso「Récapitulation des denrées exportées」数字索引中Jérémie行显示**60,744 l.19s8d**。这是两张不同可能税基的表/后世取整，不是已证明的原书错误；保留为`OCR_OR_TAX_BASE_UNRESOLVED`，严禁替换为113,000或计算该港口“漏税额”。论文表格标题本身在PDF搜索抽取中存在列丢失，应等原页才升级列映射可信度。

## 二、1788年圣多明各「外商进口」的国别构成

P.-É. Herbin de Halle等编辑、1803–1804年出版的 ***Statistique générale et particulière de la France et de ses colonies*** 图表集内载「État des importations faites aux colonies françaises d'Amérique par le commerce étranger en 1788」。原始图表扫描的搜索结构化文本：https://upload.wikimedia.org/wikipedia/commons/f/fa/Statistique_g%C3%A9n%C3%A9rale_et_particuli%C3%A8re_de_la_France_et_de_ses_colonies_..._%28IA_b2201763x%29.pdf；1803年法文统计作品及1804年图表册背景见 https://www.napoleon.org/en/magazine/napoleonic-pleasures/the-statistics-of-napoleonic-france。

其 **Saint-Domingue** 行（**表内金额单位尚待原版页像确认，以下只沿用印刷数字单位，不擅换成1788地方里弗尔**）：

| 输入来源 | 表内列报数值 | 同一行占比 |
|---|---:|---:|
| États-Unis | 5,922,000 | 84.14% |
| Anglais | 69,000 | 0.98% |
| Espagnols | 673,000 | 9.56% |
| Portugais | 未列数字（破折号） | 不计入已报告分项的加总 |
| Danois | 37,000 | 0.53% |
| Hollandais | 333,000 | 4.73% |
| Suédois | 4,000 | 0.06% |
| **总计** | **7,038,000** | **100.00%** |

可见六个有金额的国别分项以整数精确加至原印刷**7,038,000**，且美国占**84.14%**。这是**在该回顾性编纂的外商输入表列报的Saint-Domingue这一行内部**，而不是“美国占殖民地全部进口84%”。法属本土贸易、奴隶贸易不同分类及走私/未报贸易可能不属于此分母。葡萄牙空白不是统计意义的绝对零。

Manuel Covo, *Entrepôt of Revolutions*, ch.2 (2022), https://academic.oup.com/book/44542/chapter-abstract/376575311 从现代跨帝国贸易研究强调1784–1788年美国向圣多明多供应基础资源的价值及走私/关税规避网络。这提供机制上的同向参考，**不是对这张1804年的统计表独立逐项复算**。

## 三、反例：统计汇编其他行有可见的内部不闭合

1900年前印刷的国别数据经当代扫描OCR抽取后出现：
- 瓜德罗普列出的分项逐格相加=3,444,000；所列总额3,424,000，差20,000；
- 多巴哥分项相加=2,122,000；所列总额2,127,000，差5,000；
- `Danois`列所见各岛合计=192,000，但末行标172,000，差20,000；
- `Hollandais`列所见各岛合计=1,450,000，但末行标1,455,000，差5,000。

**不能断言这些差额来自原书印刷，也不能断言来自OCR；需查看原扫描视觉图像，先前已尝试web PDF截图，失败。** 这意味着即使圣多明多单行加总准确，也不能认定全表每个地理/国家汇总都完全可信。完整异常列表见[数据质量清单](secondary_trade_table_quality_m2.csv)。

## 四、对法国殖民财政机制的新增限制

现有四类统计要分账：
1. **圣多明多地方出口税**（`octroi`，Marbois N.III，殖民地账）；
2. **分地区的出口商品物量与“customs duties”**（Manuel 二手整理、同一Marbois底稿）；
3. **外国商人向法属殖民地进口商品**（1804历史汇编，`commerçe étranger`）；
4. **法国本土从所有法属殖民地进口贸易金额**（TOFLIT18，源档AN F12 251）。

这四者方向、地域、会计主体、货币、贸易范围不同。**不能相除或相减去估计法国殖民地财政税率、王室国库税收留存率或法国商人利润率**。

当前仅可提出待检验假说：圣多明多经济扩张所依赖的投入与贸易利润可能有相当部分属于法国外部的美国等商人网络；殖民地的商业规模与巴黎国库可支配资源之间，需经过贸易税制和汇兑清算才可能连接。该假说需要独立美法船舶交易、商人账本及法国王室实际资金来源的原始记录支持，不能由84%推断经济因果贡献。

## 五、下一项实证行动

下一步首先取得 Marbois N.III verso 出口税「Récapitulation」及**《Statistique générale》1804外商进口表**的清晰印刷页，消除国别表内部列错位与地域不同定义；随后对照TOFLIT18原始地理伙伴项和 SHD MS338（1785外国商船记录）建同税种/同来源的贸易图谱。法国王室1788 `G¹46*` 和 `G¹44*` 真实收付仍未取得；结论不可升级为净财税收益或因果估计。

**状态：** M2 evidence extension；regional/row integer sums PASS；source table original visual `BLOCKED`；royal cash `NOT_ACQUIRED`；historical cause `NOT_RUN`。
