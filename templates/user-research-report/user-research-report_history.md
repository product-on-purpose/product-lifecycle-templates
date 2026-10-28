# user-research-report: history

Change log for the `user-research-report` bundle. Each entry records what changed and why, so a reader
can tell a correction from a preference.

## 0.1.0 - 2026-10-27

**Initial release, the second and closing founding member of `research-docs`.** Researched 2026-10-25
across seven dimensions, one of them run twice: government and standards bodies' formal reports,
vendors' section lists at two depths, the evidence a finding carries, practice and its debates, the
standing-repository gap question, the library's own neighbours and the Acme Analytics chain, and a
gap-fill pass. [`user-research-report_research-log.md`](user-research-report_research-log.md) records
**52 sources, all 52 fetched-and-verified**, with no not-retrieved entry and nothing quarantined. By
tier they are 22 vendor, 20 practitioner, 6 primary and 4 standards. Every quotation was checked against
the source's raw text rather than against a retrieval tool's summary: of 381 quotations the recheck
read, 312 passed strict, 10 passed as extraction artifacts, and 59 failed and were corrected before this
release, the large majority of them traced to a corrupted stored copy (the Employee Express `.docx`,
re-extracted as paragraph text) or a table-reading artifact (Ethnio's stored copy, re-fetched).

### The second of the two founding `research-docs` members

[ADR 0081](../../docs/internal/decisions/0081-adopt-research-docs-family-contract.md) adopted the
`research-docs` family contract on 2026-10-23 with no member built. This bundle and its sibling,
`user-research-plan` (catalog entry 210, built 2026-10-24), are both founding members, specced together
on 2026-10-23 and ruled on together by the maintainer on 2026-10-24 ("I approve your ten choices,"
recorded at `docs/internal/tier2-specs.md:7376-7393`). The contract's section 1 states the membership
test this bundle meets: it "reports on ... one study of the people a product serves," after the study
ends, answering the questions the plan set out before it ran. This bundle was built second, by the
maintainer's own ruling (ruling 8), so that its example could report against the plan's own example
rather than against an invented one.

This bundle answers the spec written 2026-10-23
(`docs/internal/tier2-specs.md:6963-7425`), closed by the maintainer's ten rulings of 2026-10-24.
Catalog entry 18 is unchanged from the master catalog; this release is its first bundle.

### The friction study's readout, closing a chain four shipped examples opened

The PRD, design brief, epic and internal-announcement examples each cite "Discovery readout: Reporting
friction study, 2026-05" as a document that exists, and until the plan's 2026-10-24 release only the
plan showed any part of that study. Per the contract's section 4 shared-scenario rule,
[`user-research-report_example.md`](user-research-report_example.md) chains onto the same study: it is
the report for the 2026-05 Reporting friction study that
[the plan](../user-research-plan/user-research-plan_example.md) set out on 2026-04-20, dated 2026-05-27,
after the sessions (2026-05-04 to 2026-05-15) the plan scheduled. Priya Nair, PM for Reporting, is named
as author in both examples, by the maintainer's ruling 7. Every fact this example states about the
study, the method, and the participant count holds against the plan's own example and against the four
sibling examples that already cite the study; a figure that appears only in a sibling template's own
GOOD or WEAK text is that template's illustration, not a fact of the scenario, and does not bind this
example.

### Two sizes, by the maintainer's ruling

The maintainer ruled on 2026-10-24 (ruling 3) to ship `sizes_available: [lean, full]`, `default_size:
lean`, as recommended. Lean carries six sections: Summary, Research Questions and Answers, What We Did,
Key Findings, Task Results, and Recommendations. Full adds three, Background and Objectives, Open
Questions, and Appendix, each in the same place both sizes would put it were it present in both, and the
lean six are a strict ordered subset of the full nine, unchanged in name and order, per contract section
3.2.

### The usability block ships at every size, filled in only when the study is a usability test

Task Results is the section that makes the alias "usability test report" true, following the same
pattern the maintainer set for the plan's Tasks and Measures (ruling 4: one conditional section at both
sizes, for both members, over a separate usability-only variant). For any other method - interviews, a
diary study, a survey, a field visit - the section is one line naming the method actually used, with the
task table and the questionnaire line marked N/A, which is a complete answer and never a placeholder.

### The report recommends; it does not decide

Per the family contract's boundary against `discovery-docs`, which "take[s] the findings and frame or
decide," this bundle's guidance keeps every GOOD line in the recommending register ("We recommend") and
rules out the deciding one ("The team will build"). The guide and companion each name the sources that
pull toward recording the decision too, and state plainly that this library declines to follow them
here.

### `pairs_with: [discover-interview-synthesis]`, by the maintainer's ruling

The maintainer's ruling 6 assigns `discover-interview-synthesis` to this bundle, not to the plan, as
recommended: "Use after conducting user interviews, customer calls, or usability sessions to extract and
communicate findings across participants" is this bundle's own job, in the skill's own words. Verified
present at `skills/discover-interview-synthesis/SKILL.md` in `product-on-purpose/pm-skills` on
2026-10-27 (commit `4100cb88b`, skill version 2.3.0, `phase: discover`), and added to
`tools/known-skills.txt` in this release, which is where the id first enters that pinned list.

### `related_templates` carries no `future:` reference

`[user-research-plan, prd, design-brief, epic, announcement-internal-comms, user-persona]`. Every
target already exists on disk. `user-research-plan`'s own `related_templates` is corrected in this same
release, dropping its `future:user-research-report` prefix now that this bundle exists, per the spec's
own closing note (`docs/internal/tier2-specs.md:7372`) and the maintainer's ruling 10; see
[`user-research-plan_history.md`](../user-research-plan/user-research-plan_history.md).

### `methodology-agnostic`, matching the plan

The maintainer's ruling 9 set `methodology-agnostic` for both founding members, against the sources'
heavier UX-research and usability-testing lineage, matching `problem-statement` and `design-brief`, this
family's nearest `discovery-docs` neighbours, rather than naming one research methodology this report
requires.

### Still open at this landing

[`spike-report_guide.md`](../spike-report/spike-report_guide.md) names `discover-interview-synthesis`
in its own pairing section but does not yet carry the dated note routing user research to this bundle
that the spec calls for at the report's landing (`docs/internal/tier2-specs.md:7366`). That edit is
outside this bundle's own two files and is left for the landing PR that carries this release.
