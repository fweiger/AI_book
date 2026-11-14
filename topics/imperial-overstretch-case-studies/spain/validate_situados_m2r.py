#!/usr/bin/env python3
"""Audits M2r's two transcribed Serrano (2020) tables using Python stdlib only."""
from __future__ import annotations

import csv
import json
import sys
from decimal import Decimal
from pathlib import Path

BASE = Path(__file__).resolve().parent
SOURCE = "https://www.scielo.org.mx/scielo.php?pid=S1405-22532020000100002&script=sci_arttext"

def rows(filename: str) -> list[dict[str, str]]:
    path = BASE / filename
    with path.open("r", encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        if reader.fieldnames is None:
            raise ValueError(f"{filename}: missing header")
        data = list(reader)
        if not data or any(None in d for d in data):
            raise ValueError(f"{filename}: missing or extra columns")
    return data

def check(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)

def decimal_sum(data: list[dict[str, str]], field: str) -> Decimal:
    return sum((Decimal(r[field]) for r in data), Decimal(0))

def main() -> int:
    sent = rows("barlovento_dual_sender_reconstructions_m2r.csv")
    received = rows("havana_reception_account_table4_m2r.csv")
    check([int(r["year"]) for r in sent] == list(range(1765, 1789)), "Table1 years missing/duplicate")
    check([int(r["year"]) for r in received] == list(range(1766, 1789)), "Table4 years missing/duplicate")
    s = decimal_sum(sent, "serrano_reconstruction_pesos")
    m = decimal_sum(sent, "marichal_souto_klein_pesos")
    ht = decimal_sum(received, "havana_total_receipts_pesos")
    hs = decimal_sum(received, "havana_received_situados_pesos")
    check((s, m) == (Decimal(84453062), Decimal(103172038)), "Table1 totals fail")
    check((ht, hs) == (Decimal(112185483), Decimal(74541779)), "Table4 totals fail")
    for r in sent:
        check(Decimal(r["marichal_souto_klein_pesos"]) - Decimal(r["serrano_reconstruction_pesos"])
              == Decimal(r["difference_msk_minus_serrano_pesos"]), "Table1 annual delta fail")
    for r in received:
        calc = Decimal(100) * Decimal(r["havana_received_situados_pesos"]) / Decimal(r["havana_total_receipts_pesos"])
        check(abs(calc - Decimal(r["computed_annual_share_percent"])) < Decimal("0.000001"), "share precision fail")
        check(int(calc + Decimal("0.5")) == int(r["published_annual_share_percent"]), "published rounded share mismatch")
    wrong_denominator = Decimal(24)
    actual_denominator = Decimal(len(received))
    check((ht / wrong_denominator).quantize(Decimal("1")) == Decimal(4674395), "published total mean mismatch")
    check((hs / wrong_denominator).quantize(Decimal("1")) == Decimal(3105907), "published situado mean mismatch")
    paper_unweighted_share = sum(Decimal(r["published_annual_share_percent"]) for r in received) / actual_denominator
    original_sender_same_years = sum(Decimal(r["serrano_reconstruction_pesos"]) for r in sent if int(r["year"]) >= 1766)
    out = {
      "status": "PASS_SOURCE_TRANSCRIPTION_ARITHMETIC_ONLY",
      "source": SOURCE,
      "sender_table_years": len(sent), "receiver_table_years": len(received),
      "sender_serrano_total_pesos": int(s), "sender_msk_total_pesos": int(m),
      "disagreement_pesos": int(m-s), "disagreement_pct_of_msk": float(100*(m-s)/m),
      "havana_total_receipts_pesos": int(ht), "havana_received_situados_pesos": int(hs),
      "published_mean_total_pesos": 4674395, "correct_23_year_mean_total_pesos": float(ht / actual_denominator),
      "published_mean_situados_pesos": 3105907, "correct_23_year_mean_situados_pesos": float(hs / actual_denominator),
      "matching_published_24_denominator": True,
      "havana_aggregate_situados_share_percent": float(100*hs/ht),
      "unweighted_annual_share_using_published_rounded_percents_percent": float(paper_unweighted_share),
      "sending_1766_1788_serrano_pesos": int(original_sender_same_years),
      "sender_receiver_difference_pesos": int(original_sender_same_years-hs),
      "original_archival_account_reproduction": "NOT_RUN",
      "causal_estimation": "NOT_RUN"
    }
    print(json.dumps(out, ensure_ascii=False, indent=2))
    return 0

if __name__ == "__main__":
    try:
        sys.exit(main())
    except (OSError, ValueError, ArithmeticError, AssertionError) as exc:
        print(json.dumps({"status": "FAIL", "error": str(exc)}, ensure_ascii=False), file=sys.stderr)
        sys.exit(1)
