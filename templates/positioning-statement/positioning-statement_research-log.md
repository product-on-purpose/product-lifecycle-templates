# positioning-statement: research log

Research conducted 2026-10-20, building on admission sweep 6 (2026-10-14), the sitting follow-up of 2026-10-15
(`_local/research/2026-10-15_sitting-followup/positioning.json`, gitignored), and the approved spec
(`docs/internal/tier2-specs.md:6162-6528`). The build's six-dimension fan-out covered the canon, meaning the
formula, its published field sets and its disputed origin; April Dunford's components, process and critique; who
owns the statement; its boundaries with vision, strategy, messaging and the battlecard, and when it is revisited;
the library's own neighbours and the Acme Analytics chain; and the standing gap question. **59 sources are
recorded below: 57 fetched-and-verified, one confirmed to exist but not read, and one not retrieved.** The 57 are
25 primary, 16 practitioner, 13 vendor, 2 academic and 1 reference. Twenty-four of the 25 primary sources are
Dunford's own posts and pages; the other is Christopher Lochhead's excerpt [58]. The page confirmed but not read is
Product Marketing Alliance's messaging-framework template [50], a lead-capture shell. The source not retrieved is
Dunford's book, Obviously Awesome, in either edition [33]. One fetched source, an AI-agent toolkit's template on
the npm registry [54], is listed because it was consulted; it carries no quotation and supports nothing here.

**Every quotation in this log was checked against the source's raw text**, not against the summary a retrieval
tool returns. Five research dimensions returned on the first run. The sixth, on Dunford, failed on malformed JSON
and was re-run once, one model tier up, writing its result to a file. Together they returned 303 quotations. 288
passed as returned and 15 failed: 13 outright, and 2 flagged as extraction artifacts. Seven of the 15 came from
the toolkit template [54], which was dropped with all eight of its quotations. Three long quotations were dropped:
one Dunford sentence [21], one Sharebird answer [43], and the RUP template's formula [44]. Ten Quotable lines were
rescued by re-quoting from raw text: one short re-quote stands for the Dunford sentence [21], four stand for the
Sharebird answer [43], and five keep the words the agents returned (Martech Zone [42], two Dunford list lines
[23], and the two artifact flags on [48] and [56]). Before that check, two cache bodies, koji.so [56] and Lumen
Learning [59], were found stale and replaced with raw fetches. Two Dunford quotations, the customer-positioning
sentence [23] and the six-month check-in [26], passed against the cache but failed a fresh fetch. The main loop
confirmed that both are spacing artifacts around a dash, and the text is on the live page. `sources-report.txt`
records 59 entries, 297 quotations kept, 3 split and 3 dropped. **297 Quotable lines remain.** Quotable lines
render the sources' long dashes as hyphens; copy them as they stand.

---

## What the checks caught, and what was not read

**This log does not carry every span the spec quotes, unlike the `trade-study` log.** Five quotations in the spec
are not Quotable lines here, so no drafting stage may quote them from this log:

- The Starr Conspiracy's "1 to 3 sentences" (`docs/internal/tier2-specs.md:6374`).
- The Starr Conspiracy's messaging-framework cadence, "two-to-three years for brand and category, quarterly for
  audience and product" (`:6295`).
- Yesware's "A positioning statement requires input from several different teams" (`:6422-6423`).
- Product Marketing Alliance's "share it with stakeholders across the organization" (`:6424-6425`).
- Poorvi Shrivastav's continuation, "It is more focused on the present, defining the target audience"
  (`:6343-6344`). It sat inside a longer quotation that failed and was split, and the clause did not survive.

The RUP template's slot-by-slot formula [44] was also dropped. RUP can be cited for its section names and its
bracketed instruction, not for its slots. Every other external span the spec quotes is a Quotable line here,
including Devika Nair's full, untruncated sentence [39].

**The Sharebird attribution is sound.** The ownership dimension reported that Mike Flouton and Poorvi Shrivastav
do not appear on the Sharebird page it read. That page is a different question, [39], which carries Nair's
answer. Both practitioners are on [43], read in its raw cache body for this log: Flouton under Boxford Capital,
Shrivastav under Meta. The spec's attribution stands (`docs/internal/tier2-specs.md:6339-6344`). Both answers are
truncated on the page behind a read-more control, so only their opening sentences were read.

**The gap-question dimension rested partly on [54], which now supports nothing.** Its write-up drew per-claim
proof points, an exclusions list, named approver roles, an internal rollout sequence and five repositioning
triggers from that template. Seven of the template's eight quotations failed a fresh fetch. This head reports a
gap lead only where a surviving source carries it, and drops every lead that rested on [54] alone. The same
dimension's name for Lumen's formula and its list of Koji's revisit triggers are not Quotable lines, and neither
is used.

**The Goodreads source is not about Moore.** [6] is one reader's highlights of Al Ries and Jack Trout's
Positioning: The Battle for Your Mind, and it carries no slot-based template [6]. The canon dimension reports that
the fetched highlights run only to a 34 percent reading-progress marker. That conflicts with the spec's account of
a Goodreads note carrying a matching template at a 59 percent marker (`docs/internal/tier2-specs.md:6221-6223`).
Whether a second Goodreads note exists, for Crossing the Chasm, is not settled by this pass.

**Product Marketing Alliance's field set was not re-confirmed.** The spec describes a one-page, five-row `.docx`
behind a free-account signup, from a browser observation on 2026-10-15 (`docs/internal/tier2-specs.md:6208`).
This pass's raw text shows only the gate: "Become a member to see the rest." [5]. No PMA slot may be quoted.

**What was assigned and not read, or read only in part:**

- **Geoffrey Moore's Crossing the Chasm.** Not retrieved, and it has no entry below. No accessible preview pinned
  the template to an edition, chapter or page. The page-186 citation the follow-up found resurfaced only as a
  search summary, not as text this pass owns.
- **Ries and Trout's book itself.** Not read; only the highlights page [6].
- **Obviously Awesome, both editions, and Sales Pitch** [33]. Not read, and no preview read. Dunford's posts
  establish that the first edition had five components and ten steps [23], [31], and that the second edition,
  shipped in February 2026, restructured them [23], [31], [32]. The first edition's ten steps were not found in
  her own words.
- **Dunford's templates.** The 2019 template on [8] exists only as an image. Its field names were transcribed by
  eye, not raw-checked, and may not be quoted. Her current templates are a 12-page workbook given to newsletter
  subscribers [12]; an updated set was still in preparation in 2026 [29], [32].
- **Dunford's promised post on assembling the positioning team** [23]. The Dunford dimension did not find it in her
  Substack archive. Her Lenny's Newsletter guest post [29] and her podcast episodes were not read.
- **Gated or partial pages.** HubSpot's bonus template download [2] was not read. Ibrahim Bashir's post [57] was
  read as a free preview only.
- **Pragmatic Institute's own framework.** Its FrameWork PDF was not read. Its workshop page [40] holds no
  sentence on ownership and none on section order. A secondary summary claiming that the framework gives
  positioning to a Product Line Manager returned HTTP 404 and is not used. An archived Applied Frameworks page,
  whose search summary suggested that product management owns positioning while marketing communications owns
  messaging, failed to load. It is the one lead toward the library's ownership default, and it is unverified.
- **Referenced but not fetched:** a Kompyte post on messaging check-ins, a Mind the Product summary of Dunford's
  six-month check-in (now superseded by her own words [26]), a Sharebird answer on messaging cadence, and a vendor
  blog on review tiers. Two pages, echogravity.com and marketful.com, were blocked by bot checks. None is used.
- **An AI-agent skill page** on SkillsCat was read by the ownership dimension, holds no ownership statement, and
  has no entry below.

---

## Findings

### The formula and its field sets

**Five sources carry the slot-based form in readable text**: MIT [1], HubSpot [2], eCornell [3], Yesware [4], and
the classic form, as Heinz Marketing's summary of Dunford's first edition renders it [9]. Product
Marketing Alliance's slots are gated [5]. The RUP template names a "Product Position Statement" subsection [44],
but its slots were dropped (see above). The slots, source by source:

| Slot | MIT [1] | HubSpot [2] | eCornell [3] | Yesware [4] | Classic form, via Heinz [9] |
|---|---|---|---|---|---|
| Target | "[target customer]" | "[your target market]" | "[insert Target Market]" | "[target market]" | "[target buyers]" |
| Need | "[a compelling reason to buy]" | "[target market need]" | none | "[target market need]" | none |
| Product | "[product name]" | "[your brand name]" | "[insert Brand]" | "[brand name]" | "[your offering]" |
| Category | "[product category]" | none | "[insert Frame of Reference]" | "[market category]" | "[market category]" |
| Benefit | "[these key benefits]" | merged with differentiation | merged with differentiation | "[end benefit]", plus the merged slot below | "[main benefits]" |
| Named alternative | "[the main competitor]" | none | none in the formula | none | "[competitor]" |
| Differentiation | "[provides these key differentiation points]" | "[main benefit that differentiates your offering from competitors]" | "[insert Point of Differentiation]" | "[point of difference/primary benefit differentiating you from competitors]" | none; it names "[competitor's benefits]" |
| Reason to believe | none | "[reason why target market should believe your differentiation statement.]" | "[insert Reason to Believe]" | "[reason to believe]" | none |

**Every form carries a target, a product and a benefit.** Three of the five merge the benefit with the
differentiation: HubSpot's single slot [2], eCornell's point of differentiation, which "describes how your brand
or product benefits customers in ways that set you apart from your competitors" [3], and Yesware's combined slot
[4]. Four forms carry a category; HubSpot has none [2]. eCornell's frame of reference "is the segment or category
in which your company competes" [3]. Three carry a need: MIT, HubSpot and Yesware. Three carry a reason to
believe: HubSpot, eCornell and Yesware. MIT and the classic form have none.

**Only two forms carry a named-alternative slot**: MIT's "Unlike [the main competitor]," [1] and the classic
form's "unlike [competitor]" [9]. eCornell's formula has none, though its worked Amazon example reads "Unlike
traditional book retailers" [3]. Only Yesware adds an outcome clause, "so they can [end benefit]" [4]. eCornell
allows the wording to vary but not the content: "it must contain the five main components in brackets above" [3].

**The spec's six components are the union of these sets, not their intersection.** Target, need, category,
benefit, named alternative and differentiation match MIT's six slots [1], as the spec records
(`docs/internal/tier2-specs.md:6385-6392`). The named alternative, which the spec treats as positioning's core, is a
formula slot in only two of the five. Its stronger support is Dunford's first component, competitive alternatives
[7], [10], and her account of what positioning describes: "It describes why a specific type of customer should
choose your product over any other alternative way of solving the problem" [11].

**The spec's because-clause departs from every published one.** The spec says its labels are the library's own
wording (`docs/internal/tier2-specs.md:6401`), and that stands; the clause's content is the issue. The Statement
row reads "unlike [named alternative], because [differentiation]" (`:6401`). In the three forms with a
because-clause, the clause carries the reason to believe, not the differentiation [2], [3], [4]. MIT gives the
differentiation its own closing slot, "The [product name] [provides these key differentiation points]." [1]. See
the companion notes.

**Length.** MIT: "A product positioning statement forces you to use a one page format to summarize everything that
matters for your product." [1]. HubSpot: "Aim for no more than three to five sentences, if possible." [2]. Yesware:
"Positioning statements should be relatively short (3 - 5 sentences, at the most)." [4]. eCornell calls it "a
concise description of your target market" [3]. The Starr Conspiracy describes "A single internal statement that
defines the target customer, the category, the key benefit, and the primary differentiator." [46]. All of this
fits one lean size.

**Audience and use.** Every source that names a reader names an internal one. HubSpot: "your positioning
statement isn't public-facing" [2], although "Investors, new hires, and external agencies who work closely with
your businesses will need to use this document, too." [2]. eCornell: "your positioning statement is an internal
tool." [3], and "Every product and marketing decision you make regarding your brand has to align with and support
your positioning statement." [3]. Yesware: "typically meant to be internal and are used by marketing and sales
teams" [4]. Product Marketing Alliance: "an internal resource" [5] and "just an internal document" [47].

**The origin.** The canon dimension found no attribution to Moore, Ries or Trout on any admitting source's page;
the entries for HubSpot, eCornell and Yesware record it [2], [3], [4]. Ries and Trout's concept, in the highlights
read, is perceptual and carries no fields: "positioning is not what you do to a product. Positioning is what you do
to the mind of the prospect." [6]. Dunford dates the practice loosely and names no author: "Since the 1970's we've
been taught that "Positioning" is critical to our businesses" [13]. **No source in this log attributes the
formula to Moore.** The attribution's only footholds are the catalog row (`docs/internal/catalog.md:43`) and the
follow-up's blog citation to page 186 of the 3rd edition, which was never verified against the book
(`docs/internal/tier2-specs.md:6223-6224`). Admission does not lean on him (`:6225-6226`), and this research gives
no reason to strengthen the attribution.

### Dunford's components, process and critique

**Her definition.** "Positioning defines how your product is a leader at delivering something that a well-defined
set of customers cares a lot about." [7]. More plainly: "positioning defines what market you intend to win and
why you deserve to win it." [7].

**Her five components, in her order.** Her 2020 and 2021 posts list competitive alternatives, differentiated
features or capabilities, value for customers, target customer segmentation, and market category [7], [10]. Her
labels drift by year. In 2019 they were "competitive alternatives, unique capabilities, differentiated value,
target customers, market category" [17]. A 2026 post walks "Step 1 - Competitive Alternatives", "Step 2 - Distinct
Capabilities" and "Step 3 - Differentiated Value" [27]. Heinz's labels, including "Relevant Trends (Bonus)", are the
summary author's, not Dunford's [9]. Her own posts mention trends only as book content, "how you can take advantage
of trends" [10]. A bundle that names her components should quote one of her own lists and give its year.

**The components depend on each other, and the alternatives come first.** "Your differentiated features are only
"differentiated" when you compare them to competitive alternatives." [10]. "I had the realization that the
starting point had to be competitive alternatives." [10]. Her working question for that first component: "What
would a customer do if your offering didn't exist?" [18]. Her answer puts the status quo first: "To win business,
the first competitive alternative we need to beat is the status quo." [18]. The questions that follow
are "What do we have that the alternatives do not?" [10] and "So what for customers?" [10].

