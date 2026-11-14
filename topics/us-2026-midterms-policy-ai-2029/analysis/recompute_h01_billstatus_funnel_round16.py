#!/usr/bin/env python3
"""H01 round16: exhaustive official GovInfo BILLSTATUS HR/S bill-vehicle funnel.
Stdlib only. Downloads two ZIPs per Congress, verifies SHA, parses each XML.
Not a causal estimator; signed laws and associated policy content may be moved
between bill vehicles and the 119th Congress is unfinished.
"""
import csv, hashlib, json, os, sys, urllib.request, zipfile
from collections import Counter, defaultdict
from pathlib import Path
from xml.etree import ElementTree as ET

ALL_CONGRESSES=(110,116,118,119)
AREAS=('Health','Economics and Public Finance','Taxation','Energy',
       'Government Operations and Politics','Science, Technology, Communications',
       'Foreign Trade and International Finance','Armed Forces and National Security')
CACHE=Path(os.environ.get('H01_GOVINFO_CACHE','/tmp/h01_round16_govinfo'))
OUT=Path(os.environ.get('H01_OUTPUT_DIR','/tmp/h01_round16_govinfo_result'))
CONGRESSES=tuple(int(x) for x in os.environ.get('H01_CONGRESSES','110,116,118,119').split(','))
assert set(CONGRESSES)<=set(ALL_CONGRESSES)
CUT={c:f'{2008+2*(c-110):04d}-11-14' for c in ALL_CONGRESSES}

def get_zip(url,path):
    path.parent.mkdir(parents=True,exist_ok=True)
    if path.exists() and zipfile.is_zipfile(path):return
    t=path.with_suffix('.downloading')
    req=urllib.request.Request(url,headers={'User-Agent':'TOPIC011-H01-reproducible-public-research/1.0'})
    with urllib.request.urlopen(req,timeout=90) as src,open(t,'wb') as dst:
        while True:
            b=src.read(1048576)
            if not b:break
            dst.write(b)
    if not zipfile.is_zipfile(t):raise ValueError('Invalid ZIP '+str(t))
    t.replace(path)

def earlier(items, cutoff):
    d=[x for x in items if x and x<=cutoff]
    return min(d) if d else ''

def parse(z,c,typ,cutoff):
    rows=[];quality=Counter()
    for name in z.namelist():
        if not name.lower().endswith('.xml'):continue
        quality['xml_count']+=1
        try:
            bill=ET.fromstring(z.read(name)).find('bill')
            if bill is None:quality['missing_bill']+=1;continue
            if int(bill.findtext('congress','0'))!=c or bill.findtext('type','').lower()!=typ:
                quality['bad_id']+=1;continue
            number=int(bill.findtext('number','0'))
            intro=(bill.findtext('introducedDate','') or '')[:10]
            if number<=0 or not intro:quality['bad_intro']+=1;continue
            if intro>cutoff:quality['after_cutoff']+=1;continue
            acts=defaultdict(list)
            for a in bill.findall('./actions/item'):
                code=a.findtext('actionCode','').strip()
                date=(a.findtext('actionDate','') or '')[:10]
                if code and len(date)==10:acts[code].append(date)
            reports=[]
            for a in bill.findall('./committees/item/activities/item'):
                if (a.findtext('name','') or '').lower()=='reported by':
                    d=(a.findtext('date','') or '')[:10]
                    if d:reports.append(d)
            h=earlier(acts.get('8000',()),cutoff)
            s=earlier(acts.get('17000',()),cutoff)
            p=earlier(acts.get('28000',()),cutoff)
            law=earlier(acts.get('36000',()),cutoff)
            rep=earlier(reports+acts.get('5000',[])+acts.get('14000',[]),cutoff)
            rows.append(dict(congress=c,bill_id=f'{c}{typ}{number}',bill_type=typ,
                             introduced=intro,committee_reported=rep,
                             house_passed=h,senate_passed=s,
                             both_passed=max(h,s) if h and s else '',
                             presented=p,became_law=law,
                             policy_area=bill.findtext('./policyArea/name') or 'Unknown'))
        except Exception as e:
            quality['bad_xml']+=1
            if quality['bad_xml']<4:print('BAD_XML',name,type(e).__name__,str(e)[:150],file=sys.stderr)
    return rows,quality

