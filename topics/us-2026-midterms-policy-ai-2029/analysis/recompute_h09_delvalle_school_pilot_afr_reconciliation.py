#!/usr/bin/env python3
"""H09 Del Valle ISD FY PILOT financial-report receipts vs school Ch313 tax year report.

Sources:
 FY2022 https://emma.msrb.org/P11685898.pdf
 FY2024 https://emma.msrb.org/P21874726.pdf (includes FY2023 comparator)
 FY2025 https://emma.msrb.org/P31547867.pdf (includes FY2024 comparator)
 CDR 2025 https://assets.comptroller.texas.gov/dat/ch313/1496/01496-CDR-2025-1014.xlsx

Requires poppler pdftotext and Python standard library.
School PILOT financial-statement revenue described as "received", not
bank-confirmed payment date or company net benefit. NOT Travis County Ch381.
"""
from __future__ import annotations
import csv,io,json,subprocess,hashlib,re,urllib.request,zipfile,xml.etree.ElementTree as ET

PDFS={
    2022:{"url":"https://emma.msrb.org/P11685898.pdf",
          "sha":"a4f60f7208a36affd9baed1f647a06d575ce7e44c4f9268e9db1f3dfaafcdd32"},
    2024:{"url":"https://emma.msrb.org/P21874726.pdf",
          "sha":"1671cbc7b922df1b6dad519bc2b56f8cef9857f97ba643874c1b99f9ee6b194b"},
    2025:{"url":"https://emma.msrb.org/P31547867.pdf",
          "sha":"dc5909585a8e84d06e60a669fa2cb9c1f331f745f98831b8bb5213afb84cffae"}
}
CDR_URL="https://assets.comptroller.texas.gov/dat/ch313/1496/01496-CDR-2025-1014.xlsx"
CDR_SHA="a0d3dcc7a071bd8400081a427acb78887bacad9cf8cd1d69ed96a5026556a432"
NS={"x":"http://schemas.openxmlformats.org/spreadsheetml/2006/main"}
EXPECTED_FY={2022:999609,2023:9543964,2024:17946611,2025:23002842}

def download(url):
    req=urllib.request.Request(url,headers={"User-Agent":"Mozilla/5.0"})
    with urllib.request.urlopen(req,timeout=18) as response:
        return response.read()
def sha_check(content, expected):
    sha=hashlib.sha256(content).hexdigest()
    assert sha==expected,(sha,expected)
    return sha
def pdftext(content):
    r=subprocess.run(["pdftotext","-layout","-","-"],input=content,capture_output=True,timeout=28)
    if r.returncode:raise ValueError(r.stderr.decode("utf8","replace")[:200])
    return r.stdout.decode("utf8","replace")
def pilot_in_note(text,year):
    start=text.find("N. Tax Abatements")
    if start<0:start=text.find("Tax Abatements")
    assert start>=0
    around=text[start:start+12000]
    pattern=rf"year ended\s+June\s+30,\s*{year},[\s\S]{{0,500}}?PILOT\s+of\s+\$\s*([\d,]+)"
    m=re.search(pattern,around,re.I)
    assert m,(year,around[:1400])
    return int(m.group(1).replace(",",""))
def parse_cdr(raw):
    z=zipfile.ZipFile(io.BytesIO(raw))
    shared=["".join(t.text or "" for t in e.findall(".//x:t",NS))
            for e in ET.fromstring(z.read("xl/sharedStrings.xml")).findall("x:si",NS)]
    sheet=ET.fromstring(z.read("xl/worksheets/sheet1.xml"))
    results={}
    for row in sheet.findall(".//x:sheetData/x:row",NS):
        vals={}
        for c in row.findall("x:c",NS):
            v=c.find("x:v",NS)
            if v is None:continue
            string=v.text or ""
            if c.get("t")=="s":string=shared[int(string)]
            column="".join(z for z in c.get("r") if z.isalpha())
            vals[column]=string
        year=vals.get("A","")
        if year in {"2021","2022","2023","2024"}:
            def get(col):return int(vals[col].replace(",","")) if col in vals else None
            results[int(year)]={"gross_tax_saving":get("J"),"revenue_protection":get("K"),
                                "supplemental":get("M")}
    assert len(results)==4
    return results
