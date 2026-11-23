# TOPIC-018｜124 个第二层候选节点的证据闭合与深度复核队列（Batch 4）

> 日期：2026-11-23 · [规范 Issue #74](https://github.com/fweiger/AI_book/issues/74) · [PR #75](https://github.com/fweiger/AI_book/pull/75)  
> 输入：[当前 124 个 L2 候选表](industry-recursive-split-register.md)；新增 [16 个 L3 实例](industry-depth3-paper-project-map.md)  
> **本表是入口级 triage / 自动标签 + 定向人工资料核对，不是 124 项论文/仓库的独立真实性审计，不代表任何 L2 已全面 LEAF_CLOSED。**

## 1. Batch4 建表时的静态分母与不同统计口径（历史快照；最新进展见 1A）

| 指标 | 值 | 解释 |
|---|---:|---|
| 一级行业 | 12 | 原行业分类 |
| 初始父节点 | 60 | 60/60 至少向 L2 拆一层 |
| L2 候选研究节点 | **124** | 每条都挂一条实际 GitHub 仓库地址；是场景与项目关系数，不是项目数 |
| L2 唯一 ID | **124** | 以 Markdown 登记表逐行计算 |
| GitHub 仓库路径去重后 | **84** | 仅去除 URL 中大小写等完全一致路径；**不包含重命名/迁移/镜像/组织拆合的统一实体去重** |
| 当前有下级 L3 的 L2 父节点 | **8** | 本轮有 16 个新 L3 候选 |
| 尚未进入 L3 的 L2 节点 | **116** | 不意味着 116 个都必须再拆，需依单问题与项目闭合条件逐个判断 |
| 本轮 L3 候选 | **16** | 都有真实 GitHub URL 和论文/研究说明，仍未做外部项目构建 |

## 1A. 第三、第四层的实际进展（Batch 4–7）

- [Batch4 L3 表](industry-depth3-paper-project-map.md)：**8 个 P0 L2 → 16 个 L3**。
- [Batch5 L3/L4 代码锚点](industry-depth3-p0-source-anchors-batch5.md)：**9 个新的 P0 L2 → 27 个 L3，另外 2 个 CVaR L4 证明目标**。
- [Batch6 六个 P0 的 17 L3 源码/论文映射](industry-depth3-p0-source-anchors-batch6.md)：OpenVM、Zisk、机制设计、控制理论、信息论与 Sparkle 6 个此前未进入 L3 的 P0 L2 → 17 个 L3（源码/技术资料来源级 E1）。
- [Batch7 剩余 7 个 P0 的 21 L3 研究映射](industry-depth3-p0-source-anchors-batch7.md)：IFP、PIT 历史股票池、SciLean、LegalLean、Concerto、CGM/OpenAPS、ClimaCore 的直接 Lean 代码 / 行业源码缺口分层。
- 合计已有 **30/30 个 P0 L2 至少继续一层**；新一层共 **81 个 L3**（16+27+17+21）和 **2 个 L4**。**剩余未至少进入 L3 的 P0：0**；这仅为研究深度覆盖，不是 LEAF_CLOSED。其他 47+47 个 P1/P2 的来源关系仍未整体验收。
- `L3_MAPPING_E1` 仅证明已定位研究问题、第一手资料与代码/项目入口；并非 `LEAF_CLOSED`，不自动解除 `PAPER_GAP` 或 `LEAN_GAP`。
- **尚未继续 L3 的 P0 ID：无（30/30 均已至少细分一层）**。下一轮改为逐个核验 L3 是否足够小、源码/theorem 是否对应论文及证明状态；不可根据 P0 初次细拆就宣布研究闭合。

## 1B. Batch8：83 个登记单元 / 82 个终端叶节点的来源级闭合矩阵（当前最新）

- [全部 83 条 L3/L4 证据闭合门禁矩阵](industry-leaf-evidence-closure-matrix-batch8.md) 已生成并回读，包含 **81 个 L3 + 2 个 L4、30 个 P0 父节点、83 个唯一 ID**；其中 `IND04-03-B-02` 已细拆为两个 L4，故 **终端叶节点为 82，而不是 83**。此前的“83 项研究终端单元”必须改为“83 项登记研究单元/82 个实际终端节点”。
- 证据定位粒度：**37** 个直接 Lean 文件链接、**9** 个仓库目录、**14** 个 GitHub 仓库级链接、**10** 个技术/项目说明链接、**11** 个非 Lean 业务实现、**2** 个内部源码/示例；以上为来源类型统计，不是证明验收分数。
- 研究级别：具名 theorem 或模型说明 ≠ 独立 kernel 校验；未处理条件性 premises、作者部分完成、`sorry_proof`、显式 axiom、非 Lean 系统 LEAN_GAP。**当前 LEAF_CLOSED 未作最终判定；不得将 P0 的 30/30 下钻覆盖当成 30/30 证据闭合。**
- **唯一下一步**：根据矩阵弱源码位置，优先把 **23 个仓库/目录级入口**定位到具体文件/具名性质/论文关联并审查适用前提，按每条列出的下一证据动作判断来源级闭合或继续分拆；然后推进其余文档级缺口与 P1/P2 94 个 L2 来源关系。仍不执行无目标的外部 clean build 和原型。

## 1C. Batch9：23 个 repo/dir 弱入口已定位到原始源码（最新来源精度）

- [Batch9：23 个源文件/具名符号、论文范围及开放条件对照](industry-repo-dir-source-anchors-batch9.md) 已实际 GET 回读 **23/23**。这是对 Batch8 14 仓库级 + 9 目录级入口的**证据精度升级**；原 Batch8 `source_type` 统计仍作为历史快照保留，不能再称当前还存在 23 个未定位源码的弱链接。
- Lean-MLIR `denote_rewritePeepholeAt`、VCVio oracle/program logic、MathFin CRR、StatsMLlib 四类概率/统计定理、Brownian 项目构造/连续修改、SP1 局部 faithfulness、Resonate trace invariant、TorchLean checked lowering/CROWNQuery 和 ArkLib legacy/Hachi 均找到实际文件/声明；不等于整套框架或部署系统 correctness。
- **仍需证据**：ArkLib Sumcheck Interaction 迁移与 Hachi/Fiat-Shamir 组合、SP1 witness decode seam、Resonate 31/92、TorchLean Float/FFI/CUDA 与 Lean proof 的实现距离、Lean-MLIR 固定 ITP24 artifact 与当前 main 的差异；所有情况仍按单问题标注。**没有将任何叶节点擅自升级 LEAF_CLOSED。**
- **唯一下一步**：优先对 **10 个仍为 `PROJECT_DOC_LINK` 的 L3/L4 节点**定位相应的源码、具名性质、论文/工程边界；完成后对 83 登记单元/82 终端开展统一来源级闭合判定，再推进 P1/P2 94 个 L2。

## 1D. Batch10：10 个文档级 P0 L3 源码精确映射与证明缺口（最新）

- [Batch10 10 项 doc→source 原始代码/符号与信任边界](industry-doc-to-source-anchors-batch10.md) 已 GET 回读，分别对应 Resonate validator（1）、TorchLean CUDA/FFI（1）、Lean Kernel Verify P0/P1 规格（5）、Zisk FV Aeneas 提取/解码桥接（1）、Sparkle 仲裁器与 Signal DSL（2）。来源为真实 `.lean` 文件或具名工具/模型声明，**10/10 文件级定位 PASS ≠ 10 项完成证明**。
- 与 [Batch9 23 个 repo/dir 源码锚点](industry-repo-dir-source-anchors-batch9.md) 合并后，Batch8 建表时的 **33 个低精度索引入口**均有可回读的文件级 overlay；原 37/9/14/10/11/2 分类保留为历史快照，不应再说尚有 23 repo/dir 或 10 doc 节点等待首个文件定位。
- **重要纠偏：** Resonate 的 `valid/lean/correctness.lean` 多处 `sorry`；LKV `holdsPar_eq`、TMEM/Store 判定只是抽象 KIR/Run 模型里的 checker/spec 关系；Zisk 当前 main 存在 ProductionM2/Aeneas 提取 + opcode/decoder bridge 的具体 Lean 文件，之前“主树未接入任何桥接”的笼统说法过时，仍须把完整 root 声明前提与 Rust/Sail extraction TCB 分开；Sparkle `ArbiterProps.lean` pure FSM theorem 与 `RoundRobin.lean` Signal+Verilog 生成不能自动宣称是同一证明的实现等价。
- **唯一下一步**：在 83 登记单元/82 个终端的全量矩阵基础上，结合 Batch9+10 overlay 逐条判定**来源级** `SOURCE_LEVEL_CLOSED` 或 `REQUIRES_MORE_EVIDENCE`，记录每项的 paper↔repo 直接性与源码类型、Lean GAP/开放前提；然后再推进 P1/P2 的 94 个 L2，禁止把来源级归档说成 Lean kernel 构建验收。

## 1E. Batch11：83 个登记研究单元的来源级闭合判定（本专题最新）

- [Batch11：83 行来源级闭合判定全量矩阵](industry-leaf-source-closure-decisions-batch11.md) 已真实提交并 GET 回读：83/83 ID 唯一，**52 条 `SOURCE_LEVEL_CLOSED`、31 条 `REQUIRES_MORE_EVIDENCE`**；含一个不计终端的 CVaR L3 父项，故**82 个终端 = 52 个来源级闭合 + 30 个仍需证据**。`SOURCE_LEVEL_CLOSED` 仅说明单问题→源码/论文或技术资料的限定对应，**不是 theorem/kernel PASS 或真实系统验证**。
- 原 Batch8 的 23 个 repo/dir、10 个 doc 弱入口均已经 Batch9+10 得到可回读的 Lean 文件级 overlay。其余 11 个 non-Lean 行业参考始终保持 `LEAN_GAP`，2 个内部应用/样例单独标注。IFP/Resonate 作者报告、SciLean `sorry_proof`、LegalLean `axiom`、SP1/Zisk extraction trust、LKV GPU KIR/实机和 PIT as-of 限制不得从来源级结论升级为实际 proof。
- **当前唯一下一步（保持宽度优先）**：31 个仍需证据项保留为明确的异常/证明义务队列，必要时按真实新证据定向完善；主线转向 **P1/P2 共 94 个 L2**，以行业批次下钻到单一问题、目标性质、原论文/官方资料、实际 GitHub 项目与源码/具名定理或显式 `LEAN_GAP`。不对已来源级闭合的 52 项做无差别重复搜索，不提前进行全项目审计或原型。

## 1F. Batch12：P1/P2 首批跨12行业下钻到实际源码（本阶段最新）

- [Batch12 12 个 P1/P2 L2 → 24 个新 L3/具体 GitHub 文件](industry-depth3-p1p2-source-map-batch12.md) 已实际提交并GET回读：12个父节点（P1 4 + P2 8）对应IND01–IND12全部12个一级行业，每个L2两个具名性质/项目节点，24个唯一L3；原124 L2表的12个父行已反向链接。
- **累计树**：原P0 30个L2/81L3+2L4=83登记（82终端）；新24 L3后**105 L3+2L4=107登记、106终端**。已细拆到L3的L2父节点 **42/124 = P0 30 + P1/P2 12**；P1/P2 仍有 **82 个未进入第三层（P1剩43、P2剩39）**。
- **范围/来源差异**：Cedar/CompPoly/LeanLTL/RateDistortion/AQFT存在实际Lean4源文件和定理/定义；Sail→Lean生成代码的type-check非实现精化；Langmuir/BET是历史Lean3论文伴随项目；Catala用F*而非Lean；libSBML为C++行业参考；FormalConjectures还有`sorry`；LeanCopilot tactic建议不是证明。SocialChoiceLean Pivato定理不可直接与原登记中的EconCSLib论文做错配。
- **唯一下一步**：继续其他未展开的P1/P2 L2，优先第二批跨行业不同子领域12个父节点，按“单问题/性质→一手文献→真实GitHub文件/具名定理或LEAN_GAP”下钻，保持P0 31条未闭合异常为有界队列。**24条仅SOURCE_MAPPED_WITH_SCOPE，不叫LEAF_CLOSED或已独立构建**。

## 1G. Batch13：第二批P1/P2跨12行业真实源码下钻（2026-11-24）

- [Batch13：12个不重复P1/P2父节点→24个新L3，精确文件/性质/论文关系](industry-depth3-p1p2-source-map-batch13.md) 已实际提交和GET回读，横跨IND01–IND12的不同子领域，P1=4/P2=8。原124 L2主表与本队列各12个原父行已建立Batch13反向链接。
- **最新树分母**：12行业/60初始父/124 L2（P0=30/P1=47/P2=47）不变；Batch11的P0 81L3+2L4、Batch12增24L3、Batch13再增24L3，累计 **129 L3+2 L4=131登记单元**；旧CVaR父L3不算终端，故**130终端**。具第三层的L2 **54/124 = P0 30 + P1/P2 24**；P1还39、P2还31，即**70个未下钻**。
- **来源类型和重要缺口**：CertifyingDatalog有Lean proof-tree与DAG checker theorem；Aeneas FRI fold_step局部 theorem 与ArkLib `sorry`分别保留；Sparkle AXI4-Lite FSM proof与Signal实现精化未闭；Matheconlib/Lean DynamicalSystems有具名定理；KeYmaera X是Scala/dL、ESBMC-PLC+是SMT/BMC、VerifiableP4是Coq、alpha-beta-CROWN是Python数值算法、ElectionGuard验证器是Rust、FHIR是HL7标准XML、leanblueprint是Python依赖图工具。非Lean必须明确保留`LEAN_GAP`，不能被项目声称formal verification而误标成Lean proof。
- **唯一下一步**：从剩余 **70个P1/P2 L2** 再选第三批约12个此前未下钻的父节点，以相同“具体问题→目标性质→原论文/标准/项目资料→GitHub源码→开放边界”路径继续扩展；P0 Batch11的31条证据缺口保持有界队列。新增24项`SOURCE_MAPPED_WITH_SCOPE`，**不是`LEAF_CLOSED`或`LEAN_BUILD_PASS`**，没有独立运行外部build。

## 1H. Batch14：P1/P2第三批跨12行业下钻与不可信公理识别（2026-11-24）

- [Batch14：12个全新P1/P2父节点→24个L3具名文件/性质/论文关系](industry-depth3-p1p2-source-map-batch14.md) 已实际提交/GET回读，IND01–IND12各选一父（P1=6/P2=6），与Batch12/13的24父不重复，原124个L2登记和本triage各有12个Batch14反向链接。
- **累计分母**：原12一级行业/60初始父/124 L2（P0 30、P1 47、P2 47）不变。已第三层父节点 **66/124** = P0 30 + P1 14 + P2 22；还有 **P1 33 + P2 25 =58** 未展开。累计 **153 L3 +2 L4=155登记单元**，原CVaR父L3不算终端，故**154真实终端**。新24项SOURCE_MAPPED_WITH_SCOPE、外部proof未独立build。
- **本轮必要的证据披露**：Lean-MLIR中`PeepholeRefine.lean`存在`axiom refinement_correctness {p:Prop}:p`以及`toPeepholeUNSOUND`，明确**UNSOUND_AXIOM_GAP**，不能用其他Lean代码掩盖；xv6iris top theorem有初始态和磁盘假设；OpenVM SHA256定理只限压缩桥接；Markowitz/LeanInfoTheory/Physlib量子信息定理有模型前提。SUMO、pandapower、Biopython、OCDS均是非Lean实现/规范，LeanDojo v2和GameServer只是证明系统工具；OCDS主树`1.2-dev`含1.1.5 schema ID版本错位必须pin。
- **唯一下一步**：继续P1/P2剩余58个父节点的第四批跨行业论文→源码/定理研究下钻，优先前几批未覆盖的子领域及一手研究证据，注意上述高风险缺口保留有界队列，不转为无期限全仓审计。

## 2. 关键词证据缺口基线（存在重叠，非最终人工判定）

| 关键词/类型 | L2 命中数量 | 该信号的含义 |
|---|---:|---|
| CONTINUE_SPLIT | 8 | 已明确指向 L3 细分研究 |
| LEAN_GAP | 20 | 当前仅有相邻形式化工具/行业参考实现，缺少直接 Lean 业务代码证据 |
| PAPER_GAP | 12 | 缺少足够直接的学术论文，可能有作者技术报告或项目 README |
| CROSS_DOMAIN_REUSE | 6 | 同一真实项目在不同行业节点复用，不可计算成多个独立仓库 |
| RELATED_METHOD | 30 | 论文不一定是所列仓库的 companion artifact |
| DIRECT_COMPANION（候选） | 33 | 表中已有直接配套关系标记，但仍需逐项确认论文研究范围 |
| PROJECT_DOC_ONLY | 7 | 尚以项目文档为研究证据来源 |
| PROJECT_LINEAGE/SUCCESSOR | 4 | 旧仓库与新整合库/迁移链需区分 |

此表的所有数量只从**当前记录文本**匹配关键词生成，不能用“124−20−12”计算已确认无缺口比例；标签多重重叠，尚未标记的节点也可能有漏项。

### 按研究缺口优先级分流

- `P0 = 30`：已确认继续拆分、直接论文缺口、项目缺口、或本轮定向判定过宽的节点，优先在对应父节点继续研究。
- `P1 = 47`：Lean 适配空白、相关方法但非直接 companion、跨行业复用、项目血缘/原始技术说明等需要补证。
- `P2 = 47`：已有直接或间接研究与 GitHub 链接，仍需抽查数学对象与对应关系；**不是关闭/验收通过**。

## 3. 全部 124 个 L2 候选的映射闭合工作队列

| L2 ID | 当前问题（摘要） | 主要 GitHub 仓库（按表中首次出现） | 优先级 | 需复核的关系 / 风险 |
|---|---|---|---|---|
| `IND01-05-A` | OpenVM v2.0.0 的 RV32IM opcode 语义是否满足指令规格 | [openvm-org/openvm-fv](https://github.com/openvm-org/openvm-fv) | P0 | PAPER_GAP · **L3_MAPPING_E1 Batch6 ×3** |
| `IND01-05-B` | SP1 Hypercube chip 的逐行约束是否忠实于参考语义 | [succinctlabs/sp1-lean](https://github.com/succinctlabs/sp1-lean) | P0 | PAPER_GAP · **细拆候选** · **L3_MAPPING_E1 Batch5 ×4** |
| `IND01-05-C` | Zisk RV64IM 相关组件的 Lean 形式化 | [eth-act/zisk-fv](https://github.com/eth-act/zisk-fv) | P0 | PAPER_GAP, PROJECT_DOC_ONLY · **L3_MAPPING_E1 Batch6 ×3** |
| `IND02-02-A` | 将受限 Rust 函数语义抽取为 Lean 函数并证明规格 | [AeneasVerif/aeneas](https://github.com/AeneasVerif/aeneas) | P2 |  |
| `IND02-02-B` | Rust 源码到 Lean/F*/Rocq 的翻译与证明边界 | [pereq-dev/hax](https://github.com/pereq-dev/hax) | P1 | RELATED_METHOD |
| `IND02-04-A` | 分布式软件状态机的 LTL 安全性与活性 | [UCSCFormalMethods/LeanLTL](https://github.com/UCSCFormalMethods/LeanLTL) | P2 | DIRECT_COMPANION_CANDIDATE |
| `IND02-04-B` | 异步工作流的状态迁移、幂等性与故障恢复 | [resonatehq/resonate-specification](https://github.com/resonatehq/resonate-specification) | P0 | PAPER_GAP · **L3_MAPPING_E1 Batch5 ×3** |
| `IND03-02-A` | 有限域多项式运算和可计算多项式基础 | [Verified-zkEVM/CompPoly](https://github.com/Verified-zkEVM/CompPoly) | P1 | RELATED_METHOD · **Batch12 L3 ×2：源码级映射** · [证据](industry-depth3-p1p2-source-map-batch12.md) |
| `IND03-02-B` | IOR/SNARK 证明系统的组合结构与验证关系 | [Verified-zkEVM/ArkLib](https://github.com/Verified-zkEVM/ArkLib) | P0 | RELATED_METHOD · **细拆候选** · **L3_MAPPING_E1 Batch5 ×3** |
| `IND03-02-C` | 游戏式密码学安全证明与归约 | [Verified-zkEVM/VCVio](https://github.com/Verified-zkEVM/VCVio) | P2 | DIRECT_COMPANION_CANDIDATE |
| `IND03-05-A` | Veil 中 BFT 协议的 transition-system 不变量 | [verse-lab/veil](https://github.com/verse-lab/veil) | P0 | DIRECT_COMPANION_CANDIDATE · **细拆候选** · **L3_MAPPING_E1 Batch5 ×3** |
| `IND03-05-B` | IFP 中协议状态与故障假设的验证对象 | [sarvalabs/ifp](https://github.com/sarvalabs/ifp) | P0 | PAPER_GAP, PROJECT_DOC_ONLY · **L3_MAPPING_E1 Batch7 ×3** |
| `IND04-01-A` | Brownian motion 的定义、滤过与路径性质 | [RemyDegenne/brownian-motion](https://github.com/RemyDegenne/brownian-motion) | P0 | CONTINUE_SPLIT, DIRECT_COMPANION_CANDIDATE |
| `IND04-01-B` | SDE/随机积分的定义与基础定理 | [formal-applied-math/formal-mathfin](https://github.com/formal-applied-math/formal-mathfin) | P2 |  |
| `IND04-02-A` | CRR 二叉树定价递推和无套利条件 | [formal-applied-math/formal-mathfin](https://github.com/formal-applied-math/formal-mathfin) | P0 | CONTINUE_SPLIT, RELATED_METHOD |
| `IND04-02-B` | Black–Scholes 连续时间定价公式的假设与推导 | [formal-applied-math/formal-mathfin](https://github.com/formal-applied-math/formal-mathfin) | P1 | RELATED_METHOD |
| `IND04-03-A` | Markowitz 均值—方差模型的可行域与最优性条件 | [formal-applied-math/formal-mathfin](https://github.com/formal-applied-math/formal-mathfin) | P1 | RELATED_METHOD · **Batch14 L3×2：论文/源码及可信边界** · [证据](industry-depth3-p1p2-source-map-batch14.md) |
| `IND04-03-B` | CVaR 的定义、凸表示与优化等价关系 | [formal-applied-math/formal-mathfin](https://github.com/formal-applied-math/formal-mathfin) | P0 | RELATED_METHOD · **细拆候选** · **L3_MAPPING_E1 Batch5 ×4** |
| `IND04-04-A` | 单条数据是否在决策时点可见：availableAt ≤ decisionTime | [fweiger/AI_book](https://github.com/fweiger/AI_book) | P1 | RELATED_METHOD |
| `IND04-04-B` | 历史股票池成员、成分调整与历史修订是否按当时可得版本回放 | [fweiger/AI_Trader](https://github.com/fweiger/AI_Trader) | P0 | RELATED_METHOD · **细拆候选** · **L3_MAPPING_E1 Batch7 ×3** |
| `IND04-05-A` | 投票规则的公平性、公理与反例 | [dominikpeters/SocialChoiceLean](https://github.com/dominikpeters/SocialChoiceLean) | P1 | RELATED_METHOD · **Batch12 L3 ×2：源码级映射** · [证据](industry-depth3-p1p2-source-map-batch12.md) |
| `IND04-05-B` | 拍卖规则的激励相容、个体理性与分配性质 | [gametheoryinlean/EconCSLib](https://github.com/gametheoryinlean/EconCSLib) | P0 | RELATED_METHOD, DIRECT_COMPANION_CANDIDATE · **细拆候选** · **L3_MAPPING_E1 Batch6 ×3** |
| `IND04-05-C` | 均衡存在性与机制约束下的经济结论 | [matheconlib/matheconlib](https://github.com/matheconlib/matheconlib) | P1 | RELATED_METHOD · **Batch13 L3×2：源码/论文/形式化语言分类** · [证据](industry-depth3-p1p2-source-map-batch13.md) |
| `IND05-01-A` | 两条进路是否冲突、锁闭和释放条件是否安全 | [egrabanica/safe-railway-system-promela](https://github.com/egrabanica/safe-railway-system-promela) | P1 | RELATED_METHOD |
| `IND05-01-B` | ETCS 状态与通信消息顺序是否允许非法状态 | [apalache-mc/apalache](https://github.com/apalache-mc/apalache) | P1 | RELATED_METHOD |
| `IND05-03-A` | 神经网络反馈控制器闭环可达集是否越过安全边界 | [neu-autonomy/nfl_veripy](https://github.com/neu-autonomy/nfl_veripy) | P1 | RELATED_METHOD |
| `IND05-03-B` | 连续/混合车辆控制器是否保持安全不变量 | [LS-Lab/KeYmaeraX-release](https://github.com/LS-Lab/KeYmaeraX-release) | P1 | RELATED_METHOD · **Batch13 L3×2：源码/论文/形式化语言分类** · [证据](industry-depth3-p1p2-source-map-batch13.md) |
| `IND06-01-A` | IEC 61131-3 PLC 逻辑的扫描周期、计时器和安全属性 | [IS2Lab/esbmc-plcplus](https://github.com/IS2Lab/esbmc-plcplus) | P2 | DIRECT_COMPANION_CANDIDATE · **Batch13 L3×2：源码/论文/形式化语言分类** · [证据](industry-depth3-p1p2-source-map-batch13.md) |
| `IND06-01-B` | PLC 运行时/参考实现对 IEC 61131-3 程序的执行语义 | [thiagoralves/OpenPLC_v3](https://github.com/thiagoralves/OpenPLC_v3) | P1 | RELATED_METHOD |
| `IND06-03-A` | 任务级机械臂动作序列与抓取/放置规划 | [moveit/moveit_task_constructor](https://github.com/moveit/moveit_task_constructor) | P2 | DIRECT_COMPANION_CANDIDATE |
| `IND06-03-B` | 机器人动力系统的稳定性与控制约束 | [AnandGokhale/LeanForControl](https://github.com/AnandGokhale/LeanForControl) | P0 | RELATED_METHOD, DIRECT_COMPANION_CANDIDATE · **细拆候选** · **L3_MAPPING_E1 Batch6 ×3** |
| `IND06-04-A` | 潮流计算与节点电压/线路约束 | [e2nIEE/pandapower](https://github.com/e2nIEE/pandapower) | P2 | DIRECT_COMPANION_CANDIDATE · **Batch14 L3×2：论文/源码及可信边界** · [证据](industry-depth3-p1p2-source-map-batch14.md) |
| `IND06-04-B` | 电网操作中的序贯动作、拓扑切换与安全状态 | [Grid2op/Grid2Op](https://github.com/Grid2op/Grid2Op) | P2 | E1_SCOPE_CHECK |
| `IND07-04-A` | SBML 模型结构、引用、单位与模型交换的一致性 | [sbmlteam/libsbml](https://github.com/sbmlteam/libsbml) | P1 | RELATED_METHOD · **Batch12 L3 ×2：源码级映射** · [证据](industry-depth3-p1p2-source-map-batch12.md) |
| `IND07-04-B` | 生化反应网络 ODE 模型的仿真语义与复现 | [sys-bio/tellurium](https://github.com/sys-bio/tellurium) | P1 | RELATED_METHOD |
| `IND08-01-A` | Shannon entropy 与 KL divergence 的定义和基本不等式 | [serhatemrecoban/LeanInfoTheory](https://github.com/serhatemrecoban/LeanInfoTheory) | P0 | PAPER_GAP · **L3_MAPPING_E1 Batch6 ×3** |
| `IND08-01-B` | Mutual information 与数据处理不等式 | [matteonerini/infotheorylib](https://github.com/matteonerini/infotheorylib) | P1 | RELATED_METHOD, PROJECT_DOC_ONLY |
| `IND08-02-A` | 率失真函数、失真下界与最优编码率 | [fubinyan/rate_distortion_lean4](https://github.com/fubinyan/rate_distortion_lean4) | P2 | DIRECT_COMPANION_CANDIDATE · **Batch12 L3 ×2：源码级映射** · [证据](industry-depth3-p1p2-source-map-batch12.md) |
| `IND08-02-B` | 信源/信道编码定理的概率与信息量度基础 | [serhatemrecoban/LeanInfoTheory](https://github.com/serhatemrecoban/LeanInfoTheory) | P1 | RELATED_METHOD · **Batch14 L3×2：论文/源码及可信边界** · [证据](industry-depth3-p1p2-source-map-batch14.md) |
| `IND08-03-A` | Stateful P4 packet processing 的状态语义和多包性质 | [verified-network-toolchain/VerifiableP4](https://github.com/verified-network-toolchain/VerifiableP4) | P2 | DIRECT_COMPANION_CANDIDATE · **Batch13 L3×2：源码/论文/形式化语言分类** · [证据](industry-depth3-p1p2-source-map-batch13.md) |
| `IND08-03-B` | P4 编译器前端与 IR 变换是否保持程序行为 | [p4lang/p4c](https://github.com/p4lang/p4c) | P1 | RELATED_METHOD |
| `IND09-03-A` | Star-set reachability 对神经网络输出集合的过近似 | [V2A2/StarV](https://github.com/V2A2/StarV) | P2 | DIRECT_COMPANION_CANDIDATE |
| `IND09-03-B` | ReLU 网络在输入约束下是否违反安全性质 | [NeuralNetworkVerification/Marabou](https://github.com/NeuralNetworkVerification/Marabou) | P2 | DIRECT_COMPANION_CANDIDATE |
| `IND09-03-C` | Branch-and-bound 神经网络验证的界传播与剪枝正确性 | [Verified-Intelligence/alpha-beta-CROWN](https://github.com/Verified-Intelligence/alpha-beta-CROWN) | P2 | DIRECT_COMPANION_CANDIDATE · **Batch13 L3×2：源码/论文/形式化语言分类** · [证据](industry-depth3-p1p2-source-map-batch13.md) |
| `IND09-05-A` | 检索增强的 theorem/lemma 检索与 premise selection | [lean-dojo/LeanDojo](https://github.com/lean-dojo/LeanDojo) | P2 | DIRECT_COMPANION_CANDIDATE · **Batch14 L3×2：论文/源码及可信边界** · [证据](industry-depth3-p1p2-source-map-batch14.md) |
| `IND09-05-B` | 根据当前 proof state 推荐 tactic 并保持 Kernel 检查 | [lean-dojo/LeanCopilot](https://github.com/lean-dojo/LeanCopilot) | P2 | DIRECT_COMPANION_CANDIDATE · **Batch12 L3 ×2：源码级映射** · [证据](industry-depth3-p1p2-source-map-batch12.md) |
| `IND10-04-A` | ODE/PDE 与数值算法中的定义、误差与可计算性 | [lecopivo/SciLean](https://github.com/lecopivo/SciLean) | P0 | PAPER_GAP, RELATED_METHOD · **细拆候选** · **L3_MAPPING_E1 Batch7 ×3** |
| `IND10-04-B` | 动力系统不变量、稳定性与长期行为 | [mcdoll/DynamicalSystems](https://github.com/mcdoll/DynamicalSystems) | P1 | RELATED_METHOD · **Batch13 L3×2：源码/论文/形式化语言分类** · [证据](industry-depth3-p1p2-source-map-batch13.md) |
| `IND10-04-C` | Lyapunov/小增益等控制稳定性定理 | [AnandGokhale/LeanForControl](https://github.com/AnandGokhale/LeanForControl) | P2 | DIRECT_COMPANION_CANDIDATE |
| `IND11-01-A` | 法律规则、例外、资格判定的形式化表达 | [edu-ap/legal-lean](https://github.com/edu-ap/legal-lean) | P0 | PAPER_GAP, PROJECT_DOC_ONLY · **L3_MAPPING_E1 Batch7 ×3** |
| `IND11-01-B` | 将法规/税法条款表达为可执行且可审查的程序 | [CatalaLang/catala](https://github.com/CatalaLang/catala) | P2 | DIRECT_COMPANION_CANDIDATE · **Batch12 L3 ×2：源码级映射** · [证据](industry-depth3-p1p2-source-map-batch12.md) |
| `IND11-04-A` | 加密选票、零知识证明与可验证计票 | [Election-Tech-Initiative/electionguard](https://github.com/Election-Tech-Initiative/electionguard) | P2 | DIRECT_COMPANION_CANDIDATE · **Batch13 L3×2：源码/论文/形式化语言分类** · [证据](industry-depth3-p1p2-source-map-batch13.md) |
| `IND11-04-B` | 投票规则的公平性公理和社会选择性质 | [dominikpeters/SocialChoiceLean](https://github.com/dominikpeters/SocialChoiceLean) | P1 | RELATED_METHOD |
| `IND12-04-A` | 通过检索找到相关 theorem/premise 并构造证明上下文 | [lean-dojo/LeanDojo](https://github.com/lean-dojo/LeanDojo) | P2 | DIRECT_COMPANION_CANDIDATE |
| `IND12-04-B` | 从当前 proof state 推荐 tactic 并生成候选证明步骤 | [lean-dojo/LeanCopilot](https://github.com/lean-dojo/LeanCopilot) | P2 | DIRECT_COMPANION_CANDIDATE |
| `IND02-01-A` | Cedar 策略语言的授权决策语义和关键性质是否可形式化证明 | [cedar-policy/cedar-spec](https://github.com/cedar-policy/cedar-spec) | P2 |  · **Batch12 L3 ×2：源码级映射** · [证据](industry-depth3-p1p2-source-map-batch12.md) |
| `IND02-01-B` | Rust 生产授权引擎与 Lean 参考规格如何发现行为不一致 | [cedar-policy/cedar-spec](https://github.com/cedar-policy/cedar-spec) | P2 |  |
| `IND02-05-A` | xv6-riscv 内核及设备/断电模型下系统是否会 stuck，输出 trace 是否满足给定规格 | [mit-pdos/xv6iris](https://github.com/mit-pdos/xv6iris) | P2 | DIRECT_COMPANION_CANDIDATE · **Batch14 L3×2：论文/源码及可信边界** · [证据](industry-depth3-p1p2-source-map-batch14.md) |
| `IND02-05-B` | xv6 用户态指令执行和分离逻辑资源规格如何连接 | [mit-pdos/xv6iris](https://github.com/mit-pdos/xv6iris) | P2 | DIRECT_COMPANION_CANDIDATE |
| `IND09-02-A` | 张量形状约束与线性代数运算如何在 Lean 中表达 | [lean-dojo/TorchLean](https://github.com/lean-dojo/TorchLean) | P1 | RELATED_METHOD |
| `IND09-02-B` | 模型计算图重写是否保持语义，证书/证明如何验证 | [lean-dojo/TorchLean](https://github.com/lean-dojo/TorchLean) | P0 | CONTINUE_SPLIT, RELATED_METHOD |
| `IND09-02-C` | CPU/CUDA 训练路径共享的算子定义与 autograd tape 对应关系 | [lean-dojo/TorchLean](https://github.com/lean-dojo/TorchLean) | P0 |  · **细拆候选** · **L3_MAPPING_E1 Batch5 ×3** |
| `IND01-01-A` | 如何把 Sail RISC-V ISA 规范转换为 Lean 可类型检查的形式化指令语义 | [opencompl/sail-riscv-lean](https://github.com/opencompl/sail-riscv-lean) | P2 |  · **Batch12 L3 ×2：源码级映射** · [证据](industry-depth3-p1p2-source-map-batch12.md) |
| `IND01-04-A` | Blackwell TLX/Triton/CuTe GPU kernel 在**给定案例输入**下有无越界/地址回绕 | [facebookresearch/lean_kernel_verify](https://github.com/facebookresearch/lean_kernel_verify) | P0 | PAPER_GAP · **L3_MAPPING_E1 Batch5 ×2** |
| `IND01-04-B` | 给定 kernel 编译变体中 barrier/TMEM 或 shared-memory 复用次序是否违反指定安全规 | [facebookresearch/lean_kernel_verify](https://github.com/facebookresearch/lean_kernel_verify) | P0 | PAPER_GAP · **L3_MAPPING_E1 Batch5 ×3** |
| `IND02-03-A` | 对 Datalog 推导结果提供 proof-tree 证书并以 Lean 验证其语义正确性 | [knowsys/CertifyingDatalog](https://github.com/knowsys/CertifyingDatalog) | P2 | DIRECT_COMPANION_CANDIDATE · **Batch13 L3×2：源码/论文/形式化语言分类** · [证据](industry-depth3-p1p2-source-map-batch13.md) |
| `IND02-03-B` | 对共享子推导的 DAG 证书进行验证，以降低重复 proof-tree 编码 | [knowsys/CertifyingDatalog](https://github.com/knowsys/CertifyingDatalog) | P2 | DIRECT_COMPANION_CANDIDATE |
| `IND07-02-A` | 医疗记录 FHIR Resource/Profile 的结构、必填字段和 cardinality 是否符合指定版本标 | [HL7/fhir](https://github.com/HL7/fhir) | P1 | LEAN_GAP · **Batch13 L3×2：源码/论文/形式化语言分类** · [证据](industry-depth3-p1p2-source-map-batch13.md) |
| `IND07-02-B` | FHIR 跨资源引用、患者归属及业务权限能否在实际服务器工作流中满足业务约束 | [hapifhir/hapi-fhir](https://github.com/hapifhir/hapi-fhir) | P1 | LEAN_GAP |
| `IND08-04-A` | FloodSet 一类协议在状态迁移下的指定时序性质如何表达、模型检查与证明 | [verse-lab/veil](https://github.com/verse-lab/veil) | P1 | RELATED_METHOD |
| `IND11-02-A` | 如何将含例外和默认规则的税收/社保法条变成可执行且可审查的规则 | [CatalaLang/catala](https://github.com/CatalaLang/catala) | P2 | DIRECT_COMPANION_CANDIDATE |
| `IND11-02-B` | 结构化合同模型与条款数据的字段、类型、引用关系如何定义与校验 | [accordproject/concerto](https://github.com/accordproject/concerto) | P0 | LEAN_GAP, PAPER_GAP, PROJECT_DOC_ONLY · **L3_MAPPING_E1 Batch7 ×3** |
| `IND12-02-A` | 将尚未解决的科研数学猜想转换为 Lean 4 可检查的精确**命题陈述** | [google-deepmind/formal-conjectures](https://github.com/google-deepmind/formal-conjectures) | P2 | DIRECT_COMPANION_CANDIDATE · **Batch12 L3 ×2：源码级映射** · [证据](industry-depth3-p1p2-source-map-batch12.md) |
| `IND12-02-B` | 已翻译 Lean 命题是否忠实原始论文中的量词、边界值、条件与反例语义 | [google-deepmind/formal-conjectures](https://github.com/google-deepmind/formal-conjectures) | P2 |  |
| `IND01-02-A` | Lean 4 组合电路规格→Signal DSL→Verilog 生成 | [Verilean/sparkle](https://github.com/Verilean/sparkle) | P0 | PAPER_GAP, PROJECT_DOC_ONLY · **L3_MAPPING_E1 Batch6 ×2** |
| `IND01-02-B` | 时序仲裁器/AXI4-Lite 总线状态约束 | [Verilean/sparkle](https://github.com/Verilean/sparkle) | P2 |  · **Batch13 L3×2：源码/论文/形式化语言分类** · [证据](industry-depth3-p1p2-source-map-batch13.md) |
| `IND01-03-A` | MLIR SSA peephole 重写语义保持 | [opencompl/lean-mlir](https://github.com/opencompl/lean-mlir) | P0 | CONTINUE_SPLIT, DIRECT_COMPANION_CANDIDATE |
| `IND01-03-B` | LLVM IR→RISC-V 指令选择的精化 | [opencompl/lean-mlir](https://github.com/opencompl/lean-mlir) | P2 |  · **Batch14 L3×2：论文/源码及可信边界** · [证据](industry-depth3-p1p2-source-map-batch14.md) |
| `IND03-01-A` | 概率/oracle 密码安全游戏的精确定义 | [Verified-zkEVM/VCVio](https://github.com/Verified-zkEVM/VCVio) | P0 | CONTINUE_SPLIT |
| `IND03-01-B` | game hopping/归约与 oracle-handler 关系逻辑 | [Verified-zkEVM/VCVio](https://github.com/Verified-zkEVM/VCVio) | P0 | CONTINUE_SPLIT |
| `IND03-03-A` | zkVM SHA-256 precompile 的 AIR soundness | [openvm-org/openvm-fv](https://github.com/openvm-org/openvm-fv) | P2 |  · **Batch14 L3×2：论文/源码及可信边界** · [证据](industry-depth3-p1p2-source-map-batch14.md) |
| `IND03-03-B` | ZisK RV64IM trace 的 Sail ISA 符合性 | [eth-act/zisk-fv](https://github.com/eth-act/zisk-fv) | P2 |  |
| `IND05-04-A` | 飞控相关 ODE/线性系统稳定性数学基础 | [AnandGokhale/LeanForControl](https://github.com/AnandGokhale/LeanForControl) | P2 |  |
| `IND05-04-B` | 飞控离散模式与连续动力学混合安全包线 | [LS-Lab/KeYmaeraX-release](https://github.com/LS-Lab/KeYmaeraX-release) | P1 | LEAN_GAP |
| `IND05-05-A` | 城市交通路网/信号相位微观仿真 | [eclipse-sumo/sumo](https://github.com/eclipse-sumo/sumo) | P1 | LEAN_GAP · **Batch14 L3×2：论文/源码及可信边界** · [证据](industry-depth3-p1p2-source-map-batch14.md) |
| `IND05-05-B` | 双交通灯信号的安全时序性质形式化 | [UCSCFormalMethods/LeanLTL](https://github.com/UCSCFormalMethods/LeanLTL) | P1 | RELATED_METHOD · **Batch12 L3 ×2：源码级映射** · [证据](industry-depth3-p1p2-source-map-batch12.md) |
| `IND06-02-A` | 工业离散控制的层级状态机与事件顺序 | [Modelica/ModelicaStandardLibrary](https://github.com/Modelica/ModelicaStandardLibrary) | P1 | LEAN_GAP |
| `IND06-02-B` | CPS Modelica/FMI 联合仿真与控制接口 | [OpenModelica/OpenModelica](https://github.com/OpenModelica/OpenModelica) | P1 | LEAN_GAP |
| `IND06-05-A` | 热工/化工装置流体与热模型的 ODE 仿真 | [OpenModelica/OpenModelica](https://github.com/OpenModelica/OpenModelica) | P1 | LEAN_GAP |
| `IND06-05-B` | 化工吸附 Langmuir/BET 公式推导证明 | [atomslab/LeanChemicalTheories](https://github.com/atomslab/LeanChemicalTheories) | P2 | DIRECT_COMPANION_CANDIDATE · **Batch12 L3 ×2：源码级映射** · [证据](industry-depth3-p1p2-source-map-batch12.md) |
| `IND07-03-A` | 开源 AID 系统胰岛素在体量 IOB 计算口径 | [openaps/oref0](https://github.com/openaps/oref0) | P1 | LEAN_GAP |
| `IND07-03-B` | CGM 时效/预测/剂量约束的控制状态建模 | [openaps/oref0](https://github.com/openaps/oref0) | P0 | LEAN_GAP · **细拆候选** · **L3_MAPPING_E1 Batch7 ×3** |
| `IND09-01-A` | 统计学习 Gaussian Lipschitz concentration 定理 | [YuanheZ/lean-stat-learning-theory](https://github.com/YuanheZ/lean-stat-learning-theory) | P0 | CONTINUE_SPLIT, DIRECT_COMPANION_CANDIDATE, PROJECT_LINEAGE |
| `IND09-01-B` | localized least-squares 泛化/最优统计率界 | [YuanheZ/lean-stat-learning-theory](https://github.com/YuanheZ/lean-stat-learning-theory) | P0 | CONTINUE_SPLIT, DIRECT_COMPANION_CANDIDATE, PROJECT_LINEAGE |
| `IND10-02-A` | Haag–Kastler AQFT 公理化局部可观测量 | [physicslib/physicslib4](https://github.com/physicslib/physicslib4) | P2 |  · **Batch12 L3 ×2：源码级映射** · [证据](industry-depth3-p1p2-source-map-batch12.md) |
| `IND10-02-B` | GNS/谱理论/Stone 定理在 Lean QFT 库中的复用 | [physicslib/physicslib4](https://github.com/physicslib/physicslib4) | P2 |  |
| `IND10-03-A` | 量子态/信道的 Lean 数学表示 | [leanprover-community/physlib](https://github.com/leanprover-community/physlib) | P1 | PROJECT_LINEAGE |
| `IND10-03-B` | 量子熵/信息容量等式与界的条件 | [leanprover-community/physlib](https://github.com/leanprover-community/physlib) | P2 |  · **Batch14 L3×2：论文/源码及可信边界** · [证据](industry-depth3-p1p2-source-map-batch14.md) |
| `IND10-05-A` | 单层 Langmuir 吸附模型形式化 | [atomslab/LeanChemicalTheories](https://github.com/atomslab/LeanChemicalTheories) | P2 | DIRECT_COMPANION_CANDIDATE |
| `IND10-05-B` | 多层 BET 吸附模型形式化 | [atomslab/LeanChemicalTheories](https://github.com/atomslab/LeanChemicalTheories) | P2 | DIRECT_COMPANION_CANDIDATE |
| `IND10-06-A` | 气候动力核网格/PDE 离散与数值守恒候选性质 | [CliMA/ClimaCore.jl](https://github.com/CliMA/ClimaCore.jl) | P0 | LEAN_GAP · **细拆候选** · **L3_MAPPING_E1 Batch7 ×3** |
| `IND10-06-B` | 全球大气求解/微物理/对流参数化模型 | [CliMA/ClimaAtmos.jl](https://github.com/CliMA/ClimaAtmos.jl) | P1 | LEAN_GAP |
| `IND12-01-A` | Natural Number Game 互动自然数证明练习 | [leanprover-community/NNG4](https://github.com/leanprover-community/NNG4) | P2 |  |
| `IND12-01-B` | Lean Game Server 关卡及证明检查流程 | [leanprover-community/lean4game](https://github.com/leanprover-community/lean4game) | P1 | PROJECT_DOC_ONLY · **Batch14 L3×2：论文/源码及可信边界** · [证据](industry-depth3-p1p2-source-map-batch14.md) |
| `IND12-03-A` | Lean Blueprint 数学定理依赖可视化 | [PatrickMassot/leanblueprint](https://github.com/PatrickMassot/leanblueprint) | P2 | E1_SCOPE_CHECK · **Batch13 L3×2：源码/论文/形式化语言分类** · [证据](industry-depth3-p1p2-source-map-batch13.md) |
| `IND12-03-B` | Blueprint 文档与 Lean 代码声明同步核对 | [PatrickMassot/leanblueprint](https://github.com/PatrickMassot/leanblueprint) | P2 | E1_SCOPE_CHECK |
| `IND03-04-A` | Rust MIR/LLBC 翻译为 Lean 可验证纯函数的工具链 | [AeneasVerif/aeneas](https://github.com/AeneasVerif/aeneas) | P2 |  |
| `IND03-04-B` | Rust FRI folding 核心算法经 Aeneas/Hax 两条路径形式化 | [Verified-zkEVM/rust-lean](https://github.com/Verified-zkEVM/rust-lean) | P2 |  · **Batch13 L3×2：源码/论文/形式化语言分类** · [证据](industry-depth3-p1p2-source-map-batch13.md) |
| `IND05-02-A` | 简化铁路双轨信号系统的区段互斥 | [egrabanica/safe-railway-system-promela](https://github.com/egrabanica/safe-railway-system-promela) | P1 | LEAN_GAP |
| `IND05-02-B` | 铁路信号站间事件顺序的 deadlock/liveness 建模 | [egrabanica/safe-railway-system-promela](https://github.com/egrabanica/safe-railway-system-promela) | P1 | LEAN_GAP |
| `IND07-01-A` | 血液透析设备 preparation/initiation/ending 工作流的 ASM 规格 | [asmeta/asmeta](https://github.com/asmeta/asmeta) | P1 | LEAN_GAP |
| `IND07-01-B` | 透析超滤控制系统的流量约束及模型到控制器测试 | [mathworks/Dialysis-Machine-Simulink](https://github.com/mathworks/Dialysis-Machine-Simulink) | P1 | LEAN_GAP |
| `IND07-05-A` | 生物序列文件解析、编码与格式一致性 | [biopython/biopython](https://github.com/biopython/biopython) | P1 | LEAN_GAP · **Batch14 L3×2：论文/源码及可信边界** · [证据](industry-depth3-p1p2-source-map-batch14.md) |
| `IND07-05-B` | 化学分子 SMILES/结构表示与描述符计算一致性 | [rdkit/rdkit](https://github.com/rdkit/rdkit) | P1 | LEAN_GAP |
| `IND09-04-A` | AI GPU 推理 kernel 在指定 shape 下的访存界限 | [facebookresearch/lean_kernel_verify](https://github.com/facebookresearch/lean_kernel_verify) | P1 | CROSS_DOMAIN_REUSE |
| `IND09-04-B` | CuTe/Triton kernel barrier 与 TMEM 复用时序 | [facebookresearch/lean_kernel_verify](https://github.com/facebookresearch/lean_kernel_verify) | P1 | CROSS_DOMAIN_REUSE |
| `IND10-01-A` | 高能物理定义和代数物理结果的 Lean 领域库组织 | [leanprover-community/physlib](https://github.com/leanprover-community/physlib) | P1 | PROJECT_LINEAGE |
| `IND10-01-B` | 高能物理新形式化材料进入 PhyslibAlpha 后如何与核心库区分 | [leanprover-community/physlib](https://github.com/leanprover-community/physlib) | P2 | E1_SCOPE_CHECK |
| `IND11-03-A` | 企业细粒度 RBAC/ABAC 授权策略的 Lean 语义与权限约束 | [cedar-policy/cedar-spec](https://github.com/cedar-policy/cedar-spec) | P1 | CROSS_DOMAIN_REUSE |
| `IND11-03-B` | 授权策略在 Lean 规格与 Rust 执行引擎之间的差分一致性 | [cedar-policy/cedar-spec](https://github.com/cedar-policy/cedar-spec) | P1 | CROSS_DOMAIN_REUSE |
| `IND11-05-A` | 政府采购 tender/award 字段模式与阶段约束 | [open-contracting/standard](https://github.com/open-contracting/standard) | P1 | LEAN_GAP · **Batch14 L3×2：论文/源码及可信边界** · [证据](industry-depth3-p1p2-source-map-batch14.md) |
| `IND11-05-B` | 政府采购 contract amendment 的变更历史与可追溯性 | [open-contracting/standard](https://github.com/open-contracting/standard) | P0 | LEAN_GAP · **细拆候选** · **L3_MAPPING_E1 Batch5 ×2** |
| `IND12-05-A` | 跨学科物理知识的 Lean4 定理库与文献依赖管理 | [leanprover-community/physlib](https://github.com/leanprover-community/physlib) | P1 | CROSS_DOMAIN_REUSE |
| `IND12-05-B` | 化学物理 Langmuir/BET 论文结果的可检查知识资产 | [atomslab/LeanChemicalTheories](https://github.com/atomslab/LeanChemicalTheories) | P1 | CROSS_DOMAIN_REUSE |

## 4. 下一轮优先深钻的 12 个“仍过宽”典型问题

| L2 ID | 必要的拆分理由与后续技术方向 |
|---|---|
| `IND04-03-B` | 风险定义、有限状态的鲁棒表示、CVaR 优化约束是不同性质；继续按 theorem/约束拆分 |
| `IND04-04-B` | 历史股票池、成分变更、修订 as-of join 分不同数据契约；AI_Trader Issue 不能替代可定位的具体代码/规格 |
| `IND06-03-B` | 动力系统稳定性与控制律实现精化分开；LeanForControl 与 DynamicalSystems 不应自动互为同一论文 companion |
| `IND09-02-C` | Autograd tape、CPU 算子、CUDA kernel、编译降级属于不同接口和验证目标 |
| `IND10-04-A` | SciLean 的数值表示、微分算子、误差界是独立技术问题；repo 作者称 proof-of-concept |
| `IND03-05-A` | BFT safety 的 quorum、状态转移、归纳不变量以及 liveness 假设应该分开 |
| `IND07-03-B` | CGM 时点有效性、剂量上限、泵动作确认分别是不同控制/医疗安全问题；Lean 直接工程仍缺 |
| `IND10-06-A` | ClimaCore 网格几何/离散算子/数值守恒各是独立假设；目前仅行业实现 |
| `IND11-05-B` | 采购 release/record 版本链与合同 amendment 合法性完全不同；后者需独立 Lean/法律语义证据 |
| `IND03-02-B` | ArkLib IOP/SNARK 组合性、soundness/completeness 及承诺机制是不同算法接口；各自证明范围尚未核 |
| `IND04-05-B` | 激励相容、个体理性、资源可行性应按不同机制与策略空间拆分 |
| `IND01-05-B` | SP1 约束 soundness、completeness 与 Rust→Clean→Lean fidelity 是不同性质，不能一个叶节点全包 |

以上 12 条是**进一步分解的研究建议**；只有在论文、标准、项目 README 或源文件已有可追溯证据时才能补充实际 L3/L4 节点。不凭想象补具体 theorem 或 GitHub 仓库。

## 5. 研究闭合标准

1. 一条叶节点必须是一个独立可形式化问题，有准确的对象、假设、验证目标与边界。
2. 每个最终节点必须链接至少一个真实 GitHub 仓库，区分 Lean 直接项目、Lean 基础设施、其他形式化方法、参考实现。
3. 论文/标准必须是 direct companion、原始方法或与问题紧密相关且明确标 `RELATED_METHOD`；纯项目 README 算 `PROJECT_DOC_ONLY`，不能伪装成同行评审论文。
4. 旧版/后继库、跨行业复用同一个 repo 以额外引用关系表达，不重复加“独立仓库数”。
5. 若根本没有 Lean 实现，保留 `LEAN_GAP`；如果只有 Issue、目录或论文没有实际代码项目，标 `PROJECT_GAP`，不可虚构。
6. `LEAF_CLOSED` 仅是**研究映射闭合**，绝不等于 theorem axiom footprint、软件构建、模型正确性或生产部署通过，这些属于用户今后按需选择的项目审计。
7. 定向人工验证可以将 P0/P1/P2 升降，但应保留所用原始资料和版本；不把自动 triage 结果误当实证检验。

## 6. 唯一下一步（Batch14 更新）

经过Batch12/13/14，P1/P2已下钻 **36个L2→72个L3**，再加原P0 30个父，累计**66/124个L2进入第三层**。尚有P1 33 +P2 25，共58个未下钻。**下一动作：从这58个中挑第四批约12个新的L2父节点，沿具体性质、原论文/官方标准和真实GitHub源文件继续下钻**；避免重复已覆盖的36父；原P0 31来源证据缺口和Batch14编译器不可信公理作为明确例外队列保留。保持Issue #74原目标和AC不变。

## Batch6 增量证据（2026-11-23）

[17 个 L3 源码/论文映射完整表](industry-depth3-p0-source-anchors-batch6.md) 已实际写入、回读校验 ID 唯一。本批 6 个父节点此前均未下钻；目前 23/30 个 P0 有 L3，剩余 7 个在 §1A 列示。研究级 E1 不自动转为 LEAF_CLOSED，外部 clean build、依赖/公理审计、原型和独立 QA 均 NOT_RUN。原 124 L2 和 P0/P1/P2 = 30/47/47 分母不变。


## Batch7 增量证据：30/30 P0 覆盖，但证明与叶节点均未全部闭合

- [Batch7 的 21 个 L3 源码锚点与 Lean GAP](industry-depth3-p0-source-anchors-batch7.md) 已实际写回并 GET 回读：7 个原未下钻 P0，各 3 个唯一 L3，涵盖 IFP、PIT 历史股票池、SciLean、LegalLean、Concerto、CGM/OpenAPS 与 ClimaCore；直接 Lean 项目与其他行业实现严格分开。
- **累计 81 L3、2 L4，30/30 P0 至少继续一层；原 124 L2/P0=30、P1=47、P2=47 不变。** 任何补全比例仅表示研究地图结构深度，不表示源码编译、证明独立 QA 或行业现实安全。
- 纠偏要点：IFP 93/103 不变量仍有 10 pending；SciLean `odeSolve_fixed_dt` 有 `sorry_proof`；LegalLean 的 TypeclassConstraint 有显式 `axiom IsReasonable`；Concerto/OpenAPS/ClimaCore 是 LEAN_GAP；PIT 已有 eligibility theorem 但没有历史成员版本选择完整证明。
- **下一轮优先**：对 30 P0 的 **81 个 L3 和 2 个 L4** 建立 closure 状态矩阵，定理/假设/论文/代码相符才记来源级闭合；如果有必要再向 L4/L5 递归。随后处理 P1/P2 来源匹配与未完成 AC，不开展无目标的外部项目审计。
