---
title: "Restricted viewer opening a shared view receives only entitled rows"
case_id: "TC-047"
verifies: "Test plan risk R-05 (shared-view entitlement). No acceptance criterion covers this case."
priority: "P1"
case_status: "active"
case_version: "1.1"
last_updated: "2026-07-08"
related:
  - "../test-plan/test-plan_example.md (Saved Views test plan; this case is in Risk-Ranked Approach row 1)"
  - "../sdd/sdd_example.md (Saved Views design; the entitlement re-check happens on recipient read)"
  - "../acceptance-criteria/acceptance-criteria_example.md (the agreed criteria, which do not cover this case)"
doc_type: test-case
size: full
source_template: test-case
source_template_version: 0.1.0
---

<!--
Worked example for the test-case bundle: a full-variant case for one verification, continuing the Acme
Analytics "Saved Views" thread used across the delivery-docs and qa-docs families. Figures marked
"illustrative" are made up for the example.

WHY THIS CASE WAS CHOSEN, and it is not because it is typical. It is the clearest available demonstration of
the companion's section 6 argument: this case traces to a High-tier risk in the test plan and to NO acceptance
criterion. Nobody agreed to it, because nobody thought of it. That is what "test design continues past the
agreed criteria" means in practice.

WHY THE FULL VARIANT: the case is security-relevant and was reviewed before it ran, it is partly automated
with a stated gap, and it sits behind a formal gate in the test plan. A routine case on this feature would use
the lean variant.
-->

# TC-047: Restricted viewer opening a shared view receives only entitled rows

## Identification and Traceability

Verifies that when a user opens a saved view shared with them, they receive only the rows their own
entitlements permit, including inside aggregate values, and never the rows the view's owner can see.

**Traces to:** risk **R-05** in the [Saved Views test plan](../test-plan/test-plan_example.md), the highest
tier in its Risk-Ranked Approach, which inherits from the program risk register: a shared view embeds filter
values, so a recipient without entitlement could see a segment and the personal data in it.

**Traces to no acceptance criterion, and that is deliberate.** The
[acceptance criteria for the default-view story](../acceptance-criteria/acceptance-criteria_example.md) cover
what the business agreed: a user can set, load and share views, and one user's default does not change
another's. Nobody wrote a criterion about what a *restricted* viewer sees inside a shared view's aggregates,
because the question only arises once you look at how sharing is implemented. This case comes from test
design, not from the agreed criteria.

**Priority: P1.** A failure here is a reportable data-exposure incident, is not user-recoverable, and is a
suspension event under the test plan rather than a defect to triage.

## Preconditions and Test Data

**System state**
- Build 2.3.1 or later on staging, `saved_views` flag enabled.
- Dashboard **DB-7** exists and carries a `region` filter field and at least one aggregate metric (total
  revenue) computed across regions.
- User **O** (owner persona) has entitlement to all regions and owns saved view **SV-31** on DB-7, with
  `config.filters = [{ field: "region", op: "in", value: ["EMEA"] }]` and `scope = shared`.
- User **R** (restricted viewer persona) has read access to dashboard DB-7 but **no entitlement to region
  EMEA**, and does have entitlement to region AMER.
- DB-7 holds at least one row in EMEA and one in AMER (illustrative: 40 EMEA rows, 60 AMER rows), so that an
  unfiltered aggregate and an entitled aggregate differ by a detectable amount.

**Test data**
- Personas O and R from the standard permission set created by Platform before test entry.
- Saved view SV-31 as configured above.
- Region reference data seeded with EMEA and AMER only, so that "everything R may see" is unambiguous.

**Must not be true:** R must not hold a wildcard or admin entitlement inherited from another group. Verify
this in step 1 rather than assuming it, because an inherited grant makes the whole case pass vacuously.

## Steps and Expected Results

