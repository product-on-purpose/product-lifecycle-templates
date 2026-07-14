---
title: "Strategy Brief: Turning the Master Catalog into a Template Library"
status: draft
doc_version: 0.1.0
owner: "product-on-purpose"
last_reviewed: 2026-06-29
license: Apache-2.0
source_inputs:
  - deep-research_master-catalog.md
  - template-library-design-spec.md
  - template-system-layered-design.md
  - pm-sdlc-document-research-prompt.md
related:
  - implementation-plan_catalog-to-template-library.md
---

# Strategy Brief: Turning the Master Catalog into a Template Library

> **What this is.** A decision-ready analysis that takes the 205-type [Master Catalog](../catalog.md) as raw material and answers: which of these become templates, in what order, in what shape, and how does the resulting library relate to `pm-skills`. It reconciles the three design documents where they disagree and gives an opinionated 80/20 path to a shippable v0.1.
>
> **Reading order.** This brief frames the strategy and resolves the open decisions. The companion [Implementation Plan](../plan.md) turns the resolved decisions into an executable, phased build.

---

## 1. What I Understand (Input Mirror)

You have run a deliberately exhaustive deep-research sweep and produced a **Master Catalog of 205 deduplicated PM/SDLC document types**, organized into 19 categories, with aliases folded in, a self-declared **"must-have 28" tier** that covers roughly 80% of organizations, a long tail of methodology-specific artifacts (Amazon PR/FAQ, Shape Up pitch, SAFe PI objectives), and a regulated tier (FDA design controls, ISO 14971, SOC 2, GDPR) flagged as rare-but-mandatory in its domains. Each entry carries a structured schema (`canonical_name`, aliases, phase, owner, sections, methodology, formality, rarity, relationships, size variant) deliberately aligned to template frontmatter.

Around that catalog sit three design documents that already commit to a direction:

- **`template-library-design-spec.md`** specifies `pm-templates`: a local-first, file-based library where every document type ships as a **bundle** (S/M/L variant files + worked example + usage guide + machine-readable manifest), governed by a two-tier metadata model, family contracts, and a CI-enforced Definition of Done. It positions the library as a **sibling to `pm-skills`**: skills teach an agent *how to produce* an artifact; templates provide *the artifact itself*.
- **`template-system-layered-design.md`** zooms out to a **three-layer model**: Layer 0 the static library (noun), Layer 1 an optional generator that applies an org profile to emit tailored-but-blank templates (verb that shapes), Layer 2 `pm-skills` that fills templates with context (verb that fills). It recommends **packaging Shape C reached by way of A**: ship the static library first, design an attach point for a generator, build the generator only if a decision gate clears.
- **`pm-sdlc-document-research-prompt.md`** is the provenance of the catalog and confirms the design intent: the per-item fields map onto library frontmatter, and a natural triage filter (`formality: standard` + `rarity: common/occasional` first) is already anticipated.

**The implicit ask.** You are not asking "is the catalog good." You are asking: *given this catalog and these designs, what is the strategy and the build plan?* The three threads I see are (1) **scope and sequencing** - which of 205 become templates, in what order; (2) **shape and architecture** - the bundle, variant, and metadata decisions, including where the two design docs contradict each other; and (3) **system boundary** - whether this is one repo or three layers, and how hard to commit to the generator now.

---

## 2. Problem Space

