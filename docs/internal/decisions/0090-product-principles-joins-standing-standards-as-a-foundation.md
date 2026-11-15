---
status: accepted
date: 2026-11-14
decision-makers: [jprisant]
consulted: [claude]
---

# `product-principles` is a type of its own, and joins `standing-standards` as a `foundation`

## TL;DR

- **Decision.** A `product-principles` bundle (issue #360, bundle: product-principles) declares
  **`family: standing-standards`** and **`classification: foundation`**. It joins with
  [ADR 0089 (design principles joins standing-standards)](0089-design-principles-joins-standing-standards-as-a-foundation.md),
  which widened the family's membership sentence.
- **What the type is.** It is the short set of beliefs a product team uses to resolve product trade-offs, written to
  complement its vision and strategy. Marty Cagan: "I always like to complement the product vision and product
  strategy with a set of product principles."
- **What it is not.** It is not the Product Principles section of `product-strategy`'s one-pager full variant. That
  section summarises the set inside a strategy; this bundle is the standing set itself.
- **Status:** accepted 2026-11-14. The two sweep critics split on whether the type is already covered. The maintainer
  ruled "d2 a", a type of its own, then asked for a family recommendation and accepted it ("D4 ok").

## Context and Problem Statement

Backlog section 9.1 listed the product principles document with one source, a Productboard AI prompt, and proposed
testing it as a duplicate first. [ADR 0087 (product discovery plan declined)](0087-product-discovery-plan-is-declined.md)
had mapped Cagan's "Product Principles" component to `product-strategy` (line 83). Admission sweep 8 tested both
questions on 2026-11-14, and the main loop read Cagan's chapters in the maintainer's copies of *Inspired* (chapter 27)
and *Empowered* (chapter 39). The working files are gitignored, at `_local/research/2026-11-14_admission-sweep-8/`.

**The checks.**

1. **Written document.** It passes, at medium confidence. Cagan gives product principles a chapter in each book, and
   *Empowered* says "Product principles complement the product vision". GitLab's handbook keeps a standalone page.
   Cagan's 2005 PRD guide has a step titled "Define your Product Principles".
2. **Phase fit.** Not applicable.
3. **Written form.** It passes: a short prose list.
4. **Not duplicated.** This was the open judgment. Only `product-strategy_template-one-pager-full.md` (line 157)
   carries a principles section. The default kernel format has none.
5. **Software audience.** It passes: GitLab's product organisation, Monzo and SVPG.

## Decision Drivers

- Sources place product principles in four homes: standalone (Cagan's books, GitLab, Productboard), a step in a PRD
  (Cagan 2005), a vision page (Monzo) and a strategy one-pager. That spread is why neither critic called the overlap
  clear.
- One section in one non-default format is weaker coverage than ADR 0074's "already ships" standard required.
- The family should place sibling types where their guides can draw the line between them.

## Considered Options

1. **A type of its own, in `standing-standards` as `foundation`.** Chosen.
2. **A type of its own, in `strategy-docs`.** Rejected. Its question list is closed, and this would be a second
   widening in the same change as [ADR 0091 (competitive analysis joins strategy-docs)](0091-competitive-analysis-joins-strategy-docs-as-an-eighth-member.md).
   Cagan ties the principles to the vision, but the family follows how a document is used, not what it sits beside.
3. **Covered by `product-strategy`.** The first critic's recommendation, at medium confidence. Not chosen by the
   maintainer.

## Decision Outcome

**Chosen: its own type, `standing-standards`, `classification: foundation`.**

- **Membership.** The widened sentence from ADR 0089 reads "what every decision about its product must honour". That
  describes product principles almost word for word, so this member needs no further amendment.
- **The falsifier.** Product principles are consulted at the moment a trade-off is decided. The shipped one-pager's
  own guidance says principles "let people decide without asking".
- **Classification.** A trade-off is judged against the principles; nobody executes them under time pressure. That is
  `foundation`.
- **Two types, not one.** GitLab's Pajamas page says "There are two kinds of principles", and Productboard ships two
  separate prompts. NN/g writes only about design principles, and SVPG only about product principles. The weakness:
  GitLab's own split is process against output, which is not quite this split.

### Consequences

- `standing-standards` grows to ten members with ADR 0089, at `0.8.0`.
- **`product-strategy` keeps its one-pager section.** Its guidance should point at this bundle for the full set at
  the bundle's landing. ADR 0087 gains a dated note that its mapping now has a dedicated bundle.
- **Corrections owed, made in this change:** `product-strategy_history.md` said the spec's Principles "survive in the
  full variant", which is true of the one-pager only; catalog row 2 lists "principles" among `product-strategy`'s key
  sections, which is true of the one-pager only.
- The guide must state the difference from design principles, since the skeletons will be similar.
- The catalog row lands at the build.

## More Information

- The sibling record: [ADR 0089](0089-design-principles-joins-standing-standards-as-a-foundation.md).
- The earlier mapping: [ADR 0087](0087-product-discovery-plan-is-declined.md), line 83.
- Family contract: [`standing-standards`](../contracts/standing-standards.md).
