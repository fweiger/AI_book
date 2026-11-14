#!/usr/bin/env python3
"""CASE-PRT-001 M3: 2019 Rodrigues public debt primary/secondary split.

Reproduce a NEW arithmetic reconciliation using only dates, principal amounts
and whether Table 5 describes a payment DIRECT to royal treasury.
Source: Lisbeth Rodrigues, 'Os padrões de juro da Misericórdia de Lisboa,
1767–1797', Ler História 74 (2019), Tables 4-5;
https://doi.org/10.4000/lerhistoria.4730
Original article openly licensed CC BY-NC 4.0; this is an attributed
limited-item numerical transcription, not copied PDF or table text.
No actual archival manuscripts have been accessed.

Important:
- 20 Table 5 entries; exactly one principal displayed as a DASH;
  NEVER silently impute it as zero or invent its amount.
- Table 4 published total = 195,509,941 reis. Summing the 19 observed
  Table 5 principals = 179,853,941 reis, so 15,656,000 reis remains
  unassigned between the two published tables; DO NOT ascribe it to
  the single dashed row without source confirmation.
- Five treasury-direct assignments (106,773,748 reis) purchased public
  debt from the treasury but were earmarked to pay older royal creditors;
  NOT automatically net new government borrowing.
- Historic 1775 legislation restricting this one charity's private
  lending is NOT a quasi-experimental identification without a
  comparator and genuine pretrend/credit-default checks.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
from pathlib import Path

SOURCE_URL="https://journals.openedition.org/lerhistoria/4730"
SOURCE_DOI="https://doi.org/10.4000/lerhistoria.4730"
PUBLISHED_TABLE4_SUM_REIS=195_509_941

# Original authors' Table 5 DATE and PRINCIPAL only; omit sellers' names,
# source private-person details, tax coffer metadata and quotation.
# Type = T: explicitly delivered to royal treasury for creditor replacement;
# S: secondary-market bond from another holder. Dashed principal = None.
TABLE5=(
 ("1782-12-23",18_000_000,"T"),
 ("1783-06-17",92_000,"S"),
 ("1784-03-16",1_474_800,"S"),
 ("1784-04-26",750_000,"S"),
 ("1784-04-26",700_000,"S"),
 ("1784-04-26",50_000_000,"S"),
 ("1784-05-04",2_905_928,"S"),
 ("1784-06-05",5_236_564,"S"),
 ("1784-09-11",2_400_000,"T"),
 ("1784-10-27",1_559_024,"T"),
 ("1785-03-21",500_000,"S"),
 ("1786-02-08",None,"S"),
 ("1786-02-18",4_657_815,"S"),
 ("1786-04-06",500_000,"S"),
 ("1788-01-24",600_000,"S"),
 ("1788-01-24",804_370,"S"),
 ("1788-12-13",2_000_000,"S"),
 ("1790-01-01",14_814_724,"T"),
 ("1790-02-25",70_000_000,"T"),
 ("1792-04-07",2_858_716,"S"),
)

COLUMNS=[
 "metric","records_in_2019_table5","known_principal_nominal_reis",
 "known_principal_contos","percent_of_table5_observed_known_sum",
 "percent_of_2019_table4_published_total",
 "evidence_status","interpretation_warning","source_doi"
]

def fmt(value):
    return f"{value:.6f}"

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output",required=True,type=Path)
    x=parser.parse_args()
    if len(TABLE5)!=20 or sum(v is None for _,v,_ in TABLE5)!=1:
        raise ValueError("Published Table 5 count and missingness changed")
    if any(kind not in ("T","S") for _,_,kind in TABLE5):
        raise ValueError("Unrecognized issuer/secondary-market status")
    if [date for date,_,_ in TABLE5]!=sorted(date for date,_,_ in TABLE5):
        raise ValueError("Date ordering changed")
    known=sum(v for _,v,_ in TABLE5 if v is not None)
    treasury=sum(v for _,v,kind in TABLE5 if v is not None and kind=="T")
    secondary=sum(v for _,v,kind in TABLE5 if v is not None and kind=="S")
    unknown_count=sum(1 for _,v,_ in TABLE5 if v is None)
    direct_count=sum(1 for _,_,kind in TABLE5 if kind=="T")
    secondary_count=sum(1 for _,_,kind in TABLE5 if kind=="S")
    treasury_1790=sum(v for date,v,kind in TABLE5
                      if date.startswith("1790") and kind=="T")
    mismatch=PUBLISHED_TABLE4_SUM_REIS-known
    if (known,treasury,secondary,unknown_count,direct_count,secondary_count,
        treasury_1790,mismatch)!=(179_853_941,106_773_748,73_080_193,
                                  1,5,15,84_814_724,15_656_000):
        raise ValueError("Publisher's Table4/Table5 arithmetic no longer matches")

    def r(metric,n,amount,status,warning):
        return dict(zip(COLUMNS,[
            metric,n,amount if amount is not None else "",
            fmt(amount/1e6) if amount is not None else "",
            fmt(100*amount/known) if amount is not None else "",
            fmt(100*amount/PUBLISHED_TABLE4_SUM_REIS) if amount is not None else "",
            status,warning,SOURCE_DOI]))
    result=[
      r("published_table4_all_acquisitions","",PUBLISHED_TABLE4_SUM_REIS,
        "PUBLISHED_TOTAL_FROM_TABLE4",
        "Fiscal-year investment accounts; not reconciled to every Table5 line"),
      r("table5_all_20_records_with_19_known_principals",20,known,
        "SUM_OF_19_RECORDED_AMOUNTS",
        "One additional Table5 bond has principal displayed as dash—not zero"),
      r("table5_treasury_direct_creditor_replacement",direct_count,treasury,
        "EXPLICIT_TREASURY_DELIVERY",
        "Money delivered to sovereign Treasury to satisfy existing creditors; not net borrowing"),
      r("table5_secondary_bonds_14_known",secondary_count,secondary,
        "14_KNOWN_OF_15_SECONDARY",
        "15 secondary contracts in total; one principal unreported"),
      r("table5_secondary_unobserved_principal",unknown_count,None,
        "NOT_ACQUIRED",
        "Do not impute 15656000 reis as this missing row without original ledger"),
      r("table4_minus_19_known_table5_principals","",mismatch,
        "SOURCE_TABLE_RECONCILIATION_OPEN",
        "Difference could be missing/unlisted or different measurement conventions"),
      r("treasury_direct_year_1790",2,treasury_1790,
        "TWO_PUBLISHED_1790_DIRECT_OBSERVATIONS",
        "Both earmarked for redemption of earlier creditors"),
    ]
    x.output.parent.mkdir(parents=True,exist_ok=True)
    with x.output.open("w",newline="",encoding="utf-8") as f:
        w=csv.DictWriter(f,fieldnames=COLUMNS,lineterminator="\n")
        w.writeheader()
        w.writerows(result)
    print(f"PASS 2019_20_table5_entries=20 observed_principals=19 "
          f"treasury_count=5 secondary_count=15 "
          f"table5_known_reis={known} table4_published_reis={PUBLISHED_TABLE4_SUM_REIS} "
          f"unreconciled_reis={mismatch} treasury_observed_share_pct={100*treasury/known:.6f} "
          f"treasury_as_share_table4_pct={100*treasury/PUBLISHED_TABLE4_SUM_REIS:.6f} "
          f"output_sha256={hashlib.sha256(x.output.read_bytes()).hexdigest()}")

if __name__=="__main__":
    main()