**Why this matters now.** You have a near-empty repo (`product-lifecycle-templates`: a README and these discovery docs) and a mature sibling (`pm-skills`: 68 skills, heavy CI, family contracts, marketplace + plugin manifests). The catalog is fresh and the design thinking is done. The window is open to lay down conventions *once*, correctly, before any content accretes and ossifies bad choices. The cost of getting the spine wrong is not a bad file; it is a combinatorial refactor later (the spec's own warning: size x stage x audience folders would be 45 files per type).

**What "solved" looks like.** A shippable v0.1 that is a *complete, useful product on its own* - not a folder of stubs. Concretely: one document type, fully worked end-to-end (variants + example + guide + manifest), passing a real CI quality gate, installable on the same rails as `pm-skills`, and carrying the `pairs_with` bridge to its sibling skill. From that single bundle, every pattern in the library is provable and repeatable. Success at the strategy level is a build order that lets value compound (each family makes the next cheaper) without ever shipping shelfware.

**Who is affected.** Three audiences, already named in the design: individual PMs/engineers who want the right-sized blank shape fast; teams who want a shared institutional standard; and AI agents that need clean, structured, machine-readable artifacts to fill. A fourth, quieter stakeholder is **future-you as maintainer** - the person who has to keep 205 potential bundles from rotting. Every governance decision in this brief is really a bet about that person's time.

**The adjacent problem the catalog exposes.** The catalog covers 205 types, but `pm-skills` already *produces* ~30 phase document types and already bundles a `TEMPLATE.md` per skill. So the library does not start from zero demand - it starts from **overlap**. The strategic question hiding inside "which types first" is really: *do we build where `pm-skills` already pairs (deepening the ecosystem), or where it has gaps (broadening coverage)?* This is the highest-leverage decision in the brief and Section 3 treats it head-on.

**Desired outcomes, ranked.** (1) A correct, durable spine and metadata contract. (2) One fully-worked bundle that proves the contract. (3) A sequencing rule that ties build order to real pull, not to catalog completeness. (4) A clean, reversible answer to the generator question that does not block shipping. Completeness of the library is explicitly *not* a near-term outcome; 205 bundles is a multi-quarter horizon and chasing it early is the main failure mode.

---

## 3. Analysis

### Core lenses

**Strengths.** The inputs are unusually strong. The catalog is rigorous and pre-structured for frontmatter, which removes the normal "what fields do we need" guesswork. The design spec is already best-in-class thinking (two-tier metadata, nesting rule, family contracts, CI DoD). The layered model correctly refuses to over-build the generator. And there is a live, mature reference implementation next door (`pm-skills`) whose conventions can be copied rather than invented - CI scripts, manifest shape, family-contract pattern, HISTORY/CHANGELOG discipline, no-emdash sweep. Most template-library projects start with none of this; you start with all of it.

**Weaknesses.** The two design docs **disagree on the variant model**, and the disagreement is not cosmetic. The spec mandates rigid **`S/M/L` with a strict nesting rule** and abstract filenames (`template.s.md`). The later layered doc softens this to *"default lean/full; S/M/L only where a type earns three weights; descriptive filenames preferred over abstract size letters."* These produce different repos. Shipping before resolving this bakes in churn. A second weakness: the spec capitalizes `phase: Deliver` and names the axis "Triple Diamond: Discover, Define, Develop, Deliver, Measure, Iterate," but the *actual* `pm-skills` frontmatter uses lowercase `phase: deliver` with skill IDs like `deliver-prd`. The compatibility seam is only real if the casing and ID conventions match exactly. Third: the repo is already named `product-lifecycle-templates` on disk, while every design doc says `pm-templates` - an unresolved identity that will leak into READMEs, manifests, and install commands if not settled first.

**Risks.** The dominant risk is **breadth-chasing**: treating "205 types" as a backlog and trying to cover it, which produces hundreds of thin, unexampled stubs - the exact shelfware the catalog's own recommendations warn against ("only build a methodology pack when a team is actively practicing it"). The second risk is **convention drift from `pm-skills`**: if the library invents its own manifest shape, phase casing, or CI style, the "ecosystem coherence" value pillar evaporates and you maintain two divergent systems. Third is **premature generator**: building Layer 1 speculatively rebuilds `pm-skills` badly (the layered doc's own bright line) and burns the v0.1 window. Fourth, quieter risk: **regulated templates shipped without traceability discipline** - FDA/ISO/SOC2/GDPR artifacts are auditable, and a blank-but-wrong regulated template is worse than none, especially with the QMSR terminology change effective 2026-02-02 already noted in the catalog.

**Open questions.** Does the `skills` CLI install a repo with no `SKILL.md` (determines whether the `use-template` companion skill is *required* for distribution)? Does the agentskills.io spec define a non-skill "resource/template" type the manifest should conform to rather than inventing one? Is customization a one-time fork or a recurring re-apply (the generator decision gate)? These are flagged in the source docs as unresolved and remain so.

**Concerns.** My main concern is **over-engineering the v0.1**. The design spec is so complete that it is tempting to build the whole governance apparatus (seven CI scripts, family-contract validator, count-consistency guards) before a single bundle exists. That inverts the 80/20. The governance is the *destination*; the first bundle plus the two or three CI checks that protect *its* contract is the *start*.

### Situational lenses

**Build-vs-reuse lens.** Almost nothing here should be built from scratch. The CI scripts, manifest generator, family-contract validator, and release hygiene already exist in `pm-skills` in `.sh`/`.ps1`/`.mjs` form. The right move is **port and adapt**, not author. This both saves effort and *enforces* the convention-coherence that is the whole point of being a sibling repo. The brief's recommendations lean on this heavily.

