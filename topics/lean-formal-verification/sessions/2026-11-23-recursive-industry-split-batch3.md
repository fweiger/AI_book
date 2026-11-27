# TOPIC-018｜跨行业递归下钻 Batch 3：完成 60 个初始父节点的一层覆盖

> 日期：2026-11-23 · Task ID：`AI-BOOK-TOPIC-018-LEAN-FORMAL-VERIFICATION`  
> 规范任务：[Issue #74](https://github.com/fweiger/AI_book/issues/74) · [Draft PR #75](https://github.com/fweiger/AI_book/pull/75)  
> 主要交付：[124 个候选子节点及论文—GitHub 项目表](../industry-recursive-split-register.md)（§2C、§2D）  
> **核心目标：** 先把 Lean 及相邻形式化技术可以进入哪些行业/业务领域/问题的研究树递归钻到具体项目，后续才按用户选定方向启动仓库审计或最小原型。

## 1. 继续前恢复与实际范围

- 原已批准 Goal/Scope/Non-goals/AC、任务属主与路由保持不变；锁定的 Task Center V1.2.2 protocol commit `f0e5ccb90c54265dcd07abb9a975c903eb031ccf`。
- 回读时：规范 Issue #74、PR #75、唯一 `task-goals/issue-74/GOAL_TRACKER.md`。上一批 Batch2 事件已在 Issue #74 comment #7093511668 唯一回读；原 Writer 为 NONE，状态 SYNCED。
- 原计划：60 个初始父节点中有 35 个已拆，25 个未拆；74 个候选子节点。应继续递归，但不为固定数量凑项目。
- 本轮按行业问题逐项读取了 GitHub README、项目技术规格和必要的论文/标准入口，识别可独立研究的问题，并区分 Lean 直接项目、通用 Lean 基础设施、相邻形式化工具、行业参考实现以及没有 Lean 项目的差距。

## 2. 数据范围、计算口径与结果

| 计数 | 本轮前 | 本轮后 | 解释 |
|---|---:|---:|---|
| 一级行业 | 12 | 12 | 行业导航范围不变 |
| 首轮父节点 | 60 | 60 | 父节点已编号 `IND01-01` 等 |
| 已至少拆一次的父节点 | 35 | **60** | 仅表示存在至少一个问题级子节点 |
| 完全未拆的父节点 | 25 | **0** | **不表示再也无需向更深层递归** |
| 累计候选子节点 | 74 | **124** | Batch3 新增 **50** 个 |
| 本轮新拆父节点 | — | **25** | 16 个父节点 + 后续 9 个父节点 |
| 本轮带有 GitHub 仓库 URL 的候选子节点 | — | **50/50** | 真实仓库定位/README 来源级核验，不是代码构建验收 |

数据由两份 Markdown 主表抽取：`industry-leaf-project-map.md` 的 60 个父 ID，以及 `industry-recursive-split-register.md` 的 124 个唯一子 ID。实际回读确认：124/124 子节点均包含 GitHub URL；124 个子 ID 唯一；全部 60 个父 ID 至少对应一个子节点。存在项目别名、归档/后继及跨行业重复引用，因此 **124 绝不等于 124 个唯一 GitHub 项目**。

## 3. 新增 25 个父节点与 50 个子问题

### 3.1 第一组：16 个父节点 → 32 个子节点

| 行业/父节点 | 拆分的两类具体问题 | GitHub 关键入口 | 主要原始证据 |
|---|---|---|---|
| IND01-02 芯片 RTL | 组合逻辑规格→Verilog；时序仲裁/总线状态与性质 | [Verilean/sparkle](https://github.com/Verilean/sparkle) | Sparkle 原始验证框架及 Signal DSL 资料；项目技术材料，不当作同行评审论文 |
| IND01-03 编译器 | SSA peephole 变换正确性；LLVM→RISC-V 指令选择精化 | [lean-mlir](https://github.com/opencompl/lean-mlir) | [ITP 2024](https://doi.org/10.4230/LIPIcs.ITP.2024.9) 论文与上游仓库直接对应；早期代码生成学位仓库已归档并上游 |
| IND03-01 密码学 | oracle/概率游戏语义；game hopping/关系程序逻辑 | [VCVio](https://github.com/Verified-zkEVM/VCVio) | [ePrint 2026/899](https://eprint.iacr.org/2026/899) |
| IND03-03 zkVM | OpenVM SHA-256 precompile soundness；ZisK RV64IM trace correctness 的实际边界 | [openvm-fv](https://github.com/openvm-org/openvm-fv)、[zisk-fv](https://github.com/eth-act/zisk-fv) | 各项目原始 README/正式规范；ZisK 明确警告仍 WIP、不能作为安全保证 |
| IND05-04 航空飞控 | 线性/ODE/Lyapunov 数学控制性质；飞控混合系统模式和安全包线 | [LeanForControl](https://github.com/AnandGokhale/LeanForControl)、[KeYmaeraX](https://github.com/LS-Lab/KeYmaeraX-release) | 控制数学项目资料、KeYmaera X 原始论文；**无证据证明 PX4 生产飞控已经由 Lean 验证** |
| IND05-05 城市交通 | SUMO 微观路网/信号仿真；LeanLTL 交通灯安全时序示例 | [SUMO](https://github.com/eclipse-sumo/sumo)、[LeanLTL](https://github.com/UCSCFormalMethods/LeanLTL) | 项目原始说明与 ITP 2025 论文；两个项目并不互为一套正式形式化交通系统 |
| IND06-02 工业 CPS | 层级状态机；FMI/SSP 联合仿真模型接口 | [ModelicaStandardLibrary](https://github.com/Modelica/ModelicaStandardLibrary)、[OpenModelica](https://github.com/OpenModelica/OpenModelica) | 工程模型/项目资料，**LEAN_GAP**；仿真不等于定理证明 |
| IND06-05 过程工业 | 热流体 ODE 工程模型；吸附 Langmuir/BET 科学公式证明 | [OpenModelica](https://github.com/OpenModelica/OpenModelica)、[LeanChemicalTheories](https://github.com/atomslab/LeanChemicalTheories) | [RSC 化学物理论文](https://doi.org/10.1039/d3dd00077j)；Lean 化学项目论文对应旧 Lean 3 |
| IND07-03 开源 AID | IOB 时间/估计量；CGM 与预测/输注约束 | [openaps/oref0](https://github.com/openaps/oref0) | 原始系统代码及临床/共识论文（背景，不是算法的形式化 companion）；**LEAN_GAP**，无临床建议 |
| IND09-01 统计学习 | 高斯 Lipschitz 集中界；localized regression 风险与 minimax 率 | [lean-stat-learning-theory](https://github.com/YuanheZ/lean-stat-learning-theory) | [ICML 2026 论文](https://arxiv.org/abs/2602.02285)；不把论文之后新增模块全部算作论文已证明 |
| IND10-02 QFT/AQFT | Haag–Kastler 公理；GNS/谱/Stone 结构与定理 | [physicslib4](https://github.com/physicslib/physicslib4) | 原始理论论文与 Blueprint/项目文档；README 研究计划不等于全部 theorem 已验证 |
| IND10-03 量子信息 | 量子态/信道基础；量子熵/信息不等式 | [Physlib](https://github.com/leanprover-community/physlib) | 旧 [Lean-QuantumInfo](https://github.com/Timeroot/Lean-QuantumInfo) README 确认 2026-03 并入 Physlib；避免重复计算活跃仓库 |
| IND10-05 化学材料 | Langmuir 单层吸附；BET 多层吸附 | [LeanChemicalTheories](https://github.com/atomslab/LeanChemicalTheories) | [RSC 论文及附录](https://doi.org/10.1039/d3dd00077j)；论文伴随源码历史 Lean 3 |
| IND10-06 气候 | ClimaCore 球面/笛卡尔网格 PDE 离散；ClimaAtmos 大气/对流参数化 | [ClimaCore.jl](https://github.com/CliMA/ClimaCore.jl)、[ClimaAtmos.jl](https://github.com/CliMA/ClimaAtmos.jl) | 官方 Julia 项目资料；**LEAN_GAP**，ClimateMachine 旧论文不是新库直接 companion |
| IND12-01 教育 | 自然数证明关卡；Lean 游戏服务器/课程接口 | [NNG4](https://github.com/leanprover-community/NNG4)、[lean4game](https://github.com/leanprover-community/lean4game) | 教育研究论文与项目 README；框架工程成功不等于教学效果已证明 |
| IND12-03 科研知识 | Blueprint 定理依赖与代码映射；checkdecls/文档一致性 | [PatrickMassot/leanblueprint](https://github.com/PatrickMassot/leanblueprint) | 官方 README 与 PFR Blueprint 方法文章；该工具是知识/工程基础设施，不是独立数学证明 |

### 3.2 第二组：最后 9 个父节点 → 18 个子节点

| 行业/父节点 | 拆分的两类具体问题 | GitHub 关键入口 | 主要界限 |
|---|---|---|---|
| IND03-04 密码工程 | Aeneas Rust MIR/LLBC→Lean 翻译；Rust FRI folding 证明案例 | [aeneas](https://github.com/AeneasVerif/aeneas)、[rust-lean](https://github.com/Verified-zkEVM/rust-lean) | 翻译器与使用该翻译器的论文实践仓库不能混为一体 |
| IND05-02 铁路 | 区段互斥 safety；消息顺序/deadlock/liveness | [safe-railway-system-promela](https://github.com/egrabanica/safe-railway-system-promela) | **Promela/SPIN 课程项目，非完整 ETCS 系统验证，LEAN_GAP** |
| IND07-01 医疗器械 | 透析状态机 ASM；透析超滤控制仿真 | [asmeta](https://github.com/asmeta/asmeta)、[Dialysis-Machine-Simulink](https://github.com/mathworks/Dialysis-Machine-Simulink) | ASMETA 工具与透析研究有关，但未独立定位该论文具体项目文件；Simulink 工程不是 Lean 认证医疗设备 |
| IND07-05 生物信息 | 生物序列解析；分子/SMILES/descriptor | [Biopython](https://github.com/biopython/biopython)、[RDKit](https://github.com/rdkit/rdkit) | 行业参考实现，尚无直接 Lean 项目，不能把普通包的单元测试当作定理证明 |
| IND09-04 AI 计算硬件 | Triton GPU kernel 给定输入下内存边界；CuTe/TMEM 同步 | [lean_kernel_verify](https://github.com/facebookresearch/lean_kernel_verify) | **跨行业复用 IND01-04**；不另算为一个独立项目或独立证明 |
| IND10-01 高能物理 | 物理定义/定理入库；PhyslibAlpha 与 reviewed core 的治理 | [Physlib](https://github.com/leanprover-community/physlib) | **旧 HepLean→PhysLean 已并入 Physlib**，Alpha 草案不能视为 review PASS |
| IND11-03 权限合规 | Cedar RBAC/ABAC 规则语义；Lean/Rust 差分一致性 | [cedar-spec](https://github.com/cedar-policy/cedar-spec)、[cedar](https://github.com/cedar-policy/cedar) | **跨行业复用 IND02-01**，不是新增一项独立验证 |
| IND11-05 公共采购 | OCDS tender/award schema；合同 amendment 变更与版本血缘 | [open-contracting/standard](https://github.com/open-contracting/standard) | 标准/Schema 工程，**LEAN_GAP**；采购规范正确性不是 Lean 已证明 |
| IND12-05 科学知识 | Physlib 物理知识形式化；LeanChemicalTheories 化学论文结果资产化 | [Physlib](https://github.com/leanprover-community/physlib)、[LeanChemicalTheories](https://github.com/atomslab/LeanChemicalTheories) | 复用 IND10-01/IND10-05；同项目跨行业出现不等于独立新增仓库 |

## 4. 数据质量与证据边界

逐行重新解析两个主表，结果：

- 60/60 首轮父节点有至少一个子节点。
- 124/124 子节点 ID 唯一；124/124 有 GitHub URL；0 个子节点完全没有原始来源 URL。
- 其中 **20 条文本包含 `LEAN_GAP`**、**6 条文本包含 `CROSS_DOMAIN_REUSE`**。这两个数是当前登记字段的关键词命中数，不是穷尽的专业审计分类，不代表其他节点都完整证明。
- **124 是行业应用场景—问题关联数，不是论文数、项目数、唯一项目数，更不是通过审核的 Lean 证明数。**
- 任何新节点均为 `CANDIDATE_LEAF`；`LEAF_CLOSED` 要求更进一步的单问题粒度与直接证据核验。查不到 direct Lean 项目的行业仍然保留机会假设，不虚构仓库。
- 项目 README 中所谓 sorry-free、proof count、build green、production-grade 等是上游作者陈述，本轮没有核验其版本、构建、信任边界和独立复现。
- 源码审计、license 检查、external clean build、原型：**NOT_RUN**，按用户要求后置。
- 未修改 AI_Trader #488，未进行交易或生产访问。

## 5. 容易出现的逻辑错误与改进规则

1. **“父节点全部拆分” ≠ “所有叶节点已研究到底”。** 本次仅补齐初始一层，仍须继续深入到不可再拆的算法/性质/项目级条目。
2. **同一代码仓库跨行业**：例如 Cedar 既用于云授权也用于合规，LKV 既用于芯片/kernel 也用于 AI 计算平台，Physlib 既用于物理研究也用于知识服务；保留行业场景映射，但标 `CROSS_DOMAIN_REUSE`，最终统计唯一仓库需单独去重。
3. **技术报告、论文与版本**：Sparkle、LKV、ZisK 和 OpenModelica 的项目文档不自动变成同行评审论文；论文/标准与代码版本关系尚需深查。
4. **形式化方法 ≠ Lean 专属**：KeYmaera X、SPIN、Modelica、ASMETA、Simulink 与直接 Lean 证明有不同定位。
5. **形式化证明 ≠ 现实可靠性**：对于医疗设备、金融策略和气候模型，模型语义、测量数据及生产实现都需独立核验。
6. **历史项目迁移**：HepLean/PhysLean→Physlib，Lean-QuantumInfo→Physlib，RISC-V 早期 codegen thesis→lean-mlir 必须记成前驱/后继关系，而非独立活跃项目。

## 6. 状态和唯一下一步

- **PASS（结构映射层）**：12 行业 / 60 父节点全部至少一层递归，下钻 124 个具有原始材料和 GitHub 仓库的候选项目级场景。
- **PARTIAL（AC-03）**：124 个候选叶节点尚未全部证实“单一问题—目标性质—论文/标准—实际项目”强关系；有跨行业复用、项目级资料缺口和继续下钻空间。
- **PARTIAL（AC-07）**：Lean 专属应用、相邻形式化工具和普通参考实现已有分级，但具体行业边界仍需深挖。
- **NOT_RUN**：本轮新项目审计、外部 build、独立 QA 和最小原型。
- **Goal drift：D0**；没有改变 Issue #74 已批准 Goal/Scope/AC。
- **唯一下一步：** 不再机械增加一级父节点覆盖数量；对 124 个候选子节点进行 **叶节点深度复核与来源完整性分层**，优先识别 `CONTINUE_SPLIT`、`DIRECT_COMPANION`、`RELATED_METHOD`、`PAPER_GAP`、`PROJECT_GAP`、`CROSS_DOMAIN_REUSE` 和 `LEAN_GAP`。对仍包含不同算法/系统/目标性质的子节点继续向第三、第四及更深层拆分，直到各最小问题可对应 GitHub 项目（项目审计和原型仍后置）。
