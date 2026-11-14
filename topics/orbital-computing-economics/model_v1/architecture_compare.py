#!/usr/bin/env python3
"""TOPIC-012 R4: LEO hub servicing vs replaceable satellite constellation.

All prices, hazards, and future transport products are what-if assumptions.
The observed servicing missions are NOT used as engineering qualification.
The model uses an exact binomial probability for at-least-one failures per
service window (rather than treating a fractional expected failure as a
certain dedicated launch). Hardware refresh is separate from partial failure.
"""
from __future__ import annotations
import argparse
import json
import math
from pathlib import Path


def check(config: dict) -> None:
    for k in ("it_kw", "nodes", "horizon_years", "refresh_years"):
        x=config[k]
        if isinstance(x,bool) or not isinstance(x,int) or x<=0: raise ValueError(f"{k} must be a positive integer")
    if config["it_kw"]!=1000 or config["nodes"]!=10: raise ValueError("R4 prototype supports documented 1MW/10 nodes only")
    if config["horizon_years"]%config["refresh_years"]: raise ValueError("horizon must contain integral refresh blocks")
    for k in ("discount_rate","node_failure_hazard_per_year","shared_site_loss_probability_per_year"):
        x=config[k]
        if isinstance(x,bool) or not isinstance(x,(int,float)) or not math.isfinite(x) or x<0 or (k!="node_failure_hazard_per_year" and x>=1):raise ValueError(f"{k} invalid")
    for k in ("initial_orbital_mass_kg","compute_payload_mass_kg","base_manufacture_usd","compute_manufacture_usd","robot_capex_usd","robot_mass_kg","robot_annual_ops_usd","robot_visit_fee_usd","fleet_extra_unit_capex_usd","fleet_extra_annual_ops_usd","hub_annual_ops_usd","base_gpu_hours_per_year","usable_orbit_factor","ground_usd_per_effective_gpu_hour"):
        x=config[k]
        if isinstance(x,bool) or not isinstance(x,(int,float)) or not math.isfinite(x) or x<0:raise ValueError(f"{k} invalid")
    if config['compute_payload_mass_kg']>config['initial_orbital_mass_kg'] or config['compute_manufacture_usd']>config['base_manufacture_usd']:raise ValueError("component exceeds total")
    if config['usable_orbit_factor']>1 or config['usable_orbit_factor']==0:raise ValueError('usable_orbit_factor must be (0,1]')
    for name,v in config['transport'].items():
        if v['kind']=='proportional':
            if v['usd_per_kg']<0:raise ValueError(name)
        elif v['kind']=='dedicated':
            if v['flight_usd']<0 or v['capacity_kg']<=config['initial_orbital_mass_kg']+config['robot_mass_kg']:raise ValueError(name)
        else:raise ValueError('bad transport kind')


def avg_survival(hazard:float, start_age_years:int, duration_years:float=1.0) -> float:
    if hazard==0:return 1.0
    return math.exp(-hazard*start_age_years)*(-math.expm1(-hazard*duration_years))/(hazard*duration_years)


def p_dispatch(nodes:int, hazard:float, window_years:float=1.0) -> float:
    """Probability >=1 failed node, independent exponential hazards."""
    return -math.expm1(-nodes*hazard*window_years)


