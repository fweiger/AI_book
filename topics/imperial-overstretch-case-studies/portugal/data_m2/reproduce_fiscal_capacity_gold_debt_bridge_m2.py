#!/usr/bin/env python3
"""CASE-PRT-001 M2: published fiscal capacity x independently reproduced debt and gold.

Stand-alone chronological *descriptive* bridge, NOT an imperial fiscal ROI or
ASCM causal estimate. Period revenue/GDP comes from a published sparse-benchmark
study, NOT from a recovered annual revenue panel. Gross gold remittances and
recorded debt service are different components, not linked ledger entries.

Run from the data_m2/ directory with two separately downloaded author XLSX files:
python3 reproduce_fiscal_capacity_gold_debt_bridge_m2.py \
 --debt-xlsx /path/DEBT_PT_A.xlsx --gdp-xlsx /path/PalmaReis_2019.xlsx \
 --source-dir . --output-dir ./reproduced
"""
from __future__ import annotations
import argparse,csv,hashlib,math
from pathlib import Path
from reproduce_debtpt_annual_ratios_m2 import (
 EXPECTED_DEBT_SHA256, EXPECTED_GDP_SHA256, read_workbook_sheet,annual
)

FISCAL_NAME="fiscal_revenue_with_without_empire_2024_table3_m2.csv"
ANNUAL_NAME="debtpt_annual_debt_gdp_ratios_1641_1800_m2.csv"
GOLD_NAME="gold_remittances_fiveyear_b1_1720_1804_m2.csv"
SOUSA_NAME="sousa_2008_decadal_gold_private_public_m2.csv"
OUT_FISCAL="fiscal_revenue_vs_debt_service_periods_m2.csv"
OUT_GOLD="public_gold_vs_debt_service_matched_periods_m2.csv"
FISCAL_FIELDS=["start_year","end_year","n_years",
 "published_central_revenue_with_empire_pct_gdp",
 "published_central_revenue_without_empire_pct_gdp",
 "implied_published_net_empire_gdp_percentage_points",
 "mean_debt_service_pct_gdp_from_annual_panel",
 "mean_debt_stock_pct_gdp_from_annual_panel",
 "illustrative_service_to_revenue_ratio_of_period_means_pct",
 "illustrative_service_to_published_net_empire_ratio_of_period_means_pct",
 "not_an_actual_annual_expenditure_share","fiscal_source"]
GOLD_FIELDS=["start_year","end_year","n_years",
 "debt_service_sum_million_reis",
 "nominal_gdp_sum_million_reis",
 "public_gold_2025_sum_million_reis",
 "public_gold_2008_estimate_from_rounded_annual_means_million_reis",
 "gold_public_2025_to_debt_service_pct",
 "gold_public_2008_to_debt_service_pct",
 "public_gold_versions_difference_million_reis",
 "debt_service_sum_pct_of_nominal_gdp",
 "public_gold_2025_sum_pct_of_nominal_gdp",
 "source_debt","source_gold_2025","source_gold_2008"]

def read(path):
 with path.open(encoding="utf-8-sig",newline="") as f:return list(csv.DictReader(f))
def write(path,fields,rows):
 with path.open("w",encoding="utf-8",newline="") as f:
  w=csv.DictWriter(f,fieldnames=fields,lineterminator="\n");w.writeheader();w.writerows(rows)
def pct(v):return f"{v:.6f}"

