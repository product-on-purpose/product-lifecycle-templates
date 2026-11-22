# product-principles: research log

Research conducted 2026-11-20. It builds on admission sweep 8 of 2026-11-14, held in a gitignored folder under
`_local/research/`, and on
[ADR 0090](../../docs/internal/decisions/0090-product-principles-joins-standing-standards-as-a-foundation.md)
(product principles joins standing-standards as a foundation). It also builds on the family contract
(`docs/internal/contracts/standing-standards.md`) and on the spec, the section of `docs/internal/tier2-specs.md`
headed "standing-standards (tenth member): product principles". The maintainer accepted ADR 0090 on 2026-11-14 and
ruled every open choice in the spec as recommended on 2026-11-20 ("ok to all"). Those rulings are: a single `lean`
size, an Acme Analytics example owned by Dana Okoro, VP Product, a pointer from the `product-strategy` one-pager's
Product Principles guidance to this bundle, and this bundle built second, after `design-principles`. This bundle is
issue #360 (bundle: product-principles), and it fills a new catalog entry, 214.

The build ran six dimensions. The working files are numbered by return order: `dim1.md` holds origins, `dim2.md`
relationships, `dim3.md` the gap question, `dim4.md` structure, `dim5.md` practice and `dim6.md` debates.

**40 sources are recorded below, and all 40 are fetched-and-verified.** By tier they are 26 practitioner, 9 vendor
and 5 primary, two of them books. The books are Marty Cagan's *Inspired* [39] and *Empowered* [40], read from the
maintainer's own copies.

## What the checks caught, and what was not read

**Every web quotation was checked against raw text**, never against a retrieval tool's summary. Of the 123 web
quotations the agents returned, 122 passed the first check. The one failure was a trim, not an invention: the
agent had changed the first word of a sentence on Intercom's page, which reads "our current set". The verbatim span replaces it in [8].

**Every book quotation was checked against the page text of the maintainer's copies.** That text has broken word
spacing and replaces apostrophes with a placeholder character, so the check ignores spaces and restores apostrophes.
One quotation from *Inspired* crossed a page break, where the printed page number sits inside the sentence. It is
shortened to the part on one page.

**The main loop carried in quotations of its own.** Admission sweep 8 had raw-checked quotations on seven of these
pages, and the spec's reads of 2026-11-17 added Productboard's revisit conditions [4] and a line from SVPG [2]. Each
was re-tested against the cached raw body when the entries below were generated.

**Bare counts were spot-checked in the main loop.** GitLab's eight principles, three of them in an "over" form [5],
and Intercom's fourteen, as four R&D, five product design and five engineering principles [7], were re-counted
against the cached pages. The other counts in the structure table are as the structure dimension read them.

**One article appears twice.** Ethan Eismann's article *Why your organization needs product principles* is entry [18], on
Slack's design site, and entry [25], on TechCrunch. They are kept as two entries because two dimensions read two
pages. They are one author's one argument, and they count as one voice.

**Repository files read, not listed as sources.** The relationships dimension read ADR 0090, the `design-principles`
guide and companion, `product-strategy_template-one-pager-full.md` (its Product Principles section, lines 157-175),
and the guides for `product-vision`, `prd`, `positioning-statement`, `trade-study` and `definition-of-done`. They are
cited below by path, not by number.

**Pages wanted and not read.** Gusto's own product principles page returned HTTP 403. Shopify's careers page for its
product principles returned 404, though a search engine lists it. A 2017 Mind the Product article that Marc Abraham
links [32] returned 404. Intercom's per-principle series was read only in Stephen Forbes's post [17]. A governance
guide that proposes a steward for a set was found in search and not read. The tail of this log lists the blocked
page.

## Findings

### What the type is

A product principles document is a short standing set of beliefs that a product team uses to resolve product
trade-offs: what to build, for whom, and what to refuse. Cagan: "Product principles complement the product vision by
stating the values and beliefs that are intended to inform the many product decisions that will need to be made."
[40] His coaching article lists them as one of six kinds of strategic context, which "is meant to apply to all
product teams in the company" [2].

Two exclusions are stated by the sources. Cagan: "Product principles are not a list of features, and they are not
tied to any one product release." [39] ProductPlan: "You don’t build principles, they guide what you decide to build
and how to build it." [22]

### Origins: from a step in a PRD to a standing artifact

**No source read names who first wrote about a team writing its own product principles.** The research names no
originator, and the companion must not either.

**The earliest source read is Cagan's PRD guide [1]**, whose "Step 4: Define your Product Principles" is one of ten
steps. Its only date is a 2005 copyright footer, and the PDF sits under a 2024 upload path. The guide already reports
earlier sets: a TiVo list and eBay's, where "at eBay the mantra was: 1) easy to use; 2) safe; and 3) fun." So the
practice predates the guide.

**Cagan's framing moved in three steps**, each tied to a source:

| Year | Scope | Author | Source |
|---|---|---|---|
| 2005 | One project: "These principles will be specific to your domain and your particular project." | The team | [1] |
| 2017 | A product line: "The principles are aligned with the product vision for an entire product line." | Not stated | [39] |
| 2020 | The strategic context for every team: "As the product leaders create the product vision, I encourage them to also prepare a set of product principles to complement the vision" | Product leaders | [40], [2] |

*Inspired* also allows a set to stay internal: "In many cases, the principles are simply a tool for the product
teams." [39] Its worked example is eBay's rule for buyers and sellers, which opens "In cases where the needs of the
buyers and the sellers conflict" [39]. Cagan's 2017 article "Principles" [3] is about principles of product
management in general, not this document. It must not be cited for the type.

### Structure: what a published set puts in each principle

| Set | Count | What each principle carries |
|---|---|---|
| GitLab [5] | 8 | A clause that is both name and statement, then reasoning. Three use an "over" form, such as "We value quality over velocity:" |
| Monzo [6] | 6, for one internal product | A name and a reasoning paragraph. Two carry a case study of a decision the principle settled |
| Intercom [7] | 14, in layers of 4, 5 and 5 | A numbered name and one to three sentences |
| Linear [9] | 7 | A name and one to three sentences. Some names carry the trade-off, such as "Simple first, then powerful" |
| Slack, via Salesforce [10] | 5 | A name, "What it means:" and "How it shows up:", a product example |
| Supabase [11] | 7 | A name and one to three sentences, some with a litmus test |
| PostHog [12] | 3 | One line each, such as "Get in first." |
| David Pereira [14] | 12, in four layers of three | A name and one sentence |
| Productboard's prompt [4] | 5, prescribed | A name, a statement, what it means in practice, what it means the team will not do, and a "TENSION" line |

