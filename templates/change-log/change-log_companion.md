# Companion: The Change Log

> The deep explainer for the change-log bundle. Read this to understand what a change log is, where it
> came from, why it is shaped the way it is, and where practitioners disagree about it. The short
> operator card is [`change-log_guide.md`](change-log_guide.md); a fully worked instance is
> [`change-log_example.md`](change-log_example.md). Inline citations like [[1]](#ref-1) resolve to the
> [References](#references) at the bottom, tagged by source reliability.

---

## 1. Orientation

A change log is the register a project or program keeps of every change requested against an agreed
baseline and what was decided about each one. The Project Management Institute states the job in one
line: "The change log is used to record all submitted change requests." [[1]](#ref-1). The Association
for Project Management's glossary states the same job with the outcome named: "A record of all project
changes: proposed, authorised, rejected or deferred." [[3]](#ref-3). The European Commission's PM² guide
adds the verb the log actually serves: "A Change Log is used to document, monitor and control all project
changes (see Appendix B)." [[7]](#ref-7).

Multiple public bodies ship a working version of it rather than only defining it. PM² publishes a
seventeen-field template across four groups [[7]](#ref-7); the Connecticut Department of Social Services
ships an eleven-column log described as "Also known as Project Change Register" [[10]](#ref-10); the US
Department of Health and Human Services instructs every project, "regardless of type or size," to
maintain one [[26]](#ref-26), against a fifteen-column spreadsheet [[11]](#ref-11); and the University of
California Office of the President ships a seven-column change request log [[13]](#ref-13). San Francisco
State University publishes a fifteen-column log that repeats the HHS spreadsheet's fields, drop-downs and
instructional prose almost word for word; this bundle counts that as evidence that the HHS template
travels between institutions, not as another independently designed structure [[14]](#ref-14).

The name collides with two other artifacts a reader will meet under similar words, and this bundle is
neither of them. A software changelog is "a curated, chronologically ordered list of notable changes for
each version of a project," written for users and contributors rather than for a
governance decision, and it carries no requester, decider, decision, or status field at all
[[15]](#ref-15). ITIL's own glossary has no entry named "change log"; it names a Change Record, which
"contains all the details of a Change, documenting the lifecycle of a single Change," and a Change
Schedule, "a Document that lists all approved Change Proposals and Changes and their planned
implementation dates" [[16]](#ref-16)[[17]](#ref-17). PRINCE2 is the one named methodology exception on
the other side: it keeps the whole function inside its issue register, with a change log named only as an
alternative place to write the eventual decision (section 5).

**At a glance**
- Named directly by PMI [[1]](#ref-1), APM [[3]](#ref-3), and PM² [[7]](#ref-7); shipped as a working
  template by PM² [[8]](#ref-8), Connecticut DSS [[10]](#ref-10), HHS [[11]](#ref-11), and UCOP
  [[13]](#ref-13).
- **The change request is not the log.** A change request is one document; the log is the register that
  gets one row per request [[1]](#ref-1)[[4]](#ref-4)[[7]](#ref-7)[[13]](#ref-13). This bundle follows
  that two-document convention (section 6).
- **Every request gets a row, and no row is ever deleted**, including a rejected, withdrawn, or postponed
  one [[3]](#ref-3)[[10]](#ref-10)[[26]](#ref-26)[[40]](#ref-40).
- **A decision is not the same thing as a status.** A row that is closed still says what was decided and
  why [[7]](#ref-7)[[11]](#ref-11) (section 6).
- Also called a change register [[3]](#ref-3)[[4]](#ref-4)[[10]](#ref-10), a change management log
  [[11]](#ref-11)[[26]](#ref-26)[[27]](#ref-27), or a change request log
  [[13]](#ref-13)[[29]](#ref-29); a change control log appears in one practitioner source and no public
  body [[28]](#ref-28).
- **PRINCE2 keeps this function inside its issue register, by design**, and this bundle's family treats
  that as a methodology choice, not the failure it otherwise warns against [[5]](#ref-5).

If you read nothing else: a change log is the **cumulative, never-pruned record of every requested change
against a stated baseline**, kept apart from the request document itself, kept apart from the decision
that was made about it, and useless for governing anything unless a named person decides within a stated
authority and the log shows, in total, how far the baseline has actually moved.

---

## 2. Origins and evolution

No source read names an inventor or a founding document for the change log, and the honest pattern is
convergent naming rather than one lineage: several standards bodies arrive at the same artifact from their
own traditions rather than inheriting it from a common ancestor. PMI's own *Lexicon of Project Management
Terms* carries no standalone "change log" entry at all; it defines the surrounding vocabulary instead,
change control, the change control board, the change control system, and the change management plan
[[2]](#ref-2), and leaves the log itself to be named where PMI actually uses it: as an output of Perform
Integrated Change Control, in the *PMBOK Guide*'s sixth-edition errata [[1]](#ref-1). Only that errata was
read; the *PMBOK Guide* itself, sixth or eighth edition, was not, so nothing in this bundle rests on either
edition's own text.

APM's glossary carries two adjacent entries rather than one, and they say different things: "Change log A
record of all project changes: proposed, authorised, rejected or deferred," against "Change register (or
log) A record of all proposed changes to scope" [[3]](#ref-3). This bundle takes the first, broader sense,
the one PMI [[1]](#ref-1) and PM² [[7]](#ref-7) share.

PM² is the source this bundle draws its richest structure from, and for a specific reason beyond
thoroughness: it is the only source read here that ships the complete artifact, all seventeen fields
defined, under a licence that permits reuse. The guide itself states the licence plainly: "Document
licensed under CC BY 4.0 license" [[7]](#ref-7). A companion change note confirms the Change Log's field
structure held steady across the guide's own revision, from version 3.0.1 to 3.1: "The new templates do
not introduce any changes to the template structure or core content" [[9]](#ref-9), so the field list this
bundle cites is not a snapshot of one edition passing through.

The public-sector templates that follow, Connecticut's [[10]](#ref-10), HHS's
[[11]](#ref-11)[[12]](#ref-12), and UCOP's [[13]](#ref-13), state no reuse licence at all. This bundle
treats them as **structure evidence**, what a real, governed program's field list actually looks like, and
never as text to adapt directly. Two limits are worth naming rather than working around. ISO 21502:2020
and AXELOS's PRINCE2 manual are both paid standards this research did not read; PRINCE2 enters this
companion instead through prince2.wiki's practitioner pages [[5]](#ref-5)[[6]](#ref-6). And Wikipedia's own
"Changelog" article was not retrieved, so the boundary this bundle draws against the software changelog
rests on Keep a Changelog alone [[15]](#ref-15).

---

## 3. Anatomy (section by section)

The template carries seven sections in full, four of them in lean. Every field named below is one a real,
published source carries; where two published sources disagree about a field's presence or its values,
that disagreement is stated rather than smoothed into a single answer.

### Purpose and Boundary

**What it is:** a short statement of which baseline, or baselines, this log tracks, by artifact and
version, and what does not belong in it. **Why it exists:** because the name collides with two other
documents a reader will meet under similar words, and the first job of this section is to rule them out
before the table starts. The line separating this artifact from a software changelog rests on Keep a
Changelog's own account of what a changelog is for: "To make it easier for users and contributors to see
precisely what notable changes have been made between each release (or version) of the project"
[[15]](#ref-15), a purpose with no requester, decider, or decision at all. The line against PRINCE2 is a
named methodology choice rather than a boundary dispute: PRINCE2 keeps a request for change inside its
issue register, "Issues must be recorded in the issue register," and names a change log only as an
alternative place to write the eventual decision, "should be documented in the issue register or change
log" [[5]](#ref-5). APM's own process page places the standing register as the first concrete step inside
change control itself: "Log change request in a change register (or log)." [[4]](#ref-4).

### Status Vocabulary

**What it is:** the status values a request can hold, and, kept apart from status, the decision values
that record what was actually decided. **Why it exists:** no two published sources use the same list, and
naming both up front is what keeps the table itself short. PM²'s eight-value status list is this
template's sourced default, offered under the licence that permits it [[7]](#ref-7); Connecticut's
seven-value list, "Submitted, In Review, Approved, Denied, Deferred, Withdrawn, or Closed"
[[10]](#ref-10), and HHS's three-core-plus-three-optional list [[11]](#ref-11) are named as alternatives,
because HHS's own guidance leaves the actual choice to the team: "THE LIST OF ELEMENTS IS AT THE
DISCRETION OF THE PROJECT MANAGER." [[12]](#ref-12). **Decision is kept distinct from status**, following
PM², which defines "four possible decisions: approve, reject, postpone or merge the change request"
[[7]](#ref-7) as a field separate from status; Connecticut, HHS and UCOP carry status alone, and HHS's own
"Closed" value is explicitly ambiguous about what was decided: "The change request is no longer considered
an active project threat and can be closed with or without resolution." [[11]](#ref-11). Two published
sources are worth flagging as internally inconsistent rather than corrected silently: PM² names its own
second status value once as "Investigating" and once, in its own field-by-field appendix, as "Assessing"
[[7]](#ref-7); and HHS's Priority field lists three valid values in its own instructions and then defines a
fourth, Critical [[11]](#ref-11).

### Change Log

**What it is:** the load-bearing table, one row per request, and the section the other six exist to
support. **Why it exists:** because the register's whole value is in never losing a row. HHS states the
rule directly, "Each change request should be recorded as a single line item. Do not combine multiple
requests under one change request ID." [[26]](#ref-26), and no row is ever deleted for having gone the
wrong way: APM's own definition already names rejected and deferred outcomes as part of what the log
records, not exceptions to it, "proposed, authorised, rejected or deferred" [[3]](#ref-3); Connecticut
carries Withdrawn and Deferred as ordinary statuses, not removals [[10]](#ref-10); and a published template
states the reason directly, keeping a rejected row "prevents the same request from being resubmitted
without understanding why it was declined." [[40]](#ref-40). Three or more of the published field lists
checked here share an identifier, a description, the date raised, and a status; most also carry a requester and a
priority. This bundle's research adds two fields beyond that shared spine. The first is **the baseline
each request would change, by artifact and version**, following HHS's own shared data-element list for
the request form and the log alike: "The product version that the suggested change is for" [[12]](#ref-12).
The second is **the decision, with its reason, kept beside the row rather than only in the request
document**, following HHS's "Final Resolution & Rationale" field [[11]](#ref-11), Connecticut's
Resolution/Comments column [[10]](#ref-10), and the published guidance to record a reason with every
rejection [[40]](#ref-40). Who decided and when belong in lean; the full variant's table can carry more of
the surrounding detail without adding a new field's worth of judgment to make.

### Authority and Escalation

**What it is:** who may decide which changes, and the point at which a change goes above them. **Why it
exists, and why it carries this name rather than the spec's original "Escalation":** every source this
research found on the subject is actually about who holds the authority to decide; escalation is simply
what happens when a change exceeds it. PRINCE2's practitioner literature states the role plainly: "The
change authority is a person or group to whom the project board may delegate responsibility for reviewing
and approving change requests or off-specifications." [[6]](#ref-6). HHS supplies a worked threshold: "a
project manager (PM) may be authorized to personally approve changes with a project impact of less than
$5,000" [[26]](#ref-26). PM² carries the same idea as a per-row flag rather than a policy statement:
"Escalation to the Directing or Steering layer is needed? (Yes or No)." [[7]](#ref-7). A federal audit of
agency rebaselining policies states, as its own criterion for a documented baseline-change decision rather
than as a claim about change logs, that "a rebaselining policy should identify the authority who decides
whether the rebaselining is warranted" [[36]](#ref-36); this bundle applies that criterion to a change-log
row only by analogy, because the source audits policies, not logs.

### Implementation and Traceability

**What it is:** the target date and the actual delivery date, kept apart from the decision date; what was
actually updated and to which version; and links out to the change request document and to any related
issue, risk, or decision. **Why it exists:** because the date a change is decided is not the date it
ships, and a source read for a different domain shows exactly how that gap becomes a problem when nobody
tracks it: an inspector general's review of a real change-order system found that "the approval date in
eBuilder represents the date that the staff finalized the approval process for a change order and not the
Governing Boards authorization date." [[39]](#ref-39). PM² keeps the two dates as separate fields for
exactly this reason: "The target date for the change to be delivered." and, kept apart from it, "The date
on which the change was actually delivered." [[7]](#ref-7); HHS carries the same split as Expected and
Actual Resolution Dates [[11]](#ref-11). Traceability out to other logs is PM²'s own field, stated
directly: "The ID(s) of the tasks (in the Project Work Plan) that implement the change, and/or the IDs of
related issues, risks or decisions." [[7]](#ref-7); HHS's Assoc ID column carries the same idea in one
field [[11]](#ref-11). PM²'s Implemented status is the sourced definition of what closes this section out,
"the work implementing this change has been incorporated into the Project Work Plan." [[7]](#ref-7), and a
second, independent source names a matching field for the same event, "Date Request Integrated into
Project Plan" [[29]](#ref-29).

### Cumulative Effect

**What it is:** the running total of approved change against the baseline as it was first agreed, computed
from the log's own rows rather than read off any single one of them. **Why it exists:** because no single
row shows drift, only the sum of many rows does, and this is the section the research added rather than
inherited from a published field list. An APM practitioner names the function directly: the register
"provides an audit history of how the change has been managed and shows the additional time/cost/scope
that has been approved since the project scope was first agreed." [[37]](#ref-37). A real inspector
general's audit computed exactly this, approved change as a percentage of the original contract value,
because a list of individual entries does not itself show the compounding effect against a baseline
[[39]](#ref-39). A practitioner's own illustration of the same effect, "By week eight, the cumulative
impact of those small changes had shifted the schedule by two weeks." [[40]](#ref-40), is stated here as an
illustration of the mechanism, not as a measured figure; nothing in this research measured how often or
how far real projects actually drift this way.

### Review and Ownership

**What it is:** the named keeper of the log, the cadence at which it is reviewed, and what closes an
approved row against its baseline. **Why it exists:** because a register nobody owns and nobody reviews is
a file, not an instrument. Four sources name a keeper, and they do not agree on a title: HHS names the
Change Manager, "The Change Manager enters the CR into the CR Log." [[12]](#ref-12); UCOP names the Change
Request Coordinator, "responsible for maintaining the Change Request Log on behalf of the Change
Management Lead." [[13]](#ref-13); PM² gives the job to the project manager, who "collects
information on any project changes and related actions and controls the status of each change
management activity." [[7]](#ref-7); and one open textbook names the project manager as the end-to-end owner
of the whole process, "responsible to monitor the change process from the very beginning to the very end."
[[29]](#ref-29). No source read separates the person who decides a change from the person who writes its
row as a general rule, so the template asks for a named keeper and leaves the title to the team. Only one
figure on review cadence is sourced at all: HHS's own guidance that the review process "may happen daily
but should happen at least weekly for even the simplest projects" [[26]](#ref-26), and that guidance
concerns reviewing open change requests, not the log as a standing artifact; no other cadence appears
anywhere in this research, and none should be read as this bundle's recommendation. Closing each
approved row against its baseline is sourced, not a position. PM² makes it the project manager's duty:
"For approved or merged changes, the Project Manager (PM) should incorporate all related actions into the
Project Work Plan and update the related documentation and logs (i.e. Risk, Issue, Change and Decision Logs
and other plans)." It adds that "the Change Log should be kept up-to-date." [[7]](#ref-7). PM²'s
Implemented status [[7]](#ref-7) and the open textbook's integration column [[29]](#ref-29) are the
row-level record of that duty. A periodic audit of the whole log against its baselines, beyond closing
each row, is this library's own position, and the template labels it as such rather than as sourced
practice.

---

## 4. Variants and sizing

**Lean** is the smallest complete change log: **Purpose and Boundary**, **Status Vocabulary**, the
**Change Log** table itself, and **Authority and Escalation**. It is a working register a team can
populate and govern from the first submitted request, and it is enough for a project whose changes decide
and close inside the team without a formal delivery hand-off or a standing cumulative figure anyone asks
for.

**Full** is a strict superset, adding **Implementation and Traceability** (the target and actual delivery
dates kept apart from the decision, plus links to the request document and related logs), **Cumulative
Effect** (the running total of approved change against the original baseline), and **Review and
Ownership** (a named keeper and a stated cadence). Move to full when a sponsor or governance body will ask,
weeks later, how far the baseline has actually moved in total [[37]](#ref-37)[[39]](#ref-39), when the
decision date and the delivery date genuinely diverge often enough that conflating them would mislead an
auditor [[39]](#ref-39), or when the log needs a named owner because more than one person could plausibly
be asked to keep it.

---

## 5. Methodology lineage

- **PMI / PMBOK.** Names the change log as an output of Perform Integrated Change Control, "the change log
  is used to record all submitted change requests" [[1]](#ref-1); the *Lexicon* defines the surrounding
  vocabulary, change control, the change control board, the change control system, and the change
  management plan, but carries no standalone change-log entry of its own [[2]](#ref-2).
- **APM.** Carries two adjacent glossary entries, a broader change log and a narrower, scope-only change
  register [[3]](#ref-3), and places the register as the first concrete step of its own change-control
  process [[4]](#ref-4).
- **PM² (European Commission).** The fullest published field list this research found, seventeen fields
  across four groups, an eight-value status vocabulary kept apart from a four-value decision field, and
  the only source this bundle may adapt directly under an open licence [[7]](#ref-7). It ships the Change
  Log as its own downloadable artefact, separate from the Change Request Form [[8]](#ref-8), and keeps a
  standing Decision Log beside it, linked through the traceability field rather than merged into it
  [[7]](#ref-7).
- **PRINCE2.** The named exception. A request for change is one of its issue types, "issues must be
  recorded in the issue register," and a change log appears only as an alternative place to write the
  decision, "should be documented in the issue register or change log" [[5]](#ref-5). This bundle's family
  contract treats that as a deliberate methodology choice, not the collapse it otherwise warns against.
- **Public-sector programs.** Connecticut [[10]](#ref-10), HHS [[11]](#ref-11)[[12]](#ref-12), and UCOP
  [[13]](#ref-13) each ship a working, differently-shaped log with no stated reuse licence; San Francisco
  State's near-identical copy of the HHS spreadsheet is evidence that a public template travels between
  institutions, not another independent design [[14]](#ref-14).
- **Agile teams without a fixed baseline.** The Scrum Guide carries no change-log vocabulary at all and
  routes change through one person instead: "Those wanting to change the Product Backlog can do so by
  trying to convince the Product Owner." [[31]](#ref-31). Shape Up rejects a standing list outright,
  "Backlogs are a big weight we don't need to carry." [[35]](#ref-35), though its subject is the backlog,
  not a change log specifically; section 6 below treats this as a question of whether a fixed baseline
  exists, not a disagreement within one context.
- **Contracted and regulated work.** A fixed-price federal contract clause requires a written order and an
  equitable adjustment for any change to drawings, designs, or specifications [[33]](#ref-33), and the federal
  design-control rule at 21 CFR 820.30(i) requires "the identification, documentation, validation or where appropriate
  verification, review, and approval of design changes before their implementation" [[34]](#ref-34): both
  describe exactly the record a change log formalizes, for a baseline that carries weight outside the
  team.

---

## 6. Debates and contested boundaries

**Is the request one document with the log, or two?** PM² ships them as two separate artefacts, "This
template is part of the Monitor & Control Logs." [[8]](#ref-8), while stating a shared data-element list
between the request form and the log [[12]](#ref-12) and keeping a distinct logging step, "The Change
Manager enters the CR into the CR Log." [[12]](#ref-12). UCOP is explicit that the log is populated by
copying out of a separate form: "Transfer the Date of Request, Change Request #, Change Request Title, the
resource assigned to the change request, the description of the change requested, current status and
implementation date from the change request form for each specific change request." [[13]](#ref-13).
Connecticut's own template does not say whether a form feeds it at all [[10]](#ref-10). **This bundle
follows the two-document convention**, and does not read HHS's shared field list as evidence that HHS
merges the two artefacts into one.

**Is the decision a status?** Only PM² keeps them apart, a Status field and a separate Decision field with
"four possible decisions: approve, reject, postpone or merge the change request" [[7]](#ref-7).
Connecticut, HHS and UCOP carry status alone, and HHS's own "Closed" value is explicitly ambiguous about
what was actually decided [[11]](#ref-11). **This bundle keeps Decision distinct from Status, following
PM², and says so as a stated choice rather than an industry norm.**

**What the log covers.** APM's glossary carries two entries: the change log records "all project changes:
proposed, authorised, rejected or deferred," while the change register (or log) records only "all proposed
changes to scope" [[3]](#ref-3). **This bundle takes the first, broader sense**, the one PMI [[1]](#ref-1)
and PM² [[7]](#ref-7) share.

**Which statuses.** PM² offers eight values and is internally inconsistent about the name of one of them
[[7]](#ref-7); Connecticut offers seven [[10]](#ref-10); HHS offers three core values and three optional
ones, and is internally inconsistent about how many priority values are valid [[11]](#ref-11); and HHS's
own plan template leaves the whole list to the project's discretion [[12]](#ref-12). **No source read
claims its own list is universal**, and the template does not present one as though it were.

**Does work without a fixed baseline need a change log at all?** Scrum routes change through the Product
Owner's own judgment and carries no change-log vocabulary [[31]](#ref-31); Shape Up rejects standing lists
outright, though for the backlog specifically rather than a change log [[35]](#ref-35). Against that, a
fixed-price contract clause requires a documented, written-order adjustment for any change [[33]](#ref-33),
and design-control regulation requires documented review and approval before implementation
[[34]](#ref-34). **The split is by whether an agreed baseline exists that carries weight outside the
team, not a disagreement inside one context**; both sides of this split are reported, not resolved into one
rule.

**What DORA's finding is actually about.** DORA's own capability page concerns approval of production
changes by an external body such as a change-advisory board, and finds "no evidence was found to support
the hypothesis that a more formal, external review process was associated with lower change fail rates"
[[32]](#ref-32). **It never mentions a project baseline or a change log, and this companion does not apply
it to one**; the finding is about software delivery approval gates, a different subject from the artifact
this bundle documents.

**Who keeps the log.** HHS names the Change Manager as the one who enters requests [[12]](#ref-12); UCOP
names a Change Request Coordinator maintaining the log "on behalf of the Change Management Lead."
[[13]](#ref-13); one open textbook names the project manager as the end-to-end owner of the whole change
process [[29]](#ref-29). **No source read separates the person who decides a change from the person who
writes its row as a general rule**; the template asks for a named keeper and leaves the title to the
team.

**How often it is reviewed.** Only one figure is sourced anywhere in this research, HHS's guidance that
review "may happen daily but should happen at least weekly for even the simplest projects"
[[26]](#ref-26), and it concerns reviewing open change requests, not the log as a standing artifact. **Any
other cadence is the team's own choice**, and this bundle does not offer one as settled practice.

**The change-log-versus-decision-log boundary rests on one practitioner.** "A decision log tracks what was
decided. A Change Control Log tracks what changed, why it changed, who approved it, and what the impact
was on the baseline." [[28]](#ref-28). Six further decision-log pages checked specifically for this
boundary either never mention a change log by name or mention it only as a marketing list of log types a
tool supports, and none states the distinction
[[20]](#ref-20)[[21]](#ref-21)[[22]](#ref-22)[[23]](#ref-23)[[24]](#ref-24)[[25]](#ref-25). PM² is the one
primary source that keeps a separate Decision Log beside its Change Log, linked through a shared
traceability field rather than merged into either [[7]](#ref-7). **No standards body states this boundary
in any source this research read**; it is attributed to one named practitioner, by name.

---

## 7. Anti-patterns and failure modes

**A deliberate honesty check belongs first.** This research looked for a named source listing the ways a
change log fails, among them entries that never receive a decision, approved changes never carried into
the baseline, and a log kept but never read, and found none that names them as failure modes. **This
bundle therefore offers no checklist of how change logs fail.** What the research did find is
narrower, mostly a single practitioner's account or a finding from an adjacent domain applied here by
analogy, and it is stated that way below rather than generalized.

1. **Decisions made and never written down.** One practitioner's account of the failure this artifact
   exists to prevent: "Changes happen. Decisions get made informally. Nobody writes it down. And
   eventually, the project is living in a reality that the plan never accounted for and nobody officially
   approved." [[28]](#ref-28). One source, and this bundle says so rather than presenting it as measured.
2. **A date that records the wrong event.** A real inspector general's review of a construction
   change-order system, not a project change log, found that "the approval date in eBuilder represents the
   date that the staff finalized the approval process for a change order and not the Governing Boards
   authorization date." [[39]](#ref-39). Cited here as an auditor's finding about a change register,
   applied by analogy; the source's own subject is construction change orders.
3. **Drift that no single row shows.** An APM practitioner describes the register's audit-history function
   directly [[37]](#ref-37); the same inspector general's audit computed approved change as a percentage
   of the original contract for the same reason [[39]](#ref-39); a vendor template's own illustration of
   the effect, "By week eight, the cumulative impact of those small changes had shifted the schedule by
   two weeks." [[40]](#ref-40), is an illustration of the mechanism, not a measured finding.
4. **A rejected request that comes back.** Keeping a rejected request in the log with its reason
   "prevents the same request from being resubmitted without understanding why it was declined."
   [[40]](#ref-40). Vendor tier, and the only source that states this particular failure directly.

---

## 8. Relationships to other artifacts

**Change log vs change request.** The request is one document, filed to describe and justify a single
proposed change; the log is the standing register that gets one row per request, whatever the request's
eventual disposition [[1]](#ref-1)[[4]](#ref-4)[[7]](#ref-7)[[13]](#ref-13). This bundle's sibling
[`change-request`](../change-request/change-request_guide.md), in the `delivery-docs` family, is the
document that feeds each row.

**Change log vs issue log, risk register, RAID log, and KPI dashboard.** This family's own contract states
the position directly: a change log "stands to the delivery chain's change request as the issue log
stands to the RAID log's Issues column: the standing, cumulative record behind a document that is filed
once per occasion and then archived"
([governance-docs family contract](../../docs/internal/contracts/governance-docs.md), section 1). No
source read in this bundle's own research compares a change log to a risk register, a RAID log, or a KPI
dashboard directly; the parallel above is this library's own framing, stated as such, not a claim drawn
from any numbered source.

**Change log vs decision log.** PM² keeps a separate Decision Log beside its Change Log, connected only
through a shared traceability field rather than merged into either [[7]](#ref-7). The boundary between the
two artifacts in general rests on one named practitioner, "A decision log tracks what was decided. A
Change Control Log tracks what changed, why it changed, who approved it, and what the impact was on the
baseline." [[28]](#ref-28), a claim no standards body corroborates in any source this research read
(section 6).

**Change log vs a software changelog.** A software changelog is "a curated, chronologically ordered list
of notable changes for each version of a project," written for users and contributors,
"Changelogs are for humans, not machines." [[15]](#ref-15). It carries no requester, decider, decision, or
status field, and it is the release-notes half of change communication, not the governance half this
artifact is.

**Change log vs ITIL's Change Record and Change Schedule.** ITIL's own glossary has no entry named "change
log" [[16]](#ref-16)[[17]](#ref-17). Its Change Record documents the lifecycle of one operational change,
usually created from a preceding request for change, and its Change Schedule lists approved changes and
their planned implementation dates [[16]](#ref-16). Neither is the cumulative, decision-and-authority
record this artifact holds, and this bundle does not claim ITIL defines a change log by any name.

**Change log vs a change-advisory board.** A CAB "delivers support to a change-management team by advising
on requested changes, assisting in the assessment and prioritization of changes" [[18]](#ref-18); it is a
reviewing body, not a document, and no source read names a cumulative log artifact as one of its outputs.

**Change log vs configuration change control.** NIST's guidance on security-focused configuration
management uses no "change log" wording at all; its own vocabulary is "Configuration Change Control," the
"documented process for managing and controlling changes to the configuration of a system or its
constituent CIs." [[19]](#ref-19). This is a distinct, systems-security domain from the project-baseline
record this bundle documents, and this companion draws no equivalence between the two.

---

## 9. Adaptations

- **PM²-based teams.** Adopt the field list, the status vocabulary, and the separate decision field as
  printed; PM² is the one source this bundle may adapt directly, under its stated CC BY 4.0 licence
  [[7]](#ref-7), and its structure held across the guide's own 3.0.1-to-3.1 revision [[9]](#ref-9).
- **PRINCE2 teams.** Decide explicitly whether requests for change stay inside the issue register,
  PRINCE2's own design [[5]](#ref-5)[[6]](#ref-6), or move to a standalone change log; either is
  defensible, and this bundle's family contract treats the first choice as a methodology decision, not the
  collapse it otherwise warns against.
- **Public-sector and government teams.** Several public bodies already publish working change-log
  structures freely, though none states a reuse licence, so they are useful as structure evidence rather
  than adaptable source text [[10]](#ref-10)[[11]](#ref-11)[[13]](#ref-13).
- **Small teams and small projects.** One practitioner states the proportionality directly: "A two-person
  project running for eight weeks does not need a Change Control Board with quarterly meetings. It needs a
  lightweight log and a clear agreement between the project manager and the sponsor about what requires
  formal approval versus what can be handled directly." [[28]](#ref-28).
- **Contracted and regulated work.** Where a fixed-price contract [[33]](#ref-33) or a design-control
  regulation [[34]](#ref-34) already requires a documented change-approval record, the change log is the
  place that record lives; the authority and escalation section should name the contracting officer or the
  regulatory reviewer directly rather than a generic role.
- **Agile teams with no fixed baseline.** Where change routes through the Product Owner's own judgment
  against an emergent backlog [[31]](#ref-31), a standing change log adds process a team without an
  external baseline does not need; adopt one only once a baseline that carries weight outside the team
  exists, a contract, a regulator, or a sponsor-signed scope and budget.

---

## 10. Worked example

[`change-log_example.md`](change-log_example.md) is the full-variant change log for the same **Reporting
Platform Modernization** program that
[`change-request_example.md`](../change-request/change-request_example.md) and
[`issue-log_example.md`](../issue-log/issue-log_example.md) already name without showing. It carries one
row, the same CR-SV-01 request the change-request example states, deciding it Postponed against the Saved
Views for Dashboards PRD, and it demonstrates the not-set fields this companion's Change Log section
describes: no priority, no estimate, and no target or delivery date, each stated as not set and why,
rather than invented to fill the table. Its cumulative-effect figure is none, and its keeper and review
cadence match the program's other governance logs.

---

## References

<a id="ref-1"></a>[1] Project Management Institute. "[Errata: A Guide to the Project Management Body of
Knowledge (PMBOK Guide), Sixth Edition (Fifth Printing)](https://www.pmi.org/-/media/pmi/documents/public/pdf/pmbok-standards/pmbok-guide-6th-edition-5th-printing.pdf?v=5ec5b4d9-abb5-4d42-8542-8af75be7de3b)."
pmi.org (accessed 2026-09-28). The change log named as an output of Perform Integrated Change Control
("The change log is used to record all submitted change requests."). Errata only; the PMBOK Guide itself
was not read. [primary]

<a id="ref-2"></a>[2] Project Management Institute. "[PMI Lexicon of Project Management Terms](https://www.pmi.org/-/media/pmi/documents/registered/pdf/pmbok-standards/pmi-lexicon-pm-terms.pdf?rev=447328d841c249af985d14177ddd5f95)."
Version 5.0, last updated January 2026 (accessed 2026-09-28). Confirms the Lexicon has no standalone
change-log entry, and defines the surrounding vocabulary instead ("change control. A process whereby
modifications to documents, deliverables, or baselines associated with the project are identified,
documented, approved, or rejected."). [primary]

<a id="ref-3"></a>[3] Association for Project Management. "[APM glossary of project management terms](https://www.apm.org.uk/resources/glossary/)."
apm.org.uk (accessed 2026-09-28). The two adjacent glossary entries this bundle draws its scope claim from
("Change log A record of all project changes: proposed, authorised, rejected or deferred."; "Change
register (or log) A record of all proposed changes to scope."). No licence stated. [primary]

<a id="ref-4"></a>[4] Association for Project Management. "[What is change control?](https://www.apm.org.uk/resources/what-is-project-management/what-is-change-control/)"
apm.org.uk (accessed 2026-09-28). Places logging the request as the first concrete step of change control
("Log change request in a change register (or log)."). [primary]

<a id="ref-5"></a>[5] Frank Turley (EMPII Group). "[Issues](https://prince2.wiki/practices/issues/)."
prince2.wiki (accessed 2026-09-28). PRINCE2's convention of recording a request for change in the issue
register, with a change log named only as an alternative destination for the decision ("Issues must be
recorded in the issue register."; "should be documented in the issue register or change log."). Creative
Commons Attribution. [practitioner]

<a id="ref-6"></a>[6] Frank Turley (EMPII Group). "[Change authority](https://prince2.wiki/people/change-authority/)."
prince2.wiki (accessed 2026-09-28). The change authority role and how the project board delegates it ("The
change authority is a person or group to whom the project board may delegate responsibility for reviewing
and approving change requests or off-specifications."). Creative Commons Attribution. [practitioner]

<a id="ref-7"></a>[7] European Commission / PM² Alliance. "[PM² Project Management Methodology Guide](https://www.pm2alliance.eu/wp-content/uploads/2024/02/pm%C2%B2-project-management-methodology-NO0523520ENN.pdf)."
v3.1, Appendix B.7 Change Log and Appendix B.10 Decision Log (accessed 2026-09-28). The seventeen-field,
four-group Change Log, its status and decision vocabularies, the escalation and traceability fields, and
the CC BY 4.0 licence ("A Change Log is used to document, monitor and control all project changes (see
Appendix B)."; "There are four possible decisions: approve, reject, postpone or merge the change request.";
"Escalation to the Directing or Steering layer is needed? (Yes or No)."; "Document licensed under CC BY 4.0
license"). [primary]

<a id="ref-8"></a>[8] PM² Alliance. "[Change Log](https://www.pm2.eu/change-log/)." pm2.eu artefacts listing
(accessed 2026-09-28). Confirms the Change Log ships as its own downloadable artefact, separate from the
Change Request Form ("This template is part of the Monitor & Control Logs."). [vendor]

<a id="ref-9"></a>[9] PM² Alliance / European Commission. "[PM²-Project Artefacts Change Note (v3.0.1 to v3.1)](https://pm2.europa.eu/document/download/005bb253-3e7e-4299-bd5d-f7cc26e9f8cc_en?filename=PM2-Project%20Artefacts.ChangeNote.from_.v3.0.1%20to%203.1.pdf)."
pm2.europa.eu (accessed 2026-09-28). Confirms the Change Log's field structure did not change between
v3.0.1 and v3.1 ("The new templates do not introduce any changes to the template structure or core
content."). [primary]

<a id="ref-10"></a>[10] Connecticut Department of Social Services, Enterprise PMO. "[Project Change Log v1.1](https://portal.ct.gov/-/media/Departments-and-Agencies/DSS/CT-METS/Library/General/CTDSSChangeLogv11.pdf)."
portal.ct.gov (accessed 2026-09-28). An eleven-column published log, its seven-value status list, and its
own name for itself ("Also known as Project Change Register"; "Status - Assign a status to the change
request; Submitted, In Review, Approved, Denied, Deferred, Withdrawn, or Closed."). No licence stated.
[primary]

<a id="ref-11"></a>[11] US Department of Health and Human Services, EPLC. "[Change Management Log](https://web.archive.org/web/20260226151501id_/https://www.hhs.gov/sites/default/files/ocio/eplc/EPLC%20Archive%20Documents/07%20-%20Change%20Management%20Plan/eplc_change_management_log.xls)."
spreadsheet, Internet Archive capture dated 2026-02-26 (accessed 2026-09-28, hhs.gov itself returns HTTP
403 to automated requests). The fifteen-column field list, the status and priority vocabularies, and their
internal inconsistencies ("Closed: The change request is no longer considered an active project threat and
can be closed with or without resolution."; "Valid options include the following: High, Medium, Low.";
"Critical: change request will stop project progress if not resolved."). [primary]

<a id="ref-12"></a>[12] US Department of Health and Human Services, EPLC. "[Change Management Plan template](https://web.archive.org/web/20260226151438id_/https://www.hhs.gov/sites/default/files/ocio/eplc/EPLC%20Archive%20Documents/07%20-%20Change%20Management%20Plan/eplc_change_management_plan_template.doc)."
Internet Archive capture dated 2026-02-26 (accessed 2026-09-28). The shared data-element list for the
request form and the log, the Change Manager as keeper, and the discretion clause ("The Change Manager
enters the CR into the CR Log."; "The product version that the suggested change is for"; "THE LIST OF
ELEMENTS IS AT THE DISCRETION OF THE PROJECT MANAGER."). [primary]

<a id="ref-13"></a>[13] University of California Office of the President, Information Technology Services.
"[Change Request Log Template](https://www.ucop.edu/information-technology-services/_files/itlc/3.5-supporting-change-request-log-template.xlsx)."
ucop.edu (accessed 2026-09-28). A seven-column log populated from a separate request form, and its named
keeper ("The Change Request Coordinator is responsible for maintaining the Change Request Log on behalf of
the Change Management Lead."; "Transfer the Date of Request, Change Request #, Change Request Title, the
resource assigned to the change request, the description of the change requested, current status and
implementation date from the change request form for each specific change request."). No licence stated.
[primary]

<a id="ref-14"></a>[14] San Francisco State University, IT Services. "[Change Management Log Template](https://its.sfsu.edu/sites/default/files/documents/Change_Management_Log_Template.xlsx)."
sfsu.edu (accessed 2026-09-28). A fifteen-column log whose fields, drop-downs and instructional prose are
effectively a verbatim copy of the HHS spreadsheet [[11]](#ref-11), found independently rather than
assigned. [primary]

<a id="ref-15"></a>[15] Keep a Changelog project. "[Keep a Changelog](https://keepachangelog.com/en/1.1.0/)."
version 1.1.0 (accessed 2026-09-28). What a software changelog records, and the absence of any
requester/decider/decision/status field ("A changelog is a file which contains a curated, chronologically
ordered list of notable changes for each version of a project."; "To make it easier for users and
contributors to see precisely what notable changes have been made between each release (or version) of the
project."; "Changelogs are for humans, not machines."). [practitioner]

<a id="ref-16"></a>[16] IT Process Maps (IT Process Wiki). "[ITIL Glossary / ITIL Terms C](https://wiki.en.it-processmaps.com/index.php/ITIL_Glossary/_ITIL_Terms_C)."
it-processmaps.com (accessed 2026-09-28). ITIL's two named change artifacts and the absence of any "change
log" entry ("The Change Record contains all the details of a Change, documenting the lifecycle of a single
Change."; "A Document that lists all approved Change Proposals and Changes and their planned implementation
dates."). [vendor]

<a id="ref-17"></a>[17] IT Process Maps (IT Process Wiki). "[Change Management](https://wiki.en.it-processmaps.com/index.php/Change_Management)."
it-processmaps.com (accessed 2026-09-28). Confirms the same two ITIL artifacts on the process page, and
continued absence of "change log" wording. [vendor]

<a id="ref-18"></a>[18] Wikipedia contributors. "[Change-advisory board](https://en.wikipedia.org/wiki/Change-advisory_board)."
wikipedia.org (accessed 2026-09-28). What the CAB oversees, and confirmation it names no cumulative
change-log artifact ("A change-advisory board (CAB) delivers support to a change-management team by
advising on requested changes, assisting in the assessment and prioritization of changes."). [reference]

<a id="ref-19"></a>[19] National Institute of Standards and Technology. "[SP 800-128, Guide for
Security-Focused Configuration Management of Information Systems](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-128.pdf)."
nist.gov (accessed 2026-09-28). Confirms NIST 800-128 uses no "change log" wording at all, naming
Configuration Change Control instead ("Configuration Change Control - process for managing updates to the
baseline configurations"; "Configuration change control is the documented process for managing and
controlling changes to the configuration of a system or its constituent CIs."). [primary]

<a id="ref-20"></a>[20] Lucid Meetings. "[What is a Decision Log?](https://www.lucidmeetings.com/glossary/decision-log)"
lucidmeetings.com (accessed 2026-09-28). Negative evidence: defines a decision log and never mentions a
change log. [vendor]

<a id="ref-21"></a>[21] ProjectManager.com. "[How to Use a Decision Log for Optimal Results for Your Project](https://www.projectmanager.com/blog/project-decision-log)."
projectmanager.com (accessed 2026-09-28). Negative evidence: its one mention of "change log" is a marketing
list of log types a tool supports, not a stated distinction ("Keep your project decision log, change log,
issue log, risk log, action log, raid log, risk register or any log you use on the task list view of our
software."). [vendor]

<a id="ref-22"></a>[22] Lark Suite. "[Change Log Project Management: A Comprehensive Guide](https://www.larksuite.com/library/project-management/project-management-concepts/change-log-project-management)."
larksuite.com (accessed 2026-09-28). Negative evidence: never mentions a decision log, so it draws no
boundary against one. [vendor]

<a id="ref-23"></a>[23] Project Management Knowledge. "[Change Log](https://project-management-knowledge.com/definitions/c/change-log/)."
project-management-knowledge.com (accessed 2026-09-28). Negative evidence: never mentions a decision log.
[practitioner]

<a id="ref-24"></a>[24] meetjamie.ai. "[What is a Decision Log?](https://www.meetjamie.ai/blog/decision-log)"
meetjamie.ai (accessed 2026-09-28). Negative evidence: describes decision logs at length and never states a
boundary against a named change log. [vendor]

<a id="ref-25"></a>[25] Plane. "[Decision log: What it is, why teams use it, and template](https://plane.so/blog/decision-log-what-it-is-why-teams-use-it-and-template)."
plane.so (accessed 2026-09-28). Negative evidence: the only sentences pairing "decision" with "change"
describe change as an input to a decision, never a stated boundary between two named log artifacts.
[vendor]

<a id="ref-26"></a>[26] US Department of Health and Human Services, EPLC. "[Change Management Practices Guide](https://web.archive.org/web/20260226151357id_/https://www.hhs.gov/sites/default/files/ocio/eplc/EPLC%20Archive%20Documents/07%20-%20Change%20Management%20Plan/eplc_change_management_practices_guide.pdf)."
Internet Archive capture dated 2026-02-26 (accessed 2026-09-28). The instruction to maintain a log
regardless of project size, the unique-entry rule, the review-cadence figure, and the approval threshold
example ("All projects, regardless of type or size, should maintain a change log and regularly manage
requested changes."; "Each change request should be recorded as a single line item. Do not combine
multiple requests under one change request ID."; "the review process may happen daily but should happen at
least weekly for even the simplest projects."; "a project manager (PM) may be authorized to personally
approve changes with a project impact of less than $5,000"). [primary]

<a id="ref-27"></a>[27] US Department of Health and Human Services, EPLC. "[Change Management Checklist v1.0](https://web.archive.org/web/20260226151616id_/https://www.hhs.gov/sites/default/files/ocio/eplc/EPLC%20Archive%20Documents/07%20-%20Change%20Management%20Plan/eplc_change_management_checklist.pdf)."
Internet Archive capture dated 2026-02-26 (accessed 2026-09-28). Names updating the log as the checklist's
one ongoing activity, with no role attached ("Update the Change Management Log."). [primary]

<a id="ref-28"></a>[28] William Meller. "[How to Handle Every Project Change Without Becoming the Person
Everyone Hates](https://projectmanagementcompass.substack.com/p/how-to-handle-every-project-change)."
Project Management Compass, Substack (accessed 2026-09-28, free preview only; the article is paywalled
past its outline, and nothing past the preview is cited). The decision-log-versus-change-log boundary, the
failure of undocumented informal decisions, and the proportionality guidance for a small project ("A
decision log tracks what was decided. A Change Control Log tracks what changed, why it changed, who
approved it, and what the impact was on the baseline."; "Changes happen. Decisions get made informally.
Nobody writes it down. And eventually, the project is living in a reality that the plan never accounted for
and nobody officially approved."; "A two-person project running for eight weeks does not need a Change
Control Board with quarterly meetings. It needs a lightweight log and a clear agreement between the project
manager and the sponsor about what requires formal approval versus what can be handled directly.").
[practitioner]

<a id="ref-29"></a>[29] Abdullah Oguz. "[Project Management: Navigating the Complexity](https://pressbooks.ulib.csuohio.edu/project-management-navigating-the-complexity/chapter/11-4-change-control-process/),"
ch. 11.4, Cleveland State University Pressbook, open textbook (accessed 2026-09-28). The project manager
as end-to-end owner of the change process, and the integration-into-plan column ("The project manager is
responsible to monitor the change process from the very beginning to the very end."; "Date Request
Integrated into Project Plan"). [academic]

<a id="ref-31"></a>[31] Ken Schwaber and Jeff Sutherland. "[The 2020 Scrum Guide](https://scrumguides.org/scrum-guide.html)."
scrumguides.org (accessed 2026-09-28). Scrum's own mechanism for changing the Product Backlog, and the
absence of any change-log or change-control vocabulary ("Those wanting to change the Product Backlog can
do so by trying to convince the Product Owner."). Licensed CC BY-SA 4.0. [primary]

<a id="ref-32"></a>[32] DORA (Google Cloud). "[Streamlining change approval](https://dora.dev/capabilities/streamlining-change-approval/)."
dora.dev (accessed 2026-09-28). What the finding is actually about, production-change approval by an
external body, used to state precisely what it does not claim about a project baseline change log ("no
evidence was found to support the hypothesis that a more formal, external review process was associated
with lower change fail rates"). [practitioner]

<a id="ref-33"></a>[33] US General Services Administration / Acquisition.gov. "[FAR 52.243-1, Changes, Fixed-Price](https://www.acquisition.gov/far/52.243-1)."
acquisition.gov (accessed 2026-09-28). The contracted, fixed-price mechanism for ordering a change and
recording an equitable adjustment against it ("The Contracting Officer may at any time, by written order,
and without notice to the sureties, if any, make changes within the general scope of this contract in any
one or more of the following: (1) Drawings, designs, or specifications..."). [primary]

<a id="ref-34"></a>[34] Cornell Law School Legal Information Institute (mirror of the US Code of Federal
Regulations). "[21 CFR 820.30(i), Design controls](https://www.law.cornell.edu/cfr/text/21/820.30)."
law.cornell.edu (accessed 2026-09-28). The regulated-industry requirement to document, review, and approve
a design change before implementation ("Each manufacturer shall establish and maintain procedures for the
identification, documentation, validation or where appropriate verification, review, and approval of
design changes before their implementation."). Mirror of a federal regulation. [primary]

<a id="ref-35"></a>[35] Ryan Singer / Basecamp. "[Bets, Not Backlogs](https://basecamp.com/shapeup/2.1-chapter-07),"
ch. 7, *Shape Up* (accessed 2026-09-28). The named, published rejection of a standing backlog in favor of
fixed-time, variable-scope betting ("Backlogs are a big weight we don't need to carry."). [practitioner]

<a id="ref-36"></a>[36] US Government Accountability Office. "[Information Technology: Agencies Need to
Establish Comprehensive Policies to Address Changes to Projects' Cost, Schedule, and Performance Goals](https://www.govinfo.gov/content/pkg/GAOREPORTS-GAO-08-925/html/GAOREPORTS-GAO-08-925.htm)."
GAO-08-925, 2008-07-31 (accessed 2026-09-28). An auditor's stated criteria for a documented baseline-change
decision, applied here to a change-log row by analogy; the report itself audits agency rebaselining
policies, not change logs ("A rebaselining policy should identify the authority who decides whether the
rebaselining is warranted and the rebaselining plan is acceptable."). [primary]

<a id="ref-37"></a>[37] Mike Wild FAPM ChPP. "[How do project managers control the decision to make a change?](https://www.apm.org.uk/blog/how-do-project-managers-control-the-decision-to-make-a-change/)"
Association for Project Management blog (accessed 2026-09-28). The register's audit-history function
against the baseline as first agreed ("It provides an audit history of how the change has been managed and
shows the additional time/cost/scope that has been approved since the project scope was first agreed.").
[practitioner]

<a id="ref-39"></a>[39] J. Timothy Beirnes, CPA, Inspector General. "[Monitoring Review of Construction
Change Orders from April 1, 2024 through September 30, 2024](https://www.sfwmd.gov/sites/default/files/documents/FINAL_Change_Order_Review_Sep_2024.pdf),"
Project #25-04, South Florida Water Management District Office of Inspector General (accessed
2026-09-28). A real auditor's review of a change-order system, applied by analogy to a project change log:
one date field conflating two different events, and cumulative approved change computed as a percentage
of the original contract ("It should be noted that the approval date in eBuilder represents the date that
the staff finalized the approval process for a change order and not the Governing Boards authorization
date."). The report's own subject is construction change orders, not a project change log. [primary]

<a id="ref-40"></a>[40] Project Management Formula. "[Change Log Template](https://projectmanagementformula.com/change-log-template/)."
projectmanagementformula.com (accessed 2026-09-28). Keeping a rejected request in the log with its reason,
and the target date diverging from the date work actually starts ("Keep them in the log with a clear
"Rejected" status and a note explaining why. This provides a record for future reference and prevents the
same request from being resubmitted without understanding why it was declined."; "By week eight, the
cumulative impact of those small changes had shifted the schedule by two weeks."). [vendor]
