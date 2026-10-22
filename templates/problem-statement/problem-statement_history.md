# problem-statement: history

Change log for the `problem-statement` bundle. Each entry records what changed and why, so a reader
can tell a correction from a preference.

## 0.1.1 - 2026-10-22 - the opportunity statement becomes its own type

**An alias change from the maintainer's 2026-10-17 decision sitting, items D6 and D9.** No section,
placeholder or rubric row changed.

- **"Opportunity statement" is no longer an alias (D9).** The maintainer ruled the problem statement and
  the opportunity statement different documents. The opportunity statement became catalog entry 207, a
  candidate type tracked as issue #298, not yet researched on its own. The guide, both templates' opening
  comment and three companion passages now say so, each with its date. The evidence is unchanged: Nielsen
  Norman Group still treats the two as one document, and the companion still reports it.
- **"Point of view statement" is a new alias (D6).** The Interaction Design Foundation calls the Define
  mode's problem statement one "commonly known as the Point of View (POV) in Design Thinking", and the
  Canada School of Public Service titles its job aid "Point-of-View (POV) Problem Statement". Both were
  already in the research log. The sitting declined two other proposed aliases, "market problem
  statement" and "target behaviour definition".
- **The research log carries a dated note**, not a rewrite, because it records what the research found.

## 0.1.0 - 2026-10-11

**Initial release.** Researched 2026-10-11 across six dimensions: UX discovery practice, government
service design, design thinking, product-management worksheets, the family's own named neighbours,
and the standing gap question. [`problem-statement_research-log.md`](problem-statement_research-log.md)
records **43 sources, all fetched-and-verified**, and 264 quotations checked against raw source text
rather than a retrieval summary. Nine of the 43 came from a gap-fill pass after drafting. That pass
found constraints labelled in engineering-design sources, which the bundle routes to `project-brief`
against one engineering paper's dissent, and it showed that one source does contrast a problem
statement with a business case by name, which the first draft had denied in seven places. Only
`fetched-and-verified` sources are quoted anywhere in this bundle. A separate group of sources was
never added to the log at all, because this research could not retrieve them: eight fetch attempts
across two passes against McKinsey's own problem-statement worksheet timed out, two of Atlassian's
companion templates open only inside an application shell, two Harvard Business Review articles from
2012 and 2017 are paywalled, and PMI's own problem-statement page returned HTTP 403. None of those
appears anywhere in this bundle, quoted or otherwise.

**Catalog entry 206, a new type with no prior row.** Under
[ADR 0030](../../docs/internal/decisions/0030-templating-scope-markdown-documents.md), a new type's
catalog row waits for its own research to find a named source; this research found two, Heap's own
"problem brief" label and Nielsen Norman Group's "opportunity statement," and the row landed on the
build branch before this build ran, carrying the catalog count from 205 to 206.

### The fourth `discovery-docs` member, and the family's first `define`-phase member

[ADR 0069](../../docs/internal/decisions/0069-problem-statement-joins-discovery-docs.md) admitted the
type: `discovery-docs`'s own membership test, "exists to decide whether to build something, before
anyone commits to building it," fit a problem statement without amendment, and its cadence clause,
written once and finished when the decision is made, fits a document every admitting source describes
written once at the start of an initiative. What needed an amendment was the axis, not the membership
test: the contract had pinned `discover` alone, and
[ADR 0068](../../docs/internal/decisions/0068-define-means-problem-framing.md) reserves `define` for a
document that frames one problem and names no solution, option, project, or investment. This bundle
declares `phase: define`, the family's first use of that value, and the family's shared-scenario thread
is extended backward by one more step: a problem statement now precedes the project brief and the
business case it already chains onto.

### Two sizes, by the maintainer's ruling, against the research's own lean-only finding

This build's own research found high-confidence support for one size only: every admitting source
describes a few sentences or a short page, and the problem-statement research dimension stated
plainly that a full variant "would be inventing structure beyond what any source in this sweep actually
shows." The maintainer ruled on 2026-10-11 to ship two sizes regardless,
`sizes_available: [lean, full]`, on the condition that every full-only section rest on a source this
build's research actually read rather than on the family contract alone. The full variant's four added
sections, How People Cope Today, What Is Not Part of the Problem, How We Will Know It Is Solved, and
Open Questions and Assumptions, each cite a source in `problem-statement_companion.md` section 3
(Anatomy); none rests on the contract's own obligation alone. The lean variant's six sections are a
strict ordered subset of the full variant's ten, unchanged in name or order, per contract section 3.2.

### What stays out at every size

Options, a recommended solution, a cost estimate, a project scope or plan, and a request for funding
stay out at both sizes, because naming any of them would break the `define`-phase rule that a member
names no solution, option, project, or investment. Constraints are not carried either: the sources that
label them use them to bound a solution, and `project-brief` carries them. A root cause stays out of the Problem Statement section itself,
following NHS Wales's own rule that "problem statements do not describe the solution or root causes";
a suspected cause instead gets a labeled, hypothesis-only place in Open Questions and Assumptions,
following the University of South Carolina's A3 template's own separation of the two steps. That
placement is this library's own position, not a point every source in the log agrees on.

### The boundary with `business-case`, named directly rather than hidden

`business-case`'s own Problem and Opportunity section asks the same questions this bundle asks, inside
a funded investment case. This bundle's companion names the overlap in its own Relationships section
rather than leaving a reader to find it: the standalone statement comes earlier, asks for no money, and
decides whether a problem is worth a project brief or a business case at all. A business case written
after this statement can cite it and shorten its own section accordingly. One source read for this
bundle contrasts the two documents by name; the order, statement first, is this library's own position.

### The boundary with `project-brief`

An Association for Project Management consultation draft, read for this library's `project-brief`
research (`project-brief_research-log.md:156`), lists "problem statement," "project brief," and
"project charter" as names used interchangeably for one early rationale. This research read APM's own
published online glossary directly and found no "problem statement" entry there at all; the glossary
defines "Brief" and "Charter" as two separate things. This bundle's companion cites only what the
glossary itself says, and records the interchangeable usage as a reported practice rather than as this
library's own position.

### One pm-skills pairing, verified and recorded in `tools/known-skills.txt`

`define-problem-statement` was read directly at pm-skills commit `152b17518` (2026-06-10), skill
version 2.1.0, `phase: define`. Its own description reads "Creates a clear problem framing document
with user impact, business context, and success criteria," and its own "When NOT to Use" list routes a
reader to `deliver-prd`, `develop-solution-brief`, `define-jtbd-canvas`, and `define-hypothesis`, each a
boundary this bundle also draws from its own sources. `tools/known-skills.txt` did not list the ID
before this release; it is added in the same change, with the verification command and result recorded
there, so this bundle's `pairs_with: [define-problem-statement]` resolves rather than being declared
and left unchecked.

### The example chains backward, per the family's shared-scenario rule

[`problem-statement_example.md`](problem-statement_example.md) is dated 2026-01-09, an Acme Analytics
statement for the New-Account Second-View Stall problem that:

- follows [user-persona](../user-persona/user-persona_example.md)'s Recurring Analyst, dated
  2026-01-05, four days before this statement;
- precedes [product-vision](../product-vision/product-vision_example.md), dated 2026-01-14, five days
  after this statement;
- precedes [project-brief](../project-brief/project-brief_example.md), dated 2026-01-16, seven days
  after this statement, and [business-case](../business-case/business-case_example.md), dated
  2026-01-20, eleven days after this statement. Both later documents go on to answer the problem this
  statement frames; this statement names neither of their solutions, consistent with the family's
  chronology obligation that a discovery document is written before the documents it leads to.
