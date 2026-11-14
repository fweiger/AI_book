#!/usr/bin/env python3
"""CASE-PRT-001: reproducible *derived summaries* from Palma-Reis (2019) XLSX.

Usage:
  python3 reproduce_gdp_from_author_xlsx.py \
    --source palmareis_JEH_2019.xlsx --output-dir ./derived

Inputs must be obtained from the original author's publicly referenced file.
This program does NOT redistribute the source workbook. Standard library only.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import json
import math
import re
import sys
import xml.etree.ElementTree as ET
import zipfile
from pathlib import Path

EXPECTED_SHA256 = "ee80439059ebfa3f67f870430671098fe6c853000be64d2605111285ee63045c"
AUTHOR_URL = "https://drive.google.com/file/d/17M1nrjx-6B7fIMJGNTJ6tle6TtWNkLA7/view"
DOI_2019 = "https://doi.org/10.1017/S0022050719000056"
DOI_2025 = "https://doi.org/10.1017/S0022050725100764"
NS = "{http://schemas.openxmlformats.org/spreadsheetml/2006/main}"
REL = "{http://schemas.openxmlformats.org/officeDocument/2006/relationships}"
PACKAGE_REL = "{http://schemas.openxmlformats.org/package/2006/relationships}"


def as_number(v: str | None):
    if v is None or v == "":
        return None
    try:
        return float(v)
    except ValueError:
        return v


def read_sheet(zf: zipfile.ZipFile, sheet_name: str):
    wb = ET.fromstring(zf.read("xl/workbook.xml"))
    rels = ET.fromstring(zf.read("xl/_rels/workbook.xml.rels"))
    paths = {r.get("Id"): r.get("Target") for r in rels.findall(f"{PACKAGE_REL}Relationship")}
    target = None
    for sheet in wb.findall(f"{NS}sheets/{NS}sheet"):
        if sheet.get("name") == sheet_name:
            target = paths.get(sheet.get(f"{REL}id"))
            break
    if not target:
        raise ValueError(f"Required worksheet not found: {sheet_name}")
    path = target.lstrip("/") if target.startswith("/") else "xl/" + target
    if not path.startswith("xl/worksheets/") or ".." in path:
        raise ValueError(f"Unexpected XLSX worksheet path: {path}")
    if "xl/sharedStrings.xml" in zf.namelist():
        ss = ET.fromstring(zf.read("xl/sharedStrings.xml"))
        strings = ["".join(x.itertext()) for x in ss.findall(f"{NS}si")]
    else:
        strings = []
    root = ET.fromstring(zf.read(path))
    result = []
    for row in root.findall(f"{NS}sheetData/{NS}row"):
        d = {}
        for c in row.findall(f"{NS}c"):
            ref = c.get("r") or ""
            m = re.match(r"^([A-Z]+)(\d+)$", ref)
            if not m:
                continue
            col = m.group(1)
            node = c.find(f"{NS}v")
            if node is None:
                inline = c.find(f"{NS}is")
                value = "".join(inline.itertext()) if inline is not None else None
            elif c.get("t") == "s":
                value = strings[int(node.text)]
            else:
                value = as_number(node.text)
            d[col] = value
        result.append(d)
    return result


def output_csv(path: Path, fieldnames: list[str], rows: list[dict]):
    with path.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def round6(v):
    return round(float(v), 6)


def change(a: float, b: float):
    return round6((b / a - 1) * 100)


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--source", type=Path, required=True, help="Author XLSX (download separately)")
    ap.add_argument("--output-dir", type=Path, required=True)
    ap.add_argument("--allow-new-version", action="store_true", help="Allow source hash mismatch but flag it")
    args = ap.parse_args(argv)
    source = args.source.resolve()
    b = source.read_bytes()
    source_sha = hashlib.sha256(b).hexdigest()
    verified = source_sha == EXPECTED_SHA256
    if not verified and not args.allow_new_version:
        raise SystemExit("Workbook SHA-256 mismatch: do not silently mix versions. Use --allow-new-version to inspect explicitly.")
    with zipfile.ZipFile(source) as zf:
        gp = read_sheet(zf, "GDPs")
        cp = read_sheet(zf, "CPIs")
    if not gp or not cp:
        raise ValueError("Empty workbook sheet(s)")
    records = {}
    for g in gp[1:]:
        if g.get("A") is None:
            continue
        y = int(g["A"])
        if y in records:
            raise AssertionError(f"Duplicate GDP year: {y}")
        records[y] = {
            "year": y, "pc_gdp_1990_gk": float(g["B"]), "population_persons": float(g["C"]),
            "population_million": float(g["D"]), "real_gdp_million_1990_gk": float(g["E"]),
            "real_gdp_index_1850_100": float(g["F"]), "nominal_gdp_index_1850_100": float(g["G"]),
            "nominal_gdp_million_reis": float(g["H"]),
        }
    cpi = {}
    for c in cp[1:]:
        if c.get("A") is None:
            continue
        y = int(c["A"])
        if y in cpi:
            raise AssertionError(f"Duplicate CPI year: {y}")
        cpi[y] = {"cpi_silver_1850_100":float(c["B"]), "silver_price_reis_per_gram":float(c["C"]),
                  "silver_price_index_1850_100":float(c["D"]), "cpi_reis_1850_100":float(c["E"])}
    years = list(range(1527,1851))
    if sorted(records) != years or sorted(cpi) != years:
        raise AssertionError("Unexpected year ranges or missing years")
    max_real_err = max(abs(r["pc_gdp_1990_gk"]*r["population_million"]-r["real_gdp_million_1990_gk"]) for r in records.values())
    max_cpi_err = max(abs(c["cpi_silver_1850_100"]*c["silver_price_index_1850_100"]/100-c["cpi_reis_1850_100"]) for c in cpi.values())
    if max_real_err > 1e-7 or max_cpi_err > 1e-7:
        raise AssertionError(f"Arithmetic consistency failed: GDP={max_real_err}; CPI={max_cpi_err}")
    for r in records.values():
        if any(not math.isfinite(float(v)) or float(v)<=0 for k,v in r.items() if k!="year"):
            raise AssertionError("Invalid nonpositive GDP measure")
    args.output_dir.mkdir(parents=True,exist_ok=True)
    # Only derived aggregates and selected-year citation audit are published. No full source series mirror.
    bench_years = (1527,1550,1600,1650,1680,1694,1700,1710,1750,1755,1800,1807,1822,1850)
    paper_table = {1650:830,1700:830,1750:1372,1800:916,1850:923}
    benchmarks=[]
    for y in bench_years:
        r=records[y]; c=cpi[y]
        published=paper_table.get(y)
        benchmarks.append({"year":y,"pc_gdp_1990_gk":round6(r["pc_gdp_1990_gk"]),
            "population_persons":int(r["population_persons"]),"real_gdp_million_1990_gk":round6(r["real_gdp_million_1990_gk"]),
            "cpi_silver_1850_100":round6(c["cpi_silver_1850_100"]),
            "cpi_reis_1850_100":round6(c["cpi_reis_1850_100"]),
            "published_2025_table1_pc_gdp":published if published is not None else "",
            "published_minus_author_2019":round6(published-r["pc_gdp_1990_gk"]) if published is not None else "",
            "source_2019":DOI_2019,"comparison_2025":DOI_2025 if published is not None else ""})
    output_csv(args.output_dir/"gdp_benchmarks_m2.csv",list(benchmarks[0]),benchmarks)
    decades=[]
    for decade in range(1520,1860,10):
        ys=[y for y in years if decade<=y<decade+10]
        if not ys:continue
        n=len(ys)
        decades.append({"decade_label":f"{decade}s", "year_start":ys[0],"year_end":ys[-1],"n_years":n,
            "mean_pc_gdp_1990_gk":round6(sum(records[y]["pc_gdp_1990_gk"] for y in ys)/n),
            "mean_population_persons":round(sum(records[y]["population_persons"] for y in ys)/n),
            "mean_real_gdp_million_1990_gk":round6(sum(records[y]["real_gdp_million_1990_gk"] for y in ys)/n),
            "mean_cpi_silver_1850_100":round6(sum(cpi[y]["cpi_silver_1850_100"] for y in ys)/n),
            "mean_cpi_reis_1850_100":round6(sum(cpi[y]["cpi_reis_1850_100"] for y in ys)/n),
            "annual_years_complete":n==10,"author_source":DOI_2019})
    output_csv(args.output_dir/"gdp_decadal_aggregates_m2.csv",list(decades[0]),decades)
    spans=[(1650,1700),(1694,1700),(1700,1750),(1694,1750),(1750,1755),(1750,1800),(1755,1800),(1800,1822),(1800,1850)]
    changes=[]
    for y0,y1 in spans:
        r0=records[y0];r1=records[y1]
        changes.append({"year_start":y0,"year_end":y1,"pc_gdp_pct_change":change(r0["pc_gdp_1990_gk"],r1["pc_gdp_1990_gk"]),
            "population_pct_change":change(r0["population_persons"],r1["population_persons"]),
            "real_gdp_pct_change":change(r0["real_gdp_million_1990_gk"],r1["real_gdp_million_1990_gk"]),
            "scope":"two_point_descriptive_not_causal", "author_source":DOI_2019})
    output_csv(args.output_dir/"gdp_window_changes_m2.csv",list(changes[0]),changes)
    variables = [
      ("GDPs","A","year","calendar year","individual year"),
      ("GDPs","B","pc_gdp_1990_gk","1990 Geary-Khamis international dollars per capita","historical model reconstruction"),
      ("GDPs","C","population_persons","persons","historical population reconstruction"),
      ("GDPs","D","population_million","million persons","C divided by 1000000"),
      ("GDPs","E","real_gdp_million_1990_gk","million 1990 GK international dollars","B multiplied by D"),
      ("GDPs","F","real_gdp_index_1850_100","index (1850=100)","real GDP relative to 1850"),
      ("GDPs","G","nominal_gdp_index_1850_100","index (1850=100)","nominal GDP relative to 1850"),
      ("GDPs","H","nominal_gdp_million_reis","million reis (contos de reis)","historically reconstructed nominal GDP"),
      ("CPIs","A","year","calendar year","individual year"),
      ("CPIs","B","cpi_silver_1850_100","index (1850=100)","aggregate CPI valued in silver; NOT a real exchange rate or sectoral nontradable price"),
      ("CPIs","C","silver_price_reis_per_gram","reis per gram of silver","silver conversion factor"),
      ("CPIs","D","silver_price_index_1850_100","index (1850=100)","silver price index"),
      ("CPIs","E","cpi_reis_1850_100","index (1850=100)","B multiplied by D/100; aggregate nominal CPI, NOT sectoral nontradables index"),
    ]
    dfields=["sheet","author_excel_column","normalized_variable","unit","definition_and_limit","source_2019"]
    dictionary=[dict(zip(dfields,[*v,DOI_2019])) for v in variables]
    output_csv(args.output_dir/"gdp_source_variable_dictionary_m2.csv",dfields,dictionary)
    # Additional documented averages for sensitivity to point-year noise.
    rolling=[]
    for n in (1,5,11,21):
        z=n//2
        avg={y:sum(records[t]["pc_gdp_1990_gk"] for t in range(y-z,y+z+1))/n for y in (1700,1750,1800)}
        rolling.append({"centered_window_years":n,"pc_gdp_1700":round6(avg[1700]),"pc_gdp_1750":round6(avg[1750]),
                        "pc_gdp_1800":round6(avg[1800]),"growth_1700_to_1750_pct":change(avg[1700],avg[1750]),
                        "growth_1750_to_1800_pct":change(avg[1750],avg[1800]),"source_2019":DOI_2019})
    output_csv(args.output_dir/"gdp_rolling_sensitivity_m2.csv",list(rolling[0]),rolling)
    # Manifest captures input provenance and deterministic output hashes.
    files=["gdp_benchmarks_m2.csv","gdp_decadal_aggregates_m2.csv","gdp_window_changes_m2.csv","gdp_rolling_sensitivity_m2.csv","gdp_source_variable_dictionary_m2.csv"]
    manifest={
        "case_id":"CASE-PRT-001", "phase":"M2", "workbook_name":source.name,
        "author_workbook_source_url":AUTHOR_URL,"author_workbook_sha256":source_sha,
        "expected_source_sha256":EXPECTED_SHA256,"source_hash_verified":verified,
        "author_citation":DOI_2019,"historical_gdp_units":"1990 Geary-Khamis international dollars",
        "years":{"first":years[0],"last":years[-1],"count":len(years)},
        "consistency":{"max_abs_real_gdp_identity_error":max_real_err,"max_abs_cpi_index_identity_error":max_cpi_err},
        "publication_conflict":{"year":1700,"author_workbook_pc_gdp":records[1700]["pc_gdp_1990_gk"],
            "published_2025_table1_pc_gdp":830,"status":"SOURCE_CONFLICT_UNRESOLVED_NOT_A_PROVEN_MODEL_INPUT_ERROR"},
        "license_notice":"Author source workbook linked, not redistributed. Public redistribution license not verified; derivatives here are selected benchmarks and aggregated statistics.",
        "status":{"workbook_audit":"PASS","model_replication":"NOT_RUN","annual_fiscal":"NOT_ACQUIRED"},
        "outputs":{f:hashlib.sha256((args.output_dir/f).read_bytes()).hexdigest() for f in files},
    }
    with (args.output_dir/"gdp_source_manifest_m2.json").open("w",encoding="utf-8") as f:
        json.dump(manifest,f,ensure_ascii=False,indent=2,sort_keys=True)
        f.write("\n")
    print(json.dumps({"years":len(years),"decades":len(decades),"benchmark_rows":len(benchmarks),
        "source_sha256":source_sha,"real_identity_err":max_real_err,"cpi_identity_err":max_cpi_err,
        "bench_1700":records[1700]["pc_gdp_1990_gk"],"published_2025_1700":830,
        "outputs":list(manifest["outputs"])},ensure_ascii=False,sort_keys=True))

if __name__ == "__main__":
    try:main()
    except (ValueError,AssertionError,KeyError,zipfile.BadZipFile) as exc:
        print(f"Data verification failed: {exc}",file=sys.stderr)
        raise SystemExit(2)
