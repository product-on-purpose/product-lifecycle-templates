# Business Case: the guide

How to tell whether you need one, how to pick lean or full, and how to grade what comes back before it
reaches a funding decision.

## Before you start: is this the right document at all?

Write a business case when a real investment decision is at stake and you need to say, in writing, what the
investment is being compared against, including doing nothing. That comparison is the job. A document that
argues for one option without naming what it beats is not a shorter business case, it is a proposal wearing
a bigger name.

**Write something else if:**

| You actually need | Because |
|---|---|
| a **project brief** | you need a short overview for starting up a project, not an investment case. A project brief absorbs an outline business case as one component and retires once initiation documentation exists; the business case itself keeps being refined, it does not retire with the brief |
| a **trade study** | you are comparing technical approaches against weighted criteria, not comparing whether to invest at all. A trade study's output feeds into Options Considered as one input, it does not replace the case |
| a **PRD** | the investment decision is already made and you need to specify what gets built. A PRD deliberately excludes market opportunity and revenue, which is exactly the ground this document covers |
| a **cheap way to test a hypothesis** | you would rather validate an assumption than build a funding case for a known investment. The named alternative tradition is the SAFe Lean Business Case, which substitutes a hypothesis and leading indicators for a financial model. It is a genuinely different document, not a shorter one, and it is not shipped in this library |

**Write nothing at all if** no funding or go/no-go decision is actually on the table. The document exists to
decide whether an investment is worth making; if nobody is deciding that, there is no case to make.

**One posture worth adopting before you start writing.** Every standard this library's research could read in
full treats the business case as revisited as the work proceeds, not filed once at approval and never
reopened. Write it expecting to reopen it, not expecting to file it.

## Picking a variant

**Lean** carries Problem and Opportunity, Options Considered, and Recommendation: enough to scope a decision
and name what it is being compared against, without a financial model behind it. Use it to get agreement that
an idea is worth exploring further.

**Full** inserts Costs, Benefits, Risks and Financials between Options Considered and Recommendation, the four
sections a reader needs to actually commit money rather than merely agree the idea is worth exploring.

The signal to move from lean to full: are you asking someone to agree an idea is worth exploring, or asking
them to release real money? A rough estimate is a legitimate way to scope a decision, but the tolerance for an
unexamined estimate should shrink as the decision gets closer to an actual commitment, which is exactly the
point at which lean stops being enough.

If you would rather validate an assumption cheaply than build either size of this case, that is not a smaller
version of this document. See the hypothesis-driven alternative named above, and do not reinvent a thinner
version of this template to get the same effect.

## The rubric

Score each row 0, 1 or 2. Under 11 out of 16 on a full case, and finance should send it back before it reaches
a funding decision. Under 6 out of 8 on a lean case, and it cannot carry the scoping conversation it exists
to open, so that conversation gets decided on something other than what the document says. The lean variant
scores against fewer rows because it does not ship the four sections a funding decision depends on; the
scope table below says which.