**Her process exists in three versions.** The 2019 blog exercise has five steps, from "Step 1: Let go of where you
came from" to "Step 5 - Choose your best market frame of reference" [8], and no competitive-alternatives step. The
first edition had "5 positioning components but 10 steps" [23]. The second edition has "Prep work (the decisions
and preparation you need before starting) - 5 core steps (matching the 5 positioning components) - Post work (how
to make your positioning real)" [23]. The prep work is four decisions, ending with "Which persona are you
positioning for?" [23]. Before launch, "what you're actually creating is a positioning thesis, not true
positioning." [23]. The 2019 version's opening step guards against a specific failure: "Weak positioning is usually
the result of hanging on to a "default" market position that is rooted in the history of the product idea." [8].

**Who is in the room.** "For smaller companies, the CEO needs to drive the effort (for bigger companies, it should
be whoever is ultimately responsible for the business the product is part of)." [30]. "Product, Marketing, and
Sales (plus often customer success and development) - need to be involved in creating the positioning." [30].
"The obvious way to fix this is to have sales involved in creating the positioning in the first place." [25]. A
2017 post makes the same point: "implementing it crosses every department in the company, not just marketing." [14].

**Her critique of the fill-in-the-blank statement**, in five posts over five years:

- 2017: "The positioning statement: candidate for most useless business tool ever" [13]. "Somewhere along the way
  we have confused teaching people HOW TO DO positioning with teaching people HOW TO WRITE DOWN positioning." [13].
- 2019: a section headed "The Positioning Statement is Harmful and You Should Never Do One" [8]. Its three reasons:
  the exercise "assumes great positioning is magically locked inside your head" [8]; its output "cannot be easily
  shared, understood or remembered by the teams who need to use it." [8]; and it "gives you the false sense that
  you are "done" doing positioning" [8].
- 2019: "a laughably vague fill in the blanks exercise" [17].
- 2020: "the best way I can describe it is as a sort of "Mad Libs" fill in the blanks exercise for marketing
  folks." [7]. The exercise is "not only pointless but potentially dangerous" because "the exercise assumes that
  there is only one answer for each of the blanks." [7].
- 2021: "How would this exercise help me understand that my "Microsoft Access Killer" was really an "Embeddable
  Database for Mobile Devices?" The answer is that it simply would not." [10].

**The qualifying sentences narrow the critique, and the bundle depends on them.** She grants the statement one
use: "The only valuable thing we can learn from the statement is that there are multiple components of
positioning. These are, in essence, the blanks of the positioning statement." [7]. The same 2019 post that says
never do one then says "Once you have all the pieces together, you will want to write it down." [8]. Her two
reasons: "1/ You have a record of the agreed upon positioning, in a form that makes it easy to understand why the
positioning is what it is." [8] and "2/ The document is dated so you can track when the positioning was last
reviewed." [8]. She keeps that record apart from messaging: "The positioning template should not be a way of
documenting your value proposition or approved messaging around features or value." [8].

**This library's reading, not her words:** her critique forbids filling the blanks from assumption, and it
forbids treating the sentence as the end of the work. It does not forbid a short, dated, internal record of
positioning reached by analysis and used as an input to messaging [7], [8], [13]. The bundle stands on the
record she endorses only if its components carry the analysis and its sentence is a summary of them.

### Ownership

**Product marketing owns it, in three sources.** Blackblot: "Product positioning statements are created by the
product marketer who belongs to the Product Marketing department." [34]. The same page says statements are
"irrelevant to the product planner (a role in Product Planning)" [34] and that "The MarCom Manager does not create
product positioning statements." [34]. Young Urban Project: "Both are strategic, but product positioning is
usually owned by the Product Marketing function." [35], and "Product marketing owns these pieces. And positioning
is their secret weapon." [35]. Douglas Karr, describing the Pragmatic Framework: "Product marketers’ work shines
in the Planning category. Here, activities like positioning, persona development, buyer experience mapping, and
use scenario planning come to life." [42]. He adds "A well-crafted positioning document aligns marketing, sales,
and product development around a single narrative." [42] and "Product marketers translate market data into
messaging frameworks that inform campaigns, content, sales enablement, and thought leadership." [42]. Karr is a
practitioner's account of that framework, not Pragmatic Institute's own text. Pragmatic's workshop page carries no
ownership sentence; it lists only the roles that benefit from its training [40].

**Product management shares it, in four.** Aha!'s guide: "Product positioning is a cross-functional exercise. It
typically involves product management and product marketing working closely together to define the core essence
of your product." [36]. Aha!'s blog: "Product positioning is a strategic exercise typically carried out by product
management and product marketing teams. Close collaboration is important - both groups have a unique point of view
on the marketplace, other solutions available, and how your own product fits in." [38]. Aha!'s template catalog
files "Product positioning templates" under "Strategy product management templates", apart from "Marketing
positioning templates" [37]. That split is structural; it says nothing about who drafts. Devika Nair (Director of
Product Management, Oracle), in full: "Product Management primarily partners with engineering. They are
responsible for what we build, and why we built it. Product Marketing is responsibile for how we position these
products to the customers. While product management is also responsible for the positioning, they are looking at
it as part of the vision and decision making." [39].

**A third shape, which neither camp names: the executive drives it and the functions build it together.** Dunford
puts the CEO, or the person responsible for the business, in charge, with product, marketing and sales creating
it [30]. "If the CEO isn't on board with the new positioning, it doesn't stick." [30]. "If they aren't involved in
creating it, it will be very hard to get their buy-in after the fact." [30]. After the positioning, "Marketing and
Sales (and often product) must build a sales pitch that reflects the positioning." [30], and "sales leadership
needs to drive rolling the pitch out to the sales team." [30]. She describes a revisit as "an opportunity to get
the executive team together and re-align itself with the business fundamentals." [22]. Her workshop "is designed
to help align your executive team around your best positioning and a sales pitch that accelerates revenue." [24].
An acquisition brings "folks from across marketing, sales, and product - from both sides of the acquisition -
together" [28]. "Great B2B positioning will die inside the company if it doesn't successfully make the jump from
marketing to sales." [25]. "Today Positioning needs to be embodied across the entire organization." [14]. The
product team's own stated role is narrower: it "might want to keep an eye on" phantom competitors "as a future
competitive threat" [18]. Adi Oran: "Positioning is a team sport." [53] and "Get marketing, product, sales,
customer success, and executives (especially the CEO) together in a room." [53]. Applied Frameworks: "if you can
get the execs to sign off on positioning, you can reduce your internal approvals dramatically." [55]. Dunford in
2017: "The process of Positioning can no longer be left to the marketing department along and is a
cross-functional effort" [15].

**Readers, not owners.** HubSpot calls it "an internal tools that help marketers appeal to their buyer personas"
[2], whose goal "is to align marketing efforts with a company's brand and value proposition." [2]. Yesware says
statements "are used by marketing and sales teams" [4]. Aha! says the resulting document "helps everyone in the
organization understand the real value you provide beyond features and functionality." [38]. The Institute of
Product Leadership's guide names no owner and calls positioning "a crucial component of any marketing plan" [41].

**No source supports the library's suggested default.** No Quotable line states that product management owns the
statement as product direction while product marketing drafts or co-writes it. Aha! describes joint work with no
division of tasks [36], [38]. Nair gives product marketing "how we position these products to the customers" and
gives product management a share "as part of the vision and decision making" [39]. That is a split, but it is not
the default's split. **Where the sources lean, they lean toward product marketing** [34], [35], [42]. No Quotable
line states that ownership varies by organization. Blackblot's "It all depends on the given situation." is about
how many statements are needed, not who owns them [34]. The closest is Dunford's: who drives the work depends on
company size [30]. The default therefore stays labelled as this library's reasoning, as the spec already labels it
(`docs/internal/tier2-specs.md:6330-6333`). ADR 0076 records that the default was accepted without the
maintainer's read
(`docs/internal/decisions/0076-positioning-statement-joins-strategy-docs-as-a-sixth-member.md:48-51`). The spec
counted two product-marketing sources (`docs/internal/tier2-specs.md:6305`); with Karr there are three.

### Boundaries with vision, strategy, messaging and the battlecard

**Versus vision: the present-versus-future line now has a primary source.** Mike Flouton: "Product vision is
long-term, aspirational, inspiring, speaks to a broad audience, and paints a picture of what could be in the
future." [43]. "A positioning statement, on the other hand, is much more present-day, marketing-oriented, and is
typically something that you'd write to position a feature, product, or capability towards a specific target
audience." [43]. Poorvi Shrivastav: "A product vision statement defines the long-term goal and direction of a
product." [43]. "It's where the product aims to be in the future, independent of the current state or
competition." [43]. "A positioning statement, on the other hand, outlines how a product will be perceived in the
market relative to competitors." [43]. Dunford draws the same line in three posts. "Positioning is firmly rooted
in the present. Positioning describes how your product wins business today in the market as it exists today and
is the foundation of your current sales pitch." [11]. "Our positioning today needs to reflect why a customer would
choose us over the other alternatives they might choose in the market right now, not why we believe we will be a
great choice in the future." [26]. "Customer positioning focuses on now and the immediate future" [23]. "It
describes why a specific type of customer should choose your product over any other alternative way of solving
the problem" [11].

**Customer positioning, not investor positioning.** "The methodology in Obviously Awesome is designed specifically
for customer positioning-not investor positioning, not employee positioning, not partner positioning." [23]. Read
in the raw text for this log, and not Quotable lines: [26] numbers its first B2B rule as separating the
longer-term vision from what is sold now, and its second as positioning for customers differing from positioning
for investors. [11] contrasts the investor pitch, which looks to the future, with the sales pitch, rooted in the
present.

**Against the line.** A RUP vision template nests a "Product Position Statement" under a "Positioning" heading
inside the Vision document [44]: "[Provide an overall statement summarizing at the highest level, the unique
position the product intends to fill in the marketplace. The following format may be used:]" [44]. It is a
software-engineering methodology artifact, which the spec weights below Sharebird
(`docs/internal/tier2-specs.md:6348-6351`). Dunford, in 2020, lists the vision among things downstream of
positioning: "messaging, a tag line, your vision, branding - these are all examples of things that happen after
positioning. Each of these things requires positioning as an input or the starting point." [7]. In the raw text the
list opens with storytelling. On this log's reading, the vision there sits among communications rather than as a
direction-setting document, but the post does not say so.

**Dunford on the chain: she supports strategy before positioning, and rejects a simple cascade.** "I don't see it
as quite that simple, particularly because our positioning will change with each step of our strategy." [11]. The
sentence before it, read in the raw text and not a Quotable line, names the view she rejects: a cascade in which
the vision leads to a strategy that then dictates positioning. Her alternative: "Positioning changes over time as
we follow our strategy on the journey to the vision. At each step, you will have different positioning." [11].
On this log's reading, **this supports third place over second**: positioning is set for the current stage of a
strategy, so it follows the strategy. **It also undercuts a static reading of the link**: one strategy carries
several positionings in sequence, and she rejects the idea that the strategy simply dictates one. Also on this
log's reading, Nair's "as part of the vision" [39] speaks to who holds the responsibility, not to document order,
so it is weaker evidence for second place than the spec's wording suggests
(`docs/internal/tier2-specs.md:6270-6277`). Dunford's 2020 list [7] cuts against any fixed order with the vision
first. No Quotable line places positioning relative to the North Star metric or OKRs.

**Versus strategy.** Dunford treats the choice of market frame as strategy: "It's not merely a marketing decision or
a messaging decision - it's a strategy decision." [19], and "the frame of reference we choose for that product will
change the entire trajectory of the business." [19]. "Positioning is closely tied to your overall business
strategy" [14]. "A change in positioning is a fundamental change in your business." [8]. CLIMB ties frequent
rewrites to an unfinished strategy: "If you find yourself rewriting your positioning statement every quarter, the
problem likely isn't the statement. It's that the underlying strategic choices haven't been made firmly enough."
[51]. The Starr Conspiracy: "Positioning is direction; messaging is tactical." [45]. Blackblot places positioning
far later, after requirements: "product positioning is created only after the PRD (Product Requirements Document)
is created by the Product Architect" [34]. No Quotable line states the positioning statement's place relative to a
product strategy document by name. Aha!'s positioning guide sits under its product-strategy guide's address [36].

**Versus messaging: every source that addresses it puts positioning first.** "Positioning is not the same thing as
messaging. It isn't a tag line." [7]. "Once you have your positioning figured out, this becomes a set of inputs to
your messaging." [8]. "I usually build a messaging document that references the positioning template." [8].
"Positioning is not the result of a story. Stories require positioning as an input." [16]. "The outcome of product
positioning is an internal document that informs external messaging" [36]. "A messaging framework translates that
positioning into specific language for different audiences and contexts." [45]. "A positioning statement is one
input." [46] and "Lock the positioning statement first." [46]. Product Marketing Alliance lists "Your positioning
statement - The starting point of your narrative" [47]. Atlassian's message house starts there: "Write down the
positioning statement that you put your blood, sweat, and tears into here." [49]. Dunford's later work puts a sales
pitch first among the downstream artifacts: the second edition covers "how best to create a sales pitch to test
positioning and then turn that positioning into messaging." [31]. The one source that blurs the line is
secondary, and it inverts her stance: "the positioning statement should be an integral part of marketing,
messaging, and iteration." [9].

**Versus the battlecard.** Downstream, and reinforcing: "Well-designed battlecards ensure reps are aligned on
product positioning, can confidently differentiate your offering, and reinforce messaging consistency." [48].

**Versus mission, tagline and value proposition.** "A positioning statement sits behind all of those, shaping what
they say and how they say it." [51]. "A tagline can change with a campaign." [51]. "Unlike a mission statement ,
your positioning statement isn't public-facing." [2].

### Revisit cadence and triggers

**The spec's premise is contradicted.** The spec says "No source read states a review cadence for the positioning
statement itself" and rests the `foundation` classification partly on that gap
(`docs/internal/tier2-specs.md:6285-6301`). Three sources in this log state a cadence for positioning, one of them
for the positioning statement by name, and a fourth asks for a dated record so reviews can be tracked.

**Cadences, verbatim:**

- Dunford, 2024: "When I was working in-house, we would have a positioning checkin every six months. We would also
  call an emergency check-in if something big happened (e.g., a new competitor in the space, an acquisition, a new
  big product release, etc.)." [26].
- Dunford, 2023: "Plan for this by having a regular (a couple of times a year) check-in to determine whether or
  not you need to make a positioning adjustment." [30].
- Lawson Abinanti, 2017: "It's a good idea to audit your positioning statement every 12 months." [52], and
  "Summertime is the best time to audit your positioning statement for effectiveness, and it's easy to do." [52].
