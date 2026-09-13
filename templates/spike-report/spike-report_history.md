# History: Spike Report bundle

Per-bundle changelog, by `template_version`. Newest first.

## 0.1.0 - 2026-09-12

- Initial spike-report bundle. Fourth bundle in the `decision-docs` family, joining `adr`, `rfc` and
  `sdd` with no contract change, exactly as
  [ADR 0022 (adopt the decision-docs family contract)](../../docs/internal/decisions/0022-adopt-decision-docs-family-contract.md)
  anticipated in its own Consequences. Catalog entry 67, `spike-research-spike-report`. The fourth role
  is **investigates**: an RFC proposes a technical decision, an ADR records one, an SDD describes the
  design that implements it, and a spike report investigates the question that precedes all three.
- **Admitted on exactly one named source, and that is the defining fact about this bundle.** Researched
  2026-09-11 across six dimensions; the verdict was neither the clean pass the build order had assumed
  nor the clean failure `prototype-brief` produced. Exactly one source publishes a spike report as a
  written document: Microsoft's Code with Engineering Playbook, which states the deliverable "should be
  a document" and ships a fill-in template, both read from the raw markdown in its repository rather
  than from a rendered page. **The term's own inventors publish the opposite** - Ward Cunningham's c2
  account, crediting Kent Beck, describes the output as throwaway **code**, and Mike Cohn describes an
  activity, not an artifact. The reading that admits the type anyway is
  [ADR 0048 (one named source clears the admission test)](../../docs/internal/decisions/0048-one-named-source-clears-the-admission-test.md):
  [ADR 0030 (templating scope is Markdown documents)](../../docs/internal/decisions/0030-templating-scope-markdown-documents.md)
  says "a named source", singular, and one is therefore enough. Full evidence:
  [`spike-report-admission-evidence.md`](../../docs/internal/spike-report-admission-evidence.md).
- **The four-lens review found two fabricated quotations in the first draft, and that is recorded here
  rather than quietly fixed.** Both were in the companion, both read entirely plausibly, and both cited a
  real source that does not contain them: two sentences attributed to Mike Cohn about a time box being a
  fixed investment with a checkpoint at the end, and one attributed to Don Wells about reducing risk and
  improving estimate reliability. Neither string appears anywhere in the research log. The Cohn reference
  also carried an invented publication date and an invented one-line description. All were **deleted**
  rather than re-sourced, per this library's fix rule: searching for a source that supports a sentence
  already written is how a fabrication acquires a footnote. Where the point was worth keeping it is now
  labelled as this bundle's own recommendation, argued in companion section 9, rather than as practice
  anyone read.
- **Four further claims were corrected for overstating what the log carries**: a count of filled spike
  reports given as "roughly fourteen" when the research read 14 documents of which **11** were spike
  reports (the log now records both figures); a time-box line credited to Ron Jeffries individually when
  the c2 page is signed by five contributors; a gloss of Katy Mulvey's position quoted as her words when
  it was the researcher's paraphrase; and an eight-section list attributed to the paired pm-skills skill's
  output template, which no logged source describes. The last was deleted outright rather than trimmed.
- **The obligation that came with the admission: teach the dispute, do not resolve it.** ADR 0048 states
  it in those terms, and no other bundle in this library carries it. Every file here says plainly that
  writing up a spike is contested rather than settled practice: the template's preamble, companion
  sections 1, 2 and 6.1, the opening of the guide's "When to use", and the example's own header note. A
  sentence presenting "write up your spike" as received practice would have been a claim this evidence
  does not support, which is the defect class this library's reviews exist to catch.
- **Two departures from the spec, both forced by the research**, recorded here rather than quietly
  absorbed. The spec in [`tier2-specs.md`](../../docs/internal/tier2-specs.md) was written before the
  research pass and said outright it expected to be wrong somewhere. These are where.
  1. **`Time Box` does not ship as its own section. It is folded into `Scope and Time Box`.** The spec
     made it one of six, calling it the section that distinguishes a spike from open exploration and the
     one most likely to be quietly dropped. The structure dimension found the opposite of what that
     assumed: a dedicated time-box heading belongs to **pre-spike planning** artifacts, a Jira ticket's
     time-box field and a spike *plan*'s "Deadline", and is usually **absent** from the report of a
     completed spike. Folded into Scope, where the evidence puts it, the box is still recorded, allotted
     and actually spent, and the scope boundary it produced sits next to it.
  2. **`What This Does Not Settle` is retained, and it was defended rather than assumed.** The spec
     flagged it as a deliberate departure from the paired skill's four-part shape (question, approach,
     findings, recommendation) and said it should be defended or dropped on evidence like any other
     section. The blinded gap dimension, which never saw the spec's section table, found an explicit
     non-scope statement to be the single most consistent element real filled spike reports supply and a
     naive four-part shape omits, present under four different headings across four unrelated projects,
     while the structure dimension found that **not one blank template asks for it**. Every template
     omits it; the good filled reports include it anyway.