**Sequencing/dependency lens.** The catalog's three tiers are a ready-made build order, but the *first* increment should be even smaller than Tier 1. The dependency chain is: spine + metadata contract -> one bundle -> one family -> Tier 1 -> Tier 2 by pull -> Tier 3 as a separate module. Each link de-risks the next. The family chosen first should be the one with live `pairs_with` targets, which points unambiguously at **`delivery-docs`** (PRD, user stories, acceptance criteria, release notes) because `pm-skills` already ships `deliver-prd`, `deliver-user-stories`, `deliver-acceptance-criteria`, `deliver-release-notes`.

**Reversibility lens.** The decisions split cleanly into "cheap to change later" and "expensive to change later." Cheap: which Tier 2 packs, the generator, the companion skill's home. Expensive: the directory spine (document type), the metadata field names, the phase casing, the placeholder convention, the name. The strategy is to **commit hard and early on the expensive-to-reverse decisions** and **stay deliberately uncommitted on the cheap ones** (the layered doc's "reserve a `profiles/` attach point but build nothing" is exactly this instinct).

**Ecosystem-coherence lens.** The library's differentiated value is not "templates exist" (awesome-lists already point at scattered templates). It is *governed, self-describing, sized, traceable templates that speak `pm-skills`' language*. Every decision that strengthens the seam with `pm-skills` (shared phase vocabulary, `pairs_with` by ID, mirrored CI, mirrored bundle-vs-references layout) compounds that differentiation. Every decision that weakens it erodes the only moat.

---

## 4. Approaches

The genuinely distinct strategic paths differ on **how much system to commit to up front** and **what the first unit of value is**. They are not intensity variants; they imply different repos.

### Approach A: Static library, one-bundle-first, mirror `pm-skills` (the "Shape A, deepen-then-broaden" path)

**Summary.** Build Layer 0 only. Ship one fully-worked bundle (`deliver-prd`), then complete the `delivery-docs` family, then Tier 1 by pull. Port CI from `pm-skills`. Reserve a `profiles/` attach point but build no generator. Start where `pm-skills` already pairs.

**Detailed breakdown.** v0.1 is a single bundle exercising every pattern: variants, example, guide, `template.meta.yaml`, instance frontmatter with provenance fields, the two or three CI checks that protect *that* bundle's contract, plus README/AGENTS.md/marketplace stub. v0.2 completes the first family and stands up the family-contract validator. v0.3 adds the `use-template` companion skill and the catalog generator. Tiers 2 and 3 are demand-gated.

**Pros.** Lowest risk; every increment is independently useful. Maximizes reuse of `pm-skills` machinery, which simultaneously enforces coherence. Resolves the overlap question crisply (deepen the existing pairs first). Defers every expensive-to-build, cheap-to-reverse decision. Directly matches the layered doc's recommendation and the spec's own roadmap.

**Cons.** Coverage grows slowly; if someone expects "a template for all 205 types" soon, this disappoints. The `pairs_with`-first choice means early bundles partly duplicate templates `pm-skills` skills already bundle, so the *marginal* value of the first few bundles is "richer/sized/traceable versions of templates that already exist" rather than net-new coverage - a real value but a subtler sell.

**Key risks.** Discipline risk: the team gets bored of one-bundle-deep and jumps to breadth. Mitigated by making the family-contract gate a hard CI blocker.

**Effort/complexity.** Low-to-moderate. Most effort is content quality (real examples, real guides), not engineering.

**Honest commentary.** This is what the source documents already argue for, made concrete. Its strength is that it is nearly unfalsifiable as the *right start* - it is the lowest-regret path regardless of how the open questions resolve.

### Approach B: Coverage-first breadth (the "fill the catalog" path)

**Summary.** Treat the 28 must-haves (or more) as a backlog and produce thin bundles across all of them quickly, deepening examples and guides later.

**Detailed breakdown.** Generate skeletal bundles for Tier 1 in parallel, each with variant files and minimal frontmatter, deferring worked examples and guides. Optimize for "a template exists for X" across the broadest surface.

**Pros.** Visible breadth fast; a wide catalog "looks" complete and may attract more initial interest. Better if the primary user need is "any starting point beats a blank page" across many types at once.

**Cons.** Directly violates the catalog's own Recommendation 1 and 2 and the design spec's Definition of Done (a bundle is not "done" without a genuine example and a guide with anti-patterns). Produces shelfware risk at scale. The CI quality bar, if honestly enforced, would *block* most of these from merging - so either you ship low-quality or you weaken the gate, and weakening the gate kills the differentiation.

**Key risks.** Quality collapse and convention drift, because breadth pressure pushes against the governance that makes the library special.

**Effort/complexity.** Deceptively high: thin breadth still needs frontmatter, naming, and manifest entries for every type, and the example/guide debt compounds.

