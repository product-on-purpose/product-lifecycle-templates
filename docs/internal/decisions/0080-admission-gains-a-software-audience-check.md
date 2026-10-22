---
status: accepted
date: 2026-10-22
decision-makers: [jprisant]
consulted: [claude]
---

# The admission test gains a fifth check: does a software, UX or technology team write or use the document

## TL;DR

- **Decision.** Add a fifth admission check. It asks whether a named source shows a software product, UX or
  technology team writing or using the candidate document. The maintainer chose to draft this test. Every
  choice below began as this library's own recommendation, and the maintainer's delegation adopted each one.
  The question of a same-job source under another name stays open.
- **The gap this closes.** The written admission rules ask whether a document exists as a written form (ADR
  0030, ADR 0048 and ADR 0078) and whether it fits its phase (ADR 0077). Admission sweeps also ask whether a
  built bundle already does its job. None of these asks who writes the document. Four of the seven
  candidates still waiting on one settling read trace to sources outside this library's stated audience.
  Those sources are NASA, the Department of Defense (DoD), ISO 27001 and the Behavioural Insights Team (BIT).
- **Status:** proposed 2026-10-22, **accepted 2026-10-22 on the maintainer's delegation**. This record's text
  was offered for a read, and the maintainer directed a merge on the agent's best judgment. That direction
  stands in for the read, as similar ones did for
  [ADR 0074](0074-analytics-requirements-measurement-plan-per-feature-is-declined.md) and
  [ADR 0078](0078-maps-canvases-and-session-records-are-templatable-through-their-written-form.md). This
  record amends no family contract, so the standing stop for a contract read does not apply. **Its
  recommendations were accepted without a read**, and the maintainer may change any of them by a dated note.

## Context and Problem Statement

[AGENTS.md](../../../AGENTS.md) states the library's scope in its first section. It is "a library of
document-template bundles for product management and software delivery." Every admission test written down
so far checks a different thing. ADR 0030 and ADR 0048 ask whether a candidate is a real written document.
ADR 0077 asks whether it fits a phase, for `define` candidates. ADR 0078 asks whether its written form
clears scope. None of them asks whether the candidate belongs to the audience AGENTS.md names.

The gap surfaced during PR #300 (the Define re-score), which re-tested 67 candidates from three earlier
sweeps. Seven candidates came back evidence-insufficient: one more read would settle each. Checked against
the score files directly, four of those seven trace outside this audience. One is a NASA
concept-of-operations document. One is a DoD Initial Capabilities Document. One is a regulatory
requirements register sourced to an ISO 27001 control. One is the Target phase of the Behavioural Insights
Team's TEST method. Each of the four could still clear every written test above on its own evidence. None
of the four tests would catch that no source on disk shows a software, product or UX team writing or using
any of them.

