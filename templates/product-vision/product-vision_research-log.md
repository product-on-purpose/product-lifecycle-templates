# Research log: product-vision

Built for the `product-vision` bundle (strategy-docs family, first member) to the methodology section 6
honest-retrieval standard. Every source below is tagged with its tier and retrieval status; **only sources
marked fetched-and-verified may be quoted verbatim** in the companion, and each verbatim phrase used is
listed here.

**Two passes, and the second one mattered.** The first was a five-dimension fan-out (canon and origins,
structure, vision versus its neighbours, debates, practice and lifecycle), sources [1] to [36]. It ended by
naming its own gaps, and a second five-dimension pass went after each one, sources [37] to [52]. That second
pass **corrected the first rather than decorating it**, in two ways worth stating up front:

1. The first pass concluded there was **no empirical evidence base** for vision, on the strength of a single
   paywalled paper it could not read. That was wrong. Three relevant studies exist (fact 7).
2. The first pass could find **no primary Bezos source** for "stubborn on vision". One exists, in Amazon's
   2020 shareholder letter, and it is now quoted from the letter rather than from someone quoting it
   (fact 4).

Both corrections came from testing a negative rather than accepting it. That is the habit worth carrying into
the next bundle: **an unverified absence is a to-do, not a finding.**

Research date: 2026-07-25. Catalog ref: 1.

**One standing rule for this bundle, adopted because of what the research found:** every Cagan quotation comes
from a page on svpg.com that was actually fetched. Reader summaries of *Inspired* were found and read
[35][36], and they carry attractive quotable lines, but the book itself was not read, so nothing is quoted
through them. Attributing a book quote to an author via someone else's summary is precisely the failure this
bundle is most exposed to.

---

## Honest framing (the through-line for the companion)

**The uncomfortable fact this bundle has to open with:** the most-cited named authority on the product vision
specifically, Marty Cagan, rejects the approach this library is built on. His Product Vision FAQ says plainly:
*"don't expect to find a simple fill-in-the-blanks, paint-by-numbers, canvas or board approach to a strong
product vision"* [2]. He calls a strong vision *"the result of a creative process, much like crafting a
story"* [2] and *"a bit of an art form, as fundamentally it is a persuasion tool"* [1].

The other named authority, Roman Pichler, published exactly such a board in May 2011 [5] and has maintained it
since. So this is not a fringe objection against a settled practice - it is a live, unresolved disagreement
between the two people who wrote most directly about product vision as a document type. **A template for this
document type is a position in that argument, and the companion says so rather than pretending the argument
does not exist.**

The bundle's answer is not to pick a winner. It is the decision-utility test, which is the sharpest arbiter
any source offers: *"If your vision can't kill a feature request from an influential stakeholder, it isn't
doing its job"* [17]. A vision that passes that test has done its work whether it arrived as a canvas or as a
narrative. A vision that fails it is wallpaper in either format.

**This research changed the library.** The finding that the shapes are siblings rather than sizes of one
document is what prompted [ADR 0028](../../docs/internal/decisions/0028-adopt-a-format-axis.md), which added a
format axis orthogonal to size. So the bundle does not have to choose between the camps at all: it ships the
canvas Pichler published **and** the narrative form Cagan advocates **and** the Amazon PR/FAQ, and the
disagreement becomes a choice the reader makes with all three in hand. The positioning sentence is the one
circulating shape deliberately **not** shipped, for the attribution reason in point 3 below.

**The load-bearing honest-retrieval facts (do not get these wrong):**

1. **The Collins and Porras citation order is backwards in common usage.** *Built to Last* was published
   1994-09-16 [11]; the Harvard Business Review article *Building Your Company's Vision* was published in the
   September-October 1996 issue [10]. The article is a later distillation of the book, not its origin.
2. **Collins and Porras wrote about companies, not products.** BHAG, core ideology and envisioned future are
   organisation-level constructs; the Goodreads listing for the book states its scope as *"their ultimate
   creation is the company itself"* [11]. Product management borrowed the vocabulary. Neither author applied
   it to a product vision document. **The HBR article body is paywalled and was not read** [10].
3. **VERDICT, Moore positioning template: UNVERIFIABLE, after two attempts.** *Crossing the Chasm* was first
   published in 1991 [13]. The fill-in-the-blank statement universally attributed to it ("For [target
   customer] who...") was **not found verbatim in any page read** in either research pass, and no page
   identified a chapter, page, or edition. The second pass tried Google Books (404), archive.org (blocked),
   the publisher listing (no readable body) and the Wikipedia article (mentions positioning, does not
   reproduce the template) [13]. **The template may well be in the book; its presence, wording and
   location simply cannot be asserted from anything read.** Independently of that, a positioning statement is
   a market-positioning tool, not a multi-year aspiration, so its use as a vision template is a practitioner
   reframe [16][24]. This is why the positioning format is **not shipped** as one of the bundle's formats.
4. **VERDICT, "stubborn on vision": PARTIALLY CONFIRMED, and this one improved.** The first pass could find no
   primary Bezos source. The second pass read Amazon's **2020 letter to shareholders**, Bezos's last as CEO,
   which states: *"On the details, we at Amazon are always flexible, but on matters of vision we are stubborn
   and relentless."* [50] That is a primary source and it is quotable. **It is not the circulating aphorism.**
   The widely-repeated forms ("Be stubborn on the vision, and flexible on the details") are semantically
   equivalent condensations whose provenance is still unverified: the 2016, 2017, 2018, 2019 and 2021 letters
   were checked and do not contain the phrase [50], and letters before 2016 were inaccessible. **So quote
   the 2020 letter exactly, or quote Cagan quoting the aphorism [3]. Never present the aphorism as a verbatim
   Bezos quotation.**
5. **VERDICT, Amazon PR/FAQ originator: UNVERIFIABLE, and now on stronger evidence.** The second pass read
   Bryar and Carr's own site, which attributes the practice to Amazon **collectively and names no
   individual** [51]. Ian McAllister's widely-cited Quora answer returned HTTP 403 and was not read. Do not
   write "invented by". The practice is best described as one that emerged at Amazon.
6. **VERDICT, Saint-Exupery ship quote: REFUTED.** Quote Investigator was fetched and read in full [52]. The
   modern English wording appears in **no published work by Saint-Exupery**. The nearest real passage is
   *Citadelle* (1948), section LXXV, which is thematically related and completely different in wording; the
   earliest traceable English instance is a **November 1999 Usenet post** where it is already misattributed
   [52]. It is a late-1990s paraphrase by an unknown intermediary. It appears nowhere in this bundle, and the
   companion uses it as the worked example of why attribution hygiene matters in this particular field.
