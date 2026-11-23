# competitive-analysis: research log

Research conducted 2026-11-22. It builds on admission sweep 8 of 2026-11-14, held in a gitignored folder under
`_local/research/`, and on
[ADR 0091](../../docs/internal/decisions/0091-competitive-analysis-joins-strategy-docs-as-an-eighth-member.md)
(competitive analysis joins strategy-docs as an eighth member). It also builds on the family contract
(`docs/internal/contracts/strategy-docs.md`) and on the spec, the section of `docs/internal/tier2-specs.md` headed
"strategy-docs (eighth member, by amendment): the competitive analysis". The maintainer accepted ADR 0091 on
2026-11-14, which ruled the family and `classification: utility`. The maintainer confirmed its chain place,
immediately before the positioning statement, on 2026-11-17. The maintainer ruled every remaining choice in the spec
as recommended on 2026-11-20 ("ok to all"). Those rulings are: sizes `lean` and `full` with `lean` the default, an Acme Analytics example for the
Recurring Analyst segment with its first version dated 2026-01-29, a sentence for this member's example in the
contract's section 4, and SWOT kept out. This bundle is issue #361 (bundle: competitive-analysis), and it fills
catalog entry 11.

The build ran six dimensions: origins, structure, practice, debates, relationships, and the standing gap question.
The working files are numbered by return order: `dim1.md` holds the gap question, `dim2.md` origins, `dim3.md`
practice, `dim4.md` debates, `dim5.md` relationships and `dim6.md` structure.

**56 sources are recorded below, and all 56 are fetched-and-verified.** By tier they are 25 practitioner, 23
vendor, 5 reference, 2 standards and 1 primary. **The entries carry 197 quotations, and every one was tested
against the cached raw text of its page.** The 153 quotations that this build's research agents returned all passed
a strict raw check. The rest were carried from admission sweep 8 and from the spec's reads of 2026-11-17.

## What the checks caught, and what was not read

**Three carried quotations had been attached to the wrong page, and the generator dropped them there.** The
sentence from NN/g that separates competitive testing from a competitive review sits on one NN/g article, entry
[40]. It had also been carried onto two sibling NN/g articles, [39] and [41], and failed on both. Aha!'s two framing
questions sit on its whiteboard template page [8], not on its ten-template guide [9], where they also failed. Each
quotation survives only on the page that holds it.

**A cadence misquote in ADR 0091 and the family contract was caught while the spec was written.** Both had quoted
GitLab's annual interval without its condition. The raw page ties the interval to a category at its most mature
level, and names an event for every other category. The spec records the correction. A grep of both files found the dated note of 2026-11-17 in each. The finding is set out under Practice below.

**One dimension's null finding was false across the whole source list.** The practice dimension found no source
that prescribes a source and a date for each claim. The gap dimension found one: Calven's template asks for where
each claim came from, and when [51]. Calven sells an AI product-marketing platform, so the finding is a vendor's.
The structure dimension's claim that a narrative brief appears only at Productboard holds for the vendor templates
read, but SVPG also asks for a narrative [29].

**Several pages were readable only in part.** BABOK's technique 10.4 page returned its title and the table of
contents, not the technique's text [3]. Porter's 1979 article was read as its public abstract only [4]. Aha!'s
whiteboard template body needs a trial sign-up, and HubSpot's ten templates sit behind a download form, so their
fields were read from the pages that describe them [8], [10]. Atlassian's page was read from its how-to steps, not
the template body [13]. NN/g's video on competitive reviews and competitive research carries only a summary line
[42]. Crayon's 2025 report is a PDF, read as extracted text [23]. The recheck's fresh fetch of Octopus Intelligence's page
returned empty text, so its three quotations rest on the cached copy [37].

**Repository files read, not listed as sources.** The spec section was read whole. The family contract and ADR
0091 were grepped for the GitLab note only. The `product-strategy` example (lines 40-70, 95-105 and 139-142), the
`positioning-statement` example (lines 50-65 and 100-112) and the `positioning-statement` guide (lines 85-92) were
read to check the example's required facts. They are cited below by path, not by number, and the line references
in the example paragraph are the spec's.

**Pages wanted and not read.** Dunford's own site and her book, Ash Maurya's Lean Canvas page, a BABOK v2 draft
that a search summary mentioned, Cagan's books, a Forbes article on the status quo and the US intelligence
community's confidence standard were all found and not read. The tail of this log lists the blocked pages.

## Findings

### What the type is

This library's reading, taken from the spec, is that a competitive analysis says who else serves the customers a
strategy chose, compares them, and says what that means for the product's direction. Aha! frames it as two questions: "How do our products and services compare to the
alternatives? And how can we better differentiate what we offer?" [8] Productboard calls it "the ongoing practice of
researching and evaluating competing products, companies, and market alternatives" [11]. The encyclopedia
definition is narrower: "the assessment of the strengths and weaknesses of current and potential competitors" [1].
Confidence: high that these are the sources' words; medium that they describe one document.

**The audience is product teams.** Aha!'s template "is for product managers and product marketers" [8]. At GitLab,
"A Product Manager will lead their quad team" [19].

**GitLab splits the name in two.** A competitor evaluation compares solutions: "It evaluates solutions." A
competitor analysis compares business models and positioning: "A competitor analysis evaluates companies." [20]
Aha!'s ten templates run from company profiles to feature analyses under one name [9]. Productboard's definition
covers "competing products, companies" alike [11]. This library's reading is that
the bundle holds both: profiles of companies, and a comparison of what their products do for the chosen customers.

### Origins: strategy writing, BABOK and the missing first document

**Competition was a subject of strategy writing by 1979.** Porter's *How Competitive Forces
Shape Strategy* appeared in Harvard Business Review in 1979, and opens "The essence of strategy formulation is
coping with competition." [4] His book *Competitive Strategy* followed in 1980 [7]. Wikipedia reports that "Porter
developed his Five Forces Framework in response to the then-prevalent SWOT analysis" [5]. These sources are cited for
existence and date only. The full 1979 text was not read. Confidence: high.

**SWOT's own origin is disputed.** Wikipedia credits a 1965 Stanford Research Institute report through some
authors, and reports the Harvard-origin story as an "academic urban legend" in Puyt et al.'s account [6]. Only
Wikipedia's account of the dispute was read. The encyclopedia article on competitor analysis calls it "an essential
component of corporate strategy" and lists technique steps [1]. That article carries a 2013 banner asking for more
citations, so it is a lead, not evidence.

**BABOK has no technique titled Competitive Analysis.** The current BABOK Guide's chapter 10 lists 50 techniques.
Technique 10.4 is "10.4 Benchmarking and Market Analysis", and SWOT is "10.46 SWOT Analysis" [2]. A case-insensitive
search of the table of contents for the word *competitive* found nothing [2]. The 10.4 page confirmed only its title [3]. A
technique is a way of doing analysis work, not a written document. Under ADR 0030 (templating scope: Markdown
documents) a technique cannot count as an origin for a document type. Confidence: high on the title and number; low
on what 10.4 says, which was not read.

**The catalog's BABOK note does not survive.** Catalog entry 11 cites a BABOK technique 10.4 in its note. The
number exists, but the technique's title is Benchmarking and Market Analysis, and it is a technique [2], [3]. The
spec lists the note among the corrections the landing PR should check.

**No first written competitive analysis for product teams was established.** The origins dimension ran one web
search for who first described such a document or template, and found no source naming one. The companion must not
name an originator.

### Structure: what readable templates put in a competitive analysis

**The name covers several documents, and no two vendors share a field set.** Aha!'s guide offers "10 competitive
analysis templates for product teams" [9]. HubSpot's kit names ten as well [10]. Miro lists over ten [14].
Confidence: high on what each page says; medium on the grouping below, which is the structure dimension's reading.

| Publisher | Form | What the page says it holds |
|---|---|---|
| Aha! whiteboard [8], [18] | A per-competitor table plus a scorecard | "mission statements, pricing, top features, strengths, weaknesses, and differentiators", which the blog calls "six columns" [18] |
| Aha! guide [9] | Ten templates in several forms | Profiles, a "Competitor scorecard", a "Competitor overview", a "Capabilities analysis", a "Features analysis" with "Harvey Balls", an "Imitability analysis" and a "Competitive differentiation analysis" |
| Aha! 2018 blog [17] | Nine approaches | Includes a "Value proposition analysis", which the current guide does not list |
| HubSpot kit [10] | Ten named templates, fields not shown | Includes "Competitor Battle Card", "Multiple Competitor Feature Comparison", "SWOT Analysis Template" and a "Content Marketing Analysis Template" |
| Productboard glossary [11] | No template despite its title | Eight "Key Components of Competitor Analysis", a matrix, and five frameworks including a "Positioning Map" |
| Productboard brief [12] | A narrative brief on one competitor | Six sections, from "COMPANY OVERVIEW" to "SALES BATTLECARD SUMMARY", and a "last updated" note with a "recommended refresh cadence" |
| Atlassian [13] | A one-page you-versus-competitor document | A profile table with a tier weight, a "Competitive Advantage" section, product and marketing tables, and a "SWOT analysis" |
| Miro [14] | A collection of shapes | A "Competitive Analysis Matrix", a "Competitive Analysis Table", "Competitive Advantage [MOATs]" and "Competitor Tiers" |
| Dscout [15] | A UX-research sheet | Goals and pain points scored on a "0 to 5 scale", and a step to "Conduct a heuristic evaluation" |
| Product Marketing Alliance [16] | A sales battlecard | Sections such as "Key differentiators", "Why you win" and "Pricing overview" |

