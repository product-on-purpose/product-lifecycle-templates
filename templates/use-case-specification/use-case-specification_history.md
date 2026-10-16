# use-case-specification: history

Change log for the `use-case-specification` bundle. Each entry records what changed and why, so a
reader can tell a correction from a preference.

## 0.1.0 - 2026-10-15

**Initial release.** Admitted into `delivery-docs` under a new sixth membership verb, "elaborates," by
[ADR 0072 (use-case-specification joins delivery-docs)](../../docs/internal/decisions/0072-use-case-specification-joins-delivery-docs.md),
which lands the family contract at `0.3.0`. Assigned and specced 2026-10-15, building on admission sweep
5 (2026-10-12) and the spec research of 2026-10-14. The build's six-dimension fan-out covered Cockburn's
canon (his templates, formality levels, goal levels and writing rules), the other published templates,
the lineage from Jacobson through UML to Use-Case 3.0, the debates over stories, detail and the named
failure modes, this library's own neighbors and the facts the worked example must agree with, and the
standing gap question. [`use-case-specification_research-log.md`](use-case-specification_research-log.md)
records **27 sources, all fetched-and-verified**: 8 primary, 2 standards bodies, 15 practitioner and 2
vendor. Every quotation was checked against each source's raw text rather than a retrieval tool's
summary of it: of 212 quotations the build's agents returned, 178 passed as normalized substrings, 7
more passed once a whitespace artifact was ignored, and 4 more passed once markup was ignored. Two
quotations that ran list or table cells together were split into 14 passing parts. Twenty-one failed, on
extraction artifacts, small edits, or a misattribution, and 36 quotations, mostly shorter re-quotes of
those failures, were added from raw text. **238 quotations remain, all checked against raw source
text.**

### The family contract gained a verb it did not already have

Nine of this library's ten family contracts excluded the type outright when tested against it, and
`delivery-docs` offered only a strained fit on its five existing verbs. ADR 0072 adds "elaborates" to
section 1: a document that walks one named actor through a complete interaction with the system toward
one goal, with its main success scenario stated as a numbered sequence of steps and the alternative and
exception paths that branch off it. The verb deliberately does not admit a diagram, a board, or a live
tool schema; it does not admit a user flow (`user-flow-task-flow` in the catalog), named as the nearest
kept-out neighbor whose own placement stays undecided; and it does not admit a document that checks a
path rather than specifying it, which `qa-docs` carries as `test-case`. The chain position this type
takes is stated in the contract itself: after the stories a backlog decomposes, and before the
acceptance criteria that confirm them.

### Two sizes map to two of Cockburn's three degrees of formality, not all three

Cockburn names three degrees of formality: brief, casual, and fully dressed. This bundle ships `lean`
for casual and `full` for fully dressed, a mapping this library chose rather than one any source states.
Cockburn's own casual form is written as prose paragraphs; the lean template keeps numbered steps
instead, so lean is casual's nearest equivalent in how much it covers, not in what shape it takes. The
brief form, two to six sentences with no real branching, sits below anything this library templates.

### The fully dressed field set rests on three things read directly, not on reconstruction

The 2001 book's own fully-dressed template (pages 119-120) could not be read: every Internet Archive copy
is lending-restricted, and the available sample pages carry only the book's table of contents, preface,
and index. The field set instead rests on the pre-publication draft's own fully dressed template, read in
full and verbatim; Cockburn's 1998 template; and the 2001 book's preface, table of contents, and index,
which confirm the draft's template was later renumbered rather than resolve whether any field changed.
This bundle does not claim the published book's Use Case 24 was read, and does not claim its fields match
the draft's Use Case 7.

### Corrected catalog metadata carried into this meta

The catalog entry for this type (`docs/internal/catalog.md` #35) is corrected in the same pass that built
this bundle: methodology moves from "Waterfall/UP/RUP" to `methodology-agnostic`, because no source read
ties the type to Waterfall, neither Cockburn's nor Wiegers' templates name a methodology, and Use-Case 3.0
describes applying use cases "in an agile and scalable fashion" while serving waterfall teams too. This
meta's `methodology` field carries that correction rather than the catalog's superseded value.

### The honest core

**No source read for this bundle measured whether writing a use case specification changes a project
outcome.** The one source offering a measurement (an academic traceability protocol) measures its own
protocol against its own worked case, not what writing use cases does for a project more generally.
Whether use cases have fallen out of favor against user stories is reported in the companion as a live,
dated argument rather than settled by this bundle.
