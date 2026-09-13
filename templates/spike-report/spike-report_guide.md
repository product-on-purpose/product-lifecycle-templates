# Guide: Spike Report (operator card)

The short card. Why the document is shaped this way, and the argument behind every rule here, is in
[`spike-report_companion.md`](spike-report_companion.md). A fully worked instance is
[`spike-report_example.md`](spike-report_example.md).

## When to use

**Read this first, because it changes what the card is claiming.** This is the one document type in this
library whose own canon argues against writing it: in Extreme Programming a spike produces code you throw
away, and Ward Cunningham's founding account says *"We plan to throw away the code, although sometimes
something is salvaged."* Exactly one named source in this bundle's research publishes the deliverable as a
document, Microsoft's Code with Engineering Playbook: *"Generally the deliverable from a Technical Spike
should be a document detailing what was evaluated and the outcome of that evaluation."* So nothing here says
that writing up your spike is settled practice. It says how to write a good one if you are writing one. Both
sides: [companion section 6](spike-report_companion.md#6-debates-and-contested-boundaries).

- A **named decision is waiting** on an answer nobody has, and someone other than you will act on it.
- The uncertainty is **knowledge-limited, not time-limited**, which is the founding XP wiki's own condition
  for reaching for a spike at all: *"Spikes are good when you are knowledge-limited, not time-limited"*. More
  hours of the current approach will not produce the answer; a different, bounded experiment will.
- The result has to be **checkable by someone who was not there**, rather than taken on your word.
- The evidence will **outlive your memory of it** and get cited. A later decision record, proposal or design
  document will lean on this rather than reconstruct it.
- **The answer might be no**, and a no needs to be as findable as a yes. A refuted hypothesis is a successful
  spike.

## When NOT to use

**Write something else if:**

| You actually need | Because |
|---|---|
| an **[ADR](../adr/adr_guide.md)** | the decision is being **recorded**, not investigated. It has already been made, and you are writing down what was chosen and what it costs. This is the drift to watch for: a spike report that arrives at a recommendation without recording what was tried is a bad ADR, and an ADR that shows its working is not a spike report. If the call is genuinely made, write the record and stop |
| an **[RFC](../rfc/rfc_guide.md)** | you are **proposing** a change and asking people to shape it, not investigating whether it is possible. An RFC argues a case and requests input; a spike report hands over evidence and gets out of the way. They are a sequence rather than a choice: what a spike hands over is what an RFC's motivation can then argue from |
| an **[SDD](../sdd/sdd_guide.md)** | you are **describing** a design: how the thing will be built, its components and their interactions. That document assumes the feasibility question is behind you. If it is not, the spike comes first and the design document cites it |
| **nothing** | the question can be answered by reading the documentation for ten minutes. Then read it, and spend the box on something that is actually uncertain. A spike is for an uncertainty that reading cannot close, and a spike with no answerable question is a research project wearing a time box |

**Write nothing at all if** no named decision is waiting on the answer. A ticket and a write-up created to
demonstrate activity rather than to reduce uncertainty is a failure mode this bundle calls the performative spike,
and the test for it is simple: somebody should be blocked on the result, and you should be able to say who.

## Pick a variant

There is no choice to make. This bundle ships **one file**, `spike-report_template-lean.md`, and that is a
finding rather than a shortcut: no source read for this bundle publishes two weights of a spike report, and
the one named source that publishes the document at all ships exactly one template. The variation the
research did find runs across **genre**, not weight. The longest templates found were written for an AI
coding agent to fill in, and their section counts should not be read as normal for a human team; at the other
end, one real published engineering process ships no document at all and closes the spike issue with a single
summary comment instead. The case is in
[companion section 4](spike-report_companion.md#4-variants-and-sizing).

The practice's own discipline argues against a heavier variant anyway. A spike is bounded at a couple of days
at the canonical end and one iteration at the outer end, and a document whose ceremony costs a meaningful
fraction of the investigation that produced it has inverted the point of the practice. *(That last sentence
is this bundle's judgment; no source read makes the argument directly.)*

## Quality rubric (self-grade before you hand it over)

Score each 0, 1 or 2. Under 13 out of 18 and the report hands its reader a verdict they cannot check, so they
either take your word for it or spend their own box repeating your work. Both outcomes waste the one you just
spent.

| # | Criterion | 0 | 1 | 2 |
|---|---|---|---|---|
| 1 | **Question answerable** | Names a topic, or an activity to perform | A question, but no result could have made it false | A stranger can say what result would have refuted it, and who was waiting on the answer |
| 2 | **Box reported both ways** | Only the word timeboxed, or an allotment with no spend | Both figures are present, but an overrun or an early finish is left unexplained | Allotted and spent are both there, and where they differ the document says what happened |
| 3 | **Non-scope is explicit** | Nothing says what was left alone | An exclusion is named, but a branch abandoned partway is not | A reader can name what was deliberately not attempted, including anything dropped mid-investigation, and the signal that stopped it |
| 4 | **Method reproducible** | Approaches or vendors named with no versions, data or commands | Enough detail to guess at the approach, not enough to repeat it | A colleague could re-run it from what is written: versions, environment and data pinned, and any evidence reused from earlier work flagged as reused |
| 5 | **Facts apart from inference** | Observation and interpretation share the same sentences | Separated by heading, but at least one inference is still stated as an observation | Every claim is visibly one or the other, and the confidence in an interpretive step is stated wherever it is not obvious |
| 6 | **Retractions in place** | An earlier finding changed and nothing in the document says so | A correction is mentioned, but the superseded claim has been deleted | Anything that turned out wrong is marked where it stood, saying what changed, so a reader can tell which conclusions moved and which never did |
| 7 | **Verdict is explicit** | The reader has to infer it from tone | Proceed or stop is stated, but nothing says what it rests on | The first line says proceed, do not proceed, or names the next spike, and any condition is written so a reader knows what would flip it |
| 8 | **Boundary written down** | The section is empty, or marked N/A on a spike that got an answer | It lists what the team plans to do next | It names what a reader must not conclude, and the dataset, version or platform the answer was actually measured on |
| 9 | **Askable later** | No investigator, no contact, no date | A team is named rather than a person | A person, a way to reach them, a date and a stable identifier, so a later document can cite this instead of paraphrasing it |

The test behind every cell above: **could someone satisfy it without improving the document?** A row that
counted findings, or counted exclusions, would reward padding, and five bulleted things nobody looked at
would score the same as one honest sentence. Every cell instead asks whether a specific piece of evidence
exists and whether a second person, not the author, could find it.

## Named anti-patterns (the usual wrecks)

1. **The ADR with a longer preamble.** The sharpest failure for this type, and the easiest to commit. The
   verdict was reached before the box opened and the evidence sections exist to justify it; the tell is a
   Recommendation you could have written on day zero. If the decision is genuinely already made, write an
   [ADR](../adr/adr_guide.md) and stop pretending the investigation was open.
2. **The recommendation with no working.** A verdict is there, and What Was Tried is missing, vague or
   unrepeatable, so nobody can check the reasoning that produced it. This is the cost Microsoft's playbook is
   warning about when it argues *"The goal of a spike should be fact-finding, not decision-making or
   recommendation."* This template keeps the Recommendation section deliberately, and this anti-pattern is
   the price of keeping it.
3. **The unanswerable question.** A spike aimed at a topic rather than a question. The box expires, the
   report describes the terrain, and nothing is decided. Three questions is three spikes; a question no
   evidence could refute is a research project that a time box will not rescue.
4. **The silently dropped branch.** You abandoned a promising approach at hour three and never mentioned it,
   so the next team spends their whole box rediscovering that it does not work. You stopped for a reason, and
   the reason is evidence. It belongs beside the budget that forced it.
5. **Findings with no anchor.** No counts, no versions, no commands, no file references. A reader who
   disagrees has nothing to check, so the disagreement gets settled by seniority rather than by evidence, and
   the report has become an opinion with formatting.
6. **The bounded answer with no boundary.** The result held on one dataset, one version and one platform, and
   the report never said so, so the next reader takes a narrow answer as a general one. An empty What This
   Does Not Settle on a spike that believes it answered its question is worth a second look before you
   accept it as clean. Why that section is here at all, and the three caveats that travel with the evidence
   behind it, are in [companion section 6](spike-report_companion.md#6-debates-and-contested-boundaries).

## Pairing with a skill

`pairs_with: [develop-spike-summary]`. The skill documents a completed spike, and it draws the same boundary
this card does: it sends you to `develop-adr` for the architecture decision the spike informs, and to
`discover-interview-synthesis` when the exploration was user research rather than technical feasibility. That
agreement is worth noticing, because it is one edge two independently built artifacts describe the same way.

**Be aware that the two shapes differ.** The skill's description names the four things it captures - the
original question, the approach, evidence-backed findings, and a proceed-or-not recommendation - and this
template keeps all four. **What its own output template looks like is not recorded in this bundle's
research**, so no claim is made here about its section list; if you are moving content between the two,
read the skill and compare for yourself. The difference worth knowing in advance is the one this
template is opinionated about:

- **The time box.** The skill makes documenting allocated against actual time its own instruction step. This
  bundle folds the same content into **Scope and Time Box**, on the evidence that a dedicated time-box
  heading belongs to pre-spike planning artifacts rather than to the report of a completed spike.
- **Open questions and follow-ups are two sections there, and one here.** This bundle ships **What This Does
  Not Settle** and deliberately keeps it out of roadmap territory. The open questions transfer; the
  follow-up items mostly belong somewhere else, in the backlog rather than in this document.
- **Neither shape asks what was deliberately not attempted.** The skill has no non-scope section, which is
  exactly consistent with this bundle's research: not one blank template found asks for one, and the good
  filled reports supply it anyway. That half of **Scope and Time Box** is content you will have to write
  without prompting from either tool.