7. **There IS an empirical evidence base on vision, and the first pass of this research got that wrong.**
   The first pass found one paywalled paper about *mission* statements [29] and concluded no evidence existed.
   A second, targeted pass found three relevant studies about **vision** [47][48][49]. The corrected position,
   which the companion states in this form:
   - Evidence exists that **leader and organisational** vision relates to outcomes, from one longitudinal
     field study [47], one lab experiment [48], and one mixed archival-plus-experimental study [49].
   - **None of it measures a product vision document against product-team outcomes.** That negative survived
     a determined search across Google Scholar, OpenAlex and Semantic Scholar, so it is reported as
     a tested negative rather than an absence of looking.
   - **Causation is not established for real organisations.** Every real-world study is observational; the
     only causal evidence comes from lab experiments with students on simulated tasks [48]. Practitioner
     writing that says vision *causes* performance is upgrading a claim the studies do not make.
   - The bundle therefore claims **no performance benefit for writing a product vision**, which is the same
     conclusion the first pass reached, but now for a defensible reason rather than a false one.

7a. **The single most actionable evidence-backed finding in this bundle** is that vision *content composition*
   matters: a large amount of concrete imagery combined with a **small** number of values is associated with
   better performance, and leaders in practice tend to do the opposite, under-using imagery and over-using
   value-laden rhetoric [49]. This shapes the template directly: ask for a concrete picture of the future and
   cap the abstractions. Caveat that must travel with it: Carton and colleagues studied leader **rhetoric**,
   not written vision documents, and only the 62-group experiment half of that study is causal.

7b. **A retrieval caution that applies to all three studies, and is worth learning from.** All three were
   reached through the OpenAlex API, which **reconstructs** an abstract from a stored word-position index
   rather than serving the original text. Two reconstructions contain visible artifacts (see [47] and [48]),
   which proves the pipeline is lossy. A reconstruction that happens to read cleanly is therefore still not a
   verbatim quote. **No verbatim quotation is carried from any of the three**; their designs, samples and
   findings are reported as abstract-level metadata, explicitly labelled.

8. **Almost no agile framework defines a product vision, and that explains the rest of this log.** Checked
   directly: the **Scrum Guide** (2020 [37] and 2017 [38]) does not contain the word "vision" at all, its
   nearest concept being the Product Goal; the **Nexus Guide** does not either, verified by reading the full
   10-page PDF rather than a summary [39]; the **Agile Manifesto** and its twelve principles do not [40];
   **LeSS** defines no vision artifact and mentions the term only when describing what *traditional* product
   management does [43]. Two frameworks do define one: **SAFe** has an explicit Vision artifact [41], and
   **Scrum at Scale** names a "Strategic Vision" owned by the Chief Product Owner [42]. **PMBOK 7 [44],
   BABOK [45] and ISO/IEC/IEEE 29148 [46] could not be read** and are reported as unknown rather than absent.

   **Why this matters more than it first appears.** A Scrum team has no standard telling them to write a
   vision, what it should contain, or when it is done. That vacuum is what practitioner books and blogs
   filled, and it is the reason this document type's canon is *named individuals* rather than a specification.
   Which in turn is why **misattribution is this subject's characteristic failure mode** rather than staleness:
   with no authoritative text to check against, a phrase drifts from Citadelle to a Usenet post to a keynote
   slide to a template, and nothing anywhere says otherwise. Facts 1 through 6 are that drift, caught.
8. **A vision statement and a vision document are different artifacts**, and most things published under the
   title "product vision template" teach the statement. Pichler's board makes the distinction structural: one
   Vision cell, four supporting cells [6].
9. **Pichler's board has five sections, and sources that say four are counting only the supporting cells.**
   Pichler's own enumeration is unambiguous: *"The vision captures the ultimate purpose for offering a
   product. The target group characterises the product's users and customers. The needs describe the problem
   the product should address or the benefit it should offer. The product section states its standout
   features. The business goals capture the desired benefits the product should achieve for the company
   developing and providing it."* [6] A secondary source describes it as *"a one-page canvas with four cells:
   target group, needs, product, and business goals"* [24], which is the same board minus the vision cell.
10. **Pichler uses "big, hairy, audacious goal" without attribution** in his own post; the phrase is Collins
    and Porras's from *Built to Last* [8][11]. A template must not credit it to Pichler.

**The two named authorities disagree about the time horizon, and both are quotable.** Cagan: *"The product
vision should describe the desired end state 2-5 years out for software companies, and 5-10 years out for
device companies."* [2] Pichler asks for guidance *"for at least the next five years"* [8]. Cagan's upper
bound for software is Pichler's floor. Neither offers evidence; both are practitioner judgment. The most
useful framing found is a third practitioner's: *"A one-year vision is not visionary - it is a roadmap. A
ten-year vision risks becoming disconnected from market reality."* [23]

**Sharpest teaching points:**

1. **The test of a vision is whether it can refuse something.** [17] A vision nobody has ever used to say no
   is decoration, whatever its prose quality.
2. **The dominant failure mode is disuse, not bad writing.** *"Most product vision statements get written
   once, pinned to a Notion page, and never read again."* [15]
3. **Vision versus strategy is settled; vision versus mission is not.** Every source read agrees vision faces
   the future and strategy is the path [3][14][22]. On mission, sources agree on direction but disagree on
   which question each answers, and practitioners routinely label a mission statement a vision. Cagan:
   *"Most people I meet, when they show me their 'product vision,' what they are really showing me is their
   'mission statement.'"* [1]
4. **The most practical resolution of the mission argument is to stop arguing about the label.** *"The label
   matters less than whether the statement actually orients the team toward a destination."* [15]
5. **"North star" is two different things.** It is a metaphor for what a vision does, and it is also a
   specific quantitative artifact. Herbig's formulation keeps them apart: the North Star Metric is *"the
   quantified sibling of the Product Vision"* [14].
6. **Borrowed grandeur is a named failure mode**: *"a startup writes a vision way bigger than its actual
   ambition"* [15]. So is aspirational fluff: *"'Delight users through innovation' sounds nice and helps
   nobody decide what to build"* [17].
7. **Ownership is genuinely contested, three ways**, and the honest answer is that it depends on the
   organisation. Scrum literature puts it with the Product Owner [31][33]; enterprise practice puts it with
   the CPO or VP Product [26]; Cagan argues against per-team visions entirely, because *"When each team has
   their own vision, it's the equivalent of everyone picking out their own star from the sky, and calling it
   their 'north star' and then heading in their own direction."* [1]
8. **A vision cannot be validated before you commit to it.** Cagan's framing on his own site is that a vision
   is a persuasion tool [1]; the leap-of-faith framing appears in reader summaries of *Inspired* [35][36] and
   is **not quoted here** because the book was not read. The template expresses the idea structurally instead,
   through a section that asks what must be true.
9. **Vision versus positioning statement is a real boundary that the product management literature does not
   draw.** No source read compares them explicitly - which is notable, because Moore's positioning template is
   simultaneously the most widely circulated "vision template" [16][24][25]. The bundle draws the boundary
   from first principles and labels it as such.

---

## Sources (curated, deduplicated, contiguously numbered; one source per entry)

