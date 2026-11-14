#!/usr/bin/env python3
"""R3 orbital eclipse and maintenance-dispatch scenario model, not quotes."""
from __future__ import annotations
import argparse
import copy
import json
import math
from pathlib import Path
from orbital_cost_model import calculate_design
from lifecycle_cost_model import run_case

def scalar(v, name, min_value=0.0):
    if isinstance(v, bool) or not isinstance(v,(int,float)) or not math.isfinite(float(v)) or float(v)<=min_value:
        raise ValueError(f"{name}: invalid positive scalar")
    return float(v)

def eclipse_fraction(altitude_km, beta_degrees, earth_radius_km=6371.0):
    """Cylindrical umbra, circular orbit, beta=Sun-orbit-plane angle."""
    alt=scalar(altitude_km,"altitude")
    R=scalar(earth_radius_km,"earth_radius")
    if isinstance(beta_degrees,bool) or not isinstance(beta_degrees,(float,int)) or not math.isfinite(beta_degrees) or abs(beta_degrees)>90:
        raise ValueError("beta not in [-90,90]")
    r=R+alt
    crit=math.asin(R/r)
    b=abs(math.radians(beta_degrees))
    if b>=crit:return 0.0
    x=math.sqrt(1-(R/r)**2)/math.cos(b)
    return math.acos(min(1,max(-1,x)))/math.pi

def circular_period_hours(altitude_km, earth_radius_km=6371.0, mu_km3_s2=398600.4418):
    alt=scalar(altitude_km,"altitude")
    R=scalar(earth_radius_km,"earth radius")
    mu=scalar(mu_km3_s2,"gravitational parameter")
    return 2*math.pi*math.sqrt((R+alt)**3/mu)/3600

def orbit_physics_case(kw,beta_deg,base_design,settings):
    period=circular_period_hours(settings["altitude_km"],settings["earth_radius_km"],settings["earth_mu_km3_s2"])
    fraction=eclipse_fraction(settings["altitude_km"],beta_deg,settings["earth_radius_km"])
    d=copy.deepcopy(base_design)
    d["orbit_period_hours"]=period
    d["eclipse_fraction"]=fraction
    return {"beta_deg":beta_deg,"orbit_period_h":period,"eclipse_fraction":fraction,
            "eclipse_minutes":fraction*period*60,"design":calculate_design(kw,d)}

def finance_schedule(kw,physical,lifecycle,settings,delivery,repair_policy):
    """Two alternative maintenance policies; failed electronics are expected fractions.
    Service robots, ground transfer, volume packing and whole-module loss are NOT priced.
    """
    if repair_policy not in ("annual_repair","four_year_refresh_only"):raise ValueError("unknown repair policy")
    h=scalar(settings["analysis_horizon_years"],"horizon")
    refresh=scalar(settings["hardware_refresh_period_years"],"refresh")
    if int(h)!=h or int(refresh)!=refresh or h>100:raise ValueError("noninteger horizon/refresh")
    h,refresh=int(h),int(refresh)
    f=settings["partial_compute_failure_fraction_per_year_assumed"]
    r=settings["real_discount_rate"]
    if isinstance(f,bool) or not isinstance(f,(int,float)) or not 0<=f<1:raise ValueError("failure rate")
    if isinstance(r,bool) or not isinstance(r,(int,float)) or not 0<=r<=1:raise ValueError("discount")
    p=lifecycle["scenario_prices"]
    mass=physical["mass_items_kg"]
    it_mass=mass["compute_payload_kg"]
    gpu_count=math.floor(kw*1000*p["fraction_it_power_at_gpu_tdp"]/p["gpu_tdp_w"])
    if gpu_count<1:raise ValueError("zero GPU count")
    compute_build=gpu_count*p["gpu_unit_price_usd"]+kw*p["other_it_equipment_usd_per_kw"]
    build_items={
        "it_gpu_and_support":compute_build,
        "solar_array":mass["solar_array_kg"]*p["solar_array_manufacture_usd_per_kg"],
        "battery_pack":mass["battery_pack_kg"]*p["battery_pack_manufacture_usd_per_kg"],
        "radiator_system":mass["radiator_system_kg"]*p["radiator_system_manufacture_usd_per_kg"],
        "bus_shield_comms":mass["bus_comms_shield_kg"]*p["bus_shield_comms_manufacture_usd_per_kg"],
        "orbital_integration":kw*p["orbit_integration_usd_per_kw"]}
    def fee(kg):
        if kg<=1e-12:return 0,0.0
        if delivery["kind"]=="proportional":
            return 0,kg*scalar(delivery["usd_per_kg"],"delivery unit price")
        if delivery["kind"]=="dedicated":
            n=math.ceil(kg/scalar(delivery["payload_capacity_kg"],"launch capacity"))
            return n,n*scalar(delivery["flight_price_usd"],"flight fee")
        raise ValueError("bad delivery type")
    rows=[]
    flights=0
    for year in range(h+1):
        if year==0:
            kg=physical["initial_operational_mass_kg"]
            B=sum(build_items.values())
            hours=0.0
            category="initial_deployment"
        else:
            scheduled=year<h and year%refresh==0
            if repair_policy=="annual_repair":
                repair_mass=it_mass*f if year<h and not scheduled else 0.0
                survival=(1-f)**0.5
            else:
                repair_mass=0.0
                survival=(1-f)**(((year-1)%refresh)+0.5)
            kg=(it_mass if scheduled else 0)+repair_mass
            B=kw*p["orbital_operations_usd_per_kw_year"]
            B+=compute_build if scheduled else 0
            B+=compute_build*repair_mass/it_mass
            if year==h:B+=kw*p["orbital_deorbit_usd_per_kw_end"]
            hours=gpu_count*8760*p["compute_utilization"]*p["orbit_availability"]*p["orbit_performance_retention_factor"]*survival
            category="refresh" if scheduled else ("partial_repair" if repair_mass else "operations")
        count,A=fee(kg)
        flights+=count
        rows.append({"year":year,"category":category,"delivered_kg":kg,
                     "launch_count_if_dedicated":count,"A_transport_usd":A,
                     "B_build_ops_usd":B,"effective_gpu_h":hours})
    pv=lambda key:sum(x[key]/(1+r)**x["year"] for x in rows)
    A,B,H=pv("A_transport_usd"),pv("B_build_ops_usd"),pv("effective_gpu_h")
    return {"it_kw":kw,"beta_deg":physical["beta_deg"],"repair_policy":repair_policy,
      "pricing_name":delivery["name"],"pricing_kind":delivery["kind"],
      "initial_mass_kg":rows[0]["delivered_kg"],"total_delivered_mass_kg":sum(x["delivered_kg"] for x in rows),
      "delivery_campaigns":sum(x["delivered_kg"]>1e-10 for x in rows),
      "dedicated_flights_lower_bound":flights if delivery["kind"]=="dedicated" else None,
      "A_transport_PV_usd":A,"B_build_operations_PV_usd":B,"total_PV_usd":A+B,
      "discounted_effective_gpu_h":H,"levelized_usd_per_effective_gpu_h":(A+B)/H,
      "initial_B_items_usd":build_items,"flows":rows}

