# North Star Metric: the guide

An operator card. Read it before you fill the template and again before you agree the definition. The
reasoning behind every rule here lives in [`north-star-metrics_companion.md`](north-star-metrics_companion.md).

## Before you start: is this the right document at all?

A North Star Metric names the single measure of customer value that shows a product's strategy is working,
and the small set of inputs a team can actually move to drive it. If your real question is something else,
write something else.

| If the real question is | Write this instead |
|---|---|
| Where are we trying to get to, over years, and why is it worth getting to? | [`product-vision`](../product-vision/) |
| Which problems will we solve to get there, and which will we not? | [`product-strategy`](../product-strategy/) |
| In what order will we work on those problems? | [`product-roadmap`](../product-roadmap/) |
| What measurable change do we expect this period, and did we get it? | [`okrs`](../okrs/) |
| What is the formula, the data source, the refresh schedule, or the target behind this number? | [`kpi-dashboard`](../kpi-dashboard/) |
| What does the whole hierarchy of metrics beneath this one look like? | the catalog's own metric-tree document type, which the companion notes is not yet built in this library |

**Write nothing at all if you cannot yet name a product strategy for this product.** A North Star measures
whether a strategy is moving the product toward its vision; with no strategy stated, there is nothing for
the number to measure yet, and the document would be guessing at both ends.

## Picking a variant

**lean** carries the metric's name and definition, the case for it, its inputs, what it serves, and the
trigger that would bring you back to it. That is enough for a first definition, or for a team that is
unlikely to be asked what was rejected.

**full** adds four sections: Candidates Considered, Guardrails, What It Does Not Tell Us, and Definition
History. Reach for full once the North Star has already faced, or will soon face, real scrutiny: named
alternatives were seriously compared, a stakeholder will ask "why not X", or the definition has already
changed once and the change needs a record.

**Guardrails is worth a separate word.** It is the one full-only section whose evidence does not come from
Amplitude, the publisher this document type is admitted on. Amplitude's own two documents never use
"guardrail" for a measure tracked beside the North Star; the section instead rests on three other sources.
Choosing lean and leaving Guardrails out is not skipping an Amplitude step.

## The one test that outranks the rest

**Could your team move this number directly?** John Cutler, co-author of Amplitude's own playbook, states
the test plainly: "If you can move your North Star directly, it's probably not a good North Star." A number
your team can push on its own is a lever, not a North Star; the North Star is what the levers are supposed
to move.

One boundary check sits beside it, about discipline rather than form: **does anything here belong to
`kpi-dashboard` instead?** A formula, a data source, a refresh schedule, a target, a threshold. If you catch yourself writing
one of those into this document, stop and open `kpi-dashboard`.

## The rubric

Score each 0, 1 or 2. Below 15 out of 22, the document has named a metric without doing the one thing a
North Star is for: letting someone else ask, of a real piece of work, "does this move the north star", and
get an answer instead of a shrug. The lean variant scores against fewer rows; see the scope table below.

