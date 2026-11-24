---
title: "{{product_name}} Competitive Analysis"
product: "{{product_name}}"
owner: "{{who_owns_this_analysis}}"
customer_segment: "{{customer_segment_short_name}}"
current_version: "{{current_version}}"
status: "{{draft_or_agreed}}"
last_updated: "{{date}}"
doc_type: competitive-analysis
size: full
source_template: competitive-analysis
source_template_version: 0.1.1
---

<!--
FULL COMPETITIVE ANALYSIS. Every section of competitive-analysis_template-lean.md, in the same
order, plus two: Competitor Briefs, a short narrative on each main rival, after Competitor
Profiles, and Jobs-Based Scorecard, which rates each rival on how well it helps the chosen
customers get a job done, after Comparison on What Customers Value.

USE FULL WHEN a major choice rests on how a few main rivals differ, or when the lean comparison
keeps ending in an argument about which criteria the customers truly care about. That signal is
this library's reading, not a measured one: no source read measures when the second weight pays
for itself. Aha! asks for both weights of work: "Conduct a high-level competitive analysis on a
regular basis." and "Perform a more detailed analysis to inform major strategic decisions." Use
lean (competitive-analysis_template-lean.md) as the default.

WHAT THIS DOCUMENT IS, AND IS NOT. A competitive analysis says who else serves the customers your
strategy chose, compares them on what those customers value, and says what that means for the
product's direction. It is a dated snapshot: each refresh adds a version, and the document is the
series. That reconciliation is this library's reading (Klue: "Competitive landscape analysis is a
snapshot"). The name covers several documents; Aha!'s guide offers "10 competitive analysis
templates for product teams". This template holds profiles of companies and a comparison of what
their products do for the chosen customers, which is this library's scope.

It is NOT a product strategy, which it informs and does not set. It is NOT a positioning statement,
which takes one named alternative where this maps many. It is NOT a sales battlecard, which this
library treats as downstream. It is NOT a SWOT of your own company, which assesses us. It is NOT a
competitive usability study: NN/g writes "Competitive testing is not the same as a competitive
review." It is NOT market sizing or a win/loss analysis, though a win/loss finding can correct the
set. Each boundary, and which are this library's own, is in competitive-analysis_companion.md
sections 1 and 8.

THE TRAP THIS TEMPLATE IS BUILT AROUND. A feature checklist compares rivals on the features they
chose, not on what your chosen customers value. Steve Blank, Strategyn and THRV argue against it;
Product School presents the feature matrix as one framework among several, and nobody measured the
harm. This template takes the customer-value side in Comparison on What Customers Value. See
competitive-analysis_companion.md section 6.

WHERE THIS SITS IN THE CHAIN. After the product strategy and immediately before the positioning
statement in the strategy-docs family. That place is this library's POSITION; no source states the
sequence. Nothing here depends on it, only on the analysis taking its customers from a strategy that
has already chosen them. See competitive-analysis_companion.md section 8.

WHAT THE RESEARCH RESTS ON. Twenty-three of the 56 sources are vendor writing, and nearly every
refresh interval and template structure the research found comes from a vendor. No published,
filled-in competitive analysis was read, and no refresh interval has been measured, so the section
set is largely this library's POSITION. Aha!, Productboard and HubSpot state no reuse licence, so
every column and section name here is this library's own. Names in GOOD and WEAK are invented.

HOW TO FILL THIS IN
1. Read the comment under each heading: WHAT it wants, WHY it matters (with a pointer into
   competitive-analysis_companion.md), guiding questions to ASK, a GOOD and a WEAK example, and the
   TRAP to avoid. For the tables, PRIORITY explains the ordering rule and ROW HINT says what a good
   row contains.
2. Replace each {{placeholder}} with your content. Where you do not know a fact, write "unknown"
   in that cell and say why. A blank beats a guess.
3. If a section does not apply, write "N/A" and one line of why, rather than deleting it.
4. This is a standing document: each refresh adds a dated row to Refresh Trigger and Versions and
   keeps the earlier version. Before you first share it: self-grade against
   competitive-analysis_guide.md, then DELETE every HTML comment. They are guidance, not content.
   Keep the source_template and source_template_version fields in the frontmatter.
-->

# {{product_name}} Competitive Analysis

## Purpose and Scope