def run_all(physics,lifecycle,settings):
    phys=[orbit_physics_case(kw,beta,physics["design"],settings)
          for kw in settings["compute_it_kw"] for beta in settings["beta_angles_deg"]]
    cases=[]
    for kw in settings["compute_it_kw"]:
        sample=next(x for x in phys if x["design"]["it_kw"]==kw and x["beta_deg"]==settings["target_beta_deg_for_logistics"])
        selected={**sample["design"],"beta_deg":sample["beta_deg"]}
        ground=run_case(kw,physics["design"],lifecycle,0)["ground_levelized_usd_per_effective_gpu_h"]
        for policy in settings["repair_policies"]:
            for cost in settings["pricing_cases"]:
                item=finance_schedule(kw,selected,lifecycle,settings,cost,policy)
                item["ground_levelized_usd_per_effective_gpu_h"]=ground
                item["levelized_ratio_to_ground"]=item["levelized_usd_per_effective_gpu_h"]/ground
                cases.append(item)
    return {"schema_version":settings["schema_version"],"status":"GEOMETRY_AND_ASSUMED_COSTS_NO_REAL_550KM_CONTRACT",
            "orbit_cases":phys,"logistics_cases":cases,"sources":settings["sources"]}

def main():
    q=argparse.ArgumentParser()
    q.add_argument("--physics",type=Path,default=Path(__file__).with_name("inputs.json"))
    q.add_argument("--life",type=Path,default=Path(__file__).with_name("inputs_lifecycle.json"))
    q.add_argument("--config",type=Path,default=Path(__file__).with_name("inputs_logistics.json"))
    q.add_argument("--output",type=Path,default=Path(__file__).with_name("results_logistics.json"))
    args=q.parse_args()
    root=json.loads(args.physics.read_text(encoding="utf-8"))
    life=json.loads(args.life.read_text(encoding="utf-8"))
    cfg=json.loads(args.config.read_text(encoding="utf-8"))
    result=run_all(root,life,cfg)
    args.output.write_text(json.dumps(result,ensure_ascii=False,indent=2,allow_nan=False)+"\n",encoding="utf-8")
    print("Computed",len(result["orbit_cases"]),"orbit cases and",len(result["logistics_cases"]),"logistics cases")
    for c in result["logistics_cases"]:
        if c["it_kw"]==1000 and c["pricing_kind"]=="dedicated":
            print(c["repair_policy"],"flights",c["dedicated_flights_lower_bound"],"USD/GPU-h",round(c["levelized_usd_per_effective_gpu_h"],3))
if __name__=="__main__":main()