**Four findings follow.** A name and a statement appear in all eight published sets tabulated; Langfuse [15], below,
has lists but no named principles. *(Narrowed 2026-11-21 from "are universal", after a Codex review.)* Reasoning inside the statement is common. An
examples field appears in two published sets, Slack and Monzo. **A field for what a principle rules out, and a
separate field for its tension, appear only in Productboard's prompt [4]**, a vendor's AI prompt. Langfuse [15]
publishes the nearest thing, a list headed "What we don't do", but as one list for the whole set.

**No source publishes a blank template other than that prompt, and none publishes a long and a short version of one
set.** Intercom pairs a short list with a post per principle, and GitLab follows its eight with a long section headed
"How we follow our Principles". Neither is two versions of one set. **A single size is supported**, as the maintainer
ruled.

**Licences.** No page read states a reuse licence. Productboard's prompt reserves its rights. **The bundle describes
the structures it found and copies no set's text.**

### Practice: use, ownership and change

**Use in review is the best-documented use.** Stephen Forbes describes Intercom's first principle in use "Not just in
product reviews, roadmap meetings, or design critiques" [17]. At Slack, "Product managers and designers at Slack
reference them in weekly workshops where projects are shared at every stage" [18]. Onboarding appears too: a new
joiner's "onboarding pack contains their first “Intermission”" [17].

**Saying no is asserted more than shown.** Pendo reports of Box: "If a feature idea doesn’t align with these
principles, then Box does not pursue it." [36] No named company source read describes a principle used to decline a
specific request. Slack limits the use: "Product principles exist to inform execution rather than roadmapping,
strategic thinking or planning" [18].

**No source names who owns a set after it is written, or who approves a later change.** LogRocket describes
leadership signing off a draft [28], and Slack says the set should be company-wide [25]. Cagan's 2020 position is
that product leaders prepare the set [40] and that "The product manager needs to understand these principles and the reasoning behind each one." [2]
Intercom's account is of organic change: principles are "guides, they’re not rules" [16].

**Intercom gives the one dated record of a set changing.** In 2019: "we have three high level principles today, we
used to have five and then we merged three of them into one" [16]. By October 2021 there were four top-level
principles, among them *Deliver outcomes* [7]. In 2022 the set was "the third major iteration since we first
introduced them about eight years ago" [8]. Intercom also says "We also update them every 1-2 years" [7], which
three iterations in eight years does not match unless wording edits count. The sources do not say which.

**Slack's set changed between two snapshots.** The 2021 list [18] and the 2026 list [10] differ by one principle.
Neither source gives a reason or a date, so this is a comparison, not a change record.

**What reopens a set.** Productboard's prompt says "These principles should be revisited when" "The company strategy
changes significantly", when "We've consistently violated one without deciding to change it", and when "A new
principle would have resolved 3+ debates in the last quarter" [4]. Intercom reopens on a valid exception, to "try and
re-codify that back in or change a principle, evolve it" [16]. Slack tunes a principle that does not take hold
[18]. Those are statements of intent, not logged events.

**Stated intervals disagree.** Guru: "The principles you write should be able to hold their ground for at least a
year" [21]. LogRocket: "Review your product principles every three months" [28], a review rather than a rewrite.
ProductPlan: "An update should be an unusual and well-considered event, not a regular occurrence." [22] **The
`foundation` classification holds**, and the Review Trigger takes conditions, not a calendar.

### Debates: strategy, lifespan, authorship, ranking and the count

**Inside the strategy or beside it?** No source read says a set should live only as a section of a strategy
document, but the sources split on how close they sit. Cagan places them beside the vision and the strategy [39]. Guru: "Product principles tie the product’s vision and
strategy together." [21] Hyperact calls them "an important asset of a solid product strategy" [33]. Product School treats them as a lens
inside product strategy [24], and Pereira groups one layer of his principles under strategy [28]. Slack keeps them
out of strategy altogether [25]. **No source ties a principle's life to one strategy period.** That is the
library's ground for a standing set, and it is the library's reading.

**Standing or per project?** This is the dispute Cagan's own writing carries. His 2005 principles are "specific to
your domain and your particular project" [1]. His 2017 principles "are not tied to any one product release" [39].
Intercom does both: "We sometimes even create principles for specific projects to get aligned on our approach up
front." [8] The bundle is the standing set. A project's own principles belong in that project's PRD.

**Whose set?** ProductPlan says "defined product principles are driven by the team itself" [22]. Product School:
"Talk to your team, not just leadership" [24]. ThoughtSpot built its set with every relevant team [27]. LogRocket
recommends "A hybrid approach works better where leadership presents a draft and sharpens the principles with the
team" [28]. Cagan's 2020 text has product leaders prepare it [40]. This is a real split.

**The truism test.** Intercom: "no principle is a truism" and "The opposite of a principle should itself be a
principle" [7]. AWS, on tenets: "To be effective a tenet needs to have an opposite which could be acceptable to an
organisation." [38] Productboard's prompt says that a principle without a reasonable opposite is not one: "it's not a
principle" [4]. The counter-view is airfocus, for which principles "should trigger an emotional response" [23]. A
moving line that nobody would oppose passes airfocus and fails Intercom.

**Ranked, or a trade-off in each principle?** ThoughtSpot stack-ranked candidates "within each category from most
to least important" [27], and ProductPlan says "The principles should clearly state what is most important." [22]
The trade-off form is the alternative. Nir Gazit: "Take a stand by preferring one alternative over the other(s)."
[26] Microsoft's patterns and practices team wrote "Quality over scope" [35]. LogRocket names Martin Eriksson's
"'even over' statements" [28]. ThoughtSpot also wrote that "it didn’t matter if some principles contradicted others"
[27]. **No source read opposes ordering outright, and none gives a worked rule for two principles that conflict.**

**How many?** Gazit: "No more than three to five principles are needed." [26] Product School: "A good set has 3-5
principles." [24] Slack: "no more than seven" [25]. ThoughtSpot: "nine is too many, five is a great number, if you
can get there" and "We landed on seven." [27] Intercom holds fourteen, in layers [7]. **None cites a measurement.**

### Relationships: design principles, company values, vision and strategy

**Design principles.** The sources split the two by scope. ProductPlan: "They also aren’t design principles",
which are "much more about implementation" [22]. airfocus: "Design principles refer purely to the design aspect of a
product" [23]. Marc Abraham: "I treat them very much as two distinct concepts" [32]. Intercom keeps five product
design principles inside its product principles [7], so one company holds both under one roof. **The library's
test is its own**, and the `design-principles` bundle already states it: a principle that settles how a screen,
message or interaction behaves is a design principle, and one that settles what the team builds, funds or declines is
a product principle (`templates/design-principles/design-principles_companion.md`, section 8). The sources' scope
test and the library's test point the same way. No source draws the library's line in its words.