- Dunford, 2019: "2/ The document is dated so you can track when the positioning was last reviewed." [8].
- Dunford, 2024, on process: "3/ We need to expect our positioning to change over time and have the processes in
  place to review and adjust our position." [26], and "A structured process is needed to do positioning because
  you will have to do it more than once." [26].

**Stability, verbatim:**

- CLIMB: "A positioning statement should stay stable for years, only shifting when your market, your competitive
  landscape, or your strategic direction fundamentally changes." [51]. "A positioning statement isn't permanent,
  but it shouldn't change often." [51]. "The goal is stability with occasional recalibration, not constant
  reinvention." [51].
- The Starr Conspiracy: "Positioning should be stable for years. Value props and campaign messaging shift with
  market conditions." [46], and a positioning statement "Rarely changes, so it provides long-term stability" [46].
- Product Marketing Alliance: "once you've established one it shouldn't be set in stone; you have to update and
  refresh it over time." [47].

**Change is expected, verbatim:**

- "Consumer products rarely shift positioning, where positioning shifts are expected and normal for B2B
  products." [26].
- "In tech companies, it's normal for our positioning to shift over time." [30]. "Your positioning might also
  change due to shifts in the competitive landscape or changes in customer behavior (often driven by economic
  forces)." [30].
- "Positioning will (and should) shift over time as features, markets, competitors shift." [15]. "Modern
  positioning is iterative, and is developed and refined over time by the company and prospects interacting with
  each other." [15].
- "Markets change as companies, technologies, and buyers change. Great positioning often becomes weak over time.
  Positioning cannot be a "one and done" exercise." [8]. The mechanism: "an offering which once had a very strong,
  clearly differentiated position will have its position weakened as features that were once unique become table
  stakes." [8].
- The failure she names when nobody revisits: "Like other totally useless business exercises - it is completed and
  never, ever referred to again." [8].
- Heinz, secondary: "that's why repositioning and taking an iterative approach to your positioning statement is
  important." [9].
- "We should also expect that our positioning for prospects will evolve over time as our differentiated value
  shifts relative to other alternatives in the market." [11].
- "Over time, launched 16 products into the market. We repositioned every single one at some point." [17].

**Triggers, verbatim:**

- Positive events: "Sometimes, those big events are positive - like an acquisition, a new round of funding, or new
  senior executive hires." [22].
- Negative events: "Other times, the big event is less positive - a bad quarter, a set of painful lost deals, a
  security breach, an outage, a regulatory fine, an unexpected change in the CEO or other senior folks." [22].
- "You shouldn't wait until disaster strikes to adjust your positioning, but when it does, that's a great time to
  revisit it." [22]. "We often don't look at our positioning until something big happens." [22]. "I've seen a
  pattern around moments where the CEO or exec team pauses to do some bigger-picture thinking about their
  businesses. It tends to happen around significant events." [22].
- Planning season, for the pitch built on positioning: "If you get to December without getting the key
  stakeholders aligned on a new pitch, don't be surprised if it ends up looking like a warmed-over version of last
  year's pitch." [22].
- Acquisitions: "An acquisition - for both the acquiring company and the company that has been acquired - is a
  golden opportunity to revisit and tighten up positioning." [28]. "If the new product adds significant new value
  that the parent product did not previously deliver, then you will want to adjust the positioning for the parent
  product, just like you would for a major new product release that adds new value." [28].
- A phantom competitor that becomes real: "if you do start to see them in deals, you can adjust your positioning at
  that time." [18], [10].
- Launch: "Launch the product, see where the market pulls you, then tighten up your positioning based on what you
  learn." [23].
- Each stage of the strategy: "At each step, you will have different positioning." [11].
- CLIMB: "Revisit it when your target market shifts meaningfully, when a new competitor changes the landscape,
  when you launch a product that doesn't fit the existing framework, or when customer research reveals that
  buyers see you differently than you intended." [51].
- Monitoring: "Companies with more established products get into trouble by not being diligent about monitoring
  their market landscape." [8].

