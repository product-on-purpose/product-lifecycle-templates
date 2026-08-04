# Guide: grading a product vision before you share it

Self-grade against this before circulating a draft. It takes about ten minutes and it is the last cheap
moment to fix anything.

Use it for all three formats. The criteria are about what the document **does**, not how it is laid out, so
they apply equally to a canvas, a narrative and a PR/FAQ. Where a format changes how a criterion is met, the
row says so.

Deep background for every criterion is in [`product-vision_companion.md`](product-vision_companion.md); a
worked pass is [`product-vision_example.md`](product-vision_example.md).

---

## Before you start: is this the right document at all?

**Write a product vision when** the team faces choices that a roadmap cannot settle, when people who were not
in the founding conversation need to make decisions consistent with it, when you are hiring or raising against
a future rather than a feature set, or when prioritisation arguments keep reopening the same question.

**Do not write one when** any of these is true:

- **You cannot name a single thing it would rule out.** Then you do not yet have a destination, you have a
  direction, and writing it down will produce the wallpaper described in the companion's section 7.
- **What you actually need is a strategy.** If the question is "which problems do we solve first", that is
  strategy, and the vision is upstream of it. Companion section 8.
- **What you actually need is a roadmap.** If the question is "what ships when", writing a vision will delay
  the answer without improving it.
- **Nothing has changed and the last one still works.** A strategy change is not a reason to rewrite a
  vision. If you are rewriting yearly, you are maintaining a roadmap under the wrong title.
- **Honest caveat:** no source found addresses whether a vision is worth writing for a very small team or a
  solo product. The practitioner literature assumes medium-to-large organisations. At small scale, judge it
  by the refusal test below rather than by alignment benefits that only appear at scale.

## Picking a format and a size

| If the job is... | Use |
|---|---|
| Orient a team fast, and be quotable in a prioritisation argument | **canvas, lean** (4 sections) |
| The above, plus survive readers who were not in the room: funders, a board, an incoming leader | **canvas, full** (8 sections) |
| Make someone *want* this future: hiring, a founding team, a team that has lost the thread | **narrative** |
| Argue that the future is worth having at all, and surface objections early | **PR/FAQ** |

They are not tiers. A narrative is not a better canvas, and the canvas is not a summary of the narrative;
they are different documents serving the same purpose. Companion section 4 explains why the library ships
three rather than picking one.

---

## The one test that outranks the rest

**Can this document be used to refuse something?**

Find a real request from the last year that somebody senior wanted and that this vision says no to. Point at
the sentence that does the refusing.

If you cannot, stop grading and fix that first. Everything below improves a document that is already doing
its job; this decides whether it is doing its job at all. A vision nobody has ever cited to decline anything
is decoration, however good the prose. See companion section 1.

---

## The rubric

Score each 0, 1 or 2. **Under 17 out of 24 and this will not be cited in an argument.** It will be pasted
into an onboarding deck, admired once, and never opened again, which is the documented failure mode for this
document type.

**Rows 9 and 10 do not apply to the lean canvas**, which omits Horizon and Review and Leaps of Faith by
design. Grade the other ten and score against 14 out of 20.

