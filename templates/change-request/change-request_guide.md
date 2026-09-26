# Guide: Change Request (operator card)

**If you searched for "RFC" and landed here:** ITIL calls this document a "request for change (RFC)," but
this library's `rfc` bundle is a different type, a request for comments. Use this bundle for a project or
product baseline change; use `rfc` if you meant the discussion document instead.

The short card. Why the document is shaped this way, and the argument behind every rule here, is in
[`change-request_companion.md`](change-request_companion.md). A fully worked instance is
[`change-request_example.md`](change-request_example.md).

## When to use

- Something already agreed on a unit of product work needs to move: its scope, its requirements, a
  deliverable, or the schedule and cost baselined for it. Four independently published bodies define a
  change request this same way, as an appeal against an *agreed baseline*, not against a wish list.
- The proposal is new and additional to what was already delivered, not a fix for something that was
  supposed to work already.
- The baseline carries weight outside the team: a contract, a regulator, or a budget and scope a steering
  group already signed off on.
- Someone with real authority, one named person or a standing board, needs to choose from a stated set of
  decisions (approve, reject, postpone, or merge), not just agree in a hallway conversation.
- A later reader, an auditor, a new project manager, the next reviewer, has to be able to reconstruct why the
  baseline moved: what changed, what it cost, who decided, and why.

## When NOT to use

- **A team can get there by convincing its own Product Owner.** Scrum routes a Product Backlog change through
  one person, not a board or a form. If the backlog is the only baseline in play, use that channel instead.
- **Something is wrong with what was already delivered.** That is a defect, not a change: file it with
  `bug-report`. The working line: a bug means the delivered work does not do what it already promised to do;
  a change request means someone wants something new that nothing promised.
- **The change targets a running production system that a change advisory board or a configuration control
  board will review.** That IT service lineage is this bundle's closest neighbor and is deliberately not
  templated here. Describe it if you need to name it; do not force it into this form.
- **Nothing was actually agreed yet.** With no baselined PRD, no accepted scope, no signed-off budget, there
  is no "before" for this document to compare against, and the request has nothing to target.

## Is this a change request, an issue, or a defect?

**The published definitions genuinely disagree on where this document lives**, so name your own convention
rather than guessing at someone else's. One convention files a change request as one of several types of
issue, tracked on the issue log; another treats it as its own document with its own log. This library does
not pick a side: the request records where it came from, and links back to the issue log when there is one
(see Implementation and Traceability, full only).

**Against a defect, the line is origin, not severity.** A change request alters something that was agreed; a
defect fails something that was already promised. If the software does not do what it already says it does,
file a `bug-report`. If someone wants it to do something new, file this instead.

## Pick a variant

**Lean (four sections):** The Request, Why, Impact, Decision. Enough to get one well-reasoned decision
recorded and dated. Use it for a change small enough that one reviewer can weigh it without a documented set
of alternatives.

**Full (seven sections):** adds Options Considered, Out of Scope, and Implementation and Traceability. Move
up when the decision needs a documented set of alternatives, including the no-change option, when the
boundary of what the change touches is genuinely ambiguous, or when the project keeps a change log this
request has to feed into cleanly.

## Quality rubric (self-grade)

Score each 0, 1 or 2. **Under 11 out of 16, and a full change request leaves its decider guessing:**
something the decider needed in order to choose is missing. Lean scores against fewer rows, and under 7 out of
10 a lean request leaves its decider guessing in the same way; see the scope table below.

| # | Criterion | 0 | 1 | 2 |
|---|---|---|---|---|
| 1 | **Baseline named** | No baseline stated | A baseline is named, but not its version | Names the specific artifact and version this request targets, so a reader can tell exactly what "before" means |
| 2 | **Honest consequence** | No consequence of declining is stated | A consequence is stated but reads as inflated, or too vague to weigh | States a specific, proportionate consequence of not making the change |
| 3 | **Impact fully assessed** | One or more dimensions are blank | Every dimension has an entry, but some are a bare "impacted" or "yes" | Every dimension carries "None" or a stated effect (a duration, a cost, a scope boundary), so no follow-up question is needed |
| 4 | **Decision named and dated** | A bare yes or no, or no decision recorded at all | One of the stated decisions is recorded, but the decider or a date is missing | One of the stated decisions, one named decider, and a decision date (or a decision-needed-by date) are all present |
| 5 | **Origin links back** | No origin stated for the request | An origin is named, but a logged issue, risk, or decision it came from is not linked | Names the origin and, where a logged record exists, links to it instead of restating it |
| 6 | **No-change considered** *(full only)* | No options section, or only the chosen option is shown | Alternatives are listed, but the no-change option is missing or its impact is not assessed | The no-change option and at least one real alternative are each scored against cost, scope, schedule, and quality, and the win is explained |
| 7 | **Boundary is specific** *(full only)* | No boundary stated, or "nothing else changes" | A boundary is named, but not specific enough to catch a plausible misreading | Names a specific thing a reader could otherwise assume is included, and states plainly that it is excluded |
| 8 | **Record is traceable** *(full only)* | No mention of what happens once the request is decided | States "logged" or "updated" with nothing a later reader could follow | Names the change log entry (or states none is kept), the artifact and version updated, and the origin it links back to |

### Rubric scope by variant

| Variant | Rows scored | Maximum | Threshold |
|---|---|---|---|
| lean | 1-5 | 10 | 7 |
| full | all 8 | 16 | 11 |

Lean ships no Options Considered, Out of Scope, or Implementation and Traceability section, so rows 6 through
8 grade content it does not carry; score lean against rows 1 through 5 only. A lean request at 7 out of 10
clears a comparable bar to a full request at 11 out of 16.

## Named anti-patterns (the usual wrecks)

1. **Change that was never authorized.** Scope creep is defined by authorization, not size: an expansion of
   scope that was approved is not scope creep. Fix: route every scope change through this document, however
   lightweight, rather than letting it enter through conversation.
2. **Decisions that never get made.** A request left without a decision date sits in a board's queue
   indefinitely, with nobody accountable for the delay. This pattern is documented only thinly, a personal
   blog post and two vendor posts, not a measured finding, but the fix is cheap: state a decision-needed-by
   date on every request you file (row 4 above).
3. **Overstating the case to win approval.** Inflating the consequence of declining, to force urgency,
   corrupts the one section (Why) a decider actually needs to read honestly. Fix: write the consequence of
   declining as it actually is, not as leverage.
4. **Calling a request a bug, or a bug a request.** Misclassifying either implies the delivered work was
   defective when it was not, or lets a genuine defect hide behind a change-request queue with a longer
   timeline. Fix: use `bug-report` for something that fails a promise already made, and this template only
   for something new.
5. **Multiple approving authorities collapsed into one status.** A single "approved" line hides which
   authority actually signed and which is still pending, and a decision can get lost in the gap. Fix: record
   each authority's decision on its own line, in Decision or in Implementation and Traceability, never a
   merged status.
6. **Undocumented change reaching production regardless of the paperwork.** This is an engineering caution,
   not a project-management finding: a well-known industrial failure traced back to a change that had not
   been properly thought out, documented, or risk-assessed before it was made. It is included here as the
   reason traceability is worth the friction it adds, not as evidence that project baseline change requests
   specifically fail this way. Fix: treat Implementation and Traceability as load-bearing, not paperwork.

## No paired skill

`pairs_with: []`. No pm-skills skill produces or consumes a change request today. Until one exists, this
template is filled by hand.
