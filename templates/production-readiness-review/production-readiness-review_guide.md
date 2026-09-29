# Guide: Production Readiness Review (operator card)

The short card. Why the document is shaped this way, and the argument behind every rule here, is in
[`production-readiness-review_companion.md`](production-readiness-review_companion.md). A fully worked
instance is
[`production-readiness-review_example.md`](production-readiness-review_example.md).

## When to use

- A service is about to change hands, for example because a development team is asking an SRE or platform
  function to take over standing production ownership, and you want that handoff to depend on a checklist
  someone can point at, not on which reviewer happens to be asking questions that day.
- More than one service, or more than one handoff, will consult this same instrument. It is a standing
  questionnaire, reused across services, not a document invented fresh for one occasion.
- You want the criteria a service must clear, and the evidence that would actually satisfy each one, settled
  before the handoff rather than argued case by case while responsibility is already changing hands.
- You are not sure yet who should hold the checklist, who decides when a finding blocks, or how often a
  passed review should be revisited. Reviewer and Authority and Review Cadence exist to answer exactly that.
- You need every not-applicable answer to carry a written reason, so a later reader cannot mistake a
  considered exclusion for an item nobody checked.

## When NOT to use

- **You are evaluating one specific launch, not a service's standing ability to be run.** That is a launch
  coordination checklist. The two share engineering-scoped roots, but this review asks whether a service can
  be run once responsibility changes hands, on a basis expected to outlast one release; the launch checklist
  asks whether one specific launch is ready to ship.
- **You want a standing quality bar every unit of work is judged against, not a readiness gate for one
  service's production handoff.** That is a definition of done, a per-increment bar the team judges itself
  against every sprint. A definition of done is necessary but not sufficient input to this review; it is not
  a substitute for it, and this review is not a substitute for it.
- **You are advising on a requested change to a system already in production, not on a service's overall
  readiness to be run.** That is what a change advisory board reviews; its unit is one requested change, not
  a service.
- **You need the procedure a responder actually executes once a known situation has already happened.** That
  is a runbook. This review checks that a runbook exists; it does not write one.
- **Your organization does hardware manufacturing, and you were pointed at "Production Readiness Review" from
  an aerospace or defense context.** NASA and the US Department of Defense publish a document under the
  identical name that determines whether a manufacturer is ready to produce hardware at scale, judged by
  production planning and supplier management. It shares nothing with this document but the name.
- **You need a per-release go-live review with a rollback trigger, a business-cost-of-delay estimate, and a
  post-implementation configuration check.** One federal agency runs a document it also calls a Production
  Readiness Review before every release, but that content belongs to the release moment; use
  `launch-coordination-checklist` and `runbook` for it instead.

## Pick a variant

**Lean (five sections)** is Scope and Trigger, Readiness Criteria, Not-Applicable Rule, Outcome and
Sign-off, and Review Trigger. It carries the load-bearing table, the two rules that keep it honest, the
recorded outcome, and the standing checklist's own staleness trigger. At its lightest this is still a
genuine review, the couple-hours version one practitioner reports having seen run, not an exemption from
one.

**Full (eight sections)** adds Reviewer and Authority, Review Cadence, and When This Does Not Apply. Move to
full when at least one of these is true:

- more than one plausible reviewer exists, so naming who conducts the review and who is authorized to say a
  finding blocks is worth its own section rather than left implied;
- the service is expected to be reviewed more than once, so a cadence commitment, one-time, event-driven,
  or continuous, is worth stating and justifying rather than left to whoever remembers next time;
- your review program covers enough services that treating all of them identically would itself be a
  failure mode, so a documented lighter path, with a stated minimum it still requires, is worth naming rather
  than left as an unspoken exception.

Every lean heading appears in full unchanged, in the same order. Growing from lean to full is additive; you
never reorder or rename a section you already filled in.

## Quality rubric (self-grade)

Score each 0, 1 or 2. Full below 11 out of 18 ships a review a service can pass while still carrying the
exact kind of gap this review exists to catch: a criterion nobody can verify, a finding with no owner, or a
checklist with no way to notice it has gone stale. Lean is scored on rows 1 to 6 only (see the scope
table below), and below 7 of 12 a lean review can still pass a service with the same gaps.

