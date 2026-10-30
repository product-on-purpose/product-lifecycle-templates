# Build backlog: where it lives, what is outstanding, and what comes next

**This page is a dated snapshot, taken 2026-10-20 and refreshed 2026-10-29 and 2026-10-30.** The issue counts in section 2 were
read from GitHub on 2026-10-30, and no gate checks them, so they go stale as issues move. The catalog
counts in section 3 sit under a counts marker that [`tools/check-counts.py`](../../tools/check-counts.py)
gates, so CI fails when they drift.
[`STATE.md`](../../STATE.md) outranks this page wherever the two disagree.

Section 7 says when to revisit this page. The Define re-score that
[ADR 0077](decisions/0077-define-ends-with-a-chosen-concept.md) (define ends with a chosen concept) and
[ADR 0078](decisions/0078-maps-canvases-and-session-records-are-templatable-through-their-written-form.md)
(maps, canvases and session records are templatable) called for ran on 2026-10-20. Sections 2, 4, 5 and 6
reflect it. Its digest is held locally, at `_local/research/2026-10-20_define-rescore/digest.md`.

## 1. Where the backlog lives

No single list holds the backlog. Three places hold parts of it, and each one lacks something the others have.

| Place | What it holds | What it lacks |
|---|---|---|
| [GitHub issues labelled `build-candidate`](https://github.com/product-on-purpose/product-lifecycle-templates/issues?q=is%3Aissue+is%3Aopen+label%3Abuild-candidate) | The working backlog: every type someone has proposed to build, labelled by status, priority, tier, family and axis. Closed issues record the types built or declined | Any type nobody has proposed. Issue #180 (the ranking, and what would be refused) carries the label but is a discussion, not a candidate |
| [`catalog.md`](catalog.md), rendered from `atlas/catalog-data.json` into the atlas | All 210 types the library's research found, each with a tier and a build state | A priority field. It also has no "declined" state, so a type declined by record still reads "candidate" there |
| The [Progress table](tier2-specs.md#progress) in `tier2-specs.md` | Every type assessed or specced beyond its catalog row, with its status and the record behind it | The types nobody has assessed yet |

**Only the issues carry a priority.** The catalog has tiers, and the build order among unproposed types is the
maintainer's own preference, by [ADR 0041](decisions/0041-maintainer-preference-sets-the-build-order.md).

**When an issue body and its labels disagree, the labels are current.** An issue body is written once, when
the issue opens. The `messaging-framework` issue still says "an admission sweep" is next, but sweep 6 has since
run and its label now reads `status:parked`.

## 2. The working backlog: the open candidates

| Issue | Type | Status | Priority | Tier | Family and axis | Next action |
|---|---|---|---|---|---|---|
| [#298](https://github.com/product-on-purpose/product-lifecycle-templates/issues/298) | `opportunity-statement` | Parked by the maintainer 2026-10-22, after its admission sweep | P3 | 2 | Unassigned; labelled `phase:define` | None while parked. The sweep found it distinct only in Jeff Gothelf's net-new sense, on one formula, and `problem-statement`'s guide now covers that case. A template with sections for it would reopen the question |
| [#312](https://github.com/product-on-purpose/product-lifecycle-templates/issues/312) | `product-opportunity-assessment` | Candidate, opened 2026-10-22 | P3 | 2 | Unassigned; labelled `phase:discover` | An admission sweep; its boundary with `business-case` is untested |
| [#261](https://github.com/product-on-purpose/product-lifecycle-templates/issues/261) | `requirements-traceability-matrix` | Candidate | P3 | 3 | Unassigned; `qa-docs` does not cleanly admit it | An admission sweep |
| [#329](https://github.com/product-on-purpose/product-lifecycle-templates/issues/329) | `manager-user-guide` | Candidate, opened 2026-10-27 from the 2026-10-23 resource crawl | P3 | None; no catalog row | Unassigned | An admission sweep |
| [#330](https://github.com/product-on-purpose/product-lifecycle-templates/issues/330) | `lean-ux-canvas` | Candidate, opened 2026-10-27; raised to P2 by the maintainer on 2026-10-30, who chose to include it after admission sweep 7 recommended a decline | P2 | None; entry 211 arrives with the build | `discovery-docs`, `phase: discover`, by [ADR 0082](decisions/0082-lean-ux-canvas-joins-discovery-docs-at-discover.md) | ADR 0082 accepted 2026-10-30. Next: the spec's choices C1 to C7 in [`tier2-specs.md`](tier2-specs.md#discovery-docs-sixth-member-at-discover-the-lean-ux-canvas) |
| [#337](https://github.com/product-on-purpose/product-lifecycle-templates/issues/337) | `lean-canvas` | Candidate, opened 2026-10-30 by the maintainer's choice to include it | P2 | 2 | `strategy-docs`, `classification: utility`, by [ADR 0083](decisions/0083-lean-canvas-joins-strategy-docs-as-a-seventh-member.md) | ADR 0083 accepted 2026-10-30. Next: the spec's choices D1 to D7 in [`tier2-specs.md`](tier2-specs.md#strategy-docs-seventh-member-by-amendment-the-lean-canvas) |
| [#331](https://github.com/product-on-purpose/product-lifecycle-templates/issues/331) | `product-discovery-plan` | Candidate, opened 2026-10-27 from the 2026-10-23 resource crawl | P3 | None; no catalog row | Unassigned; labelled `phase:discover` | An admission sweep |
| [#257](https://github.com/product-on-purpose/product-lifecycle-templates/issues/257) | `metric-tree` | Parked | P3 | 2 | Unassigned; a classification, never a phase, by the re-score | An admission re-test under ADR 0078 (see section 4) |
| [#258](https://github.com/product-on-purpose/product-lifecycle-templates/issues/258) | `messaging-framework` | Parked | P3 | 2 | Unassigned; neither candidate family admits it as written | None while its placement is held under [decision procedure 10](decision-procedures.md#10-a-family-or-axis-assignment-is-uncertain) |
| [#264](https://github.com/product-on-purpose/product-lifecycle-templates/issues/264) | `concept-test-validation-brief` | Parked by the maintainer 2026-10-06 | P4 | 2 | Unassigned; `discovery-docs` admits it as written | None while parked |

| Count by | Result |
|---|---|
| Status | 6 candidates, 4 parked |
| Priority | P2: 2, P3: 7, P4: 1 |
| Tier | Tier 2: 6, Tier 3: 1, no catalog row: 3 |

Sixty candidate issues are closed: 52 built and 8 declined. The last to close was #317 (user-research-report). Two of the declined types,
`solution-brief` and `prototype-brief`, never had a catalog row.

**Format candidates for a built bundle's next revision.** *(Recorded 2026-10-26.)* The library's 2026-10-23
resource crawl found three documents that fail the distinctness test as new types and would ship instead as
formats of built bundles, under [ADR 0028](decisions/0028-adopt-a-format-axis.md). The maintainer chose on
2026-10-25 to note them here rather than sweep them now, because no revision of those bundles is open.

| Format candidate | Named source | Would become a format of |
|---|---|---|
| Test Card | Strategyzer | `experiment-design-doc` |
| Learning Card | Strategyzer | `experiment-readout` |
| Problem Roadmap | Melissa Perri | `product-roadmap` |

Each still needs its own check, when its bundle is next revised, that a structurally distinct form of it
is in circulation.

## 3. The catalog by tier

<!-- counts: statebuilt=52, statecandidate=156, stateoutofscope=2, tier1=25, tier1remaining=2 -->

The catalog holds 210 types. Its `state` field reads 52 built, 156 candidate and 2 out of scope. Four of the
156 were declined by record, so 152 types are still open.

| Tier | Types | Built | Declined or out of scope | Still open |
|---|---|---|---|---|
| 1 | 27 | 25 | 2: `wireframe` and `interactive-prototype`, out of scope by [ADR 0030](decisions/0030-templating-scope-markdown-documents.md) | **0** |
| 2 | 156 | 27 | 4, declined by record (below) | **125** |
| 3 | 27 | 0 | 0 | **27** |
| **All** | **210** | **52** | **6** | **152** |

The four Tier 2 types declined by record are `pi-release-retrospective`
([ADR 0049](decisions/0049-pi-release-retrospective-fails-the-admission-test.md)), `deployment-plan`
([ADR 0064](decisions/0064-deployment-plan-is-declined.md)), the steering committee pack
([ADR 0065](decisions/0065-steering-committee-pack-is-declined.md)), and the per-feature analytics
measurement plan ([ADR 0074](decisions/0074-analytics-requirements-measurement-plan-per-feature-is-declined.md)).
The last was declined in its per-feature reading only, and its business-scope reading has not been swept.

**Most of the open types have never been proposed.** They have no issue, so they have no priority either.

## 4. The define phase

| Layer | Count | Which |
|---|---|---|
| Built bundles with `phase: define` | 2 | `problem-statement`; `design-brief`, built 2026-10-22 (#294) |
| Open issues labelled `phase:define` | 1 | `opportunity-statement` (#298), parked |
| Candidates one read could still move | 7 | Listed in the re-score table below |

**The re-score replaced the planning estimate with a count.** This page previously said "roughly 60"
candidates awaited the re-score. The re-score enumerated 62 from the three Define research sweeps' files by
script, and added five types by name: `business-case`, `trade-study`, `metric-tree` (#257),
`concept-test-validation-brief` (#264) and `opportunity-statement` (#298). Two of the 67 rows are one type
scored under two names (the research synthesis and the diary or field-study synthesis), so 66 distinct types
were tested. Three Sonnet scorers tested one sweep each, against the
[`discovery-docs` 0.4.0](contracts/discovery-docs.md) section 2 define rule. A Sonnet critic reviewed all
three, and the main loop checked the critic's blocking findings against the sources.

| Re-score outcome, 2026-10-20 | Count | Candidates |
|---|---|---|
| Returns for an admission sweep at `define` | 2 | `design-brief` (#294), in the Design Council's sense; `opportunity-statement` (#298) |
| Returns for an admission sweep elsewhere | 4 | `metric-tree` (as a classification, never a phase); design principles (`foundation`); the DMAIC project charter (which points at the unbuilt `project-charter`); GDPR records of processing activities (a standing instrument) |
| Evidence insufficient: one read would settle it | 7 | NASA's needs, goals and objectives statement with its concept of operations; a platform and device support matrix; the DoD Initial Capabilities Document; the proto-persona; an accessibility conformance target; a regulatory requirements register; the "Target" phase of the Behavioural Insights Team's TEST method |
| Already decided | 6 | `problem-statement` (built, `define`); `business-case` (stays `discover`); `trade-study` (stays `develop`); the point of view statement (an alias of `problem-statement`, sitting item D6); `user-persona` (stays `discover`); `concept-test-validation-brief` (parked by the maintainer) |
| Stays out of `define` | 48 | Every other candidate, among them `lean-canvas`, `opportunity-solution-tree`, the Shape Up pitch and LEGO's Foundation Document |

**"Stays out" means out of `define`, not out of the library.** *(Added 2026-10-30.)* The re-score tested
every candidate against the `define` rule only. Its brief offered an "other-admission" outcome for a type that
passes admission but belongs elsewhere, and four candidates received it. Eighteen of the 48 rows that stay out
of `define` passed admission and were never tested in another family. They include the competitive analysis, the
threat model, the data protection impact assessment, the accessibility conformance report, the market
requirements document and `lean-canvas`. Each keeps `state: candidate` in the catalog. The score files are held
locally, at `_local/research/2026-10-20_define-rescore/`.

**The design brief returns in the Design Council's sense only, with medium confidence.** The Design Council
names a design brief as Define's result, one "which clearly defines the challenge", and that document clears
the rule. Peter Phillips's wider commissioning brief does not fit as cleanly. He calls it "a written
agreement, or contract, between the parties", which reads as the project authorization the rule excludes. He
also counts a design strategy among its most critical sections. That can read as `develop`, though the reading
is contested, because design-management usage can mean how design serves business objectives. The admission
sweep must draw that line, possibly as a lean concept-handoff variant beside a full commissioning variant.
*(Settled 2026-10-22: the sweep drew the line at the concept handoff, ADR 0079 admitted that sense alone, in a
lean and a full size, and the bundle was built the same day. Phillips's commissioning brief stays unbuilt.)*

**The opportunity statement returns with one open question, at medium confidence.** It passes the rule on the
sources `problem-statement` already logs. One of those sources says the two are "written and used in the same
way", so its admission sweep must show that the types are distinct, or decline it as a duplicate.
*(Settled 2026-10-22: the sweep found them distinct only in Jeff Gothelf's net-new sense, on one formula,
and the maintainer parked the type. See section 5.)*

**`business-case` stays at `discover`, with high confidence.** Its defining job is deciding whether an
investment is worth making, and the define rule says in so many words that a define document "decides no
investment". Moving it would need a record that amends `discovery-docs` section 2, which comes close to the
option ADR 0077 did not choose.

**The Shape Up pitch stays out, but the call is contested, at medium-low confidence.** One scorer moved it to
admission, because its old failure rested on the retired "names no solution" test. The critic reversed that.
Shaped work arrives solved at the level of how it works, which leans `develop`. The pitch also exists to be bet
on, and the bet commits a team's cycle, which comes close to the investment decision the rule excludes. The
opposing reading, that the pitch's appetite is the budget for handing the concept on that the rule permits, is
a fair one.

**`lean-canvas` and `opportunity-solution-tree` stay out on grounds ADR 0078 did not retire.** The lean
canvas's admission rests on one vendor page, it carries its Solution block beside its Problem block from the
first draft, and it is revisited rather than finished. The opportunity solution tree's sources are boards, and
ADR 0078 keeps the rule that a vendor's board template is not a named source publishing a written form.
*(2026-10-30: the lean canvas's grounds answered the `define` question only. Its admission now rests on Ash
Maurya's own teaching page, because Atlassian's site is treated as barred under the terms rule.
[ADR 0083](decisions/0083-lean-canvas-joins-strategy-docs-as-a-seventh-member.md) places it in `strategy-docs`
at `classification: utility`, where a canvas revised rather than finished fits, and the maintainer gave it
priority P2 as issue #337.)*

**The catalog's `definition` stage is not a define count.** The catalog files every type under one of 30 older
stages, which predate the library's six phases. That stage holds three types, among them the PRD, which
ADR 0077 keeps in `deliver`.

## 5. Where the Define effort stands

- **2026-10-10.** The maintainer ruled that `define` is for problem-framing documents
  ([ADR 0068](decisions/0068-define-means-problem-framing.md), since superseded).
- **2026-10-11.** `problem-statement` was built, the library's first `define` bundle. The first Define research
  sweep ran the same day.
- **2026-10-16.** Two more sweeps ran. The second found the Design Council naming a design brief as Define's
  output, and `design-brief` became candidate #294.
- **2026-10-17.** A decision sitting ruled that `define` ends with a chosen concept, never a specification.
  ADR 0077 supersedes ADR 0068 and moved `discovery-docs` to `0.4.0`. ADR 0078 widened what counts as
  templatable: a map, a canvas or a session record, through its written form.
- **2026-10-19.** `test-strategy` and `positioning-statement` were specced and accepted. #298 opened for the
  opportunity statement, which the sitting ruled a type of its own rather than an alias of
  `problem-statement`.
- **2026-10-19.** The parked `metric-tree` check ran. AIHR's KPI tree template, the one candidate source, is a
  page of fill-in boxes in four labelled columns, not text fields or tables. Before ADR 0078, that meant a
  refusal. Under ADR 0078, a labelled fill-in form can be templatable through its written form, as
  `product-vision`'s canvas format already is. So the type needs an admission re-test, not a refusal record.
- **2026-10-20.** The maintainer supplied the Zendesk Triple Diamond post and its linked milestones page as
  PDFs, after the raw fetch had returned HTTP 403. Zendesk names no Define phase, and its concept is chosen and
  tested after its Problem Definition milestone, still inside its Discovery phase. ADR 0077's first cost stands
  as stated, and a dated note on ADR 0077 records the read.
- **2026-10-20.** The Define re-score ran over 67 candidates (section 4). The design brief and the opportunity
  statement return for an admission sweep at `define`, and seven candidates wait on one read each. The
  maintainer queued `test-strategy` and `positioning-statement` the same day, and both builds began.
- **2026-10-21.** `test-strategy` (#301) and `positioning-statement` (#302) landed as the 48th and 49th
  bundles. Both sit at `classification: foundation`, so the define count stays at one. The maintainer confirmed
  `foundation` over `define` for `positioning-statement`, and confirmed ADRs 0070, 0074, 0075, 0076 and 0078 in
  one batch.
- **2026-10-22.** The maintainer named the design brief and the opportunity statement as the next Define work.
  The `problem-statement` change for sitting items D6 and D9 landed: "point of view statement" became an alias,
  and the opportunity statement left the alias list to become catalog entry 207. The design brief's admission
  sweep and spec ran the same day. The maintainer answered the spec's ten choices in one sitting, taking nine
  recommendations and choosing two sizes over one. ADR 0079 was accepted the same day on the maintainer's
  delegation. The
  opportunity statement's admission sweep began the same day. ADR 0080 (a fifth admission check, for a
  software audience) was drafted and accepted the same day on the maintainer's delegation.
- **2026-10-22, later.** The opportunity statement's sweep found five jobs under the name. Only Jeff Gothelf's
  net-new statement is distinct from `problem-statement` and allowed at `define`, and it rests on one formula.
  The maintainer parked the type, and `problem-statement`'s guide gained a paragraph for that case. The same
  walk confirmed ADRs 0079 and 0080, recorded Cagan's Product Opportunity Assessment as catalog entry 208,
  and gave the design brief's build its go.
- **2026-10-22, at landing.** `design-brief` was built through the `build-bundle` workflow as the 50th bundle
  and the second at `define`, with catalog entry 209. Its landing closes #294, so the define count is two.
- **2026-10-23.** An admission sweep found the user research plan and the usability test plan to be one
  type, and the maintainer agreed. It became catalog entry 210, the user research plan, a Tier 2 candidate
  with no family and no issue yet. The maintainer ruled that entry 18 (user research report) gets its own
  admission sweep first, because that result decides whether the plan founds a new family.
- **2026-10-23, later.** Entry 18's sweep cleared, and the maintainer recorded it as admitted. Both types gained
  build-candidate issues, #316 and #317, at P2. [ADR 0081](decisions/0081-adopt-research-docs-family-contract.md)
  adopts a `research-docs` contract at `discover` for the pair, after the maintainer's read the same day.
- **2026-10-24.** Both types were specced in one section of `tier2-specs.md`, each in two sizes, with examples
  that plan and report the 2026-05 Reporting friction study. The maintainer took all ten of the spec's
  recommendations in one line. Once the spec merged (#319), the maintainer queued both types, so #316 and #317
  now carry `status:queued`.
- **2026-10-24, at landing.** `user-research-plan` was built through the `build-bundle` workflow as the 51st
  bundle and the first `research-docs` member, at `discover`. Its landing closes #316, and the define count
  stays at two.
- **2026-10-27, at landing.** `user-research-report` was built through the `build-bundle` workflow as the
  52nd bundle and the second `research-docs` member, at `discover`, which completes the family's founding pair.
  Its landing closes #317, and the define count stays at two.

## 6. What comes next, in order

1. **A small README change for sitting item D8** (the "four literatures" passage).
2. **The seven evidence-insufficient reads, cheapest first.** Each one's score row names the read that would
   settle it. ADR 0080 (a fifth admission check, for a software audience), accepted on 2026-10-22, applies to
   them first.
3. **The four candidates that return outside Define, only when the maintainer chooses them.** None is urgent.

Outside this Define list, the `research-docs` contract
([ADR 0081](decisions/0081-adopt-research-docs-family-contract.md)) is adopted, and the specs for #316 and #317 were
ruled on 2026-10-24. Both members are now built: the plan on 2026-10-24 and the report on 2026-10-27.

Two steps this list carried on 2026-10-20 are done. `test-strategy` and `positioning-statement` landed on
2026-10-21, and the maintainer confirmed the five delegated acceptances the same day. A third step, the
`problem-statement` change for sitting items D6 and D9, landed on 2026-10-22. A fourth, the opportunity
statement's admission sweep, ended on 2026-10-22 with the type parked. A fifth, the design brief's build,
landed the same day.

## 7. When to revisit this page

- **When the next Define candidate moves**: one of the seven evidence-insufficient reads (step 2 above), or
  the parked opportunity statement. Update sections 2, 4 and 6 from its outcome.
- **At every release.** [`release-process.md`](release-process.md) lists this page among the technical surfaces
  to read. Refresh section 2 from GitHub, and read the prose around section 3's marker.
- **When a catalog row is added, or a bundle lands.** `check-counts.py` fails until the marker moves. Move the
  tables and prose with it, because the check reads the marker only.
- **By 2026-11-03 if nothing above has happened.** Re-read this page, and ask whether the seven
  evidence-insufficient reads are still the next piece of Define work.

## 8. How to refresh the numbers

The working backlog, from GitHub:

```
gh issue list --label build-candidate --state open --limit 200 --json number,title,labels
```

The catalog counts come from the `tier` and `state` fields in `atlas/catalog-data.json`. `check-counts.py`
computes the gated ones; run it and read any marker it reports as stale. The define counts come from the
`phase` field in [`manifest.json`](../../manifest.json) and from the issues labelled `phase:define`.
