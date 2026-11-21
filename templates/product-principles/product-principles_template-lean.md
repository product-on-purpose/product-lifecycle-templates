---
title: "{{product_name}} Product Principles"
doc_type: product-principles
size: lean
product_name: "{{product_name}}"
owner: "{{owner}}"
status: draft
doc_version: "{{doc_version}}"
created: "{{date}}"
updated: "{{date}}"
related_links: []
source_template: product-principles
source_template_version: 0.1.0
---

<!--
LEAN PRODUCT PRINCIPLES. This bundle ships one size, deliberately. No source the research read publishes
a long and a short version of one set. The sources that add depth add it per principle, not per
document, and so does this template. A long variant would model a weight the research did not find.
Confidence in the single size is medium, because it rests on the absence of a published pair. See
product-principles_companion.md section 4 (Variants and sizing).

A PRODUCT PRINCIPLES DOCUMENT IS A SHORT STANDING SET OF BELIEFS that a product team agrees once and
then uses to settle product trade-offs. Cagan defines the type: "Product principles complement the
product vision by stating the values and beliefs that are intended to inform the many product decisions
that will need to be made." He writes that principles are "not a list of features" and "are not tied to
any one product release", and that they are "aligned with the product vision for an entire product
line". This library reads the set as settling what the team builds and what it refuses. That reading
goes past Cagan's sentence, and Slack limits a set to execution, so it is held at medium-low confidence.
The set is a standard that product decisions are judged against, applied by judgement, not by
checkbox: Intercom writes "Principles are not rules - they exist to guide, not control." See
product-principles_companion.md section 1 (Orientation) and section 6 (Debates and contested boundaries).

