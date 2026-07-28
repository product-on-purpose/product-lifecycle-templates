---
title: "{{product_name}} Product Vision"
product: "{{product_name}}"
owner: "{{who_owns_this_vision}}"
horizon: "{{target_year_or_range}}"
status: "{{draft_or_agreed}}"
last_updated: "{{date}}"
next_review: "{{date_or_trigger}}"
doc_type: product-vision
size: full
format: canvas
source_template: product-vision
source_template_version: 0.1.0
---

<!--
FULL PRODUCT VISION (canvas format). The lean vision plus everything needed for it to survive contact with
people who were not in the room: the competitive context that explains why this future is not already
someone else's, the business goals that stop it being borrowed grandeur, an explicit horizon with a review
trigger, and the assumptions it rests on. This is a strict superset of product-vision_template-lean.md;
every lean section appears here unchanged and in the same order.

USE FULL WHEN the vision will be handed to an incoming leader, cited in a funding conversation, read by a
board, or used to justify declining something expensive. Use lean when a small team needs a shared
destination it can cite in a prioritisation argument. See product-vision_companion.md section 4.

THE TEST THIS DOCUMENT HAS TO PASS is the same at either size: can it be used to refuse something? If it
cannot be cited to kill a plausible request from someone senior, it is decoration, however well written.

THIS IS ONE OF THREE FORMATS. The canvas orients and is citable;
product-vision_template-narrative-full.md persuades; product-vision_template-prfaq-full.md argues that the
future is worth having. They are different documents serving one purpose, not sizes of one document, and
the library ships all three because the two most-cited authorities on product vision genuinely disagree
about whether a canvas can do this job. See product-vision_companion.md section 4.

HOW TO FILL THIS IN
1. Read the comment under each heading: WHAT it wants, WHY it matters (with a pointer into
   product-vision_companion.md), guiding questions to ASK, a GOOD and a WEAK example, and the TRAP to avoid.
2. Replace each {{placeholder}} with your content.
3. Write it with the people who will have to live by it. The alignment argument is most of the value.
4. If a section does not apply, write "N/A" and one line of why, rather than deleting it.
5. Before you share it: self-grade against product-vision_guide.md, then DELETE every HTML comment.
-->

# {{product_name}} Product Vision

## The Vision

<!-- WHAT  The future you intend to create, described as a state of the world rather than as a plan. Two or
           three sentences, or one memorable line plus a short paragraph. Write it so someone can picture it.
     WHY   The one piece of evidence-backed advice in this whole subject is about this section: vision
           statements that carry a lot of concrete imagery and only a small number of abstract values are
           associated with better performance, and leaders in practice tend to do the opposite. Concrete
           picture, few abstractions. That finding studied leader RHETORIC rather than written documents and
           only its experimental half is causal, so treat it as a strong steer, not a law. Deep dive:
           product-vision_companion.md section 3 (The Vision) and section 6.
     ASK   What is different about the world once this works? Who is doing what, that they cannot do today?
           If a stranger read only this paragraph, what would they picture? Which single word here is doing
           the most work, and is it a picture or an abstraction?
     GOOD  "Anyone at Acme who has a question about the business can answer it themselves, in the time it
           takes to ask it out loud. The people who own the numbers stop being a queue in front of them."
     WEAK  "To be the leading provider of best-in-class analytics solutions that delight our customers and
           drive value." (abstractions stacked on abstractions; nothing to picture, nothing to disagree with)
     TRAP  Writing your mission here by mistake. A mission says what you do now and why you exist; a vision
           says what the world looks like when you have succeeded. If your sentence would still be true and
           unchanged in ten years of no progress, it is a mission. -->

{{the_vision}}

## Who It Is For, and What They Need

<!-- WHAT  The specific people this future is for, and the need or problem it addresses for them. Name a
           group narrow enough to exclude someone.
     WHY   A vision for everyone constrains nothing, and a vision that constrains nothing cannot be used to
           decline anything. Naming who this is NOT for is what gives "What This Rules Out" something to
           bite on. Deep dive: product-vision_companion.md section 3 (Who It Is For, and What They Need).
     ASK   Who exactly? What do they do today instead, and what does that cost them? Who is explicitly not
           the target, even though they might use it? What need is durable enough to still exist in five
           years?
     GOOD  "Operations and finance managers at mid-market companies who currently wait on a two-person
           analytics team. They need answers within a working session, not within a sprint. Not for
           professional analysts, who are better served by the query tools they already have."
     WEAK  "Business users who need data." (excludes nobody, so it permits everything)
     TRAP  Describing a market segment instead of a person with a problem. "Mid-market SaaS" is a place to
           sell, not a need to serve. -->