**Company values.** Every source read puts values upstream and broader. Abraham calls principles "a clear set of
standards and goals that connect company values with the outcomes that we’re trying to achieve" [32]. Guru:
"Product principles are often inspired by your company's core values or mission statement" [21]. ProductPlan warns
that "A common mistake is conflating the company’s mission, product vision, and goals with product principles." [22]
No source gives a test between a value and a principle. The `product-strategy` one-pager's TRAP supplies one: values
describe how you want to behave, and principles decide arguments
(`templates/product-strategy/product-strategy_template-one-pager-full.md`). That test is the library's.

**Vision and strategy.** Cagan: "I always like to complement the product vision and product strategy with a set of
product principles." [39] Guru says principles capture what "aren’t addressed or implied in the Vision or Strategy"
[21]. The `product-strategy` one-pager full variant holds a Product Principles section (lines 157-175), which asks
for two to five rules that resolve recurring trade-offs. That section summarises the set inside a strategy. This
bundle is the set.

**PRD, trade study, definition of done, positioning statement.** Cagan's 2005 guide is the only source that relates
principles to a PRD [1], and it places project principles inside it. No source read relates product principles to a
trade study, a definition of done or a positioning statement. Every line the guide draws to those bundles is the
library's inference.

### The gap question, routed under decision procedure 12

The gap dimension did not read the spec, ADR 0090 or either principles bundle before searching. Its baseline was a
naive template with a title and a description per principle. Its candidates are routed here, not adopted wholesale.

| # | Candidate | Sources | Route |
|---|---|---|---|
| 1 | A trade-off written into the principle, and the cost it accepts | Microsoft [35], Gazit [26], Box via Pendo, "The tradeoff? Expense." [36], Eriksson via [28], Kindel [37] | A field in section 2, The trade-off it accepts |
| 2 | A test that the principle is real, not a truism | Intercom [7], [8]; AWS [38]; Productboard [4] | A guide rubric row and an anti-pattern, not a field |
| 3 | An order, or a rule, for two principles that conflict | ThoughtSpot [27], ProductPlan [22], NN/g on design principles [31] | Section 3, When Principles Conflict |
| 4 | A worked decision the principle settled | Monzo's case studies [6], Gazit [26], LogRocket's stories [28] | A field in section 2, A decision it settled |
| 5 | What the principle rules out | Box via Pendo [36], LogRocket's "Boundaries - What lines can you not cross?" [28], Langfuse [15], Productboard [4] | A field in section 2, What it rules out |
| 6 | The reasoning behind each principle | Cagan: "The product team needs to understand these principles and the reasoning behind each one." [40]; GitLab's reasoning [5] | A field in section 2, Why we hold it |
| 7 | A scope: what the set covers, and at what level | ProductPlan [22], Slack [25], Intercom's layers [7], Kindel's foundational and aspirational tenets [37] | Section 1, Purpose and Scope |
| 8 | A change record | Intercom [8], [16]; Kindel's "unless you know better ones" [37]; ProductPlan [22] | Section 5, Ownership and Changes, gains a dated change log |
| 9 | Checkpoints where the set is applied | Slack [25]; ThoughtSpot's tests in design conversations [27]; LogRocket [28] | Section 4, Using Them in Decisions |

## Claims flagged contested or time-bound

- **Standing or per project.** Cagan moved from project principles (2005) to a standing set (2017, 2020). Intercom
  does both.
- **Whose set.** Team-driven (ProductPlan, Product School, ThoughtSpot), leader-prepared (Cagan 2020), or a hybrid
  (LogRocket).
- **Memorable or arguable.** airfocus wants an emotional response; Intercom, AWS and Productboard want an opposite a
  reasonable team might choose.
- **The count.** Three to five, up to seven, or fourteen in layers. None is measured.
- **The cadence.** Quarterly review, every one or two years, or rare. Intercom's two figures fit each other only if
  wording edits count as updates, and the sources do not say whether they do.
- **Time-bound.** Slack's set changed between 2021 and 2026. Intercom's set changed in 2019 and 2021. The PRD guide's
  date rests on its footer.

## Honest framing

The bundle can say what a product principles document is, where Cagan places it, what published sets put in each
principle, and what reopens a set. It cannot say who invented the practice, how many principles is right, or that any
field beyond a name and a statement is standard. **No source other than a vendor's AI prompt publishes a template**,
so most of the template's structure is the library's POSITION. The strongest negative finding: across eight
published sets, none carries a field for what a principle rules out. Only the vendor's prompt and Langfuse's single
list come close. The template asks for it, and says it is asking for more than published sets do.

## Notes for the companion

**Load-bearing sections.** Section 2 (The Principles) is the document. Section 3 (When Principles Conflict) is where
the set decides between its own members. Section 6 (Review Trigger) is the family's obligation.

**The section design, as the spec proposed and this research tested.**

1. **Purpose and Scope.** The product or products covered, the level of the set (company, product line or product),
   its relation to the vision, the strategy and the design principles, and the principles that straddle the line with
   design principles. Gap candidate 7 lands here.
2. **The Principles.** Three to five. Each carries a statement, why we hold it, the trade-off it accepts, what it
   rules out, and a decision it settled. A name and a statement are universal; the reasoning is common and is Cagan's
   ask [40]; the trade-off form is shown by GitLab, Linear and method writers; the other two are the gap dimension's
   candidates.
3. **When Principles Conflict.** Which principle wins, in which kind of decision.
4. **Using Them in Decisions.** Where the set is applied: review, prioritisation, saying no to a request, and
   onboarding. How a decision cites a principle.
5. **Ownership and Changes.** The named owner, how anyone proposes a change, who decides, and a dated change log.
6. **Review Trigger.** A table of Condition, Owner, What They Do About It. Its conditions are sourced: the strategy
   changes significantly, a principle is consistently violated without a decision to change it, and a new principle
   would have settled repeated debates (all three from Productboard's prompt [4], attributed as a vendor's AI prompt);
   a valid exception recurs (Intercom [16]); a principle does not take hold (Slack [18]). No calendar interval is
   required.

**The sharpest teaching points.**

- A principle that no reasonable team would reverse is a truism. Intercom, AWS and Productboard agree on the test.
- The set is standing, and a project's own principles belong in its PRD. Cagan's own move from 2005 to 2017 is the
  evidence.
- The line with design principles is the library's, and the sibling bundle states it. Use the same test, in the
  other direction.
- The line with the `product-strategy` one-pager is a matter of size. A team that needs two or three rules inside its
  strategy uses the one-pager's section. A team that needs the standing set uses this bundle.

