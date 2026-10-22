---
title: "Acme Analytics North Star Metric"
product: "Acme Analytics"
owner: "Dana Okoro, VP Product"
status: "agreed"
last_updated: "2026-02-04"
doc_type: north-star-metrics
size: full
source_template: north-star-metrics
source_template_version: 0.1.0
---

> **Worked example.** A filled `north-star-metrics`, full variant, for the same Acme Analytics product used
> throughout this library's examples. Per [ADR 0070](../../docs/internal/decisions/0070-north-star-metrics-joins-strategy-docs-as-a-fifth-member.md),
> this type sits third in the `strategy-docs` chain: it is dated 2026-02-04, one week after the
> [FY26 product strategy](../product-strategy/product-strategy_example.md) (2026-01-28) it measures, and it
> will sit just ahead of the product roadmap still to come. Dana Okoro, VP Product, owns the vision, the
> strategy, this document, and the roadmap that follows it, which is why the four speak in one voice. Nothing
> below carries a formula, a data source, a refresh schedule, a target, or a threshold; those belong to a KPI
> dashboard, not to this document. *(2026-10-20: since [ADR 0076](../../docs/internal/decisions/0076-positioning-statement-joins-strategy-docs-as-a-sixth-member.md) placed the positioning statement third, this type sits fourth in the chain. Nothing else here changes.)*
>
> All figures are illustrative. They are internally consistent with the other examples in this library and
> are not drawn from a real company. Any figure this document shares with an earlier example, the 31 percent
> baseline and the second-view measure above all, repeats that example's own number exactly.

# Acme Analytics North Star Metric

## The North Star

Our North Star is **Weekly Self-Served Outcomes**: the count, across every active Acme Analytics account, of
a working session in which someone outside the analytics team opens a report, gets an answer to the question
that made them open it, and acts on that answer in the same session, by exporting it, sharing it, annotating
it, or running a follow-on query, without asking Dev or the analytics team first. Counted weekly, across the
whole account base, not only new accounts. The exact event definitions, the data source, and the weekly
target this North Star is held to live on the dashboard our data team maintains, not here.

- Product this North Star belongs to, if your company has more than one: This North Star covers
  Acme Analytics only, not the rest of Acme's portfolio.

## Why This Metric

- The customer value case: The [2026-01-14 product vision](../product-vision/product-vision_example.md)
  defines the value we are trying to create as the end of the waiting period between noticing something and
  understanding it, stated as someone who "can answer a question about their own operations in the time it
  takes to ask it out loud." A view someone opens and never acts on has not closed that gap; this count only
  moves when the gap actually closes, in the same session the question was asked.
- Why it leads rather than lags revenue: It measures behavior inside the product this week, not a renewal
  decision that lands months later. An account can produce a self-served outcome today whether or not it
  renews next year, which is exactly why it has to move before self-serve net revenue retention does, not
  after.
- Why it is not a vanity metric: It is a count of actions, not of accounts logged in or pages viewed, and it
  can fall. An account that stops acting on what it sees, even while it keeps opening reports, produces fewer
  outcomes, not more; a metric built from raw usage would keep climbing through exactly that failure.
- What shows it predicts retention or revenue in your own data, or how you will find out: Not yet validated.
  We have not run this count against a real account's renewal outcome, because the count itself does not
  exist in production yet. Once the Reporting team's event instrumentation ships in Q2, Priya Nair's team
  will pull the first cohort of accounts with two full quarters of this count against their Q4 renewal
  decision and report whether the two move together.

## Input Metrics

| Input Metric | Owning Team | Why It Drives the North Star |
|---|---|---|
| Share of new accounts that build a second view within 14 days of signup, from a 31 percent baseline in Q4 FY25 | Reporting team (Priya Nair) | Already the number every team watches weekly on the shared dashboard, and the strategy's own leading indicator, so near-term planning ladders to this number before it ladders to anything else; an account that never builds a second view has no second surface from which a self-served outcome could ever occur, and the North Star above shows whether that first activation turns into repeated value or stops there |
| Per-vertical modelling-default coverage: share of new accounts whose first view is built from a shipped default rather than a blank canvas | Platform team | Question-first entry can only resolve a question to something real if a modelled default already exists for that account's vertical; an account with no default behind it has nothing to answer against |
| Question-first resolution rate: share of question-first queries that resolve to the right dataset and join without the user correcting them | Platform team | A query that resolves wrong produces a correction, not an answer, so it cannot become an outcome someone acts on in that same session |

