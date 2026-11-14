#!/usr/bin/env python3
"""CASE-PRT-001 M2: 2025 published Brazilian gold remittances / 2019 Portugal GDP.

Supply the author's historical XLSX separately and the curated, short Table B.1 CSV.
The program does not re-estimate ASCM or mirror the 324-row annual input data.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import math
import sys
import zipfile
from pathlib import Path

from reproduce_gdp_from_author_xlsx import EXPECTED_SHA256, read_sheet

FIELDS = (
    "period", "year_start", "year_end", "nominal_gdp_five_year_sum_million_reis",
    "nominal_gold_remittances_five_year_million_reis", "gold_to_gdp_pct",
    "public_gold_to_gdp_pct", "private_gold_to_gdp_pct", "mean_annual_pcgdp_1990_gk",
    "gold_source", "gdp_source",
)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", required=True, type=Path, help="Palma/Reis 2019 author XLSX")
    parser.add_argument("--gold-file", required=True, type=Path, help="Published Table B.1 transcription CSV")
    parser.add_argument("--output", required=True, type=Path, help="Derived short public CSV output")
    parser.add_argument("--allow-new-version", action="store_true", help="Explicitly accept XLSX hash mismatch")
    args = parser.parse_args()

    source_hash = hashlib.sha256(args.source.read_bytes()).hexdigest()
    if source_hash != EXPECTED_SHA256 and not args.allow_new_version:
        parser.error("Author XLSX hash mismatch; use --allow-new-version for separate version-audit outputs")

    with zipfile.ZipFile(args.source) as source_zip:
        sheet = read_sheet(source_zip, "GDPs")
    annual = {}
    for cell in sheet[1:]:
        if cell.get("A") is None:
            continue
        year = int(cell["A"])
        if year in annual:
            raise ValueError(f"Duplicate GDP year {year}")
        annual[year] = (float(cell["H"]), float(cell["B"]))
    if sorted(annual) != list(range(1527, 1851)):
        raise ValueError("Incomplete or unexpected author annual GDP years")
    if any(not (math.isfinite(nom) and math.isfinite(pcgdp) and nom > 0 and pcgdp > 0)
           for nom, pcgdp in annual.values()):
        raise ValueError("Nonpositive or nonfinite GDP")

    with args.gold_file.open("r", encoding="utf-8-sig", newline="") as f:
        gold_rows = list(csv.DictReader(f))
    if len(gold_rows) != 17:
        raise ValueError("Expected 17 five-year Table B.1 rows")

    result = []
    total_private = total_public = total_gdp = 0.0
    for index, row in enumerate(gold_rows):
        start, end = int(row["year_start"]), int(row["year_end"])
        if start != 1720 + 5 * index or end != start + 4:
            raise ValueError(f"Noncontiguous five-year B.1 interval: {row['period']}")
        # Publication transcriptions have integer nominal million-reis units.
        private = int(row["private_nominal_million_reis"])
        public = int(row["public_nominal_million_reis"])
        gold = int(row["total_nominal_million_reis"])
        if min(private, public, gold) < 0 or gold != private + public:
            raise ValueError(f"Unbalanced public/private gold categories: {row['period']}")
        gdp = sum(annual[y][0] for y in range(start, end + 1))
        pcgdp_mean = sum(annual[y][1] for y in range(start, end + 1)) / 5
        result.append(dict(zip(FIELDS, (
            f"{start}-{end}", start, end, f"{gdp:.6f}", gold,
            f"{100 * gold / gdp:.6f}", f"{100 * public / gdp:.6f}",
            f"{100 * private / gdp:.6f}", f"{pcgdp_mean:.6f}",
            "Kedrosky_Palma_2025_Supplement_B1_p31", "Palma_Reis_2019_author_GDPs_H",
        ))))
        total_private += private
        total_public += public
        total_gdp += gdp

    if int(total_private) != 211080 or int(total_public) != 59965:
        raise ValueError("Gold public/private checksum differs from official B.1 published table")
    if not 9_000_000 < total_gdp < 10_000_000:
        raise ValueError("Unexpected denominator scale (possible currency unit mismatch)")
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=FIELDS, lineterminator="\n")
        w.writeheader()
        w.writerows(result)
    print(f"SOURCE_SHA256={source_hash} verified={source_hash == EXPECTED_SHA256}")
    print(f"ROWS={len(result)} GDP_85Y_MILLION_REIS={total_gdp:.6f}")
    print(f"GOLD_TO_GDP_PCT={100*(total_private+total_public)/total_gdp:.6f}")
    print(f"PUBLIC_TO_GDP_PCT={100*total_public/total_gdp:.6f}")
    print(f"PRIVATE_TO_GDP_PCT={100*total_private/total_gdp:.6f}")
    print(f"OUTPUT_SHA256={hashlib.sha256(args.output.read_bytes()).hexdigest()}")


if __name__ == "__main__":
    try:
        main()
    except (ValueError, KeyError, OSError, zipfile.BadZipFile) as exc:
        print(f"M2 Gdp/gold bridge failed: {exc}", file=sys.stderr)
        raise SystemExit(2)
