#!/usr/bin/env python3
"""CASE-PRT-001 M3 archival inventory and 1765 fiscal accounting QA.

Inputs: original source-linked *catalogue locator metadata* (NOT a
transcription of actual AHTC manuscript pages) and limited published
numerical claims from Rodrigues (2019 PhD, reconstructed 1765 balances)
and Sousa (2003, ANTT-based gold coin stocks). Check stock/flow/domain
separation, archival time windows, current 2024 AHTC->ANTT access boundary
and approximate (1 conto) financial-statement rounding residual.

Run: python3 validate_ahtc_ledger_requisition_and_1765_cash_specie_scope_m3.py \
    --inventory ahtc_1763_1777_treasury_original_ledger_requisition_inventory_m3.csv \
    --metrics treasury_1765_cash_accounts_vs_gold_coin_stock_provenance_m3.csv
"""
from __future__ import annotations
import argparse,csv,hashlib,sys
from pathlib import Path

VOLUME_YEAR_PAIRS={
 1763:(2,3),1765:(5,6),1766:(7,8),1767:(9,10),1777:(29,30)
}
CASHBOOKS={155:(1762,1763),156:(1763,1764),157:(1765,1765),
           158:(1766,1766),159:(1766,1767),169:(1777,1777)}
OTHER={
 399:("Tesouraria_mor_alcances_rendas_direitos","tax_arrears_and_rights_collection"),
 405:("Tesouraria_mor_royal_orders","royal_treasury_order_decree"),
 406:("Tesouraria_mor_royal_orders","royal_treasury_order_decree"),
 410:("Tesouraria_mor_royal_orders","royal_treasury_order_decree"),
 5351:("Tesouraria_Geral_das_Tropas_credit_debit","military_payroll_prior_arrears")
}
EXPECTED_VALUES={
 "RODRIGUES_1765_TWOCASHACCOUNT_BALANCE":(2765.,"reported_two_caixa_accounts_balance_four_contadorias"),
 "SOUSA_1765_TREASURY_GOLD_COIN":(76.8,"royal_treasury_gold_coin_asset_stock"),
 "RODRIGUES_1765_ACCOUNTING_GAIN":(2690.,"annual_reconstructed_accounting_gain_approx"),
 "RODRIGUES_1762_1764_PRIOR_GAINS":(8244.,"accumulated_prior_period_accounting_gains_approx"),
 "RODRIGUES_1765_TOTAL_DEVE":(17725.,"consolidated_debit_or_assets_approx"),
 "RODRIGUES_1765_TOTAL_HAVER":(6790.,"consolidated_credit_or_liabilities_approx"),
 "SOUSA_1763_TREASURY_GOLD_COIN":(835.,"royal_treasury_gold_coin_asset_stock")
}
def read(path):
 with path.open(encoding="utf-8-sig",newline="") as f:return list(csv.DictReader(f))
