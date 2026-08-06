---
title: "{{runbook_title}}"
service_or_system: "{{service_or_system}}"
triggering_alert: "{{triggering_alert}}"
owner: "{{owner}}"
status: "{{status}}"
last_updated: "{{date}}"
doc_type: runbook
size: lean
source_template: runbook
source_template_version: 0.1.0
---

<!--
LEAN RUNBOOK. The smallest procedure that is still a real runbook: what invokes it, what to do, how to
confirm it worked, and what would make it wrong. Four sections, because a runbook a responder cannot read in
the middle of an incident has already failed at its one job. To carry prerequisites, cleanup, and an explicit
boundary (see runbook_template-full.md), ADD sections; never rename or reorder the ones below, because the
full variant is a strict superset of this one.

A RUNBOOK IS THE PROCEDURE FOR ONE TRIGGER, NOT ONE SERVICE. It is scoped to the alert or condition that
opens it, not to everything a responder might ever need to know about the system. If you find yourself
listing several unrelated triggers here, you are probably writing two runbooks under one title. See
runbook_companion.md sections 1 and 3.

A NOTE ON THE NAME. The Google literature this practice traces back to calls this artifact a "playbook," not
a runbook; the word "runbook" appears in that canon only inside a third-party case study, never in Google's
own analytical prose. This library keeps the catalog's own name, runbook, and says so plainly rather than
implying the canon uses it. See runbook_companion.md section 2.

WHAT A RUNBOOK IS, AND IS NOT
It is the executable procedure a responder opens when a known situation occurs. It is NOT a knowledge base
article ("check the logs and restart the service if needed" is not a runbook; it must direct a specific
action), NOT a disaster recovery plan (that recovers one or more systems at an alternate facility after a
major failure, one register above this), NOT a checklist in the Gawande sense (a minimal memory guard against
omission, not a full procedural walkthrough), and NOT the standing service-operations manual some sources
publish under the same name, which covers an entire service rather than one trigger. See
runbook_companion.md section 8.

HOW TO FILL THIS IN
1. Read the comment under each heading: WHAT it wants, WHY it matters (with a pointer into
   runbook_companion.md), guiding questions to ASK, a GOOD and a WEAK example, and the TRAP to avoid. For
   tables, PRIORITY explains the ordering rule and ROW HINT says what a good row contains.
2. Replace each {{placeholder}} with your content. Fill Purpose and Trigger and Procedure first; everything
   else depends on them.
3. If a section does not apply, write "N/A" and one line of why, rather than deleting it silently.
4. Before you ship it: self-grade against runbook_guide.md, then DELETE every HTML comment. They are
   guidance, not content.
-->

# {{runbook_title}}

## Purpose and Trigger

<!-- WHAT  What invokes this runbook, the system or service it is about, and the one-line job it does. Name
           the specific alert, condition, or page, not a general topic.
     WHY   The Google source most of this literature traces to states that "whenever an alert is created, a
           corresponding playbook entry is usually created." A runbook with no stated trigger cannot be told
           apart from a wiki page about the service, which is the exact boundary a knowledge base article
           fails to cross. Deep dive: runbook_companion.md section 3 (Anatomy > Purpose and Trigger) and
           section 8.
     ASK   What is the specific alert, condition, or page that opens this document? What system or service
           does it belong to? What is the one-line outcome this runbook exists to produce? Is it linked from
           the alerting tool itself?
     GOOD  "Triggered by the SavedViewsAPI-HighErrorRate PagerDuty alert on the Saved Views API. Purpose:
           restore the API error rate below 1 percent within 15 minutes of the page firing."
     WEAK  "This runbook covers the Saved Views service." (no named alert, no condition, no stated outcome;
           a responder cannot tell this apart from a wiki page)
     TRAP  Naming several unrelated triggers in one document. That is usually a sign you are writing two
           runbooks under one title; split them. -->

{{purpose_and_trigger}}

## Procedure

