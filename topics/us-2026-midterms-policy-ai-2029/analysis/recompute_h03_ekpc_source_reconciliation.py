#!/usr/bin/env python3
"""TOPIC-011 H03: exact PJM 2026 B9/B9b RTO offset attribution to EKPC.

Four official releases, four SHA pins. Jan 13-modified B9b is independent,
Feb 6-corrected B9 is independent, combined B9/B9b includes negative EKPC,
and May accuracy reprints the RTO series without EKPC. No pre-Feb B9 bytes
have been found; do NOT estimate the correction itself from mixed-date tables.

python3 analysis/recompute_h03_ekpc_source_reconciliation.py
python3 analysis/recompute_h03_ekpc_source_reconciliation.py \
 --jan-b9b jan.xlsx --feb-b9 feb.xlsx --combined combined.xlsx --accuracy accuracy.xlsx
"""
from __future__ import annotations
import argparse,csv,hashlib,json,re,xml.etree.ElementTree as ET,zipfile
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
SHA={
 "jan_b9b":"ee3b682929db0b59a043c8ab6d1c9776f697ab10fc86fe603a6d0d724893c4ba",
 "feb_b9":"990e2cb82d02a6c689a9e21b5c7ccb13944613f960dcc2f6eb3109e51a49d6a1",
 "combined":"59a62facf819962e430101c96dd1335229d8173fb6886dd8045ced325443f607",
 "accuracy":"e0f24fe03a79af016826089c653b2c2e15e55edcb04a7bd4be5fa643136425fc"
}
YEARS=range(2026,2047)
ZONES={"AE","BGE","DPL","JCPL","METED","PECO","PENLC","PEPCO","PL","PS",
       "RECO","UGI","AEP","APS","ATSI","COMED","DAYTON","DEOK","DLCO","EKPC","OVEC","DOM","RTO"}
N={"m":"http://schemas.openxmlformats.org/spreadsheetml/2006/main",
   "r":"http://schemas.openxmlformats.org/officeDocument/2006/relationships"}
def load(name):
 with (ROOT/"data"/name).open(encoding="utf-8",newline="") as f:return list(csv.DictReader(f))
def almost(a,b,eps=.001):assert abs(float(a)-float(b))<eps,(a,b)
def xlsx(path,kind):
 data=path.read_bytes()
 if hashlib.sha256(data).hexdigest()!=SHA[kind]:
  raise ValueError("Source XLSX SHA changed; archive new version instead of overwriting "+kind)
 with zipfile.ZipFile(path) as z:
  wb=ET.fromstring(z.read("xl/workbook.xml"))
  rel={x.attrib["Id"]:x.attrib["Target"] for x in ET.fromstring(z.read("xl/_rels/workbook.xml.rels"))}
  strings=[]
  if "xl/sharedStrings.xml" in z.namelist():
   for si in ET.fromstring(z.read("xl/sharedStrings.xml")).findall("m:si",N):
    strings.append("".join(q.text or "" for q in si.findall(".//m:t",N)))
  def cv(c):
   v=c.find("m:v",N)
   if v is not None:return strings[int(v.text)] if c.attrib.get("t")=="s" else v.text
   v=c.find("m:is",N)
   return "".join(x.text or "" for x in v.findall(".//m:t",N)) if v is not None else ""
  def sheet_values(name,header,accuracy=False):
   sh=next(s for s in wb.findall("m:sheets/m:sheet",N) if s.attrib["name"]==name)
   t=rel[sh.attrib["{"+N["r"]+"}id"]].lstrip("/")
   part=t if t.startswith("xl/") else "xl/"+t
   xml=ET.fromstring(z.read(part))
   years={};out={};note=""
   for row in xml.findall("m:sheetData/m:row",N):
    num=int(row.attrib["r"]);cells={}
    for c in row.findall("m:c",N):
     mm=re.match(r"[A-Z]+",c.attrib.get("r",""))
     if mm:cells[mm.group()]=cv(c)
    if num==header:
     excluded={"A","B","C"} if header==4 else {"A"}
     years={col:int(value) for col,value in cells.items() if col not in excluded and str(value).isdigit()}
    if accuracy:
     if cells.get("C")=="2026 Load Forecast July Peak" and str(cells.get("B","")).isdigit():
      out.setdefault("RTO",{})[int(cells["B"])]=float(cells["D"])
     continue
    if num==3 and kind=="feb_b9":note=str(cells.get("A") or "")
    if num==6 and kind=="combined" and name=="Table B9":note=str(cells.get("A") or "")
    zone=str(cells.get("A") or "").strip()
    if zone=="PJM RTO":zone="RTO"
    if zone in ZONES and years:
     out[zone]={yr:float(cells[col]) for col,yr in years.items() if cells.get(col) not in (None,"")}
   return out,note
  if kind=="jan_b9b":
   out,_=sheet_values("Total LargeLoad Breakdown",4)
   core=z.read("docProps/core.xml").decode("utf-8")
   assert "2026-01-13T16:17:25Z" in core
   return {"B9b":out}
  if kind=="feb_b9":
   out,note=sheet_values("LargeLoad Above Embed Breakdown",4)
   assert "updated 2/6/2026" in note,note
   core=z.read("docProps/core.xml").decode("utf-8")
   assert "2026-02-06T13:00:15Z" in core
   return {"B9":out}
  if kind=="combined":
   b9,note=sheet_values("Table B9",7)
   b9b,_=sheet_values("Table B9b",7)
   assert "updated 2/6/2026" in note
   return {"B9":b9,"B9b":b9b}
  if kind=="accuracy":
   out,_=sheet_values("RTO",0,True)
   return {"RTO":out["RTO"]}
 raise ValueError(kind)
