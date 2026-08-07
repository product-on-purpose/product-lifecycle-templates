# incident-postmortem: history

Change log for the `incident-postmortem` bundle. Each entry records what changed and why, so a reader can
tell a correction from a preference.

## 0.1.0 - 2026-08-07

**Initial release.** Researched 2026-08-07 across six parallel dimensions: the SRE canon, structure in
published templates, the attribution of the field's folklore, the root-cause argument, empirical evidence,
and boundaries against adjacent documents.
[`incident-postmortem_research-log.md`](incident-postmortem_research-log.md) records **37 sources**, all 37
`fetched-and-verified`, carrying **139 verbatim quotable phrases**. By tier: 14 vendor, 11 primary, 9
practitioner, 3 standards.

**The second `process-docs` member**, arriving beside `sprint-retrospective-notes` under
[ADR 0033 (the process-docs family contract)](../../docs/internal/decisions/0033-adopt-process-docs-family-contract.md),
which put both here specifically so the postmortem-versus-retrospective distinction could be taught by
contrast: a retrospective looks back on a period, on a cadence, at how the team worked; a postmortem looks
back on an event, triggered by it, at why a specific thing failed.

### "Timeline" is not canon prose, and the count was re-verified independently

A full-text search of the SRE book's own postmortem chapter, the source most people would name if asked
where "timeline" comes from, returns zero occurrences of the word. It exists only as a heading in the
separately linked worked example (Appendix D). This count was re-verified independently by fetching both
pages and counting over the stripped visible text rather than trusting the research pass: chapter 15 says
"timeline" 0 times and "contributing factor" 0 times; Appendix D says "timeline" 3 times and "contributing
factor" once. The same re-count found the research pass's other term counts slightly off in both
directions, which is why only the zeros, robust to how the text is extracted, are used as teaching points.

### No single canonical section set

The canon disagrees with itself: the SRE book's own worked example and the Workbook's two worked examples
use materially different headings. The nine full-variant sections were chosen because each is attested by
the canon's own worked example and at least one published template, not because any single source states
them as a fixed list. The five lean sections, Summary, Impact, Timeline, Root Causes, and Action Items, are
the sections attested across the widest span of the corpus, including Elastic's real, named-organisation
postmortem with no fixed template structure at all.

**The two-size packaging is this bundle's own decision, and it is labelled as such.** All five published
vendor templates read for this bundle are single-size. What the corpus supports is that depth genuinely
varies in practice; this bundle packages that real variation as two sizes and says plainly that no vendor
publishes a named lean/full pair.

### The Action Items section name is a pick, not a convergence

Published templates write the same concept three different ways and never converge: "Action Items"
(PagerDuty, Elastic), "Corrective actions" (Atlassian, GitLab), "Follow-up actions" (incident.io). This
bundle uses the canon's own word and says so. Its most load-bearing rule concerns where the contents live
once the postmortem is finished: two independent practitioner sources agree that action items belong in the
team's existing ticket tracker, not the postmortem document itself, and neither names a risk register as a
destination. This library's own family contract offers the risk register and the RAID log alongside the
product backlog; the companion flags that as this library's own convention rather than received postmortem
practice.

### Contested attributions carried into the bundle, not settled by it

- **"Blameless postmortem" traces to one dated post that does not claim to have coined the phrase.** John
  Allspaw's May 2012 Etsy post is the earliest attributable use this research found. Its canonical URL
  returns HTTP 403 to automated retrieval; this research read it through a full-text mirror and says so.
- **"Just culture" arrives already established in that post, crediting nobody.** A practitioner
  introduction attributes the term to James Reason's aviation-safety work of the late 1990s; Sidney
  Dekker's own author page states no coinage date or origin credit. Recorded as unresolved.
- **Five whys' origin is contested.** Wikipedia credits original creation to Sakichi Toyoda and
  formalisation to Taiichi Ohno; practitioner writing overwhelmingly credits Ohno alone. Ohno's 1988 book
  could not be read directly. Most tellingly, the essay most responsible for making "five whys is
  dangerous" into folklore does not itself trace the technique to Ohno or Toyota anywhere in its own text.
- **The anti-root-cause critique has a founding document and a named lineage that cites itself**, and this
  bundle ships the Root Causes section over that live, unresolved argument rather than resolving it. The
  strongest named defence found concedes it does not recognise the process the critique describes.

### Statistics found and deliberately excluded

Every circulating percentage about what postmortems achieve is untraceable. No controlled or correlational
study linking postmortems to recurrence or MTTR turned up on arXiv, in three years of DORA's own reports,
or in general search. Two figures, a "24 percent reduction in repeat incidents" and a "35 percent mean
incident reduction (SD=18.0 percent), statistically significant," were produced by a search-tool summary
that fabricated a citation rather than reading the source it claimed to summarise; neither appears in the
document it was attributed to. A DORA-attributed 47/64 percent figure does not appear in the DORA report as
retrieved either. None of these appears in the bundle as fact; the fabrication is named in the companion as
its own failure mode because it happened inside research tooling, not inside a human writer's memory.

### No pm-skills pairing

`pairs_with` is declared empty. No skill in `tools/known-skills.txt` addresses incident postmortems or
root-cause analysis; the closest neighbours, the strategy-docs and qa-docs skills, serve a different job.
