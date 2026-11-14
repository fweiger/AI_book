# CASE-FRA-001｜M2：1788年法国本土殖民税与海军汇票的原始档案路线（2026-11-14）

**权威研究任务：** https://github.com/fweiger/AI_book/issues/35  
**现有 Draft PR：** https://github.com/fweiger/AI_book/pull/39  
**任务阶段：** M2 原始账簿定位及跨洋支付机制复核；**未**取得法国王室1788年实际殖民税入库总额、**未**取得1788圣多明各105.31万里弗尔汇票实际兑现凭证。不是净帝国收益估计。

## 一、最重要的增量：法国国家档案馆已将1788年相关收支日记账正式编目

法国国家档案馆《Inventaire des sous-séries G1 à G6》（1894初编/1967复核/1999打字增补）明确记录：
- **AN G¹ 46\***：1788年总收款人关于 *traites, domaine d’Occident, huiles et savons* 的 **recettes et dépenses** 日记账，目录印刷第**19页**。这不是全部王室收入或全殖民税票据簿，而是包含多类税收的税务总收款人账簿；提取时必须逐项识别税种、征收区域、现金/转账性质。
- **AN G¹ 44\***：Ferme générale 总收款人 Foacier 的 1788 年收支日记账（账本后来记至1794），目录第19页。适合与G¹46*核对总账入账/转账，不得预设它必然含Saint-Domingue全部款项。
- **AN G¹ 84**：Domaine d’Occident相关的法令、备忘录、合同，并含**1787—1788年马提尼克、圣卢西亚和多巴哥**的税收产品卡（目录第31页），**不是圣多明各1788出口税总账**。
- **AN G¹ 61**：1788年包税机构支付凭证与其他财政义务（目录第23页）；可能有清算线索，但未验证其能关联至殖民税。
- **AN G¹ 80 dossier 26**：贸易及税收各方向的地方产品表，研究者在Languedoc专题将其用于1788年其他间接税收的逐口岸明细；不能认定其就是Saint-Domingue原账。

档案目录：https://www.archivesnationales.culture.gouv.fr/chan/chan/fonds/EGF/SA/InvSAPDF/G1_G6_rep.pdf 。本轮完成的是**官方档案目录核查**，并非实际翻阅相关 G¹ 原始账簿。已尝试web PDF页面截图，但截图访问失败；**不声称视觉扫描通过**。来源等级：`OFFICIAL_ARCHIVAL_INVENTORY_VERIFIED / ORIGINAL_LEDGER_NOT_ACQUIRED`。

### 为什么这条线索重要

上一阶段已建立 **圣多明各1788年 local octroi毛净 → Caisse de la Marine普通收入** 的精确算术桥，[见原报告](CASE_FRA_M2_TAX_TO_LOCAL_TREASURY_BRIDGE_20261114.md)。但 **local octroi** 与法国本土的 **Domaine d’Occident** 是不同税目/征收环节。只有把 **1788年港口征收者 → Domaine d’Occident会计 → Ferme générale汇总账 → 王室国库实际收付** 的对应条目依次找到，才能在同年月且同币种基础上判断中央财政取得多少。

**G¹ 46*中的“收款”也不等于王室Trésor royal已实际入库；仍需王室最终收款凭证。**

## 二、行政组织：为何海关与殖民税不能直接相加

Marie-Laure Legay 的 *Dictionnaire numérique de la Ferme générale* 「Colonies」专题说明：18世纪末 **Domaine d’Occident** 在法国本土约有24个征收办事处，港口记录上报后由巴黎的西印度领地税办公室编制总账；此税与其它 `traites` 海关系统虽有关联，却保持机构与制度区别（来源 https://fermege.meshs.fr/notice/198）。

同一研究项目关于Languedoc的专题记载，**1787年Sète口岸的Domaine d’Occident税收入13,248 livres tournois**（来源 https://fermege.meshs.fr/notice/237）。它是一项具有来源的 **单口岸单年历史研究重建数值**，不是1787年法国全部殖民税、更不是1788年巴黎实际入库，也不能与Saint-Domingue 1788年octroi相比而称效率差异。原始地方账簿尚未取得，定量状态 `PUBLISHED_SCHOLARLY_FIGURE_ORIGINAL_REGISTER_NOT_READ`。

## 三、汇票的跨区域融资机制：已取得可验证的比较案例，但不是圣多明各本地实测

Juliette Françoise, “Monnaie, dette publique et comptabilité : Les circuits financiers entre les îles de France et de Bourbon et la métropole au regard de la comptabilité de la Marine et des Colonies 1769–1783”, *Comptabilités* 14 (2021), https://journals.openedition.org/comptabilites/pdf/4937 。

