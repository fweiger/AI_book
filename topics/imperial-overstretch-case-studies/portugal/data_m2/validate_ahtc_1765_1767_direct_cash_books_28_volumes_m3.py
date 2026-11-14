#!/usr/bin/env python3
"""CASE-PRT-001: official 1977 Crown fiscal archive 28-volume cross-ledger audit.

The official Tribunal de Contas finding aid lists historical volumes, not
digitized ledger transaction content. Verify archival source SHA provenance,
volume identities / time frames, three source-date anomalies and accounting
series boundaries. No 371.4-contos loan cash receipt is claimed as found.

Usage:
 python3 validate_ahtc_1765_1767_direct_cash_books_28_volumes_m3.py \
    --input ahtc_1765_1767_receipts_diaries_master_crossledger_28_volumes_m3.csv \
    [--catalogue Inventario_Adenda_Erario_Regio.pdf]
"""
from __future__ import annotations
import argparse,csv,hashlib,sys
from pathlib import Path
from collections import Counter
from datetime import date

URL="https://erario.tcontas.pt/pt/arquivo_biblioteca/instrumentos_pesquisa/Inventario_Adenda_Erario_Regio.pdf"
PDF_SHA="fd31975695bfbc0c5299e5eed2dda24c6b21c976eadd43528e7ff79baaef6739"
CASH={
 617:("1765-01-01","1765-03-31","NONE"),
 618:("1765-04-01","1765-07-20","NONE"),
 619:("1765-07-22","1765-10-15","CATALOGUE_JULY_21_NOT_COVERED"),
 620:("1765-10-16","1765-12-31","NONE"),
 621:("1766-01-01","1766-04-04","NONE"),
 622:("1766-04-05","1766-06-30","NONE"),
 623:("1766-07-01","1766-09-05","SEPTEMBER_05_ALSO_IN_VOL_624"),
 624:("1766-09-05","1766-12-31","SEPTEMBER_05_ALSO_IN_VOL_623"),
 625:("1767-01-01","1767-03-23","NONE"),
 626:("1767-03-24","","CATALOGUE_IMPOSSIBLE_JUNE_31_END_UNRESOLVED"),
 627:("1767-07-03","1767-09-30","POTENTIAL_JULY_01_02_GAP_AFTER_VOL626"),
 628:("1767-10-01","1767-12-31","NONE")
}
MASTER={537:("1762-01-01","1766-12-31"),538:("1767-01-01","1769-12-31"),
 2699:("1762-01-01","1768-12-31"),3976:("1762-01-01","1772-12-31"),
 4154:("1762-01-01","1773-12-31")}
DIARY={548:("1765-01-01","1766-12-31"),549:("1766-01-01","1767-12-31"),
 2718:("1765-01-01","1766-12-31"),2719:("1766-01-01","1767-12-31"),
 3982:("1765-01-01","1767-12-31"),4160:("1762-01-01","1770-12-31")}
DRAFT={555:("1765-01-01","1765-12-31"),556:("1766-01-01","1766-09-30"),
 557:("1766-09-01","1766-12-31"),4168:("1765-01-01","1766-12-31"),
 4169:("1766-01-01","1769-12-31")}

def main():
 p=argparse.ArgumentParser(description=__doc__)
 p.add_argument("--input",type=Path,required=True)
 p.add_argument("--catalogue",type=Path)
 args=p.parse_args()
 if args.catalogue:
  raw=args.catalogue.read_bytes()
  if hashlib.sha256(raw).hexdigest()!=PDF_SHA:raise ValueError("Unexpected official archival finding aid PDF SHA")
  if not raw.startswith(b"%PDF"):raise ValueError("Official archive source not a PDF")
 with args.input.open(encoding="utf-8-sig",newline="") as f:rows=list(csv.DictReader(f))
 if len(rows)!=28:raise ValueError("Expected exactly 28 candidate volume items")
 ids=[int(r["book_number"]) for r in rows]
 if len(set(ids))!=28:raise ValueError("Duplicate 1977 book/cota number")
 expected=set(CASH)|set(MASTER)|set(DIARY)|set(DRAFT)
 if set(ids)!=expected:raise ValueError(f"Unexpected volume IDs {set(ids)^expected}")
 cats=Counter()
 warnings=[]
 for row in rows:
  n=int(row["book_number"])
  if n in CASH:
   series="central_royal_treasury_received_and_paid_605_781"
   s,e,warning=CASH[n]
  elif n in MASTER:series="four_contadorias_general_ledgers";s,e=MASTER[n];warning="NONE"
  elif n in DIARY:series="four_contadorias_journal_books";s,e=DIARY[n];warning="NONE"
  else:
   series="four_contadorias_draft_journals";s,e=DRAFT[n]
   warning="PARTIAL_MONTH_OVERLAP_WITH_VOL556" if n==557 else "NONE"
  cats[series]+=1
  if row["series"]!=series or (row["start_date_normalized"],row["end_date_normalized"])!=(s,e):
   raise ValueError(f"Archive book {n}: wrong volume/series or date range")
  if row["date_quality"]!=warning:raise ValueError(f"Archive book {n}: unresolved inventory date caveat omitted")
  if row["source_url"]!=URL or row["source_pdf_sha256"]!=PDF_SHA:
   raise ValueError("Archive inventory citation or PDF SHA mismatch")
  if row["handwritten_ledger_status"]!="NOT_ACQUIRED" or row["metadata_status"]!="1977_OFFICIAL_ARCHIVE_INVENTORY_ONLY":
   raise ValueError("Inventory catalogue is NOT original handwritten historical account")
  if row["current_shelfmark_status"]!="VERIFY_POST_2024_ANTT_TRANSFER":
   raise ValueError("1977 book numbers may need 2024 ANTT cota crosswalk")
  if row["priority"] not in ("P0","P1","P2"):raise ValueError("Unrecognized priority")
  if not row["original_period_as_published"] or not row["matching_target"]:
   raise ValueError("Missing original printed scope or reconciliation target")
  date.fromisoformat(s)
  if e:date.fromisoformat(e)
  if warning!="NONE":warnings.append(n)
 assert cats==Counter({"central_royal_treasury_received_and_paid_605_781":12,
  "four_contadorias_general_ledgers":5,
  "four_contadorias_journal_books":6,
  "four_contadorias_draft_journals":5})
 high={int(r["book_number"]) for r in rows if r["priority"]=="P0"}
 if high!={621,622,623,624,537,548,549,3982}:
  raise ValueError("Loan-focused initial P0 request scope changed")
 if set(warnings)!={619,623,624,626,627,557}:
  raise ValueError("Source catalogue overlaps/gaps are not accounted for")
 print(
 f"PASS 1977_archival_book_locations={len(rows)} cash_1765_1767=12 "
 f"cash_1766=4 master=5 journal=6 draft=5 P0={len(high)} "
 f"catalogue_date_flags={len(warnings)} flagged_ids={sorted(warnings)} "
 "invalid_1767_June31=NOT_NORMALIZED 1766_Sep5=OVERLAP "
 "1766_371400000_reis_creditor_loan_crown_cash_ENTRY_NOT_FOUND "
 "handwritten_original_pages=NOT_ACQUIRED causal_inference=NOT_RUN "
 f"csv_sha256={hashlib.sha256(args.input.read_bytes()).hexdigest()}")
if __name__=="__main__":
 try:main()
 except (ValueError,KeyError,OSError,AssertionError) as ex:
  print("FAIL",ex,file=sys.stderr)
  raise SystemExit(2)
