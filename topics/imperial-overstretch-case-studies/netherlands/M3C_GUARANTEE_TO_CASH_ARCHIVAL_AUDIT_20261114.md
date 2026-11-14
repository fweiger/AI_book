# CASE-NLD-001 | M3C original archival fiscal bridge: guarantees vs actual outlays | 2026-11-14

Canonical issue https://github.com/fweiger/AI_book/issues/33 and original Draft PR #37, branch topic-010/case-nld-001-netherlands-20261114. **This phase reads official Nationaal Archief finding-aid editorial descriptions, NOT original 1793 payment vouchers or company journals.** Historical causal testing NOT_RUN.

## 1. The strongest new concrete fiscal observation: emergency cap ≠ issued state money
Nationaal Archief [3.02.33 topical appendix index, §5 *Geldbehoeften van de VOC en financiële steun van de provincies*](https://www.nationaalarchief.nl/onderzoeken/archief/3.02.33/beschrijving/appendices) precisely locates the 1793 failed f4m corporate loan negotiation, Holland States' temporary emergency financial resources for its chambers **initially up to f2m, later up to f4m**, and says that the **actual issuance through the Gecommitteerde Raden was NOT MORE THAN f500,000** in records Feb18–Jun28 1793. Exact archival papers: `inv18/142A,144,146,147; inv19/153,161`.

**Arithmetic / accounting guardrail:** at most f500,000 relative to revised stated maximum f4m is an **upper-bound 12.5% of maximum facility size**, **not** a validated drawdown rate on a legally appropriated fully funded f4m line. Actual cash may be less and original individual voucher dates and receivers are not read. The initial f2m and revised f4m refer to same facility: **NEVER add 2+4+0.5** or treat 4m as state expenditure. This is an archival editor's explicit 'daadwerkelijke uitreiking ... niet meer dan ƒ 500.000' synopsis, stronger than a pledge-only secondary narrative but not direct double-entry verification.

## 2. Long-lived debt maturity refinancing, not additive new flows
- Same catalogue `inv11/SSS; inv12/5; inv13/28–30` identifies a new 1791 guarantee-related f5m company debt negotiation to address mandatory **December 1791 repayment of the proceeds of an earlier f5m funding operation by Holland for VOC under States resolution of 5 December 1783**. Treat both as **one rollover family R83-91**, not f10m fresh cash. Exact realized gross proceeds of either 1791 negotiation, creditor identity and remaining principal NOT_ACQUIRED.
- Catalogue `inv5/R,S,T; inv10/CC,LL,OO,YY; inv11/QQQ` describes negotiations of **f10m bonded borrowing under Holland+Zeeland guarantee around 1790–1792**, alongside proposed conversion of still outstanding pre-1781 anticipation-money receipts to guaranteed obligations. This is **issuance/guarantee/refinancing documentation**, not proof of f10m direct fiscal expenditure.
- `inv18/128,129,131` traces **f4m** 1792–1793 attempted guaranteed funding; source's 1793 emergency shortage note refers to its **failure**. Later 1793–1794 exchange-bill facilities, Zeeland requests for a f6m total (not an incremental 6m) and extension of a former f4m by f3.5m are later financial structures, not new state cash by definition.
- 1794 director request for at least f1.5m recepissen in exchange for an **equal amount of already-approved bills** is a proposed paper-to-paper swap, not f1.5m of fresh public funds.
- 1795 state committee materials concern **400 bills still unsigned and undebited**, related to 1794 f3.5m expansion; 400 is **number of bills, not guilders** and not proof of their payment.
- 1795 proposed supplier bill financing up to f1.2m under provisional Holland guarantees is a **maximum guarantee amount**, no demonstrated actual cash.

Detailed 16-financial-observation ledger: [voc_1790_1795_guarantee_cash_bridge_m3c.csv](voc_1790_1795_guarantee_cash_bridge_m3c.csv). The fields separate `facility_family`, `reported_amount`, `qualifier`, `stock vs refinance vs issuance`, with nulls where actual receipts missing. **Do not total** the rows; many refer to same liability or revised cap.

## 3. Monthly VOC accounts: stronger route to a 1790–1794 company cash-flow panel
The same authoritative archive index §11 lists *Maandstaten van inkomsten en uitgaven van de afzonderlijke kamers, 1790–1794*: **all six original VOC chambers** Amsterdam, Zeeland, Delft, Rotterdam, Hoorn, Enkhuizen, separately by interval with precise annex labels. We catalogued **19 chamber × available-window entries** in [voc_1790_1795_six_chamber_monthly_source_windows_m3c.csv](voc_1790_1795_six_chamber_monthly_source_windows_m3c.csv).

Examples: Amsterdam June–Nov 1790 `inv6/U`, Dec1790–Dec1792 `inv6/U1`, Jan1793–Oct1794 `inv8/U2`; Zeeland same initial `inv6/U`, later `inv6/U2` and `inv8/U2`; Hoorn/Enkhuizen include 1793–1794 `inv9/U2`. **Annex labels can be shared by many chambers**: they are distinct account contents, not 19 distinct physical volumes and not 19 complete calendar years.

**Critical small catalogue corruption:** Rotterdam last listed 1793 period ends in the source text `179 dec.` without year; M3C CSV leaves end empty and records `END_YEAR_TRUNCATED_AS_179_DEC_IN_FINDING_AID`; do not invent 1793-12 end. The catalogue includes a lone Rotterdam January 1795 sheet `inv14/60`, outside main 1790–94 scope; kept separately.

These are **monthly reported income/outlay statements**, not automatically paid/received bank transactions. Externally check forecasts (*calculatieve staten*) vs realized monthly accounts and same-year chamber transfers before consolidating. All monthly figures `NOT_ACQUIRED`, so no synthetic 1790–94 panel is claimed.

## 4. Critical extra original-document sources that can resolve much of M2–M3
The new thematic index has much more precise **original** archive targets than generic archive series:
- `3.02.33 inv5/J*,J`: Holland VOC chambers' expenditures for **1779–1790** and contemporary savings memo. This can bridge prewar expenses and postwar budgets, after original figures transcribed.
- `inv13/19A Litt.V app.B, printed pp215–218`: contemporary historical EQUIPAGE TABLE **1770–1771 through 1779–1780** (plus naval strength snapshot 15 Feb 1791 app.F p220), potentially resolve the same-publication 1770s '198m' vs Table1 '186.5m' conflict. Does **not** settle 1640–1700 original f370m vs f465.7m without different source.
- `inv13/19B Litt.Q1,Q2`: **Asian office-specific costs/profit/income 1786, 1787, 1788**, directly targets territorial-overhead model H2, but scope & exchange-rate rules must be checked.
- `inv17/115, inv19/151, inv20/181`: company **general financial states as at 31 May 1791, 1792, 1793**. These are potential VOC total *stock* snapshots, unlike six chambers' monthly *flows*.
- `inv24/701,705,769,821`: documents on VOC 1780–1794 debts and **causes** of those debts, important to reconcile 1760/1780/1784 later historical claims. Read original text to distinguish stakeholder perspective from actual accounting.
- `inv14/59`: **1790 Dec original Dutch-versus-English East Indiaman course/sailing-speed memos** by Nieuwland, Frijkenius and Kuvel, a contemporaneous check on Solar/de Zwart (2017) late navigation advantage.
- `inv17/121; inv19/154,175; inv20/183,188,193,205`: 1792–94 Zeeland director Radermacher's case for spijkerhuid rather than copperhuid, **actual historical alternatives to coppering**, not a modern author's inference alone.
- `inv24/893`: official archive footnote reports **Titsingh & Co private advance funded hemp needed to operate VOC yard in 1795**. No amount; private company cash ≠ Dutch state support, and the cited paper's content remains not directly read.

These high-priority items are in [voc_m3c_exact_primary_source_targets.csv](voc_m3c_exact_primary_source_targets.csv).

## 5. New original archive accessibility correction: BGB ledger duplicate and microfilm IDs
Directly reviewed the Nationaal Archief PDF inventory (J. E. Heeres 1893, current version 2022-09-16), **PDF screenshots printed pp9, 10, 13**: https://www.nationaalarchief.nl/onderzoeken/archief/1.04.18.02/download/pdf

- Batavia **general ledger `1.04.18.02 inv10735` (1779–1780), microfilm `2167.01`**, explicitly **IDENTICAL** to `inv10743` (1779–1780, microfilm `2167.09`). The two inventories must not be counted as independent identical 1779–80 company-year observations.
- `inv10736` (1780–1781): ledger microfilm `2167.02`.
- `inv10796` (1781–1782): journal microfilms `2182.6` AND `2183.1`.
- `inv10801` (1779–1780): journal microfilm `2184.2`.
- Official historic PDF expressly says **`Slechts raadpleegbaar op microfilm`** ('consultable only on microfilm') for these archive entries, although current HTML inventory calls them `DIGITALIZED` in places. Web viewer first image link returning HTTP404 does not override the restriction or prove original ledger digitization is available by public download. Need ask archive whether microfilm scans or viewing copies can be provided.

## 6. Evidence hierarchy, causal limits and precise next step
- Institutional official archive appendix descriptions `PASS_CATALOGUE_VERIFIED`, including actual-issuance **UPPER BOUND** and names/dates/locators; actual 1793 state cash vouchers, interest/refinancing and general states `NOT_ACQUIRED`.
- The 16-event table and 19 monthly-windows matrix are metadata/transcriptions of institutional archive summaries, **not** originals verified by reading the historical documents.
- 1793 ≤f0.5m vs revised facility ≤f4m is a **cap-to-cap upper bound**, not universal rescue execution rate; 1783 old 5m and 1791 refinanced 5m are potentially same principal; 1790 10m bonds, 1793 bills and 1795 unsigned bills might overlap; no all-in Dutch national aid total computed.
- All prior 1640–1700 M1 f370m/f465.7m source accounting discrepancy `OPEN` and 1780–84 original company debt entries `NOT_ACQUIRED`.
- Independent economic-history review, company/treasury consolidated fiscal panel and event-study causal estimates `NOT_RUN`.

**Unique next action:** obtain **original `3.02.33 inv18/142A,144,146,147` or `inv19/153,161`** to extract *actual* issued payments corresponding to ≤f500k vs f4m facility, plus **monthly statements `inv6/U,U1,U2; inv8/U2; inv9/U2`** across six chambers. Record paid date, voucher, recipient, government source, and cross-chamber transfer; only then compare with VOC `inv17/115`, `inv19/151` stocks and BGB separate Asian accounts. This route may deliver more relevant cash evidence than reattempting blocked 52MB 1872 volume.
