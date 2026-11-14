# CASE-ESP-001 M2d session, 2026-11-14 | Banco de San Carlos sovereign exposure

**Task** https://github.com/fweiger/AI_book/issues/32 | Draft PR #36 (same branch).

**Asked**: Recover actual 1807 bank balance-sheet evidence and test whether bank-government exposure and interest arrears are reconciled.

**Inspected**: Banco de España 1994 official scholarly book I.1 published balance (source line + notes), Fundacion BBVA 2005 historical statistics Table 9.8 and publisher metadata, Banco de España Rafael Moreno Fernández 2010 p.130 (different government claim), Banco de España 2017 footnote 4 reales/peseta, Banco de España official Historical Archive Section17 inventory and digital-image request form. Internet PDF screenshot attempts for full 1994/2005/2010 books TIMEOUT; searchable source table text used. No original physical ledger accessed.

**New substantive results**: 1994 Banco book has 1807 year-end assets 313.4m nominal reales, gross claim to Crown 217.3m (69.34%), cash 9.3m of which only 1m metallic (0.32% assets), dividends in arrears 40.1m. FBBVA 2005 Table 9.8 has 23 observed years 1784–1808 (1792–1793 missing), allowing 6 novel grouped windows. 1784–89 royal claim share 12.11% across reported year-end balance snapshots vs 68.84% for 1805–08, descriptive. Both 1994 and 2005 depend on Tedde (1988), so agreement NOT independent primary replication. 2010 Banco study instead describes 1807 Crown debt 41.6m normalized pesetas (166.4m reales=53.10% same total assets) vs 217.3m; 50.9m gap unresolved. 1994 cash 9.3 vs FBBVA 2005 cash 9.2 also disagree by 0.1m.

**Original source locator**: AHBE Section17 books of accounts including Inventarios y Balances, code ES.28079.AHBE/01.17 is a series-level, NOT item-level signatura. Digital request form requires ID, email and exact item reference. Not submitted; must first obtain exact 1807 libro mayor/interest account references.

**Artifacts**: M2D_BANK_SOVEREIGN_EXPOSURE_AUDIT_20261114.md; bank_concentration_windows_m2d.csv; bank_1807_balance_diagnostics_m2d.csv; source_registry_m2d.csv; this session; README and CHANGELOG.

**Checks**: historical bank share and cash ratios computed from published values, 1994 balance 313.4=217.3+9.3+86.8 and 313.4=240+40.1+33.3, bank 2010 normalized currency 41.6*4=166.4, gap 50.9; 1992/93 missing in reference series not imputed.

**NOT_DONE**: original 1807 bank ledger, PDF screenshot reconfirmation of full balance, UKDS g104spd3.tab, 1811 government-debt to 1807 bank claims reconciliation, matched cash paid coupons and military cost, causal bank credit crowding-out.

**Single next action**: ask Banco de España Histórico for exact 1807 Bank San Carlos account-book/signatura (Inventario/Balance, Cuenta Real Hacienda, Intereses atrasados) then obtain authorized digital scans; perform liability/interest-class reconciliation with 1808 Cortes inventory. No signed conclusion before this.
