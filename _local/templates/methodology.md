---
title: "Template Bundle Methodology: Researching and Drafting a Best-in-Class Template"
status: draft
doc_version: 0.2.0
owner: "{{owner}}"
last_reviewed: 2026-06-30
license: Apache-2.0
applies_to: "every bundle under templates/ (provisionally _local/templates/)"
related:
  - ../initial-discovery/docs/template-library-design-spec.md
  - ../initial-discovery/docs/strategy-brief_catalog-to-template-library.md
  - ../initial-discovery/docs/implementation-plan_catalog-to-template-library.md
  - ../initial-discovery/docs/deep-research_master-catalog.md
---

# Template Bundle Methodology

> **What this is.** The repeatable process that produces every template bundle in this library. It is the answer to "how do we make each one best in class, and how do we keep them consistent." Read it before authoring any bundle; follow it in order; do not skip the research phase.
>
> **Why it exists.** A template is cheap to copy and expensive to trust. The trust comes from two things this methodology enforces: the blank shape is genuinely well-formed, and the companion document that explains it is researched, cited, and honest. Without a fixed process, ten bundles drift into ten shapes and the library's only moat (governed quality) evaporates.

---

## 1. Principles

These govern every judgment call the process does not explicitly cover.

1. **Research before drafting.** No bundle is written from memory alone. Every document type is researched against current, authoritative sources first. Memory seeds the search; it does not replace it.
2. **Cite or cut.** Every non-obvious claim in the companion carries a numbered citation. A claim that cannot be sourced is either marked as the author's reasoned judgment or removed. No fabricated facts, no invented metrics, no imaginary citations.
3. **Source honesty.** Sources are tiered and tagged. A vendor blog and a standards body do not carry equal weight, and the reader is told which is which (see [§6](#6-citation-standard)).
4. **Recency is a feature.** Standards and conventions shift (IEEE 829 to ISO/IEC/IEEE 29119; FDA Part 820 to QMSR). Every bundle records when it was researched and flags claims with a known expiry.
5. **Dual-readable.** The blank template is clean for a human and parseable by an agent. Guidance lives in HTML comments that vanish on render. The companion serves a beginner and an expert in the same document without making either wade through the other's material (it is sectioned by reader need).
6. **Contested means contested.** Where authorities genuinely disagree (PRD vs prototype-as-spec; runbook vs playbook), the companion presents the disagreement, names the camps, and recommends. It does not flatten a real debate into a false consensus.
7. **Smallest useful default.** Bias the lean variant toward the minimum that is still genuinely useful. Structure is a cost; make the reader opt into more, not strip out excess.
8. **House style.** No emdash or endash characters anywhere (org-wide rule, CI-enforced). Reference IDs always carry a human-readable handle.

---

## 2. The Bundle (what we are producing)

One document type produces one **bundle**: a folder named by the document-type handle (e.g. `prd/`), containing seven files. The doc-type handle prefixes every filename so a file is self-identifying if it is moved or attached out of context. Phase is recorded in metadata, never in the path, so the eventual directory scaffold (flat, nested-by-phase, or other) stays a deferred, derivable choice.

| File | Role | Reader | Length guide |
|---|---|---|---|
| `<type>_template-lean.md` | The blank shape, minimum useful | author filling a quick doc | short |
| `<type>_template-full.md` | The blank shape, comprehensive (strict superset of lean) | author filling a thorough doc | medium |
| `<type>_companion.md` | The deep explainer: what it is, why, debates, exhaustive references | beginner learning + expert checking | long (2,000-5,000+ words) |
| `<type>_guide.md` | The operator card: when-to-use, quality rubric, anti-patterns | someone deciding fast | short |
| `<type>_example.md` | A real worked instance, no lorem, no fabricated metrics | author wanting a model to copy | medium |
| `<type>_meta.yaml` | The machine manifest (catalog meta) | the repo, CI, agents | short |
| `<type>_history.md` | Per-bundle changelog by `template_version` | maintainers | grows over time |

The companion and the guide are deliberately separate (Diataxis split: explanation/reference vs how-to). The companion is the stable, research-backed artifact; the guide is a short derivative of it.

---

## 3. Phase A: Research Protocol

Do this fully before writing any bundle file. Output is a research log you keep open while drafting.

### A1. Seed from the catalog

Start at the document type's entry in [`deep-research_master-catalog.md`](../initial-discovery/docs/deep-research_master-catalog.md). Capture its canonical name, aliases, lifecycle phase, owner, purpose, typical sections, methodology, formality, rarity, relationships, and named sources. This is the hypothesis, not the answer.

### A2. Build the source set (tiered)

Gather sources in priority order. Aim for breadth across tiers; do not rely on a single tier.

- **Tier 1, primary / authoritative:** standards bodies (IEEE, ISO, IEC, AICPA, NIST), regulators (FDA eCFR), the originating methodology source (Scrum Guide, SAFe framework, Basecamp's Shape Up, Amazon's Working Backwards, Google SRE books, PMBOK, IIBA BABOK), and the named originator of a specific artifact (Nygard for ADR, Osterwalder for BMC, Torres for opportunity solution trees, Moore for positioning).
- **Tier 2, established practitioner:** recognized authorities and their canonical writing (Marty Cagan / SVPG, Lenny Rachitsky, Teresa Torres, Reforge, Pragmatic Institute), well-regarded books and talks.
- **Tier 3, vendor / commercial:** tool vendors and their blogs (Atlassian, Aha!, ProductPlan, Notion, Figma; Vanta / Drata / Secureframe for compliance). Reliable on structure and convention, but commercially motivated. Use for "what teams actually do," corroborate claims of fact against Tier 1 or 2.

### A3. Live research sweep

Run real searches (do not work from memory). For each document type, establish:

- **Origin and evolution:** who introduced it, when, why; what it replaced or superseded; how it has changed.
- **Canonical structure:** the sections a strong version contains, and which are load-bearing vs optional.
- **Methodology lineage:** how different schools treat it (or reject it).
- **Live debates:** where practitioners actively disagree about its form, value, or boundaries.
- **Current status:** is it current, legacy, or being deprecated; any standard that recently changed it.
- **Relationships:** what it precedes, follows, and feeds.

### A4. Verification and the claim-citation rule

For every factual claim destined for the companion:

1. Find a source. Prefer the highest tier available for that claim.
2. If two reputable sources conflict, record both and treat it as a contested point (A5).
3. If no source can be found, either label the statement explicitly as the author's reasoned judgment, or cut it.
4. Quote sparingly and exactly; attribute every quote. Never paraphrase a source into a stronger claim than it makes.

### A5. Recency and contested-claim handling

- Record the research date in the companion and `meta.yaml` (`last_reviewed`).
- Flag any claim with a known expiry (a standard mid-transition, a regulation with a future effective date).
- For genuine disagreements, name the positions and their proponents; do not pick a winner silently.

### A6. Research log

Keep a running list of every source consulted with its URL, tier, and the claims it supports, as you go. This becomes the companion's reference section (no reconstructing citations from memory after the fact). A source you read but do not cite can be dropped; a claim you cite must trace to a logged source.

---

## 4. Phase B: Drafting Protocol

Draft the seven files in this order. Each draws on the research log.

### B1. The template variants (`_template-lean.md`, `_template-full.md`)

- **Lean** is the minimum genuinely useful version. **Full** is comprehensive and a **strict superset**: every lean section ID appears in full, unchanged in name and order; full only adds sections. This enables upgrade-in-place (a doc grows lean to full without a re-author).
- Add `s/m/l` (three weights) only where a type genuinely earns three distinct sizes; most earn two (lean/full). Let the type decide.
- **Instance frontmatter** at the top of each variant, with placeholder values (`{{snake_case}}`), including the provenance fields (`source_template`, `source_template_version`).
- **Section guidance** lives in HTML comments (`<!-- ... -->`) immediately under each heading, so it is visible to the author filling the template in an editor and strips cleanly on render, leaving a clean blank shape. Each section's comment carries these labeled fields (omit one only when it would be padding, not to save effort):
  - **WHAT** the section wants, in one or two lines.
  - **WHY** it matters, ending with a deep-link pointer into the companion by section (for example, `Deep dive: prd_companion.md section 3 (Anatomy > Problem)`).
  - **ASK** two to four guiding questions the author answers while writing.
  - **GOOD** a short, realistic strong example, drawn from this bundle's own worked example where possible.
  - **WEAK** the same thing done badly, with a parenthetical naming why it is weak.
  - **TRAP** the single anti-pattern most likely to wreck this section.
  For table sections, add **PRIORITY** (a legend for any priority column) and **ROW HINT** (what a good row contains), and give GOOD and WEAK as example rows.
- **A "How to fill this in" preamble** sits in the top HTML comment of each variant: read each section's comment, replace the placeholders, write "N/A" plus one line for an inapplicable section, and self-grade against the guide then delete all comments before shipping.
- **Placeholders** are `{{snake_case}}` everywhere, so a generator can find substitution points deterministically.

### B2. The companion (`_companion.md`)

The deep explainer. Use the fixed skeleton in [§5](#5-companion-document-structure). Write for two readers at once by sectioning: orientation and anatomy carry the beginner; lineage, debates, and references reward the expert. Every non-obvious claim is cited inline by number; the full reference list sits at the bottom.

### B3. The guide (`_guide.md`)

The operator card, derived from the companion. Three parts only: **when to use / when not to use**, a **quality rubric** (a short checklist or table the author can self-grade against), and **named anti-patterns** (the few mistakes that most often wreck this artifact). Short by design. It points to the companion for the why.

### B4. The example (`_example.md`)

A single, realistic, fully worked instance, filled end to end. No `{{placeholders}}` remain. No fabricated metrics or fake quotes; if illustrative numbers are needed, label them clearly as illustrative. It should read like a strong real document a team would be glad to copy.

### B5. Manifest and history (`_meta.yaml`, `_history.md`)

- `meta.yaml` carries catalog meta per the design spec: `id`, `title`, `summary`, `doc_type`, `phase` (lowercase), `family`, `sizes_available` (must match the variant files present), `methodology`, `pairs_with` (skill IDs, or null), `status`, `template_version`, `tags`, `related_templates`, `last_reviewed`, `license`.
- `history.md` opens with an entry for the current `template_version` and the research date.

---

## 5. Companion Document Structure

Every `_companion.md` follows this skeleton. Sections may scale, but all are present; an inapplicable section says so in one line rather than being dropped.

1. **Orientation + TL;DR.** One paragraph in plain language: what this artifact is and the one job it does. Then a 3-5 bullet at-a-glance for skimmers.
2. **Origins and evolution.** Where it came from, who introduced it, how it changed, what it replaced or superseded.
3. **Anatomy (section by section).** For each section of the template: what it is, why it exists, a beginner note (how to do it) and, where useful, an expert note (when to drop, expand, or distrust it).
4. **Variants and sizing.** Lean vs full, and the signal for scaling up.
5. **Methodology lineage.** How different schools treat the artifact (Scrum, SAFe, Shape Up, Amazon, Lean, design thinking, regulated), including those that reject or replace it.
6. **Debates and contested boundaries.** The live arguments about its form, value, and edges. Name the camps and proponents. Recommend, do not flatten.
7. **Anti-patterns and failure modes.** The recurring ways it goes wrong, beginner and subtle.
8. **Relationships to other artifacts.** What precedes, follows, and feeds it; the natural document lineage.
9. **Adaptations.** Regulated, org size, solo vs team, methodology-specific tailoring.
10. **Worked example pointer.** A one-line pointer to `_example.md` and what it demonstrates.
11. **References.** Exhaustive, numbered, reliability-tagged (see [§6](#6-citation-standard)).

---

## 6. Citation Standard

References live at the bottom of the companion, numbered, and are cited inline by their number (e.g. "Cagan argues the prototype should be the spec [4]").

**Format per entry:**

```
[n] Author or Organization. "Title." Publisher/site, year. URL (accessed YYYY-MM-DD). [tier-tag]
```

**Reliability tags** (the reader must be able to weigh a source at a glance):

- `[primary]` standards body, regulator, or the originating methodology/author source.
- `[practitioner]` recognized independent authority or canonical book/talk.
- `[vendor]` tool vendor or commercially motivated source; reliable on convention, corroborate claims of fact.

**Rules:**

- Every inline citation number resolves to exactly one reference entry.
- A quote carries the exact source and, where it matters, a locator (clause, page, section).
- Prefer the primary source over a secondary description of it (cite the Scrum Guide, not a blog summarizing it), unless the secondary source is itself the claim's origin.
- Do not pad the list with sources you did not actually use.
- **References are linked, not bare text.** Each entry begins with an anchor `<a id="ref-n"></a>`, and the source title is a Markdown hyperlink to its URL; the bare URL is dropped from the visible text. Internal sources link to their relative repo path where one exists.
- **Inline citations are clickable.** Write each inline `[n]` as `[[n]](#ref-n)` so it renders as a bracketed number that jumps to the matching entry.

---

## 7. Definition of Done (per bundle)

A bundle is done only when every item holds. This is the gate.

- [ ] **Research:** a research log exists; every companion claim traces to a logged source or is labeled author judgment.
- [ ] **Variants:** lean and full present (or the earned `s/m/l` set); section IDs nest (smaller is a strict subset of larger).
- [ ] **Placeholders:** `{{snake_case}}` consistently; none left in `_example.md`.
- [ ] **Guidance:** in HTML comments; strips cleanly on render; every section carries WHAT, WHY (with a companion deep-link), a GOOD and a WEAK example, and a TRAP (plus PRIORITY / ROW HINT for tables); a "How to fill this in" preamble is present.
- [ ] **Companion:** all 11 skeleton sections present; dual-reader; inline citations all resolve.
- [ ] **Guide:** when-to-use, quality rubric, and at least two named anti-patterns.
- [ ] **Example:** genuinely worked, no placeholders, no fabricated metrics.
- [ ] **References:** numbered, reliability-tagged, no orphan citations, no padded entries; each entry has an `<a id="ref-n"></a>` anchor and a hyperlinked title; every inline `[n]` is a working `[[n]](#ref-n)` jump.
- [ ] **Meta:** valid YAML; `sizes_available` matches variant files; `pairs_with` resolves to a known skill ID or is null.
- [ ] **History:** entry for the current `template_version` with research date.
- [ ] **House style:** zero emdash/endash; reference IDs carry handles.

---

## 8. End-to-End Checklist

Run a bundle through these steps in order.

1. **Seed** from the catalog entry (A1).
2. **Source** across tiers (A2).
3. **Sweep** with live research; build the research log (A3, A6).
4. **Verify** every claim; flag contested and time-bound points (A4, A5).
5. **Draft** the variants (B1).
6. **Write** the companion against the skeleton, citing as you go (B2, §5, §6).
7. **Derive** the guide (B3).
8. **Work** the example (B4).
9. **Fill** meta and history (B5).
10. **Gate** against the Definition of Done (§7). Fix until green.

---

## Appendix: Why two documents, not one

The companion and the guide answer different questions for different readers in different moods. The guide answers "should I use this here, and how do I not blow it" in under a minute. The companion answers "what is this, where did it come from, why is it shaped this way, and who disagrees" over a longer read. A single document serving both makes the hurried reader scroll through an essay and makes the essay carry a checklist it keeps tripping over. Separating them lets each be excellent at one job. The cost (two files, a little edge overlap) is small because the companion is stable once researched and the guide is a short projection of it.