def main():
 p=argparse.ArgumentParser(description=__doc__)
 p.add_argument("--inventory",required=True,type=Path)
 p.add_argument("--metrics",required=True,type=Path)
 a=p.parse_args()
 arc=read(a.inventory)
 met=read(a.metrics)
 if len(arc)!=21 or len({(r["series"],r["inventory_volume"]) for r in arc})!=21:
  raise ValueError("Official 1977 inventory must contain 21 unique indexed item rows")
 wanted={n for pair in VOLUME_YEAR_PAIRS.values() for n in pair}|set(CASHBOOKS)|set(OTHER)
 got={int(r["inventory_volume"]) for r in arc}
 if got!=wanted:raise ValueError(f"Inventory volume count/scope not expected: {sorted(got^wanted)}")
 by={int(r["inventory_volume"]):r for r in arc}
 for y,(h1,h2) in VOLUME_YEAR_PAIRS.items():
  for v,first_end in [(h1,("01-01","06-30")),(h2,("07-01","12-31"))]:
   row=by[v]
   if row["series"]!="Tesouraria_mor_receita_despesa" or (
       row["start_date"],row["end_date"])!=(f"{y}-{first_end[0]}",f"{y}-{first_end[1]}"):
    raise ValueError(f"Misidentified half-year volume {v} year {y}")
 for v,(lo,hi) in CASHBOOKS.items():
  r=by[v]
  if (r["series"],r["start_date"],r["end_date"])!=(
      "Tesouraria_mor_Livros_Caixa",str(lo),str(hi)):
   raise ValueError(f"Incorrect Cash book number/range {v}")
 for v,(series,kind) in OTHER.items():
  r=by[v]
  if (r["series"],r["record_category"])!=(series,kind):
   raise ValueError(f"Archive inventory classification error {v}")
 for r in arc:
  if r["verification_status"]!="OFFICIAL_INVENTORY_ONLY_NOT_MANUSCRIPT":
   raise ValueError("Never claim original AHTC manuscript accessed")
  if r["current_cota_status"]!="1977_inventory_number_verify_current_ANNT_cota":
   raise ValueError("AHTC 2024 transfer may change current shelfmark")
  if not r["inventory_pdf_url"].startswith("https://erario.tcontas.pt/"):
   raise ValueError("Missing official primary archive INVENTORY (not original ledger)")
 if len(met)!=7 or {r["metric_id"] for r in met}!=set(EXPECTED_VALUES):
  raise ValueError("Incomplete published source-specific fiscal metrics")
 fiscal={}
 for r in met:
  n,kind=EXPECTED_VALUES[r["metric_id"]]
  if float(r["amount"])!=n or r["accounting_basis"]!=kind:
   raise ValueError("Changed 1765 accounting or 1763 gold published observation")
  if r["original_manuscript_status"].find("NOT_ACQUIRED")<0:
   raise ValueError("Underlying royal Treasury manuscript not obtained")
  if r["monetary_unit"]!="contos" or not r["measurement_guardrail"]:
   raise ValueError("Units or noncomparable-source warning missing")
  fiscal[r["metric_id"]]=n
 gold=next(r for r in met if r["metric_id"]=="SOUSA_1765_TREASURY_GOLD_COIN")
 if gold["asof_date_quality"]!="exact_month_day_NOT_REPORTED":
  raise ValueError("Do not invent day of 1765 gold balance")
 cash=next(r for r in met if r["metric_id"]=="RODRIGUES_1765_TWOCASHACCOUNT_BALANCE")
 if "NOT_EQUATE_WITH_GOLD_COINS" not in cash["measurement_guardrail"]:
  raise ValueError("Full cash accounts not comparable directly to specie holdings")
 # Rounded 2019 scholarly presentation only; NOT exact audited equality:
 # 17,725 - 6,790 - 8,244 = 2,691 vs printed ~2,690.
 approx=fiscal["RODRIGUES_1765_TOTAL_DEVE"]-fiscal["RODRIGUES_1765_TOTAL_HAVER"]-fiscal["RODRIGUES_1762_1764_PRIOR_GAINS"]
 if abs(approx-fiscal["RODRIGUES_1765_ACCOUNTING_GAIN"])!=1:
  raise ValueError("Expected 1-contos rounding mismatch is absent; recheck thesis")
 print(
  f"PASS AHTC_archival_locator_rows={len(arc)} "
  f"receipt_expense_half_year_books={2*len(VOLUME_YEAR_PAIRS)} "
  f"cashbooks={len(CASHBOOKS)} supplementary_books={len(OTHER)} "
  f"Rodrigues_1765_cash_accounts={fiscal['RODRIGUES_1765_TWOCASHACCOUNT_BALANCE']} "
  f"Sousa_1765_gold_coin={fiscal['SOUSA_1765_TREASURY_GOLD_COIN']} "
  "ACCOUNT_AND_ASOF_NOT_COMPARABLE "
  f"accounting_rounded_gain_residual_contos={approx-fiscal['RODRIGUES_1765_ACCOUNTING_GAIN']:.0f} "
  "original_manuscripts=NOT_ACQUIRED transaction_causal_effect=NOT_RUN "
  f"inventory_sha256={hashlib.sha256(a.inventory.read_bytes()).hexdigest()} "
  f"metrics_sha256={hashlib.sha256(a.metrics.read_bytes()).hexdigest()}"
 )
if __name__=="__main__":
 try:main()
 except (ValueError,KeyError,OSError) as exc:
  print("FAIL",exc,file=sys.stderr)
  raise SystemExit(2)