<!-- WHAT  The customers this analysis covers, taken from the segment your product strategy chose,
           and the decisions it is meant to inform.
     WHY   Aha! frames the job as two questions: "How do our products and services compare to the
           alternatives? And how can we better differentiate what we offer?" Calven, a vendor of
           an AI product-marketing platform, gives the instruction for scope: "Define the decision
           it serves." Tying the scope to the segment your strategy chose is this library's own
           POSITION. Its reasoning is that a competitor set only means something for a stated
           customer. Deep dive: competitive-analysis_companion.md section 3 (Purpose and Scope).
     ASK   Which customers, by the segment your strategy chose, is this comparing rivals for? What
           decision will the analysis inform, and who makes it? If the analysis showed a rival
           ahead, what would you do differently? Who reads it, product, product marketing or both?
     GOOD  "Covers independent physiotherapy practices of 3 to 15 clinicians with no dedicated
           office manager, the segment our strategy chose. It informs one decision, owned by the
           head of product: whether the next two quarters go to patient reminders or to group
           booking."
           (names the customers and the decision, so a reader can tell what to leave out)
     WEAK  "This analysis looks at the appointment-booking market."
           (no customer and no decision, so nothing can be ruled out and nothing can be used)
     TRAP  Scoping to a market rather than to the customers your strategy chose. With no stated
           customer, nothing tells you which rivals belong in the set or which facts about them
           matter. -->

- The customers this covers, and the strategy segment they come from: {{customers_covered}}
- The decisions this analysis informs, and who makes them: {{decisions_informed}}
- Who reads it, and what they will do with it: {{readers_and_use}}

## The Competitor Set