该文利用**毛里求斯/留尼汪（Mascareignes）而非圣多明各**的18世纪档案，分析海军与殖民地政府如何借助 `lettres de change/rescriptions` 实施跨洋延期付款及其信用约束。具体机制包括：
- 对汇票赋予编号、记载具体支出用途，并把票据连同用途证明送到法国本土登记（文中PDF第8–9页）；
- 当地行政每月向巴黎海军总司库发送分类清单，以预测将到期的应付款项；
- 汇票可能按三个月或六个月期限支付，债务集中到期时对海军现金流产生流动性压力（PDF第9–10页）；
- 作者明确区分汇票**签发、提交登记、应付及实际清偿**。其引用的原始档案包括 `AN F/4/1008`（1770–1776年法兰西岛/波旁岛汇票与海军部通信）、`ADR/19C` (1776–1783年汇票及登记清单)，以及 `ADR/22C`。

**严格限制：** 以上事实直接证明的是1770年代印度洋殖民地的海军支付机制，不能直接证明Saint-Domingue 1788年那笔 **1,053,105 l.10s.4d** 已被巴黎承兑、已于何时支付、到期为几个月、支付给谁或造成何种财政挤出。该金额在[1788原金库账](CASE_FRA_M2_TAX_TO_LOCAL_TREASURY_BRIDGE_20261114.md)是非常收入的组成，已计入总额，不能重复加上。

可据此为1788年圣多明多汇票创建的**待验证字段**：`issue_date`, `drawee`, `payee`, `issue_location`, `underlying_expenditure`, `nominal_amount`, `currency`, `registration_date`, `maturity_date`, `acceptance_date`, `actual_payment_date`, `payment_location`, `cash_or_offset`, `duplicate_in_extraordinary_income`。没有原件，所有Saint-Domingue个别字段均为`NOT_ACQUIRED`。

另一个重要限制：AN F/4/1008/ADR 19C直接提供的是**印度洋比较组**，不能伪装为Saint-Domingue 1788年账目凭据。

## 四、与法国王室财政的下一阶段核账流程

| 核账阶段 | 源档案优先序 | 必需字段 | 当前状态 |
|---|---|---|---|
| A：圣多明多出口税/地方海军金库 | Marbois 1790 N.º III/XI | 地方税、费用、金库入账、期初结转、票据项目 | 文字复算PASS；扫描图像BLOCKED |
| B：法国本土西印度领地税征收 | **AN G¹ 46***；G¹ 84 | 港口、税目、会计期、应征、已征、退税、入账 | `OFFICIAL_INVENTORY_ONLY` |
| C：包税机构汇总和现金结算 | **AN G¹ 44***；G¹ 61 | 汇总资金、支付、调拨、欠款、对手账 | `OFFICIAL_INVENTORY_ONLY` |
| D：王室国库实际入库 | 待定位1788 Trésor royal实际账户 | 到账日、币种、对手方、净额与冲销 | `NOT_ACQUIRED` |
| E：海军汇票清算 | Saint-Domingue 1788原票据/巴黎海军总司库账 | 签发、承兑、期限、付款、实际资金方向 | `NOT_ACQUIRED` |
| F：可归属殖民维持成本 | 海军港口、军费与殖民开支分账 | 普通、战争、共同成本与分摊依据 | `NOT_ACQUIRED` |

在未获得 **B–F** 的实际原始数字之前，**不执行“贸易值 × 税率 = 王室净收入”，不发布帝国财政净收益、税收效率时间序列或战争因果挤出统计**。

## 五、研究交接与可证伪性

- 如果G¹46*与王室实际入库凭证显示征税到账、中央清算稳定，则“地方财富无法转化中央收入”不成立或至少需要大幅限缩。
- 如果出现大额被包税环节留存、地区抵扣、退税、未清汇票或时滞，则需要估算具体金额和与海外军事成本同期的关系；单凭机构存在不可宣称“财政传导失灵”。
- 海地革命及受奴役者反抗仍是独立政治机制，不能由税收链单因替代解释。

**下一项唯一工作：** 从国家档案馆取得 **G¹ 46*** 1788账页及 **G¹ 44*** 同年对手账，定位 `Domaine d’Occident` 收付、期末欠款与流向；如资料不开放则按档号向档案馆申请扫描/阅览，再联系Marbois 1790原报告核查1788地方税汇票。原件未取得记为 `NOT_ACQUIRED`，而非虚构数值。
