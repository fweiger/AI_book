#!/usr/bin/env python3
"""CASE-PRT-001: test same-author 1765 regional-table edition lineage and 1766 posting shock.

Numerical source: Manuel Jose Benavente Rodrigues 2011 ISCTE Master
Table 3.31 (PDF p99) and 2019 ISCTE PhD Tables 5.9 and 4.5
(PDF pp152 and 109); AHTC FGER Livro 537 fol.36 and fol.274
are ARCHIVAL LOCATORS only, NOT_ACQUIRED original manuscript pages.

Measures: 1765 revenue tax collection jurisdiction and author's goods
origin attribution (both published 2011 and 2019); 1765/1766 first
Contadoria reconstructed balances and gains/losses account accumulated
debit/credit. They are NOT Treasury cash receipts or newly incurred
war expenditures. 1766 1,564 contos transferred to military expense
from prior 1762-66 treasurer-debtor balances is a separate approximate
published description, no independently audited receipt or payment.
"""

from __future__ import annotations
import argparse,csv,hashlib,sys
from pathlib import Path

REGION_FILE="rodrigues_1765_regional_reclass_2011_2019_persistent_70k_m3.csv"
ACCOUNT_FILE="rodrigues2019_1765_1766_first_contadoria_account_rollover_m3.csv"
DERIVED_FILE="rodrigues_1765_1766_edition_and_war_rollover_summary_m3.csv"
REGIONS={
 "corte_estremadura":(2583307266,810285413),
 "reino_iles":(1149449290,1143901917),
 "rio_oriente_asia":(656340260,924921442),
 "africa_maranhao_bahia":(38095805,1548013849),
}
RAW_ACCOUNT={
 (1765,"balance","debit"):(8176,20),
 (1765,"balance","credit"):(481,6),
 (1766,"balance","debit"):(7147,18),
 (1766,"balance","credit"):(248,6),
 (1765,"gains_loss_cumulative","debit"):(441,32),
 (1765,"gains_loss_cumulative","credit"):(2583,62),
 (1766,"gains_loss_cumulative","debit"):(4080,35),
 (1766,"gains_loss_cumulative","credit"):(3284,73),
}
RESULT_COLUMNS=["metric","value","unit","source_location","status_and_interpretation_warning"]

def read(path):
 with path.open(encoding="utf-8-sig",newline="") as f:return list(csv.DictReader(f))

