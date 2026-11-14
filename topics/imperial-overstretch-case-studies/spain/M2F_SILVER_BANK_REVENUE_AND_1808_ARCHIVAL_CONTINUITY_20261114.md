# CASE-ESP-001 | M2f: Silver-export revenue shock, 1808 board continuity, and pinpoint archive requests

Date 2026-11-14. Canonical Issue: https://github.com/fweiger/AI_book/issues/32 . Existing Draft PR: https://github.com/fweiger/AI_book/pull/36 .

**Status:** PUBLISHED_SILVER_BUSINESS_EVIDENCE_PDF_IMAGE_VERIFIED / HISTORICAL_1808_GOVERNANCE_SOURCE_TEXT_READ / PRECISE_1808_BOARD_MINUTES_LOCATED_BY_PUBLISHED_CITATION / ATENEO_1808_FOLDED_BALANCE_NOT_DIGITIZED_IN_CATALOG / ORIGINAL_BANK_BOOK_NOT_ACQUIRED / CREDIT_OR_NAVY_CAUSAL_TEST_NOT_RUN.

## 1. Next best test: distinguish sovereign-asset crowding from collapse of a profitable trade line

M2d showed that bank Treasury claims occupied ~217.3 of 313.4 million nominal reales (69.34%) in the bank's end-1807 book assets. M2e showed that income shares shifted toward Treasury advances **plus other investments**. These cannot alone identify whether *private lending was crowded out*.

An alternative mechanism is that British blockade and interrupted American silver shipments independently destroyed one of Banco Nacional de San Carlos' earning businesses: **licensed silver exports**, putting pressure on bank profitability even in the absence of a new sovereign loan.

**Pedro Tedde de Lorca (Banco de España, Boletín Económico, March 2000), "El Banco Español de San Fernando: un predecesor del Banco de España (1829–1856)," printed p.3, PDF zero-index page 2**, official link:
https://www.bde.es/f/webbde/SES/Secciones/Publicaciones/InformesBoletinesRevistas/BoletinEconomico/00/Fich/be0003-art4.pdf

The **published page was visually read and its Spanish text directly checked** in this session. In the author’s own **historically estimated nominal units**:

| Period | Banco silver exports: published approximate annual mean | Banco profit from exporting silver: approximate annual mean | Source access |
|---|---:|---:|---|
| 1790–1794 | about 120 million reales/year (author: >6m pesos fuertes/year) | about 3 million reales/year | Bank historical article, published PDF page image |
| 1799 | no silver exported, per author | **not reported** | Bank historical article |
| 1800 | no silver exported, per author | **not reported** | Bank historical article |
| 1801–1807 | about 14 million reales/year (author: nearly 5m pesos fuertes over whole span) | about 0.3 million reales/year | Bank historical article |

Arithmetic on those *approximately published* period averages: silver export amount ~**88.33% lower** in 1801–07 than 1790–94; export-business profit ~**90.0% lower**, both descriptive only. We did NOT retrieve or total the underlying bank shipping manifests, prices, commissions, yearly books or realized net income. The two windows differ in length and contain their own war/peace exposure, including 1802–04 pause. Therefore neither observed difference is a causal blockade effect, and one cannot treat the silver business profit as the bank's overall net income.

The same Banco de España article (same PDF and page) describes **three** threats together: depreciation and unsustainability of discounting government vales reales; naval wartime interruption of silver export profits; mounting Crown credits with >43m nominal reales of accrued unpaid interest by 1807. These mechanisms plausibly interact. They must remain distinct variables until annual source data identify causes.

New small evidence dataset: [bank_silver_export_profit_m2f.csv](bank_silver_export_profit_m2f.csv), four observations (two windows, two zero-export years), without incorrectly imputing zero profits where none are reported.

## 2. Archival priority upgrade: real 1808 board-minutes BOOK numbers now available

**Rafael Moreno Fernández, Banco de España (2009 imprint, online release often dated 2010), _El personal del Banco de España: ... Vol. I Banco de San Carlos_,** pp.118–119 and 140, notes 58 and 32–34:
https://www.bde.es/f/webbde/SES/Secciones/Publicaciones/PublicacionesSeriadas/EstudiosHistoriaEconomica/Fic/roja54.pdf

