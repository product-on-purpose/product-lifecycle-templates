---
status: accepted
date: 2026-09-11
decision-makers: [jprisant]
consulted: [claude]
---

# The usage precondition leaves the language too, and the honesty gate stays where ADR 0043 left it

## TL;DR

- **Decision:** **no document in this repository may describe a missing usage signal as a constraint, a
  blocker, or a binding anything.** [ADR 0043](0043-the-usage-gate-becomes-advisory.md) removed the usage
  *permission* gate on 2026-09-03; the prose did not follow, and prose that still reads as a gate works
  like one. WP-31 becomes a piece of work the maintainer may do whenever they want, ranked like any other.
- **What does NOT move, and it is again half the decision:** the **honesty gate**. A bundle is still `beta`
  until a real usage cycle is recorded, is still never called "verified", "proven" or "complete" on a green
  gate alone, and this library still publishes **zero real fills as zero**. Removing a constraint on what
  may be BUILT and removing a constraint on what may be CLAIMED are different acts, and only the first is
  taken here - for the second time, on purpose.
- **Two maintainer evaluations recorded at the same time.** (1) `docs/releases/v0.6.0.md` **does not count**
  as this library's first real usage cycle. (2) Distribution submissions **wait**, on judgment rather than
  on any gate.
- **Status:** accepted 2026-09-11.

## Context and Problem Statement

ADR 0043 was unambiguous eight days ago: "no usage signal gates any build in this library ... Growth
proceeds at the maintainer's discretion, indefinitely, with no usage precondition anywhere."

**And then every document went on saying otherwise.** On 2026-09-11 the tree still contained:

- `roadmap.md` describing M3 as "**the binding constraint**", and WP-31 as the thing "still zero real fills"
  blocks;
- `STATE.md` carrying the same framing;
- and - written the same day, by an agent that had read ADR 0043 - a **new** sequencing rule in
  [`site-plan.md`](../site-plan.md) section 10.1 saying "nothing in S1 or later should start before WP-31
  records one real fill."

That last one is the evidence this record exists for. **A policy repealed in an ADR grew back in a plan
eight days later**, hedged as "a preference, not a prohibition", which is exactly the hedge ADR 0043 said
had been read as a ban the first time. A rule that regenerates itself in new documents was never really
repealed; it was moved.

## Decision Drivers

* **The gate never stopped a bad build.** ADR 0043's finding, unchanged: it only ever stopped good ones.
* **Prose is policy.** A maintainer reading "the binding constraint" before deciding what to do next is
  being gated, whatever the ADR says.
* **The two gates are genuinely different.** One says *you may not build this*. The other says *you may not
  call this proven*. The first was costing real work; the second is the entire reason this library is worth
  anything.
* **A repeal has to be checkable.** "We removed it" is a claim; "no document says it" is a state.

## Decision Outcome

**The usage precondition is removed from the language, and the honesty gate is restated so the difference
cannot be missed again.**

### What changes

1. **`site-plan.md` section 10.1 is deleted**, not softened. S0 through S3 run whenever the maintainer
   wants. The section was added 2026-09-11 and removed the same day, which is the shortest life any rule in
   this repository has had and the right one.
2. **`roadmap.md` stops calling M3 "the binding constraint"** and stops describing WP-31 as blocking. M3's
   items remain real work with a real exit criterion; they are not a precondition for M4, M5, or anything
   else.
3. **`STATE.md` carries the same correction.**

### What does not change, stated so the next reader cannot mistake it

**The honesty gate.** In every family contract, `status: beta until one real usage cycle is recorded` stands
exactly as written. All 27 bundles are `beta` and stay `beta`. No bundle is called "verified", "proven" or
"complete" on a green gate. **Zero real fills is published as zero**, in `STATE.md` and everywhere else.

This is not caution and it is not a compromise position. The library's one credibility asset is that it
does not claim what it has not earned, and a usage-free `stable` badge would spend that asset to buy
nothing. **If the maintainer wants that gate gone too, it is a one-line instruction and a separate record.
It is not implied by this one.**

### Two evaluations recorded here

**`docs/releases/v0.6.0.md` does not count as the first real usage cycle.**
[`evaluating-a-template.md`](../../how-to/evaluating-a-template.md) makes this the maintainer's call, and
the call is no. The document is genuine - stamped `source_template: release-notes`, version `0.1.1`, and it
found a real bug in the tool that filled it. It is also stamped `filled_by: agent:claude-opus-5`. An agent
filled a template, from this library, for this library's own release. Every participant in that loop is
inside the house. The dogfood was worth doing and it is not evidence about strangers.

**Distribution submissions wait.** Not blocked by a gate - ADR 0043 removed those and this record removes
their shadow. Held on judgment: the venue research is over two months old, and on 2026-09-11 this library
discovered that its headline `v0.6.0` feature could not start for anyone who followed its own install
instructions (DF-7 in [`STATE.md`](../../../STATE.md)). Directing strangers at it the same week is worse
timing than waiting.

### Consequences

* **Good:** WP-31, the site, Tier-2 bundles and M4 all become ordinary work, ranked by preference like
  everything else since [ADR 0041](0041-maintainer-preference-sets-the-build-order.md).
* **Good:** the repeal becomes checkable. A grep for constraint language over the tracked tree is a test
  this record can be held to.
* **Neutral:** one real fill is still the most valuable thing that could happen to this library. Nothing
  here says otherwise. It says only that its absence stops nothing.
* **Bad, and worth naming:** removing the language removes a reminder, and the thing it reminded about is
  real. The honesty gate is what keeps that from turning into a claim: with zero fills the bundles stay
  `beta`, so the absence is still visible in the metadata even when no prose is nagging about it.

### Confirmation

No tracked document describes a missing usage signal as a constraint or blocker. Every family contract
still carries its `beta` rule, `STATE.md` still publishes zero real fills as zero, and all 27 bundles still
declare `status: beta`.
