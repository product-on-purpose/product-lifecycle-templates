# Lean UX Canvas: the guide

An operator card. Read it before a first pass and again every time the team loops back through it.
The reasoning behind every rule here lives in
[`lean-ux-canvas_companion.md`](lean-ux-canvas_companion.md).

## When to use this document

Open a canvas when an initiative is about to start and nobody has yet written down the business
problem, the outcomes, the users, or a candidate solution for it. Gothelf's own walkthrough starts
here, before any other box is touched, and the book calls the canvas "a great way to start an
initiative," filled by the whole team with stakeholders and clients joining "as much as possible."
A first pass rarely takes less than half a day, and some teams spread it across a series of
meetings over a couple of weeks; either is normal, and the spread reflects the initiative's own
scope, not disagreement about the method.

Treat the canvas as a facilitation tool first. Its originators call it exactly that, "a
facilitation tool for cross-functional teams designed to create a customer-centric conversation,"
and the filled page is the record of that conversation, not the thing of value on its own. If no
cross-functional conversation is happening, a page of boxes filled in alone by one person has not
done this document's job, whatever it says.

## Is this the right document at all?

| If the real question is | Write this instead |
|---|---|
| Which problem is worth solving, before anyone names a solution? | [`problem-statement`](../problem-statement/) |
| We have chosen one concept; who will design it? | [`design-brief`](../design-brief/) |
| We need to plan one test of one hypothesis, with variants, allocation, and a decision rule | [`experiment-design-doc`](../experiment-design-doc/) |
| Where is the whole product going, over years? | [`product-vision`](../product-vision/) |
| Who exactly are we building for, researched rather than guessed? | [`user-persona`](../user-persona/) |
| What does the whole business look like: channels, revenue, cost structure? | [`lean-canvas`](../lean-canvas/), Ash Maurya's Lean Canvas; this canvas asks nothing about revenue or cost *(2026-10-30: this cell said the bundle was planned and not yet built; it is built now)* |

## When NOT to use this document

- **The problem is already chosen and so is the concept.** A canvas names candidate solutions in
  Box 5 and turns them into hypotheses in Box 6; it has not chosen one. Once a concept is chosen,
  hand it to the people who will design it in a design brief instead.
- **The team already knows exactly which test it is running.** Box 8 only sketches the shape of a
  test: the smallest thing that would learn whether the riskiest assumption holds. It does not plan
  one, with variants, an allocation, metrics, and a decision rule. If the team already knows those,
  it needs an experiment-design-doc, not another pass of this canvas.
- **Nobody from outside the writer will read or discuss it.** The canvas earns its name as "a
  facilitation tool," and its own book lists communicating the work "broadly beyond the team" among
  what a filled canvas is for. A canvas written and filed by one person, with no conversation and no
  wider reader, has skipped the half of its job a document alone cannot do.
- **The initiative is actually the whole product's direction for years, not one initiative for
  weeks.** That scale is a product vision's job.

## Picking a variant

There is nothing to pick. This bundle ships one size, `lean`, with no full variant: Gothelf
publishes the canvas as a single one-page shape in both the 2019 and 2024 versions, and this
research found no source that splits a short form of the canvas from a longer one. Do not invent a
full-size version by adding sections the originators never wrote; a team that needs more structure
than the canvas itself offers is better served by `experiment-design-doc` once Box 8's smallest
experiment becomes a real test, or by `design-brief` once the team has chosen a concept, than by an
invented longer canvas. See the companion's Variants and sizing section.

## The rubric

Below 12 out of 18, the canvas reads as filled-in homework rather than the record of a conversation.
A reader cannot tell what the team actually believes about any box, and the facilitator ends up
walking every reader through it live instead of letting the page carry the conversation on its own.

Each row's test is the same: could someone satisfy this cell without actually improving the box?
If a cell can be cleared by adding words rather than evidence, it is written wrong, and no row here
is scored by counting items.

