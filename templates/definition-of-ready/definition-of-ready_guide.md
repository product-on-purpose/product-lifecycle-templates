# Guide: Definition of Ready (operator card)

The short card. Why the document is shaped this way, and the full argument behind every rule here, is in
[`definition-of-ready_companion.md`](definition-of-ready_companion.md). A fully worked instance is
[`definition-of-ready_example.md`](definition-of-ready_example.md).

One framing worth carrying into every use of this card: whether a team should keep a Definition of Ready
at all is a live, three-sided argument in the field, not a settled question this card resolves for you.
Neither the 2020 Scrum Guide nor the Scaled Agile Framework's own glossary names the type at all, and the
practitioners in this bundle's research who argue for keeping one also argue for keeping it small and easy
to drop. Reaching for this template because "a real team has one" gets the reasoning backward.

## When to use

- A team keeps pulling in backlog items it does not actually understand, and loses real sprint time to
  questions that could have been answered before the sprint started.
- The team wants a shared, joint way to decline ill-defined work at the door, without that decline turning
  into a rule one role can invoke unilaterally against another.
- More than one criterion for "this item is clear enough to start" keeps getting re-litigated item by item,
  and the team would rather agree it once than argue it every time.
- The team has a genuine, nameable pain (not an aspiration to "better process") and is willing to write down
  what would make the document worth dropping, not just what makes it worth keeping.

## When NOT to use

Four things get reached for instead of, or confused with, a Definition of Ready. Confirm which one you
actually need before filling in this template.

| You actually need | Because |
|---|---|
| **A Definition of Done** | A Definition of Ready gates entry into a sprint; a Definition of Done gates exit from one. They are the mirror image of each other, not two names for the same gate, and a Definition of Done is the one of the pair that is actually part of Scrum. |
| **Acceptance criteria** | Acceptance criteria state the conditions unique to one backlog item. A Definition of Ready applies across every item in scope and may require that acceptance criteria exist before an item is pulled in, without ever stating what those criteria are itself. |
| **Better backlog refinement, not a written document** | Whether a standing Definition of Ready should exist at all, versus letting the refinement activity itself do this job, is a real, unresolved argument among the practitioners this bundle's research read. Confirm the team has actually leaned on refinement first, before reaching for a written document instead. |
| **A governance stage-gate review** | A stage gate is an explicit decision point, taken above the team, with outcomes like continue, kill, hold, or recycle the work. If the criteria you are writing would ever produce one of those outcomes rather than simply starting a conversation, you are no longer writing a Definition of Ready. |

## Pick a variant

