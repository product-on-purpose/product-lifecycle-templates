---
title: "Acme Analytics Platform Launch Coordination Checklist"
team_or_product: "Platform team, Acme Analytics"
owner: "Dana Osei (Staff Engineer, Platform)"
status: "active"
last_updated: "2026-07-18"
doc_type: launch-coordination-checklist
size: full
related_links:
  - "../sdd/sdd_example.md (Saved Views design; the entitlement re-check this checklist's Readiness Checks section leans on)"
  - "../test-plan/test-plan_example.md (Saved Views test plan; its exit review on 2026-07-17 is the event this snapshot follows)"
  - "../bug-report/bug-report_example.md (DEF-2291; the incident this checklist's Readiness Checks and Review Trigger sections were shaped by)"
  - "../definition-of-done/definition-of-done_example.md (Reporting Squad DoD; a per-story floor this checklist does not restate)"
source_template: launch-coordination-checklist
source_template_version: 0.1.0
---

> **Worked example.** A filled `launch-coordination-checklist`, full variant, for the Platform team at the
> fictional Acme Analytics. It is not a per-launch record: per this family's own contract, it is the standing
> instrument, shown as it stood the day after the Saved Views Sharing launch's exit review on 2026-07-17, the
> same exit review the [`test-plan`](../test-plan/test-plan_example.md) example schedules and the same
> incident, DEF-2291, the [`bug-report`](../bug-report/bug-report_example.md) and
> [`sdd`](../sdd/sdd_example.md) examples describe. Per the `standing-standards` family contract, that chaining
> is loose by design: this document belongs to the Platform team across every launch it coordinates, not to
> one moment in the Saved Views story. Two later events in the same thread postdate this snapshot and are not
> cited below: the Reporting Squad Definition of Done's 2026-07-24 amendment and the entitlement-audit
> runbook's first live use on 2026-07-28. Read this alongside
> [`launch-coordination-checklist_guide.md`](launch-coordination-checklist_guide.md), the rubric it was graded
> against. All names not already established in the library's Acme Analytics thread, all thresholds, and all
> dates not otherwise cited are illustrative.

# Acme Analytics Platform Launch Coordination Checklist

## Scope and Launch Classes

For the Platform team, a launch is any change that becomes reachable by an account outside the team that
wrote it: a new or materially changed API response shape, a permission or entitlement boundary that did not
exist before, a flag flipped on for traffic outside the owning team's own dashboards, or a new externally
visible control. A change that stays behind a flag with zero external traffic, or that only a member of the
owning team can reach, is not yet a launch under this definition, whatever its size in the codebase. The
classes below decide how much of this checklist a given launch has to clear, down to the smallest class
needing none of it.

| Launch Class | Qualifying Criteria | Sections Required |
|---|---|---|
| Tier 1 | Introduces or changes a permission or entitlement boundary, puts in front of customers something none of them has used before, or touches any billing or invoicing path | Every section of this checklist, each filled for the specific launch |
| Tier 2 | Reaches accounts outside the owning team, or reaches Support or Documentation, but touches no permission, entitlement, or billing boundary | Readiness Checks, Rollout and Rollback, Go/No-Go Criteria, Review Trigger. Roles and Decision Authority is skipped: the on-call engineer for the owning service holds decision authority by default. Launch Communications is skipped unless Support or Documentation is affected |
| Tier 3 | Reversible in a single deploy, reaches no account outside the owning team, and touches no permission or billing boundary | None. This checklist does not apply; the change is judged against the owning squad's own Definition of Done and merges through the normal pull-request process |

The Saved Views Sharing launch below is Tier 1: it opens a new entitlement boundary (a view one account owns
becomes visible to another) on top of the Tier 3 private-views work that shipped ahead of it.

## Roles and Decision Authority