<!-- WHAT  The steps that resolve the situation the trigger describes, starting from a known state. Say
           plainly, in one sentence, whether this procedure is written GENERAL (principles, changes slowly)
           or STEP-BY-STEP (exact commands, reduces variability), and why.
     WHY   Google names this choice contentious inside its own organisation: some argue for general entries
           that change slowly, others for step-by-step entries that reduce human variability and drive down
           MTTR, and its own chapter calls it "a contentious topic." This template does not pick a side its
           source declines to pick; it asks you to state which you are writing. The same source draws one
           hard line regardless of style: "if your playbooks are a deterministic list of commands that the
           on-call engineer runs every time a particular alert fires," automate it instead of documenting it.
           Deep dive: runbook_companion.md section 3 (Anatomy > Procedure) and section 6.
     ASK   Are you writing general guidance or exact commands, and why, given who runs this and how often?
           What is the known starting state? What are the ordered steps? Has any step here been run
           unchanged so many times that it is now a candidate for automation instead of documentation?
     PRIORITY  Number the steps in the order a responder actually performs them. Start from a known state
           rather than "open the dashboard," which hides exactly the context a responder under pressure does
           not have.
     ROW HINT  A good row names one concrete action, the exact command or decision it requires, and the
           result that tells the responder it worked before moving on. A weak row is a vague verb with no
           way to tell whether it succeeded.
     GOOD  | 1 | Run `kubectl rollout restart deploy/saved-views-api -n prod` | Rollout status shows all
           pods Ready within 3 minutes |
     WEAK  | 1 | Restart the service | It should come back |
     TRAP  Writing "open the dashboard" or "check the logs" as a step with no named dashboard, no named
           log, and no signal to look for. That is a knowledge-base sentence, not a runbook step. -->

{{procedure_approach}}

| Step | Action | Expected result |
|---|---|---|
| {{step_number}} | {{step_action}} | {{step_expected_result}} |

## Validation

<!-- WHAT  The specific signal that confirms the situation is actually resolved before you close out: a
           metric back to baseline, an alert clearing, a health check passing.
     WHY   "Confirm it's fixed" cannot be checked by someone else; a named signal can. In a regulated
           environment this table is also your audit trail, so it should let a reviewer see what was
           checked, not just that something was. Deep dive: runbook_companion.md section 3 (Anatomy >
           Validation).
     ASK   What signal tells you the situation is actually resolved, not just quiet? Where do you look for
           it? How do you tell a false negative (it looks fine but is not) from a real recovery?
     PRIORITY  List every check a responder must clear before closing the incident, not just the first one
           that looks reassuring. Order them in the sequence you would actually check them.
     ROW HINT  A good row names one specific, observable signal, the value or state that counts as pass,
           and exactly where to look. A weak row is "confirm it's fixed" with no location and no threshold.
     GOOD  | Error rate | Below 1 percent for 5 consecutive minutes | Saved Views API dashboard, error-rate
           panel |
     WEAK  | Everything looks fine | OK | Eyeballing the dashboard |
     TRAP  Treating the alert clearing as the only check. An alert can clear because its threshold rearmed,
           not because the underlying cause is fixed; pair it with a second, independent signal. -->

| Check | What counts as pass | Where to verify it |
|---|---|---|
| {{validation_check}} | {{validation_signal}} | {{validation_method}} |

## Review Trigger

<!-- WHAT  The event that would make this runbook wrong, and the named person or role expected to notice
           it. Not a calendar date alone.
     WHY   A runbook fails silently: "the decay is silent until the moment of failure," and the mechanism is
           a process mismatch: the runbook lives in a wiki while the system lives in code, maintained by
           different people. No source this bundle's research read names an event-plus-owner trigger; every
           one reaches for a calendar, a quarterly cadence or a 90-day-untouched heuristic. This section is
           this bundle's own contribution, built to close that gap, not received industry practice. Deep
           dive: runbook_companion.md section 3 (Anatomy > Review Trigger) and section 6.
     ASK   What system change would make this runbook wrong: a redeploy, a schema change, a dependency
           swap, an ownership handover? Who is on the hook to notice when that happens? What do they do
           about it, re-verify, update, or retire the runbook?
     PRIORITY  Pair every date-based cadence with at least one event-based trigger. An event with no named
           owner is not a trigger, it is a hope.
     ROW HINT  A good row names a specific system change, the person or role who notices it, and what they
           do next. A weak row is "review quarterly" with nobody named.
     GOOD  | Saved Views API redeployed on a new runtime | On-call lead for Saved Views | Re-run this
           procedure against the new environment before the next on-call rotation starts |
     WEAK  | Review this runbook quarterly | Team | Update if needed |
     TRAP  Naming only a calendar date. A quarterly review passes every audit and can still be wrong the
           day an incident actually needs it; pair the date with the event that breaks the document. -->

| Event that would make this wrong | Owner who notices | What they do about it |
|---|---|---|
| {{review_event}} | {{review_owner}} | {{review_action}} |