def case(config, architecture, policy, transport_name):
    check(config)
    if architecture not in ("serviceable_hub","replaceable_fleet"):raise ValueError('architecture')
    if policy not in ("annual","four_year_only"):raise ValueError('policy')
    t=config['transport'][transport_name]
    N=config['nodes']; lam=config['node_failure_hazard_per_year']; r=config['discount_rate'];
    yrs=config['horizon_years']; ref=config['refresh_years']; kg=config['initial_orbital_mass_kg'];
    itkg=config['compute_payload_mass_kg']; capex=config['base_manufacture_usd']; itcapex=config['compute_manufacture_usd'];
    robot=config['robot_capex_usd'] if architecture=='serviceable_hub' else 0
    robotmass=config['robot_mass_kg'] if architecture=='serviceable_hub' else 0
    fleetextra=N*config['fleet_extra_unit_capex_usd'] if architecture=='replaceable_fleet' else 0
    annual_ops=config['hub_annual_ops_usd'] if architecture=='serviceable_hub' else config['hub_annual_ops_usd']+config['fleet_extra_annual_ops_usd']
    if architecture=='serviceable_hub':annual_ops+=config['robot_annual_ops_usd']

    def shipment(expected_kg,prob_nonempty):
        if t['kind']=='proportional': return expected_kg*t['usd_per_kg'], None
        # The delivery is one dedicated flight when any failure occurs, not one per fractional expected node.
        # If shipment could exceed capacity this proxy is invalid and must be rejected.
        if expected_kg > t['capacity_kg'] + 1e-9:raise ValueError("capacity exceeded")
        return prob_nonempty*t['flight_usd'], prob_nonempty
    rows=[]
    initial_mass=kg+robotmass if architecture=='serviceable_hub' else kg
    initial_a,flights=shipment(initial_mass,1)
    initial_b=capex+robot+fleetextra
    rows.append({'year':0,'kind':'initial','expected_kg':initial_mass,'expected_dedicated_launches':flights,'A':initial_a,'B':initial_b,'effective_gpu_h':0})
    for year in range(1,yrs+1):
        refresh=year<yrs and year%ref==0
        is_repair=policy=='annual' and not refresh and year<yrs
        at_age=(year-1)%ref if policy=='four_year_only' else 0
        surv=avg_survival(lam,at_age)
        hours=config['base_gpu_hours_per_year']*config['usable_orbit_factor']*surv
        expected_failure_nodes=N*(-math.expm1(-lam)) if is_repair else 0
        fail_prob=p_dispatch(N,lam) if is_repair else 0
        if architecture=='serviceable_hub':
            if refresh: expected_kg=itkg; hardware_cost=itcapex; prob=1
            elif is_repair: expected_kg=itkg*expected_failure_nodes/N; hardware_cost=itcapex*expected_failure_nodes/N;prob=fail_prob
            else:expected_kg=hardware_cost=prob=0
            visit_fee=config['robot_visit_fee_usd']*(1 if refresh else fail_prob) if (refresh or is_repair) else 0
            B=annual_ops+hardware_cost+visit_fee
        else:
            if refresh: expected_kg=kg; hardware_cost=capex+fleetextra;prob=1
            elif is_repair: expected_kg=kg*expected_failure_nodes/N;hardware_cost=(capex+fleetextra)*expected_failure_nodes/N;prob=fail_prob
            else: expected_kg=hardware_cost=prob=0
            B=annual_ops+hardware_cost
        A,flight=shipment(expected_kg,prob)
        rows.append({'year':year,'kind':'refresh' if refresh else 'repair' if is_repair else 'operations',
                     'expected_kg':expected_kg,'expected_dedicated_launches':flight,'A':A,'B':B,'effective_gpu_h':hours})
    PV=lambda key:sum(z[key]/(1+r)**z['year'] for z in rows)
    if t['kind']=='dedicated':launches=sum(z['expected_dedicated_launches'] or 0 for z in rows)
    else:launches=None
    A=PV('A');B=PV('B');H=PV('effective_gpu_h')
    return {'architecture':architecture,'policy':policy,'transport':transport_name,
            'cost_A_pv_usd':A,'cost_B_pv_usd':B,'total_pv_usd':A+B,'discounted_effective_gpu_h':H,
            'levelized_usd_per_gpu_hour':(A+B)/H,
            'ratio_to_assumed_ground':((A+B)/H)/config['ground_usd_per_effective_gpu_hour'],
            'total_expected_delivery_mass_kg':sum(z['expected_kg'] for z in rows),
            'expected_dedicated_launches':launches,
            'prob_at_least_one_node_failure_in_year':p_dispatch(N,lam),
            'shared_failure_tail_prob_hub':config['shared_site_loss_probability_per_year'] if architecture=='serviceable_hub' else None,
            'prob_all_fleet_nodes_fail_independent':(1-math.exp(-lam))**N if architecture=='replaceable_fleet' else None,
            'rows':rows}


def run(config):
    all_cases=[case(config,a,p,t) for a in ('serviceable_hub','replaceable_fleet') for p in ('annual','four_year_only') for t in config['transport']]
    return {'status':'ILLUSTRATIVE_SCENARIOS_NOT_VENDOR_QUOTE_NOT_LUNAR_OR_GEO_SERVICE_PROOF',
            'key_probabilities':{'per_node_annual_failure':1-math.exp(-config['node_failure_hazard_per_year']),
               'p_one_or_more_of_10_fail_in_a_year':p_dispatch(config['nodes'],config['node_failure_hazard_per_year'])},
            'cases':all_cases,'provenance':config['provenance']}


def main():
    ap=argparse.ArgumentParser();ap.add_argument('--config',type=Path,required=True);ap.add_argument('--output',type=Path,required=True)
    arg=ap.parse_args();cfg=json.loads(arg.config.read_text(encoding='utf-8'));data=run(cfg)
    arg.output.parent.mkdir(exist_ok=True,parents=True);arg.output.write_text(json.dumps(data,indent=2,ensure_ascii=False,allow_nan=False)+'\n')
    for x in data['cases']:
        print(f"{x['architecture']:18} {x['policy']:14} {x['transport']:20} ${x['levelized_usd_per_gpu_hour']:.2f}/GPUh, A=${x['cost_A_pv_usd']/1e6:.1f}M, B=${x['cost_B_pv_usd']/1e6:.1f}M, flights={x['expected_dedicated_launches']}")
if __name__=='__main__':main()