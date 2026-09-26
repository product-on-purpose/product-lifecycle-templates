# Companion: The Change Request

> The deep explainer for the change-request bundle. Read this to understand what a change request is,
> where it came from, why it is shaped the way it is, and where practitioners disagree about it. The short
> operator card is [`change-request_guide.md`](change-request_guide.md); a fully worked instance is
> [`change-request_example.md`](change-request_example.md). Inline citations like [[1]](#ref-1) resolve to
> the [References](#references) at the bottom, tagged by source reliability.

---

## 1. Orientation

A change request is a formal proposal to alter something already agreed about a unit of product work: its
scope, requirements, a deliverable, or the schedule and cost attached to it. Four independently published
bodies define it in close to the same words. PMI's Lexicon: "change request. A formal proposal to modify a
document, deliverable, or baseline." [[1]](#ref-1). APM's glossary: "A request to obtain formal approval for
changes to the approved baseline." [[3]](#ref-3). The European Commission's PM² guide: "A change request
logs an appeal to amend an aspect of the agreed baseline of a project (i.e. scope, requirements,
deliverables, resources, costs, timeframe or quality characteristics)." [[7]](#ref-7). PRINCE2's practitioner
wiki: "It is a proposal for a change to a baselined product" [[5]](#ref-5).

The honest thing to say up front, and it is unusual for this library, is that the definition itself is not
what is contested. What is contested is where the document lives (its own artifact, or one type of issue),
whether the decision belongs on the same form as the request, whether the request is the log or a separate
thing that feeds one, and which of two lineages the name even means.

**At a glance**
- Four bodies agree on the definition almost word for word [[1]](#ref-1)[[3]](#ref-3)[[7]](#ref-7)
  [[5]](#ref-5); what disagrees is where the document lives, not what it says.
- This bundle serves the **project and product baseline** lineage. The IT service lineage, a change to a
  running production system reviewed by a change advisory board, is the closest neighbor and is described,
  never templated (section 8).
- A change request alters an agreement; a defect fails one [[31]](#ref-31). The template carries no Defect
  type even though two published forms offer one (section 3).
- One named decider chooses from a stated, closed set of decisions, never a bare yes or no
  [[7]](#ref-7)[[1]](#ref-1)[[6]](#ref-6).
- A team changing its own Product Backlog through its Product Owner does not need one [[21]](#ref-21); this
  bundle is for baselines that carry weight outside the team, a contract, a regulator, or a budget and scope
  a steering group already signed off on.

If you read nothing else: a change request is the record that gets a *decision*, made by a *named* person
or body, about whether an *already-agreed* baseline moves, and it says what happens if it does not.

---

## 2. Origins and evolution

No source names a single inventor of the change request. What the record shows instead is convergent naming
across every major project management body, each defining the same document from its own tradition: PMI's
formal-proposal wording [[1]](#ref-1), APM's approved-baseline wording [[3]](#ref-3), PRINCE2's
baselined-product wording [[5]](#ref-5), and PM²'s agreed-baseline wording [[7]](#ref-7). The PMBOK errata
adds the process the request feeds: "Perform Integrated Change Control is the process of reviewing all
change requests; approving changes and managing changes to deliverables, project documents, and the project
management plan; and communicating the decisions." [[2]](#ref-2).

**PM² is the source this companion draws its structure from**, for a reason beyond thoroughness: of the
bodies read, it is the one that publishes the complete process, all four decisions, and a matching form,
under a license that permits adaptation, "Reproduction and reuse is authorised provided the source is
acknowledged" [[7]](#ref-7). Its own Change Request Form template gives the field-level shape: "Current
Situation:", "Desired Situation:", "Impact or Risks:", "Out of Scope:" [[8]](#ref-8).

Four other named public bodies publish the form itself, and no two agree on its full shape. The CDC Unified
Process ships a three-section form, submitter, PM analysis, and board decision, offering "Enhancement" or
"Defect" as the type of change [[9]](#ref-9). The US GSA's Requirements Change Request Form offers "New
Requirement, Change to Existing Requirement, Defect" and a separate management-certification block that is
not the board's decision [[10]](#ref-10). Texas DIR's Project Change Request puts the approval block above
the definition fields and asks for Approve or Reject under a column headed "Recommendation" [[12]](#ref-12).
One body, HHS's EPLC program, merges the request form and the change log into a single field list rather than
keeping them apart, "AT A MINIMUM, THE FOLLOWING DATA SHOULD BE INCLUDED ON THE PROJECT'S CHANGE REQUEST FORM
AND CHANGE MANAGEMENT LOG" [[11]](#ref-11), a genuine documented alternative to the separate-artifacts
convention PM² and the PMBOK errata both follow. A university PMO's completion guidance describes the
sections a form should carry in prose rather than a template, and states plainly that the form is "logged
and reviewed" by a separate body once submitted [[13]](#ref-13).

**The type's own abbreviation collides with an unrelated document.** ITIL names its version of this artifact
a "request for change (RFC)" [[16]](#ref-16), and the same three letters name the IETF's entirely different
document series, the archival "Request for Comments" through which Internet standards are published and
discussed [[34]](#ref-34). This bundle's catalog metadata drops the alias "RFC (ITIL)" for exactly this
reason, since this library already ships an `rfc` bundle for the other meaning; this companion is the place
that collision is named for a reader who arrives having typed the wrong search.

**The IT service lineage is the closest neighbor, and it is not templated here.** NIST's SP 800-128 publishes
a full sample change request and a Configuration Control Board charter, but for a Configuration Control Board
established to govern a running information system's security posture, not a project's baseline
[[14]](#ref-14); NIST's SP 800-53 control CM-3 describes the same review-and-approve mechanism for
organizational systems generally [[15]](#ref-15). ITIL 4's glossary defines standard and emergency changes
and a change authority for service change enablement [[16]](#ref-16); the ITIL 2011 glossary also defines a
normal change, a term ITIL 4's glossary has no entry for, evidence that even ITIL's own vocabulary moved
between editions [[17]](#ref-17). IT Process Wiki's checklist routes any non-standard change
to a Change Advisory Board or Emergency CAB for approval [[18]](#ref-18), and Prairie View A&M's university IT
form carries a rollback description and a change control committee sign-off in the same lineage
[[48]](#ref-48).

**DORA's research belongs to that neighbor too, and this companion states its scope carefully.** The
2019 Accelerate report found "formal change management processes that require the approval of an external
body such as a change advisory board (CAB) or a senior manager for significant changes have a negative
impact on software delivery performance" [[20]](#ref-20), and DORA's own capability page restates the finding
for the same population, production and customer-facing IT service changes [[19]](#ref-19). No source read
applies this finding to a project baseline change board, and this companion does not either; it belongs to
the neighbor this bundle names and does not build.

---

## 3. Anatomy (section by section)

The template carries seven sections in full, four of them in lean: The Request, Why, Impact, and Decision
in both; Options Considered, Out of Scope, and Implementation and Traceability added in full.

### The Request

**What it is:** identifies the change, names the baseline it targets by artifact and version, and states
where it came from. **Why it exists:** PM²'s guide describes both routes a request can take: "formally
submitted via a Change Request Form, or... identified and raised during meetings as a result of decisions,
issues or risks" [[7]](#ref-7); PM²'s own form splits the description itself into two named fields, "Current
Situation:" and "Desired Situation:" [[8]](#ref-8), and a vendor source argues for keeping a third thing
separate from both, "Separate the underlying need from the requester's preferred implementation."
[[40]](#ref-40). **Beginner note:** name the baseline, which artifact and which version, the request is
against; without it, a reviewer cannot tell what "before" even means. **Expert note:** when the request came
from a decision, issue, or risk already logged elsewhere [[7]](#ref-7), link back to it rather than
restating it; that link is what keeps a change request from becoming its own untraceable island (section 8).

### Why

**What it is:** the reason for the change, including what happens if it is not made. **Why it exists:** PM²'s
process instructs the reviewer to "consider the impact of not implementing the proposed change"
[[7]](#ref-7); Texas DIR's form gives this its own named field, "Impact of Not Implementing" [[12]](#ref-12);
and a practitioner source treats it as decision-critical rather than optional context, "you should include
details of the consequence of not accepting the change" [[39]](#ref-39). **Beginner note:** write the
consequence of declining, not only the benefit of accepting; a request that argues only its upside gives a
reviewer half the decision. **Expert note:** the same practitioner source that asks for this field also
warns against writing it dishonestly, "do not over state the impact in an attempt to gain approval"
[[39]](#ref-39). Overstating the case to win approval is a named failure mode (section 7), and this is the
section where it happens.

### Impact

**What it is:** what the change costs, and what it touches, across the dimensions the baseline was agreed
on. **Why it exists:** PM²'s list runs across scope, requirements, deliverables, resources, costs, timeframe,
and quality [[7]](#ref-7); the CDC Unified Process form asks for hours, duration, schedule, and cost impact
[[9]](#ref-9); the GSA form asks for estimates [[10]](#ref-10); Texas DIR carries a dedicated schedule-impact
table [[12]](#ref-12). **Beginner note:** impact outside the project itself is worth a line even where the
template gives it no field of its own; one source names the case directly, "it could have an adverse impact
on an external project" [[39]](#ref-39), which this bundle treats as a hint for the row rather than a section
of its own. **Expert note:** keep the risk of making the change separate from the risk of not making it, per
one vendor source, "Distinguish the risk of making the change from the risk of declining or delaying it"
[[40]](#ref-40); this is a useful distinction inside the section even where the template does not force two
separate columns for it, and it is vendor-tier guidance, not a settled convention.

### Decision

**What it is:** the outcome, chosen from a stated set, made by one named decider, by a stated date, with any
conditions spelled out. **Why it exists:** PM² names four possible decisions, "approve, reject, postpone or
merge the change request" [[7]](#ref-7); PMI's Lexicon defines the deciding body, a change control board
"responsible for reviewing, evaluating, approving, delaying, or rejecting changes" [[1]](#ref-1); PRINCE2
delegates the decision to a named change authority that "may be given a change budget and can approve
changes within that budget," illustrated with a worked delegation of changes under 400 euros to the project
manager [[6]](#ref-6). **Beginner note:** pick the decision from the set the template offers rather than
inventing a new one; the set differs by body, APM names three outcomes [[4]](#ref-4), PM² names four
[[7]](#ref-7), and the CDC Unified Process form adds a fifth, "More Info" [[9]](#ref-9), so a bespoke choice
this template does not offer just means the next reader has to guess what it meant. **Expert note:** two
fields belong here that the published forms above do not universally carry, and this companion says plainly
that both rest on thinner evidence than the rest of the section. A date by which the decision is needed:
"a change request without a deadline gives the board permission to defer indefinitely" [[41]](#ref-41),
corroborated by a practitioner source naming the same field [[39]](#ref-39). And, where the decision is
approval with conditions, an owner and a deadline for each one: "Approval with conditions must identify the
owner and deadline for each condition" [[40]](#ref-40). Both sources are vendor tier, and the template's own
guidance says so rather than presenting either field as an industry standard.

### Options Considered (full only)

**What it is:** the alternatives weighed, including doing nothing, and why the chosen option won. **Why it
exists:** a widely distributed free template names it directly, "Options considered to implement the
change," scored per option "on Cost, Scope, Schedule and Quality" [[43]](#ref-43); one vendor source insists
the no-change option itself belongs on the list, "Include the no-change option plus realistic alternatives"
[[40]](#ref-40); Texas DIR's form carries a plainer version of the same idea, an Alternatives field
[[12]](#ref-12). **Beginner note:** write the no-change option even when it obviously loses; a reviewer who
cannot see it was considered cannot tell whether it was rejected or never asked. **Expert note:** the naive
baseline this section is scaling up from is real and published. Two independently written sources describe a
change request with no options field at all, only a single "Proposed resolution" [[44]](#ref-44), or a
five-step process that never names alternatives at all [[45]](#ref-45). Moving to full is the decision to
stop being that baseline.

### Out of Scope (full only)

**What it is:** a stated boundary naming what the change explicitly does not touch. **Why it exists:** PM²'s
own form carries this as a named section, "Out of Scope:" [[8]](#ref-8), and one vendor source states the
rule behind it, "Define what will be added, removed or modified and what remains explicitly out of scope."
[[40]](#ref-40). **Beginner note:** a boundary that is not written down is not a boundary; the next reader
will assume everything not explicitly excluded is included. **Expert note:** this section is easy to skip on
a small change and expensive to skip on a large one; scale how much is written to how much a reviewer could
plausibly misread as included.

### Implementation and Traceability (full only)

**What it is:** what happens to the request once it is decided, where it is logged, and what it links to.
**Why it exists:** PM²'s own form is archived once logged, "Once the change request is logged into the
Change Log, then this form is updated with the assigned Change ID and the form is archived" [[8]](#ref-8);
the PMBOK errata states the log's job in the same terms, "The change log is used to record all submitted
change requests." [[2]](#ref-2); the richest single source found for what a full record should let a later
reader do states it plainly, "A sound record lets an authorized reviewer reconstruct the prior baseline,
requested difference, evidence, options, authority, implementation and result" [[40]](#ref-40). **Beginner
note:** the request is not the log; it feeds one. If the project keeps no change log, say so here rather
than leaving the section to imply one exists. **Expert note:** the same vendor source warns against a
related failure this section can hide, multiple approving authorities collapsed into one status: "do not
collapse them into an overall green status before every mandatory approval is satisfied" [[40]](#ref-40).
Where more than one authority must sign off, record each decision separately rather than one merged line.

---

## 4. Variants and sizing

**Lean** is The Request, Why, Impact, and Decision, four sections, enough to get a single, well-reasoned
decision recorded and dated. It is enough for a change small enough that one reviewer can weigh it without a
documented set of alternatives.

**Full** is a strict superset, adding Options Considered, Out of Scope, and Implementation and Traceability.
Move up when the decision needs a documented set of alternatives (including the no-change option), when the
boundary of what the change touches is genuinely ambiguous, or when the project keeps a change log the
request must feed into cleanly.

---

## 5. Methodology lineage

- **PMI / PMBOK.** The broadest wording of the four, a named change control board, and a separate change log
  with no stated rule for its overlap with an issue log [[1]](#ref-1)[[2]](#ref-2).
- **APM.** Anchors both terms to "approved baseline," and a three-outcome control process, capture, evaluate,
  then approve, reject, or defer [[3]](#ref-3)[[4]](#ref-4).
- **PRINCE2.** Files a change request as one of five types of issue, not a standalone document category, and
  delegates the decision to a named, budget-holding change authority rather than a standing board
  [[5]](#ref-5)[[6]](#ref-6).
- **PM² (European Commission).** The fullest published field list and process, and the only source this
  bundle may adapt directly, under a CC BY 4.0 license [[7]](#ref-7)[[8]](#ref-8).
- **IT service management (ITIL, NIST SecCM, IT Process Wiki).** The neighbor, described and not templated:
  a request to change a running system, reviewed by a change advisory or control board
  [[14]](#ref-14)[[15]](#ref-15)[[16]](#ref-16)[[17]](#ref-17)[[18]](#ref-18).
- **Agile.** Routes change through one channel and one accountable person: the Product Owner and the Product
  Backlog. No artifact named a change request appears anywhere in the Scrum Guide [[21]](#ref-21), and the
  Manifesto's own values place responding to change above following a plan [[22]](#ref-22)[[23]](#ref-23).
  Where an agreed baseline carries weight outside the team, a contract [[26]](#ref-26)[[27]](#ref-27)
  [[24]](#ref-24) or a regulator [[25]](#ref-25), formal change control survives inside agile delivery rather
  than being replaced by it (section 6).

---

## 6. Debates and contested boundaries

**Is a change request an issue?** PRINCE2 says yes, definitionally: "There are five types of issues; they
are: Request for change" [[5]](#ref-5). PMI [[1]](#ref-1)[[2]](#ref-2), APM [[3]](#ref-3)[[4]](#ref-4), and
PM² [[7]](#ref-7) each treat it as its own document, and PMI and PM² each keep a separate change log for it. This library's ruling, carried over
from this library's own `issue-log` bundle's routing, is that the request records where it came from and
links back to the issue log when there is one, rather than picking a side. PRINCE2's own page concedes the
overlap is not absolute either: "The issues practice is not solely about handling change requests"
[[5]](#ref-5).

**Does the decision belong on the form?** PM²'s Change Request Form template carries no decision section at
all; the decision is made after the form is logged [[8]](#ref-8). The CDC Unified Process and GSA forms both
carry a named decision section, "CHANGE CONTROL BOARD - DECISION" and "Change Control Board Approval
Information" [[9]](#ref-9)[[10]](#ref-10). Texas DIR puts per-approver checkboxes under a column headed
Recommendation, placed above the request's own definition fields [[12]](#ref-12). This bundle's own template
keeps the decision inside the same document (section 3), following the majority of published forms rather
than PM²'s split.

**Is the request separate from the log?** PM²'s form is archived once logged [[8]](#ref-8), and the PMBOK
errata treats the log as the separate register [[2]](#ref-2). HHS's EPLC program merges the two into one
field list instead [[11]](#ref-11). This is a genuine, documented split in convention, not a mistake in one
source; this bundle follows the separate-artifacts convention and names the merged one as an alternative.

**Are defects change requests?** The GSA form offers Defect as a type of change [[10]](#ref-10), and the CDC
Unified Process form offers Enhancement or Defect [[9]](#ref-9). A practitioner source draws the opposite
line: a bug is "something is wrong with the delivered code," a change request is "new and additional to
what was delivered" [[31]](#ref-31). This library's `bug-report` guide follows the practitioner line, and
this template offers no Defect type even though two published forms do.

**What can the decision be?** PM² states four: "approve, reject, postpone or merge the change request"
[[7]](#ref-7). APM states three: "captured, evaluated and then approved, rejected or deferred"
[[4]](#ref-4). PMI's change control board is "responsible for reviewing, evaluating, approving, delaying, or
rejecting changes" [[1]](#ref-1). The CDC Unified Process form adds approval with conditions and a request
for more information as further options [[9]](#ref-9). No two published vocabularies match exactly; this
bundle follows PM²'s four, since PM² is the source it may adapt directly.

**Does agile work need one?** The 2020 Scrum Guide routes change through one person, "Those wanting to
change the Product Backlog can do so by trying to convince the Product Owner" [[21]](#ref-21), and the
Manifesto values "Responding to change over following a plan" [[22]](#ref-22). Against that, a Wikipedia
survey of agile contract types shows fixed-price agile contracts carrying change-control provisions of their
own [[24]](#ref-24), Jeff Sutherland's own contract clauses write change into the agreement itself, priced at
Sprint boundaries [[27]](#ref-27), and an experience report from an FDA-regulated project shows formal design
change control surviving inside agile delivery because a regulator requires it [[25]](#ref-25). Ron Jeffries
makes the strongest named-practitioner case for the middle ground, that fixed contracts already carry change
control provisions in practice and directly rebuts the view that fixed-scope work cannot be done in an agile
way [[26]](#ref-26). **This is genuinely unresolved, and this companion reports both camps rather than
picking one.**

**What DORA's finding is actually about.** The 2019 Accelerate report and DORA's current capability page
both concern approval of production changes by an external body, "formal change management processes that
require the approval of an external body such as a change advisory board (CAB) or a senior manager for
significant changes have a negative impact on software delivery performance" [[20]](#ref-20)[[19]](#ref-19).
DORA's own report also states the CAB retains "an important role" in a continuous-delivery paradigm
[[20]](#ref-20). **No source read applies this finding to a project baseline change board, and this bundle
must not either.**

**Change boards as bottlenecks or rubber stamps.** Sourced only for IT service change boards, by named ITSM
consultants: "CABs belong in history as an example of how ITSM put a straightjacket around agility and
innovation" [[36]](#ref-36). No project-management source for the same claim about a project baseline change
board was found in this research, and this companion does not extend the claim to one.

**How much a request needs.** Lean templates stop at requestor, description, reason, impact, and approval
[[44]](#ref-44)[[45]](#ref-45); one free template adds options, each with its impact and the reason one was
chosen [[43]](#ref-43); other sources argue that without options, conditions, a
deadline, and a decision record the process degrades [[40]](#ref-40)[[41]](#ref-41). Both camps sit at
practitioner or vendor tier; neither is a standards-body position.

---

## 7. Anti-patterns and failure modes

1. **Change that is never authorized.** Scope creep is defined by authorization, not size: "The key part is
   whether changes are authorized or not. If an expansion of scope is approved, then it is not scope creep."
   [[35]](#ref-35). Fix: route every scope change through this document, however lightweight, rather than
   letting it enter through conversation.
2. **Decisions that never get made.** A practitioner names change requests among the things whose
   postponement goes untracked, "the cost of decisions not made" [[37]](#ref-37), and a second, vendor-tier
   source corroborates the same pattern from a different angle, advising that requests not be left pending or
   in some other purgatory status [[38]](#ref-38). A third, vendor-tier source traces the pattern to a
   specific missing field, "A change request without a deadline gives the board permission to defer
   indefinitely" [[41]](#ref-41). **All three are thin evidence**, a 2026 personal blog post and two vendor
   posts, not a measured finding; the fix this bundle recommends, a stated decision date (section 3), is
   labeled accordingly rather than presented as settled practice.
3. **Overstating the case to win approval.** A practitioner source states the caution directly: "do not over
   state the impact in an attempt to gain approval" [[39]](#ref-39). Fix: write the Why section's
   consequence honestly, not persuasively.
4. **Calling a request a bug, or a bug a request.** Misclassification causes friction because it implies the
   delivered work was defective when it was not: "mixing up the two... drives me crazy, as I feel that the
   person reporting it... thinks that what was delivered is wrong in some way" [[31]](#ref-31). Fix: use
   `bug-report` for something that fails a promise already made, and this template for something new.
5. **Multiple approving authorities collapsed into one status.** "Do not collapse them into an overall green
   status before every mandatory approval is satisfied" [[40]](#ref-40); a second, practitioner-tier source
   names the same discipline as a board best practice, "all CCB change decisions must be properly documented
   with context and rationale" and warns that without it "decisions can get lost leading to misalignment"
   [[46]](#ref-46). Fix: record each authority's decision on its own line.
6. **Undocumented, unassessed change reaching production regardless of paperwork.** This is an engineering
   parallel rather than a project-management finding, and this companion states it as one: a documented
   industrial disaster is traced directly to a change that "had not been properly thought out, documented
   and risk-assessed" [[42]](#ref-42). It is included here as a reason traceability is worth the friction it
   adds, not as evidence about project baseline change requests specifically.

---

## 8. Relationships to other artifacts

**This bundle's position in the family chain.** The `delivery-docs` family contract places this type
directly: a change request "alters what was agreed about it once that agreement exists," once a PRD or
Product Backlog has opened the chain, stories or a Sprint Backlog have decomposed it, and acceptance criteria
have confirmed it. The contract change that admitted this bundle is
[ADR 0060](../../docs/internal/decisions/0060-change-request-joins-delivery-docs.md) (change request joins
delivery-docs), which widened the family's membership test with the verb "changes" after testing this type
against all nine of this library's family contracts and finding that none admitted it as written.

**Change request vs. issue log.** PRINCE2 treats a request for change as one of five issue types
[[5]](#ref-5); PMI, APM, and PM² each keep it as its own document instead [[1]](#ref-1)[[3]](#ref-3)
[[7]](#ref-7). This library's own ruling, carried from `issue-log`'s routing, does not pick a side: the
request records where it came from and links back to the issue log when there is one.

**Change request vs. bug report.** The boundary is tense and origin, not severity: a bug is something wrong
with what was delivered, a change request is something new that was never promised [[31]](#ref-31). This
library's `bug-report_guide.md` sends a reader asking for behavior nothing promised to this bundle instead of
treating the request as a defect.

**Change request vs. the change log.** The request is not the log; PM²'s form is archived once logged into
one [[8]](#ref-8), and the PMBOK errata describes the log as the register that collects submitted requests
[[2]](#ref-2). HHS's EPLC program merges the two, a documented alternative rather than an error
[[11]](#ref-11). A standing change log, if this library ever builds one, is a `governance-docs` candidate,
not a variant of this bundle.

**Change request vs. IT service change (the neighbor).** A change to a running production system, reviewed
by a change advisory board under ITIL or a Configuration Control Board under NIST's SecCM guidance, is this
bundle's closest neighbor and is deliberately not templated here [[14]](#ref-14)[[15]](#ref-15)
[[16]](#ref-16)[[17]](#ref-17)[[18]](#ref-18); DORA's research on external approval belongs to that neighbor,
not to a project baseline board (section 6).

**Change request vs. the change authority or board that decides it.** PRINCE2 delegates the decision to a
named, budget-holding change authority [[6]](#ref-6); PMI and PM² instead name a standing change control
board [[1]](#ref-1)[[7]](#ref-7). Either shape can hold the Decision section's named decider (section 3).

---

## 9. Adaptations

- **PM²-based teams.** Adopt the five-step process and the four-decision vocabulary with attribution, since
  PM² is the source this bundle may adapt directly [[7]](#ref-7).
- **PRINCE2 teams.** File the change request as an issue type, following PRINCE2's own convention
  [[5]](#ref-5), and decide explicitly whether a change authority holds a delegated budget the way PRINCE2's
  worked example does [[6]](#ref-6).
- **Regulated or contract-bound teams.** Keep formal change control even where the rest of delivery is
  agile. An FDA-regulated project keeps "Design changes" and "Change control procedures" as named, required
  elements of its design history file inside an otherwise agile process [[25]](#ref-25), and named contract
  clauses put an explicit price on change instead of pretending a fixed contract has none
  [[27]](#ref-27)[[26]](#ref-26)[[24]](#ref-24).
- **Agile teams without an external baseline.** Skip the change request and route change through the
  Product Owner and the Product Backlog instead [[21]](#ref-21).
- **Public-sector and IT teams.** The published forms surveyed here are useful as structure evidence rather
  than adoptable text, since none states a reuse license beyond PM²'s [[9]](#ref-9)[[10]](#ref-10)
  [[12]](#ref-12)[[14]](#ref-14)[[48]](#ref-48).

---

## 10. Worked example

[`change-request_example.md`](change-request_example.md) chains onto the Saved Views PRD from this library's
shared delivery-docs scenario. The PRD lists "Scheduled delivery of a view by email or Slack" as an
out-of-scope non-goal, and the example's request asks to bring that non-goal into scope. The decision it
demonstrates is postpone, one of PM²'s four named decisions [[7]](#ref-7), sending the change to a follow-on
release rather than approving or rejecting it outright, and it deliberately states no release number, since
the release numbering across this library's other worked examples is not yet internally consistent.

---

## References

<a id="ref-1"></a>[1] Project Management Institute. "[Lexicon of Project Management Terms](https://www.pmi.org/-/media/pmi/documents/registered/pdf/pmbok-standards/pmi-lexicon-pm-terms.pdf?rev=447328d841c249af985d14177ddd5f95)." Version 5.0 (accessed 2026-09-25). Canonical definitions of change request, change control, and the change control board, cross-referenced to baseline ("change request. A formal proposal to modify a document, deliverable, or baseline."; "change control board (CCB). A formally chartered group responsible for reviewing, evaluating, approving, delaying, or rejecting changes to the project, and for recording and communicating such decisions."). Licensed for personal use only; quoted briefly, never adapted. [primary]

<a id="ref-2"></a>[2] Project Management Institute. "[A Guide to the Project Management Body of Knowledge (PMBOK Guide)](https://www.pmi.org/-/media/pmi/documents/public/pdf/pmbok-standards/pmbok-guide-6th-edition-5th-printing.pdf?v=5ec5b4d9-abb5-4d42-8542-8af75be7de3b)." Sixth edition, errata, fifth printing (accessed 2026-09-25). The Perform Integrated Change Control process and the change log's role as the register of submitted change requests ("The change log is used to record all submitted change requests."; "Perform Integrated Change Control is the process of reviewing all change requests; approving changes and managing changes to deliverables, project documents, and the project management plan; and communicating the decisions."). The errata only; the Guide's own body was not read. [primary]

<a id="ref-3"></a>[3] Association for Project Management. "[Glossary](https://www.apm.org.uk/resources/glossary/)." apm.org.uk (accessed 2026-09-25). APM's definitions of change request and change control board, both anchored to the approved baseline ("A request to obtain formal approval for changes to the approved baseline."; "A formally constituted group of stakeholders responsible for approving or rejecting changes to the project baselines."). No license stated. [standards]

<a id="ref-4"></a>[4] Association for Project Management. "[What is change control?](https://www.apm.org.uk/resources/what-is-project-management/what-is-change-control/)" apm.org.uk (accessed 2026-09-25). The change-control process, capture, evaluate, then approve, reject, or defer, and change requests commonly arising from issues ("Change requests may arise as a result of issues that occur from the management of work or external sources."; "captured, evaluated and then approved, rejected or deferred"). [standards]

<a id="ref-5"></a>[5] Frank Turley (EMPII Group). "[Issues](https://prince2.wiki/practices/issues/)." prince2.wiki (accessed 2026-09-25). PRINCE2's taxonomy filing a request for change as one of five issue types, plus its concession that the issues practice is broader than change handling ("There are five types of issues; they are: Request for change : It is a proposal for a change to a baselined product, i.e., a product that has already been approved."; "The issues practice is not solely about handling change requests."). Creative Commons Attribution. [practitioner]

<a id="ref-6"></a>[6] Frank Turley (EMPII Group). "[Change authority](https://prince2.wiki/people/change-authority/)." prince2.wiki (accessed 2026-09-25). PRINCE2's delegated change authority, distinct from the project board, and a worked delegation example ("The change authority is a person or group to whom the project board may delegate responsibility for reviewing and approving change requests or off-specifications. This authority may be given a change budget and can approve changes within that budget."; "with a level 2 issue (change request), The project manager could approve a change if only one product is affected and the change is under €400"). Creative Commons Attribution. [practitioner]

<a id="ref-7"></a>[7] European Commission. "[PM² Project Management Methodology Guide](https://www.pm2alliance.eu/wp-content/uploads/2024/02/pm%C2%B2-project-management-methodology-NO0523520ENN.pdf)." Open Edition v3.1, Publications Office of the European Union, 2023 (accessed 2026-09-25). The fullest published change-request definition, five-step process, and four-decision vocabulary, under a license permitting reuse ("A change request logs an appeal to amend an aspect of the agreed baseline of a project (i.e. scope, requirements, deliverables, resources, costs, timeframe or quality characteristics)."; "There are four possible decisions: approve, reject, postpone or merge the change request."; "b) consider the impact of not implementing the proposed change"; "Reproduction and reuse is authorised provided the source is acknowledged. Document licensed under CC BY 4.0 license."). [standards]

<a id="ref-8"></a>[8] PM² Alliance. "[PM² Change Request Form template](https://www.pm2.center/wp-content/uploads/2022/02/21.I.PM2-Template.v3.Change_Request_Form.ProjectName.dd-mm-yyyy.vx_.x-1.docx)." v3.0.1 (accessed 2026-09-25). Field-level structure: "Current Situation:", "Desired Situation:", "Out of Scope:", and the form's own archive-once-logged rule ("Once the change request is logged into the Change Log, then this form is updated with the assigned Change ID and the form is archived"). [primary]

<a id="ref-9"></a>[9] CDC Unified Process (Daniel Vitek). "[Change Request Form (example)](http://web.archive.org/web/20240601190446id_/https://www2a.cdc.gov/cdcup/library/templates/CDC_UP_Change_Request_Form_Example.doc)." Archived copy (accessed 2026-09-25). Three-section structure (submitter, PM analysis, board decision), a Defect option, and a four-state decision vocabulary ("3.) CHANGE CONTROL BOARD - DECISION"; "Approved", "Rejected", "More Info"; "Type of CR"; "Defect"). Read from the Internet Archive; the live copy 404s. [primary]

<a id="ref-10"></a>[10] U.S. General Services Administration. "[M3 Playbook Change Request Form Template](https://ussm.gsa.gov/assets/files/M3-Playbook-Change-Request-Form-Template.docx)." (accessed 2026-09-25). Field structure offering Defect as a type of change and a board decision vocabulary distinct from a certification block ("Type of Change"; "New Requirement, Change to Existing Requirement, Defect"; "Change Control Board Approval Information"; "Board Decision"). [primary]

<a id="ref-11"></a>[11] U.S. Department of Health and Human Services, EPLC. "[Change Management Plan template](http://web.archive.org/web/20260226151438id_/https://www.hhs.gov/sites/default/files/ocio/eplc/EPLC%20Archive%20Documents/07%20-%20Change%20Management%20Plan/eplc_change_management_plan_template.doc)." (accessed 2026-09-25). Merges the change request form and the change log into one field list, the documented alternative to the separate-artifacts convention ("Change Request Form and Change Management Log"; "AT A MINIMUM, THE FOLLOWING DATA SHOULD BE INCLUDED ON THE PROJECT'S CHANGE REQUEST FORM AND CHANGE MANAGEMENT LOG"). Read from the Internet Archive; the live copy 403s. [primary]

<a id="ref-12"></a>[12] Texas Department of Information Resources. "[PM Essentials Project Change Request Template](https://dir.texas.gov/sites/default/files/2021-08/PM%20Essentials%20Change%20Request%20Template_ver01%20(1).docx)." (accessed 2026-09-25). Approval block placed above the definition fields, Approve or Reject under a Recommendation column, and an Alternatives field ("Project Change Request"; "Recommendation"; "Alternatives"; "retained to memorialize any changes or denial of changes"). [primary]

<a id="ref-13"></a>[13] University of Iowa Health Care, Health Care Information Systems PMO. "[Change Request](https://hcis.healthcare.uiowa.edu/pmo/changerequest.html)." (accessed 2026-09-25). Completion guidance describing sections in prose and stating the form is logged and reviewed separately ("Project Impact Analysis"; "the change request form will be logged and reviewed by the Project Core Team"). [practitioner]

<a id="ref-14"></a>[14] National Institute of Standards and Technology. "[SP 800-128, Guide for Security-Focused Configuration Management of Information Systems](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-128.pdf)." (accessed 2026-09-25). A sample change-request template and a Configuration Control Board charter for a running information system's security posture, not a project baseline ("The following is a sample template for a Change Request artifact that can be used within a SecCM program."; "The Configuration Control Board (CCB) represents the interests of program and project management by ensuring that a structured process is used to consider proposed changes"). [primary]

<a id="ref-15"></a>[15] National Institute of Standards and Technology. "[SP 800-53 Rev. 5, Security and Privacy Controls for Information Systems and Organizations](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-53r5.pdf)." Control CM-3 (accessed 2026-09-25). Configuration change control naming Configuration Control Boards or Change Advisory Boards as the review-and-approve mechanism for organizational systems ("Processes for managing configuration changes to systems include Configuration Control Boards or Change Advisory Boards that review and approve proposed changes."). [primary]

<a id="ref-16"></a>[16] PeopleCert (redistributed by iGEN). "[ITIL 4 Foundation Glossary](https://igen.nl/wp-content/uploads/2024/10/ITIL-4-Foundation_Glossary_Digital.pdf)." (accessed 2026-09-25). ITIL 4's change-enablement vocabulary and the confirmed absence of a "normal change" entry ("request for change (RFC) A description of a proposed change used to initiate change enablement."; "standard change A low-risk, pre-authorized change that is well understood and fully documented"; "change authority A person or group responsible for authorizing a change."). [vendor]

<a id="ref-17"></a>[17] AXELOS/OGC-derived, mirrored by Boston University IT. "[ITIL Glossary and Abbreviations](https://www.bu.edu/tech/files/2018/10/ITIL%C2%AE-glossary-and-abbreviations.pdf)." ITIL 2011 edition (accessed 2026-09-25). The 2011 glossary's normal change and change advisory board definitions, the vocabulary ITIL 4's later glossary drops the "normal change" term from ("A change that is not an emergency change or a standard change. Normal changes follow the defined steps of the change management process."; "A group of people that support the assessment, prioritization, authorization and scheduling of changes."). [vendor]

<a id="ref-18"></a>[18] Stefan Kempter (IT Process Maps). "[Checklist Request for Change (RFC)](https://wiki.en.it-processmaps.com/index.php/Checklist_Request_for_Change_RFC)." IT Process Wiki (accessed 2026-09-25). A practitioner RFC content checklist and the routing of any non-standard change to a Change Advisory Board or Emergency CAB ("The RFC is a precursor to the 'Change Record' and contains all information required to approve a Change."; "A Request for Change is to be submitted to Change Management for any non-standard Change"). [practitioner]

<a id="ref-19"></a>[19] DORA (Google Cloud program). "[Streamlining change approval](https://dora.dev/capabilities/streamlining-change-approval/)." Capability guide (accessed 2026-09-25). The current-form finding, scoped entirely to production and customer-facing IT service changes ("Traditionally, these goals have been met through a heavyweight process involving approval by people external to the team proposing the change: a change advisory board (CAB) or a senior manager. However, DORA's research shows that these approaches have a negative impact on software delivery performance."; "In the continuous delivery paradigm the CAB still has a vital role"). [practitioner]

<a id="ref-20"></a>[20] Forsgren, Humble, et al. (DORA / Google Cloud). "[Accelerate: State of DevOps 2019](https://dora.dev/research/2019/dora-report/2019-dora-accelerate-state-of-devops-report.pdf)." (accessed 2026-09-25). The primary research: production-system change approval, framed around release risk management, never project baseline management ("We found that formal change management processes that require the approval of an external body such as a change advisory board (CAB) or a senior manager for significant changes have a negative impact on software delivery performance."; "Continuous delivery offers a superior risk management approach compared to traditional change management processes, but there is still an important role for the CAB."). [primary]

<a id="ref-21"></a>[21] Ken Schwaber and Jeff Sutherland. "[The 2020 Scrum Guide](https://scrumguides.org/scrum-guide.html)." scrumguides.org (accessed 2026-09-25). Change enters through one channel and one accountable person; no artifact named a change request appears in the Guide ("Those wanting to change the Product Backlog can do so by trying to convince the Product Owner."; "The Product Owner is one person, not a committee."). Licensed CC BY-SA 4.0. [primary]

<a id="ref-22"></a>[22] Agile Manifesto authors. "[Manifesto for Agile Software Development](https://agilemanifesto.org/)." (accessed 2026-09-25). The fourth value placing responding to change above following a plan ("Responding to change over following a plan"). [primary]

<a id="ref-23"></a>[23] Agile Alliance authors. "[Principles behind the Agile Manifesto](https://agilemanifesto.org/principles.html)." (accessed 2026-09-25). Welcoming late requirement change as a competitive weapon rather than gating it through a control board ("Welcome changing requirements, even late in development. Agile processes harness change for the customer's competitive advantage."). [primary]

<a id="ref-24"></a>[24] Wikipedia contributors. "[Agile contracts](https://en.wikipedia.org/wiki/Agile_contracts)." (accessed 2026-09-25). Names the contract families that formalize where change enters an agile engagement outside a single team's Product Backlog ("Further aspects of an Agile contract are risk share... or the option of either party leaving the contract at any stage (exit points)."). [reference]

<a id="ref-25"></a>[25] Certified Compliance Solutions / Agiletek (Hughes, Skach, Jenks, Rasmussen). "[Moving to Agile in an FDA Environment: An Experience Report](https://www.agilealliance.org/wp-content/uploads/2017/05/Moving-to-Agile-in-an-FDA-Environment.pdf)." Agile Alliance, 2009 (accessed 2026-09-25). Design changes and change control procedures as named, required elements of an FDA design history file inside an agile project ("Design changes"; "Change control procedures"; "Manage scope and limit feature creep"). [practitioner]

<a id="ref-26"></a>[26] Ron Jeffries. "[Fixed-Everything: Agile?](https://ronjeffries.com/articles/019-01ff/fixed-everything-agile/)" ronjeffries.com (accessed 2026-09-25). The clearest named-practitioner statement that fixed contracts already carry change control provisions and are not actually static ("Most such contracts, in my experience, include "change control" provisions."; "I think Agile works as well as anything, better than most, in such situations, and I don't agree with what Allen said."). [practitioner]

<a id="ref-27"></a>[27] Jeff Sutherland. "[Agile Contracts: Money for Nothing and Your Change for Free](http://jeffsutherland.com/scrum/2008/10/agile-contracts-money-for-nothing-and.html)." Scrum Log Jeff Sutherland, 2008 (accessed 2026-09-25). Primary contract clause text pricing termination and change at Sprint boundaries ("Clause: Change For Free"; "Customer shall be able to make changes to the Scope without incurring any additional cost if total Scope of contracted work is not changed. New features may be added for free at Sprint boundaries if items of equal scope are removed from the contract."). [practitioner]

<a id="ref-31"></a>[31] Ian Devlin. "[Bugs and Change Requests](https://iandevlin.com/blog/2015/06/opinion/bugs-and-change-requests/)." Personal blog, 2015 (accessed 2026-09-25). The bug-versus-change-request boundary this library's `bug-report` guide follows ("a bug means one thing, something is wrong with the delivered code... and it needs to be identified and fixed."; "Change requests however, are something different. These are things that are new and additional to what was delivered"). [practitioner]

<a id="ref-34"></a>[34] S. Bradner. "[RFC 2026, The Internet Standards Process, Revision 3](https://datatracker.ietf.org/doc/html/rfc2026)." IETF, 1996 (accessed 2026-09-25). Confirms the acronym collision this bundle's catalog metadata must avoid: the IETF's "Request for Comments" is an entirely different document series from ITIL's "request for change" ("Each distinct version of an Internet standards-related specification is published as part of the "Request for Comments" (RFC) document series."). [primary]

<a id="ref-35"></a>[35] Richard Larson and Elizabeth Larson. "[Top Five Causes of Scope Creep... and What to Do About Them](https://www.pmi.org/learning/library/top-five-causes-scope-creep-6675)." PMI Global Congress 2009, North America (accessed 2026-09-25, read from an Internet Archive snapshot). Scope creep defined by authorization, not size ("The key part is whether changes are authorized or not. If an expansion of scope is approved, then it is not scope creep."). [practitioner]

<a id="ref-36"></a>[36] Sophie Danby (InvGate), quoting Kevin Holland and Barclay Rae. "[Change Advisory Board Best Practices: 15+ Industry Leaders Weigh In](https://blog.invgate.com/do-we-still-need-the-change-advisory-board)." InvGate blog, 2022 (accessed 2026-09-25). The board-as-bottleneck claim, sourced only for ITSM change advisory boards ("CABs belong in history as an example of how ITSM put a straightjacket around agility and innovation."). [practitioner]

<a id="ref-37"></a>[37] Valerio Pianella. "[PM Tales #29: The Decisions We Didn't Make](https://www.valeriopianella.it/pm-tales/pm-tales-29-the-decisions-we-didnt-make/)." Personal blog, 2026 (accessed 2026-09-25). Change requests named among the things whose postponement goes untracked, "decision debt" ("Budget. Milestones. Risks. Issues. Deliverables. Dependencies. Change requests.... there is one thing we often track poorly: the cost of decisions not made."). [practitioner]

<a id="ref-38"></a>[38] Float. "[How to Manage a Change Request Without Derailing Projects](https://www.float.com/resources/manage-change-request)." Float resource, 2024 (accessed 2026-09-25). A second, weaker corroboration of the same failure mode Pianella names, a request left undecided eroding confidence ("Being clear and timely about decisions regarding change requests will build confidence across the team that things are being worked out and managed well."). [vendor]

<a id="ref-39"></a>[39] PM Majik. "[Impact assessment of project change requests](https://www.pmmajik.com/impact-assessment-of-project-change-requests/)." (accessed 2026-09-25). Impact of not making the change as its own field, a change deadline field, and an explicit caution against overstating impact ("Impact of not making change"; "you should include the deadline by when a decision is required on the change request"; "do not over state the impact in an attempt to gain approval"). [practitioner]

<a id="ref-40"></a>[40] kiolo. "[Project Change Request Template: Scope, Impact and Approval](https://kiolo.com/en/blog/project-change-request-template/)." Product blog (accessed 2026-09-25). The richest single source for gap elements: the no-change option, out-of-scope boundaries, conditions with an owner and deadline, and multiple authorities recorded separately ("Include the no-change option plus realistic alternatives."; "Approval with conditions must identify the owner and deadline for each condition"; "do not collapse them into an overall green status before every mandatory approval is satisfied"). [vendor]

<a id="ref-41"></a>[41] Onplana. "[What a Change Control Board Should Actually Do](https://onplana.com/blog/change-control-board-that-works)." PM software vendor blog (accessed 2026-09-25). A three-artifact submission standard and the deadline-deferral link ("Every change request submitted to a CCB needs exactly three artifacts.... Artifact 3: Decision deadline."; "A change request without a deadline gives the board permission to defer indefinitely."). [vendor]

<a id="ref-42"></a>[42] Wikipedia contributors. "[Change management (engineering)](https://en.wikipedia.org/wiki/Change_management_(engineering))." (accessed 2026-09-25). A change request document defined by why it matters and a go/no-go decision, and an industrial-disaster consequence of an undocumented change ("Document that describes the requested change and why it is important"; "The change had not been properly thought out, documented and risk-assessed, so that the event of breach of containment had not been identified."). [reference]

<a id="ref-43"></a>[43] StakeholderMap.com. "[Change Request Template](https://www.stakeholdermap.com/project-templates/change-request-template.html)." (accessed 2026-09-25). A widely distributed free template naming options considered and per-option impact ("Options considered to implement the change"; "Impact of each option (Cost, Scope, Schedule, Quality)"). [practitioner]

<a id="ref-44"></a>[44] PM Study Circle (Fahad Usmani). "[Understanding Change Request: How to Manage Scope Changes](https://pmstudycircle.com/change-request/)." (accessed 2026-09-25). The naive baseline: requestor and date, description, reason, impact analysis, proposed resolution, and approval, with no options field ("Your request should include: Requestor and date.... Description of the change.... Reason for the change.... Impact analysis.... Proposed resolution.... Approval section."). [practitioner]

<a id="ref-45"></a>[45] Tallyfy (Amit Kothari). "[How to manage change requests without the chaos](https://tallyfy.com/change-request/)." (accessed 2026-09-25). A second naive-baseline five-step process naming no options field, out-of-scope statement, or deadline ("The three questions that matter for any change request: What's the change? What's the benefit? How important is it relative to everything else?"). [vendor]

<a id="ref-46"></a>[46] DeeProjectManager (Tuyota Manuwa). "[Understanding the Role of a Change Control Board in Project Management](https://deeprojectmanager.com/change-control-board/)." (accessed 2026-09-25). Documented rationale and an audit trail named as CCB best practices, and their absence as a named failure mode ("Document all CCB Decisions: To maintain visibility, all CCB change decisions must be properly documented with context and rationale."; "Poor Tracking and Documentation: Without proper record-keeping, decisions can get lost leading to misalignment."). [practitioner]

<a id="ref-48"></a>[48] Prairie View A&M University. "[Information Technology Services Change Management Request Form](https://www.pvamu.edu/its/wp-content/uploads/sites/46/change-management-request-form_fill.pdf)." 2010, modified 2013 (accessed 2026-09-25). A university IT change form in the neighbor lineage, carrying a rollback description and a change control committee sign-off ("Rollback Description"; "Change Control Committee Sign off"). [primary]
