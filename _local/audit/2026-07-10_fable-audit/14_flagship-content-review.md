# Flagship Content Review: Is the PRD Bundle Actually Best-in-Class?

- **Date:** 2026-07-11
- **What this is:** the review the audit did not perform. Dimension A verified the PRD bundle's research *mechanics* (citations resolve, sources support claims, examples are labeled); nobody judged the *substance*: is the advice at the level of the best practitioner writing on PRDs, or merely well-organized and well-cited? The "best-in-class" claim ultimately lives here.
- **Method and epistemic status:** a single-reviewer editorial critique of the full PRD bundle (companion, guide, example, templates) at maximum reasoning depth, judged against the strongest published PRD writing and real senior-practitioner standards. These are **editorial judgments, not adversarially verified findings**; confidence is marked per item. IDs are CR-nn (content review) to keep them distinct from audit finding IDs.
- **Verdict up front:** the bundle is genuinely good, top quartile of published PRD explainers, and the example is better than most real PRDs. Against "indisputable best-in-class" it grades **B+**. Four substantive gaps separate it from an A, all fixable in one focused revision pass (template_version 0.1.0 to 0.2.0).

---

## 1. What is genuinely excellent (specific, so the bar is visible)

- **The thesis sentence earns its place:** "a PRD is a forcing function for shared understanding. Its value is the alignment it creates, not the pages it produces" (companion:23). That is the correct center for the whole artifact, stated better than most sources say it.
- **Expert notes that are actually expert.** "If you cannot write this paragraph, the work is not yet shaped enough to spec; that is a signal, not a formatting problem" (companion:44). "A PRD with no open questions is usually hiding them, not finished" (companion:74). "A risk with no mitigation and no owner is decoration" (companion:70). These are the sentences a 15-year PM says; their presence is what makes the companion feel senior rather than aggregated.
- **The debates section referees instead of flattening.** The prototype-vs-prose treatment (companion:110) gives Cagan's position its full force, states the counter precisely ("a prototype shows the what but not the why, the success criteria, the non-goals"), and lands a usable synthesis (complements, not rivals). This is the hardest editorial move in the genre and it is executed well.
- **The example models reasoning, not just structure.** Non-goals carry *why* ("raises hard scoping and permissions questions we do not need to answer yet," example:59-60); the rollback plan notes saved data is retained "so re-enabling is safe" (example:153-154); the stale-view and permission-edge states (example:109-116) are exactly the unhappy paths real PRDs omit. The open question "what magnitude counts as success?" models honesty about an unset target.
- **The guide's rubric contains one genuinely clever check:** "The problem section is meatier than the solution section" (guide:29) is a mechanical, self-gradable proxy for the deepest failure mode in the genre. Good rubric design is rare; this is good rubric design.

---

## 2. The gaps between B+ and A

### CR-1: The AI-era debate is missing, and it is this library's home turf (confidence: high; impact: highest)

The companion's evolution story ends at discovery-led product (2007-2024). As of the 2026-06-30 research date, the live practitioner conversation the companion does not touch: what a PRD is *for* when AI agents draft, prototype, and implement from it. Three positions are actually contested in the field right now: (a) the PRD becomes MORE load-bearing because it is the context/intent artifact agents consume (spec-driven development); (b) near-free AI prototyping finally settles Cagan's argument in favor of prototype-as-spec; (c) the durable spec shrinks to intent, constraints, non-goals, and acceptance/eval criteria, with everything else generated. A library whose entire positioning is agent-native, whose templates carry machine metadata precisely so agents can fill them, is silent on this debate inside its flagship companion. This is the one section where the library could be the *defining* voice rather than an excellent synthesizer.

**Fix:** add a section 6 debate entry ("Does AI change what a spec is for?") via the methodology's own A-phase protocol: run the research sweep, cite real 2024-2026 sources, name the camps, recommend (the library's natural position is a strong version of (c): the PRD as the intent-and-constraints contract that both humans and agents fill against, which also happens to be the argument for this library's existence). Candidate source families to verify during research, marked (unverified) here per house rules: SVPG's recent AI-era essays, spec-driven-development writing from major AI labs and tools, Lenny's Newsletter AI-PM coverage. Do not add the section without sources; cite-or-cut applies.
**Effort:** M (one research-and-write session). Also update the guide's "When NOT to use" with one AI-era line.