**The example.** The maintainer ruled on 2026-11-20 that the example is Acme Analytics' product principles, owned by
Dana Okoro, VP Product, who owns the vision and the strategy (`positioning-statement_example.md:18-19`). Facts it must
carry, with no contradiction:

- It is dated after the FY26 strategy (2026-01-28) and after the design principles (2026-02-03,
  `design-principles_example.md`). It may cite the persona, the vision, the strategy, the positioning statement and
  the design principles. It must not cite the Saved Views design brief (2026-06-01) or any later document.
- Its principles are consistent with the FY26 strategy's guiding policy and with what that strategy says it will not
  do (`product-strategy_example.md:59-103`). They must not restate those choices, because the principles outlive
  FY26. It must not say the strategy has changed.
- At least one principle rules out something a stakeholder has asked for.
- A Review Trigger row names the strategy changing significantly, so the link to `product-strategy` is visible.
- Its principles settle what Acme builds, funds or declines. None settles how a screen behaves, and none restates a
  design principle ("Say what a number covers", "Use the word the reader uses", "Say what to try next").
- It must not reuse "Propose, never impose", the GOOD text of the `product-strategy` one-pager template.
- All figures are labelled illustrative.

**The stop rule.** If the filled principles read as values nobody would argue against, the build stops and the
decision returns to the maintainer.

**Risks the drafting agents should hold.** Productboard's prompt [4] reserves its rights: describe its fields, copy
none of its wording. Quote Cagan only from [1], [2], [39] and [40], never from a page that quotes him. Entry [3] is
not about the type. Entries [18] and [25] are one article. The count heuristics must never be presented as measured.

## Sources

### Origins: from a step in a PRD to a standing artifact

**[1] Martin Cagan, How To Write a Good PRD (Silicon Valley Product Group, copyright 2005; PDF hosted at svpg.com uploads 2024/07).** primary. **fetched-and-verified.**
`https://www.svpg.com/wp-content/uploads/2024/07/How-To-Write-a-Good-PRD.pdf`
Supports: Step 4 'Define your Product Principles' of ten PRD steps, read in full with the surrounding text of Steps 3 to 5, the overview, the ten-step list and the author note. Every page carries the footer '2005 Silicon Valley Product Group'; that footer is the only dating evidence in the document. Shows 2005 framing: a step inside producing one product release's PRD, written by the team to guide the team 'throughout the project', with TiVo and eBay examples. I did not read Steps 6 to 10 line by line
Quotable: "It is very valuable to try and identify a set of product principles that will guide the entire team throughout the project."
Quotable: "These principles will be specific to your domain and your particular project."
Quotable: "In most teams, each product team member has some ideas in their head in terms of good principles for the product, but rarely do two people have the same ideas"
Quotable: "Step 4: Define your Product Principles"
Quotable: "at eBay the mantra was: 1) easy to use; 2) safe; and 3) fun."
Quotable: "a constant compass for the entire product team"
Quotable: "The PRD versus the Product Strategy and Roadmap"
Quotable: "The product strategy describes a vision, typically between two and five years out"

**[2] Marty Cagan, Coaching - Strategic Context (SVPG article, January 9, 2020).** primary. **fetched-and-verified.**
`https://www.svpg.com/coaching-strategic-context/`
Supports: Lists product principles as the sixth of six types of strategic context, alongside mission, scorecard, objectives, vision and strategy, and says the context applies to all product teams in the company. Confirms the standing-artifact framing in 2020 and gives a plain definition
Quotable: "The product principles complement the product vision and product strategy by stating the values and beliefs that are intended to inform many of the many product decisions that will need to be made."
Quotable: "The product manager needs to understand these principles and the reasoning behind each one."
Quotable: "is meant to apply to all product teams in the company"
Quotable: "help to illuminate the values we prioritize when we make these trade-offs"
Quotable: "illuminate the values we prioritize when we make these trade-offs"

**[3] Marty Cagan, Principles (SVPG article, 27 December 2017). It is about principles of product management in general, not the product principles document.** primary. **fetched-and-verified.**
`https://www.svpg.com/principles/`
Supports: Read in full. It is NOT about the product principles document. It explains why the 2nd edition of INSPIRED is organised around principles of product management in general and recommends Ray Dalio's Principles: Life and Work. Useful only as context for Cagan's 2017 emphasis on principles over techniques, and as a caution not to cite the URL as a source on the artifact
Quotable: "while the techniques change fairly constantly, the underlying principles endure"
Quotable: "principles of product vision and strategy"

### Structure: what a published set puts in each principle

**[4] Productboard, 'Product Principles Document' (Product Management Prompts Library).** vendor. **fetched-and-verified.**
`https://www.productboard.com/product-management-prompts-library/product-principles-document/`
Supports: The only blank structure found: a vendor AI prompt prescribing five principles, each with five fields, plus set-level sections. Footer reserves rights ('All rights reserved'); no reuse licence
Quotable: "Great principles are specific enough that they could be used to resolve an argument."
Quotable: "WHAT IT MEANS WE WON'T DO"
Quotable: "TENSION: [What this principle trades off against"
Quotable: "These principles should be revisited when"
Quotable: "The company strategy changes significantly"
Quotable: "We've consistently violated one without deciding to change it"
Quotable: "A new principle would have resolved 3+ debates in the last quarter"
Quotable: "it's not a principle"
Quotable: "TENSION"
Quotable: "Write product principles that actually guide decisions"
Quotable: "When Principles Conflict"
Quotable: "Copyright © 2026 Productboard, Inc. All rights reserved"
Quotable: "TENSION TEST: Does each principle capture a real tension or trade-off?"
Quotable: "consistently violated one without deciding to change it"
Quotable: "product_strategy: If available, use it to ensure documentation aligns with and supports strategic priorities."

**[5] GitLab, 'Product Principles' (GitLab Handbook, product section).** practitioner. **fetched-and-verified.**
`https://handbook.gitlab.com/handbook/product/product-principles/`
Supports: Eight named principles, each a bold clause (three in X-over-Y form) followed by an explanation paragraph; no examples, no separate rules-out field; a long 'How we follow our Principles' tail. No licence stated in the cached page text
Quotable: "We value quality over velocity:"
Quotable: "We value data over intuition and anecdotes:"
Quotable: "How we follow our Principles"
Quotable: "These are core principles we believe world class product organizations exhibit."
Quotable: "We value quality over velocity"
Quotable: "We are design-led"
Quotable: "We value data over intuition and anecdotes"
Quotable: "These are core principles that we believe will deliver world-class products through customer-centric innovation."
Quotable: "Last modified October 30, 2026"
Quotable: "We are design-led:"
Quotable: "GitLab’s Pajamas design system principles"
Quotable: "Consider the use of Pajamas components for UI in your MVCs."

