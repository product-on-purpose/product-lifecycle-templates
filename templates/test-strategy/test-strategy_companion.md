# Companion: The Test Strategy

> The deep explainer for the test-strategy bundle. Read this to understand what a standing test strategy
> is, how its sources describe it, and where they disagree about its scope, its ownership, and whether it
> ever goes stale. The short operator card is [`test-strategy_guide.md`](test-strategy_guide.md); a fully
> worked instance is [`test-strategy_example.md`](test-strategy_example.md). Inline citations like
> [[1]](#ref-1) resolve to the [References](#references) at the bottom, numbered exactly as the research
> log numbers them; the full retrieval trail, including one source this bundle could not read and
> quarantines, is [`test-strategy_research-log.md`](test-strategy_research-log.md). This bundle sits in
> the `standing-standards` family alongside `definition-of-done`, `definition-of-ready`, `runbook`,
> `launch-coordination-checklist`, `production-readiness-review` and `business-continuity-plan`, as a
> **foundation**: a standard every project's own test plan is judged against, or states a reasoned
> deviation from, rather than an instrument executed under time pressure, per
> [ADR 0075 (test-strategy joins standing-standards as a foundation)](../../docs/internal/decisions/0075-test-strategy-joins-standing-standards-as-a-foundation.md).

---

## 1. Orientation

A test strategy is the standing document that sets the default testing approach for every project inside
one organization or program, and the rule by which each project's own test plan either follows that
default or states a reasoned deviation. ISTQB's current official glossary defines the organizational
artefact plainly: "A strategy that describes the generic requirements for testing and how to perform
testing within an organization." [[1]](#ref-1). The UK's Office of the Public Guardian states the same
job from the inside: "The intent here is to document a baseline test strategy that we expect applications
to adhere to in order to ensure a minimal level of quality assurance." [[41]](#ref-41). Published
program-level strategies put more detailed plans beneath it. Ofgem's own Switching Programme strategy
says its testing "will be followed by a more detailed programme level Testing Management Plan"
[[11]](#ref-11). A second UK program's joint strategy, for the smart metering rollout, says the testing it
describes "will be further elaborated in the Test Approach and Test Plan documents shown on the diagram"
[[14]](#ref-14). A third program's strategy, the HNG-X Testing Strategy, shows the same relationship; this
companion cites it throughout only for its published shape and never as a model of good testing practice,
since it reaches this research as evidence disclosed to the UK Post Office Horizon IT Inquiry
[[15]](#ref-15). It "covers all the testing and integration activities required across the whole HNG-X
programme" [[15]](#ref-15) and leaves detail to "a series of subordinate documents" [[15]](#ref-15).

The job in one sentence: a short, standing document that tells every project in an organization or
program what to test by default, and that lets a project deviate from that default only with a stated
reason.

**At a glance**

- This bundle covers the standing organization-or-program sense only. `test-plan` already covers the
  per-project sense, through its own `test_strategy_ref` field and its Risk-Ranked Approach section
  (section 8 below).
- ISTQB's current official glossary scopes the organizational artefact to "within an organization" and
  says nothing about a program. The "organization or programme (one or more projects)" wording that this
  library's own `test-plan` companion has treated as ISTQB's comes only from an unofficial mirror of
  older text, not from the current official page (section 2 below).
- Three independently structured program strategies (Ofgem, DCC, and - cited for shape only - HNG-X) and
  a procurement schedule (TfL) each put detail in a subordinate plan; DCC and HNG-X each also name an
  explicit exclusion by scope (section 3's Purpose and Scope subsection).
- Whether this document is stable once approved or a living one that keeps changing is argued three
  separate ways in the sources this bundle read (section 6); the Review Trigger section states a
  condition rather than taking a side.
- "A documented strategy helps multiple teams test in a consistent way" is a vendor's claim
  [[18]](#ref-18), not a measured finding, and this companion makes no stronger claim for the type's
  value than its sources make for themselves.

If you read nothing else: a test strategy, in this bundle's sense, is a standing, organization-or-program
default, never a portfolio-level one, and it is a different document from the per-project strategy
`test-plan` already ships.

## 2. Origins and evolution

No source read for this bundle supplies a founding story for the organizational test strategy: no named
originator, no founding decade, no first-use citation. What this research can support is a dated
snapshot of where the vocabulary stands today, and an open question about where it is going.

**The official glossary is live data, not a stable text, and reading it took an extra step.** The
glossary.istqb.org page itself renders an empty HTML shell, confirmed for this research by inspecting the
page's own output: a JavaScript single-page application with no server-rendered term text
[[2]](#ref-2). The research located the page's backing API and read the actual definitions there, dated
2026-10-20 [[1]](#ref-1). That text defines "organizational test strategy" as "A strategy that describes
the generic requirements for testing and how to perform testing within an organization"
[[1]](#ref-1), with no mention of a program anywhere in the glossary's API body, which held 1,128 terms
as read for this research on 2026-10-20 [[1]](#ref-1).

**An unofficial mirror serves older text, and this bundle's own sibling already cites it as ISTQB's
current wording.** `istqb-glossary.page` serves identical text under both its "test strategy" and its
"organizational test strategy" entries: "A high-level description of the test levels to be performed and
the testing within those levels for an organization or programme (one or more projects)."
[[3]](#ref-3). That is not the current official wording of either term [[1]](#ref-1). `test-plan`'s own
companion quotes this mirror's text as ISTQB's definition and tags the mirror a primary source
(`test-plan_companion.md:379-382`, `:506`); this companion names the disagreement rather than silently
repeating it, and the correction is a candidate edit for this bundle's landing PR, maintainer-vetoable,
not a silent edit made here.

**ISTQB's current syllabus names a possible rename this research could neither confirm nor deny.** The
Advanced Test Management syllabus, version 3.0, says the organizational artefact "is considered in the
context of ISO/IEC/IEEE 29119-3 (where it is referred to as an "organizational test practice")"
[[4]](#ref-4). No other source read uses that phrase. Wikipedia's account of the standard still names
"Organizational Test Strategy" [[6]](#ref-6), and so do both of imbus's glossary entries
[[7]](#ref-7)[[8]](#ref-8). ISTQB's own current glossary has no entry under the "practice" name, checked
directly against the same 1,128-term body. The standard's own clause text returned HTTP 403 on the one
attempt made to read it [[9]](#ref-9), so nothing in this bundle cites 29119-3's own words, and this
question stays open rather than settled either way.

**The Foundation syllabus confirms at least one adjacent rename this research can see directly.** Its own
change log records "organizational test policy -> test policy" [[5]](#ref-5). That is the policy term,
not the strategy term, but it shows the glossary's own vocabulary moving in a place this research can
verify without a secondary account standing in the way.

**Secondary accounts, not the standard itself, describe the artefact's place inside ISO/IEC/IEEE 29119.**
Wikipedia names "Organizational Test Strategy" as one of several named outputs of Part 3, alongside "Test
Plan (including a Test Strategy)" [[6]](#ref-6). imbus's vendor glossary, citing the 2013 edition, calls
the organizational artefact a "document that expresses the generic requirements for the testing to be
performed on all the projects run within the organization" and adds, "An organisation could have more
than one Organizational Test Strategy to cover markedly different project contexts." [[8]](#ref-8).
imbus's separate test strategy entry calls the two "a distinct entity" from one another
[[7]](#ref-7), but its own first definition reads as the organizational artefact restated, a tension this
companion names rather than resolves (section 6, item 2 below).

## 3. Anatomy (section by section)

This bundle ships one size. Its seven sections, in order: Purpose and Scope; Test Levels and Types;
Standard Tooling and Environments; Governance and Policy Alignment; How Project Test Plans Inherit or
Deviate; Roles and Responsibilities Across Projects; Review Trigger.

### Purpose and Scope

What counts as this organization or program here, which projects it binds, and what the strategy
explicitly leaves to each project's own test plan.

Process Street's own template opens with exactly this job: "Identify objectives of the test strategy
document" [[13]](#ref-13), then "Outline scope of the tests" [[13]](#ref-13). Every published program
strategy this research read draws a named boundary rather than leaving scope implicit. Ofgem places
itself inside one workstream: "This testing strategy forms part of the Delivery Strategy workstream
within the Blueprint Phase of the Switching Programme." [[10]](#ref-10). DCC names an explicit exclusion
among several read in raw text, "Certification of Comms Hubs" [[14]](#ref-14). HNG-X, again cited only for
its structure, excludes the release trains running alongside it: "It is not concerned with the testing
and integration required for the succession of Horizon releases continuing in parallel with and in
preparation for the HNG-X programme - this will be covered in separate testing strategy documents
specific to those Horizon releases." [[15]](#ref-15). What the strategy leaves to the plan is stated
directly by Ofgem's own Design Authority issue paper: "a detailed, programme level Testing Management Plan
should be developed during DLS to define the detailed testing approach for each test phase, entry and exit
criteria, detailed roles and responsibilities, reporting arrangements, etc." [[10]](#ref-10).

Beginner note: name the organization or program this strategy binds, state which projects inside it are
in scope, and name at least one thing explicitly out of scope, the way DCC and HNG-X each do. Expert
note: more than one strategy can be correct for the same organization; imbus's own caution, "An
organisation could have more than one Organizational Test Strategy to cover markedly different project
contexts." [[8]](#ref-8), is a reason to scope narrowly rather than write one document to cover every kind
of project at once.

### Test Levels and Types

The levels and types every project in scope inherits by default, unless its own plan states a reasoned
deviation.

No standards-tier source read for this bundle names the classic four levels, component, integration,
system and acceptance testing, as a verbatim line; that illustration exists only in the unofficial
mirror's own worked example [[3]](#ref-3), and this section must label it as the mirror's own
illustration, never as ISTQB's standard. Process Street's template asks the author to "Identify necessary
test levels" and "Identify types of testing to be performed" without naming any [[13]](#ref-13). The
Foundation syllabus lists test levels among what a plan's own test approach states [[5]](#ref-5). Ham
Vocke's own balance rule is a practitioner's framing, not a standards-tier one: "Write lots of small and
fast unit tests. Write some more coarse-grained tests and very few high-level tests that test your
application from end to end." [[29]](#ref-29). Where an external obligation makes a type mandatory,
naming the obligation belongs here. The US Internal Revenue Service's manual requires that "All system,
program, or test plans must include verification strategies addressing system integration, acceptance,
regression, privacy, and security" tied to a named law [[42]](#ref-42), and the UK's GDS Way makes
accessibility a standing, legally grounded requirement across every service [[43]](#ref-43). A standing
regression rule is a second candidate this research found evidenced directly: the UK Office of the Public
Guardian's baseline states "Regression should be built into automation at the unit and integration level"
and "An automated regression test should be added whenever you find a bug." [[41]](#ref-41). This section
must not restate `test-plan`'s own Test Levels and Types section or its Risk-Ranked Approach rows; it
states the organization-or-program default, never any one release's own levels.

Beginner note: name the levels and types every project in this organization or program must run by
default, and mark any that are mandatory because of a law, a regulation, a contract, or a past incident
rather than a preference. Expert note: a mandatory type with no stated reason reads as opinion; naming the
obligation, the way the IRS and GDS examples do, is what makes the row defensible when a project later
asks why.

### Standard Tooling and Environments

The tools and environments every project is expected to use by default, unless its own plan states
otherwise.

Process Street's template names this step directly: "Establish test environment and tools requirements"
[[13]](#ref-13). DCC's joint strategy covers the same ground, read for this bundle in raw text rather than
quoted, under its own headed section on test data and environments [[14]](#ref-14). A rule for personal
or production data in test belongs here where one exists. The IRS manual requires that "If live data is
used, prepare live data waiver, and ensure all testers have complete live data training."
[[42]](#ref-42), and Spain's data protection regulator states the general principle underneath that rule:
in testing, "sampling of real personal data should be avoided" [[36]](#ref-36), with "artificially created
test data" preferred [[36]](#ref-36), while conceding that where that cannot suffice, "a comprehensive
decision must be taken and documented" [[36]](#ref-36).

Beginner note: name the tools and environments a project should reach for first, and state the rule for
using real or production-derived data in any of them. Expert note: a rule that only forbids production
data, without naming the documented-exception path the Spanish regulator's own guidance states, invites a
project to either break the rule quietly or stall for lack of an escape valve.

### Governance and Policy Alignment

How this strategy relates to any higher test policy, where one exists, and who approves a change to the
strategy itself.

ISTQB's current glossary defines the policy that sits above the strategy: "High-level documentation
describing the principles, approach and major objectives of the organization regarding testing."
[[1]](#ref-1). imbus's secondary account of the organizational artefact states the alignment directly:
"It is aligned with the Organizational Test Policy" [[8]](#ref-8). A vendor's own enumeration of what a
strategy covers, read in full after a search summary misrepresented it, names the same breadth this
section carries: "Test-strategy objectives, risk model, coverage-selection rules, automation policy,
environment and data policy, evidence policy, governance, or cross-release exceptions"
[[22]](#ref-22). Who approves a change to the strategy itself is answered differently across the sources
this research read, and this section should show that disagreement rather than pick a winner (section 6,
item 4 below): TestRail says it is "Created and maintained by QA managers, test leaders, and strategic
teams" [[20]](#ref-20); Edana says "The strategy is overseen by a QA board or a cross-functional committee
including IT, business and architecture representatives." [[21]](#ref-21); DCC's own document is "issued
to the DCC Licensee's Design Assurance Board (DAB) for approval" [[14]](#ref-14); and the unofficial
mirror's FAQ, its provenance unverified, says ownership typically sits with "the organization's test
management or QA function" [[3]](#ref-3). A candidate this section's guidance should also carry: shared
metrics every project reports. OPG's baseline requires that suites measure coverage "As a delta introduced
by each pull request" [[41]](#ref-41) and reliability, "For example tracking how often particular tests
fail to highlight flaky tests" [[41]](#ref-41).

Beginner note: name any test policy this strategy aligns with, and name who approves a change to the
strategy itself, even if that is a role rather than a named person. Expert note: the sources disagree on
granularity, a role, a function, or a committee; pick the shape that matches how your organization
actually makes its other standing decisions, not the shape one vendor's own blog happens to describe.

### How Project Test Plans Inherit or Deviate

The seam with `test-plan`'s own `test_strategy_ref` field: a project names this strategy there, inherits
its levels, types, and tooling as the default, and states any deviation with its reason.

Every program-level source this research read describes exactly this relationship. Ofgem's own Design
Authority issue paper states, "a detailed, programme level Testing Management Plan should be developed
during DLS to define the detailed testing approach for each test phase, entry and exit criteria, detailed
roles and responsibilities, reporting arrangements, etc." [[10]](#ref-10), and the earlier-stage draft of
that same paper says the strategy itself "will be followed by a more detailed programme level Testing
Management Plan" [[11]](#ref-11). DCC's
strategy states that "The testing described in this document will be further elaborated in the Test
Approach and Test Plan documents shown on the diagram." [[14]](#ref-14). A deviation, where one is taken,
is recorded in the plan with its reason, in four sources' own words: the Foundation syllabus's plan
"explains why the testing will deviate from them" [[5]](#ref-5); TfL's procurement schedule requires the
plan to state "the reasons and rationale for such differences" [[12]](#ref-12); OPG's baseline calls local
variance "a conscious choice" that should "be able to be explained and preferably documented e.g. in an
ADR" [[41]](#ref-41); and the unofficial mirror's FAQ, provenance unverified, says "The test plan records
the rationale for any deviation" [[3]](#ref-3). Inside this library, that seam is already shipped as
`test-plan`'s own `test_strategy_ref` frontmatter field (`templates/test-plan/test-plan_template-full.md:7`).
A named approver for a deviation appears in only one source this research read, and it is not a test
strategy: the IRS manual's "Test Case Deferral and Waiver Requests are initiated within the test team and
are approved by the PM" [[42]](#ref-42) governs a directive over every test plan, not a standing strategy.
No source this research read states a sign-off step for a deviation from a standing strategy itself, so
this section should ask who may accept a deviation rather than naming a required approver field.

Beginner note: write what a project must do to adopt this strategy, name it in `test_strategy_ref`, and
what it must do to deviate from it, state the reason in its own plan. Expert note: resist adding a
named-approver field here on the strength of a single directive-level source; the evidence this research
found supports an ASK about who may accept a deviation, not a mandated title.

### Roles and Responsibilities Across Projects

Who owns this document at the organization-or-program level, distinct from who executes testing on any
one project.

This recurs in every published program strategy this research read, independent of how each document is
otherwise structured: Ofgem, TfL, and DCC each name roles and responsibilities in raw text, and HNG-X's
own heading, "6.0 People, Skills & Responsibilities" [[15]](#ref-15), cited for its structure only, is a
checked, verbatim span. Who
owns the document is answered differently across the sources, and this section should show the
disagreement rather than flatten it (section 6, item 4 below): TestRail ties ownership to "QA managers,
test leaders, and strategic teams" [[20]](#ref-20); QATestLab instead says, "Project Manager prepares Test
Strategy." [[24]](#ref-24), which contradicts a QA-manager owner directly; and a job posting for a
"Program Test Manager" [[19]](#ref-19) ties the role to this scope directly, naming someone who will
"Manage program testing activities that are correctly prioritised to deliver outcomes that align to the
Departments priorities" [[19]](#ref-19) and lists the Test Strategy among that role's own artefacts. The
audience is wider than the owners. Software Testing Help names Project Sponsors, Business SMEs, and
several delivery teams among them: "Test strategy is intended for the complete project team that
comprises Project Sponsors, Business SMEs" [[17]](#ref-17), and names Application/Integration Development,
System Integration Partners, Data Conversion Teams, and Build/Release Management Teams among the rest.

Beginner note: name who owns this document, separately from who is accountable for testing on any one
project inside it, since the sources this research read do not agree on whether those are the same role.
Expert note: the catalog's own `QA Manager` owner value is supported by one source [[20]](#ref-20) and the
unofficial mirror [[3]](#ref-3), and contradicted by another [[24]](#ref-24); a reviewer deciding this
field is choosing between live disagreement, not correcting an error.

### Review Trigger

Contract-mandated: a table of named conditions, owners, and actions, the same obligation every
`standing-standards` member carries.

No structural source read for this bundle publishes a section with this name or job; it is required
directly by the `standing-standards` family contract, which asks every member for "a review trigger with
a named owner and a condition, not a calendar reminder"
(`docs/internal/contracts/standing-standards.md`), rather than being volunteered by any source this
research read. This bundle labels the section as its own contribution the way its family siblings do. The
conditions this research supports, and where each comes from: a project's own test plan records a
deviation from this strategy, which is this strategy's own inheritance mechanism signalling a possible
drift, synthesized from the deviation sources above rather than named outright by any one of them
[[3]](#ref-3)[[5]](#ref-5)[[12]](#ref-12)[[41]](#ref-41); the test policy this strategy aligns with
changes, synthesized from imbus's own alignment language [[7]](#ref-7)[[8]](#ref-8) and TestRail's own
nearest conditions, "organizational objectives" and "regulations" among them [[20]](#ref-20); a test
summary report shows a mandated level or type was skipped, the closest named source being the IRS's own
waiver process, which means "departing from the course established in the test plan" [[42]](#ref-42),
alongside Tricentis's and Edana's own lessons-learned language [[18]](#ref-18)[[21]](#ref-21); and a new
test level, tool, or environment is adopted across more than one project without this document changing
to say so, sourced to TestRail's own named conditions, "technology" among them [[20]](#ref-20), and
Edana's own "tool revisions" [[21]](#ref-21). No source this research read names who notices any of these
conditions; the owner column is the contract's own obligation, not a sourced fact. Where a source names an
annual or periodic cadence, TestRail nonetheless states, "There is no universal review schedule."
[[20]](#ref-20), and Edana's own annual-or-semi-annual assessment is one described governance model, not
a measured norm [[21]](#ref-21); this section must treat any such cadence as a floor under the
conditions above, never as a calendar rewrite of this section's own rule.

Beginner note: fill every row with a condition, a named owner, and what that owner does about it; a blank
owner column is the one failure this family's own contract exists to prevent. Expert note: an annual
review clause from a regulator or an internal policy belongs here as a stated minimum frequency layered
under the condition-based trigger, never as a substitute for it.

## 4. Variants and sizing

**One size ships: `lean`.** No source read for this bundle describes a short form and a long form of the
type. Every structure found, Process Street's twenty-step template [[13]](#ref-13), the published program
strategies [[10]](#ref-10)[[11]](#ref-11)[[12]](#ref-12)[[14]](#ref-14), and, for shape only,
[[15]](#ref-15), and the catalog's
own content note, is one comprehensive shape rather than two weights of the same shape. Where the
evidence addresses size at all, it argues against a second, heavier variant rather than for one. Kolarov's
own range runs from "a collection of few stickers on the wall" to "quite long document(s)."
[[25]](#ref-25), which is evidence of variety across organizations, not evidence of two sizes inside one
template. QATestLab's small-project case folds the strategy into the plan instead of shrinking it, "Test
Strategy can be a part of the Test Plan if a project is small." [[24]](#ref-24), which is `test-plan`'s
own territory, not a lean variant of this bundle.

## 5. Methodology lineage

**No source read for this bundle comes from Scrum, SAFe, Shape Up, Lean, design thinking, or Amazon's own
internal mechanisms.** That is a statement about what this research set contains, not a claim that those
schools have nothing to say about test strategy.

**A certification lineage** supplies the current definitional spine and the open rename question: ISTQB's
live glossary [[1]](#ref-1)[[2]](#ref-2), its Advanced Test Management syllabus [[4]](#ref-4), and its
Foundation syllabus [[5]](#ref-5).

**An unofficial-mirror lineage** supplies the older, program-hedging text one of this bundle's own
siblings cites as ISTQB's own, and which this companion treats only as a mirror's text, provenance partly
unverified [[3]](#ref-3).

**A secondary-standards lineage** supplies two non-primary accounts of ISO/IEC/IEEE 29119's own structure,
since the standard's own clause text returned HTTP 403 on the one attempt made to read it: Wikipedia
[[6]](#ref-6) and imbus's vendor glossary [[7]](#ref-7), whose organizational-strategy entry cites the
2013 edition [[8]](#ref-8).

**A public-sector program lineage** supplies every published, filled program-level strategy this research
found: Ofgem's Switching Programme [[10]](#ref-10)[[11]](#ref-11), DCC's smart metering program
[[14]](#ref-14), a UK transport procurement schedule [[12]](#ref-12), and, cited for shape only, the
HNG-X program evidenced to the Post Office Horizon IT Inquiry [[15]](#ref-15).

**A vendor-template lineage** supplies the one named, stepwise production process this research found:
Process Street's twenty-step template [[13]](#ref-13).

**A testing-vendor and practitioner lineage** supplies the living-versus-stable debate, the plan-strategy
boundary, and the named failure modes: ReqTest [[16]](#ref-16), Software Testing Help [[17]](#ref-17),
Tricentis [[18]](#ref-18), a job posting [[19]](#ref-19), TestRail [[20]](#ref-20), Edana [[21]](#ref-21),
Playcode [[22]](#ref-22), BrowserStack [[23]](#ref-23), QATestLab [[24]](#ref-24), Kolarov
[[25]](#ref-25), and Wikipedia's own test plan article [[26]](#ref-26).

**A context-driven lineage** supplies the thinking-tool, per-effort sense of "test strategy," which this
bundle does not template: Bach's Heuristic Test Strategy Model [[27]](#ref-27) and Crispin's agile testing
quadrants, rebuilt "as you plan each iteration" [[28]](#ref-28).

**A practitioner lineage on terminology itself** names the discipline's own unsettled vocabulary
directly, without naming a test strategy at all: "The software development community simply hasn't
managed to settle on well-defined terms around testing." [[29]](#ref-29).

**A government and regulator lineage** supplies the gap-question leads this bundle's Governance and
Review Trigger sections draw on: the UK Office of the Public Guardian [[41]](#ref-41), the US Internal
Revenue Service [[42]](#ref-42), and the UK's GDS Way [[43]](#ref-43), alongside the GOV.UK Service
Manual's own pages on testing practice [[37]](#ref-37)[[38]](#ref-38)[[39]](#ref-39)[[40]](#ref-40).

**A data and platform-tooling lineage** supplies the example-domain facts this bundle's worked example
may draw on: dbt [[30]](#ref-30), Great Expectations [[31]](#ref-31), k6 [[32]](#ref-32)[[33]](#ref-33),
the W3C's own accessibility quickref [[34]](#ref-34), Pact [[35]](#ref-35), and Spain's data protection
regulator [[36]](#ref-36).

## 6. Debates and contested boundaries

**1. Is the document stable once approved, or a living one?** Three camps, named in the sources'
own words. Stable once approved: Software Testing Help's "Test strategy usually will not change once
approved." [[17]](#ref-17); BrowserStack's "a test strategy is broader in scope and usually remains stable
across multiple projects or releases" [[23]](#ref-23); and QATestLab's "Test Strategy is a static
long-term plan." [[24]](#ref-24). Living and evolving: ReqTest's "The test strategy is a living document
and evolves over time" [[16]](#ref-16); Tricentis's "A good testing strategy isn't static."
[[18]](#ref-18); and TestRail's "A long-term document that evolves with the organization's needs and
growth." [[20]](#ref-20). Stable, and changed on a named event: Edana's "As a stable, long-term document,
it is updated when major changes occur in technology, tools or team maturity." [[21]](#ref-21); Ofgem's
own framing of itself as "an enduring document" updated "periodically thereafter" [[10]](#ref-10); and
DCC's "Each new version supersedes the previous version in its entirety." [[14]](#ref-14). Software
Testing Help names both of the first two camps inside its own single article, which is evidence the
disagreement is real rather than an artifact of comparing different sources. Read against this family's
own contract, the third camp is the fit: the `standing-standards` contract states that members are "not
revised on a calendar" (`docs/internal/contracts/standing-standards.md`), and a document that stays
stable and changes when a named event makes it wrong satisfies that. This is this library's own reading,
not a conclusion any one source states.

**2. Does imbus's glossary describe one artefact or two?** imbus's test strategy entry states, "The
test strategy is a distinct entity from the Organizational Test Strategy." [[7]](#ref-7). Yet that same
entry's first sense, "Documentation aligned with the test policy that describes the generic requirements
for testing and details how to perform testing within an organization." [[7]](#ref-7), reads as the
organizational artefact restated. This companion names the tension rather than resolving it.

**3. Which document is the parent?** BrowserStack's own comparison marks the plan "Derived from the test
strategy" and the strategy "Independent of individual projects" [[23]](#ref-23), and QATestLab agrees in
substance. Wikipedia's test plan article reads the other way: "A test plan documents the strategy that
will be used to verify and ensure that a product or system meets its design specifications and other
requirements." [[26]](#ref-26), and adds that the plan's major elements "are also used in a formal test
strategy." [[26]](#ref-26), never putting the strategy above the plan. ISTQB's own syllabus agrees that a
project's strategy usually lives in its plan: it is "typically documented in a test plan or as part of
other documents" [[4]](#ref-4). That per-project reading is `test-plan`'s own subject, not this bundle's.

**4. Who owns and approves the strategy itself?** The sources disagree on granularity, a role, a
function, or a committee, and this companion does not pick a winner (sections 3's Governance and Roles
subsections, above). TestRail ties it to "QA managers, test leaders, and strategic teams"
[[20]](#ref-20); Edana to "a QA board or a cross-functional committee" [[21]](#ref-21); QATestLab to a
single "Project Manager" [[24]](#ref-24); a job posting to a named "Program Test Manager" role
[[19]](#ref-19); DCC to a design assurance board [[14]](#ref-14); HNG-X, cited for its structure only, to
joint "Approval Authorities" spanning two organizations, whose own names are not a checked span
[[15]](#ref-15); and the unofficial
mirror's FAQ, provenance unverified, to "the organization's test management or QA function"
[[3]](#ref-3). This moves the catalog's own `QA Manager` owner value from uncontested to disputed: QATestLab
contradicts it directly [[24]](#ref-24), while TestRail [[20]](#ref-20) and the mirror [[3]](#ref-3)
support it.

**5. What does "test strategy" mean, full stop?** A standing organizational document, per ISTQB
[[1]](#ref-1) and QATestLab [[24]](#ref-24); a heuristic thinking tool for one effort, per Bach's own
model, meant to be modified "to fit the context of your own organization" [[27]](#ref-27); a per-iteration
practice, per Crispin's quadrants, which a team repeats "as you plan each iteration" [[28]](#ref-28); and
a generic term usable at any scope, per ISTQB's own syllabus: "The generic term "test strategy" can be
used in any context (project, organization, product)." [[4]](#ref-4). This bundle builds only the first
sense, standing and spanning more than one project.

**6. What does ISO/IEC/IEEE 29119-3 actually call the artefact?** One syllabus sentence says
"organizational test practice" [[4]](#ref-4), against "Organizational Test Strategy" in every other
source read [[1]](#ref-1)[[6]](#ref-6)[[7]](#ref-7)[[8]](#ref-8). The standard's own text was never
retrieved [[9]](#ref-9), so this question is unresolved rather than settled either way, and this bundle's
own admission case would need revisiting, not quietly patching around, if a later reader confirms the
rename against the standard's current text.

**7. Is a standing strategy waterfall legacy?** Mirjana Kolarov voices the critique most readers hold
and answers it in the same abstract: "A big document of 40+ pages with ton of theory, no one reads and is
not up to date." [[25]](#ref-25), against "each Agile project needs Test Strategy as a guidance how
testing is done." [[25]](#ref-25), "why it must be tailor-made, because one strategy cannot fit all"
[[25]](#ref-25), and the rhetorical question this bundle must answer: "Why you cannot have a template and
just fill it in?" [[25]](#ref-25). BrowserStack names "Overdocumenting Everything" and "Ignoring Agile and
CI/CD Workflows" among its own named mistakes [[23]](#ref-23). The sources agree a strategy can be
tailored and kept short; none says it is unnecessary.

**8. Do the program documents actually show use across more than one project?** Ofgem [[10]](#ref-10),
TfL [[12]](#ref-12), DCC [[14]](#ref-14), and, cited for its structure only, HNG-X [[15]](#ref-15) each
show several phases, parties, test phases, or releases inside one program. Counting that as more than one
project is this library's own reading, the same reading the maintainer's own scope ruling of 2026-10-15
made, argued fully in
[ADR 0075 (test-strategy joins standing-standards as a foundation)](../../docs/internal/decisions/0075-test-strategy-joins-standing-standards-as-a-foundation.md);
no single source states the ruling's own phrase, "more than one project." These four sources are also not
fully independent of one another: Ofgem's own paper names SMIP among the projects it examined for lessons
learned, which the research reads as DCC's own smart metering program, so [[10]](#ref-10) and
[[14]](#ref-14) are probably related rather than two unconnected data points.

**9. Does a calendar cadence exist in practice?** TestRail states plainly, "There is no universal review
schedule." [[20]](#ref-20). Edana's own article describes the opposite as one governance model: the
strategy "is reviewed during annual or semi-annual assessments" [[21]](#ref-21). Ofgem says only that its
own document should be updated "periodically thereafter" [[10]](#ref-10), with no interval named. Edana's
own model is one described governance choice, not a measured norm across the field, which is why section
3's Review Trigger states conditions rather than a calendar.

**A closing note on figures.** GDS's own page states, "Automated testing can only find around 30% of
likely accessibility problems" [[43]](#ref-43), and GOV.UK's browser-support page states that its own
table "represents approximately 98% of the most popular browsers used on GOV.UK." [[38]](#ref-38). Both
are each source's own attributed claim, with no method stated in either source, and neither is a
prevalence figure for how many organizations keep a standing test strategy; no Quotable line anywhere in
this bundle's research carries such a figure, and none appears here.

## 7. Anti-patterns and failure modes

This section states only what a logged source names as a way the document fails, or what two logged
sources together show, with its own source or sources attached. No frequency claim is made for any of
them; no source this research read measured how often any of them happens.

**BrowserStack names six, each its own labelled mistake** [[23]](#ref-23): "Treating Both Documents as
the Same", where "Using test plan and test strategy interchangeably creates confusion around testing
scope, execution, and ownership"; "Overdocumenting Everything", where "Excessively detailed documents
increase maintenance effort and are rarely followed during actual testing"; "Not Updating Documentation",
where "Outdated test plans and strategies can lead to incorrect test coverage, missed risks, and
execution gaps"; "Missing Clear Ownership", where "Without defined ownership, testing responsibilities
and reporting processes become inconsistent across teams"; "Ignoring Agile and CI/CD Workflows", where
"Static documentation often fails to keep pace with rapid release cycles and continuous testing
practices"; and "Prioritizing Documentation Over Execution", where "Test documents are effective only
when they actively support testing, risk management, and release validation."

**Shelfware, in a practitioner's own words.** Kolarov opens with the image most readers already hold: "A
big document of 40+ pages with ton of theory, no one reads and is not up to date." [[25]](#ref-25). The
same abstract answers it rather than only naming it: "each Agile project needs Test Strategy as a
guidance how testing is done." [[25]](#ref-25).

**Copying instead of tailoring.** TestRail warns against a strategy "copied unchanged between projects."
[[20]](#ref-20).

**A standing strategy with a blank where an obligation sits.** OPG's own published baseline leaves one
shared term undefined: "Accessibility To be defined" [[41]](#ref-41). GDS states plainly that
"Government services are legally required to be accessible." [[43]](#ref-43). A published standing
strategy can therefore carry a blank where a binding obligation belongs; this research found one such
instance, not a measured rate of it.

**Levels out of balance.** Vocke warns against "a test ice-cream cone that will be a nightmare to
maintain and takes way too long to run." [[29]](#ref-29).

**The family's own failure mode.** The `standing-standards` contract says members fail "by going quietly
out of date" (`docs/internal/contracts/standing-standards.md`). BrowserStack's "Not Updating
Documentation" [[23]](#ref-23) and Kolarov's "not up to date" [[25]](#ref-25) are the same failure, stated
in the sources' own words.

## 8. Relationships to other artifacts

**`test-plan`: the sharpest boundary, and the one this bundle hands off to.** A test plan is scoped to one
effort, in ISTQB's own language covering "a project, a release, a product, or any other type of system
development or acquisition initiative" [[4]](#ref-4); this bundle is standing and spans more than one
project. The seam is the already-shipped `test_strategy_ref` field
(`templates/test-plan/test-plan_template-full.md:7`): a plan that inherits from this strategy names it
there, and states any reasoned deviation inside its own Risk-Ranked Approach section, rather than this
bundle restating either section's content. `test-plan`'s own guide already names the open question this
bundle inherits: "the certification bodies put strategy at the organization or programme level, plenty of
teams carry it as a section inside the plan, and practitioners openly disagree about which is written
first" (`templates/test-plan/test-plan_guide.md:41-43`). That sentence's "organization or programme"
framing rests on the same unofficial mirror's older text this companion names in section 2 above, not on
the current official glossary, which says only "within an organization" [[1]](#ref-1).

**`definition-of-done`: the closest sibling in form, different in subject.** Both are standing, both
declare `classification: foundation` under the `standing-standards` family contract, and both are agreed
once and consulted repeatedly rather than authored per increment
(`docs/internal/contracts/standing-standards.md`). A Definition of Done is a standard every increment is
judged against, in any discipline; this bundle is the standing testing-specific standard every project's
own verification approach either follows or states a deviation from. Neither replaces the other, and a
team may hold both at once.

**A master test plan is a plan, not this bundle.** ISTQB defines it directly: "A test plan that is used
to coordinate multiple test levels or test types." [[1]](#ref-1). Ofgem's own "programme level Testing
Management Plan" [[11]](#ref-11) reads, on this library's own interpretation, as that kind of plan, sitting
beneath a program-level strategy; this bundle must not absorb it or restate its content.

**The `qa-docs` family (`test-plan`, `test-case`, `test-summary-report`, `bug-report`): a phase boundary,
not a subject boundary.** Every member of that family plans, specifies, or reports the verification of
one product increment, authored at a stage and finished. This bundle is none of those three things: it
is not authored per increment and is not finished at any one stage, the reading the `qa-docs` family
contract's own exclusion clause states.

**`production-readiness-review`: a different standing instrument, at a different moment.** That review
asks whether one service is ready for standing production ownership to change hands; this bundle sets the
testing approach every project in scope follows by default. A readiness review's own criteria may ask
whether a project's testing conformed to this strategy, where one exists, without this bundle restating
any of that review's own criteria.

**`definition-of-ready`: an entry-side standard, not a testing-approach standard.** A Definition of Ready
governs when a backlog item is ready to enter a sprint; this bundle governs how testing is approached once
work is already underway. Neither gates the other.

## 9. Adaptations

**UK government services carry a legal, continuous accessibility duty this research found in no vendor
source.** The GDS Way states plainly, "Government services are legally required to be accessible. This
means services must comply with the international WCAG 2.2 AA accessibility standard" [[43]](#ref-43),
retested "especially when you introduce a significant feature or make any major change" [[43]](#ref-43).
A standing strategy for an organization under that duty should make the type mandatory and name the
obligation, not merely list it as one testing type among others.

**US federal agencies carry a named, directive-level waiver process above any one project's plan.** The
IRS manual ties mandatory testing types directly to law: "All system, program, or test plans must include
verification strategies addressing system integration, acceptance, regression, privacy, and security as
required by Cybersecurity and Section 508 of the 1973 Rehabilitation Act as currently amended."
[[42]](#ref-42). It separates a directive-level deviation approval, "Any waivers or deviations of this
Directive require written approval from the ACIO, Enterprise Services." [[42]](#ref-42), from a
test-case-level one approved by the project manager.

**A public-sector organization with an already-published baseline can still leave a binding obligation
blank, and that is a real, named gap, not a theoretical one.** The UK Office of the Public Guardian's own
baseline states "Accessibility To be defined" [[41]](#ref-41) in a field it otherwise fills in, beside
GDS's own statement that the same obligation is a legal requirement [[43]](#ref-43). This research found
one instance of that gap, not a measured rate of it.

**This research found nothing to support an org-size, methodology-specific, or solo-versus-team
adaptation**, and this companion states that gap rather than inventing a scaling rule no source carries.
QATestLab's only size-related statement folds the strategy into the plan on a small project
[[24]](#ref-24), which is `test-plan`'s own territory, not a smaller version of this bundle.

## 10. Worked example

[`test-strategy_example.md`](test-strategy_example.md) is a program-level standing strategy for the
Reporting Platform Modernization program, the shared container `kpi-dashboard_example.md` and
`risk-register_example.md` already name, with Marta Reyes as its Program Manager. It is worth checking
three things in it. First, that it is dated after `test-plan_example.md`'s own `last_updated` date of
2026-07-06, since that plan's own frontmatter states, as of that date, "Acme Reporting has no standing
test strategy document", and this bundle's example must not retcon that sentence, only post-date it.
Second, that its owner is Anjali Rao, QA Lead, Reporting, the title `test-plan_example.md` and
`test-summary-report_example.md` already give consistently. Third, that any program-level default it
states, for data tests, load tests, contract tests, accessibility, environments, or test data, is
labelled illustrative rather than presented as a measured fact, the same labelling this bundle's own
Governance and Test Levels and Types sections require of every figure they carry. It must not restate any
row of `test-plan_example.md`'s own Risk-Ranked Approach or Test Levels and Types sections, and it must
not quote the k6 load-test-type names, the W3C contrast ratio's own number, or a UK legal duty as though
it bound a fictional company.

---

## References

Tagged by reliability, following the research log's own five-way split, which this companion keeps:
`[primary]` the originating or standards-body source itself, or a government body's own primary
document; `[standards]` a certification body's, standards body's, or government service manual's own
published guidance, read as a document rather than as an originating standard; `[reference]` a general
encyclopedic or mirror source, not itself the standard or the certifying body; `[practitioner]` a
recognized independent authority or canonical article; `[vendor]` a tool vendor or commercially motivated
source, reliable on convention, corroborated for claims of fact. Researched 2026-10-20. Retrieval status
per source is recorded in
[`test-strategy_research-log.md`](test-strategy_research-log.md); only sources marked
fetched-and-verified there are quoted here.

<a id="ref-1"></a>[1] ISTQB (International Software Testing Qualifications Board). "[Official Glossary](https://api.glossary.istqb.org/v1/terms)," live API endpoint behind glossary.istqb.org (accessed 2026-10-20). Supports the current official definitions of test strategy, organizational test strategy, test policy, test approach, test plan, and master test plan. [standards]

<a id="ref-2"></a>[2] ISTQB. "[Glossary search page](https://glossary.istqb.org/en_GB/search?term=test+strategy)," glossary.istqb.org (accessed 2026-10-20). Supports that the official rendering page itself returns an empty HTML shell with no server-rendered term text, which is why [[1]](#ref-1) reads the page's own backing API instead. [standards]

<a id="ref-3"></a>[3] istqb-glossary.page (unofficial ISTQB glossary mirror). "[Test Strategy](https://istqb-glossary.page/test-strategy/)" and "Organizational Test Strategy" entries (accessed 2026-10-20). Supports the mirror's older, program-hedging definition text, its worked illustration, and its FAQ on ownership and deviation, provenance unverified. [reference]

<a id="ref-4"></a>[4] ISTQB. "[Certified Tester Advanced Level Test Management (CTAL-TM) Syllabus, Version 3.0](https://www.istqb.org/wp-content/uploads/2024/11/ISTQB_CTAL-TM_Syllabus_v3.0_zKjKsaN.pdf)" (accessed 2026-10-20). Supports the organizational-strategy-as-given framing, the project test strategy's own scope, the generic any-context use of the term, and the open "organizational test practice" rename question. [standards]

<a id="ref-5"></a>[5] ISTQB. "[Certified Tester Foundation Level (CTFL) Syllabus, Version 4.0.1](https://www.istqb.org/wp-content/uploads/2024/11/ISTQB_CTFL_Syllabus_v4.0.1.pdf)" (accessed 2026-10-20). Supports the plan's deviation-recording language and the confirmed glossary rename, "organizational test policy -> test policy," from the syllabus's own change log. [standards]

<a id="ref-6"></a>[6] Wikipedia contributors. "[ISO/IEC 29119](https://en.wikipedia.org/wiki/ISO/IEC_29119)." Wikipedia (accessed 2026-10-20). Supports a secondary account of how Part 3 names the Organizational Test Strategy and the Test Plan as separate outputs, and of Part 2's organizational, project, and dynamic process levels. [reference]

<a id="ref-7"></a>[7] imbus. "[Glossary of software testing terms: test strategy](https://www.imbus.de/en/glossar/term/test-strategy)" (accessed 2026-10-20). Supports a secondary, vendor account of the project-level sense of test strategy and its own stated, internally tense, distinction from the Organizational Test Strategy. [vendor]

<a id="ref-8"></a>[8] imbus. "[Glossary of software testing terms: Organizational Test Strategy](https://www.imbus.de/en/glossar/term/Organizational-Test-Strategy)" (accessed 2026-10-20). Supports a secondary, vendor account of the organizational artefact, citing ISO/IEC/IEEE 29119-1:2013-09, including its policy alignment and its allowance for more than one strategy per organization. [vendor]

<a id="ref-9"></a>[9] ISO. "[Online Browsing Platform, ISO/IEC/IEEE 29119-3 preview](https://www.iso.org/obp/ui/#iso:std:iso-iec-ieee:29119:-3:ed-2:v1:en)" (attempted 2026-10-20). The standard's own clause text. Returned HTTP 403 Forbidden on the one attempt made; not retrieved, and no claim in this bundle rests on its text. [primary]

<a id="ref-10"></a>[10] Ofgem (David Liversidge). "[Switching Programme Testing Strategy](https://www.ofgem.gov.uk/sites/default/files/docs/2016/10/da_testing_strategy_da280916.pdf)," Design Authority issue paper (accessed 2026-10-20). Supports a published program-level strategy's own scope statement, its named exclusions, its "enduring document" framing, and what it leaves to a subordinate program-level plan. [primary]

<a id="ref-11"></a>[11] Ofgem (David Liversidge; James Crump). "[Switching Programme Testing Strategy](https://www.ofgem.gov.uk/system/files/docs/2016/09/ds_testing_strategy_final_product_blueprint_phase_edag.pdf)," an earlier-stage draft of the same paper as [[10]](#ref-10) (accessed 2026-10-20). Supports that the same scope and "followed by" language appears across both drafting stages of this one program strategy. [primary]

<a id="ref-12"></a>[12] Transport for London. "[Schedule 4, Testing Regime](https://content.tfl.gov.uk/lchs-schedule4-testing-regime-redacted.pdf)," London Cycle Hire Service Agreement, redacted procurement schedule (accessed 2026-10-20). Supports a Test Strategy as a required contractual deliverable, approved by the client, with each test plan required to state its reasons for differing from it. [primary]

<a id="ref-13"></a>[13] Process Street. "[Test Strategy Document Template](https://www.process.st/templates/test-strategy-document-template/)" (accessed 2026-10-20). Supports all twenty of the template's own steps, in order, paraphrased for section naming since the page states no reuse licence; not copied verbatim into any template. [vendor]

<a id="ref-14"></a>[14] DCC (Dave Norman). "[Smart Metering Implementation Programme Joint Test Strategy](https://www.smartdcc.co.uk/media/1091/joint_test_strategy_v35.pdf)," v3.5 (accessed 2026-10-20). Supports a second, independently structured published program strategy: its multi-party scope, its named exclusions, its versioning and board-approval process, and what it leaves to subordinate Test Approach and Test Plan documents. [primary]

<a id="ref-15"></a>[15] Fujitsu Services Ltd / Post Office Ltd. "[HNG-X Testing Strategy](https://postofficeinquiry.dracos.co.uk/projects/evidence/FUJ00232570/)," TST/GEN/STG/0001 v1.0, disclosed as evidence FUJ00232570 to the UK Post Office Horizon IT Inquiry (accessed 2026-10-20). Supports a third, independently structured program-scope strategy's own section headings, its scope and named exclusions, and its subordinate-document relationship. Cited throughout this companion for its published shape only, never as a model of good testing practice, given its origin as disclosed inquiry evidence. [primary]

<a id="ref-16"></a>[16] ReqTest. "[Test Documentation in Agile Projects](https://reqtest.com/en/knowledgebase/test-documentation-in-agile-projects/)" (accessed 2026-10-20). Supports the living-document camp and the relationship between a standing strategy and per-sprint test plans. [vendor]

<a id="ref-17"></a>[17] Software Testing Help. "[Difference Between Test Plan, Test Strategy, Test Case, Test Script, Test Scenario And Test Condition](https://www.softwaretestinghelp.com/difference-between-test-plan-test-strategy-test-case-test-script-test-scenario-and-test-condition/)" (accessed 2026-10-20). Supports both the stable and the living camps named inside one article, and the strategy's own, wider intended audience. [practitioner]

<a id="ref-18"></a>[18] Tricentis. "[Software Test Strategy](https://www.tricentis.com/learn/software-test-strategy)" (accessed 2026-10-20). Supports the living-document camp and the vendor's own, unmeasured claim that a documented strategy standardizes practice across teams. [vendor]

<a id="ref-19"></a>[19] SoftTest Pays Pty Ltd. "[Program Test Manager](https://careers-page.com/softtest-pays-pty-ltd/job/L688Y59W)" job posting, Canberra, ACT (accessed 2026-10-20). Supports a named, program-scoped role that manages, defines, approves, and plans the Test Strategy among other testing artefacts. [practitioner]

<a id="ref-20"></a>[20] TestRail (Idera). "[Test Plan vs Test Strategy: When to Use Each](https://www.testrail.com/blog/test-plan-vs-test-strategy/)" (accessed 2026-10-20). Supports the long-term-document framing, the tailoring warning against copying a strategy unchanged, the denial of a universal review schedule, and named review-trigger conditions. [vendor]

<a id="ref-21"></a>[21] Edana (Jonathan Massa). "[Test Plan vs Software Test Strategy: Structure, Objectives and Key Differences Explained](https://edana.ch/en/2026/01/14/test-plan-vs-software-test-strategy-structure-objectives-and-key-differences-explained/)" (accessed 2026-10-20). Supports a named governing committee, a named annual-or-semi-annual review cadence specific to one organization, and the formalize-then-tailor relationship between strategy and plan. [practitioner]

<a id="ref-22"></a>[22] Playcode.io. "[Test Plan vs Test Strategy](https://playcode.io/blog/test-plan-vs-test-strategy)" (accessed 2026-10-20). Read in full after a search summary misrepresented its content; supports only its own enumeration of what a test strategy covers, not a deviation-approval claim. [vendor]

<a id="ref-23"></a>[23] BrowserStack. "[Test Plan vs Test Strategy: Purpose & Differences](https://www.browserstack.com/guide/test-plan-vs-test-strategy)" (accessed 2026-10-20). Supports the plan-strategy scope and stability distinction, the plan-derived-from-strategy table, and six named failure modes for standing test documentation. [vendor]

<a id="ref-24"></a>[24] QATestLab. "[Difference between Test Plan and Test Strategy](https://qatestlab.com/resources/knowledge-center/test-plan-vs-strategy/)" (accessed 2026-10-20). Supports the organizational, static-document camp, a single-project-manager owner that contradicts other sources, and the small-project case where the strategy folds into the plan. [vendor]

<a id="ref-25"></a>[25] Mirjana Kolarov, via Agile Testing Days 2019 session page. "[Test Strategy - waterfall legacy or game changer in Agile](https://agiletestingdays.com/2019/session/test-strategy-waterfall-legacy-or-game-changer-in-agile/)" (accessed 2026-10-20). Supports the shelfware critique, its own practitioner reply that a strategy must be tailored and short, and evidence of size variety across organizations. [practitioner]

<a id="ref-26"></a>[26] Wikipedia contributors. "[Test plan](https://en.wikipedia.org/wiki/Test_plan)." Wikipedia (accessed 2026-10-20). Supports a general-reference definition of a test plan and its statement that the plan documents the strategy, the reverse of the organizational framing. [reference]

<a id="ref-27"></a>[27] James Bach (Satisfice, Inc.). "[Heuristic Test Strategy Model](https://www.satisfice.com/download/heuristic-test-strategy-model)" download page (accessed 2026-10-20). Supports the context-driven, per-effort, heuristic sense of "test strategy," explicitly meant to be modified per organization rather than standardized. [practitioner]

<a id="ref-28"></a>[28] Lisa Crispin, via TechTarget IT Infrastructure. "[Agile testing quadrants: Guiding managers and teams in test strategies](https://www.techtarget.com/it-infrastructure/tip/Agile-testing-quadrants-Guiding-managers-and-teams-in-test-strategies)" (accessed 2026-10-20). Supports the agile testing quadrants as a per-iteration frame for building a test strategy rather than one fixed standing document. [practitioner]

<a id="ref-29"></a>[29] Ham Vocke (Thoughtworks), via martinfowler.com. "[The Practical Test Pyramid](https://martinfowler.com/articles/practical-test-pyramid.html)" (accessed 2026-10-20). Supports a level-balance heuristic, the warning against a test ice-cream cone, and the discipline's own unsettled terminology; this article never uses the term "test strategy" itself. [practitioner]

<a id="ref-30"></a>[30] dbt Labs. "[Data tests](https://docs.getdbt.com/docs/build/data-tests)," dbt Docs (accessed 2026-10-20). Supports data-correctness testing in analytics pipelines, for this bundle's worked-example domain only. [vendor]

<a id="ref-31"></a>[31] Great Expectations. "[GX Core overview](https://docs.greatexpectations.io/docs/core/introduction/gx_overview)," GX Docs v1.24.0 (accessed 2026-10-20). Supports a second data-validation framework's own vocabulary, for this bundle's worked-example domain only. [vendor]

<a id="ref-32"></a>[32] Grafana Labs. "[Load test types](https://grafana.com/docs/k6/v2.3.x/testing-guides/test-types.md)," k6 Documentation, v2.3.x (accessed 2026-10-20). Supports a six-type load-testing taxonomy, for this bundle's worked-example domain only; the type names themselves sit inside link syntax in the raw text and are not quoted here. [vendor]

<a id="ref-33"></a>[33] Grafana Labs. "[API load testing](https://grafana.com/docs/k6/v2.3.x/testing-guides/api-load-testing.md)," k6 Documentation, v2.3.x (accessed 2026-10-20). Supports a program-level procedure for maturing API load tests over time, for this bundle's worked-example domain only. [vendor]

<a id="ref-34"></a>[34] W3C Web Accessibility Initiative. "[How to Meet WCAG (Quickref Reference)](https://www.w3.org/WAI/WCAG22/quickref/)," WCAG 2.2 (accessed 2026-10-20). Supports the existence of a contrast-ratio criterion, for this bundle's worked-example domain only; its specific ratio and level are not stated as fact anywhere in this companion. [standards]

<a id="ref-35"></a>[35] Pact Foundation. "[Introduction](https://docs.pact.io/)," Pact Docs (accessed 2026-10-20). Supports contract testing between services as a technique, for this bundle's worked-example domain only. [vendor]

<a id="ref-36"></a>[36] Agencia Española de Protección de Datos (AEPD). "[Personal Data Breaches: Development and Pre-Production Environments](https://www.aepd.es/en/prensa-y-comunicacion/blog/data-breaches-development-and-pre-production-enviroments)" (accessed 2026-10-20). Supports the data-protection principle against using real personal data in test environments and the documented-exception path where synthetic data cannot suffice. [standards]

<a id="ref-37"></a>[37] GOV.UK Service Manual. "[Working in pre-production environments](https://www.gov.uk/service-manual/technology/working-in-pre-production-environments)" (accessed 2026-10-20). Supports a named environment ladder, for this bundle's worked-example domain only. [standards]

<a id="ref-38"></a>[38] GOV.UK Service Manual. "[Designing for different browsers and devices](https://www.gov.uk/service-manual/technology/designing-for-different-browsers-and-devices)" (accessed 2026-10-20). Supports a browser-support policy and its own attributed, unmeasured "approximately 98%" coverage figure, for this bundle's worked-example domain only. [standards]

<a id="ref-39"></a>[39] GOV.UK Service Manual. "[Quality assurance: testing your service regularly](https://www.gov.uk/service-manual/technology/quality-assurance-testing-your-service-regularly)" (accessed 2026-10-20). Supports a named list of web-service test types, for this bundle's worked-example domain only. [standards]

<a id="ref-40"></a>[40] GOV.UK Service Manual. "[Test your service's performance](https://www.gov.uk/service-manual/technology/test-your-services-performance)" (accessed 2026-10-20). Supports load-testing practice and capacity planning, for this bundle's worked-example domain only. [standards]

<a id="ref-41"></a>[41] UK Ministry of Justice, Office of the Public Guardian (OPG). "[Baseline Testing Standards](https://docs.opg.service.justice.gov.uk/documentation/guides/baseline_testing_standards.html)," OPG Technical Guidance (accessed 2026-10-20). Supports a real, published, cross-project baseline strategy: its own stated intent, its local-variance mechanism, its regression policy, its mandatory shared metrics, and its own blank accessibility field. [primary]

<a id="ref-42"></a>[42] US Internal Revenue Service. "[Internal Revenue Manual 2.127.2, IT Testing Process and Procedures](https://www.irs.gov/irm/part2/irm_02-127-002)," revised 01-03-2025 (accessed 2026-10-20). Supports a mandatory federal testing directive above any one project's plan: its law-tied mandatory test types, its two-level waiver and deviation approval, its live-data rule, and its aggregated cross-project status reporting. [primary]

<a id="ref-43"></a>[43] UK Government Digital Service / Cabinet Office. "[Building accessible services](https://gds-way.digital.cabinet-office.gov.uk/manuals/accessibility.html)," The GDS Way engineering manual (accessed 2026-10-20). Supports a published engineering organization's own standard making accessibility testing mandatory, legally grounded, and continuous, including its own attributed, unmeasured "around 30%" figure for what automated testing finds. [primary]
