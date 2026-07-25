---
title: "Saved Views for Dashboards Test Plan"
release_or_feature: "Saved Views for Dashboards (phases 1 and 2)"
plan_owner: "Anjali Rao (QA Lead, Reporting)"
status: "approved"
last_updated: "2026-07-06"
test_strategy_ref: "None. Acme Reporting has no standing test strategy document; the Risk-Ranked Approach below is the strategy for this release."
related:
  - "../prd/prd_example.md (Saved Views for Dashboards PRD, the scope this plan tests)"
  - "../sdd/sdd_example.md (Saved Views design, the technical surface under test)"
  - "../acceptance-criteria/acceptance-criteria_example.md (acceptance criteria for the default-view story)"
  - "../risk-register/risk-register_example.md (program risk register; R-05, R-06 and R-02 are inherited below)"
doc_type: test-plan
size: full
source_template: test-plan
source_template_version: 0.1.0
---

<!--
Worked example for the test-plan bundle: a realistic, fully filled full-variant test plan for one feature.
It chains onto the delivery-docs examples (same company, same feature, same cast) so the reader can follow
one thread from PRD through acceptance criteria into verification. Figures marked "illustrative" are made up
for the example and would be real data in a live plan.

Why the FULL variant here: this release has a formal gate inside the cycle (the security review that the PRD
makes a precondition of phase 2), three groups testing (Reporting QA, Platform, Design Systems), and a
migration whose rollback needs rehearsing. Any one of those would justify it. A single-team feature with no
gate should use the lean variant.
-->

# Saved Views for Dashboards Test Plan

## Scope and Non-Scope

**In scope.** Functional requirements FR-1 to FR-5 of the [Saved Views PRD](../prd/prd_example.md), on build
2.3.x with the `saved_views` flag enabled, covering both rollout phases: phase 1 (private views: save, list,
switch, set default, rename, delete) and phase 2 (sharing). The concrete test items are the five
`ViewsController` REST endpoints described in the [design document](../sdd/sdd_example.md), the `saved_view`
table migration and its rollback, the `default_view_id` addition to the per-user preferences record, and the
Views control in the dashboard frontend. Non-functional coverage in scope: the shared-view entitlement
boundary, view-list load performance, graceful degradation when a saved config references a deleted filter
field, and WCAG 2.2 AA keyboard and screen-reader operation of the Views control.

**Out of scope, and why.**

- **FR-6, the stale-view change indicator.** Could priority in the PRD and not built in this release. Deferred
  with the requirement; there is nothing to test.
