# Resources and Sustainability Plan

- **Date:** 2026-07-10
- **Basis:** audit findings E-04 (maintainer math), G-05 (unowned sustainability risks), D-04 (evals portability), plus the Phase 0 corpus fingerprint
- **Question this answers:** who does the work, with what tooling, at what recurring cost, and how the math closes at Tier-1 scale (28 bundles) on a solo maintainer

---

## 1. The resource model: one human, many agents, one constitution

The library was already built this way (four bundles authored agent-assisted under `methodology.md` in roughly two working days) and the model should be named rather than left tacit:

| Role | Held by | Responsibilities |
|---|---|---|
| Maintainer (human) | jprisant | Decisions (ADRs, quality-bar ratification, releases), real-usage relationships, taste on examples and guides, final review against the DoD |
| Author (agent) | Claude sessions under the methodology + AG-3 kit | Research sweeps, drafting all 8 bundle files, citation logging, gate-fixing until green |
| Verifier (agent) | Separate agent sessions | Adversarial passes: refute citations, attack examples, re-derive nesting (the audit's Phase 2 pattern, applied to authoring) |
| Enforcement (machine) | Gate + CI + link-check + evals | Everything decidable without judgment; growing per the roadmap's WP-11/WP-21/WP-26/WP-40 |

The division of labor rule, borrowed from the plan's own owner column: **an agent drafts, a machine checks, a human decides.** Everything in the maintenance economics below assumes this split; without agent leverage, multiply the human hours by roughly 4-6x and the Tier-1 math genuinely does not close.

---

## 2. Cost model per bundle (build)

Grounded in the observed build (4 bundles, 2026-06-30, agent-assisted, per the session log) plus the audit's finding that citation integrity needed a second pass:

| Activity | Agent hours (wall-clock) | Human hours | Notes |
|---|---|---|---|
| A-phase research sweep + research log | 1.0 - 2.0 | 0.3 | Live fetches; fetch_status recorded per source (WP-26 convention) |
| Variants (lean + full) with enriched comments | 0.5 - 1.0 | 0.3 | Comment standard is mechanical once anatomy is settled |
| Companion (11 sections, cited) | 1.0 - 2.0 | 0.5 | The expensive artifact; quality ceiling set here |
| Guide + example + meta + history | 0.5 - 1.0 | 0.3 | Example realism needs the human eye most |
| Adversarial verify pass (citations, example integrity) | 0.5 - 1.0 | 0.2 | NEW relative to the first four bundles; prevents the A-01/A-02 class |
| Gate + eval baseline | 0.2 | 0.2 | Post-M4: 3 scenarios per new bundle |
| **Total per bundle** | **~4 - 7 agent-hours** | **~1.5 - 2 human-hours** | Human cost is the binding constraint |

**Tier-1 completion cost (24 remaining bundles):** roughly 36 to 48 maintainer hours plus agent time, spread across demand-gated pulls. At 2 bundles per month by pull, Tier 1 completes in about a year without ever being a backlog obligation. This is affordable IF AND ONLY IF the pull gate holds (no speculative building) and the verify pass is agent-run.

---

## 3. Maintenance economics (the recurring cost the audit flagged as unowned)

Projection basis: 37 citation anchors across 4 bundles today (verified count), ~9.25 per bundle, so ~259 at Tier-1 complete (E-04 arithmetic, verifier-confirmed).

| Recurring activity | Frequency | Cost if manual | Cost with automation | Automation that buys it |
|---|---|---|---|---|
| Link-rot detection (37 to 259 URLs) | Every push + weekly schedule | 2-6 h/quarter, growing linearly | ~0 (exceptions only) | WP-26 lychee in CI |
| Version staleness (cited standards editions) | Quarterly | 1-2 h/quarter | 0.5 h/quarter (only flagged items) | fetch_status + versioned-URL lint + quarterly report |
| Eval regression on template change | Per change | n/a (nothing measured) | ~15 min compute per changed bundle | WP-40 harness |
| Meta/manifest consistency | Per change | error-prone by hand | 0 | WP-21/WP-22 schema + generator |
| Decision triage | Monthly | drift (the 11-day D2 pattern) | 15 min/month | Decision SLA + STATE.md review |
| Freshness pass (re-verify flagged sources, refresh scorecards) | Quarterly | 4-8 h at Tier-1 scale | 1-2 h (automation surfaces the shortlist) | The quarterly cadence below |

**Proposed VL-3 maintenance cadence (write this as the ADR the audit asked for):**
- **Per push (machine):** gate, schema, manifest count, link-check, eval subset on changed bundles.
- **Monthly, 30 minutes (human):** decision triage against the SLA; pull-queue review; STATE.md refresh if drifted.
- **Quarterly, half a day (human + agent):** freshness pass over flagged sources; scorecard refresh; one adversarial re-audit of a randomly chosen bundle (the audit's Phase 2 pattern, downsized).
- **Per release (human):** CHANGELOG, tag, dogfooded release note.

Annual steady-state maintainer cost at Tier-1 scale under this cadence: **roughly 30-40 hours/year** plus build time for pulled bundles. That closes on a solo maintainer. Without the automation column, the same list is 80-150 hours/year of error-prone manual work, which does not.

---

## 4. Tooling inventory: build, port, adopt

### 4.1 Port from pm-skills (proven assets, adaptation cost only)

| Needed capability | pm-skills source asset | Port effort | Roadmap WP |
|---|---|---|---|
| Output-quality eval runner (two arms, blind judges, aggregation) | `scripts/output-eval.workflow.mjs`, `scripts/output-eval-aggregate.mjs` (unit-tested) | M: swap "skill arm" for "template+guidance arm"; scenario bank is new | WP-40 |
| Eval rubrics for all four current types | `docs/internal/eval-rubrics/specification.md` (prd, acceptance-criteria, user-stories) and `communication.md` (release-notes) | S: extraction; per-bundle guide rubrics map to skill-specific criteria | WP-40 |
| Manifest generation pattern | `scripts/gen-skill-manifest.mjs` | S-M: walk `templates/*/meta.yaml`, emit manifest.json | WP-22 |
| Count-consistency guard | `scripts/check-count-consistency.*` | S | WP-22 |
| Family-contract validator pattern | `scripts/validate-skill-family-registration.*` + meeting-skills contract doc | M | WP-24 |
| Frontmatter lint pattern | `scripts/lint-skills-frontmatter.*`, `check-frontmatter-yaml.mjs` | S-M | WP-11/WP-21 |
| Root scaffold files | LICENSE, CONTRIBUTING.md, CODE_OF_CONDUCT.md, SECURITY.md, AGENTS.md | S: copy and adapt | WP-01, WP-27 |
| MCP server architecture | `pm-skills-mcp` (TypeScript, `dist/` build, embed-content script, vitest, npm bin, v2.9.3) | L: same stack, new tool surface per the AG-2 spec | WP-51 |
| Release hygiene | pm-skills CHANGELOG discipline, release-please config as reference | S | WP-14/WP-28 |

The strategic point the audit made stands: **almost nothing here is design work; it is porting against a live reference implementation one directory away.** The gap is execution hours, not uncertainty.

### 4.2 Build new (nothing comparable exists to port)

| Tool | Purpose | Size | Spec |
|---|---|---|---|
| `tools/meta.schema.json` + schema check | Metadata contract enforcement | S | specs/spec_machine-metadata.md |
| `tools/gen-manifest.py` (or .mjs) | Root machine catalog with hashes and approx_tokens | S-M | machine-metadata spec |
| `tools/strip-template.py` | Comment strip + fill_date stamp | S (~25 lines) | LP-1 spec section 4 |
| `skills/grade-doc/` (LP-2) | The adoption wedge | M-L | specs/spec_lp2-grade-my-doc.md |
| `skills/use-template/` (LP-1) | The fill flow | M-L | specs/spec_lp1-use-template-flow.md |
| Scenario bank (12 files) | EV-1 input | M | specs/spec_ev1-efficacy-evals.md |
| Section-schema generator (AG-1) | Machine shape of each template | M | machine-metadata spec section 6 |
| Pull-queue issue form | Demand capture | S | 12_catalog-recommendations.md section 5 |

### 4.3 Adopt external (no build)

| Tool | Use | Reference |
|---|---|---|
| lychee | Link-rot gate in CI | https://github.com/lycheeverse/lychee |
| GitHub Actions | All CI | https://docs.github.com/en/actions |
| python jsonschema (or ajv if Node) | Schema validation in the gate | https://json-schema.org |
| yamllint | Meta syntax hygiene (optional, cheap) | adopt as-is |
| GitHub issue forms | Pull queue with structured fields | native GitHub feature |

---

## 5. The authoring source library (research resources per family)

A reusable, tiered source directory so each new bundle's A-phase starts from a vetted list instead of a cold search. Seeded from the four research logs plus the catalog's named sources; maintain it as `docs/reference/source-directory.md` once the docs tree exists (WP-27).

| Family / domain | Tier 1 (primary) | Tier 2 (practitioner) | Tier 3 (vendor) |
|---|---|---|---|
| Delivery docs (current) | Scrum Guide 2020; Keep a Changelog; SemVer; Conventional Commits; ISO/IEC/IEEE 29148 | Cagan/SVPG (403-blocked: cite via qualifier convention), Lenny's Newsletter (paywall: subscriber access recommended), Gojko Adzic (BDD/spec-by-example), Mike Cohn | Atlassian, Aha!, ProductPlan (structure only, corroborate) |
| Decision docs (recommended next) | Nygard "Documenting Architecture Decisions" (2011, the origin); MADR spec; adr.github.io; IEEE 1016 (SDD) | ThoughtWorks Tech Radar on ADRs; Design Docs at Google (industry writeups) | GitHub/Spotify engineering blogs |
| Ops/incident (Tier-1, pull-gated) | Google SRE Book + SRE Workbook (postmortems, runbooks, launch checklists); NIST SP 800-61 (IR playbooks) | learning-from-incidents community; PagerDuty postmortem guides (vendor-practitioner boundary: tag honestly) | incident.io, Atlassian |
| Measure/experiment | Kohavi et al. (Trustworthy Online Controlled Experiments); NN/g on metric definition | Reforge growth essays; Evan Miller sample-size writing | Optimizely/LaunchDarkly docs |
| Strategy/OKR | Doerr (Measure What Matters, originator-adjacent); Grove (High Output Management) | Cagan strategy essays; Ramp one-pager examples | Perdoo/WorkBoard (structure only) |

Rule carried from the audit (A-02 SVPG access-date finding): the **fetch_status convention is part of the resource model**, not an afterthought; a source that cannot be fetched directly is cited with its retrieval qualifier, and the paywalled source most-cited across the library (currently Lenny's Newsletter, 7 inline citations in the PRD companion) justifies one subscription as a research expense.

---

## 6. Sustainability decisions still owned by the human (with recommendations)

| Decision | Recommendation | Cost of continued silence |
|---|---|---|
| VL-1 business model | Free and open (Apache-2.0), positioned as the credibility engine and funnel for product-on-purpose (the G6 brief's VL-2 posture); revisit open-core only if a real org requests private regulated packs or profile tailoring | Distribution decisions keep stalling on an unmade choice; the audit found this "total whitespace" |
| VL-3 maintenance cadence | Adopt section 3's cadence as a one-page ADR with calendar entries | Freshness silently rots; the moat decays first where it is least visible |
| Second maintainer path | Do not recruit yet; instead ship AG-3 (authoring kit) + the ADR set + authoring-contract doc so that any competent agent session IS the second maintainer; revisit human co-maintainer at Tier-1 half-complete | Bus factor stays 1 with no mitigation at all |
| Contribution posture | Accept proposals via the pull-queue issue form; contributions land as agent-drafted, maintainer-reviewed bundles held to the same DoD; no direct-PR bundle contributions until the family contract + full gate are live (M2) | Either zero contributions forever, or early contributions that cost more to review than to write |
