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

## Quality rubric (self-grade before sprint)

- [ ] Each criterion is an observable outcome (what the user sees), not implementation detail.
- [ ] Each criterion is verifiable: you can mark it pass or fail.
- [ ] The unhappy paths are covered, not just the happy one.
- [ ] Nothing here duplicates the team's Definition of Done.
- [ ] Story-specific non-functional bars (speed, accessibility) are stated, not assumed.
- [ ] Each Given/When/Then scenario tests one behavior; "When" is a single action.
- [ ] Out of scope is stated, so omissions are not mistaken for decisions.
- [ ] All guidance comments deleted; no placeholders remain.

## Named anti-patterns (the usual wrecks)

1. **Implementation, not behavior.** "Uses a Redis cache" instead of "loads in under one second."
2. **Duplicating the Definition of Done.** Restating universal checks as story criteria.
3. **Happy path only.** No edge or negative cases.
4. **Unverifiable criteria.** Conditions you cannot mark pass or fail.
5. **Mega-scenario.** One Given/When/Then with many "And" steps testing several behaviors.
6. **Criteria as afterthought.** Written after the code, describing what was built, not what was needed.
