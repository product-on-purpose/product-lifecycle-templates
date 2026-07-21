# Research log: Software Design Document (sdd) bundle

Per methodology section 6. Every source carries its tier, its retrieval status, and the claims it
supports. Only `fetched-and-verified` sources may be quoted in the companion. Researched 2026-07-20.

Retrieval status legend: **fetched-and-verified** (the page body was read), **url-confirmed-not-read**
(a real URL confirmed by search but the body was not read), **not-retrieved** (reference only).

## Sources

### Origins and evolution

1. **[Tier 1] IEEE 1016-2009, "Standard for Information Technology - Systems Design - Software Design Descriptions."** https://standards.ieee.org/ieee/1016/4502/ - **fetched-and-verified** - Supports: the three-revision history (1987, 1998, 2009); 2009 elevated it from "recommended practice" to full standard, modeled on IEEE 1471-2000; classified **Inactive-Reserved** as of 2020-03-05.
2. **[Tier 1] IEEE 1016-1987 (IEEE Xplore record).** https://ieeexplore.ieee.org/document/565312 - **url-confirmed-not-read** (page returned no extractable body) - Supports: existence and date of the original recommended practice.
3. **[Tier 1] IEEE Std 1016-2009, standard text (PDF hosted by Cankaya University).** https://cengproject.cankaya.edu.tr/wp-content/uploads/sites/10/2017/12/SDD-ieee-1016-2009.pdf - **fetched-and-verified** (limited extraction from a binary PDF) - Supports: the 2009 revision was modeled on IEEE 1471-2000; a viewpoint-based framework; scope spans databases and paper documents.
4. **[Tier 2] Wikipedia, "DOD-STD-2167A."** https://en.wikipedia.org/wiki/DOD-STD-2167A - **fetched-and-verified** - Supports: published 1988-02-29; an SDD was required per Computer Software Configuration Item; criticized as waterfall-biased; the CASE-tool-versus-document drift problem; superseded by MIL-STD-498 in 1994.
5. **[Tier 2] Wikipedia, "Winston W. Royce."** https://en.wikipedia.org/wiki/Winston_W._Royce - **fetched-and-verified** - Supports: the 1970 WESCON paper described a seven-step model including a named Program Design step; Royce did not advocate single-pass sequential development and called it risky; the Barry Boehm attribution.
6. **[Tier 2] Wikipedia, "Software design description."** https://en.wikipedia.org/wiki/Software_design_description - **fetched-and-verified** - Supports: the four traditional SDD content areas (data, architecture, interface, procedural design); the 2009 elevation; the twelve viewpoints. **Correction logged:** this article calls the 1998 edition the "initial" practice; the IEEE standards page (source 1) shows 1987 as the original, which this log treats as authoritative.

### Canonical structure

7. **[Tier 2] Wildart, course material summarizing IEEE 1016-2009, "Software Design Descriptions (SDD)."** https://wildart.github.io/MISG5020/SDD.html - **fetched-and-verified** - Supports: the twelve IEEE 1016 viewpoint names (Context, Composition, Logical, Dependency, Information, Patterns Use, Interface, Structure, Interaction, State Dynamics, Algorithm, Resource) and the per-view rationale requirement. **Contested:** the viewpoint enumeration is from a course summary, not the paywalled standard body; treat individual names as plausible, not authoritative.
8. **[Tier 2] arc42 (Hruschka, Starke), "arc42 Documentation Home."** https://docs.arc42.org/home/ - **fetched-and-verified** - Supports: the twelve arc42 sections; the three usage modes (lean, thorough, essential).
9. **[Tier 3] DeepWiki, "Template Structure and Content - arc42."** https://deepwiki.com/arc42/arc42-template/3-template-structure-and-content - **fetched-and-verified** - Supports: section descriptions; corroborates source 8.
10. **[Tier 2] Ubl, Malte (Google), "Design Docs at Google."** https://www.industrialempathy.com/posts/design-docs-at-google/ - **fetched-and-verified** - Supports: Google's five canonical sections (Context and Scope, Goals and Non-Goals, The Actual Design, Alternatives Considered, Cross-cutting Concerns); 10-20 pages for large projects, 1-3 for incremental changes; the quote "As software engineers our job is not to produce code per se, but rather to solve problems."
11. **[Tier 2] Brown, Simon, "The C4 Model for Software Architecture."** https://c4model.com/ - **fetched-and-verified** - Supports: the four C4 levels (System Context, Container, Component, Code) and three supplementary diagram types.
12. **[Tier 2] Limoncelli, Chalup, Hogan (attributed), design-doc template from "The Practice of Cloud System Administration" (gist).** https://gist.github.com/jfwilkus/88672445af104a652648 - **fetched-and-verified** - Supports: an operations-weighted section set (Executive Summary, Goals, Out of Scope, High-Level and Detailed Design, Alternatives Considered, Special Constraints). **Contested:** authorship is attributed by the gist description, not confirmed in the body.

### Methodology lineage and fit

