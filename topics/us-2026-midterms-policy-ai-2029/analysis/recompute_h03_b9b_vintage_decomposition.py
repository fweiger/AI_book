#!/usr/bin/env python3
"""TOPIC-011 H03: decompose original PJM B9/B9b forecast vintage revisions.

Versions: PJM 2025 original Tables XLSX vs the *currently downloadable* 2026
Tables XLSX, whose B9 sheet explicitly states a 2026-02-06 correction.
Not a Jan14 frozen byte-version, not physical delivered electricity, not DC-only.

    python3 analysis/recompute_h03_b9b_vintage_decomposition.py
    python3 analysis/recompute_h03_b9b_vintage_decomposition.py \
       --source-2025 original2025.xlsx --source-2026 corrected2026.xlsx \
       --accuracy accuracy2026.xlsx

Standard Python library only. All three XLSX SHA256 values are pinned.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
import xml.etree.ElementTree as ET
import zipfile
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
SRC25="a9a797f2d3cf34154db466b74e045d1334dfebede87ec6dc3739805093474ef5"
SRC26="59a62facf819962e430101c96dd1335229d8173fb6886dd8045ced325443f607"
ACC="e0f24fe03a79af016826089c653b2c2e15e55edcb04a7bd4be5fa643136425fc"
SHEETS=("Table B9","Table B9b")
ZONES=("RTO","DOM","AEP","COMED","PS","PL")
PARTS=("DOM","AEP","COMED","PS","PL","OTHER_RTO")
NS={"m":"http://schemas.openxmlformats.org/spreadsheetml/2006/main",
    "r":"http://schemas.openxmlformats.org/officeDocument/2006/relationships"}
def load(name):
    with (ROOT/"data"/name).open(encoding="utf-8",newline="") as h:
        return list(csv.DictReader(h))

def eq(a,b,eps=.0011):
    assert abs(float(a)-float(b))<eps,(a,b)

def xlsx(path,required_sha):
    b=path.read_bytes()
    got=hashlib.sha256(b).hexdigest()
    if got!=required_sha:raise ValueError("Wrong original XLSX SHA: "+got)
    with zipfile.ZipFile(path) as z:
        wb=ET.fromstring(z.read("xl/workbook.xml"))
        rel={n.attrib["Id"]:n.attrib["Target"]
             for n in ET.fromstring(z.read("xl/_rels/workbook.xml.rels"))}
        ss=[]
        if "xl/sharedStrings.xml" in z.namelist():
            for si in ET.fromstring(z.read("xl/sharedStrings.xml")).findall("m:si",NS):
                ss.append("".join(q.text or "" for q in si.findall(".//m:t",NS)))
        def val(c):
            x=c.find("m:v",NS)
            if x is not None:return ss[int(x.text)] if c.attrib.get("t")=="s" else x.text
            x=c.find("m:is",NS)
            return "".join(q.text or "" for q in x.findall(".//m:t",NS)) if x is not None else ""
        items={}
        for s in wb.findall("m:sheets/m:sheet",NS):
            key=s.attrib["name"]
            if key not in SHEETS and not (required_sha==ACC and key in ZONES):continue
            t=rel[s.attrib["{"+NS["r"]+"}id"]].lstrip("/")
            part=t if t.startswith("xl/") else "xl/"+t
            root=ET.fromstring(z.read(part))
            rows=[]
            for row in root.findall("m:sheetData/m:row",NS):
                d={}
                for c in row.findall("m:c",NS):
                    match=re.match("[A-Z]+",c.attrib.get("r",""))
                    if match:d[match.group()]=val(c)
                rows.append((int(row.attrib["r"]),d))
            items[key]=rows
        return items

def source_original(path,sha):
    sheets=xlsx(path,sha)
    assert all(s in sheets for s in SHEETS)
    if sha==SRC26:
        correction=next((d.get("A","") for r,d in sheets["Table B9"] if r==6),"")
        assert "updated 2/6/2026" in correction,correction
    out={}
    for sheet in SHEETS:
        hdr=next(d for r,d in sheets[sheet] if r==7)
        yr={col:int(v) for col,v in hdr.items() if col!="A" and str(v).isdigit()}
        values={}
        for _,d in sheets[sheet]:
            zone=(d.get("A") or "").strip()
            if zone=="PJM RTO":zone="RTO"
            if zone not in ZONES:continue
            values[zone]={y:float(d[col]) for col,y in yr.items()
                          if col in d and d[col] not in ("",None)}
        assert set(values)==set(ZONES)
        out[sheet]=values
    return out

def source_accuracy(path):
    rows=xlsx(path,ACC)
    assert set(ZONES)<=set(rows)
    out={}
    for zone in ZONES:
        points={}
        for _,d in rows[zone]:
            if d.get("C")=="2026 Load Forecast July Peak" and str(d.get("B","")).isdigit():
                points[int(d["B"])]=float(d["D"])
        out[zone]=points
    return out

def main():
    p=argparse.ArgumentParser()
    p.add_argument("--source-2025",type=Path)
    p.add_argument("--source-2026",type=Path)
    p.add_argument("--accuracy",type=Path)
    args=p.parse_args()
    panel=load("h03_pjm_2025_2026_original_b9_b9b_revisions.csv")
    zones=load("h03_pjm_2027_original_zone_revision_contributions.csv")
    retro=load("h03_pjm_2026_original_vs_accuracy_rto.csv")
    assert (len(panel),len(zones),len(retro))==(60,7,10)
    assert len({(r["zone"],r["target_year"]) for r in panel})==60
    assert all(r["v2025_source_sha256"]==SRC25 and r["v2026_corrected_source_sha256"]==SRC26 for r in panel)
    assert all("2026-02-06" in r["source_asof_v2026"] for r in panel)
    index={(r["zone"],int(r["target_year"])):r for r in panel}
    assert {z for z,_ in index}==set(ZONES)
    assert {y for _,y in index}==set(range(2026,2036))
    metrics=("b9_above_embedded_mw","b9b_total_associated_mw","total_minus_above_mw")
    for r in panel:
        v25a=float(r["v2025_b9_above_embedded_mw"])
        v25t=float(r["v2025_b9b_total_associated_mw"])
        v26a=float(r["v2026_b9_above_embedded_mw"])
        v26t=float(r["v2026_b9b_total_associated_mw"])
        v25e=v25t-v25a
        v26e=v26t-v26a
        eq(v25e,r["v2025_total_minus_above_mw"])
        eq(v26e,r["v2026_total_minus_above_mw"])
        eq(v26a-v25a,r["revision_above_embedded_mw"])
        eq(v26e-v25e,r["revision_total_minus_above_mw"])
        eq(v26t-v25t,r["revision_total_associated_mw"])
        eq((v26a-v25a)+(v26e-v25e),v26t-v25t)
        eq(100*(v26t/v25t-1),r["revision_total_associated_pct_of_v2025"],.0011)
        assert r["zone_role"]==("AGGREGATE_RTO" if r["zone"]=="RTO" else "PRIMARY_ZONE")
    assert len({(r["zone"],r["target_year"]) for r in zones})==7
    assert {r["zone"] for r in zones}=={"RTO",*PARTS}
    contrib={}
    for r in zones:
        assert int(r["target_year"])==2027
        z=r["zone"]
        if z!="OTHER_RTO":
            src=index[z,2027]
            eq(r["v2025_total_mw"],src["v2025_b9b_total_associated_mw"])
            eq(r["v2026_total_mw"],src["v2026_b9b_total_associated_mw"])
            eq(r["revision_above_embedded_mw"],src["revision_above_embedded_mw"])
            eq(r["revision_total_minus_above_mw"],src["revision_total_minus_above_mw"])
            eq(r["revision_total_mw"],src["revision_total_associated_mw"])
        else:
            for column,original_column in [
                ("v2025_total_mw","v2025_b9b_total_associated_mw"),
                ("v2026_total_mw","v2026_b9b_total_associated_mw")]:
                parent=float(index["RTO",2027][original_column])
                subtot=sum(float(index[zone,2027][original_column]) for zone in PARTS if zone!="OTHER_RTO")
                eq(r[column],parent-subtot)
        assert r["source_v2025_sha"]==SRC25 and r["source_v2026_sha"]==SRC26
        eq(float(r["revision_total_mw"]),
           float(r["revision_above_embedded_mw"])+float(r["revision_total_minus_above_mw"]))
        eq(float(r["revision_total_minus_above_mw"]),
           float(r["v2026_embedded_related_mw"])-float(r["v2025_embedded_related_mw"]))
        contrib[z]={"total":float(r["revision_total_mw"]),
                    "above":float(r["revision_above_embedded_mw"]),
                    "embedded":float(r["revision_total_minus_above_mw"])}
    for k in ("total","above","embedded"):
        eq(contrib["RTO"][k],sum(contrib[z][k] for z in PARTS))
    assert contrib["RTO"]=={"total":-1865.0,"above":-2883.0,"embedded":1018.0}
    assert contrib["DOM"]=={"total":740.0,"above":392.0,"embedded":348.0}
    assert contrib["AEP"]=={"total":-902.0,"above":-1386.0,"embedded":484.0}
    rt_out={}
    for y in range(2026,2036):
        r=index["RTO",y]
        rt_out[y]={"total":float(r["revision_total_associated_mw"]),
                   "above":float(r["revision_above_embedded_mw"]),
                   "embedded":float(r["revision_total_minus_above_mw"])}
    assert rt_out[2030]=={"total":1755.0,"above":912.0,"embedded":843.0}
    assert rt_out[2035]=={"total":9555.0,"above":8557.0,"embedded":998.0}
    acc={int(r["target_year"]):r for r in retro}
    assert set(acc)==set(range(2026,2036))
    for year,r in acc.items():
        org=float(index["RTO",year]["v2026_b9b_total_associated_mw"])
        new=float(r["may2026_accuracy_report_2026_vintage_RTO_mw"])
        eq(r["current_2026_original_workbook_B9b_RTO_mw"],org)
        eq(r["retrospective_minus_original_mw"],new-org)
        assert r["original_report_source_sha256"]==SRC26 and r["retrospective_source_sha256"]==ACC
        assert int(new-org)==(10 if year<=2031 else 9)
    if args.source_2025:
        d=source_original(args.source_2025,SRC25)
        for zone,year in index:
            row=index[zone,year]
            eq(row["v2025_b9_above_embedded_mw"],d["Table B9"][zone][year])
            eq(row["v2025_b9b_total_associated_mw"],d["Table B9b"][zone][year])
    if args.source_2026:
        d=source_original(args.source_2026,SRC26)
        for zone,year in index:
            row=index[zone,year]
            eq(row["v2026_b9_above_embedded_mw"],d["Table B9"][zone][year])
            eq(row["v2026_b9b_total_associated_mw"],d["Table B9b"][zone][year])
    if args.accuracy:
        d=source_accuracy(args.accuracy)
        for (zone,year),row in index.items():
            assert year in d[zone],(zone,year)
            expected=float(row["v2026_b9b_total_associated_mw"])
            if zone=="RTO":expected+=10 if year<=2031 else 9
            eq(expected,d[zone][year])
    print(json.dumps({
      "source_checked_against_2025_xlsx":bool(args.source_2025),
      "source_checked_against_2026_xlsx":bool(args.source_2026),
      "source_checked_against_2026_accuracy_xlsx":bool(args.accuracy),
      "source2026_B9_contains_Feb6_correction":True,
      "panel_zone_target_rows":len(panel),
      "2027_revision_RTO":contrib["RTO"],
      "2027_zone_contributions":contrib,
      "RTO_revision_2027_to_2035":{str(y):rt_out[y] for y in range(2027,2036)},
      "RTO_2026_edition_vs_2026_accuracy_retrospective_diffs_mw":
        {str(y):float(acc[y]["retrospective_minus_original_mw"]) for y in acc},
      "same_project_approval_or_realization_data":None,
      "not_a_DC_only_measurement":True,
      "new_congress_policy_causality":"UNTESTED"
    },ensure_ascii=False,indent=2))
if __name__=="__main__":main()
