---
title: "{{organization_or_program_name}} Test Strategy"
doc_type: test-strategy
size: lean
organization_or_program_name: "{{organization_or_program_name}}"
owner: "{{owner}}"
status: draft
doc_version: "{{doc_version}}"
created: "{{date}}"
updated: "{{date}}"
related_links: []
source_template: test-strategy
source_template_version: 0.1.0
---

<!--
LEAN TEST STRATEGY. This bundle ships one size, deliberately, and the evidence runs against a second,
heavier weight rather than for one. Mirjana Kolarov names the image most readers already hold: "A big
document of 40+ pages with ton of theory, no one reads and is not up to date." BrowserStack names the
same failure as one of its own six anti-patterns, "Overdocumenting Everything". No source read for this
bundle describes a short form and a long form of this document; every structure found is one
comprehensive shape, not two weights of the same shape. A second, heavier variant would model the exact
failure this bundle warns against, so the document stays small on purpose. See
test-strategy_companion.md section 4 (Variants and sizing).

WHAT THIS IS NOT
It is NOT a test plan. A test plan is scoped to one project and written per release; this document is
standing and spans more than one project in one organization or program. The seam is the
test_strategy_ref field already shipped in test-plan's own frontmatter: a project names this strategy
there, inherits its defaults, and states any deviation, with its reason, inside its own Risk-Ranked
Approach section. This document must not restate either of test-plan's own sections.
It is NOT a master test plan. ISTQB defines that type directly: "A test plan that is used to coordinate
multiple test levels or test types." A master test plan sits beneath this strategy, coordinating one
project's own levels, not above it.
It is NOT a Definition of Done. Both are standing, both are agreed once and consulted repeatedly rather
than authored per increment. A Definition of Done is a standard every increment is judged against, in any
discipline; this document is the testing-specific standard a project's own verification approach either
follows or states a reasoned deviation from. A team may hold both at once.
See test-strategy_companion.md section 8 (Relationships to other artifacts).

HOW TO FILL THIS IN
1. Read the comment under each heading: WHAT it wants, WHY it matters (with a pointer into
   test-strategy_companion.md for the deep reasoning), guiding questions to ASK, a GOOD and a WEAK
   example, and the TRAP to avoid. The three tables also carry PRIORITY and ROW HINT.
2. Replace each {{placeholder}} with your content.
3. If a section, or one row inside a table, does not apply, write "N/A" and one line of why, rather than
   leaving it blank or deleting the section. An unexplained blank and a skipped item look identical to a
   later reader.
4. This is a standing document, revisited on the Review Trigger below, not written once and forgotten.
   Before you first share it: self-grade against test-strategy_guide.md, then DELETE every HTML comment.
   They are guidance, not content.
-->

# {{organization_or_program_name}} Test Strategy

## Purpose and Scope

<!-- WHAT  What counts as "this organization or program" here, which projects it binds, and what it
           explicitly leaves out, either to a separate strategy or to each project's own test plan.
     WHY   Every published program strategy this bundle's research read draws a named boundary rather
           than leaving scope implicit. DCC's own joint test strategy names an explicit exclusion among
           several read in raw text: "Certification of Comms Hubs." A good strategy excludes by naming
           what it leaves out the way DCC does, rather than leaving a reader to guess. imbus's own
           caution against writing one strategy for every kind of project this organization runs: "An
           organisation could have more than one Organizational Test Strategy to cover markedly different
           project contexts." Scope this document narrowly rather than writing one strategy to cover
           every project this organization or program runs. Deep dive: test-strategy_companion.md
           section 3 (Anatomy > Purpose and Scope).
     ASK   Which organization or program does this strategy bind? Which projects inside it are in scope?
           What is explicitly out of scope, the way DCC names an exclusion? Does a different kind of
           project inside this same organization need its own, separate strategy instead of being forced
           into this one?
     GOOD  "This strategy binds every project run by the Billing Modernization program at Granite Peak
           Utilities. In scope: all projects under that program's own release calendar. Out of scope: the
           Field Operations program, which keeps its own separate test strategy, and third-party meter
           certification testing, which the vendor's own contract governs."
     WEAK  "This is how we test." (names no organization or program, no bound projects, and nothing
           explicitly excluded)
     TRAP  Writing one strategy to cover every kind of project this organization runs. imbus's own caution
           is that an organization can hold more than one Organizational Test Strategy for markedly
           different project contexts; a single document straining to fit all of them is a sign it should
           split, not a sign it is thorough. -->