def run():
    texts={}
    for fy,meta in PDFS.items():
        raw=download(meta["url"])
        sha_check(raw,meta["sha"])
        texts[fy]=pdftext(raw)
        observed=pilot_in_note(texts[fy],fy)
        assert observed==EXPECTED_FY[fy],(fy,observed)
    assert re.search(r"Payments in lieu of taxes\s+17,946,611\s+9,543,964",texts[2024],re.I)
    assert re.search(r"Payments in lieu of taxes\s+23,002,842\s+17,946,611",texts[2025],re.I)
    cdrraw=download(CDR_URL)
    sha_check(cdrraw,CDR_SHA)
    cdr=parse_cdr(cdrraw)
    out=io.StringIO()
    writer=csv.writer(out,lineterminator="\n")
    writer.writerow(["school_fiscal_year_end_06_30","school_reported_tesla_pilot_received_or_recognized_usd",
        "source_financial_report_url","source_pdf_sha256","source_field_grade",
        "candidate_prior_tax_year_for_ch313_cdr","cdr_report_vintage","cdr_source_url",
        "cdr_gross_tax_saving_usd","cdr_revenue_protection_reported_usd",
        "cdr_supplemental_payment_reported_usd","cdr_reported_protection_plus_supplement_usd",
        "fiscal_PILOT_minus_candidate_tax_year_cdr_sum_usd","alignment_assessment",
        "not_equivalent_to"])
    for fy,amount in EXPECTED_FY.items():
        src=PDFS[fy] if fy in PDFS else PDFS[2024]
        tax_year=fy-1
        row=cdr[tax_year]
        report_sum=row["revenue_protection"]+row["supplemental"]
        residual=amount-report_sum
        grade=("FINANCIAL_NOTE_DESCRIBES_RECEIPT" if fy!=2023 else
               "FY2024_AFR_PRIOR_YEAR_COMPARATIVE")
        alignment=("EXACT_ARITHMETIC_MATCH_NOT_TRANSACTION_DATE_PROOF" if not residual else
                   "NOT_RECONCILED_FISCAL_VS_TAX_YEAR_ADJUSTMENTS_UNVERIFIED")
        writer.writerow([fy,amount,src["url"],src["sha"],grade,tax_year,2025,CDR_URL,
            row["gross_tax_saving"],row["revenue_protection"],row["supplemental"],report_sum,
            residual,alignment,"NOT_TRAVIS_COUNTY_CH381_GRANT_OR_COMPANY_NET_CASH_BENEFIT"])
    summary={"verification":"PASS","fiscal_year_PILOT_USD":EXPECTED_FY,
      "sum_FY2022_to_FY2025_school_reported_PILOT_USD":sum(EXPECTED_FY.values()),
      "financial_PDF_source_sha256":{str(k):v["sha"] for k,v in PDFS.items()},
      "FY2023_prior_year_comparative_from_FY2024_AFR":True,
      "ch313_CDR_source_sha256":CDR_SHA,
      "FY2025_minus_tax_year2024_CDR_protection_plus_supplement_USD":
          EXPECTED_FY[2025]-(cdr[2024]["revenue_protection"]+cdr[2024]["supplemental"]),
      "limit":"Fiscal-year school revenue described as received is not a bank ledger; fiscal-to-tax-year alignment is candidate and unresolved FY2025 residual means never compute company net benefit from gross minus PILOT."}
    return out.getvalue(),summary
if __name__=="__main__":
    data,summary=run()
    print("BEGIN_CSV")
    print(data.rstrip("\n"))
    print("END_CSV")
    print("SUMMARY_JSON="+json.dumps(summary))
