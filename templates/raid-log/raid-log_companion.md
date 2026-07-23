# Companion: The RAID Log

> The deep explainer for the raid-log bundle. Read this to understand what a RAID log is, where it came from
> (and where it did not), why it is shaped the way it is, and where practitioners disagree about it. The short
> operator card is [`raid-log_guide.md`](raid-log_guide.md); a fully worked instance is
> [`raid-log_example.md`](raid-log_example.md). Inline citations like [[1]](#ref-1) resolve to the
> [References](#references) at the bottom, tagged by source reliability.

---

## 1. Orientation

A RAID log is **one working document that tracks the four kinds of open item a project manager has to hold in
their head: Risks, Assumptions, Issues, and Dependencies.** It is the single place a delivery team looks to
answer "what might go wrong, what are we taking on faith, what has already gone wrong, and what are we waiting
on?" The University of Waterloo's PMO puts it plainly: *"a simple, effective project/program management tool
to organize a project/program by tracking risks, actions, issues, and decisions"* [[6]](#ref-6) (this PMO
uses the Actions/Decisions expansion - the acronym debate, below, in action). The
Institute of Risk Management's definition is the closest thing to an authoritative one: *"a management tool
used to identify and manage potential risks, and issues that may arise during a project or programme"*
[[1]](#ref-1).

The honest first thing to know is that the RAID log is a **consolidation convention, not a standard.** There
is no documented inventor and no governing body that owns it. PRINCE2 7th edition *"does not name RAID logs
directly in the manual"* even though *"the method builds them right into the practices"* [[2]](#ref-2); PMBOK
does not define it either. **Even the acronym is contested** - the **A** is Assumptions or Actions and the
**D** is Dependencies or Decisions, and, tellingly, the UK's Association for Project Management uses *"risks,
actions, issues, decisions"* in its own writing [[4]](#ref-4) while other bodies keep Assumptions and
Dependencies [[1]](#ref-1). This bundle uses the Assumptions/Dependencies expansion (Risks, Assumptions,
Issues, Dependencies), chosen because Assumptions and cross-team Dependencies are the quadrants delivery teams
most often neglect (section 6), and teaches the discipline that resolves the ambiguity: pick one expansion,
write it down, and stop relitigating it every kickoff [[9]](#ref-9).

**At a glance**
- It holds **four genuinely different kinds of item** - a Risk might happen, an Assumption is believed true
  without proof, an Issue has already happened, a Dependency is a structural relationship. They do not share
  a schema [[22]](#ref-22).
- Its unifying idea is **migration**: *"An assumption that fails becomes an issue. A dependency that slips
  becomes a risk, then an issue"* [[9]](#ref-9).
- It is the **weekly working consolidation**; the deepened form of its R is a standalone
  [`risk-register`](../risk-register/risk-register_guide.md) [[8]](#ref-8).
- It is **owned by one person and populated by the team**: *"The project manager owns and maintains the log.
  The team populates it"* [[9]](#ref-9), and every item has *"a named person. Never a team, never the PM by
  default"* [[9]](#ref-9).
- Its value lives or dies on **review cadence**: *"A RAID log is only as good as its review cadence"*
  [[21]](#ref-21).

If you read nothing else: a RAID log is a **living, owned, four-quadrant record of everything open on a
project.** The moment it stops being reviewed, it becomes *"documentation theater, not management"*
[[12]](#ref-12) - the failure its critics rightly name.

---

## 2. Origins and evolution

**The RAID log has no origin story, and that is the honest finding.** No primary source credits a person, a
company, or a founding document with coining it. Every practitioner source treats the term as pre-existing
institutional knowledge; one of the earliest dateable online references, from 2010, already introduces it as
something *"which should be at the forefront of your mind if you are a project manager or a program manager"*
[[7]](#ref-7), with no claim to have invented it, which suggests it predates that date by a meaningful margin.

**Its lineage is the traditional project-management tradition, and it is best understood as a practitioner
overlay on the formal frameworks.** TechAgilist places it precisely: *"This technique has been borrowed from
the domain of traditional (waterfall) project management, which typically calls for the creation of a
deliverable such as a 'RAID log'"* [[23]](#ref-23). PRINCE2 and PMI both manage risks, issues, assumptions,
and dependencies as separate concerns; the RAID log is the convention of putting all four in one artifact.
This is why PRINCE2 7th can build the elements into its practices without naming the log [[2]](#ref-2), and
why the same underlying idea shows up when the PRINCE2 community describes a risk register that can be kept as
part of one integrated project register covering risks, actions, decisions, assumptions, issues, and lessons
together - which is functionally a RAID log.

**The acronym drifted precisely because no one owns it.** The most complete single treatment is Kim
Essendrup's *The Ultimate Guide to RAID Log*, which uses Risks, Actions, Issues, Decisions and argues the
point directly (section 6). The expansion you pick is a real decision with a functional rationale, not a
cosmetic one, which is the subject of section 6.

---

## 3. Anatomy (section by section)

A RAID log is **four tables, not one**, because the four quadrants are different kinds of thing. Every item,
whatever its quadrant, carries a shared spine - *"a unique ID, category, description, owner, priority, and
status"* [[14]](#ref-14) - but each quadrant then adds fields the others do not have. This is the single most
important structural fact about the artifact: *"you need to approach each section of your RAID log with a
different mindset. Issues are different than risks"* [[22]](#ref-22).

### Purpose and Scope

**What it is:** one short block naming the project, **which expansion of RAID you are using** (say so
explicitly), who owns the log, and the review cadence. **Why it exists:** because the acronym ambiguity is
real, the single most useful line in a RAID log is the one that says what its letters mean here. The IRM
warns of the opposite failure too - *"if you document every decision... down to the smallest detail, the log
can quickly become cluttered"* [[1]](#ref-1) - so scope also says what does *not* belong.

### Risks (R)

**What it is:** the summary of things that **might** happen: a short risk statement, a likelihood and impact,
an owner, and a response. **Why it is a summary here:** the RAID log's R is the lightweight, weekly view; the
deepened form, with inherent-versus-residual scoring, triggers, and appetite, is a standalone risk register
(see section 8). The R row can **point to** the register rather than duplicate it [[8]](#ref-8). A risk that
materializes is closed here and reopened as an Issue.

### Assumptions (A)

**What it is:** the things the team is **treating as true without proof**, each with the impact if it turns
out false, a confidence level, and a validation action and date. A well-formed entry carries *"ID, Date
raised, Source, Assumption, Description, Reason, Priority, Action to validate, Impact if incorrect, Validation
due date, Owner, Status"* [[13]](#ref-13); the distinctive fields are the *"impact statement if assumption
proves false"* and the *"confidence level regarding validity"* [[14]](#ref-14). **Why it is its own quadrant:**
an assumption is a **latent risk in disguise.** When it fails - the belief is now known to be wrong - it
becomes an **issue** (something that has happened); an assumption merely thrown into doubt but not yet
disproven first hardens into a **risk**. The "validate by" date exists to catch that decay before it happens. This is the quadrant agile teams most often
drop, because an assumption *"does not fit a sprint backlog"* [[9]](#ref-9).

### Issues (I)

**What it is:** the things that **have already happened** and are affecting the project now: a description, a
severity or priority, an owner, a resolution plan, and crucially a **raised date** so you can measure how long
it has been open [[13]](#ref-13)[[14]](#ref-14). A concise entry is just *"ID, Description, Priority, Owner,
Resolution Plan, Status"* [[25]](#ref-25); the raised date is what a fuller log adds for aging. **Why it has no probability:** an issue is not a maybe; the
event has occurred, so it carries a *"raised date for aging assessment"* [[14]](#ref-14) instead of a
likelihood or a trigger. Some teams split **severity** (how bad) from **priority** (how urgent) [[14]](#ref-14);
others merge them. The clean rule at the boundary with risks: when a risk event occurs, close the risk and
open a matching issue.

### Dependencies (D)

**What it is:** the **structural relationships** the project cannot proceed without: what you are waiting on,
from whom, by when. The distinctive field is **direction** - *"Inbound Dependencies: tasks or deliverables
your project depends on from other teams, vendors, or systems"* versus *"Outbound Dependencies: tasks your
project delivers that other projects or stakeholders rely on"* [[18]](#ref-18) - plus the party, the
needed-by date, and the dependency type (third-party, cross-team, customer) [[18]](#ref-18)[[15]](#ref-15).
**Why it is its own quadrant:** a dependency is not itself a threat; it is a relationship that can *become* a
risk (if the other party is unreliable) or an issue (if a delivery is missed). Direction drives the
escalation path: you can chase an inbound dependency, but an outbound one is someone else's risk that you
created.

### Review and Ownership

**What it is:** the cadence, the owner, and how items escalate. **Why it exists:** because the abandonment
failure is the log's defining risk. The consensus is a two-tier cadence - a weekly working review at team
level and a fuller monthly or stage-gate sweep [[8]](#ref-8) - with a nuance from long practice that the
quadrants move at different speeds: *"I update something in my action log at least once a day"* but *"risks
should be updated at least monthly"* [[5]](#ref-5). The PM owns the log; the team populates it [[6]](#ref-6);
every item has one named owner [[9]](#ref-9).

---

## 4. Variants and sizing

**Lean** is the smallest real RAID log: **Purpose and Scope**, the four quadrant tables (**Risks**,
**Assumptions**, **Issues**, **Dependencies**), and **Review and Ownership**. It is a complete working log for
one team on one project, often kept as a single combined table with a Category column [[17]](#ref-17).

**Full** is a strict superset. It keeps the six lean sections in order and adds richer per-quadrant fields
(validation dates, severity-versus-priority, dependency direction and type), an **Escalation and Aging**
section (which items are escalated and how long they have sat - *"the single best measure of whether
governance is actually deciding anything"* [[9]](#ref-9)), and a **Cross-Quadrant Summary** (counts by
category and priority, and the migrations between quadrants). Larger logs move from one combined table to
**four separate tabs**, because the quadrants' field sets and review cadences genuinely differ (compare the
per-quadrant field lists in [[7]](#ref-7) and the separate-worksheet layout in [[16]](#ref-16)); some teams
keep *"a series of RAID logs, one for each section"* [[22]](#ref-22).

**The scaling signal is volume and governance, not project length.** Move to full (and to separate tabs) when
a single view exceeds roughly fifty active items, when different owners hold different quadrants, or when a
steering group consumes an escalation view. On very large programs the four quadrants sometimes expand to
**RAAIDD** (adding Actions and Decisions) where *"if left unvalidated or untracked, assumptions can cause
major issues for the SAP PMO"* and *"mapped and agreed dependencies help in identifying the Project Critical
Path, focussing on the right things at the right time"* [[19]](#ref-19).

---

## 5. Methodology lineage

- **Traditional / PRINCE2 / PMI.** The native home. PRINCE2 manages risks, issues, and change through named
  practices and feeds them into highlight reports and the project board [[2]](#ref-2); the RAID log is the
  convention that consolidates them. This is the lineage TechAgilist names as the artifact's origin
  [[23]](#ref-23).
- **Agile / Scrum.** The RAID log is used, but adapted. The mainstream practitioner position is that it is
  *"just as useful and relevant whether you follow an agile methodology or a more predictive 'waterfall'
  methodology"* [[24]](#ref-24), reviewed inside the ceremonies rather than in a separate governance meeting:
  *"sprint planning, daily stand-ups, retrospectives, backlog refinement, stakeholder check-ins, and release
  planning"* [[10]](#ref-10), which *"supports the Agile ethos of transparency, inspection, and adaptation"*
  [[11]](#ref-11). The lighter-weight alternative some teams prefer is to run RAID on a Kanban board rather
  than a spreadsheet [[23]](#ref-23). The quadrants agile most often loses are Assumptions and cross-team
  Dependencies, precisely because neither fits a sprint backlog [[9]](#ref-9).
- **Scaled agile (SAFe, LeSS) and PMO.** In practice, ownership moves to a program-level role (a Release
  Train Engineer or program manager holds the log across teams), and dependency tracking re-enters formally because cross-team
  dependencies are a program concern (an editorial synthesis of scaled-agile practice, not a claim from a
  single cited source).

---

## 6. Debates and contested boundaries

**The acronym ambiguity is real, live, and reaches the reference bodies themselves.** The IRM's own guide says
the log *"typically consists of four categories: Risks, Assumptions, Issues, and Decisions (or Dependencies)"*
- naming both expansions in one sentence - and notes that *"some variations combine actions and decisions to
form a RAAIDD log"* [[1]](#ref-1). PortfolioHub names the split directly: *"The A is used for both assumptions
and actions"* and *"The D is used for both dependencies and decisions"* [[9]](#ref-9). There is a genuine
functional argument, not just sloppiness: Essendrup's case for Actions and Decisions is that *"Assumptions &
Dependencies are typically identified at the beginning of a project...then monitored through the project"*
while *"Action items & Decisions...have to be actively managed throughout the entire lifecycle"* [[3]](#ref-3),
so tracking the
actively-managed pair is more useful day to day. The counter-position, from complex-program practice, is that
Assumptions and Dependencies are exactly what goes untracked and bites you, so they deserve their own
quadrants (or RAAIDD keeps all six) [[19]](#ref-19). **This bundle's position:** the expansion is a real
choice; make it explicitly and once. The failure is not choosing "wrong" - it is leaving it ambiguous so the
team relitigates it every kickoff [[9]](#ref-9).

**Is the RAID log an anti-pattern?** A pointed critique, mostly from the agile community, holds that RAID
*"comes out of a PMI/PMO mindset, and is often an extensive log of 'issues' used to assign accountability (aka
'Escalate') and quite possibly blame"* [[20]](#ref-20). The sharper version of the same thread concedes the
real issue: *"it's not the act of collecting the data that is the problem. It is how it is used"* [[20]](#ref-20).
The constructive answer is the mainstream one: a RAID log is accountability infrastructure, not a blame
instrument, and its value is in *"transparency, inspection, and adaptation"* [[11]](#ref-11) when it is a
living team tool rather than a management stick.

**The real failure mode both camps agree on is abandonment.** *"Most teams set one up at kickoff and abandon
it by week three"* [[21]](#ref-21); a log nobody reviews is *"documentation theater, not management"*
[[12]](#ref-12); an outdated log *"can mislead stakeholders, foster misplaced confidence, or even generate
more confusion than if no log were kept"* [[11]](#ref-11). And there is a calibration trap on the other side -
*"too far and you're going to bog down and miss the important stuff. But if you're too cursory... it defeats
the purpose"* [[22]](#ref-22), an overloaded log *"can lead to decision paralysis"* [[10]](#ref-10). The
answer to all of it is cadence and ownership, not more or fewer columns.

**A smaller debate: one combined table or four tabs?** Asana presents the combined table as standard
[[17]](#ref-17); downloadable templates more often use four tabs [[7]](#ref-7)[[16]](#ref-16). Neither is
correct; it is a volume-and-tooling choice (section 4).

---

## 7. Anti-patterns and failure modes

1. **Documentation theater (kickoff-and-abandon).** *"Most teams set one up at kickoff and abandon it by week
   three"* [[21]](#ref-21); a log nobody reviews *"is documentation theater, not management"* [[12]](#ref-12).
   The signature failure. Fix: a stated weekly cadence and a named log owner.
2. **The undeclared acronym.** The team never says whether A is Assumptions or Actions, so half of them track
   one and half the other. Fix: state the expansion in Purpose and Scope and stop relitigating it
   [[9]](#ref-9).
3. **The bloated log.** Every tiny detail logged until *"finding information can be challenging"* [[1]](#ref-1)
   and it *"can lead to decision paralysis"* [[10]](#ref-10). Fix: scope what belongs; escalate and archive.
4. **Ownerless items.** A row owned by "the team" is owned by no one. Fix: *"a named person. Never a team,
   never the PM by default"* [[9]](#ref-9).
5. **The issue log wearing a risk mask (and vice versa).** Logging things that have already happened as risks,
   or potential events as issues, which hides what needs action now. Fix: a risk might happen; an issue has
   happened - migrate between them deliberately [[22]](#ref-22).
6. **The blame register.** Using the escalation column to assign fault rather than to get a decision, which is
   the anti-pattern critics rightly attack [[20]](#ref-20). Fix: escalate to resolve, not to target.

---

## 8. Relationships to other artifacts

**RAID log vs risk register.** They are complementary layers at different altitudes, not competitors. The
RAID log is the weekly working consolidation; the risk register is the **R pulled out and deepened**. The
split is by cadence and audience: *"RAID Log: Program team and workstream leads in 15-minute working sessions;
Risk Register: Steering committee, program board, CFO, CRO, or external auditors in 90+ minute reviews"*
[[8]](#ref-8). They feed each other - strategic risks surfaced in the weekly RAID review promote up into the
register, and *"if you only have one, half this loop is missing"* [[8]](#ref-8). The RAID's R quadrant can
reference the register rather than duplicate it. This bundle's sibling
[`risk-register`](../risk-register/risk-register_guide.md) is that deepened form.

**RAID log vs a standalone issue / assumption / dependency log.** The RAID log's whole point is
**consolidation** - seeing an assumption failure become an issue, or a dependency slip become a risk, in one
view. Teams decompose back into separate logs only when volume or different owners make one artifact
unworkable, keeping *"a series of RAID logs, one for each section"* [[22]](#ref-22).

**RAID log vs status report.** The RAID log is the **raw material** for a status report, not the report
itself. A highlight or status report draws on the RAID to characterize the project's posture without
transferring the whole log [[2]](#ref-2). The forthcoming `status-report` bundle is the reporting layer above
it.

**RAID log vs KPI dashboard.** Both are standing governance instruments in this family, but the RAID tracks
**open items to resolve** while the [`kpi-dashboard`](../kpi-dashboard/kpi-dashboard_guide.md) tracks
**performance against targets**. In the worked example they cover the same program; a dependency that slips on
the RAID shows up as a dip on the dashboard it feeds.

---

## 9. Adaptations

- **Agile teams.** Keep it lean and live it inside the ceremonies (stand-ups, refinement, retrospectives)
  [[10]](#ref-10)[[11]](#ref-11); consider a Kanban board over a spreadsheet [[23]](#ref-23); make a point of
  the two quadrants agile drops, Assumptions and cross-team Dependencies [[9]](#ref-9).
- **Large / regulated programs.** Move to four tabs, add the Escalation and Aging and Cross-Quadrant Summary
  sections, and consider **RAAIDD** where assumptions and dependencies are load-bearing [[19]](#ref-19). Run a
  standalone risk register alongside the RAID for the audit-grade R [[8]](#ref-8).
- **Scaled agile / PMO.** A program-level owner holds the log across teams; cross-team dependencies become the
  PMO's escalation responsibility (scaled-agile practice; see section 5).
- **Solo or small projects.** One combined table, a light weekly review, and the discipline of an owner per
  row is enough [[17]](#ref-17); the point is that it is reviewed at all [[21]](#ref-21).

---

## 10. Worked example

[`raid-log_example.md`](raid-log_example.md) is a full-variant RAID log for the Acme Analytics **Reporting
Platform Modernization** program - the same program the [`risk-register`](../risk-register/risk-register_example.md)
example covers. It is built to demonstrate **quadrant migration**: its **Risks** quadrant summarizes the
register's risks and points to it; its **Issues** include the materialized key-person risk (ISS-11, which was
risk R-03 on the register); its **Assumptions** are the beliefs those risks rest on (the vendor will renew,
analysts want the feature); and its **Dependencies** connect the inbound query-engine delivery and the
outbound Recommendations telemetry to the risks and the opportunity they carry. It uses the Risks,
Assumptions, Issues, Dependencies expansion, declared in its scope line, and shows the escalation-and-aging
and cross-quadrant-summary sections of the full variant.

---

## References

<a id="ref-1"></a>[1] Institute of Risk Management (IRM), Infrastructure Risk Special Interest Group. "[Short Guide to RAID](https://www.theirm.org/media/2517814/7-short-guide-raid.pdf)." theirm.org, October 2023 (accessed 2026-07-22). The closest thing to a professional-body definition; states the D = Decisions or Dependencies ambiguity, the RAAIDD variant, and the over-documentation warning ("RAID is an acronym that stands for Risks, Assumptions, Issues, and Dependencies. It is a management tool used to identify and manage potential risks, and issues that may arise during a project or programme."; "The RAID log typically consists of four categories: Risks, Assumptions, Issues, and Decisions (or Dependencies)"; "some variations combine actions and decisions to form a RAAIDD log"; "If you document every decision made in a RAID log down to the smallest detail, the log can quickly become cluttered and finding information can be challenging."). An IRM SIG guide, not a PMI/PRINCE2 primary. [primary]

<a id="ref-2"></a>[2] The Projex Academy. "[How to use RAID properly in PRINCE2 7th edition](https://www.projex.com/how-to-use-raid-properly-in-prince2-7th-edition/)." projex.com (accessed 2026-07-22). Supports that PRINCE2 7th does not name the RAID log but builds its elements into the practices, and that RAID feeds highlight reports ("PRINCE2 7th Edition does not name RAID logs directly in the manual. However, the method builds them right into the practices."; "RAID logs feed into highlight reports and project board communications, with dependencies highlighted as critical obstacles requiring board-level attention."). Practitioner trainer, not Axelos/PeopleCert. [practitioner]

<a id="ref-3"></a>[3] Essendrup, Kim. "[Wait, I thought A=Assumptions and D=Dependencies?](https://raidlog.com/book-excerpts/wait-i-thought-aassumptions-and-ddependencies/)" raidlog.com (book excerpt) (accessed 2026-07-22). Supports the A/D debate and the functional argument for Actions/Decisions ("Assumptions & Dependencies are typically identified at the beginning of a project...then monitored through the project"; "Action items & Decisions...have to be actively managed throughout the entire lifecycle."; "a seemingly small difference that has a huge impact"). The author founded a RAID-log product; the position is contested. [practitioner]

<a id="ref-4"></a>[4] Association for Project Management (APM). "[Simple solution to the constraint complaint](https://www.apm.org.uk/blog/simple-solution-to-the-constraint-complaint/)." apm.org.uk (accessed 2026-07-22). Shows a primary UK professional body using Actions and Decisions in its own casual description of RAID ("As project managers, we're all aware of the RAID log concept, to capture risks, actions, issues, decisions and any other information a project manager may wish, or be obliged to record."). A blog post, not the APM Body of Knowledge text. [primary]

<a id="ref-5"></a>[5] Harrin, Elizabeth. "[A real project manager's guide to RAID](https://rebelsguidetopm.com/raid-in-project-management/)." Rebels Guide to Project Management (accessed 2026-07-22). A 20-plus-year practitioner view; component-specific cadences and PM ownership ("in my experience RAID alone is not enough"; "I update something in my action log at least once a day."; "Risks should be updated at least monthly."; "Issues may need to be updated daily depending on what is going on."; "The project manager should update the RAID log."; "It's a good idea to review everything on the log at least once a month."; "A RAID log is a way of tracking the things that affect and influence your project. It is part of the governance and control mechanisms around your project."). [practitioner]

<a id="ref-6"></a>[6] University of Waterloo, VPAF Project Management Office. "[RAID Log](https://uwaterloo.ca/vpaf-project-management-office/methodologies/project-management/planning/raid-log)." uwaterloo.ca (accessed 2026-07-22). An institutional definition; PM as author/maintainer; RAID as a living document ("A RAID log is a simple, effective project/program management tool to organize a project/program by tracking risks, actions, issues, and decisions."; "The author and maintainer is often the Program/Project Manager. Sometimes others may be providing updates, especially to the issues log."; "It is a dynamic document that is constantly maintained throughout the project/program."). [reference]

<a id="ref-7"></a>[7] Expert Program Management. "[RAID: Risks, Assumptions, Issues and Dependencies](https://expertprogrammanagement.com/2010/10/raid-risks-assumptions-issues-and-dependencies/)." expertprogrammanagement.com, October 2010 (accessed 2026-07-22). One of the earliest dateable online RAID references, treating it as already-established; per-quadrant fields ("RAID is an acronym which should be at the forefront of your mind if you are a project manager or a program manager."; "Assumptions sheet: assumption name and description, implication (impact) if false, assumption or constraint designation, criticality level, next actions, owner"; "Dependencies sheet: name and description, inbound or outbound direction, priority, commitment status, Last Updated, Next Update, Next Actions, owner"). [practitioner]

<a id="ref-8"></a>[8] DirectorPM. "[RAID log vs risk register: when to use which](https://directorpm.com/blog/raid-log-vs-risk-register)." directorpm.com (accessed 2026-07-22). Supports the RAID-vs-register split by cadence and audience and the feed loop ("The discipline of weekly review is the most important habit for a program manager to build."; "If you only have one, half this loop is missing"; "RAID Log: Program team and workstream leads in 15-minute working sessions; Risk Register: Steering committee, program board, CFO, CRO, or external auditors in 90+ minute reviews"). [practitioner]

<a id="ref-9"></a>[9] PortfolioHub. "[RAID Log: meaning and when to review](https://portfoliohub.io/blog/raid-log)." portfoliohub.io (accessed 2026-07-22). Supports the "pick one expansion" discipline, quadrant migration, audience segregation, ownership, and the agile gap ("The A is used for both assumptions and actions."; "The D is used for both dependencies and decisions."; "What matters is that your organization picks one expansion, writes it down, and stops relitigating it in every kickoff."; "An assumption that fails becomes an issue. A dependency that slips becomes a risk, then an issue."; "The project manager owns and maintains the log. The team populates it."; "A steering committee handed a 60-row RAID log will read none of it."; "A named person. Never a team, never the PM by default."; "agile teams routinely lose are assumptions and cross-team dependencies, because neither fits a sprint backlog"). [practitioner]

<a id="ref-10"></a>[10] Smartsheet. "[How to create and use a RAID log for project success](https://www.smartsheet.com/content/raid-logs)." smartsheet.com (accessed 2026-07-22). Supports the combined-table core fields, agile-ceremony integration, the A ambiguity, and the overload failure ("A RAID log includes four core components: risks, assumptions, issues, and dependencies. Many RAID logs also include supporting details for these categories, such as impact level, owner, status, mitigation plan, and target resolution date."; "sprint planning, daily stand-ups, retrospectives, backlog refinement, stakeholder check-ins, and release planning"; "A RAID log can become overwhelming if it is overloaded with excessive information"; "While the standard definition of a RAID log lists the A as assumptions, some project managers also use the A to represent actions"). [vendor]

<a id="ref-11"></a>[11] Pontis Technology. "[The most overlooked agile practice: RAID log explained](https://pontistechnology.com/the-most-overlooked-project-management-practice-raid-logs/)." pontistechnology.com, January 2026 (accessed 2026-07-22). Supports RAID across agile frameworks, distributed ownership, and the outdated-log failure ("the log should be reviewed and refreshed regularly, ideally as part of sprint ceremonies or project check-ins"; "supports the Agile ethos of transparency, inspection, and adaptation"; "When it is left outdated, it can mislead stakeholders, foster misplaced confidence, or even generate more confusion than if no log were kept."). Advocacy piece. [practitioner]

<a id="ref-12"></a>[12] Rocketlane. "[RAID management: complete guide for PS teams](https://www.rocketlane.com/blogs/raid-management)." rocketlane.com, 2026 (accessed 2026-07-22). Supports the "documentation theater" critique, scale collapse, and the medium-items risk ("A RAID log nobody reviews is documentation theater, not management."; "A RAID log in Google Sheets works for one PM managing two projects. It breaks down at 15 PMs and 80 concurrent projects."; "the highest cumulative delivery risk often comes from 3-5 Medium items nobody actively manages."). Vendor content; failure modes corroborate independent sources. [vendor]

<a id="ref-13"></a>[13] Plaky. "[RAID log: templates + how to build one that actually works](https://plaky.com/learn/project-management/raid-log/)." plaky.com (accessed 2026-07-22). The most complete verbatim per-quadrant field lists ("Assumptions: ID, Date raised, Source, Assumption, Description, Reason, Priority, Action to validate, Impact if incorrect, Validation due date, Owner, Status"; "Issues: ID, Date reported, Source, Issue, Description, Impact, Cause, Priority, Response plan, Response actions, Updates, Status, Owner, Date resolved, Resolution, Remediation, Lessons learned"; "Dependencies: ID, Date added, Source, Dependency, Description, Type, Priority/importance, Impact if not delivered, Status, Owner, Due date, Updates"). [vendor]

<a id="ref-14"></a>[14] Rocketlane. "[RAID management: complete guide for PS teams (field requirements)](https://www.rocketlane.com/blogs/what-is-raid-management-guide)." rocketlane.com (accessed 2026-07-22). Supports the shared spine and the category-specific fields ("Complete RAID log includes a unique ID, category, description, owner, priority, and status for every item"; "Assumptions: validation approach and target date, impact statement if assumption proves false, confidence level regarding validity"; "Issues: severity rating, target resolution deadline, raised date for aging assessment"; "Dependencies: direction indicator (inbound/outbound), external party or dependent entity, due/needed-by date, dependency type classification"). [vendor]

<a id="ref-15"></a>[15] Corporate Finance Institute. "[RAID Log: definition, purpose, breakdown](https://corporatefinanceinstitute.com/resources/management/raid-log/)." corporatefinanceinstitute.com (accessed 2026-07-22). Supports dependency and assumption field detail ("Dependencies: inbound vs. outbound designation, a detailed description of the dependency, the specific date when the dependency will be delivered, the parties that consent to the dependency, comments with date and author attribution"; "Assumptions: a distinct identifier, the date when an item was logged, a summary of the assumptions, a detailed description, status (new, in progress, closed), the stakeholders consulted"). [reference]

<a id="ref-16"></a>[16] StakeholderMap.com. "[RAID log Excel template](https://www.stakeholdermap.com/project-templates/raid-log-excel-template.php)." stakeholdermap.com (accessed 2026-07-22). Verbatim column headers from a real four-tab template using the Actions/Decisions variant, concretely demonstrating the acronym split and the four-worksheet layout ("Risks tab: Risk number, Date identified, Description, Probability, Impact, Preventative actions, Contingent actions, Owner, Actions by, Target date, Status, Notes"; "Issues tab: Issue number, Priority, Description, Owner, Cause, Resolution, Status, Comments, Target date"). Uses Risks, Actions, Issues, Decisions; no Assumptions/Dependencies tabs. [practitioner]

<a id="ref-17"></a>[17] Asana. "[RAID Log: track risks, assumptions, issues and decisions](https://asana.com/resources/raid-log)." asana.com (accessed 2026-07-22). Supports the single-combined-table layout with a Category column ("Combined table core fields: ID number, Description, Category (Risk/Assumption/Issue/Decision), Date identified, Owner, Priority (High/Medium/Low), Status (Open/In Progress/Closed), Action plan"). [vendor]

<a id="ref-18"></a>[18] RAIDLOG.com. "[Project dependencies](https://raidlog.com/education/project-dependencies/)." raidlog.com (accessed 2026-07-22). The clearest inbound/outbound dependency definitions and party-type classification ("Inbound Dependencies: tasks or deliverables your project depends on from other teams, vendors, or systems"; "Outbound Dependencies: tasks your project delivers that other projects or stakeholders rely on"; "Dependency types: Third-Party Dependencies, Cross-Team or Cross-Project Dependencies, Customer Responsibilities"). [vendor]

<a id="ref-19"></a>[19] Resulting IT. "[RAID vs RAAIDD log: why assumptions and dependencies matter for SAP](https://www.resulting-it.com/raid-vs-raaidd-log-pmo)." resulting-it.com (accessed 2026-07-22). Supports the RAAIDD expansion and the case for keeping Assumptions and Dependencies as separate quadrants ("if left unvalidated or untracked, assumptions can cause major issues for the SAP PMO"; "mapped and agreed dependencies help in identifying the Project Critical Path, focussing on the right things at the right time"). SAP/ERP context; opposes Essendrup [[3]](#ref-3). [practitioner]

<a id="ref-20"></a>[20] Agile Uprising Coalition. "[RAID: an anti-pattern? (forum thread)](https://coalition.agileuprising.com/t/raid-an-anti-pattern/1159)." coalition.agileuprising.com, 2017 (accessed 2026-07-22). Supports the PMI/PMO blame-culture critique and the "it's how it's used" nuance ("In my opinion it's not the act of collecting the data that is the problem. It is how it is used."; "RAID comes out of a PMI/PMO mindset, and is often an extensive log of 'issues' used to assign accountability (aka 'Escalate') and quite possibly blame."; "The moment any metric is used to chastise and target individuals we have big issues."). A 2017 thread, still widely linked. [practitioner]

<a id="ref-21"></a>[21] TrackingTime. "[RAID log: templates + how to build one that actually works](https://trackingtime.co/project-management-software/raid-log.html)." trackingtime.co, May 2026 (accessed 2026-07-22). Supports the kickoff-and-abandon failure and review cadence as the operative variable ("Most teams set one up at kickoff and abandon it by week three."; "The most common failure mode is logging items without tracking how much time they consume turning the log into a list rather than a management tool."; "A RAID log is only as good as its review cadence. A well-designed log reviewed monthly produces less value than a basic log reviewed every Friday."; "A RAID log that lives in a different system than the work itself becomes a parallel universe."). The author sells time-tracking software. [practitioner]

<a id="ref-22"></a>[22] ProjectManager.com. "[What is a RAID log and why should I use one?](https://www.projectmanager.com/blog/raid-log-use-one)" projectmanager.com, August 2024 (accessed 2026-07-22). Supports the living-document point, the calibration failure, per-category logs, and the different-mindset-per-quadrant rule ("a RAID log is not done once but is a living project management document. It should be reviewed and updated throughout the life cycle of the project."; "Too far and you're going to bog down and miss the important stuff. But if you're too cursory in your approach, then it defeats the purpose"; "you need to approach each section of your RAID log with a different mindset. Issues are different than risks, for example."; "Maybe you want to keep a series of RAID logs, one for each section, rather than combining the four categories into one log."). [vendor]

<a id="ref-23"></a>[23] TechAgilist. "[RAID analysis: Risks, Assumptions, Issues, Dependencies (Scrum/Agile)](https://www.techagilist.com/agile/scrum/raid/)." techagilist.com (accessed 2026-07-22). Supports RAID's waterfall lineage and the Kanban-board-as-lighter-alternative argument ("This technique has been borrowed from the domain of traditional (waterfall) project management, which typically calls for the creation of a deliverable such as a 'RAID log.'"; "It's much easier to manage RAID log via Kanban Board instead of a spreadsheet."). Undated. [practitioner]

<a id="ref-24"></a>[24] Essendrup, Kim. "[But we're agile! Why would I need a RAID?](https://raidlog.com/book-excerpts/part-6-but-were-agile-why-would-i-need-a-raid/)" raidlog.com (book excerpt) (accessed 2026-07-22). Supports the methodology-agnostic argument and the accountability case ("A RAID log is just as useful and relevant whether you follow an agile methodology or a more predictive 'waterfall' methodology."; "if you're in an area of responsibility, something goes wrong, and an exec says, 'what happened here?'...You and your team need to have an answer - an answer you can get from your RAID log."). The author sells RAID-log software; the position is contested by [[20]](#ref-20). [practitioner]

<a id="ref-25"></a>[25] RJK.info. "[Managing project RAID: Risks, Assumptions, Issues, Dependencies (template)](https://www.rjk.info/post/managing-project-raid-risks-assumptions-issues-dependencies-template)." rjk.info (accessed 2026-07-22). A concise canonical field list per quadrant ("Assumptions: ID, Description, Validity Date, Owner, Impact if False, Status"; "Issues: ID, Description, Priority, Owner, Resolution Plan, Status"; "Dependencies: ID, Description, Dependent On, Impact, Owner, Status"). [practitioner]
