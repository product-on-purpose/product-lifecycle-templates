# Catalog Recommendations: What to Build Next, and How to Decide Forever

- **Date:** 2026-07-10
- **Basis:** the master catalog (G7, 205 types), the atlas dataset (`_local/atlas/catalog-data.json`, which carries `tier`, `must_have`, `built` per type), the pm-skills seam (68 skills inspected), and audit findings B-05 (dangling references), D-05 (zero usage), E-04 (maintainer math)
- **Prime directive (unchanged):** demand-gated growth. Catalog Recommendation 1 stands: no speculative bundles; a pull (external request, or a named internal dogfood need) is the ticket to build.

---

## 1. Position, with exact numbers

- Tier 1 per the atlas data: **27 must-have types, 4 built (14.8 percent)**: `product-requirements-document`, `user-story`, `acceptance-criteria`, `release-notes`. 23 remain.
- **Count drift found while preparing this doc:** the catalog prose says "must-have 28" (G7 TL;DR line 4 and Recommendation 1); the atlas data marks 27 types `must_have: true`. One of the two is wrong, and this is precisely the count-consistency defect class the plan's own AC-13 guards against. **Recommendation:** reconcile (find the missing 28th or correct the prose), and extend the count-consistency check (roadmap WP-22) to cover the Tier-1 claim wherever it appears.
- Two Tier-1 types are not naturally markdown templates: `wireframe` and `interactive-prototype` are design artifacts. **Recommendation:** re-scope them as their documentation shadows (a wireframe/prototype **brief**: goals, flows to cover, fidelity, review questions) or mark them `out-of-scope` in the atlas state model (section 5) with one line of reasoning. Do not quietly count them against template progress either way.
- Seven Tier-1 types are single-size (`S` only) per the catalog's own size_variant column: `user-story` (built), `acceptance-criteria` (built), `definition-of-done`, `architecture-decision-record`, `test-case`, `bug-report-defect-report`, `sprint-retrospective-notes`. Two implications: (a) these are the cheapest bundles to build (no full variant, no nesting surface), making them ideal pull-response quick wins; (b) **the gate and methodology must formally support single-variant bundles**: today `check_nesting` fails if lean or full is missing, and the methodology's lean/full default needs the "let the type decide" escape hatch made operational (`sizes_available: [s]` handled by the gate; see [specs/spec_machine-metadata.md](specs/spec_machine-metadata.md) section 3).

---

## 2. The scoring framework (how every "what next" decision gets made)

Score each candidate 0-2 per criterion; build order within a pull cohort follows the total. Weights reflect the library's strategy (seam-first, demand-gated, credibility-compounding):

| Criterion | Weight | 2 means |
|---|---|---|
| Demand signal | x3 | A named requester in the pull queue (internal dogfood need counts once) |
| Tier | x2 | Tier-1 must-have |
| pairs_with liveness | x2 | A pm-skills skill exists today for this type |
| Research base strength | x2 | Originator or standards-body primary sources exist and are fetchable |
| Wedge synergy | x1 | LP-2 can grade documents of this type that teams already have in quantity |
| Dogfood value | x1 | The repo itself would use the bundle on itself |
| Build cost (inverse) | x1 | S-only single variant or otherwise cheap |

Rule of use: **demand is a gate, not just a weight.** A candidate with zero demand signal does not get built regardless of score; the scores rank what to pre-stage (research directories, catalog seeds) so the response to a pull is fast.

---

## 3. Scored shortlist (pre-staging order, not a build queue)

