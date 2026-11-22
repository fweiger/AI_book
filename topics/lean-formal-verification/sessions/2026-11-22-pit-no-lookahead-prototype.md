# 2026-11-22｜PIT / No-Lookahead 最小 Lean 规格原型

## 目标

在 AI_book TOPIC-018 内建立独立、可复现的最小 Lean 4 proof，不修改 AI_Trader #488。验证“记录可得时间不得晚于策略决策时间”这一程序级 invariant。

## 已建立资产

- `topics/lean-formal-verification/examples/pit-no-lookahead/lean-toolchain`：Lean 4.35.0。
- `lakefile.lean`：无 Mathlib 依赖的独立 Lake package。
- `PITNoLookahead.lean`：Observation 结构区分 eventTime、availableAt、value；eligibleRows 只按 availableAt 过滤。
- `eligibleRows_no_lookahead`：证明所有输出记录满足 availableAt ≤ decisionTime。
- `late_available_revision_excluded`：证明晚到修订即使 eventTime 较早也会被排除。
- 具体示例：eventTime=1、availableAt=3、decisionTime=2，决策时点不可见。
- `.github/workflows/lean-pit-no-lookahead.yml`：PR path-filtered workflow，安装 Elan 并在该目录运行 `lake build`。

## 限制

- 本轮尚未读取到专用 workflow 完成记录，build = NOT_RUN，不能称为 PASS。
- 只证明 filter safety，不证明 latest eligible revision、排序、重复版本 tie-break、空值、来源 timestamp authenticity 或完整 as-of join。
- 没有连接真实行情或 Level2 数据；没有改动 AI_Trader #488。
- 当前运行环境没有 Lean/Lake/Elan，因此必须依赖 GitHub Actions 回读实际 build 结果。

## 下一步

读取 PR #75 最新 head 的 `Lean PIT no-lookahead proof` workflow run 和 job 结果；若失败，按实际 Lean 编译错误修复；若通过，再增加 latest eligible revision 的显式排序/选择规范，而不是直接扩展到生产数据。

## Post-run verification (2026-11-22)

- GitHub Actions [Lean PIT no-lookahead proof Run #15](https://github.com/fweiger/AI_book/actions/runs/45031340887) completed successfully.
- Job: `build`; step `Build with pinned Lean toolchain`: success.
- Log: Lean 4.35.0 installed; Lake built `PITNoLookahead`; `Build completed successfully (3 jobs)`.
- `#print axioms PITNoLookahead.eligibleRows_no_lookahead` → `[propext]`.
- `#print axioms PITNoLookahead.late_available_revision_excluded` → `[propext]`.
- The proof uses the standard propositional extensionality axiom only; no `sorryAx`, no user-declared axiom, and no `Classical.choice` were reported.
- This is E2 for the minimal eligibility filter proof. It does not promote the full as-of join or any external data timestamp to verified status.
