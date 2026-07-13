# Build delivery-docs first, starting with the PRD bundle

Status: accepted (decided 2026-06-29; transcribed 2026-07-11 from strategy brief section 5; ratified 2026-07-12)
Date: 2026-06-29
Deciders: jprisant

## Context and problem statement

With 205 catalog types and a must-have tier of roughly 28, the first family choice sets the pattern every later bundle follows, and determines whether the pm-skills seam is exercised from day one or remains theoretical.

## Considered options

* Option A: `delivery-docs` (PRD, user stories, acceptance criteria, release notes) first, PRD as the reference bundle.
* Option B: start where pm-skills has gaps (net-new coverage) rather than where it already pairs.
* Option C: coverage-first breadth across the must-have tier (rejected in the strategy brief as "the seductive wrong answer").

## Decision outcome

Chosen option: A. Its `pairs_with` targets already existed as live pm-skills skills (deliver-prd, deliver-user-stories, deliver-acceptance-criteria, deliver-release-notes), so the compatibility seam was proven real rather than asserted, and the four artifacts form a natural traceable chain (PRD to stories to criteria to release note) that one shared worked example can demonstrate.

### Consequences

* Good: the seam validated on day one; the example chain became a differentiator; the family completed 2026-06-30.
* Accepted risk: early bundles partly duplicate templates bundled inside pm-skills skills, so their marginal value is "richer, sized, governed versions" rather than net-new coverage; accepted as the deliberate deepen-then-broaden posture.
