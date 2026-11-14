# CASE-ESP-001 · M2t — Santo Domingo 1754–1774 situado period-table audit and contemporary PARES evidence

Date: 2026-11-14. Owner: [AI_book #32](https://github.com/fweiger/AI_book/issues/32), [Draft PR #36](https://github.com/fweiger/AI_book/pull/36), branch `topic-010/case-esp-001-spain-20261114`. No new issue.

## Main finding: published total conflicts with reconstructed 20 source rows

[Amadeo Julián, 2017, *Clío* 194](https://academiadominicanahistoria.org.do/wp-content/uploads/2018/04/clio194.pdf), printed p47 Table *Situado de Santo Domingo (1754–1774)*, reproduces published financial data attributed to **María Rosario Sevilla Soler (1980), pp237–238**. The PDF was indexed as searchable text and the original publisher PDF extracted table was read through web. **Screenshot of source pages attempted via web screenshot but failed (CACHE_MISS); no claim of visual page audit or the 1980 book original.**

The 20 printed rows are faithfully transcribed into [source data CSV](santo_domingo_1754_1774_reales_maravedis_m2t.csv) preserving ambiguous date labels **without annual imputation**.

| Measure | Value | Status |
|---|---:|---|
| Number of printed period rows | 20 | Transcription / arithmetic audit |
| Sum of printed integer reales columns | **28,790,201** | JS independent row sum PASS |
| Sum of listed fractional maravedís (treating “--” as zero FOR ARITHMETIC ONLY) | **246 maravedís** | JS PASS |
| Carry under **34 maravedís = 1 real de vellón** | 7 reales + 8 maravedís | CONDITIONAL currency-of-account assumption |
| Conditional aggregate with carry | **28,790,208 reales, 8 maravedís** | PASS math, original textual/exchange context NOT fully confirmed |
| Table printed “Total” | **28,720,208 reales, 28 maravedís** | PUBLISHED_TABLE_TEXT_VERIFIED_ONLY |
| Following paragraph printed total | **28,790,208 reales, 28 maravedís** | PUBLISHED_PARAGRAPH_TEXT_VERIFIED_ONLY |
| Printed total vs paragraph total | **70,000 reales** difference | OPEN transcription/printing-vs-original discrepancy |
| Paragraph maravedís vs conditional reconstructed remainder | **20 maravedís** difference | OPEN |
| Paper prose equivalent | **3,598,776 pesos** by dividing 28,790,208 by 8 | PRESERVES AUTHOR'S CONVERSION; monetary account provenance NOT verified |

**Material caution:** The official Spanish Ministry of Culture [Numismatic Thesaurus: Real de vellón](https://tesauros.cultura.gob.es/tesauros/numismatica/1187257.html) verifies nominal **34 maravedís per real de vellón**. It also warns of historical currency relationships; the paper speaks of `reales`, then converts to a peso de a ocho at **8 reales per peso**. These **must not be assumed to be identical to metropolitan reales de vellón** until original source unit and silver versus vellón definitions are established. 34-based carry above is an **explicit test assumption**, not proof of currency denomination equivalence across all documents.

**Temporal exception:** Source contains the line `5/6/1756-31/12/1757` for 977,761 reales and also a separate `1756` line 1,419,109 reales. Because date labels overlap, the 977,761 cannot be treated as uniquely **calendar 1757 annual revenue**. Likewise fiscal dates run between 1766–1767 and 1770–1772 in several cells. This is a **20-row collection of heterogeneous accounting periods, not a 21-year observation-ready annual series**. Do not fill missing years with zero; do not estimate direct 1757 revenue fall or correlation to the mutiny from these period labels.

Source-level result is more precise than M2s 1742–1750 eight arrival events, but **not a direct manuscript certification or payroll vouchers**. An original 1980 book audit and matching archival account records would be needed to decide which table total and fractional remainder are authoritative.

## Contemporary **1757** official PARES archive metadata: exact item-level verified

Three [original-catalogue/secondary-locator rows](santo_domingo_pares_archive_fiscal_shipping_m2t.csv) are particularly useful:

1. **PARES `SANTO_DOMINGO,942,N.67`** — [official item](https://pares.cultura.gob.es/ParesBusquedas20/catalogo/description/13111419): Francisco Rubio governor's Ocoa Bay fleet entrance/exit and settlement correspondence, creation **1757-04-10 to 1757-08-13**, **25 folios**; official record marks digitized images and no access restrictions. This **does not establish any specific Mexican situado cash delivery**.
2. **PARES `SANTO_DOMINGO,942,N.53`** — [official item](https://pares.cultura.gob.es/ParesBusquedas20/catalogo/description/13105153): same governor's reports of English privateers attacking Spanish communication vessels, creation **1757-04-10 to 1757-08-15**, **64 folios**, four accompanying proceedings mentioned in catalog. It documents **the existence of a contemporary source on shipping attacks**, not that soldiers' salary money was aboard any intercepted ship.
3. **PARES `SGU,LEG,7150,1`** — [official item](https://pares.cultura.gob.es/ParesBusquedas20/catalogo/description/1303557), broader 1784–1787 materials **194 folios**; indexed original descriptions include **1786** Banco Nacional de San Carlos clothing, equipment and provisioning purchases for Santo Domingo military units. Distinct **1786 procurement bank operations**, not **1757 situado cash** and not 1797 Valencia Junta loans. The credit/procurement-to-empire-defense bridge is plausible but requires actual original commercial and royal accounts to classify.

Four different grade categories are maintained: **official item-level catalogue description** (PARES exact archival item dates/folios, historical object unviewed), **scholarly call-number citation** (AGI 1088/1092, no PARES item found), **digitized image listed** (not images actually accessed), and **manuscript read** (none).

For `AGI SANTO_DOMINGO,1088/1092` and Mexican `Reales Cédulas Originales vol78 exps104/109`, this round did **not** find a direct publicly readable item-level scan or year-confirming decree. **1757/1758 remains unresolved.**

## More controlled historical research program

The minimally viable sample is a two-axis dataset:
- **A. Physical transport evidence:** named ship, arrival/departure dates, port, official contemporaneous naval correspondence, ship interception; no invented cargo.
- **B. Fiscal payroll evidence:** approved situado, sent amount, document-based received amount, carryover, soldier wages due, receipts/paid dates, local bridge loans and arrears.

Only a matched transaction across both axes warrants a cash-delay claim. Useful competitors are navy/piracy conditions, variation in authorized tax revenue, local treasury priorities, civil and military account boundaries, merchant financing, governance/distribution decisions and record coverage.

### Outcome and next action

**PASS:** 20-row textual table transcribed and 28,790,201 + (246/34) = 28,790,208 reales + 8 fractional maravedís independently JS-recomputed; two archival 1757 item-level PARES metadata and a distinct 1786 bank supply file identified; historical original-source grade strictly observed.

**LIMITATION:** Screenshots of the original 2017 PDF pages returned CACHE_MISS; PARES actual manuscript folios also not opened. Original Sevilla Soler 1980 table not acquired, and 1757 salary actual payment never checked. No archival emails sent. Historical causal tests **NOT_RUN**.

**Single next action:** Attempt **PARES digitized images of `SANTO_DOMINGO,942,N.67`** first and inspect real convoy/paper carrying *situado* references, then **`N.53`** privateer incident folios, with exact image URL, folio, date and quote/uncertainty; if images remain blocked, maintain blocker and prioritize authorized research query for AGI 1092/1088 and Mexican vol78 original. Do not use metadata to assert ships or payroll carried specific money. Keep Issue #32 OPEN and Draft PR #36 DRAFT.
