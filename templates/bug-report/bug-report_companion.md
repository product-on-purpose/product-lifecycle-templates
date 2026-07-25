# Companion: The Bug Report

> The deep explainer for the bug-report bundle. Read this to understand what a bug report is, where it came
> from, why it is shaped the way it is, and where practitioners disagree about it. This is the only document
> in the qa-docs family routinely written by people who are not testers, which is most of what makes it hard.
> The short operator card is [`bug-report_guide.md`](bug-report_guide.md); a fully worked instance is
> [`bug-report_example.md`](bug-report_example.md). Inline citations like [[1]](#ref-1) resolve to the
> [References](#references) at the bottom, tagged by source reliability.

---

## 1. Orientation

A bug report is **the document that gets one defect fixed by someone who was not there when it happened.**
ISTQB calls it a defect report and defines it as *"A document reporting on any flaw in a component or system
that can cause the component or system to fail to perform its required function."* [[5]](#ref-5) The best
one-line statement of its purpose is older and better: *"the aim of a bug report is to enable the programmer
to see the program failing in front of them."* [[18]](#ref-18)

**At a glance**
- It carries **what you did**, in enough detail that someone else can do it too [[11]](#ref-11).
- It states **what you expected** as well as what happened - the single most-omitted element in real reports
  [[13]](#ref-13).
- It records **where** (build, environment, configuration) and **how reliably** it happens [[9]](#ref-9).
- It separates **severity** (how much damage) from **priority** (how soon), which are independent enough that
  each crossing case occurs in practice [[23]](#ref-23).
- It describes **the system's behavior, not a person's mistake** [[36]](#ref-36).

If you read nothing else: you are not writing an accusation or a diagnosis. You are writing a reproduction
recipe with enough context that someone can decide what to do about it.

**The honest first thing to know, and it changes how the whole document should be written:** the standards
deliberately do not call this a bug report. IEEE 829-2008 named it an **anomaly report**, and the reason is
stated plainly: *"a discrepancy between expected and actual results can occur for a number of reasons other
than a fault in the system."* [[2]](#ref-2) Its successor calls it an **incident report** [[3]](#ref-3),
and ISTQB defines an incident as *"Any event occurring that requires investigation."* [[5]](#ref-5)

At the moment you write this document, **you do not yet know whether there is a defect.** It might be a
misconfiguration, a stale cache, a misunderstanding of the intended behavior, or a genuine flaw. Writing as
though you know is what produces the defensive reply and the "works as designed" close. Report the anomaly;
let the investigation decide what it was.

**The second thing to know is a measured one.** The landmark study of 466 respondents across Apache, Eclipse
and Mozilla found that what developers most want from a report is what reporters find hardest to give:
*"Most developers consider steps to reproduce, stack traces, and test cases as helpful, which are at the same
time most difficult to provide for users."* [[12]](#ref-12)[[11]](#ref-11) That mismatch, not laziness, is why
most reports are thin. A template's job is to lower the cost of supplying the expensive parts.

## 2. Origins and evolution

**IEEE 829** carried this document from the beginning, and is now superseded: *"IEEE 829-2008 is superseded by
ISO/IEC/IEEE 29119-1-2013, ISO/IEC/IEEE 29119-2-2013, ISO/IEC/IEEE 29119-3-2013 and ISO/IEC/IEEE
29119-4-2015."* [[1]](#ref-1) Secondary summaries of the 1998 edition describe a test incident report of a
handful of sections - identifier, summary, description, impact [[8]](#ref-8) - though that list is sparse
next to what practitioners actually use and the standard itself was not read.

**The rename is the interesting part.** The 2008 edition relabeled the test incident report as an *anomaly
report*, for the reason quoted in section 1 [[2]](#ref-2). The successor series keeps the same instinct,
listing the artifact among its document types as a *Test Incident Report* [[3]](#ref-3). One practitioner
analysis of the 2021 edition notes the practical cost of that vocabulary: *"the term 'incident report' hides
the commonly known 'bug report' is introduced late in the descriptive chapters."* [[4]](#ref-4) The standards
are right about the concept and unhelpful about the name.

**ISTQB supplies the vocabulary most teams half-remember**, and it is worth getting right because the four
terms are not interchangeable [[5]](#ref-5):

- an **error** is *"A human action that produces an incorrect result."*;
- a **defect** (ISTQB treats **bug** as its synonym) is *"A flaw in a component or system that can cause the
  component or system to fail to perform its required function, e.g., an incorrect statement or data
  definition."*;
- a **failure** is *"Deviation of the component or system from its expected delivery, service or result."*;
- an **incident** is *"Any event occurring that requires investigation."*

The chain runs error to defect to failure: a person makes a mistake, which puts a flaw in the artifact, which
produces an observable failure when the artifact runs [[6]](#ref-6). **Root cause is a fourth thing**, not a
synonym for error [[6]](#ref-6).

**Two breaks in that chain matter for a template.** Not every defect produces a failure: *"Not all Defects
result in Failures; some remain inactive in the code, and we may never notice them."* [[7]](#ref-7) And not
every failure comes from a code defect; environment, data and hardware produce failures too, which is exactly
why the standard prefers "anomaly". So the symmetrical-sounding claim that every failure implies a defect is
false, and a template that assumes otherwise pushes reporters into naming a culprit they have no way of
identifying yet.

**One more standards fact, and it explains a lot of the disorder downstream.** IEEE 1044, the classification
standard for software anomalies that everyone cites for defect taxonomy, **was inactivated on 2020-03-05 after
a decade without revision, and nothing replaced it** [[38]](#ref-38). Every defect-lifecycle state list you
have seen - new, triaged, assigned, fixed, verified, reopened, won't fix, cannot reproduce - is therefore
convention. Useful convention, but not a standard, and no tool is wrong for naming its states differently.

## 3. Anatomy (section by section)

The full variant carries eight sections; the lean variant carries the first four, unchanged in name and order.

### Summary

One line that lets a reader in a triage queue decide whether to open this.

Write the observable failure and its context, not a diagnosis: "Shared view returns EMEA rows to a viewer
without EMEA entitlement" rather than "permissions broken". A good summary contains the *what* and the
*where*; the ID is assigned by whatever tracks it [[10]](#ref-10). If the report also needs a one-line
statement of who is affected and how badly, put it here rather than making a reader hunt.

### Steps to Reproduce

The numbered path from a known starting state to the failure.

This is the deliverable. The empirical work treats steps to reproduce as the primary quality lever for reports
overall [[14]](#ref-14), and it is the element developers rank at the top of what helps [[12]](#ref-12).
Tatham's instruction remains the clearest: get the reader to the point where they can see it fail themselves
[[18]](#ref-18).

Three things make steps usable. **Start from a known state**, because "open the app" hides the account,
the data and the configuration that actually matter. **Number them**, so a reply can say "step 4 works for
me". And **cut everything that is not needed to trigger it**: a minimal path is faster to run and narrows the
cause by itself.

If you genuinely cannot reproduce it, say so here rather than inventing a path. Non-reproducible reports are
a large, studied category rather than an embarrassment [[15]](#ref-15)[[16]](#ref-16), and the honest version
is far more useful than a fabricated one.

### Expected and Actual Behavior

What you expected to happen, and what happened instead.

**This is the section this bundle exists to enforce.** Across roughly 3,000 real reports, observed behavior
appeared in 93.5 percent, steps to reproduce in 51.4 percent, and **expected behavior in just 35.2 percent**
[[13]](#ref-13). Two reports in three do not say what should have happened.

That omission feels reasonable to the reporter, who thinks it is obvious, and it is expensive for the reader,
who often genuinely does not know: *"Developers might not know how the application works from end to end...
Including the expected outcome -- in addition to the actual outcome -- provides crucial information."*
[[9]](#ref-9) Tatham said the same thing before anyone measured it: *"Tell them exactly what you saw. Tell
them why you think what you saw is wrong; better still, tell them exactly what you expected to see."*
[[18]](#ref-18)

Say where the expectation comes from if you can - an acceptance criterion, documentation, the behavior of the
previous release, or your own reasonable assumption. "I expected X because the docs say X" and "I expected X
because it seemed sensible" are both legitimate, and they lead to different conversations.

### Environment and Reproducibility

Build, environment, configuration, account and how reliably it happens.

Environment detail is the defense against the "works for me" close, and reproducibility is a field rather
than an adjective: *"Knowing how frequently a bug reproduces is important. Many bugs are random."*
[[9]](#ref-9) State it concretely - always, roughly one time in five, only on first load after a cold start.

Non-reproducibility is a real operational problem, studied at scale [[15]](#ref-15), and one large study of
576 such reports found many distinct contributing factors and, usefully, that *"links to existing bug reports
might help improve the reproducibility of a reported bug"* [[16]](#ref-16). If you have seen something like
this before, link it.

**On duplicate-checking**, which every reporting guide demands: search first, but calibrate. Measured
duplicate rates across more than 150,000 reports run from roughly 2 percent on infrastructure projects to
about 28 percent on widely used consumer tools [[19]](#ref-19). The widely quoted "30 percent" sits **above**
the measured ceiling of that range rather than at it, and how hard you should hunt depends on which kind of
project you are on.

### Evidence (full variant only)

Screenshots, recordings, logs, stack traces, network captures, and the identifiers that let someone find them.

Evidence supports the steps rather than replacing them; it becomes decisive when the failure is intermittent
and the steps alone will not reproduce it [[16]](#ref-16). Stack traces in particular are among the artifacts
developers most want [[12]](#ref-12). Attach the smallest thing that shows the failure, and say what to look
at in it, because a reader should not have to hunt through a twenty-minute recording.

### Impact, Severity and Priority (full variant only)

How much damage this does, how soon it should be fixed, and who decided.

These are two independent axes, and treating them as one is the classification error the two crossing cases
below exist to prevent. ISTQB defines **severity** as *"The degree of impact that a defect has on the development or operation of a
component or system."* [[20]](#ref-20) and **priority** as *"The level of (business) importance assigned to an
item, e.g., defect."* [[21]](#ref-21)

The two crossing cases are the proof they are independent, and both are standard examples: a crash in a rarely
used legacy path is **high severity, low priority**; a cosmetic error on a high-traffic page during a launch
is **low severity, high priority** [[23]](#ref-23).

**Two honest qualifiers, both of which templates usually skip.**

First, **ISTQB defines both terms and assigns ownership to neither** [[20]](#ref-20)[[21]](#ref-21). The
familiar rule - QA sets severity, the product manager sets priority - is a widely followed convention
[[22]](#ref-22)[[23]](#ref-23), and current sources increasingly add engineering leads to the priority side
[[27]](#ref-27). Follow it, but do not call it a standard.

Second, **there is no standard severity scale.** Four-level named scales are common, five-level scales add
Blocker at the top [[26]](#ref-26), and six-level variants exist. Numeric S1-S4 labeling is tooling convention
whose meaning varies between sources [[22]](#ref-22). Pick one scale, define each level in words, and put the
definition where reporters can see it.

### Triage and Ownership (full variant only)

What triage decided, who owns it now, and against which release.

Triage is where a report stops being a claim and becomes work: the meeting reviews new defects, validates or
corrects severity and priority, and *"sets the priority based on all the inputs and assigns the defect to the
correct release."* [[24]](#ref-24) Recording the outcome in the report is what stops the same argument
happening twice.

This section is also where the report meets the test plan. Severity thresholds are the usual form of a release
gate: *"No open critical bugs: All critical bugs that impact core functionality must be resolved to meet exit
criteria."* [[25]](#ref-25) A report's severity is therefore not a label, it is an input to whether the
release happens.

### Resolution and Regression Guard (full variant only)

What was actually wrong, what changed, and what now stops it coming back.

Root cause belongs here rather than in the reporter's sections, because it is the output of the
investigation, not an input to it. The most valuable line in this section is usually the last one: **the test
case that now guards this defect.** A closed bug with no regression guard is an invitation to fix the same
thing twice.

One tool-level convention worth adopting whatever you use: *"Don't reopen closed bugs for regressions.
Instead, open a new bug and link it to the original with a Related link."* [[39]](#ref-39) A reopened ticket
loses the history of what was fixed the first time.

## 4. Variants and sizing

**Lean (four sections)** is the default, and here the default matters more than usual, because **this is the
one artifact in the family written by people who are not testers.** Support agents, salespeople, users and
developers-in-a-hurry all file bug reports, and every field beyond the necessary four is a reason to abandon
the form. Lean carries Summary, Steps to Reproduce, Expected and Actual Behavior, and Environment and
Reproducibility - which is close to the field set practitioner guidance converges on for the reporter's half
of the job [[9]](#ref-9).

**Full (eight sections)** adds Evidence, Impact/Severity/Priority, Triage and Ownership, and Resolution and
Regression Guard. Notice what those four have in common: **three of them are filled in by someone other than
the reporter, and after the report is filed.** That is the real reason for the split. The lean variant is the
intake form; the full variant is what the record becomes as it moves through triage and resolution.

Use full when the defect is being tracked formally: regulated or audited work, a release gate that depends on
severity, cross-team ownership, or any context where the closed record is evidence rather than a note.

**A warning about the count.** Whatever variant you use, do not let anyone count these. Defect counts get
gamed in documented ways the moment they become targets - splitting one bug into several tickets, filing
trivial bugs to hit quotas, relabeling to stay under a severity cap [[35]](#ref-35).

## 5. Methodology lineage

**The tracking tradition.** The canonical argument for writing this document down at all is Spolsky's: *"If
you are developing code, even on a team of one, without an organized database listing all known bugs in the
code, you are going to ship low quality code."*, and the reason is planning as much as quality, since *"if you
have a schedule with a lot of bugs remaining to be fixed, the schedule is unreliable."* [[28]](#ref-28)

**The zero-defects tradition**, in its software form, is documented from a 1989 Microsoft memo and was a
response to a specific incentive failure rather than an aspiration: developers were rewarded for checking in
features, so *"The cycle of trying to complete a feature by finding bugs could never really end - this was
called infinite bugs."* [[29]](#ref-29) (Crosby's 1964 manufacturing Zero Defects programme is a different
thing with a similar name; this bundle does not treat them as one lineage.)

**The agile tradition** pushes the other way, toward not accumulating reports at all. Fowler documents that
teams seriously practising XP reach very low defect rates, with the crucial qualifier that *"you should not
assume you are going to get super-low bug rates by just adopting XP"* [[30]](#ref-30). Lacey goes further and
argues the artifact itself is the problem: *"Don't put bugs on the product backlog. Just fix them or mark them
as won't fix."* [[31]](#ref-31)

**Where that leaves a template.** All three traditions agree on what a good report contains when you write
one. They disagree about when you should. Section 6 has the argument.

## 6. Debates and contested boundaries

### Should you log it, or just fix it?

**The case for not logging.** A tracked report is overhead: writing it, triaging it, and carrying it in a
queue costs more than the fix when the fix is fifteen minutes away. Lacey's stronger version is that the
backlog is itself the problem, because *"Having the ability to file a bug and have it on the product backlog
means there is a way to deprioritize quality by moving bugs farther down the product backlog."*
[[31]](#ref-31)

**The case for logging.** Spolsky's argument is that memory is not a database and a schedule with unknown
defects in it is fiction [[28]](#ref-28).

**The usable answer is structural rather than philosophical.** The break point is whether the fix will outlive
the working memory of the person who found it. Same person, same day, same sprint, no external reporter: fix
it. Anything crossing a boundary - a team, a sprint, a release, or a user who told you - needs a record,
because the alternative is that the knowledge exists in one head. Note also Fowler's caveat: very low defect
rates come from discipline, not from adopting a policy [[30]](#ref-30).

### Zero-bug policies

A zero-bug policy means the queue of known open defects is kept at zero by **fixing or explicitly rejecting**
each one. It does not mean the software has no defects, and conflating those two is the usual reason the
policy is dismissed as fantasy.

What makes it operable is a decision rule at intake. The sharpest one available: *"If you can live with it,
it's not a bug, it's an improvement."* [[33]](#ref-33) Everything then goes to the fix queue or the
improvement queue, and nothing accumulates in between.

The honest counter is that the rule relocates the argument rather than settling it: *"if product managers and
developers don't agree on what to call a bug, you probably need to address other problems"* [[32]](#ref-32).
And the outcome claims for these policies come from single organizations reporting on themselves; this bundle
does not repeat their numbers.

### Bankruptcy: mass-closing an old backlog

The argument for is that aged reports are cognitive overhead with little value, and that anything important
returns: *"If an idea has high enough value for customers, it will come back. It will bubble up to the top."*
[[34]](#ref-34)

The argument against is a conditional the advocates tend not to stress. **That claim is only true if intake
still works.** If the only channel by which a problem reaches you is the backlog you just deleted, nothing
bubbles up; you have destroyed a record and learned nothing. Close the backlog if you like, but fix intake
first.

### Bug, defect, issue, incident: does the word matter?

Practitioners genuinely disagree, and not subtly. In one community thread, one respondent defines a bug as
*"A bug is a defect of undetermined cause"*, while another treats issue as the superset: *"An issue is a very
broad term that encompasses bugs and defects, but also things such as new feature requests"* [[37]](#ref-37).
The standards add a fourth vocabulary in which the artifact is an anomaly or an incident [[2]](#ref-2), and
tools add a fifth [[40]](#ref-40).

**Nothing is going to resolve this.** The practical move is the one this template takes: pick a term, define
it where readers will see it, and note that other teams mean different things by the same word.

### Defect versus enhancement

The cleanest available test: a defect means the software does not work the way it says it will; an
enhancement means it does not work the way someone wants [[42]](#ref-42). If there is a violated
specification, documented behavior or reasonable expectation, it is a defect. If the request is for behavior
nobody ever promised, it is a change request.

The boundary genuinely blurs - an undocumented performance regression is the classic case - and the zero-bug
literature's classification rule [[33]](#ref-33) is a pragmatic tiebreaker when the specification is silent.

### Does tone matter?

The craft guidance is firm: *"The most important point that a tester should keep in mind is not to use an
authoritative tone in the report. This breaks morale and creates an unhealthy work relationship. Use a
suggestive tone."* [[36]](#ref-36) Describe the system's behavior rather than a person's competence.

**Stated honestly: no study is being cited here.** This is practitioner craft wisdom, and this bundle presents
it as such rather than dressing it as a finding. The mechanism it proposes is plausible and the cost of
following it is zero.

### A note on what was not read

A 2020 replication of the landmark study exists [[17]](#ref-17), and a reader may reasonably
expect it here. **It was not retrieved**: the page is paywalled, and the author list could not be confirmed
from any page actually read, with one automated summary giving a set of authors that appears to be wrong.
Rather than cite a paper this project could not open, the entry is listed and explicitly carries no claim.

## 7. Anti-patterns and failure modes

**No expected behavior.** The most common real defect in real reports [[13]](#ref-13). The reader is left
guessing whether the behavior is wrong or you are.

**A diagnosis instead of an observation.** "The cache is broken" when what you saw was a stale number. You may
be right, and if you are wrong you have sent the reader down your wrong path. Report what you saw; put the
hypothesis in its own line, labeled.

**Steps that start in the middle.** "Go to the report and click export" omits which account, which data,
which configuration. The result is a "works for me" close and two more round trips.

**The everything-report.** Three unrelated problems in one ticket, so it cannot be closed, cannot be assigned,
and cannot be prioritized. One report, one defect.

**Blaming the developer.** Costs you the collaborative fix and gets you a defensive one [[36]](#ref-36).

**Severity as a negotiating position.** Inflating severity to get attention corrupts the only signal the
release gate reads [[25]](#ref-25), and once counts or caps are watched, this becomes systematic
[[35]](#ref-35).

**Reopening a closed bug for a regression.** Loses the record of the original fix; open a new one and link
[[39]](#ref-39).

**Duplicate panic, or duplicate indifference.** Both are calibration failures: duplicate rates differ by an
order of magnitude between project types [[19]](#ref-19).

**Closing "cannot reproduce" as though it settled something.** It is a large, studied category with many
causes [[15]](#ref-15), and linking related reports is a documented way to make progress on it
[[16]](#ref-16).

## 8. Relationships to other artifacts

**Bug report and test case.** Opposite directions in time. A test case is written before, to define correct
behavior; a bug report is written after, because something was not. They share fields - steps, expected,
actual - which is exactly why beginners conflate them. The useful asymmetry: **a failing test case often
produces a bug report, and a closed bug report should produce a test case**, which is the regression guard in
section 3.

**Bug report and test plan.** The plan sets the severity thresholds and the suspension rules that decide what
happens when a report arrives [[25]](#ref-25). A report's severity is an input to a gate the plan defined.

**Bug report and incident.** Different objectives, not different severities of the same thing: *"incident
management focuses on restoring service as quickly as possible after an incident occurs, while bug management
focuses on identifying and fixing the root cause"* [[41]](#ref-41). A production incident may generate a bug
report; the incident is closed when service is restored, and the bug is closed when the flaw is gone. (Note
the vocabulary collision: ISTQB's "incident" means any event requiring investigation [[5]](#ref-5), which is
not what an on-call engineer means by it.)

**Bug report and incident postmortem.** A postmortem covers a significant service event: timeline,
contributing factors, impact, and action items. A bug report covers one flaw. A report is often an input to a
postmortem and is never a substitute for one. In this library the postmortem lives in a different family and
at a different phase, which is the taxonomy's way of saying the same thing.

**Bug report and change request.** Covered in section 6 [[42]](#ref-42).

**Bug report and acceptance criteria.** This is the boundary the qa-docs family exists to resolve, and it
matters here in a way that surprises people. An acceptance criterion is agreed with the business **before**
the work and states what must be true for a story to be done; a bug report is written **after** the fact and
states what was observed. So they are not two views of one thing, and in particular: **a defect does not have
to violate an acceptance criterion to be a defect.**

That expectation - that every bug should trace back to a criterion it broke - is the specific confusion worth
naming. It is wrong for the reason the test-case bundle sets out at length: test design continues past the
agreed criteria into negative paths, boundaries, regression and non-functional territory nobody signed off,
and a defect found there is still a defect. The worked example is exactly that case, and says so in its own
Expected and Actual Behavior section.

Where a criterion **is** violated, cite it: it makes the expected behavior unarguable, which is the single
most valuable thing you can do for a report [[13]](#ref-13). Where none applies, say where the expectation
does come from instead - the design, the previous release, or a reasonable assumption - rather than leaving
the field empty because no criterion fits.

**Bug report and the tool.** This is where the discipline meets the world, and the news is bad. Trackers
require almost nothing: in Azure Boards, *"By default, only the Title field is required."* [[39]](#ref-39)
Worse for the severity teaching, **Jira had a Severity field and deliberately removed it**, on the reasoning
that *"JIRA succeeds so well because business users can actually use it."* [[40]](#ref-40) Jira therefore
cannot express, out of the box, the severity-versus-priority
distinction that section 3 argues is essential; teams that want it add a custom field.

Take that as a fact to design around, not a reason to give up the distinction. If your tracker has one
priority field, decide as a team whether it means damage or urgency, write that down, and stop having the
argument.

**Within the qa-docs family.** The plan says what will be verified and how deeply; the test case specifies one
verification; this document records one that failed. It is also the family's only outward-facing member, which
is why its lean variant is the leanest in the family.

## 9. Adaptations

**Externally reported bugs** (from users, support or customers) need the lean variant and nothing else. Every
field you add to a public form costs you reports, and the elements you most want are already the expensive
ones [[12]](#ref-12).

**Regulated and audited work** needs the full variant, with triage decisions and resolution recorded, because
the closed report is evidence.

**Teams with a release gate** should make the severity scale visible at report time, since the gate reads it
[[25]](#ref-25).

**Teams running a zero-bug policy** should add the intake decision explicitly to the triage section: fix,
reject, or reclassify as an improvement [[33]](#ref-33).

**Teams declaring backlog bankruptcy** should fix intake before closing anything, for the reason in section 6
[[34]](#ref-34).

**Teams on a tracker with no severity field** should say in the template header which of damage and urgency
their single priority field means [[40]](#ref-40).

## 10. Worked example

[`bug-report_example.md`](bug-report_example.md) is a full-variant report for the "Saved Views for Dashboards"
feature at the fictional Acme Analytics, closing the chain this family started: it is **the defect found by
the test case** in [`test-case_example.md`](../test-case/test-case_example.md), which was itself designed from
the highest-tier risk in [`test-plan_example.md`](../test-plan/test-plan_example.md).

Three things in it are worth studying. Its **expected behavior** is stated and sourced, which two reports in
three never do [[13]](#ref-13). Its **severity and priority disagree on purpose**, demonstrating the
independence section 3 argues for. And its **resolution names the regression guard**, so the chain closes
where it began: a risk produced a case, the case produced a report, and the report produced a test that stops
the defect returning.

---

## References

<a id="ref-1"></a>[1] IEEE Standards Association. "[IEEE 829-2008: IEEE Standard for Software and System Test Documentation](https://standards.ieee.org/ieee/829/3787/)." IEEE SA (accessed 2026-07-25). Supports the supersession of IEEE 829-2008 and the successors that replaced it ("IEEE 829-2008 is superseded by ISO/IEC/IEEE 29119-1-2013, ISO/IEC/IEEE 29119-2-2013, ISO/IEC/IEEE 29119-3-2013 and ISO/IEC/IEEE 29119-4-2015."). Status page only; the standard text is paywalled and was not read. [primary]

<a id="ref-2"></a>[2] Wikipedia contributors. "[Software test documentation](https://en.wikipedia.org/wiki/Software_test_documentation)." Wikipedia (accessed 2026-07-25). Supports the renaming of the test incident report to an anomaly report in IEEE 829-2008 and the reason given for it ("a discrepancy between expected and actual results can occur for a number of reasons other than a fault in the system."). A summary of a paywalled standard; the standard text was not independently read. [reference]

<a id="ref-3"></a>[3] Wikipedia contributors. "[ISO/IEC 29119](https://en.wikipedia.org/wiki/ISO/IEC_29119)." Wikipedia (accessed 2026-07-25). Supports that the successor standard's Part 3 document set includes a "Test Incident Report". A synthesis of a paywalled standard. [reference]

<a id="ref-4"></a>[4] microTOOL GmbH. "[Test Documentation with ISO/IEC/IEEE 29119-3:2021](https://www.microtool.de/en/document-management/test-documentation-with-iso-iec-ieee-29119-32021/)." microTOOL (accessed 2026-07-25). Supports the practical cost of the standard's vocabulary ("the term 'incident report' hides the commonly known 'bug report' is introduced late in the descriptive chapters."; "Since 2013, IEEE 829 has been replaced by ISO/IEC/IEEE 29119-3."). Vendor content whose author states they read the paywalled standard, which this project could not verify. [vendor]

<a id="ref-5"></a>[5] ISTQB. "[Glossary](https://istqb-glossary.page/)." ISTQB Glossary, community mirror (accessed 2026-07-25). Supports the definitions of defect, bug, error, failure, incident and defect report, including that bug and defect share a definition while error does not, and that incident is far broader ("A flaw in a component or system that can cause the component or system to fail to perform its required function, e.g., an incorrect statement or data definition."; "A human action that produces an incorrect result."; "Deviation of the component or system from its expected delivery, service or result."; "Any event occurring that requires investigation."; "A document reporting on any flaw in a component or system that can cause the component or system to fail to perform its required function."). **A community mirror, not the official glossary**; the page carries a no-affiliation disclaimer and shows no version number. [reference]

<a id="ref-6"></a>[6] istqb.guru. "[Defect vs Failure vs Error vs Mistake](https://www.istqb.guru/defect-vs-failure-vs-error-vs-mistake-istqb/)." istqb.guru (accessed 2026-07-25). Supports the causal chain in its teaching form and the separateness of root cause as a fourth concept ("A person makes a mistake (error). This produces a defect (fault) in the work product. Executing the work product produces a failure."). No byline; a practitioner summary of a syllabus whose PDF was not readable. [practitioner]

<a id="ref-7"></a>[7] ToolsQA. "[Error, Defect and Failure](https://www.toolsqa.com/software-testing/istqb/error-defect-failure/)." ToolsQA (accessed 2026-07-25). Supports the break in the chain where a defect never produces a failure ("Not all Defects result in Failures; some remain inactive in the code, and we may never notice them."). No date visible; the page attributes a quotation to a named individual that could not be verified, and that attribution is not used here. [practitioner]

<a id="ref-8"></a>[8] ProfessionalQA. "[IEEE 829-1998 standard overview](https://www.professionalqa.com/ieee-standard-829-1998)." ProfessionalQA (accessed 2026-07-25). Supports the sparse section list attributed to the 1998 edition's test incident report. A secondary summary of a paywalled edition which may understate the standard; no field-level claim in this bundle rests on it. [practitioner]

<a id="ref-9"></a>[9] TechTarget. "[What details to include on a software defect report](https://www.techtarget.com/searchsoftwarequality/tip/What-details-to-include-on-a-software-defect-report)." SearchSoftwareQuality (accessed 2026-07-25). Supports the argument for stating expected as well as actual behavior, and for recording reproduction frequency ("Developers might not know how the application works from end to end...Including the expected outcome -- in addition to the actual outcome -- provides crucial information."; "Knowing how frequently a bug reproduces is important. Many bugs are random."). No publication date visible. [practitioner]

<a id="ref-10"></a>[10] BrowserStack. "[How to write a good defect report](https://www.browserstack.com/guide/how-to-write-a-good-defect-report)." BrowserStack (accessed 2026-07-25). Supports a representative vendor field list, including the identifier convention ("Unique identifier for tracking (e.g., DEF-0012)"). Vendor content with no named author or date. [vendor]

<a id="ref-11"></a>[11] Nicolas Bettenburg, Sascha Just, Adrian Schroeter, Cathrin Weiss, Rahul Premraj and Thomas Zimmermann. "[What makes a good bug report?](https://research.vu.nl/en/publications/what-makes-a-good-bug-report/)" ACM SIGSOFT FSE 2008 (accessed 2026-07-25). Supports the existence, authorship, venue and scope of the landmark study: 466 respondents across Apache, Eclipse and Mozilla. **The publication record was read; the paper body was not**, so the study's finding is quoted through [[12]](#ref-12). The study covers open-source projects on Bugzilla-style trackers. [primary]

<a id="ref-12"></a>[12] Jorge Aranda. "[What Makes a Good Bug Report?](https://neverworkintheory.org/2011/08/30/what-makes-a-good-bug-report.html)" It Will Never Work in Theory (published 2011-08-30; accessed 2026-07-25). Supports the study's central mismatch finding in quotable form ("Most developers consider steps to reproduce, stack traces, and test cases as helpful, which are at the same time most difficult to provide for users."). A secondary summary, cited as such, with [[11]](#ref-11) carrying the bibliographic weight. [practitioner]

<a id="ref-13"></a>[13] Oscar Chaparro, Jing Lu, Fiorella Zampetti, Laura Moreno, Massimiliano Di Penta, Andrian Marcus, Gabriele Bavota and Vincent Ng. "[Detecting Missing Information in Bug Descriptions](https://ojcchar.github.io/publications/8-fse17)." ESEC/FSE 2017 (accessed 2026-07-25). Supports the measurement this bundle leans on hardest: across approximately 3,000 reports, observed behavior appears in 93.5 percent, steps to reproduce in 51.4 percent, and expected behavior in only 35.2 percent. The corpus is open-source bug trackers. [primary]

<a id="ref-14"></a>[14] Oscar Chaparro, Carlos Bernal-Cardenas, Jing Lu, Kevin Moran, Andrian Marcus, Massimiliano Di Penta, Denys Poshyvanyk and Vincent Ng. "[Assessing the Quality of the Steps to Reproduce in Bug Reports](https://arxiv.org/abs/1906.07107)." ESEC/FSE 2019 (accessed 2026-07-25). Supports that steps to reproduce are treated as the primary quality lever for bug reports ("identify and assess the quality of the steps to reproduce in a bug report, providing feedback to the reporters"). [primary]

<a id="ref-15"></a>[15] Mona Erfani Joorabchi, Mehdi Mirzaaghaei and Ali Mesbah. "[Works For Me! Characterizing Non-reproducible Bug Reports](https://dl.acm.org/doi/10.1145/2597073.2597098)." MSR 2014 (accessed 2026-07-25). Supports the existence and scale of the non-reproducibility problem as a studied category. **The ACM page returned 403 and the paper was not read**; the scale is attributed through the authors' own publication listing and [[16]](#ref-16), and no quotation is taken from it. [primary]

<a id="ref-16"></a>[16] Mohammad Masudur Rahman, Marco Castelluccio and Foutse Khomh. "[Works for Me! Cannot Reproduce: A Large Scale Empirical Study of Non-reproducible Bugs](https://www.mozillafoundation.org/en/research/library/works-for-me-cannot-reproducea-large-scale-empirical-study-of-non-reproducible-bugs/)." Empirical Software Engineering, 2022 (accessed 2026-07-25). Supports the study of 576 non-reproducible reports from Firefox and Eclipse, the many factors behind non-reproducibility, and the value of linking related reports ("11 key factors that might lead a reported bug to non-reproducibility"; "links to existing bug reports might help improve the reproducibility of a reported bug"). [primary]

<a id="ref-17"></a>[17] Mozhan Soltani, Felienne Hermans and Thomas Back. "[The significance of bug report elements](https://link.springer.com/article/10.1007/s10664-020-09882-z)." Empirical Software Engineering, 2020 (accessed 2026-07-25). Listed because it is the modern replication of [[11]](#ref-11) and a reader may expect it. **It was not retrieved: the page is paywalled and the author list could not be confirmed from any page read**, with one automated summary giving an apparently incorrect set of authors. **No claim in this bundle rests on this entry.** [primary]

<a id="ref-18"></a>[18] Simon Tatham. "[How to Report Bugs Effectively](https://www.chiark.greenend.org.uk/~sgtatham/bugs.html)." chiark.greenend.org.uk (accessed 2026-07-25). Supports the canonical statement of a bug report's purpose and the observed-versus-expected instruction ("the aim of a bug report is to enable the programmer to see the program failing in front of them."; "Tell them exactly what you saw. Tell them why you think what you saw is wrong; better still, tell them exactly what you expected to see."). No publication date visible; an argumentative essay rather than research. [practitioner]

<a id="ref-19"></a>[19] Avinash Patil, Siru Tao and Aryan Jadon. "[GitBugs](https://arxiv.org/html/2504.09651)." arXiv (accessed 2026-07-25). Supports measured duplicate rates across more than 150,000 reports in nine projects, running from roughly 2 percent on infrastructure projects to about 28 percent on widely used consumer tools ("over 150,000 bug reports"). An arXiv preprint, not confirmed peer-reviewed; the point taken is the spread rather than any single figure. [reference]

<a id="ref-20"></a>[20] ISTQB. "[Severity](https://istqb-glossary.page/severity/)." ISTQB Glossary, community mirror (accessed 2026-07-25). Supports the canonical definition of severity ("The degree of impact that a defect has on the development or operation of a component or system."). A mirror with no version number, and **the entry specifies no owner and no scale**. [reference]

<a id="ref-21"></a>[21] ISTQB. "[Priority](https://istqb-glossary.page/priority/)." ISTQB Glossary, community mirror (accessed 2026-07-25). Supports the canonical definition of priority and its business framing ("The level of (business) importance assigned to an item, e.g., defect."). Same mirror caveat; **neither entry says who assigns either value**. [reference]

<a id="ref-22"></a>[22] Software Testing Help. "[Defect severity and priority, with the defect triage process](https://www.softwaretestinghelp.com/how-to-set-defect-priority-and-severity-with-defect-triage-process/)." Software Testing Help (accessed 2026-07-25). Supports the S1-S4 numbering convention and the ownership convention ("the Product Manager or the triage team mainly assesses the priority parameter."). No date visible; its exit-criteria claim for the lowest priority level is that source's convention, not a standard. [practitioner]

<a id="ref-23"></a>[23] BrowserStack. "[Bug severity vs priority in testing](https://www.browserstack.com/guide/bug-severity-vs-priority)." BrowserStack (accessed 2026-07-25). Supports both crossing examples in worked form and the ownership convention ("Bug Severity is primarily determined by the development or testing team."; "Bug Priority, on the other hand, is usually decided by product managers, stakeholders, or the business team."). Vendor content, no date. [vendor]

<a id="ref-24"></a>[24] Software Testing Help. "[Defect triage process and meeting](https://www.softwaretestinghelp.com/defect-triage-process-meeting/)." Software Testing Help (accessed 2026-07-25). Supports what a triage meeting decides ("sets the priority based on all the inputs and assigns the defect to the correct release."). No date; its attendee list is presented as typical rather than required. [practitioner]

<a id="ref-25"></a>[25] TestRail. "[Exit criteria: advanced strategies for agile QA teams](https://www.testrail.com/blog/exit-criteria-strategies/)." TestRail (accessed 2026-07-25). Supports how severity connects to a release gate ("No open critical bugs: All critical bugs that impact core functionality must be resolved to meet exit criteria."). Vendor content describing convention, not a standard; thresholds vary. [vendor]

<a id="ref-26"></a>[26] QATestLab. "[Bug severity levels explained](https://blog.qatestlab.com/2015/03/10/software-bugs-severity-levels/)." QATestLab (published 2015-03-10; accessed 2026-07-25). Supports a five-level named severity scale with definitions, and that such scales cite no formal standard ("Completely prevents the use or testing of the system"). [practitioner]

<a id="ref-27"></a>[27] Plane. "[Bug severity vs priority in testing](https://plane.so/blog/bug-severity-vs-priority-in-testing-key-differences)." Plane (accessed 2026-07-25). Supports a current cross-functional statement of the ownership convention that adds engineering leads to the priority side ("Typically assigned by QA engineers or testing teams"; "Typically aligned by product managers, engineering leads, and delivery stakeholders"). Vendor blog, no date; the variation is itself the evidence that the convention is not codified. [vendor]

<a id="ref-28"></a>[28] Joel Spolsky. "[The Joel Test: 12 Steps to Better Code](https://www.joelonsoftware.com/2000/08/09/the-joel-test-12-steps-to-better-code/)." Joel on Software (published 2000-08-09; accessed 2026-07-25). Supports the canonical argument for tracking defects at all ("If you are developing code, even on a team of one, without an organized database listing all known bugs in the code, you are going to ship low quality code."; "if you have a schedule with a lot of bugs remaining to be fixed, the schedule is unreliable."). Contested by short-cycle teams; see [[31]](#ref-31). [primary]

<a id="ref-29"></a>[29] Steven Sinofsky. "[Hardcore Software: Zero Defects](https://hardcoresoftware.learningbyshipping.com/p/006-zero-defects)." Hardcore Software (accessed 2026-07-25). Supports the documented origin of the software zero-defects practice and the incentive failure behind it ("The cycle of trying to complete a feature by finding bugs could never really end - this was called infinite bugs."). A participant's memoir, credible as an insider account rather than independent research. Crosby's 1964 manufacturing programme of the same name is a separate lineage and is not conflated with it here. [practitioner]

<a id="ref-30"></a>[30] Martin Fowler. "[VeryLowDefectProject](https://www.martinfowler.com/bliki/VeryLowDefectProject.html)." martinfowler.com (accessed 2026-07-25). Supports that very low defect rates are achievable and the qualifier that they do not follow from adopting practices alone ("you should not assume you are going to get super-low bug rates by just adopting XP"). Describes observed outcomes, not a controlled study. [primary]

<a id="ref-31"></a>[31] Mitch Lacey. "[Managing bugs in Scrum and agile projects](https://www.mitchlacey.com/blog/managing-bugs-in-scrum-and-agile-projects/)." mitchlacey.com (accessed 2026-07-25). Supports the strongest case against tracking bugs on a backlog ("Don't put bugs on the product backlog. Just fix them or mark them as won't fix."; "Having the ability to file a bug and have it on the product backlog means there is a way to deprioritize quality by moving bugs farther down the product backlog."). A practitioner position, not a study. [practitioner]

<a id="ref-32"></a>[32] Peter Hilton. "[Implement a zero-bug policy](https://hilton.org.uk/blog/zero-bug-policy)." hilton.org.uk (accessed 2026-07-25). Supports the observation that the bug-versus-feature classification dispute is itself diagnostic ("if product managers and developers don't agree on what to call a bug, you probably need to address other problems"). No readable publication date. [practitioner]

<a id="ref-33"></a>[33] InfoQ, reporting Simone Colosimo. "[Zero bug policy](https://www.infoq.com/news/2021/11/zero-bug-policy)." InfoQ (accessed 2026-07-25). Supports the intake rule that makes a zero-bug policy decidable ("If you can live with it, it's not a bug, it's an improvement."). A single-organization case reported by an internal advocate; its outcome figures are self-reported and are not used here. [practitioner]

<a id="ref-34"></a>[34] Adrian Bryant. "[Backlog bankruptcy: when is it time to press delete?](https://www.productplan.com/backlog-bankruptcy/)" ProductPlan (accessed 2026-07-25). Supports the case for mass-closing an aged backlog and the assumption it depends on ("If an idea has high enough value for customers, it will come back. It will bubble up to the top."). Written by an advocate; the argument holds only if intake still works, which this companion states and the source does not. [vendor]

<a id="ref-35"></a>[35] Qase. "[Why per-tester QA KPIs backfire](https://www.qase.io/blog/why-qa-testing-kpis-backfire/)." Qase (accessed 2026-07-25). Supports the documented forms defect-count gaming takes ("When a measure becomes a target, it ceases to be a good measure"). Vendor content; the gaming examples are illustrative rather than measured. [vendor]

<a id="ref-36"></a>[36] Software Testing Help. "[How to write a good bug report](https://www.softwaretestinghelp.com/how-to-write-good-bug-report/)." Software Testing Help (accessed 2026-07-25). Supports the tone guidance ("The most important point that a tester should keep in mind is not to use an authoritative tone in the report. This breaks morale and creates an unhealthy work relationship. Use a suggestive tone."). No named author, and **no study is cited** linking tone to resolution outcomes; this companion presents it as craft wisdom and says so. [reference]

<a id="ref-37"></a>[37] Iris Classon and community respondents. "[Stupid Question 154: Bug, issue or defect?](https://www.irisclasson.com/2013/02/19/stupid-question-154-bug-issue-or-defect-what-is-the-correct-term/)" irisclasson.com (published 2013-02-19; accessed 2026-07-25). Supports that practitioners draw these lines in incompatible places ("A bug is a defect of undetermined cause"; "An issue is a very broad term that encompasses bugs and defects, but also things such as new feature requests"). Community Q&A; the absence of consensus is the durable finding. [practitioner]

<a id="ref-38"></a>[38] IEEE Standards Association. "[IEEE 1044-2009: Standard Classification for Software Anomalies](https://standards.ieee.org/ieee/1044/4607/)." IEEE SA (accessed 2026-07-25). Supports that the most-cited defect classification standard was inactivated on 2020-03-05 after a decade without revision, with no replacement published. This is why every defect lifecycle state list in circulation is convention rather than standard. [primary]

<a id="ref-39"></a>[39] Microsoft. "[Define, capture, triage, and manage bugs in Azure Boards](https://learn.microsoft.com/en-us/azure/devops/boards/backlogs/manage-bugs?view=azure-devops)." Azure DevOps documentation (accessed 2026-07-25). Supports what a major tracker requires and its guidance on regressions ("By default, only the Title field is required."; "Don't reopen closed bugs for regressions. Instead, open a new bug and link it to the original with a Related link."). [vendor]

<a id="ref-40"></a>[40] Atlassian. "[Why doesn't JIRA have a Severity field like Bugzilla?](https://confluence.atlassian.com/jira061/jira-administrators-faq/usage-faq/why-doesn-t-jira-have-a-severity-field-like-bugzilla)" Atlassian documentation (accessed 2026-07-25). Supports that Jira had a Severity field and deliberately removed it, leaving Priority to carry both meanings ("JIRA succeeds so well because business users can actually use it."). Documentation for an older Jira version; the architectural consequence persists. [vendor]

<a id="ref-41"></a>[41] incident.io. "[Incident vs bug](https://incident.io/blog/incident-vs-bug)." incident.io (accessed 2026-07-25). Supports the boundary between defect management and incident management in terms of what each optimizes for ("incident management focuses on restoring service as quickly as possible after an incident occurs, while bug management focuses on identifying and fixing the root cause"). Vendor content from an incident-management company. [vendor]

<a id="ref-42"></a>[42] Rod Hilton. "[Enhancement vs. Defect: More Than Pedantry](https://www.rodhilton.com/2012/03/29/enhancement-vs-defect-more-than-pedantry/)." rodhilton.com (accessed 2026-07-25). Supports the working test for the defect-versus-change-request boundary: a defect means the software does not work the way it says it will, an enhancement means it does not work the way someone wants. A practitioner argument; the boundary remains contested in gray areas such as an undocumented performance regression. [practitioner]
