# CASE-ESP-001 | M1 deep source audit and M2 data acquisition map | 2026-11-14

> Canonical issue: https://github.com/fweiger/AI_book/issues/32  
> Existing draft PR: https://github.com/fweiger/AI_book/pull/36  
> Parent comparison: https://github.com/fweiger/AI_book/issues/30  
> Status: SOURCE_AUDIT_PARTIAL / PUBLISHED_TABLE_TRANSCRIBED / ANNUAL_DATA_NOT_ACQUIRED / CAUSAL_REPLICATION_NOT_RUN

## Research question

Test separately (1) extraction and transfer of colonial fiscal resources; (2) imperial military financing and the vulnerability of Spain's fiscal-military system; (3) reform-induced changes to local political coalitions; and (4) why a resource-rich empire did not industrialize like Britain. Do not infer causality from historical sequence or equate remittances with net Crown profit.

## New numerical evidence: New Spain remittance destination, 1720–1799

The 2022 edited volume published by Fundación Museos del Banco Central de Costa Rica and Universidad Pablo de Olavide includes María del Pilar Martínez López-Cano, “Moneda y crédito en América: El caso de Nueva España,” Cuadro 8, printed pp. 336–337, citing Marichal y Souto (2012), p. 93. Annual **averages within ten-year periods**, in historical pesos, are separately reported for **Remesas Castilla** (transfers to Castile/metropole) and **Remesas situados** (transfers financing other possessions).

| Decade | Castile pesos/year | Situados pesos/year | Both pesos/year | Situados share |
|---|---:|---:|---:|---:|
| 1770–1779 | 1,435,062 | 3,453,880 | 4,888,942 | 70.65% |
| 1780–1789 | 1,655,605 | 6,170,565 | 7,826,170 | 78.84% |
| 1790–1799 | 4,317,453 | 4,748,523 | 9,065,976 | 52.38% |

Full published 1720–1799 decade table is transcribed with source in remittance_decadal_m1.csv. The two components reconcile exactly to the printed total for each row. Shares here are calculated from displayed aggregates and rounded to 2 decimal places. The shift in the *composition* of remittances is descriptive; there is no established causal explanation from this table alone.

The 2022 chapter (pp. 337) also cites an **approximately 250 million pesos** outward fiscal remittance cumulative during 1780–1810 and approximately 35 million pesos extraordinary collections (30 million loans; 5 million donativos), reflecting Marichal (1999) and Wobeser (2003). A separately accessible chapter by Dorothy Tanck de Estrada and Carlos Marichal, “¿Reino o colonia? Nueva España, 1750–1804,” in *Nueva historia general de México*, gives approximately **100 million pesos situados** versus **150 million pesos net transfers to Spain** within the circa-250-million total. THESE ARE PUBLISHED ESTIMATES, NOT RECONSTRUCTED FROM THE ORIGINAL LEDGERS HERE. Period-end inclusion and possible overlap between historical accounts should be checked against the originals. Do not add these amounts to other fiscal components without reconciliation.

- Published Cuadro 8: https://museosdelbancocentral.org/wp-content/uploads/2022/03/Monedas-Medios-de-Cambio-y-Espacios-de-Circulacion-en-America-Latina-y-Espana-1500-1900.pdf
- El Colegio de México scholarly chapter: https://epubs.bibliotk.mx/epubReader/reader/files/nueva_historia_general_de_mexico/OEBPS/hgmcap7.html

## New evidence source: European State Finance Database (ESFDB) study 3104

UK Data Service/University of Leicester, European State Finance Database, Spanish Revenues and Loans in the Eighteenth and Early Nineteenth Centuries. DOI: https://doi.org/10.5255/UKDA-SN-3104-1

The published **codebook** at https://doc.ukdataservice.ac.uk/doc/3104/mrdoc/pdf/guide.pdf identifies:
- g104spd1.tab: 1784–1807 Spanish General Treasury revenue, article Table 1 (the codebook header has a contradictory older label, so use the source note and verify actual columns).
- g104spd2.tab: 1788–1820 reconstructed general treasury net versus notional revenue; REVTOT1 and REVTOT2 differ.
- g104spd3.tab: **24 observations, 16 variables, Madrid Treasury 1784–1807**, thousands of *reales de vellón*, based on Barbier & Klein (1981), Table B-1, p. 338.
- g104spd4.tab: 1788–1820 classified net revenues.
- g104spa1.tab/g104spa2.tab: 16th-century loan series with different provenance.

**Critical data integrity finding:** for g104spd3, MREVTOT and CHKTOT agree only in 1789, 1792, 1793, 1795, 1800, 1805; the ESFDB documentation recommends CHKTOT for graphs, but differences need reconciliation before analytical ratios. MREGION has missing values in 1806 and 1807. INDIES includes receipts from colonies **including deposits and borrowing by colonial cajas**, so INDIES is *not* all pure taxes. LOANS mixes loans with donativos, depósitos and fianzas, so not all LOANS is newly issued debt. Cross-treasury transfers must be consolidated without double counting.

Original source/archival locator: Barbier & Klein, *Journal of Economic History* 41(2), 315–339 (1981), DOI https://doi.org/10.1017/S002205070004359X ; Archivo General de Simancas, Dirección General del Tesoro, inventario 16, guión 3, legajos 10–19 (1784–1805); inventario 16, guión 19, legajos 45–67 (general treasury and 1806–07 treasury evidence). This locator is transcribed from the article notes, **not evidence this team visited AGS**.

