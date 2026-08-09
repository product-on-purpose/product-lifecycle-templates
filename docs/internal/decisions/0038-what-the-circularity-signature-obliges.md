---
status: proposed
date: 2026-08-08
decision-makers: [jprisant]
consulted: [claude]
---

# What the circularity signature obliges, and why the eval cannot answer it

## TL;DR

- **Decision (proposed, not taken):** treat the measured circularity signature as a real finding about the
  bundles, and resolve it by deciding, per held-out criterion, whether the property belongs in the
  templates, in the guides and rubrics, or nowhere. **This record proposes the decision procedure and the
  evidence needed; it does not propose an edit to any template**, and it deliberately does not assert that
  the sources required to admit any of them exist.
- **Why:** two independent 114-agent runs agree that documents written with these templates score **+0.85**
  against criteria drawn from the templates' own guide and **-0.03**, an interval spanning zero, against
  decision-usefulness criteria drawn from neither. The library's own protocol names that pattern and says
  it gets acted on rather than buried.
- **Status:** **proposed 2026-08-08.** Nothing is adopted. Three of the four candidate properties would be
  cheap and uncontroversial; one is a genuine scope question that
  [ADR 0030](0030-templating-scope-markdown-documents.md)'s admission test, as written, **does not reach**.

## Context and Problem Statement

[The matched re-run](../../../evals/results/2026-08-08_matched-rerun.md) produced two numbers that sit beside
each other and mean something only together:

| Gap (matched arms) | Point | 95% interval | Reading |
|---|---|---|---|
| Rubric criteria, drawn from the templates' own guide | **+0.85** | +0.42 to +1.27 | Real, excludes zero |
| Held-out criteria, drawn from neither template nor guide | **-0.03** | -0.42 to +0.28 | Nothing, spans zero |

Both runs agree within 0.13 on every quantity. Judging noise is 0.14 between panels and 0.42 within one,
so the contrast is larger than the noise in one direction and smaller in the other, which is what makes it
readable rather than an artifact.

[The protocol](../eval-protocol.md) section 3 defines this exactly: *"A large rubric gap beside a
null held-out gap is the circularity signature. The treatment arm has read the answer key: it can win by
mentioning rubric items rather than by being better."*

**The templates move a document toward what they already ask for, and toward nothing else measured.** The
question this record exists to frame is what, if anything, that obliges.

## The four held-out criteria, and what each would actually cost

The held-out criteria are consistent across the three measured bundles, and their absence from each
template and guide was **searched for rather than assumed**, with the search recorded per criterion in
[`evals/rubrics/`](../../../evals/rubrics/). They are not four of a kind, and treating them as "three or four
new sections" would be wrong:

| Criterion | What it asks | What changing it would actually be |
|---|---|---|
| `no_internal_contradiction` | Nothing in the document contradicts anything else in it | **A rubric row and a guide anti-pattern.** Not a section. No template gains a heading. No scope question arises, because the document is not being asked to contain anything new. |
| `scopable_without_a_meeting` | A reader could size and sequence the work from this alone | **A rubric row.** Arguably already the implicit goal of several sections; what is missing is that nothing grades the document *as a whole* against it. |
| `decision_vs_input_traceable` | A reader can tell what the author decided from what the author was told | **A writing convention plus a rubric row.** It asks for provenance marking on load-bearing claims, not a new section. Closest to a house-style change, and it would touch every guide if adopted, not one. |
| `explicit_stop_or_kill_condition` | The document names what would make the team stop or kill this | **A genuine new section or field**, and the only one of the four that raises a scope question. |

**Three of these four are guide and rubric work.** They cost a rubric row, a named anti-pattern, and a
regeneration of the affected self-grade arithmetic, which `check-rubric-scope.py` already enforces. Only
the fourth proposes that a document contain something it does not currently contain.

## Decision Drivers

* **The protocol commits the library to acting on this.** It was written before any number existed, which
  is the only condition under which "we will publish what we find" means anything.
* **The admission test exists and is load-bearing**, and it has twice changed an outcome rather than
  ratifying one (V2MOM, `prototype-brief`).
* **Adding four rubric rows is not free.** Every guide in this library carries a self-grade rubric with a
  threshold sentence, and two independent reviewers have already flagged those thresholds as unsourced
  predictive claims. Adding rows makes that open question bigger, not smaller.
* **The measurement cannot justify its own answer.** See the trap below, which is the single most
  important paragraph in this record.

## The trap, stated before any option is considered

**If the four held-out criteria are added to the templates, they stop being held out.**

The next run's "criteria drawn from neither the template nor its guide" would be criteria the templates now
ask for. The rubric gap would grow, the held-out gap would grow, and **both movements would be
uninformative**, because the instrument would have been rebuilt around the intervention. That is not a
subtle risk; it is the mechanical consequence of teaching to the test, and this library has already
published one number it had to withdraw for a structurally similar reason.

Two consequences follow, and any adopted version of this record must carry both:

1. **The eval identified candidates. It cannot justify them.** A property earns its place because a named
   source publishes documents of that type containing it, or because this library argues for it in its own
   voice and labels it as its own, per decision procedure 11. **"The eval said so" is not an admissible
   reason**, and a record that used it would be committing the unsourced-confidence defect that the
   four-lens review exists to catch.
