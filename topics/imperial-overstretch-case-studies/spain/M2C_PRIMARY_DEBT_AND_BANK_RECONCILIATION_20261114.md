# CASE-ESP-001 | M2c 官方债务清单与银行债权双边口径审计（2026-11-14）

**Canonical Issue:** https://github.com/fweiger/AI_book/issues/32  
**Existing Draft PR:** https://github.com/fweiger/AI_book/pull/36  
**Phase:** M2c (a new primary fiscal debt snapshot plus creditor perspective; NOT original year-by-year 1784–1807 account reconciliation).  
**Verification:** OFFICIAL_PARLIAMENTARY_TRANSCRIPT_REVIEWED / BANK_HISTORY_READ / DEBT_TOTAL_ARITHMETIC_PASS / PRIMARY_PDF_SCREENSHOT_BLOCKED / HISTORICAL_CAUSAL_TEST_NOT_RUN.

## 1. The actual historical question

Previous M2/M2b work identified naval-spending shares and colonial remittance disruptions but could not prove **debt service crowded out overseas defense**. Two separate mechanisms must now be tested:

- **Treasury crowd-out hypothesis (ESP-H1A):** higher obligations to bondholders and lenders lead to higher payments/arrears, causing otherwise planned Army/Navy or overseas allocations to be reduced.
- **Bank credit allocation hypothesis (ESP-H1B):** government borrowing uses most of a chartered bank's balance sheet and may displace commercial investment/credit.

They are different dependent variables; neither follows automatically from debt stock or a fall in naval spending shares.

## 2. New contemporary PRIMARY document: parliamentary debt inventory

**José Canga Argüelles, debt report presented to the Cortes on 30 March 1811; inventory headed _Estado aproximado de la Deuda nacional hasta 31 de Julio de 1808_**, published *Diario de Sesiones de las Cortes Generales y Extraordinarias*, no. 182, printed pp. 783–796, especially pp.794–796:
https://www.congreso.es/docu/blog/30031811-781.pdf

- The official indexed searchable document was retrieved as page text, with original amounts/footnotes and category labels. The PDF **image screenshot returned HTTP 403** and direct container download failed due DNS. Consequently **the table has been TEXT-TRANSCRIBED, not independently visually inspected against the original scan**. Treat potential document transcription or printing errors as live risks.
- [debt_inventory_1808_cortes_m2c.csv](debt_inventory_1808_cortes_m2c.csv) records 4 rows: three categories and one official total, preserving **whole reales + maravedís as separate integer fields**. The Spanish Ministry of Culture defines one *real de vellón* as **34 maravedís**: https://tesauros.cultura.gob.es/tesauros/numismatica/1187257.html . The printed notation "7.194.266.839 rs. 33 mrs." is **NOT** 7,194,266,839.33 decimal reales.

| Category in official 1808 inventory | Principal / liability (nominal reales, whole-unit approximation) | Listed annual interest obligations (nominal reales) |
|---|---:|---:|
| Current arrears, including Treasury arrears and Consolidation arrears | 1,309,927,739 | Not separately supplied |
| Funded / constituted debt | 4,064,130,080 plus 33 maravedís | 155,682,743 |
| Lifetime-annuity claims | 1,820,209,020 | 63,908,730 |
| **TOTAL, official estimate** | **7,194,266,839 plus 33 maravedís** | **219,591,473** |

Internal arithmetic: 1,309,927,739 + 4,064,130,080 + 1,820,209,020 = **7,194,266,839** whole reales, 33 maravedís preserved; 155,682,743 + 63,908,730 = **219,591,473** nominal reales *annual obligations*. **These are payment liabilities, NOT demonstrated actual paid annual interest**, and none is an annual military expenditure time series.

The **1,019,927,739** Treasury arrears line itself combines salaries, pensions, naval services and interest of varied debt; and the other current arrears are 290m consolidation debt. Neither is a separately identified Navy interest payment.

### Intra-source disagreement & bias risk

The same 1811 parliamentary report says the official total may understate debt and Canga personally estimates **7,863,882,285 reales plus 20 maravedís** as of approximately July 1808 — ~**669.6m reales more** than the published official table. This is **a contest of source estimates**, not a new verified stock record. Its distinct **5,972,871,647 reales plus 33 maravedís** refers to _older recognized debt_ in 1811, not to the same gross category total; do not place it in the denominator of the 1808 annual obligation ratio as an interchangeable total.

