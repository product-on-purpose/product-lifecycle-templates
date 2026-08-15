---
status: accepted
date: 2026-08-14
decision-makers: [jprisant]
consulted: [claude]
---

# Free and open source, with no paid tier, funded by the maintainer's time

## TL;DR

- **Decision:** this library is and stays **free and open source under Apache-2.0**. No paid tier, no gated
  bundles, no commercial licence, no sponsorship gate on content. Its commercial function is as an
  **authority funnel** for product-on-purpose, not as a product that charges.
- **Why:** decision **VL-1 (business model)** has been open since 2026-07-02 with no stated resolution cost
  and no scheduled date, and it **blocks the site**, which cannot choose a domain or a call to action
  without it. The roadmap's own recommended default (WP-54) was free and open; the maintainer confirmed it
  on 2026-08-14.
- **Status:** accepted 2026-08-14. Closes VL-1. Unblocks the site track.

## Context and Problem Statement

The library has been Apache-2.0 since M0 and has never charged for anything, so in practice this decision
has been made by default for six weeks. What it lacked was a written position, and the absence had a cost:
the site plan named a launch decision it could not make, because a landing page has to say what it wants the
reader to do, and that depends on whether anything is for sale.

Leaving it open also left a live question about whether any future content could be gated, which affects
what the contribution terms and the licence file are allowed to promise.

## Decision Drivers

* **The moat is credibility, and credibility compounds through reach.** The differentiator is researched,
  cited, gate-enforced content. That is worth more as evidence of judgment seen by many people than as a
  small paid product seen by few.
* **A paid tier has fixed costs this project cannot currently carry**: entitlement, access control, support
  expectations, a second licence, and a refund position. At 10 to 15 hours a week with zero users, that is
  overhead against no revenue.
* **Apache-2.0 is already granted at the repository root** and has been since M0. Retracting openness later
  would be a supersession with real reputational cost; confirming it costs nothing.
* **The unresolved decision was itself the problem.** It had aged six weeks past a three-day SLA and was
  blocking a whole track.

## Considered Options

* **A. Free and open, authority funnel.** Chosen.
* **B. Open core**, with some bundles or the regulated tier paid. Rejected for now: it requires entitlement
  machinery, and the regulated tier that would most plausibly carry a price is separately closed as "no"
  (decision D4). Building the machinery before the content would be exactly the sequencing error this
  roadmap exists to avoid.
* **C. Sponsorship or donation.** Not rejected, and not adopted: it is compatible with A and can be added at
  any time without a decision record, because it gates nothing.

## Decision Outcome

**Chosen: A. Free and open source, no paid tier.**

The library's commercial role is to demonstrate the standard of thinking that product-on-purpose sells.
Nothing in the repository is withheld, time-limited, or licence-restricted beyond Apache-2.0's terms.

### What this unblocks

* **The site track.** The two plans in `_local/planning/` (the Starlight site and the samples showcase) can
  proceed to a launch decision. They remain unratified on their own merits; they are simply no longer
  blocked by this.
* **The contribution terms**, which can now state plainly that contributions are Apache-2.0 and will never
  be moved behind a paywall.

## Consequences

* **Good:** the widest possible distribution, which is the correct optimisation while the binding constraint
  is that nobody uses the library.
* **Good:** no entitlement, access-control, or support-tier machinery ever needs building.
* **Good:** the honesty posture and the business model now agree. A library that publishes its own VOID eval
  results is not one that could comfortably charge for them.
* **Bad, and stated plainly: the maintenance is funded by the maintainer's time, indefinitely, with no
  mechanism that scales it.** That is a real constraint on how large this library should get, and it is the
  strongest argument for the maintenance cadence in VL-3. **It is also the counterweight to
  [ADR 0039](0039-maintainer-discretion-replaces-the-pull-gate.md)**, which just removed the rule limiting
  how many bundles may be built: nothing now caps the maintenance surface except the maintainer's own
  judgment about what they can keep fresh.
* **Neutral:** revenue attribution will be indirect and hard to measure. No mechanism here will show which
  engagement came from which bundle, and none is proposed.

## More Information

* Roadmap WP-54 (VL-1 positioning executed), which recommended this default.
* [ADR 0039](0039-maintainer-discretion-replaces-the-pull-gate.md), whose accepted cost this record
  sharpens: discretion to build plus no funding mechanism means the maintenance surface is bounded only by
  judgment.
* [ADR 0013 (the `_local/` split and going public)](0013-local-split-and-going-public.md), which established
  the public posture this record confirms.
