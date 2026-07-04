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

The full authoring process, the citation standard, and the per-bundle Definition of Done live in the methodology: [`_local/templates/methodology.md`](_local/templates/methodology.md).

---

## What is in the library today

**The `delivery-docs` family is complete.** All four bundles are researched, enriched, cross-linked, and verified. Their examples chain on one fictional "Saved Views" feature, so the family reads as one traceable set (a PRD leads to user stories, which lead to acceptance criteria, which ship in a release note).

| Bundle | What it is | Pairs with |
|---|---|---|
| [`prd`](_local/templates/prd/) | Product Requirements Document: what to build, for whom, and why | `deliver-prd` |
| [`user-stories`](_local/templates/user-stories/) | User-centered stories that anchor work to user value | `deliver-user-stories` |
| [`acceptance-criteria`](_local/templates/acceptance-criteria/) | The conditions that confirm a story is done | `deliver-acceptance-criteria` |
| [`release-notes`](_local/templates/release-notes/) | The customer-facing announcement of a release | `deliver-release-notes` |

Beyond these four, the library grows **by pull** from a researched catalog of 205 artifact types across 19 categories. The "must-have core" is built first; specialized and regulated types are built when a real team asks for one, not speculatively.

### The map: Product Artifact Atlas

[`_local/atlas/atlas.html`](_local/atlas/atlas.html) is a self-contained, interactive map of all 205 catalog types. Group them by category or lifecycle phase; filter by tier and by state; open any type to see its purpose, owner, methodology, and relationships. It doubles as a scoping tool: seeing the whole territory makes choosing what to build next a deliberate act rather than a guess. Open the file in any browser.

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

The working library currently lives under `_local/` (a provisional home; the final directory scaffold is a deliberate, deferred decision, since lifecycle phase is carried in metadata rather than the path).

```
_local/
  templates/
    methodology.md            The authoring process and Definition of Done
    prd/                      \
    user-stories/              }  the delivery-docs family (8 files each)
    acceptance-criteria/       }
    release-notes/            /
  atlas/
    atlas.html                Interactive map of all 205 catalog types
    catalog-data.json         The atlas dataset
  initial-discovery/docs/     Strategy briefs, implementation plan, design spec, catalog
```

---

## Design and roadmap

The thinking behind the library is documented, not implicit:

- [`strategy-brief_catalog-to-template-library.md`](_local/initial-discovery/docs/strategy-brief_catalog-to-template-library.md) - the approach and the resolved architecture decisions.
- [`implementation-plan_catalog-to-template-library.md`](_local/initial-discovery/docs/implementation-plan_catalog-to-template-library.md) - the phased plan and acceptance criteria.
- [`template-library-design-spec.md`](_local/initial-discovery/docs/template-library-design-spec.md) - the formal specification.
- [`strategy-brief_raising-the-ceiling_2026-07-02.md`](_local/initial-discovery/docs/strategy-brief_raising-the-ceiling_2026-07-02.md) - where the library goes next: proving quality with evals, closing the usage loop, and serving templates to agents.

---

## Quality gate

The governance is enforceable, not aspirational. [`_local/tools/check-bundles.py`](_local/tools/check-bundles.py) runs the structural checks from the methodology's Definition of Done across every bundle in one command: the eight files are present, no em-dash or en-dash characters appear, the lean variant nests inside the full one, the worked example has no leftover placeholders, every cited companion reference resolves to its anchor, and the declared sizes match the files on disk.

```
python _local/tools/check-bundles.py
```

All four delivery-docs bundles currently pass. This is a local prototype of the continuous-integration gate planned for the repository.

## Conventions

- **Placeholders** are `{{snake_case}}` everywhere, so a generator or agent can find substitution points deterministically.
- **Reference IDs carry a human-readable handle**, never a bare code.
- **No em-dash or en-dash characters** anywhere in the library (an organization-wide house rule).

## License

Apache-2.0.
