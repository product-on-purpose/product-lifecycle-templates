# A worked example: the first real grading run

**This is real output, not an illustration.** It was produced on 2026-08-19, the day this skill was built,
by running the procedure in `SKILL.md` by hand against a document that already existed.

**The document was deliberately not one of this library's own worked examples.** Grading those would be
circular: the example and the rubric were written by the same author, against each other, and a high score
would prove nothing. The document graded here is
[ADR 0039](../../../docs/internal/decisions/0039-maintainer-discretion-replaces-the-pull-gate.md), a real
decision record in this repository, written to **MADR v4 and the wider organization's scaffolding**, not to
this library's `adr` template. Nobody wrote it with this rubric in view.

**It scored C, and it found a defect nothing else had caught.** Both facts are why this example is worth
shipping.

---

## The report card

```markdown
---
graded_against: adr (template_version 0.1.0, full variant)
grader: plt-grade-doc 0.3.1
date: 2026-08-19
rubric_form: checklist
scale: grader (unratified; see guide-rubric-spec s4 item 2)
guide_threshold: none stated
grade: C
---

# Report card: "The maintainer may build any template; grow-by-pull becomes an input, not a gate" (ADR)

**Verdict:** an unusually honest decision record, carrying a named falsifier and a cost the author
plainly did not want to accept, and it loses most of its points on follow-through rather than on
reasoning: the record it amends was never updated to point at it. Grade: C (structure 32.5/40,
quality 21/26 scaled to 40.4/50, anti-patterns: 0 hits).

**Keep doing:** the record states the cost it is accepting rather than burying it. "If the maintainer
builds forty more bundles with zero users, nothing in this repository will stop it. The honest-numbers
discipline is a disclosure rule, not a brake."

**Three fixes worth an hour:**
1. **Update ADR 0021 to point here.** It is the record this one amends, its title still reads
   "grow-by-pull governs Tier-2 and Tier-3 only", and a reader landing on it gets the superseded rule
   with no forward pointer. This is the rubric's only zero.
2. **Add a Confirmation section, or say in one line that nothing enforces this.** The full variant
   ships one and this record omits it. The material is already in the document: "The labelling clause
   exists because of that risk, and it depends on being followed."
3. **Say which driver each rejected option fails.** The drivers are falsifiable and option A clearly
   fails two of them, but the record never draws the line, so the reader has to.

## Section by section

| Section | Present | Score | Evidence |
|---|---|---|---|
| Context and Problem Statement | yes | 2/2 | situational and dated: "The three intake templates in `.github/ISSUE_TEMPLATE/` shipped 2026-08-07 and have received zero issues" |
| Decision Drivers | yes | 1/2 | four drivers, all falsifiable, but no option is mapped to the driver it fails |
| Considered Options | yes | 2/2 | three options; "do nothing" is option A and is named as such: "a decision to build nothing further, made by inaction rather than on purpose" |
| Decision Outcome | yes | 1/2 | outcome is "Chosen: B" and the changes read passive: "A Tier-2 or Tier-3 bundle may be initiated" |
| Consequences | yes | 2/2 | two "Bad" bullets on the chosen option, not only on the rejected ones |
| Confirmation | no | 1/2 | no section; the honest statement exists but sits inside Consequences |
| Pros and Cons of the Options | partial | n/a | content is inline in Considered Options rather than in its own section |
| More Information | yes | 2/2 | links the amended record and its load-bearing clause |

## Rubric, criterion by criterion

| # | Criterion | Score | Evidence |
|---|---|---|---|
| 1 | Title names the decision | 2/2 | "The maintainer may build any template; grow-by-pull becomes an input, not a gate" |
| 2 | Context is situational, not the argument | 2/2 | opens with the standing rule and the tree's state, not the conclusion |
| 3 | Records conditions that could expire | 2/2 | "Zero people outside the author have used the library", plus a named falsifier at forty bundles |
| 4 | "Do nothing" appears | 2/2 | option A, and it is argued rather than listed |
| 5 | No straw men | 2/2 | both rejected options get substantive reasons |
| 6 | Active voice, human named | 1/2 | `decision-makers: [jprisant]` names a person; the outcome reads "Chosen: B" and the changes are passive |
| 7 | A real negative consequence | 2/2 | "nothing in this repository will stop it" |
| 8 | Chosen option has honest cons | 2/2 | three bullets against the chosen option |
| 9 | (Full) Drivers are falsifiable | 1/2 | drivers are falsifiable; no option-to-driver mapping is written |
| 10 | (Full) Confirmation names a check | 1/2 | "it depends on being followed" is honest, but there is no Confirmation section |
| 11 | Status correct, amended record updated | **0/2** | `status: accepted` is correct. **ADR 0021 contains no reference to 0039.** Verified by search |
| 12 | Filed at the right path, fresh number | 2/2 | `docs/internal/decisions/0039-maintainer-discretion-replaces-the-pull-gate.md` |
| 13 | No guidance comments or placeholders | 2/2 | zero occurrences of a placeholder or an HTML comment |

## Anti-patterns detected

**None.** All seven were tested. Approval theater, the CYA record, decision-without-alternatives and
all-upside consequences are the four this record most plausibly risked, and it clears each of them
explicitly rather than by accident.

## What this grade is, and is not

The 0/1/2 scale is this skill's, not the guide's: the `adr` guide carries a checklist rubric with no
scale and no threshold, and converting those guides is an open decision recorded in
`guide-rubric-spec.md` section 4, item 2. This grades the document against a researched standard. It
is not evidence that the decision inside it was right.

## If you want the full checklist

This grading used `templates/adr/adr_guide.md`. The blank template is
`templates/adr/adr_template-full.md`; this document is at full scope and is two sections short of the
full shape.
```

---

## What the run actually proved, and what it did not

**Proved.** The skill's first run against a real document found a defect nothing else in the repository
catches: **ADR 0021 was never updated to point at the record that amends it.** No gate checks
cross-references between decision records, `check-adr-index.py` checks the index rather than the links, and
the defect had stood since 2026-08-14. That is the case for a grader: it reads what checks cannot.

**The defect was fixed in the same change that shipped this skill**, so a reader checking ADR 0021 today
will find the pointer and should not conclude the report card was wrong. The card above is the grading as
it stood on 2026-08-19 before the fix, kept unedited, because a worked example rewritten to match a
later tree teaches nothing about what the grader actually did.

**Also proved, and less comfortable.** A carefully written record scored **C**. The two full-variant
sections it omits cost it 7.5 structure points, and the missing backlink cost it the rubric's only zero.
Whether a C is the right verdict on that document is exactly the kind of question the EV-3 form's third
question exists to surface.

**Not proved, and not claimed:**

- **This is one document, graded by hand, by the author of the skill.** It is a smoke test, not a
  measurement, and the blinding the efficacy harness uses is entirely absent here.
- **Nothing in the build spec's acceptance criteria has been run**, other than end-to-end grading of one
  document. The type-detection target of 9 of 10 on a mixed set, the wall-clock target, the Slack and
  GitHub rendering check, and the EV-3 write have all **not been run**, because each needs documents this
  repository does not have.
- **The band is arithmetic.** No research supports the weights or the cut lines, and a C here is not
  comparable to a C anywhere else.
