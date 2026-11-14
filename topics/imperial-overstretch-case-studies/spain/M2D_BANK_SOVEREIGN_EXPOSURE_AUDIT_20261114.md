# CASE-ESP-001 | M2d: Banco de San Carlos 1807 balance-sheet reconstruction and sovereign exposure (2026-11-14)

> Canonical Issue https://github.com/fweiger/AI_book/issues/32 | Existing Draft PR https://github.com/fweiger/AI_book/pull/36  
> Status: BANK_PUBLISHED_LEDGER_RECONSTRUCTION_ACQUIRED / SIX_DESCRIPTIVE_WINDOW_CHECKS_PASS / ACCOUNTING_CONFLICT_UNRESOLVED / ORIGINAL_BANK_LEDGER_NOT_ACQUIRED / CAUSAL_CROWDING_OUT_NOT_RUN

## Research question

M2c located the 1811 debt inventory (Spanish Treasury debtor) and a 2000 Banco de España retrospective estimate of ~217m reales owed to the chartered Banco de San Carlos (creditor). This session asks: **what does the bank's 1807 balance sheet actually show, how did asset concentration evolve, and do historical publications use compatible asset/debt concepts?**

Results MUST distinguish bank book assets from realized recoverable values, from government debt acknowledged in an 1811 schedule, and from actual Treasury annual interest paid. None is equivalent to imperial profit or an annual fiscal spending flow.

## 1. Newly retrieved published full bank balance (1807 year-end)

**Pedro Tedde and Carlos Marichal, eds. (1994), _La formación de los bancos centrales en España y América Latina_, Vol.I, Chapter I, Cuadro I.1, printed pp.26–27**, official Banco de España publication, https://www.bde.es/f/webbde/SES/Secciones/Publicaciones/PublicacionesSeriadas/EstudiosHistoriaEconomica/Fic/roja29.pdf . It cites **Tedde (1988), _El Banco de San Carlos_**, rather than providing the original handwritten general ledger.

The published balance reports, all **million nominal current reales**, 31 December 1807:
- Total assets / book liabilities: **313.4**, balancing.
- Asset claim on **Real Hacienda: 217.3** = **69.34%** of total assets (new project calculation).
- Accounting **Caja: 9.3**, consisting of **8.3 in government vales reales and 1.0 in coin/metallic money**. The metal alone is approximately **0.32%** of total book assets, a monetary/liquidity descriptor rather than a modern statutory liquidity ratio.
- Other assets combined (project residual): 313.4 − 217.3 − 9.3 = **86.8**; this includes separate lines for public works, impaired debtors, Philippine Company claims, loans against shares and others.
- Capital book value **240.0**, accrued unpaid shareholder dividends **40.1**, and other liabilities/reserves/P&L combined residual **33.3**. Dividends in arrears are **NOT** unpaid interest owed to the bank by the Crown.
- **1994 source 9.3 cash, 2005 source 9.2 cash for 1807**. Preserve this 0.1m difference (possibly source rounding or different revision); no source-level reconciliation performed.

[bank_1807_balance_diagnostics_m2d.csv](bank_1807_balance_diagnostics_m2d.csv) records these selectively extracted factual amounts, **original residual aggregations** and metric/source status. Copyrighted full 1994 balance table or PDFs are **NOT** copied into GitHub.

**Reading confidence:** official searchable PDF table text and footnotes read via online source; a direct PDF screenshot request timed out. Thus published table is TEXT_CHECKED_NOT_IMAGE_AUDITED; not a direct audit of bank manuscripts.

## 2. Additional multi-year longitudinal source: Fundación BBVA

**Pablo Martín Aceña and María Ángeles Pons (2005), in Albert Carreras / Xavier Tafunell eds., _Estadísticas históricas de España: siglos XIX–XX_, Vol.II, ch.9, _Sistema monetario y financiero_, Cuadro 9.8, printed p.681**, https://www.fbbva.es/wp-content/uploads/2017/05/dat/autores.pdf . Fundación BBVA official publication listing: https://www.fbbva.es/publicaciones/estadisticas-historicas-de-espana-siglos-xix-xx/ .

- The published source reports historical banking **Caja**, **Real Hacienda** claims, book capital and total assets in **million reales de vellón** for annual observations including 1784–1808. **1792–1793 are explicitly omitted** in the shown section; 23 observed years in 1784–1808, not 25 complete annual observations.
- Its source note is again **Tedde (1988)**, the same dependency as the 1994 Banco book. **Agreement in 1807 Real Hacienda 217.3/total 313.4 does not count as independent primary data corroboration.**
- [bank_concentration_windows_m2d.csv](bank_concentration_windows_m2d.csv) has only **6 new period-aggregated metrics**, not the original copyrighted 23-row book table. Formula: ratio for period = SUM(observed government claim book values) / SUM(observed total bank assets); period means = SUM(observed annual values)/n. Units million nominal reales/year for period average of year-end balances, **NOT transaction flows**. When periods have 2–6 year observations, they are not mutually equal precision or necessarily comparable to macro wartime averages.

