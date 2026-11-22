# design-principles: history

Change log for the `design-principles` bundle. Each entry records what changed and why, so a reader can
tell a correction from a preference.

## 0.1.1 - 2026-11-21 - corrections from a Codex review

**Corrections, not preferences.** A read-only Codex review of the bundle, run after it merged, raised
findings that a Sonnet verifier then checked line by line against the files and the cached sources. The
ones that held are fixed here. Two guidance comments in the template change, so the template is stamped
0.1.1. No section, field or placeholder changes. The example was filled from 0.1.0 and keeps that stamp.

- **The rubric gains a floor.** A 0 on row 6 (conflict), row 8 (owner) or row 10 (Review Trigger owners)
  now fails the set whatever the total. Before this, a set scoring 0 on all three still totalled 16 of
  22 and passed the line at 15. The floor is the library's judgement, like the line.
- **NN/g's position on conflict is stated whole.** The companion, the template's When Principles Conflict
  comment and the research log said the template "takes Brignell's side" and that no source supported
  reading the dispute as one of meaning. NN/g's own passage goes on to say that where two principles
  matter in different contexts, a team should "clearly specify in which contexts one of these principles
  is more important than the other". The guide now states both views, as the spec required, and the
  quotation joins entry [1]'s Quotable lines.
- **Productboard's design prompt is credited for moments of use.** The companion and the template said no
  source read prescribes where a set is cited or the form a citation takes. The cached prompt [11] names
  design reviews and disagreements between designers, and offers "Our principles say [X] over [Y] in this
  case." The written decision line and the reviewer's options stay labelled as the library's additions.
- **Two pages state a reuse licence, not one.** The cached GOV.UK page [13] carries the same Open
  Government Licence v3.0 footer as the NHS page. The guide, the template, the companion and the log are
  corrected.

Findings that held only in part and were judged not to need a change are listed in the pull request.

## 0.1.0, reviewed 2026-11-20 - drop the `future:` prefix now that product principles is built

**No template change, so `template_version` stays 0.1.0.** `related_templates` named
`future:product-principles` because the sibling bundle had not been built. The product principles bundle (catalog
entry 214, issue #360) lands in the same pull request as this entry, so the id exists on disk and the prefix is
dropped. `related_templates` now reads `[product-vision, product-strategy, design-brief, definition-of-done,
user-persona, product-principles]`. `tools/check-bundles.py` check I would otherwise raise its stale-`future:`
failure, since the prefix fails once its target is built.

## 0.1.0 - 2026-11-20

**Initial release.** Admitted by
[ADR 0089 (design principles joins standing-standards as a foundation)](../../docs/internal/decisions/0089-design-principles-joins-standing-standards-as-a-foundation.md),
which the maintainer accepted on 2026-11-14. The spec was written on 2026-11-17 in
[`tier2-specs.md`](../../docs/internal/tier2-specs.md). On 2026-11-20 the maintainer ruled every open choice
as recommended ("ok to all") and asked for this build the same day. Built on 2026-11-20 after a
six-dimension research run covering origins, structure, practice, debates, relationships with neighbouring
documents, and the question of what the first design missed. The build is issue #359 (bundle:
design-principles), and it fills catalog entry 213.
[`design-principles_research-log.md`](design-principles_research-log.md) records **26 sources, all
fetched-and-verified**: 17 practitioner, 4 primary, 4 vendor and 1 reference, a mirror.

**The ninth `standing-standards` member.** It declares `classification: foundation`, the contract's cut for
a standard that decisions are judged against and not an instrument executed under time pressure. ADR 0089
widened the family's membership sentence to admit it: the clause "or what every decision about its product
must honour" is new. Design principles are consulted when a designer or a team chooses between two designs,
which is the moment of action the contract's falsifier asks about.

### One size ships, at medium-high confidence

The bundle ships `lean` only, as the maintainer ruled. NN/g warns that a set of ten or more leads to many
principles being forgotten, and the practitioners the research read recommend three to five. The research
read no source that publishes a fuller and a shorter version of one set. The only condensed forms it found
are a PDF that GitLab links and an NHS poster, and it opened neither, so it says nothing about what they
leave out. The sources that add detail add it per principle, not per document: practice bullets and an
example in GitLab's set, practical actions and further reading in USWDS's. The template does the same. Every
count is a practitioner's heuristic, and none of the sources cites a measurement.

### Most of the structure is this library's position

No source the research read publishes a template for a design principles document. The six sections are
therefore assembled from published sets and method articles, and each says in its comment where it is the
library's own position. Three fields per principle have a source in a published set or in a vendor's prompt:
the statement, the question a reviewer asks and what the principle rules out. Only a vendor's AI prompt asks
for the third. **Two fields are this library's additions.** No set the research read carries a field for what
a principle rests on or for a decision it settled, and the template says that it is asking for more than the
published sets do. The role names in Ownership and Changes and the table form of the Review Trigger are the
library's position too.

### The research found no founding text, and the bundle names no originator

No source read names who first wrote about a team writing its own design principles, or when. The earliest
dated method piece read is Jared Spool's article of 1 March 2011. GOV.UK's set was first published on 3
April 2012, and the research cannot say it was the first public set. NN/g's article of 2 August 2020 is a
definition and method source, not an origin. The practice is described as a convergence of practitioner
writing, and the companion names no originator.

### Where the sources disagree, and what the bundle chose

- **Whether principles may conflict.** NN/g says a principle should not conflict with the others and that
  each should carry one value only. Ben Brignell, who curates principles.design, says real principles reveal
  priorities and that consistency sometimes conflicts with clarity. The two camps may mean different things
  by "conflict". **The template takes Brignell's side**: section 3, When Principles Conflict, names which
  principle wins when two pull apart, and the guide states both views. That is the library's position.
