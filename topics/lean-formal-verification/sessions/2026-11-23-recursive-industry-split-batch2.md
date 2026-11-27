# TOPIC-018｜跨行业递归下钻 Batch 2：7 父节点 → 12 具体问题 → 论文/标准 → GitHub

> 日期：2026-11-23  
> 规范任务：[AI_book #74](https://github.com/fweiger/AI_book/issues/74) · [Draft PR #75](https://github.com/fweiger/AI_book/pull/75)  
> 范围：先形成跨行业研究树，每个最小问题实际落到 GitHub 仓库；不进行项目独立 build、许可证/axiom/sorry 质量审计、最小原型或生产集成。  
> 交付文件：[递归拆分登记表 §2B](../industry-recursive-split-register.md)。

## 1. 回读与总体状态

恢复时：批准 Issue #74、唯一 Tracker 的 Writer 状态为 NONE / SYNCED；上轮 Batch1 event #7093114680 已回读；PR #75 仍是 Draft。锁定 Task Center V1.2.2 协议 commit 为 `f0e5ccb90c54265dcd07abb9a975c903eb031ccf`。用户批准 Goal/Scope/AC 未修改。

本轮从剩余的 32 个未拆父节点中选取 7 个具有明确原始来源与真实 GitHub 仓库的方向，每个具体问题通过一级行业、父节点 ID、子节点 ID 关联：

| 统计项 | 本轮前 | 本轮后 |
|---|---:|---:|
| 一级行业 | 12 | 12 |
| 首轮父节点 | 60 | 60 |
| 有子节点的父节点 | 28 | **35** |
| 仍未下钻父节点 | 32 | **25** |
| 候选子节点 | 62 | **74** |
| 本轮新增 | — | **12** |

**没有声明 74 个均为 LEAF_CLOSED**。按现阶段统一的最小节点闭合标准，仍须验证具体性质、论文—仓库对应强度、论文和项目实际研究边界。

## 2. 各行业下钻与来源证据

### IND01-01｜半导体 / RISC-V 指令语义（1）

- [opencompl/sail-riscv-lean](https://github.com/opencompl/sail-riscv-lean) README 表示其从官方 Sail RISC-V 模型生成 Lean 表示并通过类型检查；但作者也明确注明 **Lean backend 尚在开发、生成代码目前不可执行**。
- [RISC-V ISA Manual](https://github.com/riscv/riscv-isa-manual) 和 [Sail RISC-V](https://github.com/riscv/sail-riscv) 是规格及模型来源。
- **拆分重点：** 将“ISA 形式化语义生成/类型检查”独立于“OpenVM 各 opcode 电路的 soundness 证明”；后者已有 IND01-05-A，避免重复计数。
- 状态：DIRECT_LEAN_RESEARCH / STANDARD_OR_SPEC / CANDIDATE_LEAF；不把模型 typecheck 当作实现 correctness。

### IND01-04｜半导体 / GPU kernel（2）

- [facebookresearch/lean_kernel_verify](https://github.com/facebookresearch/lean_kernel_verify) README 明确采用编译器 PTX/IR → KIR → Lean 规格判定。
- [项目 specs.md](https://github.com/facebookresearch/lean_kernel_verify/blob/main/references/specs.md) 分别列出内存边界/地址回绕与 named barrier convergence、TMEM/shared-memory reuse 等安全条件。
- **拆分重点：** 内存安全与同步/资源复用两个独立目标性质；其 PASS/FAIL 仅对应给定 case input，不能声称适用于所有 shape、所有 GPU kernel 或一般 race/deadlock-freedom。
- 状态：DIRECT_LEAN_RESEARCH / PRIMARY_PROJECT_SPEC；同行评审 companion paper 本轮未找到，标 PAPER_GAP。

### IND02-03｜软件 / Datalog 推理（2）

- 原始 ITP 2025 论文：[Verifying Datalog Reasoning with Lean](https://doi.org/10.4230/LIPIcs.ITP.2025.36)（Tantow et al.），论文摘要明确指出两种 JSON 证书：proof tree 与 directed acyclic graph。
- 原始实现：[knowsys/CertifyingDatalog](https://github.com/knowsys/CertifyingDatalog) README 说明其 Lean 4 checker 验证 tree/DAG 证书。
- **拆分重点：** proof-tree correctness 与 DAG 共享子证明的证书验证分开组织；共同复用 Lean checker，不误认为证明了所有 Datalog 引擎内部实现。
- 状态：DIRECT_LEAN_RESEARCH / DIRECT_COMPANION / CANDIDATE_LEAF。

### IND07-02｜医疗信息 / FHIR（2）

- [HL7 FHIR R5 Validation](https://hl7.org/fhir/validation.html) 官方区分结构、cardinality、value sets、invariants、profile 以及应用层 business rules，并提醒没有一种校验方式能覆盖所有业务合规要求。
- [HL7 FHIR References](https://hl7.org/fhir/references.html) 是跨资源引用语义的官方规格。
- **资源结构约束：** [HL7/fhir](https://github.com/HL7/fhir) + [FHIR/fhir-test-cases](https://github.com/FHIR/fhir-test-cases)。
- **跨资源引用与业务规则：** [HL7/fhir](https://github.com/HL7/fhir) + [hapifhir/hapi-fhir](https://github.com/hapifhir/hapi-fhir)（真实 Java FHIR 系统/参考实现）。
- 两者都是 **DOMAIN_REFERENCE_IMPLEMENTATION**；本轮没有发现直接 Lean FHIR 项目，必须保留 LEAN_GAP。不把 FHIR schema 验证等同于患者数据授权或临床正确性。

### IND08-04｜通信 / 分布式协议时序性质（1）

- [verse-lab/veil](https://github.com/verse-lab/veil) README v2 介绍 FloodSet temporal 教程、模型检查与个别 temporal 证明入口。
- [Veil CAV 2025](https://doi.org/10.1007/978-3-031-98682-6_2) 是技术方法证据，**不自动成为 Veil v2 所有新增示例的 companion artifact**。
- 目标性质：在明确环境/公平性假设下的指定时序公式，不把某个例子已证明推广为协议所有 safety+liveness。
- 状态：DIRECT_LEAN_RESEARCH / RELATED_METHOD + PROJECT_DOC / CANDIDATE_LEAF。

### IND11-02｜法律与合同计算（2）

- **法律法规例外与默认逻辑：** [Catala: A Programming Language for the Law (ICFP 2021)](https://doi.org/10.1145/3473582) ↔ [CatalaLang/catala](https://github.com/CatalaLang/catala)，直接论文—工具关系。Catala 原始 [形式化说明](https://github.com/CatalaLang/catala/blob/master/doc/formalization/README.md) 使用 **F***，且文档披露一项暂时 admitted lemma。这里不能误记为 Lean 项目，也不能宣称完整 verified compiler。
- **合同字段和结构模型：** [accordproject/concerto](https://github.com/accordproject/concerto) 提供模型定义、解析及分析工具，属于合同**数据模型**，不是法律义务逻辑的完整实现。尚无可信同行评审 companion paper。
- 状态分别为 ADJACENT_FORMAL_TOOL / DIRECT_COMPANION 与 DOMAIN_REFERENCE_IMPLEMENTATION / PAPER_GAP / LEAN_GAP。

### IND12-02｜数学科研 / 数学猜想形式化（2）

- 原始研究：[Formal Conjectures, arXiv 2605.13171](https://arxiv.org/abs/2605.13171) ↔ [google-deepmind/formal-conjectures](https://github.com/google-deepmind/formal-conjectures)。
- **猜想陈述形式化：** 将开放数学问题变为 Lean 4 规格，主要是 `statement` 项目，不是已完成其证明。
- **命题翻译忠实度：** 项目原始 [STATEMENTS.md](https://github.com/google-deepmind/formal-conjectures/blob/main/STATEMENTS.md) 要求核对原文量词、隐含条件、空集/零等边界、定义解释和意外真值。它是另外一类重要的 QA 研究问题。
- 状态：DIRECT_LEAN_RESEARCH / DIRECT_COMPANION（论文与仓库）+ PROJECT_REVIEW_PROCESS；不把 README 的论文 benchmark 结论理解为所有命题均被独立证实。

## 3. 校核原则与不足

本轮专注于 **研究映射是否真实**，不评价仓库的商业价值或 Lean 工程质量。项目 README 中提到的证明/构建状态属于项目作者的证据陈述；本轮实际只读取了所列仓库的文档与公开论文/标准页面，没有运行外部仓库构建或检查关键 theorem 的证明依赖。

- PASS（来源级）：12 个新子节点均有 GitHub 仓库与原始规格、论文或项目技术资料，并按 Lean/相邻工具/行业实现类型分类。
- PARTIAL（叶节点闭合）：74 个候选节点尚未全部复核直接论文—仓库对应关系；25 个首轮父节点尚未下钻。
- NOT_RUN：外部项目源码审计、依赖/许可证/axiom/sorry/build 检查、独立原型。
- Goal drift：D0；目标仍是 Lean 可进入哪些行业、具体业务问题、哪些技术方法及对应论文/项目的知识树。

## 4. 当前未拆的 25 个父节点

`IND01-02`, `IND01-03`, `IND03-01`, `IND03-03`, `IND03-04`, `IND05-02`, `IND05-04`, `IND05-05`, `IND06-02`, `IND06-05`, `IND07-01`, `IND07-03`, `IND07-05`, `IND09-01`, `IND09-04`, `IND10-01`, `IND10-02`, `IND10-03`, `IND10-05`, `IND10-06`, `IND11-03`, `IND11-05`, `IND12-01`, `IND12-03`, `IND12-05`。

## 5. 唯一下一步

继续对这 25 个父节点逐步拆到单一业务问题与真实 GitHub 仓库，优先跨工业控制、航空交通、科学计算与医疗等尚未充分下钻的行业；对已存在的 74 个候选子节点复核论文 companion / 直接技术资料 / 相关方法关系，发现不真实的映射则纠正。**不得为增加数量而制造子节点；没有真实项目就标 PROJECT_GAP。**
