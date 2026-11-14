# CASE-FRA-001｜M2：1789—1790殖民地财政控制权、专款约束与政治指控的来源审查

**权威Issue：** https://github.com/fweiger/AI_book/issues/35  
**现有Draft PR：** https://github.com/fweiger/AI_book/pull/39  
**范围：** 该专题不是法国中央王室实收税额的替代品，而是对财政转换效率研究补充两种可能机制——**谁对殖民地税收具有实际支配权**和**哪些资金受到用途约束**。

## 一、1789年9月21日地方省议会文件中的跨海资金转移指控

美国马里兰大学 *A Colony in Crisis* 项目整理的1789年北部省议会 *Arrêt ... contre Barbé de Marbois*，英译及编目：https://colonyincrisis.lib.umd.edu/1789/09/21/judgment-of-the-northern-provincial-assembly-of-saint-domingue-session-in-le-cap-against-barbe-de-marbois-his-council-accomplices-and-followers-september-21-1789/。

该文件控诉Marbois曾把**超过二百万的殖民地钱款送往法国，以支持其信用活动**，并涉及地方教区款项、贸易和粮食管理争端。法语原文字形为 **« plus de deux millions d’argent de cette Colonie »**（法文转录见https://fr.wikisource.org/wiki/Page:Arr%C3%AAt_de_l%27Assembl%C3%A9e_provinciale_de_la_Partie_du_Nord_de_Saint-Domingue_s%C3%A9ant_au_cap%2C_contre_Barb%C3%A9_de_Marbois%2C_ses_conseils%2C_complices_%26_adh%C3%A9rens._En_date_du_21_Septembre_1789_.djvu/6）。**没有给出明确已确认的货币单位，不能写成200万枚银币或直接认作200万法国本土里弗尔。**

**史料类型：** `CONTEMPORARY_POLITICAL_CHARGE_PRIMARY_TEXT`，并不是银行汇款凭证、经过审计的国库账户或证明指控真实的独立法庭裁判。议会判决/宣示发生于当时激烈的殖民地政治冲突，需用相反立场的材料和真实汇票登记证明。**本轮没有证明发生过该笔跨洋转账。**

**日期异常（不能忽视）**：原文件标题与BnF的目录称 **1789-09-21**（BnF馆藏目录：https://gallica.bnf.fr/selections/fr/html/bibliotheque-de-moreau-de-saint-mery），马里兰大学网页英译末尾却出现 **1789-08-21**；后者可能属于翻译或编辑笔误，也可能涉及不同签发日，但在检查原始页末之前，保留 `HEADER_FOOTER_DATE_CONFLICT`，使用9月21日作为标题日期而不默认为原正文签发日也相同。

## 二、1789年3月29日官方通信：国家法令与地方贸易自主权冲突

马里兰大学的原文件英译：https://colonyincrisis.lib.umd.edu/1789/03/29/letters-between-chilleau-and-marbois/。总督Marquis du Chilleau针对粮食短缺，提出开放殖民地港口进口外粮，要求相应通知港务人员，并使用王室储备粮平抑价格。财政长官Marbois回信指出，此举可能与法国专有贸易法规（Exclusive）和皇家部长指示冲突，不能简单用一封信改变殖民贸易制度。

它能说明当时法国本土贸易限制与殖民地粮食供给、地方行政自主决策之间存在**真实的官方分歧**，但这封信不提供殖民地税收实际净汇往巴黎的金额，也不证实有地方财政舞弊。

## 三、1790年Marbois本人的公开答辩：必须建立竞争叙事

