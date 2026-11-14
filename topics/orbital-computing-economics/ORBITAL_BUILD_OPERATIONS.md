# TOPIC-012｜双模块成本架构：发射运输 vs 在轨建设与运营（V0.1）

> 目标：分别检验 **运输至轨道的单位成本** 与 **算力基础设施在轨制造部署/运行的全生命周期成本**，最后归并到无重复计数的每有效GPU-hour/TCO。归属 [Issue #60](https://github.com/fweiger/AI_book/issues/60)。本页为模型/账本规格，**不是已取得的项目报价**。

## 1. 成本模块 A：发射与交付（Transport & Delivery）

```
A0 initial_launch_and_delivery =
  cost_launch_contracts
+ payload_integration / fairing-adapter
+ orbital_transfer / propellant / tug
+ deployment logistics / assembly mission transport
+ transport insurance / launch failure expected loss
A1 replacement_transport =
  replacement launches + transfer/deployment + insurance
A_total = A0 + PV(A1)
```

**输出**：`transport_USD_per_initial_kg`、`launches_to_operational`、`launches_per_year_required`、`transport_USD_per_delivered_MW`。目标轨道、价格时间、可用质量/体积/单体体积与装载率必须一致。

**视频作者输入的证据等级**：$130M当次成本、$20–30M回收情景、$40–85/kg未来极端成熟期皆是 `VIDEO_SCENARIO`；不能把$40–85/kg写为现价或独立实测。

## 2. 成本模块 B：在轨建造与运营（Build & Operate）

```
B0 initial_orbital_build =
  GPU_CPU_memory_storage
+ space_rated_buses / shielding / attitude / propulsion
+ PV_panels / batteries / distribution
+ radiators / heat-pipes / pumps / thermal structures
+ comms_ground_link / optical_inter-satellite_link
+ robotics_assembly_payloads / commissioning
+ space_qualification / engineering / integration
+ initial_ground_network_capex
B1 orbital_operations =
  monitoring / flight_software / spectrum / ground stations
+ networking / service support / deorbit / debris compliance
+ in_orbit_inspection / maintenance / servicing
+ replacement_hardware_manufacturing / failure_expected_losses
+ business_continuity / cybersecurity / insurance
B_total = B0 + PV(B1)
```

**防重复计数规则**：组装“服务运输费用”记 A，组装机器人和本体制造记 B；补发运费记 A1，补发设备的制造成本记 B1；资金成本与保险要么在现金流层统一处理，要么组件内分摊，**不得两处相加**。

**输出**：`B_build_USD_per_MW`、`B_operating_USD_per_year`、`hardware_replacement_cycle_years`、`power_availability`、`radiator_mass_per_MW`、`delivered_compute_h`。不因为光照免费就把光伏阵列、电池、散热、控制系统和退役成本设为0。

## 3. 对比：地面数据中心全生命周期成本
```
C_ground = IT_electronics + land_building + energy + PUE_cooling
         + cooling_equipment + networks + service_maint_replacement
         + insurance + decommissioning + financing
C_orbit = A_total + B_total + common_finance_adjustments
cost_orbit_per_effective_gpu_hour =
        discounted_costs(C_orbit) / discounted_service_hours_orbit
cost_ground_per_effective_gpu_hour =
        discounted_costs(C_ground) / discounted_service_hours_ground
```
“算力站每MW”必须明确是 **IT功率MW** 还是总电功率MW。分母GPU-hour须乘以在轨硬件数量、利用率、故障可用率、性能降级、通信等待、持续供电和实际寿命；不能把理论芯片峰值吞吐直接当服务价值。

## 4. 运输价格下降的全局上限
如果在一套模型中运输占总TCO比例为 `s`，即使将运输成本降低`r`比例，且其它项、需求与资产周转完全不变，总TCO降低幅度上限也仅 `s×r`；这**只是固定其它因素的比较静态**。

BCG 2026条件模型称发射约占轨道数据中心TCO的五分之一（`s≈0.2`），则即使运输成本下降90%，单独产生的总TCO静态下降约18%。这不等于现实总成本只会降18%，因为设备轻量化、寿命、失败率、产业规模也可同时变化；恰恰表明必须联合建模。

[BCG研究原文（2026-08-27）](https://www.bcg.com/publications/2026/space-based-data-centers-cost-outlook)给出20年轨道成本$660–750M/MW、地面$230–300M/MW（**模型假设**）。不能把它当真实商用轨道项目报价；更不能只把发射费砍到$40/kg就宣布整体成本平价。

## 5. 一项有边界的GW量级运力算例
BCG使用`1GW轨道算力在$1500/kg入轨单价下发射费约$30B`作为其**情景分析**，数学上隐含：
```
M_effective_assumed ≈ $30,000,000,000 / ($1,500/kg) = 20,000,000 kg = 20,000 t
M_per_MW = 20,000 kg/MW_IT  [if 1GW refers to 1000MW IT]
100t/发的理论最低发次 = ceil(20,000t / 100t) = 200发
200t/发的理论最低发次 = ceil(20,000t / 200t) = 100发
```
这些只是**反推该报告情景的隐含质量需求与运力下界**，不是真实已制造的GPU卫星质量；若考虑整流罩、轨道、姿态、物流与可靠性，实际可能更高。以视频$20–30M/发配100t/发，200发运输费仅算发射本身为$4–6B（情景乘法，未含设备、运维和其他运输费用）。其余成本不可能据此视为零。

## 6. 遵循用户要求的两模块判断标准
| 判定 | A：发射运输 | B：在轨建设运营 |
|---|---|---|
| 可证实的现实价格 | 航天公司公开合同/服务报价、适用轨道和构型 | 卫星制造与在轨服务合同，质量与单价 |
| 关键物理量 | 可用有效运力kg/发、体积、装载率、频率 | 计算功率、太阳翼/电池/散热质量、通信、寿命 |
| 风险 | 回收率、重飞周转天数、射场负荷、航天保险 | 辐射、失效、散热、升级迭代、碰撞/碎片/退役 |
| 必交付 | `$/operational_kg`、发次、补发需求 | `$/MW_IT`、`$/effective_GPU_h`、资产更换 |
| 不接受 | 用理论目标当实价、用内部边际成本当售价 | 把“阳光免费、太空空间免费、真空免费”误当基础设施零成本 |

## 2026-11-14 初次数量化结果（R1）

[首次可复算测算报告](R1_MASS_LAUNCH_COST_RESULTS_20261114.md) + [Python原型](model_v1/orbital_cost_model.py)：借用NASA公开小卫星光伏比功率与BCG情景散热面积，并把其他质量/电池/发射参数明确标为假设，得到100kW/1MW/10MW的初次入轨质量及运价敏感性。**A（首次运输）已完成情景重算；B（制造、GPU、散热系统制造报价、维护更换、资本成本）的真实金额尚未取得，不能宣称完成TCO或$/GPU-hour验收。**

按BCG情景固定不变的非运输TCO $560M/MW 与独立质量预算所得发射运费**不可直接叠加**，因为这来自两个不同模型口径；报告只比较成本空间及固定其他因素的算术边界。

## R2 年度现金流模型：B模块从公式进入可复算情景

已执行[R2报告](R2_BUILD_OPERATIONS_LIFECYCLE_20261114.md)、[Python模型](model_v1/lifecycle_cost_model.py)、[可追溯输入](model_v1/inputs_lifecycle.json)与[测试](model_v1/test_lifecycle_cost_model.py)，覆盖100kW/1MW、20年、5组运输费、6组设备/故障/可用率假设，共60个算例。**B采购和运营单价均为显式what-if假设，未获得供应商正式合同；不能宣称实际20年TCO已核实。**

核心新增：同时报告未折现20年费用、实质贴现现值及贴现服务GPU小时；不能混用。负数盈亏平衡运输价代表**即使运费为零也无法按同等有效算力实现平价**，不能被误读为真实可购负运价。

## 7. 验收与下一步
- R1A：针对同一轨道、同一车型，建立视频外部预测/企业官方承诺/合同价格三层参数的来源、发布日期及可交付kg，检查视频`2500/1083/200/40–85`各算式；**本次仅视频算术条件重算，采购价格未证实**。
- R1B：建立100kW与1MW分项质量与成本数据字典，按太阳翼、散热器、GPU、通信、屏蔽/结构、储能、寿命逐项记录观测/假设；**not_run**。
- R2：双账本合并成单一TCO，给出成本敏感性和地面标准化对比，保留未决假设；**not_run**。

**下一阶段唯一核心问题：** 哪个模块是对太空算力的真实约束：发射费用、系统质量、散热、寿命还是有效算力利用率？只有合并统一TCO后才能排序。