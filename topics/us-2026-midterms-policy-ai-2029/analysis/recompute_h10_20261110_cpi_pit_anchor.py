#!/usr/bin/env python3
"""Verify dated November 10 2026 CPI surprise, rate and FedWatch reportage.

Data: TOPIC-011/data/h10_20261110_cpi_consensus_fedwatch_rate_event.csv
Statistical strength: ONE event, not a market impact causal estimator.
Historical forecast index snapshots are NOT used as CPI consensus data.
"""
import csv,io,sys,json
from decimal import Decimal
from pathlib import Path

def verify():
 p=Path(__file__).resolve().parent.parent/"data"/"h10_20261110_cpi_consensus_fedwatch_rate_event.csv"
 raw=sys.stdin.read() if "--stdin-csv" in sys.argv else p.read_text(encoding="utf8")
 rows={r["obs_id"]:r for r in csv.DictReader(io.StringIO(raw))}
 assert set(rows)=={f"CPI26-{i:02d}" for i in range(1,16)},list(rows)
 n=lambda i,field:Decimal(rows[f"CPI26-{i:02d}"][field])
 assert rows["CPI26-01"]["stage"]=="PRE_RELEASE_CONSENSUS"
 assert rows["CPI26-01"]["source_publication_time"].startswith("2026-11-09")
 assert rows["CPI26-03"]["stage"]=="RELEASE_ACTUAL"
 assert rows["CPI26-03"]["source_publication_time"].startswith("2026-11-10T08:30")
 headline=n(3,"reported_actual")-n(1,"reported_forecast_or_probability")
 core=n(4,"reported_actual")-n(2,"reported_forecast_or_probability")
 assert headline==Decimal("0.1") and core==Decimal("0.1")
 prior25=n(5,"reported_forecast_or_probability")
 post25=n(6,"reported_forecast_or_probability")
 post50=n(7,"reported_forecast_or_probability")
 two=(n(9,"reported_actual")-n(8,"reported_actual"))*100
 ten=(n(11,"reported_actual")-n(10,"reported_actual"))*100
 assert (two,ten)==(Decimal("17.00"),Decimal("10.00"))
 assert post25+post50==100
 assert post25-prior25==Decimal("6.5")
 assert rows["CPI26-12"]["seasonality"]=="SA"
 assert rows["CPI26-13"]["seasonality"]=="NSA"
 assert n(12,"reported_actual")==n(14,"reported_actual")==Decimal("337.476")
 assert abs(n(13,"reported_actual")-n(15,"reported_actual"))<Decimal("0.05")
 assert n(12,"reported_actual")-n(12,"reported_forecast_or_probability")==Decimal("-1.207")
 assert n(13,"reported_actual")-n(13,"reported_forecast_or_probability")==Decimal("0.5")
 assert rows["CPI26-12"]["source_asof_assessment"]=="PIT_UNVERIFIED"
 assert rows["CPI26-13"]["source_asof_assessment"]=="PIT_UNVERIFIED"
 return {
   "validation":"PASS",
   "event_date":"2026-11-10",
   "headline_cpi_surprise_pp":str(headline),
   "core_cpi_surprise_pp":str(core),
   "two_year_treasury_full_day_change_bp":str(two),
   "ten_year_treasury_full_day_change_bp":str(ten),
   "reported_monday_25bp_hike_probability_pct":str(prior25),
   "reported_tuesday_25bp_hike_probability_pct":str(post25),
   "reported_tuesday_50bp_hike_probability_pct":str(post50),
   "reported_25bp_outcome_probability_change_pp":str(post25-prior25),
   "official_sa_cpi_index":str(n(14,"reported_actual")),
   "official_nsa_cpi_index":str(n(15,"reported_actual")),
   "vendor_sa_index_actual_minus_unverified_forecast":str(n(12,"reported_actual")-n(12,"reported_forecast_or_probability")),
   "vendor_nsa_rounded_actual_minus_unverified_forecast":str(n(13,"reported_actual")-n(13,"reported_forecast_or_probability")),
   "vendor_forecast_status":"NO_PRE_RELEASE_TIMESTAMP; DIFFERENT_SA_VS_NSA DEFINITIONS; BOTH EXCLUDED FROM REAL CPI_SURPRISE",
   "causal_limit":"Cboe next-day/article same-day quotes are not timestamped intra-day or exact FedWatch market snapshots; UST daily movement includes other news; one event does not demonstrate CPI causes Fed policy"
 }

if __name__=="__main__":
 print(json.dumps(verify(),ensure_ascii=False,indent=2))
