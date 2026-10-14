# business-continuity-plan: research log

Research conducted 2026-10-14, building on admission sweep 5 and its gap-fill (both 2026-10-12) and on the spec that
merged on 2026-10-13. The build's six-dimension fan-out covered the federal canon (NIST SP 800-34 and FEMA's Ready
Business template), the state and regulator sources that model the Disaster Recovery section and state a cadence,
the professional bodies and their debates, cloud and site reliability practice, the library's own neighbours and the
facts the worked example must agree with, and the standing gap question. **32 sources are recorded below, all
fetched-and-verified.** Only `fetched-and-verified` sources are quoted anywhere in this bundle.

**Every quotation in this log was checked against the source's raw text**, not against the summary a retrieval tool
returns: pages as downloaded, and PDFs through a text extractor. Two cached bodies were truncated and were re-fetched.
Three sources refuse a plain download, so their raw text was taken through a browser: the SANS policy PDF behind its
download link [17], FINRA's rule page [30] and an archived FDIC letter [11]. Against that raw text, 282 of the 292
quotations the build's agents returned pass: 277 as normalized substrings and 5 verbatim apart from rendering
artifacts. Twelve agent quotations were dropped, for the reasons the next section gives, and one quoted by two
dimensions was kept once. Seventeen were added from the main loop's own checks against raw text, four of them the
SANS statements re-quoted without their table identifiers. **296 quotations remain.**

---

## What the checks caught, and what was not read

**One quotation was filed under the wrong source.** The practice dimension listed SANS's sentence about the disaster
recovery plan being part of the business continuity plan under NIST SP 800-34. It is not in NIST's text, so it was
dropped from [1]. It stays under [16], where it passed: "The Disaster Recovery Plan is often part of the Business
Continuity Plan."

**The AWS sentence the spec warned about does not exist.** Earlier research attributed to the AWS whitepaper a
sentence saying a disaster recovery plan should sit inside a business continuity plan rather than stand alone. The
cloud dimension searched both cached AWS pages in full and found no such sentence. What AWS wrote is softer: "This
approach helps your organization to maintain business continuity as part of Business Continuity Planning (BCP)", and
"The objective of disaster recovery is business continuity" ([21]). The plain statement of containment among the
cloud vendors is Google's: "DR is a subset of business continuity planning." ([24]).

**The FFIEC booklet the research read is the March 2003 edition, and it is two editions old.** [9] is the 2003
Business Continuity Planning booklet, retrieved from an FDIC mirror. The Federal Reserve's 2019 transmittal letter
says the FFIEC "has revised the February 2015 version" ([10]), and FDIC's letter says the new booklet replaces the one
issued in February 2015 ([11]). So 2003 is not the immediate predecessor of the current booklet. A sentence that calls
the 2003 booklet the previous edition is wrong. The current 2019 booklet itself was not read: its canonical page
returned HTTP 403 on every attempt across two sessions.

**Twelve agent quotations were dropped.** Besides the misfiled SANS sentence: two NIST lists that the PDF's text
extraction does not reproduce in one run (the plan-review list, replaced by its lead sentence and two items checked
separately, and the Appendix A table of contents, which was not re-quoted); two FDIC
sentences that the letter's two-column layout interleaves with a sidebar; four SANS policy statements whose control
identifiers the PDF's table layout separates from their text, re-quoted without the identifier; a metadata line from
the ISO catalogue page; a FINRA list fragment; and one Visa contract sentence. None of the dropped quotations carried
a claim that no other quotation in the log carries.

**The SANS Resilience Management Policy's text is in a PDF, not on its page.** The page at [17]'s URL renders a title,
a summary and two download links. The policy text was read from the PDF those links serve, and the entry names it. The
practice dimension also reported that the policy is co-branded with a second organization. That does not appear in
the PDF's text, so this log does not repeat it.

**FEMA's Continuity Guidance Circular 1 is dated July 2013, and its status was not settled.** [29] was read on a
Minnesota legislature mirror whose path is marked inactive. A web search on 2026-10-14 returned FEMA-hosted files
titled "Continuity Guidance Circular" dated 2018 and 2024. Both returned HTTP 403 to a direct download, so this log
does not claim that either one replaced CGC 1. Treat [29] as time-bound: cite it as the 2013 circular, never as
current FEMA guidance.

**What was assigned and not read, or read only in part:**

- **ISO 22301 and ISO/IEC 27031.** Both are paywalled. [18] is ISO's free catalogue page and supports only what
  that page says. Nothing in this bundle may describe either standard's clause structure.
- **The current FFIEC Business Continuity Management booklet (2019).** HTTP 403 throughout. [10] and [11] are a
  transmittal letter and a regulator's summary, not the booklet.
- **The UK NCSC small business guidance.** The assigned collection page returned only site navigation, so it has no
  entry.
- **The Google SRE book, chapter 17.** [27] was read in full. It carries only a short passage on making disaster
  recovery tools testable offline, and none of the disaster-testing program material the research expected.
- **The BCI's Good Practice Guidelines and DRII's Professional Practices.** [14] names only the first of the BCI's
  six practices, and [15] is DRII's public summary; both full documents need a membership or login.
- **Ready.gov's Business Impact Analysis page.** It was a cache miss and was not fetched.

---

## The admission record

The spec's admission section stands, and this research confirms its two strengths. **The business continuity plan
admits on a literal fill-in template**: FEMA's Ready Business PDF ([4]) ships named sections and tables, and NIST
defines the plan independently ([1], [3]). **The disaster recovery plan admits on a definition**: NIST defines it
([1]), and the CSRC glossary carries a second, conflicting federal definition ([2]). NIST's template-building went to
the Information System Contingency Plan in its Appendix A, not to a disaster recovery plan, and no source in either
the sweep or this build ships a fill-in template titled as a standalone disaster recovery plan. California's SIMM
5325-A ([6]) is the one template-grade structure for recovering technology, and it is titled a Technology Recovery
Plan.

---

## Claims flagged contested or time-bound

1. **Whether disaster recovery is a section inside the plan or a separate plan beneath it.** The sources agree on
   the direction and disagree on the shape. NIST models the disaster recovery plan as its own plan type that "may
   support a BCP or COOP plan" ([1]), never as a section of one. Ready.gov's template lists an "Information Technology
   Disaster Recovery Plan (if not included in the business continuity plan)" among related plans ([4]), which permits
   either shape. California makes the technology recovery plan "a sub-set" of the continuity plan ([7]) and "just one
   portion" of business continuity ([6]). SANS says the disaster recovery plan "is often part of" the business
   continuity plan ([16]), and Google calls disaster recovery "a subset of business continuity planning" ([24]).
   **No source puts the two as equals, and no source requires disaster recovery to be a section rather than a
   separate supporting plan.** The bundle's shape, a Disaster Recovery section in full and none in lean, is the
   maintainer's choice that California and SANS state and NIST and Ready.gov permit. The lean variant points to a
   separate disaster recovery plan where one exists, which is the shape [4] allows.

2. **Where a disaster recovery plan recovers.** NIST SP 800-34 scopes it to "an alternate facility" and says it
   "only addresses information system disruptions that require relocation" ([1]). The CSRC glossary's CNSSI
   4009-2022 definition scopes it to recovering "at its original facilities" over "hours or days" ([2]). Two federal
   definitions disagree on the fact that most distinguishes the type.

3. **Whether the plan is reviewed and tested on a calendar or on events.** Most sources that state a cadence state an
   annual one: the 2003 FFIEC booklet in several places ([9]), HMPPS ([13]), SANS's 2014 policy ([16]), SIMM 5325-A's
   annual test ([6]), and NIST's sample attestation that a plan "will be tested at least annually" ([1]). NIST's own
   narrative is looser: review "at an organization-defined frequency or whenever significant changes occur to any
   element of the plan" ([1]). The cloud vendors and Reilly say to test regularly and give no number ([24], [26],
   [28]). Whether the current FFIEC booklet keeps a fixed interval is unsettled: [11]'s risk-commensurate framing is
   FDIC's summary, not the booklet's clause. This is the cadence tension ADR 0071 records. The bundle handles it as
   the spec says: the Review Trigger section states conditions, and an annual exercise appears as a floor that a
   regulator or policy may impose.

4. **Who writes the plan, who activates it, and who carries it out.** This is the open item in ADR 0071's
   uncertainty ledger, and the three dimensions that asked it returned three readings.
   - **Activation is separated from authorship by two sources.** NIST gives activation to "the designated authority
     (typically a senior manager or CIO)", while the ISCP Coordinator writes and maintains the plan ([1]). HMPPS says
     "A member of the nominated Business Continuity team will normally activate and stand down the plans", while
     Local Business Continuity leads "Complete the Business Continuity documentation" ([13]).
   - **Execution cuts the other way in NIST.** "The ISCP Coordinator also typically manages development and
     execution of the contingency plan." ([1]). The same role that writes the plan runs the recovery.
   - **Two sources state a design requirement, not a practice.** NIST says recovery procedures "are written at a
     level that an appropriately skilled technician can recover the system without intimate system knowledge"
     ([1]). SIMM 5325-A asks for procedures "detailed enough so that another trained information technology
     professional would be able to recover the state entity's infrastructure should those with primary
     responsibility be unavailable" ([6]). These say the plan must be written so that a stranger could run it. They
     do not say strangers usually do.
   - **The honest summary:** the activation half of the `tool` marker now has two sources. The execution half has a
     design requirement in two sources and a counter-reading in one. No source found says the author usually runs
     the plan alone. This research does not amend ADR 0071; the build PR reports the finding for the maintainer.

