# Guide: Experiment Readout (operator card)

The short card. Why the document is shaped this way, and the argument behind every rule here, is in
[`experiment-readout_companion.md`](experiment-readout_companion.md). A fully worked instance is
[`experiment-readout_example.md`](experiment-readout_example.md).

**One honest limit before anything else.** No source read for this bundle measured whether writing this
document improves a decision. The case for it rests on the failure modes the sources name (peeking,
cherry-picking, a loss reported as a win) and on keeping a record a later reader can audit, not on a
controlled comparison of documented against undocumented tests. Read the rest of this card with that limit
in mind.

## When to use

- A test that an experiment design doc planned has ended, and the decision it was meant to inform needs to
  be recorded before anyone acts on the result.
- The result needs to be checked against the pre-committed decision rule, the guardrail thresholds, and the
  validity checks the design doc set, rather than judged fresh from whatever the dashboard shows that day.
- More than one person needs the same account of what happened, including someone who was not in the room
  when the call was made.
- The result is a null or a guardrail breach, where the pull to skip writing anything down is strongest, and
  where a record matters most: a decision not to ship is still a finding worth keeping.

## When NOT to use

- **The test has not ended, or its pre-committed duration has not been reached.** Reporting a result before
  that point is the early look that inflates a reported significance level. Wait for the committed duration,
  or, if monitoring mid-test, treat anything seen as informational only.
- **You need a qa-docs test plan or test summary report.** That document verifies a product increment
  against an agreed specification and grades it pass or fail, with no hypothesis, no allocation between
  variants, and no statistical decision rule. This document estimates an effect against a baseline. See
  companion section 8 for the boundary in full.
- **You need a spike report (decision-docs).** A spike reduces uncertainty about a technical question with
  no control group and no statistical decision rule; a refuted hypothesis there is a successful spike, which
  is never true of a result reported here. See companion section 8.
- **A vendor's live scorecard or one-time metrics export already exists, and the team is tempted to call
  that the readout.** Statsig's export carries no decision field, Optimizely's scorecard is a live monitoring
  surface, and no source read for this bundle says either one replaces a written readout or sits beside it
  as a substitute. Use the in-tool surface for monitoring and
  raw export; keep the decision and its reasoning in this document.
- **A test was run before anything was built, to decide whether to build it at all.** That is excluded from
  this family by name. It is not this document's job under any variant.
- **You need a standing instrument.** A tracking plan, a KPI dashboard, or an experiment log is maintained
  across many tests and is never finished. This document is written once per test and is finished when the
  decision it exists to inform is recorded.
- **There is no design doc to report against.** Without one, there is no pre-committed decision rule,
  guardrail threshold, or validity check to check this result against, and the two documents are a
  sequential pair for exactly that reason. Write the design doc first, even retroactively, stating what the
  decision rule would have been before reading the results, rather than filling this document in from a
  blank page.

**A team that keeps one living document** for the plan and the results instead of two separate files still
uses this bundle's sections; they simply become that document's second half, after the sections the
experiment-design-doc's own guide covers. The two bundles' sections do not overlap, so nothing here needs
renaming to fit one file instead of two.

## Pick a variant

**Lean (eight sections)** is the default: Executive Summary, Context and Setup, Key Results: Primary
Metrics, Key Results: Supporting Metrics, Validity Checks, Decision, Decision Owner, and Next Steps and
Owners. Use it when the eight lean sections already carry the whole decision.

**Full (eleven sections)** adds Deep-Dive, Implementation Details and Analysis Notes, and Further Analysis.
Use it when the decision rests on more than the primary metric alone, such as a business question answered
through a specific segment, or when readers will want to audit the underlying analysis later. Every lean
heading appears in full, unchanged in name and order, so growing from lean to full never means rewriting a
section already filled in.

## The rubric (self-grade)