SOME OF THIS STRUCTURE IS THIS LIBRARY'S OWN POSITION, NOT RECEIVED PRACTICE.
No source the research read publishes a template for this type, other than a vendor's AI prompt
(Productboard's). So the six sections here are assembled from published sets and method articles. Each
principle below carries five fields. A name and a statement appear in every set read. Reasoning is common.
A trade-off written into the principle is shown by several publishers. A field for what a principle rules
out appears per principle only in Productboard's prompt. Of the eight published sets tabulated, none
carries it: Langfuse publishes one set-level list, and Box, as Pendo reports it, a comparable "Versus".
This template asks for more than published sets do, and says so. Where a section is the library's
position, its comment says so. No source read measures whether keeping such a document improves
decisions. The research found nothing on solo practitioners, regulated products or tailoring by
methodology, so the template is untested for all three.

WHAT THIS IS NOT
It is NOT a feature list or a release plan. ProductPlan writes "You don’t build principles".
It is NOT mission, vision or goals. ProductPlan calls "conflating the company’s mission, product vision,
and goals with product principles" a common mistake.
It is NOT a project's own principles. Cagan's 2005 guide has principles "specific to your domain and your
particular project". This bundle is the standing set. A principle that belongs to one project goes in
that project's PRD (see prd_template-full.md). Intercom does both, which shows they can coexist.
It is NOT a few rules inside a strategy. That is a matter of size: the Product Principles section of the
product-strategy one-pager holds two to five rules inside a strategy, and this bundle holds the standing
set with a reason, a cost, a boundary and a settled decision for each principle.
It is NOT design principles. The line is this library's own test, and the sibling design-principles
bundle states it from the other side: ask what a principle settles. If it settles how a screen, a
message or an interaction behaves, it belongs in design principles. If it settles what the team builds,
funds or declines, it belongs here. No source draws the line in those words. Some principles straddle
it, and this document should say so rather than hide them, in the last field of Purpose and Scope.
Write "product principles" for this set. One vendor source (The Org) uses "principles of product" for the
design phase, so the wording invites confusion.

All names, dates and figures in the GOOD and WEAK illustrations below are invented.

HOW TO FILL THIS IN
1. Read the comment under each heading: WHAT it wants, WHY it matters (with a pointer into
   product-principles_companion.md), guiding questions to ASK, a GOOD and a WEAK example, and the TRAP to
   avoid. Three tables also carry PRIORITY and ROW HINT.
2. Replace each {{placeholder}} with your content. Draft Purpose and Scope first, then The Principles,
   then When Principles Conflict, then the rest. Within The Principles, start from a decision the team
   has argued about, ask which option a principle would have chosen, write what it rules out and what it
   costs, and draft the statement last.
3. If a section, or one row inside a table, does not apply, write "N/A" and one line of why, rather than
   leaving it blank or deleting the section.
4. This is a standing document, reopened on the Review Trigger below. Before you first share it:
   self-grade against product-principles_guide.md, then DELETE every HTML comment. Keep the
   source_template and source_template_version frontmatter fields: they are the only record of which
   template and version produced this document. Write the principles in the team's own words. No page
   the research read states a reuse licence, and Productboard reserves its rights, so a set copied from
   another company is untested here.
-->

# {{product_name}} Product Principles

## Purpose and Scope

<!-- WHAT  The product or products the set covers, the level at which it applies, what kinds of decision it
           settles, how it relates to the product vision, the product strategy and the design principles,
           and which principles, if any, also settle how a screen behaves.
     WHY   A set with no stated scope leaves a new product with no way to know whether the set covers it.
           That reading is this library's. Sources place sets at different levels. Cagan's 2017 chapter
           has principles "aligned with the product vision for an entire product line", and Slack
           writes "Product principles should be company-wide, not siloed into the product or design
           team." Kindel describes tenets at company, organisation, team and project levels. Stating the level is a
           field this library adds, assembled from sources that each place a set at one level. What the
           set settles is itself disputed. ProductPlan says principles "guide what you decide to build and
           how to build it", and Cagan ties them to the many product decisions a team makes. Slack scopes
           them to "inform execution rather than roadmapping, strategic thinking or planning". This
           template follows Cagan and ProductPlan, which is the library's reading, held at medium-low
           confidence because the sources read it both ways. An author who wants Slack's limit can state
           it here. The line with design principles is this library's test. Intercom keeps five product
           design principles inside its product principles, so some principles will straddle. The last
           field asks the author to name them and say why, or to write "None" with a reason. No source
           read asks for it.
           Deep dive: product-principles_companion.md section 3 (Anatomy > Purpose and Scope).
     ASK   Which product or products does this set cover, and is it company-wide, per product line or per
           product? Which kinds of decision does it settle, and which does it leave alone? How does it
           relate to the product vision, the product strategy and the design principles, and does it
           outlast the current strategy? Which principles, if any, also settle how a screen, message or
           interaction behaves, and why?
     GOOD  "These principles cover Kestrel Ledger, the bookkeeping app for freelancers. They apply at the
           product level, and the two product managers, the design lead and the engineering lead use
           them. They settle what we build, fund or decline. They do not settle how a screen behaves,
           which belongs to the design principles. They sit beside the vision and the current strategy,
           and they outlast the strategy." For the last field: "Principle 2, File it for them before we
           explain it, also reaches into design, because it decides what a button does as well as
           whether we build it. We keep it here because its test is whether we fund the filing step,
           and the design principles settle how the button reads."
     WEAK  "These principles apply to everything we make." (names no product, no level and no kind of
           decision) For the last field: "None." (gives no reason, so a reader cannot tell whether the
           author tested each principle against the what-does-it-settle question or never looked)
     TRAP  A scope that drifts toward how a screen behaves. That has strayed into design principles,
           which is the library's own judgement and no source states it. A close cousin is a scope that
           names a single project, which makes this a project's principles, and those belong in that
           project's PRD. A last slip is restating the current strategy's choices as scope: the set
           outlives any one strategy. -->

**Product or products covered:** {{product_covered}}

**Level of the set (company, product line or product) and who applies it:** {{set_level_and_users}}

**Decisions this set settles, and decisions it does not:** {{decisions_scope}}

**Relation to the product vision, the product strategy and the design principles, and whether the set outlasts the current strategy:** {{neighbour_relations}}

**Principles that also settle how a screen behaves:** {{straddling_principles}}

## The Principles

<!-- WHAT  Three to five principles. Each carries five fields: a statement, why we hold it, the trade-off
           it accepts, what it rules out, and a decision it settled. This section is the document. Copy
           the block below to add a fourth or fifth principle.
     WHY   Cagan's definition makes principles the thing meant to inform the many product decisions a
           team makes, so each has to be specific enough to inform one. The three to five figure is
           advice, not a finding. Gazit writes "No more than three to five principles are needed."
           Slack caps a set at "no more than seven", ThoughtSpot "landed on seven" after debating the
           count, and Intercom holds fourteen in layers. Of the eight published sets tabulated, only
           Slack's and PostHog's fall inside three to five. None of the sources cites a measurement.
           STATEMENT: every set read carries a name and a statement. WHY WE HOLD IT: Cagan writes "The
           product team needs to understand these principles and the reasoning behind each one."
           GitLab and Monzo give a reasoning paragraph. THE TRADE-OFF IT ACCEPTS: GitLab writes three of eight in an "X over Y" form, such
           as "We value quality over velocity". Linear names a sequence in "Simple first, then
           powerful". Box, as Pendo reports it, published a named cost with each principle, such as "The
           tradeoff? Expense." Productboard's prompt has a field headed "TENSION". Writing the cost into
           the principle keeps it attached when someone quotes the principle, which is this library's
           reading of why the form matters, not a finding. WHAT IT RULES OUT: Productboard's prompt has a
           field headed "WHAT IT MEANS WE WON'T DO", and it is a vendor's AI prompt, not a published set.
           Langfuse's handbook has a list headed "What we don't do", as one list for the whole set. No
           published set read carries the field per principle, so asking for it is this library's
           position. A DECISION IT SETTLED: Monzo follows two principles with a case study, such as "Case
           Study: Refunding customers during the upgrade". Slack's "How it shows up:" gives a product
           example. Asking for one real case on every principle is this library's addition.
           THE TRUISM TEST, AND THE DISSENT. Intercom writes "no principle is a truism" and "The opposite
           of a principle should itself be a principle". AWS, writing about tenets,
           says a tenet needs "an opposite which could be acceptable to an organisation". Productboard's
           prompt says a principle without a reasonable opposite is "not a principle". airfocus holds a
           different view, that principles "should trigger an emotional response". This template follows
           Intercom, AWS and Productboard. The library's reasoning is that a reader can apply the
           opposite test and cannot apply an emotional response. Distrusting a principle that no proposed
           decision has ever strained is this library's inference from the opposite test.
           Deep dive: product-principles_companion.md section 3 (Anatomy > The Principles) and section 6
           (Debates and contested boundaries).
     ASK   Which decision has the team argued about, which option did this principle choose, and could a
           reasonable team choose the opposite? What does the principle cost, and who bears that cost?
           What can the team no longer do once it adopts the principle, and is there a request someone
           has already made that it turns down? Which real case did it settle, and what reasoning would
           a new product manager need to hold it?
     GOOD  Principle 1: "Freelancers before accountants." Statement: "When a request would make Kestrel
           Ledger faster for a freelancer doing their own books but slower to set up for a bookkeeper who
           manages many clients, we build for the freelancer." Why we hold it: "In the invented 2024
           customer survey, most paying accounts were sole traders who do their own books, and the
           accountants who tried the product left in the first month for tools with batch features."
           The trade-off it accepts: "Bookkeeping firms will choose a rival with batch tools, and our
           multi-client revenue stays small." What it rules out: "Multi-client workspaces, approval
           chains between a bookkeeper and a client, and bulk import wizards for a firm's client list.
           A partner firm with sixty clients asked for the first of these." A decision it settled: "In
           2025 the partner firm asked for a multi-client switcher. We turned it down, and shipped a
           shared-folder export a freelancer can send to their own bookkeeper."
     WEAK  Principle 1: "Put the customer first." Statement: "We always put our customers first." Why we
           hold it: "Customers matter." The trade-off it accepts: "None." What it rules out: "Bad
           experiences." A decision it settled: "Many." (a truism: no reasonable team would choose the
           opposite, so it rules nothing out, it names no cost, and no field names a real decision or a
           real reason)
     TRAP  A truism, which cannot settle an argument however well it lands. A close cousin is a principle
           with no stated cost, which cannot show what it gives up. A third is a feature or a release
           plan dressed as a principle, or a principle that restates one period's strategy and will go
           stale when the strategy does. That last caution is this library's, not a sourced one. A last
           slip is copying a principle from another company's set, which may not pass the team's own
           opposite test. -->

