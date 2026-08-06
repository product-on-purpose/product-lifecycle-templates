# User Persona: the guide

How to tell whether you need one, how to pick lean or full, and how to grade what comes back before a team
starts designing against it.

## Before you start: is this the right document at all?

Write a user persona when a product or design decision is being argued from an average user or a guess, and
you need to argue it from a specific, researched person instead. Nielsen Norman Group states the standard
this document exists to meet: a persona must be based on user research to accurately represent a product's
users, not on what a team assumes a user wants.

**Write something else if:**

| You actually need | Because |
|---|---|
| a **buyer persona** | you need insight into a purchase decision, the attitudes, concerns, and decision criteria that drive someone to choose you, a competitor, or the status quo. A profile that only lists individual characteristics reveals nothing about how to influence that decision, which is exactly what a buyer persona is built to do and a user persona is not |
| an **anti-persona** | you want to name the customer type a team deliberately does not want, built from its own data the other way around. It ships as a separate document once a positive persona exists, not a section inside this one |
| a **market segment** | you need a strategic, faceless grouping tool for a strategy that already exists. This document is a tactical, humanized single-character tool used early, to see the product through one representative person's eyes before a strategy is set |
| an **empathy map** | you need a single-session workshop canvas for understanding a stakeholder in one specific context. It is a structurally different artifact from this document, and choosing one does not rule out the other |
| a **prototype-brief** | the person already exists and a team is ready to test a specific hypothesis about what to build for them. That document takes over once this one has done its job |

**Write nothing at all if** no design or product decision is actually turning on knowing who this person is.
The document exists to let a team argue from a specific person instead of a vague average; if nobody is going
to make that argument, there is no argument to ground.

**One posture worth adopting before you start.** The evidence behind a persona is a spectrum, not a pass or
fail: a proto-persona built from workshop assumptions with no new research sits at one end, and a
statistically clustered persona built from a large survey sits at the other. Neither is illegitimate. What is
illegitimate is labelling one tier while the document actually rests on the other, so decide, honestly, which
tier you are building before you fill in a single field.

## Picking a variant

**Lean** carries Who They Are, Goals and Motivations, and Pains and Barriers: enough to name a specific
person and ground a design conversation in someone other than the designer. Use it when a team needs a
shared reference point fast and a full research programme has not run yet.

**Full** adds Context of Use, Scenarios, and Evidence Basis, the three sections a reader needs to see how this
person actually behaves and how much research stands behind the picture. Use it once a decision genuinely
turns on knowing this person's situation, not just their goals and pains, and once you have enough behind you
to fill Evidence Basis honestly rather than leave it a guess wearing a field's shape.

The signal to move from lean to full is not a calendar, it is a question: does the next decision depend on
where, when, or how this person actually uses the product, or on seeing a concrete path they take through it?
If the answer is no, lean is not a smaller version of the job, it is the whole job for that decision.

A persona untouched for years is not automatically wrong, but named triggers exist for revisiting one: a
business change, a competitive change, or a shift in who is actually using the product. Build the revisit
trigger into Evidence Basis on the full variant rather than leaving the decision to whoever next remembers the
document exists.

## The rubric

Score each row 0, 1 or 2. Under 11 out of 16 on a full persona, and a team will design against a situation or a
research claim that is not actually there, which is a worse failure than designing against no persona at all.
Under 6 out of 8 on a lean persona, and the document is not yet a specific person, it is a set of labelled
boxes a reader still has to fill in themselves before they can argue anything from it. The lean variant scores
against fewer rows because it does not ship the three sections a behavioral or evidentiary decision depends
on; the scope table below says which.