| Candidate | Catalog ref | Tier | Pairs with (live?) | Sizes | Score highlights | Total (of 24) |
|---|---|---|---|---|---|---|
| architecture-decision-record | #64 (Nygard, MADR) | 1 | develop-adr (yes) | S only | Demand: internal dogfood pull EXISTS (audit F-03 requires the repo write its own ADRs); primary sources exemplary (Nygard 2011, MADR spec, adr.github.io, all fetch-verified in the audit); cheap S-only build; LP-2 gradable (eng orgs have piles of ADRs) | 22 |
| software-design-document / design doc | #47 (IEEE 1016) | 1 | develop-design-rationale (adjacent yes) | S/M/L | Strong sources (IEEE 1016, industry design-doc culture); high wedge value (every eng org has design docs to grade); costlier (3 sizes candidate; recommend lean/full) | 18 |
| incident-postmortem | #127 | 1 | none | S/M/L | Superb sources (Google SRE, blameless culture canon); huge wedge surface; no seam skill yet | 15 |
| runbook | #116 | 1 | none | S/M/L | Strong sources (SRE); contested boundary with playbook/SOP (#117, #198) makes the companion genuinely valuable | 14 |
| status-report | #180 | 1 | foundation-stakeholder-update (yes) | S/M | Cheap, common, seam live; weaker research canon (PMBOK-generic) | 14 |
| okrs | #6 | 1 | foundation-okr-writer + measure-okr-grader (yes, two) | S/M | Two live seams; good sources (Doerr, Grove); grader skill hints at LP-2-style synergy | 14 |
| sprint-retrospective-notes | #187 | 1 | iterate-retrospective (yes) | S only | Cheap; live seam; light research base | 13 |
| definition-of-done | #39 | 1 | none direct (AC bundle relates) | S only | Completes the requirements trio; Scrum Guide primary source already in the library's source set | 12 |
| test-plan | #102 (ISO/IEC/IEEE 29119-3) | 1 | none | M/L | Standards-heavy (the 29119 supersession story is already researched in the catalog); regulated-adjacent value | 12 |
| experiment-design | #142 | 2 | measure-experiment-design (yes) | S/M | Live seam; strong methodology sources (Kohavi); Tier-2 so strictly pull-gated | 11 |
| spike-summary | #67 | 2 | develop-spike-summary (yes) | S | Cheap; live seam; thin research canon | 10 |
| rfc (engineering) | #48 | 2 | none | S/M | Pairs naturally with ADR in a family; occasional rarity | 9 |

### The recommendation

**Next family: `decision-docs` (develop phase), led by the ADR bundle, and the ADR bundle is buildable now because a genuine pull already exists: the repository's own governance needs ADRs (audit finding F-03).** The family:

| Bundle | Catalog | pairs_with | Sizes | Note |
|---|---|---|---|---|
| adr | #64 | [develop-adr] | [s] | First; dogfoods docs/decisions/ (the repo's 7 pending ADRs become its worked-example material, with the fictional-example rule adapted: real decisions, no confidentiality issue) |
| design-doc | #47 | [develop-design-rationale] | [lean, full] | Second; the RFC-vs-ADR-vs-design-doc contested boundary (catalog Caveats) is exactly the debate a companion exists to referee |
| spike-summary | #67 | [develop-spike-summary] | [s] | Third; cheap |
| rfc | #48 | null | [lean, full] | Fourth; pairs_with null is legitimate per the DoD |

Why this family beats the alternatives at pre-stage time: highest aggregate score; every member has fetchable primary sources; three of four seams are live; ADR + design-doc are Tier-1; the dogfood story (Play 5 in [13_excellence-and-innovation.md](13_excellence-and-innovation.md)) turns the build itself into credibility; and it exercises the single-variant bundle mechanics the gate needs anyway (section 1). The ops family (postmortem, runbook) is the strongest external-demand bet; hold it at pre-stage until a real pull arrives, then it jumps the queue on the demand multiplier.

---

## 4. The dangling references, resolved properly (audit B-05 follow-through)

| Reference | Where | Situation | Recommendation |
|---|---|---|---|
| `solution-brief` | prd_meta related_templates | No catalog entry exists for a "solution brief"; the pm-skills skill develop-solution-brief exists; nearest catalog types are #47 (SDD) and #27 (concept/validation brief) | Short-term: `future:solution-brief` label (roadmap WP-03). Decision needed: either add a catalog entry via a catalog-amendment note (the catalog is versionable content, not scripture) or alias solution-brief to the design-doc bundle when built. Record whichever as a one-paragraph ADR |
| `launch-checklist` | release-notes_meta related_templates | Catalog #126 is the SRE launch-coordination checklist (rarity: rare); the pm-skills deliver-launch-checklist skill is a PM/GTM launch checklist; these are different artifacts sharing a name | `future:launch-checklist` label now; when pulled, disambiguate in the alias index (gtm-launch-checklist vs sre-launch-checklist) rather than building a chimera. This name collision is exactly what the alias-index exists to referee |

---

## 5. Catalog infrastructure recommendations

### 5.1 Atlas state model (extends the existing `built` boolean)

`catalog-data.json` already carries `built: true/false` per type. Extend to a four-state enum, keep `built` for backward compatibility during one release, and render a legend in the atlas:

```json
"state": "built | queued | pull-gated | out-of-scope",
"state_note": "one line: why, or what the pull was",
"bundle_path": "templates/prd/ (present when state=built)"
```

