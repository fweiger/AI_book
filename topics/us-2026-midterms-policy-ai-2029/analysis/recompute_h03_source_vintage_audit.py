#!/usr/bin/env python3
"""PJM RTO public-source vintage/definition audit: June 2025 vs May 2026.

This is not proof of a statistical *restatement*: 2025's presentation says
RTO Total Large Load Adjustments while May 2026 gives "Historical July Peak".
Scope and month-of-peak equivalence are unverified, so differences are
public-source discrepancies, NOT new physical load or revision shock.

Run:
 python3 analysis/recompute_h03_source_vintage_audit.py
 python3 analysis/recompute_h03_source_vintage_audit.py \
   --accuracy-xlsx /path/to/2026-accuracy-report.xlsx \
   --original-2025-xlsx /path/to/2025-load-report-tables.xlsx

Standard library only. 2025 PDF values are a documented transcription
from PJM's June 2025 meeting slide 7, not extracted via an OCR model.
"""
from __future__ import annotations
import argparse,csv,hashlib,json,statistics,zipfile,xml.etree.ElementTree as ET
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
SHA_2025="a9a797f2d3cf34154db466b74e045d1334dfebede87ec6dc3739805093474ef5"
SHA_2026="e0f24fe03a79af016826089c653b2c2e15e55edcb04a7bd4be5fa643136425fc"
NS={"x":"http://schemas.openxmlformats.org/spreadsheetml/2006/main",
    "r":"http://schemas.openxmlformats.org/officeDocument/2006/relationships"}

def read(p):
    with (ROOT/"data"/p).open(encoding="utf-8",newline="") as h:
        return list(csv.DictReader(h))

def near(a,b,eps=0.00001):
    assert abs(a-b)<eps,(a,b)

