# Competitive Analysis: the companion

The reference behind the template. Read this when you want to know *why* a section exists, what the
research actually says, and where the sources disagree. The research behind it was conducted on
2026-11-22. Its log is
[`competitive-analysis_research-log.md`](competitive-analysis_research-log.md).

## 1. Orientation

As this library reads the type, a competitive analysis says who else serves the customers a strategy
chose, compares them on what those customers value, and says what that means for the product's
direction. The sources frame the job in their own words. Aha! reduces it to two questions: "How do
our products and services compare to the alternatives? And how can we better differentiate what we
offer?" [[8]](#ref-8) Productboard calls it "the ongoing practice of researching and evaluating
competing products, companies, and market alternatives" [[11]](#ref-11). The encyclopedia definition
is narrower: "the assessment of the strengths and weaknesses of current and potential competitors"
[[1]](#ref-1). Confidence: high that these are the sources' words; medium that they describe one
document.

**The sources do not agree on what the document is.** Aha!'s guide offers "10 competitive analysis
templates for product teams" under one name, in several different forms [[9]](#ref-9). HubSpot's kit
names ten templates [[10]](#ref-10), and Miro lists more than ten [[14]](#ref-14). GitLab's handbook
splits the name in two. A competitor evaluation compares solutions: "It evaluates solutions." A
competitor analysis compares business models and positioning: "A competitor analysis evaluates
companies." [[20]](#ref-20) This bundle holds both halves. It carries profiles of companies, and a
comparison of what their products do for the customers the strategy chose. That scope is this
library's reading, not a source's.

**What this companion can and cannot say.** It can say what the sources mean by the type, what
readable templates put in it, who owns it, and how the sources disagree on refresh. It cannot say
who first wrote one for a product team, because no source read names an originator. It cannot cite
the BABOK Guide as a document origin. It cannot name a refresh interval that anyone has measured.
**Twenty-three of the 56 sources are vendor writing, and nearly every refresh interval and template
structure the research found comes from a vendor.** Most of those vendors sell
competitive-intelligence or product-management software. The template's section set is therefore
largely this library's POSITION, built from vendor field lists, the Silicon Valley Product Group's
narrative exercise, GitLab's practice and the positioning sources. The strongest negative finding is
that no published, filled-in competitive analysis was read. Every gap candidate in this companion is
guidance, not observed practice.

At a glance:

- **The audience is product teams.** Aha!'s template "is for product managers and product marketers"
  [[8]](#ref-8), and at GitLab "A Product Manager will lead their quad team" [[19]](#ref-19).
- **It informs the strategy and does not set it.** Pragmatic Institute says competitors "shouldn’t
  define your product strategy." [[45]](#ref-45) This library places the analysis immediately before
  the positioning statement, and names that placement a POSITION; see section 8.
- **The competitor set follows the buyer's alternatives, and the status quo is one of them.** Four
  publishers say so, and two of the four are interested parties
  [[43]](#ref-43)[[46]](#ref-46)[[48]](#ref-48)[[52]](#ref-52)[[51]](#ref-51).
- **The trap is a comparison on features the rivals chose.** Blank and the jobs-to-be-done camp,
  which this research reads as one voice from Strategyn and THRV, argue the comparison should rest
  on what customers value, and the log records no measurement of the harm
  [[34]](#ref-34)[[35]](#ref-35)[[36]](#ref-36).
- **The sources disagree on refresh, and every interval except GitLab's comes from a vendor.** This
  library reads each refresh as a dated version, and the document as the series.

## 2. Origins and evolution

**Competition was a subject of strategy writing by 1979.** Porter's *How
Competitive Forces Shape Strategy* appeared in the Harvard Business Review in 1979 and opens "The
essence of strategy formulation is coping with competition." [[4]](#ref-4) His book *Competitive
Strategy* followed in 1980 [[7]](#ref-7). A secondary source reports that "Porter developed his Five
Forces Framework in response to the then-prevalent SWOT analysis" [[5]](#ref-5). This research cites
these sources for existence and date only. Only the public abstract of the 1979 article was read,
and the rest sits behind the journal's subscription wall [[4]](#ref-4). The sources disagree
slightly on the date: the journal's page gives the March-April 1979 issue, while one place in the
encyclopedia's reference list gives May 1979 [[4]](#ref-4)[[5]](#ref-5). Confidence: high that the
article exists and is from 1979.

**SWOT's own origin is disputed.** The encyclopedia credits a 1965 report from the Stanford Research
Institute through some authors, and reports one account that calls the Harvard-origin story an
"academic urban legend" [[6]](#ref-6). Only the encyclopedia's account of the dispute was read. The
encyclopedia article on competitor analysis calls the activity "an essential component of corporate
strategy" and lists technique steps such as a competitor array and competitor profiles
[[1]](#ref-1). That article carries a banner, dated April 2013, asking for more citations. Treat it
as a lead and not as evidence.

**The BABOK Guide has no technique titled Competitive Analysis.** The current guide's chapter 10
lists 50 techniques. Technique 10.4 is "10.4 Benchmarking and Market Analysis", and SWOT is "10.46
SWOT Analysis" [[2]](#ref-2). A case-insensitive search of the table of contents for the word
*competitive* found nothing [[2]](#ref-2). The page for technique 10.4 confirmed only its title,
because the body appears to be gated to members [[3]](#ref-3). A technique is a way of doing
analysis work, not a written document. Under [ADR 0030 (templating scope: Markdown
documents)](../../docs/internal/decisions/0030-templating-scope-markdown-documents.md), a technique
cannot count as an origin for a document type. This library's catalog entry 11 cites technique 10.4
in a note. The number exists, but the technique is Benchmarking and Market Analysis, so that note
does not survive, and the spec lists it among the corrections the landing pull request should check
[[2]](#ref-2)[[3]](#ref-3). Confidence: high on the title and number; low on what technique 10.4
says, because it was not read.

**No first written competitive analysis for product teams was established.** The origins research
ran one web search for who first described such a document or template, and found no source that
names one. This companion names no originator, and it makes no claim about what the document
replaced.

**Even one vendor's set of forms moved over time.** Aha!'s 2018 post lists nine approaches,
including a "Value proposition analysis" [[17]](#ref-17). Its current guide lists ten templates and
does not include that one [[9]](#ref-9). The name also varies between publishers. Pragmatic
Institute's framework lists a *competitive landscape* element, defined by the question "What else
could buyers use instead, including doing nothing?" [[46]](#ref-46). GitLab uses *competitor
evaluation* and *competitor analysis* for two things [[20]](#ref-20), and NN/g uses *competitive
review* and *competitive testing* for usability work [[40]](#ref-40). This library uses the name
*competitive analysis*.

## 3. Anatomy (section by section)

The template has nine sections, and its lean variant leaves out the two marked *full only*. The
section set is largely this library's POSITION, for the reason given in the Orientation. Each
subsection below says what the section is, why it exists, and what the research says about doing it
well or distrusting it.

### Purpose and Scope

This section names the customers the analysis covers and the decisions it informs. Calven's guide
gives the instruction: "Define the decision it serves." [[51]](#ref-51) Calven sells an AI
product-marketing platform, so this is a vendor's advice. The tie to the strategy's chosen segment
is this library's POSITION. Its reasoning is that the competitor set in the next section only means
something for a stated customer.

*Expert note.* The stated purpose also tells a reader whose analysis this is. Crayon's survey
reports "47% of respondents" saying "marketing owns the compete function" [[23]](#ref-23). At GitLab
the product side leads the comparison [[19]](#ref-19). The function probably differs by purpose:
product strategy at GitLab's product side, sales enablement in the survey. Confidence: medium.

### The Competitor Set

This section names direct rivals, indirect rivals and the status quo, gives each a tier and a reason
it is in, and names out-of-scope rivals as out. It decides what the whole analysis is about, so it
is a load-bearing section.

**Work from alternatives, not from every competitor.** Dunford asks "What would a customer do if
your offering didn't exist?" and says "Not Every Competitor is an Alternative" [[43]](#ref-43).
Competitors that prospects never consider are what she calls "phantom competitors", left out of
positioning but watched by the product team [[43]](#ref-43). This library's inference, at medium
confidence, is that the analysis may cover the wider field, and the positioning statement takes the
narrower set of real alternatives from it. Aha! advises focusing on direct competitors first and
then branching to indirect ones [[18]](#ref-18). GitLab distinguishes direct from indirect
competitors [[20]](#ref-20).

**The status quo belongs in the set.** Dunford writes that "the first competitive alternative we
need to beat is the status quo" [[43]](#ref-43). Pragmatic Institute's competitive-landscape element
asks "What else could buyers use instead, including doing nothing?" [[46]](#ref-46), and its
positioning page compares against alternatives "including the option of doing nothing"
[[48]](#ref-48). Two guides to this very document say it directly. Customer Impact writes "The
status quo is your largest competitor. Most teams forget it." [[52]](#ref-52) Calven writes "Start
from competitive alternatives, meaning what the buyer would use if you didn't exist.", and "That
tiered set of alternatives, status quo included, is your competitive landscape." [[51]](#ref-51)
Both sell services or software in this area. Placing the status quo inside this
bundle's competitor set is this library's POSITION, taken from the positioning statement's named
alternative. Confidence: high that the sources say it; medium on its weight, because two of the four
publishers are interested.

**Tiering is guidance from several publishers, and the log records no measurement of it.** Calven
says to tier competitors so effort follows tier [[51]](#ref-51). HubSpot's practice, relayed by
Klue, tiers competitors in groups of five by deal frequency and market focus [[22]](#ref-22).
Atlassian's template carries a tier weight in its profile table [[13]](#ref-13), and Miro's
collection includes "Competitor Tiers" [[14]](#ref-14). Win/loss evidence can correct which
competitors the set includes. Pragmatic Institute defines it as evidence on "why recent evaluators
did or didn’t buy from you" [[47]](#ref-47). That correction is this library's inference, at medium
confidence. Klue also warns "Don't just rely on CRM data" when building the picture [[54]](#ref-54).

*Expert note.* NN/g's competitive usability testing selects differently: "The sites you select do
not need to be direct competitors." [[41]](#ref-41) A usability study follows what is worth learning
from. A competitive analysis follows whom the buyer considers. Do not import one selection rule into
the other.

### Competitor Profiles

This section holds one row per competitor, in a table. The nearest published column set is Aha!'s
six: "mission statements, pricing, top features, strengths, weaknesses, and differentiators"
[[8]](#ref-8), which its later post calls "six columns" and says can be added to [[18]](#ref-18).
Aha!'s 2018 post describes an overview template running from "website, location, year founded" to
mission, strengths and weaknesses [[17]](#ref-17).  Atlassian's one-page template has a profile
table, and Productboard's single-competitor brief has a company overview
[[13]](#ref-13)[[12]](#ref-12).

**No two vendors share a field set, and no vendor page read shows the full column set of its
download.** Aha!'s whiteboard body needs a trial sign-up, and HubSpot's templates sit behind a
download form [[8]](#ref-8)[[10]](#ref-10). The bundle's own column set is therefore this library's
POSITION. It describes what these structures contain and copies no table, column order or wording.

*Expert note.* The modal artifact in the vendor material is a competitor-by-attribute grid, with
pricing, features, strengths, weaknesses and differentiators per competitor
[[8]](#ref-8)[[9]](#ref-9)[[11]](#ref-11)[[13]](#ref-13)[[14]](#ref-14). That is the structure
research's own inference from the vendor templates read, at medium-low confidence. None of the
sources states which form is most common. GitLab names websites, documentation, demo videos,
customers and competitors as inputs to accuracy [[21]](#ref-21), so a profile row can rest on more
than one kind of input.

### Competitor Briefs (full only)

This section is a short narrative on each main rival. The method is Cagan's: for each competitor,
identify "the three key things" it does that customers value, and the three areas where the
customer's needs go unmet [[28]](#ref-28). His coaching exercise asks a product manager to "evaluate
the top 3-5 players in the space, and to write up a narrative comparing and contrasting" them
[[29]](#ref-29). Productboard's competitor brief is another narrative form. It has six sections,
from a company overview to a sales battlecard summary, with a "last updated" note and a recommended
refresh cadence [[12]](#ref-12).

*Expert note.* Cagan's coaching exercise gives no maintenance rule [[29]](#ref-29), so it shows a
point-in-time default by omission and not a stated position. A table shows that rivals differ, and a
narrative can say why a customer would pick one. That reading is this library's.

### Comparison on What Customers Value

This section is a load-bearing section, because it is where the feature-checklist trap is avoided or
not. Its criteria come from the chosen customers, not from the rivals' feature lists. Each criterion
is weighted by its importance, as Aha!'s scorecard is "weighted by the importance of each attribute
to your customers" [[9]](#ref-9). Each rival is rated on a three-level scale and not yes or no.
Productboard's matrix rates a capability "fully supported", "partially supported" or "not available"
[[11]](#ref-11). Calven's template uses the same three levels [[51]](#ref-51). Aha!'s guide also
shows "Harvey Balls" as a rating form [[9]](#ref-9), and Dscout's research sheet scores on a "0 to 5
scale" [[15]](#ref-15).

**Why not a feature checklist.** Steve Blank argues "a competitive analysis drives a maximum feature
set" and asks for "No feature lists without facts" [[34]](#ref-34). Strategyn, Tony Ulwick's firm,
says "feature-to-feature comparisons is no guarantee of success" [[35]](#ref-35). THRV, a
jobs-to-be-done consultancy, writes "Feature catch-up with your competitors is a race"
[[36]](#ref-36). Product School shows the other side of the debate: it presents the feature matrix
as one framework among several and says "Which framework you choose depends on your goal"
[[38]](#ref-38). Confidence: medium that the feature checklist is the type's named failure. The log
records no measurement of how often it happens.

*Expert note.* Weighting by customer importance is Aha!'s practice [[9]](#ref-9). GitLab says the
comparison "should be completely data/evidence driven" [[19]](#ref-19). A weight that is a guess is
a guess recorded in a cell, so say where each weight came from; see Evidence and Sources below.

### Jobs-Based Scorecard (full only)

This section scores each rival on how well it helps the chosen customers get a job done. GitLab's
scorecard is built this way: "As a Category Maturity Scorecard is based on Jobs to be Done"
[[19]](#ref-19). Strategyn says to assess "how much better or worse a product is at helping the
customer get a job done" [[35]](#ref-35). GitLab's evaluation page likewise compares solutions
against jobs to be done [[20]](#ref-20).

*Expert note.* Strategyn and THRV both sell a jobs-to-be-done method, and THRV's page shows no
author and sits on a mirror of its content system, so its attribution is weak
[[35]](#ref-35)[[36]](#ref-36). Read the two as one camp. The lean variant keeps the weighted
comparison and leaves this section out.

### Implications for Our Direction

This section is what makes the document a `strategy-docs` member, and it is a load-bearing section.
It says what changes in the strategy, the positioning or the roadmap, with an owner for each
implication. The routing to each sibling is this library's POSITION.

**The boundary: an input to strategy, not its author.** Pragmatic Institute writes "Competitors can
provide useful market intelligence, but they shouldn’t define your product strategy."
[[45]](#ref-45) Cagan lists "the competitive landscape" among the insights a strategy draws on
[[30]](#ref-30), and frames it as one slice of industry insight [[31]](#ref-31). He also wrote "So
stop chasing your competitors and start focusing on providing real value for your customers"
[[28]](#ref-28). The section answers both: it is where a finding becomes a decision about the
product, and not a reaction to the rival.

**End each finding in one move.** Customer Impact advises "Let every finding end in one concrete
move with an owner and a date", and caps the list at three to five actions per quarter
[[52]](#ref-52). Calven gives the same advice in other words [[51]](#ref-51). Both are consultancy
and vendor guidance, with a selling interest in the service.

### Evidence and Sources

This section records a source and a date for each claim, and marks a gap as unknown and not guessed.
Calven's template asks for "Where each claim came from, and when. Makes the doc auditable."
[[51]](#ref-51) It also writes "Every field needs a source you can name, and a blank field beats a
guessed one." and "A cell with an invented number in it is worse than an empty one, because it looks
like knowledge." [[51]](#ref-51) The research found one source that prescribes this, and it is a
vendor's. An earlier finding that no source did was false across the whole list until Calven's page
was read.

**What other sources add.** GitLab says the comparison "should be completely data/evidence driven",
and records the result when teams "Document/update the scoring" [[19]](#ref-19). GitLab also
requires a legal check of competitors' acceptable use policies before using their products
[[19]](#ref-19). Its marketing side names websites, documentation, demo videos, customers and
competitors as accuracy inputs, and says "all our product comparison pages are un-gated"
[[21]](#ref-21). Aha! lists company websites, review sites, industry news and press releases as
source types [[25]](#ref-25). Klue's sales guide advises "Skip the website fluff" [[55]](#ref-55).
Dovetail lists "failing to update or spot-check data" as a common mistake [[27]](#ref-27).

**A confidence rating on each item was considered and turned away.** The intelligence community's
Admiralty code rates source reliability apart from information credibility, so that "the reliability
of the source does not influence the assessed accuracy of the report" [[53]](#ref-53). No
competitive-analysis source read uses one, and the encyclopedia article on the code carries a banner
saying it relies on a single source, so it is a pointer to the convention and not the standard's
text [[53]](#ref-53). The research also found no source that sets how recent evidence must be,
beyond Calven's one quarter [[51]](#ref-51).

### Refresh Trigger and Versions

This section is the `utility` obligation, and a load-bearing section. It names the owner, the events
that call for a refresh, an interval floor the team chooses, and a dated row for each version. **The
table below lists the intervals the sources state, and none of them is measured.** Two sources,
Aha! and GitLab, name a single owner, and GitLab adds a product marketing manager or developer
advocate alongside the product manager [[9]](#ref-9)[[19]](#ref-19). Aha! says "Assign a point person to keep the report updated throughout
the year." [[9]](#ref-9) Crayon's survey puts the function with marketing for many respondents
[[23]](#ref-23), so the owner's function is contested (section 6). Naming one owner and the people
they consult is this library's reading.

**The refresh table.** Every row is an opinion or a self-reported survey figure, and nearly every
row comes from a publisher that sells software. Confidence: medium.

| Who | Interval or rule | Interest |
|---|---|---|
| GitLab, product side [[19]](#ref-19) | "should be done at least annually if you're at Complete"; "Otherwise, when you intend to make a category shift" | Uses the practice; does not sell competitive-intelligence tooling |
| GitLab, marketing side [[21]](#ref-21) | Continuous open editing and no fixed interval: staff "update, correct, amend and comment" | Same publisher |
| Klue [[54]](#ref-54) | "Quarterly is a solid default." | Sells competitive-intelligence software |
| HubSpot, relayed by Klue [[22]](#ref-22) | "Tier one and two competitors, we update our battlecards every quarter." "The rest we update every six months." | Klue sells the software; the cadence is for battlecards |
| Aha!, 2018 [[17]](#ref-17) | A possible "quarterly deliverable" | Sells product-management software |
| Aha!, later post [[18]](#ref-18) | "revisit and refresh your competitive analysis biannually" | Same publisher, a second interval |
| Dovetail [[26]](#ref-26)[[27]](#ref-27) | "Once a year.", "Once a quarter." or "Based on specific events."; audits "monthly, quarterly, or annual" | Sells research-repository software |
| Crayon survey [[23]](#ref-23)[[24]](#ref-24) | Sharing with sales most often monthly; "only 26% of CI teams update battlecards monthly" | Sells competitive-intelligence software; the figures concern battlecards and sharing with sales |
| Calven [[51]](#ref-51) | "A profile built once is usually wrong within a quarter." | Sells an AI product-marketing platform |

**The GitLab cadence needs its condition.** ADR 0091 and the family contract had quoted GitLab's
annual interval as a general cadence, and both now carry a dated note of 2026-11-17 recording the
correction. The raw page reads "should be done at least annually if you're at Complete", then
"Otherwise, when you intend to make a category shift" [[19]](#ref-19). So GitLab's annual interval
applies to a category at its most mature level, and for every other category it names an event and
not an interval. GitLab also recommends an early comparison, before a category matures
[[19]](#ref-19). Confidence: high, from the raw page. The `utility` classification does not depend
on this interval.

**Event triggers the sources name.** Dovetail names a new product coming to market, a shift in a
competitor's marketing and a change in customer habits [[26]](#ref-26). GitLab names a category
shift [[19]](#ref-19).

**Dated versions.** The document is a series of dated snapshots, each refresh adding a row. That
reading is this library's POSITION, and the nearest source is Klue's pairing of a snapshot with its
refreshes [[54]](#ref-54). The interval floor in the template is the team's own choice, because the
sources do not converge on one.

## 4. Variants and sizing

**Lean is the default.** It carries the sections that name the set, profile it, compare it on what
customers value, draw the implications, record the evidence and say when to refresh. It leaves out
the two sections marked *full only*, the competitor briefs and the jobs-based scorecard.

**Full adds a narrative per main rival and a scorecard on the jobs.** The nearest published source
for two weights is Aha!, which asks for both a regular pass and a deeper one: "Conduct a high-level
competitive analysis on a regular basis." and "Perform a more detailed analysis to inform major
strategic decisions." [[8]](#ref-8) Atlassian's one-page document is a published example of a short
form [[13]](#ref-13).

**The signal for scaling up is this library's reading, not a measured one.** Move to full when a
major choice rests on how a few main rivals differ, or when the lean comparison keeps ending in an
argument about which criteria the customers truly care about. The log records no measurement of when
the second weight pays for itself. Size calls in this library are hypotheses that evidence can
overturn.

## 5. Methodology lineage

This library reads the type as methodology-agnostic. This research did not look for
methodology-specific forms of the document, so it makes no claim about how any named delivery
method, or regulated delivery, treats it. The bullets below group the sources by the tradition each
speaks from.

- **Strategy writing.** Porter's competitive-forces tradition treats coping with competition as the
  essence of strategy [[4]](#ref-4), and the encyclopedia places competitor analysis within
  corporate strategy [[1]](#ref-1). Pragmatic Institute's framework places a competitive-landscape
  element beside strategy, win/loss, market definition and positioning [[46]](#ref-46).
- **Product management practice.** Cagan coaches it as a written narrative on the top three to five
  players, with no maintenance rule [[29]](#ref-29). GitLab runs a product-side comparison led by the product manager [[19]](#ref-19).
- **Jobs to be done.** Strategyn and GitLab's scorecard compare rivals on how well they help a
  customer get a job done [[35]](#ref-35)[[19]](#ref-19). THRV argues that feature catch-up with
  competitors is a race [[36]](#ref-36).
- **Customer discovery.** Blank argues that customer discovery, not a feature table, should decide
  which features matter [[34]](#ref-34).
- **Competitive intelligence as a function.** Klue's relayed customer practice, Crayon's survey and
  Octopus Intelligence's argument concern a standing function that works with sales through
  battlecards [[22]](#ref-22)[[23]](#ref-23)[[37]](#ref-37). All three publishers sell software or
  services in that function.
- **Business analysis.** The BABOK Guide holds techniques named Benchmarking and Market Analysis and
  SWOT Analysis, and no technique titled Competitive Analysis [[2]](#ref-2).
- **UX research.** NN/g and Dscout use competitive comparison as a way to learn about designs, with
  users or with a heuristic evaluation [[39]](#ref-39)[[40]](#ref-40)[[15]](#ref-15).

## 6. Debates and contested boundaries

**Living document or dated snapshot.** The living camp, among the pages read, is all vendors.
Octopus Intelligence says a battle card fails when it is "built as a project rather than maintained
as a programme", and writes "A battle card is a document. Competitive intelligence is a process."
[[37]](#ref-37) Product School says competitive analysis "should be a living part of product
culture" [[38]](#ref-38). Productboard says it "isn't a one-time project" [[11]](#ref-11). HubSpot
names "A one-and-done exercise" as what competitive analysis is not [[10]](#ref-10). Klue's sales
guide describes competitive analysis for sales enablement as "Continuous, driven by live deal
feedback" [[55]](#ref-55). Each of
these sells software, training or services, so confidence is high on the words and low on their
independence. GitLab's marketing side also edits continuously, as a practice rather than an argument
[[21]](#ref-21).

**The snapshot reading has a vendor voice too.** Klue recommends a quarterly refresh, and also
writes "Competitive landscape analysis is a snapshot" and calls landscape analyses "temporary
snapshots that need refreshes as the market changes" [[54]](#ref-54). Aha! asks for both a regular
pass and a deeper one [[8]](#ref-8). Pragmatic Institute says the Six Forces model, like SWOT,
"represents a moment frozen in time" [[44]](#ref-44). The research found no named practitioner who
argues for a one-off snapshot as a principle. Cagan's exercise is a single narrative with no
maintenance rule [[29]](#ref-29), which shows a default by omission, not a position. His line
"product strategy is never static" is about strategy, not competitor documents [[30]](#ref-30).

**This library reconciles the two with dated versions.** Each refresh is a dated snapshot, and the
document is the series. The reconciliation is this library's POSITION. Because a vendor voice sits
on both sides of the question, it is offered as a reading and not as a resolution.

**Features or customer value.** Blank, Strategyn and THRV oppose the feature matrix [[34]](#ref-34)
[[35]](#ref-35)[[36]](#ref-36). Product School presents it as one framework among several
[[38]](#ref-38), and Productboard lists a feature comparison matrix among its five frameworks
[[11]](#ref-11). Cagan's prescription sits between the camps: "take the holistic view when
evaluating competitors" [[28]](#ref-28). This library takes the customer-value side for the
comparison section. Klue's sentence "Feature comparison tables double as top-notch sales
battlecards" describes a battlecard and not this analysis [[54]](#ref-54).

**Whether to study rivals at all.** Cagan wrote "So stop chasing your competitors and start focusing
on providing real value for your customers" [[28]](#ref-28). In an interview he advises that teams
"not worry so much about competitors" [[32]](#ref-32). Harshal Patil, a product manager, reads the
advice as "prioritize your customers more than your competitors", and writes "I thought I was being
customer-centric by ignoring competitors" [[33]](#ref-33). Cagan is not on a never-study side. The
same 2011 article asks a product leader to "identify the three key things" each competitor does well
[[28]](#ref-28), and his coaching asks for a written narrative [[29]](#ref-29). Pragmatic Institute
says competitors "shouldn’t define your product strategy" [[45]](#ref-45). The gap between the camps
is emphasis and not yes or no.

**How often to refresh.** The table in the Refresh Trigger and Versions section sets the positions
side by side. None of the sources offers evidence for any interval. Crayon's survey also reports
that teams sharing updates daily or weekly are "75% more likely" to report revenue impact
[[23]](#ref-23). That is a self-reported survey correlation from a vendor that benefits from faster
refresh, and it does not show cause.

**Whether SWOT belongs.** SWOT recurs across vendors, at HubSpot, Atlassian, Miro and Productboard
[[10]](#ref-10)[[13]](#ref-13)[[14]](#ref-14)[[11]](#ref-11). This library keeps it out of the
template, because a SWOT assesses our own company, and this document is about the others. That
reason is this library's, and not any source's. Pragmatic Institute makes a related point: "SWOT
will not help you set the product objectives because it assumes you have already set them."
[[44]](#ref-44)

**Who owns it.** The product manager at GitLab [[19]](#ref-19) and marketing in Crayon's survey
[[23]](#ref-23) differ, probably because the purposes differ. Pragmatic Institute says product
managers are often responsible for competitive analysis [[49]](#ref-49).

**What the name means.** The vendors use one name for several forms, and GitLab separates an
evaluation of solutions from an analysis of companies
[[20]](#ref-20)[[9]](#ref-9)[[10]](#ref-10)[[14]](#ref-14).

**What to treat as time-bound.** HubSpot's page carries an update dated 01/09/26 [[10]](#ref-10).
The Aha! post that gives the six-column set shows Sept 2023 dates in its page text, and its exact
post date was not confirmed [[18]](#ref-18). Aha!'s template count moved between its 2018 post and
its current guide [[17]](#ref-17)[[9]](#ref-9). Calven's page is dated 13 November 2026
[[51]](#ref-51), and Customer Impact's page was updated on 20 October 2026 [[52]](#ref-52). Crayon's
figures are from its 2025 survey [[23]](#ref-23). Treat each as the state of that page on that date.

## 7. Anti-patterns and failure modes

The log records no measurement of how often any of these occurs. Each is named by a source or is
this library's reading, and every source is cited as the one that names it.

- **A feature checklist.** Comparing rivals on the features they chose, and not on what the chosen
  customers value. Named by Blank, Strategyn and THRV [[34]](#ref-34)[[35]](#ref-35)[[36]](#ref-36).
- **Leaving out the status quo.** Customer Impact says most teams forget it [[52]](#ref-52). Dunford
  and Pragmatic Institute place it among the alternatives [[43]](#ref-43)[[46]](#ref-46).
- **A guessed cell.** Calven says an invented number "looks like knowledge" and is worse than an
  empty cell [[51]](#ref-51).
- **A comparison nobody refreshes.** Dovetail lists "failing to update or spot-check data" as a
  common mistake [[27]](#ref-27), and Calven says a profile built once is "usually wrong within a
  quarter" [[51]](#ref-51). The quarter is an unmeasured vendor claim.
- **A project and not a programme.** Octopus Intelligence says a battle card fails when it is "built
  as a project rather than maintained as a programme" [[37]](#ref-37). That sentence is about battle
  cards, so treat it as a pointer for this document, not a finding about it.
- **Recording every move.** Aha!'s 2018 post warns against recording every competitor move and
  against obsessing over competitors versus customers [[17]](#ref-17). Its later post says "This
  does not mean monitoring competitors around the clock." [[18]](#ref-18)
- **Letting the analysis set the strategy.** Competitors "shouldn’t define your product strategy"
  [[45]](#ref-45).
- **Findings with no next step.** Customer Impact advises ending each finding in a move with an
  owner and a date [[52]](#ref-52).
- **Relying on one input.** Klue warns "Don't just rely on CRM data" [[54]](#ref-54).
- **Treating a vendor's interval as the consensus.** No interval is measured, and every one but
  GitLab's comes from a vendor [[19]](#ref-19)[[54]](#ref-54)[[18]](#ref-18)[[26]](#ref-26).
- **Presenting a survey figure as cause.** Crayon's "75% more likely" is a vendor's self-reported
  correlation [[23]](#ref-23).
- **Skipping the legal check.** GitLab requires a check of competitors' acceptable use policies
  before using their products [[19]](#ref-19).

## 8. Relationships to other artifacts

**Named sources state a boundary for only some neighbours.** NN/g states one for competitive
usability testing [[40]](#ref-40), Dunford states one for positioning [[43]](#ref-43), and Pragmatic
Institute separates trend analysis, win/loss, strategy, market definition and positioning by listing
them as distinct elements [[45]](#ref-45)[[46]](#ref-46). The research found no source that states a
boundary with the Lean Canvas, with market sizing, or between the analysis and a battlecard beyond
describing the battlecard. Confidence: high on the quotations; medium on the inferences marked
below.

**Position in the family chain.** The [strategy-docs family
contract](../../docs/internal/contracts/strategy-docs.md) lists eight members in order: the product
vision, the Lean Canvas, the product strategy, the competitive analysis, the positioning statement,
the North Star metric, the product roadmap and the OKRs. The analysis's place, after the strategy
and immediately before the positioning statement, is this library's POSITION. No source states the
sequence, and the place rests on the positioning statement's guide, which names the analysis as
upstream work. The analysis joined the family under [ADR 0091 (competitive analysis joins
strategy-docs as an eighth
member)](../../docs/internal/decisions/0091-competitive-analysis-joins-strategy-docs-as-an-eighth-member.md).
The `foundation` classification, read as a dated snapshot refreshed on triggers, is the considered
alternative to its `utility` one. The family contract holds that a positioning statement built
without a current competitive analysis names an alternative nobody has compared, and that link is
also the library's POSITION.

**Product strategy (before it).** The analysis is an input to strategy and does not set it
[[45]](#ref-45)[[30]](#ref-30). The [product strategy
companion](../product-strategy/product-strategy_companion.md) covers the strategy, which chooses the
segment and problems. That this analysis takes the chosen segment as its scope is this library's
POSITION. In this library's [strategy example](../product-strategy/product-strategy_example.md), a
competitor announcement is not itself a trigger to revisit the strategy, so a competitor's move
refreshes this analysis instead.

**Positioning statement (after it).** Dunford works from competitive alternatives, not every
competitor [[43]](#ref-43). Pragmatic Institute's third positioning pillar is "meaningful
differentiation relative to real alternatives" [[48]](#ref-48). This library's inference, at medium
confidence, is that the analysis covers the wider field and the positioning statement takes the real
alternatives from it. See the [positioning statement
companion](../positioning-statement/positioning-statement_companion.md).

**Vision, Lean Canvas, North Star metric, roadmap and OKRs.** The research found no source that
states a boundary between this document and the Lean Canvas, and none for the vision, the North Star
metric or the OKRs. Pragmatic Institute says market analysis, a neighbour, should inform positioning
and the roadmap [[44]](#ref-44). The positions below are therefore this library's reading, built
from the family chain and the sections above.

- **Product vision.** The vision sits at the top of the chain, and this analysis sits well downhill
  of it. That is this library's POSITION and rests on chain order alone.
- **Lean Canvas.** The canvas comes second in the chain, before the strategy, and this analysis
  comes after the strategy. That is this library's POSITION and rests on chain order alone.
- **North Star metric.** The metric comes after the positioning statement, so this analysis sits two
  places upstream of it. That is this library's POSITION and rests on chain order alone.
- **Product roadmap.** The Implications section routes findings to the strategy, the positioning or
  the roadmap. That routing is this library's POSITION, and Pragmatic Institute's statement about
  market analysis is the nearest source for it [[44]](#ref-44).
- **OKRs.** The OKRs come last in the chain, downstream of this analysis. That is this library's
  POSITION and rests on chain order alone.

**Market trend analysis and market sizing.** Pragmatic Institute separates competitive analysis from
trend analysis: "they answer different questions" [[45]](#ref-45). It lists market definition as its
own element: "Which segment is most likely to buy, and is it big enough?" [[46]](#ref-46) It also
says "Market analysis differs from market research" [[44]](#ref-44). None of the sources says
whether sizing sits inside a competitive analysis.

**Win/loss analysis.** Pragmatic Institute defines it as evidence on "why recent evaluators did or
didn’t buy from you", and says "Have someone outside sales run the interviews" [[47]](#ref-47). Its
framework lists win/loss beside the competitive landscape as a separate element [[46]](#ref-46).
GitLab feeds a win/loss provider into its competitive intelligence [[21]](#ref-21). This library's
inference, at medium confidence, is that win/loss is buyer evidence from real deals, and it can
correct which competitors the analysis includes.

**Sales battlecard.** Pragmatic Institute writes "Battle cards are internal documents", built as
"simple one-page battle cards" [[50]](#ref-50). It advises that teams "arm your sales team with
talking points acknowledging a competitor’s strengths and then counter them" [[49]](#ref-49).
Productboard's brief ends in a battlecard summary, and HubSpot's kit includes a "Competitor Battle
Card" [[12]](#ref-12)[[10]](#ref-10). Product Marketing Alliance's battlecard has sections such as
"Key differentiators", "Why you win" and "Pricing overview" [[16]](#ref-16). None of the sources
says a battlecard is not a competitive analysis. The direction, analysis upstream and battlecard
downstream, is this library's inference.

**Competitive usability testing and competitive reviews.** NN/g writes "Competitive testing is not
the same as a competitive review." [[40]](#ref-40) Testing "requires that designs be tested with
actual users" [[40]](#ref-40). In a review, "a usability expert takes an in-depth look at a series
of related products" [[39]](#ref-39). NN/g says "the main goal of a competitive evaluation is not to
declare a winner" [[39]](#ref-39), and its testing guidance says "not to crown a winner"
[[41]](#ref-41). A video from NN/g carries a summary line saying "There is more than one way to
conduct a competitive evaluation." and no transcript, so it supports only that a difference exists
[[42]](#ref-42). A competitive usability study is research, and the analysis may cite its findings.

**Benchmarking.** NN/g uses the word for a recurring UX measurement: "Benchmarking is often a
program rather than a one-time activity" [[56]](#ref-56). That is why the template does not use
*benchmarking report* as an alias. BABOK lists benchmarking as a technique with market analysis
[[2]](#ref-2).

## 9. Adaptations

The research read little that bears on adaptation, so this section records only what it read.

- **A short form for a small team.** Atlassian's template is a one-page, you-versus-competitor
  document [[13]](#ref-13). The lean variant is this library's short form.
- **Who owns it.** Product at GitLab [[19]](#ref-19), marketing in Crayon's survey [[23]](#ref-23).
  Pick by purpose, and name the owner in the refresh section either way.
- **Tiered refresh.** HubSpot's practice, relayed by Klue, refreshes tiers on different clocks
  [[22]](#ref-22). The refresh section may adopt this.
- **A UX-research reading.** Dscout's sheet scores user goals and pain points and adds a heuristic
  evaluation [[15]](#ref-15). It has no competitor profile columns, so it is a different document
  under the same name.
- **A downstream sales view.** The battlecard is a one-page sales tool
  [[16]](#ref-16)[[50]](#ref-50). That it sits downstream of the analysis is this library's
  inference.
- **Regulated work, and the legal check.** The research did not cover regulated settings. GitLab's
  own requirement of a legal check of competitors' acceptable use policies is an adjacent practice
  it did find [[19]](#ref-19).
- **Sharing.** GitLab publishes product comparison pages un-gated [[21]](#ref-21). Whether this
  analysis should be shared that widely is not something the research settled.
- **Licence.** This library describes what the vendor templates contain and copies none of their
  tables, column orders or wording.

## 10. Worked example

[`competitive-analysis_example.md`](competitive-analysis_example.md) continues this library's single
Acme Analytics thread. It is Acme's competitive analysis for the segment the product strategy
example chose, someone at a 50-500 person company with no data team. Its first version is dated
2026-01-29, between the FY26 strategy and the positioning statement, so the positioning statement is
built on a current analysis. A later dated version inside the same fiscal year shows a refresh. Its
competitor set matches the positioning statement's alternatives, and it names no real vendor.

## References

Every source below is marked fetched-and-verified in the research log. Where a page was read only in
part, the entry says so, and nothing beyond what was read is claimed.

<a id="ref-1"></a>[1] Wikipedia contributors - ["Competitor analysis"](https://en.wikipedia.org/wiki/Competitor_analysis). Cached copy fetched 2026-11-14; the article carries a banner dated April 2013 asking for more citations, so it is a lead. [reference]

<a id="ref-2"></a>[2] IIBA - ["Preface" of the BABOK Guide, table of contents of the Business Analysis Standard](https://www.iiba.org/knowledgehub/the-business-analysis-standard/preface/). Only the table of contents was readable. [standards]

<a id="ref-3"></a>[3] IIBA - ["10.4 Benchmarking and Market Analysis"](https://www.iiba.org/knowledgehub/business-analysis-body-of-knowledge-babok-guide/10-techniques/10-4-benchmarking-and-market-analysis/). Only the title and numbering were read; the technique text is not on the page. [standards]

<a id="ref-4"></a>[4] Michael E. Porter, Harvard Business Review, March-April 1979 - ["How Competitive Forces Shape Strategy"](https://hbr.org/1979/03/how-competitive-forces-shape-strategy). Public abstract page only, not the full article. [primary]

<a id="ref-5"></a>[5] Wikipedia contributors - ["Porter's five forces analysis"](https://en.wikipedia.org/wiki/Porter%27s_five_forces_analysis). [reference]

<a id="ref-6"></a>[6] Wikipedia contributors - ["SWOT analysis"](https://en.wikipedia.org/wiki/SWOT_analysis). [reference]

<a id="ref-7"></a>[7] Wikipedia contributors - ["Michael Porter"](https://en.wikipedia.org/wiki/Michael_Porter). [reference]

<a id="ref-8"></a>[8] Aha! - ["Competitive analysis Template - Create a Competitive analysis"](https://www.aha.io/roadmapping/guide/templates/create/competitive-analysis). The template body needs a trial sign-up; the page text was read. [vendor]

<a id="ref-9"></a>[9] Aha! - ["Competitive Analysis Templates: Options for Product Teams"](https://www.aha.io/roadmapping/guide/templates/competitor-analysis). [vendor]

<a id="ref-10"></a>[10] HubSpot - ["10 Free Competitive Analysis Templates"](https://blog.hubspot.com/marketing/competitive-analysis-kit). The page carries "Updated: 01/09/26"; the template files sit behind a form and were not read. [vendor]

<a id="ref-11"></a>[11] Productboard - ["Competitor Analysis: Framework, Template & Best Practices"](https://www.productboard.com/glossary/competitor-analysis/). [vendor]

<a id="ref-12"></a>[12] Productboard - ["Competitor Intelligence Brief"](https://www.productboard.com/product-management-prompts-library/competitor-intelligence-brief/). [vendor]

<a id="ref-13"></a>[13] Atlassian - ["Competitive Analysis Template & Overview"](https://www.atlassian.com/software/confluence/templates/competitive-analysis). Read from the how-to steps; the template body is not shown. [vendor]

<a id="ref-14"></a>[14] Miro - ["Free Competitive Analysis Templates & Examples"](https://miro.com/templates/competitive-analysis/). A collection page, not a template body. [vendor]

<a id="ref-15"></a>[15] Nikki Anderson, Dscout, 5 December 2023 - ["UXR Competitive Analysis Template"](https://dscout.com/people-nerds/competitive-analysis-template). The spreadsheet is behind a download step; the page's summary was read. [practitioner]

<a id="ref-16"></a>[16] James Shaw, Product Marketing Alliance, 14 May 2023 - ["Sales battlecard template"](https://productmarketingalliance.com/battlecard-template). The files are members-only; the page's section list was read. [practitioner]

<a id="ref-17"></a>[17] Ron Yang, Aha!, 22 October 2018 - ["The Best Templates for Product Managers to Complete Competitive Analysis"](https://www.aha.io/blog/product-competitive-analysis-template). [vendor]

<a id="ref-18"></a>[18] Aha! - ["New product management template: Competitive analysis"](https://www.aha.io/blog/new-product-management-template-competitive-analysis). The page text shows Sept 2023 dates; the exact post date was not confirmed. [vendor]

<a id="ref-19"></a>[19] GitLab Handbook - ["Category Maturity - Competitor Comparison"](https://handbook.gitlab.com/handbook/product/ux/category-maturity/competitor-comparison/). [practitioner]

<a id="ref-20"></a>[20] GitLab Handbook - ["Competitor Evaluations"](https://handbook.gitlab.com/handbook/product/ux/competitor-evaluations/). Last modified 2026-02-23. [practitioner]

<a id="ref-21"></a>[21] GitLab Handbook - ["Competitive Intelligence"](https://handbook.gitlab.com/handbook/marketing/brand-and-product-marketing/product-and-solution-marketing/competitive-intelligence/). Last modified 2026-10-30 per the page footer. [practitioner]

<a id="ref-22"></a>[22] Adam McQueen, Klue, 17 Sep 2023 - ["Updating Your Battlecards | Compete Confidential (CE LIVE) | Shoulda Done It"](https://klue.com/newsletter/updating-your-battlecards-compete-confidential-ce-live-shoulda-done-it). A relayed customer cadence, not Klue's own. [vendor]

<a id="ref-23"></a>[23] Crayon - ["State of Competitive Intelligence 2025"](https://www.crayon.co/hubfs/Crayon%27s%202025%20State%20of%20CI%20Report.pdf). A PDF, read as extracted text; vendor survey, self-reported. [vendor]

<a id="ref-24"></a>[24] Shannon De Marco, Crayon, 25 February 2025 - ["Outdated Battlecards are a Thing of the Past: Automate Your Compete Program With Sparks Content"](https://www.crayon.co/blog/sparks-content). The 26% figure is quoted on the page without a methodology. [vendor]

<a id="ref-25"></a>[25] Aha! - ["How product managers should research competitors"](https://www.aha.io/roadmapping/guide/product-strategy/how-should-product-managers-research-competitors). [vendor]

<a id="ref-26"></a>[26] Dovetail Editorial Team, last updated 21 March 2024 - ["Analyzing your competitor's products with a competitive product analysis"](https://dovetail.com/product-development/how-to-do-a-product-competitive-analysis). [vendor]

<a id="ref-27"></a>[27] Dovetail, last updated 3 April 2024 - ["Conducting an effective competitor audit"](https://dovetail.com/market-research/competitor-audit). [vendor]

<a id="ref-28"></a>[28] Marty Cagan, Silicon Valley Product Group, 2 August 2011 - ["Competition"](https://www.svpg.com/competition/). [practitioner]

<a id="ref-29"></a>[29] Marty Cagan, Silicon Valley Product Group, 22 April 2019 - ["Coaching Tools - The Plan"](https://www.svpg.com/coaching-tools-the-plan/). [practitioner]

<a id="ref-30"></a>[30] Marty Cagan, Silicon Valley Product Group - ["Product Strategy - Overview"](https://www.svpg.com/product-strategy-overview/). [practitioner]

<a id="ref-31"></a>[31] Marty Cagan, Silicon Valley Product Group - ["Product Strategy - Insights"](https://www.svpg.com/product-strategy-insights/). [practitioner]

<a id="ref-32"></a>[32] Dovetail - ["Getting in front of the customer with Marty Cagan"](https://dovetail.com/outlier/getting-in-front-of-the-customer-with-marty-cagan/). An interview. [practitioner]

<a id="ref-33"></a>[33] Harshal Patil, Substack, 2 July 2025 - ["When Customer-First Fails, Use A Competitor Research Power-Up"](https://harshalpatil.substack.com/p/use-competitive-research-not-just-customer-insights). [practitioner]

<a id="ref-34"></a>[34] Steve Blank, 1 March 2010 - ["Death By Competitive Analysis"](https://steveblank.com/2010/03/01/death-by-analysis/). [practitioner]

<a id="ref-35"></a>[35] Strategyn - ["Competitive Analysis"](https://strategyn.com/competitive-analysis/). Tony Ulwick's firm, which sells a jobs-to-be-done method. [vendor]

<a id="ref-36"></a>[36] THRV - ["Stop the downward spiral of feature-to-feature comparison"](https://thrv-cms.vercel.app/blog/stop-the-downward-spiral-of-feature-to-feature-comparison). Read on a content-system mirror; no author shown, so attribution is weak. [vendor]

<a id="ref-37"></a>[37] Octopus Intelligence - ["CRO Competitive Intelligence Example: Your Battle Cards Are Out of Date Before the Ink Is Dry"](https://www.octopusintelligence.com/cro-competitive-intelligence-example-your-battle-cards-are-out-of-date-before-the-ink-is-dry/). A fresh fetch returned empty text, so the quotations rest on the cached copy. [vendor]

<a id="ref-38"></a>[38] Product School - ["Product Manager Competitive Analysis"](https://productschool.com/blog/skills/product-manager-competitive-analysis). [vendor]

<a id="ref-39"></a>[39] Nielsen Norman Group - ["Competitive Usability Evaluations: Definition"](https://www.nngroup.com/articles/competitive-usability-evaluations/). [practitioner]

<a id="ref-40"></a>[40] Nielsen Norman Group - ["Parallel & Iterative Design + Competitive Testing = High Usability"](https://www.nngroup.com/articles/parallel-and-iterative-design/). [practitioner]

<a id="ref-41"></a>[41] Nielsen Norman Group - ["Competitive Usability Testing to Discover Better Designs"](https://www.nngroup.com/articles/redesign-competitive-testing/). [practitioner]

<a id="ref-42"></a>[42] Therese Fessenden, Nielsen Norman Group, 2024-07-03 - ["Competitive Reviews vs. Competitive Research"](https://www.nngroup.com/videos/competitive-reviews-vs-competitive-research/). A video page with a summary line only, no transcript. [practitioner]

<a id="ref-43"></a>[43] April Dunford, 2020-12-28 - ["Positioning and Competition"](https://aprildunford.substack.com/p/positioning-and-competition). [practitioner]

<a id="ref-44"></a>[44] Pragmatic Institute - ["Choosing a Market Analysis Framework (SWOT and Six Forces)"](https://www.pragmaticinstitute.com/resources/articles/product/doing-market-analysis-easy-right/). [practitioner]

<a id="ref-45"></a>[45] Pragmatic Institute - ["A Product Manager's Guide to Market Trend Analysis"](https://www.pragmaticinstitute.com/resources/articles/product/a-product-managers-guide-to-market-trend-analysis/). [practitioner]

<a id="ref-46"></a>[46] Pragmatic Institute - ["Product Management Framework"](https://www.pragmaticinstitute.com/product/framework/). [practitioner]

<a id="ref-47"></a>[47] Pragmatic Institute - ["The Ultimate Guide to Win/Loss Analysis"](https://www.pragmaticinstitute.com/product/framework/win-loss-analysis/). [practitioner]

<a id="ref-48"></a>[48] Pragmatic Institute - ["Product Positioning Strategies for Competitive Markets"](https://www.pragmaticinstitute.com/resources/articles/product/product-positioning-strategies-for-competitive-markets/). [practitioner]

<a id="ref-49"></a>[49] Pragmatic Institute - ["Competitive Strategy from Strength to Weakness"](https://www.pragmaticinstitute.com/resources/articles/product/ask-the-experts-how-do-you-find-the-weakness-in-a-competitors-strength/). Ask the Experts. [practitioner]

<a id="ref-50"></a>[50] Pragmatic Institute - ["Advanced Strategy For Building Effective Sales Battle Cards"](https://www.pragmaticinstitute.com/advanced_strategy_for_building_effective_sales_battlecards_21-09/). A PDF, read as text; the example competitor in it is fictitious. [practitioner]

<a id="ref-51"></a>[51] David Kolinek, Calven, dated 13 November 2026 - ["Competitor Analysis Template: How to Fill In Every Field"](https://calven.ai/resources/competitive-intelligence/competitor-analysis). Vendor of an AI product-marketing platform. [vendor]

<a id="ref-52"></a>[52] Tanguy De Keyzer, Customer Impact, updated 20 October 2026 - ["B2B Competitive Analysis: Step-by-Step"](https://www.customerimpact.be/en/blog/how-to-do-b2b-competitive-analysis/). A consultancy blog. [vendor]

<a id="ref-53"></a>[53] Wikipedia contributors - ["Admiralty code"](https://en.wikipedia.org/wiki/Admiralty_code). The article carries a single-source banner, so it is a pointer to the convention and not the standard's text. [reference]

<a id="ref-54"></a>[54] Klue - ["How to Do a Competitive Landscape Analysis"](https://klue.com/blog/competitive-landscape-analysis-guide). Read in admission sweep 8, 2026-11-14. [vendor]

<a id="ref-55"></a>[55] Klue - ["How to Conduct a Competitive Analysis on Top Rivals"](https://klue.com/topics/do-a-competitive-analysis). Read in admission sweep 8, 2026-11-14. [vendor]

<a id="ref-56"></a>[56] Nielsen Norman Group - ["7 Steps to Benchmark Your Product's UX"](https://www.nngroup.com/articles/product-ux-benchmarks/). Read in admission sweep 8, 2026-11-14. [practitioner]
