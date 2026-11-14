#!/usr/bin/env python3
"""QA of Sousa (2003) treasury-gold stocks, state Mint coinage and deposit loans.

Original source: Sousa, Rita Martins de (2003), Análise Social 38(168)
'Moeda e Estado: políticas monetárias e determinantes da procura (1688-1797)'
pp. 788-790, https://revistas.rcaap.pt/analisesocial/article/download/35368/24541/156638

The eight small published observations are all different STOCK, FLOW and
retrospective loan constructs. This script checks arithmetic/provenance
but neither inspects original ANTT manuscripts nor establishes military
causality, a shared end-of-year cash series or a 1766 loan receipt ledger.
"""
from __future__ import annotations
import argparse,csv,hashlib,sys
from pathlib import Path
from urllib.parse import urlparse

EXPECTED={
 "PRT_1763_MINTING":("1763","state_gold_coinage_flow",1794),
 "PRT_1763_GOLD_TREASURY":("1763-12-31","royal_treasury_gold_asset_stock",835),
 "PRT_1765_GOLD_TREASURY":("1765","royal_treasury_gold_asset_stock",76.8),
 "PRT_1767_GOLD_TREASURY":("1767","royal_treasury_gold_asset_stock",67.2),
 "PRT_1766_STATE_LOAN":("1766","public_deposit_fund_loan_to_treasury_retro_1777",371.4),
 "PRT_1766_MINTING":("1766","state_gold_coinage_flow",1073),
 "PRT_1777_JUNTA_ALL_OUTSTANDING":("1777","public_deposit_fund_all_borrowers_loan_stock",673),
 "PRT_1798_TREASURY_JUNTA_LOAN":("1798","public_deposit_fund_treasury_loan_reported_amount",1616)
}
def main():
 p=argparse.ArgumentParser(description=__doc__)
 p.add_argument("--source",type=Path,required=True)
 a=p.parse_args()
 with a.source.open(newline="",encoding="utf-8-sig") as f:rows=list(csv.DictReader(f))
 if len(rows)!=len(EXPECTED) or {r["claim_id"] for r in rows}!=set(EXPECTED):
  raise ValueError("Expected all eight unique 1760–1798 fiscal benchmarks")
 vals={}
 for r in rows:
  date,typ,num=EXPECTED[r["claim_id"]]
  if (r["observed_date_or_year"],r["measure_class"])!=(date,typ):
   raise ValueError(f"Date/stock/flow classification changed {r['claim_id']}")
  if not r["published_source_url"].startswith("https://revistas.rcaap.pt/"):
   raise ValueError("No official academic publication provenance")
  u=urlparse(r["published_source_url"])
  if u.scheme!="https" or not u.netloc:raise ValueError("Invalid source URL")
  if "ORIGINAL_ARCHIVE_VERIFIED" in r["verification_grade"]:
   raise ValueError("Original ANTT manuscript NOT reviewed")
  if r["currency_unit"]!="contos":raise ValueError("Wrong monetary units")
  val=float(r["amount_nominal"])
  if abs(val-num)>1e-9:raise ValueError(f"Published amount altered {r['claim_id']}")
  if not r["noncomparable_account_warning"]:raise ValueError("Missing scope warning")
  vals[r["claim_id"]]=val
 if "not 1777 newly lent cash" not in next(r for r in rows if r["claim_id"]=="PRT_1766_STATE_LOAN")["noncomparable_account_warning"]:
  raise ValueError("Retrospective 1766 loan may not be treated as 1777 issuance")
 for id in ["PRT_1765_GOLD_TREASURY","PRT_1767_GOLD_TREASURY"]:
  if "Exact month/day not supplied" not in next(r for r in rows if r["claim_id"]==id)["noncomparable_account_warning"]:
   raise ValueError("Do not invent month/day for a stock balance")
 share=100*vals["PRT_1766_STATE_LOAN"]/vals["PRT_1777_JUNTA_ALL_OUTSTANDING"]
 if round(share,1)!=55.2:raise ValueError("Published 55.2% Junta share fails")
 print(f"PASS data_rows={len(rows)} measures=gold_treasury_stock|state_gold_coinage_flow|public_deposit_loan "
       f"reconstructed_1766_loan_share_of_1777_all_outstanding={share:.6f}% "
       "archival_manuscripts=NOT_ACQUIRED fiscal_cash_causality=NOT_RUN "
       f"sha256={hashlib.sha256(a.source.read_bytes()).hexdigest()}")
if __name__=="__main__":
 try:main()
 except (ValueError,KeyError,OSError) as e:
  print(f"FAIL {e}",file=sys.stderr);sys.exit(2)