5. **Plan versus programme.** The professional bodies treat the written plan as one output of a management
   programme: the BCI places "plans" inside an "operational cycle" that "sits within a bigger 'management cycle'"
   ([14]), DRII lists "Plan Development and Implementation" as one practice of ten ([15]), and ISO describes "a
   documented management system" ([18]). URM argues that "having a BCP on paper is not enough" ([19]). **No source
   found defends a plan without exercising and maintenance as sufficient**, so this is consensus with a historical
   contrast, not two live camps. The bundle templates the plan, not the programme, and the companion says so.

6. **Test or exercise.** The 2003 FFIEC booklet names four test types ([9]) and NIST lists testing methods and
   exercise types side by side ([1]). URM insists that "these activities are an exercise, not a test", because an
   exercise has no pass or fail ([19]). The bundle keeps both words, as the section title "Training, Testing and
   Exercising" does, and does not adjudicate.

7. **Immutable backups.** Vendors promote immutable storage for ransomware recovery, but the joint government guide
   requires offline backups and says to "Use immutable storage with caution" ([31]). Nothing in this bundle presents
   immutability as settled practice.

8. **SANS's 2014 policy contradicts itself.** Its scope says it "does not provide requirement around what goes into
   the plan or subplans", and its next section requires seven named contingency plans ([16]). Whether SANS's 2026
   Resilience Management Policy ([17]) replaces it is stated by neither document.

9. **Time-bound sources.** [9] is the 2003 FFIEC booklet, at least two editions old. [29] is the 2013 FEMA circular,
   status unsettled. [16]'s canonical SANS page is gone, and the entry cites the SANS-hosted copy. [6] is the March
   2023 edition of SIMM 5325-A, and [7] the October 2025 revision of SAM 5325.1.

---

## Notes for the companion

**The honest framing.** A business continuity plan says how an organization keeps its critical business processes
going through a significant disruption and recovers them afterward. It is written and rehearsed before the
disruption and consulted during it. NIST and FEMA define it ([1], [3]), and FEMA ships it as a fill-in template ([4]).
Disaster recovery is narrower: it recovers the information systems those processes use, and NIST scopes it to
relocation ([1]). The two halves of the catalog's merged name admit at different strengths, template-grade for the
business continuity plan and definitional for disaster recovery, and the companion must not round the weaker one up.
The sources agree that disaster recovery serves business continuity and disagree on whether it is a section or a
separate plan (contested item 1). This bundle makes it a section in the full variant and a pointer in lean, and says
whose choice that was. The Business Impact Analysis is upstream: NIST templates it separately and says its results
"should be appropriately incorporated" into the plans ([1]), and California says the recovery plan "must be derived
from" it ([7]). The plan carries the analysis's results, not the analysis.

**The evidentiary spine, in the order it should be used:**

- **Definitions and plan types:** [1] for the business continuity plan, disaster recovery plan, contingency plan,
  RTO, RPO and maximum tolerable downtime; [2] for the conflicting disaster recovery definition; [3] for the glossary
  match.
- **Published structure:** [4]'s headings and prompts for the lean variant; [6]'s fourteen numbered sections in two
  parts, and [7]'s requirement that they be covered, for the Disaster Recovery section; [13]'s documentation set as a
  second government structure; [1]'s Activation and Notification, Recovery and Reconstitution phases.
- **Activation and its authority:** [1] (activation criteria, a designated authority, one person with a successor);
  [6] 4.3 (who makes the activation decision); [13] (a nominated team member activates and stands down); [9] (those
  "who have authority to declare a disaster").
- **Recovery objectives and strategies:** [22], [24] and [26] define RTO and RPO consistently with [1]; [23] orders
  four strategies "in increasing order of cost and complexity, and decreasing order of RTO and RPO" and warns against
  a strategy "more stringent than it needs to be".
- **Testing and exercising:** [9]'s four test types, its "Unmanned recovery testing" rule and its independent
  observer; [1]'s exercise types and after action report; [25]'s three criteria, "data integrity, recovery time
  objective (RTO), and recovery point objective (RPO)"; [26]'s "Include all of the human processes in your drills";
  [28]'s restore strategy; [13]'s debrief and lessons learnt log.
- **Keeping it current:** [1]'s review elements and "Certain elements, such as contact lists, will require more
  frequent reviews."; [9]'s change list and "living" document; [13]'s review after an exercise or incident; [30]'s
  update on "any material change".
- **The gap sources:** [29], [30], [31] and [32], routed below.

**How it fails, as sourced, and nothing more:**

- **Neglect, because disasters are rare.** [16]: "Since disasters happen so rarely, management often ignores the
  disaster recovery planning process."
- **Disaster recovery bolted on late.** [28]: "I think a lot of DR is an afterthought".
- **Backups nobody has restored.** [28]: "If you have backups, but you haven't tested restoring them, you don't really
  have backups." [24]: "It isn't enough just to have a plan for backing up or archiving your data."
- **The rarely used path breaks first.** [28]: "Parts of the system that are only used in disasters need the most
  testing, or they'll fail you when you need them."
- **A test that does not exercise the people who will recover.** [9]'s "Unmanned recovery testing" sentence; [26]'s
  instruction to include "all of the human processes".
- **Dependency deadlock during recovery.** [28]: "After an outage, you can end up with a deadlock: two systems that
  each can't start until the other is running and providing some functionality."
- **Stale contacts and documentation.** [1] on contact lists; [28]: recovery exercises reveal "that the documentation
  for the process is missing or out of date".
- **The plan unreachable during the outage.** [31] asks for "a hard copy of the plan and an offline version" of a
  response plan; [29] asks organizations to "strongly consider multiple redundant media" for essential records. No
  source in this research describes this failure as observed, so it is a precaution, not a measured failure.

**What this bundle must not say:** that the AWS whitepaper states disaster recovery must not stand alone (it does
not); that the 2003 FFIEC booklet is the current or the previous edition; that ISO 22301 or ISO/IEC 27031 contains
any particular clause; that every source treats disaster recovery as a section of the plan; that the plan's author
usually runs it, or usually does not; that immutable backups are settled practice; that FEMA's 2013 circular is
current guidance; or that any failure mode above is "the most common". No source in this research measured how often
any of them happens.

**The section design, as the research moved it from the spec.** The spec's section names and order stand: eight in
lean, and full inserts Disaster Recovery before Review Trigger. The research adds content to five of them, each homed
in an existing section rather than added as a new one:

- **Purpose and Scope** (lean): the business covered, what counts as a disruption here, and where the disaster
  recovery plan lives if it is a separate document ([4], [1]). In lean this is the pointer contested item 1 allows.
- **Business Continuity Team and Roles** (lean): the team roster ([4]), roles by job title rather than by name
  ([6] 9.1, [29]), the person with authority to activate and a named successor ([1]), and delegations that take
  effect "when normal channels of direction are disrupted" ([29]).
- **Business Impact Analysis Summary** (lean, a table): each critical process with its RTO and RPO, drawn from a
  separate analysis ([1], [4], [7]), and the systems and suppliers it depends on ([22], [30], [32]). It carries the
  analysis's results, never the worksheet.
- **Continuity Strategies and Manual Workarounds** (lean): how each critical process keeps running without its
  systems ([4]), at a recovery level chosen against cost ([23], [24]).