### CR-2: The measurement teaching stops exactly where it gets hard (confidence: high)

The companion instructs "define metrics in advance and pick a guardrail" (companion:64) and the example complies, but neither teaches the two things senior reviewers actually probe: **how to set the magnitude** and **how to attribute the change**. The example's primary metric is direction-only ("Target direction: down; magnitude to be set with the data team," example:121), which the open-questions list honestly flags, but the companion never warns that a direction-only target is unfalsifiable (any decline can claim success). Sharper still: the example's own rollout plan contains a better measurement design than its measurement plan uses. Phase 3 rolls out via flag at 10, 50, 100 percent (example:151-152), which is a natural experiment; yet the measurement window is a pre/post cohort comparison (example:123) vulnerable to seasonality and mix shifts. The document teaches instrumentation discipline, then leaves its strongest identification strategy sitting unused in the adjacent section.

**Fix:** (a) companion anatomy, success-metrics expert note: add two sentences on target-setting (baseline first, then a minimum worthwhile effect) and one on attribution (if you are rolling out by flag percentage, the holdback IS your control group; use it). (b) Example: one line in Success metrics using the Phase 3 holdback as the comparison. (c) Guide rubric: upgrade the metric item to "primary metric has a baseline and a target magnitude, or names when the target will be set and by whom."
**Effort:** S. This single fix hardens the bundle exactly where LP-2 gradings will be judged by data-literate reviewers.

### CR-3: The evidence teaching is interview-only; best practice triangulates (confidence: high)

The companion's problem-section guidance and the example's problem statement both rest on qualitative evidence (9 of 12 interviewed analysts, a personal-text-file anecdote). That is good evidence, well-deployed. But the fictional product is an *analytics product*; a senior reviewer's first question is "you have telemetry; what does it say?" The example cites no behavioral data in the problem statement, then demonstrates full instrumentation fluency later (example:127-130). The companion never teaches evidence triangulation (qualitative + behavioral + cost quantification) as the standard for "evidence it is real and worth solving now."

**Fix:** companion problem-section expert note gains one sentence on triangulation; example problem gains one behavioral line ("instrumentation shows a median of N filter reconfigurations per active analyst per day (illustrative)") and a rough cost line. Three sentences total.
**Effort:** S.

### CR-4: No "alternatives considered," in the anatomy or the example (confidence: medium-high)

The example moves from problem directly to the chosen solution (a Views control). A reviewer immediately asks: why this shape and not shareable filter URLs, pinned per-dashboard defaults, or browser bookmarks of parameterized links, all cheaper and common in analytics products? The strongest real PRDs (and several of the best published templates) carry a short "alternatives considered" or "solution rationale" block, and its absence here is felt because everything else models reasoning so well. The companion's anatomy has no section for it either, and the debates section (which loves contested ground) never mentions that solution-rationale-in-the-PRD is itself contested (some schools push it to the design doc or RFC).

**Fix:** add "Alternatives considered (full)" to the full template between Solution overview and User stories: 2-4 rows (option, why not, what would change our mind). Under the nesting rule this is a safe full-only addition (lean unchanged); it is a template_version 0.2.0 change with a history entry. Add the anatomy entry, one example block (URL-sharing considered and rejected because links rot and cannot be defaulted; a one-line "what would change our mind"), and one guide rubric line for the full variant.
**Effort:** S-M. Note: this touches template structure, so it re-runs the whole gate and (post-EV-1) the eval regression, which is exactly how the governance is supposed to absorb content evolution.

### CR-5: The example's requirements do not quite trace to its stories, under a family that advertises traceability (confidence: high; scope: narrow)