**Four findings follow.**

- **The modal artifact is a competitor-by-attribute grid**, with pricing, features, strengths, weaknesses and
  differentiators per competitor [8], [9], [11], [13], [14]. That is the structure dimension's inference from six
  publishers, at medium-low confidence. None of the 56 entries states which form is most common.
- **A three-level rating on capability, not yes or no, appears at two publishers.** Productboard's matrix rates a feature "fully
  supported", "partially supported" or "not available" [11]. Calven's template uses the same three levels [51].
- **Weighting by what customers value appears at Aha!.** Its scorecard is "weighted by the importance of each
  attribute to your customers" [9].
- **SWOT recurs across vendors**, at HubSpot, Atlassian, Miro and Productboard [10], [13], [14], [11]. The spec
  rules it out because a SWOT assesses our own company. That reason is the spec's, not the sources'.

**Even one vendor's set moved over time.** Aha!'s 2018 post lists nine approaches with a "Value proposition
analysis" [17], and its current guide lists ten without one [9].

**No vendor page read exposes the full column set of its download.** Five publishers in the table sell software: Aha!,
HubSpot, Productboard, Atlassian and Miro. Their field lists are vendors' structures. The structure dimension recorded that null for
Aha!, HubSpot, Product Marketing Alliance and Dscout [8], [10], [16], [15]. Only field names, as short quotes, are
recorded here.

### Practice: ownership, evidence and how often it is refreshed

**None of the 56 entries offers evidence for any refresh interval, and the stated intervals do not converge.** Every interval
below is an opinion or a self-reported survey figure. Nearly every one comes from a publisher that sells software.
Confidence: medium.

| Who | Interval or rule | Interest |
|---|---|---|
| GitLab, product side [19] | "should be done at least annually if you're at Complete"; "Otherwise, when you intend to make a category shift" | Uses the practice; does not sell competitive-intelligence tooling |
| GitLab, marketing side [21] | Continuous open editing, no fixed interval: staff "update, correct, amend and comment" | Same publisher |
| Klue [54] | "Quarterly is a solid default." | Sells competitive-intelligence software |
| HubSpot, relayed by Klue [22] | "Tier one and two competitors, we update our battlecards every quarter." "The rest we update every six months." | Klue sells competitive-intelligence software; the cadence is for battlecards |
| Aha! 2018 [17] | A possible "quarterly deliverable" | Sells product-management software |
| A later Aha! post (its page text shows September 2023 dates) [18] | "revisit and refresh your competitive analysis biannually" | Same publisher, a second interval |
| Dovetail [26], [27] | "Once a year.", "Once a quarter." or "Based on specific events."; audits "monthly, quarterly, or annual" | Sells research-repository software |
| Crayon survey [23], [24] | Sharing with sales most often monthly; "only 26% of CI teams update battlecards monthly" | Sells competitive-intelligence software; the figures concern battlecards and sharing with sales |
| Calven [51] | "A profile built once is usually wrong within a quarter." | Sells an AI product-marketing platform |

**The GitLab cadence correction.** ADR 0091 and the family contract had quoted GitLab's "should be done at least
annually" as a general cadence [19]. The raw page reads "should be done at least annually if you're at Complete",
then "Otherwise, when you intend to make a category shift" [19]. So GitLab's annual interval applies to a product
category at its most mature level. For every other category, GitLab names an event, not an interval. GitLab also
recommends an early comparison, before a category matures [19]. Confidence: high, from the raw page. The `utility`
classification does not depend on this interval.

**Among the 56 entries, GitLab's is the only refresh interval from an entry not tiered vendor, and it is
conditional.**
The spec asked the build to look for a practitioner's interval. The practice dimension's search for a Pragmatic
Institute or Mind the Product page that gives a cadence or an owner found none. Cagan's coaching exercise gives
no refresh rule [29].

**Ownership: two sources name one owner, and the owner's function is contested.** Two sources, Aha! and GitLab, name
a single owner, and GitLab adds a product marketing manager or developer advocate alongside the product manager
[9], [19]. Aha! says "Assign a point person to keep the report updated throughout the year." [9] Crayon's survey
puts the function with marketing for many respondents: "47% of respondents" say "marketing owns the compete
function", and some respondents without an owner said "nobody really owns CI" [23]. So the owner's function is
contested. Pragmatic Institute's page says product managers are often responsible for competitive analysis [49],
which the practice dimension's search had not found. The function probably differs by purpose: product strategy at
GitLab's product side, sales enablement in Crayon's survey. Naming one owner and the people they consult is this
library's reading. Confidence: medium.

**Crayon's revenue figure is a vendor's survey correlation.** Teams that share updates daily or weekly are "75% more
likely" to report revenue impact [23]. It is self-reported, from a vendor that benefits from faster refresh, and it
does not show cause.

**Evidence.** GitLab says the comparison "should be completely data/evidence driven", and the result is recorded
when teams "Document/update the scoring" [19]. GitLab's marketing page names websites, documentation, demo videos,
customers and competitors as accuracy inputs, and says "all our product comparison pages are un-gated" [21]. GitLab
also requires a legal check of competitors' acceptable use policies before using their products [19]. Aha! lists
company websites, review sites, industry news and press releases as source types [25]. Klue warns "Don't just rely
on CRM data" [54], and Klue's sales guide says "Skip the website fluff" [55]. Dovetail lists "failing to update or
spot-check data" as a common mistake [27].

**Event triggers named.** Dovetail names a new product coming to market, a shift in a competitor's marketing and a
change in customer habits [26]. GitLab names a category shift [19].

### Debates: living or snapshot, features or value, and whether to study rivals

**Living document or dated snapshot.** The living camp, among the pages the debates dimension read, is all vendors.
GitLab's marketing side also edits continuously, as a practice rather than an argument [21]. Octopus Intelligence says a battle card fails
when it is "built as a project rather than maintained as a programme", and that "A battle card is a document.
Competitive intelligence is a process." [37] Product School says competitive analysis "should be a living part of
product culture" [38]. Productboard says it "isn't a one-time project" [11]. HubSpot names "A one-and-done exercise"
as what it is not [10]. Each sells software, training or services. Confidence: high on the words, low on their
independence.

**The snapshot reading has a vendor voice too.** Klue recommends a quarterly refresh. It also says "Competitive
landscape analysis is a snapshot", and calls landscape analyses "temporary snapshots that need refreshes as the
market changes" [54]. Aha! asks for both: "Conduct a high-level competitive analysis on a regular basis." and
"Perform a more detailed analysis to inform major strategic decisions." [8] Pragmatic Institute says the Six Forces
model, like SWOT, "represents a moment frozen in time" [44].

**No named practitioner argues for a one-off snapshot as a principle.** The debates dimension recorded that null.
Cagan's coaching exercise is one narrative of "the top 3-5 players in the space", with no maintenance rule [29]. That
shows a point-in-time default by omission, not a stated position. Cagan's "product strategy is never static" is about
strategy, not competitor documents [30].

**This library's reading reconciles the two with dated versions.** Each refresh is a dated snapshot, and the
document is the series. Klue's pairing of snapshot and refresh is the nearest source [54]. The reconciliation itself
is the library's POSITION.

**Features or customer value.** Steve Blank argues that "a competitive analysis drives a maximum feature set", and
asks for "No feature lists without facts" [34]. Strategyn, Tony Ulwick's firm, says "feature-to-feature comparisons
is no guarantee of success", and assesses "how much better or worse a product is at helping the customer get a job
done" [35]. THRV, a jobs-to-be-done consultancy, calls feature catch-up "a race" it cannot win [36]. Its page shows
no author and sits on a CMS mirror, so attribution is weak. Product School presents the feature matrix as one
framework among several: "Which framework you choose depends on your goal" [38]. Cagan's prescription sits between
the camps: "take the holistic view when evaluating competitors" [28]. Confidence: medium that the feature checklist
is the type's named failure.

**Klue's sentence on feature tables describes a battlecard, not this analysis.** It says "Feature comparison tables
double as top-notch sales battlecards" [54].

