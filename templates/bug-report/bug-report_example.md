---
title: "Shared view totals include rows the recipient is not entitled to see"
report_id: "DEF-2291"
reported_by: "Anjali Rao (QA Lead, Reporting)"
reported_on: "2026-07-13"
affected_build: "2.3.1 (staging)"
severity: "S1 Critical"
priority: "P1"
assigned_to: "Marcus Bell (Staff Engineer, Reporting)"
status: "closed"
related:
  - "../test-case/test-case_example.md (TC-047, the case that found this, at step 4)"
  - "../test-plan/test-plan_example.md (Saved Views test plan; risk R-05 and the suspension rule)"
  - "../sdd/sdd_example.md (Saved Views design; the entitlement re-check on recipient read)"
doc_type: bug-report
size: full
source_template: bug-report
source_template_version: 0.1.0
---

<!--
Worked example for the bug-report bundle: a full-variant report closing the chain this family started. The
defect was found by TC-047 step 4, which was designed from risk R-05 in the test plan, which inherited it
from the program risk register. Figures marked "illustrative" are made up for the example.

WHY THE FULL VARIANT: this report was filed by QA against a release gate, triage changed one of its values,
and the closed record is the evidence that the gate was satisfied. A user-filed report of the same defect
would arrive in the lean variant and grow into this one.

THREE THINGS TO STUDY. First, the expected behavior is stated AND sourced - the element missing from two real
reports in three. Second, the reporter and triage disagreed about priority, and the disagreement is recorded
rather than silently overwritten, which is what teaches the next reporter how the scale works. Third, the
resolution names the regression guard, so the chain closes where it began: a risk produced a plan, the plan
produced a case, the case produced this report, and this report produced a test.
-->

# DEF-2291: Shared view totals include rows the recipient is not entitled to see

## Summary

A recipient opening a shared saved view sees aggregate values computed over rows they are not entitled to,
even though those rows are correctly hidden from the table. On dashboard DB-7, an analyst entitled only to
AMER sees the combined AMER and EMEA revenue total. Affects any recipient of any shared view whose filter
selects data the recipient cannot otherwise access, which on current usage is an estimated 40 shared views
across 12 dashboards (illustrative).

## Steps to Reproduce

1. As an administrator, confirm test account **R** has entitlement to AMER and **not** to EMEA on dashboard
   **DB-7**. (If R holds EMEA by inheritance the test proves nothing; this is why the check is step 1.)
2. As account **O** (entitled to all regions), create a saved view on DB-7 filtered to `region in [EMEA]`,
   and set its scope to `shared`. This is view **SV-31**.
3. As account **R**, request `GET /dashboards/DB-7/views/SV-31`.
4. Read the `total_revenue` value in the response, and compare it with the returned rows.

At step 4 the returned rows array is empty of EMEA rows, correctly, while `total_revenue` equals the EMEA
total. The same is visible in the UI: open DB-7 as R, select SV-31, and read the Total Revenue tile above an
empty table.

## Expected and Actual Behavior

**Expected.** The aggregate reflects only rows the recipient is entitled to, so for account R the total should
be the AMER-only total, or zero for a view that selects nothing R may see. This follows from the design
document, which states that on any read of a shared view by another user the service re-checks that user's
access to the underlying dashboard data, *so a shared view can never widen what a recipient may see*.

**Actual.** The row filter is applied correctly and the aggregate is not. `total_revenue` returns 1,284,900
(illustrative), which is the EMEA total that account O would see, while `rows` is empty. The magnitude of data
R may not access is therefore disclosed exactly, in a single number.

**Note on where the expectation comes from, because it matters here.** No acceptance criterion covers this.
The agreed criteria for the Saved Views stories describe saving, loading, defaulting and sharing views; none
of them says anything about what a partially entitled recipient sees inside an aggregate. The expectation
comes from the design document's re-check statement and from the program's PII risk appetite, not from
anything the business signed off. This is exactly the territory test design is supposed to reach and
acceptance criteria are not.

**Theory, labeled as a theory:** the aggregate looks like it is computed before the entitlement row filter is
applied. Not verified at the time of filing.

## Environment and Reproducibility

Staging, build **2.3.1**, `saved_views` flag enabled. Accounts R (AMER only) and O (all regions) from the
standard permission persona set. Reproduced via the API **5 times out of 5** and in the browser (Chrome 141,
macOS) **3 times out of 3**, including after a hard refresh and in a private window.

Not reproducible when the recipient has no entitlement to *any* row the view selects: in that case the total
returns zero, which is why the fully-unentitled case (TC-048) passed and did not surface this. The defect
requires a **partially** entitled recipient, which is the partition TC-047 was written to cover.

