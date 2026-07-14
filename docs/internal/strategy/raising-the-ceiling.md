---
title: "Raising the Ceiling: Quality, Vision, and Value Improvements for product-lifecycle-templates"
doc_type: strategy-brief
status: draft
doc_version: 0.1.0
owner: "product-on-purpose"
created: 2026-07-02
last_reviewed: 2026-07-02
additive_to:
  - strategy-brief_catalog-to-template-library.md
  - implementation-plan_catalog-to-template-library.md
  - template-library-design-spec.md
  - ../../templates/methodology.md
note: "This brief deliberately does NOT relitigate locked decisions (name, variant model, bundle shape, taxonomy spine, pull-based coverage). It proposes work that sits in the whitespace those docs leave open."
---

# Raising the Ceiling

> **Thesis.** The repo has already won the *architecture* argument: bundle shape, metadata, variant nesting, taxonomy spine, and a real methodology are settled and good. The next ceiling is not more structure - it is **proof, usage, and reach.** Today "best-in-class" is *asserted* by a Definition of Done that checks structure; it is not yet *demonstrated* by evidence that these templates make real documents faster or better, not yet *exercised* by anyone filling one in anger, and not yet *reachable* by the agents the vision names as first-class users. This brief proposes how to close those three gaps, plus the business question the planning docs are entirely silent on.

Each idea carries a short handle so you can reference it later (for example "EV-1 (efficacy evals)"). Ideas are grouped by theme; a prioritization table and a recommended sequence follow at the end.

---

## 1. What is already strong (so this brief can build, not repeat)

Credit where due, because these are the foundation the rest stands on:

- **Governed quality as the stated moat**, not coverage. The methodology and design spec both name this explicitly, and the 4-bundle `delivery-docs` family now proves it is achievable (enriched templates, linked companions, per-bundle DoD).
- **The dual-reader split** (companion for the why, guide for the how) is a genuine differentiator over every "awesome-list" of templates.
- **Agent-legible metadata** (`meta.yaml`, `pairs_with`, provenance fields) already points at the agent-native future.
- **A real research protocol** with tiered, reliability-tagged citations. Most template collections have none.

The gaps below are not corrections. They are the difference between a beautifully engineered library and a library that is *proven*, *used*, and *sold*.

---

## 2. The core strategic gap: best-in-class is asserted, not proven

Every quality gate in the plan (AC-1..AC-14, the CI scripts, the per-bundle DoD) checks **structure**: nesting holds, citations resolve, no dashes, placeholders consistent. Not one of them checks whether a template actually helps someone produce a better document. The sibling `pm-skills` repo has an `evals/` directory; the template repo has no behavioral analog. This is the single highest-leverage gap, because the entire positioning rests on a quality claim the repo cannot currently substantiate. Theme A exists to fix exactly this.

---

## 3. Improvement ideas by theme

### A. Prove the quality (evaluation and evidence)

**EV-1 (efficacy evals).** Build a behavioral harness, mirroring `pm-skills`' `evals/`. For each bundle: give a model the blank template plus a realistic scenario, have it produce a filled doc, and score the result against the guide's rubric (ideally with an LLM-judge plus a couple of human-graded anchors). Run it two ways - with the template and with only a bare prompt - so you can show the *lift* the template provides. Re-run on every template change as a regression test. **Impact: very high** (this is what converts "best-in-class" from a claim to a measured fact, and it protects against edits that quietly degrade a template). **Effort: high.** **Relation to plan:** net-new; the natural P4/P6 companion (evals ship with the reference bundle, not after all bundles).

**EV-2 (quality scorecard).** Turn each guide's rubric into a scored self-grade and publish a per-bundle "template quality index" (research depth, example realism, rubric coverage, citation reliability mix, freshness). A visible score per bundle creates internal pressure to keep every bundle at the bar and gives an external signal of rigor. **Impact: high. Effort: low-medium.** **Relation:** extends the DoD from pass/fail to graded.

**EV-3 (red-team and real-user protocol).** Define a lightweight, repeatable critique loop: a structured adversarial review pass ("attack this template - where would a real author go wrong, what is missing, what is padding") plus a real-usage feedback capture (a 5-question form the first real author fills after using a bundle). The catalog already sets an adoption *threshold* ("survives one usage cycle") but names no method to gather the signal. This is the method. **Impact: high. Effort: low.** **Relation:** operationalizes the pull-based adoption gate.