**Whether to study rivals at all.** Cagan wrote "So stop chasing your competitors and start focusing on providing
real value for your customers" [28]. In an interview he advises that teams "not worry so much about competitors"
[32]. Harshal Patil, a product manager, reads the advice as "prioritize your customers more than your competitors",
and writes "I thought I was being customer-centric by ignoring competitors" [33]. Cagan is not on a never-study side.
The same 2011 article asks a product leader to "identify the three key things" each competitor does well [28], and
his coaching asks for a written narrative [29]. Pragmatic Institute says "Competitors can provide useful market
intelligence, but they shouldn’t define your product strategy." [45] The gap between the camps is emphasis, not yes
or no.

### Relationships: positioning, battlecards, win-loss and competitive testing

**Named sources state a boundary for only some neighbours.** NN/g states one for competitive usability testing
[40]. Dunford states one for positioning [43]. Pragmatic Institute separates trend analysis, win/loss, strategy,
market definition and positioning by listing them as distinct elements [45], [46]. The relationships dimension found no source that
states a boundary with the Lean Canvas, the battlecard beyond describing it, or market sizing. Confidence: high on
the quotes; medium on the inferences marked below.

**Positioning.** Dunford works from competitive alternatives, not every competitor. She asks "What would a customer
do if your offering didn't exist?", and says "Not Every Competitor is an Alternative" [43]. Competitors that
prospects never consider are "phantom competitors", left out of positioning but watched by the product team [43].
Pragmatic's third positioning pillar is "meaningful differentiation relative to real alternatives" [48]. The
inference, at medium confidence: the analysis may cover the wider field, and positioning takes the narrower set of
real alternatives from it.

**The status quo belongs among the alternatives, on four sources.** Dunford: "the first competitive alternative we
need to beat is the status quo" [43]. Pragmatic's competitive landscape asks "What else could buyers use instead,
including doing nothing?" [46], and its positioning page compares against alternatives "including the option of
doing nothing" [48]. Two competitive-analysis guides say it of this document directly. Customer Impact: "The status
quo is your largest competitor. Most teams forget it." [52] Calven: "Start from competitive alternatives, meaning
what the buyer would use if you didn't exist." [51] Both sell services or software in this area. Placing the status
quo in this bundle's competitor set is the library's POSITION, taken from the positioning statement's named
alternative. Confidence: high that the sources say it; medium on its weight, since two of the four are interested.

**Product strategy.** Pragmatic says competitors "shouldn’t define your product strategy" [45]. Cagan lists "the
competitive landscape" among the insights a strategy draws on [30]. The boundary as stated: the analysis is an input
to strategy, and does not set it. The chain place, after the strategy and before the positioning statement, is the
library's POSITION. None of the 56 entries states the sequence.

**Market trend analysis and market sizing.** Pragmatic separates competitive analysis from trend analysis: "they
answer different questions" [45]. It lists market definition as its own element: "Which segment is most likely to
buy, and is it big enough?" [46] It also says "Market analysis differs from market research" [44]. None of the 56
entries says whether sizing sits inside a competitive analysis.

**Win/loss analysis.** Pragmatic defines it as evidence on "why recent evaluators did or didn’t buy from you", and
says "Have someone outside sales run the interviews" [47]. Its framework lists win/loss beside the competitive
landscape as a separate element [46]. GitLab feeds a win/loss provider into its competitive intelligence [21]. The
inference, at medium confidence: win/loss is buyer evidence from real deals, and it can correct which competitors the
analysis includes.

**Sales battlecard.** Pragmatic: "Battle cards are internal documents", built as "simple one-page battle cards"
[50]. It advises that teams "arm your sales team with talking points acknowledging a competitor’s strengths and then
counter them" [49]. Productboard's brief ends in a battlecard summary [12], and HubSpot's kit includes one [10]. None of
the 56 entries says a battlecard is not a competitive analysis. The direction, analysis upstream and battlecard downstream, is
inferred.

**Competitive usability testing.** NN/g: "Competitive testing is not the same as a competitive review." [40] Testing
"requires that designs be tested with actual users" [40]. In a review, "a usability expert takes an in-depth look at
a series of related products" [39]. NN/g says "the main goal of a competitive evaluation is not to declare a winner"
[39]. It also says "The sites you select do not need to be direct competitors." [41] That last point differs from a
competitive analysis, which follows whom the buyer considers. A competitive usability study is research, and the
analysis may cite its findings.

**Benchmarking.** NN/g uses the word for a recurring UX measurement: "Benchmarking is often a program rather than a
one-time activity" [56]. That is why the spec keeps the alias *benchmarking report* off the list.

### The gap question, routed under decision procedure 12

The gap dimension asked what a strong competitive analysis does that a typical template does not ask for. Its
candidates come from published guidance, not from finished analyses. **It found no published, named, filled-in
competitive analysis to read.** The evidence is two interested vendors, Calven [51] and Customer Impact [52], plus
one borrowed intelligence-community convention [53]. Confidence: medium that the candidates are real elements of
vendor guidance; low that they predict a better document. Each is routed under decision procedure 12 (a property or
section is proposed for a template) to a section the spec already proposes, or to a guide rubric row. No section is
added.

| # | Candidate | Sources | Route |
|---|---|---|---|
| 1 | A source and a date for each claim: "Where each claim came from, and when. Makes the doc auditable." | Calven [51] | A field in section 8, Evidence and Sources |
| 2 | Gaps marked, not guessed: "Every field needs a source you can name, and a blank field beats a guessed one." | Calven [51] | A convention on how claims are written, so a guide rubric row and a TRAP, not a field |
| 3 | A confidence rating on each item of evidence, judged apart from the source | The Admiralty code [53] | Not adopted. No competitive-analysis source read uses one. Recorded here as turned away |
| 4 | The status quo as a named competitor: "The status quo is your largest competitor." | Customer Impact [52], Calven [51], Dunford [43] | Section 2, The Competitor Set |
| 5 | The decision the analysis serves: "Define the decision it serves." | Calven [51] | Section 1, Purpose and Scope |
| 6 | An action per finding: "Let every finding end in one concrete move with an owner and a date" | Customer Impact [52], Calven [51] | Section 7, Implications for Our Direction, with an owner per implication |
| 7 | Competitors tiered, so effort follows the tier | Calven [51], HubSpot via Klue [22], Atlassian's tier weight [13], Miro's "Competitor Tiers" [14] | Section 2 records a tier; section 9 may refresh by tier |
| 8 | A review date: "A profile built once is usually wrong within a quarter." | Calven [51] | Section 9, Refresh Trigger and Versions. The quarter is an unmeasured vendor claim |

**The gap dimension also searched for a source that sets how recent evidence must be, and found none** beyond
Calven's quarter [51].

## Claims flagged contested or time-bound

- **The refresh interval.** GitLab ties an annual minimum to its most mature categories and an event to the rest
  [19]. Klue says quarterly [54]. Aha! said quarterly in 2018 [17] and biannually in a later post (its page text shows September 2023 dates) [18]. Dovetail offers
  annual, quarterly, monthly or event-driven [26], [27]. None is measured, and every one except GitLab's comes from
  a vendor.
- **Living or snapshot.** Vendors argue for a living process [37], [38], [11]. Klue calls the analysis a snapshot
  that needs refreshes [54]. Cagan's exercise is a single narrative [29].
- **Features or value.** Blank, Strategyn and THRV oppose feature matrices [34], [35], [36]. Product School treats
  them as one framework among several [38].
- **Whether to study rivals.** Cagan says to stop chasing them [28]. Patil says ignoring them hurt his work [33].
- **The owner's function.** The product manager at GitLab [19], marketing in Crayon's survey [23].
- **What the name means.** GitLab separates an evaluation of solutions from an analysis of companies [20]. The
  vendors use one name for both, and for up to ten forms [9], [10], [14].
- **Porter's date.** HBR's page gives the March-April 1979 issue [4]. Wikipedia's reference list gives May 1979 in
  one place [5].
- **Time-bound.** HubSpot's page carries an update dated 01/09/26 [10]. Calven's page is dated 13 November 2026 [51],
  and Customer Impact's was updated 20 October 2026 [52]. Crayon's figures are from its 2025 survey [23]. Aha!'s
  template count moved between 2018 and 2026 [17], [9].

## Honest framing

The bundle can say what the sources mean by a competitive analysis, what readable templates put in it, who owns it,
and how its sources disagree on refresh. It cannot say who first wrote one for a product team. It cannot cite BABOK
as a document origin. It cannot name a refresh interval that anyone has measured. **Twenty-three of the 56 sources are
vendor writing, and nearly every refresh interval and template structure the research found comes from a vendor.**
Most of those vendors sell competitive-intelligence or product-management software. The
template's section set is therefore largely the library's POSITION, built from vendor field lists, SVPG's narrative,
GitLab's practice and the positioning sources. The strongest negative finding: no filled-in, published competitive
analysis was read, so every gap candidate is guidance, not observed practice.

## Notes for the companion

