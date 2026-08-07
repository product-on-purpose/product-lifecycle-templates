# Companion: The Incident Postmortem

> The deep explainer for the incident-postmortem bundle. Read this to understand what an incident
> postmortem is, why its section names are not what most teams assume, and where the sources this bundle
> read disagree about it. The short operator card is
> [`incident-postmortem_guide.md`](incident-postmortem_guide.md); a fully worked instance is
> [`incident-postmortem_example.md`](incident-postmortem_example.md). Inline citations like
> [[1]](#ref-1) resolve to the [References](#references) at the bottom, tagged by source reliability.
> This bundle sits in the `process-docs` family alongside `sprint-retrospective-notes`: a retrospective
> looks back on a **period**, on a cadence, at how the team worked; a postmortem looks back on an
> **event**, triggered by it, at why a specific thing failed.

---

## 1. Orientation

A postmortem is **the document a team writes after an incident to explain why it happened and what
will change so it does not happen the same way again.** Its trigger is a decision a team publishes in
advance, not a reaction improvised after the fact: the canon most of this literature traces to states an
explicit list of what should prompt one, *"User-visible downtime or degradation beyond a certain
threshold; Data loss of any kind; On-call engineer intervention (release rollback, rerouting of traffic,
etc.); A resolution time above some threshold; A monitoring failure (which usually implies manual
incident discovery)"* [[1]](#ref-1), and holds that a team should agree those criteria before an
incident rather than argue them during one.

**At a glance**
- The word most people assume is canon prose is actually a heading. A full-text search of the SRE
  book's own postmortem chapter returns zero occurrences of "timeline"; the word exists only as a
  heading in the separately linked worked example [[1]](#ref-1)[[3]](#ref-3).
- There is **no single canonical section set**, because the canon disagrees with itself: the book's
  worked example and the workbook's two worked examples use materially different headings
  [[2]](#ref-2)[[3]](#ref-3).
- The concept everyone calls "action items" is written three different ways across published templates
  and never converges: Action Items, Corrective actions, Follow-up actions
  [[4]](#ref-4)[[5]](#ref-5)[[6]](#ref-6)[[7]](#ref-7).
- Every circulating statistic about what postmortems achieve is untraceable, and two are demonstrably
  fabricated by a search-tool summary rather than present in the documents they claim to summarise
  [[23]](#ref-23)[[24]](#ref-24)[[25]](#ref-25)[[26]](#ref-26)[[30]](#ref-30). No controlled or
  correlational study linking postmortems to recurrence or MTTR turned up on arXiv, in three years of
  DORA's own reports, or in general search [[21]](#ref-21)[[22]](#ref-22)[[27]](#ref-27)[[28]](#ref-28)
  [[29]](#ref-29).
- "Root cause" is argued against by a named, cross-citing community and defended by almost nobody by
  name [[17]](#ref-17)[[19]](#ref-19)[[20]](#ref-20).
- Published practice puts action items in the team's existing ticket tracker, and no source found names
  a risk register as a destination [[35]](#ref-35)[[36]](#ref-36).

**A methodological warning worth stating up front.** Fourteen of this bundle's 37 sources are vendor
tier, and every one of them has a commercial stake in incident practice, whether that is
incident-management software, developer tooling, or ITIL training. Every vendor claim in this companion
says, in the same sentence, who stands to benefit from it being believed.

If you read nothing else: a postmortem is a learning document, not a punishment that follows an outage,
and its section names are borrowed and contested rather than fixed by any single authority.

## 2. Origins and evolution

**The load-bearing source is one Google chapter, and its own companion volume mostly defers to it
rather than repeating it.** The SRE book's "Postmortem Culture: Learning from Failure"
[[1]](#ref-1) states the purpose, the trigger criteria, and a qualitative outcome claim. The Workbook's
follow-up chapter, "Beyond Blameless," is the more likely place a real Google statistic would live and
instead contains only a narrative case example and an explicit pointer back to the first book: *"For a
comprehensive discussion on blameless postmortem philosophy, see Chapter 15 in our first book, Site
Reliability Engineering."* [[2]](#ref-2) The one thing the Workbook adds that the book does not is a
hard requirement tying the document to tracked work: *"To our users, a postmortem without subsequent
action is indistinguishable from no postmortem."* The rule it draws from that is narrower than that sentence
alone suggests: every postmortem following a **user-affecting** outage must carry at least one
associated **bug** at P0 or P1 priority, a priority the source writes as a bracketed alternation rather
than spelling both out. It is a requirement about tracked work, not about the document's own contents, and
it does not apply to every incident of any severity. [[2]](#ref-2)

**"Blameless postmortem" traces to one dated post, and the post itself does not claim to have coined
the phrase.** John Allspaw's May 2012 Etsy post is the earliest attributable use this research found:
*"Having a 'blameless' Post-Mortem process means that engineers whose actions have contributed to an
accident can give a detailed account of: what actions they took at what time, what effects they
observed, expectations they had, assumptions they had made, and their understanding of timeline of
events as they occurred...and that they can give this detailed account without fear of punishment or
retribution."* [[11]](#ref-11) That post's canonical URL returns HTTP 403 to automated retrieval; this
research read it through a full-text mirror, and says so rather than quietly citing the dead link. No
earlier dated use of the phrase was found, so this companion says "earliest attributable use," not
"coined by."

**"Just culture" arrives already established, and its own origin is contested.** Allspaw uses the term
as though it needs no introduction, *"Having a Just Culture means that you're making effort to balance
safety and accountability,"* crediting nobody in the body read [[11]](#ref-11). A practitioner
introduction attributes the term to *"the work on aviation safety by Professor James Reason in the late
90s and early 00s"* [[15]](#ref-15), while Sidney Dekker's own author page, for the book most closely
associated with the phrase today, states no coinage date and credits no origin on the page read
[[16]](#ref-16).

**The anti-root-cause critique has a founding document and a named lineage that cites itself.** Richard
Cook's "How Complex Systems Fail" states the position flatly: *"Post-accident attribution to a 'root
cause' is fundamentally wrong."* [[17]](#ref-17) The critique is carried forward by Cook, Allspaw,
Hollnagel, Woods, Dekker and Leveson, who cite one another and are treated as canon inside resilience
engineering [[17]](#ref-17)[[12]](#ref-12)[[18]](#ref-18)[[19]](#ref-19). Section 6 states plainly that
this is not two evenly matched schools of thought.

**Five whys has a contested origin that practitioner folklore treats as settled.** Wikipedia attributes
original creation to Sakichi Toyoda and formalisation to Taiichi Ohno inside Toyota
[[13]](#ref-13); practitioner writing overwhelmingly credits Ohno alone [[14]](#ref-14). Ohno's 1988
book could not be read directly by this research. Most tellingly, Allspaw's "The Infinite Hows," the
essay most responsible for making "five whys is dangerous" into folklore, does not itself trace the
technique to Ohno or Toyota anywhere in its own text [[12]](#ref-12).

## 3. Anatomy (section by section)

The full variant carries nine sections; the lean variant carries five of them, unchanged in name and
order, so lean is a strict ordered subset of full. Every title below appears in at least one primary
source and at least one published template; none was chosen because it sounded right.

### Summary (lean and full)

**What it is.** A short synopsis of what happened, written before any of the analysis that follows it.

**Why it exists.** Attested by the canon's own worked example and three of the five published templates
read in full [[3]](#ref-3)[[5]](#ref-5)[[6]](#ref-6)[[7]](#ref-7). Even here the canon disagrees with
itself: the Workbook's two worked examples open with a different set of headings again, including
Executive Summary, Problem Summary, Background and Glossary [[2]](#ref-2). This bundle's Summary keeps
the plainer, more widely attested title rather than either Workbook variant.

### Impact (lean and full)

**What it is.** Who and what was affected, and how badly.

**Why it exists.** The most broadly attested section besides Timeline: it appears in the canon's own
example and four of the five published templates read [[3]](#ref-3)[[4]](#ref-4)[[5]](#ref-5)
[[6]](#ref-6)[[9]](#ref-9). A postmortem that skips straight from Summary to Root Causes leaves the
reader unable to judge whether the analysis that follows was worth the time it took to write.

### Detection (full only)

**What it is.** How the incident was discovered: a monitoring alert, an on-call page, a customer
report.

**Why it exists.** Attested by the canon's own worked example and two of the five published templates
[[3]](#ref-3)[[5]](#ref-5)[[6]](#ref-6). It earns full-only weight rather than lean weight because three
of the five templates read fold this content into a combined heading or drop it entirely (PagerDuty,
incident.io and Elastic), so the concept is real but not yet universal enough for the smallest version of
this document.

### Timeline (lean and full)

**What it is.** A chronological account of what happened, in order.

**Why it exists.** Attested as broadly as any title in this research, tying with Impact at the canon's own
example plus four of the five published templates [[3]](#ref-3)[[4]](#ref-4)[[5]](#ref-5)[[6]](#ref-6)
[[7]](#ref-7). It is also this bundle's sharpest teaching point about received wisdom: the SRE book's own
postmortem chapter, the source most people would name if asked where "timeline" comes from, contains
zero occurrences of the word in its prose. It exists only as a heading in the separately linked worked
example [[1]](#ref-1)[[3]](#ref-3). Treat that as a caution about this whole document type: a section
label can be universally assumed to be canon prose and turn out to be a heading in a document most
readers of the canon never open.

### Trigger (full only)

**What it is.** The specific, named criterion that made this event a postmortem rather than an ordinary
day of operations.

**Why it exists.** Attested by the canon's own worked example and one published template
[[3]](#ref-3)[[5]](#ref-5), the narrowest attestation of any section in this bundle, which is why it is
full-only. It also does the most conceptual work of any section here: it is where a team writes down
which of its own agreed-in-advance criteria fired [[1]](#ref-1), rather than leaving readers to infer
after the fact why this event, and not some other bad day, got a document.

### Root Causes (lean and full)

**What it is.** The analysis of contributing causes, plural by design.

**Why it exists.** Attested by the canon's own example and one published template using this exact
title [[3]](#ref-3)[[4]](#ref-4), though the naming varies across the corpus: GitLab titles it "Root
Cause Analysis" [[6]](#ref-6), Elastic titles it "Root Cause," singular [[9]](#ref-9), and Atlassian
splits it into "Root cause identification: The Five Whys" followed by "Root cause"
[[5]](#ref-5). The concept is close to universal, present in four of five templates read
[[4]](#ref-4)[[5]](#ref-5)[[6]](#ref-6)[[9]](#ref-9); this bundle keeps the canon's own plural title.

This is also the one section this bundle ships over a live, named argument that it does not resolve. The
strong position is that there is no root cause at all in a complex system [[17]](#ref-17)[[19]](#ref-19);
GitLab's own template states the sharpest practical version of the same caution directly inside its
guidance: *"A root cause can **never be a person**"* [[6]](#ref-6). Section 6 lays out the argument and
its one named defender; this section exists because four of five published templates carry it and the
canon's own example does [[3]](#ref-3), and it teaches the argument rather than settling it.

### Resolution (full only)

**What it is.** What specifically ended the incident: the technical or operational action taken,
distinct from the Action Items that follow it, which are future work rather than what already happened.

**Why it exists.** Attested by the canon's own example and two published templates
[[3]](#ref-3)[[4]](#ref-4)[[9]](#ref-9). It is full-only because three of the five templates read fold this
content elsewhere: Atlassian calls the equivalent moment "Recovery" [[5]](#ref-5), GitLab folds it into
"Detection & Response" [[6]](#ref-6), and incident.io folds it into its timestamp fields rather than
naming it separately [[7]](#ref-7).

### Lessons Learned (full only)

**What it is.** What the team concludes it should change about how it works, distinct from the specific
technical fix recorded under Resolution and from the concrete tickets recorded under Action Items.

**Why it exists.** Attested by the canon's own worked example, which carries named subsections under
this heading, and one published template [[3]](#ref-3)[[5]](#ref-5). It is full-only on the same logic
as Detection and Resolution: real, but not yet attested widely enough to earn a place in the smallest
version of this document.

### Action Items (lean and full)

**What it is.** Concrete, owned, tracked follow-up work.

**Why it exists.** Attested by the canon's own example and two published templates
[[3]](#ref-3)[[4]](#ref-4)[[9]](#ref-9), but the name itself is this bundle's most visible pick among
several: published templates write it three different ways and never converge, "Action Items"
(PagerDuty [[4]](#ref-4), Elastic [[9]](#ref-9)), "Corrective actions" (Atlassian [[5]](#ref-5), GitLab
[[6]](#ref-6)), and "Follow-up actions" (incident.io [[7]](#ref-7)). This bundle uses the canon's own
word and says plainly that it is a pick, not a convergence. The canon's own worked example shows what a
filled row looks like: *"Plug file descriptor leak in search ranking subsystem | prevent | agoogler |
Bug 5554825 DONE"* [[3]](#ref-3), a specific owner and a specific tracked bug, not a bulleted wish.

The section's most load-bearing rule is about where its contents live once the postmortem is finished.
Two independent practitioner sources say the same thing in nearly the same words: *"The moment the
meeting ends, every item needs a ticket in the same backlog your team already uses for planned work --
Jira, Linear, or whatever tool your sprint planning runs through"* [[35]](#ref-35), and *"Post-mortem
actions must live in your team's existing task management system -- not in the post-mortem document, not
in a separate spreadsheet"* [[36]](#ref-36). ITOC360 states the failure mode most sharply: *"The
postmortem document is where action items are born. It is not where they should live."* [[35]](#ref-35)
Neither source names a risk register or a RAID log as a destination. This library's own family contract
offers those alongside the product backlog; the backlog option is what practice actually describes, and
this companion says plainly that the risk-register and RAID-log routes are this library's own
convention rather than received postmortem practice.

## 4. Variants and sizing

**Lean (five sections)** is Summary, Impact, Timeline, Root Causes, and Action Items. It carries the
sections attested across the widest span of the corpus, and it is the information a reader would still need even
from a one-off, freeform report like Elastic's, which covers Impact, Root Cause, Resolution and Action
Items under its own headings and labels neither a Summary nor a Timeline [[9]](#ref-9).

**Full (nine sections)** adds Detection, Trigger, Resolution, and Lessons Learned, in place. Notice what
the four additions have in common: each is attested by the canon's own example plus at most two
published templates, real content that has not yet converged across the wider corpus the way Summary,
Impact, Timeline, Root Causes and Action Items have.

**The two-size packaging is this bundle's own decision, and it is labelled as such.** All five published
templates read for this bundle are single-size [[4]](#ref-4)[[5]](#ref-5)[[6]](#ref-6)[[7]](#ref-7)
[[9]](#ref-9). What the corpus does support is that depth genuinely varies in practice: incident.io ships
configurable templates and "Dynamic template selection" by incident type or severity [[8]](#ref-8), and
Elastic published a real, named-organisation postmortem with no fixed template structure at all
[[9]](#ref-9). This bundle packages that real variation as two sizes. No vendor publishes a named
lean/full pair, and this document does not imply one does.

**One format, not two.** No source found publishes a second, structurally distinct shape *as a
postmortem*: the corpus varies in section names, not in structure. Elastic's freeform report
[[9]](#ref-9) is a real observation about practice, but it is the absence of a fixed format, not evidence
of a second format alongside this one.

## 5. Methodology lineage

**The SRE lineage is load-bearing.** The book's postmortem chapter [[1]](#ref-1), the Workbook's
follow-up chapter [[2]](#ref-2), and the book's own worked example [[3]](#ref-3) together carry nearly
all of this bundle's structural and definitional content.

**A resilience-engineering lineage runs alongside it as a named critique, not a competing template.**
Cook's founding statement [[17]](#ref-17), Allspaw's direct application of it to postmortem practice
[[12]](#ref-12)[[19]](#ref-19), and Hochstein's symmetry argument, *"It doesn't make sense to ask what
the 'root cause of success' is for an effort like this, because it's a collaboration that requires the
work of many different people to succeed"* [[18]](#ref-18), do not propose an alternative document
shape. They argue about how the Root Causes section, once written, should be read.

**A vendor and practitioner tooling lineage publishes independently, and does not converge.** PagerDuty
[[4]](#ref-4), Atlassian [[5]](#ref-5), GitLab [[6]](#ref-6), and incident.io
[[7]](#ref-7)[[8]](#ref-8) each ship their own named structure, and the naming disagreement documented in
section 3's Action Items entry is the clearest evidence that this lineage has not settled on shared
vocabulary even where it agrees on the underlying concept.

**An ITSM lineage treats the adjacent artifact as a different one.** ITIL's Problem Record *"contains
all details of a Problem, documenting the history of the Problem from detection to closure"*
[[33]](#ref-33), and one ITSM-tradition source uses the words "Postmortem Review" as a single step
inside Problem Management rather than treating the review and the record as the same document
[[34]](#ref-34). A team working inside that tradition should expect this artifact to feed a Problem
Record, not to replace it; section 8 returns to this boundary.

## 6. Debates and contested boundaries

**Is there a single canonical section set?** No. The book's own worked example and the Workbook's two
worked examples use materially different headings [[2]](#ref-2)[[3]](#ref-3). Any claim that "the canon"
has one settled template is not supportable, and this bundle does not make it.

**Should root-cause language be abolished, or used carefully?** The strong position is that there is no
root cause at all in a complex system [[17]](#ref-17)[[19]](#ref-19); a softer position within the same
camp distinguishes live anomaly response from retrospective analysis rather than rejecting the concept
outright [[18]](#ref-18). The critics do not fully agree with each other, and this bundle does not
flatten that into one camp. The clearest **named** defence found is a CTO's blog post conceding *"I
think the criticism is ill considered and I don't really recognize the RCA process they describe, and
then take down,"* while also conceding, *"sometimes you won't find a root cause. It happens."*
[[20]](#ref-20) That the critique's strongest named opponent does not recognise the process being
attacked is itself worth reading as evidence that the argument may be against a careless version of root
cause analysis rather than a disciplined one.

**Who originated five whys?** Wikipedia credits original creation to Sakichi Toyoda and formalisation
inside Toyota to Taiichi Ohno [[13]](#ref-13); practitioner writing overwhelmingly credits Ohno alone
[[14]](#ref-14). Ohno's 1988 book was not readable by this research, so this is recorded unresolved
rather than adjudicated.

**Where does "just culture" come from?** A practitioner introduction credits James Reason's aviation
safety work of the late 1990s [[15]](#ref-15); Sidney Dekker's own author page states no coinage date or
credit chain on the page read [[16]](#ref-16); Allspaw uses the term as already established, crediting
nobody in the body read [[11]](#ref-11).

**Did Allspaw coin "blameless postmortem"?** No source found claims he invented the phrase, and no
earlier dated use turned up in this research [[11]](#ref-11). Absence of an earlier use in this
particular search is not proof none exists, and this companion does not overstate the finding.

**Which GitLab template is actually live?** The public root-cause-analysis issue template in the GitLab
repository was read in full [[6]](#ref-6), but GitLab's own handbook now directs incident leads to a
proprietary settings page inside a vendor product instead of stating headings itself [[10]](#ref-10),
so the public template may be legacy rather than what GitLab teams fill in today.

**Does Elastic's report count as a template at all?** It is a genuinely published post-incident document
from a named organisation, and its heading structure was read verbatim [[9]](#ref-9), but it reads as
one-off and hand-structured rather than reusable, which is why section 4 treats it as evidence of
variation rather than as a sixth fixed template.

**Is a risk register ever a genuine postmortem action destination?** No source found names one
[[35]](#ref-35)[[36]](#ref-36). This library's own family contract offers it alongside the product
backlog and the RAID log. That is flagged here as a convention gap this library is choosing to fill, not
as an error in either the sources or the contract.

**A statistic attributed to DORA that could not be located.** A vendor guide attributes *"47% more
likely to engage in process improvements and 64% more likely to report near-misses"* to DORA's 2021
report [[26]](#ref-26). Neither percentage appears in that report as retrieved [[27]](#ref-27). This is
recorded as unverified rather than fabricated, because the fetch may have been incomplete, which is a
weaker accusation than the two statistics addressed next.

## 7. Anti-patterns and failure modes

**Assuming "the canon" has one settled section set.** It does not; the book's and the Workbook's own
worked examples disagree [[2]](#ref-2)[[3]](#ref-3).

**Assuming "Timeline" is canon prose.** It is a heading in an appendix most readers never open, absent
from the chapter's own prose entirely [[1]](#ref-1)[[3]](#ref-3).

**Citing an unmeasured percentage as though it were a finding.** Every MTTR or recurrence figure this
research chased traced to a headline with no method [[23]](#ref-23)[[24]](#ref-24), a single customer
testimonial [[25]](#ref-25), or a claim absent from the very document it was attributed to
[[26]](#ref-26)[[30]](#ref-30). Two of those figures, a "24 percent reduction in repeat incidents" and a
"35 percent mean incident reduction (SD=18.0 percent), statistically significant," were produced by a
search-tool summary that fabricated a citation rather than reading the source it claimed to summarise
[[26]](#ref-26)[[30]](#ref-30). This is worth naming as its own failure mode: the fabrication happened
inside a research tool, not inside a human writer's memory, and it would have shipped as fact if the
source had not been read in full and checked against the claim.

**Leaving action items inside the postmortem document instead of the team's tracker.** *"The postmortem
document is where action items are born. It is not where they should live."* [[35]](#ref-35) A
postmortem that ends in a bulleted list at the bottom of the page rather than tickets in the tool the
team already uses has produced a wish list, not follow-up work.

**Treating root-cause language as settled science on either side.** The critique is real and
well-evidenced [[17]](#ref-17)[[19]](#ref-19); so is the concern that the critique targets a careless
version of the practice rather than a disciplined one [[20]](#ref-20). Presenting either position as
uncontested misreads the debate this bundle documents in section 6.

**Naming a person as a root cause.** GitLab's own guidance states the rule plainly: *"A root cause can
**never be a person**"* [[6]](#ref-6). A postmortem that lands on an individual has produced blame, not
analysis, and directly contradicts the blameless framing the document type is named for.

**Calling the process blameless while still punishing the people in it.** Allspaw's founding framing
requires that engineers can give their account *"without fear of punishment or retribution"*
[[11]](#ref-11). A process that keeps the blameless label without the practice fails at its own founding
definition, not at some external standard.

**Treating "five whys is dangerous" as settled folklore without reading the argument itself.** Even the
essay most responsible for that reputation does not trace the technique to Ohno or Toyota anywhere in
its own text [[12]](#ref-12); repeating the attribution as though the critique settled it conflates two
separate, unresolved questions.

## 8. Relationships to other artifacts

**Postmortem and sprint retrospective notes.** This is the family's own central teaching point, and it
is stated here directly rather than only implied by the family sitting next to it in the catalog. A
retrospective is cadence-triggered and looks back on a period, at how the team worked; a postmortem is
event-triggered and looks back on one specific thing that failed and why. The clearest named source
drawing this apart is a vendor blog contrasting the two on timing, trigger, participants and output:
sprint retrospectives *"often coming at the end of each sprint, or approximately every 2 weeks,"* with
*"only direct team members ... typically involved"*, against postmortems that follow *"a big milestone,
project or feature"* and produce *"a report for leaders, who may or may not be part of the team
implementing the work"* [[37]](#ref-37). The common real-world error runs both directions: running a
retrospective on an incident produces a blameless discussion of a thing that needed a causal analysis,
and running a postmortem on an ordinary sprint pathologises normal work. If the trigger is a date on the
calendar, reach for `sprint-retrospective-notes`; if the trigger is a specific criterion firing
[[1]](#ref-1), reach for this document.

**Postmortem and incident report.** The only source found drawing this line cleanly is a vendor blog,
not a standard: *"If the incident report answers the question what happened, the postmortem answers why
it happened and what will prevent this from happening again"* [[31]](#ref-31), and, more vividly, *"One
captures reality. The other interprets it. One provides accountability. The other provides
improvement."* [[31]](#ref-31) This bundle's own build spec called this the sharpest distinction it
could make, and this companion says plainly that only one, vendor-tier source draws it this cleanly; no
standards-tier source found does.

**Postmortem and After Action Review.** "After-action review" is a catalog alias for this document
type, and it is worth reading the primary source for what it actually is before assuming the alias is
exact. The US Army's own guide describes it as *"a professional discussion of a training event that
enables Soldiers/units to discover for themselves what happened and develop a strategy for improving
performance"* [[32]](#ref-32), facilitator-led, scoped to a single training event, and explicitly not a
critique: *"Leaders avoid creating the environment of a critique during AARs ... The climate of the
critique, focusing only on what is wrong, prevents candid and open discussion of training events and
stifles learning and team building."* [[32]](#ref-32) The spirit, blameless, structured self-discovery
after a single event, matches this document type closely; the domain, a live facilitated conversation
running 30 minutes to 2 hours [[32]](#ref-32), does not. Treat the alias as directionally right, not
literally interchangeable.

**Postmortem and the ITIL problem record.** These are related but distinct in the ITSM tradition read
for this bundle. A Problem Record *"contains all details of a Problem, documenting the history of the
Problem from detection to closure"* [[33]](#ref-33), and a separate ITSM source treats "Postmortem
Review" as one step conducted inside Problem Management rather than as a synonym for the record itself:
*"Postmortem Review: Teams conduct an open, blame-free review to discuss incidents, root causes, and
responses."* [[34]](#ref-34) A team working inside ITIL should expect this document to feed the Problem
Record, not stand in for it.

**Postmortem and five whys.** Five whys is a technique that can be applied inside the Root Causes
section, not a competing document, and its critique [[12]](#ref-12) is a comment on how root-cause
reasoning is conducted, not on whether a postmortem should exist at all.

## 9. Adaptations

**Teams whose tooling ships configurable or severity-based templates** should read this bundle's two
sizes as their own coarse version of the finer-grained idea incident.io's product already implements,
"Dynamic template selection" by incident type or severity [[8]](#ref-8), not as a discovered industry
standard; section 4 says plainly that no vendor publishes a named lean/full pair.

**Teams operating inside an ITIL or ITSM practice** should treat this document as feeding a Problem
Record rather than replacing it [[33]](#ref-33), and should watch for vendor material that uses
"Postmortem Review" and "Problem Record" as though they were the same artifact when the tradition treats
the review as one step inside a larger process [[34]](#ref-34).

**Teams reaching for five whys as a default technique** should read Allspaw's critique before adopting
it uncritically, particularly the warning that a causal technique can become
*"What-You-Look-For-Is-What-You-Find"* [[12]](#ref-12), and should decide deliberately whether they are
running the named technique or stepping into the wider debate around it.

**Teams under pressure to justify postmortem practice with an ROI figure** should treat every
circulating percentage as an assertion until they trace the method themselves. This bundle's own
research found that pressure produce a fabricated citation even inside automated research tooling
[[26]](#ref-26)[[30]](#ref-30); a human writer under the same pressure is not immune to the same failure.

**Teams tempted to shorten Root Causes to one line because "there is no root cause"** should read the
debate in section 6 rather than treat either side as settled. This bundle ships the section because four
of five published templates and the canon's own example carry one
[[3]](#ref-3)[[4]](#ref-4)[[5]](#ref-5)[[6]](#ref-6)[[9]](#ref-9), not because the philosophical question
is closed.

## 10. Worked example

[`incident-postmortem_example.md`](incident-postmortem_example.md) will demonstrate a full-variant
postmortem analysing an event already modelled elsewhere in this library's Acme Analytics thread, as the
`process-docs` family's shared-scenario rule requires, rather than a newly invented incident. Two things
are worth checking once it exists. First, the trigger it names should be Acme's own published criterion,
not Google's canon list restated as though it were Acme's own [[1]](#ref-1); a team's own agreed
criteria are exactly what section 3's Trigger anatomy asks for. Second, the event it analyses carries no
customer impact, and its actions should still land somewhere this library already models, the risk
register, the RAID log, or the product backlog, with at least one of them left open, owned and dated,
because a postmortem where every action is already closed by the time it is published is not an honest
one.

---

## References

<a id="ref-1"></a>[1] Google SRE (Betsy Beyer et al., eds.). "[Postmortem Culture: Learning from
Failure](https://sre.google/sre-book/postmortem-culture/)." Site Reliability Engineering, ch.15, Google
SRE (accessed 2026-08-07). Supports the trigger-criteria list, the chapter's own purpose statement, and
the verified absence of "timeline" anywhere in its prose. [primary]

<a id="ref-2"></a>[2] Google SRE (Betsy Beyer et al., eds.). "[Postmortem Culture: Beyond
Blameless](https://sre.google/workbook/postmortem-culture/)." The Site Reliability Workbook, ch.10,
Google SRE (accessed 2026-08-07). Supports the P0/P1 action-item requirement, the chapter's deferral to
the book's ch.15, and the Workbook's own differently headed worked examples. [primary]

<a id="ref-3"></a>[3] Google SRE, "[Example
Postmortem](https://sre.google/sre-book/example-postmortem/)." Site Reliability Engineering, Appendix D
(accessed 2026-08-07). Supports the canon's one actual worked template, its exact section headings, and
its Action Items row format. [primary]

<a id="ref-4"></a>[4] PagerDuty, Inc. "[Postmortem
Template](https://postmortems.pagerduty.com/assets/pdf/PostmortemTemplate.pdf)" (PDF, accessed
2026-08-07). Supports the full verbatim section list of PagerDuty's own published postmortem template.
[vendor]

<a id="ref-5"></a>[5] Atlassian. "[A Guide to the Incident Postmortem
Process](https://www.atlassian.com/incident-management/postmortem/templates)." Atlassian (accessed
2026-08-07). Supports the full verbatim, in-order heading list of Atlassian's postmortem template.
[vendor]

<a id="ref-6"></a>[6] GitLab.org. "[GitLab project's public root-cause-analysis issue
template](https://gitlab.com/gitlab-org/gitlab/-/raw/master/.gitlab/issue_templates/rca.md)"
(.gitlab/issue_templates/rca.md, accessed 2026-08-07). Supports GitLab's own actual RCA/postmortem
template as used in the GitLab project itself, including its "root cause can never be a person"
guidance. [vendor]

<a id="ref-7"></a>[7] incident.io. "[Our incident post-mortem
template](https://incident.io/hubs/post-mortem/incident-post-mortem-template)" (hub page, accessed
2026-08-07). Supports the full verbatim, in-order heading list of incident.io's published postmortem
template. [vendor]

<a id="ref-8"></a>[8] incident.io. "[Post-mortem
templates](https://docs.incident.io/post-incident/postmortem-templates)." docs.incident.io (accessed
2026-08-07). Supports incident.io's product-level support for configurable templates and dynamic
template selection by incident type or severity. [vendor]

<a id="ref-9"></a>[9] Elastic. "[Elastic Cloud Incident Report: February 4,
2019](https://www.elastic.co/blog/elastic-cloud-incident-report-feburary-4-2019)." elastic.co blog
(accessed 2026-08-07). Supports a real, named-organisation published post-incident report, used as
evidence that a genuinely published postmortem need not use a fixed reusable template. [practitioner]

<a id="ref-10"></a>[10] GitLab. "[Incident
Review](https://handbook.gitlab.com/handbook/engineering/infrastructure-platforms/incident-review/)."
GitLab handbook (accessed 2026-08-07). Supports that the handbook's own template subsection now directs
incident leads to a proprietary vendor settings page rather than stating headings itself. [vendor]

<a id="ref-11"></a>[11] John Allspaw. "[Blameless PostMortems and a Just
Culture](https://www.etsy.com/codeascraft/blameless-postmortems/)" (canonical URL returns HTTP 403 to
automated fetch; read via full-text mirror at
`https://jaytaylor.com/notes/node/1498058768000.html`). Code as Craft / Etsy Engineering, May 22, 2012
(accessed 2026-08-07). Supports the earliest attributable use of "blameless postmortem" and confirms
Allspaw credits nobody for "just culture" in the body read. [primary]

<a id="ref-12"></a>[12] John Allspaw. "[The Infinite Hows (or, the Dangers Of the Five
Whys)](https://www.kitchensoap.com/2014/11/14/the-infinite-hows-or-the-dangers-of-the-five-whys/)."
Kitchen Soap, November 14, 2014 (accessed 2026-08-07). Supports the direct critique of five whys, the
"What-You-Look-For-Is-What-You-Find" framing, and the verified absence of any Ohno/Toyota attribution in
Allspaw's own text. [primary]

<a id="ref-13"></a>[13] Wikipedia. "[Five whys](https://en.wikipedia.org/wiki/Five_whys)" (accessed
2026-08-07). Supports the attribution of five whys to Sakichi Toyoda's original creation and Taiichi
Ohno's formalisation inside Toyota. [standards]

<a id="ref-14"></a>[14] John Shook, Lean Enterprise Institute. "[Clarifying the '5 Whys'
Problem-Solving Method](https://www.lean.org/the-lean-post/articles/five-whys-animation/)." The Lean
Post (accessed 2026-08-07). Supports the practitioner-side attribution of five whys to Ohno alone via
his machine-breakdown example. [practitioner]

<a id="ref-15"></a>[15] missinfogeek.net. "['Just Culture': an
introduction](https://missinfogeek.net/just-culture-an-introduction/)" (accessed 2026-08-07). Supports
the attribution of "just culture" to James Reason's aviation-safety work of the late 1990s and early
2000s. [practitioner]

<a id="ref-16"></a>[16] Sidney Dekker. "[Just Culture](https://sidneydekker.com/just-culture)" (author
page, accessed 2026-08-07). Supports that Dekker's own site describes his book but states no coinage
date or origin credit on the page read. [primary]

<a id="ref-17"></a>[17] Richard I. Cook. "[How Complex Systems Fail](https://how.complexsystems.fail/)."
Cognitive Technologies Laboratory, University of Chicago, originally 1998 (accessed 2026-08-07). Supports
the founding statement of the anti-root-cause position and the hindsight-bias mechanism behind it.
[primary]

<a id="ref-18"></a>[18] Lorin Hochstein. "[Root cause of failure, root cause of
success](https://surfingcomplexity.blog/2021/08/13/root-cause-of-failure-root-cause-of-success/)."
Surfing Complexity, 2021-08-13 (accessed 2026-08-07). Supports the "root cause of success" symmetry
argument against singling out one failure cause. [practitioner]

<a id="ref-19"></a>[19] John Allspaw (Kitchen Soap, republished on SafetyRisk.net). "[There is no Root
Cause](https://safetyrisk.net/there-is-no-root-cause/)" (accessed 2026-08-07). Supports the "each
necessary, but only jointly sufficient" formulation and the explicit naming of the shared critique's
lineage. [practitioner]

<a id="ref-20"></a>[20] Leon Chism. "[In Defense of The Root Cause Analysis
Process](https://medium.com/@leonc/in-defense-of-the-root-cause-analysis-process-a849c4a9d570)." Medium
(accessed 2026-08-07). Supports the strongest named defence of root-cause analysis found, including its
concession that a root cause is not always findable. [practitioner]

<a id="ref-21"></a>[21] arXiv. "[Failures and Fixes: A Study of Software System Incident
Response](https://arxiv.org/abs/2008.11192)" (2008.11192, accessed 2026-08-07). Supports that the
closest arXiv paper found is a qualitative study of 30 incidents, not a recurrence or MTTR measurement.
[standards]

<a id="ref-22"></a>[22] arXiv. "[Case study of postmortem practices at a national space research
center](https://arxiv.org/pdf/2509.06301)" (2509.06301, accessed 2026-08-07). Supports a qualitative,
interview-based case study of postmortem practice with no recurrence or MTTR quantification. [standards]

<a id="ref-23"></a>[23] Rootly. "[Rootly vs Blameless: Which Cuts MTTR Faster by Up to
40%](https://rootly.com/sre/rootly-vs-blameless-cuts-mttr-faster-up-40-today)" (accessed 2026-08-07).
Supports that the "40 percent MTTR reduction" figure appears only in the title, with no methodology in
the article body. [vendor]

<a id="ref-24"></a>[24] Rootly. "[AI-Generated Postmortems that Cut MTTR by 30% in
Minutes](https://rootly.com/sre/aigenerated-postmortems-cut-mttr-30-minutes)" (accessed 2026-08-07).
Supports that the "30 percent MTTR reduction" figure appears only in the headline, backed by a single
anecdotal comparison rather than a study. [vendor]

<a id="ref-25"></a>[25] incident.io. "[Incident post-mortem software ROI: quantifying MTTR reduction and
engineer time savings](https://incident.io/blog/postmortem-software-roi-calculator)" (accessed
2026-08-07). Supports that the "37 percent faster resolution" figure traces to a single named customer
testimonial, not an independent study. [vendor]

<a id="ref-26"></a>[26] Hyperping. "[Incident post-mortems: the complete, blameless
guide](https://hyperping.com/blog/incident-post-mortem)" (accessed 2026-08-07). Supports that a
"24 percent reduction in repeat incidents" claim attributed to this page by a search-tool summary does
not appear anywhere in the article's full body, and that a DORA-attributed 47/64 percent figure appears
on this page. [vendor]

<a id="ref-27"></a>[27] DORA. "[Accelerate State of DevOps Report
2021](https://dora.dev/research/2021/dora-report/)" (accessed 2026-08-07). Supports that neither the 47
nor the 64 percent figure Hyperping attributes to this report appears in the report as retrieved.
[primary]

<a id="ref-28"></a>[28] DORA. "[Accelerate State of DevOps Report
2023](https://dora.dev/research/2023/dora-report/)" (accessed 2026-08-07). Supports the absence of any
postmortem or post-incident-review measurement in the 2023 edition as retrieved. [primary]

<a id="ref-29"></a>[29] DORA. "[Accelerate State of DevOps Report
2024](https://dora.dev/research/2024/dora-report/)" (accessed 2026-08-07). Supports the absence of any
postmortem-specific finding in the 2024 edition as retrieved. [primary]

<a id="ref-30"></a>[30] Lalith Sriram Datla. "[Postmortem Culture in Practice: What Production Incidents
Taught Us about Reliability in Insurance
Tech](https://ijeret.org/index.php/ijeret/article/download/135/124)." International Journal of Emerging
Research in Engineering and Technology, vol. 3, issue 3, 2022 (accessed 2026-08-07). Supports that a
"35 percent mean incident reduction (SD=18.0 percent), statistically significant" figure attributed to
this paper by a search-tool summary does not appear anywhere in the paper's full ten-page body.
[practitioner]

<a id="ref-31"></a>[31] COEhub. "[Why Both Incident Reports and Postmortems
Matter](https://www.coehub.ai/blog/incident-reports-vs-postmortems)" (accessed 2026-08-07). Supports the
postmortem-versus-incident-report distinction drawn explicitly and by name. [vendor]

<a id="ref-32"></a>[32] US Army Combined Arms Center - Training, Training Management Directorate. "The
Leader's Guide to After-Action Reviews
(AAR)" (`https://pinnacle-leaders.com/wp-content/uploads/2018/02/Leaders_Guide_to_AAR.pdf`), December
2013 (accessed 2026-08-07). Supports what the Army's own primary material prescribes for After Action
Review, including its facilitator-led, non-critique framing and its duration guidance. [primary]

<a id="ref-33"></a>[33] IT Process Wiki (IT Process Maps GbR). "[Problem
Management](https://wiki.en.it-processmaps.com/index.php/Problem_Management)" (ITIL reference, accessed
2026-08-07). Supports the ITIL Problem Record's own definition and purpose. [practitioner]

<a id="ref-34"></a>[34] itil.org.uk (Purple Griffon). "[Incident Management vs Problem
Management](https://www.itil.org.uk/blog/incident-management-vs-problem-management)" (accessed
2026-08-07). Supports that this ITSM-tradition source treats "Postmortem Review" as a step inside Problem
Management rather than as a synonym for the Problem Record. [vendor]

<a id="ref-35"></a>[35] ITOC360. "[Postmortem Action Items: How to Track Them to
Closure](https://www.itoc360.com/postmortem-action-items/)" (accessed 2026-08-07). Supports that action
items belong in the team's existing backlog or ticket tracker, not the postmortem document itself.
[practitioner]

<a id="ref-36"></a>[36] incident.io. "[Why Do Post-Mortem Action Items Fail? How to Make Incident
Follow-Ups Actually Get
Done](https://incident.io/blog/why-do-post-mortem-action-items-fail-how-to-make-incident-follow-ups-actually-get-done)"
(accessed 2026-08-07). Supports a second, independent source corroborating that action items must live
in the team's actual task-management system, explicitly ruling out the postmortem document itself.
[vendor]

<a id="ref-37"></a>[37] Parabol. "[Post-mortems vs Retrospectives: What's the
Difference](https://www.parabol.co/blog/retrospectives-vs-post-mortems/)" (accessed 2026-08-07). Supports
the explicit distinction between postmortem and sprint retrospective on timing, trigger, participants,
and output. [vendor]