The codebook is accessible; **underlying tab records were NOT downloaded or recalculated in this round**. Thus annual 1784–1807 Madrid revenue values, annual military spending and debt-service ratios remain NOT_ACQUIRED/NOT_RUN.

## Data acquisition: El Colegio de México

The portal https://realhacienda.colmex.mx/ (Klein/TePaske-related royal treasury database) provides separate Nueva España, Perú, Alto Perú etc. datasets. Nueva España Excel ZIP is linked at https://realhacienda.colmex.mx/wp-content/uploads/2021/07/NE.zip . In this round the ZIP fetch via accessible paths was unsuccessful (WEB_UNSUPPORTED_ZIP / DOWNLOAD_FAILED), so **no underlying workbook was inspected**. The portal itself advises consulting supporting archival books for fine precision. No raw tables are represented as locally checked.

## Additional competing mechanism: Bourbon intendancy reform

Chiovelli, Fergusson, Martínez, Torres & Valencia Caicedo, **June 24, 2025 working-paper version**, *Bourbon Reforms, State Capacity, and Revolution in the Spanish Empire*: https://www2.um.edu.uy/fcee_papers/2020/Bourbon_Reforms_State_Capacity_and_Revolution_in_the_Spanish_Empire.pdf

The paper describes a raw base of **85 royal treasuries** across 1770–1799 and a **79-treasury / 1,959 treasury-year** baseline estimation sample (Table 3 col 1). Its fixed-effects estimate for the introduction of intendants is **0.290 log points**, standard error **0.115**, implying exp(0.290)-1 ≈ 33.6% within its specified identification design; this is **not** a 33.6% increase in the whole empire's aggregate revenue or an independent project replication.

The authors report increased administration and tax collection, lower Indigenous rebellion incidence, and local elite political backlash. However, evidence for post-1808 independence is distinct from direct fiscal impact identification; time-varying confounding and selective archives remain concerns. Their appendix says fewer than 50% of treasuries have data by 1810; the political exit analysis requires sensitivity to attrition. Table 6 finds a spending increase, but not a statistically distinguishable increase in the share of public-goods spending; it cannot prove 'all extra taxes became military expenses'. The paper remains a **working paper** in the reviewed version; regression code/data were not downloaded or reproduced.

Importantly, the source paper's standardization uses **pesos de ocho**, including source-specific conversions from *pesos ensayados* and *pesos de oro*. Those are not a general license to convert Madrid's *reales de vellón* at a fixed timeless rate.

## Counterexamples and falsification

| H-ID | Mechanism | Discriminating test | Counterexample / blocker |
|---|---|---|---|
| ESP-H1 | Repeated overseas wars -> disruption of colonial transfers + financing costs -> central fiscal constraint | 1784–1807 time-aligned Madrid Indies/ordinary receipts vs war-year spending, credit costs, ship blockade indicators; distinguish cash from accrual | Debt payment suspensions in the 1500s did not immediately dissolve empire; annual spending/debt interest not acquired |
| ESP-H2 | Intendancy reforms -> more tax collection AND erosion of Creole elite support | 1770–1799 local treasury panel with actual intendant arrival year, event-study and pre-trends; link elite biographies separately | Indigenous conflict may fall while elite antagonism rises; thus 'all uprisings increased' is false |
| ESP-H3 | Royal resource gains -> inadequate domestic industrial transformation | Regional textile, capital, wages, coal costs and trade exposure vs Britain; track 1720–1820 | Catalan industrial development rules out 'Spain had zero manufacturing'; sector and region must be specified |
| ESP-H4 | 1808 dynastic illegitimacy -> local sovereignty claims and war -> imperial exit | Distinguish 1808 shock, local juntas, military loss and regional fiscal collapse | Fiscal pressures existed long before 1808; loss of most continental colonies did not end Cuba/Philippines rule |

No regression, sensitivity test, financial ROI, military-cost/revenue causal estimate, or cross-country statistical comparison has been executed in this work.

## Evidence levels and sole next action

- **SOURCE_VERIFIED**: publisher and institutional pages; study 3104 codebook and explicit known integrity exceptions; published table headings/values in the 2022 institutional volume; full readable text of 2025 working paper.
- **LITERATURE_REPORTED**: 250m cumulative remittances, 100m/150m destination split, 0.290 log-point effect; no independent historical/causal reproduction.
- **NOT_ACQUIRED**: g104spd3.tab original data records, El Colegio de México NE.zip workbook, original AGS manuscripts, annual debt-interest and military expense rows.
- **NOT_RUN**: original-account reconciliation, inter-treasury consolidation, cross-country model, direct historical peer review.
- **Next action (single)**: acquire permitted access to UKDS **g104spd3.tab** 1784–1807; separately check 24 annual records / 16 columns / MREGION missingness / CHKTOT vs MREVTOT, and only then build a same-owner annual cash-flow series. If access is denied, document license/access and fall back to sourced printed Table B-1; do not fabricate annual data.

All quotations have been paraphrased; no publisher PDF or restricted dataset has been committed.
