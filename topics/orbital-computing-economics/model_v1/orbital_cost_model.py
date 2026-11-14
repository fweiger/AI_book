#!/usr/bin/env python3
"""TOPIC-012 first-order orbital mass + launch cost scenario model.

This is an illustrative model, not a space-qualified design or commercial
quote. Every non-public parameter is explicitly scenario-labelled in inputs.json.
"""
from __future__ import annotations
import argparse
import json
import math
from pathlib import Path

SIGMA = 5.670374419e-8

def positive(value, name):
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise ValueError(f"{name}: expected a number")
    value = float(value)
    if not math.isfinite(value) or value <= 0:
        raise ValueError(f"{name}: must be finite and > 0")
    return value

def fraction(value, name, allow_zero=False):
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise ValueError(f"{name}: expected a number")
    value = float(value)
    valid = (0 <= value < 1) if allow_zero else (0 < value <= 1)
    if not math.isfinite(value) or not valid:
        raise ValueError(f"{name}: invalid fraction")
    return value

def calculate_design(it_kw, d):
    it_kw = positive(it_kw, "it_kw")
    overhead = positive(d["power_overhead_factor"], "power_overhead")
    if overhead < 1:
        raise ValueError("power_overhead_factor must be >= 1")
    eclipse = fraction(d["eclipse_fraction"], "eclipse", allow_zero=True)
    orbit_hours = positive(d["orbit_period_hours"], "orbit_hours")
    eol = fraction(d["solar_pv_eol_factor"], "solar_eol")
    roundtrip = fraction(d["charge_discharge_roundtrip_efficiency"], "roundtrip")
    solar_wkg = positive(d["solar_array_specific_power_w_per_kg"], "solar_wkg")
    batt_whkg = positive(d["battery_pack_specific_energy_wh_per_kg"], "battery_whkg")
    dod = fraction(d["battery_max_depth_of_discharge"], "battery_dod")
    dis_eff = fraction(d["battery_discharge_efficiency"], "discharge_eff")
    temp = positive(d["radiator_temperature_kelvin"], "radiator_temperature")
    if not 150 <= temp <= 600:
        raise ValueError("radiator temperature outside conservative guardrails")
    emissivity = fraction(d["radiator_emissivity"], "emissivity")
    view_factor = fraction(d["radiator_effective_view_factor"], "view_factor")
    radiator_floor = positive(d["radiator_area_floor_m2_per_100kw_it"], "radiator_floor")
    radiator_kgm2 = positive(d["radiator_system_specific_mass_kg_per_m2"], "radiator_kgm2")
    compute_kgkw = positive(d["compute_specific_mass_kg_per_kw_it"], "compute_kgkw")
    bus_kg100kw = positive(d["bus_comms_shield_mass_kg_per_100kw_it"], "bus_kg100kw")

    electrical_kw = it_kw * overhead
    solar_sun_kw = electrical_kw * (1 + eclipse / ((1 - eclipse) * roundtrip))
    rated_solar_kw = solar_sun_kw / eol
    pv_mass_kg = 1000 * rated_solar_kw / solar_wkg
    eclipse_kwh = electrical_kw * eclipse * orbit_hours
    battery_mass_kg = 1000 * eclipse_kwh / (batt_whkg * dod * dis_eff)
    # First-order radiative heat only; external solar/earth heat not resolved.
    ideal_area_m2 = electrical_kw * 1000 / (SIGMA * temp**4 * emissivity * view_factor)
    area_m2 = max(ideal_area_m2, radiator_floor * it_kw / 100)
    masses = {
        "solar_array_kg": pv_mass_kg,
        "battery_pack_kg": battery_mass_kg,
        "radiator_system_kg": area_m2 * radiator_kgm2,
        "compute_payload_kg": it_kw * compute_kgkw,
        "bus_comms_shield_kg": bus_kg100kw * it_kw / 100,
    }
    total_mass = sum(masses.values())
    energy_in = solar_sun_kw * (1 - eclipse)
    required = electrical_kw * ((1 - eclipse) + eclipse / roundtrip)
    if not math.isclose(energy_in, required, rel_tol=1e-12):
        raise ArithmeticError("electricity balance failed")
    if area_m2 * SIGMA * temp**4 * emissivity * view_factor < electrical_kw * 1000 * (1 - 1e-12):
        raise ArithmeticError("radiative balance failed")
    return {
        "it_kw": it_kw,
        "total_electrical_load_kw": electrical_kw,
        "peak_solar_generation_during_sun_kw": solar_sun_kw,
        "rated_solar_peak_kw": rated_solar_kw,
        "eclipse_energy_kwh": eclipse_kwh,
        "radiator_ideal_area_m2": ideal_area_m2,
        "radiator_model_area_m2": area_m2,
        "mass_items_kg": masses,
        "initial_operational_mass_kg": total_mass,
        "specific_mass_kg_per_mw_it": total_mass / (it_kw / 1000),
        "power_balance_residual_kw": energy_in - required,
    }

