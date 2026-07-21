---
status: accepted
date: 2026-07-20
decision-makers: [jprisant]
consulted: [claude]
---

# Complete the Tier-1 floor on a schedule; grow-by-pull governs Tier-2 and Tier-3 only

## Context and Problem Statement

The repo's standing rule is **grow by pull, not speculation**: no bundle gets built until a real request or a named internal need pulls it (audit Catalog Recommendation 1, "demand is a gate, not just a weight"). The rule exists for a good reason: building templates nobody uses is easy busywork that substitutes for the hard work of finding real users, and zero real usage is the library's most weighted weakness.

But the library covers **6 of the catalog's 27 Tier-1 "must-have" types**. A product-lifecycle template library that thin has a credibility-floor problem the machine layer cannot fix, and it risks a chicken-and-egg trap: too incomplete to be worth pulling into, so it stays incomplete because nothing pulls. The maintainer's call is to build the full Tier-1 floor to establish a best-in-class comprehensive foundation.

## Decision Drivers

- The 27 Tier-1 types are the catalog's own `must_have` baseline; completing a defined baseline differs from open-ended speculation.
- A comprehensive foundation is table stakes for the library to be taken seriously and to be pull-worthy at all.
- The risk grow-by-pull guards against (mistaking coverage for traction) is real but can be neutralized by a single discipline: honest usage claims.

## Considered Options

* **Option A: complete the Tier-1 floor on a schedule, keep grow-by-pull for Tier-2 and Tier-3.** Chosen.
* **Option B: keep strict grow-by-pull** and build nothing without a demand signal.
* **Option C: build everything speculatively** (Tier-1, Tier-2, Tier-3).

## Decision Outcome

Chosen: **A. Build the 21 remaining Tier-1 bundles on a schedule, per [`docs/internal/buildout-plan.md`](../buildout-plan.md). Grow-by-pull still governs Tier-2 and Tier-3.**

This amends the audit's Catalog Recommendation 1 for the Tier-1 set only. Tier-2 and Tier-3 remain strictly demand-gated: a candidate outside the Tier-1 floor still needs a real pull to be built.

**The one discipline kept from grow-by-pull:** a bundle is never called "verified", "proven", or "complete" on the strength of a green gate. STATE.md keeps coverage (how many bundles exist) and traction (how many have been filled by a real user) as separate, honestly-stated numbers, and "zero real usage" stays visible until it is not true. This is what keeps floor-completion from being self-deception.

Option B was rejected because the chicken-and-egg is real: the library is too thin to pull, so waiting for a pull waits forever. Option C was rejected because open-ended speculation is exactly the waste grow-by-pull correctly forbids; the Tier-1 floor is a bounded, defined target, not a blank cheque.

### Consequences

* Good: the library reaches a credible, comprehensive foundation (27 of 27 Tier-1) rather than sitting at 6.
* Bad, accepted: the maintenance surface grows to 27 bundles with still-zero external usage; the bet is that a credible foundation earns the pull a thin one never will.
* Bad, accepted: 21 more bundles is 21x the surface for the citation-defect class the gate cannot catch (WP-10 found 28 in the first six). Mitigated by mandatory adversarial citation verification per bundle and a maintainer read before merge (buildout-plan section on the pipeline).
* Neutral: the build is bounded. When the Tier-1 floor is complete, growth reverts to pull for Tier-2 and Tier-3.

### Confirmation

`docs/internal/buildout-plan.md` (adopted by this ADR) is the executable plan. Each bundle ships gate-green (eleven checks) and maintainer-reviewed. STATE.md tracks real usage separately from coverage, and its "zero real usage" line stays until a real fill exists.

## More Information

Amends the grow-by-pull framing in the audit, the roadmap ("scale by pull"), and STATE.md for the Tier-1 floor only. Each new family the floor requires gets its own contract ADR on the [ADR 0020](0020-adopt-delivery-docs-family-contract.md) pattern before its members are enforced as family members.
