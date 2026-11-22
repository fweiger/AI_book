# TOPIC-018｜核心主张与证据状态

> C-ID 稳定；本表只登记有明确来源和证据等级的主张。初始来源级别以公开官方文档/论文为主，不代表本仓库已独立构建或复现对应项目。

| C-ID | 主张 | 来源 | 状态 | 最强限制/反例 |
|---|---|---|---|---|
| C018-001 | Lean 基于依赖类型理论；其最小 Kernel 检查证明项，tactic 生成的项仍交由 Kernel 检查 | [Lean Language Reference](https://lean-lang.org/doc/reference/latest/) | E1 / 官方参考文档已读 | Kernel 检查形式化证明项，不检查自然语言命题是否建模正确 |
| C018-002 | Elan 是 Lean 工具链/版本管理器，负责按项目配置切换工具链，不是证明内核 | [Lean 安装手册](https://lean-lang.org/install/manual/) | E1 / 官方安装文档已读 | 仍需结合项目 lean-toolchain 与锁定依赖确定可复现版本 |
| C018-003 | Mathlib 是社区驱动的 Lean 数学库，提供可复用数学定义、定理和自动化 | [Mathlib](https://mathlib.org/)；[Mathlib 论文](https://doi.org/10.1145/3372885.3373824) | E1 / 官方页面与论文入口已读 | 论文发表于 2020，不能代表当前全部模块；具体定理仍需逐条查证 |
| C018-004 | Aeneas 将受支持的 Rust 程序转换为适合验证的函数式模型，并提供 Lean 等验证后端 | [Aeneas 官方项目页](https://aeneasverif.github.io/projects/) | E1 / 官方项目说明已读 | 官方页面明确其当前目标为 safe、sequential Rust；不代表任意 Rust 程序均可处理 |
| C018-005 | 已有研究将 Rust 密码学代码抽取到 Lean，并结合形式化规格库和 AI prover 关闭部分证明义务 | [Rust-to-Lean Pipeline Experience Report](https://arxiv.org/abs/2605.30106) | E1 / 论文摘要与正文开头已读 | 论文描述的项目范围和成功义务有限；不能推断 AI 可自动完成全部证明 |
| C018-006 | MathFin 是基于 Mathlib/BrownianMotion 的 Lean 4 金融数学库，覆盖随机微积分、定价、投资组合与风险 | [MathFin 官方站](https://formal-applied-math.github.io/formal-mathfin/index.html)；[论文](https://arxiv.org/abs/2606.01356) | E1 / 官方项目页与论文入口已读 | 项目统计会随版本变化；具体条目需核对 faithfulness tier、假设和源码 |
| C018-007 | MathEconLib 正在建设经济学 Lean 4 共享形式化基础，覆盖微观、宏观和计量经济学方向 | [MathEconLib](https://mathecon.dev/) | E1 / 官方项目页已读 | 其长期目标范围不等于所有领域已经形式化完成 |
| C018-008 | TorchLean 研究在 Lean 中统一神经网络执行语义与验证语义，并显式建模 Float32 等数值细节 | [TorchLean 论文](https://arxiv.org/abs/2602.22631) | E1 / 预印本已读 | 预印本方法和案例不能自动推广到所有网络架构或部署栈 |
| C018-009 | physicslib4 将代数化量子场论等物理数学结构形式化，并提供从 Blueprint 到 Lean 定理的教程 | [physicslib4 教程](https://kellyjdavis.github.io/aqft/physicslib4-tutorial/) | E1 / 项目教程已读 | 证明的是指定公理化模型中的数学结果，不等于实验物理理论已被验证 |

## 证据等级

- **E0**：项目/仓库/页面存在，未核实具体形式化内容。
- **E1**：官方文档或原始论文已读取到足以确认方法、目标和限制。
- **E2**：锁定 commit、依赖和环境后，公开构建/测试真实通过。
- **E3**：独立复现、交叉实现或独立审查通过。
- **E4**：相关现实应用还获得领域内适当的外部/经验验证；E4 不是 Lean 自身可授予的等级。

不要把一个项目的 E1/E2 自动传递给它引用的所有 theorem、模块或应用。
