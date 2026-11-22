# TOPIC-018｜阅读与研究路径

| 路径 | 推荐顺序 | 目标 | 适合对象 |
|---|---|---|---|
| R01 Lean 基础 | README → 官方 Language Reference → Elan 安装手册 → Mathlib 入门 | 分清 Lean/Kernel/Mathlib/Elan/Lake，建立可编译环境 | 初学者、工程研究者 |
| R02 数学猜想与证明 | questions Q02/Q03 → Lean Projects → Mathlib → Liquid Tensor / Formal Conjectures | 理解自然语言命题、形式化陈述、证明依赖与 Kernel 检查 | 数学研究者 |
| R03 软件与密码学 | Aeneas → Rust-to-Lean 经验报告 → ArkLib / Verified-zkEVM | 理解规格、程序抽取、精化、AI prover 和实现验证边界 | 软件/安全工程师 |
| R04 经济金融 | MathEconLib → EconCSLib / Econlib → MathFin → AI_Trader #488 | 比较经济学和金融数学库，区分数学定理与金融实证 | 经济/金融研究者 |
| R05 AI 与物理 | TorchLean → physicslib4 教程 → FormalQFT | 研究数值语义、神经网络认证、物理公理化模型 | AI/科学计算/物理研究者 |
| R06 方法工程 | methods-and-tactics → formalization-playbook → case-studies | 学习证明构造、自动化、Blueprint、CI、版本和独立审查 | 所有贡献者 |

## 研究顺序原则

- 先读官方定义和工具职责，再读案例。
- 先核验 theorem statement 与假设，再讨论 proof 是否完整。
- 先读源码/CI，再判断项目成熟度。
- 涉及程序时，必须单独建立实现精化关系；只有测试时按测试证据报告。
- 任何领域都可以保留为“证据不足”，不强行形成统一结论。