{{purpose_and_scope_statement}}

**Explicitly out of scope:** {{explicit_exclusions}}

## Test Levels and Types

<!-- WHAT  The levels and types every project in this organization or program inherits by default, and
           which of them are mandatory because of a law, a regulation, a contract, or a past incident
           rather than a preference.
     WHY   No standards-tier source read for this bundle names a single required list of levels; a
           published vendor template asks only that an author name the levels and types a strategy
           covers, without prescribing one. Where an external obligation makes a type mandatory, naming
           the obligation belongs here. A UK government engineering manual states the duty plainly for
           public-sector services: "Government services are legally required to be accessible. This means
           services must comply with the international WCAG 2.2 AA accessibility standard." A US federal
           agency ties several types directly to law: "All system, program, or test plans must include
           verification strategies addressing system integration, acceptance, regression, privacy, and
           security as required by Cybersecurity and Section 508 of the 1973 Rehabilitation Act as
           currently amended." A standing regression rule is a third candidate evidenced directly, from a
           UK public body's own published baseline: "Regression should be built into automation at the
           unit and integration level" and "An automated regression test should be added whenever you
           find a bug." This section must not restate test-plan's own Test Levels and Types section or
           its Risk-Ranked Approach rows; it states the organization-or-program default, never any one
           release's own levels. Deep dive: test-strategy_companion.md section 3 (Anatomy > Test Levels
           and Types).
     ASK   Which levels and types does every project in this organization or program run by default? Is
           any of them mandatory because of a law, a regulation, a contract, or a past incident, rather
           than a preference? Where does this strategy currently carry a blank where one of those
           obligations belongs?
     PRIORITY  List any level or type mandated by a law, a regulation, a contract, or a past incident
           first; a team can get a preference wrong and adjust it later, but a mandated type left out is
           a different kind of failure.
     ROW HINT  A good row names a level or type, states whether it is this program's own default or a
           mandatory requirement, and, if mandatory, names the obligation behind it. A weak row names
           neither a level nor an obligation.
     GOOD  | Accessibility (WCAG 2.2 AA) | Mandatory | Legal obligation for UK public-sector services:
           "Government services are legally required to be accessible. This means services must comply
           with the international WCAG 2.2 AA accessibility standard." |
     WEAK  | Testing | Default | | (names no level, no type, and no obligation)
     TRAP  Leaving a binding obligation blank rather than researching it once and writing it down. A UK
           public body's own published baseline, otherwise filled in, states "Accessibility To be
           defined" beside a sibling obligation another source calls a legal requirement. A single
           instance is not a measured rate of this failure, but it is a real, preventable one. -->

| Level or Type | Default or Mandatory | Reason or Obligation |
|---|---|---|
| {{level_or_type}} | {{level_or_type_status}} | {{level_or_type_reason}} |

## Standard Tooling and Environments

<!-- WHAT  The tools and environments every project is expected to use by default, and the rule for
           using real or production-derived data in any of them.
     WHY   A published vendor template names establishing test environment and tooling requirements as
           its own step, without prescribing what they must be. A data protection regulator states the
           general principle a rule here should rest on: in testing, "sampling of real personal data
           should be avoided," with "artificially created test data" preferred, while conceding that
           where that cannot suffice, "a comprehensive decision must be taken and documented". A US
           federal agency's own live-data rule shows one working version of that documented exception:
           "If live data is used, prepare live data waiver, and ensure all testers have complete live data
           training." Deep dive: test-strategy_companion.md section 3 (Anatomy > Standard Tooling and
           Environments).
     ASK   What tools and environments should a project reach for first, by default? What is the rule for
           using real or production-derived data in any of them? Is there a documented-exception path for
           when synthetic data cannot suffice, or does the rule simply forbid it?
     GOOD  "Default environment: a staging tier seeded with synthetic data generated from the production
           schema, never production data itself. Where synthetic data cannot exercise a defect under
           investigation, a written, dated waiver naming the specific tables and the reviewer who
           approved it is required before any real data is loaded."
     WEAK  "Use whatever environment you have." (names no default tools or environments, and says
           nothing about production-derived data)
     TRAP  Writing a rule that only forbids production data, with no documented-exception path. A project
           that hits a case synthetic data cannot cover will then either break the rule quietly or stall
           for lack of an escape valve; a regulator's own guidance names the exception path as part of the
           rule, not as a separate concession. -->

