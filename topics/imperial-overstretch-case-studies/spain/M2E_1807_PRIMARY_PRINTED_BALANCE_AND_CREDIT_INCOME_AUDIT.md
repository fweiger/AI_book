# CASE-ESP-001 — M2e Primary 1807 bank balance acquisition and income-mix verification (2026-11-14)

Canonical Issue https://github.com/fweiger/AI_book/issues/32 | Existing Draft PR https://github.com/fweiger/AI_book/pull/36
Evidence state: PRIMARY_1808_MEETING_PUBLICATION_LOCATED_NOT_READ / BANCO_1994_PUBLISHED_PDF_PAGE_VISUALLY_CHECKED / 2010_SOURCE_INCOME_MIX_TEXT_READ / ORIGINAL_1807_ACCOUNT_BOOK_NOT_ACQUIRED / CAUSAL_CROWDING_OUT_NOT_RUN.

## 1. Newly located original shareholders' report, not yet obtained

The **Ateneo de Madrid** retains an 1808 Banco Nacional de San Carlos general meeting serial under **call number A-Caj.179/5**, verified from the official Madrid historical library union catalog: https://bibliotecavirtualmadrid.comunidad.madrid/bvmadrid_publicacion/es/consulta/registro.do?id=63115 .

A 2025 antiquarian physical-copy description (El Remate auction no.265, **lot 420**) describes the **Vigesimosexta Junta General de Accionistas del Banco Nacional de San Carlos, 20 April 1808**, printed by Imprenta de Ibarra **in 1815**, 80 pages, with a **folded statement at end containing the bank's general balance for 1807**: https://www.elremate.es/wp-content/uploads/2025/12/catalogo-subasta-el-remate-265-diciembre-2025.pdf .

Source-critical qualifications:
- The meeting occurred **1808**, but this available described printing is dated **1815**. It is an historical primary bank shareholders' publication rather than 1807 original ledger entries.
- Ateneo holdings confirm the 1808 issue, but **do not yet establish that their particular copy has the intact foldout**; the auction catalog describes another physical exemplar. Request a page-by-page holdings check before saying that the Ateneo foldout itself was verified.
- BNE historical serial records cover 1782–1829 but the accessible digitization listing only identified a **1791** exemplar; no authenticated 1808 1807-balance scan was obtained.
- This PRIMARY report is therefore **LOCATED_NOT_READ**, not original balance audit PASS. If the foldout is obtained, it can cross-check the 1994/Tedde reconstructed book figures; it may still be a summarized institutional balance rather than line-item principal/interest ledgers.

The actionable Spanish-language custodial inquiries are prepared in ARCHIVAL_REQUEST_ES_M2E_20261114.md. No individual contact information supplied, no request submitted.

## 2. Corrected image-reading status for the 1994 Banco balance

This round successfully used a live PDF screenshot of **Banco de España (1994), La formación de los bancos centrales... vol.I, Cuadro I.1, printed p.27, PDF page index 25**:
https://www.bde.es/f/webbde/SES/Secciones/Publicaciones/PublicacionesSeriadas/EstudiosHistoriaEconomica/Fic/roja29.pdf

Previous M2d report had recorded a screenshot timeout; the new screenshot **succeeded**. Thus the accurate status is now PUBLISHED_1994_PAGE_IMAGE_VERIFIED, not ORIGINAL_1807_BANK_MANUSCRIPT_VERIFIED.

Publisher table values, in **million nominal reales de vellón**, 31 December 1807:
- Asset entries: Caja 9.3; Real Hacienda 217.3; Obras Públicas 13.1; Deudores en suspenso 17.6; Efectos a cobrar 9.5; Ayuntamiento de Madrid 4.7; Compañía de Filipinas 26.3; Corresponsales 2.2; Préstamos sobre acciones 11.6; Cuentas diversas 1.8. **Recomputed asset sum = 313.4**.
- Liabilities/equity: Capital 240.0; Reservas 15.9; Depósitos diversos 2.4; Pérdidas y ganancias 11.1; Dividendos atrasados 40.1; Cuentas diversas 3.9. **Recomputed liabilities/equity sum = 313.4**.
- Publisher footnote: **8.3m of Caja 9.3m are government vales reales, only 1.0m metallic coin**. Philippine company 26.3m includes 21m invested fund and 5.3m receivable. Bank book values are not direct liquidation proceeds.

No full copyrighted publication table or PDF is recopied into this repo. These are brief factual values used for audit and new calculations, with original reference.

## 3. New economic evidence: shares of BANK REVENUE, not credit-stock flows

Rafael Moreno Fernández, **Banco de España (2010), El personal del Banco de España ... Vol. I: Banco de San Carlos**, printed pp.129–130 and Annex 3, https://www.bde.es/f/webbde/SES/Secciones/Publicaciones/PublicacionesSeriadas/EstudiosHistoriaEconomica/Fic/roja54.pdf .

