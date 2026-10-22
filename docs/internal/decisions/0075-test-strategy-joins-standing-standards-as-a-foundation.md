---
status: accepted
date: 2026-10-19
decision-makers: [jprisant]
consulted: [claude]
---

# `test-strategy` joins `standing-standards` as a `foundation`, its seventh member and third unforecast one

## TL;DR

- **Decision.** The `test-strategy` bundle (catalog id `test-strategy`; issue #260, bundle: test-strategy)
  declares **`family: standing-standards`** and **`classification: foundation`**. It becomes that family's
  seventh member, beside `definition-of-done` (`foundation`), `runbook` (`tool`),
  `launch-coordination-checklist` (`tool`), `definition-of-ready` (`foundation`),
  `production-readiness-review` (`tool`) and `business-continuity-plan` (`tool`), and the
  [contract](../contracts/standing-standards.md) moves to `0.6.0`.
- **Scope, settled by the maintainer and not reopened here.** This is the standing document for an
  organization or program, "a standing strategy used across more than one project" (the maintainer's own
  words, 2026-10-15), never a portfolio and never the per-project sense `test-plan` already ships. A
  2026-10-15 follow-up found no source scoping a test strategy to a portfolio, and found the per-project
  sense already shipped inside `test-plan`'s own Test Levels and Types section and its `test_strategy_ref`
  field.
- **Why a record is needed.** Like `production-readiness-review` (ADR 0062) and `business-continuity-plan`
  (ADR 0071), this type was never named on the contract's "likely future members" list
  (`standing-standards.md:46`). It is the family's third member admitted purely on the membership test and
  falsifier, with no forecast to confirm. **A second reason, specific to this candidate:** the contract's
  own membership clause never states an organization-wide scope, so the maintainer's organization-or-program
  ruling interprets that silence rather than widening an exclusion. That is a different shape from ADR 0071,
  where no comparable scope ambiguity existed inside the contract's own words.
- **What settled membership:** the family's own falsifier, the same test ADR 0053, ADR 0062 and ADR 0071
  each applied. A standing test strategy that one or more projects inherit from, and that each project's
  own test plan either follows or states a reasoned deviation from, is consulted at the moment each of
  those plans is written.
- **What settled classification:** the contract's section 2 cut, "is it a standard you judge against, or an
  instrument you execute?" Argued marker by marker below, on the same reasoning ADR 0058, ADR 0062 and ADR
  0071 each used.
- **A consequence this record keeps rather than resolves by amendment: the cadence tension.** Section 1 of
  the contract says members are "not revised on a calendar." Two sources describe a test strategy as itself
  periodically revised; a third says it will not change once approved. This ADR records the tension and
  routes it to the bundle's own Review Trigger section, the same move ADR 0071 made for
  `business-continuity-plan`.
- **Status:** proposed 2026-10-19, drafted 2026-10-16, **accepted 2026-10-19 on the maintainer's
  delegation**. This record, the spec, and the contract diff were offered for the maintainer's own read,
  per the standing rule that every contract edit is read before it is merged. Told that the PR amends two
  family contracts and that nothing would merge before the read, the maintainer directed a merge on the
  agent's best judgment. That direction stands in for the read for this PR only, as similar ones did for
  [ADR 0070](0070-north-star-metrics-joins-strategy-docs-as-a-fifth-member.md) and
  [ADR 0078](0078-maps-canvases-and-session-records-are-templatable-through-their-written-form.md).
  The standing rule is not repealed. **The contract diff was accepted without a read.** The family and the
  scope are the maintainer's own rulings of 2026-10-13 and 2026-10-15; the `foundation` classification is
  argued here, not ruled. The maintainer has not yet confirmed this delegated acceptance, and may reopen
  the record for a read.

## Context and Problem Statement

The 2026-10-12 admission sweep of five queued candidates tested `test-strategy` against its admission
evidence and against all ten family contracts, on both axes. Unlike the other four candidates in that
sweep, it ran only two of the usual three research dimensions; the dedicated named-sources admission
dimension never ran. A 2026-10-14 follow-up ran it. Three independent sources clear admission: ISTQB's own
glossary (read via an unofficial mirror, `istqb-glossary.page`, which serves identical text under both its
"test strategy" and "organizational test strategy" entries), Process Street's own "Test Strategy Document
Template" (four of its spans independently re-checked and passing), and Wikipedia's secondary account of
ISO/IEC/IEEE 29119's Part 3 structure, which names "Organizational Test Strategy" and "Test Plan (including
a Test Strategy)" as separate outputs. The standard's own current clause text was never reached by any
automated fetch in either research dimension, a finding the 2026-10-14 critic states directly, so this
record and the spec it accompanies never cite ISO/IEC/IEEE 29119-3's own words, only secondary accounts of
it, labelled as such. *(2026-10-20: the build read ISTQB's official glossary through the API behind its page. Its definition is "A strategy that describes the generic requirements for testing and how to perform testing within an organization.", with no program wording, so the text this record reads via the mirror is the mirror's older wording, not ISTQB's current one. Admission still stands, now on the official definition and on the published strategies the build read in raw text. The research log is [`test-strategy_research-log.md`](../../../templates/test-strategy/test-strategy_research-log.md).)*

A second, harder question followed admission: at what scope is this type standing? The 2026-10-12 sweep's
own family-fit critic found the question undecidable from the evidence gathered to that point. Strong,
direct, mostly primary evidence places a test strategy at program scope: Ofgem's two Switching Programme
testing-strategy documents, and Transport for London's Schedule 4 procurement contract, which requires a
supplier to "prepare and submit to TTL a Test Strategy." Evidence for a whole-organization reading is real
but thinner and more secondary: Wikipedia's account of the standard, a 2009 academic slide deck describing
a then-draft of the standard, a vendor guide asserting organization-wide scope without demonstrating an
instance, and one unpublished claim in an HMRC blog post. The critic also found that `standing-standards.md`
section 1's own membership clause, "agreed once and applied every time... consulted repeatedly without
being rewritten," never says "the whole organization," so reading it as organization-wide-only is a gloss
layered on top of the contract's text, not something the text itself requires.

The maintainer ruled on this scope question on 2026-10-15, after a dedicated terminology follow-up: the
test strategy is scoped to "an organization or program, a standing strategy used across more than one
project." That follow-up also closed a live question the maintainer had raised, whether "portfolio" should
replace "program": no source checked scopes a test-strategy document itself to a portfolio, and PMI's and
APM's own definitions place a portfolio above a programme, as a collection whose components "may not
necessarily be interdependent or directly related," which would have widened this bundle's scope beyond
what the maintainer described wanting.

This record exists to make the family and classification calls reviewable rather than asserted, the way
ADR 0062 and ADR 0071 each did for their own members. That is because
[ADR 0032](0032-adopt-standing-standards-family-contract.md) and check K can verify only that a member
picked a value from the set `{foundation, tool}`. They cannot verify that it picked the right one.

## Decision Drivers

- The classification must follow what the document does, per the contract's own cut, not what its strongest
  admission quotation sounds like out of context. That is the same caution ADR 0062 and ADR 0071 each
  named for their own members.
- Family membership (the falsifier) and classification (the cut) are two different questions.
  [ADR 0058](0058-definition-of-ready-joins-standing-standards-as-a-foundation.md) already warns that
  conflating them is the easiest way to get a member wrong.
- This is the family's third member with no forecast to confirm. The admission argument must rest on the
  membership test as written, per
  [ADR 0057](0057-issue-log-joins-governance-docs-as-a-fourth-member.md)'s principle that the membership
  test, not a list of members once predicted, governs a candidate.
- The scope question is a reading of the contract's own silence, not a new fact about the world the
  contract asserts, so it does not trigger
  [decision-procedures.md procedure 11](../decision-procedures.md#11-a-family-contract-asserts-something-about-the-world)
  the way a contract's own factual claim would. It is recorded here because a future reader should see the
  scope ruling was reasoned through the contract's actual words, not assumed from the sitting's first,
  narrower framing.
- The research surfaced a cadence tension: two sources describing periodic revision against section 1's
  "not revised on a calendar." That tension needs an explicit answer rather than a silent pass, the same
  posture ADR 0071 took for `business-continuity-plan`.

## Considered Options

1. **`standing-standards`, `classification: foundation`.** Chosen.
2. **`standing-standards`, `classification: tool`.** The case for it: Ofgem's own language shows the
   strategy used "by all parties" within a programme, which could read as executed by people other than its
   authors, part of the `tool` marker's authorship half. Rejected below: the stronger half of that marker,
   execution under time pressure, is not met, and the document's own change cadence argues the other way.
3. **`qa-docs`.** The case for it: testing is this type's entire subject, and `qa-docs` is the family built
   for testing documents. Rejected: that contract's own membership clause requires a type to "plan, specify,
   or report the verification of a product increment" and to be "produced at a stage and finished." An
   organization-or-program-level strategy is none of these; it is consulted by many increments across more
   than one project and finishes at none of them. The research scored this reading a clean `excludes`
   against `qa-docs`, with no strain needed to reach that verdict.
4. **Decline, per the ADR 0049 shape.** Rejected on the evidence: three independent named sources,
   corroborated by a dedicated follow-up dimension, clear ADR 0030's admission test several times over.
5. **Scope the bundle to the organization only, or widen it to the portfolio.** Neither is this ADR's call
   to reopen. The maintainer ruled organization-or-program on 2026-10-15, after the portfolio question was
   checked and closed. Recorded here as options this ADR does not revisit.

## Decision Outcome

**Chosen: `standing-standards` with `classification: foundation`.**

### Why the family question tracks the falsifier, not the forecast

Read as a standing strategy, consulted whenever a project in its scope writes or revises its own test plan,
this type passes the same falsifier ADR 0053, ADR 0062 and ADR 0071 each applied: "if a candidate arrives
that matches the cadence but is not consulted at the moment of action, this family has been drawn around
the axis rather than around a job" (`standing-standards.md:108-110`). Ofgem's own passing language states
the inheritance relationship directly: "This testing strategy will be followed by a more detailed programme
level Testing Management Plan," and a companion Ofgem document adds that "a detailed, programme level
Testing Management Plan should be developed... to define the detailed testing approach for each test
phase." Read as a one-time record written for one project after that project's own testing ended, with no
further project ever consulting it, the type excludes on the contract's own analogy at
`standing-standards.md:37`: "a runbook written for one incident is an incident report." **This bundle is
the standing strategy**, and a filled instance that served only one project's own plan is a different,
narrower artefact this bundle does not template.

### Why `foundation`, marker by marker, against the honest `tool` case

The contract gives each value three markers (`standing-standards.md:80-85`). ADR 0062's and ADR 0071's own
tables are the model this ADR follows rather than picking the convenient row:

| Marker | `foundation` | `tool` | A test strategy for an organization or program |
|---|---|---|---|
| What it is | "a standard you are judged against" | "an instrument you execute" | The levels, types, tools and governance every project in scope inherits or states a reasoned deviation from. Software Testing Help's own passing quote reads this way directly: "Test strategy usually will not change once approved" |
| When and by whom | "argued to, agreed by a team, and changed deliberately and rarely" | "usually under time pressure and often by someone who did not write it" | Agreed at the organization-or-program level, by the team or role that owns testing across its projects, then applied by every project team in scope. ISTQB's own worked example (passed) shows this cadence: "An organization that develops and maintains an e-commerce platform defines a test strategy stating that all projects will perform component, integration, system, and acceptance testing." Nobody applies it under time pressure; applying it is simply writing the next project's own test plan |
| Where authority comes from | "from having been agreed" | "from being correct right now" | From having been agreed at the organization-or-program level and inherited by every project in scope, the same register `definition-of-done`'s own admission language uses, not from being correct at the moment a disruption or a launch is underway |

**The honest `tool` case, stated rather than hidden.** Ofgem's own language states the strategy is "for use
within the programme by all parties," which could be read as execution by people other than its authors,
the authorship half of the `tool` marker. **What breaks the parallel is the timing half.** A business
continuity plan and a production readiness review are both executed under time pressure, once a disruption
is declared or a handoff is underway. A test strategy is not executed under any comparable pressure: a
project team consults it, or deviates from it with a stated reason, in the ordinary course of writing its
own test plan, which is itself a document authored well before any release. That reading is this library's
own inference by analogy with the contract's markers: no research dimension tested when or under what
pressure a test strategy is applied. The `foundation` call rests on the
timing half failing to support `tool`, and on the strategy's own change cadence, which Software Testing
Help's passing quote states directly, reading closer to `definition-of-done`'s "changed deliberately and
rarely" than to a runbook's or a continuity plan's activation-under-pressure pattern.

### Why not `qa-docs`, in that contract's own words

`qa-docs.md` section 1 admits a type whose job is to "plan, specify, or report the verification of a product
increment." Section 2 states the phase case instrument by instrument: "A test plan is written per release
and closed at its exit criteria; a test case is authored once for one behavior; a bug report is opened,
triaged, and closed. Each is produced at a stage and finished, which is the definition of a phase artifact."
An organization-or-program-level test strategy, the sense this bundle builds, is none of these: it is not
written per increment, is not closed at any one release's exit criteria, and is not finished at a stage.
The 2026-10-12 research scored this reading a clean `excludes` against `qa-docs`, with no strain needed to
reach that verdict, a cleaner exclusion than the per-project sense drew from the same contract (which the
research scored `admits-with-strain`, a reading this bundle does not build and this ADR does not revisit).

### The scope ruling, and why this record differs from ADR 0071 in one respect

`standing-standards.md` section 1's membership clause reads, in full: "A bundle belongs to this family when
its document type is agreed once and applied every time. Not written per increment, not revised on a
calendar, not the output of a phase: written when the team decides how it will work, and then consulted
repeatedly without being rewritten." Nowhere does this clause say "the whole organization." The maintainer's
organization-or-program ruling of 2026-10-15 reads a clause that was always open to a program-scoped
reading, rather than widening a clause that had excluded one. **This is the one respect in which this
admission's reasoning differs from ADR 0071's own**, where no comparable scope ambiguity existed inside the
contract's own words for `business-continuity-plan`. Both records exist for the same underlying reason, an
unforecast member whose classification has to be argued rather than inherited from a forecast; this record
additionally had to settle, with the maintainer, what the contract's silence on scope actually permits.

### The cadence tension, recorded as a consequence rather than resolved by amendment

`standing-standards.md` section 1 states members are "not revised on a calendar." TestRail's own passing
language describes the type as "a long-term document that evolves with the organization's needs and
growth," and ReqTest's own passing language states "the test strategy is a living document and evolves over
time." Software Testing Help's own passing language cuts the other way: "Test strategy usually will not
change once approved." All three spans passed the recheck.

**This ADR does not widen the contract to accommodate the tension.** The contract-mandated Review Trigger
section, required of every member by section 4, already asks each member to name a condition rather than a
date. This bundle's own Review Trigger section names conditions drawn from the sources above: a project's
own test plan recording a deviation in its `test_strategy_ref` field or its Risk-Ranked Approach section; a
change to the organizational or program test policy this strategy is aligned with; a test summary report
showing a strategy-mandated level or type was skipped; or a new test level, tool or environment adopted
across more than one project without the strategy being revised to say so. Reading TestRail's and ReqTest's
"evolves" language as a description of this condition-driven process, rather than as a calendar rewrite, is
consistent with Software Testing Help's own "will not change once approved" and does not need a contract
amendment to resolve. **The tension is recorded here, as a consequence of admitting this member, not argued
away.**

### The counter-argument this record keeps rather than omits

**No contract's forecast list named this type.** `standing-standards.md:46` names only "a coding-standards
or engineering-handbook document." A reader who expects family assignment to track a contract's own
predictions would find nothing here to point to, the same gap ADR 0062 and ADR 0071 each recorded for their
own members. It does not change the outcome, for the reason ADR 0057 gives: the membership test, not the
forecast list, governs a candidate.

**A second counter-argument, specific to this candidate: ISTQB's own current (2024) advanced syllabus hints
the standard it teaches toward may have renamed the organization-level artefact.** It states the
organization-level construct is "referred to as an "organizational test practice"" in the standard, which,
if that is the current standard's own wording, would mean the strongest organization-level sources behind
this admission (Wikipedia's secondary account, and a 2009 academic slide deck on a then-draft of the
standard) describe a name the current standard may have dropped. This record does not resolve that
question: no automated fetch in either research dimension reached the current standard's own clause text.
If a later reader does reach it and finds the rename confirmed, the admission case for the organization-wide
half of ISTQB's own hedge would need revisiting, though the program-scope evidence (Ofgem, TfL), which
carries none of this risk, would be untouched. *(2026-10-20: the "hedge" this paragraph calls ISTQB's own is the unofficial mirror's older text; ISTQB's current glossary says "within an organization" and nothing about a program. The program-scope evidence is now wider than Ofgem and TfL: the build also read DCC's joint test strategy and the Fujitsu and Post Office HNG-X testing strategy in raw text. The rename question stays open: one syllabus sentence says 29119-3 calls the artefact an "organizational test practice", and the standard was not retrieved.)*

### Consequences

- `standing-standards` grows from six members to seven. Its contract's Members line and change note are
  updated in this change, moving to `0.6.0`. That follows the contract's own requirement that a change to
  itself carry a decision record.
- Check K gates `classification` membership of the set `{foundation, tool}` and cannot verify this member
  picked the right value. That stays a review obligation. The marker-by-marker argument above is the
  standard this member is reviewed against.
- **The cadence tension is a standing consequence of this admission, not a resolved question.** A future
  reader of the contract should expect the Review Trigger section, not a contract amendment, to be where
  this tension is answered, the same expectation ADR 0071 set for `business-continuity-plan`.
- **The scope ruling is a standing interpretation of the contract's silence, not an amendment of its text.**
  A future candidate whose own cadence matches this family but whose scope sits below "program," at a single
  team or a single project, is not pre-admitted by this ruling; this ADR settles only that "organization or
  program" is within the clause's existing reach, nothing narrower or wider.
- **The classification rests on the timing marker, not the authorship marker.** If a later reader finds that
  applying a test strategy is in practice time-pressured in some context this research did not surface, the
  `tool` case gets stronger. This record is where to reopen it.
- `tier2-specs.md` records this type as specced. The maintainer's read of this ADR, the spec and the
  contract diff together decides whether the build proceeds, per
  [ADR 0041](0041-maintainer-preference-sets-the-build-order.md)'s rule that the maintainer's preference
  sets the build order.

## More Information

- Family contract: [`standing-standards`](../contracts/standing-standards.md), adopted by
  [ADR 0032](0032-adopt-standing-standards-family-contract.md).
- The classification precedent this follows most closely, on both membership and classification:
  [ADR 0062](0062-production-readiness-review-joins-standing-standards-as-a-tool.md) and
  [ADR 0071](0071-business-continuity-plan-joins-standing-standards-as-a-tool.md) (`tool`, the family's
  first and second unforecast members). The classification precedent on the `foundation` side:
  [ADR 0058](0058-definition-of-ready-joins-standing-standards-as-a-foundation.md).
- The family it does not join: [`qa-docs`](../contracts/qa-docs.md), adopted by
  [ADR 0026](0026-adopt-qa-docs-family-contract.md).
- The refusal-record shape considered and not used:
  [ADR 0049 (pi-release-retrospective fails the admission test)](0049-pi-release-retrospective-fails-the-admission-test.md).
- The admission standard for new types:
  [ADR 0030 (templating scope: markdown documents)](0030-templating-scope-markdown-documents.md), and
  [ADR 0048 (one named source clears the admission test)](0048-one-named-source-clears-the-admission-test.md).
- The sibling bundle this type hands off to: [`test-plan`](../../../templates/test-plan/test-plan_guide.md),
  whose own `test_strategy_ref` field and routing table already name this type as a standing document the
  library had not yet built.
- Where the spec, the admission case in full, the scope ruling, and the section design live:
  [`tier2-specs.md`](../tier2-specs.md).
