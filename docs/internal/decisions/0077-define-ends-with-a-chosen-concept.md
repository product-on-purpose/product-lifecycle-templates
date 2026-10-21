---
status: accepted
date: 2026-10-17
decision-makers: [jprisant]
consulted: [claude]
---

# The `define` phase ends with a chosen concept, never a specification

## TL;DR

- **Decision.** `define` now holds a document that converges on one chosen problem and, where the team has
  got that far, on one concept chosen for design. A `define` document never specifies how that concept works
  or what it must do. This record supersedes
  [ADR 0068 (the define phase means problem framing)](0068-define-means-problem-framing.md), whose test was
  that a `define` document names no solution.
- **The line that keeps this reading from becoming the declined one: concept yes, specification never.** How
  the solution works stays in `develop`. What it must do, in testable detail, stays in `deliver`. So `prd`,
  `epic`, `user-stories` and `acceptance-criteria` stay where
  [ADR 0020 (adopt the delivery-docs family contract)](0020-adopt-delivery-docs-family-contract.md) put them,
  and ADR 0068's decline of the requirements reading stands.
- **The cost, named.** This library's six phase words come from pm-skills' Triple Diamond
  ([ADR 0003 (phase vocabulary)](0003-phase-vocabulary.md)). As pm-skills documents it, the proposed solution
  approach is a Develop output. From this record on, this library's `define` admits a chosen concept, so the
  seam with pm-skills holds for the spelling of the six values and not for the width of `define`.
- **The contract.** [`discovery-docs`](../contracts/discovery-docs.md) moves to `0.4.0`. Its `define` rule
  changes, and its cadence clause gains one exception, for a document that hands a chosen concept to the
  people who will design it and is revised while that design work runs.
- **What this does not decide.** It does not decide whether `business-case` moves to `define`, which earlier
  candidates return for admission, or whether `define` members need a family of their own. A re-score of the
  three Define sweeps' candidates answers the first two.
  [ADR 0069](0069-problem-statement-joins-discovery-docs.md) already names the trigger for the third.
- **Status:** accepted 2026-10-17. The maintainer ruled the reading on 2026-10-17 and asked for this record and
  the contract change. Every contract amendment stops for the maintainer's read; the maintainer read the
  pull request that carries this record and approved its merge the same day.

## Context and Problem Statement

ADR 0068 reserved `define` for a document that "frames a problem before any solution is chosen". The maintainer
made that call on 2026-10-10. Three Define admission sweeps followed, one on 2026-10-11 and two on 2026-10-16.
Only `problem-statement` cleared both the admission test and the phase test, and
[ADR 0069](0069-problem-statement-joins-discovery-docs.md) admitted it to `discovery-docs`.

**The single result came from three stacked filters, not from the stage itself.**

1. **The sweeps' own written-document test was stricter than the library's scope rule.**
   [ADR 0030 (templating scope)](0030-templating-scope-markdown-documents.md) excludes an artifact whose
   primary form is "visual, executable, or a live data surface". The sweep briefs also excluded boards,
   canvases kept only in a whiteboard tool, workshop exercises, diagrams and slides.
2. **ADR 0068's test kept only problem framing.** Most documents written at the close of Define also set a
   direction, so they failed it.
3. **The `discovery-docs` contract added two clauses.** Its section 2 said a `define` member "names no
   solution, option, project or investment". Its section 1 said every member "is written once for a
   decision".

The maintainer rejected the sweeps' conclusion that Define is mostly an activity rather than a source of
documents, and reopened the reading on 2026-10-17.

**Evidence that arrived after ADR 0068 points toward a chosen concept inside Define.** The Design Council's
2007 report *Eleven lessons: managing design in eleven global brands* studied how eleven companies managed
design. It describes Define as the stage "where findings from the Discover stage are analysed, defined and refined as
problems, and ideas for solutions are pitched and prototyped". It says "The Define stage ends with a clear
definition of the problem(s) and a plan for how to address this through a design-led product or service". It
also reports: "At most of the companies we visited, the Define stage would end with final sign-off of the
concept and approval of work to begin on design and development." Stage-Gate's Stage 2 leads "to a Business
Case, including product/service and project definition, project justification, and the proposed plan for
development", before its Develop stage. Heap describes a design brief whose goal is "to describe,
holistically and at a high level, your proposed design solution(s)".