### Cagan (Silicon Valley Product Group) - the inspiration-first camp

**[1] Marty Cagan - Product Vision vs. Mission.** practitioner. **fetched-and-verified.**
`https://www.svpg.com/product-vision-vs-mission/`
Supports: the vision/mission boundary and the most common practitioner confusion; vision as persuasion tool;
the argument against per-team visions.
Quotable: "Most people I meet, when they show me their 'product vision,' what they are really showing me is
their 'mission statement.'"; "A good product vision keeps us focused on the customer"; "A good product vision
inspires ordinary people to create extraordinary products"; "A good product vision is a bit of an art form, as
fundamentally it is a persuasion tool"; "When each team has their own vision, it's the equivalent of everyone
picking out their own star from the sky, and calling it their 'north star' and then heading in their own
direction."; "Increasingly that's a video of a visiontype, which is a special form of prototype. They
dramatize the user experience. They show how our customer's lives demonstrably and emotionally improve."
Contested/time-bound: published 2020-08-04. The claim that "most" people confuse the two is a consulting
observation, not a measurement.

**[2] Marty Cagan - Product Vision FAQ.** practitioner. **fetched-and-verified.**
`https://www.svpg.com/product-vision-faq/`
Supports: **the single most important source in this bundle** - Cagan's explicit rejection of the
canvas/board/template approach; the time-horizon guidance; the creative-process framing.
Quotable: "don't expect to find a simple fill-in-the-blanks, paint-by-numbers, canvas or board approach to a
strong product vision"; "A strong product vision is the result of a creative process, much like crafting a
story."; "The product vision should describe the desired end state 2-5 years out for software companies, and
5-10 years out for device companies."; "The much more common problem is that the company gives up on their
product vision far too soon."
Contested/time-bound: published 2020-08-10. Directly conflicts with the canvas tradition [5][6]. No evidence
is offered for the 2-5 year figure.

**[3] Marty Cagan - Vision vs. Strategy.** practitioner. **fetched-and-verified.**
`https://www.svpg.com/vision-vs-strategy/`
Supports: the vision/strategy boundary; vision formats; vision as a recruiting tool; **the only verified
carrier of the "stubborn on the vision" line**.
Quotable: "the product vision describes where we ultimately want to go; the product strategy helps us decide
what problems to solve in order to get to our vision."; "the product vision should be inspiring, and the
product strategy should be very intentional."; "It might be in the form of a story board, or a narrative like
a white paper, or a prototype (referred to as a 'visiontype')."; "When done well, the product vision is one of
our most effective recruiting tools"; "trying to please everybody will almost certainly please nobody"; "be
'stubborn on the vision, and flexible on the details'"
Contested/time-bound: published 2016-07-15. Cagan credits the "stubborn" line to Bezos but gives no primary
source; see [20] and the contested-claims section.

**[4] Marty Cagan - The Power of Visiontypes.** practitioner. **fetched-and-verified.**
`https://www.svpg.com/the-power-of-visiontypes/`
Supports: the visiontype as an alternative to a written vision; the claim that most discovery happens after
the vision is set.
Quotable: "The power of a compelling visiontype is that it helps you to imagine a future that could be."; "the
vast majority of the product discovery work and innovation comes after the product vision"
Contested/time-bound: published 2024-01-02. Its Xerox PARC, Apple and HP Labs illustrations are historical
reconstructions, not primary accounts.

### Pichler - the structured-canvas camp

**[5] Roman Pichler - The Product Vision Board.** practitioner. **fetched-and-verified.**
`https://www.romanpichler.com/blog/the-product-vision-board/`
Supports: origin date and authorship of the Product Vision Board; the acknowledged influence; the vision as
overarching goal.
Quotable: "The vision plays an important role in bringing a new product to life: It acts as the overarching
goal guiding everyone involved in the development effort."; "Summarises the three to five features that make
your product stand out and that are critical for its success."; "There are, of course, other helpful tools
available that help you capture your ideas, including Ash Maurya's Lean Canvas and Alexander Osterwalder's
business model canvas."; "your overarching goal, the ultimate reason for creating the product, and the
positive change you want to bring about"; "Big and inspiring; use a brief statement or slogan; and ensure that
the stakeholders and development team(s) support it"; "Without a shared vision and an effective strategy,
people are likely to pull in different directions, and the chances of creating a successful product are slim"
Contested/time-bound: first published 2011-05-10, last updated 2025-10-13. Pichler names Osterwalder's
Business Model Canvas as the inspiration for the extended board; he does **not** cite Collins/Porras or Moore.

**[6] Roman Pichler - Product Vision Board (checklist and criteria).** practitioner.
**fetched-and-verified.** *(A distinct post from [5]; note the URL differs only by the leading "the-".)*
`https://www.romanpichler.com/blog/product-vision-board/`
Supports: **the authoritative five-section enumeration**, resolving the four-versus-five discrepancy; the
review cadence; the connection down to an outcome roadmap.
Quotable: "The product vision board is regularly inspected and adapted, at least once every three months as a
rule of thumb."; "The strategy captured on the board is systematically connected to more specific outcomes,
preferably to an outcome-based, goal-oriented product roadmap like my GO Product Roadmap."; "The vision
captures the ultimate purpose for offering a product. The target group characterises the product's users and
customers. The needs describe the problem the product should address or the benefit it should offer. The
product section states its standout features. The business goals capture the desired benefits the product
should achieve for the company developing and providing it."
Contested/time-bound: published 2023-01, updated 2024-01. **The quarterly cadence is Pichler's rule of thumb
for his own board**, not an industry norm; citing it as general guidance overstates its scope.

**[7] Roman Pichler - Tips for Writing a Compelling Product Vision.** practitioner.
**fetched-and-verified.**
`https://www.romanpichler.com/blog/tips-for-writing-compelling-product-vision/`
Supports: vision as overarching goal; brevity and memorability; collaborative authorship; vision distinct from
the product itself.
Quotable: "The product vision is the overarching goal you are aiming for, the reason for creating the
product."; "Be clear on the difference between the product vision and the product and don't confuse the
two."; "Your vision should be short and sweet, it should be easy to memorise and recite."; "Rather than
formulating a product vision and then selling it to the key people you create it together."; "Without a shared
vision, people follow their own goals making it much harder to achieve product success."
Contested/time-bound: published 2014-10-08, updated 2023-02-15. Recommendations reflect Pichler's own
framework; none is derived from survey data.

**[8] Roman Pichler - Double Vision: How to Capture the Product Vision.** practitioner.
**fetched-and-verified.**
`https://www.romanpichler.com/blog/double-vision-how-to-capture-the-product-vision/`
Supports: the two competing capture approaches (Moore-style sentence versus short aspirational goal), with
Pichler recommending the latter; the five-year floor; the strategy-changes-without-vision-changing rule.
Quotable: "a strategy change does not necessitate a vision change"; "motivates the stakeholders and
development teams to act together"; "captured as a memorable statement or slogan"; "the product's North Star
and provides continued guidance for at least the next five years"; "HEALTHY EATING"
Contested/time-bound: **Pichler uses "big, hairy, audacious goal" here without attribution**; the phrase is
Collins and Porras's [11]. Do not credit it to Pichler.

