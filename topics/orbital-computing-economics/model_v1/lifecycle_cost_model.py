#!/usr/bin/env python3
"""R2 orbital compute A/B cost ledgers with transparent scenario-only prices.

No prices in this prototype are supplier quotations. This model reconstructs
its own ground comparator; it does NOT relabel BCG's TCO as a comparable NPV.
"""
from __future__ import annotations
import argparse
import copy
import json
import math
from pathlib import Path
from orbital_cost_model import calculate_design


def numeric(v, label, *, low=0, allow_zero=False):
    if isinstance(v, bool) or not isinstance(v, (float, int)):
        raise ValueError(f"{label}: number required")
    if not math.isfinite(float(v)) or (float(v)<low if allow_zero else float(v)<=low):
        raise ValueError(f"{label}: out of bounds")
    return float(v)


def signed(v, label):
    if isinstance(v, bool) or not isinstance(v,(float,int)) or not math.isfinite(float(v)):
        raise ValueError(f"{label}: invalid number")
    return float(v)


def fraction(v, label, *, inclusive_zero=False):
    x = signed(v,label)
    if not ((0 <= x <= 1) if inclusive_zero else (0 < x <= 1)):
        raise ValueError(f"{label}: outside fraction range")
    return x


def run_case(kw, physics, cfg, p_perkg):
    kw = numeric(kw,"it_kw")
    p = numeric(p_perkg,"transport_usd_per_kg",allow_zero=True)
    y = int(numeric(cfg["horizon_years"], "horizon_years"))
    if y != float(cfg["horizon_years"]) or y > 50:
        raise ValueError("invalid horizon_years")
    r = numeric(cfg["real_discount_rate_per_year"],"discount_rate",allow_zero=True)
    if r>1:
        raise ValueError("discount_rate cannot exceed 1")
    a=cfg["scenario_prices"]
    fractional_fields = ("fraction_it_power_at_gpu_tdp","orbit_availability","ground_availability",
                         "compute_utilization","orbit_performance_retention_factor","ground_performance_retention_factor")
    for name in fractional_fields: fraction(a[name],name)
    for name in ("orbit_annual_partial_compute_replacement_fraction", "ground_annual_partial_compute_replacement_fraction", "orbit_annual_whole_module_loss_probability"):
        fraction(a[name],name,inclusive_zero=True)
    for name in ("orbit_refresh_period_years","ground_refresh_period_years"):
        raw=numeric(a[name],name)
        if raw!=int(raw): raise ValueError(f"{name}: integer years required")
    px=calculate_design(kw,physics)
    masses=px["mass_items_kg"]
    gpu_count=math.floor(kw*1000*fraction(a["fraction_it_power_at_gpu_tdp"],"gpu_fraction")/numeric(a["gpu_tdp_w"],"gpu_w"))
    if gpu_count<1: raise ValueError("GPU count is zero; lower scale needs alternate GPU accounting")
    cost_gpu=gpu_count*numeric(a["gpu_unit_price_usd"],"gpu_unit_price")
    compute_build=cost_gpu+kw*numeric(a["other_it_equipment_usd_per_kw"],"it_support_cost")
    orbital_build_items={
        "it_gpu_and_support":compute_build,
        "solar_array":masses["solar_array_kg"]*numeric(a["solar_array_manufacture_usd_per_kg"],"solar_price"),
        "battery_pack":masses["battery_pack_kg"]*numeric(a["battery_pack_manufacture_usd_per_kg"],"battery_price"),
        "radiator_system":masses["radiator_system_kg"]*numeric(a["radiator_system_manufacture_usd_per_kg"],"radiator_price"),
        "bus_shield_comms":masses["bus_comms_shield_kg"]*numeric(a["bus_shield_comms_manufacture_usd_per_kg"],"bus_price"),
        "orbital_integration":kw*numeric(a["orbit_integration_usd_per_kw"],"integration_price")
    }
    orbit_build=sum(orbital_build_items.values())
    refresh_mass=masses["compute_payload_kg"]
    total_mass=px["initial_operational_mass_kg"]
    assert total_mass>refresh_mass

    ground_initial_build=compute_build+kw*numeric(a["ground_build_usd_per_kw"],"ground_build")
    ground_annual_fixed=kw*numeric(a["ground_annual_opex_excl_power_usd_per_kw"],"ground_opex")
    # 1 kW continuous * 8760 h = 8760 kWh / calendar year.
    ground_electric_annual=kw*8760*numeric(a["ground_power_usage_effectiveness"],"ground_PUE")*numeric(a["ground_electricity_usd_per_kwh"],"electricity_usd_per_kwh")
    orbit_annual_fixed=kw*numeric(a["orbital_operations_usd_per_kw_year"],"orbit_opex")
    ground_partial=fraction(a["ground_annual_partial_compute_replacement_fraction"],"ground_partial",inclusive_zero=True)
    orbit_partial=fraction(a["orbit_annual_partial_compute_replacement_fraction"],"orbit_partial",inclusive_zero=True)
    whole_loss=fraction(a["orbit_annual_whole_module_loss_probability"],"whole_loss",inclusive_zero=True)
    # At t=0, initial capital/launch cash flow. End-of-year recurrent costs at t=1..T.
    flow=[]
    flow.append({"year":0,"orbital_A_transport_usd":total_mass*p,"orbital_B_build_ops_usd":orbit_build,
                 "ground_total_usd":ground_initial_build,"orbital_effective_gpu_h":0,"ground_effective_gpu_h":0,
                 "expected_new_launch_mass_kg":total_mass,"service_hours_discounted_at_zero":0})
    for year in range(1,y+1):
        periodic_o=compute_build if year<y and year%int(a["orbit_refresh_period_years"])==0 else 0
        periodic_g=compute_build if year<y and year%int(a["ground_refresh_period_years"])==0 else 0
        # Annual partial attrition (expectation). Full-module loss is a separate stress;
        # it is additive and does not reset a surviving cohort's periodic refresh clock.
        replace_o=compute_build*orbit_partial
        replace_g=compute_build*ground_partial
        failure_module_B=whole_loss*orbit_build
        failure_module_A=whole_loss*total_mass*p
        A=p*(refresh_mass*((1 if periodic_o else 0)+orbit_partial))+failure_module_A
        B=orbit_annual_fixed+periodic_o+replace_o+failure_module_B
        if year==y:
            B+=kw*numeric(a["orbital_deorbit_usd_per_kw_end"],"deorbit")
        ground=ground_annual_fixed+ground_electric_annual+periodic_g+replace_g
        if year==y:
            ground+=kw*numeric(a["ground_decommission_usd_per_kw_end"],"ground_decommission")
        effective_orb=gpu_count*8760*a["compute_utilization"]*a["orbit_availability"]*a["orbit_performance_retention_factor"]
        effective_ground=gpu_count*8760*a["compute_utilization"]*a["ground_availability"]*a["ground_performance_retention_factor"]
        flow.append({"year":year,"orbital_A_transport_usd":A,"orbital_B_build_ops_usd":B,"ground_total_usd":ground,
                     "orbital_effective_gpu_h":effective_orb,"ground_effective_gpu_h":effective_ground,
                     "expected_new_launch_mass_kg":refresh_mass*((1 if periodic_o else 0)+orbit_partial)+whole_loss*total_mass})
    def totals(k,discount):
        return sum(row[k]/((1+r)**row["year"] if discount else 1) for row in flow)
    def transport_mass(discount):
        return sum(row["expected_new_launch_mass_kg"]/((1+r)**row["year"] if discount else 1) for row in flow)
    a_nom=totals("orbital_A_transport_usd",False)
    b_nom=totals("orbital_B_build_ops_usd",False)
    g_nom=totals("ground_total_usd",False)
    a_pv=totals("orbital_A_transport_usd",True)
    b_pv=totals("orbital_B_build_ops_usd",True)
    g_pv=totals("ground_total_usd",True)
    mass_nom=transport_mass(False)
    mass_pv=transport_mass(True)
    assert math.isclose(a_nom,p*mass_nom,rel_tol=1e-10,abs_tol=1e-5)
    assert math.isclose(a_pv,p*mass_pv,rel_tol=1e-10,abs_tol=1e-5)
    hours_o=totals("orbital_effective_gpu_h",True)
    hours_g=totals("ground_effective_gpu_h",True)
    # Distinguish total-cost parity from levelized service-cost parity.
    nominal_breakeven=(g_nom-b_nom)/mass_nom
    pv_breakeven=(g_pv-b_pv)/mass_pv
    # Comparison uses delivered GPU-hours normalized for availability and performance.
    leveled_breakeven=((g_pv/hours_g)*hours_o-b_pv)/mass_pv
    return {
        "it_kw":kw, "gpu_count_assumed":gpu_count,
        "initial_operational_mass_kg_R1":total_mass,
        "periodic_compute_refresh_mass_kg":refresh_mass,
        "transport_usd_per_kg_scenario":p,
        "orbital_B_initial_build_item_costs_usd":orbital_build_items,
        "orbital_A_20y_undiscounted_usd":a_nom,
        "orbital_B_20y_undiscounted_usd":b_nom,
        "orbital_20y_total_undiscounted_usd":a_nom+b_nom,
        "ground_20y_total_undiscounted_usd":g_nom,
        "orbital_A_20y_real_pv_usd":a_pv,
        "orbital_B_20y_real_pv_usd":b_pv,
        "orbital_20y_total_real_pv_usd":a_pv+b_pv,
        "ground_20y_total_real_pv_usd":g_pv,
        "orbital_discounted_effective_gpu_h":hours_o,
        "ground_discounted_effective_gpu_h":hours_g,
        "orbital_levelized_usd_per_effective_gpu_h":(a_pv+b_pv)/hours_o,
        "ground_levelized_usd_per_effective_gpu_h":g_pv/hours_g,
        "cost_ratio_nominal_orbit_to_ground":(a_nom+b_nom)/g_nom,
        "cost_ratio_levelized_orbit_to_ground":((a_pv+b_pv)/hours_o)/(g_pv/hours_g),
        "total_expected_launch_mass_kg_20y_nominal":mass_nom,
        "total_expected_launch_mass_kg_20y_discounted":mass_pv,
        "break_even_transport_usd_per_kg_for_nominal_20y_cost_parity":nominal_breakeven,
        "break_even_transport_usd_per_kg_for_real_pv_cost_parity":pv_breakeven,
        "break_even_transport_usd_per_kg_for_levelized_GPU_hour_parity":leveled_breakeven,
        "break_even_feasible_at_nonnegative_transport_price":leveled_breakeven>=0,
        "yearly_cashflows":flow
    }