{{standard_tooling_and_environments}}

**Rule for real or production-derived data in test:** {{production_data_rule}}

## Governance and Policy Alignment

<!-- WHAT  How this strategy relates to any higher test policy, where one exists, and who approves a
           change to the strategy itself.
     WHY   ISTQB's current glossary defines the policy that sits above this kind of strategy:
           "High-level documentation describing the principles, approach and major objectives of the
           organization regarding testing." A secondary account of the standard this strategy's own
           structure draws on states the alignment directly for this kind of document: "It is aligned
           with the Organizational Test Policy". Who approves a change to the strategy itself is answered
           differently across the sources this bundle's research read, and this section should show that
           disagreement rather than pick a winner: one vendor ties it to "QA managers, test leaders, and
           strategic teams"; another ties it to "a QA board or a cross-functional committee including IT,
           business and architecture representatives." A published program strategy instead routes
           approval to a named design assurance board. Deep dive: test-strategy_companion.md section 3
           (Anatomy > Governance and Policy Alignment).
     ASK   Does a test policy exist above this strategy? If so, name it and state how this strategy
           aligns with it. If not, say so plainly rather than leaving the question unanswered. Who
           approves a change to this strategy itself: a named role, a function, or a committee?
     GOOD  "No separate test policy exists yet; this strategy is Granite Peak Utilities' first written
           statement of testing principles and will be revised to align the day a policy is adopted.
           Changes to this strategy are approved by the VP of Engineering, after review by the Billing
           Modernization program's own architecture group."
     WEAK  "Approved by QA." (names no policy relationship, and no actual approving person, function, or
           body a reader could go find)
     TRAP  Assuming one shape, a single manager, a function, or a committee, because one source's own
           account happens to describe it. The sources disagree on granularity; pick the shape that
           matches how this organization actually makes its other standing decisions. -->

{{test_policy_alignment_statement}}

**Who approves a change to this strategy:** {{strategy_approver}}

## How Project Test Plans Inherit or Deviate

<!-- WHAT  The seam with test-plan's own test_strategy_ref field: what a project must do to adopt this
           strategy's defaults, and what it must do, and who may accept it, when it deviates.
     WHY   Every program-level source this bundle's research read describes exactly this relationship.
           One published program strategy states, "This testing strategy will be followed by a more
           detailed programme level Testing Management Plan". It names what that subordinate plan
           carries too: "the detailed testing approach for each test phase, entry and exit criteria,
           detailed roles and responsibilities, reporting arrangements". A procurement schedule requires a
           project's own plan to state "the reasons and rationale for such differences" wherever it
           differs from this kind of strategy. A UK public body's own baseline calls a local variance "a
           conscious choice" that should "be able to be explained and preferably documented e.g. in an
           ADR." No source this research read states a required, named approver for a deviation from a
           standing strategy itself, so this section asks who may accept a deviation rather than naming a
           mandated title. Deep dive: test-strategy_companion.md section 3 (Anatomy > How Project Test
           Plans Inherit or Deviate).
     ASK   What must a project do to adopt this strategy? (Name it in test-plan's own test_strategy_ref
           field.) What must it do to deviate from one of this strategy's defaults? Who may accept that
           deviation, by role rather than by name?
     GOOD  "A project adopts this strategy by naming it in its own test plan's test_strategy_ref field.
           Any deviation from this strategy's levels, types, or tooling is recorded with its reason in
           that plan's own Risk-Ranked Approach section. The program's QA Lead may accept a deviation
           after reviewing the stated reason; this strategy does not require sign-off above that role."
     WEAK  "Follow the strategy." (names no adoption mechanism, no deviation path, and no one who may
           accept a deviation)
     TRAP  Naming a required, named approver title for a deviation on the strength of a single
           directive-level source. The evidence this research found supports asking who may accept a
           deviation, not mandating a title; adding one anyway invents an approval step no program-level
           source this bundle read actually names. -->

{{inherit_or_deviate_statement}}

**Who may accept a deviation from this strategy:** {{who_may_accept_a_deviation}}

## Roles and Responsibilities Across Projects

