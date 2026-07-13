# product-lifecycle-templates

> The template layer that humans and AI agents both reach for first: governed, self-describing, sized to context, and traceable. Coverage is not the product; correct-by-construction reuse is.

A curated library of product-management and software-lifecycle document templates. Anyone can publish a folder of Markdown templates. What makes this one different is that every template ships as a **governed bundle**: a blank shape you fill in, a researched explainer of why it is shaped that way, a fast operator card, a fully worked example, and machine-readable metadata so an agent can select and fill it deterministically.

The north star is simple and demanding: be the indisputable best-in-class reference implementation of a template library, not a folder of templates.

---

## What makes a bundle best-in-class

Each document type produces one **bundle**. The blank template is only one file in it. The bundle is what earns trust:

- **Dual-reader by design.** A deep `companion` explains what the artifact is, where it came from, and where serious practitioners disagree, with tiered, hyperlinked citations. A short `guide` answers "should I use this here, and how do I not blow it" in under a minute. Neither makes the other reader wade through material they did not come for.
- **Sized to context.** Every type ships a `lean` and a `full` variant under a strict nesting rule: the lean template's sections are a subset of the full one's, in the same order, so a document can grow in place from lean to full without a re-author.
- **Guidance where you write.** Each section of a blank template carries an HTML-comment block with what it wants, why it matters (deep-linked to the companion), guiding questions, a strong-versus-weak example drawn from the real worked instance, and the one anti-pattern that most often wrecks it. The guidance is visible while you fill the template and vanishes when the document renders.
- **Traceable.** Filled documents carry provenance frontmatter (`source_template`, `source_template_version`), and each bundle names the skill it `pairs_with`, so the library speaks the same language as the tools that fill it.
- **Researched, not remembered.** Every non-obvious claim in a companion carries a numbered, reliability-tagged citation (`[primary]` / `[practitioner]` / `[vendor]`). Sources that could not be fetched directly are flagged honestly rather than dressed up.

The full authoring process, the citation standard, and the per-bundle Definition of Done live in the methodology: [`templates/methodology.md`](templates/methodology.md).

---

## What is in the library today

**The `delivery-docs` family is complete.** All four bundles are researched, enriched, cross-linked, and verified. Their examples chain on one fictional "Saved Views" feature, so the family reads as one traceable set (a PRD leads to user stories, which lead to acceptance criteria, which ship in a release note).

| Bundle | What it is | Pairs with |
|---|---|---|
| [`prd`](templates/prd/) | Product Requirements Document: what to build, for whom, and why | `deliver-prd` |
| [`user-stories`](templates/user-stories/) | User-centered stories that anchor work to user value | `deliver-user-stories` |
| [`acceptance-criteria`](templates/acceptance-criteria/) | The conditions that confirm a story is done | `deliver-acceptance-criteria` |
| [`release-notes`](templates/release-notes/) | The customer-facing announcement of a release | `deliver-release-notes` |

Beyond these four, the library grows **by pull** from a researched catalog of 205 artifact types across 19 categories. The "must-have core" is built first; specialized and regulated types are built when a real team asks for one, not speculatively.

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
tools/
  check-bundles.py          The governance gate (runs locally and in CI)
atlas/
  atlas.html                Interactive map of all 205 catalog types
  catalog-data.json         The atlas dataset
docs/
  decisions/                Architecture decision records
STATE.md                    What is actually true today. Outranks every plan.
```

Note on the directory layout: lifecycle phase is carried in bundle metadata, never in the path, so `templates/` is flat by document type rather than nested by phase. That is deliberate, and it means a type's phase can be reassigned without renaming anything. See [`docs/decisions/20260712-scaffold-graduation-flat-templates.md`](docs/decisions/20260712-scaffold-graduation-flat-templates.md).

---

## State, decisions, and roadmap

The thinking behind the library is documented, not implicit, and the honest current state is one file away.

- **[`STATE.md`](STATE.md)** is the single source of truth about what actually exists. It outranks every plan and brief in this repo, it lists what is deliberately *not* built, and it says plainly which of the front-door claims are earned and which are still on credit. If a document here disagrees with it, that document is wrong.
- **[`docs/decisions/`](docs/decisions/)** holds the architecture decision records: why bundles are named by document type, why templates ship lean and full under a strict nesting rule, why the research log is a shipped artifact, and what the governance gate is and is not.

The library grows **by pull**, not by speculation. The next family is built when a real team asks for one. What is coming, in order: verifiable citations and a first tagged release; a machine-readable metadata layer so an agent can select a bundle deterministically; then efficacy evaluations, so "best-in-class" becomes a measurement rather than an assertion.

That last one is the honest gap. Nothing here yet proves a template produces a better document than a good prompt does. Until it does, the claim is a hypothesis, and `STATE.md` says so.

---

## Quality gate

The governance is enforceable, not aspirational. [`tools/check-bundles.py`](tools/check-bundles.py) runs the structural checks from the methodology's Definition of Done across every bundle in one command: the eight files are present, no em-dash or en-dash characters appear, the lean variant nests inside the full one, the worked example has no leftover placeholders, every cited companion reference resolves to its anchor, and the declared sizes match the files on disk.

```
python tools/check-bundles.py
```

All four delivery-docs bundles currently pass. GitHub Actions runs this same script on every push to `main` and on every pull request ([`.github/workflows/ci.yml`](.github/workflows/ci.yml)), so a bundle that breaks these checks cannot merge.

Scope, stated honestly: the gate automates roughly **half** the methodology's Definition of Done. The research-tracing, guidance-comment-structure, companion-skeleton, guide-structure, and history-content clauses have no automation yet and are human-verified. "Enforceable, not aspirational" is true of what CI runs, and only of that. Current coverage always lives in [`STATE.md`](STATE.md).

## Conventions

- **Placeholders** are `{{snake_case}}` everywhere, so a generator or agent can find substitution points deterministically.
- **Reference IDs carry a human-readable handle**, never a bare code.
- **No em-dash or en-dash characters** anywhere in the library (an organization-wide house rule).

## License

Apache-2.0.