**Honest commentary.** This is the seductive wrong answer. It feels productive and demos well, but it inverts the project's stated value (governed quality over coverage) and is the exact failure the inputs warn against. Include it only to name it and reject it.

### Approach C: Library + generator together (the "Shape B, build the system" path)

**Summary.** Commit to the three-layer system now: build the static library *and* the org-profile generator as one installable product, on the bet that org customization is the core value.

**Detailed breakdown.** Define the org-profile format, build the `standard + profile = tailored` transform with validate/iterate analogs to `pm-skills`' builder lifecycle, and ship library + generator as a single plug-in (packaging Shape B).

**Pros.** If - and only if - customization is *recurring* (orgs re-apply house standards as upstream improves), the generator is "the actual point" per the layered doc, and building it early avoids a later retrofit. Strongest story for enterprise adoption where house terminology and mandatory sections matter.

**Cons.** Bets the v0.1 window on an *unanswered* decision-gate question (one-time vs recurring customization). Risks blurring the bright line (a generator that drifts toward emitting filled content rebuilds `pm-skills` badly). Higher complexity before any single bundle has proven the underlying contract - you would be building the transform over a substrate that does not exist yet.

**Key risks.** Premature commitment; the generator's value is conditional on a fact not yet in evidence.

**Effort/complexity.** High. Two products' worth of surface, plus a profile schema and a re-apply mechanism.

**Honest commentary.** Not wrong forever - possibly right *later*. Wrong *now*, because it spends the scarce early window on a conditional bet. The layered doc itself says "do not build the generator speculatively," and this approach is the speculative build.

---

## 5. The 80/20 Recommendation

**Take Approach A.** It is the lowest-regret path, it is what the inputs already argue for, and it is the only one that ships a *complete* thing soon without betting on unanswered questions. The 20% that delivers 80% of the value is **one document type, fully worked, with the contract and CI that protect it - and nothing else built yet.**

But Approach A only works if you first **resolve the four expensive-to-reverse decisions** the source docs left open or contradictory. Do this *before* writing bundle content, because they are cheap to decide now and costly to change after content exists:

1. **Name. [Resolved 2026-06-29: `product-lifecycle-templates` everywhere.]** Use `product-lifecycle-templates` for the git repo, the plugin/marketplace `name` field, and the install command; drop the `pm-` family handle. The broader name ages better if the library outgrows pure PM into general software docs (design spec §15 anticipates exactly this). Coherence with `pm-skills` is carried by shared conventions and the `pairs_with` seam, not by a shared name prefix.
2. **Variant model. [Resolved 2026-06-29: lean/full, descriptive filenames, nesting kept.]** Adopt the **layered doc's softer rule** over the design spec's rigid `S/M/L`: ship the number of variants a type *earns* (most earn two: a lean and a full), use **descriptive filenames** (`template.lean.md` / `template.full.md`, and `template.s/m/l.md` only where three weights genuinely differ), and keep the **nesting discipline** (a smaller variant is a strict subset of the larger) because that is what enables upgrade-in-place. Rationale: the catalog's own `size_variant` column shows most types vary in two weights, not three; descriptive filenames are self-documenting while deterministic agent selection runs off the `sizes_available` metadata field, not the filename; and this is the later, more considered of the two conflicting design positions.
3. **Phase vocabulary.** Match `pm-skills` exactly: **lowercase `phase` values** (`discover`, `define`, `develop`, `deliver`, `measure`, `iterate`, plus `foundation`/`tool`) and **`<phase>-<doctype>` bundle IDs** (`deliver-prd`), so `pairs_with` resolves against real skill IDs.
4. **First family = `delivery-docs`**, first bundle = **`deliver-prd`**, because its `pairs_with` targets already exist in `pm-skills`.

**Concrete next steps (in order):**

1. **Decide the four above** and record each as a short ADR/decision note in the repo (you already have the `develop-adr` convention next door). This is a half-day and it unblocks everything.
2. **Build the `deliver-prd` bundle end-to-end** - variants, real worked example (not lorem), guide with named anti-patterns, `template.meta.yaml`, provenance frontmatter - and **port the three CI checks that protect it** (frontmatter lint, variant-nesting check, no-emdash sweep) from `pm-skills`. Ship it as v0.1 with README, AGENTS.md, and a marketplace stub.
3. **Only then** complete the `delivery-docs` family (v0.2) and stand up the family-contract validator.

