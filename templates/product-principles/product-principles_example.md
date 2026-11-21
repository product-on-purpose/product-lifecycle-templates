---
title: "Acme Analytics Product Principles"
doc_type: product-principles
size: lean
product_name: "Acme Analytics"
owner: "Dana Okoro, VP Product"
status: active
doc_version: "1.0.0"
created: "2026-02-05"
updated: "2026-02-05"
related_links:
  - "../user-persona/user-persona_example.md (the Recurring Analyst persona, 2026-01-05; the evidence behind the cost of principle 1)"
  - "../product-vision/product-vision_example.md (the product vision, 2026-01-14; holds where the product is heading, a decision this set does not settle)"
  - "../product-strategy/product-strategy_example.md (the FY26 product strategy, 2026-01-28; the strategy row of the Review Trigger points at it)"
  - "../positioning-statement/positioning-statement_example.md (the positioning statement, 2026-01-30; holds how Acme stands against its alternatives)"
  - "../design-principles/design-principles_example.md (the design principles, revised 2026-02-03; settles how a screen behaves, which this set leaves to it)"
source_template: product-principles
source_template_version: 0.1.0
---

> **Worked example.** A filled `product-principles`, the one size this bundle ships, for the same Acme
> Analytics product used throughout this library's examples. The `standing-standards` family contract
> weakens the chaining on purpose, because a standing standard belongs to a team rather than to a moment
> in a story, so this document sits beside the thread and not at one point on it. It is dated 2026-02-05,
> the day the set was first agreed, and the body below cites only documents that existed by then: the
> [Recurring Analyst persona](../user-persona/user-persona_example.md) of 2026-01-05, the
> [product vision](../product-vision/product-vision_example.md) of 2026-01-14, the
> [FY26 product strategy](../product-strategy/product-strategy_example.md) of 2026-01-28, the
> [positioning statement](../positioning-statement/positioning-statement_example.md) of 2026-01-30 and the
> [design principles](../design-principles/design-principles_example.md) as revised on 2026-02-03. Dana
> Okoro, VP Product, owns the vision, the strategy, the positioning statement and this set, which is why
> they speak in one voice. It comes well before the
> [Saved Views design brief](../design-brief/design-brief_example.md) of 2026-06-01 and the
> [Saved Views PRD](../prd/prd_example.md) of 2026-06-12, the documents a team working under a set like
> this one would write. The sibling bundle `design-principles` settles how a screen, a message or an
> interaction behaves, and this document leaves that to it.
>
> Read it alongside [`product-principles_guide.md`](product-principles_guide.md), the rubric it was
> graded against. Three things are visible in it. Each principle names what it costs, who pays, and what
> it rules out, including a request someone has already made. The set is dated at its first agreement, so
> no principle has been merged or retired and no Review Trigger row has fired, and the change log says
> so instead of inventing a history. And one conflict is resolved in a named kind of decision. The
> decisions under "A decision it settled" all predate the set. They are the arguments the principles
> were drafted from, as the template's fill instructions advise, and none of them is yet a citation of
> the set.
>
> This document asks for more than published sets carry. Across the eight published sets the research
> tabulated, none has a field for what a principle rules out. The only dated record of a published set
> changing that the research found is Intercom's, which said in 2019 that it used to have five principles
> and had merged three of them into one. No source read names who owns a set after it is written, or who
> approves a later change, so the role names in Ownership and Changes, and the table form of the Review Trigger, are this library's
> own position and not received practice. No source measures whether keeping such a document improves
> decisions. The set is standing for the reason Cagan gives in *Inspired*, where principles are "not tied
> to any one product release", and no source ties a principle's life to a strategy period. A set of three
> is not a target: the number is advice, and this team holds three because it could attach a real
> argument to each.
>
> All figures are illustrative. They are internally consistent with the other examples in this library
> and are not drawn from a real company. The figures that come from the strategy, the vision and the
> persona (31 percent, 71 percent, four of six implementations, three of eleven pilot users) are repeated
> exactly, because the documents describe the same facts. Halden Foods and every other figure and date in
> the cases below are invented for this example.

# Acme Analytics Product Principles

## Purpose and Scope

**Product or products covered:** Acme Analytics: the web application, the integrations that feed it, and
the services work done for individual accounts on its behalf.