This bundle ships one size, lean, and there is no second, heavier variant to choose between. That is a
deliberate call, not an unfinished one: no source read for this bundle argues for a bigger Definition of
Ready, and the ones that address its size at all argue for keeping it small, one naming shrinking over
time as the sign of a maturing team, and a `full` variant that added more sections would risk the exact
failure the practice is criticized for. If your situation feels like it needs more than five sections, that
is itself a signal worth taking seriously, not a reason to look for a heavier template. See
[`definition-of-ready_companion.md` section 4](definition-of-ready_companion.md#4-variants-and-sizing) for
the full reasoning, including the one case (readiness gated at a level above the single story, such as
program-level planning) this bundle does not attempt to cover.

## The rubric

Score each 0, 1 or 2. **Under 10 out of 16, and whether an item was actually ready stops being something
this document settles.** The argument about whether the item should have been pulled in moves into the
sprint itself, decided by whoever has the most authority in the room that day rather than by what the team
agreed in advance, which is the exact failure this document exists to prevent.

All eight rows apply. This bundle ships one size, so there is no per-variant scoping decision to make here.

| # | Criterion | 0 | 1 | 2 |
|---|---|---|---|---|
| 1 | **Pain is concrete** | The stated reason is agile vocabulary, such as "to ensure alignment," that nobody could point to a sentence disappearing if the document worked | Names an actual recent problem, but does not say it has happened more than once, or reads as a hypothetical rather than something that occurred | Names a specific, recurring problem in the team's own words, something that has happened more than once and that a teammate would recognize without being told which meeting it is about |
| 2 | **Retirement condition is real** | Blank, "never," or a calendar date such as "review in a year" | A condition is named but is vague, such as "when the team matures" | Names a condition that is a fact about the original pain going away, one a teammate could point at later and say plainly whether it is true yet |
| 3 | **Ownership is genuinely joint** | A single role is named as the author or owner, such as "the Product Owner's checklist" | No sole owner is named, but who actually agreed the document, and when it is checked, is also not stated | Names who agreed it, genuinely both the product owner and the team rather than one handing it to the other, which item types it covers, and at least one recurring moment it is checked |
| 4 | **Rows are answerable questions** | At least one criterion states a condition rather than a question, such as "story is clear" | Every row is phrased as an answerable question, but at least one consequence is missing or vague, such as "we'll see" | Every row asks a question a reviewer could answer yes or no, names the evidence that answers it, and states plainly whether a "no" stops the item at the door or only starts a conversation |
| 5 | **Hard stops are dependencies** | Any criterion requires something be fully finished before entry, or a hard stop states no reason for being one | Every hard stop states a reason, but at least one names no external party, or a dependency row does not say whose calendar is actually the constraint | Every criterion that stops an item outright names the other team or vendor whose calendar the team does not control, and every other row starts a conversation rather than closing a door |
| 6 | **Escape valve is named** | Blank, or reads as "we use judgment" with nothing further | States that an override is possible, but not who decides it or how it gets recorded | States plainly which move this team actually makes when a top-priority item misses (pull it in on team judgment, make it ready as the sprint's first task, or a documented override) and how that decision gets recorded |
| 7 | **Trigger fires both ways** | A calendar cadence, such as "reviewed quarterly," or nothing at all | Names a concrete signal and an owner for one direction, and leaves the other blank or generic | Both a too-loose and a too-tight trigger name a concrete, recurring signal and a specific person or role who notices it |
| 8 | **Anyone can answer** | Every criterion can only be resolved by the Product Owner personally, every time | Most criteria are broadly answerable, but at least one still always routes back to a single role | Any teammate, not only the Product Owner, could gather the evidence and answer every row without needing special access or standing |

Every cell above describes evidence, not a count. The test is the same one this library applies everywhere:
could someone satisfy the cell without actually making the document better? If yes, the cell is written
wrong, and that is a defect in the rubric, not a license to grade loosely.

## Named anti-patterns

1. **The 100-percent rule.** Any criterion phrased as requiring something be fully finished before an item
   can be pulled into a sprint. This is the mechanism this bundle's research names most directly as turning
   a Definition of Ready into a sequential, stage-gate approach; the contract drift in anti-pattern 3 is
   another route to the same place.
2. **The rejection weapon.** The document gets invoked by one role as grounds for turning work away, rather
   than functioning as something the whole team agreed to together. This is the direct symptom of letting
   ownership slip from joint to singular.
3. **The contract, not the guideline.** What was meant to be a shared shorthand quietly becomes something
   argued over, item by item, between the person proposing work and the person judging it, exactly the
   dynamic a jointly owned guideline exists to avoid.
4. **Weaponization.** The document gets used as leverage in an argument it was never meant to settle, rather
   than as a tool for mutual clarity about what is actually being asked.
5. **The over-regulated process.** So much process accumulates around entry that the practice stops
   resembling the lightweight, team-owned tool it started as, and starts reading as bureaucracy imposed on
   the team rather than agreed by it.
6. **The silent pressure valve.** No stated answer anywhere in the document for what happens when a
   top-priority item misses it. Under real pressure, the team either ignores the document or invents an
   answer on the spot, and neither outcome is one anybody agreed to in advance.
7. **The parking brake.** The document blocks more value than it protects. A Definition of Ready that has
   never once been loosened is, by this bundle's own reading of the dispute, at least as worth investigating as one that
   has never been tightened, which is exactly why the rubric's row 7 grades both directions.
8. **The irreversible phase.** Treating adoption as a one-way, hard-and-fast gate rather than something the
   team can experiment with, adapt, or drop entirely once the pain it was written for is gone.

## When it is good enough

When the pain this document exists to fix is written in the team's own words rather than agile vocabulary,
when every criterion is a question anyone on the team, not only the Product Owner, could actually answer,
when the one place a miss can stop an item outright is a dependency on someone outside the team's control,
and when everyone already knows what happens the next time a top-priority item does not meet it, before that
moment is ever actually under pressure.

Then delete every HTML comment. The two Review Trigger conditions you wrote are what keep this document
honest afterward, in both directions: the one that catches it going quietly too loose, and the one that
catches it becoming the parking brake it was never meant to be. If, at some point, the honest answer to
"why do we keep this" is nothing, dropping it is a legitimate outcome of this exercise, not a failure to
complete it.
