# Spec: LP-2 Grade-My-Doc (the adoption wedge)

- **Status:** proposed | **Roadmap:** WP-30 (M3) | **Effort:** M-L | **Closes:** the D-05 (zero usage) path; the audit-endorsed top-of-funnel
- **One line:** paste a document you already have; get a specific, evidence-quoted report card against the library's rubric for that document type, plus the upgrade path to the template.

## 1. Purpose and strategic role

Most teams will not start from a blank template, but every team will accept a critique of a document they already wrote. LP-2 reverses LP-1: instead of template-to-document, it runs document-to-rubric. Each grading session (a) demonstrates the rubric's value, (b) sells the template as the fix for the gaps found, (c) produces an EV-3 feedback record, and (d) doubles as the library's first real usage cycle. The report card is deliberately shareable (Play 4 in 13_excellence-and-innovation.md): its output is the marketing.

## 2. Packaging decision (and the D2 side effect)

Ship as a skill IN THIS REPO: `skills/grade-doc/SKILL.md` (+ `references/` for the grading procedure). Two reasons: the rubrics it consumes live here and version together with it; and the moment this repo contains a SKILL.md, the open D2 question (does the skills CLI install a template-only repo) becomes moot for the primary channel, because the repo is no longer template-only. Re-test the CLI install after shipping (M3 acceptance criteria).

## 3. Inputs and outputs

- **Input:** document text (pasted or file path); optional `doc_type` hint; optional `strictness` (default: standard; `launch-review` grades against full-variant expectations).
- **Output:** a report card (markdown, format in section 5) plus, on request, a fix-it patch list (specific edits, not rewrites).

## 4. Flow

1. **Type detection.** In order: explicit hint; `doc_type` in the document's frontmatter; alias-index match on title/headings; heading-fingerprint match against each bundle's section list (from the section schema when built, else template H2s). Confidence below threshold: present the top two candidates with one distinguishing question, never guess silently.
2. **Rubric assembly.** Load the bundle's `_guide.md` (quality rubric + named anti-patterns), the template section lists (lean and full), and the TRAP lines from the template comments (they are per-section anti-pattern probes).
3. **Three-layer analysis.**
   - **Structure:** which lean sections are present/missing (completeness floor); which full-only sections are present (tells the author whether they are writing at lean or full posture and whether the posture fits the document's apparent stakes).
   - **Quality per rubric item:** score 0/1/2 per guide rubric line; every score below 2 must quote the document's own text as evidence (or state "absent").
   - **Anti-patterns:** test each named anti-pattern and each TRAP; report only hits, with the offending quote.
4. **Grade computation.** Weighted: structure 40 percent (lean sections present, correctly ordered), rubric quality 50 percent, anti-pattern penalty up to 10 percent. Bands: A at 90+, B at 75+, C at 60+, D at 40+, F below. The band exists for shareability; the itemized table is the real product.
5. **Report render** (section 5), ending with the upgrade path: link to the bundle, which variant fits, and what adopting it would have prevented.
6. **EV-3 capture.** After delivery, ask the five-question feedback form (usefulness 1-5; most valuable finding; anything wrong or unfair; would you use the template; may we log this anonymously). Store under `evals/usage-log/` with date and doc type, never the document itself.

## 5. Report card format (normative)

```markdown
---
graded_against: prd (template_version 0.1.0)
grader: grade-doc v0.1
date: {{date}}
grade: B
---
# Report card: {{doc_title}} (PRD)

**Verdict:** a strong problem statement undermined by unmeasurable goals and a missing
non-goals list. Grade: B (structure 9/10, quality 21/30, anti-patterns: 1 hit).

**Keep doing:** {{one genuine strength, quoted}}.

**Three fixes worth an hour:**
1. {{fix, actionable, points at a section}}
2. ...
3. ...

## Section by section
| Section | Present | Score | Evidence |
|---|---|---|---|
| Problem | yes | 2/2 | "..." |
| Goals and non-goals | partial | 0/2 | goals listed; no non-goals ("scope-creep insurance" per the guide) |

## Anti-patterns detected
- **Solution-as-problem** (guide anti-pattern 2): "Users cannot save filters" states a missing feature, not the underlying problem.

## If you want the full checklist
This grading used [templates/prd/prd_guide.md]. The blank template with per-section
guidance is [templates/prd/prd_template-lean.md]; your document is at lean scope,
sections {{missing}} short of the lean shape.
```

Tone rules (normative): critique the document, never the author; every criticism quotes the document or names an absence; lead with one genuine strength; three fixes maximum in the headline (the table carries the rest); no rewriting the author's content unless asked.

## 6. Edge cases

| Case | Behavior |
|---|---|
| Unknown/hybrid type | Offer top-2 candidates with one question; if genuinely none fit, decline the letter grade and offer a structure-only review; log the miss as catalog demand signal |
| Very short input (under ~150 words) | No letter grade; return the lean section checklist annotated present/absent |
| Very long input | Analyze by section against the schema; cap quoted evidence per section |
| Document already template-derived (provenance frontmatter present) | Note version drift if graded template_version differs; grade normally |
| Sensitive content | State plainly: content is not retained; the usage log stores type, date, scores only |
| Non-English | Grade structure normally; note that rubric quality judgments are calibrated on English exemplars |

## 7. Acceptance criteria

- [ ] Grades a never-seen PRD, user-story set, acceptance-criteria set, and release note end to end; wall-clock under 3 minutes each.
- [ ] Every sub-2 score in the output carries a quote or an explicit absence statement (spot-check 100 percent in review).
- [ ] Type detection: 9 of 10 on a mixed test set of 10 real documents; the misses degrade to the candidate question, never a silent wrong grade.
- [ ] Report card renders correctly on GitHub and in Slack paste.
- [ ] EV-3 capture fires and writes the usage log entry.
- [ ] The skills-CLI install test is re-run post-ship and the outcome recorded against D2.

## 8. Dependencies and references

Hard: none (guides and templates exist). Better with: manifest.json + alias index (WP-22, type detection), section schema (WP-53, structure layer). References: audit findings D-05, E-04, F-01; G6 idea LP-2; report tone per Google developer documentation style guide.
