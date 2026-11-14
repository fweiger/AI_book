#!/usr/bin/env python3
"""TOPIC-011 M0: recompute the descriptive pre-election fiscal/AI baselines.

This script deliberately uses committed snapshots, no external packages, and NO
forward prediction. Official source URL + extraction metadata are in the CSVs.
Run from any working directory: python3 analysis/recompute_m0.py
"""
from __future__ import annotations

import csv
import json
from pathlib import Path
from statistics import median

ROOT = Path(__file__).resolve().parents[1]
def read_csv(name: str) -> list[dict[str, str]]:
    with (ROOT / "data" / name).open(encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))

def f(row: dict, key: str) -> float:
    return float(row[key])

def main() -> int:
    t = read_csv("treasury_october_2015_2026.csv")
    assert len(t) == 12, "Expected 2015..2026 October snapshots"
    assert [int(row["report_month"][:4]) for row in t] == list(range(2015, 2027))
    assert len(set(x["report_month"] for x in t)) == len(t)
    for row in t:
        if abs(f(row, "outlays_usd_bn") - f(row, "receipts_usd_bn") - f(row, "deficit_usd_bn")) > 0.004:
            raise ValueError("MTS deficit is not receipts/outlays reconciled")
    last, prior = t[-1], t[-2]
    delta_d = f(last,"deficit_usd_bn") - f(prior,"deficit_usd_bn")
    delta_o = f(last,"outlays_usd_bn") - f(prior,"outlays_usd_bn")
    delta_r = f(last,"receipts_usd_bn") - f(prior,"receipts_usd_bn")
    assert abs(delta_d - (delta_o - delta_r)) < 0.005
    assert abs(delta_d - 119.714) < 0.005
    assert f(last,"deficit_usd_bn") == max(f(x,"deficit_usd_bn") for x in t)
    def pc(new: float, old: float) -> float: return 100 * (new / old - 1)
    a = read_csv("capex_pre_election_2026.csv")
    byid = {r["record_id"]:r for r in a}
    assert len(a) == len(byid)
    assert all(r["public_date"] <= r["PIT_cutoff"] == "2026-11-02" for r in a)
    meta = byid["META-CY2026"]
    m_now=(f(meta,"lower_usd_bn")+f(meta,"upper_usd_bn"))/2
    m_prior=(f(meta,"previous_lower_usd_bn")+f(meta,"previous_upper_usd_bn"))/2
    orcl=byid["ORCL-FY2027-Q1"]
    g=byid["ORCL-FY2027"]
    o_now=f(orcl,"lower_usd_bn")
    o_prior=f(orcl,"previous_lower_usd_bn")
    historical=[f(x,"deficit_usd_bn") for x in t]
    output = {
        "basis": "Oct MTS month-by-month nominal report snapshots; 2026-11-14 extraction",
        "october_years": len(t),
        "oct_2026": {
            "receipts_bn":f(last,"receipts_usd_bn"),
            "outlays_bn":f(last,"outlays_usd_bn"),
            "deficit_bn":f(last,"deficit_usd_bn"),
            "yoy_deficit_delta_bn":round(delta_d,3),
            "yoy_deficit_percent":round(pc(f(last,"deficit_usd_bn"),f(prior,"deficit_usd_bn")),2),
            "yoy_outlays_percent":round(pc(f(last,"outlays_usd_bn"),f(prior,"outlays_usd_bn")),2),
            "yoy_receipts_percent":round(pc(f(last,"receipts_usd_bn"),f(prior,"receipts_usd_bn")),2),
            "contribution_outlays_delta_bn":round(delta_o,3),
            "contribution_receipts_decline_bn":round(-delta_r,3),
            "raw_nominal_rank_descending":1 + sum(v > historical[-1] for v in historical),
            "historical_oct_median_bn":round(median(historical),3),
            "caveat": "Unadjusted nominal dollars: not a cyclically adjusted fiscal impulse and not post-election activity",
        },
        "pre_election_company_guidance": {
            "META_CY2026_midpoint_now_bn":m_now,
            "META_CY2026_midpoint_prior_bn":m_prior,
            "META_midpoint_revision_percent":round(pc(m_now,m_prior),2),
            "ORCL_FY2027_Q1_cash_capex_bn":o_now,
            "ORCL_FY2026_Q1_cash_capex_bn":o_prior,
            "ORCL_Q1_yoy_percent":round(pc(o_now,o_prior),2),
            "ORCL_FY2027_gross_capex_guidance_bn":[f(g,"lower_usd_bn"),f(g,"upper_usd_bn")],
            "ORCL_FY2027_guidance_vs_FY2026_actual_percent_range":[round(pc(f(g,"lower_usd_bn"),f(g,"previous_lower_usd_bn")),2),round(pc(f(g,"upper_usd_bn"),f(g,"previous_upper_usd_bn")),2)],
            "companies_in_snapshot":sorted(set(r["company"] for r in a)),
            "comparable_2027_CAPEX_revision_index":None,
            "caveat":"Different accounting/calendar and gross/net measurements; Oracle 90-95 guidance via call transcription pending original audio cross-check; cannot sum as AI-only CAPEX",
        },
        "causal_status":"UNTESTED"
    }
    print(json.dumps(output, ensure_ascii=False,indent=2))
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
