# Guide: Change Log (operator card)

Fast reference for using the change-log bundle. For the full reasoning, history, and sources, read
[`change-log_companion.md`](change-log_companion.md).

## When to use

- A baseline already exists, or is about to be agreed, that someone outside the immediate team will hold
  you to: a spec, a PRD, a scope and a budget a sponsor signed off on. Something is being proposed against
  it.
- More than one person needs a standing, shared answer to "what changed here, and who agreed to it," not
  just an explanation of the one change under discussion right now.
- Requests get decided in ways that are not automatically remembered: in a meeting, in a chat thread, in
  someone's head. This log is the place a decision becomes durable enough to survive the person who made
  it moving on.
- A sponsor or governance body will eventually ask how far the baseline has actually moved in total, not
  just what the most recent change was. That question is answered by summing rows, never by reading one
  (see Pick a variant, below, and Cumulative Effect in the full variant).

## When NOT to use

- **Nothing has been baselined yet.** This log tracks change against something that already exists and has
  been agreed; a document still being drafted or negotiated has no baseline yet for a change to be measured
  against. Route that activity through whatever process produces the first agreed version.
- **It is a software release.** A software changelog is a different, adjacent artifact under the same word:
  it is written for users and contributors, and it carries no requester, decider, or decision field at all.
  Route release notes there, not here.
- **The team already runs PRINCE2 and keeps requests for change inside its issue register.** That is a
  named, defensible methodology choice, not a gap this log exists to close. Decide explicitly which
  artifact holds the function; do not run both without saying so.
- **Change routes through one person's ongoing judgment against an emergent backlog, with no baseline that
  carries weight outside the team.** A standing change log adds process a team like this does not need.
  Adopt one once a baseline exists that someone outside the team can hold the project to: a contract, a
  regulator, or a sponsor-signed scope and budget.

## Change log, or change request?

The two are easy to conflate because one feeds the other. They are not interchangeable.

| | **Change log** | **Change request** |
|---|---|---|
| What it is | The standing register: one row per request | One document, filed to describe and justify a single change |
| Lifecycle | Never finished; every disposition stays on it | Filed once, decided, then archived |
| Deletion | No row is ever removed, whatever was decided | N/A, it is a single document |
| Audience | Whoever needs the cumulative, governing picture | Whoever must decide this one request |

The request feeds a row into the log; the log is not a second copy of the request, and the request is not a
substitute for the log. If your team runs PRINCE2, the same relationship holds inside the issue register
instead, by that methodology's own design (see When NOT to use, above).

## Pick a variant

- **Lean** (default): Purpose and Boundary, Status Vocabulary, Change Log, Authority and Escalation. A
  complete working register a team can populate and govern from the first submitted request, without a
  formal delivery hand-off, a standing cumulative figure anyone asks for, or a question about who keeps
  the log.
- **Full**: adds **Implementation and Traceability** (the target and actual delivery dates, kept apart from
  the decision date, plus links back to the request document and to related logs), **Cumulative Effect**
  (the running total of approved change against the baseline as first agreed), and **Review and Ownership**
  (a named keeper and a stated cadence). Move to full once a sponsor or governance body will ask, weeks
  later, how far the baseline has moved in total; once the decision date and the delivery date genuinely
  diverge often enough that conflating them would mislead a reader; or once the log needs a named owner
  because more than one person could plausibly be asked to keep it.

Grow lean into full by adding the three sections; the first four keep their name, order, and table. The
scaling signal is whether anyone outside the team will ask about the baseline's total movement or the gap
between deciding and delivering, not how large the project is.

## Quality rubric (self-grade)

Score each row 0, 1, or 2. Below 11 out of 16, the first reader who actually tries to trace one change
through this log, from request to decision to delivery, will hit a row they cannot follow: a status
standing in for a decision, a baseline named only as "the project," or an escalation nobody can confirm was
ever resolved. A lean log carries no delivery, cumulative, or ownership section to trace, so it is scored,
and cleared, against a smaller table; see the scope table below.

