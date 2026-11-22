# TOPIC-018｜Lean 形式化证明与跨学科可验证系统

> 规范研究任务：[AI_book Issue #74](https://github.com/fweiger/AI_book/issues/74)  
> Task ID：AI-BOOK-TOPIC-018-LEAN-FORMAL-VERIFICATION  
> 建立：2026-11-22；专题版本：0.6.0（Draft）；状态：OPEN_RESEARCH / M0 项目准入进行中，M2/M3 已有金融与密码学源码证据。静态源码审计不代表项目已独立构建或完整证明。

## 最初的问题

Lean 如何把数学猜想、定义和证明转化为机器可检查的形式化对象？除数学以外，软件工程、密码学、分布式系统、经济学、金融、AI、物理学等领域如何实际使用 Lean？研究者具体采用哪些证明策略、工具、工程流程和 AI 协作技巧？

## 核心研究框架

**问题/猜想 → 数学定义与假设 → Lean 形式化陈述 → 证明分解与定理复用 → Kernel 检查 →（如涉及程序）实现精化/差分验证 → 独立审查与可复现归档。**

本专题不是 Lean 语法手册，也不只围绕某个著名猜想。核心资产是可复用的跨学科案例、方法卡、证据和边界。

## 术语边界

- **Lean 4**：基于依赖类型理论的交互式定理证明器，同时也是函数式编程语言。
- **Lean Kernel**：检查证明项的可信核心；tactic 生成的证明项仍由 Kernel 检查。
- **Mathlib**：社区维护的 Lean 数学库，提供定义、定理、结构层级和自动化工具。
- **Elan**：Lean 工具链/版本管理器，不是证明器或证明内核。
- **Lake**：Lean 项目的构建与依赖管理工具。
- **Blueprint**：大型形式化项目的数学文档、定理依赖和 Lean 声明之间的可追踪组织方式。

任何项目都应锁定自身 lean-toolchain、依赖版本和 commit；不能把某个项目在特定版本下的构建结果推广到其他版本。

## 导航

- [数学与跨学科应用全景](field-map.md)
- [代表案例与项目审计台账](case-studies.md)
- [方法与技巧库](methods-and-tactics.md)
- [形式化研究工作流](formalization-playbook.md)
- [研究问题](questions.md) · [核心主张](claims.md)
- [知识关系图](knowledge-map.md) · [机器可读图谱](knowledge-graph.json)
- [论文、官方文档和项目来源](bibliography.md)
- [唯一目标跟踪器](../../task-goals/issue-74/GOAL_TRACKER.md)
- [研究会话记录](sessions/README.md) · [变更记录](CHANGELOG.md)

## 初始证据边界

本轮已读取 Lean 官方语言参考、Lean 社区项目目录、Aeneas 官方项目页、MathFin、MathEconLib、TorchLean 论文和 physicslib4 教程等来源。当前为**来源级初筛**：未逐一克隆项目、锁定所有 release/commit、检查全部许可证或执行完整构建。详见 field-map.md 与 case-studies.md。

## 重要限制

- Kernel 检查的是形式化陈述及其证明，不会替研究者保证陈述忠实表达自然语言猜想。
- 定理只在其定义、假设和依赖下成立；模型假设与现实世界的符合性需要独立证据。
- 证明一个规范正确，不自动证明某个 Python/Rust/C++ 实现符合规范；需要精化证明或明确分级的测试证据。
- 形式化金融数学不证明策略有超额收益，也不自动证明原始市场数据的时点真实性。


## 最新研究进展（2026-11-22）

- 首批 10 个仓库完成固定 commit / README / toolchain / LICENSE / Lake 配置入口级初审；8 个 Lean 4 项目的 Lake manifest 已解析。
- Hax/Aeneas 使用同一份 Rust FRI arity 选择函数源码，已建立同源对照；Aeneas BasicProofs 的源码证明项比 Hax 版本更完整，但 ArkLib bridge 仍有显式 axioms/sorry。
- Hax ADC 从早期 PoC 发展为官方 \`lean_adc\` 示例：\`specset bv\` + \`hax_mvcgen\` + \`bv_decide\`。
- 本轮所有 Lean build 均 NOT_RUN；没有把静态源码检查升级为 Kernel 构建验收。
- 详细证据见 [case-studies.md](case-studies.md)、[methods-and-tactics.md](methods-and-tactics.md) 和 [claims.md](claims.md)。

## 金融领域新增结论（2026-11-22）

MathFin 提供了可复用的数学金融证明样例，但它不替代行情数据、PIT 核验和经验回测。重点新增了 CVaR 点态证书、Markowitz KKT 充分性、CRR 特征函数收敛、假设非空性检查，以及 benchmark formalization fidelity 与生成式公理审计方法。

面向 AI_Trader #488 的候选接口是：Lean 证明数据可得时间、as-of filter、point-in-time universe 和状态机不变量；Python 负责真实数据、数值计算、统计检验、交易成本与样本外回测。此接口目前仍是研究设计，未接入生产或 #488 实验。

## PIT/no-lookahead 最小原型

已建立独立 Lean 4.35.0 示例：[PITNoLookahead.lean](examples/pit-no-lookahead/PITNoLookahead.lean)。它区分 eventTime 与 availableAt，证明过滤后的每条记录都不晚于 decisionTime。该示例还没有实现 latest-revision as-of join，GitHub Actions build 结果待核验。
