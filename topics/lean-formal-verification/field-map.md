# TOPIC-018｜数学与跨学科应用全景

> 初始来源审查日期：2026-11-22。以下是来源级地图，不是完整系统综述。E1 表示官方项目页/原始论文已读到方法与边界；未克隆构建的项目均不得标为 E2。

## A. 数学领域

| 子领域/应用 | 代表项目或来源 | Lean 实际承担的工作 | 当前证据 | 待核事项 |
|---|---|---|---|---|
| 数学基础设施 | [Mathlib](https://mathlib.org/) | 统一定义、定理库、结构层级、自动化与跨项目复用 | E1 | 版本化模块清单、贡献审查和 API 设计 |
| 猜想与定理陈述 | [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) | 把文献/研究中的猜想转成 Lean 声明，便于机器搜索与证明 | E0/E1 待逐项核验 | 声明、证明、部分证明和仅有注释的区分 |
| 研究级数学形式化 | [Lean Projects Registry](https://leanprover-community.github.io/lean_projects.html) | 组织分析、代数、数论、几何、组合等项目 | E1 | 逐项目读取原文、源码与构建状态 |
| 大型证明工程 | [Liquid Tensor Experiment](https://github.com/leanprover-community/lean-liquid) | 以多人协作、Mathlib 复用、Blueprint 和 Kernel 检查完成复杂证明 | E1 / 项目入口已核 | 原始定理与形式化版本之间的细节差异 |
| 数论 | [Fermat's Last Theorem 项目入口](https://leanprover-community.github.io/lean_projects.html) | 将证明分解为可依赖的定义、引理和定理 | E1 / 社区目录级 | 项目具体目标范围和当前完成状态 |
| 组合数学/代数结构 | [Equational Theories Project](https://leanprover-community.github.io/lean_projects.html) | 对大量代数恒等式及蕴含关系进行形式化判定 | E1 / 社区目录级 | 自动工具、人工证明与 Lean 检查的分工 |
| 几何与分析 | [Tao's Analysis I 等项目](https://leanprover-community.github.io/lean_projects.html) | 将教材/研究级数学内容形式化为可复用库 | E1 / 社区目录级 | 具体项目文件与证明覆盖逐项审查 |

Lean 社区目录明确说明其项目列表是代表性样本，不保证穷尽；目录同时包含成熟项目和早期意向，不能把两类状态混为一谈。

## B. 非数学领域

| 领域 | 已发现的真实案例/来源 | Lean 形式化对象或方法 | 初步状态 | 边界 |
|---|---|---|---|---|
| 软件工程/程序验证 | [Aeneas](https://aeneasverif.github.io/projects/)；[Rust-to-Lean 经验报告](https://arxiv.org/abs/2605.30106) | Rust → Charon LLBC → Lean 函数模型 → 规格与证明 | E1 | Aeneas 官方说明当前针对 safe、sequential Rust；抽取范围有限 |
| 密码学/零知识证明 | [ArkLib](https://github.com/Verified-zkEVM/ArkLib)；[Rust-to-Lean 经验报告](https://arxiv.org/abs/2605.30106) | SNARK/协议规格、密码学原语和生产 Rust 代码验证 | E1 / 论文已读 | 必须核对每个定理所覆盖的协议组件、威胁模型和假设 |
| 分布式系统/共识 | [Veil/IFP 项目](https://github.com/sarvalabs/ifp) | 对 BFT 共识协议安全性质建立 Lean 模型和证明 | E0/E1 待源码审查 | 当前只登记项目线索，不宣称协议证明已独立复现 |
| 经济学/博弈论/机制设计 | [MathEconLib](https://mathecon.dev/)；[EconCSLib](https://github.com/gametheoryinlean/EconCSLib)；[Econlib](https://github.com/danlyng/Econlib) | 偏好、均衡、拍卖、社会选择、激励相容、计量基础 | E1 | 需区分共享基础库、论文逐篇形式化库及长期目标 |
| 金融数学 | [MathFin](https://formal-applied-math.github.io/formal-mathfin/index.html) | 随机微积分、无套利、衍生品定价、组合和风险度量 | E1 | 形式化数学不证明市场数据质量、Python 实现或策略收益 |
| AI/机器学习 | [TorchLean](https://arxiv.org/abs/2602.22631) | 网络语义、Float32、鲁棒性界、证书检查和神经控制器 | E1 / 预印本 | 核实模型类别、实验规模、代码可用性和部署边界 |
| 物理学 | [physicslib4 教程](https://kellyjdavis.github.io/aqft/physicslib4-tutorial/)；[FormalQFT](https://arxiv.org/abs/2603.15770) | AQFT、GNS 构造、Haag–Kastler / Osterwalder–Schrader 等公理化数学结构 | E1 | 公理体系内推导不等于实验事实或物理理论完整性 |
| 信息论/编码理论 | [EconLib4 项目页](https://edu-ap.github.io/EconLib4/) 等候选 | Shannon 编码、熵、信息处理不等式等数学结构 | E0 / 候选线索 | 尚需独立核实代码、声明和证明状态 |
| 控制/科学计算 | TorchLean 的 Lyapunov 神经控制器案例；[Lean 项目目录](https://leanprover-community.github.io/lean_projects.html) 中 SciLean | 稳定性条件、数值误差界、科学计算定义 | E1/E0 | 需要区分形式化模型、数值实现和物理系统行为 |

## C. 本轮技术体系初核

- Lean 官方语言参考说明 Lean 是基于依赖类型理论的交互式定理证明器；最小 Kernel 检查证明项，tactics 生成的项仍由 Kernel 检查。
- Elan 在官方安装手册中被定义为 Lean version manager；项目实际版本由项目工具链文件约束。
- Mathlib 是社区驱动数学库，不是 Lean Kernel。
- Lake、Blueprint 的具体职责与复现流程仍需在 M0 逐项补充官方文档和真实工程示例。

## D. 后续审查优先级

1. 数学：Mathlib、Formal Conjectures、Liquid Tensor、Fermat、Equational Theories。
2. 工程：Aeneas、Hax、ArkLib、Verified-zkEVM。
3. 经济金融：MathEconLib、两种不同的 EconCSLib、Econlib、MathFin。
4. AI/物理：TorchLean、physicslib4、FormalQFT、Physlib。
5. 分布式、信息论、控制：先核实源代码、具体声明与证明状态，再决定是否列为正式案例。

所有项目的版本、许可证、构建和 sorry/admit/公理审计都在 case-studies.md 持续补齐。


## E. M0 版本与生态边界发现（2026-11-22）

- Lean 4 项目不能只按“Lean”标签合并。Liquid Tensor Experiment 的仓库 README 明确说明它使用 Lean 3；这是重要的大型形式化历史案例，但与当前 Lean 4/Mathlib4 项目的工具链不同。
- 当前审查的 Lean 4 项目分别固定在 4.30.0、4.33.1、4.35.0、4.36.0 和 4.37.0-rc1。版本兼容和依赖锁是跨项目复现的首要工程问题。
- Formal Conjectures 主要把猜想转成形式化声明，项目的贡献规则明确排除已解决陈述；它的价值是开放问题基准和 AI 定理证明任务，不代表项目内猜想已被证明。
- EconCSLib 的稳定库接口与 OpenProblem 实验接口分离；Blueprint 记录了尚未实现的数学目标。必须分别记录 stable theorem、stated target 和 open problem。
- Aeneas 的 Lean backend 位于 backends/lean 子目录，不能仅检查仓库根目录来判断 Lean 工具链和构建入口。
- rust-lean 是多子项目集合；正确的审计单位应下沉到具体 Hax/Aeneas 子项目，而不是将仓库根目录当成单一 Lean 包。


### 版本锁定的进一步发现

8 个 Lean 4 项目的 Lake manifest 已确认存在并解析。Mathlib、Formal Conjectures、Aeneas、ArkLib、MathEconLib、EconCSLib、MathFin 和 physicslib4 均将依赖固定到具体 Git commit。Mathlib revision 在这些项目之间并不相同；因此只复制 lean-toolchain 不足以复现，必须同时保存项目 commit 和 lake-manifest.json。


### 密码学与软件验证：两个可迁移的 Rust→Lean 实践

- **Hax-FRI**：把 Plonky3 的 Rust FRI folding 函数抽取到 Lean，再连接 ArkLib 的协议规格。源码 README 报告部分基础证明已构建，但最终 FoldingCorrectness 定理仍为 TODO。
- **Hax ADC**：把 32-bit limb addition with carry 的 pre/post 条件写在 Rust 注解中，抽取后用 hax_bv_decide 做 bit-blasting。案例同时暴露了 cast、shift、tuple projection、monadic representation 和 BitVec fragment 支持问题。
- 这两类案例的关键技巧是先把目标缩小到可验证的函数和明确的前后置条件，再逐层建立从抽取代码到协议规格的 refinement。自动化 tactic 的支持范围本身必须纳入验收。


## F. 密码学 / 软件验证：同源 FRI 代码的 Hax 与 Aeneas 对照

2026-11-22 在 \`Verified-zkEVM/rust-lean\` 固定 commit 上，确认 Hax 与 Aeneas 两条 pipeline 使用相同 Git blob SHA 的 \`compute_log_arity_for_round\` Rust 源文件，形成可控的工具对照：

- Hax：Rust HIR + annotations → 自定义 \`RustM\` → Lean；两个核心输出边界定理已有证明，但 Hax BasicProofs 有 9 个 sorry，ArkLib 集成文件另有 4 个 sorry。
- Aeneas：Rust MIR → Charon LLBC → 函数式 \`Result\` → Lean；BasicProofs 六个 theorem 和三个 example 的源码没有显式 sorry/axiom；但 ArkLib 集成 target 为处理 \`BitVec.toNat_pow\` 冲突，使用 3 个 axioms、1 个 opaque 和 4 个 sorry。
- 这个样本显示 Aeneas 在局部算术/分支性质上更易于直接证明；不代表工具整体优劣。两者都没有完成完整 FRI 多轮协议和多项式折叠证明。
- Hax ADC 的历史 PoC 问题已由上游多项 PR 迭代；官方 ADC example 采用 \`specset bv\` + \`hax_mvcgen\` + \`bv_decide\`，更适合作为可迁移的方法。

**研究边界：** 本轮是固定 commit 的源码与依赖审计；没有运行 Lean build，也没有独立复现上游报告。不能把源码中无 sorry 等同于 Kernel 已接受，也不能把 axiomatized bridge 视为实现精化证明。

### Hax/Rust 验证生态的时点修正

Hax ADC README 记录的是早期开发阶段的失败列表。后续 Hax 上游已合并 cast 类型标注（#1925）、规格集分离（#1933）、模块命名修复（#1927）和完整 Lean package scaffold（#2142）。研究问题应从“功能是否缺失”转为“目标项目锁定的 Hax 版本是否包含修复，以及升级后能否完成抽取、构建和正确性证明”。

Hax-FRI 固定的 Hax commit 是 2026-01-20 的 Lean 4.26.0 升级提交，早于 #1925/#1933；Hax 0.5.0（2026-11-09）要求 Lean 4.35.0 并包含 breaking changes。应保留旧版可复现基线，再单独建立新版迁移分支。

## G. 金融数学与量化研究：MathFin 的可迁移边界

MathFin 是数学金融的形式化库，而不是量化策略回测系统。它已覆盖 Gaussian VaR/CVaR、coherent risk、Markowitz、Black-Litterman、FTAP、Black-Scholes、CRR 收敛、Itô/Girsanov 等理论结果。其重要价值不只在 theorem 数量，还在于把 `full`、`library_wrapper`、`reduced_core` 分开记录，并将 benchmark 引用到的常量纳入生成式公理审计。

对 A 股量化工作，建议把 Lean 放在 Python 研究流程的**逻辑正确性层**，而不是替代统计计算：
1. 时间可得性：每条输入记录携带 `eventTime` 与 `availableAt`，决策时点为 (t)，仅允许 `availableAt ≤ t) 的记录进入特征计算。
2. 历史修订：同一 eventTime 的晚到修订必须按 availableAt 控制，不得因 eventTime 早于决策时点就被误认为当时已知。
3. 股票池：成员资格按决策时点的上市/退市状态与当时可用的指数/行业成分快照判断。
4. 标签与特征：证明训练/回测的 feature window、label window 和 decision time 满足时序隔离。
5. 执行与风控：证明订单状态机、现金/持仓守恒、仓位上限、止损与可交易状态约束。

这些是可 formalize 的候选不变量，不是已经验证的 AI_Trader 生产代码。完整 as-of join 还需要证明排序、重复版本优先级、空值与修订策略；一个简单 filter safety theorem 只证明不泄漏，不证明选中了最新可用记录。

**边界：** Lean 可以证明程序在给定输入/时间戳语义下满足不变量；不能证明数据源时间戳真实、市场制度假设完整、样本外收益显著或策略盈利。统计结论仍需 Python/真实数据/样本外检验。

### PIT/no-lookahead 的第一份可执行规格原型

已在 AI_book 专题分支建立独立 Lean 4.35.0 package，区分 eventTime 与 availableAt，并证明 eligibleRows 的所有输出均满足 availableAt ≤ decisionTime；一个“事件已发生但修订尚未发布”的例子被正确排除。当前仍是 filter safety，不是完整 as-of join；GitHub Actions build 结果待回读。它是 AI_Trader #488 可采用的形式化接口样例，不是对 #488 现有代码的验证。