**[6] Monzo, 'The Vision and Principles for Our Internal Product'.** practitioner. **fetched-and-verified.**
`https://monzo.com/internal-product`
Supports: Six named principles for one internal product (Customer Operations tooling), each a paragraph of reasoning; two are followed by a dated-free case study of a decision it settled; a set-level list of six purposes precedes them. No licence stated
Quotable: "Optimise for learning with simple solutions"
Quotable: "Prove it"
Quotable: "Case Study: Refunding customers during the upgrade"
Quotable: "To make sure we’re consistent in how we approach problems and build our product to achieve our vision, we have a set of principles."
Quotable: "empower everyone to make decisions autonomously"
Quotable: "evaluate new ideas and solutions by clearly putting them in perspective"
Quotable: "steer group discussions into the right direction and make them more productive"
Quotable: "Care about our platform contributors"

**[7] Des Traynor (Intercom), 'Foundations to build on: Intercom's principles for building product', 20 October 2021.** practitioner. **fetched-and-verified.**
`https://www.intercom.com/blog/intercom-product-principles/`
Supports: Intercom's set as of 20 October 2021: fourteen principles in three tiers, four R&D principles that everyone inherits (Start with the problem; Think big, start small, learn fast; Ship fast, ship early, ship often; Deliver outcomes), five product design principles and five engineering principles. Each is a numbered name plus one to three sentences, with no examples and no rules-out field. It states the test that the opposite of a principle should itself be a principle, and the only stated revision interval found, an update every one to two years. No licence stated
Quotable: "The opposite of a principle should itself be a principle"
Quotable: "We also update them every 1-2 years"
Quotable: "no principle is a truism"
Quotable: "update them every 1-2 years"

**[8] Connolly, Emmet (Intercom). Introducing Intercom's product principles. Intercom blog, 2022-02-09.** practitioner. **fetched-and-verified.**
`https://www.intercom.com/blog/product-principles/`
Supports: The opposite-flip test for truisms; principles are explicitly not rules; revision history (third major iteration in about eight years); layered sets (R&D, Product Design, Engineering, project-specific); rationale and worked examples published per principle in a follow-on series; Same 14 principles as names only, with a stated plan to publish one deep-dive post per principle (a short list plus a long form per principle); the third major iteration in about eight years. I read this overview, not the per-principle posts. No licence stated; Dated count of revisions (third major iteration in about eight years); principles used for onboarding newcomers and in assessing and debating options; project-specific principles; principles valued over process; Standing set plus occasional per-project principles; flip-it-around litmus test for truisms; principles are not rules; third major iteration in about eight years
Quotable: "Principles are not rules - they exist to guide, not control."
Quotable: "A good litmus test here is to flip the principle around to express the exact opposite and see if it holds up."
Quotable: "the third major iteration"
Quotable: "is the third major iteration since we first introduced them about eight years ago"
Quotable: "We sometimes even create principles for specific projects to get aligned on our approach up front."
Quotable: "flip the principle around to express the exact opposite"
Quotable: "our current set of Intercom R&D principles is the third major iteration since we first introduced them about eight years ago"

**[9] Linear, 'Principles & Practices' (Linear Method).** practitioner. **fetched-and-verified.**
`https://linear.app/method/introduction`
Supports: Seven principles (name plus one to three sentences, no examples) kept separate from thirteen 'Practices'; a few carry a sequence or contrast in the name. No licence stated
Quotable: "Simple first, then powerful"
Quotable: "Decide and move on"

**[10] Niki Bamford (Salesforce blog for Slack), Slack product design principles article.** vendor. **fetched-and-verified.**
`https://www.salesforce.com/blog/slack-product-design-principles/`
Supports: A marketing article dated March 24, 2026 on Salesforce's blog for Slack. Five principles, each with a name, a one-line gloss, 'What it means' and 'How it shows up', a product example. The page calls them product principles, but the URL and the context lean toward design. Against Slack's 2021 list [18], Seek the steepest part of the utility curve appears where Don't reinvent the wheel stood, and Take bigger, bolder bets is reworded. No reason is given for either change. The footer reserves all rights
Quotable: "What it means:"
Quotable: "How it shows up:"
Quotable: "Product principles are the shared language between product, engineering, design, and research."

**[11] Supabase, 'Architecture' (docs), section 'Product principles'.** practitioner. **fetched-and-verified.**
`https://supabase.com/docs/guides/getting-started/architecture`
Supports: Seven principles, each a name plus one to three sentences; some add a litmus test or a stated sacrifice. No licence stated for the page (licences shown on the page belong to Supabase's tools, not its text)
Quotable: "Everything works in isolation"
Quotable: "Less, but better."

**[12] Ian Vanagas (PostHog), 'How we decide what to build', 10 January 2024.** practitioner. **fetched-and-verified.**
`https://posthog.com/newsletter/how-we-decide-what-to-build`
Supports: Three one-line principles for what to build, inside an article that argues principles make it easier to say no. No fields beyond the line. No licence stated
Quotable: "Get in first."

**[13] Tobias Freudenreich (Mind the Product), 'Using principles to make better decisions faster by Martin Eriksson', 15 August 2022.** practitioner. **fetched-and-verified.**
`https://www.mindtheproduct.com/overcoming-decision-overload-using-principles-to-make-better-decisions-faster-by-martin-eriksson/`
Supports: A product leader's form guidance, not a set: principles written as 'even over' trade-offs. Three sample lines only. The page reserves rights (Pendo copyright)
Quotable: "Conversion even over revenue"

**[14] David Pereira (Untrapping Product Teams), 'How to Implement Product Principles so You Stop Struggling with Decisions'.** practitioner. **fetched-and-verified.**
`https://dpereira.substack.com/p/implementing-product-principles-effectively`
Supports: A product leader's own twelve principles in four layers of three, each a name plus one sentence in a 'name : sentence' form; recommends 'even over' form (citing Eriksson) and a three-monthly review. Page © David Pereira; no reuse licence
Quotable: "Evidence talks louder than opinions"

**[15] Langfuse handbook, 'Product Engineering Principles'.** practitioner. **fetched-and-verified.**
`https://langfuse.com/handbook/product-engineering/principles`
Supports: Counter-example: titled principles but built as 'What we do' and 'What we don't do' bullet lists with no named principles. Shows a rules-out structure only. © ClickHouse; no reuse licence
Quotable: "What we don't do"

### Practice: use, ownership and change

**[16] Des Traynor (with Paul Adams), Intercom on Product: The principles behind how we build (podcast and transcript), 25 July 2019.** practitioner. **fetched-and-verified.**
`https://www.intercom.com/blog/podcasts/intercom-on-product-ep04`
Supports: Intercom's own account of how its principles are used (design and product reviews, scope documents, posters, leaders held to them) and of how the set changed: five top-level principles merged to three, a proposed outcome principle, new principles pressure-tested
Quotable: "we have three high level principles today, we used to have five and then we merged three of them into one"
Quotable: "they evolve very slowly"
Quotable: "these are guides, they’re not rules"
Quotable: "try and re-codify that back in or change a principle, evolve it"
Quotable: "Is it helping us make decisions faster"

**[17] Stephen Forbes, Intercom's product principles: Start with the problem to achieve better solutions, Intercom Blog, 5 October 2022.** practitioner. **fetched-and-verified.**
`https://www.intercom.com/blog/intercom-product-principles-start-with-the-problem/`
Supports: A principle used in product reviews, roadmap meetings, design critiques, Friday show-and-tells and in the new-joiner onboarding pack (first problem statement, called an Intermission); the principle is said to give permission to focus on problems and to shape how time is spent
Quotable: "Not just in product reviews, roadmap meetings, or design critiques"
Quotable: "their onboarding pack contains their first “Intermission”"

**[18] Ethan Eismann (VP of Product Design, Slack), Why your organization needs product principles, Slack Design (first published on TechCrunch; the TechCrunch URL carries 2021/03/01).** practitioner. **fetched-and-verified.**
`https://slack.design/articles/why-your-organization-needs-product-principles/`
Supports: Slack's 2021 set of five (including Don't reinvent the wheel); weekly workshops where PMs and designers cite principles; principles inform execution, not roadmapping; company-wide rollout; the keep, tune or drop stance on evolution. The slack.design page text did not show a publication date; 2021 is inferred from the TechCrunch URL
Quotable: "Product managers and designers at Slack reference them in weekly workshops where projects are shared at every stage"
Quotable: "Product principles exist to inform execution rather than roadmapping, strategic thinking or planning"
Quotable: "If a principle doesn’t take hold, it’s important to observe how it’s being used in the business and tune it based on your findings."

