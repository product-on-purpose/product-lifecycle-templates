---
title: "{{product_name}} Product Roadmap"
product: "{{product_name}}"
owner: "{{who_owns_this_roadmap}}"
horizon: "{{period_this_covers}}"
audience: "{{internal_or_customer_facing}}"
status: "{{draft_or_agreed}}"
last_updated: "{{date}}"
doc_type: product-roadmap
size: full
format: go
source_template: product-roadmap
source_template_version: 0.1.0
---

<!--
PRODUCT ROADMAP, GO FORMAT (goal-oriented). A different organising principle from now-next-later, not a
different size of it.

WHEN TO REACH FOR THIS INSTEAD OF NOW-NEXT-LATER. The now-next-later format sorts by confidence and refuses
to say when. This one sorts by RELEASE and attaches a measurable goal to each. Reach for it when releases are
real events in your world (shipped versions, regulated milestones, hardware gates) and each one needs to
answer "what is this release for, and how will we know it worked?". If your releases are continuous and
nobody can name the next one, use now-next-later instead.

WHERE THIS SHAPE COMES FROM. It is Roman Pichler's GO Product Roadmap, and its five fields are his: DATE,
NAME, GOAL, FEATURES, METRICS. This bundle ships it because it is structurally distinct from the other two
and is published with a named source, which is the bar this library sets before adding a format. ONE SECTION
IS THIS BUNDLE'S ADDITION and is not in the published format: "What Is Not On Here". It is added because a
goal grid can otherwise fill every row without ever recording a refusal.

DATES HERE ARE NOT THE SAME AS DATES ON A GANTT CHART. The author's own position is that dates "are neither
good nor bad per se... it depends on how you use them and the context you are in", and his guidance is to use
them on internal roadmaps while keeping external ones coarse. The discriminator that survives is that a
project plan details how work gets done, while a roadmap communicates why it is worth doing.

THE FEATURES COLUMN IS THE TRAP IN THIS FORMAT. It exists in the published original, and it is also the
column that turns a roadmap into a feature list if you let it. Keep it to the smallest set that could
plausibly meet the goal, and treat it as an illustration of the goal rather than a commitment. The author's
own checklist is explicit: "Do not state any product details such as user stories."

WHAT THE EVIDENCE ACTUALLY SAYS. No study links any roadmap format to outcomes. See
product-roadmap_companion.md section 1.

HOW TO FILL THIS IN
1. Read the comment under each heading: WHAT, WHY (with a companion pointer), ASK, GOOD, WEAK, TRAP.
2. Replace each {{placeholder}} with your content.
3. Fill GOAL before FEATURES for every row. A row whose features were chosen first has no goal, it has a
   justification.
4. If a section does not apply, write "N/A" and one line of why.
5. Before you share it: self-grade against product-roadmap_guide.md, then DELETE every HTML comment.
-->

# {{product_name}} Product Roadmap

## The Strategy This Serves

<!-- WHAT  The strategy or goal this roadmap implements, named and linked. Two or three sentences.
     WHY   A goal-oriented roadmap is only as good as the goals, and goals arrive from somewhere. Published
           guidance puts the strategy above both the roadmap and the OKRs: the roadmap "takes the strategy
           as input and states how it will be implemented". Without naming that input, the goals below are
           just this team's opinions with dates attached. Deep dive: product-roadmap_companion.md section 3
           (The Outcome This Serves) and section 8.
     ASK   Which document decided this? Would its author recognise these goals as serving it? What in the
           strategy would we point at to refuse a proposed release goal?
     GOOD  "Implements the FY26 dispatch strategy: get urgency out of free-text notes and into the
           schedule. Each release goal below is a step in that, and the metrics are the strategy's own
           leading indicator."
     WEAK  "Supports company objectives and customer needs." (names no document and excludes nothing)
     TRAP  Writing the strategy here because none exists. If you find yourself inventing it, stop and write
           a product strategy first; a roadmap is not the place to decide direction. -->

{{the_strategy_this_serves}}

## Release Goals

<!-- WHAT  One row per release. DATE (or time frame), NAME, GOAL, FEATURES, METRICS. Three to six rows.
     WHY   The five fields are the published format, and the ordering is the argument: the goal is the
           reason the release exists, the features are what might achieve it, and the metrics decide
           whether it did. A row with features and no metric cannot be evaluated, and a row with a metric
           and no goal is a measurement in search of a purpose. Deep dive:
           product-roadmap_companion.md section 3 (Release Goals).
     ASK   Could we tell, three months after this release, whether it worked? Are the features the smallest
           set that could meet the goal, or everything we hope to ship? Is the date a forecast or a
           commitment, and does the reader know which?
     PRIORITY  Order rows by date. The nearest release should be the most specific; later rows should get
           visibly coarser, both in features and in the precision of the date.
     ROW HINT  GOOD row: "Q2 2026 | Signal | Dispatchers stop reading notes to find emergencies |
               urgency inference at intake; inferred priority shown beside the dispatcher's own |
               override rate below 30 percent, from a 48 percent baseline"
               WEAK row: "Q2 2026 | v2.4 | Improve dispatch | notes parsing, UI refresh, API v2 |
               increased engagement" (the goal restates the release name, the features are a shipping
               list, and the metric could not come back negative)
     GOOD  A table of three to six rows, nearest first, where every row's metric would let a stranger
           decide whether the goal was met.
     WEAK  A table where every row's goal is the name of the release, or where the metrics column is empty
           for anything beyond the first row.
     TRAP  Filling the features column first. Features chosen before a goal will always look like they
           serve it, because the goal gets written to fit them. -->

| Date | Name | Goal | Features | Metrics |
|---|---|---|---|---|
| {{date_1}} | {{name_1}} | {{goal_1}} | {{features_1}} | {{metrics_1}} |
| {{date_2}} | {{name_2}} | {{goal_2}} | {{features_2}} | {{metrics_2}} |
| {{date_3}} | {{name_3}} | {{goal_3}} | {{features_3}} | {{metrics_3}} |

## What Is Not On Here

<!-- WHAT  Things asked for, considered, and deliberately excluded from every release above, with one line
           each on why. Two to five.
     WHY   THIS SECTION IS THIS BUNDLE'S ADDITION to the published format, and the reason is that a goal
           grid fills up without ever recording a refusal: every row says yes to something and no row says
           no to anything. A roadmap that cannot be cited to decline a request settles no arguments. Deep
           dive: product-roadmap_companion.md section 3 (What Is Not On Here) and section 7.
     ASK   What has been asked for repeatedly that no release goal covers? Who will notice its absence?
           Has anyone told them, or are they going to find out by reading this?
     GOOD  "Customer-facing arrival windows. The most requested item we have; it depends on scheduling
           accuracy we do not yet have. Revisit when the override rate is under 20 percent. Sales knows."
     WEAK  "Anything not aligned to the strategy." (refuses nothing anyone actually asked for)
     TRAP  Leaving this empty because the table above is already full. A full table is not a refusal; it
           is a queue. -->

{{what_is_not_on_here}}
