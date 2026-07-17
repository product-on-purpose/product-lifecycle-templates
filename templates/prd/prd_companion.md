# Companion: The Product Requirements Document (PRD)

> The deep explainer for the PRD bundle. Read this to understand what a PRD is, where it came
> from, why it is shaped the way it is, and where serious practitioners disagree about it. The
> short operator card is [`prd_guide.md`](prd_guide.md); a fully worked instance is
> [`prd_example.md`](prd_example.md). Inline citations like [[1]](#ref-1) resolve to the
> [References](#references) at the bottom, tagged by source reliability.

---

## 1. Orientation

A Product Requirements Document (PRD) is the artifact that says **what to build, for whom, and why, with enough scope and success criteria that a team can design and build the right thing.** It sits between problem understanding and implementation: discovery decides whether a problem is worth solving, and the PRD translates the chosen solution into something engineering, design, and QA can act on [[9]](#ref-9)[[12]](#ref-12).

It travels under many names. "Product spec," "product brief," "feature spec," "one-pager," and "product requirements" are the same artifact at different weights, not different documents [[12]](#ref-12). This bundle treats them as one type with size variants.

**At a glance**
- It communicates intent, not implementation. It says what must be true, and leaves engineering room on how.
- Its center of gravity is the **problem**, not the feature list. Strong teams spend more time there than feels comfortable [[7]](#ref-7).
- Modern PRDs are short, living documents that evolve through an "open questions" list, not 50-page manifestos signed once and frozen [[10]](#ref-10)[[11]](#ref-11).
- It is methodology-agnostic but contested: some respected practitioners argue the high-fidelity prototype, not the prose, should be the real spec [[2]](#ref-2)[[3]](#ref-3).

If you read nothing else: a PRD is a **forcing function for shared understanding**. Its value is the alignment it creates, not the pages it produces.

---

## 2. Origins and evolution

The PRD is a descendant of the **waterfall and phase-gate era**, when product definition, design, and delivery happened in sequence and each phase handed a document to the next. In that lineage the PRD followed a **Market Requirements Document (MRD)**: the MRD captured the market problem and the "why," and the PRD translated it into the "what" and "how" for designers, developers, and QA [[6]](#ref-6). Organizations using this model often wrote highly detailed MRDs and PRDs running dozens of pages [[6]](#ref-6). The Pragmatic Institute framework, in wide use since the 1990s, codified this MRD-then-PRD split [[6]](#ref-6).

Two shifts reshaped the artifact:

- **Agile.** As teams moved to iterative delivery, the heavyweight PRD was widely criticized as slow and quickly outdated. The response was not to abolish the document everywhere but to **shrink it**: shorter, lighter, living PRDs that start as a one-pager and evolve in tools like Jira or Confluence as sprints progress [[10]](#ref-10)[[11]](#ref-11). Scrum went further and recognized no PRD at all; its Product Backlog absorbs the requirement-capturing job (see [§5](#5-methodology-lineage)) [[1]](#ref-1).
- **Discovery-led product.** A second critique, from the Silicon Valley Product Group, holds that the real problem a spec must solve is communicating the intended experience precisely, and that **a high-fidelity prototype does this better than prose**. Cagan has argued since 2006 that "the majority of the product spec should be the high-fidelity prototype," a position he has only sharpened as prototyping tools improved [[2]](#ref-2)[[3]](#ref-3)[[4]](#ref-4).

The result today is a spectrum, not a single form: from a one-paragraph one-pager, through a living agile PRD, to a prototype-plus-companion-doc, to the still-heavyweight PRD that regulated and hardware contexts genuinely need.

---

## 3. Anatomy (section by section)

What each section is, why it exists, and how to do it well. Beginner guidance is plain; expert notes flag when to drop, expand, or distrust a section. The lean variant carries the starred sections; the full variant adds the rest.

**Summary (lean).** One paragraph capturing the whole idea and the outcome it produces. *Why:* a reviewer should be able to grasp and triage the work before reading detail. *Expert note:* if you cannot write this paragraph, the work is not yet shaped enough to spec; that is a signal, not a formatting problem.

**Context and background (full).** The strategic thread the work hangs from, plus relevant history and what changed to make it timely. *Why:* without it, reviewers cannot judge whether the work should be built at all, only whether it is well-described. *Expert note:* tie this to a specific goal, OKR, or bet; a PRD that cannot name the strategy it serves is a candidate to kill, not to refine.

**Problem (lean).** The user's problem, with evidence it is real and worth solving now. *Why:* the problem is the highest-leverage part of the document. Lenny Rachitsky's widely-copied template makes crystallizing the problem the first step, and asks how you know the problem is real and worth solving before it asks what the thing is [[8]](#ref-8). *Beginner trap:* writing a missing feature ("users cannot export to CSV") instead of the problem beneath it ("users rebuild reports by hand in another tool, losing an hour a week"). *Expert note:* high-performing templates deliberately separate problem from solution to force time on the problem; that template's sections put Problem, Why, Success, and Audience ahead of "What does this look like in the product?" [[8]](#ref-8).

**Goals and non-goals (lean).** The outcomes the work must achieve, and what you are deliberately not doing. *Why:* non-goals are where scope discipline lives. *Expert note:* the non-goals list is the most-skipped and most-valuable section; it is the cheapest scope-creep insurance you can write [[11]](#ref-11).

**Target users and personas (lean: target users).** Who this is for, specifically, and the context they are in. *Why:* design and tradeoffs depend on knowing the user. *Beginner trap:* "all users." *Expert note:* name the primary user when the segments conflict; designing for everyone optimizes for no one.

**Solution overview (lean).** The core idea and how a user experiences it, with a link to the prototype or mockup. *Why:* it gives the team a shared mental model before detail. *Expert note:* this is the seam where the prototype-as-spec debate bites. If you have a high-fidelity prototype, this section can be short and point at it; the prototype carries the precision [[2]](#ref-2)[[3]](#ref-3).

**User stories (full).** The work as user-centered stories, grouped by flow. *Why:* it keeps requirements anchored to user value and feeds the backlog. *Expert note:* keep acceptance criteria out of here; they belong in their own artifact, or the PRD bloats into a test plan.

**Functional requirements (full).** What the system must do, as testable, prioritized statements. *Why:* engineering needs to know what is required versus nice-to-have. *Beginner trap:* 80 equally-weighted requirements with no priority. *Expert note:* prioritize explicitly (MoSCoW or similar) so tradeoffs are possible when time runs short.

**Non-functional requirements (full).** Performance, security, accessibility, reliability, privacy, compliance, with measurable thresholds. *Why:* these qualities are expensive to retrofit. *Expert note:* the most common production surprise is an NFR (latency, accessibility, data residency) that was implicit until launch.

**UX and design (full).** Key flows and all states (empty, loading, error, edge), with links to wireframes or the interactive prototype. *Why:* the unhappy paths are where real work and real bugs live. *Beginner trap:* documenting only the happy path.

**Success metrics (lean).** Primary metric(s) tied to goals, a guardrail you must not harm, and the window. *Why:* it defines "did it work" before you are emotionally invested in the answer. *Expert note:* define metrics in advance and pick a guardrail; a feature that lifts engagement while raising churn is not a win.

**Analytics and instrumentation (full).** The events, properties, and dashboards needed to measure the metrics above. *Why:* metrics without instrumentation ship blind. *Expert note:* if the tracking plan is not in the PRD, the launch usually cannot measure its own success criteria.

**Dependencies (full).** Teams, services, data, approvals, and third parties this needs, with status. *Why:* the unwritten dependency is the classic mid-build blocker.

**Risks and mitigations (full).** What could go wrong and how you reduce or detect it. *Expert note:* a risk with no mitigation and no owner is decoration. Pair it with a premortem for high-stakes work.

**Rollout and release plan (full).** Phasing, flags, dates, rollback, comms. *Why:* how it reaches users is part of what to build. *Expert note:* tie this to the release-notes and launch-checklist artifacts rather than restating them.

**Open questions (lean).** A living list of the undecided: question, owner, needed-by. *Why:* surfaced unknowns are what make a PRD an honest living document rather than a frozen claim of certainty [[11]](#ref-11). *Expert note:* a PRD with no open questions is usually hiding them, not finished.

**Appendix (full).** Research, competitive notes, glossary, prior decisions. *Beginner trap:* burying a load-bearing decision here where reviewers miss it.

---

## 4. Variants and sizing

This bundle ships two weights, governed by a nesting rule: the **lean** PRD's sections are a strict subset of the **full** PRD's, in the same order, so a document can grow in place from lean to full without a re-author.

- **Lean** (summary, problem, goals and non-goals, target users, solution overview, success metrics, open questions). The default. Use it for a single feature, a spike, or an early idea. It maps to what practitioners call the **one-pager**, recommended as the starting point for most projects [[7]](#ref-7).
- **Full.** Use it when the cost of a misunderstanding is high: multiple teams, external dependencies, regulated or safety-relevant work, or a launch with real downside.

**The scaling signal:** add a full-only section the moment a real question it answers comes up (a dependency appears, an NFR gets contested, a rollout needs a flag). Do not pre-fill the full template out of diligence. The bias is toward the smallest variant that is still useful, because structure is a cost the reader pays every time [[11]](#ref-11).

---

## 5. Methodology lineage

The same three letters mean different things across schools. Knowing which school a reader is from prevents most arguments about "what a PRD should be."

- **Waterfall / Pragmatic.** The PRD is a formal, sequential deliverable following an MRD; detailed, sometimes dozens of pages, signed before design [[6]](#ref-6). Still appropriate where change is expensive (hardware, regulated systems).
- **Agile (general).** The PRD survives but slims down: a living, lightweight doc emphasizing shared understanding, user needs, and out-of-scope clarity over exhaustive detail [[10]](#ref-10)[[11]](#ref-11).
- **Scrum (specifically).** There is **no PRD**. The 2020 Scrum Guide recognizes only three artifacts, Product Backlog, Sprint Backlog, and Increment, with three commitments, the Product Goal, Sprint Goal, and Definition of Done. The Product Backlog is the requirement-capturing mechanism, which is why many Scrum teams never write a document called a PRD [[1]](#ref-1).
- **SVPG / discovery-led.** The PRD as a prose spec is actively de-emphasized in favor of the high-fidelity prototype as the primary specification, with written material as supporting context [[2]](#ref-2)[[3]](#ref-3)[[4]](#ref-4).
- **Amazon / Working Backwards.** The starting artifact is not a PRD but a **PR/FAQ**: a mock press release plus FAQ, written before building, that forces customer-value clarity. A PRD, if used, comes after the PR/FAQ to guide implementation. Amazon has used this since around 2004 for products including Kindle, Prime, and AWS [[5]](#ref-5).
- **Lean / one-pager.** The PRD compresses to a single page that leads with the problem and defers solution detail until the problem is agreed [[7]](#ref-7).

The practical reading: the PRD is methodology-agnostic as a *type*, but its weight, and whether it exists at all, is set by the methodology around it.

---

## 6. Debates and contested boundaries

Where serious practitioners genuinely disagree. Presented as live arguments, with a recommendation rather than a forced consensus.

**Is the PRD dead? (Prose vs prototype.)** The strongest critique, from Cagan and SVPG, is that prose specs fail at the one job a spec must do, communicating the intended experience precisely, and that a high-fidelity prototype does it better; "the majority of the product spec should be the high-fidelity prototype" [[2]](#ref-2)[[3]](#ref-3). The counter-view is that a prototype shows the *what* but not the *why*, the success criteria, the non-goals, or the constraints, and that a short companion document still carries those. *Recommendation:* treat the prototype as the source of truth for the experience and keep a lean PRD for the why, metrics, scope, and open questions. They are complements, not rivals.

**PRD vs PR/FAQ.** Amazon's PR/FAQ front-loads customer value before any spec; the press release forces you to justify *why it matters to a customer* before detailing *what gets built* [[5]](#ref-5). *Recommendation:* for genuinely new products, write the PR/FAQ first and let the PRD follow for implementation; for incremental features, a lean PRD alone is usually enough.

**PRD vs user stories.** Many agile teams replace the PRD with a backlog of stories plus acceptance criteria [[1]](#ref-1)[[12]](#ref-12). *Recommendation:* stories scale well for delivery but scatter the problem, metrics, and non-goals across many cards; keep a thin PRD as the connective tissue that the stories implement.

**MRD vs PRD vs BRD.** These blur in practice. The clean split: MRD = market problem and why; BRD = business needs and objectives; PRD = the product's what and how [[6]](#ref-6)[[12]](#ref-12). *Recommendation:* most modern teams fold the MRD's "why" into the PRD's problem and context sections rather than maintaining three documents.

**How long?** Waterfall says thorough; agile says one page. *Recommendation:* let the downside of a misunderstanding set the length. Low-stakes feature: one page. Multi-team, regulated, or irreversible: the full variant.

---

## 7. Anti-patterns and failure modes

The recurring ways a PRD goes wrong.

- **Feature-first, problem-thin.** The document opens with the solution and treats the problem as a sentence. This is the most common and most damaging failure; the fix is to spend disproportionate time on the problem [[7]](#ref-7).
- **No non-goals.** Without an explicit out-of-scope list, scope creeps silently [[11]](#ref-11).
- **Spec as a substitute for discovery.** Writing a detailed PRD for a solution that was never validated. Cagan's core caution: the PRD becomes a way to *look* rigorous while skipping the discovery that determines whether the thing should exist [[2]](#ref-2)[[4]](#ref-4).
- **Frozen document.** A PRD signed once and never updated, so it drifts from reality and the team stops trusting it. The antidote is the open-questions list and a living-document habit [[10]](#ref-10)[[11]](#ref-11).
- **Happy-path only.** Specifying the success case and leaving empty, loading, and error states to be invented during build.
- **Metrics defined after the fact.** Choosing success criteria once results are in, which guarantees a flattering read. Define them up front, with a guardrail.
- **Vanity metrics.** Tracking a number that can rise while the user outcome does not.
- **Detail in the wrong place.** Pixel-level UI in the PRD (it belongs in the prototype) or load-bearing decisions buried in the appendix.

---

## 8. Relationships to other artifacts

The PRD sits in a natural document lineage [[12]](#ref-12):

- **Upstream (precede it):** product strategy and roadmap (set the bet), discovery research and personas (validate the problem and user), opportunity solution trees or a problem statement (frame what is worth solving), and for new products a PR/FAQ or solution brief.
- **Sibling / inside it:** the high-fidelity prototype (often the real experiential spec the PRD points at), and analytics or measurement plans.
- **Downstream (follow it):** user stories and acceptance criteria (decompose it for delivery), the software design doc and ADRs (decide how to build it), the test plan (verify it), and release notes plus the launch checklist (ship it).

In this library the PRD pairs with the `deliver-prd` skill and relates to the `user-stories`, `acceptance-criteria`, and `release-notes` templates in the same `delivery-docs` family.

---

## 9. Adaptations

- **Solo or early-stage.** Use the lean variant, often just summary, problem, solution, and success metric. The one-pager is the right default [[7]](#ref-7).
- **Large or multi-team.** Use the full variant; the dependencies, risks, and rollout sections carry their weight when coordination is the hard part.
- **Regulated (health, finance, safety-critical).** The PRD feeds, and must trace to, formal requirements artifacts (SRS per ISO/IEC/IEEE 29148, requirements traceability matrices, design controls). Keep requirement IDs stable so downstream traceability holds [[12]](#ref-12).
- **Discovery-led teams.** Invert the center of gravity: prototype first, then a lean PRD that captures the why, metrics, scope, and open questions the prototype cannot [[2]](#ref-2)[[3]](#ref-3).
- **Amazon-style orgs.** Write the PR/FAQ first; the PRD is the implementation follow-on, not the starting point [[5]](#ref-5).

---

## 10. Worked example

See [`prd_example.md`](prd_example.md) for a complete, filled full-variant PRD for a realistic feature (a saved-views capability in an analytics product). It demonstrates a problem stated from the user's perspective with evidence, explicit non-goals, a primary metric paired with a guardrail, and an honest open-questions list. Illustrative figures in the example are labeled as such.

---

## References

Tagged by reliability: `[primary]` standards body, regulator, or originating source; `[practitioner]` recognized independent authority; `[vendor]` commercially motivated, reliable on convention. Researched 2026-06-30.

<a id="ref-1"></a>[1] Ken Schwaber and Jeff Sutherland. "[The 2020 Scrum Guide](https://scrumguides.org/scrum-guide.html)." scrumguides.org, 2020 (accessed 2026-06-30). [primary]

<a id="ref-2"></a>[2] Marty Cagan. "[Revisiting the Product Spec](https://www.svpg.com/revisiting-the-product-spec/)." Silicon Valley Product Group, **2006-10-12** (**fetched and verified 2026-07-16**). Verbatim: "But the majority of the product spec should be the high-fidelity prototype, representing the functional requirements, the information architecture, the interaction design, and the visual design of the user experience." [practitioner]

<a id="ref-3"></a>[3] Marty Cagan. "[How To Write a Good PRD](https://www.svpg.com/wp-content/uploads/2024/07/How-To-Write-a-Good-PRD.pdf)." Silicon Valley Product Group, 2024. **PDF; URL confirmed live 2026-07-16 (a prior 403 no longer reproduces), but the body was not read in this pass. Cited only as corroboration for the position [[2]](#ref-2) states verbatim; no claim rests on it alone.** [practitioner]

<a id="ref-4"></a>[4] Marty Cagan. "[Discovery vs. Documentation](https://www.svpg.com/discovery-vs-documentation/)." Silicon Valley Product Group. **URL confirmed live 2026-07-16 (a prior 403 no longer reproduces); body not read claim by claim in this pass. Cited as corroboration only.** [practitioner]

<a id="ref-5"></a>[5] Colin Bryar and Bill Carr. "[The Amazon Working Backwards PR/FAQ Process](https://workingbackwards.com/concepts/working-backwards-pr-faq-process/)." Working Backwards; see also Bryar and Carr, "Working Backwards: Insights, Stories, and Secrets from Inside Amazon," 2021 (accessed 2026-06-30). [practitioner]

<a id="ref-6"></a>[6] Pragmatic Institute. "[Writing the Market Requirements Document](https://www.pragmaticinstitute.com/resources/articles/product/writing-the-market-requirements-document/)." pragmaticinstitute.com (accessed 2026-06-30). [practitioner]

<a id="ref-7"></a>[7] Lenny Rachitsky. "[Examples and templates of 1-Pagers and PRDs](https://www.lennysnewsletter.com/p/prds-1-pagers-examples)." Lenny's Newsletter. **PAYWALLED: the page returns "This post is for paid subscribers" and the article body is not readable (checked 2026-06-30 and 2026-07-16). Nothing is quoted from it, and claims it is cited for are corroborated from the free portion and from [[8]](#ref-8), which reproduces the template itself.** [practitioner]

<a id="ref-8"></a>[8] "[Lenny's Product Requirements template](https://www.atlassian.com/software/confluence/templates/lennys-product-requirements)." Atlassian Confluence Templates, created by Lenny Rachitsky (**fetched and verified 2026-07-16**). The freely readable rendering of the template whose source post [[7]](#ref-7) is paywalled: sections run Description, Problem, Why, Success, Audience, then "What does this look like in the product?", and step one is "Crystallize the problem you are solving". [vendor]

<a id="ref-9"></a>[9] ProductPlan. "[Product Requirements Document (PRD)](https://www.productplan.com/glossary/product-requirements-document/)." ProductPlan Glossary (accessed 2026-06-30). [vendor]

<a id="ref-10"></a>[10] Atlassian. "[What is a Product Requirements Document (PRD)?](https://www.atlassian.com/agile/product-management/requirements)" atlassian.com (accessed 2026-06-30). [vendor]

<a id="ref-11"></a>[11] Figma. "[How To Create a Product Requirements Document](https://www.figma.com/resource-library/product-requirements-document/)." Figma Resource Library (accessed 2026-06-30). [vendor]

<a id="ref-12"></a>[12] "[Master Catalog of Product Management and SDLC Document and Artifact Types](../../docs/internal/catalog.md)," entry 29 (PRD). Internal deep-research catalog, 2026. [internal]
