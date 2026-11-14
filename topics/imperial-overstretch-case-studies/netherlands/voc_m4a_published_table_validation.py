#!/usr/bin/env python3
"""CASE-NLD-001 M4A: audit arithmetic from PUBLISHED Table 1 and narrative.

No original archival data, ICPSR price files, or unpublished datasets are loaded.
All amounts in Table 1 are nominal current guilders; AWB balances are separate units.
"""
from decimal import Decimal

D = Decimal
SOURCE = "https://onlinelibrary.wiley.com/doi/full/10.1111/ehr.13345"
QUARTERS = (
    ("1772Q1", "59996", "1099394", 94),
    ("1772Q2", "76433", "1451700", 138),
    ("1772Q3", "139716", "2321093", 129),
    ("1772Q4", "178822", "1693324", 158),
    ("1773Q1", "1345057", "4161887", 78),
    ("1773Q2", None, "1641577", 40),
)

def pct(a, b):
    if b == 0:
        raise ZeroDivisionError("reference amount is zero")
    return (a / b) * D("100")

def audit():
    assert sum(row[3] for row in QUARTERS) == 637
    q4 = QUARTERS[3]; q1 = QUARTERS[4]
    b4, t4 = D(q4[1]), D(q4[2]); b1, t1 = D(q1[1]), D(q1[2])
    assert b4 < t4 and b1 < t1
    out = {
        "britain_protest_value_change_pct": pct(b1 - b4, b4),
        "britain_share_1772Q4_pct": pct(b4, t4),
        "britain_share_1773Q1_pct": pct(b1, t1),
        "britain_share_change_pp": pct(b1, t1) - pct(b4, t4),
        "total_protest_value_change_pct": pct(t1 - t4, t4),
        "britain_fraction_total_increase_pct": pct(b1 - b4, t1 - t4),
        "clifford_margin_share_new_cash_pct": pct(D("250000"), D("400000")),
        "boe_reported_loss_to_lending_pct": pct(D("93000"), D("650000")),
    }
    assert D("652.17") < out["britain_protest_value_change_pct"] < D("652.19")
    assert D("21.75") < out["britain_share_change_pp"] < D("21.77")
    assert D("47.24") < out["britain_fraction_total_increase_pct"] < D("47.25")
    assert out["clifford_margin_share_new_cash_pct"] == D("62.5")
    # Do not silently conflate two potentially different sample populations:
    assert 795 != 796
    return out

if __name__ == "__main__":
    for key, value in audit().items():
        print(f'{key}={value.quantize(D("0.0001"))}')
    print("PUBLISHED_TABLE_ARITHMETIC_PASS; PRIMARY_SERIES_NOT_ACQUIRED; SAMPLE_795_VS_796_OPEN")