| # | Criterion | 0 | 1 | 2 |
|---|---|---|---|---|
| 1 | **Problem, not a solution** | The box names a feature or a solution, or no evidence is given for what changed | A problem is named, but you cannot point to the evidence behind it, or it never closes on a how-might-we question | You can point at the sentence naming what changed, the evidence that it is real, and the closing how-might-we question |
| 2 | **Outcome is a behavior** | A revenue figure, an output count, or a feeling, with no stated magnitude | A behavior is named, but with no stated magnitude or timeframe, or it reads as a feeling rather than a measured change | You can state who does what, by how much, and by when, as a measured behavior change, not a number on a report or a feeling |
| 3 | **Users named specifically** | Only "users" or a single buyer is named | A group is named, but a stranger to the project could not picture a member of it, or only the buyer appears | You can name a group a stranger could picture, and it includes anyone who configures the product or is affected by it beyond the buyer |
| 4 | **A distinct user outcome** | The user outcome restates the business outcome's measured behavior in different words | A user's own reason is attempted, but it still reads as a measurable, business-shaped target | You can point to a reason stated in the user's own language, distinct from Box 2's measured behavior, even if it is not itself measurable |
| 5 | **Genuinely different candidates** | A single solution appears, with no non-technical option | Several candidates appear, but they are variations of one software feature | You can point to candidates that take different approaches to the problem, one of them a non-technical option that is not a thinner version of a software one |
| 6 | **One feature per hypothesis** | A row spans more than one feature, or a slot (outcome, user, benefit, feature) is missing | One hypothesis per row, but a slot is vague enough that you could not design a test from it alone | Each row names the business outcome, the user, the benefit, and exactly one feature, specific enough to test on its own |
| 7 | **One named riskiest assumption** | A list of risks appears, with no single one chosen | An assumption is implied, but several are named with no stated priority among them | You can point to one named assumption, and the sentence states it as the one most important to learn right now |
| 8 | **Learning, not a release** | The box describes building a smaller version of the eventual product | An activity is named, but you cannot tell whether it tests the named assumption or only previews the feature | You can point to a specific test that would prove or disprove the named assumption, with no feature actually built |
| 9 | **Dated revision outcomes** | No dated row exists, or a row states only that something was "tested," with no outcome | A dated row exists, but you cannot tell whether the assumption held or which boxes changed as a result | You can point to a dated row naming the assumption tested, whether it held, and which boxes changed; once the canvas stops changing, a successor document is named |

## Anti-patterns

**Starting from a solution rather than a problem.** Box 1 asks what changed in the world, not what
to build. A community pitfalls list puts this first among six recurring failures, and the canvas's
own structure makes it visible immediately: nothing in Box 1 should read like Box 5.

**Writing a vague business outcome.** A revenue figure, an output count, or a sentiment in Box 2
fails Gothelf's own test that an outcome is a measured change in human behavior. A vague outcome in
Box 2 also breaks Box 6, since the hypotheses table pulls its business-outcome slot straight from
this box.

**Naming a user segment too broadly to act on.** "Users" or "fleet managers" cannot be pictured by
a stranger to the project, and Gothelf tightened Box 3's wording in 2019 specifically because teams
were taking this shortcut. Naming only the buyer and skipping everyone who configures or is
affected by the product is the same failure in a different shape.

**Confusing the business outcomes box with the user outcomes box.** This is the canvas's
best-documented point of confusion: Gothelf names it directly, and an independent podcast discussion
of the same revision reports that Box 4 was the part of the canvas with the most confusion.
Business outcomes are measured behavior; user outcomes are why users seek the product out in the
first place, and they are often not measurable at all. Writing one box's content into the other is
the confusion Gothelf rewrote Box 4 to remove, and a community pitfalls list names it as one of its
six recurring failures.

**Filling the solutions box with only one idea.** Box 5 was explicitly widened in 2019 to admit new
systems, business models, and non-technical solutions, not only software features. A single idea
here undercuts that widening before the team ever reaches Box 6.

**Bundling more than one feature into a single hypothesis.** The canvas's own rule is one feature
per hypothesis; a sentence spanning several features cannot be tested cleanly, because a result
would not say which feature caused it.

**Skipping the experiment step entirely.** A canvas that reaches Box 6 and stops, with no riskiest
assumption named in Box 7 and no smallest test designed in Box 8, has stopped short of the reason
the canvas exists: to find out whether the hypotheses are true before anyone commits to building.

**Leaving the revisions section blank because a first pass feels finished.** The canvas is revised
while its experiments run: after Box 8 returns a result, the team asks Box 7's question again, and
evidence can even send the team back to Box 1. A canvas revised with no record of what changed
cannot show what the team actually learned, which is exactly why this section exists.

## Before you share it

Self-grade against the rubric above, then delete every HTML comment; they are guidance, not
content. Remember that a canvas is not finished when you first fill it. It stays open while the
initiative's experiments run, and it is finished only when the team commits to building, changes
course, or stops the initiative, at which point the final row of the revisions section should name
what takes over.
