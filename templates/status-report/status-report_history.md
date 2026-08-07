# status-report: history

Change log for the `status-report` bundle. Each entry records what changed and why, so a reader can tell a
correction from a preference.

## 0.1.0 - 2026-08-07

**Initial release.** Researched 2026-08-07 across six parallel dimensions: whether a standard specifies this
artifact at all, the provenance and definition of RAG status, structure in published templates, the empirical
literature on reporting honesty, boundaries against adjacent documents, and failure modes.
[`status-report_research-log.md`](status-report_research-log.md) records **30 sources, all 30 fetched and
verified**, carrying 143 verbatim quotable phrases. No source in this log sits at `url-confirmed-not-read` or
`not-retrieved`, the first bundle in this library for which that is true.

**The first, and so far only, `communication-docs` member**, the family adopted by
[ADR 0034 (communication-docs family contract)](../../docs/internal/decisions/0034-adopt-communication-docs-family-contract.md).
The contract states plainly that a one-member family is a legal shape and names what would join it: an
executive briefing, a release announcement distinct from `release-notes`, a stakeholder update. This bundle
closes the last entry of the original 25-type catalog floor named in
[`buildout-specs.md`](../../docs/internal/buildout-specs.md), catalog entry 180.

### The defining property: this document owns none of its own facts

Every number in a status report is read from something with more authority, a KPI dashboard, a risk
register, a RAID log, and the template's job is to narrate what those sources mean for one audience in one
period rather than originate anything. That framing is this library's own contribution, not a rule the
research found stated anywhere: the search for an explicit "do not introduce new information" prohibition
came back empty, and the closest analog, PMBOK's chain from raw observations through analysis to a compiled
report, supports compilation rather than a prohibition on invented figures. The companion says so rather than
dressing a library convention as established practice.

Per the family contract's no-new-facts rule, the worked example enforces this literally: it reports on the
**Reporting Platform Modernization** program at Acme Analytics and reads every figure and reference ID from
the `kpi-dashboard`, `risk-register`, `raid-log`, `product-roadmap` and `okrs` examples, plus the
`incident-postmortem` and `definition-of-done` examples for two cited items, all of which already exist and
already agree with each other. The example is dated 28 July 2026 and cites nothing dated after that day. It
also carries one thing going badly, as the contract requires: Time to Insight sits at 18 percent against a
30 percent target and reads amber.

### Only one methodology specifies this document, and a live standard is shown declining to

**PRINCE2's Highlight Report** is the only fully specified status-report artifact this research found, with a
named producer, recipient and cadence: "the highlight report provides a regular update on stage progress,
prepared by the project manager for the project board." The reachable text is a community mirror rather than
AXELOS's own paywalled manual, and the companion says so.

**GovS 002, the UK government's cross-government functional standard for project delivery, was found
deliberately declining to specify one.** It states a principle, that a reporting framework "should be defined
and established to meet the needs of the identified report recipients," and its illustrative list of report
types is charts, not sections. A live, primary, public standard looking at this document type and choosing
not to define it is a stronger finding than silence would have been, and it is recorded as such rather than
read as an absence of evidence.

**PMBOK could not be retrieved, for the second time in this library**, after `business-case`. Nothing in the
bundle rests on it.

### RAG status is used, and its gap is named rather than smoothed over

The UK Infrastructure and Projects Authority's Delivery Confidence Assessment gives the most careful published
Red/Amber/Green scheme this research found, with prose criteria for each colour, and then states outright that
"definitions have only been given for Red, Amber and Green; Amber-Red and Amber-Green can be used to reflect a
status that lies in between." The two intermediate colours, which do the most delicate signalling work on a
five-point scale, are left to judgement even in the most detailed public scheme available. The template does
not invent a threshold the literature does not supply; it requires that whatever threshold a team uses is
written down next to the colour, because a threshold-free colour is one of the two mechanisms the companion
names as the document's actual failure modes.

### The measured honesty gap

This is the one document type in the library whose central weakness has actually been measured, not argued.
Keil, Smith, Iacovou and Thompson's synthesis of a research programme running from 1999 to 2013 reports that,
across a records review of 56 experienced software project managers, "project managers write biased reports
60% of the time and that their bias is more than twice as likely to be optimistic... than pessimistic." The
companion keeps that records-review finding distinct from the same programme's separate 60-student laboratory
study rather than flattening both into one undifferentiated claim. The template's response is structural, not
exhortative: it makes a threshold-free colour and a figure with no source harder to produce, rather than
telling an author to be more honest.

### Boundaries drawn against adjacent document types

The guide adds a comparison table against the two documents a status report is most often confused with. A
KPI dashboard is where a metric is defined; a status report reads a metric from that definition and never
redefines it. A decision paper narrows to the evidence for one ask; a status report that tries to carry every
metric as evidence for a single recommendation produces the decision paralysis a focused ask is meant to
avoid. A problem that has already happened gets its own record in the risk register or RAID log by ID,
referenced here rather than described fresh, so the same fact is never reported twice under two different
names.
