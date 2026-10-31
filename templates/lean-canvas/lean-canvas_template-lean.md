---
title: "{{product_name}} Lean Canvas"
product: "{{product_name}}"
owner: "{{who_sketched_this_canvas}}"
status: "{{draft_or_tested}}"
last_updated: "{{date}}"
doc_type: lean-canvas
size: lean
source_template: lean-canvas
source_template_version: 0.1.0
---

<!--
LEAN CANVAS. This bundle ships one size, deliberately: Ash Maurya publishes one page and says
"Embrace a 1-page constraint", and no source this research read splits a short canvas from a long
one. See lean-canvas_guide.md, "Picking a variant," for the fuller argument; it is not repeated
here.

WHAT THIS DOCUMENT IS, AND IS NOT. A Lean Canvas states a product's business model on one page, as
beliefs to test, not as a finished plan. Ash Maurya built it as "an adaptation of Alexander
Osterwalder's Business Model Canvas - optimized for the Lean Startup methodology", keeping
Osterwalder's layout on purpose to credit the source. It is NOT a business plan: "While a business
plan can take weeks or months to write, your initial canvas should be sketched quickly." It is NOT
a finished forecast of Revenue Streams or Cost Structure; both boxes below ask for a near-term
milestone, not a multi-year model. It is NOT a product-strategy document: this canvas names no
decision about which problems to pursue, only the whole business model as a set of beliefs. It is
NOT the Business Model Canvas, the tool it adapts: that tool keeps Key Partnerships, Key Resources,
Key Activities and Customer Relationships, which this canvas replaces with Problem, Solution, Key
Metrics and Unfair Advantage. See lean-canvas_companion.md section 1 and section 8 for the fuller
set of boundaries, including this library's own argued boundaries with `product-strategy`,
`positioning-statement`, `north-star-metrics` and `lean-ux-canvas`, none of which any source read
states directly.

WHO FILLS THIS IN, AND HOW FAST. Sketch the first canvas alone, even on a team: "If you're part of
a team, avoid creating a Lean Canvas as a group exercise. Instead, have each team member create
their snapshot first." Then share it: "The important thing is sharing it with at least one other
person when you are done." A first sketch takes "less than 20 minutes", in "one sitting", on one
page, and it is normal to leave boxes blank: "it's okay to leave boxes blank". Maurya built the
canvas "for startups operating under conditions of extreme uncertainty", and his own company draws
the line at product-market fit, not company age: "If you are pre-product-market fit, start with
Lean Canvas". See lean-canvas_companion.md section 6 (Debates) and section 9 (Adaptations) before
using this for an established, proven line of business.

WHERE THIS SITS IN THE CHAIN. This library places the Lean Canvas second among its strategy-docs
family, between the product vision and the product strategy, and names that placement its own
POSITION rather than a sourced finding: no source compares the two sequences by name. A considered
alternative places the canvas after the strategy, as the strategy's business model kept current
beside the roadmap. Nothing in this template depends on which place is correct; it depends only on
the canvas stating beliefs a later product strategy can commit to or reject. See
lean-canvas_companion.md section 6 (Debates) and section 8 (Relationships).

THE CANVAS IS COPYRIGHTED. No open licence appears on Maurya's own pages. This template names the
boxes and quotes him briefly with attribution; it does not reproduce his visual grid layout.

A NAME COLLIDES INSIDE THIS LIBRARY. `product-vision_guide.md` uses the phrase "the lean canvas"
for that bundle's own short, one-page `canvas` format, an unrelated meaning of the same two words.
This document is Ash Maurya's Lean Canvas, described fully in lean-canvas_companion.md section 8.

HOW TO FILL THIS IN
1. Read the comment under each heading: WHAT it wants, WHY it matters (with a pointer into
   lean-canvas_companion.md for the deep reasoning), guiding questions to ASK, a GOOD and a WEAK
   example, and the TRAP to avoid. The last two sections also carry PRIORITY and ROW HINT for their
   table.
2. Replace each {{placeholder}} with your content. Maurya's own fill order starts from Customer
   Segments and Problem, together, and this template follows that order top to bottom; he also
   says "There is no right order for sketching a Lean Canvas", so treat the order as a default, not
   a rule.
