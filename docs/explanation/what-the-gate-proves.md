---
title: "What the gate proves"
description: "The honest scope of this library's quality claim, and what it deliberately does not claim"
audience: "both"
level: "intermediate"
tags:
  - explanation
  - governance
  - evidence
---

# What the gate proves

This is the honest scope of the quality claim behind this library, written for a reader who has not
seen the repository before and is deciding whether to trust it. Every factual claim below points at a
file you can open. Every number carries a marker that [`tools/check-counts.py`](../../tools/check-counts.py)
checks in CI: if the number in this file ever drifts from the tree, the build fails, not the sentence.

The short version: a machine proves structure. A human, or an agent doing a human's job, has to judge
content. This document draws that line as precisely as the tree allows, then states what is still owed.

## What the gate proves

The gate is [`tools/check-bundles.py`](../../tools/check-bundles.py). It runs eleven checks against every
bundle in the library (a "bundle" is the full set of files that make up one document type, such as
`prd` or `bug-report`; see [`README.md`](../../README.md#anatomy-of-a-bundle) for the anatomy). Each check
is structural: it can be answered by parsing text, never by judging whether the text is right.

| Check | Name | What it guarantees |
|---|---|---|
| A | Files | All eight files are present, and exactly the size variants the bundle's meta declares exist on disk, no more and no fewer |
| B | Dashes | No em-dash or en-dash character appears anywhere in the bundle |
| C | Nesting | The lean template's sections are an ordered subset of the full template's, matching both heading text and heading level |
| D | Example | No unfilled `{{placeholder}}` survives in the worked example |
| E | Citations | Every inline citation resolves to a reference anchor, and every anchor is cited by something, in both directions |
| F | Meta contract | The declared size vocabulary is non-empty, internally consistent, and carries no unfilled placeholder |
| G | Frontmatter YAML | Every YAML frontmatter block in the bundle parses |
| H | History | A history entry exists for the template version the meta claims |
| I | Refs resolve | `pairs_with` names a skill on the pinned list, and `related_templates` names a bundle that exists, or is marked `future:` and is genuinely unbuilt |
| J | Meta schema | The meta validates against [`tools/meta.schema.json`](../../tools/meta.schema.json): required fields present, enums legal, exactly one of `phase` or `classification` |
| K | Family | The bundle's phase or classification, status, and size shape conform to its family's contract in [`docs/internal/contracts/`](../internal/contracts/) |

<!-- counts: bundles=27 -->
All twenty-seven bundles pass all eleven checks today. GitHub Actions runs the gate on every push and every
pull request ([`.github/workflows/ci.yml`](../../.github/workflows/ci.yml)), and `main` is branch-protected
on it, so a bundle that fails a check cannot merge. That is what "enforced" means here: not a convention
anyone is trusted to remember, but a script with an exit code.

## What the CI steps beyond the gate prove

The gate is one job in a longer pipeline. The other steps each close a specific gap the gate cannot see
by itself, most of them opened by a real defect that shipped past a green gate first.

- **Two fixture-driven self-tests** for check K (family conformance) and the format axis. Most of their
  failure branches have no live subject once the tree is clean, so a self-test is the only way to know
  they still fail when they should. Each is mutation-checked against a deliberately broken
  implementation.
  <!-- counts: checkk=96 -->
  `tools/test-check-k.py` runs 94 assertions;
  <!-- counts: checkformats=82 -->
  `tools/test-check-formats.py` runs 80.
- **The link gate** (`tools/check-links.py`). The bundle gate only looks inside one bundle at a time, so
  a link broken by moving or renaming a file elsewhere in the tree passes it green. This step also
  enforces that no tracked file links into the untracked `_local/` directory, which would resolve for
  one person and 404 for everyone else.
- **Manifest and atlas freshness** (`tools/gen-manifest.py --check`, `tools/gen-atlas.py --check`).
  [`manifest.json`](../../manifest.json) and the atlas dataset are generated from the bundle metas and
  committed; these steps regenerate both in memory and fail if the committed copy has drifted.
- **The ADR index** (`tools/check-adr-index.py`). Fails if any decision record under
  [`docs/internal/decisions/`](../internal/decisions/) is missing from its own index, or the index points
  at a file that does not exist.
- **Changelog freshness** (`tools/check-changelog.py`). Fails if a decision record since the last release
  has no entry in `CHANGELOG.md`. It proves nothing is missing from the log, not that what is there is
  good.
- **The research-log contract** (`tools/check-research-logs.py`, plus its own self-test). Every source in
  a bundle's research log must carry a retrieval status and, where the entry supports a claim, a
  `Supports:` clause.
  <!-- counts: logsgated=21, sourcesgated=826 -->
  This runs across all 20 research logs the check gates, covering 796 individual sources.
- **Self-reported counts** (`tools/check-counts.py`). The same mechanism that pins every number in this
  document. It recomputes each fact from the tree and fails when a marker disagrees. It does not, and by
  its own header comment says it cannot, read the sentence sitting next to a marker that is technically
  correct.
- **Example independence and example chronology** (`tools/check-example-independence.py`,
  `tools/check-example-chronology.py`). The first catches a worked example that is the template's own
  guidance text reworded rather than a genuinely different scenario. The second catches an example that
  cites a document dated after itself, breaking the chronology the library's chained examples depend on.
- **Rubric scope** (`tools/check-rubric-scope.py`). Enforces that a guide's scored rubric carries a scope
  table when its rows are variant-specific, and that the arithmetic in that table is consistent.
- **Workflow prompt strings** (`tools/check-workflow-prompts.py`) and the **research-log generator
  self-test** (`tools/test-gen-research-log.py`) guard the build tooling itself, not the templates.
  <!-- counts: checklogs=89 -->
  The generator's own self-test runs 88 assertions.
- **A repo-wide dash sweep.** Check B only scans inside bundles; this step scans every tracked
  `.md`, `.yaml`, `.yml`, `.py`, and `.json` file in the repository for an em-dash or en-dash.
- **Eval arm parity** (`tools/check-eval-arm-parity.py`). The efficacy eval's treatment and control arms
  must be handed a byte-identical block of general writing advice, so that the only difference between
  them is whether one of them also got a template. That identity lives in two hand-maintained files, and
  if they ever diverge the arms stop being comparable while every check still passes and every number
  still looks reasonable. This is the one step in the list that guards a *measurement* rather than a
  document.
- **The published skill surface** (`tools/check-export-surface.py`). Every other step in this list
  validates the **tree**. This one asks what a **stranger receives**, and those turned out to be
  different things: on 2026-08-08 the first ever run of `npx skills add` installed two skills, the second
  being the maintainer-internal build harness. Nothing here could see it, because nothing here was
  looking outward. It asserts that the set of skills the installer would export equals exactly the set
  `library.json` declares, in both directions: an undeclared skill that ships is a leak, and a declared
  skill that does not ship is a broken install.
- **Version agreement** (`tools/check-version-agreement.py`). The library's version is written in six
  places, and listing clause L4 requires them to agree while naming its own verification method as
  "review". One of the six is not metadata: the skill's body says it fetches templates from the release
  tag matching its own `metadata.version`, so that field is half of a URL, and a stale value points every
  installed copy at a tree it did not ship with while nothing fails. Two of the six are deliberately left
  to checks that already exist rather than duplicated here.
- **The Standard's conformance gate** (`node scripts/check.mjs`, from a pinned checkout of
  `agent-skills-toolkit`, which also supplies the README version-badge guard `check-readme-version.mjs`
  run in the same step). See below: it is the only step whose rules were written elsewhere.

<!-- counts: cisteps=26 -->
Twenty-six CI steps run in total, and they are not all the same kind of thing. **Four** are checkout,
runtime setup and dependency installation, and prove nothing at all. **Twenty-one** prove the tree is
*structurally* consistent with itself: files exist, links resolve, generated artifacts match their
source, a marker matches a count.

**The twenty-sixth is the only one that can surprise anybody**, because it is the only one whose rules
this repository did not write. It runs the Advanced Skill Library Standard's conformance gate, and the
toolkit's README version-badge guard, from a pinned checkout of a separate repository, so it can report
that this library has stopped meeting a published external standard. Every other step can only report
that this library disagrees with itself. On 2026-08-08 it earned that description twice over: it caught a
frontmatter violation in a release note that all twelve local checks, four self-tests and both generators
had passed.

None of the twenty-five, individually or together, can tell you whether a sentence in a companion is true.

## What no machine checks

This is the review surface, and it is the most important section in this document. It is drawn directly
from [`docs/internal/review-standards.md`](../internal/review-standards.md), the brief a review agent reads
before judging a bundle, and every item on it has shipped past a green gate at least once.

**1. A claim no logged source supports.** This is the dominant defect class the library has found in
itself. A number, a year, a named person, or a mechanism that reads as entirely plausible, is written in
the same confident voice as everything around it, and is backed by nothing in the bundle's research log.
Recorded examples, quoted in `review-standards.md` section 5, include a companion attributing a
definition to a named person and year that return zero matches in that bundle's log, and a claim that a
failure mode is "the single most common" where the phrase "most common" appears nowhere in the log
either. The fix the standard states is not optional: delete the claim, or label it honestly as unproven.
Searching for a source that would justify a sentence already written is how a fabrication acquires a
footnote after the fact, and the standard names that specifically as the failure mode to avoid.

**2. A quotation that exists in no source.** The gate's citation check (E) confirms a citation *resolves*
to an anchor. It cannot confirm the quoted words actually appear at that source, because it never reads
the source. Two fabricated quotations shipped inside one bundle's research log and survived a
verification pass over the log's source entries, because the quotations sat in the log's narrative
prose, not in the structured entries the pass checked. A verification pass over source entries does not
verify the prose that cites them.

**3. A frequency or superlative claim nothing measured.** Phrases like "the most common failure" or
"universally acknowledged" assert a comparison across evidence nobody counted. `tools/lint-number-provenance.py`
and `tools/lint-unsourced-confidence.py` enumerate candidate phrases mechanically, but neither produces a
defect list: a flagged line is a candidate for a human or reviewing agent to judge, not a finding.

**4. A teaching point that contradicts a sibling file.** A bundle's companion, guide, and example are
meant to teach the same thing three different ways. Nothing in the gate compares them to each other for
agreement; a companion and a guide can quietly disagree about when a document type applies, and every
check still passes.

**5. An example that is the template's own guidance text reworded.** `tools/check-example-independence.py`
catches a copied *passage*, string for string. It cannot catch a copied *argument*: the same point made
in different words is invisible to a string comparison and has to be read to be caught.

**6. A rubric row that grades a section the variant does not ship.** `tools/check-rubric-scope.py`
enforces that a scope table exists and that its arithmetic is internally consistent. Whether the table
correctly maps each rubric row to the variants that actually ship that section is a judgment call the
check does not make.

**7. Prose that disagrees with a count marker beside it.** This is the mechanism this very document uses.
`tools/check-counts.py` states in its own header that it compares markers against the tree and cannot
read the sentence sitting next to a marker that technically matches. A marker can be correct while the
paragraph around it is stale.

## What the four-lens review adds, and why it is not a machine

Past the gate and the CI steps, every bundle also goes through a four-lens review before it ships. Each
lens reads a different subset of the bundle's files and owns a different one of the judgment calls above,
following the same `review-standards.md` brief:

| Lens | Reads | Owns |
|---|---|---|
| citation-support | research log, companion | Every companion claim checked against the log's `Supports:` clause; every quote checked against the log's `quotable` field |
| dod-family-conformance | templates, guide, family contract | Guidance-comment structure, section skeleton, guide shape, and the bundle's own family obligation |
| accuracy-teaching-point | companion, guide, example | Historical and conceptual claims checked against the log; the teaching point held consistent across all three files |
| chaining-consistency | example, sibling examples, templates | The worked example internally sound, every template section instantiated, and the example consistent with the shared narrative thread it belongs to |

The reason this is not a machine check, stated plainly: each lens has to decide whether a source
*supports* a claim, not whether a citation resolves; whether a teaching point in one file *agrees* with
another, not whether both files parse; and whether a worked example is a *genuinely different scenario*,
not whether a string match ran clean. All three of those are judgment calls, not parses. The two lint
tools that feed the review (`tools/lint-number-provenance.py`, `tools/lint-unsourced-confidence.py`) are
explicit about this in their own output: they enumerate candidates for a reader to judge, and neither one
returns a defect list on its own.

## The limits, stated flatly

Coverage is not validation, and this library's own tier rule says so about itself. These are the limits
as they stand today, stated without softening:

- **Template quality was measured on 2026-08-08, on three of the twenty-six bundles then in the library, and the result was VOID.**
  The gate and the CI steps prove structure; the four-lens review argues content, and an argument is not a
  measurement. An actual measurement now exists and it does not support a quality claim either. Two
  blinded runs both failed the discrimination gate, and what they show consistently is the **circularity
  signature**: **+0.85** on criteria drawn from the templates' own guide, beside **-0.03**, an interval
  spanning zero, on decision-usefulness criteria drawn from neither the template nor its guide.
  [The result](../../evals/results/2026-08-08_matched-rerun.md), and
  [the protocol](../internal/eval-protocol.md) that was written before any number existed.

  **Updated 2026-09-03, and this is the first run that is not void.** A fourth run cleared every validity
  gate over **two scenarios of the `prd` bundle only**. Rubric gap **+1.18** (interval +1.10 to +1.26),
  held-out gap **+0.14** (+0.11 to +0.17), and **probe gap exactly 0.00**: a writer with no template
  answered a reader's questions as well as one with it. Per protocol section 4 the held-out gap is **not a
  gate** and neither passes nor fails anything, and its criteria are selected on absence, which biases them
  toward null by design. Two scenarios of one bundle says nothing about the other twenty-six.
  [The result](../../evals/results/2026-09-03_two-scenario.md).
- **No efficacy claim is available in either direction.** Nothing here shows that a document written with
  one of these templates leads to a better outcome than one written without it, and nothing here shows the
  reverse. Three bundles of twenty-six were tested, by an LLM rather than a human author, and scored by
  LLM judges.
- **No template has been filled by anyone but the author.** Every worked example in every bundle was
  written by the same person who wrote the template. Independent usage, the strongest test of whether a
  template's shape actually holds up in someone else's hands, has not happened yet.
- **By the library's own tier rule, nothing here has graduated.** [`README.md`](../../README.md#the-claim-and-what-it-is-worth)
  states the rule directly: a document type graduates from Tier 1 to Tier 2 when it "survives one real
  usage cycle."
  <!-- counts: tier1=25 -->
  Twenty-five of the 25 templatable Tier-1 types are now built, which closes the library's coverage
  floor. It does not close the graduation question. Every one of those 25 is still Tier 1, and every
  bundle in the library carries a `status: beta` in its meta (see, for example,
  [`templates/prd/prd_meta.yaml`](../../templates/prd/prd_meta.yaml)), because none has cleared that bar.
- **A green gate has been wrong before, at scale.** A manual citation pass in July 2026 found 28 defects
  across four bundles that had been passing the gate green for weeks, including wrong dates, quotations
  from sources that could not be read, and claims attributed to people who do not make them. Every one of
  those was invisible to the gate then, and the class of defect they belong to is invisible to the gate
  now, for the same structural reason: the gate checks that a citation resolves, never that it is true.
- **The version this document describes is `v0.1.0`.** A `v0.2.0` is being prepared, but it has not
  shipped, and this document describes the gate and review process as they run against the tree today,
  not as they are planned to run.

None of this is an argument against using the library. It is the argument for reading this page before
you decide how much to trust a bundle: the structure is enforced and will stay enforced, the content is
argued by people (and reviewing agents) doing their best reading, and the two are not the same claim.
