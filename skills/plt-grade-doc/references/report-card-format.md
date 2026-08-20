# The report card format

Normative. The report card is the product, and it is designed to be pasted into Slack, a pull request, or a
document comment without losing the things that keep it honest.

## Why the frontmatter carries the provenance

**A report card gets screenshotted.** The caveat that says which scale produced the grade is the first
thing a crop removes, and the letter is the last. So the scale's provenance is a structured field at the
top rather than a sentence at the bottom, and it is repeated in prose once.

## The shape

```markdown
---
graded_against: <type> (template_version <version>)
grader: plt-grade-doc <skill metadata.version>
date: <date>
rubric_form: scored-table | checklist
scale: guide | grader (unratified; see guide-rubric-spec s4 item 2)
guide_threshold: <the guide's own words, or "none stated">
grade: <A-F, or "not issued">
---

# Report card: <document title> (<Type>)

**Verdict:** one or two sentences. What the document does well, and the one thing that most
undermines it. Grade: B (structure 9/10, quality 21/30, anti-patterns: 1 hit).

**Keep doing:** one genuine strength, quoted from the document.

**Three fixes worth an hour:**
1. A specific, actionable fix that points at a named section.
2. ...
3. ...

## Section by section

| Section | Present | Score | Evidence |
|---|---|---|---|
| Problem | yes | 2/2 | "the quote from the document" |
| Goals and non-goals | partial | 0/2 | goals listed; no non-goals stated |

## Anti-patterns detected

- **Solution-as-problem** (guide anti-pattern 2): "Users cannot save filters" states a missing
  feature, not the underlying problem.

## What this grade is, and is not

One or two lines. Where the scale came from, and the standing limit: this grades the document
against a researched standard and is not evidence that the document will work.

## If you want the full checklist

This grading used `templates/<type>/<type>_guide.md`. The blank template with per-section guidance
is `templates/<type>/<type>_template-lean.md`; this document is at <lean|full> scope, <n> sections
short of the <variant> shape.
```

## Field rules

| Field | Rule |
|---|---|
| `rubric_form` | Read off the guide, never remembered. `scored-table` when the rubric is a numbered table with 0, 1 and 2 columns; `checklist` when it is `- [ ]` items |
| `scale` | `guide` only when `rubric_form` is `scored-table`. Otherwise `grader`, with the routing note, because the scale is unratified |
| `guide_threshold` | The guide's sentence, quoted, attributed. `none stated` for checklist guides. **Never paraphrased into a claim of this skill's own** |
| `grade` | `not issued` for a document under about 150 words, for a type that could not be identified, and for a guide with no rubric at all |

## The tone rules, restated because they are the part that gets dropped

1. **Critique the document, never the author.** No sentence in the output takes a person as its subject.
2. **Every criticism quotes the document or names an absence.** A score below 2 with no quote behind it
   does not ship.
3. **Lead with a genuine strength.** If there is none, say there is none. Do not manufacture one; a false
   compliment costs the rest of the card its credibility.
4. **Three fixes in the headline, maximum.** The table carries everything else.
5. **No rewriting.** The fix list says what to change and where. It does not produce the replacement text
   unless the reader asks after seeing the card.

## What must never appear in a report card

- A predicted outcome ("this will get approved faster"). Nothing in this library supports one.
- A score for a rubric row that does not apply to the variant in front of you.
- A quote the document does not contain. Every quoted string is copied, never reconstructed.
- The document's own content stored anywhere. The usage log takes type, date and scores only.
