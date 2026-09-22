# Bundle build reports

What it actually cost to build a bundle, measured from the harness transcripts rather than estimated.
[`INDEX.md`](INDEX.md) is the list view; [`reports/`](reports/) holds one report per bundle per
`template_version`, as a readable `.md` and a machine-readable `.json`.

**Everything here is generated** by
[`tools/gen-bundle-build-report.py`](../tools/gen-bundle-build-report.py) and must not be edited by
hand. This file is the only hand-authored page in the directory.

## Why this exists

Two documents in this repository stated a per-bundle build cost, and they disagreed:
`docs/internal/bundle-pipeline.md` said "roughly 0.6-1M tokens" and `.claude/commands/build-bundle.md`
said "roughly 700K-1M". Neither cited a measurement. Both were wrong by more than an order of
magnitude, which nobody could have known, because the number that decides whether a bundle is worth
building was the least evidenced number in a library that refuses to call a single bundle proven
without evidence.

The measurement was always available. The Claude Code harness writes per-agent transcripts with a
full `usage` block on every turn; nothing had ever read them.

## What a number here means

Each report gives five raw counts - fresh input, cache write, cache read, output, and server-side web
search or fetch calls - and one **weighted total** in fresh-input-token-equivalents:

| Component | Weight |
|---|---|
| input | x1.0 |
| cache write | x1.25 |
| cache read | x0.1 |
| output | x5.0 |

The weights are the published Claude ratios and are printed in every report, so that two reports
written months apart stay comparable and a reader can re-weight with their own numbers. **Read the
weighted total, not the raw sum**: cache reads are typically 90 percent or more of the raw token
events and roughly a tenth of the cost, so a raw sum overstates a build by about an order of
magnitude in the opposite direction from the old estimates.

## The two words in the index that carry the caveats

**Scope** answers "is this a whole build?"

- `whole build` - agents from both the research and the drafting fan-outs were found, so the figure
  covers the pipeline.
- `floor` - at least one fan-out is missing from the numbers. Read it as "at least this much". This
  is common for bundles built before the labelling convention, whose research agents wrote no file
  and never named their bundle in a way a machine could recover.

**Confidence** answers "how do we know these agents belong to this bundle?"

- `high` - every run was attributed by a workflow label or by a file the agent wrote under
  `templates/<id>/`. Exact.
- `medium` - at least one run was attributed by run-level consensus: every agent in the run named the
  same bundle in its prompt's subject line. Strong, but not exact. **A research run compares its
  subject against a sibling type, so a consensus attribution can in principle land on the sibling.**
- `mixed` - reliable signals disagreed within a run.

## What these reports deliberately do not measure

- **Reasoning effort.** It is not recorded anywhere in the transcript tree. Only the requested model
  tier is, and that is reported.
- **The orchestrator's own spend.** One session interleaves several bundles and other work, so the
  main loop's tokens cannot honestly be divided per bundle. They are never billed to one here.
- **Anything about quality.** A build that cost more is not a better bundle. These numbers rank
  spend, nothing else. The library's position on what a bundle is worth is unchanged and is stated
  in [`README.md`](../README.md#the-claim-and-what-it-is-worth).

## Why the source data is not in this repository

The transcripts live under `~/.claude/projects/` on the machine that ran the build. They are
machine-local, they are not on the CI runner, and they are pruned eventually. So:

- **Ingestion is local and one-way.** `--ingest` reads transcripts and writes the reports. Once
  written, the committed JSON is the source of truth. A measurement whose source can disappear has to
  be captured at the moment it is true.
- **The gate checks the index against the reports**, never the reports against the transcripts. CI
  cannot re-derive these numbers and does not pretend to.

This is the honest limit of the design, and it is why the report is generated at the end of a build
rather than whenever someone remembers.

## Usage

```bash
python tools/gen-bundle-build-report.py --ingest      # read transcripts, write reports (local only)
python tools/gen-bundle-build-report.py --ingest --dry-run
python tools/gen-bundle-build-report.py               # regenerate INDEX.md from committed reports
python tools/gen-bundle-build-report.py --check       # freshness gate, runs in CI
```

`--ingest` writes a report for every bundle it can attribute, so re-running it after a new build
refreshes the whole directory rather than appending. Reports are keyed by bundle and
`template_version`, which is the same key `<type>_history.md` uses, so a rebuild at a new version
lands beside its predecessor instead of overwriting it.
