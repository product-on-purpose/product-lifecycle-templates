# Tier-2 build-out: per-type specs and progress

Companion to [`buildout-specs.md`](buildout-specs.md), which is the **Tier-1 floor** spec sheet and says so
in its own heading. That floor is complete, and this file is where a Tier-2 type's per-type judgment lives
instead.

It exists because the build runbook has a hole. [`bundle-pipeline.md`](bundle-pipeline.md) and the
`build-bundle` command both name "the type's spec in `buildout-specs.md`" as required reading before a
build starts, and for a Tier-2 type there is no such entry and never was. The first Tier-2 build would
otherwise have been exactly what `buildout-specs.md`'s preamble says a spec sheet prevents: "an open-ended
design task" rather than "a spec-driven execution".

> **A spec here is not a decision to build.** Build order is the maintainer's own preference and need
> ([ADR 0041](decisions/0041-maintainer-preference-sets-the-build-order.md)), and nothing on this page
> schedules anything. What a spec does is make the judgment reviewable *before* roughly 7M to 12M weighted
> token-equivalents, $14 to $41 at API list rates, are spent executing it
> ([measured](../../bundle-builds/INDEX.md); this sentence read "700K to 1M tokens" until 2026-09-22, an
> estimate nobody had measured, and "$33 to $41" until 2026-09-23, before the first build through the
> committed workflow cost $14.22).

## Progress