[1790年Marbois对粮食商业利益指控的申辩](https://colonyincrisis.lib.umd.edu/1790/02/12/charges-of-fraud-the-obstinate-rebuttal-of-a-banished-intendant-concerning-the-grain-shortage-and-criminal-negligence/)经马里兰大学刊载为1789—1790年当事人一手文本的现代英译。Marbois否认曾通过岳父在费城屯粮来牟利，并引用个人书信进行答辩。这是**利益相关者自辩**，本身也不是独立事实审计。

**关键证据限度：** 该公开转录只针对粮食贸易牟利相关的一项控诉。它**不能被误用为已经逐项驳斥或确认1789年地方议会所指控的“超过二百万资金转法国”**。两种指控需分别查付款记录、民事刑事文书与不同当事人证词。

## 四、1790年圣马克议会与Proisy的20万里弗尔/月争议（后期史著）

[后期《Histoire des révolutions d'Haïti》在p.140–141的文字转录](https://www.scribd.com/document/767084430/histoiredesrvo00sain)称圣马克议会要求临时财政主管Proisy**每月拨出200,000里弗尔作为议员补助/费用**，Proisy以殖民地税收已有特定用途为由拒绝，议会据称曾试图禁止征收官向太子港总司库缴款，但最终没有执行。

**核验等级：** `RETROSPECTIVE_HISTORICAL_ACCOUNT / ORIGINAL_RESOLUTION_NOT_ACQUIRED`。不把200,000里弗尔/月记为实际付款，也不把形式年化2,400,000里弗尔当已执行年度支出；作者、版本、页码仍需进一步独立书目核验。

**机制含义：** 在控制同一笔税收的过程中，(i)国王任命的官员、(ii)本地议会/种植园精英、(iii)征税官及当地金库、(iv)法国本土财政机构有可能提出竞争性的调拨请求；专款约束不等于资金不存在，也不等于王室已到账。

## 五、必须区分的四种证据

| 证据标签 | 可以支持 | 不能支持 |
|---|---|---|
| `PRIMARY_POLITICAL_CHARGE` | 特定时期有人提出某项指控 | 被指控的汇款实际发生、属于国库损失 |
| `PRIMARY_INTEROFFICE_LETTER` | 官方人员对外粮进口政策存在争议 | 真实粮食供应量、税收净汇或指控真实性 |
| `PRIMARY_SELF_DEFENSE` | 当事人公开陈述反对解释 | 其说法已独立证实、全部财政控诉已被反驳 |
| `LATER_HISTORICAL_SYNTHESIS` | 后世史家记述特定预算拨款冲突 | 1790年实际财政支付、原件真实日期 |

这一层与既有的[1788地方出口税已征未缴及金库余额](CASE_FRA_M2_NONREMITTED_OCTROI_1788_20261114.md)互补，但**不能将政治冲突金额与前轮的429,374里弗尔已征未缴税款相加或做单年负债比率**。

## 六、对原命题的竞争假说和验证关卡

- **H-A：流动性/追偿摩擦。** 需要征收官实际缴库日、应收/预付及金库现金余额序列。当前有1788截面，因果证据不足。
- **H-B：政治预算支配冲突。** 需要1790圣马克决议、Proisy原始答复、王室财政官员的法定权限、各项税收指定用途以及实际执行流水。当前只有后期史书摘要和1789互相争执的政治文书。
- **H-C：财政挪用及跨海转移。** 需要1789相关指控的原始法国/殖民地汇票、银行结算和个人账目及议会法律程序；当前**仅有指控，真实性未知**。
- **H-D：专有贸易与粮食供给成本。** 需要运粮量、市场价格、开放港口政策的执行证据，以及因粮食供应短缺导致的财政影响；目前仅有争论与制度约束的直接文书。
- **H-E：奴役人口的独立政治主体性。** 不可将种植园主的财政诉求当成整个殖民地人民的代表性意见。海地革命、争取自由与废奴运动不是财政调拨争议的附属变量。

## 七、阶段状态及唯一下一项动作

新增可核查研究记录：[political_fiscal_claims_1789_1790_m2.csv](political_fiscal_claims_1789_1790_m2.csv)，登记**不同当事人的直接文书/历史摘要、是否有真正资金流水证据和反证需求**；[political_fiscal_sources_m2.csv](political_fiscal_sources_m2.csv)登记5项来源及接触层级。

- 原始历史指控与官方通信：`PRIMARY_TEXT_AVAILABLE`（部分为现代英译或法语OCR），**不是原账复核**；
- 1790年20万/月及征款拒付：`RETROSPECTIVE_ONLY`，未获得原始拨付令或凭证；
- 1788年原账折叠表高清视觉校验：`BLOCKED`；1789 Proisy原始全年收支未取得；
- 1788 France G¹46*实际王室到款：`NOT_ACQUIRED`；历史因果模型`NOT_RUN`。

**下一步只优先获取1790年圣马克议会拨款令和Proisy的同期书面回复、1789年“二百万”控诉的对应资金账与Marbois对该具体财务指控的答辩页，再与既有G¹46*/44*财政账簿对手记录连接。不要因政治指控或后世史家叙述，就宣称殖民地财政净输送失败。**

## 八、已定位财政管理者Wante的连续同期答辩

见[1790原刊与1789预算档案链](CASE_FRA_M2_DIRECT_REBUTTALS_AND_1789_BUDGET_ARCHIVES_20261114.md)。BnF现确认Wante本人1790年1月9日第二次答辩（25页）及第三次答辩（45页，2月13日或经手改为3月13日），并录有首次财政答复所附的1789年**预计**开支摘要。SHD另收MS142第99件1789预算原表，两处是否同源待查；未读具体答辩正文，不能声称已证实或驳斥1789跨海转款指控。SHD MS338的1785外国船税收和MS353的私人商业信用信件可用于后续私人/国家财政分账，但不代表现已获得金额。