**Principle 1: {{principle_1_name}}**

- **Statement:** {{principle_1_statement}}
- **Why we hold it:** {{principle_1_why}}
- **The trade-off it accepts:** {{principle_1_tradeoff}}
- **What it rules out:** {{principle_1_rules_out}}
- **A decision it settled:** {{principle_1_decision_settled}}

**Principle 2: {{principle_2_name}}**

- **Statement:** {{principle_2_statement}}
- **Why we hold it:** {{principle_2_why}}
- **The trade-off it accepts:** {{principle_2_tradeoff}}
- **What it rules out:** {{principle_2_rules_out}}
- **A decision it settled:** {{principle_2_decision_settled}}

**Principle 3: {{principle_3_name}}**

- **Statement:** {{principle_3_statement}}
- **Why we hold it:** {{principle_3_why}}
- **The trade-off it accepts:** {{principle_3_tradeoff}}
- **What it rules out:** {{principle_3_rules_out}}
- **A decision it settled:** {{principle_3_decision_settled}}

## When Principles Conflict

<!-- WHAT  A table that says which principle wins when two pull apart, and in which kind of decision.
     WHY   AWS expects tensions between tenets and says they need judgement. ProductPlan writes "The
           principles should clearly state what is most important." Productboard's prompt has a set-level
           section headed "When Principles Conflict", though the research cannot say what that section
           demands beyond its heading. A set that never says which one wins leaves the argument to
           whoever is in the room. That last sentence is this library's inference, not a sourced claim.
           THIS SECTION TAKES A SIDE IN A LIVE DISPUTE, AND THE SIDE IS THIS LIBRARY'S POSITION.
           ThoughtSpot stack-ranked its candidates "within each category from most to least important",
           and the same post says "it didn’t matter if some principles contradicted others". Nielsen
           Norman Group, writing about design principles, takes a middle position: principles should "Not conflict with
           one another", and where two matter, "then clearly specify in which contexts one of these
           principles is more important than the other". No source read opposes ordering outright, and
           none gives a worked rule for two principles that conflict. This template asks the author to
           say which principle wins in a named kind of decision. That is closest to the NN/g position,
           which is a method analogue for design principles and not product evidence, and it is the
           library's choice. A resolution can take other forms. GitLab puts the priority inside the
           principle with "X over Y", and Eriksson teaches the "even over" form. A ranked list is the
           other shape. A resolution scoped to a kind of decision is less brittle than a global order,
           and that reading is the library's.
           Deep dive: product-principles_companion.md section 3 (Anatomy > When Principles Conflict) and
           section 6 (Debates and contested boundaries).
     ASK   Which two principles are most likely to collide? In which kind of decision do they collide?
           Which one wins there, and why? Is the answer different in another kind of decision?
     PRIORITY  Resolve the most likely collision first, and do not rank every pair. One resolved conflict
           in a named kind of decision is worth more than a complete table nobody applies. That is this
           library's advice, not a sourced rule.
     ROW HINT  A good row names the two principles, names the kind of decision, says which principle wins
           there and gives the reason. A weak row says both matter equally.
     GOOD  | Freelancers before accountants, against File it for them before we explain it | A request
           for a batch filing tool that files for many clients at once | Freelancers before accountants |
           The filing step is in scope for one freelancer, and the batch tool serves a firm, so it waits
           until a freelancer can file in two taps. |
     WEAK  | All of them | Everything | Use judgement | They are all important. | (no pair, no kind of
           decision, no winner)
     TRAP  Saying that all principles are equally important, or ranking every pair. A close cousin is a
           row whose winner is the principle that sounds better, with no reason given. -->

