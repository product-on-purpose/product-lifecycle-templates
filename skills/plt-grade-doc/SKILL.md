---
name: plt-grade-doc
description: Grades and reviews a product document that already exists against the researched rubric for its own document type, returning an itemized report card that quotes the document's own text as evidence, names the anti-patterns it hit, and lists the three fixes worth an hour. Use when someone asks for a review, a critique, a quality check, a second opinion, or a score on a PRD, user stories, acceptance criteria, an ADR, an RFC, a software design document, a test plan, a test case, a bug report, a risk register, a RAID log, a KPI dashboard definition, OKRs, a product vision, strategy or roadmap, a business case, a user persona, a definition of done, a runbook, an incident postmortem, retrospective notes, a status report, a backlog, or release notes.
license: Apache-2.0
metadata:
  version: "0.5.0"
  updated: 2026-09-03
  category: documentation
  author: product-on-purpose
  status: experimental
---
<!-- product-lifecycle-templates | https://github.com/product-on-purpose/product-lifecycle-templates | Apache 2.0 -->

# Grade a product document

**This skill reverses the usual direction.** [`plt-fill-template`](../plt-fill-template/SKILL.md) goes from
a blank template to a document. This one goes from a document someone already wrote to a report card
against that document type's own researched rubric.

<!-- counts: bundles=27, tier1=25 -->
The rubrics come from the same 27 bundles, covering all 25 templatable Tier-1 document types plus two Tier-2 types.

Nobody has to adopt anything to use this. That is the point: a critique of a document that already exists
costs the reader nothing but the reading.

## When to use

- Someone wants a document **reviewed, critiqued, scored, or sanity-checked** before it circulates.
- Someone is **about to send a PRD to engineering** and wants to know what a reviewer will ask.
- Someone wants to know **whether their document is missing something** that this type usually carries.
- An agent has just produced a document and should check it before handing it over.

## When NOT to use

- **The document does not exist yet.** Use [`plt-fill-template`](../plt-fill-template/SKILL.md).
- **The reader wants the document rewritten.** This produces a critique and a fix list. Rewriting the
  author's content is out of scope unless they ask for it after seeing the report.
- **The document is not one of the 27 types.** Say so and offer a structure-only review. Grading a
  strategy memo against the PRD rubric produces confident nonsense, and forcing the nearest bundle is the
  specific failure this library rejected two candidate types to avoid.
- **The reader wants a verdict on whether the underlying idea is good.** The rubric grades the document,
  never the decision inside it.

## How to use it

### 0. Confirm the library is present, and STOP if it is not

**This skill is a wrapper. The rubrics it grades against are not inside it.** Whether they are on disk
depends entirely on how this skill was installed:

| Install route | What you have |
|---|---|
| **Claude Code plugin** | the whole repository. Everything below works |
| **`npx skills add`** | this file, its README and its references. **No bundles, no `manifest.json`** |

**Before doing anything else, check that `manifest.json` is readable.**

**If it is not, fetch what you need (next section) or stop.** Do not grade from memory. A report card
produced without the guide is an opinion wearing a rubric's clothes, and it is worse than declining
because the letter grade makes it look measured.

### 0b. If the library is absent, fetch only what you need

Fetch from the tag matching this skill's own `metadata.version`, so the rubric you grade against is the one
this skill was written against:

```
https://raw.githubusercontent.com/product-on-purpose/product-lifecycle-templates/v<metadata.version>/manifest.json
https://raw.githubusercontent.com/product-on-purpose/product-lifecycle-templates/v<metadata.version>/templates/<type>/<type>_guide.md
```

**Two requests.** The manifest to detect the type with, and the guide to grade against. Add
`<type>_template-lean.md` only if the structure layer needs the section list and the guide does not carry
it.

**If the network is unreachable too, stop and say the library is unavailable.** Do not substitute for it.

### 1. Detect the document type

In this order, stopping at the first that resolves:

1. **An explicit type from the reader.** Always wins.
2. **`source_template` or `doc_type` in the document's frontmatter.** A document produced by this library
   carries its own provenance.
3. **Alias and tag match** on the document's title and headings against `manifest.json`, whose `aliases`
   field carries what practitioners actually call each type ("decision record" for `adr`,
   "cost-benefit analysis" for `business-case`).
