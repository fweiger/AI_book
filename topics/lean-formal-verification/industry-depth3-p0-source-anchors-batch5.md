# TOPIC-018｜P0 深度映射 Batch 5：9 个 L2 高优先级分支 → 27 个可定位代码的 L3 问题

> 日期：2026-11-23 · [规范 Issue #74](https://github.com/fweiger/AI_book/issues/74) · [Draft PR #75](https://github.com/fweiger/AI_book/pull/75)  
> L2 主表：[124 个候选子节点](industry-recursive-split-register.md) · [P0/P1/P2 证据队列](industry-leaf-closure-triage.md) · [前一批 L3 的 16 个节点](industry-depth3-paper-project-map.md)  
> **本轮：处理 9 个 P0 L2 方向，增加 27 个 L3（每条问题/性质/源码路径/资料来源/限制），并将 CVaR 其中 1 个 L3 拆出 2 个 L4。** 这是源码入口和原文“索引核对”，不是代码审计/构建或任何新的 theorem 证明。

## 1. 选择理由与证据标准

初始 60/60 父节点已经有一层，现阶段不能靠机械增加项目数量推进。当前 30 个 P0 L2 中 9 个具备较明确的一手项目资料和子模块/算法边界；研究横跨 zkVM 硬件、异步工作流、SNARK、分布式共识、金融 CVaR、AI 算子、GPU 内存与同步安全（拆为两个 L2 父节点）、政府采购版本血缘。将不同目标性质保持为独立研究问题，保留 Lean / 相邻技术 / 行业参考实现与对应论文证据的区分。

**注意**：Github 项目的文件路径来自官方 README/项目规格，其中部分已通过仓库按路径回读，另一部分为 README 中指向的目录，标注 `PROJECT_DOCUMENTED_PATH` / `REPOSITORY_LAYOUT_VERIFIED`。`SOURCE_FILE_VERIFIED` 只证明本轮实际读取了指定原始文件内容；不等于证明通过。

## 2. 27 个 P0 第三级候选节点

| L3 ID | L2 父节点 | 单一目标问题 | 形式化对象 / 目标性质 | GitHub 中实际代码/目录 | 论文或一手技术证据 | 归类与读取级别 | 必须保留的限定 |
|---|---|---|---|---|---|---|---|
| `IND01-05-B-01` | `IND01-05-B` | SP1 加法芯片单行 AIR 约束的 soundness | AddChip.main/Assumptions/Spec; GeneralFormalCircuit.Soundness | [具体代码/源码位置](https://github.com/succinctlabs/sp1-lean/blob/main/SP1Clean/Proofs/Chips/AddChip/Formal.lean) | [第一手论文/技术资料](https://github.com/succinctlabs/sp1-lean/blob/main/README.md) | DIRECT_LEAN / SOURCE_ANCHOR_VERIFIED | 仅单 chip/row 的证明声明，非 zkVM 端到端 |
| `IND01-05-B-02` | `IND01-05-B` | AddChip 指定有效见证下的 completeness | AddChip.completeness、输入/见证存在性、row satisfaction | [具体代码/源码位置](https://github.com/succinctlabs/sp1-lean/blob/main/SP1Clean/Proofs/Chips/AddChip/Formal.lean) | [第一手论文/技术资料](https://github.com/succinctlabs/sp1-lean/blob/main/docs/release-audit.md) | DIRECT_LEAN / SOURCE_ANCHOR_VERIFIED | 其他芯片的 deferred completeness 不被此 theorem 覆盖 |
| `IND01-05-B-03` | `IND01-05-B` | Rust 约束到 Lean 模型的 faithful extraction | SP1 Rust extractor、Extracted/Circuit/、Faithful proof、witness conformance | [具体代码/源码位置](https://github.com/succinctlabs/sp1-lean/tree/main/SP1Clean/Faithful) | [第一手论文/技术资料](https://github.com/succinctlabs/sp1-lean/blob/main/docs/release-audit.md) | DIRECT_LEAN / PROJECT_DOCUMENTED_PATH | pin 与信任边界按 release-audit；不以测试等价替代所有源码精化 |
| `IND01-05-B-04` | `IND01-05-B` | ChipRow/程序跟踪组合与 whole-machine capstone | state/memory/program bus invariants；sp1_machine_soundness；decode seam | [具体代码/源码位置](https://github.com/succinctlabs/sp1-lean/tree/main/SP1Clean/Soundness) | [第一手论文/技术资料](https://github.com/succinctlabs/sp1-lean/blob/main/docs/release-audit.md) | DIRECT_LEAN / PROJECT_DOCUMENTED_PATH | 已记录 capstone 仍有 premise/decode 边界，不能称 whole VM 全证 |
| `IND02-04-B-01` | `IND02-04-B` | 异步 Promise/Task/Schedule 的状态迁移参考语义 | 请求处理、system τ steps、抽象状态与 effects | [具体代码/源码位置](https://github.com/resonatehq/resonate-specification/tree/main/spec/02-abstract) | [第一手论文/技术资料](https://github.com/resonatehq/resonate-specification/blob/main/README.md) | DIRECT_LEAN / REPOSITORY_LAYOUT_VERIFIED | 本项目是执行规格，不能自动声称真实服务器与规格等价 |
| `IND02-04-B-02` | `IND02-04-B` | 92 项状态/相邻状态协议性质的证明覆盖 | property catalogue、decidable predicate、unbounded invariants | [具体代码/源码位置](https://github.com/resonatehq/resonate-specification/tree/main/spec/04-theorems) | [第一手论文/技术资料](https://github.com/resonatehq/resonate-specification/blob/main/README.md) | DIRECT_LEAN / REPOSITORY_LAYOUT_VERIFIED | 官方自述 31/92 unbounded，61 open；1,464 scripts decide 不能当 92 全部已证 |
| `IND02-04-B-03` | `IND02-04-B` | 真实服务器 NDJSON 轨迹能否被 Lean 抽象机解释 | request/response+time、τ-step existential search、valid/lean checker | [具体代码/源码位置](https://github.com/resonatehq/resonate-specification/blob/main/valid/README.md) | [第一手论文/技术资料](https://github.com/resonatehq/resonate-specification/blob/main/README.md) | DIRECT_LEAN / SOURCE_FILE_VERIFIED | checker 接受 trace 是观测符合性，不是全系统无限轨迹证明 |
| `IND03-02-B-01` | `IND03-02-B` | IOR 的顺序组合与关系提升是否维持安全界 | OracleReduction、source/target relation、soundness/composition hypotheses | [具体代码/源码位置](https://github.com/Verified-zkEVM/ArkLib/tree/main/ArkLib/OracleReduction) | [第一手论文/技术资料](https://github.com/Verified-zkEVM/ArkLib/blob/main/ROADMAP.md) | DIRECT_LEAN / LEGACY_LAYER | 旧层较稳定，结论不能自动移交 Interaction 新层 |
| `IND03-02-B-02` | `IND03-02-B` | 依赖历史消息的 Interaction-tree IOR 执行与 Sumcheck | PolyFun interaction、world-backed execution、Sumcheck spec | [具体代码/源码位置](https://github.com/Verified-zkEVM/ArkLib/tree/main/ArkLib/ProofSystem/Sumcheck/Interaction) | [第一手论文/技术资料](https://github.com/Verified-zkEVM/ArkLib/blob/main/docs/design/00-current-status.md) | DIRECT_LEAN / ACTIVE_LAYER_STATUS | 当前迁移中，只按已完成的 Sumcheck/通用接口描述；不能称全部协议已迁移 |
| `IND03-02-B-03` | `IND03-02-B` | 承诺方案、Opening/BCS、Fiat-Shamir 变换的组合边界 | commitment interface、oracle opening、random oracle、SNARK security assumptions | [具体代码/源码位置](https://github.com/Verified-zkEVM/ArkLib/tree/main/ArkLib/Commitments) | [第一手论文/技术资料](https://github.com/Verified-zkEVM/ArkLib/blob/main/ROADMAP.md) | DIRECT_LEAN / ROADMAP_STATUS_REVIEW | 变换部分与成熟协议的状态不同；未核 theorem 不能称完备 |
| `IND03-05-A-01` | `IND03-05-A` | 同步 crash-fault FloodSet 的一致性与有效性 | agreement、validity、fail-stop、synchronous-round transition | [具体代码/源码位置](https://github.com/verse-lab/veil/blob/main/Examples/Tutorial/FloodSet.lean) | [第一手论文/技术资料](https://github.com/verse-lab/veil/blob/main/README.md) | DIRECT_LEAN / SOURCE_FILE_VERIFIED | 不是一般 Byzantine BFT；原 L2 的 BFT 概括应缩窄到 crash-fault 示例 |
| `IND03-05-A-02` | `IND03-05-A` | FloodSet 在故障假设下的 termination temporal claim | finite-state temporal property、#temporal_check、prove_temporal_by | [具体代码/源码位置](https://github.com/verse-lab/veil/blob/main/Examples/Demo/FloodSet/FloodSetLiveness.lean) | [第一手论文/技术资料](https://github.com/verse-lab/veil/blob/main/README.md) | DIRECT_LEAN / SOURCE_FILE_VERIFIED | 时间活性结论取决于同步轮次和故障假设，不能无条件推广 |
| `IND03-05-A-03` | `IND03-05-A` | 模型检查反例与归纳不变量的不同证据价值 | explicit/symbolic checking、invariant discovery、interactive Lean proof | [具体代码/源码位置](https://github.com/verse-lab/veil/blob/main/Examples/Tutorial/FloodSet.lean) | [第一手论文/技术资料](https://github.com/verse-lab/veil/blob/main/docs/ModelChecker-Guide.md) | DIRECT_LEAN / SOURCE_FILE_VERIFIED | model check PASS 与无界 theorem proof 分开记录 |
| `IND04-03-B-01` | `IND04-03-B` | 一般损失分布的 VaR 与 ES 量词和积分定义 | loss measurable、level α∈(0,1)、quantile/expectedShortfall | [具体代码/源码位置](https://github.com/formal-applied-math/formal-mathfin/blob/main/MathFin/Risk/ValueAtRisk.lean) | [第一手论文/技术资料](https://doi.org/10.21314/JOR.2000.038) | DIRECT_LEAN / SOURCE_FILE_VERIFIED | 一般概率分布含原子；理论定义不是具体交易风险模型 |
| `IND04-03-B-02` | `IND04-03-B` | Rockafellar–Uryasev CVaR 优化的全分布最小化定理 | isLeast_rockafellarUryasev、VaR point minimizer、Integrable X | [具体代码/源码位置](https://github.com/formal-applied-math/formal-mathfin/blob/main/MathFin/Risk/ExpectedShortfall.lean) | [第一手论文/技术资料](https://doi.org/10.21314/JOR.2000.038) | DIRECT_LEAN / SOURCE_FILE_VERIFIED | 原文为方法来源（不是 MathFin 项目的原论文 companion），保证仅针对形式化模型及假设 |
| `IND04-03-B-03` | `IND04-03-B` | Expected Shortfall 是否满足四条 coherent risk 公理 | mono、cash-additivity、positive homogeneity、subadditivity | [具体代码/源码位置](https://github.com/formal-applied-math/formal-mathfin/blob/main/MathFin/Risk/Coherent.lean) | [第一手论文/技术资料](https://github.com/formal-applied-math/formal-mathfin/blob/main/MathFin/Risk/ExpectedShortfall.lean) | DIRECT_LEAN / SOURCE_FILE_VERIFIED | 区分 loss 符号约定与 ADEH gain convention，不能误用方向 |
| `IND04-03-B-04` | `IND04-03-B` | 有限状态下风险度量的 acceptance-cone 对偶表示 | IsLUB 期望损失上界、representing probabilities、finite state | [具体代码/源码位置](https://github.com/formal-applied-math/formal-mathfin/blob/main/MathFin/Risk/AcceptanceSet.lean) | [第一手论文/技术资料](https://github.com/formal-applied-math/formal-mathfin/blob/main/MathFin/Risk/Coherent.lean) | DIRECT_LEAN / SOURCE_FILE_VERIFIED | 有限状态假设明确，不能擅自称一般无限维空间 |
| `IND09-02-C-01` | `IND09-02-C` | 精确实数算术下的 lowered tape 反向传播导数对应 | backwardDenseAll_eq_fderiv、GraphData.toTape、FDerivCorrectAt | [具体代码/源码位置](https://github.com/lean-dojo/TorchLean/blob/main/TorchLean/NN/Tape/Lowering/BackwardDenseGraph.lean) | [第一手论文/技术资料](https://github.com/lean-dojo/TorchLean/blob/main/docs/TRUST_BOUNDARIES.md) | DIRECT_LEAN / SOURCE_FILE_VERIFIED | 这不是 Float rounding 或 CUDA backward correctness |
| `IND09-02-C-02` | `IND09-02-C` | 后端 Capsule 合约如何限制 native CUDA/LibTorch 信任层 | ContractCheck/KernelCapsule、shape/layout/value/VJP assurances | [具体代码/源码位置](https://github.com/lean-dojo/TorchLean/blob/main/TorchLean/NN/Backend/ContractCheck.lean) | [第一手论文/技术资料](https://github.com/lean-dojo/TorchLean/blob/main/docs/TRUST_BOUNDARIES.md) | LEAN_CHECKER_AND_RUNTIME_GATE / SOURCE_FILE_VERIFIED | checked capsule 也可能走外部实现；测试/证书/证明不可混同 |
| `IND09-02-C-03` | `IND09-02-C` | CUDA/FFI 实际数值路径与 Lean 数学定理间的未覆盖部分 | Float rounding、LibTorch ATen、CUDA driver/hardware implementation | [具体代码/源码位置](https://github.com/lean-dojo/TorchLean/blob/main/docs/TRUST_BOUNDARIES.md) | [第一手论文/技术资料](https://github.com/lean-dojo/TorchLean/blob/main/README.md) | TRUST_BOUNDARY / SOURCE_FILE_VERIFIED | 这是需要验证的差距，不是已完成的 CUDA correctness 证明 |
| `IND01-04-A-01` | `IND01-04-A` | 给定 KIR/Input 下被 mask-in 的全局访存是否越过分配边界 | P0-1、allocation bounds、metadata load、KV.eval | [具体规格](https://github.com/facebookresearch/lean_kernel_verify/blob/main/references/specs.md) | [项目第一手说明](https://github.com/facebookresearch/lean_kernel_verify/blob/main/README.md) | DIRECT_LEAN / PRIMARY_PROJECT_SPEC | 只对给定 KIR 和具体 case input，不是所有 shape |
| `IND01-04-A-02` | `IND01-04-A` | GPU 地址表达式中的 i32/i64 BitVec wrap 是否导致越界 | P0-1 address-path wrap、BitVec width、concrete evaluation | [具体规格](https://github.com/facebookresearch/lean_kernel_verify/blob/main/references/specs.md) | [项目第一手说明](https://github.com/facebookresearch/lean_kernel_verify/blob/main/README.md) | DIRECT_LEAN / PRIMARY_PROJECT_SPEC | 与真实 GPU 编译器和任意 kernel 的完整证明不同 |
| `IND01-04-B-01` | `IND01-04-B` | named barrier 的 warp count 是否在给定执行中收敛 | P0-6、`bar.sync`/`bar.arrive`、warp arrival ledger | [具体规格](https://github.com/facebookresearch/lean_kernel_verify/blob/main/references/specs.md) | [README](https://github.com/facebookresearch/lean_kernel_verify/blob/main/README.md) | DIRECT_LEAN / PRIMARY_PROJECT_SPEC | 只对该 KIR 的参与角色计数，不能推出所有 barrier 无死锁 |
| `IND01-04-B-02` | `IND01-04-B` | CuTe kernel 中不同角色访问同一 TMEM cell 的重用是否被 ordered | P1-1、TMEM reuse、barrier/wait ordering | [具体规格](https://github.com/facebookresearch/lean_kernel_verify/blob/main/references/specs.md) | [README](https://github.com/facebookresearch/lean_kernel_verify/blob/main/README.md) | DIRECT_LEAN / PRIMARY_PROJECT_SPEC | P1 KIR 的 CuTe 范围，不涵盖通用 CUDA race freedom |
| `IND01-04-B-03` | `IND01-04-B` | TLX/Triton 异步 TMA store 的 shared-memory/tensormap 源是否提前复用 | P1-2、async store source reuse、PTX/KIR event ordering | [具体规格](https://github.com/facebookresearch/lean_kernel_verify/blob/main/references/specs.md) | [README](https://github.com/facebookresearch/lean_kernel_verify/blob/main/README.md) | DIRECT_LEAN / PRIMARY_PROJECT_SPEC | 只检查源码指定的 P1 事件条件，非全程序并发正确性 |
| `IND11-05-B-01` | `IND11-05-B` | OCDS 合同 amendment release 的版本化记录结构 | ocid、release.id/date/tag、contractAmendment payload | [具体代码/源码位置](https://github.com/open-contracting/standard/blob/main/docs/examples/change_history/contractAmendment.json) | [第一手论文/技术资料](https://github.com/open-contracting/standard/blob/main/schema/release-schema.json) | DOMAIN_REFERENCE_IMPLEMENTATION / PRIMARY_STANDARD | 当前只有 JSON/标准实现，LEAN_GAP；schema 合法不等于采购合法 |
| `IND11-05-B-02` | `IND11-05-B` | 合同变更的历史 release 合并为 compiled record 的数据血缘 | multiple releases、compiled record、revision chronology/merge | [具体代码/源码位置](https://github.com/open-contracting/standard/blob/main/docs/examples/change_history/records/contractAmendment.json) | [第一手论文/技术资料](https://github.com/open-contracting/standard/blob/main/README.md) | DOMAIN_REFERENCE_IMPLEMENTATION / PRIMARY_STANDARD | 这是版本血缘验证场景，未找到直接 Lean 项目，LEAN_GAP |

## 3. 第四层示例：一般分布 CVaR 最小化再拆为两条基本证明义务

以 `IND04-03-B-02` 为父节点，继续到可命名的 `MathFin/Risk/ExpectedShortfall.lean` 定理：**理论闭合与算法应用是两个层次**。

| L4 ID | L3 父节点 | 最小证明目标 | 具体源码/理论来源 | 仍需核对的假设 |
|---|---|---|---|---|
| `IND04-03-B-02-01` | `IND04-03-B-02` | **全局下界**：任意阈值 c 的 Rockafellar–Uryasev objective 均不低于 ES，源码 `expectedShortfall_le_rockafellarUryasev` | [ExpectedShortfall.lean](https://github.com/formal-applied-math/formal-mathfin/blob/main/MathFin/Risk/ExpectedShortfall.lean) / [Rockafellar–Uryasev](https://doi.org/10.21314/JOR.2000.038) | `Integrable X`、`α∈(0,1)`、损失符号约定 |
| `IND04-03-B-02-02` | `IND04-03-B-02` | **最优值可达**：在 `c = VaR_α(X)` 等号成立，源码 `rockafellarUryasev_valueAtRisk`；两者组合成 `isLeast_rockafellarUryasev` | [ExpectedShortfall.lean](https://github.com/formal-applied-math/formal-mathfin/blob/main/MathFin/Risk/ExpectedShortfall.lean) / [Rockafellar–Uryasev](https://doi.org/10.21314/JOR.2000.038) | quantile 定义、可积条件、允许分布原子点；未证明任何真实交易组合最优性 |

这些定理名称是对**作者仓库源文件的实际读取**，并非本轮运行 Lean 的定理验证。

## 4. 本轮实质纠错

### 金融风险：从泛用项目跳转到定理级论文和代码

以前 `IND04-03-B` 将“CVaR 的定义、凸表示与优化等价关系”合成一个节点。现已分开：
- `ValueAtRisk.lean`：一般损失的 VaR、ES 量词/分位数定义。
- `ExpectedShortfall.lean`：对一般**可积损失**的 RU 最小值定理，包括离散/含原子分布；`gaussianCVaR_isLeast_ruObjective` 仅为 `RockafellarUryasev.lean` 的高斯特例。
- `Coherent.lean` 与 `ExpectedShortfall.lean`：风险度量四公理与 ES 的证据。
- `AcceptanceSet.lean`：风险度量的有限状态对偶表达，不自动适用于一般无限维模型。

因此原始 [Rockafellar–Uryasev (2000)](https://doi.org/10.21314/JOR.2000.038) 是**经典数学定理来源**，不是 MathFin 仓库自身的“companion paper”。需要精确区分 `FORMALIZATION_OF_CLASSIC_THEOREM`。

### SP1、ArkLib、TorchLean 证明/实现的信任边界

- SP1 [README](https://github.com/succinctlabs/sp1-lean) 将 per-chip soundness、completeness、约束提取 faithfulness 和 whole-machine 组装分开；其 [release-audit](https://github.com/succinctlabs/sp1-lean/blob/main/docs/release-audit.md) 有固定版本和开放证明前提。**不得使用“SP1 zkVM 已全部完成验证”**这样的描述。
- ArkLib [README](https://github.com/Verified-zkEVM/ArkLib) 和 [current-status](https://github.com/Verified-zkEVM/ArkLib/blob/main/docs/design/00-current-status.md) 区分 legacy OracleReduction 和正在迁移的 Interaction layer；旧层定理不自动覆盖新层。
- TorchLean [trust boundaries](https://github.com/lean-dojo/TorchLean/blob/main/docs/TRUST_BOUNDARIES.md) 明确 Lean 定理、可执行证书检查器、数值后端与外部 CUDA/FFI 处于不同信任层级。证明 exact tape 在 ℝ 上符合导数不等于 Float/CUDA 实际执行已证明。

### 分布式协议与政府采购的不同证据类型

- Veil [FloodSet 示例](https://github.com/verse-lab/veil/blob/main/Examples/Tutorial/FloodSet.lean) 是**同步、crash-fault、fail-stop 协议**，不能被 L2 宽泛“BFT 共识”概括为 arbitrary Byzantine 容错。
- Resonate [spec](https://github.com/resonatehq/resonate-specification) 自述 92 项性质、31 项无界证明、61 项仍开放，其 `valid/` checker 的轨迹验证也不自动升级为服务器全系统 correctness。
- OCDS [标准仓库](https://github.com/open-contracting/standard) 实际存在采购 release、contract amendment 与合并 record 资料，可以做结构/时间血缘研究；它是 `DOMAIN_REFERENCE_IMPLEMENTATION / LEAN_GAP`，不应称已有 Lean 法律合规证明。

## 5. 完成边界和下一步

- **结构核验 PASS**：8 个既有 P0 L2 父节点被拆成 27 个唯一 L3 条目，另 1 个 L3 拆成 2 个 L4；不增加新一级行业/项目数量指标。
- **来源级 E1 PASS / 研究闭合 PARTIAL**：每个 L3/L4 都有原始研究/项目文档与实际 GitHub 项目/代码路径；部分目录级路径仍是 README 指向，不能算“代码精确证明位置已独立审计”。
- **NOT_RUN**：任何外部项目源码审计、axiom/sorry 核验、clean build、论文结果独立复现、最小原型、生产实现或交易。
- **D0**：延续原 Goal，Scope/Non-goals/AC 不变。
- **唯一下一步**：将 Batch5 的 9 条 P0 父节点加入全局 triage 的 `L3_MAPPING_E1`，然后从剩余未深入的 P0 中挑出最具独立业务问题与项目来源的分支继续深入；已细拆节点需要进一步核对旧版/新层/证明目标差异并决定何时只算研究映射闭合。
