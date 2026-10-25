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
- [`spike-report/`](spike-report/) - Spike / Research Spike report. Axis phase develop; ships lean. The fourth `decision-docs` member: it INVESTIGATES the question an RFC proposes, an ADR records, and an SDD designs against.
- [`trade-study/`](trade-study/) - Trade Study / Options Analysis. Axis phase develop; ships lean/full. The fifth `decision-docs` member, admitted with no contract change under [ADR 0022](../docs/internal/decisions/0022-adopt-decision-docs-family-contract.md): it EVALUATES named technical alternatives against weighted criteria and recommends one, feeding the decision an ADR records.

**`delivery-docs`**

- [`acceptance-criteria/`](acceptance-criteria/) - Acceptance Criteria. Axis phase deliver; ships lean/full.
- [`announcement-internal-comms/`](announcement-internal-comms/) - Announcement / Internal Comms. Axis phase deliver; ships lean. The eighth `delivery-docs` member ([ADR 0059](../docs/internal/decisions/0059-announcement-internal-comms-joins-delivery-docs.md)): the internal announcement of a product launch or change - what it means for people who did not do the work, and what they must do.
- [`change-request/`](change-request/) - Change Request. Axis phase deliver; ships lean/full. The ninth `delivery-docs` member ([ADR 0060](../docs/internal/decisions/0060-change-request-joins-delivery-docs.md)): a formal request to alter an agreed baseline (scope, requirements, schedule, cost), and the decision on it.
- [`epic/`](epic/) - Epic. Axis phase deliver; ships lean/full.
- [`prd/`](prd/) - Product Requirements Document. Axis phase deliver; ships lean/full.
- [`product-backlog/`](product-backlog/) - Product Backlog. Axis phase deliver; ships lean/full.
- [`release-notes/`](release-notes/) - Release Notes. Axis phase deliver; ships lean/full.
- [`sprint-backlog/`](sprint-backlog/) - Sprint Backlog. Axis phase deliver; ships lean/full.
- [`use-case-specification/`](use-case-specification/) - Use Case Specification. Axis phase deliver; ships lean/full. The tenth `delivery-docs` member ([ADR 0072](../docs/internal/decisions/0072-use-case-specification-joins-delivery-docs.md)): one primary actor's full path to one goal, a numbered main success scenario plus the alternative and exception paths that branch off it. It elaborates one story the chain already names, before acceptance criteria confirm it.
- [`user-stories/`](user-stories/) - User Story. Axis phase deliver; ships lean/full.

**`discovery-docs`**

- [`business-case/`](business-case/) - Business Case. Axis phase discover; ships lean/full.
- [`user-persona/`](user-persona/) - User Persona. Axis phase discover; ships lean/full.
- [`project-brief/`](project-brief/) - Project Brief. Axis phase discover; ships lean/full. The third `discovery-docs` member ([ADR 0063](../docs/internal/decisions/0063-project-brief-reopens-discovery-docs.md)): the request for authority to start finding out whether and how to proceed.
- [`problem-statement/`](problem-statement/) - Problem Statement. Axis phase define; ships lean/full. The fourth `discovery-docs` member and the library's first `phase: define` bundle ([ADR 0069](../docs/internal/decisions/0069-problem-statement-joins-discovery-docs.md)): which problem is worth solving, who has it, and the evidence that it is real, before anyone names a solution.
- [`design-brief/`](design-brief/) - Design Brief. Axis phase define; ships lean/full. The fifth `discovery-docs` member and the library's second `phase: define` bundle ([ADR 0079](../docs/internal/decisions/0079-design-brief-joins-discovery-docs-at-define.md)): the chosen problem and the one concept chosen for design, handed to the people who will design it, before anyone specifies how that concept works.

**`experimentation-docs`**

- [`experiment-design-doc/`](experiment-design-doc/) - Experiment Design Doc. Axis phase measure; ships lean/full. The first `experimentation-docs` member ([ADR 0066](../docs/internal/decisions/0066-adopt-experimentation-docs-family-contract.md)): the plan for one experiment, fixed before it runs, which the family's second member, the readout, reports against.
- [`experiment-readout/`](experiment-readout/) - Experiment Readout. Axis phase measure; ships lean/full. The second `experimentation-docs` member, which completes the family ([ADR 0066](../docs/internal/decisions/0066-adopt-experimentation-docs-family-contract.md)): what one experiment found, read against the plan and decision rule its design doc fixed in advance, and the ship, iterate or stop decision that followed.

**`governance-docs`**

- [`kpi-dashboard/`](kpi-dashboard/) - KPI Dashboard. Axis classification utility; ships lean/full.
- [`raid-log/`](raid-log/) - RAID Log. Axis classification utility; ships lean/full.
- [`risk-register/`](risk-register/) - Risk Register. Axis classification utility; ships lean/full.
- [`issue-log/`](issue-log/) - Issue Log. Axis classification utility; ships lean/full. The fourth `governance-docs` member ([ADR 0057](../docs/internal/decisions/0057-issue-log-joins-governance-docs-as-a-fourth-member.md)): the deepened, standalone form of the RAID log's Issues quadrant, as the risk register is of its Risks.
- [`change-log/`](change-log/) - Change Log. Axis classification utility; ships lean/full. The fifth `governance-docs` member ([ADR 0061](../docs/internal/decisions/0061-change-log-joins-governance-docs-as-a-fifth-member.md)): the standing register behind the per-occasion change request, one row per request with its decision kept apart from its status.
- [`tracking-plan/`](tracking-plan/) - Tracking Plan. Axis classification utility; ships lean/full. The sixth `governance-docs` member ([ADR 0067](../docs/internal/decisions/0067-tracking-plan-joins-governance-docs-as-a-sixth-member.md)): the standing, product-wide plan of which events and properties a product records and why, upstream of the KPI dashboard's metrics.
- [`data-dictionary/`](data-dictionary/) - Data Dictionary. Axis classification utility; ships lean/full. The seventh `governance-docs` member ([ADR 0073](../docs/internal/decisions/0073-data-dictionary-joins-governance-docs-as-a-seventh-member.md)): the standing reference to what the fields of a dataset or table mean, so that different teams compute the same number from them. It documents fields, while the tracking plan specifies events and the KPI dashboard locks metric formulas.

