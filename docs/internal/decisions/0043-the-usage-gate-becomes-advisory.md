---
status: accepted
date: 2026-09-03
decision-makers: [jprisant]
consulted: [claude]
---

# The usage gate becomes advisory, and the honesty gate does not move

## TL;DR

- **Decision:** **no usage signal gates any build in this library.** ADR 0041's forty-bundle falsifier
  becomes a **soft reminder** rather than a trigger that re-opens a decision, the roadmap's risk-table
  language stops reading as a prohibition, and milestone **M5 is no longer gated on an M3 usage signal**.
  Growth proceeds at the maintainer's discretion, indefinitely, with no usage precondition anywhere.
- **What does NOT move, and this is half the decision:** the **honesty gate** stays exactly where it is. A
  bundle is still `beta` until a real usage cycle is recorded, is still never called "verified", "proven"
  or "complete" on a green gate alone, and the library still publishes zero real fills as zero. **Removing
  a permission gate and removing an honesty gate are different acts, and only the first is taken here.**
- **Why:** the usage gate has never once stopped a bad build. It has only ever stopped good ones, and it
  did so by making every build feel like a violation of a rule nobody could satisfy. The maintainer reports
  using the library in other contexts and being pleased with it, which is precisely the evidence the gate
  demanded and could not accept, because it was written to be satisfied only by strangers.
- **Status:** accepted 2026-09-03. **Amends [ADR 0039](0039-maintainer-discretion-replaces-the-pull-gate.md)
  and [ADR 0041](0041-maintainer-preference-sets-the-build-order.md)**, which each removed one gate and
  left a falsifier behind that re-imposed it at a threshold. Adds
  [`docs/how-to/evaluating-a-template.md`](../../how-to/evaluating-a-template.md), because a reminder with
  no method is just guilt.

## Context and Problem Statement

Three records have now walked the same rule backwards, and each stopped one step short:

| Record | What it removed | What it left |
|---|---|---|
| [0021](0021-complete-the-tier-1-floor.md) | grow-by-pull, for the Tier-1 floor only | the rule intact everywhere else |
| [0039](0039-maintainer-discretion-replaces-the-pull-gate.md) | the gate on *whether* a type may be built | a falsifier that re-opens the decision |
| [0041](0041-maintainer-preference-sets-the-build-order.md) | the rule that *ordered* builds | the same falsifier, restated and tightened |

**So building was already ungated before this record, and it did not feel ungated.** That gap is the
problem being solved. Three things kept the gate alive after its removal:

1. **ADR 0041's falsifier is a trigger, not a note.** "Re-open this record when the library reaches roughly
   forty bundles with still-zero external fills" means a countdown is running, and a maintainer building
   bundle 28 is spending down a budget toward a reckoning.
2. **The roadmap's risk table reads as a prohibition.** *"Fix outreach, do not soothe a stalled wedge by
   building more content"* is written as an instruction, and it has been quoted as one repeatedly,
   including by this project's own agent in the same session that shipped the `epic` bundle.
3. **Milestone M5 is marked "correctly gated on M3 signal".** Since M3's signal is a usage number that has
   been zero since the library existed, an entire milestone was parked behind a condition nothing in the
   maintainer's control could produce.

**The evidence that broke it:** the maintainer is using the library in other contexts and is pleased with
it. M3's own acceptance criterion accepts that case in as many words, since it reads "whose author is not
the library author, **or** whose content is a real work artifact". The prose above that criterion says
"zero fills by anyone but the library's author", which is stricter than the criterion it introduces, and
**the stricter prose is what everyone has been quoting**, including this repository's agent throughout
2026-09-03. A gate whose own acceptance criterion is more permissive than its summary is not a gate. It is
a discouragement with a citation.

## Decision Drivers

* **A gate that cannot open is not managing risk, it is preventing work.** ADR 0039 said this. The
  falsifiers it and 0041 left behind re-introduced the shape it named.
* **The library's honesty does not depend on the growth gate.** It depends on `beta` status, on publishing
  zero as zero, and on never calling a bundle proven. Those are separate mechanisms and they are untouched.
* **A reminder without a method is guilt.** Telling a maintainer to gather feedback while providing no
  procedure produces neither feedback nor builds.
* **Removing the countdown is the point.** Growth should not feel like borrowing against a debt that comes
  due at forty bundles.

## Considered Options

1. **Make the usage gate advisory and supply a method.** Chosen.
2. **Leave it and rely on the maintainer to ignore it.** Rejected. It has been quoted as binding by an
   agent working in this repository, which is evidence it reads as binding to a reader.
3. **Remove the honesty gate too, so a bundle can go `stable` without usage.** Rejected firmly. That would
   convert "measured, not asserted" into a slogan. The value of `beta` on twenty-seven bundles is that it
   is true.
4. **Set a higher threshold instead of removing it.** Rejected. Any number is invented at the moment of
   setting it, which is the reasoning ADR 0041 used against the demand rule.

## Decision Outcome

**No usage signal gates any build.** Specifically:

- **ADR 0041's falsifier is downgraded to a soft reminder.** Reaching forty bundles with zero external
  fills does not re-open any decision. It prompts one question, asked once, and a "no, keep going" is a
  complete answer that needs no justification.
- **The roadmap's risk-table entry is reworded** from an instruction into an observation.
- **M5 is no longer gated on an M3 usage signal.** It may start whenever the maintainer wants it.
- **Nothing in this record permits a quality claim.** See below.

### What stays, stated so it cannot be quietly lost

| Mechanism | Status |
|---|---|
| `beta` until a real usage cycle is recorded; then `stable` eligible | **Unchanged**, in all nine family contracts |
| Never call a bundle "verified", "proven" or "complete" on a green gate | **Unchanged** ([ADR 0021](0021-complete-the-tier-1-floor.md)) |
| Publish zero real fills as zero | **Unchanged** |
| Coverage and real usage are separate honest numbers | **Unchanged** |
| Efficacy claims require the eval protocol's gates | **Unchanged** |
| Distribution submissions stop for the maintainer | **Unchanged** |

**A library may grow without evidence. It may not claim without evidence.** This record moves the first and
leaves the second exactly where it was.

### Consequences

* **Good:** the maintainer can build what they want, when they want, without a countdown. That is the whole
  ask and it is now true in the records rather than only in principle.
* **Good:** a method now exists for turning real usage into recorded evidence
  ([`evaluating-a-template.md`](../../how-to/evaluating-a-template.md)), which the gate never provided. The
  gate demanded feedback and supplied no way to give it.
* **Bad, and named rather than argued away:** this removes the last structural pressure toward outreach.
  ADR 0041 already named that cost and this record increases it. **The library can now grow indefinitely
  with nobody using it, and nothing will object.** The honesty mechanisms mean it will at least be visible
  while it happens.
* **Neutral:** no check changes. Check K already permits `beta` and `stable`; nothing in CI reads a usage
  number.

### The reminder, in full

Not a gate, not a threshold, not a trigger. **One question, worth asking when a build feels routine:**

> Has anything you built recently been used on real work, by you or anyone else, and did you write down
> what happened?

If yes, [`evaluating-a-template.md`](../../how-to/evaluating-a-template.md) is the method. If no, that is a
complete answer and the next build proceeds.