**Level of the set (company, product line or product) and who applies it:** Product level. Dana Okoro, VP
Product, and the product managers apply it to every decision about what to build, fund or decline. The
design lead, the engineering leads and the services team lead meet it when a decision reaches them. Sales
leadership meets it as the group that brings most of the asks it answers.

**Decisions this set settles, and decisions it does not:** It settles whether Acme builds something, in
what form for an account that asks, how widely it is released, and what the team gives up in exchange.
It treats an ask from a customer, a prospect, sales or services in the same way. It does not settle
which segments Acme targets or declines this year, which the FY26 strategy holds. Whether to turn down
one account's particular request is settled here. It does not settle where the
product is heading, which the vision holds, or how Acme describes itself against the spreadsheet and the
general-purpose BI tool, which the positioning statement holds. It does not settle how a screen, a message
or an interaction behaves, or what any single sprint contains.

**Relation to the product vision, the product strategy and the design principles, and whether the set outlasts the current strategy:** The
[vision](../product-vision/product-vision_example.md) says where Acme is going, and these principles say
how the team chooses along the way. One overlap is deliberate. Principle 2 names the general rule behind
a line in the vision's What This Rules Out, the bespoke warehouse integration for one large account, and
adds the cost the vision does not state. The
[FY26 strategy](../product-strategy/product-strategy_example.md) chooses a target and a guiding policy for
one year. No principle below restates that choice, and each is written so that it would still be arguable
if a later strategy chose a different target. The set outlives the strategy, and the strategy row of the
Review Trigger is where the two meet. The
[design principles](../design-principles/design-principles_example.md) belong to Marcus Webb, Design Lead,
Reporting, and decide how a screen behaves.

**Principles that also settle how a screen behaves:** None. Each of the three decides whether Acme
builds, funds, releases or retires something. Principle 1 decides how widely a feature is released,
principle 2 decides whether a request is built in a form every account can use, and principle 3 decides
whether a new surface is funded and which old one is retired. None of them says how a screen, a message
or an interaction reads for the person using it, and the design principles settle that. The
what-does-it-settle test was applied to each of the three, not skipped.

## The Principles

**Principle 1: Measured before widened**

- **Statement:** A feature that answers a question on the reader's behalf stays with a small group of
  accounts until we have measured how often readers correct its answers on their own questions, and what
  they do after a wrong one. A good score on our own test questions, a strong demonstration, or a request
  from a senior person does not shorten that wait.
- **Why we hold it:** Our one accuracy figure so far comes from the prototype, which resolved 71 percent of
  test questions to the right dataset. That figure describes questions we chose and not questions readers
  ask, and the [FY26 strategy](../product-strategy/product-strategy_example.md) records no measure of what
  happens after a wrong answer. The [vision](../product-vision/product-vision_example.md) names the risk
  as its first leap of faith: that someone who did not derive an answer will act on it. Three of eleven
  pilot users still take our answers to a colleague who knows the data, to check them. A wrong figure costs
  the person who presents it. The [persona](../user-persona/user-persona_example.md) records Elena Cho
  correcting a hub count in front of her VP. That miss came from her own filters. An automatic answer that
  was wrong would put her in the same room without a mistake of her own, which is our reasoning and not a
  finding from the interviews. A team that sells on first impressions could reasonably choose the
  opposite and widen on the strength of the demonstration. That choice is why this is a principle and not
  a truism.
- **The trade-off it accepts:** Readers in accounts outside the small group keep stalling at the dataset
  picker for as long as the measurement takes, and today only 31 percent of new accounts build a second
  view within 14 days. Sales shows a narrower product than it could. A rival that switches on automatic
  answers for everyone first will look ahead in a side-by-side comparison.
- **What it rules out:** Switching an answer-giving feature on for every trial account because it
  demonstrates well. Quoting the share of test questions answered correctly as though it were the share
  of readers' questions answered correctly. Matching a competitor's release date for its own sake.
  Widening the group before the correction rate has a number behind it. Acme's sales leadership has
  made the first of these requests.