| # | Criterion | 0 | 1 | 2 |
|---|---|---|---|---|
| 1 | **Goals are sourced** | A goal appears with no evidence column filled in, or the column says only "user research" with nothing a reader could go check | An evidence column names a method, but not enough for a reader to find the actual thing it points to, no count, no date, no way to locate it | A reader could go find the interview, ticket pattern, or observation named and see this exact goal for themselves |
| 2 | **Quote earns its place** | No quote, or a quote that reads like a mission statement anyone in the role could have written | A quote exists, but nothing in it or the background could not apply to any person in that role at any company | The quote states something specific enough that only someone who actually talked to this population would have produced it, and the background places the person without extra demographic fields |
| 3 | **Barrier paired with cost** | A pain or barrier is listed with no stated impact and no evidence | An impact is stated, but it is generic enough to describe any frustration ("communication could be better") | The barrier names a concrete cost to this specific person, is paired with the goal it blocks, and states where it was observed or heard |
| 4 | **Field earns its place** | Fields are stacked with no bearing on a design decision, and nothing states why they are there | Some fields beyond the essentials are present, but nothing in the document says what decision any one of them would change | Every field, if removed, would change what a reader could confidently decide or build; nothing in the document is there because a template elsewhere had it |
| 5 | **Context changes a decision** *(full only)* | A context row restates the persona's role, or answers a yes/no question with no detail behind it | A context row states a real fact, but nothing about it would change what actually gets built | At least one context row, if it were wrong, would change a real design or engineering choice, and you can name which one |
| 6 | **Scenario has an outcome** *(full only)* | The scenario is a single sentence, or walks through product screens with no want and no outcome | The scenario has a beginning, middle, and end, but you could swap in a different persona's name and nothing would need to change | The scenario names a specific want, a specific path through the product tied to that want, and an outcome that could plausibly have gone the other way |
| 7 | **Tier matches its basis** *(full only)* | The evidence tier is a label like "research-backed" with no basis stated underneath it | A tier is named and a basis is stated, but the basis does not actually support the tier claimed, for example "qualitative" with zero interviews behind it | The stated tier and the stated basis agree, and a reader could check the basis against a plain definition of that tier and reach the same label |
| 8 | **Revisit trigger stated** *(full only)* | No revisit trigger is stated, or it names a fixed calendar date with no reasoning behind it | A trigger is named, but it is generic enough to apply to any persona for any product ("when things change") | The trigger names a specific kind of event, a business change, a competitive change, or a shift in who is actually using the product, that a reader would recognize the moment it happened |

**Which rows apply to what.** Full ships all eight rows because a design decision that depends on situation,
path, or research strength depends on all of them. Lean ships only the four rows that do not require a section
it does not carry.

| Document | Rows | Maximum | Score against |
|---|---|---|---|
| lean | 1, 2, 3, 4 | 8 | **6** |
| full | all 8 | 16 | **11** |

## Anti-patterns

**Treating an unresearched persona as though it were evidence-backed.** A proto-persona built openly from
workshop assumptions is not a lesser document, it is this same format used honestly. The failure is not
building one at the lightest tier, it is labelling it as though it sat at a heavier one.

**Adding fields past what changes a decision.** A persona's population coverage shrinks combinatorially as
attributes accumulate, worked through to roughly 134 people in the whole United States for a 21-attribute
example. Every field added makes the persona describe fewer real people, and each one should earn its place
by changing what a reader would build or decide.

**Citing the 900 percent statistic, or figures like it, as fact.** The widely circulated persona-effectiveness
number traces to a single uncontrolled case study that bundled persona work with a full site redesign, a
content overhaul, and an email-automation change, with no comparison group and no isolation of the persona
variable. The number is real; it supports nothing about personas specifically, and repeating it in your own
document does not make it more credible.

**Treating the persona as an isolated UX deliverable.** The documented account of why personas fail in
practice is organizational rather than method-level: not an endeavor undertaken by one team and unveiled like
a piece of artwork, and not a stack of handouts nobody actually opens. A persona that nobody outside its
authors ever consults has already failed, whatever its content says.

**Building a persona to justify a decision already made.** Persona use has been documented as serving
primarily to justify decisions made on other grounds rather than informing them. If every goal in the table
happens to match a feature already on the roadmap, that is worth noticing, not celebrating.

**Letting a persona go stale.** Named triggers exist for revisiting one: a business change, a competitive
change, or a shift in who is actually using the product. A persona left untouched for five or more years is,
in the field's own description, performing about as well as a dull knife on steak, and a stated revisit
trigger is what keeps that from happening quietly.

**Writing pains and barriers that quietly exclude disability.** Naming, imagery, and accessibility are three
concrete bias vectors in how pains and barriers get written. A persona for a broad user base that never names
a disability-related barrier is making a choice, not an omission, and the choice should be a deliberate one,
not a default.

**Letting a persona harden into a marketing segment wearing a person's name.** This pattern has a name in the
field's own literature: marketing segments masquerading as personas. It is a different failure from an
unresearched persona, the document still looks like a persona, but the research behind it has quietly been
replaced by a market category, and a reader has no way to tell from the page alone.

## When it is good enough

When every goal and pain in the table has a source a reader could actually go check, when no field is on the
page because a template elsewhere had it, and, for the full variant, when a reader can point to one context
factor or one scenario step that would change what actually gets built.

Then delete every HTML comment, and treat the evidence tier as the honest floor of the document rather than a
label chosen to sound more credible than the work behind it supports. That distinction, between what the
research shows and what a team would prefer it showed, is what this document exists to protect.
