# TOPIC-018｜Lean 形式化证明与跨学科可验证系统

> 规范研究任务：[AI_book Issue #74](https://github.com/fweiger/AI_book/issues/74)  
> Task ID：AI-BOOK-TOPIC-018-LEAN-FORMAL-VERIFICATION  
> 建立：2026-11-22；专题版本：0.6.3（Draft）；状态：OPEN_RESEARCH / M0 项目准入进行中，M2/M3 已有金融与密码学源码证据。静态源码审计不代表项目已独立构建或完整证明。

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

已建立独立 Lean 4.35.0 示例：[PITNoLookahead.lean](examples/pit-no-lookahead/PITNoLookahead.lean)。它区分 eventTime 与 availableAt，证明过滤后的每条记录都不晚于 decisionTime。该示例的 Lean 4.35.0 `lake build` 已由 GitHub Actions Run #19 验证通过；两个 theorem 的 `#print axioms` 均为 `[propext]`。它仍没有实现 latest-revision as-of join。

## 跨学科论文与开源项目地图（2026-11-22）

新增 [field-evidence-matrix.md](field-evidence-matrix.md)：按 10 个领域逐项列出具体研究方向、原始论文/形式化论文、Lean 项目、相邻证明助手/验证工具、项目版本线索和研究空白。首轮已覆盖数学及 9 个非数学领域。

本轮新确认的高价值方向包括：Veil/IFP 的 Lean BFT safety、AI4SLT 的统计学习理论、LeanInfoTheory/率失真形式化、Doll–Shames 的 Lean 控制理论，以及 StatWhy/StarV 等非 Lean 相邻验证工具。

**证据限制：** 外部项目大多为论文/README/toolchain/配置审查，尚未独立 build；项目 README 中的 theorem 数量和 no-sorry 声明不自动升级为本专题 E3。EconCSLib 存在两个同名独立项目；MathFin 和 LeanInfoTheory 的论文/官网/当前 README 有版本统计差异，详见矩阵。

## PIT/no-lookahead 最新构建结果（2026-11-22）

PIT package 的证明源码提交 2cbece7184815f8d17bf09130f66dd024630e51c 已通过 [Lean Actions Run #24](https://github.com/fweiger/AI_book/actions/runs/45031763832)：Lean 4.35.0 lake build success，两个 theorem 均编译，print axioms 均为 [propext]。知识库完整性 [Run #1255](https://github.com/fweiger/AI_book/actions/runs/45031763864) 同样 success。该 proof 仍只覆盖 eligibility filter safety，不是完整 as-of join 或真实数据源验证。


## 研究方向—论文—项目矩阵更新（2026-11-23）

[跨学科证据矩阵](field-evidence-matrix.md) 已扩展为逐研究方向的对应表：每条记录包含研究对象、原始论文/形式化论文、直接 Lean 项目、相邻证明助手或普通实现，以及当前验证边界。覆盖十个领域，不把相邻项目冒充 Lean 项目。

本轮对 MathFin、LeanInfoTheory、rate_distortion_lean4、AI4SLT、TorchLean、DynamicalSystems、Veil/IFP 做了 GitHub 源码与版本线索复核。外部项目构建状态仍为 NOT_RUN；论文、README、源码和 build evidence 分开记载。


## 2026-11-23 CI 回归复验

本轮新增方向矩阵后，首次知识库完整性检查发现 sessions 索引中的一个失效链接；已修复并重新验证。PR head `c45e6d94e30a45bb797019f201baac20d4c17eb8` 的 [Knowledge-base integrity Run #1268](https://github.com/fweiger/AI_book/actions/runs/45043057448) 与 [Lean PIT Run #37](https://github.com/fweiger/AI_book/actions/runs/45043057469) 均 success。PIT 两个 theorem 的 axiom 输出仍为 `[propext]`。外部项目构建未运行。
