---
status: accepted
date: 2026-08-22
decision-makers: [jprisant]
consulted: [claude]
---

# Maintainer preference and need set the build order; external demand is an input, not a rank

## TL;DR

- **Decision:** the order in which Tier-2 and Tier-3 bundles get built is set by **the maintainer's own
  preference and need**. External requests are recorded, kept visible, and may be weighed, but **they do
  not rank the queue and their absence blocks nothing**.
- **Why:** [ADR 0039](0039-maintainer-discretion-replaces-the-pull-gate.md) removed the pull gate on
  *whether* a type may be built and retained the queue "as a priority signal". **That signal has been
  empty since the intake shipped and there is no population from which it could arrive.** Ranking by an
  input that is always zero is not ranking; it produces an arbitrary order wearing a principled one's
  clothes.
- **Status:** accepted 2026-08-22. Amends ADR 0039's retention of the queue as a *priority* signal, and
  rewrites [`pull-queue-spec.md`](../pull-queue-spec.md) section 4 for the second time in two days.
  **Changes nothing about the standard a bundle is built to**, and nothing about how usage is reported.

## Context and Problem Statement

Three decisions have now touched the same rule, each narrowing it:

| Record | What it did |
|---|---|
| [0021](0021-complete-the-tier-1-floor.md) | Demand-gated Tier 2 and Tier 3; amended grow-by-pull **for the Tier-1 floor only** |
| [0039](0039-maintainer-discretion-replaces-the-pull-gate.md) | Made maintainer discretion govern **whether** a type may be built; kept the queue as a **priority** signal |
| This record | Makes maintainer preference and need govern **the order** |

**The ordering rules were rewritten into priority wording on 2026-08-21 and the rewrite exposed the
problem it was supposed to fix.** `pull-queue-spec.md` section 4 rule 1 reads: *"One named requester raises
a type from `pull-gated` to `queued`."* Rule 2: *"The maintainer's own governance need ranks as one pull."*

**Both rules meter the same currency, and the library has none of it.**

- **Zero issues have been filed**, open or closed, since the three intake templates shipped 2026-08-07.
- **Zero people outside the author have used the library.** `evals/usage-log/` is empty.
- So rule 1 has never fired and cannot fire, and rule 2 makes the only real input in the system worth
  exactly one unit of a currency whose total supply is one unit.

ADR 0039 named this shape one level up: *"A gate that cannot open is not managing risk. It is preventing
work."* **A ranking that cannot rank is the same shape applied to order rather than to permission.** It
does not prevent work; it disguises whose preference is choosing, which is worse in a different way,
because it presents the maintainer's own judgment as though a queue produced it.

## Decision Drivers

- **The maintainer is currently the only user and the only person with a need.** Ordering by their need is
  ordering by the only real evidence in the system.
- **Dogfooding is the only evidence-generating mechanism this library has ever had.** DF-1 came from
  filling the release-notes template. The [ADR 0021](0021-complete-the-tier-1-floor.md) cross-reference
  defect came from grading a real record. The `v0.4.0` known-issues section came from self-grading the
  release note. **Every one of those came from the maintainer needing the document**, not from a request.
- **An admitted preference is more honest than a derived-looking order.** This library's one credibility
  asset is that it does not claim what it has not earned. A queue that looks ranked by demand, when demand
  is zero, spends that asset.
- **The queue still has a job.** Recording a request, and making a refusal legible, are worth doing whether
  or not requests rank anything.

## Considered Options

- **A. Keep ranking by pull.** Rejected: the input is empty and has always been empty. Section 4 would
  continue to describe a mechanism that has never run.
- **B. Maintainer preference and need set the order; requests are recorded and may be weighed.** Chosen.
- **C. A formula combining request count with maintainer need.** Rejected: a weighted formula over an
  input that is uniformly zero is decoration. It would also invent a house rule the house does not follow,
  which is the reason [`check-rubric-scope.py`](../../../tools/check-rubric-scope.py) refuses to enforce a
  threshold formula.

## Decision Outcome

**Option B.** The five rules in `pull-queue-spec.md` section 4 change as follows:

| Rule | Before | After |
|---|---|---|
| 1. One named requester raises a type | A request changed rank | **A request is recorded and stays visible. It does not itself change rank.** The maintainer may weigh it |
| 2. Maintainer's need counts as one pull | Maintainer need was one input among others | **Inverted. Maintainer preference and need are the ranking criterion.** A recorded one-line rationale still accompanies each build, per ADR 0039 |
| 3. Three requests trigger the active-practice test | A count triggered a quality bar | **The test is a quality bar on the build itself, applied whenever a methodology pack is built**, regardless of any count |
| 4. Tier-3 regulated is blocked | Blocked on the currency burden, not on demand | **Unchanged. Read the consequence below** |
| 5. A queued type is not a commitment | Rank is not a schedule | **Unchanged, and now load-bearing**, because the order is now openly one person's preference |

**The state vocabulary changes with it.** `pull-gated` becomes **`candidate`**, because the name asserts a
gate this record removes and 0039 already weakened. The four states are `built`, `queued`, `candidate`,
`out-of-scope`.

## Consequences

**Good.**

- **The order can now be stated truthfully.** 177 unbuilt Tier-2 and Tier-3 types stop being an
  undifferentiated field and become a set the maintainer can rank, defer, or refuse with a reason.
- **The intake keeps its two useful jobs** and loses only the one it never performed: recording a request
  without committing to it, and making a refusal legible.
- **It unblocks the labelling work** that `pull-queue-spec.md` deliverable D4 describes, which could not
  proceed while the vocabulary encoded a gate that no longer exists.

**The cost, and it is the one worth reading twice.**

**This removes the last structural discipline against building content nobody uses.** The roadmap's whole
thesis is floor, then wedge, then proof, then reach, and its risk table says plainly: *"fix outreach, do
not soothe a stalled wedge by building more content."* [`distribution-plan.md`](../distribution-plan.md)
section 9 says the same. **This record makes that failure easier to commit**, because after it, nothing but
the maintainer's own judgment stands between an empty usage log and a twenty-seventh bundle.

That is accepted deliberately rather than argued away. ADR 0039 carried a falsifier for exactly this and
this record tightens it rather than inheriting it quietly.

**Tier 3 is not reopened, and its reopening condition is now written in a currency this record no longer
ranks in.** Decision D4 (regulated-industry appetite) closed 2026-08-14 as a deliberate no, **on the
currency burden**, meaning regulation text must be re-verified at authoring time and on a cadence forever.
That is a maintenance obligation, not a demand question, so it stands on its own and this record does not
touch it. **But D4 states that it "re-opens on a pull from a real regulated team", and a pull is exactly
what this record says does not govern the order.** Restating that condition in preference terms is left
open rather than settled here, because reopening Tier 3 is a scope decision of its own.

## The falsifier

**Re-open this record when the library reaches roughly forty bundles with still-zero external fills.**

> **Amended 2026-09-03 by [ADR 0043](0043-the-usage-gate-becomes-advisory.md): this falsifier is now a soft
> reminder, not a trigger.** Reaching forty bundles with zero external fills re-opens nothing. It prompts
> one question, and "no, keep going" is a complete answer. The original text is kept because the reasoning
> below it is still the honest reasoning; what changed is the obligation it created, not the observation
> it makes.

This is ADR 0039's falsifier, restated because this record makes it more likely to fire. At that point the
library will have added fourteen bundles under maintainer preference alone, with no external evidence that
any of the twenty-six before them were worth having. **If that happens, the honest reading is not that the
preference was wrong. It is that this record and 0039 together removed a brake whose only job was to stop
this exact drift, and nothing replaced it.**

`STATE.md`'s "zero real fills" line is the instrument. It stays visible, it is not moved, and it is not
softened.

## More Information

- [ADR 0021](0021-complete-the-tier-1-floor.md), the record this chain amends
- [ADR 0039](0039-maintainer-discretion-replaces-the-pull-gate.md), which this record amends in turn
- [`pull-queue-spec.md`](../pull-queue-spec.md) section 4, rewritten to match, and deliverable D4, whose
  state vocabulary this record settles
- [`roadmap.md`](../roadmap.md) risk table, which names the failure this record makes easier
