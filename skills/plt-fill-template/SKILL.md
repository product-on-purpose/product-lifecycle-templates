---
name: plt-fill-template
description: Selects and fills a researched product-document template from a 26-bundle library covering the full product lifecycle, then grades the result against that document type's own rubric. Use when writing a PRD, user stories, acceptance criteria, a risk register, a RAID log, a KPI dashboard definition, a test plan, a test case, a bug report, an ADR, an RFC, a software design document, a product vision, strategy, roadmap, OKRs, a business case, a user persona, a definition of done, a runbook, an incident postmortem, sprint retrospective notes, a status report, a product or sprint backlog, or release notes. Each bundle carries a lean and a full variant, a worked example, and the research log every claim traces to.
license: Apache-2.0
metadata:
  version: "0.4.0"
  updated: 2026-08-08
  category: documentation
  author: product-on-purpose
  status: experimental
---
<!-- product-lifecycle-templates | https://github.com/product-on-purpose/product-lifecycle-templates | Apache 2.0 -->

# Product lifecycle templates

A library of **26 researched document-template bundles**, covering the complete Tier-1 floor of a 205-type
product-artifact catalog. It is not a folder of blank forms. Each bundle carries the research behind its
shape, a worked example, and a rubric for judging the result.

<!-- counts: bundles=27, tier1=25 -->
27 bundles, spanning all 25 templatable Tier-1 document types plus two Tier-2 types.

## When to use

- Someone needs to **write** a product document and wants a shape that is defensible rather than invented.
- Someone has **written** one and wants it graded against something better than taste.
- An agent needs to **select** a document type from a description of a job to be done.

## When NOT to use

- **The document already exists and only needs editing.** Use [`plt-grade-doc`](../plt-grade-doc/SKILL.md),
  which grades an existing document against the bundle's rubric and returns a report card; do not restart
  from the template.
- **The type is not in the library.** The catalog holds 205 types and only the Tier-1 floor is built. If
  nothing matches, say so rather than forcing the nearest bundle. Bending an adjacent type to fit is the
  specific failure this library rejected two candidate types for.
- **You need the document filled with facts you do not have.** These templates prompt for evidence. They
  do not supply it.

## How to use it

### 0. Confirm the library is present, and STOP if it is not

**This skill is a wrapper. The 27 bundles it indexes are not inside it.** Whether they are on disk
depends entirely on how this skill was installed:

| Install route | What you have |
|---|---|
| **Claude Code plugin** | the whole repository. Everything below works |
| **`npx skills add`** | this file and its README. **No bundles, no `manifest.json`** |

**Before doing anything else, check that `manifest.json` is readable.**

**If it is not, STOP and say so.** Tell the reader the library is not installed alongside the skill, and
offer the two options in the next section.

**Do not proceed from memory. Do not write a document that resembles what a template might have asked
for.** A fluent document produced without the bundle is exactly the artifact this library exists to
replace, and delivering one under this library's name is worse than declining. The library's own eval
measured what that looks like: a template filled with confident generic prose scored **1.00 out of 5**
and answered **zero of five** retrieval probes.

### 0b. If the library is absent, fetch only what you need

Two files, not a repository. This skill's whole design is that an agent loads **one** bundle file.

Fetch from the tag matching this skill's own `metadata.version`, so the templates you read are the ones
this skill was written against:

```
https://raw.githubusercontent.com/product-on-purpose/product-lifecycle-templates/v<metadata.version>/manifest.json
https://raw.githubusercontent.com/product-on-purpose/product-lifecycle-templates/v<metadata.version>/templates/<type>/<type>_template-<size>.md
```

That is **two requests**: the manifest to select with, and the one template you chose. Add the guide
only if you are grading or choosing a variant.

**If you cannot reach the network either, stop.** Say the library is unavailable rather than
substituting for it.

### 1. Select

Read `manifest.json` at the repository root. It is generated from every bundle's metadata and is the
selection surface: `id`, `title`, `summary`, `doc_type`, `family`, `phase` or `classification`,
`sizes_available`, `default_size`, `sizing_guidance`, `status`, `tags`, `aliases`, and an `approx_tokens`
estimate **per size variant** so context can be budgeted before anything is loaded.

Match on `doc_type`, `aliases` or `tags`. If several match, `summary` distinguishes them.

### 2. Choose a size

Most bundles ship `lean` and `full`. `sizing_guidance` in the manifest says when each applies. Some ship
only `lean`, because the research found no second weight in circulation; that is a finding, not an omission.

