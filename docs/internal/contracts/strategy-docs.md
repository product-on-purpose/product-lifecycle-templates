# Family Contract: strategy-docs

Status: adopted 2026-07-25 ([ADR 0027](../decisions/0027-adopt-strategy-docs-family-contract.md)); amended 2026-10-12 ([ADR 0070](../decisions/0070-north-star-metrics-joins-strategy-docs-as-a-fifth-member.md)); amended 2026-10-19 ([ADR 0076](../decisions/0076-positioning-statement-joins-strategy-docs-as-a-sixth-member.md))
Applies to: every bundle declaring `family: strategy-docs` in its meta
Members at adoption: none built yet (product-vision, product-strategy, product-roadmap, okrs are the planned members)
Members: product-vision, product-strategy, product-roadmap, okrs, north-star-metrics ([ADR 0070](../decisions/0070-north-star-metrics-joins-strategy-docs-as-a-fifth-member.md), assigned and specced 2026-10-12 in [`tier2-specs.md`](../tier2-specs.md); built 2026-10-12), positioning-statement ([ADR 0076](../decisions/0076-positioning-statement-joins-strategy-docs-as-a-sixth-member.md), assigned and specced 2026-10-19 in [`tier2-specs.md`](../tier2-specs.md); not yet built)
Modeled on: the governance-docs contract (the first on the `classification` axis), on the delivery-docs and decision-docs contracts, on the pm-skills family-contract pattern
Axis: `classification`, spanning **two values** (`foundation` and `utility`); this is the first family to use a value **set** rather than a single value (see [ADR 0023](../decisions/0023-resolve-the-tier-1-family-taxonomy.md))
Version: 0.3.0 (changes to an obligation require a decision record; a dated in-place correction to an unsourced
claim does not, per [procedure 11](../decision-procedures.md#11-a-family-contract-asserts-something-about-the-world);
see the change note at the end)

## 1. Membership

A bundle belongs to this family when its document type **sets or tracks product direction above the level of
any single deliverable**. Its members answer, in order, six questions a product organization cannot avoid:

- a **product vision** says where we are trying to get to, and why it is worth getting to;
- a **product strategy** says which problems we will solve to get there, and which we will not;
- a **positioning statement** says how we stand against a named alternative, for which customer, now
  (added 2026-10-19, [ADR 0076](../decisions/0076-positioning-statement-joins-strategy-docs-as-a-sixth-member.md));
- a **North Star metric** says which single measure of customer value shows the strategy is moving us
  toward the vision, and which inputs drive it (added 2026-10-12,
  [ADR 0070](../decisions/0070-north-star-metrics-joins-strategy-docs-as-a-fifth-member.md));
- a **product roadmap** says in what order we intend to work on those problems;
- **OKRs** say what measurable change we expect in this period, and whether we got it.

The chain is the family's teaching value, and it runs downhill: a strategy that does not serve the vision is
drift, a roadmap that does not implement the strategy is a wishlist, and OKRs that do not measure progress
against the roadmap are a reporting exercise. **This library holds that** a North Star that does not measure
the strategy is a vanity metric, and that a roadmap that cannot say which input it moves has lost its link to
the North Star. That link is the library's POSITION: no source read states either failure as documented
practice. Its place fourth in the chain is inferred from four publishers who describe the North Star as
measuring the current strategy. No source states that sequence, and Tim Herbig orders the two the other way
(ADR 0070). **This library also holds that** a positioning statement that does not match the segment and
the problems the strategy has already chosen is drift the strategy already paid for. That link is also the
library's POSITION: no source read states this failure as documented practice either. Its place third in
the chain, between the strategy and the North Star metric, is argued from what positioning depends on, not
sourced; Devika Nair's framing of positioning "as part of the vision" (ADR 0076) pulls toward second place
instead. Each member must state its position against the other members in its companion's Relationships
section. That requirement is this library's own reasoning, not received practice (corrected 2026-08-07; see the
change note): no source read across any of the first four members' research logs documents teams producing all
four and having them contradict each other as a real-world failure mode, only named authors and sources
disagreeing with each other about how each document should be shaped. The library still holds that a chain asserted once, at the top, and
never rechecked from each member's side is the most likely way for its members to drift apart, which is the
reasoning behind the requirement.

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
| classification | **`foundation` or `utility`** - the first family contract to allow a set on the axis key. `foundation` for `product-vision`, `product-strategy`, `positioning-statement` and `north-star-metrics`; `utility` for `product-roadmap` and `okrs`. See the axis note below. A candidate whose honest axis is `phase` belongs in another family. |
| methodology | **Descriptive, not gated** (the [ADR 0020](../decisions/0020-adopt-delivery-docs-family-contract.md) lesson). This family is the sharpest illustration of why: `okrs` is genuinely **methodology-bound** (the artifact *is* the OKR method), and so is `north-star-metrics` (the artifact is the North Star Framework's own written output; added 2026-10-12), while the vision, the strategy, the positioning statement and the roadmap are methodology-agnostic. A single required value would force at least one member to lie about itself. |
| sizes_available | `[lean, full]`, or `[lean]` for a type whose own research shows it does not earn a second weight. The catalog's size calls are hypotheses, not facts (finding EC-2 in `STATE.md`); two qa-docs members have already departed from them on evidence. |
| status | `beta` until the maintainer judges the bundle settled; then `stable` eligible ([ADR 0055](../decisions/0055-retire-the-zero-fills-disclosure.md)) |
| pairs_with | the pm-skills skill ID(s) this template serves, or `[]`; every value must resolve against the pinned skill-ID list. **Unlike `qa-docs`, this family has real pairings**: `foundation-okr-writer` and `measure-okr-grader` both exist and both address `okrs` directly, and `foundation-lean-canvas` describes itself as serving strategy framing and stress-testing. Each member claims only what is true of that member. |

**The axis call, and why this family needs a set.** Every previous family gated a single value on its axis.
This one cannot, and forcing it to would misdescribe at least two of its members:

- **`product-vision` and `product-strategy` are `foundation`.** They underpin everything else, are argued
  rather than maintained, and change on a timescale of years. A vision revised quarterly was not a vision.
  **`north-star-metrics` is `foundation` too** (added 2026-10-12,
  [ADR 0070](../decisions/0070-north-star-metrics-joins-strategy-docs-as-a-fifth-member.md)). It is argued
  rather than maintained, and Amplitude and Mixpanel both describe revisiting it when the product, the market
  or the strategy shifts, not on a calendar. **`positioning-statement` is `foundation` too, recommended**
  (added 2026-10-19, [ADR 0076](../decisions/0076-positioning-statement-joins-strategy-docs-as-a-sixth-member.md)).
  No source read states a review cadence for it directly; this library infers it is argued and revisited at
  a repositioning event, not maintained on a calendar, the same shape already applied to its three siblings
  in this bullet.
- **`product-roadmap` and `okrs` are `utility`.** They are standing operational instruments, revised on a
  cadence, and their value comes precisely from being kept current. A roadmap nobody has updated in six
  months is not a stale foundation, it is a broken instrument.

The distinction that does the work is **argued-and-durable versus maintained-and-periodic**, and it is the
same distinction `governance-docs` used to claim `utility` for a risk register. All six members are standing
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
   comment grammar. A "How to fill this in" preamble sits inside each variant's opening comment block.
   *(Clarified 2026-10-12, the maintainer's call. This said the preamble "opens each variant", yet every
   member's variants open with frontmatter, and each places the preamble inside its first comment block. The
   same wording in `discovery-docs` led a review lens to file a false finding, and was clarified there on
   2026-09-30.)*
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
**chain their examples on one shared scenario**, because the artifacts only make sense as a cascade: the
strategy has to be a strategy *for* that vision, and the OKRs have to measure progress against *that*
roadmap. Independent examples would teach separate shapes and none of the relationships.

**And like `qa-docs`, this family chains onto the library's existing thread rather than a new scenario** -
but from the other end. `qa-docs` extended the Acme Analytics story **downward** into verification; this
family extends it **upward** into direction. The hook already exists in the repository: the
[PRD example](../../../templates/prd/prd_example.md) states that Saved Views serves the FY26 **"Time to
Insight"** company goal, and the [kpi-dashboard example](../../../templates/kpi-dashboard/kpi-dashboard_example.md)
wires its primary metric to that goal's panel. Those references were written before this family existed and
now have something to point at.

The obligation: each member's example is an Acme Analytics artifact, the OKR example makes "Time to Insight"
its objective, and the roadmap example must contain the work the PRD describes. The North Star metric's example
names Acme's North Star and its inputs, and states how they relate to the "Time to Insight" company goal (added
2026-10-12, [ADR 0070](../decisions/0070-north-star-metrics-joins-strategy-docs-as-a-fifth-member.md); its spec
in [`tier2-specs.md`](../tier2-specs.md) sets the constraints). The positioning statement's example states
Acme's positioning against a named alternative, for the segment the product strategy example already chose,
and contradicts neither sibling (added 2026-10-19,
[ADR 0076](../decisions/0076-positioning-statement-joins-strategy-docs-as-a-sixth-member.md); its spec sets
the constraints). **When this family completes,
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

