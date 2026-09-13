---
title: "{{title}}"
spike_id: "{{spike_id}}"
status: "{{status}}"
conducted_by: ["{{investigator_and_contact}}"]
date: "{{date}}"
work_item: "{{work_item_link}}"
doc_type: spike-report
size: lean
source_template: spike-report
source_template_version: 0.1.0
---

<!--
LEAN SPIKE REPORT. This bundle ships one size, and the evidence for that is unusually clean: no source
read for this bundle publishes two weights of a spike report, and the one named source that publishes
the document at all ships exactly one template. A document whose ceremony costs a meaningful fraction
of the investigation that produced it has inverted the point of the practice (this bundle's judgment,
not a sourced claim). See spike-report_companion.md section 4 (Variants and sizing).

READ THIS BEFORE YOU FILL IT IN, BECAUSE IT CHANGES WHAT THIS TEMPLATE CLAIMS.
The term's own inventors describe a spike's output as throwaway code, not a document. Ward
Cunningham's founding account, crediting Kent Beck with the name, says plainly: "We plan to throw away
the code, although sometimes something is salvaged." Mike Cohn describes an activity, not an artifact.
Exactly one named source found in this bundle's research pass publishes the spike's deliverable as a
written document, Microsoft's Code with Engineering Playbook: "Generally the deliverable from a
Technical Spike should be a document detailing what was evaluated and the outcome of that evaluation."
So this template does not tell you that writing up your spike is settled practice, because the
evidence does not support that sentence. It gives you a good shape for the write-up if you are doing
one. See spike-report_companion.md sections 1, 2 and 6.1 for the full argument and its sources.

THIS IS NOT AN ADR, AND THAT DRIFT IS THE EASIEST MISTAKE TO MAKE HERE.
A spike report that recommends without recording what was tried is a bad ADR; an ADR that shows its
working is not a spike report. This document investigates the question that precedes the decision: it
hands over evidence and a proceed-or-not recommendation, and it does not propose, decide, or design.
If the decision is genuinely already made and you are writing this to show your working, write an ADR
and stop. See spike-report_companion.md sections 7 and 8.

