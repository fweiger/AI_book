# TOPIC-011｜H03第六轮：SCC仍待决，但找到DC专属真实4GW峰值与PJM已批准的50MW登记机制（2026-11-14）

> **结论**：取得了2025年Dominion纯数据中心**实测同时峰值约4GW**、2026-01冻结的2027/28/29公司数据中心专属需求预测（4,933/5,448/5,980MW），以及2026-07-22约3.8GW数据中心负荷转移事件。它们比此前混合负荷数据更接近DC实体业务。弗吉尼亚SCC的具体队列审批 **截至10-23官方命令仍续审**；PJM由FERC批准的50MW登记已具法律基础但**公开端只保证区域汇总**，截至11-14仍未取得公开项目级队列。上述事件全部早于2027-01-03新国会履职；H03政治因果仍UNTESTED。

## 1. PUR-2026-00011 最新官方程序状态：2026-10-23 Continued，不是获批
- SCC 2026-10-23 [官方Order/Document No. 261060105](https://www.scc.virginia.gov/docketsearch/DOCS/8fc501%21.PDF)确切指出：FERC于10-09对PJM ER26-3515做部分接受/部分驳回，接受大型负荷定义与登记，驳回IRAS；SCC注意到联邦和州在电网与零售供电方面的权限边界，将其纳入案卷并以 **This matter is continued** 结束，**没有批准Dominion的拟议100MW队列规则**。
- 同案2026-05-12 [原始签章的Interim Order](https://www.scc.virginia.gov/docketsearch/DOCS/8c5b01%21.PDF)（Doc Control 260530154）要求修订规则、拟建匿名公开项目数据库并至少半年更新，字段EDC/县/时间/状态/MW。后续SCC10-23命令却将这份中间命令**回顾称为May 25**；两个**官方来源出现日期矛盾**。本研究保留这处冲突，以原始中间命令的实际签发和备案日2026-05-12为准，不编造第二份“May 25裁定”。
- SCC [公共案卷入口](https://www.scc.virginia.gov/case-information/) 仍可查公开文件，但未验证匿名数据库可供下载、稳定项目ID和真实阶段明细。外部案卷聚合索引将案件标为Active/Pending，最近文件10-23；此为二级印证，法律结论仍以10-23官方命令为准。
- **发电并网 Queue Status**不是本案用电大负荷队列：Dominion [Parallel Generation and Interconnection](https://www.dominionenergy.com/virginia/large-business-services/using-our-facilities/parallel-generation-and-interconnection)标记的Virginia Queue Status Report服务发电机并网，不可用其项目行数冒充70GW接入客户。
- SCC中间命令并不保证最终需公开**逐项目**客户信息，也不能把70GW申请的25GW已给预计日期写成完成率（上一轮明确35.714%仅排期覆盖）。

## 2. 真正的DC专属实测：Dominion已明确披露2025年峰值约4,000 MW
[Dominion 2026-01-06提交给PJM的三页原始信函](https://www.pjm.com/-/media/DotCom/planning/res-adeq/load-forecast/dominion-documentation.pdf)（可从[PJM Forecast Adjustment Documents官方目录](https://www.pjm.com/planning/resource-adequacy-planning/load-forecast-dev-process.aspx)链接取得，PJM页面2026-02-02）在**第1页**写明：
- Dominion为其**数据中心客户**自2013年起保存细致的电表数据，2025年的**DC coincident peak约4GW**；这是公司服务范围的实测同时峰值，**不是该年新增容量或全PJM负荷**。
- 公司使用7个最大/增长最快客户及剩下约45个客户的8个分组、每组3种模型共24个模型生成“High”，再用全行业4个候选模型择一“Low”，取二者均值成为提交给PJM的未来负荷预测。不是用47GW合同存量直接假设兑现。
- 该信函给2026—2046 **21个年度数据中心专属预测**，见[完整数值CSV](../data/h03_dominion_dc_only_physical_and_forecasts.csv)：
| 目标年 | 公司2026-01冻结DC同时峰值预测(MW) | 备注 |
|---|---:|---|
| 2025 | **约4,000 实际峰值** | 实测近似值；不是预测 |
| 2026 | 4,433 | 2026-01发布的外部预测 |
| 2027 | **4,933** | 将来用同范围DC实际峰值验证 |
| 2028 | **5,448** | 将来验证 |
| 2029 | **5,980** | 将来验证 |
| 2030 | 6,526 | 将来验证 |
| 2046 | 16,636 | 远期高度不确定 |

**预测 vs 实际禁止混算**：2025的4,000MW公司DC专属观察，不等于此前PJM 2025 DOM区`Historical July Peak Large Load Adjustment`约5,563MW（不同公用事业子区域/负荷类型），更不等于2026-09 PJM DOM总区域2027`DEMAND Requests` 8,441MW（目标年/时间/统计口径不同）。绝不拿这几组值互减生成“AI需求缩水比例”。

### 预测注册边界
原始机构信函**发行日2026-01-06**，本专题于**2026-11-14回溯归档**，已将独立21期外部预测放入专属CSV，**没有冒充本研究在2026-01就已预注册的预测F-ID**；`forecast_registry.csv`仍保留用户自己的未发布预测。未来每年评价必须从同公司同定义的DC同时峰值原始源检查实际。

## 3. Firm修正：ESA + CLOA 才是公司定义的Firm阶段
Dominion该原始信函**第2页**明确：
- ELOA工程授权有约25万美元工程保证金，平均研究9—12个月，**不是Firm**；公司称ELOA阶段未强制项目继续投资。
- CLOA对应建设成本承诺与保留容量，**公司将CLOA视为Firm**。
- ESA在正式供电和装电表之前必需，属于近期生效服务协议。
- **Firm≠已送电**；CLOA项目可能仍在建设，ESA含保留容量/合同服务条款。

[2025-12与2026-09同公司Q3报告](https://s2.q4cdn.com/510812146/files/content_files/2026-10-30-DE-IR-3Q-2026-earnings-call-slides-vTC.pdf)快照按其Firm定义可计算：

| 合同阶段 | 2025-12 (GW) | 2026-09 (GW) |
|---|---:|---:|
| ESA | 10.2 | 12.2 |
| CLOA | 11.0 | 9.8 |
| **Firm = ESA+CLOA** | **21.2** | **22.0** |
| 全阶段合同储备 | 48.5 | 54.9 |
| Firm占比 | **43.71%** | **40.07%** |

Firm绝对GW +0.8（+3.77%），但Firm占全部储备下降 **3.64个百分点**。这与“ESA独立增长19.6%”均真实但反映不同机制——**ESA在合同内上移、同时非Firm ELOA增加更快**。不能凭Firm占比下降推断真实项目取消，也不能当PJM区域与全部数据中心的批准率。2025-07历史公司信函另披露Firm 9.8+7.1=16.9GW/总47GW=35.96%，但由于发布日期不同，这仅供历史背景，不直接作为当时可交易PIT数据。
数据：[合同Firm阶段及发行时间](../data/h03_dominion_firm_capacity_stages_backtest.csv)。

## 4. 2026实际在役负荷的事件观察：2026-07-22约3800MW转移
[PJM于2026-08-11发布的事故审查](https://insidelines.pjm.com/pjm-dominion-review-large-load-transfer-event/)记录：2026-07-22当地时间早07:56左右北弗吉尼亚一条230kV线路故障，数据中心/计算型大负荷转移到现场备用发电，**约3,800MW**发生突发转移。
- PJM区域总负荷从**99,984MW→96,205MW**，净值下降**3,779MW**（接近PJM概述“约3,800MW”）；这是区域即时net drop，并非等量逐客户计量的DC负荷总体峰值。
- PJM回顾类似事件**2024-07-10、2025-02-17**每次约1500MW；三次是不同条件下的故障事件，不是可比较的DC用电增长曲线、数据中心项目数或投资回撤。
- 2026-07故障受影响规模约3.8GW，不能和2025整体DC peak4GW相除得到“2026已兑现95%”；时间、个体、事件时点和计量对象不同。

原始记录：[三次负荷转移事件](../data/h03_pjm_real_load_trip_events_2024_2026.csv)、[2026-07-22即时PJM系统净负荷差](../data/h03_pjm_2026_july_22_load_trip_balance.csv)。

## 5. 另一条数据路径：FERC已批准PJM的50MW Large Load Registry
- [FERC ER26-3515 2026-10-09命令](https://elibrary.ferc.gov/eLibrary/docinfo?accession_Number=20261009-3055)：大型负荷定义/登记制度接受，**IRAS方案被驳回**。
- PJM于2026-11-09提交[ER26-3515-002合规文件](https://www.pjm.com/pjmfiles/directory/etariff/FercDockets/9976/20261109-er26-3515-002.pdf)，要求追溯**2026-10-12**生效：Large Load≥50MW单电气站点，关联设施1英里内满足规定合并计算，与SCC拟议≥100MW DP Request不同。
- [PJM 11-09申报的RAA Schedule 11(B)(1)(e)](https://www.pjm.com/pjmfiles/directory/etariff/FercDockets/9976/20261109-er26-3515-002.pdf)：PJM网站仅在可能且符合保密要求时公开**Electric Distributor zone/area汇总**。客户、服务合同、负荷爬坡和送电日期属于PJM登记数据，但**未必开放个体级**。
- 对服务中或计划**在2027-06-01以前**投入服务的项目，相关主体**2027-03-01之前**向PJM提交；之后项目在送电前提交，变化要更新。**截止日期是向PJM报送，不等于公众届时能下载所有个体记录**。
- **核查现状**：PJM的[Large Load网站](https://www.pjm.com/markets-and-operations/large-load)在2026-11的网页正文仍标`Pending FERC Approval`，但FERC已10-09批准登记部分并且PJM11-09已提交合规文件。该站可能存在未更新文字；本研究以FERC监管文件为准，标记不同来源页面状态冲突。未核实PJM已经公开任何实际zone-level登记汇总CSV，不能把登记规则获批称为实际数据可下载。
- 两条并行的队列数据：**Virginia SCC 匿名DP队列**（若最终采纳且公布）可望有县/项目请求状态；**PJM FERC区域大型负荷Registry**公开部分可能仅有汇总，两者不应相加，也不能假设存在共同项目ID。

见[制度/发布/待办时间表](../data/h03_state_federal_large_load_registry_status.csv)、[原始来源差异](../data/h03_data_discrepancies_and_controls.csv)。

## 6. 具体可证伪的下一步
1. **优先历史预测检验**：2027、2028、2029 Dominion数据中心专属同时峰值实际值，如有与2026-01冻结公司预测同定义原始数据，则算`actual - forecast`；完全没有就保留NA。不能用PJM全区大型负荷实际替代。
2. **Firm结构研究**：按同一家公司定期锁定`ELOA, CLOA, ESA, total`不同报告版本，区分公司阶段份额变动与项目逐项取消。
3. **监管检查点**：SCC继续监控`PUR-2026-00011`明确最终命令和匿名队列真实URL；PJM核`2027-03-01`初始报送与后续区域汇总公开。若发现存在、先采集SHA和发布日期，再研究变动，严禁用“政策应发布”推断“数据已经发布”。
4. **归因边界**：这些2025—2026官方事实全部发生于2026中选前（SCC 10-23、FERC 10-09、PJM 11-09合规虽在选后但制度作出于选前）。若2027经济数据变化，仍要分清既有州/PJM监管、AI商业盈利能力、融资、天气和新国会真正新增政策。H03因果UNTESTED，路径P-B未知。

**本轮提交不是后验概率或政治看法**，而是可以复算的公司纯DC实际基线、发行人预测、事件级真实在役需求与两个登记制度的数据资格/发布时点。使用[离线复算](../analysis/recompute_h03_matured_dc_baseline.py)，所有同批项目`F→A→R`兑现率仍为NA。
