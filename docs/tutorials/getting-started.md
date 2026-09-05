---
title: "Getting started"
description: "Pick a template bundle, fill it, and self-grade the result in about fifteen minutes"
audience: "both"
level: "beginner"
tags:
  - tutorial
  - onboarding
  - templates
---

# Getting started

This is a library of researched document templates for product management and software delivery, not a
folder of blank forms. Every document type ships as a **bundle**: the fill-in-the-blank template plus the
research, guidance, and worked example that make it fast to fill well. Fifteen minutes from here, you
should have picked a template, filled it, and know whether you did it well.

## What a bundle is, and why there are eight files

Pick any folder under [`templates/`](../../templates/) and you get eight files, not one. Using
[`templates/prd/`](../../templates/prd/) (Product Requirements Document) as the running example:

| File | What it is for |
|---|---|
| `prd_template-lean.md` | The blank shape, minimum useful |
| `prd_template-full.md` | The blank shape, comprehensive (a strict superset of lean) |
| `prd_companion.md` | The deep explainer: what a PRD is, why it is shaped this way, cited sources |
| `prd_guide.md` | The one-minute operator card: when to use it, when not to, a quality rubric |
| `prd_example.md` | A real worked instance, fully filled, no placeholders |
| `prd_meta.yaml` | Machine-readable catalog metadata: phase, family, sizes, what skill it pairs with |
| `prd_history.md` | The changelog for this bundle, by template version |
| `prd_research-log.md` | The evidence trail: every source this bundle relied on, and its reliability tier |

The template, `prd_template-lean.md` or `prd_template-full.md`, is the file you actually edit. It is also
the smallest part of the bundle. The other seven files exist so you do not have to guess: whether this is
even the right document, how much of it to fill in, what "good" looks like, and where a section's
guidance came from. A template with no companion is a shape with no reason attached to it; this library's
bet is that the reason is worth shipping alongside the shape.

## The fastest path

Six steps, using PRD as the example. Any bundle under [`templates/`](../../templates/) follows the same
shape, so once you have done this once you can repeat it for any type in the library.

**1. Get the library.**

```bash
git clone https://github.com/product-on-purpose/product-lifecycle-templates.git
cd product-lifecycle-templates
```

**2. Open the guide first.** Before touching the template, read
[`templates/prd/prd_guide.md`](../../templates/prd/prd_guide.md). It is short by design: when to use a PRD,
when *not* to (for example, if the problem is still unvalidated, do discovery first), and the six
anti-patterns that most often wreck one. If the guide tells you this is the wrong document, stop there.
That is the guide doing its job, not a dead end.

**3. Copy the lean template into your own project.**

```bash
cp templates/prd/prd_template-lean.md ~/my-project/docs/my-feature-prd.md
```

**4. Fill it in.** Every section carries its own guidance as an HTML comment directly above the blank
space: what the section wants, why it matters, a question to ask yourself, a strong example and a weak
one, and the specific trap that most often ruins that section. The comment is visible while you write and
disappears when the document renders, so you are never filling a section blind.

**5. Self-grade against the rubric.** `prd_guide.md` ends with a checklist, for example "the problem
section is meatier than the solution section" and "there is a primary success metric and a guardrail
metric, defined before build." Run down it before you call the document done.

**6. Delete the guidance comments and ship.** Strip every `<!-- ... -->` block once its section is
written. Keep the `source_template` and `source_template_version` fields in the frontmatter: they are how
anyone, including you in six months, can tell which shape the document came from.

## Lean or full: how to choose

Every bundle ships at least two sizes, and the full variant's sections are always an ordered superset of
the lean one's: nothing is renamed or reordered between them, so a lean document grows into a full one by
adding sections, never by rewriting what is already there.

**Default to lean.** Reach for full only when getting it wrong would be expensive: the decision is hard
to reverse, it crosses teams, or it carries real regulatory or safety weight. For a PRD specifically,
`prd_guide.md` puts it this way: lean is for a single feature, a spike, or an early idea, worked solo or
by a small team; full is for multiple teams, external dependencies, or a launch with real downside.

You are not locked into your first choice. Because full strictly extends lean, you can start lean and add
the missing sections later without re-authoring anything you already wrote.

## Read the example before the template

[`templates/prd/prd_example.md`](../../templates/prd/prd_example.md) is a complete, fully filled PRD for a
fictional "Saved Views" feature: real-shaped prose, a stated problem with evidence, explicit non-goals, a
primary metric and a guardrail, all the way through. No placeholders, no lorem ipsum.

Reading the example first is usually faster than reading the blank template first, for the same reason a
worked example in a textbook teaches faster than the blank exercise: it shows you the *shape of a good
answer*, not just the shape of the question. Once you have seen a filled Problem section, the guidance
comment on your own blank Problem section reads as confirmation rather than instruction.

## What to do next

- **Not sure which document type you need?** Open [`atlas/atlas.html`](../../atlas/atlas.html) in a browser.
  It is a self-contained, interactive map of every artifact type this library's research catalog covers,
  filterable by lifecycle phase and by whether a template has been built. Or skim the family tables in
  [`README.md`](../../README.md#what-is-in-the-library-today), grouped by what stage of the lifecycle each
  document type belongs to.
- **Filling a bundle with an agent, not by hand?** Point the agent at the bundle folder, not just the
  template file. `_guide.md` tells it when the type applies; `_example.md` shows it what good output
  looks like. To choose the right bundle in the first place, an agent can read
  [`manifest.json`](../../manifest.json), the machine-readable catalog of every bundle's selectable fields
  (phase, family, tags, sizes, aliases).
- **Want to know why a bundle is shaped the way it is, beyond what the guide says?** Read its
  `_companion.md`. Every non-obvious claim in a companion carries a numbered, source-tagged citation, and
  `_research-log.md` lists every source the bundle drew on.
- **Curious how much of the library is actually built, and how honestly?** Read [`STATE.md`](../../STATE.md)
  first. It is the single source of truth for this repository and outranks this document, the README, and
  every roadmap file when any of them disagree.

## What this library has not proven yet

<!-- counts: bundles=27 -->
Twenty-seven bundles exist today, and the Tier-1 "must-have" floor this library set out to build is
complete: <!-- counts: tier1=25 -->all 25 templatable Tier-1 document types the catalog names are built.
Every one of them is gate-green: [`tools/check-bundles.py`](../../tools/check-bundles.py) checks structure,
citation resolution, size nesting, and metadata schema conformance on every push.

None of that is the same claim as "these templates work." **Zero of these bundles have been filled in
anger by anyone but the library's author.** Efficacy was measured for the first time on 2026-08-08 and
returned **VOID** twice; a third run on 2026-08-21 was also void. The fourth, on **2026-09-03**, is the
first that cleared every validity gate, and it covers **two scenarios of the `prd` bundle only**. On those
two it found the template worth about a point of structural completeness against its own criteria and
**nothing measurable** on whether a reader could answer their questions from the document. That is a
narrow, honest result, not evidence that a lean PRD beats a blank page, and there is still no completed
real usage cycle. The
gate proves a bundle's structure holds and its citations resolve; it cannot prove the guidance inside a
bundle is right, only that nobody has changed the underlying facts without the check noticing. If you fill
one of these templates for a real project, you will be doing something this library has not yet had done
to it. [`STATE.md`](../../STATE.md) tracks this honestly and is worth reading before you trust any claim here
more than it has earned.
