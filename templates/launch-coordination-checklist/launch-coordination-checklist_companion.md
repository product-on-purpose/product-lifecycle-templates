# Companion: The Launch Coordination Checklist

> The deep explainer for the launch-coordination-checklist bundle. Read this to understand what the type
> is, where its name comes from, why the template is shaped the way it is, and where the sources this
> bundle read disagree about it. The short operator card is
> [`launch-coordination-checklist_guide.md`](launch-coordination-checklist_guide.md); a fully worked
> instance is [`launch-coordination-checklist_example.md`](launch-coordination-checklist_example.md).
> Inline citations like [[1]](#ref-1) resolve to the [References](#references) at the bottom, tagged by
> source reliability. This bundle sits in the `standing-standards` family alongside `definition-of-done`
> and `runbook`, as a **tool**: an instrument consulted at the moment of a launch decision, not a standard
> a team is judged against on a cadence.

---

## 1. Orientation

A launch coordination checklist is **the standing list a team consults before it ships an externally
visible change, so that readiness does not depend on who happens to be asking the questions.** Its
originating source states the underlying activity plainly: the practice around it "helps an LCE assess the
launch and provides the launching team with action items and pointers to more information," and its unit
is not a box to tick but a question paired with an action, as in "Do you need a new domain name?" answered
by "Coordinate with marketing on your desired domain name, and request registration of the domain."
[[2]](#ref-2)

**At a glance**
- It has a named origin, and the origin is unusual: Google's Launch Coordination Checklist, "circa 2005,"
  published as an appendix of a named technical book rather than invented for this library
  [[1]](#ref-1).
- It is **standing, by direct statement rather than inference**: "In 3.5 years, one LCE ran 350 launches
  through the LCE Checklist." One list, hundreds of launches [[2]](#ref-2).
- Its originating appendix is a **topic list, not a checkable list**: every item there is a noun phrase,
  none carries an owner, a pass condition, or a response, and it is licensed so this bundle may cite and
  quote it briefly but may not adapt its items or reproduce its structure [[1]](#ref-1). This bundle
  therefore teaches the practice recorded around the checklist rather than reproducing the checklist
  itself.
- A check earns its place by the failure it prevents, and the same source that says so also records the
  cost of not curating: "at one point, adding new questions to Google's launch checklist required approval
  from a vice president" [[2]](#ref-2).
- Go/no-go criteria and rollback triggers are meant to be decided before the launch, by a named person, not
  argued during it; a real incident shows what happens when neither is true [[12]](#ref-12)[[19]](#ref-19).

If you read nothing else: this is a standing readiness instrument, not a per-launch to-do list invented
fresh each time, and what a team fills out for one specific launch is the record of applying it, not the
instrument itself.

## 2. Origins and evolution

The type's admission source is Appendix E of Google's *Site Reliability Engineering*, titled "Launch
Coordination Checklist," the catalog's own name for the type verbatim. The appendix introduces itself as
"Google's original Launch Coordination Checklist, circa 2005, slightly abridged for brevity" [[1]](#ref-1).
Counted directly from the page rather than from a summary of it, which one research pass undercounted by
one category, it holds ten areas and thirty-one items, each phrased as a topic ("Machine dies, rack fails,
or cluster goes offline"; "Monitoring internal state, monitoring end-to-end behavior, managing alerts")
rather than as a question with a pass condition [[1]](#ref-1). It is licensed CC BY-NC-ND 4.0, no
derivatives, which is why this bundle's Readiness Checks section is built from categories found across
several sources rather than as a restyling of that one list [[1]](#ref-1).

The practice that produced the appendix is recorded in the following chapter, "Reliable Product Launches at
Scale." Google defines the event it governs plainly: "Google defines a launch as any new code that
introduces an externally visible change to an application" [[2]](#ref-2). The team that ran the checklist
did not exist from the start; it grew out of informal peer consulting. "A small band of experienced
engineers, called the 'Launch Engineers,' volunteered to act as a consulting team. The Launch Engineers
developed checklists for new product launches," and by 2004 SRE staffed this as "a small, full-time team of
LCEs," whose "consulting sessions were formalized as Production Reviews" [[2]](#ref-2). Launch Coordination
Engineering's own job was named directly: "Auditing products and services for compliance with Google's
reliability standards and best practices, and providing specific actions to improve reliability," and
"Acting as a liaison between the multiple teams involved in a launch" [[2]](#ref-2). The apparent simplicity
of any one question hides real judgment: "While each question on the LCE Checklist is simple, much
complexity is built in to what prompted the question and the implications of its answer. In order to fully
understand this degree of complexity, a new LCE hire requires about six months of training" [[2]](#ref-2).

The checklist did not stay fixed. It grew, and growth had to be managed deliberately: "In practice, there is
a near-infinite number of questions to ask about any system, and it is easy for the checklist to grow to an
unmanageable size... In an effort to curb its growth, at one point, adding new questions to Google's launch
checklist required approval from a vice president" [[2]](#ref-2). It was also pruned on a stated cadence:
"LCEs curate the checklist continuously and make small updates when team members notice items that need to
be modified. Once or twice a year a team member reviews the entire checklist to identify obsolete items"
[[2]](#ref-2). By 2008 the checklist itself had been tiered by risk: "LCEs identified categories of low-risk
launches that were highly unlikely to face or cause mishaps... Such launches were faced with an almost
trivial checklist, while higher-risk launches underwent the full gamut of checks and balances. By 2008, 30%
of reviews were considered low-risk" [[2]](#ref-2). The same chapter names aviation and surgical checklists
as the reason checklists are used at all, "Checklists are used to reduce failure and ensure consistency and
completeness across a variety of disciplines. Common examples include aviation preflight checklists and
surgical checklists" [[2]](#ref-2), without adopting either discipline's specific rules; the book this
influence is attributed to, Gawande's *The Checklist Manifesto*, was not itself read for this bundle, so
nothing here quotes it or attributes terminology to it directly.

Google's checklist is a historical artifact of one company's mid-2000s infrastructure, not a current
external standard, and this companion presents it as the named origin of the type rather than as present
practice [[1]](#ref-1). The chapter that describes the practice around it comes from the same book, and the
latest event in Google's history that this research cites from it is dated 2008 [[2]](#ref-2).

## 3. Anatomy (section by section)

The full variant carries seven sections; the lean variant carries five of them, unchanged in name and
order, so lean is a strict ordered subset of full.

### Scope and Launch Classes (lean and full)

What counts as a launch here, and which class of launch this checklist governs, in full or in a lighter
form.

This section absorbs what an earlier design treated as a separate "When This Does Not Apply" section,
because exemption in the sources read is not a standalone carve-out but a property of the launch's class.
Google itself tiered by risk rather than by exemption, "Such launches were faced with an almost trivial
checklist, while higher-risk launches underwent the full gamut of checks and balances" [[2]](#ref-2), and a
scored, upstream tiering practice makes the same move outside Google: "Tiering should be a joint decision
with clear scoring criteria, not a negotiation where the loudest voice wins," with a named bottom tier,
"Tier 3: Minor Release (Changelog Only)" [[20]](#ref-20). Of the published structures this research read,
only GitLab's readiness template handles the inapplicable case at the level of the individual item rather
than as its own section [[10]](#ref-10), which is why this bundle keeps exemption inside scope rather than
splitting it out again.

Not every source agrees on what scaling means. The UK government's Service Standard keeps the same bar for
every service regardless of size and instead scales who assesses it: "all new or redesigned services have
had to be assessed against all 26 points in the standard," because "it ensures that no matter how small the
transaction is a service will be built to the same standards," while routing lower-volume services to a
departmental panel instead of the central team [[15]](#ref-15). This bundle does not resolve that
disagreement (see section 6); Scope and Launch Classes is the section that asks the question rather than
answering it once for every reader.

Beginner note: state plainly what counts as a launch for your team, following Google's own working
definition of "any new code that introduces an externally visible change" if nothing narrower fits
[[2]](#ref-2), then name the classes and which sections of this checklist each class actually needs. Expert
note: if every launch you have ever logged ends up in the same class, the class boundary is not doing any
work and should be redrawn or dropped.

### Roles and Decision Authority (full only)

Who coordinates the launch, and who is authorized to say no.

This section is renamed from an earlier working title of "Roles and Sign-off," because neither of the
type's originating sources names a sign-off at all [[1]](#ref-1)[[2]](#ref-2); the practice of naming a
single decision authority instead comes from a later, non-Google source built specifically around a
launch-day go/no-go call: "Assign Decision Roles," where a named role "makes the go/no-go call for the
current risk tier," with the explicit instruction to "Name roles rather than inviting a large distribution
list" [[12]](#ref-12). What an undefined review role costs in practice is recorded directly in a real
deployment failure: "Knight did not have a second technician review this deployment and no one at Knight
realized that the Power Peg code had not been removed," because "Knight had no written procedures that
required such a review" [[19]](#ref-19). The lean variant does not drop this content; it folds the
decision-maker into Go/No-Go Criteria instead of giving roles their own section, which is a reasonable
compression once a launch is small enough not to need multiple named roles.

Beginner note: name one person, by role rather than by name, who makes the go/no-go call, and name who else
must review before that call is made. Expert note: a role with no one else checking its work is the exact
shape of the Knight Capital gap; if your riskiest launches route through a single reviewer, say so and
decide whether that is acceptable.

### Readiness Checks (lean and full)

The load-bearing section: checks grouped by area, each carrying the question, what actually answers it, the
role that owns it, and why the check exists.

This is the section the type's licence constrains most directly. Google's original appendix supplies the
precedent for a checklist organized by topic area, but its items are licensed CC BY-NC-ND 4.0 and are noun
phrases with no owner, pass condition, or response attached [[1]](#ref-1), so this section's categories are
built from the structures found across several other sources rather than as an adaptation of that one list.
The shape of a good check, however, is directly sourced: Google's own unit is a question paired with an
action, "Do you need a new domain name?" paired with "Coordinate with marketing on your desired domain
name, and request registration of the domain" [[2]](#ref-2), and its guideline for which questions belong
on the list at all is explicit: "Every question's importance must be substantiated, ideally by a previous
launch disaster. Every instruction must be concrete, practical, and reasonable for developers to
accomplish" [[2]](#ref-2). What a completed check should say is answered outside Google, by the aviation
checklist literature this research consulted for design rules rather than for software-launch evidence:
"the response should always portray the actual status or the value of the item," not a bare confirmation
[[7]](#ref-7). The WHO surgical checklist's own design rule points the same way: "Actionable. Every item on
the Checklist must be linked to a specific, unambiguous action" [[8]](#ref-8). And the same aviation source
warns against the section's obvious failure mode, unbounded growth: "as the list of items grows, there may
be a higher probability of overlooking any given item" [[7]](#ref-7). Real structural precedent for grouping
checks by area, without a per-item owner field, appears repeatedly in published readiness templates
[[10]](#ref-10)[[11]](#ref-11); a rarer structure carries an owner and a pass state together for every check
[[12]](#ref-12), which this bundle's design follows rather than the more common flat, unowned shape.

Beginner note: for each check, write the question, name what evidence actually answers it, name who owns
answering it, and note briefly why the check is here; if you cannot say why a check is here, that is a
reason to cut it rather than keep it for safety. Expert note: audit this table on the same cadence the
section on curation below describes, and be honest that the response field means the current status of the
item, not "done."

### Launch Communications (full only)

Who needs to know before, at, and after the launch: support, documentation, and the announcement itself.

Of the structural sources this research read, none carries this as its own named section; it is included in
the full variant because the content is carried elsewhere, by the paired pm-skills template's Marketing,
Support, and Legal & Compliance domains and its fixed check-in cadence around the launch date
[[6]](#ref-6), and by a launch-execution playbook that names the full cross-functional roster explicitly:
"The core roster is a product manager to steer, a designer to make it usable, a marketer for research and
the GTM, a customer success or support lead for resources, and a salesperson to actually sell," with support
training named as its own pre-launch item, "Train customer support on the technical details and common
questions" [[36]](#ref-36). This is also the section that carries the boundary with a neighboring document
type: the announcement of what shipped belongs to `release-notes`, which the paired skill for this type
explicitly routes elsewhere rather than producing itself [[5]](#ref-5).

Beginner note: name who on support and documentation needs to know before the launch, not just after it,
and what they need to be told. Expert note: if this section is doing the job of drafting the customer-facing
announcement itself, that content belongs in a release notes document instead, not here.

### Rollout and Rollback (lean and full)

How the launch is staged, and the condition that reverses it, decided before the launch rather than argued
during it.

This section was promoted into the lean variant because the research found it to be the element a naive
checklist most reliably omits, and the cost of omitting it is directly evidenced. Google's own practice
treats staged rollout and automatic reversal as the default, not the exception: "Almost all updates to
Google's services proceed gradually, according to a defined process, with appropriate verification steps
interspersed," and "very few launches at Google are of the 'push-button' variety" [[2]](#ref-2). Where a
staged rollout fails validation, the reversal is pre-decided rather than debated in the moment: "If the
change doesn't pass the validation period, it's automatically rolled back," and elsewhere, "Independently
revert each such change immediately in the event of serious bugs or side effects" [[2]](#ref-2). A
launch-day framework built around the same idea states the discipline directly: "Predeclare Rollback and
Stop Triggers," with the instruction "Do not debate a clear hard trigger while impact grows. Abort first,
then investigate" [[12]](#ref-12). What happens without a predeclared trigger is recorded in a real
incident: Knight Capital's emergency response made the outage worse because "there was no kill switch," on
a deployment where the responsible engineer's own retrospective conclusion was that "deployments need to be
automated and repeatable and as free from potential human error as possible" [[19]](#ref-19). A related
readiness practice extends the same discipline past the moment of rollout: keep rollback-compatible
artifacts and configuration in place until the launch has actually been observed through a real workload
cycle, "keep rollback-compatible schema, artifacts, and configuration until the agreed observation window
ends" [[13]](#ref-13).

Beginner note: name the specific condition that triggers a rollback before you launch, not after something
goes wrong, and name who is authorized to pull it. Expert note: a rollback trigger debated for the first
time during an incident is functionally the same as having no trigger at all; if your team has never had to
use one, that is not evidence you do not need one.

### Go/No-Go Criteria (lean and full)

What blocks a launch, decided in advance, and how an accepted exception is recorded.

The clearest sourced model for this section states four possible readings of a check rather than a binary
pass or fail: "green: evidence is within the predeclared safe range; yellow: an accepted deviation requires
explicit risk ownership; red: a hard gate failed; unknown: evidence is absent, delayed, or untrustworthy,"
with the explicit warning that "Unknown is not green" [[12]](#ref-12). The same source states the rule for
what a missing prerequisite means: "Either the prerequisite is met, an authorized time-bounded exception
exists, or the decision is no-go" [[12]](#ref-12), and names the anti-pattern this rule exists to prevent:
"Executive override without ownership: a deadline silently replaces a hard gate" [[12]](#ref-12). Where an
exception is accepted rather than the launch blocked, the instruction is to record it, not to let it pass
silently: "Record yellow-state acceptance, expiry, and decision authority" [[12]](#ref-12). The lean variant
carries the decision-maker's role directly inside this section rather than pointing to a separate Roles and
Decision Authority section, on the reasoning that a small launch needs to know who decides more than it
needs a roster.

Beginner note: list the specific conditions that block a launch outright, and separately, how an accepted
exception gets recorded, who owns it, and when it expires. Expert note: watch for a deadline quietly
replacing a hard gate; if a go/no-go criterion has an exception process, the exception should be visible in
the document, not only in a decision-maker's memory.

### Review Trigger (lean and full)

What event makes this checklist wrong, and who is expected to notice.

No structural source this research read publishes a section with this name or job; it is required directly
by the `standing-standards` family contract rather than volunteered by any source, and this bundle labels it
as its own contribution the way its sibling bundles in the same family label theirs. The evidence bounding
what the trigger should ask for comes from several directions. Google's own curation practice sets a floor:
"Once or twice a year a team member reviews the entire checklist to identify obsolete items" [[2]](#ref-2),
and that same source records what happens when curation is neglected in the other direction, unbounded
growth requiring vice-presidential approval to control [[2]](#ref-2). A marketing-side launch practice
argues for updating the standing reference after every occasion rather than on a calendar: "Launch
Playbook... Update it after each launch," naming a failed launch's postmortem as the most valuable single
input, "A failed launch postmortem is the most valuable. You'll learn the most," and requiring that "every
learning needs an owner, due date, and target metric" so it becomes an actual change rather than a note
nobody acts on [[21]](#ref-21). But the two most direct sources on what an incident should do to a checklist
disagree, and this section is built to hold that disagreement rather than resolve it silently. Google's own
guideline reads permissively, "Every question's importance must be substantiated, ideally by a previous
launch disaster" [[2]](#ref-2), which invites treating any past incident as grounds for a new item. A
practitioner account of production readiness review practice warns against exactly that: "With every
incident that went awry, we would add a line item to our PRR process. Definitely do not do that, because
you end up with this PRR process that's just monstrous and you cannot understand the underlying mechanisms"
[[22]](#ref-22), while still holding that incidents belong in the loop somehow, "Incidents are catalysts to
understanding the difference between how your organization is structured in theory versus how it operates
in practice" [[22]](#ref-22). This bundle reads the two sources as compatible once the trigger asks a
narrower question than "did an incident happen": which mechanism failed, not merely that something went
wrong. One vendor's own treatment of postmortem follow-up corroborates that a mechanical incident-to-
checklist pipeline is not standard practice even where it might be expected: its only runbook-adjacent
example is a single ordinary tracked task, "update the runbook for auth service failover procedure by next
Friday," not evidence of a structured feedback loop into a standing list [[26]](#ref-26).

Beginner note: name the specific event that would make this checklist wrong, a new failure class, a
platform migration, a repeated near-miss, and who owns noticing it, rather than writing "reviewed annually."
Expert note: when an incident does prompt a change here, write down which mechanism failed and why the
existing checks did not catch it, before deciding whether the fix is a new check or something else
entirely; that discipline is what keeps this section from becoming the unmanageable list Google's own
history warns about.

## 4. Variants and sizing

**Lean (five sections)** is Scope and Launch Classes, Readiness Checks, Rollout and Rollback, Go/No-Go
Criteria, and Review Trigger. It keeps the engineering-readiness core intact, on the reading that the
originating source and most of the structural precedent read here are engineering and operations scoped
[[1]](#ref-1)[[29]](#ref-29)[[30]](#ref-30)[[31]](#ref-31)[[32]](#ref-32)[[33]](#ref-33)[[34]](#ref-34), while
carrying the launch's decision-maker inside Go/No-Go
Criteria rather than a separate roles section.

**Full (seven sections)** adds Roles and Decision Authority and Launch Communications. Both additions are
cross-functional rather than engineering-internal: naming a decision authority becomes worth its own section
once more than one role could plausibly make the call, and launch communications matters once the launch
reaches support, documentation, or a public announcement rather than staying inside one team. The paired
pm-skills template reaches into marketing, support, and legal by default [[6]](#ref-6), and a cross-
functional launch playbook names the same full roster [[36]](#ref-36); a lean, engineering-only fill is the
right default only where that reach genuinely is not needed.

## 5. Methodology lineage

**The SRE lineage is the load-bearing one.** The type's origin, its evolution, its curation discipline, and
its rollout and rollback defaults all come from Google's own account of Launch Coordination Engineering
[[1]](#ref-1)[[2]](#ref-2). The same lineage's later practice, Production Readiness Review, grew out of the
same consulting habit: "Their consulting sessions were formalized as Production Reviews" [[2]](#ref-2), and
"Usually, the SRE team establishes and maintains a PRR checklist explicitly for the Analysis phase"
[[3]](#ref-3). This bundle does not claim PRR replaced the launch checklist; no source read says that, and
the two documents govern different moments of the same lineage rather than one superseding the other (see
section 8).

**The aviation lineage** supplies design rules for what makes any checklist usable under pressure, item
wording, response discipline, and length, rather than evidence that those rules transfer to software
launches. Every use of this lineage in this bundle names the domain explicitly [[7]](#ref-7).

**The medical lineage** supplies the WHO Surgical Safety Checklist's structural design principles, Focused,
Brief, Actionable, Verbal, Collaborative, Tested, Integrated, again cited for design discipline rather than
as software-launch evidence [[8]](#ref-8), and Atul Gawande's journalism on the aviation and ICU checklist
history, read directly rather than through his book [[9]](#ref-9).

**The government-service lineage** treats readiness as a published, universal standard rather than an
internal engineering discipline: the UK's GOV.UK Service Standard assesses every service against the same
26 points regardless of size, scaling who assesses rather than what is assessed [[15]](#ref-15), and its
live-phase guidance names pre-live topics, information security, accessibility, uptime, vulnerability and
performance testing, in prose rather than as a checkable list [[14]](#ref-14).

**The go-to-market lineage** treats launch readiness as a marketing and cross-functional discipline rather
than a purely engineering one: tiering the launch by scored effort before planning starts [[20]](#ref-20),
naming the full cross-functional roster and support training explicitly [[36]](#ref-36), and treating
version-bound readiness evidence with a stated authority model that scales by launch shape [[37]](#ref-37).

**A vendor lineage reframes readiness as a continuously re-evaluated scorecard rather than a launch-window
checklist at all.** Cortex's Scorecards re-evaluate on a schedule, by default every four hours
[[30]](#ref-30); OpsLevel splits a lightweight, team-owned Scorecard from an org-wide Rubric whose level is
recomputed continuously from live check results rather than authored once per launch
[[32]](#ref-32)[[33]](#ref-33); and Spotify's Backstage Soundcheck evaluates Tracks made of Levels made of
Checks against every service on a schedule, retaining certification history rather than a per-launch record
[[34]](#ref-34). These products sell an alternative to authoring a checklist at all, and are named here as a
distinct lineage rather than corroboration for this bundle's own design.

## 6. Debates and contested boundaries

**Is the checklist standing, or is a fresh one written per launch?** Both halves are true, read at
different grains. Google ran one list through 350 launches over 3.5 years [[2]](#ref-2); vendor tooling
frames the object the same way, presenting its template as reusable, "your team can follow a proven process
from planning to post-launch monitoring without having to start over each time," and saving an improved
version forward rather than starting over [[27]](#ref-27), and other vendor practice describes revising a
checklist rather than replacing it [[28]](#ref-28)[[31]](#ref-31). The per-launch camp is equally real: the
paired pm-skills template produces a document tied to one launch, down to a check-in schedule dated around
that launch [[6]](#ref-6), and a go-to-market readiness practice states plainly that "readiness is
version-bound," so a change to the product, environment, or dependency invalidates the affected evidence and
requires it to be reviewed again by a stated date [[37]](#ref-37). This bundle's own synthesis, not stated
outright by any one source, is that the standing instrument is the list and its rules, and what a team
produces by applying it to one launch is a per-launch record rather than a second kind of document.

**What should an incident do to the checklist?** The two most direct sources disagree, and section 3's
Review Trigger anatomy states the disagreement and the reading adopted in full; in short, Google's own
guideline invites justifying a new item by a past disaster [[2]](#ref-2), while a practitioner account of
readiness-review practice warns explicitly against a naive per-incident append loop
[[22]](#ref-22), and a marketing-side practice argues for updating the standing reference after every launch
regardless [[21]](#ref-21).

**Is the checklist a gate, or a guide?** One vendor source defends the deployment checklist as a forcing
function rather than bureaucracy, explicitly rejecting a rubber-stamped version of it: "Not just
rubber-stamped. Reviewers should run the code locally or, at minimum, read the diff carefully"
[[28]](#ref-28). Other vendor sources describe good readiness review as collaborative problem-solving rather
than box-checking, "Instead of just checking boxes, they use reviews to surface risks and align on
solutions" [[35]](#ref-35), and one practitioner argues the discrete, late-stage review is the wrong pattern
altogether, proposing instead that the readiness document start alongside the design doc and be filled out
through development, turning it "from a checklist to a to-do list that is used during development"
[[23]](#ref-23). This bundle teaches the checklist as a gate consulted at a decision point, consistent with
its `classification: tool` placement in the standing-standards family, while naming the continuous
alternative as a live disagreement rather than a settled answer.

**Should a lower-risk launch get a lighter checklist, or the same checklist with a different assessor?**
Google's own tiering lightens the checklist itself for low-risk launches [[2]](#ref-2), and a marketing
tiering framework does the same, down to a changelog-only bottom tier [[20]](#ref-20). The UK government's
Service Standard instead keeps the same 26-point bar for every service and changes only who assesses it
[[15]](#ref-15). This bundle's Scope and Launch Classes section asks the question rather than answering it,
because the sources genuinely do not agree.

**Is scope engineering-only, or cross-functional?** The type's origin and the standing-scorecard vendor
cluster are engineering and operations scoped [[1]](#ref-1)[[29]](#ref-29)[[30]](#ref-30)[[31]](#ref-31)
[[32]](#ref-32)[[33]](#ref-33)[[34]](#ref-34). The paired pm-skills template and a launch-execution playbook
reach into marketing, support, and legal [[6]](#ref-6)[[36]](#ref-36)[[5]](#ref-5), and a readiness-review
practice explicitly names legal and compliance stakeholders [[35]](#ref-35); even Google's own checklist
routes one sample question to marketing [[2]](#ref-2). This bundle keeps engineering readiness as the lean
core and carries the cross-functional reach as full-only sections (see section 4).

**Is a per-check owner and evidence field the norm, or the exception?** It is the exception among the
published structures this research read. One source carries both an owner-equivalent decision role and an
explicit evidence field together [[12]](#ref-12). Everywhere else, GitLab's issue template and its filled
instance [[10]](#ref-10)[[11]](#ref-11), a government open-source checklist [[16]](#ref-16), an open-source
project's release wiki, whose closest approach is instructing a release manager to be named once for the
whole release rather than a field on each item, "Define a release manager" [[17]](#ref-17), and a personal,
optional practitioner checklist [[18]](#ref-18), carry neither an owner nor an evidence field on individual
items. This bundle's per-check design is argued from Google's own question-plus-action unit and from the
aviation source's rule on responses, not from a count of how many practitioner templates already do it this
way [[2]](#ref-2)[[7]](#ref-7).

**Does the design evidence from aviation and medicine actually transfer to software launches?** No source
this research read asserts that it does. The aviation and WHO sources are cited here for checklist design
discipline, item wording, length, response rules, never for outcome numbers, and every use of them in this
bundle names the domain explicitly [[7]](#ref-7)[[8]](#ref-8)[[9]](#ref-9).

## 7. Anti-patterns and failure modes

**No second reviewer, and no written requirement for one.** "Knight did not have a second technician review
this deployment and no one at Knight realized that the Power Peg code had not been removed," because "Knight
had no written procedures that required such a review" [[19]](#ref-19).

**No rollback trigger decided in advance.** The same incident's emergency response made things worse
because "there was no kill switch" [[19]](#ref-19); a launch-day framework states the fix directly,
"Predeclare Rollback and Stop Triggers" [[12]](#ref-12).

**Unbounded list growth.** Left unmanaged, a checklist can require executive intervention just to control
its size: "In an effort to curb its growth, at one point, adding new questions to Google's launch checklist
required approval from a vice president" [[2]](#ref-2).

**A per-incident append loop.** "With every incident that went awry, we would add a line item to our PRR
process. Definitely do not do that, because you end up with this PRR process that's just monstrous and you
cannot understand the underlying mechanisms" [[22]](#ref-22).

**A response that says "done" instead of the actual status.** The aviation source's rule exists precisely
against this failure: "the response should always portray the actual status or the value of the item"
[[7]](#ref-7).

**Treating an unknown as a pass.** "Unknown is not green" [[12]](#ref-12); an absent or delayed piece of
evidence is not the same thing as a satisfied check.

**An executive override with no owner.** "Executive override without ownership: a deadline silently replaces
a hard gate" [[12]](#ref-12).

**A rubber-stamped review.** "Not just rubber-stamped. Reviewers should run the code locally or, at minimum,
read the diff carefully" [[28]](#ref-28).

**Readiness treated as permanent once granted.** "A service that was production ready three months ago
might no longer be ready" [[29]](#ref-29); readiness evidence is version-bound and a later change can
invalidate an earlier answer without anyone updating the record [[37]](#ref-37).

**Checklist decay under production pressure**, a failure mode the aviation literature names directly even
though it is describing a different discipline: "Flight crews should be made aware that the checklist
procedure is highly susceptible to production pressures," which "may lead some to relegate checklist
procedures to second level of importance, or not use them at all" [[7]](#ref-7).

## 8. Relationships to other artifacts

**Launch coordination checklist and runbook.** Both are `tool`-classified members of the same family, and
the distinction is temporal rather than structural: a checklist prepares for an event that has not yet
happened; a runbook responds to a situation that has [[24]](#ref-24). The sharpest sourced statement of that
boundary describes what a runbook must carry that a linear checklist cannot, "what to check first, what to
avoid, when to branch, and when to escalate" [[24]](#ref-24). A set of launch checklist items that has
turned into branching, situational procedure has become a runbook and belongs in that document instead.

**Launch coordination checklist and release notes.** The paired pm-skills template for this type explicitly
routes the customer-facing announcement elsewhere: readiness and comms are this document's job, the
announcement of what shipped is `release-notes`'s job [[5]](#ref-5). Launch Communications (section 3) is
the section where that boundary lives.

**Launch coordination checklist and production readiness review.** The two are related by lineage rather
than identical or sequential. Google's Launch Engineers' consulting sessions "were formalized as Production
Reviews" [[2]](#ref-2), and later SRE practice maintains "a PRR checklist explicitly for the Analysis phase"
[[3]](#ref-3), so PRR grew out of the same practice this type's checklist documents. No source this research
read states that PRR replaced the launch checklist, and this bundle makes no such claim; the two documents
plausibly govern different moments of the same discipline. A separate distinction, between the release
moment and long-term operability, is drawn without using either term: "Deployment readiness focuses on the
moment a product is released to manufacturing or the market. Production readiness covers the broader
question of whether the product can be produced, scaled, supported, and maintained over time"
[[38]](#ref-38); this document sits on the release-moment side of that line.

**Launch coordination checklist and operational readiness review.** AWS's own ORR whitepaper describes a
curated set of questions reviewed "throughout the complete lifecycle of their service, from inception to
post-release operations" [[4]](#ref-4), a broader, recurring scope than this type's pre-launch window,
generating different checklist templates per workload from a shared question bank [[4]](#ref-4). This
bundle does not carry any claim about what an ORR review meeting feeds into, since that specific claim was
not verified against the primary source itself.

**Launch coordination checklist and definition of done.** A definition of done is a standing, per-unit-of-
work engineering quality gate, "an agreed-upon set of items that must be completed before a project or user
story can be considered complete," and is explicitly framed as necessary but not sufficient for a full
launch, "you're not done with a product (or feature) until you've put it out to pasture" [[25]](#ref-25).
The two documents are siblings in the same `standing-standards` family, classified differently: a definition
of done is a `foundation` a team is judged against, this checklist is a `tool` a team executes at the moment
of a launch decision.

**Launch coordination checklist and issue-tracker launch templates.** First-party issue-tracker tooling
offers a rendering of much of the same content, owner, deadline, and status per item, inside a timeline or
dashboard view rather than a standalone document, "assign ownership to individual team members and track the
progress each team member has made on the tasks they've been assigned" [[39]](#ref-39). Teams that already
track launch work inside their issue tracker can treat this template as the shape that content should take,
rather than as a competing artifact.

## 9. Adaptations

**Small, single-team changes should not get the full checklist at all.** The paired pm-skills template names
the failure mode of over-applying it directly: "a launch checklist adds ceremony without value; track it in
the sprint instead" [[5]](#ref-5), and a tiering framework's smallest tier asks for nothing beyond a
changelog entry [[20]](#ref-20).

**Regulated or cross-functional launches should widen the checklist deliberately, not by accident.** A
readiness-review practice names the specific gap: "Include legal and compliance stakeholders in readiness
reviews" [[35]](#ref-35), and the paired pm-skills template already carries Legal & Compliance as one of its
domains for exactly this reason [[6]](#ref-6).

**Public-sector or highly regulated teams should consider scaling the assessor rather than the bar.** GOV.UK
holds every service to the same 26-point standard and instead routes lower-volume services to a departmental
panel rather than lowering what is checked [[15]](#ref-15); a team that finds itself tempted to write a
"light" version of its checklist for smaller launches should check whether it is actually lightening the
bar or only the reviewer.

**Teams that already track launch work in an issue tracker** can render this template's Readiness Checks and
Go/No-Go Criteria as tasks with owners and status inside that tool rather than as a standalone document, the
same content the issue tracker's own launch templates already organize around a timeline [[39]](#ref-39).

## 10. Worked example

[`launch-coordination-checklist_example.md`](launch-coordination-checklist_example.md) demonstrates a
full-variant checklist as it stood at Acme Analytics' platform team, the same fictional team the
`standing-standards` family's other examples describe, at the point its Saved Views launch consulted it.
Consistent with the type's licence, it is an independent worked instance built from the categories and
design rules this companion cites, not an adaptation of Google's own appendix [[1]](#ref-1). It is worth
checking three things in it: that its Readiness Checks table states what actually answers each question
rather than a bare "done," that its Rollout and Rollback section names a trigger decided before the launch
rather than during it, and that its Review Trigger names an event and an owner rather than a calendar date.

---

## References

<a id="ref-1"></a>[1] Google, *Site Reliability Engineering* (O'Reilly Media; web edition at sre.google,
copyright 2017 Google), Appendix E: "[Launch Coordination Checklist](https://sre.google/sre-book/launch-checklist/)"
(accessed 2026-09-22). Supports the type's admission under its catalog name, the verbatim structure of
Google's circa-2005 checklist, and the CC BY-NC-ND 4.0 licence that constrains this bundle's Readiness Checks
section and its example. [primary]

<a id="ref-2"></a>[2] Rhandeev Singh and Sebastian Kirsch with Vivek Rau, edited by Betsy Beyer, "[Reliable
Product Launches at Scale](https://sre.google/sre-book/reliable-product-launches/)," chapter 27 of Google,
*Site Reliability Engineering* (O'Reilly Media; web edition at sre.google, copyright 2017 Google) (accessed
2026-09-22). Supports Google's operational definition of a launch, the LCE team's history and curation
practice, its risk tiering, and its rollout and rollback defaults. The most heavily cited source in this
bundle. [primary]

<a id="ref-3"></a>[3] Acacio Cruz and Ashish Bhambhani, edited by Betsy Beyer and Tim Harvey, "[The Evolving
SRE Engagement Model](https://sre.google/sre-book/evolving-sre-engagement-model/)," chapter 32 of Google,
*Site Reliability Engineering* (O'Reilly Media; web edition at sre.google, copyright 2017 Google) (accessed
2026-09-22). Supports that Production Readiness Review still centers on a maintained checklist for its
Analysis phase, and grew from the same lineage as the Launch Coordination Checklist. [primary]

<a id="ref-4"></a>[4] Amazon Web Services, "[Operational Readiness Reviews
(ORR)](https://docs.aws.amazon.com/wellarchitected/latest/operational-readiness-reviews/wa-operational-readiness-reviews.html),"
AWS Well-Architected Framework whitepaper, June 30, 2022 (accessed 2026-09-22). Supports ORR as a broader,
recurring, lifecycle-spanning readiness practice distinct in scope from this type's pre-launch window. A
claim about ORR meetings feeding a go or no-go decision was seen only in a search snippet and is not used
here. [vendor]

<a id="ref-5"></a>[5] product-on-purpose, "[deliver-launch-checklist
SKILL.md](https://raw.githubusercontent.com/product-on-purpose/pm-skills/main/skills/deliver-launch-checklist/SKILL.md),"
skill version 2.2.0 (accessed 2026-09-22). Supports the paired skill's per-launch framing, its explicit
routing of the customer-facing announcement to `release-notes`, and its guidance against using a full
checklist for small single-team changes. Internal, sibling-project source. [internal]

<a id="ref-6"></a>[6] product-on-purpose, "[deliver-launch-checklist
references/TEMPLATE.md](https://raw.githubusercontent.com/product-on-purpose/pm-skills/main/skills/deliver-launch-checklist/references/TEMPLATE.md)"
(accessed 2026-09-22). Supports the paired skill's nine-domain content, including Marketing, Support, and
Legal & Compliance, and its fixed check-in cadence around a specific launch date. Internal, sibling-project
source. [internal]

<a id="ref-7"></a>[7] Asaf Degani and Earl L. Wiener, "[Human Factors of Flight-Deck Checklists: The Normal
Checklist](https://ntrs.nasa.gov/api/citations/19910017830/downloads/19910017830.pdf)," NASA Contractor
Report 177549, May 1990 (accessed 2026-09-22). Supports item-wording and response-discipline design rules,
and the finding that a growing checklist raises the odds of overlooking an item. Aviation evidence, cited
for design discipline, not for software-launch outcomes. [primary]

<a id="ref-8"></a>[8] World Health Organization, "[Implementation Manual: WHO Surgical Safety
Checklist](https://www.leapfroggroup.org/sites/default/files/Files/Implementation%20manual%20WHO%20surgical%20safety%20checklist%202009.pdf)"
(2009), hosted by the Leapfrog Group (accessed 2026-09-22). Supports the Focused, Brief, Actionable, Verbal,
Collaborative, Tested, Integrated design principles. Medical evidence, cited for design discipline, not for
software-launch outcomes. [primary]

<a id="ref-9"></a>[9] Atul Gawande, "[The Checklist](https://lchc.ucsd.edu/cogn_150/Readings/gawande_checklist.pdf),"
*The New Yorker*, December 10, 2007, course-reading copy (accessed 2026-09-22). Supports the aviation origin
story of the checklist and the design philosophy behind Pronovost's ICU checklists, read directly rather than
through Gawande's later book, which was not consulted for this bundle. [practitioner]

<a id="ref-10"></a>[10] GitLab, "[.gitlab/issue_templates/Operational
Readiness.md](https://gitlab.com/gitlab-org/gitlab/-/raw/df973a6d104cd94a9fb3f8172696a4944fdbcc46/.gitlab/issue_templates/Operational%20Readiness.md),"
gitlab-org/gitlab repository (accessed 2026-09-22). Supports an in-repo readiness template with checks
grouped by area, no owner or pass-condition field per item, and inapplicability handled at the item level
rather than by a separate section. [practitioner]

<a id="ref-11"></a>[11] GitLab infrastructure, "[gl-infra/readiness issue #13, ActionCable readiness
review](https://gitlab.com/gitlab-com/gl-infra/readiness/-/issues/13)" (accessed 2026-09-22). Supports a
filled instance of the same template, confirming checks grouped by area with no owner, pass-condition, or
sign-off field on any individual item. [practitioner]

<a id="ref-12"></a>[12] Nawaz Dhandala, OneUptime, "[Run a Launch-Day Go/No-Go
Decision](https://oneuptime.com/blog/post/2026-08-06-launch-day-go-no-go/view)," 2026-08-06 (accessed
2026-09-22). Supports the four-state green/yellow/red/unknown evaluation model, named decision roles,
predeclared rollback and stop triggers, and the named anti-pattern of an unowned executive override. Vendor
source, prescriptive rather than a record of observed practice. [vendor]

<a id="ref-13"></a>[13] OneUptime, "[Run a Post-Launch Readiness
Review](https://oneuptime.com/blog/post/2026-08-06-post-launch-readiness-review/view)," 2026-08-06 (accessed
2026-09-22). Supports keeping rollback-compatible schema and configuration in place until an agreed
observation window closes. Vendor source, prescriptive. [vendor]

<a id="ref-14"></a>[14] Government Digital Service, "[How the live phase
works](https://www.gov.uk/service-manual/agile-delivery/how-the-live-phase-works)," GOV.UK Service Manual
(accessed 2026-09-22). Supports pre-live topics, information security, accessibility, uptime, vulnerability
and performance testing, stated as prose rather than as a checkable list. [primary]

<a id="ref-15"></a>[15] Government Digital Service blog, "[Meeting the standard regardless of
size](https://gds.blog.gov.uk/2014/06/17/meeting-the-standard-regardless-of-size/)," 2014 (accessed
2026-09-22). Supports a published gate assessed against all 26 points of the Service Standard for every
service regardless of size, with assessment authority, not the bar itself, scaled by transaction volume.
[primary]

<a id="ref-16"></a>[16] Consumer Financial Protection Bureau, "[opensource-checklist.md](https://github.com/cfpb/open-source-project-template/blob/main/opensource-checklist.md),"
open-source-project-template (accessed 2026-09-22). Supports a real, CC0-licensed pre-release checklist with
no owner, pass-condition, or sign-off field on any item, used here as an example of the more common,
unowned flat-list shape. [practitioner]

<a id="ref-17"></a>[17] Keptn project (CNCF), "[Release
Checklist](https://github.com/keptn/keptn/wiki/Release-Checklist)" wiki page (accessed 2026-09-22). Supports
a sequential, step-based release runbook that names a release manager once for the whole release rather than
carrying a per-item owner field. [practitioner]

<a id="ref-18"></a>[18] Radek Pietruszewski, "[Open-source project release
checklist](https://radek.io/posts/release-checklist/)" (accessed 2026-09-22). Supports a personal, optional,
self-assessment checklist with no owner, pass-condition, or sign-off fields, used here as a contrast case for
the more common unowned shape. [practitioner]

<a id="ref-19"></a>[19] Doug Seven, "[Knightmare: A DevOps Cautionary
Tale](https://dougseven.com/2014/04/17/knightmare-a-devops-cautionary-tale/)" (2014) (accessed 2026-09-22).
Supports the cost of no written requirement for a second reviewer and no predeclared rollback trigger, drawn
from Knight Capital's August 2012 deployment failure. Secondary analysis of the incident; the SEC's own
order was not read for this bundle. [practitioner]

<a id="ref-20"></a>[20] GTM Playbook, "[Launch Tiering Framework for Product Marketing
Teams](https://discover.gtmplaybook.co/launch-tiering-framework)" (accessed 2026-09-22). Supports scored,
upstream tiering decisions and a named changelog-only bottom tier for launches that do not warrant the full
process. Practitioner source, prescriptive. [practitioner]

<a id="ref-21"></a>[21] GTM Playbook, "[Launch Postmortem
Template](https://discover.gtmplaybook.co/launch-postmortem-template)" (accessed 2026-09-22). Supports
updating a standing "Launch Playbook" after every launch, naming a failed launch's postmortem as the most
valuable input, and requiring every learning to carry an owner, due date, and target metric. [practitioner]

<a id="ref-22"></a>[22] InfoQ, article on incidents, production readiness reviews, and psychological safety,
quoting Nora Jones, "[Incidents, PRRs, and Psychological
Safety](https://www.infoq.com/articles/incidents-prr-psychological-safety/)" (accessed 2026-09-22). Supports
the warning against a naive per-incident append loop into a readiness process, and incidents as a source of
understanding rather than an automatic trigger for a new item. [practitioner]

<a id="ref-23"></a>[23] Jos Visser, "[The Continuous Production Readiness
Review](https://josvisser.substack.com/p/the-continuous-production-readiness)" (accessed 2026-09-22).
Supports the argument that a late, discrete readiness review is the wrong pattern, proposing the document
start alongside the design doc instead. An argument for changing practice, not a description of it.
[practitioner]

<a id="ref-24"></a>[24] Dunya Kirkali, "[Runbooks are not
checklists](https://blog.incrementalforgetting.tech/p/runbooks-are-not-checklists)" (accessed 2026-09-22).
Supports the boundary between a linear checklist and a runbook that must encode branching judgment under
pressure. [practitioner]

<a id="ref-25"></a>[25] ProductPlan, "[The Definition of Done: What Product Managers Need to
Know](https://www.productplan.com/learn/agile-definition-of-done)" (accessed 2026-09-22). Supports the
definition of done as a standing, per-unit-of-work engineering quality gate, necessary but not sufficient
input to a full launch. [practitioner]

<a id="ref-26"></a>[26] incident.io, "[Why Do Post-Mortem Action Items
Fail?](https://incident.io/blog/why-do-post-mortem-action-items-fail-how-to-make-incident-follow-ups-actually-get-done)"
(accessed 2026-09-22). Supports the absence of a described, systematic postmortem-to-checklist feedback
mechanism even in a vendor's own treatment of the same problem space. Vendor source. [vendor]

<a id="ref-27"></a>[27] Asana, "[Software Deployment Template](https://asana.com/templates/software-deployment)"
(accessed 2026-09-22). Supports a reusable, standing-template framing for a deployment checklist, saved
forward with improvements rather than rewritten per launch. Vendor source. [vendor]

<a id="ref-28"></a>[28] DeployHQ, "[The Ultimate Deployment
Checklist](https://www.deployhq.com/blog/the-ultimate-deployment-checklist-ensuring-smooth-and-successful-releases)"
(accessed 2026-09-22). Supports the gate-as-forcing-function framing, the explicit rejection of a
rubber-stamped review, and a stated staleness-review cadence. Vendor source. [vendor]

<a id="ref-29"></a>[29] Cortex, "[Production Readiness Review Checklist & Best
Practices](https://www.cortex.io/post/how-to-create-a-great-production-readiness-checklist)" (accessed
2026-09-22). Supports readiness as version-bound and decaying over time, and readiness reviews tailored to
service type. Vendor source, which sells automated scorecards as a replacement for manual review. [vendor]

<a id="ref-30"></a>[30] Cortex, "[Standardize: Scorecards:
Create](https://docs.cortex.io/standardize/scorecards/create)," product documentation (accessed 2026-09-22).
Supports Cortex Scorecards as a continuously re-evaluated framework, by default every four hours, distinct
from a launch-window checklist. Vendor documentation. [vendor]

<a id="ref-31"></a>[31] OpsLevel, "[Production readiness checklist: An in-depth
guide](https://www.opslevel.com/resources/production-readiness-in-depth)" (accessed 2026-09-22). Supports a
standing-but-evolving readiness template, tiered by application criticality and revised as the organization
learns rather than rewritten from scratch. Vendor source. [vendor]

<a id="ref-32"></a>[32] OpsLevel, "[Scorecards](https://docs.opslevel.com/docs/scorecards)," product
documentation (accessed 2026-09-22). Supports Scorecards as a team-level, lightweight rubric distinct from
the org-wide Rubric, both representing a continuously evaluated standing framework rather than a per-launch
document. Vendor documentation. [vendor]

<a id="ref-33"></a>[33] OpsLevel, "[Getting Started with
Rubrics](https://docs.opslevel.com/docs/getting-started-with-rubrics)," product documentation (accessed
2026-09-22). Supports a component's level being continuously recomputed from live check results rather than
authored once per launch. Vendor documentation. [vendor]

<a id="ref-34"></a>[34] Spotify, "[Backstage Soundcheck: Core concepts:
Tracks](https://backstage.spotify.com/docs/plugins/soundcheck/core-concepts/tracks)," product documentation
(accessed 2026-09-22). Supports readiness modeled as Tracks composed of Levels composed of Checks, evaluated
continuously against every service rather than authored per launch. Vendor documentation for a paid
Backstage plugin. [vendor]

<a id="ref-35"></a>[35] DX (getdx), "[Production readiness checklist for dependable
releases](https://getdx.com/blog/production-readiness-checklist/)" (accessed 2026-09-22). Supports
collaborative, risk-surfacing readiness review over box-checking, tiered rigor by change type, and naming
legal and compliance stakeholders explicitly for regulated launches. Vendor source. [vendor]

<a id="ref-36"></a>[36] Userpilot, "[Product Launch Checklist for 2026: The Execution
Playbook](https://userpilot.com/blog/product-launch-checklist/)" (accessed 2026-09-22). Supports tiering by
launch magnitude, the full cross-functional roster including support training, and standing-template reuse
across launches. Vendor source, titled for 2026. [vendor]

<a id="ref-37"></a>[37] Playcode, "[Product Launch Checklist: Evidence Before
Go-to-Market](https://playcode.io/blog/product-launch-checklist)" (accessed 2026-09-22). Supports readiness
evidence as version-bound, invalidated by a change to the product, environment, or dependency, and a stated
authority model that scales by launch shape. Vendor source. [vendor]

<a id="ref-38"></a>[38] Studio Red, "[Production Readiness: A Practical Guide for Real
Launches](https://www.studiored.com/blog/design/production-readiness/)" (accessed 2026-09-22). Supports the
distinction between deployment readiness, the moment of release, and production readiness, the broader
question of long-term operability. Vendor source. [vendor]

<a id="ref-39"></a>[39] Atlassian, "[Jira Product Launch Timeline
template](https://www.atlassian.com/software/jira/templates/product-launch-timeline)" (accessed 2026-09-22).
Supports an issue-tracker rendering of owner, deadline, and status content adapted per launch, applied
inside a timeline or dashboard view rather than a standalone document. Vendor template page. [vendor]
