# TOPIC-011｜指标和公式口径 v0.1

| ID | 对应 | 可操作定义 | 来源/频率 | 限制 |
|---|---|---|---|---|
| I01 | H01 | 重大法案通过→签署/否决、关键票数、正式调查、停摆天数**分别计数** | Congress/White House 周月 | 不能把不同强度事件简单加总 |
| I02 | H02 | (同口径实际非利息联邦支出-冻结CBO预期)/冻结CBO预期 | Treasury/CBO 月财年 | 只是支出偏离，不是财政刺激总量 |
| I03 | H02 | -Δ(周期调整初级财政余额/GDP) | CBO/BEA 季年 | 必须处理周期、税收和估计修订 |
| I04 | H03 | 州/县已生效AI/数据中心监管覆盖的项目MW | 官方许可证 月 | 议案、草案不算执行 |
| I05 | H03 | 到原计划投产日仍延期项目MW / 到期项目MW | 项目数据库 季 | 分母必须固定，避免只选失败项目 |
| I06 | H03/H04 | 数据中心实际施工、投产MW；分名义/实际投资 | Census/企业 季 | 不等于AI专属投资 |
| I07 | H04 | Σ同一目标年度最新CAPEX指引与PIT冻结指引的差 / Σ冻结指引 | SEC/IR 季 | 财年和公司总CAPEX口径不一，缺值不得填0 |
| I08 | H04 | CAPEX同比增速与同比增速的变化分列 | SEC/IR 季 | 增长放缓≠投资总量下降 |
| I09 | H04/H08 | 云业务收入/AI负载、资金流、服务器利用率（如公开） | IR 季 | 定价变化影响收入的可比性 |
| I10 | H05 | 事前定义重大外交、关税、军务 vs 国内政策事件的**数量和比例** | White House/Federal Register 月 | 地缘危机混杂 |
| I11 | H06 | 政策受益州与2028选举竞争程度相关性 | FEC/国会 季 | 不能观察政治人物真实动机 |
| I12 | H07 | 政策事件T+1/T+5/T+20风险因子调整超额收益 | 合法市场数据 事件 | 公告时区/货币共同冲击 |
| I13 | H07/H08 | UST期限利差、信用利差、融资成本 | UST/FRED 日周 | 同时受到FOMC影响 |
| I14 | H08 | 美国政策高暴露项目与海外/低暴露项目的差异 | 项目与公司 季 | 先验证平行趋势/样本选择 |

**研究顺序：** 首先冻结数据定义与发布日，然后历史基线/对照，最后预注册方向/阈值和未来目标日期。当前没有运行任何历史统计检验；不要虚构显著性、胜率或Bayes后验。资产市场事件反应不等于真实AI投资下降，更不等于政治因果。

## H03新增可用的分层指标（候选，尚无项目级结果）
- `H03_PJM_TOTAL_PEAK_REVISION`：年度Y的本次PJM全区域夏季峰值预测MW减同年度上版预测MW；**这是总体负荷预测修订，含非数据中心因素**；数据见[h03 PJM CSV](data/h03_pjm_forecast_revisions_2026.csv)。
- `H03_VA_ELECTRICITY_TAX_EXPOSURE`：适用数据中心计税期内实际kWh×$0.011，不等于100MW选址门槛；目前只有9个**非真实项目的模型情景**。
- `H03_NEW_100MW_SITING_EXPOSURE`：是否2026-07-01后申请Virginia新的>=100MW需要本地选址审批项目；只有符合定义才处理；已获批扩建不大于额外100MW另行分类。
- `H03_REALIZED_DELAY_MW`：到原计划投产日却未投产MW/到期计划MW，需要项目独立记录。**当前UNKNOWN，不得填0或用PJM全区预测代替。**

## H03新基线指标：实际与预测的可比性
- `H03_PJM_2025_LARGE_LOAD_ERROR` = (同一分区2025年实际`Historical July Peak` - 2025版`Load Forecast July Peak`) / 2025版预测。只统计**双方都有报告的主要分区**；RTO和各DOM子区不再求和。
- `H03_MATCHED_FORECAST_COVERAGE` = 有历史实际的2025预测主要分区预测MW / RTO 2025全部预测MW；本轮7566/7735=97.815%。这是**预测量覆盖率，不是全部实际负荷覆盖率**。
- `H03_PJM_VINTAGE_REVISION` = 对同一个目标年Y，PJM 2026-01预测MW - 2025-01预测MW；必须分`Large Load Adjustment` vs 整体夏峰负荷，分预测版本和zone。
- `H03_REALIZED_LOAD_YOY` = 同一报告体系主要分区历史2025峰值相对2024实际峰值变化。统计只描述历史增长，**不能等于建设项目完成率**。
源指标和校验见[H03研究报告](reports/2026-11-14_h03_pjm_large_load_realization.md)。

