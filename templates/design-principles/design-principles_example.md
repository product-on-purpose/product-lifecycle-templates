---
title: "Acme Analytics Design Principles"
doc_type: design-principles
size: lean
product_name: "Acme Analytics"
owner: "Marcus Webb (Design Lead, Reporting)"
status: active
doc_version: "1.1.0"
created: "2025-10-14"
updated: "2026-02-03"
related_links:
  - "../user-persona/user-persona_example.md (the Recurring Analyst persona, 2026-01-05; the evidence behind principles 1, 2 and 3)"
  - "../product-vision/product-vision_example.md (the product vision, 2026-01-14; holds where the product is heading, a decision this set does not settle)"
  - "../product-strategy/product-strategy_example.md (the FY26 product strategy, 2026-01-28; the change that fired the 2026-02-03 revision)"
source_template: design-principles
source_template_version: 0.1.0
---

> **Worked example.** A filled `design-principles`, the one size this bundle ships, for the same Acme
> Analytics product used throughout this library's examples. The `standing-standards` family contract
> weakens the chaining on purpose, because a standing standard belongs to a team rather than to a moment
> in a story, so this document sits beside the thread and not at one point on it. It is dated 2026-02-03,
> the day of the last line in its change log, and the body below cites only documents that existed by
> then: the [Recurring Analyst persona](../user-persona/user-persona_example.md) of 2026-01-05, the
> [product vision](../product-vision/product-vision_example.md) of 2026-01-14 and the
> [FY26 product strategy](../product-strategy/product-strategy_example.md) of 2026-01-28. It comes well
> before the [Saved Views design brief](../design-brief/design-brief_example.md) of 2026-06-01, whose
> design team would work under a set like this one. The sibling bundle `product-principles` settles what
> a team builds, funds or declines, and this document leaves that to it.
>
> Read it alongside [`design-principles_guide.md`](design-principles_guide.md), the rubric it was graded
> against. Three things are visible in it. A principle has been retired and archived with its reason, not
> deleted. One Review Trigger row has fired and points at its line in the change log. One conflict is
> resolved in a named kind of decision. Published sets carry the statement and, in three of the five
> tabulated, the reviewer's question. What it rules out appears only in a vendor's AI prompt
> (Productboard). What it rests on appears in no set read. A decision it settled has partial precedent
> in GitLab Pajamas' "Example in practice" and GOV.UK's linked case studies. The role names in Ownership
> and Changes and the table form of the Review Trigger are also this library's own position, not received
> practice. A set of three is not a target: the number is advice, and this team holds three
> because it could attach a real decision to each.
>
> All figures are illustrative. They are internally consistent with the other examples in this library
> and are not drawn from a real company. The persona's interview counts are repeated exactly, because
> both documents describe the same research.

# Acme Analytics Design Principles

## Purpose and Scope

**Product or service covered:** The dashboards and the report-authoring screens of the Acme Analytics
web application, and the emails and in-product notifications that the application sends about them. The
public marketing site is not covered.

**Who applies this set:** Marcus Webb's Reporting product design team applies it to every screen it
designs. The product managers who commission a change, and the Design Systems group that reviews
pattern proposals, also apply it, and the front-end engineers meet it only through those two.

**Relation to the design system:** The set is a separate file from the shared design system, which the
Design Systems group maintains for components and patterns. The two are joined at one point. The
design system's contribution form for a new or changed pattern has a required field that asks which
principle the proposal serves, and the answer must name one from this set. A statement that names a
component belongs in the design system, so none of the principles below does.

**Decisions this set does not settle:** Which problems Acme builds for and which it declines, which the
[FY26 product strategy](../product-strategy/product-strategy_example.md) holds. Where the product is
heading, which the [product vision](../product-vision/product-vision_example.md) holds. How a component
looks or behaves on its own, which the design system holds. Whether a number is correct: engineering
owns that, and these principles settle only how a screen presents a number that is already right.

**Principles that also settle what the team builds:** Principle 3, Say what to try next. Whether a
nearer alternative exists to offer is partly a decision about what the product does, which belongs to the
product team, and this set settles only that the screen says so. Principles 1 and 2 settle how a screen
presents a figure and a label, and neither decides what Acme builds.

## The Principles

**Principle 1: Say what a number covers**

- **Statement:** Wherever a screen shows a figure, the same screen says in words which records the
  figure counts, for which period and as of when. The reader should not have to open a control to find
  out.
