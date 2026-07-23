---
title: "{{project_name}} Risk Register"
project: "{{project_name}}"
register_owner: "{{register_owner}}"
risk_management_approach: "{{approach_doc_link}}"
last_reviewed: "{{date}}"
review_cadence: "{{cadence}}"
risk_appetite: "{{appetite_statement}}"
status: "{{status}}"
doc_type: risk-register
size: full
source_template: risk-register
source_template_version: 0.1.0
---

<!--
FULL RISK REGISTER. The governance-grade register: everything in the lean variant, plus dual (inherent and
residual) scoring, an escalation-and-appetite section, and a closed-and-materialized audit trail. Use it when
a steering committee, auditor, or board consumes the register, when you must demonstrate that controls work
(which requires the residual score), or when regulation prescribes fields you must carry.

This is a STRICT SUPERSET of risk-register_template-lean.md: the first four sections are identical in name
and order; full only adds columns and the last two sections. If you are starting lean and growing, add these;
do not reorder.

A RISK REGISTER IS A LIVING DOCUMENT, NOT A KICKOFF DELIVERABLE. Its defining failure is going stale ("risk
theater"): a list created once, filed, and never reopened. Re-score against what you learn, keep last-reviewed
current, and move risks through their statuses. See risk-register_companion.md sections 1 and 7.

THE DUAL SCORE IS THE POINT OF THE FULL VARIANT. Score each risk INHERENT (before your controls) and RESIDUAL
(after them). The residual score is the figure you report upward; the gap between the two is the only
on-register evidence that your controls are doing anything. A register with a single score cannot show whether
its mitigations work. See risk-register_companion.md section 3 (the dual-score pattern).

HOW TO FILL THIS IN
1. Read the comment under each heading: WHAT, WHY (with a companion pointer), ASK, GOOD, WEAK, TRAP; tables
   add PRIORITY and ROW HINT.
2. Replace each {{placeholder}}. The Risks table is the heart; order it by residual score, highest first.
3. If a section does not apply, write "N/A" and one line of why, rather than deleting it.
4. Never finished, but before you share it: self-grade against risk-register_guide.md, then DELETE every HTML
   comment.
-->

# {{project_name}} Risk Register

## Purpose and Scope

<!-- WHAT  What objective or program this register covers, who owns the register, the governing risk
           management approach it follows, and what is in and out of scope.
     WHY   A rating is meaningless without an objective to rate against; the register's sharpest critique is
           "risks to what, and what does 'high' mean?" At the governance scale, also name the approach
           document that sets your categories, scales, and appetite. Deep dive:
           risk-register_companion.md section 3 (Purpose and Scope) and section 8 (vs the risk management plan).
     ASK   What objective does this register protect? Who owns it and who maintains it day to day? Which risk
           management approach or policy governs it? What is explicitly out of scope (and where does it live)?
     GOOD  "Risks to the on-time, on-budget delivery and adoption of the Reporting Platform Modernization
           program. Owned by the program manager, maintained by the PMO, governed by the corporate Risk
           Management Approach v3. Excludes BAU IT risks (corporate register) and product-outcome risks
           (tracked on the program KPI dashboard)."
     WEAK  "Project risks for the program." (no owner, no approach, no scope boundary)
     TRAP  Omitting the approach link at governance scale, so reviewers cannot tell where your scales and
           appetite came from and every score is arguable. -->

{{purpose_and_scope}}

## Scoring Scale

<!-- WHAT  The full likelihood and impact anchors, the 5x5 matrix / heatmap, and the inherent-vs-residual
           method. This is the reference the table's numbers point to.
     WHY   Anchored scales are the strongest answer to the risk-matrix critique: they make "high" mean a
           specific frequency and consequence rather than a gut feeling. The heatmap communicates the
           portfolio at a glance; the inherent/residual method is what lets the register demonstrate control
           effectiveness. Deep dive: risk-register_companion.md section 3 (Scoring Scale) and section 6.
     ASK   What frequency anchors each likelihood level? What consequence anchors each impact level (cost,
           schedule, regulatory, reputational)? What are your zone thresholds and act-now line? How do you
           compute residual from inherent and control effectiveness?
     PRIORITY  Score = Likelihood x Impact (1-25). Score both inherent (pre-control) and residual
           (post-control). Zone boundaries are yours to set against appetite; state them. The score triages
           and drives discussion; it is not a precise measurement.
     ROW HINT  Anchor each level to something observable: "5 = Almost certain (>80% before launch)", "5 =
           Severe (launch missed or >GBP 1M loss)". A good heatmap marks the act-now zone explicitly.
     GOOD  "Likelihood 1-5 (1=Rare <10%, 2=Unlikely 10-30%, 3=Possible 30-55%, 4=Likely 55-80%, 5=Almost
           certain >80%, within the delivery window). Impact 1-5 anchored to schedule and cost (5 = launch
           missed or >GBP 1M). Residual 15+ (red) escalates; 8-14 (amber) is actively managed; <8 (green) is
           monitored. Residual = inherent reassessed after listed controls."
     WEAK  "1-5 scale, higher is worse." (no anchors, no residual method, no thresholds)
     TRAP  Importing a safety-standard color band (e.g. ISO 45001) unchanged into a delivery program. The
           bands are context-specific; set yours to your appetite, or the heatmap misleads. -->