4. **Heading fingerprint.** Match the document's H2 set against each bundle's template section list.

**Below confidence, ask. Never guess silently.** Present the top two candidates with one distinguishing
question. A silently wrong type produces a fluent report card that grades the document against the wrong
standard, which is the worst output this skill can produce: it is wrong and it looks careful.

**If genuinely nothing fits**, say so, offer a structure-only review, and record the miss. An unmatched
document is a demand signal for a type the catalog has not built, and it is worth more than a forced grade.

### 2. Assemble the rubric, and check which form it is in

Load the bundle's `<type>_guide.md`. Take from it:

- the **quality rubric**,
- the **named anti-patterns** (almost every guide carries a `Named anti-patterns` section),
- the **variant scope**, which says which rows apply to which variant.

**The guides carry two rubric forms, and the difference changes what may be claimed.** Detect the form by
looking at the rubric section, never by remembering a list of bundles:

| Form | How to recognise it | What the guide gives you |
|---|---|---|
| **Scored table** | a table whose header row is the criterion number, the criterion, and columns `0`, `1`, `2` | numbered criteria, cell text for each of 0, 1 and 2, **and a pass threshold stated in the sentence above the table** |
| **Checklist** | `- [ ]` items under the rubric heading | criteria only. **No scale and no threshold** |

**The 0/1/2 scale this skill applies to a checklist rubric is this skill's, not the guide's.** Say so in
the report card. The library has an open decision on whether to convert the checklist guides to the scored
form, and it deliberately refuses to convert them mechanically; the decision and its reasoning are in
[`guide-rubric-spec.md`](../../docs/internal/guide-rubric-spec.md) section 4, item 2. Applying an
unratified reading is allowed here **only because the report card states it and routes it there**, which is
[decision procedure 5](../../docs/internal/decision-procedures.md).

### 3. Analyse in three layers

**Layer 1, structure.** Which lean sections are present, which are missing, and whether any full-only
sections appear. The second half matters as much as the first: it tells the author whether they are writing
at lean or full posture, and whether that posture fits the stakes of the document.

**Layer 2, quality per rubric criterion.** Score each criterion 0, 1 or 2.

> **Every score below 2 must quote the document's own text, or state plainly that the thing is absent.**
> This is not a style preference. A criticism with no quote behind it is the defect this library's own
> review process catches most often, and shipping it inside a document whose whole job is to critique
> would be that defect committed on purpose.

**Score only the rows that apply to the variant in front of you.** Several guides carry a scope table
saying which rows are scored against which variant; `okrs` is the clearest example, scoring rows 7 to 9
only against `full` because the lean variant ships none of those sections. Scoring a lean document on
full-only rows penalises the choice of variant rather than the quality of the document. The library fixed
that defect on the authoring side and it must not be reintroduced here.

**Layer 3, anti-patterns.** Test each named anti-pattern from the guide, and each `TRAP` line from the
template's guidance comments if the template is on disk. **Report only hits, each with the offending
quote.** A clean anti-pattern sweep is one line, not a table of absences.

### 4. Compute the grade

| Component | Weight | How |
|---|---|---|
| Structure | 40 | lean sections present and in order |
| Rubric quality | 50 | points scored over points available on the rows that apply |
| Anti-patterns | up to -10 | penalty per hit |

Bands: **A** at 90+, **B** at 75+, **C** at 60+, **D** at 40+, **F** below.

**These bands are this skill's, and they are arithmetic rather than researched.** They exist so the report
is shareable. **The itemized table is the real product**, and the report card says so.

**Where the guide states its own threshold, report it separately and in the guide's own words**, attributed
to the guide. Do not merge it into the band, and do not restate it as this skill's claim: several of those
threshold sentences predict a consequence, the library has them flagged as unsourced, and a family-wide
rewording is already scheduled.

### 5. Render the report card

The format is in [`references/report-card-format.md`](references/report-card-format.md) and a real one is
in [`references/worked-example.md`](references/worked-example.md). The rules that are not negotiable:

- **Critique the document, never the author.** No sentence in the output has a person as its subject.
- **Lead with one genuine strength**, quoted. If there is genuinely none, say that instead of inventing one.
- **Three fixes in the headline, maximum.** The table carries the rest.
- **Every criticism quotes the document or names an absence.**
- **The frontmatter carries the scale's provenance**, so a screenshot of the card cannot lose it.
- **End with the upgrade path**: which bundle, which variant, and what adopting it would have caught.

