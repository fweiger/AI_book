# TOPIC-018｜形式化研究工作流 Playbook

## 目标

将一个自然语言数学/工程主张转化为可审查的 Lean 形式化对象，并在涉及实际软件时明确证明模型与实现之间的关系。

## 工作流

### Step 1｜固定原始问题

记录原始论文/规格/自然语言主张、作者定义、上下文、目标对象和证据位置。不要先改写成自己熟悉的数学问题。

**交付**：source statement、术语表、未决歧义。

### Step 2｜拆出定义、假设与目标

明确对象、类型、输入与输出、时间/概率/状态/边界条件、前提和待证明结论，以及有限性、连续性、可测性、独立性或完备性等隐藏假设。

**交付**：形式化规格草案与假设清单。

### Step 3｜检索已有数学资产

优先搜索 Mathlib 或领域库中的定义、定理、类型类和实例。检查 theorem signature 是否真的匹配目标，不只看名称。

**交付**：依赖定理清单、可复用/需扩展/需新证明矩阵。

### Step 4｜建立最小 Lean 项目

- 固定 Lean toolchain。
- 固定 Mathlib/第三方库 revision。
- 保存 lakefile 与 lake-manifest.json。
- 写最小可编译定义和 theorem statement。
- 运行 lake build 并保存日志。

**交付**：可复现项目骨架和环境指纹。

### Step 5｜分解证明

用 Blueprint 或简洁依赖图将主命题拆成独立 lemma。优先证明低层数学事实，再逐层组合。每个 lemma 都要说明其假设来源。

**交付**：定理依赖图、proof status、未完成义务。

### Step 6｜证明与反例

使用 tactic、Mathlib 搜索和 AI 候选证明。对每个失败目标区分定义错误、假设缺失、目标不成立、已有定理不匹配、自动化/性能问题和真实反例。不能用增加无关假设的方式掩盖反例。

### Step 7｜可信性审计

- 检查所有 theorem 是否有完整证明。
- 搜索 sorry、admit 和自定义 axioms。
- 使用 #print axioms 或项目提供的审计脚本检查依赖。
- 核对 Lean/Mathlib 版本和第三方依赖。
- 确认构建日志对应当前 commit。

### Step 8｜如果涉及实际程序，建立实现桥

优先顺序：
1. 可证明的 refinement / semantic preservation；
2. 共享规范或可验证代码生成；
3. 对受支持源代码做形式化抽取；
4. 差分测试、属性测试、边界测试作为分层补充。

若只完成第 4 项，必须标记为测试证据，而不是实现已被 Lean 证明。

### Step 9｜独立审查与归档

独立审查者需检查原始命题到 Lean statement 的翻译、假设、依赖、证明完整性、源码 commit 和复现过程。保留反例、失败日志和未解决问题。

## 最终报告必须区分的状态

- THEOREM_KERNEL_CHECKED
- STATEMENT_FIDELITY_REVIEWED
- IMPLEMENTATION_REFINEMENT_PROVEN
- PROPERTY_OR_DIFFERENTIAL_TESTED
- DATA_PROVENANCE_VERIFIED
- EMPIRICALLY_VALIDATED
- NOT_RUN / BLOCKED / UNKNOWN

这些状态不是同义词，也不能互相自动升级。
