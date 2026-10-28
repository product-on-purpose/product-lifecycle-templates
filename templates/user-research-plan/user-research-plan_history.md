# user-research-plan: history

Change log for the `user-research-plan` bundle. Each entry records what changed and why, so a reader can
tell a correction from a preference.

## 0.1.0, reviewed 2026-10-27 - drop the `future:` prefix now that the report is built

**No template change, so `template_version` stays 0.1.0.** `related_templates` named
`future:user-research-report` because the sibling report had not landed. The report (catalog entry 18,
tracked as issue #317) landed 2026-10-27, so the id now exists on disk and the prefix is dropped per
the spec's own closing note (`docs/internal/tier2-specs.md:7372`) and the maintainer's ruling 10 of
2026-10-24. `related_templates` now reads `[user-research-report, user-persona, problem-statement,
design-brief, test-plan, experiment-design-doc]`. `tools/check-bundles.py` check I would otherwise raise
its stale-`future:` failure, since the prefix fails once its target is built.

## 0.1.0 - 2026-10-24

**Initial release, the first founding member of `research-docs` to land.** Researched 2026-10-24 across
six dimensions: government digital services' long-form plans, the library's own neighbours and the Acme
Analytics chain, vendors' and practitioners' short-form plans, the usability block, practice and its
debates, and the standing gap question. [`user-research-plan_research-log.md`](user-research-plan_research-log.md)
records **37 sources, all 37 fetched-and-verified**, with no not-retrieved entry and nothing quarantined.
By tier they are 21 practitioner, 8 vendor, 4 standards, 3 academic and 1 primary. Every quotation was
checked against the source's raw text rather than against a retrieval tool's summary; of 344 quotations
returned across five web-sourced dimensions, 315 passed strict, 9 passed as extraction artifacts, and 20
failed and were corrected or dropped before this release.

### The first of the two founding `research-docs` members

[ADR 0081](../../docs/internal/decisions/0081-adopt-research-docs-family-contract.md) adopted the
`research-docs` family contract on 2026-10-23 with no member built. This bundle and its sibling,
`user-research-report` (catalog entry 18, tracked as issue #317, not yet built), are both founding
members. The contract's section 1 states the membership test this bundle meets: it "plans ... one study
of the people a product serves." It fixes the family's axis at `phase: discover`, labelled the library's
own POSITION because no source argues for a family boundary at this phase, and states the cost directly:
both members serve studies of shipped products too, not only pre-build ones.

This bundle answers the spec written and accepted the day before this release
(`docs/internal/tier2-specs.md:6963-7397`), closed by the maintainer's ten rulings of 2026-10-24
("I approve your ten choices," recorded at `tier2-specs.md:7376-7393`). Catalog entry 210 was corrected from "research plan" to this type's own id and name by PR #315 (the user
research plan becomes catalog entry 210) on 2026-10-23, tracked as issue #316 (bundle: user-research-plan).

### Four shipped examples cite a study this bundle's own example now shows the plan for

The PRD, design brief, epic and internal-announcement examples each cite "Discovery readout: Reporting
friction study, 2026-05" as a document that exists, and until this release no bundle could show it. Per
the contract's section 4 shared-scenario rule, [`user-research-plan_example.md`](user-research-plan_example.md)
chains onto that same study: it is the plan for the 2026-05 Reporting friction study, dated 2026-04-20,
before the sessions run (2026-05-04 to 2026-05-15) and before the study's own report counterpart, which a
later build will show. Every fact this example states about the study, the method, and the participant
count holds against the other worked examples that already cite it; a figure that appears only in a
sibling template's own GOOD or WEAK text is that template's illustration, not a fact of the scenario, and
does not bind this example.

### Two sizes, following the maintainer's ruling against the spec's own uncertainty

The spec rated the plan's sections well evidenced and its two-size split less so, at medium confidence
overall: no source read names a short and a long form of one plan, only different published lengths from
different kinds of publisher (User Interviews' named minimum against digital.gov's and 18F's long forms).
The maintainer ruled on 2026-10-24 to ship `sizes_available: [lean, full]`, `default_size: lean`, as
recommended. The full variant's four added sections, What We Already Know, Roles and Observers, Consent
Privacy and Ethics, and Related Documents, each carry a named source, and the lean seven are a strict
ordered subset of the full eleven, unchanged in name and order, per contract section 3.2.

### The usability block ships at every size, filled in only when the study is a usability test

Tasks and Measures is the clause that makes the alias "usability test plan" true: Nielsen Norman Group
states the identity directly, "When planning a usability test, the research plan is often referred to as
a test plan." For any other method the section is one line naming the method, with the task table and the
two measure lines marked N/A, which is a complete answer and never a placeholder. The maintainer's ruling 4 confirmed one conditional section at
both sizes, as the spec recommended, over a separate usability-only variant.

### The session script, and three terms ruled out by name

The moderator's opening, the consent wording, and the follow-up probes stay out of this plan at every
size and live instead in a linked interview guide (catalog entry 25, an unbuilt candidate), per the
maintainer's ruling 5. Most sources this bundle's research read put that material inside the plan itself;
excluding it is this library's own position, stated in the template's own opening comment rather than
implied as a documented convention.

Three terms the guide rules out by name, so a reader does not reach for this document under the wrong
one: a **test plan** (the separate `test-plan` bundle, which verifies a product increment against a
specification and grades it, where this plan studies how people use a product and records observations);
an **experiment design document** (Itamar Gilad's line, "Per this definition an A/B test is an experiment,
but a usability test is not," carried with his own qualifier that the distinction is not the industry's
common usage); and a **research brief**, a word the research found used for at least three different
senses across the sources read (a stakeholder's request that precedes the plan, the session guide, and a
whole intake document), none of which is this plan. For that last reason, "research brief" is deliberately
excluded from `aliases` below, even though a reader might expect it.

### `pairs_with: []`, by the maintainer's own ruling

`tools/known-skills.txt` carries no research or research-plan skill ID; checked directly on 2026-10-24.
The maintainer's ruling 6 assigns `discover-interview-synthesis` to the report, not the plan, and the
plan ships with no pairing. That ID enters `tools/known-skills.txt` only at the report's landing, so it
is not referenced here.

### `related_templates` carries one `future:` reference, the only one in the library today

`[future:user-research-report, user-persona, problem-statement, design-brief, test-plan,
experiment-design-doc]`, the spec's list. `future:user-research-report` names this bundle's own report
counterpart, not yet built; `tools/meta.schema.json` permits the prefix for exactly this case. Earlier
bundles carried `future:` references until their targets were built, among them `adr` and `rfc`, so this
one is not the first, only the one live today. Per the spec's own closing note (`tier2-specs.md:7372`),
the report's landing PR drops the prefix with a history line of its own, once `tools/check-bundles.py`
can resolve the id on disk. The other five follow the spec: three documents that use research findings,
and `test-plan` and `experiment-design-doc`, the two neighbours whose aliases "test plan" and "A/B test
plan" a reader could mistake for this document. The draft listed `prd`, `product-strategy` and
`product-roadmap` in place of the two neighbours, and the list was restored to the spec's before landing.

### `methodology-agnostic`, against the sources' own UX-research lineage

The sources this bundle draws on are UX research vendors, government digital services, and the ISO/IEC
25062 Common Industry Format lineage that this family's contract names as a trap for the report sibling.
The maintainer's ruling 9 set `methodology-agnostic` for both founding members regardless, matching
`problem-statement` and `design-brief`, this bundle's nearest `discovery-docs` neighbours, rather than
naming a single research methodology this plan requires.