- **A decision it settled:** On 2026-02-02 sales leadership asked for the question-first prototype to be
  switched on for every trial account before a customer event in March. Dana Okoro turned the request
  down and held to the plan in the FY26 strategy: 5 percent of new accounts in Q2, with the correction
  rate measured. Sales received a recorded walkthrough on sample data, labelled as sample data, to show
  at the event. The set did not yet exist on that day, so this is the argument the principle was drafted
  from.

**Principle 2: One product for every account**

- **Statement:** We build what one account asks for only in a form we would ship to every account. If a
  request can be met only for that one account, we decline it, even when the services team could deliver
  it in a week.
- **Why we hold it:** The services team reports that four of six recent implementations were near-identical.
  Our reading is that much of that per-account work was a default nobody had shipped, which is our
  reasoning and not a finding. Hours spent once per account do not compound, and the same hours spent on a default do. We do not know why the other two implementations
  were not near-identical, and the cost below falls on accounts like them. A company that grows through
  services and customisation could reasonably choose the opposite and turn the custom work into product
  later. We hold that the later rarely arrives while the next custom request is waiting.
- **The trade-off it accepts:** An account whose need is its own waits longer for a general version, pays
  a rival, or leaves. Accounts like the two implementations that were not near-identical are the likeliest
  to. Sales and services lose the one-week fix that closes a quarter, and the services team lead bears
  that loss first.
- **What it rules out:** A fork or a feature flag built for one account and never meant to reach the
  others. A bespoke integration, or an export in one customer's own layout. Custom modelling for one
  account that does not become a default. A request has already been made for the third of these in a
  small form: in January 2026 a food distributor's team asked services to rebuild its reports on a week
  that starts on Sunday, for that account alone.
- **A decision it settled:** On 2026-01-12 Halden Foods, a mid-market food distributor, asked services to
  rebuild its reports on a Sunday-to-Saturday week. Services could have done it for that account in
  about a week. The team declined that form and built a week-start setting that any account can choose,
  which shipped on 2026-02-02, three weeks later. Halden's team kept a manual Sunday-week count in the
  meantime. The set did not yet exist, so this is the argument the principle was drafted from.

**Principle 3: Retire before we add**

- **Statement:** A new report type, screen or integration is funded only when its proposal names the one
  readers use least and says whether that one will be retired, merged or kept, and why.
- **Why we hold it:** Every surface costs the team that keeps it working, the designers who review it, and
  the reader who has to choose between it and the one beside it. A January 2026 usage count found that 9
  of the 24 report types were opened by fewer than 3 percent of weekly accounts in the last quarter, and
  nobody had been asked to decide what to do about them. Readers who already stall at one choice are not
  helped by a second place to make it, which is our reasoning and not a finding. A growth-stage company
  could reasonably choose the opposite, adding what wins deals and pruning once usage is clear. We hold
  that the pruning does not happen once the addition has shipped.
- **The trade-off it accepts:** Retiring a surface upsets the few accounts that still use it, and the
  work takes weeks that could have built something new. A good new idea waits when nothing can be retired
  without harm, and the product manager who proposed it bears that wait.
- **What it rules out:** A new report type or integration added for one prospect's evaluation with nothing
  retired. A surface kept "because someone might use it", with no account named. A quarter's plan made
  of additions only. The sales leadership of Acme has made the first of these requests.
- **A decision it settled:** On 2026-01-26 sales leadership asked for a new executive-summary report type
  to show a prospect's VP. The proposal had to name something to retire. The least-used report type, opened
  by 2 percent of weekly accounts, was still used every week by one named account, so retiring it needed a
  conversation first. That account agreed on 2026-01-30 to move to the weekly summary, with the old type
  to be retired at the end of April. The executive summary was funded on 2026-02-03. The set did not yet
  exist, so this is the argument the principle was drafted from.

## When Principles Conflict

| Principles in tension | Kind of decision | Which wins | Why |
|---|---|---|---|
| Measured before widened, against Retire before we add | A new path that replaces an existing one while the new path is still with a small group of accounts | Measured before widened | The proposal still names the old path and a date for retiring it, as principle 3 asks. The old path goes only after the new one has reached every account and its correction rate is measured, because retiring it sooner would leave every account outside the small group with no path at all |

The other two pairs have no row yet, because no decision the team has argued has set them against each
other. The one row above resolves the pair most likely to collide, in a kind of decision the team can
foresee. It is written ahead of an argued case and is not a record of one.

