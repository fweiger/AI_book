#!/usr/bin/env python3
"""H10 CPI vs PCE paired monthly descriptive audit, Python stdlib only.
Run:
 python analysis/recompute_h10_cpi_pce_alignment.py
 python analysis/recompute_h10_cpi_pce_alignment.py --stdin-csv < csv_file
Correlations are descriptive and NOT a Fed policy or market causality test.
"""
from __future__ import annotations
import csv
import io
import json
import math
import sys
from pathlib import Path


def compute():
    path = Path(__file__).resolve().parent.parent / "data" / "h10_cpi_pce_aligned_monthly_2025_2026.csv"
    raw = sys.stdin.read() if "--stdin-csv" in sys.argv else path.read_text("utf-8")
    r = list(csv.DictReader(io.StringIO(raw)))
    assert len(r) == 21, len(r)
    assert [a["period"] for a in r] == sorted(a["period"] for a in r)
    assert r[0]["period"] == "2025-01" and r[-1]["period"] == "2026-09"
    valid = [x for x in r if x["quality"] == "COMPARABLE_CURRENT_VINTAGE"]
    missing = [x["period"] for x in r if x["quality"] != "COMPARABLE_CURRENT_VINTAGE"]
    assert len(valid) == 18 and missing == ["2025-01", "2025-10", "2025-11"], (len(valid), missing)
    h = ["cpi_headline_mom_pct", "pce_headline_mom_pct", "headline_cpi_minus_pce_pp"]
    c = ["cpi_core_mom_pct", "pce_core_mom_pct", "core_cpi_minus_pce_pp"]
    for v in valid:
        assert abs(float(v[h[0]]) - float(v[h[1]]) - float(v[h[2]])) < 1e-6
        assert abs(float(v[c[0]]) - float(v[c[1]]) - float(v[c[2]])) < 1e-6
    def corr(x, y):
        a = [float(i[x]) for i in valid]
        b = [float(i[y]) for i in valid]
        ax=sum(a)/len(a); by=sum(b)/len(b)
        cov=sum((v-ax)*(w-by) for v,w in zip(a,b))
        sx=math.sqrt(sum((v-ax)**2 for v in a))
        sy=math.sqrt(sum((v-by)**2 for v in b))
        return cov/(sx*sy)
    def mae(gap):
        return sum(abs(float(v[gap])) for v in valid)/len(valid)
    def largest(gap):
        v = max(valid, key=lambda x:abs(float(x[gap])))
        return {"month":v["period"], "cpi_minus_pce_pp":round(float(v[gap]),6)}
    return {
        "validation":"PASS",
        "calendar_months":len(r),
        "comparable_months":len(valid),
        "missing_comparisons":missing,
        "headline_CPI_vs_PCE_MoM_Pearson_r":round(corr(h[0],h[1]),6),
        "core_CPI_vs_PCE_MoM_Pearson_r":round(corr(c[0],c[1]),6),
        "headline_gap_mean_absolute_pp":round(mae(h[2]),6),
        "core_gap_mean_absolute_pp":round(mae(c[2]),6),
        "largest_headline_gap":largest(h[2]),
        "largest_core_gap":largest(c[2]),
        "limitation":"18 matched current-vintage months with gaps; no causal or predictive inference; not FOMC reaction or PCE release-vintage PIT"
    }


if __name__ == "__main__":
    print(json.dumps(compute(),ensure_ascii=False,indent=2))