def summarize(c,period,area,rows):
    a=[r for r in rows if area=='ALL' or r['policy_area']==area]
    n=len(a)
    cnt=lambda x:sum(bool(r[x]) for r in a)
    d={'congress':c,'matched_cutoff':period,'policy_area':area,'introduced':n}
    for k in ('committee_reported','house_passed','senate_passed','both_passed','presented','became_law'):
        d[k]=cnt(k)
    d['house_only']=sum(bool(r['house_passed']) and not r['senate_passed'] for r in a)
    d['senate_only']=sum(bool(r['senate_passed']) and not r['house_passed'] for r in a)
    d['law_without_both_codes']=sum(bool(r['became_law']) and not r['both_passed'] for r in a)
    d['presented_without_both_codes']=sum(bool(r['presented']) and not r['both_passed'] for r in a)
    d['intro_to_law_pct']=round(100*d['became_law']/n,4) if n else ''
    d['intro_to_both_pct']=round(100*d['both_passed']/n,4) if n else ''
    return d

def write_csv(path,rows):
    path.parent.mkdir(parents=True,exist_ok=True)
    if not rows:return
    with path.open('w',encoding='utf-8',newline='') as f:
        w=csv.DictWriter(f,fieldnames=rows[0].keys());w.writeheader();w.writerows(rows)

def main():
    summaries=[];manifests=[];audit=[];source_sums={}
    for c in CONGRESSES:
        rows=[]
        for t in ('hr','s'):
            url=f'https://www.govinfo.gov/bulkdata/BILLSTATUS/{c}/{t}/BILLSTATUS-{c}-{t}.zip'
            path=CACHE/f'BILLSTATUS-{c}-{t}.zip'
            print('FETCH',url,flush=True,file=sys.stderr)
            get_zip(url,path)
            sha=hashlib.sha256(path.read_bytes()).hexdigest()
            with zipfile.ZipFile(path) as z:
                chunk,q=parse(z,c,t,CUT[c])
            print('PROCESSED',c,t,len(chunk),dict(q),flush=True,file=sys.stderr)
            manifests.append(dict(congress=c,bill_type=t,url=url,sha256=sha,zip_bytes=path.stat().st_size,cutoff=CUT[c],**q))
            rows+=chunk
        if len({r['bill_id'] for r in rows})!=len(rows):raise ValueError('Duplicate bill IDs')
        source_sums[c]=len(rows)
        for area in ('ALL',)+AREAS:
            summaries.append(summarize(c,CUT[c],area,rows))
        # Reproducible example rows, *not* a representative subsample
        for area in AREAS:
            sub=sorted((r for r in rows if r['policy_area']==area),key=lambda r:r['bill_id'])
            for r in (sub[:1]+[next((r for r in sub if r['became_law']),None),
                                next((r for r in sub if r['both_passed'] and not r['became_law']),None)]):
                if r and r not in audit:audit.append(r)
        write_csv(OUT/f'h01_govinfo_{c}_bill_vehicle_rows_20261114.csv',rows)
    write_csv(OUT/'h01_round16_billstatus_funnel.csv',summaries)
    write_csv(OUT/'h01_round16_source_manifest.csv',manifests)
    write_csv(OUT/'h01_round16_bill_audit_examples.csv',audit)
    summary={'asof_date':'2026-11-14','source':'GovInfo BILLSTATUS ZIP HR/S','cutoff':'Nov 14 of second year per congress',
             'congresses':CONGRESSES,'row_counts':source_sums,'summary':summaries,
             'manifests':manifests,'audit_examples_count':len(audit),
             'cautions':['All counts are bill vehicles; no related-bill/content consolidation',
                         'Only HR/S bills, not HJRES/SJRES (can become law) or ceremonial resolutions',
                         '119th is right-censored; the others are also truncated at second-year Nov14',
                         'Reported activity requires dated committee activity named Reported by',
                         'Passage codes 8000 (House), 17000 (Senate), 28000 presented, 36000 law',
                         'GovInfo bulk starts with 108th, 104th excluded from identical extraction',
                         'The latest ZIP is not an archival point-in-time snapshot from Nov14 2008,2020,2024',
                         'PolicyArea is single primary classification, does not imply enacted policy content']}
    (OUT/'h01_round16_summary.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2),encoding='utf-8')
    print('RESULT_JSON_START')
    print(json.dumps(summary,ensure_ascii=False,separators=(',',':')))
    print('RESULT_JSON_END')
if __name__=='__main__':main()
