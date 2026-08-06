---
title: "{{investment_name}} Business Case"
investment_name: "{{investment_name}}"
sponsor: "{{sponsor}}"
stage: "{{stage}}"
status: "{{status}}"
last_updated: "{{date}}"
doc_type: business-case
size: lean
source_template: business-case
source_template_version: 0.1.0
---

<!--
LEAN BUSINESS CASE. The smallest case that is still a real case: the problem or opportunity worth acting on,
the alternatives it was actually weighed against including doing nothing, and the recommendation that
follows from that comparison. Use it to scope a decision before real money or a procurement commitment is at
stake, close to what a staged model calls a Strategic Outline Case. To grow it into a case that can actually
be funded (see business-case_template-full.md), ADD sections between Options Considered and Recommendation;
never rename or reorder the ones below, because the full variant is a strict superset of this one.

The frontmatter `stage` field names where this sits if your organization stages its cases (Strategic Outline
Case / Outline Business Case / Full Business Case, or your own equivalent gates); write "N/A" if it does not.

A BUSINESS CASE IS A LIVING DOCUMENT, NOT A ONE-TIME GATE. Every standard this library's research could read
in full treats it as revisited as the work proceeds, checked and updated as assumptions firm up, not filed
once at approval and never reopened. Most people use it as a one-time gate anyway; closing that gap is this
document's whole point. See business-case_companion.md section 1 and section 7.

WHAT A BUSINESS CASE IS, AND IS NOT
It decides whether an investment is worth making and says plainly what it is being compared against,
including doing nothing. It is NOT a project brief (a short overview that absorbs an outline business case as
one component and then retires once initiation documentation exists), NOT a trade study (a bounded technical
comparison whose output feeds Options Considered as one input), and NOT a PRD (which specifies what to build
once this document's investment decision has already been made). See business-case_companion.md section 8.

HOW TO FILL THIS IN
1. Read the comment under each heading: WHAT it wants, WHY it matters (with a pointer into
   business-case_companion.md), guiding questions to ASK, a GOOD and a WEAK example, and the TRAP to avoid.
   For the table, PRIORITY explains the ordering rule and ROW HINT says what a good row contains.
2. Replace each {{placeholder}} with your content. Name a do-nothing option in Options Considered even if you
   reject it in one line; a case naming no alternative is a proposal wearing a bigger name.
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
           option's status as the one carried forward into the Recommendation.
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
     ASK   Which option is recommended? Why, given the comparison in Options Considered above? What decision
           or approval is being asked for, and by when? Who checks whether the expected benefits actually
           showed up after go-live, and when?
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
