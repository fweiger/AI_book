# CASE-NLD-001 | M2 source and provincial-finance audit | 2026-11-14

**Authority** [AI_book #33](https://github.com/fweiger/AI_book/issues/33) · Existing [Draft PR #37](https://github.com/fweiger/AI_book/pull/37) · M2 **PARTIAL**, not a finished VOC ledger reconstruction.

## A. Findings that change previous inference

**A1. The two VOC cumulative totals are not independent confirmations.** The 1992 English Nationaal Archief introduction's Chapter 1 is explicitly authored by F. S. Gaastra (PDF pp.3–4), and the differing printed 1997 Table 1 is also by F. S. Gaastra. Thus the M1 conflict (1640–1700 equipage f370m vs f465.7m from 1997 decade sums) is a **same-author, cross-publication discrepancy**, not a clean disagreement between independent historians. Other 1700–1795 differences remain open. Links: https://www.nationaalarchief.nl/sites/default/files/afbeeldingen/toegangen/NL-HaNA_1.04.02_introduction-VOC.pdf ; https://dutchaustralianculturalcentre.com.au/wp-content/uploads/2026/04/Gaastra-VOC-Australia-4155533235.pdf

**A2. An independent 1986 scholarly review identifies a currency-conversion error in De Korte (1984).** J.J. Steur, *BMGN* 101(2), printed pp.238–239, says return goods were converted from the Asian 'light money' to 'heavy money' rather than to Dutch value, making gross-trade profits and ratios in table 26 for **1660–1770** too high. The review documents ducaton accounting standards: 97.5 stuivers (light), 78 (heavy, from 1743), 66 (Dutch, 1768). **Do not apply a blanket percentage correction** without seeing every original account/period and currency description. DOI https://doi.org/10.18352/bmgn-lchr.2706 ; readable review https://bmgn-lchr.nl/article/download/URN%3ANBN%3ANL%3AUI%3A10-1-102938/1134/1211

**A3. Historic bookkeeping is not modern GAAP.** Steur points out that VOC 'staat' is not a modern balance sheet including equity, and cautions against labeling all dividends irrational, since paying dividends could support short-term credibility. Thus current H4 corporate-governance explanation should be **CONTESTED**, not accepted.

## B. Newly reproduced provincial government expenditures (not VOC)

W. Fritschy, *Economic History Review* 56(1), 2003, table **A1 on printed p.82**, provides annual reconstructed Holland province `war expenditure`, `interest burden`, `other expenditure`, total for 1603–1652, 50 consecutive observations. The 50 rows are retyped in [holland_fiscal_annual_1603_1652_m2.csv](holland_fiscal_annual_1603_1652_m2.csv), plus 1701/1750/1794 interest observations from printed p.77 [Table 4](holland_interest_anchors_m2.csv). Source DOI https://doi.org/10.1111/1468-0289.00242. Printed Table A1 uses italics/bold to distinguish estimates vs primary-account observation. **Our digital reconstruction does not preserve that per-cell style; all rows are marked SCHOLARLY_RECONSTRUCTION_MIXED_ESTIMATES** until that finer classification is coded.

| Year | War expenditure f | Interest f | Total f | Interest/total |
|---|---:|---:|---:|---:|
| 1603 | 5,184,947 | 833,100 | 6,618,047 | 12.59% |
| 1620 | 5,617,118 | 1,550,622 | 7,767,740 | 19.96% |
| 1630 | 11,005,421 | 3,295,675 | 15,205,421 | 21.67% |
| 1640 | 10,733,002 | 6,045,720 | 17,278,722 | 34.99% |
| 1648 | 10,407,827 | 6,795,073 | 17,702,901 | 38.38% |
| 1652 | 8,654,710 | 6,883,884 | 16,027,905 | 42.95% |

**Crucial negative case to simplistic crowding-out**: between 1603 and 1648, annual interest share rises from 12.59% to 38.38%, while reconstructed war expenditure rises from f5.18m to f10.41m. This does not rule out resource constraints but **refutes the logical shortcut "interest rises => war expenditure necessarily falls"**. These are nominal values in one province, not real national naval spending and not causal proof. Author specifically excludes revenues collected by the separate Admiralty boards from her provincial account discussion.

**Transcription QA**: all 50 years present consecutively; each row published `total` compared with sum of war+interest+other, max residual <=1 florin due to source rounding/printing. Each ratio recomputed from published denominator. Outlier residuals (if any) remain recorded as a numeric field instead of overwritten. Researcher's estimates are common.

**Table 4 sample** for 1701, 1750, 1794 is placed in a **separate file** because it is interest paid by provincial tax receivers and its geographic sublabels require cross-check before merging with the 1603–1652 Table A1 government expenditure series. They are not guaranteed same population or denominator.

## C. Source availability / exact archive chain

- **National Archives VOC 1.04.02 primary catalogue read**, actual account pages **NOT_ACQUIRED**. Six-chamber consolidated summaries `generale staat`: Amsterdam from 1642 inv. **4583**, collective `generale staat` summaries from 1662 inv. **4584–4597**. Journal and ledgers: Amsterdam chamber after 1700 inv. **7143–7168**, **7170–7194**; balance extracts **7195–7204**. Source https://www.nationaalarchief.nl/onderzoeken/archief/1.04.02/beschrijving/content_and_structure ; important: aggregate 'generale staat' compiled from SIX chamber books, not a modern consolidated group P&L; archive notes missing early accounts and decentralized bookkeeping.
- **De Korte 1984 source**: Bibliographic record `xiv,95,[70]pp.`, ISBN 9024721083, 14 appendices per 1986 review; full book, account appendix 1/10/11/13 **NOT_ACQUIRED**. Review indicates Table 26 currency error, so obtaining this book alone does not resolve validity without conversion correction.
- **Huygens institute `Gewestelijke Financiën 1572–1795`**: catalog and coverage confirmed for Holland, Utrecht, Friesland, Zeeland, Groningen, Overijssel, Drenthe; Gelderland omitted for source gaps, Staats-Brabant omitted for access/completeness reasons. Source amounts in **historical Holland guilders**, caution about diverse, lacunose registers. Actual `resources.huygens.knaw.nl/gewestelijkefinancien` returned **HTTP 403** in tool; data files **NOT_ACQUIRED**. https://www.huygens.knaw.nl/resources/gewestelijke-financien-ten-tijde-van-de-republiek-der-verenigde-nederlanden-1572-1795/
- A 2009 student essay reproduces 17 grouped observations of Asia `expenses/income/loss` credited to Gaastra/de Korte, but original source not checked and some row arithmetic is inconsistent (e.g., f81.8m−f70.0m = f11.8m, but printed loss says f11.0m). **Not accepted as an original VOC ledger; use ONLY as a source-discovery lead**, not a source of verified yearly profits. https://www.pastmasters.org.au/uploads/2/6/7/5/26751978/voc_wesel_etc_logs.pdf

## D. What remains falsifiable

- **Mechanism H1** Asia territorial admin burden rising: original Asia military/admin expense disaggregation and corresponding intra-Asia sales **NOT_ACQUIRED**.
- **H2** 1780 war liquidity break: pre-war anticipation credit is real but annual auction proceeds/shipping loss/credit and debt interest **NOT_ACQUIRED**. The 1780–1790 period does not isolate 1780–1784 treatment.
- **H3** Colonial maritime rent vs investment and fiscal state: Fritschy's 1603–1652 annual Holland province series is a *different accounting owner and 100+ year older* negative case, not comparable to VOC cash flow without bridge and same-year data.
- **H4** Governance dividends: contested by Steur 1986; conditional hypothesis.
- **H5** Relative industrial adoption: Dutch/English wages-coal prices and machine adoption panel still missing.

**Current formal statuses**: Table A1 1603–1652 PDF source-to-CSV and arithmetic validation `PASS_PARTIAL`; Table 4 provenance `SOURCE_REVIEWED_NOT_JOINED`; VOC 1640–1700 conflict `OPEN`; original 1750–1800 VOC yearly ledgers `NOT_ACQUIRED`; Huygens raw panel `BLOCKED_HTTP_403`; true VOC net P&L, empire ROI and causal model `NOT_RUN`.

**Unique next action**: obtain exact De Korte 1984 appendix scans or Nationaal Archief 1.04.02 `generale staat` images for 1771 and 1781, document currency regime per account line, then reconcile the f370m/f465.7m discrepancy; only subsequently estimate fiscal/war effect with same-year denominators.
