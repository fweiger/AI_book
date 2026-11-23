# TOPIC-018｜论文—GitHub 项目关联精度复核：Batch 1

> 日期：2026-11-23  
> 所属任务：[AI_book #74](https://github.com/fweiger/AI_book/issues/74) · [PR #75](https://github.com/fweiger/AI_book/pull/75)  
> 审核对象：[60 个首轮父节点](../industry-leaf-project-map.md) 与 [55 个第二轮项目级候选子节点](../industry-recursive-split-register.md)  
> 本轮范围：**只核对业务问题、原始论文/报告/标准和真实 GitHub 仓库的关联。不开启 clean build、proof/axiom/许可证审计，不运行最小原型。**

## 1. 目标与检查口径

用户明确的最终终点不是固定层数或固定数量，而是每个行业分支可递归到一个独立问题与实际 GitHub 项目。只有真实论文/标准/项目说明和 GitHub 仓库的关联可以回读，才能判断候选叶节点是否能闭合。

- **论文—项目关系**：DIRECT_COMPANION（论文说明的直接开源仓库）、DIRECT_PROJECT_MENTION（论文明确介绍该软件但不保证对应某固定版本实现）、RELATED_METHOD（同领域方法而非该仓库的配套论文）、PRIMARY_TECH_REPORT（团队原始技术报告/项目报告）、PRIMARY_SOFTWARE_RELEASE（软件发行/DOI，不等于同行评审论文）、PROJECT_DOC_ONLY。
- **技术关系**：DIRECT_LEAN_APPLICATION / DIRECT_LEAN_RESEARCH / LEAN_INFRASTRUCTURE / ADJACENT_FORMAL_TOOL / DOMAIN_REFERENCE_IMPLEMENTATION。
- **证据强度**：本轮读取 GitHub 原始 README 或项目技术说明，属于来源级 E1；**不升级为 E2/E3 或证明审计 PASS**。仓库自述的证明状态必须标成“项目自述”。
- **缺口**：缺同行评审论文不等于完全缺原始技术资料；必须将论文 GAP 与项目技术报告分开记录。一个项目“与论文相关”不等于该论文正式对应当前实现。

## 2. 全局结构核算

从当前仓库两个主表中逐条提取节点 ID：

- 首轮父节点：**60** 个，覆盖 12 个一级行业。
- 二轮候选子节点：**55** 个。
- 已产生二轮子节点的父节点：**25** 个。
- 尚未拆分的首轮父节点：**35** 个。
- 55 个子节点目前还不能因存在 GitHub 项目就全数标为 `LEAF_CLOSED`；其中若干论文对应关系、过宽问题和项目性质需进一步修正。

本轮对 **9 个有具体原始证据的子节点**修订了论文/项目关系，并追加 **7 个**有第一手仓库来源的新子节点；不是 62 个子节点的完整独立验收。

## 3. 实际回读与纠正（9 个子节点）

| ID | 原有缺陷 | 本轮实际回读的原始证据 | 修改后的关系与边界 | 当前结论 |
|---|---|---|---|---|
| IND01-05-A OpenVM | 只有开发博客，直接记为 PAPER_GAP | [openvm-fv README](https://github.com/openvm-org/openvm-fv) 明确 45 个 RV32IM opcodes、OpenVM v2.0.0 固定来源，并注明 [REPORT.pdf](https://github.com/openvm-org/openvm-fv/blob/main/REPORT.pdf) 只覆盖 RV32IM | 博客和项目报告为第一手技术报告；不能充当同行评审论文，也不能扩大为整个 zkVM 安全证明 | PRIMARY_TECH_REPORT / PEER_REVIEWED_PAPER_GAP |
| IND01-05-B SP1 | 只有“项目说明”占位 | [sp1-lean README](https://github.com/succinctlabs/sp1-lean)；[zkEVM Foundation 原始技术报告](https://zkevm.ethereum.foundation/blog/sp1-fv) | Lean 声明的 soundness、completeness、faithfulness 范围不同；README 说明部分 completeness 尚未关闭，并不是端到端 VM 证明 | PRIMARY_TECH_REPORT / PEER_REVIEWED_PAPER_GAP |
| IND02-02-A Aeneas | 将 arXiv 2605.30106 写作 Aeneas 自身 DIRECT_COMPANION | [Aeneas README](https://github.com/AeneasVerif/aeneas) 说明它是 Rust→Lean/F*/Rocq/HOL4 翻译器；[rust-lean README](https://github.com/Verified-zkEVM/rust-lean) 列明 Hax/Aeneas 的实际案例；[经验报告](https://arxiv.org/abs/2605.30106) 研究整个 pipeline | Aeneas 是所用工具，而 [rust-lean](https://github.com/Verified-zkEVM/rust-lean) 是论文描述的实验案例仓库；不能把工具和论文配套实现混同 | RELATED_TOOL + PAPER_EXPERIENCE_CASE |
| IND02-04-B Resonate | 将 Lean 形式化规格错标为普通行业参考实现 | [resonate-specification README](https://github.com/resonatehq/resonate-specification) 明确 Lean 4 可执行抽象机、状态/转换、性质目录与真实服务器 trace checker；[协议规格](https://github.com/resonatehq/distributed-async-await.io) | 应改为直接 Lean 研究/规格实现。README 自述 92 项性质：31 项无界证明、61 项仍开放；1,464 脚本上的 decide 检查不是其余 61 项的无界证明 | DIRECT_LEAN_RESEARCH / PRIMARY_PROJECT_SPEC / PEER_REVIEWED_PAPER_GAP |
| IND06-03-A MoveIt | ICRA 2019 论文只挂通用 moveit2 仓库并称 DIRECT_COMPANION | [moveit_task_constructor README](https://github.com/moveit/moveit_task_constructor) 的 citation 节直接引用 [ICRA 2019 DOI](https://doi.org/10.1109/ICRA.2019.8793898)；其功能为多阶段操纵任务规划 | 专门仓库为 DIRECT_COMPANION；[moveit2](https://github.com/moveit/moveit2) 是支撑框架，不是该论文的直接 artifact | DIRECT_COMPANION / DOMAIN_REFERENCE_IMPLEMENTATION（不是 Lean） |
| IND06-04-B Grid2Op | 误标 PAPER_GAP | [Grid2Op README](https://github.com/Grid2op/grid2op) 与 [Marot et al., PMLR 133 (2021)](https://proceedings.mlr.press/v133/marot21a.html)；论文明确介绍 Grid2Op 作为开放电网序贯决策框架 | PMLR 是直接介绍该平台的论文，但不能宣称每个当前版本算法均在论文中得到形式化验证；平台本身不是 Lean 证明工具 | DIRECT_PROJECT_MENTION / DOMAIN_REFERENCE_IMPLEMENTATION |
| IND08-01-A LeanInfoTheory | 只挂经典教材作为直接论文 | [LeanInfoTheory README](https://github.com/serhatemrecoban/LeanInfoTheory) 明确形式化熵、KL、互信息、信道等，并列出 [v0.2.0 归档 DOI](https://doi.org/10.5281/zenodo.23973538) | 教材是理论基础，Zenodo 是软件研究成果/发行锚点；本轮未核实同行评审的 LeanInfoTheory companion paper | PRIMARY_SOFTWARE_RELEASE / PAPER_GAP |
| IND09-05-A LeanDojo | 使用已弃用的旧仓库，缺少 successor | [LeanDojo README](https://github.com/lean-dojo/LeanDojo) 明确 deprecated，要求新项目用 [LeanDojo-v2](https://github.com/lean-dojo/LeanDojo-v2)；v2 README 已回读 | 旧仓库是 [LeanDojo 原论文](https://arxiv.org/abs/2306.15626) 的对应工具；v2 是后继工程，不能自动把论文实验覆盖推广到 v2 | HISTORICAL_COMPANION + SUCCESSOR_PROJECT |
| IND12-04-A LeanDojo | 教育/知识服务映射沿用同一旧入口 | 同上两个项目的原始 README；v2 增加 tracing、Agent 与模型训练等工作流 | 加入新仓库，保留历史论文关系，不将原项目退役误作 Lean 推理工具不存在 | HISTORICAL_COMPANION + SUCCESSOR_PROJECT |

### 附加观察（已读仓库，但不在本轮 9 条修正计数中）

- [Aeneas](https://github.com/AeneasVerif/aeneas) 同时支持多个后端，不能将“Rust 软件验证”全部宣称是 Lean 专属。
- [LeanForControl](https://github.com/AnandGokhale/LeanForControl) README 列出具体模块（Lyapunov、ODE、LinearSystems 等）及其自述的证明/构建状态；项目中实际定理覆盖与论文关系仍需逐项核验，不因此将对应节点直接关闭。
- [MathEconLib](https://github.com/matheconlib/matheconlib) README 明确其当前重点为微观经济理论，虽然长期目标包含宏观与计量；不能因长期目标就宣称均已形式化。
- [EconCSLib](https://github.com/gametheoryinlean/EconCSLib) README 的 Blueprint 同时包含形式化成果和数学目标；不能把目标项全部计作 Lean 已证明。
- [LeanLTL](https://github.com/UCSCFormalMethods/LeanLTL) README 中提供 TrafficLights、有限/无限 trace 等实际库入口，但不是每个分布式系统的 companion implementation。

## 3A. 在未拆父节点中追加 7 个有来源的候选子节点

本轮在上述论文/项目映射纠正后，又以 GitHub 原始 README 为依据，从 **3 个尚未拆分的父节点** 新增 **7 个** 子节点：

| 原父节点 | 追加子节点 | 区分的独立研究问题 | 第一手对应项目 |
|---|---:|---|---|
| IND02-01 云授权 | 2 | Lean 形式化 Cedar 授权决策语义；Lean/Rust 差分测试与实现一致性 | [cedar-spec](https://github.com/cedar-policy/cedar-spec) · [cedar](https://github.com/cedar-policy/cedar) |
| IND02-05 OS/xv6 | 2 | 系统/设备执行的 trace adequacy；用户态指令与资源规范 | [xv6iris](https://github.com/mit-pdos/xv6iris/tree/lean) · [论文](https://arxiv.org/abs/2609.04043) |
| IND09-02 AI/TorchLean | 3 | shape-checked tensors；graph rewrite 的验证；CPU/CUDA 共用 op/autograd 语义 | [TorchLean](https://github.com/lean-dojo/TorchLean) · [论文](https://arxiv.org/abs/2602.22631) |

**新总量：** 首轮父节点 60；累计项目级候选子节点 **62**（原 55 + 本轮 7）；已发生下钻的父节点 **28**；尚未拆分的首轮父节点 **32**。

这 7 个子节点仍为 `CANDIDATE_LEAF`，不是已验证 Lean theorem 证明完成，更不能表示生产程序已整体通过验证。新增条目已放在 [第二轮递归拆分登记表 §2A](../industry-recursive-split-register.md)。

## 4. 待拆节点与质量门槛

初始核算 **35 个父节点**尚无子节点；本轮已新增 3 个父节点的 7 个子节点，当前剩余 **32 个父节点**没有更细子节点；应优先从多个算法、组件或系统流程仍混在同一节点的方向继续拆开。下一轮先从这些父节点中选有第一手标准/论文与仓库可回读的分支进行拆分；不得让“已有 GitHub 链接”成为停止递归的充分条件。

逐条闭合检查：
1. 是否对应单个业务/技术问题，还是仍包含多种算法和性质？
2. GitHub 实际仓库是否在该问题的正确层级，是否为同一作者论文的 companion？
3. 是否区分同行评审论文、预印本、项目技术报告、官方标准和软件发行 DOI？
4. 是否确切区分 Lean 直接形式化、相邻形式化工具和行业参考实现？
5. 是否记录仍缺失的 Lean 项目、直接论文或代码落点？

**LEAF_CLOSED 仅意味着“研究映射证据闭合”**，不意味着该项目的定理、构建、许可证、生产使用或经济价值已经独立审计。

## 5. 本轮状态与唯一下一步

- **PASS：** 9 个子节点的来源/论文/仓库关系已修正；关键项目 README 已回读。
- **PARTIAL：** 总计 62 个候选子节点尚未全部校核；60 个父节点中的 32 个尚未拆出下一层。
- **NOT_RUN：** 外部项目 clean build、proof/axiom 检查、许可证审计、原型和生产集成。
- **Goal drift：** D0，仍服务于 TOPIC-018 跨行业真实应用地图。
- **唯一下一步：** 优先推进剩余 32 个未拆父节点中仍然过宽的分支，同时按同一证据口径继续复核其余 53 个候选子节点；记录 DIRECT_COMPANION / RELATED_METHOD / PRIMARY_TECH_REPORT / PROJECT_GAP，不能凑数。