| Principles in tension | Kind of decision | Which wins | Why |
|---|---|---|---|
| {{conflict_principles}} | {{conflict_decision_kind}} | {{conflict_winner}} | {{conflict_reason}} |

## Using Them in Decisions

<!-- WHAT  Where the set is applied, such as product review, prioritisation, a request the team may decline
           and onboarding, how a decision cites a principle, and how a new joiner meets the set.
     WHY   The sources describe sets in use, mostly in review settings. At Slack, product managers and
           designers "reference them in weekly workshops where projects are shared at every stage", and
           Slack advises "it’s critical to designate clear checkpoints for assessing your work against
           the principles". Cagan reports that teams tell him principles are "the part of the strategic
           context that they use most often in their daily discovery work". That is his report of what
           teams tell him, not a measurement. The research found no measured effect of a set on
           decisions. SAYING NO IS ASSERTED MORE THAN SHOWN. Pendo reports that Box does not pursue
           a feature idea that fails its principles. This research found no named company source that
           describes a principle declining a specific request. This template names saying no as a moment to record, which is the
           library's position, and confidence that sets are used this way is medium-low. ONBOARDING IS A
           USE. Intercom's new joiners get an onboarding pack that includes a first problem statement the
           company calls an Intermission. HOW A DECISION CITES A PRINCIPLE IS THE LIBRARY'S POSITION.
           ProductPlan names the ability to point back to a principle to justify a decision, but no
           source read prescribes a citation form. The set is judged against by judgement, not mechanical
           compliance. This library infers that a set no decision ever cites is decoration. That
           inference is not a sourced finding.
           Deep dive: product-principles_companion.md section 3 (Anatomy > Using Them in Decisions).
     ASK   In which two or three moments is a principle cited: a product review, a prioritisation
           discussion, a request the team is about to turn down? How is the citation written down? How
           does a new joiner meet the set, and who walks them through it?
     GOOD  "Applied in the monthly product review, when the product managers rank the backlog, and when
           we are about to turn down a request from a customer or a partner. A decision record carries one
           line naming the principle relied on and, if a principle was set aside, which one and why. A
           reviewer may accept the reasoning without accepting the outcome, and says which. A new product
           manager reads the set in their first week and brings one past decision they think it would
           have changed."
     WEAK  "Product managers should keep the principles in mind." (names no moment and no form of
           citation)
     TRAP  A set that is read at adoption and never cited again, or a citation so mechanical that it
           becomes a checkbox. A close cousin is a claim that the set is used to say no, with no case. -->

