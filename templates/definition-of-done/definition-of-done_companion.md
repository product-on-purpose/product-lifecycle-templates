# Companion: The Definition of Done

> The deep explainer for the definition-of-done bundle. Read this to understand what a Definition of
> Done actually is, where the 2020 Scrum Guide changed it, and where the folklore around it diverges
> from the canon. The short operator card is [`definition-of-done_guide.md`](definition-of-done_guide.md);
> a fully worked instance is [`definition-of-done_example.md`](definition-of-done_example.md). Inline
> citations like [[1]](#ref-1) resolve to the [References](#references) at the bottom, tagged by source
> reliability. The full retrieval trail is
> [`definition-of-done_research-log.md`](definition-of-done_research-log.md).

---

## 1. Orientation

A Definition of Done is "a formal description of the state of the Increment when it meets the quality
measures required for the product" [[1]](#ref-1). The 2020 Scrum Guide places it in a three-way
structure alongside the Product Backlog's Product Goal and the Sprint Backlog's Sprint Goal: "For the
Increment it is the Definition of Done" [[1]](#ref-1). It is a **commitment attached to an artifact**,
not an artifact of its own, and that framing is new as of 2020 [[2]](#ref-2). The job in one sentence:
one standard, applied to every increment, so that "done" stops being a matter of opinion at the moment
someone most wants it to be.

At a glance:

- It is a **commitment, not an artifact**, and that is a 2020 change. Scrum.org's own revisions page
  confirms it: "the Increment has the Definition of Done (now without the quotes)"
  [[2]](#ref-2). Material written before 2020, and a great deal of circulating material, describes it
  the older way.
- An organizational standard is a **floor, never a ceiling**, and the rule has two branches depending
  on whether one exists [[1]](#ref-1).
- **Nobody owns it.** Every source this research read makes conformance collective or contingent; no
  source names a single accountable role [[1]](#ref-1). This bundle corrects a citation error elsewhere
  in this library on exactly that point (see [section 8](#8-relationships-to-other-artifacts)).
- **Three things everyone says about it are not in the Scrum Guide**: that it is a checklist, that it
  gets stricter over time via the retrospective, and that it is "the team's contract." All three are
  folklore, not canon (see [section 6](#6-debates-and-contested-boundaries)).
- **One statistic traces cleanly, and its own authors call the evidence base thin.** The widely
  circulating claim that 93 percent of practitioners find the DoD valuable resolves to one real survey
  of 137 practitioners across 45 countries, "93% of the respondents perceive DoD as at least valuable
  for their ventures" [[13]](#ref-13), which is also the only controlled evidence this research located.

This family's own contract names its citation hazard as "folklore presented as standard." That is not
a hedge; the 2020 Guide was read directly for this bundle, and several claims that circulate as settled
practice simply are not in it.

---

## 2. Origins and evolution

The Definition of Done does not have an origin story the way a named practice like Y-statements does;
it is a concept the Scrum canon has carried since early editions and reshaped over time, most sharply
in 2020. Two editions of the Scrum Guide were read directly for this bundle, and comparing them line by
line is the most reliable way to see what actually changed.

**The 2017 Guide tied the Definition of Done to the Sprint Retrospective by name.** It reads: "During
each Sprint Retrospective, the Scrum Team plans ways to increase product quality by improving work
processes or adapting the definition of 'Done', if appropriate and not in conflict with product or
organizational standards" [[15]](#ref-15). That sentence gives the DoD an explicit adaptation
mechanism and a named moment for it.

**The 2020 rewrite did not carry that sentence forward**, at least not in the passages this research
could retrieve across repeated attempts. What the 2020 text does instead is fold the DoD into a
three-part "commitments" structure that the 2017 edition did not have, alongside the Product Goal and
Sprint Goal [[1]](#ref-1)[[2]](#ref-2). The organizational-standard rule also narrowed in wording: 2017
spoke of "conventions, standards or guidelines of the development organization" [[15]](#ref-15); 2020
tightened this to "standards of the organization" [[1]](#ref-1). No source read for this bundle states
why the authors narrowed the phrase, and this bundle does not guess. It is recorded as a version
difference, not resolved as a deliberate change of policy.

**The vocabulary shed a role along the way.** The 2020 Guide also retired "Development Team" as a named
sub-role in favor of "Developers" as part of the Scrum Team, which is the same edition that trimmed the
DoD's retrospective-trigger sentence. Whether the two changes share a cause is exactly the kind of
question the Guide itself does not answer.

---

## 3. Anatomy (section by section)

### Scope and Ownership

**What it is.** The statement of what the Definition of Done applies to (a story, a feature, a
release) and who is bound by it.

**Why it exists.** The Guide places conformance with the people doing the work, not with a named role
above them: "The Developers are required to conform to the Definition of Done," and instilling quality
"by adhering to a Definition of Done" is listed among their accountabilities [[1]](#ref-1). Authorship
is contingent rather than assigned: an organizational standard, where one exists, binds every team as a
minimum; where none exists, the team creates its own [[1]](#ref-1). For multiple teams sharing a
product, the Guide is unambiguous that there is **one** Definition of Done between them: they "must
mutually define and comply with the same Definition of Done" [[1]](#ref-1).

*Beginner note:* write down who is bound (usually the whole delivery team) and what standard, if any,
was inherited from above the team. If an organizational standard exists, name it and treat it as a
floor you may raise, never lower. If none exists, say so plainly; a silent absence reads as an
oversight later.

*Expert note:* resist naming a single owner even though it is tempting and common in practice. Every
source this research read makes ownership collective or contingent, and no source names a sole
accountable role [[1]](#ref-1). A practitioner framing worth knowing, because it circulates widely, is
Roman Pichler's: the Product Owner "appl[ies] the done criteria to accept or reject work results when
reviewing items," acting as "the guardian of quality" at the review [[17]](#ref-17). Read that as an
**enforcement-at-acceptance** claim, not a change-authority claim; it does not contradict the Guide's
placement of conformance with the Developers, but it is a real difference in emphasis between a primary
source and a named practitioner, and the practitioner framing is the one most likely to be repeated as
settled fact.

### Done Criteria

**What it is.** The concrete list of conditions an increment must meet.

**Why it exists.** This is the baseline shape every source read for this bundle carries in some form,
whether as a flat list or a sectioned one
[[1]](#ref-1)[[3]](#ref-3)[[4]](#ref-4)[[5]](#ref-5)[[6]](#ref-6). Agile Alliance's canonical framing
puts it plainly: "the team agrees on, and displays prominently somewhere in the team room, a list of
criteria" that a product increment must meet before it counts as done [[5]](#ref-5). What varies is
scope and length, not the presence of a criteria list.

*Beginner note:* two real examples show the actual range. A published vendor checklist runs six or
seven flat items scoped to team type: "Task meets defined acceptance criteria," "Code reviewed and
approved," "Feature deployed to staging and verified" [[6]](#ref-6). At the other end, GitLab's live,
currently shipping engineering Definition of Done runs 41 dated line items across six labeled
subsections gating a production merge, including "Unit, integration, and system tests that all pass on
the CI server" and "Confirmed to be working in the production with no new Sentry errors after the
contribution is deployed" [[4]](#ref-4). Neither is wrong; they gate different scopes.

*Expert note:* write criteria as **verifiable states**, not activities. "Code is good quality" and
"testing done" are not verifiable on their own terms, a failure mode named directly in vendor
commentary on DoD practice [[14]](#ref-14). GitLab's items read as checkable states for exactly this
reason: "Verified as working in production," not "verify it works."

### Criteria by Level *(full variant only)*

**What it is.** A sorting rule that separates criteria checkable per feature from criteria that only
make sense per sprint or per release.

**Why it exists.** Scrum Alliance is the clearest named source arguing that a Definition of Done is not
one flat list but a set of levels, and it supplies a decision tree rather than a fixed list per level:
"Can we do this activity for each feature? If not, then... Can we do this activity for each sprint? If
not, then... We have to do this activity for our release!" [[3]](#ref-3). This bundle's research
treated a fixed three-tier list as a candidate format and rejected it: the levels are not a
structurally distinct document, they are a sorting rule for criteria that already live inside one Done
Criteria section (see [section 4](#4-variants-and-sizing)).

*Beginner note:* for each criterion you write, ask the Scrum Alliance question in order: can this be
done for every single feature? If yes, it belongs at feature level. If not, can it be done every
sprint? If not, it is a release-level activity. Sort your list this way rather than guessing which
level feels right.

*Expert note:* the value of this section is catching criteria that quietly got promoted to "every
feature" when they can only realistically happen at release cadence (a full security audit, a
compliance sign-off). Leaving such an item at feature level does not make it happen more often; it
makes the Definition of Done a document nobody can actually satisfy, which is one route into the
"infeasible... DoD" problem the one controlled survey in this literature records directly
[[13]](#ref-13).

### What This Excludes *(full variant only)*

**What it is.** The boundary against the documents and mechanisms most often confused with a
Definition of Done.

**Why it exists.** Four neighbors get conflated with the DoD often enough that this bundle's research
treated the boundary as worth a dedicated section rather than a footnote.

*Beginner note, four boundaries in one place:*
- **Definition of Ready** gates the opposite moment: entry into a sprint, not exit from one. It is
  "generally based on the INVEST matrix" and exists so a team can "'push back' on accepting ill-defined
  features" [[7]](#ref-7). Unlike the DoD, it is genuinely contested by name; see
  [section 6](#6-debates-and-contested-boundaries).
- **A quality gate** is an automated, tool-checked pipeline checkpoint: "checkpoints in the software
  development lifecycle... for various criteria such as code coverage, complexity, and security
  vulnerabilities" [[10]](#ref-10). A DoD can include passing a quality gate as one criterion; it is not
  itself a quality gate.
- **Coding conventions** are style and practice guidelines that are "not enforced by compilers"
  [[12]](#ref-12), human-facing rather than checkable completion criteria.
- **"Done done"** is an XP-era emphatic distinguishing true completion from merely "code complete":
  "'Done, done, done' means the feature is 100% ready to deploy to production," where "code complete
  just means that the developers have reached a point where they're ready to turn the code over for
  testing" [[9]](#ref-9). It is the same idea the DoD formalizes, expressed as a phrase rather than a
  document.

*Expert note:* the relationship between a DoD and its neighbors (a quality gate, a coding standard) as
candidate line items inside the DoD, rather than as competing artifacts, is this bundle's own synthesis
from their separate definitions. No source read relates them to each other directly, so treat the
synthesis as reasoning, not as a sourced claim.

### When Work Does Not Meet It *(full variant only)*

**What it is.** What happens to an increment that fails its own Definition of Done.

**Why it exists.** The Guide is direct and leaves no ambiguity: "If a Product Backlog item does not
meet the Definition of Done, it cannot be released or even presented at the Sprint Review. Instead, it
returns to the Product Backlog for future consideration" [[1]](#ref-1). More pointedly still: "Work
cannot be considered part of an Increment unless it meets the Definition of Done" [[1]](#ref-1). Partial
completion is not partial credit, and Agile Alliance's glossary entry carries the same rule stated from
the measurement side: "Failure to meet these criteria at the end of a sprint normally implies that the
work should not be counted toward that sprint's velocity" [[5]](#ref-5).

*Beginner note:* write down where unfinished work actually goes (back to the Product Backlog, per the
Guide) and who decides that it does not meet the bar. This section exists so the consequence is agreed
before the disagreement happens, not during it.

*Expert note:* this is the section most quietly skipped, because a team that has never failed its own
DoD does not feel the need to write down what failing means. That is exactly backwards: the sentence is
cheapest to write before anyone has a stake in the answer.

### Review Trigger

**What it is.** The event that should prompt someone to revisit whether the Definition of Done is still
right, and who notices.

**Why it exists.** This is the one section in the template with no direct source. Every source this
research read that discusses keeping a Definition of Done current reaches for a cadence or a ceremony,
most often the Sprint Retrospective in the superseded 2017 text [[15]](#ref-15), or a general claim that
"The Definition of Done is not static. As the team matures, it expands" [[16]](#ref-16). **No source read supplies a condition, an event that
makes the document wrong, plus a named person who notices.** This family's own contract requires
exactly that, on the reasoning that a standing document fails by drifting quietly out of date while
everyone still believes it is current.

*Beginner note:* name an event, not a date. "Every two weeks" is a calendar reminder and decays into a
ritual nobody reads. "When the team adds a new deployment target" or "when a criterion has been waived
three times" is a condition someone can actually notice and act on.

*Expert note:* the closest thing the literature offers is Scrum Inc's warning in the opposite direction,
that a Definition of Done that never changes "means the team has stopped raising its quality bar"
[[16]](#ref-16). That is a useful pressure but not a trigger: it tells you staleness is possible, not
what event reveals it. Filling that gap with a concrete condition and a named owner is this bundle's own
contribution, not a restatement of received practice.

---

## 4. Variants and sizing

**One format ships, at two sizes**, under this library's rule that a format ships only when it is
structurally distinct and in circulation with a named source. A levelled, three-tier Definition of Done
was considered as a separate format and rejected: it is the same document with a sorting rule for
criteria, not a different outline, and Scrum Alliance is explicit that the sorting rule operates inside
one list [[3]](#ref-3). A Definition of Ready was considered too, and rejected on different grounds: it
genuinely is structurally distinct, gating entry rather than exit, but it is a different document for
the opposite moment and is taught as a boundary rather than folded in (see
[section 6](#6-debates-and-contested-boundaries)).

**Lean carries three sections: Scope and Ownership, Done Criteria, and Review Trigger.** This is the
minimum a team needs to have an honest, usable Definition of Done: who it binds, what it requires, and
what would make it stale.

**Full inserts three more: Criteria by Level, What This Excludes, and When Work Does Not Meet It.**
They are inserted between Done Criteria and Review Trigger, which keeps lean a strict ordered subset of
full's section order.

**The signal to scale up is scope.** This is the bundle's own design guidance; no source read addresses team maturity as a sizing signal. The evidence for two sizes is a direct
comparison: a six or seven item flat checklist scoped to a single team [[6]](#ref-6) and GitLab's
41-item, six-section production gate [[4]](#ref-4) are not the same weight of document, and Scrum
Alliance's sorting rule is what explains why one team's DoD can honestly stay flat while another's
cannot [[3]](#ref-3). Reach for full when the Definition of Done has to gate more than one level
(feature, sprint, and release), when it has neighbors it needs to disclaim explicitly (a team new to
the practice keeps re-litigating the DoR/DoD boundary), or when the cost of an ambiguous "does not meet
it" moment is high enough to be worth writing down in advance. Otherwise lean is not a compromise; it is
the document most teams should actually be running.

**A note on the size call itself.** This library's own master catalog originally listed the Definition
of Done as a single-size type. The research overturned that call: the seven-times variance in real
published examples is not explained by formality, it is explained by scope, and Scrum Alliance
supplies the mechanism [[3]](#ref-3). The size call here is a hypothesis grounded in the evidence
available, not a settled fact, consistent with how this library treats every size call across the
catalog.

---

## 5. Methodology lineage

| School | Treatment | What it optimizes for |
|---|---|---|
| **Scrum canon (2020)** | A commitment attached to the Increment artifact; conformance collective, ownership contingent on an organizational standard [[1]](#ref-1). | Transparency at the moment an increment is claimed complete. |
| **Scrum canon (2017, superseded)** | The same idea, plus an explicit retrospective-adaptation trigger the 2020 text does not carry forward in the passages retrieved [[15]](#ref-15). | The same, with a named mechanism for change. |
| **LeSS (large-scale Scrum)** | One product-level Definition of Done shared by every team, which individual teams may expand locally [[18]](#ref-18). | Consistency of the Increment across many teams building one product. |
| **Nexus (multi-team Scrum)** | Individual teams may apply a **more stringent** local Definition of Done than the shared Integrated Increment DoD, never a less rigorous one, per a secondary account of the Nexus Guide's rule [[22]](#ref-22). | The same integrity goal as LeSS, expressed as a one-directional ratchet. |
| **SAFe** | Its own glossary defines the DoD only thinly, as "the requirements for completeness of a work product or increment of value" [[19]](#ref-19); this research could not confirm from SAFe's own primary text whether it formally names three levels (Team, Program, Solution) or a different number, so that structure is not asserted here. | Completeness at whichever level the artifact sits. |
| **Regulated / safety-critical (medical device)** | A DoD carries compliance weight only when it explicitly incorporates documentation and traceability requirements; it does not confer compliance on its own [[20]](#ref-20). | Auditability, not just delivery quality. |

**On Nexus specifically:** this research could not render the Nexus Guide's own page across three fetch
attempts. The stricter-not-weaker rule is carried here through a secondary practitioner account
[[22]](#ref-22), and this bundle attributes it to that secondary treatment rather than to the Nexus
Guide directly, per the honest-retrieval standard this library holds itself to.

**On SAFe specifically:** aggregator sites assert a formal three- or four-level structure for SAFe's own
Definition of Done, but Scaled Agile's own primary framework text was not confirmed in this research.
The glossary entry that was read supports only its own one-sentence definition [[19]](#ref-19), and this
companion does not repeat the unconfirmed level structure as fact.

---

## 6. Debates and contested boundaries

### 6.1 Should a Definition of Ready exist at all?

This is a real, named disagreement, not a manufactured one. Agile Alliance carries the Definition of
Ready neutrally, as a practice that "avoids beginning work on features that do not have clearly defined
completion criteria, which usually translates into costly back-and-forth discussion or rework"
[[7]](#ref-7). A named practitioner account argues the opposite directly: the Definition of Ready
"conflicts with an Agile way of working" and "incentivizes Waterfall thinking and task completion over
meeting a goal," concluding flatly that it "used to be part of Scrum. But not anymore" [[8]](#ref-8).
Both sources were read in full. This bundle teaches the boundary and reports the dispute rather than
recommending a side.

### 6.2 Who has authority over the Definition of Done?

The Guide places conformance with the Developers and makes authorship contingent on whether an
organizational standard exists; it names no single accountable role [[1]](#ref-1). Roman Pichler frames
the Product Owner as the one who applies the criteria at acceptance and calls the role "the guardian of
quality" [[17]](#ref-17), a framing that reads as more central than the Guide allows. This is a genuine
difference in emphasis between a primary source and a widely read practitioner, and it is the
disagreement most likely to mislead, because the practitioner framing is the one that circulates more.

### 6.3 Is a Definition of Done a flat list or a sectioned document?

Scope-dependent rather than settled. Practitioner story-level checklists are flat and short
[[6]](#ref-6); GitLab's real production gate is sectioned and long [[4]](#ref-4); Scrum Alliance
supplies the sorting rule that explains why both are legitimate [[3]](#ref-3). No source read for this
bundle argues that either shape is wrong in principle.

### 6.4 Does the Retrospective adapt the Definition of Done?

The 2017 Guide says so directly [[15]](#ref-15). Repeated attempts to retrieve an equivalent sentence in
the 2020 Guide's Definition of Done passages did not confirm one [[1]](#ref-1). This is recorded as a
version difference, not a contradiction: absence from the passages retrieved is weaker evidence than
presence in the text actually read, and this bundle does not claim the 2020 Guide rules the practice
out.

### 6.5 A vendor claim this bundle will not repeat

A vendor blog asserts that "research shows" only team-created Definitions of Done correlate with high
performance, while externally imposed ones show no correlation [[14]](#ref-14). No primary study
supporting that claim was found in this research. The source was read; the claim was not traced to
anything that could verify it, and it is recorded here, quarantined, precisely because a reader of this
space will meet it. **It does not appear anywhere else in this bundle as fact.**

### 6.6 Is "encodes activities rather than outcomes" a real failure mode?

Argued in secondary and vendor commentary, and notably absent from the one academic survey in this
literature [[13]](#ref-13). Treat it as a practitioner concern circulating in the field, not as a
finding anyone has measured.

---

## 7. Anti-patterns and failure modes

1. **The undocumented DoD.** 26 of 137 surveyed practitioners reported their Definition of Done was
   "not explicitly documented" [[13]](#ref-13). An unwritten standard is not a lower-cost standard; it
   is a standard nobody can point to when it matters, and Agile Alliance's glossary entry names the same
   failure directly: "Effectiveness diminishes if the definition remains unwritten" [[5]](#ref-5).
2. **The DoD written once and never revisited.** 15 of 137 respondents said their Definition of Done
   "have never been updated" since creation [[13]](#ref-13), and one respondent's own words capture the
   mechanism: "DoD was not documented, unavailable (DoD was established verbally, not written down)"
   [[13]](#ref-13). This is exactly the failure the Review Trigger section exists to prevent (see
   [section 3](#3-anatomy-section-by-section)).
3. **The creeping DoD.** One surveyed practitioner's own description: "DoD was creeping (continuously
   growing in uncontrolled manner)" [[13]](#ref-13). Growth without a sorting rule is how a Definition
   of Done stops being usable at the level it was meant to gate.
4. **DoD written without the people who will be held to it.** In 22 percent of surveyed projects, the
   Definition of Done "were created without involving the developers," which the survey's own authors
   flag as surprising given that "the DoD is used by developers everyday" [[13]](#ref-13).
5. **Nobody cares because nobody was asked.** A related, distinct problem the same survey names
   directly: "Team members did not care about DoD (they omitted some or all DoD items)" [[13]](#ref-13).
6. **DoD theatre.** A checklist that exists but is not read: "A checklist buried in a wiki is a
   checklist nobody reads," and when it is externally imposed, "the rest of the team never feels
   ownership over it, so they treat it as optional" [[14]](#ref-14).
7. **Unverifiable criteria.** Items phrased as impressions rather than checkable states: "'Code is good
   quality' and 'testing done' aren't verifiable" [[14]](#ref-14). This is the mirror image of the good
   practice named in [section 3](#3-anatomy-section-by-section): write states, not activities.
8. **The static DoD, read as a strength.** A Definition of Done that never changes can look like
   stability. Scrum Inc reads it the other way: "A static Definition of Done means the team has stopped
   raising its quality bar" [[16]](#ref-16).

---

## 8. Relationships to other artifacts

- **Sibling, opposite gate: Definition of Ready.** Where the DoD gates exit from work, the DoR gates
  entry into it, and unlike the DoD its existence is itself contested (see
  [section 6](#6-debates-and-contested-boundaries)) [[7]](#ref-7)[[8]](#ref-8).
- **Feeds from below: Acceptance Criteria.** Acceptance criteria state the conditions for one specific
  item; the Definition of Done is the standing floor every item must clear regardless of what its own
  acceptance criteria say. **This bundle corrects an error found elsewhere in this library**: this
  library's own `acceptance-criteria` bundle currently states that "the development team owns the DoD,
  with the Product Owner having final say," citing a Scrum.org page that its own reference entry
  records as never successfully read (HTTP 403). Checked directly against the Guide, that claim does not
  hold: the Guide names no single owner, and "development team" is vocabulary the 2020 rewrite retired
  in favor of "Developers" [[1]](#ref-1). See [section 3](#3-anatomy-section-by-section) and
  [section 6](#6-debates-and-contested-boundaries) for the full picture, including the practitioner
  framing that comes closest to supporting a Product-Owner-centric reading [[17]](#ref-17).
- **Adjacent, automated: the quality gate.** A pipeline checkpoint a machine enforces, which a DoD may
  cite as one of its criteria without being one itself [[10]](#ref-10).
- **Adjacent, stylistic: coding conventions.** Human-facing style guidance, unenforced by a compiler
  [[12]](#ref-12), distinct from the checkable completion criteria a DoD states.
- **Historical cousin: "done done."** The XP-era phrase that carries the same idea the DoD formalizes,
  informally [[9]](#ref-9).
- **Loose, non-standard usage: release-level "DoR/DoD."** At least one vendor source uses "Definition of
  Ready" and "Definition of Done" as labels for stages of a release checklist, a usage distinct from and
  not aligned with the Scrum sprint-item sense of either term [[11]](#ref-11). Flag this when a reader
  meets the labels in a release-management context; they are not the same artifact discussed elsewhere
  in this companion.

---

## 9. Adaptations

- **Multiple teams on one product.** The Guide requires one shared Definition of Done across every team
  building the product [[1]](#ref-1). LeSS operationalizes this as one product-level document that
  individual teams may expand within their own team [[18]](#ref-18). Nexus, per a
  secondary account of its rule, permits the same one-directional tightening: stricter locally, never
  looser than the shared Integrated Increment DoD [[22]](#ref-22). A practitioner articulation of why
  this matters at scale: "A Shared Definition of Done (DoD) creates this clarity by establishing common
  expectations for quality, completeness, and consistency" across teams building one product
  [[21]](#ref-21).
- **Regulated and safety-critical work.** In medical device software, a Definition of Done "leads to
  better and more compliant development documentation" only when it explicitly includes the
  documentation and traceability requirements the regulation demands; the DoD does not confer
  compliance by simply existing [[20]](#ref-20). Treat this as a reason to use the full variant and to
  make the compliance-relevant criteria explicit line items, not an assumption.
- **Team just starting the practice.** Lean is enough. The evidence for scaling up tracks the number of
  levels the DoD actually has to gate (feature, sprint, release), not the seniority or size of the team
  [[3]](#ref-3).
- **Production-grade, single owning team.** GitLab's real, currently shipping engineering DoD is the
  clearest published example of a full-variant document at this scale: 41 items across six labeled
  subsections gating a merge to production [[4]](#ref-4).
- **Small team, story-level scope.** A short, flat checklist is a legitimate, real, and commonly
  published shape, not a lesser version of the sectioned form [[6]](#ref-6).

---

## 10. Worked example pointer

[`definition-of-done_example.md`](definition-of-done_example.md) is the fully worked instance. Per this
family's own contract, a standing standard belongs to a team rather than to a moment in a story, so its
chaining onto this library's running Acme Analytics thread is deliberately lighter than a phase-output
document's would be: it is written as the kind of Definition of Done the `sprint-backlog` and
`acceptance-criteria` examples in this library could plausibly be judged against, not as an artifact one
of those documents produces.

---

## References

Tagged by reliability, following this bundle's own four-way split (its research log records five
primary, three standards, nine practitioner and five vendor sources among those actually read):
`[primary]` the originating or standards-body source itself; `[standards]` a named professional body's
own guidance page, distinct from an originating primary text; `[practitioner]` a recognized independent
authority; `[vendor]` commercially motivated, reliable on convention. Researched 2026-08-06. Retrieval
status per source is recorded in
[`definition-of-done_research-log.md`](definition-of-done_research-log.md); only sources marked
fetched-and-verified there are quoted here.

<a id="ref-1"></a>[1] Ken Schwaber and Jeff Sutherland. "[The Scrum Guide](https://scrumguides.org/scrum-guide.html)" (2020 version). Scrum.org (accessed 2026-08-06). [primary]

<a id="ref-2"></a>[2] Scrum.org. "[Scrum Guide Revisions](https://www.scrumguides.org/revisions.html)." scrumguides.org (accessed 2026-08-06). [primary]

<a id="ref-3"></a>[3] Scrum Alliance. "[What is the Definition of Done?](https://resources.scrumalliance.org/Article/definition-dod)" resources.scrumalliance.org (accessed 2026-08-06). [standards]

<a id="ref-4"></a>[4] GitLab. "[Merge requests workflow](https://docs.gitlab.com/development/contributing/merge_request_workflow/)," Definition of Done section. docs.gitlab.com (accessed 2026-08-06). [practitioner]

<a id="ref-5"></a>[5] Agile Alliance. "[Definition of Done](https://agilealliance.org/glossary/definition-of-done/)," glossary entry. agilealliance.org (accessed 2026-08-06). [practitioner]

<a id="ref-6"></a>[6] Plane. "[Definition of done (DoD): Checklist examples for Agile teams](https://plane.so/blog/definition-of-done-dod-checklist-examples-for-agile-teams)." plane.so blog (accessed 2026-08-06). [vendor]

<a id="ref-7"></a>[7] Agile Alliance. "[What is Definition of Ready?](https://agilealliance.org/glossary/definition-of-ready/)" glossary entry. agilealliance.org (accessed 2026-08-06). [standards]

<a id="ref-8"></a>[8] Willem-Jan Ageling. "[The rise and fall of the Definition of Ready in Scrum](https://medium.com/serious-scrum/the-rise-and-fall-of-the-definition-of-ready-in-scrum-2407c6f1c455)." Serious Scrum, Medium (accessed 2026-08-06). [practitioner]

<a id="ref-9"></a>[9] Jeremy D. Miller. "['Code Complete' is a polite fiction, 'Done, done, done' is the hard truth](https://jeremydmiller.com/2012/12/13/code-complete-is-a-polite-fiction-done-done-done-is-the-hard-truth/)." personal blog, 2012 (accessed 2026-08-06). [practitioner]

<a id="ref-10"></a>[10] SonarSource. "[What are Quality Gates?](https://www.sonarsource.com/resources/library/quality-gate/)" resource library (accessed 2026-08-06). [vendor]

<a id="ref-11"></a>[11] Semaphore. "[Release Management: Definition of Ready and Definition of Done](https://semaphore.io/blog/release-management)." semaphore.io blog (accessed 2026-08-06). [vendor]

<a id="ref-12"></a>[12] Wikipedia contributors. "[Coding conventions](https://en.wikipedia.org/wiki/Coding_conventions)." Wikipedia (accessed 2026-08-06). [standards]

<a id="ref-13"></a>[13] Sylwia Kopczynska, Miroslaw Ochodek, Jakub Piechowiak and Jerzy Nawrocki. "[On the Benefits And Problems Related to Using Definition of Done - A Survey Study](https://arxiv.org/pdf/2208.04003)." Poznan University of Technology; accepted preprint of the paper published in the Journal of Systems and Software, 2022 (accessed 2026-08-06). [primary]

<a id="ref-14"></a>[14] Kollabe. "[Definition of Done Checklist: How High-Performing Teams Use DoD to Ship Better Software](https://kollabe.com/posts/definition-of-done-checklist)." kollabe.com blog (accessed 2026-08-06). Carries one unattributed "research shows" claim this bundle does not repeat; see [section 6](#6-debates-and-contested-boundaries). [vendor]

<a id="ref-15"></a>[15] Ken Schwaber and Jeff Sutherland. "[The Scrum Guide](https://scrumguides.org/scrum-guide-2017.html)" (2017 version, superseded). Scrum.org (accessed 2026-08-06). [primary]

<a id="ref-16"></a>[16] Scrum Inc. "[Definition of Done: The Team's Quality Bar](https://www.scruminc.com/definition-of-done/)." scruminc.com (accessed 2026-08-06). [practitioner]

<a id="ref-17"></a>[17] Roman Pichler. "[Why Product Owners Should Care about Quality](https://www.romanpichler.com/blog/why-product-owners-should-care-about-quality/)." romanpichler.com (accessed 2026-08-06). [practitioner]

<a id="ref-18"></a>[18] Bas Vodde and Craig Larman. "[Definition of Done](https://less.works/less/framework/definition-of-done)," LeSS framework page. less.works (accessed 2026-08-06). [primary]

<a id="ref-19"></a>[19] Scaled Agile, Inc. "[Definition of Done](https://framework.scaledagile.com/blog/glossary_term/definition-of-done)," SAFe glossary entry. framework.scaledagile.com (accessed 2026-08-06). Supports only its own one-sentence definition; SAFe's own primary framework text on any multi-level DoD structure was not confirmed in this research. [vendor]

<a id="ref-20"></a>[20] Johner Institute. "[TIR 45: Agile Software Development for Medical Devices](https://blog.johner-institute.com/iec-62304-medical-software/tir-45-agile-software-development/)," blog post on AAMI TIR45 and IEC 62304. blog.johner-institute.com (accessed 2026-08-06). [practitioner]

<a id="ref-21"></a>[21] Scaling Patterns Library. "[Shared Definition of Done (DoD)](https://scalingpatterns.org/plays/shared-definition-of-done/)," play. scalingpatterns.org (accessed 2026-08-06). [practitioner]

<a id="ref-22"></a>[22] Mirko Perkusich. "[Doing it Right: Definition of Done in Scaled Scrum](https://medium.com/@mirkoperkusich/doing-it-right-definition-of-done-in-scaled-scrum-3e67814a99ea)." Medium (accessed 2026-08-06). Secondary carrier for the Nexus Guide's own rule; scrum.org's Nexus Guide page itself would not render for direct fetch in this research, so the rule is attributed to this secondary treatment, not to the Nexus Guide directly. [practitioner]
