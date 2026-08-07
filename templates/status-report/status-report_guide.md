# Guide: Status Report (operator card)

Fast reference for using the status-report bundle. For the full reasoning, history, and sources, read
[`status-report_companion.md`](status-report_companion.md); a fully worked instance is
[`status-report_example.md`](status-report_example.md).

## When to use

- You need to tell people who are not doing the work where things stand: what changed, what is at risk, and
  what you need from them, on a recurring cadence (daily, weekly, monthly, or quarterly).
- **The document owns none of its own facts.** Every number you would put in it already lives somewhere with
  more authority, a KPI dashboard, a risk register, a RAID log, and your job is to narrate what those sources
  mean for one audience in one period.
- The audience needs the headline, not the instrument. Someone who could just as easily walk a live board or
  open the dashboard themselves does not need this document; write it for the reader who was not in the room.
- The report reaches a governance body, a sponsor, or anyone outside the delivery team who still needs a
  record even though they were not there when the work happened.

## When NOT to use

- **You are defining what the metrics are, not narrating them.** Naming a KPI, its formula, and who owns it
  is the kpi-dashboard bundle's job. A status report reads numbers from that definition; it does not create
  or redefine them.
- **The ask outranks the update.** If the meeting exists to get an approval, open with the decision ask, not
  with "here's what happened since last time." A status report that tries to carry every metric on every
  dimension as evidence for a single recommendation produces exactly the decision paralysis a focused ask is
  meant to avoid; that is a steering-committee or decision paper, not this document.
- **The audience already walks a live board.** A team running a real information radiator has less need for
  a written report between people who see the board daily. Write this for the reader who cannot see it, not
  as a duplicate of it for people who can.
- **You want a formally specified management product with its own defined producer, recipient, and cadence
  rule.** That is PRINCE2's Highlight Report, a distinct named artifact, not a variant of this template. Learn
  from its shape; do not expect this template to replace it inside a PRINCE2 environment.
- **A problem has already happened and needs its own record.** Track it in the risk register or RAID log by
  ID and reference that ID here; do not describe the underlying problem fresh in the report, or you will
  eventually report the same fact twice under two different names.

## Status report, dashboard, or decision paper? (the question people actually have)

| | **Status report** | **KPI dashboard** | **Decision paper / steering session** |
|---|---|---|---|
| Answers | "Where do things stand, and what do you need from me?" | "What are we measuring, and how?" | "Will you approve X?" |
| Opens with | A report: what happened since last time | A metric definition | A decision ask |
| Coverage | Every dimension the audience needs, at summary level | Every metric the objective needs, defined precisely | The narrow evidence for one recommendation |
| Owns its facts? | No, reads them from elsewhere | Yes, this is where a metric is defined | No, reads them from elsewhere |
| Cadence | Periodic (daily to quarterly) | Continuous, standing | Ad hoc, when a decision is needed |

They are a chain, not a choice: the dashboard defines the numbers, the status report narrates what those
numbers mean for one audience this period, and a decision paper narrows to the evidence for one ask when the
report alone would produce paralysis rather than a decision.

## Pick a variant

- **Lean** (default): Summary, Status, Accomplishments, Risks and Issues, Next Steps. The smallest report
  that still says where things stand, what happened, what is at risk, and what comes next.
- **Full**: adds Metrics, Milestones, and Decisions Needed in place, for eight sections total. Use it once
  the audience is empowered to act on the numbers and the asks directly, not just to know the headline, for
  example a steering committee or a sponsor who reads this instead of walking the board.

Grow lean into full by adding sections in place; never reorder the five sections they share. The scaling
signal is audience and cadence, not the size of the program: published templates split first by frequency
(daily, weekly, monthly, quarterly) and second by audience (executive, team, portfolio, department), not by
how much work is under way.

## The rubric

Score each 0, 1 or 2. **Under 13 out of 18 (full) or 9 out of 12 (lean), and the reader will have to go check
the source you were supposed to summarise for them.** The report has stopped doing the one job this document
type has.

