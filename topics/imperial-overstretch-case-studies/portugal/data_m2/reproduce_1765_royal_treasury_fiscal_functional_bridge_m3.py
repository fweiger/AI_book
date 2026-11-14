#!/usr/bin/env python3
"""CASE-PRT-001 M3: 1765 Portuguese Crown Exchequer source-locked published table QA.

Inputs (GitHub source data linked to ISCTE/author theses; not original AHTC
manuscripts): Rodrigues 2019, Tables 5.3, 5.5, 5.7, 5.4, 5.9, 5.11,
and same author's 2011 master's thesis Table 3.33 vs 2019 Table 5.1.
The original 1765 AHTC FGER ledgers 537, 2699, 3976, 4154 NOT_ACQUIRED.

Never reinterpret book-year expense as new calendar-year war cash outlays;
many 1765 war entries reflect the 1762 Seven Years War and 1763 military
audit/vedorias institutional closure. Never conflate Portuguese tax
collection geography with author reclassified tax product origin.

Run:
 python3 reproduce_1765_royal_treasury_fiscal_functional_bridge_m3.py \
  --source-dir /path/to/data_m2 --output /tmp/case-prt-1765-summary.csv
"""
from __future__ import annotations
import argparse,csv,hashlib,sys
from pathlib import Path

CATEGORIES="rodrigues2019_1765_royal_treasury_revenue_expense_war_m3.csv"
REGIONS="rodrigues2019_1765_revenue_collection_vs_origin_region_m3.csv"
EDITIONS="rodrigues_1765_master2011_vs_phd2019_account_edition_audit_m3.csv"
OUT_COLS=["metric","value","unit","source_basis","evidence_status","not_causal_or_cash_warning"]
EXPECTED_TAX={
 "customs_consulates":1161952486,
 "tobacco_contract":893274840,
 "decima":706724386,
 "gold_quintos":462009750,
 "sisas":399995541,
 "mesas_similares":245498722,
 "rio_mint":158400000,
 "brazilwood":100074437,
 "prior_revenues":48919984,
 "other_taxes":250342475
}
EXPECTED_EXP={
 "military":1035933367,
 "royal_household":288337457,
 "foreign_affairs":60592623,
 "wages":46495793,
 "braganca_house":35716840,
 "other":269281557
}
EXPECTED_WAR={
 "vedoria_alentejo":554723270,
 "fortifications":241436971,
 "vedoria_tras_os_montes":61014934,
 "vedoria_estremoz":59000000,
 "army_clothing":25585183,
 "artillery_alentejo":7980485
}
EXPECTED_REGIONS={
 "corte_estremadura":(2583307266,810285413,441232167,487024596),
 "reino_iles":(1149449290,1143901917,1062426942,1070407427),
 "rio_oriente_asia":(656340260,924921442,167837758,167212368),
 "africa_maranhao_bahia":(38095805,1548013849,64860770,11713246)
}
EXPECTED_EDITIONS={
 "gross_debit_balance_total":(17725700642,17725700642),
 "gross_credit_balance_total":(6790262297,6790262297),
 "prior_year_gains":(8244603361,8244603361),
 "current_year_accounting_gain":(2690834984,2690834984),
 "two_caixa_account_balances":(359525124,2765000000)
}

def load(path: Path):
 with path.open(newline="",encoding="utf-8-sig") as f:return list(csv.DictReader(f))
def exact_class(rows,label,expected):
 subset=[r for r in rows if r["source_group"]==label]
 found={r["category_id"]:int(r["nominal_reis"]) for r in subset}
 if len(subset)!=len(expected) or found!=expected:
  raise ValueError(f"Published 1765 source classification mismatch: {label}")
 if label=="war_expense_subcomponents_table_5_5":
  if not all(r["is_nested_component_of_parent"]=="true" for r in subset):
   raise ValueError("War subset must not be added to total military functional spending")
 elif not all(r["is_nested_component_of_parent"]=="false" for r in subset):
  raise ValueError("Unexpected double count flag in base 1765 source category")
 return found

