# TOPIC-018｜论文、官方文档与项目来源

> 来源分为官方技术文档、原始论文/预印本、项目源码和二手导航。每轮需记录访问日期、版本、是否全文读取及可复现状态。

## Lean / Mathlib / 工具链

1. [The Lean Language Reference](https://lean-lang.org/doc/reference/latest/) — 官方语言参考；当前页面显示版本 4.37.0-rc1。需区分 release 与 RC。
2. [Lean 安装手册](https://lean-lang.org/install/manual/) — 官方安装说明，明确 Elan 是 Lean version manager。
3. [Managing Toolchains with Elan](https://lean-lang.org/doc/reference/latest/Build-Tools-and-Distribution/Managing-Toolchains-with-Elan/) — Elan 命令与工具链管理。
4. [Mathlib 官网](https://mathlib.org/) — 社区数学库入口。
5. The mathlib Community, [The Lean Mathematical Library](https://doi.org/10.1145/3372885.3373824), CPP 2020；[arXiv:1910.09336](https://arxiv.org/abs/1910.09336)。
6. [Lean Projects Registry](https://leanprover-community.github.io/lean_projects.html) — Mathlib 下游项目代表性目录和早期项目意向。

## 数学形式化

7. [Liquid Tensor Experiment](https://github.com/leanprover-community/lean-liquid) — Lean 形式化项目与 Blueprint。
8. [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) — 数学猜想形式化声明集合；逐条证明状态待审计。
9. [Lean Blueprint](https://github.com/PatrickMassot/leanblueprint) — Lean 项目数学 Blueprint 生成工具。

## 软件验证与密码学

10. [Aeneas 项目页](https://aeneasverif.github.io/projects/) — Charon 与 Aeneas 工具链，支持包括 Lean 在内的多个验证后端。
11. Klaus, Tolmach & Conejero, [A Rust-to-Lean Verification Pipeline with AI Provers: An Experience Report](https://arxiv.org/abs/2605.30106), 2026。
12. [Verified-zkEVM/rust-lean](https://github.com/Verified-zkEVM/rust-lean) — Rust 组件到 Lean 的形式化验证案例集合。
13. [Verified-zkEVM/ArkLib](https://github.com/Verified-zkEVM/ArkLib) — Lean 4 SNARK 形式化库。

## 经济学与金融数学

14. [MathEconLib](https://mathecon.dev/) — 经济学共享形式化基础及初学者手册。
15. [gametheoryinlean/EconCSLib](https://github.com/gametheoryinlean/EconCSLib)；Bei et al., [arXiv:2606.16144](https://arxiv.org/abs/2606.16144)。
16. [nikhgarg/EconCSLib](https://github.com/nikhgarg/EconCSLib)；Garg, [arXiv:2606.13306](https://arxiv.org/abs/2606.13306)。与上一个同名但独立的项目，不可混为一谈。
17. [danlyng/Econlib](https://github.com/danlyng/Econlib) — 经济与政治理论 Lean 4 库。
18. [MathFin](https://formal-applied-math.github.io/formal-mathfin/index.html)；Coelho, [A Formally Verified Library of Mathematical Finance in Lean 4](https://arxiv.org/abs/2606.01356)。

## AI / 物理 / 其他

19. George et al., [TorchLean: Formalizing Neural Networks in Lean](https://arxiv.org/abs/2602.22631), 2026。
20. Davis, [Tutorial for the Lean 4 Library physicslib4](https://kellyjdavis.github.io/aqft/physicslib4-tutorial/), 2026-11-01。
21. [physicslib/physicslib4](https://github.com/physicslib/physicslib4) — 物理数学基础形式化项目。
22. [FormalQFT](https://github.com/FormalQFT)；Douglas et al., [Formalization of QFT](https://arxiv.org/abs/2603.15770), 2026。
23. [EconLib4](https://edu-ap.github.io/EconLib4/) — 信息论、编码理论等跨模块候选，需独立源码审计。
24. [sarvalabs/ifp](https://github.com/sarvalabs/ifp) — Veil/Lean 分布式协议验证候选案例，待核定理与状态。

## 来源质量要求

- 原始论文优先于新闻/博客；官方项目文档优先于二手介绍。
- GitHub 项目存在、README 介绍、论文摘要、源码 theorem、CI 构建、独立复现是不同证据级别。
- 对预印本注明 preprint；对动态网站数字注明访问日期。
- 不能从项目名称或摘要推断其完整功能、成熟度、许可或实际可构建性。


## Rust→Lean / Hax / Aeneas 新增来源

25. [Hax PR #1925](https://github.com/cryspen/hax/pull/1925) — 为 \`cast_op\` 添加显式类型标注，关闭整数转换与 shift 的类型推断问题。
26. [Hax PR #1927](https://github.com/cryspen/hax/pull/1927) — 保留 Rust crate/module 小写命名。
27. [Hax PR #1933](https://github.com/cryspen/hax/pull/1933) — \`specset int/bv\` 与 \`hax_mvcgen\`，分离数学整数规格与位向量规格。
28. [Hax PR #1938](https://github.com/cryspen/hax/pull/1938) — Lean backend 默认 proof 和 proof method attribute。
29. [Hax PR #1959](https://github.com/cryspen/hax/pull/1959) — 官方 ADC example，展示 \`hax_mvcgen\`、\`specset bv\` 与 \`bv_decide\`。
30. [Hax PR #2064](https://github.com/cryspen/hax/pull/2064) — Lean backend 名称调整。
31. [Hax PR #2142](https://github.com/cryspen/hax/pull/2142) — \`cargo hax into lean\` 默认生成完整 Lean package。
32. [Hax-FRI Phase 2 Report](https://github.com/Verified-zkEVM/rust-lean/blob/49a83d2a231c24f8a26a694ca2badaa36fb3914d/hax-FRI/PHASE2_REPORT.md) — Hax extraction、FRI 局部定理与后端缺口报告。
33. [Aeneas FRI fold-arity README](https://github.com/Verified-zkEVM/rust-lean/blob/49a83d2a231c24f8a26a694ca2badaa36fb3914d/aeneas-FRI/fold_arity_lean/README.md) — 同源 Rust 函数的 MIR/LLBC→Lean 证明案例。
34. [Hax ADC historical PoC](https://github.com/runtimeverification/hax-annotations-adc-verification) — 32-bit limb addition with carry 的原始示例；README 中的 Issue 清单为历史记录，需结合上游 PR 状态阅读。

## 数学金融与量化形式化新增来源

35. [formal-mathfin repository](https://github.com/formal-applied-math/formal-mathfin) — Lean 4 数学金融库、README corpus summary、使用和贡献说明。
36. [Coelho et al., arXiv:2606.01356](https://arxiv.org/abs/2606.01356) — MathFin 论文。
37. [MathFin formalization status](https://github.com/formal-applied-math/formal-mathfin/blob/cbe842dda1e71fd7173f3325971796686dbf7feb/docs/coverage.md) — full/library_wrapper/reduced_core/placeholder 分类。
38. [MathFin axiom audit generator](https://github.com/formal-applied-math/formal-mathfin/blob/cbe842dda1e71fd7173f3325971796686dbf7feb/MathFin/AxiomAuditGen.lean) — benchmark-cited declaration 的公理闭包审计。
39. [Rockafellar–Uryasev Gaussian CVaR](https://github.com/formal-applied-math/formal-mathfin/blob/cbe842dda1e71fd7173f3325971796686dbf7feb/MathFin/Risk/RockafellarUryasev.lean) — pointwise certificate proof。
40. [Markowitz Lagrangian FOC](https://github.com/formal-applied-math/formal-mathfin/blob/cbe842dda1e71fd7173f3325971796686dbf7feb/MathFin/Choice/Portfolio/MarkowitzLagrangian.lean) — KKT sufficiency。
41. [CRR characteristic-function convergence](https://github.com/formal-applied-math/formal-mathfin/blob/cbe842dda1e71fd7173f3325971796686dbf7feb/MathFin/Models/Binomial/CRRCharFun.lean) — characteristic functions and Lévy continuity。
42. [Gaussian risk report example](https://github.com/formal-applied-math/formal-mathfin/blob/cbe842dda1e71fd7173f3325971796686dbf7feb/MathFinExamples/Applications/GaussianRiskReport.lean) — worked portfolio risk report with explicit model limitations。
43. [MathFin build workflow](https://github.com/formal-applied-math/formal-mathfin/blob/cbe842dda1e71fd7173f3325971796686dbf7feb/.github/workflows/build.yml) — Python gates, lake build and axiom audit。

## PIT / No-Lookahead 形式化原型

44. [PITNoLookahead.lean](https://github.com/fweiger/AI_book/blob/topic/TOPIC-018/lean-formal-verification-20261122/topics/lean-formal-verification/examples/pit-no-lookahead/PITNoLookahead.lean) — eventTime / availableAt / decisionTime 的最小时间可得性规格。
45. [PIT proof README](https://github.com/fweiger/AI_book/blob/topic/TOPIC-018/lean-formal-verification-20261122/topics/lean-formal-verification/examples/pit-no-lookahead/README.md) — 定理范围和明确限制。
46. [PIT proof GitHub Actions](https://github.com/fweiger/AI_book/blob/topic/TOPIC-018/lean-formal-verification-20261122/.github/workflows/lean-pit-no-lookahead.yml) — Lean 4.35.0 独立构建工作流。


## 本轮新增的领域论文与项目来源（2026-11-22）

47. [CSLib: The Lean Computer Science Library](https://arxiv.org/abs/2602.04846) — Lean 计算机科学基础库的论文与项目说明。
48. [Verifying Datalog Reasoning with Lean](https://doi.org/10.4230/LIPIcs.ITP.2025.36) — ITP 2025，Datalog 证明证书的 Lean checker。
49. [LeanLTL: A Unifying Framework for Linear Temporal Logics in Lean](https://doi.org/10.4230/LIPIcs.ITP.2025.37) — ITP 2025，有限/无限 trace 的时序逻辑框架。
50. [Veil: A Framework for Automated and Interactive Verification of Transition Systems](https://doi.org/10.1007/978-3-031-98682-6_2) — CAV 2025，Lean transition-system verifier。
51. [Foundational Multi-Modal Program Verifiers](https://doi.org/10.1145/3776719) — POPL 2026，Lean 中的多模态程序验证器及 soundness 证明。
52. [Verdi: A Framework for Formally Verifying Distributed System Implementations](https://doi.org/10.1145/2737924.2737958) — PLDI 2015，Coq 分布式系统验证。
53. [IronFleet: Proving Practical Distributed Systems Correct](https://doi.org/10.1145/2815400.2815428) — SOSP 2015，Dafny/TLA 风格分布式系统验证。
54. [Raft: In Search of an Understandable Consensus Algorithm](https://www.usenix.org/conference/atc14/technical-sessions/presentation/ongaro) — USENIX ATC 2014，Raft 原始论文。
55. [VCVio: Verified Cryptography in Lean via Oracle Effects and Handlers](https://eprint.iacr.org/2026/899) — IACR ePrint 2026/899，Lean 密码学形式化。
56. [Aligning Information Theory and Formal Verification: A Lean Formalization of Rate-Distortion Theory](https://arxiv.org/abs/2610.22404) — 有限字母表 rate-distortion 的 Lean formalization。
57. [LeanInfoTheory](https://github.com/serhatemrecoban/LeanInfoTheory) — v0.2.0 README 声明 811 declarations / 57 modules；toolchain v4.33.1。
58. [infotheorylib](https://github.com/matteonerini/infotheorylib) — 按 Cover–Thomas、El Gamal–Kim、Yeung 三套教材组织的信息论 Lean library。
59. [Statistical Learning Theory in Lean 4: Empirical Processes from Scratch](https://arxiv.org/abs/2602.02285) — ICML 2026，经验过程与泛化理论形式化。
60. [TorchLean: Formalizing Neural Networks in Lean](https://arxiv.org/abs/2602.22631) — 张量、神经网络执行、图变换与验证的 Lean 统一框架。
61. [LeanDojo-v2](https://arxiv.org/abs/2611.09048) — Lean 4 AI theorem-proving 的 repo tracing、训练、检索和推理框架。
62. [StatWhy: Formal Verification Tool for Statistical Hypothesis Testing Programs](https://doi.org/10.1007/978-3-031-98679-6_10) — CAV 2025，非 Lean 的统计程序前提/规格检查工具。
63. [StarV: A Qualitative and Quantitative Verification Tool for Learning-enabled Systems](https://github.com/V2A2/StarV) — CAV 2025，Python 神经网络与学习型 CPS 验证工具。
64. [Marabou](https://github.com/NeuralNetworkVerification/Marabou) — SMT-based 神经网络性质验证工具。
65. [α,β-CROWN](https://github.com/Verified-Intelligence/alpha-beta-CROWN) — GPU 加速神经网络验证与鲁棒性证书。
66. [HepLean: Digitalising high energy physics](https://doi.org/10.1016/j.cpc.2024.109457) — Computer Physics Communications 2025。
67. [A Formalization of the Generalized Quantum Stein's Lemma in Lean](https://arxiv.org/abs/2510.08672) — 量子假设检验与相对熵的 Lean 形式化。
68. [Foundations of Machine-Checked Control Theory in Lean](https://arxiv.org/abs/2607.19727) — Lyapunov stability、LaSalle 和 small-gain 的 Lean 形式化。
69. [Elements of Information Theory](https://doi.org/10.1002/047174882X) — Cover & Thomas，信息论经典教材。
70. [Lecture Notes on Network Information Theory](https://arxiv.org/abs/1001.3404) — El Gamal & Kim，网络信息论教材。
71. [Portfolio Selection](https://doi.org/10.1111/j.1540-6261.1952.tb01525.x) — Markowitz 1952，均值—方差组合理论。
72. [Optimization of Conditional Value-at-Risk](https://doi.org/10.21314/JOR.2000.038) — Rockafellar & Uryasev 2000，CVaR 优化。
73. [Option Pricing: A Simplified Approach](https://doi.org/10.1016/0304-405X(79)90015-1) — Cox, Ross & Rubinstein 1979，二项式期权定价。
74. [Mathlib Papers](https://mathlib.org/papers.html) — Mathlib 官方形式化论文索引。
75. [Resonate Specification](https://github.com/resonatehq/resonate-specification) — Lean abstract machine、服务 trace checker 与 TLA+ 对照模型。
76. [Interaction Finality Protocol](https://github.com/sarvalabs/ifp) — Veil/Lean 的 BFT safety case；README 声明的证明数量仅对应受限 Phase 1。
77. [btc-verified](https://github.com/ProofOfKeags/btc-verified) — Bitcoin 协议组件的 Lean 形式化项目；完整 fork-choice/consensus 仍需单独审计。
78. [LeanForControl](https://github.com/AnandGokhale/LeanForControl) — 独立控制理论 Lean 项目，toolchain v4.30.0-rc2。
79. [DynamicalSystems](https://github.com/mcdoll/DynamicalSystems) — Doll–Shames 控制理论论文对应 Lean 库，toolchain v4.36.0-rc2。
80. [MathEconLib](https://github.com/matheconlib/matheconlib) — 经济学共享形式化基础，当前重点微观理论。
81. [Econlib](https://github.com/danlyng/Econlib) — 经济学/政治理论 Lean 4 library；本轮仅完成 README/toolchain 审查。
82. [Physlib](https://github.com/leanprover-community/physlib) — 物理学数字化社区项目，包含 Physlib、PhyslibAlpha 与 QuantumInfo。
83. [KTAIT](https://github.com/giulioruffini/KTAIT) — Kolmogorov/algorithmic information theory 的 Lean 项目。


## 2026-11-23｜方向级论文与项目源码核验补充

84. Zhang, Lee & Liu, [AI4SLT: Empirical Processes in Lean 4 for Formal Statistical Learning Theory](https://proceedings.mlr.press/v306/zhang26cd.html), ICML 2026 / PMLR 306 — 官方会议论文页；配套代码 [lean-stat-learning-theory](https://github.com/YuanheZ/lean-stat-learning-theory)。
85. Yan et al., [Aligning Information Theory and Formal Verification: A Lean Formalization of Rate-Distortion Theory](https://arxiv.org/abs/2610.22404), 2026 — 有限字母表率失真 formalization；配套代码 [rate_distortion_lean4](https://github.com/fubinyan/rate_distortion_lean4)。
86. Doll & Shames, [Foundations of Machine-Checked Control Theory in Lean](https://arxiv.org/abs/2607.19727), 2026 — Lyapunov stability 与 small-gain formalization；配套代码 [DynamicalSystems](https://github.com/mcdoll/DynamicalSystems)。
87. [TorchLean source repository](https://github.com/lean-dojo/TorchLean) — README 说明 Lean tensor/model definitions 复用于训练、图变换、证书检查和证明；当前 toolchain Lean 4.36.0。
88. [LeanInfoTheory v0.2.0 source](https://github.com/serhatemrecoban/LeanInfoTheory/tree/v0.2.0) — 811 supported declarations、57 modules；当前 master README 与 toolchain v4.33.1 已读取，正式复现应固定 release。
89. [HepLean repository](https://github.com/HEPLean/HepLean) — HepLean CPC 2025 论文的 companion repository；项目使用 Lean 4 数字化高能物理定义、定理、证明和计算。
90. [Veil 2.0](https://github.com/verse-lab/veil) 与 [IFP proof case](https://github.com/sarvalabs/ifp) — Veil 是 Lean transition-system verification framework；IFP README 明确 Phase 1 受限于两固定参与者、单 epoch。
91. [rate_distortion_lean4 MainResults.lean](https://github.com/fubinyan/rate_distortion_lean4/blob/main/MainResults.lean) — 主定理的 print axioms 和 Lean.collectAxioms allowlist 审计入口。
92. [MathFin current README](https://github.com/formal-applied-math/formal-mathfin/blob/main/README.md)、[CITATION.cff](https://github.com/formal-applied-math/formal-mathfin/blob/main/CITATION.cff)、[coverage.md](https://github.com/formal-applied-math/formal-mathfin/blob/main/docs/coverage.md) — 当前 corpus、软件 release、历史 coverage audit 的不同快照，禁止混为同一统计。


93. Yan, Dong, Shi, Wang & Shum, [Aligning Information Theory and Formal Verification: A Lean Formalization of Rate-Distortion Theory](https://arxiv.org/abs/2610.22404), arXiv:2610.22404, 2026 — rate-distortion finite-alphabet Lean formalization；companion [rate_distortion_lean4](https://github.com/fubinyan/rate_distortion_lean4)。
94. Zhang, Lee & Liu, [AI4SLT: Empirical Processes in Lean 4 for Formal Statistical Learning Theory](https://proceedings.mlr.press/v306/zhang26cd.html), ICML 2026 / PMLR 306:156234–156262 — official proceedings page directly links [lean-stat-learning-theory](https://github.com/YuanheZ/lean-stat-learning-theory)。
95. Pîrlea, Gladshtein, Kinsbruner, Zhao & Sergey, [Veil: A Framework for Automated and Interactive Verification of Transition Systems](https://doi.org/10.1007/978-3-031-98682-6_2), CAV 2025, LNCS 15933 — framework paper and [Veil repository](https://github.com/verse-lab/veil)。
96. Losa & Dodds, [On the Formal Verification of the Stellar Consensus Protocol](https://doi.org/10.4230/OASIcs.FMBC.2020.9), FMBC 2020 — original Ivy + Isabelle/HOL safety/liveness methodology; not the same as the narrower Veil Lean SCP example.
97. [stellar/scp-proofs](https://github.com/stellar/scp-proofs) — original SCP proof/model repository, Ivy + Isabelle/HOL; README distinguishes current Ivy 1.7 version from old commit 803b345 containing full liveness proof.


## 2026-11-23｜递归行业叶节点新增来源

### 硬件、编译器、GPU 与软件基础设施
- [RISC-V ISA Manual](https://github.com/riscv/riscv-isa-manual)；[Sail RISC-V Lean](https://github.com/opencompl/sail-riscv-lean)；[OpenVM-FV](https://github.com/openvm-org/openvm-fv)。
- [xv6iris formal verification](https://arxiv.org/abs/2609.04043)；[Formal Methods in Industry](https://doi.org/10.1145/3689374)。
- [TorchLean](https://arxiv.org/abs/2602.22631)。
- [AWS Cedar verification-guided development](https://aws.amazon.com/blogs/opensource/lean-into-verified-software-development/)；[Lean official Cedar case](https://lean-lang.org/use-cases/cedar/)。
- [Aeneas/Rust-to-Lean](https://arxiv.org/abs/2605.30106)；[Certifying Datalog, ITP 2025](https://doi.org/10.4230/LIPIcs.ITP.2025.36)；[LeanLTL, ITP 2025](https://doi.org/10.4230/LIPIcs.ITP.2025.37)；[Veil, CAV 2025](https://doi.org/10.1007/978-3-031-98682-6_2)。

### 密码学、金融与经济学
- [VCVio, IACR ePrint 2026/899](https://eprint.iacr.org/2026/899)；[MathFin research](https://arxiv.org/abs/2606.01356)。
- [Markowitz, Portfolio Selection (1952)](https://doi.org/10.1111/j.1540-6261.1952.tb01525.x)；[Rockafellar–Uryasev CVaR](https://doi.org/10.21314/JOR.2000.038)。
- [Probability of Backtest Overfitting](https://doi.org/10.21314/JCF.2016.322)；[The Seven Sins of Quantitative Investing](https://doi.org/10.3905/jpm.2019.1.069)。
- [EconCSLib research](https://arxiv.org/abs/2606.16144)；[economic mechanism formalization](https://arxiv.org/abs/2606.13306)。

### 交通、工业、医疗、能源与通信
- [SPIN railway control validation](https://doi.org/10.1109/ICDSN.2000.857524)；[ETCS interlocking verification](https://doi.org/10.1016/j.scico.2016.05.010)。
- [KeYmaera hybrid systems safety tutorial](https://doi.org/10.1007/s10009-015-0367-0)；[Code-Level Safety Verification for Automated Driving](https://doi.org/10.1007/978-3-031-71177-0_22)。
- [ESBMC-PLC+](https://arxiv.org/abs/2606.23870)；[PLC benchmark suite](https://arxiv.org/abs/2609.18994)；[Formal Verification of Control Modules in CPS](https://doi.org/10.3390/s20185154)。
- [Medical software formal methods review](https://doi.org/10.1002/smr.1943)；[ASM medical-device development](https://doi.org/10.1016/j.scico.2017.07.003)；[Open-source automated insulin delivery RCT](https://doi.org/10.1056/NEJMoa2203913)。
- [Systems Biology standards and best practices](https://pmc.ncbi.nlm.nih.gov/articles/PMC10435326/)。
- [P4 stateful packet processing verification](https://www.cs.princeton.edu/~appel/papers/FoundationalVerificationP4.pdf)；[P4 verification dissertation](https://doi.org/10.7298/a0dy-4f33)。
- [pandapower](https://doi.org/10.1109/TPWRS.2018.2829021)；[Grid2Op](https://github.com/Grid2op/Grid2op)。

### 科学、法律、选举与教育
- [Formalizing Chemical Physics Using Lean](https://doi.org/10.1039/d3dd00077j)；[LeanChemicalTheories](https://github.com/atomslab/LeanChemicalTheories)。
- [Lean control theory](https://arxiv.org/abs/2607.19727)；[FormalQFT](https://arxiv.org/abs/2603.15770)；[Quantum Stein lemma](https://arxiv.org/abs/2510.08672)。
- [Catala: a Programming Language for the Law](https://doi.org/10.1145/3473582)；[LegalLean project](https://github.com/edu-ap/legal-lean)。
- [ElectionGuard: A Cryptographic Toolkit to Enable Verifiable Elections](https://www.usenix.org/conference/usenixsecurity24/presentation/benaloh)；[ElectionGuard specification](https://electionguard.vote/spec/)。
- [Learning about Proof with Lean](https://doi.org/10.1007/s40753-021-00140-1)；[Teaching Mathematics with Lean](https://doi.org/10.1090/noti3184)；[Natural Number Game learning study](https://doi.org/10.1007/s40751-025-00193-w)。
- [LeanDojo](https://arxiv.org/abs/2306.15626)；[LeanCopilot](https://arxiv.org/abs/2404.12534)；[Mathlib paper](https://doi.org/10.1145/3372885.3373824)；[Formal Conjectures](https://arxiv.org/abs/2605.13171)。

**证据规则：** 上述来源并非都与 GitHub 项目一一对应的 companion paper。叶节点会分别标记直接论文、行业证据、标准、项目文档及尚未闭合的关系，不将一般形式化方法研究说成 Lean 采用。

- [HepLean: Digitalising high energy physics](https://doi.org/10.1016/j.cpc.2024.109457)；[PhysLib current project](https://github.com/leanprover-community/physlib)。
- [MoveIt Task Constructor for Task-Level Motion Planning, ICRA 2019](https://doi.org/10.1109/ICRA.2019.8793898)。
- [Large-eddy simulations with ClimateMachine v0.2.0](https://doi.org/10.5194/gmd-15-6259-2022)；ClimateMachine.jl README 标记旧仓库不再维护，后续资源转向 ClimaCore/ClimaAtmos/ClimaCoupler。

- [Hax: high-assurance translation of Rust into Lean/F*/Rocq](https://github.com/pereq-dev/hax)；README identifies Lean as one supported backend.

- [SP1-lean formal verification](https://github.com/succinctlabs/sp1-lean)；[Zisk-FV Lean project](https://github.com/eth-act/zisk-fv)；[OpenVM Lean verification announcement](https://blog.openvm.dev/fv)。
- [Hax Rust-to-Lean/F*/Rocq translator](https://github.com/pereq-dev/hax)；[Aeneas/Rust-to-Lean pipeline experience report](https://arxiv.org/abs/2605.30106)。
- [Black–Scholes (1973)](https://doi.org/10.1086/260062)；[Cox–Ross–Rubinstein (1979)](https://doi.org/10.1016/0304-405X(79)90015-1)。
- [HepLean: Digitalising high energy physics](https://doi.org/10.1016/j.cpc.2024.109457)；[Large-eddy simulations with ClimateMachine v0.2.0](https://doi.org/10.5194/gmd-15-6259-2022)。