Specific textual tension: the debt inventory lists **Banco Nacional de San Carlos 125,653,391 reales plus 18 maravedís**, but the report's recognized-debt breakdown earlier gives **125,633,391 reales plus 18 maravedís**, differing **20,000 reales within the same official publication**. Do not silently correct without consulting a scan/manuscript. See printed pp.784 and 794–795.

The 1811 report also discusses **314,394,994 reales of 1808–1811 accumulated overdue debt interest** in a separate *unrecognized / pending* subsection. That is a multi-year unpaid **stock of arrears**, NOT the 1808 annual interest obligation of 219,591,473; potential overlaps with other overdue claims require accounting consolidation. Neither figure demonstrates cash payment of all interest.

## 3. Creditor-side check: Banco de San Carlos

At that date Banco de San Carlos was a **privately owned chartered bank** (a predecessor of the modern Banco de España), not a modern 1807 central bank. Evidence is from independent retrospective official Bank of Spain historical publications:

1. Pedro Tedde de Lorca (2000), _El Banco Español de San Fernando: un predecesor del Banco de España (1829–1856)_, Banco de España *Boletín Económico*, March 2000, pp.1–4 within that article, https://www.bde.es/f/webbde/Secciones/Publicaciones/InformesBoletinesRevistas/BoletinEconomico/00/Fich/be0003.pdf
2. Pablo Martín-Aceña (2017), _The Banco de España, 1782–2017: The History of a Central Bank_, Banco de España, pp.9–14, https://www.bde.es/f/webbde/SES/Secciones/Publicaciones/PublicacionesSeriadas/EstudiosHistoriaEconomica/Files/roja73e.pdf

The 2000 banking history says:
- In **1794** the royal Treasury owed the bank **~107m nominal reales**.
- At **end-1807** the creditor-side balance reached **~217m reales**, **more than 43m reales comprised accrued interest in arrears**, not new principal disbursement. Hence at least **19.82%** of the reported creditor balance represented unpaid interest (strict lower bound if the >43m claim is literal).
- A further **17m reales of suspended public-works credit** was mentioned separately; **do not add the 17m to 217m** without checking consolidation and bank ledger classification.
- Following the end of the war, the Crown's debt to the bank continued to rise; this is not itself a measured causal response in private credit.

The 2017 institutional history adds that end-1807 government loans and credits were **around 70% of bank total assets and 90% of its paid-up capital**. Commercial operations became a small part of the institution's activities. These are retrospective documented balance-sheet shares, not a randomized test of banking crowd-out.

### Bilateral accounts don't reconcile yet

| Source/date | Debtor/Creditor view | Banco–Treasury claim |
|---|---|---:|
| Bank historian end-1807 | Creditor balance sheet | ~217m nominal reales, includes >43m late interest |
| Parliamentary inventory July-1808, reported in 1811 | Crown debt-category table | ~125.653m nominal reales |
| Parliamentary recognized-debt list 1811 | Old recognized debt subset | ~125.633m nominal reales |

A simple **217−125.653 ≈91.347m reales difference** flags a need for original two-sided ledger reconciliation. It is NOT evidence by itself that the Spanish Treasury understated its debt by exactly this amount. The accounts differ in date, recognition, capital vs accumulated interest, asset/liability scope and potentially subsidiary/public works balances.

[bank_treasury_crosscheck_m2c.csv](bank_treasury_crosscheck_m2c.csv) registers provenance and cross-source non-comparability instead of manufacturing a reconciled balance.

### Credit deterioration evidence (secondary historical reconstruction)

Pedro Tedde reports the government issued about **963m nominal reales of vales in 1794–95** and **more than 799m in 1799**; the vales quote fell to **32% of nominal in 1800**. These are debt-security *market valuations*, not actual government bond-interest yields or the annual Treasury coupon bill. The historical narrative links war finance, falling silver shipments, banking losses and Treasury credit expansion, but attribution and selection remain observational.

## 4. Joined model for testing — do not sum incompatible series

**Four separate data owners:**

