# TOPIC-018｜第三层递归：问题 → 证明目标/算法 → 原始论文 → GitHub（Batch 4）

> 日期：2026-11-23 · 规范 Issue [#74](https://github.com/fweiger/AI_book/issues/74) / [PR #75](https://github.com/fweiger/AI_book/pull/75)  
> 父表：[124 个候选 L2 节点](industry-recursive-split-register.md)  
> **本轮新增：8 个 L2 父节点 → 16 个 L3 叶节点候选。** 这些是下一层的研究映射，不代表 16 个项目，也不代表外部证明/代码审计成功。  
> 本阶段不构建、复现、部署、交易或测试外部项目。

## 1. 递归选择依据

以当前 124 个候选子节点为入口，挑选“包含多种数学结构、证明目标或代码模块”的 8 个方向继续下钻，覆盖半导体编译器、密码协议、金融概率与衍生品、AI 统计理论、AI 模型图验证。每个更深层节点必须明确：
1. 独立技术问题是什么。
2. Lean 或相邻工具实际建模哪个对象/验证哪类性质。
3. 论文、标准、项目研究说明分别是什么证据类型。
4. GitHub **真实仓库**、原论文 artifact 或后继项目的位置；不能仅挂 Issue/文档网页。
5. 没做独立源码/构建 QA 的研究结论只可标 `L3_MAPPING_E1`，不直接 `LEAF_CLOSED`。

## 2. 16 个第三层候选研究节点

| L3 ID | L2 父节点 | 可独立研究的具体问题 | 形式化对象 / 目标性质 | 论文及原始研究 | 实际 GitHub 项目 | 来源映射分类与限制 |
|---|---|---|---|---|---|---|
| `IND01-03-A-01` | `IND01-03-A` | SSA IR 的区段、操作、作用域语义 | SSA.Core/region semantics；类型与 denotation 语义模型 | [论文/学术证据](https://doi.org/10.4230/LIPIcs.ITP.2024.9) | [GitHub 仓库](https://github.com/opencompl/lean-mlir/tree/ITP24) | DIRECT_COMPANION / L3_MAPPING_E1；ITP 2024 论文指向 ITP24 artifact；非任意 LLVM 优化正确性 |
| `IND01-03-A-02` | `IND01-03-A` | SSA peephole rewrite 的 denotation 保持 | rewritten ops、rewrite correctness、denote_rewritePeepholeAt | [论文/学术证据](https://doi.org/10.4230/LIPIcs.ITP.2024.9) | [GitHub 仓库](https://github.com/opencompl/lean-mlir/tree/ITP24) | DIRECT_COMPANION / L3_MAPPING_E1；README 列出对应 theorem，未运行证明构建 |
| `IND03-01-A-01` | `IND03-01-A` | 带 oracle 的密码游戏程序怎样作可组合语义表示 | OracleSpec、OracleComp free monad、oracle query/bind 语义 | [论文/学术证据](https://eprint.iacr.org/2026/899) | [GitHub 仓库](https://github.com/Verified-zkEVM/VCVio) | DIRECT_PROJECT_FAMILY / L3_MAPPING_E1；框架定义不等于某个密码协议已安全 |
| `IND03-01-A-02` | `IND03-01-A` | 密码游戏的胜率/统计距离怎样对应概率测度 | ProbComp、evalDist、Pr{event}、distribution equality | [论文/学术证据](https://eprint.iacr.org/2026/899) | [GitHub 仓库](https://github.com/Verified-zkEVM/VCVio) | DIRECT_PROJECT_FAMILY / L3_MAPPING_E1；lossless 与失败质量条件须单独检查 |
| `IND03-01-B-01` | `IND03-01-B` | oracle 查询的处理器实现是否满足模拟语义 | simulateQ、QueryImpl、查询替换和 transcript | [论文/学术证据](https://eprint.iacr.org/2026/899) | [GitHub 仓库](https://github.com/Verified-zkEVM/VCVio) | DIRECT_PROJECT_FAMILY / L3_MAPPING_E1；不是外部生产协议的 refinement 证明 |
| `IND03-01-B-02` | `IND03-01-B` | 概率 Hoare/pRHL 游戏跳转如何传递事件优势 | VCVio.ProgramLogic、by_hoare、game_trans 等策略与关系规则 | [论文/学术证据](https://eprint.iacr.org/2026/899) | [GitHub 仓库](https://github.com/Verified-zkEVM/VCVio) | DIRECT_PROJECT_FAMILY / L3_MAPPING_E1；specific security bounds 未审计 |
| `IND04-01-A-01` | `IND04-01-A` | 如何从高斯有限维分布构造布朗运动的过程律 | Kolmogorov consistency/extension、Gaussian finite-dimensional laws | [论文/学术证据](https://arxiv.org/abs/2511.20118) | [GitHub 仓库](https://github.com/RemyDegenne/brownian-motion) | DIRECT_COMPANION / L3_MAPPING_E1；作者 README 描述构造完成；不扩张为随机积分已完成 |
| `IND04-01-A-02` | `IND04-01-A` | 布朗运动的连续样本路径在何条件下成立 | Kolmogorov–Chentsov continuity、path modification、假设条件 | [论文/学术证据](https://arxiv.org/abs/2511.20118) | [GitHub 仓库](https://github.com/RemyDegenne/brownian-motion) | DIRECT_COMPANION / L3_MAPPING_E1；README 确认此部分属于 Brownian 构造，Itô 半鞅积分仍在推进 |
| `IND04-02-A-01` | `IND04-02-A` | CRR 上/下跳参数的无套利条件何时成立 | crrUp、crrDown、crrPerStepRate、binomialNoArb_crr | [论文/学术证据](https://arxiv.org/abs/2606.01356) | [GitHub 仓库](https://github.com/formal-applied-math/formal-mathfin) | DIRECT_PROJECT_PAPER / L3_MAPPING_E1；作者 README 给出所需参数条件，不推广为无条件无套利 |
| `IND04-02-A-02` | `IND04-02-A` | 二叉树欧式 call 定价收敛于 Black–Scholes 的条件 | binomialPrice_call_tendsto_bs_closed、Tendsto、参数限制 | [论文/学术证据](https://arxiv.org/abs/2606.01356) | [GitHub 仓库](https://github.com/formal-applied-math/formal-mathfin) | DIRECT_PROJECT_PAPER / L3_MAPPING_E1；README 说明 |r|√T<σ 等条件，未单独运行 theorem |
| `IND09-01-A-01` | `IND09-01-A` | Gaussian Poincaré 不等式如何成为集中界的基础 | gaussianPoincare、measure/gradient assumptions、Sobolev density | [论文/学术证据](https://proceedings.mlr.press/v306/zhang26cd.html) | [GitHub 仓库](https://github.com/Lean-MoDS/StatsMLlib) | PAPER_LINEAGE + ACTIVE_CONSOLIDATED_PROJECT / L3_MAPPING_E1；ICML 论文原 SLT，StatsMLlib 现整合库；未证明全部迁移等价 |
| `IND09-01-A-02` | `IND09-01-A` | Lipschitz 高斯函数尾概率能否形式化 | gaussian_lipschitz_concentration、Lipschitz constant 与 tail bound | [论文/学术证据](https://proceedings.mlr.press/v306/zhang26cd.html) | [GitHub 仓库](https://github.com/Lean-MoDS/StatsMLlib) | PAPER_LINEAGE + ACTIVE_CONSOLIDATED_PROJECT / L3_MAPPING_E1；原论文仓库 YuanheZ/lean-stat-learning-theory 应保留作历史 companion |
| `IND09-01-B-01` | `IND09-01-B` | Dudley 熵积分如何为经验过程提供复杂度上界 | covering number、chaining、dudley theorem、metric entropy | [论文/学术证据](https://proceedings.mlr.press/v306/zhang26cd.html) | [GitHub 仓库](https://github.com/Lean-MoDS/StatsMLlib) | PAPER_LINEAGE + ACTIVE_CONSOLIDATED_PROJECT / L3_MAPPING_E1；库多次扩展，按特定模块匹配 |
| `IND09-01-B-02` | `IND09-01-B` | localized least-squares 在哪些假设下得到误差/最优率界 | LeastSquares、master_error_bound、local_gaussian_complexity_bound | [论文/学术证据](https://proceedings.mlr.press/v306/zhang26cd.html) | [GitHub 仓库](https://github.com/Lean-MoDS/StatsMLlib) | PAPER_LINEAGE + ACTIVE_CONSOLIDATED_PROJECT / L3_MAPPING_E1；统计理论命题≠训练系统样本外性能 |
| `IND09-02-B-01` | `IND09-02-B` | 模型计算图的下降转换如何对应可验证图 IR | TorchLean.Verify.Lowering、graph lowering、模型算子语义 | [论文/学术证据](https://arxiv.org/abs/2602.22631) | [GitHub 仓库](https://github.com/lean-dojo/TorchLean) | PRIMARY_PROJECT_README / L3_MAPPING_E1；论文覆盖该具体子模块待核，不默认 DIRECT_COMPANION |
| `IND09-02-B-02` | `IND09-02-B` | 模型/图转换生成的证书如何被 Lean 验证器检查 | TorchLean.Verify、certificate checking、verification entrypoint | [论文/学术证据](https://arxiv.org/abs/2602.22631) | [GitHub 仓库](https://github.com/lean-dojo/TorchLean) | PRIMARY_PROJECT_README / L3_MAPPING_E1；不能把报告 ok 当生产模型全面 correctness |

## 3. 两项必须纠正的论文—项目血缘

### 3.1 布朗运动论文与项目

此前父节点 `IND04-01-A` 使用了 MathFin arXiv 2606.01356 作为关联论文，但布朗运动定义、Kolmogorov extension 和连续样本路径的直接项目论文是 [Degenne 等，Formalization of Brownian Motion in Lean，arXiv:2511.20118](https://arxiv.org/abs/2511.20118)。该论文与 [RemyDegenne/brownian-motion](https://github.com/RemyDegenne/brownian-motion) README 直接相互关联。作者 README 说明布朗运动构造完成、相关成果在向 Mathlib 迁移，但半鞅随机积分与 Itô 引理仍在建设。故不能把布朗运动成果与后续 SDE/Itô 全部算为同一完成的定理。

### 3.2 AI4SLT 原论文与 StatsMLlib 现行整合库

[AI4SLT/ICML 2026](https://proceedings.mlr.press/v306/zhang26cd.html) 原论文的研究仓库为 [YuanheZ/lean-stat-learning-theory](https://github.com/YuanheZ/lean-stat-learning-theory)。[Lean-MoDS/StatsMLlib](https://github.com/Lean-MoDS/StatsMLlib) README 明确称整合了此前 SLT 和 FoML 两条研究线（作者与来源标注保留）。因此：
- `ORIGINAL_PAPER_COMPANION` → `YuanheZ/lean-stat-learning-theory`
- `CURRENT_CONSOLIDATED_PROJECT` → `Lean-MoDS/StatsMLlib`
- 当前整合库额外增加的高维概率、RMT 和一般统计工具不得全部说成是 2026 ICML 论文的原始实验范围。
- 这种“同领域论文→原项目→后继整合库”是一条**项目血缘链**，不是两个独立的 Lean 产业案例。

## 4. L2→L3 深度核验与仍缺的证据

| 类别 | 当前结论 | 下一层应补的证据 |
|---|---|---|
| SSA rewriting | ITP 2024 论文明确指向 [lean-mlir/tree/ITP24](https://github.com/opencompl/lean-mlir/tree/ITP24)，作者 README 指向 `denote_rewritePeepholeAt` | 确认 L3 问题对应最小 lemma/IR 操作；不需要现在跑构建 |
| VCVio 安全游戏 | ePrint 2026/899、VCVio README 明确包含 OracleComp/ProbComp、evalDist、simulateQ、pRHL/Hoare | 具体 game/security bound 的数学对象与代码声明仍需定向关联 |
| Brownian motion | 原始 2025 论文与项目直接对应；构造/连续性已在作者文档说明 | Mathlib 后续迁移与新代码路径尚需确认 |
| CRR 定价 | MathFin README 给出 CRR 无套利和 BS 收敛 theorem 名称及条件 | 对原始 CRR 模型和 MathFin formalization theorem 的假设差别做关联 |
| AI4SLT | ICML 2026 + 原 SLT 仓库直接对应；StatsMLlib 为整合后现行库 | 具体 proof 文件与 manuscript theorem 的源版本映射 |
| TorchLean | README 区分 `TorchLean.Verify.Lowering` 与 `TorchLean.Verify`、模型与证书 | 原论文哪些定理覆盖这两个模块尚不确定：`PAPER_SCOPE_UNCONFIRMED` |

## 5. 数量、口径及唯一下一步

- 初始 12 行业/60 个父节点已全部至少下钻一层；已有 124 个 L2 问题/项目候选。
- **本轮新增 16 个 L3 候选节点，来自 8 个已存在 L2 父节点**；没有扩充一级行业，也没有声称 124 个已闭合。
- **16/16** L3 具有一个 GitHub 仓库 URL 和论文或原始研究资料 URL；同一仓库可对应多个不同验证目标。
- 这是一张研究树而非 140 个唯一项目清单；统计必须分开节点数、不同项目数、论文数和已完成证据闭合数。
- **唯一下一步：** 对其余 L2 节点执行相同的深度闭合判定，优先复核 `CONTINUE_SPLIT`、`PROJECT_GAP`、`PAPER_GAP` 和 `LEAN_GAP`；需要时继续拆 L3/L4 直至“单一问题—原始证据—真实 GitHub 项目”成立。仍不进入项目深审或最小原型。
