# CASE-ESP-001 — M2 年度财政与对外贸易的已发表重建数据复算（1778—1820）

Date: 2026-11-14 | Canonical Issue https://github.com/fweiger/AI_book/issues/32 | Existing Draft PR https://github.com/fweiger/AI_book/pull/36

**Status:** PUBLISHED_ANNUAL_RECONSTRUCTION_ACQUIRED; DESCRIPTIVE_CALCULATIONS_PASS; ORIGINAL_ARCHIVAL_LEDGER_NOT_ACQUIRED; CAUSAL_ESTIMATION_NOT_RUN.

## 1. Provenance and licensing

Leandro Prados de la Escosura, *The Loss of the American Empire*, in *A Millennial View of Spain’s Development*, 2024, ch.6 pp.239–275, https://doi.org/10.1007/978-3-031-60792-9_6 . Original chapter is openly licensed CC BY 4.0: https://creativecommons.org/licenses/by/4.0/ .

Published Tables 6.2 and 6.4 contain respectively 43 annual observations of Spanish Treasury receipts and exports/re-exports, 1778–1820. This project has reformatted and derived shares from these tables:
- [fiscal_annual_prados_1778_1820_m2.csv](fiscal_annual_prados_1778_1820_m2.csv)
- [trade_annual_prados_1778_1820_m2.csv](trade_annual_prados_1778_1820_m2.csv)

Reconstructed publication data are NOT handwritten archival records; published fiscal Table 6.2 references Merino (1987). Published trade Table 6.4 is reconstructed from Fisher, Cuenca, other national trade sources and geographic-share estimation. Original author/source and license retained; amendments are standardized CSV columns, segmentation, derived percentages and quality flags.

## 2. Accounting definitions and identification limits