| # | Criterion | 0 | 1 | 2 |
|---|---|---|---|---|
| 1 | **Counts a real behavior, not a lever** | No behavior is named, the sentence names an aspiration rather than something that happens, or one team could push the number up directly without any input moving first | A behavior is named, but the actor, the window, or both are missing, or a calculation or data source has crept in | You can read the sentence once and say back who does what, how often, with nothing in it that belongs in a formula, and no single team can move it except by moving an input |
| 2 | **Validation is honest** | The claim that this metric predicts retention or revenue rests on nothing: no evidence, no plan to get any | Evidence is named, but it is another product's data, or the plan to validate has no date and no owner | You can point to a correlation run against this product's own data, or to a dated, owned plan to run one |
| 3 | **Fits in one sentence** | The definition takes more than one sentence, or leans on a term only the people who wrote it would recognize | One sentence, but it would need an example or a follow-up question before an outsider could use it | One sentence, plain enough that you can picture someone in sales or support repeating it back correctly, unprompted |
| 4 | **Inputs are real levers** | A row names a team with no measure, or restates the North Star itself under another label | Every row names a measure and an owner, but at least one owner would not actually notice it slip | For each row, you can name who would notice it slip this week and say in one sentence why moving it should move the North Star |
| 5 | **Measures, not mirrors** | The section could be lifted straight out of the product strategy with no change | It names the strategy and the vision, but the business outcome is vague, or written as if the metric were that outcome | You can say which strategy this number tests, and name the outcome it predicts without being that outcome |
| 6 | **Trigger, not a date** | The answer is a calendar entry, with nobody named to notice anything | An event is named, but nobody is named as responsible for noticing it | A specific shift is named, a specific person owns watching for it, and it is kept distinct from a target the number merely misses |
| 7 | **Filters a real decision** | Almost any project in flight could claim to serve this document; nothing here would rule one out | The document could rule something out in principle, but nobody has actually tried asking it of a real, named project | You can name a real project and show, from this document alone, whether it moves the North Star or not |
| 8 | **Candidates were real** *(full)* | Every rejected candidate is a straw metric nobody was proposing | A real candidate appears, but the reason it lost would equally disqualify the metric that was kept | At least one candidate could pass a casual glance, and its rejection names the specific test it failed |
| 9 | **Guardrails earn their place** *(full)* | A guardrail restates the North Star itself, or names a check with no stated harm | Each guardrail names a real measure, but for at least one you could not say what its decline would actually mean | Each guardrail could fall while the North Star climbs, you can state what that fall would mean, and none is the North Star's own inverse |
| 10 | **Owns its blind spots** *(full)* | The section claims the metric has no real blind spots | A blind spot is named, but nothing elsewhere in the document catches the gap it describes | A blind spot is named before the metric ships, and a guardrail or an input exists in this document because of it |
| 11 | **History survives the change** *(full)* | An earlier definition is missing from a North Star that has in fact changed, and there is no "first definition" entry either | The new definition is recorded, but the old one, or the reason for the change, is missing | The old definition sits beside the new one, dated, with the shift in product, market, or strategy that caused it, or a dated "first definition" entry if there is no earlier one |

**Which rows apply to what.**

| Document | Rows | Maximum | Score against |
|---|---|---|---|
| full | all 11 | 22 | **15** |
| lean | 1-7 | 14 | **10** |

**Rows 8 to 11 are scored only against full.** The lean variant ships no Candidates Considered, Guardrails,
What It Does Not Tell Us, or Definition History section, so grading it on those rows would penalise the
choice of size rather than the quality of the document.

## Failure signals to look for in the draft

Nothing here ranks against anything else; read it as a list, not an order.

- **A metric that can only rise.** Total registered users, cumulative downloads, and pageviews only go up,
  and a metric that can never fall cannot warn you when something is wrong. Test it with the doubling
  question: if this number doubled next month, would the business clearly be healthier? If not, it is a
  vanity metric wearing a North Star's clothes.
- **A metric the team can move directly.** See the first test above. If your own team's effort alone can
  push the number, it is a lever, not the thing the levers are supposed to move.
- **Revenue, or any lagging measure, standing in for the metric.** Every source that addresses this agrees
  on direction: revenue tells you what already happened, not what is about to.
- **Gaming it once it becomes a target.** Named independently, under different words, by a reference source
  asking how to keep the number from being gamed, and by a practitioner's essay, *South Star Metrics*, about
  exactly this failure.
- **Letting departments run their own, uncoordinated North Stars.** One practitioner's own warning is that
  this compounds as a company grows; nobody is left who can say which number the company is actually
  steering by.
- **Silently rewriting the definition instead of recording the change.** The discipline a glossary entry
  states directly: preserve the old definition and explain the break in the series rather than rewriting
  history.
- **A composite score standing in for a single metric.** Composite scores with several weighted inputs fail
  the one-sentence test even when they are, on paper, more complete.
- **Mistaking it for a goal-setting method.** Amplitude's own playbook names this directly as what the
  Framework is not, and says so right next to the warning that it can still be a foundation goals are built
  on.

## Before you share it

- [ ] You can say the definition back in one sentence, and so could someone outside the team.
- [ ] Nothing in the document is a formula, a data source, a refresh schedule, a target, or a threshold.
- [ ] Every input names an owner who would actually notice it slip.
- [ ] The revisit trigger names an event and a person, never only a date.
- [ ] If this is the full variant: Candidates Considered, Guardrails, What It Does Not Tell Us, and
      Definition History are filled with real content, not left at "N/A" by default.
- [ ] You have deleted every HTML comment before sharing it.
