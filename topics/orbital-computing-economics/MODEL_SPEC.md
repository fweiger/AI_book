# TOPIC-012｜统一物理与经济模型规范（V0.1）

> 这是**可计算规格**而非运行结果。当前 `run_status=NOT_RUN`。任何后续研究必须提交来源参数、计算脚本、单元检查和可复算输出，禁止将文中变量和例子称为既成结果。

## 1. 共同边界与结果变量
- 系统 A：在轨运算、在轨太阳能、在轨散热；B：太空光伏向地面送电；C：在轨处理太空原生数据。模型分别运行，不跨架构混用能源/通信/成本。
- 功率：`P_IT_W` 为处理器、存储、网络的有效IT负荷；`P_bus_W` 为非IT负荷；`P_gen_W`为太阳阵列瞬时电输出；`P_waste_W`为待排净热功率。用 `W/kW/MW/GW` 明确换算。
- 计算结果：`usable_GPU_h`、`effective_training_tokens`、`inference_tokens`、`remote_sensing_data_delivered` 在不同工作负载下分别跟踪，绝不只靠峰值TFLOPS声称效能。
- 经济指标：`TCO_10y`/`TCO_20y`、`$/MW_IT`、`$/usable_GPU_h`、($/delivered_result)；价格时间、名义/实际、贴现率都要统一。

## 2. 能源与太阳能模型
```
P_solar(t) = G_solar(t) × A_pv × η_pv(t) × cos(theta(t))
             × shading_factor(t) × wiring_efficiency(t)
P_solar(t) + P_battery_discharge(t) = P_IT(t) + P_bus(t)
                                      + P_battery_charge(t) + P_losses(t)
E_battery(t+Δt) = E_battery(t) + η_ch E_charge(t) − E_discharge(t)/η_dis
```
必须给轨道高度/倾角/日照食比例与结构姿态；“太阳能更充沛”不等于永不进入地影。光伏转换未成为电力的入射能，可能以辐射/热传导路径进入结构热平衡。

## 3. 热平衡与可行面积
```
Q_radiated = εσ A_effective × (T_r⁴ − T_sink_effective⁴) − Q_external_absorbed
Q_generated + Q_external_absorbed = Q_radiated + Q_other_out + dU/dt
A_effective = [Q_generated + Q_external_absorbed − Q_other_out]
              / [εσ(T_r⁴ − T_sink_effective⁴)]
```
两式仅表达同一能量平衡的重排概念，使用时**不得重复从辐射项扣除外部吸收、又在Q_generated中加一次**；数值模型需选一套一致符号：建议计算 `Q_rad_net=εσA(T_r⁴−T_sink⁴)−Q_abs`，在稳态令 `Q_rad_net=Q_generated−Q_other_out`。

基准自检值（理想有效单面，不含环境辐射/遮挡）：
- `350K, ε=1, 1MW`：约1175m²；
- `298.15K, ε=0.9, 2GW`：约4.96×10⁶m²；
- 面积不等于实际散热器质量，`M_rad = A_geom × kg_per_m² + M_pumps+M_plumbing+M_hinges+M_margin`，且有效面积与几何面积需分别记录。
- 如果电输入总额只有1GW、无其他外部能量，则稳态不能计算出2GW的计算废热。任何情况都必须通过残差检查 `abs(E_in−E_out)`。

## 4. 质量、发射与时间
```
M_total = Σ mass_item(kg)
N_launch_lower_bound = ceil(M_total / M_usable_per_launch_kg)
N_launch_actual >= N_launch_lower_bound
C_delivered = Σ launch_contracts + integration + transfer + assembly + risk
M_total_at_year_t = M_initial + cumulative_replacement − disposed_mass
```
重要：发射整流罩体积、模块最大尺寸、入轨倾角/推进需求、同轨组装及失败率可能令真实发射次数**高于**质量下界。每年可替换质量受发射频次和生产吞吐限制，必须用 `launches_per_year` 检查。

## 5. 寿命与全周期经济性
```
C_tco_nominal = C_IT + C_PV + C_storage + C_radiators + C_bus + C_launch
              + C_integration + C_comm + C_ops + C_replacements
              + C_failure + C_deorbit + C_insurance + C_financing
C_tco_pv = Σ_t [cash_outflow(t)−residual_value(t)] / (1+r)^t
usable_GPU_h = Σ_t N_GPU(t) × h_active(t) × availability(t)
               × performance_degradation_factor(t)
break_even = solve(C_orbit_per_usable_GPU_h − C_ground_per_usable_GPU_h = 0)
```
比较对象需相同负载、时窗、供电可靠性、吞吐/网络/存储服务标准和折现口径。地面算力也含电力、土地、冷却、网络、替换与资本成本。

## 6. 参数数据字典的第一版
| 字段 | 单位 | 来源/缺口 | 强制校验 |
|---|---|---|---|
| orbit_type, altitude, inclination | type, km, deg | 任务设定 | 非空且可实施 |
| IT_power | W | GPU/芯片规格、业务负载 | >0 |
| PV_area, PV_efficiency, eclipse_fraction | m², 0–1, 0–1 | 航天设计数据/待取 | 守恒 |
| radiator_temperature, radiator_emissivity, effective_area_factor | K,0–1,0–1 | NASA/设计 | 环境热源 |
| mass_IT, mass_PV, mass_radiator, mass_bus | kg | 工程质量预算 | 项目加总 |
| fairing_volume, usable_payload | m³, kg | 具体轨道/运载工具 | 质量及体积 |
| launch_price, other_delivery_costs | USD | 报价/合同/情景 | 带发布日期/适用轨道 |
| hardware_lifetime, failure_hazard, replacement_rate | years, hazard/year, kg/year | 可靠性统计/情景 | 不外推成确定值 |
| availability, comm_throughput, latency | fraction, Gbps, ms | 任务与链路预算 | 场景一致 |
| energy_price_ground, PUE_ground, discount_rate | USD/kWh, ratio, fraction/year | 地面对照 | 同币值/年 |
| source_url, observed_at, evidence_class, status | URL, date, enum, enum | 每个输入 | 禁止缺失时伪默认 |

## 7. 验收矩阵与防错项
- 单元测试：单位换算、面积的 Stefan–Boltzmann 反推、全功率余额、异常输入拒绝；`NOT_RUN`。
- 集成测试：100kW/1MW/10MW三档全闭环、质量与TCO敏感性；`NOT_RUN`。
- 对照/复现：BCG公开情景和官方报价能否在假设重建后解释量级差异；`NOT_RUN`。
- 模型中绝不把“1GW发电、2GW废热、0K宇宙背景、理想单面辐射、全部太阳能转换、零通信成本”同时作为未经检查的默认值。

**独立复核关口**：需物理模型复核（能量、热学）、航天运载复核（质量、可装载性）、经济模型复核（贴现、故障、更换）；不是多个AI赞成就算验收。