- Treasury Table 6.2: **million current reales** and separate estimates in **1808-price reales**. Indies remittances to the peninsula are NOT New Spain local treasury total, mining output, private silver flow, total imperial profits, or fiscal transfers to other colonies. Customs and Indies receipts must remain separate even if grouped as external revenues. Total receipts are not automatically ordinary sustainable taxes; loan and debt-interest components are not isolated by this table.
- Trade Table 6.4: **million current reales**, domestic Spanish manufactured/agricultural product exports and **re-exports of foreign products** classified by Hispanic America vs other markets. Exports are NOT direct royal tax receipts.
- Crucial reconstruction assumption: geographic trade shares from **1792** are applied to **1778–1807**, and shares from **1827** are applied to **1808–1820** (the author's Appendix A.1); this imputation limits pre/post 1808 causal comparisons.
- Original fiscal values are rounded to integer million reales: preserve published aggregates even if they differ by 1 or 2 from the sum of rounded components. Do not silently overwrite totals.

## 3. Descriptive calculations independently reproduced from two CSVs

Period mean = sum(series)/n years. Aggregate share = sum(numerator)/sum(denominator). Nominal series; all means in **million current reales/year**.

| Window | n | Indies remittances mean | Treasury total mean | Indies share of total | Spanish domestic exports to America mean | American share of Spanish domestic exports |
|---|---:|---:|---:|---:|---:|---:|
| 1784–1792 | 9 | 85.56 | 741.44 | 11.54% | 205.11 | 36.25% |
| 1793–1796 | 4 | 178.50 | 1650.75 | 10.81% | 218.25 | 34.93% |
| 1797–1801 | 5 | 47.20 | 1818.60 | 2.60% | 54.40 | 11.18% |
| 1802–1804 | 3 | 268.00 | 1309.67 | 20.46% | 279.67 | 29.69% |
| 1805–1807 | 3 | 31.33 | 1155.67 | 2.71% | 43.67 | 7.72% |
| 1815–1820 | 6 | 0.00 | 1103.67 | 0.00% | 106.00 | 20.74% |

Observations and logical consequences:
1. Compared with 1784–1792, the 1797–1801 mean Indies remittances fall **44.83%** and mean domestic exports to America fall **73.48%**. War-era maritime and commercial disruptions are plausible, NOT causally isolated.
2. Both series rebound strongly during 1802–1804 (Indies mean **268m reales/year**, America domestic exports **279.67m/year**). Hence the stronger claim of an *irreversible* annual collapse beginning in 1797 is **refuted by the published table**.
3. Both series return to low values in 1805–1807. The 1802–1804 window is **transitional**, not uniformly peaceful: war resumed in 1804.
4. The 1815–1820 source fiscal entries report **zero Indies remittances**, but annual average Spanish domestic exports to Hispanic America remain **106m reales**. Political fiscal control and goods-market access are distinct; this does not imply every mainland colony was already independent by 1815.

Sanity check: 1791 Indies remittance 161 / Treasury total 800 = 20.13%, consistent with the author's narrative 'about 20%'. 1802 annual Indies value = 350m reales (a rebound outlier), not to be smoothed away.

## 4. Exploratory correlations, not causality

Across the aligned 1784–1807 annual series, Pearson correlation between Indies remittances and America-directed Spanish domestic exports = **0.6363** (n=24). Subperiods: 1784–1796 **0.0599** (n=13), 1797–1807 **0.8921** (n=11). Subsample instability, shared war conditions, price shocks, timing lags, non-random port closures, and source estimation prevent interpretation as causal coefficients. No significance test or regression/parallel-trends test has been claimed.

**Accounting break in 1808**: the source reports government total receipts as 0 and customs 1; this is NOT evidence that the entire Spanish state literally had no income. Treat 1808 as war-driven structural account coverage change, not a normal data point. It was excluded from the descriptive window averages.

## 5. Competing mechanisms

| H-ID | Descriptive support | Strong alternative / falsification | M2 status |
|---|---|---|---|
| ESP-H1 wars, naval disruption and lost remittances cause fiscal fragility | Co-movement during 1797–1801 and 1805–1807; rebound 1802–04 | Ordinary tax, borrowing, expenditures and real shipment timing unobserved; Treasury totals do not test debt-interest displacement | DESCRIPTIVE_SUPPORT_ONLY |
| ESP-H2 reforms increase tax capacity and weaken elite allegiance | Separate Chiovelli et al. (2025) 79-treasury working-paper regressions | Local Indigenous protest can decline; treatment timing/selection/attrition | LITERATURE_ONLY / NOT_REPLICATED |
| ESP-H3 colonial riches fail to induce manufacturing | Export market repeatedly disrupted | Catalonia shows non-zero textile capacity; relative wages and energy inputs missing | NOT_TESTED |
| ESP-H4 1808 legitimacy crisis triggers decolonization | 1808 structural break and later fiscal remittances vanish | Multiple wars, heterogeneous local political movements and changes in central accounting overlap | CAUSAL_NOT_IDENTIFIED |
| ESP-H5 independent colonies cease all Spanish trade | Post-1815 American domestic exports remain positive | Political sovereignty and commercial access are distinct | STRONG VERSION REFUTED |

The 2024 chapter explicitly notes that the economic effects of independence are hard to separate from the wars with Britain/France and the Napoleonic invasion, and evaluates the long-term total economic impact as potentially less than previously assumed.

## 6. Verification/limitations, exact next action

- **PASS (source transcription / internal arithmetic)**: 43 distinct consecutive 1778–1820 year rows in each published reconstruction CSV; both 1778–1820 tables read back from GitHub; component sum discrepancies within two million due to rounding; matching years; computed 6 period-window summaries and exploratory correlations.
- **NOT_ACQUIRED**: UK Data Service ESFDB Spain study 3104 underlying Madrid dataset g104spd3.tab (1784–1807); El Colegio de México NE.zip; original Archivo General de Simancas manuscripts; consistent annual military spending and debt-interest/borrowing ledger.
- **NOT_RUN**: original manuscript audit, donor-recipient remittance reconciliation, borrowing-cost and military crowd-out tests, inference on causal impacts, independent historical peer review.
- Renate Pieper, *La aportación americana a la Real Hacienda española en la segunda mitad del siglo XVIII*, accessible university text highlights accounting and transport-risk caveats: https://ebuah.uah.es/dspace/bitstream/handle/10017/5766/La%20Aportaci%C3%B3n%20Americana%20a%20la%20Real%20Hacienda%20Espa%C3%B1ola%20en%20la%20Segunda%20Mitad%20del%20Siglo%20XVIII.pdf?isAllowed=y&sequence=1 . PDF screenshot access was blocked in this session; do **not** claim independent full-table visual audit.
- **Single next action**: Obtain permissible UKDS g104spd3.tab; compare its 24 annual records to this published reconstruction while explicitly resolving CHKTOT vs MREVTOT, 1806/07 MREGION missingness, and Indies/Loans tax–debt mixing. If source access requires registration or license, record the blocker and do not substitute invented annual data.
