#!/usr/bin/env python3
"""Audit 10 truly dated forecasts vs NOT-PIT retrospective 46-date vendor forecasts.
It is not a test of which forecaster was correct: source types/institutions differ.
"""
import csv,io,json,sys
from pathlib import Path
def read():
 if "--stdin-json" in sys.argv:src=json.load(sys.stdin)
 else:
  d=Path(__file__).resolve().parent.parent/"data"
  src={"dated":(d/"h10_cpi_pre_release_dated_forecasts_10events_2023_2026.csv").read_text("utf8"),
       "archive":(d/"h10_cpi_release_ust_46event_vendor_archive_not_pit.csv").read_text("utf8")}
 return {k:list(csv.DictReader(io.StringIO(v))) for k,v in src.items()}
def inspect():
 sources=read();a=sources["dated"];b={r["release_date"]:r for r in sources["archive"]}
 assert len(a)==10 and len(b)==46
 comparisons=[];absent=[]
 for r in a:
  other=b.get(r["release_date"])
  if other is None:raise ValueError("missing date")
  for category in ["headline","core"]:
   f=r["forecast_"+category+"_mom_sa_percent"]
   z=other[category+"_forecast_archived_mom_pct"]
   if f and z:
    difference=round(float(f)-float(z),6)
    comparisons.append({"date":r["release_date"],"dimension":category,"dated_published_forecast":float(f),
           "not_pit_archive_forecast":float(z),"dated_minus_archive_pp":difference,
           "original_dated_forecast_type":r["forecast_type"]})
   else:absent.append({"date":r["release_date"],"dimension":category})
 material=[x for x in comparisons if abs(x["dated_minus_archive_pp"])>=0.075]
 return {"verification":"PASS","dated_forecast_events":10,"retrospective_archive_events":46,
  "overlap_headline_comparisons":sum(x["dimension"]=="headline" for x in comparisons),
  "overlap_core_comparisons":sum(x["dimension"]=="core" for x in comparisons),
  "unusable_date_dim_due_missing_archive":len(absent),
  "material_disagreements_threshold_pp":0.075,
  "material_disagreements":material,
  "notes":"Calendar URL has historical date but actual values inserted after release. Pre-published forecasts and vendor retrospective forecasts may represent different institutions, concepts, rounding, or later revisions; NOT independent proof of deliberate alteration."}
if __name__=="__main__":
 print("SUMMARY_JSON="+json.dumps(inspect(),ensure_ascii=False))