| Type | Catalog id | Family | Spec | Built |
|---|---|---|---|---|
| `spike-report` | `spike-research-spike-report` | `decision-docs` | **Written 2026-09-11**; researched 2026-09-11, [admission evidence](spike-report-admission-evidence.md) | **Built 2026-09-12.** Admitted by [ADR 0048](decisions/0048-one-named-source-clears-the-admission-test.md) |
| `project-milestone-retrospective` | `project-milestone-retrospective` | `process-docs` | **Written 2026-09-11** | **Built 2026-09-14**, shipped in `v0.8.0` |
| `pi-release-retrospective` | `pi-release-retrospective` | `process-docs` | **Written 2026-09-11** | **No, and it will not be.** Refused on its own evidence by [ADR 0049](decisions/0049-pi-release-retrospective-fails-the-admission-test.md): SAFe's own facilitator guide names the outputs as backlog items and no document |
| `test-summary-report` | `test-report-test-summary-report` | `qa-docs` | **Written 2026-09-11** | **Built 2026-09-14**, shipped in `v0.8.0` |
| `launch-coordination-checklist` | `launch-coordination-checklist` | `standing-standards` | **Written 2026-09-22**; admission source [retrieved the same day](#standing-standards-third-member-the-launch-coordination-checklist) | **Built 2026-09-22**, shipped in `v0.12.0`. [Build report](../../bundle-builds/reports/launch-coordination-checklist_v0.1.0.md): 15 agents, all resolved to Sonnet |
| `issue-log` | `issue-log` | `governance-docs` | **Written 2026-09-23**; admission sources [retrieved and raw-checked the same day](#governance-docs-fourth-member-the-issue-log-the-library-already-routes-to) | **Built 2026-09-23**, shipped in `v0.13.0`. Family by [ADR 0057](decisions/0057-issue-log-joins-governance-docs-as-a-fourth-member.md); [build report](../../bundle-builds/reports/issue-log_v0.1.0.md) |
| `definition-of-ready` | `definition-of-ready` | `standing-standards` | **Written 2026-09-23**; admission sources [retrieved and raw-checked the same day](#standing-standards-fourth-member-the-definition-of-ready-a-type-this-library-has-argued-against) | **Built 2026-09-23**, shipped in `v0.13.0`. Family and classification by [ADR 0058](decisions/0058-definition-of-ready-joins-standing-standards-as-a-foundation.md); [build report](../../bundle-builds/reports/definition-of-ready_v0.1.0.md) |
| `announcement-internal-comms` | `announcement-internal-comms` | `delivery-docs` | **Written 2026-09-25**; admission sources [retrieved and raw-checked the same day](#delivery-docs-new-member-the-internal-announcement-the-release-notes-guide-routes-to) | **Built 2026-09-25**, shipped in `v0.14.0`. Family by [ADR 0059](decisions/0059-announcement-internal-comms-joins-delivery-docs.md), not the `communication-docs` family that forecast it; [build report](../../bundle-builds/reports/announcement-internal-comms_v0.1.0.md) |
| `change-request` | `change-request` | `delivery-docs` | **Written 2026-09-25**; admission sources [retrieved and raw-checked the same day](#delivery-docs-new-member-by-amendment-the-change-request-two-bundles-route-to) | **Built 2026-09-25**, shipped in `v0.14.0`. Family by [ADR 0060](decisions/0060-change-request-joins-delivery-docs.md), which widens the contract's membership test; [build report](../../bundle-builds/reports/change-request_v0.1.0.md) |
| `change-log` | `change-log-governance` | `governance-docs` | **Written 2026-09-27**; admission sources [retrieved and raw-checked the same day](#governance-docs-fifth-member-the-change-log) | **Built 2026-09-28.** Family by [ADR 0061](decisions/0061-change-log-joins-governance-docs-as-a-fifth-member.md), which gives the contract's roles list a fifth role |
| `production-readiness-review` | `production-readiness-review` | `standing-standards` | **Written 2026-09-27**; admission sources [retrieved and raw-checked the same day](#standing-standards-fifth-member-the-production-readiness-review) | **Built 2026-09-28.** Family and classification (`tool`) by [ADR 0062](decisions/0062-production-readiness-review-joins-standing-standards-as-a-tool.md); [build report](../../bundle-builds/reports/production-readiness-review_v0.1.0.md) |
| `project-brief` | `project-brief` | `discovery-docs` | **Written 2026-09-27**; admission sources [retrieved and raw-checked the same day](#discovery-docs-reopened-third-member-the-project-brief-that-reopens-a-closed-family) | **Built 2026-09-29.** Family by [ADR 0063](decisions/0063-project-brief-reopens-discovery-docs.md), which reopens it after ADR 0035 had recorded it as closed at two; [build report](../../bundle-builds/reports/project-brief_v0.1.0.md) |
| `deployment-plan` | `deployment-plan` | none; all nine contracts exclude it | **Researched 2026-09-27**; no spec written | **No, and it will not be.** Declined by [ADR 0064](decisions/0064-deployment-plan-is-declined.md): five public-sector sources publish it, but its content already ships in `launch-coordination-checklist` and lives on IT service change records, and admitting it would reverse `delivery-docs`' production-change exclusion |
| `executive-briefing-steering-committee-deck` | `executive-briefing-steering-committee-deck` | none; forecast by `communication-docs`, never admitted | **Researched 2026-09-27**; no spec written | **No, and it will not be.** Declined by [ADR 0065](decisions/0065-steering-committee-pack-is-declined.md): its periodic written form is what `status-report` already is, its composite exists only as a deck, and the event-driven decision paper has no family |

**2026-09-27: one admission sweep, five candidates, three specs and two declines.** The maintainer queued
five candidates on 2026-09-25 from a ranked list of the next ten. One research workflow tested all five
against ADR 0030's admission test and against all nine family contracts, with no family assumed: 24 Sonnet
agents, 356 returned quotations re-checked against raw page text in the main loop. **All five cleared
admission.** What separated them was whether each is a distinct document and whether any family can hold it.
The change log and the production readiness review fit existing families as written. The project brief fits
only `discovery-docs`, which the maintainer chose to reopen. The deployment plan and the steering committee
pack are declined on duplication and family fit, not on a missing source, so neither record takes ADR 0049's
zero-source shape. Their catalog rows stay `candidate`, as ADR 0049 left its own.

**`launch-coordination-checklist`: family assigned 2026-09-20, specced 2026-09-22.** It joins
`standing-standards` as `classification: tool`, by
[ADR 0053](decisions/0053-launch-coordination-checklist-joins-standing-standards-as-a-tool.md). The
straddle that blocked it since 2026-09-11 was real (`release-notes` is `delivery-docs`, `runbook` is
`standing-standards`, and the catalog category names both), and it was resolved by ADR 0032's falsifier
rather than by the membership test: the type is **consulted at the moment of action**, which is what
`standing-standards` is for, and it carries no unit of product work, which is what `delivery-docs`
requires of every member.

**The spec is written, [below](#standing-standards-third-member-the-launch-coordination-checklist), and
the build was directed by the maintainer on 2026-09-22**, under
[ADR 0041](decisions/0041-maintainer-preference-sets-the-build-order.md)'s rule that the maintainer's
preference sets the build order.

> **One correction landed with the assignment.** The promise tag in `release-notes_meta.yaml` read
> `future:launch-checklist` while the catalog id is `launch-coordination-checklist`.
> `tools/check-bundles.py` resolves `future:` targets **by bundle id** and raises its stale-reference
> failure only when that exact id appears on disk, so building under the catalog id would have left a
> promise pointing at an id that never arrives **with the gate still green**. The tag now reads
> `future:launch-coordination-checklist`.

> **`solution-brief` is resolved, 2026-09-20: the two tags were retired rather than the type admitted.**
> `prd_meta.yaml` and `rfc_meta.yaml` both carried `future:solution-brief`, promising readers a type with
> **no catalog entry at all** - so it had never faced
> [ADR 0030](decisions/0030-templating-scope-markdown-documents.md)'s admission test and could not be
> specced or built. Open since 2026-07-21.
>
> **Retiring was chosen over adding a catalog entry, and the order is the reason.** Adding an entry first
> would admit a type on the strength of two `related_templates` tags rather than on evidence, which is the
> expensive order and the one `prototype-brief` already proved wrong: it failed 0030's test with zero named
> sources after a full research pass. A promise is not evidence. **If `solution-brief` is ever wanted, it
> enters through the front door** - a research pass, a named source, a catalog entry, then a tag - and
> pm-skills shipping `develop-solution-brief` is an argument for starting that pass, not a substitute for it.

---

## Per-type specs

### decision-docs (fourth member; the family's first Tier-2 candidate)

**spike-report** - `decision-docs`, **phase develop**, sizes **`[lean]`** (single-size), methodology
**`agile`**, catalog id `spike-research-spike-report`, aliases: `spike`, `technical investigation`.
Catalog owner: Engineer. Catalog purpose: "Time-boxed investigation to reduce uncertainty."

#### Admission, which is settled at the family level and open at the type level

**Settled: a fourth member needs no contract change.**
[ADR 0022](decisions/0022-adopt-decision-docs-family-contract.md) says so in its Consequences, in these
words: "a fourth (a spike report, a solution brief) would join under the same contract with no contract
change unless it declares a different phase or size shape." It declares neither. The
[contract](contracts/decision-docs.md) gates `phase: develop`, and `adr`, `rfc` and `sdd` all declare
exactly that; the catalog's `stage: decision` is the **catalog's** axis and not the bundle's, so it is not
in tension with anything.

> **Read the contract and the ADR together or not at all.** The contract's section 1 says "the family's
> three roles are distinct", which read alone suggests a fourth role is a problem. The record that adopted
> it says the opposite and settled the question on 2026-07-21. A previous session read only the contract,
> concluded a spike report might not be admissible, and overrode a correctly-ranked candidate on that
> basis. The contract carries the rule; the ADR carries what the rule deliberately leaves open.

**The research ran on 2026-09-11 and the answer is "barely, and it is now a maintainer decision."** Full
evidence: [`spike-report-admission-evidence.md`](spike-report-admission-evidence.md) - a 72-record fan-out
across six dimensions, merged to **68 unique sources, 57 fetched-and-verified** once four same-page pairs
were collapsed.

**Exactly one named source publishes a spike report as a written document**: Microsoft's Code with
Engineering Playbook, which states the deliverable "should be a document" and ships a fill-in template
(*Goal / Method / Evidence / Conclusions / Next Steps*), both verified against the raw markdown in the
GitHub repo. **The term's own inventors publish the opposite**: Ward Cunningham's c2 account, crediting
Kent Beck, describes the output as throwaway **code**, and Mike Cohn describes an activity, not a document.
SAFe's readable text never uses "document" or "report"; the widely repeated "documented finding" phrasing
traces to training-vendor content marketing.

**This is not the `prototype-brief` shape.** That failed with *zero* qualifying sources. This has one,
verified and current, standing against the canon. Whether one is enough is a reading of ADR 0030 - which
says "a named source", singular - and **a build must not start until the maintainer rules**, because
"whether a type is in scope at all" is on the stop-for-the-maintainer list. **The prior stated in the
paragraph this replaces was wrong**: it assumed XP's literature would supply the document, and XP's
literature is the strongest evidence against.

#### The fourth role, which is what it adds

The contract frames the family as three distinct roles: an RFC **proposes** a technical decision, an ADR
**records** one, an SDD **describes** the design that implements it. A spike report **investigates** the
question that precedes all three, and hands over evidence plus a proceed-or-not recommendation.

That boundary is not this library's invention. The paired pm-skills skill draws it in its own description:
*"For the architecture decision the spike informs, use `develop-adr` instead; for research-based
exploration, use `discover-interview-synthesis`."* The companion's cross-reference obligation (contract
section 4) therefore has a fourth edge to place correctly, and the easiest error to make is letting the
spike report drift into being an ADR with a longer preamble. **A spike report that recommends without
recording what was tried is a bad ADR; an ADR that shows its working is not a spike report.**

#### Section design

Single-size, so there is no nesting obligation and no `full` variant to diverge from. Six sections,
derived from what the practice actually produces:

| Section | What it carries |
|---|---|
| **The Question** | The uncertainty being reduced, written so it can be answered yes or no. A spike with no answerable question is a research project |
| **Time Box** | What was allotted and what was actually spent. This is the section that distinguishes a spike from open exploration, and the one most likely to be quietly dropped |
| **What Was Tried** | Approach, and what was deliberately not attempted. The scope boundary is evidence |
| **What Was Found** | Evidence-backed findings. Facts observed, separated from what they imply |
| **Recommendation** | Proceed, do not proceed, or a named next spike. Explicit, not inferred from tone |
| **What This Does Not Settle** | The open questions the spike did not close, so the next reader does not mistake a bounded answer for a general one |

The last section is a deliberate departure from the paired skill's four-part shape (question, approach,
findings, recommendation) and should be defended or dropped on research evidence like any other. The case
for it: this library's whole credibility posture is not claiming more than was earned, and a time-boxed
investigation is the document type where over-claiming is most natural, because the box closes whether or
not the question was answered.

> **The 2026-09-11 research defends it, and by a route worth reading.** The blinded gap dimension - which
> never saw this table - found that an explicit, named non-scope section is **the single most consistent
> element that real filled spike reports supply and the naive four-part shape omits**, present under four
> different headings across four unrelated projects (`## Out of scope for this spike`, `Non-goals for now`,
> `## Not covered here`, `Follow-ups (deferred, not in v1)`). Meanwhile the structure dimension found that
> **not one blank template asks for it.** Every template omits it; the good filled reports include it
> anyway. Three caveats travel with that finding (selection bias toward structured reports, a corpus
> showing signs of agent-authored drafting, and three distinct genres that must not be pooled) and they are
> recorded in [`spike-report-admission-evidence.md`](spike-report-admission-evidence.md).
>
> **The same research weakens `Time Box` as its own section.** A dedicated time-box heading appears in
> *pre-spike planning* artifacts (a Jira ticket field, a spike plan's "Deadline") and is usually **absent**
> from the report of a completed spike. If this bundle is built, that section must be argued from evidence
> or folded into Scope.

#### Metadata

| Field | Value | Why |
|---|---|---|
| `family` | `decision-docs` | ADR 0022 |
| `phase` | `develop` | Contract-gated; matches all three existing members |
| `sizes_available` | `[lean]` | Catalog `size_variant: S`. The contract admits `[lean]` for a single-size type, and exempts it from nesting, not from anything else |
| `status` | `beta` | Contract: `beta` until the maintainer judges it settled ([ADR 0055](decisions/0055-retire-the-zero-fills-disclosure.md)) |
| `methodology` | `agile` | **The first decision-docs member to declare a non-generic methodology.** The catalog says Agile/XP, and a spike is genuinely an XP practice rather than a methodology-agnostic instrument. The contract anticipated exactly this: methodology is "descriptive, not gated ... a future member is free to declare otherwise rather than have the truth bent to a rule" |
| `pairs_with` | `[develop-spike-summary]` | Verified present at `skills/develop-spike-summary/SKILL.md` in product-on-purpose/pm-skills on 2026-09-11, v2.2.0, `phase: develop`. Added to `tools/known-skills.txt` in the same change as this spec |
| `related_templates` | `[adr, rfc, sdd]` | Its three siblings |

#### Two things landing this bundle would close elsewhere

1. **`templates/adr/adr_meta.yaml` carries `related_templates: [rfc, sdd, future:spike-report]`.** The
   `future:` prefix is the gate's sanctioned way to reference an unbuilt type, and check I fails a
   `future:` reference whose target the library has since built. **So the bundle directory must be named
   `spike-report`, not the catalog id.** That matches the house rule that bundle ids are bare
   document-type handles ([ADR 0005](decisions/0005-bundle-ids-doctype-spine.md)) while catalog ids are
   long-form: `architecture-decision-record` in the catalog is `templates/adr/` on disk.
2. **The example-independence rule applies.** Contract section 5: decision-docs examples are deliberately
   independent, each a different real decision, because the family teaches the *distinction* between roles
   rather than one thread. So this bundle's example must not extend the Acme Analytics chain, and
   `tools/check-example-independence.py` enforces it.

#### Not applicable, stated so nobody applies it

**The Tier-2 active-practice test does not gate this type.** The pull-queue rule applies that bar "whenever
a Tier-2 **methodology pack** is built" - a Scrum or SAFe or XP *collection*. A single methodology-leaning
document type is not a pack, and `tier_inferred: true` on the catalog row means even the tier itself is a
derived guess rather than a maintainer's call.

---

## What a spec on this page is worth

The same as one in `buildout-specs.md`, which is to say provisional. Every per-type spec in that file was
written before its research pass, and **four of `user-persona`'s section calls were overturned by its own
research** and recorded as departures in its research log. That is the system working: the spec front-loads
judgment so the research has something specific to disagree with. Expect these to be wrong somewhere,
and expect the research logs to say where.

---

### process-docs (members three and four; build them as one job)

**`project-milestone-retrospective`** - `process-docs`, **phase iterate**, methodology **`pmbok-agile`**,
catalog id `project-milestone-retrospective`, aliases: `lessons learned`, `post-project review`,
`after-action review`. Catalog owner: PM / PgM. Purpose: "Capture lessons at project/milestone close."

**`pi-release-retrospective`** - `process-docs`, **phase iterate**, methodology **`safe-scaled`**, catalog
id `pi-release-retrospective`, aliases: `inspect & adapt (SAFe)`, `release retro`. Catalog owner: RTE / PM.
Purpose: "Reflect and improve at PI/release cadence."

#### Admission: the contract names both of them, by id

The [`process-docs` contract](contracts/process-docs.md) lists under **Likely future members, if pulled**:
`project-milestone-retrospective` and `pi-release-retrospective`, by exact catalog id. The family's axis is
`phase` with the single value `iterate`, and a retrospective at any cadence is an iterate-phase artifact by
construction. **There is no family question to answer here**, which is what makes this pair the cheapest
admission in the Tier-2 catalog.

ADR 0030's admission test still has to be met by research, and the prior is strong but is not a retrieval:
`after-action review` is a named, published US Army artifact with doctrine behind it, `lessons learned` is a
named PMBOK artifact, and SAFe publishes Inspect & Adapt. **All three have to be read, not assumed.**

#### Build them as one job, and why

They share almost their whole research base: the retrospective literature (Kerth, Derby and Larsen), the
PMBOK lessons-learned line, the SAFe Inspect & Adapt line, and the scope-and-cadence debate that separates
them. Two fan-outs over the same sources would pay for those pages twice and produce two research logs that
then have to be reconciled.

**One research pass, one contested register, two bundles.** The family goes from two members to four in a
single build, which is also the first time `process-docs` has enough members to teach its own boundary.

#### The distinction that is the whole teaching point

`sprint-retrospective-notes` already ships and looks back on **a period, on a cadence, at how the team
worked**. These two are not more of that at a larger size, and a spec that treats them that way will produce
three documents nobody can tell apart.

- **`project-milestone-retrospective`** looks back on **a bounded piece of work that has ended**. It is
  terminal: the project is over, the team may disperse, and part of the audience was not there. That is why
  its aliases are `lessons learned` and `post-project review` - the output is meant to outlive the team that
  produced it, which a sprint retro's output explicitly is not.
- **`pi-release-retrospective`** looks back on **a scaled cadence across multiple teams**. Its distinguishing
  feature is not duration but **breadth**: it reconciles findings no single team can see, which is what
  SAFe's Inspect & Adapt is built around.

The built bundle's companion already cites sources that separate these: material describing use "in a longer
iteration, release, or project retrospective", a source giving release and project retrospectives their own
chapter, and InfoQ distinguishing a sprint retrospective from a release retrospective on scope and strategic
framing. **That is inherited evidence and must be re-read at its source, not carried across.**

#### Section design, and the honest uncertainty in it

The classic five-stage retrospective shape (set the stage, gather data, generate insights, decide what to do,
close) is Derby and Larsen's, and it describes **facilitating a session**. These are **documents**, and the
document of a session is not the agenda of one. Proposed:

| Section | Both | Notes |
|---|---|---|
| **Scope and Period** | yes | What is being looked back on, and its boundaries. The section that stops these three documents blurring |
| **What Happened** | yes | The factual record, separated from interpretation |
| **What Worked** | yes | |
| **What Did Not** | yes | |
| **Lessons for Others** | `project-milestone` only | The terminal-handover section, whose whole reason for existing is a reader who was not there |
| **Cross-Team Findings** | `pi-release` only | The breadth section: findings no single team could have seen |
| **Actions and Owners** | yes | With owners and dates, or it is a feelings log |

**Expect the research to move this**, and the contract says so itself: `sizes_available` may be `[lean]`
"where the type's research shows it does not earn a second weight", and it warns to **expect pressure** on
exactly that question. The catalog says `size_variant: M` for both, and `sprint-retrospective-notes` shipped
single-size against a similar prior.

#### Metadata

| Field | `project-milestone-retrospective` | `pi-release-retrospective` |
|---|---|---|
| `family` | `process-docs` | `process-docs` |
| `phase` | `iterate` (contract-gated, single value) | `iterate` |
| `sizes_available` | `[lean, full]` **provisional** | `[lean, full]` **provisional** |
| `status` | `beta` | `beta` |
| `methodology` | `pmbok-agile` | `safe-scaled` |
| `pairs_with` | **open, see below** | **open, see below** |
| `related_templates` | `sprint-retrospective-notes`, `incident-postmortem` | same |

#### One inherited question this spec will not answer quietly

`pairs_with` is **`[]` on both built members**, and the obvious pm-skills candidate is
`iterate-retrospective`, whose own description reads: "Use at the end of a sprint, **project, or milestone**
to reflect and improve team practices."

**That description names the sprint, and `sprint-retrospective-notes` still declares `pairs_with: []`.** So
either the built bundle's empty pairing is a miss nobody has revisited, or it was deliberate and the
reasoning is not recorded where a later reader finds it. **Pairing these two while the sprint bundle pairs
with nothing would make the family internally inconsistent**, and silently pairing all three is a change to
a shipped bundle that a Tier-2 spec has no business making.

Resolve it explicitly during the build: read the skill in full, decide for all three members together, and
record the decision. `iterate-retrospective` is **not** in `tools/known-skills.txt`, so pairing also requires
verifying it and adding it per that file's own procedure.

---

### qa-docs (fourth member), and the paywall that shapes the whole build

**`test-summary-report`** - `qa-docs`, **phase develop**, sizes `[lean, full]`, methodology **`generic`**,
catalog id `test-report-test-summary-report`, aliases: `test results`, `test completion report`. Catalog
owner: QA Lead. Purpose: "Summarize test execution outcomes and quality status."

#### Demand: the library already sends readers to a document it does not ship

The strongest inbound signal in the Tier-2 catalog, and it is self-inflicted. `templates/test-plan/` ships
all of the following today:

- `test-plan_guide.md`: a "You actually need" row reading **"You need a test report."**
- `test-plan_guide.md`: a routing row, "What we found, and whether we are shipping" to **"A test report"**
- `test-plan_companion.md`: "Results, status and the verdict live in **the test report** and the test tool, not here"
- `test-plan_template-full.md`: the document is "NOT a test report (that is retrospective, written after)"

**Four places send a reader to a document this library does not have.** No `future:` tag records that
promise, which is why no gate has ever flagged it.

#### Admission, and where it is genuinely less settled than the spike report

**ADR 0030's test is met on the strongest possible evidence, with one enormous caveat.**
**ISO/IEC/IEEE 29119-3** is an international standard whose entire subject is software test documentation,
and it defines a **Test Completion Report** - which is one of this type's catalog aliases, verbatim. A named
source does not get more named than that.

**The caveat: nobody in this library has read it, and it may not be readable.** The `test-plan` bundle's
research log already establishes from its own retrieval that **29119-3 is paywalled** at ISO, IEEE and BSI,
and states plainly: "Nobody in this research read 29119-3." Under honest retrieval that source may be cited
`url-confirmed-not-read` and **nothing may be quoted from it, and no claim may rest on it alone.**

So this build's central research risk is known in advance and specific: **the most authoritative source for
this document's structure cannot be read, and its readable predecessor (IEEE 829-2008) is superseded and also
sold, with second-hand enumerations of its contents that already disagree** - the `test-plan` research found
a vendor claiming 16 sections against a different count elsewhere. A section design resting on second-hand
descriptions of a superseded standard is not a section design; it is a rumour with a table.

**The research must find the structure somewhere readable** - published practitioner templates, open-source
project QA documentation, tool-generated report formats - and say openly that the standard is cited for
existence and authority rather than for content. If it cannot, that is a finding, and a thin honest bundle
beats a confident one.

**The family question is a genuine judgment call, unlike the spike report's.** The `qa-docs` contract admits
a type whose job is to "plan, specify, or **report the verification of a product increment**", which this
does exactly. But its three named roles assign the *reporting* role specifically to the bug report ("records
one verification that **failed**"), and **[ADR 0026](decisions/0026-adopt-qa-docs-family-contract.md)
contains no fourth-member clause** - unlike [ADR 0022](decisions/0022-adopt-decision-docs-family-contract.md),
which admits a fourth `decision-docs` member in as many words. Read together, the contract admits it on its
exclusion clause and is silent in its role list. **That is close enough to be a maintainer decision rather
than a spec-writer's**, and it is flagged here rather than assumed.

#### Section design

| Section | In lean | Notes |
|---|---|---|
| **Scope and What Was Tested** | yes | What the report covers, and against which plan |
| **Execution Summary** | yes | Run, passed, failed, blocked, not run. The counting section |
| **Defects** | yes | What was found, by severity, and what remains open |
| **Quality Assessment** | yes | The judgement the numbers do not make by themselves |
| **Release Recommendation** | yes | Ship, do not ship, or ship with named conditions. Explicit |
| **Variances from Plan** | full only | What was planned and not done, and why. Most likely to be omitted, most likely to matter |
| **Residual Risk** | full only | What remains untested, and what that exposes |

**`Release Recommendation` is the load-bearing section**, and the one separating this document from a tool's
exported test run. A CI dashboard can produce every number in Execution Summary. It cannot say whether to
ship.

#### Metadata

| Field | Value |
|---|---|
| `family` | `qa-docs`, pending the admission judgment above |
| `phase` | `develop` (contract-gated) |
| `sizes_available` | `[lean, full]`, matching its three siblings and the catalog's `size_variant: M` |
| `status` | `beta` |
| `methodology` | `generic`. The catalog says methodology-agnostic and a test report genuinely is |
| `pairs_with` | `[deliver-edge-cases]` or `[]`. `test-plan` pairs with `deliver-edge-cases`; whether an edge-case skill honestly pairs with a *report* is weaker and should be argued or dropped. **pm-skills has no testing or QA reporting skill** (finding EC-4) |
| `related_templates` | `test-plan`, `test-case`, `bug-report` |

#### Two obligations inherited from the family

1. **The example chains.** Unlike `decision-docs`, `qa-docs` examples chain on one shared scenario: the plan
   schedules the case, and the case that fails produces the bug report. **This bundle's example must close
   that chain on the same feature**, reporting the run that produced the existing bug report. That is the
   most valuable thing this bundle adds, because it completes the end-to-end thread from PRD to a shipping
   verdict.
2. **The standards-recency trap is a citation obligation**, per the contract's section 3.6 and ADR 0026.
   Every member must get IEEE 829's status right - **superseded, not withdrawn** - verified at the IEEE SA
   page rather than inherited from this file or from the catalog.

---

### standing-standards (third member): the launch coordination checklist

**`launch-coordination-checklist`** - `standing-standards`, **`classification: tool`**, sizes
**`[lean, full]`** (provisional), methodology **`SRE`**, catalog id `launch-coordination-checklist`
(catalog 126), alias: `launch checklist (SRE)`. Catalog owner: Launch Coordinator / SRE. Purpose:
"Coordinate cross-team launch readiness." Contents, per the catalog: "dependencies, monitoring, comms,
rollback, sign-offs". `size_variant: M`, `rarity: rare`, `tier_inferred: true`. **The catalog row's own
source column reads "Google SRE appendix."**

#### Admission: retrieved rather than assumed, which no earlier spec on this page could say

**The family question is settled.**
[ADR 0053](decisions/0053-launch-coordination-checklist-joins-standing-standards-as-a-tool.md) assigned the
type to `standing-standards` as a `tool`, and the [contract](contracts/standing-standards.md) names it as a
member.

**The type-level test was answered by a retrieval made while writing this spec.** Every earlier spec here
carried a prior into its research pass; this one carries a source. On 2026-09-22
<https://sre.google/sre-book/launch-checklist/> was fetched and read in full. It is Appendix E of Google's
*Site Reliability Engineering* (O'Reilly, 2016), titled **"Launch Coordination Checklist"**, the catalog's
name verbatim, and it introduces itself as "Google's original Launch Coordination Checklist, circa 2005,
slightly abridged for brevity". A named source publishing the type as a written document, under the type's
own name, clears [ADR 0030](decisions/0030-templating-scope-markdown-documents.md)'s test on
[ADR 0048](decisions/0048-one-named-source-clears-the-admission-test.md)'s one-source reading with room to
spare, and it is the source the catalog already credits.

**What it contains, counted from the page's HTML rather than from a summary of it:** ten areas, 31 items.
An automated summary of the same page reported nine areas while listing ten, which is why the count was
redone by hand.

| Area | Items |
|---|---:|
| Architecture | 2 |
| Machines and datacenters | 2 |
| Volume estimates, capacity, and performance | 4 |
| System reliability and failover | 6 |
| Monitoring and server management | 5 |
| Security | 2 |
| Automation and manual tasks | 2 |
| Growth issues | 3 |
| External dependencies | 3 |
| Schedule and rollout planning | 2 |

**Four properties of that source shape the build, and each is a trap if it is missed:**

1. **It is a topic list, not a checklist in the checkable sense.** Every item is a noun phrase ("Storage
   capacity", "Monitoring the monitoring"). None is a question with a pass condition, and none has an
   owner. The research must establish whether the practice around it, chapter 27 ("Reliable Product
   Launches at Scale"), supplies the questions, owners and pass conditions, or whether this bundle
   supplies them and says so.
2. **It omits most of what the catalog row lists.** No sign-off, no go/no-go decision, no rollback (only
   "canaries under live traffic, staged rollouts"), and no launch communications. Of "dependencies,
   monitoring, comms, rollback, sign-offs", only the first two appear. Any section carrying the rest must
   be sourced elsewhere or labelled as this bundle's own contribution, the way `spike-report` labelled its
   non-scope section.
3. **It is twenty years old and describes one company's infrastructure**: "circa 2005", "N+2
   redundancy", "Don't crash mail servers by sending yourself email alerts in your own server code". The
   companion must present it as the named origin of the type, not as current practice. That is this
   family's citation hazard (contract section 3.6, "folklore presented as standard") running in reverse: a
   real historical artifact presented as a present-day standard.
4. **It is licensed CC BY-NC-ND 4.0: no derivatives.** The bundle may cite it and quote it briefly. **The
   template must not be an adaptation of its items**, and the example must not reproduce its list. This is
   the first source in the library whose licence constrains the template rather than only the citation.

**The build still records admission properly.** The research pass logs this source with a retrieval
status like any other, and looks for a second: a production or operational readiness review published as
a document. The catalog relates the type to PRR, and the SRE book's chapter on its engagement model is the
first place to look. One source suffices; a second would change the teaching.

#### The design question that is actually open: a standing checklist, or one filled per launch

The contract's membership test is "agreed once and applied every time", and its own change note concedes
the test "is genuinely ambiguous for a launch checklist, which is arguably written per launch". The two
sources in hand pull opposite ways:

- **Google's checklist is standing.** One list, reused across launches, and each launch answers it.
- **pm-skills' `deliver-launch-checklist` is per launch.** It "Creates a cross-functional pre-launch
  checklist covering engineering, design, marketing, support, legal, and operations readiness, with
  owners, dates, and go/no-go criteria", used "1-2 weeks before any significant launch".

**Proposed resolution: the template is the standing checklist, and a per-launch record is what applying
it produces.** That is the move the contract already makes for the runbook ("a runbook written for one
incident is an incident report"): the instrument is standing and its execution is per occasion. It keeps
ADR 0053's assignment honest, and it turns the pairing into a question of grain rather than of kind: the
skill produces the per-launch copy, and this template is what the copy is made from.

**If the research shows practitioners do not keep a standing launch checklist at all**, so that every
published instance is a per-launch plan, then ADR 0053's assignment is wrong on evidence and the build
**stops for the maintainer**, because that is a change in the decision rather than in the design.

**The scope question rides with it.** Google's list is engineering readiness only; the paired skill and
the catalog row both reach into communications and sign-off. The proposal below keeps engineering
readiness as the core and carries the cross-functional parts as full-only sections, so a lean fill stays
an engineering instrument. The research decides whether that line is drawn in the right place.

#### Section design

Provisional, derived from the source's shape and the catalog row, and expected to move:

| Section | In lean | What it carries |
|---|---|---|
| **Scope and Launch Classes** | yes | What counts as a launch here, and which classes of launch get the full list. A launch checklist with no scope rule is applied to everything or to nothing |
| **Roles and Sign-off** | full only | Who coordinates, and who can say no. The source names no roles; the catalog names sign-offs |
| **Readiness Checks** | yes | The load-bearing section: checks grouped by area, each a question with the evidence that answers it and the role that owns it. A table section, so it carries PRIORITY and ROW HINT guidance |
| **Launch Communications** | full only | Who must know before, at and after the launch: support, documentation, and the announcement. The edge with `release-notes` lives here |
| **Rollout and Rollback** | full only | How the launch is staged, and the condition that reverses it, stated before the launch rather than argued during it |
| **Go/No-Go Criteria** | yes | What blocks a launch, decided in advance. The difference between a checklist and a list |
| **When This Does Not Apply** | full only | Launches exempt from the list, and what they get instead. Mirrors `runbook` |
| **Review Trigger** | yes | **Contract-mandated** (section 4): a named owner and a condition, not a calendar. The obvious candidate: a launch causes an incident a check should have caught, which ties the trigger to `incident-postmortem` |

**`Readiness Checks` is where the licence bites.** The ten areas above are a reasonable taxonomy, but the
section must be built from the categories the research finds across sources, not as a restyling of one
no-derivatives list.

#### What makes it not a sibling

The companion's cross-reference section has three edges to place, and each is a likely drift:

- **Not a `runbook`.** A runbook responds to a situation that has occurred; a launch checklist prepares
  for an event that has not. Both are `tool` and both are SRE-lineage, and a launch checklist whose
  checks have turned into procedures has become a runbook.
- **Not `release-notes`.** Readiness versus announcement, a line the paired skill draws in its own
  description: "For the customer-facing announcement of what shipped, use deliver-release-notes instead."
  `release-notes_guide.md` already routes "a full launch plan and comms" here.
- **Not a production readiness review.** The catalog relates the type to PRR. Whether a PRR is a
  different document or the same instrument at a different gate is a research question, and the answer is
  a teaching point either way.

#### Metadata

| Field | Value | Why |
|---|---|---|
| `family` | `standing-standards` | ADR 0053 |
| `classification` | `tool` | ADR 0053: "an instrument you execute", sibling of `runbook` |
| `sizes_available` | `[lean, full]` **provisional** | Catalog `size_variant: M`, and both siblings ship two weights. The contract allows `[lean]` "where the type's own research shows it does not earn a second weight" |
| `status` | `beta` | Every bundle |
| `methodology` | `SRE` | The catalog's value. `runbook` declares `DevOps/SRE-lineage` and the contract leaves methodology descriptive, so pick one wording deliberately at build time rather than by copying |
| `pairs_with` | `[deliver-launch-checklist]` **provisional** | Verified present at `skills/deliver-launch-checklist/SKILL.md` on pm-skills `origin/main` (released at v2.33.0; the skill's own version is 2.2.0), `phase: deliver`, on 2026-09-22, and added to `tools/known-skills.txt` in the same change as this spec. **Honest only if the standing-versus-per-launch resolution above holds**; otherwise `[]` |
| `related_templates` | `[release-notes, runbook, incident-postmortem]` **provisional** | The type that promised it, its sibling instrument, and the document its Review Trigger fires on |

#### What landing this bundle closes elsewhere

1. **`release-notes_meta.yaml` carries `future:launch-coordination-checklist`**, the only `future:` tag
   in the tree. Check I fails a `future:` target that has been built, so the build drops the prefix in the
   same change. The bundle directory is `launch-coordination-checklist`, the id ADR 0053 fixed the tag to.
2. **The `standing-standards` contract's Members line**, which records whether the member is specced and
   built.
3. **This page's Progress table.**

#### The example

**A standing checklist belonging to a team, not a moment in a story**, which is the contract's own caveat
about chaining in this family. The natural owner is Acme Analytics' platform team, and the natural
demonstration is its checklist as it stood when the Saved Views launch consulted it, so it can chain to the
`sdd`, `test-plan` and `release-notes` examples without pretending to be a per-launch record. Contract
section 3.7 applies in full: no placeholders, illustrative figures labelled, and independent of the
template's GOOD and WEAK text. **It must not reproduce Google's items**, per the licence.

#### What the build costs, and what it settles at no extra cost

Measured, a whole bundle build is about **10M to 12M weighted token-equivalents, or $33 to $41 at API list
rates** ([`bundle-builds/INDEX.md`](../../bundle-builds/INDEX.md)), with drafting over two thirds of the
dollars because its agents resolved to Opus in both measured builds. **This build is the first whose report
can say why**, because every agent label now carries its bundle type. Projected from the two measured builds'
token counts:

- drafting resolves to **`claude-sonnet-5`**: the pin works, the measured builds ran from a drifted working
  tree, and the build costs about **$20 to $24**;
- **`claude-opus-5-5`**: the drafting agents inherit the session's model, so the pin is not being applied,
  at about **$24 to $29**;
- **`claude-opus-5`**: no longer the session model and pinned nowhere, so only a cached or resumed run could
  produce it, at about **$33 to $41**.

Run `python tools/gen-bundle-build-report.py --ingest` in Phase 6, on the machine that ran the build.

**Outcome, 2026-09-22.** Drafting resolved to **`claude-sonnet-5`**, but **none of the three causes above
was the right one.** The measured builds never ran `build-bundle.js`: the drafting scripts that session
actually executed, saved beside its transcripts, were written per bundle and pinned no model at all. This
build, the first through the committed script, cost **7,108,920 weighted token-equivalents, $14.22 at API
list rates** for its subagents ([report](../../bundle-builds/reports/launch-coordination-checklist_v0.1.0.md)),
below the $20 to $24 projected above, because every stage was smaller than in the measured builds and not
only drafting. The orchestrator's own spend is not in that figure.

---

### governance-docs (fourth member): the issue log the library already routes to

**`issue-log`** - `governance-docs`, **`classification: utility`**, sizes **`[lean, full]`** (provisional),
methodology **`generic`**, catalog id `issue-log` (catalog 152), aliases `issue register`, `issue tracker`.
Catalog owner: PM. Purpose: "Track active issues needing resolution." Contents, per the catalog: "issue,
owner, priority, status, resolution". `size_variant: S`, `rarity: common`, `tier_inferred: true`,
`relationships: [RAID]`.

#### Demand: promise debt in two shipped bundles, in the shape that found `test-summary-report`

The library sends readers to this document from both of its sibling registers, and no `future:` tag
records the promise, which is why no gate has flagged it:

- `risk-register_guide.md` and `raid-log_guide.md` each carry a chooser table with an **Issue log**
  column ("Register, RAID log, or issue log?" and "RAID log, risk register, or issue log?").
- `risk-register_template-lean.md` says the register "is NOT an issue log", and both risk-register
  templates send a materialized risk to "the issue log".
- `risk-register_guide.md`'s rubric fails a row that "has already happened" ("that belongs in the issue
  log"), and its anti-patterns say to "move materialized risks to the issue log".
- `raid-log_guide.md` routes a reader with only realized problems away from RAID: "if that is all you have,
  an issue log is enough."

**The family is settled by [ADR 0057](decisions/0057-issue-log-joins-governance-docs-as-a-fourth-member.md)**:
`governance-docs`, `utility`, the fourth member, contract to `0.2.0`. Built on the maintainer's direction of
2026-09-23 under [ADR 0041](decisions/0041-maintainer-preference-sets-the-build-order.md) (GitHub issue
#176, build-candidate 2).

#### Admission: retrieved, and the widest named-source base of any Tier-2 spec on this page

Every quotation below was checked against the source's raw text on 2026-09-23, not against a retrieval
tool's summary of it. **Four named bodies define the type by name, and one of them publishes it under an
open licence that permits adaptation.**

| Source | What it says | Licence |
|---|---|---|
| European Commission, *PM² Project Management Methodology Guide* v3.1 (Publications Office of the EU, 2023), Appendix B.9 | "The Issue Log is a register (log file) used to capture and maintain information on all issues that are being formally managed" | **CC BY 4.0** |
| PMI, *Lexicon of Project Management Terms* v5.0 (January 2026) | "issue log. A project artifact where information about issues is recorded and monitored." | PMI, personal use only |
| PMI, *PMBOK Guide* 6th edition, errata (fifth printing) | "Issue log. Described in Section 4.3.3.3." The Guide itself is sold and was not read | PMI |
| APM, glossary (read 2026-09-23) | "A log of all issues raised during a project or programme, showing details of each issue, its evaluation, what decisions were made and its current status." | not stated |
| PRINCE2 2009 glossary, reproduced with AXELOS's permission (stakeholdermap.com) | Issue register: "A register used to capture and maintain information on all of the issues that are being managed formally" | AXELOS, all rights reserved |

Readable templates from four public bodies supply the structure the standards describe: the Northern
Ireland Civil Service's *Issue Log* (whose own text says it is "based on the PRINCE2 recommended issue log"),
the Tasmanian Government's *Project Management Guidelines* v7.0 (2011) "Project Issues Register", the
Connecticut Department of Social Services' *Project Issue Log* v1.13, and Washington State OFM's issue
tracking template. **None states a reuse licence, so they are structure evidence only, never wording.**

**What was not read, and must be cited as such.** AXELOS's own manuals (PRINCE2 6th edition 2017, PRINCE2
Agile 2016, PRINCE2 7 2023) are behind a subscription and were not retrieved. ISO 21502:2020 was read only as
its official free preview: clause 3.11 defines an issue ("event that arises during a project ... requiring
resolution for the project to proceed") and the contents list "7.9 Issues management", but the clause body is
past the preview. **ISO frames a practice, not a named document, in everything readable**, and the bundle must
not claim otherwise. The UK government's Teal Book chapter on issue management refused every raw fetch and is
unquotable.

**This is the reverse of `test-summary-report`'s position.** That bundle's governing standard was paywalled and
its section design had to rest on a syllabus. Here the most structurally detailed source is openly licensed,
so the bundle can adapt PM²'s field definitions with attribution, and the paywalled standards are needed only
for existence and authority, which the Lexicon and the glossaries already supply.

#### The definition is where the sources disagree, and the template must make a team choose

The sources agree on the risk boundary, and on almost nothing else about what an issue *is*:

- **Anything that has happened and needs someone to act.** PM²: "An issue is any unplanned event related to the
  project that has already happened and requires the intervention of the Project Manager (PM) or higher
  management". PMI's Lexicon is broader still: "A current condition or situation that may have an impact on one
  or more objectives."
- **Only what breaches a tolerance.** APM's glossary: "A problem that is now breaching, or is about to breach,
  delegated tolerances for work on a project or programme." Anything inside tolerance is the day's work, not
  a logged issue.
- **Anything that could affect the project, forward-looking.** PRINCE2 7 (2023), as PeopleCert describes it:
  "anything that could affect the project". This is a change from PRINCE2's 2009 glossary ("A relevant event
  that has happened, was not planned, and requires management action"), and it pulls the concept toward the
  risk register's territory.

**The consequence for the design:** three incompatible definitions mean two people keeping the same log can
disagree about whether a row belongs in it at all. So the template's first section carries the team's own
threshold, stated, with the three positions offered as the choices they are. **That framing is this
library's**, derived from the disagreement above; no source prescribes it.

#### The change-request fork, which also bears on build-candidate 5

PRINCE2 puts a **request for change inside the issue concept**. As PeopleCert puts it: "Not all issues
result in changes" and "all changes start as issues"; the Northern Ireland template instructs that "Issues,
including those raised as changes under the project change control mechanism, should be recorded on the issue
log." PMI's PMBOK Guide instead **names two separate project documents**, each defined on its own ("The
change log is used to record all submitted change requests."), and states no rule for where they overlap: it
answers a different question from PRINCE2's rather than the opposite one. PM² keeps a separate Change Log
linked from the issue by a Traceability field.

**Proposed resolution:** the issue log records where a change request **came from** and hands it to change
control, with a cross-reference, and the companion names PRINCE2's alternative plainly. That is compatible with
both lineages and leaves the boundary with a future `change-request` bundle (GitHub issue #179) to that
bundle's own research rather than deciding it here. **If the research finds the PRINCE2 lineage dominant in
practice**, the type field carries request-for-change as a value and the companion says so.

#### Section design

Provisional, mirroring the `risk-register` shape its readers already know, and expected to move:

| Section | In lean | What it carries |
|---|---|---|
| **Purpose and Threshold** | yes | What counts as an issue here, stated as one of the three positions above, and what does not go in: risks (the register), defects (the bug tracker), approved changes (change control) |
| **Priority Scale** | yes | What each priority or impact level means, in words a second person would apply the same way. PM²'s 1-to-5 urgency and impact scales and Connecticut's Material/Non-Material split are the two published shapes |
| **Issues** | yes | **The load-bearing section.** One row per issue: ID, title and description, type, raised by and date, priority, **one named owner**, next action and target date, status. A table section, so it carries PRIORITY and ROW HINT |
| **Escalation** | yes | Who handles which priority, and the condition that moves an issue up. **In lean, unlike the risk register**, because every readable source carries escalation and APM defines an issue by a tolerance breach. Published shapes differ (a Yes/No field in PM², a status value in Connecticut, a change of decision-maker in Washington's template, a tolerance in APM's definition), and the guidance offers them rather than picking one |
| **Review and Ownership** | yes | Who keeps the log, how often it is reviewed, and when it is retired. Sankararajan and Shrivastava in PMI's *PM Network* (2012): "Issues recorded in the issues register should be discussed almost every day" |
| **Closed Issues** | full only | What each issue's resolution was, **who confirmed it**, and when. PM² defines Resolved and Closed as separate states ("Closed: This status indicates that all work is completed and verified"); Connecticut's template has Resolved and a closing date but no separate Closed state. The mirror of `risk-register`'s "Closed and Materialized Risks" |
| **Links to Other Logs** | full only | Each issue's origin and hand-offs: the risk that materialized into it, the change request it raised, the decision that closed it. PM²'s Traceability field is the published model |

**Two claims the build must not source to anyone.** The boundary with a bug tracker appears in no source
read, so it is labelled as this library's judgment. And four failure modes a brief might expect ("dumping
ground", "duplicates the ticket tracker", "used to assign blame", "never closed") were **not found in any
verified quotation**. The two that were found are an issue with no owner (ProjectManager.com: "If the issue
doesn't have an owner, it's likely never to get resolved.") and a log nobody reviews (prince2.wiki: "This
task often gets neglected when project managers get busy"). The rest are labelled or cut, never given a
citation found afterwards to justify them.

#### What makes it not a sibling

The companion's Relationships section places it against all three siblings, per the contract:

- **Not the risk register**, and the library has already said why: `risk-register_companion.md` section 8
  quotes "risk registers track conditions that might happen; issue logs address conditions that have happened".
  The new companion must agree with that section, not restate it differently. PRINCE2 7's forward-looking
  definition is the one real challenge to it, and the companion names it.
- **Not the RAID log.** An issue log stands to RAID's **I** as the risk register stands to its **R**: the
  deepened, standalone form of one quadrant. `raid-log_guide.md` already draws that system. The one
  practitioner source read on RAID (Asana) defines its issues the same way a standalone log does, so the
  choice is organizational, not definitional, and the companion says so.
- **Not the KPI dashboard.** The dashboard tracks performance against targets; an issue that the dashboard
  surfaces lands here, and the two do not share rows.
- **Not an impediment backlog.** The 2020 Scrum Guide prescribes neither: it names impediments only as
  something removed or surfaced ("Causing the removal of impediments to the Scrum Team's progress"), never as a
  written artifact. An agile team may need no issue log, and the guide's When NOT to use says so.

#### Metadata

| Field | Value | Why |
|---|---|---|
| `family` | `governance-docs` | ADR 0057 |
| `classification` | `utility` | The only value the contract allows, and correct: maintained, not executed |
| `sizes_available` | `[lean, full]` **provisional** | The catalog says `S`, but PM² separates the rules for handling issues (its Issue Management Plan, Appendix B.4) from the log itself (B.9), and a full weight carrying closure evidence and traceability is the same split both siblings make. If the research shows the rules do not earn a second weight, `[lean]` is allowed by the contract |
| `status` | `beta` | Every bundle |
| `methodology` | `generic` | All three siblings declare it, and the type is defined by PMI, PRINCE2, APM and PM² alike. The catalog's `PMBOK` would misdescribe it |
| `pairs_with` | `[]` | No pm-skills skill produces or consumes an issue log (checked against pm-skills `origin/main` on 2026-09-23); the contract says members adopt `[]` until one does |
| `related_templates` | `[raid-log, risk-register, status-report]` **provisional** | The two instruments it deepens and completes, and the report that already cites `ISS-11` |
| `aliases` | `issue register` kept; **`issue tracker` dropped, recommended** | "Issue tracker" is what a reader looking for Jira-style defect tooling types. Matching them to a project register is the collision the bug-tracker boundary exists to prevent. A build decision, argued in the research log |

#### What landing this bundle closes elsewhere

1. **The `governance-docs` contract `0.2.0`**, which lands with ADR 0057 in the same change as this spec, and
   its Members line, which records whether the member is specced and built.
2. **One sibling owes a Relationships line, and this is not optional.** Contract `0.2.0` obliges every
   member to state its position against the other members. `risk-register_companion.md` section 8 and
   `raid-log_companion.md` section 8 ("RAID log vs a standalone issue / assumption / dependency log")
   already do; **`kpi-dashboard_companion.md` never mentions an issue log** and calls the family "the three",
   so it gains its position in the same change as the bundle. *(Corrected 2026-09-23: this item said
   `raid-log`'s companion never mentions an issue log. It does, under a heading a phrase search missed.)* Whether the promise references in
   `risk-register` and `raid-log` link to the bundle, and whether `related_templates` gains it, is a build
   decision; no sibling's position changes.
3. **This page's Progress table**, and GitHub issue #176.

#### The example

**The Reporting Platform Modernization program's issue log**, which the family's shared-scenario rule makes a
hard constraint rather than a preference. `ISS-11` (the query-engine lead's departure, raised 2026-06-14,
target 2026-07-31, owner Marta Reyes, escalated to the steering group for a GBP 45,000 backfill contractor)
and `ISS-12` (staging view-list load at 620ms against a 500ms budget, raised 2026-07-10, target 2026-07-24,
owner Dana Osei) already appear across five sibling examples between them (`raid-log`, `risk-register`,
`status-report`, `kpi-dashboard`, `project-milestone-retrospective`), and the example carries them **exactly
as recorded there**. Because the scenario keeps them in the RAID log's Issues quadrant, this is the **deepened
record behind that quadrant**, dated so it can cite the RAID log and the risk register. Any further issue it
adds must be one the RAID log's working summary could plausibly omit, or one closed before that date.

**This build exercises the chaining-lens fix** that shipped in `v0.12.0` untested: the lens now reads the
sibling examples its example cites, and five of them carry these two issues.

#### What the build costs

One whole build has run through the committed `build-bundle.js`: `launch-coordination-checklist`, **$14.22
at API list rates**, every agent on Sonnet
([report](../../bundle-builds/reports/launch-coordination-checklist_v0.1.0.md)). This build is the
**second measurement, not a confirmation of a rate**. Run `python tools/gen-bundle-build-report.py --ingest`
in Phase 6, on the machine that ran the build.

**Outcome, 2026-09-23.** **8,378,876 weighted token-equivalents, $16.76 at API list rates**, 18 agents, every
one resolved to Sonnet ([report](../../bundle-builds/reports/issue-log_v0.1.0.md)). Like for like, the 15
research, drafting and review agents cost **$14.29 against `launch-coordination-checklist`'s $14.22**; the
other three were this landing's count sweep ($2.47), which the previous build did in the orchestrator, where
no report counts it. Two builds now agree within a dollar, which is two points, not a rate. Not counted in
either figure: the admission sweep run while the spec was written (16 agents, covering this type and
`definition-of-ready` together) and the orchestrator's own spend.
*(Note 2026-09-29: the linked report now reads 7,143,159 weighted, $14.29 and 15 agents. The maintainer ruled
that a report counts only the build agents, so the $2.47 sweep moved to the report's own landing-sweep line.
The figures above were the report's when this was written.)*

---

### standing-standards (fourth member): the definition of ready, a type this library has argued against

**`definition-of-ready`** - `standing-standards`, **`classification: foundation`**, sizes **`[lean]`**
(single-size, provisional), methodology **`agile-scrum`**, catalog id `definition-of-ready` (catalog 40),
alias `DoR`. Catalog owner: Scrum Team. Purpose: "Criteria a backlog item must meet to enter a sprint."
`category: Requirements`, `formality: lightweight`, `rarity: occasional`, `size_variant: S`,
`tier_inferred: true`, `relationships: [Sprint Backlog]`.

#### Demand, and the library's own position against the easy version

The `standing-standards` contract names this type first among its likely future members, and twelve files
across two bundles mention it (`definition-of-done` and `product-backlog`, counted case-insensitively on
2026-09-23; GitHub issue #178's "8 files" counted exact-case matches). **Almost every mention draws a
boundary rather than making a promise**, and three of them argue against the document:

- `definition-of-done_guide.md`: "unlike the DoD, whether a DoR should exist at all is a real, named
  disagreement in the field".
- `product-backlog_guide.md` names "The rigid Definition of Ready" as an anti-pattern, and both
  `product-backlog` templates carry the same TRAP.
- `definition-of-done_example.md`: "**Not a Definition of Ready.** The squad does not currently keep one."

**So this is a bundle for a type its own siblings warn about**, which is the `spike-report` shape: that
bundle's canon argued against writing one, and it shipped teaching the dispute. It is built on the
maintainer's direction of 2026-09-23 under
[ADR 0041](decisions/0041-maintainer-preference-sets-the-build-order.md) (GitHub issue #178,
build-candidate 4). **The family and classification are settled by
[ADR 0058](decisions/0058-definition-of-ready-joins-standing-standards-as-a-foundation.md).** The instruction of
2026-09-23 read "delivery ready"; the maintainer confirmed the same day that it meant `definition-of-ready`.

#### Admission: met at the practitioner and pattern tier, and declined by both standards that could have met it

Every quotation below was checked against the source's raw text on 2026-09-23.

| Source | What it says | Licence |
|---|---|---|
| Richard Kronfält, "Ready-ready: the Definition of Ready for User Stories going into sprint planning", *Scrum FTW* blog, 1 October 2008 | "So, the definition of Ready should be;" followed by a list. The earliest verified instance | none stated |
| The Scrum Patterns Group, "Definition of Ready" pattern, scrumbook.org (also in *A Scrum Book*, Pragmatic Bookshelf, 2019) | "Richard Kronfält apparently published the first formal description of Definition of Ready in 2008" | all rights reserved |
| Microsoft, *Code-With Engineering Playbook*, "Definition of Ready" | "Definition of Ready is the agreement made by the scrum team around how complete a user story should be in order to be selected as candidate for estimation in the sprint planning" | **CC BY 4.0** (the repository's licence file) |
| Agile Alliance, glossary | a DoR "provides the team with an explicit agreement allowing it to "push back" on accepting ill-defined features" | all rights reserved |
| Scrum Alliance, "Definition of Ready vs. Definition of Done" | "While the definition of done (DoD) is part of scrum, a definition of ready (DoR) is an external and optional tool" | not stated |

**Two sources that could have admitted it decline to.** The 2020 Scrum Guide never uses the phrase
"Definition of Ready"; its nearest sentence is "Product Backlog items that can be Done by the Scrum Team
within one Sprint are deemed ready for selection in a Sprint Planning event." And the Scaled Agile Framework's
glossary defines the Definition of Done and has no entry for a Definition of Ready. Two authors writing
on Scrum.org treat the silence as meaningful rather than an oversight: Barry Overeem (2016),
"So why isn't the Definition of Ready described in the Scrum Guide? Because it is. However not as a checklist
but as an activity: backlog refinement."; Joanna Płaskonka (2023), "Is Definition of Ready obligatory in
Scrum?" and "The answer is short: no". Both are individually authored posts, not Scrum.org policy, and are
cited that way. Both pages refuse plain HTTP clients and were read through a rendering browser.

**ADR 0030's test is met several times over** on
[ADR 0048](decisions/0048-one-named-source-clears-the-admission-test.md)'s one-source reading. One research
dimension returned "weak" by quietly substituting a stricter bar, a published fillable template, for the
rule's actual wording; its completeness critic caught the substitution, and it is recorded here so the
research log does not repeat it. **What the tier does oblige is honesty about the tier.** This family's
named citation hazard is "folklore presented as standard", and "a Definition of Ready is part of Scrum" is
that folklore exactly. The companion says in plain words that neither Scrum's nor SAFe's own text names it.

**One correction the retrieval made, recorded because the brief was wrong.** The "ready-ready" coinage is in
Jakobsen and Sutherland, "Scrum and CMMI - Going from Good to Great: Are you ready-ready to be done-done?":
"Systematic introduced the term ready-ready, to express that work from the Product Backlog has been
sufficiently elaborated to be allocated to a sprint for implementation." It is **not** in the earlier
Sutherland, Jakobsen and Johnson paper "Scrum and CMMI Level 5: The Magic Potion for Code Warriors", where
the string does not occur. The later paper's venue and year (Agile 2009) come from its filename and
bibliographies, not its text, and are cited that way.

#### The dispute, which the bundle carries rather than settles

Three positions, each sourced from raw text:

- **Against a rigid one.** Mountain Goat Software, Mike Cohn's company: "If these rules include saying that
  something must be 100 percent finished before a story can be brought into an iteration, the definition of
  ready becomes a huge step towards a sequential, stage-gate approach." Its remedy is not abolition: "Favor
  guidelines rather than rules on your Definition of Ready."
- **Against having one.** Allan Kelly (2017): a DoR "reduces agility because it breaks up process flow,
  assumes greater role specific responsibilities, introduces more wait states (delay) and potentially
  undermines business-value based prioritisation". His alternative for an item that is top priority and not
  ready: "then the first task is to make it ready". Stefan Roock, quoted by InfoQ (2014): "the Definition of
  Ready should be shrinking over time and not growing". Overeem, on Scrum.org: "Instead of using the
  Definition of Ready as a sequential, phase-gate checklist I prefer the activity of Backlog Refinement."
- **For one, kept small and shared.** Roman Pichler: "the definition of ready (DOR) is jointly owned by the
  product owner and the team", and "I recommend starting with a good-enough DOR and adapting it in the sprint
  retrospectives if and when necessary". Big Agile (2025) names the middle position outright: "a clarity
  compass, not a compliance document".

**The bundle's position is the library's usual one for a contested type: it teaches the dispute and does
not recommend a side** (the `definition-of-done` companion's section 6.1 takes the same stance). Concretely,
the template teaches a DoR **written as guidelines**, the stage-gate failure is the TRAP of its load-bearing
section, and the guide's When NOT to use is unusually prominent: the `definition-of-done` example's squad
keeps no DoR, and that is presented as a legitimate end state, not a gap.

#### The design question: `foundation` or `tool`, and the twist in the failure mode

The contract's cut is "a standard you judge against" (`foundation`) against "an instrument you execute,
usually under time pressure and often by someone who did not write it" (`tool`). **A DoR is the first.** It is
agreed by the team that applies it, consulted at refinement and sprint planning to judge whether an item is
ready, and changed deliberately and rarely. Nobody executes it under time pressure. It is the entry-side
mirror of `definition-of-done`, which is `foundation`. ADR 0058 records the counter-argument (it operates as a
checklist at a moment, which sounds like a `tool`) and why it does not carry.

**The twist, and the sharpest teaching point the family gains.** The contract names `foundation`'s failure
mode: "being agreed once and never honoured". **A DoR's documented failure is the opposite: being honoured
too hard**, enforced as a gate on items the team would rightly have taken. So the Review Trigger that section
4 of the contract mandates must fire **in both directions**: when an item the DoR blocked turns out to have
been ready enough, and when an item it let through stalls on something it should have caught. Microsoft's
playbook supplies the second direction in its own words ("Update or change the definition of ready anytime
the scrum team observes that there are missing information in the user stories that recurrently impacts the
planning"); **the first direction is this library's own contribution**, derived from the dispute above, and is
labelled that way. *(Corrected 2026-09-23 by the build's research: Big Agile states the first direction too,
"When the DoR blocks more value than it enables, it stops being a safety rail and becomes a parking brake", so
the bundle sources it rather than labelling it its own.)*

#### Sizes: single-size, because the research argues against a second weight

The contract allows `[lean]` "where the type's own research shows it does not earn a second weight", and this
is the first member where the research argues it directly. Every source that is not flatly against a DoR
wants it shorter, not longer: Roock's "The smaller the better", Pichler's "good-enough DOR", Cohn's
guidelines over rules. A `full` variant that added criteria would model the documented failure. The catalog
agrees (`size_variant: S`).

**The one thing a second weight could honestly carry** is readiness above the story: Applied Frameworks'
"A Definition of Ready for PI Planning" (2022) is a published feature-level DoR, and it is a consultancy's
extension, not a SAFe artifact. **If the build's research finds published DoRs that genuinely operate at two
levels in one document**, a full variant carrying "Readiness by Level" is the natural shape, mirroring
`definition-of-done`'s "Criteria by Level". Otherwise the companion describes feature-level readiness and the
template does not carry it.

#### Section design

Provisional, derived from the sources' shapes and the contract, and expected to move:

| Section | What it carries |
|---|---|
| **Why We Keep One** | The specific problem this team's DoR exists to fix, and the condition under which the team would drop it. A DoR that cannot say why it exists has no answer to Kelly. **This section is the library's own contribution**, the dispute carried into the template itself |
| **Scope and Ownership** | Which work items it applies to, at which moment (Microsoft ties the checklist to refinement; the Scrum Guide's "ready for selection" is sprint planning), and who owns it: jointly the product owner and the team, per Pichler and Atlassian ("created for the team, by the team") |
| **Readiness Criteria** | **The load-bearing section.** Each criterion as a guideline: the question it asks, the evidence that answers it, and whether a miss stops the item or starts a conversation. A table section, so it carries PRIORITY and ROW HINT. The TRAP is Cohn's: any criterion phrased as "100 percent" before entry |
| **When an Item Is Not Ready** | What happens to a top-priority item that misses: Kelly's "the first task is to make it ready", or an explicit exception. The pressure valve that keeps a DoR from becoming a gate, and the mirror of `definition-of-done`'s "When Work Does Not Meet It" |
| **Review Trigger** | **Contract-mandated** (section 4), and bidirectional, as argued above |

**Two structural sources, and neither may be restyled.** INVEST (Bill Wake, 2003) is the usual content of the
criteria, and Wake's article never uses the term "Definition of Ready", so it is cited as INVEST's origin
only. Pichler's "clear, feasible and testable" is a competing three-criterion shape. The template offers the
question each criterion asks, not either list; Microsoft's CC BY 4.0 playbook is the only source whose wording
may be adapted.

#### What makes it not a sibling

- **Not the `definition-of-done`.** Entry against exit. Scrum Alliance: "The definition of done refers to the
  PBI itself, while the definition of ready often refers to externalities". Kelly collapses the two in a flow
  system ("The definition of done at the end of one activity is the definition of ready for the next"), and
  the companion reports that as a real position.
- **Not acceptance criteria.** Scrum Alliance: "The definition of done applies to all work in the backlog.
  Contrast this with acceptance criteria, which are unique to each PBI". A DoR applies across items and may
  require that acceptance criteria exist; it never states them.
- **Not backlog refinement.** The Scrum Guide: "Product Backlog refinement is the act of breaking down and
  further defining Product Backlog items into smaller more precise items." Refinement is the activity; the DoR
  is what it aims at.
- **Not a stage gate.** Cooper's Stage-Gate model decides "Go, Kill, Hold, or Recycle"; a DoR with those
  outcomes has become one.
- **Not ISTQB entry criteria**, which serve the same function from a testing lineage: "The set of generic and
  specific conditions for permitting a process to go forward with a defined task". *(Corrected 2026-09-23: this
  said no source bridges the two vocabularies. The unofficial ISTQB glossary mirror lists "definition of ready"
  among the synonyms of entry criteria; the companion reports that, and that the mirror is not ISTQB's own
  site.)*

#### Metadata

| Field | Value | Why |
|---|---|---|
| `family` | `standing-standards` | ADR 0058; the contract's own forecast |
| `classification` | `foundation` | ADR 0058: a standard items are judged against, the mirror of `definition-of-done` |
| `sizes_available` | `[lean]` **provisional** | Argued above. The contract permits it on research grounds |
| `status` | `beta` | Every bundle |
| `methodology` | `agile-scrum` | `definition-of-done`'s value. The catalog says `Scrum/Kanban`, but the sharpest critics write from flow and Kanban practice, so claiming Kanban lineage would misdescribe the type |
| `pairs_with` | `[]` | The only candidate is pm-skills `iterate-refinement-notes`, whose description mentions stories moving to "ready-for-sprint" but which never mentions a definition of ready (checked on pm-skills `origin/main`, 2026-09-23). Pairing would claim something the skill does not say |
| `related_templates` | `[definition-of-done, product-backlog, acceptance-criteria, sprint-backlog]` **provisional** | The exit-side sibling, the backlog it gates, the per-item criteria it may require, and the sprint it admits items to |

#### What landing this bundle closes elsewhere

1. **The `standing-standards` contract's Members line and forecast**, which move with ADR 0058 in the same
   change as this spec. The forecast entry moves to Members rather than being deleted, as the contract's own
   change note did for the launch checklist.
2. **`definition-of-done` and `product-backlog` may link to the bundle**, a build decision. Neither changes its
   position: both keep reporting the dispute, and the DoR bundle agrees with them.
3. **This page's Progress table**, and GitHub issue #178.

#### The example

**The Reporting Squad's first Definition of Ready**, chained onto a sentence the family already wrote:
`definition-of-done_example.md` says that "if the squad adopts a Definition of Ready later, it will gate entry
into the sprint, not exit from it, and will not replace anything above." The example makes that sentence true
rather than contradicting it, so it is dated after that example's last update (2026-07-24), and whatever
prompted the squad to adopt one must agree with the Saved Views items' recorded states in the `product-backlog`
and `sprint-backlog` examples. **It must be short**, because a long example would teach the anti-pattern the
bundle warns against, and it must not reproduce Microsoft's, Atlassian's or the ScrumPLoP pattern's lists.

#### What the build costs

The third build through the committed `build-bundle.js`, after `launch-coordination-checklist` ($14.22) and
`issue-log` ($14.29 for the same 15 build agents). A single-size bundle writes one template instead of two, so
drafting should be smaller; the report will say whether it was. **The committed workflow's templates stage
writes both variants**, so a single-size build needs that stage told to write lean only, as `spike-report`'s
per-bundle script did.

**Outcome, 2026-09-23.** The workflow gained a `sizes` input before this build rather than being told per
run, and the build ran through it. **6,947,001 weighted token-equivalents, $13.89 at API list rates**, 18
agents, every one resolved to Sonnet ([report](../../bundle-builds/reports/definition-of-ready_v0.1.0.md)).
Like for like, the 15 research, drafting and review agents cost **$11.69, against $14.29 for `issue-log` and
$14.22 for `launch-coordination-checklist`**; the other three were the landing's count sweep ($2.20). The
prediction held, and by a margin: the drafting stage cost $4.71 against $5.63 and $7.15, and its templates
agent $1.24 against $1.58 and $2.62, one variant instead of two. Three builds is still three points, not a
rate. Not counted: the admission retrieval run while the spec was written, and the orchestrator's own
spend. *(Note 2026-09-29: the linked report now reads 5,846,070 weighted, $11.69 and 15 agents. The maintainer
ruled that a report counts only the build agents, so the $2.20 sweep moved to the report's own landing-sweep
line. The figures above were the report's when this was written.)*

---

### delivery-docs (new member): the internal announcement the release-notes guide routes to

**`announcement-internal-comms`** - `delivery-docs`, **`phase: deliver`**, sizes **`[lean]`** (provisional),
methodology **`methodology-agnostic`**, catalog id `announcement-internal-comms`, catalog name "Announcement /
Internal Comms", aliases `internal memo`, `launch announcement`, `Slack canvas`. Catalog owner: PM / PMM.
Purpose: "Announce changes or launches to internal/external audiences". `size_variant: S`, `rarity: common`,
`tier_inferred: true`, `relationships: [Release Notes]`.

**Scope, narrowed from the catalog's:** the **internal** announcement of a **product launch or change**,
written for people in the organization who did not do the work (support, sales, other teams, leadership). The
record of what changed, for customers or for anyone else, is `release-notes`' job, so the catalog's
"internal/external" narrows to internal, and the entry is corrected when the bundle lands.

#### Demand: one routing row, and a family forecast that lost to research

- `release-notes_guide.md`, When NOT to use: "You need a full launch plan and comms. Use a launch checklist and
  announcement; release notes are one input." The launch checklist shipped in `v0.12.0`; this is the other half
  of that sentence.
- The `communication-docs` contract named "a release announcement distinct from `release-notes`" as a likely
  member. **It does not join that family**; see the next section and
  [ADR 0059](decisions/0059-announcement-internal-comms-joins-delivery-docs.md).
- Built on the maintainer's direction of 2026-09-24 under
  [ADR 0041](decisions/0041-maintainer-preference-sets-the-build-order.md) (GitHub issue #177,
  build-candidate 3).

#### The family: `delivery-docs`, by ADR 0059

Tested on 2026-09-25 against the membership section and axis rule of all nine contracts. Two admit it:
`communication-docs`, whose membership test fits ("exists to tell people who are not doing the work what is
happening with it") but whose only axis value, `utility`, ADR 0034 justified as "maintained, periodic"; and
`delivery-docs`, whose test admits it as written ("announces a unit of product work") at a phase that describes
it honestly. **The maintainer chose `delivery-docs` on 2026-09-25.** The contract moves to `0.2.0` with the
change-request amendment below, and the chain sentence gains the internal announcement beside the release note.

#### Admission: three qualifying sources, and all of them vendor or practitioner tier

Every quotation below was checked against the source's raw text on 2026-09-25, not against a retrieval
tool's summary of it. **No standards body, government or professional institute publishes this document.**
The UK Government Communication Service's functional standard names announcements only as an activity
("Communication, in the context of this functional standard, includes announcements, media management,
coordinated communication activities"); Prosci, CIPR and the Institute of Internal Communication publish
communication *plans* and *strategies*, never the announcement itself. The `communication-docs` contract
predicted this about the whole category ("its literature is thin and vendor-dominated"), and the bundle must
say so rather than dress vendor content as practice.

| Source | What it publishes | Licence |
|---|---|---|
| Staffbase, "Organizational Announcements" (Robert Grover, 2025, updated 2026) | Defines the type by name ("An organizational announcement is an internal communication that shares important updates with employees across a company") and ships seven worked templates, one a new product launch: "These templates are a starting point, not a one-size-fits-all solution" | All rights reserved |
| GitLab Handbook, "How to make a company wide announcement" | Prescribed content, not a file: "Keep it simple, brief and summarize what is important. Cover the 5 W's", and "The majority of information should still be in the Handbook which you include links to" | All rights reserved (the handbook's own footer; GitLab's product docs are CC BY-SA, the handbook is not) |
| Jason Fried (37signals), "Deployments: How we announce new features and updates internally at Basecamp" | A named internal format for a shipped feature: a post that "explains what's new" and "points out what could be an issue", and is "wonderful for those on the front lines too" | Not stated |

**Any one of the three clears [ADR 0048](decisions/0048-one-named-source-clears-the-admission-test.md)'s bar.**
All three are all-rights-reserved or unstated, so **they are structure evidence and short quotation only; no
wording may be adapted.** Atlassian's Team Playbook play "Change Management Communication With Video" supplies
three content prompts ("What's changing?", "Why is this change important?", "How will this change impact
them?") but its deliverable is a video, so it corroborates structure and is not counted.

**Two things the research deliberately did not count.** US Army AR 25-50 publishes the memorandum, which the
catalog lists as an alias ("internal memo"), but counting it would be the library certifying itself through
its own alias. And **AR 25-50 is not a source for "bottom line up front"**: the current edition (2020, revised
2024) contains neither the phrase nor the acronym; only the superseded 2013 edition did. The principle is
sourced instead to Nielsen Norman Group ("Start content with the most important piece of information so
readers can get the main point, regardless of how much they read") and the MLA, for which a writer buries
the lede "when the newsworthy part of a story fails to appear at the beginning, where it's expected".

#### Scope: after the decision, for the people who did not make it

The sharpest boundary in the research is time. Amazon's PR/FAQ borrows the announcement's form for the
opposite purpose, before anything is built: Bryar and Carr write that "Normally, writing a press release is the
last step in launching a new product", and the PR/FAQ inverts that as a forcing function. This library ships
that device as `product-vision`'s `prfaq` format. **The internal announcement fires after the decision and
alongside the launch**, to people who must act on it.

The internal-versus-external question has **no consensus**, and the companion reports three positions rather
than picking one: one document with internal and external parts (the PR/FAQ's External and Internal FAQs);
separate documents with no stated order (GitLab's handbook keeps internal and external communication in
separate sections); and separate documents, internal first (Tomorrow People: "you should leave enough time
between your internal and external launch so you can set realistic milestones for each department"). The last
rests on one marketing agency's post, and the companion says so.

#### Section design

Provisional, one size. **The evidence argues against a second weight.** Staffbase's seven templates share one
shape (a subject line, a salutation and three or four sentences), and its two highest-stakes examples differ
from the rest by one sentence, not a section. Leadership quotes and FAQ links appear on that page only as
optional best practice ("Involve leadership", "Link to FAQs or additional resources"), never inside a template.
A full variant built from them would be the library's invention, so none is proposed.

| Section | What it carries |
|---|---|
| **Headline** | One line a reader can act on without opening the rest. Every Staffbase template opens with a subject line; the inverted-pyramid rule is NN/g's. The TRAP is the buried lede (MLA; Tomorrow People: "avoid burying the most relevant information with the generic bits") |
| **What Is Changing, and When** | The launch or change, who it applies to, and the date. GitLab's 5 W's; Atlassian's "What's changing?" |
| **Why It Matters** | The reason, in the reader's terms. Atlassian's "Why is this change important?"; the TRAP is jargon (Staffbase: "Use plain language and avoid corporate jargon"; Tomorrow People: "product marketing teams use a lot of jargon") |
| **What It Means for You** | What changes for this audience, and what, if anything, they must do and by when. Atlassian's "How will this change impact them?"; Staffbase's "what they need to do (if anything)"; Basecamp's front-line purpose |
| **Known Issues** | What could go wrong or is not done yet, so support hears it here first. Fried: a Deployment post "points out what could be an issue". Where it overlaps `release-notes`' Known Issues, **it links there rather than restating** |
| **Where to Learn More** | The source of truth and a named contact. GitLab: the detail belongs in the linked source, not in the announcement; Staffbase's "named contact" |

**Frontmatter, not sections:** the audience, the channel and the send date. They are the author's decisions,
not the reader's content. GitLab gates its company-wide channel by reach ("Is this relevant to all team
members globally?") and asks for notice "ideally 72 hours (at minimum 24 hours) in advance of a due date";
**that window is GitLab's own house rule** and the guidance labels it so rather than stating it as a norm.

**The design rule this bundle owes most to its sources: link, do not restate.** GitLab's instruction to keep
the information in the linked source is also what keeps an announcement from contradicting the release notes
or the PRD it summarizes. Every fact in it should be traceable to an upstream artifact, and the guide's rubric
checks for one that is not.

#### Failure modes: which are sourced, and which the build must label or cut

| Failure | Status |
|---|---|
| Burying the point | **Sourced**: NN/g, MLA, Tomorrow People |
| Jargon | **Sourced**: Staffbase, Tomorrow People |
| Posting it where it gets lost | **Sourced**: GitLab, "we recommend that you do not use #whats-happening-at-gitlab as a sole location for important announcements as information might get lost or muted" |
| Broadcasting instead of starting a conversation | **Sourced**: Staffbase, "internal announcements feel more like broadcasts than conversations"; Prosci's "telling plan rather than a communications plan" |
| Contradicting the release notes | **Not found in any verified source.** The library's own, and labelled so |
| No call to action | **Only the fix is sourced** (Staffbase, GitLab's "call to action"); the failure's name is the library's |
| "Announcement fatigue" | **Not found as a term.** The adjacent, sourced concept is notification fatigue (tchop: "Notification fatigue is the exhaustion and desensitisation people feel when they receive too many alerts"), and GitLab's "Be mindful of the attention economy" |

#### What makes it not a sibling

- **Not `release-notes`.** A release note is a constrained record of what changed; GitLab's own release-note
  process caps an entry at "125 words or fewer, and no images or videos", and LaunchNotes calls it a "Curated
  user-impact summary for a release, written so customers and GTM teams know what changed and why it
  matters". The announcement tells the people who did not do the work what the change means for them and what
  they must do, and links to the notes. **The line is purpose, not audience**, and it is this library's, drawn
  in the contract: `release-notes_companion.md` already recommends "the full notes internally and the lean
  notes externally", so an internal reader is not what distinguishes the two.
- **Not `launch-coordination-checklist`.** The checklist's Launch Communications section confirms that the
  right people have been told; the announcement is one of the things it confirms. Its example already names
  the communications owner (Priya Nair) for the Saved Views Sharing launch.
- **Not `status-report`.** A status report is periodic and backward-looking; the announcement is written once,
  for one event.
- **Not `product-vision`'s PR/FAQ.** Before the decision, not after it (above).
- **Not a communication plan.** Prosci's deliverable is a plan for repeated, multi-sender messages; the
  announcement is one message within such a plan, if there is one.

#### Metadata

| Field | Value | Why |
|---|---|---|
| `family` | `delivery-docs` | ADR 0059 |
| `phase` | `deliver` | The only value the contract allows, and honest: it announces a launch or change of a unit of product work |
| `sizes_available` | `[lean]` **provisional** | Argued above; the catalog agrees (`size_variant: S`), and the contract permits it |
| `status` | `beta` | Every bundle |
| `methodology` | `methodology-agnostic` | `release-notes`' value; nothing in the sources ties the type to a method |
| `pairs_with` | `[]` | No pm-skills skill produces an internal launch announcement. The nearest, `foundation-stakeholder-update`, translates one meeting's outcomes for people who were not there (checked on pm-skills `origin/main`, 2026-09-25, with the direct contents call) |
| `related_templates` | `[release-notes, launch-coordination-checklist, prd]` **provisional** | The record it links to, the checklist that confirms it was sent, and the source of its facts |
| `aliases` | `internal memo`, `launch announcement` kept; **`Slack canvas` dropped, recommended**; **never `release announcement`** | `release-notes` already carries `release announcement`. A Slack canvas is a surface, not a document type. A build decision, argued in the research log |

#### What landing this bundle closes elsewhere

1. **The `delivery-docs` contract `0.2.0`** and the dated correction in `communication-docs` section 1, both of
   which land with ADR 0059 in the same change as this spec.
2. **`release-notes`' Relationships section owes a line.** The contract obliges every member to state its
   position in the chain, and `release-notes_companion.md` has never had an internal announcement to place.
   `release-notes_guide.md`'s routing row may link to the bundle, a build decision.
3. **The catalog entry**, per [procedure 1](decision-procedures.md#1-a-catalog-call-loses-to-research): its
   purpose ("internal/external audiences") narrows to internal, and the `Slack canvas` alias goes if the build
   drops it. `docs/internal/catalog.md` and `atlas/catalog-data.json` both, then regenerate the atlas.
4. **This page's Progress table**, and GitHub issue #177.

#### The example

**The internal announcement of the Saved Views Sharing launch**, sent by its communications owner, Priya Nair.
`launch-coordination-checklist_example.md` names her in that role and says the public announcement is "Drafted
separately as a `release-notes` entry", with Support and Documentation briefed before go-live; this example is
the internal counterpart. **Every fact must be read from an existing example** (the checklist, the PRD, the
release notes, the test plan), and the link-do-not-restate rule means the example should show it doing that.

**A pre-existing contradiction the build must resolve first, not inherit.** `release-notes_example.md`
(Acme Analytics 2.4.0, 2026-06-30) lists sharing under New ("share a view with your team"), while the
launch checklist says Sharing launched later, with an exit review on 2026-07-17, "on top of the Tier 3
private-views work that shipped ahead of it", and the PRD phases sharing after a security review. **An
announcement that reads its facts from both would repeat the disagreement.** The build either corrects the
release-notes example (a history entry and a version bump on that bundle) or announces a launch whose facts
agree across every source it reads.

#### What the build costs

Single-size, like `definition-of-ready` ($13.89 at API list rates, $11.69 for its 15 build agents), so
drafting should cost about the same. Build through `build-bundle.js` with `sizes: ["lean"]`, every agent on
Sonnet.

**Outcome, 2026-09-25. The prediction did not hold.** **8,495,731 weighted token-equivalents, $16.99 at API
list rates**, 15 agents, every one resolved to Sonnet
([report](../../bundle-builds/reports/announcement-internal-comms_v0.1.0.md)). Drafting cost **$8.58**,
against $4.71 for `definition-of-ready` and $5.78 for `change-request` built the same evening with two
templates; almost all of the difference is cache reads (24.6M in drafting), as its example agent read widely
across the Saved Views thread to chain one launch onto four siblings. One template instead of two did not make
this build cheaper, so writing fewer variants is not by itself a predictor of cost. After the review, the
main loop found the template's GOOD examples reused the example's own scenario, which no lens flagged; they
were rewritten before landing.

---

### delivery-docs (new member, by amendment): the change request two bundles route to

**`change-request`** - `delivery-docs`, **`phase: deliver`**, sizes **`[lean, full]`** (provisional),
methodology **`generic`**, catalog id `change-request`, catalog name "Change Request", aliases `RFC (ITIL)`,
`change record`, `change ticket`. Catalog owner: Change Manager. Purpose: "Formally request and authorize a
production change". Category Release / Deployment / Runbooks, stage `release`, methodology ITIL, `formality:
formal-auditable`, `size_variant: S/M`, `relationships: [CAB review]`. **Almost every one of those catalog
calls describes the lineage this bundle does not serve**, and the entry is corrected when it lands.

#### Demand: two bundles route to it

- `bug-report_guide.md`: "**It is a request, not a defect.** If nothing promised the behavior you want, that is
  a change request." Its companion covers the boundary in section 6.
- `issue-log_template-full.md` links each issue "to a risk it materialized from, a change request it raised, or
  a decision that closed it", and its guide names a raised request for change as a reason to use the full
  weight.
- Built on the maintainer's direction of 2026-09-24 under
  [ADR 0041](decisions/0041-maintainer-preference-sets-the-build-order.md) (GitHub issue #179,
  build-candidate 5).

#### The family: `delivery-docs`, by amendment (ADR 0060)

**No contract admitted this type as written, and that is the finding that shaped everything else.** Tested on
2026-09-25 against all nine membership tests, a per-occasion change request fitted none; `governance-docs`,
the natural-looking home, excludes "An event-driven or phase-bound artifact". The maintainer chose to widen
`delivery-docs` with a fifth verb: the family's artifacts now define, decompose, verify, **change**, or announce
a unit of product work. The contract's section 1 states what the verb does not admit (a change to a running
production system; the standing change log). See
[ADR 0060](decisions/0060-change-request-joins-delivery-docs.md), which also records the three rejected
options.

#### Which change request: the project and product baseline

Two lineages share the name, and the readable sources support them about equally:

| Lineage | What changes | Readable sources |
|---|---|---|
| **Baseline** (served) | Something agreed about a unit of work: scope, requirements, schedule, cost | PMI's Lexicon; the PMBOK Guide 6th edition errata; PRINCE2 (via prince2.wiki); APM; the European Commission's PM² guide and Change Request Form; the CDC Unified Process form; GSA's M3 Playbook form |
| IT service (the neighbour) | A running system | NIST SP 800-128 Appendix E and SP 800-53 CM-3; the ITIL glossary; Prairie View A&M's form; IT Process Wiki's RFC checklist |

**The maintainer chose the baseline lineage on 2026-09-25**, because the library's routing already used it (a
bug-report reader asking for behavior nothing promised is asking to change what the PRD and acceptance criteria
agreed) and because its audience is product management and software delivery, not IT operations. The IT
service lineage stays a named neighbour: its vocabulary (standard, normal and emergency changes, a change
authority, a back-out plan) is described in the companion and does not appear in the template.

**The two lineages share a skeleton**, which is why one bundle can name both honestly: an identifier, a
requester, a description of the change, a reason, an impact assessment, and a decision by a named authority.
**They diverge on everything else**: the IT forms add configuration items, security impact and rollback; the
baseline forms add scope, schedule and cost impact against an agreed plan.

#### Admission: retrieved, and the widest named-source base on this page

Every quotation below was checked against the source's raw text on 2026-09-25. Three sources were reached only
through the Internet Archive, because their live pages now return 403 or 404, and **the research log must cite
the archived copy that was actually read**, not the dead URL.

| Source | What it says or publishes | Licence |
|---|---|---|
| PMI, *Lexicon of Project Management Terms* v5.0 (January 2026) | "A formal proposal to modify a document, deliverable, or baseline." | PMI, personal use only |
| PMI, *PMBOK Guide* 6th edition, errata (fifth printing) | "The change log is used to record all submitted change requests." The Guide itself is sold and was not read | PMI |
| European Commission, *PM² Project Management Methodology Guide* v3.1 (2023) | A change request asks to "amend an aspect of the agreed baseline of a project", and "can be formally submitted via a Change Request Form, or can be identified and raised during meetings as a result of decisions, issues or risks"; "There are four possible decisions: approve, reject, postpone or merge the change request" | **CC BY 4.0** |
| PM² Change Request Form template v3.0.1 (docx) | Four narrative sections, "Current Situation", "Desired Situation", "Impact or Risks" and "Out of Scope", and "Once the change request is logged into the Change Log, then this form is updated with the assigned Change ID and the form is archived" | **Not stated in the file**; the guide's CC BY 4.0 does not automatically cover it |
| CDC Unified Process, *Change Request Form (example)* (2009, archived copy) | Three sections by actor: "SUBMITTER - GENERAL INFORMATION", "PROJECT MANAGER - INITIAL ANALYSIS", "CHANGE CONTROL BOARD - DECISION" | Not stated; presumptively a US government work, unconfirmed |
| US GSA, *M3 Playbook Change Request Form Template* (docx, read from its XML) | "Requirements Change Request Information" and "Change Control Board Approval Information" | Not stated |
| APM glossary and "What is change control?" | A change request: "A request to obtain formal approval for changes to the approved baseline"; and "Change requests may arise as a result of issues" (the second is on the change-control page, not the glossary) | APM, not stated |
| PRINCE2, via prince2.wiki | A request for change: "It is a proposal for a change to a baselined product"; the change authority is "A person or group to whom the project board may delegate responsibility for reviewing and approving change requests or off-specifications" (the second is on the change-authority page) | AXELOS, all rights reserved |

**PM² is the adaptable source**, as it was for `issue-log`: its guide is CC BY 4.0, so its definitions and
process wording may be adapted with attribution. Its form's field layout is structure evidence only until a
licence covering the docx is found. HHS's EPLC Change Management Plan (2008, archived copy) is a useful
outlier rather than a third form: it gives one field list for "THE PROJECT'S CHANGE REQUEST FORM AND CHANGE
MANAGEMENT LOG" together, and the companion reports it as the case where the two are merged.

**What was not read.** The PMBOK Guide body, ISO 21502:2020 beyond its catalog page, AXELOS's own PRINCE2 and
ITIL manuals, and the ITIL 4 Change Enablement practice guide. ITIL's change types are sourced only to
PeopleCert-copyrighted Foundation training material redistributed by a training provider, and "normal change"
is absent from that glossary; since the template carries no ITIL vocabulary, none of this is load-bearing.

**Retrieval notes for the build's research**, because several of these sources cannot be read at the address
a search returns, and a research agent that tries the live URL will drop them:

| Source | Read from | How |
|---|---|---|
| CDC UP Change Request Form (example) | <http://web.archive.org/web/20240601190446/https://www2a.cdc.gov/cdcup/library/templates/CDC_UP_Change_Request_Form_Example.doc> | Live site returns 404. A 1997-format `.doc`: extract with `antiword`, not a text decode |
| HHS EPLC Change Management Plan | <http://web.archive.org/web/20260226151438/https://www.hhs.gov/sites/default/files/ocio/eplc/EPLC%20Archive%20Documents/07%20-%20Change%20Management%20Plan/eplc_change_management_plan_template.doc> | Live returns 403. `antiword` |
| CDC UP newsletter on change management (2009) | <http://web.archive.org/web/20250418071852/https://stacks.cdc.gov/view/cdc/77284/cdc_77284_DS1.pdf> | Live returns 403. Practice narrative only; **not** the form |
| PM² Change Request Form v3.0.1 | <https://www.pm2.center/wp-content/uploads/2022/02/21.I.PM2-Template.v3.Change_Request_Form.ProjectName.dd-mm-yyyy.vx_.x-1.docx> | The `pm2.eu` landing page carries no fields; read the docx's `word/document.xml` |
| PM² Methodology Guide v3.1 | <https://www.pm2alliance.eu/wp-content/uploads/2024/02/pm%C2%B2-project-management-methodology-NO0523520ENN.pdf> | `pdftotext` without `-layout` |
| GSA M3 Playbook Change Request Form | <https://ussm.gsa.gov/assets/files/M3-Playbook-Change-Request-Form-Template.docx> | Read `word/document.xml`; a text decode of the docx fails every quote |
| PRINCE2 change authority | <https://prince2.wiki/people/change-authority/> | The definition is here, not on `/practices/issues/` |
| APM, change requests arising from issues | <https://www.apm.org.uk/resources/what-is-project-management/what-is-change-control/> | Not on the glossary page |
| DORA 2019 report | <https://dora.dev/research/2019/dora-report/2019-dora-accelerate-state-of-devops-report.pdf> | The CAB finding and "there is still an important role for the CAB" |

The sweep's full returns and the main loop's re-check are kept, untracked, at
`_local/research/2026-09-25_admission-sweep-2/`.

#### The change-request fork, answered

`issue-log`'s spec left one question to this bundle's research: **if the PRINCE2 lineage (a request for change
is a kind of issue) proved dominant, the type field would carry it.** It is not dominant. PRINCE2 files a
request for change as one of "five types of issues"; PMI names a separate change log, and PM², the CDC form and
GSA's form all treat the request as its own document. **So the request records where it came from**: PM²'s own
list, "decisions, issues or risks", plus a meeting or a stakeholder, with a link back to the issue log entry
when there is one. That is compatible with the issue log's existing Links to Other Logs section and needs no
change to it.

#### Defects: where the government forms and this library disagree

Two of the readable forms **fold defects in**: GSA's "Type of Change" offers New Requirement, Change to Existing
Requirement and Defect, and the CDC form's type is Enhancement or Defect. This library's `bug-report` guide draws
the opposite line, and one named practitioner draws it too (Ian Devlin: a defect is "something is wrong with the
delivered code", a change request covers "things that are new and additional to what was delivered"). **The
template follows the library's line** and offers no Defect type; the companion reports that two public-sector
forms do, so a reader from that background is not told they are wrong.

#### The agile position, and who the bundle is for

The 2020 Scrum Guide routes change through the backlog: "Those wanting to change the Product Backlog can do so
by trying to convince the Product Owner." The Agile Manifesto ranks "Responding to change over following a
plan". **A team working that way needs no change request**, and the guide's When NOT to use says so first.
The bundle is for work where an agreed baseline carries weight outside the team: a fixed-price contract
("fixed-price contracts usually require a detailed and exact description of the subject matter of the contract
in advance", Wikipedia's "Agile contracts"), a regulated product (an Agile Alliance experience report maps
design changes onto "Change control procedures" in an FDA-regulated project), or a budget and scope a steering
group signed off. Two sharper agile claims (a Scrum.org forum thread, and a remark attributed to Mary
Poppendieck that needing a change request is itself a warning sign) were found only as search snippets and
**must not be quoted**.

#### Section design

Provisional, mirroring the CDC form's three actors and PM²'s four decisions, and expected to move:

| Section | In lean | What it carries |
|---|---|---|
| **The Request** | yes | What should change, in one sentence, and what it changes: which agreed artifact and version (the PRD, the acceptance criteria, the plan). Requester, date, and where it came from (decision, issue, risk, meeting). PM²'s "Current Situation" and "Desired Situation" are the published shape |
| **Why** | yes | The reason, and **what happens if it is not made**: NIST's sample asks for the expected impact of not making the change, and PM²'s process asks the assessor to "consider the impact of not implementing" it. Both lineages ask, which is why it is in lean |
| **Impact** | yes | On scope, schedule, cost, quality and risk, each stated or marked "none". PM²'s baseline list and the CDC form's hour, duration, schedule and cost impact are the published shapes. A table section, so it carries PRIORITY and ROW HINT |
| **Decision** | yes | Approve, reject, postpone or merge (PM²'s four), by whom, on what date, with any conditions. **One named decider**; the PMI Lexicon's change control board and PRINCE2's change authority are the two published forms of that authority |
| **Options Considered** | full only | Alternatives to the change as requested, including a smaller version and doing nothing. The CDC form's Recommendations and the PM analysis role |
| **Out of Scope** | full only | What this request does not change, so an approval is not read as broader than it was. PM²'s form carries it as a section of its own |
| **Implementation and Traceability** | full only | What was updated when the change was approved (which artifact, which new version), the change log entry, and links to the issue, risk or decision it came from. PM²'s form archives itself once the change is logged |

**What stays out of the template:** a back-out plan, configuration items, change types and a CAB. They belong
to the IT service lineage, and the companion places them there.

#### What makes it not a sibling

- **Not a `bug-report`** (above). A defect fails an agreement; a change request alters one.
- **Not the `rfc` bundle.** ITIL abbreviates a request for change as RFC; this library's `rfc` is a request for
  comments, a technical design proposal, in the IETF lineage ("Request for Comments"). **The guide names the
  collision on its first line**, and the catalog alias `RFC (ITIL)` is dropped, recommended.
- **Not the `issue-log`.** An issue may raise a change request; the request is not an issue in this library's
  convention (above), and it links back.
- **Not an `adr`.** An ADR records a technical decision already made; a change request asks an authority to
  decide on altering an agreed baseline.
- **Not a change log.** PMI: "The change log is used to record all submitted change requests." The log is a
  standing register, a separate catalog candidate (`change-log-governance`) that `governance-docs` admits as
  written; this bundle is one request.
- **Not IT change enablement.** The neighbour, above. DORA's 2019 report is the reason the companion does not
  present a change board as an unqualified good: it found that approval by "an external body such as a change
  advisory board (CAB) or a senior manager" had "a negative impact on software delivery performance", while
  holding that "there is still an important role for the CAB". **That finding is about production changes**,
  and the companion must not stretch it to a project change board.

#### Failure modes: mostly unsourced, and the build must say so

The research found **no verified source** for the failure modes a brief would expect: scope creep through
informal change (PMI's article was not read), requests that never get a decision, and change boards that
rubber-stamp project changes. Each is labelled as the library's own judgment or cut. **One tempting source
must not be used**: Prosci's "change fatigue" describes people absorbing too much organizational change, not a
flood of change requests.

#### Metadata

| Field | Value | Why |
|---|---|---|
| `family` | `delivery-docs` | ADR 0060 |
| `phase` | `deliver` | The only value the contract allows; a baseline change is raised while a unit of work is being delivered |
| `sizes_available` | `[lean, full]` **provisional** | The catalog says `S/M`. PRINCE2's request is light (the products to change and a justification) and the CDC form carries three actors' sections, the same split the other members make |
| `status` | `beta` | Every bundle |
| `methodology` | `generic` | PMI, PRINCE2, APM and PM² define it alike; the catalog's `ITIL` describes the lineage not served |
| `pairs_with` | `[]` | No pm-skills skill produces or consumes a change request (checked on pm-skills `origin/main`, 2026-09-25, with the direct contents call) |
| `related_templates` | `[prd, acceptance-criteria, bug-report, issue-log]` **provisional** | The baseline it changes, the agreement it alters, and the two bundles that route to it |
| `aliases` | `change record` kept; **`RFC (ITIL)` and `change ticket` dropped, recommended** | `RFC` collides with a shipped bundle; "change ticket" is service-desk vocabulary for the lineage not served. A build decision, argued in the research log |

#### What landing this bundle closes elsewhere

1. **The `delivery-docs` contract `0.2.0`**, which lands with ADR 0060 in the same change as this spec.
2. **`bug-report` and `issue-log` may link to the bundle**, a build decision; neither changes its position.
   **`rfc`'s guide owes one line** naming the ITIL collision from its side, because a reader who searches "RFC"
   today finds only the design proposal and nothing tells them there is another meaning.
3. **The catalog entry**, per [procedure 1](decision-procedures.md#1-a-catalog-call-loses-to-research):
   purpose, owner, category, methodology, relationships and aliases all describe the IT service lineage. Both
   `docs/internal/catalog.md` and `atlas/catalog-data.json`, then regenerate the atlas.
4. **This page's Progress table**, and GitHub issues #179 and #180.

#### The example

**A change request against the Saved Views PRD**, chained onto the delivery-docs scenario rather than the
governance one. `prd_example.md` (doc version 0.3.0, owner Priya Nair) lists as a non-goal "Scheduled delivery
of a view by email or Slack. Out of scope now; likely a fast follow." A request to bring it into scope, and a
decision to postpone it to a follow-on release, is exactly the case the type exists for, and it agrees with the
`release-notes` example, which ships no scheduled delivery. The request must be dated inside the PRD's life
(created 2026-06-12) and must not contradict any later sibling.

**One constraint from the governance side.** `issue-log_example.md` states that neither ISS-11 nor ISS-12 raised
a change request ("No request for change; no decision"), so this example must not attach one to either.

#### What the build costs

Two sizes, like `issue-log` ($16.76 whole, $14.29 for its 15 build agents). Build through `build-bundle.js`
with every agent on Sonnet.

**Outcome, 2026-09-25.** **7,203,075 weighted token-equivalents, $14.41 at API list rates**, 15 agents, every
one resolved to Sonnet ([report](../../bundle-builds/reports/change-request_v0.1.0.md)): research $6.01,
drafting $5.78, review $2.62. The review found 15 findings, one blocking (a sentence that credited ITIL 4's
glossary with a term its own log records it lacks); the main loop found two more that no lens flagged, the
templates' GOOD examples reusing the example's scenario and the example repeating the thread's known sharing
contradiction. Not counted: the admission sweep run while the spec was written, and the orchestrator's own
spend.

---

### governance-docs (fifth member): the change log

**`change-log`** - `governance-docs`, **`classification: utility`**, sizes **`[lean, full]`** (provisional),
methodology **`generic`** (provisional; corrects the catalog's `PMBOK/ITIL`), catalog id
`change-log-governance` (catalog 154 in [`catalog.md`](catalog.md), verbatim at
[`atlas/catalog-data.json`](../../atlas/catalog-data.json)), catalog name "Change Log
(governance)", aliases (catalog) `change register`, `change control log`. Catalog owner: PM / Change
Manager (open question, not source-confirmed; see Catalog corrections). Catalog purpose: "Track requested
and approved changes to baselines." Catalog contents: "change, requestor, impact, decision, date."
Catalog `stage`: governance. Catalog `formality`: lightweight. Catalog `rarity`: common. Catalog
`size_variant`: S. Catalog `relationships`: `[Change Requests]`. `tier: 2`, `tier_inferred: true`,
`must_have: false`, `built: false`, `state: candidate`.

**The bundle id is `change-log`, not the catalog id verbatim, and that is a design choice this spec makes
rather than inherits.** See "Deciding the bundle id" below.

#### Demand: the sibling that names it and defers it

Two shipped bundles already point at a standing change log without building one, and the deferral is
recorded, not implied:

- `change-request_companion.md:369-373` (`change-request`, the per-occasion document): "**Change request
  vs. the change log.** The request is not the log; PM²'s form is archived once logged into one
  [[8]](#ref-8), and the PMBOK errata describes the log as the register that collects submitted requests
  [[2]](#ref-2). HHS's EPLC program merges the two, a documented alternative rather than an error
  [[11]](#ref-11). A standing change log, if this library ever builds one, is a `governance-docs`
  candidate, not a variant of this bundle." *(As it stood 2026-09-27. The change-log landing rewrote
  this paragraph on 2026-09-28, now `change-request_companion.md:373-378`: HHS "shares one field list
  between them but keeps two artifacts", and the closing sentence names the built bundle.)*
- `change-request_template-lean.md:45`: "This document is not the change log; it feeds one."
- `change-request_template-full.md:23,242-254`: the full template's WHY and GOOD text both name the log as
  the request's destination once decided.
- `change-request_guide.md:58,76`: routes a reader to the full size "when the project keeps a change log
  this request must feed into cleanly," and the rubric's row 8 grades whether a filled request "names the
  change log entry (or states none is kept)."
- `issue-log_companion.md:60,358-361` and `issue-log_template-full.md:224-226,244` and
  `issue-log_guide.md:51-55`: `issue-log`'s own Links to Other Logs boundary names "a separate change log
  for submitted change requests" as the PMI convention it records against, and its TRAP line warns against
  "duplicating the risk register's or **change log's** own detail" instead of linking to it.
- `docs/internal/contracts/delivery-docs.md:13`: "it does not admit the standing register of such requests
  (a change log), which is a `governance-docs` instrument if it is ever built."
- `docs/internal/decisions/0060-change-request-joins-delivery-docs.md:84-86,105-106`
  (**ADR 0060, change-request joins delivery-docs**): considered and rejected building the log instead of
  the request ("it builds a different document from the one three bundles route to"), and states three
  times that `governance-docs` "admits a standing register as written" if the type is ever built.
- `atlas/catalog-data.json:3903-3926`: the candidate has carried `state: "candidate"` in the catalog since
  before either sibling shipped.

#### Deciding the bundle id: `change-log`, keeping `change-log-governance` as the catalog id

**Chosen: bundle id `change-log`.** Three reasons, weighed against the one real risk.

1. **Every other `governance-docs` member's bundle id is a bare type name, with no family qualifier.**
   `risk-register`, `raid-log`, `kpi-dashboard` and `issue-log` (**ADR 0057**, issue-log joins
   governance-docs as a fourth member) all drop any "-governance" or "-register" suffix the catalog's own
   compound naming might invite. Keeping `change-log-governance` as the bundle id would be the only member
   of this family to carry a family qualifier in its own directory name, for no mechanical reason.
2. **The library has already shortened a compound catalog id for a Tier-2 bundle twice.** `spike-report`
   ships under `spike-research-spike-report`'s catalog entry, and `test-summary-report` ships under
   `test-report-test-summary-report`'s. Both keep the compound string as the catalog id and ship the
   natural, shorter descriptive phrase as the bundle id. `change-log-governance` is the same shape: a type
   name plus a parenthetical qualifier the catalog added to disambiguate a candidate row, not a name a
   reader would search for whole.
3. **No mechanical collision exists either way.** `tools/mcp_server.py:371-384`'s `search_templates`
   matches a query against `b["id"].lower()` exactly or as a substring of the bundle's own joined
   `aliases`. A query `changelog` does not equal `change-log` (the hyphen differs) and is not a substring
   of this candidate's catalog aliases (`change register`, `change control log`); a query `change-log`
   does not appear inside `release-notes_meta.yaml:18`'s alias list either. `tools/check-bundles.py`
   resolves `future:` tags and cross-references by exact bundle id, which this decision does not touch.
   Checked directly against both files on 2026-09-27; neither normalizes hyphens.

**The risk, named rather than hidden.** `release-notes` carries alias `changelog` (`release-notes_meta.yaml:18`),
and `release-notes_companion.md:132-137` already draws the boundary from its own side: "A **changelog** is
a portable, permanent, structured record of every notable change, maintained with the project (Keep a
Changelog)... **Release notes** are a curated, often customer-facing summary for a specific release." A
plain-English reader who has that sentence in mind and then meets a bundle named `change-log` is one
short step from the wrong artifact, even though no string collides. **This is exactly the near-miss ADR
0059 (announcement-internal-comms joins delivery-docs) found for its own alias `release announcement`
against `release-notes`**, and that record's answer was to fix it in the build, not to avoid the name. This
bundle's guide and companion must name the collision on their first line, the way `change-request_guide.md`'s
first line already names the `rfc` collision, and `release-notes_guide.md` gains one routing line from its
own side (see What landing this bundle closes elsewhere). The catalog id `change-log-governance` is
unchanged, so any future `related_templates` or `future:` reference written against the catalog id still
resolves once the bundle directory is checked against it.

#### Admission: five independent named bodies, one already read by a sibling bundle

Every quotation below was checked against the source's raw text on 2026-09-27, in the main loop's re-check of
the admission sweep (`_local/research/2026-09-27_admission-sweep-3/`, gitignored). Three named standards
bodies and two named government bodies each define or ship the type by name, clearing
**ADR 0048** (one named source clears the admission test) with room to spare.

| Source | What it says or ships | Licence |
|---|---|---|
| PMI, *PMBOK Guide* 6th edition, errata (5th printing) | "The change log is used to record all submitted change requests." | PMI, hosted openly, no login wall |
| European Commission / PM² Alliance, *PM² Project Management Methodology Guide* v3.1, Appendix B.7 | "A Change Log is used to document, monitor and control all project changes." Ships an actual 17-field template across four groups (Identification and Description, Assessment and Action, Approval, Implementation); one of its eight Status values, in the Identification and Description group, "Waiting for approval," was independently re-checked against the live PDF on 2026-09-27 and passes | **CC BY 4.0** ("Document licensed under CC BY 4.0 license," raw-checked) |
| PM² Alliance, pm2.eu Artefacts listing | "template for Change Log document," "Free, downloadable and easy to edit" | Not independently confirmed on this listing page; the Guide it is drawn from is CC BY 4.0 |
| Association for Project Management (APM), UK chartered body, glossary | "A record of all proposed changes to scope" (entry name "Change register (or log)"; a separate entry, "Change log", reads "A record of all project changes: proposed, authorised, rejected or deferred." Entry names corrected 2026-09-28 by the build's research); independently confirms the register/log naming equivalence this candidate's own alias claims | Not stated |
| Connecticut Department of Social Services, Enterprise PMO, *Project Change Log* v1.1 | "Also known as Project Change Register." Ships a fielded, versioned, 11-column template | Not stated; presumed public-sector work product |
| US Department of Health and Human Services, EPLC, *Change Management Practices Guide* | "All projects, regardless of type or size, should maintain a change log and regularly manage requested changes." | US federal government work, presumptively public domain |

**Retrieval note for the build's research.** `hhs.gov` returns HTTP 403 to both `WebFetch` and
`rawcheck.py`; the HHS quotations above and below were read from the Internet Archive's `id_` raw copy
(`https://web.archive.org/web/2025id_/<hhs.gov URL>`), and the research log must cite
the archived copy actually read, the same convention `change-request`'s own spec already models
(`tier2-specs.md:1295-1308`). **One sentence in that same HHS folder is usable only as a fragment**:
"A submitter completes a CR Form and sends the completed form to the Change Manager" wraps a table-cell
break in the `.doc` extraction, and only "A submitter completes a CR Form and sends the" passed the
raw-text check. Do not quote the full sentence; either use the fragment or use the passing companion
quote below instead.

**What was not read, or does not admit the type.** The PMI *Lexicon of Project Management Terms* v5.0 has
no standalone "change log" entry; a full-text search returned zero hits, so the Guide's body defines the
term and the Lexicon does not, a factual gap rather than a boundary claim. ISO 21502:2020 is a commercial
standard and was not retrieved. The CDC Unified Process newsletter (`stacks.cdc.gov`) returns HTTP 403 and
and was not recovered from an archive copy in this pass, so its sentence, word for word the same claim the
HHS Practices Guide makes above, is not usable; cite HHS, not CDC. The ITIL glossary
mirror (IT Process Wiki) is rawcheck-passed but does not admit "change log" itself; see Boundaries below.

#### Structure: PM²'s four groups as the backbone, cross-checked by two independent government templates

**PM² Appendix B.7** (17 fields, four groups): Identification and Description (ID, Category, Title,
Description, Status, Requested by, Date Identified); Assessment and Action (Action Details, Size,
Priority, Target Delivery Date); Approval (Escalation, Decision, Decided by, Decision Date); Implementation
(Actual Delivery Date, Traceability and Comments). *(Corrected 2026-09-28: this placed Target Delivery Date in
the Approval group; Appendix B.7 places it in Assessment and Action.)* Its eight status values include "Waiting for approval,"
independently re-checked against the live PDF on 2026-09-27, and "Merged," which matches PM²'s own
four-decision vocabulary already adopted by `change-request` ("There are four possible decisions: approve,
reject, postpone or merge"). **Connecticut DSS** ships 11 columns, a different seven-value status list, and
states its own audience explicitly: "The audience for the Project Change Log includes the project team, project
sponsor, business owner, steering committee, and may include key project stakeholders." **HHS EPLC** ships a 15-column spreadsheet (`CR# | Current Status | Priority | Change
Request Description | Assigned To Owner | Expected Resolution Date | Escalation Required (Y/N)? | Action
Steps | Impact Summary | Change Request Type | Date Identified | Assoc ID | Entered By | Actual Resolution
Date | Final Resolution & Rationale`), independently parsed from its own binary spreadsheet cells rather
than a decoded-text summary. All three converge on: an identifier, a type or category, a description, a
requester, a date raised, a priority, a status, a named decision, a named decider, a decision date, and a
resolution. **No single status vocabulary is presented as canonical**; the template offers a sourced
default and states plainly that organizations customize it, the same move `issue-log`'s Priority Scale
section already makes for its own three published shapes.

#### Section design

Provisional, and expected to move once a build's own research runs:

| Section | In lean | What it carries |
|---|---|---|
| **Purpose and Boundary** | yes | What baseline changes this log tracks, and what does not go in: the per-instance change request (a separate document that feeds one row here), the software CHANGELOG (a different artifact under the identical word), a decision log (see Boundaries; thinly sourced), and configuration or version history. Names PRINCE2's exception up front, the way `change-request_guide.md`'s first line already names its own `rfc` collision |
| **Status Vocabulary** | yes | The status values this log uses, stated once so every row is comparable. Offers PM²'s eight, Connecticut DSS's seven, and HHS's set as sourced defaults, and states plainly that a team may adapt them. **POSITION**: not to present any one list as canonical, since no source claims its own list is universal |
| **Change Log** | yes | **The load-bearing section.** One row per change request: ID, type or category, title and description, requester, date raised, priority, status, decision, decider, decision date. Every field traced to at least two of PM², Connecticut DSS, HHS. A table section, so it carries PRIORITY and ROW HINT |
| **Escalation** | yes | Who acts, and under what condition, when a logged change needs authority above the log's normal decider. PM²'s Escalation field (Approval group) and HHS's `Escalation Required (Y/N)?` column are the two published shapes |
| **Implementation and Traceability** | full only | What was actually done once a change was decided: the actual delivery or resolution date, the artifact and version updated, and a link back to the change-request document this row came from and to any issue or risk that raised it. PM²'s Implementation group (Actual Delivery Date, Traceability and Comments) and HHS's Actual Resolution Date and Final Resolution & Rationale are the published shapes; the language should match `change-request`'s own Implementation and Traceability section so a request's exit point and this log's entry point read as one seam, not two vocabularies |
| **Review and Ownership** | full only | Who keeps the log and how it is reconciled to the baseline it tracks. **Thinly sourced**: the one supporting data point is HHS's own one-page checklist, whose sole ongoing activity is "Update the Change Management Log." Beyond that one line, the review cadence and reconciliation duty are this library's own judgment and must be labeled **POSITION**, not attributed |

#### Boundaries with each named neighbour

- **Not the change request (the per-instance document).** Three independent sources agree the log is the
  cumulative register and the request is the document that feeds one row into it: PM² documents a change
  "via a Change Request Form and in the Change Log" (`change-request_research-log.md:289`, already cited
  by the sibling bundle, not re-verified fresh in this pass); the PMBOK errata lists "Change log" and
  "Approved change requests" as two separate outputs; HHS's own Change Management Plan template defines one
  shared list of data elements for the "Change Request Form and Change Management Log", yet keeps two
  artifacts: its process table has a "Log CR" step ("The Change Manager enters the CR into the CR Log"), and
  HHS ships the log as its own spreadsheet.
- **PRINCE2 is the named exception, not an omission.** `prince2.wiki` (rawcheck-passed): "should be
  documented in the issue register or change log," folding change-request tracking into the Issue Register
  and naming a standalone change log only as an interchangeable alternative, not a mandatory companion
  document. State this plainly, by name, the same way `issue-log_companion.md:358-361` already states
  PRINCE2's parallel convention from its own side.
- **Not the software CHANGELOG (Keep a Changelog / `release-notes`' alias).** "A changelog is a file which
  contains a curated, chronologically ordered list of notable changes for each version of a project"
  (Keep a Changelog, rawcheck-passed). It has no requester, approver, decision, or status field at all; the
  identical word names a released-software artifact shipped with the codebase, categorically different
  from a governance register of pending and decided requests. Put this on the first line of the guide,
  since it is the single most likely mis-search, mirroring `release-notes_companion.md:132-137`'s own
  framing of the same boundary from its side. The pm-skills skill `utility-pm-changelog-curator` (checked
  2026-09-27 against `pm-skills` `origin/main`, 68 skills listed) targets exactly this software sense
  ("Draft CHANGELOG entries from git log"), not this candidate's governance sense; it is not a pairable
  skill here.
- **Not a decision log.** No rawcheck-passing quotation, from any source read this pass, names this
  boundary explicitly. Several vendor blogs converge informally on "a decision log records why a choice was
  made; a change log records what changed and who approved it," but none passed the raw-text check, and one
  attempted quote (bvop.org) failed it outright. **This boundary, if the companion states it at all, must
  be labeled the library's own POSITION**, not sourced.
- **Not configuration or version history.** HHS's own EPLC document archive keeps "07 - Change Management
  Plan" and "08 - Configuration Management Plan" as two separately numbered template categories, observed
  directly in the real archive URLs the research returned. This is a structural fact about the archive's
  own organization, not a quotation, and should be reported as such rather than dressed up as a sourced
  sentence.

#### Family fit and the ADR

**Governance-docs admits the type as written; the contract's own enumeration does not yet name it.**
`docs/internal/contracts/governance-docs.md:13`'s membership test ("a continuously-maintained register,
log, or dashboard ... to track risk, open items, or performance") describes a standing change log in its
own words, and **ADR 0060** states this three times without deciding it: "A register of requests is a
standing instrument; if it is ever built, it is a `governance-docs` candidate as written"
(`0060:106`). Every other family contract excludes the type on the same grounds `change-request` was
excluded from them (`delivery-docs.md:13`: an event-driven per-occasion form is not a standing register;
`standing-standards`: continuously revised, not agreed once; `decision-docs`, `qa-docs`, `process-docs`,
`communication-docs`, `discovery-docs`, `strategy-docs`: each excludes on the same ground ADR 0060 already
argued for the request itself, which applies at least as clearly to its standing register).

**What still needs stating, not assuming, is the same gap ADR 0057 (issue-log joins governance-docs as a
fourth member) closed for `issue-log`.**
`governance-docs.md:15` reads "The four roles are distinct but related," with an enumeration of exactly
four bullets and no change-log line. Admitting a fifth member without editing that sentence would leave
the contract's own prose out of step with its own membership, the same drift ADR 0057 and
**ADR 0050** (qa-docs admits a fourth member) each closed by amending the roles list and adding a dated
change note, not by treating the general membership sentence as sufficient on its own.
[ADR 0061](decisions/0061-change-log-joins-governance-docs-as-a-fifth-member.md) (change log joins
governance-docs as a fifth member) makes that edit, and the contract carries it in its 0.3.0 change note.

**One qualification the contract's own POSITION needs, that ADR 0057 did not have to add.**
`governance-docs.md:23` asserts, as the family's own reasoning rather than a sourced claim, that these
instruments "most often fail by collapsing into each other rather than by staying separate." PRINCE2 folds
change tracking into the Issue Register **by design**, not by failure, which is a named methodology choice
this contract's relationship story must accommodate rather than contradict. The change note ADR 0061 adds
should record this qualification with a date, per [procedure 11](decision-procedures.md#11-a-family-contract-asserts-something-about-the-world)
(a family contract's CLAIM sentences are tested against each new member's research log), so the sentence
stays a POSITION the library owns rather than a CLAIM this candidate's own admission evidence contradicts.

#### The worked example: the Reporting Platform Modernization program's change log

**The shared-scenario rule (contract section 4) is a hard constraint, and it is unusually specific here**:
the example must be this program's standing change-control log, and it must carry `CR-SV-01` exactly as
`change-request_example.md` states it, because that document already treats this unbuilt log as the place
its own decision was recorded:

> "This request went through the Reporting Platform Modernization program's change-control process, the
> one the program's issue log says every change request is handed to the day it is raised, and CR-SV-01 is
> its identifier there; this document is the record that process decided on."
> (`change-request_example.md:111-113`)

And `issue-log_example.md:43-46` states the same routing from its own side: "this program hands every
change request straight to its own change-control process the day it is raised, so no row below carries
one." **This candidate's example is that change-control process's own standing register** - the document
both siblings gesture at without instantiating.

**Facts the one entry must carry exactly, with no invention:**

| Field | Value | Source |
|---|---|---|
| Identifier | `CR-SV-01` | `change-request_example.md:3` |
| Title | "Scheduled Email Delivery for Saved Views" | `change-request_example.md:2` |
| Baseline artifact and version | Saved Views for Dashboards PRD, v0.3.0 | `change-request_example.md:4-5` |
| Requester | Priya Nair (PM, Reporting), submitted 2026-07-08 | `change-request_example.md:6-7` |
| Decider | Marta Reyes (Program Manager, Reporting Platform Modernization) | `change-request_example.md:8` |
| Decision and date | Postponed, 2026-07-18 | `change-request_example.md:9-10` |
| Origin | Not an issue, a risk, or a decision already on a program log; raised from account-management feedback | `change-request_example.md:50-55` |

**Constraints the example must not violate**, each already established in a sibling and not this library's
to re-decide:

- No row for `ISS-11` or `ISS-12`. `issue-log_example.md:131-132,139` states plainly that neither issue
  raised a change request ("No request for change," twice), a constraint **ADR 0060** already names for
  the sibling bundle's own example (`0060:119-120`) and that binds this example identically.
  `raid-log_example.md` and `risk-register_example.md` carry the same two issues under `R-03` and `R-06`
  and must not gain a change-log row either.
- The PRD stays at baseline v0.3.0. `change-request_example.md:114-115`: "the Saved Views PRD stays at its
  0.3.0 baseline, and no target version or release is set, because the release that would carry the work
  has not been scoped." A change-log row for `CR-SV-01` must show no artifact updated and no delivery date,
  matching that outcome rather than inventing one.
- Release 2.4.0 shipped 2026-06-30 with no scheduled delivery (`change-request_example.md:37-38`); nothing
  in this log may contradict that.
- If the drafting agent adds an illustrative second or historical row for realism, it must be dated inside
  a window no sibling example pins, or closed before the earliest date any sibling states (2026-06-14, the
  key-person risk's materialization), and it must not touch `R-03`, `R-06`, `ISS-11`, or `ISS-12`. **The
  safer build choice is one entry, `CR-SV-01`, stated plainly as the log's first and only logged change to
  date**, leaving a second row to a future build rather than to invention.
- `last_reviewed` (or equivalent frontmatter) should sit at or after 2026-07-18, the decision date, so the
  log reads as current with respect to its own one entry.

**A sibling sentence the landing PR corrects.** `change-request_companion.md:371-372` said "HHS's EPLC
program merges the two" (corrected 2026-09-28; the sentence is now lines 375-377), meaning the request form and the log. Both readings of the HHS plan template are
partly right. The template defines one shared list of data elements for the "Change Request Form and Change
Management Log", which is what `change-request`'s research log recorded. It also keeps two artifacts: a
"Log CR" step in which "The Change Manager enters the CR into the CR Log", and a log shipped as its own
spreadsheet. The landing PR gives the companion's sentence a dated correction to that reading.

#### Catalog corrections the landing PR must make

Per [procedure 1](decision-procedures.md#1-a-catalog-call-loses-to-research), both
`docs/internal/catalog.md:223` and `atlas/catalog-data.json:3903-3926`, then regenerate the atlas:

- **`methodology: "PMBOK/ITIL"` is contradicted.** No rawchecked source shows ITIL naming or shipping a
  "change log" as such. ITIL's own two rawcheck-passed artifacts are differently-named and narrower: a
  "Change Schedule" ("A Document that lists all approved Change Proposals and Changes and their planned
  implementation dates") and a "Change Record" ("documenting the lifecycle of a single Change"), and
  neither is a cumulative log of every submitted request the way PM²'s and Connecticut DSS's logs are.
  Every source that actually admits and structures this type (PMI, PM², APM, Connecticut DSS, HHS) shares
  the same lineage as `issue-log`'s own methodology correction. **Recommend `methodology: generic`**,
  matching `issue-log`'s and `change-request`'s own corrected values, and cite ITIL as a named neighbour in
  the companion instead of as a source.
- **Aliases should gain sourced terms, not lose the sourced ones already there.** `change register` is
  independently confirmed by APM's own glossary entry, "Change register (or log)," and should be kept.
  `change control log` has no source in this pass; **recommend it be sourced before the build or dropped**.
  *(2026-09-28: the entry name is corrected from "Change log (or log)". The build sourced `change control log`
  to one named practitioner, and no public body; see `change-log_research-log.md`.)*
  Recommend adding `change management log` and `change request log`, both directly attested by HHS's own
  named documents across three separate files.
- **`owner: "PM / Change Manager"` is an open question, not a correction.** Nothing read this pass either
  confirms or contradicts "Change Manager" as this type's owner; every source that names an audience names
  a role (PM, sponsor, business owner, steering committee) rather than a title. Flag it for the spec
  author or reviewer, not the build; do not invent a source for it.
- **`size_variant: "S"` likely undercounts the shipped shape.** The same correction `issue-log`'s own
  landing made: the catalog's single-letter size marker predates any research into the type's actual
  published shapes, and this pass's own structure findings (PM²'s four groups, Connecticut DSS's 11
  columns, HHS's 15 columns) support a two-weight `[lean, full]` split, not a single size.

#### `pairs_with`: checked, and empty

Checked 2026-09-27 against `pm-skills` `origin/main` directly (`gh api
repos/product-on-purpose/pm-skills/contents/skills --jq '.[].name'`, 68 skills returned) and against
`tools/known-skills.txt`. One name suggested a match and was read in full:
`utility-pm-changelog-curator` ("Draft CHANGELOG entries from git log via the pm-changelog-curator
sub-agent"). It targets the software CHANGELOG sense (Keep a Changelog, git-log-driven), not this
candidate's governance sense, and never mentions a change request, a baseline, or a change-control board.
No other skill name or description in the 68 suggests a governance change-log producer or consumer. On
current evidence, **`pairs_with: []`** is the correct value, the same posture `issue-log` and
`change-request` both adopt for the same reason.

#### Risks for the build and review

1. **The "five roles" enumeration lands with this spec, in the contract's 0.3.0 change.** A build that
   treated `governance-docs.md:13`'s general wording as authorization enough, without that edit, would repeat
   the gap ADR 0057 and ADR 0050 each closed rather than assumed.
2. **PRINCE2's exception must survive drafting, not get smoothed into the PMI/PM² consensus.** Every other
   named source agrees the log is a mandatory, separate companion document; PRINCE2 alone does not, and
   the companion must state its position by name, the same discipline `issue-log_companion.md:358-361`
   already keeps for its own PRINCE2 exception.
3. **The HHS quotations carry a retrieval hazard a research agent will hit if it tries the live URL.**
   `hhs.gov` returns 403; cite the Internet Archive `id_` copy, and do not quote "A
   submitter completes a CR Form and sends the completed form to the Change Manager" whole. Only the
   fragment "A submitter completes a CR Form and sends the" passed the raw-text check.
4. **The decision-log boundary is a POSITION at best, and must not gain an invented citation.** No source
   read this pass or the prior sweep passes the raw-text check on that specific distinction; state it as
   the library's own judgment or cut it, never source it after the fact to make the companion read more
   confident than the evidence.
5. **The alias and skill near-misses need a first-line disambiguation, not a rename that hides them.**
   `release-notes`' `changelog` alias and pm-skills' `utility-pm-changelog-curator` are both close enough,
   in plain English, to misdirect a reader even though no string collides mechanically. State the
   collision on the guide's and companion's first page, the way `change-request_guide.md` already states
   its own `rfc` collision, and add the one routing line `release-notes_guide.md` owes from its own side.
6. **The templates stage has repeatedly copied the worked example's own scenario into GOOD and WEAK text**,
   and no lens catches it reliably: `tier2-specs.md:1432-1434` records this exact failure surfacing in
   `change-request`'s own build, caught only by the main loop after every automated lens passed. **Every
   GOOD and WEAK illustration in this bundle's templates must use a scenario unrelated to the Reporting
   Platform Modernization program**, independent of the worked example, per the shareable-boundary rule
   (contract section 5) and the family's own contract section 3.7.
7. **The landing PR corrects `change-request_companion.md:371-372`'s "merges the two"**, as set out under
   the worked example, so the two companions describe HHS the same way. *(Done 2026-09-28; the corrected
   sentence is `change-request_companion.md:375-377`.)*

---

### standing-standards (fifth member): the production readiness review

**`production-readiness-review`** - `standing-standards`, **`classification: tool`** (maintainer's ruling,
2026-09-27; argued in [ADR 0062](decisions/0062-production-readiness-review-joins-standing-standards-as-a-tool.md)),
sizes **`[lean, full]`** (provisional), methodology **`SRE-lineage`**, catalog id `production-readiness-review`
(catalog 125), aliases `PRR`. Catalog owner: SRE. Purpose: "Assess whether a service is ready for production."
Contents, per the catalog: "reliability, monitoring, runbooks, capacity, on-call". `size_variant: M`, `rarity:
occasional`, `tier_inferred: true`. **The catalog row's own source column reads "Google SRE practice."**

#### Demand: prose routing, not a promise tag, and weaker than `issue-log`'s

No `future:` tag points here. `grep -rn "future:production-readiness" templates/` returns nothing, checked
2026-09-27. The demand is three lines of prose that already assume the type exists, plus the catalog's own
cross-reference:

- `templates/launch-coordination-checklist/launch-coordination-checklist_companion.md:464-469` gives the type
  its own subsection ("Launch coordination checklist and production readiness review") and states, without a
  tag to enforce it, "the two documents plausibly govern different moments of the same discipline."
- `docs/internal/tier2-specs.md:480-483` (the launch-checklist spec) asks its own research pass to "look for a
  second [source]: a production or operational readiness review published as a document," and says "one source
  suffices; a second would change the teaching." **This sweep found it**: three named sources publish the
  document, and several more describe the review.
- `docs/internal/decisions/0053-launch-coordination-checklist-joins-standing-standards-as-a-tool.md:41` and
  `:105` both name the relationship in passing ("relates to `PRR`"; "a PRR relationship").
- `atlas/catalog-data.json` already carries an asymmetric edge: `launch-coordination-checklist`'s
  `relationships` is `["PRR"]`; `production-readiness-review`'s own `relationships` is `[]`. The catalog
  promises the reverse link and does not pay it.

This is real routing, not a gate obligation the way `issue-log`'s `future:` tags were. No check fails today for
not building this type. It is, as the digest puts it, a maintainer scope call under
[ADR 0041 (maintainer preference sets the build order)](decisions/0041-maintainer-preference-sets-the-build-order.md),
made on 2026-09-27.

#### Admission: three named sources publish the document, and more describe the review

Every quotation below was checked against the source's raw text on 2026-09-27, either in the sweep's own
re-check pass or by a direct `rawcheck.py` call made while writing this spec (marked below). Four quotes are
cited to a different page than the one the sweep first filed them under, because the re-check found them
there.

| Source | What it says | Licence |
|---|---|---|
| Google, *Site Reliability Engineering* (O'Reilly, 2016), ch. 32, "The Evolving SRE Engagement Model" | "The SRE team establishes and maintains a PRR checklist explicitly for the Analysis phase." (re-checked in the main loop) | **CC BY-NC-ND 4.0**, confirmed by a direct `rawcheck.py` call against this page's own footer text, not carried from the launch-checklist spec's "CC BY-ND" note |
| Susan Fowler, *Production-Ready Microservices* (O'Reilly, 2016/2017), Appendix A | "This will be a checklist to run over all microservices," under the heading "A Production-Ready Service Is Stable and Reliable" and four more, ~35 items across the five, counted directly from the pages | Cited as Fowler, *Production-Ready Microservices* (O'Reilly, 2016), Appendix A, **via the sponsored O'Reilly excerpt** ("Compliments of", chapters 1, 3, 4, 7 and Appendix A), hosted by F5 |
| Mercari, Inc., `production-readiness-checklist` (Production Readiness Check, PRC) | "which is required for all services before receiving real production traffic"; "If a specific item is not applicable to your service check the item and explain" | **MIT** (GitHub API, 2026-09-27; not archived, last push 2021-11-22) |
| GitLab Inc., archived `.gitlab/issue_templates/production_readiness.md` | "This issue serves as a tracking issue to guide you through the readiness review"; "It's not the production readiness document itself" | Not stated on this file |
| GitLab Inc., the same project's `README.md` (cite here, not the issue template) | "The Production Readiness Review process has been superseded by" [PREP]. GitLab archived this project; do not cite it as a current process | Not stated |
| AWS, Well-Architected "Operational Readiness Reviews" whitepaper | "Amazon Web Services (AWS) created the Operational Readiness Review (ORR) to distill the learnings from AWS operational incidents"; "Teams perform self-assessments on operational risks ... throughout the complete lifecycle of their service, from inception to post-release operations"; "Any high-criticality findings are escalated to leadership as input to a go or no-go launch decision" | Not stated |
| AWS, the same whitepaper's `the-orr-tool.html` sub-page (cite here, not the landing page) | "The main tool for ORR is the checklist of questions itself"; grouped under "Release quality" and "Event management"; a third heading, "Architecture," re-checked directly with `rawcheck.py` on 2026-09-27 rather than left "not retested" | Not stated |
| AWS, `inspect-the-process.html` | "When was your last ORR performed" | Not stated |
| Microsoft, Azure Well-Architected `operational-excellence/maturity-model` (cite here, not `/checklist`) | "Level 3: Release readiness"; "Testing becomes a go-live requirement to ensure safe and stable deployments" | Not stated |
| Grafana Labs, company blog | "Production readiness review (PRR) is a process that originated at Google"; "a completely separate process ... having the product in question reviewed by an experienced engineer, ideally outside of the product team"; "We're looking into a periodic and/or incremental PRR as part of our continuous product improvements" | Not stated |
| GitLab Inc., `docs.runway.gitlab.com` platform guide | "SaaS Platforms uses production readiness review process for new services" | Not stated |
| Google Cloud, "How SREs find the landmines in a service" (CRE Life Lessons) | "During an SRE entrance review (SER), also referred to as a Production Readiness Review (PRR), the SRE team takes the measure of a service currently running in production" | Not stated |
| Cortex, `docs.cortex.io` Scorecard docs | "Scorecards automate the process of checking whether services meet criteria such as ownership, on-call coverage, runbooks, monitoring, and security requirements" | Not stated. **Do not** cite Cortex's specific 6-category/24-item breakdown; it failed `rawcheck` (a JS-rendered marketing page returning 245 extractable characters) |

**Three sources publish the document**: Fowler's Appendix A, GitLab's template and Mercari's checklist.
Google's chapter 32 says its SRE team maintains a PRR checklist. Grafana, GitLab's Runway guide, AWS and
Microsoft describe the review practice without shipping the document, and Cortex describes a live scorecard
product, which is out of scope for a Markdown template. That clears
[ADR 0048](decisions/0048-one-named-source-clears-the-admission-test.md)'s one-source floor three times.
Confidence: high.

**A name collision, confirmed and out of scope.** NASA's *Systems Engineering Handbook* Appendix B ("A review
for projects developing or acquiring multiple or similar systems greater than three ... The PRR determines the
readiness of the system developers to efficiently produce the required number of systems") and AcqNotes'
DoD-acquisition glossary ("The Production Readiness Review (PRR) determines if a systems design is ready for
production," "normally performed as a series of reviews toward the end of the Engineering [and Manufacturing
Development phase]") both publish "Production Readiness Review" as a written document, and both quotes passed
`rawcheck`. This is a hardware-manufacturing-readiness gate from an unrelated discipline that predates the SRE
usage; it shares only the name and is not this bundle's subject. The companion needs one disambiguating
sentence; the template needs none.

**What must not be carried into a companion.** The claim that SRE book chapter 32 calls the Launch Coordination
Engineering team "a lighter-weight alternative" is refuted: the phrase is not on the chapter's page, which a
direct raw-text check confirmed. Chapter 32's only cross-reference to that team is
that it "spends a majority of its time consulting with development teams." Say no more than that.

#### The launch-checklist boundary: this is the central review risk

**The subject-matter distinction fails, and the spec must say so plainly rather than assert cross-functional
scope by inference.** A gap-fill retrieval in this sweep read Google's own Appendix E, "Launch Coordination
Checklist" (`sre.google/sre-book/launch-checklist/`), which `docs/internal/tier2-specs.md:442-457` already
counted at ten areas and 31 items. Every one of its ten section headings is engineering- or operations-scoped:
Architecture; Machines and datacenters; Volume estimates, capacity, and performance; System reliability and
failover; Monitoring and server management; Security; Automation and manual tasks; Growth issues; External
dependencies; Schedule and rollout planning. None names marketing, legal, external communications, or
pricing/go-to-market. So the boundary cannot rest on "PRR is engineering-only, the launch checklist is
cross-functional": both are engineering-scoped in their own founding documents. **The distinction that survives
is trigger, team, and timing**, all three sourced to the same primary chapters:

| Axis | Production Readiness Review (ch. 32) | Launch Coordination Checklist (ch. 27) |
|---|---|---|
| Trigger | "a development team requests that SRE take over production management" of a service already running | "Most audits are conducted before a new product or service launches" |
| Team | "Usually one to three SREs are selected or self-nominated to conduct the PRR" | "The Launch Coordination Engineering (LCE) team," "held to the same technical requirements as any other SRE" |
| Timing | "The Production Readiness Review can be started at any point of the service lifecycle" | Pre-launch, gatekeeping: "Acting as gatekeepers and signing off on launches determined to be" safe |

*(Corrected 2026-09-28, when the bundle was built: trigger and timing separate the two in Google's chapters, not in
adopters' practice. Mercari requires its check "for all services before receiving real production traffic",
GitLab gates each maturity level of a new service, Grafana writes of a "pre-launch PRR", and the US Federal Student
Aid office runs a PRR on every release before implementation, so a PRR and a launch checklist can meet at the same
launch. What differs in every source read is the object: a PRR reviews a service's standing ability to be run, and
the launch checklist reviews one launch. That reading is this library's, and the companion labels it so. The
quotations are in the [research log](../../templates/production-readiness-review/production-readiness-review_research-log.md), contested item 10.)*

A second, independent framing agrees without naming either type: Studio Red's practitioner guide draws a
release-moment-versus-long-term-operability line, already quoted at
`launch-coordination-checklist_companion.md:472-473` (ref 38). That source was not re-verified against its
primary text in this sweep, so it is reported here as the sibling companion's own citation, not this sweep's,
and is not requoted.

**The new companion must agree with `launch-coordination-checklist_companion.md:464-469`, not restate it
differently.** That section already holds the position "the two documents plausibly govern different moments
of the same discipline" and explicitly declines to claim replacement or sequence. This bundle's own
Relationships section states the same position from its side, adds the trigger/team/timing table above as the
evidence for it, and **retracts the subject-matter half of the argument** rather than repeating it, because
Appendix E now falsifies it directly. Per `decision-procedures.md` section 11, that retraction is the honest
move: a claim a later retrieval falsifies is corrected in place, not defended.

**A second neighbour, AWS's Operational Readiness Review, is the same shape at a different cadence.** ORR is
reviewed "throughout the complete lifecycle of their service, from inception to post-release operations" and
tracks "When was your last ORR performed" as a standing metric (cited to `inspect-the-process.html`). Google's own PRR is, on the sources read here, closer to one-time
("Once the issues have been fixed, the product has passed the PRR," Grafana), while Grafana itself reports
reconsidering that design ("We're looking into a periodic and/or incremental PRR"). **Cadence is contested
across real adopters, not settled**, and the template's Review Trigger section, not a fixed assumption, is
where that dispute belongs.

**A third neighbour, the runbook, is complementary rather than competing, and the catalog under-states it.**
Every PRR source that ships an actual checklist checks that a runbook already exists rather than producing one:
Cortex's scorecard criteria include "runbooks" by name; GitLab's and Fowler's checklists ask for one as an
input (per the launch-checklist bundle's own already-published research log, not re-verified here). `runbook`'s
catalog `relationships` field is `[]` despite this; the catalog corrections below add the reverse edge.

**A fourth neighbour, the Change Advisory Board, is a different unit of review, both raw-checked.** A CAB
"delivers support to a change-management team by advising on requested changes" and "is responsible for
oversight of all changes in the production environment" - a portfolio-wide, standing panel reviewing many
changes across many services, not a per-service technical assessment. The two do not overlap in scope or
grain.

**A fifth neighbour, Definition of Done, differs in object and authority, both raw-checked.** The Scrum Guide's
DoD is "a formal description of the state of the Increment," a per-work-item bar the Developers agree and judge
themselves against every sprint. A PRR is service-level, typically reviewed by someone other than the team that
built the service ("an experienced engineer, ideally outside of the product team," Grafana), and its cadence is
occasional-to-periodic rather than every increment.

#### Family fit: `standing-standards` admits the standing questionnaire; the per-service record does not exist as a separate type

**Two readings, one membership answer.** A maintained PRR checklist (the questionnaire) passes the family's own
falsifier the same way `launch-coordination-checklist` did: it is "consulted at the moment of action," per
[ADR 0053](decisions/0053-launch-coordination-checklist-joins-standing-standards-as-a-tool.md)'s test, restated
at `docs/internal/contracts/standing-standards.md:102-104`. A per-service review record (one team's filled
answers for one service, one time) excludes from every family tested, standing-standards included, on the
contract's own analogy: "a runbook written for one incident is an incident report"
(`standing-standards.md:31`). **This resolves the library's stated either/or**: the bundle is the standing
questionnaire, and the worked example is a filled instance of it, exactly the relationship
`launch-coordination-checklist_example.md` already has to its own template.

**`governance-docs` admits with strain, not as written.** Its membership test names "a register, log, or
dashboard" (`docs/internal/contracts/governance-docs.md:11`); a review checklist with pass/fail criteria is
none of the three in form, even though its whole-lifecycle framing (AWS's ORR, above) matches the family's
spirit. `standing-standards` fits the letter as well as the spirit; this spec follows the maintainer's ruling
into that family.

**Every phase-axis family excludes, on the catalog's own `stage: release` value**, which sits outside each of
`qa-docs` (`develop`), `decision-docs` (`develop`), `delivery-docs` (`deliver`), `discovery-docs` (`discover`),
`process-docs` (`iterate`), `communication-docs` (`utility`, audience
inside the team, not outside), and `strategy-docs` (organization-wide direction, not one service).

**This is the family's first unforecast member, and that is worth naming rather than hiding.**
`standing-standards.md:40` names only "a coding-standards or engineering-handbook document" as a likely future
member. Unlike `launch-coordination-checklist` and `definition-of-ready`, which the contract predicted by name
before either was built, this admission rests entirely on the membership test and the falsifier, not on a
forecast the contract can be shown to have gotten right. Per
[ADR 0057](decisions/0057-issue-log-joins-governance-docs-as-a-fourth-member.md)'s principle, "the membership
test, not the list of members that happened to be planned, governs a candidate," so this does not weaken
admission; it does mean the ADR cannot claim the forecast's confirmation the way ADR 0053 and ADR 0058 could.

#### Section design

Provisional, drawn from the intersection across sources rather than any one source's exact taxonomy (no two of
Fowler, Google, GitLab and AWS agree on section count or naming), and expected to move:

| Section | In lean | What it carries |
|---|---|---|
| **Scope and Trigger** | yes | What counts as "production" here, and what event starts a review: an SRE-ownership handoff ("a development team requests that SRE take over production management"), a maturity-gate promotion (GitLab's Experiment/Beta/GA), or a periodic re-review (AWS's ORR). A review with no stated trigger is applied to everything or nothing, the same trap `launch-coordination-checklist`'s Scope section names |
| **Reviewer and Authority** | full only | Who conducts the review and who decides the outcome. Sourced: "Usually one to three SREs are selected or self-nominated" (Google); "an experienced engineer, ideally outside of the product team" (Grafana). Neither source ties this to a single named decision authority the way `launch-coordination-checklist`'s Roles section does; the template supplies the field and the companion says so |
| **Readiness Criteria** | yes | **The load-bearing section.** Checks grouped by domain, each with the evidence that answers it and an owner. Domain list is the counted intersection: architecture and dependencies, capacity and scalability, monitoring and alerting, on-call and incident response, deployment and rollback, security, and data/backup/DR - drawn from the areas Google's chapter 32 names a PRR evaluates, Fowler's five headed sections, GitLab's per-gate subsections and AWS's Architecture/Release-quality/Event-management grouping, not copied from any one. A table section: carries PRIORITY and ROW HINT |
| **Not-Applicable Rule** | yes | An item marked not-applicable must carry a written reason, not a blank check. **Sourced, for once**: Mercari's PRC states this rule directly ("If a specific item is not applicable to your service check the item and explain") |
| **Outcome and Sign-off** | yes | What the review concluded: passed, passed-with-conditions, or not ready, and who signed. Fowler and Grafana both describe a pass/fail outcome ("the product has passed the PRR"); neither publishes a fixed vocabulary for it, so the template supplies one and the companion labels it as this library's own |
| **Review Cadence** | full only | Whether this review is one-time, periodic, or triggered by a later event, and why. **Genuinely contested across sources, not a default**: Google/Grafana currently one-time-but-reconsidering versus AWS's ORR already periodic ("throughout the complete lifecycle"). The template asks the filler to state a position rather than assuming one |
| **When This Does Not Apply** | full only | Services or changes exempt from a full review, and what smaller check they get instead. Mirrors `runbook` and `launch-coordination-checklist` |
| **Review Trigger** | yes | **Contract-mandated** (section 4): a named owner and a condition, not a calendar. Candidate condition: a production incident whose contributing cause a passed criterion should have caught, tying this section to `incident-postmortem` the way `launch-coordination-checklist`'s does |

#### Catalog corrections the landing PR must make

Per [decision-procedures.md procedure 1](decision-procedures.md#1-a-catalog-call-loses-to-research), both
`docs/internal/catalog.md` and `atlas/catalog-data.json`, then regenerate the atlas:

1. **Aliases: add, sourced.** "production readiness checklist" and "PRC" (Fowler's and Mercari's own names for
   the artifact they ship); "SRE entrance review" and "SER" (the Google Cloud CRE blog's own interchangeable
   usage inside Google: "also referred to as a Production Readiness Review (PRR)").
2. **Aliases: drop, unsourced and collision-prone.** "launch readiness review" has no supporting quotation in
   any source this sweep or the launch-checklist bundle's own research read, and it is the phrase most likely
   to be typed by a reader actually looking for `launch-coordination-checklist`. Recommended, not gate-mandated.
3. **Relationships: reverse the edge.** `production-readiness-review`'s `relationships` is `[]` while
   `launch-coordination-checklist`'s already carries `["PRR"]`; add `["launch-coordination-checklist"]` here.
4. **Relationships: `runbook` gains a forward edge.** Every PRR source that ships a real checklist checks for an
   existing runbook; `runbook`'s own `relationships` is `[]`. Add `["production-readiness-review"]`.
5. **The name collision goes in the guide and companion, not the catalog row.** `gen-atlas.py` blanks
   `state_note` for a built type, so the one-line note that "Production Readiness Review" also names a DoD and
   NASA hardware-manufacturing milestone belongs on the guide's first page and in the companion.

#### `pairs_with`: checked, empty

`gh api repos/product-on-purpose/pm-skills/contents/skills --jq '.[].name'` returned all 68 skill names on
2026-09-27. No name contains "readiness" that targets production or
operational readiness: the two hits, `tool-design-sprint-readiness` and `tool-foundation-sprint-readiness`, are
design-sprint and foundation-sprint precondition checks, unrelated in subject. `deliver-launch-checklist`, the
one plausibly adjacent skill, already pairs with `launch-coordination-checklist`
(`launch-coordination-checklist_meta.yaml:15`), not this type. **`pairs_with: []`**, per the contract's own rule
that a member "adopts `[]` until one does."

#### Risks for the build and review

1. **The launch-checklist boundary is the finding a reviewer will test hardest.** The subject-matter argument
   is refuted by this sweep's own gap-fill retrieval; only trigger, team and timing survive. A companion that
   reaches for the easier, refuted line ("PRR is engineering, the launch checklist is cross-functional, so
   they're obviously different documents") will fail review on a claim this same sweep already falsified.
2. **The "lighter-weight alternative" phrase is a live temptation** because it appears in two of this sweep's
   own returns as if confirmed. It is refuted by a direct raw-text check; do not carry it into the companion under any
   paraphrase that keeps its substance.
3. **Cortex's specific category/item breakdown failed rawcheck** and must not be quoted or paraphrased as a
   specific structure; only its general Scorecard description (docs.cortex.io, raw-checked) is usable.
4. **The build workflow's templates stage has repeatedly copied the worked example's own scenario into the
   template's GOOD text**, a defect this library has already named and not yet mechanically gated. The
   Readiness Criteria section's GOOD and WEAK illustrations must describe a service and an incident **other
   than** the example's Acme Analytics dashboard-service PRR below; grep the drafted templates for the
   example's proper nouns (Acme, Dana Osei, Marcus Bell, Sam Okafor, Anjali Rao, Priya Nair, DEF-2291,
   dashboard-service) before review, the way the digest recommends for every build.
5. **This is the family's first unforecast member and its fifth overall.** The contract's own coherence
   caveat ("this family's coherence is thinner than `governance-docs`' or `strategy-docs`'") was written for
   three members; a fifth, unforecast one is exactly the kind of candidate the falsifier exists to test
   rigorously rather than wave through on precedent.
6. **No source read supplies a fixed pass/fail vocabulary** for a review's outcome, or a full list of failure
   modes. Only three failure modes are sourced (below); everything else must be labelled the library's own
   judgment or cut, per `review-standards.md` section 5's dominant-defect-class rule. *(Corrected 2026-09-28,
   when the bundle was built: the bundle's research found both. OneUptime's practitioner guide publishes four
   decision states, of which the template takes "Ready", "Ready with conditions" and "Not ready", attributed to
   that guide and not presented as a standard. The sourced failure modes grow from three to eight: a third from
   Alves, three antipatterns that Nolan's talk names, and drift after a one-time review, which the adhorn ORR
   template names outright. The [research log](../../templates/production-readiness-review/production-readiness-review_research-log.md) quotes all eight.)*

**Failure modes, sourced, and nothing beyond these three without a citation** *(eight since 2026-09-28; see the
correction to item 6)*:

- Lack of buy-in: "Running a PRR without any specific goal means that the PRR can drop to the bottom of the
  development team's priority list" (Alves, USENIX).
- Defensiveness from the reviewed team: "If the development team feels threatened by the review" (Alves).
- Engagement starting too late to change the design: "The main limitations of the PRR Model stem from the fact
  that the service is launched and serving at scale," and "SRE engagement starts very late in the development
  lifecycle" (Google, ch. 32). This is the sharpest of the three, since Google names it as the model's own
  stated limitation, not an outside critique.

Do not assert "checkbox exercise," "findings never followed up," or "criteria not tailored to the service" as
sourced findings; none surfaced in a raw-checked quotation in this sweep.

#### The worked example: a scenario, not a launch, chained onto facts that already exist

**This must not be the Saved Views Sharing launch itself, or the example collapses into
`launch-coordination-checklist_example.md`'s own scenario and the spec's central boundary argument (trigger:
ownership handoff, not launch date) has nothing to demonstrate.** The proposed scenario is the SRE-lineage
trigger directly: after the Saved Views Sharing launch stabilizes, Acme Analytics' Platform team requests that a
newly formed Acme Analytics SRE function take over production ownership of `dashboard-service`, the same
service the `sdd` and `test-plan` examples describe, and the review this bundle demonstrates is the one that
decides whether SRE accepts. *(Corrected 2026-09-28: `dashboard-service` belongs to the Reporting team, whose
Staff Engineer Marcus Bell `runbook_example.md:5` names as its owner, so Reporting makes the request, not Platform.
The example also names two reviewers outside Reporting: Ines Halvorsen from the new SRE function, the team
Google's ch. 32 says conducts the review, and Dana Osei, the outside engineer Grafana describes.)*

- **Date: 2026-08-22.** Later than every date the sibling thread already occupies (PRD created 2026-06-12;
  DEF-2291 discovered 2026-07-13; the exit review and launch, 2026-07-17; the Reporting Squad DoD's amendment,
  2026-07-24; the entitlement-audit runbook's first live use, 2026-07-28; the dashboard-scoped kill-switch
  acceptance's own expiry, 2026-08-15), so the review can reference each of those events as already-settled
  history without needing to reconcile a date against them.
- **People: reuse the thread's named roles, in the roles the sources give them.** Dana Osei (Staff Engineer,
  Platform; `launch-coordination-checklist_example.md:57`) is the natural reviewer per Grafana's "an
  experienced engineer, ideally outside of the product team," because Dana holds decision authority across
  launches rather than owning `dashboard-service`'s day-to-day code. Marcus Bell (`launch-coordination-checklist_example.md:58`;
  `runbook_example.md:5`) is the service owner answering the review, the position Google's ch. 32 describes as
  the requesting development team.
- **Content it may chain onto, without repeating the launch checklist's own table rows.** The review may cite
  that DEF-2291 occurred (2026-07-13) and that a regression guard and an entitlement-audit reconciliation job
  exist as a result (`runbook_example.md:32-33`), as evidence its Readiness Criteria section's monitoring and
  on-call rows can point to. **It must not restate the specific checks `launch-coordination-checklist_example.md`
  already runs** (the permission matrix, the dashboard-scoped kill switch); a PRR reviewing whether SRE takes on
  a service asks different questions (on-call rotation ownership, alerting coverage, capacity headroom, backup
  and DR) than a launch checklist asks about one specific change.
- **The build number contradiction it must simply not touch.** `release-notes_example.md` dates build/version
  2.4.0 at 2026-06-30; `launch-coordination-checklist_example.md:109` dates build 2.3.2 at 2026-07-14;
  `runbook_example.md:32` and `incident-postmortem_example.md:28` both describe a build numbered 2.4.0 as
  postdating DEF-2291 (2026-07-13). No file reconciles this. **The PRR example must cite no build or release
  number for `dashboard-service` at all**, referring only to dated events (the incident, the launch, the
  amendment) the way this spec does above.

Per the family's own shared-scenario rule (`standing-standards.md` section 4), the chaining stays loose by
design: this is a standing instrument belonging to the Platform and the new SRE function, shown as it stood at
one review, not a record that only this launch could have produced.

#### Metadata

| Field | Value | Why |
|---|---|---|
| `family` | `standing-standards` | Maintainer ruling, 2026-09-27; argued in ADR 0062 |
| `classification` | `tool` | Maintainer ruling. Argued marker-by-marker in ADR 0062 against `standing-standards.md`'s section 2 cut: executed by someone other than the service's own author ("an experienced engineer, ideally outside of the product team," Grafana; "one to three SREs ... selected or self-nominated," Google), at the moment SRE takes on a service, not a standard the service's own team is judged against on a schedule |
| `sizes_available` | `[lean, full]` **provisional** | GitLab's three maturity gates (8, 4 and 6 subsections, counted from the raw template) show a real tiering pattern beyond Fowler's flat five-section list; lean carries the flat engineering-readiness core (Scope and Trigger, Readiness Criteria, Not-Applicable Rule, Outcome and Sign-off, Review Trigger), full adds the gating and cadence apparatus (Reviewer and Authority, Review Cadence, When This Does Not Apply). This split is this library's own judgment, not any one source's structure |
| `status` | `beta` | Every bundle |
| `methodology` | `SRE-lineage` | Matches its closest sibling, `launch-coordination-checklist_meta.yaml`'s own value, rather than `runbook`'s `DevOps/SRE` or the catalog's plain `SRE`; nearly every admission source in this sweep sits inside the same Google-originated lineage |
| `pairs_with` | `[]` | Checked against pm-skills `origin/main`, 2026-09-27; no skill produces or consumes this type |
| `related_templates` | `[launch-coordination-checklist, runbook, definition-of-done]` **provisional** | The neighbour the boundary risk names, the instrument it checks for rather than replaces, and the family sibling it is classified alongside |
| `aliases` | `PRR` kept; **add `production readiness checklist`, `PRC`, `SRE entrance review`, `SER`**; **drop `launch readiness review`, recommended** | See catalog corrections above |

#### What landing this bundle closes elsewhere

1. **The `standing-standards` contract's Members line**, from "not yet built" to the build date. The contract
   moved to `0.4.0` in the spec PR, with ADR 0062.
2. **`launch-coordination-checklist_companion.md`'s own Relationships subsection is not changed by this
   landing**; it already holds the position this bundle's companion must agree with. Whether it gains a direct
   link to the new bundle is a build decision, not a required edit.
3. **The catalog entry**, per the corrections above, in both `docs/internal/catalog.md` and
   `atlas/catalog-data.json`, then the atlas regenerated.
4. **This page's Progress table.**

#### What the build would cost

No build has run for this type. Projected from the two most recent Tier-2 bundles built through the committed
`build-bundle.js`, both with every agent resolved to Sonnet: `issue-log` at $16.76 whole ($14.29 for its 15
build agents) and `change-request` at $14.41 whole ($14.41 for its 15 build agents, research $6.01, drafting
$5.78, review $2.62). A whole-bundle estimate of **$14 to $17 at API list rates** is reasonable on that basis;
it is a projection, not a measurement, until `python tools/gen-bundle-build-report.py --ingest` runs against an
actual build report.

---

### discovery-docs (reopened, third member): the project brief that reopens a closed family

**`project-brief`** - `discovery-docs`, **`phase: discover`**, sizes **`[lean, full]`** (provisional),
methodology **`PRINCE2`**, catalog id `project-brief` (catalog 71), catalog name "Project Brief", aliases
`lightweight charter`, `project one-pager`. Catalog owner: PM. Purpose, per the catalog: "Lightweight project
definition for smaller efforts" (corrected below). Contents, per the catalog: "objectives, scope, timeline,
budget, stakeholders". `size_variant: S`, `rarity: common`, `tier_inferred: true`, `relationships: [Charter]`.
**The maintainer ruled 2026-09-27: build, and reopen `discovery-docs` to admit it.** The contract
edits of [ADR 0063](decisions/0063-project-brief-reopens-discovery-docs.md) landed with this spec, so the
metadata below is written against the reopened contract.

#### Demand: a shipped bundle already routes a reader here, and already names a source for it

**`business-case`, already shipped, routes a reader to this type by name, defines the boundary against itself,
and cites a named source for it**, the same routing shape `issue-log`'s demand section rested on:

- `business-case_guide.md:17`: "a **project brief** | you need a short overview for starting up a project,
  not an investment case. A project brief absorbs an outline business case as one component and retires once
  initiation documentation exists; the business case itself keeps being refined, it does not retire with the
  brief".
- `business-case_companion.md:315-317`: "It is not a project brief: PRINCE2's project brief is 'a short,
  high-level overview of the project, created during the starting up a project process,' and it absorbs an
  outline business case as one component before retiring once the project initiation documentation exists;
  the business case itself is not retired the same way, it continues to be refined [[32]]."
- `business-case_companion.md:420`: reference 32 is "PRINCE2 Wiki. 'Project brief,' management products,
  baselines," already logged as a citation in a shipped bundle's research trail.
- `business-case_template-full.md:37` and `business-case_template-lean.md:32` both carry the same boundary
  sentence in the template body itself: "It is NOT a project brief (a short overview that absorbs an outline
  business case as one component...)".

The shape is the same as `issue-log`'s: a "You actually need | Because" chooser row in a shipped guide, plus a
companion and both templates that state the boundary in their own body text. No gate flags it, because nothing
here is a stale `future:` reference; it is a named, cited, boundary-defining neighbour that a shipped bundle
has been describing the edges of without the library building it.

#### The family: `discovery-docs`, reopened by amendment (ADR 0063), not widened

This is not the `change-request` pattern. ADR 0060 widened `delivery-docs`'s own membership test to admit a
type no contract test passed. Here, one contract's test already admits the type: `discovery-docs`'s own
membership clause, "exists to decide whether to build something, before anyone commits to building it"
(`discovery-docs.md:33-34`), fits a project brief without strain on that sentence alone. **What blocks
admission is not the test; it is the contract's own closure statement**, "`discovery-docs.md:6`: "Members:
`business-case`, `user-persona`. The family is closed at two." That closure recorded
[ADR 0035](decisions/0035-prototype-brief-fails-the-admission-test.md)'s **outcome** for a different candidate,
`prototype-brief`, whose own admission test failed. It was never written as a rule that no fourth candidate
could ever be tested; ADR 0031 said the opposite in advance: a two-member result was "a legitimate outcome and
not a failure of the contract" (`0031:54`), a statement about that research's result, not a permanent ceiling.

The strain the maintainer must weigh, named plainly rather than argued around: the UK Government's own primary
guide states "Approval of the Project Brief is the official start of the project" (BIS 2010, raw-checked,
below), which reads as the commitment trigger itself, not a document that only informs a commitment made
afterward. [ADR 0063](decisions/0063-project-brief-reopens-discovery-docs.md) carries this strain in its body
and states this library's own POSITION on it: approval of the brief commits to **initiating**, to spending
effort finding out whether to proceed, not to **building**; the document that commits to building is a
project charter or PID (unbuilt in this library), or a PRD once the investment is approved. That is the same
distinction prince2.ca draws for the type against PMBOK's charter (below), read onto the family boundary.

#### Admission: retrieved and raw-checked, on a wide named-source base

Every quotation below passed the main loop's raw-text re-check on 2026-09-27.
**At least four independently named bodies publish "project brief" as a written document, not merely a
practice**, and the AXELOS glossary is the strongest of them because it is the standards body itself, not a
practitioner's reading of it.

| Source | What it says | Licence |
|---|---|---|
| AXELOS Limited, *PRINCE2 Glossary of Terms English* v.1.1 (2012, PRINCE2 2009 edition), read via the Internet Archive because the live host no longer serves the file | "Statement that describes the purpose, cost, time and performance requirements, and constraints for a project"; created "pre-project during the Starting up a Project process"; "superseded by the Project Initiation Documentation and not maintained" | AXELOS, all rights reserved: short quotes only, never adapted |
| UK Government, Department for Business, Innovation and Skills, *Guidelines for Managing Projects* (November 2010) | "the Project Brief says why the project is needed, what it must achieve and who should be involved"; "Approval of the Project Brief is the official start of the project" | **Crown copyright, Open Government Licence**: adaptable with attribution |
| prince2.wiki, "Project brief" (practitioner, edition of the underlying manual not stated on the page) | "a short, high-level overview of the project, created during the starting up a project process by the project manager"; the composition list begins "background, objectives, scope" and continues, per the page, through constraints, risks, stakeholders and "outline business case"; "the project brief is no longer used in project management activities" once the PID exists | Creative Commons Attribution (site states it; adaptable, but AXELOS marks are used under a permission of unstated scope, so this library describes structure in its own words rather than adapting the page's text directly) |
| NSW Health, *Project Brief Template for Projects Valued at Less than $10 million* (v3.0, 2010) | "This template is mandated for the development of project briefs for projects valued at less than $10 million"; "The Project Brief is in four Parts" | Not stated; qualifies the **heavyweight** sense of the name (below), not the one this bundle builds |
| Treasury Board of Canada Secretariat, *Guide to a Project Brief* | "a project brief must be appended to the Treasury Board submission"; "a project brief is to be supported by a business case, project charter and project management plan" | Not stated; also the heavyweight sense |
| UK Government Functional Standard GovS 002 v2.1, read via a third-party mirror because the official host returns 403 | "project brief:" (a glossary heading in Annex B) | Confirms the term is standardised in current UK government usage; its definition text could not be recovered this session and is not attributed to this source |

*(Corrected 2026-09-29, when the bundle was built: GovS 002 has no "project brief" entry in Annex B. The
build read [the standard's text](../../templates/project-brief/project-brief_research-log.md#what-the-checks-caught-and-what-was-not-read) end to end, and the
term is not among Annex B's defined terms. The one passage naming a brief is in the body, among the senior
responsible owner's accountabilities: the vision, justification and outcomes "are documented in a programme or
project brief". The row's conclusion stands, since the term is in current UK government use, but it is in
the body, not the glossary.)*

**Against this, PMI does not name "project brief."** The PMI *Lexicon of Project Management Terms*, version
5.0, the exact URL this task's research specified, was fetched and raw-checked: "project brief" is absent as a
case-insensitive substring across 80,417 extracted characters, while "Project Charter" and "Version 5.0" both
pass. The 2017 edition (v3.2), read from a third-party mirror and therefore corroboration rather than the
load-bearing source, lacks the term too. **The catalog's "PMBOK 7 (new)" methodology credit is unsupported by
either document**; the PMBOK 7 Standard's own paywalled body was not read, so an isolated mention there cannot
be ruled out, but nothing raw-checked supports the credit. PM² (v3.0 guide, 345,797 characters, raw-checked)
does not use the term either; its Initiating phase produces a Project Initiation Request, a Business Case and
a Project Charter as three separate named artefacts, none called a brief.

**The composition question, where two AXELOS-adjacent sources disagree, and the gap-fill this task specified
resolves in favour of caution.** The official AXELOS glossary itself names only "purpose, cost, time and
performance requirements, and constraints" as the brief's content; it does not itemise background, objectives,
risks or stakeholders as named sections, and its separate "start-up" entry lists "the outline Business Case,
Project Brief and Initiation Stage Plan" as three parallel outputs rather than nesting the business case
inside the brief. **The seven-item composition list this research otherwise leans on (background, objectives,
scope, constraints, risks, stakeholders, outline business case) is prince2.wiki's own synthesis, of an edition
the page does not state**, not the AXELOS glossary's wording. The build must attribute that list to prince2.wiki
by name, not to "PRINCE2" or "AXELOS" generically, and the companion must say plainly that the one official,
freely-readable AXELOS source is thinner than the practitioner synthesis the section design leans on. **The
one candidate that would have settled this, AXELOS's own Appendix A.19 product description in PRINCE2 Agile
2016, is unreachable**: its host, `publications.axelos.com`, no longer resolves at all, and no archived
snapshot exists. Record this as a closed research gap, not a further task.

**What was not read, stated as plainly as `issue-log`'s spec states it.** The PRINCE2 6th (2017) and 7th
(2023) edition manuals are behind a subscription and were not read; the one AXELOS glossary source read is the
2009 edition. The APM Body of Knowledge 7th edition is members-only and was read only as a boundary source (its
one usable quote is below), not as a composition source.

#### Boundaries with each named neighbour

**Not `business-case` (purpose settled; timing contested).** The purpose boundary is solid and already
adopted in this library's own text: the brief is "a short overview for starting up a project, not an
investment case" (`business-case_guide.md:17`). The **timing** boundary is not as clean as the earlier research
pass reported: PMStudyCircle's "the business case is created first, before the project is approved" describes
one order, but the BIS guide's "Approval of the Project Brief is the official start of the project" makes the
brief itself the trigger a business case might follow, not a document that only summarises a decision already
made. The companion must report this boundary as contested on timing and settled only on purpose (justify an
investment, versus define a project already approved to be started).

**Not a `project-charter`/PID (POSITION, where sources split three ways).** prince2.ca's named comparison:
"The main difference in purpose is that the approved Project Brief gives the project manager the authority and
resources to complete the work necessary for the Initiation Stage" and "does not give authorization to
complete the project activities" (sequenced, different authorization scope). Asana: "A project charter
formally authorizes a project and grants the project manager authority to allocate resources. A project brief
summarizes key details to align the team" (distinct, different authority, not sequenced). Smartsheet: "A
project brief is a simplified project charter" (same document, lighter weight). The APM Body of Knowledge lists
"problem statement", "project brief" and "project charter" as three interchangeable common-usage names for one
undifferentiated project rationale, the strongest evidence in this set that the name can collapse rather than
compete. **This library's own POSITION, stated because the sources do not settle it**: approval of a project
brief authorizes initiating, spending effort to find out whether and how to proceed; a project charter or PID
authorizes building. The companion states this as an adopted choice, not a reported fact. **`project-charter`
(catalog alias PID) inherits nothing from this ruling** and must pass ADR 0030's admission test on its own
evidence, per the method ADR 0049 already established for a sibling catalog category.

**Not a product brief or PRD (the weakest-evidenced boundary; label it as inferred).** No source read
contrasts "product brief" with "project brief" by name in one sentence. Productboard: a product brief "is a
foundational document that captures the essence of a product opportunity or initiative before teams commit to
building solutions", answering why to build a product; Storyflow frames a project brief as answering "what you
are doing and why" at the initiative level. The distinction (product-scope versus initiative-scope) must be
labeled inferred from triangulation, not cited as a settled contrast.

**Not a creative or design brief (clean).** SHERPA Global: the project brief is "the bird's-eye view of the IT
project"; the creative brief instead "defines how to best connect with the target audience by clarifying their
needs and motivations". Storyflow adds a structural claim: "The project brief is the parent document" and
"creative, design, and campaign briefs nest inside it".

**Not a project proposal or one-pager pitch.** Storyflow distinguishes the brief from a scope of work, "the
detailed, often contractual list of exactly what will be delivered", and separately states "A project brief is
a lightweight alignment document" that "defines what you are doing and why", where a plan "defines how and
when". A proposal or pitch document sells a decision not yet made; this bundle's brief documents one that
enough of a mandate already exists to start exploring (the sense the BIS trigger describes). The distinction
between a persuasive pitch and this library's brief is this library's own framing, not a single named source's
contrast, and the guide should say so.

**Not the Project Canvas (medium, not content).** Antonio Nieto-Rodriguez's named Project Canvas is "a one-page
template" with "14 dimensions", built because "project management methods have tended to be too complex to be
easily understood and applied by non-experts". No source treats a canvas as a synonym for a brief; they differ
in form, a diagram meant to be read at a glance versus prose in sections, not in what they cover.

**Not the NSW Health / Treasury Board of Canada heavyweight sense, named and put out of scope.** Two named
public-sector sources publish something also called "project brief" that is large, iterative and gate-adjacent:
options analysis, capital and recurrent cost estimates, a formal risk table, resubmission "at regular and
meaningful intervals throughout the life-cycle of the project" (TBS Canada). **This bundle builds the
PRINCE2/UK BIS sense: short, pre-project, superseded once initiation documentation exists.** The companion
must name the heavyweight sense explicitly as a different document under the same name, out of scope here, so
a reader who found this bundle searching for NSW Health's or TBS Canada's shape is told plainly they want a
different document, not that theirs does not exist.

#### Family fit: eight contracts exclude it as written; one admits it with strain

Every other family contract was tested against the type's own membership language and excludes it, several by
direct analogy to the already-shipped `business-case`:

| Family | Verdict | Why |
|---|---|---|
| `strategy-docs` | excludes | Names `business-case` as its own worked exclusion example, "a one-time, phase-bound artifact... this is why business-case is not a member" (`strategy-docs.md:32-36`); a project brief is at least as phase-bound |
| `delivery-docs` | excludes | Its five admitted verbs (define, decompose, verify, change, announce) describe acting on an already-agreed unit of work (`delivery-docs.md:11`); a brief precedes and scopes the project itself |
| `decision-docs` | excludes | "a technical decision-or-design artifact of the develop phase" (`decision-docs.md:11`); a brief is not a technical design record |
| `governance-docs` | excludes | Names `business-case` as its own worked exclusion, "an event-driven or phase-bound artifact (an incident postmortem, a business case) does not [belong], however operational it feels" (`governance-docs.md:23`) |
| `qa-docs` | excludes | "a verification artifact of the develop phase" (`qa-docs.md:12`); a brief plans nothing about verifying a product increment |
| `process-docs` | excludes | Its own contract text routes a forward-looking candidate away from itself: "discovery-docs before a decision, strategy-docs for direction, delivery-docs for the work itself" (`process-docs.md:23`) |
| `standing-standards` | excludes | "the output of a phase belongs to a phase family" (`standing-standards.md:37`); a brief is written once per project, not consulted repeatedly unchanged |
| `communication-docs` | excludes | "the document owns none of its own facts" is this family's defining property (`communication-docs.md:25`); a brief originates its own content and is not periodic |
| `discovery-docs` | admits, with strain | Its own membership test fits: "exists to decide whether to build something, before anyone commits to building it" (`discovery-docs.md:33`). The strain is the BIS "official start of the project" line, carried into ADR 0063's body as a named POSITION rather than smoothed over |

No fallback family exists on this evidence. If the maintainer's ruling to reopen were instead a ruling not to
build, there would be no other family this research found that admits the type; the record would read like
ADR 0035's, a legitimate negative outcome, not a search failure.

#### Structure and sections per size

**Sizes: `[lean, full]`, provisional, and full stays short.** Two sources that speak to length agree it should
stay brief: prince2.wiki's own quality bar is "short, focused" and "SMART"; Smartsheet, describing the
collapsed-with-charter camp, says "It should be a single page long, and anyone should be able to understand it
at a glance." BIS, the primary source, does not state a length. The one long confirmed example, NSW Health's
20-plus fields across three parts, is explicitly the heavyweight sense this bundle puts out of scope. **`full`
therefore does not mean heavier in the NSW Health/TBS Canada sense; it adds the two sections the lean variant
omits, and nothing about options analysis, cost breakdowns or procurement.** The contract permits `[lean]`
alone if the build's own research shows the second weight does not earn its place (`discovery-docs.md:89`);
this spec's judgment is that it does, because `Project Approach` and `Relationship to Other Documents` are
real, separately-named content the lean size would otherwise have to compress out entirely.

| Section | In lean | What it carries |
|---|---|---|
| **Background and Mandate** | yes | Where this came from and who asked for it: the mandate, "often as simple as an email" from a senior manager (BIS), that triggers Starting Up a Project and is expanded into the brief (prince2.wiki: created "during the starting up a project process") |
| **Objectives** | yes | What the project must achieve, stated so a reader can tell later whether it did. BIS's own checklist: "Objectives - achievable and measurable (SMART)"; prince2.wiki confirms SMART as the brief's own quality bar |
| **Scope and Exclusions** | yes | What is in, and, named as its own field, what is explicitly out: BIS's checklist item "Scope - what in and what's out", and WorksBuddy's finding that the exclusions half is "the section that most teams skip" and the one that "prevents the most expensive misunderstandings." **A named, mandatory field, not folded into a general scope paragraph** |
| **Outline Business Justification** | yes | Why this is worth doing, in outline only, plus a statement that a fuller comparison of options (including doing nothing) will be brought to a named approval gate by a `business-case` document. Sourced to prince2.wiki's "outline business case" as one brief component; bounded by `business-case_guide.md:17`, which this section must not cross into |
| **Constraints and Who Should Be Involved** | yes | Known constraints on the work, and the people who need to be part of it, sourced to BIS's own sentence, "the Project Brief says why the project is needed, what it must achieve and who should be involved." **Not** sourced to a "project management team structure" component: that phrase failed raw-text verification against prince2.wiki and is not confirmed as a stated part of the brief by any source read this session |
| **Decision Requested** | yes | What approval is being asked for, from whom, and what happens to the answer: proceed to develop the business case, proceed to initiation, or stop. One named approver. **POSITION**: this section exists because the family's contract obliges each member to say which document takes over (`discovery-docs.md:49-51`), not because a named source specifies this as a brief component |
| **Project Approach** | full only | How the work will be approached (build, buy, or a mix). Named as a brief component by prince2.wiki; not elaborated in any source read this session, so the guidance text here is labeled this library's own, not attributed to PRINCE2 |
| **Relationship to Other Documents** | full only | Where this document sits against the mandate, the business case, and initiation documentation (a project charter or PID), naming plainly that neither `project-charter` nor a PID is built in this library. **POSITION**: this section is how the template answers the same contract obligation (`discovery-docs.md:49-51`) at the size that has room for it, not a sourced composition item |

*(Corrected 2026-09-29, when the bundle was built. Five points in this table were settled otherwise by the
build's research, each recorded with its quotations in the
[research log](../../templates/project-brief/project-brief_research-log.md#what-the-checks-caught-and-what-was-not-read):
(1) "project management team structure" is verbatim on prince2.wiki's starting-up page, though absent from
its project brief page, so Constraints and Who Should Be Involved may cite it there;
(2) Decision Requested and Project Approach are sourced, not only the library's position, because the
starting-up page makes the request to initiate the process's final output and names "the project approach",
and Oxford City Council's and Bestoutcome's templates carry both an approvals block and an approach section;
(3) the BIS items this table quotes for Objectives and Scope come from BIS's start-up checklist, not from its
list of the brief's contents;
(4) WorksBuddy's "the section that most teams skip" is an assertion on a vendor page, not a finding, and the
bundle does not repeat it as fact;
(5) an outline estimate of time and cost is adopted inside Outline Business Justification, labelled
illustrative, because the AXELOS definition and both BIS lists name time and cost. Costed estimates stay out,
as below. Options analysis also stays out, but as this library's position rather than a gap in the sources,
since Oxford City Council's template has a "Project Options" section of its own.)*

**What stays out at any size, named so a reader is not left to guess:** options analysis, capital or recurrent
cost estimates, a formal risk-scoring table, and resubmission across the project lifecycle. Those are the
NSW Health / Treasury Board of Canada heavyweight sense, out of scope by the design choice above, and the
companion says so rather than leaving the omission silent.

#### Metadata

| Field | Value | Why |
|---|---|---|
| `family` | `discovery-docs` | ADR 0063, reopening the family at its own membership test |
| `phase` | `discover` | The only value the contract allows; a project brief precedes commitment, like both existing members |
| `sizes_available` | `[lean, full]` **provisional** | Reasoned above; the contract allows `[lean]` alone if the build's own research disagrees |
| `status` | `beta` | Every bundle |
| `methodology` | `PRINCE2` | The one methodology this research confirmed by an official-tier source (the archived AXELOS glossary); the catalog's `PMBOK 7 (new)` is corrected below |
| `pairs_with` | `[]` | Checked against pm-skills `origin/main` with the direct-contents call on 2026-09-27 (68 skills returned). Two near-name matches were read and ruled out: `foundation-meeting-brief` (a private meeting-prep document, not a project-initiation document) and `develop-solution-brief` (a technical-solution pitch at `phase: develop`). No pairing exists |
| `related_templates` | `[business-case, user-persona]` **provisional** | The sibling whose outline it absorbs and already cites by name, and the family's other member. `project-charter` is deliberately not listed: it is not built and this ruling does not admit it by inheritance |
| `aliases` | `lightweight charter` and `project one-pager` kept, both flagged | "Lightweight charter" encodes the Smartsheet "simplified charter" camp as settled fact when the strongest sources (PRINCE2, BIS) describe a per-project pre-initiation product regardless of size, not a small-project variant; the critic named this as a maintainer-review flag, not a rewrite performed here. "Project one-pager" is what a reader wanting a persuasive pitch or proposal types, the boundary this spec draws above; a build decision, not resolved here |

#### Catalog corrections the landing PR must make

Per [procedure 1](decision-procedures.md#1-a-catalog-call-loses-to-research), both `docs/internal/catalog.md`
(entry 71) and `atlas/catalog-data.json` (`id: "project-brief"`), then the regenerated atlas:

1. **`methodology`: "PMBOK 7 (new)" is unsupported and must be replaced or dropped.** The PMI Lexicon, versions
   5.0 (the exact URL specified) and 3.2, were both raw-checked to lack the term entirely while both define
   "Project Charter." PRINCE2 is the methodology this research actually confirmed; correct the field to
   `PRINCE2`.
2. **`purpose`/`formality` flagged, not rewritten here.** "Lightweight project definition for smaller efforts"
   and the relationship note "S variant of Charter" encode only the Smartsheet/NSW-Tasmania reading (a brief
   as a smaller charter scaled to project size). The strongest-evidenced sources describe a per-project,
   pre-initiation product used regardless of size. Flag for the maintainer's read at landing; do not silently
   rewrite a catalog row this record did not adopt a final wording for.
3. **`relationships`** currently reads `[Charter]` alone. Add `Business Case`, since the type's own admission
   evidence (the shipped `business-case` bundle's boundary text) is a stronger, closer relationship than the
   unbuilt charter.
4. **`built`, `state`, `state_note`** flip only when the bundle itself lands; this record specs and reopens the
   family, and does not build.

#### `pairs_with`: no pairing exists

`gh api repos/product-on-purpose/pm-skills/contents/skills --jq '.[].name'`, run 2026-09-27, returned 68 skill
names. None is `project-brief` or a plausible variant. Two names containing "brief" were read in full and
ruled out: `foundation-meeting-brief` (a private, pre-meeting tactical document, never shared with attendees)
and `develop-solution-brief` (a technical-solution pitch document at `phase: develop`, bridging problem
understanding to detailed specification). `tool-design-sprint-brief` and `tool-foundation-sprint-brief` were
not read in full, since their names alone place them as sprint-kickoff briefs scoped to a five-day exercise
rather than a whole project, the same neighbouring-artifact pattern ADR 0035 found for `prototype-brief`
candidates. `pairs_with: []` is the honest declaration.

#### Risks for the build and review

1. **The composition attribution is this spec's main correctness risk.** The section design above leans on
   prince2.wiki's seven-item list, not the thinner official AXELOS wording. A build or review that quietly
   upgrades "prince2.wiki says" into "PRINCE2 says" throughout the companion reintroduces exactly the defect
   this section works to avoid. Every Anatomy subsection must name its actual source (prince2.wiki, BIS, or
   POSITION), not "PRINCE2" generically.
2. **The family-reopening question is a maintainer decision this spec presents, not one it resolves.** The
   2026-09-27 ruling settles it for this run, but the ADR must state the strain (BIS's "official start of the
   project") in its own body, not in a footnote, so a future reader does not find the closure re-asserted
   without the reason it was lifted.
3. **`project-charter` sits in the same catalog category and shares this type's purpose.** Any research run
   for it will be tempted to inherit this ruling's family-fit reasoning wholesale. Per ADR 0049's own method,
   it must be tested on its own admission evidence; this record settles nothing for it.
4. **The AXELOS glossary is 2009-edition and all-rights-reserved.** The companion may quote it briefly (as
   this spec does) but must not adapt its wording into template guidance text; BIS, Crown copyright under the
   Open Government Licence, is the adaptable source for anything beyond a short quote.
5. **The build workflow's templates stage has repeatedly copied the worked example's own scenario into GOOD
   and WEAK illustrative text**, a defect no lens currently catches on its own: `tier2-specs.md:1433-1435`
   records that on `change-request`, "the main loop found two more that no lens flagged, the templates' GOOD
   examples reusing the example's scenario and the example repeating the thread's known sharing contradiction."
   This bundle's example uses Acme Analytics' Question-First Entry initiative; the GOOD and WEAK text in every
   guidance comment must use a scenario that is **not** that initiative, checked by grepping the template for
   the example's own nouns (`Dana Okoro`, `Priya Nair`, `Question-First Entry`, `Meridian Freight`) before the
   review closes.
6. **No pm-skills pairing exists, and none is expected to appear.** Not a blocker, but the bundle gains no
   cross-repository routing benefit from being built, unlike `issue-log` and `change-request`.

#### What landing this bundle closes elsewhere

1. **The `discovery-docs` contract moved to `0.2.0` in the spec PR**, with ADR 0063, and every place that said
   the family was closed or complete at two got a dated correction there. The landing PR changes the Members
   line from "not yet built" to the build date.
2. **`business-case`'s boundary text needs no edit; its worked-example callout does.**
   `business-case_guide.md:17`, `business-case_companion.md:315-317` and both templates' "NOT a project brief"
   lines already state the boundary this bundle must agree with, and the new companion agrees with them rather
   than restating the boundary differently. But `business-case_example.md:16-18`'s callout, "ahead of
   everything except its sibling user persona and the product vision it builds on," becomes false once this
   example exists (see the example section's contradiction 6, below), and needs a one-line dated correction in
   the same change.
3. **`project-charter`'s eventual research owes ADR 0049's method**, testing its own admission evidence rather
   than inheriting this ruling by catalog-category proximity.
4. **The catalog entry**, per procedure 1 above: both `docs/internal/catalog.md` and `atlas/catalog-data.json`,
   then the regenerated atlas, when the bundle lands.
5. **This page's Progress table.**

#### The example

**A project brief for the Question-First Entry and Modelling Defaults initiative**, dated **2026-01-16**:
two days after the [product vision](../../templates/product-vision/product-vision_example.md) (agreed 2026-01-14) and four
days before the [business case](../../templates/business-case/business-case_example.md) (dated 2026-01-20). This keeps the
family's chronology obligation: the example must precede what it leads to (the business case's own funding
decision, and any future initiation documentation) and must not cite either as existing. It sits after the
[user persona](../../templates/user-persona/user-persona_example.md) (2026-01-05), which itself claims only to sit "ahead
of even the product vision" (`user-persona_example.md:18`); this brief's later date does not disturb that
claim. `README.md:223` separately calls the persona "the earliest document in the library", a stronger,
published claim this date also respects.

**Facts it reads, by file and line, and nothing it must not.** From `business-case_example.md`: the sponsor,
Dana Okoro, VP Product (line 4); the telemetry the brief's Background section shares with the case, that "only
31 percent build a second dashboard view within 14 days of signup" and that "revenue per new account has been
flat for five quarters" (lines 34, 41), both Acme's own pre-existing telemetry rather than an output of the
case itself; and the December leadership review that supplies the brief's mandate, "the flat revenue-per-account
trend surfaced at the December leadership review and finance asked for a funding decision" (line 52-53). From
`user-persona_example.md`: the Recurring Analyst (lines 43-47) as the segment this initiative serves, and
Priya Nair, PM, Reporting (line 6), as this brief's named Project Manager.

**What it must not cite or contain, because doing so would contradict an already-shipped sibling.**

1. **No staged case vocabulary.** `business-case_example.md:5` states plainly, "Acme has no staged case model
   (no SOC/OBC/FBC)". The Outline Business Justification section must not call itself an SOC, OBC or FBC.
2. **No Reporting Platform Modernization program, and no Marta Reyes.** That program and its program manager
   are a mid-2026 fact of the delivery-docs and governance-docs thread (`change-request_example.md:8`,
   `issue-log`'s ISS-11 raised 2026-06-14), five months after this brief's date. The brief uses `business-case`'s
   own investment name, "Question-First Entry and Modelling Defaults," as its project name.
3. **No pre-computed benefit range or financial metrics.** The 6-11 percentage point second-view lift, the
   NPV, IRR, payback and ROI figures (`business-case_example.md:78-102`) are the business case's own later
   analysis. The brief may cite the early prototype's 71 percent question-resolution finding as an existing
   fact (it predates the case, per the case's own framing), but must not anticipate the case's computed
   benefit range or financial metrics.
   *(Corrected 2026-09-29, when the bundle was built: the allowance for the 71 percent figure is withdrawn,
   and the example does not cite it. No sibling dates the prototype, and every document that reports the
   figure is dated after this brief, so it could not be shown to predate the brief.)*
4. **No options decision.** The brief defers the comparison of options, including doing nothing, to the
   business case; it must not commit to OPT-3 or name it, since choosing between options is exactly the job
   `business-case_guide.md:17` reserves for the other document.
5. **No initiation documentation, project charter or PID cited as existing.** None is built in this library.
6. **A sibling's own worked-example callout becomes false the day this bundle lands, and that is a correction
   this landing owes, not a constraint on the new example.** `business-case_example.md:16-18` states the case
   "sits near the start of the shared timeline, ahead of everything except its sibling user persona and the
   product vision it builds on." A brief dated 2026-01-16 makes that sentence false the moment it ships. The
   landing PR must add a one-line dated correction to that callout, the same pattern already used for
   `README.md:223`'s "earliest document" claim once a still-earlier document exists. *(Done 2026-09-29: the callout,
   now `business-case_example.md:16-20`, carries that correction.)*

**Decision requested, closing the loop honestly.** The brief asks Dana Okoro, as executive, to authorize
proceeding to a funding decision, to be brought to the leadership review on 2026-01-26, the same date
`business-case_example.md:118` already names. The brief's own "what happens to the answer" is exactly that
business case, arriving four days later: nothing here is invented for the brief to hand off to.