- **Whether to rank a set.** Salesforce stack-ranked its four principles, Atlassian writes each as one thing
  before another, and Jeremy Keith recommends the form "X, even over Y". GOV.UK, the NHS and USWDS publish
  their sets unranked. The template offers the X-over-Y form as a GOOD example and does not require it.
- **Whether generic principles earn a place.** Jay Mistry and a critic of the GOV.UK set say no, and Brad
  Frost says a few do no harm. The template asks what each principle rules out, which is the test Mistry's
  opposite-approach argument implies.
- **Whether a principle is a rule.** GOV.UK says its set is not a rule book, and USWDS calls its set an
  evaluative lens. That is a tension with reading the type as a standard judged against. The library reads
  the phrase as judgement, not mechanical compliance, and says so.

### The line with product principles is the library's, and published sets cross it

[ADR 0090](../../docs/internal/decisions/0090-product-principles-joins-standing-standards-as-a-foundation.md)
admits `product-principles` as a type of its own. The line between the two is the library's working test, at
medium-low confidence: ask what the principle settles. If it settles how an interaction, a message or a
screen behaves for its user, it is a design principle. If it settles what the team builds, funds or
declines, it is a product principle. No source read draws that line in so many words. One of NN/g's own
example principles and USWDS's principle on earning trust both cross it, and Pajamas' two kinds of
principles are a split between process and output, which is a different line. The guide says some
principles will straddle, and the worked example marks one that does.

**The bundle never uses NN/g's own longer name for the type.** It begins with the word "product" and so
collides with the sibling bundle. The aliases are "UX design principles" and "experience principles", as
the maintainer ruled.

### The staleness mechanism is a Review Trigger with conditions, and no interval is sourced

The family contract forbids a calendar reminder as the only trigger. No source read states a revision
interval. GOV.UK's update history has three entries across thirteen years, a set kept for years and changed
on an event, and the NHS page carries an update date of April 2023. Both show a set kept for years, and
neither says how often it changed. Reading that as "changed deliberately and rarely" is this library's
inference at low to medium confidence. No cadence tension of the kind ADR 0088 recorded for the support
matrix arose, so the `foundation` classification stands. The Review Trigger carries five conditions, and the
template labels which are sourced and which are the library's own synthesis:

- A new cross-cutting concern with people behind it, from GOV.UK's 2025 working group.
- An audit that finds principles overlapping or forgotten, from Spotify's audit of its own set and NN/g's
  warning about forgotten principles.
- A new product or surface joining the scope, from Spool's question about whether a principle has been
  evaluated for the project.
- A recurring debate that no principle settles, which is the library's own synthesis.
- A change of audience or strategy, which the spec lists and no source states.

### What the gap question added

The gap dimension did not read the spec or this bundle's files before searching. It surfaced six candidates,
and each was routed as a candidate and not an obligation:

- A priority order, or a trade-off written into each statement, went to section 3.
- The research a principle rests on became an optional field in section 2.
- A worked case in which the principle decided something became a field in section 2.
- A scope statement went to section 1, Purpose and Scope.
- A change process and a dated record gave section 5 a change log.
- A reversal test, or what a principle rules out, became a field in section 2 and a row in the guide's
  rubric.

### Verified before drafting

**Every quotation was checked against raw text**, never against a retrieval tool's summary. Of the 120
quotations the research agents returned, 116 passed the first check, five of them only after markup was
stripped. Two failures, both from slides by Alla Kholmatova, are not used. The main loop also carried in
quotations from the admission sweep and from the spec's own reads, and each was re-tested against the cached
raw body, so 163 quotations stand in the log's entries.

**Pages the research could not read are quarantined.** Atlassian's own principles pages returned a script
redirect and then a sign-in page, so its set is read only through the principles.design mirror. Two other
essays returned HTTP 403, and the principles.design field guide is a paid PDF past its sales page, so
nothing is said about its contents. No claim or quotation in the bundle rests on any of them, and the log
lists them under pages not read.

**Licences.** The NHS page is the only one read that states a reuse licence, the Open Government Licence
v3.0. Productboard's prompt reserves its rights. **The bundle describes the structures it found and copies
no set's text.**

### Pairing

`pairs_with` is empty. `tools/known-skills.txt` holds no skill for design principles, which a read of that
file on 2026-11-20 confirmed. An empty list is the legal answer, and the pairing stays unclaimed until a
skill exists that addresses this document.

### The example, and the stop rule it was built under

The worked example is the design principles document for Acme Analytics' own product, at `lean` size,
paired in intent with the later `product-principles` example so that a reader can see an experience
principle and a product trade-off for one product. It is owned by Marcus Webb, the design lead named in the
Saved Views design brief, and approved by Dana Okoro, VP Product. It holds three principles, one conflict
resolved in a named kind of decision, a change log with a first version and one revision, and a Review
Trigger row that fired once. It is dated inside FY26, cites only documents that existed by its last change,
and labels every figure illustrative. It was built under the stop rule ADR 0064 and ADR 0074 record: if the
filled principles read as slogans that no design decision could break, the build would stop and the
decision would return to the maintainer.

### What the research did not settle

- Who started the practice, and when.
- How many principles is right. Every figure is a heuristic.
- That any field beyond a statement is standard practice.
- That keeping such a document improves outcomes. No source measures it.
- How the template behaves for a solo practitioner or a regulated product. The research found no source on
  either, so the template is untested for both.
