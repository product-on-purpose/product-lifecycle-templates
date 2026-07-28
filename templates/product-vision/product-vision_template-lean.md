---
title: "{{product_name}} Product Vision"
product: "{{product_name}}"
owner: "{{who_owns_this_vision}}"
horizon: "{{target_year_or_range}}"
status: "{{draft_or_agreed}}"
last_updated: "{{date}}"
doc_type: product-vision
size: lean
format: canvas
source_template: product-vision
source_template_version: 0.1.0
---

<!--
LEAN PRODUCT VISION (canvas format). The smallest vision that can still do a vision's job: the future you
intend to create, who it is for and what they need, why this team is the one to build it, and what it rules
out. Four sections, one page. To grow it into a vision that has to survive people who were not in the room
(see product-vision_template-full.md), ADD sections; never rename or reorder the ones below, because the full
variant is a strict superset of this one.

THE TEST THIS DOCUMENT HAS TO PASS. A vision is not judged by how it reads. It is judged by whether anyone
can use it to refuse something. If it cannot be cited to kill a plausible feature request from someone
senior, it is decoration, however well written. That is why "What This Rules Out" is in the LEAN variant and
not an optional extra: it is the section that makes the other three usable.

THE FAILURE MODE TO EXPECT IS NOT BAD WRITING, IT IS DISUSE. The most commonly reported failure of product
visions is that they are written once, stored somewhere, and never consulted again. Nothing in a template
can prevent that. What a template can do is make the vision short enough to remember and specific enough to
argue with. See product-vision_companion.md section 7.

THIS IS ONE OF THREE FORMATS, AND THE CHOICE IS REAL.
- This canvas orients people fast and gives them something citable.
- product-vision_template-narrative-full.md is prose, for when the vision has to persuade rather than orient.
- product-vision_template-prfaq-full.md is a launch announcement dated years out, for when the argument is
  whether this future is worth having at all.
They are not sizes of one document; they are different documents serving one purpose, and the most cited
authority on product vision argues that a canvas alone cannot do what the narrative does. The library ships
all three rather than pretending that disagreement is settled. See product-vision_companion.md section 4.

WHAT A PRODUCT VISION IS, AND IS NOT
It describes a future state. It is NOT a mission (that describes present purpose), NOT a strategy (that is
the set of choices for getting there), NOT a roadmap (that is sequence and timing), and NOT a positioning
statement (that is how you stand against alternatives for a customer today). The vision/mission boundary is
the one practitioners get wrong most often. See product-vision_companion.md section 8.

HOW TO FILL THIS IN
1. Read the comment under each heading: WHAT it wants, WHY it matters (with a pointer into
   product-vision_companion.md), guiding questions to ASK, a GOOD and a WEAK example, and the TRAP to avoid.
2. Replace each {{placeholder}} with your content.
3. Write it with someone, not for them. The alignment argument is most of the value; the document is the
   residue of it.
4. If a section does not apply, write "N/A" and one line of why, rather than deleting it.
5. Before you share it: self-grade against product-vision_guide.md, then DELETE every HTML comment. They are
   guidance, not content.
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
           (a state of the world, in customer terms, picturable, no feature named)
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
           decline anything. Naming who this is NOT for is what gives the next section something to bite on.
           Deep dive: product-vision_companion.md section 3 (Who It Is For, and What They Need).
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
