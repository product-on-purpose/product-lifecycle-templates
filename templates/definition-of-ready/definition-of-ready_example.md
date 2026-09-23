---
title: "Reporting Squad Definition of Ready"
doc_type: definition-of-ready
size: lean
team: "Reporting Squad, Acme Analytics"
owner: "Priya Nair (PM, Reporting)"
status: active
doc_version: "1.0.0"
created: "2026-07-29"
updated: "2026-07-29"
related_links:
  - "../product-backlog/product-backlog_example.md (Saved Views product backlog; the SV-5 dependency row this document's hard-stop criterion is written for)"
  - "../epic/epic_example.md (Saved Views epic; D-02, the cross-team permissions dependency SV-5 is waiting on)"
  - "../definition-of-done/definition-of-done_example.md (Reporting Squad Definition of Done; that document gates exit from the sprint, this one gates entry)"
  - "../sprint-backlog/sprint-backlog_example.md (Sprint 24 Sprint Backlog; the two-week cadence this document's dates follow)"
source_template: definition-of-ready
source_template_version: 0.1.0
---

> **Worked example.** A filled `definition-of-ready`, the bundle's only size, for the Reporting Squad at the
> fictional Acme Analytics, the same squad whose
> [Definition of Done](../definition-of-done/definition-of-done_example.md) and
> [Sprint 24 Sprint Backlog](../sprint-backlog/sprint-backlog_example.md) this library's other examples
> already describe. It is the squad's first Definition of Ready, and it arrives exactly the way the
> Definition of Done predicted it would: "if the squad adopts a Definition of Ready later, it will gate
> entry into the sprint, not exit from it, and will not replace anything above." Nothing in that document
> changes here. It is dated 2026-07-29, the squad's first refinement session of Sprint 25, five days after
> that document's last amendment at the planning session that opened the sprint, and its reason for existing is SV-5 (the sharing story) and the cross-team dependency
> the [Saved Views epic](../epic/epic_example.md) records as D-02, "Confirmed, integration pending," which
> is the one sourced case this bundle's own research allows as a hard stop rather than a guideline. Read it
> alongside [`definition-of-ready_guide.md`](definition-of-ready_guide.md), the rubric it was graded
> against. All names already established in the library's Acme Analytics thread are drawn from there; any
> threshold marked illustrative below is invented for this example alone.

# Reporting Squad Definition of Ready

## Why We Keep One

SV-5, the sharing story, has come up at backlog refinement three sessions running, and each time the squad
has spent most of the slot re-arguing whether it can go into the next sprint rather than doing any of the
sharing work itself. The story keeps almost, but not quite, clearing a bar the squad has been applying
informally and inconsistently, and the missing piece has been different each time: first it was whether the
spike had actually landed, second it was whether anyone had seen Platform's permissions confirmation in
writing rather than heard about it secondhand, third it was open disagreement over who even gets to say a
story is ready. Writing the bar down once, so the squad stops re-deriving it every refinement, is what this
document is for.

**We would drop this document if:** a story reached agreement on its readiness in a single refinement pass,
for four sprints running, without anyone needing to point at a line below to get there. (illustrative
threshold)

## Scope and Ownership

Applies to user stories only. SV-5 and its siblings are the only kind of backlog item the squad has needed a
shared readiness bar for so far; a bug like BUG-231 and a spike like SV-0 are scoped and sized differently
enough that folding them into the same rows would blur what each row is actually asking. Checked at backlog
refinement, the squad's standing mid-sprint session, and re-checked at sprint planning only if a story
changed materially between the refinement pass that cleared it and the planning session that would pull it
in. Agreed at that first Sprint 25 refinement session on 2026-07-29 by Priya Nair and the development team
together, Marcus Bell and Anjali Rao among them; the rows were drafted in the room, one at a time, rather than
brought to it finished.

## Readiness Criteria

Below is the bar as it stands today, written the week the squad walked SV-5 through it for the first time.
Applied now, SV-5 clears the first three rows: refinement during Sprint 24 reached a shared account of the
story in the squad's own words, the squad sized it at 8 points and confirmed it fits inside one sprint, and
the epic's own acceptance criterion for sharing, "a teammate who already has access to the dashboard can
pick a view its owner marked shared and see the same slice of data," is already the line the squad tests
SV-5 against at refinement, ahead of a dedicated acceptance-criteria document like SV-4's. It fails the
fourth row: Platform has confirmed the permissions check exists (D-02, in the epic's dependency table) but
has not yet given the squad a date it can plan a sprint around, so SV-5 stays in refinement on this
document's own hard stop, not on Priya Nair's say-so.

| Criterion (a question) | Evidence | If Missing |
|---|---|---|
| Does the squad have a shared account of what the story is asking for, said out loud at refinement rather than assumed from the ticket text? | The refinement notes record the story's intent in the squad's own words, with no question still marked open. | Guideline: starts a conversation at the next refinement session, does not by itself block sprint planning. |
| Can the story realistically finish inside one sprint against the squad's own Definition of Done? | The squad has sized it and named at least one way to split it if it turns out not to fit. | Guideline: starts a conversation at refinement; a story that cannot be split and does not fit stays there rather than entering a sprint. |
| Is there a testable line the squad can check the finished story against, beyond the Definition of Done's own criteria? | A draft acceptance criterion exists and is linked from the story, even if not yet a full acceptance-criteria document. | Guideline: starts a conversation at refinement. |
| If the story depends on work another team or a vendor owns, has that team or vendor confirmed a date the squad can plan a sprint around, in writing, rather than only confirmed the dependency exists? | A dated line from the other side's own owner, not a status label the squad set for them. | Hard stop: the story does not enter sprint planning until this line carries a name and a date from the other side, because the squad cannot negotiate its way past another team's or a vendor's own calendar. |

## When an Item Is Not Ready

For any of the first three rows above, the guideline rows, the squad's default when a top-priority story
still misses one at the moment a sprint is being planned is to make the story ready as that sprint's first
task, spending the first day closing exactly the gap refinement flagged rather than either forcing the story
in blind or losing a whole sprint waiting for the next refinement slot. Any developer can instead raise a
documented override at planning if the squad judges the story genuinely completable anyway; whichever path
is taken gets written into that sprint's own planning notes, so it is visible later rather than only
remembered.

The fourth row, the cross-team or vendor dependency, gets neither path, on purpose. The squad cannot make
Platform's confirmation happen by spending a sprint day on it, and overriding a dependency the squad does
not control would only move the risk from the backlog into the sprint, where it is harder to see and more
expensive to unwind. A story blocked on that row waits in refinement until the other side's owner supplies
the date; the pressure valve here is chasing the dependency, not overriding this document.

## Review Trigger

**Too loose trigger:** a story this document called ready gets pulled from a sprint, or needs substantial
rework before the squad can even start it, for a reason refinement could have caught, more than once across
three sprints running. (illustrative threshold)
**Noticed by:** whoever facilitates that sprint's planning session, raised at the next refinement.

**Too tight trigger:** a story fails only one of the three guideline rows, never the cross-team dependency
row, for more than two refinement sessions running, and the squad starts to suspect the row itself, not the
story, is what is not ready. (illustrative threshold)
**Noticed by:** Priya Nair, raised at the next retrospective.
