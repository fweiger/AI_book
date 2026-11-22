# Lean 跨学科研究方向—论文—开源项目证据矩阵

**版本：0.1.0-draft｜审查日期：2026-11-22｜所属专题：TOPIC-018 / Issue #74**

本文件回答三个连续问题：

1. 一个学科中，哪些具体研究方向适合形式化？
2. 每个方向有哪些原始论文、理论来源或 Lean 形式化论文？
3. 是否存在 Lean 项目；若没有，是否有 Coq/Rocq、Isabelle、Dafny、TLA+、SMT 或普通开源实现可借鉴？

本轮是有来源的首轮地图，不是所有项目的完整构建审计。每个仓库仍需固定 commit、许可证、依赖和 theorem 状态后才能升级为可复现实验。

## 0. 证据口径与项目分类

### 0.1 证据等级

| 等级 | 含义 | 可作出的结论 |
|---|---|---|
| E0 | 搜索发现、索引或二手提及 | 仅是候选线索 |
| E1 | 读取原始论文、官方 README 或官方项目文档 | 可描述项目目标和作者声称的范围 |
| E2 | 进一步读取源码、toolchain、Lake 配置、CI 日志或具体定理 | 可描述被检查的代码/构建状态，但不代表本地独立复现 |
| E3 | 在隔离环境固定 commit 后独立构建并复核 theorem/axiom | 可称为独立复现 |

本轮外部项目大多为 E1/E2；TOPIC-018 自己的 PIT 最小 Lean package 在 GitHub Actions 上通过了构建，属于 E2 / CI PASS，尚未做另一环境的 E3 独立复现。

### 0.2 项目类型

- **Lean library**：领域定义、引理和定理直接写在 Lean 中。
- **Lean verifier / framework**：提供程序、状态机、协议或神经网络的规格和验证方法。
- **Extraction / refinement bridge**：从 Rust 等源程序抽取到 Lean，再验证抽取语义或规格。
- **Adjacent prover**：使用 Rocq/Coq、Isabelle/HOL、F*、Dafny、TLA+、Why3 或 SMT；可借鉴，但不能标成 Lean 项目。
- **Ordinary implementation**：Python/C++/Rust 等实现或实验代码；可以作为对照，不能等同于机器检查证明。

### 0.3 论文类型

- **T**：领域理论论文/经典结果。
- **F**：形式化、证明助手或形式验证论文。
- **A**：相邻证明助手/验证工具论文。

形式化论文证明的是它精确编码的命题；自然语言到形式化定义的翻译仍需领域专家检查。

## 1. 总览矩阵

| 领域 | 主要研究方向 | Lean 项目/框架 | 其他相似项目 | 本轮判断 |
|---|---|---|---|---|
| 数学基础 | 分析、概率、代数、数论、形式化猜想 | Mathlib、Formal Conjectures、Liquid Tensor | 其他证明助手主要作为对照 | Lean 生态最成熟的基础层 |
| 计算机科学与软件验证 | 程序语义、Rust、Datalog、LTL、程序正确性 | CSLib、Aeneas、Hax、Veil、Loom、Velvet、Lentil、CertifyingDatalog | Verdi、IronFleet、TLA+ | 有成熟框架，但模型到真实实现仍需精化证据 |
| 密码学与零知识 | 安全游戏、SNARK/IOP、多项式承诺、实现正确性 | VCVio、ArkLib、CompPoly、Aeneas/Hax、rust-lean | EasyCrypt、Fiat-Crypto、HACL* | Lean 项目已覆盖多个层次，协议到实现的桥接仍是难点 |
| 分布式系统 | BFT、共识、安全/活性、状态机、事件驱动系统 | Veil、IFP、Lentil、Resonate Specification、btc-verified | Verdi、IronFleet、Raft/TLA+ | 找到真实 Lean BFT 案例；尚未确认完整 Lean Raft/Paxos 证明 |
| 经济学与博弈论 | 均衡、匹配、拍卖、机制设计、社会选择、宏观与计量 | MathEconLib、两套不同的 EconCSLib、Econlib | SocialChoiceLean 等早期项目 | 微观/计算经济学基础正在形成；宏观和计量覆盖较弱 |
| 金融数学与量化金融 | 随机分析、定价、组合、风险、PIT、回测 | MathFin、BrownianMotion、TOPIC-018 PIT 原型 | AFP actuarial mathematics、StatWhy | 数学金融已有大型库；经验回测和市场数据语义仍是明显空白 |
| AI/ML 与统计学习 | 泛化界、经验过程、神经网络语义、鲁棒性、证明 Agent | AI4SLT、TorchLean、LeanDojo-v2、LeanCopilot | StatWhy、StarV、Marabou、α,β-CROWN | 既有学习理论证明库，也有模型验证框架 |
| 物理学与量子信息 | 高能物理、量子场论、量子假设检验 | Physlib、PhyslibAlpha、QuantumInfo、physicslib4 | 其他数学物理证明助手项目 | 领域项目已存在，但子领域与代码库仍有分化 |
| 信息论与编码理论 | 熵、KL、互信息、数据处理、Fano、信道、率失真 | LeanInfoTheory、infotheorylib、rate_distortion_lean4、KTAIT | Rocq/Coq infotheo | 从基础 Shannon 理论扩展到率失真，发展速度很快 |
| 控制与网络化物理系统 | Lyapunov、LaSalle、小增益、输入输出稳定、混合系统 | LeanDynamicalSystems、LeanForControl、TorchLean | VeriDrone、KeYmaera X、Isabelle/HOL | Lean 控制理论已有可引用的代表性论文和开源库 |

