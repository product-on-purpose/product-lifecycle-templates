# Companion: The Production Readiness Review

> The deep explainer for the production-readiness-review bundle. Read this to understand what the type
> is, where its name comes from, why the template is shaped the way it is, and where the sources this
> bundle read disagree about it. The short operator card is
> [`production-readiness-review_guide.md`](production-readiness-review_guide.md); a fully worked
> instance is [`production-readiness-review_example.md`](production-readiness-review_example.md).
> Inline citations like [[1]](#ref-1) resolve to the [References](#references) at the bottom, tagged by
> source reliability. This bundle sits in the `standing-standards` family alongside `definition-of-done`,
> `definition-of-ready` and `launch-coordination-checklist`, as a **tool**: a standing checklist a
> reviewing team consults, not a standard the reviewed team is judged against on a cadence.

---

## 1. Orientation

A production readiness review is the checklist a team fills in, and an outside reviewer checks, before
responsibility for a service's production behavior changes hands. Google, which named the type, states
the underlying idea directly: it is "a process that identifies the reliability needs of a service based
on its specific details" [[1]](#ref-1), and "a PRR is considered a prerequisite for an SRE team to accept
responsibility for managing the production aspects of a service" [[1]](#ref-1). Its stated goals are to
"verify that a service meets accepted standards of production setup and operational readiness, and that
service owners are prepared to work with SRE and take advantage of SRE expertise," and to "improve the
reliability of the service in production, and minimize the number and severity of incidents that might be
expected" [[1]](#ref-1).

**At a glance**
- Three bodies actually publish the document itself, not only a description of the practice: Susan
  Fowler's Appendix A [[5]](#ref-5), GitLab's issue template [[6]](#ref-6), and Mercari's four-file
  checklist [[9]](#ref-9)[[10]](#ref-10)[[11]](#ref-11)[[12]](#ref-12).
- Past that shared core, almost everything varies by source: when the review runs, how often it recurs,
  who conducts it, what the outcome is called, and how much depth a given service actually needs.
- The name collides with two unrelated things: a hardware-manufacturing milestone used by NASA and the
  US Department of Defense [[32]](#ref-32)[[33]](#ref-33), and a per-release go-live review run by one
  federal agency [[38]](#ref-38).
- No outcome vocabulary read for this bundle is a published standard. This bundle borrows three of one
  practitioner's four named states and drops the fourth, attributed throughout [[37]](#ref-37).
- It is a review of a service's standing ability to be run, not a review of one specific launch; section
  8 below draws that boundary against the neighboring launch coordination checklist.

If you read nothing else: this is a standing readiness instrument consulted at a handoff or an ownership
change, not a record of one release. What a team fills out for one specific handoff is the record of
applying the instrument, not the instrument itself.

## 2. Origins and evolution

The type's admission source is Chapter 32 of Google's *Site Reliability Engineering*, "The Evolving SRE
Engagement Model," written by Acacio Cruz and Ashish Bhambhani: "the most typical initial step of SRE
engagement is the Production Readiness Review (PRR)" [[1]](#ref-1). The trigger the chapter describes is a
request, not a calendar date: "when a development team requests that SRE take over production management
of a service, SRE gauges both the importance of the service and the availability of SRE teams"
[[1]](#ref-1). The team that runs it is small: "usually one to three SREs are selected or self-nominated to
conduct the PRR process" [[1]](#ref-1), and the review itself is not fixed to one lifecycle moment: "the
Production Readiness Review can be started at any point of the service lifecycle, but the stages at which
SRE engagement is applied have expanded over time" [[1]](#ref-1). The chapter's own domain list names six
areas: "system architecture and interservice dependencies," "instrumentation, metrics, and monitoring,"
"emergency response," "capacity planning," "change management," and "performance: availability, latency,
and efficiency" [[1]](#ref-1). Once a service passes, "an SRE team assumes its production responsibilities"
[[1]](#ref-1), and the improvements a review surfaces are negotiated rather than simply issued: "the
priorities are discussed and negotiated with the development team, and a plan of execution is agreed upon"
[[1]](#ref-1). The chapter also names the model's own limitation candidly: "the main limitations of the PRR
Model stem from the fact that the service is launched and serving at scale, and the SRE engagement starts
very late in the development lifecycle" [[1]](#ref-1), a limitation microservices sharpened further, since
they "imply an expectation of lower lead time for deployment, which was not possible with the previous PRR
model (which had a lead time of months)" [[1]](#ref-1). The same chapter names the Launch Coordination
Engineering team as a separate, related function that "spends a majority of its time consulting with
development teams" [[1]](#ref-1); section 8 below draws the boundary between the two in more detail.

Google's follow-up book confirms the same chapter as the review's own defining source and shows where it
sits in a service's life: "Chapter 32 in our first SRE book describes technical and procedural approaches
that an SRE team can take to analyze and improve the reliability of a service. These strategies include
Production Readiness Reviews (PRRs), early engagement, and continuous improvement" [[2]](#ref-2), and
completing it is framed as a general-availability gate: "in this phase, the service has passed the
Production Readiness Review... and is accepting all users" [[2]](#ref-2). The same book names a sibling
instrument, the Application Readiness Review, whose proposed changes are "prioritized jointly by the
developers and the SREs" alongside a PRR's [[2]](#ref-2). Both books carry the same license: "Copyright ©
2017 Google, Inc." and "Copyright © 2018 Google, Inc.," "Published by O'Reilly Media, Inc. Licensed under CC
BY-NC-ND 4.0" [[1]](#ref-1)[[2]](#ref-2), a no-derivatives license that permits quoting the books directly
but not adapting their wording into this bundle's own template text.

Google itself uses a second name for the review, and adopters outside Google kept the first. Google
Cloud's own customer-reliability-engineering writing calls the same practice an "SRE
entrance review (SER), also referred to as a Production Readiness Review (PRR)," in which "the SRE team
takes the measure of a service currently running in production" [[3]](#ref-3), evaluated across "four main
axes of improvement for a service in an onboarding process: extant bugs, reliability, automation and
monitoring/alerting" [[3]](#ref-3). Grafana Labs, an adopter outside Google, states
its lineage plainly, "production readiness review (PRR) is a process that originated at Google" [[4]](#ref-4),
and describes its own find-then-fix structure: a product-team lead requests a reviewer, the reviewer
attends meetings that sometimes cast the reviewer "in the role of an attacker who tries to break the
system in review," any issues found "are filed as product bugs," and "once the issues have been fixed, the
product has passed the PRR" [[4]](#ref-4). Grafana was, by its own account, reconsidering the review's
one-time design at the time of writing: "we're looking into a periodic and/or incremental PRR as part of
our continuous product improvements" [[4]](#ref-4).

The name also collides with two unrelated practices that predate none of this and share no lineage with
it. NASA's own systems-engineering glossary defines "Production Readiness Review (PRR)" as "a review for
projects developing or acquiring multiple or similar systems greater than three... [that] determines the
readiness of the system developers to efficiently produce the required number of systems" [[32]](#ref-32),
and the US Department of Defense's acquisition literature describes the same hardware milestone,
determining "if a systems design is ready for production and if the system developer has accomplished
adequate production planning to enter Low-Rate Initial Production (LRIP) and Full-Rate Production (FRP),"
judged by a named "Technical Review Chair" [[33]](#ref-33). Neither source is read here as related to the
SRE-lineage review; the shared name is coincidence, not shared descent. A third, more recent collision
comes from Federal Student Aid's own process, which uses the name "Production Readiness Review (PRR)" for
a review run before every release rather than before a standing handoff [[38]](#ref-38); section 8 states
what this bundle takes from that source and what it deliberately leaves out.

One more thread of the origin story is a caution rather than a lineage: GitLab published a Production
Readiness issue template with three maturity gates [[6]](#ref-6), but its own README now states plainly
that "this project is archived and preserved for historical reference only. No new reviews should be
opened here," because "the readiness process has been consolidated into PREP (Platform Readiness
Enablement Process)" [[7]](#ref-7). A separate, current Runway platform page directs readers to "create an
issue using Runway template in the readiness project" [[8]](#ref-8), which contradicts the README's
archived status. This bundle follows the README [[7]](#ref-7) and treats GitLab's template as a historical
artifact of the type's structure rather than as current practice. GitLab's own project metadata records no
license at all [[16]](#ref-16), a second reason this bundle only quotes it rather than adapting its wording.

## 3. Anatomy (section by section)

The full variant carries eight sections; the lean variant carries five of them, unchanged in name and
order, so lean is a strict ordered subset of full: Scope and Trigger, Readiness Criteria, Not-Applicable
Rule, Outcome and Sign-off, and Review Trigger. Full adds Reviewer and Authority, Review Cadence, and When
This Does Not Apply.

### Scope and Trigger (lean and full)

What "production" means for this review, which service or services it covers, what event starts a review,
and what this review deliberately does not cover.

No source read for this bundle agrees on what starts a review. Google's own account is a request: "when a
development team requests that SRE take over production management of a service, SRE gauges both the
importance of the service and the availability of SRE teams" [[1]](#ref-1). Mercari's is a hard gate before
traffic: its check "is required for all services before receiving real production traffic" [[9]](#ref-9).
GitLab's is a maturity level: "it is only required to fill in the items up to and including the
corresponding maturity level and lower" [[6]](#ref-6). AWS's ORR practice ties the trigger to a proposal
rather than a running service at all: "the ORR Lifecycle for New Service and Iterations is initiated when a
new service, new feature, or architecture change is proposed" [[21]](#ref-21). Federal Student Aid ties it
to a release [[38]](#ref-38). Because no trigger read here is universal, this section asks the reviewing
team to name its own trigger rather than adopting any one source's. It is also the section this bundle uses
to name the two unrelated hardware-milestone uses of the same name, so a reader who has met "Production
Readiness Review" in an aerospace or defense context does not assume the same document [[32]](#ref-32)
[[33]](#ref-33).

The section also names what this review deliberately leaves out and where that is reviewed instead,
following a personal ORR template's own explicit exclusion: "_NOTE: Security must have its own, in-depth,
review._" [[39]](#ref-39).

Beginner note: state plainly what "production" and "this service" mean for your context, pick the trigger
that actually matches how your review gets started, and name at least one thing this review is not the
place to assess. Expert note: if your team's real trigger does not match any of the five read here, write
your own rather than forcing a fit; the disagreement among sources is evidence that no single trigger is
authoritative.

### Reviewer and Authority (full only)

Who conducts the review, and who decides when a finding is serious enough to block.

Two camps disagree on who should even hold the checklist, and the disagreement is not between strangers.
Pedro Alves argues for an outside reviewer: "to maximise the potential to identify risks, and remove
biases, reviewers should be external to the team," with "two reviewers" as "the sweet spot" [[34]](#ref-34).
Alves's own article was shepherded for publication by Laura Nolan [[34]](#ref-34), whose own talk argues
close to the opposite: "the team themselves should be the ones who define what their criteria are for
production readiness, because they know that software best" [[35]](#ref-35). Grafana's practice sides with
Alves, seeking "an experienced engineer, ideally outside of the product team" [[4]](#ref-4); Mercari's sides
with Nolan, asking the reviewed team to "verify if each item is satisfied or not by your own team"
[[9]](#ref-9); and AWS's ORR practice sits between the two, running self-assessments that are then "reviewed
during a scheduled meeting with an audience including the engineering team, principal engineers in their
organization, leadership and management, and any stakeholders from dependencies or customers of the
service" [[17]](#ref-17)[[22]](#ref-22).

Who decides when a finding blocks is equally unsettled. AWS escalates by criticality: "any high-criticality
findings are escalated to leadership as input to a go or no-go launch decision" [[22]](#ref-22). Microsoft's
Azure Well-Architected guidance names a single accountable role instead: "the directly responsible
individual (DRI) should make the final decisions with input from key stakeholders and technical
decision-makers" [[25]](#ref-25). Federal Student Aid raises the required signatory with the release's own
risk: "based on the operational risk factors for the release, the CTO Enterprise Architecture and IT
Planning Branch will indicate if additional sign-off by FSA Senior Management is required" [[38]](#ref-38).
Alves leaves the choice to the team being reviewed: "it is generally up to the development team to decide
whether and how to follow up on those risks" [[34]](#ref-34). One vendor's evidence-and-gates model separates
the two roles explicitly: "the service owner owns readiness. Reviewers challenge evidence and apply policy;
they should not become the default owners of every remediation item. An approval meeting with no
accountable service owner is itself a readiness gap" [[37]](#ref-37).

Beginner note: name the reviewer or reviewers, name who the reviewed team is, and name who is authorized to
say a finding blocks. Expert note: if your riskiest reviews and your routine ones escalate to the same
person regardless of risk, Federal Student Aid's risk-scaled signatory is worth borrowing even where the
rest of that source's content is not [[38]](#ref-38).

### Readiness Criteria (lean and full, the load-bearing table)

Criteria grouped by domain, each carrying the evidence that answers it, an owner, and a status.

No single source's domain list was taken wholesale; the starting set here is drawn across sources rather
than from any one taxonomy. Monitoring appears as a heading in Google's list, Fowler's, GitLab's, and
Mercari's [[1]](#ref-1)[[5]](#ref-5)[[6]](#ref-6)[[12]](#ref-12); capacity or performance in Google's,
Fowler's, and GitLab's [[1]](#ref-1)[[5]](#ref-5)[[6]](#ref-6); architecture and dependencies in Google's and
AWS's [[1]](#ref-1)[[20]](#ref-20); change or deployment in Google's, GitLab's, and AWS's [[1]](#ref-1)
[[6]](#ref-6)[[20]](#ref-20); emergency response or event management in Google's, Fowler's, and AWS's
[[1]](#ref-1)[[5]](#ref-5)[[20]](#ref-20); security in GitLab's, Mercari's design checklist, Mercari's
pre-production checklist, and Google's own launch checklist [[6]](#ref-6)[[11]](#ref-11)[[12]](#ref-12)
[[28]](#ref-28); data recovery in GitLab's, Mercari's, and AWS's [[6]](#ref-6)[[12]](#ref-12)[[20]](#ref-20);
and documentation in Fowler's and inside Mercari's own Accessibility section [[5]](#ref-5)[[12]](#ref-12).

The evidence-and-status mechanics are sourced to Mercari specifically, which is MIT-licensed
[[14]](#ref-14)[[15]](#ref-15) and so may be adapted with attribution rather than only quoted: "if it is satisfied, check the item in the
list and provide evidence (e.g. links to tickets, screenshots, documents, test results, ...) showing that
it is satisfied" [[9]](#ref-9). A full-size table may add whether a criterion blocks outright, following the
distinction that "not all issues are blockers to SRE takeover" [[3]](#ref-3) and one vendor's three-level
gate model, "blocking... conditional... advisory" [[37]](#ref-37), and the tier that requires it, following
GitLab's maturity gates [[6]](#ref-6) and Mercari's own service-level basis, "the main factor of choosing a
Service Level is the expected SLO" [[13]](#ref-13). The questions used to draft or challenge a row may
include a personal ORR template's own worry-elicitation question, "what are you worried about?"
[[39]](#ref-39).

Beginner note: for each criterion, name the evidence that would actually satisfy it, not a bare
confirmation, name who owns producing that evidence, and record its current status honestly. Expert note:
resist copying one source's domain list wholesale; the disagreement across sources (section 6) means the
right set of domains is the one that matches what has actually gone wrong for your own service.

### Not-Applicable Rule (lean and full)

An item marked not applicable carries a written reason, never a bare mark.

This rule is sourced three times independently. GitLab: "leave all non-applicable items intact and add
'N/A' or reasons for why in place of the response" [[6]](#ref-6). Mercari, MIT-licensed and adaptable with
attribution: "if a specific item is not applicable to your service check the item and explain, as evidence,
why it's not applicable" [[9]](#ref-9)[[14]](#ref-14). Federal Student Aid states the same rule as a
prohibition: "no item in the PRR should only be marked "N/A" or "Not Applicable;" instead an explanation
should be provided as to why a particular item does not apply" [[38]](#ref-38).

Beginner note: never leave a checkbox marked N/A with nothing beside it; write the one line that explains
why the item does not apply to this service. Expert note: an unexplained N/A and a skipped item are
indistinguishable to a later reader, which is exactly what this rule exists to prevent.

### Outcome and Sign-off (lean and full, a table section)

The outcome, the findings not met, and who signed.

No outcome vocabulary read for this bundle is an industry standard. One practitioner's own four-state model
says so directly: "these states are a recommended governance model, not a Google, AWS, or Kubernetes
platform behavior" [[37]](#ref-37). A vendor's own model is a plain binary instead: "criteria are either
passed or flagged for follow-up" [[36]](#ref-36). This bundle's template borrows three of that four-state
model's states, "ready with conditions" [[37]](#ref-37) and "not ready" [[37]](#ref-37), alongside an
unconditional ready state, and drops the fourth, "withdrawn" [[37]](#ref-37), which concerns a launch whose
scope or date moved rather than a service's own readiness.

Each finding not met carries its own record. Alves: "that list should include: what risks were identified;
their criticality; recommendations on how to address the risk" [[34]](#ref-34). The same vendor's four-state
model states the fuller record: "for each finding, capture: severity and customer or business consequence;
exact affected scope; evidence that produced the finding; remediation and named owner; due date and
verification method; whether it blocks launch; exception record, if the risk is accepted temporarily"
[[37]](#ref-37). A condition accepted at sign-off is listed, owned, and dated rather than implied: Federal
Student Aid states plainly that "when FSA Management signs-off on the PRR, they are approving implementation
even with the issues listed" [[38]](#ref-38), and a vendor's exception workflow ties the same idea to a
deadline, "teams can ship on time while staying accountable for closing gaps after launch, which prevents
exceptions from becoming permanent technical debt" [[36]](#ref-36).

The template's Outcome and Sign-off section records who signed and in what role, not what each signature
certifies. Federal Student Aid differentiates its own signatories by what each one attests to
[[38]](#ref-38). This bundle carries that distinction into neither a template field nor the guide's
rubric; a team whose signatories attest to different things can add the column.

TRAP: an empty findings list read as an all-clear. Federal Student Aid's own instruction guards against
exactly this: "if no risks are identified, then the IPT should indicate "No Risks Identified" in the first
row of the risk table - there are always unknown risks" [[38]](#ref-38).

Beginner note: write the outcome, list every finding with its owner and date even when a condition has been
accepted, and never leave the findings table blank without writing "no risks identified" explicitly. Expert
note: a blank findings row is not the same claim as a row that states no risks were identified; the second
is a decision someone made and can be held to, the first is silence.

### Review Cadence (full only)

Whether this review is repeated for a service that has already passed once, and on what schedule.

Four camps disagree, and none is universal. One-time: Google's original account has an SRE team assume
responsibility "after sufficient improvements are made and the service is deemed ready for SRE support"
[[1]](#ref-1), and Grafana's early practice reads "once the issues have been fixed, the product has passed
the PRR" [[4]](#ref-4), though Grafana was reconsidering that design even as it wrote it down, "we're looking
into a periodic and/or incremental PRR" [[4]](#ref-4). Event-driven plus a fixed annual floor: AWS requires
that "at least annually, teams are expected to perform an ORR on their full service using a checklist
tailored to that event" [[21]](#ref-21), a cadence its own whitepaper frames as a mechanism rather than a
one-off audit, since "the cyclic nature of a mechanism makes it best suited for solving recurring problems
or opportunities, as opposed to one-off challenges" [[18]](#ref-18), consisting of "a tool that builders are
driven to adopt, and then the results of the process are inspected... the mechanism is iterated and
improved upon" [[24]](#ref-24). Continuous, tied to every deployment: Azure's operational-excellence guidance
gates every release promotion through staged approvals [[25]](#ref-25), and Cortex's Scorecards can "block
deployment based on Scorecard scores" on every attempt [[27]](#ref-27). Staged across the whole lifecycle
rather than fixed to any single cadence: a personal ORR template states the design goal outright, "the key
is making ORR a continuous exercise rather than a one-time checklist" [[39]](#ref-39).

Beginner note: pick one of the four camps deliberately and write down why, rather than defaulting to
silence on cadence. Expert note: a one-time review is defensible for a first handoff, but if your team has
never revisited a passed review, that absence is itself worth naming rather than leaving unstated.

### When This Does Not Apply (full only)

Which services get a lighter check, and what that lighter check actually contains.

No source read for this bundle exempts a service from review outright; every source that speaks to scaling
depth scales the review instead of skipping it. GitLab scales per section by maturity gate [[6]](#ref-6).
Mercari scales per row by service level, chosen from the service's own target SLO: "the main factor of
choosing a Service Level is the expected SLO" [[13]](#ref-13), and its own tiering is not strictly
monotonic; a "Manual Scale" row a lower level requires is replaced rather than kept once "Auto Scale" is
required at a higher one [[12]](#ref-12). AWS scales per occasion and workload type: "AWS uses different
checklists for different occasions and workload types" [[21]](#ref-21), and deliberately keeps lesser risks
out of the list at all in order to stay usable: "medium or low risks aren't included in the ORR to keep it a
lightweight process that doesn't overburden teams and reduce their agility and ability to innovate"
[[20]](#ref-20). Even at its lightest, a review that has actually run is still a review: Laura Nolan
describes having "seen people do PRRs that just consisted of filling in a template document over a couple
of hours" [[35]](#ref-35), which is minimal, not absent.

TRAP: treating any of this as license for a blanket exemption. No source read here supports one.

Beginner note: name which of your services would use the lighter path, and write down what that lighter
path still requires rather than what it skips. Expert note: if a service has never gone through even the
lightest version of this review, that is a gap to name, not a category to invent.

### Review Trigger (lean and full, contract-mandated)

What event makes this checklist itself wrong, and who is expected to notice.

No structural source read for this bundle publishes a section with this name or job; it is required
directly by the `standing-standards` family contract rather than volunteered by any source, and this bundle
labels it as its own contribution the way its sibling bundles in the same family label theirs (see
[`standing-standards.md`](../../docs/internal/contracts/standing-standards.md)). Here, unlike the family's
first two members, a condition for revising the checklist is genuinely sourced rather than supplied by the
library alone. AWS names three sources for a new question: "real incidents that you've had in the past,"
"near-misses that you've had in the past," and "the failure modes that haven't occurred, but that you're
concerned about" [[20]](#ref-20), and ties incident review directly to the checklist through a named
question, "would any ORR recommendations have reduced or avoided the impact of this event?" [[22]](#ref-22),
curated by a standing role, the "Ops Champion," who "challenges the team on their answers to the
checklist" and "ends up influencing everything from workload architecture to operational culture in the
team" [[23]](#ref-23). One vendor's evidence-and-gates model tempers how loosely that trigger should be
read: "do not add a question merely because something once went wrong. State the failure it prevents, the
evidence that answers it, and the launch types for which it applies" [[37]](#ref-37).

Beginner note: name the specific kind of event, an incident, a near miss, or a named worry that turned out
to be real, that would make you revise this checklist, and name who owns noticing it. Expert note: when an
incident does prompt a change here, name which criterion should have caught it and why it did not, before
deciding the fix is a new row rather than something else entirely.

## 4. Variants and sizing

**Lean (five sections)** is Scope and Trigger, Readiness Criteria, Not-Applicable Rule, Outcome and
Sign-off, and Review Trigger. It carries the load-bearing table, the two rules that keep it honest, the
recorded outcome, and the standing checklist's own staleness trigger, which the family contract requires of
every member regardless of size. At its lightest, this is still a genuine review, matching the couple-hours
version Laura Nolan describes having seen [[35]](#ref-35), not an exemption from one.

**Full (eight sections)** adds Reviewer and Authority, Review Cadence, and When This Does Not Apply. All
three become worth their own section once a review program serves more than one service: naming a reviewer
and an escalation path matters once more than one plausible reviewer exists, a cadence commitment matters
once a service is expected to be reviewed more than once, and a documented lighter path matters once the
program covers enough services that treating all of them identically would be its own failure mode, the
one AWS's own scope-limiting design and Mercari's tiered service levels both guard against
[[13]](#ref-13)[[20]](#ref-20).

## 5. Methodology lineage

**The SRE lineage is load-bearing.** The type's origin, its trigger, its team size, its domain list, and
its own stated limitation all come from Google's account of the Evolving SRE Engagement Model
[[1]](#ref-1), confirmed and extended by its own follow-up book [[2]](#ref-2), and independently
corroborated under a different name by Google Cloud's customer-reliability-engineering writing
[[3]](#ref-3).

**An independent-adopter lineage** shows the practice surviving outside Google entirely, with its own
process shape and its own doubts about a one-time design: "production readiness review (PRR) is a process
that originated at Google," fitted to a reviewer-from-outside-the-team model and later reconsidered for
cadence [[4]](#ref-4).

**The AWS Operational Readiness Review lineage** treats readiness as a recurring mechanism rather than a
discrete audit. Its own stated purpose is incident-driven: AWS "created the Operational Readiness Review
(ORR) to distill the learnings from AWS operational incidents into curated questions with best practice
guidance" [[17]](#ref-17), aimed at "decreasing the frequency of incidents (fewer), decreasing the duration
of incidents (shorter), and decreasing the scope of impact of an incident (smaller)" [[19]](#ref-19), run on
a cycle of adoption, inspection, and iteration [[18]](#ref-18)[[24]](#ref-24), embedded across the whole
lifecycle rather than only pre-launch [[21]](#ref-21), and curated by a named role rather than left to drift
[[23]](#ref-23).

**The Azure Well-Architected lineage** treats readiness as a release-control protocol rather than a
periodic review: "release promotion" moves a change "through various stages with quality gates," and
"the directly responsible individual (DRI) should make the final decisions with input from key
stakeholders and technical decision-makers" [[25]](#ref-25), against a flat, numbered checklist of
recommendations rather than one grouped by topic area, down to a named deployment-safety item, "clearly
define your workload's safe deployment practices" [[26]](#ref-26).

**A vendor Scorecard lineage** reframes readiness as a continuously computed, tiered score rather than a
review event at all: Cortex's Scorecards check "criteria such as ownership, on-call coverage, runbooks,
monitoring, and security requirements," structured into "three levels - Bronze, Silver, and Gold," which a
deployment Workflow can gate on directly [[27]](#ref-27).

**A practitioner running-the-review lineage** argues from direct experience rather than from a published
framework: Pedro Alves's account of reviewer selection, goal-setting, and follow-up ownership
[[34]](#ref-34), and Laura Nolan's talk arguing for team ownership of the criteria and naming named
antipatterns [[35]](#ref-35).

**A vendor evidence-and-gates lineage** formalizes the outcome itself: Cortex's own account of a
cross-functional walkthrough with exception tracking [[36]](#ref-36), and a four-state governance model with
a named risk-tiered gate structure, both explicitly prescriptive rather than a record of observed practice
[[37]](#ref-37).

**A federal, per-release lineage** uses the same name for a different moment: Federal Student Aid's process
runs before every release, carries a risk-scaled signatory and a rule against bare N/A marks that this
bundle borrows, and carries release-moment content, rollback activation criteria, the business cost of
delay, a post-implementation configuration check, and a workforce-relations review, that this bundle
deliberately leaves to `launch-coordination-checklist` and `runbook` instead [[38]](#ref-38).

**A hardware and defense lineage** shares the name and nothing else: NASA's and the Department of Defense's
Production Readiness Review governs whether a manufacturer is ready to produce hardware at scale, judged by
production planning and supplier management rather than service reliability [[32]](#ref-32)[[33]](#ref-33).

**A personal, community ORR lineage** states its own limits openly, "this is not THE template - it is A
template" [[39]](#ref-39), and contributes the worry-elicitation questions and the continuous-cadence
argument this bundle draws on for Readiness Criteria and Review Cadence.

## 6. Debates and contested boundaries

**What starts a review?** Google's is a request from the owning team [[1]](#ref-1); Mercari's is a hard gate
before traffic [[9]](#ref-9); GitLab's is a maturity level [[6]](#ref-6); AWS's is a proposed change
[[21]](#ref-21); Federal Student Aid's is a release [[38]](#ref-38). No trigger read here is universal, so
Scope and Trigger asks the team to name its own rather than adopting one source's answer.

**How often does it recur?** One-time in Google's and early Grafana practice [[1]](#ref-1)[[4]](#ref-4);
event-driven plus an annual floor in AWS's [[21]](#ref-21); continuous, tied to every deployment, in Azure's
and Cortex's [[25]](#ref-25)[[27]](#ref-27); staged across the whole lifecycle in a personal ORR template's
[[39]](#ref-39). Four camps, no consensus; Review Cadence asks the team to take a position and say why.

**Who reviews?** Alves and a shepherded Nolan disagree inside the same publication relationship: Alves
argues for reviewers "external to the team" [[34]](#ref-34), while the article was shepherded for
publication by Nolan, whose own talk argues the reviewed team should define its own criteria "because they
know that software best" [[35]](#ref-35). Grafana sides with Alves [[4]](#ref-4); Mercari sides with Nolan
[[9]](#ref-9); AWS runs self-assessments reviewed at a meeting, which is neither camp cleanly
[[17]](#ref-17)[[22]](#ref-22).

**What is the outcome called?** One practitioner's four states are explicitly "a recommended governance
model, not a Google, AWS, or Kubernetes platform behavior" [[37]](#ref-37); a vendor's is a binary
[[36]](#ref-36); Google Cloud's writing asks only that the review "state clearly whether the service merits
SRE takeover, and if so, why (or why not)" [[3]](#ref-3), naming no fixed vocabulary at all. No vocabulary
read here is standard; this bundle attributes the one it borrows.

**Who decides a blocking finding?** AWS escalates by criticality to leadership [[22]](#ref-22); Azure names
a single DRI [[25]](#ref-25); Federal Student Aid raises the required signatory with the release's own risk
[[38]](#ref-38); Alves leaves follow-up to the reviewed team itself [[34]](#ref-34).

**Does every finding block?** No. Google Cloud's own writing states "not all issues are blockers to SRE
takeover" [[3]](#ref-3); AWS keeps lesser risks out of the checklist entirely to stay lightweight
[[20]](#ref-20); one vendor's model grades findings into "blocking... conditional... advisory"
[[37]](#ref-37).

**How is depth tiered?** By section and maturity gate in GitLab's [[6]](#ref-6); by row and target SLO in
Mercari's [[13]](#ref-13); by occasion and workload type in AWS's [[21]](#ref-21). Section 3's When This
Does Not Apply anatomy carries the detail; no source scales depth to zero.

**Is GitLab's own process still live?** Its README says no: "this project is archived and preserved for
historical reference only" [[7]](#ref-7); a separate current page directs readers to file a new issue in
the same project [[8]](#ref-8), contradicting the README. This bundle follows the README.

**What is the review even called?** "SRE entrance review (SER), also referred to as a Production Readiness
Review (PRR)" at Google Cloud [[3]](#ref-3); "Production Readiness Check (PRC)" at Mercari [[9]](#ref-9);
"Operational Readiness Review" at AWS [[17]](#ref-17), which frames ORR as "a complementary process to
Well-Architected," never as complementary to a PRR [[17]](#ref-17); and a hardware-manufacturing milestone
under the identical name at NASA and the Department of Defense [[32]](#ref-32)[[33]](#ref-33).

**Where is the boundary with the launch coordination checklist?** Google's own two chapters separate them
by trigger and object: this review starts when a team asks SRE to take over a running service
[[1]](#ref-1), while "most audits are conducted before a new product or service launches" [[29]](#ref-29).
Adopters blur that trigger in practice: Mercari requires its check "for all services before receiving real
production traffic" [[9]](#ref-9), GitLab gates each maturity level of a new service [[6]](#ref-6), and
Federal Student Aid runs its own PRR on every release [[38]](#ref-38). What holds across every source read
here is the object rather than the trigger: this review asks whether a service can be run on a standing
basis, "required for all services" [[9]](#ref-9), while the launch checklist asks whether one launch is
ready. That reading is this library's own, drawn from the sources' wording rather than stated outright by
any one of them.

**What domains belong on the criteria table?** No two sources agree on a taxonomy. Monitoring, capacity,
and change management recur across several sources; security, data recovery, and documentation recur across
a different, overlapping set (see section 3's Readiness Criteria anatomy for the full breakdown). This
bundle's domain list is a starting point built across sources, not a copy of any one of them.

## 7. Anti-patterns and failure modes

**Engagement that starts too late to change the design.** Google names this as the model's own stated
limitation: "the main limitations of the PRR Model stem from the fact that the service is launched and
serving at scale, and the SRE engagement starts very late in the development lifecycle" [[1]](#ref-1).

**No stated goal, so no priority.** "Running a PRR without any specific goal means that the PRR can drop to
the bottom of the development team's priority list" [[34]](#ref-34).

**A defensive reviewed team that hides risk.** "If the development team feels threatened by the review, or
that the team itself is under review, they can go on the defensive, and actively hide any potential risk in
the system" [[34]](#ref-34).

**A template too heavy to actually fill in.** "Keep the template current, relevant, usable, and no more
complex than absolutely necessary" [[34]](#ref-34).

**Shallowness that substitutes for the reviewed team's own attention.** "You can't do another team's PRR
for them" [[35]](#ref-35).

**The template treated as an inflexible rule.** "We should not build a PRR template and then make that a
hard and fast rule, like a set of hoops that a team has to jump through to launch their service"
[[35]](#ref-35).

**Forgetting the humans.** "This is one of the biggest antipatterns: forgetting the humans" [[35]](#ref-35);
the value of the review is the time the owning team spends with its own system, not the filled-in form
itself.

**Drift after a one-time review.** A personal ORR template names this outright as the reason to repeat the
exercise: run it "periodically (approximately once per year) - ensure operations haven't drifted but
improved over time" [[39]](#ref-39), echoed by AWS's own annual floor [[21]](#ref-21) and by Grafana's stated
reconsideration of its one-time design [[4]](#ref-4).

## 8. Relationships to other artifacts

**Production readiness review and launch coordination checklist.** The two share a founding source and a
loose lineage, since Google's Launch Engineers' "consulting sessions were formalized as Production Reviews"
[[29]](#ref-29), but they answer different questions: this review asks whether a service can be run on a
standing basis, the launch checklist asks whether one specific launch is ready, drawing on domains such as
"architecture," "security," and "schedule and rollout planning" that name no marketing, legal, or pricing
concern of their own [[28]](#ref-28). The Launch Coordination Engineering team's role is explicitly
cross-functional even where the checklist itself is not: "as a nonpartisan advisor, an LCE plays a
balancing and mediating role between stakeholders including SRE, product developers, product managers, and
marketing" [[29]](#ref-29).

**Production readiness review and the Federal Student Aid process of the same name.** This bundle admits
only four elements from that source: evidence for each criterion, a written reason for every not-applicable
answer, a sign-off that names the open issues it accepts, and a signatory that rises with risk
[[38]](#ref-38). Its release-moment content, rollback activation criteria, the business cost of delay, a
post-implementation configuration check, and a workforce-relations review, belongs to the release itself
rather than to a service's standing readiness, and is left to `launch-coordination-checklist` and `runbook`
instead.

**Production readiness review and Operational Readiness Review.** AWS's own ORR is this document's closest
cross-vendor analog under a different name, but AWS never calls its own practice a PRR: it names ORR "a
complementary process to Well-Architected," never as complementary to a Production Readiness Review
[[17]](#ref-17).

**Production readiness review and definition of done.** A definition of done governs an Increment of work,
not a service: "the Definition of Done is a formal description of the state of the Increment when it meets
the quality measures required for the product," and "the Developers are required to conform to the
Definition of Done" [[30]](#ref-30). The two are `standing-standards` siblings judged against different
objects, one an increment of work, the other a running service.

**Production readiness review and the change advisory board.** A CAB reviews a requested change, not a
service's standing readiness: it "delivers support to a change-management team by advising on requested
changes, assisting in the assessment and prioritization of changes" [[31]](#ref-31).

**Production readiness review and runbook.** Every published checklist read here checks that a runbook
exists; none of them produces one. Fowler: "instructions on how to triage, mitigate, and resolve the alert
should also be added to the service's on-call runbook" [[5]](#ref-5). GitLab: "link to the troubleshooting
runbooks" [[6]](#ref-6). Mercari: "it has OnCall playbooks" [[12]](#ref-12). Cortex: Scorecards check
"criteria such as ownership, on-call coverage, runbooks, monitoring, and security requirements"
[[27]](#ref-27). A personal ORR template asks directly, "when did you last execute each runbook end-to-end?"
[[39]](#ref-39).

**Production readiness review and the hardware-manufacturing milestone of the same name.** NASA's and the
Department of Defense's Production Readiness Review governs whether a manufacturer is ready to produce
hardware at scale [[32]](#ref-32)[[33]](#ref-33). This bundle claims no shared lineage between the two, only
a shared, coincidental name.

## 9. Adaptations

**Regulated or high-risk contexts** can borrow Federal Student Aid's risk-scaled signatory directly even
where the rest of that source's content is left to other document types: "based on the operational risk
factors for the release... additional sign-off by FSA Senior Management is required" [[38]](#ref-38).

**Very small reviews** can be genuinely light without becoming absent. Laura Nolan describes having "seen
people do PRRs that just consisted of filling in a template document over a couple of hours" [[35]](#ref-35).
Where the service is instead critical or complex, Nolan's own recommendation runs the other way, embedding a
reviewer with the team for "a quarter or maybe two quarters, or maybe longer depending on the size and the
complexity and the criticality of it" [[35]](#ref-35), and stating a floor even for the ordinary case: "for
any complex or critical service, I think a PRR should take at least one person a quarter" [[35]](#ref-35).

**Organizations that want the review continuously re-evaluated rather than run once** can adopt Cortex's
Scorecard model, tiered into "Bronze, Silver, and Gold," gating deployment automatically rather than through
a discrete review event [[27]](#ref-27).

**Service type should tailor which criteria matter, not just how deep the review goes.** A vendor's own
guidance states this directly: "what matters for a customer-facing API is different from what matters for
an internal batch job. Your checklist should be tailored to the type of service being launched while still
maintaining organizational consistency" [[36]](#ref-36), and a separate source states the cost of not doing
so: "requiring the same evidence from a text-only user-interface change and a cross-region data migration
makes teams route around the process" [[37]](#ref-37).

## 10. Worked example

[`production-readiness-review_example.md`](production-readiness-review_example.md) demonstrates a
full-variant review as Acme Analytics' newly formed SRE function runs it against `dashboard-service`,
owned by the Reporting team, deciding whether SRE accepts standing production ownership. It is worth
checking three things in it: that its Reviewer and Authority section states, rather than leaves implied,
why its two reviewers were chosen; that its Outcome and Sign-off section records a "ready with conditions"
outcome with every condition owned and dated rather than left open; and that it names no launch's own
build or release number, since this review is a service's own readiness rather than a launch's.

---

## References

<a id="ref-1"></a>[1] Acacio Cruz and Ashish Bhambhani, "[The Evolving SRE Engagement
Model](https://sre.google/sre-book/evolving-sre-engagement-model/)," chapter 32 of Google, *Site
Reliability Engineering* (O'Reilly Media; web edition at sre.google, copyright 2017 Google) (accessed
2026-09-28). Supports the type's definition, goals, trigger, team, timing, evaluation-domain list, outcome
mechanics, and stated model limitations. The most heavily cited source in this bundle. [primary]

<a id="ref-2"></a>[2] Michael Wildpaner, Gráinne Sheerin, Daniel Rogers, and Surya Prashanth Sanagavarapu,
with Adrian Hilton and Shylaja Nukala, "[SRE Engagement Model](https://sre.google/workbook/engagement-model/),"
chapter 18 of Google, *The Site Reliability Workbook* (O'Reilly Media; web edition at sre.google, copyright
2018 Google) (accessed 2026-09-28). Supports chapter 32 as the review's own defining source, the sibling
Application Readiness Review, and the general-availability gate framing. [primary]

<a id="ref-3"></a>[3] Adrian Hilton et al., "[How SREs at Google find the landmines in a
service](https://cloud.google.com/blog/products/gcp/how-sres-find-the-landmines-in-a-service-cre-life-lessons/),"
Google Cloud CRE Life Lessons, part 2 (accessed 2026-09-28). Supports an independent definition under the
name SER/PRR, its four evaluation axes, and its rule that not every finding blocks. [vendor]

<a id="ref-4"></a>[4] Grafana Labs, "[How we're building a production readiness review process at Grafana
Labs](https://grafana.com/blog/2021/10/13/how-were-building-a-production-readiness-review-process-at-grafana-labs/),"
company blog, 2021 (accessed 2026-09-28). Supports an independent adopter's outside-reviewer model, its
find-then-fix process, and its own stated reconsideration of a one-time cadence. [practitioner]

<a id="ref-5"></a>[5] Susan Fowler, *Production-Ready Microservices* (O'Reilly, 2016), Appendix A, via the
F5-sponsored free-chapters excerpt
(`https://cdn.studio.f5.com/files/k6fem79d/production/fa24cb335b342add5e3b21a77efaa71462e7d6de.pdf`)
(accessed 2026-09-28). Supports a five-pillar published checklist structure and the runbook-linked alerting
rule. Proprietary, no open license. [primary]

<a id="ref-6"></a>[6] GitLab Inc., "[production_readiness.md issue
template](https://gitlab.com/gitlab-com/gl-infra/readiness/-/raw/master/.gitlab/issue_templates/production_readiness.md),"
gl-infra/readiness project (archived) (accessed 2026-09-28). Supports the three-gate maturity structure, the
not-applicable rule, and per-gate reviewer roles. [primary]

<a id="ref-7"></a>[7] GitLab Inc., "[gl-infra/readiness
README](https://gitlab.com/gitlab-com/gl-infra/readiness/-/raw/master/README.md)" (archived) (accessed
2026-09-28). Supports that the project is archived and superseded by PREP, which this bundle follows over
[[8]](#ref-8). [primary]

<a id="ref-8"></a>[8] GitLab Inc., "[Production Readiness Review
guide](https://docs.runway.gitlab.com/guides/production-readiness/)," Runway platform documentation
(accessed 2026-09-28). Supports a current page that contradicts [[7]](#ref-7) by directing readers to file
a new issue in the same archived project; not followed by this bundle. [vendor]

<a id="ref-9"></a>[9] Mercari, Inc., "[Check Production
Readiness](https://github.com/mercari/production-readiness-checklist/blob/master/docs/guides/check-production-readiness.md),"
production-readiness-checklist repository (accessed 2026-09-28). Supports the evidence-and-status mechanics
and the not-applicable rule this bundle adapts under MIT license, and the team-reviews-itself model.
[practitioner]

<a id="ref-10"></a>[10] Mercari, Inc., "[production-readiness-checklist.md
index](https://raw.githubusercontent.com/mercari/production-readiness-checklist/master/docs/references/production-readiness-checklist.md)"
(accessed 2026-09-28). Supports the design/pre-production phase split and the Level A/B/C tiering
definition. [practitioner]

<a id="ref-11"></a>[11] Mercari, Inc., "[design-checklist.md](https://raw.githubusercontent.com/mercari/production-readiness-checklist/master/docs/references/design-checklist.md)"
(accessed 2026-09-28). Supports the design-phase checklist's sections, including its own Security section.
[practitioner]

<a id="ref-12"></a>[12] Mercari, Inc., "[pre-production-checklist.md](https://raw.githubusercontent.com/mercari/production-readiness-checklist/master/docs/references/pre-production-checklist.md)"
(accessed 2026-09-28). Supports the pre-production checklist's sections, its runbook-adjacent "OnCall
playbooks" item, and the non-monotonic Manual Scale / Auto Scale tiering row. [practitioner]

<a id="ref-13"></a>[13] Mercari, Inc., "[production-readiness-level.md](https://raw.githubusercontent.com/mercari/production-readiness-checklist/master/docs/references/production-readiness-level.md)"
(accessed 2026-09-28). Supports the SLO basis for choosing a service level and the tiering it drives.
[practitioner]

<a id="ref-14"></a>[14] Mercari, Inc., "[LICENSE](https://raw.githubusercontent.com/mercari/production-readiness-checklist/master/LICENSE)"
(accessed 2026-09-28). Supports the MIT license that permits this bundle to adapt Mercari's evidence and
not-applicable wording with attribution. [practitioner]

<a id="ref-15"></a>[15] GitHub, "[repository metadata for mercari/production-readiness-checklist](https://api.github.com/repos/mercari/production-readiness-checklist)"
(accessed 2026-09-28). Supports independent confirmation of the MIT license recorded in [[14]](#ref-14).
[reference]

<a id="ref-16"></a>[16] GitLab, "[project metadata for gitlab-com/gl-infra/readiness](https://gitlab.com/api/v4/projects/gitlab-com%2Fgl-infra%2Freadiness?license=true)"
(accessed 2026-09-28). Supports that GitLab's readiness project states no license. [reference]

<a id="ref-17"></a>[17] Amazon Web Services, "[Operational Readiness Reviews
(ORR)](https://docs.aws.amazon.com/wellarchitected/latest/operational-readiness-reviews/wa-operational-readiness-reviews.html),"
AWS Well-Architected Framework whitepaper, June 30, 2022 (accessed 2026-09-28). Supports ORR's incident-driven
purpose, its framing as complementary to Well-Architected rather than to a PRR, and its self-assessment
model. [vendor]

<a id="ref-18"></a>[18] Amazon Web Services, "[Building
mechanisms](https://docs.aws.amazon.com/wellarchitected/latest/operational-readiness-reviews/building-mechanisms.html),"
ORR whitepaper section (accessed 2026-09-28). Supports ORR's framing as a recurring mechanism rather than a
one-off audit. [vendor]

<a id="ref-19"></a>[19] Amazon Web Services, "[The ORR
mechanism](https://docs.aws.amazon.com/wellarchitected/latest/operational-readiness-reviews/the-orr-mechanism.html),"
ORR whitepaper section (accessed 2026-09-28). Supports the desired outcomes, fewer, shorter, and smaller
incidents, that motivate ORR. [vendor]

<a id="ref-20"></a>[20] Amazon Web Services, "[The ORR
tool](https://docs.aws.amazon.com/wellarchitected/latest/operational-readiness-reviews/the-orr-tool.html),"
ORR whitepaper section (accessed 2026-09-28). Supports the three sources of a new question, the deliberate
exclusion of medium and low risks from the checklist, and the domain groupings this bundle draws on.
[vendor]

<a id="ref-21"></a>[21] Amazon Web Services, "[Gaining
adoption](https://docs.aws.amazon.com/wellarchitected/latest/operational-readiness-reviews/gaining-adoption.html),"
ORR whitepaper section (accessed 2026-09-28). Supports the SDLC-embedded, event-plus-annual cadence and
tiering by occasion and workload type. [vendor]

<a id="ref-22"></a>[22] Amazon Web Services, "[Inspect the
process](https://docs.aws.amazon.com/wellarchitected/latest/operational-readiness-reviews/inspect-the-process.html),"
ORR whitepaper section (accessed 2026-09-28). Supports the self-assessment-reviewed-at-a-meeting model, the
escalation of high-criticality findings to leadership, and the incident-review question tying ORR to a
checklist trigger. [vendor]

<a id="ref-23"></a>[23] Amazon Web Services, "[Iteration](https://docs.aws.amazon.com/wellarchitected/latest/operational-readiness-reviews/iteration.html),"
ORR whitepaper section (accessed 2026-09-28). Supports the named Operational Champion role and its
checklist-curation responsibility. [vendor]

<a id="ref-24"></a>[24] Amazon Web Services, "[Conclusion](https://docs.aws.amazon.com/wellarchitected/latest/operational-readiness-reviews/conclusion.html),"
ORR whitepaper section (accessed 2026-09-28). Supports the tool-adopt-inspect-iterate cycle framing.
[vendor]

<a id="ref-25"></a>[25] Microsoft, "[Operational Excellence maturity
model](https://learn.microsoft.com/en-us/azure/well-architected/operational-excellence/maturity-model),"
Azure Well-Architected Framework, Microsoft Learn (accessed 2026-09-28). Supports the continuous,
release-gate cadence and the named DRI decision role. [vendor]

<a id="ref-26"></a>[26] Microsoft, "[Design review checklist for Operational
Excellence](https://learn.microsoft.com/en-us/azure/well-architected/operational-excellence/checklist),"
Azure Well-Architected Framework, Microsoft Learn (accessed 2026-09-28). Supports a flat, numbered checklist
structure distinct from a topic-grouped one, and a named deployment-safety recommendation. [vendor]

<a id="ref-27"></a>[27] Cortex, "[Standardize and automate production
readiness](https://docs.cortex.io/solutions/production-readiness/configure)," Cortex Docs (accessed
2026-09-28). Supports the continuously computed, tiered Scorecard model and deployment gating by score, at
the level of a general description only. [vendor]

<a id="ref-28"></a>[28] Google, "[Launch Coordination
Checklist](https://sre.google/sre-book/launch-checklist/)," Appendix E of *Site Reliability Engineering*
(accessed 2026-09-28). Supports the launch checklist's own section headings, used to test and reject the
claim that the launch checklist is cross-functional while this review is engineering-only. [primary]

<a id="ref-29"></a>[29] Rhandeev Singh, Sebastian Kirsch, and Vivek Rau, edited by Betsy Beyer, "[Reliable
Product Launches at Scale](https://sre.google/sre-book/reliable-product-launches/)," chapter 27 of Google,
*Site Reliability Engineering* (accessed 2026-09-28). Supports the launch checklist's trigger, timing, and
the Launch Coordination Engineering team's explicitly cross-functional role. [primary]

<a id="ref-30"></a>[30] Ken Schwaber and Jeff Sutherland, "[Scrum Guide](https://scrumguides.org/scrum-guide.html)"
(2020 revision) (accessed 2026-09-28). Supports the definition of done's object, the Increment, and who is
accountable for conforming to it. [primary]

<a id="ref-31"></a>[31] Wikipedia, "[Change-advisory board](https://en.wikipedia.org/wiki/Change-advisory_board)"
(accessed 2026-09-28). Supports the change advisory board's unit of review, a requested change rather than a
service's standing readiness. [reference]

<a id="ref-32"></a>[32] NASA, "[NASA Systems Engineering Handbook Appendix (Definitions of
Terms)](https://www.nasa.gov/reference/system-engineering-handbook-appendix/)" (accessed 2026-09-28).
Supports NASA's own hardware-manufacturing definition of a Production Readiness Review, unrelated in
lineage to this bundle's type. [primary]

<a id="ref-33"></a>[33] AcqNotes, "[Production Readiness Review (PRR)](https://acqnotes.com/acqnote/acquisitions/production-readiness-review)"
(accessed 2026-09-28). Supports the US Department of Defense's hardware-manufacturing definition and its
Technical Review Chair role, unrelated in lineage to this bundle's type. [practitioner]

<a id="ref-34"></a>[34] Pedro Alves, "[Production Readiness Reviews: A Surprisingly Versatile
Practice](https://www.usenix.org/publications/loginonline/production-readiness-reviews-surprisingly-versatile-practice),"
USENIX ;login: online, April 28, 2025, shepherded by Laura Nolan (accessed 2026-09-28). Supports
reviewer-outside-the-team guidance, the two-reviewer sweet spot, findings tracking, and named goal-setting
and defensiveness anti-patterns. [practitioner]

<a id="ref-35"></a>[35] Laura Nolan, "[Why Don't We Have a Fire Code for
Software?](https://www.infoq.com/presentations/fire-code-software/)," QCon Plus, April 14, 2022, transcript
published on InfoQ (accessed 2026-09-28). Supports the team-defines-its-own-criteria model, embedding a
reviewer for a critical service, and three named antipatterns: shallowness, the template as law, and
forgetting the humans. [practitioner]

<a id="ref-36"></a>[36] Cortex, "[Production readiness review checklist & best
practices](https://www.cortex.io/post/how-to-create-a-great-production-readiness-checklist)," Cortex
engineering blog, January 14, 2026 (accessed 2026-09-28). Supports a cross-functional walkthrough model, a
binary outcome vocabulary, exception-with-expiration tracking, and tailoring the checklist by service type.
A survey percentage in this source was not used, since its underlying method was not verified. [vendor]

<a id="ref-37"></a>[37] Nawaz Dhandala, "[Run a Production Readiness Review with Evidence and Real
Gates](https://oneuptime.com/blog/post/2026-08-06-production-readiness-review-evidence-owners-launch-gates/view),"
OneUptime engineering blog, August 6, 2026 (accessed 2026-09-28). Supports the four-state outcome
vocabulary this bundle borrows from, per-finding closure tracking, the owner-versus-reviewer role
separation, and the rule against adding a question without a stated failure and evidence. [vendor]

<a id="ref-38"></a>[38] Federal Student Aid (U.S. Department of Education, Chief Technology Office),
"[Production Readiness Review (PRR) Process
Description](https://studentaid.gov/sites/default/files/fsawg/static/gw/docs/ciolibrary/PRR_Process.pdf),"
Version 26.0, 7/31/2026 (accessed 2026-09-28). Supports the four admitted elements, evidence per item, a
reason for every not-applicable answer, a sign-off naming accepted open issues, and a risk-scaled signatory,
while its release-moment content is routed to `launch-coordination-checklist` and `runbook` instead. Not
counted toward this bundle's admission on its own. [primary]

<a id="ref-39"></a>[39] adhorn (GitHub handle; author's legal name not confirmed), "[Operational Readiness
Review Template](https://github.com/adhorn/operational-excellence/blob/main/ORRtemplate.md),"
operational-excellence repository (accessed 2026-09-28). Supports worry-elicitation questions, a continuous,
multi-touchpoint cadence, diversified reviewer composition, and the explicit exclusion of security review
from this document's scope. [practitioner]
