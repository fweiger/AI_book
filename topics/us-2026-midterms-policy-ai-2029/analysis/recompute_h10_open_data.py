#!/usr/bin/env python3
"""TOPIC-011 H10 offline reproducibility check; Python standard library only.

Default: read companion CSV from ../data.
Run standalone over supplied files: python recompute_h10_open_data.py --stdin-json
where stdin JSON object contains keys cpi, rates, pce, fomc with full CSV text.

The dataset is a 2026-11-14 RETROSPECTIVE SNAPSHOT, not a historical PIT
market-consensus archive. The test checks arithmetic and publication-order,
not Fed reaction causality or expected rate changes.
"""
from __future__ import annotations

import csv
import io
import json
import sys
from pathlib import Path

DATA = {
    "cpi": "h10_bls_cpi_sa_monthly_2025_2026.csv",
    "rates": "h10_us_treasury_2y_10y_daily_2025_2026.csv",
    "pce": "h10_bea_pce_release_vintages_2026.csv",
    "fomc": "h10_fomc_official_decisions_2026.csv",
}


def load():
    if "--stdin-json" in sys.argv:
        inputs = json.load(sys.stdin)
    else:
        d = Path(__file__).resolve().parent.parent / "data"
        inputs = {k: (d / v).read_text(encoding="utf-8") for k, v in DATA.items()}
    result = {}
    for key in DATA:
        if key not in inputs or not inputs[key]:
            raise AssertionError(f"missing file: {key}")
        r = list(csv.DictReader(io.StringIO(inputs[key])))
        if not r or not all(r[0].keys()):
            raise AssertionError(f"bad CSV {key}")
        result[key] = r
    return result


def f(value):
    return None if value in ("", "-", None) else float(value)


def near(a, b, tol=0.00011):
    assert abs(a-b) <= tol, (a,b)


def analyze():
    raw = load()
    c = {r["period"]: r for r in raw["cpi"]}
    r = {r["date"]: r for r in raw["rates"]}
    p = {(x["reference_month"], x["variable"], x["vintage"]): x for x in raw["pce"]}
    m = {x["decision_date"]: x for x in raw["fomc"]}
    assert len(c) == 22 and len(r) == 467
    assert c["2025-10"]["headline_cpi_sa_index"] == ""
    assert c["2025-10"]["core_cpi_sa_index"] == ""
    assert c["2026-10"]["headline_yoy_pct_from_index"] == ""
    assert c["2026-10"]["core_yoy_pct_from_index"] == ""
    h10 = 100 * (f(c["2026-10"]["headline_cpi_sa_index"]) / f(c["2026-09"]["headline_cpi_sa_index"]) - 1)
    h09 = 100 * (f(c["2026-09"]["headline_cpi_sa_index"]) / f(c["2026-08"]["headline_cpi_sa_index"]) - 1)
    core10 = 100 * (f(c["2026-10"]["core_cpi_sa_index"]) / f(c["2026-09"]["core_cpi_sa_index"]) - 1)
    core3m_annualized = 100 * ((f(c["2026-10"]["core_cpi_sa_index"]) /
                              f(c["2026-07"]["core_cpi_sa_index"])) ** 4 - 1)
    near(h10, float(c["2026-10"]["headline_mom_pct_from_index"]))
    near(h09, float(c["2026-09"]["headline_mom_pct_from_index"]))
    near(core10, float(c["2026-10"]["core_mom_pct_from_index"]))
    assert round(h10, 1) == 0.4, h10
    assert round(h09, 1) == 0.6, h09
    assert round(core10, 1) == 0.3, core10

    nov9, nov10 = r["2026-11-09"], r["2026-11-10"]
    two_bp = 100 * (f(nov10["treasury_2y_pct"]) - f(nov9["treasury_2y_pct"]))
    ten_bp = 100 * (f(nov10["treasury_10y_pct"]) - f(nov9["treasury_10y_pct"]))
    near(two_bp, 17)
    near(ten_bp, 10)
    assert "2026-11-11" not in r  # Holiday; never forward-fill.
    assert p[("2026-08","core_pce_mom","FIRST_RELEASE")]["release_date"] == "2026-09-30"
    orig = float(p[("2026-08","core_pce_mom","FIRST_RELEASE")]["month_change_pct_official"])
    rev = float(p[("2026-08","core_pce_mom","REVISED_IN_SEPT_RELEASE")]["month_change_pct_official"])
    near(orig, 0.2)
    near(rev, 0.3)
    assert p[("2026-09","core_pce_mom","FIRST_RELEASE")]["release_date"] == "2026-10-29"
    assert m["2026-09-16"]["target_change_bp"] == "25"
    assert m["2026-10-28"]["target_change_bp"] == "0"
    assert "2026-10-29" > "2026-10-28"  # September PCE not public at Oct 28 meeting.
    assert "2026-11-10" > "2026-10-28"  # October CPI not public at Oct 28 meeting.
    return {
        "data_snapshot_date": "2026-11-14",
        "cpi_months": len(c), "cpi_nonempty_months": sum(x["headline_cpi_sa_index"] != "" for x in c.values()),
        "treasury_daily_rows": len(r), "treasury_2025_rows": sum(k.startswith("2025-") for k in r),
        "treasury_2026_rows": sum(k.startswith("2026-") for k in r),
        "cpi_oct2025_missing": True,
        "cpi_oct2026_headline_mom_pct_computed": round(h10, 4),
        "cpi_oct2026_core_mom_pct_computed": round(core10, 4),
        "cpi_sep2026_headline_mom_pct_computed": round(h09, 4),
        "core_cpi_oct2026_3mo_annualized_pct_not_yoy": round(core3m_annualized, 4),
        "bea_aug2026_core_pce_first_release_pct": orig,
        "bea_aug2026_core_pce_later_vintage_pct": rev,
        "bea_aug_revision_percentage_points": round(rev - orig, 4),
        "bea_sep2026_core_pce_first_release_pct": float(p[("2026-09","core_pce_mom","FIRST_RELEASE")]["month_change_pct_official"]),
        "treasury_2y_nov9_pct": f(nov9["treasury_2y_pct"]),
        "treasury_2y_nov10_pct": f(nov10["treasury_2y_pct"]),
        "treasury_10y_nov9_pct": f(nov9["treasury_10y_pct"]),
        "treasury_10y_nov10_pct": f(nov10["treasury_10y_pct"]),
        "treasury_2y_nov9_to_nov10_bp": round(two_bp, 2),
        "treasury_10y_nov9_to_nov10_bp": round(ten_bp, 2),
        "two_ten_slope_nov9_bp": f(nov9["10y_minus_2y_bp"]),
        "two_ten_slope_nov10_bp": f(nov10["10y_minus_2y_bp"]),
        "fomc_sep16_change_bp": int(m["2026-09-16"]["target_change_bp"]),
        "fomc_oct28_change_bp": int(m["2026-10-28"]["target_change_bp"]),
        "key_causal_limitation": "There is no timestamped consensus and no corporate debt panel. Daily co-movement is NOT CPI or political causal attribution.",
        "validation": "PASS",
    }


if __name__ == "__main__":
    print(json.dumps(analyze(), ensure_ascii=False, indent=2))