- **The dashboard permissions service itself.** Owned and tested by Platform. This plan tests *our use of it*
  (that a shared view re-checks the recipient's access on read), not the service's own correctness.
- **Adoption.** Risk R-04 on the program register is an adoption risk, and adoption is measured after launch
  on the KPI dashboard, not verified by testing. Naming it here stops the recurring question of whether QA is
  covering it.
- **The legacy report flow.** Unchanged by this release; covered by the existing regression suite, which runs
  but is not re-planned here.

Exclusions agreed with Priya Nair (PM, Reporting) and Marcus Bell (Staff Engineer, Reporting) on 2026-07-06.

## Risk-Ranked Approach

Product risks are inherited from the [program risk register](../risk-register/risk-register_example.md) and
the PRD's own risk and non-functional tables rather than invented here, so a change in either flows into this
plan instead of diverging from it. Areas are tested in the order shown: if the window is cut short, what is
lost is the bottom of this table, by design.

| Area under test | Risk (what could go wrong, and the consequence) | Tier and why | Technique and depth | Order |
|---|---|---|---|---|
| Shared-view entitlement | A shared view embeds filter values, so a recipient without entitlement could see a segment (and the PII in it) they may not access, causing a reportable incident | **High.** Register R-05, escalated: residual 8 exceeds the program's PII appetite line of 6. Low likelihood, severe and irreversible impact | Full permission matrix: 3 personas (owner, permitted viewer, restricted viewer) x 4 filter scopes, negative cases executed first; re-check asserted on *recipient read*, not at share time, per the design; PII-in-filter scan on every share path | 1 |
| Config migration and rollback | Saved-view configs move from the legacy key-value store to the `saved_view` schema, so a silent conversion failure loses analysts' views at cutover | **High.** Register R-02. Data loss is not user-recoverable and the blast radius is every existing view | Migration dry run with count reconciliation (expect 0 mismatch); rollback rehearsal to the read-only legacy store; `config` schema version 1 validation on read of a v0 row | 2 |
| Stale-field degradation | A saved config references a filter field that no longer exists, so the dashboard fails to load instead of loading what it can | **Medium-high.** PRD reliability NFR and the design's `stale_fields` path. Moderate likelihood (fields do get removed), contained impact | Error-path testing: delete a referenced field, assert the resolvable parts load, `stale_fields` is populated, and the PRD's "some filters no longer exist" message appears with a route to re-save | 3 |
| View-list load performance | A dashboard accumulates many views, so the view list exceeds the 500ms budget and degrades the speed the program is selling | **Medium.** Register R-06, residual 6. Degrades rather than breaks | Load test at 3x the expected view count (illustrative target: 150 views on one dashboard), p95 measured separately on the view-list endpoint (register R-06 budget: under 500ms) and on view switch (PRD non-functional requirement: under 1s at p95) | 4 |
| Default-view resolution | The per-user default resolves wrongly, so a user opens someone else's view or the generic default | **Medium.** Touches the acceptance criteria directly, but failures are visible and recoverable | State and precedence cases from the [acceptance criteria](../acceptance-criteria/acceptance-criteria_example.md): setting a new default clears the previous one; a default that is a shared view the user can no longer read falls back cleanly; one user's default never changes another's | 5 |
| Accessibility of the Views control | The control is not keyboard-operable or not labeled, so the feature is unusable with assistive technology and breaches the PRD's stated WCAG 2.2 AA target | **Medium.** Certain to matter if wrong; caught late is expensive to fix | Keyboard-only traversal of the full menu, screen-reader label and state announcement (NVDA and VoiceOver), focus management on open and close | 6 |
| Rename and delete | A rename or delete fails or affects the wrong row | **Low.** Simple owner-only operations on a single row, easily observed | Equivalence partitioning only: owner and non-owner, existing and deleted row | 7 |

## Test Levels and Types

| Level or type | Owner | Environment | Why it is required (or waived) |
|---|---|---|---|
| API (system) | Anjali Rao | Staging | The four views endpoints are new in this release; the entitlement re-check is only observable here |
| End-to-end (browser) | Anjali Rao | Staging | The Views control, the default-on-open path and the stale-field message are user-visible behaviors |
| Migration and rollback | Lee Zhang (Data Eng) | Migration sandbox, then staging | Register R-02; a rollback that has never been rehearsed is not a rollback |
| Performance | Marcus Bell | Pre-prod replica | Register R-06 and the PRD's p95 targets; staging is too small to be representative |
| Security review | Sam Okafor (Security) | n/a (review, not execution) | Made a precondition of phase 2 by the PRD rollout plan; gates sharing |
| Accessibility | Sofia Marino (Design Systems) | Staging | PRD non-functional requirement: WCAG 2.2 AA |
| Unit and component | Marcus Bell | CI | Waived as a planned activity here: covered by the team's existing CI gate, which must be green as an entry criterion below |
| Localization | n/a | n/a | Waived: this release adds no user-facing copy beyond two strings already in the translation pipeline |

## Entry and Exit Criteria

**Entry criteria** (all must hold before execution starts; each would genuinely stop the work if it failed):

1. Build 2.3.1 or later deployed to staging with the `saved_views` flag enabled.
2. The CI unit and component gate is green on that build.
3. Three permission personas seeded (owner, permitted viewer, restricted viewer) and two dashboards
   provisioned, one of which carries a restricted filter field. Provided by Platform (Dana Osei).
4. The migration dry-run dataset is loaded in the migration sandbox.
5. The smoke suite passes on staging.

**Exit criteria** (all must hold before testing is called done):

1. Every High and Medium-high tier area in the Risk-Ranked Approach has its planned cases executed. Not "most
   cases": these three areas, complete.
2. The permission matrix is 100 percent executed with zero failures. This one is absolute; a single failure
   here is a suspension event, not a defect to triage.
3. Zero open Sev-1 or Sev-2 defects against in-scope requirements.
4. Migration reconciliation shows a zero-row mismatch on the dry run, and the rollback rehearsal has been
   completed once end to end.
5. p95 view switch under 1s and p95 view-list load under 500ms on the pre-prod replica at 3x expected view
   count (illustrative thresholds, taken from the PRD and the register).
6. Accessibility findings at AA level are either fixed or accepted in writing by Priya Nair.

Deliberately **not** an exit criterion: an overall pass-rate percentage. A pass rate can be raised by writing
more shallow cases and would hide a single catastrophic permission failure inside a comfortable number. Every
criterion above is a coverage, severity or threshold statement instead.

**Agreed** with Priya Nair (PM, Reporting), Marcus Bell (Staff Engineer, Reporting) and Sam Okafor (Security)
on 2026-07-06. Any change to criterion 2 or 3 requires re-agreement by all three.

## Suspension and Resumption Criteria

**Suspension.** A confirmed entitlement failure (any case in which a recipient can see data through a shared
view that they cannot see directly) suspends **all phase 2 sharing testing** immediately. Anjali Rao makes the
call and notifies Priya Nair, Marcus Bell and Sam Okafor the same day. Phase 1 (private views) testing
continues, because it does not exercise the sharing path.

Testing is also suspended, wholly, if the staging environment loses the seeded permission personas, since
every High-tier case depends on them and results produced without them would be misleading rather than merely
absent.

**Resumption.** Sharing testing resumes when: the defect is fixed and deployed; the **entire** permission
matrix is re-run from the start, not just the failing case, because an entitlement bug invalidates the
assumption behind every passing result in that matrix; and Sam Okafor confirms the security review is
unblocked. Environment loss resumes on re-seeding plus a green smoke run.

## Environment, Data, and Ownership

**Environments.** Staging on build 2.3.x with the flag enabled, reseeded nightly from an anonymized production
snapshot, for functional, end-to-end and accessibility work. A pre-prod replica sized to production for
performance, because staging carries roughly a tenth of the data (illustrative) and would produce reassuring
numbers that mean nothing. A separate migration sandbox holds a copy of the legacy key-value store for the
dry run and rollback rehearsal.

**Test data**, and this is the long-lead item:

- Three permission personas: an owner, a permitted viewer, and a restricted viewer who lacks access to one
  filter field used in a shared view. Created by Platform (Dana Osei) before entry criterion 3 can be met.
- Two dashboards, one carrying a restricted filter field, one carrying a field that will be deleted mid-cycle
  to exercise the stale-field path.
- 150 saved views on a single dashboard for the performance run (illustrative: 3x the expected ceiling).
- A legacy-store extract with 12 known-bad configs (illustrative) for migration reconciliation, including two
  that reference deleted fields.

The anonymized snapshot does **not** contain a restricted filter field by default; that is why persona data is
manufactured rather than sampled, and why it is called out as a risk to the effort below.

**Ownership.** Functional, end-to-end and the permission matrix: Anjali Rao. Migration and rollback: Lee
Zhang. Performance: Marcus Bell. Accessibility: Sofia Marino. Security review: Sam Okafor. Test data
provisioning: Dana Osei. Plan ownership and the suspension call: Anjali Rao.

## Schedule and Deliverables

**Window:** 2026-07-06 to 2026-07-17 (illustrative), aligned to the PRD's phased rollout.

| Milestone | Date | Gate |
|---|---|---|
| Entry criteria met, phase 1 execution starts | 2026-07-06 | Smoke green, personas seeded |
| Migration dry run and rollback rehearsal complete | 2026-07-09 | Zero-row reconciliation mismatch |
| Security review | 2026-07-10 | **Gates phase 2**: no sharing testing before it, per the PRD rollout plan |
| Phase 2 (sharing) execution | 2026-07-13 to 2026-07-16 | Permission matrix first |
| Performance run on pre-prod replica | 2026-07-15 | 3x view count loaded |
| Exit review and handover | 2026-07-17 | Exit criteria assessed with the three agreeing stakeholders |

**Deliverables.** Executed case results in the test tool (the tool's own "test plan" record for sprint 14, not
this document); an open-defect list with severities; a one-page test summary against the exit criteria,
delivered to the release checklist on 2026-07-17; and the migration rollback rehearsal record, which the
release checklist requires separately.

Execution status lives in the test tool, not in this plan. This document is the intent; it is revised when the
intent changes, not when a case passes.

## Risks to the Test Effort

These threaten the testing rather than the product; product risks are in the Risk-Ranked Approach above.

| Risk to the testing | Impact if it happens | Owner | Contingency and trigger |
|---|---|---|---|
| Staging is shared with the Billing migration in week 2 | Up to 3 days of blocked execution (illustrative), landing on the phase 2 window when the permission matrix runs | Dana Osei | Window booked 2026-06-29 for 13-16 July. Trigger: Billing requests the environment. Fallback: run the permission matrix against the pre-prod replica and record the environment deviation in the summary |
| The anonymized snapshot has no restricted filter field, so persona data must be manufactured | Entry criterion 3 unmet; every High-tier case blocked from day one | Dana Osei | Manufactured persona set built and verified by 2026-07-03, ahead of entry. Trigger: verification fails. Fallback: hand-built fixtures in the migration sandbox, accepting reduced realism |
| Sam Okafor is the only security reviewer and is single-threaded across two programs | The 2026-07-10 gate slips, and phase 2 cannot start; the whole sharing scope is at risk of leaving the window | Marta Reyes | Review slot confirmed in writing. Trigger: no confirmation by 2026-07-08. Fallback: escalate to the security lead for a second reviewer; if unavailable, ship phase 1 alone and re-plan phase 2 |
| The performance replica is refreshed mid-window, changing the data profile | Performance results across the window are not comparable, and R-06 stays unverified | Marcus Bell | Freeze the replica for the window. Trigger: a refresh is scheduled. Fallback: re-run the whole performance set after the refresh rather than comparing across it |

## Approvals and Change Control

| Approver | Role | What they are approving | Date |
|---|---|---|---|
| Priya Nair | PM, Reporting | Scope, the exclusions, and the exit criteria | 2026-07-06 |
| Marcus Bell | Staff Engineer, Reporting | Technical scope, environments, and the entry criteria | 2026-07-06 |
| Sam Okafor | Security | The entitlement approach, the suspension rule, and the phase 2 gate | 2026-07-06 |
| Marta Reyes | Program Manager | Schedule, and the contingencies for risks to the effort | 2026-07-06 |

**Change control.** Edits to wording, dates within the agreed window, and additions to the test data list are
made in place by the plan owner and noted in the version history. The following require re-approval by the
named approver before they take effect: any change to the in-scope requirement list or the exclusions (Priya
Nair); any relaxation of exit criteria 2 or 3 (all three signatories to the criteria); any change to the
suspension rule or the phase 2 gate (Sam Okafor). A change made without the required re-approval leaves the
plan unapproved until it is obtained, and the release checklist treats an unapproved plan as a blocker.
