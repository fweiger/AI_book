# TOPIC-018｜Batch 5：P0 深度研究下钻至 L3/L4 与代码/论文锚点

> 日期：2026-11-23；任务： [AI_book #74](https://github.com/fweiger/AI_book/issues/74) · [Draft PR #75](https://github.com/fweiger/AI_book/pull/75)  
> 本批交付：[P0 第三级与 CVaR 第四级地图](../industry-depth3-p0-source-anchors-batch5.md) · [124 L2 完整队列](../industry-leaf-closure-triage.md)  
> 原目标：行业→业务子领域→单一可形式化问题→具体数学性质/代码→论文/标准→实际 GitHub 项目。**本批不做外部仓库构建、许可/依赖/axiom/sorry 深审或最小原型。**

## 1. 恢复与本轮执行

回读了 Issue #74、原分支 Draft PR #75、唯一 Tracker、124 节点 P0/P1/P2 优先级队列和锁定的 Task Center V1.2.2 协议；原状态是 `CONSISTENT / SYNCED`、Writer 为 `NONE`，最后有效 event `DEPTH3-PAPER-REPO-BATCH4-20261123`。

在当前 30 个 P0 中挑出 **9 个尚未下钻的 L2**，逐项读取 GitHub 项目 README、官方研究状态、定向源码文件、标准样例和对应学术方法；同一性质的不同约束/假设被拆成独立问题，并对旧记录的过宽表述进行纠正。

## 2. 实际完成的研究映射

| L2 父节点 | 新 L3 | 证据中关键的代码或模型 | 修正的边界 |
|---|---:|---|---|
| `IND01-05-B` SP1 | 4 | [AddChip/Formal.lean](https://github.com/succinctlabs/sp1-lean/blob/main/SP1Clean/Proofs/Chips/AddChip/Formal.lean)、[release-audit](https://github.com/succinctlabs/sp1-lean/blob/main/docs/release-audit.md) | per-chip soundness、completeness、Rust constraints faithfulness 与 whole-VM soundness/capstone 分开，版本与 proof gaps 必须保留 |
| `IND02-04-B` Resonate | 3 | [spec/02-abstract](https://github.com/resonatehq/resonate-specification/tree/main/spec/02-abstract)、[valid/README](https://github.com/resonatehq/resonate-specification/blob/main/valid/README.md) | 92 项性质中官方自述 31 项已证明、61 项仍开放；轨迹 checker 不是所有服务器行为无界正确性 |
| `IND03-02-B` ArkLib | 3 | [ArkLib/OracleReduction](https://github.com/Verified-zkEVM/ArkLib/tree/main/ArkLib/OracleReduction)、[docs/design/current-status](https://github.com/Verified-zkEVM/ArkLib/blob/main/docs/design/00-current-status.md) | legacy layer 与新的 Interaction layer 的迁移状态分开；过去挂的 Rust-to-Lean 论文非直接 companion |
| `IND03-05-A` Veil | 3 | [FloodSet.lean](https://github.com/verse-lab/veil/blob/main/Examples/Tutorial/FloodSet.lean)、[FloodSetLiveness.lean](https://github.com/verse-lab/veil/blob/main/Examples/Demo/FloodSet/FloodSetLiveness.lean) | FloodSet 是同步 crash-fault / fail-stop 协议，不能称一般 Byzantine BFT 验证 |
| `IND04-03-B` 金融 CVaR | 4 | [ValueAtRisk.lean](https://github.com/formal-applied-math/formal-mathfin/blob/main/MathFin/Risk/ValueAtRisk.lean)、[ExpectedShortfall.lean](https://github.com/formal-applied-math/formal-mathfin/blob/main/MathFin/Risk/ExpectedShortfall.lean)、[AcceptanceSet.lean](https://github.com/formal-applied-math/formal-mathfin/blob/main/MathFin/Risk/AcceptanceSet.lean) | 一般分布的 RU 最小化、ES coherent risk、公理和有限状态对偶不同；原始论文是理论来源而非该仓库 companion |
| `IND09-02-C` TorchLean | 3 | [BackwardDenseGraph.lean](https://github.com/lean-dojo/TorchLean/blob/main/TorchLean/NN/Tape/Lowering/BackwardDenseGraph.lean)、[ContractCheck.lean](https://github.com/lean-dojo/TorchLean/blob/main/TorchLean/NN/Backend/ContractCheck.lean) | exact tape/实数证明与 Float rounding、CUDA/LibTorch FFI 完全不同 |
| `IND01-04-A` GPU 访存 | 2 | [LKV specs](https://github.com/facebookresearch/lean_kernel_verify/blob/main/references/specs.md) P0-1 | concrete KIR/Input 访存边界与地址回绕；不验证任意 shape |
| `IND01-04-B` GPU 同步 | 3 | 同 [LKV specs](https://github.com/facebookresearch/lean_kernel_verify/blob/main/references/specs.md) P0-6/P1-1/P1-2 | named barriers、TMEM reuse、async store source reuse 分开；不推广 general race/deadlock freedom |
| `IND11-05-B` OCDS | 2 | [change_history/contractAmendment.json](https://github.com/open-contracting/standard/blob/main/docs/examples/change_history/contractAmendment.json)、[release-schema.json](https://github.com/open-contracting/standard/blob/main/schema/release-schema.json) | 行业 Schema/版本血缘参考实现；目前 `LEAN_GAP`，不将数据合规称为采购合法性证明 |
| **合计** | **27** | **9 个 P0 L2 父节点** | 源码与具体目标对齐，不是新建 27 个独立项目 |

此外对 `IND04-03-B-02` 增加 **2 个 L4**，明确 [ExpectedShortfall.lean](https://github.com/formal-applied-math/formal-mathfin/blob/main/MathFin/Risk/ExpectedShortfall.lean) 两个 theorem：
`expectedShortfall_le_rockafellarUryasev`（任意阈值的目标函数下界）与 `rockafellarUryasev_valueAtRisk`（在 VaR 阈值达到等号）。它们在更高一层合成 `isLeast_rockafellarUryasev`。原始经典论文是 [Rockafellar–Uryasev 2000](https://doi.org/10.21314/JOR.2000.038)。

## 3. 定量质量控制

- L1：60/60 父节点已有至少一个 L2；L2：124 条 ID 唯一。
- 前轮 Batch4：8 个 P0 L2 → 16 个 L3；本轮 Batch5：9 个**不同** P0 L2 → 27 个 L3、2 个 L4。
- 合计 **17/30 个 P0 L2 已至少下钻一层；43 个 L3、2 个 L4**；剩余 **13 个 P0** 待进一步研究。P0/P1/P2 的原始队列计数不变（30/47/47）。
- 代码/原始资料 `SOURCE_FILE_VERIFIED` 表示读取过文件；目录级路径是官方 README 指向。未把全部路径/每个定理在当前 toolchain 中编译复现。
- `LEAF_CLOSED=0` 不作推断：本轮不正式宣告任何 L3/L4 已通过全部研究映射闭合验收，相关问题需要后续单独检查证据质量。**新节点 ≠ 新仓库/新论文/新证明。**

## 4. 实际修订和剩余问题

- 更正 LKV 的 **层级归属**：访存与地址回绕在 `IND01-04-A`；Barrier/TMEM/async reuse 在 `IND01-04-B`，不能错误挂载。
- 更正 Veil 的 **故障模型**：FloodSet 是同步 fail-stop/crash fault，不可当作任意 BFT。
- 更正 ArkLib 的 **论文关系**：Rust-to-Lean 经验论文不是 ArkLib 的唯一 companion，应引用 ArkLib 自身 README、ROADMAP 和 design status。
- 进一步精确 MathFin 的 **证明范围**：一般分布可积 CVaR 的 RU 最小化/Coherent risk，以及有限状态风险对偶，与真实资金组合损益优化完全不同。
- 新写的 P0 下钻不涉及用户账号/健康个人数据，医疗应用方向未开展实际临床验证。

## 5. 原目标、AC 状态与唯一下一步

- Goal drift：**D0**；原 Issue #74 Goal/Scope/AC 没有改变。
- **AC-03 PARTIAL**：L3/L4 证据更精确，仍有 13 个 P0 和大量 P1/P2 未逐叶闭合。
- **AC-07 PARTIAL**：Lean 直接形式化、外部原生模型和 trust boundaries 已进一步区分。
- AC-05 外部项目审计：本轮 `NOT_RUN`，不提升既有状态。
- AC-06：保留先前 PIT Lean 工作流的单独历史结果，本轮没有新原型。
- AC-08 独立验收：`NOT_RUN`。
- **唯一下一步：** 按 [triage](../industry-leaf-closure-triage.md) 中列出的剩余 13 个 P0，先研究有直接代码/论文出处的分支，然后对已经下钻的 17 个 P0 逐条作 `LEAF_CLOSED` 的映射闭合判定，继续必要的 L4/L5；不提前进行项目内部审计或最小原型。