{{scoring_scale}}

## Risks

<!-- WHAT  The register table, ordered by residual score, highest first. Each row is one risk with a category,
           a cause-event-consequence statement, inherent and residual scores, a response, a trigger, an owner
           and actionee, and a status.
     WHY   The dual score is what makes this governance-grade: inherent shows raw exposure, residual shows
           exposure after controls, and the gap is your control-effectiveness evidence. The trigger converts
           the register into an early-warning system and pre-defines when a risk becomes an issue. Deep dive:
           risk-register_companion.md section 3 (Risks; the dual-score pattern; the trigger).
     ASK   For each risk: category? cause-event-consequence? inherent L/I/score before controls? response
           strategy and specific action? residual L/I/score after controls? observable trigger / KRI? named
           owner and (if different) actionee? proximity (when it could hit)? status?
     PRIORITY  Order by RESIDUAL score, highest first. Strategy is one of avoid / reduce / transfer / accept
           / escalate (threats) or escalate / exploit / share / enhance / accept (opportunities). Owner is one named
           person; actionee is who executes if different. Status: Open, In Mitigation, Escalated, Accepted,
           Closed, Materialized.
     ROW HINT  A good row carries a real cause-event-consequence statement, two distinct scores (inherent >
           residual when controls help), a concrete trigger, and a named owner. A weak row is a theme label
           with one gut score and no trigger.
     GOOD  | R-01 | Vendor | Because the charting-library licence renews mid-build, there is a risk its terms change and force a re-platform, delaying launch by a quarter | 3x5=15 | Mitigate: negotiate a locked 24-month licence before the renewal date | 2x5=10 | Renewal notice received, or licence terms circulated | Dana Osei / Legal | Q3 | In Mitigation |
     WEAK  | R-01 | Risk | Vendor problems | High | fix it | | | Eng | | Open |
     TRAP  Setting residual equal to inherent for every row. If controls never move the score, either they do
           nothing or you have not reassessed; both defeat the point of dual scoring. -->

| ID | Category | Risk (cause -> event -> consequence) | Inherent (LxI=S) | Response (strategy + action) | Residual (LxI=S) | Trigger / KRI | Owner / Actionee | Proximity | Status |
|---|---|---|---|---|---|---|---|---|---|
| {{risk_id}} | {{category}} | {{risk_statement}} | {{inherent_score}} | {{response}} | {{residual_score}} | {{trigger}} | {{owner_actionee}} | {{proximity}} | {{risk_status}} |

## Review and Ownership

