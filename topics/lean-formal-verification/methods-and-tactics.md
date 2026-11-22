# TOPIC-018｜方法与技巧库（首版分类）

> 本页是方法目录，不把 tactic 名称当作完整教程。每张方法卡后续必须补充来源、最小可运行例子、前置条件、失败模式和版本。

## 1. 问题形式化与类型建模

- **Definition-first**：先定义对象、关系、状态和约束，再陈述性质；避免把自然语言歧义直接塞入 theorem。
- **Structure / Typeclass**：将共享数据和数学结构放入结构体/类型类；尽量使用足够弱的假设，避免无必要地固定到某个具体模型。
- **State-machine invariants**：把协议状态转换、合法操作和安全不变量显式建模。
- **Dependent types**：当对象的类型需要携带索引、维度、边界或前置条件时使用；要控制复杂度和 elaboration 成本。

## 2. 证明构造与分解

| 技巧 | 典型用途 | 风险/注意 |
|---|---|---|
| intro | 引入全称量词/蕴含前提 | 先确认目标的逻辑结构 |
| have | 建立中间引理 | 中间命题应服务于证明依赖结构 |
| apply / exact | 应用已有定理或精确提交证明项 | 类型参数和隐式假设需检查 |
| rw | 用等式重写表达式 | 注意重写方向和匹配位置 |
| simp / simp only | 规范化表达式 | 关键证明宜显式控制 simp 集合 |
| constructor | 拆解合取、结构或等价目标 | 每个子目标都要完整关闭 |
| induction | 对自然数、列表、归纳结构证明 | 归纳假设和归纳变量选取决定证明难度 |
| cases | 对归纳对象或条件分支分析 | 分支覆盖与不可达情况要清楚 |
| calc | 展示多步等式/不等式链 | 每一步注明理由，避免隐藏推导 |

## 3. 自动化与定理搜索

- exact?、apply?、rw?：探索可复用的现有定理；最终代码应记录明确使用的结果。
- simp?：发现可能的简化规则；稳定证明可评估改写为 simp only。
- aesop：搜索逻辑结构中的证明路径；应观察生成目标和依赖，避免把自动化当黑盒结论。
- omega：适合 Presburger 算术范围内的整数/自然数约束。
- linarith：线性算术关系。
- ring：交换半环/环上的多项式恒等式。
- nlinarith：一定范围内的非线性算术推理。
- Mathlib API、类型/表达式搜索与 Loogle：先找已有定义与定理，避免重复造轮子。

**版本提醒**：tactic 的可用性、导入模块和自动化行为依赖 Lean/Mathlib 版本；每个示例必须在锁定环境中实际构建。

## 4. 大型证明工程

- **定理依赖图**：先拆主定理为可独立审查的定义、引理和主结论。
- **Blueprint**：保持数学叙述、依赖关系和 Lean 声明双向可追踪。
- **接口先行**：对子任务定义稳定 theorem signature，减少 Agent 间接口漂移。
- **分层模块**：把通用数学基础、领域模型、领域定理和案例应用分层。
- **并行工作**：只并行无循环依赖的子目标；统一由主维护者整合并编译。
- **证明审查**：检查隐藏假设、非预期公理、sorry/admit、依赖版本与 statement fidelity。

## 5. 程序实现验证与组合方法

- **Specification**：先定义程序应满足的输入/输出与不变量。
- **Refinement**：建立实际程序语义与形式化模型之间的对应关系；这是“验证模型”升级为“验证实现”的关键桥梁。
- **Extraction / Translation**：使用 Aeneas/Charon、Hax 等工具将受支持的源代码转成可证明表示；需记录支持子集和翻译语义。
- **Model Checking**：在有限/抽象状态空间搜索反例。
- **SMT**：自动求解适合的约束子问题。
- **Property-based / Differential Testing**：作为实现级补充证据，不能冒充形式化精化证明。

## 6. AI Agent 协作方法