**Explicitly defer:** the generator (Layer 1) until the decision-gate question is answered against real usage; Tier 2 methodology/discipline packs until a team actively pulls one; Tier 3 regulated artifacts into a separate, access-controlled, traceability-first module; multi-language and audience-rendering tooling indefinitely.

**Confidence: high** on the path (the inputs converge on it and the reference implementation exists), **medium** on the variant-model recommendation (a genuine judgment call between two reasonable positions - see Section 7), **high** on deferring the generator (the inputs and the unanswered gate both point that way).

---

## 6. Evidence & Source Map

| Claim | Source |
|---|---|
| 205 deduplicated types, 19 categories, "must-have 28," tiered by formality/rarity | `deep-research_master-catalog.md` (TL;DR, Key Findings, Recommendations) |
| Per-item schema aligned to template frontmatter; triage filter `standard` + `common/occasional` first | `pm-sdlc-document-research-prompt.md` (Notes for the requester) |
| Bundle anatomy, two-tier metadata, family contract, CI DoD, S/M/L nesting rule, name candidates | `template-library-design-spec.md` (§6-§16) |
| Three-layer model, bright line, decision gate, Shape C via A, "lean/full, descriptive filenames," reserve `profiles/` | `template-system-layered-design.md` (§2-§11) |
| `pm-skills` is mature: 68 skills, phase-prefixed IDs, lowercase `phase: deliver`, bundle = SKILL.md + HISTORY.md + references/{TEMPLATE,EXAMPLE} + evals/, marketplace + plugin manifests, ~100 CI scripts, family contracts | Direct inspection of `E:/Projects/product-on-purpose/pm-skills` (skills/, scripts/, .claude-plugin/, skills/deliver-prd/) |
| `delivery-docs` family maps to existing skills `deliver-prd`, `deliver-user-stories`, `deliver-acceptance-criteria`, `deliver-release-notes` | `pm-skills/skills/` listing |
| Repo currently near-empty (README + discovery docs) | Direct inspection of `product-lifecycle-templates` |
| QMSR effective 2026-02-02; verify FDA text on ecfr.gov before audit-grade templates | `deep-research_master-catalog.md` (Key Findings, Recommendation 3, Caveats) |

**Evidence gaps (honest):** The brief's *recommendations* are reasoning over the inputs plus the live `pm-skills` repo, not external market validation. I have not tested the `skills` CLI behavior with a no-`SKILL.md` repo, nor read the current agentskills.io spec for a "resource/template" type - both are open questions carried from the source docs, not resolved here. The variant-model recommendation is a judgment call, not a measured finding.

---

## 7. Uncertainties & Open Items

**Things I am unsure about (with confidence labels):**

- **Variant model (medium confidence).** I recommend the softer "lean/full, descriptive filenames" rule, but the rigid `S/M/L` spec has a real virtue: a fixed vocabulary is easier for an agent to select against deterministically. If agent-driven selection turns out to be the dominant use, the rigid model may be worth its busywork. *Resolvable by:* deciding which consumer (human upgrade-in-place vs agent selection) is primary for v0.1.
- **CLI distribution without `SKILL.md` (low confidence, high impact).** Whether the `skills` CLI installs a template-only repo determines if the `use-template` companion skill is *required* or merely *nice*. *Resolvable by:* a 30-minute test against the CLI before committing the distribution story.
- **agentskills.io "resource" type (low confidence).** If the spec defines a non-skill template/resource type, the manifest should conform rather than invent. *Resolvable by:* reading the current spec.

**What requires human (your) judgment:**

- The **name** decision (identity/branding, not derivable from analysis).
- The **generator decision gate**: is org customization one-time (fork-and-edit, no generator) or recurring (re-applyable profile, generator is the point)? This is a fact about *your users*, not about the code, and it gates whether Layer 1 ever exists.
- **Regulated tier appetite**: whether you intend the library to serve regulated domains at all, which determines if Tier 3's traceability-first module is on the roadmap or out of scope.

**What would benefit from additional research:**

- A quick scan of `pm-skills`' existing `overrides/` directory (the layered doc §12 flags it as "not yet inspected") - it may already be the generator attach point, or may be unrelated.
- Confirming the exact `marketplace.json` schema in `pm-skills` so the template `marketplace.json` aligns field-for-field rather than structurally.

**Suggested follow-up generation:** The natural next artifact is the **detailed implementation plan** (companion document, [`implementation-plan_catalog-to-template-library.md`](../plan.md)), which turns the four resolved decisions and Approach A into a phased, task-level build with CI gates and acceptance criteria. After that, the logical artifacts are (a) four short decision notes capturing the Section 5 resolutions, and (b) the `delivery-docs` family contract once the first bundle is proven.
