#!/usr/bin/env python3
"""Reproduce TOPIC-011 H03 baseline. No third-party packages and no network.
PJM official 2026 vs 2025 forecast changes, Virginia hypothetical tax exposures.
Run: python3 analysis/recompute_h03_m0.py
"""
from __future__ import annotations
import csv, json
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
def load(n):
    with (ROOT/"data"/n).open(encoding="utf-8",newline="") as fh:
        return list(csv.DictReader(fh))
def almost(a,b,eps=1e-6):
    assert abs(a-b)<eps,(a,b)
def main():
    p=load("h03_policy_events_2026.csv")
    assert len(p)==8
    assert len(set(v["policy_id"] for v in p))==len(p)
    assert sum(v["status_asof_2026_11_14"]=="ENACTED_ACTIVE" for v in p)==3
    assert all(v["realized_project_delay_mw"]=="UNKNOWN" for v in p)
    assert all(v["enacted_before_midterm"]=="YES" for v in p[:5])
    assert p[-2]["status_asof_2026_11_14"]=="PROCEDURAL_VOTE_PASSED_73_25"
    assert p[-1]["status_asof_2026_11_14"]=="PROCEDURAL_VOTE_PASSED_62_21"
    a=load("h03_pjm_forecast_revisions_2026.csv")
    assert len(a)==6
    for r in a:
        new=int(r["pjm_2026_jan_forecast_summer_peak_mw"])
        change=int(r["change_vs_pjm_2025_forecast_mw"])
        old=int(r["pjm_2025_implied_forecast_mw"])
        assert new-old==change
        almost(100*change/old,float(r["pct_change_calculated"]),0.001)
        assert "NOT_DATACENTER_ONLY" in r["limits"]
    s=load("h03_va_electricity_tax_scenarios.csv")
    assert len(s)==9
    for r in s:
        cap=float(r["capacity_mw"]); load=float(r["average_utilization_fraction"])
        kwh=cap*1e3*8760*load
        almost(kwh,float(r["electricity_kwh_year"]))
        amt=kwh*float(r["rate_usd_kwh"])
        almost(amt,float(r["annualized_va_tax_usd"]))
        almost(amt/1e6,float(r["annualized_va_tax_usd_million"]))
    one=[r for r in s if r["capacity_mw"]=="100" and r["average_utilization_fraction"]=="0.9"][0]
    v={
      "policy_rows":len(p),
      "active_pre_election_law_rows":sum(r["status_asof_2026_11_14"]=="ENACTED_ACTIVE" for r in p),
      "baaja_bill_enacted":False,
      "baaja_cloture_vote":"73-25",
      "2027_PJM_summer_peak_revision_MW":-3735,
      "2028_PJM_summer_peak_revision_MW":-4414,
      "2029_PJM_summer_peak_revision_MW":-4564,
      "example_va_100MW_90pct_utilization_annualized_tax_USD":float(one["annualized_va_tax_usd"]),
      "reliable_datacenter_specific_project_cancellation_estimate_MW":None,
      "causal_status":"UNTESTED",
      "note":"PJM total summer peak forecast revision ≠ data center-only or realized decline. Virginia tax is assumed scenario only. BAAJA not law."
    }
    print(json.dumps(v,indent=2,ensure_ascii=False))
if __name__=="__main__":
    main()
