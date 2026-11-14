#!/usr/bin/env python3
"""CASE-PRT-001 M3 source audit for early tax-backed credit & 1749/1750 edict.

Validate nine attributed historical claims, their currencies, account types,
publication provenance and date conflict. This test DOES NOT independently
verify inaccessible 1647/1704 loan contracts, 1883 law p318, nor original
1743/1744 Mint accounts. Numerically adjacent entries are NOT cash flow links.
Usage: python3 validate_pre_gold_credit_collateral_and_edict_dispute_m3.py --source ./file.csv
"""
from __future__ import annotations
import argparse,csv,hashlib,datetime,sys
from collections import Counter
from pathlib import Path
from urllib.parse import urlparse

SOURCE_COLUMNS=[
"claim_id","date_start","date_end","claim_class","amount","unit",
"interest_rate_or_new_rate_pct","tax_or_institution",
"historical_source_definition","source_url","specific_page",
"evidence_level","accounting_or_date_caveat"
]
IDS=[
"PRT_PRE_GOLD_1647_SUGAR_COLLATERAL","PRT_1662_INFANTRY_LOAN",
"PRT_1704_1706_CUSTOMS","PRT_1743_COUPON_REDUCTION",
"PRT_1743_1744_STATE_GOLD_COINS","PRT_1743_1744_REFUND_ESTIMATE",
"PRT_1749_DATE_CLAIM_AZEVEDO","PRT_1749_DATE_CLAIM_SOUSA",
"PRT_1750_DATE_CLAIM_PANORAMA"
]
def yr(d):
 try:return int(d) if len(d)==4 else datetime.date.fromisoformat(d).year
 except (ValueError,TypeError) as exc:raise ValueError(f"Invalid date: {d}") from exc

def main():
 p=argparse.ArgumentParser(description=__doc__)
 p.add_argument("--source",type=Path,required=True)
 args=p.parse_args()
 with args.source.open(encoding="utf-8-sig",newline="") as f:
  reader=csv.DictReader(f)
  if reader.fieldnames!=SOURCE_COLUMNS:raise ValueError("Missing/reordered source columns")
  rows=list(reader)
 if len(rows)!=9 or [r["claim_id"] for r in rows]!=IDS:raise ValueError("Nine unique claims expected")
 r={x["claim_id"]:x for x in rows}
 for x in rows:
  start,end=yr(x["date_start"]),yr(x["date_end"])
  if not (1400<=start<=end<=1900):raise ValueError(f"Impossible publication/history date {x['claim_id']}")
  u=urlparse(x["source_url"])
  if u.scheme!="https" or not u.netloc or not x["specific_page"]:
   raise ValueError(f"Untraceable page/link: {x['claim_id']}")
  if "PRIMARY_MANUSCRIPT_VERIFIED" in x["evidence_level"]:
   raise ValueError("This cycle did not acquire original primary contracts")
 loan=r["PRT_PRE_GOLD_1647_SUGAR_COLLATERAL"]
 customs=r["PRT_1704_1706_CUSTOMS"]
 minted=r["PRT_1743_1744_STATE_GOLD_COINS"]
 processed=r["PRT_1743_1744_REFUND_ESTIMATE"]
 if (loan["amount"],loan["unit"],loan["interest_rate_or_new_rate_pct"],loan["tax_or_institution"])!=("200000","cruzados","6.25","sugar_duty"):
  raise ValueError("1647 sugar credit terms incorrectly retyped")
 if (customs["amount"],customs["unit"],customs["interest_rate_or_new_rate_pct"])!=("480","contos",""):
  raise ValueError("1704-06 individual loan rate NOT independently identified")
 if (minted["amount"],minted["unit"],processed["amount"],processed["unit"])!=("4196","contos","5000","contos"):
  raise ValueError("Sousa 2003 coinage versus Azevedo amortization conflict altered")
 if "NOT" not in minted["accounting_or_date_caveat"] or "cannot subtract" not in processed["accounting_or_date_caveat"]:
  raise ValueError("Do not treat coinage as disposable Treasury revenue or amortization as cash")
 editions=[r[id] for id in IDS[-3:]]
 dates=Counter(t["date_start"] for t in editions)
 if dates!={"1749-03-16":2,"1750-03-16":1}:
  raise ValueError("1749 versus 1750 publication date conflict concealed")
 if len({x["source_url"] for x in editions})!=3:raise ValueError("Expected 3 different publication locations")
 for x in editions:
  if "CONFLICT" not in x["accounting_or_date_caveat"]:
   raise ValueError("Do not quietly select an unverified decree date")
 print(
  f"PASS rows={len(rows)} early_tax_backed_loan_1647=200000_cruzados "
  "customs_borrowing_1704_1706=480_contos_loan_rate_NOT_IDENTIFIED "
  "minted_1743_1744=4196_contos_nonfiscal "
  "debt_amortization_reported=5000_contos_non_cash_reconciled "
  "edict_1749_or_1750=SOURCE_DATE_CONFLICT_OPEN "
  "archival_original_laws=NOT_ACQUIRED "
  "cash_loan_causality=NOT_RUN "
  f"file_sha256={hashlib.sha256(args.source.read_bytes()).hexdigest()}")
if __name__=="__main__":
 try:main()
 except (ValueError,OSError,KeyError) as exc:
  print(f"FAIL {exc}",file=sys.stderr)
  sys.exit(2)
