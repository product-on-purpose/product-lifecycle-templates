---
title: "{{investment_name}} Business Case"
investment_name: "{{investment_name}}"
sponsor: "{{sponsor}}"
stage: "{{stage}}"
status: "{{status}}"
last_updated: "{{date}}"
financial_model_ref: "{{financial_model_ref}}"
doc_type: business-case
size: full
source_template: business-case
source_template_version: 0.1.0
---

<!--
FULL BUSINESS CASE. The case that can actually be funded: everything the lean variant carries, plus Costs,
Benefits, Risks and Financials inserted between Options Considered and Recommendation, the four sections a
reader needs to commit real money rather than merely agree the idea is worth exploring. Use it once you are
past scoping, roughly where a staged model moves from a Strategic Outline Case to an Outline or Full Business
Case, and where the tolerance for unexamined optimism should shrink accordingly.

THIS VARIANT IS A STRICT SUPERSET OF THE LEAN ONE. The three lean sections appear here under the same
headings and in the same order, with the same placeholders; four sections are inserted between Options
Considered and Recommendation. If you started lean, grow into this without rewriting anything you already
filled in.

The frontmatter `stage` field names where this sits if your organization stages its cases (Strategic Outline
Case / Outline Business Case / Full Business Case, or your own equivalent gates); write "N/A" if it does not.

A BUSINESS CASE IS A LIVING DOCUMENT, NOT A ONE-TIME GATE. Every standard this library's research could read
in full treats it as revisited as the work proceeds, not filed once at approval and never reopened. PRINCE2
makes this a named principle with a real consequence: if the case stops being justified, the work it justifies
should stop too. See business-case_companion.md section 1 and section 5.

