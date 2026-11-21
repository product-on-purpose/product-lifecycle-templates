# Guide: Product Principles (operator card)

The short card. The reasoning behind every rule here, with the sources, is in
[`product-principles_companion.md`](product-principles_companion.md). A fully worked instance is
[`product-principles_example.md`](product-principles_example.md). Where this card calls something the
library's position, no source read for the bundle publishes it, and the card says so each time.

**What this document decides.** A product principles document settles which way a product decision
should lean when two good options compete: what the team builds, funds or declines. That reading goes
past Cagan's own definition, which speaks of the values and beliefs that inform product decisions, so it
is the library's. It does not settle how a screen, a message or an interaction behaves for the person using it. That test is
the library's own inference, at medium-low confidence. The sources split product principles from design
principles by scope, and no source draws the line in these words. Published sets cross it, so some
principles will straddle. The Purpose and Scope section has a field where the document says which ones.

**What to call it.** Write "product principles" for the standing set that settles what the team builds.
One vendor source, The Org, uses "principles of product" for the design phase, so that wording invites
confusion with the sibling bundle [`design-principles`](../design-principles/design-principles_guide.md).

## When to use

- The team keeps arguing the same trade-off between two good options, and nothing written says which way
  to lean. Cagan's 2020 position is that principles help a team see which values it prioritises when it
  makes a trade-off. One vendor's AI prompt treats three or more debates in a quarter that a new
  principle would have settled as a reason to add one. That is the vendor's figure, not a measured one.
- A request keeps arriving that the team feels it should decline, and nobody can say why in a sentence.
  The set can hold the reason. Sources assert that principles are used to say no, and this research found
  no named company case that shows it, so treat that benefit as unproven.
- Leadership has written a product vision and a strategy and wants the beliefs that sit beside them
  written down. Cagan places principles beside the vision and the strategy, and his 2020 text has product
  leaders preparing the set for every team.
- A new product or team has joined, and nobody can say whether the existing set covers it. The Purpose
  and Scope section holds the answer.
- A new product manager needs to learn how the team decides. Intercom puts a first problem statement in
  its new-joiner onboarding pack, and says it uses its principles to assess and debate options.
- A set already exists and nobody cites it. Grade it with the rubric below, then rewrite the rows that
  score 0.
- The strategy has changed significantly and the set has not been read against it. Productboard's prompt
  names that as a condition for revisiting a set, and the Review Trigger section carries it.

## When NOT to use

Several documents get mistaken for product principles. The table says which one you likely need.

| You actually need | Because |
|---|---|
| **Design principles** | Those settle how a screen, a message or an interaction behaves. This document settles what the team builds, funds or declines. The sources split the two by scope (ProductPlan, airfocus, Marc Abraham). The line in these words is the library's, at medium-low confidence. When a principle straddles, say so in the Purpose and Scope field built for it. See the [`design-principles` guide](../design-principles/design-principles_guide.md). |
| **A few rules inside a strategy** | The Product Principles section of the [`product-strategy` one-pager](../product-strategy/product-strategy_template-one-pager-full.md) holds two to five rules inside a strategy. This bundle holds the standing set, with a reason, a cost, a boundary and a settled decision for each principle. The choice is a matter of size, and the library's. |
| **A project's own principles** | Cagan's 2005 guide places them inside a PRD, "specific to your domain and your particular project". His later writing has principles not tied to one release. Put a project's own principles in that project's [PRD](../prd/prd_guide.md). Intercom keeps both a standing set and occasional per-project principles, so the two can coexist. |
| **Mission, vision or goals** | ProductPlan calls conflating the three with principles "a common mistake". The [product vision](../product-vision/product-vision_guide.md) says where the product is going, and the [product strategy](../product-strategy/product-strategy_guide.md) says how it will get there. A principle says which way a trade-off leans on the way. That last reading is the library's. |
| **Company values** | The sources read that address values (Abraham, Guru, ProductPlan) put them upstream and broader, and Cagan's 2020 text has principles state values and beliefs. No source gives a test between a value and a principle. The `product-strategy` one-pager's TRAP supplies one, which is the library's: values describe how you want to behave, and principles decide arguments. |
| **A feature list or a release plan** | Cagan writes that principles are "not a list of features" and are not tied to one release. Ask whether the line could be shipped and finished. A principle is never reached. |
| **A rule book or a compliance checklist** | Intercom writes "Principles are not rules - they exist to guide, not control." A set meant to be checked off item by item is a different document. |

## Pick a variant

