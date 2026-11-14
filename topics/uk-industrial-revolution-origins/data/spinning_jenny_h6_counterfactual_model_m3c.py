#!/usr/bin/env python3
# Reproducible 1780 spinning-jenny thought experiment; no dependencies or internet.
# Crafts 2010 (Warwick) Table 1: https://wrap.warwick.ac.uk/44710/
# Gragnolati, Moschella, Pugliese 2011 Table 2:
# https://doi.org/10.1017/S0022050711001604
# Source rows below are author's *assumptions/model outputs*, not actual company IRRs.
from __future__ import annotations
import argparse, csv
from pathlib import Path

PUBLISHED = [
 (2,.3,12.3,-21.7,44.6,6.8), (2,.4,24,-8.2,63.9,17.9),
 (2,.5,34.6,.2,82.8,27.5), (3,.3,24,-8.2,101.5,36.5),
 (3,.4,38,2.5,138.8,53.5), (3,.5,51.2,10.7,176,70),
 (4,.3,29.4,-3.7,157.4,61.8),(4,.4,44.7,6.8,213.2,86.2),
 (4,.5,59.2,15.3,269,110.2)]
SOURCE = 'https://doi.org/10.1017/S0022050711001604'

def annuity(r: float) -> float:
    if r <= -1: raise ValueError('r must exceed -1')
    return sum((1+r)**(-t) for t in range(1,11))

def irr(w:float,k:float,p:float,d:float,scenario:str) -> float:
    if w<=0 or k<=0 or p<=1 or not 0<d<=1:
        raise ValueError('invalid model input')
    labor = 250*d*(1-1/p if scenario=='fixed_output' else (p-1))
    if scenario not in ('fixed_output','fixed_labor_market_clears'):
        raise ValueError('invalid scenario')
    annual = w*labor-.10*k
    if annual <= 0: raise ValueError('no positive-cash-flow IRR')
    low, high = -.999,100.
    for _ in range(150):
        middle = (low+high)/2
        if annual*annuity(middle)>k:low=middle
        else: high=middle
    return 100*(low+high)/2

def write(path,header,body):
    with path.open('w',encoding='utf-8',newline='') as f:
        out=csv.writer(f,lineterminator='\n')
        out.writerow(header);out.writerows(body)

def run(outdir:Path):
    outdir.mkdir(parents=True,exist_ok=True)
    grid=[]
    for p,d,fe,ff,le,lf in PUBLISHED:
        for regime,uk,fr in [('fixed_output',fe,ff),
                              ('fixed_labor_market_clears',le,lf)]:
            for country,w,k,unit,published in [
                ('England',6.25,840,'pence',uk),
                ('France',9,2800,'sous',fr)]:
                computed=irr(w,k,p,d,regime)
                if abs(computed-published)>.35:
                    raise AssertionError('source model crosscheck fails')
                grid.append([p,d,regime,country,w,k,unit,
                    f'{computed:.4f}',f'{published:.1f}',
                    f'{computed-published:.4f}',str(computed>=15).lower(),
                    SOURCE,'PUBLISHED_ASSUMPTION_RECALCULATION_NOT_REALIZED_RETURN'])
    grid_head=['P','D','scenario','country','wage_local',
       'machine_cost_local','currency_local','computed_irr_pct',
       'published_irr_pct','difference_pp','passes_15pct_model_hurdle',
       'source_url','data_status']
    write(outdir/'spinning_jenny_published_model_m3c.csv',grid_head,grid)
    others=[]
    for wage_source,w in [('English_wage',6.25),('French_wage',4.66)]:
        for capital_source,k in [('English_machine',840),
                                 ('French_machine',1450)]:
            r=irr(w,k,3,.4,'fixed_output')
            a=annuity(.15)
            kmax=w*250*.4*(1-1/3)*a/(1+.1*a)
            others.append([wage_source,capital_source,w,k,f'{r:.4f}',
                 f'{kmax:.4f}',str(r>=15).lower(),
                 'https://wrap.warwick.ac.uk/44710/',
                 'MODEL_CROSSOVER_NOT_REALIZED_HISTORICAL_RETURN'])
    ch=['wage_source','machine_price_source',
        'wage_daily_pence_equivalent_rounded',
        'machine_price_pence_equivalent_rounded','fixed_output_irr_pct',
        'max_machine_price_at_15pct_pence_equivalent',
        'above_15pct_hurdle','source_url','data_status']
    write(outdir/'spinning_jenny_wage_capital_cross_m3c.csv',ch,others)
    assert len(grid)==36 and len(others)==4
    assert abs(irr(9,2800,3,.4,'fixed_output')-2.5)<.1
    assert abs(irr(9,2800,3,.4,'fixed_labor_market_clears')-53.5)<.1
    assert irr(4.66,840,3,.4,'fixed_output')>15
    assert irr(6.25,1450,3,.4,'fixed_output')<15
    print('PASS: rows=36, crossover=4, source tolerance <0.35pp')

if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('--outdir',default='.')
    args=parser.parse_args()
    run(Path(args.outdir))