This Banco scholarly text supplies specific citations **to the historical Banco de España archive for 1808**:

| Historical event | Published source's archival call reference | Status |
|---|---|---|
| 9 April 1808 board investigations into accountant/tenedor Joaquín Cifuentes | **ABE, Secretaría, AJG, libro 204 (AR), fols. 251 y ss.** | Item-level citation from academic history, original folios not inspected |
| 10 September 1808 board accounting and staffing reforms | **ABE, Secretaría, AJG, libro 194, fols. 42–45v** | Same limitation |
| 17 September 1808 reforms | **ABE, Secretaría, AJG, libro 194, fols. 53–56** | Same limitation |
| 5 October 1808 report | **ABE, Secretaría, AJG, libro 194, fols. 66–66v** | Same limitation |

This is substantial progress from M2d/e's **only 1783** book examples. However **libro 204 and 194 are 1808 administrative-board minute sources, NOT 1807 bank general balances or Real Hacienda ledger**. No claim that they contain the missing principal/interest breakdown or authoritatively solve 217.3 vs 166.4 vs125.653m.

A caution about contemporary internal controls: the same Banco history reports investigation of **duplicate dividends of 118,452 reales and 21 maravedís** and manipulated entries relating to accountant Joaquín Cifuentes, plus an 1808 proposal to tighten bookkeeping. This supports a distinct internal-control concern; it is **not** evidence of a 50.9m sovereign-credit discrepancy, and its magnitude is orders smaller. The published historian describes a General Shareholders meeting **28 April 1808** regarding Cifuentes, while other historical sources and the original book's title identify the 26th regular shareholders meeting on **20 April 1808**. We cannot tell from currently inspected excerpts whether there were separate meetings or an uncorrected date inconsistency. **Do not merge them into a single precisely dated event.**

## 3. Falsification of the very strong version of immediate political shutdown on 2 May 1808

**Julio Fernández-Sanguino Fernández, _El Banco de San Carlos y la Constitución de 1812_, historical study, full searchable PDF**:
https://www.cervantesvirtual.com/descargaPdf/el-banco-de-san-carlos-y-la-constitucion-de-1812-1214681/

The author reconstructs the bank's post-uprising board activities:
- 20 April 1808 shareholders' general meeting reported.
- **2 May** Madrid uprising.
- **9 May** bank board meeting dealing with continuing matters, including a delayed French/Spanish currency exchange.
- **14 May** bank board discussed a notification/decree from the newly imposed political authorities.
- Author says **four May board sessions**, average attendance roughly seven, without providing all calendar dates here.

Thus **"Bank administration immediately ceased entirely on 2 May"** is inconsistent with the published institutional meeting timeline. That does NOT prove the bank continued normal lending, private discounts, silver transport, metallic convertibility or ordinary operations. The source PDF text was directly read; the web screenshot for this PDF failed due Unicode decoding, so its original page image was NOT visually audited in this session. The correct identification statement is **SECONDARY_SOURCE_TEXT_SUPPORT**, not primary session-minute verification.

[bank_1808_board_archival_chronology_m2f.csv](bank_1808_board_archival_chronology_m2f.csv) records eight source-derived dated events (including precise April/September/October AJG references), year/day and evidence grade.

## 4. Source-access stop rule: official catalog explicitly has no digital item

Official Madrid Community union catalog for the San Carlos shareholder meeting serial:
https://bibliotecavirtualmadrid.comunidad.madrid/bvmadrid_publicacion/es/consulta/registro.do?id=63115

**Verified text: "Sin objeto digital asociado" (no associated digital object) for this catalog record.** It confirms the **Ateneo de Madrid 1808 physical issue A-Caj.179/5**, but does not provide an online scan, and does not prove the 1807 folded bank balance is complete in the Ateneo copy. The 2025 auction lot 420 separately says another exemplar has 80 pages and an end-of-volume folded 1807 financial statement. This official no-digital-object marker provides a rational stop rule: do not keep claiming that refreshing this catalog will yield the original balance; first use the actual custodial reproduction route.

**Ateneo official librarian policy and contact, verified in live institutional page:**
https://ateneodemadrid.com/biblioteca/

