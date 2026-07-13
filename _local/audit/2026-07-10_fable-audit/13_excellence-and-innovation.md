# Excellence and Innovation: Insights and Differentiation Plays

- **Date:** 2026-07-10
- **Basis:** synthesis across the audit's seven dimensions, the verifier corrections, and the ideas backlog; everything here is opportunity, not defect (defects live in [AUDIT_REPORT.md](AUDIT_REPORT.md))
- **How to read:** section 2 is what the audit taught beyond its findings; section 3 is ranked innovation plays, each with a mini-spec; section 4 is the operating principles that keep excellence durable

---

## 1. The one-sentence thesis

The library's differentiation is not templates; it is **earned claims with visible verification**: every promise on the front door is either machine-checked, eval-measured, or explicitly labeled aspirational, and no competitor in this space even attempts that posture.

---

## 2. Insights the audit surfaced (beyond individual findings)

**2.1 The methodology outgrew the plan, and that is the normal direction.** The build produced a better bundle contract (8 files, enriched comments, research logs) than the plan specified (6 files). The failure was not the deviation; it was that the plan kept claiming authority it no longer had ("source of truth," "recorded as ADRs"). Operating rule: treat `methodology.md` as the constitution (versioned, ADR-amended) and every plan as a dated, disposable projection. Plans should carry an expiry stance: "statements here decay; STATE.md is current truth."

**2.2 Adversarial verification pays for itself; internalize it.** The audit's Phase 2 killed or downgraded 3 of 19 High findings and corrected details in 4 more, at roughly 15 percent of total token spend. The same asymmetry applies to authoring: a verifier agent that re-fetches every citation and attacks every example would have prevented the two worst content findings (A-01 Ranorex mis-support, A-02 SVPG access dates) before they shipped. The authoring pipeline should always be author-agent, then verifier-agent, then human, never author-then-human alone.

**2.3 Every claim-versus-reality finding traces to tense.** "Enforceable, not aspirational" (present tense, was aspirational), "CI-enforced" (present, no CI), "agents reach for it first" (present, no agent path), "recorded as ADRs" (past, never happened). None of these were lies; they were roadmap statements written in the present tense. The fix is a writing rule, not a process: **present tense is reserved for what a fresh clone can verify.** This single rule would have prevented findings G-02, F-05, C-01's marketing component, and the G4:381 false retrospective.

**2.4 The gate is a flywheel, not a checklist.** Every content defect the audit found implies a gate extension that makes the defect class impossible (padded entries, placeholder metas, dangling refs, stale versions). A library that converts each incident into an automated check compounds: by bundle 28, the gate embodies the accumulated failure knowledge of 28 builds. Name this explicitly in the methodology: "every defect found in review adds a check if one is expressible."

**2.5 Zero-to-one usage beats four-to-eight bundles on every axis.** The single highest-information action available is not more content; it is one real person filling or grading one real document. It tests the guidance comments (do the ASK questions actually help), the rubric (can it score), the wedge (does grading sell templates), and the catalog thesis (is PRD even the right first type). Bundle #5 before user #1 is building inventory for a store with no door.

