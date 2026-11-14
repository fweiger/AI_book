#!/usr/bin/env python3
"""TOPIC-010 M3C: reproduce Crafts (2014) Table 9 model IRRs.

Source: https://warwick.ac.uk/fac/soc/economics/research/centres/cage/manage/publications/214-2014_crafts.pdf
Model assumptions from Allen/Crafts: P=3; jenny lifetime=10 years;
annual maintenance=10% of machinery purchase price; full-day-equivalent annual
working time=100. No historical factory returns or national treatment effects.
"""
from __future__ import annotations
import csv
import math
import sys
from pathlib import Path

CSV_NAME = "uk_france_spinning_jenny_irr_counterfactual_m3c.csv"

def npv(r: float, machine_price: float, annual_net_saving: float, years: int = 10) -> float:
    return -machine_price + sum(
        annual_net_saving / ((1.0 + r) ** year)
        for year in range(1, years + 1)
    )

def compute_irr(wage: float, price: float, days: float,
                productivity_multiplier: float = 3.0,
                annual_maintenance_rate: float = 0.10, years: int = 10) -> float:
    if wage <= 0 or price <= 0 or days <= 0 or productivity_multiplier <= 1 or years <= 0:
        raise ValueError("Wage, machine price, workdays and productivity assumptions must be positive")
    net_annual_saving = (wage * days *
                         (1.0 - 1.0 / productivity_multiplier) -
                         annual_maintenance_rate * price)
    lower, upper = -0.99, 100.0
    if npv(lower, price, net_annual_saving, years) <= 0:
        raise ValueError("No IRR root in the tested range")
    for _ in range(250):
        mid = (lower + upper) / 2.0
        if npv(mid, price, net_annual_saving, years) > 0:
            lower = mid
        else:
            upper = mid
    return 100.0 * (lower + upper) / 2.0

def main() -> int:
    path = Path(__file__).with_name(CSV_NAME)
    if not path.is_file():
        raise FileNotFoundError(f"Required source audit file not found: {path}")
    with path.open(newline="", encoding="utf-8") as file:
        rows = list(csv.DictReader(file))
    assert len(rows) == 8
    seen = set()
    for row in rows:
        key = row["scenario"]
        assert key not in seen, f"Duplicate scenario {key}"
        seen.add(key)
        wage = float(row["wage_pence_equivalent_per_full_workday"])
        price = float(row["jenny_price_pence_equivalent"])
        days = float(row["effective_workdays_per_year"])
        value = compute_irr(wage, price, days)
        assert math.isclose(value, float(row["recomputed_irr_pct"]), abs_tol=0.0001)
        pub = row["source_table_reported_irr_pct"]
        if pub:
            # Crafts's displayed model values are rounded and use intermediate historical inputs.
            assert abs(value - float(pub)) <= 0.25, (key, value, pub)
        print(f"{key}, model_IRR={value:.4f}%")
    assert {"UK_BASE", "FR_BASE", "FR_UK_MACHINE_PRICE", "UK_FR_MACHINE_PRICE"}.issubset(seen)
    print("PASS_M3C_MODEL_RECALC; HISTORICAL_MACHINE_ADOPTION_CAUSAL_TEST_NOT_RUN")
    return 0

if __name__ == "__main__":
    try:
        sys.exit(main())
    except (AssertionError, ValueError, OSError) as exc:
        print(f"FAIL_M3C: {exc}", file=sys.stderr)
        sys.exit(1)
