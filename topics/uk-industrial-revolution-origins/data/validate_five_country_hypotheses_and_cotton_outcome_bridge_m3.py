#!/usr/bin/env python3
"""TOPIC-010: validate five-country H1-H7 source/counterexample matrix and
three-stage India->British cotton market transition (author's 2005 working paper).

This test establishes only source-admission, internally consistent published
tables and exact arithmetic. No British industrialization causal model run.
The 2005 working-paper reconstruction and 2009 peer-reviewed Broadberry-Gupta
paper are related editions, not independent empirical replications.

python3 validate_five_country_hypotheses_and_cotton_outcome_bridge_m3.py \
    --source-dir . --output /tmp/uk_hypothesis_cotton_bridge.csv
"""
from __future__ import annotations
import argparse,csv,hashlib,sys
from decimal import Decimal
from pathlib import Path
from collections import Counter

MATRIX="five_country_H1_H7_industrialization_competing_hypotheses_matrix_m3.csv"
COTTON="cotton_india_britain_1700_1850_trade_skill_adoption_source_observations_m3.csv"
COUNTRIES={"GBR","NLD","PRT","ESP","FRA"}
HYPOTHESES={"H1","H2","H3","H4","H5","H6","H7"}
PDF_SHA="9a63fff33030510ae2da94fa1384bc8c93c157e0b93d162c3c6c0753409e3638"
EXPECTED_COTTON={1700:Decimal("1.1"),1750:Decimal("2.8"),1770:Decimal("4.8"),
                 1780:Decimal("15.5"),1800:Decimal("59.6"),
                 1830:Decimal("320.7"),1840:Decimal("526.3")}
EXPECTED_TRADE={
 1699:(367,340,20,"1697_fixed_official_prices"),
 1772:(697,701,221,"1697_fixed_official_prices"),
 1784:(1344,395,797,"nominal_current_prices"),
 1794:(1687,1148,3801,"nominal_current_prices"),
 1804:(823,777,16339,"nominal_current_prices"),
 1834:(347,406,22398,"nominal_current_prices")
}
EXPECTED_SPIN={1780:2000,1790:1000,1795:300,1825:135}
METRIC_COLS=["metric","value","unit","source","interpretation_guardrail"]

def csvread(path):
 with path.open(encoding="utf-8-sig",newline="") as f:return list(csv.DictReader(f))