def b9b_rto_original(path:Path):
    data=path.read_bytes()
    sha=hashlib.sha256(data).hexdigest()
    if sha!=SHA_2025:raise ValueError("Original 2025 XLSX SHA mismatch: "+sha)
    with zipfile.ZipFile(path) as z:
        book=ET.fromstring(z.read("xl/workbook.xml"))
        rel=ET.fromstring(z.read("xl/_rels/workbook.xml.rels"))
        paths={r.attrib["Id"]:r.attrib["Target"] for r in rel}
        strings=[]
        if "xl/sharedStrings.xml" in z.namelist():
            for si in ET.fromstring(z.read("xl/sharedStrings.xml")).findall("x:si",NS):
                strings.append("".join(x.text or "" for x in si.findall(".//x:t",NS)))
        def cv(c):
            node=c.find("x:v",NS)
            if node is None:return ""
            return strings[int(node.text)] if c.attrib.get("t")=="s" else node.text
        for sh in book.findall("x:sheets/x:sheet",NS):
            if sh.attrib["name"]!="Table B9b":continue
            t=paths[sh.attrib["{"+NS["r"]+"}id"]].lstrip("/")
            t=t if t.startswith("xl/") else "xl/"+t
            ws=ET.fromstring(z.read(t))
            header=None;rto=None
            for row in ws.findall("x:sheetData/x:row",NS):
                i=int(row.attrib["r"])
                if i not in (7,33):continue
                d={}
                for c in row.findall("x:c",NS):
                    column="".join(q for q in c.attrib["r"] if q.isalpha())
                    d[column]=cv(c)
                if i==7:header=d
                if i==33:rto=d
            assert header is not None and rto is not None
            assert rto["A"]=="PJM RTO"
            return {int(header[k]):float(rto[k]) for k in "BCDEFG"}
    raise RuntimeError("Table B9b or RTO row 33 not found in official 2025 workbook")

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument("--accuracy-xlsx",type=Path)
    parser.add_argument("--original-2025-xlsx",type=Path)
    args=parser.parse_args()
    hist=read("h03_pjm_rto_2014_2024_cross_publication_history.csv")
    fcasts=read("h03_pjm_rto_2023_2030_cross_publication_forecasts.csv")
    sens=read("h03_pjm_rto_2023_2024_error_definition_sensitivity.csv")
    assert (len(hist),len(fcasts),len(sens))==(11,21,3)
    assert [int(x["year"]) for x in hist]==list(range(2014,2025))
    assert len({(r["vintage_label"],r["target_year"]) for r in fcasts})==21
    assert len({(r["target_year"],r["forecast_vintage"]) for r in sens})==3
    assert all(r["historical_series_identity_verified"]=="UNCONFIRMED_IDENTICAL_DEFINITION" for r in hist)
    diffs=[];percent=[]
    for r in hist:
        old=float(r["june2025_report_history_mw_rounded"])
        new=float(r["may2026_accuracy_historical_july_peak_mw"])
        delta=new-old;pc=100*(new/old-1)
        near(delta,float(r["cross_publication_difference_mw"]),.000002)
        near(pc,float(r["cross_publication_difference_pct_of_june"]),.000002)
        assert r["june_publication"]=="2025-06-10"
        assert r["may_publication"]=="2026-05-29"
        diffs.append(delta);percent.append(pc)
    assert all(x>0 for x in diffs)
    oldmap={};newmap={}
    byv={}
    for r in fcasts:
        v=int(r["vintage_label"]);target=int(r["target_year"])
        old=float(r["june2025_presentation_forecast_mw_rounded"])
        new=float(r["may2026_accuracy_same_vintage_forecast_mw"])
        assert 2023<=v<=2025 and v<=target<=2030
        near(new-old,float(r["cross_publication_difference_mw"]),.000002)
        near(100*(new/old-1),float(r["cross_publication_difference_pct_of_june"]),.000002)
        oldmap[v,target]=old;newmap[v,target]=new
        byv.setdefault(v,[]).append(new-old)
        assert r["vintage_original_documentation_status"]==(
            "ORIGINAL_B9B_XLSX_CROSSCHECKED" if v==2025 else "JUNE2025_RECAP_NOT_DIRECT_ORIGINAL_VINTAGE")
    assert [len(byv[v]) for v in (2023,2024,2025)]==[8,7,6]
    assert all(d<0 for d in byv[2023])
    assert all(d>0 for d in byv[2024])
    assert sum(d>0 for d in byv[2025])==3
    oldh={int(r["year"]):float(r["june2025_report_history_mw_rounded"]) for r in hist}
    newh={int(r["year"]):float(r["may2026_accuracy_historical_july_peak_mw"]) for r in hist}
    sensitivity=[]
    for r in sens:
        y=int(r["target_year"]);v=int(r["forecast_vintage"])
        oldb=100*(oldh[y]/oldmap[v,y]-1)
        newb=100*(newh[y]/newmap[v,y]-1)
        near(float(r["june2025_report_forecast_mw"]),oldmap[v,y])
        near(float(r["june2025_report_history_mw"]),oldh[y])
        near(float(r["may2026_accuracy_forecast_mw"]),newmap[v,y],.000002)
        near(float(r["may2026_accuracy_actual_mw"]),newh[y],.000002)
        near(oldb,float(r["june2025_actual_minus_forecast_pct_of_forecast"]),.000002)
        near(newb,float(r["may2026_actual_minus_forecast_pct_of_forecast"]),.000002)
        near(newb-oldb,float(r["difference_in_bias_percentage_points"]),.000002)
        sensitivity.append({"target":y,"vintage":v,"june2025_bias_pct":round(oldb,3),
                            "may2026_bias_pct":round(newb,3),
                            "difference_pp":round(newb-oldb,3)})
    if args.accuracy_xlsx:
        from recompute_h03_pjm_accuracy import source_rows
        source=source_rows(args.accuracy_xlsx)
        rt=source["RTO"]["_index"]
        for r in hist:
            y=r["year"]
            near(float(r["may2026_accuracy_historical_july_peak_mw"]),
                 rt[y,"Historical July Peak"],.000001)
        for r in fcasts:
            y=r["target_year"];v=r["vintage_label"]
            near(float(r["may2026_accuracy_same_vintage_forecast_mw"]),
                 rt[y,f"{v} Load Forecast July Peak"],.000001)
    if args.original_2025_xlsx:
        rto=b9b_rto_original(args.original_2025_xlsx)
        assert list(sorted(rto))==list(range(2025,2031))
        for year,value in rto.items():near(value,oldmap[2025,year])
    out={
        "publication_history_pair_years":len(hist),
        "all_2026_published_history_values_higher":all(d>0 for d in diffs),
        "historical_report_delta_pct_min":round(min(percent),3),
        "historical_report_delta_pct_median":round(statistics.median(percent),3),
        "historical_report_delta_pct_max":round(max(percent),3),
        "history_2024_june2025_mw":oldh[2024],
        "history_2024_may2026_mw":round(newh[2024],3),
        "history_2024_crosspub_difference_mw":round(newh[2024]-oldh[2024],3),
        "same_labeled_forecast_points_across_reports":len(fcasts),
        "forecast_difference_sign_pattern":{str(v):{"points":len(ds),
            "positive":sum(x>0 for x in ds),"negative":sum(x<0 for x in ds)}
            for v,ds in byv.items()},
        "original_2025_RTO_B9b_2025_target_mw":oldmap[2025,2025],
        "may2026_RTO_2025_vintage_target2025_mw":newmap[2025,2025],
        "2023_2024_target_backtest_source_sensitivity":sensitivity,
        "rechecked_original_2025_xlsx":bool(args.original_2025_xlsx),
        "rechecked_2026_accuracy_xlsx":bool(args.accuracy_xlsx),
        "semantic_definition_comparability":"UNCONFIRMED",
        "physical_dc_growth_inferred_from_publication_delta":False,
        "political_causal_status":"UNTESTED"
    }
    print(json.dumps(out,ensure_ascii=False,indent=2))
if __name__=="__main__":main()
