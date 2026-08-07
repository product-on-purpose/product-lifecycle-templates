---
title: "{{postmortem_title}}"
incident_id: "{{incident_id}}"
status: "{{status}}"
author: "{{author}}"
incident_date: "{{incident_date}}"
postmortem_date: "{{date}}"
doc_type: incident-postmortem
size: full
source_template: incident-postmortem
source_template_version: 0.1.0
---

<!--
FULL INCIDENT POSTMORTEM. Everything the lean variant carries, plus Detection, Trigger, Resolution, and
Lessons Learned, inserted in place rather than appended, so lean stays a strict ordered subset. Reach for
this variant when the incident is severe enough, cross-team enough, or novel enough that skipping straight
from Impact to Root Causes, or from Root Causes to Action Items, would leave a reader unable to tell how the
incident was found, which of your team's own criteria made it a postmortem at all, what specifically ended
it, or what the team now believes differently about how it works.

THE TWO-SIZE PACKAGING IS THIS BUNDLE'S OWN DECISION, LABELLED AS SUCH. All five published postmortem
templates this bundle's research read in full are single-size; none ships a named lean/full pair. What the
corpus does support is that depth genuinely varies in practice: one vendor's product ships configurable
templates and "Dynamic template selection" by incident type or severity, and a real published postmortem
from a named organization used no fixed template structure at all. This library packages that real variation
as two sizes; reach for full where the incident's severity would, in a template-selecting tool, pick the
deeper option. See incident-postmortem_companion.md section 4.

A POSTMORTEM IS TRIGGERED BY A CRITERION YOUR TEAM PUBLISHED IN ADVANCE, NOT BY A BAD DAY. Google's SRE book
states an explicit list of what should prompt one: "Common postmortem triggers include: User-visible
downtime or degradation beyond a certain threshold; Data loss of any kind; On-call engineer intervention
(release rollback, rerouting of traffic, etc.); A resolution time above some threshold; A monitoring failure
(which usually implies manual incident discovery)," and holds that a team should agree its own version of
that list before an incident rather than argue it during one. See incident-postmortem_companion.md section 1.

THERE IS NO SINGLE CANONICAL SECTION SET FOR THIS DOCUMENT. The canon's own worked example and its own
follow-up volume's worked examples use materially different headings from each other. The nine sections
below are the ones this bundle could attest to a primary source and a published template, reordered for
reading rather than kept in the canon's own appendix order. See incident-postmortem_companion.md section 4.

WHAT AN INCIDENT POSTMORTEM IS, AND IS NOT
It is the document a team writes after an incident to explain why it happened and what will change so it
does not happen the same way again. It is NOT a sprint retrospective (that looks back on a period, on a
cadence, at how the team worked; a postmortem is event-triggered, about one specific thing that failed). It
is NOT the incident report: by one vendor's account, "if the incident report answers the question what
happened, the postmortem answers why it happened and what will prevent this from happening again," though
that distinction is not standards-tier, and this template treats it as one useful framing rather than
settled fact. It is NOT an After Action Review in the literal sense of that catalog alias: the US Army's own
guide describes a facilitator-led discussion running 30 minutes to 2 hours about a single training event,
not a written document. It is NOT the ITIL Problem Record: a team working inside that tradition should
expect this document to feed the Problem Record, not replace it. See incident-postmortem_companion.md
section 8.

HOW TO FILL THIS IN
1. Read the comment under each heading: WHAT it wants, WHY it matters (with a pointer into
   incident-postmortem_companion.md), guiding questions to ASK, a GOOD and a WEAK example, and the TRAP to
   avoid. For tables, PRIORITY explains the ordering rule and ROW HINT says what a good row contains.
2. Replace each {{placeholder}} with your content. Fill Summary and Impact first; the rest depends on
   knowing what actually happened before you analyze why.
3. If a section does not apply, write "N/A" and one line of why, rather than deleting it silently.
4. Before you share it: self-grade against incident-postmortem_guide.md, then DELETE every HTML comment.
   They are guidance, not content.
-->

# {{postmortem_title}}

## Summary