2. **Any future run must draw fresh held-out criteria**, authored against the post-change templates, with
   the same absence-search discipline. Re-using these four after adopting them would produce a number that
   looks like progress and measures nothing.

## The problem with the governing test, which the maintainer should see before choosing

The continuation brief assigned this question to [ADR 0030's admission
test](0030-templating-scope-markdown-documents.md). Read literally, **that test does not reach it.**

ADR 0030 says: *"A candidate **type** is templatable when a named source publishes it **as a written
document** ... not 'could someone write this', but 'does someone'."*

It admits and rejects **document types**. It says nothing about **elements within** an admitted type. The
question "should the `prd` bundle ask for a stop-or-kill condition" is not "is a PRD a real document", and
`prd` was admitted long ago.

So one of three things must be true, and this record cannot choose between them:

* **(a) The test extends by analogy.** The element-level form would be: *a section is admissible when a
  named source publishes documents of that type containing it.* Clean, consistent with ADR 0028's lineage,
  and it makes the fourth criterion an evidence question rather than a taste question.
* **(b) The test does not apply, and the governing rule is decision procedure 11**: the library may state
  its own position provided it labels the claim as its own rather than as received practice. This is the
  route `standing-standards` already took for its Review Trigger sections, which are labelled as the
  bundle's own contribution precisely because the literature supplies no condition-based trigger.
* **(c) Neither, and a new rule is needed.**

**This is a live gap in the library's own rules, not a detail of this proposal**, and it will recur the
next time anyone proposes a section rather than a bundle. It is closely related to the open item already
recorded in [`STATE.md`](../../../STATE.md): ADR 0028's format-admission rule turned out to have a third
criterion in practice that the written rule does not contain.

## Considered Options

* **A. Adopt nothing.** Record the finding, change no bundle. The signature stands as a published,
  unacted-on result.
* **B. Adopt the three guide-and-rubric criteria only**, and route the fourth through whichever admission
  rule the maintainer selects above.
* **C. Adopt all four**, treating `explicit_stop_or_kill_condition` as a new section across the affected
  families.
* **D. Adopt all four across all 26 bundles**, on the reasoning that a house-style property should not vary
  by family.

## Decision Outcome

**None. This record is `proposed` and takes no decision.** The recommendation offered for the maintainer
to accept or reject is **option B**, for three reasons:

1. It separates the cheap and uncontroversial from the genuinely contested, so the scope question is
   argued on its own rather than carried along by three easy changes.
2. The three it adopts require **no source at all**, because they ask the document to be internally
   coherent and legible rather than to contain new content. A rubric row asking "does anything here
   contradict anything else" makes no claim about the world.
3. It leaves the fourth blocked on evidence rather than on opinion, which is the shape this library's
   admission decisions have taken every previous time.

**What acceptance of option B would require**, none of which this record has done:

* A search, per affected bundle, for whether named sources publish that document type **containing a
  stated stop, kill, or halt condition**, logged to the same standard as any bundle's research pass and
  capable of returning "no", as `prototype-brief`'s did.
* A decision on the admission-rule gap above, since the search only settles the question under reading (a).
* A pass over every guide's self-grade rubric, because rows change the arithmetic and
  `check-rubric-scope.py` enforces it, and because the unresolved threshold-wording question recorded in
  `STATE.md` gets larger with every row added.
* Fresh held-out criteria for any subsequent measurement.

### Consequences

* Good: the finding is acted on through the library's own admission machinery rather than by an edit
  justified by a number.
* Good: the admission-rule gap is surfaced now, while it is one record's problem, rather than the next time
  someone proposes a section.
* Bad, and stated plainly: **option B changes what several guides grade, and this library has an open,
  twice-raised question about how its rubric thresholds are worded.** Adding rows before settling that
  makes the eventual family-wide edit larger.
* **Open, and not closed by this record:** whether the templates *should* move a document toward anything
  beyond their own criteria at all. A +0.85 rubric gap may be exactly what a user wants, and
  [the re-run](../../../evals/results/2026-08-08_matched-rerun.md) explicitly takes no position on whether
  scoring better against a document type's own standards is valuable.

## More Information

* [The matched re-run](../../../evals/results/2026-08-08_matched-rerun.md), which produced the signature, and
  the two independent runs behind it.
* [The eval protocol](../eval-protocol.md), section 3, which named the signature before any number existed.
* [`evals/rubrics/`](../../../evals/rubrics/), where each held-out criterion carries the recorded search that
  established its absence from the template and guide.
* [ADR 0030 (templating scope)](0030-templating-scope-markdown-documents.md) for the admission test this
  record argues does not reach element-level questions, and
  [ADR 0028 (the format axis)](0028-adopt-a-format-axis.md) for its lineage.
* [ADR 0032 (standing-standards)](0032-adopt-standing-standards-family-contract.md) for the worked
  precedent of a section shipped as the library's own labelled contribution when the literature supplied
  none.

**Three of the twenty-six bundles were measured.** Nothing here generalises to the other twenty-three, and
any adopted version of this record should say which bundles it believes it is talking about.