{{who_it_is_for_and_what_they_need}}

## Why Us

<!-- WHAT  What makes this team or product the one that reaches this future, when others have not. An
           insight, an asset, a capability, or a bet about where the world is going.
     WHY   This is what separates a vision from a wish. Without it, the document describes a future anyone
           could pursue, which gives a reader no reason to believe this one. Deep dive:
           product-vision_companion.md section 3 (Why Us).
     ASK   What do we know, have, or believe that others do not? What has changed recently that makes this
           possible now when it was not before? If a well-funded competitor read this, what could they not
           simply copy next quarter?
     GOOD  "We already sit inside the systems where the questions get asked, so we can answer them in
           context rather than in a separate tool. Every general-purpose analytics product has to import the
           data first; we do not."
     WEAK  "Our team is world-class and deeply committed to customer success." (true of everyone who would
           ever write this sentence, and therefore evidence of nothing)
     TRAP  Listing current features. Features are what you have built toward the vision, not the reason you
           will reach it. A feature list here dates the document within two quarters. -->

{{why_us}}

## Market and Competitive Context

<!-- WHAT  What exists today that people use instead, why those alternatives do not reach this future, and
           what is changing in the market that makes now the moment. Include the honest option of "they do
           nothing" or "they use a spreadsheet", which is usually the real incumbent.
     WHY   A vision written without this reads as though the future is unoccupied. It almost never is, and a
           reader who knows the market will discount the whole document if it pretends otherwise. This is
           also the section that stops a vision quietly describing a future a competitor has already
           reached. Deep dive: product-vision_companion.md section 3 (Market and Competitive Context).
     ASK   What do our target users do today instead? Which alternatives are structurally unable to get
           where we are going, and why? What shift (technical, regulatory, behavioural) opens this window,
           and could it close? Who else is aiming at this same future?
     GOOD  "Today these questions go to a shared analytics inbox, or into a spreadsheet that is copied and
           diverges. General-purpose BI tools can answer them but require modelling work our users cannot
           do, so adoption stalls at the analyst. The shift we are riding is that operational systems now
           expose usable APIs, which is what makes answering in context possible at all."
     WEAK  "The analytics market is large and growing, with several established players." (market sizing,
           not competitive reasoning; tells the reader nothing about why this future is reachable by us)
     TRAP  Naming competitors and asserting they are worse. State what their approach structurally cannot
           do. "Slower and clunkier" is an opinion that ages badly; "requires a modelling step our users
           cannot perform" is a claim with a mechanism. -->

{{market_and_competitive_context}}

## What This Rules Out

<!-- WHAT  The work this vision makes it correct to decline: directions, customer segments, or categories of
           feature that would serve someone else's future rather than this one. Two to five concrete
           examples, ideally ones somebody has actually proposed.
     WHY   THIS IS THE SECTION THAT DECIDES WHETHER THE DOCUMENT IS REAL. The sharpest available test of a
           product vision is whether it can be used to refuse a feature request from an influential
           stakeholder. A vision that has never been cited to say no is not guiding anything, whatever else
           it is doing. Deep dive: product-vision_companion.md section 3 (What This Rules Out) and section 7.
     ASK   What has been proposed in the last year that this future says no to? Which adjacent market are we
           deliberately not entering? What would we refuse even if a large customer paid for it? If nothing
           comes to mind, is the vision specific enough to rule anything out at all?
     GOOD  "We are not building a general-purpose query builder; that serves analysts, and analysts are not
           who this is for. We are not pursuing the enterprise compliance-reporting market, which needs
           audit guarantees this future does not require. We would decline a bespoke data warehouse
           integration for a single large account, because it moves us toward being a services business."
     WEAK  "We will stay focused and avoid distractions." (names nothing, refuses nothing, and will never be
           quoted in a real argument)
     TRAP  Listing only things nobody wanted to do anyway. If every exclusion is uncontroversial, the section
           is theatre. At least one entry should be something a reasonable colleague would argue for. -->