| Role | Named Holder | Responsibility |
|---|---|---|
| Decision authority | Dana Osei (Staff Engineer, Platform) | Holds final say on whether every Tier 1 launch across Acme Analytics proceeds; his is the one signature a Yellow row in Go/No-Go Criteria needs before the launch may proceed on it |
| Launch coordination lead | Rotates per launch, named at kickoff. For Saved Views Sharing: Marcus Bell (Staff Engineer, Reporting) | Keeps Readiness Checks and Go/No-Go Criteria current for the specific launch; the person Dana Osei's go/no-go call is actually based on |
| Security reviewer | Sam Okafor (Security) | Signs off the entitlement or permission row in Go/No-Go Criteria before that row may read Green; required on every Tier 1 launch, not only ones flagged as sensitive by the coordination lead |
| Permission-matrix owner | Anjali Rao (QA Lead) | Owns the permission-matrix result in Go/No-Go Criteria and the regression guard behind it; one of the two inputs Dana Osei's go call cannot proceed without |
| Communications owner | Priya Nair (PM, Reporting), for Saved Views Sharing | Owns Launch Communications for the specific launch: confirms Support and Documentation are briefed before the coordination lead may bring Go/No-Go to Dana Osei |

Because Dana Osei is the single decision authority, his go call requires both Anjali Rao's
permission-matrix result and Sam Okafor's security sign-off to already read Green in Go/No-Go Criteria
before he may act on it. He does not evaluate either input himself. This is a direct response to what an
earlier launch in this program cost when nobody held that second-reviewer role: DEF-2291 shipped past the
row-level checks because nothing beyond the implementer's own read confirmed the aggregate path, and the
gap was not visible until a permission-matrix case designed to look at aggregates, not just rows, caught it
in staging.

## Readiness Checks

| Area | Question | What Answers It | Owner | Why This Check Exists |
|---|---|---|---|---|
| Entitlement and permissions | Does every read path re-check the recipient's actual access, including any aggregate or count derived from the underlying rows, not only the rows themselves? | The design document's entitlement re-check statement, confirmed against an aggregate value in the same response, not only the row list | Marcus Bell (coordination lead) | DEF-2291 shipped because the row-level filter was correct while the aggregate was computed before that filter ran; a check that only reads the rows would have passed |
| Regression coverage | Is the specific failure class from the most recent entitlement incident now enforced on every pipeline run for this release branch, not only in a local test file? | The regression case's own status in the CI configuration for the release branch | Anjali Rao (QA Lead) | A fix with no standing regression guard reopens on the next change that touches the same code path |
| Shared-scope isolation | If sharing misbehaves, can shared views alone be switched off while every customer's private views keep working? | A dry run against this week's build flipped the flag off and confirmed the dashboard falls back cleanly, and the flip touched only the shared-view scope, not the whole `saved_views` flag | Marcus Bell | Private views came first, in phase one, and sharing is built on top of them; a switch that could not separate the two would take away working behaviour in order to stop broken behaviour |
| Dependency readiness | Does the team this launch depends on know it is about to receive load or scrutiny it has not seen before from this surface? | A written confirmation from that team's own on-call rotation, not an assumption that they read the same planning document | Dana Osei | The permissions service is the one dependency every entitlement check in this launch resolves through; an unprepared owner on the other end is a blind spot the launching team cannot see from its own dashboards |
| Exposure if the worst case happens | If the entitlement check failed the way it failed before, how many existing records would already carry the wrong result before anyone noticed? | A count taken from the data itself, run against the current production dataset, not an estimate from memory of how many views exist | Marcus Bell | Sizing the blast radius before launch is what turns "we think it's contained" into a number Dana Osei can actually weigh against the launch date |

## Launch Communications

| Audience | What They Need To Know | When | Owner |
|---|---|---|---|
| Support | What "shared" means for entitlement: the recipient's own permissions still gate what they see, and the one-line answer to "why did my total change after I opened a shared view" | Before the first rollout stage opens, because the first shared view a customer receives is also the first question Support gets | Jordan Ames (Support Lead) |
| Documentation | A help center article covering creating, sharing, and setting a default view is published and linked from the Views control's own help icon | Live before go-live, not drafted after | Priya Nair |
| Public announcement | That Saved Views sharing has shipped, and what changed for a user who receives a shared view. Drafted separately as a `release-notes` entry; this checklist only confirms the right people have already seen it | At go-live | Priya Nair |