Score each row 0, 1 or 2. Score the full variant under 14 out of 20, or the lean variant under 11 out of 16,
and a reader needs to reopen the design doc and the raw numbers to reconstruct what was actually decided
and why, which is exactly the meeting this document exists to make unnecessary. The lean variant carries fewer rows; the scope table below states each
variant's own maximum and threshold.

| # | Criterion | 0 | 1 | 2 |
|---|---|---|---|---|
| 1 | **Decision stated up front** | The summary describes the test or its mechanics but never states a decision; a reader must go to the Decision section to find out what happened | A decision word appears ("null," "shipped") with no statement of why it matters or what it changes | The first sentence names the decision and the one finding behind it, so a reader who stops there could still repeat, correctly, what was decided and why |
| 2 | **Deviations from plan checked** | The design doc is not linked, or the deviations line is missing entirely | The design doc is linked and "no deviations" is asserted, with nothing said about what was actually checked (dates, split, population) against the plan | The design doc is linked, and the deviations line either names the specific change, with what, when and why, or confirms the match by naming the actual dates, split and population run |
| 3 | **Uncertainty is legible** | A change is reported with no interval at all | An interval appears, but its confidence level is not stated in the row, or only one of the absolute or relative change columns is filled in | Both change columns, the interval, and the interval's own stated confidence level appear in the same row, so a reader can tell the result from noise without a follow-up question |
| 4 | **Guardrails read against thresholds** | A guardrail is reported with a value and no threshold to compare it to, or a guardrail the design doc named is missing from the table | Thresholds appear for some guardrails but not all, or a threshold was set at readout time rather than carried from the design doc | Every guardrail the design doc named appears, each against the design doc's own threshold, with a held-or-breached call a reader could check against the adjacent numbers |
| 5 | **Validity checks named** | One blanket line, such as "looks fine," stands in for the whole section, with no individual check named | Some checks are named with a specific result, but at least one check the design doc pre-committed to running is missing, or a result is stated with no specifics | Every check the design doc pre-committed to appears by name with a specific, checkable result, a number, a date range, or an explicit "not applicable" with why, and nothing beyond what was pre-committed is invented |
| 6 | **Null scope stated** | The outcome carries a label (win, null, loss) with no statement of what that label rules in or out | An effect size or interval is mentioned but not tied explicitly to what the result does and does not rule out | The decision names which of ship, iterate or stop the pre-committed rule produced, and for a null result, states the effect size it rules out and names a smaller one it does not |
| 7 | **Owner reconciled with plan** | No individual is named; "the team decided" or "leadership agreed" stands in for a person | A specific person is named, with nothing said about whether that person matches the design doc's own decision-maker field | A specific person and venue are named, and the section states explicitly whether that person matches the design doc's decision-maker, with a reason if it changed |
| 8 | **Next steps owned** | An action is listed with no owner, or "the team" stands in for a name | Most rows carry one named owner, but at least one does not, or no row carries a status | Every row names exactly one person and a status, and the action the decision itself requires, such as a rollout, a rollback or a retirement, appears first |
| 9 | **Segments name complements** *(full)* | A segment's result is reported with no statement of whether the design doc fixed that segment in advance, and no complement value shown | The segment is named as pre-registered or exploratory, but its complement's own number is missing, or vice versa | Every segment claim states whether the design doc fixed it in advance, and shows the complement subgroup's own number alongside it, so a reader can see whether the effect is isolated or general |
| 10 | **Further Analysis kept separate** *(full)* | An item there is also invoked, even implicitly, to support the Decision section above, or the section reads as an unsorted dump with no stated reason the items do not matter to the decision | Items read as plausibly exploratory, but the section never states outright that none of them factored into the decision | The section states explicitly that nothing in it factored into the decision above, and every item is framed as a lead for a future test rather than evidence for this one |

**Rows 9 and 10 are scored only against the full variant.** The lean variant ships no Deep-Dive and no
Further Analysis section, so grading it on those rows would penalize the choice of variant rather than the
quality of the document.

**Which rows apply to what.**