- **biblioteca@ateneodemadrid.es** is explicitly listed for remote reference questions and document reproductions.
- Copying is subject to the library's legal and preservation rules and may involve payment or personal identification. The site gives a physical address Prado 21, Madrid, Spain, but **this is archival access context, not travel-route advice**.
- An actionable Spanish draft message already exists in [ARCHIVAL_REQUEST_ES_M2E_20261114.md](ARCHIVAL_REQUEST_ES_M2E_20261114.md); M2f appends the verified recipient to that draft, asks exact leaf completeness and image reproduction rights. **NO EMAIL WAS SENT, NO USER ACCOUNT IDENTITY WAS USED, NO REPLY RECEIVED**.
- Banco archives similarly require source identification and user-controlled permissions. The new 1808 AJG book numbers offer a real item-level starting point for staff to locate analogous Real Hacienda books for 1807.

## 5. New mechanism comparison and quantitative limits

| Candidate mechanism | New evidence supporting exposure or chronology | Distinguishing countertest | Status |
|---|---|---|---|
| ESP-H1B sovereign banking credit concentration | M2d 217.3m Crown bank claim in 1807, >43m late interest; M2e revenue composition skew | Principal vs accrued interest, bank private-loan book and government loan disbursement, compare same-year balances | DESCRIPTIVE_SUPPORT_ONLY |
| ESP-H1D blockade harms profitable cross-Atlantic silver business | Banco 2000 reports 120m→14m annual exports and 3m→0.3m annual profits | Same-period registered shipment volumes and costs; permit controls, maritime interception, monopoly legislation; port-level comparisons | PUBLISHED_DESCRIPTIVE_ESTIMATE |
| ESP-H1E immediate absolute bank institutional shutdown after 2 May | 9/14 May board meetings continued, so strongest shutdown claim fails | Separate operations: May–June discounting books, cash balances, advances, bank divided Madrid/Cádiz | ABSOLUTE_SHUTDOWN_CLAIM_NOT_SUPPORTED |
| ESP-H1F accounting-control failure contributes to bank stress | 1807–08 Cifuentes accounting and duplicate-dividend investigation, direct archival minute citation | Audit loss amounts, insurance/recovery, independent accountant ledger; do not extrapolate from 118k to 50.9m | QUALITATIVE_RIVAL |
| ESP-H1A fiscal coupon cash service crowds out Navy | 1811 official 1808 interest **due** not paid, Barbier published peninsular naval spend; still mismatched stock/flow | Obtain annual matching-owner coupon cash payments, military debits and bank creditor-interest amortizations | NOT_IDENTIFIED |

**We do NOT estimate causal effects from published annual or period summaries, or declare colonization profitable/unprofitable on this evidence.** No original UKDS study 3104 1784–1807 Madrid dataset acquired, no actual fiscal interest paid per year, no treasury/army/net ROI reconciliation.

## 6. Validation, rights and one next action

- Banco de España (2000) **publisher PDF page image** seen; its published period silver figures and no-export years correctly tagged approximately reported.
- Banco de España (2009/2010) p119 and 140 **indexed article PDF text** supplies original 1808 archive **book and folio numbers**; screenshot timed out, no actual AJG books read.
- Cervantes-hosted Fernández-Sanguino article full text explicitly gives 20 April meeting and 9/14 May board meetings; page image unreadable due Unicode tool failure.
- Ateneo institutionally verifies **library email** for remote document copying; union catalog explicitly says no associated digital item.
- No new online 1807 folded balance image acquired and no message sent. All four earlier 1783-only references retain their original date labels; 1808 new references are independently date-stamped to 1808.

**Single next action:** through user-authorized contact to **biblioteca@ateneodemadrid.es**, request a scan or precise permission for **Ateneo A-Caj.179/5 (1808 meeting, published 1815) including the complete 1807 balance foldout**; in parallel ask Banco Historical Archive for the **1807 original account books that match the now pinpointed 1808 AJG inventory series**, particularly Real Hacienda principal vs overdue-interest. Until a response or lawful image acquisition, this is ACCESS_BLOCKED rather than a ledger-reconciliation pass.
