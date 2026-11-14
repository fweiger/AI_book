#!/usr/bin/env python3
"""CASE-PRT-001 M3: reproducible selected DEBT.PT fiscal-coffer debt-service balances.

Source: DEBT.PT B workbook 'FISCAL COFFERS ... 1529-1557 & 1641_1800'
Tab 2, Long-term debt. J,K correspond 1722-1761; M,N to 1762-1800.
K/N are *period net changes in debt-service assignments*, NOT annual
tax receipts, not total fiscal revenues, not year-1743 issues.
J/M are *period net changes in bond count*, may be fractional or negative.
Selection includes MIXED-SOURCE comparison coffers, no total empire ROI.

Original workbook is NOT redistributed. Download from project's official site.
"""
from __future__ import annotations
import argparse,csv,hashlib,math,re,sys,xml.etree.ElementTree as ET,zipfile
from pathlib import Path

EXPECTED_SHA256="48727613d6463b990842b7098a5b5c25aeaf9235ced3bb142634b591af5b6850"
SHEET_XML="xl/worksheets/sheet2.xml"
TAG="{http://schemas.openxmlformats.org/spreadsheetml/2006/main}"
URL="https://debt.pt/pdf/FISCAL%20COFFERS_%20debt%20service%201529-1557%20%26%201641_1800.xlsx"
OUT="debtpt_selected_fiscal_coffers_debt_service_changes_m3.csv"
FIELDS=[
 "source_row","region","fiscal_coffer","empire_source_tag",
 "bond_count_net_change_1722_1761","debt_service_net_change_1722_1761_million_reis",
 "bond_count_net_change_1762_1800","debt_service_net_change_1762_1800_million_reis",
 "source_sheet","source_period_basis","source_url","not_fiscal_tax_revenue"
]
SELECT={
 28:("mixed_lisbon_customs_not_uniquely_empire","Alfândega Grande de Lisboa"),
 31:("domestic_central_finance_comparator","Junta dos Três Estados"),
 32:("explicit_one_percent_gold_tax_mixed_with_warehouse_debt","Intendência das Dívidas dos Armazéns"),
 33:("mixed_asian_trade_administration","Casa da Índia"),
 34:("mixed_coinage_not_only_colonial_gold","Casa da Moeda"),
 37:("overseas_council_multi_tax_source","Conselho Ultramarino"),
 39:("tobacco_monopoly_related_to_empire_not_single_gold_tax","Estanco do Tabaco"),
 40:("mixed_commerce_council_not_single_empire_source","Junta do Comércio"),
}
def csvout(path, rows):
 with path.open("w",encoding="utf-8",newline="") as f:
  w=csv.DictWriter(f,fieldnames=FIELDS,lineterminator="\n");w.writeheader();w.writerows(rows)

def main():
 a=argparse.ArgumentParser(description=__doc__)
 a.add_argument("--source",type=Path,required=True)
 a.add_argument("--output-dir",type=Path,required=True)
 x=a.parse_args()
 h=hashlib.sha256(x.source.read_bytes()).hexdigest()
 if h!=EXPECTED_SHA256:raise ValueError(f"DEBT.PT B source hash mismatch: {h}")
 with zipfile.ZipFile(x.source) as z:
  ss=["".join(n.itertext()) for n in ET.fromstring(z.read("xl/sharedStrings.xml")).findall(TAG+"si")]
  root=ET.fromstring(z.read(SHEET_XML))
  result={}
  for row in root.findall(".//"+TAG+"sheetData/"+TAG+"row"):
   i=int(row.get("r"))
   if i not in SELECT:continue
   cells={}
   for c in row.findall(TAG+"c"):
    match=re.match(r"([A-Z]+)",c.get("r",""))
    if not match:continue
    v=c.find(TAG+"v")
    if v is None or v.text is None:continue
    val=ss[int(v.text)] if c.get("t")=="s" else v.text
    cells[match.group(1)]=val
   for col in ("C","J","K","M","N"):
    if col not in cells:raise ValueError(f"missing source row={i} col={col}")
   tag,required=SELECT[i]
   name=cells["C"]
   if required not in name:raise ValueError(f"coffer row #{i} changed: {name}")
   nums=[float(cells[q]) for q in ("J","K","M","N")]
   if not all(math.isfinite(v) for v in nums):raise ValueError("nonfinite numeric coffer")
   result[i]={
    "source_row":i,"region":cells.get("B",""),"fiscal_coffer":name,
    "empire_source_tag":tag,
    "bond_count_net_change_1722_1761":f"{nums[0]:.6f}",
    "debt_service_net_change_1722_1761_million_reis":f"{nums[1]/1e6:.6f}",
    "bond_count_net_change_1762_1800":f"{nums[2]:.6f}",
    "debt_service_net_change_1762_1800_million_reis":f"{nums[3]/1e6:.6f}",
    "source_sheet":"B_Long-term_debt",
    "source_period_basis":"net_period_balance_NOT_a_single_year",
    "source_url":URL,
    "not_fiscal_tax_revenue":"true"
   }
 if sorted(result)!=sorted(SELECT):raise ValueError("coffer selection not complete")
 gold=result[32]
 assert math.isclose(float(gold["debt_service_net_change_1722_1761_million_reis"]),50.983813,abs_tol=0.000002)
 assert math.isclose(float(gold["bond_count_net_change_1722_1761"]),516,abs_tol=1e-5)
 assert math.isclose(float(result[37]["debt_service_net_change_1722_1761_million_reis"]),41.093489,abs_tol=0.000002)
 x.output_dir.mkdir(parents=True,exist_ok=True)
 dest=x.output_dir/OUT
 csvout(dest,[result[k] for k in sorted(result)])
 print(f"PASS selected_coffers={len(result)} period_1722_1761=NET_CHANGES "
       f"gold-linked-coffer_1722_1761_debt-service-change={float(gold['debt_service_net_change_1722_1761_million_reis']):.6f} "
       f"output_sha256={hashlib.sha256(dest.read_bytes()).hexdigest()}")
if __name__=="__main__":
 try:main()
 except (ValueError,KeyError,OSError,zipfile.BadZipFile) as e:
  print(f"FAIL: {e}",file=sys.stderr);raise SystemExit(2)
