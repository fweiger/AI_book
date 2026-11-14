#!/usr/bin/env python3
"""TOPIC-011 H03 source-scoped study, 2026-11-14.
Verify company data-center-only *metered* baseline, issuer's vintage forecasts,
contract-stage firm counts, PJM reliability event, and two different registries.

No network, no external packages, no claim of individual project realization.
"""
from __future__ import annotations
import csv, json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
def load(name):
    with (ROOT/"data"/name).open(encoding="utf-8",newline="") as f:return list(csv.DictReader(f))
def near(a,b,eps=.02):assert abs(a-b)<eps,(a,b)
def pct(new,old):return 100*(new/old-1)
def main():
    f=load("h03_dominion_dc_only_physical_and_forecasts.csv")
    c=load("h03_dominion_firm_capacity_stages_backtest.csv")
    e=load("h03_pjm_real_load_trip_events_2024_2026.csv")
    incident=load("h03_pjm_2026_july_22_load_trip_balance.csv")
    reg=load("h03_state_federal_large_load_registry_status.csv")
    conflicts=load("h03_data_discrepancies_and_controls.csv")
    assert [len(x) for x in (f,c,e,incident,reg,conflicts)]==[22,3,3,1,7,3]
    assert len({x["metric_id"] for x in f})==22
    observed=[x for x in f if x["observation_type"].startswith("OBSERVED")]
    assert len(observed)==1 and observed[0]["target_year"]=="2025"
    assert int(observed[0]["value_mw"])==4000
    future=[x for x in f if x["observation_type"].startswith("EXTERNAL_COMPANY_FORECAST")]
    assert [int(x["target_year"]) for x in future]==list(range(2026,2047))
    y={int(x["target_year"]):float(x["value_mw"]) for x in future}
    assert [y[k] for k in (2026,2027,2028,2029,2030,2046)]==[4433,4933,5448,5980,6526,16636]
    assert all(y[k]>y[k-1] for k in range(2027,2047))
    assert all(x["source_letter_date"]=="2026-01-06" and x["logged_at"]=="2026-11-14" for x in f)
    assert all("future target not actual" in x["critical_caveat"] for x in future)
    by={x["asof_month"]:x for x in c}
    assert len(by)==3
    firm={}
    share={}
    for date,row in by.items():
        esa=float(row["esa_gw"]);cloa=float(row["cloa_gw"]);eloa=float(row["eloa_gw"])
        total=float(row["total_company_contract_pipeline_gw"])
        firm[date]=esa+cloa
        share[date]=100*firm[date]/total
        near(float(row["firm_esa_plus_cloa_gw"]),firm[date])
        near(float(row["firm_share_pct"]),share[date])
        assert abs((esa+cloa+eloa)-total)<=.101
        assert "not actual" in row["limit"] .lower() or "not track" in row["limit"].lower()
    assert firm=={"2025-07":16.9,"2025-12":21.2,"2026-09":22.0}
    assert abs(share["2026-09"]-share["2025-12"])>3
    assert {x["event_date"] for x in e}=={"2024-07-10","2025-02-17","2026-07-22"}
    event2026=next(x for x in e if x["event_date"]=="2026-07-22")
    assert float(event2026["approx_large_load_transfer_mw"])==3800
    net=int(incident[0]["PJM_RTO_load_mw_before"])-int(incident[0]["PJM_RTO_load_mw_after"])
    assert net==int(incident[0]["net_RTO_load_drop_mw"])==3779
    assert abs(net-int(event2026["approx_large_load_transfer_mw"]))<=100
    byid={x["record_id"]:x for x in reg}
    assert len(byid)==7
    assert byid["VA-SCC-PUR202600011-LATEST"]["case_status"]=="NO_FINAL_APPROVAL_IN_ORDER"
    assert byid["FERC-ER263515-ORDER"]["case_status"]=="EFFECTIVE_2026-10-12"
    assert byid["PJM-REGISTRY-INITIAL-DUE"]["action_or_deadline_date"]=="2027-03-01"
    assert all(x["public_data_availability"]!="PROJECT_LEVEL_PUBLIC_OBSERVED" for x in reg)
    assert len({x["conflict_id"] for x in conflicts})==3
    ans={
      "observed_dc_only_coincident_peak_2025_MW_approx":4000,
      "external_issued_2026_jan_forecast_DC_peak_2027_MW":y[2027],
      "external_issued_2026_jan_forecast_DC_peak_2029_MW":y[2029],
      "future_annual_forecast_rows":len(future),
      "firm_esa_plus_cloa_GW_2025Dec":firm["2025-12"],
      "firm_esa_plus_cloa_GW_2026Sep":firm["2026-09"],
      "firm_absolute_growth_pct":round(pct(firm["2026-09"],firm["2025-12"]),3),
      "firm_share_of_pipeline_pct_2025Dec":round(share["2025-12"],3),
      "firm_share_of_pipeline_pct_2026Sep":round(share["2026-09"],3),
      "firm_share_change_percentage_points":round(share["2026-09"]-share["2025-12"],3),
      "PJM_2026Jul22_reported_DC_transfer_MW_approx":3800,
      "PJM_2026Jul22_RTO_net_load_drop_MW":net,
      "SCC_queue_approval_asof_2026Nov14":"PENDING",
      "Virginia_public_project_queue_observed":False,
      "PJM_50MW_Large_Load_Registry_effective":"2026-10-12",
      "PJM_registry_first_submission_deadline":"2027-03-01",
      "PJM_public_registry_scope":"ELECTRIC_DISTRIBUTOR_ZONE_AGGREGATES_ONLY_WHERE_POSSIBLE",
      "actual_2027_DC_peak_MW":None,
      "project_matched_F_to_A_to_R_realization_rate":None,
      "causal_h03":"UNTESTED"
    }
    print(json.dumps(ans,ensure_ascii=False,indent=2))
if __name__=="__main__":
    main()
