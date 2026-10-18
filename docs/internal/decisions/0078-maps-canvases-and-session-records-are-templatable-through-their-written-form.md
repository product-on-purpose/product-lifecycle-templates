---
status: proposed
date: 2026-10-17
decision-makers: [jprisant]
consulted: [claude]
---

# Maps, canvases and session records are templatable through their written form

## TL;DR

- **Decision.** [ADR 0030 (templating scope)](0030-templating-scope-markdown-documents.md) stands word for
  word: this library templates artifacts whose primary form is a written document. This record says how that
  rule applies to kinds of artifact that research kept rejecting. A map, a model or a canvas is in scope
  through a structured written form of it. A workshop, a design sprint or a whiteboard session is in scope
  through its written record. Both ship as Markdown.
- **The admission bar does not move.** Each candidate still needs one named source that publishes its written
  form, as [ADR 0048](0048-one-named-source-clears-the-admission-test.md) reads ADR 0030. This record says
  these kinds of artifact can be templated. It admits no type.
- **What it retires.** Two Define admission sweeps on 2026-10-16 used a written-document test stricter than
  ADR 0030. It excluded "a board, a canvas shipped only in Miro, Mural or FigJam, a workshop exercise, a
  diagram, or a slide". No tracked file ever stated that test, and no record adopted it.
- **What stays out.** Wireframes, interactive prototypes, websites and live dashboards stay out, as ADR 0030
  already says. Rendered diagrams are not admitted either.
- **Markdown always ships.** Self-contained HTML files, or resources that import into Miro or FigJam, may be
  considered later. They would only ever accompany the Markdown, and they need a decision of their own.
- **Status:** proposed 2026-10-17. It stops for the maintainer's read.

## Context and Problem Statement

ADR 0030 (2026-07-30) set the scope rule: "This library templates artifacts whose primary form is a
**written document**. An artifact whose primary form is **visual, executable, or a live data surface** is out
of scope for templating". It set the admission test in the same breath: "A candidate type is templatable when
a named source publishes it **as a written document**." It applied both to two catalog types, the wireframe
and the interactive prototype, and excluded them. It did not say how the rule applies to a canvas, a map or a
workshop.

**Research briefs filled that gap with a stricter test.** The second Define admission sweep, on 2026-10-16,
stated its written-document test as: one named source defines the artifact as a written document, "not a
board, a canvas shipped only in Miro, Mural or FigJam, a workshop exercise, a diagram, or a slide". The third
sweep reused that test. The briefs lived in gitignored working files, so the test was applied without ever
being written into the repository or adopted by a record. The review that followed, on 2026-10-17, found it
was one of three filters behind the sweeps' single Define bundle.
[ADR 0077](0077-define-ends-with-a-chosen-concept.md) records the other two.

**The library already ships the written form of artifacts like these.**

- `product-vision` ships `canvas` as its default format, rendered in Markdown under
  [ADR 0028 (the format axis)](0028-adopt-a-format-axis.md).
- `sprint-retrospective-notes` and `project-milestone-retrospective` are written records of a session. Both
  are `process-docs` members at `phase: iterate`.
- `kpi-dashboard` is the written definition of a live data surface, which ADR 0030 itself names as legitimate.
- `runbook` is a written procedure, a `standing-standards` member.

**The maintainer's direction, given on 2026-10-17.** The concern behind ADR 0030 was that this library should
not become "a html prototype and website builder". Within that line, "maps, workshops, processes, run books,
whiteboards, canvases" can all be artifacts. On format, the maintainer said: "There should always be md files
too though".

So the question this record answers is how ADR 0030's rule applies to maps, models, canvases and sessions,
and what this library ships for them.

## Decision Drivers

- **ADR 0030's line is in the right place.** The exclusion that protects the library is the artifact whose
  primary form is visual, executable or a live data surface. A canvas or a workshop has a written form that a
  team can fill and keep.
- **A test nobody adopted should not keep deciding admissions.** Research briefs should apply the rule the
  repository states, not a stricter one they wrote for themselves.
- **The precedents already exist.** Four built bundles template the written form of something that is not
  prose.
- **Admission stays per candidate.** ADR 0030 asks "not 'could someone write this', but 'does someone'", and
  this record leaves that question to each candidate's research.
- **The efficacy record.** The library's evaluations found that documents written with these templates score
  no better than a strong generic-prompt control on decision-usefulness criteria drawn from neither the
  template nor its guide. A session record keeps most of its value in the room, not in the document, so it
  widens that unproven surface fastest.