- **What it rules out:** A headline figure whose scope lives only in filter controls that are collapsed,
  or in a hover tip. A chart titled with the measure alone, such as "On-time delivery", with no region
  and no week beside it. A glanceable wall display could reasonably choose the opposite, because nobody
  carries its number into a meeting. Acme's reader does.
- **The question a reviewer asks:** If someone read this figure aloud at a meeting, could a listener who
  never saw the filters say what it covers?
- **What it rests on:** The [Recurring Analyst persona](../user-persona/user-persona_example.md) of
  2026-01-05. It records that Elena Cho, a customer's regional operations manager, presented three hubs'
  on-time numbers in October 2025 where she meant four, and corrected herself in front of her VP. It also
  records how the miss comes about: the dashboard opens on the company-wide default, and she rebuilds the
  region, week and hub filters by hand each Monday from a personal spreadsheet. The persona does not
  record what the figure on her screen said about its scope. The design team's reading is that the figure
  itself should have told her which hubs it counted. That reading is a judgement, not a finding from the
  interviews.
- **A decision it settled:** At the design critique of 2025-11-25 the team decided how a headline tile
  should show its filters. It added a caption under each figure, which read, on sample data, "All four
  hubs, week of 3 November, as of 06:00 Monday". It turned down a small badge reading "3 filters
  applied", because the badge would have told the reader that filters existed without saying what they
  were.

**Principle 2: Use the word the reader uses**

- **Statement:** When the product names something that a person at an operating company already has a
  word for, the screen uses that word first. The system's own term appears only when the person asks to
  see it.
- **What it rules out:** A column or table name, such as "fct_shipments.delivered_flag", as the main
  label for what the person calls "delivered on time". A heading that explains a feature in the
  vocabulary of the data model. A query tool for developers could reasonably choose the opposite, because
  its reader wants the schema's names. Acme's reader has no query background.
- **The question a reviewer asks:** Would the person say this label out loud at their own weekly review,
  in these words?
- **What it rests on:** The same persona. It describes Elena Cho as having no dedicated analyst and no
  query background, and it says that a team hearing the word "analyst" builds for someone who can write
  a query, and that she cannot.
- **A decision it settled:** At the design critique of 2025-12-09 the team reviewed the labels in the
  filter panel. It labelled the region control "Region" and kept the table's column name available when
  the person asks for it. It turned down showing both names on every label, because that doubled the text
  a reader had to scan before reaching the control.

**Principle 3: Say what to try next**

- **Statement:** When the product cannot give a person what they asked for, the screen says in one
  sentence what it could not do, and offers the nearest thing it can do from that same screen.
- **What it rules out:** An empty chart with no words. A message that reads only "No results found" or
  quotes an error code. A dead end that sends the person to someone else before they can continue. A
  product sold to teams that keep an analyst on hand could reasonably choose the opposite and say "ask
  your analyst". Acme's reader has no dedicated analyst.
- **The question a reviewer asks:** If this screen cannot give the person what they came for, can they
  act on what it says without leaving the screen or asking anyone?
- **What it rests on:** The same persona's finding that when the dashboard cannot answer a question, the
  only path is to ask someone else, a data analyst, and wait. Eight of the twelve interviewees raised it, and the
  question often goes unasked. The interviews ran in November and December 2025.
- **A decision it settled:** At the design critique of 2026-02-03, where this principle was added, the
  team applied it to a chart whose filters match no records. It turned down the empty chart and the
  sentence "No results found". It chose a sentence saying that the filters matched no records, with the
  previous week offered as the next thing to look at. **This principle straddles a line.** Whether a
  nearer alternative exists to offer is partly a decision about what the product does, which belongs to
  the product team. This principle settles only that the screen has to say so.

## When Principles Conflict

| Principles in tension | Kind of decision | Which wins | Why |
|---|---|---|---|
| Use the word the reader uses, against Say what a number covers | The label of a figure whose everyday name differs from what the product counts, such as "on time" | Say what a number covers. The reader's word may stay as the heading, with the exact count written under it | A familiar word that hides a different count lets the reader repeat the figure with confidence in the wrong meaning. A longer and less familiar phrase costs a few seconds of reading |

## Using Them in Decisions

**Where the set is applied:** At the Reporting design team's critique, which runs every two weeks and
is the main place. In the Design Systems group's review of a pattern proposal, through the form field
named above. And whenever someone writes or edits the wording of an email or a notification the
product sends.

