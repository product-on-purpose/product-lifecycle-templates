# Audit Package Index: 2026-07-10 Fable Audit and Delivery Expansion

Everything produced by the 2026-07-10 audit of `product-lifecycle-templates` and its follow-on expansion, in reading order.

## The audit (produced first)

| File | What it is |
|---|---|
| [AUDIT_REPORT.md](AUDIT_REPORT.md) | The main deliverable: executive summary, corpus fingerprint, 49 prioritized findings (19 adversarially verified), detailed findings with ready-to-commit snippets, roadmap, ideas, documentation rebuild plan, traceable source list |
| [00_context-sheet.md](00_context-sheet.md) | Phase 0 corpus fingerprint given to every audit agent: governance corpus map, bundle inventory, plan-vs-actual gap map, open-decisions ledger |
| [findings/raw-results.json](findings/raw-results.json) | Full structured output of all 7 dimension auditors and 19 verifiers |
| [findings/digest.md](findings/digest.md) | Merged human-readable digest with verifier notes and the priority table |

## The delivery expansion (produced second, on request)

| File | What it is |
|---|---|
| [10_roadmap-expanded.md](10_roadmap-expanded.md) | Milestones M0-M6 with work packages, acceptance criteria, dependencies, timeline, non-goals, and roadmap-staleness safeguards |
| [11_resources-and-sustainability.md](11_resources-and-sustainability.md) | The resource model (human + agents + gate), per-bundle cost model, maintenance economics and the VL-3 cadence proposal, port-vs-build-vs-adopt tooling inventory, authoring source library |
| [12_catalog-recommendations.md](12_catalog-recommendations.md) | Exact Tier-1 position (4 of 27 built; count-drift flag), the scoring framework, the decision-docs family recommendation led by the ADR bundle, dangling-reference resolutions, atlas state model, alias index, pull-queue mechanics, coverage ledger |
| [13_excellence-and-innovation.md](13_excellence-and-innovation.md) | Seven cross-cutting insights, nine ranked innovation plays (eval-certified bundles, conformance levels, trust manifest, dogfood loop, and more), eight operating principles proposed for methodology v0.3 |

## The depth pass (produced third: Fable-grade analyses and the adoption kit)

| File | What it is |
|---|---|
| [14_flagship-content-review.md](14_flagship-content-review.md) | The review the audit did not perform: a substantive editorial critique of the PRD bundle's actual advice quality (verdict: B+ against best-in-class; seven CR findings incl. the missing AI-era debate, the measurement-teaching gap, and a requirements-to-stories traceability slip in the example), with a one-pass revision plan |
| [15_measurement-validity.md](15_measurement-validity.md) | Adversarial epistemics for EV-1 before its number goes public: the precise estimand, eight threats to validity (rubric circularity, form bias, strawman control, and more) with mitigations incl. the hollow-template control arm, and a nine-item spec amendment list |
| [16_premortem.md](16_premortem.md) | Seven failure narratives ranked by honest probability, each with early signal, tripwire, and pre-commitment; the two-day insurance policy that covers the top three |
| [adoption-kit/](adoption-kit/README.md) | Ready-to-review drafts of the judgment-bearing M0 artifacts: **eight** ADRs (the audit's seven plus a newly surfaced one recording the doc-type-spine bundle-ID decision that diverged from the plan), the delivery-docs family contract, and STATE.md. Review, move into place, commit |

## Build specs

| File | What it specifies |
|---|---|
| [specs/spec_lp2-grade-my-doc.md](specs/spec_lp2-grade-my-doc.md) | The adoption wedge: grade an existing document against a bundle's rubric; report-card format; ships as a skill (which also unlocks the skills-CLI channel) |
| [specs/spec_lp1-use-template-flow.md](specs/spec_lp1-use-template-flow.md) | Interview-driven fill flow; the normative guidance-comment grammar; strip-template.py behavior |
| [specs/spec_ev1-efficacy-evals.md](specs/spec_ev1-efficacy-evals.md) | Two-arm blind-judged efficacy evals; scenario format; discrimination-gap metric; regression policy; honest-number rules |
| [specs/spec_ag2-mcp-server.md](specs/spec_ag2-mcp-server.md) | Deterministic MCP server (5 tools, 3 resources, token budgets, provenance headers), mirroring the pm-skills-mcp stack |
| [specs/spec_machine-metadata.md](specs/spec_machine-metadata.md) | meta.yaml field contract with consumers, manifest.json format, single-variant bundle support, instance frontmatter v0.2, alias index, section schema, the gate check alphabet A-N |

## Suggested reading paths

- **15 minutes:** AUDIT_REPORT.md section 1 (executive summary) + 10_roadmap-expanded.md sections 1-2.
- **Deciding what to do Monday:** 10_roadmap-expanded.md M0/M1 tables (one day + one week of work, fully specified).
- **Deciding what to build next:** 12_catalog-recommendations.md sections 1-4.
- **Understanding the long game:** 13_excellence-and-innovation.md, then the specs.
