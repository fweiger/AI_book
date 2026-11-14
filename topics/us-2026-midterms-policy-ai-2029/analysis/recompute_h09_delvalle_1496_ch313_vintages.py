#!/usr/bin/env python3
"""TOPIC-011 H09: official Texas Comptroller Del Valle ISD #1496 Chapter313 CDR vintages.

Read the official 2023 and 2025 School District Cost Data Report XLSX files
using stdlib zipfile + ElementTree (raw OOXML; no additional dependencies).
Output a source-anchored CSV and JSON source/arithmetical validation.

IMPORTANT:
- This is Del Valle ISD Chapter313 school property-tax value limitation,
  NOT Travis County Chapter381 grant/ACH payments.
- "Gross_Tax_Saving" is the workbook's gross tax-levy difference, NOT cash paid
  by the county, NOT net realized company benefit, and NOT a future actual.
- 2025 reporting-year rows are not independently verified payment receipts.
"""
import csv,io,json,sys,urllib.request,zipfile,xml.etree.ElementTree as ET,hashlib

FILES={
 "2023": {"url":"https://assets.comptroller.texas.gov/dat/ch313/1496/01496-CDR-2023-1016.xlsx",
          "sha256":"f076ff7810b24d141b33b0fe49bddbc7c47bf02402119bdfd0d75165b4b3b12c",
          "posted_date":"2026-02-06"},
 "2025": {"url":"https://assets.comptroller.texas.gov/dat/ch313/1496/01496-CDR-2025-1014.xlsx",
          "sha256":"a0d3dcc7a071bd8400081a427acb78887bacad9cf8cd1d69ed96a5026556a432",
          "posted_date":"2026-10-14"}
}
NS={"s":"http://schemas.openxmlformats.org/spreadsheetml/2006/main"}
FIELDS=["Tax_Year","Total_Investment","Property_Market_Value","Taxable_Value_IS_purposes",
        "Taxable_Value_MO_purposes","I&S_Tax_Rate","M&O_Tax_Rate",
        "Tax_Levy_Without_Limitation","Tax_Levy_With_Limitation","Gross_Tax_Saving",
        "Revenue_Protection","Extraordinary_Educational_Expenses","Supplemental_Payments"]

def parse_xlsx(data):
    z=zipfile.ZipFile(io.BytesIO(data))
    shared=[]
    for si in ET.fromstring(z.read("xl/sharedStrings.xml")).findall("s:si",NS):
        shared.append("".join(el.text or "" for el in si.findall(".//s:t",NS)))
    sheet=ET.fromstring(z.read("xl/worksheets/sheet1.xml"))
    def unpack(row):
        result={}
        for cell in row.findall("s:c",NS):
            val=cell.find("s:v",NS)
            if val is None:continue
            value=val.text or ""
            if cell.get("t")=="s":value=shared[int(value)]
            col="".join(c for c in cell.get("r") if c.isalpha())
            result[col]=value
        return result
    raw=[unpack(r) for r in sheet.findall(".//s:sheetData/s:row",NS)]
    assert [raw[0].get(chr(65+i)) for i in range(13)]==FIELDS,raw[0]
    years={}
    for d in raw[1:]:
        if "A" not in d or not d["A"].isdigit():continue
        year=int(d["A"])
        if 2020<=year<=2036:
            values={}
            for i,k in enumerate(FIELDS):
                cell=d.get(chr(65+i))
                values[k]=int(cell.replace(",","")) if cell and "," in cell else (float(cell) if cell and "." in cell else int(cell)) if cell else None
            years[year]=values
    assert {2022,2023,2024,2025,2026}.issubset(years)
    return years

def run():
    out=[]
    originals={}
    for vintage,meta in FILES.items():
        req=urllib.request.Request(meta["url"],headers={"User-Agent":"Mozilla/5.0 (AI_book public data validation)"})
        with urllib.request.urlopen(req,timeout=15) as resp: content=resp.read()
        sha=hashlib.sha256(content).hexdigest()
        assert sha==meta["sha256"],(vintage,sha,meta["sha256"])
        originals[vintage]=parse_xlsx(content)
        for year,values in originals[vintage].items():
            if year<2022 or year>2028:continue
            reportyear=int(vintage)
            status="HISTORICAL_PRE_REPORT" if year<reportyear else ("REPORTING_YEAR_VALUE_UNAUDITED_CASH" if year==reportyear else "FUTURE_PROJECTED_NOT_ACTUAL")
            gross=values["Gross_Tax_Saving"]
            levywithout=values["Tax_Levy_Without_Limitation"]
            levywith=values["Tax_Levy_With_Limitation"]
            assert levywithout-levywith==gross,(vintage,year,levywithout,levywith,gross)
            out.append([vintage,meta["posted_date"],year,status,
                        values["Total_Investment"],values["Property_Market_Value"],
                        values["Taxable_Value_MO_purposes"],levywithout,levywith,gross,
                        values["Revenue_Protection"],values["Supplemental_Payments"],
                        meta["url"],meta["sha256"],"DELV_ISD_CH313_NOT_TRAVIS_CH381_GRANT"])
    out.sort(key=lambda r:(int(r[2]),int(r[0])))
    names=["reporting_year_vintage","state_posted_date","tax_year","tax_year_status_at_report",
       "reported_total_investment_usd","reported_property_market_value_usd",
       "reported_MO_taxable_value_usd","reported_levy_without_limitation_usd",
       "reported_levy_with_limitation_usd","reported_gross_tax_saving_usd",
       "reported_revenue_protection_usd","reported_supplemental_payments_usd",
       "original_xlsx_url","original_xlsx_sha256","incentive_program_separation"]
    buf=io.StringIO()
    writer=csv.writer(buf,lineterminator="\n")
    writer.writerow(names)
    writer.writerows(out)
    V1,V2=originals["2023"],originals["2025"]
    change={}
    for year in [2022,2023,2024,2025,2026]:
        old=V1[year]["Gross_Tax_Saving"];new=V2[year]["Gross_Tax_Saving"]
        change[str(year)]={"2023_vintage":old,"2025_vintage":new,"difference_usd":new-old,
             "difference_pct":round(100*(new-old)/old,3) if old else None,
             "2025_vintage_revenue_protection":V2[year]["Revenue_Protection"],
             "2025_vintage_supplemental_payments":V2[year]["Supplemental_Payments"]}
    s2022_24=sum(V2[y]["Gross_Tax_Saving"] for y in [2022,2023,2024])
    s2022_25=sum(V2[y]["Gross_Tax_Saving"] for y in [2022,2023,2024,2025])
    summary={"verification":"PASS","program":"Del Valle ISD Chapter313 No1496, not Travis County Chapter381",
      "observations":len(out),"source_vintages":FILES,"gross_saving_comparison":change,
      "2025_vintage_reported_taxyears_2022_to_2024_gross_sum_usd":s2022_24,
      "2025_vintage_taxyears_2022_to_2025_gross_sum_usd_includes_current_reportyear":s2022_25,
      "status_limit":"Reported difference in tax levy, not actual Treasury grant payment or net-after-revenue-protection/supplemental expense; post-report future values are forecasts."}
    return buf.getvalue(),summary

if __name__=="__main__":
    csvout,metadata=run()
    print("BEGIN_CSV")
    print(csvout.rstrip("\n"))
    print("END_CSV")
    print("SUMMARY_JSON="+json.dumps(metadata))
