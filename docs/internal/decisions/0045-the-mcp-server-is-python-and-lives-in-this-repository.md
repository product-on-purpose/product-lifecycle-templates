---
status: accepted
date: 2026-09-06
decision-makers: [jprisant]
consulted: [claude]
---

# The MCP server is Python and lives in this repository, rather than a TypeScript package mirroring pm-skills-mcp

## TL;DR

- **Decision:** build the AG-2 server as [`tools/mcp_server.py`](../../../tools/mcp_server.py) in this
  repository, declared to Claude Code through a plugin-root [`.mcp.json`](../../../.mcp.json), gated by
  the same CI that gates everything else. Reject the 2026-07-12 audit sketch's plan for a separate
  publishable npm package (`product-lifecycle-templates-mcp`) built with TypeScript, `tsc`, vitest and an
  embed step packaging `templates/**` into the artifact.
- **Why:** the recommended install route already clones this whole repository, so there is **nothing to
  embed**; two of the five tools are already written in Python here, so wrapping is an `import` where
  mirroring is a rewrite plus a parity test maintained forever; and an embedded copy of `templates/**`
  would be a **fifth artifact that can drift from the tree**, which is the defect class this library
  spends its entire gate catching.
- **Also decided, and the part with teeth:** the server **calls** `validate-fill.py` and
  `strip-template.py` rather than reimplementing them. "The server agrees with the CLI" is therefore true
  by construction, not by a parity suite somebody has to keep running - though the suite asserts it
  anyway, on the refusing path as well as the passing one.
- **Status:** accepted 2026-09-06. Completes roadmap WP-51 (AG-2, the MCP server) and unblocks
  [`ag2-mcp-spec.md`](../ag2-mcp-spec.md), which had been held at "blocked on one maintainer decision"
  since 2026-09-05.

## Context and Problem Statement

The AG-2 sketch, written 2026-07-12 as part of the Fable audit package, specified the server by analogy:
mirror `pm-skills-mcp`, the sibling repository's server. TypeScript, the MCP TypeScript SDK, a `tsc`
build, an embed step, vitest, an npm bin, published to the registry.

That analogy carried an assumption nobody stated: that the server would reach users as a package. It is
worth checking, because **this repository has no `package.json`, no `tsconfig.json`, and no JavaScript
build of any kind.** Its toolchain is Python plus four `.mjs` scripts node runs directly. Standing up the
sketch means adopting a second language toolchain, a build, a test framework and a publish flow before
its first assertion runs.

The question is not which language is better. It is **what the server has to reach the user through**,
and whether an embedded copy of the content is a cost or a feature.

## Decision Drivers

- The install routes that actually exist, per [`installing.md`](../../how-to/installing.md).
- Drift. Every generated artifact in this repository has a `--check` mode precisely because a second copy
  of a fact goes stale, and this library's own changelog records four separate instances of it doing so.
- What is already written. `validate_fill` and `stamp_and_strip` exist as Python tools with tests.
- What CI can gate today without a new toolchain.

## Considered Options

- **A. TypeScript npm package**, as sketched, mirroring `pm-skills-mcp`.
- **B. Python in this repository**, wrapping the existing tools, declared through `.mcp.json`.

## Decision Outcome

Chosen: **B**.

### The install route removes the reason for an embed step

`installing.md` documents two routes. The recommended one is the Claude Code plugin, which **clones this
repository** and gives the user both skills and all 27 bundles. The second, `npx skills add`, installs the
skills alone at roughly 47 KB.

An MCP server declared in a plugin-root `.mcp.json` rides the first route. When the plugin is enabled, the
templates are already on disk beside the server, at a path `${CLAUDE_PLUGIN_ROOT}` resolves. There is
nothing to package because the content arrived with the server.

The sketch's embed step exists to solve a problem that route does not have. Worse, solving it creates one:
an embedded `templates/**` inside a published npm artifact is a copy, and this repository's whole
architecture is an argument that copies go stale. `manifest.json`, `sections.json`, the atlas and
`INDEX.md` are all generated with `--check` modes for exactly this reason. Adding a fifth copy that no
`--check` can reach, in another repository, on another release cadence, would be the first place the
library stopped taking its own advice.

### Wrapping is an import; mirroring is a rewrite plus a permanent obligation

