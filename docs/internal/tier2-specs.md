# Tier-2 build-out: per-type specs and progress

Companion to [`buildout-specs.md`](buildout-specs.md), which is the **Tier-1 floor** spec sheet and says so
in its own heading. That floor is complete, and this file is where a Tier-2 type's per-type judgment lives
instead.

It exists because the build runbook has a hole. [`bundle-pipeline.md`](bundle-pipeline.md) and the
`build-bundle` command both name "the type's spec in `buildout-specs.md`" as required reading before a
build starts, and for a Tier-2 type there is no such entry and never was. The first Tier-2 build would
otherwise have been exactly what `buildout-specs.md`'s preamble says a spec sheet prevents: "an open-ended
design task" rather than "a spec-driven execution".

> **A spec here is not a decision to build.** Build order is the maintainer's own preference and need
> ([ADR 0041](decisions/0041-maintainer-preference-sets-the-build-order.md)), and nothing on this page
> schedules anything. What a spec does is make the judgment reviewable *before* 700K to 1M tokens are spent
> executing it.

## Progress

| Type | Catalog id | Family | Spec | Built |
|---|---|---|---|---|
| `spike-report` | `spike-research-spike-report` | `decision-docs` | **Written 2026-09-11** | No |

---

## Per-type specs

### decision-docs (fourth member; the family's first Tier-2 candidate)

**spike-report** - `decision-docs`, **phase develop**, sizes **`[lean]`** (single-size), methodology
**`agile`**, catalog id `spike-research-spike-report`, aliases: `spike`, `technical investigation`.
Catalog owner: Engineer. Catalog purpose: "Time-boxed investigation to reduce uncertainty."

#### Admission, which is settled at the family level and open at the type level

**Settled: a fourth member needs no contract change.**
[ADR 0022](decisions/0022-adopt-decision-docs-family-contract.md) says so in its Consequences, in these
words: "a fourth (a spike report, a solution brief) would join under the same contract with no contract
change unless it declares a different phase or size shape." It declares neither. The
[contract](contracts/decision-docs.md) gates `phase: develop`, and `adr`, `rfc` and `sdd` all declare
exactly that; the catalog's `stage: decision` is the **catalog's** axis and not the bundle's, so it is not
in tension with anything.

> **Read the contract and the ADR together or not at all.** The contract's section 1 says "the family's
> three roles are distinct", which read alone suggests a fourth role is a problem. The record that adopted
> it says the opposite and settled the question on 2026-07-21. A previous session read only the contract,
> concluded a spike report might not be admissible, and overrode a correctly-ranked candidate on that
> basis. The contract carries the rule; the ADR carries what the rule deliberately leaves open.

**Open, and only research can close it: [ADR 0030](decisions/0030-templating-scope-markdown-documents.md)'s
admission test.** A candidate type is templatable only when **a named source publishes it as a written
document**. A catalog entry is necessary and not sufficient - `prototype-brief` had one and failed
([ADR 0035](decisions/0035-prototype-brief-fails-the-admission-test.md)), closing `discovery-docs` at two
members. **So this bundle ships only if its own research pass finds that source, and the honest outcome of
this spec is allowed to be that it does not ship.** The candidate's favourable prior is XP's own
literature, where a spike is a named, documented practice rather than a folk term, but a prior is not a
retrieval.

#### The fourth role, which is what it adds

The contract frames the family as three distinct roles: an RFC **proposes** a technical decision, an ADR
**records** one, an SDD **describes** the design that implements it. A spike report **investigates** the
question that precedes all three, and hands over evidence plus a proceed-or-not recommendation.

That boundary is not this library's invention. The paired pm-skills skill draws it in its own description:
*"For the architecture decision the spike informs, use `develop-adr` instead; for research-based
exploration, use `discover-interview-synthesis`."* The companion's cross-reference obligation (contract
section 4) therefore has a fourth edge to place correctly, and the easiest error to make is letting the
spike report drift into being an ADR with a longer preamble. **A spike report that recommends without
recording what was tried is a bad ADR; an ADR that shows its working is not a spike report.**