3. If a section does not apply, write "N/A" and one line of why, rather than deleting it.
4. This is a snapshot of your current best guess, not a finished plan: "Like everything on the
   canvas, you start with the best guess and iterate from there." Before you first share it,
   self-grade against lean-canvas_guide.md, then DELETE every HTML comment. They are guidance, not
   content.
-->

# {{product_name}} Lean Canvas

## Customer Segments

<!-- WHAT  Who has the problem and who will pay for a solution to it, with a line for the Early
           Adopters, the specific subset you target first.
     WHY   Maurya's product page defines both directly: "Customer Segments - Who has the problem
           and who will pay" and "Early Adopters - The specific subset of customers you target
           first". His current teaching page draws the paying customer apart from a mere user: "A
           customer is someone who pays for your product. A user does not." Both his current
           teaching page and his 2011 walkthrough start the fill order from this box, and the
           walkthrough ties it to the next box directly: "The "Problem-Customer" pair usually
           drives the rest of the canvas which is why I tackle them together". Deep dive:
           lean-canvas_companion.md section 3 (Customer Segments).
     ASK   Who exactly has this problem, in concrete terms rather than a demographic label? Who
           will actually pay for a solution, as distinct from who will merely use it for free?
           Within that segment, who is the early adopter: the person who will adopt before anyone
           else does, not the eventual mainstream buyer?
     GOOD  "Busy home cooks who already use a grocery delivery app but still spend 20 minutes every
           evening deciding what to cook. Early Adopters: cooks who have already tried and
           abandoned at least one other meal-planning app in the past year."
           (names who pays, and narrows to a specific early adopter rather than the whole market)
     WEAK  "People who cook dinner." (no payer named, and no early adopter named apart from the
           mainstream market)
     TRAP  Writing the eventual mainstream buyer here instead of the early adopter. Maurya is
           direct about this: "Your objective is to define an early adopter, not a mainstream
           customer." -->

{{customer_segments}}

**Early Adopters.** The specific subset of customers you target first: {{early_adopters}}

## Problem

<!-- WHAT  The top one to three problems this segment has, with a line for Existing Alternatives:
           how these customers solve the problem today, without your product.
     WHY   "List the top one to three problems." Maurya's reasoning for keeping the box narrow is
           explicit: "Problems, not solutions, create spaces for innovation." The Existing
           Alternatives sub-block asks a separate question: "Document how you think your early
           adopters currently address these problems today." An alternative does not have to be a
           named competitor or even another product; doing nothing at all can be an alternative
           too. Deep dive: lean-canvas_companion.md section 3 (Problem).
     ASK   What are the top one to three problems this segment actually has, stated as problems,
           not as the solution you already want to build? How does this segment solve each problem
           today, including an alternative that is not a competing product at all?
     GOOD  "1. Deciding what to cook takes longer than actually cooking it. 2. The planned meal
           often does not match what is already in the fridge. 3. The grocery list gets written
           from a recipe, not from what is already on hand. Existing Alternatives: a paper list on
           the fridge door, a group text to whoever is cooking tonight, or skipping the plan
           entirely and ordering takeout."
           (names problems, not features, and gives a real existing alternative, including doing
           nothing)
     WEAK  "People need a better way to plan meals." (names the shape of a solution, not a problem,
           and names no existing alternative)
     TRAP  Naming a solution here instead of a problem. If the "problem" you wrote is already the
           answer you want to build, the rest of the canvas has nothing genuine left to test it
           against; this is the same solution-first trap the Solution box below is built to resist.
           Draft this box together with Customer Segments, not after it; the pairing is
           deliberate. -->

{{top_problems}}

**Existing Alternatives.** How customers solve these problems today: {{existing_alternatives}}

## Unique Value Proposition