No existing report found. Searched the tracker for "shared view total", "aggregate entitlement" and
"saved view permissions".

## Evidence

- `shared-view-total.png` - the Total Revenue tile reading 1,284,900 above an empty table, as account R.
- `response.json` - the full API response for step 3. Look at `total_revenue` on line 3 against the empty
  `rows` array on line 8.
- Staging application log, 2026-07-13 14:22 UTC, request ID `7f3c-4a11-a91b` (illustrative). The entitlement
  re-check is logged as passing, which is correct: the check ran and filtered the rows. Nothing in the log
  indicates the aggregate path exists, which is itself the useful signal.

No customer data is attached; both accounts are synthetic personas and the revenue figures are seeded test
data.

## Impact, Severity and Priority

| Field | Value | Why | Set by |
|---|---|---|---|
| Severity | **S1 Critical** | Discloses the magnitude of data across an entitlement boundary. Not user-recoverable and not detectable by the affected user. On Acme's four-level scale (S1 Critical / S2 Major / S3 Minor / S4 Trivial), data exposure is S1 by definition | Anjali Rao (QA Lead) |
| Priority | **P1**, raised from P2 | Reporter set P2 on the reasoning that this is staging and the feature is behind a flag, so no customer is currently exposed. Triage raised it: the test plan's exit criteria treat any entitlement failure as a **suspension event** rather than a triage item, and phase 2 of the rollout cannot proceed until it is fixed and the full permission matrix is re-run | Priya Nair (PM), at triage |

**Impact if shipped.** Any recipient of a shared view could infer the size of data they are not permitted to
see, without any indication that they were seeing it. The row-level protection working correctly is what makes
this dangerous rather than obvious: the table looks right, so nothing prompts a user or a reviewer to
question the total.

**The severity and priority disagreement is worth keeping**, not tidying away. Both readings were reasonable.
The reporter weighed current exposure, which was genuinely zero; triage weighed the release gate, which the
reporter did not own. The record now shows the next reporter how Acme's scale treats a flagged, staging-only
entitlement failure.

## Triage and Ownership

Triaged **2026-07-13**, same day, by Priya Nair (PM), Marcus Bell (Engineering) and Sam Okafor (Security).

- Severity confirmed at S1.
- Priority raised from P2 to P1, for the reason recorded above.
- **Phase 2 (sharing) testing suspended immediately**, per the test plan's suspension rule. Anjali Rao made
  the call at 15:10 UTC and notified Priya Nair, Marcus Bell and Sam Okafor the same afternoon. Phase 1
  (private views) testing continued, since it does not exercise the sharing path.
- Owner: **Marcus Bell**. Assigned to the **2.3.2** hotfix, not to the next scheduled release.
- Sam Okafor confirmed the security review remains blocked until this is closed and the full permission
  matrix has been re-run from the start.

## Resolution and Regression Guard

**Cause.** The aggregate for dashboard tiles was computed in the query layer *before* the entitlement row
filter was applied. The re-check itself was implemented correctly and ran on every recipient read, exactly as
the design document specifies; it filtered rows on the way out and never touched the pre-computed aggregates.
The reporter's labeled theory turned out to be right, but the investigation confirmed it rather than
inheriting it.

**Why it was not caught earlier.** Every earlier entitlement case asserted on returned rows. A row-level
assertion cannot see this defect: the rows were always correct. TC-047 caught it only because step 4 asserts
on the aggregate as well, and that step was added at version 1.1 after Sam Okafor's review of the case.
Version 1.0 of TC-047 would have passed against this build.

**Fix.** PR 812 (illustrative) moves aggregate computation behind the entitlement filter, so both are derived
from the same permitted row set. Released in build **2.3.2** on 2026-07-14.

**Verification.** Re-run by Anjali Rao on 2026-07-15 against the original steps: `total_revenue` returns the
AMER-only total for account R, and O's view is unchanged. The **full permission matrix was re-executed from
the start**, not just this case, per the test plan's resumption rule: an entitlement defect invalidates the
assumption behind every passing result in that matrix. All 12 combinations passed. Sam Okafor confirmed the
security review unblocked on 2026-07-15 and phase 2 testing resumed the same day.

**Regression guard.** [TC-047](../test-case/test-case_example.md) step 4, which asserts the aggregate as well
as the rows, is now part of the release regression set and runs on every pipeline execution for the release
branch. A second case, TC-053, was added for the same class of defect on the row-count badge, which shares the
pre-filter computation path and was not covered by anything.

**Not reopened.** If this recurs, a new report is opened and linked to this one, so that the record of what
2.3.2 actually changed stays intact.