**Load-bearing sections.** Section 2 (The Competitor Set) decides what the analysis is about, and it carries the
status quo. Section 5 (Comparison on What Customers Value) is where the feature-checklist trap is avoided or not.
Section 7 (Implications for Our Direction) is what makes it a `strategy-docs` member. Section 9 (Refresh Trigger and
Versions) is the `utility` obligation.

**The section design, as the spec proposed and this research tested.**

1. **Purpose and Scope.** The customers covered, from the strategy's chosen segment, and the decisions the analysis
   informs. Gap candidate 5 lands here. The tie to the strategy's segment is the library's POSITION.
2. **The Competitor Set.** Direct rivals, indirect rivals and the status quo, each with a tier and a reason it is in.
   Out-of-scope rivals are named as out. Gap candidates 4 and 7 land here.
3. **Competitor Profiles.** One row per competitor. Aha!'s six columns are the nearest published set [8]. The
   bundle's own column set is the library's POSITION, because no vendor's download was read.
4. **Competitor Briefs** (full only). After SVPG: three things each main rival does that customers value, and three
   needs it leaves unmet [28], [29].
5. **Comparison on What Customers Value.** Criteria drawn from the chosen customers, weighted by their importance, as
   Aha!'s scorecard does [9]. A three-level rating, as Productboard's and Calven's are [11], [51].
6. **Jobs-Based Scorecard** (full only). After GitLab's scorecard, which is based on jobs to be done [19], and
   Strategyn's job-based comparison [35].
7. **Implications for Our Direction.** What changes in the strategy, the positioning or the roadmap, with an owner
   per implication. Gap candidate 6 lands here. The routing to each sibling is the library's POSITION.
8. **Evidence and Sources.** A source and a date for each claim, and a gap marked as unknown rather than guessed
   [51]. Gap candidates 1 and 2 land here.
9. **Refresh Trigger and Versions.** The owner, the events that call for a refresh, an interval floor the team
   chooses, and a dated row per version. The sources disagree on the interval, and the guide must say so [19], [54],
   [18], [26]. Gap candidate 8 lands here.

**The sharpest teaching points.**

- **A feature checklist is the trap.** A comparison on the features rivals chose, rather than on what the chosen
  customers value, is the failure Blank, Strategyn and THRV name [34], [35], [36].
- **The status quo belongs in the competitor set.** Dunford, Pragmatic Institute, Customer Impact and Calven all put
  it among the alternatives [43], [46], [52], [51]. Its place in this document is the library's POSITION.
- **Each refresh is a dated snapshot, and the document is the series.** That reconciles the living camp [37], [11]
  with Klue's snapshot [54]. It is the library's reading.
- **The analysis informs the strategy and does not set it** [45].

**The vendor-framing hazard.** Klue, Crayon, Octopus Intelligence, Calven, Aha!, Productboard, HubSpot, Dovetail,
Miro and Atlassian all sell software. Strategyn and THRV sell a method, and Customer Impact sells consulting. Every
cadence or structure claim from them must be labelled as that vendor's, and no vendor's cadence may be presented as
a consensus. Crayon's survey figures concern battlecards and sharing with sales, not a product team's analysis [23],
[24]. HubSpot's quarterly and six-monthly rhythm is for battlecards, relayed by Klue [22].

**The licence.** Aha!, Productboard and HubSpot state no reuse licence for their templates, and Productboard's
prompt reserves its rights. The bundle may describe what their structures contain and quote them briefly with
attribution. It copies no table, column order or wording, and every guidance comment is in the library's own words.

**The example.** The maintainer ruled on 2026-11-20 that the example is Acme Analytics' competitive analysis for the
Recurring Analyst segment, someone at a 50-500 person company with no data team (`product-strategy_example.md:43-48`).
Its first version is dated 2026-01-29, between the FY26 strategy (2026-01-28) and the positioning statement
(2026-01-30, `positioning-statement_example.md:7`), so the positioning statement was built on a current analysis. A
later dated version inside FY26 shows a refresh. Its competitor set matches the positioning statement's
alternatives: the spreadsheet, the shared analytics inbox and the colleague's favour, and general-purpose BI tools
(`positioning-statement_example.md:57-62`). It names no real vendor; any named rival is fictional and labelled
illustrative. It must not contradict the positioning statement's finding that no single alternative recurs often
enough in lost deals to name by brand (`positioning-statement_example.md:110`). Connector count appears as a
criterion on which rivals lead and customers do not stop, after the strategy's "Connector count is the metric our
competitors compete on; it is not where our users stop" (`product-strategy_example.md:102-103`). The strategy's
non-targets, enterprise data-platform teams and the embedded-analytics OEM channel, are named out of scope
(`product-strategy_example.md:50-57`). Its refresh triggers include the positioning statement's revisit event, a BI
vendor shipping a modeling layer "that a non-analyst can complete alone" (`positioning-statement_example.md:106-107`).
The later version records a rival's release that the analysis checked and that did not meet that bar. The strategy
says a competitor announcement is explicitly not a trigger for itself (`product-strategy_example.md:141`), so a
competitor's move refreshes the analysis instead.

**Risks the drafting agents should hold.**

- Quote Cagan only from the SVPG pages [28], [29], [30], [31] and the Dovetail interview [32], never from a page
  that quotes him. His books were not read.
- The encyclopedia article on competitor analysis [1] and the Admiralty code article [53] both carry banners asking
  for more sources. Cite them as leads.
- BABOK 10.4 [3] supports its title and number only. The NN/g video [42] supports only that a difference exists.
- THRV's attribution is weak [36]. Treat it as one voice with Strategyn.

Before review, grep the template for "Recurring Analyst", "spreadsheet", "favour" and any fictional rival's name, so
the example's scenario does not leak into the GOOD and WEAK text.

## Sources

### Origins: strategy writing, BABOK and the missing first document

**[1] Wikipedia contributors, 'Competitor analysis'.** reference. **fetched-and-verified.**
`https://en.wikipedia.org/wiki/Competitor_analysis`
Supports: Encyclopedia definition of competitive analysis as an assessment activity in marketing and strategic management, with technique steps (competitor array, competitor profiles). Its own text flags it as needing more citations (April 2013). It describes technique and profile contents, not a standalone written document for product teams. Cached copy fetched 2026-11-14
Quotable: "Competitive analysis in marketing and strategic management is the assessment of the strengths and weaknesses of current and potential competitors."
Quotable: "Competitive analysis is an essential component of corporate strategy."
Quotable: "the assessment of the strengths and weaknesses of current and potential competitors"

**[2] IIBA, 'Preface' of the BABOK Guide on the IIBA KnowledgeHub (table of contents of the Business Analysis Standard).** standards. **fetched-and-verified.**
`https://www.iiba.org/knowledgehub/the-business-analysis-standard/preface/`
Supports: The current BABOK Guide chapter 10 lists 50 techniques. 10.4 is 'Benchmarking and Market Analysis'. 10.46 is 'SWOT Analysis'. No technique is titled 'Competitive Analysis' (a case-insensitive search of the page text for 'competitive' found nothing). Only the table of contents was readable; section bodies are not on the page
Quotable: "10.4 Benchmarking and Market Analysis"
Quotable: "10.46 SWOT Analysis"

**[3] IIBA, '10.4 Benchmarking and Market Analysis', BABOK Guide on the IIBA KnowledgeHub.** standards. **fetched-and-verified.**
`https://www.iiba.org/knowledgehub/business-analysis-body-of-knowledge-babok-guide/10-techniques/10-4-benchmarking-and-market-analysis/`
Supports: Confirms the page for technique 10.4 exists and is titled 'Benchmarking and Market Analysis'. HTTP 200, but the fetched HTML contained only site navigation and the same table of contents, not the technique text (it appears gated to members). So I confirm the title and numbering only; I did not read the technique's definition or any mention of competitors
Quotable: "10.4 Benchmarking and Market Analysis"

**[4] Porter, Michael E., 'How Competitive Forces Shape Strategy', Harvard Business Review, March-April 1979 (public abstract page only, not the full article).** primary. **fetched-and-verified.**
`https://hbr.org/1979/03/how-competitive-forces-shape-strategy`
Supports: Existence and date of the founding five-forces article (March-April 1979 issue), author, and its opening premise. Only the summary and first paragraph are public; the remainder is behind HBR's subscription wall and was not read
Quotable: "The essence of strategy formulation is coping with competition."

**[5] Wikipedia contributors, "Porter's five forces analysis".** reference. **fetched-and-verified.**
`https://en.wikipedia.org/wiki/Porter%27s_five_forces_analysis`
Supports: Secondary report that five forces was first published in HBR in 1979, was developed in response to SWOT, and that Porter's 1980 book is Competitive Strategy. Its reference list cites the 1979 article as 'May 1979 (Vol. 57, No. 2), pp. 137-145'
Quotable: "This framework was first published in Harvard Business Review in 1979."
Quotable: "Porter developed his Five Forces Framework in response to the then-prevalent SWOT analysis"

