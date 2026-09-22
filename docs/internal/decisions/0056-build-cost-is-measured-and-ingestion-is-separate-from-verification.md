---
status: accepted
date: 2026-09-22
decision-makers: [jprisant]
consulted: [claude]
---

# Build cost is measured from harness transcripts, and ingestion is deliberately separate from verification

## TL;DR

- **Decision.** Per-bundle build cost is **measured**, not estimated, and lives in a new top-level
  `bundle-builds/` directory: one report per bundle per `template_version`, as a readable `.md` and a
  machine-readable `.json`, with a generated `INDEX.md`. It is produced by
  [`tools/gen-bundle-build-report.py`](../../../tools/gen-bundle-build-report.py) from the Claude Code
  harness transcripts, which already carry a full `usage` block on every subagent turn.
- **The structural decision, and the one a future reader will question:** `--ingest` and `--check` are
  **separate commands** and the CI gate **cannot verify the reports it gates**. That looks wrong from
  outside and is deliberate. Transcripts are machine-local, absent on the runner, and pruned
  eventually; a measurement whose source can disappear has to be captured at the moment it is true.
  The committed JSON is the source of truth thereafter.
- **Why now:** two documents stated a per-bundle cost, disagreed with each other, and neither cited a
  measurement. Measured, both were wrong by 20 to 30 times. In a library that will not call a single
  bundle proven without evidence, the number used to decide whether a bundle was worth building was
  the least evidenced number in the repository.
- **What it deliberately does not do:** rank quality, divide the orchestrator's own spend per bundle,
  or record reasoning effort. Each is stated in every report rather than left for a reader to assume.

## Context and Problem Statement

[ADR 0041 (maintainer preference sets the build order)](0041-maintainer-preference-sets-the-build-order.md)
made build order a judgment about what is worth the spend, because the pull queue has never produced a
ranking input. That judgment needs a price. Two documents supplied one and they disagreed:

| Source | Claim |
|---|---|
| `docs/internal/bundle-pipeline.md` line 20 | "Per-bundle cost is roughly 0.6-1M tokens" |
| `.claude/commands/build-bundle.md` line 120 | "Roughly 700K-1M tokens per bundle" |

Neither cited a measurement. Both were written from impression. They also disagreed on where the cost
goes: the runbook said it was "dominated by research fan-out and the four-lens review".

**The measurement was always available and nothing had ever read it.** The harness writes, per session:
the orchestrator's own transcript; a `journal.jsonl` per workflow run mapping each subagent to its
label, phase and the file it wrote; a per-agent transcript carrying model and `usage` on every turn;
and a per-agent sidecar carrying the requested model tier. This is the same failure shape recorded on
2026-09-21 for the MCP config: a fact sitting in plain view that no check and no reader ever touched.

### What the measurement actually said

Measured across the two builds captured end to end:

| | |
|---|---|
| `test-summary-report` | 24,650,553 weighted token-equivalents, 15 agents, 3 runs |
| `spike-report` | 20,743,317 weighted token-equivalents, 15 agents, 3 runs |
| By stage, `test-summary-report` | draft 10,206,549; research 9,032,973; lens 5,411,031 |

So the estimates were low by **20 to 30 times**, and the runbook's claim about where the cost goes was
wrong in a way that matters: **drafting is the largest single stage** and the four-lens review is under
half of research, not co-dominant with it.

"Weighted" means input x1.0, cache write x1.25, cache read x0.1, output x5.0. The weighting is not
cosmetic: cache reads are typically 90 percent or more of raw token events and roughly a tenth of the
cost, so a raw sum overstates a build by about an order of magnitude in the opposite direction from the
estimates it replaces.

## Decision Drivers

* **A number this library states about itself must be regenerable.** DF-5 (prose counts drift) has
  recurred nine or more times, and the fix that works is a generated artifact plus a gate, never a
  more careful author.
* **The source data is outside the repository and is not durable.** This is the constraint that shapes
  everything else. Transcripts live under `~/.claude/projects/` on the machine that ran the build.
* **A gate must not claim more than it checks.** The precedent is the 2026-09-21 finding that the MCP
  self-test degraded to a skip and printed OK, so CI had never verified the server starts.
* **Cost is not quality.** The library's whole posture is refusing to let a measurable proxy stand in
  for an unmeasured claim, and spend is the most seductive proxy available.

## Considered Options

