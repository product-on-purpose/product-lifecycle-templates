# Contributing to product-lifecycle-templates

This is a curated library of governed document-template bundles for product management and the
software lifecycle. If you have not read [`README.md`](README.md) yet, start there: it explains what
a bundle is and what "governed" means here. [`STATE.md`](STATE.md) is the single source of truth for
what is actually built today; it outranks this file, the README, and every plan in `docs/internal/`.

Status is `beta`. The gate is enforced in CI, but the library has **zero fills by anyone but the
author** ([`STATE.md`](STATE.md)). Keep that in mind while reading the rest of this file: the thing
this project needs most is not more prose, it is evidence that the prose is right.

---

## What contributions are wanted

**1. Corrections to research.** This is the largest real defect class this library has found in
itself. A citation that resolves is not the same as a citation that supports the claim next to it;
[`STATE.md`](STATE.md) records several rounds where a manual pass against raw sources found wrong
dates, quotations from sources nobody could read, and claims attributed to authors who never made
them, all of it sitting behind a green gate for weeks. If you read a companion or a research log and
the source does not say what the text claims, that is a welcome bug report. Point at the specific
claim, the file and section it lives in, and (ideally) the primary source that shows the correction.
The review standard this kind of finding is judged against lives in
[`docs/internal/review-standards.md`](docs/internal/review-standards.md).

**2. A bundle for a document type.** The Tier-1 "must-have" floor (the catalog's own baseline of
templatable types) is complete: every templatable Tier-1 type is built, and the build backlog is
empty. New bundles beyond the floor come from the wider catalog in
[`docs/internal/catalog.md`](docs/internal/catalog.md), and they are pulled in on demand rather than
built speculatively: the catalog's own rule is to add a type only "based on which teams actually
request them", and only "when a team is actively practicing it" (`catalog.md`, the Tier-2 build
principle). If you want a type this library does not have, the strongest opening move is to say who
needs it and why, not to open a PR with a template already attached. See "What is not wanted" below
before proposing a brand-new type.

**3. A real usage report.** This is the most valuable contribution this library can receive, and the
rarest: nobody but the maintainer has ever filled one of these templates for real work. If you copy a
bundle into a real project and fill it in, a report of what worked, what section fought you, and what
you had to cut is worth more than most PRs. The catalog's own graduation rule for a Tier-1 type is that
it "survives one real usage cycle"; by that standard, nothing here has graduated yet, and this file
does not claim otherwise.

---

## What is not wanted (without evidence): new document types

Do not open a PR inventing a document type this library has never templated, on the theory that
practitioners would probably find it useful. That instinct has already produced a rejection here:
[ADR 0031](docs/internal/decisions/0031-adopt-discovery-docs-family-contract.md) ratified
`prototype-brief` as a provisional third member of the `discovery-docs` family, and its own research
pass then failed the admission test and it does not ship
([ADR 0035](docs/internal/decisions/0035-prototype-brief-fails-the-admission-test.md)).

The admission test that decision applies, generalised across the whole library in
[ADR 0030](docs/internal/decisions/0030-templating-scope-markdown-documents.md): **a candidate type is
templatable only when a named source publishes it as a written document.** Reasoning that a type
*ought* to exist, or that an adjacent artifact could be relabeled to fill a gap, is exactly the failure
this library rejected when it excluded `wireframe` (no named source publishes a written wireframe
specification; designers annotate inside the design tool) and `V2MOM` (presented under another type's
name with no source backing the presentation). A proposal for a new type should come with the same
thing a bundle's own research pass would have to find: a named source that publishes this exact type as
a document, not a plausible case for why one should exist.

---

## Running the gate locally

The bundle gate is a Python script with no external dependency beyond `pyyaml` and `jsonschema`,
both of which it skips gracefully if absent:

```bash
python tools/check-bundles.py          # the structural bundle gate (files, dashes, nesting,
                                        # citations, meta, YAML, history, refs, schema, family contract)
python tools/check-links.py            # every relative link and in-page anchor resolves
python tools/gen-manifest.py --check   # manifest.json and the README bundle-count marker are fresh
python tools/gen-atlas.py --check      # the atlas's built flags match the bundles on disk
python tools/check-adr-index.py        # the decision-record index lists every ADR
python tools/check-changelog.py        # every decision record since the last release is in CHANGELOG.md
python tools/check-research-logs.py    # every research log meets the source-record contract
python tools/check-counts.py           # every generated-count marker in a document matches the tree
```

<!-- counts: cisteps=20 -->
The full list runs in CI on every push and every pull request
([`.github/workflows/ci.yml`](.github/workflows/ci.yml)), 20 steps in total including two dependency
installs, and `main` is branch-protected on the result: a change that fails any step cannot merge.
Run the checks above before opening a PR; they take seconds and catch nearly everything CI would
catch.

**What the gate proves, and what it does not.** The gate proves structure: files present, no em-dash
or en-dash, variants nest correctly, citations resolve in both directions, metadata is well-formed.
**It never proves a citation supports the claim beside it.** That is a human review job, described
next.

---

## The build pipeline, in outline

