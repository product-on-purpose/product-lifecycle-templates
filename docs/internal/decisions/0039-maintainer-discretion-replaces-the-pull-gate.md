---
status: accepted
date: 2026-08-14
decision-makers: [jprisant]
consulted: [claude]
---

# The maintainer may build any template; grow-by-pull becomes an input, not a gate

## TL;DR

- **Decision:** amend [ADR 0021](0021-complete-the-tier-1-floor.md) so that **Tier-2 and Tier-3 bundles may
  be initiated by the maintainer at their own discretion**, with a recorded one-line rationale, whether or
  not an external request exists. The pull queue is **retained as an intake and as a priority signal**, and
  stops being a precondition.
- **Why:** with the Tier-1 floor complete and zero external users, a strict pull gate is not a gate. It is a
  stop. Nothing can be built until an audience the library does not yet have asks for it, which is the
  chicken-and-egg ADR 0021 named, one tier up and with no scheduled escape.
- **Status:** accepted 2026-08-14. Amends ADR 0021 for Tier 2 and Tier 3. **Changes nothing about the
  standard a bundle is built to**, and nothing about how usage is reported.

## Context and Problem Statement

The repository's standing rule was **grow by pull, not speculation**: no bundle gets built until a real
request or a named internal need pulls it. [ADR 0021](0021-complete-the-tier-1-floor.md) amended that for
the Tier-1 floor only, on a bounded, defined target, and kept it strict for everything else.

**The floor is now complete.** 26 bundles cover all 25 templatable Tier-1 types, every family contract is
adopted, and the build backlog is empty. So grow-by-pull is the only remaining gate on new content, and:

- **Nothing has ever been requested.** The three intake templates in `.github/ISSUE_TEMPLATE/` shipped
  2026-08-07 and have received **zero issues**.
- **Zero people outside the author have used the library**, so there is no population from which a pull
  could plausibly arrive.
- 151 Tier-2 and 27 Tier-3 catalog types are therefore **candidates that cannot be built**, indefinitely.

**A gate that cannot open is not managing risk. It is preventing work.** ADR 0021 made exactly this argument
about the floor: *"the chicken-and-egg is real: the library is too thin to pull, so waiting for a pull waits
forever."* That argument does not stop applying at the boundary of the 27 must-have types.

## Decision Drivers

* **The maintainer carries the entire maintenance cost**, so the maintainer's judgment about what is worth
  maintaining is the relevant judgment. There is no second party whose interests the gate is protecting.
* **What grow-by-pull actually protects against is self-deception**, not building. The risk it names is
  mistaking coverage for traction. ADR 0021 already identified the discipline that neutralises that risk,
  and it is a **reporting** discipline rather than a build gate.
* **The intake is worth keeping regardless.** A request from a named person remains the strongest evidence
  this library can receive, and it is now built. Demoting it from gate to signal costs nothing.
* **A rule nobody can satisfy gets ignored rather than followed.** Leaving it in place invites it to be
  quietly worked around, which is worse than amending it in the open.

## Considered Options

* **A. Keep strict grow-by-pull for Tier 2 and Tier 3.** Rejected: it cannot open. With zero users there is
  no mechanism by which a pull arrives, so this is a decision to build nothing further, made by inaction
  rather than on purpose.
* **B. Maintainer discretion, with the honest-numbers discipline retained.** Chosen.
* **C. Abolish the pull queue entirely.** Rejected: external requests remain the strongest available signal,
  the intake already exists, and removing it would discard information for no gain.

## Decision Outcome

**Chosen: B.**

### What changes

1. **A Tier-2 or Tier-3 bundle may be initiated by the maintainer without an external request**, recording a
   one-line rationale in the build record.
2. **The pull queue is retained** as an intake and as a **priority** input: a type with a named requester
   outranks a type with only a maintainer rationale, all else being equal.
3. **A recorded maintainer rationale is never reported as demand.** It is labelled as what it is.

### What does not change, and this clause is the reason the amendment is safe

1. **Coverage and real usage stay separate, honest numbers.** "Zero real fills" stays visible in
   [`STATE.md`](../../../STATE.md) until it is not true.
2. **No bundle is called "verified", "proven", or "complete" on the strength of a green gate.**
3. **Every bundle still passes the full pipeline**: the research fan-out, the four-lens adversarial review,
   the citation discipline, [ADR 0030](0030-templating-scope-markdown-documents.md)'s admission test, and
   the gate.

**Discretion is about which types get built. It is never about the standard they are built to.** The
admission test in particular still applies and still has teeth: it has twice rejected a type the library
intended to ship.

### What this does not unblock

**Tier-3 regulated content remains blocked**, not by this record but by decision D4, closed separately on
2026-08-14 as a deliberate "no for now". That tier carries a regulation-currency burden this library has not
committed to, and no amount of maintainer discretion changes that.

## Consequences

* **Good:** the library can grow again, and on the judgment of the person who will maintain it.
* **Good:** the rule now describes what will actually happen, so it can be followed rather than worked
  around.
* **Good:** the intake keeps its value without carrying weight it cannot bear.
* **Bad, and accepted:** the audit named coverage-first *"the seductive wrong answer"*, and that risk is now
  guarded by judgment rather than by rule. **If the maintainer builds forty more bundles with zero users,
  nothing in this repository will stop it.** The honest-numbers discipline is a disclosure rule, not a
  brake.
* **Bad:** a recorded rationale is materially weaker evidence than a named requester, and a future reader
  skimming build records could mistake a list of rationales for a list of pulls. The labelling clause exists
  because of that risk, and it depends on being followed.
* **Neutral:** the pull queue's urgency drops, since it is no longer a precondition for any work. Its worth
  does not. [`pull-queue-spec.md`](../pull-queue-spec.md) is unchanged by this record except that its demand
  rule now governs **prioritisation** rather than **permission**.

### The falsifier

**If the library passes roughly forty bundles with still-zero external fills, this amendment should be
re-opened.** At that point the pattern grow-by-pull was written to prevent would have evidence behind it
rather than being a worry, and "the maintainer decided" would have stopped being a reason and started being
a habit.

## More Information

* [ADR 0021 (complete the Tier-1 floor)](0021-complete-the-tier-1-floor.md), which this record amends, and
  whose "one discipline kept from grow-by-pull" clause is the load-bearing inheritance here.
* [`pull-queue-spec.md`](../pull-queue-spec.md) for the intake that is retained.
* [ADR 0030 (templating scope)](0030-templating-scope-markdown-documents.md) for the admission test that
  still gates every candidate regardless of who proposed it.