def main():
 p=argparse.ArgumentParser(description=__doc__)
 p.add_argument("--source-dir",required=True,type=Path)
 p.add_argument("--output",required=True,type=Path)
 a=p.parse_args()
 cat=load(a.source_dir/CATEGORIES)
 if len(cat)!=22:raise ValueError("Expected 22 published tax/spend/war component rows")
 rev=exact_class(cat,"revenue_tax_classification_table_5_7",EXPECTED_TAX)
 exp=exact_class(cat,"expense_functional_table_5_3",EXPECTED_EXP)
 war=exact_class(cat,"war_expense_subcomponents_table_5_5",EXPECTED_WAR)
 totalrev=sum(rev.values())
 totalexp=sum(exp.values())
 military=exp["military"]
 war_total=sum(war.values())
 if (totalrev,totalexp,war_total)!=(4427192621,1736357637,949740843):
  raise ValueError("2019 Table5.3/5.5/5.7 sums incorrect")
 income=totalrev-totalexp
 if income!=2690834984 or war_total>military:
  raise ValueError("1765 published accounting profit/war subset arithmetic mismatch")
 reg=load(a.source_dir/REGIONS)
 fields=("recorded_revenue_by_collection_1765_reis",
         "researcher_reclassified_revenue_by_goods_origin_reis",
         "recorded_expense_by_contadoria_1765_reis",
         "researcher_reclassified_expense_by_region_reis")
 vals={}
 for r in reg:
  if r["region"] in vals:raise ValueError("Duplicate region")
  vals[r["region"]]=tuple(int(r[k]) for k in fields)
 if len(reg)!=4 or vals!=EXPECTED_REGIONS:
  raise ValueError("Regional 1765 published data differs from audited Table5.9/5.11")
 region_sums=[sum(t[i] for t in vals.values()) for i in range(4)]
 if region_sums!=[totalrev,totalrev-70000,totalexp,totalexp]:
  raise ValueError("Do not silently repair published 70,000 reis reclassification residual")
 overseas={"rio_oriente_asia","africa_maranhao_bahia"}
 overseas_at_collection=sum(vals[i][0] for i in overseas)
 overseas_at_goods_origin=sum(vals[i][1] for i in overseas)
 editions=load(a.source_dir/EDITIONS)
 cross={r["stat"]:(int(r["2011_value_reis"]),int(r["2019_value_reis_or_approx"]))
        for r in editions}
 if len(editions)!=5 or cross!=EXPECTED_EDITIONS:
  raise ValueError("2011 vs 2019 same-author source version fields changed")
 for name in ("gross_debit_balance_total","gross_credit_balance_total",
              "prior_year_gains","current_year_accounting_gain"):
  if cross[name][0]!=cross[name][1]:
   raise ValueError("Other cross-edition balance components do not match")
 bal_debit=cross["gross_debit_balance_total"][0]
 bal_credit=cross["gross_credit_balance_total"][0]
 past_gain=cross["prior_year_gains"][0]
 if bal_debit-bal_credit-past_gain!=income:
  raise ValueError("1765 income statement does not reconcile with author balance entries")
 if cross["two_caixa_account_balances"][0]==cross["two_caixa_account_balances"][1]:
  raise ValueError("The unexplained Caixa balance version conflict disappeared; investigate")
 if next(r for r in editions if r["stat"]=="two_caixa_account_balances")["cross_version_status"]!="NOT_COMPARABLE_WITHOUT_ACCOUNT_BREAKDOWN":
  raise ValueError("Cash account observation must remain SOURCE_VERSION_CONFLICT_OPEN")

 def emit(metric,value,unit,basis,warning):
  return dict(zip(OUT_COLS,[metric,value,unit,basis,
       "PUBLISHED_AUTHOR_SOURCE_ARITHMETIC_REPRODUCED_OR_EXPLICIT_CONFLICT",
       warning]))
 summary=[
  emit("recorded_revenues_1765",totalrev,"nominal_reis","Rodrigues2019_Table5_7","NOT_full_Kingdom_annual_tax_cash_revenue"),
  emit("recorded_expenses_1765",totalexp,"nominal_reis","Rodrigues2019_Table5_3","1762_war_arrears_partly_booked_1765_NOT_contemporaneous_cash"),
  emit("recorded_accounting_gain_1765",income,"nominal_reis","Tables5_1_5_3_5_7","NOT_cash_budget_surplus"),
  emit("military_recorded_expenses_1765",military,"nominal_reis","Rodrigues2019_Table5_3","NOT_same_calendar_year_actual_war_spend"),
  emit("military_share_recorded_expenses_pct",f"{100*military/totalexp:.6f}","percent","Rodrigues2019_Table5_3","1762_war_carryover_AND_1763_vedorias_closed"),
  emit("war_items_researcher_selected_1765",war_total,"nominal_reis","Rodrigues2019_Table5_5","SUBSET_OF_military_NOT_additive_to_total_expenses"),
  emit("war_items_share_recorded_expenses_pct",f"{100*war_total/totalexp:.6f}","percent","Rodrigues2019_Table5_5","NOT_actual_1765_war_cost_cash"),
  emit("gold_quintos_recorded_revenue_1765",rev["gold_quintos"],"nominal_reis","Rodrigues2019_Table5_7","NOT_gold_output_nor_all_imperial_fiscal_income"),
  emit("gold_quintos_share_revenue_pct",f"{100*rev['gold_quintos']/totalrev:.6f}","percent","Rodrigues2019_Table5_7","Gold_tax_vs_war_items_NOT_funding_trace"),
  emit("overseas_collection_location_reported",overseas_at_collection,"nominal_reis","Rodrigues2019_Table5_9","Not_total_colonial_origins"),
  emit("overseas_collection_location_share_pct",f"{100*overseas_at_collection/totalrev:.6f}","percent","Rodrigues2019_Table5_9","Collection_location_NOT_goods_origin"),
  emit("overseas_goods_origin_reclassified",overseas_at_goods_origin,"nominal_reis","Rodrigues2019_Table5_9_5_11","Researcher_reallocation_NOT_net_colonial_roi"),
  emit("overseas_goods_origin_share_pct",f"{100*overseas_at_goods_origin/totalrev:.6f}","percent","Rodrigues2019_Table5_9_5_11","Author_tax_origin_scope_not_cash_net_fiscal_contribution"),
  emit("published_regional_reclassification_residual",totalrev-region_sums[1],"nominal_reis","Rodrigues2019_Table5_9_5_11","PUBLISHED_70K_source_discrepancy_NOT_AUTO_CORRECTED"),
  emit("2011_master_two_Caixa_exact",cross["two_caixa_account_balances"][0],"nominal_reis","Rodrigues2011_master_p93","not_reconciled_to_2019_author_Caixa_definition"),
  emit("2019_phd_two_Caixa_approx",cross["two_caixa_account_balances"][1],"nominal_reis_approximately","Rodrigues2019_PhD_p130","Approximate_value_NOT_exact_reis_or_same_scope"),
 ]
 a.output.parent.mkdir(parents=True,exist_ok=True)
 with a.output.open("w",newline="",encoding="utf-8") as f:
  writer=csv.DictWriter(f,fieldnames=OUT_COLS,lineterminator="\n")
  writer.writeheader();writer.writerows(summary)
 print(f"PASS revenue={totalrev} expense={totalexp} gain_exact={income} "
  f"military_pct={100*military/totalexp:.6f} war_subset_pct={100*war_total/totalexp:.6f} "
  f"overseas_collection_pct={100*overseas_at_collection/totalrev:.6f} "
  f"overseas_goods_origin_pct={100*overseas_at_goods_origin/totalrev:.6f} "
  "regional_total_printed_residual_reis=70000 "
  "2011_2019_Caixa_conflict=OPEN original_ledger=NOT_ACQUIRED "
  f"output_rows={len(summary)} output_sha256={hashlib.sha256(a.output.read_bytes()).hexdigest()}")

if __name__=="__main__":
 try:main()
 except (ValueError,KeyError,OSError) as exc:
  print(f"FAIL {exc}",file=sys.stderr)
  raise SystemExit(2)