## Considered Options

1. **Maps, models and canvases only.** Their published structured written forms are in scope. Session records
   are not addressed.
2. **Maps, models and canvases now, session records after research of their own.** The agent's recommendation
   on 2026-10-17, at medium confidence.
3. **Maps, models, canvases and session records now.** Chosen by the maintainer on 2026-10-17.
4. **All of option 3, plus rendered diagrams in templates**, such as Mermaid blocks. This would need ADR 0030
   itself to change.

## Decision Outcome

**Chosen: option 3.** The following kinds of artifact are in scope through their written form, and each
candidate type still faces the admission test.

| Kind of artifact | The written form this library would template | A precedent already shipped |
|---|---|---|
| A map, a model or a canvas | The structured written form a named source publishes, such as fields, sections or a table, rendered in Markdown | `product-vision`'s `canvas` format |
| A workshop, a design sprint or a whiteboard session | Its written record, in the shape a named source publishes | `sprint-retrospective-notes`, `project-milestone-retrospective` |
| A process or a procedure | The written procedure | `runbook` |

**What stays out of scope.**

- **Everything ADR 0030 already excludes.** A wireframe, an interactive prototype, a website and a live
  dashboard each have a primary form that is visual, executable or a live data surface.
- **Rendered diagrams (option 4).** A template in this library never depends on a renderer. A map is written
  as a table or a list. A diagram whose meaning only appears once it is drawn pulls toward the visual-primary
  class that ADR 0030 excludes.

**Markdown always ships.** Every bundle keeps shipping its templates as Markdown. A future decision may add
self-contained HTML files, or resources that import into Miro or FigJam, as companions to that Markdown. Such
a decision would have to address two existing commitments.
[`AGENTS.md`](../../../AGENTS.md) promises an agent that "every file is plain Markdown, YAML, or JSON", and
ADR 0030 excludes artifacts whose primary form is executable. This record makes no such addition.

### Templates for running an exercise

Later the same day, the maintainer added a note: "templates for gamestorming, design thinking / sprint
exercise and tools" make sense for this library. The maintainer gave it as information, not as a ruling, and
this section depends on it. A template for running an exercise is a written plan with a human reader, such as
a facilitation guide. So it is in scope on ADR 0030's own rule, and it faces the same admission bar. ADR 0030's
test for a commissioning document applies here too: the filled document must be valuable to a person who has
never heard of an LLM, or it is a prompt and belongs in a skills library. This record admits no exercise type.

### What the decision costs, stated rather than smoothed over

1. **More candidates reach admission, and each costs research.** Several catalog types that earlier sweeps
   rejected under the unadopted test become testable again. Testable is not admitted.
2. **Many of these artifacts exist mainly inside a tool.** A vendor's board template is not a named source
   publishing a written form. Candidates whose only sources are boards will still fail admission, and this
   record does not change that.
3. **Session records may need a family.** Where a session record lands is decided per candidate, by its own
   placement record. It might join `process-docs`, which already holds the two retrospectives, or need a
   contract of its own.
4. **The unproven surface grows fastest here.** That cost is named in the drivers and is not repeated.

### Consequences

- **The admission test is unchanged.** One named source must publish the candidate's written form
  (ADR 0048). No type is admitted, and no catalog row changes, in this record.
- **Research briefs apply ADR 0030 as clarified here.** The unadopted test quoted above is retired.
  Candidates rejected only under it may be tested again. The Define re-score that ADR 0077 calls for applies
  this record.
- **`prototype-brief` is not reopened.** [ADR 0035](0035-prototype-brief-fails-the-admission-test.md) found
  no named source publishing a prototype brief at all. A card or worksheet with its own published written
  form would be a different candidate type, tested on its own evidence.
- **ADR 0030 carries a dated note** that points to this record. Nothing in ADR 0030 was false, so the note is
  not a correction.
- **No family contract changes, and check K is untouched.** The promise in `AGENTS.md` is unchanged.

## More Information

- The scope rule this record clarifies: [ADR 0030](0030-templating-scope-markdown-documents.md).
- How many sources admission needs: [ADR 0048](0048-one-named-source-clears-the-admission-test.md).
- The format axis that let `product-vision` ship a canvas: [ADR 0028](0028-adopt-a-format-axis.md).
- The phase decision made the same day, which names the stricter test as one of three filters:
  [ADR 0077](0077-define-ends-with-a-chosen-concept.md).
- The type that stays declined: [ADR 0035](0035-prototype-brief-fails-the-admission-test.md).
