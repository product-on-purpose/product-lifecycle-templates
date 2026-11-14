# Build backlog: where it lives, what is outstanding, and what comes next

**This page is a dated snapshot, taken 2026-10-20 and refreshed 2026-10-29, 2026-10-30, 2026-11-04, 2026-11-05, 2026-11-06, 2026-11-07, 2026-11-08 and 2026-11-09.** The issue counts in section 2 were
read from GitHub on 2026-11-09, and no gate checks them, so they go stale as issues move. The catalog
counts in section 3 sit under a counts marker that [`tools/check-counts.py`](../../tools/check-counts.py)
gates, so CI fails when they drift.
[`STATE.md`](../../STATE.md) outranks this page wherever the two disagree.

Section 7 says when to revisit this page. The Define re-score that
[ADR 0077](decisions/0077-define-ends-with-a-chosen-concept.md) (define ends with a chosen concept) and
[ADR 0078](decisions/0078-maps-canvases-and-session-records-are-templatable-through-their-written-form.md)
(maps, canvases and session records are templatable) called for ran on 2026-10-20. Sections 2, 4, 5 and 6
reflect it. Its digest is held locally, at `_local/research/2026-10-20_define-rescore/digest.md`.

## 1. Where the backlog lives

No single list holds the backlog. Four places hold parts of it, and each one lacks something the others have.
*(The fourth, section 9, was added 2026-11-13.)*

