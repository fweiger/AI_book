#!/usr/bin/env python3
"""TOPIC-011 H02 Round 18: CBO February 2026 baseline, FY2026–2029.

Reads CBO's official open-data repo at an exact source commit and verifies
SHA256. Distinguishes unadjusted federal fiscal-year flows, payment timing
adjustments, and an exploratory (not cyclically adjusted) primary deficit / GDP
change. Source release vintage is Feb 2026, not proof of Feb 11 source bytes.
No added political treatment or post-election realized data are inferred.

Dependencies: Python standard library only. Outputs CSVs plus a QA JSON receipt.
"""
import csv
import hashlib
import io
import json
import sys
import urllib.request
from decimal import Decimal, ROUND_HALF_UP
from pathlib import Path

SOURCE_COMMIT = "284a95665f9f2f74ed1f482feb629b43fce323da"
FILES = {
    "ten_year_budget": ("6a2d727e70fb53512e45afdcc8d145f7dc952b2d4e87ca03591cb4e5bd63f0db", 145228),
    "long_term_budget": ("61018d3f4334c26a1704438e28c3b523b641c45549c8bf04c3890fd463f7a5f5", 38564),
}
BASE = "https://raw.githubusercontent.com/US-CBO/cbo-data/" + SOURCE_COMMIT + "/data/budget/"
YEARS = (2026,2027,2028,2029)
ZERO=Decimal("0")
KEYS = {
 "total_revenues":"proj_rev_total",
 "individual_income_tax_revenues":"proj_rev_individual_income",
 "payroll_tax_revenues":"proj_rev_payroll",
 "corporate_income_tax_revenues":"proj_rev_corporate_income",
 "customs_duties_revenues":"proj_rev_customs",
 "other_revenues":"proj_rev_other",
 "total_outlays":"proj_outlays_total",
 "mandatory_outlays":"proj_outlays_mandatory",
 "discretionary_outlays":"proj_outlays_discretionary",
 "net_interest_outlays":"proj_outlays_net_interest",
 "defense_discretionary_outlays":"proj_disc_defense",
 "nondefense_discretionary_outlays":"proj_disc_nondefense",
 "social_security_outlays":"proj_mand_social_security",
 "health_care_gross_before_medicare_offsets":"proj_mand_health_care",
 "medicare_offsetting_receipts":"proj_offset_medicare",
 "medicare_gross_outlays":"proj_mand_medicare",
 "medicaid_outlays":"proj_mand_medicaid",
 "chip_outlays":"proj_mand_chip",
 "premium_tax_credit_outlays":"proj_mand_premium_tax_credits",
 "total_outlays_timing_adjusted":"proj_outlays_total_timing_adj",
}
def dec(v):
    return Decimal(v)
def geturl(kind):
    return BASE + kind + "/annual_fy_2026-02.csv"
def source_bytes(kind,local):
    sha,sz = FILES[kind]
    if local:
        b=(Path(local)/(kind + "_2026-02.csv")).read_bytes()
    else:
        req=urllib.request.Request(geturl(kind), headers={"User-Agent":"TOPIC011-CBO-fiscal-bridge/1.0"})
        with urllib.request.urlopen(req,timeout=75) as r: b=r.read()
    got=hashlib.sha256(b).hexdigest()
    if got!=sha or len(b)!=sz:raise ValueError(f"Source drift for {kind}: sha={got}, size={len(b)}")
    return b
def indexed(b):
    rows={}
    for r in csv.DictReader(io.StringIO(b.decode("utf-8-sig"))):
        if r["date"] in {f"FY{y}" for y in YEARS}:
            k=(r["date"],r["variable"])
            if k in rows:raise AssertionError(f"Duplicate {k}")
            rows[k]=dec(r["value"])
    return rows
def at(d,fy,key):
    k=(f"FY{fy}",key)
    if k not in d:raise KeyError(k)
    return d[k]
def approx(a,b,tol="0.003"):
    assert abs(a-b)<=dec(tol),(str(a),str(b),str(a-b))
def put(path,rows):
    assert rows
    path.parent.mkdir(parents=True,exist_ok=True)
    with path.open("w",encoding="utf-8",newline="") as f:
        writer=csv.DictWriter(f,fieldnames=list(rows[0].keys()))
        writer.writeheader()
        for row in rows:writer.writerow({k:(str(v) if isinstance(v,Decimal) else v) for k,v in row.items()})
