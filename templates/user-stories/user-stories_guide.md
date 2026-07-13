# Guide: User Story (operator card)

Fast reference for the User Story bundle. For the full reasoning, history, and sources, read
[`user-stories_companion.md`](user-stories_companion.md).

## When to use

- To express a unit of work from the user's point of view, ready for a backlog.
- When you want the work to stay a conversation, with detail emerging in refinement.
- When a team estimates and pulls work iteratively.

## When NOT to use

- You need the whole feature's scope, metrics, and non-goals. Use a PRD; stories implement it.
- You need exhaustive actor-system flows. Use a use-case specification.
- The "done" conditions are detailed enough to deserve their own artifact. Use acceptance criteria.

## Pick a variant

- **Lean** (default): a single story card (Story, Acceptance criteria, Notes). What you write most.
- **Full**: adds INVEST, estimate, and dependencies. For risky, cross-team, or must-size stories.
  Grow lean into full by adding sections; never reorder the shared ones.

## Quality rubric (INVEST, self-grade before refinement)

- [ ] **Independent**: not blocked by a sibling story.
- [ ] **Negotiable**: the how is open; only the need is fixed.
- [ ] **Valuable**: a user or customer would recognize the value.
- [ ] **Estimable**: the team can size it.
- [ ] **Small**: fits in one iteration.
- [ ] **Testable**: the acceptance criteria are verifiable.
- [ ] The "so that" clause states a real benefit, not a restatement of the goal.
- [ ] All guidance comments deleted; no placeholders remain.

## Named anti-patterns (the usual wrecks)

1. **The card is the spec.** Treating the one-liner as complete and skipping the conversation.
2. **UI task disguised as a story.** "As a user I want a dropdown" states a solution, not a goal.
3. **No "so that."** Dropping the benefit hides whether the work is worth doing.
4. **Too big.** A story that cannot fit an iteration; split it.
5. **Hidden dependencies.** Unlisted blockers that surface mid-sprint.
6. **Persona theater.** "As a user" everywhere, when naming the real situation would change the design
   (consider a job story instead).
