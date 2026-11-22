# Companion: Design Principles

> The deep explainer for the design-principles bundle. Read this to understand what a design principles
> document is, what published sets put in each principle, and where practitioners disagree about conflict,
> ranking, generic principles and the right number. The short operator card is
> [`design-principles_guide.md`](design-principles_guide.md); a fully worked instance is
> [`design-principles_example.md`](design-principles_example.md). Inline citations like
> [[1]](#ref-1) resolve to the [References](#references) at the bottom, numbered exactly as the research log
> numbers them. The full retrieval trail, including the pages this bundle could not read, is
> [`design-principles_research-log.md`](design-principles_research-log.md).
> This bundle sits in the `standing-standards` family as a **foundation**: a standard that a team's
> experience decisions are judged against, not an instrument executed under time pressure, per
> [ADR 0089 (design principles joins standing-standards as a foundation)](../../docs/internal/decisions/0089-design-principles-joins-standing-standards-as-a-foundation.md).

---

## 1. Orientation and TL;DR

A design principles document is a short list of value statements that one team agrees once and then uses
to frame and settle decisions about the experience of its product. Nielsen Norman Group (NN/g) defines the
type as "value statements that describe the most important goals that a product or service should deliver
for users and are used to frame design decisions" [[1]](#ref-1). principles.design gives a second
definition that matches it: "Design principles are clear statements that help teams make consistent
decisions and trade-offs when designing products, services, or systems." [[2]](#ref-2)

The job in one sentence: a short, standing page that tells the people who design and review the product
which way their decisions should lean when two good options compete, and who changes that lean when
conditions change.

**At a glance**

- **It is a direction document, not a craft document.** NN/g says these principles are "specific to the
  product or service" and "not directions on how to design specific UI elements (like design patterns or
  standards)" [[1]](#ref-1). Ben Brignell, who curates principles.design, puts the same line as "Design
  principles belong to direction and judgement." [[19]](#ref-19)
- **A principle that rules nothing out is a slogan.** Brignell writes "A slogan describes intent. A
  principle guides a choice." [[18]](#ref-18) Jay Mistry writes "Most design principles read like
  motivational posters." [[20]](#ref-20) No source read defends the poster.
- **The one set with a dated history changed rarely, and on an event.** GOV.UK's update history records
  three entries over thirteen years [[13]](#ref-13), and the 2025 addition followed a working group, not a
  date [[14]](#ref-14). No source read states a revision interval, so this rests on thin evidence.
- **The strongest finding is negative.** Across the five sets whose per-principle fields this research
  tabulated (GitLab Pajamas, USWDS, the NHS, IBM and Microsoft), none carries a field for the evidence
  behind a principle, and only a vendor's AI prompt asks what a principle rules out [[11]](#ref-11). The
  template asks for both and says so.
- **Every count of principles is a heuristic.** NN/g warns that "having 10 or more leads to many being
  forgotten" [[1]](#ref-1), and Brignell says "The most effective examples use 3-5 principles."
  [[18]](#ref-18). None of the sources cites a measurement.

If you read nothing else: write principles so that a designer could disagree with them, and say what each
one rules out. The rest of the template is structure around that test.

**Confidence.** High on the definition and the two exclusions, which two publishers state. Medium
on the section design, because no source publishes a template and most of the structure is the library's
own position. Low to medium on any claim about how often sets change, because three dated entries on one
page are a thin base.

## 2. Origins and evolution

**No source read names who first wrote about a team writing its own design principles, or when.** This
companion therefore names no originator. What the dated sources show is a practice already established by
the early 2010s.

- **Jared Spool's article on six tests for design principles is dated 1 March 2011** [[4]](#ref-4). It is the
  earliest dated method piece this research read. Its tests name elements a principle should carry, and
  later sections of this companion use several of them.
- **GOV.UK's set was first published on 3 April 2012** [[13]](#ref-13). A 2025 post by the same service says
  the principles "have been guiding the design for government services since their creation in 2012"
  [[14]](#ref-14). This research cannot say it was the first public set, only that it is an early dated one.
- **Alla Kholmatova's 2018 talk lists earlier writing** by Spool and by Stephen Anderson, under the titles
  "Creating Great Design Principles Jared M. Spool" and "Principles To Build By Stephen Anderson", with no
  dates [[3]](#ref-3). It also quotes a Government Digital Service principle, "This is for everyone"
  [[3]](#ref-3). Her slides are slide text only, so the reasoning behind each slide is not visible.
- **NN/g's article is dated 2 August 2020** [[1]](#ref-1). It is a definition and method source. It is not
  an origin source, and this companion does not use it as one.
- **Replacement is part of the record.** Spotify published a new set of three principles on 8 July 2020 after
  auditing its predecessor of six, which dated from 2013, and the audit named three defects in that
  predecessor, among them "Overlapping concepts" [[17]](#ref-17). Spool expects the same, writing that "old
  principles will need to go into storage" [[4]](#ref-4).

principles.design is a maintained collection of published sets, and it lists a "Fisher-Price Toy Making
Principles" set credited to "Irving Price and Helen Schelle" [[2]](#ref-2). No source read dates that set,
so this companion draws no lineage from it.

**What the research did not find.** This research did not find a source that traces how the form of a design
principles document changed over time, or what it replaced. The type does not appear to have a founding text. It reads as a convergence of
practitioner writing, which is why the next section reports sets and arguments, not a lineage.

**Time-bound items.** Brignell's two 2026 articles [[18]](#ref-18), [[19]](#ref-19) and NN/g's 2025 design
guidance article [[23]](#ref-23) are recent, and the principles.design collection changes. The GOV.UK set
changed on 2 April 2025 [[13]](#ref-13). Re-read any of these before relying on it as current.

## 3. Anatomy (section by section)

The template has six sections, in one size. **No source publishes a template for a design principles
document**, so every section was assembled from published sets and method articles, and most of the
structure is the library's own position. Each subsection below says which parts a source supports and which
parts are the library's. Sections 2 and 3 carry the weight, and section 6 carries the family's obligation.

### Purpose and Scope

**What it is.** The product or service the principles cover, who applies them, how they relate to the
design system, which kinds of decision they do not settle, and which principles, if any, also settle what
the team builds. It is short.

**Why it exists.** NN/g says "Design principles are specific to the product or service that is being
designed." [[1]](#ref-1) Brignell makes the same point from the other side: "Design principles are unique
to an organisation, team or project." [[19]](#ref-19) The library's reading is that a set with no stated scope leaves a new product with no way to know whether
the set covers it. Spool's test asks the same question as a question: "Have You Evaluated it for This
Project?" [[4]](#ref-4) Stuart Blackie separates industry heuristics, team principles and business or program
principles, which implies that a set should say which kind it is [[22]](#ref-22). NN/g says to "Publish them
in blogs or with your design system" [[1]](#ref-1).

**The relation to the design system is the library's position.** GitLab says its principles "are outlined in
the Pajamas Design System and guide all product design work" [[15]](#ref-15). The U.S. Web Design System
(USWDS) says "These design principles are one set of shared values, and the design language of the U.S.
Web Design System is another." [[6]](#ref-6) Between them, the sources show one team keeping its principles
inside its design system and another naming the two as separate sets of values. The template asks the author
to state the relation and does not prescribe one.

**The straddling field is the library's position.** The last field, "Principles that also settle what the
team builds", asks the author to name any principle that also decides what the team builds, funds or
declines, and to say why, or to write "None" with a reason. It follows from the working test in section 8,
which is the library's inference at medium-low confidence. No source read asks for such a field, and
published sets cross the line it guards [[23]](#ref-23), [[6]](#ref-6).

**Beginner note.** Name the product or products, say who applies the set (designers, or designers and
product managers and engineers), and say whether a design system exists that the set sits beside or inside.
One sentence for each is enough. Then apply the what-does-it-settle test to each principle before you write
the straddling field.

**Expert note.** The scope statement is where the line with `product-principles` is first drawn. If the
author finds the scope drifting toward what the team should build or decline, the document has strayed
into the sibling's territory (see section 8). Scope also decides when the set is reopened, because a new
product that falls inside the scope is a Review Trigger condition.

### The Principles

**What it is.** The set itself: three to five principles, each carrying five fields. This is the document.
The rest of the template exists to keep these five fields honest.

**Why it exists.** NN/g's definition makes principles the thing that "frame design decisions"
[[1]](#ref-1), so the principles themselves have to be specific enough to frame one. The published sets
differ both in how many principles they carry (three to eleven) and in what each one carries. The table
below states what the research found for each field, and where a field has no support.

| Field | What it holds | What the research found |
|---|---|---|
| **Statement** | One principle in a line or two | All five sets whose per-principle fields this research tabulated carry one: GitLab Pajamas [[5]](#ref-5), USWDS [[6]](#ref-6), the NHS [[7]](#ref-7), IBM [[8]](#ref-8) and Microsoft [[9]](#ref-9) |
| **What it rules out** | The choice a team can no longer make once it adopts this principle | Productboard's AI prompt has a field headed "What it rules out:" [[11]](#ref-11). Spool's test asks "Does it Help You Say 'No' Most of the Time?" [[4]](#ref-4). No published set read carries the field |
| **The question a reviewer asks** | A question someone can put to a proposed design | GitLab's pages say "When designing any feature, ask:" [[5]](#ref-5). IBM gives four to six yes-or-no questions per principle [[8]](#ref-8). USWDS gives "Key considerations" [[6]](#ref-6) |
| **What it rests on** | The research, a prior decision or a stated value that the principle came from | Spool's first test asks "Does It Come Directly From Research?" [[4]](#ref-4). The NHS states a provenance for its set [[7]](#ref-7), and USWDS lists "Further reading" [[6]](#ref-6). No published set read carries a field for it |
| **A decision it settled** | One real case where the principle decided the outcome | GitLab pairs each principle with an "Example in practice" [[5]](#ref-5). Spotify reports "The more examples, the better" [[17]](#ref-17). GOV.UK links illustrative case studies [[13]](#ref-13) |

**What is received practice and what is the library's addition.** Published sets carry the statement and, in
three of the five tabulated, the reviewer's question. What it rules out appears only in a vendor's AI prompt
(Productboard) [[11]](#ref-11). What it rests on appears in no set read. A decision it settled has partial
precedent in GitLab Pajamas' "Example in practice" and GOV.UK's linked case studies [[5]](#ref-5),
[[13]](#ref-13). Per-principle fields in the published sets vary: GitLab uses a title, a one-line statement, a reviewer question, practice bullets
and an example [[5]](#ref-5). The NHS uses a short imperative title and one to four sentences
[[7]](#ref-7). IBM uses a two-word title, a paragraph and the questions [[8]](#ref-8). Microsoft uses a
one-word name and a sentence or two in the user's own voice [[9]](#ref-9). Gabriel Svennerberg's anatomy is
the baseline a naive template would reproduce, a title, a description and examples, and it does not mention
priority, scope, evidence or a change process [[12]](#ref-12).

**Where principles end.** Microsoft's page moves from its five principles to what it calls signature
experiences, which are visual-language topics and not principles [[9]](#ref-9). That is a useful marker of
the boundary NN/g draws between a principle and a UI direction [[1]](#ref-1).

**The reversal and opposite tests.** Spool asks "Is it Something You Might Reverse in a Future Release?"
[[4]](#ref-4), and Jeremy Keith names the same idea the "reversability test" [[26]](#ref-26). Mistry asks for
the opposite: "If you can't imagine another successful product using the opposite approach, you don't have
a principle - you have a platitude." [[20]](#ref-20) These are why the "what it rules out" field is there. A
principle whose opposite nobody would choose rules nothing out. Brad Frost dissents in part, and section 6
sets out his view [[21]](#ref-21).

**Beginner note.** Draft the statement last. Start from a decision the team has argued about and ask which
option the principle would have chosen, then write down what it ruled out and the question a reviewer would
have asked. Then write the decision as the example.

**Expert note.** The number of principles is a heuristic, not a finding. NN/g's "10 or more" warning
[[1]](#ref-1), Brignell's "3-5" [[18]](#ref-18), Kholmatova's "not more than 3-5" [[3]](#ref-3) and Mistry's
"Limit to 3-4 maximum." [[20]](#ref-20) all state a number, and none of them cites a measurement. Published
set sizes run from three to eleven. IBM (four) [[8]](#ref-8), USWDS (five) [[6]](#ref-6) and Microsoft
(five) [[9]](#ref-9) fall inside the 3-5 advice. GitLab and the NHS (ten each) [[5]](#ref-5),
[[7]](#ref-7) and GOV.UK (eleven) [[13]](#ref-13) exceed it. The Atlassian mirror [[25]](#ref-25) and
Spotify's 2020 set [[17]](#ref-17) have three each. Published practice is therefore mixed, and it does not
settle the heuristics. The template asks for three to five and treats the number as advice. Distrust a principle
you cannot attach a decision to.

### When Principles Conflict

**What it is.** A statement of which principle wins when two pull apart, and in which kind of decision.

**Why it exists.** NN/g's method has a step titled "Identify Any Common Tradeoffs" [[1]](#ref-1), and its
method also tells the author to "Take a stand on which value is important" [[1]](#ref-1). Brignell says "Real
principles reveal priorities." and "Sometimes consistency conflicts with clarity." [[18]](#ref-18) A set that
never says which one wins leaves the argument to whoever is in the room. Brignell writes "If everything is
equally important, nothing actually guides the decision." [[18]](#ref-18)

**This section takes a side in a live dispute, and that side is the library's position.** NN/g also says a
principle should "Not conflict with one another" [[1]](#ref-1), and Blackie lists "Non-conflicting:" among
his criteria [[22]](#ref-22). The two camps may mean different things by "conflict". NN/g may mean that two
principles should not contradict each other, while Brignell means that a useful principle exposes a tension.
This companion reads the disagreement that way, at medium-low confidence, because no source says it. The
template resolves it by asking the author to name, for the kinds of decision where two principles pull
apart, which one wins.

**Forms a resolution takes.** Salesforce "stack-ranked" its four principles, after it "took each principle to
the extreme", and the article records the rationale for each position [[24]](#ref-24). Keith recommends the
form "X, even over Y." [[26]](#ref-26). Atlassian's set, as the principles.design mirror records it, writes
each principle as one thing before another: "Trusted fundamentals before comprehensive patterns" and "Meeting
system needs before delivering features" [[25]](#ref-25). Keith also gives a ranked-conflict example from HTML
design principles: "In case of conflict, consider users over authors over implementors over specifiers over
theoretical purity." [[26]](#ref-26) None of GOV.UK, the NHS and USWDS states a priority order
[[13]](#ref-13), [[7]](#ref-7), [[6]](#ref-6). That is an inference from what those pages say, and the NHS
list is numbered, which this research did not test for an implied order.

**Beginner note.** Pick the two principles most likely to collide, name one kind of decision where they do,
and say which wins there and why. Do not rank every pair. A single resolved conflict is more useful than a
complete table nobody applies. The template offers the X-over-Y form as one good shape, not as a requirement.

**Expert note.** A full ranking is the strongest form and also the most brittle. Salesforce's method of
pushing each principle to the extreme shows how a ranking was found, not that it holds in every case
[[24]](#ref-24). A resolution scoped to a kind of decision survives longer than a global order, and it is the
shape the template asks for. That reading is the library's, not a source's.

### Using Them in Decisions

**What it is.** Where the set is applied, such as critique, design review and pattern proposals, and how a
decision cites a principle.

**Why it exists.** The sources say what a set is for before they say how to apply it. The NHS says "Use them
to get started on a project and to help with making decisions." [[7]](#ref-7) NN/g advises teams to "use the
principles to explain and justify design decisions" [[1]](#ref-1). NN/g's design guidance article says
"Design principles align teams and provide consistency for evaluating design choices." [[23]](#ref-23) Without
a stated place and a stated form of citation, a set risks being read once and not applied. That is the
library's inference. Brignell names principles nobody refers to as a failure mode [[18]](#ref-18), but no
source read ties it to this cause.

**What practice looks like in the sources read.** GitLab's handbook says its principles "guide all product
design work" [[15]](#ref-15), and its critique sessions tell designers to "Connect feedback to user needs and
business goals instead of personal preference" and to "Review the complete design principles in Pajamas"
[[16]](#ref-16). Salesforce used its ranked principles in design review, and the practice spread to marketing
and product management [[24]](#ref-24). Spotify planned a rollout, ran a survey afterwards and reported that
more examples were needed [[17]](#ref-17). Productboard's AI prompt, a vendor's prompt and not a published
set, names moments of use: "In design reviews", when two designers disagree, when judging outside patterns,
and when making trade-offs, with the line "Our principles say [X] over [Y] in this case." [[11]](#ref-11)
The template's list of places draws on these sources. The written line a decision record carries, and what a
reviewer may do when a principle is set aside, are the library's additions.

**A tension the library resolves by reading.** GOV.UK says "This isn't a straitjacket or a rule book."
[[13]](#ref-13), and USWDS calls its set "an evaluative lens for design and implementation decisions"
[[6]](#ref-6). GitLab says "Principles act as a reusable standard for teams to measure their work."
[[5]](#ref-5) The `foundation` classification reads a set as a standard that decisions are judged against.
GOV.UK's phrase reads against a mechanical version of that. The library reads "judged against" as judgement,
not compliance: a decision cites the principle it leaned on and the one it set aside, and a reviewer may
accept the reasoning without accepting the outcome. Brignell states the same reading, "Unlike rules, which
prescribe a specific outcome, principles guide judgement." [[19]](#ref-19)

**Beginner note.** List the two or three moments when a principle is cited, such as a design critique, a design
review and a proposal for a new pattern. Say how the citation is written, for
example a line in the decision record naming the principle.

**Expert note.** A set that is not applied is a poster. The sources agree that a set is meant to be used in
decisions, and the log records no study of whether a team's use of one
changed outcomes.

### Ownership and Changes

**What it is.** The named owner, how anyone proposes a change, who decides, and a dated change log.

**Why it exists.** This is where the set's own staleness is handled. GOV.UK credits a
body, not a named individual: the Government Digital Service and the Central Digital and Data Office
[[13]](#ref-13). Pajamas says "Everyone is welcome to suggest improvements by opening an issue"
[[5]](#ref-5), and the NHS offers "Feed back or share insights on GitHub" [[7]](#ref-7). GitLab's handbook
names designers as "the DRIs for design decisions" [[15]](#ref-15), but its page names no owner, review
interval or revision trigger for the principles themselves. **No source read names a role that decides a
change to a set.** The role names the template asks for are the library's position.

**The dated record is sourced in practice, not in method.** GOV.UK's update history lists "First
published" on "3 April 2012", "Updated illustrative blog posts added." in 2019 and a principle on
environmental impact added on "2 April 2025" [[13]](#ref-13). The NHS page carries "Updated: April 2023"
[[7]](#ref-7). The 2025 addition came from a cross-government working group, and its authors wrote "We
facilitated 2 workshops" [[14]](#ref-14). Afterwards, "we're now looking for someone to create an 11th poster,
and to update the other 10" [[14]](#ref-14). That reply from the authors on the post is the sign that a
change carried a cost beyond the sentence. The post is the one documented amendment of a set by a working
group that this research found.

**The cadence finding.** Three entries in thirteen years is a set kept for years and changed on an event.
No source read states a revision interval. The `foundation` classification therefore holds, and the cadence
tension recorded for the platform and device support matrix in
[ADR 0088](../../docs/internal/decisions/0088-platform-device-support-matrix-joins-standing-standards-as-a-foundation.md)
does not arise here. That conclusion rests on a few dated pages, so it is at low to medium confidence.

**Beginner note.** Name one person who owns the set and one place where anyone can propose a change. State who
decides. Start the change log with the date the set was first agreed.

**Expert note.** Sets are replaced as well as amended. Spotify replaced a set of six with a set of three
after an audit [[17]](#ref-17). Keith, writing about priorities rather than whole sets, says "Prioritisation
isn't and shouldn't be a one-off exercise." [[26]](#ref-26) A change log that shows only additions hides this. Record a retirement as a change, and keep
the reason. Spool's phrase for the retired ones is storage, not deletion [[4]](#ref-4).

### Review Trigger

**What it is.** A table of three columns: the Condition that makes the set wrong or incomplete, the Owner who
notices, and What They Do About It. It is the family's own obligation, not a published convention.

**Why it exists.** The `standing-standards` contract requires every member to ship a trigger with a named
owner and a condition, not a calendar reminder, because members fail by going quietly out of date. **No
design principles source names a trigger.** Where a condition has a source, it is named below. The rest are
the library's own synthesis.

| Condition | Where it comes from |
|---|---|
| A new cross-cutting concern with people behind it | GOV.UK added a principle in 2025 after a cross-government working group formed around the topic [[14]](#ref-14) |
| An audit finds principles overlapping or forgotten | Spotify's audit named "Overlapping concepts" as a defect [[17]](#ref-17). NN/g warns that "having 10 or more leads to many being forgotten" [[1]](#ref-1) |
| A new product or surface joins the scope | Spool's test asks "Have You Evaluated it for This Project?" [[4]](#ref-4) |
| A debate recurs and no principle settles it | The library's own position. Mistry's stated goal is to end repeated debates, not all debate [[20]](#ref-20) |
| The audience or the strategy changes | The library's own inference. No source read states it |

**No calendar interval is sourced, so none is required.** The template does not add one. A team may add an
interval as a floor if it wants one, and it should label the interval as its own choice.

**Beginner note.** Write each condition as an event someone can observe, not as a date. Give each row an owner
by role and say what that person does: reopen the set, run a short audit, or write the change into the log.

**Expert note.** The strongest rows are the ones that have already fired once. The example for this bundle
shows a row that did.

## 4. Variants and sizing

**The bundle ships one size, `lean`.** The maintainer ruled on 2026-11-20 that the bundle has a single size.
The reasons are in the research. NN/g's warning about ten or more [[1]](#ref-1) and Brignell's "3-5"
[[18]](#ref-18) both point to a short document, and a set that short does not earn a second weight. No source
read publishes a fuller and a shorter version of one set. The only condensed forms found are a PDF that
GitLab links "for easy reference" [[5]](#ref-5) and an NHS poster [[7]](#ref-7), and this research opened
neither, so it says nothing about what they leave out. Confidence in a single size is medium-high.

**What to do when a team wants more.** The research found no source for a fuller shape, so there is no second
variant. The sources that add detail add it per principle, not per document: GitLab's practice bullets and
example [[5]](#ref-5), USWDS's "Practical actions" and "Further reading" [[6]](#ref-6), and Spotify's lesson
that more examples were needed [[17]](#ref-17). That is the library's reading of where depth belongs. The library's inference is that a
set that needs long guidance for each principle risks drifting into design-system territory (see section 8).
The counterexample is that USWDS and GitLab carry long per-principle guidance and still publish it as
principles [[6]](#ref-6), [[5]](#ref-5).

**There is no second axis here.** This bundle has one size and one format.

## 5. Methodology lineage

**This research did not look for a tie between design principles and a delivery methodology, and it found
none.** The bundle's `methodology` is `generic`, and the log records no treatment of the type by any
named delivery methodology, or by a regulated-industry school. This companion therefore claims no lineage by school. A table that sorted the type into methods would
be invented.

What the sources do show is a set of working methods for writing a set, each from one author or team.

- **NN/g's four-step method.** "Step 1: Identify Core Values", "Step 2: Consider How These Values Impact
  Users", "Step 3: Identify Any Common Tradeoffs" and "Step 4: Write, Compare, and Iterate" [[1]](#ref-1).
  The article adds that "Having many people write a version of a design principle for each value can help to
  generate many good ideas." [[1]](#ref-1)
- **Kholmatova's chain.** Her talk, "From Purpose to Patterns", draws on her research into what makes
  effective principles. It gives four criteria (genuine, opinionated, actionable and memorable), a chain from
  purpose through principles to patterns, and tests for each criterion [[3]](#ref-3). Her slide "purpose
  informs principles" places the principles downstream of a purpose [[3]](#ref-3).
- **Spool's six tests.** Each test names an element a principle should carry: research, a power to say no, a
  contrast with competitors, a reversal scenario, an evaluation per project, and a meaning tested over time
  [[4]](#ref-4).
- **Spotify's three questions.** Its 2020 rewrite was built on why, who for and how used [[17]](#ref-17).
- **Productboard's quality test.** A vendor's AI prompt tests for specificity, tension and falsifiability, and
  warns against principles that are only "brand adjectives" [[11]](#ref-11). It is a prompt, not a
  methodology, and its text is copyrighted, so the template describes its fields and copies none of its wording.

**Who publishes sets.** The sets read are from public-sector services (GOV.UK [[13]](#ref-13), USWDS
[[6]](#ref-6), the NHS [[7]](#ref-7)), from vendors (IBM [[8]](#ref-8), Microsoft [[9]](#ref-9)) and from
product organisations that write about their own practice (GitLab [[5]](#ref-5), Spotify [[17]](#ref-17) and
Salesforce [[24]](#ref-24)). The research does not show that the three groups use the type differently.

## 6. Debates and contested boundaries

The method articles and critics read (NN/g, Brignell, Kholmatova, Mistry and Blackie) push toward
principles that are specific and few. Several published sets are longer, and Brad Frost dissents in part
on generic principles [[21]](#ref-21). The sources disagree about conflict, ranking, generic principles, the
right count and the number of types. One source the library leans on has a
commercial interest: Brignell
curates principles.design and sells an audit, a course and a field guide on the same site
[[2]](#ref-2), [[18]](#ref-18), [[10]](#ref-10). His claims are the curator's.

**May principles conflict?** NN/g says a principle should "Not conflict with one another" and that "Each
principle should be dedicated to one value only." [[1]](#ref-1) Brignell says "Real principles reveal
priorities." and "Sometimes consistency conflicts with clarity." [[18]](#ref-18) Blackie lists "Non-conflicting:"
among his criteria [[22]](#ref-22). **The dispute is narrower than the first quotes suggest.** In the same
passage, NN/g says that where two principles both matter in different contexts, a team should "clearly
specify in which contexts one of these principles is more important than the other" [[1]](#ref-1). So NN/g
asks a team to avoid principles that contradict each other, and to say which wins where both apply. Brignell
says a useful principle exposes a tension. **Recommendation: name which principle wins in a named kind of
decision**, which is the practice both views end in, and which NN/g's sentence states. The table the template
uses to record it is the library's form.

**Slogan or decision tool?** Brignell writes "A slogan describes intent. A principle guides a choice."
[[18]](#ref-18) and "Design principles aren't mission statements." [[18]](#ref-18) Mistry writes "Most design
principles read like motivational posters." [[20]](#ref-20) Brignell also writes "Values shape culture.
Principles shape decisions." [[18]](#ref-18) No source read defends the poster, though the sample is mostly practitioners writing critiques.
**Recommendation: treat the slogan as a failure.** A reviewer should be able to point at a decision a principle would change.

**Generic or specific?** Mistry writes "design principles are mostly platitudes" [[20]](#ref-20). Blackie writes
"Stating the obvious takes up space" and criticises the GOV.UK set as generic [[22]](#ref-22). Brad Frost
dissents in part: "including a few key principles that aren't entirely unique isn't the worst thing in the
world" [[21]](#ref-21). Frost's post is a short link commentary on another essay, and his point is that
organisations scaling design awareness may benefit from a few generic-sounding principles [[21]](#ref-21).
**Recommendation: ask the opposite test of every principle.** A principle that passes may still sound
familiar. A principle that fails is a platitude, in Mistry's sense.

**How many?** NN/g's "10 or more" warning [[1]](#ref-1), Brignell's "3-5" [[18]](#ref-18), Kholmatova's "not
more than 3-5" [[3]](#ref-3) and Mistry's "3-4" [[20]](#ref-20) agree in direction and differ in number. **None
of them cites a measurement.** Treat every number as a practitioner's heuristic. The template asks for three
to five, and the guide should say that this is advice.

**Ranked or unranked?** Salesforce, Keith and Atlassian rank or write the trade-off into each statement
[[24]](#ref-24), [[26]](#ref-26), [[25]](#ref-25). None of GOV.UK, the NHS and USWDS states a priority
order [[13]](#ref-13), [[7]](#ref-7), [[6]](#ref-6), though the NHS list is numbered, and this research
did not test whether the numbering implies one. **Recommendation: ranking is welcome and not
required.** The template asks for a resolved conflict, which sits between the two camps.

**A standard or a lens?** GOV.UK says its set is not a rule book [[13]](#ref-13), and USWDS calls its set "an
evaluative lens" [[6]](#ref-6). GitLab says its principles are "a reusable standard" [[5]](#ref-5). The family
classifies the document as a standard judged against. The two views meet in the reading in section 3: a
decision is judged against a principle by reasoning, not by checkbox.

**Two kinds of principles?** Pajamas says "There are two kinds of principles", but its two are "The principles
that guide the process" and "The principles that define the output" [[5]](#ref-5). That is a split between
process and output, not between design and product. External support for the library's two-type split is
thin, and section 8 returns to it.

**Not disputed in any source read.** Whether the design team or the product team should own the set is not a
dispute any source takes up. This companion does not present it as one.

## 7. Anti-patterns and failure modes

**Beginner failures**

- **A slogan.** A statement with no decision it would change. Brignell: "A slogan describes intent. A
  principle guides a choice." [[18]](#ref-18) The test is whether a designer could disagree with it.
- **A platitude.** A principle whose opposite no one would choose. Mistry's test is the opposite approach
  [[20]](#ref-20). Productboard's prompt warns against "brand adjectives" [[11]](#ref-11).
- **Too many.** NN/g warns that ten or more are forgotten [[1]](#ref-1), and the numbers elsewhere are
  smaller [[18]](#ref-18), [[3]](#ref-3), [[20]](#ref-20). Treat the figure as a heuristic.
- **A UI direction dressed as a principle.** NN/g separates principles from "directions on how to design
  specific UI elements" [[1]](#ref-1). A statement that names a component belongs in the design system.
- **A principle copied from a published set.** The NHS and GOV.UK pages state a reuse licence, the Open
  Government Licence v3.0, except where otherwise stated [[7]](#ref-7)[[13]](#ref-13). Productboard reserves its rights [[11]](#ref-11). The other pages read state no licence
  in the text read, which is not proof that none exists. Write the team's own words.
- **Values mistaken for principles.** Brignell: "Values shape culture. Principles shape decisions."
  [[18]](#ref-18).

**Subtle failures**

- **No stated order when two principles collide.** Brignell: "If everything is equally important, nothing
  actually guides the decision." [[18]](#ref-18)
- **Overlapping principles.** Spotify's audit named "Overlapping concepts" in its own predecessor set
  [[17]](#ref-17). NN/g's rule is one value per principle [[1]](#ref-1).
- **No examples.** Spotify's lesson was "The more examples, the better" [[17]](#ref-17). Svennerberg's anatomy
  lists examples as a field [[12]](#ref-12).
- **A set nobody cites.** The sources agree that principles are meant to be used in decisions, and Brignell
  names principles nobody refers to as a failure mode [[18]](#ref-18). The library's inference is that a set
  with no place where it is cited risks being read once and not applied. No source read ties the failure to
  that cause.
- **A set that never changes, or changes with no record.** Spotify replaced its set after an audit
  [[17]](#ref-17), and GOV.UK keeps a dated update history [[13]](#ref-13). A set with no owner and no
  reopening condition has no way to do either.
- **A set that restates the current strategy.** This is the library's own caution, not a sourced one. A
  principle that restates one period's strategy choice will go stale when that strategy does, and a standing
  document should outlive it.
- **Borrowing the set from a different product.** NN/g says principles are "specific to the product or service"
  [[1]](#ref-1), and Brignell says they are "unique to an organisation, team or project" [[19]](#ref-19).

**Naming trap.** NN/g's own longer name for the type begins with the word "product" and collides with this
library's sibling bundle, `product-principles`. This bundle does not use that longer name. Its safe aliases
are "UX design principles" and "experience principles".

## 8. Relationships to other artifacts

**NN/g places design principles in a hierarchy of four kinds of guidance.** "Think of them as a hierarchy that
connects your team's foundational agreements to your tactical implementations." [[23]](#ref-23) Team charters
govern how a team works. Usability heuristics are universal, while design principles are "specific to an
organization" [[23]](#ref-23). Patterns are different again: NN/g says "design patterns offer concrete
solutions and are much more tactical in nature" [[23]](#ref-23). NN/g lists "Regularly updated" as a trait of an effective team charter and not of a set of
principles [[23]](#ref-23).

**What feeds a set.** NN/g says "These important values may have been captured in vision statements or project
briefs." [[1]](#ref-1) Kholmatova's slide "purpose informs principles" also places principles downstream of
a purpose, which is a related but different artifact [[3]](#ref-3). In this library the upstream artifact is
the [product vision](../product-vision/product-vision_guide.md), on NN/g's note and the library's own
reading: the vision says where the product is going, and
a principle says how every design decision on the way should lean.

**What the set feeds.** USWDS separates its principles from its design language [[6]](#ref-6), and NN/g
separates principles from "design patterns or standards" [[1]](#ref-1). In this library a
[design brief](../design-brief/design-brief_guide.md) hands one chosen concept to the people who design it.
A brief may cite the principles. The principles outlive every brief.

**The nearest sibling in shape is the definition of done.** The
[definition of done](../definition-of-done/definition-of-done_guide.md) is also a standing standard that work is
judged against. It judges whether an increment is finished, and design principles judge which design choice to
make. A done criterion may say that work was reviewed against the principles, and the principles own the
content of that review.

**The line with product principles is drawn by this library, not by the sources.** The `product-principles`
bundle is this bundle's sibling, and [ADR 0090 (product principles joins
standing-standards)](../../docs/internal/decisions/0090-product-principles-joins-standing-standards-as-a-foundation.md)
admits it as a type of its own. [ADR 0089](../../docs/internal/decisions/0089-design-principles-joins-standing-standards-as-a-foundation.md)
says design principles frame experience decisions and product principles resolve product trade-offs. No
source read draws that line in so many words, and the published sets cross it. One of NN/g's own example
principles, "Prioritize user needs over business constraints.", has the purpose to "Help make tie-breaking
design decisions." [[23]](#ref-23) USWDS's principle on earning trust asks about data privacy and
continuous-integration testing, which is product and engineering territory [[6]](#ref-6). Pajamas' two kinds
are a different split, as section 6 says [[5]](#ref-5).

**A working test, at medium-low confidence and the library's own inference.** Ask what the principle settles.
If it settles how an interaction, a message or a screen should behave for its user, it is a design principle.
If it settles what the team builds, funds or declines, it is a product principle. Some principles will
straddle, and the guide should say so.

**The strategy neighbour.** The Product Principles section of the
[`product-strategy` one-pager full variant](../product-strategy/product-strategy_template-one-pager-full.md)
asks for rules that resolve recurring product trade-offs. That is product principles' territory, summarised
inside a strategy.

**What stays out of this bundle.** Component rules, design tokens and pattern guidance belong to a design
system. Brand voice belongs to a brand or content guide. General usability heuristics are not a team's own
set. NN/g separates product-specific principles from "principles of good design, such as usability
guidelines, heuristics, or visual-design principles" [[1]](#ref-1).

## 9. Adaptations

The log records no research on adaptations, so this section reports what the sources show and marks the
rest as untested.

- **Scale and scope.** Sets are published at several levels: a government-wide set that USWDS says is meant
  "to help teams across government align on common goals" [[6]](#ref-6), a product organisation's set
  [[5]](#ref-5), and a set Spotify wrote for itself [[17]](#ref-17). Brignell says a set may belong to "an
  organisation, team or project" [[19]](#ref-19). The template's scope section is where that choice is made.
- **Reusing a published set.** Only the NHS and GOV.UK pages state a reuse licence [[7]](#ref-7)[[13]](#ref-13), and Productboard
  reserves its rights [[11]](#ref-11). A team that wants to adapt a published set should check its licence and
  should still write its own opposite test, because a set written for another product may not pass it
  [[20]](#ref-20).
- **Writing the set with others.** NN/g suggests having many people write a version of a principle for each
  value [[1]](#ref-1). GOV.UK's 2025 change was drafted with a cross-government working group and two
  workshops [[14]](#ref-14).
- **Methodology-specific tailoring.** None was found, as section 5 says.
- **Solo practitioners and regulated products.** No source read addresses either, and the log records no
  research on them. The template should be read as untested for both, and a solo author can still use the
  rules-out and decision fields, which need no group.

## 10. Worked example

[`design-principles_example.md`](design-principles_example.md) is the design principles document for Acme
Analytics' own product, in the `lean` size. It is paired with a later `product-principles` example for the
same product, so a reader can see an experience principle and a product trade-off side by side and watch the
line in section 8 being drawn. It is worth checking four things in it. First, that each principle carries
every field in section 3, including something it rules out and a decision it settled. Second, that at least one
principle serves the Recurring Analyst, the person the Acme strategy example names by behaviour. Third, that
its conflict section resolves a real tension between two of its principles, in a named kind of decision.
Fourth, that its change log shows a first version and one revision, and that the revision fired from a row in
its Review Trigger table, so the trigger is shown working. The example's principles rest on the persona rather
than on a strategy choice, and the set is reread when the target segment changes, as its Review Trigger
row shows. Every figure in it is labelled illustrative.

---

## References

Access dates are the research date, 2026-11-20, because the research log records no per-source fetch date.

<a id="ref-1"></a>[1] Maria Rosala (Nielsen Norman Group). "[Crafting Product-Specific Design Principles to Support Better Decision Making](https://www.nngroup.com/articles/design-principles/)." nngroup.com, 2 August 2020 (accessed 2026-11-20). Supports NN/g's definition of design principles as value statements used to frame design decisions, the separation from general principles of good design and from UI directions, the four-step method, the qualities a principle needs, the warning that ten or more are forgotten, and the advice to use the principles to explain and justify decisions. A definition source, not an origin source. [practitioner]

<a id="ref-2"></a>[2] Ben Brignell. "[Design Principles | A Free Library of Real-World Design Principles](https://principles.design/)." principles.design home page (accessed 2026-11-20). Supports a second definition that matches NN/g's, and the listing of the NHS, Monzo and Fisher-Price sets. It dates nothing on its home page, and its curator sells an audit, a field guide and consulting on the same site. [practitioner]

<a id="ref-3"></a>[3] Alla Kholmatova. "[From Purpose to Patterns](https://speakerdeck.com/craftui/from-purpose-to-patterns)." Speaker Deck, 16 June 2018 (accessed 2026-11-20). Supports four quality criteria, a purpose-to-principles-to-patterns chain, a count guide of not more than three to five, and a list of earlier writing without dates. Slide text only; the book chapter was not read. [practitioner]

<a id="ref-4"></a>[4] Jared M. Spool (Center Centre). "[Creating Great Design Principles: 6 Counter-intuitive Tests](https://articles.centercentre.com/?p=245)." 1 March 2011 (accessed 2026-11-20). Supports six tests (research origin, a power to say no, competitor contrast, a reversal scenario, a per-project evaluation and a continuously tested meaning), the date of the earliest method piece read, and the expectation that principles retire. [practitioner]

<a id="ref-5"></a>[5] GitLab. "[Pajamas Design System - Principles](https://design.gitlab.com/about/principles/)." design.gitlab.com (accessed 2026-11-20). Supports a set of ten principles, each with a title, a one-line statement, a reviewer question, practice bullets and an "Example in practice", the process-against-output split, the invitation to propose changes by issue, and a linked condensed PDF that was not opened. [practitioner]

<a id="ref-6"></a>[6] U.S. Web Design System (GSA). "[Design principles](https://designsystem.digital.gov/design-principles/)." designsystem.digital.gov (accessed 2026-11-20). Supports five principles with statement, "Key considerations", "Practical actions" and "Further reading", the framing as an evaluative lens, the separation from the design language, and a principle on earning trust that reaches into product and engineering. [primary]

<a id="ref-7"></a>[7] NHS England. "[Design principles](https://service-manual.nhs.uk/design-system/design-principles)." NHS digital service manual (accessed 2026-11-20). Supports ten principles, each a short imperative title and one to four sentences, a stated use, a stated provenance, a GitHub feedback channel, an "Updated: April 2023" date and the Open Government Licence v3.0. The poster PDF was not opened. [primary]

<a id="ref-8"></a>[8] IBM. "[IBM Design Language - Principles](https://www.ibm.com/design/language/philosophy/principles/)." ibm.com (accessed 2026-11-20). Supports four principles, each a two-word title, a paragraph and four to six yes-or-no reviewer questions. The page carries a copyright footer and no reuse licence in the text read. [vendor]

<a id="ref-9"></a>[9] Microsoft. "[Windows 11 design principles](https://learn.microsoft.com/en-us/windows/apps/design/design-principles)." Microsoft Learn (accessed 2026-11-20). Supports five principles, each a short name and a sentence or two in the user's voice, with a move to visual-language topics afterwards. No reuse licence is stated in the text read. [vendor]

<a id="ref-10"></a>[10] Ben Brignell. "[Design Principles in Practice: A field guide](https://principles.design/field-guide/)." principles.design (accessed 2026-11-20). Supports only that a paid field guide exists, with a chapter titled "The anatomy of a strong principle" and three worksheets. It is a sales page, and the guide's contents were not read, so nothing in this companion rests on them. [vendor]

<a id="ref-11"></a>[11] Productboard. "[Design Principle Generator](https://www.productboard.com/product-management-prompts-library/design-principle-generator/)." Product Management Prompts Library (accessed 2026-11-20). Supports a vendor's AI prompt with five fields per principle, four to six principles, a quality test of specificity, tension and falsifiability, and a "What it rules out:" field. It is a prompt, not a published set or a template, and its text is not copied here. [vendor]

<a id="ref-12"></a>[12] Gabriel Svennerberg. "[The Anatomy of a Design Principle](https://www.designprinciplesftw.com/articles/the-anatomy-of-a-design-principle)." Design Principles FTW (accessed 2026-11-20). Supports the baseline a naive template would reproduce: a title, a description and examples. It does not mention priority, scope, evidence or a change process. [practitioner]

<a id="ref-13"></a>[13] Government Digital Service and Central Digital and Data Office. "[Government Design Principles](https://www.gov.uk/guidance/government-design-principles)." GOV.UK guidance (accessed 2026-11-20). Supports an eleven-principle set, an update history of three entries (3 April 2012, 2019 and 2 April 2025), no stated revision interval, linked case studies, and the statement that the set is not a rule book. [primary]

<a id="ref-14"></a>[14] Government Digital Service. "[Adding sustainability to the Government Design Principles](https://services.blog.gov.uk/2025/04/02/adding-sustainability-to-the-government-design-principles)." Services in government blog, 2 April 2025 (accessed 2026-11-20). Supports the one documented amendment of a set by a working group found: a working group, two workshops, and a reply from the authors seeking someone to draw an 11th poster and update the other 10, triggered by a new cross-cutting topic and not by a calendar. [primary]

<a id="ref-15"></a>[15] GitLab. "[Product Design](https://handbook.gitlab.com/handbook/product/ux/product-design/)." GitLab Handbook (accessed 2026-11-20). Supports the statement that the principles live in the Pajamas Design System and guide all product design work, and that designers are the directly responsible individuals for design decisions. The page names no owner or revision trigger for the principles. [practitioner]

<a id="ref-16"></a>[16] GitLab. "[Product Designer workflow](https://handbook.gitlab.com/handbook/product/ux/product-designer/)." GitLab Handbook (accessed 2026-11-20). Supports a design critique that connects feedback to user needs and business goals, and that points designers to the principles in Pajamas. [practitioner]

<a id="ref-17"></a>[17] Spotify Design. "[Introducing Spotify's New Design Principles](https://medium.com/spotify-design/introducing-spotifys-new-design-principles-c99c58ed7558)." Medium, 8 July 2020 (accessed 2026-11-20). Supports a replacement of a 2013 set of six after an audit that named three defects, three guiding questions, a rollout plan, a survey, and the lesson that more examples were needed. [practitioner]

<a id="ref-18"></a>[18] Ben Brignell. "[Why Most Design Principles Fail](https://principles.design/articles/why-most-design-principles-fail/)." principles.design, 6 March 2026 (accessed 2026-11-20). Supports failure modes (slogans, no trade-offs, too many, nobody refers to them, values mistaken for principles), the claims that real principles reveal priorities and that consistency can conflict with clarity, and a range of three to five. The author sells a course and an audit on the same site. [practitioner]

<a id="ref-19"></a>[19] Ben Brignell. "[Design Principles vs. The Principles of Design](https://principles.design/articles/design-principles-vs-principles-of-design/)." principles.design, 12 February 2026, updated 15 February 2026 (accessed 2026-11-20). Supports the line between direction and judgement on one side and craft and execution on the other, and the point that design principles are unique to an organisation, team or project. [practitioner]

<a id="ref-20"></a>[20] Jay Mistry. "[Your Design Principles Are Useless (Here's What Actually Works)](https://jaymistry.substack.com/p/design-principles-tenets)." Substack, 14 June 2025 (accessed 2026-11-20). Supports a named critic's view that generic principles are platitudes, the opposite test, a limit of three to four, and the goal of ending repeated debates. [practitioner]

<a id="ref-21"></a>[21] Brad Frost. "[In the future, design principles won't be about design](https://bradfrost.com/blog/link/in-the-future-design-principles-wont-be-about-design/)." bradfrost.com, link post, 6 June 2017 (accessed 2026-11-20). Supports a named counterweight on generic against specific principles. It comments on another essay and quotes Spool and Keith. [practitioner]

<a id="ref-22"></a>[22] Stuart Blackie (Mantel). "[Principles with purpose: making design rules that matter](https://mantelgroup.com.au/principles-with-purpose-making-design-rules-that-matter/)." mantelgroup.com.au (accessed 2026-11-20). Supports a criteria list that includes non-conflicting, a typology of heuristics, team principles and business or program principles, and a critique of the GOV.UK set as generic. [practitioner]

<a id="ref-23"></a>[23] Rachel Krause (Nielsen Norman Group). "[Design Guidance: Principles, Patterns, Heuristics, and Team Charters](https://www.nngroup.com/articles/design-guidance/)." nngroup.com, 18 April 2025 (accessed 2026-11-20). Supports a hierarchy of four kinds of design guidance, one of NN/g's own example principles as a tie-breaking trade-off, and the trait "Regularly updated" listed for team charters and not for principles. [practitioner]

<a id="ref-24"></a>[24] JD Vogt (Salesforce UX). "[Defining Principles to Drive Design Decisions](https://medium.com/@salesforce/defining-principles-to-drive-design-decisions-811a85032c56)." Medium, 19 May 2016 (accessed 2026-11-20). Supports four explicitly stack-ranked principles, the method of pushing each to the extreme, and their use in design review. [practitioner]

<a id="ref-25"></a>[25] Atlassian, as mirrored by Ben Brignell. "[Atlassian Design System values and principles](https://principles.design/examples/atlassian-design-system)." principles.design (accessed 2026-11-20). Supports three values each paired with a principle written as one thing before another. A mirror; Atlassian's own page was not read because it returned a script redirect and then a sign-in page. [reference]

<a id="ref-26"></a>[26] Jeremy Keith (Clearleft). "[Principles and priorities](https://clearleft.com/thinking/principles-and-priorities)." clearleft.com, 27 April 2020 (accessed 2026-11-20). Supports the "X, even over Y" form for priority, a reversal test, the HTML priority of constituencies as a ranked-conflict example, and prioritisation as a repeated activity. [practitioner]
