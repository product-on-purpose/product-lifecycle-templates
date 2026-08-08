---
title: "Filling a template"
description: "The loop that takes a copied blank template to a document you would ship"
audience: "both"
level: "intermediate"
tags:
  - how-to
  - authoring
  - variants
  - rubric
---

# Filling a template

You have picked a document type, opened its folder under [`templates/`](../../templates/), and copied
the variant you need into your own project. This page is the next step: the loop that gets you from
that blank file to a document you would actually ship.

If you have not done this before, [`docs/getting-started.md`](../tutorials/getting-started.md) walks the whole path
end to end in about fifteen minutes; this page goes deeper on the fill loop specifically. If you have
not chosen a bundle yet, [`docs/choosing-a-template.md`](../reference/choosing-a-template.md) turns "what am I trying
to do" into a bundle name, and [`atlas/atlas.html`](../../atlas/atlas.html) maps the whole catalog. Each
bundle's own `_guide.md` states when its type applies and, just as important, when it does not; if the
guide tells you not to use this type here, that is the guide working, not a wrong turn on your part.

## Read the worked example first

Before you write a single word into the template, open the bundle's `_example.md`. For the PRD bundle
that is [`templates/prd/prd_example.md`](../../templates/prd/prd_example.md); every bundle has one at the
same place, named `<type>_example.md`.

This is worth doing even though it feels like the slow way in. The example and the guidance comments
inside the template are meant to do two different jobs, on purpose. The comments under each heading
(covered below) show you the shape of one section at a time: a short, isolated strong illustration, a
short weak one, and the trap that produces the weak one. The example is supposed to show you the
substance independently of those hints: a complete, real document where every section has to work
together and carry one consistent story, filled by someone who is not simply restating the comment
underneath each heading. That independence is a named convention here, not just a hope: the library's
gate runs a check
([`tools/check-example-independence.py`](../../tools/check-example-independence.py)) specifically to catch
an example that turns out to be a template's own GOOD or WEAK snippets reworded, because that has
shipped here before and it teaches a reader nothing they had not already read once. The check catches
verbatim reuse; it cannot catch the same point paraphrased in different words, and it says so in its own
header, so treat a green run as "no copy-paste was caught," not as proof the example is teaching
something new. A number of bundles also chain their examples across a shared fictional program
(delivery-docs, governance-docs, and qa-docs, among others, follow one "Saved Views" feature and one
"Acme Analytics" program), so reading a family's examples in order shows you how one document's output
becomes the next one's input, on top of showing you one document done well. No `{{placeholder}}` remains
in a shipped example, and any number that is not real data is labeled "illustrative" rather than
presented as fact.

Read the comments for guidance on any one section. Read the example for what "done" looks like as a
whole.

## What is in the file you copied

Open the template file and you will find two layers before any real content. First, YAML frontmatter
with placeholder values: a title, an owner, a status, dates, and two fields worth protecting,
`source_template` and `source_template_version`. Those two say which bundle this document came from
and which version of its shape it used, which is how you (or an agent, or a teammate six months from
now) can tell where a document originated. Fill in the other frontmatter fields; keep these two as
they are.

Second, a "HOW TO FILL THIS IN" preamble, sitting in one HTML comment right after the frontmatter. It
is short and it is the same four steps in every bundle: read each section's guidance comment, replace
the placeholders, write "N/A" plus one line rather than deleting a section that does not apply, and
self-grade against the guide before you delete every comment and ship. Everything below expands on
those four steps.

## The guidance comments

Every section of every template carries an HTML comment directly under its heading. It is invisible
once the document renders (an HTML comment never displays), but it is the actual teaching, and it is
why filling one of these templates is a different experience from filling a blank Google Doc titled
"PRD". Each comment carries the same labeled fields, in the same order:

- **WHAT** the section wants, in a line or two.
- **WHY** it matters, ending with a pointer into the bundle's `_companion.md` for the deeper reasoning
  (for example, "Deep dive: prd_companion.md section 3"). The companion is where the research and the
  citations live; the template only carries the distilled version.
- **ASK** two to four questions to answer while you write, so you are not staring at a blank
  placeholder wondering where to start.
- **GOOD** a short, realistic strong example, usually drawn from that bundle's own worked example.
- **WEAK** the same thing done badly, with a parenthetical naming why it falls short.
- **TRAP** the single anti-pattern most likely to wreck that section specifically.

A table-shaped section (a risk register's Risks table, a test plan's rows) adds two more fields in
place of GOOD and WEAK prose: **PRIORITY**, the legend for a scoring or ordering column, and **ROW
HINT**, what a well-formed row contains, illustrated with a strong and a weak row.

Read the comment before you write the section, not after. It is written to be read first.

## Placeholders

Every fill-in point in every template is written `{{snake_case}}`, so a person or an agent can find
every substitution point in a file by pattern rather than by guessing which prose is a placeholder and
which is instruction. Replace each one with real content. A shipped, filled document has none left; the
bundle's own worked example is the proof that a fully replaced document is achievable and still reads
naturally.

