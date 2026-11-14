#!/usr/bin/env python3
"""Audit pre-election Dominion/AEP firm-contract and realized operations signals.

Company pipeline stocks, newly connected campus design capacity, high-load
revenue, and PJM requested load are NOT interchangeable measurements.
This script calculates only quantities justified by comparable source scope.
"""
from __future__ import annotations
import csv, json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
def load(name):
    with (ROOT/"data"/name).open(encoding="utf-8",newline="") as f:
        return list(csv.DictReader(f))
def num(x):return float(x)
def growth(a,b):return 100*(a/b-1)
def almost(a,b,eps=0.005):
    assert abs(a-b)<eps,(a,b)
def main():
    st=load("h03_dominion_contract_stage_history.csv")
    rev=load("h03_dominion_highload_revenue_quarters.csv")
    cm=load("h03_dominion_completed_campus_and_sales_share.csv")
    aep=load("h03_aep_evidence_scope_matrix.csv")
    scope=load("h03_maturity_scope_crosswalk.csv")
    assert [len(x) for x in (st,rev,cm,aep,scope)]==[3,6,6,5,8]
    assert {r["asof_month"] for r in st}=={"2023-07","2025-12","2026-09"}
    for row in st:
        total=num(row["reported_pipeline_total_gw"])
        elo=num(row["eloa_gw"]); clo=num(row["cloa_gw"]); esa=num(row["esa_gw"])
        almost((elo+clo+esa)-total, num(row["stage_sum_minus_reported_gw"]))
        assert abs(elo+clo+esa-total)<=0.101,"Source stage numbers rounded to tenths GW"
        almost(100*esa/total,num(row["esa_share_pct"]),0.001)
    stid={r["asof_month"]:r for r in st}
    earlier=stid["2025-12"]; now=stid["2026-09"]
    esa_change=growth(num(now["esa_gw"]),num(earlier["esa_gw"]))
    almost(esa_change,19.6078431372549)
    assert num(now["reported_pipeline_total_gw"])==54.9
    q={(r["year"],r["quarter"]):r for r in rev}
    assert len(q)==6
    assert all(r["data_type"]=="HIGH_LOAD_ELECTRIC_SALES_REVENUE_NOT_DATA_CENTER_ONLY" for r in rev)
    for i in range(1,4):
        last=q["2025",f"Q{i}"]; current=q["2026",f"Q{i}"]
        assert last["year"]=="2025" and current["year"]=="2026"
        assert current["same_quarter_prior_year_usd_million"]==last["high_load_revenue_usd_million"]
        almost(growth(num(current["high_load_revenue_usd_million"]),
                      num(last["high_load_revenue_usd_million"])),num(current["yoy_pct"]),0.001)
    yoy22=sum(num(q["2025",f"Q{i}"]["high_load_revenue_usd_million"]) for i in range(1,4))
    yoy23=sum(num(q["2026",f"Q{i}"]["high_load_revenue_usd_million"]) for i in range(1,4))
    assert yoy22==1308 and yoy23==2156
    by={(r["year"],r["metric"]):r for r in cm}
    assert len(by)==6
    count24=num(by["2024","new_connected_campuses"]["value"])
    count25=num(by["2025","new_connected_campuses"]["value"])
    final24=num(by["2024","new_connected_campuses_ultimate_capacity"]["value"])
    final25=num(by["2025","new_connected_campuses_ultimate_capacity"]["value"])
    sales24=num(by["2024","data_center_share_electricity_sales"]["value"])
    sales25=num(by["2025","data_center_share_electricity_sales"]["value"])
    assert (count24,count25,final24,final25,sales24,sales25)==(15,11,977,744,26,28)
    ae={r["evidence_id"]:r for r in aep}
    assert len(ae)==5
    assert num(ae["AEP-PJM-2025-NEAR"]["value"])==11182
    assert num(ae["AEP-PJM-2025-ESA"]["value"])==8600
    assert num(ae["AEP-ALL-2026"]["value"])==84000
    assert num(ae["AEP-NEW-Q3"]["value"])==15000
    assert num(ae["AEP-TEXAS-ERCOT"]["value"])==49000
    assert sum("NOT_COMPARABLE" in r["comparison_rule"] for r in scope)>=4
    assert all(r["comparison_rule"] for r in scope)
    out={
      "Dominion_ESA_2025Dec_GW":num(earlier["esa_gw"]),
      "Dominion_ESA_2026Sep_GW":num(now["esa_gw"]),
      "Dominion_ESA_growth_percent":round(esa_change,3),
      "Dominion_ESA_2026Sep_share_of_reported_pipeline_percent":round(100*num(now["esa_gw"])/num(now["reported_pipeline_total_gw"]),3),
      "Dominion_pipeline_total_change_2025Dec_to_2026Sep_percent":round(growth(num(now["reported_pipeline_total_gw"]),num(earlier["reported_pipeline_total_gw"])),3),
      "Dominion_2025_highload_revenue_Q1_to_Q3_usd_million":yoy22,
      "Dominion_2026_highload_revenue_Q1_to_Q3_usd_million":yoy23,
      "Dominion_highload_revenue_YTD_YOY_percent":round(growth(yoy23,yoy22),3),
      "Dominion_connected_new_campuses_2024":count24,
      "Dominion_connected_new_campuses_2025":count25,
      "Dominion_new_connected_campuses_YOY_percent":round(growth(count25,count24),3),
      "Dominion_new_connected_campus_ultimate_capacity_2024_MW":final24,
      "Dominion_new_connected_campus_ultimate_capacity_2025_MW":final25,
      "Dominion_new_campus_design_capacity_YOY_percent":round(growth(final25,final24),3),
      "Dominion_DC_share_electricity_sales_2024_to_2025_percentage_points":sales25-sales24,
      "AEP_2025_PJM_near_term_signed_ESA_lower_bound_percent_strictly_greater_than":round(100*8600/11182,3),
      "AEP_companywide_signed_ESA_OR_LOA_2026_MW":84000,
      "PJM_F_to_A_to_R_cohort_matched_conversion":None,
      "causal_status":"UNTESTED",
      "warning":"Do not compare Dominion ESA GW with PJM DOM request MW, AEP national contracts with PJM AEP request, or revenue USD with metered MW."
    }
    print(json.dumps(out,ensure_ascii=False,indent=2))
    return 0
if __name__=="__main__":
    raise SystemExit(main())
