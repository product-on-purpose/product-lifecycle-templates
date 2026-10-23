# design-brief: history

Change log for the `design-brief` bundle. Each entry records what changed and why, so a reader can tell a
correction from a preference.

## 0.1.0 - 2026-10-22

**Initial release.** Researched 2026-10-22 across six dimensions covering the canon, section structure,
altitude, practice by software teams, boundaries, and the standing gap question.
[`design-brief_research-log.md`](design-brief_research-log.md) records **32 sources: 30 fetched-and-verified
and 2 confirmed to exist but not read** (Peter Phillips's book and Noric Dilanchian's article, neither of
which carries a quotation), and **228 Quotable lines**, each checked against the source's raw text rather
than against a retrieval tool's summary. The log was built on the third Define sweep (digest dated
2026-10-16), the 2026-10-20 Define re-score (PR #300), and the spec written and accepted the same day as this
release, [ADR 0079](../../docs/internal/decisions/0079-design-brief-joins-discovery-docs-at-define.md)
(design-brief joins discovery-docs at define).

### The fifth `discovery-docs` member, and the second at `define`

The type builds the Design Council's own concept-handoff sense: "The result is to create a design brief
which clearly defines the challenge based on these insights." It hands one chosen problem and the one
concept chosen for design to the people who will design it, before anyone specifies how that concept works,
decides no investment, and authorizes no project. [ADR 0077](../../docs/internal/decisions/0077-define-ends-with-a-chosen-concept.md)
(define ends with a chosen concept) is what made this content legitimate at `phase: define`; the third
Define sweep had tested the type a day before ADR 0077 shipped and found it too thin to build. The
2026-10-20 re-score returned it, at medium confidence, and the maintainer accepted ADR 0079 on 2026-10-22 by
delegation, then confirmed it the same day.

This member also takes the family's one cadence exception: it may be revised while the design work it hands
off runs, because several sources describe it as a document consulted and updated through the project, and
it is still finished when that design work is done rather than becoming a standing instrument. No other
`discovery-docs` member takes this exception.

### The term has no settled meaning, and the bundle's own shape is this library's composition

The canon gives "design brief" at least four senses: a commissioning agreement between client and designer
(the genre's main book, Phillips, and the commonest published sense), a specification, a chosen problem
narrowed to a chosen concept (the Design Council's sense this bundle builds), and, in one software-analytics
source, a document closer to a worked solution. "There is no clear or univocal definition in the literature."
No source read confines a brief to a chosen challenge, a chosen concept and a handoff with none of those
other senses; the research log labels that composition a POSITION rather than a canon finding, and the
companion says so throughout rather than implying the narrow shape is original doctrine.

### Catalog entry 209, not 207

Issue #294 (bundle: design-brief) carried the candidate under catalog entry 207 from 2026-10-16. By
2026-10-22, PR #305 had already taken 207 for the opportunity statement and 208 for Cagan's Product
Opportunity Assessment, so this bundle lands at catalog entry 209.

### Two sizes, by the maintainer's ruling, against the spec's own single-size recommendation

The spec argued for one size, `[lean]`: no source read splits a short brief from a long one, the long form
sources do describe is the commissioning agreement the `define` rule bars, and the slice the contract does
permit, the handoff's own scope, time line and budget, appears in no source at that scope. The maintainer
ruled on 2026-10-22 to ship two sizes regardless, `sizes_available: [lean, full]`, `default_size: lean`, on
the same ground used for `problem-statement` against that bundle's own lean-only finding. Every full-only
section cites a source or carries the POSITION label rather than resting on the family contract alone:

- **Constraints on the Design** rests on Kuse's "the constraints that shape the solution" and Heap's "the
  constraints within which it exists"; the kinds of limit a reader might expect rest on a source this
  research could not retrieve, so the section stands at low confidence.
- **Open Questions for Design** rests on a reading of Heap's own design-brief template that this log could
  not raw-check, so it stands at medium-low confidence.
- **The Handoff's Scope, Time Line and Budget** has no source that scopes a time line or a budget to the
  handoff alone; the section is the library's own POSITION, at low confidence.

The lean variant's four sections, The Challenge, Who It Is For and What We Learned, The Chosen Concept, and
The Handoff, are a strict ordered subset of the full variant's seven, unchanged in name and order, per
contract section 3.2.

### What stays out, and why

The Chosen Concept names the candidates weighed and the one chosen, at concept level only; no source
publishes a candidates list as a brief section, so that part is also POSITION. Nothing in any section names
how the concept works, sets a cost or a benefit against an alternative, or requests authority to start a
project: naming any of those would break the `define`-phase rule this family enforces. The Shape Up pitch
(catalog entry 45) was weighed and kept out at medium-low confidence: a pitch arrives shaped and exists to
commit a bet at a betting table, where a design brief hands a concept to designers without committing one.

### Boundaries named directly rather than left for a reader to find

The companion's Relationships section states what this bundle is not: not `problem-statement` (which chooses
the problem; this bundle carries that choice forward with a concept), not `project-brief` (which asks for
authority to proceed; this bundle names a concept and asks for none), not `business-case` (which decides an
investment; this bundle decides none), not `product-vision` (a standing document; this bundle finishes when
the handoff's design work is done), and not the `prd` (which states testable requirements for how the concept
works; this bundle carries none). It is also not a creative brief or a Design Sprint brief, for which no
catalog row exists.

### No pm-skills pairing

`pairs_with: []`. pm-skills ships no design-brief skill; `tools/known-skills.txt` was checked directly and
carries no matching ID. That is consistent with this library's own position that it never assumes pm-skills
is installed, and it matches `user-persona` and `project-brief`, the family's other two members with no
pairing.

### The example chains backward in the family's shared scenario

[`design-brief_example.md`](design-brief_example.md) is dated 2026-06-01, an Acme Analytics brief that hands
the Saved Views concept to the people who will design it, and that:

- follows [user-persona](../user-persona/user-persona_example.md)'s Recurring Analyst, dated 2026-01-05,
  well before this brief;
- follows the 2026-05 Reporting friction study that surfaces the re-filtering problem this brief frames;
- precedes [prd](../prd/prd_example.md)'s Saved Views PRD, dated 2026-06-12, eleven days after this brief,
  which later specifies how the chosen concept works. This brief names no screen, button or flow, and cites
  no later Saved Views document as already existing, consistent with the family's chronology obligation that
  a discovery document is written before the documents it leads to.