- **Activation and Incident Management** (lean): activation criteria stated in advance ([1]), who declares ([1], [6],
  [13]), who is told and in what order, including customers and regulators where the organization owes them notice
  ([29], [30]), and the condition for standing down ([13], [29], and NIST's deactivation in [1]).
- **Training, Testing and Exercising** (lean, a table): the exercise schedule and type ([9], [1], [19]), what each one
  validates, who observes ([9]), and each finding as an owned, dated corrective action ([29], [1], [13]).
- **Plan Administration** (lean): vendors and contractors, revision history and distribution ([4]), and where copies
  are kept so the plan can be reached when the systems it protects are down ([31], [29]).
- **Disaster Recovery** (full only): the recovery strategy for each critical system ([6], [23]); backup and offsite
  storage, including offline copies ([6], [31]); recovery procedures written so another trained person can follow
  them ([6], [1]); the order of recovery across dependent systems ([28], [22]); verifying restored data before
  service resumes ([25], [29], and NIST's reconstitution in [1]); and the recovery test ([6], [25]). This collapses
  SIMM 5325-A's fourteen sections into fewer headings, which is the library's grouping, not SIMM's.
- **Review Trigger** (lean, contract-mandated): a named owner and conditions: a change in people, suppliers, systems,
  facilities or the business ([9], [1], [30]); a change to the Business Impact Analysis ([1]); an activation; and an
  exercise or test finding ([13]). Where a regulator or policy requires an annual exercise, it appears as a floor
  under those conditions, not as the trigger itself (contested item 3).

**Gap-question candidates, routed by decision procedure 12:**

- **Admitted to the templates, each homed in an existing section above:** delegation of authority and succession by
  position title ([29]); stand-down criteria ([29], [13], [1]); communications to customers and regulators where owed
  ([29], [30]); suppliers as named dependencies, not only as contacts ([30], [32]); plan copies reachable offline
  ([31], [29]); exercise findings as owned, dated corrective actions ([29]); offline backups in the Disaster Recovery
  section ([31]).
- **To the guide, as a rubric row or anti-pattern:** a restore that has never been tested ([28], [25], [26]); high
  availability mistaken for a recovery plan ([26], [21]); an exercise that leaves out the people ([26], [9]); the plan
  kept only on the systems it protects ([31]).
- **Declined:** a separate assumptions and out-of-scope section, because the gap dimension found no primary or
  standards source that asks for one; a separate regulatory notification section, because the duty is binding only in
  some sectors ([30] binds FINRA's member firms), so it is folded into the communications line of Activation; and
  immutable storage as a recommendation (contested item 7).

**Teaching points the templates, guide and example must stay consistent with:**

- **The plan keeps business processes going; disaster recovery recovers the systems they use** ([1], [24], [6]).
- **The Business Impact Analysis is upstream. The plan carries its results, not the analysis** ([1], [4], [7]).
- **Activation is a decision made in advance:** stated criteria, a named authority, a named successor, and a condition
  for standing down ([1], [13], [29]).
- **Recovery procedures are written so that someone other than their author could follow them** ([1], [6]). That is a
  design requirement, not a claim about who usually runs them.
- **A backup is not a recovery until a restore has been tested**, judged on data integrity, RTO and RPO ([28], [25],
  [26]).
- **An exercise produces findings, and the findings change the plan** ([1], [13], [29]).
- **High availability is not a recovery plan** ([26], [21]).
- **The review trigger is a set of conditions with an owner; an annual exercise is a floor, not the trigger**
  ([9], [13], [1]; contested item 3).

**The example.** The Acme Analytics **Platform team's business continuity plan**, the instrument the
production readiness review example names without showing. `production-readiness-review_example.md:85` says the
`saved_view` table "lives in the shared main Postgres database" and that "Backup and disaster recovery for that
database is Platform's own standing responsibility, reviewed under Platform's own instrument, and is not duplicated
here", and line 74 marks the review's own "Data and backup, disaster recovery" criterion Not Applicable on that
ground. **The plan must therefore exist by 2026-08-22**, the review's date: its revision history carries an entry on
or before that date, and it never says the review found no plan. **The owner is Dana Osei (Staff Engineer,
Platform)**, the title six examples give consistently (for example `sdd_example.md:5`, `production-readiness-review_example.md:54`).
**The reviewer is Ines Halvorsen (Engineer, SRE)**, who appears in only one example, the production readiness review,
as its decision authority. Nothing earlier connects SRE to Platform, so the example states why SRE reviews: the
review on 2026-08-22 decided whether SRE takes standing ownership of `dashboard-service`, which depends on Platform's
database. **The
example sets its own recovery figures and labels them illustrative**, because no RTO, RPO, backup, failover or outage
fact exists anywhere in the thread. **It introduces the list of services that depend on the shared database itself**,
because no file enumerates them beyond `saved_view`, and it names `dashboard-service` as one of them. **It cites no
risk-register or RAID-log row**, because none concerns the database, a backup or an outage. **It cites no build or
release number**, following the production readiness review example's convention, and refers only to dated events.
It must not restate the review's Readiness Criteria rows, the runbook's entitlement-audit procedure or any risk
register row. Dates it may sit among: the definition of done updated 2026-07-24, the runbook 2026-07-28, the
definition of ready 2026-07-29, and the production readiness review 2026-08-22. **The templates' GOOD and WEAK text
must use a different organization, system and disruption**: grep the drafted templates for Acme, Platform, Postgres,
`saved_view`, Dana Osei and Ines Halvorsen before review.

---

## Sources

### CANON: THE FEDERAL DEFINITIONS AND THE READY BUSINESS TEMPLATE

**[1] Swanson, Bowen, Phillips, Gallup, Lynes (NIST), "Contingency Planning Guide for Federal Information Systems," NIST Special Publication 800-34 Rev. 1, May 2010.** standards. **fetched-and-verified.**
`https://nvlpubs.nist.gov/nistpubs/legacy/sp/nistspecialpublication800-34r1.pdf`
Supports: The definitions of the business continuity plan, disaster recovery plan, contingency plan, continuity of operations plan, business impact analysis, RTO, RPO and maximum tolerable downtime; how the plan types relate (a disaster recovery plan may support a business continuity plan, and only addresses relocation); the contingency plan template's activation, recovery and reconstitution phases; review cadence and the elements a review covers; the BIA as an input to the plans; exercise types and the after action report; and roles, where activation sits with a designated senior authority while the ISCP Coordinator writes the plan and typically manages its execution (contested item 4)
Quotable: "The documentation of a predetermined set of instructions or procedures that describe how an organization's mission/business processes will be sustained during and after a significant disruption."
Quotable: "A written plan for recovering one or more information systems at an alternate facility in response to a major hardware or software failure or destruction of facilities."
Quotable: "Management policy and procedures designed to maintain or restore business operations, including computer operations, possibly at an alternate location, in the event of emergencies, system failures, or disasters."
Quotable: "An analysis of an information system's requirements, functions, and interdependencies used to characterize system contingency requirements and priorities in the event of a significant disruption."
Quotable: "A predetermined set of instructions or procedures that describe how an organization's mission essential functions will be sustained within 12 hours and for up to 30 days as a result of a disaster event before returning to normal operations."
Quotable: "The amount of time mission/business process can be disrupted without causing significant harm to the organization's mission."
Quotable: "The point in time to which data must be recovered after an outage."
Quotable: "The overall length of time an information system's components can be in the recovery phase before negatively impacting the organization's mission or mission/business processes."
Quotable: "The DRP applies to major, usually physical disruptions to service that deny access to the primary facility infrastructure for an extended period. A DRP is an information system-focused plan designed to restore operability of the target system, application, or computer facility infrastructure at an alternate site after an emergency."
Quotable: "The DRP only addresses information system disruptions that require relocation."
Quotable: "A DRP may support a BCP or COOP plan by recovering supporting systems for mission/business processes or mission essential functions at an alternate location."
Quotable: "The BCP focuses on sustaining an organization's mission/business processes during and after a disruption."
Quotable: "Because mission/business processes use information systems (ISs), the business continuity planner must coordinate with information system owners to ensure that the BCP expectations and IS capabilities are matched."
Quotable: "Continuity planning normally applies to the mission/business itself; it concerns the ability to continue critical functions and processes during and after an emergency event. Contingency planning normally applies to information systems, and provides the steps needed to recover the operation of all or part of designated information systems at an existing or new location in an emergency."
Quotable: "Provides procedures for sustaining mission/business operations while recovering from a significant disruption."
Quotable: "Provides procedures for relocating information systems operations to an alternate location."
Quotable: "Activated after major system disruptions with long-term effects."
Quotable: "Information systemfocused plan that activates one or more ISCPs for recovery of individual systems."
Quotable: "The ISCP Coordinator develops the strategy in cooperation with other functional and resource managers associated with the system or the mission/business processes supported by the system. The ISCP Coordinator also typically manages development and execution of the contingency plan."
Quotable: "The procedures for execution of such a capability shall be documented in a formal contingency plan by the Information Systems Contingency Plan (ISCP) Coordinator and must be reviewed annually and updated as necessary by the ISCP Coordinator."
Quotable: "The ISCP should be activated if one or more of the activation criteria for that system are met. If an activation criterion is met, the designated authority should activate the plan."
Quotable: "The designated authority (typically a senior manager or CIO) has the authority to activate the contingency plan. That authority may vary based on the organization or system, but the individual with this authority should be designated clearly in the plan. Only one individual should have this authority, and a successor should be clearly identified to assume that responsibility if necessary."
Quotable: "A senior management official, such as the CIO, has the ultimate authority to activate the plan and to make decisions regarding spending levels, acceptable risk, and interagency coordination. The senior management official typically leads the management team."
Quotable: "Leadership roles should include an ISCP Director, who has overall management responsibility for the plan, and an ISCP Coordinator, who is responsible to oversee recovery and reconstitution progress, initiate any needed escalations or awareness communications, and establish coordination with other recovery and reconstitution teams as appropriate."
Quotable: "The following persons or roles may activate the ISCP if one or more of these criteria are met: Establish one or more roles that may activate the plan based on activation criteria. Authorized persons may include the system or business owner, or the operations point of contact (POC) for system support."
Quotable: "Provide a statement in accordance with the agency's contingency planning policy to affirm that the ISCP is complete and has been tested sufficiently. The statement should also affirm that the designated authority is responsible for continued maintenance and testing of the ISCP."
Quotable: "I further attest that this ISCP for {system name} will be tested at least annually."
Quotable: "As a general rule, the plan should be reviewed for accuracy and completeness at an organization-defined frequency or whenever significant changes occur to any element of the plan."
Quotable: "When a significant change occurs, the BIA should be updated with the new information to identify new contingency requirements or priorities."
Quotable: "An up-to-date ISCP is essential for successful ISCP operations. As a general rule, the ISCP should be reviewed for accuracy and completeness at least annually, as well as upon significant changes to any element of the ISCP, system, mission/business processes supported by the system, or resources used for recovery procedures."
Quotable: "The BIA helps identify and prioritize information systems and components critical to supporting the organization's mission/business processes."
Quotable: "The BIA enables the ISCP Coordinator to characterize the system components, supported mission/business processes, and interdependencies."
Quotable: "Results from the BIA should be appropriately incorporated into the analysis and strategy development efforts for the organization's COOP, BCPs, and DRP."
Quotable: "The BIA is the first source for determining resiliency and contingency planning strategies."
Quotable: "Tabletop Exercises. Tabletop exercises are discussion-based exercises where personnel meet in a classroom setting or in breakout groups to discuss their roles during an emergency and their responses to a particular emergency situation... A tabletop exercise is discussion-based only and does not involve deploying equipment or other resources."
Quotable: "Functional Exercises. Functional exercises allow personnel to validate their operational readiness for emergencies by performing their duties in a simulated operational environment... Functional exercises vary in complexity and scope, from validating specific aspects of a plan to full-scale exercises that address all plan elements."
Quotable: "For high-impact systems, a full-scale functional exercise at an organization-defined frequency should be conducted. The full-scale functional exercise should include a system failover to the alternate location... The test should also include a full recovery and reconstitution of the information system to a known state."
Quotable: "There are several methods for testing and/or exercising contingency plans to identify potential weaknesses (e.g., checklist, walk-through/tabletop, simulation; parallel, full interrupt)."
Quotable: "Results of the test are documented in an After Action Report, and Lessons Learned are developed for updating information in the ISCP."
Quotable: "Finalize after action report and lessons learned... Update ISCP based on lessons learned... Approve and distribute updated version of ISCP."
Quotable: "Certain elements, such as contact lists, will require more frequent reviews."
Quotable: "Responsibility for the planning process generally falls under the auspice of the Information System Contingency Plan Coordinator, or ISCP Coordinator, who is typically a functional or resource manager within the organization. The ISCP Coordinator develops the strategy in cooperation with other functional and resource managers... The ISCP Coordinator also typically manages development and execution of the contingency plan."
Quotable: "Activities and procedures are written at a level that an appropriately skilled technician can recover the system without intimate system knowledge."
Quotable: "Activation of the ISCP occurs after a disruption or outage that may reasonably extend beyond the RTO established for a system."
Quotable: "This phase consists of two major activities: validating successful reconstitution and deactivation of the plan."
Quotable: "At a minimum, plan reviews should focus on the following elements:"
Quotable: "Names and contact information of team members"
Quotable: "Vital records (electronic and hardcopy)"

**[2] NIST, "disaster recovery plan (DRP)" entry, Computer Security Resource Center (CSRC) Glossary.** standards. **fetched-and-verified.**
`https://csrc.nist.gov/glossary/term/disaster_recovery_plan`
Supports: A second, conflicting CNSSI 4009-2022 definition of DRP that scopes recovery to the original facility rather than an alternate one
Quotable: "Management policy and procedures used to guide an enterprise response to a major loss of enterprise capability or damage to its facilities. The DRP is the second plan needed by the enterprise risk managers and is used when the enterprise must recover (at its original facilities) from a loss of capability over a period of hours or days."
Quotable: "Management policy and procedures used to guide an enterprise response to a perceived loss of mission capability. The Contingency Plan is the first plan used by the enterprise risk managers to determine what happened, why, and what to do. It may point to the continuity of operations plan (COOP) or disaster recovery plan (DRP) for major disruptions."
Quotable: "A written plan for processing critical applications in the event of a major hardware or software failure or destruction of facilities."

**[3] NIST, "business continuity plan (BCP)" entry, Computer Security Resource Center (CSRC) Glossary.** standards. **fetched-and-verified.**
`https://csrc.nist.gov/glossary/term/business_continuity_plan`
Supports: Confirms the glossary carries no definition for BCP beyond the one SP 800-34 already supplies; no second, conflicting source exists for BCP the way one exists for DRP
Quotable: "The documentation of a predetermined set of instructions or procedures that describe how an organization's mission/business processes will be sustained during and after a significant disruption."

**[4] FEMA / Ready Business, "Business Continuity Plan" fill-in PDF template.** primary. **fetched-and-verified.**
`https://www.ready.gov/sites/default/files/2020-03/business-continuity-plan.pdf`
Supports: The template's section headings and table/field labels in printed order; what it says (and does not say) about who writes, approves and activates the plan
Quotable: "Program Administration"
Quotable: "Business Continuity Organization"
Quotable: "Business Impact Analysis"
Quotable: "Business Continuity Strategies & Requirements"
Quotable: "Manual Workarounds"
Quotable: "Incident Management"
Quotable: "Training, Testing & Exercising"
Quotable: "Program Maintenance and Improvement"
Quotable: "References to Related Policies & Procedures"
Quotable: "Vendors & Contractors"
Quotable: "Revision History"
Quotable: "Plan Distribution & Access"
Quotable: "Schedule, triggers, and assignments for the periodic review of the business continuity and IT disaster recovery plan"
Quotable: "Information Technology Disaster Recovery Plan (if not included in the business continuity plan)"
Quotable: "The Plan will be distributed to members of the business continuity team and management. A master copy of the document should be maintained by the business continuity team leader."
Quotable: "Insert results of Business Impact Analysis"
Quotable: "Identify Recovery Time Objectives for business processes and information technology"
Quotable: "Identify Recovery Point Objective for data restoration"
Quotable: "lines of authority, succession of management, and delegation of authority"
Quotable: "Business continuity plan activation"

**[5] FEMA / Ready Business, "Business Continuity Planning" page, Ready.gov.** primary. **fetched-and-verified.**
`https://www.ready.gov/business-continuity-plan`
Supports: The short page's own characterization of a BCP; confirms the page carries no language naming who has authority to activate the plan
Quotable: "Organize a business continuity team and compile a business continuity plan to manage a business disruption."

### STRUCTURE AND CADENCE: CALIFORNIA, THE FFIEC AND UK GOVERNMENT

**[6] California Department of Technology, Office of Information Security - "Technology Recovery Plan Instructions" (SIMM 5325-A, March 2023).** standards. **fetched-and-verified.**
`https://www.cdt.ca.gov/wp-content/uploads/policy/simm/SIMM-5325-A-Technology-Recovery-Plan-Instructions.pdf`
Supports: The numbered section/subsection structure that models the bundle's Disaster Recovery section (question a), and the single testing-frequency statement in this source (question b)
Quotable: "SIMM number change, change "agency" to "state entity", change "disaster recovery" to "technology recovery", and change references to other related SIMM documents."
Quotable: "SECTION 1: MINIMUM TRP REQUIREMENTS"
Quotable: "1.0 STATE ENTITY ADMINISTRATIVE INFORMATION"
Quotable: "2.0 CRITICAL BUSINESS FUNCTIONS/APPLICATIONS"
Quotable: "3.0. CRITICAL INFRASTRUCTURE"
Quotable: "4.0 RECOVERY STRATEGY"
Quotable: "5.0 BACKUP AND OFFSITE STORAGE PROCEDURES"
Quotable: "6.0 TECHNOLOGY AND INFRASTRUCTURE RECOVERY PROCEDURES"
Quotable: "7.0 DATA CENTER SERVICES"
Quotable: "8.0 RESOURCE REQUIREMENTS"
Quotable: "9.0 ASSIGNMENT OF RESPONSIBILITY"
Quotable: "10.0 CONTACT INFORMATION"
Quotable: "11.0 TESTING"
Quotable: "SECTION 2: SUPPLEMENTAL TRP REQUIREMENTS"
Quotable: "1.0 DAMAGE RECOGNITION AND ASSESSMENT"
Quotable: "2.0 MOBILIZATION OF PERSONNEL"
Quotable: "3.0 PRIMARY SITE RESTORATION AND RELOCATION"
Quotable: "1.1 An executive summary that serves as a guide to the structure of the plan, the procedures for updating (plan maintenance) and distributing the plan, and a description of the state entity's test and awareness programs."
Quotable: "5.1 Backup and retention schedules and procedures that are critical to the recovery of a state entity's critical business applications and data, and critical infrastructure facilities, systems, controls and information."
Quotable: "9.1 Distinct management and personnel assignment of responsibilities must be clearly designated within the technology recovery plan. Within procedures, job titles (rather than the names of individuals) should be used to assign responsibility as it lessens maintenance on procedures as personnel changes."
Quotable: "4.3 A description of how the incident response plan and strategy interplays with TRP and strategy to include when an incident is declared a disaster and the TRP procedures are initiated, and identification of individual(s) responsible for making the TRP activation decision."
Quotable: "11.1 A description of the annual technology recovery test(s) performed, including how the test(s) were conducted, high level timeframes for each test, and the level of testing appropriate to the complexity of the system(s), program(s), process(es), or organization(s) being recovered. Examples of testing may include tabletop exercises, data recovery testing, forced testing (actual recovery due to an unplanned outage or failure), and/or full plan testing"
Quotable: "The TRP is just one portion of contingency planning and business continuity. A complete business continuity plan includes emergency/disaster management, business resumption, and technology recovery plans."
Quotable: "6.4 The procedures should be detailed enough so that another trained information technology professional would be able to recover the state entity's infrastructure should those with primary responsibility be unavailable during the recovery process."

**[7] California Department of General Services - State Administrative Manual (SAM) Section 5325.1, "Technology Recovery Plan" (revised 10/2025).** standards. **fetched-and-verified.**
`https://www.dgs.ca.gov/Resources/SAM/TOC/5300/5325-1/10-29-2025`
Supports: The governing policy clause that requires the TRP, ties it to the BIA and Continuity Plan, and its one explicit cadence statement (annual filing)
Quotable: "As a sub-set of a state agency or entity's Continuity Plan, the Technology Recovery Plan (TRP) is activated immediately after a significant disruption or disaster and focuses on priority recovery and restoration of systems, services, and data supporting mission and business essential functions identified as part of a Business Impact Analysis (BIA)."
Quotable: "The TRP must be derived from the state agency or entity's BIA and Continuity Plan."
Quotable: "Each state agency or entity must annually file a copy of the following:"
Quotable: "Each state agency or entity TRP must cover, at a minimum, the sections which are listed and described in SIMM 5325-A, Technology Recovery Plan Instructions."

**[8] California Department of Technology - "Summary of What Changed in SIMM September 2013".** standards. **fetched-and-verified.**
`https://www.cdt.ca.gov/wp-content/uploads/2017/02/Summary_of_What_Changed_in_SIMM_September_2013.pdf`
Supports: Confirms the exact renaming event: SIMM 65A "Disaster Recovery Documentation for Agencies Preparation Instructions" became SIMM 5325A "Technology Recovery Plan Instructions" under TL 13-04, alongside the companion certification renumbering (65B to 70B became 5325B)
Quotable: "Deleted SIMM Section 65A Disaster Recovery Documentation for Agencies Preparation Instructions and replaced it with SIMM Section 5325A Technology Recovery Plan Instructions."
Quotable: "Deleted SIMM Section 70B Agency Disaster Recovery Plan Certification and replaced it with SIMM Section 5325B Technology Recovery Program Certification."

**[9] Federal Financial Institutions Examination Council - "Business Continuity Planning" IT Examination Handbook booklet (March 2003), retrieved via an FDIC mirror.** standards. **fetched-and-verified.**
`https://fdic.gov/system/files/2024-07/bcp.pdf`
Supports: Every testing/review-frequency statement, every update-trigger statement, the four test types and what makes a test insufficient, and who should observe test results (questions b, c, d). This is the superseded 2003 edition, not the current 2019 BCM booklet
Quotable: "Testing the BCP at least annually; Subjecting the BCP to independent audit and review; and Updating the BCP based upon changes to personnel and the internal and external environments."
Quotable: "Management should ensure recovery testing is conducted at least annually, or more frequently, depending on the operating environment and criticality of the applications and business functions."
Quotable: "Approving the BCP on an annual basis; and"
Quotable: "The plan should be reviewed by senior management, the planning team or coordinator, team members, internal audit, and the board of directors at least annually."
Quotable: "The board of directors reviews and approves the plan(s) annually and after significant changes and updates."
Quotable: "Determine if the board reviews and approves the written BCP(s) and testing results at least annually and documents these reviews in the board minutes."
Quotable: "As part of the review process, the testing plan should be revised to account for any changes to key personnel, policies, procedures, facilities, equipment, outsourcing relationships, vendors, or other components that impact a critical business function."
Quotable: "Management should update BCPs as business processes change."
Quotable: "A BCP is a “living” document; changing in concert with changes in the business activities it supports."
Quotable: "the team, or coordinator should contact business unit managers throughout the financial institution at regular intervals to assess the nature and scope of any changes to the institution’s business, structure, systems, software, hardware, personnel, or facilities."
Quotable: "Orientation/Walk-through"
Quotable: "Tabletop/Mini-drill"
Quotable: "Functional Testing"
Quotable: "Full-scale Testing"
Quotable: "Unmanned recovery testing, where back-up tapes are sent to the recovery site to be run by service provider employees, is not a sufficient test of an institution's BCP."
Quotable: "The involvement and oversight of independent staff such as auditors will help to ensure the validity of the testing process and the accuracy of the reporting."
Quotable: "the audit department or other independent party should directly observe tests of the BCP."
Quotable: "The board should receive and carefully review audit reports on the effectiveness of the institution's process that identify any areas of weakness."
Quotable: "Determine if audit involvement in the business continuity program is effective, including: • Audit coverage of the business continuity program; • Assessment of business continuity preparedness during line(s) of business reviews; • Audit participation in testing in an observer role; and • Audit review of testing plans and results."
Quotable: "Clearly defines responsibilities and decision-making authorities for designated teams and/or staff members, including those who have authority to declare a disaster"
Quotable: "Typically, the business continuity coordinator or team facilitates the identification of risk and the development of risk mitigation strategies across business areas."

**[10] Board of Governors of the Federal Reserve System - SR 19-13, "FFIEC Information Technology Examination Handbook" (transmittal letter, December 2019).** standards. **fetched-and-verified.**
`https://www.federalreserve.gov/supervisionreg/srletters/sr1913.htm`
Supports: Confirms the 2019 Business Continuity Management booklet exists, replaced the February 2015 edition, and names its topic headings. It is a two-paragraph transmittal letter, not the booklet itself, so it carries no testing-frequency language of its own
Quotable: "The Federal Financial Institutions Examination Council (FFIEC) has revised the February 2015 version of the "Business Continuity Management" (BCM) booklet of the FFIEC Information Technology Examination Handbook (IT Handbook)."
Quotable: "This booklet discusses BCM governance and its related components, including resilience; strategies, and plan development; training and awareness; exercises and tests; maintenance and improvement; and reporting for the board of directors."

**[11] FDIC - Financial Institution Letter FIL-71-2019, "Updated FFIEC IT Examination Handbook - Business Continuity Management Booklet" (archived copy).** standards. **fetched-and-verified.**
`https://archive.fdic.gov/view/fdic/8792/fdic_8792_DS1.pdf`
Supports: That the 2019 Business Continuity Management booklet replaced a February 2015 booklet, and FDIC's own summary of the booklet's orientation. It is a regulator's transmittal letter, not the booklet, so it settles no cadence question (contested item 3)
Quotable: "The change from business continuity planning to business continuity management reflects the expanded role information technology (IT) plays in supporting business operations and meeting customer expectations."
Quotable: "The changes do not impose new requirements on examined entities."
Quotable: "The booklet replaces the Business Continuity Planning booklet issued in February 2015."

**[12] GOV.UK (Ministry of Justice / HMPPS) - "HMPPS business continuity policy framework" publication page.** standards. **fetched-and-verified.**
`https://www.gov.uk/government/publications/hmpps-business-continuity-policy-framework`
Supports: The publication's annex list (nine annexes: five BIA/BCP templates by site type, plus supplementary guidance, an incident-reporting form, an exercise-plan template and a lessons-learnt-log template) and the one-paragraph policy summary tying the framework to ISO 22301
Quotable: "This policy framework sets out the arrangements necessary to ensure Business Continuity Management (BCM) is performed in accordance with ISO 22301 as required by Cabinet Office."
Quotable: "All providers of HMPPS services (including CRCs and privately operated establishments) are required to produce and maintain Business Continuity Plans (BCPs) to ensure critical business activities and locations remain operational and that a prompt and efficient recovery of ‘business as usual’ activities takes place in the event of an incident or other disruption affecting premises or resources (including both staff and information)."
Quotable: "HMPPS business continuity policy framework"
Quotable: "Annex A: BIA/BCP Template, Prisons"
Quotable: "Annex F: Supplementary Guidance to aide completion of BIA/BC templates"
Quotable: "Annex G: BC Incident Reporting Form"
Quotable: "Annex H: Exercise plan Template"
Quotable: "Annex I: Lessons Learnt log template"

**[13] HM Prison & Probation Service / Ministry of Justice - "HMPPS Business Continuity and Resilience Policy Framework" (Re-Issue 06 March 2023; the PDF the landing page links).** standards. **fetched-and-verified.**
`https://assets.publishing.service.gov.uk/media/640611b48fa8f527f2ef9658/hmpps-business-continuity-policy-framework.pdf`
Supports: Its own plan structure and annexes, its review/exercise-frequency language, and the clearest direct statement in the whole research set on who activates a plan versus who writes and maintains it (questions e and f)
Quotable: "Policy Name: HMPPS Business Continuity and Resilience Policy Framework"
Quotable: "1. Purpose"
Quotable: "2. Evidence"
Quotable: "3. Definition"
Quotable: "4. Outcomes"
Quotable: "5. Roles & Responsibilities"
Quotable: "6. Business Continuity Documentation to be completed by each site/regional/team SPOC (Single Point of Contact)"
Quotable: "7.0 BC Incident reporting"
Quotable: "8.0 Validation & Assurance"
Quotable: "9. Annexes"
Quotable: "6.1 Key Contacts and Locations/ Functions"
Quotable: "6.2 Communication & Activation"
Quotable: "6.3 Business Impact Assessment (BIA)"
Quotable: "6.4 Business Continuity Plans (BCP)"
Quotable: "6.5 Decision Log & Outcomes"
Quotable: "This gives a flow chart of how the plan will be activated in response to an incident causing significant disruption to normal service/business particularly the delivery of critical functions/ activities. A member of the nominated Business Continuity team will normally activate and stand down the plans."
Quotable: "5.5 Local Business Continuity leads"
Quotable: "Complete the Business Continuity documentation for their HMPPS locations and business units and ensure they are reviewed least annually or following an incident or exercise"
Quotable: "Test at least one local BCP annually as a minimum"
Quotable: "For Business Continuity Plans to remain effective they must be regularly reviewed and tested. Staff with responsibility for maintaining BCPs must review and test their plans annually. At least one risk/scenario must be tested every 12 months as a minimum by means of a desktop exercise to ensure that they meet the requirements of this policy framework"
Quotable: "8.1 At least one risk/scenario identified in each plan must be tested annually as a minimum through exercising."
Quotable: "8.3 The Business Continuity documentation must be reviewed annually, following an exercise and/or BC incident."
Quotable: "8.4 Debrief sessions must be held following an exercise and lessons learnt log completed."
Quotable: "Annex A BIA/BCP template to be used by Prison establishments"
Quotable: "Annex F Supplementary Guidance for completion of Annex A-D BC documentation"
Quotable: "Annex G Business Continuity Incident Reporting Form"
Quotable: "Annex H Exercise Plan template"
Quotable: "Annex I Lessons Learnt Log template"

### PRACTICE: PROFESSIONAL BODIES, POLICY TEMPLATES AND EXERCISING

**[14] BCI (Kieran Matthews) - "Good Practice Guidelines 7.0: A new focus on the Business Continuity Management System" (BCI news article, 12 Oct 2023).** practitioner. **fetched-and-verified.**
`https://www.thebci.org/news/bci-gpg-edition-7-0-a-new-focus-on-the-bcms.html`
Supports: (a) names PP1 only and its new title; the operational-cycle/management-cycle nesting of the plan inside a programme; (b) the professional body's own move away from plan/lifecycle-centric language
Quotable: "The new GPG consists of six Professional Practices, split into two management practices and four technical practices, which provide a structure to be used in the development of a Business Continuity Management System."
Quotable: "the previously termed 'Business Continuity Management Lifecycle' has been replaced by the more scalable and holistic term 'Business Continuity Management System'"
Quotable: "PP1 now renamed ‘Establishing a BCMS’ to highlight how it serves as the first stage in this process"
Quotable: "as more of an enabler to the creation of a Business Continuity Management System, but not the primary focus of the entire Business Continuity Management System"
Quotable: "the 'operational cycle' consisting of the business impact analysis (BIA), strategy, plans, and exercising, which sits within a bigger 'management cycle' (i.e. setting up your policy, your performance review, etc)"
Quotable: "the title of PP1 has been revised to ‘Establishing a Business Continuity Management System’ rather than the 2018 edition’s ‘Policy and Programme Management’"
Quotable: "[PP1 sets out] the framework of the Business Continuity Management System... Everything that comes after supports this framework"

**[15] DRI International (DRII) - "Professional Practices" resource page (2023 revision landing page, public Executive Summary section).** practitioner. **fetched-and-verified.**
`https://drii.org/resources/professionalpractices`
Supports: (a) the ten Professional Practices' verbatim names and one-line objectives, including Practice 6 (plan development) and Practice 8 (exercise/test, assessment, maintenance); the full PP document body is gated behind login, so only the publicly visible Executive Summary/objectives list was read
Quotable: "Created and maintained by Disaster Recovery Institute (DRI) International, The Professional Practices for Business Continuity Management is a body of knowledge designed to assist in the development, implementation, and maintenance of business continuity programs."
Quotable: "1. Program Management"
Quotable: "3. Business Impact Analysis"
Quotable: "4. Business Continuity Strategies"
Quotable: "5. Incident Preparedness and Response"
Quotable: "6. Plan Development and Implementation"
Quotable: "Document plans to be used during an incident that will enable the entity to continue to function."
Quotable: "Define the exercise/testing criteria to validate that the plans will accomplish the desired goal."
Quotable: "8. Business Continuity Plan Exercise/Test, Assessment, and Maintenance"
Quotable: "Establish a business continuity plan exercise/test, assessment and maintenance program to maintain a state of readiness of the entity."
Quotable: "9. Crisis Communications"
Quotable: "Professional Practice One was changed from Program Initiation and Management to Program Management; Professional Practice Five was changed from Incident Response to Incident Preparedness and Response to emphasize the activities that are necessary to create an effective response plan; Professional Practice Eight was changed from Business Continuity Plan Exercise, Assessment, and Maintenance to Business Continuity Plan Exercise/Test, Assessment, and Maintenance for consistency; and Professional Practice Ten was changed from Coordination with External Agencies to Coordination with External Agencies and Resources."

**[16] SANS Institute / Consensus Policy Resource Community - "Disaster Recovery Plan Policy" (2014 policy template, SANS-hosted CDN copy; canonical SANS page now 404s).** practitioner. **fetched-and-verified.**
`https://assets.contentstack.io/v3/assets/blt36c2e63521272fdc/blt3cf8b9a0b2e45133/5e9ddb9ab1704560004196b5/disaster_recovery_plan_policy.pdf`
Supports: (d) the "management often ignores" failure mode; (f) the DRP's own required sub-plans, its own scope disclaimer, its stated relationship to the BCP, and its testing/review cadence
Quotable: "Since disasters happen so rarely, management often ignores the disaster recovery planning process."
Quotable: "The Disaster Recovery Plan is often part of the Business Continuity Plan."
Quotable: "This policy is directed to the IT Management Staff who is accountable to ensure the plan is developed, tested and kept up-to-date. This policy is solely to state the requirement to have a disaster recovery plan, it does not provide requirement around what goes into the plan or subplans."
Quotable: "4.1 Contingency Plans The following contingency plans must be created: • Computer Emergency Response Plan... • Succession Plan... • Data Study... • Criticality of Service List... • Data Backup and Restoration Plan... • Equipment Replacement Plan... • Mass Media Management"
Quotable: "Table top exercises should be conducted annually."
Quotable: "The plan, at a minimum, should be reviewed an updated on an annual basis."

**[17] SANS Institute - "Resilience Management Policy" (policy template, last updated February 2026; the text was read from the PDF the page links as "Download PDF", https://sansorg.egnyte.com/dd/RvJ6hPJjv37v).** practitioner. **fetched-and-verified.**
`https://www.sans.org/information-security-policy/resilience-management-policy/`
Supports: (d)/(f) current (2026) SANS framing of BCP/DR as a safeguard inside a broader resilience/incident-management policy, and how little it specifies about BCP content compared to the 2014 DRP policy
Quotable: "Our Resilience Management Policy aims to establish a comprehensive framework for ensuring the availability, resilience, and timely recovery of our critical systems, data, and networks in the event of a cybersecurity incident or disruption."
Quotable: "Maintain a documented Business Continuity and Disaster Recovery (BCP / DR) program that documents the organization's safeguards to address business continuity."
Quotable: "Regularly perform tabletop exercises with key stakeholders to test the organization's Business Continuity and Disaster Recovery (BCP / DR) and Incident Management (IM) plans."
Quotable: "Define a process the organization will use to update its Business Continuity and Disaster Recovery (BCP / DR) and Incident Management (IM) documentation after changes to its information technologies."
Quotable: "Ensure that the organization's documented Incident Management (IM) plan defines workforce members' leadership and decision-making responsibilities during a cybersecurity incident."

**[18] ISO - "ISO 22301:2019, Security and resilience - Business continuity management systems - Requirements", catalogue page only (the standard itself is paywalled and was not read).** standards. **fetched-and-verified.**
`https://www.iso.org/standard/75106.html`
Supports: (a)/(b), strictly limited to what the free catalogue page itself states: ISO frames the standard as governing a "documented management system," while its own marketing FAQ still uses plan-document language ("robust business continuity plan"). No claim about the standard's clause structure or requirements text is sourced from this page; that text is paywalled and was not read
Quotable: "ISO 22301 is the international standard for Business Continuity Management Systems (BCMS). It provides a framework for organizations to plan, establish, implement, operate, monitor, review, maintain, and continually improve a documented management system to protect against, reduce the likelihood of, and ensure recovery from disruptive incidents."
Quotable: "Organizations of all sizes seeking to establish a robust business continuity plan."

**[19] URM Consulting (Phillip Knight, Senior Consultant) - "Business Continuity Exercising" (blog, published 5 June 2025, based on a URM webinar).** vendor. **fetched-and-verified.**
`https://www.urmconsulting.com/blog/business-continuity-exercising`
Supports: (b) the plan-insufficient-without-exercising argument; (c) a second named taxonomy of exercise types and what exercising should produce (a learning outcome, not a pass/fail test); (e) incidental evidence that a crisis/incident management team, not necessarily the plan's author, runs tabletop exercises
Quotable: "However, having a BCP on paper is not enough. Your organisation’s resilience depends on whether those plans work in practice. Waiting for a real incident to test them is, of course, an extremely high-risk approach."
Quotable: "It is also important to understand that these activities are an exercise, not a test. Whilst the term ‘test’ implies a pass/fail outcome, there is no such binary judgement in exercising. Every BC exercise is a learning opportunity, and identifying a problem should not be considered a failure, but progress."
Quotable: "Technical tests Desktop documentation walkthroughs Walkthroughs Table-top simulation Full live exercises Building evacuation/redeployment test Communications testing."
Quotable: "Tabletop simulations are the most common format. These involve progressing through a realistic scenario, often with your crisis or incident management team, and simulating your response as the scenario unfolds."
Quotable: "Among the more intense exercise formats are full live exercises, which can involve restricting access to premises and mimicking a real crisis in real-time."
Quotable: "Finally, ISO 22301, the International Standard for Business Continuity Management Systems (BCMS), requires conformant organisations to conduct exercises."

### DISASTER RECOVERY IN PRACTICE: CLOUD PROVIDERS AND SITE RELIABILITY ENGINEERING

**[20] AWS - "Disaster Recovery of Workloads on AWS: Recovery in the Cloud" (whitepaper landing page).** vendor. **fetched-and-verified.**
`https://docs.aws.amazon.com/whitepapers/latest/disaster-recovery-workloads-on-aws/disaster-recovery-workloads-on-aws.html`
Supports: scope statement of the whitepaper and the publication-level framing of RTO/RPO; the body text here is thin (a landing page), and the per-question substance comes from the Introduction and the two Well-Architected pages below
Quotable: "This paper outlines the best practices for planning and testing disaster recovery for any workload deployed to AWS, and offers different approaches to mitigate risks and meet the Recovery Time Objective (RTO) and Recovery Point Objective (RPO) for that workload."

**[21] AWS - "Introduction" (Disaster Recovery of Workloads on AWS whitepaper).** vendor. **fetched-and-verified.**
`https://docs.aws.amazon.com/whitepapers/latest/disaster-recovery-workloads-on-aws/introduction.html`
Supports: (a) AWS's RPO/RTO definitions; (c) the relationship AWS states between DR and business continuity planning; (f) DR vs. availability/HA
Quotable: "Disaster recovery (DR) is an important part of your resiliency strategy and concerns how your workload responds when a disaster strikes (a disaster is an event that causes a serious negative impact on your business)."
Quotable: "This response must be based on your organization's business objectives which specify your workload's strategy for avoiding loss of data, known as the Recovery Point Objective (RPO), and reducing downtime where your workload is not available for use, known as the Recovery Time Objective (RTO)."
Quotable: "This approach helps your organization to maintain business continuity as part of Business Continuity Planning (BCP)."
Quotable: "Disaster recovery focuses on disaster events, whereas availability focuses on more common disruptions of smaller scale such as component failures, network issues, software bugs, and load spikes. The objective of disaster recovery is business continuity, whereas availability concerns maximizing the time that a workload is available to perform its intended business functionality. Both should be part of your resiliency strategy."

**[22] AWS Well-Architected Framework - REL13-BP01 "Define recovery objectives for downtime and data loss".** vendor. **fetched-and-verified.**
`https://docs.aws.amazon.com/wellarchitected/latest/framework/rel_planning_for_recovery_objective_defined_recovery.html`
Supports: (a) AWS's formal RTO/RPO definitions and the matrix/worksheet method for assigning them per workload, including dependency questions
Quotable: "Recovery Time Objective (RTO) is the maximum acceptable delay between the interruption of service and restoration of service."
Quotable: "Recovery Point Objective (RPO) is the maximum acceptable time after the last data recovery point."
Quotable: "When you set RTOs and RPOs for your workloads, you establish clear and measurable goals for recovery based on your business needs. Once you've set those goals, you can create disaster recovery (DR) plans that are tailored to meet them."
Quotable: "What are the recovery objectives and availability expectations of workloads that this one depends on (downstream)? ... What are the recovery objectives and availability expectations of workloads that depend on this one (upstream)?"

**[23] AWS Well-Architected Framework - REL13-BP02 "Use defined recovery strategies to meet the recovery objectives".** vendor. **fetched-and-verified.**
`https://docs.aws.amazon.com/wellarchitected/latest/framework/rel_planning_for_recovery_disaster_recovery.html`
Supports: (b) the four named AWS DR strategies and the cost-vs-RTO/RPO tradeoff; THE AWS SENTENCE recheck; (g) RDS/DynamoDB recovery mechanics (failback, promoting read replicas, point-in-time restore via AWS Backup)
Quotable: "Define a disaster recovery (DR) strategy that meets your workload's recovery objectives. Choose a strategy such as backup and restore, standby (active/passive), or active/active."
Quotable: "When architecting a DR strategy across multiple Regions, you should choose one of the following strategies. They are listed in increasing order of cost and complexity, and decreasing order of RTO and RPO."
Quotable: "Backup and restore (RPO in hours, RTO in 24 hours or less): Back up your data and applications into the recovery Region. Using automated or continuous backups will permit point in time recovery (PITR), which can lower RPO to as low as 5 minutes in some cases."
Quotable: "Pilot light (RPO in minutes, RTO in tens of minutes): Provision a copy of your core workload infrastructure in the recovery Region."
Quotable: "Warm standby (RPO in seconds, RTO in minutes): Maintain a scaled-down but fully functional version of your workload always running in the recovery Region."
Quotable: "Multi-Region (multi-site) active-active (RPO near zero, RTO potentially zero): Your workload is deployed to, and actively serving traffic from, multiple AWS Regions."
Quotable: "Choosing a DR strategy is a trade-off between reducing downtime and data loss (RTO and RPO) and the cost and complexity of implementing the strategy. You should avoid implementing a strategy that is more stringent than it needs to be, as this incurs unnecessary costs."
Quotable: "To learn more, see Business Continuity Plan (BCP)."
Quotable: "For all of the above strategies you may need to promote read-only instances of databases to become the primary read/write instance."
Quotable: "For backup and restore, restoring data from backup creates resources for that data such as EBS volumes, RDS DB instances, and DynamoDB tables."
Quotable: "If using Amazon DynamoDB global tables, even if the table in the primary Region had become not available, when it comes back online, DynamoDB resumes propagating any pending writes."

**[24] Google Cloud - "Disaster recovery planning guide" (Cloud Architecture Center).** vendor. **fetched-and-verified.**
`https://docs.cloud.google.com/architecture/dr-scenarios-planning-guide`
Supports: (a) Google's RTO/RPO definitions and their relation to SLO/SLA; (b) the cold/warm/hot DR-pattern vocabulary and cost tradeoff; (c) DR as a subset of BCP; (f) HA vs DR relationship; general DR-plan construction advice (specific tasks, regular testing, security parity)
Quotable: "DR is a subset of business continuity planning."
Quotable: "DR planning begins with a business impact analysis that defines two key metrics"
Quotable: "A recovery time objective (RTO), which is the maximum acceptable length of time that your application can be offline."
Quotable: "A recovery point objective (RPO), which is the maximum acceptable length of time during which data might be lost from your application due to a major incident."
Quotable: "Typically, the smaller your RTO and RPO values are (that is, the faster your application must recover from an interruption), the more your application will cost to run."
Quotable: "You might also be planning an architecture for high availability (HA). HA doesn't entirely overlap with DR, but it's often necessary to take HA into account when you're thinking about RTO and RPO values."
Quotable: "DR patterns are considered to be cold, warm, or hot. These patterns indicate how readily the system can recover when something goes wrong."
Quotable: "It isn't enough just to have a plan for backing up or archiving your data. Make sure your DR plan addresses the full recovery process, from backup to restore to cleanup."
Quotable: "After you create a DR plan, test it regularly, noting any issues that come up and adjusting your plan accordingly."
Quotable: "Don't wait for a disaster to occur before checking that your users can access the DR environment."

**[25] Google Cloud - "Perform testing for recovery from data loss" (Well-Architected Framework, reliability pillar).** vendor. **fetched-and-verified.**
`https://docs.cloud.google.com/architecture/framework/reliability/perform-testing-for-recovery-from-data-loss`
Supports: (d) why and how to test recovery: judging success by data integrity/RTO/RPO, verifying backup consistency by restoring to a non-production environment, scheduling backup frequency to the RPO, monitoring RPO adherence
Quotable: "We recommend that you use three criteria to judge the success or failure of this type of recovery test: data integrity, recovery time objective (RTO), and recovery point objective (RPO)."
Quotable: "The goal of data restoration testing is to periodically verify that your organization can continue to meet business continuity requirements."
Quotable: "You need to verify that your backups contain consistent and usable snapshots of data that you can restore to immediately bring applications back into service."
Quotable: "To test backups, restore them in a non-production environment. To ensure your backups can be restored efficiently and that the restored data meets application requirements, regularly simulate data recovery scenarios."
Quotable: "To minimize data loss during restoration and to meet RPO targets, it's essential to have regularly scheduled backups. Establish a backup frequency that aligns with your RPO."
Quotable: "Set a clear RPO based on your business needs, and monitor adherence to the RPO. If backup intervals exceed the defined RPO, use Cloud Monitoring to set up alerts."

**[26] Microsoft - "What are business continuity, high availability, and disaster recovery?" (Azure Well-Architected Framework / reliability docs).** vendor. **fetched-and-verified.**
`https://learn.microsoft.com/en-us/azure/reliability/disaster-recovery-overview`
Supports: (a) Microsoft's RPO/RTO definitions; (c) the BCP/HA/DR relationship, stated most explicitly of the four vendors; (d) testing and drills guidance, including the sequencing rule for backup as last resort; (f) HA vs DR, the core question this source was chosen for; (g) backup storage location, data-loss and recovery-time considerations for database backups
Quotable: "Business continuity is the state in which a business can continue operations during failures, outages, or disasters. Business continuity requires proactive planning, preparation, and the implementation of resilient systems and processes."
Quotable: "Planning for business continuity requires identifying, understanding, classifying, and managing risks. Based on understanding the risks and their likelihoods, you can design a healthy business continuity plan to achieve a high availability (HA) and disaster recovery (DR) strategy that suits your business needs."
Quotable: "High availability is about designing a solution to be resilient to day-to-day issues and to meet the business needs for availability."
Quotable: "Disaster recovery is about planning how to deal with uncommon risks and the catastrophic outages that can result."
Quotable: "The HA of each workload contributes to your business continuity plan."
Quotable: "High availability and disaster recovery are interrelated, and so it's important to plan strategies for both of them together."
Quotable: "A disaster is a distinct, uncommon, major event that has a larger and longer-lasting impact than an application can mitigate through the high availability aspect of its design."
Quotable: "Recovery Point Objective (RPO) is the maximum duration of acceptable data loss in the event of a disaster."
Quotable: "Recovery Time Objective (RTO) is the maximum duration of acceptable downtime in the event of a disaster, where "downtime" is defined by your specification."
Quotable: "A strong DR plan turns strategy into decisive action. It provides a clear roadmap for responding to disasters, minimizing downtime, and ensuring business continuity."
Quotable: "With backups you can recover from disasters when automatic failover to another replica isn't possible, or when data corruption has occurred."
Quotable: "Because backups are typically taken infrequently, backup restoration usually involves data loss. For this reason, backup recovery should be used as a last resort and a disaster recovery plan should specify the sequence of steps and recovery attempts that must take place before restoring from a backup."
Quotable: "Backup restoration often takes time, so it's critical to test your backups and restoration processes to verify their integrity and understand how long the restoration process takes."
Quotable: "It's critical to routinely validate and test your DR plans, as well as your wider reliability strategy. Include all of the human processes in your drills, and don't just focus on the technical processes."
Quotable: "If you haven't tested your recovery processes in a disaster simulation, you're more likely to face major problems when using them in an actual disaster."

**[27] Google SRE Book - Chapter 17, "Testing for Reliability".** practitioner. **fetched-and-verified.**
`https://sre.google/sre-book/testing-reliability/`
Supports: (d) only narrowly: a short "Testing Disaster" passage on designing disaster-recovery automation tools to run offline, checkpointable, and loadable so they can be release-tested. The chapter as fetched does NOT contain the DiRT-style "Disaster Role Playing"/game-day material or a stated test-frequency rule that this question anticipated
Quotable: "Many disaster recovery tools can be carefully designed to operate offline."
Quotable: "Compute a checkpoint state that is equivalent to cleanly stopping the service"
Quotable: "In many cases, you can implement these phases so that the associated tests are easy to write and offer excellent coverage. If any of the constraints (offline, checkpoint, loadable, barrier, or clean start) must be broken, it's much harder to show confidence that the associated tool implementation will work at any time on short notice."

**[28] Tanya Reilly (Site Reliability Engineer, Google), interviewed by Nikki McDonald - "Creating better disaster recovery plans" (O'Reilly).** practitioner. **fetched-and-verified.**
`https://www.oreilly.com/content/creating-better-disaster-recovery-plans/`
Supports: (d) the backup-vs-restore-strategy distinction, why untested recovery fails, and the case for regular wide-scale disaster tests; (e) service interdependencies and circular dependencies making recovery harder, and the strata/dependency-management mitigation
Quotable: "The classic line is "you don't need a backup strategy, you need a restore strategy." If you have backups, but you haven't tested restoring them, you don't really have backups."
Quotable: "Testing doesn't just mean knowing you can get the data back; it means knowing how to put it back into the database, how to handle incremental changes, how to reinstall the whole thing if you need to."
Quotable: "At the same time, you have to be sure that the people involved know what to do, so it's good to plan regular wide-scale disaster tests."
Quotable: "Recovery exercises are a great way to find out that the documentation for the process is missing or out of date, or that you don't have enough resources (disk, network, etc.) to transfer and reinsert the data."
Quotable: "I think a lot of DR is an afterthought: "We have this great system, and our business relies on it … I guess we should do DR for it?" And by that point, the system is extremely complex, full of interdependencies and hard to duplicate."
Quotable: "The only way to be sure you've covered everything is to fail over in earnest. Plan your disaster for a time when you're ready for it!"
Quotable: "An occasional scheduled fake disaster is good for shaking those out."
Quotable: "Parts of the system that are only used in disasters need the most testing, or they'll fail you when you need them."
Quotable: "If you've got just one binary, then recovering it is relatively easy: you start that binary back up. But we increasingly break out common functionality into separate services."
Quotable: "After an outage, you can end up with a deadlock: two systems that each can't start until the other is running and providing some functionality. It's a hard situation to recover from!"
Quotable: "You can even end up with things that indirectly depend on themselves-for example, a device that you need to configure to bring up the network, but you can't get to it while the network is down."
Quotable: "Often people have thought about these circular dependencies in advance and have some sort of fallback plan, but those are inherently the road less traveled: they're only intended to be used in extreme cases, and they follow a different path through your systems or processes or code. This means they're more likely to have a bug that won't be uncovered until you really, really need them to work."
Quotable: "Managing your dependencies is essential for being sure you can recover from a disaster. It makes operating the systems easier too. If your dependencies aren't reliable, you can't be reliable, so you need to know what they are."
Quotable: "The other advantage of starting early is that you can split up your services into vertical "strata," where the functionality in each stratum must be able to come completely online before the next one begins."

### THE GAP QUESTION: WHAT GOOD PRACTICE ADDS BEYOND THE COMMONEST SECTIONS

**[29] FEMA - "Continuity Guidance Circular 1 (CGC 1): Continuity Guidance for Non-Federal Entities" (July 2013), read on a Minnesota legislature mirror (lcc.mn.gov) whose path is marked inactive.** primary. **fetched-and-verified.**
`https://www.lcc.mn.gov/inactive/eeptf/meetings/150819/5%20-%20Continuity%20Guicance%20Circular%201.pdf`
Supports: A full-text government continuity standard that explicitly names, as required plan elements distinct from the commonest published sections: delegations of authority (decision authority when leaders are unreachable), orders of succession pre-plan-publication (not just a roster), a reconstitution/deactivation plan with data-and-capability verification before resuming, essential-records accessibility at continuity facilities, communications reaching customers/public (not just internal staff), interdependency exercising across organizations, and a standing Corrective Action Program that converts exercise/AAR findings into tracked fixes
Quotable: "Generally, predetermined delegations of authority will take effect when normal channels of direction are disrupted and will terminate when these channels are reestablished."
Quotable: "To the extent possible, organizations should identify the individuals to whom authorities are delegated by position title and not by name."
Quotable: "Organizations should include delegations of authority as an essential record and ensure they are available at all continuity facilities."
Quotable: "Organizations should include at least one individual in their order of succession who is geographically dispersed from the organization head and other individuals within the order of succession."
Quotable: "Reconstitution requirements address the need for organizations to identify, develop, and coordinate a plan to return to normal operations once leadership determines that the actual emergency, or the threat of an emergency, is over."
Quotable: "Detail how the organization will verify operational capability and availability, including systems, communications, essential records, infrastructure, and other required resources, and that the organization is fully capable of accomplishing all essential functions and operations at the new or restored facility"
Quotable: "Identify how the organization will determine which (if any) records were affected by the incident and ensure an effective transition or recovery of essential records and databases"
Quotable: "Organizations should designate a Reconstitution Manager and a Devolution Reconstitution Manager (if the primary reconstitution manager is located at the primary operating facility) to oversee all phases of the reconstitution process."
Quotable: "These systems should support full connectivity, under all conditions, among key leadership, internal elements, other organizations, critical customers, and the public."
Quotable: "Annual exercise of internal and external interdependencies identified in the organization's continuity plan, with respect to performance of an organization's and other organizations' essential functions."
Quotable: "Deficiencies, actions to correct them, and a timeline for remedy are documented in an organization's Corrective Action Program (CAP)."
Quotable: "A CAP to assist in documenting, prioritizing, and resourcing continuity issues across all continuity elements identified during TT&E, assessments, and emergency operations."
Quotable: "Organizations should strongly consider multiple redundant media for storing their essential records."
Quotable: "Organizations should develop procedures to ensure that as soon as possible after activation of continuity plans, but in all cases within 12 hours of an activation, ERG/DERG at the continuity facilities have access to the appropriate media for accessing essential records."

**[30] FINRA, Rule 4370 (Business Continuity Plans and Emergency Contact Information).** primary (regulation). **fetched-and-verified.**
`https://www.finra.org/rules-guidance/rulebooks/finra-rules/4370`
Supports: A real, enforced BCP rule requires: customer-facing disclosure of how the plan handles disruption; documenting the relationship when the firm relies on another entity for any required BCP category (third-party/vendor dependency); and naming 'communications with regulators' and 'regulatory reporting' as required plan contents distinct from customer communications
Quotable: "Each member must disclose to its customers how its business continuity plan addresses the possibility of a future significant business disruption and how the member plans to respond to events of varying scope."
Quotable: "If a member relies on another entity for any one of the above-listed categories or any mission critical system, the member's business continuity plan must address this relationship."
Quotable: "How the member will assure customers' prompt access to their funds and securities in the event that the member determines that it is unable to continue its business."
Quotable: "Each member must update its plan in the event of any material change to the member's operations, structure, business or location. Each member must also conduct an annual review of its business continuity plan"

**[31] CISA, NSA, FBI, MS-ISAC, #StopRansomware Guide (2023).** primary. **fetched-and-verified.**
`https://www.cisa.gov/sites/default/files/2023-05/stopransomware_guide_508c.pdf`
Supports: A primary government incident-response guide specifying that cyber/ransomware recovery requires offline backups kept separate from the production network specifically because ransomware targets reachable backups, plus a hard-copy, offline version of the response/communications plan itself so the plan survives the same outage it addresses
Quotable: "Maintain offline, encrypted backups of critical data, and regularly test the availability and integrity of backups in a disaster recovery scenario [CPG 2.R]."
Quotable: "It is important that backups are maintained offline, as many ransomware variants attempt to find and subsequently delete or encrypt accessible backups to make restoration impossible unless the ransom is paid."
Quotable: "Some cloud vendors offer immutable storage solutions that can protect stored data without the need for a separate environment. Use immutable storage with caution as it does not meet compliance criteria for certain regulations and misconfiguration can impose significant cost."
Quotable: "Create, maintain, and regularly exercise a basic cyber incident response plan (IRP) and associated communications plan that includes response and notification procedures for ransomware and data extortion/breach incidents [CPG 2.S]. Ensure a hard copy of the plan and an offline version is available."
Quotable: "Ensure that data breach notification procedures adhere to applicable state laws."

**[32] Visa, 'Disaster Recovery and Business Continuity Requirements' (supplier/vendor contract schedule).** primary (a supplier contract schedule). **fetched-and-verified.**
`https://usa.review.visa.com/content/dam/VCOM/regional/na/us/partner-with-us/documents/disaster-recovery-and-business-continuity-requirements.pdf`
Supports: A real contractual flow-down showing that good BCP practice makes a supplier's own subcontractors' continuity an explicit, auditable dependency, and requires post-incident recovery reporting (root cause plus corrective actions) distinct from routine exercise findings, plus a timed disaster-notification duty to the affected counterparty
Quotable: "Supplier shall ensure all Subcontractors have Business Continuity Programs and Disaster Recovery Plans sufficient to meet delivery of the Services during a Disruptive Event."
Quotable: "In the event of a Disruptive Event, Supplier shall promptly notify Visa of the nature of the interruption, if known, and an estimate of the time it will take to recover the Services and return to business as usual service levels."
