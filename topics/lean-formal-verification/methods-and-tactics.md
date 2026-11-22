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
- **步骤**：在 Rust 源码中写 pre/post 函数和 Hax annotations；通过 Hax 抽取到 Lean；用 hax_lib::lean::after 注入 theorem；对 bit-vector 运算尝试 hax_bv_decide bit-blasting。
- **工程技巧**：把 adc_pre 与 adc_post 拆成独立函数，降低 Lean 中展开和推理复杂度。
- **失败边界**：当前 README 记录了 cast、shift、tuple projection、monadic binds 和 BitVec fragment 支持问题；抽取/编译失败时不得报告 theorem PASS。
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