<!-- WHAT  Who owns this document at the organization-or-program level, distinct from who executes
           testing on any one project inside it.
     WHY   This recurs in every published program strategy this bundle's research read, independent of
           how each document is otherwise structured. Who owns the document is answered differently
           across the sources, and this section should show the disagreement rather than flatten it: one
           vendor ties ownership to "QA managers, test leaders, and strategic teams", while another source
           instead states, "Project Manager prepares Test Strategy." That directly contradicts the first. A
           job posting for a program-scoped role ties the artifact to that role instead, naming someone
           who will "Manage program testing activities that are correctly prioritised to deliver outcomes
           that align to the Departments priorities." The audience is wider than the owners: a
           practitioner source names "Project Sponsors, Business SMEs" among those this kind of document
           is written for, alongside several delivery teams. Deep dive: test-strategy_companion.md
           section 3 (Anatomy > Roles and Responsibilities Across Projects).
     ASK   Who owns this document, separately from who is accountable for testing on any one project
           inside it? The sources this research read do not agree those are the same role; which is it
           here? Who else needs to read this document even though they do not own or execute against it?
     PRIORITY  Name the document's own owner first. Every other row, including who executes testing on
           any one project, depends on knowing who actually approves a change to the document itself.
     ROW HINT  A good row names a role and the actual person or team holding it, and states what that
           role does with respect to this document, not to any one project's own testing. A weak row
           names neither a holder nor a responsibility.
     GOOD  | Program-level strategy owner | VP of Engineering, Granite Peak Utilities | Owns this
           document; approves changes (see Governance and Policy Alignment above) |
     WEAK  | QA | | (no holder, no stated responsibility)
     TRAP  Naming only the roles that execute testing on one project and omitting the person or group who
           owns this document itself across every project in scope. The sources disagree on whether those
           are the same role; this table should not quietly assume they are. -->

| Role | Holder | Responsibility |
|---|---|---|
| {{role_name}} | {{role_holder}} | {{role_responsibility}} |

## Review Trigger

<!-- WHAT  Named conditions, not a calendar reminder, that tell this organization or program the
           strategy has gone stale, each with a named owner and what that owner does about it.
     WHY   The standing-standards family this bundle belongs to requires every member to carry this
           mechanism, because every member fails the same quiet way: by drifting out of date while
           everyone still believes it is current. No source read for this bundle names who notices any of
           these conditions; the owner column is this family's own obligation, not a sourced fact. One
           vendor states plainly, "There is no universal review schedule." Where a source names an annual
           or semi-annual clause instead, that is one described governance model, not a measured norm
           across the field, and it belongs here only as a floor layered under a named condition, never as
           a calendar rewrite of this section's own rule. Candidate conditions this research supports: a
           project's own test plan records a deviation from this strategy, which is this strategy's own
           inheritance mechanism signalling a possible drift; the test policy this strategy aligns with
           changes; a test summary report shows a strategy-mandated level or type was skipped on a real
           release; or a new test level, tool, or environment is adopted across more than one project
           without this document being revised to say so. Deep dive: test-strategy_companion.md section 3
           (Anatomy > Review Trigger).
     ASK   What concrete, recurring condition would tell us this strategy is out of date: a recorded
           deviation, a changed policy, a skipped mandated level, or a tool or environment adopted without
           this document changing? Who actually notices each one, by name or by role? What do they do
           about it once they notice?
     PRIORITY  List the deviation-recording condition first. It is this strategy's own built-in signal,
           surfaced by test-plan's own test_strategy_ref field and Risk-Ranked Approach section, so it
           needs no new instrumentation to start working.
     ROW HINT  A good row names a condition someone could actually notice without being told to look, a
           named owner, and what that owner does about it. A weak row is a calendar date with no
           condition and no stated action.
     GOOD  | A project's own test plan records a deviation from this strategy's levels, types, or tooling |
           Program QA Lead | Reviews whether the deviation reveals the strategy itself is now wrong, not
           just that one project's own case |
     WEAK  | Reviewed annually | | (a calendar reminder; it fires whether or not anything is actually
           wrong, and names no owner's action)
     TRAP  Writing only a calendar reminder. One vendor source states plainly that no universal review
           schedule exists; where an annual clause is genuinely useful, write it as a floor under a named
           condition in this table, never as a substitute for one. -->

| Condition | Owner | What They Do About It |
|---|---|---|
| {{review_trigger_condition}} | {{review_trigger_owner}} | {{review_trigger_action}} |
