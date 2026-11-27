# 2026-11-22｜MathFin 数学金融库与量化形式化方法审查

## 固定快照

仓库：`formal-applied-math/formal-mathfin`  
commit：`cbe842dda1e71fd7173f3325971796686dbf7feb`  
Lean：`leanprover/lean4:v4.35.0`  
Mathlib：`e91b128082cc221d6432a6a5aadcd3243af8e76c`  
BrownianMotion：`497e5e2a60450796f75ab920e6c33addae4d644d`

## 实际读取和交叉核验

- README、coverage/glossary、lakefile、manifest、build.yml、reproduce.sh、AxiomAudit、AxiomAuditGen、CVaR、Markowitz、CRR、GaussianRiskReport 等源码/文档。
- README 报告 906 项 corpus：866 full、18 library_wrapper、22 reduced_core。本轮独立解析 risk_measures.json（49）、portfolio_and_performance.json（67）、binomial.json（40），156 项均标记 full。
- AxiomAuditGen 声明覆盖 1,115 个 MathFin 常量与 29 个上游常量，使用 1,144 个 #print axioms guard pin exact dependency set；项目默认 build workflow 含 Python gates + lake build + declaration index/ratchet。
- README/coverage 明确区分 full、library_wrapper、reduced_core、placeholder；只有 full + wrapper 计入交付就绪。

## 三个主要金融数学案例

1. Gaussian CVaR：Rockafellar-Uryasev variational theorem，使用 pointwise certificate `(L-c)^+ ≥ (L-c) 1_{Z>z}` 积分证明全局最小性；Gaussian loss 条件。
2. Markowitz：PSD covariance + budget/target-return constraints + Lagrangian FOC ⇒ global minimum variance；只证明充分性，不证明必要性。
3. CRR→Black-Scholes：characteristic function / cos-sin asymptotics / Lévy continuity / bounded put payoff / put-call parity；证明 distributional and call-price convergence。

## 形式化质量发现

CRR Call convergence benchmark 记录了 2026-08-20 的一次重要修正：原 no-arbitrage hypothesis 量化到 n=0，但 n=0 时 u=d=1，假设不可能成立，定理会 vacuously true。修正后限制 n≥1，并给出 `|r|√T<σ` 足以满足 no-arbitrage 的证明。该例说明必须审查 hypothesis satisfiability。

## 对 A 股量化研究的边界映射

MathFin 的数学定理可以提供模型层基础，但不证明市场数据真实性、因子有效性或策略盈利。对 AI_Trader #488，Lean 候选用途是证明 availableAt/decisionTime、as-of filter、point-in-time universe、feature/label 时序隔离、订单/持仓/现金状态机和风险约束；Python 仍负责真实数据、数值计算、统计检验、交易成本与样本外回测。此映射尚未实现，未接管 #488。

## 构建状态与限制

- MathFin 有 build.yml 和 scripts/reproduce.sh，但本轮 GitHub wrapper 未返回该 commit 的 PR workflow run/status；该 wrapper 仅筛选 PR-triggered runs，空结果不能解释为没有 CI。
- 本轮执行环境没有 Lean/Lake/Elan；MathFin build = NOT_RUN。
- 没有独立复现 906 条 corpus；只解析了三个 JSON 文件 156 条。
- 未独立运行 #print axioms；静态读取 AxiomAuditGen 不能代替 build。
- MathFin 的 `MathFinFrontier` 和 Palomar `Challenge` 有单独用途，不能与核心 MathFin 库的证明状态混为一谈。

## 新增资产

- M-08 至 M-13：形式化保真度、生成式公理审计、CVaR 点态证书、CRR 特征函数收敛、Markowitz KKT 充分性、假设非空性。
- C018-026 至 C018-033；图谱升级到 0.5.0，新增 Q09。
- 新增 PIT/no-lookahead 作为候选 formalization design，不计入已完成 proof methods。

## 当前唯一下一步候选

建立一个独立的最小 Lean 4.35.0 PIT/no-lookahead 规格示例：把 eventTime、availableAt 和 decisionTime 分开；证明任何通过 eligible filter 的记录都满足 availableAt ≤ decisionTime，并用“事件发生早但数据晚到”的修订样例验证 eventTime 不能代替 availableAt。只在 AI_book 专题分支建立示例，不修改 AI_Trader #488；之后用 GitHub Actions 运行 lake build，build 前不报告 PASS。
