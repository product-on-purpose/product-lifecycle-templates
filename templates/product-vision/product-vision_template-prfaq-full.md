---
title: "{{product_name}} Product Vision"
product: "{{product_name}}"
owner: "{{who_owns_this_vision}}"
dateline: "{{future_date_two_to_three_years_out}}"
status: "{{draft_or_agreed}}"
last_updated: "{{date}}"
doc_type: product-vision
size: full
format: prfaq
source_template: product-vision
source_template_version: 0.1.0
---

<!--
PRODUCT VISION, PR/FAQ FORMAT. A launch announcement written as though the future has already happened,
dated years ahead, followed by the questions it provokes. This is a DIFFERENT DOCUMENT from the canvas and
the narrative, not a longer one, and the gate asserts no nesting relationship between formats.

WHERE THIS COMES FROM, STATED CAREFULLY. The working-backwards PR/FAQ is an Amazon practice, described at
book length by Colin Bryar and Bill Carr in Working Backwards (2021). No source this library could read names
an individual as its originator, and the practice is best described as one that emerged at Amazon rather than
one that was invented by a named person. It also predates any of the product-vision literature and was not
designed as a vision format: it defines a specific launch. Using it for a multi-year vision is a practitioner
extension, and a good one, but the library says so rather than implying Amazon prescribed it. See
product-vision_companion.md sections 2 and 4.

WHEN TO REACH FOR IT. When the live question is whether this future is worth having at all. Writing the
announcement first forces the benefit into customer language before any engineering path exists, and the FAQ
forces the objections out while they are still cheap. It is the most uncomfortable of the three formats to
write, which is the point: a future that cannot be announced in plain language usually is not a future, it is
a roadmap with ambition.

RULES THAT MAKE THIS FORMAT WORK
1. DATE IT IN THE FUTURE AND WRITE IN THE PAST AND PRESENT TENSE. The launch has happened. No "will".
2. THE HEADLINE MUST BE ABOUT THE CUSTOMER, NOT THE PRODUCT. If it names a feature, start again.
3. NO INTERNAL VOCABULARY. If a phrase would need explaining to a customer, it fails here, and its presence
   usually means the benefit has not been found yet.
4. THE FAQ IS WHERE THE DOCUMENT EARNS ITS KEEP. A press release with an easy FAQ is marketing. Put the
   questions you are afraid of in it.
5. IT MUST STILL BE ABLE TO REFUSE SOMETHING. The Internal FAQ carries that job here.

HOW IT IS READ. This format is conventionally reviewed by having the room read it in silence first, then
discuss. If you are writing one, plan for that: it has to stand on its own for twenty minutes without you
narrating it.

HOW TO FILL THIS IN
1. Write the headline and the first paragraph twenty times before writing anything else. That is the work.
2. Replace each {{placeholder}} with your content.
3. Before you share it: self-grade against product-vision_guide.md, then DELETE every HTML comment.
-->

# {{product_name}}: {{customer_benefit_headline}}

## Press Release

<!-- WHAT  A one-page announcement dated {{future_date}}, written as though the future described has shipped.
           Headline, one-line subhead naming who it is for, a first paragraph stating the benefit, two or
           three paragraphs on the problem and how the world is different now, a quote from a customer, a
           quote from you, and how to get started.
     WHY   Writing the announcement first is the entire mechanism of this format: it makes you state the
           benefit in the customer's language before you have permission to talk about how it is built, and
           an unwritable press release is an early and cheap signal that the future is not compelling. Deep
           dive: product-vision_companion.md section 4 (PR/FAQ format).
     ASK   What is the headline a customer would actually care about? Who is the subhead naming? If a reader
           stopped after the first paragraph, would they know what changed and for whom? Is there a single
           word here a customer would not use?
     GOOD  Headline: "Acme customers now answer their own operational questions in under a minute."
           Subhead: "For the operations and finance managers who used to wait on an analytics queue."
           First paragraph: "Starting today, anyone at a company using Acme can ask a question about their
           own numbers in the tool where they noticed the problem, and get an answer while they are still
           thinking about it."
     WEAK  Headline: "Acme launches next-generation AI-powered analytics platform." (about the product and
           its technology, not about anyone's day; and it would have been written the same way in any of the
           last five years)
     TRAP  A customer quote that no customer would say. If your quote contains "leveraging" or a product
           name used as a verb, it is you talking. Write what Priya would say to a colleague. -->

{{press_release}}

## Customer FAQ

<!-- WHAT  The questions a customer or user asks after reading the release. Six to ten, with real answers.
           Include the awkward ones: what it costs, what it does not do, what happens to their existing way
           of working, whether they can trust the answers.
     WHY   The press release states the benefit; this establishes it is a benefit under scrutiny rather than
           in a brochure. It is also where the vision's boundaries first become visible to an outsider. Deep
           dive: product-vision_companion.md section 4 (PR/FAQ format).
     ASK   What would a sceptical user ask in the first two minutes? What does this NOT do that they might
           assume it does? What do they have to give up or change? Why should they believe the answers are
           right?
     GOOD  "Q: How do I know the answer is correct? A: Every answer shows the rows behind it and the filter
           that produced it, and you can open them. We expect people to check the first few and then stop;
           the point is that checking is possible, not that it is required."
     WEAK  "Q: Is it easy to use? A: Yes, extremely." (a question nobody asks and an answer nobody believes)
     TRAP  Only asking questions you have good answers to. The FAQ that is comfortable to write is the one
           that was not worth writing. -->

{{customer_faq}}

## Internal FAQ

<!-- WHAT  The questions the organisation asks: why this and not something else, what it rules out, what has
           to be true, what it costs, what happens if the central assumption is wrong, and how far out this
           is. Six to twelve, with honest answers including the ones that are "we do not know yet".
     WHY   THIS IS WHERE THIS FORMAT MEETS THE TEST THE OTHER TWO ALSO FACE: can the document be used to
           refuse something? The Internal FAQ is also the only part of a PR/FAQ that carries the business
           case, the horizon, and the leaps of faith, all of which the canvas format gives dedicated
           sections. If you skip it, you have written marketing rather than a vision. Deep dive:
           product-vision_companion.md section 3 (What This Rules Out, Business Goals, Leaps of Faith).
     ASK   What are we deliberately NOT building, and what has been proposed that this says no to? Why is
           this worth years rather than the alternative use of the same people? What must be true that we
           cannot prove? What would tell us early that we are wrong? By when do we expect this to be real,
           and when do we next review it?
     GOOD  "Q: Are we building a query builder? A: No, and we will keep being asked. A query builder serves
           analysts, and the release above is explicitly not for analysts. Q: What is the biggest thing we
           are assuming? A: That someone who did not derive an answer will act on it. If pilot users take
           answers to the analytics team to verify, we have built a faster way to create work for that team,
           and the vision is wrong rather than early."
     WEAK  "Q: What are the risks? A: As with any ambitious initiative, there are execution risks that we
           will manage carefully." (names nothing, refuses nothing, disproves nothing)
     TRAP  Letting this section become a project plan. Resourcing and sequencing belong to the strategy and
           the roadmap; what belongs here is why the destination is worth the journey and what would change
           our minds about it. -->

{{internal_faq}}