<!-- WHAT  The single message that states why this product is different and worth attention, with
           a line for the High-Level Concept: an "X for Y" analogy that makes the idea instantly
           understandable.
     WHY   Maurya's product page defines the sub-block directly: "High-Level Concept - The X for Y
           analogy that makes your idea instantly understandable". His 2011 walkthrough places the
           Unique Value Proposition itself at the centre of the canvas and treats it as one of the
           hardest boxes to get right, though no line of his on that point survives as a direct
           quotation, so treat any stronger claim about this box with caution. Deep dive:
           lean-canvas_companion.md section 3 (Unique Value Proposition).
     ASK   Why is this product different from every existing alternative named above, in one clear
           message rather than a feature list? What single analogy would make a stranger
           understand the idea in one sentence?
     GOOD  "Hearth is the app that turns what is already in your fridge into tonight's dinner, in
           under a minute. High-Level Concept: a meal planner for people who already shop, not for
           people who want to shop differently."
           (one clear message, plus a concrete analogy a stranger could repeat back)
     WEAK  "Hearth helps you eat better." (no stated reason to pay attention, and no analogy)
     TRAP  Writing a feature list instead of one message. If this section needs more than a
           sentence or two, the message is not yet found; keep working it rather than padding the
           box with everything the product does. -->

{{unique_value_proposition}}

**High-Level Concept.** The X for Y analogy that makes the idea instantly understandable:
{{high_level_concept}}

## Solution

<!-- WHAT  The simplest thing that addresses each listed problem, in a box kept deliberately small.
     WHY   "I purposely made the solution box less than one-ninth of the entire canvas". The
           instruction to wait is stated in both eras of Maurya's writing: "Bind a solution to your
           problem as late as possible." Deep dive: lean-canvas_companion.md section 3 (Solution)
           and section 6 (Debates, the solution-first trap).
     ASK   What is the simplest version of a solution that addresses the problems above, not the
           most complete one? Have Customer Segments and Problem actually been settled first, or is
           this box being filled from a solution already decided on?
     GOOD  "Photograph the fridge shelf; the app matches it against three dinner options already
           in the house." (one simple mechanism, stated small)
     WEAK  A paragraph-long feature list covering onboarding, notifications, social sharing and a
           recipe marketplace, reading like a product specification rather than the simplest
           version of the idea.
     TRAP  Filling this box before Customer Segments and Problem are settled. Writing a solution
           early is the specific habit this companion calls the solution-first trap; a founder who
           finds this box too small to hold a full solution description is being told something
           about scope, not about formatting. -->

{{solution}}

## Channels

<!-- WHAT  The path to reach customers, now and at scale.
     WHY   This is the thinnest-sourced box in the research behind this bundle. Maurya's 2011 text
           advises selling manually before automating, and selling in person before letting others
           sell on the founder's behalf, though no line of his on this point survives as a direct
           quotation, so it is reported here as paraphrase. Where this box is thin on texture, lean
           on the current teaching page's box order rather than inventing detail the research did
           not find sourced. Deep dive: lean-canvas_companion.md section 3 (Channels).
     ASK   How will the early adopters named above actually be reached today, one at a time if
           necessary? What is the first channel that gets this in front of a real early adopter
           this week, not the channel that would work once the product is proven?
     GOOD  "Early adopters reached one at a time through a cooking forum and a manual waitlist; no
           paid channel yet." (a specific, near-term, founder-reachable path)
     WEAK  "Marketing." (names no actual path to a single customer)
     TRAP  Writing a full go-to-market plan here, or a channel strategy that assumes scale the
           product has not earned yet. No source read names a channel framework that extends this
           box; keep it a short, founder-written line. -->

{{channels}}

## Revenue Streams

<!-- WHAT  How the product makes money, priced now rather than modeled years out.
     WHY   "Rather than thinking in terms of three- or five-year forecasts, it's better to take a
           more stage-based approach. Focus on your most immediate short-term milestones three to
           six months from now." Maurya's 2011 walkthrough is direct about timing: "Second, I
           believe pricing is one of the riskiest (and most critical) parts of the business model
           and should be tested early." Deep dive: lean-canvas_companion.md section 3 (Revenue
           Streams).
     ASK   What is the near-term price, and the near-term milestone it is tested against, three to
           six months out? Has this price actually been tested with a real early adopter, or is it
           a guess that has not yet been put in front of anyone?
     GOOD  "$9 a month, tested against the first 20 waitlist signups; next milestone is 10 paying
           households within three months." (a near-term price, tied to a near-term, testable
           milestone)
     WEAK  "A freemium model, pricing to be decided later, with a five-year revenue projection
           attached." (no near-term price, and the exact multi-year forecast this box is built
           against)
     TRAP  Writing a multi-year revenue model instead of a near-term price and milestone. This box
           shares its sourcing with Cost Structure below; the same stage-based instruction governs
           both. -->

