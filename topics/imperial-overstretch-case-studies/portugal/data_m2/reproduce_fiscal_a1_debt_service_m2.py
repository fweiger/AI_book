#!/usr/bin/env python3
"""CASE-PRT-001: audit official 2024 Anatomy Appendix A1 treasury benchmarks
against 1641–1800 DEBT.PT sovereign debt service.

Important: a benchmark receipt at 1716/1730 is NOT a complete annual
historical state expenditure, and a 1762–1777 nominal mean is not an
observed receipt for any individual year. Debt service is reconstructed,
including observable short maturities; fiscal source terms differ.

Usage (Python 3.10+, no third-party packages):
 python3 reproduce_fiscal_a1_debt_service_m2.py \
 --debt-xlsx ./DEBT_PT_A.xlsx --source-dir . --output-dir ./derived
"""
from __future__ import annotations
import argparse,csv,hashlib,math
from pathlib import Path
from reproduce_debtpt_annual_ratios_m2 import (
    EXPECTED_DEBT_SHA256, read_workbook_sheet, annual
)

APPENDIX="fiscal_nominal_revenue_benchmarks_appendix_a1_2024_m2.csv"
DEBT_RATIOS="debtpt_annual_debt_gdp_ratios_1641_1800_m2.csv"
OUT_MAIN="fiscal_a1_explicit_years_vs_debt_service_m2.csv"
OUT_1748="debt_1748_published_vs_current_source_window_m2.csv"

HEAD_MAIN=[
    "year_start","year_end","n_years",
    "fiscal_appendix_nominal_central_receipt_annual_mean_contos",
    "debtpt_mean_annual_recorded_debt_service_contos",
    "descriptive_ratio_debt_service_to_nominal_receipts_pct",
    "fiscal_observation_type","original_appendix_cited_source",
    "caveat"
]
HEAD_1748=[
    "year","current_debtpt_plus_2019_gdp_debt_pct_gdp",
    "rounded_nearest_integer_pct","published_2024_table1_pct_if_listed",
    "published_minus_reconstructed_pct_points",
    "not_proven_source_cause"
]
def read_csv(path):
    with path.open("r",encoding="utf-8-sig",newline="") as fd:return list(csv.DictReader(fd))
def out_csv(path,cols,rows):
    with path.open("w",encoding="utf-8",newline="") as fd:
        w=csv.DictWriter(fd,fieldnames=cols,lineterminator="\n")
        w.writeheader();w.writerows(rows)

def main():
    pa=argparse.ArgumentParser(description=__doc__)
    pa.add_argument("--debt-xlsx",type=Path,required=True)
    pa.add_argument("--source-dir",type=Path,default=Path(__file__).resolve().parent)
    pa.add_argument("--output-dir",type=Path,required=True)
    args=pa.parse_args()
    sha=hashlib.sha256(args.debt_xlsx.read_bytes()).hexdigest()
    if sha!=EXPECTED_DEBT_SHA256:raise ValueError("DEBT.PT source SHA-256 does not match locked version")
    service=annual(read_workbook_sheet(args.debt_xlsx,3),"C",["D","E","F"],1641,1800)
    fiscal=read_csv(args.source_dir/APPENDIX)
    ratios=read_csv(args.source_dir/DEBT_RATIOS)
    assert len(fiscal)==36 and len(ratios)==160
    existing={int(r["year"]):float(r["total_recorded_debt_stock_pct_nominal_gdp"]) for r in ratios}
    if sorted(existing)!=list(range(1641,1801)):raise ValueError("annual debt panel years incomplete")

    matched=[]
    for a in fiscal:
        start,end=int(a["year_start"]),int(a["year_end"])
        if not (1641<=start and end<=1800):continue
        if end>start and (start,end)!=(1762,1777):
            raise ValueError("unexpected multi-year interval")
        rev=float(a["nominal_central_revenue_contos"])
        if not rev>0:raise ValueError("nonpositive revenue")
        avg_service=sum(service[y]["F"] for y in range(start,end+1))/(end-start+1)/1e6
        matched.append(dict(zip(HEAD_MAIN,[
            start,end,end-start+1,f"{rev:.6f}",f"{avg_service:.6f}",
            f"{100*avg_service/rev:.6f}",a["window_type"],
            a["published_original_source"],
            ("DESCRIPTIVE_RATIO_TO_BENCHMARK_NOT_FULL_ANNUAL_SPENDING;REPORTS_PERIOD_AVERAGE"
                if end>start else
             "DESCRIPTIVE_SAME_YEAR_SOURCE_MIX_NOT_MODERN_EXHAUSTIVE_CASH_BUDGET")
        ])))
    matched.sort(key=lambda x:int(x["year_start"]))
    if len(matched)!=7:raise ValueError("Expected 6 single-year + one multi-year entries; actual "+str(len(matched)))
    assert (int(matched[-1]["year_start"]),int(matched[-1]["year_end"]))==(1762,1777)

    around=[]
    published={1748:9.,1757:9.}
    for y in range(1743,1758):
        calc=existing[y]
        pub=published.get(y)
        around.append(dict(zip(HEAD_1748,[
            y,f"{calc:.6f}",round(calc),f"{pub:.0f}" if pub is not None else "",
            f"{pub-calc:.6f}" if pub is not None else "",
            "DIFFERENCE_UNRESOLVED_POSSIBLE_VERSION_OR_DEFINITION"
        ])))
    assert round(existing[1748])==8 and round(existing[1757])==9
    # Table1 displays 1748=9, which is NOT obtained by ordinary integer rounding of 8.152251.
    assert abs(existing[1748]-8.152251)<1e-6
    args.output_dir.mkdir(parents=True,exist_ok=True)
    for name,fields,rows in [(OUT_MAIN,HEAD_MAIN,matched),(OUT_1748,HEAD_1748,around)]:
        dest=args.output_dir/name
        out_csv(dest,fields,rows)
        print(name,"rows",len(rows),"sha256",hashlib.sha256(dest.read_bytes()).hexdigest())
    print("PASS appendix_a1_rows=36 matched_revenue_entries=7 debt_local_window=15 year1748_table_conflict=OPEN")
if __name__=="__main__":main()
