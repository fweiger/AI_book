#!/usr/bin/env python3
"""CASE-PRT-001: independent arithmetic QA of 2008 vs 2025 gold compilations.

The script reads only short, citable CSV tables stored in the same directory.
It cannot establish original-archive truth, public-debt causal effects or ASCM.
Usage: python3 audit_gold_sources_and_debt_m2.py [--input-dir ./data_m2]
"""
from __future__ import annotations
import argparse
import csv
import json
import math
from pathlib import Path


def read(path: Path) -> list[dict]:
    with path.open(encoding="utf-8", newline="") as stream:
        return list(csv.DictReader(stream))


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--input-dir", type=Path, default=Path(__file__).resolve().parent)
    args = ap.parse_args()
    base = args.input_dir

    gold_old = read(base / "sousa_2008_manifestos_5year_m2.csv")
    gold_new = read(base / "gold_remittances_fiveyear_b1_1720_1804_m2.csv")
    decadal_old = read(base / "sousa_2008_decadal_gold_private_public_m2.csv")
    debt = read(base / "sovereign_debt_2024_crosscountry_benchmarks_m2.csv")
    debtservice = read(base / "sovereign_debt_service_2024_benchmarks_m2.csv")

    assert len(gold_old) == len(gold_new) == 17
    assert len(decadal_old) == 9
    assert len(debt) == 7 and len(debtservice) == 8
    oldtotal, newtotal, matched_abs = 0, 0, []
    matched = []
    for idx, (old, new) in enumerate(zip(gold_old, gold_new)):
        os, oe = int(old["start_year"]), int(old["end_year"])
        ns, ne = int(new["year_start"]), int(new["year_end"])
        assert os == ns == 1720 + 5 * idx
        if idx < 16:
            assert oe == ne == os + 4
        else:
            assert oe == 1807 and ne == 1804
        oldv, newv = int(old["manifestos_million_reis"]), int(new["total_nominal_million_reis"])
        assert newv == int(new["private_nominal_million_reis"]) + int(new["public_nominal_million_reis"])
        oldtotal += oldv
        newtotal += newv
        if oe == ne:
            matched.append((os, oe, oldv, newv, newv - oldv))
            matched_abs.append((abs(newv - oldv), os))
    assert oldtotal == 270804  # printed article narrative says 270803; 1 conto discrepancy
    assert newtotal == 271045
    assert len(matched) == 16
    assert max(matched_abs) == (1726, 1780)
    assert next(x for x in matched if x[0] == 1780)[4] == -1726

    old_1780 = next(x for x in decadal_old if x["period"] == "1780-1789")
    reported_old_state_annual = int(old_1780["state_average_annual_contos"])
    new_1780_public_ten_year = sum(int(r["public_nominal_million_reis"]) for r in gold_new
                                   if 1780 <= int(r["year_start"]) <= 1789)
    assert reported_old_state_annual == 482 and new_1780_public_ten_year == 3093
    delta_1780_public = new_1780_public_ten_year - reported_old_state_annual * 10
    assert delta_1780_public == -1727  # 1 conto rounding in published 2008 decadal average

    a = {int(r["year"]): r for r in debt}
    assert (int(a[1748]["portugal_debt_stock_pct_gdp"]),
            int(a[1748]["england_debt_stock_pct_gdp"]),
            int(a[1748]["holland_province_debt_stock_pct_gdp"])) == (9,109,233)
    assert (int(a[1763]["portugal_debt_stock_pct_gdp"]),
            int(a[1763]["england_debt_stock_pct_gdp"])) == (9,177)
    sv = {int(r["year"]): float(r["portugal_debt_service_share_state_expenditure_pct"])
          for r in debtservice}
    assert math.isclose(sv[1680], 22.9) and math.isclose(sv[1766], 7.6)
    result = {
        "case": "CASE-PRT-001",
        "status": "PASSED_PUBLISHED_TABLE_ARITHMETIC_ONLY",
        "manifestos_2008_table1_sum_contos": oldtotal,
        "manifestos_2008_narrative_sum_contos": 270803,
        "manifestos_2025_appendix_B1_sum_contos": newtotal,
        "matching_5year_windows": len(matched),
        "unmatched_last_window_2008": "1800-1807",
        "unmatched_last_window_2025": "1800-1804",
        "largest_matched_discrepancy_period": "1780-1784",
        "largest_matched_discrepancy_2025_minus_2008_contos": -1726,
        "largest_matched_discrepancy_pct": round(100 * -1726 / 8727, 6),
        "sousa2008_1780s_public_annual_contos": reported_old_state_annual,
        "k2025_1780s_public_total_contos": new_1780_public_ten_year,
        "old_decadal_vs_new_public_1780s_difference_contos": delta_1780_public,
        "portugal_debt_gdp_1748_pct": 9,
        "england_debt_gdp_1748_pct": 109,
        "holland_province_debt_gdp_1748_pct": 233,
        "portugal_debt_service_1680_pct_of_expenses": 22.9,
        "portugal_debt_service_1766_pct_of_expenses": 7.6,
        "model_ASCM": "NOT_RUN",
        "original_archival_ledger_independent_check": "NOT_RUN",
    }
    print(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