**`process-docs`**

- [`incident-postmortem/`](incident-postmortem/) - Incident Postmortem. Axis phase iterate; ships lean/full.
- [`sprint-retrospective-notes/`](sprint-retrospective-notes/) - Sprint Retrospective Notes. Axis phase iterate; ships lean.
- [`project-milestone-retrospective/`](project-milestone-retrospective/) - Project / Milestone Retrospective. Axis phase iterate; ships lean/full. Looks back on work that has **ended**, where the team may disperse and part of the audience was not there - as against the sprint retrospective's cadence and the incident postmortem's trigger.

**`qa-docs`**

- [`bug-report/`](bug-report/) - Bug Report. Axis phase develop; ships lean/full.
- [`test-case/`](test-case/) - Test Case. Axis phase develop; ships lean/full.
- [`test-summary-report/`](test-summary-report/) - Test Report / Test Summary Report. Axis phase develop; ships lean/full. The fourth `qa-docs` member ([ADR 0050](../docs/internal/decisions/0050-qa-docs-admits-a-fourth-member.md)): it reports the verification as a whole, closing the chain the plan opens and the bug report interrupts.
- [`test-plan/`](test-plan/) - Test Plan. Axis phase develop; ships lean/full.

**`research-docs`**

- [`user-research-plan/`](user-research-plan/) - User Research Plan. Axis phase discover; ships lean/full. The first `research-docs` member ([ADR 0081](../docs/internal/decisions/0081-adopt-research-docs-family-contract.md)): the plan for one study of the people a product serves, written before it runs, with the tasks and the measures when the study is a usability test.

**`standing-standards`**

- [`definition-of-done/`](definition-of-done/) - Definition of Done. Axis classification foundation; ships lean/full.
- [`runbook/`](runbook/) - Runbook. Axis classification tool; ships lean/full.
- [`launch-coordination-checklist/`](launch-coordination-checklist/) - Launch Coordination Checklist. Axis classification tool; ships lean/full.
- [`definition-of-ready/`](definition-of-ready/) - Definition of Ready. Axis classification foundation; ships lean. The fourth `standing-standards` member ([ADR 0058](../docs/internal/decisions/0058-definition-of-ready-joins-standing-standards-as-a-foundation.md)): a team's agreement on when a backlog item is ready to pull into a sprint, the entry-side mirror of the Definition of Done.
- [`production-readiness-review/`](production-readiness-review/) - Production Readiness Review. Axis classification tool; ships lean/full. The fifth `standing-standards` member ([ADR 0062](../docs/internal/decisions/0062-production-readiness-review-joins-standing-standards-as-a-tool.md)): the standing checklist a service is reviewed against before the team that will carry its pager takes it on. It checks that a runbook exists rather than producing one.
- [`test-strategy/`](test-strategy/) - Test Strategy. Axis classification foundation; ships lean. The seventh `standing-standards` member ([ADR 0075](../docs/internal/decisions/0075-test-strategy-joins-standing-standards-as-a-foundation.md)): the standing document that sets the default testing approach for every project inside one organization or program, which each project's own test plan either follows or states a reasoned deviation from.

**`strategy-docs`**

- [`okrs/`](okrs/) - OKRs. Axis classification utility; ships lean/full.
- [`product-roadmap/`](product-roadmap/) - Product Roadmap. Axis classification utility; ships lean/full.
- [`product-strategy/`](product-strategy/) - Product Strategy. Axis classification foundation; ships lean/full.
- [`product-vision/`](product-vision/) - Product Vision. Axis classification foundation; ships lean/full.
- [`north-star-metrics/`](north-star-metrics/) - North Star Metric. Axis classification foundation; ships lean/full. The fifth `strategy-docs` member ([ADR 0070](../docs/internal/decisions/0070-north-star-metrics-joins-strategy-docs-as-a-fifth-member.md)): the one metric that shows customers get the value the strategy promises, and the input metrics a team can move.
- [`positioning-statement/`](positioning-statement/) - Positioning Statement. Axis classification foundation; ships lean. The sixth `strategy-docs` member ([ADR 0076](../docs/internal/decisions/0076-positioning-statement-joins-strategy-docs-as-a-sixth-member.md)): the internal, present-tense record of how this product stands against a named alternative, for a specific target customer, now.
- [`business-continuity-plan/`](business-continuity-plan/) - Business Continuity Plan. Axis classification tool; ships lean/full. The sixth `standing-standards` member ([ADR 0071](../docs/internal/decisions/0071-business-continuity-plan-joins-standing-standards-as-a-tool.md)): the standing plan that keeps critical business processes going through a significant disruption. Lean points to a separate disaster recovery plan; full carries Disaster Recovery as its own section.

**Not a bundle**

- [`methodology.md`](methodology.md) - the authoring methodology every bundle is built against
- [`_working/`](_working/) - retained drafting artifacts from the guidance-style decision, kept because
  [ADR 0006 (guidance style, approach A)](../docs/internal/decisions/0006-guidance-style-approach-a.md)
  cites them as the options it chose between
