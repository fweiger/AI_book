#!/usr/bin/env python3
"""TOPIC-011 H03: verify source XLSX (optional) and recalculate published snapshots.
No external dependencies. The official XLSX is NOT committed; download separately
from the source URL recorded in data/h03_pjm_2025_zone_observed_vs_forecast.csv.

Usage:
  python3 analysis/recompute_h03_pjm_accuracy.py
  python3 analysis/recompute_h03_pjm_accuracy.py --input /path/to/2026-accuracy-report.xlsx
"""
from __future__ import annotations
import argparse, csv, hashlib, io, json, re, zipfile
import xml.etree.ElementTree as ET
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SHA = "e0f24fe03a79af016826089c653b2c2e15e55edcb04a7bd4be5fa643136425fc"
NS = {"m":"http://schemas.openxmlformats.org/spreadsheetml/2006/main",
      "r":"http://schemas.openxmlformats.org/officeDocument/2006/relationships"}
FOUR = ("DOM", "AEP", "COMED", "PS")

def load_csv(filename: str) -> list[dict[str,str]]:
    with (ROOT / "data" / filename).open(newline="", encoding="utf-8") as fh:
        return list(csv.DictReader(fh))

def asnum(v: str | None) -> float | None:
    return None if v in ("", None) else float(v)

def source_rows(path: Path) -> dict[str,dict[str,float|None]]:
    data = path.read_bytes()
    digest = hashlib.sha256(data).hexdigest()
    if digest != SHA:
        raise ValueError("Source XLSX changed SHA: archive original and create a new snapshot, do not overwrite this one")
    with zipfile.ZipFile(io.BytesIO(data)) as z:
        wb = ET.fromstring(z.read("xl/workbook.xml"))
        rel_root = ET.fromstring(z.read("xl/_rels/workbook.xml.rels"))
        rels = {x.attrib["Id"]: x.attrib["Target"] for x in rel_root}
        strings = []
        if "xl/sharedStrings.xml" in z.namelist():
            for si in ET.fromstring(z.read("xl/sharedStrings.xml")).findall("m:si", NS):
                strings.append("".join(t.text or "" for t in si.findall(".//m:t", NS)))
        def text(c):
            v = c.find("m:v",NS)
            if v is not None:
                return strings[int(v.text)] if c.attrib.get("t") == "s" else v.text
            inline = c.find("m:is",NS)
            return "".join(t.text or "" for t in inline.findall(".//m:t", NS)) if inline is not None else None
        out = {}
        for sh in wb.findall("m:sheets/m:sheet", NS):
            name = sh.attrib["name"]
            rel = rels[sh.attrib["{" + NS["r"] + "}id"]].lstrip("/")
            part = rel if rel.startswith("xl/") else "xl/" + rel
            xml = ET.fromstring(z.read(part))
            index = {}
            for row in xml.findall("m:sheetData/m:row", NS):
                cells = {}
                for c in row.findall("m:c",NS):
                    match = re.match(r"[A-Z]+", c.attrib.get("r",""))
                    if match: cells[match.group()] = text(c)
                if all(k in cells for k in "ABCD") and cells["B"] != "Year":
                    index[(str(cells["B"]),str(cells["C"]))] = float(cells["D"])
            out[name] = {
                "forecast_2024_vintage_for_2025_mw": index.get(("2025","2024 Load Forecast July Peak")),
                "forecast_2025_vintage_for_2025_mw": index.get(("2025","2025 Load Forecast July Peak")),
                "historical_2024_july_peak_mw": index.get(("2024","Historical July Peak")),
                "historical_2025_july_peak_mw": index.get(("2025","Historical July Peak")),
                "_index": index
            }
    return out

