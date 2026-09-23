# Companion: The Issue Log

> The deep explainer for the issue-log bundle. Read this to understand what an issue log is, where it
> came from, why it is shaped the way it is, and where practitioners disagree about it. The short
> operator card is [`issue-log_guide.md`](issue-log_guide.md); a fully worked instance is
> [`issue-log_example.md`](issue-log_example.md). Inline citations like [[1]](#ref-1) resolve to the
> [References](#references) at the bottom, tagged by source reliability.

---

## 1. Orientation

An issue log is **the written record a project or program keeps of problems that need someone above the
day-to-day work to act on them: what the problem is, who owns getting it fixed, whether it has been
escalated, and when it is genuinely closed.** The European Commission's PM² guide states the job plainly:
*"The Issue Log is a register (log file) used to capture and maintain information on all issues that are
being formally managed"* [[1]](#ref-1). PMI's *Lexicon* names the same artifact in one line: *"A project
artifact where information about issues is recorded and monitored"* [[2]](#ref-2).

The honest first thing to know is that an issue log is one of the most widely published project documents
there is, and the sources that publish it agree on almost nothing except that it is not a risk register.
Four different standards bodies state four different definitions of the thing the log is supposed to hold
(section 6), two authors disagree with each other inside the same article about how often to review it
[[15]](#ref-15), and no two of the freely available published templates carry quite the same field list
(section 3). This bundle's job is not to resolve that disagreement. It is to make a team decide, in
writing, the three things the sources leave open: what counts as an issue here, when an issue goes up, and
what "closed" means.

**At a glance**
- Named by every major body checked: PMI's *Lexicon* [[2]](#ref-2), the *PMBOK Guide* [[3]](#ref-3), APM's
  glossary [[4]](#ref-4), PRINCE2's 2009 glossary [[8]](#ref-8), and the European Commission's PM² guide
  with a full field list [[1]](#ref-1).
- **What counts as an issue is contested**, and this template forces a stated threshold rather than
  inheriting an ambiguous one (section 6).
- It is **not a risk register**: a risk might happen, an issue already has, or is judged close enough to
  certain to require action now (section 8). A materialized risk becomes an issue and the risk entry closes
  as occurred, linked both ways [[27]](#ref-27).
- It is the **deepened, standalone form of a RAID log's Issues quadrant** [[28]](#ref-28)[[29]](#ref-29).
  This library places it beside the risk register, which stands to a RAID log's Risks quadrant the same
  way; that parallel is the family's own framing, not a claim either source makes.
- **One named person owns each issue** [[1]](#ref-1); escalation is decided before it is needed, not
  invented in the moment [[1]](#ref-1)[[19]](#ref-19)[[24]](#ref-24); and Resolved is not the same state as
  Closed [[1]](#ref-1)[[19]](#ref-19).

If you read nothing else: an issue log is a **living, owned record of things that have already happened
and require action**, distinguished from a risk register by tense (something that occurred, not something
that might) and made useful only by a threshold, an escalation rule, and a definition of closed that the
team actually writes down rather than assumes everyone shares.

---

## 2. Origins and evolution

**The issue log has no single origin either**, in the sense that no source names an inventor or a founding
document. What the record shows instead is convergent naming across every major standards body, each
arriving at the same document from its own tradition. PMI's *Lexicon of Project Management Terms* defines
both halves of the artifact directly: *"issue. A current condition or situation that may have an impact on
one or more objectives"* and *"issue log. A project artifact where information about issues is recorded
and monitored"* [[2]](#ref-2). The *PMBOK Guide* (sixth edition) lists the issue log as a named project
document produced from its issue-management process, and separately names a change log used to record all
submitted change requests, without stating a rule for where the two overlap [[3]](#ref-3). APM's glossary
defines the same artifact from a tolerance-based tradition: *"A log of all issues raised during a project
or programme, showing details of each issue, its evaluation, what decisions were made and its current
status"* [[4]](#ref-4).

PRINCE2's lineage is the clearest case of the definition actually changing over time. The 2009 glossary
defines an issue as *"a relevant event that has happened, was not planned, and requires management
action"* and the Issue Register as the place it is captured [[8]](#ref-8). PRINCE2 7 (2023) widened the
definition considerably: PeopleCert, the method's examining institute, states that *"in PRINCE2 7, the
broad definition of issues is 'anything that could affect the project'"*, and adds the governing rule that
*"not all issues result in changes. But all changes start as issues"* [[10]](#ref-10). This bundle states
only that PRINCE2 7 changed the definition, on PeopleCert's authority as the method's own examining body;
one training provider's page, dated before PRINCE2 7's release and written throughout in sixth-edition
terms despite its PRINCE2 7 title, is recorded here only as a hazard against citing it for anything
[[14]](#ref-14).

**PM² is the source this bundle draws its structure from**, and for a reason beyond thoroughness: of the
sources read, it is the one that publishes the complete artifact, every field defined, under a licence that
permits adaptation: *"Reproduction and reuse is authorised provided the source is acknowledged"*
[[1]](#ref-1). That is the reverse of a hazard this library has hit in an earlier bundle, where an origin
source's terms forbade derivatives; here the origin source invites them.

Two limits are worth stating plainly rather than working around. ISO 21502:2020 defines an issue as *"event
that arises during a project (3.20) requiring resolution for the project to proceed"* and lists *"7.9
Issues management"* as a practice clause beside risk management, but its clause body sits past the free
preview this research could read [[7]](#ref-7). **Nothing in this bundle claims that ISO names an issue
log**, because nothing readable said so. And AXELOS's own PRINCE2 manuals sit behind a subscription this
research did not hold; PRINCE2 enters this companion instead through its openly reproduced 2009 glossary
[[8]](#ref-8), PeopleCert's account of the PRINCE2 7 change [[10]](#ref-10), and prince2.wiki's practitioner
pages [[11]](#ref-11)[[12]](#ref-12)[[13]](#ref-13).

---

## 3. Anatomy (section by section)

The template carries seven sections in full, five of them in lean. Every field name below is one a real,
published source carries; where a plan text and a log disagree about a field's presence, that
disagreement is stated rather than smoothed over.

### Purpose and Threshold

**What it is:** a short statement of what counts as an issue on this project and what does not, plus the
line that separates a logged issue from a problem the team simply fixes in passing. **Why it exists:**
because the sources genuinely disagree about the definition (section 6), the single most useful sentence
in an issue log is the one that says what its rows mean here. APM's Body of Knowledge supplies the reason a
threshold matters at all: *"issues are differentiated from problems that are dealt with on a day-to-day
basis by the project manager and team"* [[5]](#ref-5). A worked example of a stated threshold comes from a
government issue-management plan: *"the event cannot be resolved at the project team level within three
days"* [[19]](#ref-19). PRINCE2's practitioner literature draws the same line from the other side, keeping
informal concerns out of the formal register entirely: the register's purpose is *"to capture and maintain
information about all formal issues that require attention or decision-making"* [[12]](#ref-12), a
different population from every day-to-day concern a team raises and resolves without ever writing it down.

### Priority Scale

**What it is:** however the team ranks issues for attention, which the published sources split three
different ways. PM² scores urgency and impact separately on parallel one-to-five scales, from *"5=Very
high"* to *"1=Very low"* [[1]](#ref-1); a Connecticut state government template instead names five impact
levels outright, from *"1 - Low; easily mitigated by an individual or team"* to *"5 - Catastrophic; Impact
to Cost/Schedule/Scope resulting in project failure"*, alongside a separate Material or Non-Material split
[[18]](#ref-18); a third published log assesses impact against named cost, schedule, and quality dimensions
directly rather than a numeric scale [[36]](#ref-36). APM's Body of Knowledge frames what any of these
scales is actually weighing: *"the relative priorities of scope, quality, time, cost and benefits"*
[[5]](#ref-5). **One honest correction belongs here.** PM²'s own plan text (Appendix B.4) refers to a scale
of "priority", but its log fields (Appendix B.9) carry no field literally named priority, only urgency,
impact, and size; this template follows PM²'s field list as printed and does not claim a priority field
that its own primary source does not carry [[1]](#ref-1).

### Issues

**What it is:** the load-bearing table, one row per issue. Every published field list agrees on a small
spine, ID, description, owner, and status, and then diverges on everything else. PM² names the owner field
precisely as *"the person accountable for resolving the issue"* [[1]](#ref-1), and its status vocabulary is
four values, with Open, Postponed, Resolved, and Closed each separately defined [[1]](#ref-1). The
description column is written to carry both cause and consequence, following APM's account of what
analysis at the point of logging should capture: *"the nature of the issue, its causes and impacts"*
[[5]](#ref-5). This template's row set gains a **Last updated** column beyond PM²'s own field list, a field
three independently published sources carry and PM²'s does not [[9]](#ref-9)[[16]](#ref-16)[[37]](#ref-37).
Two other published field lists were checked and show how much a "standard" table still varies in practice:
one carries free-text resolution notes and no confirmer or last-updated field at all [[35]](#ref-35), and
another has neither a risk-origin field, a confirmer field, nor a last-updated field, treating lessons
learned as a use of the log rather than a column in it [[34]](#ref-34).

### Escalation

**What it is:** the record of what went up, to whom, when, and what decision is awaited. **Why it exists:**
because every source that discusses escalation agrees it should happen and disagrees completely about what
triggers it. One university PMO playbook runs a role ladder with no timer, escalating only when the current
holder cannot resolve the issue: *"if the delay cannot be resolved through the Project Manager's direct
engagement, the Project Manager should then escalate the issue to the Functional Lead"* [[21]](#ref-21). A
vendor's escalation framework instead runs a clock: *"the aging clock starts on the day the issue is first
logged, not the day the PM decides it's serious"*, and records *"the issue, the date first logged, the date
escalated, the decision made, the authority who made it, and the outcome"* [[24]](#ref-24). PM² runs neither
a ladder nor a clock by default but a per-issue flag set against thresholds fixed in advance in the Issue
Management Plan: *"whether or not the issue is to be escalated to the Directing or Steering Layers (Yes or
No)"* [[1]](#ref-1). No source read reconciles these three shapes, so the template's guidance offers all
three rather than picking one. **One correction is worth recording here too.** An earlier pass of this
bundle's own research reported that no source carries a dedicated escalation field, and separately that
PM²'s Issue Log has no field for cross-references. Both were wrong: the primary text, read directly, carries
the escalation field quoted above and a Traceability/Comments field linking an issue to related changes,
risks, or decisions [[1]](#ref-1). Elsewhere, escalating is treated as a request for help rather
than an accusation: *"stay factual, talk about the implications for the project"* and *"go to them with a
solution in mind"* [[23]](#ref-23).

### Review and Ownership

**What it is:** the stated cadence, the owner of the log itself, and which issues get looked at first. The
fullest published lifecycle comes from a government issue-management plan: *"issue reviews are scheduled
weekly"* with *"review priority... given to high severity and escalated issues"* [[19]](#ref-19). Cadence
is a genuine point of disagreement rather than a settled default: two authors of the same practitioner
article disagree with each other inside it, one writing *"we review the open issues on the issue log every
week"* and the other that *"issues recorded in the issues register should be discussed almost every day"*
[[15]](#ref-15). A university PMO's practice sits between the two, folding issue review into governance
that already meets rather than convening a separate log-review meeting: *"progress of the issue should be
reviewed regularly through the project board or steering group"* [[22]](#ref-22). This bundle reports the
disagreement rather than resolving it.

### Closed Issues

**What it is:** a lean-excluded section holding resolution detail, confirmation, the closed date, and any
lesson learned. **Why it exists as a separate block:** because Resolved and Closed are not the same state,
and conflating them is one of this artifact's live definitional gaps (section 6). PM² defines them
separately, with Closed meaning *"all work is completed and verified"* [[1]](#ref-1), and the same
government plan puts a second person in the loop before that verification happens: *"the issue originator
reviews a resolved issue and verifies it can be closed"* [[19]](#ref-19). Lessons learned belong here rather
than as an afterthought: PM²'s own management plan instructs teams to *"specify the procedure for updating
the Lessons Learned after an issue is resolved"* [[1]](#ref-1), and prince2.wiki's practitioner guidance to
the register agrees: *"capture lessons learned from resolved issues"* [[12]](#ref-12).

### Links to Other Logs

**What it is:** the second lean-excluded section, recording the origin risk if the issue began as one, any
change request it was handed to change control as, the decision that closed it, and the tasks that
implement its fix. This is PM²'s Traceability field made explicit as its own block: *"the ID(s) of the
tasks (in the Project Work Plan) that implement the issue actions, and/or the IDs of related changes,
risks, or decisions"* [[1]](#ref-1). The risk half of that link has its own convention worth stating: a
risk that materializes *"closes as occurred, which is what preserves the evidence that the event was
foreseen"*, rather than being deleted or marked withdrawn [[27]](#ref-27).

---

## 4. Variants and sizing

**Lean** is the smallest complete issue log: **Purpose and Threshold**, **Priority Scale**, the **Issues**
table, **Escalation**, and **Review and Ownership**. It is a working log a team can populate and review
from week one, and it is enough for a project whose issues resolve inside the team without needing a
change-control hand-off or a lessons-learned record.

**Full** is a strict superset, adding **Closed Issues** (resolution, confirmer, closed date, lesson
learned) and **Links to Other Logs** (origin risk, change request, decision, implementing tasks). Move to
full when issues start resolving into other artifacts often enough that losing the trail matters: a
materialized risk that should close its register entry as occurred [[27]](#ref-27), a request for change
that PRINCE2's convention says should be handed to change control [[10]](#ref-10), or a governance board
that will ask, weeks later, what was actually decided and why.

---

## 5. Methodology lineage

- **PM² (European Commission).** The fullest published field list this research found, and the only source
  it may adapt directly, under an open licence [[1]](#ref-1). Separates the rules, held in an Issue
  Management Plan, from the register itself: *"the structure of the Issue Log is defined in the Issue
  Management Plan"* [[1]](#ref-1).
- **PMI / PMBOK.** The broadest definition of the four (section 6), a named project document, and a
  separate change log with no stated rule for where the two overlap [[2]](#ref-2)[[3]](#ref-3).
- **APM.** A tolerance-based definition, distinguishing issues from routine day-to-day problems and tying
  prioritization to the classic scope, quality, time, cost, and benefits trade-off [[4]](#ref-4)[[5]](#ref-5).
  Escalation runs upward through the sponsor to a governance board [[5]](#ref-5).
- **PRINCE2.** The definition itself changed between the 2009 edition (something that has already happened
  [[8]](#ref-8)) and PRINCE2 7 (anything that could affect the project [[10]](#ref-10)), and PRINCE2 folds
  requests for change into the issue concept rather than routing them elsewhere from the start
  [[10]](#ref-10). A distinct, deeper artifact, the issue report, exists for issues that need formal
  handling beyond a register row [[13]](#ref-13).
- **ISO 21502.** Names an issue and a practice clause for managing issues; whether it names an issue log by
  that title sits past the free preview this research could read, so this bundle does not say either way
  [[7]](#ref-7).
- **Agile / RAID.** The issue log's natural companion here is the RAID log, where Issues is one of four
  quadrants tracking things that have already happened [[28]](#ref-28)[[29]](#ref-29). Agile's own
  team-level equivalent, an impediments backlog, is scoped more narrowly to immediate blockers rather than
  the whole project's record of problems [[31]](#ref-31); the Scrum Guide itself names removing impediments
  as a Scrum Master accountability but prescribes no log for them [[32]](#ref-32).

---

## 6. Debates and contested boundaries

**What an issue even is, stated four ways.** PM² and PRINCE2 2009 agree an issue is something that has
already happened: *"an issue is any unplanned event related to the project that has already happened and
requires the intervention of the Project Manager (PM) or higher management"* [[1]](#ref-1), and *"a
relevant event that has happened, was not planned, and requires management action"* [[8]](#ref-8). APM
instead draws the line at tolerance: *"a problem that is now breaching, or is about to breach, delegated
tolerances"* [[4]](#ref-4). PRINCE2 7 moves toward risk with a forward-looking definition, *"anything that
could affect the project"* [[10]](#ref-10). PMI's *Lexicon* is broader still, requiring neither an event
nor a tolerance breach: *"a current condition or situation that may have an impact on one or more
objectives"* [[2]](#ref-2). One practitioner wiki page states two of these four positions on the same page
without reconciling them [[11]](#ref-11). This template does not pick a winner; it requires the team to
state its own threshold in the Purpose and Threshold section (section 3).

**Whether a request for change is an issue.** PRINCE2 says yes, definitionally: an issue can be *"a
problem, a concern, a business opportunity, a request for change, or something off-specification"*, and
*"not all issues result in changes, but all changes start as issues"* [[10]](#ref-10). A government
template built on PRINCE2 follows suit, recording changes on the issue log directly [[16]](#ref-16). PMI
instead names a separate change log for submitted change requests and states no rule for the overlap
[[3]](#ref-3); one practitioner states the opposite convention as a personal choice: *"some people also
manage changes to the project as issues, but personally, I don't"* [[28]](#ref-28). This is a live,
unreconciled split; the template names both conventions and asks the team to record which one it follows.

**Review cadence.** Two authors of the same article disagree with each other about how often an issue log
should be reviewed, one saying weekly and the other saying almost daily [[15]](#ref-15). A government
issue-management plan settles on weekly with triage by severity [[19]](#ref-19).

**Escalation trigger: a ladder, a clock, or a flag.** Section 3 above lays out all three published shapes
[[21]](#ref-21)[[24]](#ref-24)[[1]](#ref-1). No source read reconciles them into one rule.

**Resolved and closed.** PM² defines them as two distinct states, with Closed requiring completed and
verified work [[1]](#ref-1). A government issue-management plan puts a second person, the issue's
originator, in the loop to verify a resolved issue before it can be closed, but then records the final
state as "Resolved" with a separate closed date rather than moving it to a distinct "Closed" status
[[19]](#ref-19). One university PMO's own glossary does not separate the two terms at all [[21]](#ref-21).
This bundle defines both terms itself, drawing the distinction from [[1]](#ref-1) and the confirmation step
from [[19]](#ref-19), and says so rather than presenting the split as settled industry consensus.

**What the register is even called.** The same two-author article disagrees on this too: *"I call the
issue register the 'issue log' because it denotes logging of something that already has happened"*
[[15]](#ref-15). APM treats the two names as synonyms outright [[4]](#ref-4); PRINCE2 uses "register"
throughout [[8]](#ref-8). This bundle uses "issue log" as its title and treats "issue register" as the same
artifact.

**Whether PRINCE2 7 relocated the register.** Two practitioner sources place the PRINCE2 7 issue record
inside a single combined project log rather than a standalone register [[12]](#ref-12), but one of the two
is the training-provider page already flagged as unreliable on edition [[14]](#ref-14). This bundle states
only that PRINCE2 7 changed the definition of an issue [[10]](#ref-10), not where PRINCE2 7 files the
record, because the more reliable of the two sources on the relocation question is the one this research
distrusts.

---

## 7. Anti-patterns and failure modes

**A deliberate honesty check belongs first.** Four failure modes a reader would reasonably expect an issue
log to suffer from, that it becomes a dumping ground for everything, that it duplicates a ticket tracker,
that it gets used to assign blame, or that it simply never closes anything, were searched for specifically
in this research, including in audit and inspector-general reports, and none turned up as a documented,
observed failure of an issue log by name. **This bundle does not assert any of the four.** What the
research did find, below, is narrower and mostly prescriptive rather than a record of an actual incident.

1. **No owner.** *"If the issue doesn't have an owner, it's likely never to get resolved"* [[38]](#ref-38).
   One RAID-management source names why ownership goes missing in the first place, not specific to issue
   logs but the same dynamic: *"nobody wants to create conflict at kickoff by assigning ownership of
   something potentially difficult"* [[26]](#ref-26). Fix: one named person, never a role and never "the
   team", on every row.
2. **Nobody reviews it.** *"This task often gets neglected when project managers get busy"* [[12]](#ref-12).
   Fix: a stated cadence, reviewed by someone other than the person who is supposed to be doing the review.
3. **Raised late, decided badly.** APM's Body of Knowledge names two distinct barriers in the same
   sentence: *"a lack of time or reluctance from project professionals to identify and escalate issues
   early"*, and, once an issue does reach governance, *"an inability of the governance board to make an
   informed decision that addresses the root cause of the issue rather than treating the symptoms"*
   [[5]](#ref-5). Fix: log it immediately [[22]](#ref-22), and escalate with a proposed solution rather
   than a bare problem [[23]](#ref-23).
4. **Aging without movement.** These are prescriptions, not measured incidents: *"never let a RAID item go
   more than two reviews without movement"* [[26]](#ref-26); *"unresolved issues will damage the project"*
   [[25]](#ref-25). Fix: the Last updated field this template adds beyond PM²'s own list (section 3), and a
   review cadence that actually looks at stale rows.
5. **Blame.** Named as a warning, not an observed pattern: *"adding additional layers of complexity by
   introducing conflict, blame or other emotions will not help the resolution of the issue"*
   [[25]](#ref-25). Fix: escalate to get a decision, never to assign fault.

---

## 8. Relationships to other artifacts

**Issue log vs risk register.** They are separated by tense, not by subject: a risk register holds things
that have not happened yet, and an issue log holds things that have. Multiple independent sources draw the
same boundary from different traditions [[15]](#ref-15)[[5]](#ref-5)[[27]](#ref-27), and PRINCE2's own
practitioner wiki states the resolving rule directly: an uncertain concern belongs on the risk register,
and *"when categorizing issues, it's helpful to check if the issue is actually a risk... if this is the
case, the issue should be transferred to the risk register"* [[11]](#ref-11). The direction that matters
most for this template is the other one: when a risk materializes, it becomes an issue, and the risk entry
*"closes as occurred, which is what preserves the evidence that the event was foreseen"* rather than being
deleted [[27]](#ref-27). Both entries keep a link back to each other. This bundle's sibling
[`risk-register`](../risk-register/risk-register_guide.md) is where the standalone, deepened form of that
boundary lives.

**Issue log vs RAID log.** A RAID log's Issues entries are the same population an issue log holds,
formalized: *"things that have happened and are causing a problem on your
project get added to the issue log, which is one part of the RAID log"* [[28]](#ref-28), and *"an issue log
can help formalize this tracking"* [[29]](#ref-29). This library's framing, not those sources', is that the
issue log stands to the RAID log's Issues quadrant exactly as the standalone risk register stands to its
Risks quadrant: the deepened, single-subject form of one column in a four-column consolidation. This bundle's
sibling [`raid-log`](../raid-log/raid-log_guide.md) is that consolidation.

**Issue log vs KPI dashboard.** The dashboard tracks performance against targets; the issue log tracks
problems that have happened. A realized problem can show on the dashboard first, as a metric turning amber,
and the issue log is where it gets an owner, a next action and a confirmed close; neither carries the other's
rows. This is this library's own positioning within the family, not a claim drawn from any source above; no
source read compares the two directly.

**Issue log vs change log or change control.** PRINCE2's convention folds requests for change into the
issue concept, with the rule that every change starts as an issue even though not every issue becomes a
change [[10]](#ref-10); a government template following PRINCE2 records changes on the issue log directly
[[16]](#ref-16). PMI's convention instead keeps a separate change log for submitted change requests
[[3]](#ref-3), and at least one practitioner makes the same separation a personal choice rather than a rule
[[28]](#ref-28). The template records whichever convention the team follows, in Links to Other Logs.

**Issue log vs decision log and action log.** One vendor source defines both of the other two logs plainly:
*"a decision log records what decisions were made, why they were made, and who made them"*, and *"decision
logs capture choices, whereas action logs track execution"* [[30]](#ref-30). That source never mentions an
issue log at all, so the boundary drawn here, that an issue log tracks the problem itself while a decision
log records what was decided about it and an action log tracks the resulting work, is this library's own
reasoning from those two definitions, not a claim any source makes about issue logs directly.

**Issue log vs impediments backlog.** An agile team's impediments backlog is scoped to immediate blockers
in front of the team right now; the issue log is broader: *"the impediments backlog is more specific to
immediate team impediments, while the issue log is a comprehensive record of all project-related
problems"* [[31]](#ref-31). The Scrum Guide itself prescribes no log for impediments at all, naming only
their removal as an accountability [[32]](#ref-32).

**Issue log vs a software bug or ticket tracker.** No source read compares the two directly; one reference
source divides categories of tracking software from each other, not a project issue log from a software
tracker [[33]](#ref-33). Any boundary drawn between a project issue log and a bug tracker in this bundle is
therefore this library's own judgment, not a sourced distinction.

---

## 9. Adaptations

- **PM²-based teams.** Adopt the field list as printed, including the separate urgency and impact scales
  and the four-value status vocabulary, with attribution, since PM² is the source this bundle may adapt
  directly [[1]](#ref-1).
- **PRINCE2 teams.** Decide explicitly whether requests for change are recorded on the issue log, following
  PRINCE2's own convention [[10]](#ref-10)[[16]](#ref-16), or routed to a separate change log, following
  PMI's [[3]](#ref-3); either is defensible, but say which.
- **Agile teams.** Keep the team's immediate blockers on an impediments backlog or the board itself
  [[31]](#ref-31), and reserve the issue log for the project-wide record that survives longer than a
  sprint; review it inside governance that already meets rather than adding a new meeting
  [[22]](#ref-22).
- **Larger or governed programs.** Choose an escalation rule deliberately, a role ladder [[21]](#ref-21), an
  aging clock [[24]](#ref-24), or a plan-held per-issue threshold [[1]](#ref-1), rather than improvising
  one when the first serious issue arrives.
- **Public-sector and government teams.** Several public bodies already publish working issue log
  structures freely, though none states a reuse licence, so they are useful as structure evidence rather
  than adaptable source text [[16]](#ref-16)[[17]](#ref-17)[[18]](#ref-18)[[20]](#ref-20).

---

## 10. Worked example

[`issue-log_example.md`](issue-log_example.md) is the full-variant issue log for the same **Reporting
Platform Modernization** program that the [`risk-register`](../risk-register/risk-register_example.md) and
[`raid-log`](../raid-log/raid-log_example.md) examples cover, dated to match the RAID log's last review.
It carries the same two open issues the RAID log's Issues quadrant records, deepened with the fields this
template adds beyond a RAID row: full escalation history, confirmation and closure detail, and links back
to the risk that one of them materialized from. It demonstrates the risk-to-issue conversion this companion
describes in section 8, an issue that started as a risk on the register and closed that risk entry as
occurred when it materialized.

---

## References

<a id="ref-1"></a>[1] European Commission. "[PM² Project Management Methodology Guide](https://www.pm2alliance.eu/wp-content/uploads/2024/02/pm%C2%B2-project-management-methodology-NO0523520ENN.pdf)." Open Edition v3.1, Publications Office of the European Union, 2023, Appendix B.4 Issue Management Plan and Appendix B.9 Issue Log (accessed 2026-09-23). The fullest published field list for the artifact, with the four-value status vocabulary, escalation and traceability fields, and a licence permitting reuse with attribution ("The Issue Log is a register (log file) used to capture and maintain information on all issues that are being formally managed."; "An issue is any unplanned event related to the project that has already happened and requires the intervention of the Project Manager (PM) or higher management."; "The structure of the Issue Log is defined in the Issue Management Plan."; "The person accountable for resolving the issue."; "Whether or not the issue is to be escalated to the Directing or Steering Layers (Yes or No)."; "The ID(s) of the tasks (in the Project Work Plan) that implement the issue actions, and/or the IDs of related changes, risks or decisions (Log entries)."; "5=Very high, 4=High, 3=Medium, 2=Low, 1=Very low"; "Open: The issue has been identified and requires attention and, if possible, a resolution."; "Resolved: This status indicates that all necessary actions are completed, and the issue is resolved."; "Closed: This status indicates that all work is completed and verified."; "Specify the procedure for updating the Lessons Learned after an issue is resolved."; "Reproduction and reuse is authorised provided the source is acknowledged."). Its plan text (B.4) refers to a "priority" scale its log fields (B.9) do not carry by that name. [primary]

<a id="ref-2"></a>[2] Project Management Institute. "[Lexicon of Project Management Terms](https://www.pmi.org/-/media/pmi/documents/registered/pdf/pmbok-standards/pmi-lexicon-pm-terms.pdf)." Version 5.0, last updated January 2026 (accessed 2026-09-23). PMI's own definitions of an issue and the issue log, the broadest of the four contested definitional positions ("issue. A current condition or situation that may have an impact on one or more objectives."; "issue log. A project artifact where information about issues is recorded and monitored."). Licensed for personal use only; quoted briefly, never adapted. [primary]

<a id="ref-3"></a>[3] Project Management Institute. "[A Guide to the Project Management Body of Knowledge (PMBOK Guide)](https://www.pmi.org/-/media/pmi/documents/public/pdf/pmbok-standards/pmbok-guide-6th-edition-5th-printing.pdf?v=5ec5b4d9-abb5-4d42-8542-8af75be7de3b)." Sixth Edition, errata, fifth printing (accessed 2026-09-23). Names the issue log as a project document and a separate change log for submitted change requests, with no stated rule for the overlap ("Issue log. Described in Section 4.3.3.3."; "New issues raised as a result of this process are recorded in the issue log."; "The change log is used to record all submitted change requests."). The errata only; the PMBOK Guide itself was not read. [primary]

<a id="ref-4"></a>[4] Association for Project Management. "[Glossary](https://www.apm.org.uk/resources/glossary/)." apm.org.uk (accessed 2026-09-23). APM's tolerance-based definition of an issue and the issue log, and its treatment of "issue register" as a synonym ("A problem that is now breaching, or is about to breach, delegated tolerances for work on a project or programme."; "A log of all issues raised during a project or programme, showing details of each issue, its evaluation, what decisions were made and its current status."; "Issue register  See Issue log."). No licence stated. [primary]

<a id="ref-5"></a>[5] Association for Project Management. "[APM Body of Knowledge](https://www.apm.org.uk/media/qpyau3pc/apm-body-of-knowledge-7th-edition-for-supporting-2025-consultation.pdf)." 7th edition, consultation copy, section 4.3.5 Issue management (accessed 2026-09-23). The threshold that separates an issue from a day-to-day problem, the analysis performed at logging, prioritization against scope/quality/time/cost/benefits, the escalation path to the sponsor and governance board, and the two named barriers to issue management working ("Issues are differentiated from problems that are dealt with on a day-to-day basis by the project manager and team."; "When an issue is detected, it is logged in an issue register and analysis is performed quickly to understand the nature of the issue, its causes and impacts if it is not resolved."; "the relative priorities of scope, quality, time, cost and benefits"; "Issues are escalated to the sponsor, who may, in turn, escalate them to the governance board for resolution."; "a lack of time or reluctance from project professionals to identify and escalate issues early"; "an inability of the governance board to make an informed decision that addresses the root cause of the issue rather than treating the symptoms"). Marked for APM members only; quoted briefly, adapted nowhere. [primary]

<a id="ref-7"></a>[7] International Organization for Standardization. "[ISO 21502:2020](https://cdn.standards.iteh.ai/samples/74947/d2f2b2e60a8249ab88240adc92be71ad/ISO-21502-2020.pdf)." Project, programme and portfolio management, Guidance on project management, first edition 2020-12, official free preview (accessed 2026-09-23). ISO's definition of an issue and its practice-clause title; whether ISO names an issue log sits past the preview and this bundle does not claim it either way ("event that arises during a project (3.20) requiring resolution for the project to proceed"; "7.9 Issues management"). Clause body paywalled. [primary]

<a id="ref-8"></a>[8] AXELOS. "[PRINCE2 Glossary of Terms](https://www.stakeholdermap.com/prince2/prince2-glossary-I-impact.html)." 2009 edition, entries "Issue" and "Issue Register", reproduced with AXELOS's permission by stakeholdermap.com (accessed 2026-09-23). PRINCE2 2009's definition of an issue as something that has already happened, the Issue Register, and requests for change inside the issue concept ("A relevant event that has happened, was not planned, and requires management action."; "It can be any concern, query, request for change, suggestion or off-specification raised during a project."; "A register used to capture and maintain information on all of the issues that are being managed formally."). 2009 edition, superseded twice; AXELOS copyright, reproduced with permission. [primary]

<a id="ref-9"></a>[9] stakeholdermap.com. "[PRINCE2 Issue Register](https://www.stakeholdermap.com/project-templates/prince-2-issue-register.html)." Reproducing AXELOS material (accessed 2026-09-23). The PRINCE2 Issue Register's column headers, including a last-updated date distinct from the closure date ("The Purpose of the Issue Register is to capture and maintain information on all of the issues that are being formally managed."). Headers only; AXELOS copyright. [primary]

<a id="ref-10"></a>[10] PeopleCert. "[PRINCE2 7 Issues: not every issue equals a change](https://www.peoplecert.org/news-and-announcements/prince2-7-issues)." peoplecert.org (accessed 2026-09-23). PRINCE2 7's widened, forward-looking definition of an issue, its issue types, and the rule connecting issues to change ("In PRINCE2 7, the broad definition of issues is "anything that could affect the project"."; "for example, issues can be either a problem, a concern, a business opportunity, a request for change, or something off-specification."; "Not all issues result in changes. But all changes start as issues."). PeopleCert examines PRINCE2, describing its own method's change. [vendor]

<a id="ref-11"></a>[11] Frank Turley (EMPII Group). "[Issues](https://prince2.wiki/practices/issues/)." prince2.wiki (accessed 2026-09-23). Two PRINCE2 definitions stated on one page without reconciliation, and the rule that an uncertain concern transfers to the risk register ("Any expectation different from the baselines is called an issue in PRINCE2."; "An issue is an event relevant to the project that requires project management consideration."; "When categorizing issues, it's helpful to check if the issue is actually a risk. Risks are uncertain, and if this is the case, the issue should be transferred to the risk register."). Creative Commons Attribution. [practitioner]

<a id="ref-12"></a>[12] Frank Turley (EMPII Group). "[Issue register](https://prince2.wiki/management-products/project-log/issue-register/)." prince2.wiki (accessed 2026-09-23). The register's purpose as formal issues only, review neglected under load, lessons from resolved issues, and linking an issue to its originating risk ("The primary purpose of the issue register is to capture and maintain information about all formal issues that require attention or decision-making."; "A risk becomes an issue once it materializes."; "This task often gets neglected when project managers get busy"; "Capture lessons learned from resolved issues"). Creative Commons Attribution. [practitioner]

<a id="ref-13"></a>[13] Frank Turley (EMPII Group). "[Issue report](https://prince2.wiki/management-products/issue-report/)." prince2.wiki (accessed 2026-09-23). The issue report as a distinct, deeper document from the register row, for issues needing formal handling ("An issue report provides a detailed description and impact assessment of one or more issues that require formal handling."; "Not all entries in the issue register require a standalone issue report"). Creative Commons Attribution. [practitioner]

<a id="ref-14"></a>[14] Projex Academy. "[PRINCE2 7 Issues and Change Control](https://www.projex.com/prince2-7-issues/)." projex.com, dated 3 April 2023 (accessed 2026-09-23). Recorded here only as an attribution hazard: titled and addressed as PRINCE2 7 material, dated before PRINCE2 7's release, and written throughout in sixth-edition terms. Supports nothing in this bundle. [vendor]

<a id="ref-15"></a>[15] Duraideivamani Sankararajan and N. K. Shrivastava. "[Risks vs. issues](https://www.pmi.org/learning/library/risks-vs-issues-project-failure-2328)." PM Network 26(6), pp. 28-29, Project Management Institute, June 2012 (accessed 2026-09-23). Two practitioners' account of the risk-and-issue boundary, the fields the register tracks, moving a materialized risk into the log, and their own internal disagreement about review cadence and the register's name ("Risk is an event that has not happened yet but may; an issue is something that already has happened."; "When a risk is materialized, I move it to the issue log and the person who was assigned to the risk now works on the issue."; "I call the issue register the "issue log" because it denotes logging of something that already has happened."; "We review the open issues on the issue log every week."; "Issues recorded in the issues register should be discussed almost every day"). [practitioner]

<a id="ref-16"></a>[16] Northern Ireland Civil Service, Centre of Expertise for Programme and Project Management. "[Issue Log](https://www.finance-ni.gov.uk/sites/default/files/publications/dfp/Programme%20and%20project%20management%20templates%20-%20issue%20log.DOC)." Generic PPM Templates, V1.0 (accessed 2026-09-23). A government issue log derived from PRINCE2, carrying a last-updated column and recording changes on the issue log directly ("based on the PRINCE2 recommended issue log"; "Issues, including those raised as changes under the project change control mechanism, should be recorded on the issue log."). No licence stated; structure evidence only. [primary]

<a id="ref-17"></a>[17] Tasmanian Government, Department of Premier and Cabinet. "[Project Management Guidelines](https://www.dpac.tas.gov.au/__data/assets/pdf_file/0029/108992/Tasmanian_Government_Project_Management_Guidelines_V7_0_July_2011_2.pdf)." Version 7.0, July 2011, section 6 Issues management (accessed 2026-09-23). A government issues register structure and the rule that an unresolvable issue may become a risk ("A Project Issues Register is basically a form, often a table, for systematically recording issues."; "If an issue cannot be resolved, it could become a risk"). 2011; disclaimed to Tasmanian Government agencies; structure evidence only. [primary]

<a id="ref-18"></a>[18] Connecticut Department of Social Services, Enterprise Program Management Office. "[Project Issue Log](https://portal.ct.gov/-/media/Departments-and-Agencies/DSS/CT-METS/Library/General/CTDSSIssueLogv113.pdf)." v1.13 (accessed 2026-09-23). A five-level named impact scale and a Material/Non-Material priority split ("1 - Low; easily mitigated by an individual or team."; "5 - Catastrophic; Impact to Cost/Schedule/Scope resulting in project failure."). No licence stated; structure evidence only. [primary]

<a id="ref-19"></a>[19] Connecticut Department of Social Services (CT-METS). "[Issue Management Plan](https://portal.ct.gov/-/media/Departments-and-Agencies/DSS/CT-METS/Library/General/CTDSSIssueManagementPlanv11.pdf)." v1.1 (accessed 2026-09-23). The fullest published lifecycle: a worked logging threshold, a weekly review with priority triage, and closure verified by the issue's originator ("The event cannot be resolved at the project team level within three days"; "Issue reviews are scheduled weekly"; "Review priority is given to high severity and escalated issues"; "As notified by the issue owner, team or Project Manager, the issue originator reviews a resolved issue and verifies it can be closed"). Sets the final status to "Resolved" with a separate closed date rather than a distinct "Closed" status. No licence stated. [primary]

<a id="ref-20"></a>[20] Washington State Office of Financial Management. "[Issue Management Log](https://results.wa.gov/sites/default/files/issueTrackingTemplate.xls)." template (accessed 2026-09-23). An audit-context issue log that handles escalation by changing a decision-maker column rather than a status. Written for performance-audit issue tracking; no licence stated; structure evidence only. [primary]

<a id="ref-21"></a>[21] Colorado College, Office of Information Technology Services. "[ITS Project Management Office (PMO) Playbook](https://www.coloradocollege.edu/offices/its/PMO-Playbook-2024.pdf)." 2024-2025 (accessed 2026-09-23). An escalation ladder by role, triggered by inability to resolve, with no timer, and a glossary that does not separate Resolved from Closed ("If the delay cannot be resolved through the Project Manager's direct engagement, the Project Manager should then escalate the issue to the Functional Lead"; "If the issue remains unresolved after the Director of PMO's involvement and if there is no response from the Functional Lead, the Director of PMO will escalate the issue to the CIO"). [practitioner]

<a id="ref-22"></a>[22] University of Essex, Strategic Project Delivery. "[Risk and issue management](https://www.essex.ac.uk/staff/strategic-project-delivery/risk-issue-management)." essex.ac.uk (accessed 2026-09-23). Logging an issue immediately and reviewing it through existing governance rather than a separate meeting ("Issues should be logged immediately"; "Progress of the issue should be reviewed regularly through the project board or steering group"). [practitioner]

<a id="ref-23"></a>[23] Elizabeth Harrin. "[5 Scenarios where you should escalate a project issue](https://rebelsguidetopm.com/issue-escalation/)." Rebel's Guide to Project Management (accessed 2026-09-23). Escalation as a factual request for help with a proposed solution, not an accusation ("Stay factual, talk about the implications for the project"; "Go to them with a solution in mind"). [practitioner]

<a id="ref-24"></a>[24] Onplana (Devsoft Solutions). "[An Escalation Framework Project Managers Can Actually Use](https://onplana.com/blog/escalation-framework-pm)." onplana.com (accessed 2026-09-23). A worked aging-clock escalation model and what an escalation record holds ("The aging clock starts on the day the issue is first logged, not the day the PM decides it's serious"; "The issue, the date first logged, the date escalated, the decision made, the authority who made it, and the outcome"). A vendor's own model, adopted by no named organization. [vendor]

<a id="ref-25"></a>[25] Mosaic Projects. "[Issues Management](https://mosaicprojects.com.au/WhitePapers/WP1089_Issues_Management.pdf)." White Paper WP1089 (accessed 2026-09-23). A warning against blame in resolving issues and a prescription to escalate what the team cannot resolve ("adding additional layers of complexity by introducing conflict, blame or other emotions will not help the resolution of the issue"; "Unresolved issues will damage the project"). Prescriptive, not an account of an actual failure. [practitioner]

<a id="ref-26"></a>[26] Rocketlane. "[RAID Management: Complete Guide for PS Teams](https://www.rocketlane.com/blogs/raid-management)." rocketlane.com (accessed 2026-09-23). Why ownership goes missing at kickoff, and an aging rule for items that stop moving ("Nobody wants to create conflict at kickoff by assigning ownership of something potentially difficult"; "Never let a RAID item go more than two reviews without movement"). A vendor's prescription, not a measured finding. [vendor]

<a id="ref-27"></a>[27] Project Management Pathways. "[Risk register versus issue log: what goes in each, and the moment one becomes the other](https://projectmanagementpathways.com/articles/risk-register-vs-issue-log/)." projectmanagementpathways.com (accessed 2026-09-23). The moment a risk becomes an issue, closing the risk entry as occurred rather than deleting it, with a link kept both ways ("A risk becomes an issue the moment it happens"; "not deleted and not quietly marked withdrawn"; "keeps a link back to the risk it came from, and writes a note on both entries recording the conversion"; "it closes as occurred, which is what preserves the evidence that the event was foreseen"). [practitioner]

<a id="ref-28"></a>[28] Elizabeth Harrin. "[RAID logs in project management: How to actually use one](https://rebelsguidetopm.com/raid-in-project-management/)." Rebel's Guide to Project Management (accessed 2026-09-23). That a RAID log's Issues quadrant is the same population an issue log holds, and a practitioner's own split on managing changes as issues ("Things that have happened and are causing a problem on your project get added to the issue log, which is one part of the RAID log"; "Some people also manage changes to the project as issues, but personally, I don't"). [practitioner]

<a id="ref-29"></a>[29] Asana. "[RAID Log: Track Risks, Assumptions, Issues & Decisions](https://asana.com/resources/raid-log)." asana.com (accessed 2026-09-23). RAID's definition of an issue and a standalone issue log as the formalized version of RAID's Issues tracking ("Issues are problems that occur during a project that you did not anticipate."; "An issue log can help formalize this tracking"). [vendor]

<a id="ref-30"></a>[30] Eleco (PM3). "[What Is A Decision Log? The Essential Tool For Project Managers](https://eleco.com/pm3/knowledge-centre/decision-log/)." eleco.com (accessed 2026-09-23). What a decision log and an action log each hold; never mentions an issue log, so the boundary drawn from it here is this library's own reasoning ("A decision log records what decisions were made, why they were made, and who made them"; "decision logs capture choices, whereas action logs track execution"). [vendor]

<a id="ref-31"></a>[31] BrainBOK. "[Impediments Backlog](https://www.brainbok.com/guide/agile/agile-artifacts/impediments-backlog)." Agile artifacts guide (accessed 2026-09-23). The scope difference between an agile team's impediments backlog and a project-wide issue log ("An impediments backlog is a list of impediments, obstacles, or blockers that hinder progress in a project"; "The impediments backlog is more specific to immediate team impediments, while the issue log is a comprehensive record of all project-related problems"). [practitioner]

<a id="ref-32"></a>[32] Ken Schwaber and Jeff Sutherland. "[The 2020 Scrum Guide](https://scrumguides.org/scrum-guide.html)." scrumguides.org (accessed 2026-09-23). Scrum names impediment removal as an accountability and prescribes no log for impediments ("Causing the removal of impediments to the Scrum Team"). Licensed CC BY-SA 4.0. [primary]

<a id="ref-33"></a>[33] Wikipedia contributors. "[Issue tracking system](https://en.wikipedia.org/wiki/Issue_tracking_system)." wikipedia.org (accessed 2026-09-23). Distinguishes categories of software tracking tool from each other, not a project issue log from a bug tracker, so any such boundary in this bundle is its own judgment ("In bug trackers, issues are generally quality or feature related to the software codebase"). [reference]

<a id="ref-34"></a>[34] Rosemet. "[Issue Log Instructions](https://www.rosemet.com/issue-log-instructions/)." rosemet.com (accessed 2026-09-23). A published field list carrying no risk-origin, confirmer, or last-updated field, and treating lessons learned as a use of the log rather than a field in it ("lessons-learned database"). [practitioner]

<a id="ref-35"></a>[35] Plane. "[What is an issue log? How to maintain one in project management](https://plane.so/blog/what-is-an-issue-log-how-to-maintain-one-in-project-management)." plane.so (accessed 2026-09-23). A second published field list with free-text resolution notes and no confirmer or last-updated field ("A brief record of what was done to fix the issue"). [vendor]

<a id="ref-36"></a>[36] Mastt. "[Issue Log (Word, Excel)](https://www.mastt.com/resources/issue-log)." mastt.com (accessed 2026-09-23). A published field list that assesses impact against named cost, schedule, and quality dimensions rather than a single scale, plus a category field ("A summary of how the issue affects time, cost, or project quality"; "Classification such as design, contract, safety, scheduling, or quality"). [vendor]

<a id="ref-37"></a>[37] Smartsheet. "[Free Issue Tracking Templates](https://www.smartsheet.com/content/issue-tracking-templates)." smartsheet.com (accessed 2026-09-23). A published template carrying a last-updated date distinct from open and close dates ("fields to enter the project name, manager, application or site, and the last updated date"). [vendor]

<a id="ref-38"></a>[38] Jason Westland. "[What Is an Issue Log? Templates, Tips and More](https://www.projectmanager.com/blog/what-is-an-issue-log)." ProjectManager.com, 10 April 2025 (accessed 2026-09-23). The failure of an issue logged with no owner ("If the issue doesn't have an owner, it's likely never to get resolved."). [vendor]
