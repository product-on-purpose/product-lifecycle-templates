# product-lifecycle-templates

> The template layer that humans and AI agents both reach for first: governed, self-describing, sized to context, and traceable. Coverage is not the product; correct-by-construction reuse is.

A curated library of product-management and software-lifecycle document templates. Anyone can publish a folder of Markdown templates. What makes this one different is that every template ships as a **governed bundle**: a blank shape you fill in, a researched explainer of why it is shaped that way, a fast operator card, a fully worked example, and a metadata manifest.

The north star is simple and demanding: be the indisputable best-in-class reference implementation of a template library, not a folder of templates.

---

## Quick start: use a template

Six steps, start to finished document. No install, no tooling, no account.

**1. Get the library.**

```
git clone https://github.com/product-on-purpose/product-lifecycle-templates.git
cd product-lifecycle-templates
```

**2. Pick your document type.** One folder per type under [`templates/`](templates/). If you are not sure which you want, open [`atlas/atlas.html`](atlas/atlas.html) in a browser, or read the one-line descriptions in [the table below](#what-is-in-the-library-today).

**3. Read the guide first. It takes a minute and it is the highest-value minute.**

```
templates/prd/prd_guide.md
```

It tells you when this document is the right tool, when it is **not**, and the anti-patterns that most often wreck it. If the guide says do not use it, stop here: that is the guide working.

**4. Copy the variant you need, into your own project.**

```
cp templates/prd/prd_template-lean.md ~/my-project/docs/my-feature-prd.md
```

**Default to `lean`.** Reach for `full` only when the cost of being wrong is high (hard to reverse, crosses teams, carries security or regulatory weight). You can grow lean into full later by adding sections: the variants nest by design, so nothing needs re-authoring.

**5. Fill it in. The guidance is already in the file.**

Each section carries an HTML comment with what it wants, why it matters, guiding questions, a strong-versus-weak example, and the anti-pattern to avoid. It is visible while you write and invisible when the document renders. Stuck on *why* a section exists? The comment deep-links into the companion (e.g. `templates/prd/prd_companion.md`). Want to see one finished? Every bundle ships a real worked example (`prd_example.md`).

**6. Delete the guidance comments, and ship.**

Strip the `<!-- ... -->` blocks once the section is written. Keep the `source_template` and `source_template_version` frontmatter: it is how anyone (including you, in six months) can tell where the document came from and which version of the shape it used.

> **Filling one with an agent?** Point it at the bundle folder, not just the template. The `_guide.md` tells it when the type applies, and the `_example.md` shows it what good looks like. To pick the right bundle in the first place, an agent can read [`manifest.json`](manifest.json), the machine catalog of every bundle's selectable fields (phase or classification, family, tags, sizes, aliases), generated from the metas and kept fresh by the gate. What is not yet possible is *installing* the library as a unit; see [what is on credit](#the-claim-and-what-it-is-worth) below.

---

## What makes a bundle best-in-class

Each document type produces one **bundle**. The blank template is only one file in it. The bundle is what earns trust:

- **Dual-reader by design.** A deep `companion` explains what the artifact is, where it came from, and where serious practitioners disagree, with tiered, hyperlinked citations. A short `guide` answers "should I use this here, and how do I not blow it" in under a minute. Neither makes the other reader wade through material they did not come for.
- **Sized to context.** Every type ships a `lean` and a `full` variant under a strict nesting rule: the lean template's sections are a subset of the full one's, in the same order, so a document can grow in place from lean to full without a re-author.
- **Guidance where you write.** Each section of a blank template carries an HTML-comment block with what it wants, why it matters (deep-linked to the companion), guiding questions, a strong-versus-weak example drawn from the real worked instance, and the one anti-pattern that most often wrecks it. The guidance is visible while you fill the template and vanishes when the document renders.
- **Traceable.** Filled documents carry provenance frontmatter (`source_template`, `source_template_version`), and each bundle names the skill it `pairs_with`, so the library speaks the same language as the tools that fill it.
- **Researched, not remembered.** Every non-obvious claim in a companion carries a numbered, reliability-tagged citation (`[primary]` / `[practitioner]` / `[vendor]`). One entry, one source. A source that is paywalled, blocked, or a print book says so **in the reference itself**, and nothing is quoted that was not fetched and compared word for word.

The full authoring process, the citation standard, and the per-bundle Definition of Done live in the methodology: [`templates/methodology.md`](templates/methodology.md).

---

## The claim, and what it is worth

The pitch above is the ambition. Here is the same thing with the credit separated from the cash, which is the fastest way to judge whether this library is worth your time:

- **Earned today.** Researched, dual-reader, nesting-disciplined, provenance-stamped bundles, with citations verified against raw sources and every correction recorded in the open. A gate that runs in CI and blocks merges. Decision records for every non-obvious choice.
- **Mostly earned now: "agent-native".** The machine layer landed 2026-07-17. Every bundle's metadata validates against a published schema in CI ([`tools/meta.schema.json`](tools/meta.schema.json), gate check J, [ADR 0016](docs/internal/decisions/0016-adopt-machine-checkable-metadata-schema.md)), and [`manifest.json`](manifest.json) exposes every bundle's selectable fields as structured data an agent reads instead of parsing prose, regenerated and freshness-checked by the gate ([ADR 0018](docs/internal/decisions/0018-machine-catalog-generated-manifest.md)). **What is still on credit is installability**: per decisions D2/D3 (resolved 2026-07-17), the library is **not installable via `npx skills add` nor listable on agentskills.io**, because both take exactly one unit, the *skill*, and this repo ships no `SKILL.md`. That is one missing file, not an architecture problem, and it is scheduled ([roadmap LP-2](docs/internal/roadmap.md)).
- **Still on credit: "reference implementation".** Six of 205 types, untagged, and **zero fills by anyone but the author**. By the catalog's own tier rule (a type graduates when it "survives one real usage cycle"), nothing here has graduated.

If that reads harsher than a README usually does, that is the point: [`STATE.md`](STATE.md) is the source of truth, it outranks this file, and it is kept honest on purpose.

---

## What is in the library today

<!-- bundle-count: 6 -->
**Six bundles, in two families.** Status `beta`: every one is gate-green and researched, and none has been filled in anger by anyone but the author.

**`delivery-docs`** (four bundles). Their examples chain on one fictional "Saved Views" feature, so the family reads as one traceable set: a PRD leads to user stories, which lead to acceptance criteria, which ship in a release note.

| Bundle | What it is | Pairs with |
|---|---|---|
| [`prd`](templates/prd/) | Product Requirements Document: what to build, for whom, and why | `deliver-prd` |
| [`user-stories`](templates/user-stories/) | User-centered stories that anchor work to user value | `deliver-user-stories` |
| [`acceptance-criteria`](templates/acceptance-criteria/) | The conditions that confirm a story is done | `deliver-acceptance-criteria` |
| [`release-notes`](templates/release-notes/) | The customer-facing announcement of a release | `deliver-release-notes` |

**`decision-docs`** (two bundles). A sequence, not a choice: **RFC to decide, ADR to record.**

| Bundle | What it is | Pairs with |
|---|---|---|
| [`rfc`](templates/rfc/) | The proposal circulated *before* a decision, to gather input | (none: no `develop-rfc` skill exists) |
| [`adr`](templates/adr/) | The record of a decision *after* it is made, in [MADR v4](https://github.com/adr/madr) | `develop-adr` |

Beyond these six, the library grows **by pull** from a researched catalog of 205 artifact types across 19 categories. The "must-have core" is built first; specialized and regulated types are built when a real team asks for one, not speculatively.

*A word on "complete".* This README used to call `delivery-docs` complete and verified. Both words were doing more work than they had earned, so they are gone. The family has all four intended bundles, but no family contract is adopted or validated ([roadmap WP-24](docs/internal/roadmap.md)), and "verified" did not survive contact with evidence: a citation pass on 2026-07-16 found **28 defects across those four bundles**, every one of which had been passing the gate green for weeks. They are verified *now*, against raw sources, with the corrections recorded in each bundle's research log. What the gate can and cannot prove is stated in [Quality gate](#quality-gate).

### The map: Product Artifact Atlas

[`atlas/atlas.html`](atlas/atlas.html) is a self-contained, interactive map of all 205 catalog types. Group them by category or lifecycle phase; filter by tier and by state; open any type to see its purpose, owner, methodology, and relationships. It doubles as a scoping tool: seeing the whole territory makes choosing what to build next a deliberate act rather than a guess. Open the file in any browser.

---

## Anatomy of a bundle

A bundle is a folder named by document type (for example `prd/`), containing these files:

| File | Role |
|---|---|
| `<type>_template-lean.md` | The blank shape, minimum useful |
| `<type>_template-full.md` | The blank shape, comprehensive (a strict superset of lean) |
| `<type>_companion.md` | The deep explainer: what it is, why, debates, cited references |
| `<type>_guide.md` | The operator card: when to use, quality rubric, anti-patterns |
| `<type>_example.md` | A real worked instance, no lorem, no fabricated metrics |
| `<type>_meta.yaml` | The machine manifest (catalog metadata, `pairs_with`, sizes available) |
| `<type>_history.md` | Per-bundle changelog by template version |
| `<type>_research-log.md` | The evidence trail: every source, its tier, and what it supports |

---

## How this fits with pm-skills

This library is the sibling of a skills repository. The division is clean: **a skill teaches an agent how to produce an artifact; a template is the artifact itself.** The two form a loop. A skill decides how to shape a document, the template is what gets filled, and the filled document feeds the next skill. The `pairs_with` field in each bundle's metadata is the seam that joins them.

---

## Repository layout

```
templates/
  methodology.md            The authoring process and Definition of Done
  prd/                      \
  user-stories/              }  the delivery-docs family (8 files each)
  acceptance-criteria/       }
  release-notes/            /
  rfc/                      \  the decision-docs family (8 files each)
  adr/                      /
tools/
  check-bundles.py          The governance gate (runs locally and in CI)
  check-links.py            The link gate (no tracked file may link into _local/)
  known-skills.txt          Pinned skill IDs that pairs_with may name
atlas/
  atlas.html                Interactive map of all 205 catalog types
  catalog-data.json         The atlas dataset
docs/
  internal/
    decisions/              Architecture decision records (MADR v4)
    roadmap.md              Milestones and work packages
    catalog.md              The 205-type master catalog
STATE.md                    What is actually true today. Outranks every plan.
```

Note on the directory layout: lifecycle phase is carried in bundle metadata, never in the path, so `templates/` is flat by document type rather than nested by phase. That is deliberate, and it means a type's phase can be reassigned without renaming anything. See [`docs/internal/decisions/0009-scaffold-graduation-flat-templates.md`](docs/internal/decisions/0009-scaffold-graduation-flat-templates.md).

---

## Design and roadmap

The thinking behind the library is documented, not implicit:

- [`strategy-brief_catalog-to-template-library.md`](docs/internal/strategy/catalog-to-template-library.md) - the approach and the resolved architecture decisions.
- [`implementation-plan_catalog-to-template-library.md`](docs/internal/plan.md) - the phased plan and acceptance criteria.
- [`template-library-design-spec.md`](docs/internal/design-spec.md) - the formal specification.
- [`strategy-brief_raising-the-ceiling_2026-07-02.md`](docs/internal/strategy/raising-the-ceiling.md) - where the library goes next: proving quality with evals, closing the usage loop, and serving templates to agents.

---

## Quality gate

The governance is enforceable, not aspirational. [`tools/check-bundles.py`](tools/check-bundles.py) runs eleven structural checks from the methodology's Definition of Done across every bundle in one command: the eight files are present, no em-dash or en-dash characters appear, the lean variant nests inside the full one (comparing heading *level* as well as text), the worked example has no leftover placeholders, citations resolve **in both directions** (no inline citation without a reference, and no reference nothing cites), the declared sizes match the files on disk and the meta carries no unfilled placeholder, every YAML block parses, the history documents the version the meta claims, `pairs_with` / `related_templates` point at things that exist, every meta validates against the [metadata schema](tools/meta.schema.json) (`phase` XOR `classification`, legal enums, no stray fields), and each bundle conforms to its [family contract](docs/internal/contracts/delivery-docs.md) (a delivery-docs member is in the `deliver` phase, `beta`/`stable`, and lean/full).

```
python tools/check-bundles.py     # the eleven bundle checks
python tools/check-links.py       # every relative link and anchor resolves
```

All six bundles currently pass. GitHub Actions runs both scripts on every push to `main` and on every pull request ([`.github/workflows/ci.yml`](.github/workflows/ci.yml)), and `main` is branch-protected on the gate, so a bundle that breaks these checks cannot merge.

**Scope, stated honestly, because this is the claim most worth distrusting.** The gate automates roughly **half** the methodology's Definition of Done. The research-tracing, guidance-comment-structure, companion-skeleton, guide-structure, and history-content clauses have no automation and are human-verified.

More pointedly: **the gate proves a citation *resolves*, never that the source *supports the claim*.** In July 2026 a manual pass against raw sources found 28 defects across four bundles that had been green for weeks, including two wrong dates, two quotations from sources that could not be read at all, and several claims attributed to authors who do not make them. Every one was invisible to this script and always will be. **A green run means the structure holds, not that the content is true.** Current coverage always lives in [`STATE.md`](STATE.md).

## Conventions

- **Placeholders** are `{{snake_case}}` everywhere, so a generator or agent can find substitution points deterministically.
- **Reference IDs carry a human-readable handle**, never a bare code.
- **No em-dash or en-dash characters** anywhere in the library (an organization-wide house rule).

## License

Apache-2.0.
