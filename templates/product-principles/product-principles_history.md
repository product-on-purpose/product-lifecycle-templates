# product-principles: history

Change log for the `product-principles` bundle. Each entry records what changed and why, so a reader can
tell a correction from a preference.

## 0.1.1 - 2026-11-21 - corrections from a Codex review

**Corrections, not preferences.** A read-only Codex review of the bundle, run after it merged, raised
findings that a Sonnet verifier then checked line by line against the files and the cached sources. The
ones that held are fixed here. Three guidance comments in the template change, so the template is stamped
0.1.1. No section, field or placeholder changes. The example was filled from 0.1.0 and keeps that stamp.

- **The rubric gains a floor.** A 0 on row 7 (conflict), row 9 (owner) or row 11 (Review Trigger owners)
  now fails the set whatever the total. Before this, a set scoring 0 on all three still totalled 18 of
  24 and passed the line at 16. The floor is the library's judgement, like the line.
- **Productboard's prompt says more than its heading.** The template and the companion said the research
  could not say what the prompt's When Principles Conflict section demands. The cached prompt [4] asks for
  a hierarchy or a process and gives a hypothetical example, now described as a vendor's prompt. The
  companion also said no source states the strategy-change trigger, though its own trigger table quotes
  the prompt stating it; that sentence now credits the prompt.
- **The gap on saying no is narrower.** The guide said the research found no named company case of a set
  used to say no. Monzo [6] and Gazit's Pay.com account [26] show teams turning down an option of their
  own. What the research did not find is a set used to decline a request from outside the team, and the
  guide now says that.
- **"Every set read" becomes "all eight tabulated".** Langfuse [15], read beside the table, has lists but
  no named principles. The template's preamble, its section 2 comment and the log's finding are narrowed.

Findings that held only in part and were judged not to need a change are listed in the pull request.

## 0.1.0 - 2026-11-20

**Initial release.** Admitted by
[ADR 0090 (product principles joins standing-standards as a foundation)](../../docs/internal/decisions/0090-product-principles-joins-standing-standards-as-a-foundation.md),
which the maintainer accepted on 2026-11-14. The spec was written on 2026-11-17 in
[`tier2-specs.md`](../../docs/internal/tier2-specs.md). On 2026-11-20 the maintainer ruled the open choices
as recommended and asked for this build, which follows `design-principles` as the backlog planned. The build
is issue #360 (bundle: product-principles), and it fills catalog entry 214, a new row.
[`product-principles_research-log.md`](product-principles_research-log.md) records **40 sources, all
fetched-and-verified**: 26 practitioner, 9 vendor and 5 primary. Two of the five primary sources are books,
Marty Cagan's *Inspired* and *Empowered*, read from the maintainer's own copies.

**The tenth `standing-standards` member.** It declares `classification: foundation`, the contract's cut for
a standard that decisions are judged against and not an instrument executed under time pressure. Product
principles are consulted when a team chooses what to build, fund or decline, which is the moment of action
the contract's falsifier asks about.

### One size ships, at medium confidence

The bundle ships `lean` only, as the maintainer ruled. The research read no source that publishes a long and
a short version of one set. Intercom pairs a short list with a post per principle, and GitLab follows its
eight principles with a long section on how it follows them. Neither is two versions of one set. The
sources that add depth add it per principle, in Monzo's case studies, Slack's "How it shows up:" field and
Intercom's per-principle posts, and the template does the same. Every count in the sources is advice. They
say three to five, no more than seven, or fourteen in layers, and none cites a measurement. Confidence in a
single size is medium, because it rests on the absence of a published pair and on the maintainer's ruling.

### Most of the structure is this library's position

No source the research read publishes a template for a product principles document, other than a vendor's AI
prompt from Productboard, which reserves its rights. The six sections are therefore assembled from
published sets and method articles, and each says in its comment where it is the library's own position. A
name and a statement appear in every set read, and reasoning is common. A trade-off written into the
principle is shown by several publishers. **A field for what a principle rules out appears per principle
only in that vendor's prompt.** Of the eight published sets tabulated in the companion, none carries it.
Langfuse publishes one set-level list, and Box, as Pendo reports it, a comparable "Versus". The template
asks for more than published sets do and says so. The role names in Ownership and Changes are the library's
position too.

### The research found no founding text, and the bundle names no originator

No source read names who first wrote about a team writing its own product principles, or when. The earliest
source read is Cagan's PRD guide, which carries a step titled "Define your Product Principles" and whose
only date is a 2005 copyright footer. His framing then moves in three steps: principles specific to one
project in 2005, principles aligned with the vision for a product line in 2017 and the strategic context
that product leaders prepare for every team in 2020. The companion reports that move and names no
originator.

### Where the sources disagree, and what the bundle chose

- **The truism test against emotion.** Intercom, an AWS tenets post and Productboard's prompt want a
  principle whose opposite a reasonable team could choose. airfocus wants one that triggers an emotional
  response. **The template follows the opposite test**, on the library's reasoning that a reader can apply
  the test and cannot apply an emotional response.
- **Whose set.** ProductPlan, Product School and ThoughtSpot describe a team-driven set, Cagan's 2020 text
  has product leaders preparing it and LogRocket recommends a hybrid. **The template settles none of
  them.** It asks only for a named owner and a stated way to propose a change.
- **Ranked, or a trade-off in each principle.** ThoughtSpot stack-ranked its candidates and also wrote that
  contradiction between principles did not matter. Salesforce UX and Nielsen Norman Group, both writing
  about design principles, give the ranked case and a middle position. No source opposes ordering outright,
  and none gives a worked rule for two principles that conflict. **The template writes the trade-off into
  the principle and asks which principle wins in a named kind of decision.** That choice is closest to the
  NN/g method and is the library's own position.