Two of the five tools already exist and are tested: `tools/validate-fill.py` and
`tools/strip-template.py`. In Python the server loads and calls them. In TypeScript it either shells out
to Python - inheriting the interpreter problem without the benefit - or reimplements the placeholder
scan, the guidance strip, the provenance stamp and the section-completeness check, and then owns a parity
suite forever.

That parity suite is not hypothetical work. `strip-template.py`'s placeholder scan runs on the **stripped**
body, because guidance comments name placeholders as instruction and scanning raw text refuses every
document forever. A reimplementation that missed that subtlety would pass a naive test and fail every real
document. Calling the original cannot miss it.

### Consequences

- Good: one toolchain. The server is gated by the CI that already runs, in the language the repository
  already uses, with no build step between the source and what runs.
- Good: the server and the tools cannot disagree, because they are the same code.
- Good: `tools/run-gate.py` picks the new CI step up automatically, since it derives its list from
  `ci.yml` rather than from a directory listing.
- **Bad, and named rather than minimised:** this diverges from `pm-skills-mcp`. Two sibling repositories
  now serve MCP differently, and a future maintainer will have to hold both shapes in their head. That
  cost is real. It is accepted because nobody has asked for an npm package, and consistency with a sibling
  is a weaker reason than not shipping a copy of the content that can drift.
- Bad: a new dependency, `mcp`, in the CI install step. It is required rather than optional, because a
  test that skips when a dependency is absent is a test that proves nothing on the day it matters.
- Bad: `.mcp.json` names one interpreter, and `python`, `python3` and `py` routinely resolve to three
  different interpreters on one machine. The failure is handled rather than avoided: the server names the
  interpreter it was run under in its ImportError, so the message is diagnosable instead of "install a
  package you already installed".

## What building it falsified

The spec this decision unblocks was itself corrected by execution, and the pattern is now familiar enough
to state plainly: **a filter that returns something is not a filter that returns the right thing.**

1. **The taxonomy axis is `phase` XOR `classification`.** Measured: 17 bundles carry a phase, 10 carry a
   classification, none carry both and none carry neither. The sketch specified a `phase` filter alone,
   which would have returned plausible non-empty results while **ten bundles, 37% of the library, were
   unreachable**. The server takes an `axis` parameter accepting either.
2. **Only four of the six phase values are used by any built bundle.** [ADR 0003](0003-phase-vocabulary.md)
   fixed the vocabulary at six to match the pm-skills seam, and its own final section left "does this
   library need a second axis?" open. The tree has since answered yes. A teachable error listing all six
   sends an agent looking for `define` and `measure` bundles that do not exist, so `axis_values()` reports
   what is there and, separately, what is declared and unused.
3. **The 500-token discovery budget was ours and it was wrong.** Three candidates carrying the field list
   the spec itself prescribed cost **1,194** tokens, not 500. `sizing_guidance` alone averages 632
   characters. It is post-selection prose - what you read once you have chosen a bundle and are choosing a
   size - so it moved to `get_template`, and the measured worst case fell to 685. This is the ninth
   falsified budget in this lineage and the first that was not the 2026-07-12 sketch's.

## Not decided here

- **`alias-index.json` is not built.** The sketch names it as an embed input and as what "carries most
  real traffic" for search. The spec's own section 4 says ranking over `aliases`, `title`, `summary` and
  `tags` directly is adequate for v1, and it measurably is. Building a fifth generated artifact to serve a
  ranking that already works would be the countable-target failure in generator form. If ranking quality
  is ever measured and found wanting, that is the moment.
- **Whether the ranking is good.** No assertion in `tools/test-mcp-server.py` scores it, and the suite says
  so in its own output. It asserts contracts: field names, addressability of all 58 variants, parity with
  the wrapped tools, and that refusals surface as refusals.
- **Distribution.** Nothing here is submitted anywhere. The server ships to whoever installs the plugin,
  and that is the whole of its reach today.

## More information

- Spec: [`ag2-mcp-spec.md`](../ag2-mcp-spec.md), whose section 7 posed this decision.
- The wrapped tools: [ADR 0043](0043-the-usage-gate-becomes-advisory.md) records the honesty posture these
  responses inherit; [ADR 0044](0044-the-section-schema-is-a-second-generated-artifact.md) built
  `sections.json`, which `validate_fill` reads.
- The format axis the variant addressing implements:
  [ADR 0028](0028-adopt-a-format-axis.md).