The historical author describes the bank's **cumulative income shares**:

| Period | Anticipaciones a la Hacienda AND other smaller investments (% cumulative bank revenue) | Descuentos / bill discounting (% cumulative bank revenue) |
|---|---:|---:|
| 1791–1799 | 52.2 | 5.3 |
| 1800–1808 | 80.2 | 0.3 |
| Later minus earlier | +28.0 percentage points | −5.0 percentage points |

The author separately reported that in 1799 about **81.5% of banking assets were immobilized**, including government debt and doubtful claims from the Philippine company, share-backed loans and French debt. Government was important but **not the only plausible driver of bank distress**.

Critical cautions: the broad 80.2% category is NOT pure government loan interest; it includes small other investments. Income mix is **not a year-by-year private credit balance, transaction volume or causal credit-displacement regression**. The 2010 PDF searchable pages were read but its screenshot operation timed out; label source TEXT_CHECKED only. Data: bank_income_composition_m2e.csv.

An earlier Banco historical account says the 1799 metallic bank run was temporarily relieved when Cinco Gremios Mayores repaid a sizable balance. That event is an alternative liquidity explanation. It does not show absence of serious government debt exposures.

## 4. More precise archival references, strictly date-scoped

Rafael Moreno Fernández, **De Computis** (2013), *La organización contable en la constitución del Banco de San Carlos en 1783*, Appendix 2 printed p.46, https://dialnet.unirioja.es/descarga/articulo/4730878.pdf , documents actual BOOK IDs of **1783** in the historic Banco archive:
- General balance: **Libro 471 (1783)**;
- General Diary: **Libros 67, 353 (1783 only)**;
- General Ledger: **Libros 129, 238 (1783 only)**;
- Caja cash-count book: **Libro 99 (1783–1790)**.

These are valid examples of original book-level call numbers, but **none identifies a 1807 record**. Original 1807 record remains NOT_ACQUIRED. The broad official archive classification **ES.28079.AHBE/01.17** includes Mayores, Diarios, Inventarios y Balances. The 2026 archive researchers' page https://www.bde.es/wbe/es/punto-informacion/contenidos/servicios/archivo-historico/investigadores/ confirms that account-specific consultation needs stated topic/dates, prior appointment, identification for in-person access and possible permission. No identity data has been submitted.

The more efficient acquisition path is:
1. Ask **Ateneo** first for availability, completeness and authorized scan of **1808 meeting 1815 printing A-Caj.179/5 including 1807 foldout**.
2. Ask Banco Historical Archive staff for **1807** balance, Real Hacienda Mayor, outstanding-interest account and Diario **exact item signaturas** (using 1783 volume examples only as navigational evidence).
3. When a source image is legally acquired, verify its denomination, exact accounting date, lending principal, accrued unpaid interest, government-funded public-works entries, transfers and written-off balances, comparing:
   - 1994/Tedde wider book asset **217.3m**;
   - 2010 Moreno narrower 41.6m retrospective pesetas = **166.4m** reales (currency conversion 4:1);
   - 1811 Cortes government schedule circa **125.653m** reales as of July 1808.
4. Do not assume the 50.9m gap equals overdue interest. Another Banco historian says 1994 gross item includes >43m accrued arrears but its exact components and historical account cutoffs remain unresolved.

## 5. Validation / falsification outcomes

| Test | State |
|---|---|
| Visually inspect 1994 Banco official published Table I.1 page | **PASS in this round**, but reconstructed edition only |
| Sum all 10 published asset categories and 6 liabilities/equity items | **PASS, both 313.4m** |
| 2010 author-reported revenue-mix percentages and period differences | SOURCE_TEXT_REVIEWED / ARITHMETIC_CHECKED |
| Locate 1808 meeting 1815 publication and Ateneo call number | BIBLIOGRAPHIC_LOCATION_PASS; source foldout NOT_READ |
| Locate 1783 original archival books and correctly mark dates | PEER_REVIEWED_PUBLISHED_LOCATOR; no 1807 book ID |
| 217.3 vs166.4 vs125.653 borrower-creditor reconciliation | **NOT_RUN / ORIGINAL_LEDGER_NOT_ACQUIRED** |
| Cash coupon vs navy spending or commercial credit causal tests | **NOT_RUN** |
| Unauthorized requests or redistribution | NONE |

**Single next action:** obtain an authorized **1807 folded balance sheet from the Ateneo's 1808 meeting record** (and/or precise 1807 Banco Mayores signaturas); read and digitize its relevant data first, then proceed to the creditor–borrower reconciliation. Avoid converting missing archives into simulated numbers. Keep Draft PR and Issue open.
