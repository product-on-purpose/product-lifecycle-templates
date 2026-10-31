# lean-ux-canvas: history

Change log for the `lean-ux-canvas` bundle. Each entry records what changed and why, so a reader can tell a
correction from a preference.

## 0.1.0 - 2026-10-30

**Initial release.** Researched 2026-10-30 across six dimensions: origins, structure, practice, debates,
relationships and the gap question. [`lean-ux-canvas_research-log.md`](lean-ux-canvas_research-log.md)
records **19 sources, and all 19 are fetched-and-verified** (11 primary, 7 practitioner, 1 vendor), and
**168 Quotable lines**, 139 from the 18 web entries and 29 from the book. The build rests on
[ADR 0082](../../docs/internal/decisions/0082-lean-ux-canvas-joins-discovery-docs-at-discover.md) (the Lean
UX Canvas joins discovery-docs at discover), the family contract at
[`discovery-docs.md`](../../docs/internal/contracts/discovery-docs.md) version 0.6.0, and the spec in
[`tier2-specs.md`](../../docs/internal/tier2-specs.md), "discovery-docs (sixth member, at discover): the
Lean UX Canvas." The maintainer ruled all seven of that spec's choices as recommended on 2026-10-30. This
bundle is issue #330 (bundle: lean-ux-canvas) and adds catalog entry 211.

### The sixth `discovery-docs` member, and the second to take the family's cadence exception

The canvas frames one initiative's business problem, outcomes, users, user outcomes and candidate
solutions, turns those links into hypotheses, and names the single most important thing to learn right now
and the least work that would learn it, all before anyone commits to building. That fits the family's
membership sentence as written. It also earns the family's second bounded cadence exception: it may be
revised while one initiative's experiments run, because Gothelf's own how-to page closes the loop after
Box 8 by asking Box 7's question again, and it is finished when the team commits, changes course or stops,
never becoming a standing instrument. `design-brief` holds the family's first exception; this is the
second, and the two are independent.

### One size, because no source splits a short canvas from a long one

`sizes_available: [lean]`. Gothelf has published the canvas three times, in 2016, 2019 and 2024, each
as one canvas. This research found no source that offers a shorter or longer sectioned form of the same
type, so the single-size call rests on an absence across 19 sources rather than on the family contract's
permission alone.

### The name is kept, and the 2024 rename is carried as an alias

The canvas was renamed the Lean Product Canvas on 2024-11-04: "The canvas is now called the Lean Product
Canvas." The bundle keeps `id: lean-ux-canvas` and the title Lean UX Canvas, by the maintainer's ruling,
because the older name is the one issue #330 and the third edition of the Lean UX book use, and at least
one third-party guide written after the rename still leads with it. "Lean Product Canvas" ships as the sole alias, so a reader searching the
newer name still finds the bundle. The 2024 PDF's own three heading and three prompt changes (Box 1, Box 4
and Box 8 reworded; Box 2, Box 4 and Box 7 given new prompts) are recorded in the companion against the 2019
wording, rather than silently treated as a different document.

### A ninth section this library adds, and says so

The template carries nine sections: the eight boxes in Gothelf's own numbering, Business Problem through
The Least Work to Learn It, plus a ninth, Revisions and What Takes Over. Its dated half is sourced: the 2024
canvas's own header carries a date and an iteration field, and two guides built on the canvas treat it as
revisited as the team learns. Its successor half, the document that takes over, is the library's own
POSITION, built on the cadence exception and on Atomic Object's account of the canvas being abandoned for
other tools once a project matured. The companion, the guide and the template say which half is which.

### Corrections the build made to its own research before drafting

- **A misquote in the spec, corrected.** The spec's own account of Gothelf's walkthrough said the Lean UX
  book is "structured around" the canvas. The walkthrough instead says the third edition is "organized
  around" the canvas and calls it "the backbone of the book"; "structured around" is the walkthrough's
  phrase for a separate self-paced video class. The meaning the spec wanted stands; the quoted wording did
  not, and this log carries the corrected text.
- **A misattribution, corrected.** One research pass credited the Lean UX book with calling the canvas a
  "living document." The book uses that phrase for proto-personas, not the canvas; Atomic Object's post is
  the source that calls the canvas itself a living document. No claim in the bundle rests on the
  misattributed phrase.
- **IdeaScale's page, read in error, withdrawn.** One agent read a vendor page on ideascale.com before
  checking the site's terms, which forbid automated access. The main loop found the clause after the
  research stage, removed the entry, and nothing quoted from it appears anywhere in the bundle; the
  withdrawal is logged in the research log's closing section.
- **Quotations checked against raw text, three dropped and 24 added.** An automated recheck read 122
  quotations against cached raw pages: 110 passed strictly, 3 passed as extraction artifacts, and 9 failed.
  The log generator then kept only quotations that pass against the cached page. It split three list-shaped
  lines into their passing parts and dropped three outright: two paraphrases of Gothelf's walkthrough and
  one bracketed paraphrase of the Hypothesis Prioritization Canvas page. The main loop added 24 lines from
  the same cached pages, eight of them to the walkthrough entry, which had been left with none.

### Boundaries named directly, including with a type not yet built

The companion and the guide each state what this document is not: not a `problem-statement` (which names no
solution; this canvas names candidates in Box 5), not an `experiment-design-doc` (which plans one test in
detail; this canvas only picks the next hypothesis and sketches the least work), not a `design-brief` (which
hands over one chosen concept; this canvas has chosen none), not a `product-vision` (years, not one
initiative), not a `user-persona` (a line pointing to a persona, not the researched portrait), and not Ash
Maurya's Lean Canvas, which models a whole business and asks nothing about revenue or cost. That type is
accepted as a future `strategy-docs` member
([ADR 0083](../../docs/internal/decisions/0083-lean-canvas-joins-strategy-docs-as-a-seventh-member.md)) but
not yet built, so `related_templates` carries it as `future:lean-canvas`. Where the canvas sits relative to
`experiment-design-doc` and `design-brief` in the chain is this library's own POSITION; no source states
that sequence.

### No pm-skills pairing

`pairs_with: []`. `tools/known-skills.txt` was checked directly on 2026-10-30 and carries no skill ID that
addresses the canvas, matching the spec's own finding. This is consistent with `user-persona`,
`project-brief` and `design-brief`, the family's other unpaired members.

### The example chains the family's shared scenario backward, into the roadmap's own gap

[`lean-ux-canvas_example.md`](lean-ux-canvas_example.md) frames the FY26 product roadmap's Later-lane item,
Collaborative analysis, "Nobody has shaped," dated after the roadmap and before the roadmap's 15 October
2026 review trigger, so it carries no citation to a document that postdates it. Box 2's outcome ladders to
the product strategy's own measure, the share of new accounts that build a second view within 14 days from
a 31 percent baseline to 50 percent. Box 3 names the Recurring Analyst, by that name, as the persona and the
strategy example both require. Its Hypotheses table does not name Saved Views sharing as a new solution,
because the internal announcement example already tells the Reporting squad it can share a saved view with
a teammate today; introducing it here as new would contradict a document this one is chained to. All
figures in the example are illustrative and labelled so.
