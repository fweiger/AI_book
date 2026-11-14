#!/usr/bin/env python3
"""TOPIC-011 H10 BEA NIPA Table 2.8.4 monthly PCE index consistency check.
This CSV is a single 2026-11-14 retrieval, NOT historical release vintages.
Run in repo: python3 analysis/recompute_h10_bea_snapshot.py
Or pass CSV through stdin: python3 analysis/recompute_h10_bea_snapshot.py --stdin-csv
Only stdlib; arithmetic + missing-year checks; does not establish any Fed causality.
"""
import csv
import io
import json
import sys
from pathlib import Path


def f(x):
    return None if x is None or x == "" else float(x)


def ne(x, y, tol=0.000005):
    assert abs(x-y) < tol, (x, y)


def compute():
    path = Path(__file__).resolve().parent.parent / "data" / "h10_bea_nipa_pce_headline_core_2024_2026_snapshot.csv"
    content = sys.stdin.read() if "--stdin-csv" in sys.argv else path.read_text(encoding="utf-8")
    rows = list(csv.DictReader(io.StringIO(content)))
    assert len(rows) == 33, len(rows)
    bym = {r["period"]: r for r in rows}
    assert len(bym) == len(rows)
    assert min(bym) == "2024-01" and max(bym) == "2026-09"
    assert len({r["source_file_sha256"] for r in rows}) == 1
    assert {r["vintage_type"] for r in rows} == {"CURRENT_BEA_NIPA_FLATFILE_NOT_ORIGINAL_MONTHLY_RELEASE"}
    def prior(period, n):
        yr, mm = map(int, period.split("-"))
        v = yr*12+mm-1-n
        return f"{v//12:04d}-{v%12+1:02d}"
    for r in rows:
        now = r["period"]
        p1 = bym.get(prior(now, 1))
        p12 = bym.get(prior(now, 12))
        for key, out in [
            ("pce_headline_index_sa", "pce_headline_mom_pct_derived"),
            ("pce_core_index_sa", "pce_core_mom_pct_derived"),
        ]:
            current = f(r[key])
            prev = f(p1[key]) if p1 else None
            actual = f(r[out])
            if prev is None:
                assert actual is None
            else:
                ne(actual,100*(current/prev-1))
        for key, out in [
            ("pce_headline_index_sa", "pce_headline_yoy_pct_derived"),
            ("pce_core_index_sa", "pce_core_yoy_pct_derived"),
        ]:
            current=f(r[key]); prev=f(p12[key]) if p12 else None; actual=f(r[out])
            if prev is None:
                assert actual is None
            else:
                ne(actual,100*(current/prev-1))
    latest = bym["2026-09"]
    headline_mom = f(latest["pce_headline_mom_pct_derived"])
    core_mom = f(latest["pce_core_mom_pct_derived"])
    headline_yoy = f(latest["pce_headline_yoy_pct_derived"])
    core_yoy = f(latest["pce_core_yoy_pct_derived"])
    assert round(headline_mom,1)==0.5
    assert round(core_mom,1)==0.3
    assert round(headline_yoy,1)==3.6
    assert round(core_yoy,1)==3.1
    return {
        "validation":"PASS",
        "months":len(rows),
        "first":min(bym),
        "last":max(bym),
        "bea_source_sha256":rows[0]["source_file_sha256"],
        "sep2026_headline_mom_percent":round(headline_mom,4),
        "sep2026_core_mom_percent":round(core_mom,4),
        "sep2026_headline_yoy_percent":round(headline_yoy,4),
        "sep2026_core_yoy_percent":round(core_yoy,4),
        "aug2026_core_mom_percent_current_vintage":round(f(bym["2026-08"]["pce_core_mom_pct_derived"]),4),
        "epistemic_limit":"Retrospective index snapshot, not each month's original first-release version; no policy causal identification"
    }


if __name__=="__main__":
    print(json.dumps(compute(),indent=2,ensure_ascii=False))
