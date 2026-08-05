---
name: build-bundle
description: Build one governed template bundle for this library end to end, from research fan-out through the four-lens review to a merged PR. Use when adding a new document type from the build backlog, when asked to "build the <type> bundle", "do the next bundle", or "process through the remaining bundles". Maintainer-internal; it builds this repository, it is not shipped to library users.
metadata:
  version: 0.1.0
  updated: 2026-08-03
  tier: advanced
  audience: advanced
  category: governance
  agent-targets: [claude]
  status: active
---

# Build one bundle

You are building one bundle for `product-lifecycle-templates`: eight files, gate-green, merged.

**Read these two and follow them. Do not restate them, and do not re-derive what they settle.**

| File | What it settles |
|---|---|
| [`docs/internal/bundle-pipeline.md`](../../../docs/internal/bundle-pipeline.md) | The six-phase runbook, the gotchas, the check E snippet, model routing |
| [`docs/internal/review-standards.md`](../../../docs/internal/review-standards.md) | What CI already proves, the seven defect classes it cannot, the standards, the lens scoping |

Then read the type's spec in [`buildout-specs.md`](../../../docs/internal/buildout-specs.md) and its family contract in
`docs/internal/contracts/<family>.md`. That is your whole reading list.

## Before you start

- `main` clean, zero open PRs, `git pull`.
- The type is on the build backlog and its family contract exists. If the contract does not exist,
  **stop**: contracts are drafted then read by the maintainer, never self-approved.
- The catalog entry exists. A type with no catalog entry has not passed ADR 0030's admission test.

## The arc

**Phase 0-2, research.** Fan out parallel sonnet agents over the type's research dimensions, synthesize
one research log. Honest retrieval is not negotiable: three tokens, and only `fetched-and-verified` may be
quoted. See the runbook.

**Phase 3, draft.** Run `{stage:"draft", type, family}`. Seven files in dependency order: companion ->
both templates -> guide -> example -> meta and history, because each is built from the one before.

**Each stage writes its file and returns only a summary.** That is the point, not an implementation
detail: a stage returning its 600 lines through the schema would push the whole bundle through your
context and save nothing. One agent writes BOTH templates, because the lean-subset-of-full nesting rule
is the easiest thing here to get wrong and a split would break it.

**Phase 3.5, machine pre-read.** Two report-only lints, seconds each. Their output aims phase 4.

```
python tools/lint-number-provenance.py <type>
python tools/lint-unsourced-confidence.py <type> --uncited
```

**Phase 4-5, review and apply.** Four sonnet lenses, each reading only its own files per the brief's lens
table. **Every finding is a claim: verify it against the source before applying.** The review reliably
finds real defects and occasionally proposes a fix that is wrong.

**Phase 6, gate and land.** `git add` **before** the link gate (it skips untracked files and gives a false
green). Then the gate, manifest, links, README and STATE updates, PR, CI, merge.

## Source ownership, and why it is a rule

Parallel research agents converge on the same canonical sources. Left alone, five agents each fetch and
each *read* the field's founding paper, and the library pays for that page five times over.

`tools/source-cache.py` fixes the network cost: one fetch per bundle, shared. It does **not** fix the
context cost, because a cache hit still returns a body that an agent then reads.

So each dimension **owns** sources, and ownership is declared, not assumed:

1. Every research agent checks `python tools/source-cache.py get <url>` before any fetch. Exit `0` hit,
   `1` miss, `2` stale (older than 14 days: re-fetch). On a miss, fetch, then `put`.
2. Each agent returns an explicit `owned_sources` list: the sources it read in full and extracted
   quotables from.
3. **A dimension that does not own a source does not read its body.** It cites the URL and states what it
   needs from it; the synthesis step takes the extract from the owning dimension. If two dimensions
   genuinely need the same body, the second takes it from the cache and says in its return that it did.
4. The synthesizer resolves collisions: one log entry per source, never combined, with the owning
   dimension's extract. Two agents reporting the same source is normal; two *entries* for it is a defect
   the research-log contract check will fail on.

## What always stops for the maintainer

From [`decision-procedures.md`](../../../docs/internal/decision-procedures.md). These are not judgment calls.

- **Scope.** Whether a type is in scope at all. ADR 0030 governs; a new type needs a named source
  publishing it as a written document.
- **Family contracts.** Draft them, then stop for the read. Never self-approve.
- **Releases.** Any version bump.
- **Claims about the library** in the README or public prose.

A green bundle PR merges on its own authority. Everything above waits.

## Definition of done

Gate green, links resolve, counts agree, CI green, PR merged, `main` pulled, and the progress table in
`buildout-specs.md` updated. A bundle is not done because the files exist; it is done when the tree says so.

## What this costs

Roughly 700K-1M tokens per bundle, dominated by research fan-out and the four-lens review. The brief and
the lens scoping exist to hold that down; if a run is far above it, the likely cause is lenses reading the
whole bundle instead of their own files, or research agents re-reading sources they do not own.