def main():
 p=argparse.ArgumentParser()
 for flag in ("jan_b9b","feb_b9","combined","accuracy"):
  p.add_argument("--"+flag.replace("_","-"),type=Path,dest=flag)
 args=p.parse_args()
 records=load("h03_pjm_2026_ekpc_source_reconciliation_2026_2046.csv")
 zones=load("h03_pjm_2026_ekpc_zone_source_match_summary.csv")
 sources=load("h03_pjm_2026_jan_feb_publication_manifest.csv")
 sens=load("h03_pjm_2027_rto_baseline_publication_sensitivity.csv")
 assert [len(z) for z in (records,zones,sources,sens)]==[21,23,5,3]
 assert {r["zone"] for r in zones}==ZONES
 assert [int(r["target_year"]) for r in records]==list(YEARS)
 assert len({r["target_year"] for r in records})==21
 assert len({r["comparison_id"] for r in sens})==3
 assert len({r["source_id"] for r in sources})==5
 assert sources[0]["sha256"]==SHA["jan_b9b"]
 assert sources[1]["sha256"]==SHA["feb_b9"]
 assert sources[2]["sha256"]==SHA["combined"]
 assert sources[3]["sha256"]==SHA["accuracy"]
 for z in zones:
  expected=21 if z["zone"] in ("RTO","EKPC") else 0
  assert int(z["years_checked_each_source"])==21
  assert int(z["january_standalone_B9b_vs_combined_different_years"])==expected
  assert int(z["february_standalone_B9_vs_combined_different_years"])==expected
  assert float(z["max_abs_source_offset_mw"])==(10. if expected else 0.)
 for row in records:
  year=int(row["target_year"])
  jan=float(row["january_2026_standalone_B9b_RTO_mw"])
  feb=float(row["february_2026_corrected_standalone_B9_RTO_mw"])
  combined_b9=float(row["current_combined_B9_RTO_mw"])
  combined_b9b=float(row["current_combined_B9b_RTO_mw"])
  acc=float(row["may_2026_accuracy_RTO_forecast_mw"])
  ekpc=float(row["current_combined_EKPC_adjustment_B9b_mw"])
  expected=-10 if year<=2031 else (-9 if year<=2037 else -8)
  assert ekpc==expected
  assert float(row["current_combined_EKPC_adjustment_B9_mw"])==ekpc
  assert float(row["standalone_EKPC_adjustment_mw"])==0.
  for field,value in (("standalone_B9b_minus_combined_B9b_mw",jan-combined_b9b),
                      ("standalone_B9_minus_combined_B9_mw",feb-combined_b9),
                      ("may_accuracy_minus_jan_B9b_mw",acc-jan),
                      ("mixed_Jan_total_minus_Feb_above_mw",jan-feb),
                      ("combined_B9b_minus_B9_mw",combined_b9b-combined_b9)):
   almost(row[field],value)
  almost(jan-combined_b9b,-ekpc)
  almost(feb-combined_b9,-ekpc)
  almost(acc,jan)
  almost(jan-feb,combined_b9b-combined_b9)
  for f,k in (("source_sha_jan","jan_b9b"),("source_sha_feb","feb_b9"),
              ("source_sha_combined","combined"),("source_sha_accuracy","accuracy")):
   assert row[f]==SHA[k]
 lookup={r["comparison_id"]:r for r in sens}
 assert set(lookup)=={"JAN14_STANDALONE_TOTAL_B9b","CURRENT_CORRECTED_COMBINED_B9b","MAY2026_RETROSPECTIVE_JULY_PEAK"}
 for r in sens:
  prior=float(r["prior_forecast_mw"]);later=float(r["new_forecast_mw"])
  almost(later-prior,r["revision_mw"])
  almost(100*(later/prior-1),r["revision_pct_vs_prior"],.0002)
 assert int(float(lookup["JAN14_STANDALONE_TOTAL_B9b"]["revision_mw"]))==-1855
 assert int(float(lookup["CURRENT_CORRECTED_COMBINED_B9b"]["revision_mw"]))==-1865
 assert int(float(lookup["MAY2026_RETROSPECTIVE_JULY_PEAK"]["revision_mw"]))==-1860
 supplied={k:getattr(args,k) for k in ("jan_b9b","feb_b9","combined","accuracy")}
 parsed={k:xlsx(v,k) for k,v in supplied.items() if v is not None}
 if "jan_b9b" in parsed:
  d=parsed["jan_b9b"]["B9b"]
  assert set(d)==ZONES
  for row in records:
   y=int(row["target_year"])
   almost(d["RTO"][y],row["january_2026_standalone_B9b_RTO_mw"])
   almost(d["EKPC"][y],row["standalone_EKPC_adjustment_mw"])
 if "feb_b9" in parsed:
  d=parsed["feb_b9"]["B9"]
  assert set(d)==ZONES
  for row in records:almost(d["RTO"][int(row["target_year"])],row["february_2026_corrected_standalone_B9_RTO_mw"])
 if "combined" in parsed:
  b9=parsed["combined"]["B9"];b9b=parsed["combined"]["B9b"]
  assert set(b9)==set(b9b)==ZONES
  for row in records:
   y=int(row["target_year"])
   almost(b9["RTO"][y],row["current_combined_B9_RTO_mw"])
   almost(b9b["RTO"][y],row["current_combined_B9b_RTO_mw"])
   almost(b9["EKPC"][y],row["current_combined_EKPC_adjustment_B9_mw"])
   almost(b9b["EKPC"][y],row["current_combined_EKPC_adjustment_B9b_mw"])
 if "accuracy" in parsed:
  d=parsed["accuracy"]["RTO"]
  for row in records:almost(d[int(row["target_year"])],row["may_2026_accuracy_RTO_forecast_mw"])
 if "jan_b9b" in parsed and "combined" in parsed:
  one=parsed["jan_b9b"]["B9b"];two=parsed["combined"]["B9b"]
  for z in ZONES:
   for y in YEARS:
    almost(one[z][y]-two[z][y],-two["EKPC"][y] if z in ("RTO","EKPC") else 0)
 if "feb_b9" in parsed and "combined" in parsed:
  one=parsed["feb_b9"]["B9"];two=parsed["combined"]["B9"]
  for z in ZONES:
   for y in YEARS:
    almost(one[z][y]-two[z][y],-two["EKPC"][y] if z in ("RTO","EKPC") else 0)
 print(json.dumps({
  "source_xlsx_crosschecked":sorted(parsed),
  "total_years":len(records),"zones_reconciled":len(zones),
  "Jan14_B9b_RTO_2027":float(records[1]["january_2026_standalone_B9b_RTO_mw"]),
  "Feb06_B9_RTO_2027":float(records[1]["february_2026_corrected_standalone_B9_RTO_mw"]),
  "combined_B9b_RTO_2027":float(records[1]["current_combined_B9b_RTO_mw"]),
  "EKPC_combined_2027_mw":float(records[1]["current_combined_EKPC_adjustment_B9b_mw"]),
  "EKPC_2026_to_2031":-10,"EKPC_2032_to_2037":-9,"EKPC_2038_to_2046":-8,
  "different_zone_names":["EKPC","RTO"],
  "RTO_source_offsets_fully_explained_by_EKPC":True,
  "Jan_B9b_equals_May_accuracy_all_21_years":True,
  "B9b_first_introduced_in_2025_official_report":True,
  "January14_uncorrected_original_B9_obtained":False,
  "Feb6_numerical_correction_effect_quantifiable":False,
  "all_data_is_forecasts_not_realized":True,
  "political_causality":"UNTESTED"
 },ensure_ascii=False,indent=2))
if __name__=="__main__":main()