- `H03_PJM_MACRO_ONLY_PEAK_REVISION`：同一规划年度`July 2026 informational summer coincident peak - January 2026 official summer coincident peak`，单位MW；严格标记**informational only、总峰值非数据中心、发生在选举前**。研究用途是宏观预测输入导致的普通版本修订对照，不是政策效果测量。

## H03新增四阶段项目兑现指标（截至2026-11-14）
- `C=SUBMITTED_CAPACITY_MW`：提交者容量口径；`D=SUBMITTED_DEMAND_MW`：经需求比率折算，不等于PJM准入。
- `D/C`：2027全区17462.7/30466.9 = 57.317%。这是模型/企业提交中的容量→需求比，不是审批率。
- `F/D`：具有ESA、CC等满足PJM firm条件的需求占提交需求比，当前**全国NA**；部分ODEC案例仅能描述承诺筛选机制。
- `A/D`：PJM同批、同指标、同目标年的最终接受负荷与申请比；2027正式forecast尚未发布，当前**NA**；不同资料版本和嵌入量不能直接除。
- `R/A`：同批最终接受的项目到目标日实际并网/使用电力占比；未有项目对应实际，当前**NA**。
- `ZONE_CONCENTRATION`：按**折算需求D**分区；2027DOM+AEP占77.611%，禁止与DOM子区叠加。

## H03新增Firm与实体业务的不同粒度指标
- `ESA_COMPANY_PIPELINE_SHARE`：同日同地区同公司ESA储备 / 所有阶段合同储备；Dominion 2026-09为12.2/54.9=**22.22%**，只是合同阶段占比，非PJM接纳或项目投产率。
- `NEW_CONNECTED_DC_CAMPUS_COUNT`：该年度新带电园区**数量**；`NEW_CAMPUS_ULTIMATE_MW`：那些园区的**未来设计总MW**，不是当年真实峰值用电。2024/25 Dominion园区数量15→11，设计容量977→744MW。
- `HIGH_LOAD_REVENUE_YOY`：同公司同类高负荷业务实际季度收入同比，包含非数据中心及电价/燃料因素，不用来推导真实DC MW。
- `AEP_2025_PJM_ESA_LOWER_BOUND`：对2025-09 PJM AEP特定近端需求队列，ESA **严格 >8600/11182=76.91%**；不是跨公司/跨年度对2026-10的成熟度估计。
- `PROJECT_FIRM_TO_ACTUAL_MW`：需要项目ID、ESA生效/初始计划日期、真实并网/实际计量与PJM最终接受相同批次。当前全域无法计算，应为NA。
- 可比性判断由[data/h03_maturity_scope_crosswalk.csv](data/h03_maturity_scope_crosswalk.csv)记录，禁止使用不同公司的全国合同、PJM未来单年申请、公司收入直接相除。

## H03队列成熟度、总实物电量与2027监管负对照（v0.1.7）
- `DOM_QUEUE_PROJECTED_DATE_COVERAGE`=已有预计接入日MW / 申请队列MW：2026-02披露的25,000/70,000≈**35.714%**。其中45GW的批次时间参考截至2025-12，因此只是近似队列成熟度，**不是Firm/批准/实际电量兑现率**。
- `DOM_PHYSICAL_DELIVERED_YOY`=同一Dominion Energy Virginia全区域同期间Electricity Delivered MWh同比：2025全年100.2/94.5−1=**+6.03%**、2026年前三季80.6/76.1−1=**+5.91%**、第三季度29.4/27−1=**+8.89%**，全是所有客户的真实电量，不是数据中心专属。
- `DOM_DC_SALES_SHARE`=数据中心占Virginia Power Electricity Sales的比例2024=26%、2025=28%，必须另保留该份额的分母原文；**尚未严格证明可与上面的全部Delivered直接相乘**。
- `H03_COOLING_DEGREE_DAYS_Q3`：Dominion 2026Q3 1313 vs2025Q3 1066（+23.17%），气象因素；不能因用电增长就说全来自AI建设。
- `GS5_BILLED_DEMAND_FLOOR_SCENARIO`：100MW合同而实际需求20MW，T&D最低可计费85MW、适用时Generation最低可计费60MW；**是费率计费基础而非实际用电MW，绝非收入美元**。生效2027-01-01，批准2025-11-25。
- `PJM_PROJECT_REALIZED_FROM_DATED_QUEUE`：必须匹配同一个申请/接入点的预计日期、实际带电、计量MWh。当前项目级数据库未定位，保持NA，不能由25/70推算。
