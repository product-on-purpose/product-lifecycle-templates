# requirements-traceability-matrix: history

Change log for the `requirements-traceability-matrix` bundle. Each entry records what changed and why, so a
reader can tell a correction from a preference.

## 0.1.0 - 2026-11-06

**Initial release.** Researched 2026-11-06 across six dimensions: origins, structure, practice, debates,
relationships and the gap question.
[`requirements-traceability-matrix_research-log.md`](requirements-traceability-matrix_research-log.md)
records **22 sources, all fetched-and-verified**. Every quotation was checked against raw text and never
against a retrieval tool's summary: of the 102 quotations the agents returned, 99 passed on the first check,
and the main loop repaired two failures with exact wording from the raw page and dropped the third.

**The eighth `governance-docs` member**, admitted by
[ADR 0084 (the requirements traceability matrix joins governance-docs as an eighth member)](../../docs/internal/decisions/0084-requirements-traceability-matrix-joins-governance-docs-as-an-eighth-member.md),
which lands the family contract at `0.6.0`. The bundle fills catalog entry 37 and is issue #261
(bundle: requirements-traceability-matrix). The maintainer ruled the spec's four choices as recommended on
2026-11-05: the classification `utility`, the sizes lean and full, the methodology `generic`, and the Saved
Views worked example with a stop rule.

### Why `utility`, and not a `qa-docs` phase

A matrix is updated whenever its requirements or tests change, so it is not produced at one stage and then
finished. ADR 0084 records that the `qa-docs` axis would be the wrong one for that reason, and it records
the one clause the family contract's purpose phrase gained to admit the type. The bundle declares
`classification: utility` and `methodology: generic`.

### `pairs_with` resolved to empty

No skill in [`tools/known-skills.txt`](../../tools/known-skills.txt) addresses authoring or maintaining a
requirements traceability matrix. The family contract's section 2 already says no governance skill exists
in pm-skills, and the pinned list holds nothing on traceability or verification. `pairs_with: []` is a
checked answer and not a gap to paper over.

### `related_templates`

The list names the upstream documents that state requirements (`prd`, `acceptance-criteria`), the
verification documents the matrix reads from (`test-plan`, `test-case`, `test-summary-report`), the register
the full variant's Risk Control Trace links to by identifier (`risk-register`), and the change record whose
boundary the companion draws (`change-log`). The boundaries against `acceptance-criteria`,
`test-summary-report` and `change-log` are the library's own position, and the companion says so: no
external source read states any of them.

### Two sizes, and the split is a hypothesis

Lean carries what TestDevLab describes, requirement to test, read in both directions, with the five sections
that make it usable. Full adds Implementation Trace, Risk Control Trace and Baselines. **No source read shows
a template that carries every link type**, so the division between the sizes is the library's hypothesis,
held at medium-low confidence. The signal to scale up is a question the team owes an answer to that the lean
table cannot give.

### What the research found, and what it did not

- **The first use of the phrase is not established.** No source read shows where it began, and the bundle
  offers no origin story. A 1980s defence-standards account surfaced only in low-authority pages and stays an
  unverified lead.
- **Traceability and the matrix are kept apart.** The bundle states that traceability is a property and the
  matrix is one implementation of it. NASA's verification matrix is a related artifact and is not this type.
- **A linked test is not a verified requirement.** NASA ties completion of verification to documented
  objective evidence and to closure of nonconformance reports. This is the bundle's sharpest teaching point,
  and Trace Conventions is where a matrix says which meaning its status words carry.
- **The type is contested, and the guide leads with who should not use it.** Named practitioners say the
  matrix rarely repays its upkeep, and no named software team outside regulated or safety-critical work was
  found describing its own matrix. High confidence that the search found none, medium that none exists. The
  strongest named case is regulated. A mapping study of 63 papers says strong industrial evidence is still
  needed. **Nothing read shows that keeping a matrix improves outcomes.**
- **Several section layouts are the library's position.** No source shows how a gap is displayed, how a stale
  matrix is marked on a hand-kept row, or what form an update trigger takes. The template labels each as a
  position at its point of use.
- **No cadence is stated as a norm.** NASA gives key reviews and Jama gives a change-driven rule. No source
  gives a calendar interval.

### Sources withdrawn, and pages not read

Three sources an agent read were withdrawn, and no claim rests on them. The Texas Department of Information
Resources instructions were withdrawn because the site's terms could not be checked and the agent had retrieved
the file with a browser-style client string. A chapter on requirements traceability hosted on a university
faculty page was withdrawn because a raw re-fetch failed and the publisher of that copy was not established. A
task file in one npm package was withdrawn because its host's terms page did not render, and with it went the
only source for a graded full, partial and none coverage scale, so that scale is not adopted as a norm.

Standards were not read: ISO/IEC/IEEE 29148, 29119-3 and 24765, IEEE 829 and 830, 21 CFR 820.30 and the QMSR,
DO-178C and the INCOSE handbook. A standard is cited for its existence and never for its content. Also unread:
a 2023 paper in *Requirements Engineering* on why teams do not trace, whose publisher's page returned a client
challenge, and PMI's template, which sits behind a membership wall.

### Terms checked after the research

The log records that the terms check ran after the research, which was the wrong order. The main loop then
read the terms page of each host first read in this run, and none bars a read of this kind. The absence of a
terms page for two practitioner sites is recorded as absence and not as clearance.
