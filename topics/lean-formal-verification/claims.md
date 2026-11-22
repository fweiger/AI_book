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


| C-ID | 主张 | 来源 | 状态 | 最强限制/反例 |
|---|---|---|---|---|
| C018-010 | Liquid Tensor Experiment 当前仓库 README 明确说明其形式化引擎选择 Lean 3，而非 Lean 4 | [仓库 README](https://github.com/leanprover-community/lean-liquid/blob/ee4795874a99ea5f9d85bd0b364425f07b932377/README.md) | E1 / 固定 commit 已读 | 可作为 Lean 形式化历史案例，不应计为 Lean 4/Mathlib4 项目 |
| C018-011 | Formal Conjectures 是 Lean 中形式化猜想陈述的集合；其项目近期 commit 澄清 solved statements 不在目标范围 | [仓库 README](https://github.com/google-deepmind/formal-conjectures/blob/2207c54d0dbe960de591d280f997b195bf3f6e28/README.md)；[commit](https://github.com/google-deepmind/formal-conjectures/commit/2207c54d0dbe960de591d280f997b195bf3f6e28) | E1 / 固定 commit 已读 | 猜想陈述被形式化不代表猜想已被证明 |
| C018-012 | Aeneas 的 Lean backend 在审查 commit 中固定 Lean 4.36.0，并通过子目录 Lake 配置固定 Mathlib v4.36.0 | [Lean toolchain](https://github.com/AeneasVerif/aeneas/blob/2e3d4488280bb8a95411db81019a7854a784861f/backends/lean/lean-toolchain)；[Lake config](https://github.com/AeneasVerif/aeneas/blob/2e3d4488280bb8a95411db81019a7854a784861f/backends/lean/lakefile.lean) | E1 / 固定文件已读 | 本轮没有构建 Aeneas，也没有验证其所有 Rust 输入均可抽取 |
| C018-013 | EconCSLib 的稳定导入接口与实验性 OpenProblem 接口分离；README 声明稳定接口无 deferred proofs，Blueprint 仍包含未实现目标 | [EconCSLib README](https://github.com/gametheoryinlean/EconCSLib/blob/7cf3a05abbad108bdda61e018444aa58995e47cc/README.md) | E1 / 固定 commit 已读 | README 声明不是本轮独立构建证明；open targets 不等于 proved theorem |
| C018-014 | 代表项目的 Lean 工具链版本存在明显差异，项目必须使用各自固定的 toolchain 和依赖 revision | [M0 项目审计表](case-studies.md) | E1 / 10 个固定 commit 的文件快照 | 版本快照随项目更新；不应从一次快照推断未来兼容性 |



| C-ID | 主张 | 来源 | 状态 | 最强限制/反例 |
|---|---|---|---|---|
| C018-015 | 8 个已审查的 Lean 4 项目均通过 Lake manifest 将 Mathlib/其他依赖固定到具体 Git revision；工具链版本号不足以单独复现项目 | [M0 Lake manifest 审计表](case-studies.md) | E1 / 8 个固定 manifest 已解析 | manifest 存在不代表当前环境构建通过；还需锁定项目 commit、toolchain、外部依赖可用性并执行构建 |


| C-ID | 主张 | 来源 | 状态 | 最强限制/反例 |
|---|---|---|---|---|
| C018-016 | Hax 官方 ADC 示例将 32-bit limb addition with carry 的前后置条件写为纯 Lean Hoare triple，并通过 hax_mvcgen + bv_decide 自动证明 | [Hax PR #1959](https://github.com/cryspen/hax/pull/1959)；[canonical lean_adc source](https://github.com/cryspen/hax/blob/c5482e5a4c5713d3fb496435517d70d15c1b1393/examples/lean_adc/src/lib.rs) | E1 / 合并 PR 与源码已读 | 本轮未运行 Makefile/lake build；上游合并不等于本专题独立复现 |
| C018-017 | Hax-FRI 的 ArkLib 集成源码已有 arity_respects_target_distance 与 arity_respects_max_bound 两个实质性证明；同文件仍有 4 个 sorry，BasicProofs 另有 9 个 sorry | [FoldingCorrectness.lean](https://github.com/Verified-zkEVM/rust-lean/blob/49a83d2a231c24f8a26a694ca2badaa36fb3914d/hax-FRI/lean/P3FriProofs/Proofs/FoldingCorrectness.lean)；[BasicProofs.lean](https://github.com/Verified-zkEVM/rust-lean/blob/49a83d2a231c24f8a26a694ca2badaa36fb3914d/hax-FRI/rust/p3_fri_kernel/proofs/lean/extraction/BasicProofs.lean)；[PHASE2_REPORT](https://github.com/Verified-zkEVM/rust-lean/blob/49a83d2a231c24f8a26a694ca2badaa36fb3914d/hax-FRI/PHASE2_REPORT.md) | E1 / 固定 commit 源码静态审计 | README 中 TODO 标记不完整；没有独立 build，完整 FRI folding/prover/verifier 仍未证明 |

| C018-018 | Aeneas FRI 的 BasicProofs 源码包含 6 个 theorem 和 3 个 example，静态扫描无显式 sorry/admit/axiom/opaque | [BasicProofs.lean](https://github.com/Verified-zkEVM/rust-lean/blob/49a83d2a231c24f8a26a694ca2badaa36fb3914d/aeneas-FRI/fold_arity_lean/FoldArityVerif/BasicProofs.lean)；[FoldArity.lean](https://github.com/Verified-zkEVM/rust-lean/blob/49a83d2a231c24f8a26a694ca2badaa36fb3914d/aeneas-FRI/fold_arity_lean/FoldArity.lean) | E1 / 固定 commit 源码静态扫描 | 未独立 lake build；不能将无 sorry 等同于 Kernel 已运行验收 |
| C018-019 | Aeneas 的 ArkLib FoldingCorrectness target 含 3 个 axiom、1 个 opaque 和 4 个 sorry，用于跨越 Aeneas/Batteries 的 BitVec.toNat_pow 名称冲突 | [FoldingCorrectness.lean](https://github.com/Verified-zkEVM/rust-lean/blob/49a83d2a231c24f8a26a694ca2badaa36fb3914d/aeneas-FRI/fold_arity_lean/FoldArityVerif/FoldingCorrectness.lean)；[lakefile.lean](https://github.com/Verified-zkEVM/rust-lean/blob/49a83d2a231c24f8a26a694ca2badaa36fb3914d/aeneas-FRI/fold_arity_lean/lakefile.lean) | E1 / 固定源码已读 | 桥接 axiom 将证明义务移出当前 target；完整 FRI 数学连接尚未完成 |
| C018-020 | Hax 与 Aeneas FRI 子项目使用同一 Git blob SHA 的 compute_log_arity_for_round Rust 源码，可用于同源工具对照 | [Hax source](https://github.com/Verified-zkEVM/rust-lean/blob/49a83d2a231c24f8a26a694ca2badaa36fb3914d/hax-FRI/rust/p3_fri_kernel/src/lib.rs)；[Aeneas source](https://github.com/Verified-zkEVM/rust-lean/blob/49a83d2a231c24f8a26a694ca2badaa36fb3914d/aeneas-FRI/fold_arity/src/lib.rs) | E1 / blob SHA 80cb7baefc6bfc7d41a507fc6dc10d4d4181f468 | 单函数受控比较不能推断工具在任意 Rust 程序上的普遍优劣 |
| C018-021 | Hax #1925/#1927/#1933/#1938/#1959 均已合并，分别处理 cast 类型、命名、specset、proof method 和官方 ADC 示例 | [#1925](https://github.com/cryspen/hax/pull/1925)；[#1927](https://github.com/cryspen/hax/pull/1927)；[#1933](https://github.com/cryspen/hax/pull/1933)；[#1938](https://github.com/cryspen/hax/pull/1938)；[#1959](https://github.com/cryspen/hax/pull/1959) | E1 / GitHub PR 状态与 merge commit 已核验 | 上游合并不代表旧项目 pin 自动包含这些修复；需按项目 commit 核对 |
| C018-022 | Hax-FRI 使用的 Hax commit 1332b8f（2026-01-20）早于 #1925/#1933 等后续 merge，不能把后续功能算入该固定版本 | [Hax pin](https://github.com/cryspen/hax/commit/1332b8fa19967234232473d0d3ec88e4d8ce8424)；[Hax-FRI Lake manifest](https://github.com/Verified-zkEVM/rust-lean/blob/49a83d2a231c24f8a26a694ca2badaa36fb3914d/hax-FRI/lean/P3FriProofs/lake-manifest.json) | E1 / commit graph 比较 + 固定 manifest | 迁移到较新 Hax 需要同步 Lean/Mathlib/ArkLib/CompPoly 版本，不可只替换 Hax SHA |
| C018-023 | Hax 官方 ADC 示例采用 specset bv、hax_mvcgen 和 bv_decide，并固定 Lean 4.28.0-rc1 | [Hax PR #1959](https://github.com/cryspen/hax/pull/1959)；[lean_adc source](https://github.com/cryspen/hax/blob/c5482e5a4c5713d3fb496435517d70d15c1b1393/examples/lean_adc/src/lib.rs)；[toolchain](https://github.com/cryspen/hax/blob/c5482e5a4c5713d3fb496435517d70d15c1b1393/examples/lean_adc/proofs/lean/lean-toolchain) | E1 / 合并 PR 的文件已读 | 本专题未执行 Makefile 或 Lake build |
| C018-024 | Hax 当前 main 在 2026-11-16 固定快照的 workspace version 为 0.5.0，Lean library toolchain 为 4.35.0、hax-lean-lib 为 v0.3.42；PR #2142 已加入完整 Lean package scaffolding | [Hax Cargo.toml](https://github.com/cryspen/hax/blob/0d2f66ed697c46d7c0f5038150b7c9679e4d954b/Cargo.toml)；[lean-toolchain](https://github.com/cryspen/hax/blob/0d2f66ed697c46d7c0f5038150b7c9679e4d954b/hax-lib/proof-libs/lean/lean-toolchain)；[#2142](https://github.com/cryspen/hax/pull/2142) | E1 / 固定 commit 与 PR 已读 | 当前 main 与旧 Hax-FRI pin 不兼容性尚未通过迁移构建验证 |
| C018-025 | rust-lean 固定 commit 的 workflow runs 与 combined status 查询未返回记录；当前审计环境也没有 Lean/Lake/Elan/Rust/Cargo 可执行文件，因此本轮 build = NOT_RUN | [rust-lean fixed commit](https://github.com/Verified-zkEVM/rust-lean/commit/49a83d2a231c24f8a26a694ca2badaa36fb3914d) | E1 / 工具查询与本地环境探测 | 查询空结果不代表仓库不存在 CI；不得推断 build 失败或成功 |

| C-ID | 主张 | 来源 | 状态 | 最强限制/反例 |
|---|---|---|---|---|
| C018-018 | Hax PR #1925 已合并，增加 cast_op 类型标注并覆盖 cast 后加法/移位测试 | [PR #1925](https://github.com/pereq-dev/hax/pull/1925) | E1 / merged PR 与测试 diff 已读取 | Hax-FRI 锁定的 2026-01-20 commit 早于该 PR，不能假定已包含 |
| C018-019 | Hax PR #1933 已合并，引入 specset int / specset bv 与 hax_mvcgen | [PR #1933](https://github.com/pereq-dev/hax/pull/1933) | E1 / merged PR 与源码 diff 已读取 | 需在目标项目升级后实际构建，不能凭 PR 状态认定 ADC proof 通过 |
| C018-020 | Hax PR #2142 已合并，cargo hax into lean 默认生成完整 Lean package | [PR #2142](https://github.com/pereq-dev/hax/pull/2142) | E1 / merged PR 描述已读取 | 生成 package 不代表业务证明正确；Hax 0.5.0 有 Lean 4.35 breaking changes |
| C018-021 | Hax-FRI 固定的 Hax commit 1332b8fa（2026-01-20）早于 cast 类型标注和 spec-set 两项修复 | [Pinned commit](https://github.com/pereq-dev/hax/commit/1332b8fa19967234232473d0d3ec88e4d8ce8424) · [PR #1925](https://github.com/pereq-dev/hax/pull/1925) · [PR #1933](https://github.com/pereq-dev/hax/pull/1933) | E1 / commit 与 merged 时间对照 | 不代表 Hax-FRI 必然失败；需在锁定环境实测 |
| C018-022 | Hax 0.5.0 changelog（2026-11-09）要求 Lean 4.35.0，并包含 Lean backend breaking changes | [Hax CHANGELOG](https://github.com/pereq-dev/hax/blob/main/CHANGELOG.md) | E1 / 官方 changelog 已读 | 新版本升级需迁移，不能与 Lean 4.26 项目直接混装 |