| # | Criterion | 0 | 1 | 2 |
|---|---|---|---|---|
| 1 | **Named scope and trigger** | No trigger stated, or the review reads as though it applies to every service the same way with no stated boundary | A trigger is named, but a reader cannot tell what this review deliberately does not cover | The trigger matches how this review actually starts here, and at least one thing the review does not cover is named, with where that gap is reviewed instead |
| 2 | **Evidence-backed criteria** | Rows carry a status word and nothing else, "done," "yes," with no way for a second person to check it | Some rows name evidence a second person could go check; others stop at a bare confirmation | Every row's evidence names something a second person could go check themselves, and every criterion has a named owner |
| 3 | **Honest not-applicable reasons** | An item is marked N/A with nothing beside it | Some N/A items carry a reason; others are bare marks | Every item marked Not Applicable carries a written reason a later reader could evaluate, not a bare checkmark |
| 4 | **Findings, owned and dated** | The findings table is blank, or a finding is listed with no owner and no date | Findings are listed, but some carry no owner, no date, or no stated severity | Every finding not fully met carries a named owner, a due date, and its severity, and an accepted condition is explicitly listed rather than implied |
| 5 | **No silent all-clear** | The outcome and findings table are simply left empty | The outcome is stated, but an empty findings table is left blank rather than addressed | Where no findings exist, the document says so explicitly rather than leaving the table blank, so a reader cannot mistake silence for an all-clear |
| 6 | **Owned review trigger** | Only a calendar cadence is named, or nothing at all | An event is named, but with no owner, or the next action is only "update the checklist" | A specific kind of event, an incident, a near miss, or a named worry that turned out real, is paired with a named owner whose first move is to check which existing criterion should have caught it |
| 7 | **Named blocking authority** *(full)* | No one is named as authorized to call a finding blocking, or a channel or distribution list stands in for a person | A reviewer or role is named, but no escalation path exists for when the reviewer and the reviewed team disagree | A specific role is named as authorized to call a finding blocking, and a named escalation path exists for a disagreement, scaled to the risk of what is being reviewed |
| 8 | **Cadence as a position** *(full)* | Cadence is unstated, or left as "we'll revisit if needed" | A cadence is named, but with no stated reason tied to how this service actually changes | One of one-time, event-driven, or continuous is named deliberately, with a reason tied to how this service changes, and a stale, unexamined one-time review is named as a gap rather than left silent |
| 9 | **Bounded lighter path** *(full)* | A category is granted a blanket exemption with nothing left to check | A lighter category is named, but what it still requires is vague or unstated | A specific service or change type is named for the lighter path, and what it still requires, not only what it skips, is stated plainly |

**Which rows apply to what.**

| Document | Rows | Maximum | Score against |
|---|---|---|---|
| full | all 9 | 18 | **11** |
| lean | 1-6 | 12 | **7** |

Rows 7, 8, and 9 are scored only against full. Lean ships neither Reviewer and Authority, Review Cadence,
nor When This Does Not Apply, so grading it on those three rows would penalize the choice of variant rather
than the quality of the document.

The test behind every cell above: **could someone satisfy it without improving the document?** A row that
counted criteria rows, named domains, or listed findings would reward padding. Every cell instead asks
whether a specific piece of evidence exists, and whether a second person, not the author, could check it
without asking who wrote the document.

## Named anti-patterns (the usual wrecks)

1. **Engagement that starts too late to change the design.** The model's own stated limitation is that the
   service is already launched and serving at scale by the time SRE engagement begins, so a reviewer's
   findings can only recommend changes a team must retrofit rather than build in from the start.
2. **No stated goal, so no priority.** A review run with no specific goal drops to the bottom of the
   development team's own priority list, and gets treated as paperwork rather than as a real check.
3. **A defensive reviewed team that hides risk.** A team that feels itself to be under review, rather than
   served by the review, goes on the defensive and actively hides potential risk in the system instead of
   surfacing it.
4. **A template too heavy to actually fill in.** Keeping the checklist current, relevant, and usable matters
   more than keeping it complete; a template that has grown more complex than necessary stops getting filled
   in honestly.
5. **Shallowness that substitutes for the reviewed team's own attention.** A reviewer cannot do another
   team's review for them; the value of the exercise is the time the owning team spends with its own system,
   not the filled-in form a reviewer produces on their behalf.
6. **The template treated as an inflexible rule.** Building this checklist and then treating it as a hard
   and fast set of hoops a team must jump through, rather than a starting point tailored to what the service
   actually needs, misuses the instrument.
7. **Forgetting the humans.** The template is not the point; the conversation the owning team has with its
   own system, prompted by the checklist, is. A review that optimizes for a completed form over that
   conversation has already failed at its own purpose.
8. **Drift after a one-time review, with no trigger to notice it.** A service reviewed once and never
   revisited can drift out of the state the review certified without anyone noticing, which is exactly why
   the standing-standards family requires every member to carry its own named Review Trigger rather than
   relying on a calendar reminder nobody owns.

## Pairing with your process

This bundle ships in the `standing-standards` family alongside `definition-of-done`, `definition-of-ready`
and `launch-coordination-checklist`, as a **tool**: a standing checklist a reviewing team consults, not a
standard the reviewed team is judged against on a cadence. All four are agreed once and consulted
repeatedly rather than authored per occasion, but they answer different questions: a definition of done is
a standard a team is judged against, a definition of ready is the agreement on when a backlog item can be
pulled into a sprint, a launch coordination checklist asks whether one specific launch is ready to ship, and
this review asks whether a service can be run on a standing basis by whoever will carry its pager next.
Keep the boundaries where they belong: this review does not certify one launch, it does not tell a
responder what to type once something has gone wrong, and it checks that a runbook exists without writing
one. Where your organization also runs an Operational Readiness Review under AWS's name for the practice, or
a per-release review under a federal agency's use of this same document's name, this bundle's scope is the
service's standing readiness; route release-moment content, rollback triggers, cost-of-delay estimates,
post-implementation configuration checks, to `launch-coordination-checklist` and `runbook` instead. Update
this file when the questionnaire itself needs to change, not every time a service is reviewed.
