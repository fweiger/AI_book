#!/usr/bin/env python3
"""PJM historical forecast-vintage backtest. Retrospective, not causal.
Usage: python3 analysis/recompute_h03_vintage_calibration.py
       python3 analysis/recompute_h03_vintage_calibration.py --input /path/to/2026-accuracy-report.xlsx
Source XLSX SHA and 2023/2024/2025 vintage release dates are archived in CSV.
No nonstandard dependencies. Original workbook is not committed to GitHub.
"""
from __future__ import annotations
import argparse,csv,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
SHA="e0f24fe03a79af016826089c653b2c2e15e55edcb04a7bd4be5fa643136425fc"
RELEASE={"2023":"2023-05-22","2024":"2023-12-27","2025":"2025-01-24"}
def load(name):
 with (ROOT/"data"/name).open(encoding="utf-8",newline="") as f:return list(csv.DictReader(f))
def near(a,b,eps=.000005):assert abs(a-b)<eps,(a,b)
def main():
 p=argparse.ArgumentParser();p.add_argument("--input",type=Path);opts=p.parse_args()
 rows=load("h03_pjm_load_forecast_vintage_backtest_2023_2025.csv")
 score=load("h03_pjm_2025_paired_vintage_scorecard.csv")
 cra=load("h03_cra_nov2026_scenario_assumptions.csv")
 assert (len(rows),len(score),len(cra))==(31,2,10)
 assert len({(r["zone"],r["target_year"],r["forecast_vintage"]) for r in rows})==31
 assert all(r["source_sha256"]==SHA for r in rows+score)
 observed={}
 for r in rows:
  year=int(r["target_year"]);vintage=int(r["forecast_vintage"])
  assert vintage<=year and r["vintage_original_publish_date"]==RELEASE[str(vintage)]
  assert r["observed_actual_asof_date"]=="2026-05-29"
  f=float(r["forecast_mw"]);a=float(r["actual_mw"])
  assert f>0 and a>0
  near(float(r["signed_error_mw"]),a-f,.000002)
  near(float(r["signed_error_div_forecast_pct"]),100*(a/f-1),.000002)
  near(float(r["abs_error_div_actual_pct"]),100*abs(a-f)/a,.000002)
  key=(r["zone"],year)
  if key in observed:near(observed[key],a)
  observed[key]=a
 assert all(r["zone_role"]=="RTO_AGGREGATE" for r in rows if r["zone"]=="RTO")
 assert all(r["zone_role"]=="DOM_CHILD" for r in rows if r["zone"].startswith("DOM - "))
 out={}
 for vintage in (2024,2025):
  subset=[r for r in rows if r["target_year"]=="2025" and r["forecast_vintage"]==str(vintage) and r["zone"] in ("DOM","AEP","PS")]
  assert len(subset)==3 and {r["zone"] for r in subset}=={"DOM","AEP","PS"}
  fc=sum(float(r["forecast_mw"]) for r in subset)
  ac=sum(float(r["actual_mw"]) for r in subset)
  ae=sum(abs(float(r["actual_mw"])-float(r["forecast_mw"])) for r in subset)
  wape=100*ae/ac
  mape=sum(float(r["abs_error_div_actual_pct"]) for r in subset)/3
  s=next(x for x in score if x["vintage"]==str(vintage))
  for key,val in [("forecast_mw_sum",fc),("actual_mw_sum",ac),("sum_absolute_error_mw",ae),
                  ("WAPE_abs_error_div_actual_pct",wape),("MAPE_mean_abs_error_div_actual_pct",mape),
                  ("net_actual_minus_forecast_mw",ac-fc)]:near(float(s[key]),val,.000005)
  out[str(vintage)]={"forecast_mw":round(fc,3),"actual_mw":round(ac,3),
                    "absolute_error_mw":round(ae,3),"WAPE_pct":round(wape,3),"MAPE_pct":round(mape,3)}
 assert out["2025"]["WAPE_pct"]>out["2024"]["WAPE_pct"]
 assert out["2025"]["MAPE_pct"]<out["2024"]["MAPE_pct"]
 cm=next(r for r in cra if r["assumption_id"]=="CRA-2030-POWER-GAP")
 assert cm["numeric_value"]=="11.5" and cm["epistemic_status"]=="FUTURE_SCENARIO"
 assert all(r["source_published_at"]=="2026-11-02" for r in cra)
 if opts.input:
  from recompute_h03_pjm_accuracy import source_rows
  source=source_rows(opts.input)
  for r in rows:
   index=source[r["zone"]]["_index"];yr=r["target_year"];v=r["forecast_vintage"]
   near(float(r["forecast_mw"]),index[yr,f"{v} Load Forecast July Peak"],.000001)
   near(float(r["actual_mw"]),index[yr,"Historical July Peak"],.000001)
 def detail(zone,v):
  r=next(r for r in rows if r["zone"]==zone and r["target_year"]=="2025" and r["forecast_vintage"]==str(v))
  return {"forecast_mw":float(r["forecast_mw"]),"actual_mw":float(r["actual_mw"]),
          "bias_vs_forecast_pct":round(float(r["signed_error_div_forecast_pct"]),3)}
 print(json.dumps({"source_xlsx_crosscheck":bool(opts.input),"matched_records":len(rows),
  "paired_three_primary_zones_one_target_year":out,
  "WAPE_worsening_percentage_points":round(out["2025"]["WAPE_pct"]-out["2024"]["WAPE_pct"],3),
  "MAPE_improvement_percentage_points":round(out["2024"]["MAPE_pct"]-out["2025"]["MAPE_pct"],3),
  "Dominion_2025_target_by_vintage":{str(v):detail("DOM",v) for v in (2023,2024,2025)},
  "RTO_2025_target_by_vintage":{str(v):detail("RTO",v) for v in (2023,2024,2025)},
  "CRA_2030_hard_supply_shortfall_GW_approx":11.5,
  "statistical_significance":"NOT_TESTED__SMALL_PAIRED_SAMPLE",
  "policy_causality":"UNTESTED"},ensure_ascii=False,indent=2))
if __name__=="__main__": main()