| Variant | Rows | Maximum | Threshold |
|---|---|---|---|
| full | 1-10 | 20 | **14** |
| lean | 1-8 | 16 | **11** |

Score a row 2 only when you can point at the specific sentence, number or name its cell asks for; a longer
document is not automatically a better one.

## Named anti-patterns

**Naming the lift-decay pattern a "primacy effect."** The tell: a draft describes an early lift that falls
across date segments and labels it with that term. No source read for this bundle uses it. The fix: call it a
novelty effect, the term the sourced pattern actually carries, and detect it by segmenting the result by
date, the way the Validity Checks section asks for. Deep dive: companion section 7.

**Presenting "ship, iterate or stop" as a convention the sources use.** The tell: a draft cites a source for
the three-way outcome by name. It is this family's own wording, stated as the contract's position, not a
phrase any source read here uses verbatim. The fix: state it as this library's own choice, as the anatomy in
companion section 3 does, rather than attributing it to the research. Deep dive: companion section 7.

**Presenting a significance level, power level or test duration as a field-wide standard.** The tell: a
draft states "95% confidence" or a fixed test length as a default rather than something the design doc or the
platform actually used. The one specific figure in the sources is one company's own reported practice, not a
cross-industry norm. The fix: state whichever level the design doc or the platform actually used, in the
row, and do not present a borrowed number as a default. Deep dive: companion section 6, item 8.

**Treating a null result as proof the change has no effect.** The tell: the Decision section reads a null as
"it doesn't work" with no reference to the interval's width. A null on a test powered to detect a large
effect says nothing about a smaller one. The fix: state the specific effect size the result rules out, and
name a smaller one it does not, as rubric row 6 requires. Deep dive: companion section 7.

**Treating a guardrail breach as an automatic block on shipping.** The tell: a draft states that any
guardrail movement past its threshold ends the test, as a universal rule rather than the specific rule the
design doc fixed. No source read for this bundle states a standard way to weigh a primary gain against a
guardrail regression. The fix: report the guardrail's movement against the design doc's own pre-committed
rule for that specific trade-off, and let that rule, not a blanket policy, decide what the breach means. Deep
dive: companion section 7.

**Claiming that tags make an experiment archive findable.** The tell: a draft adds a tags field to this
document's frontmatter and describes it as how future readers will find the experiment. One source reports
the opposite of its own practice: labelling experiments with tags proved unsustainable at its scale. The fix:
rely on the frontmatter fields this bundle already carries, the experiment's name and its design-doc link,
rather than adding a field this bundle has no source for. Deep dive: companion section 6, item 5.

**Borrowing a clinical or public-sector element and presenting it as product-management practice.** The
tell: the deviations-from-plan line, the both-sided effect-size columns, or the complement-subgroup rule
appears with no statement of where it comes from. Each of these three pieces is borrowed from a clinical
trial-reporting standard, not from any product source. The fix: name the lineage each time a borrowed
element is used, as the anatomy in companion section 3 does, rather than letting it read as settled product
practice. Deep dive: companion section 5.

**Treating a vendor's in-tool scorecard or export as a substitute for, or a companion to, this document.**
The tell: a draft links a live scorecard or a one-time PDF export in place of filling in Key Results or
Validity Checks. Statsig's export carries no decision field, and no source read for this bundle claims either
surface replaces or sits beside a written readout. The fix: use the in-tool surface for what it is built for,
live monitoring and raw metric export, and keep the decision and its reasoning in this document. Deep dive:
companion section 8.

## When it is good enough

When a reader who was not in the room, and has not seen the raw data, could state the decision, the one
finding behind it, and what happens next, from this document alone, without reopening the design doc or the
dashboard to check any of it. A readout that still requires a meeting to explain what the result meant has
not finished its own job.

Then self-grade against the rubric above, confirm the decision owner matches the design doc's own
decision-maker or states why it changed, and delete every HTML comment before sharing it.
