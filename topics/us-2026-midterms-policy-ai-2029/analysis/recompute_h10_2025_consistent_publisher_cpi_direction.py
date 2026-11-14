#!/usr/bin/env python3
"""TOPIC-011 H10: single publisher dated-pre-release CPI consensus vs 2025 US Treasury daily direction.

Fixed calendar cohort contains ALL 11 actual 2025 BLS CPI release dates.
Only seven have explicitly date-stamped Calculated Risk posts quoting
survey consensus, with BLS official first-release actual. Missing
publisher forecasts remain EMPTY and are not backfilled.

Research limitations: publisher-reported consensus (not microdata),
blog historical pages can be revised, whole-day rates include other news,
sample 7 is small, 2025-10 CPI release disrupted by govt shutdown.
No causal or trade-result claim.
"""
import csv,io,sys,json,math,datetime
from pathlib import Path

def sign(x):return (x>0)-(x<0)
def exact_two_sided(n,k):
    if n==0:return None
    p=sum(math.comb(n,j) for j in range(0,n+1) if math.comb(n,j)<=math.comb(n,k))/2**n
    return round(min(1,p),6)

def calculate():
    fname="h10_cpi_consistent_publisher_2025_pre_release_cohort.csv"
    source=sys.stdin.read() if "--stdin-csv" in sys.argv else (Path(__file__).resolve().parent.parent/"data"/fname).read_text("utf8")
    rows=list(csv.DictReader(io.StringIO(source)))
    assert len(rows)==11
    assert [x["release_date"] for x in rows]==sorted(x["release_date"] for x in rows)
    good=[r for r in rows if r["forecast_evidence_grade"]=="PRE_RELEASE_DATED_CALCULATED_RISK_QUOTED_MARKET_CONSENSUS"]
    absent=[r["release_date"] for r in rows if r not in good]
    assert len(good)==7
    assert absent==["2025-04-10","2025-05-13","2025-10-24","2025-12-18"]
    assert all(r["preview_original_url"].startswith("https://www.calculatedriskblog.com/2025/") for r in good)
    for r in good:
        a=datetime.datetime.fromisoformat(r["dated_consensus_published_at"])
        event=datetime.datetime.strptime(r["release_date"]+"T08:30","%Y-%m-%dT%H:%M").replace(tzinfo=a.tzinfo)
        assert a<event,(r["release_date"],a,event)
        for group in ["headline","core"]:
            f=float(r[f"consensus_{group}_sa_mom_pct"])
            first=float(r[f"bls_first_release_{group}_sa_mom_pct"])
            sur=float(r[f"{group}_surprise_pp"])
            assert abs(first-f-sur)<0.000001
        assert r["treasury_prior_observation_date"]<r["release_date"]
    def one(group,omit=None):
        selected=[r for r in good if r["release_date"]!=omit]
        nonzero=[r for r in selected if abs(float(r[group+"_surprise_pp"]))>=0.05]
        nz=[r for r in nonzero if float(r["ust2y_daily_signed_bp"])!=0]
        match=[r for r in nz if sign(float(r[group+"_surprise_pp"]))==sign(float(r["ust2y_daily_signed_bp"]))]
        other=[r["release_date"] for r in nz if r not in match]
        result={"dated_previews":len(selected),"nonzero_surprise":len(nonzero),"two_year_signed_nonzero":len(nz),
            "two_year_sign_matches":len(match),"two_year_opposite_dates":other,
            "two_year_zero_dates":[r["release_date"] for r in nonzero if float(r["ust2y_daily_signed_bp"])==0],
            "exact_binomial_two_sided_p":exact_two_sided(len(nz),len(match))}
        return result
    return {
        "validation":"PASS","all_BLS_2025_release_dates":len(rows),
        "same_publisher_date_verified_forecasts":len(good),
        "no_same_publisher_archive_pre_release":absent,
        "headline":one("headline"),"core":one("core"),
        "core_omit_mar12":one("core","2025-03-12"),
        "headline_omit_jan15":one("headline","2025-01-15"),
        "notes":"Convenience of same-publisher availability; missing 4 calendar releases, current blog pages not independently immutable archived originals; daily yield sign is not a pure CPI surprise response; p exploratory."
    }

if __name__=="__main__":
    print("SUMMARY_JSON="+json.dumps(calculate(),ensure_ascii=False))