| # | Criterion | 0 | 1 | 2 |
|---|---|---|---|---|
| 1 | **Problem before solution** | The section names a solution, not a problem | Names a problem, but you cannot point to who is affected or how the author knows | You can point to who is affected, how the author knows, and nothing in the sentence already names the fix |
| 2 | **Genuine alternatives** | One option only, or no do-nothing row | A do-nothing row exists, but its rejection reason is a single adjective with no content behind it | At least one alternative is a real option a reader could actually choose, and the do-nothing row states a genuine reason, not a formality |
| 3 | **Cost adjustment visible** *(full only)* | One lump total, no breakdown, no adjustment shown | Costs are broken into categories, but the optimism-bias adjustment is folded into the total invisibly | The base estimate and the adjustment appear as separate numbers, and the adjustment states its basis |
| 4 | **Benefits as ranges** *(full only)* | A benefit is named with no number attached | A single confident point figure appears with no stated method behind it | Each benefit is a range with a stated method, and no figure is one of the well-known unverified benefits-realisation statistics |
| 5 | **Risk mechanism named** *(full only)* | A risk is a generic worry with no owner | An owner is named, but the risk does not say whether it is closer to self-deception or deliberate overselling | The mechanism is named, an owner is named, and a concrete trigger for reopening the case is stated |
| 6 | **Financials caveated** *(full only)* | A metric is stated as a bare number with no caveat | A caveat is present but generic, not tied to what that specific metric actually gets wrong | Each metric carries a caveat drawn from that metric's own documented limit, and no ratio is used as an automatic accept-or-reject rule |
| 7 | **Recommendation earns its place** | The recommendation reads as a starting assumption with no link back to the analysis above it | The recommendation names the chosen option, but the reasoning could apply to any of the options listed | You can point to a specific line in Options Considered, and in Costs, Benefits, Risks or Financials where they exist, that the recommendation's reasoning depends on |
| 8 | **Post-go-live check named** | The post-go-live field is blank or says "TBD" | A check is named, but with no owner or no date | A named person checks a named outcome against this case's own figures, on a stated date or trigger |

**Which rows apply to what.** Full ships all eight rows because a funding decision depends on all of them.
Lean ships only the four rows that do not require a section it does not carry.

| Document | Rows | Maximum | Score against |
|---|---|---|---|
| lean | 1, 2, 7, 8 | 8 | **6** |
| full | all 8 | 16 | **11** |

## Anti-patterns

**The one-time gate.** Filed at approval and never reopened. Every standard this research could read in full
treats the opposite as the discipline: revisited as the work proceeds, with PRINCE2 naming a real
consequence, if the case stops being justified, the work it justifies should stop too.

**No genuine alternative.** Missing a do-nothing row, or a do-nothing row rejected in a single adjective with
no reasoning behind it. Both traditions this research read treat a named alternative as non-negotiable in
substance, whichever tradition places the section differently in the document.

**Optimism hidden in a lump total.** A single already-adjusted cost figure with no visible base estimate or
adjustment. The documented remedy is an explicit, empirically grounded adjustment shown separately from the
base number, not vigilance alone, and the tolerance for skipping it should shrink as the decision gets closer
to a real commitment.

**Strategic misrepresentation mistaken for optimism.** Treating every inflated estimate as innocent
self-deception when some are deliberate. The two are complementary mechanisms, not one blurred into the
other, and naming the wrong one misses the actual failure.

**Decision-based evidence making.** Assembling the case to support a decision someone has already made. This
can happen even with no competing proposal in sight, which is what makes it easy to mistake for strategic
misrepresentation; the fix is different because the underlying incentive is different.

**Borrowed benefits-realisation statistics.** Citing one of the well-known percentages that circulate in
practitioner writing with a name attached. This research could not independently verify any of them, and
repetition in your own case does not make an unverifiable number more credible.

**A ratio used as an automatic verdict.** Rejecting a proposal because its benefit-cost ratio misses a round
number, or comparing IRRs across projects of very different scale without their dollar size attached. A lower
ratio can still represent good value once benefits that were not monetized are weighed in, and a high
percentage on a small base is not automatically the better bet.

**No accountable check after go-live.** The sources this research could read hand the check to an
organisational layer on a generic schedule, a benefits review after the project closes, and stop there.
Inheriting that generic answer is the anti-pattern. Say explicitly which person checks whether the expected
benefits showed up, and on what date or trigger, rather than leaving it at the layer the standard names.

## When it is good enough

When someone with money to release can point to the alternative this recommendation beat, when the cost and
benefit figures show their own adjustment rather than hiding it, and when a named person already knows they
are checking this case's benefits on a specific date after go-live.

Then delete every HTML comment, and treat the document as reopened rather than filed away. That is the
discipline every standard this research could read in full insists on, and the distance between saying it
and doing it is what this bundle was built around. How wide that distance is, no source this research could
reach has measured.
