# Lean Canvas: the guide

An operator card. Read it before you sketch the canvas, and again before you share it with the first
other person. The reasoning behind every rule here lives in
[`lean-canvas_companion.md`](lean-canvas_companion.md).

## When to use this document

Sketch a Lean Canvas when the business model behind a product is still a set of beliefs rather than a
settled fact: who has the problem, who will pay, how the product reaches them, how it makes money, and
what would have to be true for it to win. Ash Maurya built the canvas to "deconstruct an idea into key
assumptions or beliefs", and every box exists to state one of those beliefs in a form that can be tested,
not to describe a plan that has already been decided. Write the first sketch alone, even if you work on
a team: "If you're part of a team, avoid creating a Lean Canvas as a group exercise. Instead, have each
team member create their snapshot first." Keep it fast: "your initial big idea canvas should be sketched
quickly - in less than 20 minutes", on one page, with "Set a timer for 20 minutes" as a literal
instruction rather than a figure of speech. Share the finished sketch at once: "The important thing is
sharing it with at least one other person when you are done."

Maurya's own company draws the line for when this document applies by stage, not by company size or
age: "If you are pre-product-market fit, start with Lean Canvas". This library places the canvas second
in its `strategy-docs` chain, between the product vision and the product strategy, and names that
placement its own position rather than a sourced finding: no source compares the two sequences by name.
What the placement does not change is what the canvas is for: it exists so a later product strategy has
beliefs to commit to or reject, not the other way around. See `lean-canvas_companion.md` section 6
(Debates) and section 8 (Relationships) before treating the order as settled either way.

## Is this the right document at all?

| If the real question is | Write this instead |
|---|---|
| Where are we trying to get to, over years, and why is it worth it? | `product-vision` |
| Which problems will we solve to get there, and which will we not? | `product-strategy` |
| How do we stand against one named alternative, for one customer, now? | `positioning-statement` |
| Which single measure of customer value shows the strategy is working? | `north-star-metrics` |
| Does this one investment decision justify the spend? | `business-case` |
| What does this one customer type actually look like, researched in depth? | `user-persona` |
| What are the hypotheses behind one initiative, not the whole business? | `lean-ux-canvas` |
| Already past product-market fit, and want the tool built for an established business model? | the Business Model Canvas, catalog entry 4, not yet built in this library |

## When NOT to use this document

- **The business already has product-market fit.** Maurya's company states the test directly:
  "the better tool for mapping and communicating established business models" is the Business Model
  Canvas, not this one, and "If you are pre-product-market fit, start with Lean Canvas" names the
  opposite case as this document's own ground. That same source also softens the line,
  "Use what is most natural for you", so treat the stage test as the sourced default, not an absolute
  rule.
- **A team is about to use it as a group whiteboard exercise for a first draft.** The current teaching
  page names this directly as the wrong way to start: "If you're part of a team, avoid creating a Lean
  Canvas as a group exercise. Instead, have each team member create their snapshot first." Reconciling
  individual snapshots afterward is the method; drafting by committee from a blank page is not.
- **The problems and customer segment have not been named yet at all.** This document asks you to state
  beliefs about a segment and its problems, not to discover the segment from scratch; if nothing is known
  yet, talk to customers first and come back to the canvas once there is a first guess to write down.
- **The content is a financial model or a multi-year budget.** "Rather than thinking in terms of three-
  or five-year forecasts, it's better to take a more stage-based approach." A real financial model belongs
  in `business-case`, not in this canvas's Revenue Streams or Cost Structure boxes.
- **The content is one initiative's hypotheses, not the whole business.** A Lean UX Canvas frames one
  piece of work; this canvas states the business model that work sits inside, including revenue, cost
  and channels, which a single initiative does not need to answer on its own.
- **The reader needs a finished plan rather than a current best guess.** "Unlike a business plan, the
  goal with a Lean Canvas isn't to achieve perfection but to take a snapshot." A reader expecting a
  business plan's completeness will be disappointed by design, not by a defect in the fill.

## Picking a variant

There is nothing to pick. This bundle ships one size, `lean`, and every source that addresses length
agrees the canvas is meant to be compact rather than offered in a longer form. "Embrace a 1-page
constraint", and the reason given is not a formatting preference: "Describing your idea on a single
page is not about using smaller fonts but fewer words." The 2011 walkthrough agrees from its own angle:
"Sketch a canvas in one sitting", and "The boxes on the Lean Canvas are intentionally small because it
forces you to be concise." It is normal, not a sign of an unfinished draft, to leave a box short: "it's
okay to leave boxes blank", and "It's okay to leave sections blank". Do not build a longer variant by
copying a worked example's length into the template; the shortness is the design, not a limitation of a
first pass. See `lean-canvas_companion.md` section 4 for the fuller argument; it is not repeated here.

One further note on scope, not on size: if more than one customer segment is genuinely in play, the
originator's own method is to sketch a separate canvas per segment rather than to widen one canvas to
hold both. "Sketch a Lean Canvas for each customer segment", starting with
"the top 2-3 customer segments you feel you understand the best or find most promising", then
"lay them side by side and select the best business model to start with." Treat a single canvas, filled
in with this template, as covering one segment at a time.

## The rubric

Score each row 0, 1 or 2. Below 12 out of 18, hold the canvas back from the one other person you are
supposed to share it with once it is done: at least one box is still asking that reader to react to a
feature list, a multi-year forecast, or a belief nobody could ever prove wrong, rather than to a real
current best guess.

