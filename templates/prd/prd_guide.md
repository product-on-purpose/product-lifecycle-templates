# Guide: PRD (operator card)

Fast reference for using the PRD bundle. For the full reasoning, history, and sources, read
[`prd_companion.md`](prd_companion.md).

## When to use

- After the problem and a solution direction are understood, before engineering starts building.
- When more than one person or team must share one understanding of what to build and why.
- When you need a durable answer to "what are we building, for whom, how do we know it worked."

## When NOT to use

- The problem is still unframed or unvalidated. Do discovery first; a PRD assumes an agreed problem.
- You only need work broken into sprint tickets. Use user stories and acceptance criteria instead.
- You have a high-fidelity prototype that already communicates the experience. Keep only a lean PRD
  for the why, metrics, scope, and open questions; let the prototype carry the rest.
- You are inventing a genuinely new product. Consider an Amazon-style PR/FAQ first, then a PRD.

## Pick a variant

- **Lean** (default): single feature, spike, early idea, solo or small team. The one-pager.
- **Full**: multiple teams, external dependencies, regulated or safety-relevant work, or a launch
  with real downside. Grow lean into full by adding sections; never reorder the shared ones.

## Quality rubric (self-grade before sharing)

- [ ] The problem is stated from the user's point of view, with evidence it is real and worth solving now.
- [ ] The problem section is meatier than the solution section.
- [ ] Goals are outcomes, ideally measurable; non-goals are explicit.
- [ ] Target user is specific, not "all users."
- [ ] There is a primary success metric and a guardrail metric, defined before build.
- [ ] Open questions are surfaced, each with an owner and a needed-by date.
- [ ] (Full) Error, empty, and edge states are covered, not just the happy path.
- [ ] (Full) Functional requirements are prioritized; dependencies and risks have owners.
- [ ] No load-bearing decision is buried in the appendix.
- [ ] Every guidance comment has been deleted; no placeholders remain.

## Named anti-patterns (the usual wrecks)

1. **Feature-first, problem-thin.** Opens with the solution; treats the problem as one line. The most common and most damaging failure.
2. **No non-goals.** The silent entry point for scope creep.
3. **Spec instead of discovery.** A detailed PRD for a solution nobody validated; it looks rigorous and skips the step that decides whether to build at all.
4. **Frozen document.** Signed once, never updated, drifts from reality, stops being trusted.
5. **Happy-path only.** Empty, loading, and error states left for engineering to invent.
6. **Metrics defined after results.** Guarantees a flattering read; define them up front with a guardrail.
