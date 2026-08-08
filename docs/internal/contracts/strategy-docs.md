# Family Contract: strategy-docs

Status: adopted 2026-07-25 ([ADR 0027](../decisions/0027-adopt-strategy-docs-family-contract.md))
Applies to: every bundle declaring `family: strategy-docs` in its meta
Members at adoption: none built yet (product-vision, product-strategy, product-roadmap, okrs are the planned members)
Modeled on: the governance-docs contract (the first on the `classification` axis), on the delivery-docs and decision-docs contracts, on the pm-skills family-contract pattern
Axis: `classification`, spanning **two values** (`foundation` and `utility`); this is the first family to use a value **set** rather than a single value (see [ADR 0023](../decisions/0023-resolve-the-tier-1-family-taxonomy.md))
Version: 0.1.1 (changes to an obligation require a decision record; a dated in-place correction to an unsourced
claim does not, per [procedure 11](../decision-procedures.md#11-a-family-contract-asserts-something-about-the-world);
see the change note at the end)

## 1. Membership

A bundle belongs to this family when its document type **sets or tracks product direction above the level of
any single deliverable**. Its members answer, in order, four questions a product organization cannot avoid:

- a **product vision** says where we are trying to get to, and why it is worth getting to;
- a **product strategy** says which problems we will solve to get there, and which we will not;
- a **product roadmap** says in what order we intend to work on them;
- **OKRs** say what measurable change we expect in this period, and whether we got it.

The chain is the family's teaching value, and it runs downhill: a strategy that does not serve the vision is
drift, a roadmap that does not implement the strategy is a wishlist, and OKRs that do not measure progress
against the roadmap are a reporting exercise. Each member must state its position against the other three in
its companion's Relationships section. That requirement is this library's own reasoning, not received
practice (corrected 2026-08-07; see the change note): no source read across any of the four members' research
logs documents teams producing all four and having them contradict each other as a real-world failure mode,
only named authors and sources disagreeing with each other about how each document should be shaped. The
library still holds that a chain asserted once, at the top, and never rechecked from each member's side is the
most likely way for the four to drift apart, which is the reasoning behind the requirement.

A candidate type whose job is to specify, decompose or verify a **unit of work** belongs to `delivery-docs`
or `qa-docs`, not here. A candidate that is a **one-time, phase-bound** artifact belongs elsewhere too: this
is why `business-case` is **not** a member, having moved to `discovery-docs` at `phase: discover`
([ADR 0023](../decisions/0023-resolve-the-tier-1-family-taxonomy.md)); it is written once to justify an
investment decision and is then finished, which is the definition of a phase artifact.

## 2. Required catalog metadata and allowed values

Every member's `<type>_meta.yaml` carries the full field set defined by the
[metadata schema](../../../tools/meta.schema.json) (methodology B5), with these family-specific constraints:

| Field | Allowed values for this family |
|---|---|
| family | `strategy-docs` |
| classification | **`foundation` or `utility`** - the first family contract to allow a set on the axis key. `foundation` for `product-vision` and `product-strategy`; `utility` for `product-roadmap` and `okrs`. See the axis note below. A candidate whose honest axis is `phase` belongs in another family. |
| methodology | **Descriptive, not gated** (the [ADR 0020](../decisions/0020-adopt-delivery-docs-family-contract.md) lesson). This family is the sharpest illustration of why: `okrs` is genuinely **methodology-bound** (the artifact *is* the OKR method) while the other three are methodology-agnostic. A single required value would force one of the four to lie about itself. |
| sizes_available | `[lean, full]`, or `[lean]` for a type whose own research shows it does not earn a second weight. The catalog's size calls are hypotheses, not facts (finding EC-2 in `STATE.md`); two qa-docs members have already departed from them on evidence. |
| status | `beta` until one real usage cycle is recorded; then `stable` eligible |
| pairs_with | the pm-skills skill ID(s) this template serves, or `[]`; every value must resolve against the pinned skill-ID list. **Unlike `qa-docs`, this family has real pairings**: `foundation-okr-writer` and `measure-okr-grader` both exist and both address `okrs` directly, and `foundation-lean-canvas` describes itself as serving strategy framing and stress-testing. Each member claims only what is true of that member. |

**The axis call, and why this family needs a set.** Every previous family gated a single value on its axis.
This one cannot, and forcing it to would misdescribe two of its four members:

- **`product-vision` and `product-strategy` are `foundation`.** They underpin everything else, are argued
  rather than maintained, and change on a timescale of years. A vision revised quarterly was not a vision.
- **`product-roadmap` and `okrs` are `utility`.** They are standing operational instruments, revised on a
  cadence, and their value comes precisely from being kept current. A roadmap nobody has updated in six
  months is not a stale foundation, it is a broken instrument.

The distinction that does the work is **argued-and-durable versus maintained-and-periodic**, and it is the
same distinction `governance-docs` used to claim `utility` for a risk register. All four members are standing
artifacts with no single lifecycle phase, which is what makes the family `classification`-axis; they simply
sit in two different classes within it.

Check K has supported a set on the axis key since [ADR 0023](../decisions/0023-resolve-the-tier-1-family-taxonomy.md),
which added it precisely because this family was known to be coming, and `tools/test-check-k.py` has carried a
`strategy-docs` fixture asserting exactly this behaviour ever since. **This contract is the first live use of
that capability**, and the fixture becomes a real subject when the first member lands.

## 3. Structural obligations (gate-checkable)

1. **The eight files.** Every member ships all eight roles: template-lean, template-full (where two sizes
   exist), companion, guide, example, meta.yaml, history, research-log; filenames prefixed `<type>_`.
2. **Nesting.** Where two sizes exist, the lean variant's H2 sections are a strict ordered subset of the full
   variant's; shared sections keep name and order. Single-size members are exempt from nesting, not from
   anything else.
3. **Guidance comments.** Every section of every variant carries the Approach A comment (WHAT, WHY with a
   companion pointer, ASK, GOOD, WEAK, TRAP; PRIORITY and ROW HINT for table sections), parseable under the
   comment grammar. A "How to fill this in" preamble opens each variant.
4. **Companion skeleton.** All 11 sections of methodology section 5, in order; an inapplicable section says
   so in one line rather than being dropped.
5. **Guide shape.** When to use; when NOT to use; pick a variant; a self-gradable quality rubric; at least
   two named anti-patterns.
6. **Citations.** Methodology section 6 in full: numbered, reliability-tagged, anchored, hyperlinked, cited
   inline, no padded entries, retrieval qualifiers on any source not directly fetched. **This family carries a
   specific citation hazard**: its canonical sources are largely books and named practitioners rather than
   standards, so misattribution is the likely failure mode rather than staleness. Verify who said what before
   quoting it.
7. **Example.** One fully worked instance, no placeholders, illustrative figures labeled, provenance
   frontmatter stamped.

## 4. The shared-scenario rule (family-specific)

Like `delivery-docs`, `governance-docs` and `qa-docs`, and unlike `decision-docs`, `strategy-docs` members
**chain their examples on one shared scenario**, because the four artifacts only make sense as a cascade: the
strategy has to be a strategy *for* that vision, and the OKRs have to measure progress against *that*
roadmap. Four independent examples would teach four shapes and none of the relationships.

**And like `qa-docs`, this family chains onto the library's existing thread rather than a new scenario** -
but from the other end. `qa-docs` extended the Acme Analytics story **downward** into verification; this
family extends it **upward** into direction. The hook already exists in the repository: the
[PRD example](../../../templates/prd/prd_example.md) states that Saved Views serves the FY26 **"Time to
Insight"** company goal, and the [kpi-dashboard example](../../../templates/kpi-dashboard/kpi-dashboard_example.md)
wires its primary metric to that goal's panel. Those references were written before this family existed and
now have something to point at.

The obligation: each member's example is an Acme Analytics artifact, the OKR example makes "Time to Insight"
its objective, and the roadmap example must contain the work the PRD describes. **When this family completes,
the library will hold one continuous worked thread from a product vision down to a bug report**, which is a
demonstration no single bundle can make. A member whose example invents an unrelated company forfeits that and
is out of contract even if every file exists.

## 5. Shareable-boundary rule

Template body (headings, placeholders, tables) is the reusable shape; guidance lives only in comments; example
content never leaks into templates; meta describes the asset, never the filled instance. A member whose guide
has grown explanatory (companion material) or whose companion has grown procedural (guide material) is out of
contract even if every file exists.

## 6. Enforcement

The gate enforces section 2 and the mechanical part of section 3. **Family check letter K** validates section
2's family-specific values for every declared member (a `classification` of **either** `foundation` or
`utility`, a `beta`/`stable` status, and a `[lean, full]` or `[lean]` size shape) and that this contract file
resolves; methodology is descriptive and is not gated (see section 2). A member declaring `phase` instead of
`classification` fails check K with a message naming the axis it should have used, and a member declaring
`classification: tool` fails with a message listing the allowed set, because the check reports the set rather
than a single value ([ADR 0023](../decisions/0023-resolve-the-tier-1-family-taxonomy.md)). Of section 3's
obligations, the eight files (3.1), nesting (3.2), citations (3.6), and the clean example (3.7) are enforced
by checks A, C, E, and D respectively; guidance comments (3.3), the companion skeleton (3.4), and guide shape
(3.5) have no mechanical check yet and are review obligations at authoring time. Sections 4 and 5 are likewise
review obligations at authoring time and audit obligations thereafter. A member failing this contract is not
"in the family with issues"; it is out of the family until green, and the catalog count reflects that.

