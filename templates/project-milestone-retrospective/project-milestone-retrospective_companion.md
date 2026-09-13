# Companion: Project Milestone Retrospective

> The deep explainer for the project-milestone-retrospective bundle. Read this to understand what this
> document actually is, which two named lineages admit it, why the foundational Army source is the weaker
> of the two, and why the criticism aimed at it is narrower than it first sounds. The short operator card
> is [`project-milestone-retrospective_guide.md`](project-milestone-retrospective_guide.md); a fully worked
> instance is [`project-milestone-retrospective_example.md`](project-milestone-retrospective_example.md).
> Inline citations like [[1]](#ref-1) resolve to the [References](#references) at the bottom, tagged by
> source reliability. The full retrieval trail is
> [`project-milestone-retrospective_research-log.md`](project-milestone-retrospective_research-log.md).
>
> This bundle is the third member of the `process-docs` family, and the family is built to be taught by
> contrast. A **sprint retrospective** looks back on a **period**, on a cadence, at how a team worked. An
> **incident postmortem** looks back on an **event**, triggered by it, at why a specific thing failed.
> This document looks back on **a bounded piece of work that has ended**. If you cannot tell those three
> apart after reading this, the bundle has failed.

---

## 1. Orientation

A project milestone retrospective is **the document a team writes when a bounded piece of work is over,
for readers who may not have been there.** It is terminal. The project closes, the team disperses, and the
account has to survive both. That is why the type travels under the aliases `lessons learned`,
`post-project review` and `after-action review`, and why Kerth's founding handbook states the rationale in
exactly those terms: "the collective team wisdom acquired during the previous project is likely to be lost
as individuals are scattered across the organization to support new undertakings. If, at the end of a
project, the collective wisdom is discussed and documented, it becomes knowledge that survives the
breakup of the team" [[6]](#ref-6).

At a glance:

- **Two independent named lineages publish it as a document, not just a meeting.** The Center for Army
  Lessons Learned, the US Army's own lessons-learned proponent, names the "After action report" separately
  from the review and defines it as "A written report that is typically submitted after a training, combat
  operation, or other mission that normally documents a unit's actions for historical purposes but also
  provides key observations and LL" [[1]](#ref-1). PMI's PMBOK Guide Sixth Edition lists "Lessons learned
  register" as the first named output of process 4.4, Manage Project Knowledge [[3]](#ref-3).
- **The foundational Army source is the weaker one, and this inverts the obvious assumption.** TC 25-20
  (1993), the older and more foundational of the two Army sources, defines the AAR as a discussion: "An AAR is a dynamic,
  candid, professional discussion of training which focuses on unit performance against the Army standard
  for the tasks being trained," and insists "An AAR is not a critique" [[2]](#ref-2). Anyone citing
  TC 25-20 for a written after-action report is citing the wrong document.
- **The criticism is real, and it is narrower than it sounds.** Every fetched critic in this research
  attacks a specific pattern, an inert repository or minutes filed and never consulted, and **every one of
  them still recommends writing something down** [[31]](#ref-31)[[32]](#ref-32)[[33]](#ref-33). The
  discriminator is whether retrieval is wired into somebody's workflow. The honest framing of this bundle
  is **anti-deposit-and-forget, not anti-documentation**.
- **Two peer-reviewed findings pull in opposite directions, and this bundle keeps both.** Dingsøyr et al.
  find that publishing the document can damage the practice: "Having minutes public could also lead to
  critique being toned down or removed completely" [[34]](#ref-34). Anandayuvaraj et al., studying
  engineers at a national space research centre, find the opposite failure, knowledge dying with turnover
  in an organisation that has no such document at all: "I don't think they are documented, pretty much at
  all" [[35]](#ref-35).
- **Naming the audience changes what gets written, not just the cover page.** This is the strongest
  finding from the four real filled documents read for this bundle. The IRS relabelled its own findings:
  "We have labeled these lessons opportunities, because they will help both improve the tax filing
  ecosystem and inform the decision about Direct File's future" [[15]](#ref-15). A naive
  what-went-well/what-did-not/actions shape has no field for that at all.
- **Its current PMBOK status is genuinely uncertain, and this companion says so rather than guessing.**
  The Eighth Edition restructured around principles, and its freely published table of contents contains no
  "Lessons Learned" heading [[4]](#ref-4). Whether the register survives under that name could not be
  confirmed, because the full text is paywalled and was not read. Everything here cites the Sixth Edition
  and labels it as such.

---

## 2. Origins and evolution

### 2.1 The Army lineage, and why the foundational source is the weaker one

The after-action review enters civilian practice from US Army doctrine, and a civilian adaptation states
the descent plainly: "First used by the Army on combat missions, the AAR is a structured approach for
reflecting on the work of a group" [[19]](#ref-19).

The 1993 training circular is **about a conversation**. TC 25-20 defines the AAR
as a discussion, contrasts it directly with a critique [[2]](#ref-2), and the only written record it
mandates belongs to the observer, taken before the session as preparation: "He should keep an accurate
written record of what he sees and hears and record events, actions, and observations by time sequence to
prevent loss of valuable information and feedback" [[2]](#ref-2). Those are prep notes, not a published
retrospective.

**The written artifact comes from CALL's later doctrine, and CALL names the two things separately.** Its
handbook on establishing a lessons-learned programme defines the after action review as "A verbal,
professional discussion of a unit's actions that typically occurs immediately after a training event,
combat operation, or other mission" and the after action report as the written document quoted in
[section 1](#1-orientation) [[1]](#ref-1). It then publishes a formal written-AAR template and states its
two purposes: "two key purposes of the written AAR should be to (1) document the operations conducted by
the unit for historical purposes and (2) provide best practices and lessons in the
observation-discussion-recommendation format that can be used to inform the Army's LL program"
[[1]](#ref-1).

That second purpose is the terminal-handover idea, stated in doctrine in 2011: the document exists to reach
people outside the unit that wrote it.

### 2.2 The PMI lineage, and the edition problem inside it

PMI's own free lexicon defines lessons learned as knowledge rather than as a document: "The knowledge
gained during a project which shows how project events were addressed or should be addressed in the future
for the purpose of improving future performance" [[5]](#ref-5). It has no entry for a lessons learned
register, even though it gives the structurally analogous risk register one: "Risk Register. A repository
in which outputs of risk management processes are recorded" [[5]](#ref-5).

The named document lives in the PMBOK Guide itself. PMI's freely published Sixth Edition errata reproduces
"Figure 4-8. Manage Project Knowledge: Inputs, Tools & Techniques, and Outputs" and lists "Lessons learned
register" as that process's first output, recurring afterwards as a project-document input across roughly a
dozen other processes [[3]](#ref-3). A PMI-hosted practitioner paper written against the Fourth Edition
shows the earlier state of the same idea, where lessons learned "can be collected at any time during the
project and identifies the process specifically in the closing process at the end of the project phases and
reviewed during planning" [[30]](#ref-30): an activity at closing, not yet a named living register.

**And then the structure moved again.** The Eighth Edition's table of contents, fetched from pmi.org,
carries no "Lessons Learned" heading, because the guide reorganised around principles rather than named
inputs, tools and outputs [[4]](#ref-4). The absence of a heading in a table of contents is not proof the
concept was dropped, and the full text was not read. This companion therefore cites the Sixth Edition for
the artifact and treats the current status as open (see
[section 6](#6-debates-and-contested-boundaries)).

### 2.3 Kerth, 2001: the project-scale founding text

Norman Kerth's *Project Retrospectives: A Handbook for Team Reviews* is the founding handbook for this
occasion in software. Its publisher synopsis frames the job as organisational preservation: "project
retrospectives offer organizations a formal method for preserving the valuable lessons learned from the
successes and failures of every project" [[7]](#ref-7).

Kerth supplies the two rationales that make this document type different in kind from a cadence retro, and
both are about **who will not be in the room**:

- **The team disperses**, so undocumented wisdom is lost with it [[6]](#ref-6).
- **Nobody present holds the whole account**: "no one person knows all the stories, and no one person knows
  how the pieces fit together to tell the tale of the entire project" [[6]](#ref-6).

He is also candid that the name was a preference among names already circulating, not a coinage: "this
ritual, called by many names - postmortem or postpartum, for example, or, my preference, retrospective - is
important to our practice of software" [[6]](#ref-6). And he prices the practice honestly: "Simply stated,
effective retrospectives require about three days" [[6]](#ref-6).

**A retrieval caveat that matters.** Only the publisher's free sample was read for this bundle: front
matter, Chapter 3 in full, the table of contents and the index [[6]](#ref-6). Chapters 7 and 10 exist and
their titles were read, but their bodies were not, and nothing here is attributed to them. The complete
book was not retrieved.

The Prime Directive that the book is best known for is quoted here from a community wiki carrying its full
text, because the sampled pages did not include the page it sits on: "Regardless of what we discover, we
understand and truly believe that everyone did the best job they could, given what they knew at the time,
their skills and abilities, the resources available, and the situation at hand" [[13]](#ref-13).

### 2.4 Derby and Larsen, 2006: five stages that describe a session, not a document

Esther Derby and Diana Larsen's *Agile Retrospectives* supplies the five-stage structure this research found cited elsewhere:
Set the Stage, Gather Data, Generate Insights, Decide What to Do, Close [[8]](#ref-8). It is worth being
precise about what that structure is, because it is routinely mistaken for a document outline.

**It describes facilitating a meeting.** The book's own definition is a meeting: "When we say retrospective,
here's what we have in mind: a special meeting where the team gathers after completing an increment of work
to inspect and adapt their methods and teamwork" [[8]](#ref-8). A later practitioner extending the model
confirms the same reading from outside: "These form the structure of a retrospective and are based on the
original phase model in Esther Derby and Diana Larsen's book" [[12]](#ref-12). **The agenda of a session is
not the outline of a document**, and a template that copies the five stages onto headings produces a
transcript rather than a record.

The book's default scope is also explicitly short-cycle: "Our main focus in this book is short
retrospectives - retrospectives that occur after one week to one month of work" [[8]](#ref-8). Releases and
project retrospectives get their own separate chapter, "Releases and project retrospectives"
[[11]](#ref-11), which is structural evidence that the terminal occasion is a different thing rather than a
longer version of the same one. That chapter's body was not in the retrieved text and nothing here is
quoted from it.

The lineages are connected by people as well as by ideas: Kerth co-founded the Retrospective Facilitators
Gathering with both authors, "With Norm Kerth, Esther and Diana are founders of the annual Retrospective
Facilitators Gathering" [[10]](#ref-10).

**One argument from that camp is pointed directly at this document type.** The Agile Alliance's own page
for the book renders it bluntly: "retrospectives (also known as 'post-mortems') are only held at the end of
the project - too late to help" [[9]](#ref-9). Section 6 takes that seriously rather than filing it.

---

## 3. Anatomy (section by section)

The lean variant carries six sections. The full variant carries the same six, unchanged in name and order,
plus one, so lean is a strict ordered subset of full.

### Scope and Period (lean and full)

**What it is.** Two things in one section: what is being looked back on and where its boundaries fall, and
**who reads this and what they decide with it**.

**Why it exists.** The first half is the section that stops these three documents blurring, and it has
direct template attestation: ITU's Post Implementation Review gives Scope of Review its own numbered
section, where "The paragraph provides a clear explanation of the scope of the review" [[22]](#ref-22), and
the VA's AAR template records whether the review ran "During Project" or "After Project Completion"
[[19]](#ref-19).

The second half is this bundle's strongest evidence-driven departure from the obvious template shape.
**Naming the audience and the document's next use changed the content of every accountability-grade
document read,
not just its cover page.** The IRS report relabelled its findings as opportunities rather than lessons
*because* they fed a specific pending decision, and said so in the same sentence [[15]](#ref-15), while
stating that the decision itself was still ahead: "We anticipate making a decision about the future of
Direct File later this Spring" [[15]](#ref-15). GAO-19-25 is literally an addressed letter, and it ends by
naming what it wants from whom: "GAO is making three recommendations, including that DOE and NNSA develop
requirements for defining how and where project management lessons learned for capital asset projects
should be documented and shared routinely and in a timely manner" [[17]](#ref-17). The NAO report closes in
lettered recommendations aimed at one named body [[16]](#ref-16). The only PMI-hosted lessons-learned
article this research could read in full reaches the same conclusion from the template-design side: a
lessons-learned template should "group data by areas of interest and in a standard format that allows
comparison with other similar projects, and segregate data by target audiences" [[29]](#ref-29).

*Beginner note:* write the boundaries as dates and deliverables, not as a mood. Then write one sentence
naming the reader and the decision: who opens this, and what are they about to do.

*Expert note:* if you cannot name a reader or a next use, that is a finding, not a formatting problem. It
is the exact condition every critic in [section 6](#6-debates-and-contested-boundaries) describes: a
document written into a repository nobody has a reason to open [[31]](#ref-31)[[32]](#ref-32). Decide
whether to find the reader or to stop writing.

### What Happened (lean and full)

**What it is.** The factual record, kept separate from interpretation, and **quantified wherever something
material can be counted**.

**Why it exists.** Published templates separate fact from judgement structurally. The DOE Office of Science
closeout report holds the baseline and closeout status in their own numbered sections and puts the
narrative lessons in a separate one [[20]](#ref-20). ITU separates Results Achievement, Financial Status,
Findings, Lessons Learned, Conclusions and Recommendations into six distinct sections [[22]](#ref-22).
Kubernetes' own Storage SIG retrospective opens by stating that its job is the record: "This document is
intended to chronicle the decisions made by the Storage SIG near the end of the Kubernetes 1.3 release with
the storage stack that were not well understood by the wider community" [[18]](#ref-18).

**On quantification, note the limit this research found.** All three government sources read lead with
numbers, and the IRS is the sharpest example: "The cost to develop the Direct File pilot came in much lower
than initial estimates," followed by "Through the end of the pilot, the total amount spent by IRS was $24.6
million, including the Report to Congress" [[15]](#ref-15). DOE's template is explicit that the numbers are
for reuse: "The purpose for this request is to allow other projects to use historical cost data of a
completed project" [[20]](#ref-20). But the Kubernetes retrospective quantifies engineering quantities, a
defect rate and a schedule slip, rather than money [[18]](#ref-18). **So the rule this template teaches is
quantify something material, not quantify in currency.** Demanding dollars would overfit the type to
public-money accountability documents.

*Beginner note:* write what a reader could verify from a system of record, and keep opinions out until the
next two sections. *A key engineer left one week before code freeze* is a fact; *we were under-resourced*
is an interpretation.

*Expert note:* in the `full` variant this section carries a quantification table. Pick the two or three
measures the work was actually judged on, and record planned against actual. If the only number available
is elapsed time, say that, rather than manufacturing a metric to fill a row.

### What Worked (lean and full)

**What it is.** What actually went well, and why it went well.

**Why it exists.** It is the half of the retrospective shape every genre read here carries, with template
attestation in each: the VA AAR template pairs "What went well and why?" with a
column for how to ensure that success in future [[19]](#ref-19), HSEEP's executive summary opens with major
strengths [[21]](#ref-21), and all three vendor templates read for this bundle carry a
version of it [[40]](#ref-40)[[47]](#ref-47)[[48]](#ref-48).

*Beginner note:* name the practice, not the mood. A sentence a stranger could copy into their own project
is the target.

*Expert note:* the VA template's column header is doing real work: it asks "and why?", and then asks how to
ensure the same success again [[19]](#ref-19). A strength with no mechanism attached is a compliment, and a
compliment does not transfer to a reader who was not there.

### What Did Not (lean and full)

**What it is.** What went wrong or fell short, with enough analysis that a reader can tell cause from
symptom.

**Why it exists.** The same cross-genre attestation as What Worked: the VA pairs "What can be improved and
how?" with a recommendations column [[19]](#ref-19), and HSEEP asks each observation to be labelled
explicitly, "Begin this section with a heading indicating whether the observation is a 'Strength' or an
'Area for Improvement.'" [[21]](#ref-21). The worked Kubernetes retrospective shows what a good entry reads
like, both the fact, "Near the end of 1.3 development, on May 13, 2016, approximately one week prior to code
freeze, a key engineer for this effort left the project," and the judgement, "In the decision to move
forward with coding beyond code freeze, not enough thought was invested in what could go wrong or how to
mitigate that" [[18]](#ref-18).

*Beginner note:* keep Kerth's Prime Directive in the room [[13]](#ref-13), and keep it honest. Its defender
is explicit that it is not an amnesty: "The prime directive doesn't mean there isn't accountability"
[[14]](#ref-14).

*Expert note:* this is the section Dingsøyr et al.'s finding is aimed at. If the document will be published,
participants may soften what they say before it is ever written down [[34]](#ref-34). Decide the
circulation of this document **before** the discussion, not after, and if it must be public, consider
keeping the sharpest material in a narrower channel rather than pretending publication is free.

### Previously Identified Issues (full only)

**What it is.** The things this retrospective is finding **again**: problems already named in an earlier
review, and what happened to the corrective actions that were supposed to close them.

**Why it exists.** It is a defining section of the accountability-grade genre, and it is worth being
precise about where the evidence comes from. GAO-19-25 names the pattern directly, reporting "a long
history of identifying corrective actions and declaring them successfully resolved" only for the same class
of problem to reappear [[17]](#ref-17). The NAO report is built on it mechanically: it "builds on our 2016
report on the Home Office's project to provide a new mobile communications service for the emergency
services" [[16]](#ref-16), restates its own prior conclusion, "We reported on ESN in September 2016 and
concluded that the Home Office was underrating the risks to delivering ESN successfully" [[16]](#ref-16),
and then marks the repeat explicitly: "How the ESN service will be governed and managed when it is a live
service is still not clear, although we identified this risk in our report in 2016" [[16]](#ref-16). The
IRS report does the same thing inside a self-authored document: "Each of the next three sections reassesses
an operational challenge identified in the Report to Congress" [[15]](#ref-15).

**The limit, stated plainly.** This research found repeat-lesson tracking **specifically in the
external-audit genre** and not in the team-authored retrospectives read. That is why it is full-only and
why the template invites it rather than demanding it: a first-of-its-kind project genuinely has no prior
review to check against, and a team forced to fill this section will invent one.

*Beginner note:* if there is a prior retrospective, review, or audit covering this work, list what it said
and what actually happened. *Raised in the phase 1 review, action assigned, not started* is a complete and
useful row.

*Expert note:* of the seven sections here, this is the one that appeared only in the accountability-grade
sources read for this bundle [[16]](#ref-16)[[17]](#ref-17), and it is also the easiest one to drop under
pressure. If it is being removed, say who removed it and why in Scope and Period rather than letting it
vanish.

### Lessons for Others (lean and full)

**What it is.** The terminal-handover section. Its entire reason for existing is **a reader who was not
there**.

**Why it exists.** This is where the two admission lineages converge. CALL's stated second purpose for a
written AAR is dissemination beyond the unit [[1]](#ref-1). The VA's template has an explicit sharing step,
"Share the AAR report with your project sponsor or other appropriate leader in your facility, VISN or
national VHA offices," and states where the value lands: "The greatest benefit of an AAR comes from applying
the lessons learned to future work and teams" [[19]](#ref-19). ITU's template asks the transferability
question directly on the page: "Could these lessons be utilized as best practices in other Regions?"
[[22]](#ref-22). DOE's Lessons Learned section asks for the same content in the same spirit: "The section
should discuss good work practices, innovative approaches, negative experiences, subcontractor performance,
deviations from what was planned versus what was performed" [[20]](#ref-20). PRINCE2's terminal Lessons
Report is described the same way, "designed to help future projects avoid common mistakes and replicate
successful practices" [[25]](#ref-25).

*Beginner note:* write each lesson so it makes sense to somebody with no context on this project. If a
lesson only parses to people who were in the room, it belongs in What Did Not, not here.

*Expert note:* Nancy Dixon's caution is the one to hold against this section: "The greatest value of lessons
learned is for those who took the action" [[32]](#ref-32). Transfer to strangers is the harder claim and the
weaker one. Write this section anyway, because it is what makes the document terminal rather than
ceremonial, but do not let it crowd out the part of the exercise that helps the people who lived it.

### Actions and Owners (lean and full)

**What it is.** What changes, who owns each change, and by when. With owners and dates, or it is a feelings
log.

**Why it exists.** This is the `process-docs` family's shared obligation, and the family contract is
explicit that every member must carry owned actions with a place they are tracked rather than a list of
observations. **It is also the section where published practice is weakest, and this bundle says so.** Of
the templates read in full, exactly one gives actions both an owner and dates: HSEEP's "Table A.1
Improvement Plan Matrix," whose columns run "Capability | Observation Title | Recommendation | Corrective
Action Description | Capability Element | Primary Responsible Agency | Agency POC | Start Date | Completion
Date" [[21]](#ref-21). The VA template has no owner or due-date field anywhere [[19]](#ref-19); ITU's
Recommendations section has none, offering only that "Priorities will be identified for the implementation
of recommendations" [[22]](#ref-22); PRINCE2's Lessons Log has no owner field at all, and the reference
describing it says so directly: "The document does not specify an 'owner' field" [[26]](#ref-26); and the two
vendor templates read in full carry neither [[47]](#ref-47)[[48]](#ref-48).

So this section is **the library's own insistence, backed by one published template and by the family
contract**, not a majority convention. That is a stronger position than it sounds, because the failure it
guards against is the one every critic in [section 6](#6-debates-and-contested-boundaries) describes.

*Beginner note:* one row, one change, one named person, one date. A row owned by a team is owned by nobody.

*Expert note:* HSEEP puts its owned actions in an **appendix**, separate from the AAR narrative
[[21]](#ref-21), which is a real design signal: the narrative is for readers, the matrix is for tracking.
If your organisation tracks work in a ticket system, put the tracking identifier in the row and let the
system own the state, so this document does not quietly become a second, stale tracker.

---

## 4. Variants and sizing

**This bundle ships two sizes, and the argument is in the corpus rather than in a convention.** The filled
and blank documents read for this research split into two genuinely different genres, and they are not two
sizes of one reader's needs.

| | Team-authored retrospective | Accountability-grade report |
|---|---|---|
| Who writes it | The team that did the work | The team, or an oversight body reviewing it |
| Who reads it | The team, its neighbours, whoever comes next | A sponsor, a board, a named official |
| Examples read | Kubernetes 1.3 Storage SIG [[18]](#ref-18), 18F's acquisition retrospective [[24]](#ref-24) | IRS Direct File [[15]](#ref-15), NAO on ESN [[16]](#ref-16), GAO-19-25 [[17]](#ref-17) |
| Length and register | Short, narrative, internal vocabulary | Long, quantified, formal, addressed |
| Tracks prior findings | Not in the examples read | Yes, structurally [[16]](#ref-16)[[17]](#ref-17) |
| Template weight | `lean` | `full` |

`lean` serves the first genre: six sections, enough to make the record durable and the actions owned.
`full` serves the second: the same six in the same order, plus **Previously Identified Issues**, plus a
quantification table inside What Happened.

**Reach for `full` when any of these is true:** money, safety or a regulator is involved; the document will
be read by someone who can stop or fund the next thing; there is a prior review of the same work whose
findings need checking; or the work is being closed formally against a baseline, which is the shape DOE
[[20]](#ref-20) and ITU [[22]](#ref-22) both template.

**One honest counter-signal.** A real filled retrospective may abandon headings entirely. 18F's published
acquisition retrospective uses none of the standard sections and is organised instead around the project's
own three named aims, introduced with "Below are the aims that we hoped to achieve" [[24]](#ref-24). That
is a legitimate shape, and it is worth knowing that the strongest worked example this research found did
not use a template at all. The template's claim is that these six sections are what this research
found missing, not that no good document was ever written without them.

---

## 5. Methodology lineage

| School | Treatment | What it optimizes for |
|---|---|---|
| **US Army doctrine, 1993** | The AAR is a verbal discussion and explicitly not a critique; the only written record is the observer's own prep notes [[2]](#ref-2). | Immediate, candid unit learning while the event is fresh. |
| **US Army doctrine, CALL 2011** | Names the verbal review and the written report as two things, publishes a written-AAR template, and states historical record plus Army-wide dissemination as its purposes [[1]](#ref-1). | A record that outlives the unit and reaches the rest of the organisation. |
| **PMI, PMBOK 6th Edition** | A named artifact: the lessons learned register, output of Manage Project Knowledge and input to a dozen later processes [[3]](#ref-3). | A living project-level knowledge record that other processes consume. |
| **PMI, PMBOK 8th Edition** | Restructured around principles; no "Lessons Learned" heading in the published table of contents, full text not read [[4]](#ref-4). | Unknown from free material; see [section 6](#6-debates-and-contested-boundaries). |
| **PRINCE2** | Splits the continuous Lessons Log from the terminal Lessons Report, and also carries lessons as one content item inside the End Project Report [[25]](#ref-25)[[26]](#ref-26)[[27]](#ref-27). | Separating running capture from the once-only handover. |
| **Kerth's project retrospectives** | A multi-day facilitated review at project end, governed by the Prime Directive, whose written output preserves wisdom past the team's breakup [[6]](#ref-6)[[13]](#ref-13). | Collective sense-making at a scale a sprint retro cannot reach. |
| **Derby and Larsen** | A five-stage facilitated session, scoped by default to one week to one month of work, with releases and project retrospectives treated separately [[8]](#ref-8)[[11]](#ref-11). | A well-run meeting, sized to the increment; the document is not the deliverable. |
| **Scrum and SAFe cadence line** | Output is backlog items, not a document: "They may even be added to the Sprint Backlog for the next Sprint" [[37]](#ref-37); "A set of improvement backlog items (Enablers, Features, or Stories) that go into the ART Backlog for consideration in the next PI Planning event" [[38]](#ref-38). | Continuous adjustment inside a running system, with no artifact to file. |
| **Government and audit genre** | Long, numbered, quantified, addressed to a named recipient, and structurally tracking prior findings [[15]](#ref-15)[[16]](#ref-16)[[17]](#ref-17)[[20]](#ref-20)[[21]](#ref-21)[[22]](#ref-22). | Accountability for public money and a defensible record of what was already known. |
| **Retro-tool vendor tier** | Boards and template menus rather than documents [[39]](#ref-39)[[40]](#ref-40); Confluence is the exception, generating persisted pages and an index across occasions [[46]](#ref-46). | Running the session; the record is a by-product except where the tool is a wiki. |

**The structural finding that separates this type from the cadence line, and it is the load-bearing one.**
Scrum and SAFe both describe the output of their retrospective events as backlog items, at team scale and
at multi-team scale alike [[37]](#ref-37)[[38]](#ref-38). **Cadence retrospectives feed a backlog; terminal
retrospectives produce a document.** That difference is why this type ships and why
`pi-release-retrospective` does not, recorded in
[ADR 0049 (pi-release-retrospective fails the admission test)](../../docs/internal/decisions/0049-pi-release-retrospective-fails-the-admission-test.md)
and evidenced in
[the admission evidence file](../../docs/internal/pi-release-retrospective-admission-evidence.md).

---

## 6. Debates and contested boundaries

### 6.1 The foundational Army source does not say what it is cited for

TC 25-20 is the older of the two Army sources, and it defines the AAR as a discussion that is explicitly
not a critique [[2]](#ref-2). The written-report admission comes from CALL's
later doctrine [[1]](#ref-1). The two are not in conflict, but a citation that attaches the written report
to TC 25-20 is making a claim its own source does not support. This bundle cites CALL for the document and TC 25-20 only for what it
actually says.

### 6.2 Does the PMBOK lessons learned register survive the Eighth Edition?

**Unresolved, and stated as unresolved.** The Sixth Edition names the register unambiguously [[3]](#ref-3).
The Eighth Edition's published table of contents has no "Lessons Learned" heading, consistent with its move
away from named process outputs [[4]](#ref-4). The full Eighth Edition text is paywalled and was not read,
and an absence in a table of contents is weak evidence about a body. PMI's free lexicon, which would be the
natural free substitute, defines the concept but not the register [[5]](#ref-5). **A reader working under
the current edition should verify this against the edition they hold rather than trusting this companion's
Sixth Edition citation to be current.**

### 6.3 Is the practice criticised, or is the document criticised?

This is the debate that shapes the whole bundle, and getting it wrong in either direction misleads.

**The criticism is real and it is specific.** Negri and Dülgerler state it at its sharpest: "even when
lessons are correctly identified, documented, and communicated, they often get lost in some sort of 'lessons
learned database' - as in, a 'black hole' (Dalton, 2013) - that nobody ever looks at" [[31]](#ref-31), and
call the traditional collect-document-communicate process "highly ineffective, because most of the time
companies fail to 'assimilate' the lessons they have identified, so people don't change their ways of doing
things" [[31]](#ref-31). Nancy Dixon, writing from knowledge management, is equally blunt: "So all those
repositories of lessons learned that we built in the early days of KM just didn't work very well and lessons
learned took on a bad name within organizations" [[32]](#ref-32). John Carter's piece is titled against
retrospectives outright and describes the artifact's fate precisely: "these flip charts are written up in
Microsoft Word document and sent to the team with a cc to some managers. The team members & managers get the
email and either file them or delete them. And life goes on" [[33]](#ref-33).

**And every one of them still recommends writing something down.** Carter, in the same piece, argues that
retrospectives "should be kept in a repository so they can be used to look at trends and provide evidence of
improvement over time" and that "every and I mean EVERY project kick off meeting should have a presentation
of the most recent retrospective" [[33]](#ref-33). Negri and Dülgerler's fix is a different container, not
no container: "if a lesson is not into the right checklist, you have not learned it!" [[31]](#ref-31), and
they trace NASA's repository failure to searchability rather than to the act of recording, reporting "one
reason why the NASA 'official' agency-wide repository for lessons learned was not widely used, was because
its lessons covered so many topics that it was difficult to search for an applicable lesson"
[[31]](#ref-31). **Dixon is the exception in this group and is not folded into it**: her guidance is about
the timing and framing of the meeting - "Meetings to construct lessons are held as soon as possible after
the outcome because memory fades quickly" and "It is framed as a meeting to learn, not to judge"
[[32]](#ref-32) - and this research records her as locating the value in **in-team sense-making rather
than in a transferable artifact**. She proposes no container at all, which is a different position from
Carter's and Negri's, and it is kept distinct here rather than absorbed. PMI's own 1999 practitioner guidance
already said where the artifact should live and how access should work [[29]](#ref-29).

**The discriminator is retrieval, wired into somebody's workflow**: a kickoff presentation, a
deliverable-specific checklist, a mandatory field. Not a general archive nobody has a reason to open. The
honest summary is **anti-deposit-and-forget, not anti-documentation**. A bundle that reported the
criticism without that distinction, as though the document itself were the target, would be overstating
its own sources.

### 6.4 Two peer-reviewed findings pull in opposite directions, and both are kept

**The document can harm the practice.** Dingsøyr et al., studying retrospectives inside a large-scale agile
programme, report that "Having minutes public could also lead to critique being toned down or removed
completely" [[34]](#ref-34). That is not inertness; it is the artifact degrading the discussion that
produces it. The same study finds the scope problem as well, "We find, however, that teams mainly deal with
team-internal issues in retrospectives" [[34]](#ref-34), with its own tally, as recorded in this bundle's
research log, putting 17 of 109 issues and 6 of 36 action items in large-scale categories, and it doubts the
depth of the learning, "Given the short time spent on retrospectives, they do not seem to facilitate 'deep'
learning" [[34]](#ref-34).

**The absence of the document can harm the organisation.** Anandayuvaraj et al., studying engineers at a
national space research centre, find the opposite failure: "knowledge loss due to team turnover & fragmented
documentation" [[35]](#ref-35), practitioners reporting that "I don't think they are documented, pretty much
at all" [[35]](#ref-35), and failure knowledge "not referenced once [the project] is closed"
[[35]](#ref-35). One interview quote captures the retrieval problem exactly: "I didn't know where to find
stuff...I didn't know what was documented in GitLab...in the wiki...on the team [channel]...And people don't
know that it's there and don't look at it. So it doesn't really help" [[35]](#ref-35).

GAO found the same absence pattern in a different sector, warning that "relying on person-to-person
discussions to share lessons learned can be problematic because personal networks can dissolve"
[[17]](#ref-17).

**Both are carried.** A bundle holding only the first would be arguing against its own artifact; one holding
only the second would be ignoring a documented harm. The practical reading: decide circulation before the
discussion, and write the document for a named reader rather than for an archive.

### 6.5 Is the end of the project simply too late?

The Agile Alliance's page for *Agile Retrospectives* states the cadence camp's objection directly:
retrospectives "are only held at the end of the project - too late to help" [[9]](#ref-9). The book itself
draws the same contrast, "in contrast to traditional postmortems or project reviews, retrospectives focus
not only on the development process, but on the team and team issues" [[8]](#ref-8).

**That objection is about improving the project you are in, and it is correct on its own terms.** It is not
an argument against this document, whose readers are the next project and the organisation, not the team
that is finishing. Both can be true: run cadence retrospectives to improve the work in flight, and write
this document because the team is about to stop existing [[6]](#ref-6). A team running only one of the two
is missing something real.

### 6.6 The name itself carries baggage

A practitioner piece contrasting the two names reports the reaction plainly: "try telling a group of people
you are scheduling a lessons-learned meeting and look for the eye-rolls!" [[36]](#ref-36). This is a single
practitioner observation, not measured evidence, and is recorded here as colour rather than as a finding.
The practical consequence is small and real: the catalog aliases exist so the type is findable under
whichever name an organisation uses, and a team free to choose can pick the one that will not lose the room.

### 6.7 Does the Prime Directive survive contact with a real audience?

Its defender records live resistance to it, reporting that during a talk "a person in the audience shouted
to me 'that is a lie!'" [[14]](#ref-14) and answering that "The prime directive doesn't mean there isn't
accountability" [[14]](#ref-14). The wording quoted in [section 2](#2-origins-and-evolution) comes from a
community wiki rather than from the book's own page [[13]](#ref-13), because the sampled chapters did not
include it. Treat the Directive as a facilitation stance with a named defender and one recorded objection, not as a
settled rule.

---

## 7. Anti-patterns and failure modes

1. **The black hole.** Lessons "get lost in some sort of 'lessons learned database' ... that nobody ever
   looks at" [[31]](#ref-31). The named fix is not less writing, it is a retrieval path somebody actually
   walks [[31]](#ref-31)[[33]](#ref-33).
2. **A repository too broad to search.** NASA's agency-wide lessons repository "was not widely used ...
   because its lessons covered so many topics that it was difficult to search for an applicable lesson"
   [[31]](#ref-31). Reported by a practitioner paper citing a 2002 source rather than observed firsthand
   here.
3. **Written up, emailed, filed, deleted.** The fate one critic describes in detail, while still wanting
   the document written [[33]](#ref-33).
4. **Held so late that memory has gone.** "Meetings to construct lessons are held as soon as possible after
   the outcome because memory fades quickly" [[32]](#ref-32). Kerth's own timing rationale is the same one,
   run against team dispersal rather than memory [[6]](#ref-6).
5. **Publication that quietly censors the content.** "Having minutes public could also lead to critique
   being toned down or removed completely" [[34]](#ref-34). The failure happens before the document exists,
   which is why circulation is a Scope and Period decision.
6. **Not writing it at all, and losing it to turnover.** "knowledge loss due to team turnover & fragmented
   documentation" [[35]](#ref-35), and GAO's warning that personal networks "can dissolve" [[17]](#ref-17).
7. **Capturing lessons only at the end, when the expensive decisions were early.** GAO found that
   "DOE Order 413.3B's requirements for project management lessons learned do not require that all lessons
   learned be submitted routinely or in a timely manner," leaving the earliest planning and design phases
   uncovered [[17]](#ref-17).
8. **Declaring corrective actions resolved and meeting the same problem again.** "a long history of
   identifying corrective actions and declaring them successfully resolved" [[17]](#ref-17). This is the
   failure Previously Identified Issues exists to catch (see
   [section 3](#3-anatomy-section-by-section)).
9. **Actions with no owner and no date.** The family's shared failure mode, and the one published practice
   is worst at: only one template read gives an action both an owner and dates [[21]](#ref-21), while
   several prominent ones give neither [[19]](#ref-19)[[26]](#ref-26)[[47]](#ref-47)[[48]](#ref-48).
10. **Scope that never leaves the team.** Even inside a large multi-team programme, "teams mainly deal with
    team-internal issues in retrospectives" [[34]](#ref-34). For a terminal document whose point is a reader
    who was not there, that is fatal rather than merely limiting.
11. **A ceremony with nothing behind it.** "Retrospectives performed at this level are less beneficial than
    a celebration dinner" [[33]](#ref-33).
12. **Writing for an archive instead of a person.** The IRS example shows the opposite done deliberately,
    findings reframed because a specific decision was pending [[15]](#ref-15); PMI's own older guidance asks
    the template to "segregate data by target audiences" [[29]](#ref-29).

---

## 8. Relationships to other artifacts

**Sibling, different trigger: `sprint-retrospective-notes`.** A sprint retrospective looks back on a
**period**, on a cadence, at how the team worked; its canonical output is not a document at all but a change
that may travel into the next Sprint Backlog [[37]](#ref-37), and the event "concludes the Sprint"
[[37]](#ref-37). This document looks back on **a bounded piece of work that has ended**. Vendor vocabulary
draws the same line from the other side: "sprint retrospectives take place multiple times at a regular
cadence throughout the course of a project. But the project post-mortem only takes place once," and its
scope covers "the entire project roadmap from start to finish" [[39]](#ref-39). Another names the register
difference: "Sprint retrospectives are tactical" against "Release retrospectives are strategic"
[[41]](#ref-41). **If the trigger is the calendar and the audience is the team that will keep working
together, reach for `sprint-retrospective-notes`. If the work has ended and part of the audience was not
there, reach for this one.**

**Sibling, different trigger again: `incident-postmortem`.** A postmortem is **event-triggered** learning
about a specific failure. Named sources draw this by purpose: "Post-mortems attempt to understand what went
wrong," while "Retrospectives, on the other hand, primarily engage and serve the team doing the work"
[[42]](#ref-42), and, more directly, "Retrospectives exist to encourage regular retrospection, whereas
postmortems serve to understand root causes of incidents and prevent future reoccurences" [[43]](#ref-43).
**If a specific thing failed and the question is why, reach for `incident-postmortem`, even if the project
also just ended.**

**The library's own framing, labelled as such.** This family's contract states that the common real-world
error runs both ways, a retro run on an incident or a postmortem run on ordinary work. Per the contract's
own change note, **no source read states that**, and it is carried here as this library's reasoning rather
than as received practice. The counterexamples are live and named: Honeycomb calls its incident process an
incident review and prefers "blame-aware incident reviews" [[44]](#ref-44), and FireHydrant splits the word
"retrospective" into an incident type and a project type, describing the second as the one that "takes place
after project completion where the team looks at the project from the start to the end" [[45]](#ref-45).
**Industry vocabulary is less settled than a clean three-way split implies, and this bundle says so rather
than asserting a consensus that does not exist.**

**The member that does not exist: `pi-release-retrospective`.** The same research pass that admitted this
type refused that one, and the reason is structural rather than editorial. SAFe's own facilitator guide names
the Inspect and Adapt event's outputs as "A set of improvement backlog items (Enablers, Features, or Stories)
that go into the ART Backlog for consideration in the next PI Planning event" [[38]](#ref-38), with no
document anywhere in it, and the Scrum Guide describes the team-scale event the same way [[37]](#ref-37). See
[ADR 0049 (pi-release-retrospective fails the admission test)](../../docs/internal/decisions/0049-pi-release-retrospective-fails-the-admission-test.md).

**Upstream of this document: the running record.** Both major methodologies separate continuous capture from
terminal reporting. PRINCE2 keeps a Lessons Log, "a repository for lessons that may benefit current and
future projects" [[26]](#ref-26), and produces the terminal Lessons Report from it: "the project manager
produces a lessons report using information from the lessons log" [[25]](#ref-25). PMBOK's register plays the
running-record role [[3]](#ref-3), and a training-vendor summary draws the same split in PMI's vocabulary,
between "Project-level documentation, updated throughout the project or phase" and "An organizational
repository, updated at project or phase closure, accessible to future teams and stakeholders"
[[28]](#ref-28). **If your organisation keeps a running log, this document is written from it, not instead of
it.**

**Adjacent, overlapping, not the same: the formal closeout report.** PRINCE2's End Project Report carries
lessons as one content item inside a broader report, "A summary of key insights that can benefit future
projects" [[27]](#ref-27), and DOE's closeout report does the same, with a Lessons Learned section sitting
beside baseline, closeout status and archive sections [[20]](#ref-20). Where an organisation mandates a
closeout report, this document is best used as the lessons content inside it rather than as a competing
artifact.

**Downstream: wherever actions are actually tracked.** HSEEP's design is the model, keeping the narrative
separate from the improvement matrix that carries owners and dates [[21]](#ref-21). This library's family
contract allows actions to land in the `product-backlog`, the `risk-register` or the `raid-log`, and is
explicit that **only the ticket-tracker destination reflects published practice**; the other two are this
library's own convention.

**Where the document lives.** Confluence is the one surveyed tool whose native retrospective artifact is a
persisted page rather than a board, and it builds the index for you: "The first time you create a
retrospective page in a space, Confluence will automatically create an 'index' page, which will list all
retrospectives in the space" [[46]](#ref-46). An index is exactly the retrieval affordance
[section 6](#6-debates-and-contested-boundaries) says the critics are missing.

---

## 9. Adaptations

- **Public money, safety, or a regulator.** Use `full`. Lead with quantities, address the document to a
  named recipient, and fill Previously Identified Issues properly. The government corpus read here is
  consistent on all three points [[15]](#ref-15)[[16]](#ref-16)[[17]](#ref-17)[[20]](#ref-20)
  [[21]](#ref-21)[[22]](#ref-22).
- **An end-of-phase boundary inside continuing work.** This is a recognised occasion in its own right. The
  UK Service Manual lists end-of-phase retrospectives separately from ordinary retrospective meetings, notes
  that they "usually include people who've been involved in the work from outside the team, too, like
  procurement or policy colleagues," and frames the output forward: "This can help identify what could be
  improved in the next phase of the project" [[23]](#ref-23). Use `lean`, and be strict about Scope and
  Period, because the boundary is a decision rather than a fact.
- **A short, self-contained delivery by one team.** Use `lean` and keep it short. Kubernetes' Storage SIG
  retrospective is a good model of the register: factual, specific, unsparing about its own decisions, and
  candid about reach, "The Storage SIG decisions were not advertised widely enough outside of the SIG early
  on" [[18]](#ref-18).
- **A project already dispersed before anyone wrote anything.** Write it anyway, and say in Scope and Period
  who was reachable and who was not. The alternative is the failure mode two independent sources describe,
  where knowledge leaves with the people [[17]](#ref-17)[[35]](#ref-35).
- **An organisation with no repository and no retrieval habit.** Do not let this become a filing exercise.
  Name a specific next use in Scope and Period, and prefer a destination somebody already opens, the way the
  critics themselves recommend: a kickoff presentation of the most recent retrospective [[33]](#ref-33), or
  a checklist that gets consulted [[31]](#ref-31).
- **A team that will publish the document widely.** Decide that before the discussion and tell participants,
  because publication can cost you the content [[34]](#ref-34). If the sharpest material cannot be
  published, say in Scope and Period that a narrower account exists and who holds it, rather than letting
  the published version imply it is the whole story.
- **A regulated organisation using the AAR name.** The civilian AAR template tradition is real and worth
  matching on vocabulary: background, participants, what went well and why, what can be improved and how,
  and an explicit sharing step [[19]](#ref-19). Map this template's sections onto those headings rather than
  fighting your organisation's forms.

---

## 10. Worked example pointer

[`project-milestone-retrospective_example.md`](project-milestone-retrospective_example.md) is the fully
worked instance: one bounded piece of work from the library's Acme Analytics thread, closed out, with every
section filled and no placeholders left.

What it is there to demonstrate is the boundary this bundle exists to teach. It is written to be told apart
from its two siblings at a glance: it is not a cadence review of how the team worked, and it is not a causal
analysis of a single failure, even though the same programme contains one. Read it alongside
[`sprint-retrospective-notes_example.md`](../sprint-retrospective-notes/sprint-retrospective-notes_example.md)
and [`incident-postmortem_example.md`](../incident-postmortem/incident-postmortem_example.md), which cover
the same programme from the other two angles.

---

## References

Tagged by reliability, following this bundle's own split: `[primary]` the originating or first-party source
itself; `[standards]` a named professional or doctrinal body's own guidance; `[academic]` peer-reviewed
research; `[practitioner]` a recognized independent authority or named professional; `[reference]` a
community or catalog reproduction of a source that is itself paywalled or unavailable; `[vendor]`
commercially motivated, reliable on convention. The 48 entries below are 9 primary, 6 standards, 2 academic,
14 practitioner, 6 reference and 11 vendor. Researched 2026-09-12. **Every entry below is recorded as
fetched-and-verified** in
[`project-milestone-retrospective_research-log.md`](project-milestone-retrospective_research-log.md), which
also records the sources that were paywalled, blocked or unread and therefore quoted nowhere in this bundle.

<a id="ref-1"></a>[1] Center for Army Lessons Learned (CALL), US Army. "[CALL Handbook 11-33: Establishing a Lessons Learned Program, Appendix C: Military After Action Reports/Reviews](https://www.globalsecurity.org/military/library/report/call/call_11-33-appc.htm)." June 2011, read via the globalsecurity.org reproduction (accessed 2026-09-12). [standards]

<a id="ref-2"></a>[2] US Army, Headquarters Department of the Army. "[TC 25-20: A Leader's Guide to After-Action Reviews](https://nick.groenen.me/attachments/public/gitignored/TC%2025-20%20A%20Leader's%20Guide%20to%20After-Action%20Reviews.pdf)." 1993, read via a personal-site mirror of the training circular PDF (accessed 2026-09-12). [standards]

<a id="ref-3"></a>[3] Project Management Institute. "[A Guide to the Project Management Body of Knowledge (PMBOK Guide), Sixth Edition, Errata, 3rd Printing](https://www.pmi.org/-/media/pmi/documents/public/pdf/pmbok-standards/pmbok-guide-6th-errata.pdf)." PMI, 2017, fetched directly from pmi.org (accessed 2026-09-12). Cited for the Sixth Edition only; see [section 6](#6-debates-and-contested-boundaries). [standards]

<a id="ref-4"></a>[4] Project Management Institute. "[PMBOK Guide, Eighth Edition, Table of Contents](https://www.pmi.org/-/media/pmi/documents/public/pdf/publications/pmbok-guide-eighth-edition_table-of-contents.pdf)." PMI (accessed 2026-09-12). Read only as a negative check on the table of contents; the full edition is paywalled and was not read. [standards]

<a id="ref-5"></a>[5] Project Management Institute. "[PMI Lexicon of Project Management Terms, Version 3.2](https://vets2pm.com/wp-content/uploads/2024/10/pmi-lexicon-pm-terms.pdf)." PMI, September 2017, read via a third-party mirror after PMI's own URL returned HTTP 403; authenticity checked against the document's own PMI copyright page (accessed 2026-09-12). [standards]

<a id="ref-6"></a>[6] Norman L. Kerth. "[Project Retrospectives: A Handbook for Team Reviews](https://ptgmedia.pearsoncmg.com/images/9780133488579/samplepages/0133488578.pdf)," publisher's free sample. Dorset House, 2001, via Pearson/InformIT (accessed 2026-09-12). Front matter, Chapter 3, table of contents and index only; the complete book was not retrieved. [primary]

<a id="ref-7"></a>[7] Google Books. "[Project Retrospectives: A Handbook for Team Reviews](https://books.google.com/books/about/Project_Retrospectives.html?id=BxROAQAAIAAJ)," publisher-sourced catalog page. books.google.com (accessed 2026-09-12). [reference]

<a id="ref-8"></a>[8] Esther Derby and Diana Larsen. "[Agile Retrospectives: Making Good Teams Great](https://agile.2ia.net/Agile%20Retrospectives.pdf)." The Pragmatic Bookshelf, 2006, read via a third-party PDF mirror and cross-checked against the publisher and Agile Alliance pages below (accessed 2026-09-12). [primary]

<a id="ref-9"></a>[9] Agile Alliance. "[Agile Retrospectives: Making Good Teams Great!](https://agilealliance.org/resources/books/agile-retrospectives-making-good-teams-great/)," book resource page. agilealliance.org (accessed 2026-09-12). [practitioner]

<a id="ref-10"></a>[10] The Pragmatic Bookshelf. "[Agile Retrospectives: Making Good Teams Great](https://pragprog.com/titles/dlret/agile-retrospectives/)," publisher page and author biography. pragprog.com (accessed 2026-09-12). [vendor]

<a id="ref-11"></a>[11] Goodreads. "[Agile Retrospectives: Making Good Teams Great](https://www.goodreads.com/book/show/721338.Agile_Retrospectives)," book page and chapter-level table of contents. goodreads.com (accessed 2026-09-12). Cited for the chapter title only; the chapter body was not read. [reference]

<a id="ref-12"></a>[12] Marc Loeffler. "[Improving Agile Retrospectives: The Retrospective Phase Model](https://www.informit.com/articles/article.aspx?p=2916288&seqNum=3)," book excerpt. Pearson/InformIT, 2018 (accessed 2026-09-12). [practitioner]

<a id="ref-13"></a>[13] Agile Retrospective Resource Wiki. "[The Prime Directive](https://retrospectivewiki.org/index.php?title=The_Prime_Directive)." retrospectivewiki.org (accessed 2026-09-12). Used for the Directive's wording because the retrieved Kerth sample did not include the page it appears on. [reference]

<a id="ref-14"></a>[14] Enrico Teotti. "[Analyze Kerth prime directive](https://teotti.com/analyze-kerth-prime-directive/)." teotti.com, 2018 (accessed 2026-09-12). [practitioner]

<a id="ref-15"></a>[15] Internal Revenue Service, US Department of the Treasury. "[IRS Direct File Pilot Program: Filing Season 2024 After Action Report](https://www.irs.gov/pub/irs-pdf/p5969.pdf)" (Pub. 5969). irs.gov (accessed 2026-09-12). Cover through Section I read in detail. [primary]

<a id="ref-16"></a>[16] National Audit Office (UK). "[Progress delivering the Emergency Services Network](https://www.nao.org.uk/wp-content/uploads/2019/05/Progress-delivering-the-Emergency-Services-Network.pdf)" (HC 2140, Session 2017 to 2019). nao.org.uk (accessed 2026-09-12). Cover, key facts, full summary and lettered recommendations read. An oversight-body audit rather than a team-authored retrospective. [primary]

<a id="ref-17"></a>[17] US Government Accountability Office. "[Project Management: DOE and NNSA Should Improve Their Lessons-Learned Process for Capital Asset Projects](https://www.gao.gov/assets/gao-19-25.pdf)" (GAO-19-25). gao.gov (accessed 2026-09-12). [primary]

<a id="ref-18"></a>[18] Kubernetes Storage SIG (Brad Childs, Michael Rubin and others). "[Kubernetes 1.3 Storage Retrospective](https://github.com/kubernetes/community/tree/main/sig-storage/1.3-retrospective)." github.com (accessed 2026-09-12). Full document text read. [practitioner]

<a id="ref-19"></a>[19] Susanne Salem-Schatz, Diana Ordin and Brian Mittman. "[Guide to the After Action Review](https://cebma.org/assets/Uploads/Salem-Schatz-Guide-to-the-After-Action-Review.pdf)," v1.1. VA Center for Implementation Practice and Research Support / VA Office of Quality and Performance, October 2010 (accessed 2026-09-12). [practitioner]

<a id="ref-20"></a>[20] US Department of Energy, Office of Science. "[Template for Closeout Report](https://science.osti.gov/-/media/opa/word/SC_Project_Closeout_Report_v6.docx)," Project Closeout Report v6. science.osti.gov (accessed 2026-09-12). Verified by direct extraction of the document XML rather than by tool summarization. [primary]

<a id="ref-21"></a>[21] US Department of Homeland Security / FEMA, Homeland Security Exercise and Evaluation Program. "[After Action Report/Improvement Plan (AAR/IP) Template](https://www.rac-g.org/docs/AARIP_Template.pdf)." rac-g.org (accessed 2026-09-12). [primary]

<a id="ref-22"></a>[22] International Telecommunication Union, ITU-D. "[Post Implementation Review Template](https://www.itu.int/en/itu-d/projects/documents/templatepostimplementationreview.pdf)." itu.int (accessed 2026-09-12). An ITU internal project-management template, not an ITU-T Recommendation. [standards]

<a id="ref-23"></a>[23] UK Government Digital Service. "[Agile tools and techniques](https://www.gov.uk/service-manual/agile-delivery/agile-tools-techniques)," GOV.UK Service Manual. gov.uk (accessed 2026-09-12). [primary]

<a id="ref-24"></a>[24] Rebecca Refoy, Ashley Owens, Omid Ghaffari-Tabrizi and Michelle McNellis. "[An Acquisition Retrospective](https://18f.gsa.gov/2020/03/18/an-acquisition-retrospective/)." 18F / GSA Technology Transformation Services, 18 March 2020, retrieved via the Internet Archive because 18F was shut down in March 2025 and the live URL no longer resolves (accessed 2026-09-12). [practitioner]

<a id="ref-25"></a>[25] PRINCE2 Wiki. "[Lessons Report](https://prince2.wiki/management-products/reports/lessons-report/)," management product description. prince2.wiki (accessed 2026-09-12). A third-party community reproduction; AXELOS's own manual is paywalled and was not read. [reference]

<a id="ref-26"></a>[26] PRINCE2 Wiki. "[Lessons log](https://prince2.wiki/management-products/project-log/lessons-log/)," management product description. prince2.wiki (accessed 2026-09-12). Third-party reproduction; PRINCE2's own wording was not retrieved. [reference]

<a id="ref-27"></a>[27] PRINCE2 Wiki. "[End Project Report](https://prince2.wiki/management-products/reports/end-project-report/)," management product description. prince2.wiki (accessed 2026-09-12). Third-party reproduction. [reference]

<a id="ref-28"></a>[28] BrainSensei. "[Mastering the Lessons Learned Register for PMP and CAPM Exams](https://brainsensei.com/mastering-the-lessons-learned-register/)." brainsensei.com (accessed 2026-09-12). An exam-prep vendor describing PMBOK, not PMI's own text. [vendor]

<a id="ref-29"></a>[29] Adrian Abramovici. "[Gathering and using lessons learned](https://www.pmi.org/learning/library/gathering-using-lessons-learned-5116)." PM Network 13(10), Project Management Institute, October 1999 (accessed 2026-09-12). The only PMI-hosted lessons-learned article this research could read in full. [practitioner]

<a id="ref-30"></a>[30] PMI Learning Library, individually authored conference paper. "[Lessons Learned: Do it Early, Do it Often](https://www.pmi.org/learning/library/lessons-learned-early-often-6746)." pmi.org (accessed 2026-09-12). Written against the PMBOK Guide Fourth Edition. [practitioner]

<a id="ref-31"></a>[31] Marco Negri and Mustafa Dülgerler. "[Lessons (Really) Learned? How to Retain Project Knowledge and Avoid Recurring Nightmares](https://www.pmi.org/learning/library/knowledge-management-lessons-learned-10161)." PMI Global Congress 2016 EMEA (accessed 2026-09-12). A practitioner congress paper, not blind-peer-reviewed; its NASA repository claim is itself cited to Li (2002) and was not independently verified here. [practitioner]

<a id="ref-32"></a>[32] Nancy Dixon. "[The Value of Lessons Learned](https://web.archive.org/web/2015id_/http://www.nancydixonblog.com/2010/02/the-value-of-lessons-learned.html)." nancydixonblog.com, February 2010, retrieved via the Internet Archive because the original domain has lapsed (accessed 2026-09-12). [practitioner]

<a id="ref-33"></a>[33] John Carter. "[Why Retrospectives are a Waste of Time](https://www.tcgen.com/blog/why-retrospectives-are-a-waste-of-time/)." TCGen, May 2023, updated July 2024 (accessed 2026-09-12). [practitioner]

<a id="ref-34"></a>[34] Torgeir Dingsøyr, Marius Mikalsen, Anniken Solem and Kathrine Vestues. "[Learning in the Large: An Exploratory Study of Retrospectives in Large-Scale Agile Development](https://arxiv.org/pdf/1805.10310)." XP2018, Springer LNBIP vol. 314 (accessed 2026-09-12). Read as the arXiv postprint of the published version. [academic]

<a id="ref-35"></a>[35] Dharun Anandayuvaraj, Tanmay Singla, Zain A. H. Hammadeh, Andreas Lund, Alexandra Holloway and James C. Davis. "[Learning From Software Failures: A Case Study at a National Space Research Center](https://arxiv.org/pdf/2509.06301)." ICSE 2026 (accessed 2026-09-12). Read as an arXiv preprint, not in final published form. [academic]

<a id="ref-36"></a>[36] Jake Calabrese. "[Lessons-Learned vs Project Retrospectives](https://helpingimprove.com/lessons-learned-vs-project-retrospectives/)." Helping Improve LLC (accessed 2026-09-12). [practitioner]

<a id="ref-37"></a>[37] Ken Schwaber and Jeff Sutherland. "[The Scrum Guide](https://scrumguides.org/docs/scrumguide/v2020/2020-Scrum-Guide-US.pdf)," November 2020. scrumguides.org (accessed 2026-09-12). [primary]

<a id="ref-38"></a>[38] Scaled Agile, Inc. "[SAFe Inspect and Adapt: Facilitator's Guide](https://framework.scaledagile.com/wp-content/uploads/2026/03/SAFe-Inspect-and-Adapt-Facilitators-Guide.pdf)." framework.scaledagile.com (accessed 2026-09-12). Four-page guide read in full. [vendor]

<a id="ref-39"></a>[39] EasyRetro. "[The Project Post-Mortem Retrospective Template](https://easyretro.io/templates/post-mortem-retrospective/)." easyretro.io (accessed 2026-09-12). [vendor]

<a id="ref-40"></a>[40] EasyRetro. "[Project Retrospective Template](https://easyretro.io/templates/project-retrospective-template/)." easyretro.io (accessed 2026-09-12). Delivers a three-column board rather than a document. [vendor]

<a id="ref-41"></a>[41] TeamRetro. "[Sprint retrospective vs. release retrospective](https://www.teamretro.com/blog/sprint-retrospective-vs-release-retrospective/)," company blog. teamretro.com (accessed 2026-09-12). [vendor]

<a id="ref-42"></a>[42] Parabol. "[Post-mortems vs Retrospectives: What's the Difference](https://www.parabol.co/blog/retrospectives-vs-post-mortems/)," company blog. parabol.co (accessed 2026-09-12). [vendor]

<a id="ref-43"></a>[43] Jonathan Hall. "[Retrospectives or Postmortems?](https://jhall.io/archive/2021/07/31/retrospectives-or-postmortems/)" jhall.io, 2021 (accessed 2026-09-12). [practitioner]

<a id="ref-44"></a>[44] Honeycomb. "[The Incident Retrospective Ground Rules](https://www.honeycomb.io/blog/incident-retrospective-ground-rules)," company engineering blog. honeycomb.io (accessed 2026-09-12). [practitioner]

<a id="ref-45"></a>[45] FireHydrant. "[What are Blameless Retrospectives? How Do You Run Them?](https://firehydrant.com/blog/what-are-blameless-retrospectives-do-they-work-how/)," company blog. firehydrant.com (accessed 2026-09-12). [vendor]

<a id="ref-46"></a>[46] Atlassian. "[Retrospective Blueprint](https://confluence.atlassian.com/doc/retrospective-blueprint-427623496.html)," Confluence documentation. confluence.atlassian.com (accessed 2026-09-12). [vendor]

<a id="ref-47"></a>[47] Smartsheet Inc. "[Free Project Management Lessons Learned Templates](https://www.smartsheet.com/content/lessons-learned-template)." smartsheet.com (accessed 2026-09-12). Cited for its published section list, which carries no owner or due-date field. [vendor]

<a id="ref-48"></a>[48] ProjectManager.com. "[Project Retrospective Template for Word](https://www.projectmanager.com/templates/project-retrospective-template)." projectmanager.com (accessed 2026-09-12). Cited for its published section list, which carries no owner or due-date field. [vendor]