| # | Action | Expected result |
|---|---|---|
| 1 | As an administrator, confirm user R's effective entitlements on DB-7 | R has AMER and does not have EMEA. If R holds EMEA by inheritance, stop: the preconditions are not met and the case cannot verify anything |
| 2 | As user O, confirm SV-31 is shared and its filter is `region in [EMEA]` | The view is listed as shared on DB-7 and its filter is unchanged |
| 3 | As user R, request `GET /dashboards/DB-7/views/SV-31` | HTTP 200. The response contains no EMEA rows. The response is not an error: the design re-checks the recipient's access on read so that a shared view can never widen what a recipient may see, which means a partly entitled reader gets their entitled data rather than a refusal. (The design's `stale_fields` degradation path is a different case, for deleted filter fields, and is covered by TC-052) |
| 4 | Inspect the aggregate metric in the same response | The total revenue is computed over R's entitled rows only (illustrative: the AMER-only total, not the EMEA total and not the combined total). A correct row filter with an uncorrected aggregate is the specific leak this case exists to catch |
| 5 | As user R, open dashboard DB-7 in the browser and select saved view SV-31 | The view loads and displays the same entitled subset. No EMEA value appears in any row, chart label, tooltip or total |
| 6 | As user O, open the same view | O sees the full EMEA-filtered result. The two users' results differ, confirming the difference in step 3 was entitlement and not an empty dataset |

## Postconditions and Teardown

No data is created, modified or deleted; the case is read-only against DB-7 and SV-31. Both sessions are
ended at the end of the run so that an authenticated session is not carried into the next case. SV-31 is left
shared, which is the precondition TC-048 expects.

## Design Rationale

**Equivalence partitioning on entitlement.** The input domain here is the recipient's entitlement relative to
the shared view's filter, and it has three partitions: **fully entitled** (recipient may see everything the
filter selects), **partially entitled** (recipient may see some of it), and **not entitled** (recipient may
see none of it).

This case covers **partially entitled**, which is the partition where a filter-level leak can actually occur:
the other two tend to be handled correctly by construction, because an all-or-nothing check is the obvious
implementation and the one a developer writes first. TC-046 covers fully entitled and TC-048 covers not
entitled; the three together exhaust the partition set.

Boundary value analysis is not applied, because entitlement here is set membership rather than an ordered
range, and there is no boundary to sit either side of.

**Step 4 exists because of a design fact plus an inference from it, not by symmetry**, and the two are worth
keeping apart. The **fact**, from the design document: the service re-checks the recipient's access on read,
so a shared view can never widen what a recipient may see. The **inference**, which is test design rather than
anything the design document states: the most likely implementation of that re-check is a row filter, and an
implementation that computes aggregates before applying that filter would leak EMEA magnitudes to R even when
every returned row is correct. Step 4 exists to catch that implementation risk. It is the case's real
objective; steps 1, 2 and 6 are setup and control.

## Environment and Configuration

Staging, build 2.3.1 or later, `saved_views` flag enabled. Entitlement is evaluated server-side, so the
API portion of this case (steps 3 and 4) is browser-independent and is run once. Step 5 is run on Chrome only;
the browser matrix is covered by the accessibility cases rather than repeated here, because nothing about
entitlement is client-dependent.

Not valid against the pre-prod replica, whose entitlement data is anonymized in a way that collapses the
region grants (illustrative), which would make R appear fully entitled and the case pass vacuously.

## Automation Status

**Partially automated.** Steps 1 to 4 and step 6 are automated at
`tests/entitlement/shared_view_restricted_viewer_spec.rb` (illustrative path) and run on every pipeline
execution for the release branch. Owner: Marcus Bell.

**Step 5 remains manual and is run once per release.** The automated version asserts on the API response; it
does not verify that no EMEA value appears in a rendered tooltip or chart label, which is a genuine gap rather
than an oversight, and is why the manual step is retained rather than deleted. Recording the gap here is the
point: the automation checks less than the case specifies, and a reader who assumed otherwise would believe
this behavior is fully guarded.

## Version and Approval

| Reviewer | Role | What they reviewed | Date |
|---|---|---|---|
| Sam Okafor | Security | The entitlement assertions and the partition choice | 2026-07-08 |
| Anjali Rao | QA Lead, Reporting | Steps, preconditions and the automation gap | 2026-07-08 |

**Version 1.1**, changed from 1.0 by adding step 4 (the aggregate check) and its design rationale, after Sam
Okafor's review observed that row-level filtering alone would not catch a leak through a pre-filter aggregate.
Version 1.0 would have passed against a defective implementation, which is the strongest argument in this
bundle for reviewing cases before running them.

**Change rule.** Wording, path and data-value edits are made in place by the case owner. Any change to the
assertions in steps 3, 4 or 5, or to the partition claim in Design Rationale, requires re-review by Security
before the case is run again, because those are the assertions the release's entitlement evidence rests on.