**0.3.0, 2026-10-19, [ADR 0076](../decisions/0076-positioning-statement-joins-strategy-docs-as-a-sixth-member.md):
a sixth member, and the second widening of this family's list of questions.** `positioning-statement` joins
at `classification: foundation` (recommended), placed third in the chain, between the product strategy and
the North Star metric, which moves from third place to fourth. That place is argued rather than sourced,
and ADR 0076 records why, and names a second place (between the vision and the strategy) as the considered
alternative. The membership sentence admitted the type as written. What blocked it was the closed list that
follows the sentence, so section 1's "five questions" becomes "six questions" and gains a third bullet. The
chain sentence gains a second link, also labelled the library's POSITION. Section 2's classification row,
methodology row and axis note name the new member, and the axis note now counts six members. Section 4's
obligation gains its example. **No structural obligation changed**, and check K's registry entry needs no
edit, because `foundation` is already in the set it gates, and `[lean]` alone is already an allowed
`sizes_available` value. The `product-strategy`, `north-star-metrics`, `product-roadmap` and `okrs`
companions gain no line; ADR 0076 states that gap. `product-vision`'s own companion carries a dated
correction when the bundle is built, not an amendment to this contract; ADR 0076 and the bundle's own spec
state it.

**0.2.0, 2026-10-12, [ADR 0070](../decisions/0070-north-star-metrics-joins-strategy-docs-as-a-fifth-member.md):
a fifth member, and the first widening of this family's list of questions.** `north-star-metrics` joins at
`classification: foundation`, placed third in the chain, between the product strategy and the product roadmap.
That place is inferred rather than sourced, and ADR 0070 records why. The membership sentence admitted the type
as written. What blocked it was the closed list that follows the sentence, so section 1's "four questions"
becomes "five questions" and gains a third bullet. The roadmap bullet's "work on them" becomes "work on those
problems", because the new bullet now sits between it and the strategy. The chain sentence gains one link,
labelled the library's POSITION, and the relationship obligation reads "against the other members" rather than
"against the other three". Section 2's classification row, methodology row and axis note name the new
member, and section 4's obligation gains its example. **No structural obligation changed**, and check K's registry
entry needs no edit, because `foundation` is already in the set it gates. The `product-strategy`,
`product-roadmap` and `okrs` companions never mention a North Star and gain no line; ADR 0070 states that gap.

**2026-10-12: a wording clarification, with no obligation changed.** Section 3 said a "How to fill this
in" preamble "opens each variant". Every member's variants open with frontmatter and carry the preamble
inside their first comment block. Section 3 now says so, with a dated note beside the sentence. The same
wording in `discovery-docs` led a review lens to file a false finding, and was clarified there on
2026-09-30. The maintainer chose this on 2026-10-12 after reading the exact text. No version moves, because
no obligation changed.

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