<!-- WHAT  Who is in the comparison and why: direct rivals, indirect rivals, and the status quo,
           which is what your chosen customers do today if they buy nothing. Each has a tier and a
           reason it is in. Rivals you looked at and left out are named as out, each with a reason.
           This section decides what the whole analysis is about.
     WHY   Dunford works from alternatives, not from every competitor. She asks "What would a
           customer do if your offering didn't exist?", says "Not Every Competitor is an
           Alternative", and calls rivals that prospects never consider "phantom competitors",
           left out of positioning but watched by the product team. The status quo is named by
           at least four sources, among them Dunford ("the first competitive alternative we need to beat is the status
           quo"), Pragmatic Institute's competitive landscape ("What else could buyers use
           instead, including doing nothing?"), Customer Impact ("The status quo is your largest
           competitor. Most teams forget it.") and Calven ("Start from competitive alternatives,
           meaning what the buyer would use if you didn't exist."). Customer Impact and Calven both
           sell services or software in this area. Placing the status quo in this set is this
           library's POSITION, taken from the positioning statement's named alternative. Tiering
           is guidance from several publishers, and no source read measures it. Deep dive:
           competitive-analysis_companion.md section 3 (The Competitor Set).
     ASK   Who would the chosen customers compare you with, and what do they do if they buy
           nothing? Which rivals are real alternatives for them, and which are phantom? What would
           make a rival tier 1 here, and who decided? Which rivals did you look at and leave out,
           and what is the one-line reason for each?
     PRIORITY  Order rows by tier, heaviest first, and put the status quo where its tier puts it,
           not last by habit. The tiering rule is yours. HubSpot's practice, relayed by Klue,
           tiers competitors for its battlecards in groups of five by deal frequency and market
           focus, and Atlassian's template carries a tier weight in its profile table. Cagan's
           coaching exercise asks for "the top 3-5 players in the space"; this template does not
           cap the rows.
     ROW HINT  A good row names the competitor or the alternative, its kind (direct, indirect or
           status quo), its tier, and the reason the chosen customers would weigh it. A weak row is
           a name with no reason.
     GOOD  | Northgate Booking | Direct | Tier 1 | The product clinic owners named when we asked
           what they compared us with before buying |
           | Paper appointment book at the front desk | Status quo | Tier 1 | What a clinic does
           if it buys nothing: no licence fee, and the owner already trusts it |
     WEAK  | Northgate Booking | Competitor | | |
           (no tier, no reason, and a set with no row for what customers do today)
     TRAP  Leaving out the status quo, or filling the set from a list of every product in the
           category. The set follows whom your chosen customers consider, and a set built from the
           category's whole shelf compares you with rivals nobody is choosing between. -->

| Competitor or alternative | Kind | Tier | Why it is in the set |
|---|---|---|---|
| {{competitor_name}} | {{competitor_kind}} | {{competitor_tier}} | {{reason_in_set}} |

- Rivals looked at and left out of the set, each with the reason: {{rivals_left_out}}

## Competitor Profiles

<!-- WHAT  One row per competitor or alternative in the set: who it serves, what it offers, how it
           charges, where it wins, where it falls short, and how it differentiates itself.
     WHY   The nearest published column set is Aha!'s, which records competitors' "mission
           statements, pricing, top features, strengths, weaknesses, and differentiators". No two
           vendors share a field set, and no vendor's downloadable template was opened,
           because the downloads sit behind sign-ups and forms. The column set here is
           this library's own POSITION. GitLab names websites, documentation, demo videos,
           customers and competitors as inputs to accuracy, so a row can rest on more than one kind
           of input. Deep dive: competitive-analysis_companion.md section 3 (Competitor Profiles).
     ASK   What does each row rest on, and where is that recorded in Evidence and Sources? Where
           do you not know, and have you written "unknown" there? What does the status quo row say
           the customer does today, in the customer's terms?
     PRIORITY  The same order as the competitor set, so the two tables read side by side.
     ROW HINT  A good row has a sourced fact or a marked "unknown" in every cell. For the status
           quo, write what the customer does and what it costs them in time or money. A weak row
           is made of adjectives, or has a number nobody can trace.
     GOOD  | Northgate Booking | Clinics of 5 to 20 clinicians | Online booking, text reminders,
           group booking | Per clinician each month, from its public price page | Reminders and
           group booking | No billing; exports are manual | Positions itself on fewer missed
           appointments |
     WEAK  | Northgate Booking | Everyone | Booking | Cheap | Good product | Bad support | Better |
           (adjectives and a guessed price, with nothing a reader could trace)
     TRAP  Filling a cell with a number you did not read. Calven writes "A cell with an invented
           number in it is worse than an empty one, because it looks like knowledge." It is a
           vendor's line, and it is a good rule for any row here. -->

| Competitor | Customers it serves | What it offers | How it charges | Where it wins | Where it falls short | How it differentiates |
|---|---|---|---|---|---|---|
| {{profile_competitor}} | {{profile_customers_served}} | {{profile_offer}} | {{profile_pricing}} | {{profile_wins}} | {{profile_shortfalls}} | {{profile_differentiation}} |

## Competitor Briefs

<!-- WHAT  A short narrative on each main rival, meaning the tier 1 rows in the set: the things it
           does that your chosen customers value, and the needs it leaves unmet. Copy the block
           below once per rival. Full variant only.
     WHY   Cagan asks a product leader to find "the three key things that they think the competitor
           does that provides real value for their customers, and the three major areas where they
           think the customer's needs are not met". His coaching exercise asks a product manager to
           "evaluate the top 3-5 players in the space" and write a narrative about them.
           Productboard's competitor brief is another narrative form, in six sections that run
           from a company overview to a sales battlecard summary. Cagan's exercise gives no
           maintenance rule. That a table shows that rivals differ and a narrative can say why a
           customer would pick one is this library's reading. Deep dive:
           competitive-analysis_companion.md section 3 (Competitor Briefs).
     ASK   Which rival does a chosen customer have in mind when you lose them, and what do they
           value in it? What does it leave unmet that you could meet? When would a customer
           reasonably pick it over you?
     GOOD  "Northgate Booking: valued for its text reminders, its group booking and its quick
           setup. Leaves unmet: billing, exports without manual steps, and a view of a clinician's
           week. A clinic that already bills through another tool and wants nothing more would
           reasonably pick it."
           (three things valued, the unmet needs, and an honest case for the rival)
     WEAK  "Northgate Booking is a strong competitor with a good product and many customers."
           (nothing a customer values is named, no unmet need, nothing to act on)
     TRAP  Writing the brief as a verdict on whether the rival is good. Cagan's frame is the
           customer's value and the customer's unmet needs, so the brief is a view from the
           customer's side, not a rating of the rival. -->

- The rival: {{brief_competitor}}
- The three things it does that the chosen customers value: {{brief_values}}
- The three needs it leaves unmet: {{brief_unmet_needs}}
- When a chosen customer would reasonably pick it over us: {{brief_pick_reason}}

## Comparison on What Customers Value

<!-- WHAT  The criteria your chosen customers use, each with a weight for how much they care, and
           each rival rated against them, the status quo included. This section is where the
           feature-checklist trap is avoided or not.
     WHY   Steve Blank argues that "a competitive analysis drives a maximum feature set", and asks
           for "No feature lists without facts". Strategyn says "feature-to-feature comparisons is
           no guarantee of success". THRV writes "Feature catch-up with your competitors is a
           race". THRV's page shows no author, so read it as one voice with Strategyn. Product
           School presents the feature matrix as one framework among several: "Which framework you
           choose depends on your goal". As far as this research found, none of them measured the
           harm, so treat the trap as a named failure and not a quantified one. Cagan writes "The
           key is to constantly drive value for your customers." Aha!'s scorecard is "weighted by
           the importance of each attribute to your customers". Productboard's matrix rates a
           feature "fully supported", "partially supported" or "not available", and Calven uses
           the same three levels. Aha!'s guide shows "Harvey Balls" and Dscout's research sheet
           uses a "0 to 5 scale"; no source read measures which scale works better. This library
           takes the customer-value side and a three-level scale. GitLab says the comparison
           "should be completely data/evidence driven". Deep dive:
           competitive-analysis_companion.md section 3 (Comparison on What Customers Value) and
           section 6 (Features or customer value).
     ASK   Where did each criterion come from: what your chosen customers said or did, or a
           rival's feature page? How much does each criterion matter to them, and where did that
           weight come from? Is there a criterion on which a rival leads and the chosen customers
           give it little weight? If so, keep it in the table with its low weight and say what you
           decided.
     PRIORITY  Order criteria by weight, heaviest first, so the table opens on what the chosen
           customers care about most.
     ROW HINT  A good row has a criterion in the customer's words, a weight with its source, and a
           rating in every column that Evidence and Sources can back. A weak row is a feature name
           copied from a rival's page, with no weight. Add one rating column per tier 1 rival, and
           keep the status quo column.
     GOOD  | A new patient can book without calling | High | Raised unprompted in the switch
           interviews we ran | Fully | Fully | Partly | Not at all |
     WEAK  | Has text reminders | | | Yes | Yes | No | No |
           (a feature taken from a rival's list, no weight, and a yes or no in place of a level)
     TRAP  A weight that is a guess. A guess recorded in a cell looks like a finding, so say where
           each weight came from, and mark an unknown weight "unknown" rather than inventing
           one. -->

| What customers value | Weight | Where the weight came from | Us | {{rival_a_name}} | {{rival_b_name}} | {{status_quo_name}} |
|---|---|---|---|---|---|---|
| {{value_criterion}} | {{criterion_weight}} | {{weight_source}} | {{rating_us}} | {{rating_rival_a}} | {{rating_rival_b}} | {{rating_status_quo}} |

- The rating scale, stated once: {{rating_scale}}
- Criteria on which a rival leads and the chosen customers weight lightly, and what you decided
  about them: {{rival_lead_light_weight}}

## Jobs-Based Scorecard

<!-- WHAT  Each job your chosen customers are trying to get done, and how well each rival, and the
           status quo, helps them do it. Full variant only.
     WHY   GitLab's scorecard is built this way: "As a Category Maturity Scorecard is based on Jobs
           to be Done". Strategyn says to compare by "assessing how much better or worse a product
           is at helping the customer get a job done". GitLab's evaluation page likewise compares
           solutions against jobs to be done. Strategyn and THRV both sell a jobs-to-be-done
           method, and THRV's attribution is weak, so read the two as one camp. That this
           section scores whole jobs where the comparison scores single criteria is this
           library's reading. Deep dive: competitive-analysis_companion.md section 3 (Jobs-Based
           Scorecard).
     ASK   What is each chosen customer trying to get done, in their words and not as a feature?
           Which jobs matter most to them? How well does each rival help with the whole job, not
           one step of it? Does the status quo already do this job well enough?
     PRIORITY  Order jobs by importance to the customer, heaviest first.
     ROW HINT  A good row names a job as the customer would say it, how much it matters, and a
           rating per column that Evidence and Sources can back. A weak row names a feature, or
           gives no importance. Add one rating column per tier 1 rival, and keep the status quo
           column. The scorecard uses the rating scale stated in the comparison section.
     GOOD  | Keep the week full without chasing cancellations | High | Partly | Partly | Fully |
           Partly |
     WEAK  | Reminders | | Yes | Yes | No | No |
           (a feature in place of a job, no importance, and a yes or no in place of a level)
     TRAP  Restating the comparison table's rows as jobs. If each job is just a criterion renamed,
           this section adds nothing; a job spans several steps and can be met or missed as a
           whole. -->

| Job the customer is trying to get done | Importance to the customer | How well we help | How well {{rival_a_name}} helps | How well {{rival_b_name}} helps | How well {{status_quo_name}} helps |
|---|---|---|---|---|---|
| {{customer_job}} | {{job_importance}} | {{job_us}} | {{job_rival_a}} | {{job_rival_b}} | {{job_status_quo}} |

## Implications for Our Direction

<!-- WHAT  What the comparison means for your product strategy, your positioning or your roadmap,
           one move per finding, each with an owner and a date. This is the section that makes the
           analysis a strategy document and not a research file.
     WHY   Pragmatic Institute writes "Competitors can provide useful market intelligence, but
           they shouldn’t define your product strategy." Cagan lists "the competitive landscape"
           among the insights a strategy draws on, and also writes "So stop chasing your
           competitors and start focusing on providing real value for your customers". So the
           analysis is an input to strategy and does not set it, and this section is where a
           finding becomes a decision about your product, not a reaction to a rival. Customer
           Impact advises "Let every finding end in one concrete move with an owner and a date",
           and caps the list at three to five actions per quarter. Calven gives the same advice in
           other words. Both sell in this area. Routing each finding to the strategy, the
           positioning or the roadmap is this library's POSITION. Deep dive:
           competitive-analysis_companion.md section 3 (Implications for Our Direction).
     ASK   What does each finding change, and in which document, the strategy, the positioning
           statement or the roadmap? What is the single move, who owns it, and by when? If a
           finding confirms the current direction, what did you confirm and what would have
           changed your view? Is any finding here only a reaction to what a rival did?
     PRIORITY  Order rows by how much of your direction they could change, largest first. Customer
           Impact caps its list at three to five actions per quarter; if you have far more rows,
           check whether the lower ones are decisions or observations.
     ROW HINT  A good row names a finding, the document it routes to, one move, an owner and a
           date. A weak row restates a fact about a rival and names no move.
     GOOD  | Northgate Booking has no billing, and our chosen clinics already ask for it | Roadmap |
           Scope a billing export before any new reminder feature | Head of product | End of next
           quarter |
     WEAK  | Northgate Booking is growing quickly | Strategy | Keep an eye on them | | |
           (a fact about a rival, no decision, no owner, no date)
     TRAP  Letting a rival's move set your strategy. Each row should trace to what the chosen
           customers value in the comparison above, not to what a rival announced. A strategy
           change proposed here goes to the strategy's owner as a proposal, and this analysis does
           not rewrite the strategy. -->

| Finding | Routes to | The move | Owner | By when |
|---|---|---|---|---|
| {{finding}} | {{routes_to}} | {{implication_move}} | {{implication_owner}} | {{implication_date}} |

## Evidence and Sources

<!-- WHAT  A source and a date for each claim in the sections above, and a gap marked "unknown"
           where there is no source. Also whether you used rivals' products, and the legal check.
     WHY   Calven's template asks for "Where each claim came from, and when. Makes the doc
           auditable." Calven also writes "Every field needs a source you can name, and a blank
           field beats a guessed one." The research found one source that prescribes this, and it
           is a vendor's. GitLab says the comparison "should be completely data/evidence driven",
           records the result when teams "Document/update the scoring", and requires a legal check
           of competitors' acceptable use policies before using their products. Aha! lists company
           websites, review sites, industry news and press releases as source types, and Klue warns
           "Don't just rely on CRM data". A confidence rating on each item, in the style of an
           intelligence-community convention, was considered and is not asked for here: no
           competitive-analysis source read uses one. No source read sets how recent evidence must
           be, beyond Calven's one quarter. A dated source lets your reader judge. Deep dive:
           competitive-analysis_companion.md section 3 (Evidence and Sources).
     ASK   For each claim in the profiles and the comparison, where did it come from, and when was
           that source written or read? Which claims rest on one input only, such as CRM data?
           Where did you not find out, and is the cell marked "unknown"? Did you check the legal
           terms before using a rival's product?
     PRIORITY  Group rows by the section the claim appears in, then by the weight of the claim:
           a claim a decision rests on comes before a background fact.
     ROW HINT  A good row names the claim, a source a reader could open, and the date of that
           source. A gap is a row too: the claim, "unknown", and why. A weak row cites "online
           research" or has no date.
     GOOD  | Northgate Booking charges per clinician each month | Its public price page | Read on
           the date of this version | Plans may differ by region; one region checked |
           | Northgate Booking has no billing | Its features and price pages, neither of which
           lists billing | Read on the date of this version | Absent from its pages, and not tested
           in the product |
           | Whether Northgate Booking's reminders cut missed appointments | unknown | | Only the
           vendor's own claim found; asked in no interview |
     WEAK  | Northgate Booking is cheaper | Online research | | |
           (no source anyone could open, no date, and a comparison with nothing to compare)
     TRAP  A guessed cell. A cell with an invented figure reads like knowledge, and the next reader
           cannot tell it from a fact. Write "unknown". -->

| Claim, and where it appears | Source | Source date | Note, including any gap |
|---|---|---|---|
| {{evidence_claim}} | {{evidence_source}} | {{evidence_date}} | {{evidence_note}} |

- Use of rivals' products, and the legal check on their terms: {{legal_check}}

## Refresh Trigger and Versions

<!-- WHAT  The owner, the events that call for a refresh, an interval floor your team chooses, and
           a dated row for each version. Each refresh is a dated snapshot, and the document is the
           series. This is what makes the analysis a standing document and not a one-off.
     WHY   No source offers evidence for any refresh interval, and the stated intervals do not
           converge. GitLab's product side: the comparison "should be done at least annually if
           you're at Complete", its most mature category level, and "Otherwise, when you intend to
           make a category shift". Klue says "Quarterly is a solid default." Aha! says "revisit
           and refresh your competitive analysis biannually". Dovetail offers "Once a year.", "Once
           a quarter." or "Based on specific events." Calven writes "A profile built once is
           usually wrong within a quarter." Apart from GitLab's, every one comes from a vendor,
           and the quarter is an unmeasured vendor claim. Crayon's and HubSpot's cadences are for
           battlecards and sharing with sales, so they are not offered here. Aha! says "Assign a
           point person to keep the report updated throughout the year." At GitLab, "A Product
           Manager will lead their quad team". Crayon's survey reports "47% of respondents" saying
           "marketing owns the compete function". This library reads the difference as one of
           purpose, product strategy against sales enablement. Dovetail names a new product coming
           to market, a shift in a competitor's marketing and a change in customer habits as
           events. The version rows are this library's POSITION, and Klue's pairing of "snapshot"
           with "temporary snapshots that need refreshes as the market changes" is the nearest
           source. Deep dive: competitive-analysis_companion.md section 3 (Refresh Trigger and
           Versions) and section 6 (How often to refresh).
     ASK   Who is the one named owner, and who do they consult? What events would make you refresh
           before the floor? What is the longest you will let the analysis stand, and why that
           long? What changed in each version, where is the earlier one kept, and, if a
           positioning statement already exists, is its revisit event listed here too?
     PRIORITY  Newest version first, so the current state is the first row a reader meets.
     ROW HINT  A good row has a version label, its date, the event or floor that triggered it, what
           changed from the version before, and where that earlier version is kept. A weak row is
           a date with no reason.
     GOOD  | v2 | The date of the refresh | A rival shipped a billing feature | Rated that rival
           partly on the billing criterion and moved one implication to done | Archive, v1 |
     WEAK  | v2 | The date of the refresh | Scheduled | Updated | |
           (no event, no change named, and no way to find the earlier version)
     TRAP  Setting an interval because a vendor named it. None of the intervals is measured, and a
           floor is only useful if you also name the events that would call for a refresh sooner.
           The floor is your own choice. -->

- The one named owner, and who they consult: {{refresh_owner}}
- The events that call for a refresh before the floor: {{refresh_events}}
- The interval floor your team chose, and why: {{refresh_interval_floor}}

| Version | Date | What triggered it | What changed | Where the earlier version is kept |
|---|---|---|---|---|
| {{version_label}} | {{version_date}} | {{version_trigger}} | {{version_changes}} | {{version_prior_location}} |
