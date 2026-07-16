# Companion: The Architecture Decision Record (ADR)

> The deep explainer for the ADR bundle. Read this to understand what an ADR is, where it came
> from, why it is shaped the way it is, and where serious practitioners disagree about it. The
> short operator card is [`adr_guide.md`](adr_guide.md); a fully worked instance is
> [`adr_example.md`](adr_example.md). Inline citations like [[1]](#ref-1) resolve to the
> [References](#references) at the bottom, tagged by source reliability.

---

## 1. Orientation

An Architecture Decision Record is **one file, one decision, written once and never quietly
rewritten.** It records a choice that was hard to make and would be expensive to reverse: the
forces that made it necessary, the options that were genuinely on the table, the one that was
chosen, and the price the team knowingly agreed to pay [[1]](#ref-1).

Its purpose is narrow and worth stating precisely. An ADR does not exist to describe your
architecture; a diagram does that, and does it better. It exists to answer a question a diagram
cannot: **"why is it like this, and did you consider the obvious alternative?"** Michael Nygard,
who introduced the format in 2011, framed the motivation as a trap that new team members walk into:
faced with an old decision and no recorded rationale, they can either accept it blindly or change
it blindly, and both are bad [[1]](#ref-1).

**At a glance**
- The value is in the **rejected options** and the **negative consequences**. A record listing only
  the winner and its benefits is marketing, not memory.
- It is **immutable once accepted.** You supersede it with a new record; you do not edit it. The
  audit trail is the product [[1]](#ref-1)[[3]](#ref-3).
- It lives **in the repository, next to the code it binds**, not in a wiki. ThoughtWorks makes
  exactly this recommendation [[9]](#ref-9), and it recurred more than any other single piece of
  advice across the sources read for this bundle.
- It is **short.** Nygard's original guidance: "The whole document should be one or two pages long.
  We will write each ADR as if it is a conversation with a future developer" [[1]](#ref-1).
- The hard part is not the format. It is **deciding what deserves a record at all**, and that
  question is genuinely contested (see [section 6](#6-debates-and-contested-boundaries)).

If you read nothing else: an ADR is a **letter to the engineer who will want to undo your work.**
Write it so that they can tell, quickly, whether they know something you did not.

---

## 2. Origins and evolution

**The format is younger than the practice.** Documenting design rationale is an old idea in software
architecture, and it arrived in a heavyweight form first. Tyree and Akerman published a decision
template in *IEEE Software* in 2005 running to fourteen fields [[4]](#ref-4). It is rigorous, it is
thorough, and it is not the template the industry ended up adopting. The gap between those two facts
is the whole story of what came next. (That paper is paywalled and was not read for this bundle. The
field count comes from a widely used community reconstruction, and nothing in this section rests on
the specific field names; see [`adr_research-log.md`](adr_research-log.md).)

**Nygard's 2011 contribution was subtraction.** In a short Cognitect blog post he cut the template to
five parts (Title, Context, Decision, Status, Consequences), put the file in the repository, and
numbered the records sequentially and monotonically, never reusing a number [[1]](#ref-1). The
insight was not the fields. It was that a document large enough to be complete is a document nobody
writes and nobody reads, while a short record living beside the code stands a chance of surviving.
Martin Fowler's bliki entry credits Nygard as the origin and carried the practice to a wider audience
[[3]](#ref-3).

**The industry ratified it quickly.** Lightweight ADRs entered the ThoughtWorks Technology Radar in
Trial in November 2016 and have since moved to Adopt, the ring reserved for practices the firm
believes the industry should simply be using. The Radar's specific advice is to keep records in
source control rather than a wiki [[9]](#ref-9).

**MADR is where the format actually lives now.** Markdown Architectural Decision Records, maintained
in the open at the `adr` GitHub organization, began in 2017 and reached v4.0.0 on 2024-09-17
[[2]](#ref-2). Its one substantive addition to Nygard is **Considered Options**, which it makes
*mandatory*: Nygard's five sections give the rejected alternatives no home of their own, and MADR
promotes them to a required list. Everything else it adds is *optional*: Decision Drivers,
Confirmation, Pros and Cons of the Options, More Information, and (perhaps surprisingly) Consequences
itself. It is the format this bundle teaches, and [section 5](#5-methodology-lineage) explains why.

**A detour worth knowing, because it is the scope debate wearing a disguise.** MADR renamed itself
from "Markdown *Architectural* Decision Records" to "Markdown *Any* Decision Records" in v3.0.0
(2022), and then reverted to "Architectural" in the v4 line (2024). Its documentation explains that
the name spells out "Architectural" so as "to strengthen the importance for decisions in software
architecture work" [[2]](#ref-2). A standard that changed its own name twice in two years, over
whether the format belongs to architecture or to everything, is telling you exactly where the live
argument is. Many blog posts still describe MADR as "Any Decision Records." **As of v4, that is out
of date.**

**A parallel lineage compresses rather than expands.** Y-statements were presented by Olaf Zimmermann
at SATURN 2012 and published in *IEEE Software* by Zdun, Capilla, Tran and Zimmermann in 2013
[[5]](#ref-5). They squeeze an entire decision into one sentence, built from six clauses: *"In the
context of [context], facing [concern], we decided for [option] and neglected [alternatives], to
achieve [quality], accepting that [downside]"* [[6]](#ref-6). The "Y" is for "why." It is the smallest
honest ADR anyone has proposed, and it is a useful test: if you cannot fill in the *"accepting that"*
clause, you have not finished thinking.

**One claim to stop repeating.** It is commonly asserted that ISO/IEC/IEEE 42010 mandates ADRs. It
does not. The standard requires that an architecture description capture decision *rationale*,
including alternatives not chosen, and the 2022 edition specifies requirements for doing so. It
prescribes no particular document format, and no secondary source reports it using the term "ADR"
at all [[12]](#ref-12). Note the shape of that last sentence: the standard is paywalled and this
bundle did not read it, so what is claimed is what the secondary literature reports, not what a
reading of the text established. The standard is a reason to record rationale. It is not a reason to
use this template, and citing it as one is an appeal to authority that a careful reader will check,
which is precisely why the hedge belongs here rather than buried in the reference list.

---

## 3. Anatomy (section by section)

### Frontmatter and status

MADR defines five frontmatter fields (`status`, `date`, `decision-makers`, `consulted`, `informed`)
and marks them **collectively optional**, on its full template only; its minimal template carries no
frontmatter at all [[2]](#ref-2). This bundle takes a firmer line than the standard does: lean
requires the first three, and full adds the last two. **That split is this library's design decision,
not MADR's**, and it is a deliberate tightening, for the reason the beginner note below gives.

Nygard's original status values were `proposed`, `accepted`, `deprecated`, and `superseded`
[[1]](#ref-1). MADR keeps all four, adds `rejected`, and writes supersession as
`superseded by ADR-NNNN` so the chain stays followable [[2]](#ref-2).

*Beginner note:* `status` is the field that decays, and a stale one is worse than no record at all. A
record that still says `accepted` for a technology you ripped out last year is not merely useless; it
actively misleads the next person who finds it, because the field asserts the decision still holds
[[15]](#ref-15). This is exactly why the bundle requires `status` where MADR leaves it optional: an
absent status is honest, and a wrong one is a trap, but a field nobody is obliged to fill is the
surest route to the wrong one.

*Expert note:* `decision-makers` is a list, and keeping it honest is a small act of courage. It is
the field that resists the "safety in numbers" failure Pureur and Bittner describe, where a record
exists so that no individual can be blamed [[8]](#ref-8). A record that names nobody was decided by
nobody.

This bundle's templates also carry `doc_type`, `size`, and `source_template` for the library's own
provenance. MADR tooling ignores keys it does not know, so these ride along harmlessly.

### Title

A statement naming both the problem and the chosen option. Not a question, not a topic.

*Beginner note:* the filename is the interface. A decisions directory is read as a list of
filenames far more often than it is read as documents, so a title like "Database decision" makes the
record invisible in the only view most people will ever use.

### Context and Problem Statement

The forces in play: technical, business, organizational, plus the real constraints (team skill,
deadline, budget) [[1]](#ref-1). MADR asks you to make the *scope* explicit by naming the components
the decision binds [[2]](#ref-2).

*Beginner note, and if you read only one paragraph of this companion, read this one:* **write down
the situation you were in, not the argument you won.** Describe the forces, constraints, and
pressures as they actually stood at the time, including the unflattering ones (nobody on the team had
used the alternative; the deadline was three weeks; the budget was already spent). The temptation is
to write this section last, working backwards from the option you chose, so that the context reads as
a case for the decision. Resist it. That version is easy to write, sounds authoritative, and is
worthless.

*Expert note:* the reason it is worthless is that **context is the part that expires.** A decision can
remain correct long after the reason for it has quietly stopped being true, and the only way a future
reader can detect that is if you recorded the conditions you were actually under. Justification-shaped
context strips out exactly the information that would let someone revisit the call responsibly: it
tells them why you were right, when what they need to know is what was true. A record whose context
section is an argument cannot expire, which sounds like a feature and is the defect.

### Decision Drivers *(full variant only)*

The criteria the options are judged against [[2]](#ref-2).

*Beginner note:* these are the things you would use to argue an option is wrong. Write them as
qualities you need (latency under a threshold, auditability, the ability to back out in a week) or
constraints you cannot break (no new infrastructure, no third-party dependency, ships before the
audit). Three to five is plenty. Write them before you compare the options, not after, or you will
find yourself writing the criteria that your favorite option happens to satisfy.

*Expert note:* drivers are the yardstick, and they only work if an option could **fail** one. If every
option satisfies every driver, the drivers are decoration and the real reason for the choice is still
unwritten. Say explicitly which driver is the knockout criterion. Doing so is what stops the
comparison below from being a rationalization of the answer you already preferred, and it is what lets
a future reader re-run your reasoning when one of the drivers stops applying.

### Considered Options

The alternatives, by title [[2]](#ref-2).

*Beginner note:* include "do nothing." It is a real option, it is frequently the right one, and
teams that never write it down never seriously consider it.

*Expert note:* this section is where a record is most often quietly dishonest. Two decoys and a
winner is not a decision record, it is a press release. If an option was never genuinely on the
table, leave it out; a shorter honest list beats a padded one, and a reader can smell the difference.

### Decision Outcome

The chosen option and the justification, in active voice.

*Beginner note:* two or three sentences is usually right. Name the option, then say which decision
driver it won on. The justification is not a summary of the whole debate (that is what Pros and Cons
is for); it is the one reason that actually settled it. If you find yourself writing paragraphs here,
the material probably belongs in Consequences or Pros and Cons instead. Start the sentence with "We
will" or "We chose," and make sure a real person's name appears in `decision-makers`.

*Expert note:* Nygard's phrasing convention ("We will ...") is not a style preference. Passive voice
("it was decided that ...") is the grammar of accountability theater: it produces a sentence in which
a decision exists but nobody made it, which is the linguistic form of the exact failure mode Pureur
and Bittner name [[8]](#ref-8). Watch for it as a symptom: when a team reaches for the passive here,
it is often because the decision was not really made, or not really agreed, and the record is papering
over that.

### Consequences

What gets easier and what gets harder. Nygard is explicit that **all** consequences are listed, not
just the positive ones [[1]](#ref-1).

*Beginner note:* write at least one "Bad, because" line, and make it one somebody would actually act
on. A useful prompt: what will the team complain about in six months *because of this decision*? What
did you give up? What new thing must now be maintained, monitored, or paid for? Consequences are not
risks (things that might happen); they are what is now true.

*Expert note:* the negative consequences are the highest-value lines in the record, because they are
what a future reader tests against reality to decide whether the decision still holds. A "Bad,
because" line so weightless that it is really a "Good" in disguise ("there is a small learning curve")
is a tell that the author was selling rather than deciding. If you cannot name a cost you actually
paid, you probably have not understood the decision yet, and the record you are writing will not
survive its first serious reader.

### Confirmation *(full variant only)*

How compliance with the decision can be checked: a test, a lint rule, a CI gate, an architecture
fitness function, or a named review step [[2]](#ref-2). MADR notes that although the section is
classified optional, it is included in many real ADRs [[2]](#ref-2).

*Beginner note:* answer one question: **if someone violated this decision tomorrow, what would catch
them?** A CI check, a lint rule, a test, a schema validation, a required review by a named person.
Write down whichever it is. If nothing would catch them, write *that* down instead, in plain words.
"Nothing currently enforces this" is a legitimate and genuinely useful answer, and it is far better
than the reflex placeholder "the team will keep this in mind during code review," which means nothing
and commits no one.

*Expert note:* this is the section that separates a decision that **binds** from a decision that
merely **happened**, and it is the one teams skip most. It is also the section whose value has risen
sharply, for a reason [section 6](#6-debates-and-contested-boundaries) takes up: a decision a machine
can check is a constraint, and a decision nothing checks is a comment. Treat a blank Confirmation
section as a measurement, not a gap in the paperwork. It tells you how much this decision is really
worth to the organization, which is often less than the effort spent writing it down.

### Pros and Cons of the Options *(full variant only)*

Each option weighed against the drivers [[2]](#ref-2).

*Beginner note:* one subsection per option, including the one you picked. Use "Good, because ..." and
"Bad, because ..." bullets, and tie each one back to a driver you listed above rather than to a
general impression. Two or three bullets per option is enough. For a rejected option, the most useful
single line is the one that names the driver it failed.

*Expert note:* weigh the **winner** honestly. It has real cons, or it would not have been a decision
worth recording. A chosen option presented with no downsides tells the reader the analysis was
retrospective, and it costs you their trust in everything else in the file. The worked example in this
bundle is a live demonstration: the option it chose forces the project to parse YAML with a regular
expression, which is genuinely brittle, and saying so is what makes the rest of the record credible.

### More Information *(full variant only)*

Related records, supporting evidence, the team agreement, and when the decision should be revisited
[[2]](#ref-2).

*Beginner note:* link the records this one depends on, refines, or supersedes, and say in a clause
*why* each one matters rather than just dropping the link. Then add one sentence starting "Revisit
if ...". That sentence is the most valuable thing in the section.

*Expert note:* the "revisit if" sentence sets the record's **expiry**, and it is what lets a future
team tell the difference between reading history and reading law. A decision made under conditions
that will predictably change (a pricing tier, a team size, a library's maturity, a constraint you
accepted only because of a deadline) should name the event that ought to reopen it. Without that, the
next team faces a record that is silent about its own shelf life, and their only options are to obey
it or to override it, which is precisely the accept-blindly-or-change-blindly bind that Nygard
invented the format to escape [[1]](#ref-1).

---

## 4. Variants and sizing

**Lean is the default, and it is not a compromise.** It carries exactly the three sections MADR marks
mandatory (Context and Problem Statement, Considered Options, Decision Outcome, with Consequences
nested under the outcome) [[2]](#ref-2). Most decisions are recorded honestly in half a page, and a
short record that actually gets written beats a thorough one that does not. That is Nygard's entire
argument [[1]](#ref-1), and it is the lightweight form, not the fourteen-field one, that the industry
actually went on to adopt [[9]](#ref-9).

**Full adds Decision Drivers, Confirmation, Pros and Cons of the Options, and More Information.**

The signal to scale up is not the importance of the *system*. It is the **contestedness of the
decision**. Reach for full when:

- The decision is expensive or slow to reverse (a data model, a persistence engine, a public API).
- Reasonable engineers on the team actively disagreed, and the disagreement deserves a record.
- It crosses teams, so people who were not in the room must be able to reconstruct the reasoning.
- It carries regulatory, safety, or security weight and you expect to defend it to an auditor.
- The comparison itself is the value, and compressing it would destroy the record's usefulness.

Otherwise use lean. Reaching for the full variant by reflex is how a decisions directory fills up
with ceremony that nobody reads, which is the failure mode [section 7](#7-anti-patterns-and-failure-modes)
returns to.

**A note on the size vocabulary.** This library's master catalog originally classified the ADR as a
single-size type. The evidence overturned that: MADR itself ships a minimal template and a full
template as separate files, which is the clearest possible signal from the standard's own
maintainers that the type earns two weights [[2]](#ref-2). Pleasingly, MADR's minimal section list is
already a strict ordered subset of its full one, so the two variants satisfy this library's nesting
rule without any adjustment. That was not arranged; it was discovered, and it is decent evidence that
the nesting rule describes something real about how documents grow.

---

## 5. Methodology lineage

Different schools record decisions differently, and the differences are not cosmetic.

| School | Form | What it optimizes for |
|---|---|---|
| **Nygard (2011)** | 5 sections, in-repo, numbered | Getting written at all. The founding minimal form [[1]](#ref-1). |
| **MADR (v4, 2024)** | 3 mandatory + 5 optional sections, YAML frontmatter | Tooling and comparison. The maintained modern standard [[2]](#ref-2). |
| **Tyree and Akerman (2005)** | 14 fields | Completeness and formal traceability. Predates the lightweight turn [[4]](#ref-4). |
| **Y-statements (2012/2013)** | One sentence, six clauses | Compression. Forces the "accepting that" clause into the open [[5]](#ref-5)[[6]](#ref-6). |
| **RFC tradition** | Long proposal, review period, then acceptance | Deciding, not recording. A different artifact (see below) [[11]](#ref-11). |
| **Google-style design docs** | Long-form narrative, reviewed pre-build | Design exploration; rationale is embedded, not indexed. |
| **ISO/IEC/IEEE 42010:2022** | Requires rationale; prescribes no format | Conformance. Compatible with all of the above [[12]](#ref-12). |

**Why this bundle teaches MADR rather than Nygard.** Nygard's format is the origin and it remains
perfectly serviceable. MADR is chosen here for three reasons:

1. **It is a maintained, versioned specification.** v4.0.0 shipped 2024-09-17, on a changelog going
   back to v1.0.0 in 2017 [[2]](#ref-2). Nygard's is a blog post, excellent and frozen since 2011.
2. **Its section set is a superset**, so any Nygard record can be expressed in MADR without loss. The
   mapping is one-to-one and appears in [`adr_guide.md`](adr_guide.md); a team already on Nygard can
   adopt this template without rewriting anything.
3. **It is what this organization already standardized on** for its own decision records, which for
   anyone working inside a product-on-purpose repository is the decisive reason and not merely a
   supporting one.

**Tooling is not one of the three reasons, and the honest picture is worth stating,** because it is
the argument a MADR advocate reaches for first and it does not survive checking. The best-known ADR
command-line tool, `adr-tools`, is **Nygard-only** and does not support MADR at all. The tools that
do support MADR (Log4brains, adr-manager) target **MADR 2.1.2**, and the ADR project's own tooling
page lists nothing that tracks v4 [[18]](#ref-18). So the tooling ecosystem lags the specification by
two major versions, and choosing v4 means choosing the spec over the tools.

That is a real cost, and for some teams it is decisive: if a shell-script workflow around `adr-tools`
is load-bearing for you, staying on Nygard is a defensible call, and the mapping table will still get
you most of the way here. It is not decisive for this bundle, because the sections MADR marks
mandatory have been stable across 2.x, 3.x, and 4.x, so a record written to this template is readable
by the 2.1.2 tools regardless. But a reader who clicks that citation should find the caveat already
written down rather than discover it themselves.

---

## 6. Debates and contested boundaries

### 6.1 What counts as "architecturally significant"? (the live one)

This is the real argument, and it has named camps.

**Expand.** Olaf Zimmermann argues the format is valuable for any consequential decision, not only
architectural ones; the case is made directly in his "Any Decision Records" essay
[[7]](#ref-7). MADR itself flirted with this position hard enough to rename itself, then backed off
(see [section 2](#2-origins-and-evolution)).

**Restrict.** Pierre Pureur and Kurt Bittner argue in *InfoQ* that scope bloat is a genuine harm:
teams with nowhere else to put non-architectural decisions dump them into ADRs, and the effect is to
make "the architecture harder to perceive" [[8]](#ref-8). Their proposed fix is a separate class of
record for decisions that are significant but not architectural.

**Deflect.** Spotify's public guidance says it is "up to each team to align on what defines"
significance [[10]](#ref-10). This is the most common position and it is a non-answer, and Pureur and
Bittner would say it is precisely how the sprawl gets in.

*This bundle's recommendation:* apply a **reversibility test**, not a significance test. If the
decision is cheap to reverse later, do not spend a record on it. If it is expensive or slow to
reverse, record it, whether or not it is "architectural" in a purist sense. Reversibility is
observable and arguable; significance is a matter of taste, and a criterion nobody can apply
consistently produces exactly the sprawl the restrict camp warns about.

### 6.2 Immutability, and where this library draws the line

The canonical rule, from Nygard and repeated by Fowler, is that an accepted record is never reopened
or changed; it is superseded [[1]](#ref-1)[[3]](#ref-3). Practitioner guides describe teams deviating
toward a "living document" approach instead, updating accepted records in place as reality shifts
[[15]](#ref-15).

Notably, **this bundle's research found no source publicly arguing against immutability as a
principle.** Where the deviation appears, it is described as pragmatic drift, not defended as
better. That asymmetry is worth taking seriously. (Stated as a fact about our search rather than
about the literature, which is all a search can honestly support.)

*This bundle's line, and it is a fine distinction that pays for itself:* **a factual error in a
record is corrected in place, with the correction dated and the error named. A change in the
decision itself gets a new number.** Superseding a record asserts that the *decision changed*. If
what was actually wrong was a false statement inside the record, a supersession misrepresents the
history: it tells a future reader that the team once believed something it never believed. So the
error is corrected and the scar is left visible. A record that silently rewrites itself is worth less
than one that shows its scars. This library applies the rule to itself, in
[ADR 0011 (adopt MADR v4)](../../docs/internal/decisions/0011-madr-v4-at-docs-internal-decisions.md).

### 6.3 ADR vs RFC vs design doc

Candost Dagdeviren draws the cleanest line: an **RFC requests input before a decision is made**; an
**ADR records a decision already taken.** They are sequential, not competing, and the natural pipeline
is RFC first for anything with cross-team impact, ADR to record the outcome [[11]](#ref-11).

The overlap is real and the confusion is genuine: MADR's own issue tracker carries a thread asking
whether ADRs can replace design docs and RFCs, opened in 2023 and still unresolved
[[19]](#ref-19). But much of the apparent disagreement in the literature is practitioners using the
word "RFC" for different artifacts rather than actually disagreeing about anything.

### 6.4 Why do so many ADR collections become write-only?

The phenomenon is universally acknowledged. The **cause** is contested. One camp argues the failure
is *structural*: records stored outside the codebase, in a wiki or Confluence, are guaranteed not to
be read, and the fix is purely a matter of location. The other argues it is *cultural*: records get
written for uncontentious decisions after the fact, as a gesture toward documentation discipline, and
no change of location saves a practice nobody believes in.

*Read:* the structural claim is specific and falsifiable, and it is the one ThoughtWorks endorses in
practice by telling teams to keep records in source control [[9]](#ref-9). The cultural claim is
older and harder to act on. Do the structural thing first, because it is free.

### 6.5 The AI-era question, which is new and is not hype

This is the most interesting current development, and it deserves careful, hedged handling.

**There is one measured result, and it is routinely misreported. Including, on the first draft, by
this document.** A 2026 preprint benchmarks AI coding-agent *decision compliance* across 8 tasks
containing 41 weighted decision points, and reports 95% compliance for an augmented configuration
against 46% for a baseline agent with codebase access only: a **49 percentage-point** gain, not a
49% relative improvement [[13]](#ref-13).

Read the fine print before you repeat that number, because two things about it matter:

- **The intervention was not ADRs.** It was a commercial product-context retrieval system whose
  retrieval set is recorded decisions *plus* persona pain points, customer signals, and competitive
  intelligence. The study does not isolate decision records, so it cannot tell you what ADRs alone
  are worth. It is also, in plain terms, its authors evaluating their own product, which is why this
  bundle tags it `[vendor]` and not `[primary]`.
- **The genuinely interesting finding is the one nobody quotes.** Broken out per decision, the
  baseline agent scored **100% compliance on decisions that were visible in the codebase, and
  0-33% on decisions that required context the code did not contain** [[13]](#ref-13). That is a
  sharp result and it is the honest core of the ADR argument for AI-assisted work: an agent reliably
  infers what the code shows and reliably violates what only a human ever knew. The gap is exactly
  the shape of what a decision record holds.

So: suggestive, directional, worth knowing, and not proof. One preprint, one benchmark, vendor-run,
not replicated. Anyone citing it at you as "ADRs improve AI compliance by 49%" has repeated three
errors in six words.

**The rest of the writing is conceptual.** The sharpest framing is that machine-checkability is what
gives a decision force: an ADR nobody checks is a comment, and an ADR a machine checks is a
constraint [[14]](#ref-14). That argument is not empirical, but it converges with something the
format already had, and it is the reason this bundle treats MADR's optional **Confirmation** section
as a first-class teaching point rather than a footnote.

**The live tension is `AGENTS.md` versus `decisions/`.** An argument is circulating that agent
instruction files are displacing ADRs as the operative artifact for AI-assisted work. (This bundle's
research could not retrieve the piece most often cited for it, so treat the claim as a framing you
will encounter rather than as a position anyone here has verified.) The better read is that the two
are complements answering different questions: a decisions directory tells an agent **why** the
system is the way it is, and an instruction file tells it **what to do right now**. An agent holding
only the instruction file will comply with your conventions and cheerfully re-open settled questions,
because nothing ever told it they were settled.

---

## 7. Anti-patterns and failure modes

1. **Approval theater.** Records written after the fact, for decisions that were never contentious,
   so the folder can look disciplined. Nobody reads them, and their presence makes the genuinely
   contested records harder to find.
2. **The CYA record.** Written to dilute accountability rather than to inform. Pureur and Bittner
   name the mechanism precisely: safety in numbers, protecting the team from blame
   [[8]](#ref-8). The tell is passive voice and an empty or crowded `decision-makers` field.
3. **The decision without the alternatives.** The single most common substantive failure. It leaves
   the record unable to answer the only question it will ever be asked, which is "did you consider
   X?", and it guarantees the next team re-litigates from zero.
4. **The stale status.** A record that still reads `accepted` for a choice long since abandoned. A
   record justifying a technology you ripped out two years ago is not merely useless to whoever finds
   it next; it actively misleads them, because its status field asserts that the decision still holds
   [[15]](#ref-15).
5. **Scope bloat.** Every decision becomes an ADR because there is nowhere else to put decisions.
   The architecture becomes *harder* to perceive, which inverts the artifact's entire purpose
   [[8]](#ref-8). This is the failure the reversibility test in [section 6](#6-debates-and-contested-boundaries)
   is designed to prevent.
6. **The orphaned record.** The author leaves, and the record has no owner and no one who will
   supersede it when it goes stale. It ages into misinformation.
7. **Consequences that are all upside.** A record whose costs are cosmetic is a record whose analysis
   was retrospective. Nygard's insistence that all consequences be listed is aimed squarely at this
   [[1]](#ref-1).
8. **The wiki.** Storing records anywhere other than the repository, which ThoughtWorks specifically
   advises against [[9]](#ref-9). Records that live where the code does not are records that get
   read when someone remembers they exist, which is to say rarely.

---

## 8. Relationships to other artifacts

- **Precedes it:** an **RFC** or design proposal, where cross-team input is gathered *before* the
  call is made. The RFC is the debate; the ADR is the verdict [[11]](#ref-11).
- **Precedes it:** a **spike** or technical investigation, which produces the evidence an ADR's
  Decision Drivers refer to.
- **Follows it:** the **technical design doc** or implementation plan, which elaborates *how* to
  execute the decision the ADR settled. If a design doc re-argues the choice, the ADR failed.
- **Sibling:** the **`AGENTS.md` / `CLAUDE.md` instruction file.** The decisions directory carries
  the *why* and the history; the instruction file carries the *what to do now*. They are complements,
  and neither substitutes for the other (see [section 6](#6-debates-and-contested-boundaries)).
- **Itself:** ADRs form **supersession chains.** A record's most important outbound link is often to
  the record that replaced it. In this library, the chain is the deliverable.
- **In this repo:** the ADR pairs with the [`develop-adr`](https://github.com/product-on-purpose/pm-skills)
  skill in pm-skills, which drafts a record interactively. See the compatibility note in
  [`adr_guide.md`](adr_guide.md).

---

## 9. Adaptations

- **Regulated, safety-critical, or audited work.** Use the full variant, and treat **Confirmation**
  as mandatory rather than optional: an auditor's question is almost always "how do you know this is
  still true?" ISO/IEC/IEEE 42010 requires that rationale, including rejected alternatives, be
  captured somewhere in the architecture description; ADRs are a good way to satisfy that, though the
  standard does not require this or any other specific format [[12]](#ref-12).
- **Solo developers and very small teams.** The record is a letter to yourself in eighteen months,
  and that reader has forgotten everything. Lean is enough. Skipping the practice entirely because
  "I will remember" is the most reliably regretted call in this whole document.
- **Large organizations and many repositories.** Decision records fragment across repos, and
  discoverability becomes the binding constraint. A cross-repo index or a dedicated searchable site
  is the usual answer [[17]](#ref-17). Note honestly that no study establishes how well large
  collections actually get used; the searchability problem at scale is widely asserted and thinly
  evidenced.
- **Who writes them.** Every source this bundle's research surfaced lands in the same place, so this
  is *not* a real debate: the whole team writes them, with a designated owner per record
  [[16]](#ref-16). The architect-only model persists in some enterprise settings, but the research
  turned up nobody publicly defending it.
- **Backfilling.** Recording a decision that was made months ago is legitimate and Spotify explicitly
  endorses it [[10]](#ref-10). Set the `date` to when the decision was actually made, not when you
  wrote it down, and say in More Information that it was reconstructed. A backfilled record that
  pretends to be contemporaneous is the beginning of approval theater.

---

## 10. Worked example

[`adr_example.md`](adr_example.md) is a full-variant record of a **real decision made in this
repository**: the choice to make a bundle's `sizes_available` field the authoritative size contract
that the governance gate enforces in both directions.

It is deliberately not an invented scenario. It is the first worked example in this library that was
not authored to be an example, and it can be checked against the live artifacts it produced: the
decision it records is [ADR 0010](../../docs/internal/decisions/0010-meta-declares-size-contract.md),
and its **Confirmation** section points at gate checks that actually run in CI, on this repository,
on every push to `main` and every pull request. It demonstrates the sections teams most often skip
(Decision Drivers, Confirmation, and
an honest set of cons on the *winning* option), and it shows the lean-to-full relationship directly:
the repo's own copy of that record is leaner than the example, which is itself the point.

---

## References

Tagged by reliability: `[primary]` standards body, regulator, or originating source; `[practitioner]` recognized independent authority; `[vendor]` commercially motivated, reliable on convention. Researched 2026-07-14. Retrieval status per source is recorded in [`adr_research-log.md`](adr_research-log.md).

<a id="ref-1"></a>[1] Michael Nygard. "[Documenting Architecture Decisions](https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions)." Cognitect, 2011-11-15 (accessed 2026-07-14). [primary]

<a id="ref-2"></a>[2] adr organization (maintainer Oliver Kopp). "[MADR: Markdown Architectural Decision Records](https://adr.github.io/madr/), v4.0.0." adr.github.io/madr, released 2024-09-17; [minimal](https://raw.githubusercontent.com/adr/madr/main/template/adr-template-minimal.md) and [full](https://raw.githubusercontent.com/adr/madr/main/template/adr-template.md) templates and [CHANGELOG](https://github.com/adr/madr) fetched raw (accessed 2026-07-14). [practitioner]

<a id="ref-3"></a>[3] Martin Fowler. "[Architecture Decision Record](https://martinfowler.com/bliki/ArchitectureDecisionRecord.html)." martinfowler.com (accessed 2026-07-14). [practitioner]

<a id="ref-4"></a>[4] Jeff Tyree and Art Akerman. "[Architecture Decisions: Demystifying Architecture](https://dl.acm.org/doi/10.1109/MS.2005.27)." IEEE Software, vol. 22, no. 2, pp. 19-27, 2005. DOI 10.1109/MS.2005.27 (paywalled; field list via secondary reconstruction, see research log). [practitioner]

<a id="ref-5"></a>[5] Uwe Zdun, Rafael Capilla, Huy Tran and Olaf Zimmermann. "[Sustainable Architectural Design Decisions](https://doi.org/10.1109/MS.2013.97)." IEEE Software, vol. 30, no. 6, pp. 46-53, 2013. DOI 10.1109/MS.2013.97 (paywalled; format confirmed via [6]). [practitioner]

<a id="ref-6"></a>[6] Olaf Zimmermann. "[Y-Statements: A Light Template for Architectural Decision Capturing](https://medium.com/olzzio/y-statements-10eb07b5a177)." Medium, 2020-05-07; see also [ozimmer.ch](https://ozimmer.ch/practices/2020/04/27/ArchitectureDecisionMaking.html), 2020-04-27 (accessed 2026-07-14). [primary]

<a id="ref-7"></a>[7] Olaf Zimmermann. "[Architectural Decision Records: Any Decision Records?](https://ozimmer.ch/practices/2021/04/23/AnyDecisionRecords.html)" ozimmer.ch, 2021-04-23 (accessed 2026-07-14). [primary]

<a id="ref-8"></a>[8] Pierre Pureur and Kurt Bittner. "[What Is the Purpose of Architectural Decision Records?](https://www.infoq.com/articles/architectural-decision-record-purpose/)" InfoQ (accessed 2026-07-14). [practitioner]

<a id="ref-9"></a>[9] Thoughtworks. "[Lightweight Architecture Decision Records](https://www.thoughtworks.com/en-us/radar/techniques/lightweight-architecture-decision-records)." Technology Radar; entered Trial November 2016, now Adopt (accessed 2026-07-14). [practitioner]

<a id="ref-10"></a>[10] Spotify Engineering. "[When Should I Write an Architecture Decision Record?](https://engineering.atspotify.com/2020/04/when-should-i-write-an-architecture-decision-record)" engineering.atspotify.com, 2020-04 (accessed 2026-07-14). [practitioner]

<a id="ref-11"></a>[11] Candost Dagdeviren. "[ADRs and RFCs: Differences and When to Use Which](https://candost.blog/adrs-rfcs-differences-when-which/)." candost.blog (accessed 2026-07-14). [practitioner]

<a id="ref-12"></a>[12] ISO/IEC/IEEE. "[ISO/IEC/IEEE 42010:2022, Software, systems and enterprise: Architecture description](https://www.iso.org/standard/74393.html)." International Organization for Standardization, 2022 (paywalled; scope confirmed via secondary sources, see research log). [primary]

<a id="ref-13"></a>[13] Drew Dillon and Kasyap Varanasi. "[Context-Augmented Code Generation: How Product Context Improves AI Coding Agent Decision Compliance by 49%](https://arxiv.org/abs/2605.08112)." arXiv preprint 2605.08112, submitted 2026-04-27 (accessed 2026-07-14). **Read the caution in section 6.5 before citing this.** The intervention is the authors' own commercial product-context system, not ADRs; the 49 figure is a percentage-point delta (46% to 95%), not a relative gain; single preprint, 8 tasks, not independently replicated. Tagged vendor because the authors are evaluating their own product. [vendor]

<a id="ref-14"></a>[14] Theo Valmis. "[How AI Coding Agents Use ADRs](https://mnemehq.com/insights/how-ai-coding-agents-use-adrs/)." Mneme HQ, 2026-07 (accessed 2026-07-14). Conceptual framing, no measured outcomes. [vendor]

<a id="ref-15"></a>[15] Catio. "[Architecture Decision Records](https://www.catio.tech/blog/architecture-decision-record)." catio.tech, 2026 (**search-corroborated; page not fetched**; see research log). Used only for failure modes other sources independently attest; nothing is quoted from it. [vendor]

<a id="ref-16"></a>[16] Stride. "[Should Engineers Write ADRs?](https://www.stride.page/blog/should-engineers-write-adrs)" stride.page (accessed 2026-07-14). [practitioner]

<a id="ref-17"></a>[17] Amazon Web Services. "[Master Architecture Decision Records: Best Practices for Effective Decision Making](https://aws.amazon.com/blogs/architecture/master-architecture-decision-records-adrs-best-practices-for-effective-decision-making/)." AWS Architecture Blog (**search-corroborated; page not fetched**; see research log). [vendor]

<a id="ref-18"></a>[18] adr organization. "[ADR Tooling](https://adr.github.io/adr-tooling/)." adr.github.io (accessed 2026-07-14). Establishes which tools support which format: `adr-tools` is Nygard-only; Log4brains and adr-manager are MADR. [practitioner]

<a id="ref-19"></a>[19] "[Can ADRs replace design docs and RFCs?](https://github.com/adr/madr/issues/97)" Issue 97, adr/madr, opened 2023, open at time of writing (accessed 2026-07-14). [primary]
