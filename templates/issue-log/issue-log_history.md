# issue-log: history

Change log for the `issue-log` bundle. Each entry records what changed and why, so a reader can tell a
correction from a preference.

## 0.1.0 - 2026-09-23

**Initial release.** Admitted as the fourth `governance-docs` member by
[ADR 0057 (issue-log joins governance-docs as a fourth member)](../../docs/internal/decisions/0057-issue-log-joins-governance-docs-as-a-fourth-member.md),
which lands the family contract at `0.2.0`. Specced the same day in
[`tier2-specs.md`](../../docs/internal/tier2-specs.md), built on the maintainer's direction under
[ADR 0041 (maintainer preference sets the build order)](../../docs/internal/decisions/0041-maintainer-preference-sets-the-build-order.md).
[`issue-log_research-log.md`](issue-log_research-log.md) records **41 sources**: 38 fetched and verified, 2
with their URL confirmed without the body being read, and 1 (the AXELOS PRINCE2 manuals) not retrieved at
all. Every quotation was checked against the source's raw text on 2026-09-23, not against a retrieval
tool's summary of it.

**The document the library already routes to.** Both `risk-register_guide.md` and `raid-log_guide.md`
already carried a chooser table naming an issue log, and both risk-register templates already sent a
materialized risk to it, before this bundle existed to receive that traffic.

### The definitional split, made a first-section decision rather than papered over

Four named bodies define "issue" four incompatible ways, and the template does not pick a winner:

- PM²'s field-list source, the one this bundle may adapt: "An issue is any unplanned event related to the
  project that has already happened and requires the intervention of the Project Manager (PM) or higher
  management."
- PMI's *Lexicon* is broader still, requiring neither an event nor a tolerance breach: "A current condition
  or situation that may have an impact on one or more objectives."
- APM's glossary requires a tolerance breach: "A problem that is now breaching, or is about to breach,
  delegated tolerances for work on a project or programme."
- PRINCE2 7 (2023) widens the concept forward, as PeopleCert describes it, to "anything that could affect
  the project," a change from PRINCE2's 2009 glossary, which required something that "has happened, was
  not planned, and requires management action."

**The consequence for the design is this library's own, not sourced to any of the four:** three
incompatible definitions mean two people keeping the same log can disagree about whether a row belongs in
it at all, so the template's Purpose and Threshold section requires the team to state its own position
among the three, rather than inheriting an ambiguous one silently.

### Section design departs from the provisional spec in one place

`tier2-specs.md` proposed the shape mirroring `risk-register`, with Escalation carried in lean rather than
full, unlike the risk register. Research supported keeping it there: every readable source carries
escalation, and APM's own definition of an issue is a tolerance breach, which is an escalation condition
by definition. The published shapes for the escalation record differ (a Yes/No field in PM², a status value
in Connecticut's template, a change of decision-maker in Washington's template, a tolerance in APM's
definition), and the guidance offers them as choices rather than picking one.

### `sizes_available` resolved to `[lean, full]`, no longer provisional

The provisional spec allowed `[lean]` if the research found the rules-versus-register split did not earn a
second weight. It did: PM² separates the rules for handling issues (its Issue Management Plan, Appendix
B.4) from the log itself (Appendix B.9), the same split both `governance-docs` siblings make, and a full
weight carries the closed-issues audit trail (resolution, confirmer, closed date, lesson learned) and the
links-to-other-logs block that the lean variant does not need.

### `aliases` narrowed from the provisional spec

`tier2-specs.md` proposed `issue register` and `issue tracker`. Only `issue register` ships. "Issue
tracker" is what a reader looking for Jira-style software defect tooling types, and no source read
compares a project issue log with a software tracker directly; matching that alias to a project register
is the exact collision the bug-tracker boundary in the guide's When NOT to use exists to prevent.

### The change-request boundary is left open on purpose

PRINCE2 puts a request for change inside the issue concept ("all changes start as issues"); PMI's *PMBOK
Guide* instead names the change log as a separate project document with no stated overlap rule; PM² keeps
a separate Change Log linked from the issue by a Traceability field. The companion states PRINCE2's
alternative plainly rather than deciding the boundary here, and leaves it to a future `change-request`
bundle's own research.

### Relationships against the other three members

Per the family contract's section 1 and 4, the companion states the issue log's position against all
three siblings: it is not the risk register (tense: something that occurred, not something that might,
and a materialized risk closes there and opens here, linked both ways, never deleted); it is not the RAID
log (the deepened, standalone form of RAID's Issues quadrant, exactly as a standalone risk register stands
to RAID's Risks quadrant); and it is not the KPI dashboard (a different subject, performance against
targets, sharing no rows). It also states a boundary no source supplies: a software defect with no
project-management dimension belongs on a bug or ticket tracker, not here, labelled in the guide as this
library's own judgment rather than a sourced rule.

### The shared scenario, carried forward rather than invented

Per the family's shared-scenario rule, the example is the Reporting Platform Modernization program's issue
log, and it carries `ISS-11` (the query-engine lead's departure, raised 2026-06-14, target 2026-07-31,
owner Marta Reyes, escalated to the steering group for a GBP 45,000 backfill contractor) and `ISS-12`
(staging view-list load at 620ms against a 500ms budget, raised 2026-07-10, target 2026-07-24, owner Dana
Osei) exactly as recorded in the five sibling examples that already cite them: `raid-log`, `risk-register`,
`status-report`, `kpi-dashboard`, and `project-milestone-retrospective`.

### What was not read, and is not claimed

AXELOS's own PRINCE2 manuals (6th edition 2017, PRINCE2 Agile 2016, PRINCE2 7 2023) are behind a
subscription and were not retrieved; PRINCE2 enters this bundle only through its openly reproduced 2009
glossary and secondary practitioner accounts. ISO 21502:2020's official free preview defines an issue and
lists "Issues management" as a clause, but the clause body itself is past the preview, so the bundle
states that ISO frames a practice, not a named document, and claims nothing past that. The UK government's
Teal Book chapter on issue management refused every raw fetch and carries no claim in this bundle beyond
its own existence.
