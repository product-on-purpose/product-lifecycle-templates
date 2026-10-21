---
title: "Acme Analytics - Reporting Platform Modernization Test Strategy"
doc_type: test-strategy
size: lean
organization_or_program_name: "Acme Analytics - Reporting Platform Modernization"
owner: "Anjali Rao (QA Lead, Reporting)"
status: active
doc_version: "1.0.0"
created: "2026-07-20"
updated: "2026-07-20"
related_links:
  - "../test-summary-report/test-summary-report_example.md (Saved Views summary report, final 2026-07-17; its DEF-2291 finding is why this strategy exists)"
  - "../test-plan/test-plan_example.md (Saved Views for Dashboards Test Plan, approved 2026-07-06, before this strategy existed; its test_strategy_ref field predates the seam this document now fills)"
source_template: test-strategy
source_template_version: 0.1.0
---

> **Worked example.** A filled `test-strategy`, the lean variant this bundle ships in only one size, for
> Acme Analytics' Reporting Platform Modernization program: the standing document the
> [`test-plan`](../test-plan/test-plan_example.md) example's own `test_strategy_ref` field names as absent
> ("Acme Reporting has no standing test strategy document") at that plan's date of 2026-07-06. It is dated
> 2026-07-20, the same program steering review date the
> [`kpi-dashboard`](../kpi-dashboard/kpi-dashboard_example.md) and
> [`raid-log`](../raid-log/raid-log_example.md) examples were last reviewed, and three days after the
> [`test-summary-report`](../test-summary-report/test-summary-report_example.md) example went final on
> 2026-07-17 and drew the lesson behind DEF-2291: an entitlement assertion written against individual rows
> cannot catch a leak in an aggregate computed across them, the gap every entitlement case written before
> that release's own case review shared. Per the `standing-standards` family contract, this document's
> chaining stays loose by design: a program agrees it once and consults
> it repeatedly, rather than any one project's release producing it. No test plan in this library yet
> names it in a `test_strategy_ref` field; this is that seam's first filled strategy. Read it alongside
> [`test-strategy_guide.md`](test-strategy_guide.md), the rubric it was graded against. Names already
> established in the library's Acme Analytics thread are reused as established; the Scheduled Exports
> project, the data residency attestation, and every figure marked illustrative are this example's own
> invention.

# Acme Analytics - Reporting Platform Modernization Test Strategy

## Purpose and Scope

Acme Analytics had never run a program-level test strategy until this one. The gap showed up directly:
Saved Views for Dashboards, the Reporting Platform Modernization program's first project, caught DEF-2291
only because a case review added an aggregate assertion to a High-tier case five days before that case
fired. Every entitlement case written before that review had asserted on
individual rows, and every row was always correct; nothing told the team that an entitlement check has to
assert on an aggregate as well as a row. The project's own test plan had no program default to inherit,
only its own judgment, so the next project would have had to rediscover the same lesson on its own. This
strategy binds every project the Reporting Platform Modernization program runs under its own release
calendar: today, that is the Reporting squad's ongoing Saved Views work, and the forthcoming Scheduled
Exports project the program has not yet staffed (invented for this example; no other document in this
library names it). A project signs on the same way `test-plan` already expects: it writes this strategy's
name into its own `test_strategy_ref` field, rather than drafting defaults from nothing.

**Explicitly out of scope:** The Growth pillar's own A/B experimentation platform, whose testing validates
statistical experiment design rather than release readiness and will keep its own separate strategy once
one is written; Acme's data residency attestation with its cloud hosting provider, which that provider's
own audit process covers, not any project's test plan; and the legacy reporting flow that predates this
program, which stays under its existing regression suite until it is migrated onto the platform this
program builds.

## Test Levels and Types

| Level or Type | Default or Mandatory | Reason or Obligation |
|---|---|---|
| Unit and integration (CI gate) | Default | Every level below assumes the CI gate is already green; a project that skips it is testing on top of an unknown foundation |
| WCAG 2.2 AA accessibility testing | Mandatory | Written into Acme Analytics' enterprise customer contracts, not a government accessibility law; Legal confirmed this with Sales before this strategy was written |
| Security review of any change touching a permission boundary | Mandatory | A review by Security found the gap behind DEF-2291 before it shipped: an entitlement case that asserts only on rows cannot see a leak in an aggregate computed across them; this gate makes that review a standing requirement rather than each project's own discovery |
| Data tests on any new or changed table | Default | A project that ships a pipeline or warehouse table runs, at minimum, a uniqueness check, a not-null check, an accepted-values check and a referential check on it before the table goes live |
| Load testing of any new or materially changed query path | Default | Reporting workloads spike at month-end close; a new query path is smoke-tested first, then run at progressively higher load toward its expected ceiling before production |
| Contract testing across service boundaries | Default | The program's services talk to each other over internal APIs that can change independently; a consumer-driven contract test runs in CI before either side of a boundary ships a breaking change |

