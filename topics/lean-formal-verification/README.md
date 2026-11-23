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
- [跨行业递归拆分登记表（60/60 父节点至少拆一层、124 个候选子节点）](industry-recursive-split-register.md)
- [第三层研究地图：8 个 L2 分支→16 个 L3 问题/论文/GitHub](industry-depth3-paper-project-map.md)
- [P0 深度映射 Batch 5：9 个 L2→27 个 L3，CVaR 再拆 2 个 L4](industry-depth3-p0-source-anchors-batch5.md)
- [Batch 5 原始资料及研究边界记录](sessions/2026-11-23-depth3-p0-source-anchors-batch5.md)
- [124 个 L2 节点的叶节点闭合/缺口复核队列](industry-leaf-closure-triage.md)
- [Batch 4：第三层研究与证据分级记录](sessions/2026-11-23-depth3-paper-repo-and-closure-triage.md)
- [跨行业递归 Batch 3：25 父节点新增 50 子问题，首轮父节点覆盖贯通](sessions/2026-11-23-recursive-industry-split-batch3.md)
- [论文—GitHub 项目映射精度核验 Batch 1（9 项纠正）](sessions/2026-11-23-leaf-linkage-verification-batch1.md)
- [行业递归下钻 Batch 2（7 个父节点、12 个新子节点）](sessions/2026-11-23-recursive-industry-split-batch2.md)
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

用户明确要求所有行业分支按业务复杂度递归下钻，不能停在二级/三级；每条研究叶节点必须挂接对应论文/标准和实际 GitHub 项目。当前已形成 [60 个首轮候选父节点](industry-leaf-project-map.md) 与 [124 个候选子节点](industry-recursive-split-register.md)：**60/60 父节点均至少下钻一层**，但这不是 124 个终端研究单元全部闭合；目前已有 [Batch4 的 16 个 L3](industry-depth3-paper-project-map.md) 与 [Batch5 的 27 个 L3/2 个 L4](industry-depth3-p0-source-anchors-batch5.md)，合计 17/30 个 P0 L2 已至少继续下钻一层；[124 节点缺口队列](industry-leaf-closure-triage.md)仍持续核验。后续应继续核验论文—仓库关系、重复复用与必要的更深层递归。项目审计与最小原型留待用户选定方向后进行。


## 2026-11-23｜第二轮项目级递归拆分

首轮 60 个候选父节点不是最终叶节点。本轮新增 55 个更细的子节点，并将状态分为 CANDIDATE_LEAF、LEAF_CLOSED、PAPER_GAP、PROJECT_GAP 和 CONTINUE_SPLIT。项目映射不等于项目审计。


## 2026-11-23｜Batch6：6 个 P0 节点的 17 个 L3 源码/论文入口

[Batch6 源码锚点与单问题研究表](industry-depth3-p0-source-anchors-batch6.md)：补充 OpenVM RV32IM、Zisk RV64IM、EconCSLib 机制设计、LeanForControl、LeanInfoTheory、Sparkle 等六个此前未进入 L3 的 P0 父节点，新增 17 个研究单元。累计 23/30 个 P0 已至少继续一层，60 个 L3 与 2 个 L4；尚余 7 个 P0 待下钻。更新后的 [124 节点 triage](industry-leaf-closure-triage.md) 保持原 P0/P1/P2 分母与未关闭的来源缺口。来源级 E1 不等于外部项目独立 build、证明审计或 LEAF_CLOSED；当前仍以跨行业递归框架及论文—GitHub 项目关联为主线。


## 2026-11-23｜Batch7：剩余 7 个 P0 的 21 个 L3 研究对象