| Place | What it holds | What it lacks |
|---|---|---|
| [GitHub issues labelled `build-candidate`](https://github.com/product-on-purpose/product-lifecycle-templates/issues?q=is%3Aissue+is%3Aopen+label%3Abuild-candidate) | The working backlog: every type someone has proposed to build, labelled by status, priority, tier, family and axis. Closed issues record the types built or declined | Any type nobody has proposed. Issue #180 (the ranking, and what would be refused) carries the label but is a discussion, not a candidate |
| [`catalog.md`](catalog.md), rendered from `atlas/catalog-data.json` into the atlas | All 212 types the library's research found, each with a tier and a build state | A priority field. It also has no "declined" state, so a type declined by record still reads "candidate" there |
| The [Progress table](tier2-specs.md#progress) in `tier2-specs.md` | Every type assessed or specced beyond its catalog row, with its status and the record behind it | The types nobody has assessed yet |
| [Section 9](#9-researched-types-with-no-issue-and-no-decision) of this page | Every type a research run named as a candidate that has no issue and no decision, including types with no catalog row | A ruling: each row's next step is a proposal |

**Only the issues carry a priority.** The catalog has tiers, and the build order among unproposed types is the
maintainer's own preference, by [ADR 0041](decisions/0041-maintainer-preference-sets-the-build-order.md).

**When an issue body and its labels disagree, the labels are current.** An issue body is written once, when
the issue opens. The `messaging-framework` issue still says "an admission sweep" is next, but sweep 6 has since
run and its label now reads `status:parked`.

## 2. The working backlog: the open candidates

| Issue | Type | Status | Priority | Tier | Family and axis | Next action |
|---|---|---|---|---|---|---|
| [#298](https://github.com/product-on-purpose/product-lifecycle-templates/issues/298) | `opportunity-statement` | Parked by the maintainer 2026-10-22, after its admission sweep | P3 | 2 | Unassigned; labelled `phase:define` | None while parked. The sweep found it distinct only in Jeff Gothelf's net-new sense, on one formula, and `problem-statement`'s guide now covers that case. A template with sections for it would reopen the question |
| [#257](https://github.com/product-on-purpose/product-lifecycle-templates/issues/257) | `metric-tree` | Parked | P3 | 2 | Unassigned; a classification, never a phase, by the re-score | An admission re-test under ADR 0078 (see section 4) |
| [#258](https://github.com/product-on-purpose/product-lifecycle-templates/issues/258) | `messaging-framework` | Parked | P3 | 2 | Unassigned; neither candidate family admits it as written | None while its placement is held under [decision procedure 10](decision-procedures.md#10-a-family-or-axis-assignment-is-uncertain) |
| [#264](https://github.com/product-on-purpose/product-lifecycle-templates/issues/264) | `concept-test-validation-brief` | Parked by the maintainer 2026-10-06 | P4 | 2 | Unassigned; `discovery-docs` admits it as written | None while parked |

| Count by | Result |
|---|---|
| Status | 4 parked |
| Priority | P3: 3, P4: 1 |
| Tier | Tier 2: 4 |

Sixty-seven candidate issues are closed: 56 built and 11 declined. The last to close was #353 (platform-device-support-matrix). Four of the declined types,
`solution-brief`, `prototype-brief`, `manager-user-guide` and `product-discovery-plan`, never had a catalog row.

**Admission sweep 7 ran on 2026-10-29, so "an admission sweep" is no longer the next action for its candidates.**
*(Recorded 2026-11-04.)* The sweep judged #312, #261, #329 and #331, plus the Lean UX Canvas (#330), which it
recommended declining and which the maintainer then asked to have specced and built. Its verdicts are recommendations:
no candidate has been admitted, and none carries `status:queued`. The maintainer chose on 2026-11-04 to take the four
through admission in this order: #312, #261, #329, #331. The digest is held locally, at
`_local/research/2026-10-29_admission-sweep-7/digest.md`, and each issue carries its verdict as a comment.
*(2026-11-05: the maintainer has since ruled on three of the four. #261 is admitted and built, #312 and #329 are
declined and closed, and #331 waits on one more read.)* *(2026-11-07: #331 is declined and closed, by
[ADR 0087](decisions/0087-product-discovery-plan-is-declined.md), so all four are ruled on.)*

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

<!-- counts: statebuilt=56, statecandidate=154, stateoutofscope=2, tier1=25, tier1remaining=2 -->

The catalog holds 212 types. Its `state` field reads 56 built, 154 candidate and 2 out of scope. Five of the
154 were declined by record, so 149 types are still open.

| Tier | Types | Built | Declined or out of scope | Still open |
|---|---|---|---|---|
| 1 | 27 | 25 | 2: `wireframe` and `interactive-prototype`, out of scope by [ADR 0030](decisions/0030-templating-scope-markdown-documents.md) | **0** |
| 2 | 158 | 30 | 5, declined by record (below) | **123** |
| 3 | 27 | 1 | 0 | **26** |
| **All** | **212** | **56** | **7** | **149** |

The five Tier 2 types declined by record are `pi-release-retrospective`
([ADR 0049](decisions/0049-pi-release-retrospective-fails-the-admission-test.md)), `deployment-plan`
([ADR 0064](decisions/0064-deployment-plan-is-declined.md)), the steering committee pack
([ADR 0065](decisions/0065-steering-committee-pack-is-declined.md)), the per-feature analytics
measurement plan ([ADR 0074](decisions/0074-analytics-requirements-measurement-plan-per-feature-is-declined.md)),
and `product-opportunity-assessment` ([ADR 0086](decisions/0086-product-opportunity-assessment-is-declined.md)).
The analytics plan was declined in its per-feature reading only, and its business-scope reading has not been swept.

**Most of the open types have never been proposed.** They have no issue, so they have no priority either.

## 4. The define phase

| Layer | Count | Which |
|---|---|---|
| Built bundles with `phase: define` | 2 | `problem-statement`; `design-brief`, built 2026-10-22 (#294) |
| Open issues labelled `phase:define` | 1 | `opportunity-statement` (#298), parked |
| Candidates still short of evidence | 2 | The DoD Initial Capabilities Document and a regulatory requirements register, after the 2026-11-08 reads below |

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

**The seven settling reads ran on 2026-11-08, and five of the seven moved.** Each read was the one its score row
named, with ADR 0080's audience check applied first. One used the maintainer's own copy of *Lean UX* (2021). The
web reads checked each site's terms before reading it, and every quotation used was checked against the page's
raw text. The read record is held locally, at `_local/research/2026-11-08_define-reads/`. No catalog row changed,
and no candidate is admitted: an admission sweep still needs the maintainer's choice.

| Read outcome, 2026-11-08 | Candidates | Confidence |
|---|---|---|
| Stays out of `define` | The proto-persona: *Lean UX* presents it as Box 3 of the Lean UX Canvas, which `lean-ux-canvas` carries, and `user-persona` teaches it as its lightest evidence tier | high |
| Stays out of `define` | NASA's needs, goals and objectives with its concept of operations: NASA defines a need as the answer to "What problem are we trying to solve?", which is `problem-statement`'s question, and the concept of operations describes a system already envisioned. No software source could be read | medium-high |
| Stays out of `define` | The accessibility conformance target: no source treats the target as a document. W3C puts the level inside an organisation's accessibility policy, and GOV.UK requires only a statement after release | medium |
| Stays out of `define` | The "Target" phase of the Behavioural Insights Team's TEST method: its handbook names a target statement and a short list of target behaviours, written on worksheets inside a project. No software or UX use was found | medium |
| Returns for an admission sweep elsewhere | The platform and device support matrix: GOV.UK publishes both a browser test table and a set of graded support levels. Technology teams write it and revise it as usage changes, which makes it a standing standard rather than a `define` document. *(2026-11-09: its admission sweep ran on 2026-11-08, and it is admitted to `standing-standards` by [ADR 0088](decisions/0088-platform-device-support-matrix-joins-standing-standards-as-a-foundation.md), issue #353.)* | medium |
| Still short of evidence | The DoD Initial Capabilities Document: its only software use found is inside defence acquisition, so ADR 0080 parks it whatever its settling read finds | medium |
| Still short of evidence | The regulatory requirements register: the only register forms found were vendor pages whose terms could not be checked, and the ISO/IEC 27001 text is paywalled | low |

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
- **2026-10-30.** At the maintainer's request, Jeff Gothelf's Lean UX Canvas (#330) and Ash Maurya's Lean
  Canvas (#337) were specced and admitted, by ADR 0082 into `discovery-docs` and by ADR 0083 into
  `strategy-docs`. The maintainer accepted both records after reading the contract diffs, then took all
  fourteen of the specs' recommendations in one line. Once the specs merged (#338), both types were queued, so
  #330 and #337 now carry `status:queued`.
- **2026-10-30, at landing.** `lean-ux-canvas` landed as the 53rd bundle and the sixth `discovery-docs`
  member, at `discover`, carrying catalog entry 211. Its landing closes #330, and the define count stays at
  two.
- **2026-10-30, at landing.** `lean-canvas` landed as the 54th bundle and the seventh `strategy-docs`
  member, at `classification: utility`, carrying catalog entry 5. Its landing closes #337, and the define
  count stays at two, since the family sits on the classification axis rather than the phase axis.
- **2026-11-06, at landing.** `requirements-traceability-matrix` landed as the 55th bundle, the eighth `governance-docs`
  member and the first built Tier 3 type, carrying catalog entry 37. Its landing closes #261, and the define
  count stays at two, since the family sits on the classification axis.
- **2026-11-08.** The seven evidence-insufficient reads ran (section 4). Four candidates stay out of `define`,
  the device support matrix returns for an admission sweep outside it, and two stay short of evidence. The define
  count stays at two.
- **2026-11-09.** The device support matrix's admission sweep (run 2026-11-08) admits it to `standing-standards`
  as a `foundation`, by [ADR 0088](decisions/0088-platform-device-support-matrix-joins-standing-standards-as-a-foundation.md),
  accepted the same day after the maintainer read the contract change. It opens as #353 (bundle: platform-device-support-matrix). The define count stays at
  two, since the family sits on the classification axis.
- **2026-11-12, at landing.** `platform-device-support-matrix` landed as the 56th bundle, the eighth
  `standing-standards` member, carrying catalog entry 212, a new row added at its build. Its landing closes #353,
  and the define count stays at two.

## 6. What comes next, in order

1. **The five candidates that return outside Define, only when the maintainer chooses them.** These are the four
   from the 2026-10-20 re-score and the device support matrix from the 2026-11-08 reads. None is urgent.
   *(2026-11-09: the device support matrix is admitted and queued as #353, so four remain.)*
2. **The two candidates still short of evidence, only if a source turns up.** The DoD Initial Capabilities
   Document is parked by ADR 0080. The regulatory requirements register needs a source whose terms permit reading
   and that shows a software team keeping one.

No Define candidate is now waiting on a read the library can run by itself.

Outside this Define list, the `research-docs` contract
([ADR 0081](decisions/0081-adopt-research-docs-family-contract.md)) is adopted, and the specs for #316 and #317 were
ruled on 2026-10-24. Both members are now built: the plan on 2026-10-24 and the report on 2026-10-27.

The maintainer's 2026-11-04 choice put the four sweep 7 candidates ahead of this Define list. All four are now
ruled on: the last, #331 (product discovery plan), was declined on 2026-11-07 by [ADR 0087](decisions/0087-product-discovery-plan-is-declined.md).
A candidate goes to a build only after
it clears admission and the maintainer gives that build its own go.

Two steps this list carried on 2026-10-20 are done. `test-strategy` and `positioning-statement` landed on
2026-10-21, and the maintainer confirmed the five delegated acceptances the same day. A third step, the
`problem-statement` change for sitting items D6 and D9, landed on 2026-10-22. A fourth, the opportunity
statement's admission sweep, ended on 2026-10-22 with the type parked. A fifth, the design brief's build,
landed the same day. A sixth, the README change for sitting item D8, landed on 2026-11-08. It rewrote the
`standing-standards` passage on review triggers against all seven members' research logs, not the six the
approved draft named, because `test-strategy` had joined the family since. A seventh, the seven
evidence-insufficient reads, ran the same day.

## 7. When to revisit this page

- **When the next Define candidate moves**: the maintainer chooses one of the candidates in step 1 above, a
  source turns up for one in step 2, or the parked opportunity statement moves. Update sections 2, 4 and 6 from
  its outcome.
- **At every release.** [`release-process.md`](release-process.md) lists this page among the technical surfaces
  to read. Refresh section 2 from GitHub, and read the prose around section 3's marker.
- **When a research run ends.** Add every type it recommended that the maintainer did not queue to section 9,
  so a later session can find it without the run's gitignored report.
- **When a catalog row is added, or a bundle lands.** `check-counts.py` fails until the marker moves. Move the
  tables and prose with it, because the check reads the marker only.
- **By 2026-12-04 if nothing above has happened.** Re-read this page, and ask whether any Define work remains
  that the library can start without the maintainer's choice. *(The 2026-11-03 date passed with two bundles
  landed and the four sweep 7 candidates chosen ahead of the seven reads, which then ran on 2026-11-08.)*

## 8. How to refresh the numbers

The working backlog, from GitHub:

```
gh issue list --label build-candidate --state open --limit 200 --json number,title,labels
```

The catalog counts come from the `tier` and `state` fields in `atlas/catalog-data.json`. `check-counts.py`
computes the gated ones; run it and read any marker it reports as stale. The define counts come from the
`phase` field in [`manifest.json`](../../manifest.json) and from the issues labelled `phase:define`.

## 9. Researched types with no issue and no decision

*(Added 2026-11-13.)* The library's research runs name more document types than ever reach an issue. A run
ends with the maintainer queueing its strongest few, and the rest stay in a gitignored report that no later
session reads. Queueing the strongest few is a decision about those few. It is not a decline of the others, so
until now the others sat in limbo. This section is their committed home.

**What qualifies.** A type is listed here when a research run named it as a candidate, and it has no
build-candidate issue, no decision record, no row in the [Progress table](tier2-specs.md#progress), and no
ruling elsewhere on this page. Types that a run tested and rejected on its own evidence are not listed, and
the last subsection names where those rejections live.

**Every "Proposed next step" is a proposal.** Nothing in this section admits, queues or declines a type. A
type still needs an admission sweep and the maintainer's choice, under
[ADR 0041](decisions/0041-maintainer-preference-sets-the-build-order.md), before it gets an issue. Issue #180
(the ranking, and what would be refused) still governs when an issue opens: "When a candidate earns a ranking
basis, it gets an issue." The `_local/` paths below are gitignored and exist only on the maintainer's machine.

### 9.1 New types a run recommended for an admission sweep

None of these has a catalog row. Two runs produced them. The PM-resources Standard run of 2026-10-23
recommended sixteen types; the maintainer queued its three high-confidence types on 2026-10-25, and all
three have since been ruled on. Its pilot of 2026-10-22 recommended a research plan, a usability test plan and
five more types; the maintainer chose to sweep the first two, which became `user-research-plan`. The confidence
column is the run's own.

| Type | Named source | Run | Confidence | What the run left open | Proposed next step |
|---|---|---|---|---|---|
| Product handover document | Mind the Product | Standard | medium | It is written when a role changes hands, so neither a phase nor a classification fits cleanly | Sweep, with a placement read first |
| Value Proposition Canvas | Strategyzer | Standard | medium | One usable source; a second copy was gated, which is not a contradiction. The run found no catalog type naming both of its sides, the closest being `business-model-canvas` (catalog 4) | Sweep beside `business-model-canvas`; [ADR 0078](decisions/0078-maps-canvases-and-session-records-are-templatable-through-their-written-form.md) admits canvases through their written form |
| LLM-as-judge rubric (critique shadowing record) | Hamel Husain | Standard | medium | Whether it and the error-mode taxonomy are one artifact at two stages | Sweep the two together as one candidate |
| Error-mode taxonomy (open-coding log) | Hamel Husain | Standard | low | A narrated practice at one company; no published shape was verified | Fold into the rubric's sweep |
| A/B testing roadmap (experimentation backlog) | CXL | Standard | medium | It plans many tests, so it is distinct from `experiment-design-doc`, which plans one | Sweep against the [`experimentation-docs`](contracts/experimentation-docs.md) contract |
| Experimentation platform RFP | Statsig | Standard | medium | Most of its verified headings are not the RFP's own, and the filled template was never read | Park until the filled template is read by hand |
| Debt inventory | ProdPad | Standard | medium | The checklist body sits behind an email gate | Park until the maintainer reads the body by hand |
| Product principles document | Productboard | Standard | medium | Its only source is an AI prompt whose output is the document | Test as a duplicate first: [ADR 0087](decisions/0087-product-discovery-plan-is-declined.md) maps Cagan's "Product Principles" component to `product-strategy`. If it survives, sweep it together with design principles (9.2), which may be the same type |
| User Story Map | Jeff Patton | Standard | low to medium | The written form is in Patton's book, which was not read | Park until a read of the book |
| PM skills gap analysis | SVPG | Standard | low to medium | It assesses a person, not a product, so the [ADR 0080](decisions/0080-admission-gains-a-software-audience-check.md) audience check is unclear | Run the audience check before any sweep |
| Whole-product bill of materials checklist | Rich Mironov | Standard | low to medium | The only evidence is a document title | Park until a source shows the written form |
| Idea Bank | Itamar Gilad | Standard | low to medium | The template is gated; the same run's delivery-docs report proposed naming it in `product-backlog`'s "When NOT to use" list instead | Weigh the guide line before a sweep |
| Positioning and messaging rollout checklist | Product Marketing Alliance | Standard | low | The body is paywalled, and its audience is product marketers rather than software teams | Park; the ADR 0080 audience check is the likely blocker |
| Screener | GOV.UK, dscout, User Interviews | Pilot | medium | Whether it is distinct from `survey-instrument` (catalog 26): the same form, a different job | Sweep with the recruitment brief as one recruiting pair; see the note below the table on placement |
| Recruitment brief | GOV.UK | Pilot | medium | One source | Sweep with the screener |
| Participant information sheet | GOV.UK | Pilot | medium | Whether it and the consent form are one bundle with two documents | Sweep with the consent form as one consent pair |
| Consent form | GOV.UK | Pilot | medium | As for the information sheet | Sweep with the information sheet |
| Interview snapshot | Product Talk (Teresa Torres) | Pilot; and the Torres book read of 2026-11-07, which ADR 0087 records as a side finding not acted on | medium | Its distinctness from `empathy-map` (catalog 20), which has different fields | Sweep; placement is open, as for the four above |

**Placement is the hard question for the last five.** Each one is used for or during one study. The
[`research-docs`](contracts/research-docs.md) contract admits only a type that "plans or reports on one study",
and it names the interview guide and the survey instrument as types it does not admit without an amendment for
the same reason. So each of these needs either that amendment or another family. `user-research-plan`'s full
template already asks where the screener lives, which shows the need but admits nothing.

Sources: `_local/resources/product-management-resources/standard-run/standard-report.md`, the seven
`standard-run/*/w4-candidates.md` files beside it, and
`_local/resources/product-management-resources/pilot-discovery-research/pilot-report.md`.

### 9.2 Types the Define re-score sent to a sweep outside `define`

The 2026-10-20 re-score (section 4) gave four candidates the "returns for an admission sweep elsewhere"
outcome. `metric-tree` is issue #257, parked, and none of the other three has an issue.

| Type | Catalog | Proposed next step |
|---|---|---|
| Design principles / experience principles | none | Sweep as a `foundation`, together with the product principles document (9.1) |
| DMAIC project charter | points at `project-charter` (catalog 70), unbuilt | Sweep `project-charter` itself first; the DMAIC charter, and the DMADV charter the re-score found no different, are its variants |
| GDPR records of processing activities | catalog 176, Tier 3 | Held by decision D4 (no Tier-3 regulated content), which reopens only on a pull from a real regulated team |

### 9.3 Types that passed admission in the re-score and were never tested in another family

The re-score tested every candidate against the `define` rule only, so a pass on admission followed by "stays
out of `define`" says nothing about any other family (section 4). Three such rows are covered by bundles built
since: `lean-canvas`, the research synthesis (`user-research-report`) and the Lean UX hypothesis box
(`lean-ux-canvas`). The rest are below. This list reads the score files' admission verdict directly and keeps
two rows whose pass was qualified, the technical constraints document and the architecture context, so it does
not match section 4's count exactly. Source: `_local/research/2026-10-20_define-rescore/score-*.json`.

| Type | Catalog | Proposed next step |
|---|---|---|
| Competitive analysis | 11 | Sweep; it is the one row here that the re-score, the 2026-10-04 ranking and the Standard run all reached |
| Threat model | 155 | Sweep, with placement open |
| Stakeholder map / register | 181 | Sweep |
| Assumptions log / tracker | 153 (`assumption-log`) | Sweep beside `raid-log`, which the re-score named as its overlap; the 2026-10-04 ranking called it a standing governance artifact, and the July 2026 expansion plan proposed a strategic assumptions log as a `strategy-docs` member |
| Market requirements document | 10 | Settle a conflict first: the 2026-10-04 ranking pre-failed it because `prd`'s companion folds the MRD into the PRD, while the Standard run's strategy cluster called its evidence the strongest structural evidence any existing candidate gained there |
| Accessibility conformance report / VPAT | 179, Tier 3 | Ask whether decision D4 reaches it before any sweep; the catalog's methodology field reads "compliance (WCAG/Section 508)" |
| Data protection impact assessment | 177, Tier 3 | Held by decision D4; the catalog's methodology field reads "compliance (GDPR)" |
| Design inputs document | 160, Tier 3 | Held by decision D4; the catalog cites 21 CFR 820.30(c) and ISO 13485 |
| Creative brief | none | Run the ADR 0080 audience check first. `design-brief`, built two days after the re-score, names it as a separate document that informs a design brief, so it is a named neighbour rather than a duplicate |
| Hills (IBM Enterprise Design Thinking) | none | Test as a possible alias or section of `product-strategy`, which the re-score named as its overlap |
| SAFe epic hypothesis statement | none | Test as a duplicate first; the re-score named `business-case` as its overlap, and `epic` is worth checking too |
| Technical feasibility assessment | none | Test as a duplicate first; the re-score found it not distinct from built content |
| Technical constraints document | none | As for the feasibility assessment; its admission pass was also never raw-checked |
| Architecture context / system context statement (arc42) | none | Test as a section of `sdd` before any sweep |
| DOE mission need statement (DOE G 413.3-17); DoD Software Acquisition Pathway capability needs statement | none | Run the ADR 0080 audience check on each. Both come from government programme guidance, and ADR 0080 already parks the DoD Initial Capabilities Document because its only software use is inside defence acquisition |

### 9.4 Catalog rows an earlier ranking found a family for, with no issue

The 2026-10-04 ranking (`_local/research/2026-10-04_pm-candidates.md`) ranked thirty types. Its first nine
rows were all built or parked. These later rows had a family fit, or a strong admission prior, and nothing has
happened to them since.

| Type | Catalog | What the ranking found | Proposed next step |
|---|---|---|---|
| Business model canvas | 4 | No family admitted it cleanly, but its admission prior is strong, because `methodology.md` names Osterwalder as Tier 1 | Sweep with the Value Proposition Canvas (9.1); `lean-canvas`, a canvas the same ranking also placed nowhere, has since joined `strategy-docs` by [ADR 0083](decisions/0083-lean-canvas-joins-strategy-docs-as-a-seventh-member.md) |
| Empathy map | 20 | No family admits it, and no admission prior was found beyond `user-persona`'s guide treating it as complementary | Re-test under ADR 0078, which postdates the ranking, against the interview snapshot (9.1) |
| Product operating model / team topology doc | 7 | `standing-standards` admits it by analogy, with an unclear falsifier; admission prior unknown | Sweep |
| Strategic theme / portfolio vision | 9 | `strategy-docs` admits it by analogy, strained against the four-question chain | Sweep |

**`research-docs` did not exist when that ranking ran.** The ranking found no family for the interview guide
(catalog 25), the survey instrument (26) and the diary or field study plan (28), because each is written once
per study. The `research-docs` contract, adopted by
[ADR 0081](decisions/0081-adopt-research-docs-family-contract.md) on 2026-10-23, names all three. It says its
membership clause would admit the diary study plan if a sweep finds it distinct from `user-research-plan`. It
does not admit the interview guide or the survey instrument without an amendment, because each is used during a
study rather than planning or reporting on one. The diary study plan is therefore the cheapest re-test in this
subsection.

The ranking also found no family for win-loss analysis (15), pricing and packaging (16), the voice-of-customer
report (17), cohort retention analysis (145), funnel analysis (146), the model card (149), the customer journey
map (23), the service blueprint (24) and the TAM/SAM/SOM model (12). None of these has been re-tested since.
The `research-docs` contract places the voice-of-customer report outside itself, as a standing aggregate.

### 9.5 Types a shipped guide names, with no catalog row

Issue #180's ranking basis puts first "the documents the shipped library already routes readers to and does
not ship". These types are named in a shipped guide and have no catalog row, so each needs a row before it can
be proposed. The 2026-09-22 ranking proposal (`_local/backlog/2026-09-22_candidate-backlog-ranking-proposal.md`)
found them, and a grep of the guides on 2026-11-13 confirmed that each one is still named there. Three of its
types are left out. The PRINCE2 highlight report is now an alias of the built `status-report`. The guides no
longer name a coding standards document or engineering handbook in those words. The one "stakeholder update" a
guide names is a skill in another repository, not a document type.

| Type | Named in | Catalog |
|---|---|---|
| Anti-persona | `user-persona_guide.md`, as a separate document written once a positive persona exists | none |
| Governance stage-gate review | `definition-of-ready_guide.md`, as a neighbour; `product-backlog_guide.md` | none |
| ITIL problem record | `incident-postmortem_guide.md`, as the record a postmortem feeds | none |
| Service operations manual | `runbook_guide.md`, as a bigger scope than a runbook | none |
| Prosci change-management communications plan | `announcement-internal-comms_guide.md`, as a neighbour | possibly `communication-management-plan` (catalog 83), whose aliases include "stakeholder communication plan"; the 2026-09-22 proposal called the match unconfirmed |

The proposed next step for each is the same: decide whether the guide's mention is a routing promise or only a
boundary. Only a routing promise earns a catalog row and then a sweep.

### 9.6 Catalog rows that only gained evidence

The Standard run tied every verified quotation and heading to its catalog row, and most of the rows it reached
are unbuilt. The rows are candidates already, so gaining evidence changes no state, and they are not repeated
here. The full table is `_local/resources/product-management-resources/standard-run/candidate-evidence.csv`.
Among unbuilt rows, the ones with the most verified headings include the team charter (catalog 80), the runbook,
knowledge base or SOP row (198, which may belong to the built `runbook` instead), the project management plan
(72), win-loss analysis (15), the messaging framework (14, issue #258), the FAQ document (185) and the sales
battlecard (196). Admission sweep 7 named the team charter, the working agreement (100) and the onboarding
guide (195) as the nearest neighbours of the declined manager user guide.

### 9.7 What this section does not cover

**Already refused or settled, so not listed.** These types are settled in issue #180's refusals (the ADR 0030
scope rule and the library's written rulings), in section 4's Define reads, in the format candidates of
section 2, and in the [Progress table](tier2-specs.md#progress). The Standard run's report also lists the
types it recommended as nothing.

**Resource types, not document types.** The 2026-07-17 expansion research proposes a glossary, a method
selection guide, an anti-pattern catalog, an artifact relationship map and workshop kits. Those are library
resources rather than templates. They belong to the expansion plan, not to this backlog.

**Sources read for this section:** the Standard run report and its seven cluster files, the pilot report and
its candidate file, the re-score's score files, the 2026-09-22 ranking proposal and session brief, the
2026-09-25 and 2026-10-04 candidate lists, the 2026-07-17 expansion research and phases plan, the digests of
admission sweeps 2, 3, 4 and 7, the 2026-11-08 Define reads digest, and the read notes on Cagan's books,
Torres's book, the product opportunity assessment and the manager user guide.

**Sources not read for it:** the two ChatGPT deep-research reports of July 2026, of which the first opens on the
library's direction and ecosystem and the second concerns a different repository; the digests of admission sweeps 5 and 6, whose outcomes are in the
Progress table; the raw files of the three Define sweeps, which the re-score enumerated; and the
`_local/research/hand-reads/` folder. A type missing from this section is not thereby ruled out.

**When to update it.** When a research run ends, add every type it recommended that the maintainer did not
queue. When a type here gets an issue or a decision, move it out and say where it went.