Building a new bundle (or substantially reworking one) follows a fixed six-phase pipeline. The full
runbook, including the exact prompts, schemas, and the gotchas that have each cost a rework pass, lives
in [`docs/internal/bundle-pipeline.md`](docs/internal/bundle-pipeline.md); read it before starting real
work. In outline:

1. **Research fan-out.** Parallel research across several dimensions (origins, structure, methodology
   lineage, debates, relationships), each pass using real web retrieval under the honest-retrieval
   discipline described below.
2. **Synthesize the research log.** Dedupe sources, tier and status each one, and record what every
   source supports.
3. **Draft.** Companion first (every non-obvious claim cited), then the lean and full templates (full
   is a strict superset of lean), then the guide, the worked example, the metadata, and the history.
4. **Adversarial review.** Several independent lenses check citation support, Definition-of-Done and
   family-contract conformance, factual accuracy, and cross-example consistency. This is the
   non-negotiable phase: the pipeline's own governing principle is that the gate proves structure and
   the review is what proves content.
5. **Apply findings and re-verify.** Every review finding is itself a claim and gets checked against
   the source before it is applied; not every finding survives that check.
6. **Gate and land.** Run the full local check list, regenerate the manifest, update
   [`STATE.md`](STATE.md), the README, and `docs/internal/buildout-specs.md`, and open a PR against
   `main`.

---

## The research standard

Every non-obvious claim in a companion needs a citation, and every citation needs a source that was
actually read. The discipline, in full, is in
[`docs/internal/bundle-pipeline.md`](docs/internal/bundle-pipeline.md) and
[`docs/internal/research-prompt.md`](docs/internal/research-prompt.md); the load-bearing rule is:

- Each source is recorded once, tiered honestly (`primary`, `standards`, `academic`, `practitioner`,
  `vendor`, `reference`, `internal`), and its retrieval is recorded as exactly one of:
  - `fetched-and-verified`, meaning the page body was actually read. **Only a source in this state may
    be quoted verbatim.**
  - `url-confirmed-not-read`, meaning the URL resolves but the body was not read. No claim rests on
    this source alone.
  - `not-retrieved`, meaning neither.
- A quoted phrase must appear verbatim in a source's own recorded quotable list. Paraphrasing it into
  a "quote" is a fabrication, and this library's own review has caught that exact defect shipping
  behind a green gate more than once.
- A source that is paywalled, blocked, or a physical book that was not retrieved says so **in the
  reference itself**, rather than being presented as if it had been read.

<!-- counts: logsgated=20 -->
<!-- counts: sourcesgated=796 -->
`tools/check-research-logs.py` gates the structural side of this contract in CI (every source entry
has a number, an identity, a tier, and a retrieval status token) across 20 of the library's research
logs and 796 individual source entries; the ones it does not cover are named exceptions in the check's
own output. What it cannot check, and says so on every run, is whether a `Supports:` line is actually
true. That half is the adversarial review's job.

---

## House rules

- **No em-dash or en-dash anywhere**, in any tracked text file. Use a space-hyphen-space, or restructure
  the sentence. This is swept repo-wide in CI, not just inside bundles.
- **Reference IDs carry a human-readable handle.** Never a bare code like `ADR-0030` or `EC-4` on its
  own; pair it with a short description of what it is on first use.
- **Placeholders are `{{snake_case}}` everywhere**, quoted, so a generator or agent can find
  substitution points deterministically.
- **Generated counts, never retyped ones.** If a document states a number about the repository (a
  bundle count, an ADR count, a gate-assertion count), it carries a `<!-- counts: key=value -->` marker
  directly above the sentence, and `tools/check-counts.py` fails CI if the marker disagrees with the
  tree. This file uses the same convention; the markers above are not decoration.
- **Decision records go in [`docs/internal/decisions/`](docs/internal/decisions/)**, in
  [MADR v4](https://github.com/adr/madr) format, one file per decision, numbered sequentially. Every
  non-obvious choice in this library has one; if you are wondering why something is the way it is,
  check there before asking.

---

## How PRs are reviewed

CI is required and `main` is branch-protected: a PR cannot merge while any gate step is red, and
merging around a red gate with admin rights is against the project's own runbook (it has happened
exactly once, during a genuine CI outage, and the reason is recorded in
[`.github/workflows/ci.yml`](.github/workflows/ci.yml)).

Beyond CI, review is manual, against the Definition of Done in
[`templates/methodology.md`](templates/methodology.md): the parts of the standard the gate cannot
check (guidance-comment structure, whether a citation's `Supports:` claim is actually true, whether the
example is genuinely independent prose rather than the template's own hints reworded) are read by a
human. A bundle contribution is expected to have already been through something like the adversarial
review phase described above before it is opened as a PR; a bundle that has only passed the mechanical
gate is not yet ready for review.

For a new or reworked bundle, the same PR should update
[`STATE.md`](STATE.md) and the README's bundle table, and (if it completes or starts a family)
`docs/internal/buildout-specs.md`'s progress table, so no surface disagrees with another while the PR
is open.

---

## License

Contributions are accepted under the project's [Apache-2.0 license](LICENSE).