**The library's own vocabulary source points the other way.** ADR 0003 adopted the six phase values from
pm-skills, and the design spec calls them "the `pm-skills` Triple Diamond axis". pm-skills'
[Triple Diamond workflow page](https://github.com/product-on-purpose/pm-skills/blob/main/_workflows/triple-diamond.md)
gives Define the goal "Frame the problem and form hypotheses". Its Define outputs are a problem statement with
success criteria, a prioritized opportunity tree, testable hypotheses, and an understanding of the job to be
done. It gives Develop the goal "Explore solution approaches", and the first Develop skill it lists is
described as "Document proposed solution approach".

**Two limits on that evidence.** pm-skills' README names a Zendesk article as the Triple Diamond's origin
(`medium.com/zendesk-creative-blog/the-zendesk-triple-diamond-process-fd857a11c179`). That article returned
HTTP 403 to a raw fetch on 2026-10-17 and has not been read. pm-skills' pages are therefore a secondary source,
and its concept page and workflow page also describe the third diamond differently.

So the question this record answers is which reading the library uses. Product-practice sources put a chosen
concept inside Define. The library's vocabulary source puts the proposed solution approach in Develop.

## Decision Drivers

- **A phase value has to mean one thing.** This driver is carried over from ADR 0068 unchanged. A reader
  filtering by `define`, through `manifest.json` or the MCP server's `search_templates`, should get documents
  that share a job.
- **Product practice chooses a concept before it commits design and development effort.** The Eleven Lessons
  report observed this at most of the companies it studied, and Stage-Gate builds it into its Stage 2 output.
- **The line between a concept and a specification has to hold.** Without it, this reading collapses into the
  requirements reading that ADR 0068 declined, and the four delivery bundles would follow.
- **The seam with pm-skills.** ADR 0003's stated consequence was "one vocabulary across the ecosystem". This
  driver weighs against the chosen option, and the record says so.

## Considered Options

1. **Problem framing only.** The status quo under ADR 0068.
2. **Convergence on a direction.** Define frames the problem and hands designers a direction and its
   constraints, and names no solution. It admits the design brief only in the Design Council's sense.
3. **The Triple Diamond reading.** Define frames the problem, sets success criteria, prioritizes
   opportunities and forms testable hypotheses. The proposed solution approach belongs to Develop.
4. **A chosen concept inside Define.** Define ends with a chosen problem and one concept chosen for design,
   and never a specification. Chosen by the maintainer on 2026-10-17.
5. **A chosen concept plus the project go-ahead.** Option 4, plus project authorization, which would make an
   unbuilt `project-charter` a Define candidate.
6. **The requirements reading.** Closed by ADR 0068 and listed here only so a reader sees it was not reopened.

The agent's recommendation moved twice in one session on 2026-10-17: from option 2, to option 4, to "option 3
or option 4". The ruling therefore went to the maintainer with options 3 and 4 named and no recommendation.
The options were then shown as outcomes, meaning the last thing a team writes down before Develop starts under
each reading, and the maintainer chose option 4.

## Decision Outcome

**Chosen: option 4, a chosen concept inside Define.** A `define` document converges on one chosen problem. It
may also record the candidate concepts the team considered, the one it chose for design, and the approval to
begin design work. It never specifies how the solution works, and it never states what the solution must do in
testable detail.

**Why.** It is the maintainer's call, made after the options were shown as outcomes. The product-practice
sources quoted above support it. The design-school sources support a narrower reading, and this record does not
claim they agree: the Design Council's current history page says the Define result "is to create a design brief
which clearly defines the challenge based on these insights", and it places solutions in the next stage. This
library holds that a product team chooses a concept before it commits design and development effort, and the
Eleven Lessons report observed that pattern at most of the companies it visited. That sentence is the
library's POSITION.

### The line between a concept and a specification

| A `define` document may say | It belongs to `develop` | It belongs to `deliver` |
|---|---|---|
| Which problem the team chose, for whom, and how success will be judged | How the chosen concept works: its design, architecture and feasibility | What the solution must do, in testable detail |
| Which candidate concepts the team weighed, at concept level | Comparisons between designed alternatives, and the decisions they lead to | The PRD, the epic, the user stories and the acceptance criteria |
| Which one concept the team chose for design, and that design work may begin | Spikes, trade studies and architecture decisions | |

A concept names the kind of answer the team will pursue. A specification says how that answer works or what it
must do. The first may appear in `define`. The second never does.

### What the decision costs, stated rather than smoothed over

1. **It departs from the vocabulary source's meaning of `define`.** As pm-skills documents the Triple Diamond,
   the proposed solution approach is a Develop output, and this library's `define` now admits a chosen concept.
   Matching on spelling is unaffected, so `pairs_with` values and phase filters still resolve without a
   translation layer. A reader who moves between the two repositories must not assume `define` has the same
   width in both. ADR 0003 carries a dated note that says so.
2. **The Triple Diamond's primary source has not been read.** Every claim here about the Triple Diamond rests
   on pm-skills' pages. If the Zendesk article, once read, places a chosen concept inside Define, the first
   cost shrinks. If it does not, the first cost stands as stated. *(2026-10-20: the maintainer supplied the
   article and its linked milestones page as PDFs, and both were read. Zendesk names no Define phase. Its
   Problem Definition milestone summarizes findings "in a solution-agnostic way", and the concept is chosen and
   tested afterwards, still inside Zendesk's Discovery phase and before Development. The article does not place
   a chosen concept inside Define, so the first cost stands as stated. The read is held locally, with the
   other evidence for this record.)*
3. **The contract's cadence clause takes its first exception.** `discovery-docs` section 1 said every member
   "is written once for a decision, and is finished when that decision is made". A document that hands a
   chosen concept to the people who will design it is revised while that work runs. Design Society research
   says the design brief "should be used as a validation tool periodically throughout the project". Peter
   Phillips's *Creating the Perfect Design Brief* (Allworth Press, 2004) says "The design brief is also a
   project-tracking tool." The exception is bounded: such a document is finished when the design work it
   hands off is done, and it never becomes a standing instrument.
4. **`business-case` may move, and this record does not move it.** Stage-Gate places a business case with
   product definition inside it before its Develop stage. Under this reading, `business-case` is a candidate
   for `define`. Until the re-score rules on it, the contract keeps "investment" out of `define`, so
   `business-case` stays at `discover`. If the re-score moves it, a separate record moves a built bundle and
   amends that clause.
5. **It widens a surface this library has not proven.** The library's efficacy runs found that documents
   written with these templates score no better than a strong generic-prompt control on decision-usefulness
   criteria drawn from neither the template nor its guide. Every bundle this reading admits joins that
   unproven surface.

### Consequences

- **ADR 0068 is superseded.** Its status becomes "superseded by ADR-0077". It also carries a dated correction
  for a factual error, below, as [ADR 0011](0011-madr-v4-at-docs-internal-decisions.md) requires for an error
  of fact.
- **ADR 0069 is superseded on one point and left unedited.** Its decision stands: `problem-statement` is a
  `discovery-docs` member at `phase: define`. Only its quotation of the `define` rule ("names no solution,
  option, project or investment") is out of date. This follows the precedent of
  [ADR 0055](0055-retire-the-zero-fills-disclosure.md), which left the records it superseded on one point
  unedited.
- **The contract moves to `0.4.0`.** The header's Axis line, the section 1 cadence clause, the section 2 phase
  row, the section 6 enforcement sentence and the change note change in the same edit. The new `define` rule,
  an OBLIGATION of this library's own, reads: a member declares `define` when its whole document converges on
  one chosen problem; it may also name the candidate concepts weighed, the one concept chosen for design, and
  the scope, time line and budget of handing it to the people who will design it; it never specifies how the
  solution works or what it must do, it decides no investment, and it is not the record that authorizes a
  project.
- **Check K does not change.** It still gates `["discover", "define"]` for `discovery-docs`. Which value a
  member should declare remains a review obligation against section 2, as it has been since ADR 0069.
- **No built bundle changes phase in this record.** `problem-statement` stays at `define`, because it frames a
  chosen problem and the new rule admits a document that names no concept. `business-case`, `user-persona` and
  `project-brief` stay at `discover`.
- **ADR 0003 carries a dated note** recording that its seam with pm-skills now holds for spelling, and that
  `define` here is wider than pm-skills' Define.
- **The next step is a re-score, not a build.** The roughly sixty candidates from the three Define sweeps are
  scored again under this reading, from evidence already gathered. That pass decides whether `business-case`
  moves and which candidates return for admission. The design brief
  ([issue #294](https://github.com/product-on-purpose/product-lifecycle-templates/issues/294)) is the first
  Define spec if the re-score confirms it. *(2026-10-20: the re-score ran over 67 candidates and confirmed the
  design brief for an admission sweep at `define`, in the Design Council's sense of a document that defines the
  challenge. `business-case` stays at `discover`, because its job is the investment decision the rule
  excludes. The outcomes are in [`backlog.md`](../backlog.md) section 4.)*
- **The artifact scope the maintainer ruled the same day is a separate decision.** Whether maps, canvases and
  workshop records are templatable is a question for ADR 0030, not for the phase vocabulary, and this record
  does not answer it.

## Correction carried from ADR 0068

ADR 0068 said the 2026-10-11 sweep "found no named written deliverable for the Define stage". That was true of
the pages that sweep read. It was not true of the Design Council's own history page, which the second Define
sweep read on 2026-10-16: "The result is to create a design brief which clearly defines the challenge based on
these insights." The quotation passed a raw-text check in that sweep and again in the third. ADR 0068 carries
the correction in place, dated, with the error named.

## More Information

- The record this supersedes: [ADR 0068](0068-define-means-problem-framing.md).
- The record superseded on one point and left unedited: [ADR 0069](0069-problem-statement-joins-discovery-docs.md).
- The phase vocabulary and its seam with pm-skills: [ADR 0003](0003-phase-vocabulary.md).
- The family contract: [`discovery-docs`](../contracts/discovery-docs.md), `0.4.0`.
- The scope rule the sweeps' test was stricter than: [ADR 0030](0030-templating-scope-markdown-documents.md).
- Sources quoted, each checked against raw text:
  - Design Council, *Eleven lessons: managing design in eleven global brands* (2007),
    <https://www.designcouncil.org.uk/fileadmin/uploads/dc/Documents/ElevenLessons_Design_Council%2520%25282%2529.pdf>.
  - Design Council, "History of the Double Diamond",
    <https://www.designcouncil.org.uk/our-resources/the-double-diamond/history-of-the-double-diamond/>.
  - Stage-Gate International, "Discovery to Launch Process",
    <https://www.stage-gate.com/about/stage-gate-innovation-performance-framework/discovery-to-launch-process/>.
  - Heap, "Save time and get aligned with a design brief",
    <https://www.heap.io/blog/save-time-and-get-aligned-with-a-design-brief>.
  - Design Society, "Design briefs: is there a standard?",
    <https://www.designsociety.org/download-publication/33176/design_briefs_is_there_a_standard>.
  - Peter L. Phillips, *Creating the Perfect Design Brief* (Allworth Press with the Design Management
    Institute, 2004), checked through Open Library's search-inside index.
  - pm-skills, "Triple Diamond" workflow page,
    <https://github.com/product-on-purpose/pm-skills/blob/main/_workflows/triple-diamond.md>, read raw on
    2026-10-17.
- The three Define sweeps are summarised in the [`tier2-specs.md`](../tier2-specs.md) progress notes dated
  2026-10-11, with a dated note added by this record.
