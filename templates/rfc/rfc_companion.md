# Companion: The Request for Comments (RFC)

> The deep explainer for the RFC bundle. Read this to understand what an engineering RFC is, where
> it came from, why it is shaped the way it is, and where practitioners disagree about it. The short
> operator card is [`rfc_guide.md`](rfc_guide.md); a fully worked instance is
> [`rfc_example.md`](rfc_example.md). Inline citations like [[1]](#ref-1) resolve to the
> [References](#references) at the bottom, tagged by source reliability.

---

## 1. Orientation

A Request for Comments is a written proposal that says **here is a change I want to make, and here is
your chance to shape it before it is decided.** It circulates a motivation, a proposal, the
alternatives, the trade-offs, and the open questions to an audience whose input can still change the
outcome. Its whole reason for existing is the feedback it gathers while the decision is still open.

That last clause is the entire artifact, and it is worth stating against its near-twin. An RFC is
the **pre-decision** document; the [ADR](../adr/adr_companion.md) is the **post-decision** one. An
RFC asks "should we do this, and how?"; an ADR records "we decided this, because." Run them in
sequence, not in competition: the RFC gathers the input, and when the decision lands, an ADR records
it [[11]](#ref-11)[[20]](#ref-20).

**At a glance**
- The value is in the **comment**, not the document. An RFC read by no one who could change it has
  failed, however well written.
- It is **mutable while open and settled once decided.** Unlike an ADR, you revise an RFC freely
  during review; the discipline is to record the outcome when the discussion closes.
- The **alternatives and the open questions** are the load-bearing sections. They are what turn a
  reader from an audience into a reviewer.
- It needs a **decider and a deadline.** An RFC with an open-ended comment period and no named
  authority does not reach consensus; it reaches exhaustion [[16]](#ref-16).
- The name is older than the practice and means almost the opposite of what it did at the source
  (see [section 2](#2-origins-and-evolution)).

If you read nothing else: an RFC is a **forcing function for input before commitment.** Written after
the decision, it is theater. Written before, it is the cheapest place your colleagues will ever catch
your mistake.

---

## 2. Origins and evolution

**The name is a 1969 act of humility, and it has traveled strangely.** The first Request for Comments,
RFC 1, was written by Steve Crocker in April 1969 for the small group building the ARPANET, the
network that became the internet [[1]](#ref-1). Crocker's group had, in the words of a participant
history, no charter and no authority; they were graduate students documenting tentative agreements
[[4]](#ref-4). RFC 1 opens by disclaiming its own weight: *"I present here some of the tentative
agreements reached and some of the open questions encountered,"* and, plainly, *"Very little of what
is here is firm and reactions are expected"* [[1]](#ref-1).

That posture was deliberate. RFC 3, which set the conventions for the series, made informality a
rule: *"Notes are encouraged to be timely rather than polished,"* and the series existed, it said,
because *"we hope to promote the exchange and discussion of considerably less than authoritative
ideas"* [[2]](#ref-2). The name "Request for Comments" was chosen precisely to avoid sounding
authoritative, so that anyone would feel entitled to respond. In his own later reflections Crocker
described even the word "proposal" as having felt too strong for what they were doing [[4]](#ref-4).

**Then the IETF RFC became almost the opposite of that.** As the ARPANET conventions matured into the
Internet Engineering Task Force, the RFC series became the **archival, official publication channel**
for internet standards [[3]](#ref-3). A modern IETF RFC is published *after* the working-group
discussion concludes, carries a formal maturity level (Proposed Standard, Internet Standard,
Informational, Experimental, Best Current Practice, Historic), and is **permanent**: once published,
an RFC is not edited. Corrections are handled by separate errata or by publishing a new,
higher-numbered RFC that obsoletes the old one, never by changing the original [[6]](#ref-6). The
"Request for Comments" has become, at the IETF, a document published when the comments are essentially
over. The name is now nominal.

**The engineering RFC is a second borrowing, and it went back to the source.** Sometime in the 2010s,
software companies and open-source projects took the *name* "RFC" and attached it to an internal
proposal circulated *before* a decision, to gather input, often discarded or superseded once the
decision is made. The Rust project formalized one of the earliest and most-copied versions in 2014,
adopting the term with no reference to its IETF origin [[13]](#ref-13); React followed in 2017,
explicitly citing Yarn, Ember, and Rust as inspiration [[14]](#ref-14). By the early 2020s the format
had spread across Uber, Squarespace, Google (as "design docs"), Stripe, Spotify, and many others,
mostly by engineers carrying the practice between employers [[10]](#ref-10)[[19]](#ref-19).

Here is the irony worth keeping: the engineering RFC, by circulating provisional ideas for comment
*before* anything is settled, is far closer to what Crocker meant in 1969 than the modern IETF RFC is.
The corporate world borrowed the name a second time and, without meaning to, recovered the original
spirit that the IETF had formalized away.

**Some borrowers changed the name to fix it.** Oxide Computer runs the practice but calls its
documents RFDs, Requests for *Discussion*, explicitly to avoid confusion with the IETF construct and
its accreted formality, while keeping RFC 3's "timely rather than polished" spirit [[15]](#ref-15).
Python's PEPs (Python Enhancement Proposals) are a parallel cousin with their own lifecycle
[[18]](#ref-18). The underlying artifact is the same; the naming is a small running argument about
which tradition you are claiming.

---

## 3. Anatomy (section by section)

### Frontmatter and status

The YAML block carries `title`, `status`, `authors`, and dates; the full variant adds `reviewers`
and a `review_by` date. **`status` is the field that matters most**, and it is a lifecycle:
`draft` to `in-review` to `accepted`/`rejected`/`withdrawn`, and later possibly `superseded`.

*Beginner note:* update the status the moment the RFC moves, especially when a decision is reached.
The most common way an RFC collection rots is a pile of documents stuck at `in-review` forever,
because a decision was made in a meeting and nobody went back to mark the document [[12]](#ref-12).

*Expert note:* the full variant asks for named `reviewers` and a `review_by` date on purpose. An RFC
addressed to everyone is addressed to no one, and an RFC with no deadline discusses itself to death.
Naming who must weigh in, and by when, is the difference between a process that decides and one that
merely accumulates comments [[16]](#ref-16)[[17]](#ref-17).

### Summary

Two or three sentences: the proposed change and what becomes true if it ships.

*Beginner note:* write this last, once you know what you are actually proposing, but put it first.
It is the triage surface: most people decide whether to engage from the summary alone.

*Expert note:* the summary must contain the *proposal*, not just the problem. A summary that only
states the problem sends readers into the Motivation section looking for a proposal that is not
there yet, and the thread fills with people re-litigating whether the problem is real.

### Motivation

The problem or opportunity, the forces in play, and the cost of doing nothing.

*Beginner note:* this is where you spend the most effort. Describe who feels the problem, how often,
and what it costs. Concrete beats abstract: "leaked twice this year, each rotation costs a day" lands
where "not best practice" does not.

*Expert note:* the failure mode is motivation reverse-engineered from the solution you already
favor, so it only justifies that one option. Write the problem so honestly that a *different*
proposal could win on its merits. If your motivation cannot survive someone else's solution, it is
advocacy wearing the mask of analysis, and a good reviewer will smell it.

### Goals and Non-Goals *(full variant only)*

Goals: what the proposal must achieve. Non-goals: what it is deliberately not addressing.

*Beginner note:* the non-goals are the more valuable half. They tell reviewers what *not* to bring
up, which keeps the discussion bounded.

*Expert note:* most runaway RFC threads are reviewers arguing about something the author never meant
to solve. A crisp non-goal ends that thread before it opens. Naming non-goals is one of the most
reliable ways to keep an RFC from sprawling, and omitting them is a common way to let it.

### Proposal

The proposed change as a shared mental model: the core idea, concrete enough to disagree with.

*Beginner note:* aim for the level where a colleague could argue with you. Not the technology name
("adopt mTLS"), and not the byte-level detail, but the shape: what changes, and how someone
experiences it.

*Expert note:* the proposal has to present a real surface to push on. A proposal pitched too
abstractly produces vague approval and no genuine review, which is how a weak idea sails through and
fails later. Give reviewers something specific enough to find the flaw in.

### Detailed Design *(full variant only)*

The how, for the reviewers who must implement or integrate: interfaces, failure modes, migration,
security and privacy surface.

*Beginner note:* cover the parts a careful reviewer will probe: what happens when it fails, how data
migrates, what the security surface is. This is where a proposal that sounded fine reveals whether it
works.

*Expert note:* resist using length as a weapon. Jacob Kaplan-Moss's critique of RFC processes names
the failure precisely: they can reward people who write to exhaustion, burying objections under
volume until reviewers give up and approve [[16]](#ref-16). An exhaustive design nobody can finish
reading is approved by fatigue, not by understanding. Detail the risky parts; compress the obvious
ones.

### Alternatives Considered

The options you genuinely weighed and why you are not proposing them, including "do nothing."

*Beginner note:* include "do nothing" almost always. It is a real option, it is frequently correct,
and writing it down forces you to state why acting now beats waiting.

*Expert note:* this section is the clearest signal of whether the RFC is reasoning or rationalizing.
Two decoys and a winner is a sales pitch. A genuinely considered alternative, described well enough
that a reader could prefer it, is what earns the proposal its credibility, and it is where the
reviewer who knows something you do not gets the opening to say so. Its absence is a well-worn
anti-pattern: reviewers will supply the alternatives themselves, adversarially.

### Drawbacks and Trade-offs *(full variant only)*

The honest costs of the proposal itself: what gets worse, harder, or riskier if it is accepted.

*Beginner note:* name at least one real cost that someone would actually act on. New dependency, new
operational burden, new failure surface, a group who pays for it.

*Expert note:* a proposal presented with no downsides tells reviewers you are selling, and it invites
them to go hunting for the cost you concealed, which is slower and more adversarial than naming it
yourself. The trade-off you disclose is disarming; the one they discover is disqualifying.

### Open Questions

What is genuinely undecided, that you want input on.

*Beginner note:* these are the literal request for comment. They point reviewers at exactly where
their input changes the outcome, which is how you get real engagement instead of a silent nod.

*Expert note:* a confident-looking RFC with no open questions gets rubber-stamped, and the questions
you buried resurface later as production incidents. Surfacing the hard unknowns is not weakness; it
is the whole mechanism. An RFC with no open questions is usually hiding them, not finished.

### Rollout and Adoption *(full variant only)*

How the change reaches production and gets adopted: sequencing, flags, migration, backout, and how
you will know it worked.

*Beginner note:* say what ships first, what is behind a flag, how teams migrate, who supports them,
and how you back out if it goes wrong.

*Expert note:* many RFCs die at rollout rather than at design. The idea is sound, everyone agrees,
and then no one owns the messy path to production, so it never ships. A credible adoption plan, with
an owner and a backout, is often what separates an RFC that happens from one that is merely admired.

### Outcome

The decision once made: accepted, rejected, or deferred; who decided; the date; the one-line why;
and what happens next.

*Beginner note:* while the RFC is open, this section says so ("in review, decision due <date>"). The
moment a decision is reached, record it here and update the status. Do not delete the section because
the RFC is unfinished.

*Expert note:* an RFC that never records its own outcome is the format's most common failure, and the
most corrosive: the discussion happens, a decision forms somewhere off the page, and the document is
abandoned mid-thread, so six months later no one can tell what was decided or why. This section is
the bridge to the [ADR](../adr/adr_companion.md): an accepted RFC's Outcome is what the resulting ADR
is written from. The RFC holds the argument; the ADR holds the verdict [[11]](#ref-11).

---

## 4. Variants and sizing

**Lean is the default.** It carries Summary, Motivation, Proposal, Alternatives Considered, Open
Questions, and Outcome. That is enough to state a change, show you considered the alternatives, ask
for input where it matters, and record what was decided. Most proposals that deserve an RFC at all
are well served by the lean one.

**Full adds Goals and Non-Goals, Detailed Design, Drawbacks and Trade-offs, and Rollout and
Adoption.** The shared sections keep their names and order, so lean is a strict subset of full.

The signal to scale up is the **cost of being wrong**, not the size of the system:

- The change is hard or slow to reverse (a data model, an auth scheme, a public contract).
- It crosses several teams, who need the Detailed Design and the Rollout plan to reason about it.
- It carries security, privacy, or regulatory weight, and the Drawbacks section will be read by
  someone whose job is to find what you missed.
- Reasonable people are likely to disagree, and the discussion needs the structure that Goals,
  Non-Goals, and explicit trade-offs provide to stay bounded.

Otherwise, lean. The full variant reached for by reflex is exactly how an RFC process becomes the
heavyweight bureaucracy its critics describe: templates with ten mandatory sections that no small
change can justify filling, so people either avoid the process or treat it as a checkbox
[[12]](#ref-12).

---

## 5. Methodology lineage

Different traditions run the same artifact differently, and the differences are instructive.

| Tradition | Form | What it optimizes for |
|---|---|---|
| **IETF RFC** | Permanent, archival, published post-consensus, formal maturity levels | Durable, citable standards for an entire industry [[3]](#ref-3)[[6]](#ref-6) |
| **Crocker's original (1969)** | Timely, unpolished, provisional, explicitly non-authoritative | Lowering the barrier to circulating an unfinished idea [[1]](#ref-1)[[2]](#ref-2) |
| **Rust RFC** | PR-based, subteam sign-off, 10-day Final Comment Period, tracking issue on accept | Open-source governance at scale, with a clear decider [[13]](#ref-13) |
| **React RFC** | Two classes: team RFCs (post-design) and community RFCs (rarely merged), 3-day FCP | A small core team steering a huge community [[14]](#ref-14) |
| **Oxide RFD** | Renamed to "Discussion," six states, covers culture as well as code | Reclaiming the original informal spirit, minus IETF baggage [[15]](#ref-15) |
| **Python PEP** | Formal enhancement proposals, Steering Council decides, "Provisional" state | Language governance with room to revise post-release [[18]](#ref-18) |
| **Corporate eng RFC** | Internal, pre-decision, often ephemeral, tiered by impact | Aligning teams before a costly build, then feeding an ADR [[9]](#ref-9)[[10]](#ref-10) |

**Why this bundle teaches the corporate, pre-decision RFC** rather than the IETF standards
instrument: this is a product-lifecycle template library, and the RFC people reach for during product
and engineering work is the internal proposal that gathers input before a decision. The IETF RFC is a
different and more specialized artifact that this template does not try to serve. Where the two are
confused, [section 2](#2-origins-and-evolution) is the disambiguation.

One structural choice is worth calling out against every one of these traditions: this template puts
an **Outcome** section even in the lean variant. Several real processes leave the decision record
implicit or off in a separate tracking issue, which is exactly where the "no decision recorded"
failure lives. Making Outcome a required section, at every size, is this bundle's opinionated fix.

---

## 6. Debates and contested boundaries

### 6.1 Alignment versus paralysis (the live one)

**Camp A, RFCs create durable alignment.** Writing a proposal down and circulating it for review
catches expensive mistakes on paper, democratizes decisions beyond the people in the room, and leaves
a record of why things were done [[10]](#ref-10)[[19]](#ref-19). Squarespace redesigned its review
process specifically to catch subtle flaws and needless complexity before implementation [[17]](#ref-17).

**Camp B, RFC processes are a poor fit for most organizations.** Jacob Kaplan-Moss makes the sharpest
version: as an organization grows, RFC discussions tend toward the endless, because there is always
one more question or concern, and the process rewards those who can out-write and out-last everyone
else. Worse, he argues, the processes are insensitive to real power dynamics: they present the org as
an even, egalitarian body reaching consensus, when companies do not actually operate that way
[[16]](#ref-16).

*This bundle's reading:* both camps are describing the same artifact with and without a **decider**.
The thing that turns durable alignment into endless discussion is the absence of a named authority and
a deadline. Kaplan-Moss's own prescription is not "stop writing" but "document, discuss, and *then
decide*," with an explicit decision mechanism [[16]](#ref-16). That is why this template's full
variant asks for named reviewers and a `review_by` date, and why even the lean one has an Outcome
section: the cure for paralysis is not less writing, it is a structural commitment to decide.

### 6.2 The rubber-stamp RFC

A widely named failure: the "what" is settled in advance, in meetings or by a senior voice, and the
RFC is written afterward to document the "how" while performing consultation that already happened.
The tell is a proposal with no live open questions and an alternatives section full
of decoys. This is the exact analogue of the ADR failure mode where a record is written to spread
accountability rather than to inform, and the fix is the same: if the decision is genuinely made,
write an ADR and stop pretending it is open.

### 6.3 Async writing versus meetings

One camp holds that an RFC's purpose is to *replace* meetings with a written, inclusive, asynchronous
record. Another, learned the hard way, is that pure async fails for complex proposals: Squarespace
pairs async comments with a synchronous architecture-review discussion for the proposals that need
deep review [[17]](#ref-17). The
defensible middle is that async is the default and a meeting is a tool for the specific proposal that
a comment thread cannot resolve, not a ceremony every RFC must pass through.

### 6.4 RFC versus ADR versus design doc

The cleanest distinction in the practitioner literature is temporal and is worth memorizing: an
**RFC proposes a decision and solicits feedback before it is finalized; an ADR records a decision
after it is made** [[11]](#ref-11)[[20]](#ref-20). An accepted RFC can spawn several ADRs, one per
concrete decision it settles [[11]](#ref-11). The **design doc** is the fuzziest term: at Google and
Amazon it is the primary artifact and overlaps heavily with the RFC, and much of the industry uses
"RFC" and "design doc" interchangeably [[10]](#ref-10). This bundle treats the RFC as the
pre-decision proposal, the ADR as the post-decision record, and leaves "design doc" as a
locally-defined near-synonym for the RFC rather than a fourth distinct type.

---

## 7. Anti-patterns and failure modes

1. **The RFC with no decider.** Circulated to everyone, owned by no one, with no deadline. Absent a
   process that moves toward a decision, such an RFC's default outcome is inaction: it stalls in an
   open thread that never closes [[16]](#ref-16). Name an approver and a date.
2. **The rubber stamp.** Written after the decision to perform consultation. No live open questions,
   decoy alternatives. Write an ADR instead.
3. **The comment pile-on / bikeshedding.** Reviewers flood the document, blocking and non-blocking
   feedback indistinguishable, and the author drowns. Squarespace's fix was explicit "yes, if"
   language and named approvers who can actually clear it [[17]](#ref-17).
4. **Writing to exhaustion.** Using length and exhaustive detail to bury objections until reviewers
   give up and approve. Approval by fatigue is not approval [[16]](#ref-16).
5. **Template bloat.** Ten mandatory sections that a small change cannot justify filling, so people
   route around the process or treat it as a checkbox [[12]](#ref-12). This is what the lean variant
   exists to prevent.
6. **No alternatives.** The proposal cannot show it was reasoned, and reviewers supply the missing
   options adversarially. A common substantive weakness.
7. **No recorded outcome.** The discussion concludes, the decision forms off the page, the document
   is abandoned at `in-review`. Later, no one can reconstruct what was decided or why. This bundle's
   required Outcome section is the direct countermeasure [[12]](#ref-12).
8. **Wrong audience.** Sent to people with no stake, who ignore it, while the people who should review
   it never see it. Poor targeting looks like consensus and is actually silence [[12]](#ref-12).
9. **Process without the culture.** An RFC practice needs a blameless, trusting environment; imposed
   on a blame-heavy one, it produces defensive documents rather than honest exploration
   [[12]](#ref-12).

---

## 8. Relationships to other artifacts

- **Feeds it:** a **spike** or technical investigation, which supplies the evidence the Motivation and
  Detailed Design lean on.
- **Follows it:** the **[ADR](../adr/adr_companion.md)**. This is the most important relationship in
  the bundle. An accepted RFC's Outcome is the raw material for one or more ADRs: the RFC is the
  argument and the audience's input; the ADR is the durable verdict, close to the code
  [[11]](#ref-11)[[20]](#ref-20). If your organization uses only one of the two, the common and
  reasonable choice is RFC-for-discussion, ADR-for-record.
- **Overlaps with:** the **design doc**, which in much of the industry is the same artifact under a
  different name [[10]](#ref-10). Do not maintain both for the same decision.
- **Runs beside:** the **PRD**. A PRD says what to build for the user and why; an RFC proposes how to
  build a specific technical piece of it. At companies like Uber the two are stored and reviewed
  side by side [[10]](#ref-10).
- **Cousins in other traditions:** the **IETF RFC** (a permanent standard, not a proposal; see
  [section 2](#2-origins-and-evolution)) and the **Python PEP** (a language-governance proposal with
  its own lifecycle) [[18]](#ref-18).

---

## 9. Adaptations

- **Open-source projects.** Make the RFC a pull request, as Rust and React do, so the proposal, the
  discussion, and the decision all live in version control and the history is public
  [[13]](#ref-13)[[14]](#ref-14). Expect most community RFCs not to merge, and say so, so contributors
  are not misled about the odds [[14]](#ref-14).
- **Large organizations.** Tier the process by impact: a lightweight template for team-scoped changes,
  the full variant for org-wide ones, as Uber did when hundreds of weekly RFCs began overwhelming
  reviewers [[10]](#ref-10). Invest in discoverability early; RFCs scattered across documents that no
  one can find is a named scaling failure.
- **Small teams and solo work.** The lean variant, or a paragraph in a shared doc. The point is to
  externalize the reasoning and invite one other set of eyes before you commit; the ceremony can be
  near zero. Do not build a heavyweight RFC process for a team that fits in one room.
- **Regulated or safety-critical work.** Use the full variant and treat Drawbacks and Detailed Design
  as mandatory; an auditor's first question is about the risks you accepted and the alternatives you
  rejected, which are precisely the RFC's Alternatives and Drawbacks sections.
- **Naming.** If your culture confuses the engineering RFC with the IETF one, consider Oxide's move
  and call them RFDs, Requests for Discussion [[15]](#ref-15). The artifact is what matters; the label
  should reduce confusion, not add it.

---

## 10. Worked example

[`rfc_example.md`](rfc_example.md) is a full-variant RFC for a **real, currently-open decision in this
repository**: whether and how the library should ship a machine-readable metadata schema so that an
agent could select a bundle deterministically (roadmap item WP-21).

It is deliberately a *live* proposal, not a settled one, because that is what an RFC is. Its status is
`in-review` and its Outcome section records that no decision has been made yet, with a decision owner
and a date. This is the honest state of an RFC in flight, and it demonstrates the thing the format is
for: the argument is on the page, the alternatives are real, the open questions are genuinely open,
and the decision, when it comes, will be recorded here and then carried into an ADR. It is the first
example in this library whose Outcome is, correctly, "not yet decided."

---

## References

Tagged by reliability: `[primary]` standards body, regulator, or originating source; `[practitioner]` recognized independent authority; `[vendor]` commercially motivated, reliable on convention. Researched 2026-07-15. Retrieval status per source is recorded in [`rfc_research-log.md`](rfc_research-log.md); the two RFC-series quotations were verified verbatim against the primary text.

<a id="ref-1"></a>[1] Steve Crocker. "[Host Software](https://www.rfc-editor.org/rfc/rfc1.txt)." RFC 1, Network Working Group, 1969-04-07 (accessed 2026-07-15). [primary]

<a id="ref-2"></a>[2] Steve Crocker. "[Documentation Conventions](https://www.rfc-editor.org/rfc/rfc3.txt)." RFC 3, Network Working Group, 1969 (accessed 2026-07-15). [primary]

<a id="ref-3"></a>[3] Scott Bradner. "[The Internet Standards Process, Revision 3](https://www.rfc-editor.org/rfc/rfc2026)." RFC 2026 (BCP 9), IETF, 1996-10 (accessed 2026-07-15). [primary]

<a id="ref-4"></a>[4] Steve Crocker. "[Today's Internet Still Relies on an ARPANET-Era Protocol: The Request for Comments](https://spectrum.ieee.org/todays-internet-still-relies-on-an-arpanetera-protocol-the-request-for-comments)." IEEE Spectrum, 2020-07-29 (accessed 2026-07-15). [primary]

<a id="ref-5"></a>[5] Steve Crocker. "[How the Internet Got Its Rules](https://www.nytimes.com/2009/04/07/opinion/07crocker.html)." The New York Times, 2009-04-07 (paywalled; not fetched, see research log). [primary]

<a id="ref-6"></a>[6] Heather Flanagan and Sandy Ginoza. "[RFC Style Guide](https://www.rfc-editor.org/rfc/rfc7322)." RFC 7322, RFC Editor, 2014-09 (accessed 2026-07-15). [primary]

<a id="ref-7"></a>[7] Michael Nygard. "[Documenting Architecture Decisions](https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions)." Cognitect, 2011-11-15 (accessed 2026-07-15). [practitioner]

<a id="ref-8"></a>[8] Martin Fowler. "[Architecture Decision Record](https://martinfowler.com/bliki/ArchitectureDecisionRecord.html)." martinfowler.com (accessed 2026-07-15). [practitioner]

<a id="ref-9"></a>[9] Phil Calcado. "[A Structured RFC Process](https://philcalcado.com/2018/11/19/a_structured_rfc_process.html)." philcalcado.com, 2018-11-19 (accessed 2026-07-15). [practitioner]

<a id="ref-10"></a>[10] Gergely Orosz. "[Companies Using RFCs or Design Docs and Examples of These](https://blog.pragmaticengineer.com/rfcs-and-design-docs/)." The Pragmatic Engineer, 2022 (partially paywalled; free portion fetched, see research log). [practitioner]

<a id="ref-11"></a>[11] Candost Dagdeviren. "[ADRs and RFCs: Their Differences and When to Use Which](https://candost.blog/adrs-rfcs-differences-when-which/)." candost.blog (accessed 2026-07-15). [practitioner]

<a id="ref-12"></a>[12] Candost Dagdeviren. "[How and Why RFCs Fail](https://candost.blog/how-and-why-rfcs-fail/)." candost.blog (accessed 2026-07-15). [practitioner]

<a id="ref-13"></a>[13] The Rust Project. "[The Rust RFC Book](https://rust-lang.github.io/rfcs/)" and [RFC 0002 (RFC Process)](https://rust-lang.github.io/rfcs/0002-rfc-process.html). rust-lang.github.io/rfcs, from 2014 (accessed 2026-07-15). [primary]

<a id="ref-14"></a>[14] The React Team. "[React RFCs](https://github.com/reactjs/rfcs)" (README) and "[Introducing the React RFC Process](https://legacy.reactjs.org/blog/2017/12/07/introducing-the-react-rfc-process.html)," 2017-12-07 (accessed 2026-07-15). [primary]

<a id="ref-15"></a>[15] Oxide Computer Company. "[RFD 1: Requests for Discussion](https://rfd.shared.oxide.computer/rfd/0001)" and the [RFD 1 blog post](https://oxide.computer/blog/rfd-1-requests-for-discussion) (accessed 2026-07-15). [primary]

<a id="ref-16"></a>[16] Jacob Kaplan-Moss. "[RFC processes are a poor fit for most organizations](https://jacobian.org/2023/dec/1/against-rfcs/)." jacobian.org, 2023-12-01 (accessed 2026-07-15). [practitioner]

<a id="ref-17"></a>[17] Squarespace Engineering. "[The Power of 'Yes, If': Iterating on our RFC Process](https://engineering.squarespace.com/blog/2019/the-power-of-yes-if)." engineering.squarespace.com, 2019 (accessed 2026-07-15). [practitioner]

<a id="ref-18"></a>[18] Barry Warsaw, Jeremy Hylton, David Goodger, Nick Coghlan. "[PEP 1: PEP Purpose and Guidelines](https://peps.python.org/pep-0001/)." Python Software Foundation (accessed 2026-07-15). [primary]

<a id="ref-19"></a>[19] Vaidehi Joshi. "[Planning for Change with RFCs](https://increment.com/planning/planning-with-requests-for-comments/)." Increment, Issue 19, 2021 (accessed 2026-07-15). [practitioner]

<a id="ref-20"></a>[20] "[RFCs vs ADRs](https://designdoc.tech/blog/rfcs-vs-adrs)." DesignDoc.tech, 2026 (accessed 2026-07-15). [vendor]