<!-- WHAT  A short synopsis of what happened, written before the analysis that follows it. Read first, even
           though it is usually the last thing written.
     WHY   Attested by the canon's own worked example and three of the five published templates this
           bundle's research read in full. A reader who stops here should still know what happened, how bad
           it was, and whether it is over. Deep dive: incident-postmortem_companion.md section 3 (Anatomy >
           Summary).
     ASK   What happened, in two or three sentences someone outside the incident could follow? What is the
           current status: resolved, mitigated, or still ongoing?
     GOOD  "On July 14, a config change to the Saved Views API's rate limiter caused it to reject 60 percent
           of legitimate requests for 42 minutes before the change was rolled back. Fully resolved; no data
           was lost."
     WEAK  "The Saved Views API had some issues." (no cause, no duration, no resolution state; a reader
           learns nothing from the section built to be read alone)
     TRAP  Writing the Summary as a preview of Root Causes. It is a synopsis for someone who may never read
           past it, not a teaser for the analysis below. -->

{{summary}}

## Impact

<!-- WHAT  Who and what was affected, and how badly: systems, users, duration, and any data loss.
     WHY   The most broadly attested section besides Timeline: the canon's own example and four of the five
           published templates read carry it. A postmortem that skips straight from Summary to Root Causes
           leaves the reader unable to judge whether the analysis that follows was worth the time it took to
           write. Deep dive: incident-postmortem_companion.md section 3 (Anatomy > Impact).
     ASK   What system or user population was affected? For how long? What was the magnitude (percentage of
           requests failed, records affected, revenue)? Was any data lost?
     PRIORITY  List the most severe or most visible impact first. State a real number, not a category;
           "some users" is not measurable.
     ROW HINT  A good row names one affected system or population, a duration, and a magnitude a reader
           could check against a dashboard or a support queue. A weak row is a category with no number.
     GOOD  | Saved Views API | 42 minutes | 60 percent of requests returned 429; no data loss |
     WEAK  | The API | A while | Users were affected |
     TRAP  Reporting only technical impact and skipping user or business impact, or the reverse. "The API
           was down" hides whether anyone outside engineering noticed. -->

| Affected system or population | Duration | Magnitude |
|---|---|---|
| {{impact_affected}} | {{impact_duration}} | {{impact_magnitude}} |

## Detection

<!-- WHAT  How the incident was discovered: a monitoring alert, an on-call page, a customer report, and the
           delay between the underlying failure starting and someone finding out.
     WHY   Attested by the canon's own worked example and two of the five published templates read. It is
           full-only because two other templates read fold this content into a combined heading or drop it
           entirely, so the concept is real but not yet universal enough for the smallest version of this
           document. Deep dive: incident-postmortem_companion.md section 3 (Anatomy > Detection).
     ASK   What actually surfaced this: an alert, a page, a customer ticket, or an engineer noticing
           something by chance? How long after the underlying problem started was it detected? Would an
           earlier signal have caught it sooner?
     GOOD  "Detected by the SavedViewsAPI-HighErrorRate PagerDuty alert, 6 minutes after the rate limiter
           config deployed. No customer report arrived before the alert fired."
     WEAK  "We noticed the API was having problems." (no named signal, no delay, no source; nothing here
           tells the next reader whether monitoring worked or the team got lucky)
     TRAP  Recording only that an alert fired, not how long after the failure began. The gap between failure
           and detection is often the more useful number to reduce. -->

{{detection_narrative}}

## Timeline

<!-- WHAT  A chronological, timestamped account of what happened, in order.
     WHY   The single most attested title in this bundle's research, appearing in the canon's own example
           and four of the five published templates read. It is also this document type's sharpest lesson
           about received wisdom: the SRE book's own postmortem chapter, the source most people would name
           if asked where "timeline" comes from, contains zero occurrences of the word in its prose. It
           exists only as a heading in the separately linked worked example. Deep dive:
           incident-postmortem_companion.md section 3 (Anatomy > Timeline) and section 1.
     ASK   In order, what happened, and when? Include the failure's start, detection, escalation, any
           mitigation attempts, and resolution, each with a timestamp.
     PRIORITY  List every entry in chronological order, earliest first. Do not skip the boring entries; a
           gap in the timeline is itself information about what nobody was watching.
     ROW HINT  A good row has a timestamp precise enough to check against a log or a chat transcript, and
           one clear event. A weak row has a vague time ("morning") or bundles several events into one line.
     GOOD  | 14:02 UTC | Rate limiter config change deployed to production |
     WEAK  | Sometime that afternoon | Things started going wrong |
     TRAP  Writing the timeline from memory days later without checking it against logs, alerts, or chat
           history. A timeline nobody can verify is a story, not a record. -->

