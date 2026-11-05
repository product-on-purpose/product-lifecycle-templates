---
status: accepted
date: 2026-11-05
decision-makers: [jprisant]
consulted: [claude]
---

# `product-opportunity-assessment` clears the admission test and does not ship: the lean business case already does its job

## TL;DR

- **Decision.** `product-opportunity-assessment` (catalog entry 208, issue #312) **does not ship**, for now. The
  `business-case` guide gains a paragraph that points a new-product case at Marty Cagan's questions.
- **Why.** The lean `business-case` already decides whether an idea is worth pursuing, on the same cadence and in
  the same family. What the candidate adds is a set of questions, and a guide paragraph can supply those.
- **Who loses.** A reader who wants a ten-question screen as a fixed template. Market size has no prompt in any
  shipped template.
- **Status:** accepted 2026-11-05. The maintainer read the recommendation and ruled: "I guess decline this for
  now." The reopening conditions below are what "for now" means.

## Context and Problem Statement

Admission sweep 7 recommended parking the type on 2026-10-29, pending one side-by-side read against the lean
business case. That read ran on 2026-11-04 and widened its frame, because `lean-canvas` landed the day after the
sweep. The maintainer supplied *Inspired* (2nd edition) on 2026-11-05, and chapter 35 was then read directly.

## Decision Drivers

- **Admission and the build decision are separate questions**
  ([ADR 0064 (deployment plan declined)](0064-deployment-plan-is-declined.md)).
- **Check 4 asks whether a built bundle already does the candidate's job**, which is a different test from whether
  any bundle holds all the same content.
- **Build order is the maintainer's preference**
  ([ADR 0041](0041-maintainer-preference-sets-the-build-order.md)), so this ruling needs no further argument, and
  this record states the reasoning for a later reader.

## Considered Options

1. **Decline, with a guide paragraph.** Chosen.
2. **Park, with the same paragraph, leaving the issue open.** This is the #298 (opportunity statement) outcome. It
   keeps one more open row with no event that would move it.
3. **Admit as a one-size type in `discovery-docs`.** It would pass on content, but its guide would have to explain
   why it is not a lean business case.
4. **A format of `business-case`.** A shape with no comparison of options contradicts the bundle's own guide, which
   calls a case with no alternative "a proposal wearing a bigger name".

## Decision Outcome

**Chosen: option 1.**

### Admission clears, and the record says so

[Cagan's SVPG page](https://svpg.com/assessing-product-opportunities/), dated December 13, 2006, publishes the ten
questions, and it calls the assessment "an extremely important responsibility of the product manager". The sweep
judged checks 1, 3 and 5 as passes, and this record does not reopen them.

### Check 4 fails on the job, and passes on the content (POSITION)

**On content, no single bundle holds the ten questions.** The lean business case directly holds four (the problem,
who has it, why now, the recommendation) and partly holds two. Across all shipped bundles, eight are held, go-to-market
is partly held, and market size is held nowhere.

**On the job, the lean business case already does this.** Its guide says lean exists "to get agreement that an idea is
worth exploring further". Cagan's purpose is to stop poor opportunities early. Both are written once, for one decision,
in `discovery-docs`. [ADR 0083 (lean canvas joins strategy-docs)](0083-lean-canvas-joins-strategy-docs-as-a-seventh-member.md)
admitted the lean canvas on a combination test, but that canvas also differs in its job and its cadence, and this
candidate differs in neither.

### What chapter 35 adds

*Inspired* (2nd edition, 2017), chapter 35, presents an opportunity assessment as four questions: the business
objective, the key results, the customer problem and the target market. Cagan calls them "the bare minimum", and says
preparing the answers normally takes "a few minutes". The product manager then shares them with the team and key
stakeholders before discovery starts.

**This supports the decline.** The later version frames work a team is about to do, and it does not gate an investment.
A few minutes' framing does not need a bundle, and the guide paragraph routes it accordingly. The book does not say the
four replace the ten, so this record does not say so either. Only that chapter and term searches of the book were read.

### Consequences

**Good.**

- A reader of the business case guide learns which questions a new-product case should add, at the cost of one paragraph.
- The issue closes rather than sitting open with nothing to move it.

**Bad, and stated plainly.**

- **The prompts are advice and not template sections**, so nothing checks that a filled case answers them.
- **The catalog row stays `candidate` and carries no state override**, following
  [ADR 0049](0049-pi-release-retrospective-fails-the-admission-test.md)'s rule. The decline is discoverable through
  this record and the [`tier2-specs.md`](../tier2-specs.md) progress table.

### What would reopen this, stated so it is falsifiable

1. **The maintainer chooses to build it**, as ADR 0041 allows. The Lean UX Canvas went that way after a sweep recommended
   declining it.
2. **A real reader asks for the ten-question screen as its own template**, and the guide paragraph does not meet the need.
3. **A named source shows a software team keeping an opportunity assessment as a document distinct from a business case.**

## More Information

- The read and the book notes are held locally, at `_local/research/2026-11-04_poa-read/read.md` and
  `_local/research/2026-11-05_cagan-books/notes.md`. The book stays on the maintainer's machine.
- The guide paragraph: [`business-case_guide.md`](../../../templates/business-case/business-case_guide.md).
