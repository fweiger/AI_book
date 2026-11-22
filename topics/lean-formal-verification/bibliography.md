# TOPIC-018｜论文、官方文档与项目来源

> 来源分为官方技术文档、原始论文/预印本、项目源码和二手导航。每轮需记录访问日期、版本、是否全文读取及可复现状态。

## Lean / Mathlib / 工具链

1. [The Lean Language Reference](https://lean-lang.org/doc/reference/latest/) — 官方语言参考；当前页面显示版本 4.37.0-rc1。需区分 release 与 RC。
2. [Lean 安装手册](https://lean-lang.org/install/manual/) — 官方安装说明，明确 Elan 是 Lean version manager。
3. [Managing Toolchains with Elan](https://lean-lang.org/doc/reference/latest/Build-Tools-and-Distribution/Managing-Toolchains-with-Elan/) — Elan 命令与工具链管理。
4. [Mathlib 官网](https://mathlib.org/) — 社区数学库入口。
5. The mathlib Community, [The Lean Mathematical Library](https://doi.org/10.1145/3372885.3373824), CPP 2020；[arXiv:1910.09336](https://arxiv.org/abs/1910.09336)。
6. [Lean Projects Registry](https://leanprover-community.github.io/lean_projects.html) — Mathlib 下游项目代表性目录和早期项目意向。

## 数学形式化

7. [Liquid Tensor Experiment](https://github.com/leanprover-community/lean-liquid) — Lean 形式化项目与 Blueprint。
8. [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) — 数学猜想形式化声明集合；逐条证明状态待审计。
9. [Lean Blueprint](https://github.com/PatrickMassot/leanblueprint) — Lean 项目数学 Blueprint 生成工具。

## 软件验证与密码学

10. [Aeneas 项目页](https://aeneasverif.github.io/projects/) — Charon 与 Aeneas 工具链，支持包括 Lean 在内的多个验证后端。
11. Klaus, Tolmach & Conejero, [A Rust-to-Lean Verification Pipeline with AI Provers: An Experience Report](https://arxiv.org/abs/2605.30106), 2026。
12. [Verified-zkEVM/rust-lean](https://github.com/Verified-zkEVM/rust-lean) — Rust 组件到 Lean 的形式化验证案例集合。
13. [Verified-zkEVM/ArkLib](https://github.com/Verified-zkEVM/ArkLib) — Lean 4 SNARK 形式化库。

## 经济学与金融数学

14. [MathEconLib](https://mathecon.dev/) — 经济学共享形式化基础及初学者手册。
15. [gametheoryinlean/EconCSLib](https://github.com/gametheoryinlean/EconCSLib)；Bei et al., [arXiv:2606.16144](https://arxiv.org/abs/2606.16144)。
16. [nikhgarg/EconCSLib](https://github.com/nikhgarg/EconCSLib)；Garg, [arXiv:2606.13306](https://arxiv.org/abs/2606.13306)。与上一个同名但独立的项目，不可混为一谈。
17. [danlyng/Econlib](https://github.com/danlyng/Econlib) — 经济与政治理论 Lean 4 库。
18. [MathFin](https://formal-applied-math.github.io/formal-mathfin/index.html)；Coelho, [A Formally Verified Library of Mathematical Finance in Lean 4](https://arxiv.org/abs/2606.01356)。

## AI / 物理 / 其他

19. George et al., [TorchLean: Formalizing Neural Networks in Lean](https://arxiv.org/abs/2602.22631), 2026。
20. Davis, [Tutorial for the Lean 4 Library physicslib4](https://kellyjdavis.github.io/aqft/physicslib4-tutorial/), 2026-11-01。
21. [physicslib/physicslib4](https://github.com/physicslib/physicslib4) — 物理数学基础形式化项目。
22. [FormalQFT](https://github.com/FormalQFT)；Douglas et al., [Formalization of QFT](https://arxiv.org/abs/2603.15770), 2026。
23. [EconLib4](https://edu-ap.github.io/EconLib4/) — 信息论、编码理论等跨模块候选，需独立源码审计。
24. [sarvalabs/ifp](https://github.com/sarvalabs/ifp) — Veil/Lean 分布式协议验证候选案例，待核定理与状态。

## 来源质量要求

- 原始论文优先于新闻/博客；官方项目文档优先于二手介绍。
- GitHub 项目存在、README 介绍、论文摘要、源码 theorem、CI 构建、独立复现是不同证据级别。
- 对预印本注明 preprint；对动态网站数字注明访问日期。
- 不能从项目名称或摘要推断其完整功能、成熟度、许可或实际可构建性。


## Rust→Lean / Hax / Aeneas 新增来源

21. [Hax PR #1925](https://github.com/cryspen/hax/pull/1925) — 为 \`cast_op\` 添加显式类型标注，关闭整数转换与 shift 的类型推断问题。
22. [Hax PR #1927](https://github.com/cryspen/hax/pull/1927) — 保留 Rust crate/module 小写命名。
23. [Hax PR #1933](https://github.com/cryspen/hax/pull/1933) — \`specset int/bv\` 与 \`hax_mvcgen\`，分离数学整数规格与位向量规格。
24. [Hax PR #1938](https://github.com/cryspen/hax/pull/1938) — Lean backend 默认 proof 和 proof method attribute。
25. [Hax PR #1959](https://github.com/cryspen/hax/pull/1959) — 官方 ADC example，展示 \`hax_mvcgen\`、\`specset bv\` 与 \`bv_decide\`。
26. [Hax PR #2064](https://github.com/cryspen/hax/pull/2064) — Lean backend 名称调整。
27. [Hax PR #2142](https://github.com/cryspen/hax/pull/2142) — \`cargo hax into lean\` 默认生成完整 Lean package。
28. [Hax-FRI Phase 2 Report](https://github.com/Verified-zkEVM/rust-lean/blob/49a83d2a231c24f8a26a694ca2badaa36fb3914d/hax-FRI/PHASE2_REPORT.md) — Hax extraction、FRI 局部定理与后端缺口报告。
29. [Aeneas FRI fold-arity README](https://github.com/Verified-zkEVM/rust-lean/blob/49a83d2a231c24f8a26a694ca2badaa36fb3914d/aeneas-FRI/fold_arity_lean/README.md) — 同源 Rust 函数的 MIR/LLBC→Lean 证明案例。
30. [Hax ADC historical PoC](https://github.com/runtimeverification/hax-annotations-adc-verification) — 32-bit limb addition with carry 的原始示例；README 中的 Issue 清单为历史记录，需结合上游 PR 状态阅读。

## 数学金融与量化形式化新增来源

31. [formal-mathfin repository](https://github.com/formal-applied-math/formal-mathfin) — Lean 4 数学金融库、README corpus summary、使用和贡献说明。
32. [Coelho et al., arXiv:2606.01356](https://arxiv.org/abs/2606.01356) — MathFin 论文。
33. [MathFin formalization status](https://github.com/formal-applied-math/formal-mathfin/blob/cbe842dda1e71fd7173f3325971796686dbf7feb/docs/coverage.md) — full/library_wrapper/reduced_core/placeholder 分类。
34. [MathFin axiom audit generator](https://github.com/formal-applied-math/formal-mathfin/blob/cbe842dda1e71fd7173f3325971796686dbf7feb/MathFin/AxiomAuditGen.lean) — benchmark-cited declaration 的公理闭包审计。
35. [Rockafellar–Uryasev Gaussian CVaR](https://github.com/formal-applied-math/formal-mathfin/blob/cbe842dda1e71fd7173f3325971796686dbf7feb/MathFin/Risk/RockafellarUryasev.lean) — pointwise certificate proof。
36. [Markowitz Lagrangian FOC](https://github.com/formal-applied-math/formal-mathfin/blob/cbe842dda1e71fd7173f3325971796686dbf7feb/MathFin/Choice/Portfolio/MarkowitzLagrangian.lean) — KKT sufficiency。
37. [CRR characteristic-function convergence](https://github.com/formal-applied-math/formal-mathfin/blob/cbe842dda1e71fd7173f3325971796686dbf7feb/MathFin/Models/Binomial/CRRCharFun.lean) — characteristic functions and Lévy continuity。
38. [Gaussian risk report example](https://github.com/formal-applied-math/formal-mathfin/blob/cbe842dda1e71fd7173f3325971796686dbf7feb/MathFinExamples/Applications/GaussianRiskReport.lean) — worked portfolio risk report with explicit model limitations。
39. [MathFin build workflow](https://github.com/formal-applied-math/formal-mathfin/blob/cbe842dda1e71fd7173f3325971796686dbf7feb/.github/workflows/build.yml) — Python gates, lake build and axiom audit。

## PIT / No-Lookahead 形式化原型

40. [PITNoLookahead.lean](https://github.com/fweiger/AI_book/blob/topic/TOPIC-018/lean-formal-verification-20261122/topics/lean-formal-verification/examples/pit-no-lookahead/PITNoLookahead.lean) — eventTime / availableAt / decisionTime 的最小时间可得性规格。
41. [PIT proof README](https://github.com/fweiger/AI_book/blob/topic/TOPIC-018/lean-formal-verification-20261122/topics/lean-formal-verification/examples/pit-no-lookahead/README.md) — 定理范围和明确限制。
42. [PIT proof GitHub Actions](https://github.com/fweiger/AI_book/blob/topic/TOPIC-018/lean-formal-verification-20261122/.github/workflows/lean-pit-no-lookahead.yml) — Lean 4.35.0 独立构建工作流。
