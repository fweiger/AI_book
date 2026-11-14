# CASE-NLD-001 | M3B: Anglo-Dutch voyage timing and exact VOC/BGB archive inventory crosswalk | 2026-11-14

Authority https://github.com/fweiger/AI_book/issues/33 ; same Draft PR #37, stay unmerged. Added quantitative cross-empire technology/organization comparator and exact archival item numbers. Do NOT call this a 1780 war causal estimate.

## 1. Directly accessed 2017 original peer-reviewed journal HTML and Table 1
Peter M. Solar & Pim de Zwart (2017), *Why were Dutch East Indiamen so slow?*, *International Journal of Maritime History* 29(4), DOI 10.1177/0843871417725487. Article full HTML including Table1 and technical interpretation was directly read: https://journals.sagepub.com/doi/10.1177/0843871417725487

Table1 Batavia SAME DESTINATION outward voyages, DAYS (authors' reconstructed period means, not this session's individual logbook calculations):

| Period | Company | Mean days | Median days | N voyages |
|---|---|---:|---:|---:|
| 1770-1775 | VOC_Dutch | 253 | 237 | 156 |
| 1770-1775 | EIC_English | 173 | 160 | 20 |
| 1783-1792 | VOC_Dutch | 238 | 231 | 238 |
| 1783-1792 | EIC_English | 179 | 173 | 10 |

Original underlying Dutch *Dutch-Asiatic Shipping* and English Farrington (1999) ship-log entries were not read independently; 2017 Table1 is a peer-reviewed academic comparative reconstruction, and **British Batavia N is just 20 prewar and 10 after**.

Published-cell arithmetic, explicitly *not* an event-study:
- 1770–1775 mean VOC-EIC Batavia gap: 253−173=**80 days**; median gap=237−160=**77 days**.
- 1783–1792 mean VOC-EIC Batavia gap: 238−179=**59 days**; median gap=231−173=**58 days**.
- Same-destination gap change: **−21 days mean**, **−19 days median**, with different samples, ship types, routes, sea conditions and overlapping war+postwar years. NO significance test, NO confidence interval, NO claim VOC overtook EIC.
- The article text says the overall English advantage widened across Asian destinations in the 1780s, but this very limited same-Batavia subset shows NARROWING. This is a meaningful **aggregation/destination-mix caution** rather than a refutation of the article or a causal negative effect of coppering.

See [voc_anglo_dutch_batavia_voyage_m3b.csv](voc_anglo_dutch_batavia_voyage_m3b.csv) for 4 company/period rows and [voc_batavia_gap_audit_m3b.csv](voc_batavia_gap_audit_m3b.csv) for 2 exact comparisons. Same-destination single port improves comparability but NOT route, build, charter status and cargo mix.

## 2. Competitive technology is not a magic post-1780 treatment
2017 article details slow VOC adoption of copper hull sheathing, with original eighteenth-century directors' decisions discussed but primary Heeren XVII folios NOT independently acquired. [voc_copper_sheathing_events_m3b.csv](voc_copper_sheathing_events_m3b.csv) codes historical chronology and decision vs adoption:

- 1777, 1780, 1783, 1786: some VOC chambers experimented with copper sheathing; corrosion and shallow-water conditions led to reservations.
- 1788: officials from Canton explicitly raised English copper sheathing and performance as reasons for faster journeys; **not proof they fully quantified commercial gains**.
- 1789: boards postponed a uniform decision; British EIC hired-vessel coppered rate reported **78% by 1789**, which is neither British merchant fleet-wide nor original ship-level company-year longitudinal data.
- Late 1791: first newly built copper-bottom Dutch East Indiaman departed for Asia. End 1792: copper on new builds requested but NOT mandatory. June 1794: formally required on new builds, implementation later interrupted by wars.
- Mechanisms are competing and complementary: shallow Dutch inland waterways encouraged broader flatter hulls, component chambers valued capacity, English copper reduced hull fouling and repairs and lengthened active ship life. The technology catch-up delay plausibly contributed to efficiency differences; it does not explain by itself the debt and cash crisis that began in 1780, or prove the 1780 war was unimportant.

