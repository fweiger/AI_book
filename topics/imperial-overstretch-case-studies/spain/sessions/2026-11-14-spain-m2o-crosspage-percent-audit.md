# CASE-ESP-001 session 2026-11-14 M2o — cross-page evidence reconciliation

Canonical research [AI_book #32](https://github.com/fweiger/AI_book/issues/32), existing Draft PR #36, Spain branch unchanged. Task Center ENTRY and task Goal/AC resumed. No duplicate task or mainline merge.

## Actual source findings
Original **peer-reviewed publisher indexed PDF** for Ricardo Franch Benavent 2016, *Obradoiro de Historia Moderna* 25, doi10.15304/ohm.25.3202, is search-index readable at separate original printed page locations. Official p217 original text says **202 peones represented 45 percent of all 1797 Valencia port construction workers** and precisely reports 18 at5 nominal reales/day, 163 at4.5, 21 at4. Official p236 original text footnote reports **78 additional amasadores at5/day**, 23 specialized masons (avg~7.7), two senior construction jobs, and first-party 1797 source call number **A.M.V. Documentación Lonja caja56 exp19**. These are distinct passages from the **SAME ARTICLE**, not independent archival source reviews. Publisher original PDF open503, so screenshot unavailable; original published searchable text evidence only.

**Important correction of erroneous M2n quarantine:** M2n's rule "not mentioned on p236 -> unsupported anywhere" was false. Original p217 independently **within the same authored work** supports 45percent. Updated legacy M2m wage CSV restore45 in a dedicated reported_percent_of_total_workers field, with workers_count left blank on percentage row and grade PUBLISHED_SECONDARY_APPROXIMATE_P217_NOT_ORIGINAL_ROSTER. Older M2m and M2n narrative and two source registries corrected. 202/0.45=448.88889 is an inverse-source estimate ~449, not actual roster N. Assuming 45% nearest integer percent, N integer444..453, not known rounding rule or historical observed count; grade CONDITIONAL. New M2o report, source registry, crosspage evidence matrix and sensitivity scenarios.

Historic conditional common-day nominal wage models unaffected: peones 202/907.5; plus78 amasadores ->280/1297.5. Another 23 skilled masons with approximate avg7.7 and two senior staff remain outside exact constructed wage. Nothing establishes wages actually paid, amount overdue, headcount in one shift or finance causal attribution.

## Original PDF catalog retrieval attempts and actual outcomes
Ayuntamiento Valencia official [Archivo Histórico Municipal](https://www.valencia.es/es/-/archivo-hist%C3%93rico-municipal) live HTML directly READ, links inventory “Documentación Lonja (Pdf 1.2MB)” (link id28). Web attempted direct PDF with and without URL query and clicked exact official link; result repeated timeout/400. Local Python requests DNS lookup for www.valencia.es failed; no PDF copy downloaded, no specific Caja56 Exp19 catalog item verified. Therefore scholar-cited exact box is not same as verified modern archive entry. No original 1797 personnel/wages manuscript acquired, no outbound scholarly email sent, no proprietary source PDF uploaded.

## Reproducible QA & known blockers
- Published p217 202/45pct and p236 archive/junior trade counts separately recorded as source claims. Manual source page screenshot unavailable (publisher returns503), not reported as visual.
- 202/0.45~449 descriptive, nearest-integer bound N444–453 is modeled and conditional, not historic exact.
- M2o CSVs historical-source crosspage 7, source provenance5, denominator sensitivity10; new report and session, README/CHANGELOG, M2m/M2n corrections. GitHub readback checks and CI separately reported.
- Original 1797 Caja56Exp19, 1795 Banco bank port deed,1862 bank payout certificate and UKDS data NOT_ACQUIRED; wage arrears/fiscal interest Navy causal regression NOT_RUN.

**One next action:** obtain authorized original municipal archive Caja56 Exp19 item index, worker roster and wage-pay accrual/actual pay pages, then separate Feb11 1797 protest documentary file; study port bank-disbursement months with municipality tax actual money after original access. Leave existing Issue OPEN and PR DRAFT.
