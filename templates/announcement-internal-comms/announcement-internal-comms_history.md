# announcement-internal-comms: history

Change log for the `announcement-internal-comms` bundle. Each entry records what changed and why, so a
reader can tell a correction from a preference.

## 0.1.0 - 2026-09-25

**Initial release.** Specced in
[`tier2-specs.md`](../../docs/internal/tier2-specs.md), built on the maintainer's direction under
[ADR 0041 (maintainer preference sets the build order)](../../docs/internal/decisions/0041-maintainer-preference-sets-the-build-order.md)
(GitHub issue #177, build-candidate 3). Researched 2026-09-25 in two passes: an admission sweep run while the
spec was written, covering named bodies, product and engineering practice, boundaries and failure modes, and
the library's own references, and the build's six-dimension fan-out (canon, structure, boundaries, failure
modes, audience and timing, and the standing gap question).
[`announcement-internal-comms_research-log.md`](announcement-internal-comms_research-log.md) records **39
sources, all fetched-and-verified.** Of 181 quotations the build's agents returned, 161 passed as returned,
12 more passed once the spacing an HTML extraction inserts before punctuation was normalized, and **8 were
dropped**; four quotations were added from the admission sweep's own checks.

**Thin admission, held plainly rather than hedged.** No standards body, government communication function,
or professional institute publishes this document by name. Admission rests on three sources, all vendor or
practitioner tier: Staffbase's blog, which names and defines the type with seven worked scenario templates;
GitLab's Communication handbook, which prescribes required content and a channel-reach gate for a
company-wide announcement; and Jason Fried's account of Basecamp's named "Deployment" post. A fourth
candidate, the US Army's AR 25-50 memorandum, was set aside during the admission sweep: the only link
between it and this type is the library's own catalog alias ("internal memo"), which would be the library
certifying itself rather than an outside body naming the type. The companion states the thinness of the
evidence rather than borrowing confidence the sources do not carry, and any specific number a source gives
(a notice window, a repetition count) is carried as that one organization's own house rule, never as a
general convention.

**Joins `delivery-docs` at `phase: deliver`, not the `communication-docs` family that forecast it.** The
`communication-docs` contract had named "a release announcement distinct from `release-notes`" as a likely
member. Its membership test fits this type; its only axis value does not, because `classification: utility`
was justified there as "maintained, periodic, valuable only while current," and this document is written
once and never revised. `delivery-docs`' membership test ("announces a unit of product work") admits the
type as written, and its `phase: deliver` axis describes it honestly. See
[ADR 0059 (announcement-internal-comms joins delivery-docs)](../../docs/internal/decisions/0059-announcement-internal-comms-joins-delivery-docs.md),
which carries the family contract to `0.2.0` together with
[ADR 0060 (change-request joins delivery-docs)](../../docs/internal/decisions/0060-change-request-joins-delivery-docs.md).
No obligation the contract already enforced changed: the new member is checked by section 2's same
`phase`/`status`/size-shape values as every other one.

### The line against `release-notes`, stated once and kept

The boundary between this type and its closest sibling is purpose, not audience: a release note is a
curated, user-impact record of what changed; this type says what that change means for one specific reader
and what they must do, then links to the release note rather than restating it. `release-notes_companion.md`
already recommends shipping the full notes internally, so a split drawn by audience instead would contradict
a shipped bundle. That boundary is this library's own; no source in the research log draws it in those
words, and the guide and companion both say so rather than presenting it as a finding.

### One size, and why no second was built

The template ships `[lean]` only. The strongest admission source publishes seven worked templates that all
share one shape, a subject line, a salutation, and three or four sentences, and its two highest-stakes
examples (a security incident, a major restructuring) differ from the rest of the set by one sentence, not
an added section. The material a heavier variant might plausibly add, a leadership quote or a linked FAQ,
appears in that same source only as optional best practice, never as a section inside any worked template.
Treated as provisional, following from the strongest source found rather than from a wide survey of longer
internal announcements.

### `pairs_with` resolved to empty

No skill in [`tools/known-skills.txt`](../../tools/known-skills.txt) addresses authoring a one-shot internal
announcement; nothing there names comms, announcements, or launches from the internal-audience side.
`pairs_with: []` is a deliberate, checked answer, in the same posture the `rfc` and `change-request` bundles
already take for the same reason.

### `related_templates` and the catalog entry

`related_templates` names the siblings this document actually connects to, drawn from the shared-example
chain: `prd` as the upstream decision this announcement translates, `release-notes` as its closest sibling by
purpose and the downstream public-facing record it links to rather than restates, `launch-coordination-checklist`
as the workstream this announcement's send step can close out, `status-report` as a document the example's
narrative cites for the surrounding period, and `test-plan`, `bug-report`, and `definition-of-done` as the
delivery-chain documents the worked example's launched feature carries provenance from.

The library's own catalog (entry 186, "Announcement / Internal Comms") lists aliases `internal memo`,
`launch announcement`, and `Slack canvas`, all three carried into this meta unchanged; no catalog value
needed correcting on landing.
