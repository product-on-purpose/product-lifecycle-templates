<a id="readme-top"></a>

# product-lifecycle-templates

**The template layer that humans and AI agents both reach for first: governed, self-describing, sized to context, and traceable.**

A curated library of product-management and software-lifecycle document templates. Anyone can publish a folder of Markdown files. What makes this one different is that every template ships as a **governed bundle**: a blank shape you fill in, a researched explainer of why it is shaped that way, a fast operator card, a fully worked example, and machine-readable metadata. Coverage is not the product; correct-by-construction reuse is.

[**Quick start**](#quick-start) &nbsp;·&nbsp; [**What a bundle is**](#what-makes-a-bundle-best-in-class) &nbsp;·&nbsp; [**The claim**](#the-claim-and-what-it-is-worth) &nbsp;·&nbsp; [**Library**](#what-is-in-the-library-today) &nbsp;·&nbsp; [**Quality gate**](#quality-gate) &nbsp;·&nbsp; [**Status**](#project-status)

<p>
  <img src="https://img.shields.io/badge/status-beta-yellow?style=flat-square" alt="Status: beta">
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-Apache--2.0-blue?style=flat-square" alt="License: Apache-2.0"></a>
  <img src="https://img.shields.io/badge/version-0.1.0-blue?style=flat-square" alt="Version 0.1.0">
  <a href="#what-is-in-the-library-today"><img src="https://img.shields.io/badge/bundles-12-brightgreen?style=flat-square" alt="Bundles: 12"></a>
  <a href="#what-is-in-the-library-today"><img src="https://img.shields.io/badge/Tier--1%20floor-11%20%2F%2027-orange?style=flat-square" alt="Tier-1 floor: 11 of 27"></a>
  <a href="#what-is-in-the-library-today"><img src="https://img.shields.io/badge/families-3-brightgreen?style=flat-square" alt="Families: 3"></a>
  <a href="#quality-gate"><img src="https://img.shields.io/badge/gate-11%20checks%20in%20CI-success?style=flat-square" alt="Gate: 11 checks in CI"></a>
  <a href="#the-claim-and-what-it-is-worth"><img src="https://img.shields.io/badge/real%20fills-0%20(honest)-lightgrey?style=flat-square" alt="Real fills: 0"></a>
</p>

The north star is simple and demanding: be the indisputable best-in-class reference implementation of a template library, not a folder of templates.

---

<details>
<summary><strong>Table of Contents</strong></summary>

- [Quick start](#quick-start)
- [What makes a bundle best-in-class](#what-makes-a-bundle-best-in-class)
- [The claim, and what it is worth](#the-claim-and-what-it-is-worth)
- [What is in the library today](#what-is-in-the-library-today)
- [Anatomy of a bundle](#anatomy-of-a-bundle)
- [How this fits with pm-skills](#how-this-fits-with-pm-skills)
- [Quality gate](#quality-gate)
- [Project status](#project-status)
  - [At a glance](#at-a-glance) · [Repository layout](#repository-layout) · [Design and roadmap](#design-and-roadmap)
- [Conventions](#conventions)
- [License](#license)
- [About the maintainer](#about-the-maintainer)

</details>

---

## Quick start

Six steps, start to finished document. No install, no tooling, no account.

**1. Get the library.**

```bash
git clone https://github.com/product-on-purpose/product-lifecycle-templates.git
cd product-lifecycle-templates
```

**2. Pick your document type.** One folder per type under [`templates/`](templates/). Not sure which? Open [`atlas/atlas.html`](atlas/atlas.html) in a browser, or read the one-line descriptions in [the table below](#what-is-in-the-library-today).

**3. Read the guide first. It takes a minute, and it is the highest-value minute.**

```bash
templates/prd/prd_guide.md
```

It tells you when this document is the right tool, when it is **not**, and the anti-patterns that most often wreck it. If the guide says do not use it, stop here: that is the guide working.

**4. Copy the variant you need into your own project.**

```bash
cp templates/prd/prd_template-lean.md ~/my-project/docs/my-feature-prd.md
```

**Default to `lean`.** Reach for `full` only when the cost of being wrong is high (hard to reverse, crosses teams, carries security or regulatory weight). Variants nest by design, so a document can grow from lean to full by adding sections, with nothing re-authored.

**5. Fill it in. The guidance is already in the file.**

Each section carries an HTML comment with what it wants, why it matters, guiding questions, a strong-versus-weak example, and the anti-pattern to avoid. It is visible while you write and invisible when the document renders. Stuck on *why* a section exists? The comment deep-links into the companion (`templates/prd/prd_companion.md`). Want to see one finished? Every bundle ships a real worked example (`prd_example.md`).

**6. Delete the guidance comments, and ship.**

Strip the `<!-- ... -->` blocks once each section is written. Keep the `source_template` and `source_template_version` frontmatter: it is how anyone (including you, in six months) can tell where the document came from and which version of the shape it used.

> **Filling one with an agent?** Point it at the bundle folder, not just the template. The `_guide.md` tells it when the type applies; the `_example.md` shows it what good looks like. To pick the right bundle in the first place, an agent reads [`manifest.json`](manifest.json), the machine catalog of every bundle's selectable fields (phase or classification, family, tags, sizes, aliases), generated from the metas and kept fresh by the gate. What is not yet possible is *installing* the library as a unit; see [The claim](#the-claim-and-what-it-is-worth).

<p align="right">(<a href="#readme-top">back to top</a>)</p>

---

## What makes a bundle best-in-class

Each document type produces one **bundle**. The blank template is only one file in it. The bundle is what earns trust:

- **Dual-reader by design.** A deep `companion` explains what the artifact is, where it came from, and where serious practitioners disagree, with tiered, hyperlinked citations. A short `guide` answers "should I use this here, and how do I not blow it" in under a minute. Neither makes the other reader wade through material they did not come for.
- **Sized to context.** Every type ships a `lean` and a `full` variant under a strict nesting rule: the lean template's sections are an ordered subset of the full one's, so a document grows in place without a re-author.
- **Guidance where you write.** Each section of a blank template carries an HTML-comment block: what it wants, why it matters (deep-linked to the companion), guiding questions, a strong-versus-weak example drawn from the real worked instance, and the one anti-pattern that most often wrecks it. Visible while you fill, gone when it renders.
- **Traceable.** Filled documents carry provenance frontmatter (`source_template`, `source_template_version`), and each bundle names the skill it `pairs_with`, so the library speaks the same language as the tools that fill it.
- **Researched, not remembered.** Every non-obvious claim in a companion carries a numbered, reliability-tagged citation (`[primary]` / `[practitioner]` / `[vendor]`). One entry, one source. A source that is paywalled, blocked, or a print book says so **in the reference itself**, and nothing is quoted that was not fetched and compared word for word.

| It is | It is not |
|---|---|
| **A governed bundle** - template, companion, guide, example, metadata, per type | A folder of blank Markdown files |
| **Researched and cited** - every non-obvious claim sourced and reliability-tagged | Remembered from training data |
| **Sized to context** - lean and full variants that nest, so documents grow in place | One heavy template you cut down by hand |
| **Honest about its edges** - each guide names when *not* to use the type | A confident claim that you always need this doc |
| **Gate-enforced** - a CI check blocks a bundle that breaks the rules | A style guide nobody runs |
| **Honest about coverage** - [`STATE.md`](STATE.md) outranks this README and is kept honest | Marketing that inflates what is done |

The full authoring process, the citation standard, and the per-bundle Definition of Done live in the methodology: [`templates/methodology.md`](templates/methodology.md).

<p align="right">(<a href="#readme-top">back to top</a>)</p>

---

## The claim, and what it is worth

The pitch above is the ambition. Here is the same thing with the credit separated from the cash, which is the fastest way to judge whether this library is worth your time:

- **Earned today.** Researched, dual-reader, nesting-disciplined, provenance-stamped bundles, with citations verified against raw sources and every correction recorded in the open. A gate that runs in CI and blocks merges. Decision records for every non-obvious choice.
- **Mostly earned now: "agent-native".** The machine layer landed 2026-07-17. Every bundle's metadata validates against a published schema in CI ([`tools/meta.schema.json`](tools/meta.schema.json), gate check J, [ADR 0016](docs/internal/decisions/0016-adopt-machine-checkable-metadata-schema.md)), and [`manifest.json`](manifest.json) exposes every bundle's selectable fields as structured data an agent reads instead of parsing prose, regenerated and freshness-checked by the gate ([ADR 0018](docs/internal/decisions/0018-machine-catalog-generated-manifest.md)). **What is still on credit is installability**: per decisions D2/D3 (resolved 2026-07-17), the library is **not installable via `npx skills add` nor listable on agentskills.io**, because both take exactly one unit, the *skill*, and this repo ships no `SKILL.md`. That is one missing file, not an architecture problem, and it is scheduled ([roadmap LP-2](docs/internal/roadmap.md)).
- **Still on credit: "reference implementation".** Twelve of 205 catalog types (11 of the 27 Tier-1 floor), and **zero fills by anyone but the author**. By the catalog's own tier rule (a type graduates when it "survives one real usage cycle"), nothing here has graduated.

If that reads harsher than a README usually does, that is the point: [`STATE.md`](STATE.md) is the source of truth, it outranks this file, and it is kept honest on purpose.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

---

## What is in the library today

<!-- bundle-count: 12 -->
**Twelve bundles, in three families.** Status `beta`: every one is gate-green and researched, and none has been filled in anger by anyone but the author.

### `delivery-docs` (six bundles, the family complete)

Their examples chain on one fictional "Saved Views" feature, so the family reads as one traceable set: a PRD leads to user stories, ordered in a product backlog and pulled into a sprint backlog, which lead to acceptance criteria, which ship in a release note.

| Bundle | What it is | Pairs with |
|---|---|---|
| [`prd`](templates/prd/) | Product Requirements Document: what to build, for whom, and why | `deliver-prd` |
| [`user-stories`](templates/user-stories/) | User-centered stories that anchor work to user value | `deliver-user-stories` |
| [`product-backlog`](templates/product-backlog/) | The ordered, goal-anchored list of work the team draws from | (none exists yet) |
| [`sprint-backlog`](templates/sprint-backlog/) | One sprint's forecast of work, drawn from the product backlog | (none exists yet) |
| [`acceptance-criteria`](templates/acceptance-criteria/) | The conditions that confirm a story is done | `deliver-acceptance-criteria` |
| [`release-notes`](templates/release-notes/) | The customer-facing announcement of a release | `deliver-release-notes` |

### `decision-docs` (three bundles, the family complete)

Three distinct jobs, deliberately kept separate: an **RFC** proposes a decision, an **ADR** records it, and an **SDD** describes how the thing gets built.

| Bundle | What it is | Pairs with |
|---|---|---|
| [`rfc`](templates/rfc/) | The proposal circulated *before* a decision, to gather input | (none exists yet) |
| [`adr`](templates/adr/) | The record of a decision *after* it is made, in [MADR v4](https://github.com/adr/madr) | `develop-adr` |
| [`sdd`](templates/sdd/) | The software design document: how a system will be built, before the code | (none exists yet) |

### `governance-docs` (three bundles, the family complete)

The first family gated on the `classification` axis rather than a lifecycle phase: standing governance instruments a PM maintains across the whole lifecycle. Their examples chain on one program (Reporting Platform Modernization) and interlock: the register tracks **threats**, the RAID log tracks **open items**, the dashboard tracks **whether the delivered program works**.

| Bundle | What it is | Pairs with |
|---|---|---|
| [`risk-register`](templates/risk-register/) | The maintained, owned record of risks to an objective, scored and reviewed | (none exists yet) |
| [`raid-log`](templates/raid-log/) | One log for the four kinds of open item: Risks, Assumptions, Issues, Dependencies | (none exists yet) |
| [`kpi-dashboard`](templates/kpi-dashboard/) | The definition of the KPIs that show whether objectives are being met | (none exists yet) |

Beyond these twelve, the library is completing its **Tier-1 "must-have" floor** (the 27 core types) from a researched catalog of 205 artifact types across 19 categories ([ADR 0021](docs/internal/decisions/0021-complete-the-tier-1-floor.md)). Grow-**by-pull** governs Tier-2 and Tier-3: specialized and regulated types are built when a real team asks for one, not speculatively.

> *A word on "complete".* A family being complete means its members are built, gate-green, and contract-validated, not that they are proven. A citation pass on 2026-07-16 found **28 defects across the original four delivery-docs bundles**, every one of which had been passing the gate green for weeks. They are verified *now*, against raw sources, with the corrections recorded in each bundle's research log. What the gate can and cannot prove is stated under [Quality gate](#quality-gate).

### The map: Product Artifact Atlas

[`atlas/atlas.html`](atlas/atlas.html) is a self-contained, interactive map of all 205 catalog types. Group them by category or lifecycle phase; filter by tier and by state; open any type to see its purpose, owner, methodology, and relationships. It doubles as a scoping tool: seeing the whole territory makes choosing what to build next a deliberate act rather than a guess. Open the file in any browser.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

---

## Anatomy of a bundle

A bundle is a folder named by document type (for example `prd/`), containing eight files:

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

<p align="right">(<a href="#readme-top">back to top</a>)</p>

---

## How this fits with pm-skills

This library is the sibling of a skills repository. The division is clean: **a skill teaches an agent how to produce an artifact; a template is the artifact itself.** The two form a loop: a skill decides how to shape a document, the template is what gets filled, and the filled document feeds the next skill. The `pairs_with` field in each bundle's metadata is the seam that joins them. (It is also honest: most bundles read `(none exists yet)` because the matching skill has not been built.)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

---

## Quality gate

The governance is enforceable, not aspirational. [`tools/check-bundles.py`](tools/check-bundles.py) runs **eleven structural checks** from the methodology's Definition of Done across every bundle in one command: the eight files are present; no em-dash or en-dash characters appear; the lean variant nests inside the full one (comparing heading *level* as well as text); the worked example has no leftover placeholders; citations resolve **in both directions**; the declared sizes match the files on disk and the meta carries no unfilled placeholder; every YAML block parses; the history documents the version the meta claims; `pairs_with` / `related_templates` point at things that exist; every meta validates against the [metadata schema](tools/meta.schema.json) (`phase` XOR `classification`, legal enums, no stray fields); and each bundle conforms to its [family contract](docs/internal/contracts/) (the family's axis value, status, and size shape).

```bash
python tools/check-bundles.py     # the eleven bundle checks
python tools/test-check-k.py      # the family-contract check's own test suite
python tools/gen-manifest.py --check   # manifest and README count are fresh
python tools/check-links.py       # every relative link and anchor resolves
```

All twelve bundles currently pass. GitHub Actions runs these on every push to `main` and every pull request ([`.github/workflows/ci.yml`](.github/workflows/ci.yml)), and `main` is branch-protected on the gate, so a bundle that breaks these checks cannot merge.

> **Scope, stated honestly, because this is the claim most worth distrusting.** The gate automates roughly **half** the methodology's Definition of Done. The research-tracing, guidance-comment-structure, companion-skeleton, guide-structure, and history-content clauses have no automation and are human-verified.
>
> More pointedly: **the gate proves a citation *resolves*, never that the source *supports the claim*.** In July 2026 a manual pass against raw sources found 28 defects across four bundles that had been green for weeks, including two wrong dates, two quotations from sources that could not be read at all, and several claims attributed to authors who do not make them. Every one was invisible to this script and always will be. **A green run means the structure holds, not that the content is true.** Current coverage always lives in [`STATE.md`](STATE.md).

<p align="right">(<a href="#readme-top">back to top</a>)</p>

---

## Project status

`v0.1.0` - **public and building out.** The library is completing its Tier-1 floor one family at a time, with a maintainer review at each family boundary. [`STATE.md`](STATE.md) is the single source of truth and outranks every plan and this README.

### At a glance

|  |  |
|---|---|
| **Current version** | [v0.1.0](CHANGELOG.md) |
| **Bundles** | 12, across 3 complete families (delivery-docs, decision-docs, governance-docs) |
| **Tier-1 floor** | 11 of the 27 "must-have" types built ([ADR 0021](docs/internal/decisions/0021-complete-the-tier-1-floor.md)) |
| **Catalog** | 205 researched artifact types across 19 categories ([`docs/internal/catalog.md`](docs/internal/catalog.md)) |
| **Gate** | 11 checks in CI, plus link, manifest-freshness, and family-contract tests; `main` branch-protected |
| **Decision records** | 24 ADRs in [MADR v4](https://github.com/adr/madr) ([`docs/internal/decisions/`](docs/internal/decisions/)) |
| **Real usage** | 0 fills by anyone but the author (coverage is not validation) |
| **License** | [Apache-2.0](LICENSE) |

### Repository layout

```
templates/
  methodology.md            The authoring process and Definition of Done
  prd/                      \
  user-stories/              \
  product-backlog/            \
  sprint-backlog/              }  the delivery-docs family (8 files each)
  acceptance-criteria/        /
  release-notes/             /
  rfc/                      \
  adr/                       }  the decision-docs family (8 files each)
  sdd/                      /
  risk-register/            \
  raid-log/                  }  the governance-docs family (classification axis)
  kpi-dashboard/            /
tools/
  check-bundles.py          The governance gate (runs locally and in CI)
  test-check-k.py           The family-contract check's own test suite
  check-links.py            The link gate (no tracked file may link into _local/)
  gen-manifest.py           Generates manifest.json and checks README freshness
  known-skills.txt          Pinned skill IDs that pairs_with may name
atlas/
  atlas.html                Interactive map of all 205 catalog types
  catalog-data.json         The atlas dataset
docs/
  internal/
    decisions/              Architecture decision records (MADR v4)
    contracts/              Family contracts enforced by the gate
    roadmap.md              Milestones and work packages
    catalog.md              The 205-type master catalog
manifest.json               The machine catalog an agent selects a bundle from
STATE.md                    What is actually true today. Outranks every plan.
```

Note on the layout: lifecycle phase (or classification) is carried in bundle metadata, never in the path, so `templates/` is flat by document type rather than nested by phase. That is deliberate: a type's phase can be reassigned without renaming anything ([ADR 0009](docs/internal/decisions/0009-scaffold-graduation-flat-templates.md)).

### Design and roadmap

The thinking behind the library is documented, not implicit:

- [`strategy-brief_catalog-to-template-library.md`](docs/internal/strategy/catalog-to-template-library.md) - the approach and the resolved architecture decisions.
- [`implementation-plan_catalog-to-template-library.md`](docs/internal/plan.md) - the phased plan and acceptance criteria.
- [`template-library-design-spec.md`](docs/internal/design-spec.md) - the formal specification.
- [`buildout-plan.md`](docs/internal/buildout-plan.md) and [`buildout-specs.md`](docs/internal/buildout-specs.md) - the Tier-1 floor build-out plan and per-type specs.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

---

## Conventions

- **Placeholders** are `{{snake_case}}` everywhere, so a generator or agent can find substitution points deterministically.
- **Reference IDs carry a human-readable handle**, never a bare code.
- **No em-dash or en-dash characters** anywhere in the library (an organization-wide house rule, enforced repo-wide in CI).
- **Every non-obvious choice is a decision record.** If you want to know why something is the way it is, read the [ADRs](docs/internal/decisions/).

<p align="right">(<a href="#readme-top">back to top</a>)</p>

---

## License

Distributed under the **[Apache License 2.0](LICENSE)**. You may use this library commercially, modify and redistribute it, use it privately, and include it in proprietary software; the only requirements are attribution and including the license notice. Copyright Jonathan Prisant.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

---

## About the maintainer

<a href="https://github.com/jprisant"><img src="https://img.shields.io/badge/Maintained_by-Jonathan_Prisant-blue?style=for-the-badge&logo=github" alt="Maintained by Jonathan Prisant"></a>

Built and maintained by **Jonathan Prisant** ([@jprisant](https://github.com/jprisant)). This library is the artifact sibling to [`pm-skills`](https://github.com/product-on-purpose/pm-skills) and [`thinking-framework-skills`](https://github.com/product-on-purpose/thinking-framework-skills): the skills decide *what* to do and *how* to shape a document, and this library is the document that gets filled.

<p align="center">
  <strong>Built with purpose by <a href="https://github.com/product-on-purpose">Product on Purpose</a></strong><br>
  <sub>Governed, self-describing templates a human or an agent can actually trust</sub>
</p>

<div align="right"><a href="#readme-top">Back to top ↑</a></div>