## What It Serves

- The product strategy this metric measures: The FY26 strategy to make the product usable without data
  expertise, "rather than making expertise easier to acquire." Every one of its four coherent actions, the
  question-first entry point, the shipped modelling defaults, instrumenting the second view, and moving
  services capacity toward defaults, is aimed at producing more sessions where a non-expert gets and uses an
  answer, which is what this North Star counts.
- The product vision that strategy serves: The 2029 vision of ending the wait between noticing something and
  understanding it, and of "Removing the analytics team as a bottleneck" on every other product decision. A
  self-served outcome is that vision happening once, in one session, for one person.
- The business outcome it is expected to predict, and how it differs from that outcome: It is expected to
  predict both of the strategy's lagging measures, the FY26 "Time to Insight" company goal and self-serve net
  revenue retention. It differs from both: it is a weekly count of sessions, not a median time and not a
  renewal percentage, and it is designed to move before either of them does, not to restate either one in a
  different unit.

## When We Revisit It

- The signal that would bring you back to this definition, not a date: Two signals. First, the 2026-01-14
  vision already names a leap of faith we are watching in the pilot: three of eleven pilot users still take
  our answers to Dev to check them before acting. If that share does not fall as familiarity with the product
  grows, the sessions this count calls "self-served" are not what the vision means by the word, and the
  definition needs to change, not just the number. Second, if Acme starts selling to a buyer who is required
  to route a decision through a data team for compliance reasons, acting without that team stops being
  possible for that account regardless of how the product works, and the definition would need to say so
  rather than silently undercount them.
- Who is responsible for noticing that signal: Dana Okoro, VP Product.

## Candidates Considered

| Candidate Metric | Why It Was Rejected |
|---|---|
| The FY26 "Time to Insight" company goal | The strategy already calls this a lagging measure. A number that only tells you what happened after the fact cannot also be the number that predicts it. |
| Share of new accounts that build a second view within 14 days | Kept, but as Input 1, not as the North Star. It counts new accounts only, inside their first 14 days, so it goes silent for every account that passed day 14 months ago; it cannot show whether an account that activated last spring is still getting value every week. |
| Self-serve net revenue retention | A revenue number one layer removed from the product. It moves on a renewal cycle, not weekly, and a renewal can rise or fall for reasons that have nothing to do with whether this week's questions got answered. |

## Guardrails

| Guardrail Metric | What Decline Would Mean |
|---|---|
| Share of self-served outcomes that get taken to Dev afterward to double-check | If this climbs even as the North Star climbs, the sessions we are counting are not evidence of trust in the answer; the 2026-01-14 vision names exactly this failure as building "a faster way to create work for" the team we were trying to remove as a bottleneck. |
| Services-ticket requests to build or verify a view, filed by an account in the same week it produced a self-served outcome | If this rises alongside the North Star, some share of the outcomes we are counting were actually delivered by a person behind the scenes, not by the product acting self-served at all. |

## What It Does Not Tell Us

- What this metric cannot show on its own: Whether the question acted on mattered. A user who exports a chart
  confirming something they already half-knew counts exactly the same as a user who caught a real problem
  before it cost the business anything. A single account can also sit flat for a whole week without that
  meaning anything is wrong; a healthy account can go a week with no new question worth acting on, and one
  quiet week is not a signal the input metrics above do not already explain.
- How it could be gamed, and what that would look like: A team under pressure to move the number could
  encourage exporting or annotating as a habit regardless of whether a decision actually followed, which
  would look like this count rising while the services-ticket guardrail above also rises, because the
  "self-served" action was decorative rather than load-bearing.

## Definition History

| Date | Previous Definition | New Definition | Why It Changed |
|---|---|---|---|
| 2026-02-04 | N/A, first definition | Weekly Self-Served Outcomes, as defined above | First definition. Recorded here, with today's date, so that any future change to this metric has to add a row rather than quietly rewriting this one. |
