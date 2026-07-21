# Companion: The Software Design Document (SDD)

> The deep explainer for the SDD bundle. Read this to understand what a software design document is,
> where it came from, why it is shaped the way it is, and where practitioners disagree about it. The
> short operator card is [`sdd_guide.md`](sdd_guide.md); a fully worked instance is
> [`sdd_example.md`](sdd_example.md). Inline citations like [[1]](#ref-1) resolve to the
> [References](#references) at the bottom, tagged by source reliability.

---

## 1. Orientation

A software design document says **here is how we are going to build this, before we build it (or while
we build it), so the people who must implement, review, operate, or inherit it can reason about the
design first.** It sits between the problem statement and the code: a PRD or SRS says *what* to build
and for whom, and the SDD says *how* the system will be structured to deliver it. Its one job is to
make the technical design explicit and reviewable while changing it is still cheap.

The honest first thing to know is that "SDD" names two quite different artifacts, and this bundle
teaches the living one. The **heavy, formal SDD** codified by IEEE 1016 and the US defense standards is
now largely historical: IEEE 1016 was classified Inactive-Reserved in 2020 [[1]](#ref-1), and the
document it described was a comprehensive, viewpoint-structured specification produced up front. The
**living form** is the lightweight "design doc" that Google, Uber, Stripe, and much of the industry
actually write today: a few pages to a few dozen, written to think a design through and get it reviewed,
then archived once the code ships [[10]](#ref-10)[[19]](#ref-19). This bundle covers the modern design
doc, with its formal lineage acknowledged rather than imitated.

**At a glance**
- It describes an **implementation**, not a decision. That single distinction separates it from its two
  nearest neighbours: an RFC *proposes* a decision and asks for feedback, an ADR *records* a decision
  after it is made, and a design doc *describes how a thing will be built* [[18]](#ref-18). Conflating
  the three is the most common failure around this artifact ([section 8](#8-relationships-to-other-artifacts)).
- The **value is in the review**, not the document. A design doc read by no one who could catch the flaw
  has failed, however thorough. Its purpose is to surface the expensive mistake on paper.
- It is **living while the design is open and archived once it ships.** The worst version is a
  half-correct document kept as truth long after the code diverged from it [[19]](#ref-19).
- **Lean is the default.** Most changes worth a design doc are well served by five sections and one to
  three pages; the heavyweight form is for the design whose cost of being wrong is high
  [[10]](#ref-10)[[8]](#ref-8).
- Its shape is **not one canonical outline** but a stable core the strong versions share: context,
  goals and non-goals, the design itself, the alternatives, and the cross-cutting concerns
  [[10]](#ref-10).

If you read nothing else: a design doc is a **forcing function for thinking a design through and getting
it reviewed before it is expensive to change.** Google's own framing is the sharpest, and it is worth
holding onto against every temptation to over-produce: *"As software engineers our job is not to produce
code per se, but rather to solve problems"* [[10]](#ref-10). The document is a means to that, not the
product.

---

## 2. Origins and evolution

**The design step is as old as the idea of a software process.** Winston Royce's 1970 paper, the one
the industry misremembers as inventing "the waterfall," actually described a seven-step model that
included a named **Program Design** step preceding coding, and Royce explicitly warned that running those
steps once, straight through, was risky and invited failure; the single-pass reading and the "waterfall"
label were applied later, and the popularization of the term is usually attributed to Barry Boehm
[[6]](#ref-6). The point worth keeping is that a distinct design-before-code step has been in the
process from the beginning, and even its supposed origin argued for iterating it rather than freezing it.

**The formal SDD was a defense-and-standards artifact.** The US Department of Defense standard
DOD-STD-2167A, published in 1988, required a Software Design Document as a deliverable for each Computer
Software Configuration Item; it was heavily criticized for institutionalizing a waterfall model and for a
process that let the documentation drift from the software it described, and it was superseded by
MIL-STD-498 in 1994 [[5]](#ref-5). In parallel, the IEEE codified the artifact as a standard: IEEE 1016
began as a recommended practice in 1987 [[1]](#ref-1)[[3]](#ref-3), was revised through 1998, and in 2009
was elevated from recommended practice to a full standard, restructured around the viewpoint framework of
IEEE 1471-2000 [[1]](#ref-1)[[2]](#ref-2). The traditional content the standard lineage settled on is
four design areas: data design, architectural design, interface design, and procedural (component-level)
design [[4]](#ref-4). The 2009 revision organized a design description into a set of **design
viewpoints** (context, composition, logical, dependency, information, interface, structure, interaction,
state dynamics, and others), each answering a distinct concern and each requiring its rationale to be
recorded [[7]](#ref-7). (These viewpoint names come from a course summary of the standard rather than the
paywalled standard text, and are best read as indicative rather than authoritative.)

**Then the standard went dormant and the practice went lightweight.** IEEE 1016 was classified
**Inactive-Reserved in 2020** [[1]](#ref-1), and by then most software teams had stopped writing the
formal document at all. What replaced it was not "no design doc" but a **lighter** one: the internal
"design doc" that circulates a proposed implementation for review before coding, championed most visibly
by Google's engineering culture [[10]](#ref-10) and since adopted widely across the industry
[[14]](#ref-14). Gergely Orosz's survey found more than eighty companies running
some form of design-doc or RFC process, on a spectrum from a one-page template to a formal, numbered,
RFC-2119-worded instrument, with organizations like Uber moving from lightweight documents toward heavier
processes as they scaled [[14]](#ref-14). The through-line from Royce to Google is a single idea that
never actually left: **make the design explicit and reviewable before you commit to it.** What changed is
that the industry stopped believing the design had to be complete and frozen to be worth writing down.

---

## 3. Anatomy (section by section)

The template's sections are the stable core that the strong design-doc outlines share: Google's five
canonical sections [[10]](#ref-10), the arc42 architecture template [[8]](#ref-8)[[9]](#ref-9), the C4
model for the structural views [[11]](#ref-11), the IEEE viewpoint set [[7]](#ref-7), and an
operations-weighted template attributed to Limoncelli and colleagues [[12]](#ref-12). Where they agree is
where this template puts a required section; where only the heavyweight sources insist, the section is in
the full variant only.

### Frontmatter and status

The YAML block carries `title`, `status`, `authors`, and dates; the full variant adds `reviewers`. **The
`status` field is a lifecycle, not a label**: `draft` to `in-review` to `approved`, then `implemented`,
and eventually `superseded` when a later design replaces it.

*Beginner note:* update the status the moment the document moves, especially when the design ships. A
design doc's most common decay is a pile of documents stuck at `in-review`, or worse, marked `approved`
and then never updated as the built system drifts away from them.

*Expert note:* the status is also the signal for how much to trust the body. An `implemented` doc is a
historical record of the design as approved, not a live description of the running system, and it should
say so rather than pretend to be current. That honesty is the difference between an archive and a lie
([section 6](#6-debates-and-contested-boundaries)).

### Context and Scope

What exists today, what is changing, and the boundary of this design. The system's place in the larger
whole, and what is explicitly outside this document.

*Beginner note:* orient a reader who was not in the meetings. A short description of the current state
and the boundary of what you are designing is worth more than a page of background nobody asked for.

*Expert note:* scope is where design docs quietly fail. A document whose boundary is vague invites
reviewers to drag in every adjacent system, and the review never converges. State what is in and, as
importantly, what is out. This is Google's first canonical section, and its brevity is deliberate: it
orients, it does not re-derive the requirements [[10]](#ref-10).

### Goals and Non-Goals

Goals: what the design must achieve to be a success, ideally observable. Non-goals: what it is
deliberately not trying to do.

*Beginner note:* the non-goals are the more valuable half. They tell reviewers what not to raise, which
is how the discussion stays bounded.

*Expert note:* most runaway design reviews are reviewers arguing about something the author never meant to
solve. A crisp non-goal ends that thread before it opens. Goals and non-goals are a canonical section
precisely because they are the cheapest scope control the document has [[10]](#ref-10).

### The Design

The heart of the document: how the system is actually structured to meet the goals. In the lean variant
this is a single section carrying the core idea, the main components, and how they fit together. The full
variant breaks it into the views a heavier design needs.

*Beginner note:* describe the design at the level where a colleague could argue with it: the components,
how they interact, and the data that flows between them. A diagram is usually worth more than the
paragraph it replaces.

*Expert note:* this is the section that most tempts over-production, and the one where restraint matters
most. Google names it "the actual design" and warns against turning it into an exhaustive specification;
the job is to convey the design and expose the risky parts, not to pre-write the code [[10]](#ref-10). The
full variant's subsections map to the standard structural views:

- **Static structure and components** (what the parts are and how they depend on each other) is the
  arc42 static-structure view and the C4 Container and Component levels [[8]](#ref-8)[[11]](#ref-11).
- **Runtime and data flow** (how the parts behave together over time, the important sequences and state)
  is arc42's runtime view and the IEEE interaction and state-dynamics viewpoints [[8]](#ref-8)[[7]](#ref-7).
- **Interfaces and contracts** (the APIs, schemas, and events the design exposes and consumes) is the
  interface viewpoint that every lineage insists on [[7]](#ref-7)[[4]](#ref-4).
- **Deployment and operations** (where it runs and how it is released) is arc42's deployment view
  [[8]](#ref-8) and the operational weighting that the template attributed to Limoncelli foregrounds
  [[12]](#ref-12).

Use the C4 model's discipline for the diagrams: pick a level of abstraction (system context, container,
component) and keep one diagram to one level, rather than drawing one diagram that tries to show
everything and communicates nothing [[11]](#ref-11).

### Alternatives Considered

The other designs you genuinely weighed and why you are not proposing them, including "do nothing" or
"the obvious approach" where those are real options.

*Beginner note:* include the option a reader would immediately think of, and say why you did not take it.
That is what stops the review from re-treading ground you already covered.

*Expert note:* this section is the clearest signal of whether the design is reasoned or merely preferred.
It is a canonical section in Google's set and the standard place a reviewer who knows something you do not
gets the opening to say so [[10]](#ref-10). Two decoys and a winner is a sales pitch; a genuinely
considered alternative, described well enough that a reader could prefer it, is what earns the design its
credibility. Its absence invites reviewers to supply the alternatives adversarially.

### Cross-Cutting Concerns

The concerns that touch every part of the design rather than living in one component: security and
privacy, observability, error handling and failure modes, data retention, internationalization,
accessibility, cost.

*Beginner note:* walk the list and, for each, write one honest line: how the design handles it, or that
it does not apply and why. A single sentence that says "auth is unchanged; this service inherits the
existing mesh identity" is worth more than silence.

*Expert note:* cross-cutting concerns are a canonical section in Google's template because they are where
a design that looked clean reveals its real cost: the security review, the privacy surface, the
observability that has to be designed in rather than bolted on [[10]](#ref-10). arc42 treats the recurring
solution patterns as "cross-cutting concepts," a distinct section from the quality targets, and the
distinction is worth keeping: this section is *how recurring concerns are handled across the design*,
while Quality Attributes (full variant) is *the measurable targets the design must hit* [[8]](#ref-8).

### Quality Attributes *(full variant only)*

The non-functional requirements the design must satisfy, stated as targets a reader could check:
performance and latency, scalability, availability, reliability, security posture, maintainability.

*Beginner note:* give numbers where you can. "p99 under 200ms at 1000 rps" is a target; "should be fast"
is a wish that no one can design toward or verify.

*Expert note:* arc42 makes quality requirements a first-class section built from concrete quality
scenarios rather than adjectives, and that is the discipline to import: a quality attribute the design
does not have a scenario and a target for is one the design has not actually addressed [[8]](#ref-8).
This section is where the design meets the parts of the SRS or PRD that were never functional to begin
with, and it is the section a regulated or safety-critical review will read first
([section 9](#9-adaptations)).

### Risks and Open Issues *(full variant only)*

The parts of the design that are uncertain, risky, or undecided, and what you plan to do about them.

*Beginner note:* name the things that keep you up at night about this design: the dependency that might
not scale, the migration that might lose data, the question you have not answered yet. Naming a risk is
not weakness; hiding it is.

*Expert note:* this is arc42's "risks and technical debt" section, and it is the honest counterpart to
the Quality Attributes targets: the targets say what the design must achieve, the risks say where you are
not yet sure it will [[8]](#ref-8). A design doc with no risks section, on any non-trivial design, is not
riskless; it is undisclosed. Where a risk is really an open decision, that is often the signal to spin out
an RFC or record an ADR rather than bury it here ([section 8](#8-relationships-to-other-artifacts)).

---

## 4. Variants and sizing

**Lean is the default.** It carries Context and Scope, Goals and Non-Goals, The Design, Alternatives
Considered, and Cross-Cutting Concerns. That is exactly Google's five-section "mini design doc," the form
they recommend for the common case, and Google sizes such a doc at roughly one to three pages for an
incremental change [[10]](#ref-10). Most designs worth a document at all are well served by it.

**Full adds the heavyweight structure**: it breaks The Design into its structural, runtime, interface,
and deployment views, and adds Quality Attributes and Risks and Open Issues. The shared sections keep
their names and order, so lean is a strict subset of full and a document can grow from one to the other
in place. A full design doc in the Google idiom runs to something like ten to twenty pages for a large
project [[10]](#ref-10); arc42 explicitly supports the same document being used in a lean, a "thorough,"
or an "essential" mode depending on need [[8]](#ref-8).

The signal to scale up is the **cost of being wrong**, not the size of the system:

- The design is hard or slow to reverse (a data model, a public API, a persistence choice).
- It crosses several teams, who need the interface contracts and the deployment view to reason about it.
- It carries security, privacy, or regulatory weight, and the Quality Attributes and Cross-Cutting
  sections will be read by someone whose job is to find what you missed.
- It has real non-functional targets (latency, scale, availability) that the design has to be shaped
  around rather than measured after.

Otherwise, lean. The lightweight-design-doc literature converges on the same range and the same rule:
Hampus Wessman frames the living design doc at roughly two to fifteen pages and advises writing one
exactly when a piece of work is hard to estimate or hard to deliver without thinking the design through
first [[21]](#ref-21). Reaching for the full variant by reflex is how a design-doc practice turns into the
big-design-up-front bureaucracy its critics warn about ([section 6](#6-debates-and-contested-boundaries)).

---

## 5. Methodology lineage

Different traditions treat the design document very differently, and the differences are instructive.

| Tradition | Form of the design doc | What it optimizes for |
|---|---|---|
| **IEEE 1016 / formal** | A comprehensive, viewpoint-structured Software Design Description, produced up front | A complete, standardized, auditable design record [[1]](#ref-1)[[7]](#ref-7) |
| **US defense (2167A lineage)** | A required SDD deliverable per software item, contract-driven | Traceable, contractually verifiable design in a regulated acquisition [[5]](#ref-5) |
| **arc42** | Twelve sections, used in lean, thorough, or essential mode | A pragmatic, tailorable architecture description [[8]](#ref-8) |
| **Google-style design doc** | Five core sections, one to twenty pages, archived after shipping | Thinking a design through and getting it reviewed cheaply [[10]](#ref-10)[[19]](#ref-19) |
| **Large-scale eng (Uber, and others)** | Tiered: lightweight for team-scoped, heavier RFC for org-wide | Reviewing design docs at scale without drowning [[14]](#ref-14) |
| **Amazon** | A customer-facing PR/FAQ precedes a separate technical design | Forcing the *why* before the *how*, as distinct documents [[15]](#ref-15) |
| **Agile / XP / Shape Up** | Minimal up-front design; "just enough," emergent where possible | Keeping design close to the code and deferring commitment [[17]](#ref-17)[[20]](#ref-20) |

**Why this bundle teaches the Google-style living design doc** rather than the IEEE 1016 instrument: this
is a product-lifecycle template library, and the design document a product-engineering team actually
reaches for is the lightweight one written to review an implementation before building it. The formal SDD
is a more specialized artifact, now standards-dormant [[1]](#ref-1), and this template does not try to
reproduce it; where a regulated context genuinely needs the heavier form, [section 9](#9-adaptations)
covers the adaptation.

A word on the agile objection, because it is the one most often raised. Adopting agile does not remove the
need to think a design through before building it; Google's own guidance is explicit that design docs are
agile-compatible, pre-coding documents, and that prototyping is a complement to a design doc, not a
replacement for it [[10]](#ref-10). Marc Brooker makes the parallel argument for specifications: making a
design explicit does not require freezing it up front, and a spec can be a living, iterative artifact
[[13]](#ref-13). The lean variant exists so that "just enough design up front" has somewhere to live.

---

## 6. Debates and contested boundaries

### 6.1 How much design up front (the live one)

**Camp A, design before you build.** Making the design explicit and reviewing it catches expensive
mistakes on paper, aligns the people who were not in the room, and leaves a record of why the system is
shaped as it is [[10]](#ref-10)[[14]](#ref-14). This is the design-doc culture's core claim, and the
breadth of its adoption across the industry is its strongest evidence [[14]](#ref-14).

**Camp B, design emerges from the work.** The agile and Extreme Programming traditions push back on **big
design up front** (BDUF): a complete design produced before coding is waste, because the design that
survives contact with implementation is rarely the one you drew, and detailed up-front design commits you
before you have learned the most [[17]](#ref-17).

*This bundle's reading:* the mature middle is not a compromise but a named position. Josh Kerievsky's
"sufficient design" and the Poppendiecks' "responsible moment" describe designing up front only as much
as reduces real risk, and no more [[17]](#ref-17); Herb Bowie's
"just enough design up front" (JEDUF) frames it explicitly as a dial between BDUF and purely emergent
design, set by the specific project's risk and reversibility [[20]](#ref-20). The lean variant is this
library's answer: the smallest design doc that still de-risks the work, with the full variant reserved for
the designs whose cost of being wrong actually earns it. The academic picture confirms the debate is
unsettled rather than won: a 2023 systematic review of 74 studies on documentation in agile development
found that *"conflicting opinions"* about what should be documented remain unresolved, and that tooling
for agile documentation is fragmented [[16]](#ref-16).

### 6.2 Living document or archived record

Once the code ships, what happens to the design doc? Two honest positions. Google's documentation guidance
is that a design doc is a point-in-time decision tool that should be **archived after implementation**
rather than maintained as a living description of the system, because a half-updated design doc is worse
than none: its own maxim is that *"dead docs are bad"* precisely because a document kept alive but not
kept correct actively misleads [[19]](#ref-19). The other position, argued by Marc Brooker for
specifications generally, is that a design artifact *can* remain a living, iterative document if the team
actually maintains it [[13]](#ref-13). The defensible practice is to pick one on purpose: either archive
the doc and point new readers to the code and the ADRs, or commit to maintaining it and mark clearly when
it was last verified against reality. The failure is the accidental third state, a doc everyone treats as
current and no one has checked in a year.

### 6.3 Design doc, or RFC, or ADR

The sharpest and most practically useful distinction, treated in full in
[section 8](#8-relationships-to-other-artifacts): an RFC *proposes* a decision and seeks feedback, an ADR
*records* a decision after it is made, and a design doc *describes how something will be built*
[[18]](#ref-18). Much of the industry uses "design doc" and "RFC" interchangeably [[14]](#ref-14), which
is defensible when a single document both proposes and describes, but the ADR is genuinely distinct and
conflating it with the other two is a real and common error ([section 7](#7-anti-patterns-and-failure-modes)).

---

## 7. Anti-patterns and failure modes

1. **Big design up front.** A complete, detailed design produced before any code, treated as fixed. It
   commits you before you have learned the most and produces a design the implementation quietly
   abandons [[17]](#ref-17). The lean variant and the "just enough" framing exist to counter it
   [[20]](#ref-20).
2. **The stale living doc.** A design doc kept as the system's description long after the code diverged
   from it. A half-correct document that everyone trusts is more dangerous than an obviously archived one;
   "dead docs are bad" [[19]](#ref-19). Archive it, or mark when it was last verified.
3. **Conflating design doc, RFC, and ADR.** Writing a "design doc" that is really an undecided proposal
   (it is an RFC), or burying a significant, hard-to-reverse decision inside a design doc instead of
   recording it as an ADR where it can be found later [[18]](#ref-18). Know which of the three you are
   writing ([section 8](#8-relationships-to-other-artifacts)).
4. **Writing to exhaustion.** Using length and exhaustive detail as a substitute for clear thinking, so
   the design is approved because no reviewer could finish reading it rather than because it is sound.
   Google's principle that our job is to solve problems, not produce code, is the corrective
   [[10]](#ref-10); detail the risky parts and compress the obvious ones.
5. **Design-documentation drift.** The classic failure the defense standards were criticized for: the
   document and the software describe two different systems, because the design was written once and never
   reconciled with what got built [[5]](#ref-5). This is why the modern practice archives rather than
   pretends to maintain.
6. **No alternatives.** A design presented as the only option cannot show it was reasoned, and reviewers
   supply the missing alternatives adversarially [[10]](#ref-10). Include "do nothing" and the obvious
   approach you rejected.
7. **Scope with no boundary.** A Context and Scope section that never says what is *out* of scope, so the
   review drags in every adjacent system and never converges [[10]](#ref-10).
8. **Wishes instead of targets.** A Quality Attributes section full of adjectives ("fast," "scalable")
   with no numbers or scenarios, so nothing in the design can actually be checked against it
   [[8]](#ref-8).

---

## 8. Relationships to other artifacts

This is the section to read if you read only one, because the design doc's boundaries with its neighbours
are where teams most often get confused.

- **Precedes it:** the **PRD** (what to build for the user, and why) and, in more formal settings, the
  **SRS** (the specified requirements). The design doc follows them: it takes the *what* as given and
  works out the *how* [[4]](#ref-4). At Amazon the ordering is explicit and the documents are separate: a
  customer-facing **PR/FAQ** establishes the *why* before any engineering design is written
  [[15]](#ref-15).
- **The three-way distinction that matters most:** a **design doc describes an implementation**, an
  **RFC proposes a decision and seeks feedback**, and an **ADR records a decision after it is made**
  [[18]](#ref-18). They are not competitors but a division of labor. A design doc that is genuinely asking
  "should we do this?" is an RFC wearing the wrong name; much of the industry uses the two terms
  interchangeably and that is fine when the document does both jobs, but the moment feedback on the
  *decision* is the point, it is an RFC [[14]](#ref-14). And a significant, hard-to-reverse choice made
  inside a design doc (a database, an auth model, a public contract) belongs *also* in an
  [ADR](../adr/adr_companion.md), because six months later someone will look for that decision next to the
  code, not in a design doc they may never find. The healthy pattern: the design doc holds the whole
  design; the ADRs hold the individual decisions worth finding on their own; an RFC, where used, is the
  pre-decision conversation that fed both.
- **Accompanied by:** **C4 architecture diagrams** and, in heavier settings, the **arc42** structure,
  which embeds ADRs and C4 views inside a fuller architecture description [[11]](#ref-11)[[8]](#ref-8).
  These are how the design's structural views get drawn rather than described.
- **Feeds:** the **code**, the **test plan** (the design's interfaces and quality targets are what tests
  are written against), and the team's shared understanding of the system.

---

## 9. Adaptations

- **Small teams and solo work.** The lean variant, or a single page. The point is to externalize the
  design and get one other set of eyes before committing; the ceremony can be near zero, and Google sizes
  the incremental-change doc at one to three pages precisely so the bar to writing one stays low
  [[10]](#ref-10). Do not build a heavyweight design process for a team that fits in one room.
- **Large organizations.** Tier the process by impact, as Uber did as its design-doc volume grew beyond
  what reviewers could handle: a lightweight template for team-scoped designs and a heavier,
  reviewed process for org-wide ones [[14]](#ref-14). Invest early in making design docs discoverable;
  designs scattered where no one can find them is a named scaling failure.
- **Architecture-heavy work.** Adopt arc42's structure and use its lean-to-thorough tailoring rather than
  this template's, especially where the design must live alongside a formal architecture description that
  embeds ADRs and C4 views [[8]](#ref-8)[[11]](#ref-11).
- **Regulated or safety-critical work.** The heavy design document persists here for real reasons. In
  aerospace and defense, standards like DO-178C require traceability from requirements through design and
  code to tests, with the rigor scaling to the software's assurance level [[22]](#ref-22). A caution kept
  deliberately honest: this bundle does **not** claim that DO-178C mandates a document literally named
  "SDD." The primary standard describes design *data* and traceability objectives; a specific mandated
  "SDD" artifact is a vendor characterization that this bundle could not verify against the primary text
  [[23]](#ref-23). What is safe to say is that regulated industries sustain SDD-*class* artifacts (a
  reviewed, traceable design record) long after general industry went lightweight, and the full variant
  plus explicit Quality Attributes and traceability is the right starting point there. The defense-standard
  lineage (DOD-STD-2167A and its successors) is where that expectation comes from [[5]](#ref-5).
- **Methodology.** The template is methodology-agnostic by design, matching the catalog's own
  classification of the type. In an agile context, write the lean variant at the "just enough" threshold and
  keep it close to the code [[17]](#ref-17)[[20]](#ref-20); in a plan-driven or contractual context, the
  full variant with traceability is the expected form.

---

## 10. Worked example

[`sdd_example.md`](sdd_example.md) is a full-variant design doc for a **real-shaped feature**: adding
**Saved Views** to a project-management product, letting users save a configured filter-and-sort of a task
list and share it with their team. It is the same fictional feature the `delivery-docs` family's examples
chain on (its PRD, user stories, acceptance criteria, and release note), so the design doc slots into that
traceable set: the PRD says what Saved Views is and why, and this design doc works out how it is built. It
demonstrates every section carrying real content, the three structural views drawn with C4-style figures
labeled as illustrative, honest non-goals and risks, and a decision (the storage model) that the example
notes should also be captured as an ADR, showing the design-doc-to-ADR relationship in practice rather
than merely asserting it.

---

## References

Tagged by reliability: `[primary]` standards body, regulator, or originating source; `[practitioner]`
recognized independent authority or canonical writing; `[vendor]` commercially motivated, reliable on
convention; `[reference]` consolidated secondary (an encyclopedia or aggregator). Researched 2026-07-20;
per-source retrieval status is recorded in [`sdd_research-log.md`](sdd_research-log.md). Only sources
fetched and verified are quoted; two sources (IEEE 1016-1987 and the Parasoft page) were confirmed live
but not read, are marked as such, and carry no claim alone.

<a id="ref-1"></a>[1] IEEE. "[IEEE 1016-2009: Standard for Information Technology - Systems Design - Software Design Descriptions](https://standards.ieee.org/ieee/1016/4502/)." IEEE Standards Association (accessed 2026-07-20). Supports the three-revision history (1987, 1998, 2009), the 2009 elevation to a full standard, and the Inactive-Reserved status as of 2020-03-05. [primary]

<a id="ref-2"></a>[2] IEEE. "[IEEE Std 1016-2009 (standard text)](https://cengproject.cankaya.edu.tr/wp-content/uploads/sites/10/2017/12/SDD-ieee-1016-2009.pdf)." Hosted PDF, Cankaya University (accessed 2026-07-20; limited extraction from a binary PDF). Supports that the 2009 revision was modeled on IEEE 1471-2000 and uses a viewpoint-based framework. [primary]

<a id="ref-3"></a>[3] IEEE. "[IEEE 1016-1987 (IEEE Xplore record)](https://ieeexplore.ieee.org/document/565312)." IEEE Xplore. **URL confirmed live, body not read (the record returned no extractable text, checked 2026-07-20); cited only to corroborate the existence and 1987 date of the original recommended practice, which [[1]](#ref-1) carries.** [primary]

<a id="ref-4"></a>[4] Wikipedia. "[Software design description](https://en.wikipedia.org/wiki/Software_design_description)." en.wikipedia.org (fetched and verified 2026-07-20). Supports the four traditional SDD content areas (data, architecture, interface, procedural design) and the 2009 elevation. The article calls the 1998 edition the "initial" practice; [[1]](#ref-1) shows 1987 as the original, which this bundle treats as authoritative. [reference]

<a id="ref-5"></a>[5] Wikipedia. "[DOD-STD-2167A](https://en.wikipedia.org/wiki/DOD-STD-2167A)." en.wikipedia.org (fetched and verified 2026-07-20). Supports the 1988 publication, the SDD-per-Computer-Software-Configuration-Item requirement, the waterfall-bias and documentation-drift criticisms, and the 1994 supersession by MIL-STD-498. [reference]

<a id="ref-6"></a>[6] Wikipedia. "[Winston W. Royce](https://en.wikipedia.org/wiki/Winston_W._Royce)." en.wikipedia.org (fetched and verified 2026-07-20). Supports that Royce's 1970 WESCON paper described a seven-step model including a named Program Design step, that Royce did not advocate single-pass sequential development and called it risky, and that the "waterfall" popularization is attributed to Barry Boehm. [reference]

<a id="ref-7"></a>[7] Wildart. "[Software Design Descriptions (SDD)](https://wildart.github.io/MISG5020/SDD.html)," course material summarizing IEEE 1016-2009. wildart.github.io (fetched and verified 2026-07-20). Supports the IEEE 1016 design-viewpoint framework and the per-view rationale requirement. **Contested: the specific viewpoint enumeration is from a course summary, not the paywalled standard body; the individual viewpoint names are treated as plausible, not authoritative.** [reference]

<a id="ref-8"></a>[8] Hruschka, Peter and Starke, Gernot. "[arc42 Documentation Home](https://docs.arc42.org/home/)." arc42 (fetched and verified 2026-07-20). Supports the twelve arc42 sections (including runtime view, deployment view, cross-cutting concepts, quality requirements, and risks and technical debt) and the lean/thorough/essential usage modes. [practitioner]

<a id="ref-9"></a>[9] DeepWiki. "[Template Structure and Content - arc42](https://deepwiki.com/arc42/arc42-template/3-template-structure-and-content)." deepwiki.com (fetched and verified 2026-07-20). Corroborates the arc42 section descriptions in [[8]](#ref-8). [vendor]

<a id="ref-10"></a>[10] Ubl, Malte. "[Design Docs at Google](https://www.industrialempathy.com/posts/design-docs-at-google/)." industrialempathy.com (fetched and verified 2026-07-20). Supports Google's five canonical sections (Context and Scope, Goals and Non-Goals, The Actual Design, Alternatives Considered, Cross-cutting Concerns), the 10-20 pages for large projects and 1-3 for incremental changes sizing, the agile-compatibility of design docs, and prototyping as a complement rather than a replacement. Verbatim: "As software engineers our job is not to produce code per se, but rather to solve problems." [practitioner]

<a id="ref-11"></a>[11] Brown, Simon. "[The C4 model for visualising software architecture](https://c4model.com/)." c4model.com (fetched and verified 2026-07-20). Supports the four C4 abstraction levels (System Context, Container, Component, Code) and the one-diagram-one-level discipline. [practitioner]

<a id="ref-12"></a>[12] Limoncelli, Thomas; Chalup, Strata; Hogan, Christina (attributed). "[Design document template](https://gist.github.com/jfwilkus/88672445af104a652648)," gist attributed to *The Practice of Cloud System Administration*. github.com (fetched and verified 2026-07-20). Supports an operations-weighted section set (executive summary, goals, out of scope, high-level and detailed design, alternatives considered, special constraints). **Contested: authorship is asserted by the gist description, not confirmed in the source body.** [practitioner]

<a id="ref-13"></a>[13] Brooker, Marc. "[Spec Driven Development isn't Waterfall](https://brooker.co.za/blog/2026/04/09/waterfall-vs-spec.html)." brooker.co.za, 2026-04-09 (fetched and verified 2026-07-20). Supports that a specification can be a living, iterative artifact and that making a design explicit does not require freezing it up front. [practitioner]

<a id="ref-14"></a>[14] Orosz, Gergely. "[Companies Using RFCs or Design Docs and Examples of These](https://blog.pragmaticengineer.com/rfcs-and-design-docs/)." The Pragmatic Engineer (fetched and verified 2026-07-20). Supports that more than eighty companies use RFCs or design docs, the spectrum from minimal to RFC-2119-formal, the interchangeable use of "RFC" and "design doc," and Uber's evolution from lightweight documents toward heavier processes as it scaled. [practitioner]

<a id="ref-15"></a>[15] Working Backwards. "[The Amazon Working Backwards PR/FAQ Process](https://workingbackwards.com/concepts/working-backwards-pr-faq-process/)." workingbackwards.com (fetched and verified 2026-07-20). Supports that the PR/FAQ is a customer-facing product artifact (under six pages), not a technical design specification, and that it precedes engineering design. [vendor]

<a id="ref-16"></a>[16] Islam, A. K. M. Najmul; Hasan, Mahmudul; Eisty, Nasir U. "[Documentation Practices in Agile Software Development: A Systematic Literature Review](https://arxiv.org/abs/2304.07482)." IEEE SERA 2023 (fetched and verified 2026-07-20). Supports that a review of 74 studies found unresolved "conflicting opinions" on what should be documented and that agile documentation tooling is fragmented. Verbatim: "conflicting opinions." [primary]

<a id="ref-17"></a>[17] Wikipedia. "[Big design up front](https://en.wikipedia.org/wiki/Big_design_up_front)." en.wikipedia.org (fetched and verified 2026-07-20). Supports the BDUF definition and its agile critique, and the "sufficient design" / "responsible moment" middle positions attributed to Kerievsky and the Poppendiecks. [reference]

<a id="ref-18"></a>[18] Dagdeviren, Candost. "[ADRs and RFCs: Their Differences and When to Use Which](https://candost.blog/adrs-rfcs-differences-when-which/)." candost.blog (fetched and verified 2026-07-20). Supports the functional distinction between an ADR (records a decision made), an RFC (proposes a decision and seeks feedback), and a design doc (describes an implementation). [practitioner]

<a id="ref-19"></a>[19] Google. "[Documentation Best Practices](https://google.github.io/styleguide/docguide/best_practices.html)." google.github.io/styleguide (fetched and verified 2026-07-20). Supports the minimum-viable-documentation principle and design docs as pre-implementation decision tools archived after shipping rather than kept as half-correct living documents. Verbatim: "dead docs are bad." [practitioner]

<a id="ref-20"></a>[20] Bowie, Herb. "[Just Enough Design Up Front](https://www.softdevbigideas.com/just-enough-design-up-front.html)." softdevbigideas.com (fetched and verified 2026-07-20). Supports the JEDUF framing as a dial between big design up front and emergent design, set by a project's risk and reversibility. [practitioner]

<a id="ref-21"></a>[21] Wessman, Hampus. "[Agile Design Docs and Product Planning](https://hampuswessman.se/2024/02/agile-design-docs-and-product-planning/)." hampuswessman.se, 2024-02 (fetched and verified 2026-07-20). Supports lightweight design docs (roughly two to fifteen pages) as discovery before implementation, written when a piece of work is hard to estimate or to deliver without it. [practitioner]

<a id="ref-22"></a>[22] Wikipedia. "[DO-178C](https://en.wikipedia.org/wiki/DO-178C)." en.wikipedia.org (fetched and verified 2026-07-20). Supports that DO-178C is objective-based and requires requirement-to-design-to-code-to-test traceability, with documentation rigor scaling to the Development Assurance Level. **Contested: a specifically mandated document named "SDD" is not confirmed from the primary standard.** [reference]

<a id="ref-23"></a>[23] Parasoft. "[DO-178C Software Compliance for Aerospace and Defense](https://www.parasoft.com/learning-center/do-178c/)." parasoft.com. **URL confirmed live, body not read (checked 2026-07-20); a vendor claim that an SDD is a required artifact under DO-178C, not verified against the primary standard and carried by no claim in this bundle beyond noting it is a vendor characterization.** [vendor]
