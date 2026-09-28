---
status: proposed
date: 2026-09-27
decision-makers: [jprisant]
consulted: [claude]
---

# The steering committee pack does not ship: its periodic written form is the shipped `status-report`, and its composite exists only as a deck

## TL;DR

- **Decision:** `executive-briefing-steering-committee-deck` **does not ship**, and the `communication-docs`
  forecast that named it is corrected in place with a date.
- **Why:** the catalog describes one pack that carries status, risks, decisions sought and asks. The only
  named source found for that composite is a slide deck. The written sources split it into two different
  documents: a **periodic report** to the steering group, and an **event-driven decision paper** written when
  one decision is needed. **The periodic report is what the shipped `status-report` already is**: its worked
  example is addressed to the "Program steering group", fortnightly, and carries a Decisions Needed table.
- **The decision paper is distinct, and it is not queued.** `decision-docs` admits only technical decisions,
  and the maintainer chose on 2026-09-27 not to widen it.
- **This is not a zero-source refusal.** The written forms clear
  [ADR 0030](0030-templating-scope-markdown-documents.md)'s admission test under other names. The decline
  rests on duplication and family fit, like
  [ADR 0064 (deployment-plan is declined)](0064-deployment-plan-is-declined.md), decided the same day.
- **Status:** proposed 2026-09-27, on the maintainer's ruling of the same day. Held proposed until the
  maintainer reads the diff, as [ADR 0059](0059-announcement-internal-comms-joins-delivery-docs.md) and
  [ADR 0060](0060-change-request-joins-delivery-docs.md) were.

## Context and Problem Statement

The catalog lists `executive-briefing-steering-committee-deck` as a Tier-2 candidate (aliases `exec update`,
`steerco pack`, `QBR deck`; purpose "Brief executives on status, decisions needed, asks"). The
`communication-docs` contract has named "`executive-briefing` / steering-committee pack" as a likely future
member since it was adopted by [ADR 0034](0034-adopt-communication-docs-family-contract.md). The shipped
`status-report` guide also routes one kind of reader away from itself, to "a steering-committee or decision
paper, not this document" (`status-report_guide.md:27`).

A research pass on 2026-09-27 tested the type against ADR 0030's admission test and against all nine family
contracts. Because the library templates written documents only, it looked for the written form a deck may
accompany.

## Decision Drivers

- **The library templates written documents, not decks** (ADR 0030).
- **A candidate that duplicates a shipped bundle adds a second template for one job.** Two templates for one
  document would split readers between them and teach neither boundary.
- **A family-contract widening stops for the maintainer**
  ([decision-procedures.md, "What always stops for the maintainer"](../decision-procedures.md)).

## Considered Options

1. **Decline the pack; correct the forecast; tighten the `status-report` pointer.** Chosen.
2. **Build the periodic pack in `communication-docs`**, set apart from `status-report` by its steering
   audience. Its axis fits, since the pack recurs per meeting, but the document it describes already ships.
3. **Build the event-driven decision paper** by widening `decision-docs` from technical to business
   decisions. Real and sourced, but it is a different type from this catalog row, and the maintainer did not
   queue it.
4. **Build the composite anyway**, as a Markdown rendering of a deck.

## Decision Outcome

**Chosen: option 1.**

### The composite exists only as a deck

The source nearest the catalog's own alias "steerco pack" is Influential PMO's SteerCo Pack template. Its
page is organised around "Creating a Project SteerCo Template in PowerPoint", with sections such as
"SteerCo Pack Action Log" and "SteerCo Pack Decisions". No written source in this pass combined status,
risks, decisions sought and asks in one document. Option 4 would therefore invent a written document to fill
a catalog slot, which is the move ADR 0030 refused for `wireframe`.

### The periodic written form is what `status-report` already is

The European Commission's PM² methodology publishes two periodic reports. "A Project Status Report is a
frequent report" that "contains just a one-page summary of the project status". "The Project Progress Report
is an artefact created by the Project Manager", written "to inform the Project Steering Committee (PSC) on how
the project is progressing". Both are reports on the state of the work, sent to governance on a cadence.

The shipped `status-report` already is that document for this library, by its own worked example:

