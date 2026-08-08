---
title: "Choosing a template"
description: "Every shipped bundle listed by the job it does, so a need resolves to one bundle name"
audience: "both"
level: "beginner"
tags:
  - reference
  - catalog
  - selection
---

# Choosing a template

This library ships 26 governed document bundles, one per document type, organized under
`templates/`. Each bundle is a folder, not a single file: a blank template, a deep companion,
a short operator guide, a worked example, and machine metadata. See
[`README.md`](../../README.md) for what a bundle contains and why.

This page exists to answer a narrower question: **which bundle, if any, matches the job you
have in front of you right now.** It is organized by what you are trying to do, not by the
library's internal grouping. If you already know the library's family structure, skip to
[The family map](#the-family-map).

## Start with what you are doing

### I am deciding whether to build something

Before anything is scoped or scheduled, this is where you find out whether the investment is
worth making and who it is for.

- [`business-case`](../../templates/business-case/) - whether an investment is worth making, and
  what it is being compared against, including doing nothing.
- [`user-persona`](../../templates/user-persona/) - who you are building for, grounded in research
  rather than imagination, with the evidence tier stated on the document.

### I am defining what to build

Two different altitudes live here. Direction comes first, then the specific thing.

- [`product-vision`](../../templates/product-vision/) - the future this product is trying to
  create, and what that rules out.
- [`product-strategy`](../../templates/product-strategy/) - which problems this product will solve
  to get there, and which it will not.
- [`prd`](../../templates/prd/) - what to build, for whom, and why, for one initiative.
- [`user-stories`](../../templates/user-stories/) - user-centered stories that anchor work to user
  value.
- [`acceptance-criteria`](../../templates/acceptance-criteria/) - the conditions that confirm a
  story is done.

### I am planning work

- [`product-roadmap`](../../templates/product-roadmap/) - in what order problems get solved, and
  how certain that is at each horizon.
- [`okrs`](../../templates/okrs/) - what measurable change a team expects this period, and whether
  it got it.
- [`product-backlog`](../../templates/product-backlog/) - the ordered, goal-anchored list of work
  the team draws from.
- [`sprint-backlog`](../../templates/sprint-backlog/) - one sprint's forecast of work, drawn from
  the product backlog.

If what you are tracking is risk or open items rather than scheduling delivery, that is a
different family: see `governance-docs` in [the family map](#the-family-map) below.

### I am checking quality

- [`test-plan`](../../templates/test-plan/) - what is being tested and what is not, ranked by risk,
  with criteria someone can check.
- [`test-case`](../../templates/test-case/) - the specification of one verification, written so a
  stranger gets the same answer tomorrow.
- [`bug-report`](../../templates/bug-report/) - one anomaly, reproducible by the reader, with
  severity and priority kept apart.

### I am recording a decision

Three distinct jobs, kept deliberately separate: a proposal, a record, and a design.

- [`rfc`](../../templates/rfc/) - the proposal circulated before a decision, to gather input.
- [`adr`](../../templates/adr/) - the record of a decision after it is made, in
  [MADR v4](https://github.com/adr/madr).
- [`sdd`](../../templates/sdd/) - the software design document: how a system will be built, before
  the code.

If what you are recording is a standard the team agrees on once and then applies every time,
rather than a one-off decision, that is `standing-standards`, not this family. See
[the family map](#the-family-map).

### I am looking back at what happened

- [`sprint-retrospective-notes`](../../templates/sprint-retrospective-notes/) - the written record
  that turns a retrospective discussion into one owned, dated change.
- [`incident-postmortem`](../../templates/incident-postmortem/) - the learning document written
  after one event, whose trigger is a criterion the team published in advance.

### I am telling someone else what is going on

- [`status-report`](../../templates/status-report/) - the periodic report that narrates what
  happened against metrics defined elsewhere, and invents no figure of its own.
- [`release-notes`](../../templates/release-notes/) - the customer-facing announcement of a
  release.

### Two families sit outside this list, on purpose

`governance-docs` and `standing-standards` are not tied to a single moment in the list above,
because that is what makes them different in kind. Governance documents (risk register, RAID
log, KPI dashboard) are maintained continuously across the whole lifecycle rather than authored
once at a stage. Standing standards (definition of done, runbook) are agreed once and then
consulted, not rewritten, every time the situation recurs. Both are real, gate-green bundles;
they just do not fit a "right now I am doing X" frame. Find them in the family map below.

<p align="right">(<a href="#choosing-a-template">back to top</a>)</p>

---

## The family map

The library groups its bundles into families. This is the library's own organizing structure,
included here for readers who want the complete picture rather than a situational shortcut.

| Family | What it is for | Bundles |
|---|---|---|
| `delivery-docs` | Turns an idea into shipped work, PRD through release note | [`prd`](../../templates/prd/), [`user-stories`](../../templates/user-stories/), [`product-backlog`](../../templates/product-backlog/), [`sprint-backlog`](../../templates/sprint-backlog/), [`acceptance-criteria`](../../templates/acceptance-criteria/), [`release-notes`](../../templates/release-notes/) |
| `strategy-docs` | Sets direction: where the product is going, which problems it solves first, and what counts as progress | [`product-vision`](../../templates/product-vision/), [`product-strategy`](../../templates/product-strategy/), [`product-roadmap`](../../templates/product-roadmap/), [`okrs`](../../templates/okrs/) |
| `decision-docs` | Proposes, records, and designs against a decision, as three separate jobs | [`rfc`](../../templates/rfc/), [`adr`](../../templates/adr/), [`sdd`](../../templates/sdd/) |
| `governance-docs` | Standing instruments a PM maintains across the whole lifecycle: risk, open items, and whether objectives are being met | [`risk-register`](../../templates/risk-register/), [`raid-log`](../../templates/raid-log/), [`kpi-dashboard`](../../templates/kpi-dashboard/) |
| `qa-docs` | Verifies the work: what to test, one verification's specification, and one confirmed defect | [`test-plan`](../../templates/test-plan/), [`test-case`](../../templates/test-case/), [`bug-report`](../../templates/bug-report/) |
| `discovery-docs` | Runs before the decision to build, to test whether an investment is worth making and who it is for | [`business-case`](../../templates/business-case/), [`user-persona`](../../templates/user-persona/) |
| `standing-standards` | Agreed once, applied every time, without being rewritten on a calendar | [`definition-of-done`](../../templates/definition-of-done/), [`runbook`](../../templates/runbook/) |
| `process-docs` | Looks back at what happened and commits to what changes next, on a cadence or after one event | [`sprint-retrospective-notes`](../../templates/sprint-retrospective-notes/), [`incident-postmortem`](../../templates/incident-postmortem/) |
| `communication-docs` | Reports status to someone else, sourcing every number from elsewhere rather than inventing one | [`status-report`](../../templates/status-report/) |

<!-- counts: bundles=26 -->
That is 26 bundles across every family the library currently ships, and every family is
complete: nothing in the list above is a partially built stub. See
[`README.md`](../../README.md#what-is-in-the-library-today) for what "complete" means here, and
what it does not mean.

<p align="right">(<a href="#choosing-a-template">back to top</a>)</p>

---

## When nothing above fits

Say this plainly, because it is true and it matters more than anything else on this page: **the
library covers a 205-type catalog of product and software-lifecycle artifacts, researched and
recorded in [`docs/internal/catalog.md`](../internal/catalog.md), and only a fraction of that
catalog is built.**

<!-- counts: tier1=25 -->
What is built is the Tier-1 floor: the types the catalog itself flags as must-have. All 25 of
the catalog's templatable Tier-1 types are now built (two catalog Tier-1 types, `wireframe` and
`interactive-prototype`, are out of scope for this library on purpose, because they are not
Markdown documents; see
[ADR 0021](../internal/decisions/0021-complete-the-tier-1-floor.md) and
[ADR 0030](../internal/decisions/0030-templating-scope-markdown-documents.md)). The 26th bundle,
`rfc`, is a Tier-2 type built early because `decision-docs` needed it to read as a complete
family.

Everything past that floor, the other roughly nine in ten catalog types, is not built. That is
not an oversight the library is embarrassed by; it is a stated growth rule. Tier-2 and Tier-3
types are built **by pull**: when a real team asks for one, not speculatively ahead of demand.
So if the document type you need is not in the [family map](#the-family-map) above, the honest
answer is often **nothing here yet**, and that is expected, not a bug in this page.

Two ways to check further before concluding that:

1. **Browse the whole catalog.** [`atlas/atlas.html`](../../atlas/atlas.html) is a self-contained,
   interactive map of all 205 catalog types, filterable by category, lifecycle phase, tier, and
   whether it is built. Open it in any browser. It will tell you plainly whether your type
   exists in the research and, if so, whether it has been templated yet.
2. **If you are an agent, not a person, read the manifest instead of this page.**
   [`manifest.json`](../../manifest.json) is the machine-readable catalog of every built bundle's
   selectable fields (phase or classification, family, tags, sizes, aliases). It exists
   specifically so an agent can select a bundle programmatically rather than parsing prose like
   this document, and it is regenerated and freshness-checked by the library's gate, so it
   never drifts from the tree the way hand-written prose can.

If your type genuinely is not built yet, the library has no mechanism today for requesting it
beyond opening an issue against the repository; there is no in-product request queue.

<p align="right">(<a href="#choosing-a-template">back to top</a>)</p>