def main():
 p=argparse.ArgumentParser(description=__doc__)
 p.add_argument("--source-dir",type=Path,required=True)
 p.add_argument("--output",type=Path,required=True)
 a=p.parse_args()
 m=csvread(a.source_dir/MATRIX)
 if len(m)!=35:raise ValueError(f"Five-country seven-hypothesis grid must have 35 rows, got {len(m)}")
 counter=Counter()
 for r in m:
  h=r["hypothesis_id"];country=r["country"]
  if h not in HYPOTHESES or country not in COUNTRIES:raise ValueError(f"invalid matrix cell: {h}/{country}")
  counter[h,country]+=1
  if not r["positive_evidence_or_mechanism"] or not r["strongest_counterexample_or_limit"]:
   raise ValueError("A hypothesis cell has no support or falsifier")
  if not r["preliminary_appraisal"] or not r["evidence_grade"]:
   raise ValueError("Interpretation provenance absent")
  if r["causal_effect_replicated"]!="NO":
   raise ValueError("No international causal model has been replicated")
  if r["cross_country_comparability"]!="QUALITATIVE_COMPARABILITY_ONLY_NOT_SAME_ESTIMAND":
   raise ValueError("Wrong cross-country quantitative comparability claim")
  if not all(u.startswith("https://") for u in r["source_urls"].split(";")):
   raise ValueError("Source URL missing or not https")
 if len(counter)!=35 or any(count!=1 for count in counter.values()):
  raise ValueError("Duplicate H x country or missing comparison cell")
 c=csvread(a.source_dir/COTTON)
 if len(c)!=18:raise ValueError("18 numerical published cotton anchors required")
 used=set();raw={};trade={};spin={};indiamarket=None
 for r in c:
  id=r["id"];start=int(r["year_start"]);stop=int(r["year_end"])
  if id in used:raise ValueError("duplicate cotton observation");used.add(id)
  if not (1697<=start<=stop<=1850):raise ValueError("out-of-scope timing")
  if r["working_paper_sha256"]!=PDF_SHA:
   raise ValueError("Wrong verified PDF-version SHA")
  if r["underlying_record_status"]!="ORIGINAL_DAVIS_WADSWORTH_BAINES_ELLISON_RECORDS_NOT_REEXAMINED":
   raise ValueError("Do not imply archive originals directly accessed")
  if not r["primary_author_working_paper_url"].startswith("https://"):
   raise ValueError("Missing publication link")
  if not r["interpretation_guardrail"]:
   raise ValueError("Scope/unit risk omitted")
  val=Decimal(r["value"])
  if id.startswith("COTRAW_"):
   if r["pricing_basis"]!="physical_tonnage" or r["unit"]!="million_lb_per_year" or r["author_source_table"]!="Table_1":
    raise ValueError("Raw cotton usage cannot be mixed with value-of-cloth exports")
   if any(r[z] for z in ("india_to_britain_cotton_imports_gbp_thousand",
                        "indian_cotton_reexports_via_britain_gbp_thousand",
                        "british_cotton_exports_all_markets_gbp_thousand")):
    raise ValueError("Trade source components must not leak into physical raw cotton usage")
   raw[start]=val
  elif id.startswith("COTTRADE_"):
   obs=(int(r["india_to_britain_cotton_imports_gbp_thousand"]),
        int(r["indian_cotton_reexports_via_britain_gbp_thousand"]),
        int(r["british_cotton_exports_all_markets_gbp_thousand"]),
        r["pricing_basis"])
   if obs!=EXPECTED_TRADE.get(start):raise ValueError(f"Published cotton Table 3 figure altered for {start}")
   if r["author_source_table"]!="Table_3" or r["unit"]!="GBP_thousands" or val!=obs[2]:
    raise ValueError("Trade units or export identity error")
   trade[start]=obs
  elif id.startswith("COTSPIN_"):
   if r["author_source_table"]!="Table_8" or r["unit"]!="operative_hours_per_100_lb_fine_yarn":
    raise ValueError("Mechanical frontier is not sector mean labour productivity")
   spin[start]=int(val)
  elif id=="INDMARKET_1831":
   if r["author_source_table"]!="Table_4" or val!=Decimal("3.9"):
    raise ValueError("1831-35 India market British share miscopied")
   indiamarket=val
  else:raise ValueError("Unknown cotton anchor")
 if raw!=EXPECTED_COTTON or trade!=EXPECTED_TRADE or spin!=EXPECTED_SPIN or indiamarket is None:
  raise ValueError("Source table coverage/observations incomplete")
 if trade[1699][3]==trade[1784][3]:
  raise ValueError("Table3 A fixed official value and B nominal values MUST differ")
 if trade[1772][1]<=trade[1772][0]:
  raise ValueError("Expected historical re-export > same-period import anomaly lost (stock/transit)")
 def row(k,v,u,source,guard):
  return dict(zip(METRIC_COLS,[k,str(v),u,source,guard]))
 D=Decimal
 summary=[
  row("matrix_unique_cells",len(counter),"H_by_country_cells","original_TOP-010_hypothesis_contract",
      "Qualitative evidence admission only; no causal coefficients or significance scores"),
  row("cotton_raw_use_growth_1700s_to_1840s",f"{raw[1840]/raw[1700]:.6f}","ratio",
      "Broadberry_Gupta_2005_Table1","Different underlying historic original source periods; gross cotton used not output per worker"),
  row("cotton_raw_use_growth_1770s_to_1840s",f"{raw[1840]/raw[1770]:.6f}","ratio",
      "Broadberry_Gupta_2005_Table1","Raw annual avg million lb, not value of exports or plantation wealth"),
  row("british_export_vs_indian_import_1784_1786",f"{D(trade[1784][2])/D(trade[1784][0]):.6f}","ratio",
      "Broadberry_Gupta_2005_Table3B","Different destinations: UK exports to all vs Indian cloth imports to Britain; descriptive scale only"),
  row("british_export_vs_indian_import_1794_1796",f"{D(trade[1794][2])/D(trade[1794][0]):.6f}","ratio",
      "Broadberry_Gupta_2005_Table3B","Current nominal GBP000; no constant-price comparability to Table3A or causal protection effect"),
  row("british_export_vs_indian_import_1804_1806",f"{D(trade[1804][2])/D(trade[1804][0]):.6f}","ratio",
      "Broadberry_Gupta_2005_Table3B","UK all-market exports divided by UK imports from India not same bilateral competitive market"),
  row("best_practice_spin_hours_1780_to_1825",f"{D(spin[1780])/D(spin[1825]):.6f}","ratio_reduced_hours",
      "Broadberry_Gupta_2005_Table8","Technology frontier hours per 100lb 80s yarn; NOT mean factory industry worker productivity"),
  row("british_share_of_indian_cotton_market_1831_1835",f"{indiamarket:.1f}","percent",
      "Broadberry_Gupta_2005_Table4","Historical Ellison1886 reconstructed Indian market share not a contemporary registry proof"),
 ]
 a.output.parent.mkdir(parents=True,exist_ok=True)
 with a.output.open("w",newline="",encoding="utf-8") as f:
  w=csv.DictWriter(f,fieldnames=METRIC_COLS,lineterminator="\n")
  w.writeheader();w.writerows(summary)
 print(f"PASS matrix_cells={len(counter)} cotton_anchors={len(c)} "
       f"raw_1700to1840_mult={raw[1840]/raw[1700]:.6f} "
       f"tech_frontier_hour_reduction_factor={D(spin[1780])/D(spin[1825]):.6f} "
       "mixed_h6_claim_still_open=YES published_working_paper=NOT_CAUSAL_REPLICATION "
       f"derived_rows={len(summary)} output_sha256={hashlib.sha256(a.output.read_bytes()).hexdigest()}")
if __name__=="__main__":
 try:main()
 except (ValueError,KeyError,OSError,ArithmeticError) as exc:
  print("FAIL",exc,file=sys.stderr);sys.exit(2)