**One consequence of the value set worth stating plainly.** Because check K accepts either value, it cannot
tell you that a *specific* member picked the *right* one: nothing mechanical stops `product-vision` declaring
`utility`. That assignment is a review obligation, and section 2's argued split is the standard it is
reviewed against.

## Change note

**0.1.1 (2026-08-07), per
[procedure 11](../decision-procedures.md#11-a-family-contract-asserts-something-about-the-world):** section 1's
"most common real-world failure" sentence corrected in the dated in-place pattern this library uses for the
catalog (finding EC-2), not by a superseding decision record. Searching all four members' research logs
(`product-vision`, `product-strategy`, `product-roadmap`, `okrs`) for evidence of teams producing all four
artifacts and having them contradict each other found none; every relevant hit was named authors or sources
disagreeing with each other about how a single document type should be shaped, not evidence about multi-document
drift in practice. The obligation is unchanged: every member still states its position against the other three
in its companion's Relationships section. Only the reason given for that obligation is relabelled, from an
unsourced claim about the world to this library's own reasoning.

**0.1.0 (2026-07-25, [ADR 0027](../decisions/0027-adopt-strategy-docs-family-contract.md)):** adopted,
enforced by gate check K, the fifth family contract and **the first to gate a set of axis values rather than
one**. Adopted before any member is built (contract-first, per the [ADR 0020](../decisions/0020-adopt-delivery-docs-family-contract.md)
pattern). Methodology descriptive from the start, with `okrs` as the clearest case yet of why a methodology
field cannot be a membership rule. The two-class split (`foundation` for vision and strategy, `utility` for
roadmap and OKRs) was ratified in principle by [ADR 0023](../decisions/0023-resolve-the-tier-1-family-taxonomy.md)
and is argued against the real members here, as that decision required.
