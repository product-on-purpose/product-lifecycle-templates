---
status: accepted
date: 2026-07-13
decision-makers: [jprisant, claude]
---

# Adopt MADR v4, locate records at docs/internal/decisions/, and correct rather than supersede transcription errors

## Context and Problem Statement

Milestone M0 (the credibility floor) closed audit finding F-03 (no decision records) by creating a decision-record directory. It created `docs/decisions/`, with a bespoke plain-text header (`Status:` / `Date:` / `Deciders:` lines) and date-prefixed filenames (`20260629-variant-model.md`).

Every part of that was wrong, and wrong in a specific way: it invented a convention that the organization had already settled, and it landed on the one path the organization's own tooling explicitly forbids.

The `jp-init-project` skill states the rule directly:

> Decisions live at `docs/internal/decisions/` - never at `docs/decisions/`, never at per-agent `DECISIONS.md`.

The jp-library's `madr-vs-decisions.md` records the supersession that produced that rule, dated 2026-04-12:

> Directory location finalized as `docs/internal/decisions/` (superseding an earlier `docs/decisions/` choice). Rationale: group decision records with other internal development docs (backlog, efforts), keep the repo root clean for public-facing files.

Sibling repos confirm it in practice: `agent-config-toolkit` and `thinking-framework-skills` both use `docs/internal/decisions/` with MADR v4.

A second question surfaced during the conversion, and it is the more interesting one. Record [0003 (phase vocabulary)](0003-phase-vocabulary.md) was transcribed with a factual error: it claimed the pm-skills phase enum has eight values, "plus `foundation` and `tool`", on the strength of a verification that had read exactly one skill file. pm-skills actually carries a two-axis taxonomy (six `phase:` values, plus a separate `classification:` axis for the 86 skills that have no phase at all). MADR treats accepted records as immutable. So: supersede 0003, or correct it in place?

## Decision Drivers

- **Ecosystem coherence is a stated vision claim of this repo**, not a nicety. A library whose pitch is "same conventions as its siblings" cannot invent its own decision-record format.
- **Tooling.** MADR v4 has real tooling (adr-tools, Log4brains, adr-manager, adr-log). A bespoke format has none.
- **A public repo root should stay clean.** This library is going public; `docs/decisions/` at the root competes with the product for a reader's attention, which is the exact rationale the org recorded in 2026-04-12.
- **Immutability must mean something,** but it must not become a mechanism for laundering a false statement into permanence.

## Considered Options

* **Option A:** Adopt the org standard wholesale. MADR v4 format, `docs/internal/decisions/`, `NNNN-kebab` filenames, YAML frontmatter, README instead of TEMPLATE.
* **Option B:** Keep the bespoke format and `docs/decisions/`, on the grounds that the records already existed and churn is a cost.
* **Option C:** Adopt MADR v4 format but keep the records at `docs/decisions/`, since that path is shorter and more discoverable to an outside reader.

## Decision Outcome

Chosen option: **A**, wholesale.

Option B is untenable: the cost of churn was one afternoon, and the cost of divergence is permanent. Option C is the tempting one, and it is wrong for a reason worth stating. `docs/decisions/` is not merely a different path; it is a path the organization considered, chose, and then **explicitly superseded**. Re-adopting it here would mean this repo silently re-litigating a decision another repo already made, which is the precise failure mode the whole practice of decision records exists to prevent.

**On correction versus supersession (the 0003 question): correct in place, and name the error.**

Superseding a record asserts that *the decision changed*. In 0003, the decision never changed. It was, and remains, "use lowercase phase values matching pm-skills." What was defective was the transcription's claim about *what those values are*. Issuing a superseding ADR would misrepresent the history: a future reader would conclude the project once believed something different about phase casing, which it never did.

So 0003 keeps a dated **Correction** section that names the error, states what is actually true, and explains how the false claim got in (a "verification" that sampled one file and generalized). The version history shows exactly what was believed and when it was fixed, which is what MADR's immutability is actually protecting. A record that silently rewrites itself is worth less than one that shows its scars.

The line, stated so it can be applied without re-deriving it: **a factual error in a record gets corrected in place, with the correction dated and the error named. A change in the decision itself gets a new number.**

### Consequences

* Good: the repo now matches the org standard exactly, so `jp-init-project`, any ADR tooling, and any agent that knows the convention will find the records where they expect them, in the format they expect.
* Good: the repo root stays clean for the product, which matters more now that the library is going public.
* Good: `decision-makers` is a structured list, so it is honest about the fact that records 0009, 0010, and this one were co-designed with an agent rather than authored by a human alone. The bespoke `Deciders:` line could not express that.
* Accepted cost: all ten existing records were renamed and rewritten, and cross-references across 17 files had to be updated. Paid once.
* **This record exists because it was missing.** The convention change was originally made and recorded only in a commit message and a directory README, which is exactly the gap (audit finding F-03, no decision records) that milestone M0 set out to close. Changing the decision-record convention without writing a decision record is the kind of irony that should be written down rather than quietly fixed.

## More Information

The correction to 0003 also opened a live question, tracked as **TX-1** in `STATE.md`: pm-skills needs a second taxonomy axis because roughly half its skills carry no lifecycle phase, and this library has never asked whether it needs the same. TX-1 blocks roadmap WP-21 (the metadata schema), because `phase` must not become a required enum before it is settled.