**Default to lean.** Full exists for the cases the guide names, not as the better version.

### 3. Load only what you need

Each bundle is eight files (seven if single-size). An agent normally loads **one**:

| File | Load it? |
|---|---|
| `<type>_template-lean.md` or `_template-full.md` | **Yes.** This is the artifact |
| `<type>_guide.md` | When grading, or choosing a variant |
| `<type>_example.md` | When the shape is unclear. Often faster than reading the template |
| `<type>_companion.md` | Rarely. Deep background for humans, and the largest file |
| `<type>_research-log.md` | Only to check a claim's provenance |
| `<type>_meta.yaml`, `_history.md` | Almost never. Already summarised in `manifest.json` |

### 4. Fill it

Every section carries a guidance comment in a fixed, parseable shape:

```
WHAT   what the section is
WHY    why it exists, ending in a pointer to the companion
ASK    two to four questions that produce the content
GOOD   an illustration of a filled section
WEAK   an illustration of a bad one, and why
TRAP   the specific mistake this section invites
```

These are HTML comments and strip on render. **`GOOD` and `WEAK` deliberately use a different scenario
from the worked example**, so the two teach shape and substance separately.

Placeholders are `{{snake_case}}`. If a section does not apply, **say so in one line rather than deleting
it** - a reader cannot tell a deleted section from one nobody thought about.

### 5. Grade it

Every guide ends with a rubric: numbered rows scored 0, 1 or 2, with a stated threshold and what falls
below it. Grade honestly; the rubric asks for evidence you can point at, not for counts you can inflate.

## What this library proves, and what it does not

Stated plainly, because a template library claiming more than it has earned is worth less than one that
does not.

**Enforced by CI, on every push and pull request:** 25 steps, including an 11-check gate per bundle - all
files present, no em-dash or en-dash, lean nests strictly inside full, no unfilled placeholder in any
example, every citation anchored and none padded, metadata valid against a schema, and conformance to the
bundle's family contract. Separately: every relative link resolves, every research log carries a
per-source retrieval status, no worked example cites a sibling dated later than itself, and no example
reuses its own template's guidance text.

<!-- counts: cisteps=25, logsgated=21, sourcesgated=826 -->
25 CI steps; 21 research logs gated, covering 826 sources.

**Not proved by anything:**

- **Template quality was measured on 2026-08-08, and the measurement was inconclusive.** Two blinded
  runs over three of the twenty-six bundles then in the library both returned **VOID**: the templates score well above a strong
  generic-prompt control on the bundles' *own* rubric criteria, and no better than it on
  decision-usefulness criteria drawn from neither the template nor its guide. Read the results before
  quoting anything from them, in [`evals/results/`](../../evals/results/). **No number from either run
  is a quality claim, and none may be repeated without linking the protocol's stated limits.**
- **No template here has been filled by anyone but the author.** The catalog's own rule gates Tier 2 on
  "survives one real usage cycle", so by the library's own standard nothing has graduated.
- **The gate proves structure, never that a citation supports its claim.** That is what the four-lens
  review is for, and a review is not a machine.

Every bundle's status is `beta` for those reasons.

## The research standard, in one paragraph

Every source in every research log carries one of exactly three tokens: `fetched-and-verified` (the page
body was read, **and only these may be quoted**), `url-confirmed-not-read`, or `not-retrieved`. A source
that was not fetched may support the existence of a topic and never a specific claim about it. Where a
statistic could not be traced to a method, the bundle says so instead of citing it. Several bundles' most
useful findings are absences: the word "timeline" appears zero times in the SRE chapter everyone cites for
postmortems, and the 2020 Scrum Guide contains no occurrence of "action item".

## Where to go next

- [`docs/getting-started.md`](../../docs/tutorials/getting-started.md) - fill your first template in fifteen minutes
- [`docs/choosing-a-template.md`](../../docs/reference/choosing-a-template.md) - from a job to be done to a bundle
- [`docs/filling-a-template.md`](../../docs/how-to/filling-a-template.md) - the fill loop in detail
- [`docs/what-the-gate-proves.md`](../../docs/explanation/what-the-gate-proves.md) - the honest scope of the quality claim
- [`AGENTS.md`](../../AGENTS.md) - the machine-consumption path
- [`STATE.md`](../../STATE.md) - what is true of this repository today, and it outranks every other document
