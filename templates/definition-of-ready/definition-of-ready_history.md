# definition-of-ready: history

Change log for the `definition-of-ready` bundle. Each entry records what changed and why, so a reader can
tell a correction from a preference.

## 0.1.0 - 2026-09-23

**Initial release.** Researched 2026-09-23 in two passes: an admission sweep run while the spec was
written, then the build's six-dimension fan-out (origins and admission, contents and structure, the
dispute over whether to keep one at all, boundaries against neighboring types, practice and failure, and
the standing-gap question). [`definition-of-ready_research-log.md`](definition-of-ready_research-log.md)
records **33 sources**: **30 fetched-and-verified**, two url-confirmed-not-read, and one not-retrieved.
Only fetched-and-verified sources are quoted anywhere in this bundle, and every quotation was checked
against the source's raw text rather than a retrieval tool's summary.

**The fourth member of the `standing-standards` family**, and its `classification` was argued rather than
assumed. [ADR 0058 (definition-of-ready joins standing-standards as a
foundation)](../../docs/internal/decisions/0058-definition-of-ready-joins-standing-standards-as-a-foundation.md)
tests the type against the contract's own cut, "is it a standard you judge against, or an instrument you
execute", and finds it matches all three of the contract's `foundation` markers and none of `tool`'s: it
is a standard the team is judged against, agreed deliberately by the team that applies it, with its
authority coming from having been agreed rather than from being correct in the moment. Being consulted at
a recurring moment (refinement, sprint planning) was considered and rejected as the deciding fact, because
that is the family's **membership** falsifier, not its classification test.

### Neither canonical standard names the type, and the bundle says so throughout

The 2020 Scrum Guide never uses the phrase "Definition of Ready", and the Scaled Agile Framework's own
glossary defines a Definition of Done with no entry for a Definition of Ready. Scrum Alliance states the
asymmetry directly: a Definition of Done is part of Scrum, a Definition of Ready is an external and
optional tool. This family's contract names its citation hazard as "folklore presented as standard", and
"a Definition of Ready is part of Scrum" is exactly that folklore; the companion, guide, and template all
check the Guide directly rather than repeating what circulates about it.

### Two lineages traced back to their earliest published source, and they never cite each other

The earliest verified published instance of the term is Richard Kronfält's 2008 blog post, "Ready-ready:
the Definition of Ready for User Stories going into sprint planning", which names the resulting state
directly. A second, separate lineage was traced independently. Neither origin is canonical, because there
is no Guide text to compare across editions the way a Definition of Done's 2020 rewrite could be.

### Whether to keep one at all is carried as a live, three-sided argument, not resolved

The research found the field genuinely split: abolition, keeping a small guideline-based version, and
leaving the decision to the team's own judgment. The bundle does not pick a side. The guide's own "When to
use" section states the framing directly: reaching for this template because "a real team has one" gets
the reasoning backward, since even the practitioners who argue for keeping a Definition of Ready also
argue for keeping it small and easy to drop.

### The size call is single-size, on the same evidence direction as the contract's precedent

Unlike `definition-of-done`, whose research found real examples varying by nearly an order of magnitude
and set `sizes_available: [lean, full]` on that variance, no source read for this bundle argues for a
bigger Definition of Ready, and the ones that address its size at all argue for a **smaller** one: a
maturity signal recorded in the research is a Definition of Ready that should be "shrinking over time and
not growing." `sizes_available` is `[lean]` on that evidence. A `full` variant would model the exact
failure the practice is criticized for, so none was built.

### The review trigger fires in both directions, and one direction is the library's own contribution

The family contract names `foundation`'s failure mode as being agreed once and never honoured. A
Definition of Ready's documented failure runs the opposite way: being honoured too hard, as a rigid gate.
Mountain Goat Software's warning is that a Definition of Ready requiring work to be "100 percent finished"
before entry "becomes a huge step towards a sequential, stage-gate approach." The build's research located
a second source for the same direction rather than labelling it the library's own unsupported addition:
Big Agile (2025) writes that when a Definition of Ready "blocks more value than it enables, it stops being
a safety rail and becomes a parking brake." The template's Review Trigger section is written to catch
failure in both directions.

### `pairs_with: []`, checked and rejected rather than left empty by default

The one pm-skills candidate considered, `iterate-refinement-notes`, was checked against
`tools/known-skills.txt` and never mentions a Definition of Ready. No other candidate skill names the type
either. `pairs_with` is declared empty because that was verified, not assumed.

### Sources not retrieved are quarantined

Two sources are recorded as url-confirmed-not-read and one as not-retrieved. Nothing in this bundle rests
on them, and no figure attributed to them appears as fact.

### No `default_format` key is declared

This bundle found one shape for the document type and carries no format key, consistent with the majority
of members built before the format-axis backfill.