**[9] Roman Pichler (Medium) - Double Vision: Choosing the Right Approach to Capture the Product Vision.**
practitioner. **fetched-and-verified.**
`https://romanpichler.medium.com/double-vision-choosing-the-right-approach-to-capture-the-product-vision-9e5629b7e3dc`
Supports: the same two-approach argument as [8]; corroborates that the Moore-style form produces "one long
sentence" that Pichler considers harder to use.
Quotable: "guidance for at least the next five years"; "one long sentence"; "easier to understand"
Contested/time-bound: the Medium version of [8]; both read consistently. Listed separately only to record that
the claim was corroborated across two published copies, not to inflate the source count.

### Books and the misattribution chain

**[10] Harvard Business Review - Building Your Company's Vision (Collins and Porras).** primary.
**url-confirmed-not-read (paywalled).**
`https://hbr.org/1996/09/building-your-companys-vision`
Supports: **the publication date only**, which is the load-bearing fact - September-October 1996, i.e. two
years **after** the book [11].
Quotable: none. The article body was not read.
Contested/time-bound: paywalled. Everything about its contents in this log is inference from the book listing
[11] and must not be presented as a reading of the article.

**[11] Goodreads listing - Built to Last: Successful Habits of Visionary Companies.** reference (listing for a
primary work). **fetched-and-verified (the listing page; the book was not read).**
`https://www.goodreads.com/book/show/4122.Built_to_Last`
Supports: publication date 1994-09-16; that the framework's subject is the company.
Quotable (from the listing's description, not from the book): "their ultimate creation is the company itself"
Contested/time-bound: **the book was not read.** BHAG, core ideology and envisioned future are company-level
constructs; no verbatim book quotes are carried anywhere in this bundle.

**[12] Goodreads listing - Working Backwards (Bryar and Carr).** reference (listing for a practitioner work).
**fetched-and-verified (the listing page; the book was not read).**
`https://www.goodreads.com/book/show/53138083-working-backwards`
Supports: publication date 2021-02-09 and authorship; that the PR/FAQ is a product-definition practice.
Quotable: none carried. The listing description is a summary, not book text.
Contested/time-bound: **the book was not read.** The practice predates the book at Amazon, and **no source
read names its originator or date**. The PR/FAQ defines a specific launch, not a multi-year direction; its use
as a vision format is a practitioner extension.

**[13] Wikipedia - Crossing the Chasm.** reference. **fetched-and-verified.**
`https://en.wikipedia.org/wiki/Crossing_the_Chasm`
Supports: first publication 1991, and revisions in 1999 and 2014; the book's subject.
Quotable: none carried.
Contested/time-bound: **the article mentions positioning as a topic but does not quote a fill-in-the-blank
template.** The positioning statement widely attributed to this book was **not verified in any page read**,
and no page identified a chapter. See the contested-claims section.

### Boundaries and definitions

**[14] Tim Herbig - Product Vision vs. Product Strategy: What's the Difference?** practitioner.
**fetched-and-verified.**
`https://herbig.co/product-vision-vs-product-strategy/`
Supports: the settled vision/strategy boundary; **the cleanest separation of North Star Metric from vision**;
the product-versus-company vision question.
Quotable: "A Product Vision describes the future state for your users, which emerges from the value provided
by your product."; "Product Strategy describes the set of choices needed to achieve your Product Vision."; "the
North Star Metric, which acts as the quantified sibling of the Product Vision"
Contested/time-bound: last updated 2022-02-28. Herbig's view that product-first companies may have good
reason not to separate product and company vision is practitioner judgment.

**[15] Janna Bastow (ProdPad) - Product Vision Examples: 10 Great Vision Statements.** practitioner.
**fetched-and-verified.**
`https://www.prodpad.com/blog/product-vision-examples/`
Supports: **the wallpaper critique**; the borrowed-grandeur failure mode; the pragmatic resolution of the
mission/vision label argument; vision versus roadmap.
Quotable: "Most product vision statements get written once, pinned to a Notion page, and never read again";
"Borrowed grandeur, where a startup writes a vision way bigger than its actual ambition, is a common failure
mode worth avoiding"; "A product vision is how you choose a destination. The roadmap is how you plan the
route."; "A mission statement describes the now, and a vision statement describes the future."; "The label
matters less than whether the statement actually orients the team toward a destination."
Contested/time-bound: published 2026-05-07. **Bastow co-founded ProdPad, a roadmapping tool** - a vendor
position on a question about roadmaps. The wallpaper claim is an observation, not a measurement.

**[16] ProdPad - The Only Product Vision Template You'll Ever Need.** vendor. **fetched-and-verified.**
`https://www.prodpad.com/blog/product-vision-template/`
Supports: the Moore format used as a thinking tool rather than a final artifact; the brevity test.
Quotable: "can be repeated from memory in under 30 seconds."; "The templated version gives your roadmap its
logic. The finessed version gives your roadmap its message."
Contested/time-bound: this source applies Moore's positioning format as a vision template, which is the
reframe described in the contested-claims section, not Moore's own prescription.

**[17] Aakash Gupta - Product Vision Statement: A 2026 Guide.** practitioner. **fetched-and-verified.**
`https://www.aakashg.com/product-vision-statement/`
Supports: **the decision-utility test**, which is this bundle's organising idea; the failure-mode taxonomy.
Quotable: "Too vague to guide decisions, too detailed to survive reality, or too political to challenge
anyone's pet project"; "If your vision can't kill a feature request from an influential stakeholder, it isn't
doing its job"; "Teams confuse motion with direction, then wonder why every planning cycle feels like a
reset"; "Aspirational fluff: 'Delight users through innovation' sounds nice and helps nobody decide what to
build"
Contested/time-bound: practitioner judgment, not measurement. The test is offered as a heuristic and is used
here as one.

**[18] Christian Strunk - 15 Product Vision Examples + Complete Guide [2026].** practitioner.
**fetched-and-verified.**
`https://www.christianstrunk.com/blog/product-vision`
Supports: the company-versus-product vision distinction as a matter of scope.
Quotable: "a company vision is a broad, long-term aspiration...a product vision is a focused statement that
outlines the future state...of a specific product"
Contested/time-bound: last updated 2026-01-12. **The ellipses are in the extracted text**; the bridging
material is paraphrase, so this quote is used sparingly and never as a definition of record.

**[19] Anjana Rao (LogRocket) - Mission vs. Vision Statements: Key Differences and Importance.**
practitioner. **fetched-and-verified.**
`https://blog.logrocket.com/product-management/mission-vs-vision-statements-key-differences-and-importance/`
Supports: the interchangeability problem; mission as present tense, vision as future state.
Quotable: "A mission statement and a vision statement for a product are often used interchangeably, and the
intent of each often is misunderstood."; "defined in the present tense, as it tries to address what the
product is trying to actively achieve"; "a futuristic, long-term view of the company and product's objective"
Contested/time-bound: published 2023-02-02. "Often used interchangeably" is editorial observation.

**[20] Mike Belsito (Mind the Product) - Deep Dive: Crafting Your Product Vision and Mission.**
practitioner. **fetched-and-verified.**
`https://www.mindtheproduct.com/deep-dive-crafting-your-product-vision-and-mission/`
Supports: the vivid-picture framing; customer-centric over company-centric language; **and it is one of the
sources that attributes the "stubborn" line to Bezos**.
Quotable: "They are confusing a slogan about their purpose with a product vision."; "a vision can't always be
fully validated upfront - it requires a leap of faith"; "ambitious yet achievable"; "crystal clear and easily
understood"; "describe how your product will improve customers' lives"; "not just how it will benefit your
company"
Contested/time-bound: published 2024-11-20. **This page attributes lines to Cagan; those are not used as
Cagan quotes here** - [1] through [4] are used instead. Its Bezos attribution carries no primary source.

**[21] German Frassa (News Product Alliance) - Defining Your Product Mission and Vision.** practitioner.
**fetched-and-verified.**
`https://newsproduct.org/product-kit/product-mission-and-vision`
Supports: the journey/destination framing; purpose treated as a synonym for mission rather than a third
artifact.
Quotable: "If a mission is the declared purpose of the organization's journey, a product vision states how the
organization imagines the destination."
Contested/time-bound: **no publication year was visible on the fetched page.**

**[22] UserVoice - Product Roadmap vs Strategy vs Vision Explained.** practitioner.
**fetched-and-verified.**
`https://uservoice.com/blog/product-roadmap-strategy-vision`
Supports: the vision/strategy/roadmap hierarchy; vision stability.
Quotable: "Product vision is the guiding North Star, and does not change much, if at all."
Contested/time-bound: **no author or date visible on the fetched page.** Vendor-adjacent.

**[23] Salvatore Mezzatesta - How to Define a Product Vision That Actually Aligns Your Team.**
practitioner. **fetched-and-verified.**
`https://salvatoremezzatesta.com/how-to-define-product-statement/`
Supports: **the best available framing of why the horizon range is what it is**; the aspiration/realism
tension.
Quotable: "A one-year vision is not visionary - it is a roadmap. A ten-year vision risks becoming disconnected
from market reality."; "A vision that is purely aspirational without grounding in market reality becomes
fantasy. A vision that is purely realistic without ambition fails to inspire."
Contested/time-bound: the "Vision Triad" naming appears to be this author's own framing with no prior art
cited. Practitioner judgment, not consensus. **URL recorded as fetched; verify the exact slug before citing.**

### Template surveys and vendor formats

**[24] Abrar Abutouq (Userpilot) - What Product Vision Actually Is [+ 4 Frameworks for Writing One].**
practitioner. **fetched-and-verified.**
`https://userpilot.com/blog/product-vision-examples/`
Supports: the survey of the four circulating named formats; **the four-cell description of Pichler's board**
that [6] resolves.
Quotable: "The Product Vision Board from Roman Pichler is a one-page canvas with four cells: target group,
needs, product, and business goals."; "A vision is only useful if you can tell whether the product is moving
toward it."; "this framework works best when the company is struggling to explain what category it belongs
in"; "a press release is a future state expressed as if it already exists, which is exactly what a vision is";
"Start by imagining the most extreme possible user experience for the problem you are solving, then back off
just enough"
Contested/time-bound: credits Moore's template to *Crossing the Chasm* without an edition or page. The
"Star Trek Solution" naming appears to be this author's own with no prior source.

**[25] Miro - Product Vision Templates & Examples.** vendor. **fetched-and-verified.**
`https://miro.com/templates/product-vision/`
Supports: a vendor's own five-element structure; the "success scene" idea.
Quotable: "A clear definition of _who_ we are winning for."; "Images or quotes representing the struggle the
user faces today."; "A visual or narrative description of the user's life after using the product for a
year."; "describes the world as it will exist once your product has succeeded."
Contested/time-bound: Miro's structure is its own synthesis, not a named practitioner framework.

**[26] Product School - Product Vision: How to Create One for Success.** vendor.
**fetched-and-verified.**
`https://productschool.com/blog/product-strategy/product-vision`
Supports: the CPO/VP Product ownership position; vision stability relative to strategy; the disconnection
failure mode.
Quotable: "The CPO, VP of Product, or someone in Product Leadership is responsible for defining the Product
Vision and communicating it."; "It should remain stable. Product strategy and roadmaps can change to address
market and business developments, whereas the Product Vision is more stable."; "Teams end up focused on
shipping tickets and lose sight of why they're building what they're building."; "It's common to see the
frontlines disconnected from product vision, especially in large companies."; "For very large companies like
Amazon and Google, different products will have distinct visions."
Contested/time-bound: **no author or date visible.** Product School sells training. "It's common" is a
frequency claim with no cited study behind it.

### The skeptical camp, and the evidence question

**[27] Paul Sweeney (Sense Labs) - Episode 12 of 33: Meaningless Abstractions.** practitioner.
**fetched-and-verified (no verbatim quotes carried).**
`https://senselabs.substack.com/p/episode-12-of-33-meaningless-abstractions`
Supports: the strongest form of the skeptical position - that vision and values statements function as
performance rather than guidance.
Quotable: **none carried.** No passage was extracted cleanly enough to quote safely.
Contested/time-bound: the argument targets **corporate** vision and values, not product vision specifically.
It is polemic, not study. The Saint-Exupery caution recorded in this log came from this dimension's research
and is treated as a reason for omission, not as a citable claim.

**[28] Scrum Alliance - Crafting an Effective Product Vision Statement.** practitioner.
**fetched-and-verified.**
`https://resources.scrumalliance.org/Article/write-product-vision-statement`
Supports: the synthesis position; a hypothesis-shaped vision format.
Quotable: "A product vision statement should be clear, inspiring, and purpose-driven, whereas this example
falls short."
Contested/time-bound: **no individual author named.** The "We believe that by doing X for customer Y, we'll
create outcome Z" format is presented without attribution; it resembles Lean Startup language but is not
attributed here to Ries or anyone else, and this bundle does not attribute it either.

**[29] Bart and Baetz (1998) - The Relationship Between Mission Statements and Firm Performance: An
Exploratory Study, *Journal of Management Studies*.** primary. **url-confirmed-not-read (HTTP 402).**
`https://onlinelibrary.wiley.com/doi/abs/10.1111/1467-6486.00121`
Supports: **that the best-known empirical study in this area exists, is about mission statements at the
organisational level, and was not read.**
Quotable: **none.** The paper was not read.
Contested/time-bound: **this is the most important negative result in the bundle.** Search summaries describe
136 large Canadian organisations and a selective association between mission-statement characteristics and
performance - weaker than the causal claim practitioners make when citing it. Published 1998; the
organisational context differs from modern product teams. **Do not quote or characterise its findings
further.**

### Production, ownership and lifecycle

**[30] Natalie Forman - 4 workshop exercises to facilitate defining a product vision.** practitioner.
**fetched-and-verified.**
`https://natalieforman.com/product-vision-exercises/`
Supports: a concrete workshop format; dot voting; four named exercise types.
Quotable: "Our workshops consisted of 6-8 departments executives and were tailored for a media publication
site."; "Using dot stickers, ask the participants to vote for one sticky in each blank that they think fits
best."; "Create consensus around a working product vision statement to return to during stakeholder
discussions."
Contested/time-bound: **no date visible.** One practitioner's approach at one company. The 6-8 figure is a
single case observation, not a recommended norm.

**[31] Robbin Schuurman (The Value Maximizers) - 10 Tips for Product Owners on the Product Vision.**
practitioner. **fetched-and-verified.**
`https://medium.com/the-value-maximizers/10-tips-for-product-owners-on-the-product-vision-7e033bde6b09`
Supports: the Scrum ownership position; iterative development of a vision; pivot triggers.
Quotable: "Don't be afraid to pivot!"; "your heart should start beating faster about it, you should be
passioned about the vision"
Contested/time-bound: published 2017-11-15. Scrum-centric; conflicts with [26] on ownership and sits in
tension with the stability guidance. Its Facebook/Post-it/Netflix pivot claims were **not** verified.

**[32] Pendo - Why Working Backwards Benefits Product Teams.** vendor. **fetched-and-verified.**
`https://www.pendo.io/pendo-blog/why-working-backwards-benefits-product-teams/`
Supports: the mechanics of the working-backwards review, including the silent-reading ritual.
Quotable: "Working Backwards documents are a six-page narrative memo"; "Relevant stakeholders then attend a
document review, where they spend the first 20-30 minutes reading the document silently as a group"; "Jeff
Bezos's famous Working Backwards process for new product development at Amazon."
Contested/time-bound: **no date visible.** Pendo sells analytics. The Bezos attribution is secondhand; **no
page read documented who inside Amazon originated the method or when.** Different sources give different
lengths for the memo.

**[33] airfocus - What Is Product Vision (glossary entry).** vendor. **fetched-and-verified.**
`https://airfocus.com/glossary/what-is-product-vision/`
Supports: PO ownership with collaborative creation; rewrite triggers; continuous communication.
Quotable: "While the product owner should take ownership of the vision statement, it's not solely up to them
to create it."; "You may also need to return to your product vision board, template, or statement as the
competitive landscape changes or as your users' needs evolve."; "A company vision describes the goals, scope
and the future of the company while the product vision focuses more on serving as a guide for the
stakeholders."; "Product owners need to constantly communicate the product vision to stakeholders, teammates,
and users. Keeping the vision front and center fixes everybody's eyes on the end target."
Contested/time-bound: **no author or date visible.** Vendor glossary; definitional, not research-based.

**[34] ProductPlan - Why the Most Forward-Thinking Product Teams Work Backwards.** vendor.
**fetched-and-verified.**
`https://www.productplan.com/learn/product-teams-working-backwards`
Supports: the press-release method; **and the useful observation that the method has more than one lineage**.
Quotable: "Amazon starts every project with the product manager authoring a press release articulating the
current problem."; "Iterating on a press release is a lot quicker and less expensive than iterating on the
product itself."
Contested/time-bound: **no author or date visible.** The second quote is attributed in the article to Ian
McAllister, described as an Amazon PM; **that attribution was not verified.** The article also credits
FranklinCovey's "Begin with the end in mind" as a precursor, which undercuts any clean "Amazon invented this"
claim.

### Reader summaries of *Inspired* - read, recorded, and deliberately not quoted

**[35] Manas J. Saloi - Inspired by Marty Cagan (book notes).** practitioner (third-party summary).
**fetched-and-verified (the summary page only; the book was not read).**
`https://manassaloi.com/booksummaries/2021/01/12/inspired-cagan.html`
Supports: corroboration that Cagan's book treats vision as narrative/storyboard/prototype rather than
specification, and that it uses a leap-of-faith framing.
Quotable: **none carried into the bundle by deliberate policy.** The page's quotes are attributed to a book
that was not read and may be paraphrase.
Contested/time-bound: a reader summary. Recorded here so that a future reader knows the material was seen and
consciously excluded, rather than missed.

**[36] Ravi Kumar Sapata (LinkedIn) - Marty Cagan on Product Vision and Strategy, Inspired 2.**
practitioner (third-party summary). **fetched-and-verified (the summary page only; the book was not read).**
`https://www.linkedin.com/pulse/marty-cagan-product-vision-strategy-inspired-2-ravi-kumar-sapata`
Supports: corroboration of the 2-5 year horizon and of the "stubborn on vision" principle being presented as
Cagan's.
Quotable: **none carried into the bundle by deliberate policy**, same reason as [35].
Contested/time-bound: a reader summary, and one that presents the "stubborn" line as Cagan's own principle
where [3] shows Cagan quoting it and crediting Bezos. A good illustration of how attribution drifts.

---

## Second pass: sources gathered to close named gaps

The first pass left five gaps and named them. A second five-dimension fan-out went after each. **Two of its
results changed the bundle rather than decorating it:** the "no evidence exists" conclusion was wrong (see
fact 7), and Bezos became quotable from a primary source (fact 4).

### Standards and frameworks - the tier the bundle was missing

Every comparable bundle in this library has a standards-tier source. This one had none, so the first job was
to find out whether any framework defines a product vision at all. **The negatives are the finding.**

**[37] The Scrum Guide (November 2020).** standards. **fetched-and-verified.**
`https://scrumguides.org/scrum-guide.html`
Supports: **a confirmed negative.** The word "vision" does not appear anywhere in the 2020 Scrum Guide. The
nearest concept is the **Product Goal**.
Quotable: none carried; the finding is an absence.
Contested/time-bound: the 2017 edition was also checked as a PDF [38] with the same result, though PDF text
extraction was partial, so that one is high-confidence rather than byte-verified.

**[38] The Scrum Guide (2017 edition, PDF).** standards. **fetched-and-verified.**
`https://scrumguides.org/docs/scrumguide/v2017/2017-Scrum-Guide-US.pdf`
Supports: the same negative one edition earlier, so this is not a 2020 removal.
Quotable: none.
Contested/time-bound: compressed-stream extraction was limited; treat as high-confidence, not absolute.

**[39] The Nexus Guide (January 2021).** standards. **fetched-and-verified.**
`https://scrumorg-website-prod.s3.amazonaws.com/drupal/2021-01/NexusGuide%202021_0.pdf`
Supports: **the strongest negative in the set**, because the full 10-page PDF was read directly rather than
through a summarizer. "Vision" appears nowhere. Nexus defines three artifacts, none of them a vision.
Quotable: none; the finding is an absence.
Contested/time-bound: January 2021 edition. **This is the only negative in the set verified by reading the
full PDF directly** rather than through a summarizing fetch, which is why it carries the most weight. A later
revision could add a vision artifact; the claim is about this edition.

**[40] The Agile Manifesto and its twelve principles.** standards. **fetched-and-verified.**
`https://agilemanifesto.org/`
Supports: another confirmed negative. "Vision" appears on neither the values page nor the principles page.
Quotable: none; the finding is an absence.
Contested/time-bound: both the four-value statement and the twelve principles pages were checked. Unlike a
framework version, this negative is durable: the manifesto has stood unrevised since 2001.

**[41] SAFe - Vision.** standards. **fetched-and-verified.**
`https://framework.scaledagile.com/vision/`
Supports: **the one clear positive.** SAFe defines Vision as an explicit artifact and describes what it is,
how it is expressed, and how it creates alignment.
Quotable, **with the caveat below**: "A vision is a clear and motivating description of the future intended to
engage team members while setting limits and context for what they are creating."
Contested/time-bound: **retrieval caveat that applies to [41] and [42].** The fetch pipeline passes page
content through a summarizing model before returning it. These strings were returned identically across two
independent fetches, which raises confidence, but **character-exactness is not guaranteed**. The companion
therefore paraphrases SAFe rather than quoting it, and this log records why. Page last updated 2024-02-25;
the version (6.0) was inferred from an image path on a related page, not from a version string, so it is not
asserted in the bundle.

**[42] The Scrum at Scale Guide (version 2.1, February 2022).** standards. **fetched-and-verified.**
`https://www.scrumatscale.com/scrum-at-scale-guide-online/`
Supports: a second positive. Defines "Strategic Vision" as a named component of the Product Owner Cycle, and
makes setting it a Chief Product Owner responsibility.
Quotable: subject to the same summarizer caveat as [41]; paraphrased in the companion rather than quoted.
Contested/time-bound: version 2.1, February 2022. The quoted strings were returned identically across two
independent fetches, which raises confidence without guaranteeing character-exactness.

**[43] LeSS - Product Owner.** standards. **fetched-and-verified.**
`https://less.works/less/framework/product-owner.html`
Supports: a qualified negative. LeSS defines no vision artifact; "product vision" appears once, in a passage
describing what *traditional* (non-LeSS) product management does.
Quotable: **none carried.** The single occurrence sits inside a sentence about what traditional product
management does, so quoting it as a LeSS definition would invert its meaning.
Contested/time-bound: same summarizer caveat as [41].

**[44] PMBOK Guide 7th edition.** standards. **url-confirmed-not-read.**
`https://www.pmi.org/pmbok-guide-standards/foundational/PMBOK`
Supports: nothing. Every PMI URL attempted returned HTTP 403. **Whether PMBOK 7's artifact taxonomy names a
vision statement is unverified**, and the bundle says so rather than guessing.
Quotable: **none.** Nothing was read.
Contested/time-bound: **unverified in both directions, which is not the same as a negative.** PMBOK 7 does
carry an artifacts taxonomy, so a vision statement may well be in it. The bundle reports this as unknown and
never as "PMBOK does not define one".

**[45] BABOK Guide v3 (IIBA).** standards. **url-confirmed-not-read.**
`https://www.iiba.org/standards-and-resources/babok/`
Supports: nothing beyond the current version being v3. The page served marketing copy, not contents.
Quotable: **none.** Nothing was read.
Contested/time-bound: the guide is behind membership. Unknown rather than absent, on the same reasoning
as [44].

**[46] ISO/IEC/IEEE 29148 (requirements engineering).** standards. **not-retrieved.**
`https://www.iso.org/standard/72089.html`
Supports: nothing. ISO returned 403 and the IEEE URLs 404. Whether its ConOps or StRS document types are
vision analogues is **unknown**.
Quotable: **none.** Nothing was read.
Contested/time-bound: paywalled at both ISO and IEEE. 29148 **does** define Concept of Operations and
Stakeholder Requirements document types, so the live question is whether either functions as a vision
analogue. That question is open, not answered in the negative.

### The empirical evidence base

**Retrieval note governing [47], [48] and [49]:** all three were reached through the OpenAlex API, which
reconstructs an abstract from a stored word-position index rather than serving original text. Two of the
three reconstructions contain visible grammatical artifacts, which demonstrates the pipeline is lossy.
**No verbatim quotation is carried from any of them.** Designs, samples and findings below are abstract-level
metadata, and are labelled as such wherever the companion uses them.

**[47] Baum, Locke and Kirkpatrick (1998), "A longitudinal study of the relation of vision and vision
communication to venture growth in entrepreneurial firms", *Journal of Applied Psychology*.** academic.
**url-confirmed-not-read (abstract metadata via OpenAlex; paper not read).**
`https://doi.org/10.1037/0021-9010.83.1.43`
Supports: **the most directly relevant study that exists.** Longitudinal, 183 entrepreneur-CEO and employee
pairs, visions assessed against seven literature-derived attributes, structural equation modelling, outcome
is venture growth. Reported finding: vision content affects subsequent growth both directly and through
verbal and written communication.
Quotable: **none.** The reconstructed abstract is visibly garbled in place.
Contested/time-bound: **one industry only**, which the abstract itself states as a limitation. Longitudinal
but not experimental, so founders who articulate a vision may differ from those who do not on unmeasured
variables. The outcome is venture growth, **not product outcomes**.

**[48] Kirkpatrick and Locke (1996), "Direct and indirect effects of three core charismatic leadership
components on performance and attitudes", *Journal of Applied Psychology*.** academic.
**url-confirmed-not-read (abstract metadata via OpenAlex; paper not read).**
`https://doi.org/10.1037/0021-9010.81.1.36`
Supports: the only causal evidence in the set, and **a result that cuts against the usual telling**. Lab
experiment, 282 upper-level business students, simulated production task. Reported finding: high-quality
vision **weakly** affected performance but **strongly** affected attitudes, while vision *implementation*
(concrete task guidance) was the stronger driver of performance. The path ran through self-set goals and
self-efficacy.
Quotable: **none** (reconstruction artifacts present).
Contested/time-bound: students on a simulated task have very different motivation structures from product
teams. Causality holds inside the lab; ecological validity is the open question.

**[49] Carton, Murphy and Clark (2014), "A (Blurry) Vision of the Future: How Leader Rhetoric about Ultimate
Goals Influences Performance", *Academy of Management Journal*.** academic.
**url-confirmed-not-read (abstract metadata via OpenAlex; paper not read).**
`https://doi.org/10.5465/amj.2012.0101`
Supports: **the most actionable finding in the bundle.** Archival study of 151 hospitals plus an experiment
with 62 groups of full-time employees. Reported finding: much vision **imagery** combined with **few** values
improves performance via shared understanding and coordination, and leaders in practice tend to do the
inverse, under-using imagery and over-using value-laden rhetoric.
Quotable: **none.** The source agent marked this one fetched-and-verified, but its own note scopes that to
the API data rather than the paper, and the strings came through the same reconstruction pipeline as [47] and
[48]. Downgraded here deliberately.
Contested/time-bound: studies leader **rhetoric**, not written vision documents. The hospital half is
correlational; only the 62-group experiment is causal.

### Attribution verdicts

**[50] Amazon, 2020 Letter to Shareholders (Jeff Bezos's final letter as CEO).** primary.
**fetched-and-verified.**
`https://www.aboutamazon.com/news/company-news/2020-letter-to-shareholders`
Supports: **the one attribution the second pass upgraded.** A primary, quotable Bezos statement of the idea
behind the circulating aphorism.
Quotable: "On the details, we at Amazon are always flexible, but on matters of vision we are stubborn and
relentless."
Contested/time-bound: **this is not the circulating aphorism.** The 2016, 2017, 2018, 2019 and 2021 letters
were each fetched and checked and do not contain the phrase; letters before 2016 were inaccessible. The
condensed forms in circulation remain of unverified provenance.

**[51] Working Backwards LLC, About.** practitioner. **fetched-and-verified.**
`https://www.workingbackwards.com/about`
Supports: a confirmed negative from the best-placed source. Bryar and Carr, former Amazon VPs, attribute the
PR/FAQ and working-backwards practice to Amazon **collectively** and name no originator.
Quotable: none carried.
Contested/time-bound: **an About page is promotional copy, and the distinction matters here.** This is good
evidence that the two people best placed to name an originator do not *claim* one, and weak evidence about
what actually happened inside Amazon. Their book was not read. Read this as "no one claims it", not as
"no one did it".

**[52] Quote Investigator, "Teach Them to Yearn for the Vast and Endless Sea".** reference.
**fetched-and-verified.**
`https://quoteinvestigator.com/2015/08/25/sea/`
Supports: **a definitive refutation.** The modern English ship quote appears in no published Saint-Exupery
work. The nearest real passage is *Citadelle*, section LXXV, thematically related and wholly different in
wording. Earliest traceable English instance: a November 1999 Usenet post, where it is already misattributed.
Quotable: the circulating misattributed form, quoted here **only** as the object of the refutation: "If you
want to build a ship, don't drum up people together to collect wood and don't assign them tasks and work, but
rather teach them to long for the endless immensity of the sea."
Contested/time-bound: page last updated 2025-01-16. The finding is that the modern phrasing is a paraphrase of
unknown authorship, not that Saint-Exupery wrote nothing on the theme.

---

## Claims flagged contested or time-bound

1. **That Collins and Porras supply the product vision framework.** They wrote about companies [11]. The
   BHAG/core-ideology/envisioned-future vocabulary was borrowed into product work by others. **Additionally,
   the usual citation order is reversed**: the book is 1994 [11], the HBR article is 1996 [10].
2. **That Moore's positioning statement comes from *Crossing the Chasm* and is a vision template.** The
   template was **not verified verbatim in any page read**, and no page named a chapter or edition [13][24].
   Separately, positioning and vision answer different questions. The bundle does not reproduce the template
   as canon and does not attribute it.
3. **"Be stubborn on the vision, and flexible on the details."** Cagan quotes it and credits Bezos [3]; other
   sources attribute it to Bezos without sourcing [20]; a summary presents it as Cagan's own [36]. **No
   primary Bezos source was found.** Quote it only as Cagan quoting it, or not at all.
4. **That the Amazon PR/FAQ is a vision format, and that a named person created it.** It is a
   product-definition practice for a specific launch [12][32][34]; no source read names an originator or a
   date; and ProductPlan notes an earlier lineage in FranklinCovey [34].
5. **That vision or mission statements improve performance.** The best-known study [29] is paywalled, was not
   read, concerns organisational mission statements, and is summarised as a selective association. **No study
   of product-level vision documents and product outcomes was found.**
6. **The 2-5 year horizon.** Cagan's own figure [2], echoed widely, with no evidence offered. Pichler's floor
   of five years [8] partly contradicts it. Both are judgment.
7. **"Ambitious yet achievable."** Near-universal across sources [20][23], but it reflects what practitioners
   believe rather than any measured comparison against moon-shot visions.
8. **Whether inspiration or structure produces better visions.** Cagan argues for inspiration and against
   canvases [1][2]; Pichler ships a canvas [5][6]. **No empirical comparison exists.** This bundle sides with
   neither and applies the decision-utility test [17] instead.
9. **Who owns the vision.** Three mutually inconsistent positions: Product Owner [31][33], CPO/VP Product
   [26], and one-vision-per-organisation [1]. No research resolves it.
10. **Whether a vision is worth writing for a small team.** **No source read addresses this.** The
    practitioner literature assumes medium-to-large organisations. The bundle says so rather than
    extrapolating.
11. **Frequency and prevalence claims generally.** No source read cited a survey of team practice. Every
    "most teams" statement in this literature, including Cagan's [1] and Product School's [26], is
    observation. The bundle reproduces none of them as fact.
12. **Pichler's quarterly review cadence** [6] is a rule of thumb for his own board, not an industry norm.
13. **Vision versus positioning statement.** **No source read draws this boundary.** The bundle draws it from
    first principles and labels it as the bundle's own reasoning.

---

## Notes for the companion

- **Open with the template paradox, do not bury it.** Cagan's rejection of canvases [2] is the most
  interesting fact about this document type and the most useful thing a reader can know before filling
  anything in. The companion states the disagreement, names both camps, and then says what the bundle did
  about it: rather than pick a side, it ships three formats (ADR 0028), so a reader who finds the canvas
  reductive can reach for the narrative without leaving the library. The decision-utility test [17] is the
  standard that applies across all three.
- **Lead the failure modes with disuse** [15], not with prose quality. Then borrowed grandeur [15], then
  aspirational fluff [17], then roadmap-in-disguise, then per-team fragmentation [1].
- **Draw the boundaries in order of how much trouble they cause**: mission (contested, and the most common
  confusion [1]), strategy (settled [3][14]), north star metric (two meanings [14]), company vision (scope,
  not kind [18][14]), positioning statement (a boundary the field has not drawn).
- **Say the evidence base is thin.** [29] is the honest anchor, and its main use is to stop the bundle
  claiming a benefit nobody has measured.
- **Note the mission/vision reversal risk outside product management.** Every product source read treats
  vision as future-facing; adjacent management writing sometimes uses the terms the other way round. A reader
  arriving from a non-product background needs the warning.
- **Do not use** the Saint-Exupery ship quote, the Moore template as canon, a named PR/FAQ inventor, or any
  Cagan quote sourced through [35] or [36].