| # | Criterion | 0 | 1 | 2 |
|---|---|---|---|---|
| 1 | **It refuses something** | Nothing is declined | Exclusions named, all uncontroversial | An exclusion someone actually proposed, and you can say who and when |
| 2 | **It is picturable** | No person, no scene | A generic user doing a generic thing | A named person in a specific hour, doing what they cannot do today |
| 3 | **Imagery outweighs values** | Value words only | Concrete detail present but buried under abstractions | Concrete detail dominates; the abstract value words fit on one hand |
| 4 | **It excludes someone** | "Business users", "our customers" | A segment named, but nobody is ruled out | A real reader would read it and conclude "not me" |
| 5 | **It gives a reason to believe** | Credentials or ambition | An asset named that a competitor could also claim | Something a well-funded competitor could not copy next quarter, and it says why |
| 6 | **It is not a mission** | Would read identically after ten years of no progress | Future-facing, but describes the company rather than a changed world | Describes a state of the world that is currently untrue and would be visibly true if reached |
| 7 | **It is not a roadmap** | Named features or delivery dates | No features, but the horizon reads as a plan | Destination and horizon only; no sequence, no capability list |
| 8 | **It is not a positioning statement** | Compares the product to alternatives for a customer today | Mixes future state with present competitive claims | States the future; competitive material sits separately as context |
| 9 | **It has a horizon and a trigger** *(canvas full only)* | No date, no review | A date, but no trigger and no owner | A date, a named review point, and what would prompt a rewrite as distinct from a strategy change |
| 10 | **Its assumptions are named** *(canvas full and narrative)* | "Risks will be managed" | Assumptions listed, all comfortable | The assumption the author is most worried about, with the earliest signal that would disprove it |
| 11 | **It is short enough to recall** | Needs re-reading to summarise | Summarisable, but not from memory | Someone who read it once can state the destination without opening it |
| 12 | **It survives its own authors** | Only makes sense with verbal context | Understandable, but a new reader could not act on it | An incoming leader could use it to decline something without asking anyone |

**Which rows apply to what.** This bundle ships four variants and two rows grade a section that only some
of them contain, so scoring every variant against all twelve would penalise the **choice of format** rather
than the quality of the document. Row 9 needs a Horizon and Review section, which only the canvas full
variant has. Row 10 needs a place where assumptions are named: `Leaps of Faith` in canvas full, `What Has to
Be True` in the narrative. The PR/FAQ has neither, by design.

| Document | Rows that apply | Maximum | Score against |
|---|---|---|---|
| canvas, full | all 12 | 24 | **17** |
| canvas, lean | 1-8, 11-12 (it carries no horizon or assumptions section) | 20 | **14** |
| narrative, full | 1-8, 10-12 (it names assumptions but sets no dated horizon) | 22 | **16** |
| prfaq, full | 1-8, 11-12 (its horizon and its assumptions live inside the FAQ answers, not as sections) | 20 | **14** |

Every threshold above is the same proportion of the available points as the headline 17 of 24.

Every cell above describes **evidence, not a count**. That is deliberate: a threshold you can clear by adding
items will be cleared by adding items. This library's own `bug-report` research documents the mechanism for
defect counts, and a rubric row is the same kind of target. If you can satisfy a cell without improving the
document, the cell is written wrong.

**Rows 6, 7 and 8 exist because these are the three artifacts a product vision is most often confused with**,
and each confusion has a different tell. Companion section 8 has the boundaries.

---

## Format-specific checks

**Canvas.** Is every cell doing work, or is one of them restating another? "Who it is for" and "what they
need" collapsing into one thought is the usual sign the target group is not specific enough.

**Narrative.** Read it aloud. Any sentence that is hard to say aloud will be skimmed. Is it in the present
tense throughout, from inside the future? Did a bullet list creep in? A list means you have started writing
a canvas with worse formatting.

**PR/FAQ.** Would a customer recognise the headline as being about them? Is there a single word in the press
release a customer would not use? Does the Internal FAQ contain a question you are actually afraid of, or
only ones with comfortable answers? An easy FAQ is the tell that this document is marketing.

---

## Failure signals to look for in the draft

- **Every exclusion is comfortable.** Section is theatre. Find one that costs something.
- **The vision names a feature.** It will be stale within two quarters, and readers will argue about the
  feature instead of the future.
- **The business goal is a number with a date.** That is a key result. It will age faster than the vision and
  make the vision look stale by association.
- **Each team has its own version.** Companion section 7; this is a documented failure, not a scaling
  strategy.
- **You are rewriting it because the strategy changed.** The strategy is supposed to change. If the
  destination moves every time the route does, it was never a destination.
- **A quotation you did not check.** This subject has an unusually bad attribution record, including one very
  famous line that its supposed author never wrote. Companion section 6.

---

## When it is good enough

When someone who was not in the room can read it, tell you what the product is for, name a thing it rules
out, and disagree with you about something specific.

Disagreement is the signal. A vision nobody can argue with has not said anything.