def run(inputs):
    d = inputs["design"]
    m = inputs["market"]
    ground = positive(m["ground_20y_tco_reference_usd_per_mw"], "ground_tco")
    orbital = positive(m["bcg_orbit_20y_tco_reference_usd_per_mw"], "orbit_tco")
    share = fraction(m["bcg_launch_share_reference"], "launch_share")
    flight_price = positive(m["future_dedicated_flight_usd"], "future_flight_price")
    flight_capacity = positive(m["future_dedicated_effective_mass_kg_per_flight"], "future_flight_capacity")
    cases = []
    for kw in d["it_load_kw"]:
        c = calculate_design(kw, d)
        f = c["it_kw"] / 1000
        mass = c["initial_operational_mass_kg"]
        c["launch_cost_scenarios"] = []
        for price_raw in m["proportional_delivery_price_usd_per_kg_scenarios"]:
            price = positive(price_raw, "launch_price_per_kg")
            c["launch_cost_scenarios"].append({
                "usd_per_kg_assumption": price,
                "initial_transport_cost_usd": mass * price,
                "20y_nontransport_tco_headroom_usd_before_replacement": ground * f - mass * price,
                "cost_type": "hypothetical_proportional_transport_only",
            })
        flights = math.ceil(mass / flight_capacity)
        c["dedicated_launch_scenario"] = {
            "assumed_flight_price_usd": flight_price,
            "assumed_effective_mass_capacity_kg": flight_capacity,
            "minimum_flights_by_mass": flights,
            "initial_launch_fees_usd": flights * flight_price,
            "effective_usd_per_operational_kg": flights * flight_price / mass,
            "20y_nontransport_tco_headroom_usd_before_replacement": ground * f - flights * flight_price,
            "warning": "mass-only lower bound; no volume, trajectory, assembly, replacements",
        }
        cases.append(c)
    return {
        "schema_version": inputs["schema_version"],
        "model_status": "SCENARIO_CALCULATED_NOT_A_QUALIFIED_ENGINEERING_DESIGN",
        "physical_cases": cases,
        "bcg_anchored_cost_floor_sensitivity": {
            "orbital_reference_tco_usd_per_mw": orbital,
            "ground_reference_tco_usd_per_mw": ground,
            "baseline_transport_component_usd_per_mw": orbital * share,
            "baseline_nontransport_component_usd_per_mw": orbital * (1 - share),
            "orbital_tco_if_transport_cost_reduced_90pct_usd_per_mw": orbital * (1 - share * .9),
            "ratio_to_ground_after_90pct_transport_reduction": orbital * (1 - share * .9) / ground,
            "cost_gap_even_if_transport_zero_usd_per_mw": orbital * (1 - share) - ground,
            "warning": "BCG static sensitivity, not an independent full TCO reconstruction",
        },
        "provenance": inputs.get("provenance", {}),
    }

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--inputs", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    result = run(json.loads(args.inputs.read_text(encoding="utf-8")))
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2, allow_nan=False) + "\n", encoding="utf-8")
    print(f"Wrote {args.output}, cases={len(result['physical_cases'])}")
    for c in result["physical_cases"]:
        print(f"{c['it_kw']:.0f} kW: {c['initial_operational_mass_kg']:.1f} kg, "
              f"PV={c['mass_items_kg']['solar_array_kg']:.1f} kg, "
              f"radiator={c['radiator_model_area_m2']:.1f} m2, "
              f"minimum dedicated launches={c['dedicated_launch_scenario']['minimum_flights_by_mass']}")

if __name__ == "__main__":
    main()