#### Section design

Single-size, so there is no nesting obligation and no `full` variant to diverge from. Six sections,
derived from what the practice actually produces:

| Section | What it carries |
|---|---|
| **The Question** | The uncertainty being reduced, written so it can be answered yes or no. A spike with no answerable question is a research project |
| **Time Box** | What was allotted and what was actually spent. This is the section that distinguishes a spike from open exploration, and the one most likely to be quietly dropped |
| **What Was Tried** | Approach, and what was deliberately not attempted. The scope boundary is evidence |
| **What Was Found** | Evidence-backed findings. Facts observed, separated from what they imply |
| **Recommendation** | Proceed, do not proceed, or a named next spike. Explicit, not inferred from tone |
| **What This Does Not Settle** | The open questions the spike did not close, so the next reader does not mistake a bounded answer for a general one |

The last section is a deliberate departure from the paired skill's four-part shape (question, approach,
findings, recommendation) and should be defended or dropped on research evidence like any other. The case
for it: this library's whole credibility posture is not claiming more than was earned, and a time-boxed
investigation is the document type where over-claiming is most natural, because the box closes whether or
not the question was answered.

#### Metadata

| Field | Value | Why |
|---|---|---|
| `family` | `decision-docs` | ADR 0022 |
| `phase` | `develop` | Contract-gated; matches all three existing members |
| `sizes_available` | `[lean]` | Catalog `size_variant: S`. The contract admits `[lean]` for a single-size type, and exempts it from nesting, not from anything else |
| `status` | `beta` | Contract: `beta` until one real usage cycle is recorded. Nothing in this library has one |
| `methodology` | `agile` | **The first decision-docs member to declare a non-generic methodology.** The catalog says Agile/XP, and a spike is genuinely an XP practice rather than a methodology-agnostic instrument. The contract anticipated exactly this: methodology is "descriptive, not gated ... a future member is free to declare otherwise rather than have the truth bent to a rule" |
| `pairs_with` | `[develop-spike-summary]` | Verified present at `skills/develop-spike-summary/SKILL.md` in product-on-purpose/pm-skills on 2026-09-11, v2.2.0, `phase: develop`. Added to `tools/known-skills.txt` in the same change as this spec |
| `related_templates` | `[adr, rfc, sdd]` | Its three siblings |

#### Two things landing this bundle would close elsewhere

1. **`templates/adr/adr_meta.yaml` carries `related_templates: [rfc, sdd, future:spike-report]`.** The
   `future:` prefix is the gate's sanctioned way to reference an unbuilt type, and check I fails a
   `future:` reference whose target the library has since built. **So the bundle directory must be named
   `spike-report`, not the catalog id.** That matches the house rule that bundle ids are bare
   document-type handles ([ADR 0005](decisions/0005-bundle-ids-doctype-spine.md)) while catalog ids are
   long-form: `architecture-decision-record` in the catalog is `templates/adr/` on disk.
2. **The example-independence rule applies.** Contract section 5: decision-docs examples are deliberately
   independent, each a different real decision, because the family teaches the *distinction* between roles
   rather than one thread. So this bundle's example must not extend the Acme Analytics chain, and
   `tools/check-example-independence.py` enforces it.

#### Not applicable, stated so nobody applies it

**The Tier-2 active-practice test does not gate this type.** The pull-queue rule applies that bar "whenever
a Tier-2 **methodology pack** is built" - a Scrum or SAFe or XP *collection*. A single methodology-leaning
document type is not a pack, and `tier_inferred: true` on the catalog row means even the tier itself is a
derived guess rather than a maintainer's call.

---

## What a spec on this page is worth

The same as one in `buildout-specs.md`, which is to say provisional. Every per-type spec in that file was
written before its research pass, and **four of `user-persona`'s section calls were overturned by its own
research** and recorded as departures in its research log. That is the system working: the spec front-loads
judgment so the research has something specific to disagree with. Expect this one to be wrong somewhere,
and expect the research log to say where.