def rnd(a,places="0.001"):
    return a.quantize(dec(places),rounding=ROUND_HALF_UP)
def main():
    out=Path(sys.argv[1]) if len(sys.argv)>1 else Path("/tmp/h02_round18/output")
    local=Path(sys.argv[2]) if len(sys.argv)>2 else None
    buf={k:source_bytes(k,local) for k in FILES}
    main=indexed(buf["ten_year_budget"]);long=indexed(buf["long_term_budget"])
    results=[];long_rows=[];prev_raw=None;prev_adj=None
    for fy in YEARS:
        v={pretty:at(main,fy,key) for pretty,key in KEYS.items()}
        GDP=at(long,fy,"lt_gdp_trillions")*dec("1000")
        v["gdp_usd_bn"]=GDP
        v["major_health_care_net_after_medicare_offsets"]=v["health_care_gross_before_medicare_offsets"]+v["medicare_offsetting_receipts"]
        v["medicare_net_after_offsets"]=v["medicare_gross_outlays"]+v["medicare_offsetting_receipts"]
        v["medicaid_chip_marketplace_premiums"]=v["medicaid_outlays"]+v["chip_outlays"]+v["premium_tax_credit_outlays"]
        v["other_mandatory_net"]=v["mandatory_outlays"]-v["social_security_outlays"]-v["major_health_care_net_after_medicare_offsets"]
        v["noninterest_outlays"]=v["total_outlays"]-v["net_interest_outlays"]
        v["total_deficit"]=v["total_outlays"]-v["total_revenues"]  # positive deficits
        v["primary_deficit"]=v["noninterest_outlays"]-v["total_revenues"]
        v["timing_adjustment_to_outlays"]=v["total_outlays_timing_adjusted"]-v["total_outlays"]
        v["total_deficit_timing_adjusted"]=v["total_outlays_timing_adjusted"]-v["total_revenues"]
        v["primary_deficit_timing_adjusted"]=v["total_deficit_timing_adjusted"]-v["net_interest_outlays"]
        v["primary_deficit_gdp_pct"]=v["primary_deficit"]/GDP*100
        v["primary_deficit_timing_adjusted_gdp_pct"]=v["primary_deficit_timing_adjusted"]/GDP*100
        v["interest_share_of_total_deficit_pct"]=v["net_interest_outlays"]/v["total_deficit"]*100
        v["change_primary_deficit_pct_gdp_pp"]=None if prev_raw is None else v["primary_deficit_gdp_pct"]-prev_raw
        v["change_adj_primary_deficit_pct_gdp_pp"]=None if prev_adj is None else v["primary_deficit_timing_adjusted_gdp_pct"]-prev_adj
        prev_raw=v["primary_deficit_gdp_pct"];prev_adj=v["primary_deficit_timing_adjusted_gdp_pct"]
        # Source accounting identity, with tiny csv rounding differences.
        approx(v["total_revenues"],sum(v[z] for z in ("individual_income_tax_revenues","payroll_tax_revenues","corporate_income_tax_revenues","customs_duties_revenues","other_revenues")))
        approx(v["total_outlays"],v["mandatory_outlays"]+v["discretionary_outlays"]+v["net_interest_outlays"])
        approx(v["discretionary_outlays"],v["defense_discretionary_outlays"]+v["nondefense_discretionary_outlays"])
        approx(v["major_health_care_net_after_medicare_offsets"],v["medicare_net_after_offsets"]+v["medicaid_chip_marketplace_premiums"])
        approx(v["total_deficit"],-at(main,fy,"proj_deficit_total"))
        approx(v["primary_deficit"],-at(main,fy,"proj_primary_deficit"))
        approx(v["total_deficit_timing_adjusted"],-at(main,fy,"proj_deficit_total_timing_adj"))
        approx(v["primary_deficit_timing_adjusted"],-at(main,fy,"proj_primary_deficit_timing_adj"))
        approx(v["primary_deficit_timing_adjusted_gdp_pct"],-at(main,fy,"proj_primary_deficit_timing_adj_gdp_share"),"0.005")
        # Independent published report Table 1-1 rounded billions check.
        report_rounded={2026:(5596,7449,1853,1039),2027:(5885,7772,1887,1108),
                        2028:(6071,8151,2080,1218),2029:(6320,8340,2020,1324)}
        for k,expected in zip(("total_revenues","total_outlays","total_deficit","net_interest_outlays"),report_rounded[fy]):
            assert abs(v[k]-dec(expected))<dec("0.60"),(fy,k,str(v[k]),expected)
        if fy==2028:
            assert v["timing_adjustment_to_outlays"]<dec("-123")
        if fy==2029:
            assert v["timing_adjustment_to_outlays"]>dec("123")
        for k,val in v.items():
            if val is None:continue
            long_rows.append({"fiscal_year":f"FY{fy}","metric":k,"value":rnd(val),"unit":"pct_or_pp" if ("_pct" in k or k.endswith("_pp")) else "USD_bn",
                              "vintage":"CBO_2026-02","data_class":"forecast" ,"source_dataset":"US-CBO/cbo-data:2026-02",
                              "source_commit":SOURCE_COMMIT})
        names=("total_revenues","total_outlays","mandatory_outlays","discretionary_outlays","net_interest_outlays",
               "noninterest_outlays","total_deficit","primary_deficit","total_outlays_timing_adjusted",
               "total_deficit_timing_adjusted","primary_deficit_timing_adjusted",
               "timing_adjustment_to_outlays","gdp_usd_bn","primary_deficit_gdp_pct",
               "primary_deficit_timing_adjusted_gdp_pct","change_primary_deficit_pct_gdp_pp",
               "change_adj_primary_deficit_pct_gdp_pp","interest_share_of_total_deficit_pct",
               "defense_discretionary_outlays","nondefense_discretionary_outlays",
               "social_security_outlays","major_health_care_net_after_medicare_offsets",
               "medicare_net_after_offsets","medicaid_chip_marketplace_premiums",
               "other_mandatory_net","medicaid_outlays","customs_duties_revenues")
        row={"fiscal_year":f"FY{fy}","baseline_id":"CBO_2026_02_FEB11","publication_date":"2026-02-11",
             "law_cutoff":"2026-01-14","observed_at":"2026-11-14","source_commit":SOURCE_COMMIT}
        for k in names: row[k]="" if v[k] is None else rnd(v[k])
        results.append(row)
    # Freeze two distinct clocks. This is an accounting-only proxy, NOT structural fiscal impulse.
    x={r["fiscal_year"]:r for r in results}
    assert x["FY2028"]["change_primary_deficit_pct_gdp_pp"]>ZERO
    assert x["FY2028"]["change_adj_primary_deficit_pct_gdp_pp"]<ZERO
    assert x["FY2029"]["change_primary_deficit_pct_gdp_pp"]<ZERO
    assert x["FY2029"]["change_adj_primary_deficit_pct_gdp_pp"]>ZERO
    put(out/"h02_cbo_feb2026_fiscal_baseline_round18_wide.csv",results)
    put(out/"h02_cbo_feb2026_fiscal_baseline_round18_long.csv",long_rows)
    mf=[]
    for kind,(sha,bytesize) in FILES.items():
        mf.append({"source_family":"CBO_OFFICIAL_GITHUB","dataset":kind,"vintage":"2026-02",
             "source_commit":SOURCE_COMMIT,"source_url":geturl(kind),"sha256":sha,"bytes":bytesize,
             "retrieved_at":"2026-11-14","published_vintage":"2026-02-11",
             "pit_limit":"Versioned CBO data from Feb 2026, Git snapshot June 2026; not verified original Feb 11 bytes"})
    put(out/"h02_cbo_feb2026_source_manifest_round18.csv",mf)
    summary={"status":"PASS","fiscal_years":[r["fiscal_year"] for r in results],
             "source_commit":SOURCE_COMMIT,"source_shas":{k:v[0] for k,v in FILES.items()},
             "timing_adjustment_2028_usd_bn":str(x["FY2028"]["timing_adjustment_to_outlays"]),
             "timing_adjustment_2029_usd_bn":str(x["FY2029"]["timing_adjustment_to_outlays"]),
             "primary_deficit_share_adjusted_2027_2029":{r["fiscal_year"]:str(r["primary_deficit_timing_adjusted_gdp_pct"]) for r in results[1:]},
             "not_structural_fiscal_impulse":True,"not_nov2_complete_policy_baseline":True,
             "line_count":len(long_rows),"report_crosschecked":True}
    (out/"h02_cbo_feb2026_round18_validation.json").write_text(json.dumps(summary,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    print(json.dumps(summary,ensure_ascii=False,indent=2))
if __name__=="__main__":
    main()
