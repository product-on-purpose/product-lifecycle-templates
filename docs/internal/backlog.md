# Build backlog: where it lives, what is outstanding, and what comes next

**This page is a dated snapshot, taken 2026-10-20.** The issue counts in section 2 were read from GitHub that
day, and no gate checks them, so they go stale as issues move. The catalog counts in section 3 sit under a
counts marker that [`tools/check-counts.py`](../../tools/check-counts.py) gates, so CI fails when they drift.
[`STATE.md`](../../STATE.md) outranks this page wherever the two disagree.

Section 7 says when to revisit this page. Nobody has re-scored the backlog for
[ADR 0077](decisions/0077-define-ends-with-a-chosen-concept.md) (define ends with a chosen concept) or
[ADR 0078](decisions/0078-maps-canvases-and-session-records-are-templatable-through-their-written-form.md)
(maps, canvases and session records are templatable). Until that re-score runs, sections 2 to 4 describe the
backlog under the rules that came before those two records.

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
| [#260](https://github.com/product-on-purpose/product-lifecycle-templates/issues/260) | `test-strategy` | Specced; [ADR 0075](decisions/0075-test-strategy-joins-standing-standards-as-a-foundation.md) accepted 2026-10-19 | P3 | 2 | `standing-standards`, `foundation` | Build |
| [#256](https://github.com/product-on-purpose/product-lifecycle-templates/issues/256) | `positioning-statement` | Specced; [ADR 0076](decisions/0076-positioning-statement-joins-strategy-docs-as-a-sixth-member.md) accepted 2026-10-19 | P3 | 2 | `strategy-docs`, `foundation` | Build |
| [#294](https://github.com/product-on-purpose/product-lifecycle-templates/issues/294) | `design-brief` | Candidate | P3 | 2 | Unassigned; labelled `phase:define` | A spec, once the Define re-score confirms it |
| [#298](https://github.com/product-on-purpose/product-lifecycle-templates/issues/298) | `opportunity-statement` | Candidate, opened 2026-10-19 | P3 | 2 | Unassigned; no axis yet | A catalog row, then admission research |
| [#261](https://github.com/product-on-purpose/product-lifecycle-templates/issues/261) | `requirements-traceability-matrix` | Candidate | P3 | 3 | Unassigned; `qa-docs` does not cleanly admit it | An admission sweep |
| [#257](https://github.com/product-on-purpose/product-lifecycle-templates/issues/257) | `metric-tree` | Parked | P3 | 2 | Unassigned | An admission re-test under ADR 0078 (see section 5) |
| [#258](https://github.com/product-on-purpose/product-lifecycle-templates/issues/258) | `messaging-framework` | Parked | P3 | 2 | Unassigned; neither candidate family admits it as written | None while its placement is held under [decision procedure 10](decision-procedures.md#10-a-family-or-axis-assignment-is-uncertain) |
| [#264](https://github.com/product-on-purpose/product-lifecycle-templates/issues/264) | `concept-test-validation-brief` | Parked by the maintainer 2026-10-06 | P4 | 2 | Unassigned; `discovery-docs` admits it as written | None while parked |

| Count by | Result |
|---|---|
| Status | 2 specced and ready to build, 3 candidates, 3 parked |
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
| Open candidates labelled `phase:define` | 1 | `design-brief` (#294) |
| Candidates awaiting the Define re-score | Roughly 60 | Drawn from three Define research sweeps (2026-10-11 and 2026-10-16). The figure is the planning estimate, not a count |

**Most of the roughly 60 are likely to stay out.** The third sweep alone tested 29 research and constraint
artifacts, and 26 failed on the evidence it read. The other three were untested, because their only sources
were dropped or unreachable.

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
  templatable: a map, a canvas or a workshop record, through its written form.
- **2026-10-19.** `test-strategy` and `positioning-statement` were specced and accepted. #298 opened for the
  opportunity statement, which the sitting ruled a type of its own rather than an alias of
  `problem-statement`.
- **2026-10-19.** The parked `metric-tree` check ran. AIHR's KPI tree template, the one candidate source, is a
  page of fill-in boxes in four labelled columns, not text fields or tables. Before ADR 0078, that meant a
  refusal. Under ADR 0078, a labelled fill-in form can be templatable through its written form, as
  `product-vision`'s canvas format already is. So the type needs an admission re-test, not a refusal record.

## 6. What comes next, in order

1. **The `problem-statement` change for sitting items D6 and D9.** It adds "point of view statement" as an
   alias, removes "opportunity statement" as one, and appends the opportunity statement's catalog row. That row
   moves the catalog's candidate count to 158, so section 3's marker and table move in the same PR.
2. **A small README change for sitting item D8** (the "four literatures" passage).
3. **The Define re-score.** Re-score the roughly 60 candidates under ADR 0077 and ADR 0078, using the evidence
   already on disk. Include the map and canvas candidates outside Define that ADR 0078 may reopen: `metric-tree`
   (#257) for certain, and `lean-canvas` and `opportunity-solution-tree` once someone checks whether the reasons
   recorded in their [Progress rows](tier2-specs.md#progress) rest on the test ADR 0078 retired. A source check
   on the Zendesk Triple Diamond post comes first; its raw fetch returned HTTP 403 on 2026-10-17.
4. **Rewrite sections 2 to 4 of this page from the re-score's output.** That rewrite produces the first real
   define count.
5. **Spec the first new Define bundle**: the design brief (#294), or the strongest candidate the re-score
   finds. Relabel #294 to match.
6. **Build `test-strategy` and `positioning-statement` when the maintainer chooses.** Both are ready now, and
   neither waits on the re-score.
7. **One batch confirmation from the maintainer.** Five records were accepted on the maintainer's delegation
   rather than a read: ADRs 0070, 0074, 0075, 0076 and 0078. Nothing waits on the confirmation.

## 7. When to revisit this page

- **When the Define re-score lands** (step 3 above). Rewrite sections 2 to 6 from its output.
- **At every release.** [`release-process.md`](release-process.md) lists this page among the technical surfaces
  to read. Refresh section 2 from GitHub, and read the prose around section 3's marker.
- **When a catalog row is added, or a bundle lands.** `check-counts.py` fails until the marker moves. Move the
  tables and prose with it, because the check reads the marker only.
- **By 2026-11-03 if nothing above has happened.** Re-read this page, and ask whether the re-score is still
  the next piece of work.

## 8. How to refresh the numbers

The working backlog, from GitHub:

```
gh issue list --label build-candidate --state open --limit 200 --json number,title,labels
```

The catalog counts come from the `tier` and `state` fields in `atlas/catalog-data.json`. `check-counts.py`
computes the gated ones; run it and read any marker it reports as stale. The define counts come from the
`phase` field in [`manifest.json`](../../manifest.json) and from the issues labelled `phase:define`.