* **A. A ninth file inside each bundle directory** (`<type>_build-report.md`). Rejected: the eight-file
  contract is stated in `templates/methodology.md` and enforced per family, so a ninth role would mean
  amending all nine family contracts for an artifact that is not part of the bundle's teaching.
* **B. A section inside `<type>_history.md`.** Rejected: `_history.md` is hand-authored, and putting
  generated tables inside a hand-authored file is how generated and typed content get confused. It
  also could not hold the machine-readable form.
* **C. Fields on `manifest.json`.** Rejected on the precedent that kept the manifest minimal: per-section
  detail was measured at 4.6x its size and moved to `sections.json` instead, because the selection
  surface should not carry data selection never reads. Build cost is exactly such data.
* **D. A new top-level `bundle-builds/` directory, generated, gated, with ingestion separate from
  verification.** Chosen.

## Decision Outcome

**Chosen: option D.**

### The layout

```
bundle-builds/
  README.md      hand-authored; the only hand-authored file here
  INDEX.md       generated list view, gated by --check
  reports/       <type>_v<version>.md  and  <type>_v<version>.json
```

Reports are keyed by bundle **and `template_version`**, which is the key `<type>_history.md` already
uses, so a rebuild at a new version lands beside its predecessor rather than overwriting the record of
what the previous one cost.

### The split, which is the part that looks wrong from outside

| Command | Reads | Writes | Runs where |
|---|---|---|---|
| `--ingest` | harness transcripts | `reports/*.json`, `reports/*.md`, `INDEX.md` | only on the machine that ran the build |
| (no flag) | committed reports | `INDEX.md` | anywhere |
| `--check` | committed reports | nothing | CI |

**The CI gate checks that `INDEX.md` matches the committed reports. It does not and cannot check the
reports against the transcripts they came from.** Stating that limit in the tool's own output was
preferred over a gate that implies a verification it never performs.

The consequence accepted with this: **a report is trusted because it was generated once, not because
it can be re-derived.** That is weaker than every other generated artifact in this repository, and it
is the honest position given where the data lives. `--ingest` therefore belongs in Phase 6 of the
build runbook, at the end of a build on the machine that ran it, not as a periodic chore.

### The label change that makes attribution exact

Every workflow agent label now carries its bundle type: `test-summary-report/draft:companion` rather
than `draft:companion`. Without it, attribution had to be inferred from each agent's own prompt, which
worked for drafting agents (they write a file under `templates/<type>/`) and failed for the research
and review fan-outs, which write nothing and name sibling types in the same breath as their own. One
research run was billed to the sibling it was comparing against. The prefix costs nothing at runtime.

### Honesty fields, carried in every report

Because 20 of the 22 backfilled reports predate that label change, two fields are structural rather
than decorative:

- **`scope`**: `whole build` when agents from both the research and drafting fan-outs were found;
  **`floor`** otherwise, meaning "at least this much".
- **`attribution_confidence`**: `high` (label or written file), `medium` (run-level consensus across
  agent prompts), `mixed` (reliable signals disagreed).

A report that cannot say which of these it is would be worth less than no report.

### Consequences

- **Good.** The cost input to [ADR 0041](0041-maintainer-preference-sets-the-build-order.md)'s build
  order is now evidence. The stage breakdown points the next cost reduction at drafting, which nobody
  was looking at.
- **Good.** Two stale estimates are replaced, and the replacement regenerates.
- **Accepted cost.** The backfill has a permanent hole: 20 reports are floors and will never improve,
  because transcripts cannot be relabelled retrospectively.
- **Accepted cost.** CI verifies an index, not a measurement. See above.
- **Watch.** Reasoning effort is recorded nowhere in the transcript tree. If it ever needs measuring,
  the fix is the one that fixed attribution: put it in the label.
- **Open at the time of writing.** `build-bundle.js` pins `model: 'sonnet'` on all five drafting
  agents, yet the measured 2026-09-14 build shows those agents resolving to `claude-opus-5` while
  research and lens, pinned identically, resolved to sonnet. Their sidecars carry no model key at all.
  Not established, and recorded here rather than left to be rediscovered.

## More Information

- [`bundle-builds/README.md`](../../../bundle-builds/README.md) states what the numbers are and are not.
- [`bundle-builds/INDEX.md`](../../../bundle-builds/INDEX.md) is the list view.
- [`docs/internal/bundle-pipeline.md`](../bundle-pipeline.md) Phase 6 runs the ingest.
- [ADR 0041](0041-maintainer-preference-sets-the-build-order.md) is the decision this one supplies a
  price for. Nothing here supersedes it.