{{revenue_streams}}

## Cost Structure

<!-- WHAT  What it costs to reach the next milestone, three to six months out, not a multi-year
           budget.
     WHY   The same stage-based instruction that governs Revenue Streams governs this box: "Focus
           on your most immediate short-term milestones three to six months from now." Like
           Channels, this box has thin sourcing beyond that one shared instruction; do not over-read
           structure into it that the source material does not carry. Deep dive:
           lean-canvas_companion.md section 3 (Cost Structure).
     ASK   What does it actually cost, in money and in time, to reach the milestone named in
           Revenue Streams above? Is this a near-term figure, or has it quietly become a budget for
           a team and a timeline the product has not earned yet?
     GOOD  "Fridge-matching API calls and two part-time cooks reviewing suggested meals, enough to
           reach 10 paying households by month three." (a near-term cost, tied to the same
           milestone as Revenue Streams)
     WEAK  "A three-year operating budget with headcount for a 12-person team." (the exact
           multi-year budget this box is built against)
     TRAP  Pairing this box with a revenue model that has already drifted into a multi-year
           forecast. Draft Revenue Streams and Cost Structure together against the same near-term
           milestone, not against separate timelines. -->

{{cost_structure}}

## Key Metrics

<!-- WHAT  Three to five outcome metrics that show the business model is working.
     WHY   "List 3-5 key metrics", and the current teaching states a clear preference: "Prefer
           outcome metrics versus output metrics." This box has changed name and content over time:
           the first published canvas headed it "Key Activity" and asked about a single key action
           rather than a set of outcome metrics. Fill it to the current instruction, not to that
           earlier wording. Deep dive: lean-canvas_companion.md section 2 (Origins and evolution)
           and section 3 (Key Metrics).
     ASK   What three to five metrics would show, in outcomes rather than mere activity, that this
           business model is actually working? Does each metric measure a result for the customer
           or the business, rather than counting an output the team merely produced?
     GOOD  "Weekly active meal plans created; percent of planned meals actually cooked; week-four
           retention." (outcomes a customer or the business actually experiences)
     WEAK  "Number of recipes in the database." (an output the team produced, not an outcome that
           shows the model is working)
     TRAP  Treating this box as a single key activity, the way the first published version of this
           canvas asked for. The current instruction is three to five outcome metrics, not one
           activity count. -->

{{key_metrics}}

## Unfair Advantage

<!-- WHAT  Something about the business that cannot be easily copied or bought.
     WHY   "A real unfair advantage is something that cannot be easily copied or bought" (Jason Cohen,
           as Maurya quotes him). The box's
           purpose is forward-looking rather than a pass or fail test: it exists "to continually
           encourage you to work towards finding/building your unfair advantage". It is normal to
           leave this box blank at first: "Leave the unfair advantage blank." Deep dive:
           lean-canvas_companion.md section 3 (Unfair Advantage).
     ASK   Is there anything about this business, right now, that a well-funded competitor could
           not simply copy or buy? If nothing honestly qualifies yet, what would have to become
           true before something did?
     GOOD  "Left blank for now; nothing yet stops a larger app from copying the fridge-photo
           matching feature." (honest, and names what would need to change)
     WEAK  "We work harder than anyone else." (not something that cannot be copied or bought, and
           not an honest blank either)
     TRAP  Filling this box with a claim that is really just effort, enthusiasm, or a feature a
           competitor could ship next quarter. A true unfair advantage survives being named out
           loud to a competitor; most early businesses have not found one yet, and leaving the box
           blank says so honestly. -->

{{unfair_advantage}}

