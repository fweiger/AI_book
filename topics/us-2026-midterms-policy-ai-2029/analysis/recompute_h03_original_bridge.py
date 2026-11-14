#!/usr/bin/env python3
"""TOPIC-011 H03: audit the PJM 'above embedded' vs 'total' measurement bridge.

V2025 is a fully reproducible within-the-same-official-workbook
Table B-9 (above embedded) vs Table B-9b (total associated).
V2023 and V2024 compare the original PDF Table B-9 against a later
June 2025 PJM LAS retrospective TOTAL series.  Residuals are proxies:
DO NOT label them as independently verified same-vintage embedded MW.

No nonstandard dependencies:
  python3 analysis/recompute_h03_original_bridge.py
  python3 analysis/recompute_h03_original_bridge.py --original-2025-xlsx /path/to/2025-load-report-tables.xlsx
"""
from __future__ import annotations
import argparse,csv,hashlib,json,math,statistics,zipfile,xml.etree.ElementTree as ET
from pathlib import Path
R=Path(__file__).resolve().parents[1]
SOURCE_SHA="a9a797f2d3cf34154db466b74e045d1334dfebede87ec6dc3739805093474ef5"
NS={"m":"http://schemas.openxmlformats.org/spreadsheetml/2006/main",
    "r":"http://schemas.openxmlformats.org/officeDocument/2006/relationships"}
def load(name):
    with (R/"data"/name).open(encoding="utf-8",newline="") as fp:return list(csv.DictReader(fp))
def near(a,b,eps=.00002):
    assert abs(a-b)<eps,(a,b)
def asnum(x):return float(x)
def get_original_tables(path):
    b=path.read_bytes()
    digest=hashlib.sha256(b).hexdigest()
    if digest!=SOURCE_SHA:raise ValueError("Official source XLSX SHA changed: "+digest)
    with zipfile.ZipFile(path) as z:
        book=ET.fromstring(z.read("xl/workbook.xml"))
        rels={r.attrib["Id"]:r.attrib["Target"] for r in ET.fromstring(z.read("xl/_rels/workbook.xml.rels"))}
        strings=[]
        if "xl/sharedStrings.xml" in z.namelist():
            for si in ET.fromstring(z.read("xl/sharedStrings.xml")).findall("m:si",NS):
                strings.append("".join(t.text or "" for t in si.findall(".//m:t",NS)))
        def val(c):
            n=c.find("m:v",NS)
            if n is None:return None
            return strings[int(n.text)] if c.attrib.get("t")=="s" else n.text
        out={}
        for sheet in book.findall("m:sheets/m:sheet",NS):
            name=sheet.attrib["name"]
            if name not in {"Table B9","Table B9b"}:continue
            t=rels[sheet.attrib["{"+NS["r"]+"}id"]].lstrip("/")
            path=t if t.startswith("xl/") else "xl/"+t
            ws=ET.fromstring(z.read(path))
            records={}
            for row in ws.findall("m:sheetData/m:row",NS):
                idx=int(row.attrib["r"])
                if idx not in (7,21,22,31,32,33,34):continue
                records[idx]={''.join(q for q in c.attrib["r"] if q.isalpha()):val(c) for c in row.findall("m:c",NS)}
            first=7;zone_rows=({"AEP":22,"DOM":32,"RTO":34} if name=="Table B9"
                             else {"AEP":21,"DOM":31,"RTO":33})
            years={col:int(records[first][col]) for col in "BCDEFG"}
            results={}
            for zone,index in zone_rows.items():
                assert records[index]["A"]==("PJM RTO" if zone=="RTO" else zone)
                results[zone]={year:float(records[index][col]) for col,year in years.items()}
            out[name]=results
    assert set(out)=={"Table B9","Table B9b"}
    return out
