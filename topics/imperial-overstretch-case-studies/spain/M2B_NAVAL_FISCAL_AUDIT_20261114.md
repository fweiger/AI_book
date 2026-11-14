# CASE-ESP-001 — M2b Naval Expenditure, Fiscal Definitions and the Limits of "Imperial ROI" (2026-11-14)

**Canonical Issue** https://github.com/fweiger/AI_book/issues/32 | **Draft PR** https://github.com/fweiger/AI_book/pull/36 | **Status** PEER_REVIEWED_PUBLISHED_TABLE_REVIEWED / DERIVED_PERIOD_CALCULATIONS_PASS / PRIMARY_MADRID_DATA_NOT_ACQUIRED / DEBT_INTEREST_CAUSAL_TEST_NOT_RUN.

## 1. Substantive research progression

M1 examined silver, remittances, debt and legitimacy; M2 transcribed **Prados de la Escosura (2024)** annual reconstructed receipts and exports for 1778–1820. This M2b step adds **central government expenditure** and a directly relevant naval budget, allowing a partial test of a necessary component of overextension without misrepresenting a naval expense as the total cost of empire.

Primary interpretation to test:
- **Fiscal-military priority shift (descriptive):** War-time naval expenditures become very large in 1793–96 as a fraction of central government spending; they subsequently fall as the government's total spending itself remains elevated.
- **NOT proven:** Debt interest caused the reduction, colonial naval defense earned a negative net return, or British military pressure alone explains the entire change.

## 2. Credible archival-derived naval source and tables

**Jacques A. Barbier (1984), "Indies Revenues and Naval Spending: The Cost of Colonialism for the Spanish Bourbons, 1763–1805,"** *Jahrbuch für Geschichte von Staat, Wirtschaft und Gesellschaft Lateinamerikas* 21, 171–188. Tables II–IV visually inspected in authorized reprint in F. C. Schneid (ed.), *Warfare in Europe 1792–1815* (2007/2018), PDF preview:
https://api.pageplace.de/preview/DT0400.9781351125581_A32309317/preview-9781351125581_A32309317.pdf

- **Table II**: printed pp.176–177, PDF preview pp.34–35, Spanish General Treasury **total debits/peninsular naval debits** 1760–1805; **thousands of nominal reales de vellón**. It groups *sueldos y gastos de marina* with *tesoreros de marina y pagadores de guerra*. Internal transfers and year carryovers excluded. No inflation adjustment.
- Peninsular Navy accounts **do not encompass overseas Havana, colonial naval bases, local ship supply and certain indirect defense expenses** (print p.178, preview p.36). Thus a peninsular Navy figure is **not** empire-wide military cost.
- Tables III and IV compare Cádiz *Depositaría de Indias* receipts to mainland navy spending by five-year windows. 1760–79 numerator is *Indias funds*, but the 1780–89 numerator is **combined Indias + Rentas**, a structural category shift after the 1778 *comercio libre* reforms. Cross-break ratios cannot be plotted as homogeneous estimates of direct remittances.

Only **derived five-window summaries** and six five-year comparisons are committed, *not* the full copyright-protected annual Table II or the publisher's PDF. Original page and licensing boundaries preserved in source_registry_m2b.csv.

## 3. New financial evidence, 1784–1805

From annual values visible in Table II, this project computed period totals and navy-spending ratios. Values are **million nominal reales/year**, shares = sum(naval debits)/sum(total Treasury debits) within each window, *not arithmetic means of annual shares*.

| Period | n | Central Treasury total spend mean | Peninsular Navy spend mean | Navy / general spending |
|---|---:|---:|---:|---:|
| 1784–1792 | 9 | 630.504 | 157.822 | 25.03% |
| 1793–1796 | 4 | 924.953 | 291.421 | 31.51% |
| 1797–1801 | 5 | 1218.765 | 174.517 | 14.32% |
| 1802–1804 | 3 | 1127.222 | 125.485 | 11.13% |
| 1805 | 1 | 972.279 | 74.469 | 7.66% |

