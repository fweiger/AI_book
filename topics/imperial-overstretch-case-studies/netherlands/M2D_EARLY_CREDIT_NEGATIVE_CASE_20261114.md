# CASE-NLD-001 | M2D Early finance liquidity negative case and fiscal direction | 2026-11-14

Authority: [AI_book #33](https://github.com/fweiger/AI_book/issues/33), existing Draft PR #37. M2 PARTIAL: no original 1780 annual VOC ledgers obtained, no causal model run.

## Sources actually read / not read
- Directly read and visually inspected Oscar Gelderblom, Abe de Jong, Joost Jonker (2012), The Formative Years of the Modern Corporation: The Dutch East India Company VOC, 1602-1623, ERIM working paper: printed pp9-15 and pp50-51 (including Table C). Source https://repub.eur.nl/pub/32952/ERS-2012-007-FA.pdf
- Rechecked Nationaal Archief Van Ghesel official finding aid 1.10.31 printed p10: original inventory 15, 17, 19; actual historical ledger/charter subsidy pages NOT_ACQUIRED. Source https://www.nationaalarchief.nl/onderzoeken/archief/1.10.31/download/pdf
- 1872 Kroniek volume 27 page scan located at DBNL, PDF ~52 MB exceeds web extraction limit; printed page 15 and 40-41 financial numerics NOT_READ. Source https://www.dbnl.org/tekst/_kro004187101_01/downloads.php

## Early VOC financing, costs, and state-company directions
See [voc_early_credit_fiscal_events_m2d.csv](voc_early_credit_fiscal_events_m2d.csv), 7 distinct observations; all historical nominal guilders, tagged by accounting owner/recipient and evidential qualifier.

| Period | Amount (guilders) | Correct financial treatment |
|---|---:|---|
| 1606, spread over up to 3 years | 300,000 | Zeeland States approved customs-financed grant to VOC for overseas forts/garrison. NOT single-year cash disbursement; NA 1.04.02 inv 11046 cited by authors. |
| First half 1608 | approx 500,000 | Amsterdam VOC chamber increase in short-term debt, a change, NOT six-chamber total balance. |
| 1609 | >400,000 | VOC annual company military cost estimate, including wages/food/maintenance/depreciation, not Holland province military budget. |
| 1609-1612 | 390,000 | States-General awarded tax relief for VOC; cash subsidies and tax expenditures must be distinct. Extra in-kind ships and ordnance unpriced. |
| July 1610 | 400,000 | Amsterdam-to-Zeeland inter-chamber current account overdraft; it is NOT additional consolidated VOC external debt. |
| 1610-1612 | 10,400,000 | Dividends awarded, not full cash dividends paid; company frequently used commodities in kind. |
| Dec 1606–Jul 1608 | 130,000 | Zeeland chamber costs when ships returned, including wage arrears and storage; not VOC total costs. |

**Fiscal double-entry finding:** the different government entities (Zeeland Estates, States General) and accounting event types (grant authorization vs tax exemption) prevent adding 300000+390000 as cash cost to the central Dutch government.

**Countervailing fiscal direction newly located:** Nationaal Archief Van Ghesel 1.10.31 inventory 17 describes a list of VOC payments to the state for charter grants and repeated renewals from 1602-1748 (printed partly in 1872 Kroniek p15); it is COMPANY_TO_STATE, distinct from those early STATE_TO_COMPANY examples. Actual inventory 17 numerics NOT_ACQUIRED. Inventory 19 lists VOC dividends up to 1770: possible audit of awarded vs paid dividend amounts; not read. See [voc_fiscal_direction_archives_m2d.csv](voc_fiscal_direction_archives_m2d.csv).

## 1611-12 six-chamber commissioned sales table, reproduce and audit
Gelderblom et al. (2012) printed p51 Table C gives VOC company sales TURNOVER inferred from directors commissions for July 1611 to early September 1612, drawing on NA 1.04.02 inv 11349 Zeeland copies of accounts.

| Chamber | Printed guilders | Percent |
|---|---:|---:|
| Amsterdam | 2,935,455 | 51.4% |
| Zeeland | 998,050 | 17.5% |
| Enkhuizen | 10,543 | 0.2% |
| Rotterdam | 505,068 | 8.9% |
| Delft | 776,582 | 13.6% |
| Hoorn | 479,876 | 8.4% |
| Published Total | 5,705,573 | 100% |
| Our six-row sum | 5,705,574 | 100% |

**Audit residual: +1 guilder.** Keep all published entries and reported overall total untouched; do not silently fix this very small table arithmetic discrepancy. Data in [voc_1611_1612_commission_sales_m2d.csv](voc_1611_1612_commission_sales_m2d.csv).

More consequential conceptual difference: printed p50 states commission-based reported 5.7 million turnover likely includes returning-vessel back-pay and associated costs. The authors subtract an ESTIMATED 6 ships × 85,000 guilders = 510,000 guilders, obtaining around 5,195,573 guilders (about 5.2 million) as adjusted sales. This is not verified cash actually received; the adjustment is an author's modelling assumption. The same study shows that goods treated as sold could in fact be delivered as in-kind dividends or inter-chamber movements, and unsold stock did not pay immediate creditors.

## Implications for the main 1780 question and negative cases
- Mechanism exists as early as 1606-1612: military spending, slow return-ship cycle, short-term financing, government support, in-kind dividends, internal chamber credit. Yet VOC continued for roughly two centuries. Presence of these factors alone cannot be a sufficient condition for 1780s collapse.
- This is not an identification strategy to conclude the 1780 war was unimportant. Credit-market depth, product mix, British sea power, corporate obligations, and state fiscal capacity changed dramatically.
- For 1780 causal work, define *separate* budget_authorized, cash_disbursed, tax_relief_awarded, intra_company_overdraft, company_external_borrowing, commission_turnover, cash_auction_proceeds, dividends_declared, dividends_paid_cash/in_kind.
- Do not mix 1608 Amsterdam-chamber 0.5m borrowing increase with 1780 VOC company total debt lower-bound 29m in a common debt line graph.
- Source conflict 1640-1700 equipage 370m vs 465.7m remains OPEN. NA Van Ghesel inv15 1640-1770 and the 1872 Kroniek pp40-41 original extracts still NOT_ACQUIRED. The NA 4596/4597 1780 ledgers and de Korte Appendix 14 still NOT_ACQUIRED.

## QA / next action
Six chamber rows, seven independently classified finance facts and six archive locator rows; source IDs and URLs registered. Recomputed chamber sum 5,705,574 vs printed 5,705,573 (residual +1). Author estimate 5,705,573 - 6×85,000=5,195,573, not cash flow. Internal debt not summed into company debt. This is a working-paper numeric transcription, NOT independent primary-ledger replication or independent peer review.
Next sole priority: acquire a readable Van Ghesel original inventory 15 or 1872 Kroniek pp40-41 for 1640-1700 equipage reconciliation, and actual NA VOC 1.04.02 inventories 4596/4597 or de Korte financial appendix 14 for 1780-84 company debt and debt-maturity structure.

## Explicit validation statuses
- CSV shape/source foreign keys/recomputed turnover arithmetic: `PASS` (mechanical; does not verify archives independently).
- Original archival account pages `1.04.02/11046`, `1.04.02/11349` and Van Ghesel `1.10.31/15`, `/17`, `/19`: `NOT_ACQUIRED`.
- Source conflict (1640–1700 equipage 370m vs 465.7m): `OPEN`.
- Government commitment vs actual payment reconciliation: `NOT_RUN`.
- 1780–84 VOC original annual debt reconstruction, statistical causal testing and external historian review: `NOT_RUN`.