| Observed years | n | Mean annual year-end Crown claim | Mean annual year-end bank cash | Mean bank assets | Crown / assets (ratio of sums) | Cash / assets (ratio of sums) |
|---|---:|---:|---:|---:|---:|---:|
| 1784–89 | 6 | 44.817 | 27.750 | 370.083 | 12.11% | 7.50% |
| 1790–91 | 2 | 125.650 | 15.900 | 457.100 | 27.49% | 3.48% |
| 1794–96 | 3 | 110.000 | 22.067 | 293.367 | 37.50% | 7.52% |
| 1797–1801 | 5 | 141.380 | 16.020 | 276.660 | 51.10% | 5.79% |
| 1802–04 | 3 | 193.133 | 7.267 | 283.033 | 68.24% | 2.57% |
| 1805–08 | 4 | 211.675 | 10.325 | 307.500 | 68.84% | 3.36% |

The rise in bank assets concentrated on the Crown is real in the *published book definitions*; that **does not identify how much private lending was displaced**. Government claims can rise due to interest accrued on old loans, valuation, altered capital structure, and loan disbursements; those must be decomposed before claiming "each extra Crown loan reduced private loans by one real".

## 3. NEW material source conflict: two Banco de España publications yield two "Crown debt" ratios

**Rafael Moreno Fernández (2010), _El personal del Banco de España desde su origen…_, Vol.I, ch.6, printed p.130**, Banco de España _Estudios de Historia Económica_ no.54: https://www.bde.es/webbde/SES/Secciones/Publicaciones/PublicacionesSeriadas/EstudiosHistoriaEconomica/Fic/roja54.pdf .

On the same **end-1807** date it describes "el débito de Hacienda" as **41.6 million pesetas**, or **53.1%** of bank assets. That source makes a **retrospective conversion** to pesetas (not the original accounting currency in 1807). A Banco de España 2017 historical study directly states the normalization 1 peseta = 4 reales for earlier years, https://www.bde.es/f/webbde/SES/Secciones/Publicaciones/PublicacionesSeriadas/EstudiosHistoriaEconomica/Files/roja73e.pdf .

- 2010 numerator 41.6 million normalized pesetas × 4 = **166.4 million historical reales**, with 166.4/313.4 = **53.10%**, matching the 2010 narrative.
- 1994 published full asset line = **217.3 million reales**, 217.3/313.4 = **69.34%**.
- **50.9 million reales discrepancy**. This is about **16.24 percentage points of the same 313.4m bank assets**.
- A separate Tedde (2000) publication reports **>43m reales in outstanding overdue interest** included within the broader ~217m bank claim. This *could* explain a part of a wider-versus-narrower split; **it does not settle the 50.9m gap, its remainder, the exact ledger inclusion rules, or the date/recognition method**.
- Other distinctions: 1994 includes the book balance of Real Hacienda in assets; 2010's expression "débito de Hacienda" could be narrower than the gross asset including accrued arrears. Do **not** relabel 166.4m as known "principal" or 50.9m as known "interest" without the original ledger. The competing values both must be preserved with source/date/accounting definition.

Another difference: 1994 *Caja* 9.3 vs Fundación BBVA (2005) *Caja* 9.2 for 1807, difference 0.1m. Minor numerically, useful signal that even histories using Tedde (1988) are not perfectly reproduced.

**Direct inference conclusion:** 1807 bank sovereign-risk concentration is substantial under either 53.1% or 69.34%, but the amount cannot be labeled **single audited debt principal**. Government-recognized ~125.653m as of July 1808 from the 1811 Parliamentary list remains a **third, mismatched debtor-side coverage**, not a direct bank balance amount.

## 4. Alternative channel to the simple "government crowding-out" story

1994 Banco narrative explicitly describes the 1799 panic (depositors sought metallic redemption), unreliable non-government assets and losses from risky management; debts, external war/shipping shock, *vales* discount risk and administrative error all matter.

- **ESP-H1B-GOV** Government credit concentration: supported descriptively by bank balance; needs outstanding principal by year vs private loans.
- **ESP-H1B-METAL** Metallic liquidity shortage from disrupted silver remittances: supported by author's history and 1m metal in 1807; needs year-by-year specie shipment and redemption evidence.
- **ESP-H1B-OTHER** Other troubled asset positions unrelated to direct sovereign debt: public works and Philippine-company share/credit, distressed loans; not equivalent to unproductive permanent losses.
- **ESP-H1B-RECORDS** Accounting recognition effects: government exposure differs 50.9m between two institutional historical works and further differs from 1811 Crown debtor statements. No causal regressions performed.