## The N/A rule

If a section genuinely does not apply to what you are writing, do not delete it. Write "N/A" and one
line explaining why it does not apply, and leave the heading in place.

This is not a formality. A missing section and a considered "N/A" look identical to a script, but they
mean opposite things to a reader: one says nobody thought about this, the other says someone did and
decided it did not apply, here is why. The library's own gate cannot tell the difference between an
honest N/A and a deleted section (that judgment needs a human reader), so the discipline is yours to
keep. It is also the difference between a document a reviewer trusts and one they have to
cross-examine.

## Choosing and growing: lean, full, and when to move

Most bundles ship two sizes: `lean`, the minimum genuinely useful version, and `full`, a comprehensive
variant built as a strict superset. Every section in the lean template appears in the full one,
unchanged in name and order; the full variant only adds sections between them. That is what lets a
document grow from lean to full in place, by adding sections, with nothing already written re-authored
or reshuffled.

Default to lean. The README's own guidance is to reach for full only when the cost of being wrong is
high: the work is hard to reverse, it crosses teams, or it carries real security or regulatory weight.
The full template itself repeats the same instruction from the inside: do not pre-fill a full-only
section out of diligence. Add one the moment a real question it answers actually comes up, a
dependency appears, a non-functional requirement gets contested, a rollout needs a flag, not before.

A few bundles depart from the lean and full pattern in one of two ways worth knowing about before you
are confused by what you see on disk. A bundle with only one genuinely useful size, such as
`sprint-retrospective-notes`, ships `_template-lean.md` alone; there is no missing `full` file, the type
simply does not earn a second size. A handful of strategy-docs bundles, such as `product-vision`, ship
named formats (a canvas, a narrative, a PR/FAQ) instead of, or alongside, a size axis, because the
choice that matters for that type is which format fits the audience, not how much detail to include.
When a bundle does this, its `_guide.md` says so under "Pick a variant."

## Adapting a template without breaking it

You will sometimes want to add something a template does not have: an extra table column, an
org-specific compliance line, a section your team always wants. That is fine, and it does not require
permission. What you should not do is rename or reorder a section a template ships you, because that is
the one thing that breaks the nesting contract described above: it is what lets a lean document become
a full one later without a re-author, and it is what lets `source_template_version` mean something if
anyone ever compares your document against a newer version of the same bundle.

So: add sections freely, in the gaps the full variant already shows you (a full-only section can sit
anywhere among the lean ones), or appended at the end. Leave the sections you were given as they are,
in the order you found them, even when one of them ends up saying "N/A." If a bundle's type varies by
context in ways worth knowing (solo versus large team, a regulated setting, a different methodology's
conventions), that guidance lives in the companion's "Adaptations" section; read it before you improvise
your own tailoring.

## The self-grade rubric

Every `_guide.md` ends with a quality rubric: a short checklist you grade your own document against
before anyone else sees it. For the PRD bundle, that is a checklist like "the problem is stated from the
user's point of view, with evidence it is real," "there is a primary success metric and a guardrail,"
and "every guidance comment has been deleted, no placeholders remain." Each bundle's rubric is specific
to what makes that type succeed or fail; read the one in the bundle you are using rather than assuming
they are interchangeable.

Grade it honestly, which means checking each line against the actual document, not against your
intention when you wrote it. A checked box you cannot point to a sentence for is not a passed check. The
rubric is the fast version of the same standard the worked example was held to: no fabricated content,
no section that only looks filled in.

## Before you ship

Once every section is written and the rubric is honestly checked, delete every HTML comment in the
file: the preamble, and every WHAT/WHY/ASK/GOOD/WEAK/TRAP block under every heading. They are guidance
for the person filling the document, not content for the person reading it. Keep the `source_template`
and `source_template_version` frontmatter. What is left should read like an ordinary document in your
project, with no trace that it started as a template, except that it will be a better-shaped one than
most.

## What this cannot tell you

Everything above describes the mechanics of filling a template well: the comments, the rubric, the
nesting rule. None of it is a claim that a well-filled document produces a good outcome for your
product. This library has not been filled in anger by anyone but the author, so there is no track
record yet of these bundles being used on a real team's real work, and no evaluation of whether a
document that passes its own rubric performs any better than one that does not. The gate that runs in
this repository checks that a bundle's structure holds; it has no way to check that your filled-in
content is right, and [`docs/what-the-gate-proves.md`](../explanation/what-the-gate-proves.md) is the full, honest
account of that boundary. That judgment stays yours.

## Where to go next

- [`docs/getting-started.md`](../tutorials/getting-started.md) - the fifteen-minute path, start to finished document
- [`docs/choosing-a-template.md`](../reference/choosing-a-template.md) - from a job to be done to a bundle name
- [`docs/what-the-gate-proves.md`](../explanation/what-the-gate-proves.md) - what is enforced, what is argued, and what
  is not measured at all
- [`STATE.md`](../../STATE.md) - what is actually true of this repository today; it outranks every other
  document, including this one
