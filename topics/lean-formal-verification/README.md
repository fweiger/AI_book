# TOPIC-018｜Lean 形式化证明与跨学科可验证系统

> 规范研究任务：[AI_book Issue #74](https://github.com/fweiger/AI_book/issues/74)  
> Task ID：AI-BOOK-TOPIC-018-LEAN-FORMAL-VERIFICATION  
> 建立：2026-11-22；专题版本：0.8.0（Draft）；状态：OPEN_RESEARCH / M2 行业应用框架搭建中。当前先完成行业—业务场景—形式化问题—Lean 能力框架，论文和 GitHub 项目作为下游证据，项目审计按具体方向需要触发。

## 最初的问题

Lean 如何把数学猜想、定义和证明转化为机器可检查的形式化对象？除数学以外，软件工程、密码学、分布式系统、经济学、金融、AI、物理学等领域如何实际使用 Lean？研究者具体采用哪些证明策略、工具、工程流程和 AI 协作技巧？

## 核心研究框架

**行业 → 业务领域/价值链 → 具体场景 → 业务问题 → 可形式化对象 → 目标性质 → Lean 能力与适配边界 → 论文 → GitHub 项目 → 按需审计 → 原型/应用验证。**

本专题首先回答 Lean 能在哪些行业和业务领域解决什么问题。Lean 的定理证明、规格建模、可执行参考模型、程序精化和数学库是解决问题的能力，不是研究目标本身。先建立行业应用框架，再从具体机会寻找论文和项目；未选定方向前不开展大批 GitHub 项目审计。

## 术语边界

- **Lean 4**：基于依赖类型理论的交互式定理证明器，同时也是函数式编程语言。
- **Lean Kernel**：检查证明项的可信核心；tactic 生成的证明项仍由 Kernel 检查。
- **Mathlib**：社区维护的 Lean 数学库，提供定义、定理、结构层级和自动化工具。
- **Elan**：Lean 工具链/版本管理器，不是证明器或证明内核。
- **Lake**：Lean 项目的构建与依赖管理工具。
- **Blueprint**：大型形式化项目的数学文档、定理依赖和 Lean 声明之间的可追踪组织方式。

任何项目都应锁定自身 lean-toolchain、依赖版本和 commit；不能把某个项目在特定版本下的构建结果推广到其他版本。

## 导航

- [Lean 跨行业应用研究框架（主框架）](industry-application-framework.md)
- [行业应用机会地图](industry-opportunity-map.md)
- [首轮行业候选节点地图（12 行业 / 60 父节点）](industry-leaf-project-map.md)
- [递归拆分登记表（55 个初始子节点 + 本轮追加 7 个 = 62 个候选子节点）](industry-recursive-split-register.md)
- [论文—GitHub 项目映射精度核验 Batch 1（9 项纠正）](sessions/2026-11-23-leaf-linkage-verification-batch1.md)
- [应用机会卡模板](application-opportunity-card-template.md)
- [已有领域证据与论文—项目资源索引（支撑层）](field-map.md)
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


## 2026-11-23｜代表项目审计批次 A

已对三个与论文直接关联的项目固定 commit 并审计源码、许可证、toolchain、manifest、核心 theorem 和构建证据：

- [Rate-Distortion](https://github.com/fubinyan/rate_distortion_lean4)：旧 commit 有 3161-job build log，但当前 source 在 2026-10-13 大改；当前 build NOT_RUN，license 未找到，CI workflow 与 README 声明不一致。
- [AI4SLT](https://github.com/YuanheZ/lean-stat-learning-theory)：v4.32.0 release 报告 Lean 4.32.0 build PASS 与 SLT/ no-placeholder scan；当前 main 仅比 release 多 README 更新。
- [Veil](https://github.com/verse-lab/veil)：main 固定 commit 的 [Run #442](https://github.com/verse-lab/veil/actions/runs/45014566842) 在 Linux/macOS build/test PASS；TrustAudit 的 7 条 shipped route 和 positive control 均 PASS；可信 SMT 与 sorryAx 边界已记录。

本轮新增 M-19/M-20、C018-061—068 和三张项目审计卡。AC-05 仍 PARTIAL：Rate-Distortion 当前版本未 build；外部项目没有本专题独立构建。


## 2026-11-23｜研究顺序纠偏

用户明确要求先搭建 Lean 跨行业应用框架，而不是继续进入具体项目审计。当前主线为行业分类、业务领域、具体场景、可形式化问题、Lean 能力、适配边界和价值路径；随后才从具体机会映射论文与 GitHub 项目。已有项目矩阵、案例和 Batch A 审计作为证据资产保留，项目审计仅在选定具体方向并确有复用/原型需要时进行。

详见 [主框架](industry-application-framework.md)、[首版行业机会地图](industry-opportunity-map.md) 和 [应用机会卡模板](application-opportunity-card-template.md)。


## 2026-11-23｜递归下钻至 GitHub 项目叶节点

用户明确要求所有行业分支按业务复杂度递归下钻，不能停在二级/三级；每条研究叶节点必须挂接对应论文/标准和实际 GitHub 项目。当前已形成 [60 个首轮候选父节点](industry-leaf-project-map.md) 与 [62 个候选子节点](industry-recursive-split-register.md)：已有 28 个父节点被继续拆分，尚有 32 个待拆。项目审计与最小原型留待用户选定方向后进行。


## 2026-11-23｜第二轮项目级递归拆分

首轮 60 个候选父节点不是最终叶节点。本轮新增 55 个更细的子节点，并将状态分为 CANDIDATE_LEAF、LEAF_CLOSED、PAPER_GAP、PROJECT_GAP 和 CONTINUE_SPLIT。项目映射不等于项目审计。