**[6] Wikipedia contributors, 'SWOT analysis'.** reference. **fetched-and-verified.**
`https://en.wikipedia.org/wiki/SWOT_analysis`
Supports: SWOT history: a 1965 Stanford Research Institute Long Range Planning Service report (Stewart, Benepe, Mitchell) is credited by some authors; the Harvard origin claim is called an urban legend by Puyt et al.; the acronym appeared in print by 1972
Quotable: "academic urban legend"

**[7] Wikipedia contributors, 'Michael Porter'.** reference. **fetched-and-verified.**
`https://en.wikipedia.org/wiki/Michael_Porter`
Supports: Existence of Porter's 1979 HBR article and his 1980 book Competitive Strategy (Free Press), described there as having been voted the ninth most influential management book of the 20th century by Academy of Management Fellows
Quotable: "Competitive Strategy"

### Structure: what readable templates put in a competitive analysis

**[8] Aha! (Aha! Labs), 'Competitive analysis Template - Create a Competitive analysis' (Aha! Whiteboards template page).** vendor. **fetched-and-verified.**
`https://www.aha.io/roadmapping/guide/templates/create/competitive-analysis`
Supports: Aha!'s whiteboard template is a per-competitor table with six named columns plus a scorecard; the template body itself is behind a trial sign-up
Quotable: "mission statements, pricing, top features, strengths, weaknesses, and differentiators"
Quotable: "Customizable table for organizing insights by competitor"
Quotable: "Interactive scorecard for rating competitors' capabilities"
Quotable: "Conduct a high-level competitive analysis on a regular basis."
Quotable: "Perform a more detailed analysis to inform major strategic decisions."
Quotable: "is for product managers and product marketers"
Quotable: "missions, pricing, top features, strengths, weaknesses, and differentiators"
Quotable: "How do our products and services compare to the alternatives? And how can we better differentiate what we offer?"

**[9] Aha! (Aha! Labs), 'Competitive Analysis Templates: Options for Product Teams' (the '10 competitive analysis templates for product teams' guide).** vendor. **fetched-and-verified.**
`https://www.aha.io/roadmapping/guide/templates/competitor-analysis`
Supports: Aha! ships ten templates under the name, in six different forms (whiteboard table plus scorecard, workspace profile records, quadrant map, Excel profile/scorecard/overview/capability sheets, PowerPoint feature and imitability and differentiation slides); also lists eight research categories
Quotable: "10 competitive analysis templates for product teams"
Quotable: "Competitor profile"
Quotable: "Competitor scorecard"
Quotable: "Competitor overview"
Quotable: "Capabilities analysis"
Quotable: "Features analysis"
Quotable: "Imitability analysis"
Quotable: "Competitive differentiation analysis"
Quotable: "revenue, workforce, and product positioning"
Quotable: "Harvey Balls"
Quotable: "Review and update your competitive analysis regularly"
Quotable: "Assign a point person to keep the report updated throughout the year."
Quotable: "weighted by the importance of each attribute to your customers"

**[10] HubSpot, '10 Free Competitive Analysis Templates' / competitive analysis kit blog guide (page carries 'Updated: 01/09/26').** vendor. **fetched-and-verified.**
`https://blog.hubspot.com/marketing/competitive-analysis-kit`
Supports: HubSpot's kit names ten templates but the page does not show their fields; the downloads sit behind a form. The page body is weighted to content and marketing analysis, with a 'competitor content matrix' and SWOT
Quotable: "Two-Feature Competitive Landscape Chart"
Quotable: "Competitor Strategic Overview"
Quotable: "Content Marketing Analysis Template"
Quotable: "You vs. Competitor Side-By-Side"
Quotable: "Competitor Battle Card"
Quotable: "Multiple Competitor Feature Comparison"
Quotable: "Multiple Competitors Scoring Card"
Quotable: "SWOT Analysis Template"
Quotable: "Categorical Feature Comparison Template"
Quotable: "Review Tracker"
Quotable: "All fields are required."
Quotable: "A one-and-done exercise"
Quotable: "a critical component of any business strategy"

**[11] Productboard, 'Competitor Analysis: Framework, Template & Best Practices' (glossary page).** vendor. **fetched-and-verified.**
`https://www.productboard.com/glossary/competitor-analysis/`
Supports: Productboard's page, despite 'Template' in its title, gives no template. It gives eight 'Key Components', a 'competitive matrix' instruction, and five named frameworks (SWOT, Feature Comparison Matrix, Positioning Map, Jobs-to-be-Done, Porter's Five Forces)
Quotable: "Key Components of Competitor Analysis"
Quotable: "Create a competitive matrix or comparison framework"
Quotable: "fully supported"
Quotable: "partially supported"
Quotable: "not available"
Quotable: "Positioning Map"
Quotable: "isn't a one-time project"
Quotable: "Lightweight monitoring"
Quotable: "the ongoing practice of researching and evaluating competing products, companies, and market alternatives"

**[12] Productboard, 'Competitor Intelligence Brief' (Product Management Prompts library entry).** vendor. **fetched-and-verified.**
`https://www.productboard.com/product-management-prompts-library/competitor-intelligence-brief/`
Supports: A narrative one-competitor brief in six sections that ends in a battlecard summary, with an executive summary and a refresh note
Quotable: "COMPANY OVERVIEW"
Quotable: "PRODUCT ANALYSIS"
Quotable: "POSITIONING AND MESSAGING"
Quotable: "GO-TO-MARKET"
Quotable: "STRATEGIC ASSESSMENT"
Quotable: "SALES BATTLECARD SUMMARY"
Quotable: "A "last updated" note and recommended refresh cadence"

**[13] Atlassian, 'Competitive Analysis Template & Overview' (Confluence template page).** vendor. **fetched-and-verified.**
`https://www.atlassian.com/software/confluence/templates/competitive-analysis`
Supports: Section sequence of a one-page, you-versus-competitor document: profile table with tier weight, profile, competitive advantage, target market and market share, product offering, marketing by channel, SWOT. Read from the how-to steps; the template body is not shown
Quotable: "Competitive Advantage"
Quotable: "SWOT analysis"