**How a decision cites a principle:** The pull request or design ticket that ships the change opens its
description with a line beginning "Principle:", naming the one that decided it. A second line beginning
"Weighed against:" appears only when another principle pulled the other way, and it gives the reason in
a sentence. An example: "Principle: Say what a number covers. Weighed against: Use the word the reader
uses, because the everyday word hid the count."

**When a decision sets a principle aside:** The designer who proposes the change states the reason at
the critique, and the room replies in one of two ways. Either the reason holds and the change goes
ahead, or the reason is a fair argument for a worse screen and the change goes back for another pass.
The ticket records which reply it was. A principle set aside twice in the same kind of decision goes to
Marcus Webb, who decides whether it needs a row in When Principles Conflict or a rewrite.

## Ownership and Changes

**Owner (role and person):** The Design Lead, Reporting: Marcus Webb.

**How anyone proposes a change:** By opening a ticket labelled "principles" in the design team's queue,
or by raising it at the critique. Anyone at Acme may do either.

**Who decides a change:** Marcus Webb decides. Dana Okoro, VP Product, approves any change that adds or
retires a principle, because that changes what every screen is judged against.

| Date | What changed | What fired it | Who decided |
|---|---|---|---|
| 2025-10-14 | First agreed, with three principles: Say what a number covers, Use the word the reader uses, and Keep the expert's hands fast. The When Principles Conflict row, which resolves Use the word the reader uses against Say what a number covers, was part of that first agreement | First agreed | Marcus Webb, approved by Dana Okoro |
| 2026-02-03 | Keep the expert's hands fast retired to the archive below, and Say what to try next added in its place. The rests-on fields of principles 1 and 2 now cite the Recurring Analyst persona of 2026-01-05, which did not exist when they were agreed. Their wording is unchanged | Review Trigger: the audience or the strategy changes. The FY26 product strategy of 2026-01-28 names the unaccompanied analyst, the person the persona calls the Recurring Analyst, as its target segment | Marcus Webb, approved by Dana Okoro |

**Archived principle: Keep the expert's hands fast.** Agreed on 2025-10-14 and retired on 2026-02-03.
Its statement read: when a person has already told the product exactly what they want, nothing stands
between them and the result, with no confirmation step, no walkthrough and no second screen. It ruled
out a confirmation dialog on a routine action and a tutorial overlay that blocks the page. It was
retired because it served the person who already knows what to ask, and the FY26 strategy names a
different person as its target, one for whom the missing knowledge is the obstacle and the extra step is
not. It stays here with its reason, so that a later change of strategy can bring it back knowingly, and
so that nobody proposes it again as though it were new.

Principles 2 and 3 rest on the persona's evidence rather than on a strategy choice. They would survive a
change of strategy for as long as the persona holds. What would retire them is evidence that the persona
no longer describes the reader, such as research showing that most of Acme's readers now keep an analyst
on hand or a query background. The set is reread when the target segment changes, which is what the
Review Trigger row below records.

## Review Trigger

| Condition | Owner | What They Do About It |
|---|---|---|
| A new cross-cutting concern with people behind it | Marcus Webb | Asks the people raising the concern which decisions they keep losing. Drafts a principle only if two options keep recurring in those decisions. Otherwise writes the concern and the date into the change log and leaves the set alone |
| An audit finds principles overlapping or forgotten | Marcus Webb | Asks each designer to list the principles from memory. A principle that two designers cannot recall, or that settles the same decisions as another, is put to the next critique, which rewrites it or retires it. Whichever happens is dated in the log with the reason, and a retired text moves under the log |
| A new product or surface joins the scope | Priya Nair (PM, Reporting) | Raises the new surface at its first critique, before a screen is designed. Marcus Webb then either names it in Purpose and Scope or writes down why the set does not cover it |
| A debate recurs and no principle settles it | Marcus Webb | When a trade-off comes up at a second critique, writes the choice that was made as a candidate row in When Principles Conflict, or as a candidate principle, and dates it in the change log |
| The audience or the strategy changes | Dana Okoro (VP Product) | Tells Marcus Webb when a strategy or a target segment changes. Marcus Webb then reads each principle against the new audience at the next critique and rewrites or retires any that favours a group no longer targeted. **This row has fired once, on 2026-02-03, and the change log above records it** |

No calendar date is a trigger. A date would only call for a read of the set on a day when nothing had
changed.