**Required hypothesis update:** add `H6 technology + organization + waterways / ship turnover rate` independent of company cash and war treatment. Test with *same-route* voyage days, tonnage, ship life, copper status, stop count, build year, chamber, cargo and war exposure. A good negative observation is Batavia same-destination narrowing mean gap 80→59, not an automatic global speed-gap widening.

## 3. Archive-level progress: exact inventory numbers found, original scans still inaccessible
Official Nationaal Archief 1.04.18.02 inventory shows precisely:

| Book / archive item | Accounting year | Nature | Status |
|---|---|---|---|
| 10735 | 1779–1780 | Batavia `Generaal grootboek` general ledger | catalogued DIGITALIZED, first scan HTTP404 |
| 10736 | 1780–1781 | Same book | catalogued DIGITALIZED, first scan HTTP404 |
| 10795 | 1780–1781 | Batavia `Generaal journaal` original journal | catalogued DIGITALIZED, first scan HTTP404 |
| 10796 | 1781–1782 | Batavia original journal | catalogued DIGITALIZED, first scan HTTP404 |
| 10801 | 1779–1780 | additional separately listed journal | catalogued DIGITALIZED, first scan HTTP404 |

Official source https://www.nationaalarchief.nl/onderzoeken/archief/1.04.18.02. The first image link names and 404 outcomes are recorded in [voc_exact_archival_targets_m3b.csv](voc_exact_archival_targets_m3b.csv). Verified exact locators are a meaningful advance over generic collection numbers, **not access to physical account folios**.

Other side of the double-entry bridge is original state committee 3.02.33:
- **inv1** committee minutes May18 1790–Dec22 1791, **inv2** Feb7 1792–Jan15 1795.
- **inv12** annex records numbered 1–16, **inv23** index to annexes. All officially marked DIGITALIZED; first-viewer image URLs returned HTTP404. State committee covers 1790+, not the 1780 outbreak; could locate true disbursement or guarantees once scanned.
- Do NOT assert government cash payment from authorization/grant, and do not treat 1790 committee as 1780 company rescue decision.

## 4. Explicit consistency and missingness gates
- `VOC owned internal Asian fleet JULY STOCK` ≠ `Dutch homebound arrival YEARLY FLOW` from prior M3; both ≠ `voyage duration DAYS` from this M3B, nor `auction cash`.
- `NLD-S39` reuses Dutch *Dutch-Asiatic Shipping* underlying voyages shared with prior scholarship; comparing to English Farrington (1999) yields a new destination-matched quantitative question, not wholly independent Dutch raw observation.
- 1770–75 and 1783–92 windows not calendar-year event observations; the later window includes final wartime 1783–84 and postwar years. Exact war start Dec 20, 1780.
- Early British n20, late n10; raw voyages, variable composition, uncertainty estimates NOT_ACQUIRED, no historical causal or ROI coefficient.
- For copper technology, the 1791 first sailing, 1792 request, 1794 requirement represent three separate stages. EIC 1789 78% hired vessel figure cannot be used as 'all British ships'.
- Original NA primary pages not viewed even if live archives advertise DIGITALIZED: `HTTP_404_NOT_ACQUIRED`; original 1640–1700 VOC equipment f370m vs f465.7m unresolved, de Korte app1/14 not acquired; independent historian peer review and causal tests `NOT_RUN`.

## 5. Single actionable next step
Take exact original item **NA 1.04.18.02 inv10735 (1779–1780 ledger)** plus **inv10796 (1781–1782 journal)** and request an accessible scan or archivist-provided single-page finance folios, paired to **3.02.33 inv23 annex index** to locate provincial guarantees/disbursements; preserve original folio, money and fiscal-year source. Independently export monthly VOC homebound DAS voyage CSV if available, then compare against ship/auction/credit records only after source matching.

**Current task state**: M3B quantitative paper extraction `PASS_PARTIAL`; exact item IDs `CATALOGUE_VERIFIED` and page download `BLOCKED_404`; true cash finance and causal war effects `NOT_RUN`.