def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--original-2025-xlsx",type=Path)
    args=ap.parse_args()
    bridge=load("h03_pjm_original_above_embedded_vs_total_bridge_2023_2030.csv")
    cohorts=load("h03_pjm_embedded_bridge_vintage_summary.csv")
    score=load("h03_pjm_rto_2025_forecast_ranking_by_publication.csv")
    manifest=load("h03_pjm_original_document_revision_manifest.csv")
    byzone=load("h03_pjm_2025_within_workbook_zone_bridge.csv")
    assert [len(a) for a in (bridge,cohorts,score,manifest,byzone)]==[21,3,4,5,24]
    assert len({(r["vintage"],r["target_year"]) for r in bridge})==21
    assert len({(r["target_year"],r["zone"]) for r in byzone})==24
    assert {r["vintage"] for r in bridge}=={"2023","2024","2025"}
    assert {r["version_id"] for r in manifest}=={"2023","2024","2025","2025JUNE","2026MAY"}
    snapshots={}
    residual_stats={}
    for year in (2023,2024,2025):
        arr=sorted([r for r in bridge if int(r["vintage"])==year],key=lambda r:int(r["target_year"]))
        assert len(arr)=={2023:8,2024:7,2025:6}[year]
        assert int(arr[0]["target_year"])==year
        assert [int(r["target_year"]) for r in arr]==list(range(year,2031))
        residuals=[]
        for r in arr:
            above=asnum(r["above_embedded_rto_mw"]);total=asnum(r["total_large_load_rto_mw"])
            assert total>above>0
            residual=total-above
            near(residual,asnum(r["total_minus_above_mw"]))
            near(100*residual/total,asnum(r["residual_div_total_pct"]),.000001)
            assert ("SAME_OFFICIAL_XLSX" in r["source_comparability"]) == (year==2025)
            residuals.append(residual)
        avg=statistics.mean(residuals)
        cv=100*statistics.pstdev(residuals)/avg
        summary=next(r for r in cohorts if int(r["vintage"])==year)
        assert int(summary["n_years"])==len(arr)
        for field,v in [
            ("first_total_mw",asnum(arr[0]["total_large_load_rto_mw"])),
            ("first_above_embedded_mw",asnum(arr[0]["above_embedded_rto_mw"])),
            ("first_total_minus_above_mw",residuals[0]),
            ("first_residual_share_pct",asnum(arr[0]["residual_div_total_pct"])),
            ("residual_mean_mw",avg),
            ("residual_min_mw",min(residuals)),
            ("residual_max_mw",max(residuals)),
            ("residual_cv_pct",cv)]: near(asnum(summary[field]),v,.00001)
        assert cv<3.0  # near-constant offset, not exact proof of equivalent published cohorts
        snapshots[year]={"first_above_embedded_mw":asnum(arr[0]["above_embedded_rto_mw"]),
                         "first_total_mw":asnum(arr[0]["total_large_load_rto_mw"]),
                         "first_gap_mw":residuals[0],"first_gap_share_pct":round(100*residuals[0]/asnum(arr[0]["total_large_load_rto_mw"]),3)}
        residual_stats[year]={"mean_gap_mw":round(avg,3),"cv_pct":round(cv,3)}
    zone={}
    for target in range(2025,2031):
        records={r["zone"]:r for r in byzone if int(r["target_year"])==target}
        assert set(records)=={"RTO","DOM","AEP","OTHER_RTO"}
        for metric in ("b9_above_embedded_mw","b9b_total_associated_mw","total_minus_above_mw"):
            whole=asnum(records["RTO"][metric])
            parts=sum(asnum(records[z][metric]) for z in ("DOM","AEP","OTHER_RTO"))
            near(whole,parts)
        for z,r in records.items():
            near(asnum(r["b9b_total_associated_mw"])-asnum(r["b9_above_embedded_mw"]),
                 asnum(r["total_minus_above_mw"]))
            assert r["original_xlsx_sha256"]==SOURCE_SHA
            near(100*asnum(r["total_minus_above_mw"])/asnum(records["RTO"]["total_minus_above_mw"]),
                 asnum(r["share_of_rto_residual_pct"]),.000001)
        assert records["RTO"]["layer"]=="AGGREGATE"
        for z in ("DOM","AEP","OTHER_RTO"):assert records[z]["layer"]=="DISJOINT_COMPONENT"
        first=next(r for r in bridge if r["vintage"]=="2025" and int(r["target_year"])==target)
        for metric,field in [("b9_above_embedded_mw","above_embedded_rto_mw"),("b9b_total_associated_mw","total_large_load_rto_mw")]:
            near(asnum(records["RTO"][metric]),asnum(first[field]))
        zone[target]=records
    assert asnum(zone[2025]["RTO"]["total_minus_above_mw"])==4138
    assert asnum(zone[2025]["DOM"]["total_minus_above_mw"])==3286
    assert asnum(zone[2025]["AEP"]["total_minus_above_mw"])==349
    assert asnum(zone[2025]["OTHER_RTO"]["total_minus_above_mw"])==503
    ranking={}
    for r in score:
        label=(r["publication_basis"],r["forecast_vintage"])
        assert label not in ranking
        forecast=asnum(r["forecast_mw"]);actual=asnum(r["common_actual_may2026_mw"])
        near(abs(actual-forecast),asnum(r["abs_error_mw"]))
        near(100*abs(actual-forecast)/actual,asnum(r["APE_abs_error_div_actual_pct"]),.000001)
        near(100*(actual/forecast-1),asnum(r["signed_bias_actual_minus_fc_div_fc_pct"]),.000001)
        ranking[label]=100*abs(actual-forecast)/actual
    assert ranking[("JUNE_2025_TOTAL_TRACKING","2025")]<ranking[("JUNE_2025_TOTAL_TRACKING","2024")]
    assert ranking[("MAY_2026_ACCURACY_RETROSPECT","2025")]>ranking[("MAY_2026_ACCURACY_RETROSPECT","2024")]
    if args.original_2025_xlsx:
        sources=get_original_tables(args.original_2025_xlsx)
        for target,records in zone.items():
            for z in ("RTO","DOM","AEP"):
                near(asnum(records[z]["b9_above_embedded_mw"]),sources["Table B9"][z][target])
                near(asnum(records[z]["b9b_total_associated_mw"]),sources["Table B9b"][z][target])
    out={"original_2025_xlsx_crosschecked":bool(args.original_2025_xlsx),
         "source_SHA256_original2025":SOURCE_SHA,
         "bridge_record_count":len(bridge),"original_2025_same_source_zone_year_cells":len(byzone),
         "vintage_first_year_gap":snapshots,"residual_stability_by_vintage":residual_stats,
         "original2025_RTO_2025_gap_MW":4138,
         "original2025_RTO_2025_gap_from_DOM_MW":3286,
         "original2025_RTO_2025_DOM_share_of_gap_pct":round(100*3286/4138,3),
         "2025_target_RTO_forecast_error_reversal":{
              "June2025_total_v2024_APE_pct":round(ranking[("JUNE_2025_TOTAL_TRACKING","2024")],3),
              "June2025_total_v2025_APE_pct":round(ranking[("JUNE_2025_TOTAL_TRACKING","2025")],3),
              "May2026_retro_v2024_APE_pct":round(ranking[("MAY_2026_ACCURACY_RETROSPECT","2024")],3),
              "May2026_retro_v2025_APE_pct":round(ranking[("MAY_2026_ACCURACY_RETROSPECT","2025")],3)},
         "2023_2024_gap_semantics":"CROSS_PUBLICATION_PROXY_UNCONFIRMED_SAME_DOCUMENT_DECOMPOSITION",
         "historical_2026_actual_vs_2025_forecast_semantics":"JULY_VS_SUMMER_POTENTIAL_DIFFERENCES",
         "political_causality":"UNTESTED"}
    print(json.dumps(out,ensure_ascii=False,indent=2))
if __name__=="__main__":main()