1. 人类/领域专家定义问题和自然语言规格。
2. Agent A 提出形式化定义与候选 lemma。
3. Agent B 以不同路径审查 statement fidelity、隐含假设和边界。
4. Lean 编译器/Kernel 检查 proof term。
5. Agent C 审查公理依赖、sorry/admit、版本与构建日志。
6. 人类确认形式化表达是否忠实对应原研究问题。
7. 合并前由非主要实现者独立复现。

AI 可以协助搜索和生成证明，但不能代替领域专家确定模型，也不能代替 Kernel 对 proof term 的检查。

## 7. 方法卡模板

每个方法卡必须包含：

- Method ID / 名称 / 领域 / 解决的问题
- 最小 Lean 代码和固定 toolchain
- 前置假设、输入类型和输出性质
- 操作步骤、可观察成功条件
- 常见失败、反例和性能/维护成本
- 适用范围与不适用场景
- 原始来源、源码 commit、证据等级
- 可迁移领域及需要重新验证的部分


## 8. 已有源码案例的方法卡

### M-01｜Hax annotations + bit-blasting 验证定宽算术

- **领域/问题**：密码学实现中的定宽整数运算，例如 32-bit limb addition with carry。
- **输入/输出**：Rust 函数 adc_u32(a,b,carry) 输出 sum 与 carry_out。
- **规格**：carry、carry_out 属于 {0,1}；在更宽的 u64 语义下验证 a+b+carry = sum+2^32×carry_out。
- **步骤**：优先参考 Hax 官方 ADC 示例：在 Rust 源码用 `#[hax_lib::lean::after]` 注入 Hoare triple；将前后置条件表达为纯 Lean propositions；设置 `hax_mvcgen.specset "bv"`；使用 `hax_mvcgen` 生成纯验证条件，再用 `bv_decide` bit-blasting。
- **工程技巧**：把 adc_pre 与 adc_post 拆成独立函数，降低 Lean 中展开和推理复杂度。
- **失败边界**：早期 PoC 的 cast、shift、tuple projection 和 BitVec fragment 问题已有部分上游修复；旧 README 是历史问题清单。仍须锁定 Hax 版本、使用正确 specset，并在实际 build 后才报告 theorem PASS。
- **来源**：[README](https://github.com/Verified-zkEVM/rust-lean/blob/49a83d2a231c24f8a26a694ca2badaa36fb3914d/hax-annotations-adc/README.md) · [Rust 源码](https://github.com/Verified-zkEVM/rust-lean/blob/49a83d2a231c24f8a26a694ca2badaa36fb3914d/hax-annotations-adc/src/lib.rs)。
- **状态**：E1；未独立运行 Hax/Lean。

### M-02｜Rust extraction → Lean model → protocol specification

- **领域/问题**：把真实密码学/零知识证明 Rust 组件与协议级数学规格关联。
- **步骤**：选择小而纯的 Rust 函数 → Hax/Aeneas 抽取 Lean 表示 → 复用 ArkLib/CompPoly 规格 → 证明抽取实现满足规格。
- **案例**：Plonky3 单轮 FRI folding；Hax-FRI README 报告基础 proof 文件可构建，但 FoldingCorrectness 仍待证明。
- **工程技巧**：先建立稳定的 Lean import surface；只导入需要的 ArkLib 模块，避免 Hax 与 ArkLib 名称冲突；同时固定 Hax、ArkLib、Mathlib 的依赖 commit。
- **失败边界**：抽取代码编译、基础引理通过和协议正确性证明是三个不同验收层次。
- **来源**：[Hax-FRI README](https://github.com/Verified-zkEVM/rust-lean/blob/49a83d2a231c24f8a26a694ca2badaa36fb3914d/hax-FRI/README.md)。
- **状态**：E1；本轮未独立构建。

### M-03｜项目版本 + manifest 双锁定

- **领域/问题**：跨机器、跨 Agent 复现 Lean 项目。
- **步骤**：固定项目 commit；读取 lean-toolchain；读取 lakefile；解析 lake-manifest 中的所有依赖 revision；保留 build log 和 CI。
- **失败边界**：只记录 Lean 版本或 lakefile 声明，不足以重建完全相同的依赖树。
- **来源**：本专题 M0 的 8 个 Lake manifest 审计快照。
- **状态**：E1；构建复现待做。


### M-01 修订｜采用 Hax 官方 ADC 方法，而不是停留在历史 PoC

- **推荐流程**：[Hax 官方 lean_adc 示例](https://github.com/cryspen/hax/blob/c5482e5a4c5713d3fb496435517d70d15c1b1393/examples/lean_adc/src/lib.rs)。
- **规格建模**：将 carry 范围和 64-bit arithmetic identity 写成纯 Lean proposition；不要让 BitVec 决策过程直接处理未经规范化的 RustM 规格。
- **证明步骤**：在 Rust 中用 \`#[hax_lib::lean::after]\` 注入 Hoare triple；设定 \`hax_mvcgen.specset "bv"\`；使用 \`hax_mvcgen [function]\` 生成纯 verification conditions；最后 \`bv_decide\`。
- **tuple 处理**：优先在 Hoare triple 中模式匹配 \`⟨sum, carry_out⟩\`；不要依赖旧 PoC 中的 \`r.fst/r.snd\`。
- **证据边界**：上游 PR #1959 已合并并加入官方 examples；本专题未独立运行 \`make\` / \`lake build\`。

### M-04｜多语义规格集：数学整数与位向量分开证明

- **问题**：同一个定宽整数运算既可能需要按数学整数推理，也可能需要按机器位宽和溢出语义推理；一个 simp/spec 集合难以同时服务两种目标。
- **方法**：在库层分别标注 \`@[specset int]\` 与 \`@[specset bv]\`；按证明目标设置 \`hax_mvcgen.specset\`；用 \`hax_mvcgen\` 生成对应 VC。
- **bit-vector 路线**：\`set_option hax_mvcgen.specset "bv"\` → \`hax_mvcgen [f]\` → \`bv_decide\`。
- **整数路线**：选择 \`int\` specset，再配合 \`grind\` / \`omega\` 等适合数学整数目标的 tactic。
- **失败边界**：specset 选择错误时，tactic 可能无法把目标归一化到支持的 BitVec fragment；不能把 tactic 不支持误判为程序性质为假。
- **来源**：[Hax PR #1933](https://github.com/cryspen/hax/pull/1933) · [Hax PR #1959](https://github.com/cryspen/hax/pull/1959)。
- **状态**：E1 / 上游 PR 与示例源码已读；本专题未构建。

### M-05｜同源 Rust 输入下比较 Hax 与 Aeneas

- **问题**：避免仅凭工具介绍比较 Rust→Lean extraction 工具。
- **步骤**：固定同一个 Rust source blob；分别记录 Rust HIR/MIR 路线、生成的 Lean 语义类型、Option/Result/Monad 表达、算术模型、proof scripts、sorry/axiom、依赖锁和构建日志。
- **本案例**：同一 \`compute_log_arity_for_round\` 源码；Hax 输出 \`RustM\`，Aeneas 输出 \`Result\`。
- **观察指标**：源代码覆盖、生成表示复杂度、局部 theorem 完成度、proof friction、跨库桥接成本、build reproducibility。
- **失败边界**：一个函数的比较不能推断全语言支持率、性能或工具普遍优劣；必须扩展到多类 Rust 结构和更大程序。
- **来源**：[Hax pipeline](https://github.com/Verified-zkEVM/rust-lean/tree/49a83d2a231c24f8a26a694ca2badaa36fb3914d/hax-FRI) · [Aeneas pipeline](https://github.com/Verified-zkEVM/rust-lean/tree/49a83d2a231c24f8a26a694ca2badaa36fb3914d/aeneas-FRI/fold_arity_lean)。
- **状态**：E1 / 同源文件和证明源码已读；构建 NOT_RUN。

### M-06｜跨库桥接：显式管理 axioms、opaque 和 sorry

- **问题**：不同 Lean 库因同名定义、实例或版本冲突无法直接导入，研究者可能把已证明的性质先抽象成 axiom，再继续使用领域库。
- **方法**：把源程序性质、抽象模型、跨库映射和领域定理拆开；每个 bridge 记录 statement、source theorem、映射函数、假设和 proof status；对每个 axiom/opaque 建立责任清单；优先用可证明的 refinement lemma 替代公理。
- **审计**：静态搜索 \`sorry/admit/axiom/opaque\`；随后在锁定环境运行 \`lake build\` 和 \`#print axioms theoremName\`，确认 theorem 的传递依赖。
- **本案例**：Aeneas BasicProofs 源码无显式 sorry/axiom；ArkLib target 为处理 \`BitVec.toNat_pow\` 冲突而声明 3 个 axioms 和 1 个 opaque。
- **失败边界**：axiom 并非自动错误，但它把证明义务移出当前 Lean theorem；不能把使用该 axiom 的定理宣传成完全由 Kernel 从程序实现推导出的结果。
- **来源**：[Aeneas FoldingCorrectness.lean](https://github.com/Verified-zkEVM/rust-lean/blob/49a83d2a231c24f8a26a694ca2badaa36fb3914d/aeneas-FRI/fold_arity_lean/FoldArityVerif/FoldingCorrectness.lean)。
- **状态**：E1 / 源码依赖边界已读；未运行 \`#print axioms\`。

### M-07｜把成功返回与前置条件写进定理

- **问题**：Rust 的 \`usize\` subtraction 可能在无效输入下 panic；只证明成功返回值的性质，不等于证明函数对所有输入总能正常返回。
- **方法**：明确列出原 Rust 的 debug_assert / precondition；在 Lean theorem 中同时写明输入不等式、函数成功返回等式（例如 \`h_result : f args = .ok result\`）和待证后置性质。
- **本案例**：FRI arity 的 target-distance 与 next-input-distance 定理依赖高度不等式；结论只对成功返回路径成立。
- **失败边界**：若要证明 panic-freedom/total correctness，还需单独证明输入条件足以保证所有 checked subtraction 和分支成功。
- **来源**：[Hax FoldingCorrectness](https://github.com/Verified-zkEVM/rust-lean/blob/49a83d2a231c24f8a26a694ca2badaa36fb3914d/hax-FRI/lean/P3FriProofs/Proofs/FoldingCorrectness.lean) · [Aeneas BasicProofs](https://github.com/Verified-zkEVM/rust-lean/blob/49a83d2a231c24f8a26a694ca2badaa36fb3914d/aeneas-FRI/fold_arity_lean/FoldArityVerif/BasicProofs.lean)。
- **状态**：E1 / 源码方法已读；未构建。

## 9. Hax 规格分组与版本升级方法卡

### M-15｜Hax 项目版本升级与生成结构迁移

- **问题**：Hax 生成代码与 Lean proof library、Aeneas/Charon、Lean toolchain 强版本耦合。
- **步骤**：固定原项目 commit/Hax commit/Lean toolchain/Lake manifest；先复现旧环境；单独建立升级分支；采用新版本迁移 Extraction/、Assumptions/、Verification/、root module 与 Lake 配置；重跑 extraction、Lean build、spec proofs 和项目级 correctness theorem；保留新旧生成代码差异和日志。
- **失败边界**：只升级 Lean 或 Hax CLI，不同步迁移 proof library、Aeneas/Charon 和 manifest，会形成不可复现混合环境。
- **来源**：[Hax PR #2142](https://github.com/pereq-dev/hax/pull/2142) · [Hax CHANGELOG](https://github.com/pereq-dev/hax/blob/main/CHANGELOG.md)。
- **状态**：E1；迁移和构建未执行。

### M-08｜用形式化保真度等级约束研究结论

- **问题**：一个 Lean 文件可以编译，但它可能只是结构投影、假设已包含结论，或只证明了命名定理的一个缩减版本。
- **方法**：每项文献结果登记 statement、hypotheses、formalization_scope、proof status；区分 `full`、`library_wrapper`、`reduced_core`、`placeholder`；交付数量只统计 full + library_wrapper。
- **审计重点**：假设是否可满足；结论是否真的从假设推导；是否把 textbook conclusion 放进结构字段；是否存在未披露的 axiom/sorry。
- **来源**：[MathFin glossary](https://github.com/formal-applied-math/formal-mathfin/blob/cbe842dda1e71fd7173f3325971796686dbf7feb/docs/glossary.md) · [coverage policy](https://github.com/formal-applied-math/formal-mathfin/blob/cbe842dda1e71fd7173f3325971796686dbf7feb/docs/coverage.md)。
- **状态**：E1 / 项目方法和 benchmark schema 已读。

### M-09｜生成式公理审计与 CI soundness floor

- **问题**：单独人工查看少量 theorem 的 `#print axioms`，无法覆盖大型库中 benchmark 实际依赖的全部常量。
- **方法**：建立 curated `AxiomAudit.lean`；从 benchmark 引用索引生成 `AxiomAuditGen.lean`；对每个被引用常量固定 `#print axioms` 的输出；通过 `#guard_msgs` 把变化变成 build failure；再用 Python gate 检查生成文件 freshness、sorry 和 ledger 状态。
- **本案例**：MathFin 生成审计覆盖 1,115 个 MathFin 常量与 29 个上游常量；默认 CI 包含 Python gates + `lake build` + declaration index/ratchet。
- **失败边界**：这是 benchmark 引用闭包，不等于所有未被 benchmark 使用的声明都已审计；本专题没有运行 MathFin build。
- **来源**：[AxiomAuditGen.lean](https://github.com/formal-applied-math/formal-mathfin/blob/cbe842dda1e71fd7173f3325971796686dbf7feb/MathFin/AxiomAuditGen.lean) · [build.yml](https://github.com/formal-applied-math/formal-mathfin/blob/cbe842dda1e71fd7173f3325971796686dbf7feb/.github/workflows/build.yml)。
- **状态**：E1 / 构建治理源码已读；build NOT_RUN。

### M-10｜用点态证书证明风险度量的最优性

- **领域/问题**：证明 Gaussian CVaR 是 Rockafellar–Uryasev 目标函数的最小值。
- **步骤**：先确定尾部事件 Z > z；构造 shortfall positive-part 大于等于尾部事件上的线性损失项；对两边积分；利用 Gaussian tail mass 和 truncated first moment 化简；在 VaR 阈值处证明取等。
- **技巧**：将最优性证明转化为一个可积分的 pointwise certificate，避免直接求导或引入额外凸分析 machinery。
- **失败边界**：该案例在 Gaussian loss、(sigma>0)、(Phi(z)=alpha<1) 条件下成立；不能直接推到任意经验分布或厚尾收益。
- **来源**：[RockafellarUryasev.lean](https://github.com/formal-applied-math/formal-mathfin/blob/cbe842dda1e71fd7173f3325971796686dbf7feb/MathFin/Risk/RockafellarUryasev.lean)。
- **状态**：E1 / theorem 与 proof 源码已读。

### M-11｜用特征函数与 Lévy 连续性定理证明离散模型收敛

- **领域/问题**：证明 CRR n-step risk-neutral log-return 收敛到 Black-Scholes Gaussian law。
- **步骤**：精确计算单步特征函数；将其写成 cos/sin；证明 n 乘以 (phi_n - 1) 收敛到 Gaussian 指数；应用复数幂极限；再用 Lévy continuity theorem 从特征函数收敛推出弱收敛。
- **价格层**：先对有界 Put payoff 使用弱收敛，再通过 Put-Call Parity 推出 Call 价格极限，避免直接处理无界 Call payoff 的 uniform-integrability/Vitali 步骤。
- **失败边界**：CRR 每步风险中性概率必须满足概率约束；Call 收敛还依赖 no-arbitrage 假设。必须先证明这些假设可满足。
- **来源**：[CRRCharFun.lean](https://github.com/formal-applied-math/formal-mathfin/blob/cbe842dda1e71fd7173f3325971796686dbf7feb/MathFin/Models/Binomial/CRRCharFun.lean) · [CRR benchmark](https://github.com/formal-applied-math/formal-mathfin/blob/cbe842dda1e71fd7173f3325971796686dbf7feb/benchmarks/binomial.json)。
- **状态**：E1 / full benchmark entry 与源码已读。

### M-12｜从 Lagrangian FOC 与可行扰动推出全局最优性

- **领域/问题**：证明满足预算、目标收益约束及一阶条件的组合具有最小方差。
- **步骤**：定义 admissible perturbation (delta w)，要求它与预算约束和目标收益约束的法向量正交；把 (Sigma w=lambda_1mathbf 1+lambda_2mu) 代入方向导数；利用两个正交条件消去乘子项；再结合 (Sigma) 半正定和 KKT sufficiency 得到全局最优性。
- **失败边界**：当前证明 FOC 是充分条件；没有证明所有最优解必然满足 FOC，也没有单独推出所有约束下的闭式有效前沿。
- **来源**：[MarkowitzLagrangian.lean](https://github.com/formal-applied-math/formal-mathfin/blob/cbe842dda1e71fd7173f3325971796686dbf7feb/MathFin/Choice/Portfolio/MarkowitzLagrangian.lean) · [portfolio benchmark](https://github.com/formal-applied-math/formal-mathfin/blob/cbe842dda1e71fd7173f3325971796686dbf7feb/benchmarks/portfolio_and_performance.json)。
- **状态**：E1 / full benchmark entry 与源码已读。

### M-13｜证明前提可满足，避免 vacuous theorem

- **问题**：Lean theorem 即使有 proof term，也可能因为假设不可能成立而空洞为真。
- **方法**：对关键 theorem 的假设单独构造 witness；或证明在一组明确参数条件下假设可满足；对边界值（如 n=0）单独分析。
- **本案例**：CRR Call 收敛定理曾对所有 n 包括 n=0 要求 no-arbitrage；n=0 时 u=d=1，条件不可能成立。项目修正为 n≥1，并证明 (|r|sqrt T<sigma) 足以保证 no-arbitrage。
- **失败边界**：一个 witness 只证明假设非空，不证明模型假设符合真实市场；需要把数学可满足性与数据/经济真实性分开。
- **来源**：[binomial benchmark correction](https://github.com/formal-applied-math/formal-mathfin/blob/cbe842dda1e71fd7173f3325971796686dbf7feb/benchmarks/binomial.json)。
- **状态**：E1 / 历史修正记录与 theorem 条件已读。

### M-14｜用 availableAt 而不是 eventTime 证明 PIT/no-lookahead

- **领域/问题**：防止历史修订、晚到数据和延迟发布信息进入过去的交易决策。
- **数据类型**：将 observation 分成 `eventTime`（事件发生时间）、`availableAt`（策略可获得时间）和 `decisionTime`（决策时间）。
- **最小定义**：`eligibleRows t rows := rows.filter (fun row => decide (row.availableAt ≤ t)))。
- **核心证明**：对 `List.mem_filter` 展开，得到每个输出元素满足 availableAt ≤ t；再证明 late revision 在 availableAt > t 时被排除，即使 eventTime ≤ t。
- **工程技巧**：把时间语义编码在结构体字段和函数签名中，避免依赖调用者记住“发布日期”和“事件日期”不同。
- **失败边界**：该定理只证明 filter safety；未证明 latest-version selection、排序、revision tie-break、source timestamp authenticity、标签窗口隔离或生产代码实现。
- **来源**：[PITNoLookahead.lean](https://github.com/fweiger/AI_book/blob/topic/TOPIC-018/lean-formal-verification-20261122/topics/lean-formal-verification/examples/pit-no-lookahead/PITNoLookahead.lean) · [dedicated workflow](https://github.com/fweiger/AI_book/blob/topic/TOPIC-018/lean-formal-verification-20261122/.github/workflows/lean-pit-no-lookahead.yml)。
- **状态**：E1 / Lean 源码和 package 已提交；GitHub Actions build 结果待回读。