- **The three caveats on that gap finding travel with it everywhere, and are not decoration.** The
  filled corpus was **selected** by structural search, GitHub code search for `## Findings` and
  `# Spike:` headers, so it pre-selects for reports that already have structure; a large share of it
  shows signs of **agent-assisted or agent-authored** drafting, which makes a recurring element weaker
  evidence about human practice than a raw count suggests; and it mixes **three genres**, human blank
  templates, AI-coding-agent workflow templates, and filled examples, that should not be pooled into one
  frequency count. The finding is a good reason to include the section. It is not a measurement of human
  practice, and companion section 6.4 exists so nobody quotes it as one.
- **Recommendation is retained against the admitting source's own guidance, deliberately.** Microsoft's
  playbook states that "The goal of a spike should be fact-finding, not decision-making or
  recommendation", and this template makes Recommendation a required section anyway, on the practice:
  GitLab asks its engineers for "recommended path(s)" in the same breath as the learnings, and the
  filled reports read for this bundle carry explicit verdicts. Companion section 6.2 carries both sides
  and names the cost, which is the drift this document type is most prone to: a Recommendation section
  makes it easy to write the verdict first and let the evidence sections shrink into a preamble
  justifying it. The mitigation is structural rather than rhetorical, and it is why `What Was Tried`
  must be reproducible and `What Was Found` must separate facts from implications.
- **Single-size, `sizes_available: [lean]`, and for once the spec and the research agree.** No source
  read publishes two weights of a spike report, and the one named source that publishes the document at
  all ships exactly one template. The variation that does exist in the wild is across **genre**, not
  weight. Single-size members of this family are exempt from the nesting rule and from nothing else.
- **`methodology: agile`, the first non-generic declaration in `decision-docs`.** The other three members
  are `generic`, because an RFC, an ADR and a design doc are methodology-agnostic instruments; a spike is
  genuinely an XP practice. The
  [family contract](../../docs/internal/contracts/decision-docs.md) anticipated exactly this and permits
  it: methodology is "descriptive, not gated", and "a future member is free to declare otherwise rather
  than have the truth bent to a rule".
- **`pairs_with: [develop-spike-summary]`**, verified present at `skills/develop-spike-summary/SKILL.md`
  in product-on-purpose/pm-skills on 2026-09-11 and pinned in `tools/known-skills.txt`. The boundary
  against the ADR is the skill's own claim rather than this library's: "For the architecture decision
  the spike informs, use `develop-adr` instead." **A spike report that recommends without recording what
  was tried is a bad ADR; an ADR that shows its working is not a spike report.**
- **Worked example is deliberately independent of its siblings**, per the family contract's distinct-jobs
  rule: a four-day firmware investigation at a fictional water-quality monitoring operator, with every
  figure, version, identifier and date labelled illustrative. It does not extend the `adr`, `rfc` or
  `sdd` examples, because this family teaches the distinction between the roles rather than one thread
  running through them.
- Researched 2026-09-11. [`spike-report_research-log.md`](spike-report_research-log.md) records
  **72 unique sources**, of which **61 fetched-and-verified**, **5 url-confirmed-not-read** and
  **6 not-retrieved**. Only fetched-and-verified sources are quoted anywhere in this bundle. Two fidelity
  notes are recorded there: em-dashes and en-dashes inside quoted source material are normalised to
  hyphens, because this repository's gate forbids them in any tracked file, and one quoted excerpt that
  carried a relative Markdown link into its own repository is rendered as plain text.
- Status: `beta`. Gate-green, with zero real usage by anyone other than the author, per the family
  contract's own rule that `beta` holds until one real usage cycle is recorded.