- **Whether the set covers execution or the choice of what to build.** Slack limits a set to execution.
  ProductPlan and Cagan describe it as guiding what to build. The template follows Cagan and ProductPlan at
  medium-low confidence, and tells an author who wants Slack's limit to state it in Purpose and Scope.
- **Inside the strategy, or beside it.** No source argues that principles belong inside a strategy document,
  and none ties a principle's life to one strategy period. The set is standing and sits beside the vision
  and the strategy.
- **Standing, or per project.** Cagan's 2005 principles belonged to one project and his 2017 principles are
  not tied to a release. Intercom does both. The bundle is the standing set, and a project's own principles
  belong in that project's PRD.

### The line with design principles is the library's, and published sets cross it

The sources split product principles from design principles by scope. ProductPlan, airfocus and Marc Abraham
state the split. The Org states it and then blurs it, and Intercom keeps five product design principles
inside its product principles. The line the bundle draws is the library's working test, at medium-low
confidence: ask what the principle settles. If it settles how a screen, a message or an interaction behaves
for its user, it is a design principle and belongs in the sibling
[`design-principles`](../design-principles/design-principles_guide.md) bundle. If it settles what the team
builds, funds or declines, it is a product principle. No source read draws the line in those words. Some
principles will straddle it, and Purpose and Scope carries a line for them. The bundle writes "product
principles" for the standing set that settles what the team builds, because The Org uses "principles of
product" for the design phase and the two names collide.

### The staleness mechanism is a Review Trigger with conditions, and no interval is sourced

The family contract forbids a calendar reminder as the only trigger. The sources disagree on intervals:
LogRocket and David Pereira recommend a review every three months, Guru says a set should hold for at least
a year, Intercom says it updates every one to two years and ProductPlan says an update should be an unusual
event. Intercom's own two statements do not fit each other without an assumption, because it also calls its
set in 2022 the third major iteration in about eight years. **The template takes none of the intervals.**
The `foundation` classification holds, because no calendar interval is required. The Review Trigger carries
five conditions, and each names an owner by role. Three come from Productboard's prompt, which is a vendor's
statement: a significant change to the strategy, a principle consistently violated without a decision to
change it and a new principle that would have settled repeated debates. One comes from Intercom, a valid
exception that recurs, and one from Slack, a principle that does not take hold. The owner column is the
library's. A team that wants a review date may add one as a floor and label it as its own choice.

### Verified before drafting

**Every web quotation was checked against raw text**, never against a retrieval tool's summary. Of the 123
web quotations the research agents returned, 122 passed the first check. The one failure was a trim, not an
invention: an agent had changed the first word of a sentence on an Intercom page, and the verbatim span
replaced it. Book quotations were checked against the page text of the maintainer's copies, and one that
crossed a page break was shortened to the part on one page. The main loop also carried in quotations from
the admission sweep and from the spec's own reads, and each was re-tested against the cached raw body. Two
counts were re-checked in the main loop: GitLab's eight principles, three of them in an "over" form, and
Intercom's fourteen, as four research and development, five product design and five engineering.

**One article appears twice.** Ethan Eismann's article on why an organisation needs product principles is
entry 18 on Slack's design site and entry 25 on TechCrunch. They are one author's one argument and count as
one voice.

**Pages the research could not read are quarantined.** Gusto's own product principles page returned HTTP
403, Shopify's careers page returned 404, a 2017 Mind the Product article that Marc Abraham links returned
404, and a governance guide found in search was not read. No claim or quotation in the bundle rests on any
of them. Intercom's per-principle series was read only in Stephen Forbes's post, and the 2022 overview was
read without the per-principle posts.

**Licences.** No page read states a reuse licence, and Productboard, the Salesforce page and the Mind the
Product page reserve their rights. **The bundle describes the structures it found and copies no set's
text.** Cagan's books are print sources with no URL, and the companion quotes them in short spans only.

### Pairing

`pairs_with` is empty. `tools/known-skills.txt` holds no skill that addresses a principles document, which a
read of that file on 2026-11-20 confirmed. An empty list is the legal answer, and the pairing stays
unclaimed until a skill exists that addresses this document.

### Aliases

The spec recommended no aliases, because SVPG's examples page names "The Product Manifesto" and no source
read shows it is the same document. `aliases` is therefore empty.

### The example, and the stop rule it was built under

The worked example is the product principles for Acme Analytics, at `lean` size, owned by Dana Okoro, VP
Product, who also owns the vision, the strategy and the positioning statement. It is dated 2026-02-05, the
day the set was first agreed, after the FY26 strategy and after the design principles as revised on
2026-02-03, so that a reader can see a product trade-off set beside an experience set. It cites only
documents that existed by that date and labels every figure illustrative. The Saved Views design brief and
PRD are cited only in the opening note, because they come later. It was built under the stop rule that ADR
0064 and ADR 0074 record: if the filled principles read as values nobody would argue against, the build
would stop and the decision would return to the maintainer. The example is the library's own illustration.
The research found no evidence that keeping such a document improves decisions.

### What the research did not settle

- Who started the practice, and when.
- How many principles is right, and how often a set should change. Every figure is a heuristic.
- That any field beyond a statement is standard practice. The rules-out field is the clearest case.
- That keeping such a document improves decisions or outcomes. No source measures it. The sample is mostly
  practitioners and vendors who recommend the type.
- That principles are used to decline a specific request. Sources assert it, and the research found no named
  company case that shows one.
- How the template behaves for a solo practitioner, a regulated product or a particular delivery
  methodology. The research found no source on any of them, so the template is untested for all three.
