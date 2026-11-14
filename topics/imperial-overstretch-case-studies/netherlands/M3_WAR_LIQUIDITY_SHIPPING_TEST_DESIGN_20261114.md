# CASE-NLD-001 | M3 competitive mechanism and war-shipping counterexample | 2026-11-14

**Authority:** [AI_book #33](https://github.com/fweiger/AI_book/issues/33) · existing [Draft PR #37](https://github.com/fweiger/AI_book/pull/37) · TOPIC-010 Four-Empire Comparison Protocol V1. **M3 DESIGN_ONLY + M3 PARTIAL DESCRIPTIVE COUNTEREVIDENCE**, NOT an event-study or independent historical peer review.

## 1. New independent scholarly quantitative reconstruction: Asia and Netherlands-facing shipping did not collapse in the same way
Matthias van Rossum (2013), *Werkers van de wereld*, Vrije Universiteit Amsterdam PhD, printed **p55 Table 2** and p56 methodological caveat; **actual PDF page55 screenshot verified**. URL: https://research.vu.nl/ws/files/42118941/complete%20dissertation.pdf

| Year | Intra-Asian VOC-owned fleet, July snapshot (tons) | Intra-Asian fleet incl chartered 1785 sample (tons) | Homebound VOC tonnage arrived Netherlands, full year (tons) |
|---|---:|---:|---:|
| 1780 | 29,747 | — | 19,680 |
| 1785 | 22,200 | 32,373 | 22,744 |
| 1790 | 25,355 | — | 21,165 |

- Recomputed: VOC-owned intra-Asian July tonnage **1785 vs 1780 -25.37%**; 1790 vs 1780 -14.76%. These are JULY STOCK reconstructions, excluding rented ships.
- Dutch homebound arrivals tonnage **1785 vs 1780 +15.57%**; 1790 vs 1780 +7.55%. These are YEARLY ARRIVAL-FLOW proxies, NOT ship inventory, traded value, European auctions or bank receipts.
- 1785 **32,373** includes rented vessels and ships absent from July musters; it is a special sampled inclusive number. It is **not comparable** with 1780 or 1790 owned-only snapshot. Do **not** claim that difference (32,373−22,200) is exclusively chartered vessels or infer a 1780–1785 inclusive-fleet growth rate.
- The author concludes that severe lack of intra-Asian vessel capacity after the Fourth Anglo-Dutch War is not well supported; this is a **strong descriptive objection to 'all VOC fleet capacity collapsed permanently'**, but not proof that overseas operation costs, war losses, realized trade, and European liquidity did not suffer.
- Van Rossum uses *Database Generale Zeemonsterrollen* for July intra-Asian fleet and *Dutch-Asiatic Shipping* for return arrival tonnage. The **datasets do not share the same measured object or timing**. Raw muster and voyage-level records NOT downloaded this turn. The source also notes missing July musters and single-year hired ship samples.

Machine-readable source-value table: [voc_war_shipping_tonnage_m3.csv](voc_war_shipping_tonnage_m3.csv). The original 2013 dissertation is a real new quantitative source not used in M0–M2F, but not a handwritten VOC account.

## 2. A deeper source-path break-through: Asian profits and debts were in original BGB journals but are *not in* the public cargo database
The Huygens Institute Bookkeeper-General Batavia (BGB) English methods guide directly states original General Journals NA **1.04.18.02 inv 10751–10801** (1700–1790) and Zeeland copies **10802–10809** (1771–1801) form **55 distinct book years**, not a continuous ~100-year panel. The 4 overlap years are 1771–72, 1774–75, 1776–77 and 1777–78. Source: https://bgb.huygens.knaw.nl/?page_id=40

Crucially, the original General Journals also contained **bills of exchange, stocks as of 31 August, office-specific profit, income and expenses**, but the digital public BGB project recorded **ONLY cargo lists and associated voyages**, not those non-cargo finance tables. Thus simply downloading BGB public cargo CSV would **NOT** deliver the 1780 wartime office net profit or credit series the project needs. Official inventory: https://www.nationaalarchief.nl/onderzoeken/archief/1.04.18.02

**Verified historical currency-regime warning from the official institution:**
- 1700–1743: BGB book values predominantly Indian **light** guilders.
- 1743: Heren XVII ordered switch to Dutch guilders, but Huygens says sampled books indicate order **generally not followed** during 1743–1768; some books 1762–63/1763–64 have mixed heavy/light denomination.
- In 1768 the directors repeated the order; afterwards clerks recorded Dutch **heavy** guilders.
- Therefore a hardcoded 1743 breakpoint as fully enacted is invalid, and the simple 1.25 multiplier cannot repair all periods without folio-level verification. Distinguish Asian price units from Netherlands equipage ledger definitions.
See [voc_bgb_currency_regimes_m3.csv](voc_bgb_currency_regimes_m3.csv), which has an **overlapping exceptions row** rather than treating the spans as a complete mutually exclusive year panel.

## 3. Original postwar *state* fiscal evidence collection newly located
The Nationaal Archief **3.02.33, Holland state committees for affairs of the VOC (1790–1796)** includes meeting minutes and many attachments for oversight of subsidies/guarantees made by Holland and Zeeland provinces. Catalogue labels many items `DIGITALIZED`, but actual scan page not opened. This can distinguish authorization, loan issuance, government guarantees, disbursement and state risk, particularly **after 1790**, not falsely as 1780 onset.
Official URL: https://www.nationaalarchief.nl/onderzoeken/archief/3.02.33

Source [voc_m3_primary_targets.csv](voc_m3_primary_targets.csv) separately maps NA `1.04.18.02` Asian financial books, NA `1.04.02` Amsterdam/Zeeland company balances, NA `3.02.33` state oversight, and NA `1.10.31` Van Ghesel physical 1640–1770 equipment ledger.

## 4. Five competing mechanisms, falsifiers and next raw variables
See the five-row [voc_m3_hypothesis_test_matrix.csv](voc_m3_hypothesis_test_matrix.csv).

1. **H1 War -> shipping/auctions -> cash -> short-debt liquidity:** predict sharp downturn in realizable European auction cash and refinancing after Dec 1780, not necessarily sustained destruction of intra-Asian fleet tonnage. Needs actual 1775–90 company cash, auctions, short-credit maturity and voyage/cargo.
2. **H2 Asian territorial overhead:** predict *same-owner same-money same-year* armed forces, garrisons and administration cost/Asian net trade returns deteriorates even **before** Dec 1780 and persists thereafter. Needs original profit/cost sections of BGB general journals and site-specific costs, which BGB cargo database omits.
3. **H3 Permanent physical fleet destruction:** predicts fleet owned tonnage and homebound arrivals both remain markedly depressed years after war. Reconstructed homebound arrivals 1785 higher than 1780, which **opposes blanket permanent-capacity collapse**; intra-Asian company-owned ship tonnage did fall. Requires voyage-level original data and accounting for timing, hiring, survival and missing musters.
4. **H4 State rescue and takeover:** compare company liabilities, Holland/Zeeland guarantees, actual state cash outflows, government decisions, corporate transfer, political-regime change. NA oversight starts 1790, and cannot be projected backward to 1780 without other sources.
5. **H5 Product price/competitive displacement:** compare *same product* unit-price, volume and shipping share vs EIC/other European traders before war; account for war, price levels, demand shifts and inventory timing. No comparable EIC dataset acquired; `NOT_RUN`.

## 5. Reproducible design and method constraints
- Period: 1765–1795 target, with daily/monthly voyage event data if obtainable, BGB accounting Sept 1–Aug 31, and VOC Amsterdam six-chamber book period defined separately. War started **20 Dec 1780**, not at Jan 1780; mark treatment date precisely.
- **Separate outcomes:** (A) intra-Asian ship availability July snapshot; (B) homebound arrival tonnage annual; (C) return cargo *invoice* values by accounting year; (D) realized European auction proceeds and cash collection; (E) short term external debt rollovers and interest; (F) government guarantees vs actual treasury cash.
- Do not compare BGB's **55 noncontiguous years** as if 1700–1801 complete; use original available-year mask, never zero-fill unrecorded years, and do not count overlap books as extra years.
- First deliver descriptive event timeline and reported shocks; only after data validation consider interrupted time-series or matched Anglo-Dutch merchant shipping, with placebo 1672, and political-regime change controls. With one VOC subject and nonrandom war, causal attribution remains structurally difficult, even with exact monthly data.
- **Never add** `equipage` to already-included interest, or compare government fiscal burden with VOC company balance without a documented transfer bridge. VOC dissolution 1800 does not imply immediate end of Netherlands colonial presence.

### Material outcomes and statuses
- Van Rossum 2013 printed p55 fleet Table2 source-to-CSV and direct arithmetic validation: `PASS_PARTIAL`; does NOT independently validate original muster ledger.
- Official BGB archival volumes, data coverage, omitted finance tables and currency-year interpretation: `INSTITUTIONAL_METHOD_REVIEW_PASS`.
- NA 3.02.33 oversight committee original archive and digitized item list: `INVENTORY_VERIFIED`, `ACCOUNT_SCANS_NOT_ACQUIRED`.
- 1872 Kroniek pp40–41 and physical Van Ghesel inv15: `NOT_ACQUIRED`; 1640–1700 Gaastra equipage f370m / f465.7m: `OPEN_SOURCE_CONFLICT`.
- Original 1779/1781/1784 VOC Netherlands and Asian financial account pages, annual shipping raw CSV, state cash payouts: `NOT_ACQUIRED`; statistical war effect and independent historian review: `NOT_RUN`.

**Unique next step:** extract **one original BGB General Journal** (`1.04.18.02` preferably the 1779–80 and 1781–82 available-year items) and the **original 1790–1796 Holland committee** oversight financial annex that contains signed outlay or guarantee. For each, record scan ID, year convention, owner, heavy/light money, stock/flow and actual cash vs authorization. Use those to test whether shipping capacity and liquidity diverged during the crisis; leave long-period equipment conflict as a separate physical-access blocker.