WHAT A BUSINESS CASE IS, AND IS NOT
It decides whether an investment is worth making and says plainly what it is being compared against, including
doing nothing. It is NOT a project brief (a short overview that absorbs an outline business case as one
component, then retires once initiation documentation exists), NOT a trade study (a bounded technical
comparison whose output feeds Options Considered as an input), and NOT a PRD (which specifies what to build
once this document's investment decision has already been made). See business-case_companion.md section 8.
A hypothesis-driven alternative also exists for teams that would rather validate an assumption cheaply than
build a funding case for a known investment; it is a genuinely different document, not a shorter one, and is
not shipped in this library. See business-case_companion.md section 4 and section 9.

HOW TO FILL THIS IN
1. Read the comment under each heading: WHAT it wants, WHY it matters (with a pointer into
   business-case_companion.md), guiding questions to ASK, a GOOD and a WEAK example, and the TRAP to avoid.
   For tables, PRIORITY explains the ordering rule and ROW HINT says what a good row contains.
2. Replace each {{placeholder}} with your content. Options Considered still needs a do-nothing baseline; the
   four inserted sections turn that comparison into a case that can actually be funded.
3. If a section does not apply, write "N/A" and one line of why, rather than deleting it.
4. This document is never really finished, but before you circulate it for a decision: self-grade against
   business-case_guide.md, then DELETE every HTML comment. They are guidance, not content.
-->

# {{investment_name}} Business Case

## Problem and Opportunity

<!-- WHAT  The problem or opportunity this investment addresses, who it affects, and why it matters now,
           described without naming the solution you already have in mind.
     WHY   Everything below has to answer to this section; treat it as foundational to the whole case rather
           than as background. It drives which options in the next section are even worth comparing. Deep
           dive: business-case_companion.md section 3 (Anatomy > Problem and Opportunity).
     ASK   What problem or opportunity is this? Who is affected, and how do you know? Why does it matter now
           rather than later? What happens if nothing changes?
     GOOD  "Analysts rebuild the same dashboard filters an average of three times a day, according to the
           2026-05 friction study; at current headcount that is a recurring tax on the team's scarcest
           resource, and it worsens as the analyst segment grows."
     WEAK  "We should build saved views." (a solution stated as if it were the problem; the next section has
           nothing genuine left to compare it against)
     TRAP  Naming a solution instead of a problem. If the "problem" is already the answer you want, Options
           Considered below cannot do its job, because the real comparison never happens. -->

{{problem_and_opportunity}}

## Options Considered

<!-- WHAT  At least two genuine alternatives, including a do-nothing baseline, with what each would involve
           and why it was accepted, carried forward, or rejected.
     WHY   This is the load-bearing section, and the one most likely to be skipped under time pressure.
           Standards disagree about where it sits in the document, some fold it inside a wider case, some
           give it a standalone heading, but none treats comparison against a named alternative, including
           doing nothing, as optional in substance. A case that skips this section is a proposal, whatever
           its own heading claims. Deep dive: business-case_companion.md section 3 (Anatomy > Options
           Considered), section 6 (the section-order debate), section 7 (anti-patterns).
     ASK   What are the realistic alternatives, including doing nothing? What would each concretely involve?
           Why was each accepted, carried forward, or rejected? Which one do you expect to recommend?
     PRIORITY  Every case needs a do-nothing row, even when it is rejected in one line. Mark exactly one
           option's status as the one carried forward into Costs, Benefits, Risks and Financials.
     ROW HINT  A good row names a real option, states plainly what it would take, and gives a genuine reason
           for its status. A weak row is a label with no content, or a straw-man option deliberately built to
           lose.
     GOOD  | OPT-2 | Build saved views into the existing dashboard shell | Reuses the current filter and
           permissions model; estimated 6 engineer-weeks | Carried forward |
     WEAK  | OPT-2 | Build it | Because it's the obvious answer | Recommended |
     TRAP  Including a deliberately weak straw-man alternative so the preferred option wins the comparison by
           default. Every option here should be one a reasonable reader could actually choose. -->

| ID | Option | What it would involve | Why accepted, carried forward, or rejected | Status |
|---|---|---|---|---|
| {{option_id}} | {{option_name}} | {{option_description}} | {{option_rationale}} | {{option_status}} |

## Costs

<!-- WHAT  The cost of the recommended option, broken down by category, with an explicit optimism-bias
           adjustment shown separately from the base estimate.
     WHY   Optimism enters a business case first and most invisibly in its cost estimate. The documented
           remedy is an explicit, empirically grounded adjustment, not vigilance alone, and the tolerance for
           skipping that adjustment should shrink as the decision gets closer to a real commitment. Showing
           the adjustment separately from the base number is what lets a reviewer actually see it, rather
           than trust a single already-adjusted total. Deep dive: business-case_companion.md section 3
           (Anatomy > Costs), section 7 (anti-patterns).
     ASK   What are the cost categories (one-time build, ongoing run, other)? What is the base estimate for
           each, before any adjustment? What optimism-bias or contingency adjustment did you apply, and on
           what basis? What is the adjusted total?
     PRIORITY  One row per cost category. Show the base estimate and the adjustment as separate columns; a
           total with no visible adjustment hides the exact number a reviewer needs to sanity check.
     ROW HINT  A good row names the category, states a base estimate, states an adjustment with its basis,
           and gives the adjusted figure. A weak row is a single lump total with no breakdown and no visible
           adjustment.
     GOOD  | Engineering build | $180,000 base (6 engineer-weeks at loaded rate) | +20% (prior saved-feature
           builds in this codebase ran 15-25% over initial estimate) | $216,000 |
     WEAK  | Total cost | about $200,000 | | |
     TRAP  Presenting only the already-adjusted total. Without the base estimate and the adjustment shown
           separately, nobody can tell whether the optimism problem was addressed or just hidden. -->

| Category | Base estimate | Optimism-bias adjustment (and basis) | Adjusted estimate |
|---|---|---|---|
| {{cost_category}} | {{base_estimate}} | {{optimism_adjustment}} | {{adjusted_estimate}} |

## Benefits

<!-- WHAT  The expected benefits, tangible and intangible, each stated as a measurable range with the method
           behind it, not a single confident-sounding figure.
     WHY   This is the section most tempted by false precision. An honest range is more persuasive than
           fabricated precision, and a benefit that cannot be measured with ordinary accounting is not
           therefore nonexistent, it needs a proxy or a stated switching value instead. Do not reach for the
           familiar benefits-realisation percentages that circulate in practitioner writing; this bundle's
           own research could not verify them, and an unverifiable number does not become more credible by
           repetition in your own case either. Deep dive: business-case_companion.md section 3 (Anatomy >
           Benefits), section 7 (anti-patterns).
     ASK   What benefits are expected, tangible and intangible? What is the measurable range for each, and
           what is it based on? How and when will you know whether it actually happened?
     PRIORITY  Order benefits by expected magnitude or strategic importance. A benefit line with no
           measurement method is a hope, not a benefit.
     ROW HINT  A good row names the benefit, gives a range rather than a false point estimate, states its
           type, and names how it will be measured. A weak row is an adjective with no number and no method.
     GOOD  | Analyst time saved | Tangible | 8-15 minutes/analyst/day, based on the friction study's observed
           rebuild frequency | Measured via the saved-view usage event against the pre-launch baseline |
     WEAK  | Improves analyst productivity | | significantly | |
     TRAP  Citing a well-known benefits-realisation statistic, the kind of percentage that circulates with a
           name attached but resists tracing to its source, as settled fact. If you cannot point to where a
           number came from, state a range and say so, rather than borrow someone else's unverified one. -->

| Benefit | Type (tangible / intangible) | Estimated range (and basis) | Measurement method |
|---|---|---|---|
| {{benefit_name}} | {{benefit_type}} | {{benefit_range}} | {{measurement_method}} |

## Risks

<!-- WHAT  The risks that could make this case wrong, distinguishing self-deceived optimism from a
           deliberately oversold case, each with a named owner and a stated trigger for revisiting the
           recommendation.
     WHY   Forecasts go wrong for at least two different reasons, not one: optimism bias is self-deception,
           strategic misrepresentation is deliberate, and the two work as complementary mechanisms rather
           than competing ones, so naming the wrong one misses the actual failure. A third, distinct pattern,
           decision-based evidence making, can happen even with no competing proposal in sight, simply to
           support a decision someone has already made. This section tracks risk to the DECISION itself; it
           is not the delivery risk register for the resulting project. Deep dive:
           business-case_companion.md section 3 (Anatomy > Risks), section 6 (the two-mechanism debate),
           section 7.
     ASK   What could make this case's recommendation wrong? Is the likely driver closer to self-deception or
           to deliberate overselling? Who owns each risk to the case, distinct from whoever will own delivery
           risk later? What would trigger revisiting the recommendation?
     PRIORITY  Order by how much the recommendation would change if the risk materialized. Every row needs a
           named owner; an unowned risk to the case is a risk nobody will notice crystallizing.
     ROW HINT  A good row names a risk to the RECOMMENDATION, not to delivery, states which mechanism is more
           likely at work, names an owner, and states a concrete trigger for reopening the case. A weak row
           is a generic worry with no owner and no trigger.
     GOOD  | The 6-engineer-week estimate assumes no permissions-model rework; if platform's Q3 refactor
           lands first, effort could double | Optimism bias (unverified assumption, not deliberate) | Priya
           Nair | Revisit the case if the refactor's scope is confirmed before build starts |
     WEAK  | Might cost more than expected | | Engineering | |
     TRAP  Reusing the delivery project's risk register here unchanged. A risk that would change what gets
           built belongs in that register; a risk that would change whether this recommendation still holds
           belongs here. -->

| ID | Risk to the case | Mechanism (optimism bias / strategic misrepresentation / other) | Owner | Trigger to revisit the case |
|---|---|---|---|---|
| {{case_risk_id}} | {{case_risk_statement}} | {{case_risk_mechanism}} | {{case_risk_owner}} | {{case_risk_trigger}} |

## Financials

<!-- WHAT  The discount rate and its basis, followed by the financial metrics your organization uses (NPV,
           IRR, payback, ROI, or a subset), each with a plain-language caveat tied to that metric's known
           limit.
     WHY   This is the most technically dense section, and the one where a bare number is the least
           trustworthy form it can take. State the discount rate before the metrics, since every number
           below depends on it. Each of the common metrics has a documented limit worth naming rather than a
           single "the number" figure. The claim that IRR assumes reinvestment at the IRR rate is genuinely
           contested between academic and practitioner sources; state which convention you are following
           rather than asserting either side as simply settled. Deep dive: business-case_companion.md
           section 3 (Anatomy > Financials), section 6 (the IRR and real-options debates).
     ASK   What discount rate did you use, and where did it come from (a corporate hurdle rate, a published
           guidance rate, a cost of capital)? What is the NPV, IRR, payback period, and/or ROI for the
           recommended option? What does each metric's known limit mean for how much weight a reader should
           put on it? If you weighed real options, such as the value of delaying, expanding or abandoning, say so in
           the prose above the table rather than as a metric row.
     PRIORITY  State the discount rate and its source in prose before the table. Never use a benefit-cost
           ratio, or any single metric, as a mechanical accept-or-reject threshold; a lower ratio can still
           represent good value once benefits you could not monetize are weighed in.
     ROW HINT  A good row states the metric, its value, and a plain-language caveat drawn from that metric's
           real limit. A weak row is a bare number with no caveat, or a threshold applied as if it were a
           rule.
     GOOD  | IRR | 24% over 3 years | Tells you the rate of return, not the dollar size of the opportunity;
           read it alongside NPV, not instead of it |
     WEAK  | IRR | 24% | Approved |
     TRAP  Using a BCR, IRR, or any single ratio below a round-number threshold as an automatic reject. A
           ratio that clears a threshold is not automatically good value, and one that misses it is not
           automatically bad; both need the reasoning stated, not just the number. -->

{{discount_rate_and_basis}}

| Metric | Value | Caveat |
|---|---|---|
| {{financial_metric}} | {{financial_value}} | {{financial_caveat}} |

## Recommendation

<!-- WHAT  The recommended option, the reasoning that follows from everything above it, the decision being
           asked for, and how the case will be checked after go-live.
     WHY   This is where the case commits, and it should read as the conclusion the analysis above earns, not
           as the starting point everything else was built to justify. Written the other way round, it is
           indistinguishable from a decision already made being dressed up with evidence after the fact. The
           sponsor named in the frontmatter is accountable for what this section states. It is also the
           section the sources this bundle could read leave unfinished: they describe how the case is
           revised up to approval, but none names who checks it after go-live, so state that check explicitly
           rather than leaving it assumed. Deep dive: business-case_companion.md section 3 (Anatomy >
           Recommendation), section 6 (decision-based evidence making), section 7.
     ASK   Which option is recommended? Why, given the comparison, costs, benefits, risks and financials
           above? What decision or approval is being asked for, and by when? Who checks whether the expected
           benefits actually showed up after go-live, and when?
     GOOD  "Recommended: OPT-2 (build saved views into the existing shell). It clears the comparison in
           Options Considered on cost and reuses the current permissions model, avoiding OPT-3's rebuild
           risk. Decision requested: funding approval at the 2026-08-20 steering review. Post-go-live check:
           the sponsor reviews adoption and time-to-insight against this case's targets 90 days after GA."
     WEAK  "We recommend building saved views because it's the right thing to do." (no link back to the
           comparison, no decision named, no post-go-live check; nothing here follows from anything above it)
     TRAP  Writing this section first and backfilling the sections above it to support a decision already
           made. That is decision-based evidence making, and it can happen even when nobody is competing for
           the funding. -->

- Recommended option: {{recommended_option}}
- Why: {{recommendation_rationale}}
- Decision requested: {{decision_requested}}
- Post-go-live check: {{post_go_live_check}}
