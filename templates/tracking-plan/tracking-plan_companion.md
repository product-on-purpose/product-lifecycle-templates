# Companion: The Tracking Plan

> The deep explainer for the tracking-plan bundle. Read this to understand what a tracking plan is, where
> it came from, why it is shaped the way it is, and where practitioners disagree about it. The short
> operator card is `tracking-plan_guide.md`; a fully worked instance is `tracking-plan_example.md`. Inline
> citations like [[1]](#ref-1) resolve to the [References](#references) at the bottom, tagged by source
> reliability.

---

## 1. Orientation

A tracking plan is the standing catalog of the analytics events a product records, the properties each
one carries, and the user and account traits it keeps, together with why each is collected, when it
fires, where it comes from, who owns it, and whether it is still live. Amplitude puts the job in one
sentence: "A tracking plan defines every event and property you collect, why you collect each one, and
which source emits it." [[8]](#ref-8). Countly adds what the document does across teams: "It translates
product questions into an implementation contract for product, engineering, analytics, privacy, and
marketing teams." [[14]](#ref-14).

- **The core is agreed, the edges are contested.** Every admitting source shares a spine: a list of
  events, a reason for each, their properties and types, where each comes from, and a status. Past that
  spine, sources disagree about where the plan lives, how often it is reviewed, how events are named, and
  who owns what. Section 6 states each disagreement as a disagreement rather than resolving it.
- **The sources that define the document are mostly vendors, and most of those vendors sell the tool the
  plan is enforced in.** [[2]](#ref-2), [[6]](#ref-6), [[9]](#ref-9), and [[12]](#ref-12) are vendor
  documentation or vendor-published blogs defining the artifact; this bundle treats their definitions as
  the convergent core and does not present a vendor's case for its own product as a finding. The sources
  behind the contested and failure-mode material are practitioners writing independently of a specific
  tool: [[19]](#ref-19), [[20]](#ref-20), [[27]](#ref-27), [[28]](#ref-28), [[30]](#ref-30), and the
  engineering-handbook sources [[33]](#ref-33) through [[37]](#ref-37).
- **No source read for this bundle measured whether keeping a tracking plan improves data quality or
  product decisions.** What exists is practitioner testimony about what goes wrong without one: a named
  failure taxonomy [[19]](#ref-19) and one practitioner's own claim, "A tracking plan without governance
  is a document that's wrong within 60 days of shipping." [[20]](#ref-20), stated here as that author's
  view, not a measurement. This bundle's reason to exist
  rests on that testimony and on the failure modes it names, not on a measurement, and the guide repeats
  this rather than letting the document imply more certainty than the research found.
- **The document is in scope here; the schema a tool enforces at runtime is not.** Several of the same
  vendors keep a live, validated copy of the plan inside their product. This companion treats the written
  document as the artifact this library templates, and the in-tool, enforced form as something the
  document may later feed (section 8).

---

## 2. Origins and evolution

No source read for this bundle traces when the term "tracking plan" began, who coined it, or which vendor
first published one, and this companion does not invent a founding date. Nor does any source state that
the written document came first and the in-tool form after it. This library reads the document as upstream
of the enforced schema, and section 8 states that reading as the library's own position, not as a finding.

What the sources do show is the two forms side by side. Snowplow's own list of what a tracking plan
carries at its core names an explicit owner, consumers, and a change history, with no tool requirement at
all [[17]](#ref-17). RudderStack frames the document as the thing a team writes down before anything
validates against it: "Tracking Plans allow us to plan
and prescribe what our data should look like before it is sent to our destinations." [[15]](#ref-15).
DataTalks.Club's practitioner wiki states the document form as the normal starting point for a small
event set: "Teams can start with a spreadsheet or document when the event set is small. The plan still
comes before instrumentation." [[28]](#ref-28). Several vendors also validate live data against a plan
held in their own tool: Twilio Segment's Protocols feature "allows you to validate your expected events
against the live events that are delivered to Segment" [[4]](#ref-4); mParticle's blog states that once a
plan exists in its tool, "developers have the tools to programmatically import data tracking plans into
the codebase, and use this to enforce data quality throughout event instrumentation" [[12]](#ref-12); and
Avo generates implementation code directly from the plan and validates data against it [[1]](#ref-1).
RudderStack also treats the plan as something revised continually: "the intention for tracking plans is
to be an iterative process and a part of every sprint" [[15]](#ref-15).

One more practice is sourced narrowly to Avo: a git-mirrored branch-and-review workflow
for proposing a change to the standing plan before it merges into the plan's own main branch, with a
one-to-one mapping it states itself: "Typically there's a one to one mapping between Avo branches and git
branches." [[23]](#ref-23). Section 3's Change Process subsection and section 5 return to this workflow.

Two dated facts are worth recording and flagging as exactly what they are. Amplitude's own blog post on
creating a tracking plan carries an original-publication date of 2022-06-07 and an updated date of
2024-11-15 [[9]](#ref-9), which this companion reads only as evidence that the vendor has kept the page
current, not as a claim about when tracking plans began. [[19]](#ref-19), a single practitioner piece
published in 2026, reports that Mixpanel's Data Standards feature "launched Apr 16, 2025" [[19]](#ref-19),
a fact this companion attributes to that report rather than to Mixpanel directly, consistent with
contested item 7 in section 6.

---

## 3. Anatomy (section by section)

The template carries seven sections, four of them in lean. Every field named below is one a real,
published source carries; where two published sources disagree about a field's presence or its values,
that disagreement is stated rather than smoothed into a single answer.

### Purpose and Boundary

**What it is:** a short statement of what the plan covers, product-wide, and what does not belong in it.
**Why it exists:** because several neighboring documents use overlapping language, and the first job of this
section is to rule them out before the catalog starts. Wizbrand's forward-looking line draws the plan
itself: "A tracking plan describes what you intend to track (events, triggers, parameters) and why."
[[31]](#ref-31). Against the data dictionary, the same source gives the opposite tense: "A Data Dictionary
documents what the data means and how it is structured once implemented." [[31]](#ref-31). Against the
broader measurement plan, Wizbrand states the containment directly: "the measurement plan explains why
you track; the tracking plan explains how." [[32]](#ref-32). Against one feature's own instrumentation
slice, this section points to the PRD's own "Analytics and instrumentation" section, where a single
feature's events are first proposed; this bundle reads the tracking plan as what every feature's slice
merges into, following the Change Process subsection below, and states that reading as its own position
rather than as any source's claim.

### Naming Conventions

**What it is:** a short statement of the convention the catalog's event names follow. **Why it exists:**
because the forms in use disagree outright, and naming the convention once at the top keeps the catalog
itself from drifting. Countly names the obligation generally: "A strong plan defines naming conventions"
[[14]](#ref-14). Avo ties the convention to a shared tense and case: "Note how each of these event names
shares the same tense (past tense) and capitalization." [[3]](#ref-3). Twilio Segment's own editor
enforces exact matching against whatever is chosen: "Casing, spacing and spelling matter." [[4]](#ref-4).
The object-then-action form, and the past-tense verb, are attributed to the practitioners who state them,
not to any vendor's own specification: a consultancy's engineering handbook reports that "Segment's
object-action framework quickly came up as a robust and simple to understand framework" and states the
rule itself, "Action: defines how users can interact with the objects in the application. An action must
be in the past" [[27]](#ref-27). An independent newsletter states the same preference in its own voice:
"I recommend using the object+action framework because it's easy to visualise what object your user is
interacting with and what action has taken place." [[30]](#ref-30). The same newsletter explicitly
declines to settle casing: "Choose one case and stick with it." [[30]](#ref-30). Casing itself is contested: the same
engineering handbook requires snake_case outright [[27]](#ref-27), while the newsletter above lists five
casing styles and picks none [[30]](#ref-30). This section also asks whether the same event name holds up
across platforms, because one platform's automatic screen-tracking behavior can silently break that
assumption: the engineering handbook names the problem directly, "the screen names differ per platform,
which makes it hard to actually use the data." [[27]](#ref-27). The template states a convention and picks
none of these forms for the author.

### Event and Property Catalog

**What it is:** the load-bearing table, one row per event, naming its properties, its source, its owner,
and its status. **Why it exists:** because the plan's whole value is in never losing track of what a
product actually records. The columns named below are the ones three or more published sources share.
The event's **name** follows the Naming Conventions section above. **When it fires** is Countly's
"triggering conditions" [[14]](#ref-14) and Twilio's blog worked example, where the "where" column is "the
location and time at which the event is being tracked" [[6]](#ref-6). **Why it is collected**, or the
question it answers, is the same worked example's WHY column, "a short description of the business
purpose that justifies tracking the event" [[6]](#ref-6), Avo's instruction to "Summarize the reason for
tracking each event and property" [[2]](#ref-2), and Avo's own first worksheet column, "1. KPIs"
[[3]](#ref-3). **Its properties**, with type and allowed values, are Avo's "7. Property value types"
[[3]](#ref-3), Twilio Segment's "Permitted Values" field, "Enter simple regular expressions to validate
property values" [[4]](#ref-4), and Amplitude's "A name, description, examples, and rules define each
property." [[8]](#ref-8). **Where it comes from and where it goes** is Amplitude's "which source emits
it" [[8]](#ref-8) and Amplitude's own blog naming "data destinations" among what the plan specifies
[[9]](#ref-9). **Its owner** is convergent across the research: Amplitude's blog ties the source field
directly to assigning one, "Doing so even makes it easy to assign an owner-the person responsible for the
implementation of that event." [[9]](#ref-9); Amplitude's event-taxonomy page asks for "central
documentation listing every event, property, data type, and owner" [[10]](#ref-10); Countly names owners
among a plan's contents [[14]](#ref-14); and one practitioner source states the strictest form of the
rule, "owner: a named person, not a team." [[20]](#ref-20). Who owns an individual event is a different
question from who owns the plan as a whole; section 6, item 5, keeps the two apart. **Its status** is
likewise convergent: Amplitude's event-taxonomy page asks teams to "Track all taxonomy changes with
version labels like "proposed," "active," "deprecated," and "removed."" [[10]](#ref-10); Avo carries a "9.
Status" column [[3]](#ref-3); and GitLab's own event-definition and event-lifecycle guides give an event a
status field with a "removed" value as part of a defined removal procedure [[33]](#ref-33)[[34]](#ref-34).
A table section, so it carries a PRIORITY marker and a ROW HINT.

### User and Account Properties

**What it is:** a table of the traits kept about a user or an account, apart from any event. **Why it
exists:** because five independent sources keep this list separate from the event catalog rather than
folding it in. Twilio Segment defines traits by what they are not: events, but persistent facts, "Objects
persist over time, so traits can change over time." [[7]](#ref-7). Amplitude's documentation splits the
idea in two, "User properties capture traits about the user." and a parallel field for a group, "Group
properties make it easy to associate a user with a particular account" [[8]](#ref-8). Twilio Segment's
own editor treats adding a trait as a parallel action to adding an event, "You can define which traits you
expect to see passed in Identify or Group calls like how you would add Track calls to the Tracking Plan."
[[4]](#ref-4). Amplitude's blog gives the same split its own worksheet tab, instructing the author to "list
down all user properties, their data types, expected values, and destinations in the sheet labeled User
Properties." [[9]](#ref-9). Mixpanel's own best-practice checklist names "user profile properties"
alongside event properties as a distinct line item [[11]](#ref-11), and mParticle's platform guide groups
"an event, user attributes, or user identities" as the three kinds of thing a single data point can be
[[13]](#ref-13).

### Privacy, Sensitivity and Retention

**What it is:** a place to flag an event or property as sensitive, state how long it is kept, and name
what happens to it before it reaches storage. **Why it exists, and why it is full-only:** the sourcing
here is thinner and more varied than the catalog's core columns, so the section presents the shapes
different sources use rather than choosing one, and it is full-only because a lean plan for a small event
set may carry nothing sensitive yet. Countly lists "sensitivity, retention, and validation" among what a
strong plan carries [[14]](#ref-14). One practitioner source makes the flag itself a column with a defined
downstream effect: "pii_flag: true or false; routes the event through masking or exclusion pipelines."
[[20]](#ref-20). A data-governance guide frames the same need at the policy level rather than the column
level: "Your policies must include strict controls to prevent the accidental collection of Personally
Identifiable Information (PII)" [[21]](#ref-21). Mozilla's own telemetry process attaches sensitivity and
an expiry directly to each metric's own definition, "data_sensitivity:" and, separately, "expires:"
[[36]](#ref-36). Mozilla's data-collection policy ties consent to how sensitive the category is rather
than to a single yes-or-no answer, and asks the requester to state up front "for how long it will be
collected" [[37]](#ref-37). This section presents these shapes and lets the author choose among them; no
regulator was read for this bundle, so the section gives no legal advice on consent or retention, and the
guide repeats that limit.

### Review and Ownership

**What it is:** the plan's own named owner, apart from any event's owner, and how often the whole plan is
reviewed. **Why it exists:** because a standing document nobody is accountable for, and nobody revisits,
decays the way section 7 describes. Snowplow states the plan-level role directly: "An explicit owner;
that is responsible for maintaining and updating the data over time" [[17]](#ref-17), and separately names
who else has a stake in it, "Subscribers; allow colleagues to express an interest in understanding changes
that are made to the data" [[17]](#ref-17). How often the whole plan is reviewed is contested outright
(section 6, item 2), so this section asks the author to name an interval and what else, beyond the
calendar, should trigger a review, rather than stating one as a norm.

### Change Process and Version History

**What it is:** how a change to the standing plan is proposed, reviewed, and recorded, and how a removal
is carried out as its own procedure rather than a quiet status flip. **Why it exists, and why it is
full-only:** a plan that several teams change, that carries personal data, or that someone will later ask
"what changed and who approved it" needs this section; a lean plan for a small, stable event set may not
yet. Avo's branched workflow, introduced in section 2, is the fullest sourced version of the mechanism: "A
branch allows you to draft changes to the tracking plan in isolation, without impacting the main branch,
which contains the single source of truth of what's currently being tracked." [[22]](#ref-22), reviewed
before it ships, "When you've suggested changes to your tracking, mark the branch as ready for review, and
assign an editor or admin to review the changes." [[23]](#ref-23), and merged alongside its matching code
change, "As soon as the git branch is merged into the git main branch, they merge their Avo branch in the
Avo main branch." [[24]](#ref-24). A distinct, independently sourced approval path names three roles:
Amplitude's event-taxonomy page states, "Event requesters propose new events with clear use cases", "Data
stewards review naming and check for duplicates", and "Domain owners approve events within their product
areas" [[10]](#ref-10), and Mozilla's data-collection policy names an overlapping pair for data requests
specifically, a "Data requester" and a "Data steward" who "ensures the data collection process is
followed" [[37]](#ref-37). The record of a change is Snowplow's own stated element, "Change history; a
complete audit log of the changes that have been made to the tracking plan" [[17]](#ref-17), matched by
one practitioner's instruction to "Document what changed, when, why, and who approved it." [[10]](#ref-10).
Removal is sourced as a defined procedure, not a status flip: GitLab's event-lifecycle guide gives it five
explicit steps, including "Update the event definition file to set the status field to removed."
[[34]](#ref-34). A validation gate before an event ships is sourced independently twice: GitLab's own
handbook has an engineer "Verify test events match properties defined in the Issue" before a product
manager's instrumentation issue is implemented [[35]](#ref-35), and Mozilla requires that "Data reviews are
needed on all patches that add new telemetry or modify existing telemetry." [[36]](#ref-36).

---

## 4. Variants and sizing

**Lean** carries Purpose and Boundary, Naming Conventions, the Event and Property Catalog, User and
Account Properties, and Review and Ownership. It is sized for a product starting out, or for a small
event set, following the practitioner wiki's own framing, "Teams can start with a spreadsheet or document
when the event set is small." [[28]](#ref-28), the phased build-out one vendor documentation page
recommends, "Don't try to track everything at once. Build your tracking in phases" [[29]](#ref-29), and
Twilio's own four-column worked example [[6]](#ref-6).

**Full** adds Privacy, Sensitivity and Retention and Change Process and Version History. It is sized for
a plan that several teams change, that holds personal data, or that someone will later need to ask what
changed and who approved it, following Amplitude's named approval roles [[10]](#ref-10), Snowplow's named
owner and audit trail [[17]](#ref-17), and Mozilla's formal data-collection review [[37]](#ref-37). Avo's
own ten-column worksheet [[3]](#ref-3) and Countly's longer field list, "naming conventions, data types,
allowed values, triggering conditions, examples, sensitivity, retention, and validation" [[14]](#ref-14),
show the fuller weight a full-variant plan is expected to carry.

---

## 5. Methodology lineage

The research behind this bundle is a vendor-and-practitioner analytics-engineering canon, not a survey of
named delivery methodologies, and it would misstate the evidence to attach Scrum, SAFe, Shape Up, or
Amazon's own practice to a tracking plan. No source read for this bundle names any of those methodologies
in connection with a tracking plan, and this companion makes no claim about how any of them treats one.

What the research does support are four distinct, independently sourced practices for keeping a plan
current, each attributable to the source that states it and to no wider tradition:

- **Sprint-paced iteration.** RudderStack is the one place in this research where a named agile unit of
  work appears at all: "the intention for tracking plans is to be an iterative process and a part of
  every sprint" [[15]](#ref-15). This companion states that as RudderStack's own framing, not as a claim
  about Scrum generally.
- **Branch-and-merge review.** Avo's workflow, described in sections 2 and 3, proposes a change on its own
  branch, reviews it, and merges it alongside the matching code change [[22]](#ref-22)[[23]](#ref-23)[[24]](#ref-24).
  This companion describes the mechanism as Avo states it and does not attach a wider label, such as
  "git-flow" or "trunk-based development," to what the source itself does not name.
  
- **Issue-gated engineering review.** GitLab's own handbook routes a new event through a product
  manager's instrumentation issue, an engineer's implementation, and a peer validation step before it
  ships, "Verify test events match properties defined in the Issue" [[35]](#ref-35), and separately defines
  a multi-step, auditable removal procedure [[34]](#ref-34). This companion describes this as GitLab's own
  documented practice, not as evidence for any named methodology beyond GitLab's own engineering process.
- **Formal data review.** Mozilla requires a review before any telemetry patch ships: "Data reviews are
  needed on all patches that add new telemetry or modify existing telemetry." [[36]](#ref-36). It also runs an
  annual survey of every existing collection, "the data collection owner and peers will survey all of the
  existing data collection systems for their product or project... To ensure that it is still necessary
  and useful to collect a piece of data." [[37]](#ref-37). This is the closest the research comes to a
  regulated-style review cadence, sourced to Mozilla's own policy and not generalized beyond it.

---

## 6. Debates and contested boundaries

1. **Where the plan lives: a document, a spreadsheet, or the tool.** A vendor arguing for its own
   schema-first product calls the spreadsheet fragile, "If you've ever tried to manage a spreadsheet at
   scale, you know how easily things can break." [[25]](#ref-25). Against that, one practitioner wiki and
   one newsletter both treat a spreadsheet as a normal and sufficient starting medium, "Setup: Use a
   spreadsheet, Miro board, paper or whiteboard." [[30]](#ref-30); [[28]](#ref-28). Avo's own docs make the
   in-tool plan primary [[1]](#ref-1); Twilio Segment validates live events against an importable spec
   [[4]](#ref-4); mParticle accepts either [[12]](#ref-12). This bundle templates the document and names
   the tool as where it may later be enforced, rather than picking a side.
2. **How often the plan is reviewed.** One practitioner states a fixed ninety-day cadence and credits it
   to a named third party, "The 90-day audit rule from House of MarTech is the right cadence." [[20]](#ref-20).
   A monitoring vendor rejects any fixed interval outright, "Manual spot-checks and quarterly audits feel
   like relics from a different era." [[21]](#ref-21). Mozilla instead runs an annual survey of every
   collection [[37]](#ref-37), while Countly ties review to an event entirely, "It should be versioned and
   reviewed whenever the product or measurement strategy changes." [[14]](#ref-14). No interval is a
   convention here; the template asks the author to choose one and to name what else, beyond the
   calendar, should trigger a review.
3. **Event naming.** Avo wants one tense and one capitalization [[3]](#ref-3); the engineering handbook
   and the independent newsletter both recommend an object followed by a past-tense action
   [[27]](#ref-27)[[30]](#ref-30); GitLab instead uses an operation, its target, and where or when it
   happened, in its own words rather than a direct quotation, because the cached page escapes the
   characters a verbatim quote would need [[33]](#ref-33). One vendor documentation page labels its own
   pattern "Action_object pattern" while its own examples run object first, which this companion reads as
   an inconsistency inside that one source, not a second convention [[29]](#ref-29). Casing is contested
   outright: the engineering handbook requires snake_case [[27]](#ref-27), and the newsletter declines to
   choose, "Choose one case and stick with it." [[30]](#ref-30). The template asks for a convention and
   picks none.
4. **Autocapture against a designed plan.** Exactly one source argues from the autocapture side, and even
   it does not say a plan is unnecessary: it calls the choice between autocapture and a hand-built plan
   "a false choice" [[25]](#ref-25), and it still advises a team to "manually capture 5-10 core KPIs"
   [[25]](#ref-25). Every other source in this research assumes a designed plan, and one states the
   ordering directly, "Build one before you instrument code" [[8]](#ref-8). A separate vendor's
   phased-build-out advice, "Don't try to track everything at once. Build your tracking in phases"
   [[29]](#ref-29), is about how much to plan at once, not whether to plan.
5. **Who owns what.** One practitioner wants exactly one named person per event and rejects team ownership
   in those words, "means nobody owns it." [[20]](#ref-20). Two sources describe a chain of roles instead
   of a single owner, requester, steward, and owner, with one adding an implementer [[10]](#ref-10)[[19]](#ref-19);
   Mozilla names a "Data requester" and a "Data steward" [[37]](#ref-37); GitLab's handbook gives creation
   to the product manager and validation to an engineer [[35]](#ref-35); and Snowplow gives each plan, when
   split by domain, "an explicit owner" [[17]](#ref-17). These answer different questions, an event's
   owner, the plan's own owner, and the approval path, and this bundle reads them as compatible rather than
   contradictory. The template keeps the event's owner, the plan's owner, and the approval path in separate
   places rather than collapsing them into one column.
6. **"Event taxonomy" or "tracking plan."** Amplitude's event-taxonomy page uses "event taxonomy" for the
   naming and categorizing system and asks for "central documentation" of it [[10]](#ref-10); Amplitude's
   own product documentation and its blog both use "tracking plan" for the catalog itself [[8]](#ref-8)[[9]](#ref-9).
   Amplitude does not state, on either page read for this bundle, whether the two are meant as one
   document. This bundle treats the taxonomy as the naming convention a tracking plan states, rather than
   as a second, separate artifact.
7. **Time-bound figures and one vendor's own claims.** [[19]](#ref-19) is a single piece dated 2026 that
   reports Mixpanel's Data Standards feature as "launched Apr 16, 2025", a fact attributed to that report
   and not confirmed against Mixpanel's own page. The same piece's stated ceiling of 10 to 200 events and
   its claim, "The most common tracking-plan failure mode is not technical - it is organizational."
   [[19]](#ref-19), are stated there as that author's own view, not as a measured result, and this
   companion repeats them, where it repeats them at all, with that attribution attached. [[20]](#ref-20)'s
   claim that an ungoverned plan is a document that's "wrong within 60 days of shipping." is likewise one
   practitioner's own claim, not a measured figure.

---

## 7. Anti-patterns and failure modes

No source read for this bundle measured how often real tracking plans fail, or how often keeping one
prevents a failure; what follows is a named, sourced list of the shapes failure takes, not a frequency
claim.

- **Owner departure.** The clearest, most fully sourced failure mode in this research: an event with no
  accountable person behind it decays once its author leaves. One practitioner piece states both the
  mechanism and its cost directly: "The event has a named owner or data steward accountable for its
  definition. An event with no owner is the owner-departure decay vector waiting to happen - the highest
  recovery cost in the decay table." [[19]](#ref-19). The same piece names five further decay vectors by
  name only, naming drift, an autocapture shift, identity fragmentation, over-tracking, and silent
  device-mode blocking [[19]](#ref-19); this companion names them because the source's own Supports
  material lists them, and says nothing further about what any one of them means, because only the
  owner-departure vector is quoted in full in the source read.
- **Governance treated as a one-time setup.** A data-governance guide from Trackingplan, a monitoring vendor
  with an interest in continuous checking, names this directly as a root cause of program failure: "A classic mistake is treating governance like a finite project-something you set
  up, document, and promptly forget. This "one-and-done" thinking is a primary reason so many programs
  fail." [[21]](#ref-21). The same source's remedy is continuous rather than periodic: "Governance has to
  be a living, breathing process, not a dusty binder on a shelf." [[21]](#ref-21).
  
- **Unclear, team-level ownership.** One practitioner states this as the specific failure behind the
  owner-per-event rule in section 3's catalog: ""The analytics team owns it" means nobody owns it. One
  named person per event, full stop." [[20]](#ref-20).
- **The spreadsheet outgrowing itself.** A vendor arguing for its own product still names a real, observed
  failure shape rather than only a sales pitch: "If you've ever tried to manage a spreadsheet at scale, you
  know how easily things can break." [[25]](#ref-25). This bundle reads the warning as genuine while
  reading its source's interest in the matter plainly, following section 1's framing of who is making each
  claim.
- **No gate before an event ships.** Where no validation step exists before an event reaches production,
  two independently sourced engineering practices supply the contrast rather than a named failure: GitLab
  requires a peer check against the instrumentation issue before implementation is considered done
  [[35]](#ref-35), and Mozilla requires a data review on every patch that adds or changes telemetry
  [[36]](#ref-36). This bundle reads the absence of either step, in a plan that has grown past a single
  team, as the condition the Change Process section exists to prevent.

---

## 8. Relationships to other artifacts

**Tracking plan vs the PRD's own instrumentation slice.** A single feature's events are first proposed in
the PRD's own `## Analytics and instrumentation` section, where a feature's launch names the metrics it
needs and the events that measure them. This bundle reads the tracking plan as the standing document that
every feature's slice merges into over the product's life, rather than a rival to the PRD section; that
reading is this library's own position, following the Change Process subsection's branch-and-merge and
instrumentation-issue mechanisms [[22]](#ref-22)[[24]](#ref-24)[[35]](#ref-35), and no source states that
ordering in those words.

**Tracking plan vs the data dictionary.** Different tenses, by Wizbrand's own account: "A tracking plan
describes what you intend to track (events, triggers, parameters) and why." against "A Data Dictionary
documents what the data means and how it is structured once implemented." [[31]](#ref-31). The same source
states how the two should relate in practice: "the tracking plan drives implementation; the Data
Dictionary keeps Analytics interpretation consistent over time." [[31]](#ref-31).

**Tracking plan vs the broader measurement plan.** Containment, not rivalry, again by Wizbrand's own
account: "A tracking plan is usually narrower and implementation-focused: events, parameters, triggers,
and QA steps." against "An Analytics Measurement Plan includes tracking details but also covers business
objectives, KPI definitions, governance, and reporting logic." [[32]](#ref-32).

**Tracking plan vs the KPI dashboard - the governance sibling it stands upstream of.** The tracking plan
defines the events a product records; the `kpi-dashboard` defines the metrics computed from those events
and locks each metric's own formula. This bundle holds that a tracking plan does not define or lock a
metric's formula, because no source read says so and the KPI dashboard's own Metric Definitions section
does that job; this layering is this library's own position, stated here as a position rather than as any
source's claim, and a source saying otherwise would reopen it.

**Tracking plan vs Kaushik's Digital Marketing and Measurement Model - a boundary, not a sibling.**
Kaushik's own model is "a simple, structured, five step process" [[26]](#ref-26) that moves from business
objectives to key performance indicators to segments; nowhere in the page read for this bundle does it
name an event or a property. This companion does not treat it as a tracking plan or as this artifact's
ancestor, and names it here only to rule it out as a neighbor a reader might otherwise expect to find.

**Tracking plan vs the change log - a different subject entirely, despite the shared word "change."**
The tracking plan's own Change Process and Version History section, sourced in section 3 above, records
changes to the plan itself: which event was added, renamed, or removed, and who approved it
[[10]](#ref-10)[[15]](#ref-15)[[17]](#ref-17). The `change-log` instead records requested and decided
changes to a project's agreed baseline, a scope, cost, or schedule decision with its own requester and
decision date. The two logs share a verb and nothing else; a request to add a new event belongs in the
tracking plan's own version history, not in the project's change log, unless that event is itself tied to
a baseline change the project is tracking.

**Tracking plan vs the risk register and the RAID log.** Neither register's own research names a tracking
plan among its contents, and this bundle's own research names no risk or open item specific to the
tracking plan beyond what section 7 already states as a named failure mode. Where a tracking-plan failure
becomes a tracked risk, for instance an unowned event drifting silently, this bundle reads that risk as
belonging in the risk register or the RAID log's own Risks quadrant, not duplicated inside the tracking
plan.

**Tracking plan vs the issue log.** A tracking-plan event that silently stops firing, or starts carrying
the wrong value, is a realized problem once it is noticed, and this bundle reads that problem as an
`issue-log` row with its own owner, next action, and confirmed close, rather than a status the tracking
plan's own catalog is built to carry on its own. The catalog's status column, sourced in section 3,
records whether an event is still live; it does not replace a named problem's own tracking.

**Tracking plan vs the live, enforced schema in a tool.** This bundle is the specification; Avo, Twilio
Segment Protocols, and mParticle's Data Plan are implementations that validate against it or generate code
from it [[1]](#ref-1)[[4]](#ref-4)[[12]](#ref-12)[[13]](#ref-13). Reading the document as upstream of the
enforced schema is this library's own position, following section 1's scope statement; no vendor source
read states that ordering in those words.

---

## 9. Adaptations

- **Early-stage / small event set.** The lean variant, a spreadsheet or document medium, and a small,
  hand-picked set of events are all the research supports for this case [[28]](#ref-28)[[29]](#ref-29)[[30]](#ref-30).
- **Multi-platform product.** The Naming Conventions section's cross-platform ASK exists specifically for
  this case: one engineering handbook names the exact failure a plan without it invites, "the screen names
  differ per platform, which makes it hard to actually use the data." [[27]](#ref-27).
- **Several teams changing the same plan.** The full variant's Change Process section, with Avo's
  branch-and-review mechanism [[22]](#ref-22)[[23]](#ref-23)[[24]](#ref-24) or Amplitude's three-role
  approval chain [[10]](#ref-10), is sized for this case.
- **Personal or sensitive data in scope.** The full variant's Privacy, Sensitivity and Retention section,
  with Mozilla's per-metric sensitivity and expiry fields [[36]](#ref-36) and its consent-by-category
  policy [[37]](#ref-37), is sized for this case; the section gives shapes, not legal advice, and a team in
  a regulated setting should have that advice checked separately.
- **Engineering-led review discipline.** GitLab's issue-gated instrumentation process [[35]](#ref-35) and
  its own multi-step removal procedure [[34]](#ref-34) are the sourced model for a team that wants the
  Change Process section enforced as strictly as a code review.

---

## 10. Worked example

`tracking-plan_example.md` is the worked instance for this bundle, and it chains onto the same Acme
Analytics Reporting Platform Modernization program the library's other governance-docs examples share.
The research log fixes a small set of facts the example must carry exactly, rather than invent: the five
Saved Views events (`view_saved`, `view_switched`, `view_set_default`, `view_shared`, and
`view_load_error`, each carrying a dashboard ID and view scope), the experiment's exposure event
`nudge_variant_assigned`, the Time to Insight metric's proxied actions, export, share, and annotate, the
owners the KPI dashboard's own example already names, and Amplitude as the destination product events
land in. Its `last_reviewed` date is fixed at 2026-08-24, placed after every sibling example that date
constrains and before the experiment it references concludes. Everything else about the filled document,
including its size variant and any owner assignment the research log does not itself fix, is the example
stage's own decision, to be stated there as a decision rather than read back into this companion.

---

## References

<a id="ref-1"></a>[1] Avo. "[The Avo Tracking Plan](https://www.avo.app/docs/data-design/avo-tracking-plan)."
avo.app (accessed 2026-10-11). The in-tool tracking plan as the surface used to generate code from and
validate data against ("The Avo Tracking Plan is where you define the data for your application. It
contains detailed definitions of your tracking plan that can be used to generate code from and validate
your data against."). [vendor]

<a id="ref-2"></a>[2] Avo. "[Data Design index, 'What is a Tracking Plan?'](https://www.avo.app/docs/data-design)."
avo.app (accessed 2026-10-11). The one-sentence definition and the instruction to summarize each event and
property's reason for being tracked ("A tracking plan is a document that defines the key stages of your
customer life cycle and codifies a single source of truth for the data that supports it."). [vendor]

<a id="ref-3"></a>[3] Thora Gudfinnsdottir (Avo). "[Avo's Ultimate Tracking Plan Template (w/ Downloadable Worksheet)](https://www.avo.app/blog/avos-ultimate-tracking-plan-template-w-downloadable-worksheet)."
avo.app blog (accessed 2026-10-11). All ten worksheet columns, read verbatim as numbered headings, and the
instruction to hold one tense and one capitalization across event names. [vendor]

<a id="ref-4"></a>[4] Twilio Segment. "[Create a Tracking Plan](https://segment.com/docs/protocols/tracking-plan/create/)."
segment.com (accessed 2026-10-11). The in-tool schema that validates live events against the plan, the
Identify/Group trait-editing flow, and the exact-match naming rule ("Casing, spacing and spelling
matter."). [vendor]

<a id="ref-6"></a>[6] Twilio/Segment editorial. "[What is a tracking plan](https://www.twilio.com/en-us/blog/insights/what-is-a-tracking-plan/)."
twilio.com blog (accessed 2026-10-11). The one-sentence definition, the four worked-example columns (NAME,
PROPERTIES, LOCATION, WHY) read verbatim, and the statement that plans are living documents whose
convention varies by team. [vendor]

<a id="ref-7"></a>[7] Twilio Segment. "[Glossary](https://www.twilio.com/docs/segment/glossary)."
twilio.com (accessed 2026-10-11). The object/trait distinction: an object persists and its traits can
change over time, apart from any event. [vendor]

<a id="ref-8"></a>[8] Amplitude. "[Create a tracking plan](https://amplitude.com/docs/data/create-tracking-plan)."
amplitude.com (accessed 2026-10-11). The governing one-sentence definition, the instruction to build the
plan before instrumenting code, and the user-property/group-property field split. [vendor]

<a id="ref-9"></a>[9] Arpit Choudhury (Amplitude). "[How to create a tracking plan?](https://amplitude.com/blog/create-tracking-plan)."
amplitude.com blog, originally published 2022-06-07, updated 2024-11-15 (accessed 2026-10-11). The
living-document and source-of-truth language, the owner-via-source-field instruction, and the Google
Sheets template's named tabs (template file itself not opened). [vendor]

<a id="ref-10"></a>[10] Amplitude. "[What Is Event Taxonomy: Complete Definition & Framework](https://amplitude.com/explore/data/event-taxonomy)."
amplitude.com (accessed 2026-10-11). The requester/steward/domain-owner approval chain, the
proposed/active/deprecated/removed version-label vocabulary, and the instruction to document what
changed, when, why, and who approved it. [vendor]

<a id="ref-11"></a>[11] Mixpanel. "[Create A Tracking Plan](https://docs.mixpanel.com/docs/tracking-best-practices/tracking-plan)."
docs.mixpanel.com (accessed 2026-10-11). The living, centralized-document framing and the names of the
four vertical templates plus one blank template it links (template contents not opened). [vendor]

<a id="ref-12"></a>[12] mParticle. "[What is a data plan, and why is it important to have one?](https://www.mparticle.com/blog/data-tracking-plan-engineers/)"
mparticle.com blog (accessed 2026-10-11). The document-form definition, the document-versus-in-tool
distinction, and the statement that a plan without implemented tracking code is "just another document."
[vendor]

<a id="ref-13"></a>[13] mParticle. "[Data planning](https://docs.mparticle.com/guides/platform-guide/data-planning/)."
docs.mparticle.com (accessed 2026-10-11). The in-tool Data Plan's component fields (event, user attributes,
or user identities) and the named industry templates it ships (names only; contents not opened). [vendor]

<a id="ref-14"></a>[14] Countly. "[Tracking plan](https://countly.com/glossary/tracking-plan)."
countly.com glossary (accessed 2026-10-11). The one-sentence definition, the field list ("naming
conventions, data types, allowed values, triggering conditions, examples, sensitivity, retention, and
validation"), and the versioned-and-reviewed-on-change framing. [vendor]

<a id="ref-15"></a>[15] RudderStack. "[Getting Started with Tracking plans](https://www.rudderstack.com/knowledge-base/get-started-with-tracking-plans/)."
rudderstack.com knowledge base (accessed 2026-10-11). The versioning mechanism and the sprint-paced,
iterative framing of plan maintenance. [vendor]

<a id="ref-17"></a>[17] Snowplow. "[Tracking plans](https://docs.snowplow.io/docs/fundamentals/tracking-plans/)."
docs.snowplow.io (accessed 2026-10-11). The named owner, the consumers/subscribers roles, and the
change-history element, each stated as part of what a tracking plan carries at its core. [vendor]

<a id="ref-19"></a>[19] Digital Applied Team. "[Product Analytics: An Event Taxonomy That Won't Rot](https://www.digitalapplied.com/blog/product-analytics-event-taxonomy-tracking-plan-2026)."
digitalapplied.com (accessed 2026-10-11). The owner-departure decay vector, quoted in full; the names
(without further description) of five further decay vectors; and the reported, unverified claim that
Mixpanel's Data Standards feature "launched Apr 16, 2025". [practitioner]

<a id="ref-20"></a>[20] Patrik Chalupa (CustomerScore). "[Event Tracking Plan for SaaS: A Phase-One Blueprint](https://www.customerscore.io/blog/event-tracking-plan-saas)."
customerscore.io (accessed 2026-10-11). The named-person-per-event ownership rule, the pii_flag column and
its masking effect, the ninety-day audit cadence (attributed onward to House of MarTech), and the "wrong
within 60 days of shipping" claim, stated as this author's own. [practitioner]

<a id="ref-21"></a>[21] David Pombar (Trackingplan). "[Data Governance for Analytics: A Practical Guide to Trusted Data](https://www.trackingplan.com/blog/data-governance-for-analytics)."
trackingplan.com (accessed 2026-10-11). The data-owner-versus-data-steward distinction, the PII-leak
monitoring framing, and the "one-and-done" governance anti-pattern. [vendor]

<a id="ref-22"></a>[22] Avo. "[1. Plan analytics update in Avo branch](https://www.avo.app/docs/workflow/plan)."
avo.app (accessed 2026-10-11). The branch-based proposal mechanism, isolated from the plan's main branch
until reviewed. [vendor]

<a id="ref-23"></a>[23] Avo. "[Quickstart: Branches](https://www.avo.app/docs/data-design/branches)."
avo.app (accessed 2026-10-11). The branch lifecycle states (Draft, Ready for Review, Approved, Changes
Requested), the review-and-assign step, and the recommended one-to-one mapping to git branches. [vendor]

<a id="ref-24"></a>[24] Avo. "[Using Avo in large development teams with parallel workflows](https://www.avo.app/docs/implementation/guides/avo-and-git)."
avo.app (accessed 2026-10-11). The full branch-and-merge sequence alongside a matching code change, and
the guarantee that previously merged branches remain viewable, with what changed, when, and by whom.
[vendor]

<a id="ref-25"></a>[25] John Cook (Heap). "[Why Heap Isn't Built on a Manual Tracking Foundation](https://www.heap.io/blog/why-heap-isnt-built-on-a-manual-tracking-foundation)."
heap.io (accessed 2026-10-11). The autocapture position, the explicit statement that autocapture-versus-a-plan
is "a false choice", and the characterization of a spreadsheet-managed plan as fragile at scale. [vendor]

<a id="ref-26"></a>[26] Avinash Kaushik. "[Digital Marketing and Measurement Model](https://www.kaushik.net/avinash/digital-marketing-and-measurement-model/)."
kaushik.net, Occam's Razor (accessed 2026-10-11). The five-step business-objectives-to-segments model,
read here only to confirm it never names an event or a tracking plan; it is not treated as this artifact's
ancestor. [practitioner]

<a id="ref-27"></a>[27] Nimble. "[Event Tracking Guidelines](https://nimblehq.co/compass/product/analytics/event-tracking-guidelines/)."
nimblehq.co, Compass engineering handbook (accessed 2026-10-11). The object-then-past-tense-action naming
report and the snake_case casing rule, both attributed to this handbook rather than to Segment directly;
the cross-platform screen-name inconsistency named as a problem. [practitioner]

<a id="ref-28"></a>[28] DataTalks.Club. "[Tracking Plans](https://datatalks.club/podwiki/wiki/tracking-plans/)."
datatalks.club, Podcast Wiki (accessed 2026-10-11). The spreadsheet-as-acceptable-starting-medium framing
for a small event set, and the statement that ownership is part of the plan's own definition. [practitioner]

<a id="ref-29"></a>[29] Tag Insight. "[Designing your tracking plan](https://docs.taginsight.com/best-practices/tracking-plan-design)."
docs.taginsight.com (accessed 2026-10-11). The phased, start-with-business-essentials build-out argument
and the self-labeled, internally inconsistent "Action_object pattern". [vendor]

<a id="ref-30"></a>[30] Mila (Data Club). "[How to get the most out of your Product Analytics with Naming Conventions](https://dataclub.substack.com/p/how-to-get-the-most-out-of-your-product)."
dataclub.substack.com, published by the Wunderbar Network (accessed 2026-10-11). The object+action,
past-tense naming recommendation, the explicit refusal to pick a single casing style, and the
spreadsheet-or-whiteboard setup framing. [practitioner]

<a id="ref-31"></a>[31] Wizbrand. "[Data Dictionary: What It Is, Key Features, Benefits, Use Cases, and How It Fits in Analytics](https://www.wizbrand.com/tutorials/data-dictionary/)."
wizbrand.com (accessed 2026-10-11). The forward-looking-intent-versus-implemented-structure distinction
between a tracking plan and a data dictionary, and the stated relationship between the two. [vendor]

<a id="ref-32"></a>[32] Wizbrand. "[Analytics Measurement Plan](https://www.wizbrand.com/tutorials/analytics-measurement-plan/)."
wizbrand.com (accessed 2026-10-11). The containment relationship between a tracking plan and a broader
measurement plan, "the measurement plan explains why you track; the tracking plan explains how." [vendor]

<a id="ref-33"></a>[33] GitLab. "[Event definition guide](https://docs.gitlab.com/development/internal_analytics/internal_event_instrumentation/event_definition_guide/)."
docs.gitlab.com (accessed 2026-10-11). The constraint that every additional property must carry its own
description, and the lowercase-numbers-and-underscores constraint on the event name field itself; the
naming pattern is described in this log's own words because the cached page escapes the characters a
verbatim quote would need. [practitioner]

<a id="ref-34"></a>[34] GitLab. "[Event lifecycle](https://docs.gitlab.com/development/internal_analytics/internal_event_instrumentation/event_lifecycle/)."
docs.gitlab.com (accessed 2026-10-11). The five-step, auditable removal procedure, including setting the
status field to removed and recording the removing merge request's URL. [practitioner]

<a id="ref-35"></a>[35] GitLab. "[Data For Product Managers](https://handbook.gitlab.com/handbook/enterprise-data/organization/programs/data-for-product-managers/)."
handbook.gitlab.com (accessed 2026-10-11). The product-manager-authored instrumentation issue, the
engineer's implementation and peer-reviewed validation step, and the instruction to determine what to
measure before writing the issue. [practitioner]

<a id="ref-36"></a>[36] Mozilla. "[Telemetry - Implementation, Reviews, Renewals](https://firefox-source-docs.mozilla.org/mobile/android/fenix/Telemetry-implementation,-reviews,-renewals.html)."
firefox-source-docs.mozilla.org (accessed 2026-10-11). The mandatory data-review gate on every telemetry
patch, and the per-metric data_sensitivity and expires fields. [practitioner]

<a id="ref-37"></a>[37] Mozilla. "[Data Collection](https://wiki.mozilla.org/Data_Collection)."
wiki.mozilla.org (accessed 2026-10-11). The data-requester/data-steward roles, the per-request retention
duration on the request form itself, the consent-by-category policy, and the annual survey of every
existing data collection. [practitioner]
