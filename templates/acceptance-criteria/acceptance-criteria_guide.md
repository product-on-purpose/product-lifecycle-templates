# Guide: Acceptance Criteria (operator card)

Fast reference for the Acceptance Criteria bundle. For the full reasoning, history, and sources, read
[`acceptance-criteria_companion.md`](acceptance-criteria_companion.md).

## When to use

- To define, before work starts, the conditions that confirm a specific story is done and correct.
- When QA and engineering need a concrete, shared target.
- When you want "done" to be a fact, not an interpretation.

## When NOT to use

- You need a universal, team-wide completion standard. That is the Definition of Done, not AC.
- You need whole-feature scope, metrics, and non-goals. Use a PRD.
- The story is so trivial a one-line note suffices. Do not manufacture ceremony.

## Pick a variant

- **Lean** (default): a rule checklist plus story reference and scope. For straightforward stories.
- **Full**: adds Given/When/Then scenarios, edge cases, and non-functional criteria. For behavior-heavy
  or risky stories, and when AC will seed automated tests. Grow lean into full by adding sections; never
  reorder the shared ones.

## The rubric

Score each 0, 1 or 2. **Under 10 out of 14 and "done" will be settled in the review meeting rather than
before the work started**, which is the one outcome this document exists to prevent.

**Which rows apply to what.** This bundle ships two variants, and one row grades a section that only the
full variant carries, so scoring lean against all seven would penalise the choice of variant rather than the
quality of the criteria.

| Variant | Rows that apply | Maximum | Score against |
|---|---|---|---|
| full | all 7 | 14 | **10** |
| lean | 1-5, 7 (it carries no Scenarios section) | 12 | **9** |

Both thresholds sit above two-thirds of the available points; neither is a bare pass mark.

| # | Criterion | 0 | 1 | 2 |
|---|---|---|---|---|
| 1 | **Observable outcome, not implementation** | Criteria name components, technologies or internal mechanisms | Mostly behavioural, but at least one criterion says how rather than what | Every criterion states something a user could watch happen, and none names a technology |
| 2 | **Verifiable pass or fail** | Criteria rest on words like "fast", "intuitive" or "robust" with no bar | Verifiable in principle, but the tester has to choose the bar themselves | A tester who has never met the author can mark every criterion pass or fail without asking anyone |
| 3 | **Unhappy paths covered** | Happy path only | One or two error cases, chosen because they were easy to think of | The failure this story is most likely to hit in production is named, with what should happen when it does |
| 4 | **No overlap with the Definition of Done** | Restates universal checks such as tests passing or code reviewed | Mostly story-specific, with one or two DoD items carried in | Every criterion is true of this story and would be meaningless pasted onto the next one |
| 5 | **Story-specific non-functional bars** | A bar plausibly applies and none is stated | A bar is mentioned without a number or a named standard | A number or a named standard scoped to this story, or an explicit statement that none applies and why |
| 6 | **One behaviour per scenario** *(full only)* | One scenario chains several behaviours through repeated "And" steps | Scenarios are separated, but at least one "When" contains more than one action | Every scenario tests one behaviour and its "When" is a single action |
| 7 | **Out of scope is stated** | No scope statement, so a reader cannot tell an omission from a decision | Scope stated in general terms | Names something a reader would reasonably have expected here and says it is deliberately excluded |

## Named anti-patterns (the usual wrecks)

1. **Implementation, not behavior.** "Uses a Redis cache" instead of "loads in under one second."
2. **Duplicating the Definition of Done.** Restating universal checks as story criteria.
3. **Happy path only.** No edge or negative cases.
4. **Unverifiable criteria.** Conditions you cannot mark pass or fail.
5. **Mega-scenario.** One Given/When/Then with many "And" steps testing several behaviors.
6. **Criteria as afterthought.** Written after the code, describing what was built, not what was needed.