[Batch7 单一问题—论文/官方资料—GitHub 源码/Lean GAP 对照表](industry-depth3-p0-source-anchors-batch7.md)：本轮对 IFP、PIT 历史股票池、SciLean、LegalLean、Concerto、CGM/OpenAPS 和 ClimaCore 七个此前未到 L3 的 P0 各增加 3 个 L3，共 21 个源级研究问题，累计 **30/30 P0 至少再深入一层，81 个 L3、2 个 L4**。对应 [124 L2 triage](industry-leaf-closure-triage.md) 已更新。此为结构研究深度覆盖，不是 LEAF_CLOSED；SciLean `sorry_proof`、LegalLean 的显式演示 axiom、IFP 未完成不变量和 Concerto/CGM/ClimaCore 的 LEAN_GAP 必须保留。下一轮转为 81 L3/2 L4 的逐问题证据闭合核查，再处理 P1/P2，不提前开展无目标项目审计。

## 2026-11-23｜Batch8：83 条 L3/L4 来源级研究闭合门禁

[完整 83 条证据闭合矩阵](industry-leaf-evidence-closure-matrix-batch8.md) 已按 Batch4–7 原始研究行逐项生成并回读；主键核对：**81 个 L3 + 2 个 L4 = 83 个独立登记单元，30/30 P0 至少一层下钻，82 个真正终端叶节点**（因为一个 L3 是两个 L4 的父节点）。从来源精度看，37 个直接 Lean 文件、9 个目录、14 个仓库级、10 个说明/文档、11 个非 Lean 行业项目和 2 个内部示例/任务。上述分类不是 proof PASS 或 LEAF_CLOSED。现需优先为 23 个仓库/目录级入口补齐准确代码/定理锚点及论文—项目直接性，再逐项判据闭合和处理 P1/P2 94 个 L2；不提前做无目的的外部项目审计与最小原型。


## 2026-11-23｜Batch9：原 23 个 repo/dir 入口全部找到具体源码与声明

[Batch9 23 条具体源文件/定理锚点清单](industry-repo-dir-source-anchors-batch9.md) 已 GET 回读，覆盖 Batch8 仍为 14 个仓库级 + 9 个目录级的研究单元；Lean-MLIR、VCVio、Brownian、MathFin、StatsMLlib、TorchLean、SP1、Resonate、ArkLib 均按单问题匹配文件与实际声明。**23/23 为文件级来源闭合，不是 Lean theorem/kernel PASS 或 23 个独立仓库验收**；SP1 decode、Resonate 全性质、ArkLib Interaction 迁移、TorchLean Float/CUDA 等仍有具体证明缺口。历史 [Batch8 全量矩阵](industry-leaf-evidence-closure-matrix-batch8.md) 已标明 23 个弱入口状态被本轮证据覆盖；登记口径仍为 83 个研究单元/82 个终端/30 P0。当前唯一下一步转向其余 **10 个文档级原始研究入口**，仍不转无目的的外部项目审计与原型。

## 2026-11-23｜Batch10：剩余 10 个文档级来源全定位至源码

[Batch10 文档级 10 项 Lean 源文件/性质/证明前提清单](industry-doc-to-source-anchors-batch10.md) 已实际回读：Resonate trace validation、TorchLean backend/CUDA 可信边界、Lean Kernel Verify 五项 GPU KIR 规格、Zisk RV64IM Aeneas 提取/解码桥接、Sparkle pure FSM/Signal DSL 两条。连同 [Batch9 的 23 条](industry-repo-dir-source-anchors-batch9.md)，Batch8 原本 **33 个仓库/目录/文档级弱索引入口已具文件级源码 overlay**，仍不意味着完成形式化证明；Resonate `sorry`、Zisk extraction TCB、LKV KIR/现实 GPU 桥接、Sparkle FSM/RTL refinement、TorchLean FFI/CUDA 均保留。历史 83 登记/82 终端/30 P0 不变。下一步为 **83 项来源级闭合状态判定**，后续进入 P1/P2 94 个 L2；不是无目标项目审计或量化/医疗/硬件原型。

## 2026-11-23｜Batch11：83 个 L3/L4 来源级闭合决策与 P1/P2 主线

[Batch11 全 83 项研究证据闭合矩阵](industry-leaf-source-closure-decisions-batch11.md) 已按 Batch8+9+10 源码一手材料建立并回读；**52 条 SOURCE_LEVEL_CLOSED（仅已限定问题的来源/性质映射）、31 条 REQUIRES_MORE_EVIDENCE（显式未闭合的 proof/信任/论文/非 Lean GAP）**，其中一个 CVaR L3 是两个 L4 的父项，因此 **82 个终端 = 52 个来源级映射闭合 + 30 个待证**。不应把该分类写成 52 个机器证明通过或 82 个叶节点完全验收。