| Time (UTC) | Event |
|---|---|
| {{timeline_time}} | {{timeline_event}} |

## Trigger

<!-- WHAT  The specific, named criterion, agreed by the team in advance, that made this event a postmortem
           rather than an ordinary day of operations.
     WHY   The narrowest attestation of any section in this bundle, canon plus one published template, which
           is why it is full-only. It also does the most conceptual work of any section here: it is where a
           team writes down which of its own agreed-in-advance criteria fired, rather than leaving readers
           to infer after the fact why this event, and not some other bad day, got a document. Google's own
           canon publishes an example list of what such criteria might cover: "Common postmortem triggers
           include: User-visible downtime or degradation beyond a certain threshold; Data loss of any kind;
           On-call engineer intervention (release rollback, rerouting of traffic, etc.); A resolution time
           above some threshold; A monitoring failure (which usually implies manual incident discovery)."
           Name your own team's published criterion here, not this list restated as though it were yours.
           Deep dive: incident-postmortem_companion.md section 3 (Anatomy > Trigger) and section 1.
     ASK   Which of your team's own published criteria fired? Where is that criteria list published, so a
           reader could check it? Would this event have qualified without that specific criterion?
     GOOD  "Meets our published criterion 'resolution time above 30 minutes' (see team runbook, section 2).
           Also meets 'on-call engineer intervention': the rate limiter config was rolled back manually."
     WEAK  "This felt like a big enough deal to write up." (no named criterion, nothing a future reader could
           check against, no way to tell whether the next similar incident would also qualify)
     TRAP  Restating Google's example list, or any other borrowed list, as though it were your team's own
           criteria. Naming a trigger your team never actually published is inventing a rule retroactively. -->

{{trigger_narrative}}

## Root Causes

<!-- WHAT  The contributing causes, plural by design, each with the evidence behind it.
     WHY   Attested by the canon's own example, and, under varying names (GitLab's "Root Cause Analysis,"
           Elastic's singular "Root Cause," Atlassian's split "Root cause identification" and "Root cause"),
           close to universal: present in four of the five published templates read. This is also the one
           section this bundle ships over a live, unresolved argument. A named, cross-citing community
           (Cook, Allspaw, Hollnagel, Woods, Dekker, Leveson) holds there is no single root cause in a
           complex system at all; the clearest named defence found still concedes, "sometimes you won't find
           a root cause. It happens." This template does not settle that argument; it asks for causes,
           plural, and evidence for each. Deep dive: incident-postmortem_companion.md section 3 (Anatomy >
           Root Causes) and section 6.
     ASK   What conditions, each necessary but not sufficient alone, combined to produce this incident? What
           evidence (a log line, a config diff, a metric) supports each one? Have you checked whether any
           candidate cause is actually a person's name?
     PRIORITY  List every contributing cause you have evidence for, not just the first one found. A
           single-row Root Causes table is usually a sign the investigation stopped too early.
     ROW HINT  A good row names one specific, checkable condition and the evidence behind it. A weak row
           names a broad category ("human error," "process failure") or a person.
     GOOD  | The rate limiter's config validation did not reject an out-of-range threshold before deploy |
           Deploy log shows the config passed CI with no validation step for that field |
     WEAK  | Someone made a mistake | Just experience |
     TRAP  Naming a person as a cause. GitLab's own guidance states the rule plainly: "A root cause can
           **never be a person**." A postmortem that lands on an individual has produced blame, not
           analysis, and directly contradicts the blameless framing this document type is named for. -->

| Contributing cause | Evidence |
|---|---|
| {{root_cause}} | {{root_cause_evidence}} |

## Resolution

