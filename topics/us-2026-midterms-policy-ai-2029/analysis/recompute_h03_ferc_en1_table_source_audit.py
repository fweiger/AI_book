#!/usr/bin/env python3
"""H03 2026-11-14: forensic audit of Exelon FERC Exhibit EN1 (2023 vintage).

Checks six rows of FERC exhibit EN1 "Load Adjustments" against the
2023 original PJM Table B-8a Distributed Solar and Table B-9 Above Embedded.

This identifies a source/column mix-up in ONE litigant exhibit row; it does
NOT assess intent, adjudicate the complaint, or disprove subsequent growth.

No external Python dependencies. Optional original PDF flags verify exact SHA
but the six manually extracted source cells are pinned in versioned CSV.

python3 analysis/recompute_h03_ferc_en1_table_source_audit.py
python3 analysis/recompute_h03_ferc_en1_table_source_audit.py \
  --pjm-2023 /path/to/2023-load-report.pdf \
  --ferc-filing /path/to/20261103-el27-11-000.pdf
"""
from __future__ import annotations
import argparse,csv,hashlib,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
SHA_PJM="cf4ce845c13d75d06320360f9db985bc94633cdc06aabcd639c39bb11795e1b0"
SHA_FERC="599ea60395437889244791717260949dc9bdb33ab57c16470f549ddcce5b56c0"
def load(name):
    with (ROOT/"data"/name).open(encoding="utf-8",newline="") as f:return list(csv.DictReader(f))
def n(v):return float(v)
def near(a,b,eps=.000001):assert abs(float(a)-float(b))<eps,(a,b)
def check_pdf(path,sha):
    data=path.read_bytes()
    assert data.startswith(b"%PDF"),"Supplied file not a PDF"
    digest=hashlib.sha256(data).hexdigest()
    if digest!=sha:raise ValueError(f"Original PDF SHA mismatch for {path}: {digest}")
    return len(data)
def main():
    p=argparse.ArgumentParser()
    p.add_argument("--pjm-2023",type=Path)
    p.add_argument("--ferc-filing",type=Path)
    args=p.parse_args()
    six=load("h03_ferc_en1_2023_solar_vs_b9_six_years.csv")
    y5=load("h03_ferc_en1_y5_adjustment_share_audit_2017_2026.csv")
    sources=load("h03_ferc_en1_pdf_source_mapping.csv")
    assert [len(x) for x in (six,y5,sources)]==[6,10,4]
    assert [int(r["target_year"]) for r in six]==list(range(2023,2029))
    assert {r["source_id"] for r in sources}=={
       "PJM_2023_B8a","PJM_2023_B9","EXELON_2026_EN1","PJM_2024_METHOD"}
    litigant=[2888,3269,3566,3841,4035,4185]
    official_solar=[2888,3269,3566,3841,4035,4185]
    official_B9=[2231,3393,4654,6594,8300,9866]
    peak=[149059,149737,150924,152736,154275,155703]
    matched_solar=0;matched_B9=0
    for idx,r in enumerate(six):
        assert r["forecast_vintage"]=="2023" and int(r["horizon"])==idx
        a=n(r["en1_labeled_large_load_mw"])
        b=n(r["official_2023_b8a_distributed_solar_mw"])
        c=n(r["official_2023_b9_above_embedded_mw"])
        v=n(r["official_summer_peak_forecast_mw"])
        assert [a,b,c,v]==[litigant[idx],official_solar[idx],official_B9[idx],peak[idx]]
        matched_solar+=int(a==b)
        matched_B9+=int(a==c)
        near(a-c,r["en1_minus_correct_b9_mw"])
        near(100*a/v,r["en1_share_of_summer_peak_pct"])
        near(100*c/v,r["correct_b9_share_of_summer_peak_pct"])
        near(100*(c-a)/v,r["correct_minus_en1_share_percentage_points"])
        assert r["en1_equal_b8a"]=="true"
        assert r["en1_equal_b9"]=="false"
        assert r["pJm_original_sha256"]==SHA_PJM
        assert r["ferc_litigant_pdf_sha256"]==SHA_FERC
    assert matched_solar==6 and matched_B9==0
    assert [int(r["forecast_vintage"]) for r in y5]==list(range(2017,2027))
    shares={}
    for r in y5:
        v=int(r["forecast_vintage"])
        assert int(r["fifth_year_target_year"])==v+5
        litigant=n(r["en1_load_adjustment_mw"])
        corrected=n(r["corrected_consistent_b9_mw"])
        peak=n(r["PJM_RTO_summer_peak_forecast_mw"])
        near(100*litigant/peak,r["en1_reported_adjustment_share_pct_calculated"])
        near(100*corrected/peak,r["corrected_adjustment_share_pct_calculated"])
        near(100*(corrected-litigant)/peak,r["difference_percentage_points_correct_minus_en1"])
        if v==2023:
            assert (litigant,corrected,peak)==(4185,9866,155703)
            assert r["row_reliability"].startswith("EXELON_EXHIBIT_B8A")
        if v<=2022:
            assert r["row_reliability"].endswith("NOT_VERIFIED_AGAINST_"+str(v)+"_PJM_ORIGINAL")
        shares[v]={"exhibit":100*litigant/peak,"corrected":100*corrected/peak}
    ratio_wrong=shares[2026]["corrected"]/shares[2023]["exhibit"]
    ratio_fixed=shares[2026]["corrected"]/shares[2023]["corrected"]
    assert 8.07<ratio_wrong<8.09 and 3.42<ratio_fixed<3.44
    pdf_info={}
    if args.pjm_2023:pdf_info["pjm_original_pdf_bytes"]=check_pdf(args.pjm_2023,SHA_PJM)
    if args.ferc_filing:pdf_info["ferc_litigant_pdf_bytes"]=check_pdf(args.ferc_filing,SHA_FERC)
    print(json.dumps({
        "pdf_sha_checked":pdf_info,
        "ferc_2023_EN1_exact_matches_to_PJM_B8a_solar":matched_solar,
        "ferc_2023_EN1_exact_matches_to_PJM_B9_large_load":matched_B9,
        "six_target_years":[int(r["target_year"]) for r in six],
        "fifth_year_2028_litigant_adjustment_mw":4185,
        "fifth_year_2028_PJM_original_B9_adjustment_mw":9866,
        "fifth_year_underreport_mw":5681,
        "fifth_year_litigant_share_pct":round(shares[2023]["exhibit"],3),
        "fifth_year_PJM_B9_share_pct":round(shares[2023]["corrected"],3),
        "fifth_year_share_understatement_pp":round(shares[2023]["corrected"]-shares[2023]["exhibit"],3),
        "2026_vintage_fifth_year_load_adjustment_share_pct":round(shares[2026]["corrected"],3),
        "2026_vs_2023_exaggerated_share_multiple_if_using_EN1":round(ratio_wrong,3),
        "2026_vs_2023_share_multiple_using_PJM_original_2023_B9":round(ratio_fixed,3),
        "2017_to_2022_primary_PJM_B9_rows_verified":False,
        "this_is_a_party_submitted_exhibit_not_PJM_certified_historical_panel":True,
        "intent_or_misrepresentation_allegation":"NOT_ASSESSED",
        "political_causality":"UNTESTED"
    },ensure_ascii=False,indent=2))
if __name__=="__main__":main()
