# Spain M1/M2 historical treasury data dictionary | 2026-11-14

Canonical issue https://github.com/fweiger/AI_book/issues/32 ; publication stage = draft / source verified partly / not an annual dataset.

## Distinct account owners and units

| Source | Accounting owner | Period / frequency | Monetary unit | Sample acquired? |
|---|---|---|---|---|
| Bank Central edited-volume Cuadro 8 | New Spain colonial royal treasury transfers | 1720–1799 decade average of annual flows | Historical pesos, nominal | PUBLISHED_TABLE_TRANSCRIBED |
| Tanck/Marichal historical estimate | New Spain colonial treasuries | approx 1780–1810 cumulative remittances | silver pesos, nominal | LITERATURE_REPORTED |
| ESFDB Spain g104spd3.tab | Madrid Treasury receipts (partial central Spanish state) | 1784–1807 annual, 24 records | thousands of reales de vellón | CODEBOOK_ONLY, DATA_NOT_ACQUIRED |
| ESFDB Spain g104spd2.tab | Spanish General Treasury revenue | 1788–1820 annual, net vs notional | millions of reales de vellón | CODEBOOK_ONLY, DATA_NOT_ACQUIRED |
| El Colegio de México NE.zip | New Spain royal cajas and tax lines | historical variable period rows | variable historical pesos; check each line | NOT_ACQUIRED |
| Chiovelli et al. (2025) Table 3 | empire-wide selected treasury-year panel | 1770–1799, fixed-effects model | log pesos de ocho revenue | PUBLISHED_ESTIMATE_ONLY |

Do not add, divide, or compare figures from these rows without explicit conversion, common geography, date alignment, consolidation, and treatment of remittances and loans.

## Required M2 clean panel schema

- source_file / original_archive / source_page / observation_id / raw_line_item
- treasury_id / receiving_treasury_id / historical_polity / modern_location / accounting_owner
- accounting_start_date / accounting_end_date / year / year_precision / frequency / date_allocation_method
- raw_amount / raw_currency / conversion_factor_source / harmonized_amount / harmonized_currency / nominal_or_real
- fiscal_category / loan_vs_tax / parent_transfer_flag / consolidation_group / is_carryover
- original_total / recomputed_total / mismatch_amount / mismatch_flag / missing_reason / evidence_status

Classification must maintain separate **ordinary_tax_revenue**, **extraordinary_donativo**, **gross_borrowing**, **deposit_and_guarantee**, **cash_remittance_from_colony**, **intra_imperial_situado**, **military_expenditure**, **debt_interest_payment**, **principal_repayment**, **debt_stock**, **mint_output**, and **private_trade** fields.

## ESFDB 3104 specifically documented rules

1. Madrid g104spd3.tab codebook: 24 annual observations / 16 variables, 1784–1807, amounts in **thousands** of reales de vellón.
2. Two sum fields MREVTOT and CHKTOT disagree outside 1789, 1792, 1793, 1795, 1800 and 1805. Preserve both; use CHKTOT only as **provisional source-recommended plotting total** and report difference annually. Do not silently overwrite original MREVTOT.
3. MREGION values 1806 and 1807 are missing; never impute zero. Regional surpluses to Madrid should be distinguished from taxation directly received at the center.
4. INDIES includes colonial-collected receipts, also colonial treasury borrowing and deposits. It is NOT identical to colonial tax transfers or fiscal profit. Peninsula-collected taxes on colonial trade are outside INDIES.
5. LOANS bundles metropolitan borrowing with donations, deposits and guarantees; source itself warns donation and deposit are not necessarily loans. Do not infer debt-stock changes directly from LOANS totals.
6. Source note specifies carryovers already eliminated from the 1981 aggregate. Keep a no-double-counting marker when using other series.
7. Cross-border **cash flows** (Madrid vs New Spain) may be in different years due to transit and reporting lag. Consolidation requires sender/receiver reconciliation; shared amounts must not be summed as new imperial receipts.

## New Spain source harmonization (2025 working-paper Appendix A, not reproduced here)

Original sources sometimes use **pesos ensayados** and **pesos de oro** while published harmonized data uses **pesos de ocho**. The authors' source-specific multipliers were 1.6544 and 3.1 respectively. They also allocate records spanning multiple months to years by proportional monthly splitting. Their chosen tax categories include loans/donations and remittances, so their **total revenue** outcome is a study-defined aggregate, not pure taxes. These conversions and definitions must be verified against underlying metadata before application elsewhere.

## Validation checklist and execution status

- [x] Two published remittance components add to source total for all eight 10-year rows, 1720–1799 (arithmetic in current research pass).
- [x] Source links present; frequency, units and owner documented in remittance_decadal_m1.csv.
- [x] MREVTOT / CHKTOT disagreement and MREGION missingness recorded from UKDS guide.
- [ ] Actual UKDS g104spd3.tab download and 24 annual-row integrity validation: NOT_ACQUIRED.
- [ ] Actual El Colegio NE.zip download and workbook validation: NOT_ACQUIRED.
- [ ] Original handwritten Simancas treasury account cross-check: NOT_RUN.
- [ ] National annual fiscal spending, debt interest, ROI or regressions: NOT_RUN.

Sources: https://doc.ukdataservice.ac.uk/doc/3104/mrdoc/pdf/guide.pdf ; https://realhacienda.colmex.mx/ ; https://www2.um.edu.uy/fcee_papers/2020/Bourbon_Reforms_State_Capacity_and_Revolution_in_the_Spanish_Empire.pdf ; https://museosdelbancocentral.org/wp-content/uploads/2022/03/Monedas-Medios-de-Cambio-y-Espacios-de-Circulacion-en-America-Latina-y-Espana-1500-1900.pdf