**EV-4 (audit-grade citation pass).** The last session honestly flagged that several sources were corroborated by search, not primary fetch (Cagan/SVPG 403s, Lenny paywall, Scrum.org empty render). Add a per-claim verification state (verified-primary / corroborated / author-judgment) and, for the flagged sources, capture exact quotes from accessible mirrors. **Impact: medium** (raises trust, matters most for Tier 3 regulated). **Effort: medium.** **Relation:** tightens methodology §A4.

### B. Close the loop (make templates actually get used)

**LP-1 (use-template flow).** The single most important unshipped thing: nothing has ever been filled from a template. Build a `use-template` flow (a skill or CLI) that interviews the author section by section (the enriched comments are already the interview script), emits a filled draft with provenance frontmatter, and strips the guidance. This resolves open decision D2 and is where all the value is actually realized. **Impact: very high. Effort: medium-high.** **Relation:** directly answers D2; slot right after the reference bundle (P4).

**LP-2 (grade-my-existing-doc).** The strongest *adoption wedge*: let a user paste a doc they already have and get it graded against the template's rubric, with specific gaps flagged ("no non-goals; success metric has no guardrail; problem is stated as a missing feature"). Most teams will not start from a blank template, but they will happily have their existing PRD critiqued - and that critique sells the template. This is a reverse of LP-1 and reuses the same rubric. **Impact: very high. Effort: medium.** **Relation:** net-new; arguably the best top-of-funnel the library has.

**LP-3 (usage telemetry, privacy-aware).** If templates ship via a plugin/MCP, capture which templates are pulled and which sections authors most often leave blank or rewrite - the strongest possible signal for what to improve and what to build next. Opt-in and anonymized. **Impact: medium-high. Effort: medium.** **Relation:** feeds the pull-queue (P7) with data instead of anecdote.

### C. Lean into the agent-native moat (the real differentiator)

**AG-1 (machine-readable section schema).** `meta.yaml` describes the *bundle*; nothing describes the *shape of a filled instance* in a way an agent can rely on. Add a per-template section schema (required vs optional sections, field types, table columns, which sections are load-bearing) as structured data. Then an agent can fill a template deterministically and self-check completeness. **Impact: high. Effort: medium.** **Relation:** the missing piece under the "agents reach for it first" vision; also what makes LP-1 and EV-1 robust.

**AG-2 (templates as an MCP server).** The docs mention `pm-templates-mcp` as a thin "future." Make it real and designed: an MCP server that lets any agent list templates, select by intent (embeddings over purpose/when-used/aliases), fetch the blank plus its companion, and post back a filled draft. This is the difference between "a folder humans clone" and "the template layer every agent in the ecosystem calls." **Impact: very high (this is the moat). Effort: high.** **Relation:** promotes a deferred idea to a first-class deliverable; pairs with the distribution phase (P5).

**AG-3 (agent authoring kit).** The library is *already* being built by agents under `methodology.md`. Formalize that: a small kit (the methodology + a bundle-scaffolding prompt + the verification recipe used this session) so new bundles can be drafted by an agent and then human-reviewed, at consistent quality. Dogfooding the agent-native claim on the production side, not just the consumption side. **Impact: medium-high. Effort: low** (most of it exists as tacit process). **Relation:** turns this session's ad-hoc parallel-agent build into a repeatable asset.

### D. Content depth and range

**CT-1 (domain-diverse and lean examples).** Every example currently chains on one fictional "Saved Views" B2B-SaaS feature, and only the full variant is worked. A best-in-class library proves its templates *travel*: add a second worked example per bundle from a different context (a regulated/health feature, a consumer-mobile change, a platform/API change) and a lean-variant example. **Impact: high** (examples are what authors copy; range is what earns trust). **Effort: medium.** **Relation:** extends methodology B4.

**CT-2 (annotated anti-examples).** Ship a deliberately *bad* filled example per bundle with inline annotations of what is wrong and why. A good example shows the target; a bad-example-with-red-ink teaches faster than any prose. **Impact: medium-high. Effort: low-medium.** **Relation:** net-new bundle asset (an 8th/9th file, or a section of the example).

**CT-3 (the artifact atlas).** Render the 205-type catalog and its relationships as a navigable visual map of the product lifecycle - what precedes/follows/feeds what. This is simultaneously a navigation aid, a scoping tool (it shows the map so you can consciously choose the must-have 28 and prune the rest), and a genuinely shareable marketing asset. **Impact: high (doubles as content marketing). Effort: medium.** **Relation:** materializes the relationships already in the catalog and the architecture mermaid.

**CT-4 (house style and readability gate).** With bundles authored partly by parallel agents, voice drift is a real risk. Add a short library style guide (tone, person, tense, the strong/weak convention) and a readability check on companions (plain-language, sentence length). **Impact: medium. Effort: low.** **Relation:** protects consistency as authorship scales.

