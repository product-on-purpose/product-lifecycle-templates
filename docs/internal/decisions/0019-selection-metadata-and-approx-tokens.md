---
status: accepted
date: 2026-07-18
decision-makers: [jprisant]
consulted: [claude]
---

# Selection metadata: authored default_size and sizing_guidance, plus a generated heuristic approx_tokens

## Context and Problem Statement

[ADR 0018](0018-machine-catalog-generated-manifest.md) shipped `manifest.json` so an agent can find the
right bundle from structured data. But finding the bundle is not the whole job. The manifest listed
`sizes_available` and nothing else about size: it never said which variant to prefer, when to reach for
the heavier one, or how much context loading a variant would cost. An agent selecting a bundle still had
to open the template files to answer "lean or full?" and "can I afford this?" - the exact prose-reading
the manifest exists to remove, one level down.

Roadmap WP-23 closes that: selection metadata that lets an agent pick a size and budget context before
fetching.

## Decision Drivers

- **A weight should be chosen deliberately, not defaulted blindly.** A recommended default and a one-line
  "when to go heavier" turn a guess into a decision.
- **The cost of a variant should be visible before the fetch**, so an agent can budget its context window.
- **Selection data must not drift from the templates it describes**, the same discipline ADR 0018 set for
  the manifest itself.
- **The gate already carries two dependencies** (PyYAML, jsonschema; ADRs 0014 and 0017). A third should
  clear a real bar, not a convenience one.

## Considered Options

For the size estimate, `approx_tokens`:
* **Option A: a standard-library heuristic** (characters / 4, rounded), computed from the template files.
  No new dependency, model-agnostic, honestly approximate. Chosen.
* **Option B: a real tokenizer** (e.g. `tiktoken`), giving exact counts, at the cost of a third gate
  dependency and a number pinned to one model family.
* **Option C: no token estimate**, leaving an agent to fetch first and measure later.

For `default_size` and `sizing_guidance`: authored fields in the meta (chosen; they are editorial
judgment) versus generated (impossible; a machine cannot decide when a decision "needs the heavier form").

## Decision Outcome

Chosen: **authored `default_size` + `sizing_guidance`, and a generated stdlib-heuristic `approx_tokens`.**

- **`default_size`** (authored) names the recommended starting variant. The schema constrains it to a
  legal size value; the cross-field rule that it must be one of *this* meta's `sizes_available` is
  enforced by gate check F, because a JSON Schema cannot express membership in a sibling field. Every
  current bundle defaults to `lean`: start minimal, escalate deliberately.
- **`sizing_guidance`** (authored) is one sentence on when to pick each size. Required and non-empty.
- **`approx_tokens`** (generated) is a per-variant map, computed by `tools/gen-manifest.py` from each
  template file as `characters / 4` rounded to the nearest 50, and emitted into the manifest. It is a
  **budgeting hint, not an exact count**. It takes no tokenizer dependency: a number that only needs to be
  roughly right is not worth pinning the library to one model's tokenizer, and rounding to 50 signals the
  approximation honestly. Because it is computed from the file, `gen-manifest.py --check` flags the
  manifest as stale the moment a template changes, so the estimate cannot drift.

Option B (tiktoken) was rejected because it buys precision the use case does not need while adding a
dependency and a model-specific bias: exact for one family, wrong for others, for a value used only to
budget. If a consumer ever genuinely needs exact counts, that is an additive change with its own ADR.
Option C was rejected because "fetch, then discover it was too big" is the friction the estimate removes.

### Consequences

* Good: an agent can pick a size and budget context from the manifest alone, without opening a single
  template. The selection surface RFC-0001 envisioned is now complete for v1.
* Good: `approx_tokens` cannot drift from the templates, and `default_size` cannot name a size the bundle
  does not ship (check F).
* Bad, accepted: `characters / 4` is crude. Markdown with code, tables, or dense HTML comments tokenizes
  differently than prose. It is labeled approximate, rounded to advertise that, and is fit for budgeting,
  not billing.
* Neutral: `default_size` introduces the first cross-field rule the schema cannot express, so check F now
  carries a small membership check alongside the schema's per-field validation.

### Confirmation

Enforced in CI: check J requires `default_size` (a legal size value) and a non-whitespace
`sizing_guidance`; check F requires `default_size` to be one of `sizes_available`; and
`gen-manifest.py --check` keeps `approx_tokens` fresh. Branch protection covers the gate job.

Adversarially tested at authoring time (2026-07-18): a missing `default_size`, a missing or
whitespace-only `sizing_guidance`, and an illegal `default_size` enum value each fail check J; a
`default_size` that is a legal size but absent from `sizes_available` passes the schema yet fails check F;
the token estimate is computed correctly (400 and 2000 characters give 100 and 500), is deterministic
across builds, changes when a template is edited, and a stale manifest is caught. Thirteen behaviors, all
as required; the gate is 10/10 on all six bundles and the manifest is fresh.

## More Information

Builds on [ADR 0018](0018-machine-catalog-generated-manifest.md): the manifest is the surface, and this
is the selection data on it. It completes WP-23. The field set remains a v1 selection surface, not the
last word; later work (fill tooling, a family contract) continues the machine layer.
