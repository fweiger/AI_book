#!/usr/bin/env python3
"""CASE-PRT-001 M2: DEBT.PT historical debt (1641-1800) / Palma-Reis GDP.

Read original, separately downloaded XLSX files using Python's standard library.
Publish only derived annual debt and debt-service percentages, not source workbooks.
Does not replicate ASCM or resolve historical archival uncertainty.
"""
from __future__ import annotations
import argparse
import csv
import hashlib
import io
import math
import re
import sys
import xml.etree.ElementTree as ET
import zipfile
from pathlib import Path

EXPECTED_DEBT_SHA256 = "b2024474a20442b5577ca4667067edf22ffdf71a30faad01971f5a8d13104d17"
EXPECTED_GDP_SHA256 = "ee80439059ebfa3f67f870430671098fe6c853000be64d2605111285ee63045c"
DEBT_URL = "https://debt.pt/pdf/DEBT_%201529-1557%20%26%201641_1800.xlsx"
GDP_URL = "https://drive.google.com/file/d/17M1nrjx-6B7fIMJGNTJ6tle6TtWNkLA7/view"
NS = "{http://schemas.openxmlformats.org/spreadsheetml/2006/main}"
FIELDS = [
    "year", "longterm_debt_stock_pct_nominal_gdp",
    "recorded_shortterm_debt_stock_pct_nominal_gdp",
    "total_recorded_debt_stock_pct_nominal_gdp",
    "longterm_debt_service_pct_nominal_gdp",
    "recorded_shortterm_debt_service_pct_nominal_gdp",
    "total_recorded_debt_service_pct_nominal_gdp",
]


def read_workbook_sheet(path: Path, sheet_number: int) -> list[dict[str, str]]:
    """Parse XLSX cached values read-only. Formula caches must be present."""
    with zipfile.ZipFile(path) as archive:
        strings = []
        if "xl/sharedStrings.xml" in archive.namelist():
            shared = ET.fromstring(archive.read("xl/sharedStrings.xml"))
            strings = ["".join(elem.itertext()) for elem in shared.findall(NS + "si")]
        root = ET.fromstring(archive.read(f"xl/worksheets/sheet{sheet_number}.xml"))
        out = []
        for row in root.findall(".//" + NS + "sheetData/" + NS + "row"):
            record = {}
            for c in row.findall(NS + "c"):
                match = re.match(r"([A-Z]+)[1-9][0-9]*$", c.get("r", ""))
                if not match:
                    continue
                v = c.find(NS + "v")
                inline = c.find(NS + "is")
                value = v.text if v is not None else "".join(inline.itertext()) if inline is not None else None
                if c.get("t") == "s" and value is not None:
                    value = strings[int(value)]
                if value is not None:
                    record[match.group(1)] = value
            out.append(record)
        return out


def annual(rows: list[dict[str, str]], year_col: str, cols: list[str],
           start: int, end: int) -> dict[int, dict[str, float]]:
    data = {}
    for row in rows:
        try:
            year = int(row[year_col])
        except (ValueError, KeyError):
            continue
        if not start <= year <= end:
            continue
        if year in data:
            raise ValueError(f"Duplicate year: {year}")
        data[year] = {column: float(row[column]) for column in cols}
    if sorted(data) != list(range(start, end + 1)):
        raise ValueError(f"Missing/extra annual observations for {start}-{end}")
    if any(not math.isfinite(value) for v in data.values() for value in v.values()):
        raise ValueError("Non-finite numeric value in source workbook")
    return data


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source-debt-xlsx", required=True, type=Path)
    parser.add_argument("--source-gdp-xlsx", required=True, type=Path)
    parser.add_argument("--output", type=Path, help="CSV file; omit to emit CSV to stdout")
    parser.add_argument("--allow-new-version", action="store_true",
                        help="Permit hash mismatch only for separate version investigations")
    args = parser.parse_args()

    for label, path, expected in [
        ("DEBT.PT", args.source_debt_xlsx, EXPECTED_DEBT_SHA256),
        ("Palma-Reis 2019", args.source_gdp_xlsx, EXPECTED_GDP_SHA256),
    ]:
        actual = hashlib.sha256(path.read_bytes()).hexdigest()
        if actual != expected and not args.allow_new_version:
            parser.error(f"{label} source hash mismatch {actual}; refuse silent version drift")

    stock = annual(read_workbook_sheet(args.source_debt_xlsx, 2), "C",
                   ["D", "E", "F"], 1641, 1800)
    service = annual(read_workbook_sheet(args.source_debt_xlsx, 3), "C",
                     ["D", "E", "F"], 1641, 1800)
    gdp = annual(read_workbook_sheet(args.source_gdp_xlsx, 2), "A",
                 ["H"], 1527, 1850)
    output = []
    maximum_stock_error = 0.
    maximum_service_error = 0.
    for year in range(1641, 1801):
        s, v, g = stock[year], service[year], gdp[year]["H"] * 1e6
        if g <= 0 or s["F"] <= 0 or v["F"] < 0:
            raise ValueError(f"Invalid nominal GDP / fiscal data for {year}")
        a = abs(s["D"] + s["E"] - s["F"])
        b = abs(v["D"] + v["E"] - v["F"])
        maximum_stock_error = max(maximum_stock_error, a)
        maximum_service_error = max(maximum_service_error, b)
        if not math.isclose(s["D"] + s["E"], s["F"], rel_tol=1e-11, abs_tol=0.01):
            raise ValueError(f"Debt stock identity mismatch: {year} ({a})")
        if not math.isclose(v["D"] + v["E"], v["F"], rel_tol=1e-11, abs_tol=0.01):
            raise ValueError(f"Debt service identity mismatch: {year} ({b})")
        output.append([
            year,
            *(f"{100 * s[k] / g:.6f}" for k in ("D", "E", "F")),
            *(f"{100 * v[k] / g:.6f}" for k in ("D", "E", "F")),
        ])
    check = {r[0]: float(r[3]) for r in output}
    for year, expected in [(1694, 5.59189), (1763, 9.00743), (1800, 6.39501)]:
        if not math.isclose(check[year], expected, abs_tol=0.0001):
            raise ValueError(f"Benchmark mismatch for year={year}: {check[year]}")
    buf = io.StringIO(newline="")
    w = csv.writer(buf, lineterminator="\n")
    w.writerow(FIELDS)
    w.writerows(output)
    result = buf.getvalue()
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(result, encoding="utf-8")
        print(f"wrote {len(output)} records to {args.output}", file=sys.stderr)
    else:
        sys.stdout.write(result)
    print(f"PASS years={len(output)} stock_err={maximum_stock_error:.6g} "
          f"service_err={maximum_service_error:.6g} "
          f"output_sha256={hashlib.sha256(result.encode('utf-8')).hexdigest()}", file=sys.stderr)


if __name__ == "__main__":
    try:
        main()
    except (OSError, KeyError, ValueError, zipfile.BadZipFile) as exc:
        print(f"FAIL: {exc}", file=sys.stderr)
        raise SystemExit(2)