### E. Freshness as a system, not a footnote

**FR-1 (automated staleness gate).** Recency is a stated principle but has no automation. Add a scheduled job: link-check every citation URL, flag per-source "re-check by" dates, and watch known-moving targets (Keep a Changelog 2.0.0 is planned for 2026; standards transitions like IEEE 829 to 29119). CI catches dead links; a cron surfaces claims due for re-verification. **Impact: high (trust decays silently otherwise). Effort: medium.** **Relation:** promotes methodology §1.4 and catalog Rec 6 from policy to enforcement.

**FR-2 (per-bundle freshness badge).** Surface "last verified" and "sources re-checked" per bundle so a reader can weigh currency at a glance. **Impact: low-medium. Effort: low.** **Relation:** pairs with FR-1 and EV-2.

### F. Sharpen the vision and positioning

**VS-1 (name and defend the moat in one line).** The docs circle it; state it crisply and put it on the README: *the template layer that agents use correctly - governed, machine-selectable, traceable, and dual-readable.* Coverage is not the product; correct-by-construction reuse is. **Impact: high (clarity compounds). Effort: trivial.**

**VS-2 (the pm-skills flywheel).** Draw and document the closed loop the two repos form: a skill decides *how* to produce an artifact, the template *is* the artifact, a filled doc feeds the next skill. The value is not two repos, it is the loop. Make it a diagram. **Impact: medium-high. Effort: low.** **Relation:** deepens the spec's `pairs_with` seam into a narrative.

**VS-3 (coverage discipline as a feature).** 205 types is a trap if treated as a backlog. Make "we deliberately did not build this" a visible, first-class state (the atlas shows the whole map; the must-have 28 is the product; everything else is pull). Pruning and saying-no should be as documented as building. **Impact: medium. Effort: low.** **Relation:** reinforces the pull model (P7) against scope creep.

### G. Value and business model (the total whitespace)

The planning docs say **nothing** about who pays, how this sustains itself, or how it serves the `product-on-purpose` business. That is a strategic blind spot for a company asset, so it deserves explicit thought even if the answer is "stay free."

**VL-1 (open-core options).** A defensible split: the library, methodology, and must-have 28 stay free and open (that is the credibility and the funnel); the paid layer is the things that are painful to do yourself - the Layer 1 generator with org profiles (house-brand tailoring at scale), private regulated packs (Tier 3, traceability-first), template *certification* for teams, and done-for-you bundle authoring. **Impact: high if monetization is a goal. Effort: n/a (a decision, not a build).**

**VL-2 (authority and top-of-funnel).** Even if it never charges, the library is exceptional content marketing for `product-on-purpose`: the companions are genuinely best-in-class explainers, the atlas is shareable, and "the template library agents use" is a memorable authority position. Treat SEO, the atlas, and a handful of flagship companions as lead-gen for consulting/training. **Impact: high. Effort: low-medium.**

**VL-3 (sustainability and maintenance cadence).** Best-in-class content rots without a keeper. Decide the maintenance model now (who re-verifies, how often, funded how), because FR-1 will generate a steady trickle of "this needs re-checking" that needs an owner. **Impact: medium. Effort: low (a decision + a calendar).**

### H. Durability and hygiene (quick wins, do first)

**HY-1 (get the work under version control).** Everything built - four enriched bundles, the methodology, the strategy brief, the implementation plan, this document - lives under gitignored `_local/`. It is working-tree only. One lost tree and it is all gone. Decide whether `_local/` graduates to a tracked path or a tracked mirror. **Impact: high (pure risk reduction). Effort: trivial.** **Relation:** the session log's own top outstanding risk.

**HY-2 (settle the scaffold).** Flat-vs-nested is deferred as "derivable," which is true but currently blocks standing up the skeleton. Recommendation: flat `templates/<type>/` as the physical spine (matches the taxonomy decision that document-type is the only directory spine), with generated phase/lens indexes on top - phase stays metadata, navigation is derived. **Impact: medium (unblocks P2). Effort: low.**

**HY-3 (resolve the research-log question).** Keep the per-bundle `_research-log.md` (do not fold it into the companion): it is the evidence trail FR-1 and EV-4 both need, and it keeps the companion readable. Make it explicit in the methodology rather than leaving it an open call. **Impact: low. Effort: trivial.**

---

## 4. Prioritization

Rough impact-versus-effort read. "When" is expressed relative to the existing P1-P7 plan, not as a replacement for it.

