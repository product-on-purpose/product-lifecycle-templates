---
title: "{{product_name}} Product Roadmap"
product: "{{product_name}}"
owner: "{{who_owns_this_roadmap}}"
horizon: "{{period_this_covers}}"
audience: "{{internal_or_customer_facing}}"
status: "{{draft_or_agreed}}"
last_updated: "{{date}}"
doc_type: product-roadmap
size: full
format: themes
source_template: product-roadmap
source_template_version: 0.1.0
---

<!--
PRODUCT ROADMAP, THEMES FORMAT. The fullest of the three: it carries the vision and the business objectives
alongside the work, so the roadmap can argue for itself rather than assuming the reader already agrees.

WHEN TO REACH FOR THIS INSTEAD OF THE OTHER TWO. Now-next-later sorts by confidence and assumes the reader
already knows why. The GO format sorts by release and assumes releases matter. This one is for when the
roadmap has to travel: to a board, to a new leader, to a function that has never read your strategy, or into
a room where someone will ask "why these things and not others?" It is the only one of the three that
answers that question inside the document.

WHERE THIS SHAPE COMES FROM, AND WHAT THIS BUNDLE ADDED. It is the structure set out in Product Roadmaps
Relaunched (Lombardo, McCarthy, Ryan and Connors, 2017): Product Vision, Business Objectives, Themes,
Timeframes, and a Disclaimer. IMPORTANT PROVENANCE NOTE: this bundle's research could not obtain the book
itself, and that structure is taken from a third-party summary. Treat the five-part shape as
summary-reported rather than quoted from the authors. ONE SECTION IS THIS BUNDLE'S ADDITION: "What Is Not On
Here". See product-roadmap_companion.md section 4.

WHAT A THEME IS, AND WHY IT IS NOT A FEATURE CATEGORY. The clearest published definition: "Themes are an
alternative for features. Instead of promising to build a specific feature, the team commits to solving a
specific customer problem." A theme named "Reporting" is a feature category wearing a theme's clothes. A
theme named "Dispatchers cannot tell which job is urgent" is a problem someone can succeed or fail at.

THE DISCLAIMER IS A REAL SECTION, NOT BOILERPLATE. It is in the published structure because a roadmap that
travels gets read as a commitment. Note the limit honestly: a disclaimer does not actually undo that. Once a
customer has read a date, "the customers who read it will still hold you to it."

WHAT THE EVIDENCE ACTUALLY SAYS. No study links any roadmap format to outcomes. See
product-roadmap_companion.md section 1.

HOW TO FILL THIS IN
1. Read the comment under each heading: WHAT, WHY (with a companion pointer), ASK, GOOD, WEAK, TRAP.
2. Replace each {{placeholder}} with your content.
3. Write the objectives before the themes. A theme that serves no stated objective is the thing this format
   exists to make visible.
4. If a section does not apply, write "N/A" and one line of why.
5. Before you share it: self-grade against product-roadmap_guide.md, then DELETE every HTML comment.
-->

# {{product_name}} Product Roadmap

## Product Vision

<!-- WHAT  Two or three sentences on the future this product is trying to create. If a vision document
           exists, summarise it and link it rather than rewriting it.
     WHY   This format exists to let the roadmap argue for itself, and the argument starts here. A reader
           who does not know where the product is going cannot judge whether these themes move it there.
           Deep dive: product-roadmap_companion.md section 3 (themes format) and section 8.
     ASK   Does a vision document already exist, and does this match it? Would the person who wrote it
           recognise this summary? Is this a destination, or a restatement of what we already do?
     GOOD  "Dispatchers send the right van to the right job without reading a note, and trust the order the
           system proposes enough to stop rebuilding it by hand. See the product vision document for the
           full statement."
     WEAK  "To be the leading field-service platform." (a market position, not a future for a user)
     TRAP  Writing a new vision here because you cannot find the old one. Two visions is worse than none;
           people will cite whichever suits them. -->

{{product_vision}}

## Business Objectives

<!-- WHAT  The measurable business outcomes this roadmap serves, two to four, each with a number and a
           period.
     WHY   Objectives are what make a theme refusable: without them, any plausible-sounding theme belongs.
           Published guidance on alignment is explicit that a vision has to be "transformed into a strategy
           with clear goals that can be integrated into a product roadmap and communicated across the
           organization" - this section is that integration point. Deep dive:
           product-roadmap_companion.md section 3 (themes format).
     ASK   Whose objectives are these, and did they agree? Which one would each theme below move? Is there
           an objective here that no theme serves, and if so, why is it here?
     GOOD  "1. Cut median emergency response time by a third by end of FY26. 2. Hold support cost per
           account flat while accounts grow 40 percent."
           (numbers, periods, and they pull in different directions, which is what makes trade-offs real)
     WEAK  "Grow revenue, improve retention, delight customers." (no numbers, no period, no trade-off)
     TRAP  Listing objectives your roadmap does not actually serve, because they look good on the page. A
           reader will match themes to objectives, and the mismatch is what they will remember. -->

