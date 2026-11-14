#!/usr/bin/env python3
"""CASE-PRT-001 M3: DEBT.PT annual net issuance vs changes in sovereign debt stock.

Downloads of original copyrighted/uncertain-license workbook are user-supplied;
this source reproduces derived ratios only. Inputs: DEBT.PT A official XLSX
Debt stock tab cached columns C,D,E,F,H,I (1641-1800). Monetary unit: reís.
Note: the file's H/I "net" series includes reconstruction/shifted short-term
timing in some seventeenth century years; do NOT assert identity globally.
"""
from __future__ import annotations
import argparse,csv,hashlib,math,re,sys,xml.etree.ElementTree as ET,zipfile
from pathlib import Path
SOURCE_HASH="b2024474a20442b5577ca4667067edf22ffdf71a30faad01971f5a8d13104d17"
TAG="{http://schemas.openxmlformats.org/spreadsheetml/2006/main}"
ANNUAL="debtpt_issuance_vs_stock_delta_1642_1800_m3.csv"
EVENT="debtpt_1740s_net_issuance_comparison_m3.csv"
ANNUAL_HEADERS=[
 "year","total_debt_stock_million_reis","long_term_stock_million_reis",
 "short_term_stock_million_reis","stock_change_million_reis",
 "net_new_juros_million_reis","net_short_issue_million_reis",
 "reported_net_issue_sum_million_reis",
 "stock_change_minus_issues_million_reis",
 "residual_gt_0p01_million_reis",
 "long_term_stock_change_minus_juro_issue_million_reis",
 "source_tab","source_units"
]
EVENT_HEADERS=["period","year_start","year_end","n_years",
 "net_new_juros_sum_million_reis","net_short_issue_sum_million_reis",
 "recorded_net_issue_sum_million_reis","total_stock_change_million_reis",
 "sum_stock_minus_net_issue_million_reis",
 "event_1743_share_of_decade_net_juros_pct","status"]
def parse_workbook(path):
 with zipfile.ZipFile(path) as z:
  root=ET.fromstring(z.read("xl/worksheets/sheet2.xml"))
  rows={}
  for rr in root.findall(".//"+TAG+"sheetData/"+TAG+"row"):
   cells={}
   for c in rr.findall(TAG+"c"):
    m=re.match(r"([A-Z]+)[0-9]+$",c.get("r",""))
    v=c.find(TAG+"v")
    if m and v is not None and v.text is not None:cells[m.group(1)]=v.text
   try:y=int(cells["C"])
   except (KeyError,ValueError):continue
   if 1641<=y<=1800:
    if y in rows:raise ValueError(f"Duplicate year {y}")
    rows[y]={k:float(cells[k])/1e6 for k in ("D","E","F","H","I")}
 if sorted(rows)!=list(range(1641,1801)):
  raise ValueError("Year series has duplicates/missing annual observations")
 for y,r in rows.items():
  if not all(math.isfinite(v) for v in r.values()):raise ValueError(f"Nonfinite value {y}")
  if not math.isclose(r["D"]+r["E"],r["F"],rel_tol=1e-11,abs_tol=1e-8):
   raise ValueError(f"Long+short stock != total at {y}")
 return rows
def write_csv(path,cols,records):
 with path.open("w",encoding="utf-8",newline="") as f:
  w=csv.DictWriter(f,fieldnames=cols,lineterminator="\n")
  w.writeheader();w.writerows(records)
def fixed(x):return f"{x:.6f}"
def main():
 p=argparse.ArgumentParser(description=__doc__)
 p.add_argument("--source",required=True,type=Path)
 p.add_argument("--output-dir",required=True,type=Path)
 arg=p.parse_args()
 sha=hashlib.sha256(arg.source.read_bytes()).hexdigest()
 if sha!=SOURCE_HASH:raise ValueError(f"Unexpected original DEBT.PT XLSX hash {sha}")
 rows=parse_workbook(arg.source)
 annual=[]
 for y in range(1642,1801):
  r,old=rows[y],rows[y-1]
  change=r["F"]-old["F"]
  net=r["H"]+r["I"]
  err=change-net
  longerr=r["D"]-old["D"]-r["H"]
  annual.append(dict(zip(ANNUAL_HEADERS,[
   y,fixed(r["F"]),fixed(r["D"]),fixed(r["E"]),fixed(change),
   fixed(r["H"]),fixed(r["I"]),fixed(net),fixed(err),
   "true" if abs(err)>0.01 else "false",fixed(longerr),
   "DEBT_PT_A_Debt_stock","million_nominal_reis"
  ])))
 bad=[r for r in annual if r["residual_gt_0p01_million_reis"]=="true"]
 if len(bad)!=20:raise ValueError(f"Unexpected number of >0.01 million residual flags: {len(bad)}")
 if any(int(r["year"])>=1740 for r in bad):
  raise ValueError("Unexpected post-1740 net issue vs stock discrepancy")
 if abs(rows[1743]["H"]-507.9430)>0.01:raise ValueError("1743 large net issuance not present")
 events=[]
 for start,end in ((1731,1740),(1741,1750),(1751,1760),(1761,1770)):
  z=[rows[y] for y in range(start,end+1)]
  h=sum(x["H"] for x in z);i=sum(x["I"] for x in z)
  delta=rows[end]["F"]-rows[start-1]["F"]
  resid=delta-h-i
  events.append(dict(zip(EVENT_HEADERS,[
   f"{start}-{end}",start,end,end-start+1,fixed(h),fixed(i),
   fixed(h+i),fixed(delta),fixed(resid),
   fixed(100*rows[1743]["H"]/h) if start==1741 else "",
   "stockflow_reconciles_for_this_decade" if abs(resid)<0.01 else "material_unexplained_residual"
  ])))
 if not math.isclose(float(events[1]["net_new_juros_sum_million_reis"]),950.658676,abs_tol=1e-5):
  raise ValueError("1740s issuance benchmark failed")
 if not math.isclose(float(events[1]["total_stock_change_million_reis"]),943.701989,abs_tol=1e-5):
  raise ValueError("1740s stock delta benchmark failed")
 arg.output_dir.mkdir(parents=True,exist_ok=True)
 for name,headers,records in [(ANNUAL,ANNUAL_HEADERS,annual),(EVENT,EVENT_HEADERS,events)]:
  path=arg.output_dir/name
  write_csv(path,headers,records)
  print(f"{name} rows={len(records)} SHA256={hashlib.sha256(path.read_bytes()).hexdigest()}")
 print(f"PASS yearly_annual_pairs=159 bad_1640s_1660s={len(bad)} late_1740_plus_bad=0 "
       f"year_1743_net_long={rows[1743]['H']:.6f} "
       f"year_1743_share_1741_1750={100*rows[1743]['H']/sum(rows[y]['H'] for y in range(1741,1751)):.4f}%")
if __name__=="__main__":
 try:main()
 except (ValueError,KeyError,OSError,zipfile.BadZipFile) as e:
  print(f"FAIL: {e}",file=sys.stderr)
  raise SystemExit(2)