WHERE THIS FILE GOES: wherever your team keeps them. This bundle prescribes no location, and it does
not assume a file at all. One real published process (GitLab's) has none: the spike issue is the
artifact, closed out with a single summary comment carrying the learnings and the recommended paths.
If that is your culture, use the six sections below as the shape of that comment rather than fighting
for a file. See spike-report_companion.md section 9 (Adaptations).

STATUS is a short vocabulary, and there is no third state that means "gave up":
  in-progress -> complete      the box closes whether or not the question was answered
  complete -> superseded       once the decision this fed is recorded, the report is history
A spike whose box expired without an answer is still complete. Write the report anyway and make the
Recommendation a named next spike with a narrower question.

FRONTMATTER: name a person and a way to reach them, not a team. A spike report generates questions,
and a report nobody can be asked about decays into an assertion. The stable id and the date are what
let a later design doc or ADR cite this by name instead of by memory. See
spike-report_companion.md section 3 (Anatomy > Frontmatter and status).

HOW TO FILL THIS IN
1. Read the comment under each heading: WHAT it wants, WHY it matters (with a pointer into
   spike-report_companion.md for the deep reasoning), guiding questions to ASK, a GOOD and a WEAK
   example, and the TRAP to avoid.
2. Replace each {{placeholder}} with your content.
3. If a section does not apply, write "N/A" and one line of why, rather than deleting it.
4. Before you ship it: self-grade against spike-report_guide.md, then DELETE every HTML comment. They
   are guidance, not content.
-->

# {{title}}

<!-- WHAT  A title naming the question the spike went after and, where you can, the answer it came
           back with. A statement, not a topic.
     WHY   These are read later, by someone deciding whether your box already answered their
           question before they spend theirs. A title naming the area rather than the question makes
           them read the whole document to find out.
           Deep dive: spike-report_companion.md section 3 (Anatomy > Frontmatter and status).
     ASK   What was the one uncertainty? What did the box come back with? Scanning a folder of these
           six months from now, would a stranger know whether to open this one?
     GOOD  "Hosted OCR reads our supplier invoice headers well enough to drop manual entry, and does
           not read line items"
     WEAK  "OCR investigation" (names the area, not the question, and carries no answer)
     TRAP  Titling the technology instead of the question. "Vendor X evaluation" tells a reader
           nothing about what was asked or what came back, and ages into a filename nobody opens. -->

## The Question

<!-- WHAT  The single uncertainty this spike existed to reduce, written so evidence can answer it yes
           or no. One question. Three questions is three spikes, or a research project.
     WHY   The question is what makes the box meaningful: it is what the box was spent on, and it is
           what a reader checks the findings against. A spike aimed at a topic rather than a question
           ends with the terrain described and nothing decided, which is one of the named failure
           modes for this format.
           Deep dive: spike-report_companion.md section 3 (Anatomy > 1. The Question).
     ASK   What one thing did we not know? Who is waiting on the answer and what will they do with
           it? Could the evidence have come back "no"? Was this written before the work started?
     GOOD  "Can a hosted OCR service extract supplier, invoice number, date and line-item totals from
           our scanned supplier invoices accurately enough for finance to stop keying them by hand?
           The answer goes to AP operations, who will either schedule the integration this quarter or
           renew the data-entry contract for another year."
     WEAK  "Investigate OCR options for invoice processing." (a topic and an activity, not a
           question; no evidence could make it false, so the box cannot close on an answer)
     TRAP  Writing the question after the findings, shaped to the answer you got. State it as
           something the evidence is allowed to kill. A refuted hypothesis is a successful spike; a
           question that cannot be refuted is not a spike question, and the box will not save it. -->

{{the_question}}

## Scope and Time Box

<!-- WHAT  Three things: what the investigation was allotted, what it actually spent, and what was
           deliberately not attempted. All three, including the branch you abandoned partway.
     WHY   The box is what separates a spike from open exploration, and reporting it honestly in both
           directions is information: overrunning says one thing, finishing in half a day says
           another. The non-scope half sits here rather than under What Was Tried because what you
           chose not to try is a scope decision, and it reads best beside the budget that forced it.
           This bundle folds the time box into this section instead of giving it its own heading, and
           that is a departure argued from evidence rather than taste: a dedicated time-box heading
           turns out to live in pre-spike planning artifacts (a ticket field, a plan's deadline) and
           to be usually absent from the report of a completed spike.
           Deep dive: spike-report_companion.md section 3 (Anatomy > 2. Scope and Time Box), which
           carries the evidence for that departure.
     ASK   What was the box, and agreed with whom? What did it actually cost? What did we choose not
           to look at, and why? What did we abandon partway, at what point, and on what signal?
     GOOD  "Allotted: three days, agreed at sprint planning. Spent: two days. Vendor B's trial tier
           rate-limited us on day two and we cut its evaluation short rather than buy a larger key.
           Deliberately not attempted: handwritten annotations on delivery notes, which are a
           separate workflow and were excluded by agreement; and self-hosting an open-source model,
           which we stopped at hour four once the first run needed a GPU the AP environment does not
           have, so the shape was unusable before it got interesting."
     WEAK  "Timeboxed to a sprint." (no actual spend and no scope boundary; the reader learns only
           that a box was mentioned once)
     TRAP  Silently dropping the branch you abandoned. You gave up on it for a reason, and that
           reason is evidence. Leave it out and the next team spends their whole box rediscovering
           that it does not work. -->

* Allotted: {{time_allotted}}
* Spent: {{time_spent}}
* Deliberately not attempted: {{not_attempted}}

## What Was Tried

<!-- WHAT  The approach: what you built, ran, measured or read, in enough detail that a colleague
           could repeat it and get the same result. Pin the versions, the environment and the data.
     WHY   This is the section that separates a spike report from an opinion. Repeatability is what
           lets a reader disagree with your conclusion by checking your work rather than by trading
           intuitions, and the one named source that publishes this document makes repeatability an
           explicit property of it.
           Deep dive: spike-report_companion.md section 3 (Anatomy > 3. What Was Tried).
     ASK   What exactly did we run, on what data, at which versions? What would a colleague need to
           reproduce it? What did we reuse from earlier work rather than re-run, and why is that
           still valid?
     GOOD  "Sampled 200 invoices from last quarter, stratified across our five highest-volume
           suppliers. Ran each through vendor A's document API (v3, eu-west endpoint, default invoice
           model) and vendor B's (v2024.2, trial tier). Scored extraction field by field against the
           values already keyed into the ledger. Scoring script and sample manifest are in
           spikes/ocr/, commit 4f1c9ab. Vendor B's numbers cover 60 invoices only, for the
           rate-limit reason above."
     WEAK  "Tried a couple of OCR services and compared the results." (nothing named, nothing
           versioned, no data described; a second person cannot repeat any of it)
     TRAP  Reusing evidence from an earlier spike without saying so. Reusing it is legitimate;
           reusing it silently makes a stale measurement look fresh and hides the version it was
           actually taken on. -->

{{what_was_tried}}

## What Was Found

<!-- WHAT  The evidence, with the facts you observed kept visibly apart from what you think they
           imply. Anchor every fact to something a reader can open: a count, a command, a file and
           line, a version.
     WHY   That separation is this document's whole defence. An observation and an inference read
           identically in prose, and once they are blended a reader cannot tell which parts survive
           if your interpretation turns out to be wrong. The one named source that publishes this
           document argues the goal of a spike is fact-finding rather than decision-making or
           recommendation; this template keeps a Recommendation section anyway, and the separation
           here is what pays for that.
           Deep dive: spike-report_companion.md section 3 (Anatomy > 4. What Was Found).
     ASK   What did we actually observe, in numbers or output? What does each observation imply, and
           how confident are we in that step? What surprised us? Did anything we wrote earlier turn
           out to be wrong, and did we mark it or quietly edit it away?
     GOOD  "Observed: header fields (supplier, invoice number, date, total) correct on 197 of 200
           invoices for vendor A; line-item totals correct on 138 of 200. All 62 line-item failures
           were invoices carrying handwritten corrections in the line-item block, or a scan skew
           above roughly 5 degrees.
           Implies: header automation is viable now for the three suppliers who send clean PDFs;
           line-item automation is not, and because the failure mode is input quality rather than the
           model, a different vendor is unlikely to move it much. Confidence: high on the header
           count, medium on the skew threshold, which we eyeballed rather than measured."
     WEAK  "OCR worked well for most invoices but struggled with the messier ones, so it looks
           promising." (no counts, no anchor, and observation and inference are the same sentence)
     TRAP  Deleting a finding that turned out to be wrong instead of marking it. Track the retraction
           in place, saying what changed and when, so a later reader can tell which conclusions moved
           and which never did. A quietly edited report cannot be trusted on the parts that held. -->

* Observed: {{observed_facts}}
* Which implies: {{what_it_implies}}

## Recommendation

<!-- WHAT  Proceed, do not proceed, or a named next spike with a narrower question. The verdict in
           the first line, in words, followed by the reasoning and any condition it depends on.
     WHY   An investigator who spent the box and will not say what they now believe has pushed the
           hardest part of the work onto a reader with less context who was not there. Worth knowing
           as you write it: the single named source that publishes this document argues the opposite,
           that a spike should be fact-finding rather than recommendation. This template keeps the
           section deliberately, and it pays for it with the trap below.
           Deep dive: spike-report_companion.md section 6.2 (Fact-finding or recommendation?) for
           both sides of that, and section 3 (Anatomy > 5. Recommendation) for how to write one.
     ASK   Proceed, stop, or spike again? Under what condition, and what would flip it? Who decides,
           and what do they need that is not in this document? Was the decision rule written down
           before the results came in?
     GOOD  "Proceed, narrowly. Automate header extraction with vendor A for the three suppliers who
           send clean PDFs, about 60 percent of monthly volume, and keep manual entry for the rest.
           Conditional on the eu-west endpoint clearing the data-residency review already open with
           legal. If that comes back no, this becomes a do-not-proceed, not a smaller version of the
           same plan."
     WEAK  "The results were encouraging and we think this is worth pursuing further." (no verdict a
           reader can act on, no condition, and "further" names nothing)
     TRAP  Writing this section first. A verdict reached before the box opened turns the evidence
           sections into a preamble that justifies it, and that document is an ADR wearing a spike
           report's headings. A conditional recommendation can be more honest than a clean one; a
           recommendation invented after the evidence arrived is hard to tell from a preference. -->

**{{verdict}}** - {{recommendation_detail}}

## What This Does Not Settle

<!-- WHAT  The open questions this spike did not close, and what a reader must not conclude from it.
           What you would still not bet on. Then stop: this is not a roadmap.
     WHY   A spike buys a bounded answer, and the boundary is part of the answer. Without it the next
           reader takes a result that held on one dataset, one version and one platform as a general
           one. This section is a deliberate departure from the four-part shape (question, approach,
           findings, recommendation), argued from research rather than taste: real filled spike
           reports supply an explicit non-scope statement under four different headings across four
           unrelated projects, and not one blank template found asks for it. Three caveats travel
           with that finding and it should not be quoted without them.
           Deep dive: spike-report_companion.md section 3 (Anatomy > 6. What This Does Not Settle),
           and section 6.4 for exactly what that finding does and does not establish.
     ASK   What would we still not bet on? What did we measure on one dataset, one version or one
           platform that may not generalise? What question is sharper now but still open? What might
           a reader wrongly conclude from this document?
     GOOD  "Nothing here covers credit notes or multi-currency invoices; the sample contained none.
           The 197 of 200 header figure is measured on last quarter's suppliers, two of whom are
           mid-migration to a billing system that will change their layouts. Cost at production
           volume is unknown: we ran 260 documents on trial pricing and never reached a tiered rate.
           And we did not test what happens when extraction is confidently wrong rather than
           visibly failing, which is the risk finance actually cares about."
     WEAK  "Next steps: evaluate pricing, test credit notes, book a follow-up with finance." (a
           to-do list, not a boundary; it says what you plan to do, not what your answer fails to
           cover)
     TRAP  Turning this into a roadmap, or leaving it empty because the spike "answered the
           question". A report that gives its answer but not the edge of its answer is the failure
           this whole format exists to prevent, and an empty section here is worth a second look
           before you accept it as clean. -->

* Still open: {{open_questions}}
* Do not conclude from this: {{what_this_does_not_show}}
