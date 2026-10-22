---
status: accepted
date: 2026-10-15
decision-makers: [jprisant]
consulted: [claude]
---

# `analytics-requirements-measurement-plan` does not ship as a per-feature type: its content already ships in the PRD

## TL;DR

- **Decision:** `analytics-requirements-measurement-plan` **does not ship**, in the per-feature shape the
  catalog describes. The maintainer declined it on 2026-10-15, decision 11 of a decision sitting, in the
  shape of [ADR 0064 (deployment-plan is declined)](0064-deployment-plan-is-declined.md).
- **This is not a zero-source refusal**, unlike [ADR 0049 (pi-release
  retrospective)](0049-pi-release-retrospective-fails-the-admission-test.md). Two named sources publish a
  "measurement plan" as a written document: Google's Analytics Help Center and Avinash Kaushik's Digital
  Marketing and Measurement Model. Each is scoped to a whole business, site, or store, never to one
  product feature.
- **The decision rests on two grounds.** Ground (a), the real one: [ADR 0067
  (tracking-plan)](0067-tracking-plan-joins-governance-docs-as-a-sixth-member.md) already reads the
  per-feature content as shipping inside the PRD. That is this library's own position, not a sourced
  fact. Ground (b), supporting: no named source publishes the per-feature document. The nearest miss is
  Google's own HEART paper, a process with no document.
- **The business-scope reading clears admission, and this record leaves it unswept**, uncompared with
  `north-star-metrics`, `kpi-dashboard`, or `tracking-plan`. **The decline does not rest on Wizbrand**:
  its page describes a standing, quarterly-reviewed plan, not a per-feature one.
- **Status:** accepted 2026-10-15, on the maintainer's delegation. The decision itself is the maintainer's
  own answer to decision 11 of that day's sitting. This record's text was offered for a read, and the
  maintainer replied with a wrap instruction that delegated the remaining merges to the agent's best
  judgment. That direction stands in for the read, as a similar one did for [ADR 0070
  (north-star-metrics)](0070-north-star-metrics-joins-strategy-docs-as-a-fifth-member.md). This record
  amends no family contract, so the standing stop for a contract read does not apply.
  **Confirmed by the maintainer on 2026-10-21**, in one batch covering ADRs 0070, 0074,
  0075, 0076 and 0078. Offered the choice to confirm all five, to reopen any of them for a read, or
  to leave the question parked, the maintainer confirmed all five.

## Context and Problem Statement

The catalog lists `analytics-requirements-measurement-plan` as a Tier-2 candidate, catalog row 147. Its
purpose line reads "Define how a feature's success will be measured" (`docs/internal/catalog.md` line 214;
`atlas/catalog-data.json`). Its aliases are "measurement framework" and "success metrics doc". GitHub
issue #262 (bundle: analytics-requirements-measurement-plan) tracks it as a build candidate.

A research pass on 2026-10-14 tested the type against [ADR 0030 (templating scope, Markdown
documents)](0030-templating-scope-markdown-documents.md)'s admission test, as one of four candidates in an
admission sweep. It found a split result. The per-feature document the catalog describes clears on no
named source. A different, business-scope reading of the same name clears comfortably on two sources.

On 2026-10-15 the maintainer answered decision 11 of a decision sitting with "Decline the per-feature
type." The decision was titled "Decline the per-feature analytics measurement plan, in the ADR 0064
shape", and the chosen option read "A decline record. The catalog row stays a candidate, as with ADR 0064
and ADR 0065." The second is [ADR 0065 (steering committee pack is
declined)](0065-steering-committee-pack-is-declined.md). This record is that decline, argued on the
ground the research actually found, not as a zero-source refusal.

## Decision Drivers

- **A decline must be argued on the ground it actually rests on.** A zero-source refusal would misstate
  the finding, since a different reading of the same name clears admission on its own.
- **Admission and the build decision are separate questions**, as ADR 0064 established.

## Considered Options

1. **Decline on duplication, with the admission split named honestly.** Chosen.
2. **A zero-source refusal, in ADR 0049's shape.** Rejected. It would misstate a result: a different
   reading of the same name clears admission on two sources.
3. **Build the business-scope reading as its own type.** Not decided here: it has not been compared with
   `north-star-metrics`, `kpi-dashboard`, or `tracking-plan`.
4. **Defer the whole question.** Rejected. The maintainer already ruled at the 2026-10-15 sitting.

## Decision Outcome

**Chosen: option 1.**

### The per-feature type does not clear admission

