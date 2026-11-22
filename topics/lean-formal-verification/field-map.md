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