This bundle ships one size, lean, so there is no variant to choose. The reason is in
[`product-principles_companion.md` section 4](product-principles_companion.md#4-variants-and-sizing). No
source read publishes a long and a short version of one set, and confidence in a single size is medium.
Four choices remain inside it.

1. **How many principles.** Three to five is advice, not a finding, and the template ships three
   principle blocks. Sources say three to five, up to seven, or fourteen in layers, and none cites a
   measurement. Add a fourth or fifth only when you can attach a real decision to it.
2. **What level the set covers.** Company, product line or product. Sources place sets at each level, and
   the template asks the author to state which. A team that needs only two or three rules inside its
   strategy should use the one-pager's section instead.
3. **How the conflict section resolves.** The template asks for a winner in a named kind of decision.
   The library chose that over a global ranking, and no source opposes ordering outright. A principle
   written in an "X over Y" form may carry part of its own resolution.
4. **Which fields to leave honest.** If a principle has no settled case yet, write that plainly and give
   a line of why. Do not invent a case, a request or a source.

## Run these tests on each principle before you grade

1. **The opposite test.** Intercom writes "no principle is a truism", and its test is to flip the
   principle around to express the exact opposite and see whether it holds up. AWS, writing about
   tenets, says the same of an opposite an organisation could accept, and a vendor's AI prompt agrees.
   Name the team or product that would reasonably choose the opposite. If you cannot, rewrite the
   statement. One vendor, airfocus, wants a principle that triggers an emotional response, and a line
   nobody would oppose can pass that test. The template follows the opposite test, because a reader can
   apply it.
2. **The cost test.** Name what the principle gives up and who bears it. Gazit's rule is to take a stand
   by preferring one alternative over the other. Box, as Pendo reports it, published a named cost with
   each principle: "The tradeoff? Expense." If the cost is blank, the principle has taken no stand. This
   is a field the library asks for, and published sets show it in several forms.
3. **The say-no test.** Write down a choice the team could have made and can no longer make because of
   the principle. That is the "What it rules out" field. No published set read carries it per
   principle, so it is the library's request, and the template says so.
4. **The decision test.** Name one real decision the principle settled and the option it turned down. If
   you cannot attach a decision to a principle, it is probably not yet a principle. That sentence is the
   library's advice, not a sourced finding. An honest "no decision has met this yet" is allowed, and
   row 6 scores it.
5. **The what-does-it-settle test.** Ask what the principle decides. If it decides what the team builds,
   funds or declines, it belongs here. If it decides how a screen, a message or an interaction behaves,
   it belongs in `design-principles`. If it decides both, say so in the straddling field.

## Quality rubric (self-grade)

This bundle ships one size, so all twelve rows apply and no scope table is needed. Score each row 0, 1
or 2. A score under 16 out of 24 means several rows are thin or empty, so the set will not yet settle
an argument. A product manager facing a trade-off will find principles that can be read either way, or
that cost nothing, or that nobody owns, and the decision goes back to whoever is in the room. The line
at 16 is the library's judgement and is not measured. The total does not say which rows failed. Read
the rows that scored 0 first, because a 0 on row 2 (a principle that cannot be reversed) or on row 7 (no
way to choose between two principles) leaves a set that cannot decide, even when other rows score well.
Grade what the author added to the blank template. The template already prints the field labels and the
five conditions in the Review Trigger table, so a row that rewards their presence is satisfied before
anyone writes a word.

| # | Criterion | 0 | 1 | 2 |
|---|---|---|---|---|
| 1 | **Scope is bounded** | No product is named, or the scope covers "everything we make" | The product and its level are named, but nothing says which kinds of decision the set leaves alone, or how it sits beside the vision, the strategy and the design principles | You can point at the sentence naming the product, the level and the people who apply the set, at one kind of decision the set refuses to settle and where that decision goes instead, and at the line saying how the set sits beside the strategy and outlives it |
| 2 | **Principles can be reversed** | The statements are ones no thoughtful team would reject, such as "put the customer first", or the section is blank | Some principles can be reversed, and others pass only because nobody would oppose them | For every principle, a colleague who did not write the set can state the opposite approach and name a team or product that would reasonably choose it |
| 3 | **Costs are named** | The trade-off field is blank, says "none", or repeats the statement | A cost is named, but it is vague, or nobody is said to bear it, or the option it gives up is not stated | For every principle you can point at the option it gives up and the people who bear the cost, and one of those people would recognise the cost as real |
| 4 | **Refusals are real** | The rules-out field is blank, repeats the statement, or names "bad experiences" | Some principles name a choice a team could have made, and others rule out only what nobody would choose | For every principle you can point at a choice the team could have made and now cannot. Where a real request has been turned down, the request and who asked are named |
| 5 | **Reasons are held** | The reasoning field is blank, says "customers matter", or repeats the statement | A reason is given, but a reader cannot tell what it rests on, or it would justify the opposite principle as well | A new product manager who was not in the room can say, from the reason alone, why the team accepts the cost named in row 3, and you can point at the observation, decision or stated belief it rests on |
| 6 | **Cases are real** | The field says "many", describes a case no one can place, or is blank | A case is described, but the option it turned down is not named, or the same outcome would have followed without the principle, or the field says plainly that no decision has met the principle yet | You can point at the review, request or decision record where the principle settled something, the option it turned down is named, and someone who was there would recognise the account |
| 7 | **A conflict is resolved** | The section says every principle matters equally, answers "use judgement", or is blank | Two principles are named and a winner is stated, but the kind of decision is "everything" or no reason is given | You can point at two principles, a named kind of decision where they collide, which one wins there and why, and a product manager could apply it to the next decision of that kind without asking the author |
| 8 | **Use has a place** | The section says product managers should keep the principles in mind, or is blank | Moments of use are named, but the form of a citation is missing, or what a reviewer may do when a decision sets a principle aside, or how a new joiner meets the set | You can point at the moments where the set is cited, at the line a decision record carries, including which principle was set aside and why, and at how a new joiner meets the set, and someone who was not in the room could write that line |
| 9 | **Owner is reachable** | "The team", or no owner | A role is named without a person, or the place to propose a change or who decides is missing | You can point at the role and the person who own the set, the place where anyone proposes a change and who decides, and you could message the owner today |
| 10 | **Changes keep reasons** | The log is blank, or each entry is a date and the word "updated" | Entries say what changed but not what fired the change, or a merge or retirement leaves no reason | The first row gives the date the set was first agreed and who decided it. Each later row says what changed in a sentence a stranger could follow and names what fired it, and a merged or retired principle keeps its reason |
| 11 | **Triggers carry owners** | The Review Trigger table still holds the template's placeholders, or every owner is "the team", or the only condition is a date | Some conditions have a role and an action, but at least one has neither, or a condition that does not apply is left with the template's wording instead of "N/A" and a reason | Every condition has a role as owner and an action that person takes, such as reopening the set or writing a dated line in the change log, and any condition that has already fired points at its line in the change log |
| 12 | **Decisions, not screens** | Several principles settle how a screen, a message or an interaction behaves, or the set restates a design principle, or the set holds no principles, or the straddling field is blank | The statements settle what is built, funded or declined, but the straddling field says "None" with no reason, or a principle that also decides how a screen behaves is not named in it | You can apply the what-does-it-settle test to every principle and each decides what the team builds, funds or declines, and the straddling field either names every principle that also decides how a screen behaves and says why it stays here, or says "None" and gives the reason |

Every cell above describes evidence, not a count. The test for each cell is whether someone could
satisfy it without improving the document. If they could, the cell is written wrong. The rubric does
not grade how many principles the set holds, because the number is advice and not a finding.

Rows 3 to 6 grade fields that published sets carry unevenly. A name and a statement appear in every set
the research read, and reasoning is common. A trade-off written into a principle is shown by several
publishers. A per-principle rules-out field appears only in a vendor's AI prompt among the sets and
prompts tabulated, and Box's per-principle "Versus" is a comparable field found outside that table. An
examples field appears in two sets: Monzo's is a case study of a settled decision, and Slack's is a
product example. An honest "no decision has met this yet" scores 1 on row 6, so a new set can clear the line
without inventing a case. Grade with someone who did not write the set. The blank template should score 0
on every row.

## Named anti-patterns (the usual wrecks)

Each entry gives the failure, the test that catches it and the rubric row it costs. The arguments behind
them, and the disputes among sources, are in the companion's sections 6 and 7.

1. **The truism.** A principle whose opposite no reasonable team would choose, which cannot settle an
   argument however well it lands. Intercom: "no principle is a truism". Test: name the team that would
   choose the opposite. Costs row 2.
2. **The feature list or the release plan.** A line the team could ship and finish. Cagan says principles
   are not a list of features and are not tied to one release. Test: could the line ever be done? Costs
   rows 2 and 4.
3. **Mission, vision or goals relabelled.** ProductPlan: "A product principle is never “reached.”" Test:
   does the line describe a destination or a measure, or a way to choose on the road there? Costs rows 2
   and 4.
4. **No stated cost.** A principle that names nothing it gives up has taken no stand. Gazit: "Take a stand
   by preferring one alternative over the other(s)." Test: who loses when this principle wins? Costs
   row 3.
5. **Too many.** Sources say three to five, up to seven, or fourteen in layers, and none cites a
   measurement. Test: can you attach a real decision to each one? Costs row 6.
6. **A set nobody cites.** The library's inference is that a set with no stated moment of use risks being
   read once and not applied. The research found no measured effect of a set on decisions. Test: could
   someone who was not in the room write the citation line? Costs row 8.
7. **Principles treated as rules.** Intercom's podcast says "these are guides, they’re not rules", and its
   blog says principles exist to guide and not to control. Test: does a decision cite the principle it
   leaned on and the one it set aside, with a reason? A citation so mechanical that it becomes a checkbox
   has lost that reading. Costs row 8.
8. **A claim that principles say no, with no case behind it.** Pendo reports that Box does not pursue a
   feature idea that fails its principles, and PostHog argues that principles make it easier to say no.
   This research found no named company source describing a principle used to decline a specific
   request. Test: can you name the request and who asked? Costs rows 4 and 6.
9. **A principle the team consistently violates.** A vendor's prompt treats consistent violation without a
   decision to change the principle as a reason to reopen the set. The library reads a violated principle
   as either a wrong principle or a missing decision. Test: does a Review Trigger row cover it, with an
   owner? Costs row 11.
10. **Project principles inside the standing set.** A principle that belongs to one project goes in that
    project's PRD. Test: would it still hold on the next product line? Costs row 1.
11. **A set that restates the current strategy.** The library's own caution, not a sourced one. A
    principle that restates one period's strategy choice will go stale when that strategy does, and no
    source ties a principle's life to a strategy period. Test: would the principle survive a change of
    strategy? Costs rows 1 and 11.
12. **A design principle in the product set.** A principle that settles how a screen, a message or an
    interaction behaves belongs to design principles. This is the library's test. Test: the
    what-does-it-settle question. Costs row 12.
13. **No stated order when two collide.** AWS expects tensions between tenets and says they need
    judgement. The library's inference is that a set that never says which principle wins leaves the
    argument to whoever is in the room. Test: does the table name a winner in a named kind of decision?
    Costs row 7.
14. **A set that never changes, or changes with no record.** Intercom's record shows five principles
    merged into three, and a later set of four at the top level. Slack's set differs between two
    snapshots with no stated reason. A set with no owner and no reopening condition has no way to do
    either on purpose. Test: does the log keep the reason for each merge or retirement, and does each
    trigger name an owner? Costs rows 9, 10 and 11.
15. **Borrowing another company's set.** No page the research read states a reuse licence, and
    Productboard reserves its rights. A set written for another company may not pass your opposite test.
    Test: write the team's own words, then run the opposite test again. Costs rows 2 and 5.
16. **Presenting the library's positions as received practice.** A name and a statement appear in every
    published set read. What a principle rules out appears per principle only in a vendor's AI prompt
    among the sets and prompts tabulated, with Box's "Versus" a comparable field outside that table. A
    named cost appears in several forms, and an examples field in two sets (a case study at Monzo, a
    product example at Slack). The role names in Ownership and
    Changes, the dated change log and the table form of the Review Trigger are the library's. A filled
    set may keep them and should not describe them as a standard.

## Pairing with your process

This bundle ships in the `standing-standards` family as a **foundation**: a standard that a team's
product decisions are judged against. The reasoning is in
[ADR 0090 (product principles joins standing-standards as a foundation)](../../docs/internal/decisions/0090-product-principles-joins-standing-standards-as-a-foundation.md),
and the family's rules are in
[the standing-standards contract](../../docs/internal/contracts/standing-standards.md). Update the set when a
Review Trigger condition fires, not on a calendar. The stated intervals disagree: Guru says a set should
hold for at least a year, LogRocket says to review it every three months, Intercom says it updates every
one to two years, and ProductPlan says an update should be unusual. None cites a measurement. A team that
wants a review date may add one as a floor and should label it as its own choice.

## What the research did not settle

The companion's section 6 lists the open disputes: whether a set is standing or per project, whose set it
is, whether a principle should be memorable or arguable, whether to rank, how many, how often to revise,
and whether the set covers execution only or the choice of what to build. The research did not find who
first wrote about a team keeping its own product principles, who owns a set after it is written or who
approves a later change, any worked rule for two principles that conflict, or any measured effect of a set on decisions. It
found no tie to a delivery methodology, and it found no research on regulated products or a solo author.
The template is untested for both of the last two.

## When it is good enough

When a product manager who did not write the set can take the next real choice between two good options,
name the principle that decides it, say what that principle costs and rules out, and say which principle
wins if a second one pulls the other way. And when the page names who owns the set and what event reopens
it.

Then delete every HTML comment. Keep the `source_template` and `source_template_version` frontmatter
fields, because they are the only record of which template and version produced the document.
