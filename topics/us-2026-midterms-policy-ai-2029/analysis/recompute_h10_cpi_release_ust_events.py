#!/usr/bin/env python3
"""H10 CPI release-day US Treasury descriptive event study, stdlib only.

INPUT: TOPIC-011 data/h10_us_treasury_2y_10y_daily_2025_2026.csv
via --stdin-csv or sibling data file.
SOURCES: BLS CPI actual release calendar (2025 and 2026) and Treasury daily rates.
METHOD: daily par yield changes on release date vs previous observed trading date,
with same-calendar-month non-release randomized-placebo (20,000 replicates,
fixed seed). No intraday surprise, macro factor controls or causal inference.
"""
import csv, io, statistics, random, json, sys
from pathlib import Path

RELEASES=[
("2025-01-15","2024-12"),("2025-02-12","2025-01"),("2025-03-12","2025-02"),("2025-04-10","2025-03"),
("2025-05-13","2025-04"),("2025-06-11","2025-05"),("2025-07-15","2025-06"),("2025-08-12","2025-07"),
("2025-09-11","2025-08"),("2025-10-24","2025-09"),("2025-12-18","2025-11"),
("2026-01-13","2025-12"),("2026-02-13","2026-01"),("2026-03-11","2026-02"),("2026-04-10","2026-03"),
("2026-05-12","2026-04"),("2026-06-10","2026-05"),("2026-07-14","2026-06"),("2026-08-12","2026-07"),
("2026-09-11","2026-08"),("2026-10-14","2026-09"),("2026-11-10","2026-10")
]
N=20000
SEED=20261114

def read():
    p=Path(__file__).resolve().parent.parent/"data"/"h10_us_treasury_2y_10y_daily_2025_2026.csv"
    raw=sys.stdin.read() if "--stdin-csv" in sys.argv else p.read_text("utf-8")
    rows=list(csv.DictReader(io.StringIO(raw)))
    assert len(rows)==467
    rows=sorted(rows,key=lambda a:a["date"])
    d=[]
    for prev,now in zip(rows,rows[1:]):
        d.append({"date":now["date"],"month":now["date"][:7],"prior":prev["date"],
            "bp2":round(100*(float(now["treasury_2y_pct"])-float(prev["treasury_2y_pct"])),4),
            "bp10":round(100*(float(now["treasury_10y_pct"])-float(prev["treasury_10y_pct"])),4)})
    lookup={i["date"]:i for i in d}
    assert len(lookup)==len(d)
    assert len(RELEASES)==22 and len(set(a for a,b in RELEASES))==22
    assert all(d in lookup for d,_ in RELEASES),[d for d,_ in RELEASES if d not in lookup]
    return lookup,d

def test(events,nonrelease,seed):
    assert events
    mean=lambda a:sum(a)/len(a)
    pool={m:[x for x in nonrelease if x["month"]==m] for m in {e["month"] for e in events}}
    assert all(pool[e["month"]] for e in events)
    rng=random.Random(seed)
    e2=mean([abs(x["bp2"]) for x in events]);e10=mean([abs(x["bp10"]) for x in events])
    p2hits=p10hits=0; sum2=sum10=0
    for _ in range(N):
        draws=[rng.choice(pool[x["month"]]) for x in events]
        a2=mean([abs(x["bp2"]) for x in draws])
        a10=mean([abs(x["bp10"]) for x in draws])
        sum2+=a2;sum10+=a10
        p2hits+=a2>=e2;p10hits+=a10>=e10
    return dict(n=len(events),abs_2y_event_mean_bp=round(e2,4),abs_10y_event_mean_bp=round(e10,4),
                abs_2y_same_month_placebo_mean_bp=round(sum2/N,4),
                abs_10y_same_month_placebo_mean_bp=round(sum10/N,4),
                randomization_p_2y=round((p2hits+1)/(N+1),6),
                randomization_p_10y=round((p10hits+1)/(N+1),6))

def run():
    lookup,changes=read()
    keys={date for date,ref in RELEASES}
    event=[lookup[d] for d,ref in RELEASES]
    nonrelease=[d for d in changes if d["date"] not in keys]
    whole=test(event,nonrelease,SEED)
    without_top=test([x for x in event if x["date"]!="2026-11-10"],nonrelease,SEED)
    only2025=test([x for x in event if x["date"].startswith("2025-")],nonrelease,SEED)
    only2026=test([x for x in event if x["date"].startswith("2026-")],nonrelease,SEED)
    out=io.StringIO()
    writer=csv.writer(out,lineterminator="\n")
    writer.writerow(["release_date","cpi_reference_month","prior_treasury_trade_date","2y_yield_change_bp",
                     "10y_yield_change_bp","abs_2y_bp","abs_10y_bp","source_family","causality_status"])
    for date,ref in RELEASES:
        x=lookup[date]
        writer.writerow([date,ref,x["prior"],f"{x['bp2']:.2f}",f"{x['bp10']:.2f}",
                         f"{abs(x['bp2']):.2f}",f"{abs(x['bp10']):.2f}",
                         "BLS_RELEASE_CALENDAR_AND_TREASURY_DAILY_XML","DESCRIPTIVE_NOT_CAUSAL"])
    return dict(events_csv=out.getvalue(), summary={
         "validation":"PASS","n_release":len(event),"n_other":len(nonrelease),
         "other_2y_abs_mean_bp":round(sum(abs(x["bp2"]) for x in nonrelease)/len(nonrelease),4),
         "other_10y_abs_mean_bp":round(sum(abs(x["bp10"]) for x in nonrelease)/len(nonrelease),4),
         "full_sample":whole,"excluding_2026_11_10":without_top,
         "year_2025":only2025,"year_2026":only2026,
         "nov10":{"two_year_bp":lookup["2026-11-10"]["bp2"],"ten_year_bp":lookup["2026-11-10"]["bp10"]},
         "random_seed":SEED,"random_draws":N,
         "calendar_sources":["https://www.bls.gov/schedule/news_release/cpi.htm?lv=true",
                             "https://blsmon1.bls.gov/schedule/news_release/cpi.htm",
                             "https://www.bls.gov/bls/news-release/cpi.htm"],
         "limit":"No pre-release CPI consensus, futures or intra-day quotes; matched-month random draws are exploratory noncausal placebo."})

if __name__=="__main__":
    res=run()
    print("BEGIN_CSV")
    print(res["events_csv"].rstrip())
    print("END_CSV")
    print("SUMMARY_JSON="+json.dumps(res["summary"],ensure_ascii=False))