{{what_this_rules_out}}

## Business Goals

<!-- WHAT  What reaching this future is worth to the organisation, in the organisation's own terms: revenue,
           retention, market position, cost, strategic option. Not metrics with targets, which belong to
           strategy and OKRs; the outcome the business is buying.
     WHY   This is the section that catches borrowed grandeur, the named failure mode where a team writes a
           vision far larger than its actual ambition or resources. Stating the business outcome forces the
           vision to be one the company would actually fund. It is also the honest place to admit that the
           vision serves the company and not only the customer. Deep dive: product-vision_companion.md
           section 3 (Business Goals).
     ASK   Why would the company invest years in this rather than something else? What does it unlock that
           is hard to get another way? If we reach this future, what is measurably different about the
           business? Would the company fund this at the scale the vision implies?
     GOOD  "Self-service answers remove the analytics team as a bottleneck on every other product decision,
           which is the constraint on how fast the rest of the portfolio can move. Commercially, it changes
           us from a reporting add-on into the system of record for operational questions, which is a
           renewal argument rather than a feature argument."
     WEAK  "Increase revenue and improve customer satisfaction." (true of every product ever funded)
     TRAP  Putting KPI targets here. A number with a date is a key result and belongs in the OKR set; it
           will be stale long before the vision is, and its staleness will make the vision look stale too. -->

{{business_goals}}

## Horizon and Review

<!-- WHAT  How far out this future sits, and the explicit trigger for revisiting it. A date, plus the kinds
           of learning that would justify a rewrite.
     WHY   The dominant failure of product visions is not that they are wrong, it is that they are written
           once and never read again. A named review trigger is the cheapest available defence. On horizon,
           practitioner guidance clusters around a few years out for software and longer for hardware, but
           there is no evidence behind those numbers and the two most-cited authorities disagree; the useful
           framing is that a one-year vision is a roadmap and a ten-year one drifts from reality. Deep dive:
           product-vision_companion.md section 3 (Horizon and Review) and section 6.
     ASK   By when do we expect this to be true? What would have to happen for this vision to be wrong
           rather than merely behind schedule? Who reviews it, and when is the next one? What learning would
           change it, as opposed to changing the strategy underneath it?
     GOOD  "Horizon: 2029, roughly three years out. Reviewed each October alongside annual planning, and
           immediately if either of the leaps of faith below is disproven. A strategy change does not
           trigger a rewrite; the strategy is expected to change several times on the way here."
     WEAK  "This is a long-term vision that we will revisit periodically." (no date, no trigger, no owner,
           so nobody will)
     TRAP  Treating every strategy change as a reason to rewrite the vision. If the destination moves every
           time the route does, it was never a destination. -->

{{horizon_and_review}}

## Leaps of Faith

<!-- WHAT  The assumptions this vision rests on that you cannot yet prove, stated plainly, with what would
           tell you each one is wrong.
     WHY   An ambitious multi-year vision cannot be validated before you commit to it; if it could, it would
           not be ambitious. Naming the unproven parts is what separates a considered bet from wishful
           thinking, and it is what makes the review trigger above actionable. It also protects the
           document: a vision that turns out to be wrong for a stated reason is a good decision that did not
           work, while one that was never examined is just a mistake. Deep dive:
           product-vision_companion.md section 3 (Leaps of Faith) and section 6.
     ASK   What must be true about our users for this future to matter to them? What must be true about the
           technology or the market? Which of these is most likely to be wrong? What is the cheapest signal
           that would tell us early?
     GOOD  "We assume non-analysts will trust an answer they did not derive themselves, which is the biggest
           unknown; the early signal is whether pilot users act on answers or re-check them with the
           analytics team. We assume operational APIs stay open enough to read in context; the signal is
           vendor rate-limit and licensing changes."
     WEAK  "Some risks exist and we will monitor them." (no assumption named, so nothing can be disproven)
     TRAP  Listing only comfortable assumptions. If none of them frightens anyone, the real bet is still
           unstated and the section has made the vision look examined without examining it. -->

{{leaps_of_faith}}