The 1793–1796 naval mean exceeds 1784–1792 by ~84.7%; general Treasury mean rises ~46.7%. The wartime 1797–1801 navy **share** is sharply lower than 1793–1796, even while the general Treasury's total spending remains above the earlier mean. In selected years, Table II reports navy shares **22.5% (1789), 38.8% (1794), 34.5% (1795), 10.1% (1800), 7.7% (1805)**.

**What this does NOT tell us:** lower Navy expenditure might reflect a reallocation to Army, interest/coupon service, arrears, treasury financing costs, administrative charges, debt restructurings, offshore financing, or reduced physical naval investment. The source has no sufficiently matched annual interest payments to adjudicate those possibilities. Naval cash spending is not equivalent to the entire military budget or the new debt created.

### Accounting identity caution

Barbier's Table II note says the author's expenditure and income totals are within 0.80% over **1784–1805**, while pointing out **reporting-year differences**. This is a historical government treasury cash/debit accounting feature, **not proof of a fiscally balanced government, sustainable borrowing, absence of a public debt crisis, or an empire net return near zero**. Distinguish credit creation, financing, cash matching and debt stock.

## 4. Cádiz ratio study: where colonial financing did and did not "cover" the Navy

The new [cadiz_indies_naval_quinquennia_m2b.csv](cadiz_indies_naval_quinquennia_m2b.csv) transcribes only limited table-level figures and calculates an indicative receipt-to-navy cost ratio:

| Period | Cádiz money category | Cádiz related receipts (thousand nominal reales) | Mainland Navy (thousand nominal reales) | Arithmetic ratio |
|---|---|---:|---:|---:|
| 1760–64 | Indies | 286,525 | 465,580 | 61.54% |
| 1765–69 | Indies | 313,356 | 404,941 | 77.38% |
| 1770–74 | Indies | 365,727 | 458,773 | 79.72% |
| 1775–79 | Indies | 297,383 | 681,971 | 43.61% |
| 1780–84 | Indies + Rentas | 580,427 | 1,034,733 | 56.09% |
| 1785–89 | Indies + Rentas | 808,335 | 747,410 | 108.15% |

Interpretation: direct Cádiz Indies money represented a varying **potential offset to mainland Navy spending**, but never the full empire's surplus. The 1785–89 >100% ratio **must not** be interpreted as "colonies alone paid for all naval costs" because post-1778 numerator includes Rentas and source scope is Cádiz, not all colony/state ledgers. The Navy denominator excludes naval stations abroad and all other imperial Army/administrative expense.

The 1775–79 decrease in coverage to ~43.6% reflects a marked change in relative financial flows, not a proven colony-wide margin; this period includes maritime and imperial military preparation, not all colonies simultaneously losing profitability.

## 5. Independent literature cross-check reveals a definition trap

Carlos Marichal, *Benefits and Fiscal Costs of Colonialism: American Remittances to Spain, 1760–1814*, originally Spanish 1997, available English institutional-hosted version:
https://e-archivo.uc3m.es/rest/api/core/bitstreams/cf6a9b8b-a6e8-4296-b426-ef8e7c54e6c3/content

Its Table 2 "Indias" includes, **for 1783–1807**, (a) remittances from the American treasuries **plus (b) an imputation of 25% of metropolitan Tobacco income and (c) 30% of General Income**. In contrast the Prados (2024) Table 6.2 M2 source labels a narrower remittance quantity. These are not alternative measurements of one equal "colonial transfer" variable.

Illustrative source-text values, both measured in **million nominal reales**:
- **1791:** Marichal's broadly attributed Indies category **229.686** versus Prados direct remittance **161**. Denominators are **ordinary revenue 675.558** (Marichal) versus **total reconstructed public revenue 800** (Prados); consequently Marichal gives **34.00%** of ordinary versus the narrower Prados **20.13%** of total. Both percentages can correctly express *different numerator and denominator definitions*.
- **1802:** Marichal Indies broad **413.448** versus Prados direct **350**; the difference cannot be treated as a contradiction or as missing ships without inspecting category imputations, date allocation, and accounting source.
- Marichal Table 2 labels **1808 = n.i. (no information)**; Prados Table 6.2 lists anomalous 1808 covered Treasury values (zero total). Neither should be described as "the actual state had zero income in 1808". Marichal also reports ~30m silver pesos reaching the anti-Napoleonic Spanish government October 1808–February 1811, which shows differing recipient and time/agency scope; this latter number remains **author-reported, not project archival reconstruction**.