13. **[Tier 2] Ubl, Malte (Google), "Design Docs at Google"** (as source 10) - **fetched-and-verified** - Additional support: design docs are agile-compatible pre-coding documents; adopting agile does not remove the need for them; prototyping is compatible with, not opposed to, a design doc.
14. **[Tier 2] Brooker, Marc (AWS), "Spec Driven Development isn't Waterfall."** https://brooker.co.za/blog/2026/04/09/waterfall-vs-spec.html - **fetched-and-verified** - Supports: a specification can be a living, iterative artifact; making a design explicit does not require it to be frozen up front.
15. **[Tier 2] Orosz, Gergely (The Pragmatic Engineer), "Companies Using RFCs or Design Docs and Examples of These."** https://blog.pragmaticengineer.com/rfcs-and-design-docs/ - **fetched-and-verified** - Supports: 80-plus companies use RFCs or design docs; a spectrum from minimal to RFC2119-formal; Uber's evolution from lightweight documents to full RFCs as it scaled.
16. **[Tier 3] Working Backwards, "The Amazon Working Backwards PR/FAQ Process."** https://workingbackwards.com/concepts/working-backwards-pr-faq-process/ - **fetched-and-verified** - Supports: the PR/FAQ (under six pages) is a customer-facing product artifact, not a technical design specification; it precedes engineering design.

### Debates and current status

17. **[Tier 1] Islam, Hasan, Eisty, "Documentation Practices in Agile Software Development: A Systematic Literature Review," IEEE SERA 2023.** https://arxiv.org/abs/2304.07482 - **fetched-and-verified** - Supports: a 74-study review finding that "conflicting opinions" on what requires documentation remain unresolved and that agile documentation tooling is fragmented.
18. **[Tier 2] Wikipedia, "Big design up front."** https://en.wikipedia.org/wiki/Big_design_up_front - **fetched-and-verified** - Supports: the BDUF definition and its agile critique; the "sufficient design" / RDUF middle position (Kerievsky, Poppendieck).
19. **[Tier 2] Dagdeviren, Candost, "ADRs and RFCs: Their Differences and When to Use Which."** https://candost.blog/adrs-rfcs-differences-when-which/ - **fetched-and-verified** - Supports: the functional distinction between an ADR (records a decision made), an RFC (proposes a decision, seeks feedback), and a design doc (describes an implementation). (Title corrected 2026-07-20 to match the page and the URL slug; an earlier draft of this log mistitled it "and Templates.")
20. **[Tier 2] Google, "Documentation Best Practices" (style guide).** https://google.github.io/styleguide/docguide/best_practices.html - **fetched-and-verified** - Supports: the minimum-viable-documentation principle; design docs as pre-implementation decision tools that are archived after shipping rather than kept as half-correct living docs; "dead docs are bad."
21. **[Tier 3] Bowie, Herb, "Just Enough Design Up Front."** https://www.softdevbigideas.com/just-enough-design-up-front.html - **fetched-and-verified** - Supports: the JEDUF framework and the factors that place a project between BDUF and emergent design.
22. **[Tier 3] Wessman, Hampus, "Agile Design Docs and Product Planning."** https://hampuswessman.se/2024/02/agile-design-docs-and-product-planning/ - **fetched-and-verified** - Supports: lightweight design docs (2-15 pages) as discovery before implementation; write one when a story is hard to estimate or deliver without it.

### Regulated-industry persistence (treated as contested)

23. **[Tier 2] Wikipedia, "DO-178C."** https://en.wikipedia.org/wiki/DO-178C - **fetched-and-verified** (Wikipedia tier) - Supports: DO-178C is objective-based and requires requirement-to-design-to-code-to-test traceability; documentation rigor scales with Development Assurance Level. **Contested:** a specific mandated "SDD" document format is not confirmed from the primary standard.
24. **[Tier 3] Parasoft, "DO-178C Software Compliance for Aerospace and Defense."** https://www.parasoft.com/learning-center/do-178c/ - **url-confirmed-not-read** - A vendor claim that an SDD is a required artifact under DO-178C; not verified against the primary standard.

## Claims flagged contested or time-bound

- The IEEE 1016 viewpoint enumeration (source 7) is from a course summary, not the standard body.
- That Meta/Facebook deliberately minimizes documentation (source 15) is reported, not independently confirmed.
- Whether DO-178C mandates an SDD specifically (sources 23, 24) is not confirmed from the primary standard; the companion states only that regulated industries sustain SDD-class artifacts, not that DO-178C names one.
- Brooker (source 14) is dated 2026; the arXiv history review surfaced by search (arxiv 2510.03894) was abstract-only and is not relied on.

## Notes for the companion

- Frame the type honestly: the heavy, formal SDD (IEEE 1016, DoD-STD-2167A) is largely historical (IEEE 1016 Inactive-Reserved since 2020); the living form is the lightweight "design doc" (Google, Stripe, Uber, Amazon-adjacent). The bundle covers the modern design doc with its formal lineage acknowledged.
- The load-bearing sections (appearing in three or more of IEEE / arc42 / C4 / Google / Limoncelli): context and scope, goals and non-goals, the design (static structure, runtime, deployment, interfaces), design decisions and alternatives, cross-cutting concerns, quality attributes, risks. These anchor the template's section set.
- The sharpest teaching point: design doc vs RFC vs ADR are distinct (describe an implementation / propose a decision / record a decision), and conflating them is a common failure. This belongs in the companion's Relationships section and the guide's anti-patterns.
