# Companion: The Runbook

> The deep explainer for the runbook bundle. Read this to understand what a runbook is, where the name
> comes from, why the template is shaped the way it is, and where the sources this bundle read disagree
> about it. The short operator card is [`runbook_guide.md`](runbook_guide.md); a fully worked instance is
> [`runbook_example.md`](runbook_example.md). Inline citations like [[1]](#ref-1) resolve to the
> [References](#references) at the bottom, tagged by source reliability. This bundle sits in the
> `standing-standards` family alongside `definition-of-done`: a definition of done is a standard you are
> judged against, a runbook is an instrument you execute.

---

## 1. Orientation

A runbook is **the document a responder opens when a known alert fires, so that the response does not
depend on who is awake.** It is scoped to one situation rather than one service: the trigger that invokes
it, the steps that resolve it, and the check that confirms it worked. The Google source most of the
literature traces back to states its job as high-level, not exhaustive: *"Playbooks contain high-level
instructions on how to respond to automated alerts. They explain the severity and impact of the alert, and
include debugging suggestions and possible actions to take to mitigate impact and fully resolve the
alert."* [[1]](#ref-1)

**At a glance**
- It exists **because of a trigger, not a topic**: *"whenever an alert is created, a corresponding playbook
  entry is usually created."* [[1]](#ref-1)
- The canon most of this literature traces to actually calls this a **playbook**, and this bundle keeps the
  name `runbook` because that is the catalog's own name and the industry's common usage, said plainly
  rather than implied as canon [[1]](#ref-1)[[7]](#ref-7).
- Its value is **asserted far more often than it is measured**. Google's own clearest number is one
  informally stated 3x figure with no described method [[16]](#ref-16), and every vendor percentage this
  research chased turned out untraceable [[29]](#ref-29)[[30]](#ref-30)[[31]](#ref-31).
- There is a **named test for when a step should stop being a document and become automation**: whether it
  is deterministic, not how often it runs [[1]](#ref-1)[[6]](#ref-6).
- It **fails silently**: *"A runbook does not announce that it has decayed. The decay is silent until the
  moment of failure."* [[17]](#ref-17) No source this research read names an event trigger plus an owner as
  the fix, which is why this bundle ships a Review Trigger section with no published precedent.

If you read nothing else: a runbook is not a wiki page about a service, and it is not a place to write down
everything you know. It is one alert's worth of procedure, written for the person who did not write it.

## 2. Origins and evolution

**Nearly everything the canon says about this artifact sits in one chapter.** The definition, the purpose,
the maintenance debate and the automation test all come from the SRE Workbook's On-Call chapter
[[1]](#ref-1). The SRE Book proper, the more widely read of the two Google volumes, contributes exactly one
passing mention: an alert-generated bug carrying *"links to the black-box prober's recent results and to
the playbook entry for this alert"* [[2]](#ref-2). A bundle that cited "the Google SRE book" generally for
runbook practice would be citing a book that barely mentions the thing it is citing it for.

**The name is the more interesting part of the history, and it is worth stating plainly.** Google's own
voice calls this artifact a **playbook**. Four of the five SRE Book chapters most likely to discuss it,
Being On-Call, Emergency Response, Managing Incidents and Eliminating Toil, were fetched and searched by
full-text regex for both words and returned zero occurrences of either [[3]](#ref-3)[[4]](#ref-4)
[[5]](#ref-5)[[6]](#ref-6). The word "runbook" does appear, exactly three times, in the Workbook's
Incident Response chapter, and **every occurrence sits inside a contributed third-party case study**
written by PagerDuty staff, not in Google's own analytical prose: *"The on-call SRE validated that all
automated recovery actions had been executed, and completed the mitigation steps in relevant runbooks."*
[[7]](#ref-7) Google's own voice in that same chapter closes with *"Regularly review and iterate on your
incident management plans and playbooks."* [[7]](#ref-7) This bundle keeps the name `runbook` because that
is this catalog's name and the term the wider industry actually uses; it says so rather than implying the
canon endorses it.

**Outside Google, the word travels into several different lineages that do not agree on shape.** PagerDuty
attributes a seven-section structure to Tom Limoncelli and describes runbooks needing to stay *"constantly
tested and updated"* [[8]](#ref-8). Atlassian publishes two differently structured templates under the same
name, one for ITSM and one for DevOps [[9]](#ref-9)[[10]](#ref-10). Microsoft's security-operations
material calls the artifact a playbook again and gives it four fixed components [[11]](#ref-11). Emmer's
practitioner template is explicitly opinionated, six sections framed as *"the author's opinions"* where
*"not all sections apply to every runbook"* [[12]](#ref-12). Skelton Thatcher's widely referenced community
template runs to 65 headers and describes a different, larger artifact entirely [[13]](#ref-13). A more
recent lineage argues the document is a transitional stepping stone toward automation, or already obsolete
[[14]](#ref-14)[[15]](#ref-15). Section 5 traces these strands properly; the point here is that no single
lineage owns this word.

## 3. Anatomy (section by section)

The full variant carries seven sections; the lean variant carries four of them, unchanged in name and
order, so lean is a strict ordered subset of full.

### Purpose and Trigger (lean and full)

What invokes this runbook, and what it is for.

This section is not optional weight, and the build spec originally treated it as a full-only addition
before the research moved it into lean. The reason is structural: PagerDuty's format is built around the
alert that pages the responder [[8]](#ref-8), Atlassian's ITSM template lists the alerts a service produces
[[9]](#ref-9), and the SRE Workbook states plainly that *"whenever an alert is created, a corresponding
playbook entry is usually created"* [[1]](#ref-1). A runbook with no stated trigger cannot be told apart
from a wiki page about the service, which is the exact boundary section 8 draws.

Beginner note: name the specific alert, condition or page that opens this document, and link it if your
tooling supports linking an alert to its runbook, which more than one source treats as standard practice
[[18]](#ref-18)[[20]](#ref-20). Expert note: if you find yourself listing several unrelated triggers here,
that is usually a sign you are writing two runbooks under one title.

### Prerequisites and Access (full only)

What a responder needs before they can start: access, roles, tooling, logging.

Of the templates read, only Microsoft's security-operations format names this as its own fixed component:
*"Prerequisites: The specific requirements you need to complete before starting the investigation. For
example, logging that should be turned on and roles and permissions that are required."* [[11]](#ref-11)
Everywhere else this content exists, it is folded into the first procedure steps rather than named
separately, which is why the research moved it out of lean: naming it earns its own weight only once a
runbook is formal enough to also carry the other full-only sections.

Beginner note: list the concrete things a responder needs before touching anything, credentials, access
grants, a specific dashboard. Expert note: if this section grows past a handful of lines, check whether the
runbook is quietly turning into the kind of standing operations manual Skelton Thatcher publishes
[[13]](#ref-13), which is a different, larger artifact and out of scope for this template (see section 8).

### Procedure (lean and full)

The steps that resolve the situation the trigger describes.

This is the document's reason for existing, and it is also where the research found genuine, named
disagreement inside Google's own organisation about how it should read. The Workbook states two positions
in consecutive sentences: *"Some SREs at Google advocate keeping playbook entries general so they change
slowly,"* against *"Other SREs advocate for step-by-step playbooks to reduce human variability and drive
down MTTR."* Of the disagreement itself it says, *"If your team has conflicting views about playbook
content, the playbooks might get pulled in many directions. This is a contentious topic."* [[1]](#ref-1)
This bundle does not pick a side its own best primary source declines to pick; write general or
step-by-step, but decide which, and say so.

There is one place the same source does draw a hard line, and it is the sharpest practical rule in this
bundle: *"If your playbooks are a deterministic list of commands that the on-call engineer runs every time a
particular alert fires, we recommend implementing automation."* [[1]](#ref-1) The operative word is
deterministic, not frequent, and it sits inside a wider argument that manual, repeatable work is toil even
when it is fast: *"Running a script may be quicker than manually executing each step in the script, but the
hands-on time a human spends running that script (not the elapsed time) is still toil time."* [[6]](#ref-6)
Contrast that primary-source rule with vendor arguments for automating or replacing runbooks entirely
[[14]](#ref-14)[[15]](#ref-15): the primary source's test is about the shape of the procedure, the vendor
argument is about selling the automation.

Beginner note: number the steps, and start from a known state rather than "open the dashboard," which hides
exactly the context a responder under pressure does not have [[17]](#ref-17). Expert note: run the
determinism test on your own procedure periodically; a step that has not changed in months of use is a
candidate for automation, not for more documentation [[1]](#ref-1).

### Validation (lean and full)

How a responder confirms the situation is actually resolved before closing out.

The only validation section recorded by title in this bundle's research is Microsoft's Checklist, *"A list
of tasks for the steps in the flow chart. This checklist can be helpful in highly regulated environments to
verify what you have done,"* [[11]](#ref-11). Emmer's incident template covers the same ground in a section
recorded as Validating health and stability [[12]](#ref-12). The build spec originally paired validation
with rollback under one heading, "Verification and Rollback"; **no source read titles a section that way**,
so the template drops the pairing and names its own sections, Validation here and Remediation and Cleanup
below.

Beginner note: name the specific signal that tells you it worked, a metric back to baseline, an alert
clearing, a health check passing, rather than "confirm it's fixed." Expert note: in a regulated environment,
this section is your audit trail; write it so someone reviewing after the fact can see what was checked, not
just that something was.

### Remediation and Cleanup (full only)

What to undo once the immediate situation is handled: temporary mitigations, feature flags, scaled-up
capacity, anything that should not become the new permanent state.

Emmer's incident template records a section of the same shape, Remediation and cleanup [[12]](#ref-12), and
this section's name follows it closely without claiming to reproduce it. Related content appears under
different names in the standing-operations-manual sources, Disaster Recovery Plans at PagerDuty
[[8]](#ref-8) and Failover and Recovery at Skelton Thatcher [[13]](#ref-13), but those sources describe a
bigger, differently scoped artifact (see section 8), so their section names are not carried into this
template.

Beginner note: if you flipped a switch, scaled something up, or disabled a check to get through the
incident, this is where you write down that it needs to be flipped back. Expert note: an item left here
unresolved across incidents is itself a signal, the same temporary workaround recurring is often the
strongest evidence that the underlying cause was never actually fixed.

### When This Does Not Apply (full only)

The situations that look like this trigger but are not, and what to do instead.

No source this research read publishes a section with this name or job. It earns its place because the
sources disagree, repeatedly, about where a runbook's boundary sits against its neighbors: whether it is the
same thing as a standard operating procedure [[27]](#ref-27), a disaster recovery plan [[25]](#ref-25), or a
plain troubleshooting article in a knowledge base [[28]](#ref-28). A responder under pressure who cannot
tell whether this is the right document for what they are looking at is exactly the failure the "curse of
knowledge" framing describes, a runbook written by someone who cannot picture what the reader does not
already know [[18]](#ref-18). This section is the template's own device for drawing that boundary
explicitly rather than leaving a responder to guess it under pressure. It is labelled here as the bundle's
own contribution, not received practice.

Beginner note: name the symptom that looks similar but has a different cause, and point to the runbook that
actually covers it if one exists. Expert note: an empty version of this section, honestly filled with "none
identified," is a legitimate answer; a version nobody has thought about is not the same thing.

### Review Trigger (lean and full)

What event makes this runbook wrong, and who is expected to notice.

This section discharges an obligation the `standing-standards` family contract states directly rather than
one any source volunteered. The failure mode is well evidenced: *"A runbook is a frozen snapshot of how your
system used to work. The system keeps changing. The runbook does not."* [[17]](#ref-17) The mechanism is a
process mismatch: *"The runbook is in a wiki. The system is in code. The two are maintained by different
processes and often by different people."* [[17]](#ref-17) Google names the same decay from inside its own
practice: *"Details in playbooks go out of date at the same rate as production environment changes."*
[[1]](#ref-1)

Sources that address a remedy converge on ownership and versioning, *"Treat them like code. Store them in a
central, version-controlled system like Git or an incident management platform"* [[21]](#ref-21), a named
owner field, *"**Owner:** {TEAM}"* [[20]](#ref-20), and linking the runbook from the alert itself
[[18]](#ref-18)[[20]](#ref-20). But every one of those sources reaches for a calendar when it comes to
review, a quarterly cadence [[21]](#ref-21) or a 90-day untouched heuristic [[20]](#ref-20), and **none of
them names an event that makes the document wrong plus a person who notices.** Of the templates read, only
one carries a service-owner field at all [[13]](#ref-13), and none carries a last-verified date inside the
document body itself. So this section is this bundle's own contribution, stated as such rather than dressed
up as received practice, and it asks for something no source read: an event, not a date.

Beginner note: name the specific change that would make this runbook wrong, a redeploy, a schema change, a
dependency swap, and who is on the hook to notice it. Expert note: a review trigger tied only to a calendar
date will pass every audit and still be wrong the day it matters; pair the date with the event.

## 4. Variants and sizing

**Lean (four sections)** is Purpose and Trigger, Procedure, Validation, and Review Trigger. It is the
default because it is close to the shape of the sources' own smallest published templates, Emmer's six
sections framed as partly optional [[12]](#ref-12) and Microsoft's four fixed components [[11]](#ref-11),
and because a runbook that a responder cannot read in the middle of an incident has already failed at its
one job.

**Full (seven sections)** adds Prerequisites and Access, Remediation and Cleanup, and When This Does Not
Apply. Notice what the three additions have in common: none of them is content a responder needs while the
alert is actively firing. Prerequisites is read before the incident starts, Remediation and Cleanup after
it ends, and When This Does Not Apply is a scoping note rather than a step. Use full where a runbook needs
to stand up to something beyond the moment it is executed, a regulated environment where Validation doubles
as an audit trail [[11]](#ref-11), cross-team ownership where Prerequisites and an explicit boundary prevent
the wrong team from running the wrong procedure, or a service complex enough that "this does not apply
here" needs to be said rather than assumed.

**A boundary worth stating here rather than only in section 8.** This template ships the incident-scoped
procedure shape, not the standing service-operations manual PagerDuty [[8]](#ref-8) and Skelton Thatcher
[[13]](#ref-13) publish under the same name. That second artifact runs to dozens of sections and covers an
entire service rather than one alert. It is a bigger scope, not a bigger size, so it is taught as a
relationship rather than shipped as a third size.

## 5. Methodology lineage

**The SRE lineage** is the load-bearing one for this bundle: the SRE Workbook's On-Call chapter
[[1]](#ref-1) and the SRE Book's Introduction, which supplies the one quantified figure Google states for
this artifact, offered informally rather than as a study: *"When humans are necessary, we have found that
thinking through and recording the best practices ahead of time in a "playbook" produces roughly a 3x
improvement in MTTR as compared to the strategy of "winging it.""* [[16]](#ref-16) No sample, method or
comparison group accompanies that number in the text this research read; it is Google's own statement of
experience, not a described study.

**The ITSM lineage** treats the runbook as an operational-tooling artifact rather than an SRE one.
Atlassian's two templates split this further, one built around architecture and known errors for ITSM
[[9]](#ref-9), one built around system architecture and operational procedures for DevOps [[10]](#ref-10). That the same
vendor publishes two mutually inconsistent templates under the same name is itself evidence that no single
industry-standard shape exists.

**The security-operations lineage** treats the runbook as an incident-response playbook with fixed
components, Prerequisites, Workflow, Checklist, Investigation steps [[11]](#ref-11), a shape closer to a
formal investigation procedure than to a lightweight on-call aid.

**The vendor-automation lineage** argues the document itself is a transitional artifact. One vendor frames
the runbook as the manual predecessor its own automation product replaces, *"Replace manual procedures in
your runbooks with automated self-service tasks"* [[14]](#ref-14). A more aggressive version argues static
runbooks are already obsolete, *"Runbooks once worked well. But systems evolved faster than our
documentation could"* [[15]](#ref-15), while conceding automation's own limits, *"Automation often falls
short because it's brittle and struggles to adapt when incidents don't match past patterns"* [[15]](#ref-15).
Both sources sell the thing they argue for; section 6 states that incentive plainly rather than repeating
their numbers.

## 6. Debates and contested boundaries

**General guidance, or step-by-step commands?** Google names this contentious inside its own organisation,
in two consecutive sentences of the same chapter: general playbook entries change slowly, step-by-step
entries reduce variability and drive down MTTR, and *"This is a contentious topic"* [[1]](#ref-1). This
bundle does not pick a side its own primary source refuses to; the template asks the author to state which
they are writing.

**A permanent artifact, or a step toward automation?** The SRE Workbook supports a middle position, automate
the deterministic parts [[1]](#ref-1), which implies the judgment-dependent parts remain a document.
Vendors selling automation argue the whole category is temporary [[14]](#ref-14)[[15]](#ref-15). The
incentive difference is worth stating every time this argument appears: the sources arguing runbooks are
obsolete are also the sources selling what replaces them.

**One incident-scoped procedure, or a whole service-operations manual?** Both shapes have named publishers,
PagerDuty and Skelton Thatcher on one side [[8]](#ref-8)[[13]](#ref-13), Microsoft and Emmer on the other
[[11]](#ref-11)[[12]](#ref-12), and Atlassian publishes two mutually inconsistent templates
[[9]](#ref-9)[[10]](#ref-10). This bundle settles it by the family contract's own definition of a runbook
as a procedure for a known situation, not by weight of sources; see section 4.

**Is "treat runbooks like code" consensus, or an artifact of who was sampled?** Two vendor sources state it
flatly, *"Treat them like code. Store them in a central, version-controlled system like Git or an incident
management platform"* [[21]](#ref-21) and *"Runbooks should be version-controlled alongside your
infrastructure code"* [[20]](#ref-20), and nothing this research read contradicts them. But both sell
adjacent tooling and no primary source states it. Report it as a strong practitioner convention, not as
canon.

**Are a runbook and a standard operating procedure the same thing?** This library's own catalog already
treats SOP as an alias for runbook. A vendor comparison draws a real distinction on predictability, an SOP
covering *"a specific, routine task"* while a runbook covers a broader, more complex process
[[27]](#ref-27). Both the alias and the distinction are defensible; this bundle states both rather than
resolving one into the other.

**Is a disaster recovery plan the same document under another name?** NIST's own definition scopes a DR
plan to *"recovering one or more information systems at an alternate facility in response to a major
hardware or software failure or destruction of facilities"* [[25]](#ref-25), one register above the
single-system procedure this bundle templates. Some vendor material treats "DR plan" and "DR runbook" as
interchangeable regardless. This bundle uses the NIST reading, because it is the primary source, and leaves
the vendor usage unresolved rather than adjudicated.

**Is calendar review sufficient?** One source stacks a quarterly cadence with post-incident triggers without
ranking them [[21]](#ref-21); another offers a 90-day untouched heuristic [[20]](#ref-20). Neither states
the system-change trigger the family contract requires, which is exactly why this bundle's Review Trigger
section goes beyond every source read, and says so rather than presenting the gap as filled.

## 7. Anti-patterns and failure modes

**Silent decay.** *"A runbook does not announce that it has decayed. The decay is silent until the moment of
failure."* [[17]](#ref-17) A runbook can be wrong for months before anyone finds out the hard way.

**Assuming shared context that no longer holds.** *"It assumes the dashboard will be available, the alert
will fire as documented, and the responder will have credentials. None of those assumptions hold reliably
during an incident."* [[17]](#ref-17)

**The wiki-versus-code mismatch.** *"The runbook is in a wiki. The system is in code. The two are maintained
by different processes and often by different people."* [[17]](#ref-17) The runbook and the system it
describes drift apart because nothing forces them to change together.

**Written for yourself, not for the reader.** *"Watch out for the curse of knowledge while writing a
runbook. Users of your runbook may not be aware of details and assumptions that you make in the runbook."*
[[18]](#ref-18) The prescribed test is direct: *"Have newly onboarded folks try out the runbooks. Any
missing context will surface."* [[18]](#ref-18)

**Too many steps in one document.** *"If there are too many steps in your runbook, split them into more
than one."* [[18]](#ref-18) A runbook a responder cannot scan under pressure has failed regardless of how
correct it is.

**Not linked from the thing that triggers it.** *"Alerts should link directly to runbooks."* [[18]](#ref-18)
A correct runbook nobody can find during the incident is functionally the same as no runbook.

**Never updated after the incident that exposed it was wrong.** *"As part of your post-incident activities,
go through the emails, chat logs, tickets logged and update your runbooks as needed."* [[18]](#ref-18)
Google's own maintenance debate assumes this happens and does not name who is responsible for making it
happen, which is exactly the gap this bundle's Review Trigger section addresses.

**Calendar-only review, treated as though it were enough.** Quarterly cadences [[21]](#ref-21) and
untouched-duration heuristics [[20]](#ref-20) both catch staleness eventually; neither catches it at the
moment the system actually changed, which is the gap named in section 6. One practitioner account states
the decay starts immediately, before any calendar has a chance to run: a runbook *"basically gets stale
almost immediately the moment it's published"* [[19]](#ref-19), and periodic manual testing of it is, by
the same account, *"spotty, far from guaranteeing that every operational runbook is relevant and
effective"* [[19]](#ref-19).

**Citing an unmeasured number as though it were measured.** Four separate MTTR figures circulate for this
artifact and none traces to a described method [[29]](#ref-29)[[30]](#ref-30)[[31]](#ref-31). Even Google's
own 3x figure is stated informally rather than as a study [[16]](#ref-16). State the value case honestly,
or cite it as an assertion, not a finding.

## 8. Relationships to other artifacts

**Runbook and playbook.** The canon this bundle traces to uses the two words for the same object and never
contrasts them [[1]](#ref-1)[[7]](#ref-7). Where a source does draw a distinction, it splits on scope rather
than on the word itself: *"runbooks focus on step-by-step procedures for resolving specific incidents"*
while *"playbooks represent a broader strategic document that outlines an organization's overall approach to
handling various situations"* [[24]](#ref-24). That distinction is real where it is drawn, but it is not the
canon's own distinction, which uses both words for one thing.

**Runbook and the service-operations manual.** PagerDuty [[8]](#ref-8) and Skelton Thatcher [[13]](#ref-13)
publish a much larger document under the same name, covering an entire service's overview, deployment,
security, and disaster recovery in one place. That is a different artifact at a different scope, not a
bigger size of this one; this bundle templates the incident-scoped procedure and teaches the larger document
as a boundary rather than shipping it.

**Runbook and standard operating procedure.** Treated as aliases in this library's own catalog, and drawn
apart on a predictability axis elsewhere, an SOP for *"a specific, routine task,"* a runbook for something
more variable and diagnostic [[27]](#ref-27). Both readings appear in section 6.

**Runbook and disaster recovery plan.** NIST scopes a DR plan one register above a runbook, to *"recovering
one or more information systems at an alternate facility"* after a major failure or facility loss
[[25]](#ref-25). A runbook is one operational procedure within that larger recovery effort, not a
replacement for it, though vendor material sometimes treats the two as interchangeable and this research
could not settle that usage (see section 6).

**Runbook and checklist, in the Gawande sense.** A checklist is a smaller thing on purpose: *"The checklist
aims to protect against the fallibility of human memory, distraction under pressure and to highlight the
minimum necessary steps for success."* [[26]](#ref-26) The WHO surgical checklist this genre is best known
for has an evidence base a runbook does not, a measured *"47% reduction in deaths from 1.5% to 0.8%"* and a
*"36% reduction in major complications from 11% to 7%"* [[26]](#ref-26). That evidence belongs to the
checklist literature, not to runbooks; it is cited here as a contrast, not as evidence for this artifact.

**Runbook and knowledge base article.** The distinguishing test is executability, not topic: *"A
troubleshooting article may explain symptoms and possible causes. A runbook must go further"* [[28]](#ref-28)
and, more bluntly, *"'Check the logs and restart the service if needed' is not a runbook"* [[28]](#ref-28).
If a document only explains, it is documentation; if it directs a specific action to a specific trigger, it
is a runbook.

**Runbook and postmortem.** No source this research read contrasts the two directly. Google's own postmortem
definition is retrospective by design, *"a written record of an incident, its impact, the actions taken to
mitigate or resolve it, the root cause(s), and the follow-up actions to prevent the incident from
recurring"* [[23]](#ref-23), written after resolution and blameless by design [[23]](#ref-23). A runbook is
prospective, written and consulted before or during the incident it addresses. That prospective-versus-
retrospective framing is synthesis across the two artifacts' own definitions rather than a source's stated
comparison, and it is labelled as such here because this library ships `incident-postmortem` next and the
two must not be read as overlapping.

## 9. Adaptations

**Security-operations teams** are well served by the fixed four-component shape Microsoft names,
Prerequisites, Workflow, Checklist, Investigation steps [[11]](#ref-11), which maps closely onto this
template's full variant.

**Regulated or audited environments** should treat Validation as an audit trail rather than a formality; the
checklist framing exists specifically because *"this checklist can be helpful in highly regulated
environments to verify what you have done"* [[11]](#ref-11).

**Small or single-team operations** should stay on lean and add Prerequisites and Access only once a second
team, or an on-call rotation wider than the people who wrote the runbook, needs to run it without asking
questions first.

**Teams already investing in automation** should apply the determinism test on a schedule rather than once:
a procedure that has stayed the same, unchanged run after run, is the specific shape the primary source
recommends automating [[1]](#ref-1)[[6]](#ref-6), independent of vendor claims about how fast that
automation pays off [[14]](#ref-14)[[30]](#ref-30).

**Teams under pressure to abandon runbooks for an automation or agentic product** should read the vendor
argument's own concession alongside its pitch: *"Automation often falls short because it's brittle and
struggles to adapt when incidents don't match past patterns"* [[15]](#ref-15). The judgment-dependent cases
Google's own source describes are exactly the cases that argument concedes automation does not yet cover
[[1]](#ref-1)[[15]](#ref-15).

## 10. Worked example

[`runbook_example.md`](runbook_example.md) demonstrates a full-variant runbook for the Saved Views service
at the fictional Acme Analytics, the same service the `sdd` and `test-plan` examples describe, chaining the
`standing-standards` family loosely onto that thread as its own contract expects rather than forcing a
narrative position on a document that belongs to a team, not a moment. It is worth checking three things in
it: that its trigger names one specific alert rather than a general topic, that its Procedure states
plainly whether it is written general or step-by-step and why, and that its Review Trigger names an event
and an owner rather than a calendar date.

---

## References

<a id="ref-1"></a>[1] Google SRE (Betsy Beyer et al., eds.). "[SRE Workbook, Chapter 8: On-Call](https://sre.google/workbook/on-call/)." Google SRE (accessed 2026-08-06). Supports the Google canon's substantive treatment of playbooks: definition, purpose, the MTTR claim, the maintenance debate, and the recommendation to automate deterministic steps. This is the chapter carrying nearly all the load-bearing content this bundle rests on. [primary]

<a id="ref-2"></a>[2] Google SRE (Betsy Beyer et al., eds.). "[SRE Book, Chapter 12: Effective Troubleshooting](https://sre.google/sre-book/effective-troubleshooting/)." Google SRE (accessed 2026-08-06). Supports that the SRE Book proper contains exactly one passing mention of the word "playbook," a linked artifact rather than a discussion of what playbooks are. [primary]

<a id="ref-3"></a>[3] Google SRE (Betsy Beyer et al., eds.). "[SRE Book, Chapter 11: Being On-Call](https://sre.google/sre-book/being-on-call/)." Google SRE (accessed 2026-08-06). Supports the verified absence of both "playbook" and "runbook" in this chapter despite its topic, confirmed by full-text regex over the raw page. [primary]

<a id="ref-4"></a>[4] Google SRE (Betsy Beyer et al., eds.). "[SRE Book, Chapter 13: Emergency Response](https://sre.google/sre-book/emergency-response/)." Google SRE (accessed 2026-08-06). Supports the verified absence of both words in this chapter, confirmed by full-text regex over the raw page. [primary]

<a id="ref-5"></a>[5] Google SRE (Betsy Beyer et al., eds.). "[SRE Book, Chapter 14: Managing Incidents](https://sre.google/sre-book/managing-incidents/)." Google SRE (accessed 2026-08-06). Supports the verified absence of both words in this chapter, which is procedural, roles and communication, rather than artifact-specific. [primary]

<a id="ref-6"></a>[6] Google SRE (Betsy Beyer et al., eds.). "[SRE Book, Chapter 33: Eliminating Toil](https://sre.google/sre-book/eliminating-toil/)." Google SRE (accessed 2026-08-06). Supports the toil framing used for the automation test, and confirms the verified absence of "playbook" and "runbook" in this chapter, so the automation reasoning is drawn from the Workbook, not this chapter directly. [primary]

<a id="ref-7"></a>[7] Google SRE Workbook, Chapter 9: Incident Response, including a PagerDuty case study contributed by PagerDuty staff. "[Incident Response](https://sre.google/workbook/incident-response/)." Google SRE (accessed 2026-08-06). Supports that "runbook" appears exactly three times in this chapter, entirely inside the third-party case study rather than Google's own analytical text, and that Google's own voice here uses "playbooks." [primary]

<a id="ref-8"></a>[8] PagerDuty. "[What is a Runbook?](https://www.pagerduty.com/resources/automation/learn/what-is-a-runbook/)" PagerDuty (accessed 2026-08-06). Supports the seven-section runbook structure attributed by PagerDuty to Tom Limoncelli and a general, non-specific statement that runbooks require constant testing and updating. Vendor content. [vendor]

<a id="ref-9"></a>[9] Atlassian. "[ITSM runbook template](https://www.atlassian.com/software/confluence/templates/itsm-runbook)." Atlassian (accessed 2026-08-06). Supports the named three-section ITSM runbook template: ITSM Architecture, Applications and Known Errors, Troubleshooting Steps. Vendor content, no quotable prose. [vendor]

<a id="ref-10"></a>[10] Atlassian. "[DevOps runbook template](https://www.atlassian.com/software/confluence/templates/devops-runbook)." Atlassian (accessed 2026-08-06). Supports the named three-step DevOps runbook template: system architecture, organize runbook operations, explain runbook procedures. Vendor content, no quotable prose. [vendor]

<a id="ref-11"></a>[11] Microsoft. "[Incident response playbooks](https://learn.microsoft.com/en-us/security/operations/incident-response-playbooks)." Microsoft Learn (accessed 2026-08-06). Supports the four fixed components of a Microsoft security playbook, Prerequisites, Workflow, Checklist, Investigation steps, each quoted in this companion's anatomy section. [primary]

<a id="ref-12"></a>[12] Christian Emmer. "[An Effective Incident Runbook Template](https://emmer.dev/blog/an-effective-incident-runbook-template/)." emmer.dev (accessed 2026-08-06). Supports a named, ordered six-section incident-runbook template, explicitly framed by its author as opinionated and partly optional. Practitioner content. [practitioner]

<a id="ref-13"></a>[13] Skelton Thatcher Consulting (Matthew Skelton). "[run-book-template](https://raw.githubusercontent.com/SkeltonThatcher/run-book-template/master/run-book-template.md)." GitHub (accessed 2026-08-06). Supports the widely referenced community template for a full standing operations manual, 65 ordered headers spanning overview, SLAs, service owner, monitoring, backup, security, and failover. No quotable prose. [practitioner]

<a id="ref-14"></a>[14] PagerDuty. "[Runbook Automation](https://www.pagerduty.com/platform/automation/runbook/)." PagerDuty (accessed 2026-08-06). Supports the vendor framing of runbook automation as a product category that replaces manual runbook steps. Carries specific performance claims that this research could not independently verify; see [[30]](#ref-30). Vendor marketing content. [vendor]

<a id="ref-15"></a>[15] ilert. "[Runbooks are history: Why agentic AI will redefine incident response forever](https://www.ilert.com/blog/runbooks-are-history)." ilert company blog (accessed 2026-08-06). Supports the most aggressive vendor claim found, that static runbooks are obsolete, while also conceding automation's real limits with context and novel incidents. Vendor content selling an agentic-AI incident product. [vendor]

<a id="ref-16"></a>[16] Google SRE (Google). "[SRE Book, Introduction](https://sre.google/sre-book/introduction/)." Google SRE (accessed 2026-08-06). Supports the origin of the widely circulated MTTR statistic for playbooks, a roughly 3x improvement over ad hoc response, stated by Google informally rather than as a described study. [primary]

<a id="ref-17"></a>[17] ekline.io blog. "[Why Your Incident Runbook Lies to You at 3 a.m. (and How to Tell Before the Page Fires)](https://ekline.io/blog/why-your-incident-runbook-lies-to-you-at-3-a-m-and-how-to-tell-before-the-page-fires)." ekline.io (accessed 2026-08-06). Supports the staleness failure mode as silent decay, the shared-context assumptions that fail under pressure, and the wiki-versus-code process mismatch. The author or organization's identity beyond the blog byline could not be independently confirmed; treated as an unaffiliated practitioner blog. [practitioner]

<a id="ref-18"></a>[18] incidenthub.cloud blog. "[The No-Nonsense Guide to Runbook Best Practices](https://blog.incidenthub.cloud/The-No-Nonsense-Guide-to-Runbook-Best-Practices)." incidenthub.cloud (accessed 2026-08-06). Supports the curse-of-knowledge failure mode, the newly-onboarded-reader test, mock incident exercises, splitting overlong runbooks, alert-to-runbook linking, and updating runbooks as a post-incident step. Vendor blog for an incident-management product; its prescriptions read as marketing-adjacent best-practice advice. [vendor]

<a id="ref-19"></a>[19] Boris Dali. "[Your SRE On-Call Runbook Is Already Obsolete. Here's Why That's Not Your Fault](https://medium.com/google-cloud/your-sre-on-call-runbook-is-already-obsolete-heres-why-that-s-not-your-fault-0a82b3b0183c)." Medium / Google Cloud Community, published 2026-04 (accessed 2026-08-06). Supports the staleness problem as decay from the moment of writing, and periodic manual testing as an inconsistent defense against it. Practitioner content. [practitioner]

<a id="ref-20"></a>[20] OneUptime. "[How to Build Alert Runbook Links](https://oneuptime.com/blog/post/2026-01-30-alert-runbook-links/view)." OneUptime, published 2026-01-30 (accessed 2026-08-06). Supports the alert-carries-the-link pattern, a named-owner metadata field, versioning alongside infrastructure code, event-triggered review language, and a numeric 90-day staleness heuristic. Vendor content. [vendor]

<a id="ref-21"></a>[21] Rootly. "[Incident Response Runbooks: Templates, Examples & Guide](https://rootly.com/incident-response/runbooks)." Rootly (accessed 2026-08-06). Supports ownership as an explicit accountability requirement, versioning runbooks like code, a quarterly review cadence, post-mortem-triggered updates, and alert-surfaced discovery. Vendor content. [vendor]

<a id="ref-23"></a>[23] Google SRE (Beyer, Jones, Petoff, Murphy, eds.). "[Postmortem Culture: Learning from Failure](https://sre.google/sre-book/postmortem-culture/)." Site Reliability Engineering, Google SRE (accessed 2026-08-06). Supports the postmortem's own definition, its retrospective and blameless framing, and its trigger criteria, used to state where a postmortem's job begins relative to a runbook's. [primary]

<a id="ref-24"></a>[24] incident.io. "[What are runbooks and how do they fit into the incident management picture?](https://incident.io/blog/what-are-runbooks)" incident.io (accessed 2026-08-06). Supports the runbook-versus-playbook distinction drawn on scope, technical step-by-step against broader strategic response, and a runbook's trigger context. Practitioner content from a vendor in the space. [practitioner]

<a id="ref-25"></a>[25] NIST Computer Security Resource Center. "[disaster recovery plan (DRP)](https://csrc.nist.gov/glossary/term/disaster_recovery_plan)." NIST CSRC Glossary, sourced from NIST SP 800-34 Rev. 1 (accessed 2026-08-06). Supports the disaster-recovery-plan boundary: scoped to recovering information systems at an alternate facility after major failure, one register above the single-system procedures a runbook covers. [primary]

<a id="ref-26"></a>[26] PMC (NIH). "[Peer-reviewed review article on Atul Gawande's The Checklist Manifesto](https://pmc.ncbi.nlm.nih.gov/articles/PMC4953332/)." PMC4953332 (accessed 2026-08-06). Supports the checklist-versus-runbook boundary in the Gawande sense, a minimal memory guard rather than a full procedural walkthrough, and the measured WHO surgical checklist outcomes cited here strictly as a contrast, not as evidence for runbooks. [primary]

<a id="ref-27"></a>[27] Cutover. "[Runbooks vs. Playbooks vs. SOPs: Key Differences](https://cutover.com/blog/differences-runbooks-playbooks-sops)." Cutover company blog (accessed 2026-08-06). Supports a named predictability axis distinguishing standard operating procedures, runbooks and playbooks, used as a corroborating source alongside incident.io. Vendor content. [vendor]

<a id="ref-28"></a>[28] knowledge-base.software. "[Knowledge Base vs Runbook: Troubleshooting, Operations Playbooks, and Incident Response](https://knowledge-base.software/comparison/knowledge-base-vs-runbook/)." knowledge-base.software (accessed 2026-08-06). Supports the runbook-versus-wiki-article boundary: a concrete executable-steps test and an operational-moment test. Vendor or practitioner comparison content. [vendor]

<a id="ref-29"></a>[29] The circulating "Google SRE reports an X percent MTTR improvement from playbooks" claim. **not-retrieved.** No source stating this figure was located anywhere in the seven primary Google pages this research searched, by extraction and by full-text regex, for "playbook" and "runbook." Cited here only to state that no such number exists in the pages read, and that this bundle states no percentage for a runbook's effect on MTTR. No claim in this companion rests on this entry.

<a id="ref-30"></a>[30] Vendor MTTR and cost-reduction figures, PagerDuty's "up to 99% faster" and "reduce support costs by 50%" [[14]](#ref-14), and incident.io's "30-50% MTTR improvement" [[24]](#ref-24). **not-retrieved** as to method. These figures appear on product marketing pages with no visible methodology, sample or comparison group. Cited here only to state that they are marketing claims published by companies selling the product they measure, and that no claim in this companion rests on the numbers themselves.

<a id="ref-31"></a>[31] The circulating IBM incident-response MTTR statistics, a "32% reduction" attributed to a 2023 Security Incident Response Index and a "50% reduction" attributed to a 2024 Security Services Benchmark Report. **not-retrieved.** Neither report was located; the figures appear only in secondary aggregation. Cited here only to state that, together with [[29]](#ref-29) and [[30]](#ref-30), four separate MTTR figures circulate for this artifact and none of them traces to a described method. No claim in this companion rests on this entry.
