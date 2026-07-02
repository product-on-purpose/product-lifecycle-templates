---
title: "Deep Research Prompt: Exhaustive PM and SDLC Document Catalog"
status: ready
doc_version: 1.0.0
owner: "{{owner}}"
last_reviewed: 2026-06-28
purpose: "Drive a deep-research run that enumerates every PM and SDLC document/artifact type, as input to the template library."
---

# Deep Research Prompt: Exhaustive PM and SDLC Document Catalog

## How to use this

Paste the prompt block below into a deep-research agent (Claude's Research feature, or any long-horizon research tool). It is engineered for **completeness over speed**: it forces a category-by-category sweep, demands aliases and niche artifacts, and refuses to stop until each category is saturated. The per-item schema is aligned to the template library's frontmatter (`phase`, `doc_type`, owner role, typical sections), so the output drops straight in as the candidate list of document types the library should cover.

If your tool truncates long runs, execute it in passes: run once per category block in the Coverage Matrix, then a final reconciliation pass.

---

## The prompt

```
ROLE
You are a meticulous research librarian and product/engineering process
historian. Your specialty is cataloging document and artifact TYPES used
across product management and the software development lifecycle (SDLC).
You are exhaustive to the point of obsession. You would rather list a rare,
niche, or legacy artifact and flag it as uncommon than omit it.

MISSION
Produce a ridiculously exhaustive, deduplicated master catalog of EVERY
document, artifact, deliverable, and record type used anywhere across product
management and the SDLC, from initial idea through operation and end-of-life.
Cover all methodologies, all roles, all org sizes, and all maturity levels.
"Document type" means a reusable category of artifact (for example "Product
Requirements Document"), not a specific instance. Include both heavyweight
formal documents and lightweight artifacts (one-pagers, canvases, briefs,
tickets, records, logs).

EXHAUSTIVENESS MANDATE (read carefully)
1. Sweep category by category using the Coverage Matrix below. Do not free-
   associate; walk each axis deliberately and completely.
2. For every type, list its common ALIASES and near-synonyms as a single
   entry (for example: PRD = product spec = product brief). Do not create
   duplicate entries for aliases; consolidate and note them.
3. Actively hunt the long tail: methodology-specific artifacts (Shape Up
   pitch, SAFe PI objectives, Amazon PR/FAQ and six-pager), role-specific
   artifacts (BA, QA, SRE, security, data, UX), regulated-industry artifacts
   (validation protocols, DHF, traceability matrices), and legacy/Waterfall
   artifacts that are now uncommon. Include them and flag rarity.
4. Do NOT stop when you have the obvious 20. A complete catalog is well into
   the hundreds once aliases, methodology variants, and niche artifacts are
   included. If your draft has fewer than ~150 consolidated entries, you have
   not finished; resume sweeping.
5. After the first full pass, run an explicit COMPLETENESS PASS: re-walk every
   Coverage Matrix axis and ask "what belongs here that I have not listed?"
   Add what is missing. State that you performed this pass.

COVERAGE MATRIX (sweep every axis fully)
A. SDLC phase: ideation, feasibility, initiation, requirements, design/
   architecture, planning/estimation, implementation, testing/QA, security,
   release/deployment, operations/maintenance/support, analytics/measurement,
   decommission/sunset.
B. Product lifecycle: discovery/research, strategy, definition, prioritization,
   delivery, launch/GTM, growth/experimentation, retention, post-launch
   learning, iteration, deprecation.
C. Methodology lens: Waterfall, Agile/Scrum, Kanban, Lean/Lean Startup, XP,
   SAFe and other scaled frameworks, Shape Up, Amazon working-backwards,
   design thinking, Jobs-to-be-Done, OKR-driven, dual-track.
D. Role/owner lens: product manager, product owner, program/project manager,
   business analyst, product marketing, UX/UI designer, UX researcher,
   software architect, engineering lead, individual engineer, QA/test,
   security, data/analytics, SRE/DevOps, technical writer, support/CS,
   compliance/legal, executive/stakeholder.
E. Document category: strategy/vision, market/competitive, research/discovery,
   requirements, specification, design/architecture, decision records,
   planning/roadmapping, estimation, process/ceremony artifacts, QA/test,
   release/deployment/runbooks, operations/incident, analytics/measurement,
   governance/compliance/audit, stakeholder/communication, retrospective/
   post-mortem, knowledge/enablement, legal/contractual.
F. Ceremony artifacts: the inputs and outputs of standups, sprint planning,
   backlog refinement, sprint review, retrospectives, PI planning, kickoffs,
   design reviews, architecture reviews, incident reviews.
G. Org maturity/context: startup, scale-up, enterprise, regulated (health,
   finance, gov, safety-critical), open-source project governance.

PER-ITEM SCHEMA (capture all fields; use "unknown" if not determinable)
- canonical_name
- aliases: [list of synonyms / abbreviations]
- category: (from Coverage Matrix E)
- lifecycle_phase: (SDLC and/or product phase it primarily serves)
- primary_owner_role: (from Coverage Matrix D)
- contributing_roles: [list]
- purpose: (one sentence: what decision or outcome it serves)
- typical_sections: [the headings a strong version contains]
- when_used: (the trigger or moment in the lifecycle)
- methodology_association: (or "methodology-agnostic")
- formality: (lightweight / standard / formal-auditable)
- rarity: (common / occasional / rare-or-legacy)
- relationships: (commonly precedes/follows/feeds which other docs)
- notes: (regulated-only, deprecated, regional, tooling-bound, etc.)

OUTPUT FORMAT
1. A short coverage statement confirming every Coverage Matrix axis was swept
   and the Completeness Pass was performed, with the final consolidated count.
2. The master catalog, GROUPED by category (Coverage Matrix E), each entry
   following the Per-Item Schema. Within a group, order common-to-rare.
3. An ALIAS INDEX: an alphabetical list of every alias mapping to its
   canonical_name, so nothing is lost to naming variance.
4. A GAPS-AND-UNCERTAINTIES section: types you suspect exist but could not
   confirm, ambiguous boundaries between types, and anything regional or
   industry-specific you flagged as uncertain.

QUALITY AND SOURCING
- Prefer primary and authoritative sources (standards bodies, established
  methodology sources, well-known practitioner references) over content farms.
- When a type's definition is contested or varies by source, say so briefly in
  notes rather than flattening it.
- Cite sources for non-obvious or niche artifacts.
- Do not invent artifacts. If you are unsure something is real, place it in
  GAPS-AND-UNCERTAINTIES, not the main catalog.

SCOPE BOUNDARIES
- Include: PM artifacts, SDLC artifacts, ceremony inputs/outputs, decision
  records, QA/test docs, release/ops docs, governance/compliance docs,
  research/discovery artifacts, and lightweight canvases/one-pagers.
- Exclude: pure code, marketing collateral unrelated to product process,
  generic HR/finance documents, and specific filled instances of any document.
- Edge cases (tickets, ADRs, runbooks, dashboards-as-spec): include them and
  note their lightweight or hybrid nature.

STOPPING CONDITION
Stop only when every Coverage Matrix axis has been explicitly swept, the
Completeness Pass is done, and adding more would only repeat existing entries
or their aliases. State clearly when this condition is met.
```

---

## Notes for the requester

- The output is designed to be **post-processable**: the per-item fields map onto the template library's frontmatter (`doc_type`, `phase`, `primary_owner_role`, `typical_sections`, `methodology`, `formality`, `rarity`), so you can triage which types graduate into the library first.
- A natural triage filter after the run: keep `formality: standard` and `rarity: common/occasional` for the initial library; park `rare-or-legacy` and `formal-auditable` as a later, optional family.
- If you want, the same prompt can be narrowed to a single category block to run as a focused, deeper pass (for example "QA/test artifacts only"), which tends to surface more long-tail items than one broad sweep.
