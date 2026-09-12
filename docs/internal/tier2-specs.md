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
> schedules anything. What a spec does is make the judgment reviewable *before* 700K to 1M tokens are spent
> executing it.

## Progress

| Type | Catalog id | Family | Spec | Built |
|---|---|---|---|---|
| `spike-report` | `spike-research-spike-report` | `decision-docs` | **Written 2026-09-11** | No |
| `project-milestone-retrospective` | `project-milestone-retrospective` | `process-docs` | **Written 2026-09-11** | No |
| `pi-release-retrospective` | `pi-release-retrospective` | `process-docs` | **Written 2026-09-11** | No |
| `test-summary-report` | `test-report-test-summary-report` | `qa-docs` | **Written 2026-09-11** | No |

**Not specced, deliberately.** `launch-coordination-checklist` is promised by a `future:launch-checklist` tag
in `release-notes_meta.yaml` and has a pm-skills pairing candidate, but its catalog category straddles two
families (`release-notes` is `delivery-docs`, `runbook` is `standing-standards`) and **a family assignment
is not a spec-writer's call**. `solution-brief` is promised **twice** - `prd_meta.yaml` and `rfc_meta.yaml`
both carry `future:solution-brief` - and **has no catalog entry at all**, so it has not passed
[ADR 0030](decisions/0030-templating-scope-markdown-documents.md)'s admission test and cannot be specced
either. Both wait on a maintainer decision, and both are recorded here so the gap is visible rather than
forgotten.

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

**Open, and only research can close it: [ADR 0030](decisions/0030-templating-scope-markdown-documents.md)'s
admission test.** A candidate type is templatable only when **a named source publishes it as a written
document**. A catalog entry is necessary and not sufficient - `prototype-brief` had one and failed
([ADR 0035](decisions/0035-prototype-brief-fails-the-admission-test.md)), closing `discovery-docs` at two
members. **So this bundle ships only if its own research pass finds that source, and the honest outcome of
this spec is allowed to be that it does not ship.** The candidate's favourable prior is XP's own
literature, where a spike is a named, documented practice rather than a folk term, but a prior is not a
retrieval.

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

#### Metadata

| Field | Value | Why |
|---|---|---|
| `family` | `decision-docs` | ADR 0022 |
| `phase` | `develop` | Contract-gated; matches all three existing members |
| `sizes_available` | `[lean]` | Catalog `size_variant: S`. The contract admits `[lean]` for a single-size type, and exempts it from nesting, not from anything else |
| `status` | `beta` | Contract: `beta` until one real usage cycle is recorded. Nothing in this library has one |
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