### 6. Capture the feedback (EV-3)

After delivering the report, ask the five questions in
[`references/feedback-form.md`](references/feedback-form.md) and write the answers to
[`evals/usage-log/`](../../evals/usage-log/) if the repository is on disk.

**Store the type, the date and the scores. Never store the document.** If the repository is not on disk,
ask anyway and give the reader the entry to send back; the CLI install route has nowhere to write.

**This is the only route by which this library learns anything from a real user**, which is why it is a
step and not an afterthought.

## Edge cases

| Case | Behaviour |
|---|---|
| Unknown or hybrid type | Top two candidates, one distinguishing question. If nothing fits, decline the letter grade, offer a structure-only review, record the miss as catalog demand |
| Under about 150 words | **No letter grade.** Return the lean section checklist annotated present or absent |
| Very long document | Analyse section by section; cap quoted evidence per section |
| Already template-derived | Note version drift if `source_template_version` differs from the graded template. Grade normally |
| Sensitive content | State plainly: the document is not retained, and the usage log stores type, date and scores only |
| Not in English | Grade structure normally. Say that the rubric's quality judgments are calibrated on English exemplars |
| Guide has no rubric at all | Structure and anti-patterns only. No band. Say which is missing |

## Two places this deviates from its own build spec, and why

Recorded here rather than only in a commit message, because a reader of the skill cannot see the commit.

1. **The skill is `plt-grade-doc`, not `grade-doc`.** The spec predates
   [ADR 0036](../../docs/internal/decisions/0036-library-prefix-and-skill-under-skills.md), which took the
   `plt-` prefix and requires a skill's `name` to match its directory.
2. **Checklist rubrics are scored on a scale this skill supplies.** The spec assumed every guide carries a
   0/1/2 rubric. Eleven of the twenty-seven do not as of 2026-09-02, after `acceptance-criteria` converted,
   and whether the rest follow is an open decision the library has deliberately left open. **Detect the form from the guide in front of you, not from that
   count**, which nothing gates. Handled under
   [decision procedure 5](../../docs/internal/decision-procedures.md): state the rule in the artifact that
   applies it, and route the resolution to the document that owns it.

## What this proves, and what it does not

**Not proved by anything, and stated because a grader that overclaims is worse than no grader:**

- **No rubric in this library has been shown to predict document quality.** Of four efficacy runs, three
  returned **VOID**; the valid fourth, on 2026-09-03, covers two scenarios of one bundle and found **no
  measurable difference** in whether a reader could answer their questions from the document. The
  2026-08-08 runs returned **VOID** twice: templates scored well above a strong control on the
  bundles' *own* rubric criteria and no better than it on criteria drawn from neither the template nor the
  guide. The results are in [`evals/results/`](../../evals/results/). **A grade from this skill is a
  measurement against a researched standard, not evidence that the document will work.**
- **A high grade is not a good document, and a low grade is not a bad one.** The rubric can only see what
  is on the page. It cannot see whether the problem is real, whether the numbers are true, or whether
  anyone will read it.
- **Nobody outside the library's author has used this.** Coverage and real usage are separate numbers here,
  and the second one is still zero.
- **The checklist-form bundles are graded on an unratified scale.** See section 2.

**What is enforced**, by CI on every push: the rubric this skill reads is gate-checked for scope, so no row
grades a variant against a section that variant does not ship; every citation in the guide behind it is
anchored; and no example reuses its own template's guidance text.

## Where to go next

- [`references/report-card-format.md`](references/report-card-format.md) - the output format, field by field
- [`references/worked-example.md`](references/worked-example.md) - a real report card, from the first run against a document nobody wrote to this rubric
- [`references/grading-procedure.md`](references/grading-procedure.md) - the detailed procedure, type detection to scoring
- [`references/feedback-form.md`](references/feedback-form.md) - the five EV-3 questions and the log entry shape
- [`plt-fill-template`](../plt-fill-template/SKILL.md) - the other direction: blank template to document
- [`STATE.md`](../../STATE.md) - what is true of this repository today, and it outranks every other document