- `built`: bundle exists and passes the gate (4 today).
- `queued`: a real pull exists; pre-staged for build (adr today, via the internal F-03 pull).
- `pull-gated`: the default for the other ~199; explicitly a decision, not a gap (VS-3 made visible).
- `out-of-scope`: with a reason (wireframe, interactive-prototype as design artifacts; Tier-3 regulated pending D4).

This turns the atlas from a map of what exists in the literature into a map of the library's decisions, which is the stronger artifact.

### 5.2 Alias index (P7 item, pulled forward cheaply)

Format per the catalog's own appendix recommendation:

```json
{
  "product spec": "templates/prd",
  "product brief": "templates/prd",
  "one-pager": "templates/prd",
  "conditions of satisfaction": "templates/acceptance-criteria",
  "decision record": "templates/adr",
  "RCA": "future:incident-postmortem"
}
```

Generate the built entries from each meta's `aliases` field (they already exist in all four metas); hand-add high-traffic unbuilt aliases pointing at `future:` targets. Gate check: every non-future target path exists. First consumers (per the no-metadata-without-a-consumer rule): LP-2 type detection and the future MCP `select` tool.

### 5.3 pairs_with coverage ledger (the v1.0 parity yardstick)

The design spec's v1.0 milestone is phase-coverage parity with pm-skills document-producing skills. Grounding count from the skills directory: roughly 40 of the 68 skills produce documents (6 deliver, 5 define, 4 develop, 5 discover, ~10 doc-producing foundation, 4 iterate, 6 measure; the tool-* sprint suites and utility-* skills are workflow/meta, not document types). Current template coverage: **4 of ~40 (10 percent)**. Recommendation: publish this ledger as a generated table in `docs/reference/` (skill, doc type, catalog ref, bundle state) so "parity" stops being a vibe and becomes a number the manifest can carry. Do not treat the ledger as a backlog; it is the denominator for honest progress reporting.

### 5.4 Pull queue mechanics (WP-32 detail)

GitHub issue form fields (structured, machine-readable):

```yaml
- type: dropdown  # requested_type: all 205 catalog ids + "not in catalog"
- type: input     # requester_context: team/role, org size
- type: dropdown  # methodology_in_use: generic/scrum/safe/shape-up/lean/regulated
- type: textarea  # the_document_you_write_today: what they currently use (LP-2 bait)
- type: dropdown  # urgency: this-quarter / someday / just-signal
```

Demand rules: one named requester moves a type to `queued`; the maintainer's own governance needs count as one pull each (adr is the standing example); three or more requests for a Tier-2 methodology pack trigger the catalog's active-practice test before build. Every closed pull gets a link to the shipped bundle and an EV-3 follow-up.

### 5.5 Tier-2 and Tier-3 discipline (restated as policy)

- **Tier-2 methodology packs** (scrum-docs, shape-up, working-backwards, ux-discovery, analytics, release-ops): build only on evidence a requesting team actively practices the methodology (catalog Recommendation 2). The pull-queue methodology field is the evidence capture.
- **Tier-3 regulated** (FDA design controls, ISO 14971, SOC 2, GDPR): blocked on decision D4 (appetite), and on the QMSR currency discipline the catalog demands (regulation text verified on ecfr.gov at authoring time; the QMSR retitle effective 2026-02-02 is the standing example of why). If D4 opens this tier, it ships as a separate access-controlled module with traceability-first templates and the Play-3 provenance chain as a prerequisite, not an option.

### 5.6 Example-diversity plan (CT-1, scheduled rather than aspirational)

The single-domain limitation (all examples chain on one B2B SaaS feature) is a documented validity limit on the "templates travel" claim. Plan: at M4 (WP-43), give the PRD bundle a second worked example from a contrasting domain, recommended **consumer-mobile feature or regulated-health workflow**, plus one lean-variant example (all current examples are full-variant). Acceptance: the second example passes the same gate checks, carries its own provenance stamp, and the companion's worked-example pointer lists both with a one-line "what differs by domain" note. Other bundles follow only on demand; one proven traveling template is worth more than four asserted ones.

---

## 6. What NOT to add to the catalog surface (guardrails)

- No new bundle types invented outside the catalog without a catalog-amendment note first (the catalog is the controlled vocabulary; solution-brief is the live test case).
- No S/M/L three-variant builds by default; the catalog's own size_variant column plus the variant-model decision say most types earn two sizes or one.
- No methodology-pack scaffolding (empty family dirs, placeholder metas) ahead of pull; empty structure reads as shelfware and contradicts VS-3's visible-discipline posture.