<!-- WHAT  What specifically ended the incident: the technical or operational action taken. Distinct from
           Action Items, which are future work, not what already happened.
     WHY   Attested by the canon's own example and two published templates read. It is full-only because two
           other templates read fold this content elsewhere: one calls the equivalent moment "Recovery," and
           another folds it into timestamp fields rather than naming it separately. Deep dive:
           incident-postmortem_companion.md section 3 (Anatomy > Resolution).
     ASK   What action actually stopped the incident: a rollback, a config change, a manual failover, a fix
           deployed? Who took it, and when (cross-check against the Timeline above)?
     GOOD  "The rate limiter config change was rolled back at 14:44 UTC by the on-call engineer, restoring
           the previous threshold. Error rate returned to baseline within 3 minutes of the rollback
           completing."
     WEAK  "We fixed it." (no action named, no owner, no timestamp to check against the Timeline)
     TRAP  Describing a fix that has not actually shipped yet as though it already resolved the incident. If
           the underlying condition is still present and only masked, say so here and put the real fix in
           Action Items. -->

{{resolution_narrative}}

## Lessons Learned

<!-- WHAT  What the team concludes it should change about how it works, distinct from the specific technical
           fix recorded under Resolution and the concrete tickets recorded under Action Items.
     WHY   Attested by the canon's own worked example, which groups this content under named subsections,
           and one published template read. This template does not reproduce those subsection titles
           verbatim, since only the section's existence, not its exact wording, was confirmed for this
           bundle; write your own headings below if grouping helps. It is full-only on the same logic as
           Detection and Resolution: real, but not yet attested widely enough for the smallest version of
           this document. Deep dive: incident-postmortem_companion.md section 3 (Anatomy > Lessons Learned).
     ASK   What does this incident reveal about how the team works, beyond the specific bug: a gap in
           testing, a monitoring blind spot, an assumption that turned out false? What would you tell a team
           about to build something similar?
     GOOD  "We assumed config changes below a certain size never needed a canary rollout. This incident
           shows that assumption is false for anything touching the rate limiter; size is not a good proxy
           for blast radius here."
     WEAK  "We should be more careful next time." (not a lesson anyone could act on, indistinguishable from
           what every postmortem says)
     TRAP  Restating the Root Cause in different words. A lesson is what the team now believes about how it
           works; a root cause is what happened this time. -->

{{lessons_learned}}

## Action Items

<!-- WHAT  Concrete, owned, tracked follow-up work.
     WHY   Attested by the canon's own example and two published templates read, but the name itself is a
           pick: published templates write it three different ways and never converge: "Action Items"
           (two vendor templates), "Corrective actions" (two others), and "Follow-up actions" (a fifth).
           This bundle uses the canon's own word and says plainly that it is a pick, not a convergence. The
           canon's own worked example shows what a filled row looks like: "Plug file descriptor leak in
           search ranking subsystem | prevent | agoogler | Bug 5554825 DONE," a specific owner and a
           specific tracked bug, not a bulleted wish. The canon's own row combines the ticket ID and status
           in one field; this template splits them into separate columns for clarity, which is this
           template's own formatting choice. Two independent practitioner sources agree on where these rows
           live once the postmortem is finished: "The postmortem document is where action items are born.
           It is not where they should live," and a second, independent source says nearly the same thing.
           Link the ticket; do not leave the work only here. Neither source names a risk register or a RAID
           log as a destination; this library's own family contract offers those alongside the product
           backlog, which is this library's own convention rather than received postmortem practice. Deep
           dive: incident-postmortem_companion.md section 3 (Anatomy > Action Items).
     ASK   What specific, owned action follows from this incident? Is there already a ticket for it in the
           tracker your team actually uses? Who owns it, and is the status current?
     PRIORITY  List every action with an owner and a ticket link, prevention items before general cleanup.
           An action with no owner is not an action item, it is a wish.
     ROW HINT  A good row names one concrete action, its type (the canon's own quoted row uses "prevent";
           mitigate, detect, and process are reasonable values this bundle's research did not see quoted), a
           single named owner, and a linked ticket with a current status. A weak row is a bulleted intention
           with no owner and no ticket.
     GOOD  | Add config validation to reject out-of-range rate-limiter thresholds before deploy | prevent |
           Dana Osei | JIRA-4821 | In Progress |
     WEAK  | Be more careful with config changes | | | | |
     TRAP  Leaving an action item's only record inside this document. The moment this postmortem is
           published, every row here needs a ticket in the tracker your team already uses; an item that
           lives only in this file will not get done. -->

| Action | Type | Owner | Ticket | Status |
|---|---|---|---|---|
| {{action_item}} | {{action_item_type}} | {{action_item_owner}} | {{action_item_ticket}} | {{action_item_status}} |
