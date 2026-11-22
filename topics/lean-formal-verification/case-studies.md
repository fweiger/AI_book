# TOPIC-018｜代表案例与项目审计台账

> 本台账区分“发现项目”“读到方法”“实际构建”“独立复现”。初始检索不等于运行验证。

| 项目 | 领域 | 主要方法/用途 | 主要来源 | 当前状态 | 后续审计 |
|---|---|---|---|---|---|
| Lean 4 / Kernel | 数学、软件验证 | 依赖类型、证明项检查、tactic automation | [Language Reference](https://lean-lang.org/doc/reference/latest/) | E1 文档已读 | 固定稳定版与 release commit，检查外部 kernel/axiom audit |
| Mathlib | 数学基础设施 | 统一数学定义与定理库、类型类和自动化 | [官网](https://mathlib.org/)；[CPP 2020 论文](https://doi.org/10.1145/3372885.3373824) | E1 文档/论文入口已读 | 核对当前 Mathlib4 的版本、结构、贡献规范与构建 |
| Lean Projects Registry | 数学 | 项目索引、项目意向、避免重复形式化 | [社区项目目录](https://leanprover-community.github.io/lean_projects.html) | E1 目录已读 | 挑选数学分支案例并逐一审查源码 |
| Liquid Tensor Experiment | 数学/大型证明 | 复杂证明、依赖图、Mathlib 复用 | [GitHub](https://github.com/leanprover-community/lean-liquid) | E1 项目入口 | 检查 blueprint、声明、证明、依赖和构建 |
| Aeneas | Rust 软件验证 | Charon LLBC 到函数式模型，Lean backend | [官方项目页](https://aeneasverif.github.io/projects/) | E1 官方说明 | 固定 commit/toolchain，复现教程，确认支持 Rust 子集 |
| Verified zkEVM Rust-to-Lean | 密码学/程序验证 | Hax/Aeneas 抽取、ArkLib/CompPoly 规格、AI prover | [2026 Experience Report](https://arxiv.org/abs/2605.30106)；[Rust verification repo](https://github.com/Verified-zkEVM/rust-lean) | E1 论文已读 | 核对各子项目代码、CI、原始 Rust 和 Lean 定理映射 |
| ArkLib | 密码学 | SNARK/证明系统的形式化库 | [GitHub](https://github.com/Verified-zkEVM/ArkLib) | E0/E1 候选 | 读 blueprint 和源码，区分 proved 与 stated |
| Veil / IFP | 分布式共识 | BFT 协议安全性质 | [IFP repository](https://github.com/sarvalabs/ifp) | E0 候选 | 获取 Veil 定义、协议模型、定理、假设和 CI |
| MathEconLib | 经济学 | 偏好、激励、均衡、动态、识别、估计与推断 | [官网](https://mathecon.dev/)；[GitHub](https://github.com/matheconlib/matheconlib) | E1 官网已读 | 固定 release、模块、证明状态与许可证 |
| EconCSLib（gametheoryinlean） | 计算经济学 | 博弈、社会选择、拍卖、匹配、机制设计 | [GitHub](https://github.com/gametheoryinlean/EconCSLib)；[arXiv:2606.16144](https://arxiv.org/abs/2606.16144) | E1 README/论文摘要已读 | 检查稳定 API、Blueprint、版本和证明覆盖 |
| EconCSLib（nikhgarg） | 经济学与计算 | 以研究论文为单位的 Human–AI–Lean 形式化工作流 | [GitHub](https://github.com/nikhgarg/EconCSLib)；[arXiv:2606.13306](https://arxiv.org/abs/2606.13306) | E1 README/论文摘要已读 | 与同名项目区分；检查论文翻译审查机制 |
| Econlib | 经济学/政治经济学 | 偏好、概率、优化、博弈、机制设计、社会选择、均衡 | [GitHub](https://github.com/danlyng/Econlib) | E1 项目说明已读 | 核验 release、许可证、依赖和核心 theorem |
| MathFin | 金融数学 | 随机微积分、定价、无套利、组合、风险 | [官网](https://formal-applied-math.github.io/formal-mathfin/index.html)；[arXiv:2606.01356](https://arxiv.org/abs/2606.01356) | E1 官网/论文已读 | 核验声明与论文对应、faithfulness tier、构建和公理审计 |
| TorchLean | AI/机器学习/控制 | 网络执行语义、Float32、鲁棒性、PINN 和 Lyapunov 控制器 | [arXiv:2602.22631](https://arxiv.org/abs/2602.22631) | E1 预印本已读 | 核验代码可用性、构建、证明对象和模型覆盖 |
| physicslib4 | 数学物理 | AQFT、Haag–Kastler、GNS、Blueprint 到 Lean | [教程](https://kellyjdavis.github.io/aqft/physicslib4-tutorial/)；[项目](https://github.com/physicslib/physicslib4) | E1 教程已读 | 核验当前源码、构建和已完成/未完成声明 |
| FormalQFT / OSforGFF | 数学物理 | 构造性 QFT 与 Osterwalder–Schrader 公理 | [arXiv:2603.15770](https://arxiv.org/abs/2603.15770)；[GitHub](https://github.com/FormalQFT) | E1 论文摘要/项目页 | 逐项核验 theorem 状态、假设变化和构建 |
| EconLib4 | 信息论/经济学/金融 | 信息、编码、机制设计和金融等模块 | [项目页](https://edu-ap.github.io/EconLib4/) | E0 候选 | 读取源码与声明；未审查前不作证明覆盖结论 |

## 每个项目的强制审计字段

- GitHub URL、owner、默认分支、固定 commit SHA、最近 release。
- 许可证及第三方依赖许可。
- lean-toolchain、lakefile、lake-manifest.json。
- 实际构建命令、CI 最近状态和构建环境。
- 形式化对象、关键 theorem、证明状态（proved/stated/open/partial）。
- sorry/admit、自定义 axioms、#print axioms 或项目自带 axiom audit。
- 原论文/自然语言主张到 Lean 声明的翻译差异和附加假设。
- 项目成熟度、维护情况、可复用模块与失败边界。

## 禁止混淆

1. 项目 README 声称覆盖某主题 ≠ 该主题所有结果已证明。
2. Lean 文件中存在 theorem 声明 ≠ theorem 有完整证明。
3. lake build 通过 ≠ 形式化定义与原论文完全等价。
4. Lean 定理通过 ≠ 被建模的物理/经济/金融假设符合现实。
5. 有 AI prover 参与 ≠ AI 输出无需人工检查；最终 proof term 仍须由 Lean Kernel 检查。
