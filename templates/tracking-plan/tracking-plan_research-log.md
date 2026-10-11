# tracking-plan: research log

Research conducted 2026-10-11, building on an admission sweep run on 2026-10-05 while the spec was written (five
measurement candidates, one of them this one). The build's six-dimension fan-out covered the vendor canon in two
parts (Avo and Twilio Segment; Amplitude, Mixpanel, mParticle and Countly), cadence, ownership, versioning and
privacy, contested practice, the boundaries with this library's neighbours and the worked example's facts, and the
standing gap question. **37 sources are recorded below, all fetched-and-verified.** Only `fetched-and-verified`
sources are quoted anywhere in this bundle.

**Every quotation in this log was checked against the source's raw text**, not against the summary a retrieval tool
returns. The agents returned 228 quotations. 193 passed as normalized substrings and 19 more pass once a rendering
artifact is removed, such as a space before punctuation where a link closed. Of the other 16, eight were list items or
table rows an agent had joined with slashes or pipes; each part was checked on its own, and the parts are quoted
separately below. Five sat across an HTML entity in the cached download (an escaped angle bracket, quotation mark or
apostrophe) or an inserted link label; they are quoted below in their verbatim parts or dropped. One fused a heading
onto the sentence beneath it and survives as the sentence. One is a three-letter template name too short for the
checker, confirmed by reading the page, and one passes with whitespace ignored. Every page first cached during this build was fetched a
second time with the cache bypassed: 37 of 38 quotations re-checked that way pass, and the one that does not is the
fused heading just described. Dashes inside quotations are written as hyphens, as the house rule requires.

---

## What the checks caught, and what was not read

**All ten of Avo's worksheet columns are now read verbatim.** The spec recorded five of the ten as raw-checked and the
other five as read from page prose. [3] carries all ten as numbered headings: "1. KPIs" through "10. Code snippet".

**Twilio Segment's fourth column is WHY, and it is read verbatim.** The spec described "a fourth column whose name
did not pass the raw-text check". The headers sit in an image, but [6]'s prose names all four: the events and
properties are logged "in the NAME and PROPERTIES columns above", the where is "logged under LOCATION", and the why
"(logged under WHY) is a short description of the business purpose that justifies tracking the event."

**Amplitude links one template, not a template set.** The spec carried "a four-sheet Google
Sheets template plus five vertical taxonomy templates" as summary-derived. [9] links one Google Sheets template ("The tracking plan template below is a Google Sheets
spreadsheet") and names its sheets in prose: Events and Event Properties, User Properties, Organization (Group)
Properties, and Discussions. No vertical taxonomy templates appear on the page read. The spec needs a dated note at
landing. The sheet itself was not opened.