**2.6 The repo can make its own governance a product demo.** It needs ADRs (finding F-03); it will soon have an `adr` bundle candidate (Tier 1, catalog #64). Writing the repo's own decision records USING its own ADR template collapses "we practice what we ship" from claim to artifact. The same holds for release notes (v0.1.0 tag) and, later, its own PRD for LP-2. Dogfooding here is not hygiene; it is the cheapest marketing the library will ever get.

**2.7 The seam is only as valuable as its first consumer.** `pairs_with` was designed as decoration (G5 declares it human-facing) and the audit initially misread it as a broken promise. The lesson is generalizable: machine-readable fields with no consumer degrade into decoration and then into risk (dangling `related_templates`). Rule: no new metadata field without naming its first consumer (gate check, manifest, MCP tool, or atlas view) in the same commit.

---

## 3. Innovation plays (ranked by differentiation-per-effort)

Each play: what it is, why it wins, mechanism, first step, effort, and risk. Plays 1-4 are near-term compounding; 5-9 are positional.

### Play 1: Eval-certified bundles (the "measured, not asserted" badge)

- **What:** every bundle publishes an eval scorecard: with-template vs freehand discrimination gap, judge agreement, scenario count, last-run date; surfaced in meta.yaml, manifest.json, the README table, and the atlas.
- **Why it wins:** no template collection anywhere publishes evidence that its templates improve output. One number ("+31 percent rubric lift over freehand, 3 blind judges, n=12") converts the entire positioning from adjective to measurement. It is also a regression harness, so quality cannot silently decay.
- **Mechanism:** EV-1 harness (WP-40, [specs/spec_ev1-efficacy-evals.md](specs/spec_ev1-efficacy-evals.md)) writes `scorecard:` into meta; manifest and atlas render it.
- **First step:** port the pm-skills runner against the PRD bundle with 3 scenarios.
- **Effort:** L once; S per bundle after. **Risk:** judges over-fit to the rubric; mitigate with an anchor set of human-graded outputs.

### Play 2: Conformance levels (structure, research, proof)

- **What:** a bundle-level maturity grammar the gate computes and the catalog displays: **L1 Structural** (all 8 files, nesting, placeholders, links), **L2 Research-verified** (citation census clean, fetch_status honest, staleness green), **L3 Eval-proven** (scorecard above threshold, regression wired).
- **Why it wins:** it converts "best-in-class" from a binary boast into a legible ladder; it gives contributors a target; and it makes the honest state of every bundle visible (the audit's F-05 status-conflict finding becomes structurally impossible).
- **Mechanism:** gate computes level from existing checks + scorecard presence; `conformance: L2` in meta; atlas legend.
- **First step:** define the three levels in the family contract (WP-24) and have the gate print them.
- **Effort:** S-M. **Risk:** level inflation; keep level definitions in the contract under ADR control.

### Play 3: The trust manifest (verifiable provenance chain)

- **What:** `manifest.json` carries a sha256 per bundle file and per template version; filled documents already carry `source_template` + `source_template_version`; a 30-line `verify-provenance` tool answers "which live docs run on a deprecated or modified template" and "was this doc really filled from v0.1.0."
- **Why it wins:** the design spec promised exactly this query and no template system delivers it; it turns provenance from frontmatter decoration into an auditable chain. For future regulated-tier work (D4), this is the load-bearing primitive.
- **Mechanism:** gen-manifest hashes files; verify tool compares a filled doc's stamp against the manifest history (kept per tag).
- **First step:** add hashes to the manifest generator (WP-22); the verify tool can wait for demand.
- **Effort:** S for hashes, M for the verifier. **Risk:** none material; hashes are free.

### Play 4: Grade-my-doc as a self-marketing artifact (LP-2's second life)

- **What:** the LP-2 report card is designed to be shareable: a clean, branded markdown "PRD Report Card: B+ (missing non-goals, unguarded success metric)" that a PM can paste into Slack. Every shared card advertises the rubric, and the rubric advertises the template.
- **Why it wins:** the wedge acquires its own distribution. Most tools' output dies in a terminal; a report card is social currency in exactly the audience the library wants.
- **Mechanism:** the report format in [specs/spec_lp2-grade-my-doc.md](specs/spec_lp2-grade-my-doc.md) section 5 is written for forwarding (verdict first, three fixes, one link).
- **First step:** ship LP-2 (WP-30) with the shareable format as the default output.
- **Effort:** free if designed in. **Risk:** harsh grades alienate; the spec's tone rules handle this.

### Play 5: The dogfood loop (govern the repo with its own artifacts)

- **What:** every internal governance document that has a bundle counterpart is produced from that bundle: release notes from `release-notes` (starting at v0.1.0, WP-14), decision records from the future `adr` bundle, the LP-2 feature definition from `prd`, retro/postmortem of the first usage cycle from their bundles when built.
- **Why it wins:** "our own repo runs on these templates" is unfalsifiable credibility, produces real (not fictional) example material over time, and surfaces template defects through daily use, which is the usage loop in miniature.
- **First step:** WP-14's dogfooded release note; then the ADR bundle build (12_catalog section 4) writes the repo's ADRs as its worked example.
- **Effort:** near-zero marginal. **Risk:** internal docs drift from template updates; the provenance stamp (Play 3) detects exactly this.

### Play 6: Pull queue as public demand telemetry

- **What:** the GitHub issue form (WP-32) doubles as public, structured demand data: each request carries type, context, methodology, urgency; the atlas heat-maps requested-but-not-built types.
- **Why it wins:** turns "coverage discipline" (VS-3) from a private virtue into a visible, participatory roadmap; converts the 201 not-built types from a gap into an invitation; and gives LP-3 telemetry a zero-infrastructure v0.
- **First step:** one issue-form YAML + an atlas `state` field render (the field already exists as `built`; extend to the 4-state enum).
- **Effort:** S. **Risk:** empty queue looks bad early; seed it honestly with the repo's own internal pulls (adr is one).

### Play 7: The agent authoring kit as a product surface (AG-3)

- **What:** package what already tacitly exists: the methodology, a bundle-scaffolding prompt, the verifier-pass recipe (2.2 above), and the source directory (11_resources section 5) as `docs/contributing/agent-authoring-kit.md`.
- **Why it wins:** it is the bus-factor mitigation (any capable agent session becomes the second maintainer), the contribution pipeline (external contributors run the same kit), and a meta-demonstration that agent-native applies to production, not just consumption.
- **First step:** transcribe the four-bundle build session's actual process into the kit.
- **Effort:** S-M (mostly exists as tacit process). **Risk:** kit rot; the quarterly cadence re-runs it on one bundle as a drill.

### Play 8: Ecosystem interop position (registry-ready metadata)

- **What:** keep bundle metadata forward-mappable to whatever the agent-skills ecosystem standardizes for non-skill resources: resolve D3 (agentskills.io resource type, 1-hour read), track the MCP registry when AG-2 ships, and document the mapping in the machine-metadata spec.
- **Why it wins:** first-mover template libraries that align with the winning resource spec get default-listed; retrofitting after 28 bundles is exactly the cost the plan warned about.
- **First step:** the D3 read (WP-12), recorded as an ADR with a mapping table.
- **Effort:** S now. **Risk:** spec churn; mitigate by mapping, not adopting wholesale.

### Play 9: The reference-implementation scorecard (public self-audit)

- **What:** a standing `docs/reference/reference-implementation-scorecard.md`: the claims ledger (governed, researched, sized, traceable, agent-native, measured, distributed), each with its current state (true / partial / roadmap) and the artifact proving it, refreshed each release; optionally, re-run a downsized version of this audit annually and publish the grade trend.
- **Why it wins:** it institutionalizes the audit's tense discipline (2.3), makes honesty itself the brand, and gives every release a visible delta ("agent-native moved from roadmap to true in v0.4").
- **First step:** seed it from this audit's moat reality-check table (G-02/G-03 evidence).
- **Effort:** S. **Risk:** it embarrasses when neglected, which is precisely the point.

---

## 4. Operating principles for durable excellence (proposed for methodology v0.3)

1. **Present tense is earned.** A capability is described in present tense only when a fresh clone can verify it (gate output, CI badge, eval number, install command).
2. **Every defect becomes a check.** If a review or audit finds a defect class expressible as automation, the fix ships with its gate extension.
3. **No metadata without a consumer.** Every new machine-readable field names its first consumer in the same commit.
4. **Author-verify-decide.** Agent drafts, adversarial agent attacks, human decides. No bundle ships without the middle step.
5. **Demand before depth.** Bundle N+1 requires a pull (external request, or a named internal dogfood need); coverage is never self-justifying.
6. **Decisions age fast or get dates.** Under-2-hour decisions resolve in 3 working days; everything else carries an owner and a decide-by date.
7. **The constitution is versioned.** methodology.md changes only via ADR; plans are dated projections subordinate to STATE.md.
8. **Honesty compounds.** Publish the scorecard, the conformance level, the fetch_status, the not-built states. Every visible admission buys trust that marketing cannot.
