# Build backlog: where it lives, what is outstanding, and what comes next

**This page is a dated snapshot, taken 2026-10-20.** The issue counts in section 2 were read from GitHub that
day, and no gate checks them, so they go stale as issues move. The catalog counts in section 3 sit under a
counts marker that [`tools/check-counts.py`](../../tools/check-counts.py) gates, so CI fails when they drift.
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
| [`catalog.md`](catalog.md), rendered from `atlas/catalog-data.json` into the atlas | All 206 types the library's research found, each with a tier and a build state | A priority field. It also has no "declined" state, so a type declined by record still reads "candidate" there |
| The [Progress table](tier2-specs.md#progress) in `tier2-specs.md` | Every type assessed or specced beyond its catalog row, with its status and the record behind it | The types nobody has assessed yet |

**Only the issues carry a priority.** The catalog has tiers, and the build order among unproposed types is the
maintainer's own preference, by [ADR 0041](decisions/0041-maintainer-preference-sets-the-build-order.md).

**When an issue body and its labels disagree, the labels are current.** An issue body is written once, when
the issue opens. The `messaging-framework` issue still says "an admission sweep" is next, but sweep 6 has since
run and its label now reads `status:parked`.

## 2. The working backlog: 8 open candidates

| Issue | Type | Status | Priority | Tier | Family and axis | Next action |
|---|---|---|---|---|---|---|
| [#260](https://github.com/product-on-purpose/product-lifecycle-templates/issues/260) | `test-strategy` | Queued 2026-10-20; [ADR 0075](decisions/0075-test-strategy-joins-standing-standards-as-a-foundation.md) accepted 2026-10-19 | P3 | 2 | `standing-standards`, `foundation` | Build, under way |
| [#256](https://github.com/product-on-purpose/product-lifecycle-templates/issues/256) | `positioning-statement` | Queued 2026-10-20; [ADR 0076](decisions/0076-positioning-statement-joins-strategy-docs-as-a-sixth-member.md) accepted 2026-10-19 | P3 | 2 | `strategy-docs`, `foundation` | Build, under way |
| [#294](https://github.com/product-on-purpose/product-lifecycle-templates/issues/294) | `design-brief` | Candidate; confirmed for `define` by the 2026-10-20 re-score | P3 | 2 | Unassigned; labelled `phase:define` | An admission sweep and a spec, in the Design Council's sense (section 4) |
| [#298](https://github.com/product-on-purpose/product-lifecycle-templates/issues/298) | `opportunity-statement` | Candidate, opened 2026-10-19; confirmed for `define` by the re-score | P3 | 2 | Unassigned; labelled `phase:define` | A catalog row, then an admission sweep that settles whether it is distinct from `problem-statement` |
| [#261](https://github.com/product-on-purpose/product-lifecycle-templates/issues/261) | `requirements-traceability-matrix` | Candidate | P3 | 3 | Unassigned; `qa-docs` does not cleanly admit it | An admission sweep |
| [#257](https://github.com/product-on-purpose/product-lifecycle-templates/issues/257) | `metric-tree` | Parked | P3 | 2 | Unassigned; a classification, never a phase, by the re-score | An admission re-test under ADR 0078 (see section 4) |
| [#258](https://github.com/product-on-purpose/product-lifecycle-templates/issues/258) | `messaging-framework` | Parked | P3 | 2 | Unassigned; neither candidate family admits it as written | None while its placement is held under [decision procedure 10](decision-procedures.md#10-a-family-or-axis-assignment-is-uncertain) |
| [#264](https://github.com/product-on-purpose/product-lifecycle-templates/issues/264) | `concept-test-validation-brief` | Parked by the maintainer 2026-10-06 | P4 | 2 | Unassigned; `discovery-docs` admits it as written | None while parked |

| Count by | Result |
|---|---|
| Status | 2 queued and being built, 3 candidates, 3 parked |
| Priority | P3: 7, P4: 1 |
| Tier | Tier 2: 7, Tier 3: 1 |

Fifty-five candidate issues are closed: 47 built and 8 declined. Two of the declined types,
`solution-brief` and `prototype-brief`, never had a catalog row.

## 3. The catalog by tier

<!-- counts: statebuilt=47, statecandidate=157, stateoutofscope=2, tier1=25, tier1remaining=2 -->

The catalog holds 206 types. Its `state` field reads 47 built, 157 candidate and 2 out of scope. Four of the
157 were declined by record, so 153 types are still open.

| Tier | Types | Built | Declined or out of scope | Still open |
|---|---|---|---|---|
| 1 | 27 | 25 | 2: `wireframe` and `interactive-prototype`, out of scope by [ADR 0030](decisions/0030-templating-scope-markdown-documents.md) | **0** |
| 2 | 152 | 22 | 4, declined by record (below) | **126** |
| 3 | 27 | 0 | 0 | **27** |
| **All** | **206** | **47** | **6** | **153** |

The four Tier 2 types declined by record are `pi-release-retrospective`
([ADR 0049](decisions/0049-pi-release-retrospective-fails-the-admission-test.md)), `deployment-plan`
([ADR 0064](decisions/0064-deployment-plan-is-declined.md)), the steering committee pack
([ADR 0065](decisions/0065-steering-committee-pack-is-declined.md)), and the per-feature analytics
measurement plan ([ADR 0074](decisions/0074-analytics-requirements-measurement-plan-per-feature-is-declined.md)).
The last was declined in its per-feature reading only, and its business-scope reading has not been swept.

**Most of the 153 open types have never been proposed.** They have no issue, so they have no priority either.

## 4. The define phase

| Layer | Count | Which |
|---|---|---|
| Built bundles with `phase: define` | 1 | `problem-statement` |
| Open candidates labelled `phase:define` | 2 | `design-brief` (#294) and `opportunity-statement` (#298) |
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
| Stays out | 48 | Every other candidate, among them `lean-canvas`, `opportunity-solution-tree`, the Shape Up pitch and LEGO's Foundation Document |

**The design brief returns in the Design Council's sense only, with medium confidence.** The Design Council
names a design brief as Define's result, one "which clearly defines the challenge", and that document clears
the rule. Peter Phillips's wider commissioning brief does not fit as cleanly. He calls it "a written
agreement, or contract, between the parties", which reads as the project authorization the rule excludes. He
also counts a design strategy among its most critical sections. That can read as `develop`, though the reading
is contested, because design-management usage can mean how design serves business objectives. The admission
sweep must draw that line, possibly as a lean concept-handoff variant beside a full commissioning variant.

**The opportunity statement returns with one open question, at medium confidence.** It passes the rule on the
sources `problem-statement` already logs. One of those sources says the two are "written and used in the same
way", so its admission sweep must show that the types are distinct, or decline it as a duplicate.

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

## 6. What comes next, in order

1. **The `problem-statement` change for sitting items D6 and D9.** It adds "point of view statement" as an
   alias, removes "opportunity statement" as one, and appends the opportunity statement's catalog row. That row
   moves the catalog's candidate count to 158, so section 3's marker and table move in the same PR.
2. **A small README change for sitting item D8** (the "four literatures" passage).
3. **Land `test-strategy` and then `positioning-statement`.** Both builds are under way. Each landing PR edits
   its family contract's Members line, so each stops for the maintainer's read.
4. **An admission sweep and a spec for the design brief (#294).** The sweep must settle the line between
   Define's concept handoff and Phillips's commissioning brief (section 4).
5. **An admission sweep for the opportunity statement (#298).** It must settle whether the type is distinct
   from `problem-statement`. Its catalog row comes first, in step 1.
6. **The seven evidence-insufficient reads, cheapest first.** Each one's score row names the read that would
   settle it.
7. **The four candidates that return outside Define, only when the maintainer chooses them.** None is urgent.
8. **One batch confirmation from the maintainer.** Five records were accepted on the maintainer's delegation
   rather than a read: ADRs 0070, 0074, 0075, 0076 and 0078. Nothing waits on the confirmation.

## 7. When to revisit this page

- **When an admission sweep for the design brief or the opportunity statement lands** (steps 4 and 5 above).
  Update sections 2, 4 and 6 from its outcome.
- **At every release.** [`release-process.md`](release-process.md) lists this page among the technical surfaces
  to read. Refresh section 2 from GitHub, and read the prose around section 3's marker.
- **When a catalog row is added, or a bundle lands.** `check-counts.py` fails until the marker moves. Move the
  tables and prose with it, because the check reads the marker only.
- **By 2026-11-03 if nothing above has happened.** Re-read this page, and ask whether the design brief's
  admission sweep is still the next piece of Define work.

## 8. How to refresh the numbers

The working backlog, from GitHub:

```
gh issue list --label build-candidate --state open --limit 200 --json number,title,labels
```

The catalog counts come from the `tier` and `state` fields in `atlas/catalog-data.json`. `check-counts.py`
computes the gated ones; run it and read any marker it reports as stale. The define counts come from the
`phase` field in [`manifest.json`](../../manifest.json) and from the issues labelled `phase:define`.