**Where the set is applied:** {{where_applied}}

**How a decision cites a principle:** {{how_decisions_cite}}

**How a new joiner meets the set:** {{new_joiner_use}}

## Ownership and Changes

<!-- WHAT  The named owner, how anyone proposes a change, who decides, and a dated change log.
     WHY   This is where the set's own staleness is handled. No source read names who owns a set after
           it is written, or who approves a later change. LogRocket describes leadership signing off a
           draft. The role names this template asks for are the library's position. Cagan's 2020 text has product leaders prepare the set. Intercom
           describes organic change: its principles "evolve very slowly". THE AUTHORSHIP DEBATE
           SITS BEHIND THIS FIELD, AND THIS TEMPLATE DOES NOT SETTLE IT. ProductPlan writes "defined
           product principles are driven by the team itself". Product School says "Talk to your team,
           not just leadership". LogRocket writes "A hybrid approach works better", in which leadership
           presents a draft and sharpens it with the team. The template asks only that an owner be named
           and that the way a change is proposed be stated. THE DATED RECORD IS SOURCED IN PRACTICE, NOT
           IN METHOD. Intercom gives the one dated record of a set changing. In 2019 it said it used to
           have five principles and "merged three of them into one". Slack's set differs by one principle
           between its 2021 list and a later list, with no reason given in either source, so that is a
           comparison and not a change record. Revision is
           invited, and rarely: Kindel's tenets carry "unless you know better ones", and ProductPlan says
           "An update should be an unusual and well-considered event, not a regular occurrence." So
           record a retirement or a merge as a change and keep the reason. That advice is the library's.
           Intercom's merge is the one sourced example.
           Deep dive: product-principles_companion.md section 3 (Anatomy > Ownership and Changes).
     ASK   Who owns this set, by role and by name? Where does anyone propose a change? Who decides? When
           was the set first agreed, and what has changed since, including anything merged or retired?
     PRIORITY  Start the log with the date the set was first agreed, so the first row is never blank.
     ROW HINT  A good row has a date, says what changed in a sentence a stranger could follow, and names
           what fired it. A weak row is a date and the word "updated".
     GOOD  | 2025-11-04 | Principle 3 merged into principle 1: two decisions in a row were settled by
           citing both, and nobody could say how they differed | Review Trigger: a valid exception keeps
           recurring | Head of product |
     WEAK  | 2025-11-04 | Updated | | | (no change a stranger could follow, no trigger and no decider)
     TRAP  A set with no owner and no condition that reopens it. A change log that shows only additions
           hides the retirements and merges. -->

