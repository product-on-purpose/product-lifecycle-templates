# Guide: Test Strategy (operator card)

The short card. Why the document is shaped this way, and the argument behind every rule here, is in
[`test-strategy_companion.md`](test-strategy_companion.md). A fully worked instance is
[`test-strategy_example.md`](test-strategy_example.md).

## When to use

- More than one project inside one organization or program needs the same testing defaults, and you want
  those defaults written down once rather than argued out fresh inside every project's own test plan.
- You need a single place that states which levels or types are mandatory because of a law, a regulation,
  a contract, or a past incident, rather than a preference, so that obligation does not quietly get
  forgotten from one project to the next.
- A project's own test plan already exists, or is about to be written, and needs a standing document to
  name in its `test_strategy_ref` field, inheriting this strategy's defaults rather than inventing its own.
- You want a single, named answer to who owns testing decisions at the organization or program level,
  kept distinct from who actually executes testing on any one project inside that scope.
- You want the standing document itself to name the specific events that would make it wrong, a recorded
  deviation, a changed test policy, a skipped mandated type, a new tool adopted without the document
  changing, each paired with a named owner, rather than a calendar date nobody reads before renewing it.
- Nobody has written down who approves a change to this organization's or program's testing defaults, and
  you want that named rather than left to be assumed by whoever happens to be in the room.

## When NOT to use

- **You are planning testing for one project, release, or effort.** That is `test-plan`, scoped to a
  single effort. It already carries the seam: its own `test_strategy_ref` field names this strategy, and
  its Risk-Ranked Approach section records any deviation with the reason. This document must not restate
  either of `test-plan`'s own sections.
- **You need to coordinate multiple test levels or test types for one project.** That is a master test
  plan, which ISTQB defines directly as "a test plan that is used to coordinate multiple test levels or
  test types." A master test plan sits beneath this strategy, coordinating one project's own levels, not
  above it.
- **You want a standard every increment of work is judged against, in any discipline, on a cadence.** That
  is a Definition of Done. Both are standing, both are agreed once and consulted repeatedly rather than
  authored per increment, but a Definition of Done governs whether an increment is finished and this
  document governs the testing approach a project either follows or states a reasoned deviation from. A
  team may hold both at once.
- **You need the entry-side standard for when a backlog item is ready to start.** That is a Definition of
  Ready. It governs when work may enter a sprint; this document governs how testing is approached once
  work is already underway. Neither gates the other.
- **You are checking one service's standing fitness to be handed off and run day to day.** That is a
  production readiness review. Its own criteria may ask whether a project's testing conformed to this
  strategy, where one exists, without this bundle restating any of that review's own criteria.
- **You are specifying one effort's own test cases, reporting its own test run, or filing a bug.** Those
  are `qa-docs` family members (`test-case`, `test-summary-report`, `bug-report`), each authored per
  increment and finished at a stage. This document is none of those three things: it is not authored per
  increment and is not finished at any one stage.
- **You mean "test strategy" as a per-effort thinking tool rather than a standing, cross-project
  document.** A heuristic model meant to be reworked for one effort, or a set of testing quadrants rebuilt
  every iteration, is a real and useful practice, but it is not this bundle's subject: this bundle covers
  only the standing sense that spans more than one project.

## Pick a variant

This bundle ships one size, lean, and there is no second, heavier variant to choose between. That is a
deliberate call, not an unfinished one: no source read for this bundle describes a short form and a long
form of a test strategy, and the sources that address size at all argue against a second, heavier weight
rather than for one. BrowserStack names "Overdocumenting Everything" as one of its own six named failure
modes for this kind of document: "Excessively detailed documents increase maintenance effort and are
rarely followed during actual testing." Mirjana Kolarov's own conference abstract names the image most
readers already hold, "A big document of 40+ pages with ton of theory, no one reads and is not up to
date," and answers it by arguing that the document must be tailored and short, not by arguing for a second,
bigger shape. A `full` variant here would model the exact failure this bundle warns against.

