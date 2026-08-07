# sprint-retrospective-notes: history

Change log for the `sprint-retrospective-notes` bundle. Each entry records what changed and why, so a reader
can tell a correction from a preference.

## 0.1.0 - 2026-08-07

**Initial release.** Researched 2026-08-07 across six parallel dimensions: whether the artifact exists at
all, the Scrum Guide by version, the vendor and practitioner template tier, origins and evolution, the
evidence base, and relationships to the incident postmortem.
[`sprint-retrospective-notes_research-log.md`](sprint-retrospective-notes_research-log.md) records **33
sources**, of which **31 were fetched and verified** and **2 had their URL confirmed without the body being
read**. Of the 31 read, 9 are primary, 3 standards, 11 practitioner, and 10 vendor (some sources counted
more than once above; totals as recorded in the log).

**The first member of the `process-docs` family**, adopted in
[ADR 0033 (the process-docs family contract)](../../docs/internal/decisions/0033-adopt-process-docs-family-contract.md),
which groups documents written once to convert hindsight into an owned change. `sprint-retrospective-notes`
looks back on a period, on a cadence; its sibling `incident-postmortem` looks back on an event, triggered by
it, and the two exist to be taught by contrast rather than by a boundary asserted once.

### One size ships

No primary, standards, or vendor source read in this research publishes two weights of a sprint
retrospective notes document. `sizes_available` declares `[lean]` alone, the first build spec this library's
own research has confirmed rather than corrected. The genuine counter-argument, that Derby and Larsen scale
retrospective activities to iteration, release, or project cadence, was tested and rejected as a reason for
a second size: that variation is across occasions, not weights of one document. A release or project
retrospective is a different occasion, not a `full` variant of this sprint-scoped template. See
[`sprint-retrospective-notes_companion.md`](sprint-retrospective-notes_companion.md) section 4.

### Previous Actions is this bundle's own contribution

No published vendor template, Documentero, Smartsheet, or Atlassian, carries a section that checks the
status of the previous retrospective's action items. It ships here because Wolpers names exactly this gap as
a named anti-pattern, and because the mechanism Scrum itself used to carry retrospective output forward is
now optional rather than required: the 2017 Scrum Guide required at least one improvement to travel into the
next Sprint Backlog, and the 2020 rewrite softened that requirement into a permission. Previous Actions is
this bundle's answer to a documented failure, not a restatement of received practice. See
[`sprint-retrospective-notes_companion.md`](sprint-retrospective-notes_companion.md) sections 2 and 3.

### The honest core

**The Scrum Guide defines an event, not a document.** A literal search of the full 2020 text returns zero
occurrences of "action item," "retrospective notes," "root cause," and "blameless." The document tier this
bundle belongs to exists only at vendor level; no primary, standards, or academic source publishes a fixed
template.

**Nothing measured shows a retrospective improves outcomes.** The three software-specific studies read in
full measure content quality, participant perception, and practice, never velocity, defect rate, or
predictability. The largest, 963 statements across 32 teams, found 84.1 percent were bare assertions with no
justification and exactly one statement in 963 weighed a pro against a con. That finding drives the "why"
column this bundle adds to What Went Well and What To Improve, beyond what any vendor heading asks for.

**The postmortem-versus-retro failure mode is this library's own reasoning, not a sourced finding.** The
family contract asserts that running a retro on an incident produces a blameless discussion of a thing that
needed a causal analysis, and running a postmortem on a sprint pathologises ordinary work. No source read in
full states this directly; sources draw the retro/postmortem line by purpose and timing but do not name
confusing the two as an observed failure mode anyone has documented. The companion carries the family
contract's framing as the library's own reasoning and says so plainly. See
[`sprint-retrospective-notes_companion.md`](sprint-retrospective-notes_companion.md) section 6.

**Kerth did not coin "retrospective" as a deliberate rebranding of "postmortem."** His own preface calls the
ritual "postmortem or postpartum... or, my preference, retrospective," a stated preference among names
already circulating, not an argued replacement. The specific naming story, that facilitators Wayne and
Eileen Strider suggested the word to him, appears only in a reader's summary of the book and could not be
verified against Kerth's own text.

**The Prime Directive's exact wording is not stable.** The commonly circulated version reads "we understand
and truly believe" with neutral pronouns; a secondary account and a publisher blurb read "we must
understand" with gendered pronouns. Chapter 1 of Kerth's book, where the Directive itself lives, was outside
the sample this research could retrieve, so the companion quotes the commonly circulated wording and says
so. Whether the Directive itself is sound is recorded as a live, two-sided argument among named people, not
a settled matter.

**A reported trust-drop finding is carried as second-hand and weaker than the directly attributed failure
modes.** A 2025 paper reports a trust-drop finding by citing a separate industrial case study it does not
itself name; it is recorded as weaker evidence than the anti-patterns Wolpers and Cohn attribute to
themselves directly.

### pairs_with declares no skill

Enumerating `tools/known-skills.txt` found no retrospective, retro, or continuous-improvement skill among
the pinned pm-skills IDs. `pairs_with: []` is declared rather than a guessed or approximate match, consistent
with the `rfc` bundle's own precedent for an honest empty list.
