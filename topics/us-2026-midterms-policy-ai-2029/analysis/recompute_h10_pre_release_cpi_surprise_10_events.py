#!/usr/bin/env python3
"""TOPIC-011 H10: dated pre-release CPI headline/core forecasts vs first BLS releases and signed UST yields.
Use GitHub data CSV. This is an opportunistically sourced, 10-date historical illustration, not a random sample.
Retrospective vendor forecasts from another file MUST NOT be joined into this PIT cohort.
"""
import csv
import io
import sys
import json
import math
from pathlib import Path
from collections import Counter

def read():
    filename="h10_cpi_pre_release_dated_forecasts_10events_2023_2026.csv"
    p=Path(__file__).resolve().parent.parent/"data"/filename
    content=sys.stdin.read() if "--stdin-csv" in sys.argv else p.read_text(encoding="utf8")
    x=list(csv.DictReader(io.StringIO(content)))
    assert len(x)==10 and len({v["release_date"] for v in x})==10
    assert [v["release_date"] for v in x]==sorted(v["release_date"] for v in x)
    for r in x:
        ts=r["forecast_published_at"]
        assert ts[:10]<=r["release_date"] and (ts[:10]<r["release_date"] or ts.endswith("Z"))
        assert ts!=r["release_date"]
        assert r["source_temporal_grade"].startswith("PIT_")
        assert r["bls_first_release_url"].endswith("cpi_"+r["release_date"][5:7]+r["release_date"][8:10]+r["release_date"][:4]+".htm")
        for name in ["headline","core"]:
            key="forecast_"+name+"_mom_sa_percent"
            d="surprise_"+name+"_pp"
            if r[key]:
                a=float(r["actual_"+name+"_mom_sa_percent_BLS_first"])
                assert abs((a-float(r[key]))-float(r[d]))<1e-7
            else:assert r[d]==""
    return x

def sign(x):
    return (x>0)-(x<0)

def calc(x,name,consensus_only=False,omit_nov10=False):
    rows=[]
    for r in x:
        if consensus_only and r["forecast_type"]=="SINGLE_INSTITUTION_FORECAST":continue
        if omit_nov10 and r["release_date"]=="2026-11-10":continue
        sur=r["surprise_"+name+"_pp"]
        if sur=="":continue
        sur=float(sur)
        if abs(sur)<0.05:continue  # rounded BLS +/-0.1pp evidence, avoid marginal decimals
        two=float(r["ust_2y_change_bp_signed_same_day"])
        ten=float(r["ust_10y_change_bp_signed_same_day"])
        rows.append(dict(date=r["release_date"],surprise_pp=sur,two_bp=two,ten_bp=ten,
                         agreement2=sign(sur)==sign(two),agreement10=sign(sur)==sign(ten)))
    direction2=[a for a in rows if sign(a["two_bp"])!=0]
    direction10=[a for a in rows if sign(a["ten_bp"])!=0]
    correct2=sum(r["agreement2"] for r in direction2)
    correct10=sum(r["agreement10"] for r in direction10)
    def binom(n,k):
        if n==0:return None
        p_one=sum(math.comb(n,j) for j in range(k,n+1))/2**n
        return {"one_sided_tail_p":round(p_one,6),"two_sided_exact_p":round(min(1,2*p_one),6)}
    return {"surprise_nonzero_n":len(rows),"two_year_signed_nonzero_n":len(direction2),
            "two_year_sign_agree":correct2,
            "two_year_one_mismatch":[r["date"] for r in direction2 if not r["agreement2"]],
            "two_year_flat":[r["date"] for r in rows if sign(r["two_bp"])==0],
            "two_year_exact_binomial":binom(len(direction2),correct2),
            "ten_year_signed_nonzero_n":len(direction10),
            "ten_year_sign_agree":correct10,
            "ten_year_exact_binomial":binom(len(direction10),correct10),
            "event_rows":rows}

def run():
    x=read()
    out={"validation":"PASS","rows":len(x),
         "core_all_date_grounded":calc(x,"core"),
         "core_only_published_consensus":calc(x,"core",consensus_only=True),
         "core_excluding_2026_nov10":calc(x,"core",omit_nov10=True),
         "headline_all_date_grounded":calc(x,"headline"),
         "headline_only_published_consensus":calc(x,"headline",consensus_only=True),
         "limits":"First release forecast dates verified, but convenience sample not random, forecasts sometimes institution not consensus, one-decimal surprise rounding, Treasury whole-day yields not CPI-only price response; 2024-06-12 had FOMC same day."
    }
    return out

if __name__=="__main__":
    output=run()
    if "--verbose" not in sys.argv:
        for key in ["core_all_date_grounded","core_only_published_consensus","core_excluding_2026_nov10","headline_all_date_grounded","headline_only_published_consensus"]:
            output[key].pop("event_rows",None)
    print("SUMMARY_JSON="+json.dumps(output,ensure_ascii=False))
