#!/usr/bin/env python3
"""TOPIC-011 H03 v0.2.x audit: 2026-Jan uncorrected B-9 availability gate.

Read the PJM source-provenance audit and compare annual RTO summer-peak
forecast revisions with original (Jan-modified) B-9b Total Associated.
NOT a causal contribution or attribution model; B-9b includes embedded load.

By design this script will NOT infer 2026-Feb6 B-9 correction effect when no
true pre-correction B-9 table has been obtained and verified.
No nonstandard libraries.
"""
from __future__ import annotations
import argparse,csv,hashlib,json,math
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
PDF_SHA="9f2826cfc39357c54d6e6203e60946b6ce9ea627cfceeeaf4d4cd343066c6bc8"
JAN_B9B_SHA="ee3b682929db0b59a043c8ab6d1c9776f697ab10fc86fe603a6d0d724893c4ba"
FEB_B9_SHA="990e2cb82d02a6c689a9e21b5c7ccb13944613f960dcc2f6eb3109e51a49d6a1"
COMBINED_SHA="59a62facf819962e430101c96dd1335229d8173fb6886dd8045ced325443f607"
ACCURACY_SHA="e0f24fe03a79af016826089c653b2c2e15e55edcb04a7bd4be5fa643136425fc"
def load(file):
    with (ROOT/"data"/file).open(encoding="utf-8",newline="") as f:return list(csv.DictReader(f))
def num(v):return float(v)
def near(a,b,eps=.0011):assert abs(a-b)<eps,(a,b)

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument("--jan-report-pdf",type=Path,help="Optional official 36-page Jan 14 report PDF; verifies SHA only")
    opts=parser.parse_args()
    reg=load("h03_pre_correction_b9_source_availability.csv")
    rev=load("h03_rto_2025_2026_summer_vs_b9b_revision_magnitude.csv")
    assert (len(reg),len(rev))==(10,4)
    index={r["source_id"]:r for r in reg}
    assert len(index)==10
    assert index["PJM_JAN14_B9_PRE_CORRECTION"]["availability_status"]=="NOT_LOCATED_UNCORRECTED_B9"
    assert not index["PJM_JAN14_B9_PRE_CORRECTION"]["sha256_if_accessed"]
    assert index["PJM_JAN14_B9_PRE_CORRECTION"]["bytes_if_accessed"]==""
    assert index["PJM_2026_MAIN_PDF_JAN14"]["sha256_if_accessed"]==PDF_SHA
    assert int(index["PJM_2026_MAIN_PDF_JAN14"]["pages_if_pdf"])==36
    assert index["PJM_JAN14_B9B_INDEPENDENT"]["sha256_if_accessed"]==JAN_B9B_SHA
    assert index["PJM_FEB6_B9_CORRECTED"]["sha256_if_accessed"]==FEB_B9_SHA
    assert index["PJM_2026_COMBINED_CURRENT"]["sha256_if_accessed"]==COMBINED_SHA
    assert index["PJM_2026_MAY_ACCURACY"]["sha256_if_accessed"]==ACCURACY_SHA
    assert index["WAYBACK_CDX_PRE_FEB_SEARCH"]["availability_status"]=="REQUEST_TIMEOUT_NOT_PROOF_ARCHIVE_ABSENT"
    assert index["PUBLIC_GITHUB_COPIES_OCT2026"]["sha256_if_accessed"]==COMBINED_SHA
    if opts.jan_report_pdf is not None:
        contents=opts.jan_report_pdf.read_bytes()
        assert contents.startswith(b"%PDF"),"Not an original PDF"
        digest=hashlib.sha256(contents).hexdigest()
        if digest!=PDF_SHA:raise ValueError(f"Different report PDF SHA: {digest}")
        assert len(contents)==8750526,("Original bytes",len(contents))
    assert [int(x["target_year"]) for x in rev]==[2027,2028,2029,2030]
    result=[]
    for r in rev:
        y=int(r["target_year"])
        old_peak=num(r["v2025_rto_summer_peak_mw"])
        new_peak=num(r["v2026_rto_summer_peak_mw"])
        old_b9b=num(r["v2025_original_b9b_total_mw"])
        new_b9b=num(r["v2026_jan_standalone_b9b_total_mw"])
        peak_change=new_peak-old_peak
        b9b_change=new_b9b-old_b9b
        assert peak_change!=0 and old_peak>0 and new_peak>0
        near(peak_change,num(r["summer_peak_revision_mw"]))
        near(b9b_change,num(r["b9b_total_revision_mw"]))
        near(100*abs(b9b_change)/abs(peak_change),num(r["abs_revision_magnitude_ratio_percent"]))
        sign="OPPOSITE_SIGN" if peak_change*b9b_change<0 else "SAME_SIGN"
        assert r["direction"]==sign
        assert "NOT causal" in r["critical_caveat"] or "NOT causal" in r["critical_caveat"].upper().replace("NOT CAUSAL","NOT causal")
        result.append({"target":y,"summer_peak_revision_MW":peak_change,
            "b9b_total_revision_MW":b9b_change,
            "absolute_revision_magnitude_ratio_pct":round(100*abs(b9b_change)/abs(peak_change),3),
            "opposite_sign":sign=="OPPOSITE_SIGN"})
    assert all(46<z["absolute_revision_magnitude_ratio_pct"]<50 for z in result[:3])
    assert result[-1]["opposite_sign"] is True
    print(json.dumps({
        "report_sha256_verified":opts.jan_report_pdf is not None,
        "original_uncorrected_jan2026_B9_found":False,
        "exact_Feb6_embedded_B9_correction_mw":None,
        "recovery_from_original_Jan14_36page_report":"NOT_AVAILABLE_B9_NUMERIC_TABLES_SEPARATE_XLSX",
        "old_public_archive_checks":"TIMEOUT_NOT_EVIDENCE_OF_ABSENCE",
        "comparison":[*result],
        "B9b_and_RTO_summer_are_not_additive":"RATIO_IS_ONLY_MAGNITUDE_COMPARISON",
        "political_causality":"UNTESTED"
    },ensure_ascii=False,indent=2))
if __name__=="__main__":main()