def main():
 p=argparse.ArgumentParser(description=__doc__)
 p.add_argument("--debt-xlsx",type=Path,required=True)
 p.add_argument("--gdp-xlsx",type=Path,required=True)
 p.add_argument("--source-dir",type=Path,default=Path(__file__).resolve().parent)
 p.add_argument("--output-dir",type=Path,required=True)
 opt=p.parse_args()
 for label,path,expected in [("DEBT.PT",opt.debt_xlsx,EXPECTED_DEBT_SHA256),
                             ("2019 GDP",opt.gdp_xlsx,EXPECTED_GDP_SHA256)]:
  sha=hashlib.sha256(path.read_bytes()).hexdigest()
  if sha!=expected:raise ValueError(f"{label} raw source hash mismatch: {sha}")
 debt_service=annual(read_workbook_sheet(opt.debt_xlsx,3),"C",["D","E","F"],1641,1800)
 gdp=annual(read_workbook_sheet(opt.gdp_xlsx,2),"A",["H"],1527,1850)
 source_dir=opt.source_dir
 ar=read(source_dir/ANNUAL_NAME)
 assert len(ar)==160 and [int(r["year"]) for r in ar]==list(range(1641,1801))
 for r in ar:
  yr=int(r["year"])
  computed=100*debt_service[yr]["F"]/(gdp[yr]["H"]*1e6)
  if abs(computed-float(r["total_recorded_debt_service_pct_nominal_gdp"]))>1e-6:
   raise ValueError(f"Published derived debt/GDP mismatch {yr}")
 fiscal=read(source_dir/FISCAL_NAME)
 assert [(int(r["period_start"]),int(r["period_end"])) for r in fiscal]==[
  (1650,1699),(1700,1749),(1750,1799)]
 fiscal_out=[]
 for q in fiscal:
  start,end=int(q["period_start"]),int(q["period_end"])
  a=[r for r in ar if start<=int(r["year"])<=end]
  assert len(a)==50
  revenue=float(q["central_revenue_with_empire_pct_gdp"])
  no_empire=float(q["central_revenue_without_empire_pct_gdp"])
  empire_pp=float(q["net_imperial_contribution_gdp_percentage_points"])
  assert math.isclose(revenue-no_empire,empire_pp,abs_tol=1e-10)
  mean_s=sum(float(r["total_recorded_debt_service_pct_nominal_gdp"]) for r in a)/len(a)
  mean_d=sum(float(r["total_recorded_debt_stock_pct_nominal_gdp"]) for r in a)/len(a)
  fiscal_out.append(dict(zip(FISCAL_FIELDS,[
   start,end,50,pct(revenue),pct(no_empire),pct(empire_pp),
   pct(mean_s),pct(mean_d),pct(100*mean_s/revenue),
   pct(100*mean_s/empire_pp),
   "TRUE__ratio_of_separately_published_period_summaries__NOT_actual_yearwise_budget_share",
   "Costa_Henriques_Palma_2024_Table3"
  ])))
 gold=read(source_dir/GOLD_NAME)
 sousa=read(source_dir/SOUSA_NAME)
 assert len(gold)==17
 q2008={q["period"]:float(q["state_average_annual_contos"]) for q in sousa}
 gold_out=[]
 for start,end in [(1720,1749),(1750,1779),(1780,1799)]:
  valid=[q for q in gold if start<=int(q["year_start"]) and int(q["year_end"])<=end]
  expected=[(start+i,start+i+4) for i in range(0,end-start+1,5)]
  assert [(int(q["year_start"]),int(q["year_end"])) for q in valid]==expected
  public_2025=sum(float(q["public_nominal_million_reis"]) for q in valid)
  old_public=sum(q2008[f"{y}-{y+9}"]*10 for y in range(start,end+1,10))
  service=sum(debt_service[y]["F"] for y in range(start,end+1))/1e6
  nom_gdp=sum(gdp[y]["H"] for y in range(start,end+1))
  assert service>0 and nom_gdp>0 and public_2025>0
  gold_out.append(dict(zip(GOLD_FIELDS,[
   start,end,end-start+1,pct(service),pct(nom_gdp),pct(public_2025),
   pct(old_public),pct(100*public_2025/service),
   pct(100*old_public/service),pct(public_2025-old_public),
   pct(100*service/nom_gdp),pct(100*public_2025/nom_gdp),
   "DEBT_PT_A_DEBT_SERVICE_F", "Kedrosky_Palma_2025_Suppl_B1",
   "Sousa_2008_Table2_decadal_annual_averages_rounded_to_contos"
  ])))
 assert int(float(gold_out[2]["public_gold_versions_difference_million_reis"]))==-1727
 out=opt.output_dir
 out.mkdir(parents=True,exist_ok=True)
 for name,fields,rows in [(OUT_FISCAL,FISCAL_FIELDS,fiscal_out),
                          (OUT_GOLD,GOLD_FIELDS,gold_out)]:
  dest=out/name;write(dest,fields,rows)
  print(name,"rows",len(rows),"sha256",hashlib.sha256(dest.read_bytes()).hexdigest())
 print("PASS published_table3_periods=3 matched_gold_periods=3 ratio_definitions=EXPLICIT")
if __name__=="__main__":main()