**[14] Miro, 'Free Competitive Analysis Templates & Examples' (template collection page).** vendor. **fetched-and-verified.**
`https://miro.com/templates/competitive-analysis/`
Supports: Miro offers a collection of 10+ differently shaped templates under the name (matrix, table, SWOT, perceptual map, strategic group map, MOATs, Porter's); its five 'core elements' are editorial. Marketing-voiced; not a template body
Quotable: "Competitive Analysis Matrix"
Quotable: "Competitive Analysis Table"
Quotable: "Competitive Advantage [MOATs]"
Quotable: "SWOT Competitor Analysis"
Quotable: "Competitor Tiers"
Quotable: "Customer Friction Points"

**[15] Nikki Anderson (for Dscout), 'UXR Competitive Analysis Template', 5 December 2023.** practitioner. **fetched-and-verified.**
`https://dscout.com/people-nerds/competitive-analysis-template`
Supports: A UX-research reading of the name: a Google Sheet that ranks goals, needs and pain points, breaks them into usability tasks, adds a heuristic evaluation and a cost estimate. It has no competitor profile columns
Quotable: "0 to 5 scale"
Quotable: "Conduct a heuristic evaluation"

**[16] Product Marketing Alliance (author credited: James Shaw), 'Sales battlecard template', 14 May 2023.** practitioner. **fetched-and-verified.**
`https://productmarketingalliance.com/battlecard-template`
Supports: A battlecard section list: company and product overview, customer pain points, key features, key differentiators, why you win, sales tips, pricing overview, customers and testimonials. The download files are members-only
Quotable: "Key differentiators"
Quotable: "Why you win"
Quotable: "Sales tips"
Quotable: "Pricing overview"

**[17] Aha! (Ron Yang), 'The Best Templates for Product Managers to Complete Competitive Analysis', 22 Oct 2018.** vendor. **fetched-and-verified.**
`https://www.aha.io/blog/product-competitive-analysis-template`
Supports: Earlier Aha! position: a competitive analysis can be a quarterly deliverable to track competition over time, or a tightly focused look at one area; warns against recording every competitor move and against obsessing over competitors versus customers. Lists analysis types (capabilities, differentiation, landscape, overview, profile, scorecard, features, imitability ladder, value proposition). Publisher sells product-management software with competitor tracking built in; The 2018 list of approaches has nine entries and includes 'Value proposition analysis', which the 2026 guide does not; it describes the overview template as running from 'website, location, year founded' to 'mission, strengths, weaknesses'
Quotable: "quarterly deliverable"
Quotable: "Value proposition analysis"
Quotable: "Imitability ladder"
Quotable: "website, location, year founded"

**[18] Aha!, 'New product management template: Competitive analysis' (blog; page text shows Sept 2023 dates; exact post date not confirmed from the body).** vendor. **fetched-and-verified.**
`https://www.aha.io/blog/new-product-management-template-competitive-analysis`
Supports: Later Aha! position: revisit and refresh the competitive analysis biannually; share with sales, marketing and leadership; template has six columns (mission, pricing, top features, strengths, weaknesses, differentiators); focus on direct competitors first and branch to indirect. Publisher sells PM software; Repeats the six-column whiteboard set and says columns can be added
Quotable: "revisit and refresh your competitive analysis biannually"
Quotable: "six columns"
Quotable: "This does not mean monitoring competitors around the clock."
Quotable: "make time to revisit and refresh your competitive analysis biannually"
Quotable: "an ongoing exercise"

### Practice: ownership, evidence and how often it is refreshed

**[19] GitLab Handbook, 'Category Maturity - Competitor Comparison' (Product UX).** practitioner. **fetched-and-verified.**
`https://handbook.gitlab.com/handbook/product/ux/category-maturity/competitor-comparison/`
Supports: GitLab's own product-team practice: PM leads the quad with a PMM or Developer Advocate; refresh at least annually once a category is at Complete maturity, otherwise when a category shift is intended; early comparison recommended; findings must be evidence-driven; score is documented/updated on the handbook page; legal check on competitors' acceptable use policies. GitLab does not sell CI tooling (it uses Crayon internally)
Quotable: "at least annually"
Quotable: "A Product Manager will lead their quad team"
Quotable: "completely data/evidence driven"
Quotable: "Document/update the scoring"
Quotable: "should be completely data/evidence driven"
Quotable: "should be done at least annually"
Quotable: "should be done at least annually if you're at Complete"
Quotable: "Otherwise, when you intend to make a category shift"
Quotable: "As a Category Maturity Scorecard is based on Jobs to be Done"

**[20] GitLab Handbook, 'Competitor Evaluations' (Product UX; maintainer listed as Manav Khurana; last modified 2026-02-23).** practitioner. **fetched-and-verified.**
`https://handbook.gitlab.com/handbook/product/ux/competitor-evaluations/`
Supports: GitLab separates a competitor evaluation (compares solutions against Jobs to Be Done) from a competitor analysis (compares business models and strategic positioning, SWOT-like). Distinguishes direct and indirect competitors. Gives no refresh cadence. Relevant to scoping what this bundle's document is
Quotable: "It evaluates solutions."
Quotable: "A competitor analysis evaluates companies."

**[21] GitLab Handbook, 'Competitive Intelligence' (Product and Solution Marketing; last modified 2026-10-30 per page footer).** practitioner. **fetched-and-verified.**
`https://handbook.gitlab.com/handbook/marketing/brand-and-product-marketing/product-and-solution-marketing/competitive-intelligence/`
Supports: GitLab's marketing-side practice is continuous and open: all Sales, Product, Engineering and Marketing staff get collaborator access in Crayon and are encouraged to update, correct and comment; content is re-published after review via a merge-request-like comment to the CI owner; a Crayon analyst sources intel; Clozd win/loss feeds in. The page gives no fixed refresh interval. Accuracy inputs are websites, documentation, demo videos, customers and competitors; an example is given of a competitor's PM sending a correction. Customer-voice sources are G2 and TrustRadius
Quotable: "anyone can contribute to the Competitive Intelligence process"
Quotable: "update, correct, amend and comment"
Quotable: "Fair"
Quotable: "Accurate"
Quotable: "Easily consumable"
Quotable: "all our product comparison pages are un-gated"
Quotable: "timely and insightful analysis of competitors"

**[22] Klue (Adam McQueen), 'Updating Your Battlecards | Compete Confidential (CE LIVE) | Shoulda Done It', Coffee & Compete newsletter, 17 Sep 2023.** vendor. **fetched-and-verified.**
`https://klue.com/newsletter/updating-your-battlecards-compete-confidential-ce-live-shoulda-done-it`
Supports: Klue relays a customer's cadence rather than stating its own: HubSpot's Jessica Davis tiers competitors in groups of five by deal frequency and market focus, updates tier one and two battlecards quarterly and the rest every six months, and also updates comparison pages so language stays consistent. Competitive-intelligence leads from Autodesk and JFrog describe field intel intake: ask and reward contributors, set a communication cadence, run an ambassador program and periodic listening tours. Publisher sells CI software (Klue Compete, Win-Loss)
Quotable: "Tier one and two competitors, we update our battlecards every quarter."
Quotable: "The rest we update every six months."
Quotable: "competitive ambassador program"

**[23] Crayon, 'State of Competitive Intelligence 2025' (8th edition benchmark report, PDF, text-extracted with pypdf).** vendor. **fetched-and-verified.**
`https://www.crayon.co/hubfs/Crayon%27s%202025%20State%20of%20CI%20Report.pdf`
Supports: Survey data from a CI-tooling vendor: 47% of respondents say marketing owns the compete function; respondents without a designated owner described CI as a piecemeal operation. Cadence of sharing CI updates with sales: daily 5%, weekly 27%, monthly 31%, quarterly 10%, ad hoc 27%. Sales sends intel back to CI weekly 22%, monthly 25%, ad hoc 37%. Teams sharing daily or weekly are 75% more likely to report revenue impact. These are self-reported survey correlations from a vendor with an interest in more frequent intel, not controlled evidence. Note: the cache entry for this URL was first stored as binary junk by my fetch helper and I replaced it with the extracted text
Quotable: "47% of respondents"
Quotable: "marketing owns the compete function"
Quotable: "nobody really owns CI"
Quotable: "75% more likely"

**[24] Crayon (Shannon De Marco), 'Outdated Battlecards are a Thing of the Past: Automate Your Compete Program With Sparks Content', 25 Feb 2025.** vendor. **fetched-and-verified.**
`https://www.crayon.co/blog/sparks-content`
Supports: Crayon cites that only 26% of CI teams update battlecards monthly and 41% take an ad-hoc approach, and uses this to sell automated refresh (Sparks). Publisher sells CI tooling; the 26% figure is quoted without a methodology on the page (it matches the vendor's own benchmark series)
Quotable: "only 26% of CI teams update battlecards monthly"
Quotable: "41% rely on an ad-hoc approach"

**[25] Aha!, 'How product managers should research competitors' (roadmapping guide).** vendor. **fetched-and-verified.**
`https://www.aha.io/roadmapping/guide/product-strategy/how-should-product-managers-research-competitors`
Supports: Source types for competitor facts: company websites, third-party review sites, industry news, press releases, customer reviews. Gives no refresh interval (a grep for update, refresh, cadence terms found none)

**[26] Dovetail Editorial Team (reviewed by Mary Mikhail), 'Analyzing your competitor's products with a competitive product analysis', last updated 21 Mar 2024.** vendor. **fetched-and-verified.**
`https://dovetail.com/product-development/how-to-do-a-product-competitive-analysis`
Supports: Frequency depends on product, business and industry; offers three options: once a year, once a quarter, or based on specific events (a new product coming to market, a shift in a competitor's marketing tactics, a change in customer habits); warns that the work is time-consuming and should be balanced against internal resources. Publisher sells research-repository software, not CI tooling per se
Quotable: "Based on specific events."
Quotable: "Once a year."
Quotable: "Once a quarter."
Quotable: "competitor product analysis is an ongoing process"
Quotable: "A comprehensive annual review of your competition can help you develop a strategic roadmap for the coming year."
Quotable: "Revisit your findings periodically"

**[27] Dovetail (reviewed by Cathy Heath), 'Conducting an effective competitor audit', last updated 3 Apr 2024.** vendor. **fetched-and-verified.**
`https://dovetail.com/market-research/competitor-audit`
Supports: Audit timing monthly, quarterly or annual; annual shows broad trends, monthly or quarterly suit fast-changing businesses; lists 'stopping after one competitor audit and failing to update or spot-check data' and 'only sharing with a few people' as mistakes
Quotable: "monthly, quarterly, or annual audits"
Quotable: "failing to update or spot-check data"

### Debates: living or snapshot, features or value, and whether to study rivals

**[28] Marty Cagan, 'Competition', Silicon Valley Product Group, 2 Aug 2011.** practitioner. **fetched-and-verified.**
`https://www.svpg.com/competition/`
Supports: Cagan opposes cat-and-mouse competitor chasing yet endorses a bounded competitor study: three strengths, three unmet-need areas per competitor, holistic view
Quotable: "they leave us because we fail to meet their ongoing needs"
Quotable: "identify the three key things"
Quotable: "take the holistic view when evaluating competitors"
Quotable: "So stop chasing your competitors and start focusing on providing real value for your customers"
Quotable: "the three key things that they think the competitor does that provides real value for their customers, and the three major areas where they think the customer's needs are not met"
Quotable: "The key is to constantly drive value for your customers."

**[29] Marty Cagan, 'Coaching Tools - The Plan', Silicon Valley Product Group, 22 Apr 2019.** practitioner. **fetched-and-verified.**
`https://www.svpg.com/coaching-tools-the-plan/`
Supports: Cagan treats competitive analysis as required PM industry knowledge, coached as a one-time narrative write-up of 3-5 players, not as a maintained artifact
Quotable: "evaluate the top 3-5 players in the space"
Quotable: "write up a narrative comparing and contrasting the strengths and weaknesses of each player"
Quotable: "evaluate the top 3-5 players in the space, and to write up a narrative comparing and contrasting"

**[30] Marty Cagan, 'Product Strategy - Overview', Silicon Valley Product Group.** practitioner. **fetched-and-verified.**
`https://www.svpg.com/product-strategy-overview/`
Supports: Strategy is never static, but the page does not say competitive documents must be maintained; lists the competitive landscape among insight sources
Quotable: "product strategy is never static"
Quotable: "the competitive landscape"

**[31] Marty Cagan, 'Product Strategy - Insights', Silicon Valley Product Group.** practitioner. **fetched-and-verified.**
`https://www.svpg.com/product-strategy-insights/`
Supports: Cagan frames the competitive landscape as one slice of industry insight, narrower than the industry at large
Quotable: "your competitive landscape"

**[32] Dovetail, 'Getting in front of the customer with Marty Cagan' (interview).** practitioner. **fetched-and-verified.**
`https://dovetail.com/outlier/getting-in-front-of-the-customer-with-marty-cagan/`
Supports: Cagan, in an interview, advises caring for customers and worrying less about competitors even when options are many
Quotable: "not worry so much about competitors"

**[33] Harshal Patil, 'When Customer-First Fails, Use A Competitor Research Power-Up', Substack, 2 Jul 2025.** practitioner. **fetched-and-verified.**
`https://harshalpatil.substack.com/p/use-competitive-research-not-just-customer-insights`
Supports: A named PM who pushes back on the customers-not-competitors reading of Cagan and Amazon, from personal missteps
Quotable: "prioritize your customers more than your competitors"
Quotable: "I thought I was being customer-centric by ignoring competitors"

**[34] Steve Blank, 'Death By Competitive Analysis', steveblank.com, 1 Mar 2010.** practitioner. **fetched-and-verified.**
`https://steveblank.com/2010/03/01/death-by-analysis/`
Supports: Named practitioner arguing feature-comparison tables rationalize founder assumptions and drive feature sprawl; customer discovery should decide which features matter
Quotable: "a competitive analysis drives a maximum feature set"
Quotable: "No feature lists without facts"

**[35] Strategyn (Tony Ulwick's firm), 'Competitive Analysis'.** vendor. **fetched-and-verified.**
`https://strategyn.com/competitive-analysis/`
Supports: Jobs-to-be-done camp: compare how well each product helps customers get the job done against customer-defined needs, not specs
Quotable: "feature-to-feature comparisons is no guarantee of success"
Quotable: "assessing how much better or worse a product is at helping the customer get a job done"

**[36] THRV, 'Stop the downward spiral of feature-to-feature comparison' (thrv-cms.vercel.app mirror; author not shown).** vendor. **fetched-and-verified.**
`https://thrv-cms.vercel.app/blog/stop-the-downward-spiral-of-feature-to-feature-comparison`
Supports: JTBD consultancy argues feature catch-up is unwinnable and uses the Zune/iPod example
Quotable: "Feature catch-up with your competitors is a race"

**[37] Octopus Intelligence, 'CRO Competitive Intelligence Example: Your Battle Cards Are Out of Date Before the Ink Is Dry'.** vendor. **fetched-and-verified.**
`https://www.octopusintelligence.com/cro-competitive-intelligence-example-your-battle-cards-are-out-of-date-before-the-ink-is-dry/`
Supports: Living-process camp: a battle card is a snapshot that decays and loses rep trust; intelligence should be a continuous programme
Quotable: "built as a project rather than maintained as a programme"
Quotable: "A battle card is a document. Competitive intelligence is a process."
Quotable: "the difference between a photograph and a live feed"

**[38] Product School, 'Product Manager Competitive Analysis'.** vendor. **fetched-and-verified.**
`https://productschool.com/blog/skills/product-manager-competitive-analysis`
Supports: Calls competitive analysis living and continuous, yet recommends feature matrices, SWOT and positioning maps and says framework choice depends on the goal
Quotable: "It should be a living part of product culture"
Quotable: "Which framework you choose depends on your goal"

### Relationships: positioning, battlecards, win-loss and competitive testing

**[39] Nielsen Norman Group (NN/g), Competitive Usability Evaluations: Definition.** practitioner. **fetched-and-verified.**
`https://www.nngroup.com/articles/competitive-usability-evaluations/`
Supports: Splits competitive usability evaluation into two methods, competitive reviews (expert) and competitive testing (users); states the goal is to improve your design, not declare a winner; 2-4 competitor sites
Quotable: "Comparing your product against several competing designs."
Quotable: "a usability expert takes an in-depth look at a series of related products"
Quotable: "users complete a set of tasks using two or more competing designs"
Quotable: "the main goal of a competitive evaluation is not to declare a winner"
Quotable: "Comparing your product against several competing designs"
Quotable: "What are the biggest strengths of competing designs?"
Quotable: "a good initial research activity"

**[40] Nielsen Norman Group (NN/g), Parallel & Iterative Design + Competitive Testing = High Usability.** practitioner. **fetched-and-verified.**
`https://www.nngroup.com/articles/parallel-and-iterative-design/`
Supports: Source of the sentence separating competitive testing from a competitive review; competitive testing needs real users; test your design plus 3-4 competitors
Quotable: "Competitive testing is not the same as a competitive review."
Quotable: "competitive testing requires that designs be tested with actual users"

**[41] Nielsen Norman Group (NN/g), Competitive Usability Testing to Discover Better Designs.** practitioner. **fetched-and-verified.**
`https://www.nngroup.com/articles/redesign-competitive-testing/`
Supports: Competitive usability testing uses a thinking-aloud method with participants on your site plus 1-2 competitors; compared sites need not be direct competitors; purpose is insight into why design elements work, not to crown a winner
Quotable: "The sites you select do not need to be direct competitors."
Quotable: "not to crown a winner"

**[42] Nielsen Norman Group (NN/g), Competitive Reviews vs. Competitive Research (video, Therese Fessenden, 2024-07-03).** practitioner. **fetched-and-verified.**
`https://www.nngroup.com/videos/competitive-reviews-vs-competitive-research/`
Supports: Existence of an NN/g video distinguishing a competitive review from competitive research. The page carries only a summary line, no transcript, so no boundary claim beyond that a difference exists
Quotable: "There is more than one way to conduct a competitive evaluation."

**[43] April Dunford, Positioning and Competition (Positioning with April Dunford, Substack, 2020-12-28).** practitioner. **fetched-and-verified.**
`https://aprildunford.substack.com/p/positioning-and-competition`
Supports: Dunford's boundary: positioning works from competitive alternatives (including the status quo), not every competitor; phantom competitors are watched by the product team but excluded from positioning
Quotable: "What would a customer do if your offering didn't exist?"
Quotable: "Not Every Competitor is an Alternative"
Quotable: "phantom competitors"
Quotable: "the first competitive alternative we need to beat is the status quo"

**[44] Pragmatic Institute, Choosing a Market Analysis Framework (SWOT and Six Forces).** practitioner. **fetched-and-verified.**
`https://www.pragmaticinstitute.com/resources/articles/product/doing-market-analysis-easy-right/`
Supports: Six Forces model is a market-analysis framework; separates market research (gathering) from market analysis (the deliverable); says market analysis should inform positioning and the roadmap; SWOT assumes objectives already set; the page says the Six Forces model, like SWOT, represents a moment frozen in time
Quotable: "Like SWOT analyses, this model represents a moment frozen in time"
Quotable: "Market analysis differs from market research"
Quotable: "SWOT will not help you set the product objectives because it assumes you have already set them."
Quotable: "holistic view of the competitive landscape"
Quotable: "a moment frozen in time"
Quotable: "represents a moment frozen in time"
Quotable: "the final deliverable from analyzing the research and drawing conclusions"

**[45] Pragmatic Institute, A Product Manager's Guide to Market Trend Analysis.** practitioner. **fetched-and-verified.**
`https://www.pragmaticinstitute.com/resources/articles/product/a-product-managers-guide-to-market-trend-analysis/`
Supports: Draws a boundary between competitive analysis (today's landscape) and market trend analysis (broader change), and says competitors should not define product strategy
Quotable: "they answer different questions"
Quotable: "Competitors can provide useful market intelligence, but they shouldn’t define your product strategy."

**[46] Pragmatic Institute, Product Management Framework (2027 edition) - includes Product Strategy, Win/Loss Analysis, Competitive Landscape, Market Definition, Positioning.** practitioner. **fetched-and-verified.**
`https://www.pragmaticinstitute.com/product/framework/`
Supports: Pragmatic lists competitive landscape, win/loss analysis, product strategy, market definition (which includes segment size) and positioning as separate framework elements, each with its own definition. Source for the competitive-landscape definition
Quotable: "What else could buyers use instead, including doing nothing?"
Quotable: "the option to do nothing"
Quotable: "Why did recent evaluators buy from us, or not?"
Quotable: "Which segment is most likely to buy, and is it big enough?"

**[47] Pragmatic Institute, The Ultimate Guide to Win/Loss Analysis.** practitioner. **fetched-and-verified.**
`https://www.pragmaticinstitute.com/product/framework/win-loss-analysis/`
Supports: Win/loss is interview-based evidence from recent evaluators about buying decisions; interviewer outside sales, 2-4 weeks after decision; sits in the Market category beside Competitive Landscape
Quotable: "why recent evaluators did or didn’t buy from you"
Quotable: "Have someone outside sales run the interviews"

**[48] Pragmatic Institute, Product Positioning Strategies for Competitive Markets.** practitioner. **fetched-and-verified.**
`https://www.pragmaticinstitute.com/resources/articles/product/product-positioning-strategies-for-competitive-markets/`
Supports: Positioning is an internal decision discipline whose third pillar is differentiation against real alternatives; buyers compare against the option of doing nothing
Quotable: "meaningful differentiation relative to real alternatives"
Quotable: "including the option of doing nothing"

**[49] Pragmatic Institute, Competitive Strategy from Strength to Weakness (Ask the Experts).** practitioner. **fetched-and-verified.**
`https://www.pragmaticinstitute.com/resources/articles/product/ask-the-experts-how-do-you-find-the-weakness-in-a-competitors-strength/`
Supports: Competitive strategy is how businesses evaluate competitors and gain advantage; product managers are often responsible for competitive analysis; recommends arming sales with talking points that acknowledge and counter competitor strengths (link to battlecards)
Quotable: "arm your sales team with talking points acknowledging a competitor’s strengths and then counter them"

**[50] Pragmatic Institute, Advanced Strategy For Building Effective Sales Battle Cards [+5 Examples] (PDF).** practitioner. **fetched-and-verified.**
`https://www.pragmaticinstitute.com/advanced_strategy_for_building_effective_sales_battlecards_21-09/`
Supports: Battle card is a one-page internal sales tool: five-card deck (competitor overview, win/loss, objection handling, product, pricing) per competitor, built for sales conversations; the example competitor is fictitious. The URL serves a PDF, read with pdftotext
Quotable: "Battle cards are internal documents"
Quotable: "simple one-page battle cards"

### The gap question: what strong analyses do that templates do not ask for

**[51] David Kolinek (Calven), Competitor Analysis Template: How to Fill In Every Field (dated 13 Nov 2026).** vendor. **fetched-and-verified.**
`https://calven.ai/resources/competitive-intelligence/competitor-analysis`
Supports: Candidates: per-claim source plus last-updated date; mark pricing gaps rather than guess; name the decision the analysis serves; status quo as a competitive alternative; every row ends in a so-what action; ratings of 'fully / partially / not supported' rather than yes/no; tier competitors so effort follows tier; staleness. Vendor of an AI product marketing platform, so a selling interest in 'keep it current' is present
Quotable: "Every field needs a source you can name, and a blank field beats a guessed one."
Quotable: "A cell with an invented number in it is worse than an empty one, because it looks like knowledge."
Quotable: "Where each claim came from, and when. Makes the doc auditable."
Quotable: "Define the decision it serves."
Quotable: "Start from competitive alternatives, meaning what the buyer would use if you didn't exist."
Quotable: "That tiered set of alternatives, status quo included, is your competitive landscape."
Quotable: "A profile built once is usually wrong within a quarter."

**[52] Tanguy De Keyzer (Customer Impact), B2B Competitive Analysis: Step-by-Step (updated 20 Oct 2026).** vendor. **fetched-and-verified.**
`https://www.customerimpact.be/en/blog/how-to-do-b2b-competitive-analysis/`
Supports: Candidates: status quo ('do nothing' or a homegrown spreadsheet) as a named competitor; AI-assistant shortlist as a competitor set; each finding ends in one action with an owner and a date, capped at three to five per quarter; dated observation of an AI answer with its cited sources. Consultancy blog, so a selling interest in the service is present
Quotable: "The status quo is your largest competitor. Most teams forget it."
Quotable: "Let every finding end in one concrete move with an owner and a date"

**[53] Wikipedia contributors, Admiralty code.** reference. **fetched-and-verified.**
`https://en.wikipedia.org/wiki/Admiralty_code`
Supports: Candidate: a two-part rating on each item of evidence, source reliability (A-F) separate from information credibility (1-6, by corroboration). This is an intelligence-community convention (NATO, Five Eyes), not a competitive-analysis one. The article itself carries a 'relies on a single source' banner, so I treat it as a pointer to the convention, not as the standard's text
Quotable: "Each descriptor is considered in isolation to ensure that the reliability of the source does not influence the assessed accuracy of the report."
Quotable: "Confirmed by other independent sources"

### Carried from admission sweep 8

**[54] Klue - How to Do a Competitive Landscape Analysis.** vendor. **fetched-and-verified.**
`https://klue.com/blog/competitive-landscape-analysis-guide`
Supports: A vendor that sells competitive-intelligence software names quarterly as its default refresh interval, calls a landscape analysis a snapshot that needs refreshes, warns against relying on CRM data alone, and says feature comparison tables can serve as sales battlecards. Read and raw-checked in admission sweep 8 (2026-11-14)
Quotable: "Quarterly is a solid default."
Quotable: "temporary snapshots that need refreshes as the market changes"
Quotable: "Don't just rely on CRM data"
Quotable: "Competitive landscape analysis is a snapshot"
Quotable: "Feature comparison tables double as top-notch sales battlecards"

**[55] Klue - How to Conduct a Competitive Analysis on Top Rivals.** vendor. **fetched-and-verified.**
`https://klue.com/topics/do-a-competitive-analysis`
Supports: The same vendor describes competitive analysis for sales enablement as continuous and driven by live deal feedback. Read and raw-checked in admission sweep 8 (2026-11-14)
Quotable: "Continuous, driven by live deal feedback"
Quotable: "Skip the website fluff"

**[56] Nielsen Norman Group - 7 Steps to Benchmark Your Product's UX.** practitioner. **fetched-and-verified.**
`https://www.nngroup.com/articles/product-ux-benchmarks/`
Supports: NN/g uses benchmarking for a recurring UX measurement program, which is why this bundle avoids the alias benchmarking report. Read and raw-checked in admission sweep 8 (2026-11-14)
Quotable: "Benchmarking is often a program rather than a one-time activity"

## Pages not read under the terms rule

Since 2026-11-14 this section holds pages behind a login, a paywall or a bot block, not pages barred by a site's
terms. The research agents found the pages below and could not read them. The maintainer has not read any of them
by hand. No claim or quotation in this bundle rests on any of them, and the maintainer may read them by hand.

- `https://hbr.org/1979/03/how-competitive-forces-shape-strategy`: the full article is behind HBR's subscription
  wall. Only its public summary and opening line were read, which is all that entry [4] rests on.
- `https://www.iiba.org/knowledgehub/business-analysis-body-of-knowledge-babok-guide/10-techniques/10-4-benchmarking-and-market-analysis/`:
  the technique's text appears to sit behind an IIBA member login. The public page returned only its title and the
  table of contents, which is all that entry [3] rests on.
- `https://www.aha.io/roadmapping/guide/templates/create/competitive-analysis`: the whiteboard template's body needs
  an Aha! trial sign-up. Its page text was read as entry [8]; the template's own columns were not.
- `https://blog.hubspot.com/marketing/competitive-analysis-kit`: the ten template files are behind a download form.
  The guide page was read as entry [10]; the templates were not.
- `https://productmarketingalliance.com/battlecard-template`: the battlecard files are for members only. The page's
  own section list was read as entry [16].
- `https://dscout.com/people-nerds/competitive-analysis-template`: the spreadsheet sits behind a download step. The
  page's summary of it was read as entry [15].
- `https://www.forbes.com/sites/mikesmerklo/2019/05/24/the-greatest-competitor-youve-never-met/`: it returned HTTP
  403 to an automated fetch. It would have argued for counting the status quo as a competitor.
- `https://www.dni.gov/files/documents/ICD/ICD-203.pdf`: it returned HTTP 403 to an automated fetch. It is the US
  intelligence community's standard for stating confidence and source quality, wanted for the gap question's
  confidence-rating candidate.
- `https://fabric.so/blog/competitive-intelligence-that-stays-current`: not a block. A plain fetch returned only a
  JavaScript shell with no article text.