**This is not a new problem; it has already been applied twice without being written down.** The design
brief's admission sweep (#294) ran a research dimension asking which sources show "software and
product-team practice." The opportunity statement's admission sweep (#298) recorded, for the same reason,
whether each source describes "software product, UX or technology practice." One sweep asked the question
before this test was proposed; the other asked it after the maintainer approved drafting one.
Neither sweep could point to a record stating the rule, because none existed.
[Decision procedure 5 in `decision-procedures.md`](../decision-procedures.md#5-an-unwritten-rule-is-being-applied)
names exactly this failure: "an unwritten criterion applied twice becomes precedent without ever being
ratified." Its remedy is to state the rule in the artifact that applies it, and name the decision record
that owns it. This record is that remedy.

**What ADR 0041 (maintainer preference sets the build order) does not already cover.** ADR 0041 settled
that the maintainer's own preference, not a demand count, decides which queued candidate gets built next.
It says nothing about whether a candidate should be admitted in the first place. A thinly sourced NASA or
DoD document could clear every written test today. It could then sit in the queue indefinitely, waiting
only on the maintainer's own informal judgment to never be built. A written test makes that judgment
checkable. It also makes the judgment consistent across research sweeps, rather than depending on whether a
given scorer remembers to ask.

## Decision Drivers

- **The library's own stated scope names an audience.** AGENTS.md calls this a library "for product
  management and software delivery," not a general-purpose document library.
- **An unwritten rule applied twice is precedent without ratification.** Decision procedure 5 names this
  failure directly. It has already happened twice in one week.
- **The existing tests ask whether a document exists, not who writes it.** ADR 0030 and ADR 0048 are about
  form and source count. Adding an audience question to either would conflate two different questions.
- **A document can be legitimate for this library without originating in software.** A risk register and a
  runbook are both built bundles. Neither practice began in software. Both are written and used daily by
  software and technology teams today.
- **False negatives cost more than false positives here.** Declining a type outright on thin evidence
  forecloses it. A later read might still find software-side adoption that the first read missed.

## Considered Options

1. **No new test.** Leave the audience question to the maintainer's informal judgment under ADR 0041.
   Cost: the same unwritten rule gets applied a third time and a fourth time, invented fresh each time.
2. **A signal.** Audience evidence lowers a candidate's build priority but never excludes it from admission.
   Cost: priority is the currency ADR 0041 gave to the maintainer's preference alone. A second, written
   priority signal reopens the question ADR 0041 closed.
3. **An unqualified gate.** Failing the audience test excludes a candidate outright, with the same force as
   the written-form test. Cost: it forecloses a type the first time evidence is thin. A later read might
   still find software-side adoption, so this is harsher than this library's existing practice for a thin
   written-form reading, which is recorded as evidence-insufficient rather than declined.
4. **A qualified gate.** Failing the audience test excludes a candidate from admission on its own. But when
   it is the only failing test, the outcome stays evidence-insufficient. The record names the adoption
   evidence that would settle it, rather than declining the candidate outright. Cost: one more outcome label
   to track. This test still has to run alongside the other four before any candidate reaches a final
   outcome.

## Decision Outcome

**Chosen: option 4, a qualified gate, on the maintainer's delegation. Confidence: medium.**

A candidate needs at least one named source. That source must show a software product, UX or technology
team writing or using the document. Failing this test, on its own, parks the candidate as
evidence-insufficient rather than declining it outright, because adoption evidence can arrive later even
when origin evidence cannot. Failing it alongside another failing test keeps that other test's own outcome.
This test adds a reason to park a candidate; it does not soften a reason to decline one.

**Why a gate rather than a signal.** [`decision-procedures.md`'s closing list](../decision-procedures.md#what-always-stops-for-the-maintainer)
names scope, what this library is willing to template, as a question that always stops for the maintainer.
It is not a procedure applied without asking. Whether a document belongs to this library's stated audience
is a scope question in that sense, not a priority question. A signal would hand the audience question back
to ADR 0041's ranking currency. Keeping that currency clean is the one thing ADR 0041 was written to do.

**What this costs against the stricter option.** Under option 3, an audience fail alone would make a
candidate's settling read unnecessary to run at all. Under the chosen option 4, it does not. All seven
candidates already sit at evidence-insufficient. A likely audience fail does not change that label for the
NASA document, the DoD Initial Capabilities Document or the Behavioural Insights Team's TEST method. It
lowers how much their settling read is worth running soon. A pass on their other tests would still leave
them parked, pending adoption evidence. That is a smaller gain than option 3's, named here rather than
overstated.

### What counts as a pass

**Chosen: at least one named source shows a software product, UX or technology team writing or using
the document, regardless of where the document originated. Confidence: high.**

A document that originates outside software still passes if software teams write or use it. The risk
register and the runbook make the case. Neither practice began in software. Both are written daily by
technology teams today. The test asks about current use, not about the document's first author. A
candidate whose only sources are aerospace, defense, security-compliance or public-policy practice, with
nothing on disk showing software or product adoption, fails it.

**One open tension inside this criterion, flagged rather than resolved.** Should a pass require the exact
document name in software use, or only the same job under a different name? Heap, a software
product-analytics company, publishes a written document it names "Design Brief," with quotations checked against the page text. That
alone clears a name-match reading for `design-brief` (#294). Basecamp (37signals) publishes a near neighbour
of the same concept-to-design handoff, the Shape Up "pitch", under a different name. A job-match reading
would count a source like that too. A name-match reading would not need to, since Heap already clears the
test by name on its own. This record recommends that a
name-match be sufficient but not required. Either one source under the same name, or several sources doing
the same job under different names, should clear the test. Confidence: medium. This library already treats
differently named, same-job documents as aliases elsewhere. The point of view statement is ruled an alias
of `problem-statement`. That existing practice argues for the job-match reading, but no written rule yet
says so for this test specifically.

### Scope

**Chosen: applies to every admission sweep and re-score from now on. Not retroactive to the 49 built
bundles or to candidates already decided. Confidence: high.**

Going forward, the test applies to every one of the catalog's 207 types, as each comes up for an admission
sweep or a re-score. It does not reopen a built bundle's own admission. It does not revisit a candidate a
prior record already decided. This matches how ADR 0077 and ADR 0078 both took effect. Neither reopened a
built bundle's phase or admission, and both named what they left unchanged. No built bundle is retested by
this record.

### Where the test is written down

**Chosen: a dated note on ADR 0030, naming this record, following the exact precedent of the dated
note ADR 0078 added to ADR 0030 on 2026-10-17. Confidence: medium-high.**

ADR 0030 already carries the library's type-level admission test. It already carries one dated note
pointing a reader to a later record that clarifies how the test applies: ADR 0078, on maps and session
records. Adding a second such note, pointing to this record, keeps every reader of the admission test in
one place rather than three.

`templates/methodology.md` carries no admission-test language today, so it is the wrong home. It governs
how an already-admitted type gets built, not whether a type is admitted. `docs/internal/decision-procedures.md`
collects a judgment call only once it has resolved the same way at least twice inside this library's own
history. This exact question was informally asked twice. Both times happened in the same week as this
record, before any record had ratified an answer. Writing a procedures entry now would record a procedure
ahead of its own first ratified application, not after two of them. A procedures entry can follow
once this record itself has been applied at least once.

## Consequences

- Good, because the audience question becomes checkable the same way every time, rather than depending on
  whether a given research sweep happens to ask it.
- Good, because the NASA document, the DoD Initial Capabilities Document and the Behavioural Insights
  Team's TEST method can likely be deprioritized now, ahead of spending their own settling read, since
  nothing on disk ties any of the three to this library's stated audience.
- Bad, because it adds a fifth question to run alongside four others before any candidate reaches a final
  outcome. That is one more research step per candidate.
- Bad, because the name-match-or-job-match tension in "what counts as a pass" is not fully resolved here. It
  will need a ruling the first time it actually changes an outcome.
- Neutral, because no built bundle and no already-decided candidate changes as a result of this record.

## Applying the test

Each line states the audience-test outcome only. It does not restate that candidate's other
open questions: phase fit, distinctness, or whether its written-form evidence itself survived a raw-text
check.

**The two in-flight candidates**

- **`design-brief` (#294).** Heap, a software product-analytics company, names and publishes its own
  written "Design Brief," with quotations checked against the page text. This passes on Heap alone, by name match, independent of
  the open name-versus-job tension above. Confidence: high.
- **`opportunity-statement` (#298).** Nielsen Norman Group and Jeff Gothelf, already logged as sources [1]
  and [12] in `problem-statement`'s own research log, are software and UX practice sources. This passes on
  those two. Confidence: high. It leaves distinctness from `problem-statement` untouched: NN/g's own source
  is the one that calls the two documents "written and used in the same way."

**The seven evidence-insufficient candidates**

- **NASA's Needs, Goals and Objectives statement with its Concept of Operations.** No source on disk ties
  this document to a software, product or UX team. Its context is program and mission selection. Likely
  fails. Confidence: low, a judgment call pending its own settling read.
- **A platform and device support matrix.** Its one source, GOV.UK, is explicitly about web and software
  device support. Likely passes. Confidence: medium, since the matrix's own written form is still unread.
- **The DoD Initial Capabilities Document.** Its scope is general military capability gaps, not software
  products specifically. A separate DoD software-pathway document exists but was not the one scored here.
  Likely fails. Confidence: low, a judgment call.
- **The proto-persona (Lean UX).** Lean UX is software and product practice by name. Likely passes.
  Confidence: medium, since the one source found for this candidate was dropped on its own raw-text check.
- **An accessibility conformance target.** Its one source is a web-accessibility consultancy. Likely passes.
  Confidence: medium, since that source's quote also failed its raw-text check.
- **A regulatory requirements register, sourced to ISO 27001 control 5.31.** ISO 27001 governs technology
  security broadly, not software product work specifically. No software-team user of the register is named
  on disk. Contestable both ways. Confidence: low.
- **The Behavioural Insights Team's TEST "Target" phase.** No source on disk ties this method to a
  software, product or UX team. Likely fails. Confidence: low, since the Behavioural Insights Team's own
  primary documents were never read in this sweep.

## More Information

- The admission test this record adds a fifth check to: [ADR 0030](0030-templating-scope-markdown-documents.md).
- How many sources the existing tests need: [ADR 0048](0048-one-named-source-clears-the-admission-test.md).
- The phase test this record does not change: [ADR 0077](0077-define-ends-with-a-chosen-concept.md).
- The written-form coverage this record does not change: [ADR 0078](0078-maps-canvases-and-session-records-are-templatable-through-their-written-form.md).
- Why admission and build order are different questions: [ADR 0041](0041-maintainer-preference-sets-the-build-order.md).
- The procedure this record follows for an unwritten rule: `docs/internal/decision-procedures.md` section 5.
- The re-score that surfaced the gap: PR #300 (the Define re-score).
- Heap, "Save Time and Get Aligned With a Design Brief," cited for the `design-brief` application above:
  <https://www.heap.io/blog/save-time-and-get-aligned-with-a-design-brief>. ADR 0077's own source list already
  carries this URL.