**The qualifiers and the test.** "Not all problems are positioning problems." [22]. "One of the benefits of using a
structured positioning process is that we can revisit the steps and determine whether anything needs to change."
[27]. A check-in usually confirms:
"the big question is this - does any of that shift our value themes? Frequently the answer is no." [27]. "The
positioning itself does not need to change. However, if we now have new value we can deliver to customers that we
couldn't before, we'll have to go back to the drawing board and redo the positioning." [27]. "If your positioning is
just a feature list (hint: it isn't!), it will feel like you need to shift it every time your product changes in
any way." [27]. A change has a downstream duty: "A process for how downstream changes will happen when there is a
positioning change - This will include updating the sales pitch and messaging and any associated work to make
those changes." [26]. "A change in positioning can have a dramatically positive impact on a business, but only if
the company internalizes it and ensures that everything - marketing, sales, development, business development,
support - aligns with the strategic shift." [8].

**Scoped to other artifacts, and not to be imported.** The Starr Conspiracy's "Set a review cadence (quarterly, or
monthly if you're changing pricing)." governs a messaging framework [46], on the same page that calls positioning
stable for years [46]. Its "Trigger conditions that mean now, not later" are the framework's too [46]. Product
Marketing Alliance's "Update this section regularly" is a battlecard's pricing section [48], and its "Instead of a
quarterly refresh" line is about battlecards maintained by AI tools [48].

**What this means for the classification, laid out and not resolved.** The contract's test is "argued-and-durable
versus maintained-and-periodic" (`docs/internal/contracts/strategy-docs.md:85`). Its `foundation` members "change
on a timescale of years" (`:71-72`). Its `utility` members are "revised on a cadence", and "A roadmap nobody has
updated in six months is not a stale foundation, it is a broken instrument." (`:81-83`). The sources split on that
test. A six-month or annual check-in [26], [30], [52] and Dunford's stage-by-stage change [11] read as maintained
and periodic. Positioning "stable for years" [46], [51] and "Frequently the answer is no." [27] read as argued
and durable. One repository fact cuts across both: the `foundation`-class vision example already carries a review
date with a trigger, `next_review: "October 2026, or immediately if either leap of faith below is disproven"`
(`templates/product-vision/product-vision_example.md:8`). ADR 0076 recommends `foundation` and names `utility` as
the considered alternative:
`docs/internal/decisions/0076-positioning-statement-joins-strategy-docs-as-a-sixth-member.md:139-144`.
**The choice is the maintainer's.** What changes now is the premise: the bundle's "When We Revisit It" section can
cite sources for both a check-in interval and named triggers.

### The gap question's results, lead by lead

1. **The status quo as the main rival. Sourced.** "To win business, the first competitive alternative we need to
   beat is the status quo." [18]. Adi Oran: "In B2B, about 40% of deals end in "no decision."" [53], with the
   status quo described as "what they're doing now-spreadsheets, pen and paper, interns" [53], and "It has
   inertia. It's free. It's already in place. It's often "good enough."" [53]. Koji's guide contests the mechanism,
   citing Dixon and McKenna: "56% of those losses are indecision-driven - confusion, complexity, fear of choosing
   wrong - not status-quo preference (HBR, 2022)." [56]. The Dunford dimension reports that her own no-decision
   figures differ across posts; none is a Quotable line, so none may be cited.
2. **Phantom competitors. Sourced.** Competitors that never show up in deals "should not be considered when working
   on your positioning." [18]. "Dunford specifically warns against positioning against phantom competitors -
   competitors you've never actually lost to." [56]. The formula's single alternative slot [1] does nothing to
   prevent this; guidance has to.
3. **Proof beyond one reason-to-believe slot. Partly sourced.** Lumen Learning: "The "reasons to believe" are any
   proof points or evidence that show your customers how you live up to your claims about how you are different
   and better." [59]. Koji asks buyers directly: "What proof would have helped you decide faster?" [56]. A
   per-claim proof structure rested only on [54] and is dropped.
4. **Best-fit customer, and who is excluded. Sourced.** "Your best-fit target customers are customers that really
   care a lot about your unique value." [10]. "Your positioning must resonate with the champion." [23]. Koji
   defines fit by contrast: "What would be different about a peer who would NOT buy this?" [56]. Demographic and
   firmographic fields rested only on [54] and are dropped.
5. **Timing, or why now. Thinly sourced, and contested as a component.** Koji: "Relevant Trends (optional) - the
   "why now" context." [56], "What changed in the last 90 days that made you start looking?" [56], and "The trigger
   event is the urgency narrative. Without it, your positioning describes a destination buyers feel no need to
   leave for." [56]. Ibrahim Bashir: "Why buy anything? Why buy our product? Why buy right now?" [57], read as a
   preview only. Whether trends are a component is unsettled; see contested items.
6. **Deliberate exclusions. Weak.** Applied Frameworks repositions the rival rather than attacking it: "It's not
   "We are good; they are bad." It's "We are good at this; they are good at something else."" [55]. The gap
   dimension found no source stating that the statement should concede the product's own weakness. Exclusion lists
   rested only on [54] and are dropped. Blackblot's note that "separate product positioning statements will be
   needed" in some situations [34] and Dunford's prep question "What exactly are you positioning?" [23] bear on
   scope rather than exclusion.
7. **Testing with customers before adoption. The best-sourced lead.** "You will next have to test it and see if your
   positioning works with customers the way you think it should." [8]. "I would then test it on prospects, and if
   it worked, we ran with it." [10]. Koji names three interview populations: "Wins - recent customers (90-180
   days)... Losses - evaluated but didn't buy, or churned within 12 months... Never-evaluated - fit your ICP but
   never considered you." [56]. Applied Frameworks: "Interview some customers who have upgraded (or plan to
   upgrade) and what you learn will be the core of your message." [55]. Lumen adds a desk test: "If you can
   substitute any competitor's name for your own in the positioning statement-and it still sounds credible-then you
   need some additional work on your differentiators and competitive advantages." [59], and a delivery check: "You
   must be able to consistently live up to this promise" [59].
8. **Who signs off. Sourced, without named roles.** "if you can get the execs to sign off on positioning, you can
   reduce your internal approvals dramatically. After all, the words are pre-approved." [55]. "My work aligns the
   executive team around how their product should be positioned." [17]. Named approver roles rested only on [54]
   and are dropped.
9. **How it is shared and used. Sourced.** "A positioning document explains your product capabilities and message
   to your internal teams and agencies. It's the source document for branding, promotion, and sales enablement."
   [55]. HubSpot: "it's used as a source of truth to guide other processes, like the messaging for your marketing
   campaigns or the talking points salespeople use during 1:1 conversations." [2]. Recording the reasoning matters
   for adoption: "any team inside the company that doesn't understand how we developed the positioning and the
   thinking behind it will not accept it." [25]. A staged rollout plan rested only on [54] and is dropped.
10. **What brings the team back to it. Sourced**; see Revisit cadence and triggers, above.
11. **The paradigm objection. Sourced, and contested.** Lochhead argues that positioning as such is a trap:
    "Because positioning-by definition-is about placing your company inside an existing market. It assumes the
    aisle already exists." [58]. "Positioning asks: "Where do we fit?" Category Design asks: "What kind of future
    are we building?"" [58]. His "Category Kings earn 76% of the market cap." [58] is a bare figure the source
    asserts, not a finding this log can stand behind. Dunford's market category component is itself a choice of
    frame, "the definition of the market we intend to win" [10], which answers Lochhead only in part.

---

## The library's own boundaries and landing sites

**The worked example.** The contract requires an Acme Analytics example that "states Acme's positioning against a
named alternative, for the segment the product strategy example already chose, and contradicts neither sibling"
(`docs/internal/contracts/strategy-docs.md:140-142`). An example that invents another company is out of contract
(`:146-147`). What the siblings fix:

- **Target.** The strategy's target is "the unaccompanied analyst", whom downstream documents call the "Recurring
  Analyst" (`templates/product-strategy/product-strategy_example.md:45-48`). The vision's broader target is
  managers who "own a number" (`templates/product-vision/product-vision_example.md:44-46`).
- **Non-targets.** Enterprise data-platform teams (`product-strategy_example.md:50`) and the embedded-analytics OEM
  channel (`:56`). The vision excludes professional analysts (`product-vision_example.md:52-53`).
- **Alternatives already named.** "The real incumbent is the spreadsheet and the favour, not a product."
  (`product-vision_example.md:79`). General-purpose BI tools "require a modelling step our users cannot perform"
  (`:81-82`), and embedded-analytics vendors "sell to the software vendor rather than to the operator" (`:83-84`).
  No sibling names a competitor by brand. Either the status quo, which Dunford names first [18], or general-purpose
  BI tools would contradict no sibling; the choice is the build's, and it should be stated.
- **Differentiation already claimed.** The vision says Acme starts "from inside the operational systems", and
  calls that "an accident of history rather than a strategy" (`product-vision_example.md:69-71`). Dunford's warning
  about a default position "rooted in the history of the product idea" [8] bears on how the example states it.
- **Owner.** Dana Okoro, VP Product, owns the vision, the strategy and the North Star example
  (`product-vision_example.md:4`, `product-strategy_example.md:4`, `north-star-metrics_example.md:4`). No existing
  example names a product marketer. The example's owner field will enact the ownership default, so it inherits
  that default's label as the library's reasoning.

**The date window has no whole day in it.** The spec places the example after the product strategy (2026-01-28)
and before "the North Star metric example's own window (2026-01-29 through 2026-02-10)"
(`docs/internal/tier2-specs.md:6479-6480`). No date falls strictly between 2026-01-28 and 2026-01-29. The North
Star example is actually dated 2026-02-04 (`templates/north-star-metrics/north-star-metrics_example.md:6`), one week
after the strategy (`:15-16`); the roadmap example is dated 2026-02-11
(`templates/product-roadmap/product-roadmap_example.md:8`). Dates from 2026-01-29 to 2026-02-03 fall between the
strategy and the North Star examples. The internal dimension proposes 2026-01-29. The pick needs an explicit
decision and a dated correction to the spec's window, not a quiet choice. Whatever the date, the example must not
cite the North Star example, which postdates it.

**Third place leaves live sentences in `north-star-metrics` stale.** The amended contract already puts the North
Star fourth (`strategy-docs.md:180-182`). Its example says "this type sits third in the
`strategy-docs` chain" (`templates/north-star-metrics/north-star-metrics_example.md:15`). Its companion says
"This library places it third, between the strategy and the roadmap" (`north-star-metrics_companion.md:26-27`),
and again at `:249-250`. The history line at `north-star-metrics_history.md:26` is a record and stays. The spec
says no existing member's companion changes beyond the vision note (`docs/internal/tier2-specs.md:6511-6512`), and
the contract's change note says the North Star companion gains no line (`strategy-docs.md:189-190`). **Whether
these are dated factual corrections, outside that rule, is a maintainer call.**

**The no-cadence sentence lives in five places.** The spec at `docs/internal/tier2-specs.md:6285-6286`, its
section-design row at `:6404`, and its risk 5 at `:6465-6468`; the contract at `strategy-docs.md:78`; and ADR 0076
at `0076-positioning-statement-joins-strategy-docs-as-a-sixth-member.md:142`. Each is contradicted by [26], [30],
[52] and [8]. The contract allows a dated in-place correction of an unsourced claim under procedure 11
(`strategy-docs.md:9-11`).

**The vision companion note.** `templates/product-vision/product-vision_companion.md:276-280` says "No product
management source read draws this boundary". The landing PR adds a dated note, not a rewrite
(`0076-positioning-statement-joins-strategy-docs-as-a-sixth-member.md:191-196`). The note can now cite Sharebird
[43] and Dunford [11], [26], and should name the RUP counter-example [44]. The research log and history entries
recording the old finding stay (`docs/internal/tier2-specs.md:6505-6507`). The same companion's Moore paragraph
(`product-vision_companion.md:72-77`) agrees with this research and needs no change.

**Routing rows.** Three `product-vision` files route a positioning reader away without naming a destination: the
lean template (`product-vision_template-lean.md:42-44`), the guide's row 8 (`product-vision_guide.md:81`) and the
companion note above. `README.md`, `AGENTS.md` and `skills/` carry no mention of positioning (checked by grep for
"position").

**Count and family sentences stale on landing.** `README.md:214` reads "complete, five bundles" and its table lacks
a row. `templates/README.md:100-106` lists the family without this bundle. `STATE.md:278` says the family is
"complete at five members". The contract's Members line says "not yet built" (`strategy-docs.md:6`).

**The catalog row still carries the uncorrected values** (`docs/internal/catalog.md:43`): the alias "positioning
map", the owner "PMM", and "Moore's "for/who/that" template" as the named source. The spec's corrections stand
(`docs/internal/tier2-specs.md:6410-6439`), and this research adds nothing against them.

---

## Claims flagged contested or time-bound

1. **Who owns the statement.** Product marketing [34], [35], [42]; joint [36], [38]; split by task [39]; and
   executive-driven and cross-functional [30], [53]. No source states the library's default.
2. **Whether the statement is revisited on a calendar or on a trigger.** Dunford gives both, a six-month check-in
   plus emergency check-ins [26]. Abinanti gives 12 months [52]. CLIMB gives triggers and warns against quarterly
   rewrites [51]. The Starr Conspiracy calls positioning stable for years [46]. Dunford herself says B2B and
   consumer products differ [26].
3. **Where positioning sits against the vision.** Dunford's 2021 post puts it per strategy stage, on the way to the
   vision [11]; her 2020 post lists the vision among things that happen after positioning [7]. The two posts are a
   year apart and are not reconciled in anything read.
4. **Whether vision and positioning are one document or two.** Two documents, per Sharebird [43] and Dunford [11],
   [26]; one document with a positioning section, per RUP [44].
5. **Whether the fill-in statement should exist at all.** Dunford says "You Should Never Do One" [8] and also says
   to write positioning down in a dated record [8]. Heinz frames her components as building "a strong positioning
   statement" [9], which inverts her stance. Lochhead rejects positioning itself in favour of category design [58].
6. **A sixth component.** Heinz lists "Relevant Trends (Bonus)" [9]; Koji calls trends optional [56]; Dunford's own
   lists have five components [7], [10]. Only the book could settle it, and the book was not read [33].
7. **Dunford's component labels and step counts change by year**: 2019 [17], 2020 and 2021 [7], [10], 2026 [27];
   five blog steps in 2019 [8], ten book steps in the first edition, five core steps in the second [23], [31]. The
   2019 blog steps are not the second edition's steps.
8. **Time-bound: the second edition.** It shipped in February 2026 [32]; its updated templates were still pending
   [29], [32]; her promised post on assembling the team was not found [23]. Any claim about "the book" must name
   its edition.
9. **Heinz's case details.** Heinz says "Dunford's example is of IBM's database." [9]. The Dunford dimension reports
   that her own posts place that story at a database startup. Treat Heinz as a pointer to the first edition's
   structure only.
10. **No-decision figures.** Oran's "about 40%" [53] and Koji's 56 percent indecision share [56] disagree on the
    mechanism. Dunford's own figures vary across posts and none is quotable here.
11. **Bare figures.** Lochhead's 76 percent [58] and Koji's 2.5M+ conversations [56] are the sources' assertions,
    not findings of this log.
12. **Dated sources.** Applied Frameworks is from 2013 [55], Abinanti from 2017 [52], and eCornell's Amazon
    example from 2001 [3]. Dunford's views span 2017 to 2026 and her method changed in that span, most clearly on
    where to start [8], [10].
13. **Moore's authorship of the formula.** Unverified in every pass, and the Goodreads source does not bear on it
    [6].

---

## Honest framing

**What the bundle exists to say.** A positioning statement, as this bundle builds it, is a short internal document
stating how this product stands against a named alternative, for a specific target customer, now. The sources
support each part. It is internal [2], [3], [4], [5], [36], [47]. It is about the present [11], [23], [26], [43].
It names what the customer would otherwise do, including the status quo [10], [18], [53]. It is short [1], [2],
[4]. It records analysis rather than a sentence filled in from assumption [7], [8], [13]. It is an input to
messaging, the sales pitch and the battlecard, not any of them [8], [16], [36], [45], [46], [48]. It is
revisited, by check-in and by trigger [22], [26], [30], [51], [52].

**The ownership instruction.** The guide presents both ownership camps with their sources, then suggests a
default, labelled as this library's own reasoning, because no source supports it. Camp one, product marketing
owns it: Blackblot [34], Young Urban Project [35], and Karr's account of the Pragmatic Framework [42]. Camp two,
product management shares it: Aha!'s joint description [36], [38], its strategy-side template catalog [37], and
Nair's split [39]. The guide may add Dunford's account as context on who drives the work and who takes part [30],
without making it a third owner. The suggested default is that product management owns the statement as product
direction, and product marketing drafts or co-writes it. **No source states that division.** The guide must not
imply that the sources lean toward it. Where they lean, they lean toward product marketing [34], [35], [42].

**What the bundle must not claim:**

- **That writing one improves positioning or outcomes.** No source in this log measured that. The statements of
  value are claims [3], [8], [55].
- **That Geoffrey Moore wrote the formula.** No source here attributes it to him, and [6] is not about his book.
- **That no source states a cadence.** Three do [26], [30], [52], and a fourth asks for a dated review record [8].
- **That a cadence is settled.** The sources disagree on calendar against trigger (contested item 2).
- **That Dunford endorses the fill-in sentence, or that she rejects any written record.** She attacks the first
  [7], [8], [13] and endorses a dated record [8].
- **That the vision boundary is universal.** RUP nests positioning inside a vision document [44].
- **That third place in the chain is sourced.** Dunford's stage-by-stage account [11] supports strategy before
  positioning; no source states the library's sequence, and the link stays the library's POSITION.
- **That the Starr Conspiracy's quarterly cadence or trigger list applies to the positioning statement.** It
  governs a messaging framework [46].
- **That HubSpot's or Yesware's formula is this library's wording.** Their text is quotable as theirs [2], [4],
  never as the template's own.
- **Anything from the AI-agent toolkit template** [54].

---

## Notes for the companion

**Build decisions, 2026-10-20, taken from the notes below and overrulable by the maintainer.** The drafting
stages follow this list.

1. **Classification stays `foundation`, as ADR 0076 accepted it.** Whether the sourced cadence moves the type to
   `utility` is the maintainer's call at landing. The family already holds a `foundation` member with a dated
   review: the vision example's frontmatter carries `next_review` with a month and a trigger
   (`templates/product-vision/product-vision_example.md:8`). So When We Revisit It asks for the date of the last
   review, which Dunford's dated record supports [8], and for the named events that call an early review [22],
   [26], [51]. It may offer a periodic check-in as guidance, attributed to Dunford's six months [26] and
   Abinanti's 12 months [52], never as a standard, and it says the sources disagree (contested item 2). No file
   this bundle writes may say that no source states a cadence.
2. **The five sections stand, in the spec's order, with the candidates above that rest on E1 or on order alone.**
   The Statement stays first. Its reason to believe follows "because", and the differentiation takes its own
   clause [1], [2], [3], [4]. The Components lists the named alternative first [10]. The two E2 candidates in Why
   This Positioning become ASK questions rather than fields, so neither adds an element: how the positioning was
   tested with customers or prospects, and which other framing the team considered and why it lost.
3. **Ownership follows the D4 ruling of 2026-10-17.** The meta's owner is `PMM / PM`. The guide shows both camps
   with their sources, then the default as this library's own reasoning, as the ownership instruction above
   states it, including that the sources lean toward product marketing where they lean. The example enacts the
   default: Dana Okoro, VP Product, owns the statement. If the example names a product marketer who drafts or
   co-writes it, that name is new to this example and appears in no sibling.
4. **The example is dated 2026-01-30.** That falls after the product strategy example (2026-01-28) and before the
   North Star example (2026-02-04). The spec's window (`docs/internal/tier2-specs.md:6479-6480`) holds no whole day,
   so the landing PR corrects it with a dated note. The example cites neither the North Star example nor the
   roadmap example, which both postdate it.
5. **The example's named alternative is the status quo, the spreadsheet and the favour.** The vision example
   already names it the real incumbent (`product-vision_example.md:79`), and Dunford names the status quo as the
   first alternative to beat [18]. General-purpose BI tools may appear as a second alternative, in the vision's
   own terms (`:81-82`). No competitor is named by brand.

**The load-bearing sections.** The Components carries the analysis Dunford says the bare sentence skips [7], [13].
When We Revisit It is now sourced, and it is the section the classification question turns on [26], [30], [52].
Why This Positioning is where the team records why the positioning is what it is, which Dunford gives as the first
reason to write it down [8], and which decides whether other teams accept it [25]. Purpose and Boundary carries
the vision and messaging boundaries, both now sourced [11], [26], [43], [7], [8].

**The sharpest teaching points:**

1. The sentence summarizes the components; it does not replace them. "These are, in essence, the blanks of the
   positioning statement." [7].
2. The named alternative is what the customer would otherwise do, and the first one to beat is the status quo [18].
   A competitor never met in deals does not belong [18], [56].
3. The statement is customer positioning for now, not the vision and not the investor story [11], [23], [26].
4. The document is an input to messaging and holds none [8], [16], [46].
5. It gets a dated review and named triggers, and most reviews change nothing [8], [26], [27].
6. The desk test: if a rival's name fits the statement, the differentiation is not done [59]. Under decision
   procedure 12, step 1, this is a quality property, so it becomes a guide rubric row and not a template element.

**The five-section design, in light of the research.** All five sections stand. Every change below is a
**candidate**, for the maintainer or the build to accept. A change that adds an element faces decision procedure
12's admission test (`docs/internal/decision-procedures.md:232-241`): E1 means a named source publishes documents
of this type containing the element, and E2 means the library argues it in its own voice and states a falsifier.
A change to guidance wording or order adds no element; it is marked as guidance and rests on its citations. The
bundle is single-size, so every candidate must fit lean (E4).

- **Purpose and Boundary: keep.** Candidate guidance: say that this is customer positioning, not investor or
  employee positioning [23], [26], and name the persona or deal champion it is written for [23]. Guidance, homed
  in this section.
- **The Statement: keep, with two candidates.** First, an element change: put the reason to believe after
  "because", as the published forms of HubSpot, eCornell and Yesware do [2], [3], [4], and give the
  differentiation its own clause, as MIT does [1]. E1, homed in this section's sentence. Second, guidance: tell the
  writer to draft the sentence last, from the finished components. This is the library's reading of [7], [8],
  [13], labelled as such. The section stays first in reading order, so a reader who reads one line gets the
  summary. The field labels stay this library's own wording.
- **The Components: keep, with two candidates.** First, an order change: list the named alternative first,
  following Dunford's dependency argument, "the starting point had to be competitive alternatives" [10]. This is
  an arrangement, not an element, and rests on [10]. Second, guidance: the named alternative may be the status quo
  [18], [53] and may not be a phantom competitor [18], [56]. The spec's six components cover Dunford's five plus a
  need, which MIT, HubSpot and Yesware carry [1], [2], [4]. The labels stay this library's; any reference to
  Dunford's names must quote one of her lists and give its year.
- **Why This Positioning: keep, with two candidate elements, both E2.** First, a record of how the positioning was
  tested with customers or prospects. The practice is sourced [8], [10], [55], [56], but no source shows the
  document recording it. Its falsifier: a team that records its tests reaches the same agreement, with the same
  effort, as one that does not. Second, the other framing the team considered and why it lost, since "every
  product can be positioned in multiple different ways" [8]. No source asks the document to record it. Its
  falsifier: readers make the same calls whether or not the rejected framing is recorded. E3 for both: this
  section, since the battlecard and messaging are downstream and would not carry the team's reasoning [8], [48].
- **When We Revisit It: change the guidance, which the research overturns.** The spec's row says "not a calendar
  date" and that no source states a cadence (`docs/internal/tier2-specs.md:6404`). Both are now wrong as stated.
  Candidates: the date of the last review, which is E1, since Dunford's record is "dated so you can track when the
  positioning was last reviewed" [8]; a check-in interval and named triggers, which are sourced as practice [22],
  [26], [28], [30], [51], [52] but not shown inside a document, so they are E2, with the falsifier that a team
  holding them in the document revisits no more reliably than a team holding them elsewhere; Dunford's test of
  whether value themes moved [27] and the duty to update the pitch and messaging after a change [26], both as
  guidance. Whether the section asks for an interval at all depends on the classification, which stays the
  maintainer's call. A
  frontmatter review-date field, like the vision example's (`product-vision_example.md:8`), would home the E1
  date there instead of in the body.

**The traps:**

1. **Quoting the spans this log does not carry**, listed at the top of the checks section.
2. **Attributing the formula to Moore**, or citing [6] for anything about his book.
3. **Importing the Starr Conspiracy's messaging cadence and triggers** [46], or the battlecard's [48], into the
   positioning statement.
4. **Making Dunford say more than she said.** She opposes the fill-in exercise, not a written record [8]. Her
   components should not carry Heinz's labels [9]. "The book" needs an edition [31], [33].
5. **Presenting the ownership default as sourced**, or presenting shared ownership as the majority reading.
6. **Citing [54]**, or any gap lead that rested on it.
7. **Repeating bare figures as facts**: 40 percent [53], 56 percent [56], 76 percent [58], and any Dunford
   no-decision figure.
8. **Reusing the worked example's scenario in GOOD and WEAK text**, the risk the spec names
   (`docs/internal/tier2-specs.md:6469-6471`). Grep the drafted template for Acme, Dana Okoro, the unaccompanied
   analyst and the spreadsheet before review.
9. **Dating the example outside the gap between its siblings**, or citing the North Star example from it.
10. **Writing that no source states a revisit cadence**, in any file this bundle touches.
11. **Writing that no source places positioning after the strategy.** Dunford's stage-by-stage account [11] does,
    in effect. What no source states is the library's exact sequence.

## Sources

### CANON: THE FORMULA, ITS PUBLISHED FIELD SETS AND ITS DISPUTED ORIGIN

**[1] MIT Orbit Knowledgebase (Martin Trust Center for MIT Entrepreneurship), "What is a product positioning statement?".** practitioner. **fetched-and-verified.**
`https://orbit-kb.mit.edu/hc/en-us/articles/206439713-What-is-a-product-positioning-statement`
Supports: a six-slot for/who/is-a/that/unlike/that template, a 'one page format' length claim, and no statement of audience/readership
Quotable: "A product positioning statement forces you to use a one page format to summarize everything that matters for your product."
Quotable: "For [target customer]"
Quotable: "Who wants/needs [a compelling reason to buy]"
Quotable: "The [product name] is a [product category]"
Quotable: "That provides [these key benefits]."
Quotable: "Unlike [the main competitor],"
Quotable: "The [product name] [provides these key differentiation points]."

**[2] HubSpot (Meredith Hart), "16 Examples of Positioning Statements & How to Craft Your Own".** vendor. **fetched-and-verified.**
`https://blog.hubspot.com/sales/positioning-statement`
Supports: a five-field for/who/provides/because formula, a 3-5 sentence length guideline, an internal-but-also-read-by-outsiders audience claim, and no Moore/Ries/Trout attribution anywhere on the page
Quotable: "A positioning statement is a brief description of a product or service and an explanation of how it fulfills a particular need of the target market."
Quotable: "The goal of a positioning statement is to align marketing efforts with a company's brand and value proposition."
Quotable: "A positioning statement is an internal tools that help marketers appeal to their buyer personas in a relevant way."
Quotable: "Unlike a mission statement , your positioning statement isn't public-facing. You don't want to give away any competitive intelligence to your competitors, so it's used as a source of truth to guide other processes, like the messaging for your marketing campaigns or the talking points salespeople use during 1:1 conversations."
Quotable: "For [your target market] who [target market need], [your brand name] provides [main benefit that differentiates your offering from competitors] because [reason why target market should believe your differentiation statement.]"
Quotable: "A description of the target market."
Quotable: "A description of the target market needs."
Quotable: "How your business will meet their needs."
Quotable: "What differentiates your product or service from the competition."
Quotable: "Why consumers in your target market should believe your brand's claims."
Quotable: "Your brand's positioning statement should be concise and to the point. Aim for no more than three to five sentences, if possible."
Quotable: "Investors, new hires, and external agencies who work closely with your businesses will need to use this document, too."

**[3] eCornell #IMPACT (Doug Stayman, Cornell SC Johnson College of Business), "How to Write Market Positioning Statements".** academic. **fetched-and-verified.**
`https://ecornell-impact.cornell.edu/how-to-write-market-positioning-statements/`
Supports: a five-component for/is-the/among-all/because formula naming POD, FOR, and RTB explicitly, an internal-tool claim, a worked 2001 Amazon example, and no Moore/Ries/Trout attribution
Quotable: "A positioning statement is a concise description of your target market as well as a compelling picture of how you want that market to perceive your brand."
Quotable: "Though it may read like something from your promotional materials, your positioning statement is an internal tool."
Quotable: "Every product and marketing decision you make regarding your brand has to align with and support your positioning statement."
Quotable: "For [insert Target Market], the [insert Brand] is the [insert Point of Differentiation] among all [insert Frame of Reference] because [insert Reason to Believe]."
Quotable: "The wording of your positioning statement doesn't have to match this template exactly, but to be effective, it must contain the five main components in brackets above."
Quotable: "The point of differentiation (POD) describes how your brand or product benefits customers in ways that set you apart from your competitors."
Quotable: "The frame of reference (FOR) is the segment or category in which your company competes."
Quotable: "The reason to believe is just what it says."
Quotable: "For World Wide Web users who enjoy books, Amazon.com is a retail bookseller that provides instant access to over 1.1 million books. Unlike traditional book retailers, Amazon.com provides a combination of extraordinary convenience, low prices, and comprehensive selection."

**[4] Yesware (Casey O'Connor), "Positioning Statement: Examples, Templates, Best Practices".** vendor. **fetched-and-verified.**
`https://www.yesware.com/blog/positioning-statement/`
Supports: a six-field for/who/offers/so-they-can/because formula, a 3-5 sentence length guideline, an internal-audience claim naming marketing and sales teams, and no Moore/Ries/Trout attribution
Quotable: "A positioning statement is a short description of what your product or service does, whom it serves, how it differs from the competition, and how it meets the needs of your target market."
Quotable: "Positioning statements are typically meant to be internal and are used by marketing and sales teams to guide them in decision-making around sales strategy and the buying experience."
Quotable: "For [target market] who [target market need], [brand name] offers [market category] [point of difference/primary benefit differentiating you from competitors] so they can [end benefit] because [reason to believe]."
Quotable: "Positioning statements should be relatively short (3 - 5 sentences, at the most)."
Quotable: "1. Brand Identity"
Quotable: "2. Brand Values"
Quotable: "3. Target Audience"
Quotable: "4. Market Category"
Quotable: "5. Point of Difference"
Quotable: "6. Reason to Believe"
Quotable: "7. Brand Promise"

**[5] Product Marketing Alliance, "Positioning statement template" (positioning-statement-template-framework).** vendor. **fetched-and-verified.**
`https://www.productmarketingalliance.com/positioning-statement-template-framework`
Supports: an internal-resource definition, and confirmation that the actual field-by-field template is gated behind a membership paywall (no slot-by-slot formula is visible in the cached raw text, only the description and a download prompt)
Quotable: "A positioning statement is an internal resource used to influence the way a product, service, or brand is positioned to potential customers."
Quotable: "Download our template and start creating a compelling positioning statement that will resonate with stakeholders."
Quotable: "Become a member to see the rest."
Quotable: "You've landed on a piece of content that's exclusive to members ."

**[6] Goodreads, Benjamin's Kindle Notes & Highlights for "Positioning: The Battle for Your Mind" (Al Ries).** reference. **fetched-and-verified.**
`https://www.goodreads.com/notes/18914433-positioning/22295243-benjamin`
Supports: this page is reader highlights of Al Ries and Jack Trout's book 'Positioning: The Battle for Your Mind,' not of Geoffrey Moore's Crossing the Chasm, and it contains no for/who/that or any other slot-based template; it supports the general Ries/Trout concept of positioning as a mental, perceptual act, not any field-set formula
Quotable: "positioning is not what you do to a product. Positioning is what you do to the mind of the prospect. That is, you position the product in the mind of the prospect."
Quotable: "The basic approach of positioning is not to create something new and different, but to manipulate what's already up there in the mind, to retie the connections that already exist."
Quotable: "The first person, the first mountain, the first company to occupy the position in the mind is going to be awfully hard to dislodge."
Quotable: "to move a new idea or product into the mind, you must first move an old one out."

### APRIL DUNFORD'S COMPONENTS, PROCESS AND CRITIQUE

**[7] April Dunford - An Introduction to Positioning (2020).** primary. **fetched-and-verified.**
`https://www.aprildunford.com/post/an-introduction-to-positioning`
Supports: Dunford's definition of positioning; her five components listed in order (Competitive Alternatives, Differentiated Features or Capabilities, Value for customers, Target Customer Segmentation, Market Category); her 2020 critique of the Mad Libs positioning statement and its one concession (the blanks show there are multiple components); and that messaging, storytelling, tag lines, vision and branding come after positioning and take it as input
Quotable: "Positioning defines how your product is a leader at delivering something that a well-defined set of customers cares a lot about."
Quotable: "Positioning is not the same thing as messaging. It isn't a tag line."
Quotable: "the best way I can describe it is as a sort of "Mad Libs" fill in the blanks exercise for marketing folks."
Quotable: "I've written before about why I think this exercise is not only pointless but potentially dangerous, but I can summarize by saying this - the exercise assumes that there is only one answer for each of the blanks."
Quotable: "However, most products could easily be positioned in multiple different market categories, with different competitors, providing different value for different kinds of customers."
Quotable: "The only valuable thing we can learn from the statement is that there are multiple components of positioning. These are, in essence, the blanks of the positioning statement."
Quotable: "The components are: - Competitive Alternatives - Differentiated "Features" or "Capabilities" - Value for customers - Target Customer Segmentation - Market Category"
Quotable: "Great positioning is when you have defined these in the best way possible for the offering."
Quotable: "messaging, a tag line, your vision, branding - these are all examples of things that happen after positioning. Each of these things requires positioning as an input or the starting point."
Quotable: "Put simply, positioning defines what market you intend to win and why you deserve to win it."

**[8] April Dunford - A Product Positioning Exercise (2019).** primary. **fetched-and-verified.**
`https://www.aprildunford.com/post/a-product-positioning-exercise`
Supports: Her 2019 five-step positioning exercise (steps named verbatim, with no competitive-alternatives step); her three reasons the positioning statement is harmful, including that it is one-and-done; her qualifier that positioning should still be written down in a dated record so the last review date is tracked; the 2019 template (image only); testing positioning with customers; and the explicit split between the positioning template and a messaging document that references it
Quotable: "The Positioning Statement is Harmful and You Should Never Do One"
Quotable: "It's a fill-in-the-blanks exercise where you create a single phrase that encapsulates what your offering is all about relative to your competition."
Quotable: "1/ This exercise assumes great positioning is magically locked inside your head and you simply have to write it down."
Quotable: "The truth is that every product can be positioned in multiple different ways and which one you choose has a massive impact on your business."
Quotable: "The positioning statement exercise encourages you to assume there is only one way to position your offering (a dangerous assumption)."
Quotable: "2/ The output of this exercise is an awkward franken-statement of gobbledygook that cannot be easily shared, understood or remembered by the teams who need to use it."
Quotable: "Like other totally useless business exercises - it is completed and never, ever referred to again. The exercise is, at best, a waste of time."
Quotable: "3/ Creating a positioning statement gives you the false sense that you are "done" doing positioning and you can move on to worrying about other things."
Quotable: "Markets change as companies, technologies, and buyers change. Great positioning often becomes weak over time. Positioning cannot be a "one and done" exercise."
Quotable: "When I work with companies on positioning we do this in 5 steps. The steps are easy but the work is not."
Quotable: "Step 1: Let go of where you came from"
Quotable: "Step 2 - Isolate your Uniqueness"
Quotable: "Step 3 - Value: what can your uniqueness do for customers?"
Quotable: "Step 4 - Who Cares?"
Quotable: "Step 5 - Choose your best market frame of reference"
Quotable: "Weak positioning is usually the result of hanging on to a "default" market position that is rooted in the history of the product idea."
Quotable: "In this step you should list everything you have that makes your offering unique."
Quotable: "Customers don't care about your unique features, they care what those features can do for them."
Quotable: "the next step is to figure out who cares a lot about that value."
Quotable: "You need to choose a market frame of reference that makes your awesomeness completely obvious."
Quotable: "Companies with more established products get into trouble by not being diligent about monitoring their market landscape."
Quotable: "an offering which once had a very strong, clearly differentiated position will have its position weakened as features that were once unique become table stakes."
Quotable: "A change in positioning is a fundamental change in your business."
Quotable: "A change in positioning can have a dramatically positive impact on a business, but only if the company internalizes it and ensures that everything - marketing, sales, development, business development, support - aligns with the strategic shift."
Quotable: "Once you have all the pieces together, you will want to write it down. Writing it down is good for two reasons:"
Quotable: "1/ You have a record of the agreed upon positioning, in a form that makes it easy to understand why the positioning is what it is."
Quotable: "2/ The document is dated so you can track when the positioning was last reviewed."
Quotable: "So if you want to capture positioning so you can review it and share it, here's a template I use"
Quotable: "You will next have to test it and see if your positioning works with customers the way you think it should."
Quotable: "The positioning template should not be a way of documenting your value proposition or approved messaging around features or value."
Quotable: "Once you have your positioning figured out, this becomes a set of inputs to your messaging."
Quotable: "I usually build a messaging document that references the positioning template."
Quotable: "The messaging document goes a level deeper into approved messaging for value statements for different buyer personas and provides boilerplate messaging that can be used as a starting point for marketing and sales materials."

**[9] Sarah Threet, Heinz Marketing - Five Components of Effective Positioning: An Obviously Awesome Book Summary, Part 2 (2023).** practitioner. **fetched-and-verified.**
`https://www.heinzmarketing.com/blog/five-components-of-effective-positioning-an-obviously-awesome-book-summary-part-2/`
Supports: Secondary summary of the FIRST edition of Obviously Awesome (Sept 2023): the classic template in text form; Threet's labels and one-line definitions for five components plus a bonus Relevant Trends component; mention of a 10 Step Positioning Process. Credits the fast-database story to IBM, which conflicts with Dunford's own blog accounts of that story, and frames the components as building a positioning statement, which inverts Dunford's stance
Quotable: "This summary covers the five (plus one) components that make up a strong positioning statement."
Quotable: "For [target buyers], [your offering] is a [market category], which provides [main benefits] unlike [competitor] which provides [competitor's benefits]."
Quotable: "it is flawed in that it assumes we have all of the answers we need to create a powerful positioning statement."
Quotable: "Competitive Alternatives: What our target audience would use/consume if our solution did not exist."
Quotable: "Unique Attributes: The features and capabilities that our product/service has that alternatives do not."
Quotable: "Value (and Proof): The benefits of those features to our target buyers and how they address their pain point(s)."
Quotable: "Target Market Characteristics: The attributes of a group of buyers (including their pain points) that make them care about the value of our solution."
Quotable: "Market Category: The market we define our solution as fitting to better help illustrate the value to our target buyers."
Quotable: "Relevant Trends (Bonus): Trends that our target audience may be aware of/interested in that may affect the way they view our solution, and what may help or hinder our solution's relevancy."
Quotable: "Dunford's example is of IBM's database."
Quotable: "that's why repositioning and taking an iterative approach to your positioning statement is important."
Quotable: "the positioning statement should be an integral part of marketing, messaging, and iteration."

**[10] April Dunford - A Quickstart Guide to Positioning (2021).** primary. **fetched-and-verified.**
`https://www.aprildunford.com/post/a-quickstart-guide-to-positioning`
Supports: Her 2021 component list (identical to 2020); the component-to-component dependencies; that the starting point had to be competitive alternatives (after reading Jobs To Be Done); the five-part workflow with a working question for each component; the statement critique restated; and a revisit trigger (adjust positioning when a phantom competitor starts showing up in deals)
Quotable: "Positioning is not equivalent to messaging. It isn't a tagline."
Quotable: "I believe this exercise is not only pointless but potentially dangerous . The exercise assumes that there is only one answer for each of the blanks, and you simply "know" what it is."
Quotable: "How would this exercise help me understand that my "Microsoft Access Killer" was really an "Embeddable Database for Mobile Devices?" The answer is that it simply would not."
Quotable: "Breaking positioning up isn't hard because we generally agree on the components. These are, in essence, the blanks in the positioning statement."
Quotable: "The components are: Competitive Alternatives Differentiated "Features" or "Capabilities" Value for customers Target Customer Segmentation Market Category"
Quotable: "For example, the unique value that you can provide to customers is completely dependent on your differentiated features. Your differentiated features are only "differentiated" when you compare them to competitive alternatives."
Quotable: "Your best-fit target customers are customers that really care a lot about your unique value. And lastly, your best market category is the context you position your product in such that your unique value is obvious to your target customers."
Quotable: "I had the realization that the starting point had to be competitive alternatives."
Quotable: "We start with competitive alternatives , or what would customers do if our solution didn't exist."
Quotable: "Once we have that, we can ask ourselves, "What do we have that the alternatives do not?" That gives us a list of differentiated features or key unique attributes"
Quotable: "We can then go down that list and ask ourselves, " So what for customers?" Put another way, what is the value those capabilities enable for our buyers?"
Quotable: "Once we understand what our differentiated value is, then we can move to customer segmentation, or who are the customers that care a lot about our value."
Quotable: "Lastly, we move to market category. Our best market category is the context we position our product in such that our value is obvious to our target customers. Put another way, it is the definition of the market we intend to win"
Quotable: "I attempted to find the best positioning for my products by picking an arbitrary starting point (for example, features) and then working my way through the others to get a "candidate positioning." I would then test it on prospects, and if it worked, we ran with it."
Quotable: "The book gets into additional details about how to execute the methodology, how positioning changes in new versus existing markets and how you can take advantage of trends."
Quotable: "if you do start to see them in deals, you can adjust your positioning at that time."

**[11] April Dunford - Positioning vs Strategy vs Vision (2021).** primary. **fetched-and-verified.**
`https://www.aprildunford.com/post/positioning-vs-strategy-vs-vision`
Supports: Positioning is rooted in the present and is the foundation of the current sales pitch; it is distinct from vision and strategy; it changes at each stage of the strategy and as differentiated value shifts relative to alternatives
Quotable: "Positioning is firmly rooted in the present. Positioning describes how your product wins business today in the market as it exists today and is the foundation of your current sales pitch."
Quotable: "It describes why a specific type of customer should choose your product over any other alternative way of solving the problem"
Quotable: "I don't see it as quite that simple, particularly because our positioning will change with each step of our strategy."
Quotable: "Positioning changes over time as we follow our strategy on the journey to the vision. At each step, you will have different positioning."
Quotable: "We should also expect that our positioning for prospects will evolve over time as our differentiated value shifts relative to other alternatives in the market."

**[12] April Dunford - Templates (aprildunford.com page).** primary. **fetched-and-verified.**
`https://www.aprildunford.com/templates`
Supports: Her current templates are distributed as a 12-page workbook to newsletter subscribers, not as a public page
Quotable: "Looking for the templates that go with Obviously Awesome or Sales Pitch?"
Quotable: "Sign up for my newsletter and receive my workbook (yes, this is a collection of templates for both books) for free."
Quotable: "I've created a brand new 12-page workbook that includes all of the templates for Obviously Awesome and Sales Pitch combined."

**[13] April Dunford - Product Framing Can Help Grow Your Startup (2017).** primary. **fetched-and-verified.**
`https://www.aprildunford.com/post/product-framing-can-help-grow-your-startup-or-kill-it`
Supports: Her original 2017 attack on the positioning statement (most useless business tool; assumes you already know the answers; confuses doing positioning with writing it down) and her claim that every product can be framed multiple ways
Quotable: "The positioning statement: candidate for most useless business tool ever"
Quotable: "There is so much to hate about this I barely know where to start. Never has such a useless tool been so widely used."
Quotable: "The fact that the output of this exercise is a hilariously awkward franken-statement of meaningless mumbo jumbo isn't even the worst part of it."
Quotable: "No, the worst part of this "positioning exercise" is that it assumes you already know the answers!"
Quotable: "I would simply plug in my assumptions as they stand today and voila! I've nailed my positioning!"
Quotable: "Somewhere along the way we have confused teaching people HOW TO DO positioning with teaching people HOW TO WRITE DOWN positioning."
Quotable: "Since the 1970's we've been taught that "Positioning" is critical to our businesses and we have been instructed to do it by creating a "Positioning Statement""
Quotable: "In my experience, every product can be framed in multiple ways and some frames are better than others."

**[14] April Dunford - Positioning Is Not A Marketing Exercise (2017).** primary. **fetched-and-verified.**
`https://www.aprildunford.com/post/if-you-think-positioning-is-a-marketing-exercise-youre-doing-it-wrong`
Supports: Positioning must be embodied across the organization and implementing it crosses every department, not just marketing
Quotable: "Today Positioning needs to be embodied across the entire organization."
Quotable: "Positioning is closely tied to your overall business strategy - implementing it crosses every department in the company, not just marketing."

**[15] April Dunford - Everything You Know About Positioning Is Wrong (2017).** primary. **fetched-and-verified.**
`https://www.aprildunford.com/post/everything-you-know-about-positioning-is-wrong`
Supports: Positioning is iterative and should shift as features, markets and competitors shift; it is a cross-functional effort that cannot be left to marketing
Quotable: "Modern positioning is iterative, and is developed and refined over time by the company and prospects interacting with each other."
Quotable: "Positioning will (and should) shift over time as features, markets, competitors shift."
Quotable: "The process of Positioning can no longer be left to the marketing department along and is a cross-functional effort aimed at helping make the offering successful."

**[16] April Dunford - Storytelling vs Positioning (2020).** primary. **fetched-and-verified.**
`https://www.aprildunford.com/post/storytelling-vs-positioning`
Supports: Positioning comes before storytelling and messaging; her workshops end by translating positioning into a sales narrative or pitch; the five inputs needed before a story can be written
Quotable: "In my Positioning workshops, we often end with a storyboarding exercise that translates the positioning we have worked on into a sales narrative or "pitch" that embodies that positioning."
Quotable: "Positioning is not the result of a story. Stories require positioning as an input."
Quotable: "We need both. But positioning must always come first."
Quotable: "We need a deep understanding of the real competitive alternatives to our solution, the unique features we have, the differentiated value that those features drive,"
Quotable: "the segments of customers that care a lot about that value, and the market category where we win before we know what our story is all about."

**[17] April Dunford - My Positioning Book Launches Today (2019).** primary. **fetched-and-verified.**
`https://www.aprildunford.com/post/my-positioning-book-obviously-awesome-launches-today`
Supports: Her 2019 component labels (competitive alternatives, unique capabilities, differentiated value, target customers, market category) as the blanks of a positioning statement; her description of the statement process as a laughably vague fill-in-the-blanks exercise; her consulting aligns the executive team; she repositioned every one of 16 products
Quotable: "Those parts are competitive alternatives, unique capabilities, differentiated value, target customers, market category. These are essentially the "blanks" of a positioning statement."
Quotable: "is a laughably vague fill in the blanks exercise that relies on a magic combination of voodoo and intuition to choose what market you should be positioned in."
Quotable: "My work aligns the executive team around how their product should be positioned."
Quotable: "Over time, launched 16 products into the market. We repositioned every single one at some point."

**[18] April Dunford - Positioning and Competition (2020).** primary. **fetched-and-verified.**
`https://www.aprildunford.com/post/positioning-and-competition`
Supports: Competitive alternatives, not competitors, starting with the status quo; phantom competitors are excluded; adjust positioning when such a competitor starts appearing in deals
Quotable: "When working on positioning, I think it's helpful to think about "Competitive Alternatives" rather than "competitors." To win business, the first competitive alternative we need to beat is the status quo."
Quotable: "A better way to think about competitive alternatives is to ask yourself, "What would a customer do if your offering didn't exist?""
Quotable: "should not be considered when working on your positioning."
Quotable: "The product team might want to keep an eye on them as a future competitive threat, and if you do start to see them in deals, you can adjust your positioning at that time."

**[19] April Dunford - What The Heck Is Your Product, Really? (2017).** primary. **fetched-and-verified.**
`https://www.aprildunford.com/post/what-the-heck-is-your-product-really`
Supports: Choosing a market frame of reference is a strategy decision, not merely a marketing or messaging decision, and changes the trajectory of the business
Quotable: "It's not merely a marketing decision or a messaging decision - it's a strategy decision."
Quotable: "the frame of reference we choose for that product will change the entire trajectory of the business."

**[20] April Dunford - How Context can Transform Your Product (2017).** primary. **fetched-and-verified.**
`https://www.aprildunford.com/post/how-to-transform-your-product-by-giving-it-context`
Supports: Her 2017 description of positioning as a process (what sets you apart, the value it brings, which customers care most); read in full, used only for this point
Quotable: "Great positioning is a process of deeply understanding what sets you apart from the other solutions in the market, the value that differentiator brings to customers, and which customers care the most about that value."

**[21] April Dunford - Don't let Customers Decide What Your Product Is (2019).** primary. **fetched-and-verified.**
`https://www.aprildunford.com/post/dont-let-customers-decide-what-your-product-is`
Supports: If a company does not position deliberately, the team falls back on a default position or customers decide what the product is; read in full, used only for this point
Quotable: "Customers will decide what you are, using the clues they can most easily assemble."

**[22] April Dunford - When To Revisit Your Positioning (2024).** primary. **fetched-and-verified.**
`https://aprildunford.substack.com/p/when-to-revisit-your-positioning`
Supports: When to revisit positioning: a list of positive and negative trigger events (acquisition, funding round, executive hires; bad quarter, lost deals, breach, outage, fine, CEO change), with her qualifier that not all problems are positioning problems; the executive team re-aligns on who they compete with and what value they deliver
Quotable: "You shouldn't wait until disaster strikes to adjust your positioning, but when it does, that's a great time to revisit it."
Quotable: "We often don't look at our positioning until something big happens."
Quotable: "I've seen a pattern around moments where the CEO or exec team pauses to do some bigger-picture thinking about their businesses. It tends to happen around significant events."
Quotable: "Sometimes, those big events are positive - like an acquisition, a new round of funding, or new senior executive hires."
Quotable: "Other times, the big event is less positive - a bad quarter, a set of painful lost deals, a security breach, an outage, a regulatory fine, an unexpected change in the CEO or other senior folks."
Quotable: "Not all problems are positioning problems."
Quotable: "an opportunity to get the executive team together and re-align itself with the business fundamentals. Who do we REALLY compete with today in the market?"
Quotable: "If you get to December without getting the key stakeholders aligned on a new pitch, don't be surprised if it ends up looking like a warmed-over version of last year's pitch."

**[23] April Dunford - Positioning Prep Part 1: Decisions to Make Before a Positioning Exercise (2026).** primary. **fetched-and-verified.**
`https://aprildunford.substack.com/p/positioning-prep-part-1-decisions`
Supports: The second edition (2026) restructures the first edition's 10 steps into prep work, five core steps and post work; the four prep decisions (readiness, audience, what is positioned, which persona); pre-launch positioning is a thesis; customer positioning focuses on now; positioning targets the deal champion; a promised post on assembling the team
Quotable: "The first edition of Obviously Awesome had 5 positioning components but 10 steps."
Quotable: "Prep work (the decisions and preparation you need before starting) - 5 core steps (matching the 5 positioning components) - Post work (how to make your positioning real)"
Quotable: "Getting clear on these things before the exercise starts ensures you have the right folks in the room, that expectations are set realistically, and that we don't have to do any rework down the road."
Quotable: "Is now the right time to tackle positioning? - Who is the positioning for? - What exactly are you positioning? - Which persona are you positioning for?"
Quotable: "If your product hasn't launched yet, what you're actually creating is a positioning thesis, not true positioning."
Quotable: "Launch the product, see where the market pulls you, then tighten up your positioning based on what you learn."
Quotable: "The methodology in Obviously Awesome is designed specifically for customer positioning-not investor positioning, not employee positioning, not partner positioning."
Quotable: "Customer positioning focuses on now and the immediate future: What do customers get for their money today versus available alternatives?"
Quotable: "Your positioning must resonate with the champion."
Quotable: "In the next edition of this series, I'll cover the prep work you need to do once these decisions are made-how to assemble your team and what preparation needs to happen before you dive into the actual positioning exercise."

**[24] April Dunford - The Positioning + Sales Pitch Workshop (Substack page).** vendor. **fetched-and-verified.**
`https://aprildunford.substack.com/p/the-positioning-sales-pitch-workshop`
Supports: Her flagship workshop is a facilitated three-day session to align the executive team on the five components and translate them into a sales pitch
Quotable: "My flagship workshop is designed to help align your executive team around your best positioning and a sales pitch that accelerates revenue."
Quotable: "This is a facilitated three-day workshop where we develop each of the five component pieces of your positioning and translate that positioning into a sales pitch that makes a clear, compelling case for why a prospect should choose you."

**[25] April Dunford - Why Positioning Fails to Make the Jump from Marketing to Sales (2024).** primary. **fetched-and-verified.**
`https://aprildunford.substack.com/p/why-positioning-fails-to-make-the`
Supports: Sales must be involved in creating the positioning, because teams that do not understand how it was developed will not accept it
Quotable: "Great B2B positioning will die inside the company if it doesn't successfully make the jump from marketing to sales."
Quotable: "In my experience, any team inside the company that doesn't understand how we developed the positioning and the thinking behind it will not accept it."
Quotable: "The obvious way to fix this is to have sales involved in creating the positioning in the first place."

**[26] April Dunford - Shifting Positioning - Why B2B Tech is Different (2024).** primary. **fetched-and-verified.**
`https://aprildunford.substack.com/p/shifting-positioning-b2b-tech`
Supports: B2B positioning is expected to shift; positioning reflects why a customer chooses you now, not the future vision; a six-month positioning check-in plus emergency check-ins triggered by a new competitor, an acquisition or a big product release; a process for downstream changes to the sales pitch and messaging
Quotable: "Consumer products rarely shift positioning, where positioning shifts are expected and normal for B2B products."
Quotable: "Our positioning today needs to reflect why a customer would choose us over the other alternatives they might choose in the market right now, not why we believe we will be a great choice in the future."
Quotable: "3/ We need to expect our positioning to change over time and have the processes in place to review and adjust our position."
Quotable: "A structured process is needed to do positioning because you will have to do it more than once."
Quotable: "Regularly scheduled positioning checkins-When I was working in-house, we would have a positioning checkin every six months. We would also call an emergency check-in if something big happened (e.g., a new competitor in the space, an acquisition, a new big product release, etc.)."
Quotable: "A process for how downstream changes will happen when there is a positioning change - This will include updating the sales pitch and messaging and any associated work to make those changes."

**[27] April Dunford - Shifting Positioning When AI Capabilities are Rapidly Changing (2026).** primary. **fetched-and-verified.**
`https://aprildunford.substack.com/p/shifting-positioning-when-ai-capabilities`
Supports: Second-edition-era step names (Step 1 Competitive Alternatives, Step 2 Distinct Capabilities, Step 3 Differentiated Value); the test for whether a change requires new positioning: re-run the steps and ask whether the value themes changed
Quotable: "One of the benefits of using a structured positioning process is that we can revisit the steps and determine whether anything needs to change."
Quotable: "Step 1 - Competitive Alternatives"
Quotable: "Step 2 - Distinct Capabilities"
Quotable: "Step 3 - Differentiated Value"
Quotable: "the big question is this - does any of that shift our value themes? Frequently the answer is no."
Quotable: "The positioning itself does not need to change. However, if we now have new value we can deliver to customers that we couldn't before, we'll have to go back to the drawing board and redo the positioning."
Quotable: "If your positioning is just a feature list (hint: it isn't!), it will feel like you need to shift it every time your product changes in any way."

**[28] April Dunford - Positioning and Acquisitions (2024).** primary. **fetched-and-verified.**
`https://aprildunford.substack.com/p/positioning-and-acquisitions`
Supports: An acquisition is an occasion to revisit positioning; new value from an acquired product changes the parent's positioning like a major release would; a positioning exercise brings marketing, sales and product from both sides together
Quotable: "An acquisition - for both the acquiring company and the company that has been acquired - is a golden opportunity to revisit and tighten up positioning."
Quotable: "If the new product adds significant new value that the parent product did not previously deliver, then you will want to adjust the positioning for the parent product, just like you would for a major new product release that adds new value."
Quotable: "There aren't many formal opportunities to get folks from across marketing, sales, and product - from both sides of the acquisition - together in a discussion around the competitive landscape, differentiated value, and ideal prospects."

**[29] April Dunford - Guest Post on Lenny's Newsletter today (2026).** primary. **fetched-and-verified.**
`https://aprildunford.substack.com/p/guest-post-on-lennys-newsletter-today`
Supports: Updated second-edition templates with completed examples and an example sales pitch were in preparation in March 2026; links her Lenny's Newsletter guest post (not read)
Quotable: "I'm putting the finishing touches on a new set of templates for the updated version of Obviously Awesome. By popular demand, I'm including a set of completed templates and an example sales pitch."

**[30] April Dunford - Special Lenny's Podcast Drop and How to Manage A Big Positioning Change (2023).** primary. **fetched-and-verified.**
`https://aprildunford.substack.com/p/special-lennys-podcast-drop-and-how`
Supports: Who takes part: the CEO (or the business owner in a large company) drives the effort; product, marketing and sales, often with customer success and development, are involved in creating the positioning; sales leadership rolls out the pitch. Cadence: a regular check-in a couple of times a year
Quotable: "In tech companies, it's normal for our positioning to shift over time."
Quotable: "Your positioning might also change due to shifts in the competitive landscape or changes in customer behavior (often driven by economic forces)."
Quotable: "Plan for this by having a regular (a couple of times a year) check-in to determine whether or not you need to make a positioning adjustment."
Quotable: "For smaller companies, the CEO needs to drive the effort (for bigger companies, it should be whoever is ultimately responsible for the business the product is part of). If the CEO isn't on board with the new positioning, it doesn't stick."
Quotable: "Product, Marketing, and Sales (plus often customer success and development) - need to be involved in creating the positioning. If they aren't involved in creating it, it will be very hard to get their buy-in after the fact."
Quotable: "Marketing and Sales (and often product) must build a sales pitch that reflects the positioning."
Quotable: "Once we have a pitch we will agree on, sales leadership needs to drive rolling the pitch out to the sales team."

**[31] April Dunford - Announcement: Obviously Awesome, the new updated and expanded edition (2026).** primary. **fetched-and-verified.**
`https://aprildunford.substack.com/p/announcement-obviously-awesome-the`
Supports: The first edition had five components and a 10-step process; the second edition moves the first and last steps into pre-work and post-work, giving five components and five steps; the final section covers creating a sales pitch to test positioning and turning positioning into messaging; her thinking has evolved since the first edition
Quotable: "In the first edition, I describe five components of positioning and a 10-step process for doing it."
Quotable: "The first few steps were really pre-work for a positioning exercise, and the final steps described work that needed to happen after the exercise. I have repositioned those steps (see what I did there), and we now have five components and five steps."
Quotable: "The pre-work section has been expanded to include key decisions a team should make before beginning a positioning exercise."
Quotable: "The final section of the book, What Happens After a Positioning Exercise, has been greatly expanded."
Quotable: "This expanded section reflects my current thinking on how best to create a sales pitch to test positioning and then turn that positioning into messaging."
Quotable: "And while I still believe that positioning is a bedrock, evergreen marketing concept, my thinking around particular aspects of positioning has evolved."

**[32] April Dunford - New Book Available, early announcement for subscribers (2026).** primary. **fetched-and-verified.**
`https://aprildunford.substack.com/p/new-book-available-early-announcement`
Supports: The second edition shipped in February 2026 with a new pre-work section and a new chapter on value; updated templates were still pending then
Quotable: "There's a new pre-work section, a new chapter on value, added content for large companies, and a lot more."
Quotable: "The updated templates are taking me a little longer than expected."

**[33] April Dunford - Obviously Awesome (book; first edition 2019, second edition February 2026).** primary. **not-retrieved.**
`https://www.aprildunford.com/books`
Supports: Not read and no preview read. Her own posts establish that the first edition had five components and a 10-step process and that the second edition (February 2026) restructured it into prep work, five core steps and post work. Any claim about the book must name its edition; nothing in this file quotes the book; Not read and no preview read. Her posts describe it as the companion that goes deep on turning positioning into a sales pitch; nothing in this file quotes it

### OWNERSHIP AND PLACEMENT

**[34] Gabriel Steinhardt (Blackblot) - "Product Positioning Clarifications".** vendor. **fetched-and-verified.**
`https://www.blackblot.com/product-positioning-clarifications`
Supports: States plainly that product positioning statements are created by the product marketer in Product Marketing, not by product planning or by MarCom; also that the number of statements needed (not who owns them) can vary by situation
Quotable: "Product positioning statements are created by the product marketer who belongs to the Product Marketing department."
Quotable: "Product positioning statements are irrelevant to the product planner (a role in Product Planning) and to the MRD (Market Requirements Document) as product positioning is created only after the PRD (Product Requirements Document) is created by the Product Architect (a role in Development)."
Quotable: "The MarCom Manager does not create product positioning statements."
Quotable: "It all depends on the given situation. It is possible that separate product positioning statements will be needed or perhaps only one product positioning statement will suffice."

**[35] Sakshi Jonwal (Young Urban Project) - "Positioning in Product Marketing: Strategy, Frameworks & Real-World Examples".** practitioner. **fetched-and-verified.**
`https://www.youngurbanproject.com/positioning-in-product-marketing/`
Supports: States product positioning is usually owned by the Product Marketing function, feeding into messaging, content, sales enablement and campaign planning
Quotable: "Both are strategic, but product positioning is usually owned by the Product Marketing function."
Quotable: "Product marketing owns these pieces. And positioning is their secret weapon."
Quotable: "“Positioning is the act of deliberately defining how you are the best at something that a defined market cares a lot about.” - April Dunford, author of Obviously Awesome"

**[36] Aha! - "Product positioning: Tips, templates, and examples" (roadmapping guide).** vendor. **fetched-and-verified.**
`https://www.aha.io/roadmapping/guide/product-strategy/what-is-product-positioning`
Supports: States product positioning is a cross-functional exercise typically involving product management and product marketing working closely together, not a single-owner split; also confirms the already-quoted 'internal document that informs external messaging' line
Quotable: "Product positioning is a cross-functional exercise. It typically involves product management and product marketing working closely together to define the core essence of your product."
Quotable: "The outcome of product positioning is an internal document that informs external messaging - including how you will communicate product benefits to customers."

**[37] Aha! - "Templates" (roadmapping guide, full template catalog page).** vendor. **fetched-and-verified.**
`https://www.aha.io/roadmapping/guide/templates`
Supports: Confirms the catalog split already cited in tier2-specs.md: 'Product positioning templates' sits under the page's 'Strategy product management templates' heading, while a separate 'Marketing positioning templates' sits under 'Marketing' templates further down the same page
Quotable: "Strategy product management templates"
Quotable: "Product positioning templates"
Quotable: "Marketing teams bring your company’s product to market. Use these templates to set and achieve marketing milestones:"
Quotable: "Marketing positioning templates"

**[38] Aha! (staff byline) - "New product management template: Product positioning" (Aha! blog, Oct 4 2023).** vendor. **fetched-and-verified.**
`https://www.aha.io/blog/new-product-management-template-product-positioning`
Supports: States product positioning is a strategic exercise typically carried out jointly by product management and product marketing teams, with close collaboration described as important - not a PM-owns/PMM-drafts split
Quotable: "Product positioning is a strategic exercise typically carried out by product management and product marketing teams. Close collaboration is important - both groups have a unique point of view on the marketplace, other solutions available, and how your own product fits in."
Quotable: "The outcome of the exercise is a product positioning document that helps everyone in the organization understand the real value you provide beyond features and functionality."

**[39] Sharebird Q&A - "How does your company define the difference between Product Management and Product Marketing teams?" (answers by Marc Abraham/Intercom, Devika Nair/Oracle, Sourav Debnath/Finmo, JJ Miclat/Zendesk).** practitioner. **fetched-and-verified.**
`https://sharebird.com/h/product-management/q/how-does-your-company-define-the-difference-between-product-management-and-product-marketing-teams-how-do-the-responsibilities-differ`
Supports: Devika Nair's full, un-truncated sentence on who treats positioning as whose responsibility; also the page's complete answer roster, for a data-integrity check against tier2-specs.md's citation of Mike Flouton and Poorvi Shrivastav on this same URL
Quotable: "Product Management primarily partners with engineering. They are responsible for what we build, and why we built it. Product Marketing is responsibile for how we position these products to the customers. While product management is also responsible for the positioning, they are looking at it as part of the vision and decision making."

**[40] Pragmatic Institute - "Product Positioning Workshop" landing page.** vendor. **fetched-and-verified.**
`https://www.pragmaticinstitute.com/workshop/product-positioning/`
Supports: Confirms, on direct re-read, that this page contains no sentence about a sectioned positioning document or section order mattering, and no statement of who owns, drafts or creates the positioning statement. It only lists which roles (Product Managers, Product Marketers, Product Owners) 'benefit' from the training
Quotable: "Product Managers Responsible for guiding the success of a product and leading the cross-functional team."
Quotable: "Product Marketers Overseeing project execution, aligning it with strategic roadmaps."
Quotable: "Product Owners In Agile teams, responsible for setting the product vision and managing the product backlog."

**[41] Institute of Product Leadership - "Product Positioning Guide".** vendor. **fetched-and-verified.**
`https://www.productleadership.com/product-positioning-guide`
Supports: A full re-read found no explicit statement of who owns, drafts or approves the positioning statement between product management and product marketing; it treats positioning generically as 'a crucial component of any marketing plan' without assigning a department
Quotable: "A well-executed positioning strategy can lead to increased brand loyalty, higher sales, and a stronger competitive advantage in the market, making it a crucial component of any marketing plan."

**[42] Douglas Karr (Martech Zone) - "How the Pragmatic Framework Empowers Product Marketing Professionals".** practitioner. **fetched-and-verified.**
`https://martech.zone/pragmatic-framework-product-marketing`
Supports: A named practitioner's account of where the Pragmatic Framework places positioning: inside the framework's 'Planning' category, described throughout as product-marketing work, with the positioning document explicitly attributed to product marketers. Fetched fresh (not previously cached) because the Pragmatic Institute's own site gave no usable ownership sentence; stored to cache via source-cache.py put
Quotable: "Product marketers’ work shines in the Planning category. Here, activities like positioning, persona development, buyer experience mapping, and use scenario planning come to life."
Quotable: "A well-crafted positioning document aligns marketing, sales, and product development around a single narrative."
Quotable: "Product marketers translate market data into messaging frameworks that inform campaigns, content, sales enablement, and thought leadership."

### BOUNDARIES AND REVISITING

**[43] Sharebird community answers (Poorvi Shrivastav, former Senior Director of Product Management, Meta; and Mike Flouton, Managing Partner, Boxford Capital, formerly Barracuda/SilverSky/Digital Guardian/OpenPages/Cybertrust) - "What differentiates a product vision statement from a positioning statement?".** practitioner. **fetched-and-verified.**
`https://sharebird.com/h/product-management/q/what-differentiates-a-product-vision-statement-from-a-positioning-statement`
Supports: (a) how positioning is separated from vision, verbatim, from two independent practitioner voices
Quotable: "So a vision and positioning statement may seem similar at first, but they're actually wildly different. Product vision is long-term, aspirational, inspiring, speaks to a broad audience, and paints a picture of what could be in the future. A positioning statement, on the other hand, is much more present-day, marketing-oriented, and is typically something that you'd write to position a feature, product, or capability towards a specific target audience."
Quotable: "A product vision statement defines the long-term goal and direction of a product."
Quotable: "It's where the product aims to be in the future, independent of the current state or competition."
Quotable: "It focuses on solving customer problems, the impact the product will have, and the desired outcome for the business."
Quotable: "A positioning statement, on the other hand, outlines how a product will be perceived in the market relative to competitors."

**[44] Rational Unified Process (RUP) Vision document template, University of Delaware CISC 475 course materials (Richard P. Decker).** practitioner. **fetched-and-verified.**
`https://www.eecis.udel.edu/~decker/courses/475s06/documents/VISION-short.dot`
Supports: (d) this canonical software-engineering source places the positioning statement AS A SUBSECTION INSIDE the Vision document, not as a separate or prior artifact - direct evidence of a source that merges/nests the two
Quotable: "Positioning"
Quotable: "Problem Statement"
Quotable: "Product Position Statement"
Quotable: "[Provide an overall statement summarizing at the highest level, the unique position the product intends to fill in the marketplace. The following format may be used:]"
Quotable: "[A product position statement communicates the intent of the application and the importance of the project to all concerned personnel.]"

**[45] The Starr Conspiracy (Bret Starr, Founder & CEO) - "Messaging Framework: Why B2B Gets It Wrong" (guide).** practitioner. **fetched-and-verified.**
`https://www.thestarrconspiracy.com/insights/guides/what-is-a-messaging-framework`
Supports: (b) explicit separation of positioning from messaging, with positioning as the input layer to a messaging framework
Quotable: "A messaging framework is an architecture that governs how your positioning translates into consistent language across every audience, channel, and moment."
Quotable: "This is your foundational differentiation, the core claim that separates you from alternatives. It's not a tagline or elevator pitch. It's the choice about how you want to be categorized in your market."
Quotable: "A positioning statement defines how you want to be perceived in the market. A messaging framework translates that positioning into specific language for different audiences and contexts. Positioning is direction; messaging is tactical."

**[46] The Starr Conspiracy - "What Are Messaging Frameworks" (comparison).** practitioner. **fetched-and-verified.**
`https://www.thestarrconspiracy.com/insights/comparisons/what-are-messaging-frameworks`
Supports: (b) and (c): the fullest single statement found anywhere in this research of a revisit TRIGGER and CADENCE - but note precisely, it is scoped to the messaging framework, not to the positioning statement itself; also gives the clearest positioning-vs-messaging-vs-value-proposition-vs-tagline hierarchy with positioning as sole input
Quotable: "A positioning statement is one input. A messaging framework is the system that turns that input into every asset your go-to-market (GTM) team ships."
Quotable: "Positioning tells you who you serve, what category you compete in, and why you win. The framework translates that into value props, proof, objection handling, and channel-specific copy"
Quotable: "Lock the positioning statement first."
Quotable: "Governance. Assign an owner. Set a review cadence (quarterly, or monthly if you're changing pricing). Define what triggers an update (new segment, new product, new competitor, new pricing)."
Quotable: "Trigger conditions that mean now, not later: new ICP, new pricing or packaging, new sales leader, a pipeline conversion drop, or a rebrand in flight."
Quotable: "Positioning should be stable for years. Value props and campaign messaging shift with market conditions."
Quotable: "A single internal statement that defines the target customer, the category, the key benefit, and the primary differentiator. One input into a messaging framework."
Quotable: "Rarely changes, so it provides long-term stability"
Quotable: ""Our positioning statement is enough." Positioning is one input. It doesn't tell a rep how to handle the "we already have a tool for that" objection on a Tuesday call."

**[47] Product Marketing Alliance - "A Practical Guide to Creating a Winning Positioning and Messaging Strategy" (based on a Masters of Product Marketing presentation, October 2022).** practitioner. **fetched-and-verified.**
`https://www.productmarketingalliance.com/a-practical-guide-to-creating-a-winning-positioning-and-messaging-strategy/`
Supports: (b) explicit statement that the positioning statement is internal and feeds messaging, which is external; also the only (vague) revisit language found in the owned PMA/Starr/Atlassian set for positioning itself
Quotable: "There's no perfect positioning strategy, and once you've established one it shouldn't be set in stone; you have to update and refresh it over time."
Quotable: "The full process has one more element: the messaging. The positioning statement is just an internal document that you'll use to guide the creation of your external messaging and everything else that goes along with it. It also helps align teams internally."
Quotable: "Your messaging is going to help you expand on your positioning statement to articulate to your buyers why you're better than the alternatives."
Quotable: "Your positioning statement - The starting point of your narrative"

**[48] Product Marketing Alliance - "Sales Battlecards: The Complete Guide [+ Examples]" (battlecards-for-the-win).** practitioner. **fetched-and-verified.**
`https://www.productmarketingalliance.com/battlecards-for-the-win/`
Supports: (b) battlecard is downstream of and reinforces positioning, not an input to it; also carries a revisit cadence but scoped to battlecards/pricing, not the positioning statement
Quotable: "Well-designed battlecards ensure reps are aligned on product positioning, can confidently differentiate your offering, and reinforce messaging consistency."
Quotable: "Update this section regularly - pricing changes are frequent and reps must always have the most up-to-date figures."
Quotable: "Instead of a quarterly refresh, AI tools can monitor competitor websites, pricing pages, and news for changes continuously, and update the relevant card automatically."

**[49] Atlassian - "Message house template" (Confluence templates).** vendor. **fetched-and-verified.**
`https://www.atlassian.com/software/confluence/templates/message-house`
Supports: (b) and (d): direct mechanical evidence that the positioning statement is the first input written into the messaging artifact (the message-house "roof"), confirming positioning precedes and feeds messaging
Quotable: "The first section of the template is called the messaging roof. It contains the at-a-glance details of your messaging. Write down the positioning statement that you put your blood, sweat, and tears into here. Then specify who that statement speaks to, i.e., who your audience is."

**[50] Product Marketing Alliance - "Product Messaging Framework Template" (free PDF download landing page).** vendor. **url-confirmed-not-read.**
`https://www.productmarketingalliance.com/product-messaging-framework-template/`
Supports: exists only as corroboration that PMA publishes a named messaging-framework template; the cached body is a lead-capture page shell with no substantive prose (confirmed by direct inspection - the fetched HTML renders to blank/UI chrome, no article text), so no claim rests on it beyond confirming the artifact's existence

**[51] CLIMB (climbtheladder.com career/business content site) - "What Is a Positioning Statement? Definition & Examples".** practitioner. **fetched-and-verified.**
`https://climbtheladder.com/what-is-a-positioning-statement-definition-examples/`
Supports: (c) the single most direct, explicit, named statement of revisit TRIGGERS for the positioning statement itself (not a vision, not messaging, not a framework) found anywhere in this research; also restates the positioning-vs-mission/tagline/value-proposition hierarchy from (b)
Quotable: "A tagline can change with a campaign. A positioning statement should stay stable for years, only shifting when your market, your competitive landscape, or your strategic direction fundamentally changes."
Quotable: "A positioning statement isn't permanent, but it shouldn't change often. Revisit it when your target market shifts meaningfully, when a new competitor changes the landscape, when you launch a product that doesn't fit the existing framework, or when customer research reveals that buyers see you differently than you intended."
Quotable: "The goal is stability with occasional recalibration, not constant reinvention."
Quotable: "If you find yourself rewriting your positioning statement every quarter, the problem likely isn't the statement. It's that the underlying strategic choices haven't been made firmly enough."
Quotable: "A mission statement describes a company's purpose. A tagline is a catchy phrase aimed at customers. A value proposition explains benefits to buyers. A positioning statement sits behind all of those, shaping what they say and how they say it."

**[52] Aberdeen Strategy & Research blog - guest post by Lawson Abinanti, founder of Messages That Matter - "3 Questions to Help You Audit Your Positioning Statement" (2017-07-31).** practitioner. **fetched-and-verified.**
`https://aberdeenclean.wpengine.com/blogposts/3-questions-help-audit-positioning-statement/`
Supports: (c) the only named source found stating an explicit fixed CADENCE (as opposed to a trigger) for revisiting the positioning statement specifically
Quotable: "It's a good idea to audit your positioning statement every 12 months."
Quotable: "Summertime is the best time to audit your positioning statement for effectiveness, and it's easy to do."

### THE GAP QUESTION

**[53] Adi Oran - "The 5 Positioning Mistakes That Kill Deals," Position & Pitch newsletter.** practitioner. **fetched-and-verified.**
`https://oranai.beehiiv.com/p/the-5-positioning-mistakes-that-kill-deals`
Supports: status quo / do-nothing as the real competitive alternative; positioning as a cross-functional team exercise
Quotable: "In B2B, about 40% of deals end in "no decision.""
Quotable: "Status quo (what they're doing now-spreadsheets, pen and paper, interns) and the short list (other solutions they're evaluating)."
Quotable: "It has inertia. It's free. It's already in place. It's often "good enough.""
Quotable: "Positioning is a team sport."
Quotable: "Get marketing, product, sales, customer success, and executives (especially the CEO) together in a room."

**[54] jmagly - "Positioning Statement Template" (STR-003), aiwg npm package, media-marketing-kit framework.** vendor. **fetched-and-verified.**
`https://unpkg.com/aiwg@2026.5.10/agentic/code/frameworks/media-marketing-kit/templates/strategy/positioning-statement-template.md`
Supports: nothing in this bundle. An AI-agent toolkit's template published on the npm registry, not a named practitioner or organization; listed because it was consulted, and none of its text is relied on

**[55] Applied Frameworks - "Positioning Your Product in the Market" (company blog, March 12, 2013).** practitioner. **fetched-and-verified.**
`https://appliedframeworks.com/blog/positioning-your-product-in-the-market`
Supports: executive sign-off reducing downstream approvals; the positioning document as the internal source for branding, promotion and sales enablement; customer interviews as the input for upgrade positioning
Quotable: "A positioning document explains your product capabilities and message to your internal teams and agencies. It's the source document for branding, promotion, and sales enablement."
Quotable: "if you can get the execs to sign off on positioning, you can reduce your internal approvals dramatically. After all, the words are pre-approved."
Quotable: "Interview some customers who have upgraded (or plan to upgrade) and what you learn will be the core of your message."
Quotable: "It's not "We are good; they are bad." It's "We are good at this; they are good at something else.""

**[56] Koji Labs B.V. - "Positioning Research: How to Validate Your Product Positioning with Customer Interviews," Koji docs.** vendor. **fetched-and-verified.**
`https://www.koji.so/docs/positioning-research-customer-validation`
Supports: a structured customer-interview protocol for testing a positioning statement before adoption (23 questions across wins/losses/never-evaluated populations), do-nothing named as one of four competitive-alternative types, market trends/trigger events as the explicit 'why now' layer, and observable buyer/org traits distinguishing a fit customer from a non-fit peer
Quotable: "Relevant Trends (optional) - the "why now" context."
Quotable: "What changed in the last 90 days that made you start looking?"
Quotable: "The trigger event is the urgency narrative. Without it, your positioning describes a destination buyers feel no need to leave for."
Quotable: "What proof would have helped you decide faster?"
Quotable: "What would be different about a peer who would NOT buy this?"
Quotable: "Dunford specifically warns against positioning against phantom competitors - competitors you've never actually lost to."
Quotable: "Wins - recent customers (90-180 days)... Losses - evaluated but didn't buy, or churned within 12 months... Never-evaluated - fit your ICP but never considered you."
Quotable: "Matthew Dixon and Ted McKenna's analysis of 2.5M+ sales conversations found 56% of those losses are indecision-driven - confusion, complexity, fear of choosing wrong - not status-quo preference (HBR, 2022)."

**[57] Ibrahim Bashir - "Why Buy?", Run the Business newsletter (Substack).** practitioner. **fetched-and-verified.**
`https://runthebusiness.substack.com/p/why-buy`
Supports: a three-part sales qualification frame (why buy anything / why buy our product / why buy right now) applied to positioning, naming timing as a distinct question from category and differentiation; only the free preview of the article was accessible, so this supports the existence and framing of the 'why buy right now' question, not a full worked-out treatment
Quotable: "Why buy anything? Why buy our product? Why buy right now?"
Quotable: "I think it nails how to think about positioning your product - and also highlights what a lot of products get wrong."

**[58] Christopher Lochhead (with Al Ramadan) - "We Need to Talk About Positioning," excerpt from The Existing Market Trap, Different newsletter (Substack).** primary. **fetched-and-verified.**
`https://lochhead.substack.com/p/the-positioning-problem`
Supports: a direct, named-author argument that a positioning statement - even filled in well - is a category-design trap: it accepts an existing market's frame rather than defining and leading a new one, which the common formula's seven slots cannot represent because they all presuppose an existing category
Quotable: "Because positioning-by definition-is about placing your company inside an existing market. It assumes the aisle already exists."
Quotable: "Positioning says: Find a big market. Build a better mousetrap. Position your better mousetrap clearly. The world will beat a path to your door. It would be awesome. If it were true. But it's not. It's a trap."
Quotable: "Positioning asks: "Where do we fit?" Category Design asks: "What kind of future are we building?""
Quotable: "Category Kings earn 76% of the market cap. Everyone else fights over what's left."

**[59] Lumen Learning - "Reading: Developing Positioning Statements," Introduction to Marketing (SUNY HCCC), Module 8 (OER course text).** academic. **fetched-and-verified.**
`https://courses.lumenlearning.com/suny-hccc-marketing/?p=193`
Supports: a business-school course statement of the common formula (confirming it matches the task's own description) plus an evaluation rubric beyond the formula: a 'substitute a competitor's name' credibility test and a 'can you actually deliver on the promise' check
Quotable: "The "reasons to believe" are any proof points or evidence that show your customers how you live up to your claims about how you are different and better."
Quotable: "If you can substitute any competitor's name for your own in the positioning statement-and it still sounds credible-then you need some additional work on your differentiators and competitive advantages."
Quotable: "You must be able to consistently live up to this promise-otherwise you'll lose credibility, and your offering will stand for something that's untrustworthy."
