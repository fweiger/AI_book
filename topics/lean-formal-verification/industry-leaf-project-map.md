# TOPIC-018｜Lean 跨行业递归下钻与 GitHub 项目叶节点地图

> **版本：** v0.2 · 2026-11-23  
> **首轮覆盖：** 12 个一级行业、60 个最小研究单元（可变深度树）。  
> **本轮终点：** 每条研究分支必须落到至少一个真实 GitHub 项目，并挂接对应论文、标准或原始技术资料。项目内部审计、clean build、最小原型和生产集成留待用户选定方向后处理。  
> **范围说明：** 这是一张首轮覆盖地图，不代表 60 个项目都是 Lean 项目，也不代表项目已经过源码审计或生产验证。

## 1. 递归下钻规则

`L1 行业 → L2 业务领域 → L3 细分领域 → L4 价值链环节/场景 → L5 具体问题 → L6 形式化对象与目标性质 → 论文/标准 → GitHub 项目`

- 深度不是固定值。如果 L3 已形成独立问题，可提前收敛；如果 L5 仍是“系统安全”“模型正确”等宽泛描述，则继续拆成组件、算法、协议或状态转移。
- 每个叶节点必须回答：谁遇到什么问题、形式化什么对象、检查/证明什么性质、对应什么论文/标准、对应哪个 GitHub 仓库。
- 一个仓库可以覆盖多个叶节点；一个叶节点也可以挂接多个仓库。
- 没有直接 Lean 项目时，不得编造 Lean 采用案例；必须映射同一问题的相邻形式化工具或真实行业实现，并明确标记关系。

## 2. 项目关系标签与证据等级

| 标签 | 含义 |
|---|---|
| `DIRECT_LEAN_APPLICATION` | Lean 已直接进入具体应用/研发流程 |
| `DIRECT_LEAN_RESEARCH` | Lean 项目直接形式化领域数学、算法、协议或性质 |
| `LEAN_INFRASTRUCTURE` | Lean 数学库、语言基础设施或证明工具，可支撑领域形式化，但不代表行业已采用 |
| `ADJACENT_FORMAL_TOOL` | 使用 Coq/Rocq、F*、TLA+、SPIN、SMT、模型检查等相邻形式化技术，不是 Lean |
| `DOMAIN_REFERENCE_IMPLEMENTATION` | 行业真实系统/算法/数据模型，可作为后续形式化对象，本身不提供形式化证明 |

- **E1：** 已读取项目 README/官方文档，确认项目用途与叶节点的关联；未审计源码、许可证、依赖或构建。
- **E0：** 已确认 GitHub 仓库及元数据，但未完整读取 README。
- **PAPER / STANDARD：** 对应论文、规范或原始技术资料。
- **PAPER_GAP：** 尚未找到足够直接的论文；该叶节点的研究证据尚未闭合。

## 3. 行业叶节点地图

### IND-01｜半导体、计算机与硬件

