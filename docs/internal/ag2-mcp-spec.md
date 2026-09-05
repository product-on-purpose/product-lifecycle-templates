# Spec: AG-2, the MCP server, refreshed against the tree

Status: **spec, blocked on one maintainer decision** (the stack, section 7). Supersedes the 2026-07-12
audit sketch `spec_ag2-mcp-server.md`, which is gitignored and which this document quotes where it
corrects it.

This exists because the sketch was verified by execution on 2026-09-05 rather than by reading, and **seven
of its claims are false**. Its acceptance criteria cannot be met by any implementation, because they name
token budgets no payload in this library has ever fit. Building to it would have produced a server that
fails its own tests on day one.

The measurements below are reproducible from the tree. Every token figure is `characters / 4`, the same
rough estimate `tools/gen-manifest.py` uses for `approx_tokens`, so the numbers here and the numbers the
server would serve come from one method.

---

## 1. What execution falsified

| Sketch claim | Measured | Verdict |
|---|---|---|
| candidates carry `bundle_id`, `one_line_summary` | the fields are `id` and `summary` | **false** |
| candidates carry `conformance`, `state` | neither field exists in `manifest.json` | **false** |
| provenance header carries `sha256` | no hash exists anywhere in the tooling | **false** |
| empty search returns "the 8 phase names" | [ADR 0003](decisions/0003-phase-vocabulary.md) settled the vocabulary at **6** | **false** |
| `get_template` default is "roughly 1.6-2.5k tokens" | **1,543 to 6,612**, median 4,334 | **false** |
| AC: "default `get_template` under 2.6k for every bundle" | **23 of 27 exceed it**, up to 2.5x | **false** |
| `get_grading_pack` "~800-1,200 tokens" | guide alone is 530 to 3,264, median 1,744 | **false** |
| `template://{id}/summary` "~800-1,000 tokens" | 793 to 3,376, median ~1,900 | **false** |
| `search_templates` "under 400 tokens for 3 candidates" | **368** | **true** |
| out-cap at 8k "is a workable safety valve" | template+guide never exceeds 6,612, so it never fires on the default path | **true** |
| `validate_fill` section completeness against a section schema | `sections.json` provides exactly this | **true, and built** |
| `validate_fill` frontmatter provenance check | `source_template` and `source_template_version` are in 58/58 variants | **true, and built** |

**The pattern is one error repeated.** Every false budget is too small, and each was written before the
library had the bundles it now has. The sketch predates 20 of the 27.

### A note on the sibling sketch, because it sharpens what "verified by execution" is worth

