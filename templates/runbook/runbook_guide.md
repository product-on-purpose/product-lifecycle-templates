# Guide: Runbook (operator card)

The short card. Why the document is shaped this way, and the argument behind every rule here, is in
[`runbook_companion.md`](runbook_companion.md). A fully worked instance is
[`runbook_example.md`](runbook_example.md).

## When to use

- A known alert or condition can fire again, and the response should not depend on who is on call when it
  does.
- More than one person might have to run this procedure, so the steps cannot live only in one engineer's
  head.
- The situation is scoped to one trigger: one alert, one condition, one page. If you can name it in a
  sentence, it belongs here.
- You want a named signal that tells a responder the situation is actually resolved, not just quiet.
- The work is regulated or audited, and a record of what was checked has to survive the incident.

## When NOT to use

- **You do not yet have a known trigger.** If nothing has paged yet and you are documenting a service in
  general, write a wiki page or a design doc, not a runbook. A runbook exists because of a trigger, not a
  topic.
- **The steps never vary.** If the on-call engineer runs the same deterministic commands every time this
  alert fires, that is a candidate for automation, not more documentation. Writing a better runbook for a
  fully deterministic procedure treats a symptom instead of the cause.
- **You need to recover a whole system at an alternate facility after a major failure.** That is a disaster
  recovery plan, one register above what this template covers.
- **You are documenting an entire service:** its overview, deployment, security posture and disaster
  recovery in one place. That is a standing service-operations manual, a bigger scope than this template, not
  a bigger size of it. Growing Prerequisites and Access past a handful of lines is usually the first sign
  this is happening.
- **You only need a memory guard against omission**, the Gawande sense of a checklist, not a full procedural
  walkthrough. A checklist is deliberately smaller than a runbook.
- **The content only explains, and never directs.** "Check the logs and restart the service if needed" is a
  knowledge base article. A runbook must go further: a specific action for a specific trigger.

## Pick a variant

**Lean (four sections)** is the default: Purpose and Trigger, Procedure, Validation, Review Trigger. It is
close to the smallest shape actually published for this kind of document, and a runbook a responder cannot
read in the middle of an incident has already failed at its one job.

**Full (seven sections)** adds Prerequisites and Access, Remediation and Cleanup, and When This Does Not
Apply. Notice what the three additions have in common: none of them is content a responder needs while the
alert is actively firing. Prerequisites is read before the incident starts, Remediation and Cleanup after it
ends, and When This Does Not Apply is a scoping note rather than a step. Move to full when at least one of
these is true:

- the environment is regulated, and Validation needs to double as an audit trail;
- more than one team could plausibly run this procedure, so an explicit boundary and named prerequisites
  keep the wrong team from running the wrong runbook;
- the service is complex enough that "this does not apply here" needs to be said rather than assumed.

Every lean heading appears in full unchanged, in the same order, so growing from lean to full is additive.
You never rewrite what you already agreed.

## Quality rubric (self-grade)

Score each 0, 1 or 2. Full below 11 out of 16 ships a document a responder cannot run without guessing,
which is the one failure this artifact exists to prevent; lean is scored on five of these rows only (see the
scope table below), and below 7 of 10 the same failure applies to the smaller shape.

| # | Criterion | 0 | 1 | 2 |
|---|---|---|---|---|
| 1 | **Trigger is specific** | A general topic, not a stated alert or condition | Names an alert, but no stated system or outcome | Names the specific alert or condition, the system it belongs to, and a one-line outcome you could check later |
| 2 | **Style is declared** | No statement of general or step-by-step | States which, but later steps drift into the other style | States which explicitly, and every step reads consistently with that choice |
| 3 | **Steps resolve, not describe** | Steps like "open the dashboard" or "check the logs" with nothing named | Some steps name a command or dashboard; others stay vague | Every step names the exact action and a result a second person could check without asking the author |
| 4 | **Validation resists false negatives** | "Confirm it's fixed," no named signal | One named signal, and it is only the alert clearing | A named signal independent of the alert clearing, with the value that counts as pass and where to look |
| 5 | **Prerequisites earn their place** *(full)* | Nothing listed, or a general "have access" | Items listed but not tied to a specific procedure step | Every item is something that would actually block step 1, named specifically, with how to get it before an incident |
| 6 | **Cleanup items are owned** *(full)* | Nothing recorded, or an unowned "fix later" | Items listed, but missing an owner or a deadline | Every temporary change has a named owner and a trigger or deadline for reverting it |
| 7 | **Near-misses are named honestly** *(full)* | The section is missing or deleted | Filled with a catch-all vague enough to describe anything | Names specific lookalike symptoms and their actual cause, or states "none identified" as a considered answer |
| 8 | **Trigger is event-based** | A calendar cadence alone, or nothing | An event is named, but no owner | A specific system event is named, paired with a named owner and what they do about it |

**Which rows apply to what.**

| Document | Rows | Maximum | Score against |
|---|---|---|---|
| full | all 8 | 16 | **11** |
| lean | 1-4 and 8 | 10 | **7** |

Rows 5, 6 and 7 are scored only against full. Lean ships none of Prerequisites and Access, Remediation and
Cleanup, or When This Does Not Apply, so grading it on those rows would penalise the choice of variant rather
than the quality of the document.

The test behind every cell above: **could someone satisfy it without improving the document?** A row that
counted prerequisite items, cleanup rows, or near-misses would reward padding. Every cell instead asks
whether a specific piece of evidence exists, and whether a second person, not the author, could find it.

## Named anti-patterns (the usual wrecks)

1. **Silent decay.** A runbook does not announce that it has gone stale; the system it describes keeps
   changing while the document does not, and the gap is invisible until the moment someone actually needs
   it. The fix is a real Review Trigger: a named event and a named owner, not a hope.
2. **Written for yourself, not for the reader.** The author knows which dashboard, which credentials, which
   unstated assumptions hold. The next responder does not. The tell is a step that only makes sense to the
   person who wrote it; the fix is having someone who did not write the runbook try to run it.
3. **The wiki-versus-code mismatch.** The runbook lives in a wiki. The system it describes lives in code.
   Nothing forces the two to change together, so they drift apart on different schedules maintained by
   different people.
4. **A knowledge-base sentence dressed up as a step.** "Check the logs and restart the service if needed"
   explains; it does not direct. A runbook step names the exact log, the exact command, and the result that
   tells you it worked.
5. **Too many steps in one document.** A responder under pressure cannot scan a runbook that tries to cover
   several unrelated situations at once. If you are listing multiple unrelated triggers, you are writing two
   runbooks under one title; split them.
6. **Not linked from the thing that triggers it.** A correct runbook nobody can find during the incident is
   functionally the same as no runbook. If the alerting tool supports linking an alert to its runbook, do it.
7. **Calendar-only review, treated as sufficient.** A quarterly cadence or an untouched-duration heuristic
   catches staleness eventually, but neither catches it at the moment the system actually changed, which is
   the moment it matters. Pair any calendar cadence with a named event trigger.
8. **Citing an unmeasured number as though it were a finding.** Runbooks are widely asserted to shorten
   incidents and rarely, if ever, independently measured doing so. State the value case honestly, as an
   assertion, rather than attaching a specific percentage nothing behind it can support.

## Pairing with your process

This bundle ships in the `standing-standards` family alongside `definition-of-done`. A definition of done is
a standard a team is judged against; a runbook is an instrument a team executes. Keep the two apart: a
runbook does not certify that work is finished, and a definition of done does not tell a responder what to
type. Where your incident tooling supports it, link this document from the alert it answers, per the Purpose
and Trigger section; that link is what turns a correct runbook into a findable one.
