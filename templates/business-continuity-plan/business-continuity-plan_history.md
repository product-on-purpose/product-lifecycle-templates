# business-continuity-plan: history

Change log for the `business-continuity-plan` bundle. Each entry records what changed and why, so a
reader can tell a correction from a preference.

## 0.1.0 - 2026-10-14

**Initial release.** Admitted on 2026-10-12's admission sweep 5 against the catalog entry
`disaster-recovery-business-continuity-plan` (catalog id, catalog_ref 135, issue #263); specced
2026-10-13 in `tier2-specs.md`; built 2026-10-14 with a six-dimension research fan-out covering the
federal canon, the state and regulator sources that model the Disaster Recovery section and state a
cadence, the professional bodies and their debates, cloud and site reliability practice, this library's
own neighbors, and the standing gap question.
[`business-continuity-plan_research-log.md`](business-continuity-plan_research-log.md) records **32
sources, all fetched-and-verified**, and **296 quotations**, each checked against the source's raw text
rather than a retrieval tool's summary: 282 of 292 quotations the fan-out's agents returned passed, 12
were dropped for the reasons the log gives, and 17 were added from the main loop's own checks.

**The sixth `standing-standards` member, and the second this family's own forecast never named.**
[ADR 0071](../../docs/internal/decisions/0071-business-continuity-plan-joins-standing-standards-as-a-tool.md)
assigns `classification: tool`, on the same `foundation`-versus-`tool` reasoning ADR 0053 and ADR 0062
used for the family's earlier members: this plan is a maintained instrument a team executes once a
disruption is declared or a drill begins, not a standard the team is judged against on a cadence.

### One bundle, not two, by the maintainer's ruling of 2026-10-13

The catalog's merged name names two plan types. Research found that they admit at different strengths:
the business continuity plan admits on a literal fill-in template, FEMA's Ready Business PDF, and NIST's
own definition; the disaster recovery plan admits on a definition only, since no source read, including a
gap-fill run specifically to test this question, ships a complete fill-in template titled and scoped as a
standalone Disaster Recovery Plan. ADR 0071 therefore builds one bundle, with disaster recovery as a
section, modeled on California's SIMM 5325-A structure, present in the full variant and reduced to a
pointer in lean rather than as a sibling bundle. The companion names this asymmetry rather than rounding
the weaker half up to match the stronger one.

### Two federal sources disagree on where a disaster recovery plan recovers to

NIST SP 800-34 Rev. 1 scopes a disaster recovery plan to "an alternate facility." The CSRC glossary's
CNSSI 4009-2022 entry scopes it to recovering "at its original facilities" over "hours or days." Both are
federal, fetched-and-verified sources. This bundle does not resolve the disagreement: the research log and
companion both carry the contradiction rather than picking a side.

### The cadence tension is routed to the Review Trigger section, not resolved by widening the contract

Most sources that state a review or test cadence state an annual one; NIST's own narrative sets a looser
rule, review "at an organization-defined frequency or whenever significant changes occur to any element
of the plan." ADR 0071 keeps the family's own rule that a standing-standards member is "not revised on a
calendar": the bundle's Review Trigger section states conditions, and an annual exercise appears there as
a floor a regulator or policy may impose, never as the trigger itself.

### Who authors, activates and executes the plan is reported, not settled

The sources the companion draws on for the question, NIST, California's SIMM 5325-A, HMPPS's policy
framework and the 2003 FFIEC booklet, return different readings of how authorship, activation and
execution divide. No source found says
the plan's author usually runs it alone, and none says they usually do not. This research does not amend
ADR 0071's open question on this point; it reports the finding in the companion and research log for the
maintainer.

### Several structural sources are time-bound, and the bundle names each limit

The FFIEC Business Continuity Planning booklet read directly for this bundle is the March 2003 edition,
at least two editions old; the current 2019 booklet returned HTTP 403 on every retrieval attempt and was
not read. FEMA's Continuity Guidance Circular 1 is dated 2013, and whether either of two later
FEMA-titled circulars found in a 2026 search supersedes it was not confirmed. Neither is cited as current
guidance.

### `pairs_with: []`, checked and confirmed empty rather than left empty by default

No pm-skills skill ID in [`tools/known-skills.txt`](../../tools/known-skills.txt) names a business
continuity plan, a continuity plan, or a disaster recovery plan. `pairs_with` is declared empty because
that was verified against the pinned list, not assumed.

### No `default_format` key is declared

This bundle found one shape for the document type and carries no format key, consistent with the
majority of members built before the format-axis backfill.