| ID | 递归路径（L2 → L3 → 场景） | 最小问题 / 形式化对象 | 论文、标准或原始依据 | GitHub 项目 | 关系与证据 |
|---|---|---|---|---|---|
| IND01-01 | 芯片架构 → ISA → RISC-V 指令语义与实现一致性 | 指令状态转移、位向量算术、opcode 实现是否满足 ISA 规格 | [RISC-V ISA](https://github.com/riscv/riscv-isa-manual)；[xv6iris 研究](https://arxiv.org/abs/2609.04043) | [opencompl/sail-riscv-lean](https://github.com/opencompl/sail-riscv-lean)；[openvm-org/openvm-fv](https://github.com/openvm-org/openvm-fv)；[mit-pdos/xv6iris](https://github.com/mit-pdos/xv6iris/tree/lean) | DIRECT_LEAN_RESEARCH / E1 |
| IND01-02 | 芯片设计 → RTL/HDL → 组合与时序电路 | 电路状态、时序关系、模块接口、硬件描述与数学模型的一致性 | [Formal Methods in Industry](https://doi.org/10.1145/3689374)（行业证据，非 Lean 专属论文） | [Verilean/sparkle](https://github.com/Verilean/sparkle) | DIRECT_LEAN_RESEARCH / E1；Sparkle 专属同行评审论文仍待补查 |
| IND01-03 | 芯片工具链 → 编译器/IR → SSA 与 RISC-V 代码生成 | IR 语义、编译变换保持、目标指令生成与源程序语义等价 | [RISC-V Lean 代码生成研究仓库](https://github.com/salinhkuhn/llvm-riscv-verified-codegen-thesis-wip)；[Formal Methods in Industry](https://doi.org/10.1145/3689374) | [opencompl/lean-mlir](https://github.com/opencompl/lean-mlir)；[llvm-riscv-verified-codegen](https://github.com/salinhkuhn/llvm-riscv-verified-codegen-thesis-wip) | DIRECT_LEAN_RESEARCH / LEAN_INFRASTRUCTURE / E1；代码生成仓库已归档 |
| IND01-04 | 计算加速器 → GPU kernel → 内存访问与并行执行 | kernel 内存边界、索引映射、线程块约束、屏障与写入正确性 | [TorchLean 研究](https://arxiv.org/abs/2602.22631)；kernel verifier 项目文档 | [facebookresearch/lean_kernel_verify](https://github.com/facebookresearch/lean_kernel_verify)；[lean-dojo/TorchLean](https://github.com/lean-dojo/TorchLean) | DIRECT_LEAN_RESEARCH / E1 |
| IND01-05 | 芯片加速器 → zkVM/密码学硬件 → 指令与电路约束 | RISC-V 扩展、有限域运算、电路约束与参考语义一致性 | [VCVio ePrint 2026/899](https://eprint.iacr.org/2026/899)；OpenVM 规格 | [openvm-org/openvm-fv](https://github.com/openvm-org/openvm-fv)；[Verified-zkEVM/ArkLib](https://github.com/Verified-zkEVM/ArkLib)；[Verified-zkEVM/VCVio](https://github.com/Verified-zkEVM/VCVio) | DIRECT_LEAN_RESEARCH / E1 |

### IND-02｜软件、云计算与数字基础设施

| ID | 递归路径（L2 → L3 → 场景） | 最小问题 / 形式化对象 | 论文、标准或原始依据 | GitHub 项目 | 关系与证据 |
|---|---|---|---|---|---|
| IND02-01 | 云服务 → 身份与授权 → policy evaluator/authorizer | 策略求值、授权决策、类型检查与错误处理是否满足安全性质 | [AWS Cedar verification-guided development](https://aws.amazon.com/blogs/opensource/lean-into-verified-software-development/)；[Lean 官方 Cedar 案例](https://lean-lang.org/use-cases/cedar/) | [cedar-policy/cedar-spec](https://github.com/cedar-policy/cedar-spec)；[cedar-policy/cedar](https://github.com/cedar-policy/cedar) | DIRECT_LEAN_APPLICATION / E1；已公开的 Lean 生产工作流案例 |
| IND02-02 | 软件研发 → Rust 关键组件 → 程序规格与实现精化 | Rust 函数语义、前后置条件、实现精化与函数正确性 | [Aeneas/Rust-to-Lean 研究](https://arxiv.org/abs/2605.30106) | [AeneasVerif/aeneas](https://github.com/AeneasVerif/aeneas)；[Verified-zkEVM/rust-lean](https://github.com/Verified-zkEVM/rust-lean)；[cryspen/hax](https://github.com/cryspen/hax) | DIRECT_LEAN_RESEARCH / E1 |
| IND02-03 | 数据基础设施 → Datalog/查询引擎 → 规则推导 | 规则推导、查询结果正确性、可检查证书与推理过程 | [Certifying Datalog / ITP 2025](https://doi.org/10.4230/LIPIcs.ITP.2025.36) | [knowsys/CertifyingDatalog](https://github.com/knowsys/CertifyingDatalog) | DIRECT_LEAN_RESEARCH / E1 |
| IND02-04 | 云端工作流 → 异步服务/分布式任务 → 状态与时序性质 | 事件顺序、状态迁移、幂等性、安全性与活性 | [LeanLTL / ITP 2025](https://doi.org/10.4230/LIPIcs.ITP.2025.37)；[Veil/CAV 2025](https://doi.org/10.1007/978-3-031-98682-6_2) | [UCSCFormalMethods/LeanLTL](https://github.com/UCSCFormalMethods/LeanLTL)；[verse-lab/Lentil](https://github.com/verse-lab/Lentil)；[resonatehq/resonate-specification](https://github.com/resonatehq/resonate-specification) | DIRECT_LEAN_RESEARCH / DOMAIN_REFERENCE_IMPLEMENTATION / E1 |
| IND02-05 | 操作系统 → 内核组件 → 系统调用与进程状态 | 内核状态转移、系统调用语义、资源不变量与实现符合规格 | [xv6iris 研究](https://arxiv.org/abs/2609.04043) | [mit-pdos/xv6iris](https://github.com/mit-pdos/xv6iris/tree/lean) | DIRECT_LEAN_RESEARCH / E1；特定 xv6 子集，不代表完整生产 OS 已验证 |

### IND-03｜网络安全、密码学与区块链

| ID | 递归路径（L2 → L3 → 场景） | 最小问题 / 形式化对象 | 论文、标准或原始依据 | GitHub 项目 | 关系与证据 |
|---|---|---|---|---|---|
| IND03-01 | 密码学 → 安全定义 → 安全游戏与归约 | 对手、挑战者、优势、归约和安全参数的定义与证明 | [VCVio ePrint 2026/899](https://eprint.iacr.org/2026/899) | [Verified-zkEVM/VCVio](https://github.com/Verified-zkEVM/VCVio) | DIRECT_LEAN_RESEARCH / E1 |
| IND03-02 | 零知识证明 → SNARK/IOP → 证明系统组件 | 多项式承诺、约束系统、证明/验证关系与组合性质 | [ArkLib 项目研究资料](https://github.com/Verified-zkEVM/ArkLib)；[VCVio ePrint](https://eprint.iacr.org/2026/899) | [Verified-zkEVM/ArkLib](https://github.com/Verified-zkEVM/ArkLib)；[Verified-zkEVM/CompPoly](https://github.com/Verified-zkEVM/CompPoly) | DIRECT_LEAN_RESEARCH / E1；具体定理覆盖需后续逐项核对 |
| IND03-03 | 区块链基础设施 → zkVM → RISC-V/Keccak/SHA 扩展 | VM 指令执行与规格一致，密码学扩展实现满足形式化语义 | [OpenVM-FV 项目说明](https://github.com/openvm-org/openvm-fv)；RISC-V ISA | [openvm-org/openvm-fv](https://github.com/openvm-org/openvm-fv) | DIRECT_LEAN_RESEARCH / E1；不等于整个 zkVM 端到端安全证明 |
| IND03-04 | 密码工程 → Rust 密码库 → 代码抽取与实现验证 | 从受限 Rust 子集抽取语义，验证实现满足形式化规格 | [Aeneas/Rust-to-Lean 研究](https://arxiv.org/abs/2605.30106) | [AeneasVerif/aeneas](https://github.com/AeneasVerif/aeneas)；[Verified-zkEVM/rust-lean](https://github.com/Verified-zkEVM/rust-lean) | DIRECT_LEAN_RESEARCH / E1 |
| IND03-05 | 分布式安全 → BFT/共识协议 → 状态转移与不变量 | 协议参与者状态、消息顺序、容错假设、安全性与活性 | [Veil/CAV 2025](https://doi.org/10.1007/978-3-031-98682-6_2)；IFP 项目研究资料 | [verse-lab/veil](https://github.com/verse-lab/veil)；[sarvalabs/ifp](https://github.com/sarvalabs/ifp) | DIRECT_LEAN_RESEARCH / E1；部署环境和协议假设需单独建模 |

### IND-04｜金融、银行与经济基础设施

| ID | 递归路径（L2 → L3 → 场景） | 最小问题 / 形式化对象 | 论文、标准或原始依据 | GitHub 项目 | 关系与证据 |
|---|---|---|---|---|---|
| IND04-01 | 金融数学 → 随机过程 → Brownian motion/SDE | 概率空间、滤过、随机过程、布朗运动与随机积分定义 | [MathFin 研究](https://arxiv.org/abs/2606.01356)；随机分析基础文献 | [formal-applied-math/formal-mathfin](https://github.com/formal-applied-math/formal-mathfin)；[RemyDegenne/brownian-motion](https://github.com/RemyDegenne/brownian-motion) | DIRECT_LEAN_RESEARCH / E1 |
| IND04-02 | 资产定价 → 衍生品定价 → 二叉树/Black–Scholes | 无套利、风险中性测度、定价递推和模型假设 | Black–Scholes (1973)；Cox–Ross–Rubinstein (1979)；MathFin 研究 | [formal-applied-math/formal-mathfin](https://github.com/formal-applied-math/formal-mathfin)；[RemyDegenne/brownian-motion](https://github.com/RemyDegenne/brownian-motion) | DIRECT_LEAN_RESEARCH / E1；具体模型定理覆盖需后续核实 |
| IND04-03 | 资产管理 → 组合优化/风险 → Markowitz/CVaR | 可行域、目标函数、风险度量、凸性与最优性条件 | [Markowitz (1952)](https://doi.org/10.1111/j.1540-6261.1952.tb01525.x)；[Rockafellar–Uryasev CVaR](https://doi.org/10.21314/JOR.2000.038) | [formal-applied-math/formal-mathfin](https://github.com/formal-applied-math/formal-mathfin)；[Mathlib4](https://github.com/leanprover-community/mathlib4) | DIRECT_LEAN_RESEARCH / LEAN_INFRASTRUCTURE / E1；不证明真实市场收益 |
| IND04-04 | 量化研究 → PIT 数据治理 → as-of/无未来函数 | 事件时间、可得时间、修订版本、股票池成员时点与回测可见信息 | [Probability of Backtest Overfitting](https://doi.org/10.21314/JCF.2016.322)；[The Seven Sins of Quantitative Investing](https://doi.org/10.3905/jpm.2019.1.069) | [AI_book PIT/no-lookahead 规格](https://github.com/fweiger/AI_book/tree/topic/TOPIC-018/lean-formal-verification-20261122/topics/lean-formal-verification)；[AI_Trader #488](https://github.com/fweiger/AI_Trader/issues/488) | DIRECT_LEAN_RESEARCH / INTERNAL_PROJECT / E1；仍是最小规格而非全数据管线验证 |
| IND04-05 | 经济金融 → 市场设计 → 拍卖/机制/社会选择 | 偏好、策略、均衡、激励相容、投票规则与社会选择性质 | [EconCSLib 研究](https://arxiv.org/abs/2606.16144)；[经济机制 Lean 研究](https://arxiv.org/abs/2606.13306) | [matheconlib/matheconlib](https://github.com/matheconlib/matheconlib)；[gametheoryinlean/EconCSLib](https://github.com/gametheoryinlean/EconCSLib)；[SocialChoiceLean](https://github.com/dominikpeters/SocialChoiceLean) | DIRECT_LEAN_RESEARCH / E1 |

### IND-05｜航空航天、交通与汽车

| ID | 递归路径（L2 → L3 → 场景） | 最小问题 / 形式化对象 | 论文、标准或原始依据 | GitHub 项目 | 关系与证据 |
|---|---|---|---|---|---|
| IND05-01 | 铁路 → 联锁系统 → 进路锁闭/区段占用 | 状态机、轨道区段占用、冲突进路、安全不变量与活性 | [SPIN 铁路控制系统验证](https://doi.org/10.1109/ICDSN.2000.857524)；[ETCS 联锁验证](https://doi.org/10.1016/j.scico.2016.05.010) | [safe-railway-system-promela](https://github.com/egrabanica/safe-railway-system-promela)；[tlaplus/Examples](https://github.com/tlaplus/Examples) | ADJACENT_FORMAL_TOOL / E1；示例不等同工业认证 |
| IND05-02 | 铁路 → 列控通信 → ETCS/通信协议顺序 | 消息顺序、状态同步、通信故障、故障安全与协议活性 | [ETCS 联锁形式化研究](https://doi.org/10.1016/j.scico.2016.05.010)；SPIN 铁路系统研究 | [safe-railway-system-promela](https://github.com/egrabanica/safe-railway-system-promela)；[apalache-mc/apalache](https://github.com/apalache-mc/apalache) | ADJACENT_FORMAL_TOOL / E1 |
| IND05-03 | 汽车 → ADAS → ACC/AEB/LKA 控制器安全 | 混合自动机、控制不变量、可达集与神经网络控制器安全边界 | [Code-Level Safety Verification for Automated Driving](https://doi.org/10.1007/978-3-031-71177-0_22)；[CoCoSaFe 2025](https://doi.org/10.1016/j.jss.2025.112499) | [neu-autonomy/nfl_veripy](https://github.com/neu-autonomy/nfl_veripy)；[carla-simulator/carla](https://github.com/carla-simulator/carla)；[KeYmaeraX](https://github.com/LS-Lab/KeYmaeraX-release) | ADJACENT_FORMAL_TOOL / DOMAIN_REFERENCE_IMPLEMENTATION / E1 |
| IND05-04 | 航空航天 → 飞控/UAV → 自动驾驶仪与安全包线 | 混合系统动力学、控制器不变量、模式切换、故障降级与可达性 | [KeYmaera 混合系统安全教程](https://doi.org/10.1007/s10009-015-0367-0)；[Lean 控制理论](https://arxiv.org/abs/2607.19727) | [PX4/PX4-Autopilot](https://github.com/PX4/PX4-Autopilot)；[KeYmaeraX](https://github.com/LS-Lab/KeYmaeraX-release)；[LeanForControl](https://github.com/AnandGokhale/LeanForControl) | ADJACENT_FORMAL_TOOL / DOMAIN_REFERENCE_IMPLEMENTATION / DIRECT_LEAN_RESEARCH |
| IND05-05 | 城市交通 → 路网调度 → 交通流/信号与V2X | 路网状态、信号相位、交通流约束、事件顺序和调度安全 | [SUMO 参考论文](https://github.com/eclipse-sumo/sumo/blob/main/CITATION.cff)；[V2X 仿真研究](https://doi.org/10.1016/j.sbspro.2012.06.100) | [eclipse-sumo/sumo](https://github.com/eclipse-sumo/sumo)；[tlaplus/Examples](https://github.com/tlaplus/Examples) | DOMAIN_REFERENCE_IMPLEMENTATION / ADJACENT_FORMAL_TOOL / E1 |

### IND-06｜工业制造、机器人与能源

| ID | 递归路径（L2 → L3 → 场景） | 最小问题 / 形式化对象 | 论文、标准或原始依据 | GitHub 项目 | 关系与证据 |
|---|---|---|---|---|---|
| IND06-01 | 工业控制 → PLC → IEC 61131-3 梯形图/结构化文本 | PLC 扫描周期、定时器/计数器状态、互斥、响应和安全不变量 | [ESBMC-PLC+](https://arxiv.org/abs/2606.23870)；[PLC 基准集](https://arxiv.org/abs/2609.18994) | [IS2Lab/esbmc-plcplus](https://github.com/IS2Lab/esbmc-plcplus)；[PLC benchmark suite](https://github.com/pierredantas/esbmc-plc-benchmark-suite)；[OpenPLC](https://github.com/thiagoralves/OpenPLC_v3) | ADJACENT_FORMAL_TOOL / DOMAIN_REFERENCE_IMPLEMENTATION / E1 |
| IND06-02 | 智能制造 → CPS 控制模块 → 状态机到控制实现 | UML 状态机、控制模块状态、时序逻辑性质、验证模型与 FPGA 实现一致性 | [Formal Verification of Control Modules in CPS](https://doi.org/10.3390/s20185154) | [OpenModelica](https://github.com/OpenModelica/OpenModelica)；[ModelicaStandardLibrary](https://github.com/Modelica/ModelicaStandardLibrary) | ADJACENT_FORMAL_TOOL / DOMAIN_REFERENCE_IMPLEMENTATION / E1 |
| IND06-03 | 机器人 → 运动规划 → 机械臂轨迹与碰撞约束 | 运动学、动力学、轨迹约束、碰撞自由与控制器稳定性 | [MoveIt Task Constructor / ICRA 2019](https://doi.org/10.1109/ICRA.2019.8793898)；[Lean 控制理论](https://arxiv.org/abs/2607.19727) | [moveit/moveit2](https://github.com/moveit/moveit2)；[LeanForControl](https://github.com/AnandGokhale/LeanForControl)；[DynamicalSystems](https://github.com/mcdoll/DynamicalSystems) | DOMAIN_REFERENCE_IMPLEMENTATION / DIRECT_LEAN_RESEARCH / E1 |
| IND06-04 | 电力能源 → 电网运行 → 潮流/拓扑/调度安全 | 电网拓扑、潮流方程、操作约束、可行动作和安全状态 | [pandapower 论文](https://doi.org/10.1109/TPWRS.2018.2829021)；[Grid2Op 项目资料](https://github.com/Grid2op/Grid2Op) | [Grid2Op](https://github.com/Grid2op/Grid2Op)；[pandapower](https://github.com/e2nIEE/pandapower) | DOMAIN_REFERENCE_IMPLEMENTATION / E1；未找到直接 Lean 电网项目 |
| IND06-05 | 过程工业 → 化工/热工装置 → 物理过程与控制逻辑 | 物理模型、单位/量纲、ODE、控制状态、边界条件与误差界 | [Formal Verification of Control Modules in CPS](https://doi.org/10.3390/s20185154)；[Lean 化学物理形式化](https://doi.org/10.1039/d3dd00077j) | [OpenModelica](https://github.com/OpenModelica/OpenModelica)；[ModelicaStandardLibrary](https://github.com/Modelica/ModelicaStandardLibrary)；[LeanChemicalTheories](https://github.com/atomslab/LeanChemicalTheories) | DIRECT_LEAN_RESEARCH / DOMAIN_REFERENCE_IMPLEMENTATION / E1；化学项目为 Lean 3 历史版本 |

### IND-07｜医疗、医疗器械与生命科学

| ID | 递归路径（L2 → L3 → 场景） | 最小问题 / 形式化对象 | 论文、标准或原始依据 | GitHub 项目 | 关系与证据 |
|---|---|---|---|---|---|
| IND07-01 | 医疗器械 → 设备软件 → 治疗设备安全状态 | 设备状态机、报警/联锁、剂量边界、故障模式与软件安全性质 | [Medical software formal methods review](https://doi.org/10.1002/smr.1943)；[Hemodialysis device ASM method](https://doi.org/10.1016/j.scico.2017.07.003) | [KeYmaeraX](https://github.com/LS-Lab/KeYmaeraX-release)；[openaps/oref0](https://github.com/openaps/oref0) | ADJACENT_FORMAL_TOOL / DOMAIN_REFERENCE_IMPLEMENTATION / E1；未找到 Lean 医疗器械专属项目 |
| IND07-02 | 医疗信息化 → EHR/FHIR → 患者记录与资源引用一致性 | FHIR resource schema、引用完整性、工作流状态、版本兼容与数据约束 | [ISO/PAS 24305:2025](https://www.iso.org/cms/%20render/live/en/sites/isoorg/contents/data/standard/07/83/78390.html)；医疗软件形式化方法综述 | [HL7/fhir](https://github.com/HL7/fhir)；[openmrs/openmrs-core](https://github.com/openmrs/openmrs-core) | DOMAIN_REFERENCE_IMPLEMENTATION / E0；Lean 适配仍为机会假设 |
| IND07-03 | 糖尿病管理 → 自动胰岛素输注 → 控制算法与泵/CGM状态 | 输入数据时点、预测状态、剂量上限、控制状态机与安全约束 | [Open-source automated insulin delivery RCT](https://doi.org/10.1056/NEJMoa2203913)；[Open-source AID consensus](https://pmc.ncbi.nlm.nih.gov/articles/PMC8720075/) | [openaps/oref0](https://github.com/openaps/oref0)；[OpenAPS documentation](https://openaps.readthedocs.io/en/latest/) | DOMAIN_REFERENCE_IMPLEMENTATION / E1；不是 Lean 证明或医疗建议 |
| IND07-04 | 生命科学 → 系统生物学 → SBML反应网络与动力学模型 | 反应网络、物种/参数、ODE、模型语义、单位与仿真可复现性 | [Systems Biology standards and best practices](https://pmc.ncbi.nlm.nih.gov/articles/PMC10435326/) | [sbmlteam/libsbml](https://github.com/sbmlteam/libsbml)；[sys-bio/tellurium](https://github.com/sys-bio/tellurium) | DOMAIN_REFERENCE_IMPLEMENTATION / E1；Lean 专属生物模型库待发现 |
| IND07-05 | 生物信息 → 序列/分子计算 → 算法与化学结构处理 | 序列算法、分子表示、结构转换、算法不变量与数值/单位约束 | [Biopython paper](https://doi.org/10.1093/bioinformatics/btp163)；[Lean chemical physics](https://doi.org/10.1039/d3dd00077j) | [biopython/biopython](https://github.com/biopython/biopython)；[rdkit/rdkit](https://github.com/rdkit/rdkit)；[LeanChemicalTheories](https://github.com/atomslab/LeanChemicalTheories) | DOMAIN_REFERENCE_IMPLEMENTATION / DIRECT_LEAN_RESEARCH / E1 |

### IND-08｜电信、通信与信息服务

| ID | 递归路径（L2 → L3 → 场景） | 最小问题 / 形式化对象 | 论文、标准或原始依据 | GitHub 项目 | 关系与证据 |
|---|---|---|---|---|---|
| IND08-01 | 信息论 → 信息量度 → 熵/KL/互信息与数据处理不等式 | 离散/连续分布、熵、相对熵、互信息及不等式 | Cover & Thomas, *Elements of Information Theory*；Lean 信息论项目资料 | [LeanInfoTheory](https://github.com/serhatemrecoban/LeanInfoTheory)；[infotheorylib](https://github.com/matteonerini/infotheorylib) | DIRECT_LEAN_RESEARCH / E1 |
| IND08-02 | 通信编码 → 信源/信道编码 → rate-distortion | 失真函数、率失真函数、编码率下界、最优性与渐近性质 | [Rate-distortion Lean research](https://arxiv.org/abs/2610.22404) | [rate_distortion_lean4](https://github.com/fubinyan/rate_distortion_lean4)；[LeanInfoTheory](https://github.com/serhatemrecoban/LeanInfoTheory) | DIRECT_LEAN_RESEARCH / E1 |
| IND08-03 | 通信网络 → 可编程数据平面 → P4 packet processing | P4 操作语义、状态包处理、程序优化保持与多包性质 | [Foundational Verification of Stateful P4 Packet Processing](https://www.cs.princeton.edu/~appel/papers/FoundationalVerificationP4.pdf)；[P4 verification dissertation](https://doi.org/10.7298/a0dy-4f33) | [VerifiableP4](https://github.com/verified-network-toolchain/VerifiableP4)；[p4c](https://github.com/p4lang/p4c) | ADJACENT_FORMAL_TOOL（Coq）/ DOMAIN_REFERENCE_IMPLEMENTATION / E1 |
| IND08-04 | 网络协议 → 协议状态机 → 安全性/活性与消息顺序 | 状态迁移、时序逻辑、消息因果、协议安全性与活性 | [LeanLTL / ITP 2025](https://doi.org/10.4230/LIPIcs.ITP.2025.37)；[Veil/CAV 2025](https://doi.org/10.1007/978-3-031-98682-6_2) | [LeanLTL](https://github.com/UCSCFormalMethods/LeanLTL)；[Lentil](https://github.com/verse-lab/Lentil)；[Veil](https://github.com/verse-lab/veil) | DIRECT_LEAN_RESEARCH / E1 |

### IND-09｜人工智能、机器学习与自主系统

| ID | 递归路径（L2 → L3 → 场景） | 最小问题 / 形式化对象 | 论文、标准或原始依据 | GitHub 项目 | 关系与证据 |
|---|---|---|---|---|---|
| IND09-01 | 机器学习 → 统计学习理论 → 泛化界与学习保证 | 假设空间、损失函数、泛化误差、复杂度界与概率不等式 | [AI4SLT / ICML 2026](https://proceedings.mlr.press/v306/zhang26cd.html) | [lean-stat-learning-theory](https://github.com/YuanheZ/lean-stat-learning-theory) | DIRECT_LEAN_RESEARCH / E1 |
| IND09-02 | 深度学习 → 张量/算子语义 → 模型变换与计算正确性 | 张量形状、算子语义、自动微分/计算变换和数学性质 | [TorchLean research](https://arxiv.org/abs/2602.22631) | [lean-dojo/TorchLean](https://github.com/lean-dojo/TorchLean) | DIRECT_LEAN_RESEARCH / E1 |
| IND09-03 | AI 安全 → 神经网络验证 → 鲁棒性/可达性 | 输入扰动集合、输出界、可达集、反例与安全性质 | [Marabou neural network verification](https://doi.org/10.1007/978-3-030-25540-4_26)；VNN-COMP 研究 | [StarV](https://github.com/V2A2/StarV)；[Marabou](https://github.com/NeuralNetworkVerification/Marabou)；[alpha-beta-CROWN](https://github.com/Verified-Intelligence/alpha-beta-CROWN) | ADJACENT_FORMAL_TOOL / E1；可后续研究将证书导入 Lean |
| IND09-04 | AI 计算基础设施 → GPU kernel → 内存/并行正确性 | kernel 索引、内存访问、同步、边界和规格符合性 | [TorchLean research](https://arxiv.org/abs/2602.22631)；kernel verifier 项目说明 | [lean_kernel_verify](https://github.com/facebookresearch/lean_kernel_verify)；[TorchLean](https://github.com/lean-dojo/TorchLean) | DIRECT_LEAN_RESEARCH / E1 |
| IND09-05 | AI for Math → 自动证明 → 检索/前提选择/tactic建议 | 证明检索、上下文选择、候选 tactic 与 Kernel 可检查性 | [LeanDojo](https://arxiv.org/abs/2306.15626)；[LeanCopilot](https://arxiv.org/abs/2404.12534) | [LeanDojo](https://github.com/lean-dojo/LeanDojo)；[LeanCopilot](https://github.com/lean-dojo/LeanCopilot) | LEAN_INFRASTRUCTURE / DIRECT_LEAN_RESEARCH / E1；原 LeanDojo 仓库 README 标记 deprecated |

### IND-10｜科学研究与工程计算

| ID | 递归路径（L2 → L3 → 场景） | 最小问题 / 形式化对象 | 论文、标准或原始依据 | GitHub 项目 | 关系与证据 |
|---|---|---|---|---|---|
| IND10-01 | 高能物理 → 场论/粒子物理 → 物理数学结果数字化 | 物理定义、指标约定、代数恒等式、推导链和定理依赖 | [HepLean: Digitalising high energy physics](https://doi.org/10.1016/j.cpc.2024.109457) | [HEPLean/HepLean](https://github.com/HEPLean/HepLean)；[leanprover-community/physlib](https://github.com/leanprover-community/physlib) | DIRECT_LEAN_RESEARCH / E1 |
| IND10-02 | 理论物理 → QFT/AQFT → 场论定义与推导 | 算子代数、场论公理、对称性、扰动展开与数学结构 | [FormalQFT research](https://arxiv.org/abs/2603.15770) | [physicslib/physicslib4](https://github.com/physicslib/physicslib4)；[PhysLib](https://github.com/leanprover-community/physlib) | DIRECT_LEAN_RESEARCH / E1；具体 QFT 定理覆盖需核对 |
| IND10-03 | 量子科学 → 量子信息 → 量子态/信道/信息不等式 | 量子态、密度矩阵、量子信道、熵与信息论性质 | [Quantum Stein lemma formalization](https://arxiv.org/abs/2510.08672) | [PhysLib](https://github.com/leanprover-community/physlib)；[Lean-QuantumInfo](https://github.com/Timeroot/Lean-QuantumInfo) | DIRECT_LEAN_RESEARCH / E1；旧项目与 PhysLib 迁移关系待确认 |
| IND10-04 | 工程计算 → ODE/PDE/优化 → 数值算法与动力系统 | 微分方程、解的存在唯一性、稳定性、误差界、优化条件 | [Lean control theory research](https://arxiv.org/abs/2607.19727)；SciLean 项目说明 | [SciLean](https://github.com/lecopivo/SciLean)；[DynamicalSystems](https://github.com/mcdoll/DynamicalSystems)；[LeanForControl](https://github.com/AnandGokhale/LeanForControl) | DIRECT_LEAN_RESEARCH / E1；SciLean 定位为早期 proof-of-concept |
| IND10-05 | 化学与材料 → 化学物理 → 吸附/热力学/运动学推导 | Langmuir/BET 模型、热力学关系、量纲和推导假设 | [Formalizing Chemical Physics Using Lean](https://doi.org/10.1039/d3dd00077j) | [ATOMSLab/LeanChemicalTheories](https://github.com/atomslab/LeanChemicalTheories)；[RDKit](https://github.com/rdkit/rdkit) | DIRECT_LEAN_RESEARCH / DOMAIN_REFERENCE_IMPLEMENTATION / E1；论文代码为 Lean 3 历史版本 |
| IND10-06 | 地球科学 → 气候/地球系统模型 → 数值模型与守恒约束 | PDE/ODE 离散、守恒量、边界条件、数值稳定性和参数约束 | [Large-eddy simulations with ClimateMachine v0.2.0](https://doi.org/10.5194/gmd-15-6259-2022) | [CliMA/ClimaCore.jl](https://github.com/CliMA/ClimaCore.jl)；[CliMA/ClimaAtmos.jl](https://github.com/CliMA/ClimaAtmos.jl)；[CliMA/ClimaCoupler.jl](https://github.com/CliMA/ClimaCoupler.jl)；[SciLean](https://github.com/lecopivo/SciLean) | DOMAIN_REFERENCE_IMPLEMENTATION / DIRECT_LEAN_RESEARCH / E1；旧 ClimateMachine.jl 仓库 README 明确标记不再维护，已改列当前 successor repos；未找到 Lean 专属气候应用 |

### IND-11｜政府、法律、合规与公共基础设施

| ID | 递归路径（L2 → L3 → 场景） | 最小问题 / 形式化对象 | 论文、标准或原始依据 | GitHub 项目 | 关系与证据 |
|---|---|---|---|---|---|
| IND11-01 | 法律 → 成文法解释 → 资格条件/例外/裁量 | 法律规则、例外关系、证据支持、可形式化边界与人工判断事项 | [Catala: a Programming Language for the Law](https://doi.org/10.1145/3473582)；[LegalLean monograph](https://legal-lean.aguilar-pelaez.co.uk/) | [edu-ap/legal-lean](https://github.com/edu-ap/legal-lean)；[CatalaLang/catala](https://github.com/CatalaLang/catala) | DIRECT_LEAN_RESEARCH（LegalLean，早期）/ ADJACENT_FORMAL_TOOL（Catala/F*）/ E1 |
| IND11-02 | 法律科技 → 可计算合同 → 条款/义务/付款触发 | 合同数据模型、义务状态、触发条件、例外与执行结果 | [Catala ICFP 2021](https://doi.org/10.1145/3473582)；Accord Project 技术文档 | [accordproject/concerto](https://github.com/accordproject/concerto)；[CatalaLang/catala](https://github.com/CatalaLang/catala) | ADJACENT_FORMAL_TOOL / DOMAIN_REFERENCE_IMPLEMENTATION / E0 |
| IND11-03 | 政府与企业合规 → 访问控制 → 身份/角色/权限策略 | 策略语言、角色属性、授权决策、拒绝默认与类型安全 | [AWS Cedar verification-guided development](https://aws.amazon.com/blogs/opensource/lean-into-verified-software-development/) | [cedar-policy/cedar-spec](https://github.com/cedar-policy/cedar-spec)；[cedar-policy/cedar](https://github.com/cedar-policy/cedar) | DIRECT_LEAN_APPLICATION / E1 |
| IND11-04 | 公共治理 → 选举与投票 → 选票加密/计票/公平性 | 加密选票、零知识证明、可验证计票、投票规则性质 | [ElectionGuard / USENIX Security 2024](https://www.usenix.org/conference/usenixsecurity24/presentation/benaloh)；[ElectionGuard 规范](https://electionguard.vote/spec/) | [ElectionGuard](https://github.com/Election-Tech-Initiative/electionguard)；[ElectionGuard verifier](https://github.com/Election-Tech-Initiative/electionguard-verifier)；[SocialChoiceLean](https://github.com/dominikpeters/SocialChoiceLean) | DOMAIN_REFERENCE_IMPLEMENTATION / DIRECT_LEAN_RESEARCH / E1 |
| IND11-05 | 公共采购 → 采购数据与合规 → 招标字段和流程约束 | 数据 schema、字段约束、采购阶段状态、合同条款与可追溯性 | [Open Contracting Data Standard](https://standard.open-contracting.org/)；Catala 法律计算论文 | [open-contracting/standard](https://github.com/open-contracting/standard)；[accordproject/concerto](https://github.com/accordproject/concerto) | DOMAIN_REFERENCE_IMPLEMENTATION / E0；Lean 专属采购项目未找到 |

### IND-12｜教育、科研知识与知识服务

| ID | 递归路径（L2 → L3 → 场景） | 最小问题 / 形式化对象 | 论文、标准或原始依据 | GitHub 项目 | 关系与证据 |
|---|---|---|---|---|---|
| IND12-01 | 数学教育 → 证明教学 → 自然数/线性代数交互练习 | 教学命题、练习依赖、证明状态、学习脚手架与反馈 | [Learning about Proof with Lean](https://doi.org/10.1007/s40753-021-00140-1)；[Teaching Mathematics with Lean](https://doi.org/10.1090/noti3184)；[Natural Number Game study](https://doi.org/10.1007/s40751-025-00193-w) | [leanprover-community/NNG4](https://github.com/leanprover-community/NNG4)；[leanprover-community/lean4game](https://github.com/leanprover-community/lean4game) | DIRECT_LEAN_APPLICATION / E1 |
| IND12-02 | 数学科研 → 猜想形式化 → 定理陈述与证明依赖 | 猜想陈述、定义映射、引理依赖、证明对象与反例边界 | [Formal Conjectures](https://arxiv.org/abs/2605.13171)；[Mathlib paper](https://doi.org/10.1145/3372885.3373824) | [google-deepmind/formal-conjectures](https://github.com/google-deepmind/formal-conjectures)；[leanprover-community/mathlib4](https://github.com/leanprover-community/mathlib4) | DIRECT_LEAN_RESEARCH / E1 |
| IND12-03 | 科研知识管理 → Blueprint/依赖图 → 论文定理与 Lean 文件对应 | 定理、定义、依赖关系、证明状态、文献来源和版本映射 | [Mathlib paper](https://doi.org/10.1145/3372885.3373824)；Lean Blueprint 文档 | [PatrickMassot/leanblueprint](https://github.com/PatrickMassot/leanblueprint) | LEAN_INFRASTRUCTURE / E1 |
| IND12-04 | AI 知识服务 → 证明助理 → 检索/前提选择/tactic建议 | 证明检索、上下文选择、候选 tactic 与 Kernel 可检查性 | [LeanDojo](https://arxiv.org/abs/2306.15626)；[LeanCopilot](https://arxiv.org/abs/2404.12534) | [lean-dojo/LeanDojo](https://github.com/lean-dojo/LeanDojo)；[lean-dojo/LeanCopilot](https://github.com/lean-dojo/LeanCopilot) | LEAN_INFRASTRUCTURE / DIRECT_LEAN_RESEARCH / E1 |
| IND12-05 | 科学知识服务 → 学科知识数字化 → 物理/化学定理库 | 学科定义、公式、假设、推导链、跨论文定理复用 | [Formalizing Chemical Physics Using Lean](https://doi.org/10.1039/d3dd00077j)；PhysLib 项目资料 | [leanprover-community/physlib](https://github.com/leanprover-community/physlib)；[ATOMSLab/LeanChemicalTheories](https://github.com/atomslab/LeanChemicalTheories) | DIRECT_LEAN_RESEARCH / E1；化学项目对应历史 Lean 3 版本 |

## 4. 60 个叶节点覆盖统计

| 一级行业 | 叶节点数 | Lean 直接项目覆盖概况 | 主要相邻/行业项目 |
|---|---:|---|---|
| IND-01 半导体、计算机与硬件 | 5 | ISA、HDL、编译器、GPU kernel、zkVM 均有 Lean 研究线索 | RISC-V、HDL、GPU 项目 |
| IND-02 软件、云计算与数字基础设施 | 5 | Cedar、Aeneas、Datalog、LTL、xv6 均有 Lean 研究或应用 | Rust/云服务系统 |
| IND-03 网络安全、密码学与区块链 | 5 | VCVio、ArkLib、OpenVM-FV、Rust-to-Lean、Veil | 协议与密码工程 |
| IND-04 金融、银行与经济基础设施 | 5 | 数学金融、机制设计和 PIT 原型有 Lean 项目 | 风险/投资/市场系统 |
| IND-05 航空航天、交通与汽车 | 5 | Lean 主要提供控制理论支撑 | SPIN、TLA+、KeYmaera X、CARLA、PX4、SUMO |
| IND-06 工业制造、机器人与能源 | 5 | Lean 控制理论与化学理论可提供数学层支撑 | ESBMC-PLC+、Modelica、MoveIt、Grid2Op、pandapower |
| IND-07 医疗、医疗器械与生命科学 | 5 | 暂未找到可确认的 Lean 医疗生产应用 | OpenAPS、FHIR、OpenMRS、SBML、Biopython |
| IND-08 电信、通信与信息服务 | 4 | 信息论、rate-distortion、LTL/协议有 Lean 项目 | P4/Coq |
| IND-09 AI、机器学习与自主系统 | 5 | 学习理论、TorchLean、GPU kernel、证明助理有 Lean 项目 | StarV、Marabou、alpha-beta-CROWN |
| IND-10 科学研究与工程计算 | 6 | 物理、量子信息、科学计算、化学有 Lean 项目 | ClimateMachine、RDKit |
| IND-11 政府、法律、合规与公共基础设施 | 5 | LegalLean、Cedar、SocialChoiceLean | Catala、ElectionGuard、OCDS |
| IND-12 教育、科研知识与知识服务 | 5 | 教学、Mathlib、Formal Conjectures、Blueprint、AI proof search 均有项目 | Lean 教学和知识工具 |

## 5. 当前证据边界与缺口

1. 项目映射完成不代表项目审计完成。本文件不声称新增项目的 build、CI、许可证、依赖或证明完整性已通过。
2. Lean 项目和相邻项目严格区分。铁路、汽车、医疗、PLC、P4、选举等案例多数使用 SPIN/TLA+/Coq/F*/SMT 或行业参考实现。
3. 部分 Lean 仓库是历史/早期项目：LeanChemicalTheories 对应论文代码是 Lean 3；RISC-V codegen thesis repo 已归档；LeanDojo 原仓库 README 标记 deprecated；SciLean README 定位为早期 proof-of-concept。
4. 医疗与生命科学当前以行业参考实现为主，未确认 Lean 在这些具体工作流中采用。
5. 气候、电网、交通、采购等方向虽有项目，但 Lean 的增量价值仍待验证；ClimateMachine.jl 旧仓库已标记不再维护，当前映射转向 ClimaCore/ClimaAtmos/ClimaCoupler。
6. 部分论文是行业/方法证据，不是项目的直接 companion paper；后续要继续核对每条论文—项目关系，不能把相关性写成同一研究团队或同一实现。

## 6. 本阶段完成定义与下一步

完成条件：
- 12 个行业均递归拆分，不停在行业名称或抽象二级领域。
- 每个叶节点是可独立研究的问题，明确形式化对象和目标性质。
- 每个叶节点至少有一个真实 GitHub 项目，并标明 Lean、相邻工具或行业参考实现。
- 每个叶节点至少挂接一个相关论文、标准或原始技术资料；证据不足时标记缺口。
- 形成可追溯的行业—问题—论文—项目映射。

**下一轮唯一主线：** 对 60 个叶节点逐项核对论文—项目对应关系，识别项目覆盖范围、直接 Lean 证据、相邻工具、参考实现和未闭合的论文缺口；继续拆细仍然过宽的叶节点，直到每个终点都有明确问题、论文和 GitHub 项目。项目内部审计与最小原型留待用户选定方向。
