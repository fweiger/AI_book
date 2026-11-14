# M03｜太空算力的发射成本：从标称运价到交付后的可用算力

> 主问题：不是“火箭多少钱”，而是 **每单位有效在轨算力所需总质量 × 目标轨道运送与部署成本 × 全寿命补发需求**。本页是参数/口径模型，不是已经计算出的商业报价或回测结果。

## 1. 三层证据，不混用
| 证据层 | 示例 | 可用性限制 |
|---|---|---|
| L1 航天企业公开标价 | SpaceX 2026 Falcon 9 标准付款方案 $74M/发（[官方PDF](https://www.spacex.com/assets/media/Capabilities%26Services.pdf)） | 合同结构与任务配置决定实际总价；不能等于专属LEO单公斤价 |
| L1 官方运力指标 | Falcon 9官网列LEO最大约22.8t；上述PDF列22,000kg且**注明完全一次性构型最大能力** | 仅理论运力上界；可回收配置、轨道、整流罩、重心与发射场约束不同 |
| L1 小卫星拼车公开标价 | SpaceX Rideshare公开页面：SSO 50kg 起约$350k，额外重量约$7k/kg（[官网](https://new.spacex.com/rideshare)） | 拼车任务/舱位/轨道/交付接口限定，不得直接用于万吨级算力站的成本推算 |
| L2 独立研究假设 | BCG 2026 模拟 $1,500/kg 当前基线，以及未来更低值的情景（[BCG](https://www.bcg.com/publications/2026/space-based-data-centers-cost-outlook)） | 研究者条件模型，**不是可下单报价** |
| L3 前瞻/条件目标 | 可重复使用超重型火箭的若干目标 `$/kg` | 必须标为 `SCENARIO`，给适用轨道、货运频次与时间截面，不能当事实 |

## 2. 质量预算必须是闭合账本
```
M_payload = M_compute + M_memory_storage + M_solar + M_battery
          + M_radiators + M_heat_pipes_fluid_pumps
          + M_structure + M_shielding + M_comms_ground_terminals
          + M_propulsion + M_attitude_control + M_redundancy + M_spares
          + M_deployment_system + M_mass_margin
```
要求为每项提供 `source, mass_kg, power_W, heat_W, lifecycle_year, confidence, uncertainty_interval`。并明确散热器质量不只是散热板表面积，还包括系统管路、工质、展开机构、结构与稳定性。

## 3. 运送到目标轨道的真实分母
```
N_launch = ceil(M_payload / min(M_usable_by_mass, M_usable_by_volume))
C_delivery = N_launch * C_contractual_launch
            + C_payload_integration + C_deployment + C_in_orbit_assembly
            + C_transfer + C_insurance + C_injection_failure_allowance
C_per_delivered_kg = C_delivery / M_operational_in_target_orbit
```
注意：公式的 `min` 两项都要先转为**可比的质量当量**；体积上限以 `M_usable_by_volume = V_fairing_effective × density_packaged` 表示。复杂部署还需按单体模块、组合总结构成和节点可搭载性做装载分组优化，简单 `ceil` 是下界而非完整装配计划。不得以已装载质量替代最终实际可工作的质量。

## 4. 规模与替代发射分析
先做 `100kW、1MW、10MW` 三档；通过后再扩至 `100MW、1GW`。每一档分别输出：
- 设备质量 kg、单位IT功率 kg/MW、散热面积与散热系统kg、光伏及储能kg。
- 可用每次运载质量 kg/launch、每次实际价格、发射次数、每年需要的发射量、任务排期、失败后补发。
- 全生命周期失败率/替换次数、保险和补发风险的期望值与尾部区间。
- `C_delivery/MW_IT` 与 `C_delivery/effective GPU-hour`，以及总TCO占比。

至少三种运价情景：`Observed_quoted`（可核报价，注明轨道及生效日）、`Industry_reference`（如BCG的研究模型）、`Future_assumption`（明确设定，不得假称行业现价）。还需对单位功率质量和寿命同时做二维/三维敏感性，单独降低发射价并不能证明盈利。

## 5. 可否证的四个假说
| 假说 | 预测 | 主要反例/失败条件 |
|---|---|---|
| H-L1 发射单位运价下降使在轨算力接近地面 | 其他条件相同时空间TCO差缩小 | 设备损耗和寿命替换大于发射降价节省 |
| H-L2 大规模太阳翼摊薄每MWh成本 | 轨道供电可利用率提高 | 电池、阴影、接收功率、辐射老化和投影面积质量攀升 |
| H-L3 提高散热器温度降低发射质量 | 温度升高带来面积与质量降低 | GPU/冷却回路可靠性、热泵COP、散热面承载改变，系统总功耗反增 |
| H-L4 在轨处理空间原生数据先获得商业价值 | 下行通信和时延成本下降 | 星上维护/软件更新与辐射容错成本抵消优势 |

## 6. 首批硬约束
- SpaceX 2026 官方 PDF 的 $74M/发与22,000kg 最大LEO载荷不是自动配套的商业服务条件。
- BCG 2026 的 20 年 TCO 模型给当前空间$660–750M/MW、地面$230–300M/MW，约2.5–3倍；仅供**条件假设检查**，不能反推出同一通用每公斤报价，或声称独立实测。
- 不把未来火箭运价目标、首个实验卫星、1GW系统的理论算力与实际营收混为一谈。

## 7. 第一轮待执行的复算任务
补齐 `model-inputs` 的参数注册表；对每个输入记录来源、情景年份、轨道、任务架构和可信区间。求 `Break_even_launch_USD_per_kg` 并在GPU寿命/故障率/散热质量多参数变化下绘图；复算完成前结论为 `NOT_RUN`。

## 8. 2026-11-14 增补：星舰Flight 15 事实核查与发射经济学更新

本模块新增 [完整审查](FLIGHT15_COST_FACTCHECK_20261114.md)，已从Ubuntu MCP读取「未来学研究局」的转写全文，并与 SpaceX官方任务资料、SpaceX在美SEC披露、独立报道交叉核验：

- 本次26颗V3卫星部署属实（约2t/颗为公开报道约值），按视频假设$130M/52t = **$2500/kg**；`$130M`未有可核单飞财务披露。
- 60颗×2t=120t 是未来满载假设，`$130M/120t≈$1083/kg`只是条件算术，不等于Flight 15本次实际成本。
- 完全回收若单飞$20–30M、有效100t，得到`$200–300/kg`。若未来200t，得到`$100–150/kg`。
- 长期`$40–85/kg`**不能由上述$20–30M与100–200t自然推出**；若100t对应 $4–8.5M/发，若200t对应$8–17M/发，须另外论证。
- SpaceX披露 Starship V3约100t及V4潜在200t是预期运力、不是第15飞验证值。回收一次不代表可稳定高频复飞。

**模块边界调整**：发射运输只归入 `A_total`，在轨制造/光伏/散热/GPU/通信/维护/折旧归入 `B_total`，参见 [ORBITAL_BUILD_OPERATIONS.md](ORBITAL_BUILD_OPERATIONS.md)。两模块共同决定 `$/effective_GPU-hour`。
