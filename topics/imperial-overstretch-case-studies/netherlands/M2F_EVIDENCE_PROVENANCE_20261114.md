# CASE-NLD-001 M2F — source lineage / false-independent corroboration audit (2026-11-14)

Authority: https://github.com/fweiger/AI_book/issues/33 ; same Draft PR #37.  This is an **evidence-dependency** verification, not a financial original-account reconstruction.

## 1. Actual new observation: 2019 published table numerically agrees with the 1997 source
Rob de Haas, *In Nederland Door Omstandigheden; De Haas, een Indische familie in Gemert*, *Gemerts Heem* 61(1), 2019, printed p13, Table14, publishes 16 period rows (1640–1795) of VOC equipage and European sales rounded to 100,000 guilders. PDF: https://www.heemkundekringgemert.nl/wp-content/uploads/2020/02/2019-01.pdf

Crosscheck with existing GitHub `voc_trade_decades_m1.csv` (Gaastra 1997 printed p112): **16/16 period labels and 32/32 equipage/sales printed figures match exactly**. New machine-verifiable [voc_2019_republication_match_m2f.csv](voc_2019_republication_match_m2f.csv) records all rows and both labels, without adding these 16 rows to a purported independent historical sample.

**Crucial evidence tier:** this is secondary numerical republication of the same figures, NOT a new VOC financial archive and NOT independent confirmation that f465.7m is historically correct. The exact bibliographic path of copying is NOT PROVEN by numerical identity alone (the 2019 bibliography includes Gaastra's *De geschiedenis van de VOC* 1982, but it could have consulted another intermediary). Do NOT label explicit direct Gaastra(1997) copy.

The 2019 article additionally states, below Table14, that the figures have been drawn from annual statements with intervals beginning in spring **1641, 1651**, etc. Record `SECONDARY_PERIOD_ANCHOR_CLAIM_NEEDS_ORIGINAL_CHECK`: the table labels 1640–1650 are not proven to be exact Jan 1640-Dec 1649 calendar windows. The historical account-year anchor must be checked directly in de Korte Appendix1 or the chamber books before annual event studies.

**PDF source-quality caveat:** 2019 PDF text table was extracted by web content parser, but its visual screenshot request failed as the 11,123,675-byte file exceeded that tool's size cap. Accordingly all M2F 2019 rows are `TEXT_EXTRACTED_NO_SCREENSHOT`, not falsely `PDF_VISUAL_CONFIRMED`.

## 2. Critical 1872/archival material provenance
The Nationaal Archief official *Jacob van Ghesel 1.10.31* historical background specifies original former VOC director papers were partly edited by archive official **P. A. Leupe**, at **J. A. Grothe's** request, and printed in *Kroniek* **1872–1875**. The publication did **not** identify Van Ghesel or the paper provenance; its label was 'papers of an eighteenth-century VOC director'. Grothe or successors donated these papers to the national archive **1877 and 1886**. Thus the 1872 excerpts and today's *Van Ghesel 1.10.31* collection are NOT independent historical source lineages. Official source: https://www.nationaalarchief.nl/onderzoeken/archief/1.10.31/beschrijving/context

Original financial lists NA **1.10.31 inv.15** describe cost and return accounts of ships across all VOC chambers during **1640–1770**. NA live catalogue specifically marks this inventory **PHYSICAL**: https://www.nationaalarchief.nl/onderzoeken/archief/1.10.31

The DBNL library confirms *Kroniek* 1872 volume 27 is public-domain scan-only, about 49.56MiB; tool PDF fetch rejected it at **51,971,261 bytes**. Original **pp40–41 were not read**. Note crucial limited scope: official catalogue says material was only **PARTLY** printed in 1872, so even when pp40–41 are obtained they may **not** contain the exact period total required to reconcile f370m/f465.7m; inspect the actual printed headings and row scopes before promising resolution. DBNL: https://www.dbnl.org/tekst/_kro004187101_01/

Sources and their dependencies are recorded in [voc_source_lineage_m2f.csv](voc_source_lineage_m2f.csv); registry [source_registry_m2f.csv](source_registry_m2f.csv); access states [voc_archive_access_status_m2f.csv](voc_archive_access_status_m2f.csv).

## 3. Implications for source independence and statistical inference
- The 1992 Gaastra archival introduction reports f370m for 1640–1700, while the Gaastra 1997 Table1 sums f465.7m. Their **common author** means the conflicting values should not be described as independent historians disagreeing; original source account definitions still missing.
- The 2019 Table14 reproduces f465.7m early equipage and f576.8m sales by the same printed decade figures. It is **numeric transmission corroboration** but does not constitute an independent VOC reconstruction nor break the conflict.
- Gaastra (1997) printed Table1 itself cites Bruijn et al., *Dutch-Asiatic Shipping*, vol I p190, and de Korte (1984) Appendix1. The underlying tables need direct reading to establish sample years, coinage, accounting owner and `equipage` components.
- Because `equipage` includes expenditures and **interest**, no interest addition to the equipage table should be used to infer a new corporate cash use; because all observations are nominal period totals, no direct profit or 1780 war treatment-effect inference is justified.
- Annual-period anchor **spring 1641/1651** from 2019 should be treated as a methodological lead, not a correction imposed on Gaastra(1997) until the original de Korte tables are examined.

## 4. Real attempts and blocked access
- Tried DBNL volume PDF via web PDF link. Returned `400 Content length is too large: 51971261`. Tried container network requests/console download; DNS/network failed; no 1872 source PDF landed in the workspace. No single-page 1872 scan made available.
- Tried 2019 compact PDF web screenshot; it returned a `400 Content length is too large: 11123675`, though PDF full text was successfully parsed by web.
- Official NA item 1.10.31 inv15 marked PHYSICAL. The image/scan access status is **not a temporary 404 to retry with URL changes**; physical research or ordering a reproduction is the likely next step. Do not assert digitization.
- Direct de Korte Appendix1/14 and wartime NA 1.04.02 4596/4597 records remain NOT_ACQUIRED. 1640–1700 contradiction remains SOURCE_CONFLICT_OPEN.

## 5. Acceptance checks and next item
- 16 pairs / 32 numeric matches M1 vs 2019: `PASS` as **secondary-source numeric concordance**, NOT independent original archive review.
- Provenance chain from archive accession to Leupe 1872 excerpts: `PASS` as **official finding-aid metadata**, NOT actual ledger transcription.
- NA 1.10.31 inv15 original physical files, 1872 printed pp40–41, de Korte Appendix1, cash and liabilities original 1779/1784: `NOT_ACQUIRED`.
- VOC P&L, actual net return, UK-Dutch causal event study and historian independent audit: `NOT_RUN`.
- **Unique next action:** obtain a **targeted reproduction** of Nationaal Archief `1.10.31 inv.15` (and related inv9/16 only if needed) showing year start, column headings and exact cost totals; or request **only** *Kroniek* 1872 vol27 pp40–41 page images from DBNL. Then compare against de Korte 1984 Appendix1 and BOTH Gaastra editions at matching accounting scope. Do not treat 2019 as the third vote.
