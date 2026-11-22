# TOPIC-018｜知识关系图（研究框架）

> 本图展示研究对象与方法的组织关系，不代表各领域所有案例均已验证，也不表示存在因果关系。

行业与业务需求
→ 业务领域/价值链环节
→ 具体场景与问题
→ 可形式化对象与目标性质
→ Lean 能力/适配边界
→ 论文与开源项目映射
→ 按需审计、原型和应用验证

横向支撑：
- Mathlib/领域库：提供数学定义和可复用定理。
- Blueprint/定理依赖图：组织大型证明和研究任务。
- AI Agent：生成候选定义、引理和证明，协助反例修正。
- Refinement/语义保持：连接形式化模型和实际程序。
- SMT/Model Checking/属性测试/差分测试：提供互补而非等价的验证证据。

横向能力层（跨行业复用）：
- 规格与规则形式化、程序正确性、状态机/协议安全、数学定理、密码学、概率统计、优化控制、数值计算、数据时间语义、AI 模型验证。

行业应用层：见 [industry-opportunity-map.md](industry-opportunity-map.md)。统一研究流程见 [industry-application-framework.md](industry-application-framework.md)。

跨学科应用分支（支撑层，不等于行业机会排序）：
- 数学：猜想、定理、数学结构和大型证明。
- 软件工程：程序正确性、编译器、类型系统。
- 密码学：SNARK、零知识证明和协议安全。
- 分布式系统：共识、数据库和状态机不变量。
- 经济学：偏好、均衡、博弈和机制设计。
- 金融数学：随机微积分、定价、投资组合和风险。
- AI/ML：网络语义、鲁棒性和数值计算。
- 物理学：AQFT、QFT 和公理化模型。
- 信息论/控制：熵、编码、稳定性和科学计算。

金融数学与 [AI_Trader #488](https://github.com/fweiger/AI_Trader/issues/488) 建立应用关联，但不复制其 A 股 PIT/No-Lookahead 实验和动态任务状态。

## 重要禁止推断

- AI 给出证明文本 → Lean 已验证。
- theorem 声明存在 → theorem 已证明。
- Kernel 检查通过 → 原始自然语言命题翻译无误。
- 模型定理通过 → 实际程序符合模型。
- 形式化金融数学 → 市场数据正确或策略有收益。

## 2026-11-22｜跨领域证据图新增连接

领域节点不再只连接一个项目名称，而是按以下关系展开：

**领域 → 研究方向 → 原始理论论文/形式化论文 → Lean 项目 → 相邻证明助手/验证工具 → 证明范围与缺口。**

新增的重要连接：
- 分布式系统：CSLib/时序逻辑 → Veil/Lentil → IFP BFT safety case；Resonate 和 btc-verified 作为不同类型的状态机/协议组件案例。
- 统计学习：AI4SLT → 经验过程/集中不等式/泛化界 → 量化模型复杂度与过拟合理论；StatWhy 作为统计程序前提检查的非 Lean 对照。
- 信息论：LeanInfoTheory 通用 API → infotheorylib 教材映射 → rate-distortion 具体定理。
- 控制：DynamicalSystems/LeanForControl → Lyapunov/LaSalle/small-gain → TorchLean neural controller verification。
- 金融：MathFin/BrownianMotion → 风险/定价/组合；PIT prototype → 时间可得性 filter safety。经验回测、数据源真实性和策略盈利仍在 Lean 形式化边界之外。

完整节点、关系和阅读路径见 [knowledge-graph.json](knowledge-graph.json) 与 [field-evidence-matrix.md](field-evidence-matrix.md)。


## 2026-11-23｜行业应用框架优先

知识组织从“问题/项目/论文收集”调整为“行业需求驱动”：
行业 → 业务领域 → 场景 → 问题 → 形式化对象 → 目标性质 → Lean 能力 → 论文 → 项目 → 按需审计/原型。

项目与论文是对应用机会的证据和实现资源，不再作为研究入口。