## Standard Tooling and Environments

Every project defaults to the same environment ladder Reporting already runs Saved Views through: a
CI-only unit and integration run on every commit; a shared Staging tier, reseeded nightly, for functional
and end-to-end work; a Pre-prod replica, sized to match production load, for anything performance
sensitive; and, for any project that changes stored data, a separate migration sandbox for dry runs and
rollback rehearsals before anything touches Staging. A project may add an environment Platform does not
already provide, a dedicated load-test harness, for instance, but it still passes through CI and Staging
first; it does not skip straight to a bespoke environment of its own.

**Rule for real or production-derived data in test:** Staging and the migration sandbox run on anonymized
or synthetic data by default; no project loads an unanonymized production extract into either one as a
matter of course. A project that hits a case anonymized data genuinely cannot exercise, a defect that only
reproduces against one real customer's data shape, say, opens a time-boxed exception instead of loading
real data on the sly. The request names which tables are involved and goes to Dana Osei for anything
touching the shared database; nothing loads until she signs off. The exception rides with the release
window it was opened for (illustrative: two to three weeks), and a later release starts the request over
rather than inheriting it.

## Governance and Policy Alignment

No test policy exists above this strategy. Acme Analytics has never written one, and nothing here should
be read as implying one is coming soon. If Acme Analytics adopts a test policy later, aligning this
strategy to it becomes the first item on the agenda of whichever steering review follows that adoption,
ahead of whatever else that review was already going to cover.

**Who approves a change to this strategy:** Marta Reyes, Program Manager, at the program's monthly
steering review. A change that cannot wait for that cadence, correcting a wrong environment name, say, may
be made by Anjali Rao directly and reported at the next review rather than held for it.

## How Project Test Plans Inherit or Deviate

Adoption is simply writing this strategy's name into a project's own `test_strategy_ref` field; that
single step is the whole of it, which is why the field already existed in `test-plan` before this document
did. Where a project's Risk-Ranked Approach departs from one of the defaults above, a skipped level, a
different environment, a waived data test, the plan states the reason next to that row rather than in a
separate memo nobody reads later.

**Who may accept a deviation from this strategy:** Anjali Rao, as the strategy's own owner, accepts a
deviation from any Default row once the stated reason is written down. A deviation touching a Mandatory
row also needs Marta Reyes's sign-off: a Mandatory row exists because of an obligation this program does
not get to waive on one QA Lead's say alone. A deviation with no reason written down is not accepted, and
the plan stays unapproved until one is.

## Roles and Responsibilities Across Projects

| Role | Holder | Responsibility |
|---|---|---|
| Strategy owner | Anjali Rao, QA Lead, Reporting | Owns this document, drafts every revision, and brings a proposed change to the program's steering review |
| Approver | Marta Reyes, Program Manager | Approves this document and its revisions at the program's monthly steering review |
| Shared-infrastructure liaison | Dana Osei, Staff Engineer, Platform | Confirms the environment and data-exception defaults above still match what Platform actually runs, and flags this document when they drift |
| Per-project execution | Each project's own test plan owner (Anjali Rao, for Saved Views, as of this writing) | Runs testing for their own project against these defaults, recording any deviation in their own plan |

## Review Trigger

| Condition | Owner | What They Do About It |
|---|---|---|
| A project's own plan states a deviation from one of this strategy's defaults | Anjali Rao | Checks whether the same deviation has now shown up in more than one project's plan, or whether it touches one of the Mandatory rows above; either one puts the default itself on the next steering review's agenda |
| Acme Analytics adopts a test policy above this strategy, or changes one it already has | Anjali Rao | Checks every section above against the new policy and updates whatever no longer aligns, ahead of the next scheduled steering review |
| A test summary report shows a mandatory level or type above was skipped on a shipped release | Marta Reyes | Brings the skip to the next steering review as a possible defaults gap, the same kind of gap a case review caught in DEF-2291 before it could ship rather than after |
| A new test level, tool or environment is adopted on more than one project without this document naming it as a default | Anjali Rao | Proposes adding it as a program default rather than letting each project keep rediscovering it on its own |

Acme Analytics has no audit or regulatory requirement forcing a calendar review of this document. Absent
one, the conditions above are the whole of how this strategy stays current; there is no separate annual
review date standing in for them.
