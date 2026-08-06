---
title: "{{runbook_title}}"
service_or_system: "{{service_or_system}}"
triggering_alert: "{{triggering_alert}}"
owner: "{{owner}}"
status: "{{status}}"
last_updated: "{{date}}"
doc_type: runbook
size: full
source_template: runbook
source_template_version: 0.1.0
---

<!--
FULL RUNBOOK. Everything the lean variant carries, plus Prerequisites and Access, Remediation and Cleanup,
and When This Does Not Apply. Use it where a runbook needs to stand up to something beyond the moment it is
executed: a regulated environment where Validation doubles as an audit trail, cross-team ownership where
Prerequisites and an explicit boundary keep the wrong team from running the wrong procedure, or a service
complex enough that "this does not apply here" needs to be said rather than assumed.

THIS VARIANT IS A STRICT SUPERSET OF THE LEAN ONE. The four lean sections, Purpose and Trigger, Procedure,
Validation, and Review Trigger, appear here in the same order with the same headings and placeholders; full
only adds the three sections named above. If you started lean and are growing into this, add the new
sections; do not reorder or rename anything you already filled in.

A RUNBOOK IS THE PROCEDURE FOR ONE TRIGGER, NOT ONE SERVICE, AND NOT THE STANDING OPERATIONS MANUAL. This
template ships the incident-scoped procedure some sources publish, one trigger, one investigation-and-
remediation arc, not the larger, differently scoped service-operations manual other sources publish under
the same name, covering an entire service's overview, deployment, and disaster recovery in one document.
That is a bigger scope, not a bigger size of this template; if Prerequisites and Access is growing past a
handful of lines, that is the warning sign. See runbook_companion.md sections 4 and 8.

A NOTE ON THE NAME. The Google literature this practice traces back to calls this artifact a "playbook," not
a runbook; across the chapters this bundle's research read, "runbook" appears only inside a third-party case
study, never in Google's own analytical prose. This library keeps the catalog's own name, runbook, and says
so plainly rather than implying the canon uses it. See runbook_companion.md section 2.

WHAT A RUNBOOK IS, AND IS NOT
It is the executable procedure a responder opens when a known situation occurs. It is NOT a knowledge base
article ("check the logs and restart the service if needed" is not a runbook; it must direct a specific
action), NOT a disaster recovery plan (NIST scopes that to recovering one or more systems at an alternate
facility after a major failure, one register above this), NOT a checklist in the Gawande sense (a minimal
memory guard against omission, not a full procedural walkthrough), and NOT the standing service-operations
manual described above. See runbook_companion.md section 8.

HOW TO FILL THIS IN
1. Read the comment under each heading: WHAT it wants, WHY it matters (with a pointer into
   runbook_companion.md), guiding questions to ASK, a GOOD and a WEAK example, and the TRAP to avoid. For
   tables, PRIORITY explains the ordering rule and ROW HINT says what a good row contains.
2. Replace each {{placeholder}} with your content. Fill Purpose and Trigger and Procedure first; everything
   else depends on them.
3. If a section does not apply, write "N/A" and one line of why, rather than deleting it silently. "None
   identified" is a legitimate, honest answer for When This Does Not Apply.
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

## Prerequisites and Access

<!-- WHAT  What a responder needs before they can start: access grants, roles, tooling, and any logging
           that must already be turned on.
     WHY   Of the templates this bundle's research read, only Microsoft's security-operations format names
           this as its own fixed component: "Prerequisites: The specific requirements you need to complete
           before starting the investigation... logging that should be turned on and roles and permissions
           that are required." Everywhere else this content is folded into the first procedure steps, which
           is why it stays out of the lean variant: naming it separately earns its own weight only once a
           runbook is formal enough to also carry the other full-only sections. Deep dive:
           runbook_companion.md section 3 (Anatomy > Prerequisites and Access).
     ASK   What access, role, or permission must the responder already hold? What tooling or dashboard must
           already be open or configured? What logging must already be turned on for the Procedure steps to
           work at all?
     PRIORITY  List only what would actually block or slow down step 1 if missing. A nice-to-have is not a
           prerequisite.
     ROW HINT  A good row names one concrete requirement, why the Procedure needs it, and exactly how a
           responder gets it before an incident, not during one. A weak row is a vague "have access" with
           no specifics.
     GOOD  | prod-readonly role in the cluster IAM group | Step 1 requires kubectl access to the prod
           namespace | Request via the Access Portal, group saved-views-oncall |
     WEAK  | Access to the systems | Needed | Ask your manager |
     TRAP  Letting this section grow past a handful of lines. That is usually a sign the runbook is quietly
           turning into the kind of standing operations manual that documents an entire service, a
           different and larger artifact than this template covers. See runbook_companion.md section 8. -->

