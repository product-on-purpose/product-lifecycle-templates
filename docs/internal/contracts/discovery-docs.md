# Family Contract: discovery-docs

**Status:** **adopted 2026-08-04**, [ADR 0031](../decisions/0031-adopt-discovery-docs-family-contract.md).
Registered in check K, which now gates `phase: discover` on every member.
**Axis:** `phase`, single value `discover`.
**Members:** `business-case`, `user-persona`, `prototype-brief`.

This contract is written **before any member is built**, following the
[ADR 0020 (delivery-docs family contract)](../decisions/0020-adopt-delivery-docs-family-contract.md) pattern
that `qa-docs` and `strategy-docs` both used. Writing it first is what stops the contract being
reverse-engineered to fit whatever got built.

## 1. Membership

A bundle belongs to this family when its document type exists **to decide whether to build something, before
anyone commits to building it.** Its members answer, in order, three questions that precede every product
decision:

- a **business case** says whether the investment is worth making, and what it is being compared against;
- a **user persona** says who we are building for, grounded in research rather than in imagination;
- a **prototype brief** says what to build cheaply first, in order to find out whether we are right.

The thread runs *toward* commitment rather than away from it. A business case that names no alternative is a
proposal; a persona assembled from opinion is a stereotype; a prototype brief that specifies a finished
product is a PRD wearing a smaller name. Each member must say, in its companion's Relationships section, what
it is **not** and which document takes over when the decision is made.

A candidate whose job is to **set direction over time** belongs to `strategy-docs`. A candidate that
**specifies, decomposes or verifies a unit of work** belongs to `delivery-docs` or `qa-docs`. A candidate that
is a **standing instrument revised on a cadence** belongs to a `classification` family. This family is
phase-bound by construction: every member is written once for a decision, and is finished when that decision
is made.

**On `prototype-brief`, and it is provisional.** It is a **new type**, added by
[ADR 0030 (templating scope)](../decisions/0030-templating-scope-markdown-documents.md), not a rename of
catalog 54. **Its membership is conditional on its own research passing ADR 0030's admission test**: a named
source must publish this as a written document. That test was applied rigorously to reject `wireframe` and
has not yet been applied with equal rigour to admit this. **If the research finds no named source, the type
does not ship and this family has two members**, which is a legitimate outcome and not a failure of the
contract. Catalog 54 (`interactive-prototype`) is out of scope for templating because its artifact is
executable; the brief that **commissions** the prototype is a document, and that is what ships. The
distinction matters and must be stated in the bundle: renaming an out-of-scope artifact to claim its slot is
the defect this library rejected when it excluded V2MOM.

**On membership placement.** `prototype-brief` sits here rather than in a design family because families are
defined by what a document **does**, and this one commissions and validates. The catalog's own entry for the
prototype is categorised "design/**validation**" and staged at "validation, handoff". If the bundle's research
shows its dominant use is handoff-to-build rather than testing an assumption, `phase: develop` becomes the
better call and this placement should be revisited at that point, per
[`decision-procedures.md`](../decision-procedures.md) section 10.

## 2. Required catalog metadata and allowed values

Every member's `<type>_meta.yaml` carries the full field set defined by the
[metadata schema](../../../tools/meta.schema.json), with these family-specific constraints:

| Field | Allowed values for this family |
|---|---|
| family | `discovery-docs` |
| phase | **`discover`**, single value. A candidate whose honest axis is `classification` belongs in another family; this family has no standing instruments |
| methodology | **Descriptive, not gated** (the [ADR 0020](../decisions/0020-adopt-delivery-docs-family-contract.md) lesson). Members will differ: a business case is methodology-agnostic, a persona leans research-practice, a prototype brief leans dual-track or design-thinking. A single required value would force at least one to misdescribe itself |
| sizes_available | `[lean, full]`, or `[lean]` for a type whose own research shows it does not earn a second weight. The catalog's size calls are hypotheses, not facts (finding EC-2 in `STATE.md`), and two `qa-docs` members have already departed from them on evidence |
| status | `beta` until one real usage cycle is recorded; then `stable` eligible |
| pairs_with | the pm-skills skill ID(s) this template serves, or `[]`; every value must resolve against `tools/known-skills.txt`. **Verify per member at authoring time and claim only what is true of that member.** Do not assume this family has pairings; `qa-docs` found it had almost none (finding EC-4) |

## 3. Structural obligations (gate-checkable)

1. **The eight files.** Every member ships all eight roles: template-lean, template-full (where two sizes
   exist), companion, guide, example, meta.yaml, history, research-log; filenames prefixed `<type>_`.
