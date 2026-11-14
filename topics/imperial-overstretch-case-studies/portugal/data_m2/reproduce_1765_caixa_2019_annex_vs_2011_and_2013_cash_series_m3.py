#!/usr/bin/env python3
"""Portuguese imperial fiscal history: cross-author historical Cash-account QA.

PRIMARY RESEARCH DATA IS NOT ACQUIRED. Secondary published author transcriptions:
- Manuel Jose Benavente Rodrigues (2019) PhD, ISCTE, Appendix E PDF pp.275,278,281,283:
  eight signed "Caixa" account balances from 1765 four Contadorias.
- Same author 2011 MA PDF p.101: published signed Caixa net 359,525,124 reis.
- 2019 PhD p.142 narrative "cerca de 2.765 contos" (APPARENTLY DIFFERENT).
- Independent Pablo Oller Mont Serrath (2013), Saeculum 29 pp.80-82:
  nominal fiscal results 1764=-344,042,870 reis and 1765=-554,031,592 reis,
  and no detected entry in his 1766 Treasury cash records for a reportedly
  371.4-contos Crown loan from Junta do Deposito Publico.
- 2011 MA p.70: inter-Contadoria "1%" from Rio de Janeiro gold corresponds
  to 1763 onward but debtor account posting was in 1766.

These are NON-INTERCHANGEABLE measures: 1765 published net ledger signed
balances, 2019 approximate narrative Caixa, 2013 annual fiscal result and
2019 gains/losses (accrual/bookkeeping) are NOT the same fiscal variable.
DO NOT interpret a mismatch as demonstrated government accounting fraud.

Run:
  python3 reproduce_1765_caixa_2019_annex_vs_2011_and_2013_cash_series_m3.py \
    --source-dir . --output /tmp/portugal-1765-comparison.csv \
    [--pdf-2019 path] [--pdf-2011 path] [--pdf-2013 path]
Optional PDFs verify exact published university / journal source SHA256 and
presence of specific evidence strings (requires pdftotext installed).
"""
from __future__ import annotations

import argparse
import csv
import hashlib
from pathlib import Path
import shutil
import subprocess
import sys

F_CAIXA="rodrigues2019_1765_annex_e_eight_caixa_balances_m3.csv"
F_CROSS="independent_1763_1766_fiscal_timing_and_2013_cash_vs_2019_accrual_sources_m3.csv"
OUT_FIELDS=["metric","value","unit","source_or_operation","interpretation_boundary"]
EXPECTED_CAIXA={
 ("corte_estremadura","537","227","current_cash","debit"):(3222113096,275),
 ("corte_estremadura","537","180","prior_revenues_cash","credit"):(228501244,275),
 ("reino_iles","2699","138","prior_revenues_cash","debit"):(56518629,278),
 ("reino_iles","2699","154","current_cash","debit"):(247866105,278),
 ("rio_oriente_asia","3976","107","prior_revenues_cash","debit"):(334049053,281),
 ("rio_oriente_asia","3976","129","current_cash","credit"):(1108742728,281),
 ("africa_maranhao_bahia","4154","12","prior_revenues_cash","debit"):(14596096,283),
 ("africa_maranhao_bahia","4154","80","current_cash","credit"):(2178373883,283)
}
PUBLISHED_SOURCE_SHA={
 "2019":"ca8b83728950b1746440baad2ac522b9dd5010f4237ebb5a8a6e3b6c528b565e",
 "2011":"533d24ceb52b53a4e8994f1a72739b04feb36f162304a3f28c13173f6bd7b3e5",
 "2013":"355dafce8bed43b4fb6e7bace8fb92aab8b2e3fef74d479aae7b06b44a03fa8f"
}
EXPECTED_CROSS={
 "2011_gold_tax_1pct_rio_account_lag":("", "1763+","1766"),
 "2013_nominal_fiscal_result_1764":("-344042870","1764","1764"),
 "2013_nominal_fiscal_result_1765":("-554031592","1765","1765"),
 "2019_1765_gains_and_losses_result":("2690834984","1765","1765"),
 "2013_missing_1766_deposit_loan_cash_entry":("371400000","1766","1766"),
 "2013_1762_1776_colonial_revenue_share":("57.5","1762","1776"),
 "2013_1762_1776_overseas_spending_share":("4","1762","1776")
}

