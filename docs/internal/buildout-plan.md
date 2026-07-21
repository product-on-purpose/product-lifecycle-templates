# Bundle build-out plan: the Tier-1 floor

Status: **adopted 2026-07-20 ([ADR 0021](decisions/0021-complete-the-tier-1-floor.md))**. Goal: take the library from 6 bundles to the full 27 Tier-1 "must-have" set, at the same gate-green, cited standard as the six built so far.

## What is left to build (21 types)

Six are built (prd, user-stories, acceptance-criteria, release-notes, rfc, adr). The 21 remaining, grouped into the families they form:

| Family | Types | New contract? |
|---|---|---|
| delivery-docs (extend) | definition-of-done, product-backlog, sprint-backlog | no (exists) |
| decision-docs (extend) | software-design-document | yes |
| strategy-docs | product-vision, product-strategy, business-case, okrs, product-roadmap | yes |
| qa-docs | test-plan, test-case, bug-report | yes |
| governance-docs | risk-register, raid-log, kpi-dashboard | yes |
| design-docs | wireframe, interactive-prototype | yes |
| ops-docs | runbook, incident-postmortem | yes |
| discovery-docs | user-persona | yes |
| communication-docs | status-report | yes |
| process-docs | sprint-retrospective-notes | yes |

Two notes: **governance-docs** and the standing types (definition-of-done, status-report) use `classification`, not `phase` (ADR 0015). Each **new family needs a short contract first** (on the ADR 0020 pattern) before its members pass gate check K.

## Order

1. **Finish the two existing families** - decision-docs (+SDD, the one type with an existing internal pull) and delivery-docs (+3). Cheapest and lowest-risk.
2. **strategy-docs** (5) - the biggest, highest-visibility new family.
3. **qa-docs** (3), then **governance-docs** (3) - the first real use of the `classification` axis.
4. **The rest** - design, ops, discovery, communication, process (7 types across 5 small families).

## How to build one bundle

Research first, then draft, then gate (methodology section 8):

1. Research the type across source tiers; build the research log (every source: URL, tier, retrieval status).
2. Draft the two template variants (full is a strict superset of lean).
3. Write the companion (11 sections), then derive the guide from it.
4. Work the example (fully filled, no placeholders), fill the meta (20 fields) and history.
5. Run `check-bundles.py`; fix to green; regenerate the manifest; open the PR.

Each new bundle must pass all 11 gate checks + the link and dash gates, and validate against the schema and its family contract.

## How to build many (the pipeline)

Each bundle is one run of a subagent workflow: research fan-out -> **adversarial citation check** (re-verify every cited source supports its claim - the WP-10 lesson) -> parallel drafting -> multi-lens review -> gate. Realistic pace is **1-2 bundles/day**; honest research is the bottleneck, on purpose. Every bundle gets a maintainer read before merge, because the gate proves structure, never truth.

## The policy (decided)

Building the whole floor reverses the repo's **"grow by pull, not speculation"** rule for the Tier-1 set. That call is made: [ADR 0021](decisions/0021-complete-the-tier-1-floor.md) adopts floor-completion, with grow-by-pull still governing Tier-2 and Tier-3. The one discipline kept: a bundle is never called "verified" or "complete" until a real person fills it, and STATE.md keeps coverage and real usage as separate, honest numbers.

## Start here

Build the **software-design-document** bundle end to end as the pilot (decision-docs has an existing pull and a contract-shaped sibling set). One bundle through the full pipeline calibrates the pace and review load before committing to the other twenty.
