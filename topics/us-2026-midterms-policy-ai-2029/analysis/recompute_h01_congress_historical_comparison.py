#!/usr/bin/env python3
"""TOPIC-011 H01 Round 15 — historical congressional law and veto baselines.

Pure Python stdlib; uses published, manually transcribed Congress-level counts.
Validates NARA final public-law IDs, Pew pre-election accounting and selected
official Senate veto/override counts. THIS IS DESCRIPTIVE, NOT CAUSAL.
"""
import csv
import json
import statistics
from pathlib import Path

HERE = Path(__file__).resolve().parent
INPUT = HERE.parent / "data" / "h01_congress_104_119_historical_laws_20261014.csv"
with INPUT.open(encoding="utf-8", newline="") as fp:
    rows = list(csv.DictReader(fp))
assert len(rows) == 16
assert [int(r["congress"]) for r in rows] == list(range(104, 120))
nara = {104:333, 105:394, 106:580, 107:377, 108:498,
        109:482, 110:460, 111:383, 112:283, 113:296,
        114:329, 115:442, 116:344, 117:362, 118:274}
veto = {104:(17,1), 110:(11,4), 116:(10,1), 119:(2,0)}
for r in rows:
    c = int(r["congress"])
    substantive = int(r["pew_substantive_pre_election"])
    ceremonial = int(r["pew_ceremonial_pre_election"])
    pre_total = int(r["pew_public_laws_pre_election"])
    assert substantive + ceremonial == pre_total, c
    assert r["pew_source"].startswith("https://www.pewresearch.org/")
    assert r["nara_source"] == "https://www.archives.gov/federal-register/laws/past"
    if c in nara:
        assert int(r["nara_final_public_laws"]) == nara[c], c
        assert nara[c] >= pre_total, c
    else:
        assert r["nara_final_public_laws"] == "", c
    if c in veto:
        assert (int(r["senate_congress_vetoes"]), int(r["senate_congress_overrides"])) == veto[c], c
    else:
        assert r["senate_congress_vetoes"] == r["senate_congress_overrides"] == "", c
assert rows[3]["government_pattern"] == "SENATE_SWITCHED"

indexed = {int(r["congress"]): r for r in rows}
def stats(congresses):
    included = [indexed[c] for c in congresses]
    sub = [int(r["pew_substantive_pre_election"]) for r in included]
    all_laws = [int(r["pew_public_laws_pre_election"]) for r in included]
    return {
        "congresses": congresses,
        "n": len(congresses),
        "substantive_mean": round(statistics.mean(sub), 3),
        "substantive_median": statistics.median(sub),
        "all_laws_mean": round(statistics.mean(all_laws), 3),
        "all_laws_median": statistics.median(all_laws),
    }

selected = []
for c in (104, 110, 116, 119):
    r = indexed[c]
    a = int(r["pew_substantive_pre_election"])
    b = int(r["pew_ceremonial_pre_election"])
    final = int(r["nara_final_public_laws"]) if r["nara_final_public_laws"] else None
    selected.append({
        "congress":c, "government_pattern":r["government_pattern"],
        "substantive_pre_election":a, "ceremonial_pre_election":b,
        "all_pre_election":a+b, "substantive_share_pct":round(100*a/(a+b),3),
        "nara_end_total":final,
        "post_election_signed_extra":(final-a-b) if final is not None else None,
        "veto_total":int(r["senate_congress_vetoes"]),
        "override_total":int(r["senate_congress_overrides"])
    })

result = {
    "status":"PASS",
    "analysis_asof":"2026-11-14",
    "pew_119th_cutoff":"2026-10-14",
    "row_count":len(rows),
    "selected":selected,
    "groups":{
        "historical_divided_104_118":stats([104,105,106,110,112,113,114,116,118]),
        "historical_unified_104_118":stats([108,109,111,115,117]),
        "unified_including_unfinished_119":stats([108,109,111,115,117,119]),
        "early_divided_1995_2008":stats([104,105,106,110]),
        "early_unified_1995_2008":stats([108,109]),
        "later_divided_2009_2024":stats([112,113,114,116,118]),
        "later_unified_2009_2024":stats([111,115,117]),
        "sensitivity_omit_117_2021_transition":stats([108,109,111,115])
    },
    "checks":{
        "110_minus_104_pre_election_all":int(indexed[110]["pew_public_laws_pre_election"])-int(indexed[104]["pew_public_laws_pre_election"]),
        "110_minus_104_pre_election_substantive":int(indexed[110]["pew_substantive_pre_election"])-int(indexed[104]["pew_substantive_pre_election"]),
        "119_over_110_substantive_ratio":round(int(indexed[119]["pew_substantive_pre_election"])/int(indexed[110]["pew_substantive_pre_election"]),6)
    },
    "limits":[
        "Pew ceremonial vs substantive classification is secondary and generously defined, not official bill-status classification.",
        "Historical values are before election day; 119th is only as of Oct14 2026.",
        "NARA final enacted counts are NOT identical time cutoffs to Pew preelection counts.",
        "119th and its two vetoes are unfinished and subject to future additions.",
        "107th changed Senate control during Congress, excluded from constant-control groups.",
        "117th categorized unified by official House history although Jan3-Jan20 2021 transition existed.",
        "Party-control group averages have very small samples and time trends; cannot estimate causal deadlock effect.",
        "Law counts cannot measure the fiscal size of legislation, number of failed bills, or political effects on AI CAPEX."
    ]
}
print(json.dumps(result, ensure_ascii=False, indent=2))
