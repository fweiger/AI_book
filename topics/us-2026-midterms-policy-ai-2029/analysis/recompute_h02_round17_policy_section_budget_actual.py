#!/usr/bin/env python3
"""TOPIC-011 Round 17: enacted-section policy outcomes and CBO baseline gate.

Reproducible stdlib; numerical cross-checks are computations on documented
official source extractions. They are not claims of post-2026 political causality.
Optional --verify-gpo re-downloads six official original/enacted HTML sources
and verifies their observed source SHA256, not historical PIT server bytes.
"""
import csv
import hashlib
import json
import sys
import urllib.request
from decimal import Decimal
from pathlib import Path

DATA=Path(__file__).resolve().parent.parent/"data"
OBS=DATA/"h02_round17_policy_section_budget_actual_2008_2026.csv"
MANIFEST=DATA/"h02_round17_gpo_bill_to_law_6files_sha.csv"
ASOF="2026-11-14"
ELECTION="2026-11-03"
def read(path):
    with path.open(encoding="utf-8",newline="") as f:return list(csv.DictReader(f))
def get(rows,id):
    a=[r for r in rows if r["record_id"]==id]
    assert len(a)==1,(id,len(a))
    return a[0]
def val(rows,id):
    return Decimal(get(rows,id)["value"])
def main():
    obs=read(OBS);mf=read(MANIFEST)
    assert len(obs)==16 and len(mf)==6
    assert len(set(r["record_id"] for r in obs))==16
    assert len(set(r["manifest_id"] for r in mf))==6
    assert {x["law_id"] for x in obs if x["case_id"].startswith("RECONCILIATION")}=={"PL119-21"}
    assert all(r["data_asof"]<=ASOF for r in obs)
    assert all(r["policy_legal_date"]<ELECTION for r in obs)
    assert all(r["source_publication_date"]<ELECTION for r in obs)
    assert all(len(r["sha256"])==64 and len(r["source_url"])>25 for r in mf)
    assert {r["vehicle"] for r in mf}=={"HR1424","HR748","HR1"}
    for v in ("HR1424","HR748","HR1"):
        assert {r["version"] for r in mf if r["vehicle"]==v}=={"INTRODUCED","ENACTED"}
    assert val(obs,"P17-01")==700
    assert val(obs,"P17-02")==475
    assert val(obs,"P17-03")==Decimal("443.5")
    assert val(obs,"P17-04")==Decimal("31.1")
    assert Decimal(0)<val(obs,"P17-04")<val(obs,"P17-03")<val(obs,"P17-02")<val(obs,"P17-01")
    assert get(obs,"P17-06")["comparison_baseline"]=="MORE_THAN_NOT_EXACTLY"
    assert get(obs,"P17-06")["evidence_class"]=="ACTUAL_PAYMENT_LOWER_BOUND"
    assert val(obs,"P17-07")==3400 and val(obs,"P17-08")==-366
    assert get(obs,"P17-07")["comparison_baseline"]!=get(obs,"P17-08")["comparison_baseline"]
    assert get(obs,"P17-07")["period_end"]==get(obs,"P17-08")["period_end"]
    assert get(obs,"P17-07")["source_publication_date"]==get(obs,"P17-08")["source_publication_date"]
    assert val(obs,"P17-09")==4200 and get(obs,"P17-09")["evidence_class"]=="FORECAST_DYNAMIC_AND_DEBT_SERVICE"
    assert val(obs,"P17-10")==Decimal("-886.8") and val(obs,"P17-11")==Decimal("7.5")
    assert get(obs,"P17-11")["unit"]=="million_person"
    assert get(obs,"P17-12")["policy_operational_date"]=="2027-01-01"
    assert get(obs,"P17-13")["policy_operational_date"]=="2026-07-31"
    assert get(obs,"P17-13")["source_publication_date"]=="2026-06-03"
    assert all(get(obs,x)["policy_operational_date"]=="2027-12-31" for x in ("P17-14","P17-15"))
    assert all(get(obs,x)["value"]=="" for x in ("P17-12","P17-13","P17-14","P17-15","P17-16"))
    assert len([r for r in obs if r["evidence_class"].startswith("ACTUAL")])==3
    if "--verify-gpo" in sys.argv:
        for r in mf:
            req=urllib.request.Request(r["source_url"],headers={"User-Agent":"AI-book-TOPIC011-source-audit/1.0"})
            with urllib.request.urlopen(req,timeout=60) as resp:
                data=resp.read()
            assert len(data)==int(r["bytes"]),(r["manifest_id"],len(data))
            digest=hashlib.sha256(data).hexdigest()
            assert digest==r["sha256"],(r["manifest_id"],digest)
    result={
        "qa":"PASS","asof":ASOF,"policy_records":len(obs),"gpo_docs":len(mf),
        "tarp":{"initial_authority_usd_bn":"700",
                "amended_authority_usd_bn":"475",
                "actual_gross_disbursed_usd_bn":"443.5",
                "actual_lifetime_net_cost_usd_bn":"31.1",
                "actual_disbursement_pct_of_amended_ceiling":str((val(obs,"P17-03")/val(obs,"P17-02")*100).quantize(Decimal(".001"))),
                "not_an_annual_fiscal_impulse":True},
        "cares":{"first_EIP_paid_lower_bound_usd_bn":"270","bound_is_strict_greater_than":True,
                 "other_EIP_rounds_excluded":True},
        "reconciliation_2025":{"enacted":"2025-07-04",
                "cbo_2025Jan_baseline_conventional_usd_bn":"3400",
                "cbo_Senate_enforcement_conventional_usd_bn":"-366",
                "baseline_gap_usd_bn":"3766",
                "different_baselines_not_a_policy_change":True,
                "cbo_Feb2026_debt_macro_rounded_usd_bn":"4200",
                "medicaid_chapter_savings_2025_2034_usd_bn":"886.8",
                "projected_2034_additional_uninsured_millions":"7.5"},
        "delayed_policy":{"medicaid_section71119_operational_date":"2027-01-01",
                "cms_rule_effective":"2026-07-31",
                "wind_solar_45Y_48E_placed_in_service_cutoff":"2027-12-31",
                "all_primary_statutes_pre_2026_election":True,
                "2027_actual_policy_outcomes_observed":False},
        "interpretation":"Historical policy outcomes and pre-election inherited 2027 effects, not new Congress causal impacts"
    }
    print(json.dumps(result,ensure_ascii=False,indent=2))
if __name__=="__main__":main()