| ID | Idea | Impact | Effort | When |
|---|---|---|---|---|
| HY-1 | Version-control the work | High | Trivial | Now, before anything |
| VS-1 | One-line moat statement | High | Trivial | Now |
| HY-2 | Settle the scaffold | Medium | Low | Now (unblocks P2) |
| EV-3 | Red-team + real-user protocol | High | Low | With reference bundle (P4) |
| EV-2 | Quality scorecard | High | Low-Med | With P4/P6 |
| LP-2 | Grade-my-existing-doc wedge | Very High | Medium | Early; strongest funnel |
| CT-1 | Diverse + lean examples | High | Medium | P4/P6 |
| CT-3 | The artifact atlas | High | Medium | Alongside distribution (P5) |
| FR-1 | Automated staleness gate | High | Medium | With CI (P3) |
| EV-1 | Efficacy evals | Very High | High | With reference bundle (P4) |
| LP-1 | use-template flow | Very High | Med-High | Right after P4; answers D2 |
| AG-1 | Section schema | High | Medium | Before AG-2/LP-1 harden |
| AG-2 | Templates-as-MCP | Very High | High | Distribution (P5+) |
| VL-1 | Open-core decision | High* | n/a | Decide before P5 distribution |

\*High only if monetization is a goal; a decision either way.

**The 80/20:** if only three things happen beyond the current plan, make them **EV-1 (efficacy evals)** so quality is proven not asserted, **LP-1/LP-2 (use it / grade it)** so the templates leave the shelf, and **AG-2 (MCP)** so the agent-native moat is real. Everything else compounds those three.

---

## 5. Recommended sequence (woven into the existing plan)

1. **Immediately, independent of everything:** HY-1 (version control), VS-1 (moat line), HY-2 + HY-3 (scaffold + research-log decisions). Hours, not days; removes the durability risk and unblocks P2.
2. **With P3 (CI):** add FR-1 (link-check + staleness) to the CI scripts already planned, and EV-2 (scorecard) as a graded extension of the DoD.
3. **With P4 (reference bundle):** ship EV-1 (evals) and EV-3 (red-team/user protocol) *alongside* the bundle, not after - so the reference bundle is the first *proven* one. Add CT-1 (a second, non-SaaS example) and CT-2 (one anti-example) to make it the exemplar in range as well as shape.
4. **Right after P4:** LP-1 (use-template) and LP-2 (grade-my-doc), resolving D2 and giving the library its adoption wedge.
5. **With P5 (distribution):** AG-1 (schema) then AG-2 (MCP), plus CT-3 (atlas) and VL-2 (treat it as funnel). Decide VL-1 (open-core) before you publish, because it changes what goes in the public repo.
6. **Ongoing:** VL-3 maintenance cadence; LP-3 telemetry once there is a channel to measure.

---

## 6. Risks and tensions

- **Quality versus coverage, again.** Every idea here is a reason to slow down and deepen rather than add types. That is the right bias for this library, but it must be conscious - the atlas (CT-3) and coverage discipline (VS-3) exist to make saying-no visible.
- **Over-engineering before real usage (YAGNI).** Evals, MCP, and schema are high-effort. Do not build them for a library nobody uses yet. The correct order is LP-2/LP-1 first (get real usage and real feedback), *then* invest in the heavy machinery the usage justifies. EV-1 is the exception - it should ride with the very first reference bundle, because it is cheapest to build once and protects everything after.
- **Solo-maintainer bandwidth.** FR-1 will generate a steady stream of maintenance work. Without VL-3, freshness quietly becomes the thing that rots. Automate the detection, but budget the human hours.
- **Business model as a distraction.** Monetization thinking (Theme G) can pull focus from craft. The mitigation is that most of Theme G is *decisions*, not builds - make them once, write them down, move on.

---

## 7. Decisions this brief asks of you

1. **Primary user:** humans, agents, or genuinely both-as-equal? If agents are first-class, Theme C (AG-1/AG-2) moves up sharply.
2. **Is this a business asset or a craft/authority asset?** That is the VL-1 fork (monetize the generator/regulated packs) versus VL-2 (pure funnel for `product-on-purpose`). Either is fine; drifting without deciding is not.
3. **Evals now or later?** My recommendation is now (with P4), because retrofitting evals across many bundles is far more expensive than building them with the first one.
4. **Durability:** does `_local/` graduate to tracked, and when? (HY-1 - this one should not wait.)
5. **How far into the 205?** Confirm the must-have 28 is the actual product ceiling for v1, with everything beyond it strictly pull-gated.

---

*This brief is additive to the existing strategy brief, implementation plan, and design spec. It proposes no change to any locked decision. Where it recommends a specific answer to an open decision (D2 via LP-1, scaffold via HY-2, research-log via HY-3), that recommendation is a starting position for discussion, not a settled call.*
