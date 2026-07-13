# Companion: Acceptance Criteria

> The deep explainer for the Acceptance Criteria bundle. Read this to understand what acceptance
> criteria are, where the forms came from, how they differ from a Definition of Done, and where teams
> disagree. The short operator card is [`acceptance-criteria_guide.md`](acceptance-criteria_guide.md);
> a worked instance is [`acceptance-criteria_example.md`](acceptance-criteria_example.md). Inline
> citations like [[1]](#ref-1) resolve to the [References](#references), tagged by source reliability.

---

## 1. Orientation

Acceptance criteria (AC) are **the conditions a user story must satisfy to be accepted as done, stated
as observable outcomes from the user's point of view** [[2]](#ref-2)[[3]](#ref-3). They are the "Confirmation" in Ron
Jeffries' three C's of a user story: the part that turns a conversation into something verifiable [[3]](#ref-3).

AC answer one question precisely: *how will we know this specific story is done and correct?* They make
"done" a shared fact rather than an interpretation, and they give QA and engineering a concrete target
before work starts [[2]](#ref-2)[[4]](#ref-4).

**At a glance**
- They are **per-story** and **functional**: what this story must do for its user [[2]](#ref-2).
- They come in two dominant forms: **rule-oriented** (a checklist of conditions) and **scenario-oriented**
  (Given/When/Then), and the two mix freely [[4]](#ref-4)[[7]](#ref-7).
- They are written from the user's perspective, describing *what*, not *how* [[2]](#ref-2).
- They are distinct from the **Definition of Done**, which is team-wide and applies to every increment
  (see [§6](#6-debates-and-contested-boundaries)) [[2]](#ref-2)[[6]](#ref-6).

---

## 2. Origins and evolution

Acceptance criteria grew out of two lineages that converged.

The first is the **user story** itself. From the start, a story was incomplete without its Confirmation,
the tests that say it is done; Jeffries named this the third C in 2001, and Cohn described the same idea
as a story's "conditions of satisfaction" [[3]](#ref-3). In this lineage, AC are simply the testable half of a
good story.

The second is **Behavior-Driven Development (BDD)**. Dan North created BDD in 2006 to move testing
language away from developer-centric assertions and toward business-readable descriptions of behavior
[[1]](#ref-1). In 2007 the **Gherkin** syntax formalized the **Given / When / Then** structure (precondition,
trigger, outcome), giving AC a precise, executable shape that both humans and tools could read [[1]](#ref-1)[[5]](#ref-5).
Given/When/Then turned acceptance criteria from a prose checklist into structured scenarios that could
double as automated tests [[4]](#ref-4)[[5]](#ref-5).

The result today is a spectrum: from a short rule checklist on a story card, through structured
Given/When/Then scenarios, to fully executable Gherkin feature files driving automated acceptance tests.

---

## 3. Anatomy (section by section)

The lean checklist carries the starred sections; the full variant adds scenarios, edge cases, and
non-functional conditions.

**Story reference (lean).** Which story these criteria belong to. *Why:* AC are meaningless without the
story they gate; "accepted into what" must be unambiguous. *Beginner trap:* free-floating criteria with
no parent story.

**Acceptance criteria (lean).** The rule-based conditions, as a checklist of observable, pass/fail
outcomes [[2]](#ref-2)[[7]](#ref-7). *Why:* discrete rules ("must reject an empty name") are clearest as a list. *Expert
note:* keep each criterion to a single, verifiable claim; a criterion you cannot mark pass or fail is
not finished.

**Scenarios, Given/When/Then (full).** Behavior expressed as context, action, outcome [[1]](#ref-1)[[5]](#ref-5). *Why:* flows
are clearer as scenarios than as rules. *Beginner trap:* one scenario with ten "And" steps; split it so
each scenario is one behavior [[5]](#ref-5). *Expert note:* Given/When/Then maps to precondition/trigger/outcome;
keep "When" to a single action, or the scenario is testing two things [[1]](#ref-1).

**Edge cases and negative paths (full).** The unhappy paths: empty input, permission denied, conflict,
timeout, missing data. *Why:* most production defects live here, not on the happy path. *Expert note:*
the negative criteria are often more valuable than the positive ones, and the most commonly omitted.

**Non-functional criteria (full).** Story-specific quality gates: performance, accessibility, security,
privacy thresholds. *Why:* a story can pass every functional check and still be unacceptable if it is
slow or inaccessible. *Expert note:* keep these story-specific; universal quality bars belong in the
Definition of Done, not here [[2]](#ref-2)[[6]](#ref-6).

**Out of scope and notes (lean).** What the criteria deliberately do not cover, plus assumptions. *Why:*
it lets a reviewer tell an omission from a decision.

---

## 4. Variants and sizing

The two variants differ by how much **behavioral precision** the story needs.

- **Lean.** A rule checklist plus story reference and scope. The right default for straightforward
  stories where a handful of pass/fail rules say everything.
- **Full.** Adds Given/When/Then scenarios, explicit edge cases, and non-functional criteria. Use it for
  behavior-heavy, risky, or integration-sensitive stories, and where AC will seed automated tests.

The nesting rule holds: the lean checklist's sections are a strict subset of the full document's, so a
checklist can grow into scenario-based criteria in place. Default to the checklist; reach for scenarios
when a flow is genuinely easier to read as Given/When/Then than as rules [[7]](#ref-7).

---

## 5. Methodology lineage

- **XP / user stories.** AC are the story's Confirmation, the testable conditions of satisfaction [[3]](#ref-3).
- **Scrum.** AC gate the individual Product Backlog item; the Scrum Guide does not name "acceptance
  criteria" as such but relies on them implicitly through the backlog and the Definition of Done [[2]](#ref-2)[[6]](#ref-6).
- **BDD.** AC become Given/When/Then scenarios, often executable as Gherkin, blurring the line between a
  criterion and an automated acceptance test [[1]](#ref-1)[[4]](#ref-4)[[5]](#ref-5).
- **Traditional / regulated.** AC echo formal acceptance testing (UAT) and trace to requirements; the
  same intent, heavier ceremony [[8]](#ref-8).

---

## 6. Debates and contested boundaries

**Acceptance criteria vs Definition of Done.** The most important distinction to get right. AC are
**story-specific and functional** (what this story must do); the **Definition of Done is universal and
applies to every increment** (coded, reviewed, tested, documented, accessible) [[2]](#ref-2)[[6]](#ref-6). The Product Owner
typically owns AC; the development team owns the DoD, with the Product Owner having final say [[2]](#ref-2). AC are
written per story during refinement; the DoD is set once, up front, and revised rarely [[2]](#ref-2). A story is
truly done only when it meets **both** its AC and the DoD [[2]](#ref-2). *Recommendation:* never duplicate DoD
items into AC; if a check applies to every story, it belongs in the DoD.

**Rule-oriented vs scenario-oriented.** Some teams default to checklists, others to Given/When/Then [[7]](#ref-7).
Checklists are faster to write and read for discrete rules; scenarios are clearer for flows and convert
to automated tests [[4]](#ref-4)[[5]](#ref-5)[[7]](#ref-7). *Recommendation:* mix them, rules for conditions, scenarios for behavior;
do not force everything into Given/When/Then, which bloats simple criteria.

**How much detail.** Too little leaves "done" ambiguous; too much turns AC into an exhaustive spec that
duplicates the design. *Recommendation:* cover the behaviors that matter and the edges that bite, and
stop; AC are a quality gate, not a test plan.

**Who writes them.** Conventionally the Product Owner, but the strongest AC are written collaboratively
in refinement so engineering and QA can flag risky assumptions before the sprint [[2]](#ref-2). *Recommendation:*
draft as PO, refine as a team.

---

## 7. Anti-patterns and failure modes

- **Implementation, not behavior.** "Uses a Redis cache" instead of "results load in under one second."
  AC describe observable outcomes, not how they are achieved [[2]](#ref-2).
- **Duplicating the Definition of Done.** Restating universal checks (code reviewed, tests pass) as
  story AC; they belong in the DoD [[2]](#ref-2)[[6]](#ref-6).
- **Happy path only.** No edge or negative cases, so error behavior is invented during build.
- **Unverifiable criteria.** A condition that cannot be marked pass or fail, failing the story's
  "Testable" requirement.
- **Mega-scenario.** One Given/When/Then with many "And" steps testing several behaviors at once [[5]](#ref-5).
- **Criteria as afterthought.** Written after the code, so they describe what was built rather than what
  was needed.
- **No scope statement.** Silence on what is out of scope, so omissions read as decisions.

---

## 8. Relationships to other artifacts

- **Parent:** the user story (AC are its Confirmation) [[3]](#ref-3) and, above it, the PRD that sets scope.
- **Sibling / gate:** the Definition of Done (universal quality gate that AC sit alongside) [[2]](#ref-2)[[6]](#ref-6).
- **Downstream:** test cases and automated acceptance tests (AC, especially Given/When/Then, seed them)
  [[4]](#ref-4)[[5]](#ref-5), and User Acceptance Testing for business sign-off [[8]](#ref-8).

In this library Acceptance Criteria pairs with the `deliver-acceptance-criteria` skill and sits in the
`delivery-docs` family beside the `user-stories`, `prd`, and `release-notes` templates.

---

## 9. Adaptations

- **Solo or small team.** The lean checklist is usually enough; lean on conversation for the rest.
- **BDD / test-automation teams.** Use full scenarios in Given/When/Then so AC become executable Gherkin
  [[1]](#ref-1)[[5]](#ref-5).
- **Integration-heavy or risky stories.** Use the full variant and invest in edge cases and
  non-functional criteria, where the real risk sits.
- **Regulated contexts.** Tie AC to formal acceptance tests and requirement IDs so each accepted story
  traces to a controlled requirement and its verification [[8]](#ref-8).

---

## 10. Worked example

See [`acceptance-criteria_example.md`](acceptance-criteria_example.md) for full acceptance criteria for
the "set a default saved view" story from the user-stories example, combining a rule checklist,
Given/When/Then scenarios, explicit edge cases (a missing filter), and a non-functional criterion.

---

## References

Tagged by reliability: `[primary]` originating source or standards body; `[practitioner]` recognized
authority; `[vendor]` commercially motivated; `[reference]` consolidated secondary. Researched 2026-06-30.

<a id="ref-1"></a>[1] Dan North. "[Introducing BDD](https://dannorth.net/introducing-bdd/)," 2006; Gherkin and Given/When/Then, 2007. dannorth.net (accessed 2026-06-30). [primary]

<a id="ref-2"></a>[2] Scrum.org. "[What Is the Difference Between the Definition of Done and Acceptance Criteria?](https://www.scrum.org/resources/blog/what-difference-between-definition-done-and-acceptance-criteria)" scrum.org (accessed 2026-06-30). [primary]

<a id="ref-3"></a>[3] Ron Jeffries. "Card, Conversation, Confirmation," 2001; and Mike Cohn, "User Stories Applied," 2004 (conditions of satisfaction). [practitioner]

<a id="ref-4"></a>[4] Thoughtworks. "[Applying BDD acceptance criteria in user stories](https://www.thoughtworks.com/en-us/insights/blog/applying-bdd-acceptance-criteria-user-stories)." thoughtworks.com (accessed 2026-06-30). [practitioner]

<a id="ref-5"></a>[5] Cucumber / SmartBear. "[Gherkin Reference](https://cucumber.io/docs/gherkin/reference/)." cucumber.io (accessed 2026-06-30). [vendor]

<a id="ref-6"></a>[6] Ken Schwaber and Jeff Sutherland. "[The 2020 Scrum Guide](https://scrumguides.org/scrum-guide.html)" (Definition of Done commitment). scrumguides.org, 2020. [primary]

<a id="ref-7"></a>[7] Ranorex. "[When to Use Given-When-Then Acceptance Criteria](https://www.ranorex.com/blog/given-when-then-tests/)." ranorex.com (accessed 2026-06-30). [vendor]

<a id="ref-8"></a>[8] "[Master Catalog of Product Management and SDLC Document and Artifact Types](../../_local/initial-discovery/docs/deep-research_master-catalog.md)," entry 38 (Acceptance Criteria). Internal deep-research catalog, 2026. [internal]
