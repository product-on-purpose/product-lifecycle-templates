# project-brief: history

Change log for the `project-brief` bundle. Each entry records what changed and why, so a reader can tell a
correction from a preference.

## 0.1.0 - 2026-09-29

**Initial release.** Researched 2026-09-29, building on an admission sweep run on 2026-09-27 while
[docs/internal/tier2-specs.md](../../docs/internal/tier2-specs.md) was written, across six dimensions: the
PRINCE2 canon, public-sector sources in both senses of the name, published templates counted section by
section, the neighbours that share the ground or the name, using the brief itself, and the standing gap
question.
[`project-brief_research-log.md`](project-brief_research-log.md) records **33 sources, all
fetched-and-verified**, and every quotation checked against the source's raw text rather than a retrieval
summary. Only `fetched-and-verified` sources are quoted anywhere in this bundle.

**The third `discovery-docs` member, reopening a family this contract had recorded as closed at two.**
[ADR 0063 (project brief reopens discovery-docs)](../../docs/internal/decisions/0063-project-brief-reopens-discovery-docs.md)
admitted the type: the family's own membership test, "exists to decide whether to build something, before
anyone commits to building it," fit a project brief without amendment, and a shipped sibling,
`business-case`, already routed a reader here by name and cited a named source for the boundary
(`business-case_guide.md:17`, `business-case_companion.md:315-317`, and both `business-case` template
bodies).

### The document's own boundary, stated in its own header

A project brief asks for authority to start finding out whether and how to proceed. It is not a business
case (the full comparison of options and a funded recommendation; this document carries only an outline of
that case and defers the comparison), not a project charter or project initiation document (neither is
built in this library; this library's position treats the brief's approval as authorizing initiation-stage
work, not delivery), not a product brief (a weaker, inferred boundary since no source read for this bundle
draws it explicitly), not a creative or design brief, not a Project Canvas (the same content in a one-page
diagram, a difference of medium), and not a project proposal or one-page pitch (this library's position: a
pitch sells a decision not yet made, while this document records a mandate that already exists). A separate,
heavyweight sense of the name published by NSW Health, the Treasury Board of Canada, and Ireland's National
Transport Authority, revised across a whole project's life, is out of scope; this bundle builds the shorter
PRINCE2 and UK government sense instead, written once and retired.

### The strain the maintainer weighed, and this library's position on it

The UK government's own primary guide states that "Approval of the Project Brief is the official start of
the project," language that reads as the commitment trigger itself. ADR 0063 states this library's position
directly: approval of the brief commits to **initiating**, to spending effort finding out whether to
proceed, not to **building**. The document that commits to building is a project charter or PID (unbuilt in
this library) or a PRD once the investment is approved.

### Corrections the research log recorded against its own build

- **GovS 002 has no glossary entry for "project brief."** The admission sweep's spec had recorded "project
  brief:" as a heading in a source's Annex B whose definition could not be recovered; a full read confirmed
  the term is not among that Annex's defined terms. The one passage naming a brief sits in the body, among
  the senior responsible owner's accountabilities.
- **"Project management team structure" is verbatim in the source, on a different page than the admission
  sweep had checked.** The sweep reported the phrase failing a raw-text check against prince2.wiki's project
  brief page; it is absent there and present on the starting-up page instead, and the Constraints and Who
  Should Be Involved section cites it from the correct page.
- **Two sections the admission sweep labelled as the library's own unsourced position turned out to be
  sourced.** Decision Requested and Project Approach were both written up as existing only because the
  family contract obliges them. Further sources found during this build's research state the request itself
  as the final output of PRINCE2's starting-up process, and name the project approach as a selected element
  of that same process. Both sections keep their place in the template, and their guidance now cites the
  sources that support them rather than resting on the contract alone.
- **A contents list mismatch was recorded rather than corrected by guesswork.** One source's start-up
  checklist and its separate project brief contents list were conflated in an earlier pass; this log keeps
  them apart and counts one list's items exactly as printed, including one row with no separator between two
  words, rather than inferring a missing comma.

### No paired pm-skills skill

`tools/known-skills.txt` carries no skill whose description names project initiation, a project brief, or a
comparable authorization request. `pairs_with: []` is declared, matching this family's own precedent: a
verified absence, not an oversight, in the same way `qa-docs` found the pm-skills catalog strong at the
strategy end and thin at verification.

### The example chains backward, per the family's shared-scenario rule

[`project-brief_example.md`](project-brief_example.md) is dated 2026-01-16, an Acme Analytics brief that:

- carries forward [product-vision](../product-vision/product-vision_example.md)'s existing commitment,
  dated 2026-01-14, two days before this brief;
- cites [user-persona](../user-persona/user-persona_example.md)'s Recurring Analyst, dated 2026-01-05,
  eleven days before this brief;
- asks its named approver to authorize the investment that
  [business-case](../business-case/business-case_example.md), dated 2026-01-20, four days after this brief,
  then justifies in full. The business case is cited only as a future document this brief requests, never as
  existing content, consistent with the family's chronology obligation that a discovery document is written
  before the documents it leads to.
