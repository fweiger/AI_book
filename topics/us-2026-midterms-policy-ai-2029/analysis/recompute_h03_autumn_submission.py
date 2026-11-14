#!/usr/bin/env python3
"""TOPIC-011 H03 - PJM 2026 autumn raw capacity vs demand submissions.
All values are EDC/LSE SUBMISSIONS only, not accepted forecast nor realized MW.

python3 analysis/recompute_h03_autumn_submission.py
python3 analysis/recompute_h03_autumn_submission.py --input 20260929-post-meeting---informational-only-capacity-and-demand-requests.xlsx
The latter directly cross-checks the XLSX source SHA and every source row/cell.
"""
from __future__ import annotations
import argparse, csv, hashlib, io, json, re, zipfile, xml.etree.ElementTree as ET
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
SHA="211c1f69bfbb52e4e6499b5aa2f42004a65c7def4471d9e84a581e77970d7d51"
YEARS=range(2027,2032)
N={"m":"http://schemas.openxmlformats.org/spreadsheetml/2006/main"}
def load(name):
    with (ROOT/"data"/name).open(encoding="utf-8",newline="") as f:return list(csv.DictReader(f))
def parse_xlsx(path):
    data=path.read_bytes()
    digest=hashlib.sha256(data).hexdigest()
    if digest!=SHA:raise ValueError("Wrong XLSX SHA; do not silently replace version "+digest)
    z=zipfile.ZipFile(io.BytesIO(data))
    ss=[]
    if "xl/sharedStrings.xml" in z.namelist():
        for si in ET.fromstring(z.read("xl/sharedStrings.xml")).findall("m:si",N):
            ss.append("".join(q.text or "" for q in si.findall(".//m:t",N)))
    def val(c):
        v=c.find("m:v",N)
        if v is not None:return ss[int(v.text)] if c.attrib.get("t")=="s" else v.text
        inline=c.find("m:is",N)
        return "".join(t.text or "" for t in inline.findall(".//m:t",N)) if inline is not None else ""
    out={}
    for sheet,kind in (("sheet1","capacity"),("sheet2","demand")):
        root=ET.fromstring(z.read("xl/worksheets/"+sheet+".xml"))
        d={}
        for row in root.findall("m:sheetData/m:row",N):
            n=int(row.attrib["r"])
            if not(6<=n<=43):continue
            c={re.match("[A-Z]+",x.attrib["r"]).group():val(x) for x in row.findall("m:c",N)}
            if not re.fullmatch(r"-?\d+(?:\.\d+)?",str(c.get("D","")).strip()):continue
            label=(c.get("A") or "").strip()
            if n in (32,33,34,35):label="DOM-"+(c.get("C") or "").strip()
            if not label:continue
            d[n]={"zone":label,"values":[float(c.get(k) or 0) for k in "DEFGH"]}
        out[kind]=d
    return out
def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--input",type=Path,help="Original official workbook; optional")
    args=ap.parse_args()
    rows=load("h03_pjm_2026_sep_submission_capacity_demand_zone.csv")
    rto=load("h03_pjm_2026_sep_rto_submitted_pipeline.csv")
    dif=load("h03_pjm_2026_sep_source_discrepancy.csv")
    assert len(rows)==145 and len(rto)==5 and len(dif)==5
    assert len({(r["source_excel_row"],r["target_year"]) for r in rows})==145
    assert all(r["source_sha256"]==SHA for r in rows+rto)
    data={}
    for r in rows:
        year=int(r["target_year"])
        role=r["role"]
        assert role in {"RTO_AGGREGATE","PENLC_NONADDITIVE","DOM_SUBZONE","EXPLICIT_NON_DATA_CENTER_ADJUSTMENT","PRIMARY_ZONE"}
        data.setdefault(year,[]).append(r)
    reports=[]
    for year in YEARS:
        cur=data[year]
        assert len(cur)==29
        agg=next(r for r in cur if r["role"]=="RTO_AGGREGATE")
        dom=next(r for r in cur if r["zone"]=="DOM")
        aep=next(r for r in cur if r["zone"]=="AEP")
        top=[r for r in cur if r["role"] in {"PRIMARY_ZONE","EXPLICIT_NON_DATA_CENTER_ADJUSTMENT"}]
        children=[r for r in cur if r["role"]=="DOM_SUBZONE"]
        assert len(children)==4
        line=next(x for x in rto if int(x["target_year"])==year)
        for c in ("capacity","demand"):
            field="submitted_"+c+"_mw"
            total=float(agg[field])
            assert abs(sum(float(r[field]) for r in top)-total)<0.002,("RTO aggregation",year,c)
            assert abs(sum(float(r[field]) for r in children)-float(dom[field]))<0.002,("DOM children",year,c)
            rtot=float(line[c+"_request_mw"])
            assert abs(rtot-total)<0.002
        ratio=100*float(agg["submitted_demand_mw"])/float(agg["submitted_capacity_mw"])
        top2=100*(float(dom["submitted_demand_mw"])+float(aep["submitted_demand_mw"]))/float(agg["submitted_demand_mw"])
        assert abs(ratio-float(line["demand_over_capacity_pct"]))<0.002
        assert abs(top2-float(line["dom_aep_combined_share_pct"]))<0.002
        other=next(x for x in dif if int(x["target_year"])==year)
        assert abs(float(other["exelon_ferc_filing_2026_11_03_mw"])-float(other["pjm_postmeeting_informational_2026_10_12_demand_mw"])-float(other["numerical_difference_mw"]))<0.002
        reports.append({"year":year,"submitted_capacity_mw":float(agg["submitted_capacity_mw"]),"submitted_demand_mw":float(agg["submitted_demand_mw"]),"demand_to_capacity_pct":round(ratio,3),"dom_aep_share_pct":round(top2,3)})
    if args.input is not None:
        src=parse_xlsx(args.input)
        for record in rows:
            row=int(record["source_excel_row"]); year=int(record["target_year"])
            i=year-2027
            for field,stype in (("submitted_capacity_mw","capacity"),("submitted_demand_mw","demand")):
                v=src[stype][row]
                assert v["zone"]==record["zone"],(row,stype,v["zone"],record["zone"])
                assert abs(v["values"][i]-float(record[field]))<0.001,(row,field,year)
        assert set(src["capacity"])==set(src["demand"])
    print(json.dumps({"source_crosschecked":args.input is not None,"source_SHA256":SHA,"source_rows":len(rows),"RTO_submissions":reports,"status":"UNVETTED_SUBMISSIONS_AND_SOURCE_DISCREPANCY_UNRESOLVED;NOT_POLICY_EFFECT"},ensure_ascii=False,indent=2))
if __name__=="__main__":main()