| # | Criterion | 0 | 1 | 2 |
|---|---|---|---|---|
| 1 | **Early adopter, not market** | Customer Segments names only a broad market or demographic label, with no Early Adopters line that differs from it | An Early Adopters line exists, but it restates the broader segment in other words rather than narrowing it | The Early Adopters line names a trait specific enough to recognize that person before a mainstream buyer exists at all |
| 2 | **Problem stated as problem** | At least one line in Problem is already a solution in disguise; lifted into the Solution box, it would read the same way | Every line is a problem, but at least one is generic enough to fit almost any product in any category | Every problem is a pain the segment has today, independent of this product, that could still be checked as true even if this product never existed |
| 3 | **Solution bound late** | Solution covers ground the Problem box never named, reading like a specification rather than the simplest fix | Solution matches the scope of Problem, but nothing in it shows that Customer Segments and Problem were actually settled first | Every line in Solution answers one specific problem named above, and the box could not have been written before that problem was |
| 4 | **Near-term, not a forecast** | Revenue Streams or Cost Structure states a multi-year figure, a projection, or a budget for a team the product has not earned | A near-term figure appears in both boxes, but neither is tied to a stated, specific milestone | Revenue Streams and Cost Structure name the same specific milestone, three to six months out, and say whether the price has actually been tested with anyone |
| 5 | **Key Metrics are outcomes** | At least one metric counts something the team produced, such as a feature shipped or an item added to a database, rather than a result | Between three and five metrics are listed, but at least one still counts an output rather than an outcome | Three to five metrics are listed, and every one is a result a customer or the business actually experiences, not an output the team merely produced |
| 6 | **Unfair Advantage is honest** | The box names effort, enthusiasm, or a feature a well-funded competitor could ship next quarter | The box is left blank, with nothing said about what would have to become true before something qualified | The box either names something that would survive being said out loud to a competitor, or it is blank and states plainly what is still missing |
| 7 | **One message** | The box reads as a list of features or benefits rather than one sentence stating why the product is different | One message is stated, but the High-Level Concept line is missing, or is a slogan with no comparison in it | One sentence states the single reason to pay attention, and the High-Level Concept names a concrete "X for Y" comparison a stranger could repeat back unprompted |
| 8 | **Riskiest belief is falsifiable** | No row in Riskiest Beliefs and Next Tests names a test that could come back negative, or the evidence column names enthusiasm rather than evidence | At least one row names a real test, but the rows naming a customer or problem belief are not the ones treated as riskiest | The row treated as riskiest names a customer or problem belief, states honestly what evidence, if any, backs it, and names a next test specific enough that it could refute it |
| 9 | **Versions record real change** | A revision has happened but the Versions table is empty, or its one row says only that "the canvas was updated," with no box or reason named | A row names which box changed, but not the belief the change followed from, or whether that belief was confirmed or refuted | At least one row names the box that changed, the belief from Riskiest Beliefs and Next Tests it followed, and whether that belief was confirmed or refuted |

## Anti-patterns

- **Drafting the first sketch as a group exercise.** The current teaching page names this directly and
  gives the fix in the same breath: "If you're part of a team, avoid creating a Lean Canvas as a group
  exercise. Instead, have each team member create their snapshot first." Reconcile snapshots afterward;
  do not start from a blank page with the whole team in the room.
- **Skipping the canvas and keeping the beliefs in your head instead.** The 2011 walkthrough names this as
  a real and common failure, not a hypothetical one: "A lot of entrepreneurs skip this step altogether
  which is NOT the solution." The same text names the cost of skipping it: "Too many founders carry their
  hypotheses in their heads alone which makes it hard to systematically build and test a business."
- **The solution-first trap: writing the Solution box before Customer Segments and Problem are settled.**
  The instruction to wait is stated in both eras of Maurya's writing: "Bind a solution to your problem as
  late as possible." A trade-press interview reports him naming the general habit directly, including
  himself among those who fall into it:
  "The biggest mistake I find which we all make - myself included - is this love for the solution,"
  which he calls "an innovator's bias".
- **Treating Revenue Streams and Cost Structure as a multi-year forecast.** The current teaching page names
  the fix in the same sentence as the problem: "Rather than thinking in terms of three- or five-year
  forecasts, it's better to take a more stage-based approach." Both boxes get their near-term number from
  the same milestone, not from two separate timelines.
- **Filling Unfair Advantage with effort or enthusiasm instead of an honest blank.** "A real unfair
  advantage is something that cannot be easily copied or bought," in Jason Cohen's definition, which
  Maurya quotes. It is normal for the box to have
  nothing yet: "Leave the unfair advantage blank." Writing in something that is really just hard work
  or enthusiasm is worse than leaving the box honestly empty.
- **Marking a belief "validated" on the strength of excitement rather than a real test.** Maurya's own
  teaching on this practice is to "focus on your weakest links first - your riskiest assumptions", and to
  check first whether customer and problem beliefs are grounded in real learning before trusting the rest
  of the model. A row that cannot be proven wrong, backed only by how excited the team already is, has not
  done that work.
- **Sketching it once and never returning to add a Versions row.** The canvas is built to be kept current,
  not archived after one pass: "The canvas is meant to be an organic document that evolves over time", a
  format meant for "tracking ongoing learning". A Versions table with no entry after the first sketch is a
  sign this discipline has lapsed, not a sign the model turned out to be settled on the first try.

## Before you share it

- [ ] You sketched this alone, or each team member sketched a snapshot first, before anyone reconciled
      them into one canvas.
- [ ] Every line in Problem states a pain the segment has today, not a solution wearing a problem's
      heading.
- [ ] Revenue Streams and Cost Structure both name the same near-term milestone, not a multi-year number.
- [ ] Key Metrics lists three to five outcomes, not outputs the team produced.
- [ ] Unfair Advantage either names something a competitor could not simply copy or buy, or is honestly
      blank.
- [ ] The riskiest row in Riskiest Beliefs and Next Tests names a test that could actually come back
      negative.
- [ ] You have deleted every HTML comment before sharing it.
