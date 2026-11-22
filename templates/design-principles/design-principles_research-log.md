# design-principles: research log

Research conducted 2026-11-20. It builds on admission sweep 8 of 2026-11-14, held in a gitignored folder under
`_local/research/`, and on
[ADR 0089](../../docs/internal/decisions/0089-design-principles-joins-standing-standards-as-a-foundation.md)
(design principles joins standing-standards as a foundation). It also builds on the family contract
(`docs/internal/contracts/standing-standards.md`, 0.8.0) and on the spec, the section of
`docs/internal/tier2-specs.md` headed "standing-standards (ninth member): design principles". The maintainer accepted
ADR 0089 on 2026-11-14, ruled every open choice in the spec as recommended on 2026-11-20 ("ok to all"), and asked for
this build the same day. Those rulings are: a single `lean` size, an Acme Analytics example paired with the sibling
`product-principles` bundle, the aliases "UX design principles" and "experience principles", and this bundle built
first of the pair. This bundle is issue #359 (bundle: design-principles), and it fills a new catalog entry, 213.

The build ran six dimensions. The working files are numbered by return order: `dim1.md` holds origins, `dim2.md`
structure, `dim3.md` practice, `dim4.md` relationships, `dim5.md` debates and `dim6.md` the gap question.

**26 sources are recorded below, and all 26 are fetched-and-verified.** By tier they are 17 practitioner, 4 primary,
4 vendor and 1 reference, a mirror.

## What the checks caught, and what was not read

**Every quotation was checked against raw text**, never against a retrieval tool's summary. Of the 120 quotations the
agents returned, 116 passed the first check, five of them only after markup was stripped. Two of the failures, both
from Alla Kholmatova's slides [3], are not used. A third, a heading from Jared Spool's article [4], passed once its
apostrophes were normalised. A bare count copied from the principles.design home page [2] was dropped by choice,
because a number with no sentence around it supports nothing.

**The main loop carried in quotations of its own.** Admission sweep 8 had already raw-checked quotations on eight of
these pages, and the spec's own reads of 2026-11-17 added more on NN/g [1], [23] and principles.design [18]. Each was
re-tested against the cached raw body when the entries below were generated. 163 quotations stand in the entries.

**Repository files read, not listed as sources.** The relationships dimension read ADR 0089, ADR 0090 (product
principles joins standing-standards), `product-strategy_template-one-pager-full.md` lines 157-175 (its Product
Principles section), the `design-brief` guide and lean template, the `definition-of-done` guide and the
`product-vision` guide. They are cited below by path, not by number.

**Pages wanted and not read.** Atlassian's own principles pages returned a script redirect and then a sign-in page,
so its set is read only through the principles.design mirror [25]. One UX Collective essay returned HTTP 403. A
second, Ian Batterbee's essay on the design principle paradox, returned 403 to the debates dimension and was later fetched
by the gap dimension, but no agent read it, so nothing rests on it. The
field guide on principles.design [10] is a sales page for a paid PDF, so its "anatomy" chapter and its worksheets were
not read. GitLab's condensed principles PDF and the NHS poster were linked but not opened. Kholmatova's book chapter
was not found in a readable form, so only her 2018 slides [3] stand for her. The tail of this log lists the blocked
pages.

**Cache hygiene.** The gap dimension stored several pages in the source cache before finding that they held no
principles: two `atlassian.design` redirects, a `go.atlassian.com` sign-in page, a Shopify Polaris reference page and
an empty Firefox Photon shell. It also cached three pages it did not read. No entry below rests on any of them.

## Findings

### What the type is

A design principles document is a short list of value statements that a team agrees once and then uses to frame and
settle decisions about its product's experience. NN/g's definition: "Product design principles (or, in short, design
principles) are value statements that describe the most important goals that a product or service should deliver for
users and are used to frame design decisions." [1] principles.design defines them the same way: "Design principles are
clear statements that help teams make consistent decisions and trade-offs when designing products, services, or
systems." [2]

Two exclusions are stated by the sources themselves. NN/g says "product design principles are different from
principles of good design, such as usability guidelines, heuristics, or visual-design principles", and that "they are
not directions on how to design specific UI elements (like design patterns or standards)" [1]. Ben Brignell draws the
same line: "The principles of design belong to craft and execution." and "Design principles belong to direction and
judgement." [19]

### Origins: a convergence of practitioner writing, with no founding text

**No source read names who first wrote about a team writing its own design principles, or when.** The research
therefore names no originator, and the companion must not either.

What the dated sources show is a practice already established by the early 2010s:

- **Jared Spool's article on six counter-intuitive tests for design principles is dated 1 March 2011** [4], the
  earliest dated method piece read.
- **GOV.UK's set was first published on 3 April 2012** [13]. The 2025 blog post says the principles "have been guiding
  the design for government services since their creation in 2012" [14]. This research cannot say it was the first
  public set.
