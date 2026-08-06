# definition-of-done: history

Change log for the `definition-of-done` bundle. Each entry records what changed and why, so a reader can
tell a correction from a preference.

## 0.1.0 - 2026-08-06

**Initial release.** Researched 2026-08-06 across six parallel dimensions: the Scrum Guide canon, structure
in practice, the boundary against acceptance criteria and neighbors, failure modes and the evidence base,
ownership and staleness, and levels above the single team.
[`definition-of-done_research-log.md`](definition-of-done_research-log.md) records **27 sources**, of which
**22 were fetched and verified** and **5 could not be retrieved**. Of the 22 read, 5 are primary, 3
standards, 9 practitioner, and 5 vendor.

**The first member of the `standing-standards` family**, adopted in
[ADR 0032 (the standing-standards family contract)](../../docs/internal/decisions/0032-adopt-standing-standards-family-contract.md),
which groups documents agreed once and applied every time rather than written per increment or per phase.
`definition-of-done` takes `classification: foundation`, a standard the team is judged against, alongside
`runbook` at `classification: tool`, an instrument the team executes.

### The 2020 rewrite is read directly, and the folklore is named

This family's contract names its citation hazard as "folklore presented as standard." Two editions of the
Scrum Guide were fetched and compared line by line rather than summarized from secondary material, and
three claims that circulate widely as settled practice were found absent from the canon: that the
Definition of Done is a checklist, that it gets stricter over time through the retrospective, and that it
is "the team's contract." All three are recorded as folklore, not canon.

The 2020 Guide's own framing was also confirmed against its predecessor: the Definition of Done became a
**commitment attached to the Increment**, not an artifact of its own, which is new as of 2020. The
retrospective-trigger sentence present in the 2017 Guide ("plans ways to increase product quality by
improving work processes or adapting the definition of 'Done'") was not carried forward into the 2020 text
across repeated retrieval attempts, and that absence is recorded as a version difference rather than
resolved as a deliberate change of policy, since no source read for this bundle states why.

### Ownership is stated as collective, correcting a citation elsewhere in this library

Every source this research read makes conformance with the Definition of Done collective or contingent; no
source names a single accountable role. This bundle's companion corrects a citation error elsewhere in this
library that had attributed sole ownership to one role.

### The size call departs from the provisional spec, on evidence

`buildout-specs.md` originally proposed a single `lean`-only size for this type. The research instead found
published Definitions of Done vary by nearly an order of magnitude, and the variance tracks scope rather
than formality: real shipping engineering examples run far longer than a single-cadence checklist once more
than one cadence (feature, sprint, release) is gated at once. `sizes_available` was set to `[lean, full]` on
that evidence, with lean carrying Scope and Ownership, Done Criteria, and Review Trigger, and full inserting
Criteria by Level, What This Excludes, and When Work Does Not Meet It between Done Criteria and Review
Trigger, keeping lean a strict ordered subset.

### One statistic traces cleanly, and its own authors call the evidence thin

The widely circulating claim that 93 percent of practitioners find the Definition of Done valuable resolves
to one real survey of 137 practitioners across 45 countries, the only controlled evidence this research
located. It is carried with that provenance rather than as a bare figure.

### Sources not retrieved are quarantined

Five sources, including an IEEE paper, the Nexus Guide, a SAFe primary text, and two named Scrum.org worked
examples, could not be retrieved despite repeated attempts. Nothing in the bundle rests on them, and no
figure attributed to them appears as fact.

### No `default_format` key is declared

Having found one shape for this document type, this bundle carries no format key rather than declaring a
single-member axis, consistent with the majority of members built before the format-axis backfill.