If your situation feels like it needs more sections than the seven this bundle ships, take that feeling
seriously, but read it as a sign that this organization or program may need more than one strategy, the
way one vendor's own glossary cautions an organization can hold more than one for markedly different
project contexts, rather than as a reason to look for a heavier template. See
[`test-strategy_companion.md` section 4](test-strategy_companion.md#4-variants-and-sizing) for the full
reasoning.

## Quality rubric (self-grade)

Score each section 0, 1 or 2. Below 10 out of 14 and a project team reading this strategy cannot tell what
it is actually bound to follow, and falls back to inventing its own testing defaults project by project,
which is the exact failure a standing, organization-or-program strategy exists to prevent.

| # | Criterion | 0 | 1 | 2 |
|---|---|---|---|---|
| 1 | **Scope is bounded** | No organization or program is named, or the scope reads as though it covers every project with no stated boundary | An organization or program is named and the projects it binds are stated, but nothing is named as explicitly out of scope | The organization or program is named, the projects it binds are stated, and a reader can point at the named excluded program, project, or release train and say why it is excluded |
| 2 | **Mandatory rows are sourced** | The table names levels or types with no default-or-mandatory distinction, or a mandatory row names no reason | Some rows distinguish default from mandatory, but a legal, regulatory, or contractual obligation that applies to this organization is missing, or a row is left "to be defined" | Every row states whether it is a default or mandatory, and every mandatory row names the law, regulation, contract, or past incident behind it, so a project reading it knows this is not a preference |
| 3 | **Tooling and data rule** | No default tools or environments are named, or no rule is given for real or production-derived data in test | Default tools or environments are named and a rule against production data exists, but the rule states no documented path for when synthetic data cannot do the job | Default tools and environments are named, the rule for real or production-derived data is stated, and a documented exception path, who decides and what gets written down, is stated for when synthetic data cannot suffice |
| 4 | **Governance and approval** | No relationship to a test policy is stated, and no one is named who approves a change to this strategy itself | One of the two is stated, but the approver named is a vague noun rather than a role, function, or committee a reader could actually go contact | The relationship to any test policy, including its stated absence, is given, and the approver of a change to this strategy is a specific role, function, or committee someone could actually reach |
| 5 | **Inheritance and deviation** | No statement of how a project adopts this strategy, or of what it must do to deviate from it | Adoption is named, but a deviation is described without saying who may accept it | A project's adoption mechanism is named, a deviation's required reason is stated, and the role that may accept a deviation is named, without inventing a mandated approver title no program-level source actually supports |
| 6 | **Ownership is distinct** | No role owns this document at the organization-or-program level, or the table only names who executes testing on one project | An owner is named, but the table does not distinguish that role from who executes testing on any one project in scope | A document owner at the organization-or-program level is named and distinguished from per-project testing roles, and a reader can point at a second named audience, someone who reads this document but neither owns nor executes against it, and say what they use it for |
| 7 | **Review Trigger names conditions** | Only a calendar date is named, or the table is blank | At least one condition is named, but a row carries no owner, or a periodic clause stands in as the entire trigger rather than a floor under a condition | Every row names a concrete condition someone could notice without being told to look, a named owner, and what that owner does about it, with any periodic clause present only as a floor layered under a condition |

The test behind every cell above: could someone satisfy it without improving the document? A row that
counted rows, obligations, or conditions would reward padding a table. Every cell instead asks whether a
specific, checkable fact is on the page, the kind a second reader, not the author, could point at.

## Named anti-patterns (the usual wrecks)

1. **Treating the strategy and the plan as the same document.** BrowserStack names this directly: "Using
   test plan and test strategy interchangeably creates confusion around testing scope, execution, and
   ownership." This document and `test-plan` are deliberately separate; collapsing them removes the exact
   distinction the inheritance mechanism depends on.
2. **One document straining to cover every kind of project the organization runs.** imbus's own vendor
   glossary caution applies directly: an organization can hold more than one organizational test strategy
   "to cover markedly different project contexts." A single sprawling document trying to fit every project
   type is a sign it should split, not a sign it is thorough.
3. **Overdocumenting into shelfware.** Mirjana Kolarov's own conference abstract names the image most
   readers already hold: "A big document of 40+ pages with ton of theory, no one reads and is not up to
   date." BrowserStack names the same failure on its own list, "Overdocumenting Everything": "Excessively
   detailed documents increase maintenance effort and are rarely followed during actual testing."
4. **Copying a strategy unchanged between projects or organizations.** TestRail warns against a strategy
   "copied unchanged between projects." A strategy that was never tailored to this organization is not
   doing this document's job, whatever it happens to be titled.
5. **Leaving a binding legal or regulatory obligation blank.** The UK Office of the Public Guardian's own
   published baseline leaves a shared field unanswered, "Accessibility To be defined," beside the GDS Way's
   own statement that the same obligation is a legal requirement. One instance is not a measured rate of
   this failure, but it is a real, preventable gap, and this bundle's Test Levels and Types table exists
   partly to catch it before it ships blank.
6. **Inventing a named approver no source actually supports.** The one source naming a required, titled
   approver for a deviation is a directive governing every test plan inside one agency, not a standing
   test strategy. Naming a mandated approval title for a deviation here manufactures a step the published
   program-level strategies never describe.
7. **A review trigger that is only a calendar date.** TestRail states plainly, "There is no
   universal review schedule." Where an annual or semi-annual clause is genuinely useful, it belongs as a
   floor layered under a named condition, never as the whole mechanism; a trigger that only says "reviewed
   annually" fires whether or not anything is actually wrong, and names no owner's action.
8. **Missing or flattened ownership.** BrowserStack names "Missing Clear Ownership" on its own list:
   "Without defined ownership, testing responsibilities and reporting processes become inconsistent across
   teams." The sources this bundle read disagree on whether the owner is a QA function, a committee, or a
   project manager; flattening that live disagreement into an assumed single answer, rather than picking
   the shape that matches how this organization already makes its other standing decisions, is its own
   failure.

## Pairing with your process

This bundle ships in the `standing-standards` family alongside `definition-of-done`, `definition-of-ready`,
`runbook`, `launch-coordination-checklist`, `production-readiness-review` and `business-continuity-plan`,
as a **foundation**: a standard every project's own test plan is judged against, or states a reasoned
deviation from, rather than an instrument executed under time pressure. `test-plan`'s own
`test_strategy_ref` field is the seam: a project names this strategy there and inherits its defaults,
recording any deviation inside its own Risk-Ranked Approach section with the reason. Update this file
when the organization's or program's own testing defaults actually change, not every time one project's
plan records a single deviation; a recorded deviation is this strategy's own signal to review, under the
Review Trigger above, not by itself a reason to rewrite the strategy on the spot.