**Verification caveat:** Marichal PDF text and footnotes were retrieved from the university repository, but screenshot of that PDF failed with HTTP 403. Its figures above are *published-source-text extracted*, not visually inspected paper scans. This is explicitly weaker than the visually inspected Barbier tables.

## 6. Debt, wars and an incomplete financing ledger

Marichal summarizes earlier government expert Canga Argüelles estimates for the **1793–1795 war against the French Convention**: cost ~**4,741m reales**, only roughly **40%** paid by taxes, with substantial loans/donations, Banco de San Carlos and merchant advances, American contributions and *vales reales* debt. These values are secondary historical estimates from the published scholarly article; do not add reported financing items without exact cash flow, double-counting and due-date reconciliation. This is positive evidence for **financing dependence**, NOT proof that subsequent debt interest directly crowded out specific colonial/military allocations.

A candidate falsifiable mechanism is:

1. War shocks alter maritime transfers and increase extraordinary financing.
2. New debt and payments produce non-naval expenditures or arrears.
3. Peninsular naval **share** may fall even when war continues.
4. Navy/Army/debt interest as distinct time series plus colonial defense expenditure and London/Cádiz transport would be necessary to identify competition for fiscal resources.

Counter-case: In 1785–89 Cádiz Indies+Rentas proxy was 108.15% of *peninsular naval expense alone*, but this tells us nothing about total imperial costs or later regime exit. The 1802–04 return of direct remittances (M2) also contradicts a monotonic insolvency narrative.

## 7. Raw dataset access path and status (study 3104)

- UKDS study **3104**, *European State Finance Database; Spanish Revenues and Loans in the Eighteenth and Early Nineteenth Centuries*, DOI https://doi.org/10.5255/UKDA-SN-3104-1
- Public metadata/codebook https://doc.ukdataservice.ac.uk/doc/3104/mrdoc/pdf/guide.pdf
- Public records describe the data as available to **registered users under an End User Licence Agreement**, not unrestricted anonymous reuse. UKDS instructions: https://ukdataservice.ac.uk/help/access-policy/frequently-asked-questions-faqs-about-how-to-get-data-and-our-access-policy/
- **g104spd3.tab** (24 Madrid 1784–1807 annual rows, 16 variables) still **NOT_ACQUIRED**; no user authenticated data-access action or bypass attempted. The previous M2 reconstruction is a legitimate **different published source**, not an excuse to mark raw 3104 as verified.
- The codebook's CHKTOT vs MREVTOT conflict, INDIES/LOANS blend, MREGION missing years and accounting-year scope still require real source row audit.

## 8. Audit matrix and single next action

| Check | Status |
|---|---|
| Barbier Table II, III, IV visually inspected from publisher's legal preview | PASS |
| 1784–1805 annual Barbier numbers summarized into 5 derived spending windows | PASS (arithmetic; originally published secondary archive-derived evidence) |
| Five-year Cádiz comparison for 6 windows recomputed with its structural 1778 definition break | PASS (arithmetic, descriptive only) |
| Marichal 1997 definition vs Prados 2024 Table 6.2 compared at 1791 and 1802 | SOURCE_TEXT_CHECKED (Marichal PDF screenshot blocked) |
| Independent audit of original Spanish treasury manuscripts | NOT_RUN |
| Year-by-year military/Army/debt-interest/borrowing reconciliation | NOT_ACQUIRED / NOT_RUN |
| Naval-interest causal crowding-out or Empire-wide net ROI | NOT_RUN |

**Single next action:** request authorized UKDS study 3104 access and obtain g104spd3.tab (if denied, document access outcome), then reconcile matched Madrid receipts (CHKTOT vs MREVTOT), debt/extraordinary classification and year boundaries against published 1984 expenditure and 2024 revenue; continue seeking annual debt-interest and Army outlays. Keep Draft PR / Issue OPEN; do not claim original treasury verification or net colonial profits.