A. 1808 gross debt **stocks/annual scheduled interest**, as reconstructed in the 1811 government report.  
B. Banco San Carlos creditor **balance-sheet stock** 1794, 1807 (contains accrued unpaid interest).  
C. Treasury **cash receipts** 1778–1820 via Prados (2024), and Navy **central-debit outlays** via Barbier (1984); these are not the same accounting subject as A or B.  
D. Colonial New Spain **situados/remittances** 1720–1799 from institutional published decade summaries.

A/ B balances cannot be inserted as same-year expenditures into C. In particular:

- 1808 interest **due** = 219.591m ≠ interest **cash paid** in 1808 (NOT_ACQUIRED).
- The 1807 government-to-bank debt stock 217m ≠ military **expenditure** or merchant loan crowd-out quantified flow.
- The Navy spending share drop 1793–96 to 1797–1801 remains descriptively visible; it **does not identify what absorbed the budget**, because the complementary Army, arrears, debt coupon and offshore defense series are still missing.
- Snapshot ratios to 1807 Prados Treasury total are **cross-year stress illustrations**, not proper historical debt-service/revenue ratios; no such ratio is reported as a validated annual burden measure.

## 5. Competing hypotheses and source-based falsification

| Claim ID | What is now supported | Countertest | Classification |
|---|---|---|---|
| ESP-H1A War finance created substantial debt/interest obligations | Contemporary 1808 debt and >219m annual nominal contractual interest | Match annual actual payments/rollovers/Army/Navy flows and overseas expense before claiming crowd-out | DEBT_DUE_OBSERVED; CASH_PAID_NOT_ACQUIRED |
| ESP-H1B Bank resources became concentrated in Crown credit | Bank exposure ~217m, ~70% assets, >43m unpaid accrued interest | Bank's private loan ledger and trade opportunities, crisis other than government borrowing, bank-capital changes | BALANCE_SHEET_DESCRIPTIVE_SUPPORT |
| ESP-H1C Crown and Bank agree on amount owed | 1807 creditor vs 1808 debtor schedules disagree, 1811 internal 20k discrepancy | Match dates, subsidiary balances, accrued interest and recognition cuts using original bank and Treasury books | NOT_RECONCILED |
| ESP-H2 Administrative reforms increased extraction but destabilized local support | Separate 2025 working paper (not replicated) | Local elite, Indigenous resistance, 1808 shock controls | LITERATURE_ONLY |
| ESP-H4 Political rupture 1808 ended colonial finances | 1808 parliament shows legitimacy and war debt negotiations | End-1807 fiscal crunch and continuing post-1808 colonial commercial flows undermine exclusive cause | MULTICAUSAL / UNIDENTIFIED |

## 6. Source QA and unresolved constraints

- **PASS**: first government debt-category total reconciles preserving 34-maravedí unit, annual scheduled interest sum reconciles; source 1811 print identifies time, currency and payer, and its own alternative estimates; 2000/2017 Banco sources provide creditor-side exposure, overdue-interest lower bound and bank asset concentration.
- **PARTIALLY VERIFIED**: official 1811 searchable original text checked, BUT screenshot tool HTTP 403, container DNS download denied. It is a **contemporary primary parliamentary source**, but the primary page image / handwritten supporting accounts are NOT independently checked here.
- **NOT_ACQUIRED**: UKDS ESFDB 3104 annual source g104spd3.tab; complete 1784–1807 annual debt principal/repaid/coupons; Navy/Army/military unified source; Banco de San Carlos original balance-sheet line detail.
- **NOT_RUN**: archival audit of 1811 printed totals against source image; creditor–debtor reconciliation; fiscal debt-service crowd-out econometric design; public/private credit alternative model; cross-national Spain–Britain comparison in common fiscal units.
- **No irreversible finding**: do not promote “interest definitively destroyed the Navy”, “Spanish Empire was a net financial loss”, or “the 1811 minister's contested estimate is exact”.

## 7. Next single actionable step

**Obtain Banco de San Carlos original 1807 balance-sheet and Treasury-specific reconciliations, in parallel with lawful UKDS study 3104 g104spd3.tab access, and match the bank's ~217m creditor assets to the 125.653m /125.633m Crown tables with categories of principal, accrued interest, public-works balances and years.** This is more discriminating for the fiscal-credit channel than another unsourced aggregate debt estimate. Only after matched 1784–1807 interest *paid* data are recovered can naval crowd-out be tested.

All publication links retained; no copyrighted PDFs or proprietary raw account tables uploaded.