This means earlier "bank's 217m sovereign credit crowded out real investment" is an **unverified causal interpretation**, not a demonstrated amount.

## 5. Archived ORIGINAL primary materials located (but not acquired)

Banco de España Archivo Histórico, **Section 17: _Libros de contabilidad, copiadores de cartas y otros registros_**, official finding aid reference **ES.28079.AHBE/01.17** (fonds-level classification, **NOT** the specific 1807 book signature): https://www.bde.es/f/webbe/INF/MenuHorizontal/paraciudadano/archivo_historico/SECCIONES_AHBE.pdf (catalog pp.21–22). It covers historical **Mayores, Diarios, Inventarios y balances, Arqueos and Treasury registers**, allowing more exact targeting than asking generically for all 1782–1829 archives.

The Banco Archive has an official [digital copy request form](https://app.bde.es/gnt_seg/es/contacto?a=ZYflMv2MBhSQkmfsPzzxr9OWoBgKTZ9s); the form requires the user's **identity, email, exact requested source identifier and authorized intended use**, with restrictions against distributing or modifying images. The [general historical records inquiry](https://app.bde.es/gnt_seg/es/contacto?a=mQu9Z4vk9LSJC8SkUvOnjVopPY9f1i2B) can be used to obtain the *precise item-level signatura first*. No form submitted; no user identity was accessed or invented, and no archival files re-uploaded.

**Recommended precise records to ask archive staff to identify:** Banco Nacional de San Carlos **1807 year-end inventario/balance, libro mayor accounts labelled Real Hacienda and intereses atrasados, 1807–1808 ledger journal, capital/dividend account, Caja metallic and vales subaccounts**. Ask whether there is a contemporaneous Crown-side liquidation statement explaining which of these categories appeared in the July 1808 government schedule. Identify item-level signaturas before a document-copy request.

## 6. Verification matrix / single next action

| Work | Verified status |
|---|---|
| 1994 Banco published 1807 balance read from searchable online full table | PUBLICATION_TEXT_CHECKED (PDF screenshot timeout; not original scan) |
| 2005 Fundación BBVA years, source dependency and 6 period aggregates | PUBLICATION_TEXT_CHECKED / ARITHMETIC_RECOMPUTED; PDF screenshot timeout |
| 2010 Banco alternative 1807 41.6m pesetas / 53.1%, and 2017 4 reales/peseta conversion | SOURCE_TEXT_CHECKED / CURRENCY_ARITHMETIC_RECOMPUTED |
| 1807 balance major line partial adding and ratio calculation | PASS based on published numbers only |
| Archive Section 17 existence, archive access request options and form requirements | OFFICIAL_CATALOG_REVIEWED |
| Original 1807 Banco book balance and actual accrued-interest composition | NOT_ACQUIRED |
| UKDS Madrid g104spd3.tab annual 24-row source and same-owner Treasury/army/coupon flows | NOT_ACQUIRED |
| Creditor/debtor account match, private-credit counterfactual and fiscal-military crowd-out | NOT_RUN |

**Single next action:** obtain the *item-level catalogue reference* and legal digital access to **Banco de San Carlos 1807 original balance/Real Hacienda mayor with overdue-interest subledger**, then resolve **217.3 vs 166.4 vs 125.653** (government creditor asset gross/narrow/recognized debtor balance) by date, principal, unpaid interest and suspended works. Follow with UKDS 3104 authorized data and annual fiscal military tests. Keep Issue #32 OPEN and PR #36 Draft. No final "Empire net ROI" or causal judgement.


---

## Addendum — 2026-11-14 M2e after published PDF screenshot succeeded

**Correction of verification status only (not changing historic data):** an actual web PDF screenshot of Banco de España 1994, Cuadro I.1, printed p.27 / PDF 0-index page25, was successfully rendered and read in M2e after the previously reported screenshot timeout. The 1994 published table shows all 10 assets and 6 liabilities/equity figures with 313.4m reales on each side. This upgrades the **1994 published bank-balance page image** to PUBLISHED_1994_PAGE_IMAGE_VERIFIED; it still does **not** constitute checking the original Banco de San Carlos 1807 ledger or the later 1815 printed version of its 1808 shareholder meeting. The 2005 BBVA and 2010 Banco full PDF screenshot timeouts have not been cured.

**New route to original:** see [M2e](M2E_1807_PRIMARY_PRINTED_BALANCE_AND_CREDIT_INCOME_AUDIT.md), Ateneo de Madrid A-Caj.179/5 (1808 meeting, printed 1815, purported original 1807 folded balance), and [unsent Spanish archival inquiry drafts](ARCHIVAL_REQUEST_ES_M2E_20261114.md). Do not promote an original-balance verification claim until that foldout is actually acquired and inspected.
