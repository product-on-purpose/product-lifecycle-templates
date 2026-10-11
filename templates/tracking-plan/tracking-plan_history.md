# tracking-plan: history

Change log for the `tracking-plan` bundle. Each entry records what changed and why, so a reader can tell a
correction from a preference.

## 0.1.0 - 2026-10-11

**Initial release.** Admitted as the sixth `governance-docs` member by
[ADR 0067 (tracking-plan joins governance-docs as a sixth member)](../../docs/internal/decisions/0067-tracking-plan-joins-governance-docs-as-a-sixth-member.md),
which lands the family contract at `0.4.0`. Assigned and specced 2026-10-06 in
[`tier2-specs.md`](../../docs/internal/tier2-specs.md), building on an admission sweep run 2026-10-05 while
the spec was written. Research conducted 2026-10-11 across a six-dimension fan-out: the vendor canon in two
parts (Avo and Twilio Segment; Amplitude, Mixpanel, mParticle and Countly), cadence, ownership, versioning and
privacy, contested practice, the boundaries with this library's neighbors and the worked example's facts, and
a standing gap question.
[`tracking-plan_research-log.md`](tracking-plan_research-log.md) records **37 sources, all
fetched-and-verified**. Every quotation was checked against each source's raw text rather than a retrieval
tool's summary of it: of 228 quotations the build's agents returned, 193 passed as normalized substrings, 19
more passed once a rendering artifact was removed, and the remainder were repaired or, where a cached page
escaped the characters a verbatim quote needed, described in the log's own words instead of quoted.

### Membership did not fit the family's test as written

Unlike the fourth and fifth members, this type's noun ("register") and cadence ("maintained indefinitely")
fit the family's existing test, but a tracking plan specifies what the product records rather than tracking
performance itself. ADR 0067 widens section 1 of the family contract with one clause, "or to specify what the
product records so that performance can be tracked", rather than stretching the existing wording to cover a
type the contract's authors had not anticipated.

### `pairs_with` resolved to empty, and checked against the pinned list

[`tools/known-skills.txt`](../../tools/known-skills.txt) carries no skill addressing event tracking,
analytics instrumentation, or a governance register of any kind; the family contract already states that no
governance skill exists in pm-skills today for any of its six members. `pairs_with: []` is a deliberate,
checked answer, in the same posture the `rfc`, `issue-log`, and `change-log` bundles already take for the
same reason.

### `related_templates` and the family it joins

`related_templates` names `kpi-dashboard` (the governance sibling this plan stands upstream of: the plan
defines the events a metric is computed from, the dashboard locks the metric's own formula), `prd` (a single
feature's events are first proposed in its own "Analytics and instrumentation" section, and this plan is what
every feature's slice merges into once it ships), and the other four `governance-docs` members this
contract's section 1 states the relationship against: `change-log`, `issue-log`, `risk-register`, and
`raid-log`. `experiment-design-doc` is also named, because the worked example's own exposure event is fixed
by that sibling's example and the companion's section 10 states the dependency directly. Two neighbors the
companion names in its Relationships section, the data dictionary and the broader measurement plan, are not
in this list because neither is a bundle this library has built; `related_templates` points at siblings that
exist, not at every artifact the companion discusses.

### `sizes_available` resolved to `[lean, full]`, following the shared spine plus a genuine second weight

Every admitting source shares a spine: a list of events, a reason for each, their properties and types,
where each comes from, and a status, which is what lean carries alongside the naming convention and the
plan's own ownership. A second weight earned its place on the same evidence the guide's "Pick a variant"
section states: more than one team changing the plan, personal or sensitive data in scope, or a need to
answer later what changed and who approved it. Full adds exactly the two sections that answer those signals,
Privacy, Sensitivity and Retention and Change Process and Version History, and nothing else.

### The honest core

No source read for this bundle measured whether keeping a tracking plan improves data quality or product
decisions. What the research supports is practitioner testimony about what goes wrong without one: a named
failure taxonomy and one practitioner's own claim that an ungoverned plan is "wrong within 60 days of
shipping," stated in the companion as that author's view, not a measurement. The guide and companion both
say the case for the document rests on that testimony and on the failure modes it names, not on a measured
result.

### What was not read, and is not claimed

Avo's "Tagging PII" and naming-conventions pages, Twilio Segment's own object-action naming spec, three
vendor pages on resolving anonymous and known users, and Mixpanel's event-approval page were each found and
not opened. The UK Information Commissioner's cookie guidance returned no body text, so this bundle cites no
regulator on consent, and gives no legal advice on consent or retention. No vendor spreadsheet template was
opened; this bundle's catalog table synthesizes the fields the vendors share rather than reproducing any one
vendor's column list.