def read(path):
 with path.open(encoding="utf-8-sig",newline="") as f:return list(csv.DictReader(f))

def verify_pdf(path,edition):
 b=path.read_bytes()
 digest=hashlib.sha256(b).hexdigest()
 if digest!=PUBLISHED_SOURCE_SHA[edition]:
  raise ValueError(f"{edition} source PDF hash changed or unexpected: {digest}")
 exe=shutil.which("pdftotext")
 if not exe:raise ValueError("pdftotext required for optional original author PDF cross-check")
 t=subprocess.run([exe,"-layout",str(path),"-"],capture_output=True,text=True,timeout=65)
 if t.returncode!=0:raise ValueError("Cannot read published PDF text")
 check={
  "2019":["3.222.113.096","1.108.742.728","2.178.373.883","2.765 contos"],
  "2011":["359 milhões 525 mil 124","1% pago sobre o ouro","810.285.413"],
  "2013":["554.031.592","371,4 milhões","Não encontrei"]
 }[edition]
 for term in check:
  if term not in t.stdout:raise ValueError(f"{edition} PDF expected source phrase missing: {term}")
 return len(b)

def main():
 p=argparse.ArgumentParser(description=__doc__)
 p.add_argument("--source-dir",type=Path,required=True)
 p.add_argument("--output",type=Path,required=True)
 p.add_argument("--pdf-2019",type=Path)
 p.add_argument("--pdf-2011",type=Path)
 p.add_argument("--pdf-2013",type=Path)
 a=p.parse_args()
 for edition in ("2019","2011","2013"):
  pdf=getattr(a,f"pdf_{edition}")
  if pdf:print(f"PDF_HASH_AND_TEXT_{edition}_PASS bytes={verify_pdf(pdf,edition)}")
 rows=read(a.source_dir/F_CAIXA)
 if len(rows)!=8:raise ValueError("expected eight 1765 Caixa items")
 observed={}
 debit=credit=0
 current_net=prior_net=0
 for row in rows:
  key=(row["region"],row["ahtc_fger_livro_mestre"],row["folio"],
       row["account_class"],row["published_balance_side"])
  value=int(row["balance_amount_reis"])
  page=int(row["published_pdf_page"])
  if key in observed or EXPECTED_CAIXA.get(key)!=(value,page):
   raise ValueError(f"Published Appendix E Caixa entry source mismatch: {key}")
  if row["original_archive_ms_state"]!="NOT_ACQUIRED" or row["financial_reporting_date"]!="1765-12-31":
   raise ValueError("Original 1765 AHTC manuscript access/date is overstated")
  if row["source_pdf_sha256"]!=PUBLISHED_SOURCE_SHA["2019"]:
   raise ValueError("Unversioned original author PDF")
  observed[key]=value
  sign=+1 if row["published_balance_side"]=="debit" else -1
  debit+=value if sign>0 else 0
  credit+=value if sign<0 else 0
  if row["account_class"]=="current_cash":current_net+=sign*value
  elif row["account_class"]=="prior_revenues_cash":prior_net+=sign*value
  else:raise ValueError("Unexpected Caixa account classification")
 if set(observed)!=set(EXPECTED_CAIXA):raise ValueError("missing regional balances")
 net=debit-credit
 if (debit,credit,net,current_net,prior_net)!=(3875142979,3515617855,359525124,182862590,176662534):
  raise ValueError("Could not reconcile signed Appendix E Caixa accounts to 2011 MA")
 refs=read(a.source_dir/F_CROSS)
 if len(refs)!=len(EXPECTED_CROSS):raise ValueError("missing independent source audit rows")
 for ref in refs:
  id=ref["record_id"]
  if id not in EXPECTED_CROSS:raise ValueError("Unexpected historical source claim")
  observed=(ref["reported_numeric_value"],ref["historical_start_year"],ref["accounting_or_publication_year"])
  if observed!=EXPECTED_CROSS[id]:
   raise ValueError(f"2011/2013/2019 reported source amount changed: {id}")
  if not ref["interpretation_warning"] or not ref["evidence_level"]:
   raise ValueError("Missing source-level warning or data provenance")
 if len({ref["record_id"] for ref in refs})!=len(refs):raise ValueError("Duplicate source audit")
 source={ref["record_id"]:ref for ref in refs}
 if source["2013_missing_1766_deposit_loan_cash_entry"]["account_or_measure"]!="reported_1766_sovereign_deposit_loan_not_found_in_author_accounts":
  raise ValueError("Unidentified deposit loan must not be claimed verified")
 if "DEBIT" not in source["2011_gold_tax_1pct_rio_account_lag"]["account_or_measure"].upper():
  raise ValueError("Gold tax posting is an inter-Contadoria debit not a proven gold tax cash payment")
 
 def m(k,v,u,s,c):return dict(zip(OUT_FIELDS,[k,str(v),u,s,c]))
 previous_thesis=359525124
 narrative_about=2765000000 # APPROXIMATE 2019 PUBLISHED PROSE; not exact output of the historical ledgers
 cash_result1765=int(source["2013_nominal_fiscal_result_1765"]["reported_numeric_value"])
 accrual_result1765=int(source["2019_1765_gains_and_losses_result"]["reported_numeric_value"])
 o=[
  m("2019_appendix_e_1765_caixa_debit_total",debit,"reis","Rodrigues2019_AppendixE_4_Contadorias","BOOK_SIDE_NOT_PHYSICAL_CASH_HOLDINGS"),
  m("2019_appendix_e_1765_caixa_credit_total",credit,"reis","Rodrigues2019_AppendixE_4_Contadorias","CREDIT_SIDE_NOT_NEGATIVE_GOLD_TAX_REVENUE"),
  m("2019_appendix_e_1765_caixa_signed_net",net,"reis","debit_total_minus_credit_total","SIGNED_NET_ACROSS_8_PUBLISHED_BALANCE_ACCOUNTS_NOT_EXTERNAL_CASH_AUDIT"),
  m("2019_appendix_e_1765_current_caixa_signed_net",current_net,"reis","current_cash_debit_minus_credit","NOT_YEARLY_NEW_GOLD_OR_FISCAL_RECEIPTS"),
  m("2019_appendix_e_1765_previous_revenue_caixa_signed_net",prior_net,"reis","prior_revenues_cash_debit_minus_credit","PRIOR_REVENUES_LIABILITY_CLEARING_NOT_SAME_YEAR_TAX"),
  m("2011_master_exact_two_caixa_net_narrative",previous_thesis,"reis","Rodrigues2011_master_p93","SAME_RESEARCHER_AUTHOR_NOT_INDEPENDENT_SAMPLE"),
  m("2011_vs_2019_appendix_signed_net_residual",net-previous_thesis,"reis","2019_appendix_minus_2011_narrative","EXACT_ZERO_BUT_SOURCE_AUTHOR_RECONSTRUCTION_NOT_ORIGINAL_MANUSCRIPT"),
  m("2019_phd_1765_two_caixa_narrative_approx",narrative_about,"approx_reis","Rodrigues2019_phd_p130","DIFFERENT_OR_UNKNOWN_SCOPE_PREVENTS_CLAIM_OF_TYPO"),
  m("2019_phd_approx_narrative_minus_appendix_net",narrative_about-net,"approx_reis","2019_narrative_about2765_contos_minus_2019_annex_signed_net","NOT_SAME_VERIFIED_ACCOUNTING_DEFINITION"),
  m("2013_mont_serrath_1764_nominal_fiscal_result",source["2013_nominal_fiscal_result_1764"]["reported_numeric_value"],"reis","2013_saeculum_article_p81","INDEPENDENT_RECONSTRUCTED_YEAR_NET_NOT_2019_YEAR_GAIN"),
  m("2013_mont_serrath_1765_nominal_fiscal_result",cash_result1765,"reis","2013_saeculum_article_p81","UNDERLYING_YEAR_CASH_OR_BALANCE_SCOPE_NOT_IDENTIFIED_RELATIVE_TO_2019"),
  m("2019_rodrigues_1765_gains_loss_result",accrual_result1765,"reis","2019_PhD_Table5_1","AUTHOR_RECONSTRUCTED_GAINS_LOSSES_NOT_TREASURY_CASH_SURPLUS"),
  m("2019_gain_minus_2013_nominal_cash_result",accrual_result1765-cash_result1765,"reis","cross_author_same_year_unmatched_metric_subtraction","DESCRIPTIVE_MEASUREMENT_DISCREPANCY_NOT_AMOUNT_OF_MISSING_GOLD_OR_EMBEZZLEMENT"),
  m("1766_deposit_loan_cited_by_2013_not_located_in_cash_ledger",371400000,"reis","Sousa2003_cited_in_MontSerrath2013_p81","AUTHOR_CANNOT_FIND_LEDGER_ENTRY_NOT_PROOF_LOAN_DID_NOT_EXIST"),
  m("2011_gold_one_pct_corresponding_year_from",1763,"calendar_year","Rodrigues2011_p70_intercontadoria","AMOUNT_NOT_IDENTIFIED_DOES_NOT_IMPLY_YEAR_OF_GOLD_MINT_OR_RECEIPT"),
  m("2011_gold_one_pct_account_posting_year",1766,"calendar_year","Rodrigues2011_p70_intercontadoria","HISTORICAL_INTERCONTADORIA_DEBIT_NOT_DIRECT_TREASURY_RECEIPT"),
  m("1762_1776_colonial_tax_origin_revenue_share_reported",57.5,"percent","2013_article_reuses_Tomaz_1988","NOT_NET_IMPERIAL_FINANCIAL_RETURN_NOT_2019_SINGLE_YEAR_PERCENT"),
  m("1762_1776_overseas_booked_spending_share_reported",4,"percent","2013_article_reuses_Tomaz_1988","NOT_REAL_TOTAL_OVERSEAS_CONTROL_COST"),
 ]
 a.output.parent.mkdir(parents=True,exist_ok=True)
 with a.output.open("w",encoding="utf-8",newline="") as f:
  writer=csv.DictWriter(f,fieldnames=OUT_FIELDS,lineterminator="\n")
  writer.writeheader();writer.writerows(o)
 print(f"PASS 2019_AppendixE_eight_cash_entries={len(rows)} debit={debit} credit={credit} "
       f"original_2011_Caixa_reis={previous_thesis} Annex_net={net} "
       f"current_net={current_net} prior_net={prior_net} "
       f"2019_narrative_approx_conflict_reis={narrative_about-net} "
       f"2013_vs_2019_fiscal_metric_gap_reis={accrual_result1765-cash_result1765} "
       "2011_gold_1pct_1763_to_1766_posting_qualitative_only "
       "2013_1766_deposit_loan_NOT_LOCATED "
       "primary_AHTC_manuscripts_NOT_ACQUIRED causal_model_NOT_RUN "
       f"derived_rows={len(o)} sha256={hashlib.sha256(a.output.read_bytes()).hexdigest()}")

if __name__=="__main__":
 try:main()
 except (ValueError,KeyError,OSError,subprocess.TimeoutExpired) as e:
  print("FAIL",e,file=sys.stderr);sys.exit(2)
