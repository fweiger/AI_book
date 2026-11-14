# TOPIC-011｜H03 第四轮：供电合同、园区接入与真实收入（2026-11-14）

> **实证等级**：原始公司文件与SEC/PJM报告的描述统计，未识别2027民主党新国会对数据中心项目的任何因果作用。合同管线、项目实际接入、营业收入必须独立计量。原始数据与复算见文末链接。

## A. Dominion：2026选举前 ELOA/CLOA/ESA 合同储备
根据 Dominion [2026年10月30日第三季投资者演示稿](https://s2.q4cdn.com/510812146/files/content_files/2026-10-30-DE-IR-3Q-2026-earnings-call-slides-vTC.pdf)，单位GW：

| 快照 | 总储备 | 工程阶段 ELOA | 建造阶段 CLOA | 供电协议 ESA | ESA/公司总储备 |
|---|---:|---:|---:|---:|---:|
| 2023-07 | 16.5 | 8.7 | 2.0 | 5.8 | 35.15% |
| 2025-12 | 48.5 | 27.4 | 11.0 | 10.2 | 21.03% |
| 2026-09 | 54.9 | 32.8 | 9.8 | 12.2 | 22.22% |

2025-12→2026-09，ESA +2.0GW（**+19.61%**），总储备 +6.4GW（**+13.20%**）。各阶段与公司总计有0.1GW内因原文取整导致的差异。ELOA、CLOA、ESA在费用和退出义务上不同，ESA通常更具经济约束力；但**12.2GW的ESA储备不是2026年真实已使用电力，也不是某2027 PJM项目队列的最终接受MW**。22.22%只是同家公司同一时间的合同成熟度结构，绝非建设兑现率。

## B. Dominion：现实新接入园区并不与所有指标同步
[Dominion 2026年proxy/公司文件](https://www.sec.gov/Archives/edgar/data/715957/000119312526115180/d-20260319.htm)披露：2024新接入数据中心园区**15个**、这些园区最终规划容量**977MW**；2025新接入**11个**、该批最终规划容量**744MW**。同比新增园区数**-26.67%**、新园区最终规划容量总计**-23.85%**。**“最终规划容量”不是当年峰值计量实际用电，不意味着整个存量DC需求同比萎缩。**

[2025年公司10-K](https://www.sec.gov/Archives/edgar/data/715957/000119312526063120/d-20251231.htm)同时指出，数据中心贡献的 Virginia Power 电力销售比例2024约26%、2025约28%（+2个百分点）。可以出现“当年新接入园区数下降、存量数据中心销售占比上升”的组合：存量爬坡、不同园区规模、输电并网排期、客户负荷率都可能造成偏差；尚不能把差异归因为2026年选举后政策。

## C. 2026年高负荷客户实际收入在上升
Dominion SEC官方10-Q 中 `Regulated electric sales - High load` 的季度收入，单位百万美元：

| 季度 | 2025 | 2026 | 同比 |
|---|---:|---:|---:|
| Q1 | 383 | 636 | +66.06% |
| Q2 | 422 | 814 | +92.89% |
| Q3 | 503 | 706 | +40.36% |
| **前三季度** | **1,308** | **2,156** | **+64.83%** |

原始来源：[Q1 SEC](https://www.sec.gov/Archives/edgar/data/715957/000119312526200275/R16.htm) / [Q2 SEC](https://www.sec.gov/Archives/edgar/data/715957/000119312526327487/R36.htm) / [Q3 SEC](https://www.sec.gov/Archives/edgar/data/715957/000119312526440697/R16.htm)。**High load包括部分非数据中心客户**，且收入受电价、燃料调价、分摊政策影响。+64.83%是*收入*而非用电MWh或真实数据中心MW增长。

## D. AEP：2025 PJM签约与2026全国储备不能放入同一分母
[PJM官方AEP 2025年提交材料](https://www.pjm.com/-/media/DotCom/planning/res-adeq/load-forecast/aep-documentation.pdf)：当时面向2026–2030年、AEP在PJM运营范围申报的新增大负荷11,182MW，其中**超过8,600MW**已经签署 ESA，故占这份**特定同批**申报的比例严格高于**76.91%**。其他项目处于LOA或ESA谈判。这个数字不是整个AEP当前 ESA成熟度，也不是正式PJM审核通过率。

AEP [2026-10-28第三季度公告](https://www.aep.com/news/stories/view/12347/)称当季新增15GW签约，所有服务区域合计到2031年84GW已签约**ESA或LOA**。这些包括Texas/ ERCOT，**不能拿84GW与2026年PJM AEP 2027年提交需求5112MW相比，算“百分之一千多的项目兑现率”**。其[第三季SEC 10-Q](https://www.sec.gov/Archives/edgar/data/73986/000000490426000072/aep-20260930.htm)还记录AEP Texas/ERCOT约49GW LOA及当年8月Batch Zero负荷研究和上电流程暂停：大合同与实体上电可以显著脱节，该事发生于2026中期选举前，也不能推出2027国会政策效果。

## E. H03下一阶段真正需要的数据
按单个项目/同一目标队列：`company,service_territory,project_id,location,application_date,planning_MW,ESA_or_LOA_date,firm_MW,accepted_by_PJM_MW,planned_energization_date,actual_energization_date,metered_MWh,policy_exposure_start,original_source`。
只有同一批次才可计算`Firm / Demand`、`Accepted / Firm`、`Realized / Accepted`。公司总储备、近端区域申请、已新接入园区的最终容量和High load收入不是可互除的相同分母。

**本轮结论**：已确认选前公司高约束力ESA储备↑、高负荷收入↑，但2025新增园区接入数及其规划容量较2024↓。这些并非逻辑矛盾；它们反映不同层级。H03的2027–2029“政治→AI建设延迟”仍为 **UNTESTED**。