**Mixpanel names its templates; their contents were not read.** [11] lists four vertical templates by name ("Retail and
E-commerce", "Media and Entertainment", "SaaS", "Financial Services") and a blank one, which matches the spec's count of
five. [13] lists seven named mParticle industry templates. No template file was opened, so this bundle says nothing
about what any of them contains.

**The event status vocabulary is on Amplitude's own page, not only a practitioner's.** The spec treated a status or
lifecycle value as single-sourced. [10], Amplitude's own event-taxonomy page, reads: "Track all taxonomy changes with
version labels like "proposed," "active," "deprecated," and "removed."" [8] gives each event "The active or inactive
status of the event", [3] carries a "9. Status" column, and [33] and [34] give GitLab's events a status field with a
"removed" value. Status is now convergent, and the template carries it as a column without a single-source label.

**A per-event owner is no longer single-sourced either.** The spec sourced the owner column to one practitioner. [9]
names an owner per event ("the person responsible for the implementation of that event"), [10] asks for documentation
"listing every event, property, data type, and owner", [14] names owners among a plan's contents, and [20] argues the
strictest form ("owner: a named person, not a team."). Who owns the plan as a whole is a separate question; see
contested item 5.

**Snowplow's tracking-design URL now serves a different page.** The URL the spec cites for Snowplow's tracking design
returns a page titled "Event Studio" ([18]). It is cited under that title, and only for the three capabilities it lists.

**One source was owned twice.** Two dimensions both read Nimble's public engineering handbook. It has one entry, [27],
carrying both dimensions' verified extracts.

**Two cached pages escape characters a quotation needs.** GitLab's event-definition page ([33]) and Nimble's handbook
([27]) carry their naming patterns inside escaped angle brackets in the cached download, and GitLab's handbook ([35])
escapes an apostrophe. The naming patterns are therefore described in this log's own words, not quoted; both read on
the live pages as an object followed by an action in the past tense (Nimble) and an operation, its target and where or
when it happened (GitLab).

**What was not read.** Avo's "Tagging PII" page and its naming-conventions page appear in its navigation but were not
opened. Twilio Segment's own object-action naming spec was found and not read; [27] and [30] attribute the convention to
Segment, and this bundle attributes it to them, not to Segment. The UK Information Commissioner's cookie guidance
returned no body text, so this bundle cites no regulator on consent. Three vendor pages on resolving anonymous and known
users were found by search and not read, and Mixpanel's event-approval page was named and not read. None of the vendor
spreadsheets was opened. No source was read that states a review interval for a whole tracking plan other than [20]'s
90 days and [37]'s annual survey.

---

## The admission record

**[ADR 0030](../../docs/internal/decisions/0030-templating-scope-markdown-documents.md)'s test is met by several named
vendors.** One named source publishing the type as a written document is enough. [2] defines it as "a document that
defines the key stages of your customer life cycle and codifies a single source of truth for the data that supports
it." [6] calls it "a document or spreadsheet used across an organization to standardize how it tracks data." [9] calls
it "a document that acts as a source of truth for your event data", and [12] "a document that keeps different teams
aligned on the key information regarding your organization's data collection and analysis efforts." [3], [9] and [11]
ship or link spreadsheet templates.

**The family is `governance-docs`, `classification: utility`, by
[ADR 0067](../../docs/internal/decisions/0067-tracking-plan-joins-governance-docs-as-a-sixth-member.md).** Nothing read
here contradicts it. Every source that speaks to cadence describes a document kept for the product's life: [9] "it's a
living document", [11] "continuously updated with any implementation changes", [14] "versioned and reviewed whenever the
product or measurement strategy changes", and [15] "an iterative process and a part of every sprint".

**Scope: the document is in scope, the enforced schema is not.** Several vendors keep the plan inside their product as
well as in a document. [1] is "where you define the data for your application" and is used to "generate code from and
validate your data against"; [4] validates live events and reports "Violations"; [13] calls its in-tool plan "a codified
set of expectations". The written form remains named and published alongside: [7] "It's often in a spreadsheet or
document", [12] "can exist as a static document like a spreadsheet, or it can live within a data software solution",
and [28] "Teams can start with a spreadsheet or document when the event set is small." Reading the document as upstream
and the enforced schema as derived from it is this library's own POSITION, as the spec records; no vendor states that
ordering in those words.

**Licences decide what this bundle may adapt.** No page read states a content licence for its tracking-plan template or
column list. Twilio's pages carry "Copyright © 2026 Twilio Inc.", Amplitude's "All rights reserved", and the others a
site footer or nothing. This bundle quotes briefly and adapts no vendor's column list; its catalog table synthesizes the
fields the vendors share.

---

## Claims flagged contested or time-bound

1. **Where the plan lives: a document, a spreadsheet, or the tool.** [25], a vendor arguing for its own product, calls
   the spreadsheet fragile ("If you've ever tried to manage a spreadsheet at scale, you know how easily things can
   break."). [28] and [30] treat a spreadsheet as a normal start ([30]: "Setup: Use a spreadsheet, Miro board, paper or
   whiteboard."). [1] makes the in-tool plan primary; [4] validates against a spec that can be imported from a file; [12]
   accepts either. The bundle templates the document and names the tool as where it may later be enforced.
2. **How often the plan is reviewed.** [20] states a 90-day audit and attributes the cadence to another firm ("The 90-day
   audit rule from House of MarTech is the right cadence."). [21], a monitoring vendor, rejects fixed intervals ("Manual
   spot-checks and quarterly audits feel like relics from a different era."). [37] runs an annual survey of every
   collection. [14] ties review to change ("whenever the product or measurement strategy changes"). No interval is a
   convention; the template asks the author to choose one and name what else triggers a review.
3. **Event naming.** [3] wants one tense and one capitalization; [27] and [30] recommend an object followed by a
   past-tense action ([30]: "I recommend using the object+action framework"); [33] uses an operation, its target and
   where or when. [29] labels its own pattern "Action_object pattern" while its examples run object first, which this
   log reads as an inconsistency in [29], not a second convention. Casing is contested outright: [27] requires snake
   case, and [30] declines to choose ("Choose one case and stick with it."). The template asks for a convention and
   picks none.
4. **Autocapture against a designed plan.** [25] is the only source on the autocapture side, and it does not say a plan
   is unnecessary: it calls the choice between autocapture and precision tracking "a false choice", and it advises teams
   to "manually capture 5-10 core KPIs". Every other source assumes a designed plan, and [8] says to build it first ("Build one before you
   instrument code"). [29] argues for scope in phases ("Don't try to track everything at once."), which is about how
   much to plan first, not whether to plan.
5. **Who owns what.** [20] wants one named person per event and rejects team ownership in so many words ("means nobody
   owns it."). [10] and [19] describe a chain of roles (requester, steward, owner, and in [19] implementer); [37]
   names a "Data requester" and a "Data steward"; [35] gives creation to the product manager and validation to an
   engineer; [17] gives each plan, split by domain, "an explicit owner". These answer different questions (an event's
   owner, the plan's owner, the approval path) and are compatible; the template keeps them apart.
6. **"Event taxonomy" or "tracking plan".** [10] uses "event taxonomy" for the naming and categorizing system and asks
   for "central documentation" of it; [8] and [9] use "tracking plan" for the catalog. Amplitude does not say whether
   they are one document. This bundle treats the taxonomy as the naming convention a tracking plan states.
7. **Time-bound figures and vendor claims.** [19] is dated 2026 and reports Mixpanel's Data Standards as "launched Apr
   16, 2025"; [19]'s "10-200 events" ceiling and its claim that "The most common tracking-plan failure mode is not
   technical" are its own, not measured. [20]'s "wrong within 60 days of shipping" is one practitioner's view.

---

## Notes for the companion

### Honest framing

A tracking plan is the standing catalog of the analytics events a product records, the properties each carries, and
the user and account traits it keeps, with why each is collected, when it fires, where it comes from, who owns it and
whether it is still live. [8] puts the job in one sentence: "A tracking plan defines every event and property you
collect, why you collect each one, and which source emits it." [14] says what it does across teams: "It translates
product questions into an implementation contract for product, engineering, analytics, privacy, and marketing teams."

The vendors agree on a core and disagree at the edges. The core: a list of events with a description or reason,
their properties and types, where each comes from, and a status. Past the core they differ on where the plan lives
(contested item 1), how often it is reviewed (item 2), how events are named (item 3) and who owns what (item 5). Every
admitting source is a product-analytics vendor, and most of them sell the tool the plan is enforced in, so the bundle
says so and does not present a vendor's case for its product as a finding.

**No source measured whether keeping a tracking plan improves data quality or decisions.** [19]'s failure taxonomy and
[20]'s "60 days" are practitioners' testimony. The companion says the case for the document rests on that testimony
and on the failure modes it names, not on a measurement.

### The evidentiary spine, section by section

The research moves the spec's provisional section design in three places, and the companion should say so: the user
and account traits get a section of their own, the naming convention gets a short section, and the spec's
"Governance and Ownership Discipline" splits into a privacy section and a change-process section, because the owner
column it carried is now convergent and belongs in the catalog.

- **Purpose and Boundary** (lean). What the plan covers, product-wide, and what does not go in it: one feature's
  instrumentation slice (the PRD's Analytics and instrumentation section), a data dictionary ([31]: "A Data Dictionary
  documents what the data means and how it is structured once implemented."), the KPI dashboard's metric definitions,
  and the enforced schema in a tool. [31] gives the forward-looking line: "A tracking plan describes what you intend to
  track (events, triggers, parameters) and why." [32] places it inside a broader measurement plan: "the measurement plan
  explains why you track; the tracking plan explains how."
- **Naming Conventions** (lean, short). The rule the catalog's names follow. [14] "A strong plan defines naming
  conventions"; [12] asks "What names will you give to specific events/event categories?"; [3] "each of your events
  should be named in a consistent way that's in line with your agreed-on naming schema"; [4] "Casing, spacing and
  spelling matter." The forms are contested item 3, so the section asks for a convention and picks none.
- **Event and Property Catalog** (lean, the load-bearing table). One row per event. The columns the sources share:
  - the event name;
  - when it fires: [14] "triggering conditions" and "when it fires", [6]'s LOCATION ("the location and time at which
    the event is being tracked"), and [2] "Explain the location in the codebase";
  - why it is collected, or the question it answers: [6]'s WHY, [2] "Summarize the reason for tracking each event and
    property", [3]'s "1. KPIs", and [20]'s test that an event whose KPI cannot be named does not ship;
  - its properties, with type and allowed values: [3] "7. Property value types", [4] "Permitted Values", [8] "A name,
    description, examples, and rules define each property.", [9] "data types, expected values";
  - where it comes from and goes to: [8] "which source emits it", [9] "data destinations", [3] "8. Platforms";
  - its owner: see the owner note above;
  - its status: see the status note above.
  A table section, so it carries PRIORITY and ROW HINT.
- **User and Account Properties** (lean, a table). The traits kept about a user or an account, apart from events. Five
  vendors separate them: [4] defines traits for "Identify or Group calls" on their own tab; [7] "Objects persist over
  time, so traits can change over time."; [8] "User properties capture traits about the user." and "Group properties";
  [9]'s "User Properties" and "Organization (Group) Properties" sheets; [11] "user profile properties"; [13] "user
  attributes, or user identities". The catalog's own purpose names "user traits" (spec, catalog 140).
- **Privacy, Sensitivity and Retention** (full). [14] lists "sensitivity, retention, and validation" among a strong
  plan's contents; [20] makes "pii_flag" a column that "routes the event through masking or exclusion pipelines"; [21]
  requires "strict controls to prevent the accidental collection of Personally Identifiable Information (PII)"; [36]
  attaches "data_sensitivity:" and "expires:" to each metric; [37] scales consent with sensitivity ("Any collection
  requires prior Trust approval and (i) advance user notice (ii) consent and (iii) an opt-out.") and asks at request time
  "for how long it will be collected". Thinly and differently sourced; the section presents the shapes and lets the
  author choose. No regulator was read, so the bundle gives no legal advice.
- **Review and Ownership** (lean). Who keeps the plan, how often it is reviewed, and what else triggers a review. The
  plan's owner: [17] "An explicit owner; that is responsible for maintaining and updating the data over time". The
  interval is contested item 2: the section asks for one and states none as a norm.
- **Change Process and Version History** (full). How a change is proposed, reviewed and recorded. Proposal against the
  standing plan: [22] "A branch allows you to draft changes to the tracking plan in isolation, without impacting the main
  branch, which contains the single source of truth of what's currently being tracked."; [24]'s sequence ("Get a
  peer-review and approval on the changes", "Merge the Avo branch"); [20]'s steps ("Propose the change in the
  source-of-truth document (Google Sheet, Notion, or Git repo).", "Update the schema and bump plan_version."). The
  approval path: [10]'s three roles ("Event requesters propose new events with clear use cases", "Data stewards review
  naming and check for duplicates", "Domain owners approve events within their product areas"), [37]'s requester and
  steward. The record: [17]'s "Change history; a complete audit log of the changes", [10] "Document what changed, when,
  why, and who approved it.", [15] "Tracking plans support versioning". Removal as a procedure: [34]'s steps, including
  setting "the status field to removed". Validation before an event ships: [35]'s "Verify test events match properties
  defined in the Issue", [36] "Data reviews are needed on all patches that add new telemetry or modify existing
  telemetry."

**Frontmatter, not a section:** the plan's owner, its data steward, the products or sources it covers, its version and
its last-reviewed date ([17], [15], [10]).

**Sizes.** `[lean, full]`, lean the default. Lean is for a product starting out or a small event set: [28] "Teams can
start with a spreadsheet or document when the event set is small.", [29] "Build your tracking in phases", and [6]'s
four-column worked example. Full adds privacy and the change process, for a plan that several teams change, that holds
personal data, or that someone will later ask what changed and who approved it ([10], [17], [37]). Avo's ten columns
([3]) and Countly's list ([14]) show the fuller weight.

**When not to keep one, for the guide.** No source argues against keeping a tracking plan. [25] argues that capture can
come first, with a short list of hand-picked events; the guide states that view as [25]'s and routes a team with no
events yet to the PRD's own section for its first feature. A feature's one-time slice belongs in the PRD; the plan is
what every feature's slice merges into ([22], [24], read as the spec's POSITION).

### The gap question's result, and what this build does with it

Dimension 6 searched for what a good tracking plan does beyond the commonest columns, without reading the bundle.
Each candidate went through
[decision procedure 12](../../docs/internal/decision-procedures.md#12-a-property-or-section-is-proposed-for-a-template).

- **Validation before an event ships: adopted in Change Process and Version History, full.** E1: [35], [36], and [14]'s
  "test cases". E3: it is a step in how a change reaches the plan.
- **Removal as a procedure, not a status flip: adopted in the same section, full.** E1: [34], [10], [19]. E3: removal is
  a change.
- **The question each event answers: adopted as a catalog column, lean.** E1: [35], [6], [2], [20]. E4: one cell per
  row.
- **Who may request an event, and who approves it: adopted in Change Process, full.** E1: [37], [35], [10], [28].
- **Consent, sensitivity and retention per event: adopted in Privacy, Sensitivity and Retention, full.** E1: [37], [36],
  [14], [20]. The section warns that consent rules are legal questions the bundle does not answer.
- **Cross-platform consistency: adopted as an ASK in Naming Conventions.** E1: [27] ("the screen names differ per
  platform, which makes it hard to actually use the data").
- **An annual re-justification of every collection: adopted as an ASK in Review and Ownership, full.** E1: [37].
- **The identity model (anonymous and known users): null result.** No source read in full describes it as part of a
  tracking plan; three vendor pages were found and not read. The User and Account Properties section names identities
  only as [13] does.
- **Environments (development against production) per event: null result.** No source read describes a per-event
  environment field.
- **Property constraints beyond type: folded into the catalog's properties column.** [4]'s "Permitted Values" and [8]'s
  rules ("Min Length, Max Length, and Regex") are the evidence; no source read gives a required-or-optional flag.

### What the bundle must not say

- That any vendor licenses its template or column list. None states one.
- Any vendor's column list reproduced as the template.
- That Amplitude ships five vertical taxonomy templates, or what any vendor's spreadsheet contains.
- "instrumentation plan" or "analytics spec" as vendor terms. Neither was found; [4] says "data spec".
- That a review interval is a convention. 90 days is [20]'s, attributed onward to House of MarTech; annual is [37]'s.
- [19]'s "10-200 events" or its "most common" failure claim as measured facts; [20]'s "60 days" as anyone's but [20]'s.
- That autocapture makes a plan unnecessary. [25] itself calls the choice false.
- [29]'s "Action_object pattern" label as a convention.
- That Kaushik's model ([26]) is a tracking plan. It names business objectives, KPIs and segments, and never events.
- That a vendor says the document is upstream of the tool. It is the library's POSITION.
- That a tracking plan defines or locks a metric's formula. No source says so, and the KPI dashboard's Metric
  Definitions section does that job; the layering is the library's POSITION, and a source saying otherwise would
  reopen it.
- That writing a tracking plan improves data quality, as a measured result.
- Legal advice on consent or retention.
- Any gendered pronoun for a source author. Use the author's name.

### GOOD and WEAK illustrations use their own scenario

Every GOOD and WEAK example in the templates' guidance comments uses a scenario unrelated to the worked example: not Acme
Analytics, not the Reporting Platform Modernization program, not Saved Views, not dashboards, views or reports, and none
of Priya Nair, Dana Osei, Dana Okoro, Lee Zhang or Marta Reyes. Two earlier builds shipped GOOD text in the worked
example's own scenario (`announcement-internal-comms` and `change-request`, caught after every review lens had passed).

### The example

The tracking plan for **Acme Analytics' Reporting product**, kept by the Reporting Platform Modernization program,
dated within the Saved Views adoption-nudge experiment's run. A `last_reviewed` date of **2026-08-24** sits after every
other `governance-docs` example (the latest is `change-log_example.md:6`, 2026-08-17), after the 2.4.0 release on
2026-07-21, after the experiment design doc (2026-07-30), and before the experiment ends (2026-08-31) and its readout
(2026-09-04), so the plan can list the experiment's exposure event as live without knowing the result. That date is
this log's recommendation, not a sibling's fact; the example states it plainly.

It must carry these facts from its siblings, exactly, and invent none of them:

| Fact | Value | Source |
|---|---|---|
| The five Saved Views events | `view_saved`, `view_switched`, `view_set_default`, `view_shared`, `view_load_error` (with reason), "each with dashboard ID and view scope" | `templates/prd/prd_example.md:133-134` |
| Saved Views release | 2.4.0, "Release date: 2026-07-21."; no Saved Views event is live before it | `templates/release-notes/release-notes_example.md:26` |
| The experiment's exposure event | `nudge_variant_assigned`, "firing the moment an eligible account crosses its fifth dashboard view, carrying the variant id and the account id as properties"; checked in staging 2026-07-29; the test runs 2026-08-03 through 2026-08-31 | `templates/experiment-design-doc/experiment-design-doc_example.md:120-125`, `:7-9` |
| Time to Insight's proxy actions | "'action' is proxied by a set of logged events (export, share, annotate)"; the formula uses "timestamp the report was opened" and "timestamp of first logged action on a report" | `templates/kpi-dashboard/kpi-dashboard_example.md:63-70` |
| Metrics, owners and steward | Time to Insight, Saved Views adoption and Weekly active analysts owned by Priya Nair; View-list load (p95) owned by Dana Osei; data steward Lee Zhang (Data Eng) | `templates/kpi-dashboard/kpi-dashboard_example.md:53-57`, `:59-103` |
| Where product events land | "Amplitude for product events, Looker for the executive view" | `templates/kpi-dashboard/kpi-dashboard_example.md:42-43` |
| Two different people | Dana Osei (Staff Engineer, Platform; View-list load) is not Dana Okoro (VP Product; KR3) | `kpi-dashboard_example.md:55`; `okrs_example.md:3,53` |

**What the example decides, and must say it decided.** No sibling names an owner for an individual event, and the KPI
dashboard names its proxy actions but not their event identifiers. The example assigns per-event owners (a defensible
choice: Priya Nair for the events behind the metrics Priya Nair owns, Dana Osei for `view_load_error`, Lee Zhang as data
steward across the table) and gives the three proxy actions and the report-open event names in the PRD's own
object-then-past-tense pattern. Each choice is stated as the plan's own, not as read from a sibling.

It must not contain: the OKRs' Initiatives-table status line for Saved Views (`okrs_example.md:90`); any of the four
residuals PR #204 left unfixed (the announcement's "private views since late June", the retrospective's 2026-09-14
general-availability date, the release notes' known issue promising a fix in 2.4.1, and the definition of done's
"DEF-2291 shipped in build 2.3.2"); the experiment's result; or any document dated after 2026-08-24 cited in body prose.
Amplitude appears only as where events land, never with wording borrowed from Amplitude's own template.

---

## Sources

### VENDOR CANON: WHAT THE TRACKING PLAN IS, AND WHAT IT CARRIES

**[1] Avo docs, 'The Avo Tracking Plan'.** vendor. **fetched-and-verified.**
`https://www.avo.app/docs/data-design/avo-tracking-plan`
Supports: form (in-tool schema used to generate code and validate data), section breakdown (Journeys/Events/Properties/Metrics/Publishing/Connection Setup/Codegen Setup/Inspector)
Quotable: "The Avo Tracking Plan is where you define the data for your application. It contains detailed definitions of your tracking plan that can be used to generate code from and validate your data against."
Quotable: "Journeys : visually design analytics using product screenshots with AI-powered suggestions"
Quotable: "Tracking Plan Events : where all events structures are defined"
Quotable: "Tracking Plan Properties : where all properties are defined"
Quotable: "Tracking Plan Metrics : where all metrics are defined"
Quotable: "Tracking Plan Publishing : sync your tracking plan with the one in your analytics platform"
Quotable: "Connection Setup : configure sources and destinations, including setting up Inspector and Avo Codegen"
Quotable: "Codegen Setup : source specific event reference for Avo Codegen, with code snippets that help you implement"
Quotable: "Inspector : get a report of the state of your tracking and get alerted when new issues are detected"

**[2] Avo docs, 'Data Design' index ('What is a Tracking Plan?').** vendor. **fetched-and-verified.**
`https://www.avo.app/docs/data-design`
Supports: one-sentence definition; who writes/uses; three things the plan should do
Quotable: "A tracking plan is a document that defines the key stages of your customer life cycle and codifies a single source of truth for the data that supports it. Through this plan, you standardize your data management and capture better and cleaner data."
Quotable: "Clarify the events and properties that are relevant to your goals and customer journey"
Quotable: "Explain the location in the codebase that your analytics should be added to make your developers’ lives easier"
Quotable: "Summarize the reason for tracking each event and property and how they’ll be used to measure your progress."
Quotable: "In an ideal world, these three things-and your tracking plan in totality-should be stored as a central, shareable document that your team can update together."

**[3] Avo blog, 'Avo's Ultimate Tracking Plan Template (w/ Downloadable Worksheet)' by Thora Gudfinnsdottir.** vendor. **fetched-and-verified.**
`https://www.avo.app/blog/avos-ultimate-tracking-plan-template-w-downloadable-worksheet`
Supports: ten worksheet columns (all read verbatim), event-naming guidance, form as downloadable spreadsheet template, who writes/collaborates
Quotable: "A tracking plan is a document that defines the key stages of your customer life cycle and codifies a single source of truth for the data that supports it. It helps you standardize your data management and capture better and cleaner data."
Quotable: "There are dozens floating around the internet, so we went ahead and created our 🎉Ultimate Tracking Plan Template 🎉 that pulls together the 10 elements you absolutely must have."
Quotable: "1. KPIs"
Quotable: "2. Event categories"
Quotable: "3. Event names"
Quotable: "4. Event description"
Quotable: "5. Properties"
Quotable: "6. Property description"
Quotable: "7. Property value types"
Quotable: "8. Platforms"
Quotable: "9. Status"
Quotable: "10. Code snippet"
Quotable: "Additionally, each of your events should be named in a consistent way that’s in line with your agreed-on naming schema."
Quotable: "Note how each of these event names shares the same tense (past tense) and capitalization. This isn’t just to make your template look pretty; it makes everything easier to understand."
Quotable: "Please go ahead and make a copy of the template here."
Quotable: "This is one of the few sections of your tracking plan that will not greatly vary. Instead, the data in this column should include these common data types: int floating-point number boolean string datetime a list of any of the data types above"

**[4] Twilio Segment docs, 'Protocols Tracking Plan' / 'Create a Tracking Plan'.** vendor. **fetched-and-verified.**
`https://segment.com/docs/protocols/tracking-plan/create/`
Supports: one-sentence definition, form as in-tool schema that validates live events, who writes/uses, Identify/Group trait handling, event-naming/validation guidance, column names in the editor table, licence/copyright footer
Quotable: "A Tracking Plan is a data spec outlining the events and properties you intend to collect across your Segment Sources. Crafting a comprehensive Tracking Plan takes time and effort across a range of teams within your organization, and a deep understanding of your business objectives. Once created, the Tracking Plan becomes a highly valuable resource for both the engineers instrumenting Segment and all consumers of the data flowing through Segment."
Quotable: "Each user action maps to a distinct event, or Track call, that you will track in Segment. The Tracking Plan can also validate Identify, Page and Group calls."
Quotable: "The Segment Tracking Plan feature allows you to validate your expected events against the live events that are delivered to Segment. Violations generate when an event doesn't match the spec'd event in the Tracking Plan."
Quotable: "You can define which traits you expect to see passed in Identify or Group calls like how you would add Track calls to the Tracking Plan. Navigate to the Identify or Group tab in your Tracking Plan and click the ( + ) button to add a new trait."
Quotable: "It's best to keep traits optional because Identify and Group are often called and pass only new or changed traits, because Segment's client-side libraries (analytics.js, Swift, Kotlin) cache traits in local storage."
Quotable: "Description Enter a description for your event or property. These descriptions are helpful for both engineers instrumenting Segment and consumers of the data."
Quotable: "Permitted Values Enter simple regular expressions to validate property values. This works when a property data type is set to string."
Quotable: "Click into the row to add an event name and description. The event name strictly validates the name passed in your Track calls. Casing, spacing and spelling matter."
Quotable: "Copyright © 2026 Twilio Inc."
Quotable: "Property or trait data type should adhere to the data types defined by JSON schema"
Quotable: "Data type names must be lower-cased as specified in JSON schema."

**[5] Twilio docs mirror of Segment 'Create a Tracking Plan'.** vendor. **fetched-and-verified.**
`https://www.twilio.com/docs/segment/protocols/tracking-plan/create`
Supports: confirms the segment.com page's text is duplicated verbatim on the twilio.com mirror (same definition, same Identify/Group traits guidance, same column descriptions)
Quotable: "A Tracking Plan is a data spec outlining the events and properties you intend to collect across your Segment Sources."
Quotable: "Copyright © 2026 Twilio Inc."

**[6] Twilio blog, 'What is a tracking plan' by (Twilio/Segment editorial, 'Learn').** vendor. **fetched-and-verified.**
`https://www.twilio.com/en-us/blog/insights/what-is-a-tracking-plan/`
Supports: one-sentence definition, four worked-example column headers (NAME, PROPERTIES, LOCATION, WHY, all read verbatim), form as document or spreadsheet, who writes it (cross-department collaborative document), naming-convention variability, licence/copyright footer
Quotable: "A tracking plan is a document or spreadsheet used across an organization to standardize how it tracks data. Often serving as both a project management tool and a reference document, a tracking plan aligns multiple teams around one strategy for customer data collection."
Quotable: "Essentially, a tracking plan consists of a list of events (i.e., user actions) accompanied by a description for each event."
Quotable: "Your tracking plan serves as the single source of truth across your organization for understanding what data you’re tracking, where you’re tracking that data, and why. A tracking plan usually has columns for each of these values, like this:"
Quotable: "In this example, the “what” is the events and properties you track, which are logged in the NAME and PROPERTIES columns above. The “where” (logged under LOCATION) is the location and time at which the event is being tracked. Finally, the “why” (logged under WHY) is a short description of the business purpose that justifies tracking the event."
Quotable: "Not all tracking plans look exactly like this. They’re living documents that are built to suit the needs of the businesses they serve. You might use a different naming convention for event names and event properties..."
Quotable: "A tracking plan is a collaborative document, taking input from every department that touches customer data."
Quotable: "Copyright © 2026 Twilio Inc."
Quotable: "All rights reserved."

**[7] Twilio Segment glossary.** vendor. **fetched-and-verified.**
`https://www.twilio.com/docs/segment/glossary`
Supports: one-sentence (two-clause) definition of tracking plan, form as document/spreadsheet or in-tool feature, event vs. object/trait distinction, licence/copyright footer
Quotable: "A tracking plan is a tool that our customers use to keep track of their analytics setup. It contains all of the events, pages, traits and properties they want to record with information about how each is laid out. It's often in a spreadsheet or document, and Segment also includes this functionality in the core product so that people can plan out their tracking setup right from inside Segment."
Quotable: "Traits are individual pieces of information that we know about an object. Objects persist over time, so traits can change over time."
Quotable: "An object is a type of data that persists over time and can be updated, for example a Business or a User record. Objects have "traits" which record information about that object, and which can change over time."
Quotable: "An event can refer to either an action by a user, or something a user does which triggers a track call. Events have a name (for example "Product viewed") and properties (for example the product name, price, and category), and take place in a single moment in time."
Quotable: "Copyright © 2026 Twilio Inc."

**[8] Amplitude Docs, "Create a tracking plan" (Data product documentation).** vendor. **fetched-and-verified.**
`https://amplitude.com/docs/data/create-tracking-plan`
Supports: The in-tool fields a tracking plan carries in Amplitude Data, and the governing one-sentence framing of what a tracking plan is for
Quotable: "A tracking plan defines every event and property you collect, why you collect each one, and which source emits it."
Quotable: "Build one before you instrument code so analysts, PMs, and engineers work from one schema instead of arguing about field names after the data lands."
Quotable: "In Amplitude Data, the plan lives next to your events and properties, so edits flow straight into instrumentation, governance, and the Ampli code generator."
Quotable: "An event is a distinct action that a user can take in your product."
Quotable: "Event properties describe the event and the context in which a user triggered it."
Quotable: "User properties capture traits about the user."
Quotable: "Group properties make it easy to associate a user with a particular account (for example, name, industry, or employees) whenever the group() call runs."
Quotable: "A name, description, examples, and rules define each property."
Quotable: "The code exactly replicates the spec in the tracking plan and enforces all its rules and requirements."

**[9] Amplitude Blog, "How to create a tracking plan?" by Arpit Choudhury (excerpted from The Amplitude Guide to Behavioral Data & Event Tracking, originally published 2022-06-07, updated 2024-11-15).** vendor. **fetched-and-verified.**
`https://amplitude.com/blog/create-tracking-plan`
Supports: The verbatim one-sentence definition, the living-document/source-of-truth language, the fields/sheets the template carries, the owner/source role language, and the template's existence and shape (one Google Sheets template, confirmed by reading the page text describing its tabs; the template file itself was not opened)
Quotable: "A data tracking plan (usually referred to as just a tracking plan) is a document that acts as a source of truth for your event data-it's a living document that contains all the information related to the data you gather about your customers when they interact with your product."
Quotable: "Any piece of data that is not in your tracking plan should not be tracked and conducting regular audits of your tracking plan can prevent costly mistakes"
Quotable: "The tracking plan not only maintains a repository of what data needs to be tracked, but also specifies where the data comes from (data source), the tools and systems the data needs to be sent to (data destinations), as well as who is responsible for the implementation."
Quotable: "It is extremely helpful to mention the source where an event is being tracked. Doing so even makes it easy to assign an owner-the person responsible for the implementation of that event."
Quotable: "The tracking plan template below is a Google Sheets spreadsheet that was created after a lot of research and many iterations to suit almost every industry. It also comes with some sample events and properties to give you a head start."
Quotable: "The template contains the instructions as well as a glossary of terms."
Quotable: "Go ahead and list down all user properties, their data types, expected values, and destinations in the sheet labeled User Properties."
Quotable: "© 2026 Amplitude, Inc. All rights reserved. Amplitude is a registered trademark of Amplitude, Inc."

**[10] Amplitude, "What Is Event Taxonomy: Complete Definition & Framework" (Explore Hub).** vendor. **fetched-and-verified.**
`https://amplitude.com/explore/data/event-taxonomy`
Supports: Amplitude's role chain for event-taxonomy governance, verbatim, plus the event-taxonomy definition and change-tracking/versioning language
Quotable: "An event taxonomy is a structured system for naming, organizing, and categorizing user actions and their properties across your app or website."
Quotable: "Assign specific roles for taxonomy management:"
Quotable: "Event requesters propose new events with clear use cases"
Quotable: "Data stewards review naming and check for duplicates"
Quotable: "Domain owners approve events within their product areas"
Quotable: "A typical approval process includes proposal submission, naming review, domain approval, implementation, testing, and documentation updates."
Quotable: "Track all taxonomy changes with version labels like "proposed," "active," "deprecated," and "removed." Document what changed, when, why, and who approved it."
Quotable: "Create central documentation listing every event, property, data type, and owner. Include examples and implementation notes for developers and analysts."
Quotable: "© 2026 Amplitude, Inc. All rights reserved. Amplitude is a registered trademark of Amplitude, Inc."

**[11] Mixpanel Docs, "Create A Tracking Plan" (Best Practices).** vendor. **fetched-and-verified.**
`https://docs.mixpanel.com/docs/tracking-best-practices/tracking-plan`
Supports: Mixpanel's bullet definition of what a tracking plan should be/do (its closest analogue to a one-sentence definition), its living-document/source-of-truth language, its methodology steps, and the names of the templates it links on this page (four named vertical templates plus one blank template - names read directly, template contents not opened)
Quotable: "Be a centralized document that should serve as the source of truth on your Mixpanel implementation"
Quotable: "Define your business goals / KPIs and analytics strategy metrics"
Quotable: "Outline the events, event properties, and user profile properties aligned to your metrics"
Quotable: "Be treated as a living and shared document that is continuously updated with any implementation changes"
Quotable: "Include notes that are referenced across teams (product, marketing, data science, tech / dev teams, etc.)"
Quotable: "Mixpanel provides the following templates for vertical-specific tracking plans:"
Quotable: "Retail and E-commerce"
Quotable: "Media and Entertainment"
Quotable: "SaaS"
Quotable: "Financial Services"
Quotable: "You can also access a copy of a blank Tracking Plan from here."

**[12] mParticle Blog, "What is a data plan, and why is it important to have one?" (Engineering).** vendor. **fetched-and-verified.**
`https://www.mparticle.com/blog/data-tracking-plan-engineers/`
Supports: mParticle blog's one-sentence/bulleted definition of a data tracking plan, its source-of-truth language, how the document-form plan relates to the in-tool Data Plan (import path via Smartype/Snippet SDK), and which teams it aligns
Quotable: "A data tracking plan is a document that keeps different teams aligned on the key information regarding your organization's data collection and analysis efforts."
Quotable: "It is an internal framework that spells out (among other things):"
Quotable: "Which user events will be tracked?"
Quotable: "A data tracking plan can exist as a static document like a spreadsheet, or it can live within a data software solution like a Customer Data Platform (CDP)."
Quotable: "Typically, it's Marketing, Product Management, and Data Engineers that are most involved in decisions around the data tracking plan"
Quotable: "Without developers implementing tracking code, a data tracking plan is just another document."
Quotable: "One of the most significant advantages of infrastructure CDPs is that they give cross-functional teams the ability to create data plans inside of a UI, and use this as the single source of truth throughout the organization. In mParticle, for instance, once a Data Plan has been created, developers have the tools to programmatically import data tracking plans into the codebase, and use this to enforce data quality throughout event instrumentation."
Quotable: "© 2026 mParticle, Inc."

**[13] mParticle Docs, "Data planning" (Platform Guide).** vendor. **fetched-and-verified.**
`https://docs.mparticle.com/guides/platform-guide/data-planning/`
Supports: mParticle's in-tool Data Plan definition and its component fields, the three ways/tools to build one (UI, Data Plan Builder Google Sheet, Data Planning API), and the named industry templates it ships (names read directly from the page; template files not opened)
Quotable: "A data plan is a codified set of expectations about the extent and shape of your data collected with mParticle. A plan contains the following elements:"
Quotable: "Name : a descriptive label for the plan."
Quotable: "ID : a URL-safe slug. This value never changes and is automatically generated based on the original plan name."
Quotable: "Version (Optional) : an integer value."
Quotable: "Description (Optional) : an optional freeform field to describe the plan."
Quotable: "Data Points : each data point contains an event, user attributes, or user identities. You define these for each type of data you expect to receive."
Quotable: "Data Plan Builder is a Google Sheet add-on and template that helps you create a data plan:"
Quotable: "Choose from one of the industry-specific templates or the generic template."
Quotable: "Generic"
Quotable: "Travel"
Quotable: "QSR"
Quotable: "Gaming"
Quotable: "FinTech"
Quotable: "Retail"
Quotable: "Media"
Quotable: "© 2026 mParticle, Inc. All rights reserved. mParticle.com Privacy Policy Cookie Policy Do Not Sell or Share My Personal Data"

**[14] Countly Glossary, "Tracking plan".** vendor. **fetched-and-verified.**
`https://countly.com/glossary/tracking-plan`
Supports: Countly's one-sentence definition of a tracking plan, its field list, and its versioning/review language
Quotable: "A tracking plan is a governed specification of the events, properties, identities, sources, owners, and rules used to collect analytics data."
Quotable: "It translates product questions into an implementation contract for product, engineering, analytics, privacy, and marketing teams."
Quotable: "A strong plan defines naming conventions, data types, allowed values, triggering conditions, examples, sensitivity, retention, and validation."
Quotable: "It should be versioned and reviewed whenever the product or measurement strategy changes."
Quotable: "Before building checkout analytics, a team documents each event, when it fires, required properties, platforms, owners, and test cases."
Quotable: "2026 © Countly Ltd. All rights reserved."

### KEEPING IT TRUE: CADENCE, OWNERSHIP, VERSIONING AND PRIVACY

**[15] RudderStack Knowledge Base, "Getting Started with Tracking plans".** vendor. **fetched-and-verified.**
`https://www.rudderstack.com/knowledge-base/get-started-with-tracking-plans/`
Supports: Versioning mechanism (tracking plan ID + version number) and the iterative-process framing of plan maintenance
Quotable: "Tracking plans support versioning, which enables us to iterate and monitor the changes in a tracking plan event spec, the intention for tracking plans is to be an iterative process and a part of every sprint so having versioning there helps keep track of all the changes."
Quotable: "Tracking Plans allow us to plan and prescribe what our data should look like before it is sent to our destinations."

**[16] RudderStack Docs, "Tracking Plans" (Data Governance).** vendor. **fetched-and-verified.**
`https://www.rudderstack.com/docs/data-governance/tracking-plans/`
Supports: Versioning system and per-event-version validation; no stated review cadence; no explicit per-event lifecycle-state vocabulary
Quotable: "Iteratively improve your tracking plans and have better control of your data with a robust versioning system."
Quotable: "Different events may be validated against different tracking plan versions because RudderStack validates each event against the specific version that was used to instrument it."
Quotable: "This happens when: You have multiple app versions deployed simultaneously"
Quotable: "Each app version was instrumented using a different tracking plan version"
Quotable: "The SDK sends the tracking plan version along with each event"

**[17] Snowplow Docs, "Tracking plans" (Fundamentals).** vendor. **fetched-and-verified.**
`https://docs.snowplow.io/docs/fundamentals/tracking-plans/`
Supports: Named owner, consumers/subscribers, and an explicit change-history element; no stated review cadence; no per-event lifecycle-state vocabulary found
Quotable: "At its core, a tracking plan has: An explicit owner; that is responsible for maintaining and updating the data over time"
Quotable: "Consumers; who use the data to deliver use cases and are impacted by upstream changes"
Quotable: "An owner; tracking plans are typically split by domain with each tracking plan having an explicit owner that is responsible for the maintenance and evolution of that data."
Quotable: "Subscribers; allow colleagues to express an interest in understanding changes that are made to the data within a Tracking Plan, usually because the data is being used in a downstream data model or Data Model Pack."
Quotable: "Change history; a complete audit log of the changes that have been made to the tracking plan, including changes to existing data and new data that has been added over time."
Quotable: "Enhances accountability and transparency by providing a clear audit trail of all data modifications, fostering confidence in data integrity"
Quotable: "Tracking plans at Snowplow are underpinned by the concept of a data contract. They act as a formal agreement between the producers of tracking plans and the consumers of tracking plans, and support better collaboration around the data being created."

**[18] Snowplow Docs, "Event Studio" (the page served at the given 'introduction-to-tracking-design' URL; current page title is Event Studio).** vendor. **fetched-and-verified.**
`https://docs.snowplow.io/docs/understanding-tracking-design/introduction-to-tracking-design`
Supports: Ownership/governance as a toolset feature and 'tracking plans' defined as groupings of events with defined ownership; schema versioning mentioned as a Schema management capability; no review cadence or lifecycle-state vocabulary stated
Quotable: "Schema management: define and version data structures for events and entities"
Quotable: "Ownership and governance: assign ownership and establish data contracts"
Quotable: "Tracking plans: logical groupings of related business events with defined ownership"

**[19] Digital Applied, "Product Analytics: An Event Taxonomy That Won't Rot" (Digital Applied Team).** practitioner. **fetched-and-verified.**
`https://www.digitalapplied.com/blog/product-analytics-event-taxonomy-tracking-plan-2026`
Supports: Lifecycle states (reported as Amplitude's, via this practitioner piece), owner field / data-steward role, failure modes taxonomy (naming drift, owner departure, autocapture shift, identity fragmentation, over-tracking, silent device-mode blocking); PII is not addressed by this source
Quotable: "Amplitude Tracking plan as single source of truth"
Quotable: "Codegen via Amplitude Data (formerly Iteratively)"
Quotable: "Four roles: requester, steward, owner, implementer"
Quotable: "Version labels: proposed"
Quotable: "active"
Quotable: "deprecated"
Quotable: "removed"
Quotable: "The event has a named owner or data steward accountable for its definition. An event with no owner is the owner-departure decay vector waiting to happen - the highest recovery cost in the decay table."
Quotable: "A breaking change ships with a migration plan before the old event stops collecting. Deprecated events move through proposed / active / deprecated / removed states deliberately, never abandoned in place under a new name."
Quotable: "Owner departure"
Quotable: "Event author leaves; no accountable steward"
Quotable: "Nobody can explain what an event means"
Quotable: "High"
Quotable: "Required owner field; data-steward role"
Quotable: "The most common tracking-plan failure mode is not technical - it is organizational. The plan exists. It is just not enforced."
Quotable: "Mixpanel (Data Standards)"
Quotable: "Automated compliance checks; flags in Lexicon"
Quotable: "Not codegen-first; proactive convention enforcement"
Quotable: "Required metadata: descriptions, owners, media"
Quotable: "Enterprise tier; launched Apr 16, 2025"
Quotable: "10-200 events"
Quotable: "Published June 10, 2026"

**[20] CustomerScore, "Event Tracking Plan for SaaS: A Phase-One Blueprint" (Patrik Chalupa, Co-founder & CMO).** practitioner. **fetched-and-verified.**
`https://www.customerscore.io/blog/event-tracking-plan-saas`
Supports: A stated review interval (90 days, attributed to a third party, House of MarTech), a named-person ownership rule, a 14-column schema with explicit plan_version/owner/pii_flag/last_verified fields, a schema-change process, and a PII-masking rule
Quotable: "Schedule a 90-day audit. Any event unverified after 90 days is presumed broken until someone validates it."
Quotable: "The 90-day audit rule from House of MarTech is the right cadence. Any event whose last_verified date is older than 90 days is presumed broken until someone validates it in production."
Quotable: "Assign one owner per event: product, engineering, or analytics, not "the team.""
Quotable: "owner: a named person, not a team."
Quotable: "Product defines the business question and the "why" for each event."
Quotable: "Engineering confirms the trigger, the payload structure, and the "how.""
Quotable: "Analytics enforces schema compliance and owns the last_verified audit."
Quotable: "One named owner per event accepts accountability for downstream use cases."
Quotable: "pii_flag: true or false; routes the event through masking or exclusion pipelines."
Quotable: "The pii_flag and downstream_systems columns do the heaviest governance work. A true PII flag should trigger automatic masking before the event reaches your analytics warehouse."
Quotable: "Propose the change in the source-of-truth document (Google Sheet, Notion, or Git repo)."
Quotable: "Update the schema and bump plan_version."
Quotable: "Run CI validation against the new spec."
Quotable: "Stage the rollout and verify in a non-production environment."
Quotable: "Update event_version in the payload and last_verified in the plan."
Quotable: "Treat the tracking plan like code. Every schema change should go through a pull request, get reviewed by the analytics owner, and include a rollback plan. If an event isn't in the spec, it shouldn't reach the warehouse."
Quotable: "Unclear ownership. "The analytics team owns it" means nobody owns it. One named person per event, full stop. When that person leaves, the plan gets updated before the offboarding is complete."
Quotable: "Add an event_version field to every payload (e.g., event_version: "2"). When you change a property's data type or rename a field, bump the version. Segment Protocols supports this via context.protocols.event_version, and it prevents downstream breakage during schema migrations."
Quotable: "A tracking plan without governance is a document that's wrong within 60 days of shipping."

**[21] Trackingplan, "Data Governance for Analytics: A Practical Guide to Trusted Data" (David Pombar, Trackingplan).** vendor. **fetched-and-verified.**
`https://www.trackingplan.com/blog/data-governance-for-analytics`
Supports: Data Owner vs. Data Steward role distinction, PII masking/leak-prevention policy framing, governance-as-continuous-process (explicit rejection of a fixed cadence in favor of continuous automated monitoring)
Quotable: "A Data Owner is usually a senior leader who is ultimately responsible for a specific data domain, like all customer data or all product data. They aren't in the weeds managing it day-to-day, but the buck stops with them when it comes to its quality, security, and ethical use."
Quotable: "Data Stewards are your hands-on heroes. These are the subject matter experts who handle the daily management of data-defining terms, monitoring quality, and making sure everything complies with company policies. They are the frontline defenders of data integrity."
Quotable: "Your policies must include strict controls to prevent the accidental collection of Personally Identifiable Information (PII) like names or email addresses in analytics events. Automated monitoring for potential PII leaks is no longer a luxury-it's a necessity."
Quotable: "Manual spot-checks and quarterly audits feel like relics from a different era. They're slow, riddled with potential for human error, and simply can't handle the millions of data points streaming in every second. The future of effective data governance for analytics depends on continuous, automated observability."
Quotable: "A classic mistake is treating governance like a finite project-something you set up, document, and promptly forget. This "one-and-done" thinking is a primary reason so many programs fail."
Quotable: "Governance has to be a living, breathing process, not a dusty binder on a shelf."

**[22] Avo Docs, "1. Plan analytics update in Avo branch" (Avo Workflow).** vendor. **fetched-and-verified.**
`https://www.avo.app/docs/workflow/plan`
Supports: Per-feature change proposed against the standing plan via a branch, with a named role per step (Product/Data) and a peer-review gate before implementation
Quotable: "A branch allows you to draft changes to the tracking plan in isolation, without impacting the main branch, which contains the single source of truth of what's currently being tracked."
Quotable: "Role: Product or Data (This initiative is usually led by a product oriented person)"
Quotable: "The first thing you do in Avo, for a product release, is to create a new branch."

**[23] Avo Docs, "Quickstart: Branches" (Branched workflows).** vendor. **fetched-and-verified.**
`https://www.avo.app/docs/data-design/branches`
Supports: Branch lifecycle states (Draft, Ready for Review, Approved, Changes Requested) distinct from an event's own status, review/approval gate, and recommendation to merge branches quickly
Quotable: "We highly recommend always creating a branch first before making changes to the tracking plan, no matter how small the changes are - in particular if the changes made require implementation."
Quotable: "When you've suggested changes to your tracking, mark the branch as ready for review, and assign an editor or admin to review the changes."
Quotable: "When a branch is marked as Ready for Review (or later), it is locked for editing if your workspace has Protected main branch enabled. To make further changes, revert the branch to Draft-this will remove any existing approvals."
Quotable: "Branch Status: Filter branches by their current status (Draft, Ready for Review, Approved, Changes Requested, etc.)"
Quotable: "We recommend setting up branches that have isolated changes that can be opened, implemented and merged within a few days. Typically there's a one to one mapping between Avo branches and git branches."

**[24] Avo Docs, "Using Avo in large development teams with parallel workflows" (Avo and Git).** vendor. **fetched-and-verified.**
`https://www.avo.app/docs/implementation/guides/avo-and-git`
Supports: The exact branch-and-merge workflow for reconciling one feature's tracking change against the standing plan, mirroring git branches, plus a complete change-history guarantee for merged branches
Quotable: "First, they open a new branch in their Avo tracking plan, where they can modify the tracking plan without changing it for anyone else."
Quotable: "When the tracking plan changes made on the branch have been peer-reviewed and approved in Avo, they can start the tracking implementation."
Quotable: "Once the tracking has been implemented, and the feature is ready to go, the developer gets their git branch merged like they usually would. As soon as the git branch is merged into the git main branch, they merge their Avo branch in the Avo main branch. By doing so, the main branch in Avo always represents the current state of the Avo tracking plan, while the tracking plan implementation stays pinned to the branch we just implemented."
Quotable: "Previously merged Avo branches can always be viewed back in time. That means you can always see the state of your tracking plan at that point, what changes were made when, and by whom."
Quotable: "Open an Avo branch and make your Tracking Plan changes"
Quotable: "Get a peer-review and approval on the changes"
Quotable: "Implement the changes from the Avo branch in your code on a git branch"
Quotable: "Merge the git branch"
Quotable: "Merge the Avo branch"
Quotable: "Details on what changes were introduced on the Avo branch remain available for future reference"
Quotable: "Yes, the generated code from Avo as well as avo.json should be checked into your source control. With the avo.json file checked in, the source code is always pinned to a certain point in time of the Tracking Plan and the Avo CLI configuration is automatically shared within your team."

### CONTESTED PRACTICE: AUTOCAPTURE, NAMING AND WHERE THE PLAN LIVES

**[25] John Cook (Heap), "Why Heap Isn't Built on a Manual Tracking Foundation".** vendor. **fetched-and-verified.**
`https://www.heap.io/blog/why-heap-isnt-built-on-a-manual-tracking-foundation`
Supports: (a) autocapture-versus-designed-plan camp and the plan-is-not-unnecessary-but-later nuance; (d) the spreadsheet as the tracking plan's fragile home
Quotable: "we built Heap from the ground up with a different approach: automatically capture all the data"
Quotable: "We typically advise that teams manually capture 5-10 core KPIs with our Track API (actions like “Payment Processed” or “Sign Up Submitted”, for example)."
Quotable: "In other tools, events are typically managed via a “tracking plan” - a spreadsheet managed outside of the platform. If you’ve ever tried to manage a spreadsheet at scale, you know how easily things can break."
Quotable: "is a false choice."

**[26] Avinash Kaushik, "Digital Marketing and Measurement Model" (Occam's Razor).** practitioner. **fetched-and-verified.**
`https://www.kaushik.net/avinash/digital-marketing-and-measurement-model/`
Supports: (e) what the model is (a five-step business-objectives-to-segments document) and that it never mentions events or a tracking plan
Quotable: "I’ve developed the Digital Marketing & Measurement Model as a simple, structured, five step process"
Quotable: "Step one is to force us to identify the business objectives upfront"
Quotable: "Step three is to write down the key performance indicators."
Quotable: "Step five, finally, is to identify the segments of people / behavior / outcomes that we’ll analyze"

**[27] Nimble (software consultancy), "Event Tracking Guidelines" (internal engineering compass, published).** practitioner. **fetched-and-verified.**
`https://nimblehq.co/compass/product/analytics/event-tracking-guidelines/`
Supports: (b) the object-action naming convention, past-tense verbs, and snake_case casing, attributed to Segment's framework; Cross-platform consistency as a named, deliberately engineered problem, not an assumed property of an event name column
Quotable: "Segment’s object-action framework quickly came up as a robust and simple to understand framework."
Quotable: "Action: defines how users can interact with the objects in the application. An action must be in the past (e.g., “added” and not “add”, “registered” and not “register”)."
Quotable: "All event names and properties should use the snake case format. It is defined with all letters being lowercase, and using an underscore as the separator (e.g., snake_case)."
Quotable: "By default, automatic screen tracking is enabled on Firebase Analytics. As a result, the screen names differ per platform, which makes it hard to actually use the data."
Quotable: "To track the performance of mobile apps, it is recommended to track both Android and iOS under the same Google Analytics property. This way, it will be easier to run any comparison between the platforms."
Quotable: "developers must then manually log a screen_view event on each screen. And to make the data actionable, they must follow once again a naming convention."
Quotable: "pattern for naming custom event"

**[28] DataTalks.Club Podcast Wiki, "Tracking Plans".** practitioner. **fetched-and-verified.**
`https://datatalks.club/podwiki/wiki/tracking-plans/`
Supports: (d) spreadsheet as an acceptable starting home for a small event set, and (f) who touches/owns the plan
Quotable: "A tracking plan is the specification artifact for product instrumentation."
Quotable: "Teams can start with a spreadsheet or document when the event set is small. The plan still comes before instrumentation. Avo, Iteratively, and TrackPlan are collaborative tracking-plan tools for taxonomy and event-quality discussion."
Quotable: "Tracking plans need owners because event definitions change as products change, and ownership is part of the tracking-plan definition. Data engineers, analysts, analytics engineers, and product operations all touch the stack."
Quotable: "The team needs to decide who can add an event, who reviews the name and properties, and which engineer owns implementation. It also needs a product or analytics owner who confirms the meaning and downstream dependencies."

**[29] Tag Insight (vendor documentation), "Designing your tracking plan".** vendor. **fetched-and-verified.**
`https://docs.taginsight.com/best-practices/tracking-plan-design`
Supports: (a) a phased, start-simple argument that is not an autocapture position but a middle path against tracking everything at once; (b) a naming label that conflicts with the object-action order; (f) ownership split across marketing, technical and analytics teams
Quotable: "Don’t try to track everything at once. Build your tracking in phases:"
Quotable: "Phase 1: Business essentials (Weeks 1-2) Start with what directly impacts revenue"
Quotable: "Use consistent format Always lowercase Words separated by underscores Action_object pattern"
Quotable: "Marketing team: Defines business requirements Prioritizes what to track Uses the data for decisions Technical team: Implements tracking code Ensures accuracy Fixes issues Analytics team: Creates reports Identifies gaps Suggests improvements"

**[30] Mila, Data Club (Substack, published by the Wunderbar Network), "How to get the most out of your Product Analytics with Naming Conventions".** practitioner. **fetched-and-verified.**
`https://dataclub.substack.com/p/how-to-get-the-most-out-of-your-product`
Supports: (b) object+action with past-tense verbs, and explicit refusal to pick one casing as correct; (d) spreadsheet as one valid tracking-plan medium, with the plan preceding naming-convention work
Quotable: "If you don't know what you should track on your product or feel your data is already too messy - you need a tracking plan first."
Quotable: "Setup: Use a spreadsheet, Miro board, paper or whiteboard."
Quotable: "I recommend using the object+action framework because it's easy to visualise what object your user is interacting with and what action has taken place."
Quotable: "In the object-action framework, the verb is in the past tense: created clicked selected viewed connected"
Quotable: "snake_case - wallet_connected camelCase - walletConnected All lowercase - wallet connected Proper Case - Wallet Connected Sentence case - Wallet connected"
Quotable: "Choose one case and stick with it."

### BOUNDARIES: THE DATA DICTIONARY AND THE MEASUREMENT PLAN

**[31] Wizbrand, "Data Dictionary: What It Is, Key Features, Benefits, Use Cases, and How It Fits in Analytics".** vendor. **fetched-and-verified.**
`https://www.wizbrand.com/tutorials/data-dictionary/`
Supports: Tracking plan vs. data dictionary: forward-looking intent document vs. backward-looking structural record of implemented data
Quotable: "A tracking plan describes what you intend to track (events, triggers, parameters) and why."
Quotable: "A Data Dictionary documents what the data means and how it is structured once implemented."
Quotable: "In practice, they should align: the tracking plan drives implementation; the Data Dictionary keeps Analytics interpretation consistent over time."
Quotable: "Within Conversion & Measurement, it anchors your tracking plan, event taxonomy, and KPI definitions."

**[32] Wizbrand, "Analytics Measurement Plan" tutorial page.** vendor. **fetched-and-verified.**
`https://www.wizbrand.com/tutorials/analytics-measurement-plan/`
Supports: Tracking plan vs. measurement plan: narrower implementation artifact nested inside a broader business/KPI/governance document
Quotable: "A tracking plan is usually narrower and implementation-focused: events, parameters, triggers, and QA steps."
Quotable: "An Analytics Measurement Plan includes tracking details but also covers business objectives, KPI definitions, governance, and reporting logic."
Quotable: "In Conversion & Measurement, the measurement plan explains why you track; the tracking plan explains how."
Quotable: "A KPI framework defines what you measure and how success is judged. An Analytics Measurement Plan contains a KPI framework but adds data sources, instrumentation requirements, and operational governance inside Analytics."

### THE GAP QUESTION

**[33] GitLab (docs.gitlab.com) - "Event definition guide", Internal event tracking docs.** practitioner. **fetched-and-verified.**
`https://docs.gitlab.com/development/internal_analytics/internal_event_instrumentation/event_definition_guide/`
Supports: Naming-convention constraint on the event-name field itself, and a constraint on properties (each additional property must carry its own description)
Quotable: "A list of additional properties that are sent with the event. Each additional property must have a record entry with a description field."
Quotable: "Renaming an event is equivalent to deleting the existing event and creating a new one. This is acceptable if the event is not used in any metrics."
Quotable: "A unique name for the event. Only lowercase, numbers, and underscores are allowed."
Quotable: "The status of the event."
Quotable: "The milestone when the event is removed."

**[34] GitLab (docs.gitlab.com) - "Event lifecycle" guide.** practitioner. **fetched-and-verified.**
`https://docs.gitlab.com/development/internal_analytics/internal_event_instrumentation/event_lifecycle/`
Supports: Deprecation/removal of events as a defined, multi-step procedure with its own fields
Quotable: "To remove an event: Move the event definition file to the /removed subfolder. Update the event definition file to set the status field to removed. Update the event definition file to set the milestone_removed field to the milestone when the event was removed. Update the event definition file to set the removed_by_url field to the URL of the merge request that removed the event. Remove the event tracking from the codebase. Remove the event tracking tests."

**[35] GitLab handbook - "Data For Product Managers" (Enterprise Data program page).** practitioner. **fetched-and-verified.**
`https://handbook.gitlab.com/handbook/enterprise-data/organization/programs/data-for-product-managers/`
Supports: The question/decision each event serves (as a required planning step before instrumentation), a QA/validation step before an event ships, and who may request a new event / who reviews it
Quotable: "Test and Validate Owner: Engineer Perform local testing Request review from Analytics Instrumentation team member Verify test events match properties defined in the Issue"
Quotable: "Tag your assigned product analyst to review metric properties"
Quotable: "Create Instrumentation Issue Owner: Product Manager"
Quotable: "Start by determining what you need to measure: what user behaviors indicate feature success? what metrics will help you make product decisions?"

**[36] Mozilla (firefox-source-docs.mozilla.org) - Fenix "Telemetry - Implementation, Reviews, Renewals".** practitioner. **fetched-and-verified.**
`https://firefox-source-docs.mozilla.org/mobile/android/fenix/Telemetry-implementation,-reviews,-renewals.html`
Supports: A mandatory review gate before an event/metric ships, a retention/expiry field attached to each individual metric definition, and a contact list per metric
Quotable: "Data reviews are needed on all patches that add new telemetry or modify existing telemetry."
Quotable: "data_sensitivity:"
Quotable: "- interaction"
Quotable: "notification_emails:"
Quotable: "- fenix-core@mozilla.com"
Quotable: "When a telemetry metric is being renewed, do not remove the old data review links from metrics.yaml. The new approval should be added to the existing list."
Quotable: "expires:"

**[37] Mozilla Wiki - "Data Collection" (Mozilla's data collection program policy).** practitioner. **fetched-and-verified.**
`https://wiki.mozilla.org/Data_Collection`
Supports: Consent and lawful basis handled per sensitivity category (not a flat yes/no); who may request a data collection / who steward-reviews it; retention duration captured on the request form itself; periodic review of whether a collection is still justified
Quotable: "Data requester - the person requesting data to be collected"
Quotable: "Data steward - the person who ensures the data collection process is followed and that requested data complies with Mozilla policies"
Quotable: "A completed Request Form, documenting what data is to be collected, why Mozilla needs to collect this data, how much data will be collected, and for how long it will be collected"
Quotable: "Default OFF Data may be collected, but only if a user takes an clear, express action to opt-in to the collection."
Quotable: "Any collection requires prior Trust approval and (i) advance user notice (ii) consent and (iii) an opt-out."
Quotable: "Every year, the data collection owner and peers will survey all of the existing data collection systems for their product or project... To ensure that it is still necessary and useful to collect a piece of data."
