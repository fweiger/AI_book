# 2026-11-23｜跨学科方向—论文—项目映射与源码复核

## 本轮目标
回到 TOPIC-018 原始 Goal，推进 AC-03/AC-05：把学科级目录细化成“研究方向 → 原始论文/理论 → 直接 Lean 项目 → 相邻工具 → 证明对象和边界”。

## 本轮实际完成
1. 审核现有 field-evidence-matrix：已覆盖数学及 9 个非数学领域，确认主线是逐方向论文与项目关联，而不是继续围绕 Hax 单点排障。
2. 新增 22 个方向级映射项，覆盖数学、程序验证、Datalog、LTL、密码学、ZK、Rust refinement、BFT、trace conformance、经济学、金融、AI/统计学习、神经网络、HEP、量子信息、Shannon 信息论、rate-distortion、控制和 hybrid systems。
3. 通过 GitHub 连接器直接读取 MathFin、LeanInfoTheory、rate_distortion_lean4、AI4SLT、TorchLean、DynamicalSystems、Veil/IFP 的 README、关键文件和 toolchain。
4. 通过公开学术来源交叉核验 AI4SLT、MathFin、EconCSLib、Veil、Datalog、LeanLTL、HepLean、Quantum Stein、rate-distortion、Doll–Shames control papers。
5. 新增 C018-023 至 C018-029，M-16；更新 field-evidence-matrix、field-map、bibliography、case-studies、methods、claims、README、CHANGELOG。

## 关键事实与版本修正
- MathFin 当前 GitHub main README：906 corpus results = 866 full + 18 library wrappers + 22 reduced cores；CITATION software release 2.0.0（2026-11-11）为 833 delivery-ready；docs/coverage 的 806 是 2026-11-08 检查点；论文 v4 的 804 是论文快照。统计口径/日期不同，不可混用。Lean 4.35.0。
- LeanInfoTheory master README：v0.2.0（2026-11-05），811 supported declarations / 57 modules，Lean 4.33.1；官网仍有 v0.1.0/601 declarations 旧页面。
- rate_distortion_lean4：Lean 4.28.0，有限字母表、PMF、自然对数/nats；MainResults.lean 包含主要 theorem 的 print axioms 与 allowlist gate；未运行 build。
- AI4SLT：论文在 ICML 2026 PMLR 306；配套 repo Lean 4.32.0；repo README 记录论文后扩展到 Hanson–Wright、矩阵扰动与 matrix Bernstein，必须和论文原始范围分开。
- TorchLean：Lean 4.36.0；同一 Lean tensor/model 定义用于训练、图变换、证书检查和证明；CUDA 注册 native operators 使用 LibTorch ATen，CPU/CUDA 语义需分开审计。
- DynamicalSystems：Doll–Shames 2026 控制理论论文对应 repo，toolchain Lean 4.36.0-rc2；未独立 build。
- Veil：Lean 4.35.0；Veil 2.0 是 transition-system verifier。
- IFP：README 明确当前 Phase 1 是两个固定参与者、单 epoch、确定节点集合；Phase 2 才扩展多参与者，Phase 3 才加入 read locks 与 epoch reconfiguration。93/103 invariant 是当前 Phase 1 状态，不是完整协议已证明。

## 学术来源交叉验证
- AI4SLT：PMLR 官方会议论文页，ICML 2026。
- Rate-Distortion：arXiv 2610.22404，有限字母表 rate-distortion formalization。
- Control：arXiv 2607.19727，Lyapunov stability 与 small-gain theorem。
- Veil：CAV 2025 Springer paper。
- Datalog/LeanLTL：ITP 2025 Dagstuhl LIPIcs papers。
- HepLean：CPC 2025 DOI 10.1016/j.cpc.2024.109457。
- Quantum Stein：arXiv 2510.08672，形式化修正后的 quantum hypothesis-testing theorem。

## 证据边界
- 论文页、官方 README、toolchain、关键文件已读取，主要为 E1/E2。
- 本轮没有 clean clone 或执行外部项目 lake build，外部项目构建均 NOT_RUN。
- 搜索引擎缓存与 GitHub 当前源文件存在时点差异，统计采用 GitHub 当前文件并明确保留旧快照。
- 本轮没有修改 AI_Trader #488；没有将数学定理宣传为经验金融策略有效性。

## 当前唯一下一步
按每个领域选 1–2 个代表项目做项目级审计：固定 commit、LICENSE、toolchain、manifest、关键 theorem、sorry/axiom/opaque、CI 和 build log。优先 Mathlib/BrownianMotion/MathFin、LeanInfoTheory/rate_distortion/AI4SLT、Veil/Loom/CertifyingDatalog、TorchLean/DynamicalSystems。外部项目不能一次性全量构建；每个项目必须有明确验收边界。


## CI 回归与链接修复（2026-11-23）

- 首次对本轮矩阵 head 执行知识库完整性检查时失败：`sessions/README.md` 指向不存在的 `2026-11-22-cross-domain-evidence-map.md`。
- 已将链接修正为本轮真实文件 `2026-11-23-cross-domain-direction-paper-project-map.md`。
- 修复后 PR head `c45e6d94e30a45bb797019f201baac20d4c17eb8` 的 Knowledge-base integrity Run #1268 成功。
- 同一 head 的 Lean PIT no-lookahead Run #37 成功：Lean 4.35.0 `lake build` 完成；两个 theorem 均编译，axiom 输出均为 `[propext]`。
- 这是本专题 PIT 示例的持续 CI 复验，不代表外部 MathFin/AI4SLT/Veil 等项目已构建；外部项目 build 仍 NOT_RUN。


- 后续更新到最新 PR head `5f84a4ade251cf5ef769e561edfd0ef5c218973f` 后，再次通过 [Knowledge-base integrity Run #1271](https://github.com/fweiger/AI_book/actions/runs/45043181807) 与 [Lean PIT Run #40](https://github.com/fweiger/AI_book/actions/runs/45043181814)。Lean 4.35.0 build completed successfully (3 jobs)，两个 theorem 的 axioms 均为 `[propext]`。因此最新 head 的文档完整性与 PIT workflow 均 PASS。
