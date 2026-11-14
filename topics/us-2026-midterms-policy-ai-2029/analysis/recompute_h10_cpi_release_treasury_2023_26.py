#!/usr/bin/env python3
"""CPI release-days / US Treasury daily 2Y 10Y event study, 2023-2026.

Read two official Treasury CSVs from existing relative data paths, or pass the
JSON object {"old": <2023_24_csv>, "new": <2025_26_csv>} via --stdin-json.
Events use actual BLS release calendar dates. Null same-day closures are excluded.
Full-day rate moves != CPI surprises, and randomization tests are exploratory.
"""
import csv,io,json,random,sys
from pathlib import Path

BLS_DATES={
2023:["2023-01-12","2023-02-14","2023-03-14","2023-04-12","2023-05-10","2023-06-13","2023-07-12","2023-08-10","2023-09-13","2023-10-12","2023-11-14","2023-12-12"],
2024:["2024-01-11","2024-02-13","2024-03-12","2024-04-10","2024-05-15","2024-06-12","2024-07-11","2024-08-14","2024-09-11","2024-10-10","2024-11-13","2024-12-11"],
2025:["2025-01-15","2025-02-12","2025-03-12","2025-04-10","2025-05-13","2025-06-11","2025-07-15","2025-08-12","2025-09-11","2025-10-24","2025-12-18"],
2026:["2026-01-13","2026-02-13","2026-03-11","2026-04-10","2026-05-12","2026-06-10","2026-07-14","2026-08-12","2026-09-11","2026-10-14","2026-11-10"],
}
SEED=20261114
N=20000
def load():
 if "--stdin-json" in sys.argv:
  raw=json.load(sys.stdin)
 else:
  d=Path(__file__).resolve().parent.parent/"data"
  raw={
   "old":(d/"h10_us_treasury_2y10y_daily_2023_2024.csv").read_text("utf8"),
   "new":(d/"h10_us_treasury_2y_10y_daily_2025_2026.csv").read_text("utf8")
  }
 rows=list(csv.DictReader(io.StringIO(raw["old"])))+list(csv.DictReader(io.StringIO(raw["new"])))
 rows.sort(key=lambda x:x["date"])
 assert len(rows)==967,(len(rows),rows[0],rows[-1])
 assert len({r["date"] for r in rows})==967
 return rows
def monthref(dt):
 year=int(dt[:4]);mo=int(dt[5:7]);return f"{year if mo>1 else year-1:04d}-{mo-1 if mo>1 else 12:02d}"
def study():
 rows=load()
 changes=[]
 for a,b in zip(rows,rows[1:]):
  changes.append(dict(date=b["date"],prior=a["date"],year=int(b["date"][:4]),month=b["date"][:7],
      delta_2y_bp=round(100*(float(b["treasury_2y_pct"])-float(a["treasury_2y_pct"])),4),
      delta_10y_bp=round(100*(float(b["treasury_10y_pct"])-float(a["treasury_10y_pct"])),4)))
 C={r["date"]:r for r in changes}
 release=[(dt,monthref(dt)) for v in BLS_DATES.values() for dt in v]
 assert len(release)==46
 assert len({x for x,y in release})==46
 assert all(dt in C for dt,r in release),[dt for dt,r in release if dt not in C]
 event=[C[dt] for dt,ref in release]
 events={dt for dt,ref in release}
 controls=[x for x in changes if x["date"] not in events]
 assert len(controls)==920
 pools={month:[c for c in controls if c["month"]==month] for month in {e["month"] for e in event}}
 assert all(pools[e["month"]] for e in event)
 def calc(data,seed):
  rng=random.Random(seed)
  obs2=sum(abs(e["delta_2y_bp"]) for e in data)/len(data)
  obs10=sum(abs(e["delta_10y_bp"]) for e in data)/len(data)
  draws2=draws10=hit2=hit10=0
  for i in range(N):
   subset=[rng.choice(pools[e["month"]]) for e in data]
   x=sum(abs(v["delta_2y_bp"]) for v in subset)/len(subset)
   y=sum(abs(v["delta_10y_bp"]) for v in subset)/len(subset)
   draws2+=x;draws10+=y
   hit2+=x>=obs2
   hit10+=y>=obs10
  return dict(n=len(data),abs_2y_cpi_bp=round(obs2,4),abs_10y_cpi_bp=round(obs10,4),
     abs_2y_same_month_placebo_bp=round(draws2/N,4),abs_10y_same_month_placebo_bp=round(draws10/N,4),
     unadjusted_one_sided_p_2y=round((hit2+1)/(N+1),6),
     unadjusted_one_sided_p_10y=round((hit10+1)/(N+1),6))
 stats={
   "all_2023_26":calc(event,SEED),
   "only_2023_24":calc([e for e in event if e["year"]<=2024],SEED),
   "only_2025_26":calc([e for e in event if e["year"]>=2025],SEED),
   "all_except_2026_11_10":calc([e for e in event if e["date"]!="2026-11-10"],SEED),
   "only_2025_26_except_2026_11_10":calc([e for e in event if e["year"]>=2025 and e["date"]!="2026-11-10"],SEED)
 }
 out=io.StringIO()
 w=csv.writer(out,lineterminator="\n")
 w.writerow(["event_date","cpi_reference_month","treasury_prior_trade_date","treasury_2y_delta_bp","treasury_10y_delta_bp","abs_2y_delta_bp","abs_10y_delta_bp","calendar_source","market_source","causal_status"])
 for dt,ref in release:
  r=C[dt]
  src="https://www.bls.gov/schedule/"+str(r["year"])+"/home.htm" if r["year"]<=2024 else "https://www.bls.gov/bls/news-release/cpi.htm"
  w.writerow([dt,ref,r["prior"],r["delta_2y_bp"],r["delta_10y_bp"],abs(r["delta_2y_bp"]),abs(r["delta_10y_bp"]),src,"US_TREASURY_DAILY_PAR_YIELD_CURVE","DESCRIPTIVE_NOT_CAUSAL"])
 stats.update(dict(source_rows=len(rows),calendar_year_counts={str(y):len(d) for y,d in BLS_DATES.items()},non_event_changes=len(controls),
   random_draws=N,random_seed=SEED,
   comparison_limit="22-event 2025-26 evidence extended with 24 pre-2025 observations; same-day market movement includes other announcements; unknown pre-release consensus; exploratory p values not corrected for subgroup testing",
   verification="PASS"))
 return out.getvalue(),stats
if __name__=="__main__":
 out,stats=study()
 print("BEGIN_CSV")
 print(out.rstrip())
 print("END_CSV")
 print("SUMMARY_JSON="+json.dumps(stats))