- its audience is the "Program steering group" (`status-report_example.md:6`);
- its cadence is "Fortnightly, timed to the program steering group's review" (`status-report_example.md:7`);
- it carries a Decisions Needed table that names the decider and the context for each ask
  (`status-report_example.md:94-98`).

Option 2 would therefore ship a second template for the document `status-report` already covers.

### The event-driven decision paper is distinct, and it has no family

A different written document appears when one decision is needed. Canada's Privy Council Office publishes a
Memorandum to Cabinet in *A Drafter's Guide to Cabinet Documents* (2013), with named parts that include
"Implementation Plan" and "Due Diligence". The US Department of Homeland Security publishes a template headed
"DECISION MEMO". Queen's University's School of Policy Studies teaches a briefing note written "to obtain a
decision". The Governance Institute of Australia recommends "specific headings be included in all papers,
such as" purpose, proposed resolution, recommendation and next steps.

That document is not this catalog row, and no family admits it. `decision-docs` admits "a technical
decision-or-design artifact of the develop phase" ([`decision-docs.md`](../contracts/decision-docs.md),
section 1), and a funding approval or a scope ruling is not a technical decision. Admitting it would widen
that contract, as ADR 0060 widened `delivery-docs`, and the maintainer chose not to queue that change.

### The three edits this record carries

1. **`communication-docs.md`, the forecast.** A dated correction follows the forecast, in the same style as
   the 2026-09-25 correction for the release announcement. The forecast itself stays as written, because it
   was a forecast.
2. **`status-report_guide.md:27`, the pointer.** "that is a steering-committee or decision paper, not this
   document" becomes "that is a decision paper, not this document". The sentence routes a reader who needs a
   single recommendation, which is the event-driven document, and the steering-committee name would now
   point at the type this record declines.
3. **`status-report_companion.md`, the matching heading.** "Status report vs steering-committee or decision
   paper" becomes "Status report vs decision paper", for the same reason.

### Consequences

**Good.**

- The library does not ship two templates for one document, and the `status-report` pointer stops naming a
  type the library has declined.
- The event-driven decision paper is named and sourced here, so a later decision to widen `decision-docs`
  starts from evidence rather than from nothing.

**Bad, and stated plainly.**

- **A team that wants one decision paper for its steering committee finds no template here.** It gets
  `status-report` for the periodic read and nothing for the one-off ask.
- **`communication-docs` loses the second of its three forecast members**, after the internal announcement
  went to `delivery-docs` by ADR 0059. It stays at one member, which its contract calls an acceptable outcome.
- **The catalog row stays `candidate` and carries no state override**, following
  [ADR 0049 (pi-release retrospective fails the admission test)](0049-pi-release-retrospective-fails-the-admission-test.md):
  the `out-of-scope` value is for a refusal about the medium, and `gen-atlas.py` forces `state_note` to empty
  for any candidate. The decline is discoverable through this record and the
  [`tier2-specs.md`](../tier2-specs.md) progress table.

### What would reopen this, stated so it is falsifiable

1. **A named source publishes the composite as a written document**: status, risks, decisions sought and
   asks under one cover, not as a deck.
2. **The maintainer widens `decision-docs` to admit a business decision paper.** That would open the
   event-driven document, not this catalog row, and it would need its own research pass and record.
3. **A real team asks for a steering pack that `status-report` does not serve.** A documented request is
   evidence a web search cannot produce.

## More Information

- The research: the admission sweep of 2026-09-27, summarised in this type's row of
  [`tier2-specs.md`](../tier2-specs.md)'s progress table.
- Related records: [ADR 0030 (templating scope)](0030-templating-scope-markdown-documents.md),
  [ADR 0034 (the communication-docs family contract)](0034-adopt-communication-docs-family-contract.md),
  [ADR 0049 (pi-release retrospective fails the admission test)](0049-pi-release-retrospective-fails-the-admission-test.md),
  [ADR 0059 (announcement-internal-comms joins delivery-docs)](0059-announcement-internal-comms-joins-delivery-docs.md),
  [ADR 0064 (deployment-plan is declined)](0064-deployment-plan-is-declined.md).
