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
spend.
