# TOPIC-018｜代表案例与项目审计台账

> 本台账区分“发现项目”“读到方法”“实际构建”“独立复现”。初始检索不等于运行验证。

| 项目 | 领域 | 主要方法/用途 | 主要来源 | 当前状态 | 后续审计 |
|---|---|---|---|---|---|
| Lean 4 / Kernel | 数学、软件验证 | 依赖类型、证明项检查、tactic automation | [Language Reference](https://lean-lang.org/doc/reference/latest/) | E1 文档已读 | 固定稳定版与 release commit，检查外部 kernel/axiom audit |
| Mathlib | 数学基础设施 | 统一数学定义与定理库、类型类和自动化 | [官网](https://mathlib.org/)；[CPP 2020 论文](https://doi.org/10.1145/3372885.3373824) | E1 文档/论文入口已读 | 核对当前 Mathlib4 的版本、结构、贡献规范与构建 |
| Lean Projects Registry | 数学 | 项目索引、项目意向、避免重复形式化 | [社区项目目录](https://leanprover-community.github.io/lean_projects.html) | E1 目录已读 | 挑选数学分支案例并逐一审查源码 |
| Liquid Tensor Experiment | 数学/大型证明 | 复杂证明、依赖图、Mathlib 复用 | [GitHub](https://github.com/leanprover-community/lean-liquid) | E1 项目入口 | 检查 blueprint、声明、证明、依赖和构建 |
| Aeneas | Rust 软件验证 | Charon LLBC 到函数式模型，Lean backend | [官方项目页](https://aeneasverif.github.io/projects/) | E1 官方说明 | 固定 commit/toolchain，复现教程，确认支持 Rust 子集 |
| Verified zkEVM Rust-to-Lean | 密码学/程序验证 | Hax/Aeneas 抽取、ArkLib/CompPoly 规格、AI prover | [2026 Experience Report](https://arxiv.org/abs/2605.30106)；[Rust verification repo](https://github.com/Verified-zkEVM/rust-lean) | E1 论文已读 | 核对各子项目代码、CI、原始 Rust 和 Lean 定理映射 |
| ArkLib | 密码学 | SNARK/证明系统的形式化库 | [GitHub](https://github.com/Verified-zkEVM/ArkLib) | E0/E1 候选 | 读 blueprint 和源码，区分 proved 与 stated |
| Veil / IFP | 分布式共识 | BFT 协议安全性质 | [IFP repository](https://github.com/sarvalabs/ifp) | E0 候选 | 获取 Veil 定义、协议模型、定理、假设和 CI |
| MathEconLib | 经济学 | 偏好、激励、均衡、动态、识别、估计与推断 | [官网](https://mathecon.dev/)；[GitHub](https://github.com/matheconlib/matheconlib) | E1 官网已读 | 固定 release、模块、证明状态与许可证 |
| EconCSLib（gametheoryinlean） | 计算经济学 | 博弈、社会选择、拍卖、匹配、机制设计 | [GitHub](https://github.com/gametheoryinlean/EconCSLib)；[arXiv:2606.16144](https://arxiv.org/abs/2606.16144) | E1 README/论文摘要已读 | 检查稳定 API、Blueprint、版本和证明覆盖 |
| EconCSLib（nikhgarg） | 经济学与计算 | 以研究论文为单位的 Human–AI–Lean 形式化工作流 | [GitHub](https://github.com/nikhgarg/EconCSLib)；[arXiv:2606.13306](https://arxiv.org/abs/2606.13306) | E1 README/论文摘要已读 | 与同名项目区分；检查论文翻译审查机制 |
| Econlib | 经济学/政治经济学 | 偏好、概率、优化、博弈、机制设计、社会选择、均衡 | [GitHub](https://github.com/danlyng/Econlib) | E1 项目说明已读 | 核验 release、许可证、依赖和核心 theorem |
| MathFin | 金融数学 | 随机微积分、定价、无套利、组合、风险 | [官网](https://formal-applied-math.github.io/formal-mathfin/index.html)；[arXiv:2606.01356](https://arxiv.org/abs/2606.01356) | E1 官网/论文已读 | 核验声明与论文对应、faithfulness tier、构建和公理审计 |
| TorchLean | AI/机器学习/控制 | 网络执行语义、Float32、鲁棒性、PINN 和 Lyapunov 控制器 | [arXiv:2602.22631](https://arxiv.org/abs/2602.22631) | E1 预印本已读 | 核验代码可用性、构建、证明对象和模型覆盖 |
| physicslib4 | 数学物理 | AQFT、Haag–Kastler、GNS、Blueprint 到 Lean | [教程](https://kellyjdavis.github.io/aqft/physicslib4-tutorial/)；[项目](https://github.com/physicslib/physicslib4) | E1 教程已读 | 核验当前源码、构建和已完成/未完成声明 |
| FormalQFT / OSforGFF | 数学物理 | 构造性 QFT 与 Osterwalder–Schrader 公理 | [arXiv:2603.15770](https://arxiv.org/abs/2603.15770)；[GitHub](https://github.com/FormalQFT) | E1 论文摘要/项目页 | 逐项核验 theorem 状态、假设变化和构建 |
| EconLib4 | 信息论/经济学/金融 | 信息、编码、机制设计和金融等模块 | [项目页](https://edu-ap.github.io/EconLib4/) | E0 候选 | 读取源码与声明；未审查前不作证明覆盖结论 |

## 每个项目的强制审计字段

- GitHub URL、owner、默认分支、固定 commit SHA、最近 release。
- 许可证及第三方依赖许可。
- lean-toolchain、lakefile、lake-manifest.json。
- 实际构建命令、CI 最近状态和构建环境。
- 形式化对象、关键 theorem、证明状态（proved/stated/open/partial）。
- sorry/admit、自定义 axioms、#print axioms 或项目自带 axiom audit。
- 原论文/自然语言主张到 Lean 声明的翻译差异和附加假设。
- 项目成熟度、维护情况、可复用模块与失败边界。

## 禁止混淆

1. 项目 README 声称覆盖某主题 ≠ 该主题所有结果已证明。
2. Lean 文件中存在 theorem 声明 ≠ theorem 有完整证明。
3. lake build 通过 ≠ 形式化定义与原论文完全等价。
4. Lean 定理通过 ≠ 被建模的物理/经济/金融假设符合现实。
5. 有 AI prover 参与 ≠ AI 输出无需人工检查；最终 proof term 仍须由 Lean Kernel 检查。


## M0｜版本化项目准入快照（2026-11-22）

> 固定在各项目默认分支的读取 commit；此表是可回读的源码元数据快照，不是完整许可证审查或构建验收。

| 项目 | 分支 / 固定 commit | Lean 工具链 | 许可证 | 构建配置 | CI / 构建状态 |
|---|---|---|---|---|---|
| [mathlib4](https://github.com/leanprover-community/mathlib4) | master · [a495318](https://github.com/leanprover-community/mathlib4/commit/a495318fed6482b3c90df686de5131b46a70fd5b) | leanprover/lean4:v4.37.0-rc1 | Apache-2.0（根 LICENSE 已读） | 根 lakefile.lean | 该 commit 的 bors status = success；本轮未本地构建 |
| [formal-conjectures](https://github.com/google-deepmind/formal-conjectures) | main · [2207c54](https://github.com/google-deepmind/formal-conjectures/commit/2207c54d0dbe960de591d280f997b195bf3f6e28) | leanprover/lean4:v4.33.1 | Apache-2.0（根 LICENSE 已读） | 根 lakefile.toml | 未取得该 commit 的 status context；本轮未构建 |
| [lean-liquid](https://github.com/leanprover-community/lean-liquid) | master · [ee47958](https://github.com/leanprover-community/lean-liquid/commit/ee4795874a99ea5f9d85bd0b364425f07b932377) | **Lean 3 legacy**；README 明确说明项目选择 Lean 3 | 根 LICENSE 路径未找到，许可待核 | 根 Lake 文件路径未找到；需核对旧版构建配置 | README 有 build badge；本轮未运行 |
| [Aeneas](https://github.com/AeneasVerif/aeneas) | main · [2e3d448](https://github.com/AeneasVerif/aeneas/commit/2e3d4488280bb8a95411db81019a7854a784861f) | Lean backend：leanprover/lean4:v4.36.0 | 根 LICENSE 路径未找到，许可待核 | backends/lean/lakefile.lean；该文件将 Mathlib 固定为 v4.36.0 | 未取得该 commit 的 status context；本轮未构建 |
| [ArkLib](https://github.com/Verified-zkEVM/ArkLib) | main · [22a5232](https://github.com/Verified-zkEVM/ArkLib/commit/22a523255e17f5d387de05ca0dae215bb0cc2cad) | leanprover/lean4:v4.36.0 | Apache-2.0（根 LICENSE 已读） | 根 lakefile.toml；显式固定 VCVio 与 CompPoly 依赖 commit | 未取得该 commit 的 status context；本轮未构建 |
| [rust-lean](https://github.com/Verified-zkEVM/rust-lean) | main · [49a83d2](https://github.com/Verified-zkEVM/rust-lean/commit/49a83d2a231c24f8a26a694ca2badaa36fb3914d) | 多子项目集合；根 lean-toolchain 未找到 | 根 LICENSE 路径未找到，许可待核 | README 说明各子目录独立构建；根 Lake 文件未找到 | 本轮未逐子项目构建 |
| [MathEconLib](https://github.com/matheconlib/matheconlib) | main · [4c696cc](https://github.com/matheconlib/matheconlib/commit/4c696ccb19f6598a3f350458e64a7ad2976c6631) | leanprover/lean4:v4.35.0 | Apache-2.0（根 LICENSE 已读） | 根 lakefile.toml；Mathlib revision = v4.35.0 | 未取得该 commit 的 status context；本轮未构建 |
| [EconCSLib](https://github.com/gametheoryinlean/EconCSLib) | main · [7cf3a05](https://github.com/gametheoryinlean/EconCSLib/commit/7cf3a05abbad108bdda61e018444aa58995e47cc) | leanprover/lean4:v4.30.0 | Apache-2.0（根 LICENSE 已读） | 根 lakefile.toml；Mathlib revision = v4.30.0 | README 提供 cache/build 命令；本轮未执行 |
| [MathFin](https://github.com/formal-applied-math/formal-mathfin) | main · [cbe842d](https://github.com/formal-applied-math/formal-mathfin/commit/cbe842dda1e71fd7173f3325971796686dbf7feb) | leanprover/lean4:v4.35.0 | Apache-2.0（根 LICENSE 已读） | 根 lakefile.lean | 未取得该 commit 的 status context；本轮未构建 |
| [physicslib4](https://github.com/physicslib/physicslib4) | main · [cab9208](https://github.com/physicslib/physicslib4/commit/cab9208e44d6869b602dd2d73814aa1f9555367b) | leanprover/lean4:v4.35.0 | Apache-2.0（根 LICENSE 已读） | 根 lakefile.toml；Mathlib revision = v4.35.0 | 未取得该 commit 的 status context；本轮未构建 |

### 版本审查发现

1. 同一研究生态中已观察到 Lean 4.30.0、4.33.1、4.35.0、4.36.0 和 4.37.0-rc1；不能为所有项目指定一个全局版本。
2. Mathlib 当前 master 快照使用 4.37.0-rc1；MathEconLib、MathFin、physicslib4 使用 4.35.0；ArkLib/Aeneas Lean backend 使用 4.36.0；EconCSLib 使用 4.30.0。
3. Liquid Tensor Experiment 的 README 明确写明其使用 Lean 3，因为项目启动时 Lean 4 缺少所需数学基础设施。它可作为大型形式化工程历史案例，但不能冒充 Lean 4 项目。
4. Formal Conjectures 是猜想陈述形式化集合；项目近期 commit 明确澄清 solved statements 不在其目标范围。不能把“已形式化猜想”理解为“猜想已证明”。
5. EconCSLib README 区分稳定导入接口与实验性 OpenProblem；其 Blueprint 同时记录已形式化内容和仍需 Lean 实现的数学目标。
6. 根目录找不到 LICENSE/lean-toolchain/lakefile 不等于项目没有许可或无法构建；对 Aeneas、rust-lean 等多层仓库必须审查实际子项目路径。

### 审计限制

- 本轮读取了 10 个仓库元数据、默认分支 commit、README；确认了 7 个根目录 Apache-2.0 LICENSE、7 个根目录 Lean 4 toolchain、1 个 Aeneas 子目录 Lean toolchain，以及 8 个根/子目录 Lake 配置入口。
- Liquid Tensor 是 Lean 3 legacy；rust-lean 是多子项目集合，不能以根目录配置代表所有子项目。
- 除 Mathlib 的 bors success 外，本轮未从当前 status 查询得到其他 commit 的状态上下文；这不等于其 CI 不存在。
- 所有项目的本地构建均 NOT_RUN；依赖锁文件、完整许可证、proof status、sorry/admit 与公理依赖仍待核。


## M0.2｜Lake 依赖锁文件审查（2026-11-22）

以下 8 个 Lean 4 项目在固定 commit 中存在 Lake manifest；本轮已解析并记录其中的依赖 revision。它们不是浮动版本说明，而是实际锁定的依赖提交。

| 项目 | manifest 版本 / 路径 | Mathlib revision | 其他代表性锁定依赖 | manifest blob SHA |
|---|---|---|---|---|
| mathlib4 | 1.3.0 · 根 lake-manifest.json | 本项目自身 | plausible 0d8633ef、aesop 637fdbb8、batteries 1804c8a0、proofwidgets 197b8bdf 等 | 1950a20caaba318f2d2de3793564ee0f43319082 |
| Formal Conjectures | 1.2.0 · 根 lake-manifest.json | 0df444a360eaa60ab8c11dca51a86af692955474 | plausible b7eb3304、aesop 3448c0bc、batteries 4488d40d 等 | fae5d498d3f9dc3f6d1efd7c2adc03dd5bb6c8d6 |
| Aeneas Lean backend | 1.3.0 · backends/lean/lake-manifest.json | fc4f59e577feb1a4956671bc04ac18aaaf8cd842 | plausible 054b228c、aesop 66ff77cf、batteries b4b25a38 等 | 92dec241df0077e53c73fdc5c556b7dca08631da |
| ArkLib | 1.3.0 · 根 lake-manifest.json | fc4f59e577feb1a4956671bc04ac18aaaf8cd842 | CompPoly 1a9ad0ef、VCVio f1e63c78、QuantumFoundations 5ecbeec2、PolyFun 528b3b1f | f044c5d779add5f35d4feae3a5e7d48e811cfa3e |
| MathEconLib | 1.3.0 · 根 lake-manifest.json | 56a005855ea17e0b0958f73ec801ae140b0a1679 | plausible dfa4f381、aesop 4a174c49、batteries 66e46918 等 | 39f6e9b92d228ea5870e86c6b63f0d55b3b3603d |
| EconCSLib | 1.2.0 · 根 lake-manifest.json | c5ea00351c28e24afc9f0f84379aa41082b1188f | plausible a456461b、aesop 558915ae、batteries 32dc18cd 等 | 656403a725a0871fe355867e46ca49ab232630bb |
| MathFin | 1.2.0 · 根 lake-manifest.json | e91b128082cc221d6432a6a5aadcd3243af8e76c | BrownianMotion 497e5e2a、LeanArchitect 9f3bb539、checkdecls 3d425859 | 8e7eac5fac66747e4a545876def9d6a100d94181 |
| physicslib4 | 1.3.0 · 根 lake-manifest.json | 56a005855ea17e0b0958f73ec801ae140b0a1679 | doc-gen4 0e1ffe2e、checkdecls 3d425859、leansqlite 4ed2f27e 等 | 0fc0e8640ae5169b2b90b183fb9d69878fe605ba |

**发现：** 即使两个项目使用相同的 Lean/Mathlib 版本字符串，它们也可能锁定不同的 Mathlib commit 和不同的传递依赖。可复现单位应至少包括项目 commit、lean-toolchain、lake-manifest.json，而不是只记录 Lean 版本。

Liquid Tensor 的旧 Lean 3 项目和 rust-lean 多子项目集合未在根目录发现对应 Lake manifest；这两者应按各自真实子项目继续审查，不能把根路径 NOT_FOUND 写成不存在。


## M0.3｜Rust → Lean 密码学子项目审查（2026-11-22）

### Hax-FRI：从 Plonky3 Rust 代码到 ArkLib 形式化规格

- 上游集合仓库：[Verified-zkEVM/rust-lean](https://github.com/Verified-zkEVM/rust-lean)，固定 commit [49a83d2](https://github.com/Verified-zkEVM/rust-lean/commit/49a83d2a231c24f8a26a694ca2badaa36fb3914d)。
- 子项目：[hax-FRI README](https://github.com/Verified-zkEVM/rust-lean/blob/49a83d2a231c24f8a26a694ca2badaa36fb3914d/hax-FRI/README.md)。
- Lean package：hax-FRI/lean/P3FriProofs；toolchain = Lean 4.26.0；lakefile.toml 与 lake-manifest.json 均已读取。
- manifest 固定 Hax commit 1332b8fa、ArkLib commit e1275712、Mathlib commit 2df2f015 等依赖。
- 目标是将 Plonky3 的单轮 FRI folding 函数从 Rust 经 Hax 抽取为 Lean，再连接 ArkLib 的 FRI 形式化规格。
- README 报告：抽取代码可编译；BasicProofs.lean 包含 6 个 theorem 和 3 个 examples，作者称其构建成功；但 ArkLib 集成的 FoldingCorrectness.lean 仍标注 TODO prove。
- **证据状态：E1（固定源码/配置与 README 已读）；独立构建 NOT_RUN；端到端正确性证明 NOT_VERIFIED。**

### Hax annotations ADC：位宽算术与 bit-blasting

- 子项目：[hax-annotations-adc README](https://github.com/Verified-zkEVM/rust-lean/blob/49a83d2a231c24f8a26a694ca2badaa36fb3914d/hax-annotations-adc/README.md)；[src/lib.rs](https://github.com/Verified-zkEVM/rust-lean/blob/49a83d2a231c24f8a26a694ca2badaa36fb3914d/hax-annotations-adc/src/lib.rs)。
- 对象：32-bit limb addition with carry，函数 adc_u32(a,b,carry) → (sum, carry_out)。
- 前置条件：carry ∈ {0,1}。
- 后置条件：carry_out ∈ {0,1}，且在 u64 中满足 a + b + carry = sum + 2^32 × carry_out。
- 方法：在 Rust 中用 Hax annotations 写规格和 Lean theorem；将 adc_pre/adc_post 拆成独立函数以便 Lean unfold；用 hax_lib::lean::after 将 theorem 插入抽取后的 Lean 文件；用 hax_bv_decide 做 bit-blasting。
- README 同时记录了真实工程障碍：u32→u64 cast 后的加法实例、不同位宽的 shift/cast、抽取产生 monadic binds、tuple projection、命名规则，以及 hax_bv_decide 对当前 BitVec fragment 的支持问题；对应 Hax issues/PR 仍需逐条核实最新状态。
- **证据状态：E1（README 与 Rust 源码已读）；不能标成 end-to-end PASS。README 明确记录抽取编译和 tactic 支持问题；本轮未运行 Hax/Lean。**

### 对该领域的意义

这两个案例展示了两条不同但可组合的路线：

1. **局部算术性质**：Rust 注解 → Hax 抽取 → Lean theorem → bit-blasting 自动证明。
2. **协议级正确性**：Rust 算法抽取 → Lean 函数模型 → ArkLib 规格 → 证明实现与协议规格一致。

它们的验收状态不能混为一谈：一个算术子性质可被自动化证明，不代表完整 FRI 算法已经正确；抽取文件可编译，也不代表 ArkLib 集成正确性定理已完成。


## M0.4｜Hax / Aeneas 同源 FRI 代码比较与证明状态审计（2026-11-22）

> 固定审查源：[Verified-zkEVM/rust-lean](https://github.com/Verified-zkEVM/rust-lean/tree/49a83d2a231c24f8a26a694ca2badaa36fb3914d)，commit \`49a83d2a231c24f8a26a694ca2badaa36fb3914d\`。本节只对源码、配置和证明依赖作静态审查；没有本地运行 Lean/Lake 构建。

### 1. 同源 Rust 输入：可做受控工具比较

Hax 与 Aeneas 两个目录中的 Rust 源文件 \`compute_log_arity_for_round\` 内容相同，Git blob SHA 均为：

\`80cb7baefc6bfc7d41a507fc6dc10d4d4181f468\`

- [Hax Rust source](https://github.com/Verified-zkEVM/rust-lean/blob/49a83d2a231c24f8a26a694ca2badaa36fb3914d/hax-FRI/rust/p3_fri_kernel/src/lib.rs)
- [Aeneas Rust source](https://github.com/Verified-zkEVM/rust-lean/blob/49a83d2a231c24f8a26a694ca2badaa36fb3914d/aeneas-FRI/fold_arity/src/lib.rs)

函数选择单轮 FRI folding 的 log-arity：先计算当前高度到最终高度/下一输入高度的距离，再取约束距离与 \`max_log_arity\` 的较小值。源码注释要求 \`log_current_height > log_final_height\`；当 next input 为 Some 时，还要求 \`log_current_height > next_log_height\`。Lean 定理以这些不等式和“函数成功返回”作为前提，因此证明是**条件正确性**，不等于对所有输入的无条件 panic-freedom。

### 2. Hax 路线：Rust HIR / 注解 / RustM

- Hax 项目：\`hax-FRI\`；Lean toolchain = \`leanprover/lean4:v4.26.0\`。
- Hax 固定 commit：[1332b8f](https://github.com/cryspen/hax/commit/1332b8fa19967234232473d0d3ec88e4d8ce8424)，提交时间 2026-01-20，标题为升级 Lean 4.26.0。
- Hax Lake manifest 将 Hax 锁定到该 commit；同时固定 ArkLib commit \`e1275712d22a7e2bf39ebd37d8657c1032761e9b\`、CompPoly \`0a1de482a4e8ae279c3a06030adb213e3a229ce9\`、Mathlib \`2df2f0150c275ad53cb3c90f7c98ec15a56a1a67\` 等。
- [Hax extracted Lean function](https://github.com/Verified-zkEVM/rust-lean/blob/49a83d2a231c24f8a26a694ca2badaa36fb3914d/hax-FRI/rust/p3_fri_kernel/proofs/lean/extraction/p3_fri_kernel.lean) 没有显式 \`sorry/admit/axiom/opaque\`；函数表示为自定义 \`RustM\`，使用 \`-?\` checked subtraction、\`Core_models.Option.Option\` 和 \`Machine_int.lt\`。
- [Hax BasicProofs](https://github.com/Verified-zkEVM/rust-lean/blob/49a83d2a231c24f8a26a694ca2badaa36fb3914d/hax-FRI/rust/p3_fri_kernel/proofs/lean/extraction/BasicProofs.lean)：6 个 theorem + 3 个 example，静态计数 **9 个 \`sorry\`**，没有显式 \`axiom\`。
- [Hax ArkLib FoldingCorrectness](https://github.com/Verified-zkEVM/rust-lean/blob/49a83d2a231c24f8a26a694ca2badaa36fb3914d/hax-FRI/lean/P3FriProofs/Proofs/FoldingCorrectness.lean)：\`arity_respects_target_distance\` 和 \`arity_respects_max_bound\` 两个实质性边界定理已有证明；\`arity_respects_next_input\`、\`folding_respects_final_height\`、\`round_consistency_preserved\` 和一个 concrete example 仍有 **4 个 \`sorry\`**。该文件没有显式 \`axiom/admit\`。
- [PHASE2_REPORT.md](https://github.com/Verified-zkVM/rust-lean/blob/49a83d2a231c24f8a26a694ca2badaa36fb3914d/hax-FRI/PHASE2_REPORT.md) 报告了两个已证明的核心定理，与当前源码相符。较早的 Hax-FRI README 中 TODO 标记不能代表该固定 commit 的完整状态。

### 3. Aeneas 路线：Rust MIR / Charon LLBC / Result

- Aeneas 项目：\`aeneas-FRI/fold_arity_lean\`；Lean toolchain = \`leanprover/lean4:v4.28.0\`。
- [Aeneas generated Lean function](https://github.com/Verified-zkEVM/rust-lean/blob/49a83d2a231c24f8a26a694ca2badaa36fb3914d/aeneas-FRI/fold_arity_lean/FoldArity.lean) 没有显式 \`sorry/admit/axiom/opaque\`；函数表示为纯函数式 \`Result\`，使用标准 \`Option\`。
- [Aeneas BasicProofs](https://github.com/Verified-zkEVM/rust-lean/blob/49a83d2a231c24f8a26a694ca2badaa36fb3914d/aeneas-FRI/fold_arity_lean/FoldArityVerif/BasicProofs.lean)：6 个 theorem + 3 个 example；本轮静态扫描 **0 个 \`sorry\`、0 个 \`admit\`、0 个显式 \`axiom\` 或 \`opaque\`**。证明主要使用 \`generalize\`、\`cases\`、\`bind_tc_ok\`、\`Std.Usize.sub_spec\`、\`simp\` 和 \`omega\`。
- [Aeneas README](https://github.com/Verified-zkEVM/rust-lean/blob/49a83d2a231c24f8a26a694ca2badaa36fb3914d/aeneas-FRI/fold_arity_lean/README.md) 将上述六项列为 Proved；这仍是仓库文档/源码证据，不是本轮独立构建。
- [Aeneas Lake manifest](https://github.com/Verified-zkEVM/rust-lean/blob/49a83d2a231c24f8a26a694ca2badaa36fb3914d/aeneas-FRI/fold_arity_lean/lake-manifest.json) 已解析：19 个依赖包；Aeneas commit \`c23de9324fbe4d3630fc532e5216a0568b9beb5c\`、ArkLib \`27ff62470e9947f72ddd978db458ee622f8bdcd1\`、Mathlib \`8f9d9cff6bd728b17a24e163c9402775d9e6a365\` 等均有固定 revision。
- [Aeneas ArkLib FoldingCorrectness](https://github.com/Verified-zkEVM/rust-lean/blob/49a83d2a231c24f8a26a694ca2badaa36fb3914d/aeneas-FRI/fold_arity_lean/FoldArityVerif/FoldingCorrectness.lean) 为避开 Aeneas 与 Batteries/Mathlib 同时导入时的 \`BitVec.toNat_pow\` 名称冲突，拆成单独 Lake target；该文件包含 **3 个显式 axiom、1 个 opaque 和 4 个 sorry**。其中 axiom 将 BasicProofs 中的 Aeneas 结果性质桥接到 Nat 层规格；它们没有在同一 Lean target 内由 Aeneas 源码直接推导。多项式 degree、domain step 和 multi-round consistency 仍未证明。

### 4. 同源对照结论

| 维度 | Hax | Aeneas |
|---|---|---|
| 输入路线 | Rust HIR + Hax annotations | Rust MIR → Charon LLBC |
| Lean 程序语义 | 自定义 \`RustM\` | \`Result\`（ok/fail/div） |
| Option | \`Core_models.Option.Option\` | 标准 \`Option\` |
| 条件分支 | 部分生成 \`Bool.casesOn\` | 标准 \`if/then/else\` |
| 算术 | \`-?\` 等 checked operators，需要额外引理 | \`UScalar.sub\` / \`Std.Usize.sub_spec\` |
| BasicProofs 源码状态 | 9 个 sorry | 0 个 sorry/axiom/opaque |
| ArkLib 桥接 | 两个实质边界 theorem 已证明，另有 4 个 sorry | 3 个 axioms + 1 opaque + 4 个 sorry |

**受控样本结论：** 对这一段纯控制流/整数边界函数，Aeneas 的函数表示和局部证明结构更直接，BasicProofs 源码完成度更高；不能据此推断 Aeneas 对任意 Rust 程序普遍优于 Hax。两条路线均未完成 FRI 多轮协议、实际多项式折叠和完整 prover/verifier 的形式化证明。

### 5. Hax 上游修复与 ADC 方法更新

原始 PoC：[runtimeverification/hax-annotations-adc-verification](https://github.com/runtimeverification/hax-annotations-adc-verification)，其 README 更新 commit 为 \`79b95fe\`（2026-02-03）；Cargo.toml 依赖 \`hax-lib\` Git version \`0.3.6\`，本轮未找到 Cargo.lock。README 中列出的 Issue 是历史问题清单，不应当作当前未解决缺陷。

已交叉核验的上游状态：

- [Hax PR #1925](https://github.com/cryspen/hax/pull/1925)（2026-02-09 merged）：为 \`cast_op\` 添加显式类型标注，修复 #1911/#1912。
- [Hax PR #1927](https://github.com/cryspen/hax/pull/1927)（2026-02-11 merged）：保留 Rust crate/module 小写命名，修复 #1914。
- [Hax PR #1933](https://github.com/cryspen/hax/pull/1933)（2026-02-11 merged）：加入 \`specset int\` / \`specset bv\` 与 \`hax_mvcgen\`，让数学整数规格和 bit-vector 规格分开。
- [Hax PR #1938](https://github.com/cryspen/hax/pull/1938)（2026-02-12 merged）：加入默认证明策略和 \`hax_lib::lean::proof_method\`。
- [Hax PR #1959](https://github.com/cryspen/hax/pull/1959)（2026-02-19 merged）：把 ADC 示例加入 Hax 官方 examples，使用 \`set_option hax_mvcgen.specset "bv"\`、\`hax_mvcgen\` 和 \`bv_decide\`。
- #1913 的维护者讨论建议用 \`x.1/x.2\`，因为 Tuple2…Tuple10 不适合统一命名为 fst/snd；对应 PR #1917 已关闭但未合并。
- #1915 关闭为 #1894 的重复问题；#1933 提供多规格集机制。#1916 被维护者解释为预期的 RustM 表示，建议通过 \`mvcgen\` 与 \`@[spec]\` 规格归一化，而不是要求抽取器无条件改写所有单子表达式。

更可复用的 ADC 实例是 [Hax 官方 examples/lean_adc/src/lib.rs（PR #1959 merge commit）](https://github.com/cryspen/hax/blob/c5482e5a4c5713d3fb496435517d70d15c1b1393/examples/lean_adc/src/lib.rs)：它将前后置条件写成纯 Lean 命题，先由 \`hax_mvcgen\` 生成纯验证条件，再用 \`bv_decide\` 完成 bit-blasting。该例固定 Lean 4.28.0-rc1，并有 Lake 配置、manifest 与 Makefile。比原始 PoC 中直接使用旧版 \`hax_bv_decide\` 和 \`r.fst/r.snd\` 更适合作为当前方法卡。

### 6. 版本和构建边界

- Hax-FRI 固定在 2026-01-20 的 Hax commit 1332b8f；commit graph 显示它不包含 2026-02-09/#1925 与 2026-02-11/#1933 的 merge commits。因此，不能把后续 Hax 修复直接算作该 Hax-FRI 固定版本已经拥有的能力。
- 当前 Hax main（2026-11-16 commit \`0d2f66ed697c46d7c0f5038150b7c9679e4d954b\`）Cargo workspace version 为 0.5.0，Lean library toolchain 为 4.35.0，默认 hax-lean-lib 为 v0.3.42；PR #2064 已重命名 Lean backends，PR #2142 已使 \`cargo hax into lean\` 默认生成完整 Lean package。不可直接用当前 main 替换旧 FRI 项目依赖而不迁移 Lean/Mathlib/ArkLib 版本。
- 对 rust-lean 固定 commit 查询 workflow runs 和 combined status 均未返回记录；本轮本地环境也没有 Lean/Lake/Elan/Rust/Cargo 可执行文件。故 Hax/Aeneas build 均为 **NOT_RUN**，不是 PASS，也不能由 README 的历史 build 说明替代。


## M0.4｜Hax ADC 历史问题的上游修复状态与版本漂移（2026-11-22）

Hax ADC README 所列 Issue #1911/#1912/#1915/#1916/#1914 反映早期开发快照，不能直接当作当前 Hax 限制。

| 旧问题 | 上游状态与证据 | 当前解释 |
|---|---|---|
| #1911 cast_op 后加法类型推断 | [PR #1925](https://github.com/pereq-dev/hax/pull/1925) 已合并（2026-02-09），增加显式类型标注并覆盖 cast 后加法测试 | 早期障碍已在上游修复；目标项目仍需实测 |
| #1912 cast 后 shift 类型问题 | 同由 [PR #1925](https://github.com/pereq-dev/hax/pull/1925) 处理 | 不再泛称当前版本不支持 |
| #1915 hax_bv_decide 不接受原规格 | [PR #1933](https://github.com/pereq-dev/hax/pull/1933) 已合并（2026-02-11），引入 specset int / specset bv 与 hax_mvcgen | 整数推理和 bit-vector 证明需使用不同规格集 |
| #1916 RustM 单子表达式难以自动化 | 上游讨论给出通过 @[spec] 与 mvcgen 将 RustM 规格归约为纯 Lean 目标的做法 | 不是简单消除 monad，而是提供合适 spec 并经 mvcgen 归约 |
| #1914 模块名首字母大写 | [PR #1927](https://github.com/pereq-dev/hax/pull/1927) 已合并（2026-02-11） | 上游已调整模块命名 |
| 默认生成完整 Lean package | [PR #2142](https://github.com/pereq-dev/hax/pull/2142) 已合并（2026-08-26） | 新版默认生成 lean-toolchain、lakefile、root module、Verification/ 与 Assumptions/ |

### 版本漂移

- Hax-FRI manifest 固定 Hax commit 1332b8fa19967234232473d0d3ec88e4d8ce8424，标题为升级 Lean v4.26.0，创建于 2026-01-20。
- Hax PR #1925（2026-02-09）和 #1933（2026-02-11）晚于该固定 commit；不能假定 Hax-FRI 已包含这些修复。
- Hax 0.5.0 changelog（2026-11-09）要求 Lean 4.35.0，并包含 Lean backend breaking changes；与 Hax-FRI Lean 4.26.0 基线不同，不能直接替换而不迁移。
- Hax 0.5.0 还涉及 Lean module 结构、Assumptions/、Aeneas/Charon 工具版本等变化。升级应作为独立兼容性实验。

### 证据边界

已读取 Hax issues/PR 状态和 PR 描述；#1925、#1927、#1933、#2142 均 merged。已读取 Hax 0.5.0 changelog。未在 Hax-FRI 运行旧版构建，也未做 4.26.0 → 4.35.0 迁移。上游 PR merged 不等于 rust-lean 项目已采用修复或端到端 FRI 正确性证明完成。

## M0.5｜MathFin：金融数学形式化库与可迁移的研究方法（2026-11-22）

> 固定审查仓库：[formal-applied-math/formal-mathfin](https://github.com/formal-applied-math/formal-mathfin)，commit `cbe842dda1e71fd7173f3325971796686dbf7feb`。Lean toolchain = `leanprover/lean4:v4.35.0`；Lake manifest 固定 Mathlib `e91b128082cc221d6432a6a5aadcd3243af8e76c`、BrownianMotion `497e5e2a60450796f75ab920e6c33addae4d644d`、LeanArchitect `9f3bb53916b9d6fa05b7777389e1844f82b1c9a6` 等依赖。

### 1. 覆盖范围与形式化状态

MathFin 是 Lean 4 数学金融库，覆盖随机分析、Itô 积分与公式、Girsanov、鞅表示、SDE、无套利理论、衍生品定价、固定收益、投资组合、风险度量和精算数学。

README 报告 906 项文献结果：866 `full`、18 `library_wrapper`、22 `reduced_core`。本轮额外解析三个 benchmark JSON：`risk_measures.json` 49 项、`portfolio_and_performance.json` 67 项、`binomial.json` 40 项，共 156 项，均标记 `full`。156 是本轮抽查的三个文件，不是全库重算。

项目将形式化保真度区分为：
- `full`：从诚实假设出发的真实形式化推导；
- `library_wrapper`：直接调用 statement 匹配的 Mathlib/BrownianMotion 定理；
- `reduced_core`：证明比文献命名结果更窄的核心内容；
- `placeholder`：可编译但尚未表达有意义的目标。

只有 `full + library_wrapper` 计入交付就绪数量。项目明确禁止把“能编译”与“忠实证明了文献定理”混为一谈。

### 2. 三个可迁移的金融数学案例

**A. Gaussian CVaR 的 Rockafellar–Uryasev 变分刻画**

在 Gaussian 损失模型 L = μ + σZ、σ>0、Φ(z)=α<1 下，证明 CVaRα(L) 等于 Rockafellar–Uryasev 目标函数 g(c) = c + E[(L-c)^+]/(1−α) 在所有阈值 c 上的最小值，且最小值在 c = VaRα(L) 取得。

证明不是只整理闭式公式，而是构造点态尾部证书：shortfall positive-part 至少覆盖尾部事件上的线性损失项；积分后得到任意阈值 c 的下界，再证明 VaR 处取等。源码：[RockafellarUryasev.lean](https://github.com/formal-applied-math/formal-mathfin/blob/cbe842dda1e71fd7173f3325971796686dbf7feb/MathFin/Risk/RockafellarUryasev.lean)。benchmark 状态为 `full`、Axioms-clean。限制：Gaussian 损失与参数化假设，不是对真实 A 股收益分布的经验验证。

**B. Markowitz Lagrangian FOC 的充分性**

对半正定协方差矩阵 (Sigma)，若组合 w 满足预算与目标收益约束，并满足
[
Sigma w=lambda_1mathbf 1+lambda_2mu,
]
则证明 w 在同一可行集合内具有不高于其他组合的方差。源码：[MarkowitzLagrangian.lean](https://github.com/formal-applied-math/formal-mathfin/blob/cbe842dda1e71fd7173f3325971796686dbf7feb/MathFin/Choice/Portfolio/MarkowitzLagrangian.lean)。证明使用约束切空间中的 admissible perturbation、方向导数系数和 KKT sufficiency。限制：证明的是 FOC (Rightarrow) 全局最小方差；没有证明每个最优组合都必须满足该 FOC。

**C. CRR 二叉树到 Black–Scholes 的收敛**

先把单步风险中性收益的特征函数写成 cos/sin 形式，证明 (n(phiarphi_n-1)) 收敛到 Gaussian 指数，再用复数幂极限和 Lévy 连续性定理得到 n 步对数收益的分布收敛；随后用有界 Put payoff 与 Put-Call Parity 得到 Call 价格收敛。源码：[CRRCharFun.lean](https://github.com/formal-applied-math/formal-mathfin/blob/cbe842dda1e71fd7173f3325971796686dbf7feb/MathFin/Models/Binomial/CRRCharFun.lean)、[CRRClosedForm.lean](https://github.com/formal-applied-math/formal-mathfin/blob/cbe842dda1e71fd7173f3325971796686dbf7feb/MathFin/Models/Binomial/CRRClosedForm.lean)。benchmark 状态为 `full`、Axioms-clean。

**额外的形式化质量案例：排除 vacuous theorem。** CRR Call 收敛定理曾把 no-arbitrage 假设量化到 n=0；但 n=0 时 u=d=1，no-arbitrage 条件不可能成立，因此原定理假设不可满足，证明会空洞成立。项目在 2026-08-20 修正为只要求 n≥1，并给出 `binomialNoArb_crr`，在 (|r|sqrt T<sigma) 时证明该条件可满足。该修正记录在 [binomial benchmark](https://github.com/formal-applied-math/formal-mathfin/blob/cbe842dda1e71fd7173f3325971796686dbf7feb/benchmarks/binomial.json)。这说明形式化审查不仅要看 proof term，还要检查前提是否可满足。

### 3. 公理审计与构建治理

- [MathFin/AxiomAudit.lean](https://github.com/formal-applied-math/formal-mathfin/blob/cbe842dda1e71fd7173f3325971796686dbf7feb/MathFin/AxiomAudit.lean) 对代表性关键定理使用 `#guard_msgs in #print axioms` 固定其公理依赖。
- 生成文件 [MathFin/AxiomAuditGen.lean](https://github.com/formal-applied-math/formal-mathfin/blob/cbe842dda1e71fd7173f3325971796686dbf7feb/MathFin/AxiomAuditGen.lean) 对 benchmark proof 实际引用的 1,115 个 MathFin 常量及 29 个上游常量固定精确公理集；新增 `sorryAx` 或非标准公理会导致对应 guard/build 失败。
- [build.yml](https://github.com/formal-applied-math/formal-mathfin/blob/cbe842dda1e71fd7173f3325971796686dbf7feb/.github/workflows/build.yml) 定义 Python honesty gates、`lake build`、声明索引与公理审计；[reproduce.sh](https://github.com/formal-applied-math/formal-mathfin/blob/cbe842dda1e71fd7173f3325971796686dbf7feb/scripts/reproduce.sh) 提供 clean-clone 复现命令，`--corpus` 还会逐条重新 elaboration benchmark。
- `MathFinFrontier` 的 connector 是单独的未证明声明库，不被 `MathFin` 导入；根目录 `Challenge.lean` 的两个 sorry 是 Palomar Challenge/Solution 契约的一部分，由 `Solution.lean` 对应证明。不能把这些外围目标的 sorry 与核心 `MathFin/` 的证明状态混为一谈。
- 本轮没有从 GitHub connector 获得该 commit 的 workflow run 或 status context；构建工作流“存在”不等于本轮已验证它通过。本机也没有 Lean/Lake/Elan，因此本轮 build = NOT_RUN。

### 4. 对量化金融研究的适用边界

MathFin 证明的是**金融数学模型与算法性质**，不是市场数据真实性、因子有效性或策略盈利性。对 AI_Trader #488 的合理分工是：

- Lean：形式化数据准入与程序不变量，例如 observation 的 `availableAt ≤ decisionTime`、as-of filter 不泄漏未来版本、point-in-time 股票池成员资格、订单/现金/持仓状态转换和风险约束；
- Python：读取真实行情/Level2、数值计算、统计检验、交易成本、样本外回测与性能评估；
- 数据供应商时间戳、历史修订、缺失数据与市场机制事实仍需独立数据证据，Lean 不能凭空证明这些外部事实为真。

本专题只建立这种方法映射，不接管 AI_Trader #488 的实证实验，也不声称已经实现 PIT Lean proof。

## M0.6｜PIT / No-Lookahead 最小 Lean 规格原型（2026-11-22）

> 代码位置：[examples/pit-no-lookahead](https://github.com/fweiger/AI_book/tree/topic/TOPIC-018/lean-formal-verification-20261122/topics/lean-formal-verification/examples/pit-no-lookahead)。独立 Lean 4.35.0 package，无 Mathlib 依赖；专用 GitHub Actions workflow 已执行并通过：Run #15 与 Run #19 均成功；最新 Run #19 在 PR head 1e700ff 上完成。

### 数据语义

`Observation` 将两个经常被混淆的时间分开：
- `eventTime`：市场事件实际发生的时间；
- `availableAt`：策略能够获得该记录的最早时间；
- `decisionTime`：策略作出决策的时点。

`eligibleRows` 只根据 `availableAt ≤ decisionTime` 过滤，不以 eventTime 代替数据可得时间。

### 已写入的定理

- `eligibleRows_no_lookahead`：任何进入 eligibleRows 的记录，其 availableAt 不晚于 decisionTime。
- `late_available_revision_excluded`：如果一条记录的 availableAt 晚于决策时点，即使 eventTime 较早，也不能进入当时的输入集合。
- 具体反例：eventTime=1、availableAt=3、decisionTime=2 的修订记录会被排除。

### 当前证据边界

- 源码、Lean toolchain、Lake package 和独立 Actions workflow 已建立；最新 Run #19 的 `lake build` 成功，job log 显示两个定理均由 Lean 编译。
- 最新 Run #19 的 `#print axioms` 对两个定理均输出 `[propext]`，没有 `sorryAx`、`Classical.choice` 或用户自定义 axiom。该标准公理依赖已在 job log 实际回读。 [Run #19](https://github.com/fweiger/AI_book/actions/runs/45031617398)。\n- 这是 eligibility filter safety theorem，不是完整 as-of join；尚未证明 latest eligible revision 选择、输入排序、重复版本优先级、空值处理。
- 定理假设 availableAt 时间戳本身可信；它不证明数据供应商时间戳真实，也不证明任何因子有效或策略盈利。
- 该原型位于 AI_book 专题分支，不修改 AI_Trader #488。

## M0.7｜跨学科“研究方向—论文—Lean/相邻项目”映射（2026-11-22）

> 完整方向和来源矩阵见 [field-evidence-matrix.md](field-evidence-matrix.md)。本节只记录本轮新核验的项目边界、版本线索和证据等级。

| 领域 | 本轮确认的 Lean 项目/框架 | 论文/理论来源 | 当前证据与限制 |
|---|---|---|---|
| 数学 | Mathlib、Formal Conjectures、Liquid Tensor | Mathlib CPP 2020、Mathlib Papers 索引 | 基础设施成熟，但具体 theorem 仍需逐项核验 |
| CS/程序验证 | CSLib、CertifyingDatalog、LeanLTL、Lentil、Loom、Veil、Velvet、Aeneas/Hax | CSLib EPTCS 2026、Datalog ITP 2025、LeanLTL ITP 2025、Veil CAV 2025、POPL 2026 multi-modal verifiers | 已读取多个 README、论文和配置；外部项目未在本轮独立 build |
| 密码学 | VCVio、ArkLib、CompPoly、Aeneas/Hax、rust-lean | VCVio ePrint 2026/899、Rust-to-Lean pipeline 2026 | 抽取、协议证明和实现精化是不同层次 |
| 分布式 | Veil、IFP、Lentil、Resonate Specification、btc-verified | Veil CAV 2025、Verdi PLDI 2015、IronFleet SOSP 2015、Raft USENIX 2014 | IFP 仅受限 Phase 1；Resonate 不是共识；btc-verified 不是完整 consensus proof；未确认完整 Lean Raft/Paxos |
| 经济学 | MathEconLib、gametheoryinlean/EconCSLib、nikhgarg/EconCSLib、Econlib | EconCSLib 两篇 2026 论文 | 两个 EconCSLib 同名但独立；MathEconLib 当前偏微观基础；宏观/计量仍有空白 |
| 金融数学 | MathFin、BrownianMotion、PIT prototype | MathFin arXiv 2606.01356、Markowitz、Rockafellar–Uryasev、CRR | MathFin 论文 804 benchmark vs 当前 README 906；不是经验回测系统 |
| AI/ML/统计 | AI4SLT、TorchLean、LeanDojo-v2 | AI4SLT ICML 2026、TorchLean 2026、LeanDojo-v2 2026 | 学习理论、模型验证、AI 证明工具需分开；未独立 build |
| 物理/量子 | Physlib、PhyslibAlpha、QuantumInfo、physicslib4、Lean-QuantumInfo | HepLean CPC 2025、Generalized Quantum Stein 2025、FormalQFT 2026 | 多个独立 codebase，不能当作一个完整统一库 |
| 信息论 | LeanInfoTheory、infotheorylib、rate_distortion_lean4、KTAIT | Rate-Distortion Lean 2026、Cover–Thomas、El Gamal–Kim | LeanInfoTheory 官网部分页面滞后；infotheorylib 使用 Lean 4.37.0-rc1 |
| 控制 | DynamicalSystems、LeanForControl、control-theory-in-lean、TorchLean | Foundations of Machine-Checked Control Theory in Lean 2026 | DynamicalSystems 与 LeanForControl 是不同项目；toolchain 版本不同 |

### 本轮重要边界发现

1. **BFT 不等于共识完整证明**：IFP README 声称 103 个 safety invariants 中 93 个已机器验证，但其 Phase 1 是两参与者、单 epoch 的受限实例；成员动态变化和完整部署语义不能据此推断。
2. **时序逻辑不等于分布式协议实现**：LeanLTL/Lentil 提供逻辑和 trace 语言；Veil 才是状态转换系统验证框架；具体协议仍需模型、故障假设和 safety/liveness theorem。
3. **AI4SLT 不等于金融策略验证**：它提供经验过程与泛化界的数学基础；市场分布、样本外表现和回测泄漏仍需数据与统计实验。
4. **StatWhy 是相邻非 Lean 工具**：其目标是检查统计假设检验程序是否声明了必要条件，不是证明未知总体分布假设为真。
5. **信息论项目并非同一库**：LeanInfoTheory 偏通用有限离散 API，infotheorylib 偏教材逐章映射，rate_distortion_lean4 聚焦有限字母表率失真定理。
6. **金融数学与实证量化有边界**：MathFin 可形式化风险、定价和组合理论；本轮没有找到成熟 Lean 项目直接覆盖 A 股 Level-2 因子、PIT 历史修订、IC/IR、交易成本和回测执行。

### PIT 原型最新构建状态（更新至 2026-11-22）

- 证明源码提交：2cbece7184815f8d17bf09130f66dd024630e51c。
- [Lean GitHub Actions Run #24](https://github.com/fweiger/AI_book/actions/runs/45031763832)：Lean 4.35.0 lake build success，3 个构建任务完成。
- eligibleRows_no_lookahead 与 late_available_revision_excluded 均编译成功；两个 theorem 的 print axioms 均为 [propext]。
- [Knowledge integrity Run #1255](https://github.com/fweiger/AI_book/actions/runs/45031763864)：success。
- 后续 Tracker-only commit 未修改 PIT proof/package。该结果仍只证明 eligibility filter safety，不是完整 latest-revision as-of join。

**本轮外部项目状态：** 未对上述外部 Lean 仓库执行独立 clean build；均按 README/论文/配置证据分级，不标 E3。


## M0.8｜跨学科论文—项目映射的源码时点核验（2026-11-23）

### 本轮直接读取的代表项目

| 项目 | 本轮读取文件/结果 | 版本与边界 |
|---|---|---|
| MathFin | 当前 main README、CITATION.cff、docs/coverage.md、lean-toolchain | README 906 corpus results（866 full / 18 library wrappers / 22 reduced cores）；CITATION 2.0.0（2026-11-11）为 833 delivery-ready；coverage 中 806 是 2026-11-08 检查点；Lean 4.35.0。数字属于不同日期/口径 |
| LeanInfoTheory | master README、lean-toolchain | v0.2.0（2026-11-05），811 declarations、57 modules，Lean 4.33.1；官网仍有 v0.1.0 / 601 declarations 旧页面 |
| rate_distortion_lean4 | README、MainResults.lean、lean-toolchain | Lean 4.28.0；有限字母表 rate-distortion direct/converse/boundary theorem；主结果文件有显式 axiom print 与 allowlist gate |
| AI4SLT | PMLR ICML 2026 官方论文页、GitHub README、lean-toolchain | Lean 4.32.0；论文覆盖 empirical processes/Gaussian concentration/Dudley/least-squares；当前 repo README 另列论文后的高维概率扩展 |
| TorchLean | main README、lean-toolchain | Lean 4.36.0；同一 Lean model 定义用于训练、图转换、证书检查和证明；CUDA 注册 native operators 使用 LibTorch ATen，须单独审计 backend 边界 |
| DynamicalSystems | main README、lean-toolchain | Lean 4.36.0-rc2；论文对应控制理论库；未独立 build |
| Veil / IFP | Veil main README/toolchain；IFP main README | Veil 2.0 / Lean 4.35.0；IFP 103 invariants 中 93 verified、10 pending；Phase 1 明确限于两个固定参与者、单 epoch |

### 论文与项目的一一对应关系

- AI4SLT 论文 ↔ YuanheZ/lean-stat-learning-theory；论文后的 repo 扩展必须分开归因。
- Rate-Distortion 论文 ↔ fubinyan/rate_distortion_lean4；主结果文件提供 axiom audit 入口，但本轮没有运行构建。
- Doll–Shames 控制理论论文 ↔ mcdoll/DynamicalSystems；当前 toolchain 是 Lean 4.36.0-rc2，需注意 RC。
- TorchLean 论文 ↔ lean-dojo/TorchLean；同一模型定义跨训练/图变换/验证/证明，但 CPU Lean rules 与 CUDA LibTorch native operator 是不同执行路径。
- HepLean CPC 论文 ↔ HEPLean/HepLean；论文明确使用 Lean 4 数字化高能物理内容。
- Veil CAV 2025 论文 ↔ verse-lab/veil；IFP 是使用 Veil 的应用案例，而不是 Veil 框架本身。

### 当前验收边界

- 论文原始页/官方项目 README/关键文件已读取，证据为 E1/E2。
- 本轮未对这些外部项目执行 clean clone、依赖下载、lake build 或独立 theorem/axiom 输出，均为 NOT_RUN。
- README 的 theorem 数量、no-sorry 声明、CI badge 不替代实际 CI job log。
- MathFin 的 906 / 833 / 806 / 804 分别属于当前 README、软件 release、历史 coverage audit、论文快照；不可混为一个数字。


## M0.9｜方向矩阵提交后的 CI 回归复验（2026-11-23）

- 首次完整性检查失败原因：sessions/README.md 引用了不存在的跨学科 session 文件；不是论文、项目或图谱 schema 错误。
- 修复后 PR head `c45e6d94e30a45bb797019f201baac20d4c17eb8`：Knowledge-base integrity Run #1268 PASS；Lean PIT Run #37 PASS。
- Lean Run #37 使用 Lean 4.35.0，lake build 成功；eligibleRows_no_lookahead 与 late_available_revision_excluded 编译通过，print axioms 均为 [propext]。
- 外部项目 clean build 仍 NOT_RUN；此 CI 只复验专题自己的 PIT 最小包和知识库完整性。


## M1.0｜项目审计批次 A：信息论、统计学习与分布式验证（2026-11-23）

本轮固定三个上游 commit，逐项核对论文—代码关系、许可证、toolchain/manifest、核心 theorem、占位证明/公理边界和实际构建证据。证据等级按本专题定义：E1 为源码/官方文档已读，E2 为固定版本有可回读的上游构建/CI 证据；本专题未独立 clean build，不能记 E3。

### A1. Rate-Distortion：当前源码审计完成，当前构建证据不闭合

- **论文**：[Aligning Information Theory and Formal Verification: A Lean Formalization of Rate-Distortion Theory](https://arxiv.org/abs/2610.22404)，arXiv:2610.22404，2026-10-14。
- **直接项目**：[fubinyan/rate_distortion_lean4](https://github.com/fubinyan/rate_distortion_lean4)。
- **固定版本**：main commit [6ebee5bca945015ec2964ea94148e6de3857959d](https://github.com/fubinyan/rate_distortion_lean4/commit/6ebee5bca945015ec2964ea94148e6de3857959d)；RateDistortion.lean blob 7719dbbe76a95a9020b2ec177dafe9d3dc2380da；MainResults.lean blob d426b605eddfb7c3d9a3d2f9212cf17c06fc244d。
- **许可**：GitHub metadata 的 license 为 null；固定 commit 的 tree 未找到根 LICENSE/COPYING。记为 LICENSE_NOT_FOUND_IN_AUDITED_TREE，不推断作者放弃版权。
- **环境**：Lean 4.28.0；Mathlib v4.28.0；lakefile.toml、lake-manifest.json 均存在，manifest 固定 Mathlib revision。
- **形式化对象**：有限字母表、有限 PMF、有限非负 distortion、确定性 encoder/decoder、blocklength 序列和 nats 口径；核心结果覆盖 direct/converse、boundary achievability、achievable iff、最优 test channel attained 和 rate-distortion right-continuity。不是连续信源、任意随机码或无限字母表的一般定理。
- **源码审查**：固定 commit 的 4 个 Lean 文件均未发现 sorry、顶层 axiom 或 opaque 声明。MainResults.lean 对五个核心 endpoint 运行 print axioms，并通过 Lean.collectAxioms 将允许集合限定为 propext、Classical.choice、Quot.sound；当前源码存在这套审计入口，但本轮没有运行当前版本。
- **构建证据时点问题**：仓库的 [build-verification.log](https://github.com/fubinyan/rate_distortion_lean4/blob/7b9bfcaa42cc0365e7f8d4c1094b8309b61ef269/build-verification.log) 是 commit 7b9bfcaa42cc0365e7f8d4c1094b8309b61ef269（2026-09-22）加入，记录 Lean 4.28.0、3161 jobs 成功及五个 endpoint 的 axioms。可是当前 RateDistortion.lean 在 2026-10-13 的 commit 6ebee5b 又有 6393 additions / 6132 deletions；docs/verification.md 仍引用旧的 abe3000 source snapshot。故旧 log 不能证明当前 main 构建通过。
- **CI/文档不一致**：当前固定 tree 没有 .github/workflows/ 文件，Actions API 没有对应运行；README/verification 文档却声称有面向 push/PR 的 GitHub Actions workflow。应先修正文档或恢复 workflow，再对当前 commit clean build。
- **审计结论**：PARTIAL。数学源码结构和 axiom gate 值得复用；当前 main 的构建未验证，许可证未找到，CI 声明与仓库现状不一致。

### A2. AI4SLT：release build 与 core no-placeholder audit 有上游证据

- **论文**：[AI4SLT: Empirical Processes in Lean 4 for Formal Statistical Learning Theory](https://proceedings.mlr.press/v306/zhang26cd.html)，ICML 2026 / PMLR 306:156234–156262；arXiv [2602.02285](https://arxiv.org/abs/2602.02285)。
- **直接 companion**：[YuanheZ/lean-stat-learning-theory](https://github.com/YuanheZ/lean-stat-learning-theory)，PMLR 官方论文页直接列出该代码仓库。
- **固定版本**：当前 main commit [d0f506f0a695018265dccb33bcb05e2f5ca1c876](https://github.com/YuanheZ/lean-stat-learning-theory/commit/d0f506f0a695018265dccb33bcb05e2f5ca1c876)；release tag v4.32.0 指向 commit 482a1a56daf792b33afe8cf7f07f127dc0af8640。两者比较仅有 README 的 2 个提交，Lean 源码未变化。
- **许可/环境**：Apache-2.0；Lean 4.32.0、Mathlib v4.32.0；manifest 将 Mathlib 固定到 81a5d257c8e410db227a6665ed08f64fea08e997；仓库共 68 个 Lean 文件。
- **论文原始形式化范围**：Gaussian Lipschitz concentration、sub-Gaussian processes 的 Dudley entropy integral、least-squares/sparse regression sharp rate。当前仓库 README 还包含论文之后扩展的 Hanson–Wright、random matrix、matrix Bernstein 等内容；不能将这些后续扩展倒归为原论文贡献。
- **关键源码入口**：[GaussianLipConcen.lean](https://github.com/YuanheZ/lean-stat-learning-theory/blob/d0f506f0a695018265dccb33bcb05e2f5ca1c876/SLT/GaussianLipConcen.lean) 中 gaussian_lipschitz_concentration / one-sided theorem；[Dudley.lean](https://github.com/YuanheZ/lean-stat-learning-theory/blob/d0f506f0a695018265dccb33bcb05e2f5ca1c876/SLT/Dudley.lean) 中 dudley_chaining_bound_countable / dudley；[BasicInequality.lean](https://github.com/YuanheZ/lean-stat-learning-theory/blob/d0f506f0a695018265dccb33bcb05e2f5ca1c876/SLT/LeastSquares/BasicInequality.lean) 中 basic_inequality。
- **证明状态**：v4.32.0 release notes 明确记录 LEAN_NUM_THREADS=$(nproc) lake build 成功，并扫描 SLT/ 未发现 sorry、admit、axiom、native_decide。 本轮对三个代表 theorem 文件做源码检查，未发现显式占位或顶层自定义 axiom。该证据来自上游 release 声明，不是本专题独立 build。
- **CI 边界**：固定 tree 没有 .github/workflows/，Actions API 未发现 workflow run；应记为 RELEASE_BUILD_EVIDENCE，不能写成 GitHub Actions CI PASS。
- **审计结论**：PASS / E2（release build evidence）。当前 main 的 Lean 源码与已验证 release 相同；无持续 CI 仍是工程维护风险。

### A3. Veil：多模态验证器的 CI 与信任边界可回读

- **论文**：[Veil: A Framework for Automated and Interactive Verification of Transition Systems](https://doi.org/10.1007/978-3-031-98682-6_2)，CAV 2025。
- **直接项目**：[verse-lab/veil](https://github.com/verse-lab/veil)。
- **固定版本**：main commit [5a525eeca8cee37b2da8c010552db9b1aae968c2](https://github.com/verse-lab/veil/commit/5a525eeca8cee37b2da8c010552db9b1aae968c2)；Apache-2.0；Lean 4.35.0；Lake package manifest 版本 1.3.0。
- **依赖锁定**：lean-smt b8633e75...、Loom dc269f28...、VerifiedHAMT 244601f8...、Lasso 74515461...、Lentil 61e533f...，以及 Batteries/Aesop v4.35.0、ProofWidgets 固定 commit。
- **实际 CI**：[Run #442](https://github.com/verse-lab/veil/actions/runs/45014566842) 精确对应上述 main commit；Linux-x86_64 和 macOS-aarch64 两个 job 均通过 Build Veil、VeilTest、LSP/Widgets、VS Code Extension 和 Examples。
- **TrustAudit 实际输出**：CI job log 编译 VeilTest.TrustAudit 并报告七条 shipped route（fair、prune、patOnly、crossing、dijkstra、ndfs、interned）均 clean；positive control 刻意加入一条带 implemented_by 的 control route，检测器成功发现 1 个实现替换并最终 PASS。该审计递归检查指定 route 可达常量的 type/value，检查项目自定义 unsafe 与 implemented_by；不是全仓库所有模块均无 unsafe 的声明。
- **SMT/Kernel 边界**：CertificateResult 使用 collectAxioms，记录 kernelChecked 和 offenders；标准 axiom 集为 propext、Classical.choice、Quot.sound。veil.synthesizer.trust 默认 false。若 solver step 无法重放或 Kernel 拒绝，trusted fallback 会发出警告并使 theorem 依赖 sorryAx。因此 print axioms 不是完整的运行路径审计，必须同时检查 unsafe/implemented_by、solver mode 和 certificate result。
- **SCP 示例范围**：[SCP.lean](https://github.com/verse-lab/veil/blob/5a525eeca8cee37b2da8c010552db9b1aae968c2/Examples/StellarConsensus/SCP.lean) 明确说明当前 Veil 示例不证明 liveness，只证明 intertwined_safe safety property。Background 的 axiom_0、axiom_1、qi_intertwined 是抽象模型的 typeclass contract 字段，不是 Lean 顶层全局 axiom；one_such_Background 给出一个由具体 FBA.System、intact/intertwined 集及包含关系构造的 Background 实例。该实例仍以这些模型条件为前提。
- **不可混淆的原始基线**：Losa & Dodds 的 [FMBC 2020 SCP formal verification paper](https://doi.org/10.4230/OASIcs.FMBC.2020.9) 使用 Ivy + Isabelle/HOL，在 eventual synchrony 下对任意但固定配置证明 safety 与 liveness；Veil 的 Lean SCP 示例不是该完整证明的等价替代。
- **审计结论**：PASS / E2（固定 main commit 上游 CI + TrustAudit）；SCP safety case 为 PARTIAL，不得宣称 liveness 已由 Veil Lean 示例证明。

### 批次 A 的横向结论与量化迁移候选

| 项目 | 形式化/验证层 | 可迁移到量化研究的候选 | 不能推出 |
|---|---|---|---|
| Rate-Distortion | 信息量、编码率、失真和渐近可达性定理 | L2/分钟数据压缩、特征量化、信号压缩误差与信息率约束 | 不能证明压缩特征仍有 alpha；当前 main 也未 build |
| AI4SLT | 概率集中、经验过程、泛化界、稀疏回归不等式 | 因子模型复杂度、样本外泛化假设、过拟合边界的理论规格 | 不证明市场分布满足假设、不证明因子收益显著或盈利 |
| Veil | 状态转换系统、Safety/Liveness、SMT+Kernel certificate、trust audit | 订单/持仓状态机、现金守恒、重复成交禁止、仓位上限、订单终态与风控不变量 | 不证明行情输入真实、撮合系统实现符合模型或策略有收益 |

**AC-05 当前进度口径**：本批新增 3 张项目审计卡，其中 AI4SLT 与 Veil 有当前代码对应的上游 build/CI 证据；Rate-Distortion 只有旧 commit 的 build log，当前 main 未验证且许可证未找到。加上首批 10 项准入中 Mathlib 的 bors success，目前有 3 个项目具备可回读 build/CI 证据，AC-05 仍为 PARTIAL；不能把 10 个 metadata snapshot 当成 10 个项目已通过审计。