2. **Nesting.** Where two sizes exist, the lean variant's H2 sections are a strict ordered subset of the full
   variant's; shared sections keep name and order. Single-size members are exempt from nesting, not from
   anything else.
3. **Guidance comments.** Every section of every variant carries the Approach A comment (WHAT, WHY with a
   companion pointer, ASK, GOOD, WEAK, TRAP; PRIORITY and ROW HINT for table sections). A "How to fill this
   in" preamble opens each variant, and states the N/A rule and the self-grade step.
4. **Companion skeleton.** All 11 sections of methodology section 5, in order, with **one Anatomy subsection
   per template section**. An inapplicable section says so in one line rather than being dropped.
5. **Guide shape.** When to use; when NOT to use; pick a variant; a self-gradable rubric conforming to
   [`guide-rubric-spec.md`](../guide-rubric-spec.md); at least six named anti-patterns.
6. **Citations.** Methodology section 6 in full. **This family's specific citation hazard is the
   unfalsifiable number**: business cases and personas both attract invented percentages, and the prototype
   literature attracts vendor claims. Every figure traces to a logged source or is cut.
7. **Example.** One fully worked instance, no placeholders, illustrative figures labeled, provenance
   frontmatter stamped, and **independent of the template's own GOOD and WEAK text** per
   `tools/check-example-independence.py`. No member of this family is grandfathered.

## 4. The shared-scenario rule (family-specific)

Like every family except `decision-docs`, members chain their examples on **one shared scenario**, and like
`qa-docs` and `strategy-docs` this family chains onto the library's existing **Acme Analytics** thread rather
than inventing a new company.

**The direction is different from its siblings, and that is the point.** `qa-docs` extended the thread
*downward* into verification; `strategy-docs` extended it *upward* into direction. This family extends it
**backward, to before the decision was made**:

- the **business case** justifies the investment that the FY26 product strategy later spends;
- the **user persona** is the Recurring Analyst that the vision, the strategy and every PRD already assume
  without ever having defined;
- the **prototype brief** commissions the cheap test of the question-first entry hypothesis that the roadmap
  carries in its Now lane and the strategy records as an unproven assumption.

**The obligation:** each member's example is an Acme Analytics artifact, and each one must **connect to a fact
that already exists in the library** rather than a new invention. The Recurring Analyst in particular is
already named in `kpi-dashboard`'s metric definitions and in the `acceptance-criteria` example; the persona
bundle defines the person those documents have been referring to for months.

**One chronology obligation, added on evidence.** A discovery document is written **before** the documents it
leads to. Its example's date must precede the artifacts it anticipates, and it must not cite them as existing.
The `product-roadmap` example shipped dated February while citing a PRD created in June, and that defect is
easier to commit in this family than any other, because every member points forward.

## 5. Shareable-boundary rule

Template body (headings, placeholders, tables) is the reusable shape; guidance lives only in comments; example
content never leaks into templates; meta describes the asset, never the filled instance. A member whose guide
has grown explanatory (companion material) or whose companion has grown procedural (guide material) is out of
contract even if every file exists.

## 6. Enforcement

The gate enforces section 2 and the mechanical part of section 3. **Family check letter K** validates section
2's family-specific values for every declared member (a `phase` of `discover`, a `beta`/`stable` status, and a
`[lean, full]` or `[lean]` size shape) and that this contract file resolves; methodology is descriptive and is
not gated. A member declaring `classification` instead of `phase` fails check K with a message naming the axis
it should have used.

Of section 3's obligations, the eight files (3.1), nesting (3.2), citations (3.6) and the clean example (3.7)
are enforced by checks A, C, E and D; the example-independence half of 3.7 is enforced by
`tools/check-example-independence.py`, and **no member of this family may be added to its grandfather list**.
Guidance comments (3.3), the companion skeleton (3.4) and guide shape (3.5) have no mechanical check and are
review obligations at authoring time. Sections 4 and 5 are review obligations at authoring time and audit
obligations thereafter.

A member failing this contract is not "in the family with issues"; it is out of the family until green, and
the catalog count reflects that.

## Change note

**0.1.0 (proposed 2026-07-30):** drafted, pending maintainer review. The sixth family contract, the third on
the `phase` axis, and the first to include a **type that does not exist in the catalog**: `prototype-brief`,
added by [ADR 0030 (templating scope)](../decisions/0030-templating-scope-markdown-documents.md) after
`wireframe` and `interactive-prototype` were ruled out of scope for templating. `business-case` arrives here
from `strategy-docs` by [ADR 0023 (the Tier-1 family taxonomy)](../decisions/0023-resolve-the-tier-1-family-taxonomy.md),
which moved it on the reasoning that a one-time, phase-bound artifact does not belong in a family of standing
instruments.