| Requirement | Why the Procedure needs it | How to get it before an incident |
|---|---|---|
| {{prereq_item}} | {{prereq_reason}} | {{prereq_how_to_obtain}} |

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

## Remediation and Cleanup

<!-- WHAT  What to undo once the immediate situation is handled: temporary mitigations, feature flags,
           scaled-up capacity, anything that should not become the new permanent state.
     WHY   This is the evidenced name for this content, drawn from a practitioner template's own section
           title, "Remediation and cleanup." An item left here unresolved across incidents is itself a
           signal: the same temporary workaround recurring is often the strongest evidence the underlying
           cause was never actually fixed. Deep dive: runbook_companion.md section 3 (Anatomy > Remediation
           and Cleanup).
     ASK   Did you flip a switch, scale something up, or disable a check to get through the incident? What
           needs to be reverted, by when, and who owns reverting it? What happens if it is never reverted?
     PRIORITY  List every temporary change made during the Procedure, even ones that feel harmless. An
           unlisted temporary change is the one that becomes permanent by accident.
     ROW HINT  A good row names the specific temporary change, why it must be undone, a named owner, and
           the trigger or deadline for undoing it. A weak row names a worry with no owner and no deadline.
     GOOD  | Scaled saved-views-api to 12 replicas (from 4) | Temporary capacity added to absorb the retry
           storm; not load-tested at this size long-term | Dana Osei | Scale back within 24 hours of the
           alert clearing |
     WEAK  | Scaled things up | Fix later | Team | Someday |
     TRAP  Leaving an item here with no owner or deadline. An undone cleanup item is the strongest
           predictor that the same workaround will recur, unexamined, at the next incident. -->

| Item to undo | Why it must be undone | Owner | Trigger or deadline |
|---|---|---|---|
| {{cleanup_item}} | {{cleanup_reason}} | {{cleanup_owner}} | {{cleanup_trigger}} |

## When This Does Not Apply

<!-- WHAT  The situations that look like this trigger but are not, and what to do instead. An honestly
           filled "none identified" is a legitimate answer.
     WHY   No source this bundle's research read publishes a section with this name or job; it is this
           template's own device for drawing the boundary explicitly rather than leaving a responder to
           guess it under pressure. A responder who cannot tell whether this is the right document for what
           they are looking at is exactly the failure the curse-of-knowledge framing describes, a runbook
           written by someone who cannot picture what the reader does not already know. Deep dive:
           runbook_companion.md section 3 (Anatomy > When This Does Not Apply) and section 8.
     ASK   What symptom looks like this trigger but has a different cause? How would a responder tell them
           apart? If this is the wrong runbook, which one is right, and is it linked?
     PRIORITY  List only genuine near-misses a responder could plausibly confuse with this trigger. A
           lookalike nobody would ever confuse this with does not belong here.
     ROW HINT  A good row names the lookalike symptom, its actual cause, and points to the correct runbook
           or action. A weak row is vague enough to cover everything, which covers nothing.
     GOOD  | Elevated latency with error rate still under 1 percent | Usually the shared database's
           connection pool, not the Saved Views API | See db-connection-pool-exhaustion runbook instead |
     WEAK  | Other issues | Different cause | Investigate separately |
     TRAP  Leaving this section empty by omission rather than by a stated "none identified." An empty
           section nobody thought about is not the same thing as one that was checked and found empty. -->

| Symptom that looks like this trigger | What it actually is | What to do instead |
|---|---|---|
| {{lookalike_symptom}} | {{actual_cause}} | {{redirect_action}} |

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
