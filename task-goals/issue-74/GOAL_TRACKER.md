# GOAL_TRACKER.md — AI-BOOK-TOPIC-018-LEAN-FORMAL-VERIFICATION

> V1.2.2 L 级任务唯一动态执行文件。规范需求以 [AI_book #74](https://github.com/fweiger/AI_book/issues/74) 为准；本 Tracker 不修改 Issue 批准的 Goal/Scope/AC。

## 任务身份

- 规范任务 Issue：[AI_book #74](https://github.com/fweiger/AI_book/issues/74)
- 所属源仓库：fweiger/AI_book
- 项目入口：[TOPIC-018 README](https://github.com/fweiger/AI_book/blob/topic/TOPIC-018/lean-formal-verification-20261122/topics/lean-formal-verification/README.md)
- 本文件路径：task-goals/issue-74/GOAL_TRACKER.md
- 当前阶段：M0/M2/M3｜项目准入、跨学科案例和方法库并行推进
- 创建时间：2026-11-22
- 最近更新：2026-11-22（MathFin + PIT prototype checkpoint）
- 批准需求修订号：v1.0
- 选定协议路径/候选分支：task-center/v1.2.2/ENTRY.md / experiment/task-center-v1.2.2-continue-goal-guard-20261119
- **锁定执行协议 commit SHA：** f0e5ccb90c54265dcd07abb9a975c903eb031ccf
- 本轮 Tracker 写入前观察到的最新分支 HEAD：5cd30e0420af8918fc2f519bba48efd00c48427e
- 最新规范 Issue 读取时间与修订：2026-11-22；初始批准版 v1.0
- 本轮写入前 Tracker blob SHA：ebfc2460821ac5bfdc4fdeba9ea52cfb541c84b4；写入后以 GET 回读 SHA 为准
- 目标漂移状态：D0（Hax/Aeneas、MathFin 和 PIT 原型均直接推进 AC-03/04/05/06；没有接管 AI_Trader #488）
- 状态一致性：STATE_CONFLICT（专题文件已推进至 v0.6.1，但 Tracker/Issue 仍停留在 Hax 上游审计事件；本轮同步后再回读裁决）
- Issue 同步状态：ISSUE_SYNC_PENDING（本轮 MathFin + PIT prototype 事件待写入 Issue 并 GET 回读）

## 1. 批准目标基线

- **原始 Goal：** 建立一套以真实论文、官方文档、可回读源码和可复现实验为基础的 Lean 形式化证明与跨学科应用知识体系，研究 Lean 在数学中的猜想/定理形式化和证明工程，以及软件、密码学、分布式系统、经济学、金融、AI、物理、信息论等领域的真实应用、方法、技巧和边界。
- **Scope：** Lean 4/Kernel/Mathlib/Elan/Lake/Blueprint 技术体系；数学应用；跨学科项目和论文；证明技巧与工程方法；AI Agent 工作流；与 AI_Trader #488 的金融应用关联。
- **Non-goals：** 不承诺证明任意未解猜想；不把 Lean 当自动发现所有数学真理的系统；不把 theorem 通过等同于假设真实、实现已验证或策略盈利；不替换 Python 回测引擎、不改生产/交易、不上传受限或版权资料。
- **核心 AC：** AC-01 技术体系准确；AC-02 数学案例；AC-03 跨学科证据地图；AC-04 至少 12 张方法卡；AC-05 至少 10 个代表项目审计；AC-06 最小可复现工作流；AC-07 与 #488 边界正确；AC-08 独立验收。

| AC ID | 可观察的验收条件 | 验证方法 | 当前状态 | 证据链接 |
|---|---|---|---|---|
| AC-01 | Lean 4/Kernel/Mathlib/Elan/Lake/Blueprint 职责有官方依据 | 官方文档/源码对照 | partial | [Language Reference](https://lean-lang.org/doc/reference/latest/) · [case-studies.md](https://github.com/fweiger/AI_book/blob/topic/TOPIC-018/lean-formal-verification-20261122/topics/lean-formal-verification/case-studies.md) |
| AC-02 | 多数学分支至少 8 个真实代表案例，证明状态清楚 | 源码、论文、Blueprint 逐项核验 | not_run | [Lean Projects](https://leanprover-community.github.io/lean_projects.html) |
| AC-03 | 至少 6 个非数学领域完成项目/论文证据审查 | 项目与论文原文、源码核对 | partial | [field-map.md](https://github.com/fweiger/AI_book/blob/topic/TOPIC-018/lean-formal-verification-20261122/topics/lean-formal-verification/field-map.md) |
| AC-04 | 至少 12 张可复用方法卡含步骤和失败边界 | 每张卡的源码/文档/最小示例 | partial | [methods-and-tactics.md](https://github.com/fweiger/AI_book/blob/topic/TOPIC-018/lean-formal-verification-20261122/topics/lean-formal-verification/methods-and-tactics.md) · M-01—M-15 已有 15 个唯一方法 ID；独立 QA/build 未完成 |
| AC-05 | 至少 10 个代表项目核对元数据、许可证、toolchain、构建/CI | GitHub 元数据、源码、CI、复现日志 | partial | [case-studies.md](https://github.com/fweiger/AI_book/blob/topic/TOPIC-018/lean-formal-verification-20261122/topics/lean-formal-verification/case-studies.md) |
| AC-06 | 一条 Lean 项目最小流程可复现 | 固定环境/依赖并执行 build | partial | [PIT no-lookahead package](https://github.com/fweiger/AI_book/tree/topic/TOPIC-018/lean-formal-verification-20261122/topics/lean-formal-verification/examples/pit-no-lookahead) · [workflow](https://github.com/fweiger/AI_book/blob/topic/TOPIC-018/lean-formal-verification-20261122/.github/workflows/lean-pit-no-lookahead.yml)；配置已建，build NOT_RUN |
| AC-07 | 与 AI_Trader #488 关联但不重复/接管其量化实验 | 两 Issue Goal/Scope/AC 对照 | partial | [AI_Trader #488](https://github.com/fweiger/AI_Trader/issues/488) · [PIT boundary](https://github.com/fweiger/AI_book/blob/topic/TOPIC-018/lean-formal-verification-20261122/topics/lean-formal-verification/field-map.md) |
| AC-08 | 非主要研究者独立审查数学案例、跨学科案例和方法库 | 独立 QA 报告与复现 | not_run | |

## 2. 目标贡献

- **它为什么值得做：** 形式化证明已经从纯数学扩展到软件、密码学、经济学、金融和 AI 等领域；但不同领域对“证明”的对象、假设和现实映射不同，容易出现概念混用。
- **它对项目/上级目标的贡献：** 为 AI_book 建立可持续的形式化证明知识专题，沉淀跨学科案例与可迁移的方法卡；为 AI_Trader #488 提供已核验的金融数学和程序验证方法。
- **完成后应产生的可观察结果：** 形成有源码/论文/版本证据的领域地图、项目审计表、至少 12 张方法卡、最小可复现工作流和独立审查。
- **不能被局部问题替代的核心研究问题：** 不仅要证明 Lean 可以在某个领域写 theorem，还要说明它实际验证了什么、假设是什么、如何连接实现/经验对象，以及方法是否能迁移。

## 3. 当前执行路径

| 阶段 | 预期结果 | 对应目标/AC | 验证证据 | 状态 | 依赖/备注 |
|---|---|---|---|---|---|
| M0 资料与项目准入 | 官方文档、代表项目、论文、版本和许可证准入矩阵 | AC-01/03/05 | 官方来源、repo metadata、固定 commit | in_progress | 10+ 项目有固定 commit/部分元数据；构建和部分许可仍待核 |
| M1 数学应用与证明工程 | 数学分支案例、Mathlib 复用和大型证明方法 | AC-02/04 | Lean 源码、论文、Blueprint | todo | MathFin 金融数学案例已审，纯数学分支仍待深入 |
| M2 跨学科应用地图 | 至少 6 个非数学领域案例和限制 | AC-03/05 | 源码、论文、版本和 CI | in_progress | 密码学/软件验证、金融已深审；其他领域仍是初步地图 |
| M3 方法技巧与 AI 工作流 | 方法卡、Playbook、AI Agent 审查流程 | AC-04/06 | 最小可复现项目和方法证据 | in_progress | 15 个唯一方法 ID；PIT 最小 proof package 已建但 build NOT_RUN |
| M4 综合图谱与独立 QA | 证据审计、Draft PR、独立复核 | AC-07/08 | PR、CI、独立 QA 报告 | todo | 等待非主要研究者独立审查，不未经批准合并 |

## 4. 当前检查点

- **最近完成的一轮：** 2026-11-22 M0/M2/M3 证据审计：Hax/Aeneas 同源 FRI 比较、Hax 上游修复追踪、MathFin 金融数学审计、PIT/no-lookahead 最小 Lean package。
- **本轮实际完成：**
  1. 对 rust-lean 固定 commit 的 Hax/Aeneas 两条 pipeline 做同源比较；两边使用相同 blob SHA 的 compute_log_arity_for_round Rust 源码。
  2. 审计 Hax issues/PR，确认 cast/specset/ADC 等后续上游修复；识别 Hax-FRI 固定 Hax commit 早于关键修复。
  3. 深审 MathFin，读取 coverage taxonomy、AxiomAuditGen、build workflow、CVaR、Markowitz、CRR 等；解析三个 benchmark JSON 共 156 项。
  4. 建立独立 Lean 4.35.0 PIT/no-lookahead package，加入 availableAt/decisionTime filter theorem、late-revision 示例和专用 GitHub Actions workflow。
  5. 专题更新至 v0.6.1；方法库有 15 个唯一方法 ID；图谱 34 个节点、11 条阅读路径；Draft PR #75 保持未合并。
- **已经核验的结果：**
  - Hax-FRI 的 FoldingCorrectness 有两个实质性边界定理源码证明；该文件仍有 4 个 sorry，BasicProofs 有 9 个 sorry。
  - Aeneas 的 BasicProofs 有 6 个 theorem + 3 个 example，静态扫描无显式 sorry/axiom/opaque；其 ArkLib bridge 另有 3 个 axioms、1 个 opaque 和 4 个 sorry。
  - Hax/Aeneas 比较只针对同一 Rust 函数，不据此推断工具普遍优劣。
  - MathFin README 报告 906 项；本轮只独立解析 risk/portfolio/binomial 三个 JSON 共 156 项且均标记 full。AxiomAuditGen 声明覆盖 1,115 个 MathFin 常量和 29 个上游常量。
  - PIT prototype 的 Lean 源码、Lake package、toolchain 和 workflow 已写入分支；没有取得 workflow run，build 仍 NOT_RUN。
  - 历史 GitHub Actions run #1201 只验证旧 commit 的知识库结构/链接/YAML，不是 Lean build。
- **尚未验证/失败/未知：**
  - 所有 Lean/Lake build 均 NOT_RUN；当前执行环境无 Lean/Lake/Elan/Rust/Cargo，Runner registry 未发现 rust-lean/Lean 项目。
  - 当前 PR head 未返回 workflow run；新 PIT workflow 仅存在于 Draft PR 分支。
  - 未独立复现 MathFin 完整 corpus、Hax 官方 ADC example、Hax-FRI 或 Aeneas FRI build。
  - 未运行 #print axioms 的实际 Kernel 输出；静态扫描不等于 Lean build。
  - 未完成完整 as-of join/latest-revision 证明；未修改 AI_Trader #488。
  - 非主要研究者独立 QA 尚未执行。
- **对原始目标的实际贡献：** 从项目名录推进到固定源码/依赖/证明状态审计；形成密码学、软件验证和金融数学案例；15 张方法卡；建立第一份面向 PIT/no-lookahead 的可执行 Lean 规格原型。
- **当前阶段判断：** M0/M2/M3 并行进行；M1 纯数学案例和 M4 独立 QA 尚未完成。
- **本轮 AC 与目标对齐证据：** AC-03/04/05 有实质推进；AC-06 已有最小项目和 workflow 配置但无 build；AC-07 只完成边界定义，不代表已接入 #488。
- **目标漂移 D0/D1/D2/UNKNOWN 及理由：** D0；全部动作仍围绕 Lean 数学/跨学科方法、源码审计与金融 PIT 形式化边界，没有修改 #488 或转入实证策略开发。
- **状态一致性 CONSISTENT/STATE_CONFLICT/UNKNOWN 及理由：** 当前 Tracker 正在同步本轮 MathFin/PIT 事件；同步完成并回读前暂记 STATE_CONFLICT，之后重新裁决。

## 5. 阻断与未受影响工作

| 问题 | 实际影响范围 | 受影响阶段/AC | 未受影响、仍可继续的工作 | 处理决定 |
|---|---|---|---|---|
| 当前执行环境没有 Lean/Lake/Elan/Rust/Cargo；可见 Runner 项目目录未发现 Lean/rust-lean workspace；当前 PR head 无 workflow run | 无法对 PIT、Hax、Aeneas、MathFin 执行 Kernel build | M0/M3、AC-05/06 | 源码、manifest、proof status 和方法研究可继续 | 所有 build 明确 NOT_RUN；下一步需要授权 Runner 或可运行的 CI 环境 |
| Hax/Aeneas FRI 集成仍有 sorry/axiom/opaque | 完整 FRI 协议正确性尚未闭合 | M2/M3、AC-03/04/05 | 同源函数的局部证明比较和其他密码学方法仍可研究 | 不把局部 BasicProofs 说成完整 FRI 验证 |
| MathFin CI workflow 与 reproduce.sh 已读取，但没有本轮实际运行结果 | 无法独立验证 156 项之外的全 corpus 或 build | M2/M3、AC-05/06 | 可继续审查单项 theorem、scope 和 proof method | 只报告源码与 benchmark 状态，不报告本轮 build PASS |
| PIT 原型只证明 availableAt filter safety | 尚未证明 latest eligible revision、排序、tie-break、timestamp authenticity 和生产 as-of join | M3、AC-06/07 | 该最小 invariant 可独立完善 | 先取得 build 结果，再扩展 latest-version semantics；不接管 #488 |
| 纯数学分支与其余跨学科领域仍未深审 | 数学案例数量和领域覆盖未达最终 AC | M1/M2、AC-02/03 | 已有数学/软件/金融材料可继续 | 按固定来源逐项审计，不凑数量 |

## 6. 执行路径调整记录

| 时间 | 原路径 | 调整后路径 | 原因与证据 | 对目标/AC 的影响 | 是否需要用户批准 |
|---|---|---|---|---|---|
| 2026-11-22 | 无 | 先建立跨领域证据地图，再逐项目深入审计 | 用户要求同时覆盖数学和非数学应用，并收集方法技巧 | 推进 AC-01/03/05，不改变 Goal/AC | 否 |
| 2026-11-22 | 逐项目分别阅读 Hax 或 Aeneas 的宣传材料 | 固定同一 Rust blob，做 Hax/Aeneas 同源比较；随后审计 MathFin 与 PIT 时间不变量 | 两个 FRI 子项目存在完全相同的 Rust 源文件；MathFin 提供金融数学定理；量化场景需要区分 eventTime 与 availableAt | 推进 AC-03/04/05/06；不接管 AI_Trader #488，不改变 Goal/Scope/AC | 否 |

## 7. 下一步

- **唯一优先动作：** 在一个已授权且具备 Lean 4.35.0/Elan/Lake 的 Runner 中，对 `topics/lean-formal-verification/examples/pit-no-lookahead` 执行 `lake build`，保留完整版本指纹和日志，并读取 `#print axioms` 输出；若无法获得 Runner，则等待用户批准将该 workflow 纳入可执行的 base branch 后再验收。
- **对应未完成 AC 与当前阶段：** AC-06；M3。
- **为什么它推进原始目标：** 当前已经有第一份 PIT/no-lookahead Lean 规格源码，但没有 Kernel build 证据；先验证最小 proof，比继续扩写未编译的复杂 as-of join 更能推进“最小可复现工作流”。
- **预期实质交付物与完成条件/验证方法：** 固定 Lean 4.35.0；`lake build` 返回成功；`eligibleRows_no_lookahead` 和 late revision exclusion theorem 由 Kernel 编译；保存日志并核对 axiom 输出。失败则按实际编译错误修复，不能提前报告 PASS。
- **需要先读取或检查的证据：** 当前 PR #75 head、专用 workflow 状态、Lean toolchain、Lake package、PITNoLookahead.lean。
- **若受阻，下一项不受影响的工作：** 深审 MathFin 的其他风险/概率/投资组合 theorem，或补齐 M1 纯数学案例；不转入 A 股策略回测。
- **为什么本动作优于其他候选动作：** 已经建立了代码和 workflow 配置；此时最关键的不确定性是编译/Kernel 验收，而不是再增加项目名称或方法卡。
- **局部调查边界/止损条件：** 只验证当前 filter safety proof；不在同一轮扩展完整 as-of join，不修改 AI_Trader #488，不修改生产数据/策略。

## 8. 每次“继续”前的恢复核对

- [ ] 按锁定 commit SHA 恢复 V1.2.2 ENTRY/CONTINUE；不自动切换分支 HEAD。
- [ ] 回读 AI_book #74 Goal/Scope/Non-goals/AC 与最新事件。
- [ ] 回读本 Tracker 最新版本、blob SHA 和唯一下一步。
- [ ] 核对当前专题分支、PR、文件、CI 和研究来源。
- [ ] 独立判断 D0/D1/D2/UNKNOWN 与 CONSISTENT/STATE_CONFLICT/UNKNOWN。
- [ ] 将历史 next_action 视为候选，重新选择最高价值 AC 动作。
- [ ] 不修改批准 Goal/Scope/AC；不接管 AI_Trader #488 的实验状态。

## 9. 执行检查点历史（追加，不覆盖）

| 时间/批次 | 实际工作与结果 | AC 贡献 | 证据链接 | 偏差/一致性、阻断或路线调整 | 本轮建议下一步 |
|---|---|---|---|---|---|
| 2026-11-22 / INIT | 查重专题编号和既有 Issue；创建 AI_book #74；建立专题文件、唯一 Tracker、索引导航和 Draft PR #75。未运行 Lean 构建、未逐项目核验所有许可证和源码。 | AC-01/03/05 PARTIAL；AC-02/04/06/08 NOT_RUN；AC-07 边界已定义但未验收。 | [Issue #74](https://github.com/fweiger/AI_book/issues/74) · [Draft PR #75](https://github.com/fweiger/AI_book/pull/75) | D0 / CONSISTENT；Issue 已回链 Tracker 与 PR 并 GET 回读。 | M0 版本化项目准入矩阵。 |
| 2026-11-22 / CI-STRUCTURE | 对 PR head commit e57491d00728fdfba2f5a26cf7df00fd41d27f63 运行仓库完整性 workflow；validate-knowledge 与 Discussion YAML 检查均 PASS。未运行 Lean 构建。 | 结构/链接/YAML 校验 PASS；AC-01/03/05 仍仅 PARTIAL，AC-02/04/06/08 NOT_RUN。 | [Workflow run #1201](https://github.com/fweiger/AI_book/actions/runs/45007709196) · [Draft PR #75](https://github.com/fweiger/AI_book/pull/75) | D0 / CONSISTENT；CI 仅为知识库结构校验，不提升学术证据等级。 | M0 版本化项目准入矩阵。 |
| 2026-11-22 / M0-MANIFEST | 对 10 个固定仓库 commit 读取 README/toolchain/许可证/Lake 配置；8 个 Lean 4 项目 Lake manifest 成功解析并记录依赖 revision。未运行项目 build。 | AC-05 PARTIAL；AC-02/04/06/08 NOT_RUN。 | [case-studies.md](https://github.com/fweiger/AI_book/blob/topic/TOPIC-018/lean-formal-verification-20261122/topics/lean-formal-verification/case-studies.md) · [manifest audit session](https://github.com/fweiger/AI_book/blob/topic/TOPIC-018/lean-formal-verification-20261122/topics/lean-formal-verification/sessions/2026-11-22-lake-manifest-audit.md) | D0 / CONSISTENT；项目构建 NOT_RUN。 | 补齐非标准项目边界。 |
| 2026-11-22 / HAX-UPSTREAM | 核对 Hax issues/PR；确认 #1925/#1927/#1933/#2142 merged，识别 Hax-FRI 固定 commit 早于关键修复，Hax 0.5.0 已升至 Lean 4.35。未运行构建。 | AC-04 方法卡增补；AC-05 PARTIAL；AC-06 NOT_RUN。 | [Hax audit session](https://github.com/fweiger/AI_book/blob/topic/TOPIC-018/lean-formal-verification-20261122/topics/lean-formal-verification/sessions/2026-11-22-hax-upstream-fix-and-version-drift.md) · [PR #1925](https://github.com/pereq-dev/hax/pull/1925) · [PR #1933](https://github.com/pereq-dev/hax/pull/1933) · [PR #2142](https://github.com/pereq-dev/hax/pull/2142) | D0 / CONSISTENT；上游修复与目标项目采用状态分开。 | 继续核验 MathFin 与 PIT 原型。 |
| 2026-11-22 / MATHFIN-PIT | 深审 MathFin 的 CVaR/Markowitz/CRR、formalization fidelity 和 axiom audit；建立 Lean 4.35 PIT filter safety prototype 与专用 workflow；整理 M-01—M-15、claims 和图谱。 | AC-03/04/05 PARTIAL；AC-06 PARTIAL（workflow 配置已建，build NOT_RUN）；AC-07 PARTIAL。 | [MathFin session](https://github.com/fweiger/AI_book/blob/topic/TOPIC-018/lean-formal-verification-20261122/topics/lean-formal-verification/sessions/2026-11-22-mathfin-finance-audit.md) · [PIT session](https://github.com/fweiger/AI_book/blob/topic/TOPIC-018/lean-formal-verification-20261122/topics/lean-formal-verification/sessions/2026-11-22-pit-no-lookahead-prototype.md) · [PIT proof](https://github.com/fweiger/AI_book/blob/topic/TOPIC-018/lean-formal-verification-20261122/topics/lean-formal-verification/examples/pit-no-lookahead/PITNoLookahead.lean) | D0 / STATE_CONFLICT pending sync；MathFin corpus 只独立抽查 156 项，PIT build 未运行。 | 对 PIT Lean 4.35 package 执行 lake build。 |

## 10. 最近一次状态一致性回读

- **当前 active_event_key：** AI-BOOK-TOPIC-018-LEAN-FORMAL-VERIFICATION|M0|MATHFIN-PIT-PROTOTYPE-20261122
- **当前 writer_owner：** chatgpt-session-20261122-topic018-init
- **当前 write_state：** CLAIMED
- **最近完成的 event_key：** AI-BOOK-TOPIC-018-LEAN-FORMAL-VERIFICATION|M0|HAX-UPSTREAM-FIX-AUDIT-20261122
- **旧 Writer 已停止/隔离证据：** not_applicable（本轮无并发 Writer）
- **若无法 fencing：** 不适用

| 项目 | 最新核对值 | 证据/版本 | 结果 |
|---|---|---|---|
| 规范 Issue Goal/Scope/AC 与本文件§1 | Issue #74 v1.0 与 Tracker 基线一致 | [Issue #74](https://github.com/fweiger/AI_book/issues/74) | PASS |
| §3/§4当前阶段与实际证据 | M0/M2/M3 进行中；Lean build NOT_RUN | 本轮 case-studies / methods / PIT package | PARTIAL |
| §5阻断与未受影响工作 | 当前缺 Lean Runner；静态研究仍可继续 | §5 | CONSISTENT |
| §6路径变更与第7节裁决 | 已从项目初筛推进到 MathFin 与 PIT proof；下一步优先实际 build | §6/§7 | PASS |
| §7唯一当前下一步 vs §9历史最后建议 | 均指向 PIT Lean package build | §7/§9 | PASS |
| 最新 Issue 进度事件与本文件版本 | 本轮事件尚待写入 Issue 并 GET 回读 | Issue #74 · Draft PR #75 · 当前 event key | ISSUE_SYNC_PENDING |

