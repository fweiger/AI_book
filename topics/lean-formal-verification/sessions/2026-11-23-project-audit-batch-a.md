# 2026-11-23｜项目审计批次 A：Rate-Distortion、AI4SLT、Veil

## 目标与范围

继续 TOPIC-018 原 Goal，推进 AC-03/AC-05：对论文 companion project 固定 commit，核对 LICENSE、Lean toolchain、Lake manifest、关键 theorem、sorry/axiom/opaque、CI/build evidence 和研究边界。本轮只读外部仓库，不执行 clone/build，不修改 AI_Trader #488。

## 项目一：Rate-Distortion

- Paper: [arXiv:2610.22404](https://arxiv.org/abs/2610.22404)。
- Repo commit: 6ebee5bca945015ec2964ea94148e6de3857959d。
- Files: README、RateDistortion.lean、MainResults.lean、lakefile.toml、lake-manifest.json、lean-toolchain。
- Toolchain: Lean 4.28.0; Mathlib v4.28.0; manifest pins Mathlib.
- License: repo metadata license=null; root LICENSE/COPYING not found in fixed tree.
- Source scan: 4 Lean files; no explicit sorry, top-level axiom, or opaque declarations found.
- MainResults.lean: checks six public result signatures, prints axioms for five endpoints, then runs Lean.collectAxioms against [propext, Classical.choice, Quot.sound].
- Historical build log: file was added in commit 7b9bfcaa42cc0365e7f8d4c1094b8309b61ef269 on 2026-09-22. It reports Lean 4.28.0, 3161 jobs completed, and the five audited theorem endpoints depending only on the allowlisted standard axioms.
- Version drift: RateDistortion.lean was modified again in commit 6ebee5b on 2026-10-13; compare abe3000... → 6ebee5b shows 3 commits ahead and 6393 additions / 6132 deletions to this source file. Thus the September build log is not evidence for current main.
- CI mismatch: fixed current tree contains no .github/workflows file; Actions API returned no run. docs/verification.md says a workflow is included for future pushes/PRs, and README describes Actions checks. Current tree contradicts this documentation.
- Verdict: PARTIAL; source/axiom gate E1, historical build E2 only for old source, current main NOT_RUN; license not found.

## 项目二：AI4SLT

- Paper: [AI4SLT, ICML 2026 / PMLR 306](https://proceedings.mlr.press/v306/zhang26cd.html), arXiv [2602.02285](https://arxiv.org/abs/2602.02285)。
- Repo: [YuanheZ/lean-stat-learning-theory](https://github.com/YuanheZ/lean-stat-learning-theory)。
- Current main commit: d0f506f0a695018265dccb33bcb05e2f5ca1c876。
- Release v4.32.0 commit: 482a1a56daf792b33afe8cf7f07f127dc0af8640; current main is two commits ahead, and compare shows only README modified.
- License: Apache-2.0. Toolchain Lean 4.32.0; Mathlib 4.32.0 pinned to 81a5d257c8e410db227a6665ed08f64fea08e997; lake manifest present; 68 Lean files.
- Core paper objects: Gaussian Lipschitz concentration, Dudley entropy integral for sub-Gaussian processes, least-squares/sparse regression sharp rates.
- Source files inspected: SLT/GaussianLipConcen.lean, SLT/Dudley.lean, SLT/LeastSquares/BasicInequality.lean; key theorem declarations include gaussian_lipschitz_concentration, dudley, and basic_inequality.
- Release v4.32.0 notes report LEAN_NUM_THREADS=$(nproc) lake build success and a scan of SLT/ for sorry, admit, axiom, native_decide finding none.
- Current tree has no .github/workflows and Actions API has no workflow run. This is release build evidence, not CI PASS. Since main differs from release only by README, the Lean code is unchanged from the reported build.
- Verdict: PASS / E2 release build evidence; no continuous CI workflow.

## 项目三：Veil

- Paper: [Veil, CAV 2025](https://doi.org/10.1007/978-3-031-98682-6_2)。
- Repo: [verse-lab/veil](https://github.com/verse-lab/veil), fixed main commit 5a525eeca8cee37b2da8c010552db9b1aae968c2。
- License: Apache-2.0; Lean 4.35.0; Lake package version 1.3.0; 506 Lean files.
- Manifest pins lean-smt, Loom, VerifiedHAMT, Lasso, Lentil, Batteries/Aesop v4.35.0 and ProofWidgets.
- CI: [Run #442](https://github.com/verse-lab/veil/actions/runs/45014566842), event push, head_sha exactly equals audited main commit. Linux-x86_64 and macOS-aarch64 both pass Build Veil, VeilTest, LSP/Widgets, VS Code Extension and Examples.
- lakefile.lean defines VeilTest as test_driver and sets weak.veil.smt.trust=false.
- CI log compiles VeilTest.TrustAudit; seven shipped routes (fair, prune, patOnly, crossing, dijkstra, ndfs, interned) are clean; positive control with one implemented_by is detected; final output PASS.
- TrustAudit.lean recursively inspects constants reachable through types and values, checking project-local unsafe and implemented_by. It is a selected-route audit, not a global repository guarantee.
- Certificate.lean defines standard axioms [propext, Classical.choice, Quot.sound], CertificateResult.kernelChecked and offenders; synthesizer docs say trust mode defaults false. If a solver step cannot be replayed or Kernel rejects it, trusted fallback emits a warning and certificate can depend on sorryAx.
- SCP example: SCP.lean explicitly says liveness is not proved in Veil; it proves intertwined_safe. Background has fields named axiom_0, axiom_1, qi_intertwined, which are abstract model contract fields, not top-level Lean axioms. one_such_Background constructs a concrete Background from FBA.System plus intact/intertwined/inclusion witnesses.
- Original SCP paper [FMBC 2020](https://doi.org/10.4230/OASIcs.FMBC.2020.9) used Ivy + Isabelle/HOL to prove safety and liveness under eventual synchrony for arbitrary but fixed configurations. Veil's Lean example is not equivalent to that full proof.
- Verdict: PASS / E2 for Veil main commit CI and TrustAudit; SCP example is PARTIAL on safety only.

## Cross-domain and finance implications

- Rate-Distortion may support formal constraints for L2 compression, quantized features and representation distortion, but does not prove predictive utility.
- AI4SLT can supply reusable concentration/generalization lemmas for model-complexity and overfitting analysis; it does not prove A-share distributional assumptions or alpha.
- Veil can formalize order/position state machines: no double fills, no negative cash, position caps, valid cancel/replace transitions, and terminal-state/liveness properties. It does not prove exchange data truth or production implementation refinement.
- No changes to AI_Trader #488 were made.

## Evidence and status

- E1: fixed source, toolchain, manifest, license and theorem files read.
- E2: AI4SLT release build evidence; Veil exact-SHA upstream CI and TrustAudit. Rate-Distortion historical build log is E2 only for the September commit.
- E3: NOT_RUN; no external project was independently cloned/built in this environment. Local container has no Lean/Lake/Elan.
- AC-05 remains PARTIAL: this batch adds 2 current-code build/CI-backed project audits and 1 partial project audit. The earlier admission audit has 10 metadata snapshots; Mathlib's bors success is one additional build/CI-backed project. Current count with build/CI evidence is 3, not 10.
- Data-quality note: current claims.md contains C018-001—037; old CHANGELOG referenced C018-038—060, but those claim rows are absent from the current ledger. This batch does not reuse those IDs; it starts at C018-061.
- Current unique next step: audit Mathlib, MathFin and ArkLib at fixed commits, focusing on exact build/CI head SHA, manifest and proof/axiom audit.