def run_all(physics_input, lifecycle_input):
    if lifecycle_input["base_physics_inputs_file"]!="inputs.json":
        raise ValueError("unexpected linked R1 inputs file")
    output={"schema_version":"0.2.0",
            "status":"HYPOTHETICAL_PRICES_AND_RELIABILITY_NO_OBSERVED_VENDOR_CONTRACT",
            "provenance":lifecycle_input["provenance"],
            "cases":[]}
    for kw in lifecycle_input["it_kw_scales"]:
        for scenario_name,mod in lifecycle_input["what_if_modifiers"].items():
            c=copy.deepcopy(lifecycle_input)
            c["scenario_prices"].update(mod)
            for p in lifecycle_input["transport_usd_per_operational_kg_scenarios"]:
                o=run_case(kw, physics_input["design"], c, p)
                o["scenario_name"]=scenario_name
                output["cases"].append(o)
    return output


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--physics",type=Path,default=Path(__file__).parent/"inputs.json")
    parser.add_argument("--inputs",type=Path,default=Path(__file__).parent/"inputs_lifecycle.json")
    parser.add_argument("--output",type=Path,default=Path(__file__).parent/"results_lifecycle.json")
    args=parser.parse_args()
    root=json.loads(args.physics.read_text(encoding="utf-8"))
    inp=json.loads(args.inputs.read_text(encoding="utf-8"))
    out=run_all(root,inp)
    args.output.write_text(json.dumps(out,ensure_ascii=False,indent=2,allow_nan=False)+"\n",encoding="utf-8")
    print(f"Wrote {args.output} cases={len(out['cases'])}")
    for c in out["cases"]:
        if c["it_kw"]==1000 and c["transport_usd_per_kg_scenario"] in (1500,100) and c["scenario_name"] in ("baseline","lower_space_manufacturing","refresh_every_6_years"):
            print(f"{c['scenario_name']:28} p={c['transport_usd_per_kg_scenario']:<5} nominal orbit={c['orbital_20y_total_undiscounted_usd']/1e6:.1f}m ground={c['ground_20y_total_undiscounted_usd']/1e6:.1f}m, threshold levelized={c['break_even_transport_usd_per_kg_for_levelized_GPU_hour_parity']:.2f} USD/kg")

if __name__=="__main__":main()