`spec_lp1-use-template-flow.md` section 3 ships an extraction regex it calls a "normative contract".
[ADR 0044](decisions/0044-the-section-schema-is-a-second-generated-artifact.md) records that it extracts
**zero of 353 genuine `WHAT` fields**. An independent verification on 2026-09-05 reproduced that and found
something worse: run against raw file text, the regex returns **32 `WHAT` matches, and all 32 are false
positives** - ALLCAPS heading lines inside each file's preamble comment, such as `WHAT A BUSINESS CASE IS,
AND IS NOT`. None is a per-section field.

**So the failure mode is not "returns nothing", it is "returns plausible garbage".** An implementer
spot-checking the contract sees a non-empty result under the label they expected and moves on. That is the
same shape as every other defect this session surfaced: `check-counts.py` green beside stale prose, a
`future:` label passing forever, `check-adr-index.py` green over a table that renders in two pieces. **A
check that returns something is not a check that returns the right thing**, and the only way to tell them
apart is to count what it counted against a number derived another way.

(The two runs also differ on `WEAK`: 357 counted within guidance blocks only, 360 counted across raw file
text, the extra three being preamble prose. Both are correct in their own scope. ADR 0044's figure is the
guidance-block one, which is the scope that matters for a parser.)

---

## 2. The correction that matters: the budget governs discovery, not retrieval

The sketch treats "under 1,200 tokens" as a property of every response. Measured, that is achievable for
**metadata** and impossible for **content**, because a template *is* the payload:

| Response | Measured approx tokens | Fits a 1,200 budget |
|---|---|---|
| `search_templates`, 3 candidates | **368** | yes |
| `search_templates`, 8 candidates | 1,154 | yes |
| section outline, largest bundle | 1,268 | at the edge |
| whole catalog, 27 entries | 3,782 | no, must page or filter |
| **template alone, default size** | **998 to 3,348**, median 2,233 | **no** |
| template + guide | 1,543 to 6,612 | no |
| companion | 3,548 to 14,246 | no |

**So the budget is a discovery contract, not a global one.** Discovery responses stay small so an agent
can choose cheaply. Retrieval costs what the artifact costs, and the honest design is not a smaller cap
but **a priced menu**: every discovery response already carries `approx_tokens` per variant, so an agent
knows the price before it pays. That field exists today and was built for exactly this
([ADR 0019](decisions/0019-selection-metadata-and-approx-tokens.md)).

**Consequence for the default.** `parts` must default to **`["template"]`**, not template+guide. The
sketch's default is the single largest source of its budget error: adding the guide roughly doubles the
median payload for a part most callers do not need on the first fetch.

---

## 3. The tools, corrected

Five tools, unchanged in intent. **Two already exist as Python in this repository** and would be wrapped
rather than rewritten.

### 3.1 `search_templates`
- **In:** `{ query, phase?, max? = 3 }`
- **Out, per candidate:** `{ id, title, summary, doc_type, sizes_available, default_size, sizing_guidance, approx_tokens, tags, aliases }` — the field names `manifest.json` actually uses.
- **Budget:** 368 tokens for 3, 1,154 for 8. Cap `max` at 8.
- **Teachable error:** an empty result returns the **six** phase values and three example queries. Not eight.

### 3.2 `get_template`
- **In:** `{ id, size? = default, format? = default, parts? = ["template"] }`
- **`format` is new and non-optional to the design.** The sketch predates [ADR 0028](decisions/0028-adopt-a-format-axis.md); four bundles ship three or four variants, and an id-plus-size lookup cannot address them.
- **Out:** the requested parts, each with its own token count, plus `{ template_version, library_version }`. **No `sha256`**: nothing in the tree computes one, and inventing a hash to satisfy a sketch is how a spec claim becomes a lie.
- **Out cap:** 8k, retained. It never fires on the default path, which is the point of a safety valve.

### 3.3 `get_grading_pack`
- **In:** `{ id }`
- **Budget: 530 to 3,264, median 1,744.** State the real range rather than a target no bundle meets. Two of 27 fall inside the sketch's 800-1,200.

### 3.4 `validate_fill` — **already built**
`tools/validate-fill.py` performs every check the sketch names: placeholder scan, residual-comment scan,
frontmatter provenance, and section completeness against `sections.json`. It exits 2 on failure and has a
`--json` mode. The server wraps it; it does not reimplement it.

### 3.5 `stamp_and_strip` — **already built**
`tools/strip-template.py` removes guidance, stamps `filled_by` / `fill_method` / `fill_date`, and refuses
on remaining placeholders. Same wrapping.

---

## 4. What must exist first, and does not

1. **`alias-index.json`.** The sketch names it as an embed input and as what "carries most real traffic"
   for search. **It does not exist.** `manifest.json` carries per-bundle `aliases`, so the index is
   generatable rather than authorable, and it should be a fifth generator with a `--check` mode following
   [ADR 0044](decisions/0044-the-section-schema-is-a-second-generated-artifact.md). Until it exists,
   search ranks over `aliases`, `title`, `summary` and `tags` directly, which is adequate and honest.
2. **A `library_version` the server can report.** `library.json` carries the version; the server must read
   it rather than hardcode, or it will drift the way every retyped count in this repository has.

Neither is large. Both are prerequisites, not parallel work.

---

## 5. Acceptance criteria, rewritten to be meetable

- [ ] `search_templates` returns 3 candidates in **under 500** approx tokens, measured, for all 27 bundles.
- [ ] `get_template` with default `parts` returns exactly one artifact and reports its token count, and the reported count is within 10% of `manifest.json`'s `approx_tokens` for that variant.
- [ ] Every response naming a bundle uses the field names `manifest.json` uses. A response carrying `bundle_id` or `one_line_summary` fails.
- [ ] `get_template` addresses all **58** variants, including the 11 that exist only under a non-default format.
- [ ] `validate_fill` and `stamp_and_strip` agree exactly with the Python tools they wrap, asserted by running both over the same fixtures.
- [ ] An agent with only this server configured completes intent to selection to fetch to fill to validation, and the transcript shows it never guessed a token cost.
- [ ] The server reports the library version it was built from, read from `library.json`.

The dropped criterion is the sketch's "default payload under 2.6k for every bundle". It is not achievable
and was never achievable; it is replaced by the priced-menu contract in section 2.

---

## 6. What stays out of v1

Unchanged from the sketch and still right: no server-side `fill_template` (drafting is client judgment),
no embeddings (alias ranking first), no write-back (needs a storage decision that still does not exist).

---

## 7. The decision this spec is blocked on

**The stack.** The sketch says mirror `pm-skills-mcp`: TypeScript, MCP SDK, `tsc` build, an embed step
packaging content into the artifact, vitest, npm bin, published as `product-lifecycle-templates-mcp`.

That is a **separate publishable npm package**, and this repository has no `package.json`, no
`tsconfig.json`, and no JS build of any kind. Its entire toolchain is Python plus four `.mjs` scripts run
directly by node. Standing it up means adopting a second language toolchain, a build, a test framework and
a publish flow.

The alternative is a Python MCP server inside this repository, wrapping the two tools that already exist
and reading the two generated artifacts that already exist, gated by the same CI that gates everything
else.

**The trade is real in both directions.** The sketch's reason for TypeScript is ecosystem fit and
consistency with the sibling; the reason against is that two of the five tools are already written in
Python here, and an embedded copy of `templates/**` inside an npm artifact is a fifth thing that can drift
from the tree. Nothing measurable settles it, which is why it is a maintainer decision rather than a
finding.

**Neither path starts until it is made.** Building the wrong one is a week of work that lands in the wrong
repository in the wrong language.