{{business_objectives}}

## Themes

<!-- WHAT  The problems this roadmap commits to solving, three to six, each tied to an objective above.
           Problems, not features.
     WHY   The theme is the unit that makes this format honest: it commits to solving a customer problem
           rather than to shipping a named thing, which is what lets the team change its mind about the
           solution without breaking its word. Deep dive: product-roadmap_companion.md section 3 (themes format)
           and section 7.
     ASK   Is each of these a problem or a solution? Which objective does it serve, and how would we know
           it moved? If we solved this a completely different way than we expect, would the theme still be
           satisfied?
     GOOD  "Dispatchers cannot tell which job is urgent without reading notes. Serves objective 1. Success
           looks like priority being right often enough that dispatchers stop overriding it."
           (a problem, an owner objective, and a success condition that does not name a feature)
     WEAK  "Reporting improvements." (a feature category; nobody can fail at it and nobody can judge it)
     TRAP  Relabelling your feature list as themes. If each theme maps one-to-one onto a feature you had
           already decided to build, nothing changed except the vocabulary. -->

{{themes}}

## Timeframes

<!-- WHAT  When each theme is expected to be worked on, at whatever precision is honest. Broad buckets are
           legitimate; so are quarters, if you mean them.
     WHY   This is the section where the format either keeps its integrity or loses it. Precision should
           decay with distance, because "the further away something is, the more uncertain it is." Note the
           genuine disagreement here: some named practitioners hold that a roadmap should carry no firm
           dates at all, while others argue dates are fine for internal planning and one widely used
           enterprise framework commits the nearest increment outright. Choose deliberately and say which
           you chose. Deep dive: product-roadmap_companion.md section 3 (themes format) and section 6.
     ASK   Is this precision honest, or borrowed from a planning tool? Would we bet on the furthest item?
           Does a reader know which of these are commitments and which are forecasts?
     GOOD  "Theme 1: in progress now. Theme 2: starts once theme 1's first cohort reports, expected this
           half. Themes 3 and 4: next half, unshaped, no order implied between them."
           (visibly coarser further out, and the dependency is what sets the sequence)
     WEAK  "Theme 1: Q1. Theme 2: Q2. Theme 3: Q3. Theme 4: Q4." (equal precision at every horizon, which
           claims knowledge nobody has)
     TRAP  Letting the timeframes column become the document. If readers only ever look at this section,
           you have written a timeline roadmap with extra prose above it. -->

{{timeframes}}

## What Is Not On Here

<!-- WHAT  Things asked for, considered, and deliberately excluded, with one line each on why. Two to five.
     WHY   THIS SECTION IS THIS BUNDLE'S ADDITION to the published five-part structure. The disclaimer
           below says the plan may change; it does not say what the plan refused. A roadmap that cannot be
           cited to decline a request settles no arguments, and the exclusions are what stop themes from
           quietly expanding to cover everything. Deep dive: product-roadmap_companion.md section 3 (What
           Is Not On Here) and section 7.
     ASK   What has been asked for repeatedly that no theme covers? Who will be unhappy, and have they been
           told? Is any theme so broad that it silently includes something we mean to refuse?
     GOOD  "Customer-facing arrival windows. Most requested item we have; depends on scheduling accuracy we
           do not yet have. Revisit when the override rate is under 20 percent. Sales knows."
     WEAK  "Anything not serving the objectives above." (refuses nothing anyone actually asked for)
     TRAP  Assuming the disclaimer covers this. "Subject to change" is about timing; this is about scope,
           and they are different promises. -->

{{what_is_not_on_here}}

## Disclaimer

<!-- WHAT  A plain statement of what this document is and is not, and what a reader may rely on. Two or
           three lines.
     WHY   It is part of the published structure, and it exists because a roadmap that travels gets read as
           a commitment. State its limit honestly too: a disclaimer does not undo the effect. Once a date
           has been read by a customer, they will hold you to it regardless of the wording underneath. Deep
           dive: product-roadmap_companion.md section 3 (themes format) and section 9.
     ASK   Who will read this, and what will they do with it? If someone planned a budget around the Later
           items, would this paragraph have stopped them? Is anything here a commitment, and is it marked?
     GOOD  "This roadmap states our current intent, not a delivery commitment. Items in progress are
           expected to ship; everything else may change or be dropped. Nothing here should be used in a
           customer contract. The two exceptions are marked COMMITTED and are tracked separately."
           (says what may be relied on, and marks the exceptions rather than pretending there are none)
     WEAK  "Subject to change without notice." (a legal reflex; tells a reader nothing about what to do)
     TRAP  Believing this section protects you. It sets expectations for readers who are paying attention.
           It does not undo a date that a customer has already seen, and it is not a substitute for
           deciding what to publish. -->

{{disclaimer}}
