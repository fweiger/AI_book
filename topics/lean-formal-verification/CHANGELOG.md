# TOPIC-018｜变更记录

- **2026-11-22，v0.1.0（Draft）**：建立 Lean 形式化证明与跨学科应用专题框架；创建规范研究 Issue #74；初步读取 Lean 官方语言参考、Elan 安装手册、Mathlib、Lean 项目目录、Aeneas、Rust-to-Lean 经验报告、经济学/金融数学、TorchLean 和 physicslib4 等来源。当前仅为来源级初筛；未完成逐项目构建、许可证审计、独立复现或独立 QA。


- **2026-11-22，v0.2.0（Draft）**：完成首批 10 个代表仓库的默认分支 commit、README、toolchain、LICENSE 和 Lake 配置入口级审查；发现 Lean 3/Lean 4 混用、项目版本分散在 4.30.0—4.37.0-rc1、Aeneas 使用嵌套 Lean backend、rust-lean 为多子项目集合；新增 C018-010 至 C018-014 和版本化准入表。除 Mathlib bors status success 外，其他项目未获得可用 status context；所有本地构建 NOT_RUN，许可/依赖/证明状态审计未全部完成。


- **2026-11-22，v0.2.1（Draft）**：补充 8 个 Lean 4 项目的 Lake manifest 解析结果，记录 Mathlib 与关键传递依赖的精确 commit revision；新增 C018-015。进一步确认可复现性至少需要项目 commit + lean-toolchain + lake-manifest 三者，单独记录 Lean 版本不足。所有项目实际构建仍 NOT_RUN。


- **2026-11-22，v0.3.0（Draft）**：深入审查 rust-lean 的 Hax-FRI 与 Hax ADC 子项目；记录 Rust→Lean 抽取、Hax annotations、hax_bv_decide bit-blasting、ArkLib 规格连接和实际抽取障碍；新增 C018-016/017 与 M-01/M-02/M-03 方法卡。新增知识图谱节点区分局部算术证明与协议级正确性；所有案例仍为 E1，未独立构建。

- **2026-11-22，v0.4.0（Draft）**：修正 Hax ADC 历史 issue 状态，核对 #1925/#1927/#1933/#1938/#1959/#2064/#2142 上游 PR；以 Hax 官方 lean_adc 示例更新 M-01，新增 M-04 至 M-07。对同一 Rust blob 的 Hax/Aeneas FRI pipeline 做源码对照：Aeneas BasicProofs 6 theorem + 3 example 静态无 sorry/axiom；ArkLib bridge 仍含 3 axioms、1 opaque、4 sorry；Hax FRI 有 2 个实质性边界定理证明，另有 4+9 个 sorry。新增 C018-018 至 C018-025、Q07/Q08 和独立会话记录。所有 Lean build 与独立 QA 仍 NOT_RUN。

- **2026-11-22，v0.4.0（Draft）**：追踪 Hax ADC 历史障碍的上游解决状态；确认 PR #1925、#1927、#1933、#2142 已合并；识别 Hax-FRI 固定 commit 早于 #1925/#1933，而 Hax 0.5.0 已升级至 Lean 4.35.0 并包含 breaking changes。新增 C018-018 至 C018-022、M-04/M-05。下一步从“追踪旧障碍”转为“旧版基线复现 + 新版迁移对照”。

- **2026-11-22，v0.5.0（Draft）**：深审 MathFin 固定 commit，读取 4.35.0 toolchain、Mathlib/BrownianMotion manifest、coverage taxonomy、AxiomAudit/AxiomAuditGen、build workflow、Gaussian CVaR、Markowitz KKT、CRR convergence 与 Gaussian risk report；解析 risk/portfolio/binomial 三个 benchmark JSON 共 156 项且均为 full。新增 M-08 至 M-13、C018-026 至 C018-033、Q09；强调 MathFin 是数学金融证明库，不是实证回测系统。未运行 MathFin build。

- **2026-11-22，v0.6.0（Draft）**：建立独立 Lean 4.35.0 PIT/no-lookahead 最小 package 与专用 GitHub Actions build workflow；区分 eventTime/availableAt/decisionTime，加入 eligibleRows_no_lookahead、late_available_revision_excluded 和 late correction 示例；新增 M-14、C018-034 至 C018-037、Q10。当前只完成源码和工作流配置，build 等待 CI 回读。

- **2026-11-22，v0.6.1（Draft）**：去重方法卡与 claims ID，合并重复的 Hax specset 节点/路径；补齐 C018-026 至 C018-033 的 MathFin 证据行，并将 Hax 版本迁移方法单列为 M-15。修复 MathFin 方法卡中的数学符号转义问题。

- **2026-11-22，v0.6.2（Draft）**：PIT/no-lookahead 独立 Lean 4.35.0 package 的 GitHub Actions Run #15 成功；job log 确认 `lake build` completed successfully。两个 theorem 的 `#print axioms` 均为 `[propext]`。AC-06 的最小可复现流程由配置推进到实际 Kernel build PASS；完整 as-of join 仍未完成。

- **2026-11-22，v0.6.3（Draft）**：在 PR head `1e700ff89fbce8fa3106c99b93ebe45b03cc6557` 上复跑 PIT Lean workflow Run #19，job success；`lake build` completed successfully，两个 theorem 的 axiom 输出均为 `[propext]`。更新 case study、method card、claims、README 和 session evidence，确认 AC-06 最小可复现流程 PASS。

- **2026-11-23，v0.7.0（Draft，合并校正版）**：完成 10 个领域、22 个方向级“研究方向—论文—Lean 项目—相邻工具—研究空白”映射；更新 MathFin、LeanInfoTheory、Rate-Distortion、AI4SLT、TorchLean、DynamicalSystems、Veil/IFP 的源码/版本线索；新增 M-16 至 M-18、C018-023 至 C018-029 与 Q11–Q15；PIT Run #24 / integrity Run #1255 PASS。旧草稿曾引用 C018-038—060，但这些行不在当前 claims ledger，本次不复用该区间。

- **2026-11-23，v0.8.0（Draft）**：完成 Rate-Distortion、AI4SLT、Veil 三张固定 commit 项目审计卡；确认 Rate-Distortion 旧 build log 不覆盖当前 source、AI4SLT release build 与 main code 一致、Veil exact-SHA CI Run #442 与 TrustAudit PASS；区分 model assumptions、sorryAx、standard axioms、unsafe/implemented_by 和 liveness 边界；新增 M-19/M-20、C018-061 至 C018-068、Q16；AC-05 仍 PARTIAL。