Batch9/10 为历史 **33 个弱索引入口**补齐真实 GitHub Lean 源码文件；依旧单列 Resonate validator `sorry`、IFP 93/103、SciLean `sorry_proof`、LegalLean 显式 `axiom`、SP1/Zisk witness/extraction 前提、TorchLean CUDA/FFI、Sparkle Signal/RTL refinement、金融 PIT membership/latest-as-of，以及 11 个 non-Lean 行业实现。**当前唯一主线**是将同一方法推广到 **P1/P2 的 94 个 L2 节点**，按行业层级继续下钻至真实论文、项目和具名源码；31 个 P0 未完成义务保留为定向证据队列，不再无目标逐项目审计。

## 2026-11-23｜Batch12：P1/P2 横向覆盖开始，12行业→24具体源码研究单元

[Batch12 P1/P2 首批12行业、12个L2父节点→24个实际GitHub源文件L3](industry-depth3-p1p2-source-map-batch12.md) 已回读，原[124个L2登记](industry-recursive-split-register.md)及[triage队列](industry-leaf-closure-triage.md)同步了12个父节点的反向链接。已细拆到L3的父节点由P0 30扩至 **42/124**（新增P1 4+P2 8），原P0的81L3+2L4，加24新L3后累计 **105个L3+2个L4=107登记单元、106终端**。**P1/P2剩82个L2未下钻**。本批不是24个独立GitHub项目、也不是24个定理已通过审计。

样例覆盖 RISC-V Sail→Lean 生成模型、Cedar授权、CompPoly多项式证书、SocialChoiceLean的Pivato定理、LeanLTL交通灯、Langmuir/BET历史Lean3、SBML C++参考、率失真、LeanCopilot建议、Physicslib4 AQFT、Catala F*法律编译、FormalConjectures中仍为`sorry`的猜想。**有些是相邻证明语言或行业程序，不可冒充Lean**；论文直系、相关方法/理论谱系及错误配对均明确分类。下一步只选择其他 **12个未覆盖的P1/P2父节点**进行跨行业第二批下钻，原P0来源级31项开放义务有界保留，不进行无目标审计或新实验。

## 2026-11-24｜Batch13：P1/P2 第二批12行业、24个源码级研究单元

[Batch13 完整 24 项 L3 源码/论文/证明边界地图](industry-depth3-p1p2-source-map-batch13.md) 已提交并实际回读；选中IND01–IND12每行业1个新的P1/P2父节点（共P1=4、P2=8），与[Batch12首批12父/24子](industry-depth3-p1p2-source-map-batch12.md)严格不重复；原[124 L2父登记](industry-recursive-split-register.md)和[triage研究队列](industry-leaf-closure-triage.md)均已为本批12个父行增加双向可导航链接。

**累计树：54/124个L2已有L3（30 P0 + 24 P1/P2），129 L3+2 L4 = 131登记研究单元、130个真正终端**；剩余P1=39、P2=31，合计70个L2尚未到第三层。本批24项都是`SOURCE_MAPPED_WITH_SCOPE`而非`LEAF_CLOSED`或Lean kernel PASS。源证包括CertifyingDatalog的Lean tree/DAG checker定理、Aeneas FRI局部证明但ArkLib接口有`sorry`、Sparkle AXI4-Lite FSM与Signal精化缺口、Matheconlib及DynamicalSystems的数学定理；KeYmaera X Scala/dL、ESBMC-PLC+ SMT/BMC、VerifiableP4 Coq、αβ-CROWN Python、ElectionGuard Rust verifier、HL7 FHIR XML和leanblueprint Python工具均按语言/工程边界标注，不能冒称Lean证明。下一步优先第三批**约12个新的P1/P2父节点**继续横向下钻，保留P0原31条有界待证队列。