**[19] Ben Brignell (curator), Slack Product Principles, principles.design (reproduces Slack's set, citing Slack's own article as source).** practitioner. **fetched-and-verified.**
`https://principles.design/examples/slack-product-principles`
Supports: Corroborates the 2021 five-principle list as published by Slack. A curator's secondary copy (reference-grade), not used for process claims

**[20] Department of Product, Product Principles - Examples for Product Managers (author and date not shown in extracted text).** practitioner. **fetched-and-verified.**
`https://departmentofproduct.com/blog/product-principles-examples-for-product-managers`
Supports: Secondary commentary only: lists strategic, technical and customer-expectation triggers for re-evaluating principles and repeats Intercom's 1-2 year cadence. Not an owner's account of its own use

**[21] Guru, 'How Good Product Principles Support Your Workflow and Team'.** vendor. **fetched-and-verified.**
`https://www.getguru.com/blog/how-good-product-principles-support-your-workflow-team`
Supports: Principles tie vision and strategy together; vision is outward positioning, strategy is internal steps with metrics, principles are neither; principles often inspired by company values but loosely parallel them; principles should last about a year; goals and metrics belong elsewhere. Contains an unattributed quoted definition that principles capture things not addressed in the Vision or Strategy; A vendor's general guidance that principles are not revised every month or quarter and should hold for at least a year. Advice, not a record of Guru revising its own set; Principles are distinct from vision and from strategy and sit between them; whole-company audience; 3 to 5 ideas; Guru has five
Quotable: "Product principles tie the product’s vision and strategy together."
Quotable: "aren’t addressed or implied in the Vision or Strategy"
Quotable: "Product principles are often inspired by your company's core values or mission statement"
Quotable: "The principles you write should be able to hold their ground for at least a year"
Quotable: "3 to 5 ideas"

### Debates: strategy, lifespan, authorship, ranking and the count

**[22] ProductPlan, 'How to Define Your Product Principles'.** vendor. **fetched-and-verified.**
`https://www.productplan.com/learn/product-principles/`
Supports: Principles are distinct from mission, vision, goals, metrics, requirements and design principles; a principle is never 'reached'; the big picture is shaped by corporate strategy, market dynamics and product principles; Scope statement of what a principle is not (mission, vision, goals, metrics, requirements, design principles); a principle is never 'reached'; the ability to point back to a principle to justify a decision; prioritization as a component; revision should be rare; Principles distinct from mission/vision/goals/KPIs; asks for prioritization and a handful at most; says updates should be rare; says principles are team-driven
Quotable: "A common mistake is conflating the company’s mission, product vision, and goals with product principles."
Quotable: "You don’t build principles, they guide what you decide to build and how to build it."
Quotable: "They also aren’t design principles"
Quotable: "much more about implementation"
Quotable: "A product principle is never “reached.”"
Quotable: "An update should be an unusual and well-considered event, not a regular occurrence."
Quotable: "there shouldn't be more than a handful"
Quotable: "The principles should clearly state what is most important."
Quotable: "defined product principles are driven by the team itself"
Quotable: "no room for vague statements and ambiguous platitudes"

**[23] airfocus, 'What Are Product Principles? Definition & FAQ'.** vendor. **fetched-and-verified.**
`https://airfocus.com/glossary/what-are-product-principles/`
Supports: Product principles span the whole development cycle; design principles are scoped to the design aspect (workflow, layout, look and feel). Also says principles bake company values into products; Counter-position on specificity and lifespan: principles should be simple, emotive, not specific, and should keep evolving; notes long-lived principles can leave a business building outdated products
Quotable: "Product principles guide the entire product development cycle."
Quotable: "Design principles refer purely to the design aspect of a product"
Quotable: "should trigger an emotional response"
Quotable: "Sticking with the same principles over a long time can be helpful for conveying brand identity"
Quotable: "relevant, constantly adapting to the market and customer needs"

**[24] Product School (Carlos Gonzalez de Villaumbrosia), 'Product Principles That Drive Great Products' (Aug 2025).** vendor. **fetched-and-verified.**
`https://productschool.com/blog/product-strategy/product-principles`
Supports: Principles as a decision lens for trade-offs, align teams on 'how to build, not just what to build'; says principles 'support the product strategy'; examples (Slack, Intercom, Instagram, Amazon, Airbnb) include design- and trust-flavoured principles, showing the product/design line is crossed in practice. Examples are the author's characterisations, not verified against company sources; Examples of 'how it's applied' and 'why it works' per principle; the claim that principles make trade-offs easier to navigate. Its company attributions could not be matched to the primary sources read (see contested); Set size 3-5; principles drawn from the whole team rather than leadership alone; principles as a lens inside product strategy; principles are for trade-offs
Quotable: "Good principles don’t remove trade-offs-but they make them easier to navigate."
Quotable: "A good set has 3-5 principles."
Quotable: "Talk to your team, not just leadership"
Quotable: "If you can't say it in under 10 words"

