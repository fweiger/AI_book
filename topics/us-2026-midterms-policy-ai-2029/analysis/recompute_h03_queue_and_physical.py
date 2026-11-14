#!/usr/bin/env python3
"""TOPIC-011 H03 v0.1.7: regulatory queue + actual energy audit.
Only compare like-for-like periods and entities. Avoid cross-cohort conversion.
Standard-library-only reproducible calculator for source-backed CSVs.
"""
from __future__ import annotations
import csv,json
from pathlib import Path
R=Path(__file__).resolve().parents[1]
def read(s):
    with (R/"data"/s).open(encoding="utf-8",newline="") as h:return list(csv.DictReader(h))
def val(n):return float(n)
def inc(a,b):return 100*(a/b-1)
def approx(a,b,eps=.006):assert abs(a-b)<eps,(a,b)
queue=read("h03_dominion_scc_queue_cohort.csv")
rules=read("h03_virginia_scc_pre_election_tariff_and_queue_rules.csv")
energy=read("h03_dominion_actual_delivered_mwh_2024_2026.csv")
dcshare=read("h03_dominion_dc_sales_share_annual.csv")
bill=read("h03_gs5_minimum_billed_demand_scenarios.csv")
aep=read("h03_aep_pre_election_security_and_tariff_status.csv")
assert [len(x) for x in [queue,rules,energy,dcshare,bill,aep]]==[4,9,8,2,15,8]
assert len({r["rule_id"] for r in rules})==len(rules)
q={r["recorded_group"]:r for r in queue}
total=val(q["TOTAL_LARGE_LOAD_DP_REQUESTS"]["mw"])
dated=val(q["ASSIGNED_PROJECTED_CONNECTION_DATES_THROUGH_2031"]["mw"])
waiting=val(q["BATCHED_STILL_STUDYING_PROJECTED_DATES"]["mw"])
assert (total,dated,waiting)==(70000,25000,45000)
assert dated+waiting==total
approx(val(q["ASSIGNED_PROJECTED_CONNECTION_DATES_THROUGH_2031"]["pct_of_total_queue"]),dated/total*100,.001)
date_ratio=dated/total*100
assert all(r["policy_status"]=="QUEUE_STANDARDS_NOT_FINAL" for r in queue[:3])
z={(r["period"],r["year"]):r for r in energy}
assert len(z)==len(energy)
for period in ("ANNUAL","Q2","Q3","JAN_SEP"):
    years=("2024","2025") if period=="ANNUAL" else ("2025","2026")
    assert all((period,y) in z for y in years)
assert all(x["population"]=="TOTAL_DOMINION_ENERGY_VIRGINIA_ELECTRICITY_DELIVERED" for x in energy)
annual2024=val(z["ANNUAL","2024"]["delivered"])
annual2025=val(z["ANNUAL","2025"]["delivered"])
ytd2025=val(z["JAN_SEP","2025"]["delivered"])
ytd2026=val(z["JAN_SEP","2026"]["delivered"])
q32025=val(z["Q3","2025"]["delivered"])
q32026=val(z["Q3","2026"]["delivered"])
assert (annual2024,annual2025,ytd2025,ytd2026,q32025,q32026)==(94.5,100.2,76.1,80.6,27.0,29.4)
s={r["year"]:r for r in dcshare}
assert (val(s["2024"]["value"]),val(s["2025"]["value"]))==(26,28)
assert all(r["unit"]=="percent_of_electricity_sales" for r in dcshare)
assert all(r["unit"]=="million_MWh" for r in energy)
rr={r["rule_id"]:r for r in rules}
assert rr["GS5_MIN_CONTRACT_TERM"]["effective_start"]=="2027-01-01"
assert rr["GS5_MIN_TD_DEMAND_CHARGE"]["value"]=="85"
assert rr["GS5_MIN_GENERATION_DEMAND_CHARGE"]["value"]=="60"
assert rr["QUEUE_INTERIM_ANONYMOUS_DATABASE"]["legal_status_asof_2026_11_14"]=="INTERIM_DIRECTION_FOR_REVISED_PROPOSAL"
assert len({(r["assumed_contracted_mw"],r["assumed_actual_demand_pct_of_contract"]) for r in bill})==len(bill)
for r in bill:
    mw=val(r["assumed_contracted_mw"])
    real=mw*val(r["assumed_actual_demand_pct_of_contract"])/100
    approx(real,val(r["assumed_actual_demand_mw"]))
    approx(max(real,.85*mw),val(r["min_td_billed_demand_mw"]))
    approx(max(real,.60*mw),val(r["min_generation_billed_demand_mw"]))
    assert r["scenario_status"]=="HYPOTHETICAL_ONLY"
a={r["metric_id"]:r for r in aep}
assert (int(a["AEP_LARGE_LOAD_TARIFF_FILINGS"]["value"]),int(a["AEP_LARGE_LOAD_TARIFF_APPROVED"]["value"]),int(a["AEP_LARGE_LOAD_TARIFF_PENDING"]["value"]))==(8,6,2)
out={
 "Dominion_approx_queue_MW":total,
 "assigned_projected_connection_date_MW":dated,
 "assigned_date_coverage_pct":round(date_ratio,3),
 "batched_date_study_MW":waiting,
 "not_an_operational_realization_rate":True,
 "DOM_annual_delivered_MWh_millions_2024_2025":[annual2024,annual2025],
 "DOM_annual_total_delivered_yoy_pct":round(inc(annual2025,annual2024),3),
 "DOM_YTD_through_Sep_delivered_million_MWh_2025_2026":[ytd2025,ytd2026],
 "DOM_YTD_total_delivered_yoy_pct":round(inc(ytd2026,ytd2025),3),
 "DOM_Q3_total_delivered_yoy_pct":round(inc(q32026,q32025),3),
 "DOM_data_center_share_sales_pct_2024_2025":[26,28],
 "DC_absolute_MWh_same_denominator_verified":False,
 "GS5_tariff_approved_before_midterms":True,
 "GS5_effective_on":"2027-01-01",
 "example_100MW_0_pct_actual_load_min_TD_billing_MW":85.0,
 "example_100MW_0_pct_actual_load_min_generation_billing_MW":60.0,
 "AEP_pre_election_tariffs_approved_count":6,
 "same_project_FIRM_to_ACTUAL_MW_conversion":None,
 "political_causality":"UNTESTED"
}
print(json.dumps(out,ensure_ascii=False,indent=2))
