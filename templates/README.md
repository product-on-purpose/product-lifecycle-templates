---
title: "Template bundles"
---

# Template bundles

One directory per document type. **A bundle is a folder, not a file**: the blank template in each
variant it ships, a worked example, a short operator guide with a self-grade rubric, a deep companion,
the research log every claim in it traces to, and machine-readable metadata. What each file is for is
in [`methodology.md`](methodology.md); how to fill one is in
[`docs/how-to/filling-a-template.md`](../docs/how-to/filling-a-template.md); and
[`docs/reference/choosing-a-template.md`](../docs/reference/choosing-a-template.md) turns a job to be
done into a bundle name.

Bundles are grouped into **families**, and each family has a ratified contract under
[`docs/internal/contracts/`](../docs/internal/contracts) that binds every member. Gate check K reads
the contract and fails a member that drifts from it, which is why a family contract is written before
its members are built.

**A bundle declares exactly one taxonomy axis**, never both: a lifecycle `phase` for documents authored
at a stage and then finished, or a standing `classification` for documents that are maintained rather
than completed. That either-or is the rule
[ADR 0015 (the second taxonomy axis)](../docs/internal/decisions/0015-second-taxonomy-axis-phase-xor-classification.md)
settled, and gate check J enforces it.

The table below is generated from each bundle's own `*_meta.yaml`, so no column here can drift from the
tree without the gate noticing.

## Inventory

**`communication-docs`**

- [`status-report/`](status-report/) - Status Report. Axis classification utility; ships lean/full.

**`decision-docs`**

- [`adr/`](adr/) - Architecture Decision Record. Axis phase develop; ships lean/full.
- [`rfc/`](rfc/) - Request for Comments. Axis phase develop; ships lean/full.
- [`sdd/`](sdd/) - Software Design Document. Axis phase develop; ships lean/full.

**`delivery-docs`**

- [`acceptance-criteria/`](acceptance-criteria/) - Acceptance Criteria. Axis phase deliver; ships lean/full.
- [`prd/`](prd/) - Product Requirements Document. Axis phase deliver; ships lean/full.
- [`product-backlog/`](product-backlog/) - Product Backlog. Axis phase deliver; ships lean/full.
- [`release-notes/`](release-notes/) - Release Notes. Axis phase deliver; ships lean/full.
- [`sprint-backlog/`](sprint-backlog/) - Sprint Backlog. Axis phase deliver; ships lean/full.
- [`user-stories/`](user-stories/) - User Story. Axis phase deliver; ships lean/full.

**`discovery-docs`**

- [`business-case/`](business-case/) - Business Case. Axis phase discover; ships lean/full.
- [`user-persona/`](user-persona/) - User Persona. Axis phase discover; ships lean/full.

**`governance-docs`**

- [`kpi-dashboard/`](kpi-dashboard/) - KPI Dashboard. Axis classification utility; ships lean/full.
- [`raid-log/`](raid-log/) - RAID Log. Axis classification utility; ships lean/full.
- [`risk-register/`](risk-register/) - Risk Register. Axis classification utility; ships lean/full.

**`process-docs`**

- [`incident-postmortem/`](incident-postmortem/) - Incident Postmortem. Axis phase iterate; ships lean/full.
- [`sprint-retrospective-notes/`](sprint-retrospective-notes/) - Sprint Retrospective Notes. Axis phase iterate; ships lean.

**`qa-docs`**

- [`bug-report/`](bug-report/) - Bug Report. Axis phase develop; ships lean/full.
- [`test-case/`](test-case/) - Test Case. Axis phase develop; ships lean/full.
- [`test-plan/`](test-plan/) - Test Plan. Axis phase develop; ships lean/full.

**`standing-standards`**

- [`definition-of-done/`](definition-of-done/) - Definition of Done. Axis classification foundation; ships lean/full.
- [`runbook/`](runbook/) - Runbook. Axis classification tool; ships lean/full.

**`strategy-docs`**

- [`okrs/`](okrs/) - OKRs. Axis classification utility; ships lean/full.
- [`product-roadmap/`](product-roadmap/) - Product Roadmap. Axis classification utility; ships lean/full.
- [`product-strategy/`](product-strategy/) - Product Strategy. Axis classification foundation; ships lean/full.
- [`product-vision/`](product-vision/) - Product Vision. Axis classification foundation; ships lean/full.

**Not a bundle**

- [`methodology.md`](methodology.md) - the authoring methodology every bundle is built against
- [`_working/`](_working/) - retained drafting artifacts from the guidance-style decision, kept because
  [ADR 0006 (guidance style, approach A)](../docs/internal/decisions/0006-guidance-style-approach-a.md)
  cites them as the options it chose between
