# TOPIC-018｜Batch 4：从 124 个 L2 节点继续下钻 L3 并建立全量复核队列

> 日期 2026-11-23 · [Issue #74](https://github.com/fweiger/AI_book/issues/74) · [Draft PR #75](https://github.com/fweiger/AI_book/pull/75)  
> 动态状态仍按唯一 `task-goals/issue-74/GOAL_TRACKER.md`；批准 Goal/Scope/AC 不变。

## 核心目标和本轮实际成果

用户要求行业→领域→问题→形式化对象/验证性质→论文→GitHub 不限深度递归，达到真实 GitHub 项目层，不提前审计或原型。

恢复了 60 个父节点、124 个唯一 L2 候选节点及上轮 Issue event #7093733197。**新建**：

- [第三层研究地图](../industry-depth3-paper-project-map.md)：从 8 个既有 L2 节点新增 **16 个 L3 候选**，涉及 SSA/peephole、VCVio oracle/概率语义/关系逻辑、布朗运动的 Gaussian construction/连续性、CRR 无套利/收敛、AI4SLT 高斯集中/局部最小二乘、TorchLean 模型图与证书。
- [124 节点闭合复核队列](../industry-leaf-closure-triage.md)：完整列出原 124 L2 ID、对应主要 GitHub 仓库、自动关键词标签、缺口优先级和 12 条需要继续分解的典型问题。
- 修订 [L2 登记表](../industry-recursive-split-register.md)：明确标识 8 个 `CONTINUE_SPLIT`，纠正两个重要来源对应关系。

## 来源级纠错

1. `IND04-01-A` 原来把 MathFin 论文泛用为布朗运动节点的直接研究来源；新核 [Formalization of Brownian motion in Lean](https://arxiv.org/abs/2511.20118) 是 [brownian-motion](https://github.com/RemyDegenne/brownian-motion) 直接配套预印本。README 只称 Brownian construction 已完成，stochastic integrals/Itô lemma 仍在推进，不扩大完成范围。
2. `IND09-01-A/B` 原先仅挂 [YuanheZ/lean-stat-learning-theory](https://github.com/YuanheZ/lean-stat-learning-theory)，它是 [ICML 2026 AI4SLT](https://proceedings.mlr.press/v306/zhang26cd.html) 原始论文仓库；[Lean-MoDS/StatsMLlib](https://github.com/Lean-MoDS/StatsMLlib) README 称整合了先前 SLT/FoML 两条代码线，应作为当前整合代码入口，而非新独立论文成果。
3. `IND01-03-A` 的 [ITP 2024 同行评审论文](https://doi.org/10.4230/LIPIcs.ITP.2024.9) 公开列出 [lean-mlir ITP24 artifact](https://github.com/opencompl/lean-mlir/tree/ITP24)，优先作为直接复现链的仓库版本定位，而非仅默认分支。
4. VCVio [ePrint 2026/899](https://eprint.iacr.org/2026/899) 对应 [VCVio](https://github.com/Verified-zkEVM/VCVio) 的 oracle 语义、概率事件和程序逻辑。README 同时列多个不同类性质，按不同技术问题拆分更有意义；项目里的个别密码学定理没有进行本轮代码 QA。

## 核对过的数量和证据级别

| 指标 | 实际结果/口径 |
|---|---|
| 原始一级行业 | 12 |
| L1 父节点 | 60，已有至少一层 L2 子节点 |
| L2 候选 | 124，ID 唯一 |
| GitHub 不同路径（初步） | 84；只对 URL 的 owner/repo 字符串做大小写去重，没有做迁移/镜像实体统一 |
| 本轮继续拆的 L2 节点 | 8 |
| 本轮新增 L3 节点 | 16，论文或项目技术资料/实际仓库对应 |
| 其他未进入 L3 的 L2 | 116，需确认是否本已是足够小的研究终点 |
| triage P0 / P1 / P2 | 30 / 47 / 47；**仅自动标签与定向研究优先级，不是完成度、质量评分或已核论文数量** |
| Lean_Gap 关键词 | 20 / 124，存在其他未识别缺口；重叠标签不求和 |
| Paper_Gap 关键词 | 12 / 124，技术报告可能存在但同行评审论文未找到 |
| Cross-Domain-Reuse 关键词 | 6 / 124，其他同仓库重复引用仍可能没有标注 |

本轮只是 E1 论文/官方标准/README 研究关联。**未执行**外部项目 clean build、源码质量/axiom/sorry/许可证审计、真实金融数据实验、最小原型或独立 E2E QA。没有把仓库作者对其定理或生产级的声明写成独立验收。

## 目标偏离和唯一下一步

- 原 Goal：跨行业 Lean 机会知识树；本轮沿既有 ID 持续向更细问题、论文和 Github 建图，**D0**。
- AC-03：`PARTIAL`（124 L2 结构覆盖 + 16 L3 更细映射；尚未完成每个 L2 的 `LEAF_CLOSED`）。
- AC-07：`PARTIAL`（区分旧论文仓库/整合库、直接 Lean、相邻方法与应用空白）。
- AC-05：本轮无审计，状态不提升。
- **唯一下一步：** 依据 [全量 triage 队列](../industry-leaf-closure-triage.md)，优先推进 30 个 P0 中的直接论文/具体代码落点缺口和仍过宽问题，再复核 47 个 P1 的关系类型；需要时继续向 L4/L5 递归。`LEAF_CLOSED` 仅用于来源与研究映射闭合，独立证明/构建/原型后置。