The PRD example declares six functional requirements but its user-stories section carries four stories: FR-2 (list and switch views) is only weakly implied by story 1, and FR-6 (stale-view indication) has no story at all (example:87-96 vs 78-85). The sibling user-stories example does cover stale-view behavior, but as an acceptance criterion inside the set-default story, and that document is explicitly a representative set, not a decomposition. None of this is a gate violation, and the README's "traceable set" claim holds at the persona/metric level the audit verified. But in a library whose differentiation includes traceability, the flagship example's internal FR-to-story map having a visible gap is the kind of thing a sharp evaluator will find, because I just did.

**Fix:** either add the two missing stories to the example (cleanest), or add one line under the stories: "Representative stories; the full decomposition lives in the backlog; every Must/Should FR must map to at least one story before build." The second option also *teaches* the mapping discipline, which is arguably the better outcome. Update the guide rubric (full variant): "Every Must/Should functional requirement maps to at least one story."
**Effort:** S.

### CR-6: The one-pager claim vs the catalog's own sizing signal (confidence: medium; governance note)

The companion equates the lean variant with "what practitioners call the one-pager" (companion:84), but lean carries seven sections and fills to roughly two pages; the companion's own adaptations section admits solo users often need "just summary, problem, solution, and success metric" (companion:151). Meanwhile the catalog's entry for the PRD says this type earns S/M/L, three weights, and the bundle shipped two. That divergence is defensible under the variant-model decision ("let the type decide") but is documented nowhere. Either the PRD genuinely earns a true one-page S variant (four sections, nesting inside lean), or the two-size decision should be recorded with its reasoning.

**Fix:** one-paragraph decision note (fits the ADR set or the bundle history): "PRD ships lean/full; the catalog's S signal is served by the lean variant used partially; a true S variant is deferred until a real user asks for it." Or, if LP-2 gradings show most real docs are nearer four sections than seven, ship the S variant then, with the nesting rule making it painless.
**Effort:** S to document; M if the S variant is ever built.

### CR-7: Minor editorial notes (confidence: medium; all Low)

- The user-stories example's outline uses "## Lean card" followed by "## Story" at the same heading level, so the document outline reads flat and contains two identical "## Story" headings; imperfect modeling in a library that teaches structure (user-stories_example.md:28-30,46-48).
- The guide's "When NOT to use" is strong but silent on the political case every operator card should arm its reader for: what to do when stakeholders demand a heavyweight PRD for lean-scope work (one sentence of organizational judo: "agree the full sections as open questions with owners rather than filling them speculatively").
- Companion section 8 references a "solution brief" artifact the library does not ship (same world as audit finding B-05, dangling references); fine to mention upstream artifacts, but flag it as outside the library or link the catalog entry.
- Debates section could carry one more live argument that is genuinely contested: who writes the PRD in an empowered-team model (PM solo vs trio co-authorship). Worth adding only with sources, per cite-or-cut.

---

## 3. The revision plan (one pass, one version bump)

1. Run CR-2, CR-3, CR-5, CR-7 fixes (all S; roughly half a day with verification).
2. Run CR-1 as a proper A-phase research task, then the write (M; this is the pass that moves the companion from synthesis to voice).
3. Run CR-4 (template change + example + anatomy + rubric; version 0.1.0 to 0.2.0, history entries, full gate).
4. Record CR-6 as a decision note.
5. Re-run the gate; when EV-1 exists, this revision becomes the first real test of the regression harness (the eval gap should hold or improve; if it drops, the harness just earned its keep).
6. Apply the same review to the other three bundles before they are declared L3: the specific gaps that likely replicate are CR-2's measurement thinness (acceptance-criteria bundle: are thresholds taught as testable?) and CR-3's triangulation (release-notes: is "what changed" backed by usage claims?). Budget a half-day each.

## 4. The meta-point

This review is what the EV-3 red-team protocol looks like in practice, executed once by the strongest available reviewer. Its findings are editorial, but its *shape* (quote-anchored, fix-attached, severity-honest, distinct IDs, one revision pass, version bump, regression re-run) is repeatable. Fold it into the methodology as the content-excellence pass that gates L3 conformance: structure is checked by the gate, research integrity by the citation census, and substance by exactly this review.