| # | Criterion | 0 | 1 | 2 |
|---|---|---|---|---|
| 1 | **Headline stands alone** | No standalone headline; the reader must read the whole report to find the direction | A headline exists but does not say what, if anything, is needed from the reader | A reader who stops after the first sentence could state the direction and what is asked of them |
| 2 | **Threshold beside every colour** | A colour appears with no threshold at all | A threshold is stated, but it is the same number as the target rather than a separate green line, or it lives in another document | Every colour carries the specific rule, a number or a named condition, that produced it, distinct from the target where the two differ |
| 3 | **Accomplishments are completions** | Lines describe effort or intention ("worked on X") | Some lines are true completions; others describe ongoing or planned work | Every line would still be true if checked today, and none could be pasted unchanged into next period's report |
| 4 | **Metrics are traceable** *(full only)* | A number appears with no named source | A source is named, but the colour is graded against the target rather than a stated threshold, or the reverse | Every metric names its system of record, states both target and threshold where they differ, and states which one produced the colour |
| 5 | **Milestones carry a reason** *(full only)* | A milestone has no date | A date and status exist, but an at-risk or missed milestone gives no reason | Every milestone has a date, and any not on track states why in one line, pointing at a named source |
| 6 | **Risks point at the record** | The section restates the whole register with no filter | Items are filtered to what changed, but carry no register reference | Every row names the authoritative register and its ID, and states what changed this period |
| 7 | **Decisions ask, not inform** *(full only)* | The section repeats status or risk information with no decision attached | A decision is named, but has no owner or deadline | Every row names the decision, the decider, the deadline, and the one line of context needed, nothing more |
| 8 | **Next steps are checkable** | Steps are vague continuations ("continue work") | Steps are specific, but nobody could check next period whether they happened | Every step is phrased so a reader could answer yes or no at the next report, and any dependency on a decision above is named |
| 9 | **No duplicate facts** | The same underlying item is reported as two separate things across sections, or against two different sources | The duplication exists but is at least labelled as the same fact | Every fact appears exactly once, and where it is the same underlying item as a sibling register entry, that is stated rather than hidden |

Every cell above describes evidence, not a count. A threshold you can clear by adding rows will be cleared by
adding rows; this library's own `bug-report` research documents that mechanism for defect counts, and a
rubric row is the same kind of target. If you can satisfy a cell without improving the report, the cell is
written wrong.

**Which rows apply to what.** This bundle ships two variants, and three rows grade a section that only the
full variant carries, so scoring lean against all nine would penalise the choice of variant rather than the
quality of the report.

| Variant | Rows that apply | Maximum | Score against |
|---|---|---|---|
| full | all 9 | 18 | **13** |
| lean | 1-3, 6, 8-9 (it carries no Metrics, Milestones, or Decisions Needed section) | 12 | **9** |

Both thresholds sit above two-thirds of the available points; neither is a bare pass mark.

## Named anti-patterns (the usual wrecks)

1. **Watermelon reporting.** Green on the outside, red inside: the status colour and the underlying reality
   have already diverged. Fix: require the threshold beside the colour, not just the colour, so a reader can
   check the claim against the rule instead of trusting the paint.
2. **The gamed traffic light.** A colour distorted to protect the reporter rather than inform the reader,
   especially once a project has already been marked amber or red and the reporter has learned what happens
   next. Fix: name the threshold in advance, before the number that will be graded against it exists.
3. **Status theatre.** A report, or a Decisions Needed section, run for appearance rather than function: it
   satisfies the look of governance while asking nothing of anyone. Fix: keep Decisions Needed to rows with
   an actual decision attached, or write "No decisions needed this period" rather than padding it with
   information.
4. **The report nobody reads.** Mistaking the status report for the whole communications plan, so it goes
   out on schedule and nobody closes the loop on whether it landed. Fix: pair the report with an actual
   feedback channel, not just distribution.
5. **The scarlet letter.** Once a project is marked amber or red, its reputation, and its author's, does not
   recover regardless of the new plan, which is exactly the incentive that produces optimism bias in the
   first place. Fix: separate the colour from the verdict on the person; a report that punishes honesty will
   stop receiving it.
6. **Reporting activity instead of outcome.** Accomplishments that describe what shipped rather than what
   changed for the reader. Fix: ask what a completed line actually moved, not just what it produced.
7. **Duplicating the register.** The same underlying fact reported twice, once in Risks and Issues and again
   somewhere else in the document, under two different names. Fix: read the item and its status from the
   authoritative register by ID; do not re-describe it from scratch in a second place.

## When it is good enough

When a reader who was not in the room can read it once, state the headline, name the one thing that is not
going well, and act on (or approve) whatever this report actually needs from them, without opening the
dashboard or the register to check your numbers.

That last part is the test that matters most: this document type exists to save the reader a trip to the
source. The moment they have to make that trip anyway, the report has failed at the only job it has.
