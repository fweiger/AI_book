# TOPIC-018｜Batch 6：6 个 P0 父节点向真实 Lean / GitHub 代码进一步下钻

> 日期：2026-11-23。规范任务：[AI_book #74](https://github.com/fweiger/AI_book/issues/74)；研究 PR：[Draft #75](https://github.com/fweiger/AI_book/pull/75)。
> 本轮从尚未进入 L3 的 13 个 P0 L2 中研究 6 个，新增 17 个 L3 问题级映射。连同 Batch4/5：23/30 个 P0 已至少继续一层，累计 60 个 L3、2 个 L4。原始 12 行业、60 初始父节点、124 个 L2 不变。
> **证据等级 E1_SOURCE_ANCHOR：** 本轮通过 GitHub 连接器实际读取外部仓库 README/对应 Lean 源文件或原始技术说明，交叉参考原始论文/发布说明；未在本轮执行外部 clean build、独立 theorem 审计、sorries/axiom 全局扫描或原型。下表中的具体性质是研究单元或定位到的源码符号，**不能由路径存在推断证明全链闭合**。

## 1. 本轮优先级与证据定义

- 先选有真实 Lean 代码、明显可进一步拆分、横跨多个行业的六个 P0：OpenVM RV32IM、Zisk RV64IM、EconCSLib 机制设计、LeanForControl 控制理论、LeanInfoTheory 信息论、Sparkle 芯片设计。
- 相关性标记：DIRECT_LEAN 是 Lean 代码研究；PRIMARY_TECH_DOC 是项目一手技术说明（不能冒充同行评审论文）；ORIGINAL_PAPER 是学术论文；SOURCE_DOC_ONLY 表示本轮只定位项目规格或文档，尚未找到对应单个 theorem 的确切源码。
- 不能把作者的构建、证书或 no-sorry 声明当成本轮独立构建或本轮审计 PASS。不能把 Lean 数学结论扩展为现实硬件、数据、机器人或市场应用安全。

## 2. 新增 17 个第三级节点：研究问题 → 性质 → 一手源码

| L3 ID | 父 L2 | 单一待验证问题 / 假设或性质 | 已读取的一手项目源码或规格 | 理论/论文或项目来源 | 证据级别与边界 |
|---|---|---|---|---|---|
| IND01-05-A-01 | IND01-05-A | RV32IM 的 ADD/ADDI 等 ALU 指令：满足提取的芯片行约束时，解码操作与 Sail/RISC-V 参考语义一致 | [OpenvmFv/Equivalence/Equivalence.lean](https://github.com/openvm-org/openvm-fv/blob/main/OpenvmFv/Equivalence/Equivalence.lean)，实际见 equiv_ADD、equiv_ADDI | [OpenVM FV 技术发布](https://blog.openvm.dev/fv)；[作者仓库说明](https://github.com/openvm-org/openvm-fv) | DIRECT_LEAN / SOURCE_FILE_READ。仅固定 OpenVM v2.0.0 所提取约束的指令级声明，不证明整个 zkVM |
| IND01-05-A-02 | IND01-05-A | RV32IM branch/jump opcode 的控制流转移与参考指令执行是否语义一致 | [Equivalence.lean](https://github.com/openvm-org/openvm-fv/blob/main/OpenvmFv/Equivalence/Equivalence.lean) 的 BranchEqual/BranchLessThan/JalLui/JalR 导入和分支 | [OpenVM FV 技术发布](https://blog.openvm.dev/fv) | DIRECT_LEAN / SOURCE_FILE_READ。控制流声明与跨多指令的全程序控制流正确性不同 |
| IND01-05-A-03 | IND01-05-A | RV32IM load/store 的位宽、符号扩展和内存语义与参考规格是否一致 | [Equivalence.lean](https://github.com/openvm-org/openvm-fv/blob/main/OpenvmFv/Equivalence/Equivalence.lean) 的 LoadStore/LoadSignExtend 导入及等价证明组织 | [原始仓库](https://github.com/openvm-org/openvm-fv)；[固定 OpenVM v2.0.0](https://github.com/openvm-org/openvm/tree/v2.0.0) | DIRECT_LEAN / SOURCE_FILE_READ。内存/状态总线假设必须保留，非整个 guest memory 安全证明 |
| IND01-05-C-01 | IND01-05-C | 给定已绑定 raw program 和 decoder 前提的执行 trace，Zisk 接受的步骤能否构造匹配 Sail 规格的执行步骤 | [ZiskFv/Compliance.lean](https://github.com/eth-act/zisk-fv/blob/main/ZiskFv/Compliance.lean) 的 zisk_riscv_compliant_program_bus 与 [根定理说明](https://github.com/eth-act/zisk-fv) | [zisk-fv README](https://github.com/eth-act/zisk-fv) | DIRECT_LEAN / SOURCE_FILE_READ。README 的 root_soundness 前提尚无 in-tree witnesses；项目警示不能推断 ZisK 生产安全 |
| IND01-05-C-02 | IND01-05-C | 每个可执行 RV64IM raw word 能否落入支持的解码枚举；真实 Zisk decode/lowering 完备是否已经构造 | [ZiskFv/Completeness.lean](https://github.com/eth-act/zisk-fv/blob/main/ZiskFv/Completeness.lean) 的 sail_executable_within_supported_decode_shape 与 skeletal_root_completeness | [zisk-fv README](https://github.com/eth-act/zisk-fv) | DIRECT_LEAN / SOURCE_FILE_READ。前者是独立的 Sail 支持形状结论；后者仍有 ZisK 端条件，不能称完整 completeness |
| IND01-05-C-03 | IND01-05-C | Aeneas 从生产 Rust decode/lowering 抽取出的 Lean 语义，是否已真正接入 main Lake proof root | [Compliance README](https://github.com/eth-act/zisk-fv/blob/main/ZiskFv/Compliance/README.md)；[仓库抽取与构建说明](https://github.com/eth-act/zisk-fv) | [zisk-fv README](https://github.com/eth-act/zisk-fv) | DIRECT_LEAN / TRUST_BRIDGE_GAP。单独 extraction harness 的成果未作为无条件证明接入主定理 |
| IND04-05-B-01 | IND04-05-B | 一般机制的占优策略激励相容（DSIC）与事后个体理性（ex-post IR）究竟分别如何定义 | [MechBasic.lean](https://github.com/gametheoryinlean/EconCSLib/blob/main/EconCSLib/MechanismDesign/Auction/MechBasic.lean) 的 IsDSIC、IsExPostIR、truthful_isNash | [EconCSLib 学术论文](https://arxiv.org/abs/2606.16144) | DIRECT_LEAN / SOURCE_FILE_READ。DSIC 和 IR 是两个不同约束，定义存在不能证明任意机制满足 |
| IND04-05-B-02 | IND04-05-B | 二价拍卖的真实出价是否弱占优，机制能否满足 DSIC | [Vickrey.lean](https://github.com/gametheoryinlean/EconCSLib/blob/main/EconCSLib/MechanismDesign/Auction/Vickrey.lean) 的 valuation_is_dominant、truthful_weakly_dominant、mechanism_isDSIC | [EconCSLib 论文](https://arxiv.org/abs/2606.16144)；Vickrey 1961 作为原始理论来源 | DIRECT_LEAN / SOURCE_FILE_READ。局限于文件中的二价拍卖、价值/支付/并列处理假设；不推广至动态机制 |
| IND04-05-B-03 | IND04-05-B | Bayesian 单物品拍卖的 allocation capacity、feasibility 与 expected seller revenue 如何分别形式化 | [BayesianSingleItem.lean](https://github.com/gametheoryinlean/EconCSLib/blob/main/EconCSLib/MechanismDesign/Auction/BayesianSingleItem.lean) 的 RespectsSingleItemCapacity、IsFeasible、expectedSellerRevenue | [EconCSLib 学术论文](https://arxiv.org/abs/2606.16144) | DIRECT_LEAN / SOURCE_FILE_READ。风险偏好、先验独立性、收入目标和最优拍卖证明需分别核，不因结构/定义存在称最优性已证 |
| IND06-03-B-01 | IND06-03-B | 给定 Lipschitz 等假设，控制系统 ODE 的积分曲线是否能在长时间区间存在且唯一 | [ODEs/PicardLindelof.lean](https://github.com/AnandGokhale/LeanForControl/blob/main/LeanForControl/ODEs/PicardLindelof.lean) 的 exists_isIntegralCurveOn_Icc 与唯一性相关引理 | [Foundations of Machine-Checked Control Theory in Lean](https://arxiv.org/abs/2607.19727)；Khalil, Nonlinear Systems | DIRECT_LEAN / SOURCE_FILE_READ。是数学动力学条件，未涉及执行器、传感噪声或机器人硬件 |
| IND06-03-B-02 | IND06-03-B | 正定/衰减 Lyapunov 证书可以推出哪一种一致/指数稳定性 | [Stability/Continuous/LyapunovTheorems.lean](https://github.com/AnandGokhale/LeanForControl/blob/main/LeanForControl/Stability/Continuous/LyapunovTheorems.lean) 的 IsUniformLyapunovFunction.uniformlyStable、IsExponentialLyapunovFunction.locallyExponentiallyStable | [控制理论论文](https://arxiv.org/abs/2607.19727)；[Stability plan](https://github.com/AnandGokhale/LeanForControl/blob/main/LeanForControl/Stability/plan.md) | DIRECT_LEAN / SOURCE_FILE_READ。证明结论依附明示系统与证书假设，非任意闭环控制系统安全 |
| IND06-03-B-03 | IND06-03-B | LaSalle 不变性与局部/全局渐近稳定的可用条件分别是什么 | [Stability/Continuous/LaSalle.lean](https://github.com/AnandGokhale/LeanForControl/blob/main/LeanForControl/Stability/Continuous/LaSalle.lean) 的 lasalle_invariance_principle、locallyAsymptoticallyStable_of_lasalle | [控制理论论文](https://arxiv.org/abs/2607.19727)；Khalil, Nonlinear Systems | DIRECT_LEAN / SOURCE_FILE_READ。ω-limit 集与不变集条件不自动覆盖采样控制、模型误差 |
| IND08-01-A-01 | IND08-01-A | 离散 PMF 的 Shannon entropy、非负性与零熵刻画怎样形式化 | [Shannon/Entropy.lean](https://github.com/serhatemrecoban/LeanInfoTheory/blob/main/LeanInfoTheory/Shannon/Entropy.lean) 的 entropy、entropy_nonneg、entropy_eq_zero_iff | [LeanInfoTheory v0.2.0 软件归档](https://doi.org/10.5281/zenodo.23973538)；Cover & Thomas 理论源 | DIRECT_LEAN / SOURCE_FILE_READ。软件归档不等于同行评审论文；仅相应有限离散信息理论假设 |
| IND08-01-A-02 | IND08-01-A | KL divergence 的支持集条件、零散度判别与真实值转换如何避免把无穷值误写成零 | [SemanticBridge/KL.lean](https://github.com/serhatemrecoban/LeanInfoTheory/blob/main/LeanInfoTheory/Shannon/SemanticBridge/KL.lean) 的 klDiv_pmf_ne_top_iff_support_subset、toReal_klDiv_pmf_eq_zero_iff | [LeanInfoTheory v0.2.0](https://doi.org/10.5281/zenodo.23973538) | DIRECT_LEAN / SOURCE_FILE_READ。ENNReal 转 Real 必须有支持/有限性守卫，不能忽略 KL=∞ |
| IND08-01-A-03 | IND08-01-A | 有限字母表解码错误概率与 Fano 不等式的形式化关系 | [Shannon/Fano.lean](https://github.com/serhatemrecoban/LeanInfoTheory/blob/main/LeanInfoTheory/Shannon/Fano.lean) 的 decodingErrorProbability、decodingErrorProbability_eq_sum 及 Fano 模块 | [LeanInfoTheory v0.2.0](https://doi.org/10.5281/zenodo.23973538) | DIRECT_LEAN / SOURCE_FILE_READ。理论误差界不代表一个高效/可运行 codec 的实现正确性 |
| IND01-02-A-01 | IND01-02-A | Round-robin 仲裁器的安全、不饥饿、工作保持三类规格应分别证明什么 | [Verification_Framework.md](https://github.com/Verilean/sparkle/blob/main/docs/reference/Verification_Framework.md) 的 bounded_wait_A、mutual_exclusion、work_conserving 示例 | [Sparkle 项目](https://github.com/Verilean/sparkle) | DIRECT_LEAN_PROJECT / SOURCE_DOC_ONLY。文件展示规格和证明模式，本轮未定位全部对应已编译硬件 theorem；不可宣称硬件整体正式验证 |
| IND01-02-A-02 | IND01-02-A | 从纯 Lean 规格到 Signal DSL，再到 SystemVerilog 生成，在哪一步才建立实现与规格的精化保证 | [SignalDSL_Syntax.md](https://github.com/Verilean/sparkle/blob/main/docs/reference/SignalDSL_Syntax.md)；[Verification_Framework.md](https://github.com/Verilean/sparkle/blob/main/docs/reference/Verification_Framework.md) | [Sparkle README](https://github.com/Verilean/sparkle) | DIRECT_LEAN_PROJECT / SOURCE_DOC_ONLY。可综合/生成 Verilog 不是形式等价性或 FPGA 电气时序的自动证明 |

## 3. 论文、项目和定理的关键纠偏

1. **OpenVM:** 作者仓库报告 RV32IM 45 opcode 的证明；同库还提及 Keccak/SHA2 precompile，但二者不属于 RV32IM REPORT.pdf 覆盖，不能把源码/报告范围混用。提取器和 Sail 参考语义都在证明信任边界内；不是端到端 zkVM 安全认证。
2. **Zisk:** 根 soundness 的 raw program binding / decoder premise 尚无主树内实例；完整的 ZisK 端 completeness 是条件性工作。项目 README 直接警告尚不能为 ZisK RV64IM 安全背书。
3. **EconCSLib:** [gametheoryinlean/EconCSLib](https://github.com/gametheoryinlean/EconCSLib) 与 [nikhgarg/EconCSLib](https://github.com/nikhgarg/EconCSLib) 是独立仓库，不可按名称合并；论文与当前代码的具体 theorem 关系只按实际找到的文件陈述。
4. **LeanForControl:** 文章是领域理论来源，项目和论文之间的具体逐定理 companion 关系未由本轮一项项核实；Lean 下的 Lyapunov 数学稳定性与物理机器人控制器验证是两个层面。
5. **LeanInfoTheory:** 软件 DOI/Zenodo 是版本引用而非同行评审论文，当前 v0.2.0 适用范围为有限离散信息理论，canonical units 是 nats，实际通信链路/压缩软件属于下游应用。
6. **Sparkle:** 其源文档明确“规格证明 → Signal DSL 实现 → Verilog 生成”并把 refinement 列为可选步骤；若没有针对某个 IP 的连接证明，不得把 pure spec theorem 当成 Verilog 完整正确性证明。

## 4. 本批结构统计、剩余工作与验收

- Batch4：8 P0 L2 → 16 L3；Batch5：9 新 P0 L2 → 27 L3 / 2 L4；**Batch6：6 新 P0 L2 → 17 L3**。不同 P0 父节点之间不重合，累计 **23/30 P0 进入 L3，60 L3，2 L4**。
- 剩余 7 个未进入 L3 的 P0：IND03-05-B（IFP 协议）、IND04-04-B（PIT 历史股票池）、IND10-04-A（SciLean）、IND11-01-A（LegalLean）、IND11-02-B（Concerto/LEAN_GAP）、IND07-03-B（CGM 控制/LEAN_GAP）、IND10-06-A（ClimaCore/LEAN_GAP）。
- 本轮 17 个 L3 都有父节点、单一问题、来源链接、实际 Github 项目/文件路径以及证据边界。只有部分目标已定位到具体 theorem 或结构定义；对作者声明的构建结果不做本轮独立结论。
- **本轮验收**：source-level mapping PASS；外部仓库 clean build、独立 proof/kernel/axiom 检查、方法实现 QA、原型为 NOT_RUN；AC-03/AC-07 整体 PARTIAL；原 Goal/Scope/AC 保持不变（D0）。
- **下一候选动作**：依主线处理余下 7 P0 中能继续找到直接 Lean 源码的 IFP / SciLean / LegalLean，并对 PIT、Concerto、CGM、ClimaCore 建立清晰的行业实现→规格→Lean 缺口三段映射；之后复核已经下钻的 23 个 P0 是否真正达到单问题证据闭合。不转入外部审计。
