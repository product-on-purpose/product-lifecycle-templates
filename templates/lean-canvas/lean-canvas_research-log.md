# lean-canvas: research log

Research conducted 2026-10-30. The research stage stored its pages from 02:19 UTC on 2026-10-31, which is
2026-10-30 by local time. The research builds on the 2026-10-11 Define sweep and the 2026-10-20 re-score, whose
digests sit in gitignored folders under `_local/research/`, and on the placement research of 2026-10-30, which
raw-checked the admission quotations on Maurya's own pages. It builds on
[ADR 0083](../../docs/internal/decisions/0083-lean-canvas-joins-strategy-docs-as-a-seventh-member.md) (the Lean
Canvas joins strategy-docs as a seventh member), on the family contract (`docs/internal/contracts/strategy-docs.md`,
0.4.0) and on the approved spec, the section of `docs/internal/tier2-specs.md` headed "strategy-docs (seventh
member, by amendment): the Lean Canvas". The maintainer ruled all seven of that spec's choices as recommended on
2026-10-30. They fix the classification `utility`, second place in the chain between `product-vision` and
`product-strategy`, one size, eleven sections (the nine boxes, then Riskiest Beliefs and Next Tests, then
Versions, the last two labelled the library's POSITION), the embedded-analytics OEM example, and `pairs_with:
[foundation-lean-canvas]`. This bundle is issue #337 (bundle: lean-canvas), and it fills catalog entry 5.

The build ran six dimensions: origins, structure, practice, debates, relationships and the gap question. The
working files are numbered by return order, not by dimension: `dim1.md` holds structure, `dim2.md`
relationships, `dim3.md` debates, `dim4.md` origins, `dim5.md` practice and `dim6.md` the gap question.

**15 sources are recorded below, and all 15 are fetched-and-verified.** By tier they are 10 primary, 3
practitioner and 2 vendor. Eleven entries are Maurya's own or his company's: the 2010 post [1], his pages and
company pages [2] to [8], the 2024 Leaner Lean Canvas post [11], the comparison page [13] and the 2011 walkthrough
[15]. Two of those, [8] and [13], are product and comparison pages and carry the vendor tier. The tenth primary
entry is Roman Pichler's own article on his Product Vision Board [12]. The practitioner entries are one
accelerator's workshop page [9], a trade-press interview [10] and a master's thesis [14]. Entry [15] is a
copyrighted 40-page PDF read from a text copy that the maintainer supplied from their own file; its text is never
committed, and it carries no URL for that reason. **107 Quotable lines remain: 83 from the 14 web entries and 24
from the PDF.** Quotable lines render long dashes as hyphens and keep curly apostrophes; copy them as they stand.

## What the checks caught, and what was not read

**Every quotation was checked against raw text**, never against a retrieval tool's summary. The cached copy of
Maurya's comparison post [2] turned out to be a retrieval tool's summary, not the page, so four of its quotations
failed against it. The main loop replaced the cached copy with the raw page, and all four then passed.

**Two quotations were dropped because they are not on their pages.** One was a post title, *How I Document My
Business Model Hypotheses*, attributed to [2] as Maurya's name for his 2010 post. The other was a line attributed
to the Twente thesis [14], a comparison-table cell saying the Lean Canvas does not treat financial aspects. Two
findings change as a result. The origins return reported that the 2010 post's title is inconsistent across
Maurya's own pages; that contest rested on the missing quotation, so this log withdraws it rather than reporting
it. The gap return's financial-depth candidate loses its quotation and is routed below at low confidence.

**Four sites bear on this research under the terms rule.** Strategyzer's terms bar access to its services by any
means other than its interface (Section 19), and separately bar bypassing robot-exclusion headers. Tability's
acceptable-use policy bars spiders, robots and crawlers. The main loop added both to the runbook's table on
2026-10-30. The Wade Institute studio's terms bar using automated tools to access the studio at scale without
prior written permission. The practice return had read one page there, which is not at scale, but the main loop
withdrew that entry conservatively, and no claim here rests on it. Atlassian is treated as barred, as admission
sweep 7 reported on 2026-10-29.

**Three agents fetched a page before checking its site's terms.** Across the practice, debates and gap returns,
pages on tability.io and miro.com were read first, and so was a post in Maurya's newsletter at
newsletter.leanstack.com, which is hosted on Substack. The newsletter's cache entry was deleted. No claim and no
quotation in this log rests on any of those pages.

**One consequence matters for the relationships finding.** Strategyzer's own view of the Lean Canvas against the
Business Model Canvas is unread. The comparison below rests on Maurya's side alone.

**What could not be found.** No source read states a calendar interval for revising a canvas. No source read
compares the Lean Canvas by name with a business case, a product strategy, a positioning statement, a North Star
metric or the Lean UX Canvas. No named critic was read arguing that the four dropped Business Model Canvas boxes
are a defect. No source read names market sizing as a missing box, or names a missing change-log field as a
complaint about the static template. No source read says who fills the canvas on an established software team.
The first edition date of *Running Lean* was not confirmed from a primary page, and no page announces the move of
Maurya's material from leanstack.com to leanspark.ai.

## Findings

### 1. Origins: a 2010 blog post, an adaptation of Osterwalder, and several websites

Ash Maurya published the canvas on 2010-08-12 in a post on his own blog, titled "How I Document My Business
Model On 1 Page" [1]. He worked from Steve Blank's customer-development worksheets, then met Osterwalder's
Business Model Canvas and found it lacking for his purpose: "I do find some of Osterwalder's blocks a bit too
general for a lean startup" [1]. After meeting Rob Fitzpatrick's adaptation, he wrote, "So I decided to iterate
on this one more level" [1]. His 2011 walkthrough tells the same lineage: he "found some of his canvas elements
too general" and made "an adaptation that eventually became the Lean Canvas" [15]. Confidence: high.

He tested it in public before it was software: "Lean Canvas was tested and refined in these presentations and
workshops before it ever became an online tool" [15]. The walkthrough names one of those presentations, at
Capital Factory's Demo Day in Austin, to a mostly investor audience [15]. His current pages state the
authorship plainly: "Lean Canvas was created by me, Ash Maurya, and is an adaptation of Alexander Osterwalder's
Business Model Canvas - optimized for the Lean Startup methodology." [6], and "Lean Canvas is a 1-page business
model template created by Ash Maurya in 2010." [7].

**He kept Osterwalder's layout on purpose.** "I chose to work within the existing layout constraints to
attribute the work back to Alex Osterwalder's original canvas" [2]. His retrospective gives the reasons for the
boxes he changed. He judged two of the removed boxes more outside-in than founder-focused [2]. Of customer
relationships he wrote, "This seemed better captured by the existing Channels box." [2]. Of key partners, he
wrote that for an unknown startup "pursuing key partnerships from day one can be a form of waste" [2]. The frame
behind all of it is Eric Ries's: "Startups operate under conditions of extreme uncertainty." [2]. The same
retrospective dates his exposure to Osterwalder's book to May 2010 and to Fitzpatrick's variant to June 2010, and
the start of the online tool to September 2010 [2]. Confidence: high on the reasons. The month-level timeline is
low confidence: no Quotable line carries the months, and the entry's summary of them may date from the cached
retrieval summary that the main loop replaced.

**The four-box swap describes the canvas as it later stood, not as first published.** His current pages say he
replaced key partnerships, key resources, key activities and customer relationships with problem, solution, key
metrics and unfair advantage [2], [6], [7]. The 2010 post's fifth box was still headed Key Activity: "5. Key
Activity: Describe the key action users take that maps to revenue or retention?" [1]. So the first version
removed three Osterwalder boxes, added three, and repurposed the fourth. The 2011 walkthrough already heads that
box Key Metrics, but it still asks the reader to document the one or two key activities that will drive usage,
and defers Dave McClure's pirate metrics to later [15]; this was read in the maintainer's text copy and is not a
Quotable line, so it is paraphrased. The 2024 page asks for three to five outcome metrics [6]. Confidence: high.

**Maurya's material now sits on several sites.** "LEANSTACK is the company behind LEANSpark." [4]. The Lean Canvas
teaching pages, the product guide and the comparison page live on leanspark.ai [6], [7], [8], [13]. His blog
archive, the 2010 post among it, lives on ashmaurya.com, which also lists "Running Lean 3rd edition · 2022" and
says the book "Started as posts on this blog" [1], [3]. His company bio on LeanFoundry calls him "Creator of Lean
Canvas" [5]. The 2024 Leaner Lean Canvas post was read at a leanspark.leanstack.com address [11]. No page
announces the move between these sites, so it is inferred from where the pages now are. Confidence: medium.

### 2. Structure: nine boxes, three sub-blocks, and a fill order

**Twelve blocks, of which three sit inside other boxes.** Maurya's product page lists the nine boxes and three
sub-blocks [7]: "Customer Segments - Who has the problem and who will pay", "Early Adopters - The specific subset
of customers you target first", "Existing Alternatives - How customers solve these problems today" and
"High-Level Concept - The X for Y analogy that makes your idea instantly understandable" [7]. The teaching page
treats each sub-block inside its parent box [6]. Confidence: high.

**The order is customer-first, and Maurya says no order is required.** The 2024 page says "There is no right
order for sketching a Lean Canvas" [6], and then teaches the boxes from customer segments through problem, unique
value proposition, solution, channels, revenue streams, cost structure and key metrics to unfair advantage [6].
The 2011 walkthrough is firmer: "I start with the Customer Segment and follow a prescribed order to filling out a
canvas" [15]. It drafts customer and problem together, because that pair usually drives the rest of the canvas
[15]. Both leave the unfair advantage until last; the walkthrough calls it the hardest section to fill [15].
Confidence: high.

**The rules for a first sketch.** It is fast: "your initial big idea canvas should be sketched quickly - in less
than 20 minutes" [6], with the instruction "Set a timer for 20 minutes" [6]. It is short: "Embrace a 1-page
constraint" [6], since "Describing your idea on a single page is not about using smaller fonts but fewer words."
[6]. The 2011 text says "Sketch a canvas in one sitting" and "The boxes on the Lean Canvas are intentionally small
because it forces you to be concise." [15]. Blanks are allowed: "it's okay to leave boxes blank" [6], and "It's
okay to leave sections blank" [15]. A team should not draft it together: "If you're part of a team, avoid
creating a Lean Canvas as a group exercise. Instead, have each team member create their snapshot first." [6].
The finished sketch is shared: "The important thing is sharing it with at least one other person when you are
done." [15]. Confidence: high.

**One canvas per customer segment, in 2011.** The walkthrough says "Sketch a Lean Canvas for each customer
segment" and "I recommend starting with the top 2-3 customer segments you feel you understand the best or find
most promising." [15]. It then compares them: "Once you have your Lean Canvases sketched for each customer
segment, lay them side by side and select the best business model to start with." [15]. "Here is the weighting
order I use (ranked from highest to lowest)" [15], and the order it gives is customer pain level, ease of reach,
price and market size [15]. The 2024 page does not repeat the per-segment rule in its numbered guidelines [6].
Confidence: high for 2011, medium for whether the rule is still foregrounded.

**What each box asks, in Maurya's words.**

- **Customer Segments.** "A customer is someone who pays for your product. A user does not." [6]. "Your
  objective is to define an early adopter, not a mainstream customer." [6].
- **Problem.** "List the top one to three problems." [6], because "Problems, not solutions, create spaces for
  innovation." [6]. For Existing Alternatives: "Document how you think your early adopters currently address
  these problems today." [6]. The 2011 text adds that an alternative may not be an obvious competitor, that email
  is the biggest alternative to many collaboration tools, and that doing nothing can be one [15].
- **Unique Value Proposition.** The walkthrough places it dead centre, calls it one of the most important boxes
  and the hardest to get right, and defines it as a single clear message stating why the product is different
  and worth buying [15]. No Quotable line carries it, so it is paraphrased. The High-Level Concept is an X-for-Y
  analogy [7]; in 2011 Maurya jots several as an adjunct exercise rather than a canvas entry [15].
- **Solution.** "I purposely made the solution box less than one-ninth of the entire canvas" [6]. "Bind a
  solution to your problem as late as possible." [6], [15].
- **Channels.** The 2011 text advises selling manually before automating, and selling yourself before letting
  others do it [15]. Neither line is Quotable, so both are paraphrased.
- **Revenue Streams and Cost Structure.** "Rather than thinking in terms of three- or five-year forecasts, it's
  better to take a more stage-based approach. Focus on your most immediate short-term milestones three to six
  months from now." [6]. On price: "Second, I believe pricing is one of the riskiest (and most critical) parts of
  the business model and should be tested early." [15]. The 2011 case study works a back-of-the-envelope
  break-even from a cost to launch [15].
- **Key Metrics.** "List 3-5 key metrics" [6], and "Prefer outcome metrics versus output metrics." [6].
- **Unfair Advantage.** "A real unfair advantage is something that cannot be easily copied or bought." [6],
  [15]; the definition is Jason Cohen's, and both pages quote it under his name [6], [15]. When none exists: "Leave the unfair advantage
  blank." [6]. The box exists "to continually encourage you to work towards finding/building your unfair
  advantage" [2].

**The finished first canvas is Plan A.** "Documenting your Plan A is a prerequisite for moving on." [15].

### 3. Practice: who fills it, how it changes, and how often

**A founder writes it down so the beliefs can be tested.** "Too many founders carry their hypotheses in their
heads alone which makes it hard to systematically build and test a business." [15]. "You have to draw a line in
the sand." [15]. The 2011 text warns that "A lot of entrepreneurs skip this step altogether which is NOT the
solution." [15]. On a team, each member sketches a snapshot first [6], and the result is shared with at least one
other person [15]. Confidence: high for founders. No source read says who fills it on an established software
team.

**It is kept current, not finished.** "The canvas is meant to be an organic document that evolves over time"
[15], a format for "tracking ongoing learning" [15]. "Like everything on the canvas, you start with a best guess
and then iterate from there." [15]. Maurya's own tool keeps history: "Your canvas is versioned automatically."
[8]. It also holds variants for "different pivot directions or market segments you're exploring" [8]. Confidence:
high that the originator treats the canvas as revised; [8] documents a software feature, not founder behaviour.

**Revisions follow learning, not the calendar.** No source read states a calendar interval for revising a canvas
as such. Maurya ties change to tests: price is tested early [15], and the solution is bound as late as possible
[6], [15]. The one calendar interval found is a programme rule. Tufts' accelerator states "The Lean Canvas will
be a weekly deliverable for the Full Time cohort as part of our weekly accountability framework." [9], and uses
it "to check your progress and identify issues to address" [9]. That is one cohort's accountability policy, not a
cadence for the canvas. Confidence: medium-high on the absence, within the sources read.

### 4. Debates

**Startup or established company.** Maurya built the canvas for uncertainty, and his pages draw the line by
stage, not by company age. His product page says it adapts Osterwalder's canvas "for startups operating under
conditions of extreme uncertainty" [7]. His company's comparison page says "Lean Canvas was designed for
entrepreneurs, not consultants, customers, advisors, or investors" [13], calls the Business Model Canvas "the
better tool for mapping and communicating established business models" [13], and advises "If you are
pre-product-market fit, start with Lean Canvas" [13]. It also says "Use what is most natural for you" [13]. The
debates return reported a practitioner split over intrapreneurship from search summaries only; nothing behind it
was read, so this log does not report it. Confidence: medium that the sourced test is product-market fit; low on
any wider debate.

**Canvas or business plan.** Maurya's walkthrough contrasts the time each takes: "While a business plan can take
weeks or months to write, your initial canvas should be sketched quickly." [15]. The 2010 post carries a pair of
definitions that sets them apart: "Business Plan: A document investors make you write that they don't read." [1].
This log does not establish whether that line is Maurya's own or one he quotes, so the companion should present
it as the post's, not as his coinage. No source read argues the other side. Confidence: high on Maurya's view.

**The solution-first trap.** The canvas is designed against it: the solution box is deliberately less than a
ninth of the page [6], a solution is bound as late as possible [6], [15], and problems come before solutions [6].
A trade-press interview reports Maurya naming the habit innovator's bias, a love for the solution that he says
includes himself, and prescribing a shift from the product being built to the business model being built [10].
That page is not Maurya's own, so it is paraphrased. The phrase solution-first trap is the spec's, not his.
Confidence: medium.

**The dropped boxes.** Maurya presents every removal as deliberate [2], [6], [7]. No named critic arguing the
opposite was read. Pichler's article says his own board "does not capture the business model including the
competitors, the partners, the channels" [12], but that is a remark about his board, not a critique of the Lean
Canvas.

**The Leaner Canvas question is resolved.** The spec's risk note recorded that some pages describe a Leaner
Canvas that the 2026-10-11 sweep could not confirm. Maurya's own post of 2024-09-07, *Reorder your Chain of
Beliefs with a Leaner Lean Canvas*, answers it [11]. A full canvas, he writes, is "a great exercise for baselining
an idea", but "at the earliest stages, however, it helps to more narrowly focus attention on just the two outer
boxes of the canvas" [11], which are customer segment and problem. His reason: "If your customer and problem
assumptions are not yet grounded in empirical learning, it’s prudent first to get them in order." [11]. So the
Leaner Canvas is Maurya's own narrowing exercise on the same canvas, not a separate canvas and not a
misattribution. The debates return searched ashmaurya.com [3] and leanspark.ai and did not find this post, and
called the question unresolved; the gap return found and read it. Confidence: high.

### 5. Relationships

**The Business Model Canvas, from Maurya's side only.** The Lean Canvas is an adaptation of it [6], [7], keeps its
layout [2] and replaces four of its boxes [2], [6], [7]. His company's page assigns the two canvases to stages:
the Lean Canvas before product-market fit, the Business Model Canvas for "mapping and communicating established
business models" [13]. Strategyzer's pages are barred under the terms rule, so Osterwalder's side of the
comparison is unread. Confidence: high that this is Maurya's position; no claim about Osterwalder's.

**The Product Vision Board.** Pichler names the Lean Canvas among other tools: "There are, of course, other
helpful tools available... including Ash Maurya's Lean Canvas" [12]. He writes that "The product vision board
is the simplest thing that could possibly work to capture the vision and strategy of a product" [12] and says it
"does not detail how the business goals are achieved" [12]. For business-model detail he suggests teams
"complement the product vision board with the business model canvas" [12]. So he puts business-model work after
vision work. His board covers vision and strategy together, so this weakly supports the spec's second place after
`product-vision`, and says nothing about the order of the canvas and `product-strategy`. Confidence: medium-low.

**The Customer Factory.** Maurya's bio lists him as "Customer Factory Framework creator" as well as the canvas's
creator [5]. That is a separate framework of his, not a part of the canvas. The bio line is two words, so the
companion should say no more than that. Confidence: medium.

**The Lean UX Canvas, the business case, the product strategy, the positioning statement and the North Star.** No
source read here compares the Lean Canvas with any of them by name, and no Gothelf page comparing his canvas with
Maurya's was found. The `lean-ux-canvas` bundle's research log records one vendor's line between the two canvases.
Every boundary in the spec's table is the library's own, and the companion should say so.

### 6. The gap question: candidates, routed under decision procedure 12

The gap dimension read the spec's ADR record but drew its findings from Maurya's pages and one thesis. Each
candidate below is routed as decision procedure 12 requires. None adds a section by itself, and two are absorbed
by the sections the spec already labels the library's POSITION.

1. **Which belief is riskiest, and what evidence backs it.** Maurya teaches readers to "focus on your weakest
   links first - your riskiest assumptions" [11] and to ground customer and problem beliefs in learning before
   trusting the rest [11]. His product page frames the canvas as "identifying and testing your riskiest
   assumptions before you build" [7], and his comparison page as "Find the riskiest assumption, test it" [13]. He
   teaches this as a practice on top of the nine boxes, not as a box [11]. **Routing: absorbed by section 10,
   Riskiest Beliefs and Next Tests.** The section stays the library's POSITION under clause E2, because no source
   read publishes a canvas with that section; the sources now support the practice it records. A rubric row can test
   that it names beliefs from this canvas and says which are grounded in evidence. Confidence: high on the
   practice, POSITION on the section.
2. **A dated record of what was learned.** The canvas is an organic document for tracking ongoing learning [15],
   and Maurya's tool versions it automatically [8]. **Routing: absorbed by section 11, Versions**, which stays
   the library's POSITION from the `utility` class. No source names a missing change-log field as a complaint
   about the static template. Confidence: medium.
3. **The customer funnel over time.** Maurya built the Customer Factory as a separate framework [5], which
   suggests the canvas does not track a funnel. **Routing: a guidance line or companion note only.** Confidence:
   low; the evidence is a two-word bio credit.
4. **Financial depth.** The thesis's table cell on financial aspects was not on its page and was dropped. What
   remains is the thesis's finding about the ancestor canvas: "a theoretical limitation of the Business Model
   Canvas is the lack of incorporating strategy" [14]. **Routing: a boundary note pointing a financial model to
   `business-case` and a strategy to `product-strategy`**, which the spec's What stays out paragraph already
   makes. Confidence: low as a gap claim about the Lean Canvas itself.
5. **One canvas per segment.** The 2011 rule [15] and the tool's variants [8] both treat a second segment as a
   second canvas. **Routing: guidance and a rubric row** that the canvas names one segment.
6. **Null results.** No source read names market sizing as a missing box, although market size is the last of
   the 2011 weighting criteria for choosing a segment [15]. No source read names an owner field, a decision date
   or a confidence scale for the canvas. Nothing was found that the bundle should add as a section of its own.

## Claims flagged contested or time-bound

- **The fourth box is time-bound.** The 2010 post headed it Key Activity [1]; the 2011 walkthrough headed it Key
  Metrics but asked for key activities [15]; the 2024 page asks for three to five outcome metrics [6]. The
  four-box swap as told on [2], [6] and [7] describes the canvas as it later stood.
- **The retrospective's dates sit awkwardly.** It says Maurya created his first Business Model Canvases "back in
  August 2009" [2], while its timeline, as the entry summarises it, dates his exposure to Osterwalder's book to
  May 2010 [2]. It says *Running Lean* was
  "first self-published as an ebook in February 2010" [2], six months before the canvas it features was published
  [1]. The O'Reilly page was not fetched. Confidence: low; the companion should not state the first edition date.
- **The title contest is withdrawn.** It rested on a quotation that is not on [2]. The 2010 post's title is the
  one on the post itself [1].
- **Fill order.** No right order [6] against a prescribed order [15]. These do not contradict: the 2024 page
  still teaches the boxes customer-first.
- **Which rule is foregrounded.** One canvas per segment leads the 2011 method [15]; the 2024 guidelines lead with
  sketching alone before reconciling [6].
- **The High-Level Concept** is a named block in 2024 [7] and an adjunct exercise in 2011 [15].
- **Cadence.** The weekly interval at Tufts is one programme's policy [9], not a property of the canvas.
- **Startup or established company.** The sourced test is product-market fit [13], not company age.
- **The Leaner Canvas** is resolved as Maurya's own narrowing exercise [11].
- **The sites are time-bound.** The canvas material sits on leanspark.ai and the blog on ashmaurya.com today [3],
  [4], [6]; the URLs have moved before and may move again.

## Honest framing

This bundle states a product's business model on one page, in Maurya's nine boxes, as beliefs to test. It is
honest about five things.

- **The canvas is a hypothesis sheet, not a plan.** Maurya contrasts it with a business plan [15], and
  expects it to change as tests return [15]. The companion must not present a filled canvas as a forecast.
- **Three of the bundle's calls are argued, not sourced.** The `utility` class, second place in the chain and the
  duplication answer in ADR 0083 are the library's reasoning. Pichler's sequence weakly supports the chain
  position [12]; nothing settles it.
- **Sections 10 and 11 are the library's POSITION.** The practices they record are Maurya's [7], [8], [11], [15];
  the sections are not.
- **It was built for startups.** Maurya built it for extreme uncertainty and draws the line at product-market fit
  [7], [13]. The example's new line of business inside an established company fits that test, and no source read
  argues against using it there; no source read endorses it either.
- **The canvas is copyrighted, and no open licence was found on Maurya's own pages.** The bundle names the boxes,
  quotes briefly with attribution, and writes every guidance comment in its own words.

## Notes for the companion

**Facts the companion must carry.**

- The canvas dates to Maurya's post of 2010-08-12 [1], adapted from Osterwalder's canvas [6], [7], keeping its
  layout to credit it [2].
- Nine boxes and three sub-blocks, twelve blocks in all [7]. The template follows the 2024 teaching order [6];
  the 2011 walkthrough's customer-first order agrees [15].
- The first sketch takes under 20 minutes on one page [6], one sitting [15], blanks allowed [6], [15], drafted
  alone before a team reconciles [6], and shared with at least one other person [15].
- The fourth box changed from Key Activity to Key Metrics [1], [15], [6]. Teach the 2024 rule, three to five
  outcome metrics [6], and say the box was renamed.
- The canvas is revised as beliefs are tested [15], and Maurya's own tool versions it [8].

**Hazards.**

- **The name collides inside the library.** `templates/product-vision/product-vision_guide.md` line 69 says the
  lean canvas for that bundle's lean-size `canvas` format. The companion should name the collision once and
  distinguish the two.
- **Misattribution is this type's named hazard.** Quote Maurya only from [1] to [8], [11], [13] and [15]. Entry
  [10] is a trade-press page, so its innovator's bias material is reported speech, never a direct quotation.
- **The spec's Maurya phrases are now Quotable.** The main loop checked the phrases the spec quotes against the
  cached raw pages and added them to [6], [7] and [8]: the deconstruct line, Typical SaaS metrics, the twelve-blocks
  heading and its three sub-block glosses, the simplest-thing line, the next-hypotheses hook, the snapshot line,
  the best-guess line, the 1-page constraint, the 20-minute rule and the automatic versioning line. The best-guess
  line in [15] reads differently from [6]'s; quote each from its own entry. Section 10's Maurya hook can come from
  [6]'s next-hypotheses line.
- **The two outside-in boxes are unnamed.** Maurya's retrospective calls two of the removed boxes outside-in [2],
  but no Quotable line names which two. The companion must not guess.
- **No invented cadence.** No source read gives a calendar interval for the canvas. The Tufts weekly deliverable
  [9] is an accelerator's programme rule and must not become a recommended rhythm.
- **Startup against established company.** Maurya built the canvas "for startups operating under conditions of
  extreme uncertainty" [7], and his company's page draws the line at "If you are pre-product-market fit, start
  with Lean Canvas" [13]. The embedded-analytics OEM line is a new business inside Acme, with different customers
  and an unproven model, so it sits on the uncertain side of that line. That is why it is the honest fit. The
  companion should say the sources address startups, that the example applies their own test, and that no source
  read speaks to a new line inside an established company directly.
- **The Leaner Canvas** is Maurya's own narrowing to the two outer boxes [11]. Present it as an early-stage
  focusing exercise, not as a variant canvas.
- **Example reuse.** Grep the template for `OEM`, `embedded` and `software vendor` before review.

**Sourcing by box, thinnest first.** Channels rests on two paraphrased 2011 lines [15] and the box order [6].
Cost Structure rests on one 2024 line [6] and a 2011 worked example [15]. Revenue Streams rests on the same 2024
line [6] and the 2011 pricing line [15]. The High-Level Concept rests on one definition [7]. Key Metrics is well
sourced for 2024 [6] but changed over time [1], [15]. The Unique Value Proposition is sourced only in paraphrase
[15]. The richest boxes are Customer Segments, Problem, Solution and Unfair Advantage [6], [7], [15].

## Sources

### Origins: a 2010 blog post, a book, and three websites

**[1] Ash Maurya, "How I Document My Business Model On 1 Page" (ashmaurya.com, August 12, 2010) - the archived original post.** primary. **fetched-and-verified.**
`https://ashmaurya.com/blog/how-to-document-your-business-model-on-1-page`
Supports: The actual original 2010 publication: its real title, its date, Maurya's own account of building on Steve Blank's and Rob Fitzpatrick's worksheets/canvas, his critique of Osterwalder's canvas as "too general," and the original nine-box layout, which still contained a box named "Key Activity" rather than "Key Metrics."
Quotable: "How I Document My Business Model On 1 Page"
Quotable: "I do find some of Osterwalder's blocks a bit too general for a lean startup"
Quotable: "So I decided to iterate on this one more level and created a version that looks like this"
Quotable: "5. Key Activity: Describe the key action users take that maps to revenue or retention?"
Quotable: "Business Plan: A document investors make you write that they don't read. Business Model: A single diagram that describes your business."

**[2] LEANSTACK / Ash Maurya - "Why Lean Canvas versus Business Model Canvas" (leanspark.ai/learn).** primary. **fetched-and-verified.**
`https://leanspark.ai/learn/why-lean-canvas-versus-business-model-canvas/`
Supports: Maurya's own account of why he swapped Key Activities, Key Resources, Customer Relationships and Key Partners for Problem, Solution, Key Metrics and Unfair Advantage; his view that pursuing key partnerships early is 'a form of waste' for an unproven startup; the Eric Ries extreme-uncertainty framing behind the redesign; Maurya's own retrospective timeline (May 2010 exposure to Osterwalder's book, Jun 2010 exposure to Rob Fitzpatrick's variant, Aug 2010 publication of his adaptation, Sep 2010 start of the online tool, book tie-in), his stated reasons for each of the four boxes he added (Problem, Solution, Key Metrics, Unfair Advantage) and the four he removed (Key Activities, Key Resources, Customer Relationships, Key Partners), and his statement that Running Lean was "first self-published as an ebook in February 2010, now being republished as a second edition O'Reilly title in March 2012."
Quotable: "I felt both these boxes were more "outside-in" (versus entrepreneur) focussed"
Quotable: "This seemed better captured by the existing Channels box."
Quotable: "When you are an unknown startup with an untested product, pursuing key partnerships from day one can be a form of waste."
Quotable: "Startups operate under conditions of extreme uncertainty."
Quotable: "I found the initial Business Model Canvases I created back in August 2009 missing things I'd consider very high risk"
Quotable: "Lean Canvas also became a critical part of the methodology described in my book: Running Lean - first self-published as an ebook in February 2010, now being republished as a second edition O'Reilly title in March 2012"
Quotable: "This box wasn't intended to discourage you from moving forward on your vision but rather to continually encourage you to work towards finding/building your unfair advantage"
Quotable: "pursuing key partnerships from day one can be a form of waste"
Quotable: "I chose to work within the existing layout constraints to attribute the work back to Alex Osterwalder's original canvas"

**[3] Ash Maurya - personal site (ashmaurya.com), checked directly for any "Leaner Canvas" article or reference.** primary. **fetched-and-verified.**
`https://ashmaurya.com`
Supports: Absence: the site content returned (homepage and a site search for "leaner canvas") contains no article, template or mention titled or described as a "Leaner Canvas." Maurya is referred to throughout only as the creator of the (plain) Lean Canvas; Confirms Running Lean's current edition (3rd, 2022) directly from the author's own site, and that this site is where his blog archive (including the original 2010 post) now lives, separate from leanstack.com and leanspark.ai
Quotable: "Running Lean 3rd edition · 2022 The step-by-step playbook for going from initial idea to a business model that works, before running out of resources. Started as posts on this blog; now in its third edition and used by founders, accelerators, and universities worldwide."

**[4] LEANSTACK, Inc., homepage (leanstack.com).** primary. **fetched-and-verified.**
`https://leanstack.com`
Supports: The current structure of Maurya's web presence: LEANSTACK is the company; leanspark.ai is "LEANSTACK's AI product for practicing Running Lean" and hosts the Lean Canvas material (leanspark.ai/leancanvas); his writing has moved to a separate personal site, ashmaurya.com
Quotable: "LEANSTACK is the company behind LEANSpark."
Quotable: "The 1-page business model format used by over a million entrepreneurs. Created by Ash Maurya as a startup-focused adaptation of the Business Model Canvas."

**[5] LeanFoundry (Ash Maurya's company site), "About" bio page.** primary. **fetched-and-verified.**
`https://www.leanfoundry.com/about`
Supports: Maurya's own bio lists him as 'Creator of Lean Canvas' and separately as 'Customer Factory Framework creator' -- a second, separate framework he built specifically to map the customer-acquisition funnel over time, which is evidence that the nine boxes of the canvas itself do not track a funnel or a dated progression of what has been learned; that had to be built as a companion tool. Checked leanfoundry.com's own terms page (leanfoundry.com/terms) first: no clause on scraping, crawling or automated access
Quotable: "Creator of Lean Canvas"
Quotable: "Customer Factory Framework creator"

### Structure: nine boxes, three sub-blocks, and a fill order

**[6] Ash Maurya, "What is a Lean Canvas?" (leanspark.ai, published September 7, 2024).** primary. **fetched-and-verified.**
`https://leanspark.ai/learn/what-is-lean-canvas`
Supports: Box-by-box WHAT/WHY/ASK content for every box except Key Metrics' numeric detail; the 20-minute and 1-page constraints; the no-groupthink and leave-blank-if-unsure rules; the recommended fill order (Customer Segments first); the Unique Value Proposition, Solution, Channels, Revenue Streams, Cost Structure, Key Metrics and Unfair Advantage guidance in Maurya's current wording; Maurya's first-person statement that Lean Canvas is his own adaptation of Osterwalder's Business Model Canvas, and his summary of the swap (key partnerships, key resources, key activities, customer relationships replaced by problem, solution, key metrics, unfair advantage)
Quotable: "your initial big idea canvas should be sketched quickly - in less than 20 minutes"
Quotable: "Embrace a 1-page constraint"
Quotable: "Describing your idea on a single page is not about using smaller fonts but fewer words."
Quotable: "Set a timer for 20 minutes"
Quotable: "If you're part of a team, avoid creating a Lean Canvas as a group exercise. Instead, have each team member create their snapshot first."
Quotable: "it's okay to leave boxes blank"
Quotable: "There is no right order for sketching a Lean Canvas"
Quotable: "A customer is someone who pays for your product. A user does not."
Quotable: "Your objective is to define an early adopter, not a mainstream customer."
Quotable: "Problems, not solutions, create spaces for innovation."
Quotable: "List the top one to three problems."
Quotable: "Document how you think your early adopters currently address these problems today."
Quotable: "I purposely made the solution box less than one-ninth of the entire canvas"
Quotable: "Bind a solution to your problem as late as possible."
Quotable: "List 3-5 key metrics"
Quotable: "Prefer outcome metrics versus output metrics."
Quotable: "Rather than thinking in terms of three- or five-year forecasts, it's better to take a more stage-based approach. Focus on your most immediate short-term milestones three to six months from now."
Quotable: "A real unfair advantage is something that cannot be easily copied or bought."
Quotable: "Leave the unfair advantage blank."
Quotable: "Lean Canvas was created by me, Ash Maurya, and is an adaptation of Alexander Osterwalder's Business Model Canvas - optimized for the Lean Startup methodology."
Quotable: "I replaced these boxes: key partnerships, key resources, key activities, and customer relationships with these boxes: problem, solution, key metrics (KPIs), and unfair advantage (a defensible competitive advantage)."
Quotable: "helps you deconstruct an idea into key assumptions or beliefs"
Quotable: "Typical SaaS metrics"
Quotable: "Unlike a business plan, the goal with a Lean Canvas isn't to achieve perfection but to take a snapshot."
Quotable: "Like everything on the canvas, you start with the best guess and iterate from there."
Quotable: "what are the next hypotheses you need to test to move your product forward?"
Quotable: "sketch out the simplest thing you could build"

**[7] Ash Maurya, "Build Your Lean Canvas in 5 Minutes" / "What is a Lean Canvas?" definition section (leanspark.ai/leancanvas).** primary. **fetched-and-verified.**
`https://leanspark.ai/leancanvas`
Supports: The twelve-block breakdown (nine boxes plus Existing Alternatives, Early Adopters, High-Level Concept as the three named sub-blocks), one-line definitions of each block, and the four boxes Lean Canvas substitutes for BMC's Key Partners/Key Activities/Key Resources/Customer Relationships; A second, independently-worded statement of the 2010 creation date and the same four-box substitution, plus the current 12-field enumeration (the original problem/customer-segments/early-adopters split did not exist in the 2010 post)
Quotable: "Lean Canvas is a 1-page business model template created by Ash Maurya in 2010."
Quotable: "identifying and testing your riskiest assumptions before you build"
Quotable: "Customer Segments - Who has the problem and who will pay"
Quotable: "Existing Alternatives - How customers solve these problems today"
Quotable: "Early Adopters - The specific subset of customers you target first"
Quotable: "High-Level Concept - The X for Y analogy that makes your idea instantly understandable"
Quotable: "Lean Canvas replaces four boxes from the original BMC - Key Partners, Key Activities, Key Resources, and Customer Relationships - with startup-specific ones: Problem, Solution, Key Metrics, and Unfair Advantage."
Quotable: "Lean Canvas is a 1-page business model template created by Ash Maurya in 2010. It adapts Alexander Osterwalder's Business Model Canvas for startups operating under conditions of extreme uncertainty."
Quotable: "The 12 blocks of a Lean Canvas"
Quotable: "How customers solve these problems today"
Quotable: "The specific subset of customers you target first"
Quotable: "The X for Y analogy that makes your idea instantly understandable"

### Practice: who fills the canvas, and when it changes

**[8] LEANSTACK/LeanSpark (Ash Maurya's company), "Canvas" guide page, LEANSpark product documentation.** vendor. **fetched-and-verified.**
`https://leanspark.ai/guides/canvas`
Supports: Versioning and parallel-variant practice built into Maurya's own tool: the premise that a canvas is kept current rather than written once
Quotable: "Your canvas is versioned automatically. You can view past versions and restore any previous state."
Quotable: "Your business model can have multiple variants - different pivot directions or market segments you're exploring. Switch between variants from the context bar at the top."
Quotable: "Variants are alternative versions of your business model. For example, you might have one variant targeting consumers and another targeting businesses."
Quotable: "Your canvas is versioned automatically."

**[9] Prof. Elaine Chen, Derby Entrepreneurship Center at Tufts (Tufts Venture Accelerator), "Entrepreneurial Frameworks" workshop page.** practitioner. **fetched-and-verified.**
`https://derbyecenter.tufts.edu/workshops/bootcamp2-frameworks/`
Supports: A named accelerator program's own stated calendar cadence and who fills the canvas (the founder cohort, under coach review)
Quotable: "The Lean Canvas will be a weekly deliverable for the Full Time cohort as part of our weekly accountability framework."
Quotable: "We will be using the Lean Canvas throughout the summer to check your progress and identify issues to address."
Quotable: "This session is led by Prof. Elaine Chen, Cummings Family Professor of the Practice in Entrepreneurship and Director, Derby Entrepreneurship Center."

### Debates: startups and established firms, and what the canvas leaves out

**[10] SmartCompany (Startup Smart) - "Running Lean author Ash Maurya's warning about the one trap founders shouldn't fall into".** practitioner. **fetched-and-verified.**
`https://www.smartcompany.com.au/startupsmart/running-lean-author-ash-mauryas-warning-about-the-one-trap-founders-shouldnt-fall-into/`
Supports: Maurya's own term for the solution-first trap ('innovator's bias'), in his own words, including that he includes himself among those who fall into it, and his prescription to shift focus from the product being built to the business model being built
Quotable: "The biggest mistake I find which we all make - myself included - is this love for the solution,"
Quotable: "It's what I call an innovator's bias."
Quotable: "shifting the perception of what the product is from the thing we're building to the business model we're building."

**[11] Ash Maurya, "Reorder your Chain of Beliefs with a Leaner Lean Canvas" (LEANSpark/LEANSTACK blog, 7 September 2024).** primary. **fetched-and-verified.**
`https://leanspark.leanstack.com/learn/reorder-your-chain-of-beliefs-with-a-leaner-lean-canvas/`
Supports: Maurya's own teaching treats two things the task's example list names -- evidence behind a belief, and which beliefs are riskiest -- as practices layered ON TOP of the nine-box canvas, not as fields the canvas itself asks for. He tells readers to 'focus on your weakest links first -- your riskiest assumptions' and to check whether 'customer and problem assumptions are not yet grounded in empirical learning' before trusting the rest of the model. He goes further and proposes a 'Lean(er) Canvas' that drops seven of the nine boxes down to just Customer Segment and Problem, precisely because the full nine-box layout does not by itself tell a reader which belief is weakest. This is leanstack.com's own blog subdomain (leanspark.leanstack.com), distinct from the two leanspark.ai pages the structure dimension owns, and distinct from leanstack.com's main site; leanstack.com's Customer Terms of Service (checked at leanstack.com/terms, effective 1 August 2018) carry no clause on scraping, crawling, robots or automated access, so the site is not excluded
Quotable: "focus on your weakest links first - your riskiest assumptions"
Quotable: "If your customer and problem assumptions are not yet grounded in empirical learning, it’s prudent first to get them in order."
Quotable: "While sketching out a complete Lean Canvas is a great exercise for baselining an idea and internalizing the “business model as the product” mindset, at the earliest stages, however, it helps to more narrowly focus attention on just the two outer boxes of the canvas"

### Relationships: the Business Model Canvas and the Product Vision Board

**[12] Roman Pichler, "The Product Vision Board" (blog article, romanpichler.com).** primary. **fetched-and-verified.**
`https://www.romanpichler.com/blog/the-product-vision-board/`
Supports: Relationship between the Product Vision Board and the Lean Canvas / Business Model Canvas, and a recommended sequence (vision/strategy first, business-model detail after)
Quotable: "There are, of course, other helpful tools available... including Ash Maurya's Lean Canvas"
Quotable: "While a strength of the Product Vision Board is its simplicity, it does not detail how the business goals are achieved"
Quotable: "it does not capture the business model including the competitors, the partners, the channels"
Quotable: "The product vision board is the simplest thing that could possibly work to capture the vision and strategy of a product"
Quotable: "complement the product vision board with the business model canvas"
Quotable: "inspired by the business model canvas"

**[13] LeanSpark (Ash Maurya's company, formerly LeanStack), "Lean Canvas vs BMC" (comparison page, leanspark.ai).** vendor. **fetched-and-verified.**
`https://leanspark.ai/compare/lean-canvas-vs-bmc/`
Supports: What Lean Canvas does that BMC does not and vice versa, framed by Ash Maurya's own company, plus a recommended sequence between the two (Lean Canvas pre-PMF, BMC for operational planning after)
Quotable: "Find the riskiest assumption, test it"
Quotable: "Lean Canvas was designed for entrepreneurs, not consultants, customers, advisors, or investors"
Quotable: "the better tool for mapping and communicating established business models"
Quotable: "If you are pre-product-market fit, start with Lean Canvas"
Quotable: "Use what is most natural for you"

### Gaps: what a canvas leaves unasked

**[14] Bastian Coes, "Critically Assessing the Strengths and Limitations of the Business Model Canvas" (University of Twente, Master's thesis, Business Administration, 13 March 2014).** practitioner. **fetched-and-verified.**
`https://essay.utwente.nl/64749/1/Coes_MA_MB.pdf`
Supports: The thesis's own comparison table for the Lean Canvas (Table 2, p.25) marks 'Financial aspects: Not specifically mentioned in the tool' -- meaning even in a dedicated academic comparison, the canvas's Cost Structure and Revenue Streams boxes are not treated as giving financial depth. Separately (p.29-30) the thesis finds a 'theoretical limitation of the Business Model Canvas is the lack of incorporating strategy,' a limitation the Lean Canvas inherits wherever it reuses BMC boxes unchanged (Channels, Customer Segments, Cost Structure, Revenue Streams, per the thesis's own Lean Canvas table). Terms checked first: utwente.nl's disclaimer page (utwente.nl/en/about-our-website/disclaimer) bars only copying/reproducing/altering content without permission -- a copyright clause, not a bar on automated access -- so this is not a terms-rule exclusion
Quotable: "a theoretical limitation of the Business Model Canvas is the lack of incorporating strategy"

### A walkthrough read from the maintainer's own copy

**[15] Ash Maurya - How to Create Your Lean Canvas (2011), a 40-page PDF whose pages carry the running head "Running Lean".** primary (originator's own walkthrough). **fetched-and-verified, read from the maintainer's own copy on 2026-10-30.**
No URL: a copyrighted PDF, read from a text copy that the maintainer supplied from their own file on 2026-10-30; a download link would imply a retrieval that did not happen, and the text is never committed.
Supports: Maurya's own box-by-box walkthrough and worked case study. The origin account: Steve Blank's worksheets, then Osterwalder's canvas, whose elements Maurya found too general, then an adaptation tested at workshops and presentations before it became an online tool. The method: brainstorm possible customers, sketch one canvas per customer segment, starting with the top two or three, and prioritize where to start by customer pain, ease of reach, price and market size. The prescribed fill order, starting from the customer segment and taking the problem-customer pair together. The rules: sketch in one sitting, leave a section blank rather than guess at length, keep the boxes small, bind a solution to the problem as late as possible, and share the canvas with at least one other person. That pricing is among the riskiest parts of a model and should be tested early, and that the canvas is an organic document that evolves over time.
Quotable: "Sketch a Lean Canvas for each customer segment"
Quotable: "I recommend starting with the top 2-3 customer segments you feel you understand the best or find most promising."
Quotable: "Sketch a canvas in one sitting"
Quotable: "It's okay to leave sections blank"
Quotable: "I start with the Customer Segment and follow a prescribed order to filling out a canvas"
Quotable: "The "Problem-Customer" pair usually drives the rest of the canvas which is why I tackle them together"
Quotable: "Bind a solution to your problem as late as possible."
Quotable: "A real unfair advantage is something that cannot be easily copied or bought."
Quotable: "Documenting your Plan A is a prerequisite for moving on."
Quotable: "The boxes on the Lean Canvas are intentionally small because it forces you to be concise."
Quotable: "found some of his canvas elements too general"
Quotable: "an adaptation that eventually became the Lean Canvas"
Quotable: "Lean Canvas was tested and refined in these presentations and workshops before it ever became an online tool"
Quotable: "While a business plan can take weeks or months to write, your initial canvas should be sketched quickly."
Quotable: "Like everything on the canvas, you start with a best guess and then iterate from there."
Quotable: "Once you have your Lean Canvases sketched for each customer segment, lay them side by side and select the best business model to start with."
Quotable: "Here is the weighting order I use (ranked from highest to lowest)"
Quotable: "Second, I believe pricing is one of the riskiest (and most critical) parts of the business model and should be tested early."
Quotable: "Too many founders carry their hypotheses in their heads alone which makes it hard to systematically build and test a business."
Quotable: "You have to draw a line in the sand."
Quotable: "The important thing is sharing it with at least one other person when you are done."
Quotable: "A lot of entrepreneurs skip this step altogether which is NOT the solution."
Quotable: "The canvas is meant to be an organic document that evolves over time"
Quotable: "tracking ongoing learning"

## Pages not read under the terms rule

The research agents found each page below and did not read it, or read it before checking the site's terms and
then withdrew it, because the site's terms of use forbid automated access or the build treats the site as barred.
The maintainer has not read any of them by hand. No claim or quotation in this bundle rests on them. The excluded
sites and their clauses are listed in `docs/internal/bundle-pipeline.md`, under "The terms rule". The main loop
read the terms pages of Strategyzer, Tability and the Wade Institute studio on 2026-10-30 and added all three to
that table.

- `https://www.strategyzer.com/`. Strategyzer's terms bar access by any means other than the interface Strategyzer provides.
  The site would have given Osterwalder's own view of how the Lean Canvas differs from the Business Model Canvas,
  and any sequence he recommends between them. The relationships finding therefore rests on Maurya's side alone.
- `https://www.atlassian.com/software/confluence/templates/lean-canvas` and
  `https://www.atlassian.com/software/confluence/resources/guides/how-to/lean-canvas`. Atlassian is treated as
  barred: admission sweep 7 reported a bar on 2026-10-29, and nobody has read its raw terms page. Three dimensions
  wanted the pages: for the drawbacks Atlassian lists, for how it relates the canvas to other templates, and for
  whether its template adds fields such as a date, an owner or an evidence column beyond Maurya's boxes.
- `https://www.tability.io/odt/articles/lean-canvas`. Tability's acceptable-use policy bars spiders, robots and
  crawlers. A debates agent fetched the page before checking the policy; nothing from it was used. The page is a
  practitioner critique of common misuse: treating the canvas as a deliverable, filling it alone, and an
  under-thought Channels box. Two dimensions wanted it.
- `https://miro.com/templates/leaner-canvas-template/`. Miro's terms bar scraping (runbook table). The same agent
  fetched the page before checking the table; nothing from it was used. Its title, which brackets the "er", may explain
  why some pages describe a separate leaner canvas. Maurya's own post [11] now settles what the phrase means.
- `https://newsletter.leanstack.com/p/the-lean-canvas-diagnostic-3-identify`. The newsletter is hosted on
  Substack, whose terms bar crawling (runbook table). A practice agent fetched it before checking the host and
  deleted the cache entry at once; nothing from it was used. The post is Maurya's own part 3 of 7 on ranking the
  riskiest assumptions, and would have said how his method picks the next belief to test.
- `https://www.koji.so/docs/lean-canvas-guide`. koji.so is on the runbook table. Found only as a search-result
  title for a guide to mapping, validating and iterating a canvas.
- `https://studio.wadeinstitute.org.au/tool-detail-lean-canvas.html`. The studio's terms bar automated tools that
  access it at scale without written permission. A practice agent read the page before the main
  loop read those terms. The clause is qualified, but the entry was withdrawn rather than argued. The page is a
  university toolbox entry on using the canvas.
