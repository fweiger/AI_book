#!/usr/bin/env python3
"""TOPIC-010 M3C: reproduce Crafts (2010) Table 1 IRRs and scenario sensitivity.

Historical source: https://wrap.warwick.ac.uk/id/eprint/44710/1/WRAP_Carfts_10.2010_craftsindustrial.pdf
Underlying original model: https://www.nuff.ox.ac.uk/Users/Allen/unpublished/jenny5-dp.pdf

Python >=3.9; stdlib only. CSV values are published study assumptions, not
archival observed company cash flow; this script tests model arithmetic ONLY.
"""
from __future__ import annotations

import csv
import json
import math
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent

def read_rows(name: str) -> list[dict[str, str]]:
    with (HERE / name).open("r", encoding="utf-8-sig", newline="") as f:
        rd = csv.DictReader(f)
        if not rd.fieldnames:
            raise ValueError(f"{name}: missing CSV header")
        rows = list(rd)
    if not rows or any(None in r for r in rows):
        raise ValueError(f"{name}: missing/extra CSV fields")
    return rows

def irr(cost: float, wage: float, days: float = 250, fraction: float = 0.4,
        productivity: float = 3, life: int = 10, maintenance: float = 0.1) -> float:
    if (cost <= 0 or wage < 0 or days <= 0 or not (0 < fraction <= 1)
            or productivity <= 1 or life < 1 or not (0 <= maintenance < 1)):
        raise ValueError("invalid capital, wage, utilization, productivity, or lifetime")
    saved = days * fraction * (1 - 1 / productivity)
    flow = wage * saved - cost * maintenance
    def npv(r: float) -> float:
        return -cost + sum(flow / (1 + r) ** t for t in range(1, life + 1))
    low, high = -0.99, 4.0
    if npv(low) <= 0 or npv(high) >= 0:
        raise ValueError("IRR root not bracketed in (-99%,400%); inputs out of scope")
    for _ in range(120):
        midpoint = (low + high) / 2
        if npv(midpoint) > 0:
            low = midpoint
        else:
            high = midpoint
    return (low + high) / 2

def main() -> None:
    grid = read_rows("jenny_crafts_2010_4x3_irr_published_vs_replication_m3c.csv")
    scenarios = read_rows("jenny_allen_crafts_counterfactual_utilization_m3c.csv")
    if len(grid) != 12 or len(scenarios) != 4:
        raise AssertionError("expected exactly 12 Crafts grid cells and 4 scenarios")
    if len({r["grid_id"] for r in grid}) != 12:
        raise AssertionError("duplicate published cell IDs")
    if len({r["scenario_id"] for r in scenarios}) != 4:
        raise AssertionError("duplicate scenario IDs")
    maximum_error = 0.0
    for row in grid:
        got = 100 * irr(float(row["machine_cost_pence"]), float(row["daily_wage_pence"]))
        maximum_error = max(maximum_error, abs(got - float(row["published_irr_percent"])))
        if abs(got - float(row["recomputed_irr_percent"])) > 1e-5:
            raise AssertionError(f'GitHub-derived grid mismatch: {row["grid_id"]}')
    if maximum_error > 0.52:
        raise AssertionError(f"Crafts published-vs-calculated deviation {maximum_error:.4f}pp > tolerance0.52pp")
    results = {}
    for row in scenarios:
        got = 100 * irr(float(row["jenny_cost_pence"]),float(row["wage_pence_day"]),
                        float(row["calendar_work_days"]),float(row["part_time_fraction"]),
                        float(row["productivity_multiplier"]),int(row["asset_life_years"]),
                        float(row["annual_maintenance_share_of_capex"]))
        if abs(got-float(row["computed_irr_percent"])) > 1e-5:
            raise AssertionError(f'Scenario mismatch: {row["scenario_id"]}')
        expected = "MODEL_PASS" if got >= float(row["discount_hurdle_percent"]) else "MODEL_FAIL"
        if row["model_adoption_pass"] != expected:
            raise AssertionError(f'Adoption threshold mismatch: {row["scenario_id"]}')
        results[row["scenario_id"]] = round(got, 4)
    hurdle = 0.15
    annuity = sum((1 + hurdle)**(-year) for year in range(1, 11))
    labor_saved = 250 * 0.4 * (1 - 1/3)
    threshold_j = 4.66 * labor_saved/(0.1 + 1/annuity)
    threshold_w_france = 1450 * (0.1 + 1/annuity)/labor_saved
    threshold_w_britain = 840 * (0.1 + 1/annuity)/labor_saved
    if not (1038 < threshold_j < 1039 and 6.50 < threshold_w_france < 6.52
            and 3.76 < threshold_w_britain < 3.78):
        raise AssertionError("analytical break-even thresholds fail")
    print(json.dumps({
      "status": "PASS_PUBLISHED_MODEL_ARITHMETIC_ONLY",
      "published_grid_rows": len(grid),
      "scenario_rows": len(scenarios),
      "max_reproduction_difference_percentage_points": round(maximum_error, 4),
      "scenarios_irr_percent": results,
      "required_machine_price_at_french_wage_pence": round(threshold_j, 4),
      "required_french_wage_at_french_machine_price_pence": round(threshold_w_france, 4),
      "minimum_britain_wage_at_british_machine_price_pence": round(threshold_w_britain, 4),
      "historical_factory_ledger": "NOT_ACQUIRED",
      "independent_2009_empirical_reproduction": "NOT_RUN",
      "multi_country_causal_adoption_model": "NOT_RUN"
    }, ensure_ascii=False, indent=2))

if __name__ == "__main__":
    try:
        main()
    except (AssertionError, ValueError, OSError) as err:
        print(json.dumps({"status": "FAIL", "error": str(err)}, ensure_ascii=False), file=sys.stderr)
        sys.exit(1)