| # | Criterion | 0 | 1 | 2 |
|---|---|---|---|---|
| 1 | **Boundary is drawn** | No line says which baseline, by artifact and version, this log tracks | A baseline is named, but nothing says what is deliberately left out | You can point at the sentence naming the exact baseline artifact and version, and at the sentence ruling out at least one named neighbor (the request document, a software changelog, an issue register) |
| 2 | **Decision kept separate** | Only a status list appears; no separate decision value is defined anywhere | A decision value exists, but a closed or denied row does not show which one it received | You can point at any closed row and name both its status and its decision, because the two are recorded as separate fields, never folded into one word |
| 3 | **Rows never deleted** | A rejected, withdrawn, or postponed request cannot be found on the table, and nothing states closed rows stay | A closed row exists, but nothing about it or the log's own framing rules out that it could be quietly removed later | You can point at a row with a non-approved outcome, still on the table, carrying its reason, and the log states plainly that no row is ever removed once decided |
| 4 | **Baseline named per row** | A row names no baseline artifact, or names only "the project" or "the plan" | A baseline artifact is named on most rows, but its version is missing, blank, or inconsistent row to row | Every row names the exact artifact and version it would change, and a reader could go find that version without asking the keeper what it meant |
| 5 | **Authority threshold stated** | No decider is named, or the only statement is that "the team decides" | A decider is named, but nothing states the point at which a change must go above them | You can point at a stated threshold, in figures or scope terms, and at any row marked escalated, name who it went to and what decision is being waited on |
| 6 | **Delivery dated separately** *(full)* | One date field stands for both when a change was decided and when it shipped | Two date fields exist, but at least one implemented row leaves the actual date blank or repeats the decision date | Every implemented row carries a decision date and a separate actual date, and where they diverge, that gap is visible rather than absorbed into a single stamp |
| 7 | **Cumulative effect computed** *(full)* | No running total appears, or one appears without saying which rows produced it | A total is stated, but a reader cannot trace it back to specific rows above it | The section names the specific approved rows the total was computed from, and does not present an illustrative figure from elsewhere as though it were this log's own measured number |
| 8 | **Named keeper, current review** *(full)* | No individual is named as keeper, or no cadence is stated | A keeper and a cadence are both named, but the log's last-reviewed date is older than that cadence allows | A specific person is named as keeper; the cadence is stated as this team's own choice; and the last-reviewed date falls inside it |

### Rubric scope by variant

| Variant | Rows scored | Maximum | Threshold |
|---|---|---|---|
| lean | 1-5 | 10 | 7 |
| full | 1-8 | 16 | 11 |

Lean ships no Implementation and Traceability, Cumulative Effect, or Review and Ownership section, so rows
6 through 8 grade content it does not carry; score a lean log against rows 1 through 5 only. A lean log at
7 out of 10 clears a comparable bar to a full log at 11 out of 16.

## Named anti-patterns (the usual wrecks)

1. **A status standing in for a decision.** "Closed" tells a reader the row stopped moving, not which way it
   went; a change can be closed because it was approved, or closed because it was rejected, and the word
   alone cannot say which. Fix: a decision field, kept apart from status, on every row that is no longer
   open.
2. **A rejected or withdrawn row quietly removed.** Deleting a row that went the wrong way erases the
   record that the request was ever considered, and invites the same request to come back with nobody
   able to say it was already declined and why. Fix: every disposition stays on the table, with its reason,
   for as long as the log exists.
3. **The baseline left unnamed.** "Tracks changes to the project" tells a reader nothing they could check.
   Without an artifact and a version, two readers can disagree about which document a row is even changing.
   Fix: name the baseline, by artifact and version, in the Purpose and Boundary section and again on every
   row.
4. **Authority named without a threshold.** "The board approves changes" says who decides, not when a
   change is small enough to skip them. Without a stated threshold, every request becomes its own argument
   about whether to ask. Fix: state the threshold before it is tested, not the first time a change reaches
   it.
5. **One date doing the work of two** *(full)*. Recording only an "approval date" and letting it stand for
   both the decision and the delivery hides exactly the gap a later reader, or an auditor, most needs to
   see. Fix: a decision date and a separate actual date, on every implemented row.
6. **A cumulative figure asserted instead of computed** *(full)*. A running total that does not trace back
   to the specific rows behind it is a guess wearing the shape of a measurement. Fix: name the rows the
   total was built from, every time it is stated.
7. **A log with no named keeper, or a review date nobody kept current** *(full)*. A register nobody owns
   and nobody actually reopens is a file, not an instrument, however complete its rows look on the day it
   was written. Fix: one named person as keeper, and a last-reviewed
   date that stays inside its own stated cadence.
8. **Collapsing this log into the request it tracks, or into a software changelog.** The request is one
   document about one change; this log is the standing register that outlives any single request. A
   software changelog serves users and contributors and carries no requester, decider, or decision field at
   all. A log that has quietly become either has stopped doing this artifact's job. Fix: keep the two
   documents apart, and route release notes to the artifact built for them.

## No paired skill (yet)

There is **no governance skill in the product-on-purpose org today** that this bundle's `pairs_with` could
point to, so it adopts `[]` until one exists. The one pm-skills name that looks like a match,
`utility-pm-changelog-curator`, drafts software changelog entries from git history: a different artifact
under the same word, not this one (see When NOT to use, above). Until a governance-side skill exists, this
template is filled by hand.