## Riskiest Beliefs and Next Tests

<!-- WHAT  A record of which beliefs on this canvas are weakest, what evidence, if any, currently
           backs them, and what test comes next. This section is this library's own addition to
           the nine boxes Maurya publishes: no source read publishes a canvas template with a
           tenth section of this kind. POSITION.
     WHY   What this section records is sourced directly to Maurya's own teaching, layered on top
           of the nine boxes rather than inside them: "focus on your weakest links first - your
           riskiest assumptions", checking first whether "If your customer and problem assumptions
           are not yet grounded in empirical learning, it’s prudent first to get them in order."
           His product page frames the whole canvas around this discipline: "identifying and
           testing your riskiest assumptions before you build", and his company's own comparison
           page states it even more bluntly: "Find the riskiest assumption, test it". The prompt
           for what comes next is his own question: "what are the next hypotheses you need to test
           to move your product forward?" Deep dive: lean-canvas_companion.md section 3 (Riskiest
           Beliefs and Next Tests).
     ASK   Of every belief written into the nine boxes above, which one would do the most damage if
           it turned out false? What evidence, if any, already backs that belief, as opposed to
           hope or enthusiasm? What is the next concrete test that would confirm or refute it?
     PRIORITY  Name customer and problem beliefs first; Maurya's own advice is to get those grounded
           in empirical learning before trusting the rest of the model. A canvas with every belief
           marked "untested" is honest; a canvas that marks everything "validated" on day one is
           not.
     ROW HINT  A good row names a belief from one specific box above, states plainly what evidence,
           if any, currently backs it, and names a next test that could actually refute it. A weak
           row names a belief nobody could prove wrong, or claims evidence that is really just
           enthusiasm from the people who already want to build this.
     GOOD  | Problem | "The grocery list gets written from a recipe, not from what's in the house" |
           20 waitlist signups said yes when asked; no usage data yet | Watch five households use a
           paper version of the matching for one week |
     WEAK  | Problem | "People will love this" | Everyone we've talked to is excited | None named |
           (not falsifiable, the evidence is enthusiasm, and no next test is named)
     TRAP  Marking a belief "validated" on the strength of excitement rather than a real test, or
           leaving the Next Test column blank for the riskiest row on the canvas. -->

| Box | Belief | Evidence So Far | Next Test |
|---|---|---|---|
| {{belief_box}} | {{belief}} | {{evidence_so_far}} | {{next_test}} |

## Versions

<!-- WHAT  A dated row per revision: what changed on the canvas and why. This section is this
           library's own addition, chosen to match the `utility` classification this family
           contract gives the canvas: a standing instrument that earns its value by being kept
           current, not a document finished once. POSITION.
     WHY   The practice it records is sourced: the canvas is "an organic document that evolves over
           time", built for "tracking ongoing learning", and Maurya's own software tool now
           automates exactly this: "Your canvas is versioned automatically. You can view past
           versions and restore any previous state." Deep dive: lean-canvas_companion.md section 3
           (Versions).
     ASK   What changed since the last recorded revision, and which box did it change? Did the
           change follow a test result named in Riskiest Beliefs and Next Tests above, or did it
           happen without one?
     PRIORITY  List the most recent revision first, so a reader can see immediately whether this
           canvas has actually been kept current or has sat untouched since its first sketch.
     ROW HINT  A good row names which box changed, ties the change to a belief that resolved,
           confirmed or refuted, and says so in one line. A weak row records that "the canvas was
           updated" without naming what changed or why.
     GOOD  | 2026-03-01 | Narrowed Customer Segments to home cooks who already use a grocery
           delivery app | The first five interviews showed the mainstream buyer was not who
           actually signed up |
     WEAK  | 2026-03-01 | Updated the canvas | Things changed |
           (names no box, no belief, and no reason)
     TRAP  Sketching the canvas once and never adding a row after. A canvas with no Versions
           entries after its first sketch is a sign this discipline has lapsed, not a sign the
           model is settled. -->

| Date | What Changed | Why |
|---|---|---|
| {{version_date}} | {{what_changed}} | {{why_changed}} |