- **Kholmatova's 2018 talk** [3] lists earlier writing by Spool ("Creating Great Design Principles Jared M. Spool") and
  Stephen Anderson ("Principles To Build By Stephen Anderson") without dates, and quotes a GDS principle ("This is for
  everyone - Government Digital Service").
- **NN/g's article is dated 2 August 2020** [1]. It is a definition and method source, not an origin.

principles.design [2] is a maintained collection of published sets. It also lists a "Fisher-Price Toy Making
Principles" set by "Irving Price and Helen Schelle", which no source read dates.

### Structure: what a published principle carries

**Set sizes vary from three to eleven.** IBM has four [8], USWDS five [6], Microsoft five [9], GitLab Pajamas ten [5],
the NHS ten [7] and GOV.UK eleven [13]. The Atlassian mirror [25] and Spotify's 2020 set [17] have three each.
Productboard's design principle prompt asks the model to "generate 4-6 design principles" [11].

**The sets differ in what each principle carries, as well as in how many principles they hold.** *(Corrected
2026-11-20: this line first said the fields vary more than the count, a comparison nothing measured.)*

| Set | Fields per principle |
|---|---|
| GitLab Pajamas [5] | A title, a one-line statement, a reviewer question ("When designing any feature, ask:"), practice bullets and an "Example in practice" |
| USWDS [6] | A statement paragraph, "Key considerations" (questions for the team), "Practical actions" and "Further reading" |
| NHS [7] | A short imperative title and one to four sentences |
| IBM [8] | A two-word title, a paragraph, and four to six yes-or-no questions, such as "Is it IBM to do? Is it essential? Is it opinionated?" |
| Microsoft [9] | A one-word name and a sentence or two in the user's voice |
| Productboard prompt [11] | A name, a statement, the principle in action, "What it rules out:", and a trade-off written as one thing over another |

**Three findings follow from the table.** A reviewer's question is common: three of the five published sets read
carry one per principle. A field for what a principle rules out appears only in Productboard's prompt [11], which is a
vendor's AI prompt, not a published set or a template. **No set read carries a field for the evidence behind each
principle.** USWDS's "Further reading" [6] comes closest.

**No source publishes a blank template, and none publishes a fuller and a shorter version of one set.** The only
condensed forms are a GitLab PDF, "A condensed version of these principles for easy reference." [5], and an NHS poster
[7]. Neither was opened. **A single size is therefore supported**, as the maintainer ruled.

**Licences.** Two pages read state a reuse licence. The NHS page says "All content is available under the Open
Government Licence v3.0, except where otherwise stated." [7] The GOV.UK page carries the same footer, naming the Open
Government Licence v3.0 "except where otherwise stated" [13]. *(Corrected 2026-11-21: this line first named the NHS
page alone. A Codex review found the footer in the cached GOV.UK page.)* Productboard reserves its rights: "Copyright © 2026
Productboard, Inc. All rights reserved." [11] A scan of every cached body on 2026-11-21 found copyright lines or
rights reservations on several more, among them NN/g [1], [23], Center Centre [4], IBM [8], GitLab [15] and Clearleft
[26], and no reuse licence other than the two above. A reservation is not a licence, which is not proof that none
exists elsewhere on those sites. **The bundle describes the structures it found and copies no set's text.**

### Practice: how a set is applied, owned and changed

**A set changes rarely, and on an event, not a calendar.** GOV.UK's update history records three entries in thirteen
years: "First published" on "3 April 2012", "Updated illustrative blog posts added." in 2019, and "A principle about
minimising environmental impact has been added to the Government Design Principles." on "2 April 2025" [13]. The
2025 addition came from a cross-government working group, and its authors wrote "We facilitated 2 workshops" [14].
Afterwards, "we're now looking for someone to create an 11th poster, and to update the other 10" [14]. The NHS page
says "Updated: April 2023" [7]. **No source read states a revision interval.** The `foundation` classification holds,
and no cadence tension of the kind ADR 0088 (platform and device support matrix joins standing-standards) recorded
arises here.

**Sets are replaced as well as amended.** Spotify replaced its 2013 set in 2020 after an audit that named its defects,
among them "Overlapping concepts" [17]. Spool expects that "old principles will need to go into storage" [4]. Jeremy
Keith writes that "Prioritisation isn't and shouldn't be a one-off exercise." [26]

**How a set is applied.** The NHS says "Use them to get started on a project and to help with making decisions." [7]
GitLab says "Our design principles are outlined in the Pajamas Design System and guide all product design work." [15]
Its critique sessions tell designers to "Connect feedback to user needs and business goals instead of personal
preference" and to "Review the complete design principles in Pajamas" [16]. NN/g advises teams to "use the principles
to explain and justify design decisions" [1]. Salesforce used its ranked principles in design review [24].

**Who owns a set.** GOV.UK credits the Government Digital Service and CDDO [13]. Pajamas says "Everyone is welcome to
suggest improvements by opening an issue" [5], and the NHS offers "Feed back or share insights on GitHub" [7]. No source
names a role that decides a change.

**Not a rule book.** GOV.UK says "This isn't a straitjacket or a rule book." [13], while USWDS calls its set "an
evaluative lens" [6]. That is a tension with the `foundation` reading of a standard judged against. The library reads
that phrase as judgement, not mechanical compliance.

### Debates: conflict, slogans, generic sets and the count

**May principles conflict?** NN/g says a principle should "Not conflict with one another" and "Each principle should be
dedicated to one value only." [1] Brignell says "Real principles reveal priorities." and "Sometimes consistency
conflicts with clarity." [18] Blackie lists "Non-conflicting:" among his criteria [22]. The two camps may be using
"conflict" differently: NN/g may mean that two principles should not contradict each other, and Brignell that a useful
principle exposes a tension. NN/g's same passage goes on: "then clearly specify in which contexts one of these principles
is more important than the other" [1]. **Section 3 of the template names which principle wins in a named kind of
decision, which NN/g's sentence asks for. Reading Brignell's view as asking for the same thing, and the table form,
are the library's POSITION.**
*(Corrected 2026-11-21: this paragraph first said the template takes Brignell's side, and left out NN/g's sentence.)*

**Slogan or decision tool?** Brignell: "A slogan describes intent. A principle guides a choice." [18] Jay Mistry: "Most
design principles read like motivational posters." [20] No source read defends the poster.

**Generic or specific?** Mistry: "If you can't imagine another successful product using the opposite approach, you
don't have a principle - you have a platitude." [20] Blackie writes "Stating the obvious takes up space" and criticises
the GOV.UK set as generic [22]. Brad Frost dissents in part: "including a few key principles that aren't entirely unique
isn't the worst thing in the world" [21].

**How many?** NN/g warns that "having 10 or more leads to many being forgotten" [1]. Brignell says "The most effective
examples use 3-5 principles." [18] Kholmatova's slides say "not more than 3-5" [3], and Mistry "Limit to 3-4 maximum."
[20] **None of them cites a measurement.** Treat every number as a practitioner's heuristic.

**Ranked or unranked?** Salesforce "stack-ranked" its four principles after it "took each principle to the extreme"
[24]. Keith recommends the form "X, even over Y." [26] Atlassian writes each principle as one thing before another, such
as "Trusted fundamentals before comprehensive patterns" [25]. GOV.UK, the NHS and USWDS publish their sets unranked.

**Ownership, design team or product team, is not a dispute any source takes up.** It must not be written as one.

### Relationships: the other kinds of design guidance

**NN/g places design principles in a hierarchy of four kinds of guidance.** "Think of them as a hierarchy that connects
your team's foundational agreements to your tactical implementations." [23] Team charters govern how a team works,
usability heuristics are universal ("Unlike design principles, which are specific to an organization"), and "design
patterns offer concrete solutions and are much more tactical in nature" [23]. NN/g lists "Regularly updated" as a trait
of an effective team charter, not of a set of principles [23].

**USWDS separates the principles from the design system.** "These design principles are one set of shared values, and
the design language of the U.S. Web Design System is another." [6]

**The line with product principles is drawn by this library, not by the sources.** ADR 0089 (lines 91-94) says design
principles frame experience decisions and product principles resolve product trade-offs. No source read draws that
line in so many words. The published sets cross it. One of NN/g's own example design principles is "Prioritize user
needs over business constraints.", whose purpose is to "Help make tie-breaking design decisions." [23] USWDS's principle on earning
trust asks about data privacy and continuous-integration testing [6]. Pajamas says "There are two kinds of principles"
[5], but its split is between "The principles that guide the process" and "The principles that define the output", not
between design and product.

**A working test, the library's own inference at medium-low confidence.** Ask what the principle settles. If it settles
how an interaction, a message or a screen should behave for its user, it is a design principle. If it settles what the
team builds, funds or declines, it is a product principle. Some will straddle, and the guide should say so.

**Repository neighbours.**

- `product-strategy`: the one-pager full variant's Product Principles section (lines 157-175) asks for two to five
  rules that resolve recurring trade-offs. That is product principles' territory, summarised inside a strategy.
- `design-brief`: a define-phase handoff of one chosen concept. A brief may cite the principles; neither file names
  them.
- `definition-of-done`: the closest sibling in shape, a standing standard judged against. It judges whether work is
  finished; design principles judge which design choice to make. Its When NOT to use table is the model for this
  guide's routing table.
- `product-vision`: upstream. NN/g says "These important values may have been captured in vision statements or project
  briefs." [1]

### The gap question, routed under decision procedure 12

The gap dimension did not read the spec or this bundle's files before searching. Its baseline was the naive form a
principle takes in Gabriel Svennerberg's anatomy, a title, a description and "Provide some examples" [12]. Six
candidates surfaced. Each is routed here as a candidate, not an obligation.

| # | Candidate | Sources | Route |
|---|---|---|---|
| 1 | A priority order, or a trade-off written into each statement | Salesforce [24], Keith [26], Atlassian [25], Brignell [18] | Section 3, When Principles Conflict. The X-over-Y form is offered as a GOOD example, not required |
| 2 | The research or evidence each principle rests on | Spool: "Does It Come Directly From Research?" [4]; the NHS's stated provenance [7]; USWDS's "Further reading" [6] | A field in section 2, *What it rests on*, optional per principle. No set read carries it, so it is the library's POSITION |
| 3 | A worked case in which the principle decided something | Pajamas' "Example in practice" [5]; Spotify: "The more examples, the better" [17]; GOV.UK's linked case studies [13] | A field in section 2, *A decision it settled* |
| 4 | A scope statement | Spool: "Have You Evaluated it for This Project?" [4]; Blackie's typology [22] | Section 1, Purpose and Scope |
| 5 | A change process and a dated record | GOV.UK's update history [13] and its working group [14]; the NHS update date [7] | Section 5, Ownership and Changes, gains a dated change log |
| 6 | A reversal test, or what the principle rules out | Spool: "Is it Something You Might Reverse in a Future Release?" [4]; Mistry's opposite test [20]; Productboard's "What it rules out:" [11] | A field in section 2, "What it rules out", and a guide rubric row |

## Claims flagged contested or time-bound

- **Whether principles may conflict.** NN/g against Brignell, Keith and Mistry, as above. Possibly a difference of
  meaning rather than of view.
- **Whether a set should be ranked.** Salesforce, Keith and Atlassian rank or write trade-offs in; GOV.UK, the NHS and
  USWDS do not.
- **Whether generic principles earn a place.** Mistry and Blackie say no; Frost says a few do no harm.
- **The right count.** Every figure is a practitioner heuristic, and none cites a measurement.
- **Whether two principles types exist.** The maintainer ruled two types (ADR 0090). External support is thin:
  Pajamas' split is process against output.
- **A standard or a lens.** GOV.UK says its set is not a rule book [13]; the family reads principles as a standard
  judged against.
- **Time-bound.** principles.design's two articles [18], [19] are dated 2026 and its collection changes. The GOV.UK set
  changed on 2 April 2025 [13]. NN/g's design guidance article [23] is dated 2025-04-18.

## Honest framing

The bundle can say what a design principles document is, what published sets put in each principle, and how rarely a
set changes. It cannot say who invented the practice, how many principles is right, or that any field beyond a
statement is standard. **No source publishes a template**, so every section of this template is assembled from
published sets and method articles, and most of its structure is the library's POSITION. The strongest finding is
negative: across the five published sets whose fields are tabulated above, no principle carries the evidence it rests on, and only a vendor's prompt asks
what a principle rules out. The template asks for both, and says that it is asking for more than the published sets
do.

## Notes for the companion

**Load-bearing sections.** Section 2 (The Principles) is the document, and section 3 (When Principles Conflict) is the
library's position on a live dispute. Section 6 (Review Trigger) is the family's obligation.

**The section design, as the spec proposed and this research tested.**

1. **Purpose and Scope.** The product or service covered, who applies the set, and its relation to the design system.
   Gap candidate 4 lands here.
2. **The Principles.** Three to five. Each carries a statement, what it rules out, the question a reviewer asks, what
   it rests on, and a decision it settled. The first three are sourced in published sets or a prompt; the last two are
   the gap dimension's candidates.
3. **When Principles Conflict.** Which principle wins, and in which kind of decision.
4. **Using Them in Decisions.** Where the set is applied, such as critique, review and pattern proposals, and how a
   decision cites a principle.
5. **Ownership and Changes.** The named owner, how anyone proposes a change, who decides, and a dated change log.
6. **Review Trigger.** A table of Condition, Owner, What They Do About It. Its conditions are sourced where possible: a
   new cross-cutting concern with people behind it (GOV.UK [14]), an audit that finds principles overlapping or
   forgotten (Spotify [17], NN/g [1]), a new project or product joining the scope (Spool [4]), and a recurring debate no
   principle settles (the library's POSITION). No calendar interval is sourced, so none is required.

**The sharpest teaching points.**

- A principle that rules nothing out is a slogan. Brignell and Mistry agree on that, and Spool's tests point the same
  way.
- A set of more than five is a list nobody remembers. That is a heuristic, not a measurement.
- The line with product principles is the library's own, and published sets cross it. Teach the what-does-it-settle
  test.
- Never call the type "product design principles", NN/g's own name for it [1], because that name collides with the
  sibling bundle.

**The example.** The maintainer ruled on 2026-11-20 that the example is Acme Analytics' own design principles, paired
with the later `product-principles` example. Facts it must carry, with no contradiction:

- It is dated inside FY26, which runs February 2026 to January 2027 (`product-strategy_example.md:5`). Its
  `last_updated` falls after the FY26 strategy (2026-01-28) and the positioning statement (2026-01-30), and before the
  Saved Views design brief (2026-06-01, `design-brief_example.md:7`). It may cite the vision, the strategy and the
  positioning statement. It must not cite the design brief, any later document, or `product-principles`, which does not
  exist yet.
- Its owner is a named design lead. The Saved Views design brief already names one, Marcus Webb, Design Lead,
  Reporting, whose team holds a design critique every two weeks (`design-brief_example.md:117-126`). Reuse him rather
  than inventing a second. Dana Okoro, VP Product, who owns the vision and the strategy, approves it. *(Corrected
  2026-11-20: this note first said no shipped Acme example names a design lead. The example's drafting agent found
  Marcus Webb.)*
- It holds three to five principles, each with the section 2 fields.
- At least one principle serves the Recurring Analyst, who "has no data team behind them"
  (`product-strategy_example.md:45-48`).
- Section 3 resolves one real conflict between two of its principles, in a named kind of decision.
- Its change log shows a first version agreed before FY26 and one revision. The revision fired from a Review Trigger
  row: the FY26 strategy named the Recurring Analyst as its target.
- No principle restates a FY26 strategy choice, such as the connector freeze (`product-strategy_example.md:102-103`).
  The principles must outlive that strategy.
- It must not reuse "Propose, never impose", which is the GOOD text of the `product-strategy` one-pager template.
- All figures are labelled illustrative.

**The stop rule.** If the filled principles read as slogans no design decision could break, the build stops and the
decision returns to the maintainer.

**Risks the drafting agents should hold.** The Productboard prompt [11] reserves its rights: describe its fields, copy
none of its wording. The principles.design field guide [10] was not read past its sales page, so nothing may be said
about its contents. The count heuristics must never be presented as measured.

## Sources

### Origins: a convergence of practitioner writing, with no founding text

**[1] Maria Rosala (Nielsen Norman Group), 'Crafting Product-Specific Design Principles to Support Better Decision Making', 2 Aug 2020.** practitioner. **fetched-and-verified.**
`https://www.nngroup.com/articles/design-principles/`
Supports: NN/g's definition of product design principles as value statements used to frame design decisions; the separation from general principles of good design and from UI directions; the four-step method, whose third step is to identify common tradeoffs; the qualities a principle needs, including that principles should not conflict and that each should carry one value; the warning that 10 or more are forgotten; that the values behind a set may already sit in vision statements or project briefs; and the advice to use the principles to explain and justify design decisions. Dated 2020, so it is a definition source, not an origin source
Quotable: "Product design principles (or, in short, design principles) are value statements that describe the most important goals that a product or service should deliver for users and are used to frame design decisions."
Quotable: "product design principles are different from principles of good design, such as usability guidelines, heuristics, or visual-design principles"
Quotable: "Design principles are specific to the product or service that is being designed."
Quotable: "they are not directions on how to design specific UI elements (like design patterns or standards)"
Quotable: "Step 1: Identify Core Values"
Quotable: "Step 2: Consider How These Values Impact Users"
Quotable: "Step 3: Identify Any Common Tradeoffs"
Quotable: "Step 4: Write, Compare, and Iterate"
Quotable: "Take a stand on which value is important"
Quotable: "having 10 or more leads to many being forgotten"
Quotable: "value statements that frame design decisions"
Quotable: "with your design system"
Quotable: "specific to the product or service"
Quotable: "vision statements"
Quotable: "Having many people write a version of a design principle for each value can help to generate many good ideas."
Quotable: "use the principles to explain and justify design decisions"
Quotable: "Identify Any Common Tradeoffs"
Quotable: "Often, product design principles are referred to as"
Quotable: "Not conflict with one another"
Quotable: "then clearly specify in which contexts one of these principles is more important than the other"
Quotable: "Each principle should be dedicated to one value only."
Quotable: "These important values may have been captured in vision statements or project briefs."
Quotable: "Publish them in blogs or with your design system"

**[2] Ben Brignell, principles.design (home page: 'Design Principles | A Free Library of Real-World Design Principles').** practitioner. **fetched-and-verified.**
`https://principles.design/`
Supports: A maintained collection of published design principle sets, with a definition that matches NN/g's. It lists the NHS, Monzo and Fisher-Price sets. It dates nothing on its home page, so it is not a history. Its curator sells an audit, a field guide and consulting on the same site, so its claims are the curator's
Quotable: "Design principles are clear statements that help teams make consistent decisions and trade-offs when designing products, services, or systems."
Quotable: "Fisher-Price Toy Making Principles"
Quotable: "Irving Price and Helen Schelle"
Quotable: "NHS Design Principles"
Quotable: "Monzo Product Principles"

**[3] Alla Kholmatova, 'From Purpose to Patterns' (talk slides, 75 slides, Speaker Deck, 16 June 2018).** practitioner. **fetched-and-verified.**
`https://speakerdeck.com/craftui/from-purpose-to-patterns`
Supports: A 2018 practitioner talk drawing on the author's 'long-term research on what makes effective design principles'. Gives four quality criteria (genuine, opinionated/point of view, actionable, memorable), a purpose-to-principles-to-patterns chain, tests per criterion, and a 3-5 count guide. Slide text only (no speaker notes or transcript beyond slide text), so the reasoning behind each slide is not visible. It cites earlier public writing on principles (Spool, Anderson, Zhuo, Burch, Hollamby, Magera Moon) and quotes a GDS principle ('This is for everyone'), but gives no dates for them. This is the readable page found; the book chapter itself was not read
Quotable: "At the heart of every well functioning design system are effective design principles."
Quotable: "not more than 3-5"
Quotable: "work together as a set"
Quotable: "purpose informs principles"
Quotable: "know who they are for"
Quotable: "test and evolve"
Quotable: "This is for everyone - Government Digital Service"
Quotable: "Creating Great Design Principles Jared M. Spool"
Quotable: "Principles To Build By Stephen Anderson"

**[4] Jared M. Spool (Center Centre), Creating Great Design Principles: 6 Counter-intuitive Tests (1 March 2011).** practitioner. **fetched-and-verified.**
`https://articles.centercentre.com/?p=245`
Supports: Six tests that name elements a principle should carry: a research origin, a 'say no' power, a competitor contrast, a reversal scenario, a per-project evaluation (scope) and a continuously tested meaning; also that principles retire
Quotable: "Does It Come Directly From Research?"
Quotable: "Does it Help You Say 'No' Most of the Time?"
Quotable: "Is it Something You Might Reverse in a Future Release?"
Quotable: "Have You Evaluated it for This Project?"
Quotable: "old principles will need to go into storage"

### Structure: what a published principle carries

**[5] GitLab Pajamas Design System - Principles.** practitioner. **fetched-and-verified.**
`https://design.gitlab.com/about/principles/`
Supports: A set of 10 principles under one umbrella theme; each carries a title, a one-line statement, a 'When designing any feature, ask:' reviewer question, 2-3 bullets of practice, and a worked 'Example in practice'. The page also links a PDF condensed version
Quotable: "Principles act as a reusable standard for teams to measure their work."
Quotable: "When designing any feature, ask:"
Quotable: "Example in practice"
Quotable: "A condensed version of these principles for easy reference."
Quotable: "There are two kinds of principles"
Quotable: "The principles that guide the process, which are defined in the"
Quotable: "The principles that define the output, which are described on this page."
Quotable: "Though we take inspiration from other companies, our principles are defined by looking inward."
Quotable: "Everyone is welcome to suggest improvements by opening an issue"
Quotable: "Make everything feel like one product"
Quotable: "When designing any feature, ask: Does this feel like part of one unified product?"
Quotable: "What are design principles - principles.design"
Quotable: "From purpose to patterns - Alla Kholmatova"

**[6] U.S. Web Design System (GSA) - Design principles.** primary. **fetched-and-verified.**
`https://designsystem.digital.gov/design-principles/`
Supports: Five principles, each with a statement paragraph, a 'Key considerations' list of questions, a 'Practical actions' list and 'Further reading'; the longest per-principle form read. The set is framed as an evaluative lens for design and implementation decisions, and the page says the principles and the design language are separate sets of shared values. Its 'Earn trust' principle asks about data privacy and continuous-integration testing, so one published design principles set reaches into product and engineering territory
Quotable: "to be an evaluative lens for design and implementation decisions"
Quotable: "Key considerations"
Quotable: "Practical actions"
Quotable: "Further reading"
Quotable: "These design principles are one set of shared values, and the design language of the U.S. Web Design System is another."
Quotable: "These design principles are intended to help teams across government align on common goals"

**[7] NHS England - NHS digital service manual, Design principles.** primary. **fetched-and-verified.**
`https://service-manual.nhs.uk/design-system/design-principles`
Supports: Ten numbered principles, each a short imperative title and one to four sentences, with no reviewer question, example or evidence field. The page states a use (to start a project and to help make decisions), a provenance (the principles are inspired by the NHS Constitution), a poster PDF, a feedback channel on GitHub and an 'Updated: April 2023' date. It is one of two sets read that state a reuse licence, with GOV.UK [13] (corrected 2026-11-21): the Open Government Licence v3.0, except where otherwise stated
Quotable: "These principles guide all of our design."
Quotable: "All content is available under the Open Government Licence v3.0, except where otherwise stated."
Quotable: "Download design principles poster (PDF, 126KB)"
Quotable: "Feed back or share insights on GitHub"
Quotable: "Updated: April 2023"
Quotable: "Do not rely on hunches."
Quotable: "Use them to get started on a project and to help with making decisions."
Quotable: "They're inspired by the"
Quotable: "Download design principles poster"
Quotable: "Put people at the heart of everything you do"

**[8] IBM Design Language - Principles.** vendor. **fetched-and-verified.**
`https://www.ibm.com/design/language/philosophy/principles/`
Supports: 4 principles (Carefully Considered, Uniquely Unified, Expertly Executed, Positively Progressive); each is a two-word adjective-pair title, one explanatory paragraph, and 4-6 yes/no reviewer questions with no examples or rules-out. The page carries a 'Copyright 2026 IBM' footer and no reuse licence in the retrieved text
Quotable: "provide clear criteria for the conception, craftsmanship and creativity"
Quotable: "Have we removed everything gratuitous?"
Quotable: "Copyright © 2026 IBM"
Quotable: "Is it IBM to do? Is it essential? Is it opinionated?"
Quotable: "Carefully Considered"
Quotable: "Uniquely Unified"

**[9] Microsoft Learn - Windows 11 design principles (Windows apps).** vendor. **fetched-and-verified.**
`https://learn.microsoft.com/en-us/windows/apps/design/design-principles`
Supports: 5 principles (Effortless, Calm, Personal, Familiar, Complete + Coherent); each is a one-word (or short) name plus a one-to-two-sentence statement written in the user's first-person voice, with no questions, examples or evidence. The page then moves to 'signature experiences' (color, materials, typography, etc.), which are visual-language topics and not principles. Footer shows a Microsoft copyright and Trademarks/Terms of Use links; no reuse licence is stated in the retrieved text. The cached body also contains a generic 'Access to this page requires authorization' banner, but the article body was present and fully readable
Quotable: "The design principles below have guided us throughout the journey"
Quotable: "Windows 11 is faster and more intuitive."
Quotable: "The design principles below have guided us throughout the journey of making Windows the best-in-class implementation of Fluent."

**[10] Ben Brignell - Design Principles in Practice: A field guide (principles.design/field-guide/), sales page.** vendor. **fetched-and-verified.**
`https://principles.design/field-guide/`
Supports: The page is a sales page for a paid ($29 individual, $119 team) PDF guide, not the guide itself. It lists chapter titles including 'The anatomy of a strong principle' and names three worksheets (principle stress-test, trade-off mapping template, decision review checklist). It proves those artifacts exist and are paid; it states none of their contents. The guide's anatomy and the worksheet fields were NOT read. Copyright is Brignell Ltd. No reuse licence is stated
Quotable: "The anatomy of a strong principle"
Quotable: "Principle stress-test worksheet"
Quotable: "Trade-off mapping template"
Quotable: "Decision review checklist"
Quotable: "© Brignell Ltd"

**[11] Productboard - Product Management Prompts Library: Design Principle Generator (an AI prompt).** vendor. **fetched-and-verified.**
`https://www.productboard.com/product-management-prompts-library/design-principle-generator/`
Supports: This is an AI prompt, not a published principle set or a document template. It defines a 5-field principle structure (Name 2-4 words, Statement 1-2 sentences, In action with 2-3 examples, What it rules out, The trade-off 'X over Y'), asks for 4-6 principles, and a quality test of specificity, tension and falsifiability. It also asks for a precedence order and a list of exceptions. Footer: 'Copyright 2026 Productboard, Inc. All rights reserved.' No reuse licence; the prompt text must not be copied into the bundle
Quotable: "Great design principles are not brand adjectives"
Quotable: "generate 4-6 design principles"
Quotable: "What it rules out:"
Quotable: "In design reviews"
Quotable: "Our principles say [X] over [Y] in this case."
Quotable: "Copyright © 2026 Productboard, Inc. All rights reserved."
Quotable: "Write UX design principles that give your design team consistent decision-making guidance"
Quotable: "decision rules"
Quotable: "brand adjectives"
Quotable: "falsifiability"

**[12] Gabriel Svennerberg, The Anatomy of a Design Principle (Design Principles FTW).** practitioner. **fetched-and-verified.**
`https://www.designprinciplesftw.com/articles/the-anatomy-of-a-design-principle`
Supports: The baseline a naive template would reproduce: title, description, examples of applying the principle, optional illustration. Useful as the contrast case. It does not mention priority, scope, evidence or change process
Quotable: "Provide some examples"

### Practice: how a set is applied, owned and changed

**[13] Government Digital Service and Central Digital and Data Office, Government Design Principles (GOV.UK guidance page).** primary. **fetched-and-verified.**
`https://www.gov.uk/guidance/government-design-principles`
Supports: An eleven-principle public set credited to GDS and CDDO. Its update history records three entries: first published 3 April 2012, illustrative blog posts updated 10 September 2019, and an eleventh principle, on environmental impact, added 2 April 2025. No revision interval is stated. Each principle links to illustrative case-study posts, and the page says the set is not a rule book
Quotable: "First published."
Quotable: "A principle about minimising environmental impact has been added to the Government Design Principles."
Quotable: "This isn’t a straitjacket or a rule book."
Quotable: "except where otherwise stated"
Quotable: "Every circumstance is different."
Quotable: "Updated illustrative blog posts added."
Quotable: "This isn't a straitjacket or a rule book."
Quotable: "Government should only do what only government can do."
Quotable: "A principle about minimising environmental impact has been added"
Quotable: "Start with user needs"
Quotable: "Be consistent, not uniform"
Quotable: "The UK government's design principles"
Quotable: "Government Digital Service"
Quotable: "This isn't a straitjacket or a rule book"
Quotable: "First published"
Quotable: "3 April 2012"
Quotable: "2 April 2025"

**[14] Government Digital Service (blog authors), Adding sustainability to the Government Design Principles, Services in government blog, 2 April 2025.** primary. **fetched-and-verified.**
`https://services.blog.gov.uk/2025/04/02/adding-sustainability-to-the-government-design-principles`
Supports: The one documented reopening of a set: a cross-government working group and two workshops, one on how the principles are used and one to critique and rewrite the draft, added a principle in 2025 to a set first published in 2012. The trigger was a new cross-cutting topic with a community group behind it, not a calendar. A reply from the authors says the posters then needed redrawing. The cached body is a tag-stripped text extraction of the page
Quotable: "have been guiding the design for government services since their creation in 2012"
Quotable: "we're now looking for someone to create an 11th poster, and to update the other 10"
Quotable: "We facilitated 2 workshops"

**[15] GitLab, Product Design (GitLab Handbook, product/ux/product-design).** practitioner. **fetched-and-verified.**
`https://handbook.gitlab.com/handbook/product/ux/product-design/`
Supports: GitLab says its design principles live in the Pajamas Design System and guide all product design work; designers are DRIs for design decisions; all designers review each other's work and contribute to Pajamas. The page names no owner, review interval or revision trigger for the principles
Quotable: "Our design principles are outlined in the Pajamas Design System and guide all product design work."
Quotable: "As the DRIs for design decisions"
Quotable: "design principles are outlined in the Pajamas Design System and guide all product design work"

**[16] GitLab, Product Designer workflow (GitLab Handbook, product/ux/product-designer).** practitioner. **fetched-and-verified.**
`https://handbook.gitlab.com/handbook/product/ux/product-designer/`
Supports: Design critique at GitLab is a dedicated session that connects feedback to user needs and business goals rather than personal preference, and it points designers to Pajamas for the design principles. The cached body is a tag-stripped text extraction of the page
Quotable: "Connect feedback to user needs and business goals instead of personal preference"
Quotable: "Review the complete design principles in Pajamas"

**[17] Spotify Design, Introducing Spotify's New Design Principles (Medium, 8 July 2020).** practitioner. **fetched-and-verified.**
`https://medium.com/spotify-design/introducing-spotifys-new-design-principles-c99c58ed7558`
Supports: A filled set (Relevant, Human, Unified) with the audit of the predecessor set (2013, six principles) by three named defects, the three guiding questions (why, who for, how used), a rollout plan, a post-rollout survey, and a lesson that more examples were needed
Quotable: "The more examples, the better"
Quotable: "examples of good (and not-so-good) execution"
Quotable: "Overlapping concepts"

### Debates: conflict, slogans, generic sets and the count

**[18] Ben Brignell, 'Why Most Design Principles Fail', principles.design, 6 March 2026.** practitioner. **fetched-and-verified.**
`https://principles.design/articles/why-most-design-principles-fail/`
Supports: Failure modes of published sets: slogans in place of decision tools, no stated trade-offs, too many principles, principles nobody refers to, and values mistaken for principles. It says real principles reveal priorities and that consistency sometimes conflicts with clarity, and that 3-5 principles work best. The author sells a course and an audit on the same site
Quotable: "A slogan describes intent. A principle guides a choice."
Quotable: "Real principles reveal priorities."
Quotable: "If everything is equally important, nothing actually guides the decision."
Quotable: "The most effective examples use 3-5 principles."
Quotable: "Design principles aren’t mission statements."
Quotable: "Values shape culture. Principles shape decisions."
Quotable: "A design principle should do something more practical. It should help a team make a decision when there are several possible options."
Quotable: "Sometimes consistency conflicts with clarity."
Quotable: "Real design work involves trade-offs."

**[19] Ben Brignell, 'Design Principles vs. The Principles of Design', principles.design, 12 February 2026 (updated 15 February 2026).** practitioner. **fetched-and-verified.**
`https://principles.design/articles/design-principles-vs-principles-of-design/`
Supports: Design principles are strategic and about decision-making; they are distinct from visual craft principles; they are unique to an organisation, team or project; they act as constraints that give team members ownership
Quotable: "Unlike rules, which prescribe a specific outcome, principles guide judgement."
Quotable: "Design principles are unique to an organisation, team or project."
Quotable: "The principles of design belong to craft and execution."
Quotable: "Design principles belong to direction and judgement."
Quotable: "a guiding statement that helps a team make trade-offs when the right answer is not obvious"

**[20] Jay Mistry, 'Your Design Principles Are Useless (Here's What Actually Works)', Substack, 14 June 2025.** practitioner. **fetched-and-verified.**
`https://jaymistry.substack.com/p/design-principles-tenets`
Supports: Named critic: generic principles are platitudes; proposes opinionated 'tenets'; limit 3-4; context-specific; the opposite test; the goal is to end repeated debates, not all debate
Quotable: "design principles are mostly platitudes"
Quotable: "Most design principles read like motivational posters."
Quotable: "If you can't imagine another successful product using the opposite approach, you don't have a principle - you have a platitude."
Quotable: "Limit to 3-4 maximum."
Quotable: "Principles tell you to build good products. Tenets tell you how to choose between good options."

**[21] Brad Frost, 'In the future, design principles won't be about design' (link post, 6 June 2017), commenting on a UX Collective essay and quoting Jared Spool and Jeremy Keith.** practitioner. **fetched-and-verified.**
`https://bradfrost.com/blog/link/in-the-future-design-principles-wont-be-about-design/`
Supports: Named counterweight on generic vs specific: a few generic-sounding principles serve organisations scaling design awareness; principles that sound generic can come from research; secondhand statements of the reversibility and differentiation tests
Quotable: "including a few key principles that aren't entirely unique isn't the worst thing in the world"

**[22] Stuart Blackie (Mantel), Principles with purpose: making design rules that matter.** practitioner. **fetched-and-verified.**
`https://mantelgroup.com.au/principles-with-purpose-making-design-rules-that-matter/`
Supports: A criteria list (opinionated, non-conflicting, reflective of brand, minimal count), a typology (industry heuristics vs team principles vs business/program principles) that implies a scope statement, and a critique of the GOV.UK set as generic
Quotable: "Stating the obvious takes up space"
Quotable: "Non-conflicting:"

### Relationships: the other kinds of design guidance

**[23] Rachel Krause (Nielsen Norman Group), Design Guidance: Principles, Patterns, Heuristics, and Team Charters, 2025-04-18.** practitioner. **fetched-and-verified.**
`https://www.nngroup.com/articles/design-guidance/`
Supports: NN/g's hierarchy of four kinds of design guidance: team charters, design principles, usability heuristics and design patterns. Principles are organisation-specific and strategic, heuristics universal, patterns tactical. One of NN/g's own example principles, 'Prioritize user needs over business constraints', is a tie-breaking trade-off. The trait 'Regularly updated' is listed for team charters, not for design principles
Quotable: "Prioritize user needs over business constraints."
Quotable: "Help make tie-breaking design decisions."
Quotable: "Unlike design principles, which are specific to an organization"
Quotable: "design patterns offer concrete solutions and are much more tactical in nature"
Quotable: "Think of them as a hierarchy that connects your team’s foundational agreements to your tactical implementations."
Quotable: "team charters"
Quotable: "Design principles align teams and provide consistency for evaluating design choices."
Quotable: "Regularly updated"
Quotable: "Value statements"
Quotable: "Shared document or agreement"
Quotable: "Regularly updated: Adapted as the team"

### The gap question: priority order, evidence and reversal

**[24] JD Vogt (Salesforce UX), Defining Principles to Drive Design Decisions (Medium, 19 May 2016).** practitioner. **fetched-and-verified.**
`https://medium.com/@salesforce/defining-principles-to-drive-design-decisions-811a85032c56`
Supports: Salesforce Lightning's four principles are explicitly stack-ranked (Clarity, Efficiency, Consistency, Beauty), and the article records the ranking method (push each principle to the extreme at the expense of the others) and the rationale for each position, plus use in design review and spread to marketing and product management
Quotable: "we stack-ranked them"
Quotable: "took each principle to the extreme"
Quotable: "We put it first."
Quotable: "Is that list in priority order?"

**[25] Atlassian - Atlassian Design System values and principles, as mirrored on principles.design (Ben Brignell, curator).** reference (mirror). **fetched-and-verified.**
`https://principles.design/examples/atlassian-design-system`
Supports: A filled set where each of three values is paired with a principle written as 'A before B', so the trade-off is built into the statement. Reference-tier mirror; Atlassian's own page was not read (its URLs returned an 82-byte JavaScript redirect, then a sign-in page)
Quotable: "Trusted fundamentals before comprehensive patterns"
Quotable: "Meeting system needs before delivering features"

**[26] Jeremy Keith (published by Clearleft), Principles and priorities (27 April 2020).** practitioner. **fetched-and-verified.**
`https://clearleft.com/thinking/principles-and-priorities`
Supports: The 'X, even over Y' form as the way to encode priority; the reversibility test for a principle; the HTML 'priority of constituencies' as a ranked-conflict example; prioritisation as a repeated activity
Quotable: "X, even over Y."
Quotable: "In case of conflict, consider users over authors over implementors over specifiers over theoretical purity."
Quotable: "reversability test"
Quotable: "Prioritisation isn't and shouldn't be a one-off exercise."

## Pages not read under the terms rule

Since 2026-11-14 this section holds pages behind a login, a paywall or a bot block, not pages barred by a site's
terms. The research agents found each page below and could not read it. The maintainer has not read any of them by
hand. No claim or quotation in this bundle rests on them, and the maintainer may read any of them by hand.

- `https://atlassian.design/get-started/vision-values-principles`: it returned an 82-byte script redirect, and the
  redirect led to a sign-in page on `go.atlassian.com`. It would have given Atlassian's own text of the set, which is
  read here only through the principles.design mirror [25].
- `https://medium.com/designing-atlassian/co-creating-our-atlassian-design-system-values-and-principles-2547a0981923`:
  it returned HTTP 403. It would have shown how Atlassian's set was written.
- `https://uxdesign.cc/the-future-of-design-principles-c1f045b7aa26`: it returned HTTP 403. It would have been one
  more practitioner voice in the debates dimension.
- `https://principles.design/field-guide/` past its sales page: the field guide is a paid PDF. Its anatomy chapter
  and worksheets would have shown the curator's own fields for a principle. Nothing is said about its contents.