def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--input",type=Path,help="Original 2026-accuracy-report.xlsx; optional for offline CSV-only recomputation")
    args = ap.parse_args()
    zones = load_csv("h03_pjm_2025_zone_observed_vs_forecast.csv")
    revisions = load_csv("h03_pjm_2025_to_2026_vintage_revisions.csv")
    history = load_csv("h03_pjm_historical_july_2019_2025.csv")
    assert len(zones) == 23
    assert len({z["zone"] for z in zones}) == 23
    assert len(revisions) == 16 and len(history) == 35
    by = {r["zone"]:r for r in zones}
    assert all(r["source_sha256"] == SHA for r in zones + revisions + history)
    # Subzones and aggregate RTO are NON-ADDITIVE. Four primary zones report both actual and 2025 forecast.
    major = [r for r in zones if r["zone_level"] == "PRIMARY_ZONE"]
    matched = [r for r in major if r["coverage"] == "MATCHED"]
    assert {r["zone"] for r in matched} == set(FOUR)
    forecast = sum(float(r["forecast_2025_vintage_for_2025_mw"]) for r in matched)
    actual = sum(float(r["historical_2025_july_peak_mw"]) for r in matched)
    prior = sum(float(r["historical_2024_july_peak_mw"]) for r in matched)
    rto = by["RTO"]
    assert abs(forecast - 7566.0) < 0.001
    assert abs(actual - float(rto["historical_2025_july_peak_mw"])) < 0.002
    assert abs(prior - float(rto["historical_2024_july_peak_mw"])) < 0.002
    totalfc = float(rto["forecast_2025_vintage_for_2025_mw"])
    unmatched = [r for r in major if r["coverage"] == "FORECAST_ONLY"]
    assert {r["zone"] for r in unmatched} == {"APS","ATSI","BGE","PL"}
    unmatched_fc = sum(float(r["forecast_2025_vintage_for_2025_mw"]) for r in unmatched)
    assert abs((forecast + unmatched_fc) - totalfc) < 0.001
    assert abs(unmatched_fc - 169.0) < 0.001
    rev_by={(r["zone"],int(r["target_year"])):r for r in revisions}
    for r in revisions:
        f25=float(r["forecast_2025_vintage_mw"]);f26=float(r["forecast_2026_vintage_mw"])
        assert abs((f26-f25)-float(r["revision_mw"]))<0.002
        assert abs((100*(f26/f25-1))-float(r["revision_pct"]))<0.002
    def rv(zone,year):return float(rev_by[zone,year]["revision_mw"])
    assert rv("RTO",2027)==-1860.0
    assert rv("DOM",2027)==740.0
    assert rv("RTO",2035)==9801.0
    if args.input is not None:
        source=source_rows(args.input)
        assert set(source)==set(by)
        for zone,row in by.items():
            src=source[zone]
            for col in ("forecast_2024_vintage_for_2025_mw","forecast_2025_vintage_for_2025_mw",
                        "historical_2024_july_peak_mw","historical_2025_july_peak_mw"):
                v=asnum(row[col]); expected=src[col]
                assert (v is None)==(expected is None),(zone,col,v,expected)
                if v is not None: assert abs(v-expected)<0.0006,(zone,col,v,expected)
        for item in revisions:
            idx=source[item["zone"]]["_index"];year=str(item["target_year"])
            for col,m in (("forecast_2025_vintage_mw","2025 Load Forecast July Peak"),("forecast_2026_vintage_mw","2026 Load Forecast July Peak")):
                assert abs(float(item[col])-idx[year,m])<0.0006,(item["zone"],year,col)
    dom = by["DOM"]
    outcome={
        "source_crosschecked": args.input is not None,
        "official_zone_sheets":len(by),
        "primary_zones_with_both_actual_and_forecast":4,
        "2025_forecast_volume_matched_share_pct":round(forecast/totalfc*100,3),
        "primary_zones_forecast_only_no_reported_actual":[r["zone"] for r in unmatched],
        "published_rto_reported_actual_mw":round(float(rto["historical_2025_july_peak_mw"]),3),
        "published_rto_all_zone_forecast_mw":round(totalfc,3),
        "published_rto_apparent_error_pct":round((actual/totalfc-1)*100,3),
        "matched_zone_forecast_mw":round(forecast,3),
        "matched_zone_actual_mw":round(actual,3),
        "matched_zone_actual_minus_forecast_mw":round(actual-forecast,3),
        "matched_zone_error_pct":round((actual/forecast-1)*100,3),
        "matched_zone_actual_growth_2025_over_2024_pct":round((actual/prior-1)*100,3),
        "DOM_actual_2025_mw":float(dom["historical_2025_july_peak_mw"]),
        "DOM_2025vintage_forecast_mw":float(dom["forecast_2025_vintage_for_2025_mw"]),
        "DOM_2024vintage_forecast_mw":float(dom["forecast_2024_vintage_for_2025_mw"]),
        "DOM_2025_forecast_error_pct":round(float(dom["error_pct_of_2025forecast"]),3),
        "RTO_2027_future_forecast_revision_mw":rv("RTO",2027),
        "DOM_2027_future_forecast_revision_mw":rv("DOM",2027),
        "RTO_2035_future_forecast_revision_mw":rv("RTO",2035),
        "status":"DESCRIPTIVE_OBSERVED_VS_FORECAST;NOT_CAUSAL_PROOF"
    }
    print(json.dumps(outcome,ensure_ascii=False,indent=2))
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