**[25] Eismann, Ethan (Slack). Why your organization needs product principles. TechCrunch, 2021-03-01.** practitioner. **fetched-and-verified.**
`https://techcrunch.com/2021/03/01/why-your-organization-needs-product-principles/`
Supports: Slack's five principles; a stated product philosophy precedes the principles; a screening checklist of questions; a cap on count; a rollout and checkpoint mechanism; principles are never static; Principles inform execution, not strategy or roadmapping; company-wide ownership; cap of seven (Slack has five); principles are never static
Quotable: "Product principles exist to inform execution rather than roadmapping, strategic thinking or planning."
Quotable: "it’s critical to designate clear checkpoints for assessing your work against the principles"
Quotable: "Product principles should be company-wide, not siloed into the product or design team."
Quotable: "no more than seven"
Quotable: "product principles remain a work-in-progress and are never static"

**[26] Gazit, Nir. Applying product principles to guide better product decisions. Mind the Product, 2017.** practitioner. **fetched-and-verified.**
`https://www.mindtheproduct.com/applying-product-principles-guide-better-product-decisions`
Supports: Do/Don't guidance: take a stand by preferring one alternative; name the trade-off (Klarna conversion vs profitability); principles describe how to build, not what to build; three to five principles; principles evolve (Amazon example); and a worked decision (Pay.com CVC display settled by the security principle); Principles must take a stand; no more than three to five; principles can change (Amazon example); principles are not a roadmap
Quotable: "Take a stand by preferring one alternative over the other(s)."
Quotable: "No more than three to five principles are needed."
Quotable: "Product principles are not the 10 Commandments. They can change."
Quotable: "Product principles are not the 10 Commandments."

**[27] ThoughtSpot product team. How We Crafted Our Product Principles. ThoughtSpot blog.** practitioner. **fetched-and-verified.**
`https://www.thoughtspot.com/blog/how-we-crafted-our-product-principles`
Supports: Process for building a set (audience, quality criteria, brainstorm, stack-rank within categories, feedback rounds, testing in design conversations, socialisation); an explicit audience beyond designers; an acknowledged view that contradicting principles are acceptable if balanced; the count debated (landed on seven, may refine); Cross-functional team built the set; contradicts a floor of three; settled on seven; stack-ranked candidates within categories
Quotable: "it didn’t matter if some principles contradicted others"
Quotable: "Finally, we tested them, injecting them into product design conversations"
Quotable: "nine is too many, five is a great number, if you can get there"
Quotable: "stack-ranking them within each category from most to least important"
Quotable: "We landed on seven."

**[28] Pereira, David. How to define and implement product principles. LogRocket Blog, 2024-09-23.** practitioner. **fetched-and-verified.**
`https://blog.logrocket.com/product-management/product-principles-guide/`
Supports: Prerequisites that precede principles (ideal customer, experience level, boundaries, quality standards); top-down vs bottom-up authorship with leadership sign-off; routine review by usage, benefits, struggles and stories; categories (strategy, discovery, delivery, collaboration); 'even over' form attributed to Martin Eriksson; Top-down, bottom-up and hybrid authorship; 'even over' statements to express trade-offs; three-month review; principles layered by category including strategy
Quotable: "Boundaries - What lines can you not cross?"
Quotable: "Stories - Look for real stories where principles helped you and why so you can leverage that."
Quotable: "A hybrid approach works better where leadership presents a draft and sharpens the principles with the team"
Quotable: "Review your product principles every three months"
Quotable: "'even over' statements"

**[29] Glitch (blog, author not named on page). "Principle-led Product Development", 8 Feb 2018.** practitioner. **fetched-and-verified.**
`https://blog.glitch.com/post/principle-led-product-development`
Supports: Principles set at the start of one product and consulted for years (Trello); principles must be balanced against learning
Quotable: "starting not just with the problem to be solved, but a short list of product principles"
Quotable: "And they referred back to these principles as they continued to develop it, even years later."

**[30] Salesforce UX (Medium). "Defining Principles to Drive Design Decisions".** practitioner. **fetched-and-verified.**
`https://medium.com/@salesforce/defining-principles-to-drive-design-decisions-811a85032c56`
Supports: The strongest case for a ranked set (design principles for Lightning, four ranked by thought experiment). Design, not product, principles
Quotable: "we stack-ranked them"
Quotable: "giving our principles a clear order has made all the difference"

**[31] Nielsen Norman Group. Crafting Product-Specific Design Principles to Support Better Decision Making.** practitioner. **fetched-and-verified.**
`https://www.nngroup.com/articles/design-principles/`
Supports: A method for identifying common trade-offs before writing principles; principles must not conflict with one another; a principle should say why the value matters to users. This is a design-principles source and is used here only as a method analogue; Middle position between global ranking and none: principles must not conflict, and where two matter, state the context in which each wins
Quotable: "Not conflict with one another"
Quotable: "Inspire empathy"
Quotable: "then clearly specify in which contexts one of these principles is more important than the other"
Quotable: "value statements that frame design decisions"
Quotable: "with your design system"
Quotable: "specific to the product or service"
Quotable: "vision statements"
Quotable: "Product design principles (or, in short, design principles) are value statements that describe the most important goals that a product or service should deliver for users and are used to frame design decisions."
Quotable: "Having many people write a version of a design principle for each value can help to generate many good ideas."
Quotable: "having 10 or more leads to many being forgotten"
Quotable: "use the principles to explain and justify design decisions"
Quotable: "Identify Any Common Tradeoffs"
Quotable: "Often, product design principles are referred to as"

### Relationships: design principles, company values, vision and strategy

**[32] Marc Abraham, 'My Product Management Toolkit (34): Product Principles' (2019).** practitioner. **fetched-and-verified.**
`https://marcabraham.com/2019/01/11/my-product-management-toolkit-34-product-principles/`
Supports: Values, product principles and design principles as three layers; product principles connect company values to outcomes; he separates product from design principles while noting others use them interchangeably; Shopify example derives principles from its mission
Quotable: "a clear set of standards and goals that connect company values with the outcomes that we’re trying to achieve"
Quotable: "Design principles - Specific principles that drive product design"
Quotable: "I treat them very much as two distinct concepts"

