#!/usr/bin/env python3
"""Check PJM July 2026 midyear informational macro-only summer peak revision.
This is TOTAL coincident summer peak, NOT data-center-only or actual demand.
"""
from __future__ import annotations
import csv, json
from pathlib import Path
P = Path(__file__).resolve().parents[1] / "data" / "h03_pjm_2026_july_macro_only_revisions.csv"
SHA="8c2ed5a594c501718dc29755cb044b9d6bcbeac48fc751a6c25014ae1f99a94c"
with P.open(encoding="utf-8",newline="") as h: rows=list(csv.DictReader(h))
assert len(rows)==20, len(rows)
assert len({(r["planning_year"],r["pjm_zone"]) for r in rows})==20
for r in rows:
    assert r["source_sha256"]==SHA
    assert r["metric_scope"]=="SUMMER_COINCIDENT_PEAK_TOTAL_ALL_SECTORS"
    assert "Informational only" in r["source_limit"]
    jan=float(r["jan_2026_forecast_peak_mw"]); jul=float(r["july_2026_informational_peak_mw"])
    assert abs((jul-jan)-float(r["revision_mw"]))<0.01
    assert abs(100*(jul/jan-1)-float(r["revision_pct"]))<0.0002
rto=[r for r in rows if r["pjm_zone"]=="RTO"]
assert [r["planning_year"] for r in rto]==["2026/27","2027/28","2028/29","2029/30"]
assert [int(r["revision_mw"]) for r in rto]==[613,593,550,641]
assert [int(r["revision_mw"]) for r in rows if r["planning_year"]=="2027/28" and r["pjm_zone"]=="DOM"]==[-30]
print(json.dumps({
 "source_file_rows":len(rows),
 "source_sha256":SHA,
 "RTO_revision_2027_28_MW":593,
 "RTO_revision_2027_28_pct":round(100*593/160449,3),
 "DOM_revision_2027_28_MW":-30,
 "source_note":"July 2026 is FOR INFORMATION ONLY; Moody's June 2026 economics refresh, other assumptions & model structure unchanged",
 "not_a_political_effect":True,
 "not_data_center_only":True
},ensure_ascii=False,indent=2))
