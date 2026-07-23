---
title: "{{project_name}} Risk Register"
project: "{{project_name}}"
register_owner: "{{register_owner}}"
last_reviewed: "{{date}}"
review_cadence: "{{cadence}}"
status: "{{status}}"
doc_type: risk-register
size: lean
source_template: risk-register
source_template_version: 0.1.0
---

<!--
LEAN RISK REGISTER. The smallest register that is still a real register: what it covers, an anchored scale so
a score means something, the risks themselves (one owned, actionable row each), and the cadence that keeps it
alive. Use it when one team tracks and acts on its own risks without a steering committee or auditor
consuming the register. To grow it into a governance-grade register (see risk-register_template-full.md), ADD
sections and columns; never rename or reorder the ones below, because the full variant is a strict superset
of this one.

A RISK REGISTER IS A LIVING DOCUMENT, NOT A KICKOFF DELIVERABLE. Its defining failure is going stale: a list
created once, filed, and never revisited ("risk theater"). Re-score against what you have learned, keep the
last-reviewed date current, and close or escalate risks as they move. See risk-register_companion.md
sections 1 and 7.

WHAT A RISK REGISTER IS, AND IS NOT
It is the maintained record of RISKS - potential future events - to an objective, each with an owner and a
response. It is NOT an issue log (issues have already happened; they go in a separate log), NOT a RAID log
(that also tracks Assumptions, Issues, and Dependencies; this is the deepened "R"), and NOT a compliance
filing you never reopen. If a row describes something that has already happened, it is an issue, not a risk.
See risk-register_companion.md section 8.

HOW TO FILL THIS IN
1. Read the comment under each heading: WHAT it wants, WHY it matters (with a pointer into
   risk-register_companion.md), guiding questions to ASK, a GOOD and a WEAK example, and the TRAP to avoid.
   For the table, PRIORITY explains the column legend and ROW HINT says what a good row contains.
2. Replace each {{placeholder}} with your content. The Risks table is the heart; fill it top-down by score.
3. If a section does not apply, write "N/A" and one line of why, rather than deleting it.
4. This document is never finished, but before you share it: self-grade against risk-register_guide.md, then
   DELETE every HTML comment. They are guidance, not content.
-->

# {{project_name}} Risk Register

## Purpose and Scope

<!-- WHAT  One short block: what objective or project this register covers, who owns the register itself, and
           where the scoring scale lives (below). One or two sentences.
     WHY   A rating is meaningless without an objective to rate against. The register's sharpest critique is
           aimed here: "risks to what, and what does 'high' mean?" Naming the objective is what makes the
           risks rankable. Deep dive: risk-register_companion.md section 3 (Anatomy > Purpose and Scope).
     ASK   What objective or project do these risks threaten? Who owns and maintains this register? What is
           in scope and what is explicitly out?
     GOOD  "Risks to the on-time, on-budget delivery of the Reporting Platform Modernization program (launch
           end of Q3). Owned by the program manager; reviewed with the steering group. Excludes
           enterprise-wide IT risks tracked in the corporate register."
     WEAK  "A list of project risks." (no objective named, no owner, no scope; every rating that follows is
           unanchored)
     TRAP  Skipping this because "everyone knows what the project is." Without a named objective, the scores
           below cannot be defended and the register drifts into a generic worry list. -->

{{purpose_and_scope}}

## Scoring Scale