**[33] Hyperact, 'Product Principles for Better Decision Making'.** vendor. **fetched-and-verified.**
`https://www.hyperact.co.uk/blog/product-principles`
Supports: Three-way split of product, engineering and design principles; principles as an asset of a product strategy; a workshop step that begins from existing vision, mission, goals, positioning artefacts
Quotable: "Product principles are an important asset of a solid product strategy"
Quotable: "engineering principles focus on the technical implementation"

**[34] Anna Bradley-Smith, The Org, 'What is the Role of Principles in Product Work?' (Apr 2023).** vendor. **fetched-and-verified.**
`https://theorg.com/iterate/role-of-principles-in-product-work`
Supports: Principles are not the company mission and goals and inform execution rather than long-term roadmapping; 'principles of product design' are scoped to the design phase; the page itself blurs the two by saying principles guide 'product and design work'
Quotable: "Principles of product differ slightly to product principles, as they refer strictly to the design phase of a product."

### The gap question: trade-offs, tests, cases and a change record

**[35] Meier, J.D. (Microsoft patterns & practices). patterns & practices Guiding Principles. Microsoft Learn archive blog, last updated 2006-06-20.** practitioner. **fetched-and-verified.**
`https://learn.microsoft.com/en-us/archive/blogs/jmeier/patterns-practices-guiding-principles`
Supports: The 'X over Y' contrast form, modelled on the Agile Manifesto, derived from outcomes to move away from and outcomes to achieve; principles as a way to govern actions without a rule for every situation. The page lists ten items, mixing contrast pairs and non-contrast statements
Quotable: "Quality over scope"
Quotable: "contrasts one value over another"

**[36] Wilkinson, Erin (Pendo). Using Product Principles to Guide Your Decision-Making. Pendo ProductCraft blog, 2020-06-12.** vendor. **fetched-and-verified.**
`https://www.pendo.io/pendo-blog/using-product-principles-to-guide-your-decision-making`
Supports: Box's seven principles each published with a 'Versus' (what is given up in preference) and a named cost ('The tradeoff?'); a principle is applied as a go/no-go filter on feature ideas; autonomy rationale
Quotable: "If a feature idea doesn’t align with these principles, then Box does not pursue it."
Quotable: "The tradeoff? Expense."

**[37] Kindel, Tig. Tenets. tig.log blog, 2020-02-10 (page shows later update).** practitioner. **fetched-and-verified.**
`https://blog.kindel.com/2020/02/10/tenets/`
Supports: Amazon-style tenets: foundational vs aspirational kinds; the 'unless you know better ones' revision invitation; 'tenets for tenets' (one main idea, minimal cover, present tense, takes a stand, specific to the endeavor); tenets exist to settle questions that cannot be verified factually; tenets at several levels (company, org, team, project)
Quotable: "unless you know better ones"
Quotable: "Foundational"
Quotable: "Aspirational"

**[38] AWS Executive in Residence Blog (author name not captured in the extract). Tenets: supercharging decision-making. AWS Cloud Enterprise Strategy Blog.** practitioner. **fetched-and-verified.**
`https://aws.amazon.com/blogs/enterprise-strategy/tenets-supercharging-decision-making`
Supports: A tenet needs a plausible opposite; tenets are ordered by priority with a rule of thumb of no more than seven; tensions between tenets are expected and need judgement; a decision-maker translation ('what does this mean to a decision-maker') accompanies a tenet
Quotable: "To be effective a tenet needs to have an opposite which could be acceptable to an organisation."

### Books read from the maintainer's own copies

**[39] Marty Cagan - Inspired: How to Create Tech Products Customers Love, second edition (Wiley, 2017), chapter 27, "Product Principles" (printed pages 135-136).** primary (book). **fetched-and-verified, read from the maintainer's own copy on 2026-11-20.**
No URL: a copyrighted book, read from a PDF the maintainer supplied from their own library on 2026-11-05; a download link would imply a retrieval that did not happen, and the text is never committed.
Supports: Cagan's 2017 framing of product principles as a standing artifact of their own, in the book's vision and strategy part: they complement the product vision and the product strategy, speak to the nature of the products a team wants to create, are not a list of features and are not tied to one release, and are aligned with the vision for a whole product line. A set may stay an internal tool for the product teams or be published. The worked example is eBay's principle that the buyer's needs come first when buyers' and sellers' needs conflict.
Quotable: "I always like to complement the product vision and product strategy with a set of product principles."
Quotable: "the product principles speak to the nature of the products you want to create"
Quotable: "Product principles are not a list of features, and they are not tied to any one product release."
Quotable: "The principles are aligned with the product vision for an entire product line."
Quotable: "it's more about what the company and product teams believe is important"
Quotable: "In cases where the needs of the buyers and the sellers conflict"
Quotable: "In many cases, the principles are simply a tool for the product teams."

**[40] Marty Cagan - Empowered: Ordinary People, Extraordinary Products (Wiley, 2020), chapter 39, "Product Principles and Ethics" (printed pages 201-202).** primary (book). **fetched-and-verified, read from the maintainer's own copy on 2026-11-20.**
No URL: a copyrighted book, read from a PDF the maintainer supplied from their own library on 2026-11-05; a download link would imply a retrieval that did not happen, and the text is never committed.
Supports: Cagan's 2020 framing: product principles are part of the strategic context that product leaders give empowered teams, prepared by those leaders alongside the product vision. They state the values and beliefs meant to inform product decisions, and they illuminate which values come first in a trade-off. The team needs to understand each principle and its reasoning. The chapter adds ethics guidance. A footnote reports that teams say the principles are the part of the strategic context they use most often in discovery, which is Cagan's report, not a measurement.
Quotable: "Product principles complement the product vision by stating the values and beliefs that are intended to inform the many product decisions that will need to be made."
Quotable: "So many decisions revolve around trade-offs, and the product principles help to illuminate the values we prioritize when we make these trade-offs."
Quotable: "The product team needs to understand these principles and the reasoning behind each one."
Quotable: "As the product leaders create the product vision, I encourage them to also prepare a set of product principles to complement the vision"
Quotable: "Product teams often tell me that the product principles are the part of the strategic context that they use most often in their daily discovery work"
Quotable: "The principles reflect the values of the organization"

## Pages not read under the terms rule

Since 2026-11-14 this section holds pages behind a login, a paywall or a bot block, not pages barred by a site's
terms. The research agents found the page below and could not read it. The maintainer has not read it by hand. No
claim or quotation in this bundle rests on it, and the maintainer may read it by hand.

- `https://gusto.com/company-news/product-principles-we-live-by-at-gusto`: it returned HTTP 403 to an automated
  fetch. It would have given Gusto's own text and fields for its five product principles, which ProductPlan [22]
  names only by title.
