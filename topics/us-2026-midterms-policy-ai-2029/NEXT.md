# TOPIC-011｜首轮研究执行队列（2026-11-14）

**首轮M0（优先，不预设结果）**
1. DATA-00 [#50](https://github.com/fweiger/AI_book/issues/50)：冻结截至2026-11-02 CBO、主要公司财报CAPEX指引和数据中心项目计划版本；为每条信息保存**最初公开日期、发布时点及修订**。本仓库目前仅有少量来源样例，还不是时间序列。
2. H01 [#42](https://github.com/fweiger/AI_book/issues/42)：用2025-26与历史分立政府建立制度基线；2027-01-03后才观察新国会实际立法。
3. H02 [#43](https://github.com/fweiger/AI_book/issues/43)：按财政年建立联邦非利息支出/收入/结构性初级余额口径，先找CBO预测与Treasury表。
4. H04 [#45](https://github.com/fweiger/AI_book/issues/45)：逐家保存MSFT、GOOGL、AMZN、META、ORCL等选前CAPEX指引及其财年；缺AI专属拆分则标NA。
5. H08 [#49](https://github.com/fweiger/AI_book/issues/49)：对H04寻找全球/利率/融资竞争解释和可比对照。

**第二波M1**：H03核州县/项目许可与实际投产；H05政策活动时间分布；H06议题/州和2028选举；H07预注册T+1/+5/+20市场异常收益和宏观控制。

**当前未完成**：无全量历史数据、无正式预测F-ID、无因果回归/真实统计结果；不可对外宣称完成实证。

## M0进展更新（2026-11-14）
**已完成**：从Treasury官方API抽取12个年度Oct财政数据、FY2026 CBO baseline surprise分解、5家科技公司选前投资承诺和可复算脚本：[本轮报告](reports/2026-11-14_m0_readout.md)。此处链接如从NEXT目录打开，文件位于`reports/`。
**下一具体任务**：H02从CBO2026-02年度基线提取非利息支出/税收分项且考虑2026-10支付时移；H04抓每家公司2027最新指引并按未来发布日期追加，不能重写选前记录。

## H03实际推进2026-11-14
- 先前未入库的**已生效州级规则**与PJM选前预测误差现在已记录：[H03报告](reports/2026-11-14_h03_policy_grid_baseline.md)。下一轮以实际地方项目许可/并网/完工日期建面板，不再用政策提案/总电网预测代替项目取消。
- **第一验证样本：Virginia**新建>=100MW、2026-07-01起受HB153影响的项目，对同PJM可比州县项目进行匹配（先查并行趋势），同时记录2027-01-03起联邦新国会的任何新增生效政策。
- **反证重点**：核查BAAJA后续是通过、搁置还是实质修改；若快审批与强付费同真，实际建设净效果未必为负。

## H03 PJM实际兑现率和版本修订已取得（2026-11-14）
2025分区Large Load Adjustment统计已证明：**预测与实际覆盖差异必须先清理**，DOM与其他区域显著分化。阅读[第二轮实证报告](reports/2026-11-14_h03_pjm_large_load_realization.md)。后续先拿`2026/27真实分区历史值 + firm/nonfirm项目状态 + 州县许可证时间`，尽量形成同一区域“政策暴露强度→项目兑现误差”的面板，再开始H03政治增量效应估计。

## PJM总峰值非政治修订对照（2026-11-14补充）
- [经济输入更新负对照](reports/2026-11-14_h03_pjm_july_2026_macro_negative_control.md)已核实：2026-07重新输入Moody经济预测使PJM 2027/28全系统夏峰参考值比1月上修593MW；这一选前更新不因2027新国会引发。后续要以**真正的政策生效事件+项目建设事实**区分普通预测修订。

## H03：下一步不是扩大申请量，而是从申请穿透到firm、accepted与realized
- [2026年秋季申请口径审计](reports/2026-11-14_h03_sep2026_pipeline_capacity_vs_demand.md)将CAPACITY、DEMAND、Firm合同、PJM最终采纳、真实投产拆成5阶段。DOM与AEP占2027折算需求约77.6%，优先寻找二者**有实际签约时间/ESA/CC、项目MW、计划/实际并网日期**的公开报告。
- 2027-01的正式PJM Load Forecast公布后，只有同项目/同定义/同目标年的需求才能计算F/D、A/D；必须和Exelon FERC表的数值差单独核对，不得把不同资料的差值当取消。

## H03下一轮：优先Firm合同同批项目与真实带电资料
[Dominion和AEP合同-运营对照报告](reports/2026-11-14_h03_firm_operating_reconciliation.md)显示：Dominion 2025新接入园区数和最终设计容量↓，但2026 ESA储备及High Load实际收入↑，并非同一观测对象的矛盾趋势。下一步获取2026年新增园区/项目实际带电日期、公司High Load计量MWh及2027同比、PJM正式接纳2027需求（同批/同公用事业）和ESA/LOA合同金额与原计划完工日期。当前仍不具备F→A→R项目级兑现率，不计算市场总体“批文通过率”。

## 下一轮H03真正可以取得的“项目级数据源”
- 优先核查Virginia SCC PUR-2026-00011下**匿名公开队列库**是否依2026-05-12 interim要求上线，字段最少EDC、县、申请时间戳、申请MW、队列阶段及项目延期说明；该要求目前是**修订提案的指令**，不是已验证上线。得到真实官方清单后按`source_file_hash+queue_timestamp+county+EDC+MW`检查匹配，不能假设官方已给稳定ID；歧义匹配不纳入前瞻推断。
- 对照2025-11-25已公布、2027-01-01生效GS-5的旧公告与2027-01-03新国会事件。2027首季新合同变化先区分州费率预期/生效、项目准备及联邦新法。
- 保持[真实交付MWh](data/h03_dominion_actual_delivered_mwh_2024_2026.csv)与[DC电力销售占比](data/h03_dominion_dc_sales_share_annual.csv)分表；寻找客户分类的**真实MWh**及同区域实际投产时间，不把高负荷收入美元或PJM预测MW直接替代。
- 完整新证据见[第五轮H03报告](reports/2026-11-14_h03_queue_tariff_physical_delivery.md)和[新脚本](analysis/recompute_h03_queue_and_physical.py)。