def main():
 p=argparse.ArgumentParser(description=__doc__)
 p.add_argument("--source-dir",required=True,type=Path)
 p.add_argument("--output",required=True,type=Path)
 x=p.parse_args()
 rows=read(x.source_dir/REGION_FILE)
 if len(rows)!=8:raise ValueError("expected 4 regions in 2 editions")
 copies={}
 for r in rows:
  edition=r["edition"]
  if edition not in ("2011_master","2019_phd"):raise ValueError("Unapproved edition")
  if r["original_ahtc_books_status"]!="NOT_ACQUIRED":raise ValueError("Do not claim original AHTC access")
  pair=int(r["collection_location_reis"]),int(r["goods_origin_reclassified_reis"])
  if pair!=REGIONS.get(r["region"]):raise ValueError("Regional amount differs from official thesis figure")
  if int(r["reported_full_1765_total_reis"])!=4427192621:raise ValueError("Reported total changed")
  if not r["origin_discrepancy_status"].startswith("PUBLISHED_70000"):raise ValueError("Edition drift not flagged")
  if (edition,r["region"]) in copies:raise ValueError("Duplicate edition/region")
  copies[edition,r["region"]]=pair
 if len(copies)!=8:raise ValueError("Missing region edition")
 for edition in ("2011_master","2019_phd"):
  col=sum(copies[edition,name][0] for name in REGIONS)
  ori=sum(copies[edition,name][1] for name in REGIONS)
  if (col,ori,4427192621-ori)!=(4427192621,4427122621,70000):
   raise ValueError(f"Unexpected 2011/2019 70K source residual {edition}")
 for name in REGIONS:
  if copies["2011_master",name]!=copies["2019_phd",name]:
   raise ValueError("The source lineage is not identical at regional row level")

 rec=read(x.source_dir/ACCOUNT_FILE)
 values={}
 if len(rec)!=8:raise ValueError("Expected 8 first-Contadoria book/year accounts")
 for row in rec:
  key=int(row["year"]),row["account_class"],row["balance_side"]
  if key in values:raise ValueError("duplicate row")
  val=(int(row["cumulative_amount_contos_published_approx"]),
       int(row["open_accounts_count"]))
  if key not in RAW_ACCOUNT or val!=RAW_ACCOUNT[key]:
   raise ValueError(f"Published 1765/1766 Quadro 4.5 source changed {key}")
  if row["original_manuscript_status"]!="NOT_ACQUIRED":raise ValueError("Actual book unread")
  if "CUMULATIVE_BALANCES_NOT_SAME_YEAR_CASH_FLOWS"!=row["interpretation_limit"]:
   raise ValueError("Historical cash interpretation guardrail absent")
  values[key]=val
 if len(values)!=len(RAW_ACCOUNT):raise ValueError("Missing balance year/side/source")

 def out(label,val,unit,source,guard):
  return dict(zip(RESULT_COLUMNS,(label,str(val),unit,source,guard)))
 data=[]
 for edition in ("2011_master","2019_phd"):
  data.append(out("regional_total_discrepancy_"+edition,70000,"nominal_reis",
       "2011_Table_3_31|2019_Table_5_9","PERSISTENT_SAME_AUTHOR_PUBLICATION_CLAIM_NOT_INDEPENDENT_MANUSCRIPT"))
 b1765=values[1765,"balance","debit"][0]
 b1766=values[1766,"balance","debit"][0]
 gl1765=values[1765,"gains_loss_cumulative","debit"][0]
 gl1766=values[1766,"gains_loss_cumulative","debit"][0]
 data.extend([
  out("first_contadoria_balance_debit_1765",b1765,"approx_contos","2019_Table_4_5","ACCOUNT_BALANCE_NOT_CASH_NEW_ISSUE"),
  out("first_contadoria_balance_debit_1766",b1766,"approx_contos","2019_Table_4_5","ACCOUNT_BALANCE_NOT_CASH_NEW_ISSUE"),
  out("first_contadoria_balance_debit_change",b1766-b1765,"approx_contos","2019_Table_4_5","RECONSTRUCTED_BOOK_BALANCE_CHANGE_NOT_FUNDS_FLOW"),
  out("first_contadoria_gains_loss_cumulative_debit_1765",gl1765,"approx_contos","2019_Table_4_5","ACCOUNTING_CUMULATIVE_DEBIT_NOT_1765_NEW_CASH"),
  out("first_contadoria_gains_loss_cumulative_debit_1766",gl1766,"approx_contos","2019_Table_4_5","ACCOUNTING_CUMULATIVE_DEBIT_NOT_1766_NEW_CASH"),
  out("first_contadoria_gains_loss_debit_nominal_ratio_1766_vs_1765",f"{gl1766/gl1765:.6f}","ratio","2019_Table_4_5","CUMULATIVE_ACCOUNT_CHARGES_NOT_YEAR_ON_YEAR_WAR_SPEND"),
  out("treasurer_gomes_peixoto_1762_1766_cumulative_balance_transferred",1564,"approx_contos","2019_PhD_printed_p87_PDF_p99_AHTC_FGER_Livro537_folio36",
      "AUTHOR_REPORTS_ONE_TIME_1766_BOOK_TRANSFER_TO_MILITARY_GAINS_LOSS_NOT_PROVEN_1766_NEW_CASH"),
  out("treasurer_transferred_vs_1766_debit_scale_pct",f"{100*1564/gl1766:.6f}","percent","2019_PhD_printed_p87_and_Table4_5",
      "ILLUSTRATIVE_MAGNITUDE_ONLY_NOT_EXACT_SHARE_OF_NEW_CASH_OR_NOT_A_NET_ADJUSTMENT"),
  out("original_ahtc_ms_accessed",0,"manuscripts","AHTC_FGER_Livro537_folio36_folio274",
      "NOT_ACQUIRED_ONLY_PUBLISHED_AUTHOR_TRANSCRIPTION_AND_CATALOGUE"),
 ])
 x.output.parent.mkdir(parents=True,exist_ok=True)
 with x.output.open("w",newline="",encoding="utf-8") as f:
  w=csv.DictWriter(f,fieldnames=RESULT_COLUMNS,lineterminator="\n")
  w.writeheader();w.writerows(data)
 print(f"PASS region_edition_rows={len(rows)} persistent_reclass_residual_each_edition_reis=70000 "
   f"reproduced_1765_1766_account_rows={len(rec)} "
   f"1766_debit_to_1765_debit_ratio={gl1766/gl1765:.6f} "
   "1766_historian_reclassification_approx_contos=1564 "
   "original_ms=NOT_ACQUIRED true_1766_cash_flow=NOT_IDENTIFIED "
   f"derived_rows={len(data)} sha256={hashlib.sha256(x.output.read_bytes()).hexdigest()}")
if __name__=="__main__":
 try:main()
 except (ValueError,KeyError,OSError) as e:
  print("FAIL",e,file=sys.stderr);sys.exit(2)
