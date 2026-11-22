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
