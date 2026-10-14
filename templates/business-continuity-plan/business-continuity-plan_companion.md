# Companion: The Business Continuity Plan

> The deep explainer for the business-continuity-plan bundle. Read this to understand what the type is,
> how its sources describe it, and where they disagree about its shape. The short operator card is
> [`business-continuity-plan_guide.md`](business-continuity-plan_guide.md); a fully worked instance is
> [`business-continuity-plan_example.md`](business-continuity-plan_example.md). Inline citations like
> [[1]](#ref-1) resolve to the [References](#references) at the bottom, tagged by source reliability. This
> bundle sits in the `standing-standards` family alongside `definition-of-done`, `definition-of-ready`,
> `launch-coordination-checklist`, `production-readiness-review` and `runbook`, as a **tool**: a plan a team executes
> under time pressure once a disruption is declared or a drill begins, not a standard the team is judged
> against on a cadence, per
> [ADR 0071 (business-continuity-plan joins standing-standards as a tool)](../../docs/internal/decisions/0071-business-continuity-plan-joins-standing-standards-as-a-tool.md).

---

## 1. Orientation

A business continuity plan documents how an organization keeps its critical business processes going
through a significant disruption and recovers them afterward. NIST states the core definition this bundle
builds from: "The documentation of a predetermined set of instructions or procedures that describe how an
organization's mission/business processes will be sustained during and after a significant disruption"
[[1]](#ref-1). The CSRC glossary carries no second, competing definition the way it does
for disaster recovery [[3]](#ref-3). FEMA's Ready Business program ships the plan as a fill-in PDF template
with named sections and tables [[4]](#ref-4). Disaster recovery is narrower: it recovers the information
systems those processes use, and NIST scopes it to "an alternate facility" in response to "a major hardware
or software failure or destruction of facilities" [[1]](#ref-1).

The two halves of this bundle's catalog name admit at different strengths, and the companion does not round
the weaker one up. **The business continuity plan admits on a literal fill-in template**: FEMA ships one
[[4]](#ref-4) and NIST defines the type independently [[1]](#ref-1)[[3]](#ref-3). **The disaster recovery
plan admits on a definition only**: NIST defines it [[1]](#ref-1), and the CSRC glossary carries a second,
conflicting federal definition [[2]](#ref-2), but no source read for this bundle ships a fill-in template
titled as a standalone disaster recovery plan. California's SIMM 5325-A is the one template-grade structure
for recovering technology, and it is titled a Technology Recovery Plan, not a disaster recovery plan
[[6]](#ref-6).

The sources agree that disaster recovery serves business continuity and disagree on whether it is a section
inside the plan or a separate plan beneath it (section 6 below). This bundle makes it a section in the full
variant and a pointer in the lean variant, which is the shape California and SANS state and NIST and
Ready.gov permit, not a shape any one source requires [[1]](#ref-1)[[4]](#ref-4)[[6]](#ref-6)[[16]](#ref-16).
The Business Impact Analysis is upstream of both: NIST templates it as a separate artifact whose results
"should be appropriately incorporated into the analysis and strategy development efforts for the
organization's COOP, BCPs, and DRP" [[1]](#ref-1), and California requires that the recovery plan "must be
derived from" it [[7]](#ref-7). This plan carries the analysis's results in a summary table; it is not the
analysis itself.

**At a glance**
- The plan admits on FEMA's named fill-in template [[4]](#ref-4); disaster recovery admits on a definition
  only, and no source ships it as a standalone fill-in template [[1]](#ref-1)[[2]](#ref-2).
- Two federal sources define disaster recovery differently on the one fact that most distinguishes the
  type, where it recovers to: NIST says an alternate facility [[1]](#ref-1); the CNSSI 4009-2022 glossary
  entry says "at its original facilities" [[2]](#ref-2).
- Whether review and testing run on a calendar or on events is unsettled across the sources this bundle
  read; most sources that state a number say annual, and NIST's own narrative is looser [[1]](#ref-1)[[6]](#ref-6)
  [[9]](#ref-9)[[13]](#ref-13)[[16]](#ref-16).
- Who authors, activates and executes the plan is answered differently by the sources this companion
  draws on for the question, and this research does not settle it (section 6, item 4 below)
  [[1]](#ref-1)[[6]](#ref-6)[[9]](#ref-9)[[13]](#ref-13).
- The professional bodies treat the written plan as one output of a standing management programme, not as
  sufficient on its own: this bundle templates the plan, not the programme [[14]](#ref-14)[[15]](#ref-15)
  [[18]](#ref-18)[[19]](#ref-19).

If you read nothing else: this is a template-grade artifact for the business continuity half and a
definition-grade one for the disaster recovery half, and the companion names that asymmetry rather than
hiding it.

## 2. Origins and evolution

No source read for this bundle supplies a founding story for the business continuity plan: no named
originator, no founding decade, no first-use citation. What the research can support is a set of dated
events in the vocabulary and the structure, each tied to the source that states it, and nothing beyond what
those sources say.

**The federal definitional baseline is NIST Special Publication 800-34 Revision 1, May 2010** [[1]](#ref-1),
which defines the business continuity plan, the disaster recovery plan, the contingency plan, the continuity
of operations plan, and the Business Impact Analysis in one document, and whose glossary entries the CSRC
site mirrors without amendment for the business continuity plan [[3]](#ref-3) while carrying a second,
conflicting entry for the disaster recovery plan under CNSSI 4009-2022 [[2]](#ref-2).

**California's state policy renamed its own document type in September 2013.** A 2013 change summary states:
"Deleted SIMM Section 65A Disaster Recovery Documentation for Agencies Preparation Instructions and replaced
it with SIMM Section 5325A Technology Recovery Plan Instructions" [[8]](#ref-8), alongside a parallel
renumbering of the certification document from 70B to 5325B. The March 2023 edition of that instruction
document is read here [[6]](#ref-6), governed by the October 2025 revision of its parent policy section
[[7]](#ref-7).

**FEMA's Continuity Guidance Circular 1 is dated July 2013** [[29]](#ref-29), read on a legislature mirror
whose path is marked inactive; this research could not confirm whether either of two later FEMA-titled
circulars found in a 2026 web search supersedes it, so it is cited here only as the 2013 circular, never as
current FEMA guidance.

**The FFIEC's Business Continuity Management booklet has been revised at least once since 2015, and the 2003
edition this bundle read is at least two editions behind it.**
A Federal Reserve transmittal letter states that the FFIEC "has revised the February 2015 version" of the
booklet in December 2019 [[10]](#ref-10), and an archived FDIC letter states: "The booklet replaces the
Business Continuity Planning booklet issued in February 2015" [[11]](#ref-11), while also naming the shift in
the booklet's own name: "The change from business continuity planning to business continuity management
reflects the expanded role information technology (IT) plays in supporting business operations and meeting
customer expectations" [[11]](#ref-11). The March 2003 edition read directly for this bundle [[9]](#ref-9) is
therefore at least two editions old, and this research could not retrieve the current 2019 booklet itself to
confirm whether it keeps a fixed review interval.

**The professional bodies' own vocabulary moved in the other direction, from a lifecycle to a system.** The
BCI's Good Practice Guidelines 7.0, published 12 October 2023, states that "the previously termed 'Business
Continuity Management Lifecycle' has been replaced by the more scalable and holistic term 'Business
Continuity Management System'" [[14]](#ref-14). DRII's own 2023 revision renamed four of its ten Professional
Practices in the same period, including Practice 1 from "Program Initiation and Management" to "Program
Management" and Practice 8 to add "/Test" to its title "for consistency" [[15]](#ref-15).

**SANS published two differently scoped templates a decade apart, and neither states that it replaces the
other.** The 2014 "Disaster Recovery Plan Policy" names seven required contingency plans and a testing cadence
[[16]](#ref-16); the organization's current "Resilience Management Policy", last updated February 2026, frames
business continuity and disaster recovery together as one safeguard inside a broader resilience and incident
management policy, and specifies far less about plan content than the 2014 document [[17]](#ref-17). Whether
the newer policy replaces the older one is stated by neither source, and this companion does not resolve it.

None of these events describes a single lineage. They are five separate institutions revising five separate
documents on five separate schedules, and the only claim this research supports about the type's history is
that the vocabulary and the published structures have kept moving, source by source, across the period this
research can see.

## 3. Anatomy (section by section)

The full variant carries nine sections; the lean variant carries eight of them, unchanged in name and order,
so lean is a strict ordered subset of full: Purpose and Scope, Business Continuity Team and Roles, Business
Impact Analysis Summary, Continuity Strategies and Manual Workarounds, Activation and Incident Management,
Training, Testing and Exercising, Plan Administration, and Review Trigger. Full inserts Disaster Recovery
before Review Trigger.

### Purpose and Scope (lean and full)

The business covered, what counts as a disruption in this plan, and where the disaster recovery plan lives
if it is kept as a separate document.

FEMA's template lists "Information Technology Disaster Recovery Plan (if not included in the business
continuity plan)" among the related plans a complete program keeps [[4]](#ref-4), which is the source for the
lean variant's pointer: where no Disaster Recovery section is filled in, this is where a reader is told a
separate plan exists and where to find it. NIST's own plan-type distinctions, between a plan that sustains
mission and business processes and one that recovers information systems at an alternate facility, belong
here as the scope statement that keeps the two halves of this bundle's name from being read as
interchangeable [[1]](#ref-1).

Beginner note: name the business or unit this plan covers, state in plain language what a "significant
disruption" means for that scope, and if a separate disaster recovery plan exists, name it and say where it
is kept. Expert note: this section is also where contested item 1 below becomes a concrete choice for your
plan, not an abstract one; decide now whether disaster recovery gets its own section or a pointer, and let
that decision drive which variant you actually fill in.

### Business Continuity Team and Roles (lean and full)

The team roster, roles stated by job title, the person with authority to activate the plan and a named
successor, and any delegation that takes effect when normal channels of direction are disrupted.

FEMA's template carries a "Business Continuity Organization" section naming the team [[4]](#ref-4).
California's instructions ask that "job titles (rather than the names of individuals) should be used to
assign responsibility as it lessens maintenance on procedures as personnel changes" [[6]](#ref-6). NIST
requires that activation authority rest with one person: "Only one individual should have this authority,
and a successor should be clearly identified to assume that responsibility if necessary" [[1]](#ref-1).
FEMA's continuity circular adds the delegation mechanism by which that authority still functions if the
named person is unreachable: "predetermined delegations of authority will take effect when normal channels
of direction are disrupted and will terminate when these channels are reestablished" [[29]](#ref-29), and
asks that delegates also be named "by position title and not by name" [[29]](#ref-29).

Beginner note: list every role this plan depends on by job title, name who currently holds each one, name one
person with authority to activate the plan, and name that person's successor. Expert note: write the
delegation clause even if you expect never to need it; FEMA's own continuity guidance treats it as a standing
requirement, not a contingency for the unusually disorganized [[29]](#ref-29).

### Business Impact Analysis Summary (lean and full, a table section)

Each critical process with its Recovery Time Objective and Recovery Point Objective, drawn from a separate
Business Impact Analysis, and the systems and suppliers it depends on.

NIST frames the analysis itself as upstream and prior: "The BIA is the first source for determining
resiliency and contingency planning strategies" [[1]](#ref-1), and its results "should be appropriately
incorporated into" the plans that follow [[1]](#ref-1). FEMA's template field reads "Insert results of
Business Impact Analysis" [[4]](#ref-4), and California requires that the technology recovery plan "must be derived from the state
agency or entity's BIA" [[7]](#ref-7). The two objectives this table carries are defined consistently across
every vendor source this research read: a Recovery Time Objective is "the maximum acceptable delay between
the interruption of service and restoration of service" [[22]](#ref-22), and a Recovery Point Objective is
"the maximum acceptable time after the last data recovery point" [[22]](#ref-22). Suppliers belong in this
table as named dependencies rather than only as contacts, following a supplier contract's own requirement
that "Supplier shall ensure all Subcontractors have Business Continuity Programs and Disaster Recovery Plans
sufficient to meet delivery of the Services during a Disruptive Event" [[32]](#ref-32).

Beginner note: for each critical process, state its Recovery Time Objective and Recovery Point Objective in
plain units of time, and name the systems and suppliers it cannot run without. Expert note: this table carries
the analysis's results, never the worksheet; if you are deriving RTOs and RPOs for the first time, that work
happens in a separate Business Impact Analysis, not in this table.

### Continuity Strategies and Manual Workarounds (lean and full)

How each critical process keeps running without the systems it normally depends on, and at what recovery
level, chosen against cost.

FEMA's template names this as its own section, "Manual Workarounds" [[4]](#ref-4). The cost tradeoff that
governs how far to invest in a workaround is stated most explicitly by AWS's own four recovery strategies,
ordered "in increasing order of cost and complexity, and decreasing order of RTO and RPO" [[23]](#ref-23),
with an explicit warning against over-investing: "You should avoid implementing a strategy that is more
stringent than it needs to be, as this incurs unnecessary costs" [[23]](#ref-23). Google states the same
tradeoff for the process as a whole: "Typically, the smaller your RTO and RPO values are... the more your
application will cost to run" [[24]](#ref-24).

Beginner note: for each critical process, write down what staff actually do by hand when the normal system is
unavailable, not just that a workaround "exists." Expert note: the cost-versus-recovery-speed tradeoff in
section 6's recovery-objective sources applies here even though those sources were written about technology
recovery; a workaround that is faster than the process needs is also a workaround that costs more than it
needs to.

### Activation and Incident Management (lean and full)

Stated activation criteria, who declares an activation, who is told and in what order, and the condition for
standing the plan down.

NIST requires that activation criteria be stated in advance: "The designated authority... has the authority
to activate the contingency plan" [[1]](#ref-1), triggered when "one or more of the activation criteria for
that system are met" [[1]](#ref-1). California asks the plan to identify "individual(s) responsible for
making the TRP activation decision" [[6]](#ref-6). HMPPS's framework separates who activates from who writes
the plan: "A member of the nominated Business Continuity team will normally activate and stand down the
plans" [[13]](#ref-13). Notice obligations extend past the organization's own staff where regulation requires it:
FINRA's rule binds its member firms to "disclose to its customers how its business continuity plan addresses
the possibility of a future significant business disruption" [[30]](#ref-30), and the federal continuity
circular requires systems that "support full connectivity, under all conditions, among key leadership,
internal elements, other organizations, critical customers, and the public" [[29]](#ref-29). Deactivation is
its own named step, not an afterthought: NIST's reconstitution phase "consists of two major activities:
validating successful reconstitution and deactivation of the plan" [[1]](#ref-1).

Beginner note: write the specific conditions that trigger an activation, name who declares one, write the
notification order including anyone outside the organization you owe notice to, and name the condition under
which the plan stands down. Expert note: a regulatory or customer notification duty does not apply to every
organization; FINRA's duty binds its own member firms specifically [[30]](#ref-30), so fold it in only where
your own organization owes that notice, following this bundle's own decision not to split communications into
a separate section (section 6's gap-question routing, declined).

### Training, Testing and Exercising (lean and full, a table section)

The exercise schedule and type, what each one validates, who observes, and each finding as an owned, dated
corrective action.

The 2003 FFIEC booklet names four test types, from lightest to heaviest: "Orientation/Walk-through,"
"Tabletop/Mini-drill," "Functional Testing," and "Full-scale Testing" [[9]](#ref-9), a taxonomy NIST's own
exercise types echo under different names, including a tabletop exercise that "is discussion-based only and
does not involve deploying equipment or other resources" [[1]](#ref-1). The same FFIEC booklet names a
specific insufficient test: "Unmanned recovery testing, where back-up tapes are sent to the recovery site to
be run by service provider employees, is not a sufficient test of an institution's BCP" [[9]](#ref-9), and asks
that "the audit department or other independent party should directly observe tests of the BCP" [[9]](#ref-9).
A test is judged against named criteria, not against a bare pass or fail: Google Cloud names three, "data
integrity, recovery time objective (RTO), and recovery point objective (RPO)" [[25]](#ref-25). Microsoft adds
the reminder that a test must exercise the people, not only the systems: "Include all of the human processes
in your drills, and don't just focus on the technical processes" [[26]](#ref-26). Findings become tracked,
owned work rather than a filed report: the federal continuity circular names a standing "Corrective Action
Program (CAP)," where "Deficiencies, actions to correct them, and a timeline for remedy are documented"
[[29]](#ref-29), and HMPPS requires that "Debrief sessions must be held following an exercise and lessons
learnt log completed" [[13]](#ref-13).

Beginner note: schedule a named exercise type, state what it is meant to validate, name who observes it, and
turn every finding into a dated, owned action rather than a note in a report nobody revisits. Expert note: the
library keeps both words, "testing" and "exercising," in this section's own title, because URM argues directly
that "these activities are an exercise, not a test" [[19]](#ref-19), since an exercise carries no pass/fail
judgement; this bundle does not adjudicate that argument (section 6, item 6 below).

### Plan Administration (lean and full)

Vendors and contractors, revision history, and where copies of the plan are kept so it can be reached when
the systems it protects are down.

FEMA's template names this cluster of sections directly: "Vendors & Contractors," "Revision History," and
"Plan Distribution & Access" [[4]](#ref-4), with its own distribution rule stated plainly: "A master copy of
the document should be maintained by the business continuity team leader" [[4]](#ref-4). The reason a plan
needs an offline, reachable copy is sourced to the same kind of event the plan exists to survive: a federal
ransomware response guide asks that organizations "Ensure a hard copy of the plan and an offline version is
available" [[31]](#ref-31), and the continuity circular asks organizations to "strongly consider multiple
redundant media for storing their essential records" [[29]](#ref-29). FINRA ties this section to an update
trigger, not only a storage rule: "Each member must update its plan in the event of any material change to the
member's operations, structure, business or location" [[30]](#ref-30).

Beginner note: list every vendor and contractor this plan depends on, keep a dated revision history, and
state where a copy of the plan is kept that does not depend on the systems the plan protects. Expert note: a
plan that lives only on the network it describes fails exactly when it is needed; this is a precaution this
research found stated directly, not a failure this research found measured (section 7 below).

### Disaster Recovery (full only)

The recovery strategy for each critical system; backup and offsite storage, including offline copies;
recovery procedures written so another trained person can follow them; the order of recovery across
dependent systems; verifying restored data before service resumes; and the recovery test.

This section collapses California's fourteen numbered SIMM 5325-A sections into fewer headings
[[6]](#ref-6); that grouping is this library's own choice, not SIMM's, made because the fourteen numbered
sections were written for a state filing, not for a template section list. The recovery strategy choice is
the same AWS cost-versus-speed tradeoff named in Continuity Strategies above, applied to technology
specifically [[23]](#ref-23). Backup and offsite storage carries an explicit caution about one popular
technique: a joint government ransomware guide requires offline backups because "many ransomware variants
attempt to find and subsequently delete or encrypt accessible backups" [[31]](#ref-31), and separately states: "Use
immutable storage with caution as it does not meet compliance criteria for certain regulations and
misconfiguration can impose significant cost" [[31]](#ref-31). Recovery procedures carry an explicit
authorship standard in two sources: NIST asks that
they be "written at a level that an appropriately skilled technician can recover the system without
intimate system knowledge" [[1]](#ref-1), and California asks for procedures "detailed enough so that
another trained information technology professional would be able to recover the state entity's
infrastructure should those with primary responsibility be unavailable" [[6]](#ref-6). The order of recovery
across dependent systems is sourced to a practitioner's direct account of what breaks without it: "After an
outage, you can end up with a deadlock: two systems that each can't start until the other is running and
providing some functionality" [[28]](#ref-28), paired with AWS's own dependency-mapping questions, "What are
the recovery objectives and availability expectations of workloads that this one depends on (downstream)?"
[[22]](#ref-22). Verifying restored data before service resumes is Google Cloud's own stated goal of a
restore test: "To ensure your backups can be restored efficiently and that the restored data meets
application requirements, regularly simulate data recovery scenarios" [[25]](#ref-25), echoed in NIST's own
reconstitution phase, which includes "validating successful reconstitution" [[1]](#ref-1). The recovery test
itself is California's own named requirement, covering "tabletop exercises, data recovery testing, forced
testing... and/or full plan testing" [[6]](#ref-6), judged by the same three criteria named above
[[25]](#ref-25).

Beginner note: for each critical system, name its recovery strategy, where its backups live including at
least one offline copy, the order it must be recovered in relative to the systems it depends on, and how you
will confirm the restored data is actually usable before declaring the system back in service. Expert note:
having backups is not the same claim as having a recovery, and this section exists to make that distinction
unavoidable; a practitioner states the gap directly: "If you have backups, but you haven't tested restoring
them, you don't really have backups" [[28]](#ref-28).

### Review Trigger (lean and full, contract-mandated)

A named owner and conditions: a change in people, suppliers, systems, facilities or the business; a change
to the Business Impact Analysis; an activation; and an exercise or test finding.

No structural source read for this bundle publishes a section with this name or job; it is required
directly by the `standing-standards` family contract rather than volunteered by any source, and this bundle
labels it as its own contribution the way its sibling bundles in the same family label theirs
([`standing-standards.md`](../../docs/internal/contracts/standing-standards.md)). The conditions it names are
drawn from sources that state a trigger without naming this section: NIST's narrative sets the general rule,
"the plan should be reviewed for accuracy and completeness at an organization-defined frequency or whenever
significant changes occur to any element of the plan" [[1]](#ref-1), adding that "Certain elements, such as
contact lists, will require more frequent reviews" [[1]](#ref-1). The 2003 FFIEC booklet ties a review to the testing plan
whenever there is "any changes to key personnel, policies, procedures, facilities, equipment, outsourcing
relationships, vendors, or other components that impact a critical business function" [[9]](#ref-9). HMPPS
ties a review to the same two events this section names, "annually or following an incident or exercise"
[[13]](#ref-13). Where a regulator or policy requires an annual exercise, it appears here as a floor under
these conditions, not as the trigger itself; see contested item 3 below.

Beginner note: name a single owner for this section, and write the specific events that would make you revise
this plan rather than a calendar date alone. Expert note: an annual exercise requirement from a regulator or
an internal policy belongs here as a stated minimum frequency, layered under the condition-based trigger, not
as a substitute for it.

## 4. Variants and sizing

**Lean (eight sections)** is Purpose and Scope, Business Continuity Team and Roles, Business Impact Analysis
Summary, Continuity Strategies and Manual Workarounds, Activation and Incident Management, Training, Testing
and Exercising, Plan Administration, and Review Trigger. Where a separate disaster recovery plan already
exists, Purpose and Scope points to it, following the shape FEMA's own template allows: "Information
Technology Disaster Recovery Plan (if not included in the business continuity plan)" [[4]](#ref-4).

**Full (nine sections)** adds Disaster Recovery before Review Trigger, carrying the recovery strategy,
backup and offsite storage, recovery procedures, recovery order, restore verification and the recovery test
when no separate disaster recovery plan exists to hold them. This research found no source that states a
sizing signal more specific than that choice itself; the signal this bundle uses, whether a separate
disaster recovery plan already exists, is the one FEMA's template names directly rather than one this
research measured independently.

## 5. Methodology lineage

**No source read for this bundle comes from Scrum, SAFe, Shape Up, Lean, design thinking, or Amazon's own
internal mechanisms.** That is a statement about what this research set contains, not a claim that those
schools have nothing to say about continuity; it was not found in the sources this bundle's research fan-out
retrieved.

**A federal contingency-planning lineage** is the bundle's definitional spine: NIST Special Publication
800-34 Revision 1 defines every plan type this bundle names [[1]](#ref-1), its glossary entries for both the
business continuity plan [[3]](#ref-3) and, under a conflicting second definition, the disaster recovery plan
[[2]](#ref-2).

**An emergency-management lineage** supplies the published fill-in template this bundle's business
continuity half admits on: FEMA's Ready Business program [[4]](#ref-4)[[5]](#ref-5), and a separate federal
continuity-of-operations standard that names delegation, succession, reconstitution and essential-records
requirements this bundle's gap research drew on directly [[29]](#ref-29).

**A financial-regulator lineage** supplies the testing-cadence and audit-oversight language this bundle
draws on most heavily: the 2003 FFIEC booklet [[9]](#ref-9), the 2019 booklet's existence confirmed by a
transmittal letter and a regulator's summary without the booklet's own text [[10]](#ref-10)[[11]](#ref-11),
and FINRA's enforced rule requiring customer disclosure and an annual review [[30]](#ref-30).

**A state-government IT-policy lineage** supplies the one template-grade structure for recovering technology
this research found: California's SIMM 5325-A instructions [[6]](#ref-6), its governing policy clause
[[7]](#ref-7), and the 2013 renaming event that shows the document's own lineage shifting from "disaster
recovery" to "technology recovery" in its own title [[8]](#ref-8).

**A UK government lineage** supplies a second national government's plan structure, explicitly tied to ISO
22301 by policy rather than by this research reading the standard directly: "This policy framework sets out
the arrangements necessary to ensure Business Continuity Management (BCM) is performed in accordance with
ISO 22301 as required by Cabinet Office" [[12]](#ref-12), with its own annex list in the framework itself
[[13]](#ref-13).

**A professional-body lineage** treats the plan as one output of a standing management programme rather than
as sufficient on its own: the BCI's Good Practice Guidelines [[14]](#ref-14), DRII's Professional Practices
[[15]](#ref-15), and ISO's own catalogue-page framing of "a documented management system" [[18]](#ref-18),
read only from its free catalogue page since the standard itself is paywalled. A practitioner commentary argues
the same point from the exercising side: "having a BCP on paper is not enough" [[19]](#ref-19).

**A security-policy-template lineage** supplies two differently scoped templates from the same organization a
decade apart, neither stating that it supersedes the other: SANS's 2014 Disaster Recovery Plan Policy
[[16]](#ref-16) and its current Resilience Management Policy [[17]](#ref-17).

**A cloud-vendor lineage** supplies the recovery-objective definitions and recovery-strategy taxonomy this
bundle's Disaster Recovery section draws on: AWS [[20]](#ref-20)[[21]](#ref-21)[[22]](#ref-22)[[23]](#ref-23),
Google Cloud [[24]](#ref-24)[[25]](#ref-25), and Microsoft [[26]](#ref-26).

**A site-reliability-engineering lineage** supplies a direct practitioner account of why untested backups and
unmanaged dependencies cause recovery to fail [[28]](#ref-28), and a narrower, single-passage contribution on
designing recovery tools to run offline and checkpointable [[27]](#ref-27).

**A supplier-contract lineage** supplies the one source in this research that makes a supplier's own
subcontractors' continuity an explicit, auditable obligation rather than an assumption [[32]](#ref-32).

## 6. Debates and contested boundaries

**1. Is disaster recovery a section inside the plan, or a separate plan beneath it?** The sources agree on
the direction, that disaster recovery serves business continuity, and disagree on the shape. NIST models the
disaster recovery plan as its own plan type, never as a section of one: "A DRP may support a BCP or COOP
plan" [[1]](#ref-1). FEMA's template lists a disaster recovery plan among related plans, "Information
Technology Disaster Recovery Plan (if not included in the business continuity plan)" [[4]](#ref-4), which
permits either shape. California makes the technology recovery
plan "a sub-set" of the continuity plan [[7]](#ref-7) and "just one portion" of business continuity
[[6]](#ref-6). SANS says the disaster recovery plan "is often part of" the business continuity plan
[[16]](#ref-16), and Google calls disaster recovery "a subset of business continuity planning" [[24]](#ref-24).
No source puts the two as equals, and no source requires disaster recovery to be a section rather than a
separate supporting plan. This bundle's shape, a Disaster Recovery section in full and a pointer in lean, is
the choice California and SANS state and NIST and Ready.gov permit, not a shape any one source requires.

**2. Where does a disaster recovery plan recover to?** NIST scopes it to "an alternate facility" and says it
"only addresses information system disruptions that require relocation" [[1]](#ref-1). The CSRC glossary's
CNSSI 4009-2022 definition scopes it to recovering "at its original facilities" over "hours or days"
[[2]](#ref-2). Two federal definitions disagree on the fact that most distinguishes the type, and this
companion does not resolve which is correct.

**3. Is the plan reviewed and tested on a calendar or on events?** Most sources that state a cadence state an
annual one: the 2003 FFIEC booklet in several places [[9]](#ref-9), HMPPS [[13]](#ref-13), SANS's 2014 policy
[[16]](#ref-16), SIMM 5325-A's annual test [[6]](#ref-6), and NIST's sample attestation that a plan "will be
tested at least annually" [[1]](#ref-1). NIST's own narrative is looser: review "at an organization-defined
frequency or whenever significant changes occur to any element of the plan" [[1]](#ref-1). The cloud vendors
and a practitioner commentary say to test regularly and give no number [[24]](#ref-24)[[26]](#ref-26)
[[28]](#ref-28). Whether the current FFIEC booklet keeps a fixed interval is unsettled, since this research
could not retrieve the booklet itself [[11]](#ref-11). This bundle handles the tension the way
[ADR 0071](../../docs/internal/decisions/0071-business-continuity-plan-joins-standing-standards-as-a-tool.md)
records it: the Review Trigger section states conditions, and an annual exercise appears as a floor that a
regulator or policy may impose, not as the trigger itself.

**4. Who writes the plan, who activates it, and who carries it out?** The sources this companion draws on
for the question return different readings, and this research does not settle it. NIST separates activation from
authorship: "The designated authority (typically a senior manager or CIO)" activates, while "The ISCP
Coordinator also typically manages development and execution of the contingency plan" [[1]](#ref-1), which
also cuts the other way for execution, giving it back to the author. HMPPS separates activation from
documentation differently: "A member of the nominated Business Continuity team will normally activate and
stand down the plans" [[13]](#ref-13), while Local Business Continuity leads "Complete the Business Continuity
documentation" [[13]](#ref-13). The 2003 FFIEC booklet names the role without assigning it, asking that a plan
define "decision-making authorities for designated teams and/or staff members, including those who have
authority to declare a disaster" [[9]](#ref-9). Two sources state a design requirement rather than a practice: NIST and California both ask
that recovery procedures be written so a stranger, not only the author, could follow them
[[1]](#ref-1)[[6]](#ref-6). No source found in this research says the plan's author usually runs it alone, and
none says they usually do not. This research does not amend ADR 0071's open question; it reports the finding.

**5. Is the written plan sufficient, or only one output of a standing programme?** The professional bodies
treat the plan as one output of a management programme: the BCI places "plans" inside an "operational cycle"
that "sits within a bigger 'management cycle'" [[14]](#ref-14), DRII lists "Plan Development and
Implementation" as one of ten practices [[15]](#ref-15), and ISO describes "a documented management system"
[[18]](#ref-18). A practitioner argues the same point directly: "having a BCP on paper is not enough"
[[19]](#ref-19). No source found in this research defends a plan without exercising and maintenance as
sufficient, so this is consensus with a historical contrast rather than two live camps. This bundle templates
the plan, not the programme, and names that scope limit here rather than implying the template is the whole
job.

**6. "Test" or "exercise"?** The 2003 FFIEC booklet names four test types [[9]](#ref-9), and NIST lists
testing methods and exercise types side by side [[1]](#ref-1). A practitioner commentary insists that "these
activities are an exercise, not a test" [[19]](#ref-19), because an exercise carries no pass or fail judgement.
This bundle keeps both words, in the section title "Training, Testing and Exercising," and does not adjudicate
between them.

**7. Is immutable backup storage settled practice?** Vendors promote immutable storage for ransomware
recovery, but a joint government guide requires offline backups specifically and states: "Use immutable
storage with caution" [[31]](#ref-31). Nothing in this research supports presenting immutability as settled
practice, and this bundle does not.

**8. Does SANS's current policy replace its 2014 one?** The 2014 policy's own scope statement says it "does
not provide requirement around what goes into the plan or subplans" [[16]](#ref-16), and its next section
then requires seven named contingency plans, a tension inside the single 2014 document [[16]](#ref-16).
Whether the 2026
Resilience Management Policy [[17]](#ref-17) replaces the 2014 one is stated by neither document, and this
research does not assume it does.

**9. Several sources read here are time-bound, and the companion names each limit rather than letting it
pass silently.** The 2003 FFIEC booklet is at least two editions old [[9]](#ref-9). FEMA's Continuity Guidance
Circular 1 is dated 2013, and its current status is unsettled [[29]](#ref-29). SANS's 2014 policy's canonical
page is gone, and the entry here cites a SANS-hosted mirror copy [[16]](#ref-16). California's SIMM 5325-A is
its March 2023 edition, and SAM 5325.1 is its October 2025 revision [[6]](#ref-6)[[7]](#ref-7).

## 7. Anti-patterns and failure modes

This section states only what a logged source describes as a way the plan fails, with its own source attached.
No frequency claim is made for any of them; no source in this research measured how often any of them
happens.

**Neglect, because disasters are rare.** "Since disasters happen so rarely, management often ignores the
disaster recovery planning process" [[16]](#ref-16).

**Disaster recovery bolted on late.** "I think a lot of DR is an afterthought" [[28]](#ref-28).

**Backups nobody has restored.** "If you have backups, but you haven't tested restoring them, you don't
really have backups" [[28]](#ref-28). A second source states the same gap from the other direction: "It isn't
enough just to have a plan for backing up or archiving your data" [[24]](#ref-24).

**The rarely used path breaks first.** "Parts of the system that are only used in disasters need the most
testing, or they'll fail you when you need them" [[28]](#ref-28).

**A test that does not exercise the people who will recover.** The 2003 FFIEC booklet names an insufficient
test where "back-up tapes are sent to the recovery site to be run by service provider employees"
[[9]](#ref-9); Microsoft's own instruction guards against the same gap directly: "Include all of the human
processes in your drills" [[26]](#ref-26).

**Dependency deadlock during recovery.** "After an outage, you can end up with a deadlock: two systems that
each can't start until the other is running and providing some functionality" [[28]](#ref-28).

**Stale contacts and documentation.** NIST names contact lists as an element needing more frequent review
than the rest of the plan [[1]](#ref-1); a practitioner account states the same failure as something recovery
exercises reveal directly: exercises find "that the documentation for the process is missing or out of date"
[[28]](#ref-28).

**The plan itself unreachable during the outage.** A federal ransomware response guide asks for "a hard copy
of the plan and an offline version" [[31]](#ref-31); the continuity circular asks organizations to "strongly
consider multiple redundant media" for essential records [[29]](#ref-29). This is the one entry on this list
that no source in this research describes as an observed failure. It is a stated precaution, not a measured
failure, and this companion labels it that way rather than as something that has been seen to happen.

## 8. Relationships to other artifacts

**Business continuity plan and the Business Impact Analysis.** The analysis is upstream and separate: NIST
calls it "the first source for determining resiliency and contingency planning strategies" [[1]](#ref-1), and
this plan's Business Impact Analysis Summary section carries its results, never its worksheet
[[1]](#ref-1)[[4]](#ref-4)[[7]](#ref-7).

**Business continuity plan and a standalone disaster recovery plan.** Where one exists separately, this
plan's Purpose and Scope section points to it rather than duplicating it, following the shape FEMA's own
template allows [[4]](#ref-4); where none exists, this bundle's full variant carries the Disaster Recovery
section instead.

**Business continuity plan and the production readiness review.** The library's own worked-example thread
names this plan without filling it in:
[`production-readiness-review_example.md`](../production-readiness-review/production-readiness-review_example.md)
records that "Backup and disaster recovery for that database is Platform's own standing responsibility,
reviewed under Platform's own instrument, and is not duplicated here", marking that review's own data and
backup criterion Not Applicable on that ground. This bundle's own worked example is the instrument that
review names without showing (section 10 below).

**Business continuity plan and the runbook.** Both are `standing-standards` siblings and both fail the same
way the family contract names, by drifting quietly out of date while everyone believes they are current
([`standing-standards.md`](../../docs/internal/contracts/standing-standards.md)). A runbook is the procedure
for a known, usually smaller, operational situation; this plan is the procedure for a significant disruption
to the business itself. Where California's own instructions describe "A description of how the incident
response plan and strategy interplays with" the technology recovery plan and identify who declares a
disruption a disaster [[6]](#ref-6), that interplay is the seam between this plan's Activation and Incident
Management section and an organization's own incident response runbook.

**Business continuity plan and the definition of done.** Both are `standing-standards` members, but they are
judged against different objects: a definition of done governs whether an increment of work is finished; this
plan governs whether an organization can keep operating through a disruption. Neither source read for this
bundle names the other.

## 9. Adaptations

**Regulated financial institutions** carry obligations this research found nowhere else: FINRA's rule binds
member firms to disclose their plan's disruption handling to customers and to "conduct an annual review of
its business continuity plan" [[30]](#ref-30), and the 2003 FFIEC booklet asks that "The board of directors
reviews and approves the plan(s) annually and after significant changes" with independent audit involvement
[[9]](#ref-9).

**State government entities in California** carry a specific annual filing obligation distinct from any
testing cadence: "Each state agency or entity must annually file a copy of" its technology recovery plan
[[7]](#ref-7), structured against SIMM 5325-A's own numbered sections [[6]](#ref-6).

**UK government and public-sector bodies under a Cabinet Office mandate** carry an explicit ISO 22301 tie
this research found in no other national source: "This policy framework sets out the arrangements necessary
to ensure Business Continuity Management (BCM) is performed in accordance with ISO 22301 as required by
Cabinet Office" [[12]](#ref-12).

**Organizations with contracted suppliers or subcontractors** can borrow a supplier contract's own flow-down
obligation directly: "Supplier shall ensure all Subcontractors have Business Continuity Programs and Disaster
Recovery Plans sufficient to meet delivery of the Services during a Disruptive Event" [[32]](#ref-32), with a
timed notification duty on top of it.

**This research found nothing to support an org-size or solo-versus-team adaptation**, and the companion
states that gap rather than inventing a scaling rule no source carries.

## 10. Worked example

[`business-continuity-plan_example.md`](business-continuity-plan_example.md) is the instrument the
production readiness review's own worked example names without showing: Acme Analytics' Platform team's
business continuity plan for the shared Postgres database that `saved_view` and other services, including
`dashboard-service`, depend on. It is worth checking three things in it: that it exists on or before
2026-08-22, the production readiness review's own date, since that review's Not Applicable ruling on backup
and disaster recovery depends on this plan already existing; that its owner is Dana Osei, Staff Engineer,
Platform, the title six other examples in this thread give consistently; and that its recovery figures,
RTOs, RPOs and the like, are labelled illustrative rather than presented as fact, since no such figure exists
anywhere else in this library's worked-example thread.

---

## References

<a id="ref-1"></a>[1] Swanson, Bowen, Phillips, Gallup, and Lynes (NIST), "[Contingency Planning Guide for
Federal Information Systems](https://nvlpubs.nist.gov/nistpubs/legacy/sp/nistspecialpublication800-34r1.pdf),"
NIST Special Publication 800-34 Revision 1, May 2010 (accessed 2026-10-14). Supports the definitions of the
business continuity plan, disaster recovery plan, contingency plan, continuity of operations plan, Business
Impact Analysis, RTO, RPO, and maximum tolerable downtime; the plan types' relationship; the contingency
plan's activation, recovery and reconstitution phases; review cadence; exercise types; and roles. The most
heavily cited source in this bundle. [primary]

<a id="ref-2"></a>[2] NIST, "[disaster recovery plan (DRP)](https://csrc.nist.gov/glossary/term/disaster_recovery_plan),"
Computer Security Resource Center Glossary (accessed 2026-10-14). Supports a second, conflicting CNSSI
4009-2022 definition that scopes disaster recovery to the original facility rather than an alternate one.
[primary]

<a id="ref-3"></a>[3] NIST, "[business continuity plan (BCP)](https://csrc.nist.gov/glossary/term/business_continuity_plan),"
Computer Security Resource Center Glossary (accessed 2026-10-14). Supports that the glossary carries no
second, competing definition for the business continuity plan the way it does for disaster recovery.
[primary]

<a id="ref-4"></a>[4] FEMA / Ready Business, "[Business Continuity Plan](https://www.ready.gov/sites/default/files/2020-03/business-continuity-plan.pdf)"
fill-in PDF template (accessed 2026-10-14). Supports the template's section headings and field labels in
printed order, and what it says and does not say about who writes, approves, and activates the plan.
[primary]

<a id="ref-5"></a>[5] FEMA / Ready Business, "[Business Continuity Planning](https://www.ready.gov/business-continuity-plan),"
Ready.gov (accessed 2026-10-14). Supports the short page's own characterization of a business continuity
plan; confirms the page names no activation authority. [primary]

<a id="ref-6"></a>[6] California Department of Technology, Office of Information Security, "[Technology
Recovery Plan Instructions](https://www.cdt.ca.gov/wp-content/uploads/policy/simm/SIMM-5325-A-Technology-Recovery-Plan-Instructions.pdf)"
(SIMM 5325-A, March 2023) (accessed 2026-10-14). Supports the numbered section structure this bundle's
Disaster Recovery section draws on, the job-title assignment rule, and the single-source statement that
the recovery plan is "just one portion" of business continuity. [primary]

<a id="ref-7"></a>[7] California Department of General Services, "[State Administrative Manual Section 5325.1,
Technology Recovery Plan](https://www.dgs.ca.gov/Resources/SAM/TOC/5300/5325-1/10-29-2025)" (revised
10/29/2025) (accessed 2026-10-14). Supports the governing policy clause requiring the plan, tying it to the
Business Impact Analysis and the Continuity Plan, and the annual filing requirement. [primary]

<a id="ref-8"></a>[8] California Department of Technology, "[Summary of What Changed in SIMM September
2013](https://www.cdt.ca.gov/wp-content/uploads/2017/02/Summary_of_What_Changed_in_SIMM_September_2013.pdf)"
(accessed 2026-10-14). Supports the 2013 renaming of SIMM 65A, "Disaster Recovery Documentation," to SIMM
5325A, "Technology Recovery Plan Instructions." [primary]

<a id="ref-9"></a>[9] Federal Financial Institutions Examination Council, "[Business Continuity Planning](https://fdic.gov/system/files/2024-07/bcp.pdf),"
IT Examination Handbook booklet (March 2003), retrieved via an FDIC mirror (accessed 2026-10-14). Supports
every testing and review-frequency statement, the four named test types, the insufficient-test rule, and
the independent-observer requirement this bundle draws on; this is the 2003 edition, at least two editions
old, not the current booklet. [primary]

<a id="ref-10"></a>[10] Board of Governors of the Federal Reserve System, "[SR 19-13, FFIEC Information
Technology Examination Handbook](https://www.federalreserve.gov/supervisionreg/srletters/sr1913.htm)"
(transmittal letter, December 2019) (accessed 2026-10-14). Supports that the 2019 Business Continuity
Management booklet exists and replaced the February 2015 edition; carries no cadence language of its own.
[primary]

<a id="ref-11"></a>[11] FDIC, "[Financial Institution Letter FIL-71-2019, Updated FFIEC IT Examination
Handbook, Business Continuity Management Booklet](https://archive.fdic.gov/view/fdic/8792/fdic_8792_DS1.pdf)"
(archived copy) (accessed 2026-10-14). Supports that the 2019 booklet replaced the February 2015 booklet and
the regulator's own framing of the name change from planning to management; settles no cadence question
since it is a transmittal letter, not the booklet. [primary]

<a id="ref-12"></a>[12] GOV.UK (Ministry of Justice / HMPPS), "[HMPPS business continuity policy
framework](https://www.gov.uk/government/publications/hmpps-business-continuity-policy-framework)"
publication page (accessed 2026-10-14). Supports the publication's own annex list and its one-paragraph
policy summary tying the framework to ISO 22301. [primary]

<a id="ref-13"></a>[13] HM Prison & Probation Service / Ministry of Justice, "[HMPPS Business Continuity and
Resilience Policy Framework](https://assets.publishing.service.gov.uk/media/640611b48fa8f527f2ef9658/hmpps-business-continuity-policy-framework.pdf)"
(Re-Issue 06 March 2023) (accessed 2026-10-14). Supports the framework's own plan structure and annexes, its
review and exercise cadence, and its direct statement separating who activates a plan from who writes and
maintains it. [primary]

<a id="ref-14"></a>[14] BCI (Kieran Matthews), "[Good Practice Guidelines 7.0: A new focus on the Business
Continuity Management System](https://www.thebci.org/news/bci-gpg-edition-7-0-a-new-focus-on-the-bcms.html),"
BCI news article, 12 October 2023 (accessed 2026-10-14). Supports the operational-cycle-inside-a-management-
cycle framing and the professional body's own move away from lifecycle language. [practitioner]

<a id="ref-15"></a>[15] DRI International, "[Professional Practices](https://drii.org/resources/professionalpractices)"
resource page (2023 revision, public Executive Summary section) (accessed 2026-10-14). Supports the ten
Professional Practices' names and one-line objectives, including plan development and the exercise/test,
assessment and maintenance practice; the full practices document is gated behind login. [practitioner]

<a id="ref-16"></a>[16] SANS Institute / Consensus Policy Resource Community, "[Disaster Recovery Plan
Policy](https://assets.contentstack.io/v3/assets/blt36c2e63521272fdc/blt3cf8b9a0b2e45133/5e9ddb9ab1704560004196b5/disaster_recovery_plan_policy.pdf)"
(2014 policy template, SANS-hosted mirror copy) (accessed 2026-10-14). Supports the management-often-ignores
failure mode, the stated relationship between the disaster recovery plan and the business continuity plan,
the plan's required sub-plans, and its testing and review cadence. [practitioner]

<a id="ref-17"></a>[17] SANS Institute, "[Resilience Management Policy](https://www.sans.org/information-security-policy/resilience-management-policy/)"
(policy template, last updated February 2026; text read from its linked PDF) (accessed 2026-10-14). Supports
the current SANS framing of business continuity and disaster recovery as one safeguard inside a broader
resilience policy, and how much less it specifies about plan content than the 2014 policy. [practitioner]

<a id="ref-18"></a>[18] ISO, "[ISO 22301:2019, Security and resilience, Business continuity management
systems, Requirements](https://www.iso.org/standard/75106.html)," catalogue page only (accessed 2026-10-14).
Supports only what the free catalogue page itself states, the documented-management-system framing; the
standard's own clause text is paywalled and was not read. [primary]

<a id="ref-19"></a>[19] URM Consulting (Phillip Knight), "[Business Continuity Exercising](https://www.urmconsulting.com/blog/business-continuity-exercising)"
(blog, 5 June 2025, based on a URM webinar) (accessed 2026-10-14). Supports the plan-insufficient-without-
exercising argument and the test-versus-exercise distinction. [vendor]

<a id="ref-20"></a>[20] AWS, "[Disaster Recovery of Workloads on AWS: Recovery in the Cloud](https://docs.aws.amazon.com/whitepapers/latest/disaster-recovery-workloads-on-aws/disaster-recovery-workloads-on-aws.html)"
whitepaper landing page (accessed 2026-10-14). Supports the whitepaper's own scope statement and its
publication-level framing of RTO and RPO. [vendor]

<a id="ref-21"></a>[21] AWS, "[Introduction](https://docs.aws.amazon.com/whitepapers/latest/disaster-recovery-workloads-on-aws/introduction.html),"
Disaster Recovery of Workloads on AWS whitepaper (accessed 2026-10-14). Supports AWS's RPO and RTO
definitions, its stated relationship between disaster recovery and business continuity planning, and the
disaster-recovery-versus-availability distinction. [vendor]

<a id="ref-22"></a>[22] AWS Well-Architected Framework, "[REL13-BP01, Define recovery objectives for downtime
and data loss](https://docs.aws.amazon.com/wellarchitected/latest/framework/rel_planning_for_recovery_objective_defined_recovery.html)"
(accessed 2026-10-14). Supports AWS's formal RTO and RPO definitions and its dependency-mapping questions for
assigning them per workload. [vendor]

<a id="ref-23"></a>[23] AWS Well-Architected Framework, "[REL13-BP02, Use defined recovery strategies to meet
the recovery objectives](https://docs.aws.amazon.com/wellarchitected/latest/framework/rel_planning_for_recovery_disaster_recovery.html)"
(accessed 2026-10-14). Supports the four named AWS recovery strategies and the cost-versus-RTO/RPO tradeoff.
[vendor]

<a id="ref-24"></a>[24] Google Cloud, "[Disaster recovery planning guide](https://docs.cloud.google.com/architecture/dr-scenarios-planning-guide),"
Cloud Architecture Center (accessed 2026-10-14). Supports Google's RTO and RPO definitions, the cold/warm/hot
pattern vocabulary, disaster recovery as a subset of business continuity planning, and the backup-versus-full-
recovery-process distinction. [vendor]

<a id="ref-25"></a>[25] Google Cloud, "[Perform testing for recovery from data loss](https://docs.cloud.google.com/architecture/framework/reliability/perform-testing-for-recovery-from-data-loss),"
Well-Architected Framework, reliability pillar (accessed 2026-10-14). Supports the three criteria for judging
a recovery test, data integrity, RTO and RPO, and the restore-to-a-non-production-environment testing method.
[vendor]

<a id="ref-26"></a>[26] Microsoft, "[What are business continuity, high availability, and disaster
recovery?](https://learn.microsoft.com/en-us/azure/reliability/disaster-recovery-overview)," Azure
Well-Architected Framework reliability documentation (accessed 2026-10-14). Supports Microsoft's RPO and RTO
definitions, its explicit business-continuity/high-availability/disaster-recovery relationship, and the
instruction to include human processes in recovery drills. [vendor]

<a id="ref-27"></a>[27] Google SRE Book, "[Chapter 17, Testing for Reliability](https://sre.google/sre-book/testing-reliability/)"
(accessed 2026-10-14). Supports a narrow passage on designing disaster recovery tools to run offline and
checkpointable; the chapter as fetched does not carry the fuller disaster-exercise material this research
expected. [practitioner]

<a id="ref-28"></a>[28] Tanya Reilly, interviewed by Nikki McDonald, "[Creating better disaster recovery
plans](https://www.oreilly.com/content/creating-better-disaster-recovery-plans/)" (O'Reilly) (accessed
2026-10-14). Supports the backup-versus-restore-strategy distinction, why untested recovery fails, and
service-dependency deadlock during recovery. [practitioner]

<a id="ref-29"></a>[29] FEMA, "[Continuity Guidance Circular 1 (CGC 1): Continuity Guidance for Non-Federal
Entities](https://www.lcc.mn.gov/inactive/eeptf/meetings/150819/5%20-%20Continuity%20Guicance%20Circular%201.pdf)"
(July 2013), read on an inactive legislature mirror (accessed 2026-10-14). Supports delegation of authority,
succession by position title, reconstitution and deactivation, essential-records accessibility, and the
standing Corrective Action Program; cited only as the 2013 circular, never as current FEMA guidance.
[primary]

<a id="ref-30"></a>[30] FINRA, "[Rule 4370, Business Continuity Plans and Emergency Contact
Information](https://www.finra.org/rules-guidance/rulebooks/finra-rules/4370)" (accessed 2026-10-14).
Supports the enforced customer-disclosure duty, the third-party dependency disclosure requirement, and the
annual review and material-change update requirements. [primary]

<a id="ref-31"></a>[31] CISA, NSA, FBI, MS-ISAC, "[#StopRansomware Guide](https://www.cisa.gov/sites/default/files/2023-05/stopransomware_guide_508c.pdf)"
(2023) (accessed 2026-10-14). Supports the offline-backup requirement against ransomware, the caution against
relying on immutable storage, and the requirement to keep a hard copy and an offline version of the response
plan itself. [primary]

<a id="ref-32"></a>[32] Visa, "[Disaster Recovery and Business Continuity Requirements](https://usa.review.visa.com/content/dam/VCOM/regional/na/us/partner-with-us/documents/disaster-recovery-and-business-continuity-requirements.pdf)"
(supplier contract schedule) (accessed 2026-10-14). Supports the supplier-subcontractor continuity flow-down
requirement and the timed disaster-notification duty to the affected counterparty. [primary]
