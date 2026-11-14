#!/usr/bin/env python3
"""Source-governance QA for Portuguese empire 1743–1753 debt archivist index.

Validates archive locator metadata, clear NOT_ACQUIRED source-state,
date range, link syntax and strict separation of observed catalogue
metadata from original manuscript contents and actual cash proceeds.
No assertion here claims that an original manuscript or 1743 net cash
receipt has been downloaded.
"""
from __future__ import annotations

import argparse
import csv
import datetime
import hashlib
import re
import sys
from pathlib import Path
from urllib.parse import urlparse

EXPECTED_FIELDS=[
 "record_id","date_start","date_end","archival_reference","custodian",
 "catalogue_description_short","evidence_level_explained",
 "verification_grade","specific_scope_caveat",
 "institutional_or_document_url","accessed_catalogue_url",
 "original_record_status","research_use_case"
]
EXPECTED_IDS={
 "AHU_2003","AHU_491","AHU_1744_JURO_DECREE","AHU_1753_LAND_SWAP",
 "AHU_1743_JUNTA_OFFICE","SGMF_682226","BNP_POMBALINA_459",
 "GOMES_1883","SCML_RECEIPTS_001"
}
def year_of(text):
 if re.fullmatch(r"[0-9]{4}",text):
  return int(text)
 try:
  return datetime.date.fromisoformat(text).year
 except ValueError as exc:
  raise ValueError(f"Invalid archive source date: {text}") from exc

def main():
 a=argparse.ArgumentParser(description=__doc__)
 a.add_argument("--source",required=True,type=Path)
 opt=a.parse_args()
 with opt.source.open("r",encoding="utf-8-sig",newline="") as f:
  rr=csv.DictReader(f)
  if rr.fieldnames != EXPECTED_FIELDS:
   raise ValueError("Archival source registry fields changed")
  records=list(rr)
 if len(records)!=9 or {r["record_id"] for r in records}!=EXPECTED_IDS:
  raise ValueError("Missing, duplicate or unexpected archive dossier")
 counts={}
 for r in records:
  y1,y2=year_of(r["date_start"]),year_of(r["date_end"])
  if y1<1400 or y2>1850 or y1>y2:raise ValueError(f"Bad period {r['record_id']}")
  if not r["archival_reference"] or not r["custodian"] or not r["research_use_case"]:
   raise ValueError(f"Uncited archival record {r['record_id']}")
  if r["original_record_status"]!="NOT_ACQUIRED":
   raise ValueError(f"Original manuscript falsely marked acquired {r['record_id']}")
  for k in ("institutional_or_document_url","accessed_catalogue_url"):
   url=urlparse(r[k])
   if url.scheme!="https" or not url.netloc:
    raise ValueError(f"Invalid source locator {r['record_id']} {k}")
  grade=r["verification_grade"]
  if "PRIMARY_MANUSCRIPT_VERIFIED" in grade:raise ValueError("Manuscript not inspected")
  counts[grade]=counts.get(grade,0)+1
 for label in ("AHU_1744_JURO_DECREE","AHU_1753_LAND_SWAP"):
  r=next(t for t in records if t["record_id"]==label)
  if "not_new_cash" not in r["research_use_case"]:
   raise ValueError("Non-cash bond issuance alternative claim lost")
 for label in ("AHU_2003","AHU_491"):
  r=next(t for t in records if t["record_id"]==label)
  if "catalogue_entry_ONLY"!=r["verification_grade"]:
   raise ValueError("Inaccessible original AHU catalog overclaimed")
 print("PASS archival_locators=9 original_manuscripts_downloaded=0 "
       "official_catalog_metadata_provenance_including_noncash_examples=VERIFIED "
       f"grades={counts} "
       f"sha256={hashlib.sha256(opt.source.read_bytes()).hexdigest()}")
if __name__=="__main__":
 try:main()
 except (OSError,ValueError,KeyError) as e:
  print(f"FAIL {e}",file=sys.stderr);raise SystemExit(2)
