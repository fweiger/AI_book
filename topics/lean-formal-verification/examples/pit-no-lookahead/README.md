# PIT / No-Lookahead: minimal Lean proof

## What this proves

The model separates:
- `eventTime`: when the market event occurred;
- `availableAt`: when the strategy could first observe this record;
- `decisionTime`: the strategy's decision timestamp.

The eligibility filter admits a record only when `availableAt ≤ decisionTime`. The Lean theorem `eligibleRows_no_lookahead` proves that every admitted row satisfies that condition. A concrete late-revision example has `eventTime = 1`, `availableAt = 3`, and `decisionTime = 2`; it is excluded even though the event itself predates the decision.

## Build

From this directory:

```bash
lake build
```

Lean toolchain is pinned in `lean-toolchain`; this example has no Mathlib dependency.

## Explicit limits

This is an eligibility-filter proof, not a complete as-of join:
- it does not choose the latest eligible revision;
- it does not prove input rows are sorted;
- it does not define duplicate-revision tie-breaking, null handling, or vendor corrections;
- it assumes `availableAt` timestamps are truthful and correctly sourced;
- it does not prove predictive alpha, backtest validity, or profitability.

The next extension should specify deterministic latest-version selection under an explicit ordering and prove its output is still available at decision time. This example does not modify AI_Trader #488.