<!-- WHAT  The review cadence, who owns and maintains the register, the audience-tiered reporting, and the
           escalation and issue-handoff rules.
     WHY   Out-of-date scoring is the most common register failure; a stated cadence plus event triggers is
           what keeps it living. At governance scale, reporting is tiered: operational detail for owners,
           trends for the risk committee, exceptions for the board. Deep dive: risk-register_companion.md
           section 3 (Anatomy > Review and Ownership, which covers the audience-tiered reporting).
     ASK   How often is the register reviewed and by whom? What events force an off-cycle update? How is it
           reported to each audience (owners / committee / board)? When does a materialized risk move to the
           issue log?
     GOOD  "Reviewed fortnightly by the PMO with owners; residual 15+ escalated to the steering group monthly;
           board sees only risks over appetite, quarterly. A materialized risk moves to the issue log the day
           its trigger fires, and its register row is marked Materialized with a link. Last reviewed
           2026-07-20."
     WEAK  "Reviewed at steering meetings." (no cadence, no tiering, no issue handoff)
     TRAP  Reporting the same detail to every audience. A board does not want 40 rows; it wants the few over
           appetite and the decisions needed. -->

{{review_and_ownership}}

## Escalation and Risk Appetite

<!-- WHAT  The organization's risk appetite/tolerance for this program, and the thresholds and path for
           escalating a risk beyond the team.
     WHY   Appetite is the line that turns a score into a decision: a residual score above appetite demands
           action or acceptance at a higher level. Escalate is a real response strategy (PMBOK 6+) for risks
           whose response is beyond the team's authority. Without a stated appetite, "how high is too high?"
           has no answer. Deep dive: risk-register_companion.md section 3 (Scoring Scale, and Anatomy >
           Risks > Response where the escalate strategy is defined).
     ASK   What is the appetite/tolerance for this program (in schedule, cost, quality, reputation terms)?
           What residual score or category crosses it? Who does an over-appetite risk escalate to, and on
           what timeline? Which current risks are escalated, and why?
     GOOD  "Appetite: we will accept up to a two-week schedule risk but no data-loss or PII-exposure risk
           above residual 6. Any residual 15+, or any PII risk above 6, escalates to the steering group
           within one week. Currently escalated: R-05 (PII in saved views), residual 9, above the PII line."
     WEAK  "We have a low risk appetite." (not measurable; nothing to compare a score against)
     TRAP  Writing an appetite nobody can test. "Low appetite" is a slogan; "no residual PII risk above 6" is
           a rule that actually gates escalation. -->

{{escalation_and_appetite}}

## Closed and Materialized Risks

<!-- WHAT  The audit trail: risks that have been closed (mitigated, expired, or accepted and retired) and
           risks that materialized and moved to the issue log. Keep them; do not delete.
     WHY   The history is what makes the register auditable and what lets you learn: a materialized risk that
           was scored low is a scoring lesson; a closed risk shows a control worked. Deleting closed rows
           erases the evidence. Deep dive: risk-register_companion.md section 8 (vs the issue log).
     ASK   Which risks are closed, and why (mitigated / expired / accepted)? Which materialized, when, and
           where did they go (issue log link)? What did a materialized risk teach about the scoring?
     PRIORITY  Keep closed and materialized rows for the life of the register. A Materialized status links to
           the issue it became. Note the close reason and date.
     ROW HINT  A good closed/materialized row records what happened and why, not just a status flip: "R-03
           materialized 2026-06-14 (key engineer left); moved to issue log ISS-11; had been scored residual
           6, under-rated - raised owner-departure risks to a floor of 9 thereafter."
     GOOD  | R-08 | Closed 2026-05-30 | Mitigated: load test passed at 3x target; risk retired. |
     WEAK  | R-08 | Closed | (no reason, no date, no lesson) |
     TRAP  Deleting closed risks to keep the register short. The closed history is the audit trail and the
           scoring feedback loop; archive, never delete. -->

{{closed_and_materialized}}
