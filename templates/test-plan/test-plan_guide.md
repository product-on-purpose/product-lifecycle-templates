# Guide: Test Plan (operator card)

The short card. Why the document is shaped this way, and the argument behind every rule here, is in
[`test-plan_companion.md`](test-plan_companion.md). A fully worked instance is
[`test-plan_example.md`](test-plan_example.md).

## When to use

- A release or feature is about to be verified and more than one person needs to know what is covered.
- Testing spans more than one team, vendor or specialism, so coverage assumptions need to be written down
  rather than assumed.
- There is a gate inside the cycle (a security review, a compliance sign-off, a staged rollout) and someone
  has to decide in advance what passing it means.
- The context is regulated or audited and the plan is part of the evidence.
- Coverage is going to be argued about afterwards, and you would rather have the argument now, cheaply.

## When NOT to use

- **The plan would decide nothing.** One person, one afternoon, one obvious feature. Write the two entry and
  exit conditions in the ticket and move on.
- **You need a test case.** One executable verification with steps, data and an expected result is a
  different artifact. The plan schedules cases; it does not contain them.
- **You need a test report.** The plan is written before and is prospective. Results, defect counts and the
  verdict belong in a report written after.
- **You need a definition of done.** A DoD is a standing team invariant applied to every increment. A test
  plan is scoped to one release.
- **Your tool already has a "test plan".** It probably means an execution container: a grouping of suites and
  runs with a name and a date range. That is a complement to this document, not a substitute (see below).
- **Continuous delivery with no discrete release.** Do not write one plan per deploy. Write one standing plan
  per product area and revise it in place.

## Plan, strategy, case, or report? (the question people actually have)

| You want to say | Write |
|---|---|
| How this organization tests, in general, across projects | A **test strategy** (standing, rarely changes) |
| What we are testing this time, how deeply, and when we are done | A **test plan** (this template) |
| The exact steps and expected result for one behavior | A **test case** |
| What we found, and whether we are shipping | A **test report** |

Two honest notes. **The plan/strategy line is genuinely unsettled**: the certification bodies put strategy at
the organization or programme level, plenty of teams carry it as a section inside the plan, and practitioners
openly disagree about which is written first. If your organization has a standing strategy, say in one line
that this plan inherits from it. If it does not, your Risk-Ranked Approach section **is** your strategy for
this release, and that is a legitimate answer rather than a gap.

**And the tool trap is real.** When Azure Test Plans, TestRail, Xray, Zephyr or qTest says "test plan", it
means a container for suites, runs and configurations. Those tools do not require an approach, a risk ranking
or an exit criterion. Teams that believe the tool replaced the document end up with an execution container and
no recorded thinking. Keep both: the narrative here, the execution there.

## Pick a variant

**Lean (five sections)** is the default. Scope and Non-Scope, Risk-Ranked Approach, Entry and Exit Criteria,
Environment/Data/Ownership, Schedule and Deliverables. One team, one feature or release, a page or two,
revised in place.

**Full (nine sections)** adds Test Levels and Types, Suspension and Resumption, Risks to the Test Effort, and
Approvals and Change Control. Use it when at least one of these is true:

- the work is regulated or audited, and completeness is a compliance requirement;
- more than one team or vendor is testing the same release;
- there is a formal gate mid-cycle that can stop the work;
- your process requires an approved, version-controlled artifact.

The test for adding a section is whether its absence would change anything. If it would not, leave it out.
Every lean heading appears in full unchanged, so growing is additive and you never rewrite what was agreed.

## Quality rubric (self-grade)

Score each 0, 1 or 2. Under 12 out of 18 and the plan will not survive contact with the release.

| # | Criterion | 0 | 1 | 2 |
|---|---|---|---|---|
| 1 | **Non-scope is explicit** | Nothing excluded | Exclusions listed | Exclusions listed with a reason each, and agreed by a named person |
| 2 | **Risk ranking is real** | No ranking, or everything is High | Tiers assigned | Tiers assigned with a stated reason, and coverage depth differs by tier |
| 3 | **Order follows risk** | No order given | Order given | Highest-risk areas are scheduled first, visibly |
| 4 | **Criteria are checkable** | Adjectives ("ready", "complete") | Some measurable | Every criterion is a number, a state, or a named artifact |
| 5 | **Exit criteria resist gaming** | Pass rate alone | Pass rate plus something | Coverage-of-risk criterion plus a severity rule plus a named agreement with a date |
| 6 | **Owners are people** | No owners | Teams named | One named individual per area, and per risk |
| 7 | **Risks are separated** | One merged list | Both present, mixed | Product risk shapes coverage; risk to the effort is separate with contingencies |
| 8 | **Test data is named** | Not mentioned | Mentioned generally | Specific data for the negative and boundary cases, with who creates it and when |
| 9 | **It would be read** | Over ten pages of prose | Long but skimmable | Short enough that the team actually reads it, and every section decides something |

Criterion 9 is the one people argue with and the one that matters most. A plan nobody reads is not a safety
net.

## Named anti-patterns (the usual wrecks)

1. **The plan nobody reads.** Written for the kickoff, filed, never reopened. The tell: no decision in the
   last month traces back to it. Fix by cutting until it is worth reading.
2. **Completeness theater.** Every heading filled, nothing decided, because the template demanded a heading.
   A document can satisfy every required field and still say nothing. Fix by deleting sections that decide
   nothing.
3. **Adjective criteria.** "Environment is ready", "quality is acceptable". Unfalsifiable, therefore not
   criteria. Fix with a number, a state or a named artifact.
4. **Pass-rate exit.** "95 percent pass" as the only gate, satisfiable by writing more trivial tests, and
   able to hide one catastrophic failure inside a comfortable percentage. Fix by pairing it with risk
   coverage and a severity rule.
5. **The merged risk list.** Product risk and project risk in one table, so neither drives anything. Fix by
   splitting them: one shapes coverage, the other shapes the schedule.
6. **The scope with no non-scope.** Nothing excluded, so nothing can be found missing, and the argument gets
   held after the release instead of before it. Fix by writing the exclusions and getting them agreed.
7. **The plan that became a tracker.** Results and status columns creep in and the prospective document turns
   retrospective. Fix by keeping execution state in the tool and the verdict in the report.

## Pairing with a skill

`pairs_with: [deliver-edge-cases]`. There is **no testing or QA skill** in the `pm-skills` library: none of
its 68 skills produces a test plan, a test case or a bug report (recorded as finding EC-4 in the repository's
`STATE.md`). The one honest pairing is `deliver-edge-cases`: run it first and feed its edge-case catalog into
the Risk-Ranked Approach section. See companion section 8 for why the two fit together. Everything else in
this template is filled by hand.