<!-- WHAT  The anchored definitions of your likelihood and impact levels, and how they combine. A small table
           is enough for lean. The Risk Score is Likelihood x Impact.
     WHY   So "high" is not, in one critic's phrase, like calling an investment "big" or "small." Anchoring
           each level to a frequency and a consequence is what separates a real score from a gut label, and
           it is the single most effective answer to the risk-matrix critique. Deep dive:
           risk-register_companion.md section 3 (Scoring Scale) and section 6 (Debates).
     ASK   What does each likelihood level mean as a frequency (e.g. Rare = under 10% this year)? What does
           each impact level mean as a consequence (cost, delay, or regulatory outcome)? Where do you draw
           the line for "act now"?
     PRIORITY  Score = Likelihood x Impact (1-25 on a 5x5). Treat the score as a discussion-and-triage
           signal, not a precise measurement; set your own act-now threshold and state it.
     ROW HINT  A good scale row anchors a number to something observable: "4 = Likely (51-80% within the
           delivery window)", not just "4 = Likely."
     GOOD  "Likelihood 1-5 (1=Rare <10%, 3=Possible ~40%, 5=Almost certain >80% before launch). Impact 1-5
           (1=Negligible, 3=Two-week slip, 5=Launch missed). Score = LxI; 15+ is escalated."
     WEAK  "High / Medium / Low." (no anchors; two people will score the same risk differently, which is
           exactly the failure mode the critics name)
     TRAP  Copying a color-band table from the internet without setting your own thresholds. Zone boundaries
           are yours to set against your risk appetite; no banding is canonical. -->

{{scoring_scale}}

## Risks

<!-- WHAT  The ordered list of risks, highest score at the top. Each row is one risk, stated as a
           cause-event-consequence sentence, with likelihood, impact, score, a response, an owner, and a
           status.
     WHY   This is the register. A well-formed risk names why it exists, what might happen, and the effect on
           the objective; a theme label like "security" cannot be scored, owned, or acted on. Deep dive:
           risk-register_companion.md section 3 (Anatomy > Risks).
     ASK   For each risk: what is the cause, the event, and the consequence? How likely and how damaging (on
           your scale)? What is the response (avoid / reduce / transfer / accept, or escalate)? Who is the
           named owner? What is its status?
     PRIORITY  Order by score, highest first. The Response column names the strategy AND the specific action.
           The Owner is one named person, never a team. Status is a small set: Open, In Mitigation,
           Escalated, Accepted, Closed.
     ROW HINT  A good row: an ID; a cause-event-consequence statement; L, I, and their product; a strategy +
           action; a named owner; a status. A weak row is a one-word theme with no owner or action.
     GOOD  | R-01 | Because the charting-library licence renews mid-build, there is a risk its terms change and force a re-platform, delaying launch by a quarter | 3 | 5 | 15 | Mitigate: negotiate a locked 24-month licence now (Owner action) | Dana Osei | In Mitigation |
     WEAK  | R-01 | Vendor risk | H | H | | Keep an eye on it | Engineering | Open |
     TRAP  Writing theme labels instead of risk statements, or leaving the owner as a team. A risk owned by
           "Engineering" is owned by no one, and "vendor risk" cannot be scored or closed. -->

| ID | Risk (cause -> event -> consequence) | Likelihood | Impact | Score | Response (strategy + action) | Owner | Status |
|---|---|---|---|---|---|---|---|
| {{risk_id}} | {{risk_statement}} | {{likelihood}} | {{impact}} | {{score}} | {{response}} | {{owner}} | {{risk_status}} |

## Review and Ownership

<!-- WHAT  How often the register is reviewed, who owns it, and what makes a risk escalate. A few lines.
     WHY   The register's defining failure is going stale; out-of-date scoring is the most common problem in
           practice. A stated cadence plus event triggers is what keeps it a living tool rather than a filing
           cabinet. Deep dive: risk-register_companion.md section 3 (Review and Ownership) and section 7.
     ASK   How often is the register reviewed, and by whom? What event (a trigger breach, a control failure)
           forces an off-cycle update? When does a risk get escalated, and to whom? When does a risk that
           materializes move to the issue log?
     GOOD  "Reviewed fortnightly by the program manager with owners; any risk scoring 15+ is escalated to the
           steering group at its next meeting. A risk that materializes moves to the issue log the same day.
           Last reviewed 2026-07-20."
     WEAK  "Reviewed regularly." (no cadence, no owner, no escalation rule; this is how a register quietly
           dies)
     TRAP  Treating the review as a calendar formality. If nothing changes across reviews, either the risks
           are being ignored or the register has stopped reflecting reality; both are the set-and-forget
           failure. -->

{{review_and_ownership}}