## 2. 各领域研究方向、论文和项目

### 2.1 数学基础与大型形式化证明

**研究方向**
1. 实分析、拓扑、测度论与概率基础。
2. 代数、数论、表示论和几何。
3. 大型数学猜想与长证明的逐步形式化。
4. 随机过程、测度扩张、极限定理等跨领域基础。

**代表论文/理论**
- [The Lean Mathematical Library](https://doi.org/10.1145/3372885.3373824)（CPP 2020，F）：Mathlib 的协作式数学库设计。
- [Mathlib Papers](https://mathlib.org/papers.html)：官方形式化论文索引，包含正则素数情形的 Fermat's Last Theorem、Ionescu–Tulcea 定理、zeta/L-functions 等。
- [Liquid Tensor Experiment](https://github.com/leanprover-community/lean-liquid)：大型数学证明工程案例；它是项目/证明工程案例，不应将其等同于某一篇单独的论文。

**Lean 项目**
- [Mathlib](https://github.com/leanprover-community/mathlib4)：核心数学基础设施。
- [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures)：数学猜想的机器可读声明与证明任务集合。
- [Liquid Tensor Experiment](https://github.com/leanprover-community/lean-liquid)：大型证明依赖工程。

**当前缺口**
- 项目数量多不代表每个数学分支都已覆盖。
- 需要按具体定理和依赖追踪，不以仓库 README 或 theorem 数量代替证明范围审计。
- 该领域是其他九个领域的共同底座，不应与应用领域的实际验证混为一谈。

### 2.2 计算机科学、程序语义与软件验证

**研究方向**
1. 程序语义、状态转换系统和 Hoare logic。
2. Rust 内存/借用语义、抽取与实现精化。
3. Datalog、规则引擎和可验证证书。
4. LTL/时序逻辑、并发程序和协议不变量。
5. 统一的多模态验证器：模型检查、SMT 与交互式证明。

**代表论文**
- [CSLib: The Lean Computer Science Library](https://www.cslib.io/)（2026，F）：面向 Lean 计算机科学理论与工具的共享基础。
- [Verifying Datalog Reasoning with Lean](https://doi.org/10.4230/LIPIcs.ITP.2025.36)（ITP 2025，F）：使用 Lean 验证 Datalog 证明树/DAG 检查器。
- [LeanLTL: A Unifying Framework for Linear Temporal Logics in Lean](https://doi.org/10.4230/LIPIcs.ITP.2025.37)（ITP 2025，F）：将多种线性时序逻辑统一到 Lean。
- [Veil: A Framework for Automated and Interactive Verification of Transition Systems](https://doi.org/10.1007/978-3-031-98682-6_2)（CAV 2025，F）：将状态机建模、模型检查、SMT 与交互式证明结合。
- [Foundational Multi-Modal Program Verifiers](https://doi.org/10.1145/3776719)（POPL 2026，F）：多模态验证器的基础框架。
- [A Rust-to-Lean Verification Pipeline with AI Provers: An Experience Report](https://arxiv.org/abs/2605.30106)（2026，F）：Rust 到 Lean 的验证流水线与 AI 辅助证明经验。

**Lean 项目**
- [CSLib](https://github.com/leanprover/cslib)：通用计算机科学理论与工具接口。
- [CertifyingDatalog](https://github.com/knowsys/CertifyingDatalog)：Lean 证明的 Datalog 证书检查器。
- [LeanLTL](https://github.com/UCSCFormalMethods/LeanLTL)：LTL/LTLf 等逻辑的形式化；本轮读取的 toolchain 为 Lean 4.17.0-rc1，版本较旧。
- [Lentil](https://github.com/verse-lab/Lentil)：LTL 语义、规则和专用证明模式；toolchain 固定 Lean 4.35.0。
- [Loom](https://github.com/verse-lab/loom)：可执行语义、弱前置条件和多模态验证器生成。
- [Veil](https://github.com/verse-lab/veil)：面向状态转换系统与分布式协议的 Lean 验证框架。
- [Velvet](https://github.com/verse-lab/velvet)：Lean 内嵌的命令式程序验证器，支持部分/完全正确性、ghost state、测试和证明。
- [Aeneas](https://aeneasverif.github.io/) / [Hax](https://github.com/cryspen/hax)：Rust 源码到形式化后端的桥接路线。

**相邻项目**
- [Verdi](https://github.com/uwplse/verdi)（Coq）：分布式系统实现的模块化正确性证明。
- [IronFleet](https://github.com/Microsoft/Ironclad)（Dafny）：将 TLA 风格状态机精化与命令式程序证明结合。
- TLA+：适合协议规格与状态空间模型检查。

**当前缺口**
- 抽取文件可编译，不等于原始 Rust 实现已经被证明满足目标协议。
- 模型检查通过不等于无界状态空间的完整证明。
- 需要明确每个项目的 source semantics、模型假设、证明后端与 refinement boundary。

### 2.3 密码学与零知识证明

**研究方向**
1. 安全游戏、oracle/query 语义与归约证明。
2. SNARK、IOP、Polynomial Commitment、有限域和多项式代数。
3. Rust 密码学实现的功能正确性与安全属性。
4. 证明系统组件的组合、soundness 和可信计算基审计。

**代表论文**
- [VCVio: Verified Cryptography in Lean via Oracle Effects and Handlers](https://eprint.iacr.org/2026/899)：Lean 中基于 oracle effects/handlers 的密码学形式化路线。
- [A Rust-to-Lean Verification Pipeline with AI Provers](https://arxiv.org/abs/2605.30106)：可作为具体密码学实现到 Lean 的工程入口。

**Lean 项目**
- [VCVio](https://github.com/Verified-zkEVM/VCVio)：Lean 密码学与 oracle effects/handlers。
- [ArkLib](https://github.com/Verified-zkEVM/ArkLib)：Lean 4 的 SNARK/IOP 相关形式化库。
- [CompPoly](https://github.com/Verified-zkEVM/CompPoly)：多项式和相关代数基础。
- [rust-lean](https://github.com/Verified-zkEVM/rust-lean)：Hax/Aeneas Rust→Lean 对照案例。
- [Hax](https://github.com/cryspen/hax) 与 [Aeneas](https://github.com/AeneasVerif/aeneas)：面向 Rust 的抽取/验证工具链。

**相邻项目**
- [EasyCrypt](https://github.com/EasyCrypt/easycrypt)：密码学安全证明。
- [Fiat-Crypto](https://github.com/mit-plv/fiat-crypto)：经过形式化验证的密码学原语生成。
- [HACL*](https://github.com/hacl-star/hacl-star)：F* 验证的密码学实现。

**当前缺口**
- 协议级 soundness、安全游戏、实现级正确性和部署配置是不同证明目标。
- 需要逐项审计外部公理、opaque、抽取假设与实际实现之间的桥接。

### 2.4 分布式系统、共识与状态机

**研究方向**
1. BFT safety：诚实节点不能对冲突值作出决定。
2. Liveness：系统在明确公平性/网络假设下最终推进。
3. Leader election、replicated log、quorum intersection。
4. 动态成员、epoch reconfiguration、网络消息丢失/乱序/重复。
5. 服务端状态机、事件驱动工作流和 trace conformance。

**代表论文**
- [Veil: A Framework for Automated and Interactive Verification of Transition Systems](https://doi.org/10.1007/978-3-031-98682-6_2)（CAV 2025，F）。
- [Verdi: A Framework for Formally Verifying Distributed System Implementations](https://doi.org/10.1145/2737924.2737958)（PLDI 2015，A）。
- [IronFleet: Proving Practical Distributed Systems Correct](https://doi.org/10.1145/2815400.2815428)（SOSP 2015，A）。
- [In Search of an Understandable Consensus Algorithm](https://www.usenix.org/conference/atc14/technical-sessions/presentation/ongaro)（USENIX ATC 2014，T）。

**Lean 项目**
- [Veil](https://github.com/verse-lab/veil)：状态转换系统框架，当前 README 与 toolchain 指向 Lean 4.35.0；同时支持模型检查、SMT 和 Lean 证明。
- [Interaction Finality Protocol (IFP)](https://github.com/sarvalabs/ifp)：Veil/Lean 的真实 BFT 协议案例。README 声称 103 个 safety invariants 中 93 个已机器验证；但当前证明阶段仍是两个固定参与者、单 epoch 的受限实例，不能描述成完整协议已证明。
- [Lentil](https://github.com/verse-lab/Lentil)：LTL 逻辑证明基础设施。
- [Resonate Specification](https://github.com/resonatehq/resonate-specification)：Lean executable abstract machine、属性目录、真实服务 trace checker，并有 TLA+ 模型；它是 durable execution 服务规格，不是 Raft/Paxos 共识实现。
- [btc-verified](https://github.com/ProofOfKeags/btc-verified)：Bitcoin 序列化、哈希、Merkle、交易、区块等组件的 Lean 机器检查；README 将 issuance/fork-choice 等共识保证列为后续目标，不能写成完整 Bitcoin consensus 已证明。

**相邻项目**
- Verdi（Coq）、IronFleet（Dafny）、Raft 的 TLA+ specification。
- 这些项目提供了成熟的协议证明方法，但证明助手和可信边界与 Lean 不同。

**当前缺口**
- 本轮没有找到可确认的完整 Lean Raft/Paxos 端到端证明。
- IFP 的 93/103 是项目 README 声明，仍需固定 commit、读取 theorem/CI 并独立 build。
- Resonate 的 trace conformance 不等于共识安全；btc-verified 的组件证明不等于完整链选择规则已验证。

### 2.5 经济学、博弈论与机制设计

**研究方向**
1. 偏好、效用、风险厌恶和概率分布。
2. Nash / Bayesian / sequential equilibrium。
3. Matching、stable marriage、auction 和 online allocation。
4. Incentive compatibility、revenue、social choice、fair division。
5. 宏观经济学、计量经济学和因果识别。

**代表论文**
- [EconCSLib: A Lean Library for Computational Economics and AI-Assisted Research](https://arxiv.org/abs/2606.16144)：以可复用领域基础设施为中心。
- [EconCSLib: AI-Assisted Lean Formalization for Economics & Computation Research](https://arxiv.org/abs/2606.13306)：以逐篇论文形式化、依赖 DAG、验证报告和人工审查界面为中心。
- 两篇论文明确说明这两个 EconCSLib 是独立项目、方向互补，不能因同名而合并。

**Lean 项目**
- [MathEconLib](https://github.com/matheconlib/matheconlib)：共享经济学数学基础；当前重点微观经济学，长期目标包含宏观与计量经济学。
- [gametheoryinlean/EconCSLib](https://github.com/gametheoryinlean/EconCSLib)：共享概念、博弈、机制设计、拍卖、匹配、社会选择与公平分配基础；README 固定 Lean 4.30.0。
- [nikhgarg/EconCSLib](https://github.com/nikhgarg/EconCSLib)：逐篇研究论文形式化工作流；论文报告 11 篇完整、3 篇部分形式化。该仓库本轮 README 未能通过 GitHub 文件接口读取，当前证据以论文为主。
- [Econlib](https://github.com/danlyng/Econlib)：政治经济学/经济理论库，覆盖偏好、概率、优化、博弈、机制设计、社会选择和一般均衡；本轮只读取 README/toolchain，未独立 build。
- 早期专项项目：[socialchoicelean](https://github.com/dominikpeters/socialchoicelean)、[combinatorial-games](https://github.com/vihdzp/combinatorial-games)。

**当前缺口**
- 微观理论、匹配、拍卖和机制设计的形式化基础相对丰富。
- 宏观经济学、计量识别、因果推断和真实经济数据分析仍需逐项找项目，不能因项目名称覆盖“economics”就推断已完成。

### 2.6 金融数学与量化金融

**研究方向**
1. 测度论概率、Brownian motion、Itô integral、martingale、SDE。
2. No-arbitrage、风险中性测度、期权定价与对冲。
3. Portfolio optimization、KKT、CVaR、固定收益与精算。
4. 经验金融：PIT 数据、历史修订、股票池时点、因子统计、交易成本、回测执行。

**代表论文**
- Coelho, [A Formally Verified Library of Mathematical Finance in Lean 4](https://arxiv.org/abs/2606.01356)（2026，F）：覆盖随机分析、定价、风险、组合和固定收益。
- Markowitz, [Portfolio Selection](https://doi.org/10.1111/j.1540-6261.1952.tb01525.x)（1952，T）。
- Rockafellar & Uryasev, [Optimization of Conditional Value-at-Risk](https://doi.org/10.21314/JOR.2000.038)（2000，T）。
- Cox, Ross & Rubinstein, [Option Pricing: A Simplified Approach](https://doi.org/10.1016/0304-405X(79)90015-1)（1979，T）。

**Lean 项目**
- [formal-mathfin](https://github.com/formal-applied-math/formal-mathfin)：依赖 Mathlib 和 [BrownianMotion](https://github.com/RemyDegenne/brownian-motion)，覆盖 Itô/Girsanov/SDE、衍生品定价、组合、风险和固定收益。
- [TOPIC-018 PIT package](examples/pit-no-lookahead/PITNoLookahead.lean)：本专题自己的最小 no-lookahead 规格，已由 GitHub Actions 构建通过。

**相邻项目**
- [Archive of Formal Proofs](https://www.isabelle.in.tum.de/afp/) 中的 actuarial mathematics 相关工作。
- [StatWhy](https://github.com/fm4stats/statwhy)：非 Lean 的统计假设检验程序规格/检查工具，见 AI/统计学习部分。

**关键版本差异**
- MathFin 论文 v4（2026-11-07）记录 804 个 benchmark results：766 full proofs、18 upstream restatements、20 reduced cores。
- 本轮读取的当前 GitHub README 记录 906 个结果：866 full、18 restatements、22 reduced cores。
- 这可能是论文快照之后仓库继续增长，不应直接视为矛盾或任选一个数字；正式复现必须固定 repo commit/release 并对齐论文版本。

**当前缺口**
- MathFin 是数学金融库，不是 A 股量化策略库。
- 本轮未发现成熟 Lean 项目直接形式化 A 股 Level-2 微观结构、因子 IC/IR、换手/冲击成本、组合回测或策略盈利。
- PIT 原型只证明 eligibility filter safety，不证明完整 latest-revision as-of join，也不证明供应商时间戳真实性或策略盈利。

### 2.7 AI/机器学习与统计方法

**研究方向**
1. Statistical learning theory、empirical process、concentration inequalities。
2. Generalization bounds、Rademacher/Gaussian complexity、Dudley's entropy integral。
3. 神经网络的张量/浮点语义、计算图变换、鲁棒性证书。
4. Learning-enabled systems、神经控制器和安全属性。
5. AI 辅助 Lean 定理搜索、数据集生成、证明 Agent。

**代表论文**
- [Statistical Learning Theory in Lean 4: Empirical Processes from Scratch](https://arxiv.org/abs/2602.02285)（ICML 2026，F）：Gaussian Lipschitz concentration、Dudley's entropy integral、localized least-squares sharp rates。
- [TorchLean: Formalizing Neural Networks in Lean](https://arxiv.org/abs/2602.22631)（2026，F）：统一模型语义、Float32、图变换、IBP/CROWN/LiRPA 风格验证和神经控制器。
- [LeanDojo-v2](https://arxiv.org/abs/2611.09048)（2026，F）：Lean repo tracing、SFT/GRPO、retrieval、proof search 和 Lean4Code。
- [LeanCopilot](https://github.com/lean-dojo/LeanCopilot)：AI theorem proving 辅助工具；可作为 LeanDojo-v2 的历史和相关组件线索。
- [StatWhy](https://doi.org/10.1007/978-3-031-98679-6_10)（CAV 2025，A）：检查统计假设检验程序是否明确列出适用条件。
- [StarV](https://github.com/V2A2/StarV)（CAV 2025，A）：Python 的神经网络与 learning-enabled cyber-physical systems 定性/定量验证。

**Lean 项目**
- [lean-stat-learning-theory](https://github.com/YuanheZ/lean-stat-learning-theory)：AI4SLT 论文对应代码；README 声称无 sorry/axiom/admit/native_decide，当前 toolchain v4.32.0。本轮未独立 build。
- [TorchLean](https://github.com/lean-dojo/TorchLean)：同一模型定义用于执行、训练、图转换、证书检查和证明。
- [LeanDojo-v2](https://github.com/lean-dojo/LeanDojo-v2)：Lean 证明自动化与数据/Agent 框架。

**相邻项目**
- [Marabou](https://github.com/NeuralNetworkVerification/Marabou)：SMT-based 神经网络验证。
- [α,β-CROWN](https://github.com/Verified-Intelligence/alpha-beta-CROWN)：GPU 加速的 bound propagation/branch-and-bound 验证器。
- StarV、StatWhy 提供非 Lean 的统计程序和学习系统验证思路。

**当前缺口**
- 统计学习理论的泛化界不等于金融策略收益保证。
- 形式化统计程序不等于证明样本来自假设分布。
- 神经网络鲁棒性证书不等于数据、训练过程、部署后行为都已被证明。
- 需要把数学 theorem、统计假设、实际数据和运行实现分层记录。

### 2.8 物理学、量子信息与数学物理

**研究方向**
1. 高能物理中的矩阵、对称性、异常抵消和 Higgs 相关计算。
2. Axiomatic QFT、operator algebra、GNS、谱理论。
3. Quantum information、relative entropy、hypothesis testing。
4. 物理模型定义、定理与计算的可追溯数字化。

**代表论文**
- [HepLean: Digitalising high energy physics](https://arxiv.org/abs/2405.08863)；后发表于 *Computer Physics Communications*，DOI [10.1016/j.cpc.2024.109457](https://doi.org/10.1016/j.cpc.2024.109457)。
- [A Formalization of the Generalized Quantum Stein's Lemma in Lean](https://arxiv.org/abs/2510.08672)（2025，F）：量子假设检验和相对熵，形式化经修正的证明路线。
- [Formalization of QFT](https://arxiv.org/abs/2603.15770)（2026，F）：量子场论相关形式化工作。

**Lean 项目**
- [Physlib](https://github.com/leanprover-community/physlib)：物理数字化的社区项目；包含 curated Physlib、快速贡献区 PhyslibAlpha，以及独立演进中的 QuantumInfo codebase。
- [physicslib4](https://github.com/physicslib/physicslib4)：Haag–Kastler 公理、GNS、Stone、Reeh–Schlieder、Tomita–Takesaki 等 axiomatic QFT。
- [Lean-QuantumInfo](https://github.com/Timeroot/Lean-QuantumInfo)：量子信息形式化案例。

**当前缺口**
- Physlib、QuantumInfo 和 physicslib4 是不同代码库/子项目，不能视为一个统一完成的物理库。
- 数学物理项目的证明结果不能自动转化为实验物理模型的经验有效性。

### 2.9 信息论、编码理论与算法信息论

**研究方向**
1. Shannon entropy、conditional entropy、mutual information、KL divergence。
2. Markov chains、data processing inequality、Fano inequalities、sufficient statistics。
3. Source coding、channel capacity、network information theory。
4. Rate-distortion、lossy compression、typicality、achievability/converse。
5. Algorithmic information theory 与 Kolmogorov complexity。

**代表论文/理论**
- [Aligning Information Theory and Formal Verification: A Lean Formalization of Rate-Distortion Theory](https://arxiv.org/abs/2610.22404)（2026，F）：有限字母表下 rate-distortion 的 direct/converse 与可复用定义。
- Cover & Thomas, [Elements of Information Theory](https://doi.org/10.1002/047174882X)（2006，T）。
- El Gamal & Kim, [Lecture Notes on Network Information Theory](https://arxiv.org/abs/1001.3404)（2010，T）。
- [Infotheo: a Coq library for information theory](https://github.com/affeldt-aist/infotheo)（Rocq/Coq，A）。

**Lean 项目**
- [LeanInfoTheory](https://github.com/serhatemrecoban/LeanInfoTheory)：README 的 v0.2.0 声明 811 supported declarations、57 modules，覆盖熵、互信息、KL、信道、Markov、DPI、Fano 和充分统计量；toolchain v4.33.1。
- [infotheorylib](https://github.com/matteonerini/infotheorylib)：按 Cover–Thomas、El Gamal–Kim、Yeung 三套教材组织，章节文件记录已形式化和未形式化内容；本轮读取的 toolchain 为 4.37.0-rc1。
- [rate_distortion_lean4](https://github.com/fubinyan/rate_distortion_lean4)：有限字母表 rate-distortion，提供 direct/converse 和 boundary achievability theorem；toolchain v4.28.0。
- [KTAIT](https://github.com/giulioruffini/KTAIT)：Kolmogorov/algorithmic information theory 的 Lean 项目；其 README 明确区分已形式化推论与显式假设的经典 AIT 基础。

**版本注意**
- LeanInfoTheory 当前 README 为 v0.2.0 / 811 declarations；官网某些 getting-started 页面仍显示 v0.1.0 / 601 declarations。应以固定 release tag 的 API 与 toolchain 为准，不能混用旧网页数据。
- infotheorylib 的当前 toolchain 是 release candidate，复现前需固定具体 commit 和 Mathlib revision。

**当前缺口**
- Shannon 基础、有限分布与率失真已有明显进展；多终端网络信息论、连续信源、信息几何等仍需逐项审查。
- LeanInfoTheory 与 rate_distortion_lean4 是不同项目：前者偏通用信息论 API，后者聚焦操作性率失真定理。

### 2.10 控制理论与网络化物理系统

**研究方向**
1. Lyapunov stability、asymptotic stability、LaSalle invariance。
2. Input-output stability、L_p gain、passivity、small-gain theorem。
3. 连续、离散和 hybrid systems。
4. Reachability、safe control、neural controller verification。

**代表论文**
- Doll & Shames, [Foundations of Machine-Checked Control Theory in Lean](https://arxiv.org/abs/2607.19727)（2026，F）：Lyapunov stability 与 small-gain theorem 的 Lean 形式化。
- Cohen & Rouhling, [A formal proof in Coq of LaSalle's invariance principle](https://doi.org/10.1109/SOSCYPS.2016.7580008)（2016，A）。
- Jasim & Veres 的 Isabelle/HOL small-gain formalization（论文被 Doll & Shames 2026 论文引用，A）。
- [KeYmaera X](https://keymaerax.org/)：differential dynamic logic 的 hybrid systems 验证工具。

**Lean 项目**
- [DynamicalSystems](https://github.com/mcdoll/DynamicalSystems)：Doll–Shames 论文对应库，README/toolchain 线索指向 Lean 4.36.0-rc2；涵盖 Lyapunov、LaSalle、small-gain、causality、L_p stability 和 passivity。
- [LeanForControl](https://github.com/AnandGokhale/LeanForControl)：另一独立控制理论 Lean 项目；本轮 README 声称核心库无 sorry/admit，toolchain 为 Lean 4.30.0-rc2，尚未独立 build。
- [control-theory-in-lean](https://github.com/forgi86/control-theory-in-lean)：早期探索性项目，不应替代上述论文对应的主库。
- TorchLean 的 Lyapunov-style neural controller case study 可连接控制与神经网络验证。

**相邻项目**
- [VeriDrone](https://github.com/VeriDrone)：Rocq/Coq 控制与无人机相关形式化。
- [KeYmaera X](https://keymaerax.org/)：混合系统和微分动态逻辑。
- Isabelle/HOL 的 small-gain 相关形式化。

**当前缺口**
- Doll–Shames 论文指出 Mathlib 的 ODE 全局存在等基础仍不完整；具体定理需要逐项核对假设和证明范围。
- 控制定理在数学模型中成立，不等于真实执行器、传感器和采样控制系统已验证。

## 3. 跨领域共同基础与技术关系

| 共用基础 | 下游领域 | 复用方式 |
|---|---|---|
| Mathlib | 数学、经济学、金融、信息论、物理、控制、AI/ML | 实数、拓扑、测度、概率、线性代数、优化和分析 |
| BrownianMotion | 金融数学、随机过程 | Brownian motion、Itô 积分与随机分析 |
| CSLib / Loom | 软件验证、协议、数据系统 | 程序语义、抽象状态、验证器生成 |
| Veil / Lentil | 分布式系统、时序性质、工作流 | 状态转换、LTL、安全/活性、模型检查 |
| Aeneas / Hax | Rust 软件、密码学、数据处理实现 | 源码抽取、规格映射和实现级证明 |
| LeanDojo-v2 | 所有领域形式化项目 | repo tracing、证明数据、Agent、检索与证明生成 |
| AI4SLT / LeanInfoTheory | 统计学习、量化研究 | 泛化界、集中不等式、熵/KL/信息论工具 |
| TorchLean / StarV / Marabou | AI/ML、控制 | 神经网络语义、鲁棒性、reachability 与证书检查 |

## 4. 版本、命名与证据质量问题

1. **EconCSLib 同名项目**：gametheoryinlean/EconCSLib 是“基础设施优先”；nikhgarg/EconCSLib 是“逐篇论文形式化优先”。两篇论文也明确说明两者独立且互补，不能合并成一个仓库。
2. **MathFin 论文与当前 README 统计不同**：论文 v4 为 804 条 benchmark，当前 README 为 906 条。可能是论文后继续增加，必须固定 commit/release 对齐。
3. **LeanInfoTheory 官网页面滞后**：repo README v0.2.0 为 811 declarations；部分官网页面仍是 v0.1.0 的 601 declarations。
4. **IFP 项目范围**：README 的 93/103 invariants 对应当前受限 Phase 1（两参与者、单 epoch），不是完整协议、动态成员或 reconfiguration 的全部证明。
5. **Resonate 项目性质**：是服务端 durable execution 的 Lean abstract machine/trace checker，不是共识算法。README 中属性数量会随分支演进，首轮不把数量当作成熟度指标。
6. **btc-verified 项目范围**：目前的 verified components 不等于 issuance/fork-choice/完整 Bitcoin consensus 已证明。
7. **LeanLTL 版本**：本轮读取的 toolchain 为 Lean 4.17.0-rc1；若要复用，应优先比较 Lean 4.35.0 的 Lentil/Veil 生态。
8. **Control toolchain 不一致**：DynamicalSystems 使用 4.36.0-rc2，LeanForControl 使用 4.30.0-rc2；不可直接混装。
9. **RC toolchain 风险**：infotheorylib/CSLib 等项目若锁定 RC 版本，先检查 Mathlib revision 与依赖闭包，再决定是否作为稳定基线。
10. **README 声明不是独立验收**：项目宣称 no sorry、已证明或 CI 通过，仍需固定 commit、检查 theorem、axiom、CI run 和 build logs。

## 5. 与量化金融结合的优先级

| 优先级 | 方向 | 可借鉴项目 | 对量化研究的潜在落点 | 不应误解为 |
|---|---|---|---|---|
| A1 | 数学金融 | MathFin、BrownianMotion | 风险度量、组合优化、定价、随机过程、风险约束 | 策略盈利证明 |
| A1 | 统计学习理论 | AI4SLT、LeanInfoTheory | 泛化界、集中不等式、模型复杂度、过拟合分析 | 因子样本外有效性自动成立 |
| A1 | 统计程序规范 | StatWhy（非 Lean） | 假设检验前提、统计程序要求和错误使用检查 | 证明数据分布假设为真 |
| A1 | PIT 数据语义 | 本专题 PIT prototype | availableAt、历史修订、as-of join、时点股票池 | 已完成完整生产数据验证 |
| A2 | 程序与数据实现验证 | Aeneas/Hax、CSLib、CertifyingDatalog | 对关键数据转换、规则引擎和状态机建立可检查规格 | Python 实现自动等同 Lean 规格 |
| A2 | 控制理论 | DynamicalSystems、LeanForControl、TorchLean | 仓位/执行控制器稳定性、风险反馈系统 | 真实市场动态满足模型假设 |
| A2 | 经济学/博弈论 | MathEconLib、EconCSLib | 市场机制、激励、博弈、拍卖和分配 | 经验市场行为符合简化均衡假设 |
| A3 | 分布式系统 | Veil、Lentil、Resonate | 数据采集、事件处理、任务调度和状态机一致性 | 共识证明可直接推出交易逻辑正确 |
| A3 | 信息论 | LeanInfoTheory、rate_distortion_lean4 | 信息量、信号压缩、熵/KL、信道和特征信息结构 | 信息量高等于 alpha 高 |
| A3 | 密码学/零知识 | VCVio、ArkLib、Aeneas | 数据来源完整性、隐私计算和可验证计算 | ZK 证明数据源内容真实 |
| A3 | 物理/量子 | Physlib、physicslib4 | 数学结构和方法迁移 | 直接改善 A 股策略表现 |

### 对 A 股量化的明确研究空白

本轮未发现可确认的 Lean 项目直接覆盖：
- A 股 Level-2/逐笔委托成交和订单簿重建；
- 竞价、分钟资金流、行业扩散和微观结构因子的完整定义与验证；
- RankIC/ICIR、多重检验、样本外稳定性、交易成本和回测偏差的端到端 Lean 形式化；
- 真实行情供应商的历史修订、时间戳真实性和 PIT 数据血缘。

可行的分层是：Lean 证明时间可得性、数据准入、状态机和数学引理；Python 处理真实数据、统计估计、交易成本、样本外回测和性能；数据源真实性与市场制度假设仍由独立证据验证。

## 6. 本轮结论与下一步

**结论：** 本轮已经从“列举 Lean 的学科应用”推进到 10 个领域的“具体方向—论文—Lean 项目—相邻项目—研究缺口”映射。已找到多个之前没有充分展开的方向：BFT/Veil、控制理论、信息论率失真、统计学习理论和统计假设检验程序验证。

**尚未完成：** 外部仓库的全量 theorem/sorry/axiom/许可证/CI 审计和独立构建；部分项目 README/论文统计存在版本差异；领域覆盖不是穷尽性综述。

**下一步：** 先对 A1/A2 项目做固定 commit、许可证、依赖、CI、关键 theorem 与 axiom audit；然后选出可复用的方法，将它们与 PIT/量化研究流程逐项对接。不要把所有仓库同时 clone/build，也不要因一个项目阻断整个地图。