## Using Them in Decisions

**Where the set is applied:** In three places. The first is the Thursday customer-ask review, a
thirty-minute meeting where sales, services and the product managers go through every new ask from a
customer or prospect and decide to accept it, decline it, or accept it in another form. The second is the
Reporting squad's sprint planning, when Priya Nair orders the backlog and the form of an item is in
question. The third is the quarterly capacity discussion, where Dana Okoro and the product managers agree
which new surfaces are funded and which existing ones are retired.

**How a decision cites a principle:** The answer to an ask is recorded in the ask tracker, in a field
headed "Because". It names the principle by number and name and says in one sentence how it applied, for
example "Principle 2, One product for every account: the week-start setting is general, and the rebuild
for one account is not." When the answer is yes in another form, the field states the form. When a
principle is set aside, the product manager writes "Exception to principle N" with the reason. Dana Okoro
accepts the exception or sends it back, and the tracker keeps both.

**How a new joiner meets the set:** A product manager joining the team reads the set during the first
week and then sits in on the next two Thursday reviews. Before the second review, the new joiner writes
the "Because" line for one ask. Dana Okoro or Priya Nair compares it with the line the room settled on,
and the two of them talk through any difference.

## Ownership and Changes

**Owner (role and person):** VP Product: Dana Okoro.

**How anyone proposes a change:** By writing to Dana Okoro with the decision the set got wrong or did not
cover, or by raising it at a Thursday customer-ask review. Any employee may do either.

**Who decides a change:** Dana Okoro decides. Before any change to a principle that has a design
neighbour, she consults Marcus Webb, Design Lead, Reporting, so that this set and the design principles
do not claim the same decision.

| Date | What changed | What fired it | Who decided |
|---|---|---|---|
| 2026-02-05 | First agreed, with three principles: Measured before widened, One product for every account, and Retire before we add. One When Principles Conflict row was part of that first agreement | First agreed | Dana Okoro |

No principle has been merged or retired, so nothing is archived yet. When one is, its text moves under
this log with the reason it went, so that nobody proposes it again as though it were new. The first
retirement or merge will also be the first row that shows a Review Trigger row firing.

## Review Trigger

| Condition | Owner | What They Do About It |
|---|---|---|
| The strategy changes significantly | VP Product: Dana Okoro | Counts a strategy change as significant when its target segment or its guiding policy changes. A new action list or a new metric target alone does not count. Asks of each principle whether its cost now falls on someone the new strategy targets. A principle that fails that question goes to the next Thursday review for a rewrite or a retirement, and the outcome is dated in the log. The FY26 strategy's own review on 15 October 2026 is its scheduled backstop, so a significant change cannot go unread past that date, and Dana reads the set alongside it. An earlier trigger in the strategy's own Review Trigger could fire this row sooner |
| A principle is consistently violated without a decision to change it | PM, Reporting: Priya Nair | Tags in the ask tracker any shipped change that contradicts a principle with no recorded exception. Two tags against the same principle in one quarter go to Dana Okoro. Two is this team's own threshold, chosen for a team this size and not drawn from a source |
| A new principle would have settled repeated debates | VP Product: Dana Okoro | When the same trade-off returns a second time with the same two options and no principle names the winner, asks the two people on either side to write, in two sentences each, what they would have decided and why. If both answers are reasonable and they differ, drafts a statement and a cost and puts it to the next Thursday review |
| A valid exception recurs | PM, Reporting: Priya Nair | Counts an exception as valid when Dana Okoro accepted its reason. When the same kind of exception is accepted a second time, brings both to Dana, who either rewrites the principle to take that case in or writes down why it stays an exception. Principle 2 is the likeliest to meet this row, because two of six recent implementations were not near-identical and nobody knows why |
| A principle does not take hold | VP Product: Dana Okoro | Reads the "Because" fields at the end of each quarter. A principle cited in none of them, though asks that fit it were received, is read aloud at the next Thursday review by someone who did not write it. If nobody can say which asks it settles, it goes for a rewrite or a retirement |

None of these rows has fired as of 2026-02-05. A competitor's release is not a trigger, as it is not a
trigger for the strategy, and principle 1 exists partly so that the team can withstand one. Dana Okoro has
chosen to add no review date of her own.
