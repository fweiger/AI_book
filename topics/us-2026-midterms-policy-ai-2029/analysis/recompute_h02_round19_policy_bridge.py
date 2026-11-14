#!/usr/bin/env python3
"""Round 19: official enacted laws and CBO S.2 marginal score (NOT policy causality).
The CBO PDF figures are transcribed from the official 2026-06-10 score;
its bytes are not downloaded in this script. Optional --verify-gpo checks six
GPO law HTML file SHA256 and seven S.2 enacted statutory section amounts.
"""
import csv,hashlib,json,re,sys,urllib.request
from pathlib import Path
from decimal import Decimal
D=Path(__file__).resolve().parent.parent/"data"
def read(name):
    with (D/name).open(encoding="utf8",newline="") as f:return list(csv.DictReader(f))
def row(xs,key,val):
    matched=[x for x in xs if x[key]==val]
    assert len(matched)==1,(key,val,len(matched))
    return matched[0]
def d(v):return Decimal(v or "0")
laws=read("h02_round19_2026_election_pre_enacted_bills.csv")
sources=read("h02_round19_119th_sources_sha.csv")
scores=read("h02_round19_cbo_budget_bridges_scored_vs_unscored.csv")
parts=read("h02_round19_pl11998_secure_america_cbo_section_outlays.csv")
statutes=read("h02_round19_6_enacted_law_sha.csv")
bridge=read("h02_round19_fy2026_29_partial_policy_score_bridge.csv")
assert (len(laws),len(sources),len(scores),len(parts),len(statutes),len(bridge))==(67,4,11,7,6,4)
lawnums=[int(x["law_number"].split("-")[1]) for x in laws]
assert lawnums==list(range(70,137))
assert all("2026-01-15"<=x["law_date"]<="2026-11-02" for x in laws)
assert {r["type"] for r in sources}=={"hr","s","hjres","sjres"}
assert all(len(x["sha256"])==64 for x in sources+statutes)
for n,b in [(74,"HR6938"),(75,"HR7148"),(86,"HR7147"),(98,"S2"),(101,"HR6644"),(103,"HR6500")]:
    assert row(laws,"law_number","119-"+str(n))["bill"]==b
authority={"101":9550,"102":7450,"103":3450,"104":2500,"201":13020,"202":31075,"203":2500}
assert {x["section"]:int(x["fy2026_budget_authority_usd_m"]) for x in parts}==authority
assert sum(authority.values())==69545
years={2026:8817,2027:15482,2028:17913,2029:20038,2030:5416,2031:1809,2032:48,2033:18,2034:4,2035:0}
for y,total in years.items():
    assert sum(int(x["fy"+str(y)+"_outlays_usd_m"] or "0") for x in parts)==total
assert sum(years.values())==69545
assert sum(years[y] for y in (2027,2028,2029))==53433
assert {x["section"] for x in parts if x["cbo_outlays_2026_censored_lt_500k"]=="YES"}=={"104","203"}
s2=row(scores,"id","R19-06")
assert d(s2["fy2026_budget_authority_delta_usd_bn"])==Decimal("69.545")
for y in (2027,2028,2029):
    assert d(s2["fy"+str(y)+"_direct_outlay_delta_usd_bn"])*1000==years[y]
assert d(s2["fy2027_2029_direct_outlays_sum_usd_bn"])==Decimal("53.433")
assert d(row(scores,"id","R19-01")["fy2026_budget_authority_delta_usd_bn"])==2
assert d(row(scores,"id","R19-05")["rescinded_prior_authority_usd_bn"])==Decimal("11.661")
assert row(scores,"id","R19-04")["evidence_status"]=="PRELIMINARY_VERSION_NOT_FINAL_SCORE"
cr=row(scores,"id","R19-08")
assert d(cr["fy2027_budget_authority_annualized_total_usd_bn"])==Decimal("1700.879")
assert d(cr["fy2027_outlays_annualized_total_usd_bn"])==Decimal("1869.190")
assert all(x["complete_pre_election_policy_forecast"]=="NO_OFFICIAL_UPDATED_TOTAL_AS_OF_2026_11_02" for x in bridge)
for y in range(2026,2030):
    x=row(bridge,"fiscal_year","FY"+str(y))
    assert d(x["s2_pl11998_scored_direct_outlays_increment_usd_bn"])*1000==years[y]
assert len({x["law_id"] for x in statutes})==6
if "--verify-gpo" in sys.argv:
    from html import unescape
    raw={}
    for r in statutes:
        req=urllib.request.Request(r["gpo_html_url"],headers={"User-Agent":"TOPIC011-CBO-budget-source-audit"})
        with urllib.request.urlopen(req,timeout=80) as response: b=response.read()
        assert len(b)==int(r["bytes"]) and hashlib.sha256(b).hexdigest()==r["sha256"],r["law_id"]
        raw[r["law_id"]]=unescape(re.sub("<[^>]*>"," ",b.decode("utf8")))
    s=raw["119-98"]
    for sec,amt in authority.items():
        positions=list(re.finditer(r"\bSEC\.\s*"+sec+r"\.",s,re.I))
        assert positions,sec
        start=positions[-1].end()
        nxt=re.search(r"\bSEC\.\s*\d+\.",s[start:],re.I)
        text=s[start:(start+nxt.start() if nxt else len(s))]
        assert "$"+format(amt*1000000,",") in text,(sec,amt)
    assert "$11,661,000,000" in raw["119-75"]
    assert "December 11, 2026" in raw["119-103"]
    assert "DIVISION I" in raw["119-75"].upper() and "DIVISION J" in raw["119-75"].upper()
print(json.dumps({
  "status":"PASS","asof":"2026-11-14","enacted_laws":len(laws),
  "laws_legal_sequence":"119-70 through 119-136",
  "billstatus_source_zip_sha":len(sources),"govinfo_law_sha":len(statutes),
  "S2_2026_budget_authority_usd_bn":"69.545",
  "S2_direct_spending_outlays_fy2026_to_fy2029_usd_bn":{str(y):str(Decimal(v)/1000) for y,v in years.items() if y<=2029},
  "S2_direct_outlays_2027_2029_sum_usd_bn":"53.433",
  "fy2026_joint_PL11974_75_budget_authority_vs_Feb_baseline_bn":"approximately 2",
  "CR_fy2027_annualized_BA_usd_bn":"1700.879",
  "CR_fy2027_annualized_outlays_usd_bn":"1869.190",
  "CR_not_actual_short_law_spending":True,
  "FY2027_2029_complete_policy_bridge":False,
  "gpo_source_SHA_verified":"--verify-gpo" in sys.argv,
  "cbo_pdf_bytes_verified":False,"h01_h10_political_causality":"UNTESTED"
},ensure_ascii=False,indent=2))