## Rollout and Rollback

Sharing rolls out in two stages behind the existing `saved_views` flag, the same flag that already governs
the private-views work this launch builds on. Stage one enables the `shared` scope for the Reporting
squad's own dashboards only, and runs for 48 hours with every row in Readiness Checks above reading current
and every row in Go/No-Go Criteria below reading Green or an accepted Yellow. Stage two flips the flag for
every Acme Analytics dashboard. Each stage needs its own explicit go from Dana Osei; a clean stage one does
not automatically advance stage two.

| Rollback Trigger | Evidence Threshold | Authorized To Pull It |
|---|---|---|
| Any confirmed entitlement mismatch on a shared view, of any severity | One case matching DEF-2291's shape: rows correctly filtered while an aggregate or count derived from those rows is not | The on-call engineer for the surface in question, no approval required, scoped to the one dashboard the mismatch was found on |
| Shared-view load time at p95 crosses 1.5 times the phase-one (private-views) baseline for 15 consecutive minutes | The dashboard-service latency panel, filtered to requests carrying `scope=shared` | Dana Osei, no approval required |
| Shared-view creates fail with a 5xx at three times the phase-one private-view create failure rate, over any 10-minute window | The error-rate panel on `ViewsController`, split by `scope` | The on-call engineer for dashboard-service, who acts first and tells Dana Osei afterwards |

## Go/No-Go Criteria

| Criterion | State | Evidence | Owner |
|---|---|---|---|
| Full permission matrix (3 personas by 4 filter scopes) passes with zero failures | Green | Re-executed from the start on 2026-07-15, per the test plan's resumption rule, after DEF-2291; all 12 combinations passed | Anjali Rao |
| Entitlement re-check covers aggregate reads as well as row-level reads | Green | Build 2.3.2, released 2026-07-14, moves aggregate computation behind the entitlement filter; the regression case now runs on every pipeline execution for the release branch | Marcus Bell |
| Security review sign-off | Green | Unblocked on 2026-07-15, once the fix above was reverified and the full permission matrix had re-passed | Sam Okafor |
| A single, dashboard-scoped kill switch exists for shared views specifically, separate from the broader `saved_views` flag | Yellow, accepted | The existing flag already disables sharing one dashboard at a time, confirmed by the rollback rehearsal above; a switch that disables sharing everywhere at once without touching private views does not exist yet | Dana Osei, accepted through 2026-08-15, tracked as follow-up engineering work owned by Marcus Bell |
| Support and Documentation ready | Green | Help center article live; Support briefing confirmed complete by Jordan Ames | Priya Nair |

**Yellow-state exception on record.** Dana Osei accepted the missing dashboard-wide kill switch as a Tier 1
launch condition on 2026-07-17, on the reasoning that the per-dashboard switch already covers the exact
failure shape DEF-2291 exposed, and that a second, broader switch is real engineering work rather than a
configuration change that could ship before stage two. The acceptance expires 2026-08-15; if the broader
switch is not built by then, stage two does not proceed further without Dana Osei revisiting this row, not
an automatic rollback of what has already shipped.

## Review Trigger

| Event That Would Make This Wrong | Owner Who Notices | What They Do About It |
|---|---|---|
| A second entitlement-boundary defect reaches a Go/No-Go review with the permission-matrix criterion already reading Green | Dana Osei | Investigate whether the matrix's own evidence bar missed a read path, the way the pre-DEF-2291 version missed aggregates, before adding a new row to Readiness Checks for it |
| The permissions service changes how it evaluates an entitlement check, for example by adding a caching layer in front of the decision it returns | Dana Osei | Re-verify that the aggregate-read check in Readiness Checks still exercises the real, current decision path, not a cached shortcut, before the next Tier 1 launch runs a Go/No-Go review against it |
| Every launch logged in a quarter lands in the same class | Marcus Bell, as the most recent coordination lead | Bring it to the Platform team's next quarterly sync and redraw the Scope and Launch Classes boundaries above, rather than letting a class that discriminates nothing stay on the books |