Google's Analytics Help Center publishes a "measurement plan" at business scope: "A measurement plan is a
way for you to align your business objectives with your Google Analytics configuration settings"
([support.google.com](https://support.google.com/analytics/answer/7165633)). Its worked example describes
a whole store: "At the top of their measurement plan is the main objective of the store"
([support.google.com](https://support.google.com/analytics/answer/6224341)). Avinash Kaushik's Digital
Marketing and Measurement Model names a "Measurement contract"
([kaushik.net](https://www.kaushik.net/avinash/digital-marketing-and-measurement-model/)). Neither source
ties the plan to one product feature.

The nearest miss is a framework paper, not a document. Google's own HEART paper, by Rodden, Hutchinson
and Fu at CHI 2010, states: "We developed a simple process that steps teams through articulating the
goals of a product or feature, then identifying signals that indicate success, and finally building
specific metrics to track on a dashboard" ([research.google.com](https://research.google.com/pubs/archive/36299.pdf)).
It describes a process, not a document.

The most literal "Measurement Plan Template" the sweep found ships in the `aiwg` npm package, and its
authorship is unconfirmed. It names "Document Owner: Project Manager", and the sweep read it as a
standing plan rather than a per-feature one. This record does not rely on it. A gap-fill search for a
per-feature document found none.

### Ground (a): the content already ships inside the PRD, this library's own position

ADR 0067 already read this exact catalog row this way: "A per-feature plan is a different catalog
candidate, `analytics-requirements-measurement-plan`, and its content already ships inside the PRD's
"Analytics and instrumentation" section" (ADR 0067, lines 74 to 76). The shipped PRD carries both
"## Success metrics" (`templates/prd/prd_template-full.md` line 192) and "## Analytics and
instrumentation" (line 209). The catalog row allows this reading too: its relationships column reads
"section of PRD or standalone" (`docs/internal/catalog.md` line 214).

**This is this library's own position, not a sourced claim.** No source read in this sweep, or for ADR
0067, addresses that boundary directly. The question is whether a per-feature measurement document and a
PRD section hold the same content under two names. The answer here rests on this library's own judgment.

Family fit was not the deciding question, and this record does not test it. ADR 0067 considered
`delivery-docs` for a per-feature instrumentation plan and set it aside on this same ground: the content
ships in the PRD.

### The business-scope reading clears admission, and stays unswept

Two named sources, quoted above, publish a measurement plan at business, site, or store scope. That
reading of the same catalog name clears ADR 0030's admission test on its own, as a different candidate
from the one this record declines.

Nobody has compared it against `north-star-metrics`, `kpi-dashboard`, or `tracking-plan`, the three
standing instruments it would need a boundary with. This record does not run that comparison, and does
not decide the business-scope reading. It names the gap so a later pass starts from evidence.

### The decline does not rest on Wizbrand

Wizbrand's own page describes a standing, periodically revisited plan: "Many teams review it quarterly"
([wizbrand.com](https://www.wizbrand.com/tutorials/analytics-measurement-plan/)). That is not a per-feature
document, so this record does not count it as support. A dated note of 2026-10-15 on the `tracking-plan`
spec in [`tier2-specs.md`](../tier2-specs.md) already corrects the same misreading.

### Consequences

**Good.**

- **The record states both grounds honestly.** The per-feature document fails admission on its own, and
  this library separately reads its content as shipping inside the PRD. Neither ground stands in for the
  other.
- **The business-scope reading is named and sourced.** A later decision to build it can start from
  evidence, not from nothing.

**Bad, and stated plainly.**

- **A team searching this catalog for a standalone "measurement framework" or "success metrics doc" finds
  nothing here.** Both aliases name a declined type.
- **The catalog row stays `candidate` and carries no state override**, following ADR 0064 and ADR 0065.
  The `out-of-scope` value is for a refusal about the medium, and `gen-atlas.py` forces `state_note` to
  empty for any candidate. The decline is discoverable only through this record and GitHub issue #262.

### What would reopen this, stated so it is falsifiable

1. **A named source publishes a per-feature measurement document** with fixed headings. It must be
   distinct from the HEART paper's process description and from a standing, organization-level plan.
2. **The maintainer runs the business-scope comparison** against `north-star-metrics`, `kpi-dashboard`,
   and `tracking-plan`, then decides whether to build it.
3. **A real team asks for the standalone per-feature document** the PRD section does not serve. A
   documented request is evidence a web search cannot produce.

## More Information

- The research: the admission sweep of 2026-10-14 over four candidates, recorded in
  [`tier2-specs.md`](../tier2-specs.md); the decision: decision 11 of the 2026-10-15 sitting, on the
  candidate at GitHub issue #262.
- Related records: [ADR 0030 (templating scope)](0030-templating-scope-markdown-documents.md), [ADR 0049
  (pi-release retrospective)](0049-pi-release-retrospective-fails-the-admission-test.md), [ADR 0064
  (deployment-plan is declined)](0064-deployment-plan-is-declined.md), [ADR 0065 (steering committee
  pack is declined)](0065-steering-committee-pack-is-declined.md), and [ADR 0067
  (tracking-plan)](0067-tracking-plan-joins-governance-docs-as-a-sixth-member.md).
