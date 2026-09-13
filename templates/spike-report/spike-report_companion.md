# Companion: The Spike Report

> The deep explainer for the spike-report bundle. Read this to understand what a spike report is,
> where the practice came from, why the term's own inventors would not have written one, and where
> practitioners still disagree about it. The short operator card is
> [`spike-report_guide.md`](spike-report_guide.md); a fully worked instance is
> [`spike-report_example.md`](spike-report_example.md). Inline citations like [[1]](#ref-1) resolve
> to the [References](#references) at the bottom, tagged by source reliability.

---

## 1. Orientation

A spike report is the written output of a **time-boxed investigation**: one uncertainty, a bounded
amount of effort spent on it, what was actually tried, what was actually found, and a recommendation
the next reader can act on. Its job is to let a decision be made on evidence someone else can check,
instead of on the recollection of whoever did the digging.

**Start with the honest part, because it changes how you should read everything after it.** This is
the one document type in this library whose own canon argues against writing it. The term comes from
Extreme Programming, and in the XP literature a spike produces **code you throw away**, not a
document. Ward Cunningham's account, crediting Kent Beck with the name, describes writing *"the
smallest possible code that could be said to perform a function independent of existing mechanism"*
and adds, plainly, *"We plan to throw away the code, although sometimes something is salvaged"*
[[1]](#ref-1). Mike Cohn describes an activity, not an artifact [[8]](#ref-8). Exactly one named
source, in a fan-out of 72 records merged to 68 unique sources, publishes the spike's deliverable as a
written document:
Microsoft's Code with Engineering Playbook, which states that *"Generally the deliverable from a
Technical Spike should be a document detailing what was evaluated and the outcome of that
evaluation"* [[10]](#ref-10) and ships a fill-in template to match [[11]](#ref-11).

So this bundle has an unusual obligation, set deliberately in
[ADR 0048](../../docs/internal/decisions/0048-one-named-source-clears-the-admission-test.md): **teach
the dispute, do not resolve it.** Nothing here will tell you that writing up your spike is settled
practice, because the evidence does not support that sentence.

**At a glance**
- The load-bearing sections are **What Was Found** and **What This Does Not Settle.** A spike that
  reports only its answer, and not the edge of its answer, is the failure mode this format exists
  to prevent.
- It is **bounded by construction.** The box closes whether or not the question was answered, which
  is exactly why over-claiming is the natural temptation here [[9]](#ref-9).
- It **investigates**; it does not decide. Its three siblings propose, record, and describe
  (see [section 8](#8-relationships-to-other-artifacts)).
- The easiest way to write it badly is to let it **drift into an ADR with a longer preamble.** A
  spike report that recommends without recording what was tried is a bad ADR; an ADR that shows its
  working is not a spike report.
- Its own canon would tell you to throw the code away and skip the write-up. That is not a reason to
  hide the canon; it is one of the more interesting things this document type has to teach.

If you read nothing else: a spike report is **a bounded answer with its boundary written down.**

---

## 2. Origins and evolution

### The name, and what it originally named

The practice is an Extreme Programming invention, and its origin is an exchange between two people.
In Cunningham's own telling on the c2 wiki, *"I would often ask Kent, 'What is the simplest thing we
can program that will convince us we are on the right track?'"*, and *"Such stepping outside the
difficulties at hand often led us to simpler and more compelling solutions"*; then, in four words
that named the practice for the next thirty years, *"Kent dubbed this a Spike"* [[1]](#ref-1)[[2]](#ref-2).
The metaphor is geometric, not violent: *"'Spike' because TopDown is typically BreadthFirst, but a
Spike is DepthFirst"*, and *"So-called because a spike is 'end to end, but very thin', like driving a
spike all the way through a log"* [[2]](#ref-2). The practice traces to the Chrysler C3 project of the
mid-to-late 1990s; the log's own entries differ on which, so this bundle does not pick one
[[1]](#ref-1)[[3]](#ref-3). In the XP canon proper, a spike appears as a risk-reduction coding technique
and nothing else: the team identifies the risky stories and *"does WorstThingsFirst based on a
SpikeSolution"* [[4]](#ref-4).

**The output was code, and it was expected to be discarded.** Cunningham's page says so [[1]](#ref-1).
Don Wells' ExtremeProgramming.org rules page says *"A spike solution is a very simple program to explore potential solutions"*, that you should
*"Build the spike to only addresses the problem under examination and ignore all other concerns"*,
and that *"Most spikes are not good enough to keep, so expect to throw it away"* [[5]](#ref-5). It
contains no report format, no section list, and no suggestion that anything be written down. Neither
does Cunningham's. **The strongest evidence about spike documentation in the founding literature is
its complete absence.** That absence persists downstream: practitioner write-ups explaining how to
spot a spike in a plan still prescribe no documentation, mentioning the box only informally inside a
worked example, *"you timebox it for 2 hours"* [[50]](#ref-50).

### The time box, and the rule the page states

The discipline that makes a spike a spike is the box, and it arrives on the same c2 page - which is
signed by five contributors, so the lines below are the page's rather than any one author's: *"We like
a spike solution to take no more than a couple of days, and a half day is ideal"*, alongside the condition that tells you when to reach for one at all,
*"Spikes are good when you are knowledge-limited, not time-limited"* [[3]](#ref-3). Wells is more
generous for the hard cases, advising a team to *"put a pair of developers on the problem for a week
or two and reduce the potential risk"* [[5]](#ref-5).

### The disagreement is original, not later

It is worth knowing that the canon was never unanimous even about the code. On the same c2 page, the
throw-it-away position is contested by Eric Newhuis, who argues for keeping spike code and integrating
it into the build, and softened by Katy Mulvey, who reads *"throw away"* as a scale instruction rather
than a mandate to delete [[3]](#ref-3). (That reading of Mulvey is the research log's own gloss on her
position, not a phrase she is recorded as writing.) James Shore and Shane Warden carried the
definition essentially unchanged into a 2007-era practitioner reference, and their formulation is the
closest the canon comes to sanctioning an artifact: a spike is *"a technical investigation... a small
experiment to research the answer to a problem"*, and *"When you finish, throw it away, check it in as
documentation, or share it with your colleagues, but don't treat it as anything other than an
experiment"* [[6]](#ref-6). That is permission to keep something, not a template for it.

Even the tidy origin story is disputed. John Clapham challenges the neat Cunningham-asked-Beck-named-it
narrative and notes that Beck himself later moved away from the word: *"Because people variously
associate 'spike' with volleyball, railroads, or dogs, I have begun using 'architectural prototype' to
describe this implementation."* Clapham's conclusion is that *"it is entirely possible that little
thought was given to the term, the wrong word was used, it is an in joke, or that the reference is
something only the author would understand"* [[7]](#ref-7).

### The formalisation layer, which is where a document first appears

What happened next is the story of a lightweight coding technique being absorbed into heavier process
machinery.

**Scrum never adopted it.** The full text of the 2020 Scrum Guide was read and the word *spike* does
not appear anywhere in it [[14]](#ref-14). Scrum Alliance's own 2014 commentary credits XP as the
origin and frames the practice as supplementary and exceptional, while simultaneously folding it into
ordinary story accounting: *"Spikes are an invention of Extreme Programming (XP), are a special type
of story that is used to drive out risk and uncertainty"*, *"Spikes, by definition, have a maximum
time-box size of one sprint"*, and *"Use a spike as a last option"* [[15]](#ref-15).

**SAFe routinised it.** SAFe defines spikes as Enabler Stories that *"represent activities such as
exploration, architecture, infrastructure, research, design, and prototyping"* and that, *"Like other
stories... are estimated, implemented and demonstrated"* [[12]](#ref-12). Being demonstrated and
accepted implies something inspectable, but the publicly readable SAFe text never uses the words
*document* or *report*, and the deeper material is behind a login, so nothing here rests on SAFe for
the artifact. Its spike material is current rather than legacy: the sibling Enablers page carries its
own *"Last Update: 24 February 2025"* stamp, and spikes are not a fifth Enabler category but a
technique cutting across the four [[13]](#ref-13).

**Microsoft published the document.** The Code with Engineering Playbook is the single source that
closes the gap, and it does so without citing or reconciling the XP origin it contradicts: the
deliverable *"should be a document detailing what was evaluated and the outcome of that evaluation"*,
structured with a problem statement and goals, a repeatability requirement, evidence carried in
appendices, and *"Generally sections towards the beginning of the document should summarize data and
use one or more appendices for more details"* [[10]](#ref-10). A matching fill-in template ships
beside it, asking for the investigator and a link to the originating work item [[11]](#ref-11).

**Below that, a large secondary layer repeats the doctrine without a source.** Training-vendor and
SEO content routinely asserts that a spike's output is a documented finding, a decision record, or an
architecture recommendation; traced back, that phrasing resolves to content marketing rather than to
SAFe or to any notable named practitioner [[25]](#ref-25). Smaller coaching pages list a decision
record among spike outputs without naming a document type or showing a template [[26]](#ref-26).
**None of that layer supports anything in this bundle**, and it is named here so you can recognise it
when you meet it.

**The honest summary of the lineage, in one sentence:** the spike report is a **later enterprise
formalisation of an XP practice whose inventors described its output as throwaway code**.

---

## 3. Anatomy (section by section)

### Frontmatter and status

The YAML block carries the document's identity and the provenance fields this library requires of
every filled instance (`source_template`, `source_template_version`), plus a title, a date, and who
conducted the investigation.

*Beginner note:* name a person, not a team. Microsoft's template asks for *"Names and at least one
email address for follow-up questions"* [[11]](#ref-11), and the reason is practical: a spike report
generates questions, and a report nobody can be asked about decays into an assertion.

*Expert note:* a stable identifier and a date turn the report into something citable. A real design
document in the wild opens by naming its source precisely, *"Condensed from the AT spike report
(gt-3nqoz, 2026-02-08, author: nux)"* [[35]](#ref-35), and a real specification resolves five separate
open questions by pointing at one spike report's named sub-sections [[30]](#ref-30). Some teams go
further and carry machine-readable self-assessment in frontmatter, `confidence`, `evidence_grade` and
`review_state` [[36]](#ref-36). This template does not ask for those; if your organisation reads spike
reports at volume, they are worth stealing.

### 1. The Question

The single uncertainty the spike exists to reduce, written so it can be answered yes or no.

*Beginner note:* write it before you start, and write it narrow. Cohn's framing is that a spike is
*"a time-boxed research activity that helps teams make better decisions"* [[8]](#ref-8); Giora Morein
puts the same discipline in the singular, *"A spike is a time-boxed research experiment that answers
one specific question fast"* [[21]](#ref-21). Andrew Fuqua's house rules are the sharpest version:
each spike *"must have one explicit question to answer, we must know who the answer goes to, and there
must be a 'demo'"* [[18]](#ref-18).

*Expert note:* a question that cannot be answered false is not a spike question, it is a research
project, and the time box will not save you from it. The strongest filled reports read for this
bundle's research state the question as a hypothesis and then let the evidence kill it: one declares
*"The hypothesised `summary` record does not exist"* and follows with *"The charter's
compaction-summary theory is refuted"* [[42]](#ref-42). A refuted hypothesis is a successful spike.
If your question cannot produce that outcome, sharpen it before you spend the box.

### 2. Scope and Time Box

What the investigation was allotted, what it actually spent, and, explicitly, **what was deliberately
not attempted**.

*Beginner note:* record the box honestly in both directions. Overrunning it is information; so is
finishing early. What happens when the box closes on an unanswered question is **not settled by any
source this research retrieved**: Cohn describes a spike only as *"a time-boxed research activity that
helps teams make better decisions"* [[8]](#ref-8) and says nothing, in anything logged here, about
what the expiry of that box obliges. Treating the end of the box as a checkpoint rather than a
guillotine is this bundle's own recommendation, argued in section 9, not a practice anyone read. Morein says the same thing shorter: *"If you need more time, that's a new conversation
with the team"* [[21]](#ref-21).

*Expert note, and a departure this bundle owes you an explanation for.* This bundle's own
[specification](../../docs/internal/tier2-specs.md) originally gave **Time Box** its own top-level
section. The research overturned that and it is folded in here instead, because a dedicated time-box
heading turns out to live in **pre-spike planning** artifacts, not in the report of a completed spike:
it is a titled field on a Jira spike ticket alongside `PROBLEM`, `SCOPE` and `ACCEPTANCE CRITERIA`
[[47]](#ref-47), and it is a `Planned start date` and `Deadline` on a spike *plan* template whose
companion *outcome* template has no time-box section at all [[46]](#ref-46)[[45]](#ref-45). Across the
filled reports read, exactly one records time actually spent, under a *"Time Spent (Task by Task)"*
heading that is itself hedged as *"(Estimated time spent during the spike phase)"* [[41]](#ref-41).
The box governs the investigation; the report says what it cost. One heading, not two.

*Why the non-scope half sits here rather than in What Was Tried:* what you chose not to try is a
scope decision, and it is more useful to a reader beside the budget that forced it. A real spike on a
production Electron client keeps this explicit under *"Out of scope for this spike"* and preserves an
entire unexecuted fallback design rather than deleting it: *"Not run. Phase 1 succeeded, so the
spike's fallback path ... is not needed"* [[31]](#ref-31).

### 3. What Was Tried

The approach: what you built, ran, measured or read, in enough detail that someone else could repeat
it.

*Beginner note:* this is the section that separates a spike report from an opinion. Pin the
environment. A real spike heads its results *"Findings (macOS/arm64, Zig 0.16.0)"* [[32]](#ref-32),
because a finding without a version is a finding with an expiry date you cannot see. Microsoft's
playbook makes repeatability an explicit property of the document [[10]](#ref-10).

*Expert note:* anchor claims to something a reader can open. The strongest examples cite file and
line (`packages/server/review.ts:219`) [[37]](#ref-37) or paste the command and its result, as in a
test run reported as *9/9* [[34]](#ref-34). The other half of rigour is saying what you did **not**
re-run and why: one report in a spike series records *"No additional model runs were performed. The
SPIKE-006 improved prompt subsumes SPIKE-004's prompt, so SPIKE-006 results serve as the
post-improvement validation run"* [[40]](#ref-40). Reusing prior evidence is legitimate; reusing it
silently is not.

### 4. What Was Found

The evidence, with facts kept separate from what they imply.

*Beginner note:* write the observation first and the interpretation second, and keep them visibly
apart. Microsoft states the principle as a goal for the whole document: *"The goal of a spike should
be fact-finding, not decision-making or recommendation"* [[10]](#ref-10). This template keeps a
Recommendation section anyway, for reasons argued in
[section 6.2](#62-fact-finding-or-recommendation) - but the separation inside this section is exactly
what that quote is protecting.

*Expert note:* three moves from the filled corpus are worth copying. **Report the misleading number
next to the honest one:** one report gives a naive topline alongside the correctly segmented figure
and tells the reader which to trust, *"The segmented 87.2% figure is the one that matters"*
[[42]](#ref-42). **Preserve retractions rather than editing them away:** another carries a tracked
correction in place, *"Retracted (CHWIN-09, v0.1.1): the gadget inventory above is accurate, but this
is NOT a success-path demo"*, and reframes the negative result honestly as a system *"failing
cleanly"* [[39]](#ref-39). **Treat absence as evidence, carefully:** *"The absence of prior art is a
yellow flag"* [[31]](#ref-31) is a finding, provided you say it is an inference.

### 5. Recommendation

Proceed, do not proceed, or a named next spike. Explicit, never left to be inferred from tone.

*Beginner note:* say the words. The good filled reports do not hedge the verdict: *"Recommendation:
CONDITIONAL GO for Phase 1 experiment"* with the scoring that produced it, *"5/8 clear GO. 2 require
workarounds (viable mitigations). 1 conditional on Phase 1 cost validation"* [[35]](#ref-35);
*"Recommendation: adopt in narrow slices, gated on Effect v4 stable"* [[34]](#ref-34). GitLab's
handbook asks its engineers for exactly this in the spike issue, *"detailed learnings of your
investigation and recommended path(s) for the solution"*, plus *"an outline of the recommended next
step issues and/or epics"* [[27]](#ref-27).

*Expert note:* a conditional recommendation can be more honest than a clean one, and the good
examples are full of them. *"Technically de-risked; not forced"* [[36]](#ref-36) tells a reader two
distinct things: the risk is gone, and the decision is still theirs. Pre-registering the decision
rule before you look at the results is stronger still, whether as an if-this-then-that tree
(*"If Phase 1 works: proceed with renderer-only implementation"* [[31]](#ref-31)) or as scored
criteria with a pivot already written for the failure case [[40]](#ref-40). A recommendation invented
after the evidence arrived is hard to distinguish from a preference.

### 6. What This Does Not Settle

The open questions the spike did not close, so the next reader does not mistake a bounded answer for
a general one.

*Beginner note:* list what you would still not bet on, and what a reader must not conclude from this
document. Then stop; this is not a roadmap.

*Expert note, and the evidence for this section arrived by an unusual route.* This section
is a deliberate departure from the four-part shape (question, approach, findings, recommendation) that
the paired skill uses, and the departure was argued from research rather than taste.
The **blinded gap dimension** of this bundle's research, which never saw the planned section list,
found that an explicit, named non-scope statement is **the single most consistent element that real
filled spike reports supply and a naive four-part shape omits** - present under four different
headings across four unrelated projects: *"Out of scope for this spike"* [[31]](#ref-31),
*"Non-goals for now"* [[34]](#ref-34), *"Not covered here"* [[32]](#ref-32), and *"Follow-ups
(deferred, not in v1)"* kept distinct from a separate *Limitations* section [[33]](#ref-33).
Meanwhile the structure dimension found that **not one blank template asks for it.** The closest a
template comes is an optional *"Open issues/risks"* heading framed as unresolved risk rather than
scope exclusion [[45]](#ref-45). Every template omits it; the good filled reports include it anyway.
Full evidence is in [`spike-report_research-log.md`](spike-report_research-log.md).

**Three caveats travel with that finding and must not be dropped.**

1. **Selection bias.** The filled corpus was found by code search for structural headers, which
   pre-selects for reports that already have structure. Searches of engineering blogs and government
   publishing returned templates and process descriptions but never a filled instance.
2. **Provenance.** A large share of that corpus shows signs of AI-agent-assisted or agent-authored
   drafting. An element recurring across agent-drafted documents is weaker evidence about human
   practice than a raw count suggests.
3. **Genre.** Real write-ups split three ways - human blank templates, AI-coding-agent workflow
   templates, and filled examples - and pooling them into one frequency count overstates the
   evidence.

And a clean negative instance exists: a well-structured real spike report with no out-of-scope
statement, no confidence rating, and no named decision-maker [[38]](#ref-38). This section is defended
by the evidence; it is not universal in practice, and this bundle does not claim it is.

---

## 4. Variants and sizing

**One size, `lean`, and the evidence is unusually clean on this point.** No source read for this
bundle publishes two weights of a spike report. The one named source that publishes the document
ships one template [[11]](#ref-11). The one general-purpose blank outcome template found ships one
shape, with individual sections marked optional rather than a second variant [[45]](#ref-45) - from a
repository built to *"generate new Spikes by reusing the existing Spike Plan and Spike Outcome
templates"*, whose author cites XP and SAFe as the two sources drawn on [[44]](#ref-44). GitLab
does not ship a document at all: the report **is** the tracking issue, closed out with a single
summary comment in which findings and recommendation are deliberately combined [[27]](#ref-27).

There is real variation in the wild, but it is variation across **genre**, not weight. The most
exhaustive templates found - one with seven top-level sections including an *"Investigation Log"*
[[48]](#ref-48), another defining two output documents and a one-hour hard cap [[49]](#ref-49) - are
both explicitly written for an AI coding agent to fill in, and their section counts should not be read
as typical of human practice. At the other end, a real filled engineering write-up uses no named
convention at all, just bespoke numbered headings driven by content and ending in a decision record
[[43]](#ref-43).

**The type's own discipline argues against a heavier variant.** A spike is bounded at a couple of days
at the canonical end [[3]](#ref-3), twelve hours at Fuqua's [[18]](#ref-18), one iteration at Scrum
Alliance's outer limit [[15]](#ref-15). A document whose ceremony costs a meaningful fraction of the
investigation that produced it has inverted the point of the practice. *(Author judgment: no source
read makes this argument directly; it follows from the time-box evidence above.)*

Single-size members of the `decision-docs` family are exempt from the nesting rule and from nothing
else; every other obligation in the [family contract](../../docs/internal/contracts/decision-docs.md)
applies unchanged.

---

## 5. Methodology lineage

Different schools treat this practice very differently, and the spread is the point rather than a
complication to smooth over.

| Tradition | What a spike produces | Is there a document? |
|---|---|---|
| **XP, Cunningham and Beck (c. mid-1990s)** | Thin, end-to-end, throwaway code | No. The canon prescribes none [[1]](#ref-1)[[2]](#ref-2)[[3]](#ref-3) |
| **XP rules, Wells (1999-era)** | A very simple program, expected to be discarded | No. Zero format guidance of any kind [[5]](#ref-5) |
| **Shore and Warden (2007-era)** | A disposable technical investigation | Optional at most: throw it away, keep it as documentation, or share it [[6]](#ref-6) |
| **Scrum (the Guide)** | Nothing. The word does not appear | No [[14]](#ref-14) |
| **Scrum Alliance (2014 commentary)** | A story-shaped exception, one sprint maximum, demonstrated | Implied acceptance, no artifact named [[15]](#ref-15) |
| **SAFe** | An Enabler Story, estimated, implemented and demonstrated | Implied, never stated in readable text [[12]](#ref-12)[[13]](#ref-13) |
| **Cohn / Mountain Goat** | Knowledge, from a time-boxed activity | No. An activity, not an artifact [[8]](#ref-8)[[9]](#ref-9) |
| **Microsoft CSE playbook** | A document, structured, with evidence in appendices | **Yes, explicitly, with a template** [[10]](#ref-10)[[11]](#ref-11) |
| **GitLab handbook** | A recommendation on technical direction rather than code | Yes, as one summary comment on the spike issue [[27]](#ref-27) |
| **Agile Alliance (Engel)** | Information, not a shippable product; do not story-point it | Not addressed [[16]](#ref-16) |

**Why this bundle teaches the written report, stated without overclaiming.** It ships the document
because this library's admission test asks whether *a named source publishes it as a written
document* and one does [[10]](#ref-10)[[11]](#ref-11), and because the research read eleven
real, filled spike reports in public repositories, so whatever the canon prescribes, people write
these. The reasoning is recorded in
[ADR 0048](../../docs/internal/decisions/0048-one-named-source-clears-the-admission-test.md). It does
**not** ship the document because the canon endorses it. The canon does not, and
[section 2](#2-origins-and-evolution) is where that is laid out rather than softened.

---

## 6. Debates and contested boundaries

### 6.1 Code or document? (the live one, and the reason this bundle exists)

This is not a matter of emphasis. It is a direct contradiction between the practice's inventors and
the one source that publishes its written form.

**Camp A: the output is code or knowledge, and there is no report.** Cunningham's c2 account, with
Beck credited for the name, describes throwaway code and no artifact [[1]](#ref-1)[[2]](#ref-2). Ron
Jeffries' contributions on the same page set the time box and the throw-away default [[3]](#ref-3).
Don Wells' rules page prescribes no report format whatsoever [[5]](#ref-5). Mike Cohn describes an
information-producing activity with no mention of a written summary or template
[[8]](#ref-8)[[9]](#ref-9). Shore and Warden allow that you might keep the code as documentation, but
warn against treating it as anything other than an experiment [[6]](#ref-6). **This is the canon, and
it is the origin.**

**Camp B: the output is a written deliverable.** Microsoft's Code with Engineering Playbook,
explicitly and with a template, verified against the raw markdown in its own repository
[[10]](#ref-10)[[11]](#ref-11). SAFe's Enabler Story framing implies something inspectable, but its
own accessible text stops short of the word *document* [[12]](#ref-12). GitLab's handbook requires a
written summary, though as an issue comment rather than a standalone file [[27]](#ref-27). Below
those sits the vendor layer that repeats the doctrine without a named source, and it carries nothing
here [[25]](#ref-25)[[26]](#ref-26).

**What this bundle does with that, stated carefully.** It does not adjudicate, and it is worth being
precise about what Camp A actually holds. The canon does not merely prefer that you discard the code;
it describes **no written artifact of any kind**, and the founding pages contain none. So the gap is
not a detail about disposal, and this bundle will not close it by observing that what a report records
is a different object from the prototype that produced it. That observation is available to you, but
no source read makes it, and offering it as the resolution would be this bundle putting words in the
canon's mouth.

What can honestly be said is narrower, and it is all of it: a named source publishes the document
[[10]](#ref-10)[[11]](#ref-11), eleven real filled spike reports were read in full in public
repositories, and the practice's inventors asked nobody to write one [[1]](#ref-1)[[5]](#ref-5). A
reader who concludes from this bundle that XP's inventors would approve has read it wrong. A reader
who concludes the artifact does not exist in practice has read sections 3 and 4 wrong. Hold both.

### 6.2 Fact-finding or recommendation?

**The one source that admits this document also argues against one of its sections.** Microsoft's
playbook states that *"The goal of a spike should be fact-finding, not decision-making or
recommendation"* [[10]](#ref-10). This template makes **Recommendation** a required section anyway.

The counter-evidence is the practice. GitLab asks its engineers for *"recommended path(s)"* in the
same breath as the learnings [[27]](#ref-27). The filled reports read for this bundle are full of
explicit verdicts - a conditional GO with a scored matrix [[35]](#ref-35), a staged adoption gated on
an upstream release [[34]](#ref-34), a *"Technically de-risked; not forced"* [[36]](#ref-36) - and one
general blank template makes *"Recommendations"* an explicit, if optional, heading [[45]](#ref-45).

*This bundle's judgment, and the cost of it:* an investigator who has spent the box and refuses to say
what they now believe has pushed the hardest part of the work onto the reader, who has less context
and was not there. The cost Microsoft is warning about is real, though, and it is the drift named in
[section 7](#7-anti-patterns-and-failure-modes): a Recommendation section makes it easy to write the
verdict first and let the evidence sections shrink into a preamble justifying it. The mitigation is
structural rather than rhetorical - the separation of facts from implications inside **What Was
Found**, and the requirement that **What Was Tried** be reproducible.

### 6.3 How much process should a spike carry?

A live, many-sided argument with named positions on every side.

- **Estimate them like stories.** SAFe: spikes are *"estimated, implemented and demonstrated"*
  [[12]](#ref-12). Scrum Alliance's 2014 commentary similarly puts them in the backlog, sized to fit
  an iteration [[15]](#ref-15).
- **Time-box them, do not estimate them.** Andrew Fuqua: *"Spikes are, like defects, generally harder
  to estimate correctly relative to user stories. It's best to time-box them"* [[18]](#ref-18).
  Gregory Engel, for Agile Alliance, is blunter: *"Estimating spikes with story points is a vanity
  metric and teams are better served with time-boxed spikes that are unsized"* [[16]](#ref-16).
- **Do not put them on the backlog at all.** Mary Iqbal: *"Most so-called 'spikes' do not belong on
  the Product Backlog"*, because *"creating tickets to prove that the team is working is
  counterproductive"* [[22]](#ref-22)[[23]](#ref-23).
- **They are not a Scrum thing.** Matthew Hodgson: *"In Scrum there is no such thing as a Spike"*
  [[17]](#ref-17), which the Scrum Guide's silence corroborates directly [[14]](#ref-14).
- **Barely use them at all.** Mark Blandford holds the most radical named position found: *"First
  off, let me be clear I'm not 100% against completing Spikes. Perhaps 99% against them though"*
  [[20]](#ref-20).

Scrum.org has published recurring content debating spike misuse, but its site returned a bot challenge
on every fetch attempt and no claim here rests on it [[24]](#ref-24). **Nothing in this bundle
requires you to resolve this argument.** A spike report is agnostic about where the spike was tracked;
it records what the investigation found. If your organisation is in the camp that barely uses spikes,
the correct number of spike reports to write is small, and that is a coherent position.

### 6.4 What the gap finding does and does not establish

[Section 3](#6-what-this-does-not-settle) makes an unusually strong claim for this library - that an
explicit non-scope statement is the most consistent element real reports supply and templates omit -
and the three caveats stated there are load-bearing, not decoration. Restated so nobody quotes the
finding without them: the corpus was **selected** by structural search, a large share of it shows
signs of **agent-authored** drafting, and it mixes **three genres** that should not be pooled into one
frequency count. The finding is a good reason to include the section. It is not a measurement of human
practice, and citing it as one would be exactly the defect class this library's review process exists
to catch.

---

## 7. Anti-patterns and failure modes

1. **The ADR with a longer preamble.** The sharpest failure for this type, and the easiest to commit.
   The tell is a document whose evidence sections exist to justify a verdict that was reached before
   the box opened. **A spike report that recommends without recording what was tried is a bad ADR; an
   ADR that shows its working is not a spike report.** If the decision is genuinely made, write an
   [ADR](../adr/adr_companion.md) and stop.
2. **The unanswerable question.** A spike aimed at a topic rather than a question. The box expires,
   the report describes the terrain, and nothing is decided. Fuqua's rule that every spike have one
   explicit question with a named recipient is the countermeasure [[18]](#ref-18).
3. **The bounded answer read as a general one.** The result held on one platform, one version, one
   dataset, and the report never said so. This is what **What This Does Not Settle** exists to prevent,
   and what environment-pinned findings guard against [[32]](#ref-32).
4. **The silently dropped scope.** You abandoned a promising branch at hour three and never mentioned
   it, so the next team spends their box rediscovering that it does not work. Preserving the unrun
   path explicitly is the good form [[31]](#ref-31).
5. **Findings with no anchor.** Claims a reader cannot verify or reproduce: no commands, no versions,
   no file references, no counts. The report becomes an opinion with formatting
   [[37]](#ref-37)[[34]](#ref-34).
6. **The quietly edited retraction.** An early finding turns out to be wrong and is deleted rather than
   marked, so downstream readers cannot tell which conclusions moved. Track the retraction in place
   [[39]](#ref-39).
7. **The dumping ground.** Spikes multiply until they crowd out delivery. Miranda Dulin names it
   directly - *"Everyone doesn't get a spike because one isn't always warranted"*, and *"If your team
   has a Sprint that is entirely consumed with spikes...this is a sign that something is wrong"* - and
   quotes Mitch Lacey on the downstream version, where follow-on work jumps the queue: *"The team
   should not have committed to the tasks that would come out of that spike"* [[19]](#ref-19).
8. **The box that never closes.** The investigation runs long and nobody notices, because the expiry
   was never a shared event. Dulin's countermeasure is procedural: *"Development teams should discuss
   the expiration of a timebox in the Daily Scrum"* [[19]](#ref-19).
9. **The performative spike.** A ticket and a write-up created to demonstrate activity rather than to
   reduce uncertainty [[22]](#ref-22). The test is whether a named decision was waiting on the answer.
10. **The report nobody could ask about.** No named investigator, no contact, no date. Microsoft's
    template asks for an email precisely because follow-up questions are the normal case
    [[11]](#ref-11).

---

## 8. Relationships to other artifacts

**The family placement, which is this document's fourth edge.** The
[`decision-docs` contract](../../docs/internal/contracts/decision-docs.md) frames three distinct
roles, and requires every member to state its position against the others:

- an **[RFC](../rfc/rfc_companion.md) proposes** a technical decision and gathers feedback before it
  is made;
- an **[ADR](../adr/adr_companion.md) records** one, after it is made and immutably;
- an **[SDD](../sdd/sdd_companion.md) describes** the design that implements it.

A **spike report investigates the question that precedes all three.** It hands over evidence and a
proceed-or-not recommendation; it does not propose, decide, or design. That boundary is not this
library's invention: the paired pm-skills skill
[`develop-spike-summary`](https://github.com/product-on-purpose/pm-skills) draws it in its own
description, pointing authors at `develop-adr` for the architecture decision the spike informs.

**The clearest named source on this edge also complicates it.** Dan Leech argues the spike and
the ADR overlap heavily - *"they are basically the same picture"* - while still drawing the sequence
this bundle uses: *"Spikes are done before the implementations are made"*, *"It follows that the spike
can act as a supporting document for an ADR. That a spike will evolve to an ADR"*, and, on what the
spike's own artifact should be, *"the main artifact of the spike should be the notes"* [[28]](#ref-28).
That is an argued opinion, not a standard, and it is the strongest single statement found of what a
spike report is **not**: a finished decision.

- **Feeds an [RFC](../rfc/rfc_companion.md).** The evidence an RFC leans on to argue its motivation is
  often a spike's. A practitioner describing real Jira usage puts it plainly: a Spike ticket's outcome
  *"might be a design doc, planning, or other stuff"* [[56]](#ref-56).
- **Feeds an [ADR](../adr/adr_companion.md).** The path the paired skill names, and the one Dan Leech
  describes [[28]](#ref-28). A real spike report in the wild links forward to the ADR identifier it
  produced [[36]](#ref-36).
- **Feeds an [SDD](../sdd/sdd_companion.md) or a specification.** A real specification resolves five
  separate open questions by citing one spike report's named sub-sections, and expects that report to
  have captured friction items and negative-test output, not only the positive result [[30]](#ref-30).
- **Is cited by, and then superseded by, both.** A downstream design document citing a spike report by
  stable identifier, date and author is the artifact working as intended [[35]](#ref-35). Once the
  decision is recorded, the spike report is history, not governance.

**An honest note about the literature, because it explains why this edge is thinly sourced.** A
well-known practitioner survey of RFC and design-doc practice across major technology companies never
mentions spikes at all; a direct check of its text returns zero occurrences of the word [[29]](#ref-29).
The spike literature and the RFC/design-doc literature are two traditions that rarely cite each other,
so most of the mapping above rests on real artifacts found in repositories rather than on published
guidance.

**Tooling, which is where the convention is most visible.** No major tracker ships a Spike type by
default. Jira's standard work types include bug and story [[51]](#ref-51); none of Azure DevOps'
four default processes includes one [[52]](#ref-52); GitHub Issues ships *"task, bug, and feature"*
[[53]](#ref-53)[[54]](#ref-54). The sharpest confirmation comes from GitHub's own roadmap announcement,
which names spike as the paradigm example of a **custom** org-defined type: *"Users will be able to
define issue types (ex. bug, feature request, spike) at the org level"* [[55]](#ref-55). Spike is a
convention teams add, everywhere, and a shipped default nowhere.

---

## 9. Adaptations

- **When the report is an issue comment, not a file.** GitLab's model is a legitimate and fully
  worked alternative: the spike issue *is* the artifact, and it is closed with one summary comment
  combining learnings and recommended paths [[27]](#ref-27). If that is your culture, use this
  template's six sections as the shape of that comment rather than fighting for a file.
- **When your tracker has no Spike type.** Nearly nobody's does [[51]](#ref-51)[[52]](#ref-52)[[53]](#ref-53).
  Use a label or a custom type; a practitioner thread notes these *"may be separate issue types or a
  custom field describing the type of story"* [[56]](#ref-56). The report does not care which you
  chose.
- **When the box expires without an answer.** No source read prescribes a protocol for this, which is
  itself worth knowing. The nearest logged guidance is Morein's, that if you need more time *"that's a new
  conversation with the team"* [[21]](#ref-21). Nothing else read prescribes what the expiry obliges. *(Author judgment: write the report anyway. A report
  whose Recommendation is a named next spike with a narrower question is a successful outcome, not a
  failed one, and is exactly what **What This Does Not Settle** is for.)*
- **When an agent runs the spike.** A distinct and growing genre, and the templates written for it
  look different: a mandatory investigation log [[48]](#ref-48), a one-hour hard cap enforced as a
  checklist item, and separate output documents for findings and for decisions [[49]](#ref-49). Treat
  their exhaustiveness as a property of the genre rather than as a model for a human team, and see the
  provenance caveat in [section 3](#6-what-this-does-not-settle).
- **Solo and very small teams.** *(Author judgment: no logged source addresses this directly.)* The
  reader is you in three months, and that reader has forgotten which branch you abandoned and why. The
  two sections worth keeping at any size are **What Was Tried** and **What This Does Not Settle**; the
  rest can compress to a paragraph each.
- **Regulated or audited work.** *(Author judgment: no source read for this bundle addresses spikes
  in a regulated context, and this bundle will not invent one.)* If your evidence must survive an
  audit, the reproducibility practices in [section 3](#3-what-was-tried) - pinned environments,
  commands, file-level anchors, tracked retractions - are the parts to harden first, and a
  [decision record](../adr/adr_companion.md) is still the artifact an auditor will ask for.

---

## 10. Worked example

[`spike-report_example.md`](spike-report_example.md) is a single, fully worked instance of a real
time-boxed investigation, filled end to end with no placeholders remaining. Its subject is an
over-the-air firmware update: whether one fits an overnight maintenance window, and what happens to a
device when an update fails partway. It reaches a **conditional** recommendation rather than a flat
yes, which is the shape most spike reports should reach and the one a four-part template makes hardest
to express.

Per the `decision-docs` contract's independence rule (section 5), it shares no scenario with `adr`,
`rfc` or `sdd`: this family teaches the **distinction between its roles**, so a single thread running
through all four would work against the thing the family exists to show.

It exists to demonstrate the four things this format is easiest to fake: a question narrow enough to
be answered false, a time box reported honestly against what was actually spent, findings anchored to
evidence a reader could reproduce and kept separate from what they imply, and an explicit non-scope
statement that stops a bounded answer from being read as a general one. Per the
[family contract](../../docs/internal/contracts/decision-docs.md), it is deliberately independent of
the other `decision-docs` examples: the family's teaching value is the distinction between the four
roles, not a single thread running through them.

---

## References

Tagged by reliability: `[primary]` standards body, regulator, or originating source; `[practitioner]`
recognized independent authority; `[vendor]` commercially motivated, reliable on convention.
Researched 2026-09-11. **Numbering here is this document's own, contiguous from 1**; every entry
traces to a numbered source in [`spike-report_research-log.md`](spike-report_research-log.md), which
records retrieval status per source and is the audit trail. Only `fetched-and-verified` sources are
quoted; the two entries that could not be read are marked and carry no claim alone.

<a id="ref-1"></a>[1] Ward Cunningham. "[Spike Solution](https://c2.com/ppr/wiki/ExtremeProgrammingRoadmap/SpikeSolution.html)." c2 wiki / Portland Pattern Repository (accessed 2026-09-11). The founding account, crediting Kent Beck with the name; describes throwaway code and no document. [primary]

<a id="ref-2"></a>[2] Ward Cunningham. "[SpikeSolution](https://web.archive.org/web/20160105154555/http://c2.com/cgi/wiki?SpikeSolution)." Ward Cunningham's wiki, 2016 Internet Archive snapshot (accessed 2026-09-11). The live c2.com no longer serves this page directly; only the archived snapshot was readable. [primary]

<a id="ref-3"></a>[3] Ron Jeffries, Ward Cunningham, Kent Beck, Katy Mulvey and Eric Newhuis (signed wiki contributions). "[SpikeSolution](https://c2.com/xp/SpikeSolution.html)." c2 XP wiki (accessed 2026-09-11). Source of the time-box guidance and of the original keep-versus-throw-away disagreement. [primary]

<a id="ref-4"></a>[4] Ward Cunningham et al. "[Extreme Programming](https://c2.com/xp/ExtremeProgramming.html)." c2 wiki (accessed 2026-09-11). [primary]

<a id="ref-5"></a>[5] Don Wells. "[Create a Spike Solution](http://www.extremeprogramming.org/rules/spike.html)." ExtremeProgramming.org, 1999-era rules page (accessed 2026-09-11). Contains no report-format or section guidance of any kind. [primary]

<a id="ref-6"></a>[6] James Shore and Shane Warden. "[Spike Solutions](http://www.jamesshore.com/Agile-Book/spike_solutions.html)," from *The Art of Agile Development* (accessed 2026-09-11). [practitioner]

<a id="ref-7"></a>[7] John Clapham. "[Why is a Spike called a Spike?](https://johnclapham.wordpress.com/2016/02/23/why-is-a-spike-called-a-spike/)" johnclapham.wordpress.com, 2016-02-23 (accessed 2026-09-11). Disputes the standard etymology; records Beck's own later preference for "architectural prototype". [practitioner]

<a id="ref-8"></a>[8] Mike Cohn. "[Agile Spikes Deliver Knowledge So Teams Can Deliver Products](https://www.mountaingoatsoftware.com/agile/what-are-agile-spikes)." Mountain Goat Software (accessed 2026-09-11). A named practitioner describing an activity; no mention of a report or template. [practitioner]

<a id="ref-9"></a>[9] Mike Cohn. "[Agile Spikes Deliver Knowledge So Teams Can Deliver Products](https://www.mountaingoatsoftware.com/blog/spikes)." Mountain Goat Software (accessed 2026-09-11). **The same article as [8] at a second route on the site**, which is how the research log records it; it is kept as a separate entry only because both URLs were retrieved. No date is given because the page carries none that this research read. [practitioner]

<a id="ref-10"></a>[10] Microsoft (Code with Engineering Playbook, CSE/ISE). "[Technical Spike](https://microsoft.github.io/code-with-engineering-playbook/design/design-reviews/recipes/technical-spike/)." microsoft.github.io (accessed 2026-09-11). **The single named source that publishes the spike's deliverable as a document.** Represents one organisation's house convention, not the XP originators' view. [practitioner]

<a id="ref-11"></a>[11] Microsoft (Code with Engineering Playbook, CSE/ISE). "[Template: Technical Spike](https://microsoft.github.io/code-with-engineering-playbook/design/design-reviews/recipes/templates/template-technical-spike/)." microsoft.github.io (accessed 2026-09-11). Verified against the raw markdown in the microsoft/code-with-engineering-playbook repository, confirming it is a current maintained file. [practitioner]

<a id="ref-12"></a>[12] Scaled Agile, Inc. "[Spikes](https://framework.scaledagile.com/spikes/)." SAFe framework site (accessed 2026-09-11). The publicly accessible text does not use the words "document" or "report"; the deeper Technical and Functional Spikes material is behind a login and was not read. [vendor]

<a id="ref-13"></a>[13] Scaled Agile, Inc. "[Enablers](https://framework.scaledagile.com/enablers)." SAFe framework site (accessed 2026-09-11). Confirms the four Enabler categories and that spikes are not a fifth; carries its own last-update stamp. [vendor]

<a id="ref-14"></a>[14] Ken Schwaber and Jeff Sutherland. "[The 2020 Scrum Guide (US)](https://scrumguides.org/docs/scrumguide/v2020/2020-Scrum-Guide-US.pdf)." scrumguides.org (accessed 2026-09-11). Full text checked: the word "spike" does not appear. A verified null result, not an inference from silence elsewhere. [primary]

<a id="ref-15"></a>[15] Scrum Alliance. "[Spikes in Scrum: The Exception, Not the Rule](https://web.archive.org/web/20180712125321/https://scrumalliance.org/learn-about-scrum/agile-atlas/agile-atlas-commentaries/may-2014/spikes-in-scrum-the-exception,-not-the-rule)." Agile Atlas Commentaries, 2014-05. The live URL now 404s and the piece has been removed from Scrum Alliance's active navigation; retrieved via a 2018 Internet Archive capture (accessed 2026-09-11). [vendor]

<a id="ref-16"></a>[16] Gregory Engel. "[The Practice of Sizing Spikes with Story Points](https://agilealliance.org/the-practice-of-sizing-spikes-with-story-points/)." Agile Alliance (accessed 2026-09-11). [practitioner]

<a id="ref-17"></a>[17] Matthew Hodgson. "[To spike or not to spike?](https://zenexmachina.com/to-spike-or-not-to-spike/)" Zen Ex Machina (accessed 2026-09-11). [practitioner]

<a id="ref-18"></a>[18] Andrew Fuqua. "[Don't Estimate A Spike In Agile](https://liminalarc.co/dont-estimate-spike-in-agile/)." LeadingAgile, now hosted at LiminalArc; originally published 2014-04 with a 2015 addendum, content not apparently updated (accessed 2026-09-11). [practitioner]

<a id="ref-19"></a>[19] Miranda Dulin. "[Spike Antipatterns: How Not to Use Spikes](https://www.agileambition.com/Essays/Spike-Antipatterns)." Agile Ambition, 2025-10-20 (accessed 2026-09-11). Quotes published Scrum author Mitch Lacey on the dumping-ground failure mode. Site-owner identity is self-reported on the page and was not independently corroborated. [practitioner]

<a id="ref-20"></a>[20] Mark Blandford. "[No Spikes](https://dev.to/markblandford/no-spikes-547m)." dev.to, 2025-01-21 (accessed 2026-09-11). The most radical named position found; explicitly a minority view. [practitioner]

<a id="ref-21"></a>[21] Giora Morein. "[What Is an Agile Spike and When to Time-Box One](https://thinklouder.com/blog/what-is-an-agile-spike-and-when-to-time-box-one/)." ThinkLouder, updated 2026-05-19 (accessed 2026-09-11). [practitioner]

<a id="ref-22"></a>[22] Mary Iqbal. "[Spikes are so... ugh](https://www.rebelscrum.site/post/spikes-are-so-ugh)." Mirrored republication on rebelscrum.site of a piece originally published on Scrum.org's blog, 2024-06-14, updated 2025-01-10 (accessed 2026-09-11). Used because it returned readable body text where the original did not; content was not cross-verified word-for-word against the original, which is [[23]](#ref-23). [practitioner]

<a id="ref-23"></a>[23] Mary Iqbal. "[Spikes are So... Ugh](https://www.scrum.org/resources/blog/spikes-are-so-ugh)." Scrum.org. **URL CONFIRMED, BODY NOT READ: WebFetch returned an empty body on three attempts (checked 2026-09-11), consistent with a JavaScript-rendered page. Nothing is quoted from it; the quotations attributed to this piece come from the mirror at [[22]](#ref-22).** [practitioner]

<a id="ref-24"></a>[24] Scrum.org. "[The Spike Dilemma](https://www.scrum.org/resources/blog/spike-dilemma)" and related blog and forum content. **URL CONFIRMED, BODY NOT READ: every fetch returned an AWS WAF bot-challenge page rather than article content (checked 2026-09-11). Cited only as a pointer that Scrum.org publishes recurring content on spike misuse; no claim rests on it.** [practitioner]

<a id="ref-25"></a>[25] Anuj Ojha. "[What Is a Spike in Agile? Examples, Types & SAFe Guide](https://nextagile.ai/blogs/agile/what-is-a-spike-in-agile/)." NextAgile (accessed 2026-09-11). Cited as the traceable origin of widely repeated "documented finding" boilerplate that attributes itself to established practice without citing a primary source. [vendor]

<a id="ref-26"></a>[26] Radu Marinescu. "[Spike (Enabler Story)](https://agilesm.net/spike-enabler-story.html)." AgileSM.net (accessed 2026-09-11). Lists a decision record among spike outputs but names no document type and shows no template; the author is not established in the agile literature, so this is cited as thin evidence, not as a qualifying named source. [practitioner]

<a id="ref-27"></a>[27] GitLab Inc. "[Technical Exploration ('Spike') Guidelines](https://handbook.gitlab.com/handbook/engineering/development/growth/technical_spikes/)." GitLab Handbook, Growth engineering (accessed 2026-09-11). A real current org process, not a blank template; the handbook is a living document and this may change. [primary]

<a id="ref-28"></a>[28] Dan Leech. "[Why I don't write ADRs](https://www.dantleech.com/blog/2024/03/10/why-i-dont-write-adrs/)." dantleech.com, 2024-03-10 (accessed 2026-09-11). An argued opinion piece, not a standard. [practitioner]

<a id="ref-29"></a>[29] Gergely Orosz. "[Companies Using RFCs or Design Docs and Examples of These](https://blog.pragmaticengineer.com/rfcs-and-design-docs/)." The Pragmatic Engineer (accessed 2026-09-11). Cited for a negative finding: a direct check of the fetched text returns zero occurrences of "spike". [practitioner]

<a id="ref-30"></a>[30] prisma/orm. "[class-based-codec-design.spec.md](https://github.com/prisma/orm/blob/f2e3590ff2d446304e7b7af55b9a0277afb0f43e/projects/codec-registration-completion/specs/class-based-codec-design.spec.md)." GitHub (accessed 2026-09-11). A downstream specification citing a spike report's named sub-sections. The underlying spike file itself was not retrieved; only this document's citations of it were read. [practitioner]

<a id="ref-31"></a>[31] IsmaelMartinez/teams-for-linux. "[Spike: custom stickers (#2476) feasibility](https://github.com/IsmaelMartinez/teams-for-linux/blob/7657aa8bf884aede24b3211e1f46277c29f9bd6a/spike/2476-stickers/SPIKE.md)." GitHub (accessed 2026-09-11). A real filled spike on a real dated issue in a well-known project; the phase structure suggests AI-assisted drafting. [practitioner]

<a id="ref-32"></a>[32] fizzyedit/fizzy. "[Spike: driving host dvui state from a prebuilt plugin dylib](https://github.com/fizzyedit/fizzy/blob/c325818488ad9897625a41ea47304fd133610d22/spikes/shared-globals/README.md)." GitHub (accessed 2026-09-11). References an agent plan file, indicating AI-assisted authorship. [practitioner]

<a id="ref-33"></a>[33] daaain/claude-code-log. "[parse-memory-spike.md](https://github.com/daaain/claude-code-log/blob/main/work/parse-memory-spike.md)." GitHub (accessed 2026-09-11). The best filled worked write-up found, with named-maintainer scope decisions and a three-way split of its open-items apparatus; one of the strongest human-provenance sources in the sample. [practitioner]

<a id="ref-34"></a>[34] coder/xum. "[Spike Findings: Progressive Effect Migration via oRPC Integration](https://github.com/coder/xum/blob/b9bc3949cffb231787c9e9fc669672a3bc486aef/rfc/20260831_effect-orpc-spike.md)." GitHub (accessed 2026-09-11). Mentions an AI review gate on the spike itself. [practitioner]

<a id="ref-35"></a>[35] gastownhall/gastown. "[witness-at-team-lead.md](https://github.com/gastownhall/gastown/blob/649b832b7672bc7a2dbef26f5983aba6198b819b/docs/design/witness-at-team-lead.md)." GitHub (accessed 2026-09-11). Read in full, but it condenses a separate spike report that was not independently retrieved, and its named author may be an agent identity rather than a confirmed human. [practitioner]

<a id="ref-36"></a>[36] kungfu-systems/kungfu. "[Rust host shell feasibility spike report](https://github.com/kungfu-systems/kungfu/blob/a025fe8fd3063175a263c481b42b0b34f63fa91c/docs/research/rust-host-spike.md)." GitHub, dated 2026-07-10 (accessed 2026-09-11). Formal doc-metadata schema suggests deliberate but possibly AI-assisted documentation tooling. [practitioner]

<a id="ref-37"></a>[37] backnotprop/plannotator. "[SPIKE: PR Context Warm Cache](https://github.com/backnotprop/plannotator/blob/0f2bd6051c66d26f2d776a2a521d856627b3316c/adr/research/SPIKE-pr-context-warm-cache-20260630-110258.md)." GitHub (accessed 2026-09-11). Second-precision timestamped filenames in a dedicated research pipeline strongly suggest agent-generated documents. [practitioner]

<a id="ref-38"></a>[38] backnotprop/plannotator. "[Spike: Source Edit Race and Conflict Recovery](https://github.com/backnotprop/plannotator/blob/0f2bd6051c66d26f2d776a2a521d856627b3316c/adr/research/SPIKE-source-edit-race-and-conflict-20260618-095558.md)." GitHub (accessed 2026-09-11). Cited as a clean negative instance: a thorough filled report with no out-of-scope, confidence, effort or decision-maker fields. Same agent-pipeline provenance caveat. [practitioner]

<a id="ref-39"></a>[39] dbugom/rop-finder. "[Phase 4b gadget-inventory spike report](https://github.com/dbugom/rop-finder/blob/3228b1abdc8ceb180edfc1e1a80d16e52548198a/tests/spike-report.md)." GitHub (accessed 2026-09-11). Solo project; the document's structure suggests an adversarial-review-driven, possibly AI-assisted process. [practitioner]

<a id="ref-40"></a>[40] cristoslc/architecture-reference. "[Final Model Validation, SPIKE-007 Summary](https://github.com/cristoslc/architecture-reference/blob/0b7dd9fd64e6df5145ac9376bb89746a379ea614/docs/research/Complete/(SPIKE-007)-Final-Model-Validation/(SPIKE-007)-Final-Model-Validation.md)." GitHub (accessed 2026-09-11). The whole spike series is dated to a single day with heavy dependency-graph frontmatter, suggesting an automated research harness rather than a human team working over days. [practitioner]

<a id="ref-41"></a>[41] hansikadev/Jarviss. "[CORTEX v5 Spike Results: Hermes Agent Core Integration](https://github.com/hansikadev/Jarviss/blob/cb584897d1e03c16e37c50b6158964c295384b7c/SPIKE_RESULTS.md)." GitHub (accessed 2026-09-11). The only instance found recording time actually spent; it is also the lowest-confidence provenance for organic human practice, since it is ambiguous whether a human or the agent logged the time. [practitioner]

<a id="ref-42"></a>[42] miethe/CCDash. "[Claude Code Session Naming, Availability Spike](https://github.com/miethe/CCDash/blob/04286f5cc9ac22c1f6ce98dc440b778ef8f55b90/docs/project_plans/exploration/automatic-session-naming/spikes/tech-claude-spike.md)." GitHub (accessed 2026-09-11). Empirical and data-driven over a large real corpus; likely AI-assisted analysis. [practitioner]

<a id="ref-43"></a>[43] unredacted/freesocks-control-plane. "[E2EE Phase 0 spike: KEM decision, KAT sources, and the isolate-budget gate](https://github.com/unredacted/freesocks-control-plane/blob/main/docs/e2ee-phase0-spike.md)." GitHub (accessed 2026-09-11). A real filled write-up using no named-section convention at all. [practitioner]

<a id="ref-44"></a>[44] Tooramvale. "[_spike-templates](https://github.com/Tooramvale/_spike-templates)" (repository and README). GitHub (accessed 2026-09-11). Evidence that practitioners informally build spike-outcome templates, and that XP and SAFe are the two reference points such an author cites. The author is anonymous and non-notable, so this does not meet the named-source bar. [practitioner]

<a id="ref-45"></a>[45] Tooramvale. "[spike_outcome_template.md](https://github.com/Tooramvale/_spike-templates/blob/master/spike_outcome_template.md)." GitHub (accessed 2026-09-11). A real post-hoc spike report template; findings and recommendations are separate optional sections, and there is no time-box section in the outcome half of the pair. [practitioner]

<a id="ref-46"></a>[46] Tooramvale. "[spike_plan_template.md](https://github.com/Tooramvale/_spike-templates/blob/master/spike_plan_template.md)." GitHub (accessed 2026-09-11). The companion pre-spike template, where the time box actually lives. [practitioner]

<a id="ref-47"></a>[47] Vibhor Chandel. "[Spikes for uncertainties in Scrum](https://www.vibhorchandel.com/p/spikes-for-uncertainties-in-scrum)." vibhorchandel.com (accessed 2026-09-11). The clearest instance found of a dedicated time-box heading, on a pre-spike ticket template that never reaches a findings or recommendation stage. [practitioner]

<a id="ref-48"></a>[48] PeonPing. "[gitban spike template](https://github.com/PeonPing/peon-ping/blob/main/.gitban/templates/spike.md)." GitHub (accessed 2026-09-11). The richest real template found, but explicitly authored for an LLM coding agent to fill in; its section count should not be read as typical of human practice. [practitioner]

<a id="ref-49"></a>[49] nWave-ai. "[nw-spike task template](https://github.com/nWave-ai/nWave/blob/main/nWave/tasks/nw/spike.md)." GitHub (accessed 2026-09-11). Same AI-agent-genre caveat. [practitioner]

<a id="ref-50"></a>[50] kelebeklabs. "[Finding spikes in your plans](https://dev.to/kelebeklabs/finding-spikes-in-your-plans-1lof)." dev.to (accessed 2026-09-11). Cited as a corroborating null result: no documentation template, timeboxing mentioned only informally. [practitioner]

<a id="ref-51"></a>[51] Atlassian. "[What are work types?](https://support.atlassian.com/jira-cloud-administration/docs/what-are-issue-types/)" Jira Cloud Administration documentation (accessed 2026-09-11). Raw page text grepped directly: zero occurrences of "spike". [primary]

<a id="ref-52"></a>[52] Microsoft. "[About work items and work item types](https://learn.microsoft.com/en-us/azure/devops/boards/work-items/about-work-items?view=azure-devops)." Azure DevOps documentation (accessed 2026-09-11). Raw page text grepped directly: zero occurrences of "spike" across all four default processes. [primary]

<a id="ref-53"></a>[53] GitHub. "[Managing issue types in an organization](https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/managing-issue-types-in-an-organization)." GitHub Docs (accessed 2026-09-11). Raw page text grepped directly: zero occurrences of "spike". [primary]

<a id="ref-54"></a>[54] GitHub. "[About the issue type field](https://docs.github.com/en/issues/planning-and-tracking-with-projects/understanding-fields/about-the-issue-type-field)." GitHub Docs (accessed 2026-09-11). Independent confirmation of the same no-native-Spike finding on a second documentation page. [primary]

<a id="ref-55"></a>[55] GitHub product team. "[Issues: Issue Types](https://github.com/github/roadmap/issues/837)." github/roadmap issue 837, posted 2023-11-08; verified via an authenticated read of the issue body (accessed 2026-09-11). The feature later shipped with task, bug and feature as the actual defaults; "spike" remained an example, not a default. [primary]

<a id="ref-56"></a>[56] Atlassian Community practitioners. "[Functional Stories, Spikes, Technical Stories! Help](https://community.atlassian.com/forums/Agile-discussions/Functional-Stories-Spikes-Technical-Stories-Help/td-p/1913069)." Atlassian Community forum thread, c. 2022-01 (accessed 2026-09-11). Unofficial community discussion, not vendor documentation; individual usernames could not be reliably confirmed from the rendered page. [practitioner]