**Owner (role and person):** {{owner_role_and_person}}

**How anyone proposes a change:** {{how_to_propose}}

**Who decides a change:** {{who_decides}}

| Date | What changed | What fired it | Who decided |
|---|---|---|---|
| {{change_date}} | {{change_summary}} | {{change_trigger}} | {{change_decider}} |

## Review Trigger

<!-- WHAT  A table of conditions, owners and actions: what event makes this set wrong or incomplete, who
           notices, and what they do about it. The conditions are things an owner can observe, not dates.
     WHY   The standing-standards family requires every member to carry this mechanism, because members
           fail by going quietly out of date. No source read names an owner for a trigger. The owner
           column is this library's, and the conditions are statements of intent, not logged events.
           Where a condition has a source, it is named here. Productboard's AI prompt, a vendor's prompt,
           lists three conditions for revisiting a set, and this template restates them in its own rows:
           "The company strategy changes significantly", a principle "consistently violated one without
           deciding to change it", and a new principle that "would have resolved 3+ debates in the last
           quarter". The threshold of three or more debates is the vendor's figure and not a measured
           one. A valid exception: Intercom says to "try and re-codify that back in or change a
           principle, evolve it". The quotation carries no count, so "recurs" and its threshold of a
           second occurrence are this library's reading. A principle does not take hold: Slack says to
           observe how it is used and "tune it based on your findings". THE STATED
           INTERVALS DISAGREE, AND THIS TEMPLATE TAKES NONE OF THEM. Guru says principles should "hold
           their ground for at least a year". LogRocket says "Review your product principles every three
           months", which is a review and not a rewrite. Intercom says "We also update them every 1-2
           years". ProductPlan says updates should be unusual. None cites a measurement. No calendar
           interval is required, and the foundation classification holds. A team that wants a review date
           may add one as a floor and should label it as its own choice.
           Deep dive: product-principles_companion.md section 3 (Anatomy > Review Trigger).
     ASK   What could the owner observe that shows this set is wrong? Who notices each condition, by
           role? What do they do about it: reopen the set, run a short check against recent decisions, or
           write the change into the log?
     PRIORITY  List the conditions an owner is most likely to see first, and write each as an event
           someone can observe, not as a date. The strategy row is the visible link to the product
           strategy, which this set outlives and does not restate.
     ROW HINT  A good row states a condition the owner could observe, names a role as owner, and states an
           action. A weak row says "review regularly" and names no one.
     GOOD  | The strategy changes significantly | Head of product | Read each principle against the new
           strategy within a month, keep those still sound, and write any merge, retirement or addition
           into the change log with the reason. |
     WEAK  | Review regularly | The team | Update the principles. | (a condition nobody could observe, no
           named role as owner and no action anyone could take)
     TRAP  Writing a date as the only trigger, or naming one condition and treating it as the whole
           mechanism. Tie a row to a line in the change log when it fires. -->

| Condition | Owner | What They Do About It |
|---|---|---|
| The strategy changes significantly | {{strategy_change_owner}} | {{strategy_change_action}} |
| A principle is consistently violated without a decision to change it | {{violation_owner}} | {{violation_action}} |
| A new principle would have settled repeated debates | {{repeated_debate_owner}} | {{repeated_debate_action}} |
| A valid exception recurs | {{exception_owner}} | {{exception_action}} |
| A principle does not take hold | {{not_taking_hold_owner}} | {{not_taking_hold_action}} |
