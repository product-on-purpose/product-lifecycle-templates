# Tier-2 build-out: per-type specs and progress

Companion to [`buildout-specs.md`](buildout-specs.md), which is the **Tier-1 floor** spec sheet and says so
in its own heading. That floor is complete, and this file is where a Tier-2 type's per-type judgment lives
instead.

It exists because the build runbook has a hole. [`bundle-pipeline.md`](bundle-pipeline.md) and the
`build-bundle` command both name "the type's spec in `buildout-specs.md`" as required reading before a build starts, and for a Tier-2 type there is no such entry and never was. The first Tier-2 build would
otherwise have been exactly what `buildout-specs.md`'s preamble says a spec sheet prevents: "an open-ended
design task" rather than "a spec-driven execution".

> **A spec here is not a decision to build.** Build order is the maintainer's own preference and need
> ([ADR 0041](decisions/0041-maintainer-preference-sets-the-build-order.md)), and nothing on this page
> schedules anything. What a spec does is make the judgment reviewable *before* roughly 6M to 12M weighted
> token-equivalents, $12 to $41 at API list rates, are spent executing it
> ([measured](../../bundle-builds/INDEX.md); this sentence read "700K to 1M tokens" until 2026-09-22, an
> estimate nobody had measured, and "$33 to $41" until 2026-09-23, before the first build through the
> committed workflow cost $14.22; and "7M to 12M" and "$14 to $41" until 2026-10-11, after
> `definition-of-ready`'s build, at 5,846,070 weighted and $11.69, had already come in under both).

## Progress

| Type | Catalog id | Family | Spec | Built |
|---|---|---|---|---|
| `spike-report` | `spike-research-spike-report` | `decision-docs` | **Written 2026-09-11**; researched 2026-09-11, [admission evidence](spike-report-admission-evidence.md) | **Built 2026-09-12.** Admitted by [ADR 0048](decisions/0048-one-named-source-clears-the-admission-test.md) |
| `project-milestone-retrospective` | `project-milestone-retrospective` | `process-docs` | **Written 2026-09-11** | **Built 2026-09-14**, shipped in `v0.8.0` |
| `pi-release-retrospective` | `pi-release-retrospective` | `process-docs` | **Written 2026-09-11** | **No, and it will not be.** Refused on its own evidence by [ADR 0049](decisions/0049-pi-release-retrospective-fails-the-admission-test.md): SAFe's own facilitator guide names the outputs as backlog items and no document |
| `test-summary-report` | `test-report-test-summary-report` | `qa-docs` | **Written 2026-09-11** | **Built 2026-09-14**, shipped in `v0.8.0` |
| `launch-coordination-checklist` | `launch-coordination-checklist` | `standing-standards` | **Written 2026-09-22**; admission source [retrieved the same day](#standing-standards-third-member-the-launch-coordination-checklist) | **Built 2026-09-22**, shipped in `v0.12.0`. [Build report](../../bundle-builds/reports/launch-coordination-checklist_v0.1.0.md): 15 agents, all resolved to Sonnet |
| `issue-log` | `issue-log` | `governance-docs` | **Written 2026-09-23**; admission sources [retrieved and raw-checked the same day](#governance-docs-fourth-member-the-issue-log-the-library-already-routes-to) | **Built 2026-09-23**, shipped in `v0.13.0`. Family by [ADR 0057](decisions/0057-issue-log-joins-governance-docs-as-a-fourth-member.md); [build report](../../bundle-builds/reports/issue-log_v0.1.0.md) |
| `definition-of-ready` | `definition-of-ready` | `standing-standards` | **Written 2026-09-23**; admission sources [retrieved and raw-checked the same day](#standing-standards-fourth-member-the-definition-of-ready-a-type-this-library-has-argued-against) | **Built 2026-09-23**, shipped in `v0.13.0`. Family and classification by [ADR 0058](decisions/0058-definition-of-ready-joins-standing-standards-as-a-foundation.md); [build report](../../bundle-builds/reports/definition-of-ready_v0.1.0.md) |
| `announcement-internal-comms` | `announcement-internal-comms` | `delivery-docs` | **Written 2026-09-25**; admission sources [retrieved and raw-checked the same day](#delivery-docs-new-member-the-internal-announcement-the-release-notes-guide-routes-to) | **Built 2026-09-25**, shipped in `v0.14.0`. Family by [ADR 0059](decisions/0059-announcement-internal-comms-joins-delivery-docs.md), not the `communication-docs` family that forecast it; [build report](../../bundle-builds/reports/announcement-internal-comms_v0.1.0.md) |
| `change-request` | `change-request` | `delivery-docs` | **Written 2026-09-25**; admission sources [retrieved and raw-checked the same day](#delivery-docs-new-member-by-amendment-the-change-request-two-bundles-route-to) | **Built 2026-09-25**, shipped in `v0.14.0`. Family by [ADR 0060](decisions/0060-change-request-joins-delivery-docs.md), which widens the contract's membership test; [build report](../../bundle-builds/reports/change-request_v0.1.0.md) |
| `change-log` | `change-log-governance` | `governance-docs` | **Written 2026-09-27**; admission sources [retrieved and raw-checked the same day](#governance-docs-fifth-member-the-change-log) | **Built 2026-09-28**, shipped in `v0.15.0`. Family by [ADR 0061](decisions/0061-change-log-joins-governance-docs-as-a-fifth-member.md), which gives the contract's roles list a fifth role |
| `production-readiness-review` | `production-readiness-review` | `standing-standards` | **Written 2026-09-27**; admission sources [retrieved and raw-checked the same day](#standing-standards-fifth-member-the-production-readiness-review) | **Built 2026-09-28**, shipped in `v0.15.0`. Family and classification (`tool`) by [ADR 0062](decisions/0062-production-readiness-review-joins-standing-standards-as-a-tool.md); [build report](../../bundle-builds/reports/production-readiness-review_v0.1.0.md) |
| `project-brief` | `project-brief` | `discovery-docs` | **Written 2026-09-27**; admission sources [retrieved and raw-checked the same day](#discovery-docs-reopened-third-member-the-project-brief-that-reopens-a-closed-family) | **Built 2026-09-29**, shipped in `v0.15.0`. Family by [ADR 0063](decisions/0063-project-brief-reopens-discovery-docs.md), which reopens it after ADR 0035 had recorded it as closed at two; [build report](../../bundle-builds/reports/project-brief_v0.1.0.md) |
| `deployment-plan` | `deployment-plan` | none; all nine contracts exclude it | **Researched 2026-09-27**; no spec written | **No, and it will not be.** Declined by [ADR 0064](decisions/0064-deployment-plan-is-declined.md): five public-sector sources publish it, but its content already ships in `launch-coordination-checklist` and lives on IT service change records, and admitting it would reverse `delivery-docs`' production-change exclusion |
| `executive-briefing-steering-committee-deck` | `executive-briefing-steering-committee-deck` | none; forecast by `communication-docs`, never admitted | **Researched 2026-09-27**; no spec written | **No, and it will not be.** Declined by [ADR 0065](decisions/0065-steering-committee-pack-is-declined.md): its periodic written form is what `status-report` already is, its composite exists only as a deck, and the event-driven decision paper has no family |
| `experiment-design-doc` | `experiment-design-doc` | `experimentation-docs` | **Written 2026-10-06**; admission sources [retrieved and raw-checked 2026-10-05](#experimentation-docs-founding-members-the-experiment-design-doc-and-the-experiment-readout) | **Built 2026-10-08**, shipped in `v0.16.0`. The first member of the family that [ADR 0066](decisions/0066-adopt-experimentation-docs-family-contract.md) (adopt the experimentation-docs family contract) adopts at `phase: measure`. It is built first, so that its example plans the test the readout reports; four dated notes in its spec section record five points its research settled otherwise; [build report](../../bundle-builds/reports/experiment-design-doc_v0.1.0.md) |
| `experiment-readout` | `experiment-readout-results-report` | `experimentation-docs` | **Written 2026-10-06**; admission sources [retrieved and raw-checked 2026-10-05](#experimentation-docs-founding-members-the-experiment-design-doc-and-the-experiment-readout) | **Built 2026-10-11**, shipped in `v0.16.0`. The family's second founding member, which completes `experimentation-docs`; built after `experiment-design-doc` so that its example reports that document's plan. Three dated notes in its spec section record what its research settled otherwise, and a fourth records the catalog correction it asked for; [build report](../../bundle-builds/reports/experiment-readout_v0.1.0.md) |
| `tracking-plan` | `tracking-plan` | `governance-docs` | **Written 2026-10-06**; admission sources [retrieved and raw-checked 2026-10-05](#governance-docs-sixth-member-by-amendment-the-tracking-plan) | **Built 2026-10-11**, shipped in `v0.16.0`, in the same PR as `experiment-readout`. Family by [ADR 0067](decisions/0067-tracking-plan-joins-governance-docs-as-a-sixth-member.md) (tracking-plan joins governance-docs as a sixth member), which widens the contract's membership test. Four dated notes in its spec section record what its research settled otherwise, and a fifth, in the section table, points back to one of them; [build report](../../bundle-builds/reports/tracking-plan_v0.1.0.md) |
| `north-star-metrics` | `north-star-metric-definition` | `strategy-docs` | **Written 2026-10-12**; admission sources [retrieved and raw-checked 2026-10-05](#strategy-docs-fifth-member-by-amendment-north-star-metrics), and Reforge's page read in a browser 2026-10-12 | **Built 2026-10-12**, shipped in `v0.17.0`, lean and full: the research earned the full variant, so the stop condition did not trigger. Family by [ADR 0070](decisions/0070-north-star-metrics-joins-strategy-docs-as-a-fifth-member.md) (north-star-metrics joins strategy-docs as a fifth member), which widens the contract's list of questions and places the type third in the chain, between the strategy and the roadmap. The bundle id is plural by the maintainer's ruling of 2026-10-11, and the catalog id is unchanged. Admitted on one publisher, Amplitude. The example's North Star is a weekly count of self-served outcomes, with the strategy's second-view share as its first input. The [build report](../../bundle-builds/reports/north-star-metrics_v0.1.0.md) is a floor: it captures drafting and review only, because the research ran in the spec session without the bundle's label |
| `concept-test-validation-brief` | `concept-test-validation-brief` | none assigned; `discovery-docs` admits it as written | **Researched 2026-10-05**; no spec written | **Not now.** Parked by the maintainer on 2026-10-06. Its admission rests on one vendor template whose body the main loop could not check against raw text, and the new `experimentation-docs` contract excludes a test run before anything is built |
| `problem-statement` | `problem-statement` | `discovery-docs` | **Written 2026-10-11**; admission sources [retrieved and raw-checked the same day](#discovery-docs-fourth-member-at-define-the-problem-statement-the-librarys-first-define-bundle) | **Built 2026-10-11**, shipped in `v0.16.0`. The library's first `phase: define` bundle. The phase's meaning is set by [ADR 0068](decisions/0068-define-means-problem-framing.md) (the define phase means problem framing), and the family by [ADR 0069](decisions/0069-problem-statement-joins-discovery-docs.md) (problem-statement joins discovery-docs), which gives the contract a second phase value. Two sizes by the maintainer's ruling, against the sweep's lean-only finding. A gap-fill pass after drafting added nine sources (43 in all) and routes constraints to `project-brief`; [build report](../../bundle-builds/reports/problem-statement_v0.1.0.md) |
| `shape-up-pitch` | `shape-up-pitch` | none assigned | **Researched 2026-10-11** in the Define admission sweep; no spec written | **Not now, and not a Define candidate.** It clears admission on Basecamp's own Shape Up glossary, but it carries a chosen solution: "A problem without a solution is unshaped work" (chapter 6). Most of its content already ships in `prd`, and its one distinct element is a fixed appetite. Placing it would be its own family decision. Evidence held locally |
| `lean-canvas` | `lean-canvas` | `strategy-docs`, proposed by [ADR 0083](decisions/0083-lean-canvas-joins-strategy-docs-as-a-seventh-member.md) | **Researched 2026-10-11** in the Define admission sweep. **Written 2026-10-30**; admission re-established [the same day](#strategy-docs-seventh-member-by-amendment-the-lean-canvas) on Ash Maurya's own page | **Not yet built.** Priority P2 by the maintainer's choice of 2026-10-30, issue #337 (bundle: lean-canvas). *(2026-10-30: this row read "Not now, and not a Define candidate", with admission resting on Atlassian's Confluence template and "No contract admits it cleanly". That verdict answered the `define` question only. Atlassian's site is now treated as barred under the terms rule, and ADR 0083 proposes the canvas for `strategy-docs` at `classification: utility`, pending the maintainer's read.)* |
| `opportunity-solution-tree` | `opportunity-solution-tree` | none assigned | **Researched 2026-10-11** in the Define admission sweep; no spec written | **Not admitted, and no record written.** No named source publishes it as a written document: Teresa Torres links Miro, Mural and FigJam boards, and the vendors ship boards, the shape of [ADR 0035](decisions/0035-prototype-brief-fails-the-admission-test.md). A decline record waits until someone proposes building it. Evidence held locally |
| `business-continuity-plan` | `disaster-recovery-business-continuity-plan` | `standing-standards` | **Written 2026-10-13**; admission sources [retrieved and raw-checked 2026-10-12](#standing-standards-sixth-member-the-business-continuity-plan-with-disaster-recovery-inside-it), with a gap-fill the same day on whether disaster recovery is a separate document | **Built 2026-10-14**, shipped in `v0.17.0`, lean and full, with the catalog corrections applied to both catalog files. Its [build report](../../bundle-builds/reports/business-continuity-plan_v0.1.0.md) covers the whole build: 10,284,679 weighted, $20.57, 15 agents. Family and classification (`tool`) by [ADR 0071](decisions/0071-business-continuity-plan-joins-standing-standards-as-a-tool.md) (business-continuity-plan joins standing-standards as a tool), accepted 2026-10-13 when the maintainer approved the spec PR's merge. One bundle, with the business continuity plan primary and disaster recovery as a section inside it. The bundle id is the maintainer's ruling of 2026-10-13, and the catalog id is unchanged |
| `trade-study` | `trade-study-options-analysis` | `decision-docs` | **Written 2026-10-15**; admission sources [retrieved and raw-checked 2026-10-12](#decision-docs-fifth-member-the-trade-study-in-the-technical-sense-the-business-case-guide-already-names) in the five-candidate admission sweep | **Built 2026-10-15**, shipped in `v0.19.0`, lean and full, third in the build order the maintainer set that day, with the catalog corrections applied to both catalog files. Its [build report](../../bundle-builds/reports/trade-study_v0.1.0.md) covers the whole build: 10,479,257 weighted, $20.96, 16 agents. Admitted with no contract change, under [ADR 0022](decisions/0022-adopt-decision-docs-family-contract.md)'s consequence for a further member that keeps the family's phase and size shape. Build order is the maintainer's own preference ([ADR 0041](decisions/0041-maintainer-preference-sets-the-build-order.md)) |
| `use-case-specification` | `use-case-specification` | `delivery-docs` | **Written 2026-10-15**; admission sources retrieved and raw-checked 2026-10-12, in the five-candidate admission sweep [below](#delivery-docs-new-member-by-amendment-the-use-case-specification-the-user-stories-guide-routes-to), with a gap-fill the same day on the Cockburn 2001 fully-dressed field set | **Built 2026-10-15**, shipped in `v0.19.0`, lean and full, second in the build order the maintainer set that day, with the catalog corrections applied to both catalog files. Its [build report](../../bundle-builds/reports/use-case-specification_v0.1.0.md) covers the whole build: 8,370,585 weighted, $16.74, 15 agents. Family by [ADR 0072](decisions/0072-use-case-specification-joins-delivery-docs.md) (use-case-specification joins delivery-docs), accepted 2026-10-15 when the maintainer approved the spec PR's merge. Its contract diff widens the membership test with a sixth verb, "elaborates" |
| `data-dictionary` | `data-dictionary` | `governance-docs` | **Written 2026-10-15**; admission sources [retrieved and raw-checked 2026-10-12](#governance-docs-seventh-member-by-amendment-the-data-dictionary-scoped-to-what-a-datasets-fields-mean), with a tense-boundary gap-fill two days later (2026-10-14) reversing part of the maintainer's 2026-10-13 scope reasoning | **Built 2026-10-15**, shipped in `v0.18.0`, lean and full, first in the build order the maintainer set that day, with the catalog corrections applied to both catalog files. Its [build report](../../bundle-builds/reports/data-dictionary_v0.1.0.md) covers the whole build: 8,859,179 weighted, $17.72, 16 agents. Family by [ADR 0073](decisions/0073-data-dictionary-joins-governance-docs-as-a-seventh-member.md) (data-dictionary joins governance-docs as a seventh member), accepted 2026-10-15 when the maintainer approved the spec PR's merge and the boundary drawn on subject |
| `test-strategy` | `test-strategy` | `standing-standards` | **Written 2026-10-16**; admission sources [retrieved and raw-checked 2026-10-12](#standing-standards-seventh-member-the-test-strategy-for-an-organization-or-program), with a lost admission dimension recovered 2026-10-14 and a scope follow-up 2026-10-15 | **Built 2026-10-20**, shipped in `v0.20.0`. Family and classification (`foundation`) by [ADR 0075](decisions/0075-test-strategy-joins-standing-standards-as-a-foundation.md) (test-strategy joins standing-standards as a foundation), accepted 2026-10-19 on the maintainer's delegation, which stood in for the contract read. Scoped to an organization or program, the maintainer's ruling of 2026-10-15, never a portfolio and never the per-project sense `test-plan` already ships. The contract diff was accepted without a read, and the maintainer has not yet confirmed the delegated acceptance |
| `positioning-statement` | `positioning-statement` | `strategy-docs` | **Written 2026-10-16**; admission sources [retrieved and raw-checked 2026-10-14](#strategy-docs-sixth-member-by-amendment-the-positioning-statement-as-product-direction), with a sitting-decision follow-up on 2026-10-15 | **Built 2026-10-20**, shipped in `v0.20.0`. Family by [ADR 0076](decisions/0076-positioning-statement-joins-strategy-docs-as-a-sixth-member.md) (positioning-statement joins strategy-docs as a sixth member), accepted 2026-10-19 on the maintainer's delegation, without a read of the contract diff. It widens the contract's list of questions and places the type third in the chain, between the strategy and the North Star metric. The bundle id matches the catalog id, and the catalog owner becomes `PMM / PM` by the maintainer's ruling of 2026-10-17. The spec's suggested ownership default is the agent's reasoning and was accepted without a read. Admitted on five sources (MIT, HubSpot, eCornell, Yesware, Product Marketing Alliance); Geoffrey Moore is named but not credited with admission |
| `design-brief` | `design-brief` (entry 209, added at landing on 2026-10-22) | `discovery-docs` | **Written 2026-10-22**; admission sources [retrieved and raw-checked the same day](#discovery-docs-fifth-member-at-define-the-design-brief-in-the-design-councils-sense), after the 2026-10-16 Define sweeps and the 2026-10-20 re-score | **Built 2026-10-22**, lean and full. Its [build report](../../bundle-builds/reports/design-brief_v0.1.0.md) covers the whole build: 11,563,997 weighted, $25.38, 16 agents. Family by [ADR 0079](decisions/0079-design-brief-joins-discovery-docs-at-define.md) (design-brief joins discovery-docs at define), accepted 2026-10-22 on the maintainer's delegation and confirmed by the maintainer the same day. It builds the Design Council's concept-handoff sense: the chosen problem and one concept chosen for design, handed to the people who will design it, never a specification. It ships in two sizes, lean and full, by the maintainer's ruling of 2026-10-22. The Shape Up pitch stays out at medium-low confidence, on a line the spec states. The catalog row is entry 209, not the 207 that issue #294 (bundle: design-brief) still names, because PR #305 (the opportunity statement becomes catalog entry 207) took 207 and Cagan's Product Opportunity Assessment took 208 on 2026-10-22 |
| `user-research-plan` | `user-research-plan` (entry 210, added 2026-10-23 by PR #315) | `research-docs` | **Written 2026-10-23**, and the maintainer took all ten of its recommendations on 2026-10-24; admission sources [retrieved and raw-checked 2026-10-23](#research-docs-founding-members-the-user-research-plan-and-the-user-research-report) | **Built 2026-10-24**, lean and full, default lean, the first `research-docs` member. Its [build report](../../bundle-builds/reports/user-research-plan_v0.1.0.md) covers the whole build: 14,890,444 weighted, $32.47, 16 agents. Family by [ADR 0081](decisions/0081-adopt-research-docs-family-contract.md) (adopt the research-docs family contract), accepted 2026-10-23 with no member built. It was built first, by the maintainer's ruling, so that the report's example reports against its plan. Its example plans the 2026-05 Reporting friction study that four shipped examples cite. Catalog entry 210's size moved from S to S/M at landing. The build's research weakens six sentences in this section, recorded in [dated notes](#notes-from-the-plans-build-2026-10-24) rather than rewritten |
| `user-research-report` | `user-research-report` (entry 18) | `research-docs` | **Written 2026-10-23**, in the same section, with the same rulings of 2026-10-24; admission sources [retrieved and raw-checked 2026-10-23](#research-docs-founding-members-the-user-research-plan-and-the-user-research-report) | **Built 2026-10-27**, lean and full, default lean, the second `research-docs` member, which completes the family's founding pair. Its [build report](../../bundle-builds/reports/user-research-report_v0.1.0.md) covers the whole build: 19,270,748 weighted, $38.54, 23 agents. Family by [ADR 0081](decisions/0081-adopt-research-docs-family-contract.md). It was built second, by the maintainer's ruling. Its example is the friction study's readout, titled with the PRD example's citation, "Discovery readout: Reporting friction study, 2026-05". Catalog entry 18's size moved from S/M/L to S/M at landing, and its relationships gained the plan. The build's research weakens ten places in this section, recorded in [dated notes](#notes-from-the-reports-build-2026-10-27) rather than rewritten |
| `lean-ux-canvas` | none; entry 211 is added when the bundle lands | `discovery-docs`, proposed by [ADR 0082](decisions/0082-lean-ux-canvas-joins-discovery-docs-at-discover.md) | **Researched 2026-10-29** in admission sweep 7. **Written 2026-10-30**; cadence and placement evidence [retrieved and raw-checked the same day](#discovery-docs-sixth-member-at-discover-the-lean-ux-canvas) | **Not yet built.** Priority P2 by the maintainer's choice of 2026-10-30, issue #330 (bundle: lean-ux-canvas). Sweep 7 recommended a decline at medium confidence; the maintainer chose to include the type, and ADR 0082 answers the sweep's two grounds, pending the maintainer's read |

**2026-10-14: admission sweep 6, four candidates, and the maintainer's answers the next day.** Two research workflow runs on 2026-10-14 tested `positioning-statement` (#256), `metric-tree` (#257), `messaging-framework` (#258) and `analytics-requirements-measurement-plan` (#262) against ADR 0030's admission test and against the family contracts. Of 243 returned quotations, 236 passed a re-check against raw page text. **None was ready to spec, and the maintainer ruled on all four on 2026-10-15.** The library takes on positioning only, as product direction. `positioning-statement` is specced next, in `strategy-docs` by an amendment that stops for the maintainer's read, in a single size. *(2026-10-19: it is specced [below](#strategy-docs-sixth-member-by-amendment-the-positioning-statement-as-product-direction), by [ADR 0076](decisions/0076-positioning-statement-joins-strategy-docs-as-a-sixth-member.md) (positioning-statement joins strategy-docs as a sixth member), accepted the same day on the maintainer's delegation, which places it third in the chain between the strategy and the North Star metric.)* A follow-up the same day found one practitioner source for its boundary with `product-vision`, and found sources split on whether product management or product marketing owns it, so the spec must state its product-direction placement as this library's own position. `messaging-framework` is held, with its placement flagged under [decision procedure 10](decision-procedures.md#10-a-family-or-axis-assignment-is-uncertain). The same follow-up found that neither candidate family admits it as written: one source prescribes a quarterly review, and every source the follow-up read that names an owner names product marketing or brand. `metric-tree` is parked until someone opens AIHR's KPI tree template, which sits behind a download form. The per-feature `analytics-requirements-measurement-plan` is declined by [ADR 0074](decisions/0074-analytics-requirements-measurement-plan-per-feature-is-declined.md) (the per-feature measurement plan does not ship), accepted the same day on the maintainer's delegation. Its business-scope reading clears admission and stays unswept.

**2026-10-13: a five-candidate admission sweep, and the maintainer's answers the next day.** On 2026-10-12 one
research workflow tested five queued candidates against ADR 0030's admission test and against all ten family
contracts. They were `disaster-recovery-business-continuity-plan` (#263), `trade-study-options-analysis` (#259),
`test-strategy` (#260), `use-case-specification` (#254) and `data-dictionary` (#255). The workflow returned 377
quotations, and 367 passed a re-check against raw page text as filed. A targeted gap-fill ran the same day to settle
whether a standalone, template-grade disaster recovery plan exists apart from a business continuity plan. It found
none. **All five cleared admission, and the fork in every case was family placement.** Three candidates need no
contract change: `disaster-recovery-business-continuity-plan`, `trade-study-options-analysis` and `test-strategy`.
Two need an amendment the maintainer reads first: `use-case-specification` and `data-dictionary`.

**The maintainer answered all ten resulting decisions on 2026-10-13.** The disaster recovery candidate is one
bundle, with the business continuity plan primary and disaster recovery as a section inside it. **It is specced
[below](#standing-standards-sixth-member-the-business-continuity-plan-with-disaster-recovery-inside-it) as
`business-continuity-plan`, by
[ADR 0071](decisions/0071-business-continuity-plan-joins-standing-standards-as-a-tool.md)
(business-continuity-plan joins standing-standards as a tool).** *(2026-10-14: built; its progress row above carries the date.)* `trade-study-options-analysis` goes to
`decision-docs` with no contract change, in lean and full; it is not yet specced. *(2026-10-15: specced [below](#decision-docs-fifth-member-the-trade-study-in-the-technical-sense-the-business-case-guide-already-names) as `trade-study`, with no record needed.)* *(2026-10-15: `trade-study` built; its progress row above carries the date.)* `test-strategy` goes to
`standing-standards` in its organization-wide sense, but **its lost admission dimension runs first**, and that
result decides whether a spec is written. *(2026-10-15: the dimension ran on 2026-10-14 and came back undecidable. Evidence that a test strategy is organization-wide is real but thin, evidence of a per-programme test strategy is strong and direct, and no automated fetch reached the ISO/IEC/IEEE 29119-3 clause text. No spec is written, and the scope question returns to the maintainer.)* *(2026-10-15, the maintainer's ruling: the test strategy is scoped to an organization or program, a standing strategy used across more than one project, after a follow-up found that no source scopes it to a portfolio. Its example is set at Acme, dated after the shipped test plan, so no shipped file changes. The spec is written next.)* *(2026-10-19: specced [below](#standing-standards-seventh-member-the-test-strategy-for-an-organization-or-program) as `test-strategy`, by [ADR 0075](decisions/0075-test-strategy-joins-standing-standards-as-a-foundation.md) (test-strategy joins standing-standards as a foundation), accepted the same day on the maintainer's delegation, which stood in for the contract read.)* `use-case-specification` and `data-dictionary` each wait for an amendment
the maintainer reads as a diff. The use case's `delivery-docs` amendment adds the verb "elaborates", with a
paragraph that limits what it admits. The data dictionary's `governance-docs` amendment admits only the narrow
scope, the meaning of stored fields, which reverses the maintainer's first answer. Neither is specced yet. Their
records are numbered provisionally as ADR 0072 and ADR 0073, in the order they are drafted. *(2026-10-15: both are specced below, by [ADR 0072](decisions/0072-use-case-specification-joins-delivery-docs.md) (use-case-specification joins delivery-docs) and [ADR 0073](decisions/0073-data-dictionary-joins-governance-docs-as-a-seventh-member.md) (data-dictionary joins governance-docs as a seventh member), each accepted the same day when the maintainer approved the spec PR's merge. ADR 0073 keeps the narrow scope but draws its boundary on subject rather than tense, because research on 2026-10-14 found the tense line contested; the record states the change.)* *(2026-10-15: `data-dictionary` built; its progress row above carries the date.)* *(2026-10-15: `use-case-specification` built; its progress row above carries the date.)*

**2026-10-11: the Define admission sweep, four candidates, one spec.** On 2026-10-10 the maintainer chose the problem-framing reading of the `define` phase, now recorded as [ADR 0068 (the define phase means problem framing)](decisions/0068-define-means-problem-framing.md). Two research workflows on 2026-10-11 tested the opportunity solution tree, the lean canvas, the Shape Up pitch and a problem statement against ADR 0030's admission test and against that reading, with an open search for other problem-framing documents. They read 75 addresses, and the main loop checked 311 returned quotations against raw page text, of which 310 passed. **Only the problem statement is a problem-framing document that clears admission.** The other three each carry a solution, and the opportunity solution tree also has no source that publishes it as a written document. The open search found no further type. The maintainer ruled the same day to build the problem statement with two sizes and to admit it by amending `discovery-docs`, by [ADR 0069 (problem-statement joins discovery-docs)](decisions/0069-problem-statement-joins-discovery-docs.md). The three other catalog rows stay `candidate`. *(2026-10-20: the Define re-score that [ADR 0077](decisions/0077-define-ends-with-a-chosen-concept.md) (define ends with a chosen concept) and [ADR 0078](decisions/0078-maps-canvases-and-session-records-are-templatable-through-their-written-form.md) (maps, canvases and session records are templatable through their written form) called for re-tested these four and every candidate of the two 2026-10-16 sweeps, 67 in all. The lean canvas, the opportunity solution tree and the Shape Up pitch still stay out, on grounds those two records did not retire. Two candidates return for an admission sweep at `define`: the design brief and the opportunity statement. See [`backlog.md`](backlog.md) section 4.)* *(2026-10-22: the design brief is specced [below](#discovery-docs-fifth-member-at-define-the-design-brief-in-the-design-councils-sense), by [ADR 0079](decisions/0079-design-brief-joins-discovery-docs-at-define.md) (design-brief joins discovery-docs at define), accepted the same day on the maintainer's delegation, in the Design Council's concept-handoff sense.)*

> **Note added 2026-10-17: the reading this sweep tested against is superseded.** Two further Define sweeps on 2026-10-16 (gitignored working files) also found no second bundle, and the maintainer then ruled a wider reading: [ADR 0077 (the define phase ends with a chosen concept)](decisions/0077-define-ends-with-a-chosen-concept.md) supersedes ADR 0068, so a `define` document may name one concept chosen for design but never a specification. The verdicts above that rest on "carries a solution" (the lean canvas, the opportunity solution tree and the Shape Up pitch) are therefore open again, not reversed. A re-score of the three sweeps' candidates under ADR 0077 decides which return for admission; each must still clear ADR 0030's admission test, and the opportunity solution tree's separate failure, no source publishing it as a written document, is untouched by the new reading.

**2026-10-06: one admission sweep, five measurement candidates, a new family and one widening.** On 2026-10-04 the
maintainer approved an `experimentation-docs` family and queued five candidates from a ranking of the catalog's
product-management categories. One research workflow on 2026-10-05 tested all five against ADR 0030's admission test,
against all nine family contracts and against a draft of the new contract: 24 Sonnet agents, with 405 returned
quotations re-checked against raw page text in the main loop, 382 of them passing as filed and every qualifying source
confirmed. Four cleared admission. The experiment design doc and the experiment readout fit none of the nine contracts,
and [ADR 0066 (adopt the experimentation-docs family contract)](decisions/0066-adopt-experimentation-docs-family-contract.md)
founds the family that holds them; the maintainer ruled that they ship as two bundles. The tracking plan fits
`governance-docs` on its noun and its cadence but not on its purpose phrase, which
[ADR 0067 (tracking-plan joins governance-docs as a sixth member)](decisions/0067-tracking-plan-joins-governance-docs-as-a-sixth-member.md)
widens. The north star metric definition was deferred and the concept test brief parked, and both catalog rows stay
`candidate`. *(2026-10-08: the maintainer queued the north star metric definition to follow the tracking plan; its progress row says what it needs first.)* *(2026-10-12: it is specced as `north-star-metrics`, in `strategy-docs` by [ADR 0070](decisions/0070-north-star-metrics-joins-strategy-docs-as-a-fifth-member.md), and the concept test brief stays parked.)* *(2026-10-13: `north-star-metrics` is built; its progress row
above carries the date.)*

**2026-09-27: one admission sweep, five candidates, three specs and two declines.** The maintainer queued
five candidates on 2026-09-25 from a ranked list of the next ten. One research workflow tested all five
against ADR 0030's admission test and against all nine family contracts, with no family assumed: 24 Sonnet
agents, 356 returned quotations re-checked against raw page text in the main loop. **All five cleared
admission.** What separated them was whether each is a distinct document and whether any family can hold it.
The change log and the production readiness review fit existing families as written. The project brief fits
only `discovery-docs`, which the maintainer chose to reopen. The deployment plan and the steering committee
pack are declined on duplication and family fit, not on a missing source, so neither record takes ADR 0049's
zero-source shape. Their catalog rows stay `candidate`, as ADR 0049 left its own.

**`launch-coordination-checklist`: family assigned 2026-09-20, specced 2026-09-22.** It joins
`standing-standards` as `classification: tool`, by
[ADR 0053](decisions/0053-launch-coordination-checklist-joins-standing-standards-as-a-tool.md). The
straddle that blocked it since 2026-09-11 was real (`release-notes` is `delivery-docs`, `runbook` is
`standing-standards`, and the catalog category names both), and it was resolved by ADR 0032's falsifier
rather than by the membership test: the type is **consulted at the moment of action**, which is what
`standing-standards` is for, and it carries no unit of product work, which is what `delivery-docs`
requires of every member.

**The spec is written, [below](#standing-standards-third-member-the-launch-coordination-checklist), and
the build was directed by the maintainer on 2026-09-22**, under
[ADR 0041](decisions/0041-maintainer-preference-sets-the-build-order.md)'s rule that the maintainer's
preference sets the build order.

> **One correction landed with the assignment.** The promise tag in `release-notes_meta.yaml` read
> `future:launch-checklist` while the catalog id is `launch-coordination-checklist`.
> `tools/check-bundles.py` resolves `future:` targets **by bundle id** and raises its stale-reference
> failure only when that exact id appears on disk, so building under the catalog id would have left a
> promise pointing at an id that never arrives **with the gate still green**. The tag now reads
> `future:launch-coordination-checklist`.

> **`solution-brief` is resolved, 2026-09-20: the two tags were retired rather than the type admitted.**
> `prd_meta.yaml` and `rfc_meta.yaml` both carried `future:solution-brief`, promising readers a type with
> **no catalog entry at all** - so it had never faced
> [ADR 0030](decisions/0030-templating-scope-markdown-documents.md)'s admission test and could not be
> specced or built. Open since 2026-07-21.
>
> **Retiring was chosen over adding a catalog entry, and the order is the reason.** Adding an entry first
> would admit a type on the strength of two `related_templates` tags rather than on evidence, which is the
> expensive order and the one `prototype-brief` already proved wrong: it failed 0030's test with zero named
> sources after a full research pass. A promise is not evidence. **If `solution-brief` is ever wanted, it
> enters through the front door** - a research pass, a named source, a catalog entry, then a tag - and
> pm-skills shipping `develop-solution-brief` is an argument for starting that pass, not a substitute for it.

---

## Per-type specs

### decision-docs (fourth member; the family's first Tier-2 candidate)

**spike-report** - `decision-docs`, **phase develop**, sizes **`[lean]`** (single-size), methodology
**`agile`**, catalog id `spike-research-spike-report`, aliases: `spike`, `technical investigation`.
Catalog owner: Engineer. Catalog purpose: "Time-boxed investigation to reduce uncertainty."

#### Admission, which is settled at the family level and open at the type level

**Settled: a fourth member needs no contract change.**
[ADR 0022](decisions/0022-adopt-decision-docs-family-contract.md) says so in its Consequences, in these
words: "a fourth (a spike report, a solution brief) would join under the same contract with no contract
change unless it declares a different phase or size shape." It declares neither. The
[contract](contracts/decision-docs.md) gates `phase: develop`, and `adr`, `rfc` and `sdd` all declare
exactly that; the catalog's `stage: decision` is the **catalog's** axis and not the bundle's, so it is not
in tension with anything.

> **Read the contract and the ADR together or not at all.** The contract's section 1 says "the family's
> three roles are distinct", which read alone suggests a fourth role is a problem. The record that adopted
> it says the opposite and settled the question on 2026-07-21. A previous session read only the contract,
> concluded a spike report might not be admissible, and overrode a correctly-ranked candidate on that
> basis. The contract carries the rule; the ADR carries what the rule deliberately leaves open.

**The research ran on 2026-09-11 and the answer is "barely, and it is now a maintainer decision."** Full
evidence: [`spike-report-admission-evidence.md`](spike-report-admission-evidence.md) - a 72-record fan-out
across six dimensions, merged to **68 unique sources, 57 fetched-and-verified** once four same-page pairs
were collapsed.

**Exactly one named source publishes a spike report as a written document**: Microsoft's Code with
Engineering Playbook, which states the deliverable "should be a document" and ships a fill-in template
(*Goal / Method / Evidence / Conclusions / Next Steps*), both verified against the raw markdown in the
GitHub repo. **The term's own inventors publish the opposite**: Ward Cunningham's c2 account, crediting
Kent Beck, describes the output as throwaway **code**, and Mike Cohn describes an activity, not a document.
SAFe's readable text never uses "document" or "report"; the widely repeated "documented finding" phrasing
traces to training-vendor content marketing.

**This is not the `prototype-brief` shape.** That failed with *zero* qualifying sources. This has one,
verified and current, standing against the canon. Whether one is enough is a reading of ADR 0030 - which
says "a named source", singular - and **a build must not start until the maintainer rules**, because
"whether a type is in scope at all" is on the stop-for-the-maintainer list. **The prior stated in the
paragraph this replaces was wrong**: it assumed XP's literature would supply the document, and XP's
literature is the strongest evidence against.

#### The fourth role, which is what it adds

The contract frames the family as three distinct roles: an RFC **proposes** a technical decision, an ADR
**records** one, an SDD **describes** the design that implements it. A spike report **investigates** the
question that precedes all three, and hands over evidence plus a proceed-or-not recommendation.

That boundary is not this library's invention. The paired pm-skills skill draws it in its own description:
*"For the architecture decision the spike informs, use `develop-adr` instead; for research-based
exploration, use `discover-interview-synthesis`."* The companion's cross-reference obligation (contract
section 4) therefore has a fourth edge to place correctly, and the easiest error to make is letting the
spike report drift into being an ADR with a longer preamble. **A spike report that recommends without
recording what was tried is a bad ADR; an ADR that shows its working is not a spike report.**

#### Section design

Single-size, so there is no nesting obligation and no `full` variant to diverge from. Six sections,
derived from what the practice actually produces:

| Section | What it carries |
|---|---|
| **The Question** | The uncertainty being reduced, written so it can be answered yes or no. A spike with no answerable question is a research project |
| **Time Box** | What was allotted and what was actually spent. This is the section that distinguishes a spike from open exploration, and the one most likely to be quietly dropped |
| **What Was Tried** | Approach, and what was deliberately not attempted. The scope boundary is evidence |
| **What Was Found** | Evidence-backed findings. Facts observed, separated from what they imply |
| **Recommendation** | Proceed, do not proceed, or a named next spike. Explicit, not inferred from tone |
| **What This Does Not Settle** | The open questions the spike did not close, so the next reader does not mistake a bounded answer for a general one |

The last section is a deliberate departure from the paired skill's four-part shape (question, approach,
findings, recommendation) and should be defended or dropped on research evidence like any other. The case
for it: this library's whole credibility posture is not claiming more than was earned, and a time-boxed
investigation is the document type where over-claiming is most natural, because the box closes whether or
not the question was answered.

> **The 2026-09-11 research defends it, and by a route worth reading.** The blinded gap dimension - which
> never saw this table - found that an explicit, named non-scope section is **the single most consistent
> element that real filled spike reports supply and the naive four-part shape omits**, present under four
> different headings across four unrelated projects (`## Out of scope for this spike`, `Non-goals for now`,
> `## Not covered here`, `Follow-ups (deferred, not in v1)`). Meanwhile the structure dimension found that
> **not one blank template asks for it.** Every template omits it; the good filled reports include it
> anyway. Three caveats travel with that finding (selection bias toward structured reports, a corpus
> showing signs of agent-authored drafting, and three distinct genres that must not be pooled) and they are
> recorded in [`spike-report-admission-evidence.md`](spike-report-admission-evidence.md).
>
> **The same research weakens `Time Box` as its own section.** A dedicated time-box heading appears in
> *pre-spike planning* artifacts (a Jira ticket field, a spike plan's "Deadline") and is usually **absent**
> from the report of a completed spike. If this bundle is built, that section must be argued from evidence
> or folded into Scope.

#### Metadata

| Field | Value | Why |
|---|---|---|
| `family` | `decision-docs` | ADR 0022 |
| `phase` | `develop` | Contract-gated; matches all three existing members |
| `sizes_available` | `[lean]` | Catalog `size_variant: S`. The contract admits `[lean]` for a single-size type, and exempts it from nesting, not from anything else |
| `status` | `beta` | Contract: `beta` until the maintainer judges it settled ([ADR 0055](decisions/0055-retire-the-zero-fills-disclosure.md)) |
| `methodology` | `agile` | **The first decision-docs member to declare a non-generic methodology.** The catalog says Agile/XP, and a spike is genuinely an XP practice rather than a methodology-agnostic instrument. The contract anticipated exactly this: methodology is "descriptive, not gated ... a future member is free to declare otherwise rather than have the truth bent to a rule" |
| `pairs_with` | `[develop-spike-summary]` | Verified present at `skills/develop-spike-summary/SKILL.md` in product-on-purpose/pm-skills on 2026-09-11, v2.2.0, `phase: develop`. Added to `tools/known-skills.txt` in the same change as this spec |
| `related_templates` | `[adr, rfc, sdd]` | Its three siblings |

#### Two things landing this bundle would close elsewhere

1. **`templates/adr/adr_meta.yaml` carries `related_templates: [rfc, sdd, future:spike-report]`.** The
   `future:` prefix is the gate's sanctioned way to reference an unbuilt type, and check I fails a
   `future:` reference whose target the library has since built. **So the bundle directory must be named
   `spike-report`, not the catalog id.** That matches the house rule that bundle ids are bare
   document-type handles ([ADR 0005](decisions/0005-bundle-ids-doctype-spine.md)) while catalog ids are
   long-form: `architecture-decision-record` in the catalog is `templates/adr/` on disk.
2. **The example-independence rule applies.** Contract section 5: decision-docs examples are deliberately
   independent, each a different real decision, because the family teaches the *distinction* between roles
   rather than one thread. So this bundle's example must not extend the Acme Analytics chain, and
   `tools/check-example-independence.py` enforces it.

#### Not applicable, stated so nobody applies it

**The Tier-2 active-practice test does not gate this type.** The pull-queue rule applies that bar "whenever
a Tier-2 **methodology pack** is built" - a Scrum or SAFe or XP *collection*. A single methodology-leaning
document type is not a pack, and `tier_inferred: true` on the catalog row means even the tier itself is a
derived guess rather than a maintainer's call.

---

## What a spec on this page is worth

The same as one in `buildout-specs.md`, which is to say provisional. Every per-type spec in that file was
written before its research pass, and **four of `user-persona`'s section calls were overturned by its own
research** and recorded as departures in its research log. That is the system working: the spec front-loads
judgment so the research has something specific to disagree with. Expect these to be wrong somewhere,
and expect the research logs to say where.

---

### process-docs (members three and four; build them as one job)

**`project-milestone-retrospective`** - `process-docs`, **phase iterate**, methodology **`pmbok-agile`**,
catalog id `project-milestone-retrospective`, aliases: `lessons learned`, `post-project review`,
`after-action review`. Catalog owner: PM / PgM. Purpose: "Capture lessons at project/milestone close."

**`pi-release-retrospective`** - `process-docs`, **phase iterate**, methodology **`safe-scaled`**, catalog
id `pi-release-retrospective`, aliases: `inspect & adapt (SAFe)`, `release retro`. Catalog owner: RTE / PM.
Purpose: "Reflect and improve at PI/release cadence."

#### Admission: the contract names both of them, by id

The [`process-docs` contract](contracts/process-docs.md) lists under **Likely future members, if pulled**:
`project-milestone-retrospective` and `pi-release-retrospective`, by exact catalog id. The family's axis is
`phase` with the single value `iterate`, and a retrospective at any cadence is an iterate-phase artifact by
construction. **There is no family question to answer here**, which is what makes this pair the cheapest
admission in the Tier-2 catalog.

ADR 0030's admission test still has to be met by research, and the prior is strong but is not a retrieval:
`after-action review` is a named, published US Army artifact with doctrine behind it, `lessons learned` is a
named PMBOK artifact, and SAFe publishes Inspect & Adapt. **All three have to be read, not assumed.**

#### Build them as one job, and why

They share almost their whole research base: the retrospective literature (Kerth, Derby and Larsen), the
PMBOK lessons-learned line, the SAFe Inspect & Adapt line, and the scope-and-cadence debate that separates
them. Two fan-outs over the same sources would pay for those pages twice and produce two research logs that
then have to be reconciled.

**One research pass, one contested register, two bundles.** The family goes from two members to four in a
single build, which is also the first time `process-docs` has enough members to teach its own boundary.

#### The distinction that is the whole teaching point

`sprint-retrospective-notes` already ships and looks back on **a period, on a cadence, at how the team
worked**. These two are not more of that at a larger size, and a spec that treats them that way will produce
three documents nobody can tell apart.

- **`project-milestone-retrospective`** looks back on **a bounded piece of work that has ended**. It is
  terminal: the project is over, the team may disperse, and part of the audience was not there. That is why
  its aliases are `lessons learned` and `post-project review` - the output is meant to outlive the team that
  produced it, which a sprint retro's output explicitly is not.
- **`pi-release-retrospective`** looks back on **a scaled cadence across multiple teams**. Its distinguishing
  feature is not duration but **breadth**: it reconciles findings no single team can see, which is what
  SAFe's Inspect & Adapt is built around.

The built bundle's companion already cites sources that separate these: material describing use "in a longer
iteration, release, or project retrospective", a source giving release and project retrospectives their own
chapter, and InfoQ distinguishing a sprint retrospective from a release retrospective on scope and strategic
framing. **That is inherited evidence and must be re-read at its source, not carried across.**

#### Section design, and the honest uncertainty in it

The classic five-stage retrospective shape (set the stage, gather data, generate insights, decide what to do,
close) is Derby and Larsen's, and it describes **facilitating a session**. These are **documents**, and the
document of a session is not the agenda of one. Proposed:

| Section | Both | Notes |
|---|---|---|
| **Scope and Period** | yes | What is being looked back on, and its boundaries. The section that stops these three documents blurring |
| **What Happened** | yes | The factual record, separated from interpretation |
| **What Worked** | yes | |
| **What Did Not** | yes | |
| **Lessons for Others** | `project-milestone` only | The terminal-handover section, whose whole reason for existing is a reader who was not there |
| **Cross-Team Findings** | `pi-release` only | The breadth section: findings no single team could have seen |
| **Actions and Owners** | yes | With owners and dates, or it is a feelings log |

**Expect the research to move this**, and the contract says so itself: `sizes_available` may be `[lean]`
"where the type's research shows it does not earn a second weight", and it warns to **expect pressure** on
exactly that question. The catalog says `size_variant: M` for both, and `sprint-retrospective-notes` shipped
single-size against a similar prior.

#### Metadata

| Field | `project-milestone-retrospective` | `pi-release-retrospective` |
|---|---|---|
| `family` | `process-docs` | `process-docs` |
| `phase` | `iterate` (contract-gated, single value) | `iterate` |
| `sizes_available` | `[lean, full]` **provisional** | `[lean, full]` **provisional** |
| `status` | `beta` | `beta` |
| `methodology` | `pmbok-agile` | `safe-scaled` |
| `pairs_with` | **open, see below** | **open, see below** |
| `related_templates` | `sprint-retrospective-notes`, `incident-postmortem` | same |

#### One inherited question this spec will not answer quietly

`pairs_with` is **`[]` on both built members**, and the obvious pm-skills candidate is
`iterate-retrospective`, whose own description reads: "Use at the end of a sprint, **project, or milestone**
to reflect and improve team practices."

**That description names the sprint, and `sprint-retrospective-notes` still declares `pairs_with: []`.** So
either the built bundle's empty pairing is a miss nobody has revisited, or it was deliberate and the
reasoning is not recorded where a later reader finds it. **Pairing these two while the sprint bundle pairs
with nothing would make the family internally inconsistent**, and silently pairing all three is a change to
a shipped bundle that a Tier-2 spec has no business making.

Resolve it explicitly during the build: read the skill in full, decide for all three members together, and
record the decision. `iterate-retrospective` is **not** in `tools/known-skills.txt`, so pairing also requires
verifying it and adding it per that file's own procedure.

---

### qa-docs (fourth member), and the paywall that shapes the whole build

**`test-summary-report`** - `qa-docs`, **phase develop**, sizes `[lean, full]`, methodology **`generic`**,
catalog id `test-report-test-summary-report`, aliases: `test results`, `test completion report`. Catalog
owner: QA Lead. Purpose: "Summarize test execution outcomes and quality status."

#### Demand: the library already sends readers to a document it does not ship

The strongest inbound signal in the Tier-2 catalog, and it is self-inflicted. `templates/test-plan/` ships
all of the following today:

- `test-plan_guide.md`: a "You actually need" row reading **"You need a test report."**
- `test-plan_guide.md`: a routing row, "What we found, and whether we are shipping" to **"A test report"**
- `test-plan_companion.md`: "Results, status and the verdict live in **the test report** and the test tool, not here"
- `test-plan_template-full.md`: the document is "NOT a test report (that is retrospective, written after)"

**Four places send a reader to a document this library does not have.** No `future:` tag records that
promise, which is why no gate has ever flagged it.

#### Admission, and where it is genuinely less settled than the spike report

**ADR 0030's test is met on the strongest possible evidence, with one enormous caveat.**
**ISO/IEC/IEEE 29119-3** is an international standard whose entire subject is software test documentation,
and it defines a **Test Completion Report** - which is one of this type's catalog aliases, verbatim. A named
source does not get more named than that.

**The caveat: nobody in this library has read it, and it may not be readable.** The `test-plan` bundle's
research log already establishes from its own retrieval that **29119-3 is paywalled** at ISO, IEEE and BSI,
and states plainly: "Nobody in this research read 29119-3." Under honest retrieval that source may be cited
`url-confirmed-not-read` and **nothing may be quoted from it, and no claim may rest on it alone.**

So this build's central research risk is known in advance and specific: **the most authoritative source for
this document's structure cannot be read, and its readable predecessor (IEEE 829-2008) is superseded and also
sold, with second-hand enumerations of its contents that already disagree** - the `test-plan` research found
a vendor claiming 16 sections against a different count elsewhere. A section design resting on second-hand
descriptions of a superseded standard is not a section design; it is a rumour with a table.

**The research must find the structure somewhere readable** - published practitioner templates, open-source
project QA documentation, tool-generated report formats - and say openly that the standard is cited for
existence and authority rather than for content. If it cannot, that is a finding, and a thin honest bundle
beats a confident one.

**The family question is a genuine judgment call, unlike the spike report's.** The `qa-docs` contract admits
a type whose job is to "plan, specify, or **report the verification of a product increment**", which this
does exactly. But its three named roles assign the *reporting* role specifically to the bug report ("records
one verification that **failed**"), and **[ADR 0026](decisions/0026-adopt-qa-docs-family-contract.md)
contains no fourth-member clause** - unlike [ADR 0022](decisions/0022-adopt-decision-docs-family-contract.md),
which admits a fourth `decision-docs` member in as many words. Read together, the contract admits it on its
exclusion clause and is silent in its role list. **That is close enough to be a maintainer decision rather
than a spec-writer's**, and it is flagged here rather than assumed.

#### Section design

| Section | In lean | Notes |
|---|---|---|
| **Scope and What Was Tested** | yes | What the report covers, and against which plan |
| **Execution Summary** | yes | Run, passed, failed, blocked, not run. The counting section |
| **Defects** | yes | What was found, by severity, and what remains open |
| **Quality Assessment** | yes | The judgement the numbers do not make by themselves |
| **Release Recommendation** | yes | Ship, do not ship, or ship with named conditions. Explicit |
| **Variances from Plan** | full only | What was planned and not done, and why. Most likely to be omitted, most likely to matter |
| **Residual Risk** | full only | What remains untested, and what that exposes |

**`Release Recommendation` is the load-bearing section**, and the one separating this document from a tool's
exported test run. A CI dashboard can produce every number in Execution Summary. It cannot say whether to
ship.

#### Metadata

| Field | Value |
|---|---|
| `family` | `qa-docs`, pending the admission judgment above |
| `phase` | `develop` (contract-gated) |
| `sizes_available` | `[lean, full]`, matching its three siblings and the catalog's `size_variant: M` |
| `status` | `beta` |
| `methodology` | `generic`. The catalog says methodology-agnostic and a test report genuinely is |
| `pairs_with` | `[deliver-edge-cases]` or `[]`. `test-plan` pairs with `deliver-edge-cases`; whether an edge-case skill honestly pairs with a *report* is weaker and should be argued or dropped. **pm-skills has no testing or QA reporting skill** (finding EC-4) |
| `related_templates` | `test-plan`, `test-case`, `bug-report` |

#### Two obligations inherited from the family

1. **The example chains.** Unlike `decision-docs`, `qa-docs` examples chain on one shared scenario: the plan
   schedules the case, and the case that fails produces the bug report. **This bundle's example must close
   that chain on the same feature**, reporting the run that produced the existing bug report. That is the
   most valuable thing this bundle adds, because it completes the end-to-end thread from PRD to a shipping
   verdict.
2. **The standards-recency trap is a citation obligation**, per the contract's section 3.6 and ADR 0026.
   Every member must get IEEE 829's status right - **superseded, not withdrawn** - verified at the IEEE SA
   page rather than inherited from this file or from the catalog.

---

### standing-standards (third member): the launch coordination checklist

**`launch-coordination-checklist`** - `standing-standards`, **`classification: tool`**, sizes
**`[lean, full]`** (provisional), methodology **`SRE`**, catalog id `launch-coordination-checklist`
(catalog 126), alias: `launch checklist (SRE)`. Catalog owner: Launch Coordinator / SRE. Purpose:
"Coordinate cross-team launch readiness." Contents, per the catalog: "dependencies, monitoring, comms,
rollback, sign-offs". `size_variant: M`, `rarity: rare`, `tier_inferred: true`. **The catalog row's own
source column reads "Google SRE appendix."**

#### Admission: retrieved rather than assumed, which no earlier spec on this page could say

**The family question is settled.**
[ADR 0053](decisions/0053-launch-coordination-checklist-joins-standing-standards-as-a-tool.md) assigned the
type to `standing-standards` as a `tool`, and the [contract](contracts/standing-standards.md) names it as a
member.

**The type-level test was answered by a retrieval made while writing this spec.** Every earlier spec here
carried a prior into its research pass; this one carries a source. On 2026-09-22
<https://sre.google/sre-book/launch-checklist/> was fetched and read in full. It is Appendix E of Google's
*Site Reliability Engineering* (O'Reilly, 2016), titled **"Launch Coordination Checklist"**, the catalog's
name verbatim, and it introduces itself as "Google's original Launch Coordination Checklist, circa 2005,
slightly abridged for brevity". A named source publishing the type as a written document, under the type's
own name, clears [ADR 0030](decisions/0030-templating-scope-markdown-documents.md)'s test on
[ADR 0048](decisions/0048-one-named-source-clears-the-admission-test.md)'s one-source reading with room to
spare, and it is the source the catalog already credits.

**What it contains, counted from the page's HTML rather than from a summary of it:** ten areas, 31 items.
An automated summary of the same page reported nine areas while listing ten, which is why the count was
redone by hand.

| Area | Items |
|---|---:|
| Architecture | 2 |
| Machines and datacenters | 2 |
| Volume estimates, capacity, and performance | 4 |
| System reliability and failover | 6 |
| Monitoring and server management | 5 |
| Security | 2 |
| Automation and manual tasks | 2 |
| Growth issues | 3 |
| External dependencies | 3 |
| Schedule and rollout planning | 2 |

**Four properties of that source shape the build, and each is a trap if it is missed:**

1. **It is a topic list, not a checklist in the checkable sense.** Every item is a noun phrase ("Storage
   capacity", "Monitoring the monitoring"). None is a question with a pass condition, and none has an
   owner. The research must establish whether the practice around it, chapter 27 ("Reliable Product
   Launches at Scale"), supplies the questions, owners and pass conditions, or whether this bundle
   supplies them and says so.
2. **It omits most of what the catalog row lists.** No sign-off, no go/no-go decision, no rollback (only
   "canaries under live traffic, staged rollouts"), and no launch communications. Of "dependencies,
   monitoring, comms, rollback, sign-offs", only the first two appear. Any section carrying the rest must
   be sourced elsewhere or labelled as this bundle's own contribution, the way `spike-report` labelled its
   non-scope section.
3. **It is twenty years old and describes one company's infrastructure**: "circa 2005", "N+2
   redundancy", "Don't crash mail servers by sending yourself email alerts in your own server code". The
   companion must present it as the named origin of the type, not as current practice. That is this
   family's citation hazard (contract section 3.6, "folklore presented as standard") running in reverse: a
   real historical artifact presented as a present-day standard.
4. **It is licensed CC BY-NC-ND 4.0: no derivatives.** The bundle may cite it and quote it briefly. **The
   template must not be an adaptation of its items**, and the example must not reproduce its list. This is
   the first source in the library whose licence constrains the template rather than only the citation.

**The build still records admission properly.** The research pass logs this source with a retrieval
status like any other, and looks for a second: a production or operational readiness review published as
a document. The catalog relates the type to PRR, and the SRE book's chapter on its engagement model is the
first place to look. One source suffices; a second would change the teaching.

#### The design question that is actually open: a standing checklist, or one filled per launch

The contract's membership test is "agreed once and applied every time", and its own change note concedes
the test "is genuinely ambiguous for a launch checklist, which is arguably written per launch". The two
sources in hand pull opposite ways:

- **Google's checklist is standing.** One list, reused across launches, and each launch answers it.
- **pm-skills' `deliver-launch-checklist` is per launch.** It "Creates a cross-functional pre-launch
  checklist covering engineering, design, marketing, support, legal, and operations readiness, with
  owners, dates, and go/no-go criteria", used "1-2 weeks before any significant launch".

**Proposed resolution: the template is the standing checklist, and a per-launch record is what applying
it produces.** That is the move the contract already makes for the runbook ("a runbook written for one
incident is an incident report"): the instrument is standing and its execution is per occasion. It keeps
ADR 0053's assignment honest, and it turns the pairing into a question of grain rather than of kind: the
skill produces the per-launch copy, and this template is what the copy is made from.

**If the research shows practitioners do not keep a standing launch checklist at all**, so that every
published instance is a per-launch plan, then ADR 0053's assignment is wrong on evidence and the build
**stops for the maintainer**, because that is a change in the decision rather than in the design.

**The scope question rides with it.** Google's list is engineering readiness only; the paired skill and
the catalog row both reach into communications and sign-off. The proposal below keeps engineering
readiness as the core and carries the cross-functional parts as full-only sections, so a lean fill stays
an engineering instrument. The research decides whether that line is drawn in the right place.

#### Section design

Provisional, derived from the source's shape and the catalog row, and expected to move:

| Section | In lean | What it carries |
|---|---|---|
| **Scope and Launch Classes** | yes | What counts as a launch here, and which classes of launch get the full list. A launch checklist with no scope rule is applied to everything or to nothing |
| **Roles and Sign-off** | full only | Who coordinates, and who can say no. The source names no roles; the catalog names sign-offs |
| **Readiness Checks** | yes | The load-bearing section: checks grouped by area, each a question with the evidence that answers it and the role that owns it. A table section, so it carries PRIORITY and ROW HINT guidance |
| **Launch Communications** | full only | Who must know before, at and after the launch: support, documentation, and the announcement. The edge with `release-notes` lives here |
| **Rollout and Rollback** | full only | How the launch is staged, and the condition that reverses it, stated before the launch rather than argued during it |
| **Go/No-Go Criteria** | yes | What blocks a launch, decided in advance. The difference between a checklist and a list |
| **When This Does Not Apply** | full only | Launches exempt from the list, and what they get instead. Mirrors `runbook` |
| **Review Trigger** | yes | **Contract-mandated** (section 4): a named owner and a condition, not a calendar. The obvious candidate: a launch causes an incident a check should have caught, which ties the trigger to `incident-postmortem` |

**`Readiness Checks` is where the licence bites.** The ten areas above are a reasonable taxonomy, but the
section must be built from the categories the research finds across sources, not as a restyling of one
no-derivatives list.

#### What makes it not a sibling

The companion's cross-reference section has three edges to place, and each is a likely drift:

- **Not a `runbook`.** A runbook responds to a situation that has occurred; a launch checklist prepares
  for an event that has not. Both are `tool` and both are SRE-lineage, and a launch checklist whose
  checks have turned into procedures has become a runbook.
- **Not `release-notes`.** Readiness versus announcement, a line the paired skill draws in its own
  description: "For the customer-facing announcement of what shipped, use deliver-release-notes instead."
  `release-notes_guide.md` already routes "a full launch plan and comms" here.
- **Not a production readiness review.** The catalog relates the type to PRR. Whether a PRR is a
  different document or the same instrument at a different gate is a research question, and the answer is
  a teaching point either way.

#### Metadata

| Field | Value | Why |
|---|---|---|
| `family` | `standing-standards` | ADR 0053 |
| `classification` | `tool` | ADR 0053: "an instrument you execute", sibling of `runbook` |
| `sizes_available` | `[lean, full]` **provisional** | Catalog `size_variant: M`, and both siblings ship two weights. The contract allows `[lean]` "where the type's own research shows it does not earn a second weight" |
| `status` | `beta` | Every bundle |
| `methodology` | `SRE` | The catalog's value. `runbook` declares `DevOps/SRE-lineage` and the contract leaves methodology descriptive, so pick one wording deliberately at build time rather than by copying |
| `pairs_with` | `[deliver-launch-checklist]` **provisional** | Verified present at `skills/deliver-launch-checklist/SKILL.md` on pm-skills `origin/main` (released at v2.33.0; the skill's own version is 2.2.0), `phase: deliver`, on 2026-09-22, and added to `tools/known-skills.txt` in the same change as this spec. **Honest only if the standing-versus-per-launch resolution above holds**; otherwise `[]` |
| `related_templates` | `[release-notes, runbook, incident-postmortem]` **provisional** | The type that promised it, its sibling instrument, and the document its Review Trigger fires on |

#### What landing this bundle closes elsewhere

1. **`release-notes_meta.yaml` carries `future:launch-coordination-checklist`**, the only `future:` tag
   in the tree. Check I fails a `future:` target that has been built, so the build drops the prefix in the
   same change. The bundle directory is `launch-coordination-checklist`, the id ADR 0053 fixed the tag to.
2. **The `standing-standards` contract's Members line**, which records whether the member is specced and
   built.
3. **This page's Progress table.**

#### The example

**A standing checklist belonging to a team, not a moment in a story**, which is the contract's own caveat
about chaining in this family. The natural owner is Acme Analytics' platform team, and the natural
demonstration is its checklist as it stood when the Saved Views launch consulted it, so it can chain to the
`sdd`, `test-plan` and `release-notes` examples without pretending to be a per-launch record. Contract
section 3.7 applies in full: no placeholders, illustrative figures labelled, and independent of the
template's GOOD and WEAK text. **It must not reproduce Google's items**, per the licence.

#### What the build costs, and what it settles at no extra cost

Measured, a whole bundle build is about **10M to 12M weighted token-equivalents, or $33 to $41 at API list
rates** ([`bundle-builds/INDEX.md`](../../bundle-builds/INDEX.md)), with drafting over two thirds of the
dollars because its agents resolved to Opus in both measured builds. **This build is the first whose report
can say why**, because every agent label now carries its bundle type. Projected from the two measured builds'
token counts:

- drafting resolves to **`claude-sonnet-5`**: the pin works, the measured builds ran from a drifted working
  tree, and the build costs about **$20 to $24**;
- **`claude-opus-5-5`**: the drafting agents inherit the session's model, so the pin is not being applied,
  at about **$24 to $29**;
- **`claude-opus-5`**: no longer the session model and pinned nowhere, so only a cached or resumed run could
  produce it, at about **$33 to $41**.

Run `python tools/gen-bundle-build-report.py --ingest` in Phase 6, on the machine that ran the build.

**Outcome, 2026-09-22.** Drafting resolved to **`claude-sonnet-5`**, but **none of the three causes above
was the right one.** The measured builds never ran `build-bundle.js`: the drafting scripts that session
actually executed, saved beside its transcripts, were written per bundle and pinned no model at all. This
build, the first through the committed script, cost **7,108,920 weighted token-equivalents, $14.22 at API
list rates** for its subagents ([report](../../bundle-builds/reports/launch-coordination-checklist_v0.1.0.md)),
below the $20 to $24 projected above, because every stage was smaller than in the measured builds and not
only drafting. The orchestrator's own spend is not in that figure.

---

### governance-docs (fourth member): the issue log the library already routes to

**`issue-log`** - `governance-docs`, **`classification: utility`**, sizes **`[lean, full]`** (provisional),
methodology **`generic`**, catalog id `issue-log` (catalog 152), aliases `issue register`, `issue tracker`.
Catalog owner: PM. Purpose: "Track active issues needing resolution." Contents, per the catalog: "issue,
owner, priority, status, resolution". `size_variant: S`, `rarity: common`, `tier_inferred: true`,
`relationships: [RAID]`.

#### Demand: promise debt in two shipped bundles, in the shape that found `test-summary-report`

The library sends readers to this document from both of its sibling registers, and no `future:` tag
records the promise, which is why no gate has flagged it:

- `risk-register_guide.md` and `raid-log_guide.md` each carry a chooser table with an **Issue log**
  column ("Register, RAID log, or issue log?" and "RAID log, risk register, or issue log?").
- `risk-register_template-lean.md` says the register "is NOT an issue log", and both risk-register
  templates send a materialized risk to "the issue log".
- `risk-register_guide.md`'s rubric fails a row that "has already happened" ("that belongs in the issue
  log"), and its anti-patterns say to "move materialized risks to the issue log".
- `raid-log_guide.md` routes a reader with only realized problems away from RAID: "if that is all you have,
  an issue log is enough."

**The family is settled by [ADR 0057](decisions/0057-issue-log-joins-governance-docs-as-a-fourth-member.md)**:
`governance-docs`, `utility`, the fourth member, contract to `0.2.0`. Built on the maintainer's direction of
2026-09-23 under [ADR 0041](decisions/0041-maintainer-preference-sets-the-build-order.md) (GitHub issue
#176, build-candidate 2).

#### Admission: retrieved, and the widest named-source base of any Tier-2 spec on this page

Every quotation below was checked against the source's raw text on 2026-09-23, not against a retrieval
tool's summary of it. **Four named bodies define the type by name, and one of them publishes it under an
open licence that permits adaptation.**

| Source | What it says | Licence |
|---|---|---|
| European Commission, *PM² Project Management Methodology Guide* v3.1 (Publications Office of the EU, 2023), Appendix B.9 | "The Issue Log is a register (log file) used to capture and maintain information on all issues that are being formally managed" | **CC BY 4.0** |
| PMI, *Lexicon of Project Management Terms* v5.0 (January 2026) | "issue log. A project artifact where information about issues is recorded and monitored." | PMI, personal use only |
| PMI, *PMBOK Guide* 6th edition, errata (fifth printing) | "Issue log. Described in Section 4.3.3.3." The Guide itself is sold and was not read | PMI |
| APM, glossary (read 2026-09-23) | "A log of all issues raised during a project or programme, showing details of each issue, its evaluation, what decisions were made and its current status." | not stated |
| PRINCE2 2009 glossary, reproduced with AXELOS's permission (stakeholdermap.com) | Issue register: "A register used to capture and maintain information on all of the issues that are being managed formally" | AXELOS, all rights reserved |

Readable templates from four public bodies supply the structure the standards describe: the Northern
Ireland Civil Service's *Issue Log* (whose own text says it is "based on the PRINCE2 recommended issue log"),
the Tasmanian Government's *Project Management Guidelines* v7.0 (2011) "Project Issues Register", the
Connecticut Department of Social Services' *Project Issue Log* v1.13, and Washington State OFM's issue
tracking template. **None states a reuse licence, so they are structure evidence only, never wording.**

**What was not read, and must be cited as such.** AXELOS's own manuals (PRINCE2 6th edition 2017, PRINCE2
Agile 2016, PRINCE2 7 2023) are behind a subscription and were not retrieved. ISO 21502:2020 was read only as
its official free preview: clause 3.11 defines an issue ("event that arises during a project ... requiring
resolution for the project to proceed") and the contents list "7.9 Issues management", but the clause body is
past the preview. **ISO frames a practice, not a named document, in everything readable**, and the bundle must
not claim otherwise. The UK government's Teal Book chapter on issue management refused every raw fetch and is
unquotable.

**This is the reverse of `test-summary-report`'s position.** That bundle's governing standard was paywalled and
its section design had to rest on a syllabus. Here the most structurally detailed source is openly licensed,
so the bundle can adapt PM²'s field definitions with attribution, and the paywalled standards are needed only
for existence and authority, which the Lexicon and the glossaries already supply.

#### The definition is where the sources disagree, and the template must make a team choose

The sources agree on the risk boundary, and on almost nothing else about what an issue *is*:

- **Anything that has happened and needs someone to act.** PM²: "An issue is any unplanned event related to the
  project that has already happened and requires the intervention of the Project Manager (PM) or higher
  management". PMI's Lexicon is broader still: "A current condition or situation that may have an impact on one
  or more objectives."
- **Only what breaches a tolerance.** APM's glossary: "A problem that is now breaching, or is about to breach,
  delegated tolerances for work on a project or programme." Anything inside tolerance is the day's work, not
  a logged issue.
- **Anything that could affect the project, forward-looking.** PRINCE2 7 (2023), as PeopleCert describes it:
  "anything that could affect the project". This is a change from PRINCE2's 2009 glossary ("A relevant event
  that has happened, was not planned, and requires management action"), and it pulls the concept toward the
  risk register's territory.

**The consequence for the design:** three incompatible definitions mean two people keeping the same log can
disagree about whether a row belongs in it at all. So the template's first section carries the team's own
threshold, stated, with the three positions offered as the choices they are. **That framing is this
library's**, derived from the disagreement above; no source prescribes it.

#### The change-request fork, which also bears on build-candidate 5

PRINCE2 puts a **request for change inside the issue concept**. As PeopleCert puts it: "Not all issues
result in changes" and "all changes start as issues"; the Northern Ireland template instructs that "Issues,
including those raised as changes under the project change control mechanism, should be recorded on the issue
log." PMI's PMBOK Guide instead **names two separate project documents**, each defined on its own ("The
change log is used to record all submitted change requests."), and states no rule for where they overlap: it
answers a different question from PRINCE2's rather than the opposite one. PM² keeps a separate Change Log
linked from the issue by a Traceability field.

**Proposed resolution:** the issue log records where a change request **came from** and hands it to change
control, with a cross-reference, and the companion names PRINCE2's alternative plainly. That is compatible with
both lineages and leaves the boundary with a future `change-request` bundle (GitHub issue #179) to that
bundle's own research rather than deciding it here. **If the research finds the PRINCE2 lineage dominant in
practice**, the type field carries request-for-change as a value and the companion says so.

#### Section design

Provisional, mirroring the `risk-register` shape its readers already know, and expected to move:

| Section | In lean | What it carries |
|---|---|---|
| **Purpose and Threshold** | yes | What counts as an issue here, stated as one of the three positions above, and what does not go in: risks (the register), defects (the bug tracker), approved changes (change control) |
| **Priority Scale** | yes | What each priority or impact level means, in words a second person would apply the same way. PM²'s 1-to-5 urgency and impact scales and Connecticut's Material/Non-Material split are the two published shapes |
| **Issues** | yes | **The load-bearing section.** One row per issue: ID, title and description, type, raised by and date, priority, **one named owner**, next action and target date, status. A table section, so it carries PRIORITY and ROW HINT |
| **Escalation** | yes | Who handles which priority, and the condition that moves an issue up. **In lean, unlike the risk register**, because every readable source carries escalation and APM defines an issue by a tolerance breach. Published shapes differ (a Yes/No field in PM², a status value in Connecticut, a change of decision-maker in Washington's template, a tolerance in APM's definition), and the guidance offers them rather than picking one |
| **Review and Ownership** | yes | Who keeps the log, how often it is reviewed, and when it is retired. Sankararajan and Shrivastava in PMI's *PM Network* (2012): "Issues recorded in the issues register should be discussed almost every day" |
| **Closed Issues** | full only | What each issue's resolution was, **who confirmed it**, and when. PM² defines Resolved and Closed as separate states ("Closed: This status indicates that all work is completed and verified"); Connecticut's template has Resolved and a closing date but no separate Closed state. The mirror of `risk-register`'s "Closed and Materialized Risks" |
| **Links to Other Logs** | full only | Each issue's origin and hand-offs: the risk that materialized into it, the change request it raised, the decision that closed it. PM²'s Traceability field is the published model |

**Two claims the build must not source to anyone.** The boundary with a bug tracker appears in no source
read, so it is labelled as this library's judgment. And four failure modes a brief might expect ("dumping
ground", "duplicates the ticket tracker", "used to assign blame", "never closed") were **not found in any
verified quotation**. The two that were found are an issue with no owner (ProjectManager.com: "If the issue
doesn't have an owner, it's likely never to get resolved.") and a log nobody reviews (prince2.wiki: "This
task often gets neglected when project managers get busy"). The rest are labelled or cut, never given a
citation found afterwards to justify them.

#### What makes it not a sibling

The companion's Relationships section places it against all three siblings, per the contract:

- **Not the risk register**, and the library has already said why: `risk-register_companion.md` section 8
  quotes "risk registers track conditions that might happen; issue logs address conditions that have happened".
  The new companion must agree with that section, not restate it differently. PRINCE2 7's forward-looking
  definition is the one real challenge to it, and the companion names it.
- **Not the RAID log.** An issue log stands to RAID's **I** as the risk register stands to its **R**: the
  deepened, standalone form of one quadrant. `raid-log_guide.md` already draws that system. The one
  practitioner source read on RAID (Asana) defines its issues the same way a standalone log does, so the
  choice is organizational, not definitional, and the companion says so.
- **Not the KPI dashboard.** The dashboard tracks performance against targets; an issue that the dashboard
  surfaces lands here, and the two do not share rows.
- **Not an impediment backlog.** The 2020 Scrum Guide prescribes neither: it names impediments only as
  something removed or surfaced ("Causing the removal of impediments to the Scrum Team's progress"), never as a
  written artifact. An agile team may need no issue log, and the guide's When NOT to use says so.

#### Metadata

| Field | Value | Why |
|---|---|---|
| `family` | `governance-docs` | ADR 0057 |
| `classification` | `utility` | The only value the contract allows, and correct: maintained, not executed |
| `sizes_available` | `[lean, full]` **provisional** | The catalog says `S`, but PM² separates the rules for handling issues (its Issue Management Plan, Appendix B.4) from the log itself (B.9), and a full weight carrying closure evidence and traceability is the same split both siblings make. If the research shows the rules do not earn a second weight, `[lean]` is allowed by the contract |
| `status` | `beta` | Every bundle |
| `methodology` | `generic` | All three siblings declare it, and the type is defined by PMI, PRINCE2, APM and PM² alike. The catalog's `PMBOK` would misdescribe it |
| `pairs_with` | `[]` | No pm-skills skill produces or consumes an issue log (checked against pm-skills `origin/main` on 2026-09-23); the contract says members adopt `[]` until one does |
| `related_templates` | `[raid-log, risk-register, status-report]` **provisional** | The two instruments it deepens and completes, and the report that already cites `ISS-11` |
| `aliases` | `issue register` kept; **`issue tracker` dropped, recommended** | "Issue tracker" is what a reader looking for Jira-style defect tooling types. Matching them to a project register is the collision the bug-tracker boundary exists to prevent. A build decision, argued in the research log |

#### What landing this bundle closes elsewhere

1. **The `governance-docs` contract `0.2.0`**, which lands with ADR 0057 in the same change as this spec, and
   its Members line, which records whether the member is specced and built.
2. **One sibling owes a Relationships line, and this is not optional.** Contract `0.2.0` obliges every
   member to state its position against the other members. `risk-register_companion.md` section 8 and
   `raid-log_companion.md` section 8 ("RAID log vs a standalone issue / assumption / dependency log")
   already do; **`kpi-dashboard_companion.md` never mentions an issue log** and calls the family "the three",
   so it gains its position in the same change as the bundle. *(Corrected 2026-09-23: this item said
   `raid-log`'s companion never mentions an issue log. It does, under a heading a phrase search missed.)* Whether the promise references in
   `risk-register` and `raid-log` link to the bundle, and whether `related_templates` gains it, is a build
   decision; no sibling's position changes.
3. **This page's Progress table**, and GitHub issue #176.

#### The example

**The Reporting Platform Modernization program's issue log**, which the family's shared-scenario rule makes a
hard constraint rather than a preference. `ISS-11` (the query-engine lead's departure, raised 2026-06-14,
target 2026-07-31, owner Marta Reyes, escalated to the steering group for a GBP 45,000 backfill contractor)
and `ISS-12` (staging view-list load at 620ms against a 500ms budget, raised 2026-07-10, target 2026-07-24,
owner Dana Osei) already appear across five sibling examples between them (`raid-log`, `risk-register`,
`status-report`, `kpi-dashboard`, `project-milestone-retrospective`), and the example carries them **exactly
as recorded there**. Because the scenario keeps them in the RAID log's Issues quadrant, this is the **deepened
record behind that quadrant**, dated so it can cite the RAID log and the risk register. Any further issue it
adds must be one the RAID log's working summary could plausibly omit, or one closed before that date.

**This build exercises the chaining-lens fix** that shipped in `v0.12.0` untested: the lens now reads the
sibling examples its example cites, and five of them carry these two issues.

#### What the build costs

One whole build has run through the committed `build-bundle.js`: `launch-coordination-checklist`, **$14.22
at API list rates**, every agent on Sonnet
([report](../../bundle-builds/reports/launch-coordination-checklist_v0.1.0.md)). This build is the
**second measurement, not a confirmation of a rate**. Run `python tools/gen-bundle-build-report.py --ingest`
in Phase 6, on the machine that ran the build.

**Outcome, 2026-09-23.** **8,378,876 weighted token-equivalents, $16.76 at API list rates**, 18 agents, every
one resolved to Sonnet ([report](../../bundle-builds/reports/issue-log_v0.1.0.md)). Like for like, the 15
research, drafting and review agents cost **$14.29 against `launch-coordination-checklist`'s $14.22**; the
other three were this landing's count sweep ($2.47), which the previous build did in the orchestrator, where
no report counts it. Two builds now agree within a dollar, which is two points, not a rate. Not counted in
either figure: the admission sweep run while the spec was written (16 agents, covering this type and
`definition-of-ready` together) and the orchestrator's own spend.
*(Note 2026-09-29: the linked report now reads 7,143,159 weighted, $14.29 and 15 agents. The maintainer ruled
that a report counts only the build agents, so the $2.47 sweep moved to the report's own landing-sweep line.
The figures above were the report's when this was written.)*

---

### standing-standards (fourth member): the definition of ready, a type this library has argued against

**`definition-of-ready`** - `standing-standards`, **`classification: foundation`**, sizes **`[lean]`**
(single-size, provisional), methodology **`agile-scrum`**, catalog id `definition-of-ready` (catalog 40),
alias `DoR`. Catalog owner: Scrum Team. Purpose: "Criteria a backlog item must meet to enter a sprint."
`category: Requirements`, `formality: lightweight`, `rarity: occasional`, `size_variant: S`,
`tier_inferred: true`, `relationships: [Sprint Backlog]`.

#### Demand, and the library's own position against the easy version

The `standing-standards` contract names this type first among its likely future members, and twelve files
across two bundles mention it (`definition-of-done` and `product-backlog`, counted case-insensitively on
2026-09-23; GitHub issue #178's "8 files" counted exact-case matches). **Almost every mention draws a
boundary rather than making a promise**, and three of them argue against the document:

- `definition-of-done_guide.md`: "unlike the DoD, whether a DoR should exist at all is a real, named
  disagreement in the field".
- `product-backlog_guide.md` names "The rigid Definition of Ready" as an anti-pattern, and both
  `product-backlog` templates carry the same TRAP.
- `definition-of-done_example.md`: "**Not a Definition of Ready.** The squad does not currently keep one."

**So this is a bundle for a type its own siblings warn about**, which is the `spike-report` shape: that
bundle's canon argued against writing one, and it shipped teaching the dispute. It is built on the
maintainer's direction of 2026-09-23 under
[ADR 0041](decisions/0041-maintainer-preference-sets-the-build-order.md) (GitHub issue #178,
build-candidate 4). **The family and classification are settled by
[ADR 0058](decisions/0058-definition-of-ready-joins-standing-standards-as-a-foundation.md).** The instruction of
2026-09-23 read "delivery ready"; the maintainer confirmed the same day that it meant `definition-of-ready`.

#### Admission: met at the practitioner and pattern tier, and declined by both standards that could have met it

Every quotation below was checked against the source's raw text on 2026-09-23.

| Source | What it says | Licence |
|---|---|---|
| Richard Kronfält, "Ready-ready: the Definition of Ready for User Stories going into sprint planning", *Scrum FTW* blog, 1 October 2008 | "So, the definition of Ready should be;" followed by a list. The earliest verified instance | none stated |
| The Scrum Patterns Group, "Definition of Ready" pattern, scrumbook.org (also in *A Scrum Book*, Pragmatic Bookshelf, 2019) | "Richard Kronfält apparently published the first formal description of Definition of Ready in 2008" | all rights reserved |
| Microsoft, *Code-With Engineering Playbook*, "Definition of Ready" | "Definition of Ready is the agreement made by the scrum team around how complete a user story should be in order to be selected as candidate for estimation in the sprint planning" | **CC BY 4.0** (the repository's licence file) |
| Agile Alliance, glossary | a DoR "provides the team with an explicit agreement allowing it to "push back" on accepting ill-defined features" | all rights reserved |
| Scrum Alliance, "Definition of Ready vs. Definition of Done" | "While the definition of done (DoD) is part of scrum, a definition of ready (DoR) is an external and optional tool" | not stated |

**Two sources that could have admitted it decline to.** The 2020 Scrum Guide never uses the phrase
"Definition of Ready"; its nearest sentence is "Product Backlog items that can be Done by the Scrum Team
within one Sprint are deemed ready for selection in a Sprint Planning event." And the Scaled Agile Framework's
glossary defines the Definition of Done and has no entry for a Definition of Ready. Two authors writing
on Scrum.org treat the silence as meaningful rather than an oversight: Barry Overeem (2016),
"So why isn't the Definition of Ready described in the Scrum Guide? Because it is. However not as a checklist
but as an activity: backlog refinement."; Joanna Płaskonka (2023), "Is Definition of Ready obligatory in
Scrum?" and "The answer is short: no". Both are individually authored posts, not Scrum.org policy, and are
cited that way. Both pages refuse plain HTTP clients and were read through a rendering browser.

**ADR 0030's test is met several times over** on
[ADR 0048](decisions/0048-one-named-source-clears-the-admission-test.md)'s one-source reading. One research
dimension returned "weak" by quietly substituting a stricter bar, a published fillable template, for the
rule's actual wording; its completeness critic caught the substitution, and it is recorded here so the
research log does not repeat it. **What the tier does oblige is honesty about the tier.** This family's
named citation hazard is "folklore presented as standard", and "a Definition of Ready is part of Scrum" is
that folklore exactly. The companion says in plain words that neither Scrum's nor SAFe's own text names it.

**One correction the retrieval made, recorded because the brief was wrong.** The "ready-ready" coinage is in
Jakobsen and Sutherland, "Scrum and CMMI - Going from Good to Great: Are you ready-ready to be done-done?":
"Systematic introduced the term ready-ready, to express that work from the Product Backlog has been
sufficiently elaborated to be allocated to a sprint for implementation." It is **not** in the earlier
Sutherland, Jakobsen and Johnson paper "Scrum and CMMI Level 5: The Magic Potion for Code Warriors", where
the string does not occur. The later paper's venue and year (Agile 2009) come from its filename and
bibliographies, not its text, and are cited that way.

#### The dispute, which the bundle carries rather than settles

Three positions, each sourced from raw text:

- **Against a rigid one.** Mountain Goat Software, Mike Cohn's company: "If these rules include saying that
  something must be 100 percent finished before a story can be brought into an iteration, the definition of
  ready becomes a huge step towards a sequential, stage-gate approach." Its remedy is not abolition: "Favor
  guidelines rather than rules on your Definition of Ready."
- **Against having one.** Allan Kelly (2017): a DoR "reduces agility because it breaks up process flow,
  assumes greater role specific responsibilities, introduces more wait states (delay) and potentially
  undermines business-value based prioritisation". His alternative for an item that is top priority and not
  ready: "then the first task is to make it ready". Stefan Roock, quoted by InfoQ (2014): "the Definition of
  Ready should be shrinking over time and not growing". Overeem, on Scrum.org: "Instead of using the
  Definition of Ready as a sequential, phase-gate checklist I prefer the activity of Backlog Refinement."
- **For one, kept small and shared.** Roman Pichler: "the definition of ready (DOR) is jointly owned by the
  product owner and the team", and "I recommend starting with a good-enough DOR and adapting it in the sprint
  retrospectives if and when necessary". Big Agile (2025) names the middle position outright: "a clarity
  compass, not a compliance document".

**The bundle's position is the library's usual one for a contested type: it teaches the dispute and does
not recommend a side** (the `definition-of-done` companion's section 6.1 takes the same stance). Concretely,
the template teaches a DoR **written as guidelines**, the stage-gate failure is the TRAP of its load-bearing
section, and the guide's When NOT to use is unusually prominent: the `definition-of-done` example's squad
keeps no DoR, and that is presented as a legitimate end state, not a gap.

#### The design question: `foundation` or `tool`, and the twist in the failure mode

The contract's cut is "a standard you judge against" (`foundation`) against "an instrument you execute,
usually under time pressure and often by someone who did not write it" (`tool`). **A DoR is the first.** It is
agreed by the team that applies it, consulted at refinement and sprint planning to judge whether an item is
ready, and changed deliberately and rarely. Nobody executes it under time pressure. It is the entry-side
mirror of `definition-of-done`, which is `foundation`. ADR 0058 records the counter-argument (it operates as a
checklist at a moment, which sounds like a `tool`) and why it does not carry.

**The twist, and the sharpest teaching point the family gains.** The contract names `foundation`'s failure
mode: "being agreed once and never honoured". **A DoR's documented failure is the opposite: being honoured
too hard**, enforced as a gate on items the team would rightly have taken. So the Review Trigger that section
4 of the contract mandates must fire **in both directions**: when an item the DoR blocked turns out to have
been ready enough, and when an item it let through stalls on something it should have caught. Microsoft's
playbook supplies the second direction in its own words ("Update or change the definition of ready anytime
the scrum team observes that there are missing information in the user stories that recurrently impacts the
planning"); **the first direction is this library's own contribution**, derived from the dispute above, and is
labelled that way. *(Corrected 2026-09-23 by the build's research: Big Agile states the first direction too,
"When the DoR blocks more value than it enables, it stops being a safety rail and becomes a parking brake", so
the bundle sources it rather than labelling it its own.)*

#### Sizes: single-size, because the research argues against a second weight

The contract allows `[lean]` "where the type's own research shows it does not earn a second weight", and this
is the first member where the research argues it directly. Every source that is not flatly against a DoR
wants it shorter, not longer: Roock's "The smaller the better", Pichler's "good-enough DOR", Cohn's
guidelines over rules. A `full` variant that added criteria would model the documented failure. The catalog
agrees (`size_variant: S`).

**The one thing a second weight could honestly carry** is readiness above the story: Applied Frameworks'
"A Definition of Ready for PI Planning" (2022) is a published feature-level DoR, and it is a consultancy's
extension, not a SAFe artifact. **If the build's research finds published DoRs that genuinely operate at two
levels in one document**, a full variant carrying "Readiness by Level" is the natural shape, mirroring
`definition-of-done`'s "Criteria by Level". Otherwise the companion describes feature-level readiness and the
template does not carry it.

#### Section design

Provisional, derived from the sources' shapes and the contract, and expected to move:

| Section | What it carries |
|---|---|
| **Why We Keep One** | The specific problem this team's DoR exists to fix, and the condition under which the team would drop it. A DoR that cannot say why it exists has no answer to Kelly. **This section is the library's own contribution**, the dispute carried into the template itself |
| **Scope and Ownership** | Which work items it applies to, at which moment (Microsoft ties the checklist to refinement; the Scrum Guide's "ready for selection" is sprint planning), and who owns it: jointly the product owner and the team, per Pichler and Atlassian ("created for the team, by the team") |
| **Readiness Criteria** | **The load-bearing section.** Each criterion as a guideline: the question it asks, the evidence that answers it, and whether a miss stops the item or starts a conversation. A table section, so it carries PRIORITY and ROW HINT. The TRAP is Cohn's: any criterion phrased as "100 percent" before entry |
| **When an Item Is Not Ready** | What happens to a top-priority item that misses: Kelly's "the first task is to make it ready", or an explicit exception. The pressure valve that keeps a DoR from becoming a gate, and the mirror of `definition-of-done`'s "When Work Does Not Meet It" |
| **Review Trigger** | **Contract-mandated** (section 4), and bidirectional, as argued above |

**Two structural sources, and neither may be restyled.** INVEST (Bill Wake, 2003) is the usual content of the
criteria, and Wake's article never uses the term "Definition of Ready", so it is cited as INVEST's origin
only. Pichler's "clear, feasible and testable" is a competing three-criterion shape. The template offers the
question each criterion asks, not either list; Microsoft's CC BY 4.0 playbook is the only source whose wording
may be adapted.

#### What makes it not a sibling

- **Not the `definition-of-done`.** Entry against exit. Scrum Alliance: "The definition of done refers to the
  PBI itself, while the definition of ready often refers to externalities". Kelly collapses the two in a flow
  system ("The definition of done at the end of one activity is the definition of ready for the next"), and
  the companion reports that as a real position.
- **Not acceptance criteria.** Scrum Alliance: "The definition of done applies to all work in the backlog.
  Contrast this with acceptance criteria, which are unique to each PBI". A DoR applies across items and may
  require that acceptance criteria exist; it never states them.
- **Not backlog refinement.** The Scrum Guide: "Product Backlog refinement is the act of breaking down and
  further defining Product Backlog items into smaller more precise items." Refinement is the activity; the DoR
  is what it aims at.
- **Not a stage gate.** Cooper's Stage-Gate model decides "Go, Kill, Hold, or Recycle"; a DoR with those
  outcomes has become one.
- **Not ISTQB entry criteria**, which serve the same function from a testing lineage: "The set of generic and
  specific conditions for permitting a process to go forward with a defined task". *(Corrected 2026-09-23: this
  said no source bridges the two vocabularies. The unofficial ISTQB glossary mirror lists "definition of ready"
  among the synonyms of entry criteria; the companion reports that, and that the mirror is not ISTQB's own
  site.)*

#### Metadata

| Field | Value | Why |
|---|---|---|
| `family` | `standing-standards` | ADR 0058; the contract's own forecast |
| `classification` | `foundation` | ADR 0058: a standard items are judged against, the mirror of `definition-of-done` |
| `sizes_available` | `[lean]` **provisional** | Argued above. The contract permits it on research grounds |
| `status` | `beta` | Every bundle |
| `methodology` | `agile-scrum` | `definition-of-done`'s value. The catalog says `Scrum/Kanban`, but the sharpest critics write from flow and Kanban practice, so claiming Kanban lineage would misdescribe the type |
| `pairs_with` | `[]` | The only candidate is pm-skills `iterate-refinement-notes`, whose description mentions stories moving to "ready-for-sprint" but which never mentions a definition of ready (checked on pm-skills `origin/main`, 2026-09-23). Pairing would claim something the skill does not say |
| `related_templates` | `[definition-of-done, product-backlog, acceptance-criteria, sprint-backlog]` **provisional** | The exit-side sibling, the backlog it gates, the per-item criteria it may require, and the sprint it admits items to |

#### What landing this bundle closes elsewhere

1. **The `standing-standards` contract's Members line and forecast**, which move with ADR 0058 in the same
   change as this spec. The forecast entry moves to Members rather than being deleted, as the contract's own
   change note did for the launch checklist.
2. **`definition-of-done` and `product-backlog` may link to the bundle**, a build decision. Neither changes its
   position: both keep reporting the dispute, and the DoR bundle agrees with them.
3. **This page's Progress table**, and GitHub issue #178.

#### The example

**The Reporting Squad's first Definition of Ready**, chained onto a sentence the family already wrote:
`definition-of-done_example.md` says that "if the squad adopts a Definition of Ready later, it will gate entry
into the sprint, not exit from it, and will not replace anything above." The example makes that sentence true
rather than contradicting it, so it is dated after that example's last update (2026-07-24), and whatever
prompted the squad to adopt one must agree with the Saved Views items' recorded states in the `product-backlog`
and `sprint-backlog` examples. **It must be short**, because a long example would teach the anti-pattern the
bundle warns against, and it must not reproduce Microsoft's, Atlassian's or the ScrumPLoP pattern's lists.

#### What the build costs

The third build through the committed `build-bundle.js`, after `launch-coordination-checklist` ($14.22) and
`issue-log` ($14.29 for the same 15 build agents). A single-size bundle writes one template instead of two, so
drafting should be smaller; the report will say whether it was. **The committed workflow's templates stage
writes both variants**, so a single-size build needs that stage told to write lean only, as `spike-report`'s
per-bundle script did.

**Outcome, 2026-09-23.** The workflow gained a `sizes` input before this build rather than being told per
run, and the build ran through it. **6,947,001 weighted token-equivalents, $13.89 at API list rates**, 18
agents, every one resolved to Sonnet ([report](../../bundle-builds/reports/definition-of-ready_v0.1.0.md)).
Like for like, the 15 research, drafting and review agents cost **$11.69, against $14.29 for `issue-log` and
$14.22 for `launch-coordination-checklist`**; the other three were the landing's count sweep ($2.20). The
prediction held, and by a margin: the drafting stage cost $4.71 against $5.63 and $7.15, and its templates
agent $1.24 against $1.58 and $2.62, one variant instead of two. Three builds is still three points, not a
rate. Not counted: the admission retrieval run while the spec was written, and the orchestrator's own
spend. *(Note 2026-09-29: the linked report now reads 5,846,070 weighted, $11.69 and 15 agents. The maintainer
ruled that a report counts only the build agents, so the $2.20 sweep moved to the report's own landing-sweep
line. The figures above were the report's when this was written.)*

---

### delivery-docs (new member): the internal announcement the release-notes guide routes to

**`announcement-internal-comms`** - `delivery-docs`, **`phase: deliver`**, sizes **`[lean]`** (provisional),
methodology **`methodology-agnostic`**, catalog id `announcement-internal-comms`, catalog name "Announcement /
Internal Comms", aliases `internal memo`, `launch announcement`, `Slack canvas`. Catalog owner: PM / PMM.
Purpose: "Announce changes or launches to internal/external audiences". `size_variant: S`, `rarity: common`,
`tier_inferred: true`, `relationships: [Release Notes]`.

**Scope, narrowed from the catalog's:** the **internal** announcement of a **product launch or change**,
written for people in the organization who did not do the work (support, sales, other teams, leadership). The
record of what changed, for customers or for anyone else, is `release-notes`' job, so the catalog's
"internal/external" narrows to internal, and the entry is corrected when the bundle lands.

#### Demand: one routing row, and a family forecast that lost to research

- `release-notes_guide.md`, When NOT to use: "You need a full launch plan and comms. Use a launch checklist and
  announcement; release notes are one input." The launch checklist shipped in `v0.12.0`; this is the other half
  of that sentence.
- The `communication-docs` contract named "a release announcement distinct from `release-notes`" as a likely
  member. **It does not join that family**; see the next section and
  [ADR 0059](decisions/0059-announcement-internal-comms-joins-delivery-docs.md).
- Built on the maintainer's direction of 2026-09-24 under
  [ADR 0041](decisions/0041-maintainer-preference-sets-the-build-order.md) (GitHub issue #177,
  build-candidate 3).

#### The family: `delivery-docs`, by ADR 0059

Tested on 2026-09-25 against the membership section and axis rule of all nine contracts. Two admit it:
`communication-docs`, whose membership test fits ("exists to tell people who are not doing the work what is
happening with it") but whose only axis value, `utility`, ADR 0034 justified as "maintained, periodic"; and
`delivery-docs`, whose test admits it as written ("announces a unit of product work") at a phase that describes
it honestly. **The maintainer chose `delivery-docs` on 2026-09-25.** The contract moves to `0.2.0` with the
change-request amendment below, and the chain sentence gains the internal announcement beside the release note.

#### Admission: three qualifying sources, and all of them vendor or practitioner tier

Every quotation below was checked against the source's raw text on 2026-09-25, not against a retrieval
tool's summary of it. **No standards body, government or professional institute publishes this document.**
The UK Government Communication Service's functional standard names announcements only as an activity
("Communication, in the context of this functional standard, includes announcements, media management,
coordinated communication activities"); Prosci, CIPR and the Institute of Internal Communication publish
communication *plans* and *strategies*, never the announcement itself. The `communication-docs` contract
predicted this about the whole category ("its literature is thin and vendor-dominated"), and the bundle must
say so rather than dress vendor content as practice.

| Source | What it publishes | Licence |
|---|---|---|
| Staffbase, "Organizational Announcements" (Robert Grover, 2025, updated 2026) | Defines the type by name ("An organizational announcement is an internal communication that shares important updates with employees across a company") and ships seven worked templates, one a new product launch: "These templates are a starting point, not a one-size-fits-all solution" | All rights reserved |
| GitLab Handbook, "How to make a company wide announcement" | Prescribed content, not a file: "Keep it simple, brief and summarize what is important. Cover the 5 W's", and "The majority of information should still be in the Handbook which you include links to" | All rights reserved (the handbook's own footer; GitLab's product docs are CC BY-SA, the handbook is not) |
| Jason Fried (37signals), "Deployments: How we announce new features and updates internally at Basecamp" | A named internal format for a shipped feature: a post that "explains what's new" and "points out what could be an issue", and is "wonderful for those on the front lines too" | Not stated |

**Any one of the three clears [ADR 0048](decisions/0048-one-named-source-clears-the-admission-test.md)'s bar.**
All three are all-rights-reserved or unstated, so **they are structure evidence and short quotation only; no
wording may be adapted.** Atlassian's Team Playbook play "Change Management Communication With Video" supplies
three content prompts ("What's changing?", "Why is this change important?", "How will this change impact
them?") but its deliverable is a video, so it corroborates structure and is not counted.

**Two things the research deliberately did not count.** US Army AR 25-50 publishes the memorandum, which the
catalog lists as an alias ("internal memo"), but counting it would be the library certifying itself through
its own alias. And **AR 25-50 is not a source for "bottom line up front"**: the current edition (2020, revised
2024) contains neither the phrase nor the acronym; only the superseded 2013 edition did. The principle is
sourced instead to Nielsen Norman Group ("Start content with the most important piece of information so
readers can get the main point, regardless of how much they read") and the MLA, for which a writer buries
the lede "when the newsworthy part of a story fails to appear at the beginning, where it's expected".

#### Scope: after the decision, for the people who did not make it

The sharpest boundary in the research is time. Amazon's PR/FAQ borrows the announcement's form for the
opposite purpose, before anything is built: Bryar and Carr write that "Normally, writing a press release is the
last step in launching a new product", and the PR/FAQ inverts that as a forcing function. This library ships
that device as `product-vision`'s `prfaq` format. **The internal announcement fires after the decision and
alongside the launch**, to people who must act on it.

The internal-versus-external question has **no consensus**, and the companion reports three positions rather
than picking one: one document with internal and external parts (the PR/FAQ's External and Internal FAQs);
separate documents with no stated order (GitLab's handbook keeps internal and external communication in
separate sections); and separate documents, internal first (Tomorrow People: "you should leave enough time
between your internal and external launch so you can set realistic milestones for each department"). The last
rests on one marketing agency's post, and the companion says so.

#### Section design

Provisional, one size. **The evidence argues against a second weight.** Staffbase's seven templates share one
shape (a subject line, a salutation and three or four sentences), and its two highest-stakes examples differ
from the rest by one sentence, not a section. Leadership quotes and FAQ links appear on that page only as
optional best practice ("Involve leadership", "Link to FAQs or additional resources"), never inside a template.
A full variant built from them would be the library's invention, so none is proposed.

| Section | What it carries |
|---|---|
| **Headline** | One line a reader can act on without opening the rest. Every Staffbase template opens with a subject line; the inverted-pyramid rule is NN/g's. The TRAP is the buried lede (MLA; Tomorrow People: "avoid burying the most relevant information with the generic bits") |
| **What Is Changing, and When** | The launch or change, who it applies to, and the date. GitLab's 5 W's; Atlassian's "What's changing?" |
| **Why It Matters** | The reason, in the reader's terms. Atlassian's "Why is this change important?"; the TRAP is jargon (Staffbase: "Use plain language and avoid corporate jargon"; Tomorrow People: "product marketing teams use a lot of jargon") |
| **What It Means for You** | What changes for this audience, and what, if anything, they must do and by when. Atlassian's "How will this change impact them?"; Staffbase's "what they need to do (if anything)"; Basecamp's front-line purpose |
| **Known Issues** | What could go wrong or is not done yet, so support hears it here first. Fried: a Deployment post "points out what could be an issue". Where it overlaps `release-notes`' Known Issues, **it links there rather than restating** |
| **Where to Learn More** | The source of truth and a named contact. GitLab: the detail belongs in the linked source, not in the announcement; Staffbase's "named contact" |

**Frontmatter, not sections:** the audience, the channel and the send date. They are the author's decisions,
not the reader's content. GitLab gates its company-wide channel by reach ("Is this relevant to all team
members globally?") and asks for notice "ideally 72 hours (at minimum 24 hours) in advance of a due date";
**that window is GitLab's own house rule** and the guidance labels it so rather than stating it as a norm.

**The design rule this bundle owes most to its sources: link, do not restate.** GitLab's instruction to keep
the information in the linked source is also what keeps an announcement from contradicting the release notes
or the PRD it summarizes. Every fact in it should be traceable to an upstream artifact, and the guide's rubric
checks for one that is not.

#### Failure modes: which are sourced, and which the build must label or cut

| Failure | Status |
|---|---|
| Burying the point | **Sourced**: NN/g, MLA, Tomorrow People |
| Jargon | **Sourced**: Staffbase, Tomorrow People |
| Posting it where it gets lost | **Sourced**: GitLab, "we recommend that you do not use #whats-happening-at-gitlab as a sole location for important announcements as information might get lost or muted" |
| Broadcasting instead of starting a conversation | **Sourced**: Staffbase, "internal announcements feel more like broadcasts than conversations"; Prosci's "telling plan rather than a communications plan" |
| Contradicting the release notes | **Not found in any verified source.** The library's own, and labelled so |
| No call to action | **Only the fix is sourced** (Staffbase, GitLab's "call to action"); the failure's name is the library's |
| "Announcement fatigue" | **Not found as a term.** The adjacent, sourced concept is notification fatigue (tchop: "Notification fatigue is the exhaustion and desensitisation people feel when they receive too many alerts"), and GitLab's "Be mindful of the attention economy" |

#### What makes it not a sibling

- **Not `release-notes`.** A release note is a constrained record of what changed; GitLab's own release-note
  process caps an entry at "125 words or fewer, and no images or videos", and LaunchNotes calls it a "Curated
  user-impact summary for a release, written so customers and GTM teams know what changed and why it
  matters". The announcement tells the people who did not do the work what the change means for them and what
  they must do, and links to the notes. **The line is purpose, not audience**, and it is this library's, drawn
  in the contract: `release-notes_companion.md` already recommends "the full notes internally and the lean
  notes externally", so an internal reader is not what distinguishes the two.
- **Not `launch-coordination-checklist`.** The checklist's Launch Communications section confirms that the
  right people have been told; the announcement is one of the things it confirms. Its example already names
  the communications owner (Priya Nair) for the Saved Views Sharing launch.
- **Not `status-report`.** A status report is periodic and backward-looking; the announcement is written once,
  for one event.
- **Not `product-vision`'s PR/FAQ.** Before the decision, not after it (above).
- **Not a communication plan.** Prosci's deliverable is a plan for repeated, multi-sender messages; the
  announcement is one message within such a plan, if there is one.

#### Metadata

| Field | Value | Why |
|---|---|---|
| `family` | `delivery-docs` | ADR 0059 |
| `phase` | `deliver` | The only value the contract allows, and honest: it announces a launch or change of a unit of product work |
| `sizes_available` | `[lean]` **provisional** | Argued above; the catalog agrees (`size_variant: S`), and the contract permits it |
| `status` | `beta` | Every bundle |
| `methodology` | `methodology-agnostic` | `release-notes`' value; nothing in the sources ties the type to a method |
| `pairs_with` | `[]` | No pm-skills skill produces an internal launch announcement. The nearest, `foundation-stakeholder-update`, translates one meeting's outcomes for people who were not there (checked on pm-skills `origin/main`, 2026-09-25, with the direct contents call) |
| `related_templates` | `[release-notes, launch-coordination-checklist, prd]` **provisional** | The record it links to, the checklist that confirms it was sent, and the source of its facts |
| `aliases` | `internal memo`, `launch announcement` kept; **`Slack canvas` dropped, recommended**; **never `release announcement`** | `release-notes` already carries `release announcement`. A Slack canvas is a surface, not a document type. A build decision, argued in the research log |

#### What landing this bundle closes elsewhere

1. **The `delivery-docs` contract `0.2.0`** and the dated correction in `communication-docs` section 1, both of
   which land with ADR 0059 in the same change as this spec.
2. **`release-notes`' Relationships section owes a line.** The contract obliges every member to state its
   position in the chain, and `release-notes_companion.md` has never had an internal announcement to place.
   `release-notes_guide.md`'s routing row may link to the bundle, a build decision.
3. **The catalog entry**, per [procedure 1](decision-procedures.md#1-a-catalog-call-loses-to-research): its
   purpose ("internal/external audiences") narrows to internal, and the `Slack canvas` alias goes if the build
   drops it. `docs/internal/catalog.md` and `atlas/catalog-data.json` both, then regenerate the atlas.
4. **This page's Progress table**, and GitHub issue #177.

#### The example

**The internal announcement of the Saved Views Sharing launch**, sent by its communications owner, Priya Nair.
`launch-coordination-checklist_example.md` names her in that role and says the public announcement is "Drafted
separately as a `release-notes` entry", with Support and Documentation briefed before go-live; this example is
the internal counterpart. **Every fact must be read from an existing example** (the checklist, the PRD, the
release notes, the test plan), and the link-do-not-restate rule means the example should show it doing that.

**A pre-existing contradiction the build must resolve first, not inherit.** `release-notes_example.md`
(Acme Analytics 2.4.0, 2026-06-30) lists sharing under New ("share a view with your team"), while the
launch checklist says Sharing launched later, with an exit review on 2026-07-17, "on top of the Tier 3
private-views work that shipped ahead of it", and the PRD phases sharing after a security review. **An
announcement that reads its facts from both would repeat the disagreement.** The build either corrects the
release-notes example (a history entry and a version bump on that bundle) or announces a launch whose facts
agree across every source it reads. *(Resolved 2026-09-30: the release-notes example now dates 2.4.0 to
2026-07-21, after the launch checklist. It carries a history entry and no version bump, because only the
example changed.)*

#### What the build costs

Single-size, like `definition-of-ready` ($13.89 at API list rates, $11.69 for its 15 build agents), so
drafting should cost about the same. Build through `build-bundle.js` with `sizes: ["lean"]`, every agent on
Sonnet.

**Outcome, 2026-09-25. The prediction did not hold.** **8,495,731 weighted token-equivalents, $16.99 at API
list rates**, 15 agents, every one resolved to Sonnet
([report](../../bundle-builds/reports/announcement-internal-comms_v0.1.0.md)). Drafting cost **$8.58**,
against $4.71 for `definition-of-ready` and $5.78 for `change-request` built the same evening with two
templates; almost all of the difference is cache reads (24.6M in drafting), as its example agent read widely
across the Saved Views thread to chain one launch onto four siblings. One template instead of two did not make
this build cheaper, so writing fewer variants is not by itself a predictor of cost. After the review, the
main loop found the template's GOOD examples reused the example's own scenario, which no lens flagged; they
were rewritten before landing.

---

### delivery-docs (new member, by amendment): the change request two bundles route to

**`change-request`** - `delivery-docs`, **`phase: deliver`**, sizes **`[lean, full]`** (provisional),
methodology **`generic`**, catalog id `change-request`, catalog name "Change Request", aliases `RFC (ITIL)`,
`change record`, `change ticket`. Catalog owner: Change Manager. Purpose: "Formally request and authorize a
production change". Category Release / Deployment / Runbooks, stage `release`, methodology ITIL, `formality:
formal-auditable`, `size_variant: S/M`, `relationships: [CAB review]`. **Almost every one of those catalog
calls describes the lineage this bundle does not serve**, and the entry is corrected when it lands.

#### Demand: two bundles route to it

- `bug-report_guide.md`: "**It is a request, not a defect.** If nothing promised the behavior you want, that is
  a change request." Its companion covers the boundary in section 6.
- `issue-log_template-full.md` links each issue "to a risk it materialized from, a change request it raised, or
  a decision that closed it", and its guide names a raised request for change as a reason to use the full
  weight.
- Built on the maintainer's direction of 2026-09-24 under
  [ADR 0041](decisions/0041-maintainer-preference-sets-the-build-order.md) (GitHub issue #179,
  build-candidate 5).

#### The family: `delivery-docs`, by amendment (ADR 0060)

**No contract admitted this type as written, and that is the finding that shaped everything else.** Tested on
2026-09-25 against all nine membership tests, a per-occasion change request fitted none; `governance-docs`,
the natural-looking home, excludes "An event-driven or phase-bound artifact". The maintainer chose to widen
`delivery-docs` with a fifth verb: the family's artifacts now define, decompose, verify, **change**, or announce
a unit of product work. The contract's section 1 states what the verb does not admit (a change to a running
production system; the standing change log). See
[ADR 0060](decisions/0060-change-request-joins-delivery-docs.md), which also records the three rejected
options.

#### Which change request: the project and product baseline

Two lineages share the name, and the readable sources support them about equally:

| Lineage | What changes | Readable sources |
|---|---|---|
| **Baseline** (served) | Something agreed about a unit of work: scope, requirements, schedule, cost | PMI's Lexicon; the PMBOK Guide 6th edition errata; PRINCE2 (via prince2.wiki); APM; the European Commission's PM² guide and Change Request Form; the CDC Unified Process form; GSA's M3 Playbook form |
| IT service (the neighbour) | A running system | NIST SP 800-128 Appendix E and SP 800-53 CM-3; the ITIL glossary; Prairie View A&M's form; IT Process Wiki's RFC checklist |

**The maintainer chose the baseline lineage on 2026-09-25**, because the library's routing already used it (a
bug-report reader asking for behavior nothing promised is asking to change what the PRD and acceptance criteria
agreed) and because its audience is product management and software delivery, not IT operations. The IT
service lineage stays a named neighbour: its vocabulary (standard, normal and emergency changes, a change
authority, a back-out plan) is described in the companion and does not appear in the template.

**The two lineages share a skeleton**, which is why one bundle can name both honestly: an identifier, a
requester, a description of the change, a reason, an impact assessment, and a decision by a named authority.
**They diverge on everything else**: the IT forms add configuration items, security impact and rollback; the
baseline forms add scope, schedule and cost impact against an agreed plan.

#### Admission: retrieved, and the widest named-source base on this page

Every quotation below was checked against the source's raw text on 2026-09-25. Three sources were reached only
through the Internet Archive, because their live pages now return 403 or 404, and **the research log must cite
the archived copy that was actually read**, not the dead URL.

| Source | What it says or publishes | Licence |
|---|---|---|
| PMI, *Lexicon of Project Management Terms* v5.0 (January 2026) | "A formal proposal to modify a document, deliverable, or baseline." | PMI, personal use only |
| PMI, *PMBOK Guide* 6th edition, errata (fifth printing) | "The change log is used to record all submitted change requests." The Guide itself is sold and was not read | PMI |
| European Commission, *PM² Project Management Methodology Guide* v3.1 (2023) | A change request asks to "amend an aspect of the agreed baseline of a project", and "can be formally submitted via a Change Request Form, or can be identified and raised during meetings as a result of decisions, issues or risks"; "There are four possible decisions: approve, reject, postpone or merge the change request" | **CC BY 4.0** |
| PM² Change Request Form template v3.0.1 (docx) | Four narrative sections, "Current Situation", "Desired Situation", "Impact or Risks" and "Out of Scope", and "Once the change request is logged into the Change Log, then this form is updated with the assigned Change ID and the form is archived" | **Not stated in the file**; the guide's CC BY 4.0 does not automatically cover it |
| CDC Unified Process, *Change Request Form (example)* (2009, archived copy) | Three sections by actor: "SUBMITTER - GENERAL INFORMATION", "PROJECT MANAGER - INITIAL ANALYSIS", "CHANGE CONTROL BOARD - DECISION" | Not stated; presumptively a US government work, unconfirmed |
| US GSA, *M3 Playbook Change Request Form Template* (docx, read from its XML) | "Requirements Change Request Information" and "Change Control Board Approval Information" | Not stated |
| APM glossary and "What is change control?" | A change request: "A request to obtain formal approval for changes to the approved baseline"; and "Change requests may arise as a result of issues" (the second is on the change-control page, not the glossary) | APM, not stated |
| PRINCE2, via prince2.wiki | A request for change: "It is a proposal for a change to a baselined product"; the change authority is "A person or group to whom the project board may delegate responsibility for reviewing and approving change requests or off-specifications" (the second is on the change-authority page) | AXELOS, all rights reserved |

**PM² is the adaptable source**, as it was for `issue-log`: its guide is CC BY 4.0, so its definitions and
process wording may be adapted with attribution. Its form's field layout is structure evidence only until a
licence covering the docx is found. HHS's EPLC Change Management Plan (2008, archived copy) is a useful
outlier rather than a third form: it gives one field list for "THE PROJECT'S CHANGE REQUEST FORM AND CHANGE
MANAGEMENT LOG" together, and the companion reports it as the case where the two are merged.

**What was not read.** The PMBOK Guide body, ISO 21502:2020 beyond its catalog page, AXELOS's own PRINCE2 and
ITIL manuals, and the ITIL 4 Change Enablement practice guide. ITIL's change types are sourced only to
PeopleCert-copyrighted Foundation training material redistributed by a training provider, and "normal change"
is absent from that glossary; since the template carries no ITIL vocabulary, none of this is load-bearing.

**Retrieval notes for the build's research**, because several of these sources cannot be read at the address
a search returns, and a research agent that tries the live URL will drop them:

| Source | Read from | How |
|---|---|---|
| CDC UP Change Request Form (example) | <http://web.archive.org/web/20240601190446/https://www2a.cdc.gov/cdcup/library/templates/CDC_UP_Change_Request_Form_Example.doc> | Live site returns 404. A 1997-format `.doc`: extract with `antiword`, not a text decode |
| HHS EPLC Change Management Plan | <http://web.archive.org/web/20260226151438/https://www.hhs.gov/sites/default/files/ocio/eplc/EPLC%20Archive%20Documents/07%20-%20Change%20Management%20Plan/eplc_change_management_plan_template.doc> | Live returns 403. `antiword` |
| CDC UP newsletter on change management (2009) | <http://web.archive.org/web/20250418071852/https://stacks.cdc.gov/view/cdc/77284/cdc_77284_DS1.pdf> | Live returns 403. Practice narrative only; **not** the form |
| PM² Change Request Form v3.0.1 | <https://www.pm2.center/wp-content/uploads/2022/02/21.I.PM2-Template.v3.Change_Request_Form.ProjectName.dd-mm-yyyy.vx_.x-1.docx> | The `pm2.eu` landing page carries no fields; read the docx's `word/document.xml` |
| PM² Methodology Guide v3.1 | <https://www.pm2alliance.eu/wp-content/uploads/2024/02/pm%C2%B2-project-management-methodology-NO0523520ENN.pdf> | `pdftotext` without `-layout` |
| GSA M3 Playbook Change Request Form | <https://ussm.gsa.gov/assets/files/M3-Playbook-Change-Request-Form-Template.docx> | Read `word/document.xml`; a text decode of the docx fails every quote |
| PRINCE2 change authority | <https://prince2.wiki/people/change-authority/> | The definition is here, not on `/practices/issues/` |
| APM, change requests arising from issues | <https://www.apm.org.uk/resources/what-is-project-management/what-is-change-control/> | Not on the glossary page |
| DORA 2019 report | <https://dora.dev/research/2019/dora-report/2019-dora-accelerate-state-of-devops-report.pdf> | The CAB finding and "there is still an important role for the CAB" |

The sweep's full returns and the main loop's re-check are kept, untracked, at
`_local/research/2026-09-25_admission-sweep-2/`.

#### The change-request fork, answered

`issue-log`'s spec left one question to this bundle's research: **if the PRINCE2 lineage (a request for change
is a kind of issue) proved dominant, the type field would carry it.** It is not dominant. PRINCE2 files a
request for change as one of "five types of issues"; PMI names a separate change log, and PM², the CDC form and
GSA's form all treat the request as its own document. **So the request records where it came from**: PM²'s own
list, "decisions, issues or risks", plus a meeting or a stakeholder, with a link back to the issue log entry
when there is one. That is compatible with the issue log's existing Links to Other Logs section and needs no
change to it.

#### Defects: where the government forms and this library disagree

Two of the readable forms **fold defects in**: GSA's "Type of Change" offers New Requirement, Change to Existing
Requirement and Defect, and the CDC form's type is Enhancement or Defect. This library's `bug-report` guide draws
the opposite line, and one named practitioner draws it too (Ian Devlin: a defect is "something is wrong with the
delivered code", a change request covers "things that are new and additional to what was delivered"). **The
template follows the library's line** and offers no Defect type; the companion reports that two public-sector
forms do, so a reader from that background is not told they are wrong.

#### The agile position, and who the bundle is for

The 2020 Scrum Guide routes change through the backlog: "Those wanting to change the Product Backlog can do so
by trying to convince the Product Owner." The Agile Manifesto ranks "Responding to change over following a
plan". **A team working that way needs no change request**, and the guide's When NOT to use says so first.
The bundle is for work where an agreed baseline carries weight outside the team: a fixed-price contract
("fixed-price contracts usually require a detailed and exact description of the subject matter of the contract
in advance", Wikipedia's "Agile contracts"), a regulated product (an Agile Alliance experience report maps
design changes onto "Change control procedures" in an FDA-regulated project), or a budget and scope a steering
group signed off. Two sharper agile claims (a Scrum.org forum thread, and a remark attributed to Mary
Poppendieck that needing a change request is itself a warning sign) were found only as search snippets and
**must not be quoted**.

#### Section design

Provisional, mirroring the CDC form's three actors and PM²'s four decisions, and expected to move:

| Section | In lean | What it carries |
|---|---|---|
| **The Request** | yes | What should change, in one sentence, and what it changes: which agreed artifact and version (the PRD, the acceptance criteria, the plan). Requester, date, and where it came from (decision, issue, risk, meeting). PM²'s "Current Situation" and "Desired Situation" are the published shape |
| **Why** | yes | The reason, and **what happens if it is not made**: NIST's sample asks for the expected impact of not making the change, and PM²'s process asks the assessor to "consider the impact of not implementing" it. Both lineages ask, which is why it is in lean |
| **Impact** | yes | On scope, schedule, cost, quality and risk, each stated or marked "none". PM²'s baseline list and the CDC form's hour, duration, schedule and cost impact are the published shapes. A table section, so it carries PRIORITY and ROW HINT |
| **Decision** | yes | Approve, reject, postpone or merge (PM²'s four), by whom, on what date, with any conditions. **One named decider**; the PMI Lexicon's change control board and PRINCE2's change authority are the two published forms of that authority |
| **Options Considered** | full only | Alternatives to the change as requested, including a smaller version and doing nothing. The CDC form's Recommendations and the PM analysis role |
| **Out of Scope** | full only | What this request does not change, so an approval is not read as broader than it was. PM²'s form carries it as a section of its own |
| **Implementation and Traceability** | full only | What was updated when the change was approved (which artifact, which new version), the change log entry, and links to the issue, risk or decision it came from. PM²'s form archives itself once the change is logged |

**What stays out of the template:** a back-out plan, configuration items, change types and a CAB. They belong
to the IT service lineage, and the companion places them there.

#### What makes it not a sibling

- **Not a `bug-report`** (above). A defect fails an agreement; a change request alters one.
- **Not the `rfc` bundle.** ITIL abbreviates a request for change as RFC; this library's `rfc` is a request for
  comments, a technical design proposal, in the IETF lineage ("Request for Comments"). **The guide names the
  collision on its first line**, and the catalog alias `RFC (ITIL)` is dropped, recommended.
- **Not the `issue-log`.** An issue may raise a change request; the request is not an issue in this library's
  convention (above), and it links back.
- **Not an `adr`.** An ADR records a technical decision already made; a change request asks an authority to
  decide on altering an agreed baseline.
- **Not a change log.** PMI: "The change log is used to record all submitted change requests." The log is a
  standing register, a separate catalog candidate (`change-log-governance`) that `governance-docs` admits as
  written; this bundle is one request.
- **Not IT change enablement.** The neighbour, above. DORA's 2019 report is the reason the companion does not
  present a change board as an unqualified good: it found that approval by "an external body such as a change
  advisory board (CAB) or a senior manager" had "a negative impact on software delivery performance", while
  holding that "there is still an important role for the CAB". **That finding is about production changes**,
  and the companion must not stretch it to a project change board.

#### Failure modes: mostly unsourced, and the build must say so

The research found **no verified source** for the failure modes a brief would expect: scope creep through
informal change (PMI's article was not read), requests that never get a decision, and change boards that
rubber-stamp project changes. Each is labelled as the library's own judgment or cut. **One tempting source
must not be used**: Prosci's "change fatigue" describes people absorbing too much organizational change, not a
flood of change requests.

#### Metadata

| Field | Value | Why |
|---|---|---|
| `family` | `delivery-docs` | ADR 0060 |
| `phase` | `deliver` | The only value the contract allows; a baseline change is raised while a unit of work is being delivered |
| `sizes_available` | `[lean, full]` **provisional** | The catalog says `S/M`. PRINCE2's request is light (the products to change and a justification) and the CDC form carries three actors' sections, the same split the other members make |
| `status` | `beta` | Every bundle |
| `methodology` | `generic` | PMI, PRINCE2, APM and PM² define it alike; the catalog's `ITIL` describes the lineage not served |
| `pairs_with` | `[]` | No pm-skills skill produces or consumes a change request (checked on pm-skills `origin/main`, 2026-09-25, with the direct contents call) |
| `related_templates` | `[prd, acceptance-criteria, bug-report, issue-log]` **provisional** | The baseline it changes, the agreement it alters, and the two bundles that route to it |
| `aliases` | `change record` kept; **`RFC (ITIL)` and `change ticket` dropped, recommended** | `RFC` collides with a shipped bundle; "change ticket" is service-desk vocabulary for the lineage not served. A build decision, argued in the research log |

#### What landing this bundle closes elsewhere

1. **The `delivery-docs` contract `0.2.0`**, which lands with ADR 0060 in the same change as this spec.
2. **`bug-report` and `issue-log` may link to the bundle**, a build decision; neither changes its position.
   **`rfc`'s guide owes one line** naming the ITIL collision from its side, because a reader who searches "RFC"
   today finds only the design proposal and nothing tells them there is another meaning.
3. **The catalog entry**, per [procedure 1](decision-procedures.md#1-a-catalog-call-loses-to-research):
   purpose, owner, category, methodology, relationships and aliases all describe the IT service lineage. Both
   `docs/internal/catalog.md` and `atlas/catalog-data.json`, then regenerate the atlas.
4. **This page's Progress table**, and GitHub issues #179 and #180.

#### The example

**A change request against the Saved Views PRD**, chained onto the delivery-docs scenario rather than the
governance one. `prd_example.md` (doc version 0.3.0, owner Priya Nair) lists as a non-goal "Scheduled delivery
of a view by email or Slack. Out of scope now; likely a fast follow." A request to bring it into scope, and a
decision to postpone it to a follow-on release, is exactly the case the type exists for, and it agrees with the
`release-notes` example, which ships no scheduled delivery. The request must be dated inside the PRD's life
(created 2026-06-12) and must not contradict any later sibling.

**One constraint from the governance side.** `issue-log_example.md` states that neither ISS-11 nor ISS-12 raised
a change request ("No request for change; no decision"), so this example must not attach one to either.

#### What the build costs

Two sizes, like `issue-log` ($16.76 whole, $14.29 for its 15 build agents). Build through `build-bundle.js`
with every agent on Sonnet.

**Outcome, 2026-09-25.** **7,203,075 weighted token-equivalents, $14.41 at API list rates**, 15 agents, every
one resolved to Sonnet ([report](../../bundle-builds/reports/change-request_v0.1.0.md)): research $6.01,
drafting $5.78, review $2.62. The review found 15 findings, one blocking (a sentence that credited ITIL 4's
glossary with a term its own log records it lacks); the main loop found two more that no lens flagged, the
templates' GOOD examples reusing the example's scenario and the example repeating the thread's known sharing
contradiction. Not counted: the admission sweep run while the spec was written, and the orchestrator's own
spend.

---

### governance-docs (fifth member): the change log

**`change-log`** - `governance-docs`, **`classification: utility`**, sizes **`[lean, full]`** (provisional),
methodology **`generic`** (provisional; corrects the catalog's `PMBOK/ITIL`), catalog id
`change-log-governance` (catalog 154 in [`catalog.md`](catalog.md), verbatim at
[`atlas/catalog-data.json`](../../atlas/catalog-data.json)), catalog name "Change Log
(governance)", aliases (catalog) `change register`, `change control log`. Catalog owner: PM / Change
Manager (open question, not source-confirmed; see Catalog corrections). Catalog purpose: "Track requested
and approved changes to baselines." Catalog contents: "change, requestor, impact, decision, date."
Catalog `stage`: governance. Catalog `formality`: lightweight. Catalog `rarity`: common. Catalog
`size_variant`: S. Catalog `relationships`: `[Change Requests]`. `tier: 2`, `tier_inferred: true`,
`must_have: false`, `built: false`, `state: candidate`.

**The bundle id is `change-log`, not the catalog id verbatim, and that is a design choice this spec makes
rather than inherits.** See "Deciding the bundle id" below.

#### Demand: the sibling that names it and defers it

Two shipped bundles already point at a standing change log without building one, and the deferral is
recorded, not implied:

- `change-request_companion.md:369-373` (`change-request`, the per-occasion document): "**Change request
  vs. the change log.** The request is not the log; PM²'s form is archived once logged into one
  [[8]](#ref-8), and the PMBOK errata describes the log as the register that collects submitted requests
  [[2]](#ref-2). HHS's EPLC program merges the two, a documented alternative rather than an error
  [[11]](#ref-11). A standing change log, if this library ever builds one, is a `governance-docs`
  candidate, not a variant of this bundle." *(As it stood 2026-09-27. The change-log landing rewrote
  this paragraph on 2026-09-28, now `change-request_companion.md:373-378`: HHS "shares one field list
  between them but keeps two artifacts", and the closing sentence names the built bundle.)*
- `change-request_template-lean.md:45`: "This document is not the change log; it feeds one."
- `change-request_template-full.md:23,242-254`: the full template's WHY and GOOD text both name the log as
  the request's destination once decided.
- `change-request_guide.md:58,76`: routes a reader to the full size "when the project keeps a change log
  this request must feed into cleanly," and the rubric's row 8 grades whether a filled request "names the
  change log entry (or states none is kept)."
- `issue-log_companion.md:60,358-361` and `issue-log_template-full.md:224-226,244` and
  `issue-log_guide.md:51-55`: `issue-log`'s own Links to Other Logs boundary names "a separate change log
  for submitted change requests" as the PMI convention it records against, and its TRAP line warns against
  "duplicating the risk register's or **change log's** own detail" instead of linking to it.
- `docs/internal/contracts/delivery-docs.md:13`: "it does not admit the standing register of such requests
  (a change log), which is a `governance-docs` instrument if it is ever built."
- `docs/internal/decisions/0060-change-request-joins-delivery-docs.md:84-86,105-106`
  (**ADR 0060, change-request joins delivery-docs**): considered and rejected building the log instead of
  the request ("it builds a different document from the one three bundles route to"), and states three
  times that `governance-docs` "admits a standing register as written" if the type is ever built.
- `atlas/catalog-data.json:3903-3926` *(2026-10-14: the `change-log-governance` entry now sits at 3921-3949, after later landings grew the file.)*: the candidate has carried `state: "candidate"` in the catalog since
  before either sibling shipped.

#### Deciding the bundle id: `change-log`, keeping `change-log-governance` as the catalog id

**Chosen: bundle id `change-log`.** Three reasons, weighed against the one real risk.

1. **Every other `governance-docs` member's bundle id is a bare type name, with no family qualifier.**
   `risk-register`, `raid-log`, `kpi-dashboard` and `issue-log` (**ADR 0057**, issue-log joins
   governance-docs as a fourth member) all drop any "-governance" or "-register" suffix the catalog's own
   compound naming might invite. Keeping `change-log-governance` as the bundle id would be the only member
   of this family to carry a family qualifier in its own directory name, for no mechanical reason.
2. **The library has already shortened a compound catalog id for a Tier-2 bundle twice.** `spike-report`
   ships under `spike-research-spike-report`'s catalog entry, and `test-summary-report` ships under
   `test-report-test-summary-report`'s. Both keep the compound string as the catalog id and ship the
   natural, shorter descriptive phrase as the bundle id. `change-log-governance` is the same shape: a type
   name plus a parenthetical qualifier the catalog added to disambiguate a candidate row, not a name a
   reader would search for whole.
3. **No mechanical collision exists either way.** `tools/mcp_server.py:371-384`'s `search_templates`
   matches a query against `b["id"].lower()` exactly or as a substring of the bundle's own joined
   `aliases`. A query `changelog` does not equal `change-log` (the hyphen differs) and is not a substring
   of this candidate's catalog aliases (`change register`, `change control log`); a query `change-log`
   does not appear inside `release-notes_meta.yaml:18`'s alias list either. `tools/check-bundles.py`
   resolves `future:` tags and cross-references by exact bundle id, which this decision does not touch.
   Checked directly against both files on 2026-09-27; neither normalizes hyphens.

**The risk, named rather than hidden.** `release-notes` carries alias `changelog` (`release-notes_meta.yaml:18`),
and `release-notes_companion.md:132-137` already draws the boundary from its own side: "A **changelog** is
a portable, permanent, structured record of every notable change, maintained with the project (Keep a
Changelog)... **Release notes** are a curated, often customer-facing summary for a specific release." A
plain-English reader who has that sentence in mind and then meets a bundle named `change-log` is one
short step from the wrong artifact, even though no string collides. **This is exactly the near-miss ADR
0059 (announcement-internal-comms joins delivery-docs) found for its own alias `release announcement`
against `release-notes`**, and that record's answer was to fix it in the build, not to avoid the name. This
bundle's guide and companion must name the collision on their first line, the way `change-request_guide.md`'s
first line already names the `rfc` collision, and `release-notes_guide.md` gains one routing line from its
own side (see What landing this bundle closes elsewhere). The catalog id `change-log-governance` is
unchanged, so any future `related_templates` or `future:` reference written against the catalog id still
resolves once the bundle directory is checked against it.

#### Admission: five independent named bodies, one already read by a sibling bundle

Every quotation below was checked against the source's raw text on 2026-09-27, in the main loop's re-check of
the admission sweep (`_local/research/2026-09-27_admission-sweep-3/`, gitignored). Three named standards
bodies and two named government bodies each define or ship the type by name, clearing
**ADR 0048** (one named source clears the admission test) with room to spare.

| Source | What it says or ships | Licence |
|---|---|---|
| PMI, *PMBOK Guide* 6th edition, errata (5th printing) | "The change log is used to record all submitted change requests." | PMI, hosted openly, no login wall |
| European Commission / PM² Alliance, *PM² Project Management Methodology Guide* v3.1, Appendix B.7 | "A Change Log is used to document, monitor and control all project changes." Ships an actual 17-field template across four groups (Identification and Description, Assessment and Action, Approval, Implementation); one of its eight Status values, in the Identification and Description group, "Waiting for approval," was independently re-checked against the live PDF on 2026-09-27 and passes | **CC BY 4.0** ("Document licensed under CC BY 4.0 license," raw-checked) |
| PM² Alliance, pm2.eu Artefacts listing | "template for Change Log document," "Free, downloadable and easy to edit" | Not independently confirmed on this listing page; the Guide it is drawn from is CC BY 4.0 |
| Association for Project Management (APM), UK chartered body, glossary | "A record of all proposed changes to scope" (entry name "Change register (or log)"; a separate entry, "Change log", reads "A record of all project changes: proposed, authorised, rejected or deferred." Entry names corrected 2026-09-28 by the build's research); independently confirms the register/log naming equivalence this candidate's own alias claims | Not stated |
| Connecticut Department of Social Services, Enterprise PMO, *Project Change Log* v1.1 | "Also known as Project Change Register." Ships a fielded, versioned, 11-column template | Not stated; presumed public-sector work product |
| US Department of Health and Human Services, EPLC, *Change Management Practices Guide* | "All projects, regardless of type or size, should maintain a change log and regularly manage requested changes." | US federal government work, presumptively public domain |

**Retrieval note for the build's research.** `hhs.gov` returns HTTP 403 to both `WebFetch` and
`rawcheck.py`; the HHS quotations above and below were read from the Internet Archive's `id_` raw copy
(`https://web.archive.org/web/2025id_/<hhs.gov URL>`), and the research log must cite
the archived copy actually read, the same convention `change-request`'s own spec already models
(`tier2-specs.md:1360-1373`). **One sentence in that same HHS folder is usable only as a fragment**:
"A submitter completes a CR Form and sends the completed form to the Change Manager" wraps a table-cell
break in the `.doc` extraction, and only "A submitter completes a CR Form and sends the" passed the
raw-text check. Do not quote the full sentence; either use the fragment or use the passing companion
quote below instead.

**What was not read, or does not admit the type.** The PMI *Lexicon of Project Management Terms* v5.0 has
no standalone "change log" entry; a full-text search returned zero hits, so the Guide's body defines the
term and the Lexicon does not, a factual gap rather than a boundary claim. ISO 21502:2020 is a commercial
standard and was not retrieved. The CDC Unified Process newsletter (`stacks.cdc.gov`) returns HTTP 403 and
and was not recovered from an archive copy in this pass, so its sentence, word for word the same claim the
HHS Practices Guide makes above, is not usable; cite HHS, not CDC. The ITIL glossary
mirror (IT Process Wiki) is rawcheck-passed but does not admit "change log" itself; see Boundaries below.

#### Structure: PM²'s four groups as the backbone, cross-checked by two independent government templates

**PM² Appendix B.7** (17 fields, four groups): Identification and Description (ID, Category, Title,
Description, Status, Requested by, Date Identified); Assessment and Action (Action Details, Size,
Priority, Target Delivery Date); Approval (Escalation, Decision, Decided by, Decision Date); Implementation
(Actual Delivery Date, Traceability and Comments). *(Corrected 2026-09-28: this placed Target Delivery Date in
the Approval group; Appendix B.7 places it in Assessment and Action.)* Its eight status values include "Waiting for approval,"
independently re-checked against the live PDF on 2026-09-27, and "Merged," which matches PM²'s own
four-decision vocabulary already adopted by `change-request` ("There are four possible decisions: approve,
reject, postpone or merge"). **Connecticut DSS** ships 11 columns, a different seven-value status list, and
states its own audience explicitly: "The audience for the Project Change Log includes the project team, project
sponsor, business owner, steering committee, and may include key project stakeholders." **HHS EPLC** ships a 15-column spreadsheet (`CR# | Current Status | Priority | Change
Request Description | Assigned To Owner | Expected Resolution Date | Escalation Required (Y/N)? | Action
Steps | Impact Summary | Change Request Type | Date Identified | Assoc ID | Entered By | Actual Resolution
Date | Final Resolution & Rationale`), independently parsed from its own binary spreadsheet cells rather
than a decoded-text summary. All three converge on: an identifier, a type or category, a description, a
requester, a date raised, a priority, a status, a named decision, a named decider, a decision date, and a
resolution. **No single status vocabulary is presented as canonical**; the template offers a sourced
default and states plainly that organizations customize it, the same move `issue-log`'s Priority Scale
section already makes for its own three published shapes.

#### Section design

Provisional, and expected to move once a build's own research runs:

| Section | In lean | What it carries |
|---|---|---|
| **Purpose and Boundary** | yes | What baseline changes this log tracks, and what does not go in: the per-instance change request (a separate document that feeds one row here), the software CHANGELOG (a different artifact under the identical word), a decision log (see Boundaries; thinly sourced), and configuration or version history. Names PRINCE2's exception up front, the way `change-request_guide.md`'s first line already names its own `rfc` collision |
| **Status Vocabulary** | yes | The status values this log uses, stated once so every row is comparable. Offers PM²'s eight, Connecticut DSS's seven, and HHS's set as sourced defaults, and states plainly that a team may adapt them. **POSITION**: not to present any one list as canonical, since no source claims its own list is universal |
| **Change Log** | yes | **The load-bearing section.** One row per change request: ID, type or category, title and description, requester, date raised, priority, status, decision, decider, decision date. Every field traced to at least two of PM², Connecticut DSS, HHS. A table section, so it carries PRIORITY and ROW HINT |
| **Escalation** | yes | Who acts, and under what condition, when a logged change needs authority above the log's normal decider. PM²'s Escalation field (Approval group) and HHS's `Escalation Required (Y/N)?` column are the two published shapes |
| **Implementation and Traceability** | full only | What was actually done once a change was decided: the actual delivery or resolution date, the artifact and version updated, and a link back to the change-request document this row came from and to any issue or risk that raised it. PM²'s Implementation group (Actual Delivery Date, Traceability and Comments) and HHS's Actual Resolution Date and Final Resolution & Rationale are the published shapes; the language should match `change-request`'s own Implementation and Traceability section so a request's exit point and this log's entry point read as one seam, not two vocabularies |
| **Review and Ownership** | full only | Who keeps the log and how it is reconciled to the baseline it tracks. **Thinly sourced**: the one supporting data point is HHS's own one-page checklist, whose sole ongoing activity is "Update the Change Management Log." Beyond that one line, the review cadence and reconciliation duty are this library's own judgment and must be labeled **POSITION**, not attributed |

#### Boundaries with each named neighbour

- **Not the change request (the per-instance document).** Three independent sources agree the log is the
  cumulative register and the request is the document that feeds one row into it: PM² documents a change
  "via a Change Request Form and in the Change Log" (`change-request_research-log.md:289`, already cited
  by the sibling bundle, not re-verified fresh in this pass); the PMBOK errata lists "Change log" and
  "Approved change requests" as two separate outputs; HHS's own Change Management Plan template defines one
  shared list of data elements for the "Change Request Form and Change Management Log", yet keeps two
  artifacts: its process table has a "Log CR" step ("The Change Manager enters the CR into the CR Log"), and
  HHS ships the log as its own spreadsheet.
- **PRINCE2 is the named exception, not an omission.** `prince2.wiki` (rawcheck-passed): "should be
  documented in the issue register or change log," folding change-request tracking into the Issue Register
  and naming a standalone change log only as an interchangeable alternative, not a mandatory companion
  document. State this plainly, by name, the same way `issue-log_companion.md:358-361` already states
  PRINCE2's parallel convention from its own side.
- **Not the software CHANGELOG (Keep a Changelog / `release-notes`' alias).** "A changelog is a file which
  contains a curated, chronologically ordered list of notable changes for each version of a project"
  (Keep a Changelog, rawcheck-passed). It has no requester, approver, decision, or status field at all; the
  identical word names a released-software artifact shipped with the codebase, categorically different
  from a governance register of pending and decided requests. Put this on the first line of the guide,
  since it is the single most likely mis-search, mirroring `release-notes_companion.md:132-137`'s own
  framing of the same boundary from its side. The pm-skills skill `utility-pm-changelog-curator` (checked
  2026-09-27 against `pm-skills` `origin/main`, 68 skills listed) targets exactly this software sense
  ("Draft CHANGELOG entries from git log"), not this candidate's governance sense; it is not a pairable
  skill here.
- **Not a decision log.** No rawcheck-passing quotation, from any source read this pass, names this
  boundary explicitly. Several vendor blogs converge informally on "a decision log records why a choice was
  made; a change log records what changed and who approved it," but none passed the raw-text check, and one
  attempted quote (bvop.org) failed it outright. **This boundary, if the companion states it at all, must
  be labeled the library's own POSITION**, not sourced.
- **Not configuration or version history.** HHS's own EPLC document archive keeps "07 - Change Management
  Plan" and "08 - Configuration Management Plan" as two separately numbered template categories, observed
  directly in the real archive URLs the research returned. This is a structural fact about the archive's
  own organization, not a quotation, and should be reported as such rather than dressed up as a sourced
  sentence.

#### Family fit and the ADR

**Governance-docs admits the type as written; the contract's own enumeration does not yet name it.**
`docs/internal/contracts/governance-docs.md:13`'s membership test ("a continuously-maintained register,
log, or dashboard ... to track risk, open items, or performance") describes a standing change log in its
own words, and **ADR 0060** states this three times without deciding it: "A register of requests is a
standing instrument; if it is ever built, it is a `governance-docs` candidate as written"
(`0060:106`). Every other family contract excludes the type on the same grounds `change-request` was
excluded from them (`delivery-docs.md:13`: an event-driven per-occasion form is not a standing register;
`standing-standards`: continuously revised, not agreed once; `decision-docs`, `qa-docs`, `process-docs`,
`communication-docs`, `discovery-docs`, `strategy-docs`: each excludes on the same ground ADR 0060 already
argued for the request itself, which applies at least as clearly to its standing register).

**What still needs stating, not assuming, is the same gap ADR 0057 (issue-log joins governance-docs as a
fourth member) closed for `issue-log`.**
`governance-docs.md:15` reads "The four roles are distinct but related," with an enumeration of exactly
four bullets and no change-log line. Admitting a fifth member without editing that sentence would leave
the contract's own prose out of step with its own membership, the same drift ADR 0057 and
**ADR 0050** (qa-docs admits a fourth member) each closed by amending the roles list and adding a dated
change note, not by treating the general membership sentence as sufficient on its own.
[ADR 0061](decisions/0061-change-log-joins-governance-docs-as-a-fifth-member.md) (change log joins
governance-docs as a fifth member) makes that edit, and the contract carries it in its 0.3.0 change note.

**One qualification the contract's own POSITION needs, that ADR 0057 did not have to add.**
`governance-docs.md:24` asserts, as the family's own reasoning rather than a sourced claim, that these
instruments "most often fail by collapsing into each other rather than by staying separate." PRINCE2 folds
change tracking into the Issue Register **by design**, not by failure, which is a named methodology choice
this contract's relationship story must accommodate rather than contradict. The change note ADR 0061 adds
should record this qualification with a date, per [procedure 11](decision-procedures.md#11-a-family-contract-asserts-something-about-the-world)
(a family contract's CLAIM sentences are tested against each new member's research log), so the sentence
stays a POSITION the library owns rather than a CLAIM this candidate's own admission evidence contradicts.

#### The worked example: the Reporting Platform Modernization program's change log

**The shared-scenario rule (contract section 4) is a hard constraint, and it is unusually specific here**:
the example must be this program's standing change-control log, and it must carry `CR-SV-01` exactly as
`change-request_example.md` states it, because that document already treats this unbuilt log as the place
its own decision was recorded:

> "This request went through the Reporting Platform Modernization program's change-control process, the
> one the program's issue log says every change request is handed to the day it is raised, and CR-SV-01 is
> its identifier there; this document is the record that process decided on."
> (`change-request_example.md:113-115`)

And `issue-log_example.md:43-46` states the same routing from its own side: "this program hands every
change request straight to its own change-control process the day it is raised, so no row below carries
one." **This candidate's example is that change-control process's own standing register** - the document
both siblings gesture at without instantiating.

**Facts the one entry must carry exactly, with no invention:**

| Field | Value | Source |
|---|---|---|
| Identifier | `CR-SV-01` | `change-request_example.md:3` |
| Title | "Scheduled Email Delivery for Saved Views" | `change-request_example.md:2` |
| Baseline artifact and version | Saved Views for Dashboards PRD, v0.3.0 | `change-request_example.md:4-5` |
| Requester | Priya Nair (PM, Reporting), submitted 2026-07-08 | `change-request_example.md:6-7` |
| Decider | Marta Reyes (Program Manager, Reporting Platform Modernization) | `change-request_example.md:8` |
| Decision and date | Postponed, 2026-07-18 | `change-request_example.md:9-10` |
| Origin | Not an issue, a risk, or a decision already on a program log; raised from account-management feedback | `change-request_example.md:52-57` |

**Constraints the example must not violate**, each already established in a sibling and not this library's
to re-decide:

- No row for `ISS-11` or `ISS-12`. `issue-log_example.md:131-132,139` states plainly that neither issue
  raised a change request ("No request for change," twice), a constraint **ADR 0060** already names for
  the sibling bundle's own example (`0060:119-120`) and that binds this example identically.
  `raid-log_example.md` and `risk-register_example.md` carry the same two issues under `R-03` and `R-06`
  and must not gain a change-log row either.
- The PRD stays at baseline v0.3.0. `change-request_example.md:116-117`: "the Saved Views PRD stays at its
  0.3.0 baseline, and no target version or release is set, because the release that would carry the work
  has not been scoped." A change-log row for `CR-SV-01` must show no artifact updated and no delivery date,
  matching that outcome rather than inventing one.
- Release 2.4.0 shipped 2026-06-30 with no scheduled delivery (`change-request_example.md:37-38`); nothing
  in this log may contradict that.
- If the drafting agent adds an illustrative second or historical row for realism, it must be dated inside
  a window no sibling example pins, or closed before the earliest date any sibling states (2026-06-14, the
  key-person risk's materialization), and it must not touch `R-03`, `R-06`, `ISS-11`, or `ISS-12`. **The
  safer build choice is one entry, `CR-SV-01`, stated plainly as the log's first and only logged change to
  date**, leaving a second row to a future build rather than to invention.
- `last_reviewed` (or equivalent frontmatter) should sit at or after 2026-07-18, the decision date, so the
  log reads as current with respect to its own one entry.

*(Corrected 2026-09-30: the examples' timeline was reconciled. 2.4.0 now ships 2026-07-21, `CR-SV-01` is
submitted 2026-08-04 and decided 2026-08-14, and the change-log example is reviewed 2026-08-17. The facts
above keep their original dates, as the record of what this spec was built against.)*

**A sibling sentence the landing PR corrects.** `change-request_companion.md:371-372` said "HHS's EPLC
program merges the two" (corrected 2026-09-28; the sentence is now lines 375-377), meaning the request form and the log. Both readings of the HHS plan template are
partly right. The template defines one shared list of data elements for the "Change Request Form and Change
Management Log", which is what `change-request`'s research log recorded. It also keeps two artifacts: a
"Log CR" step in which "The Change Manager enters the CR into the CR Log", and a log shipped as its own
spreadsheet. The landing PR gives the companion's sentence a dated correction to that reading.

#### Catalog corrections the landing PR must make

Per [procedure 1](decision-procedures.md#1-a-catalog-call-loses-to-research), both
`docs/internal/catalog.md:223` and `atlas/catalog-data.json:3903-3926` *(2026-10-14: the `change-log-governance` entry now sits at 3921-3949, after later landings grew the file.)*, then regenerate the atlas:

- **`methodology: "PMBOK/ITIL"` is contradicted.** No rawchecked source shows ITIL naming or shipping a
  "change log" as such. ITIL's own two rawcheck-passed artifacts are differently-named and narrower: a
  "Change Schedule" ("A Document that lists all approved Change Proposals and Changes and their planned
  implementation dates") and a "Change Record" ("documenting the lifecycle of a single Change"), and
  neither is a cumulative log of every submitted request the way PM²'s and Connecticut DSS's logs are.
  Every source that actually admits and structures this type (PMI, PM², APM, Connecticut DSS, HHS) shares
  the same lineage as `issue-log`'s own methodology correction. **Recommend `methodology: generic`**,
  matching `issue-log`'s and `change-request`'s own corrected values, and cite ITIL as a named neighbour in
  the companion instead of as a source.
- **Aliases should gain sourced terms, not lose the sourced ones already there.** `change register` is
  independently confirmed by APM's own glossary entry, "Change register (or log)," and should be kept.
  `change control log` has no source in this pass; **recommend it be sourced before the build or dropped**.
  *(2026-09-28: the entry name is corrected from "Change log (or log)". The build sourced `change control log`
  to one named practitioner, and no public body; see `change-log_research-log.md`.)*
  Recommend adding `change management log` and `change request log`, both directly attested by HHS's own
  named documents across three separate files.
- **`owner: "PM / Change Manager"` is an open question, not a correction.** Nothing read this pass either
  confirms or contradicts "Change Manager" as this type's owner; every source that names an audience names
  a role (PM, sponsor, business owner, steering committee) rather than a title. Flag it for the spec
  author or reviewer, not the build; do not invent a source for it.
- **`size_variant: "S"` likely undercounts the shipped shape.** The same correction `issue-log`'s own
  landing made: the catalog's single-letter size marker predates any research into the type's actual
  published shapes, and this pass's own structure findings (PM²'s four groups, Connecticut DSS's 11
  columns, HHS's 15 columns) support a two-weight `[lean, full]` split, not a single size.

#### `pairs_with`: checked, and empty

Checked 2026-09-27 against `pm-skills` `origin/main` directly (`gh api
repos/product-on-purpose/pm-skills/contents/skills --jq '.[].name'`, 68 skills returned) and against
`tools/known-skills.txt`. One name suggested a match and was read in full:
`utility-pm-changelog-curator` ("Draft CHANGELOG entries from git log via the pm-changelog-curator
sub-agent"). It targets the software CHANGELOG sense (Keep a Changelog, git-log-driven), not this
candidate's governance sense, and never mentions a change request, a baseline, or a change-control board.
No other skill name or description in the 68 suggests a governance change-log producer or consumer. On
current evidence, **`pairs_with: []`** is the correct value, the same posture `issue-log` and
`change-request` both adopt for the same reason.

#### Risks for the build and review

1. **The "five roles" enumeration lands with this spec, in the contract's 0.3.0 change.** A build that
   treated `governance-docs.md:13`'s general wording as authorization enough, without that edit, would repeat
   the gap ADR 0057 and ADR 0050 each closed rather than assumed.
2. **PRINCE2's exception must survive drafting, not get smoothed into the PMI/PM² consensus.** Every other
   named source agrees the log is a mandatory, separate companion document; PRINCE2 alone does not, and
   the companion must state its position by name, the same discipline `issue-log_companion.md:358-361`
   already keeps for its own PRINCE2 exception.
3. **The HHS quotations carry a retrieval hazard a research agent will hit if it tries the live URL.**
   `hhs.gov` returns 403; cite the Internet Archive `id_` copy, and do not quote "A
   submitter completes a CR Form and sends the completed form to the Change Manager" whole. Only the
   fragment "A submitter completes a CR Form and sends the" passed the raw-text check.
4. **The decision-log boundary is a POSITION at best, and must not gain an invented citation.** No source
   read this pass or the prior sweep passes the raw-text check on that specific distinction; state it as
   the library's own judgment or cut it, never source it after the fact to make the companion read more
   confident than the evidence.
5. **The alias and skill near-misses need a first-line disambiguation, not a rename that hides them.**
   `release-notes`' `changelog` alias and pm-skills' `utility-pm-changelog-curator` are both close enough,
   in plain English, to misdirect a reader even though no string collides mechanically. State the
   collision on the guide's and companion's first page, the way `change-request_guide.md` already states
   its own `rfc` collision, and add the one routing line `release-notes_guide.md` owes from its own side.
6. **The templates stage has repeatedly copied the worked example's own scenario into GOOD and WEAK text**,
   and no lens catches it reliably: `tier2-specs.md:1497-1499` records this exact failure surfacing in
   `change-request`'s own build, caught only by the main loop after every automated lens passed. **Every
   GOOD and WEAK illustration in this bundle's templates must use a scenario unrelated to the Reporting
   Platform Modernization program**, independent of the worked example, per the shareable-boundary rule
   (contract section 5) and the family's own contract section 3.7.
7. **The landing PR corrects `change-request_companion.md:371-372`'s "merges the two"**, as set out under
   the worked example, so the two companions describe HHS the same way. *(Done 2026-09-28; the corrected
   sentence is `change-request_companion.md:375-377`.)*

---

### standing-standards (fifth member): the production readiness review

**`production-readiness-review`** - `standing-standards`, **`classification: tool`** (maintainer's ruling,
2026-09-27; argued in [ADR 0062](decisions/0062-production-readiness-review-joins-standing-standards-as-a-tool.md)),
sizes **`[lean, full]`** (provisional), methodology **`SRE-lineage`**, catalog id `production-readiness-review`
(catalog 125), aliases `PRR`. Catalog owner: SRE. Purpose: "Assess whether a service is ready for production."
Contents, per the catalog: "reliability, monitoring, runbooks, capacity, on-call". `size_variant: M`, `rarity:
occasional`, `tier_inferred: true`. **The catalog row's own source column reads "Google SRE practice."**

#### Demand: prose routing, not a promise tag, and weaker than `issue-log`'s

No `future:` tag points here. `grep -rn "future:production-readiness" templates/` returns nothing, checked
2026-09-27. The demand is three lines of prose that already assume the type exists, plus the catalog's own
cross-reference:

- `templates/launch-coordination-checklist/launch-coordination-checklist_companion.md:464-469` gives the type
  its own subsection ("Launch coordination checklist and production readiness review") and states, without a
  tag to enforce it, "the two documents plausibly govern different moments of the same discipline."
- `docs/internal/tier2-specs.md:543-546` (the launch-checklist spec) asks its own research pass to "look for a
  second [source]: a production or operational readiness review published as a document," and says "one source
  suffices; a second would change the teaching." **This sweep found it**: three named sources publish the
  document, and several more describe the review.
- `docs/internal/decisions/0053-launch-coordination-checklist-joins-standing-standards-as-a-tool.md:41` and
  `:105` both name the relationship in passing ("relates to `PRR`"; "a PRR relationship").
- `atlas/catalog-data.json` already carries an asymmetric edge: `launch-coordination-checklist`'s
  `relationships` is `["PRR"]`; `production-readiness-review`'s own `relationships` is `[]`. The catalog
  promises the reverse link and does not pay it.

This is real routing, not a gate obligation the way `issue-log`'s `future:` tags were. No check fails today for
not building this type. It is, as the digest puts it, a maintainer scope call under
[ADR 0041 (maintainer preference sets the build order)](decisions/0041-maintainer-preference-sets-the-build-order.md),
made on 2026-09-27.

#### Admission: three named sources publish the document, and more describe the review

Every quotation below was checked against the source's raw text on 2026-09-27, either in the sweep's own
re-check pass or by a direct `rawcheck.py` call made while writing this spec (marked below). Four quotes are
cited to a different page than the one the sweep first filed them under, because the re-check found them
there.

| Source | What it says | Licence |
|---|---|---|
| Google, *Site Reliability Engineering* (O'Reilly, 2016), ch. 32, "The Evolving SRE Engagement Model" | "The SRE team establishes and maintains a PRR checklist explicitly for the Analysis phase." (re-checked in the main loop) | **CC BY-NC-ND 4.0**, confirmed by a direct `rawcheck.py` call against this page's own footer text, not carried from the launch-checklist spec's "CC BY-ND" note |
| Susan Fowler, *Production-Ready Microservices* (O'Reilly, 2016/2017), Appendix A | "This will be a checklist to run over all microservices," under the heading "A Production-Ready Service Is Stable and Reliable" and four more, ~35 items across the five, counted directly from the pages | Cited as Fowler, *Production-Ready Microservices* (O'Reilly, 2016), Appendix A, **via the sponsored O'Reilly excerpt** ("Compliments of", chapters 1, 3, 4, 7 and Appendix A), hosted by F5 |
| Mercari, Inc., `production-readiness-checklist` (Production Readiness Check, PRC) | "which is required for all services before receiving real production traffic"; "If a specific item is not applicable to your service check the item and explain" | **MIT** (GitHub API, 2026-09-27; not archived, last push 2021-11-22) |
| GitLab Inc., archived `.gitlab/issue_templates/production_readiness.md` | "This issue serves as a tracking issue to guide you through the readiness review"; "It's not the production readiness document itself" | Not stated on this file |
| GitLab Inc., the same project's `README.md` (cite here, not the issue template) | "The Production Readiness Review process has been superseded by" [PREP]. GitLab archived this project; do not cite it as a current process | Not stated |
| AWS, Well-Architected "Operational Readiness Reviews" whitepaper | "Amazon Web Services (AWS) created the Operational Readiness Review (ORR) to distill the learnings from AWS operational incidents"; "Teams perform self-assessments on operational risks ... throughout the complete lifecycle of their service, from inception to post-release operations"; "Any high-criticality findings are escalated to leadership as input to a go or no-go launch decision" | Not stated |
| AWS, the same whitepaper's `the-orr-tool.html` sub-page (cite here, not the landing page) | "The main tool for ORR is the checklist of questions itself"; grouped under "Release quality" and "Event management"; a third heading, "Architecture," re-checked directly with `rawcheck.py` on 2026-09-27 rather than left "not retested" | Not stated |
| AWS, `inspect-the-process.html` | "When was your last ORR performed" | Not stated |
| Microsoft, Azure Well-Architected `operational-excellence/maturity-model` (cite here, not `/checklist`) | "Level 3: Release readiness"; "Testing becomes a go-live requirement to ensure safe and stable deployments" | Not stated |
| Grafana Labs, company blog | "Production readiness review (PRR) is a process that originated at Google"; "a completely separate process ... having the product in question reviewed by an experienced engineer, ideally outside of the product team"; "We're looking into a periodic and/or incremental PRR as part of our continuous product improvements" | Not stated |
| GitLab Inc., `docs.runway.gitlab.com` platform guide | "SaaS Platforms uses production readiness review process for new services" | Not stated |
| Google Cloud, "How SREs find the landmines in a service" (CRE Life Lessons) | "During an SRE entrance review (SER), also referred to as a Production Readiness Review (PRR), the SRE team takes the measure of a service currently running in production" | Not stated |
| Cortex, `docs.cortex.io` Scorecard docs | "Scorecards automate the process of checking whether services meet criteria such as ownership, on-call coverage, runbooks, monitoring, and security requirements" | Not stated. **Do not** cite Cortex's specific 6-category/24-item breakdown; it failed `rawcheck` (a JS-rendered marketing page returning 245 extractable characters) |

**Three sources publish the document**: Fowler's Appendix A, GitLab's template and Mercari's checklist.
Google's chapter 32 says its SRE team maintains a PRR checklist. Grafana, GitLab's Runway guide, AWS and
Microsoft describe the review practice without shipping the document, and Cortex describes a live scorecard
product, which is out of scope for a Markdown template. That clears
[ADR 0048](decisions/0048-one-named-source-clears-the-admission-test.md)'s one-source floor three times.
Confidence: high.

**A name collision, confirmed and out of scope.** NASA's *Systems Engineering Handbook* Appendix B ("A review
for projects developing or acquiring multiple or similar systems greater than three ... The PRR determines the
readiness of the system developers to efficiently produce the required number of systems") and AcqNotes'
DoD-acquisition glossary ("The Production Readiness Review (PRR) determines if a systems design is ready for
production," "normally performed as a series of reviews toward the end of the Engineering [and Manufacturing
Development phase]") both publish "Production Readiness Review" as a written document, and both quotes passed
`rawcheck`. This is a hardware-manufacturing-readiness gate from an unrelated discipline that predates the SRE
usage; it shares only the name and is not this bundle's subject. The companion needs one disambiguating
sentence; the template needs none.

**What must not be carried into a companion.** The claim that SRE book chapter 32 calls the Launch Coordination
Engineering team "a lighter-weight alternative" is refuted: the phrase is not on the chapter's page, which a
direct raw-text check confirmed. Chapter 32's only cross-reference to that team is
that it "spends a majority of its time consulting with development teams." Say no more than that.

#### The launch-checklist boundary: this is the central review risk

**The subject-matter distinction fails, and the spec must say so plainly rather than assert cross-functional
scope by inference.** A gap-fill retrieval in this sweep read Google's own Appendix E, "Launch Coordination
Checklist" (`sre.google/sre-book/launch-checklist/`), which `docs/internal/tier2-specs.md:505-520` already
counted at ten areas and 31 items. Every one of its ten section headings is engineering- or operations-scoped:
Architecture; Machines and datacenters; Volume estimates, capacity, and performance; System reliability and
failover; Monitoring and server management; Security; Automation and manual tasks; Growth issues; External
dependencies; Schedule and rollout planning. None names marketing, legal, external communications, or
pricing/go-to-market. So the boundary cannot rest on "PRR is engineering-only, the launch checklist is
cross-functional": both are engineering-scoped in their own founding documents. **The distinction that survives
is trigger, team, and timing**, all three sourced to the same primary chapters:

| Axis | Production Readiness Review (ch. 32) | Launch Coordination Checklist (ch. 27) |
|---|---|---|
| Trigger | "a development team requests that SRE take over production management" of a service already running | "Most audits are conducted before a new product or service launches" |
| Team | "Usually one to three SREs are selected or self-nominated to conduct the PRR" | "The Launch Coordination Engineering (LCE) team," "held to the same technical requirements as any other SRE" |
| Timing | "The Production Readiness Review can be started at any point of the service lifecycle" | Pre-launch, gatekeeping: "Acting as gatekeepers and signing off on launches determined to be" safe |

*(Corrected 2026-09-28, when the bundle was built: trigger and timing separate the two in Google's chapters, not in
adopters' practice. Mercari requires its check "for all services before receiving real production traffic",
GitLab gates each maturity level of a new service, Grafana writes of a "pre-launch PRR", and the US Federal Student
Aid office runs a PRR on every release before implementation, so a PRR and a launch checklist can meet at the same
launch. What differs in every source read is the object: a PRR reviews a service's standing ability to be run, and
the launch checklist reviews one launch. That reading is this library's, and the companion labels it so. The
quotations are in the [research log](../../templates/production-readiness-review/production-readiness-review_research-log.md), contested item 10.)*

A second, independent framing agrees without naming either type: Studio Red's practitioner guide draws a
release-moment-versus-long-term-operability line, already quoted at
`launch-coordination-checklist_companion.md:472-473` (ref 38). That source was not re-verified against its
primary text in this sweep, so it is reported here as the sibling companion's own citation, not this sweep's,
and is not requoted.

**The new companion must agree with `launch-coordination-checklist_companion.md:464-469`, not restate it
differently.** That section already holds the position "the two documents plausibly govern different moments
of the same discipline" and explicitly declines to claim replacement or sequence. This bundle's own
Relationships section states the same position from its side, adds the trigger/team/timing table above as the
evidence for it, and **retracts the subject-matter half of the argument** rather than repeating it, because
Appendix E now falsifies it directly. Per `decision-procedures.md` section 11, that retraction is the honest
move: a claim a later retrieval falsifies is corrected in place, not defended.

**A second neighbour, AWS's Operational Readiness Review, is the same shape at a different cadence.** ORR is
reviewed "throughout the complete lifecycle of their service, from inception to post-release operations" and
tracks "When was your last ORR performed" as a standing metric (cited to `inspect-the-process.html`). Google's own PRR is, on the sources read here, closer to one-time
("Once the issues have been fixed, the product has passed the PRR," Grafana), while Grafana itself reports
reconsidering that design ("We're looking into a periodic and/or incremental PRR"). **Cadence is contested
across real adopters, not settled**, and the template's Review Trigger section, not a fixed assumption, is
where that dispute belongs.

**A third neighbour, the runbook, is complementary rather than competing, and the catalog under-states it.**
Every PRR source that ships an actual checklist checks that a runbook already exists rather than producing one:
Cortex's scorecard criteria include "runbooks" by name; GitLab's and Fowler's checklists ask for one as an
input (per the launch-checklist bundle's own already-published research log, not re-verified here). `runbook`'s
catalog `relationships` field is `[]` despite this; the catalog corrections below add the reverse edge.

**A fourth neighbour, the Change Advisory Board, is a different unit of review, both raw-checked.** A CAB
"delivers support to a change-management team by advising on requested changes" and "is responsible for
oversight of all changes in the production environment" - a portfolio-wide, standing panel reviewing many
changes across many services, not a per-service technical assessment. The two do not overlap in scope or
grain.

**A fifth neighbour, Definition of Done, differs in object and authority, both raw-checked.** The Scrum Guide's
DoD is "a formal description of the state of the Increment," a per-work-item bar the Developers agree and judge
themselves against every sprint. A PRR is service-level, typically reviewed by someone other than the team that
built the service ("an experienced engineer, ideally outside of the product team," Grafana), and its cadence is
occasional-to-periodic rather than every increment.

#### Family fit: `standing-standards` admits the standing questionnaire; the per-service record does not exist as a separate type

**Two readings, one membership answer.** A maintained PRR checklist (the questionnaire) passes the family's own
falsifier the same way `launch-coordination-checklist` did: it is "consulted at the moment of action," per
[ADR 0053](decisions/0053-launch-coordination-checklist-joins-standing-standards-as-a-tool.md)'s test, restated
at `docs/internal/contracts/standing-standards.md:108-110`. A per-service review record (one team's filled
answers for one service, one time) excludes from every family tested, standing-standards included, on the
contract's own analogy: "a runbook written for one incident is an incident report"
(`standing-standards.md:37`). **This resolves the library's stated either/or**: the bundle is the standing
questionnaire, and the worked example is a filled instance of it, exactly the relationship
`launch-coordination-checklist_example.md` already has to its own template.

**`governance-docs` admits with strain, not as written.** Its membership test names "a register, log, or
dashboard" (`docs/internal/contracts/governance-docs.md:11`); a review checklist with pass/fail criteria is
none of the three in form, even though its whole-lifecycle framing (AWS's ORR, above) matches the family's
spirit. `standing-standards` fits the letter as well as the spirit; this spec follows the maintainer's ruling
into that family.

**Every phase-axis family excludes, on the catalog's own `stage: release` value**, which sits outside each of
`qa-docs` (`develop`), `decision-docs` (`develop`), `delivery-docs` (`deliver`), `discovery-docs` (`discover`),
`process-docs` (`iterate`), `communication-docs` (`utility`, audience
inside the team, not outside), and `strategy-docs` (organization-wide direction, not one service).

**This is the family's first unforecast member, and that is worth naming rather than hiding.**
`standing-standards.md:46` names only "a coding-standards or engineering-handbook document" as a likely future
member. Unlike `launch-coordination-checklist` and `definition-of-ready`, which the contract predicted by name
before either was built, this admission rests entirely on the membership test and the falsifier, not on a
forecast the contract can be shown to have gotten right. Per
[ADR 0057](decisions/0057-issue-log-joins-governance-docs-as-a-fourth-member.md)'s principle, "the membership
test, not the list of members that happened to be planned, governs a candidate," so this does not weaken
admission; it does mean the ADR cannot claim the forecast's confirmation the way ADR 0053 and ADR 0058 could.

#### Section design

Provisional, drawn from the intersection across sources rather than any one source's exact taxonomy (no two of
Fowler, Google, GitLab and AWS agree on section count or naming), and expected to move:

| Section | In lean | What it carries |
|---|---|---|
| **Scope and Trigger** | yes | What counts as "production" here, and what event starts a review: an SRE-ownership handoff ("a development team requests that SRE take over production management"), a maturity-gate promotion (GitLab's Experiment/Beta/GA), or a periodic re-review (AWS's ORR). A review with no stated trigger is applied to everything or nothing, the same trap `launch-coordination-checklist`'s Scope section names |
| **Reviewer and Authority** | full only | Who conducts the review and who decides the outcome. Sourced: "Usually one to three SREs are selected or self-nominated" (Google); "an experienced engineer, ideally outside of the product team" (Grafana). Neither source ties this to a single named decision authority the way `launch-coordination-checklist`'s Roles section does; the template supplies the field and the companion says so |
| **Readiness Criteria** | yes | **The load-bearing section.** Checks grouped by domain, each with the evidence that answers it and an owner. Domain list is the counted intersection: architecture and dependencies, capacity and scalability, monitoring and alerting, on-call and incident response, deployment and rollback, security, and data/backup/DR - drawn from the areas Google's chapter 32 names a PRR evaluates, Fowler's five headed sections, GitLab's per-gate subsections and AWS's Architecture/Release-quality/Event-management grouping, not copied from any one. A table section: carries PRIORITY and ROW HINT |
| **Not-Applicable Rule** | yes | An item marked not-applicable must carry a written reason, not a blank check. **Sourced, for once**: Mercari's PRC states this rule directly ("If a specific item is not applicable to your service check the item and explain") |
| **Outcome and Sign-off** | yes | What the review concluded: passed, passed-with-conditions, or not ready, and who signed. Fowler and Grafana both describe a pass/fail outcome ("the product has passed the PRR"); neither publishes a fixed vocabulary for it, so the template supplies one and the companion labels it as this library's own |
| **Review Cadence** | full only | Whether this review is one-time, periodic, or triggered by a later event, and why. **Genuinely contested across sources, not a default**: Google/Grafana currently one-time-but-reconsidering versus AWS's ORR already periodic ("throughout the complete lifecycle"). The template asks the filler to state a position rather than assuming one |
| **When This Does Not Apply** | full only | Services or changes exempt from a full review, and what smaller check they get instead. Mirrors `runbook` and `launch-coordination-checklist` |
| **Review Trigger** | yes | **Contract-mandated** (section 4): a named owner and a condition, not a calendar. Candidate condition: a production incident whose contributing cause a passed criterion should have caught, tying this section to `incident-postmortem` the way `launch-coordination-checklist`'s does |

#### Catalog corrections the landing PR must make

Per [decision-procedures.md procedure 1](decision-procedures.md#1-a-catalog-call-loses-to-research), both
`docs/internal/catalog.md` and `atlas/catalog-data.json`, then regenerate the atlas:

1. **Aliases: add, sourced.** "production readiness checklist" and "PRC" (Fowler's and Mercari's own names for
   the artifact they ship); "SRE entrance review" and "SER" (the Google Cloud CRE blog's own interchangeable
   usage inside Google: "also referred to as a Production Readiness Review (PRR)").
2. **Aliases: drop, unsourced and collision-prone.** "launch readiness review" has no supporting quotation in
   any source this sweep or the launch-checklist bundle's own research read, and it is the phrase most likely
   to be typed by a reader actually looking for `launch-coordination-checklist`. Recommended, not gate-mandated.
3. **Relationships: reverse the edge.** `production-readiness-review`'s `relationships` is `[]` while
   `launch-coordination-checklist`'s already carries `["PRR"]`; add `["launch-coordination-checklist"]` here.
4. **Relationships: `runbook` gains a forward edge.** Every PRR source that ships a real checklist checks for an
   existing runbook; `runbook`'s own `relationships` is `[]`. Add `["production-readiness-review"]`.
5. **The name collision goes in the guide and companion, not the catalog row.** `gen-atlas.py` blanks
   `state_note` for a built type, so the one-line note that "Production Readiness Review" also names a DoD and
   NASA hardware-manufacturing milestone belongs on the guide's first page and in the companion.

#### `pairs_with`: checked, empty

`gh api repos/product-on-purpose/pm-skills/contents/skills --jq '.[].name'` returned all 68 skill names on
2026-09-27. No name contains "readiness" that targets production or
operational readiness: the two hits, `tool-design-sprint-readiness` and `tool-foundation-sprint-readiness`, are
design-sprint and foundation-sprint precondition checks, unrelated in subject. `deliver-launch-checklist`, the
one plausibly adjacent skill, already pairs with `launch-coordination-checklist`
(`launch-coordination-checklist_meta.yaml:15`), not this type. **`pairs_with: []`**, per the contract's own rule
that a member "adopts `[]` until one does."

#### Risks for the build and review

1. **The launch-checklist boundary is the finding a reviewer will test hardest.** The subject-matter argument
   is refuted by this sweep's own gap-fill retrieval; only trigger, team and timing survive. A companion that
   reaches for the easier, refuted line ("PRR is engineering, the launch checklist is cross-functional, so
   they're obviously different documents") will fail review on a claim this same sweep already falsified.
2. **The "lighter-weight alternative" phrase is a live temptation** because it appears in two of this sweep's
   own returns as if confirmed. It is refuted by a direct raw-text check; do not carry it into the companion under any
   paraphrase that keeps its substance.
3. **Cortex's specific category/item breakdown failed rawcheck** and must not be quoted or paraphrased as a
   specific structure; only its general Scorecard description (docs.cortex.io, raw-checked) is usable.
4. **The build workflow's templates stage has repeatedly copied the worked example's own scenario into the
   template's GOOD text**, a defect this library has already named and not yet mechanically gated. The
   Readiness Criteria section's GOOD and WEAK illustrations must describe a service and an incident **other
   than** the example's Acme Analytics dashboard-service PRR below; grep the drafted templates for the
   example's proper nouns (Acme, Dana Osei, Marcus Bell, Sam Okafor, Anjali Rao, Priya Nair, DEF-2291,
   dashboard-service) before review, the way the digest recommends for every build.
5. **This is the family's first unforecast member and its fifth overall.** The contract's own coherence
   caveat ("this family's coherence is thinner than `governance-docs`' or `strategy-docs`'") was written for
   three members; a fifth, unforecast one is exactly the kind of candidate the falsifier exists to test
   rigorously rather than wave through on precedent.
6. **No source read supplies a fixed pass/fail vocabulary** for a review's outcome, or a full list of failure
   modes. Only three failure modes are sourced (below); everything else must be labelled the library's own
   judgment or cut, per `review-standards.md` section 5's dominant-defect-class rule. *(Corrected 2026-09-28,
   when the bundle was built: the bundle's research found both. OneUptime's practitioner guide publishes four
   decision states, of which the template takes "Ready", "Ready with conditions" and "Not ready", attributed to
   that guide and not presented as a standard. The sourced failure modes grow from three to eight: a third from
   Alves, three antipatterns that Nolan's talk names, and drift after a one-time review, which the adhorn ORR
   template names outright. The [research log](../../templates/production-readiness-review/production-readiness-review_research-log.md) quotes all eight.)*

**Failure modes, sourced, and nothing beyond these three without a citation** *(eight since 2026-09-28; see the
correction to item 6)*:

- Lack of buy-in: "Running a PRR without any specific goal means that the PRR can drop to the bottom of the
  development team's priority list" (Alves, USENIX).
- Defensiveness from the reviewed team: "If the development team feels threatened by the review" (Alves).
- Engagement starting too late to change the design: "The main limitations of the PRR Model stem from the fact
  that the service is launched and serving at scale," and "SRE engagement starts very late in the development
  lifecycle" (Google, ch. 32). This is the sharpest of the three, since Google names it as the model's own
  stated limitation, not an outside critique.

Do not assert "checkbox exercise," "findings never followed up," or "criteria not tailored to the service" as
sourced findings; none surfaced in a raw-checked quotation in this sweep.

#### The worked example: a scenario, not a launch, chained onto facts that already exist

**This must not be the Saved Views Sharing launch itself, or the example collapses into
`launch-coordination-checklist_example.md`'s own scenario and the spec's central boundary argument (trigger:
ownership handoff, not launch date) has nothing to demonstrate.** The proposed scenario is the SRE-lineage
trigger directly: after the Saved Views Sharing launch stabilizes, Acme Analytics' Platform team requests that a
newly formed Acme Analytics SRE function take over production ownership of `dashboard-service`, the same
service the `sdd` and `test-plan` examples describe, and the review this bundle demonstrates is the one that
decides whether SRE accepts. *(Corrected 2026-09-28: `dashboard-service` belongs to the Reporting team, whose
Staff Engineer Marcus Bell `runbook_example.md:5` names as its owner, so Reporting makes the request, not Platform.
The example also names two reviewers outside Reporting: Ines Halvorsen from the new SRE function, the team
Google's ch. 32 says conducts the review, and Dana Osei, the outside engineer Grafana describes.)*

- **Date: 2026-08-22.** Later than every date the sibling thread already occupies (PRD created 2026-06-12;
  DEF-2291 discovered 2026-07-13; the exit review and launch, 2026-07-17; the Reporting Squad DoD's amendment,
  2026-07-24; the entitlement-audit runbook's first live use, 2026-07-28; the dashboard-scoped kill-switch
  acceptance's own expiry, 2026-08-15), so the review can reference each of those events as already-settled
  history without needing to reconcile a date against them.
- **People: reuse the thread's named roles, in the roles the sources give them.** Dana Osei (Staff Engineer,
  Platform; `launch-coordination-checklist_example.md:57`) is the natural reviewer per Grafana's "an
  experienced engineer, ideally outside of the product team," because Dana holds decision authority across
  launches rather than owning `dashboard-service`'s day-to-day code. Marcus Bell (`launch-coordination-checklist_example.md:58`;
  `runbook_example.md:5`) is the service owner answering the review, the position Google's ch. 32 describes as
  the requesting development team.
- **Content it may chain onto, without repeating the launch checklist's own table rows.** The review may cite
  that DEF-2291 occurred (2026-07-13) and that a regression guard and an entitlement-audit reconciliation job
  exist as a result (`runbook_example.md:32-33`), as evidence its Readiness Criteria section's monitoring and
  on-call rows can point to. **It must not restate the specific checks `launch-coordination-checklist_example.md`
  already runs** (the permission matrix, the dashboard-scoped kill switch); a PRR reviewing whether SRE takes on
  a service asks different questions (on-call rotation ownership, alerting coverage, capacity headroom, backup
  and DR) than a launch checklist asks about one specific change.
- **The build number contradiction it must simply not touch.** `release-notes_example.md` dates build/version
  2.4.0 at 2026-06-30; `launch-coordination-checklist_example.md:109` dates build 2.3.2 at 2026-07-14;
  `runbook_example.md:32` and `incident-postmortem_example.md:28` both describe a build numbered 2.4.0 as
  postdating DEF-2291 (2026-07-13). No file reconciles this. **The PRR example must cite no build or release
  number for `dashboard-service` at all**, referring only to dated events (the incident, the launch, the
  amendment) the way this spec does above. *(Reconciled 2026-09-30: 2.4.0 now ships 2026-07-21, after
  DEF-2291, so the runbook's and the postmortem's 2.4.0 agree with the release notes. The PRR example cites
  no build number and needed no change.)*

Per the family's own shared-scenario rule (`standing-standards.md` section 4), the chaining stays loose by
design: this is a standing instrument belonging to the Platform and the new SRE function, shown as it stood at
one review, not a record that only this launch could have produced.

#### Metadata

| Field | Value | Why |
|---|---|---|
| `family` | `standing-standards` | Maintainer ruling, 2026-09-27; argued in ADR 0062 |
| `classification` | `tool` | Maintainer ruling. Argued marker-by-marker in ADR 0062 against `standing-standards.md`'s section 2 cut: executed by someone other than the service's own author ("an experienced engineer, ideally outside of the product team," Grafana; "one to three SREs ... selected or self-nominated," Google), at the moment SRE takes on a service, not a standard the service's own team is judged against on a schedule |
| `sizes_available` | `[lean, full]` **provisional** | GitLab's three maturity gates (8, 4 and 6 subsections, counted from the raw template) show a real tiering pattern beyond Fowler's flat five-section list; lean carries the flat engineering-readiness core (Scope and Trigger, Readiness Criteria, Not-Applicable Rule, Outcome and Sign-off, Review Trigger), full adds the gating and cadence apparatus (Reviewer and Authority, Review Cadence, When This Does Not Apply). This split is this library's own judgment, not any one source's structure |
| `status` | `beta` | Every bundle |
| `methodology` | `SRE-lineage` | Matches its closest sibling, `launch-coordination-checklist_meta.yaml`'s own value, rather than `runbook`'s `DevOps/SRE` or the catalog's plain `SRE`; nearly every admission source in this sweep sits inside the same Google-originated lineage |
| `pairs_with` | `[]` | Checked against pm-skills `origin/main`, 2026-09-27; no skill produces or consumes this type |
| `related_templates` | `[launch-coordination-checklist, runbook, definition-of-done]` **provisional** | The neighbour the boundary risk names, the instrument it checks for rather than replaces, and the family sibling it is classified alongside |
| `aliases` | `PRR` kept; **add `production readiness checklist`, `PRC`, `SRE entrance review`, `SER`**; **drop `launch readiness review`, recommended** | See catalog corrections above |

#### What landing this bundle closes elsewhere

1. **The `standing-standards` contract's Members line**, from "not yet built" to the build date. The contract
   moved to `0.4.0` in the spec PR, with ADR 0062.
2. **`launch-coordination-checklist_companion.md`'s own Relationships subsection is not changed by this
   landing**; it already holds the position this bundle's companion must agree with. Whether it gains a direct
   link to the new bundle is a build decision, not a required edit.
3. **The catalog entry**, per the corrections above, in both `docs/internal/catalog.md` and
   `atlas/catalog-data.json`, then the atlas regenerated.
4. **This page's Progress table.**

#### What the build would cost

No build has run for this type. Projected from the two most recent Tier-2 bundles built through the committed
`build-bundle.js`, both with every agent resolved to Sonnet: `issue-log` at $16.76 whole ($14.29 for its 15
build agents) and `change-request` at $14.41 whole ($14.41 for its 15 build agents, research $6.01, drafting
$5.78, review $2.62). A whole-bundle estimate of **$14 to $17 at API list rates** is reasonable on that basis;
it is a projection, not a measurement, until `python tools/gen-bundle-build-report.py --ingest` runs against an
actual build report.

---

### discovery-docs (reopened, third member): the project brief that reopens a closed family

**`project-brief`** - `discovery-docs`, **`phase: discover`**, sizes **`[lean, full]`** (provisional),
methodology **`PRINCE2`**, catalog id `project-brief` (catalog 71), catalog name "Project Brief", aliases
`lightweight charter`, `project one-pager`. Catalog owner: PM. Purpose, per the catalog: "Lightweight project
definition for smaller efforts" (corrected below). Contents, per the catalog: "objectives, scope, timeline,
budget, stakeholders". `size_variant: S`, `rarity: common`, `tier_inferred: true`, `relationships: [Charter]`.
**The maintainer ruled 2026-09-27: build, and reopen `discovery-docs` to admit it.** The contract
edits of [ADR 0063](decisions/0063-project-brief-reopens-discovery-docs.md) landed with this spec, so the
metadata below is written against the reopened contract.

#### Demand: a shipped bundle already routes a reader here, and already names a source for it

**`business-case`, already shipped, routes a reader to this type by name, defines the boundary against itself,
and cites a named source for it**, the same routing shape `issue-log`'s demand section rested on:

- `business-case_guide.md:17`: "a **project brief** | you need a short overview for starting up a project,
  not an investment case. A project brief absorbs an outline business case as one component and retires once
  initiation documentation exists; the business case itself keeps being refined, it does not retire with the
  brief".
- `business-case_companion.md:315-317`: "It is not a project brief: PRINCE2's project brief is 'a short,
  high-level overview of the project, created during the starting up a project process,' and it absorbs an
  outline business case as one component before retiring once the project initiation documentation exists;
  the business case itself is not retired the same way, it continues to be refined [[32]]."
- `business-case_companion.md:420`: reference 32 is "PRINCE2 Wiki. 'Project brief,' management products,
  baselines," already logged as a citation in a shipped bundle's research trail.
- `business-case_template-full.md:37` and `business-case_template-lean.md:32` both carry the same boundary
  sentence in the template body itself: "It is NOT a project brief (a short overview that absorbs an outline
  business case as one component...)".

The shape is the same as `issue-log`'s: a "You actually need | Because" chooser row in a shipped guide, plus a
companion and both templates that state the boundary in their own body text. No gate flags it, because nothing
here is a stale `future:` reference; it is a named, cited, boundary-defining neighbour that a shipped bundle
has been describing the edges of without the library building it.

#### The family: `discovery-docs`, reopened by amendment (ADR 0063), not widened

This is not the `change-request` pattern. ADR 0060 widened `delivery-docs`'s own membership test to admit a
type no contract test passed. Here, one contract's test already admits the type: `discovery-docs`'s own
membership clause, "exists to decide whether to build something, before anyone commits to building it"
(`discovery-docs.md:33-34`), fits a project brief without strain on that sentence alone. **What blocks
admission is not the test; it is the contract's own closure statement**, "`discovery-docs.md:6`: "Members:
`business-case`, `user-persona`. The family is closed at two." That closure recorded
[ADR 0035](decisions/0035-prototype-brief-fails-the-admission-test.md)'s **outcome** for a different candidate,
`prototype-brief`, whose own admission test failed. It was never written as a rule that no fourth candidate
could ever be tested; ADR 0031 said the opposite in advance: a two-member result was "a legitimate outcome and
not a failure of the contract" (`0031:54`), a statement about that research's result, not a permanent ceiling.

The strain the maintainer must weigh, named plainly rather than argued around: the UK Government's own primary
guide states "Approval of the Project Brief is the official start of the project" (BIS 2010, raw-checked,
below), which reads as the commitment trigger itself, not a document that only informs a commitment made
afterward. [ADR 0063](decisions/0063-project-brief-reopens-discovery-docs.md) carries this strain in its body
and states this library's own POSITION on it: approval of the brief commits to **initiating**, to spending
effort finding out whether to proceed, not to **building**; the document that commits to building is a
project charter or PID (unbuilt in this library), or a PRD once the investment is approved. That is the same
distinction prince2.ca draws for the type against PMBOK's charter (below), read onto the family boundary.

#### Admission: retrieved and raw-checked, on a wide named-source base

Every quotation below passed the main loop's raw-text re-check on 2026-09-27.
**At least four independently named bodies publish "project brief" as a written document, not merely a
practice**, and the AXELOS glossary is the strongest of them because it is the standards body itself, not a
practitioner's reading of it.

| Source | What it says | Licence |
|---|---|---|
| AXELOS Limited, *PRINCE2 Glossary of Terms English* v.1.1 (2012, PRINCE2 2009 edition), read via the Internet Archive because the live host no longer serves the file | "Statement that describes the purpose, cost, time and performance requirements, and constraints for a project"; created "pre-project during the Starting up a Project process"; "superseded by the Project Initiation Documentation and not maintained" | AXELOS, all rights reserved: short quotes only, never adapted |
| UK Government, Department for Business, Innovation and Skills, *Guidelines for Managing Projects* (November 2010) | "the Project Brief says why the project is needed, what it must achieve and who should be involved"; "Approval of the Project Brief is the official start of the project" | **Crown copyright, Open Government Licence**: adaptable with attribution |
| prince2.wiki, "Project brief" (practitioner, edition of the underlying manual not stated on the page) | "a short, high-level overview of the project, created during the starting up a project process by the project manager"; the composition list begins "background, objectives, scope" and continues, per the page, through constraints, risks, stakeholders and "outline business case"; "the project brief is no longer used in project management activities" once the PID exists | Creative Commons Attribution (site states it; adaptable, but AXELOS marks are used under a permission of unstated scope, so this library describes structure in its own words rather than adapting the page's text directly) |
| NSW Health, *Project Brief Template for Projects Valued at Less than $10 million* (v3.0, 2010) | "This template is mandated for the development of project briefs for projects valued at less than $10 million"; "The Project Brief is in four Parts" | Not stated; qualifies the **heavyweight** sense of the name (below), not the one this bundle builds |
| Treasury Board of Canada Secretariat, *Guide to a Project Brief* | "a project brief must be appended to the Treasury Board submission"; "a project brief is to be supported by a business case, project charter and project management plan" | Not stated; also the heavyweight sense |
| UK Government Functional Standard GovS 002 v2.1, read via a third-party mirror because the official host returns 403 | "project brief:" (a glossary heading in Annex B) | Confirms the term is standardised in current UK government usage; its definition text could not be recovered this session and is not attributed to this source |

*(Corrected 2026-09-29, when the bundle was built: GovS 002 has no "project brief" entry in Annex B. The
build read [the standard's text](../../templates/project-brief/project-brief_research-log.md#what-the-checks-caught-and-what-was-not-read) end to end, and the
term is not among Annex B's defined terms. The one passage naming a brief is in the body, among the senior
responsible owner's accountabilities: the vision, justification and outcomes "are documented in a programme or
project brief". The row's conclusion stands, since the term is in current UK government use, but it is in
the body, not the glossary.)*

**Against this, PMI does not name "project brief."** The PMI *Lexicon of Project Management Terms*, version
5.0, the exact URL this task's research specified, was fetched and raw-checked: "project brief" is absent as a
case-insensitive substring across 80,417 extracted characters, while "Project Charter" and "Version 5.0" both
pass. The 2017 edition (v3.2), read from a third-party mirror and therefore corroboration rather than the
load-bearing source, lacks the term too. **The catalog's "PMBOK 7 (new)" methodology credit is unsupported by
either document**; the PMBOK 7 Standard's own paywalled body was not read, so an isolated mention there cannot
be ruled out, but nothing raw-checked supports the credit. PM² (v3.0 guide, 345,797 characters, raw-checked)
does not use the term either; its Initiating phase produces a Project Initiation Request, a Business Case and
a Project Charter as three separate named artefacts, none called a brief.

**The composition question, where two AXELOS-adjacent sources disagree, and the gap-fill this task specified
resolves in favour of caution.** The official AXELOS glossary itself names only "purpose, cost, time and
performance requirements, and constraints" as the brief's content; it does not itemise background, objectives,
risks or stakeholders as named sections, and its separate "start-up" entry lists "the outline Business Case,
Project Brief and Initiation Stage Plan" as three parallel outputs rather than nesting the business case
inside the brief. **The seven-item composition list this research otherwise leans on (background, objectives,
scope, constraints, risks, stakeholders, outline business case) is prince2.wiki's own synthesis, of an edition
the page does not state**, not the AXELOS glossary's wording. The build must attribute that list to prince2.wiki
by name, not to "PRINCE2" or "AXELOS" generically, and the companion must say plainly that the one official,
freely-readable AXELOS source is thinner than the practitioner synthesis the section design leans on. **The
one candidate that would have settled this, AXELOS's own Appendix A.19 product description in PRINCE2 Agile
2016, is unreachable**: its host, `publications.axelos.com`, no longer resolves at all, and no archived
snapshot exists. Record this as a closed research gap, not a further task.

**What was not read, stated as plainly as `issue-log`'s spec states it.** The PRINCE2 6th (2017) and 7th
(2023) edition manuals are behind a subscription and were not read; the one AXELOS glossary source read is the
2009 edition. The APM Body of Knowledge 7th edition is members-only and was read only as a boundary source (its
one usable quote is below), not as a composition source.

#### Boundaries with each named neighbour

**Not `business-case` (purpose settled; timing contested).** The purpose boundary is solid and already
adopted in this library's own text: the brief is "a short overview for starting up a project, not an
investment case" (`business-case_guide.md:17`). The **timing** boundary is not as clean as the earlier research
pass reported: PMStudyCircle's "the business case is created first, before the project is approved" describes
one order, but the BIS guide's "Approval of the Project Brief is the official start of the project" makes the
brief itself the trigger a business case might follow, not a document that only summarises a decision already
made. The companion must report this boundary as contested on timing and settled only on purpose (justify an
investment, versus define a project already approved to be started).

**Not a `project-charter`/PID (POSITION, where sources split three ways).** prince2.ca's named comparison:
"The main difference in purpose is that the approved Project Brief gives the project manager the authority and
resources to complete the work necessary for the Initiation Stage" and "does not give authorization to
complete the project activities" (sequenced, different authorization scope). Asana: "A project charter
formally authorizes a project and grants the project manager authority to allocate resources. A project brief
summarizes key details to align the team" (distinct, different authority, not sequenced). Smartsheet: "A
project brief is a simplified project charter" (same document, lighter weight). The APM Body of Knowledge lists
"problem statement", "project brief" and "project charter" as three interchangeable common-usage names for one
undifferentiated project rationale, the strongest evidence in this set that the name can collapse rather than
compete. **This library's own POSITION, stated because the sources do not settle it**: approval of a project
brief authorizes initiating, spending effort to find out whether and how to proceed; a project charter or PID
authorizes building. The companion states this as an adopted choice, not a reported fact. **`project-charter`
(catalog alias PID) inherits nothing from this ruling** and must pass ADR 0030's admission test on its own
evidence, per the method ADR 0049 already established for a sibling catalog category.

**Not a product brief or PRD (the weakest-evidenced boundary; label it as inferred).** No source read
contrasts "product brief" with "project brief" by name in one sentence. Productboard: a product brief "is a
foundational document that captures the essence of a product opportunity or initiative before teams commit to
building solutions", answering why to build a product; Storyflow frames a project brief as answering "what you
are doing and why" at the initiative level. The distinction (product-scope versus initiative-scope) must be
labeled inferred from triangulation, not cited as a settled contrast.

**Not a creative or design brief (clean).** SHERPA Global: the project brief is "the bird's-eye view of the IT
project"; the creative brief instead "defines how to best connect with the target audience by clarifying their
needs and motivations". Storyflow adds a structural claim: "The project brief is the parent document" and
"creative, design, and campaign briefs nest inside it".

**Not a project proposal or one-pager pitch.** Storyflow distinguishes the brief from a scope of work, "the
detailed, often contractual list of exactly what will be delivered", and separately states "A project brief is
a lightweight alignment document" that "defines what you are doing and why", where a plan "defines how and
when". A proposal or pitch document sells a decision not yet made; this bundle's brief documents one that
enough of a mandate already exists to start exploring (the sense the BIS trigger describes). The distinction
between a persuasive pitch and this library's brief is this library's own framing, not a single named source's
contrast, and the guide should say so.

**Not the Project Canvas (medium, not content).** Antonio Nieto-Rodriguez's named Project Canvas is "a one-page
template" with "14 dimensions", built because "project management methods have tended to be too complex to be
easily understood and applied by non-experts". No source treats a canvas as a synonym for a brief; they differ
in form, a diagram meant to be read at a glance versus prose in sections, not in what they cover.

**Not the NSW Health / Treasury Board of Canada heavyweight sense, named and put out of scope.** Two named
public-sector sources publish something also called "project brief" that is large, iterative and gate-adjacent:
options analysis, capital and recurrent cost estimates, a formal risk table, resubmission "at regular and
meaningful intervals throughout the life-cycle of the project" (TBS Canada). **This bundle builds the
PRINCE2/UK BIS sense: short, pre-project, superseded once initiation documentation exists.** The companion
must name the heavyweight sense explicitly as a different document under the same name, out of scope here, so
a reader who found this bundle searching for NSW Health's or TBS Canada's shape is told plainly they want a
different document, not that theirs does not exist.

#### Family fit: eight contracts exclude it as written; one admits it with strain

Every other family contract was tested against the type's own membership language and excludes it, several by
direct analogy to the already-shipped `business-case`:

| Family | Verdict | Why |
|---|---|---|
| `strategy-docs` | excludes | Names `business-case` as its own worked exclusion example, "a one-time, phase-bound artifact... this is why business-case is not a member" (`strategy-docs.md:41-45`); a project brief is at least as phase-bound |
| `delivery-docs` | excludes | Its five admitted verbs (define, decompose, verify, change, announce) describe acting on an already-agreed unit of work (`delivery-docs.md:11`); a brief precedes and scopes the project itself |
| `decision-docs` | excludes | "a technical decision-or-design artifact of the develop phase" (`decision-docs.md:11`); a brief is not a technical design record |
| `governance-docs` | excludes | Names `business-case` as its own worked exclusion, "an event-driven or phase-bound artifact (an incident postmortem, a business case) does not [belong], however operational it feels" (`governance-docs.md:24`) |
| `qa-docs` | excludes | "a verification artifact of the develop phase" (`qa-docs.md:12`); a brief plans nothing about verifying a product increment |
| `process-docs` | excludes | Its own contract text routes a forward-looking candidate away from itself: "discovery-docs before a decision, strategy-docs for direction, delivery-docs for the work itself" (`process-docs.md:23`) |
| `standing-standards` | excludes | "the output of a phase belongs to a phase family" (`standing-standards.md:43`); a brief is written once per project, not consulted repeatedly unchanged |
| `communication-docs` | excludes | "the document owns none of its own facts" is this family's defining property (`communication-docs.md:25`); a brief originates its own content and is not periodic |
| `discovery-docs` | admits, with strain | Its own membership test fits: "exists to decide whether to build something, before anyone commits to building it" (`discovery-docs.md:33`). The strain is the BIS "official start of the project" line, carried into ADR 0063's body as a named POSITION rather than smoothed over |

No fallback family exists on this evidence. If the maintainer's ruling to reopen were instead a ruling not to
build, there would be no other family this research found that admits the type; the record would read like
ADR 0035's, a legitimate negative outcome, not a search failure.

#### Structure and sections per size

**Sizes: `[lean, full]`, provisional, and full stays short.** Two sources that speak to length agree it should
stay brief: prince2.wiki's own quality bar is "short, focused" and "SMART"; Smartsheet, describing the
collapsed-with-charter camp, says "It should be a single page long, and anyone should be able to understand it
at a glance." BIS, the primary source, does not state a length. The one long confirmed example, NSW Health's
20-plus fields across three parts, is explicitly the heavyweight sense this bundle puts out of scope. **`full`
therefore does not mean heavier in the NSW Health/TBS Canada sense; it adds the two sections the lean variant
omits, and nothing about options analysis, cost breakdowns or procurement.** The contract permits `[lean]`
alone if the build's own research shows the second weight does not earn its place (`discovery-docs.md:89`);
this spec's judgment is that it does, because `Project Approach` and `Relationship to Other Documents` are
real, separately-named content the lean size would otherwise have to compress out entirely.

| Section | In lean | What it carries |
|---|---|---|
| **Background and Mandate** | yes | Where this came from and who asked for it: the mandate, "often as simple as an email" from a senior manager (BIS), that triggers Starting Up a Project and is expanded into the brief (prince2.wiki: created "during the starting up a project process") |
| **Objectives** | yes | What the project must achieve, stated so a reader can tell later whether it did. BIS's own checklist: "Objectives - achievable and measurable (SMART)"; prince2.wiki confirms SMART as the brief's own quality bar |
| **Scope and Exclusions** | yes | What is in, and, named as its own field, what is explicitly out: BIS's checklist item "Scope - what in and what's out", and WorksBuddy's finding that the exclusions half is "the section that most teams skip" and the one that "prevents the most expensive misunderstandings." **A named, mandatory field, not folded into a general scope paragraph** |
| **Outline Business Justification** | yes | Why this is worth doing, in outline only, plus a statement that a fuller comparison of options (including doing nothing) will be brought to a named approval gate by a `business-case` document. Sourced to prince2.wiki's "outline business case" as one brief component; bounded by `business-case_guide.md:17`, which this section must not cross into |
| **Constraints and Who Should Be Involved** | yes | Known constraints on the work, and the people who need to be part of it, sourced to BIS's own sentence, "the Project Brief says why the project is needed, what it must achieve and who should be involved." **Not** sourced to a "project management team structure" component: that phrase failed raw-text verification against prince2.wiki and is not confirmed as a stated part of the brief by any source read this session |
| **Decision Requested** | yes | What approval is being asked for, from whom, and what happens to the answer: proceed to develop the business case, proceed to initiation, or stop. One named approver. **POSITION**: this section exists because the family's contract obliges each member to say which document takes over (`discovery-docs.md:49-51`), not because a named source specifies this as a brief component |
| **Project Approach** | full only | How the work will be approached (build, buy, or a mix). Named as a brief component by prince2.wiki; not elaborated in any source read this session, so the guidance text here is labeled this library's own, not attributed to PRINCE2 |
| **Relationship to Other Documents** | full only | Where this document sits against the mandate, the business case, and initiation documentation (a project charter or PID), naming plainly that neither `project-charter` nor a PID is built in this library. **POSITION**: this section is how the template answers the same contract obligation (`discovery-docs.md:49-51`) at the size that has room for it, not a sourced composition item |

*(Corrected 2026-09-29, when the bundle was built. Five points in this table were settled otherwise by the
build's research, each recorded with its quotations in the
[research log](../../templates/project-brief/project-brief_research-log.md#what-the-checks-caught-and-what-was-not-read):
(1) "project management team structure" is verbatim on prince2.wiki's starting-up page, though absent from
its project brief page, so Constraints and Who Should Be Involved may cite it there;
(2) Decision Requested and Project Approach are sourced, not only the library's position, because the
starting-up page makes the request to initiate the process's final output and names "the project approach",
and Oxford City Council's and Bestoutcome's templates carry both an approvals block and an approach section;
(3) the BIS items this table quotes for Objectives and Scope come from BIS's start-up checklist, not from its
list of the brief's contents;
(4) WorksBuddy's "the section that most teams skip" is an assertion on a vendor page, not a finding, and the
bundle does not repeat it as fact;
(5) an outline estimate of time and cost is adopted inside Outline Business Justification, labelled
illustrative, because the AXELOS definition and both BIS lists name time and cost. Costed estimates stay out,
as below. Options analysis also stays out, but as this library's position rather than a gap in the sources,
since Oxford City Council's template has a "Project Options" section of its own.)*

**What stays out at any size, named so a reader is not left to guess:** options analysis, capital or recurrent
cost estimates, a formal risk-scoring table, and resubmission across the project lifecycle. Those are the
NSW Health / Treasury Board of Canada heavyweight sense, out of scope by the design choice above, and the
companion says so rather than leaving the omission silent.

#### Metadata

| Field | Value | Why |
|---|---|---|
| `family` | `discovery-docs` | ADR 0063, reopening the family at its own membership test |
| `phase` | `discover` | The only value the contract allows; a project brief precedes commitment, like both existing members |
| `sizes_available` | `[lean, full]` **provisional** | Reasoned above; the contract allows `[lean]` alone if the build's own research disagrees |
| `status` | `beta` | Every bundle |
| `methodology` | `PRINCE2` | The one methodology this research confirmed by an official-tier source (the archived AXELOS glossary); the catalog's `PMBOK 7 (new)` is corrected below |
| `pairs_with` | `[]` | Checked against pm-skills `origin/main` with the direct-contents call on 2026-09-27 (68 skills returned). Two near-name matches were read and ruled out: `foundation-meeting-brief` (a private meeting-prep document, not a project-initiation document) and `develop-solution-brief` (a technical-solution pitch at `phase: develop`). No pairing exists |
| `related_templates` | `[business-case, user-persona]` **provisional** | The sibling whose outline it absorbs and already cites by name, and the family's other member. `project-charter` is deliberately not listed: it is not built and this ruling does not admit it by inheritance |
| `aliases` | `lightweight charter` and `project one-pager` kept, both flagged | "Lightweight charter" encodes the Smartsheet "simplified charter" camp as settled fact when the strongest sources (PRINCE2, BIS) describe a per-project pre-initiation product regardless of size, not a small-project variant; the critic named this as a maintainer-review flag, not a rewrite performed here. "Project one-pager" is what a reader wanting a persuasive pitch or proposal types, the boundary this spec draws above; a build decision, not resolved here. *(Resolved 2026-09-30, the maintainer's call: both kept. An alias routes a searcher to the nearest bundle rather than asserting the two are one type, no charter bundle exists to route to instead, and the guide's boundary table redirects a reader who wanted a pitch.)* |

#### Catalog corrections the landing PR must make

Per [procedure 1](decision-procedures.md#1-a-catalog-call-loses-to-research), both `docs/internal/catalog.md`
(entry 71) and `atlas/catalog-data.json` (`id: "project-brief"`), then the regenerated atlas:

1. **`methodology`: "PMBOK 7 (new)" is unsupported and must be replaced or dropped.** The PMI Lexicon, versions
   5.0 (the exact URL specified) and 3.2, were both raw-checked to lack the term entirely while both define
   "Project Charter." PRINCE2 is the methodology this research actually confirmed; correct the field to
   `PRINCE2`.
2. **`purpose`/`formality` flagged, not rewritten here.** "Lightweight project definition for smaller efforts"
   and the relationship note "S variant of Charter" encode only the Smartsheet/NSW-Tasmania reading (a brief
   as a smaller charter scaled to project size). The strongest-evidenced sources describe a per-project,
   pre-initiation product used regardless of size. Flag for the maintainer's read at landing; do not silently
   rewrite a catalog row this record did not adopt a final wording for.
   *(Resolved 2026-09-30, the maintainer's call: `purpose` now reads "Ask a named approver for authority to
   start initiation, before anyone commits to building", `when_used` drops "small/internal projects", the
   relationship reads "precedes Business Case and Charter", and the note no longer calls the brief a
   smaller charter. `formality` stays `lightweight`, because the document is short by design.)*
3. **`relationships`** currently reads `[Charter]` alone. Add `Business Case`, since the type's own admission
   evidence (the shipped `business-case` bundle's boundary text) is a stronger, closer relationship than the
   unbuilt charter.
4. **`built`, `state`, `state_note`** flip only when the bundle itself lands; this record specs and reopens the
   family, and does not build.

#### `pairs_with`: no pairing exists

`gh api repos/product-on-purpose/pm-skills/contents/skills --jq '.[].name'`, run 2026-09-27, returned 68 skill
names. None is `project-brief` or a plausible variant. Two names containing "brief" were read in full and
ruled out: `foundation-meeting-brief` (a private, pre-meeting tactical document, never shared with attendees)
and `develop-solution-brief` (a technical-solution pitch document at `phase: develop`, bridging problem
understanding to detailed specification). `tool-design-sprint-brief` and `tool-foundation-sprint-brief` were
not read in full, since their names alone place them as sprint-kickoff briefs scoped to a five-day exercise
rather than a whole project, the same neighbouring-artifact pattern ADR 0035 found for `prototype-brief`
candidates. `pairs_with: []` is the honest declaration.

#### Risks for the build and review

1. **The composition attribution is this spec's main correctness risk.** The section design above leans on
   prince2.wiki's seven-item list, not the thinner official AXELOS wording. A build or review that quietly
   upgrades "prince2.wiki says" into "PRINCE2 says" throughout the companion reintroduces exactly the defect
   this section works to avoid. Every Anatomy subsection must name its actual source (prince2.wiki, BIS, or
   POSITION), not "PRINCE2" generically.
2. **The family-reopening question is a maintainer decision this spec presents, not one it resolves.** The
   2026-09-27 ruling settles it for this run, but the ADR must state the strain (BIS's "official start of the
   project") in its own body, not in a footnote, so a future reader does not find the closure re-asserted
   without the reason it was lifted.
3. **`project-charter` sits in the same catalog category and shares this type's purpose.** Any research run
   for it will be tempted to inherit this ruling's family-fit reasoning wholesale. Per ADR 0049's own method,
   it must be tested on its own admission evidence; this record settles nothing for it.
4. **The AXELOS glossary is 2009-edition and all-rights-reserved.** The companion may quote it briefly (as
   this spec does) but must not adapt its wording into template guidance text; BIS, Crown copyright under the
   Open Government Licence, is the adaptable source for anything beyond a short quote.
5. **The build workflow's templates stage has repeatedly copied the worked example's own scenario into GOOD
   and WEAK illustrative text**, a defect no lens currently catches on its own: `tier2-specs.md:1498-1500`
   records that on `change-request`, "the main loop found two more that no lens flagged, the templates' GOOD
   examples reusing the example's scenario and the example repeating the thread's known sharing contradiction."
   This bundle's example uses Acme Analytics' Question-First Entry initiative; the GOOD and WEAK text in every
   guidance comment must use a scenario that is **not** that initiative, checked by grepping the template for
   the example's own nouns (`Dana Okoro`, `Priya Nair`, `Question-First Entry`, `Meridian Freight`) before the
   review closes.
6. **No pm-skills pairing exists, and none is expected to appear.** Not a blocker, but the bundle gains no
   cross-repository routing benefit from being built, unlike `issue-log` and `change-request`.

#### What landing this bundle closes elsewhere

1. **The `discovery-docs` contract moved to `0.2.0` in the spec PR**, with ADR 0063, and every place that said
   the family was closed or complete at two got a dated correction there. The landing PR changes the Members
   line from "not yet built" to the build date.
2. **`business-case`'s boundary text needs no edit; its worked-example callout does.**
   `business-case_guide.md:17`, `business-case_companion.md:315-317` and both templates' "NOT a project brief"
   lines already state the boundary this bundle must agree with, and the new companion agrees with them rather
   than restating the boundary differently. But `business-case_example.md:16-18`'s callout, "ahead of
   everything except its sibling user persona and the product vision it builds on," becomes false once this
   example exists (see the example section's contradiction 6, below), and needs a one-line dated correction in
   the same change.
3. **`project-charter`'s eventual research owes ADR 0049's method**, testing its own admission evidence rather
   than inheriting this ruling by catalog-category proximity.
4. **The catalog entry**, per procedure 1 above: both `docs/internal/catalog.md` and `atlas/catalog-data.json`,
   then the regenerated atlas, when the bundle lands.
5. **This page's Progress table.**

#### The example

**A project brief for the Question-First Entry and Modelling Defaults initiative**, dated **2026-01-16**:
two days after the [product vision](../../templates/product-vision/product-vision_example.md) (agreed 2026-01-14) and four
days before the [business case](../../templates/business-case/business-case_example.md) (dated 2026-01-20). This keeps the
family's chronology obligation: the example must precede what it leads to (the business case's own funding
decision, and any future initiation documentation) and must not cite either as existing. It sits after the
[user persona](../../templates/user-persona/user-persona_example.md) (2026-01-05), which itself claims only to sit "ahead
of even the product vision" (`user-persona_example.md:18`); this brief's later date does not disturb that
claim. `README.md:224` (as of `45019c5e`) separately calls the persona "the earliest document in the library", a stronger,
published claim this date also respects.

**Facts it reads, by file and line, and nothing it must not.** From `business-case_example.md`: the sponsor,
Dana Okoro, VP Product (line 4); the telemetry the brief's Background section shares with the case, that "only
31 percent build a second dashboard view within 14 days of signup" and that "revenue per new account has been
flat for five quarters" (lines 34, 41), both Acme's own pre-existing telemetry rather than an output of the
case itself; and the December leadership review that supplies the brief's mandate, "the flat revenue-per-account
trend surfaced at the December leadership review and finance asked for a funding decision" (line 52-53). From
`user-persona_example.md`: the Recurring Analyst (lines 43-47) as the segment this initiative serves, and
Priya Nair, PM, Reporting (line 6), as this brief's named Project Manager.

**What it must not cite or contain, because doing so would contradict an already-shipped sibling.**

1. **No staged case vocabulary.** `business-case_example.md:5` states plainly, "Acme has no staged case model
   (no SOC/OBC/FBC)". The Outline Business Justification section must not call itself an SOC, OBC or FBC.
2. **No Reporting Platform Modernization program, and no Marta Reyes.** That program and its program manager
   are a mid-2026 fact of the delivery-docs and governance-docs thread (`change-request_example.md:8`,
   `issue-log`'s ISS-11 raised 2026-06-14), five months after this brief's date. The brief uses `business-case`'s
   own investment name, "Question-First Entry and Modelling Defaults," as its project name.
3. **No pre-computed benefit range or financial metrics.** The 6-11 percentage point second-view lift, the
   NPV, IRR, payback and ROI figures (`business-case_example.md:78-102`) are the business case's own later
   analysis. The brief may cite the early prototype's 71 percent question-resolution finding as an existing
   fact (it predates the case, per the case's own framing), but must not anticipate the case's computed
   benefit range or financial metrics.
   *(Corrected 2026-09-29, when the bundle was built: the allowance for the 71 percent figure is withdrawn,
   and the example does not cite it. No sibling dates the prototype, and every document that reports the
   figure is dated after this brief, so it could not be shown to predate the brief.)*
4. **No options decision.** The brief defers the comparison of options, including doing nothing, to the
   business case; it must not commit to OPT-3 or name it, since choosing between options is exactly the job
   `business-case_guide.md:17` reserves for the other document.
5. **No initiation documentation, project charter or PID cited as existing.** None is built in this library.
6. **A sibling's own worked-example callout becomes false the day this bundle lands, and that is a correction
   this landing owes, not a constraint on the new example.** `business-case_example.md:16-18` states the case
   "sits near the start of the shared timeline, ahead of everything except its sibling user persona and the
   product vision it builds on." A brief dated 2026-01-16 makes that sentence false the moment it ships. The
   landing PR must add a one-line dated correction to that callout, the same pattern already used for
   `README.md:224` (as of `45019c5e`)'s "earliest document" claim once a still-earlier document exists. *(Done 2026-09-29: the callout,
   now `business-case_example.md:16-20`, carries that correction.)*

**Decision requested, closing the loop honestly.** The brief asks Dana Okoro, as executive, to authorize
proceeding to a funding decision, to be brought to the leadership review on 2026-01-26, the same date
`business-case_example.md:118` already names. The brief's own "what happens to the answer" is exactly that
business case, arriving four days later: nothing here is invented for the brief to hand off to.

---

### experimentation-docs (founding members): the experiment design doc and the experiment readout

**`experiment-design-doc`** (bundle id the same as the catalog id; see Bundle ids) - `experimentation-docs`,
**phase measure**, sizes `[lean, full]` **provisional**, methodology **`growth/dual-track`** (the
catalog's own value; descriptive only, not gated, per [the contract](contracts/experimentation-docs.md)
section 2). Catalog id `experiment-design-doc` (catalog row 142, `docs/internal/catalog.md:208`; verbatim
at `atlas/catalog-data.json:3615`). Catalog name "Experiment Design doc". Catalog aliases: `A/B test plan`,
`experiment brief`, `test design`. Catalog category: Analytics / Measurement. Catalog owner: PM / Data
Scientist. Catalog purpose: "Define hypothesis, variants, metrics, and analysis for an experiment."
Catalog contents: hypothesis, variants, primary/guardrail metrics, sample size, duration. Catalog
`stage`: growth. Catalog `formality`: standard. Catalog `rarity`: occasional. Catalog `relationships`:
`["Experiment Readout"]`. Catalog `size_variant`: S/M. Catalog `tier`: 2, `tier_inferred`: true,
`must_have`: false, `built`: false, `state`: candidate.

**`experiment-readout`** (shortened from the catalog id; see Bundle ids) - `experimentation-docs`, **phase measure**, sizes `[lean, full]` **provisional**, methodology
**`growth`** (catalog value; descriptive only). Catalog id `experiment-readout-results-report` (catalog
row 143, `docs/internal/catalog.md:209`; verbatim at `atlas/catalog-data.json:3641`). Catalog name
"Experiment Readout / Results report". Catalog aliases: `A/B test results`, `experiment analysis`.
Catalog category: Analytics / Measurement. Catalog owner: Data Scientist / PM. Catalog purpose: "Report
experiment outcomes and decision." Catalog contents: results, significance, learnings, decision, next
steps. Catalog `stage`: growth. Catalog `formality`: standard. Catalog `rarity`: occasional. Catalog
`relationships`: `["Experiment Design"]`. Catalog `size_variant`: S/M. Catalog `tier`: 2, `tier_inferred`:
true, `must_have`: false, `built`: false, `state`: candidate.

Both are founding members of `experimentation-docs`, the family that
[ADR 0066 (adopt the experimentation-docs family contract)](decisions/0066-adopt-experimentation-docs-family-contract.md)
founds at `phase: measure` with no members yet. Everything below is this spec's own research, run against
the 2026-10-05 admission sweep (`_local/research/2026-10-04_admission-sweep-4/`, gitignored) and its
main-loop quotation re-check.

#### Demand: almost none, and it is honest to say so

**Zero shipped bundles route a reader to either type.** A case-insensitive search of every file under
`templates/*/*.md` for "experiment design", "experiment readout", "experiment brief", "A/B test plan" and
"A/B test results" returns no match at all.

The only inbound links on record are three **unbuilt** catalog rows, confirmed against `manifest.json`:

- `docs/internal/catalog.md:55`, row 22, Opportunity Solution Tree: "feeds Experiment Design."
- `docs/internal/catalog.md:60`, row 27, Concept Test / Validation Brief: "overlaps Experiment Design."
- `docs/internal/catalog.md:212`, row 146, Funnel Analysis: "feeds Experiment Design."

None of `opportunity-solution-tree`, `concept-test-validation-brief`, or `funnel-analysis` is in
`manifest.json`; all three are themselves `candidate` rows, not shipped bundles. **This matches
[ADR 0066](decisions/0066-adopt-experimentation-docs-family-contract.md)'s own consequence note** ("demand
is thin... almost no shipped bundle that routes a reader to either type") and should not be inflated in
either bundle's companion. This family is built on the maintainer's own preference under
[ADR 0041 (maintainer preference sets the build order)](decisions/0041-maintainer-preference-sets-the-build-order.md),
not on an inbound gap the library created.

#### Admission: both members clear the test, independently, across three lineages

The test is [ADR 0030 (templating scope: Markdown documents)](decisions/0030-templating-scope-markdown-documents.md)'s.
A candidate type is templatable when a named source publishes it as a written document. One qualifying
source is sufficient.

Every quotation below passed a raw-text check against the URL cited. Most passed the main loop's re-check
on 2026-10-05. A few were reattributed to a sibling URL by the sweep's corrections file, and the rest passed
a second main-loop check on 2026-10-06. The sweep folder holds all three records (`recheck-out.json`,
`corrections.json` and `selfcheck-out.json`). Source names are given exactly as each page states them,
because the Bundle ids section below relies on what named sources call each document.

**`experiment-design-doc`**

*Product experimentation.*

- **GrowthBook.** Its skills reference ships a fill-in block titled "Experiment spec". The block has a
  field named "Estimated sample size" and states a hypothesis format, "If we change X, then Y will
  improve, because Z"
  (<https://github.com/growthbook/skills/blob/main/skills/experiments/references/experiment-design.md>).
- **LaunchDarkly.** Its guide names the type: "Experiment design documents contain the definition of why
  you are running this test". The guide places the document under a step it calls "Create a roadmap"
  (<https://launchdarkly.com/docs/guides/experimentation/designing-experiments>).
- **Optimizely.** Its advanced plan names "Experiment hypothesis", "Business goals", "QA checklist" and
  "Parameters for significance" among its sections
  (<https://docs.optimizely.com/experimentation-strategy/docs/create-an-advanced-experiment-plan-and-qa-checklist>).
  A sibling page tells teams to "create this document as a presentation slide, an email template, or a
  wiki page", as a "shareable document that multiple stakeholders can reference"
  (<https://docs.optimizely.com/experimentation-strategy/docs/create-a-basic-experiment-plan>). A fuller
  section count for the advanced plan is summary-derived and is not restated here.
- **Amplitude.** Its blog names a document template "Experiment Brief", which is one of the catalog's own
  aliases. The template's fields include "guardrail metrics", "Total Sample Size", "Experiment Event Name"
  and "Variation Designs", and it names "Do No Harm" as a test type. Its four phases are Plan, Configure,
  Monitor, and Analyze and Decide (<https://amplitude.com/blog/experiment-brief>). A fuller field count is
  summary-derived and is not restated here.
- **Adam Fishman.** Fishman's template has parts that include "The Why", "The Plan" and "The
  Results", with "Minimum Detectable Effect" as a field. Its stated reason to pre-commit a decision rule is
  to "establish a plan for what you'll do after the results come in"
  (<https://www.fishmanafnewsletter.com/p/experiment-document-template>). Do not name "Problem Statement"
  or "Learning Objectives" as its headings, because both failed the raw-text check.

*Academic preregistration.* AsPredicted's public sample instance confirms, verbatim, "What's the main
question being asked or hypothesis being tested in this study" and "Specify exactly which analyses you
will conduct" as numbered questions (<https://aspredicted.org/MQQ_B7B>; **do not attribute the platform to
Wharton or the Credibility Lab as confirmed text - both failed the raw-text check on every page read**).
The Open Science Framework names "Registered Report Protocol" among its named preregistration templates,
"Standard, comprehensive, and general purpose preregistration form" for its default, and names its
publisher, "Center for Open Science" (<https://help.osf.io/article/330-welcome-to-registrations>).
*(Corrected 2026-10-08, when `experiment-design-doc` was built: OSF names no default. The same article says
"We do not recommend a specific template as we do not know the details of your study, your institution's
policies (if any), or the standards of your community". The "Standard, comprehensive..." line describes one
named template, "OSF Preregistration", which the article marks "Most commonly used", the nearest it comes
to a default; see [18] in the
bundle's [research log](../../templates/experiment-design-doc/experiment-design-doc_research-log.md#what-the-checks-caught-and-what-was-not-read).)*

*Public-sector evaluation.* HM Treasury's Magenta Book requires "evaluation plans, protocols and
statistical analysis plans" as pre-registered written artefacts, defining pre-registration as "documenting
key elements of the evaluation such as its objectives, research questions, design, data collection
procedures and analytical approach" before data collection begins
(<https://assets.publishing.service.gov.uk/government/uploads/system/uploads/attachment_data/file/879438/HMT_Magenta_Book.pdf>,
which 301-redirects to the current edition; both quotes were checked against that redirect target).

*Academic/industry checklist, cited for existence, not reproduced.* Fabijan, Dmitriev, Olsson, Bosch,
Vermeer and Lewis's ICSE-SEIP 2019 paper names a pre-launch checklist, "Checklist 1. Experiment Design
Analysis". It also gives a hypothesis template attributed to an external citation, "we predict that..."
(<https://exp-platform.com/Documents/2019%20FabijanDmitrievOlssonBoschVermeerLewis_Three-Key-Checklists_ICSE_SEIP.pdf>).
**The PDF is an authors' preprint marked "Not for redistribution"; any companion citation paraphrases, it
does not reproduce.**

ADR 0030's test needs one qualifying source. The 2026-10-05 research found at least six, in three
lineages: product experimentation, academic preregistration and public-sector evaluation.

**`experiment-readout`**

*Product experimentation.* Eppo ships an actual fillable Google Doc template with named section blocks
confirmed verbatim: "Executive Summary," "Key Results: Primary Metrics," "Key Results: Supporting
Metrics," "Deep-Dive," and "Implementation Details and Analysis Notes." **Cite the Google Doc export, not
the landing page**: all five headers failed the raw-text check on
<https://www.geteppo.com/experiment-report-landing-page>, and all five passed against
<https://docs.google.com/document/d/1mWWzaAdTfuQWGp2tHE5NVN6pL-Tx0_JTKlDLZOcmUqw/export?format=txt>
(`corrections.json`, reattributed). Optimizely's documentation prescribes a written results summary whose
sections include "Purpose", "Details", "Lessons Learned" and "Revenue Impact"
(<https://docs.optimizely.com/experimentation-strategy/docs/share-your-results-with-stakeholders>).

*Academic trial reporting.* The CONSORT 2010 Statement (Schulz, Altman and Moher) is a standards-grade,
named, CC BY-licensed checklist whose own title is "CONSORT 2010 Statement". It confirms a "25 item
checklist", organised under named sections that include "Title and abstract", "Discussion" and "Other
information", with a required "flow diagram"
(<https://journals.plos.org/plosmedicine/article?id=10.1371/journal.pmed.1000251>). **Cite this PLoS
Medicine copy, not the EQUATOR Network PDF mirror** - the EQUATOR mirror failed five of its own tested
quotes while this copy of the identical statement passed all of its.

*Public-sector evaluation.* The Behavioural Insights Team's own published Pension Wise trial report
states "The Behavioural Insights Team uses a consistent methodological approach for each" trial and closes
with a section named "Conclusion and policy implications"
(<https://www.bi.team/wp-content/uploads/2017/10/Pension-wise-trials.pdf>). HM Treasury's Magenta Book
(2026 HTML edition) requires "Publishing all evaluation reports," asks "Were there any unintended or
negative impacts" as a distinct evaluation question, and situates the report-writing step as "Prepare
final evaluation analysis and outputs"
(<https://www.gov.uk/government/publications/the-magenta-book/magenta-book-central-government-guidance-on-evaluation-html>).
The same edition elsewhere calls a final evaluation report "rarely the best way to ensure impact and
influence" (self-checked against the same URL), a caution against over-weighting the written report
relative to shorter outputs; not used in the admission argument above, since no other source makes the
same point and the Magenta Book's own report requirement already stands on the three quotes just given.

*A practitioner source, corroborating only.* Tanmayi Sai publishes an "Experiment Readout Template" whose
stated purpose is "Keeping track of the performance of an experiment or feature that you shipped"
(<https://tanmayisai.com/2020/11/20/experiment-readout-template/>; both strings passed the 2026-10-06
check). It is one practitioner's page, so it corroborates the others rather than standing alone.

ADR 0030's test needs one qualifying source. The research found five (Eppo, Optimizely, CONSORT, the
Behavioural Insights Team and the Magenta Book), in three lineages, and Sai's page corroborates them.

#### One document or two, and what the readout's guide must carry

The maintainer ruled for **two bundles** on 2026-10-06, following this library's own `qa-docs` precedent
(`test-plan` and `test-summary-report`), recorded in [ADR 0066](decisions/0066-adopt-experimentation-docs-family-contract.md).
The evidence genuinely splits, and both camps are independently confirmed, not asserted:

- **Merged, one document:** Optimizely's own Confluence-distributed template puts "Results" and
  "Conclusions" on the same page that opens with "Hypothesis" (the four-section ordering - Basics,
  Experimentation Planning, Results, Conclusions - is this spec's own reading of a WebFetch summary, not
  independently raw-checked section by section)
  (<https://www.atlassian.com/software/confluence/templates/experiment-plan-and-results>). *(Corrected
  2026-10-08, when `experiment-design-doc` was built: the order is now read in raw text, as "1 Cover the
  basics", "2 Set a plan for your experiment", "3 Outline your results" and "4 Draw conclusions"; see
  [8] in the bundle's
  [research log](../../templates/experiment-design-doc/experiment-design-doc_research-log.md#what-the-checks-caught-and-what-was-not-read).)* Fishman's
  template puts "The Results" in Part 3 of the same document whose Parts 1-2 are "The Why" and "The Plan."
  Amplitude's "Experiment Brief" closes with a fourth phase, "Analyze and Decide," inside the same brief
  that opened with the hypothesis.
- **Separate, two documents:** GrowthBook's own skill ships `experiment-design.md` as a distinct reference
  file from a separate analysis reference; Eppo ships a readout-only "Report" and nothing on the design
  side; AsPredicted and OSF are pre-only by construction; the Magenta Book names three separate
  pre-registered artefacts (plan, protocol, statistical analysis plan) rather than sectioning one document;
  CONSORT's own checklist item on protocol access treats the protocol and the results report as two
  separately-dated artefacts.

**Because the split is real, the readout's guide must carry a line for teams on the other side of it.**
Recommended wording, in the guide's "when to use / when not to" section: *"If your team keeps one living
experiment document rather than this library's two, fill this bundle's Results, Validity Checks, and
Decision sections into that same document when the test concludes, instead of opening a second file. The
library ships the pair separately because `qa-docs` already teaches the same before-and-after shape; it is
not a claim that every team's practice should split in two."*

#### Structure: `experiment-design-doc` sections per size

| Section | In lean | Traced to |
|---|---|---|
| **Hypothesis** | yes | GrowthBook, LaunchDarkly, Amplitude, Fishman. **POSITION**: the field is left free text, not one prescribed sentence form - five distinct, named hypothesis-sentence conventions were found (GrowthBook's if/then/because; Amplitude's observed/by/expect/leading-to; Fishman's believe/will-know/refuted-if; the ICSE paper's based-on-insight/predict, itself attributed onward; Spotify Confidence's doing-this-for-these-people framing), and no source converges on one |
| **Population, Variants, and Allocation** | yes | GrowthBook's "Variations"; LaunchDarkly's "audience", "variations" |
| **Primary and Guardrail Metrics** | yes | GrowthBook's "Primary metric", "Guardrails"; Amplitude's "guardrail metrics". **Leads with what the PRD does not already ship** - see Boundaries |
| **Minimum Detectable Effect and Sample Size or Duration** | yes | GrowthBook's "Estimated sample size"; Fishman's "Minimum Detectable Effect"; Microsoft ExP's "power calculation sets a lower bound on the number of randomization units" (<https://www.microsoft.com/en-us/research/group/experimentation-platform-exp/articles/patterns-of-trustworthy-experimentation-pre-experiment-stage/>). **The single non-duplicated core this bundle exists to carry** |
| **Decision Rule** | yes | Eppo's named practice, "decision pre-registration": "think through as a team what data would imply what decisions and write down quantitative thresholds," in the form "We will do..." (<https://www.geteppo.com/blog/make-decisions-before-experimenting>) |
| **Tracking and Instrumentation Note** | full only | GrowthBook's "Tracking key suggestion." A pointer to the PRD's own Analytics and instrumentation section, not a restatement of it - see Boundaries |
| **Validity Pre-Commitments** | full only | **POSITION**: no source names this as its own section; it is the 2026-10-05 research's synthesis of Microsoft ExP's falsifiable-hypothesis and SRM-monitoring guidance, pre-committed at design time rather than discovered at readout time |

#### Structure: `experiment-readout` sections per size

| Section | In lean | Traced to |
|---|---|---|
| **Executive Summary** | yes | Eppo's "Executive Summary"; Optimizely's "Purpose" |
| **Context and Setup** | yes | Tanmayi Sai's "Experiment Setup" (self-checked against the page directly, 2026-10-06); Optimizely's "Details" |
| **Key Results: Primary Metrics** | yes | Eppo's named section, "Key Results: Primary Metrics". The 2026-10-05 research reports a Metric / Control / Test / Change / CI / Significant column set under it; the column names themselves were not independently raw-checked. *(Corrected 2026-10-11, when `experiment-readout` was built: the columns are now read in raw text, as one header row, "Metric Control Test Change (abs) Change (rel) CI Sig?"; see [1] in the bundle's [research log](../../templates/experiment-readout/experiment-readout_research-log.md#what-the-checks-caught-and-what-was-not-read).)* A table section; carries PRIORITY and ROW HINT |
| **Key Results: Supporting Metrics** | yes | Eppo's "Key Results: Supporting Metrics", the guardrail/secondary tier. Same table shape |
| **Validity Checks** | yes | **POSITION, UNSOURCED as a named section.** No template read in this pass labels a validity-checks block; the content (sample ratio mismatch, guardrail breach, novelty effect) is sourced only as scattered practice description - Microsoft ExP's "SRMs typically invalidate the A/B test and make any results and metric movements untrustworthy" and "Measure aspects of the product that we don't want to degrade but won't necessarily improve" (<https://www.microsoft.com/en-us/research/group/experimentation-platform-exp/articles/patterns-of-trustworthy-experimentation-during-experiment-stage/>), and GrowthBook's "peeking (deciding on an experiment before it's completed)" and "cherry-picking data" (<https://www.growthbook.io/blog/experimentation-program-mistakes-to-avoid>) and "A sample ratio mismatch is a statistically significant gap between the traffic split you configured and the split your experiment produced" (<https://www.growthbook.io/blog/sample-ratio-mismatch>). The library labels this its own POSITION because the practice is well evidenced even though no source structures it as a section |
| **Deep-Dive** | full only | Eppo's "Deep-Dive". Its companion post reads "Experiment reports discuss the" why, not the what (self-checked fragment, 2026-10-06, against <https://www.geteppo.com/blog/how-to-craft-compelling-impactful-experiment-reports>; the surrounding sentence is this bundle's own paraphrase) |
| **Decision: Ship, Iterate or Stop** | yes | **The decision requirement is sourced; the exact triad is not.** Sai's template closes with "Next Steps" (self-checked, 2026-10-06). Per the 2026-10-05 research's own reading of that section, not independently re-checked word for word, its content names rollout, iteration, or discontinuation; Fishman pre-commits the same choice earlier, in The Plan. No source uses "ship, iterate or stop" verbatim - that phrasing is [the contract's](contracts/experimentation-docs.md) own section 1 wording, adopted by the maintainer, and is a **POSITION** here too. Note the catalog's own guidance-note column (`docs/internal/catalog.md:209`) independently carries "ship/iterate/kill decision" - a different third word, equally unsourced; see Catalog corrections *(Corrected 2026-10-11, when the bundle was built: the catalog note now reads "ship, iterate or stop decision", labelled as this library's POSITION.)* |
| **Decision Owner** | yes | **POSITION, UNSOURCED.** No source read requires naming who made the call. The spec keeps it in lean because the contract finishes a readout when its decision is recorded, and a recorded decision names who made it, as an ADR names its decision-makers |
| **Next Steps and Owners** | yes | Eppo's "Next Steps", each action item carrying an explicit owner |
| **Implementation Details and Analysis Notes** | full only | Eppo's own section of that name; CONSORT's formal separation of Methods from Results |
| **Further Analysis** | full only | Sai's optional "Further Analysis" (self-checked, 2026-10-06) |

*(Corrected 2026-10-11, when `experiment-readout` was built: Eppo's own template puts "Next Steps" straight after the Executive Summary, before both Key Results sections, so it leads with what happens next. This spec's order, which puts the decision and its next steps after the evidence, is therefore the library's choice rather than Eppo's, and the companion names it as one; see [1] in the bundle's [research log](../../templates/experiment-readout/experiment-readout_research-log.md#what-the-checks-caught-and-what-was-not-read).)*

#### Boundaries with each named neighbour

- **The other member.** The design doc states its hypothesis, metrics, and decision rule before the test
  runs; the readout reports what ran against that same plan. Per [the contract](contracts/experimentation-docs.md)
  section 4, both bundles' examples chain onto one shared test - see The worked example, below.
- **The spike report (`decision-docs`).** `templates/spike-report/spike-report_companion.md:188`: "A
  refuted hypothesis is a successful spike." A spike reduces uncertainty about a technical or design
  question; it has no control group, no allocation, and no statistical decision rule. The same companion,
  at line 179, calls a spike "a time-boxed research experiment that answers" one question - load-bearing
  vocabulary ("experiment," "hypothesis") this family's companions must place themselves against by name,
  per the contract's own instruction, even though spike-report sits in a different family.
- **`test-plan` and `test-summary-report` (`qa-docs`).** `templates/test-plan/test-plan_guide.md:27`
  names the collision risk from its own side, under the heading *Your tool already has a "test plan"*,
  and distinguishes the document from an execution container. Neither qa-docs member has a hypothesis, an allocation, or a
  statistical decision rule; each verifies a product increment against an agreed specification and grades
  it pass or fail. The shared word "test" is the collision [the contract](contracts/experimentation-docs.md)
  section 1 names as the library's own POSITION. The candidate's own catalog alias "test design" sits one
  word from this bundle's shipped title, "Test Plan" (`manifest.json`); state the distinction on the
  companion's first page, the way `change-request_guide.md` already states its own `rfc` collision.
- **The PRD's "Success metrics" and "Analytics and instrumentation" sections.** `templates/prd/prd_template-full.md:192-207`
  carries primary/guardrail metric placeholders (`{{primary_metric}}`, `{{guardrail_metric}}`,
  `{{measurement_window}}`) nearly identical in shape to this bundle's own metrics section; `prd_companion.md:64`
  names it "a guardrail you must not harm." `templates/prd/prd_template-full.md:209-223` ships an
  "Analytics and instrumentation" section covering measurement readiness. **This is partial duplication,
  not full duplication, and the design doc's companion must lead with what the PRD does not already ship**:
  variants and allocation, minimum detectable effect and sample size or duration, and the decision rule.
  None of these four fields is duplicated anywhere in the library today. A design doc that leads with
  primary/guardrail metrics risks reading as the PRD's own section renamed, the failure mode
  [ADR 0064 (deployment-plan is declined)](decisions/0064-deployment-plan-is-declined.md) records for a
  different candidate.
- **OKR scoring.** `templates/okrs/okrs_example.md:113-127` grades a committed Key Result's final number
  against its target on a 0.0-1.0 scale with no statistical apparatus - a scoring ritual against a
  pre-committed target, not an inference about whether one isolated change caused an effect. An OKR cycle
  can cite a readout's outcome as evidence for a Key Result's grade without the two being the same
  document.
- **The KPI dashboard.** `templates/kpi-dashboard/kpi-dashboard_guide.md:22-23`: "That is a scorecard. A
  dashboard monitors current state; a scorecard compares actual to target at a point in time." A dashboard
  is continuously maintained and live; a readout is produced once, after one concluded test, and is
  finished.
- **Experiment scorecards and results dashboards.** Out of scope under
  [ADR 0030](decisions/0030-templating-scope-markdown-documents.md)'s rule that a live data surface is not
  templated. Optimizely's own documentation describes its Experiment Scorecard as "An Experiment Scorecard
  template consists of" a live, configurable in-tool UI
  (<https://docs.optimizely.com/analytics/docs/understand-your-experiment-scorecard>); Microsoft Research
  independently confirms its own "scorecard" is a machine-generated table inside the experimentation
  platform, not a narrative document
  (<https://www.microsoft.com/en-us/research/articles/treatment-effect-assessment-at-scale-accounting-for-correlated-metrics-and-metric-relevance-in-modern-experimentation/>).
  *(Corrected 2026-10-11, when `experiment-readout` was built: "machine-generated table" is this spec's
  own paraphrase, not Microsoft's wording. The page's own sentence is "A scorecard is a collection of
  metrics used to evaluate the success of a product change or experiment"; see [23] in the bundle's
  [research log](../../templates/experiment-readout/experiment-readout_research-log.md#what-the-checks-caught-and-what-was-not-read).)*
  Statsig's own "Experiment Summary" PDF export is the same kind of snapshot
  (<https://www.statsig.com/updates/update/experiment-summary-pdf>); a similar claim about Split's
  export formats rests only on an unverified WebSearch summary in the 2026-10-05 sweep and is not restated
  as fact here. Neither is adapted as a structural source.

#### Family fit

Settled, not re-litigated here. [The contract](contracts/experimentation-docs.md) section 1 states the
membership test both members must meet: "plans or reports on one discrete test of a hypothesis about the
effect of a change to a product or its market." It also states the two boundary sentences against
standing instruments and pre-build validation. Section 2 fixes the axis at `phase: measure`. That axis
call is labelled the library's own POSITION, per
[decision-procedures.md section 11](decision-procedures.md#11-a-family-contract-asserts-something-about-the-world).
Section 4 fixes the shared-scenario rule this spec's worked example follows. ADR 0066 records why no
existing family admits either type cleanly, and why the maintainer chose two bundles over one. Nothing in
this spec's own research contradicts any of it. This spec's own job is sizing, sections, the worked
example, and the bundle ids the contract left open.

#### Bundle ids

**The bundle ids are `experiment-design-doc` and `experiment-readout`.** The catalog ids stay unchanged in
`atlas/catalog-data.json`, as they did for every earlier shortening.

**`experiment-design-doc` keeps the catalog id.** The library's precedent shortens a catalog id that
repeats its type name behind a category prefix: `change-log-governance` became `change-log`,
`spike-research-spike-report` became `spike-report`, and `test-report-test-summary-report` became
`test-summary-report`. This id has no such prefix to trim. Named sources call the document several
things: GrowthBook says "Experiment spec", LaunchDarkly says "Experiment design documents", Amplitude says
"Experiment Brief" and Fishman says "Creating an Experiment Doc". None of them outweighs the catalog name.
A shorter `experiment-design` would read as the practice of designing an experiment rather than the
document. It would also sit close to `sdd`'s shipped aliases "design doc" and "design document", which
belong to a different family's bundle.

**`experiment-readout` drops the catalog's qualifier.** Here the precedent does apply. `results-report` is
a generic qualifier, playing the role `-governance` played in `change-log-governance`. "Experiment
Readout" is the name the catalog gives first ("Experiment Readout / Results report"), and it matches Sai's
template title. The catalog alias "A/B test results" sits one word from `test-summary-report`'s shipped
alias "test results", so the guide's first line states the distinction.

#### The worked example: the Saved Views adoption-nudge experiment

**The shared-scenario rule (contract section 4) binds both members to one test.** The design doc plans it;
the readout reports the same test against the same plan. The scenario chains onto the existing Acme
Analytics "Saved Views for Dashboards" thread, per the contract's own instruction, and the experiment must
post-date Saved Views' 2.4.0 release: `templates/release-notes/release-notes_example.md:26`, "Release date:
2026-07-21."

**The experiment.** A one-time in-app prompt, shown to a Recurring Analyst after their fifth dashboard view
following the 2.4.0 release, suggesting they save their current filter, date range, and column setup as a
view - testing whether the prompt moves adoption versus a no-prompt control.

**Facts the two examples must carry exactly, with no invention**, each already established in a sibling
file:

| Field | Value | Source |
|---|---|---|
| Primary metric | Saved Views adoption: "Share of Recurring Analysts using a saved view weekly" | `templates/kpi-dashboard/kpi-dashboard_example.md:54` |
| Starting value | 41%, KR2's starting figure; the KPI dashboard carries the same figure at its `last_reviewed: "2026-07-20"` snapshot | `templates/okrs/okrs_example.md:52`; `templates/kpi-dashboard/kpi-dashboard_example.md:6,54` |
| Target this cycle serves | 60% by end of FY26 Q3 | `templates/kpi-dashboard/kpi-dashboard_example.md:54`; `templates/okrs/okrs_example.md:52` (KR2), read with the OKRs' `period` field at `okrs_example.md:3` |
| Metric owner | Priya Nair, whose role the PRD states as "PM, Reporting" | `templates/kpi-dashboard/kpi-dashboard_example.md:54`; `templates/okrs/okrs_example.md:52`; `templates/prd/prd_example.md:5` |
| Guardrail 1 | Weekly active analysts, hold >= 480 (current 495 at the same snapshot) | `templates/kpi-dashboard/kpi-dashboard_example.md:56` |
| Guardrail 2 | Dashboard load error rate does not increase; shared-view permission incidents stay at zero | `templates/prd/prd_example.md:128` |
| Feature instrumented | `view_saved`, `view_switched`, `view_set_default`, `view_shared`, `view_load_error` | `templates/prd/prd_example.md:133-134` |

*(Corrected 2026-10-08, when `experiment-design-doc` was built: the OKRs' `period` field is at
`okrs_example.md:4`, not line 3. The fact it carries, "FY26 Q3 (August to October 2026)", is unchanged.)*

**Dates, chosen to sit cleanly downstream of every document read above and upstream of the OKR close-out
(first product review of November):** design doc drafted 2026-07-30; the experiment runs 2026-08-03 through
2026-08-31 (a four-week window, matching the PRD's own "4 weeks post-rollout, compared to the 4 weeks
prior" framing at `prd_example.md:129`); readout written 2026-09-04. These dates were chosen, not read off
a sibling file, and are recorded here so a reviewer can check them against anything that moves later. No
sibling example ships a Saved Views change inside the window. The one change request in the scenario,
CR-SV-01 (scheduled email delivery for Saved Views), was postponed on 2026-08-14 and shipped nothing
(`templates/change-request/change-request_example.md`, frontmatter and Decision section).

**One residual inconsistency this scenario must route around, not inherit.** `templates/okrs/okrs_example.md:90`
still lists the Saved Views initiative as "in build, spec at 0.3.0," dated 2026-07-27 - six days after
`release-notes_example.md`'s corrected 2026-07-21 GA date. This is a pre-existing contradiction between two
shipped sibling examples. This sweep's research found it, and it is not one of the four residuals that
PR #204 (fix the examples' release-date contradiction) recorded, listed below. It is not this spec's to fix. **Both examples must cite OKRs' KR2 numbers (41%,
60%, Priya Nair) and never its Initiatives-table status line**, which routes around the inconsistency
without resolving it.

**PR #204's four recorded residuals stay out of both examples.**
[PR #204 (fix the examples' release-date contradiction)](https://github.com/product-on-purpose/product-lifecycle-templates/pull/204)
left four inconsistencies unfixed. They are the announcement's "private views since late June"; the
retrospective's 2026-09-14 general availability date; the release notes' known issue promising a fix in
2.4.1 that the test summary defers; and the definition of done's "DEF-2291 shipped in build 2.3.2"
wording. Neither example cites any of the four. The first one matters most here. The 41% starting value
predates the 2026-07-21 release by a day, and the announcement's "since late June" is the only sibling
sentence that would explain it. That sentence is a recorded residual, so neither example explains the
figure's timing. Both cite 41% as KR2's starting value and leave it there.

**A scenario this spec considered and did not choose.** `templates/okrs/okrs_example.md:92` already names a
live, in-flight experiment inside the same shared world - "Run the question-first entry cohort to 5
percent of new accounts and read the correction rate," owned by Dana Okoro, serving KR3, with a stated
read date of "mid-September." It is a real alternative, and a reviewer may prefer it. This spec uses the
Saved Views thread instead, as [the contract](contracts/experimentation-docs.md) section 4 directs. KR3's
cohort belongs to "Question-First Entry and Modelling Defaults", which `business-case_example.md` scopes as
a separate initiative. Chaining onto it would pull a second feature's facts into this family's first
worked example.

#### Catalog corrections the build's landing PR should check (per decision-procedures.md section 1)

The PR that adds this spec edits no catalog field. Each correction below is for the PR that lands a
bundle, as [ADR 0067 (tracking-plan joins governance-docs as a sixth member)](decisions/0067-tracking-plan-joins-governance-docs-as-a-sixth-member.md)
also defers the tracking plan's catalog corrections to its build.

- **`experiment-design-doc`'s guidance note, "NN/g: define metrics in advance; power analysis", is
  unverified.** The one NN/g source read in the 2026-10-05 sweep (the UX Research Methods glossary) was
  cited only for its definition of concept testing, a different type, never for metrics-in-advance or
  power-analysis guidance. Flag it as unverified pending someone reading the specific NN/g page it was
  presumably drawn from; do not delete it and do not treat it as sourced.
- **The `experiment-readout-results-report` catalog row's guidance note, "ship/iterate/kill decision", is equally
  unverified**, and now also inconsistent with the contract's own wording. No source read in
  either research pass uses "ship/iterate/kill" or "ship, iterate or stop" verbatim; both are this
  library's own POSITION. Because [the contract](contracts/experimentation-docs.md) section 1 already
  commits to "ship, iterate or stop", recommend the landing PR correct the catalog's guidance note to match
  that wording, labelled as a POSITION rather than a sourced convention, so the two documents do not use
  different words for the same decision.
- **No methodology correction is needed.** `tools/meta.schema.json`'s `methodology` field is a free token
  with no enum, and [the contract](contracts/experimentation-docs.md) section 2 declares methodology
  "descriptive, not gated" for this family. The catalog's `growth/dual-track` and `growth` values may be
  carried forward as provisional, not corrected.
- **No owner or relationship correction is needed.** Nothing read in either research pass confirms or
  contradicts "PM / Data Scientist", "Data Scientist / PM", or the two rows' relationships, which name each
  other and already match the maintainer's two-bundle ruling.
- **`size_variant: S/M` is not contradicted.** The published shapes differ widely in length, up to
  CONSORT's "25 item checklist". That range supports a `[lean, full]` split, consistent with the catalog's
  own two-weight call.

#### Licences, as far as the evidence shows

| Source | Licence |
|---|---|
| GrowthBook, `experiment-design.md` | **Unverified.** The candidate quote "MIT License" did not appear on the file's own page and was dropped by the main loop's corrections (`corrections.json`). Check the repository's `LICENSE` file directly before adapting anything structurally. |
| LaunchDarkly docs | Not stated; standard proprietary vendor-docs copyright. |
| Optimizely, both experiment-plan pages | Not stated on either page. |
| Atlassian/Confluence "Experiment plan and results" template | No explicit content licence; the page links only Atlassian's general Cloud Terms of Service. |
| Amplitude blog, "Experiment Brief" | Not stated. |
| Fishman newsletter | Not stated; a Substack post with no reuse terms found. |
| Fabijan et al., ICSE-SEIP 2019 | Authors' preprint, marked "Not for redistribution." Paraphrase only. |
| AsPredicted | Not stated on the pages read. |
| OSF, `help.osf.io` | **Unverified.** The 2026-10-05 sweep reported a CC0 statement for the help article; a direct re-check against the article's raw text found "Licensed Under" but not the fuller CC0 phrase. Treat the article's own licence, and the underlying form content's licence, as unconfirmed. |
| HM Treasury, Magenta Book | Crown copyright; Open Government Licence (the string "Open Government Licence" passed the raw-text check on the 2026 HTML edition). |
| Eppo Experiment Report Template (Google Doc) | Not stated. |
| CONSORT 2010 (PLoS Medicine) | Creative Commons Attribution License (CC BY), confirmed. |
| Behavioural Insights Team, Pension Wise report | Not stated. |
| Strategyzer, Learning Card / Test Card | "Copyright Strategyzer AG" only; no Creative Commons or other open grant found - all rights reserved by default. |
| Optimizely, "Understand your Experiment Scorecard" | Not stated; cited only for the out-of-scope boundary, not adapted structurally. |

*(Corrected 2026-10-08, when `experiment-design-doc` was built. Two rows above are now settled. GrowthBook's
skills repository is MIT-licensed: its own `LICENSE` file reads "MIT License" and "Copyright (c) 2026
GrowthBook", so risk 5 below is closed. OSF's help article is offered under CC0: the line reads "This
Article Is Licensed Under CCO For Maximum Reuse", printed with a letter O where a zero belongs, which is
why a search for "CC0" missed it. See [2] and [18] in the bundle's
[research log](../../templates/experiment-design-doc/experiment-design-doc_research-log.md#what-the-checks-caught-and-what-was-not-read).)*

#### `pairs_with`: `[]` for both

Per the maintainer's ruling, pm-skills is not evidence for this library and was not researched for this
pair. `pairs_with: []` for both members, and no pairing is claimed.

#### Risks for the build and review

1. **The lineage trap, named in [the contract](contracts/experimentation-docs.md) section 3.6, is real
   here.** CONSORT, AsPredicted, OSF, and the Magenta Book are academic and public-sector standards. A
   member that borrows their structure must say which tradition it borrows from, in the same sentence. It
   must not present a clinical reporting standard as ordinary product-management practice.
2. **The hypothesis field is deliberately left free text.** Five distinct, named hypothesis-sentence
   conventions were found, and none is universal. Do not pick one and present it as the convention.
3. **"Ship, iterate or stop", the validity-checks section, and the decision-owner field are this
   library's own POSITION, not sourced conventions.** Cutting any of the three during drafting is a
   legitimate outcome this spec does not pre-empt. Keeping any of the three means the companion must label
   it, not cite a source for it.
4. **The `okrs_example.md:90` dating residual is a trap for whoever drafts the filled example.** It is easy
   to reach for the Initiatives table's "in build, spec at 0.3.0" line as supporting colour. Do not; cite
   only the KR2 numbers.
5. **GrowthBook's licence must stay unverified** until someone raw-checks the repository's own `LICENSE`
   file. Do not let a later draft re-introduce "MIT License" as a stated fact just because the file is
   widely believed to carry one.
6. **Reforge contributes nothing, in either direction, to this pair.** Two gap-fill attempts in the
   2026-10-05 sweep could not render its JavaScript-only page. Do not cite it for admission, and do not
   cite it for the one-or-two-document question.
7. **The GrowthBook KPI-playbook fragments must stay three separate fragments** ("the more metrics
   analyzed, the greater the chance of observing a" / "significant" / "result that is actually random
   noise") if used in the companion. They passed the raw-text check as fragments; joining them into one
   sentence is not the same claim.
8. **Every GOOD and WEAK illustration in both bundles' templates must use a scenario unrelated to the
   Saved Views adoption-nudge experiment**, independent of the worked example, per the shareable-boundary
   rule (contract section 5). This failure has happened before. In the `announcement-internal-comms` and
   `change-request` builds, both templates' GOOD examples reused the worked example's scenario. The main
   loop caught it after every review lens had passed
   ([PR #195 (the announcement and change-request builds)](https://github.com/product-on-purpose/product-lifecycle-templates/pull/195)).
9. **Two alias near-misses in `manifest.json` each need a first-line disambiguation.** The design doc's
   guide names `sdd`'s aliases "design doc" and "design document". The readout's guide names
   `test-summary-report`'s alias "test results". This is the same discipline `change-request_guide.md`
   already keeps for its own `rfc` collision.

#### Metadata (provisional)

| Field | `experiment-design-doc` | `experiment-readout` |
|---|---|---|
| `family` | `experimentation-docs` | `experimentation-docs` |
| `phase` | `measure` (contract-gated) | `measure` |
| `sizes_available` | `[lean, full]` **provisional** | `[lean, full]` **provisional** |
| `status` | `beta` | `beta` |
| `methodology` | `growth/dual-track` (descriptive) | `growth` (descriptive) |
| `pairs_with` | `[]` | `[]` |
| `related_templates` | the other member; `spike-report`; `test-plan`; `test-summary-report`; `prd` | the other member; `spike-report`; `test-summary-report`; `kpi-dashboard` |

---

### governance-docs (sixth member, by amendment): the tracking plan

**`tracking-plan`** - `governance-docs`, **`classification: utility`**, sizes **`[lean, full]`**
(provisional; corrects the catalog's single `M` marker, see Catalog corrections), methodology
**`growth/data`** (provisional; not contradicted by this sweep, and consistent with every admitting
source's product-analytics lineage), catalog id `tracking-plan` (catalog 140 in
[`catalog.md`](catalog.md), verbatim at [`atlas/catalog-data.json`](../../atlas/catalog-data.json)),
catalog name "Tracking Plan", aliases (catalog) `event tracking plan`, `analytics spec`, `instrumentation
plan` (none of the three confirmed verbatim in this sweep; see Catalog corrections). Catalog owner: PM /
Data (open question, not source-confirmed; see Catalog corrections). Catalog purpose: "Define events,
properties, and user traits to instrument." Catalog contents: "events, properties, traits, triggers,
owners." Catalog `stage`: measurement. Catalog `methodology`: growth/data. Catalog `formality`: standard.
Catalog `rarity`: occasional. Catalog `size_variant`: M. Catalog `relationships`: `[Data Dictionary,
Dashboards]`. `tier: 2`, `tier_inferred: true`, `must_have: false`, `built: false`, `state: candidate`.

**The bundle id is `tracking-plan`, the same as the catalog id, with no reason found to differ.** Unlike
`change-log`, whose catalog id (`change-log-governance`) carried a disambiguating suffix the build
dropped, this candidate's catalog id is already the bare type name every other `governance-docs` member
uses (`risk-register`, `raid-log`, `kpi-dashboard`, `issue-log`, `change-log`).

#### Demand: named inline, never routed to

Unlike `change-log` and `change-request`, no shipped bundle **routes to** a standing tracking plan as a
separate document. The PRD **absorbs** a feature's slice of it inline, and its own guidance says so,
checked directly on 2026-10-06:

- `templates/prd/prd_template-full.md:209` opens the section ("## Analytics and instrumentation"); its WHY
  at `prd_template-full.md:213` reads: "Metrics without instrumentation ship blind; if the tracking plan
  is not in the PRD, the launch usually cannot measure its own success criteria." The WEAK at
  `prd_template-full.md:220` reads: "Success metrics defined with no tracking plan to capture the data."
- `templates/prd/prd_companion.md:66` repeats the same sentence from the companion's own side: "if the
  tracking plan is not in the PRD, the launch usually cannot measure its own success criteria."
- A case-insensitive grep for "tracking plan" across `templates/` and `docs/internal/contracts/`, run
  2026-10-06, returns these three PRD lines and two contracts. The `experimentation-docs` contract's
  boundary sentence excludes the type by name and points at ADR 0067 (tracking-plan joins governance-docs as a sixth member)
  (`docs/internal/contracts/experimentation-docs.md:42-45`). The `governance-docs` contract names it in
  its kpi-dashboard axis note and in the text its `0.4.0` amendment adds. No other shipped bundle
  mentions the type.

**This is the duplication risk seen from the demand side, not only the scope side.** The one sibling that
names the type treats it as content that already belongs inline in a PRD, not as a document something
else is missing. The one sourced analogy for why a per-feature slice and a standing plan can coexist
without duplicating each other is Avo's own branch-and-merge workflow (see Boundaries, below):
single-vendor, tool-workflow evidence, not a second document-template source.

#### Admission: five independently named vendors

Every quotation below passed the main loop's 2026-10-05 re-check against raw page text
(`_local/research/2026-10-04_admission-sweep-4/recheck-out.json`), was reattributed there by
`corrections.json` to the URL cited, or was raw-checked again on 2026-10-06 with `rawcheck.py` against the
URL named; the last case is marked.

| Vendor | What it says or ships | Licence |
|---|---|---|
| Avo | Docs: "The Avo Tracking Plan is where you define the data for your application" and "It contains detailed definitions of your tracking plan that can be used to generate code from and validate your data against" ([`avo.app/docs/data-design/avo-tracking-plan`](https://www.avo.app/docs/data-design/avo-tracking-plan)). Its Data Design index page states the core definition as one sentence: "A tracking plan is a document that defines the key stages of your customer life cycle and codifies a single source of truth for the data that supports it" ([`avo.app/docs/data-design`](https://www.avo.app/docs/data-design)). Its blog ships a ten-column Google Sheets worksheet; five of the ten column names were individually raw-checked against that blog and pass (KPIs, Event categories, Event names, Property value types, Code snippet, [`avo.app/blog/avos-ultimate-tracking-plan-template-w-downloadable-worksheet`](https://www.avo.app/blog/avos-ultimate-tracking-plan-template-w-downloadable-worksheet)); the remaining five column names (Event description, Properties, Property description, Platforms, Status) are read from the same page's prose, not individually quote-checked. | No licence statement found on either page; not confirmed |
| Twilio Segment | Docs: "A Tracking Plan is a data spec outlining the events and properties" and ships live validation ("violations") against an imported "spreadsheet" ([`segment.com/docs/protocols/tracking-plan/create`](https://segment.com/docs/protocols/tracking-plan/create/)). A second docs mirror adds cadence and authorship, raw-checked 2026-10-06: "Segment offers Tracking Plan Event Versioning" and "Crafting a comprehensive Tracking Plan takes time and effort across a range of teams" ([`twilio.com/docs/segment/protocols/tracking-plan/create`](https://www.twilio.com/docs/segment/protocols/tracking-plan/create)). Its blog states the document form plainly: "a document or spreadsheet used across an organization to standardize how it tracks data" and "a tracking plan consists of a list of events" ([`twilio.com/en-us/blog/insights/what-is-a-tracking-plan`](https://www.twilio.com/en-us/blog/insights/what-is-a-tracking-plan/)), and links a downloadable Google Sheets template with a worked example table; three of its four column headers pass the raw-text check (NAME, PROPERTIES, LOCATION); the fourth did not pass and is not stated here. | No licence statement found on either page; not confirmed |
| Amplitude | Docs: "A tracking plan defines every event and property you collect, why you collect each one, and which source emits it" ([`amplitude.com/docs/data/create-tracking-plan`](https://amplitude.com/docs/data/create-tracking-plan)). Its blog states cadence and role in two separate quoted phrases, both reattributed by `corrections.json` from the docs page to [`amplitude.com/blog/create-tracking-plan`](https://amplitude.com/blog/create-tracking-plan), where the main loop's re-check passes both: "a document that acts as a source of truth for your event data" and, elsewhere on the same page, "a living document that contains all the information related to the data you gather". The blog's own prose describes a four-sheet Google Sheets template plus five vertical taxonomy templates; this count is **summary-derived**, the spreadsheets were not opened, and `corrections.json` marks it medium confidence. | Not stated on either page |
| Mixpanel | Docs: "centralized document" that is the "source of truth on your Mixpanel implementation" ([`docs.mixpanel.com/docs/tracking-best-practices/tracking-plan`](https://docs.mixpanel.com/docs/tracking-best-practices/tracking-plan)). The page's own outbound links, checked directly rather than taken from a third-party listicle, resolve to five Google Sheets templates; `corrections.json` marks this count medium confidence, since the sheets themselves were not opened. | Not stated on the page |
| mParticle | Blog: "A data tracking plan is a document that keeps different teams aligned on the key information regarding your organization's data collection and analysis efforts" ([`mparticle.com/blog/data-tracking-plan-engineers`](https://www.mparticle.com/blog/data-tracking-plan-engineers/)). Its own platform guide describes an in-tool variant on the same model: "A data plan is a codified set of expectations about the extent and shape of your data collected with mParticle," with continuous editing, "Updates to active data plans are live immediately" ([`docs.mparticle.com/guides/platform-guide/data-planning`](https://docs.mparticle.com/guides/platform-guide/data-planning/)). | Not stated on either page |

**No licence statement was found on any of the ten pages read across these five vendors.** See Licences,
below.

#### Scope under ADR 0030: the document is upstream, the enforced schema is derivative

[ADR 0030](decisions/0030-templating-scope-markdown-documents.md)'s scope rule: "This library templates
artifacts whose primary form is a written document. An artifact whose primary form is visual, executable,
or a live data surface is out of scope for templating, and is named as such with its reason rather than
left silently unbuilt" (`docs/internal/decisions/0030-templating-scope-markdown-documents.md:61-63`). Its
admission test, generalised from ADR 0028: "A candidate type is templatable when a named source publishes
it as a written document" (same file, line 65).

Four of the five vendors ship or link a spreadsheet template (Avo, Twilio Segment, Amplitude and
Mixpanel), and mParticle describes the document in prose. Twilio Segment's docs page defines the plan as
"a data spec" and also validates live events against it, reporting "violations" against an imported
"spreadsheet". That is evidence that the document can be read into the tool. Avo's own documentation describes the same
direction from its own branch-and-merge workflow: a change is drafted as a branch "in isolation, without
impacting the main branch, which contains the single source of truth of what's currently being tracked"
(`avo.app/docs/workflow/plan`), and once implemented, "the main branch in Avo always represents the
current state of the Avo tracking plan" (`avo.app/docs/implementation/guides/avo-and-git`). **Reading the
document as upstream and the enforced schema as derivative is this library's own inference from these
sourced facts** (no vendor states the inference in those words), consistent with how ADR 0030 already
treats `risk-register` and `kpi-dashboard`: the spec is in scope, a live tool that implements it is not.

The published form is tabular wherever it was checked: Avo's ten-column worksheet, Twilio Segment's
four-column worked example, Amplitude's and Mixpanel's sheet templates. This is the same tabular,
specification shape the library already renders as a Markdown table for `risk-register`'s risk rows and
`kpi-dashboard`'s KPI table and Metric Definitions section. A Markdown table is the in-scope form; a live,
validating schema inside a product-analytics tool is not, and this bundle does not attempt to template
one.

#### Cadence: a living, versioned, product-wide document

Every vendor that addresses cadence directly describes the same thing: a document that is maintained, not
written once. Amplitude's blog calls it "a living document that contains all the information related to
the data you gather." mParticle's platform guide states "Updates to active data plans are live
immediately." RudderStack's knowledge base reads: "Tracking plans support versioning, which enables us to
iterate and monitor the changes in a tracking plan event spec" (`rudderstack.com/knowledge-base/get-started-with-tracking-plans`),
and its data-governance docs add "Tracking Plans let you proactively monitor and act on non-compliant
event data" (`rudderstack.com/docs/data-governance/tracking-plans`). Snowplow's own fundamentals page
carries a named "Change History" field as part of its documented dataset
(`docs.snowplow.io/docs/fundamentals/tracking-plans`), and a practitioner blog states the event lifecycle
explicitly as "proposed / active / deprecated / removed" (`digitalapplied.com/blog/product-analytics-event-taxonomy-tracking-plan-2026`).

This is the same property [ADR 0024](decisions/0024-adopt-governance-docs-family-contract.md) already used
to place `kpi-dashboard` at `classification: utility` rather than `phase: measure`: "a standing,
continuously-maintained instrument... not a deliverable produced once at a measure phase"
(`docs/internal/decisions/0024-adopt-governance-docs-family-contract.md:39`). Every cadence signal found
for the tracking plan points the same way, which is why this spec places it at `classification: utility`
and not on the `phase` axis the new `experimentation-docs` family uses. That family's own contract already
excludes the type by name: "A standing measurement instrument is not a member, however closely it serves
experiments. A tracking plan... is maintained across many tests and is never finished, so it belongs to a
`classification` family. The tracking plan joins `governance-docs` by ADR 0067"
(`docs/internal/contracts/experimentation-docs.md:42-45`).

#### Structure: one load-bearing table, converging across five vendors

No single vendor's column list is canonical, and none should be copied whole (see Licences, below), but
the five independently published shapes converge on the same core fields. Avo's worksheet carries ten
columns (KPIs, Event categories, Event names, Event description, Properties, Property description,
Property value types, Platforms, Status, Code snippet; five individually raw-checked, see Admission).
*(Corrected 2026-10-11, when `tracking-plan` was built: all ten are now read in raw text, as numbered
headings from "1. KPIs" to "10. Code snippet"; see [3] in the bundle's [research log](../../templates/tracking-plan/tracking-plan_research-log.md#what-the-checks-caught-and-what-was-not-read).)*
Twilio Segment's worked example carries four (NAME, PROPERTIES, LOCATION, and a fourth column whose name
did not pass the raw-text check). *(Corrected 2026-10-11, when `tracking-plan` was built: the fourth
column is WHY. The headers sit in an image, but the page's prose names it: the why "(logged under WHY)
is a short description of the business purpose that justifies tracking the event." See [6] in the
bundle's [research log](../../templates/tracking-plan/tracking-plan_research-log.md#what-the-checks-caught-and-what-was-not-read).)* Amplitude's docs state the field structure in the one quote that passed:
"every event and property you collect, why you collect each one, and which source emits it" - an event
name, a reason, and a source. Mixpanel and mParticle each describe the document as centralized and
aligning, without naming individual columns in anything that passed the raw-text check.

Read together, the fields that recur are: an event or property name, what it means or why it is captured,
the properties attached to it, who owns it, and where it comes from or goes to. Two further fields are
sourced only once each and are treated as single-vendor evidence, not convergent fact: a status or
lifecycle value (Avo's "Status" column; Digital Applied's "proposed / active / deprecated / removed"),
and a per-event owner stated as a named individual rather than a team ("One named person per event, full
stop," and "a named person, not a team," `customerscore.io/blog/event-tracking-plan-saas`; Amplitude's
event-taxonomy page separately describes a four-role chain, "Event requesters propose," "Data stewards
review," "Domain owners approve," `amplitude.com/explore/data/event-taxonomy` - a richer, differently
shaped claim about the same subject, not a second confirmation of the same role).

*(Corrected 2026-10-11, when `tracking-plan` was built: neither field is single-sourced any longer.
Amplitude's own event-taxonomy page carries the status vocabulary, as version labels like "proposed,"
"active," "deprecated," and "removed," and Avo's "9. Status" column and GitLab's event definitions
carry a status too. Amplitude's tracking-plan page names an owner per event, "the person responsible for
the implementation of that event", and two more sources list an owner among a plan's contents. The
bundle carries both as columns without a single-source label. Who owns the plan as a whole is still
open; see the bundle's [research log](../../templates/tracking-plan/tracking-plan_research-log.md#what-the-checks-caught-and-what-was-not-read).)*

#### Section design

Provisional, and expected to move once a build's own research runs:

| Section | In lean | What it carries |
|---|---|---|
| **Purpose and Boundary** | yes | What this document catalogs (the events, properties, and traits a product captures, across every feature) and what does not go in: a per-feature instrumentation spec (the PRD's own "Analytics and instrumentation" section, or the unbuilt `analytics-requirements-measurement-plan`), the unbuilt data dictionary *(2026-10-15: built as `data-dictionary`)*, the KPI dashboard's Metric Definitions section, and the in-tool enforced schema some vendors build from this document. Sourced to Segment's glossary, Countly's glossary, Avo's Data Design docs |
| **Event and Property Catalog** | yes | **The load-bearing section.** One row per event: name, trigger (when it fires), properties, owner, source or destination, status. Name, meaning, properties and source recur across the vendors (see Structure). Owner and status are each single-sourced, so the companion labels them as such. *(Corrected 2026-10-11, when the bundle was built: neither is single-sourced any longer; see the note under Structure.)* A table section, so it carries PRIORITY and ROW HINT |
| **Review and Ownership** | yes | The cadence this document is kept on, who maintains it, and the living-document framing: Amplitude's "a living document," mParticle's "live immediately." Thinly sourced on cadence specifics beyond "continuously maintained"; any stated review interval is this library's own **POSITION** |
| **Governance and Ownership Discipline** | full only | The PII and ownership discipline several practitioners argue for but no vendor documentation states as a required field: one named owner per event (`customerscore.io`, a single practitioner source), PII flagging and masking ("strict controls to prevent the accidental collection of Personally Identifiable Information," `trackingplan.com/blog/data-governance-for-analytics`), and Amplitude's four-role approval chain as a richer, alternative shape for the same concern. **Thinly and sometimes differently sourced**; present both shapes rather than picking one as canonical, the same move `change-log`'s Status Vocabulary section already makes for its own three published shapes |
| **Versioning and Change History** | full only | A version or change-history field per event, and the event's lifecycle state. Snowplow's named "Change History" field, Digital Applied's "proposed / active / deprecated / removed," and RudderStack's and mParticle's versioning language are the published shapes; no single vocabulary is canonical, stated as such |

#### Boundaries with each named neighbour

- **Not the per-feature instrumentation plan, and not the PRD's own "Analytics and instrumentation"
  section.** The clearest sourced evidence on this exact boundary comes from one vendor's own
  tool-workflow documentation, not from a second document-template source: Avo's branching model treats a
  per-feature draft as a change proposed against the standing plan, reviewed in isolation, and then
  merged. "A branch allows you to draft changes to the tracking plan in isolation, without impacting the
  main branch, which contains the single source of truth of what's currently being tracked"
  (`avo.app/docs/workflow/plan`); "A branch often corresponds to a single journey for a feature or user
  flow, making it easy to design, review, and implement tracking changes together"
  (`avo.app/docs/data-design/branches`); once shipped, "the main branch in Avo always represents the
  current state of the Avo tracking plan, while the tracking plan implementation stays pinned to the
  branch we just implemented" (`avo.app/docs/implementation/guides/avo-and-git`). Read together, the
  per-feature slice is a change set proposed against the standing plan, not a second standing document
  competing with it. This is single-vendor, tool-workflow evidence, so applying it to the PRD's own
  section specifically is this library's own **POSITION**: the PRD section records one feature's events
  at one moment, in Avo's own sense a branch not yet merged; the standing tracking plan is what every
  feature's branch merges into over the product's life. Neither research dimension in this sweep found a
  source addressing the PRD-section-versus-tracking-plan relationship directly, and the critic's own
  weakest-load-bearing-claims finding names this as a genuine gap. **Falsifier, per [decision-procedures.md
  section 11](decision-procedures.md#11-a-family-contract-asserts-something-about-the-world):** a source
  stating the PRD section and the standing plan are maintained as two independent documents, neither
  feeding the other, would contradict this reading. The unbuilt `analytics-requirements-measurement-plan`
  (catalog 147) is the same per-feature artifact under its own standalone catalog row; Wizbrand's
  content-breadth distinction ("narrower and implementation-focused" tracking plan versus a broader
  measurement plan covering "business objectives, KPI definitions, governance, and reporting logic,"
  `wizbrand.com/tutorials/analytics-measurement-plan`) describes that per-feature measurement plan, not
  the standing, cross-feature type specced here. Content breadth and cadence are separate axes, and this
  spec draws the line by cadence. *(2026-10-15: Wizbrand does not describe a per-feature plan. The same page says of its measurement plan "Many teams review it quarterly", raw-checked in a 2026-10-14 admission sweep, which describes a standing document. The sentence above misreads Wizbrand on that point; the cadence line rests on Avo's branch model and this library's own POSITION, not on Wizbrand.)*
- **Not the data dictionary (catalog 141, unbuilt).** *(2026-10-15: built as `data-dictionary`. Its
  [spec](#governance-docs-seventh-member-by-amendment-the-data-dictionary-scoped-to-what-a-datasets-fields-mean)
  and ADR 0073 draw this boundary on subject rather than tense, because research on 2026-10-14 found the
  tense line contested across primary and peer-reviewed sources. The tense reading below is kept as written.)*
  One source draws a clean
  forward-looking-versus-backward-looking line, single-sourced but not contradicted, in three separately
  raw-checked phrases from the same page: "A tracking plan describes what you intend to track"; "A Data
  Dictionary documents what the data means and how it is structured once implemented"; and "the tracking
  plan drives implementation" (`wizbrand.com/tutorials/data-dictionary`).
- **Not the KPI dashboard's Metric Definitions section.** No source in this sweep addresses this
  relationship directly; both research dimensions say so, and the critic names it the most load-bearing of
  the unsourced claims. State it as this library's own **POSITION**: a tracking plan catalogs the raw
  events and properties a product captures; `kpi-dashboard`'s Metric Definitions section
  (`templates/kpi-dashboard/kpi-dashboard_template-full.md:87`) locks the derived, computed metric built
  from some of those events, with its own formula, inclusions, exclusions, owner, and data steward. The
  tracking plan stands upstream of that section. **Falsifier:** a source stating that a tracking plan
  itself defines or locks a metric's formula would contradict this layering and should reopen it.
- **Not the event schema enforced inside a tool.** Sourced directly: Twilio Segment's Protocols validates
  live events and reports "violations" against an imported "spreadsheet"
  (`segment.com/docs/protocols/tracking-plan/create`); Avo's own product is the in-tool side of the same
  document (see Scope, above); mParticle's platform guide calls its in-tool variant "a codified set of
  expectations... collected with mParticle," distinct from the document-form "data tracking plan" its own
  blog names. Read together, these sources fit the library's **POSITION** that the document is the
  upstream input and the enforced schema derives from it. No vendor states that ordering in those words.
- **Not `risk-register` or `raid-log`.** Neither research dimension found, nor would be expected to find,
  any source connecting a tracking plan to risk likelihood, impact, or the RAID quadrants. The subjects do
  not overlap: one specifies what is measured, the other tracks what might go wrong. **POSITION**, stated
  for completeness because contract section 1 requires every member to state its position against every
  other member.
- **Not `issue-log`.** Same reasoning: an issue log tracks problems that have already happened; a tracking
  plan is forward-looking, specifying what will be captured. **POSITION**.
- **Not `change-log`.** A change log tracks requested and decided changes to an agreed baseline; a
  tracking plan is a standing catalog of events and properties, not a register of decisions. A revision to
  the tracking plan could in principle itself be the subject of a change request a change log records, the
  same relationship the change log already has with every other baseline document in the family, but
  nothing in this sweep's evidence addresses that specifically for this type. **POSITION**.

#### Family fit and the amendment: ADR 0067

**The research tested the contract as it read at `0.3.0`, and the type failed on one phrase.** Section 1
then admitted a "continuously-maintained register, log, or dashboard that a product or program manager
uses to track risk, open items, or performance across the whole lifecycle". The noun fits without strain,
because a tracking plan is a register of events and properties. The cadence fits too, because every
vendor source above describes a document maintained for the product's whole life. The phrase that strains
is "to track ... performance". A tracking plan specifies what the product records so that performance can
be tracked later. It does not itself track performance, as a dashboard or a log does.

**[ADR 0067 (tracking-plan joins governance-docs as a sixth member)](decisions/0067-tracking-plan-joins-governance-docs-as-a-sixth-member.md)
widens that phrase, and the contract moves to `0.4.0`.** The clause gains "or to specify what the product
records so that performance can be tracked", and no existing word changes. It is the second admission to
widen a membership test, after ADR 0060 (change-request joins delivery-docs). The same edit changes
"The five roles" to "The six roles" and adds a sixth bullet. That bullet places the tracking plan upstream
of the KPI dashboard: the dashboard defines the metrics the family tracks, and the tracking plan defines
the events those metrics are computed from. A dated `0.4.0` change note records all three changes, the
pattern ADR 0057 (issue-log joins as a fourth member) and ADR 0061 (change-log joins as a fifth member)
each followed.

#### The worked example: the Reporting Platform Modernization program's tracking plan

**The shared-scenario rule (contract section 4) applies.** The example must carry the same Acme Analytics
/ Reporting Platform Modernization / Saved Views scenario every other `governance-docs` member's example
uses, and its events, metrics, owners, and dates must agree with what the PRD, the KPI dashboard, and the
OKRs examples already state, not invent a parallel set.

**Five events, from the PRD's own "Analytics and instrumentation" section**
(`templates/prd/prd_example.md:133-136`): "Instrument before launch: `view_saved`, `view_switched`,
`view_set_default`, `view_shared`, `view_load_error` (with reason), each with dashboard ID and view scope.
Build a Saved Views adoption dashboard (views created per active analyst, share rate, default-set rate)
and wire the primary metric to the existing Time to Insight panel." Five named events: `view_saved`,
`view_switched`, `view_set_default`, `view_shared`, `view_load_error`.

**A second event family, from the KPI dashboard's own Metric Definitions.**
`templates/kpi-dashboard/kpi-dashboard_example.md:69-70` states the Time to Insight metric's "Known
limitation: 'action' is proxied by a set of logged events (export, share, annotate)." These three logged
actions (export, share, annotate) are a second event family the tracking-plan example must also carry,
distinct from the five Saved Views events above; omitting them would leave the dashboard's own stated
proxy undocumented in the plan that is supposed to be its upstream catalog.

**The PRD's success metrics** (`templates/prd/prd_example.md:124-129`): primary metric is "median time
from dashboard open to first meaningful interaction," tied to the Time to Insight goal; guardrail is
"dashboard load error rate does not increase, and shared-view permission incidents stay at zero"; window
is "4 weeks post-rollout, compared to the 4 weeks prior, for the Recurring Analyst cohort."

**Metrics and owners, from the KPI dashboard example** (`templates/kpi-dashboard/kpi-dashboard_example.md:53-57`,
the KPIs table's five data rows, under the heading at line 47): Time to Insight (target -30% vs baseline by Q3, current -18%, owner Priya Nair); Saved
Views adoption (target 60% by end Q3, current 41%, owner Priya Nair); View-list load (p95) (target
<500ms, current 620ms staging, owner **Dana Osei**); Weekly active analysts (hold >=480, current 495,
owner Priya Nair); Migration integrity (100% at cutover, owner Lee Zhang). The Metric Definitions section
(`kpi-dashboard_example.md:59-73`) locks Time to Insight's formula and names its data steward as **Lee
Zhang (Data Eng)**. The dashboard's own frontmatter (`kpi-dashboard_example.md:1-13`) names its owner
**Marta Reyes (Program Manager)** and states the live tool split directly: "the live dashboard is
implemented in the Acme BI workspace (Amplitude for product events, Looker for the executive view)"
(`kpi-dashboard_example.md:42-43`). The example's source column can therefore name Amplitude as where
product events land. It must not borrow wording from Amplitude's own tracking-plan template, which carries
no licence (see Licences).

**Metrics and owners, from the OKRs example** (`templates/okrs/okrs_example.md`, Key Results table): KR1
at line 51, Time to Insight, -18% to -30% against the FY26 baseline, owner Priya Nair, committed; KR2 at
line 52, Saved Views adoption, 41% to 60%, owner Priya Nair, committed; KR3 at line 53, "Share of new
accounts that build a second view within 14 days," 31% to 50%, owner **Dana Okoro**, aspirational. The
tracking-plan example must not confuse Dana Okoro (OKRs, product roadmap, KR3) with Dana Osei (KPI
dashboard, View-list load) - two different people, one letter apart in their first names.

**What the example must not invent.** No sibling example assigns a named owner to an individual *event*
(as opposed to a KPI or a dashboard); `customerscore.io`'s "one named person per event" is this sweep's
own evidence for why a tracking plan's Event and Property Catalog table needs an owner column, but no
built sibling states who that person is for any of the eight events named above (the five PRD events plus
export, share, annotate). **This is a build decision, not a fact this spec can state.** One defensible
assignment, consistent with but not lifted verbatim from any sibling: Priya Nair for the events feeding
the metrics Priya Nair owns (Time to Insight, Saved Views adoption, weekly active analysts); Dana Osei for
`view_load_error`, since it threatens the View-list load metric Dana Osei owns; Lee Zhang as data steward
of record across the table. The build must state whatever it chooses plainly as its own assignment.

**Dates and constraints from PR #204's reconciliation** (decision 4, 2026-09-30, merged in #204 and
recorded in `tier2-specs.md`'s own dated notes): the shared scenario's 2.4.0 release now ships
**2026-07-21**, `CR-SV-01` is submitted 2026-08-04 and decided 2026-08-14, and the `change-log` example is
reviewed 2026-08-17. A tracking-plan example's `last_reviewed` (or equivalent frontmatter) must sit at or
after whichever date the build chooses as this document's own review point, and must not predate
2026-07-21, the reconciled release date; `view_shared` cannot be shown live before that date either.
**Four residuals PR #204 left unfixed, which this example must simply not touch:** the internal
announcement's "private views since late June"; the retrospective's 2026-09-14 general-availability date;
the release notes' known issue promising a fix in 2.4.1 that the test summary defers; and the definition
of done's "DEF-2291 shipped in build 2.3.2" wording. None of these four bears directly on a tracking
plan's content, and the safest build choice is to avoid all four dates and claims rather than test whether
a tracking plan can mention them safely. A fifth inconsistency, found by this sweep, belongs on the same
list: `okrs_example.md:90` still shows Saved Views as "in build, spec at 0.3.0" in a file updated
2026-07-27, six days after the release. The example cites KR2's numbers and never that status line.

**The gate that enforces this.** `check-example-chronology.py` and `check-example-independence.py` both
run in `tools/run-gate.py`, and any new example chaining onto this scenario must pass both, the same gate
`change-log` and the other four built members already pass.

#### A note on the templates themselves

Every GOOD and WEAK illustration drafted for this bundle's templates must use a scenario unrelated to the
Reporting Platform Modernization program and the Saved Views feature, independent of this spec's own
worked example. This is stated here on its own, separate from the risks list below, because the identical
failure, a template that passed every automated lens while silently reusing its own worked example's
scenario, reached the main loop uncaught in both `announcement-internal-comms`'s and `change-request`'s
own builds
([PR #195 (the announcement and change-request builds)](https://github.com/product-on-purpose/product-lifecycle-templates/pull/195)).
[Decision procedure 9](decision-procedures.md#9-a-defect-recurs-after-a-convention-was-adopted-to-prevent-it)
governs exactly this pattern, and a third recurrence in this bundle should be checked for, not assumed
absent.

#### Catalog corrections the build's landing PR should check

The PR that adds this spec edits no catalog field, as ADR 0067 defers these corrections to the build. Per
[procedure 1](decision-procedures.md#1-a-catalog-call-loses-to-research), the landing PR edits both
`docs/internal/catalog.md:206` and `atlas/catalog-data.json`, then regenerates the atlas, for each
correction it accepts:

- **`owner: "PM / Data"` is an open question, not a correction**, the same posture `change-log`'s own
  landing took for "PM / Change Manager." Two sources argue against treating ownership as a two-role
  department pairing: Amplitude's event-taxonomy page describes a four-role approval chain ("Event
  requesters propose," "Data stewards review," "Domain owners approve," `amplitude.com/explore/data/event-taxonomy`),
  and a single practitioner source argues for one named individual: "One named person per event, full
  stop" and "a named person, not a team" (`customerscore.io/blog/event-tracking-plan-saas`). Neither
  source names who owns the *document* as a whole, as opposed to a single event row, and no source
  attests a specific two-word replacement for "PM / Data." **Flag it for the spec author or reviewer; do
  not invent a corrected value.** The template's Event and Property Catalog table should carry a per-row
  owner column regardless of what the catalog field says, since that is what the evidence actually
  supports.
- **`stage: "measurement"` should not be corrected.** The research critic argued that the field "implies a
  phase:measure placement that the evidence does not support" and should move toward `classification:
  utility` instead. That conflates the catalog's descriptive `stage` field with the metadata schema's
  `phase`/`classification` axis. `kpi-dashboard` (catalog entry 139, shipped, `classification: utility`)
  carries `"stage": "measurement"` in `atlas/catalog-data.json` today. Treating `tracking-plan`'s identical field differently, with no new
  evidence distinguishing the two cases, would be inconsistent rather than corrective. **No change
  recommended**; the axis call that actually matters, `classification: utility`, is made in the bundle's
  `meta.yaml`, independently of this descriptive catalog field, exactly as it already is for
  `kpi-dashboard`.
- **`size_variant: "M"` likely undercounts the shipped shape.** The same correction `issue-log`'s and
  `change-log`'s own landings made: the catalog's single-letter marker predates any research into the
  type's actual published shapes, and this sweep's own structure findings (Avo's ten columns against
  Twilio Segment's four, against Amplitude's and Mixpanel's simpler centralized-document framing) support
  a two-weight split. Checked directly against both `_meta.yaml` files: every existing `governance-docs`
  member, including `risk-register` and `kpi-dashboard`, already ships `sizes_available: [lean, full]`.
  **Recommend `sizes_available: [lean, full]`.**
- **`methodology: "growth/data"` is not contradicted and should stand.** Every admitting vendor (Avo,
  Twilio Segment, Amplitude, Mixpanel, mParticle) is a product-analytics company, directly consistent with
  the "growth/data" lineage tag this sweep's own research used for all five. Unlike `issue-log`'s and
  `change-log`'s methodology fields, which research contradicted (their catalog's "PMBOK/ITIL" against
  evidence pointing to a generic lineage), nothing here argues against "growth/data"; correcting it to
  `generic` would be *less* accurate, not more. **No change recommended.**
- **Aliases: one collides in meaning, none is confirmed verbatim.** "instrumentation plan" was not found
  as a vendor-used term anywhere in this sweep, and it is also the more natural name for the unbuilt,
  per-feature `analytics-requirements-measurement-plan` (catalog 147) - a meaning collision worth flagging
  even though no string collides mechanically. **Recommend sourcing it or dropping it before the build**,
  the same move `change-log`'s landing made for "change control log." "event tracking plan" and "analytics
  spec" were not found verbatim either; Twilio Segment's own vocabulary is "data spec," not "analytics
  spec," a near-miss worth noting on the guide's first line if either alias stays. mParticle directly
  attests "data tracking plan" ("A data tracking plan is a document that keeps different teams aligned..."),
  not currently in the catalog's alias list. **Recommend reviewing all three aliases against this sweep's
  sources before the build, not carrying them forward unexamined.**
- **Relationships `[Data Dictionary, Dashboards]` are not contradicted and can stand.** Wizbrand's
  forward/backward-looking distinction supports the Data Dictionary relationship; the KPI dashboard
  relationship is this spec's own sourced-as-POSITION boundary, above. **No change recommended.**
- **Formality (`standard`) and rarity (`occasional`) are not contradicted by anything retrieved and can
  stand as-is.**

#### Licences of the vendor templates

No licence statement was found on any of the ten pages read across the five admitting vendors (Avo's docs
and blog, Twilio Segment's two docs mirrors and its blog, Amplitude's docs and blog, Mixpanel's docs,
mParticle's blog and platform guide). Two retrieval notes say so explicitly (Twilio Segment, Avo); the
rest are silent on the question. No licence claim should be made for any of the five. The template this
library ships synthesizes a column set from what the five share (see Structure, above), rather than
adapting any one vendor's sheet.

#### `pairs_with`: `[]`, no pairing claimed

Per the maintainer's ruling of 2026-10-06, `pm-skills` is not evidence for this library and was not
researched for this candidate. **`pairs_with: []`.** No pairing is claimed.

#### Risks for the build and the review

1. **The PRD-section and KPI-dashboard-Metric-Definitions boundaries are POSITION, not sourced**, and the
   critic names the PRD boundary the single most load-bearing unsourced claim in this sweep. Neither must
   gain an invented citation to read more confident than the evidence; if a build agent cannot find a
   source, it must keep the POSITION label, not remove it.
2. **Avo's branch-and-merge evidence is single-vendor and describes a tool workflow, not a second
   document-template source.** It is the best available analogy for the PRD-versus-standing-plan
   boundary, and it must be cited as exactly that, not generalized into a claim every vendor makes.
3. **Two template counts are summary-derived and must stay flagged medium confidence**: Amplitude's "four
   sheets plus five vertical taxonomy templates" and Mixpanel's "five Google Sheets templates." Neither
   spreadsheet was opened; both counts come from page prose or outbound links. *(Corrected 2026-10-11,
   when `tracking-plan` was built: Amplitude's page links one Google Sheets template, not a set, and
   names its four sheets in prose: Events and Event Properties, User Properties, Organization (Group)
   Properties, and Discussions. No vertical taxonomy templates appear on the page read. Mixpanel's page
   names four vertical templates and a blank one, which matches its count of five. Neither spreadsheet
   was opened; see [9] and [11] in the bundle's [research log](../../templates/tracking-plan/tracking-plan_research-log.md#what-the-checks-caught-and-what-was-not-read).)*
4. **No licence was found for any vendor's template.** Do not adapt column names or wording from any one
   vendor's sheet verbatim, and do not state or imply a licence for any of the five.
5. **The shared-scenario rule binds hard here.** Every event, metric, owner, and date in the worked
   example must agree with `prd_example.md`, `kpi-dashboard_example.md`, and `okrs_example.md`, exactly as
   enumerated above. It must not touch the four residuals PR #204 left unfixed, or the OKRs example's
   stale status line. `check-example-chronology.py` and `check-example-independence.py` both gate this.
6. **Per-event ownership in the worked example is a build decision, not a sourced fact.** No sibling
   example names an owner for an individual event; the build must state its own assignment plainly rather
   than presenting it as read from a sibling.
7. **The owner and stage catalog fields are flagged, not corrected, in this spec.** A build that quietly
   "fixes" either without a reviewer decision would be inventing a value this sweep's evidence does not
   support.

---

### discovery-docs (fourth member, at `define`): the problem statement, the library's first Define bundle

**`problem-statement`** - `discovery-docs`, **`phase: define`**, sizes **`[lean, full]`** (the maintainer's
ruling, against this spec's research; see below), default `lean`, methodology **`methodology-agnostic`**, a
new catalog type with **no catalog row yet**, proposed aliases `problem brief` and `opportunity statement`.
**The maintainer ruled on 2026-10-11: record "Define means problem framing" as
[ADR 0068](decisions/0068-define-means-problem-framing.md), build this type with two sizes, and admit it by
amending `discovery-docs` rather than founding a new family.** The contract edits of
[ADR 0069](decisions/0069-problem-statement-joins-discovery-docs.md) land with this spec, so the metadata
below is written against contract `0.3.0`.

#### Demand: a shipped companion already names it as an upstream document

**`prd_companion.md:141` names a problem statement as one of the documents that precede a PRD**: "Upstream
(precede it): product strategy and roadmap (set the bet), discovery research and personas (validate the problem
and user), opportunity solution trees or a problem statement (frame what is worth solving)". No bundle answers
that pointer today. The nearest shipped text is `business-case`'s Problem and Opportunity section, whose WHAT
reads "described without naming the solution you already have in mind"
(`business-case_template-lean.md:52-53`), and whose TRAP is "Naming a solution instead of a problem"
(`business-case_template-lean.md:64`). That section sits inside an investment case, and a reader who wants to
agree on a problem before anyone proposes an investment has no document to write.

**pm-skills ships `define-problem-statement`** (`phase: define`, version 2.1.0, read on 2026-10-11 at
pm-skills `main` 1cef1a9e). It is a pairing, not a ranking signal: this library never assumes pm-skills is
installed, and the pairing is no reason to build. It is recorded here because `pairs_with` must name it (see
Metadata).

#### Admission: retrieved and raw-checked on 2026-10-11

The Define admission sweep of 2026-10-11 read 75 addresses across two workflow runs. The main loop checked 311
returned quotations against raw page text, and 310 passed. Every quotation below is one of the 310.

| Source | What it says | Weight |
|---|---|---|
| Maria Rosala, Nielsen Norman Group, "Problem Statements in UX Discovery" (2021-08-22) | "A concise description of the problem that needs to be solved"; three required parts, "The background of a problem", "The people affected by the problem" and "The impact of the problem on the organization"; a quality rule, "Not contain a solution"; and "Throughout the discovery process, you can return to your problem statement and add to it" | **Admits on its own** (ADR 0048). Practitioner tier |
| Digital NSW, "Define the problem" (New South Wales Government digital service toolkit) | "Use the evidence you gather to document your clearly defined problem"; a review checklist that asks "Have we described a problem rather than a solution?"; a worked example that rewrites a solution-first sentence | **Admits on its own.** Public-sector guidance. Its full checklist was not quoted in the sweep, and the build must read every question verbatim |
| Heap, "The Problem Brief" (landing page, PDF and blog) | Landing page: "A worksheet for defining product problems". PDF: headed "PROBLEM BRIEF TEMPLATE" on all four pages, with sections including "Hypothesis statement and metrics", "Problem Statement", "Launch Plan" and "Open Questions". Vijay Umapathy, Heap's Senior Director of Product Management: "a document that lays out the problem to be solved" | Settles that the worksheet label alone does not decide form. **Not a structural source**: pages 3 and 4 carry job stories and a launch plan, delivery content the library already ships |
| Atlassian Team Playbook, "Problem Framing" | "craft one concise problem statement that sums up the issue from the customer's perspective"; "The problem statement should include who is affected, what is affecting them, why it needs to be solved, and where the problem is happening". Also, in tension: "designed to align the entire team with one solution for a project" against "the goal today is to understand and define the problem, not to solve it" | Not needed for admission. Its editable template is gated and was not read |
| Jeff Gothelf, "Business Problem Statements vs Opportunity Statements" | "Here is the template we use as part of the Lean UX process to write business problem statements"; "We have observed [in these ways] that the product isn't meeting our expectations"; it is "Box 1 in the Lean UX Canvas" | A formula inside one canvas box, not a sectioned document. All rights reserved |
| GOV.UK Service Manual, "How the discovery phase works" | "reframe it as a problem to be solved"; "agreeing what is not part of the problem" | **A negative finding on form**: the practice is described and no written deliverable is named. Crown copyright, Open Government Licence |
| Design Council, "Framework for Innovation" | "The insight gathered from the discovery phase can help you to define the challenge in a different way" | **A negative finding**: the Double Diamond's own pages name no written Define deliverable (ADR 0068) |

One quotation was dropped by the raw check: Atlassian's "who, what, where, when, and why of a business problem"
does not appear on the cached play page.

#### The family: `discovery-docs`, amended to carry `define` (ADR 0069)

`discovery-docs` section 1 admits a type that "exists to decide whether to build something, before anyone
commits to building it", and its cadence clause says every member "is written once for a decision, and is
finished when that decision is made". A problem statement passes both: it settles which problem is worth
pursuing, before any solution is named, and Digital NSW, Atlassian and Gothelf each describe it written once,
at the start of an initiative. Nielsen Norman Group supports both readings, and its "return to your problem
statement and add to it" is revision during the discovery that the statement opens, not a standing cadence.
**What needed an amendment was the axis, not the membership test.** The contract pinned `discover`, and
ADR 0068 reserves `define` for exactly this kind of document. ADR 0069 records the costs: the first
`phase`-axis set, an inverted order inside the family, and a value check K can gate but cannot judge.

#### Sizes: two, by the maintainer's ruling, and what the full variant must earn

**The sweep's own finding was one lean variant, at high confidence.** Every admitting source describes a few
sentences or a short page. The sweep's problem-statement dimension put it plainly: a full variant "would be
inventing structure beyond what any source in this sweep actually shows".

**The maintainer ruled on 2026-10-11 for two sizes.** This spec does not argue that ruling back. It sets the
condition the full variant must meet: **every full-only section rests on a source the build reads, or it is
labelled this library's POSITION in the companion's Anatomy subsection and in the guide.** The build's
research ran a dimension aimed at longer and sectioned forms. It read Heap's PDF, Gothelf's formula, NHS
Scotland's Problem Framer, NHS Wales's guide and a Rose-Hulman course template. McKinsey's worksheet and
Atlassian's editable template could not be read. The `sizing_guidance` must say when the full variant earns its
extra sections.

The sweep already shows that the sources carry more than one paragraph's worth of named parts, even where
their form is short: Nielsen Norman Group's three required parts and its 5 Ws, Atlassian's four quadrants,
GOV.UK's "agreeing what is not part of the problem", Gothelf's measurable criteria, and Heap's "Hypothesis
statement and metrics" and "Open Questions". The section design below uses those.

#### Section design (settled by the build's research the same day)

The build's six research dimensions ran on 2026-10-11, before this spec merged, and their verdicts are folded in
here rather than added later as dated notes. The full variant carries **four** sections beyond lean, each of which
recurs in independent sectioned forms. The citations are in the bundle's research log.

| Section | In lean | What it carries |
|---|---|---|
| **Problem Statement** | yes | The statement itself: a few sentences, from the affected person's perspective, naming no solution. Nielsen Norman Group's "A concise description of the problem that needs to be solved"; NHS Wales's "about 18 words long"; Atlassian's who, what, why and where. Heap's PDF uses the same section label |
| **Background** | yes | Where the problem shows up, how it came to attention, and what is affecting the people who have it. Nielsen Norman Group's "The background of a problem"; Atlassian's "What is the nature of the problem?" |
| **Who Is Affected** | yes | The people who have the problem, specifically enough to find them, linked to a persona where one exists. Nielsen Norman Group's "The people affected by the problem"; Atlassian's who; NHS Scotland's "Who The Problem Most Affects" |
| **Impact and Why Now** | yes | What the problem costs the people who have it and the organisation, and why it matters now rather than later. Nielsen Norman Group's "The impact of the problem on the organization"; Atlassian's "What happens if we don't solve it?"; GOV.UK's "consider quantifying the value of solving the problem" |
| **Evidence** | yes | What shows the problem is real, where each piece came from, and how strong it is. Digital NSW's "Use the evidence you gather to document your clearly defined problem"; NHS Wales's "without evidence of your problem, you are left with opinion" |
| **How People Cope Today** | full only | How the people who have the problem work around it now, and what has already been tried and why it did not work, as evidence and never as an option. Heap's "How do people currently solve this problem?"; Heap's author on "how customers work around the problem"; the University of Waterloo's "Describe previous attempts to solve the problem and why they failed." |
| **What Is Not Part of the Problem** | full only | Neighbouring problems this statement deliberately leaves out, so the boundary is agreed before anyone scopes work. GOV.UK's "agreeing what is not part of the problem"; Rose-Hulman's "what is to be included and, perhaps more importantly, what isn't"; Atlassian's "In what circumstances does it not occur?" |
| **How We Will Know It Is Solved** | full only | Observable signals that the problem has shrunk, stated without naming a solution: the measure, its current level, and the direction. Gothelf's "these measurable changes in their behavior"; Heap's "Metric(s) and Baseline"; Rose-Hulman's "primary success criteria". **Contested**: Queensland's "Defining success" play treats measures as a later, separate activity, and the companion names the split |
| **Open Questions and Assumptions** | full only | What is not yet known, what is being assumed, and a root cause the team suspects, labelled as a hypothesis. Heap's "Open Questions"; the Canada School of Public Service on statements "based on assumptions"; the University of South Carolina's A3 template, which keeps the root cause as a later step |
| **Decision This Informs** | yes | Who decides whether this problem is worth pursuing, by when, and which document takes over if they say yes. GOV.UK's "Your discovery is finished when you've decided whether or not you want to move on to alpha"; Digital NSW's "Is the problem clear enough to investigate further?". Which document takes over is this library's POSITION, from the contract's successor obligation (`discovery-docs.md`, section 1) |

The lean variant's six sections are a strict ordered subset of the full variant's ten, as contract
section 3.2 requires. **What stays out at any size:** options, a recommended solution, a cost estimate, a
project scope or plan, a request for funding, and a constraints section. The first five are later documents'
jobs, and naming any of them breaks the section 2 rule that a `define` member names no solution, option, project
or investment. No source read labels a constraints section. **A root cause stays out of the statement itself**:
NHS Wales says "problem statements do not describe the solution or root causes", while Digital NSW's checklist
asks "Do we understand the root cause?". Keeping a suspected cause under Open Questions and Assumptions follows the
A3 template's separation, and it is this library's POSITION.

**Quality rules go to the guide, not the template**, under
[decision procedure 12](decision-procedures.md#12-a-property-or-section-is-proposed-for-a-template). Digital
NSW's review checklist and Nielsen Norman Group's quality rules are rubric rows, and the TRAP lines carry the
no-solution rule.

#### Boundaries with each named neighbour

**Not `business-case` (the duplication risk, named plainly).** `business-case`'s Problem and Opportunity
section does the same job inside an investment case. The standalone statement comes earlier and decides
something different: whether a problem is worth a project brief or a business case at all. A business case
that follows cites the statement, and its own section can then be shorter. The companion states this as the
library's POSITION, because no source read contrasts the two by name. *(Corrected by the build on 2026-10-11: one
source does contrast them by name, Six Sigma DSI's business-case guide, source [30] in the bundle's research log. The
order, statement first, is still the POSITION, because no source sets it.)*

**Not `project-brief`.** A project brief asks a named approver for authority to start initiation
(`project-brief`'s spec, above). A problem statement asks for no authority and names no project. The
project-brief research log records an APM Body of Knowledge passage that lists "problem statement", "project
brief" and "project charter" as names in common usage for one early rationale
(`project-brief_research-log.md:156`). The build read APM's own online glossary, which has no "problem
statement" entry and defines "Brief" and "Charter" as two different things. The companion cites only what the
glossary says, and notes that the collapse of the names is reported in practice.

**Not the PRD.** The PRD's Problem section restates a problem that has already been agreed, inside a
specification of what will be built. `prd_companion.md:141` already places the problem statement upstream of
the PRD.

**Not a hypothesis statement, a How Might We question or a job story.** Each points at a solution or at a
test of one. Gothelf's Lean UX canvas carries the business problem statement in box 1 and the hypothesis in a
later box; the SAFe epic hypothesis statement is written about an epic, which SAFe defines as "a significant
solution development initiative". **An opportunity statement is the same artefact phrased positively**, by
Nielsen Norman Group's and Gothelf's accounts, which is why it is an alias rather than a neighbour.

**Not the opportunity solution tree, the lean canvas or the Shape Up pitch.** Each carries a solution, and
ADR 0068 records why none is a Define candidate.

#### Metadata

| Field | Value | Why |
|---|---|---|
| `family` | `discovery-docs` | ADR 0069 |
| `phase` | `define` | ADR 0068 reserves it for a document that frames one problem and names no solution; contract `0.3.0` section 2 |
| `sizes_available` | `[lean, full]` | The maintainer's ruling, 2026-10-11, against the sweep's lean-only finding. The full variant's conditions are above |
| `default_size` | `lean` | Every admitting source describes a short artefact |
| `status` | `beta` | Every bundle |
| `methodology` | `methodology-agnostic` | The admitting sources span UX discovery (Nielsen Norman Group), public-sector service design (Digital NSW), Lean UX (Gothelf) and product management (Heap). A single methodology would misdescribe at least two of them |
| `pairs_with` | `[define-problem-statement]` | pm-skills ships the skill at `phase: define`; its own description says it "Creates a clear problem framing document with user impact, business context, and success criteria". **The landing PR adds the ID to `tools/known-skills.txt`**, which does not list it today, after re-reading the skill at pm-skills `main` |
| `related_templates` | `[business-case, project-brief, user-persona, prd]`, inline | The two documents that take over, the persona that names who is affected, and the PRD whose companion already points here. Inline, because check I drops the first entry of a block list |
| `aliases` | `problem brief`, `opportunity statement` *(changed 2026-10-22 by decision sitting items D6 and D9: `opportunity statement` became catalog entry 207, a type of its own, and `point of view statement` was added)* | "Problem brief" is Heap's name. "Opportunity statement" is the same artefact phrased positively: Nielsen Norman Group says problem statements that capture opportunities "are sometimes referred to as opportunity statements instead of problem statements, although they are written and used in the same way" (raw-checked in the build). ModernAnalyst argues the two differ for projects, and the companion reports that dissent. Neither appears as an alias on any shipped bundle or catalog row (checked 2026-10-11 against every `_meta.yaml`, `manifest.json`, `catalog.md` and `atlas/catalog-data.json`) |

#### The catalog row the build PR adds

Under [ADR 0030](decisions/0030-templating-scope-markdown-documents.md), a new type's catalog row waits for
its own research to find a named source. The sweep found two. The row lands on the build branch **before the
build runs**, because `.claude/commands/build-bundle.md` requires a catalog entry first, and it lands in the
build PR with the count sweep from 205 catalog types to 206.

```json
{
  "id": "problem-statement",
  "name": "Problem Statement",
  "aliases": ["problem brief", "opportunity statement"],
  "category": "Research / Discovery",
  "stage": "discovery",
  "owner": "PM / UXR",
  "purpose": "Frame one problem, who has it, the evidence that it is real, and why it matters, before any solution is named",
  "methodology": "UX discovery / service design",
  "formality": "lightweight",
  "rarity": "common",
  "size_variant": "S",
  "tier": 2,
  "tier_inferred": true,
  "must_have": false,
  "relationships": ["Business Case", "Project Brief", "PRD"]
}
```

`built` and `state` are derived by `tools/gen-atlas.py`. Three fields are this spec's judgment, not sourced
facts: `rarity`, `owner` and `methodology`. The build must match the row's field set to its neighbours in
`atlas/catalog-data.json` and give it the next entry number in `docs/internal/catalog.md`.

#### `pairs_with`: one pairing, to be pinned at landing

`define-problem-statement` was read on 2026-10-11. Its "When NOT to Use" list routes a reader to `deliver-prd`
when "The problem is already agreed and engineering needs the spec", and to `define-hypothesis` when the
problem "is really an unvalidated assumption". Both boundaries match this spec's. Its output sections,
Problem Summary, User Impact, Business Context, Success Criteria, Constraints & Considerations and Open
Questions, are **not** a source for this bundle's section design: pm-skills is a sibling repository, not a
named external source, and the sections above stand on their own citations.

#### Risks for the build and the review

1. **The full variant is where invented structure would enter.** The sweep found high-confidence evidence for
   a short artefact. Any full-only section that cannot cite a source the build read must say it is the
   library's POSITION, in the companion and in the guide's variant chooser. A review lens that finds a
   full-only section presented as sourced, without a logged source, files it as blocking.
2. **The duplication with `business-case` is the reason this bundle could be declined, and the companion must
   not hide it.** Its Relationships section names the overlap and says what the standalone statement adds.
3. **Heap is not a structural source.** Its PDF carries delivery content on pages 3 and 4, and its own
   landing page calls the artefact a worksheet. The companion may cite Heap for the name "problem brief" and
   for the section labels on its first two pages, and nothing more.
4. **Atlassian's tagline and run-sheet disagree.** Report both quotations; do not resolve which governs.
5. **The templates stage has repeatedly reused the worked example's own scenario in GOOD and WEAK text.**
   `business-case`'s own Problem and Opportunity GOOD text does it ("2026-05 friction study"). Before the
   review closes, grep both templates for the example's nouns: `Priya Nair`, `Dana Okoro`, `Elena Cho`,
   `Meridian Freight`, `Recurring Analyst`, `dataset picker`, `second dashboard view` and `31 percent`.
6. **A problem statement that names a solution fails its own family rule.** The example's title and every
   section must avoid the names the later documents give the solution: "Question-First Entry", "modelling
   defaults", and the business case's option identifiers.

#### What landing this bundle closes elsewhere

1. **The contract's Members line** changes from "not yet built" to the build date.
2. **`business-case_example.md:15-28`'s callout becomes false** the day this example exists, because it says
   the case is ahead of everything except the persona, the project brief and the product vision. The landing
   PR adds a one-line dated correction, as it did for the project brief.
3. **`business-case_guide.md`'s "Write something else if" table gains a problem-statement row**, for a reader
   who needs to agree on a problem before any investment is proposed. `business-case`'s history records it.
4. **`tools/known-skills.txt` gains `define-problem-statement`.**
5. **The catalog row**, the 205-to-206 catalog count sweep, and the 41-to-42 bundle count sweep. The phase
   axis then holds 26 bundles and the classification axis 16, and `define` holds its first.
6. **`README.md`'s `discovery-docs` paragraph** (`README.md:224` as of `f6f0b648`) says the family's members "answer whether
   the investment is worth making and who it is for". It gains which problem is worth solving.
7. **This page's Progress table.**

#### The example

**A problem statement for the problem that the Question-First Entry project brief and business case later
answer**, dated **2026-01-09** and written by Priya Nair, PM, Reporting. That is four days after the
[user persona](../../templates/user-persona/user-persona_example.md) (2026-01-05), five days before the
[product vision](../../templates/product-vision/product-vision_example.md) (2026-01-14), seven days before the
[project brief](../../templates/project-brief/project-brief_example.md) (2026-01-16) and eleven days before
the [business case](../../templates/business-case/business-case_example.md) (2026-01-20). It extends the
family's thread backward, as contract section 4 requires. It does not disturb `README.md:224` (as of `f6f0b648`)'s claim that
the persona is the library's earliest document.

**Facts it may read, all of them Acme's own and older than the statement.** From
`project-brief_example.md:32-47` and `business-case_example.md:37-55`: the December 2025 leadership review at
which Dana Okoro, VP Product, raised the flat revenue-per-account trend, and finance asked for a funding
decision; the trend held for five quarters; only 31 percent of new accounts build a second dashboard view
within 14 days of signup; the drop concentrates at the step where a new account first has to pick which
table, which join and which measure answers their question; two-thirds of the accounts that stall there never
return to authoring; sign-ups grew 40 percent over the same period; the segment that stalls, an account with no
dedicated analyst and no query background, is the fastest-growing part of the signup base; and two years of
incremental investment in documentation, tutorials and services capacity has not moved the number. From
`user-persona_example.md`: the Recurring Analyst and Elena Cho, from interviews across November and December
2025 (n=12), cited the way `project-brief_example.md:40-42` cites them.

**What it must not cite or contain.**

1. **No solution, option or investment.** Not "Question-First Entry", not "modelling defaults", not any of the
   business case's options, and no recommendation. This is the section 2 rule, and the example is where a
   reader learns it.
2. **No document dated after 2026-01-09 cited as existing**: not the product vision, the project brief, the
   business case, the FY26 product strategy, or anything later.
3. **No 2026-05 Reporting friction study, no Saved Views, no Reporting Platform Modernization program, and no
   Marta Reyes.** Those are mid-2026 facts of the delivery thread.
4. **No early-prototype figures.** The 71 percent question-resolution figure and the business case's 6-11
   point benefit range are later analysis, as the project-brief spec already ruled.
5. **No staged case vocabulary** (SOC, OBC, FBC), which `business-case_example.md:5` rules out.

**Decision this informs, closing the loop honestly.** The statement asks Dana Okoro whether the problem
warrants a project brief. It may say that a brief is the next step if she agrees, as an intention. It must not
describe the brief's contents, its date or its outcome. The brief, arriving seven days later, is what took
over, and nothing here is invented for the statement to hand off to.

### strategy-docs (fifth member, by amendment): north-star-metrics

**`north-star-metrics`** - `strategy-docs`, **`classification: foundation`**, sizes **`[lean, full]`** (the
maintainer's ruling, with a stop condition; see below), default `lean`, catalog entry **8**
(`north-star-metric-definition`), `pairs_with: []`. **The maintainer chose on 2026-10-12 to admit the type by
amending `strategy-docs`, to build two sizes, to route the formula to `kpi-dashboard`, and to leave the existing
members' companions as they are. The same day, after the build's research, the maintainer accepted the
recommendation to place it third in the chain, between the strategy and the roadmap.** The contract edits of
[ADR 0070](decisions/0070-north-star-metrics-joins-strategy-docs-as-a-fifth-member.md) land with this spec, so the
metadata below is written against contract `0.2.0`.

**The bundle id is plural by the maintainer's ruling of 2026-10-11, and the document still defines one North Star.**
The catalog id stays `north-star-metric-definition`, in the shape `change-log` set against `change-log-governance`.
Amplitude's playbook says: "An obvious characteristic of the North Star Framework is that there's only one North
Star Metric." Mixpanel agrees: "Companies typically have only one North Star metric." The plural names the practice,
as Herbig's title does ("How to connect North Star Metrics, Product Strategy, and OKRs"). One filled document defines one North Star for one
product, with its input metrics beneath it. A review lens that reads the plural as a claim of several North Stars is
answered here.

#### Demand: two shipped companions already point at it

**`product-vision_companion.md:271-273` separates the metaphor from the artifact.** It reads: "As a metaphor, "north
star" describes what a vision does. As an artifact, a **North Star Metric** is a distinct quantitative thing", and it
cites Herbig calling the metric "the quantified sibling of the Product Vision". **`kpi-dashboard_companion.md:185-187`**
lists the North Star Metric as one way to frame a dashboard: "One headline value metric with a few input metrics
beneath it". No bundle answers either pointer.

**The shared scenario has the same gap.** "Time to Insight" acts as the headline metric in the `okrs`,
`kpi-dashboard`, `product-strategy` and `product-vision` examples, and no example calls it a North Star. See
[The example](#the-example-acmes-north-star) for why it cannot simply become one.

#### Admission: retrieved and raw-checked on 2026-10-05, with one read on 2026-10-12

The admission sweep of 2026-10-05 read the type's sources, and the main loop checked every returned quotation against
raw page text. Every quotation below passed that check, except the Reforge lines, which come from a browser read on
2026-10-12.

| Source | What it says | Weight |
|---|---|---|
| Amplitude, "The North Star Playbook" (PDF) | "When you define the metric, you complete this template: Our North Star Metric is called X, which we define as Y."; "The worksheet on the following page helps your teams fill in the blanks to create your North Star statement." | **Admits on its own** ([ADR 0048](decisions/0048-one-named-source-clears-the-admission-test.md)). Vendor tier. All rights reserved |
| Amplitude, "How-To Guide: Running Your North Star Workshop" (2024, PDF) | Blank fields, among them "What's your product's North Star?" and rows for input metrics; a checklist that asks "Does it express customer value?", "Is it a leading indicator of success?" and "It's not a vanity metric?"; "The inputs are the actionable factors that combine to drive your North Star Metric." | The same publisher. Evidences the case for the metric and the input metrics as fields. All rights reserved |
| Amplitude, North Star hub | "You should revisit your North Star metric periodically, whenever there's a significant shift in your product, market, or business strategy." | The cadence, which makes the type `foundation` |
| Mixpanel, "What is a North Star metric?" (blog) | "Companies typically have only one North Star metric."; "Companies should feel equally free to reevaluate their North Star metrics to make sure they still point the right direction, and amend them when they prove flawed."; and a dissent, "However, a single north star can be limiting, especially if your company has multiple core products with separate goals" | Explains the practice; publishes no document of its own |
| Tim Herbig, "How to connect North Star Metrics, Product Strategy, and OKRs" | "North Star Metrics are persistent goals that influence Product Strategy"; "OKRs are point-in-time goals that implement that Strategy" | The source for second place, the considered alternative; see [the chain position](#the-chain-position-is-contested). Practitioner tier |
| Reforge, North Star Metric artifacts page (read in a browser, 2026-10-12) | "Explore 2 examples of North Star Metrics so you never have to start from scratch." The two are member-submitted: a framework for cascading goal targets through a leadership team, and a brand concept document | **A negative finding.** Neither is a North Star metric template, and the page shows no field names. Admission stays on one publisher |

**Admission rests on one publisher, Amplitude, in two of its own documents.** The sweep's other sources, among them
Mixpanel, Herbig and Sean Ellis, explain the practice without publishing a document. The single-publisher basis is
enough under ADR 0048, and the companion must state it plainly.

#### The family: `strategy-docs`, amended to a fifth question (ADR 0070)

`strategy-docs` section 1 admits a type that "sets or tracks product direction above the level of any single
deliverable". A North Star metric does that on its face. What needed an amendment was the closed list of four
questions that follows the sentence. ADR 0070 records the three other routes it tested, `standing-standards`,
`governance-docs` and a decline, and why each was rejected.

**Where it sits.** Third, between the product strategy and the product roadmap, inferred from what a North Star
depends on. The contract's new chain link is labelled the library's POSITION, because no source read states the
failure that link names, and no source states this sequence. The next subsection gives the evidence on each side.

#### The chain position is contested

The build's research found two kinds of evidence about where the North Star sits, and they do not answer the same
question.

**Sequence: which document comes first.** Two sources say, and they disagree.

- **Tim Herbig puts the North Star first.** "...first defining your North Star Metric, then articulating a Strategy and
  finally establishing OKRs ensures each gets the attention it deserves." He also writes: "Your North Star Metrics
  shouldn’t be set backwards from a KPI dashboard but develop forwards from your Product Vision."
- **Adam Farren puts it last.** His sequence runs "everything starts with your vision", then "Next you build product
  and go-to-market strategy", then "Then set your goals". Only then does he ask: "So how do you bring all of that -
  vision, strategy, tactics - into alignment? Defining a North Star metric is a great step." That account makes the
  North Star an alignment device across the chain, not a link inside it.

**Dependency: what the North Star is made of.** Four publishers describe the North Star as measuring the current
strategy, which makes the strategy an input to it.

- Amplitude: a good North Star includes "A metric that serves as a key measure of your current product strategy".
  Its own change of North Star was justified as one that "better reflects our current product strategy".
- Swiss Post: "It represents the core of the product strategy."
- Spotify's Confidence glossary: "The north star should reflect the current strategic question".
- Umbrex: "Only change the NSM when strategy or product fundamentally shifts".

These are not cleanly opposed to Herbig, who also calls the North Star an input to the strategy. **No source places
the North Star third, between the strategy and the roadmap, as a sequence.** That position would be an inference from
the dependency evidence. Every source that relates the North Star to OKRs puts it above them.

**The maintainer first chose second place on 2026-10-12, before this research ran, on the premise that Herbig's was
the only order a source supported.** That premise was wrong. Re-presented with this evidence the same day, the
maintainer accepted the recommendation of third place, which was given at low confidence. This library's reasoning
is that a measure of the strategy cannot come before the strategy it measures. Third place also keeps every
source's placement of the North Star above OKRs. The companion names both camps, and the contract's chain link
stays the library's POSITION.

#### Sizes: two, under the `problem-statement` rule, with a stop condition

The catalog calls the type "S/M". The maintainer ruled on 2026-10-12 for two sizes, under the rule set for
`problem-statement`: **every full-only section rests on a source the build reads, or it is labelled this library's
POSITION in the companion's Anatomy subsection and in the guide.** One condition is added for this bundle. **If the
build's research cannot support a full variant, the build stops and reports to the maintainer rather than padding
one.** The `sizing_guidance` must say when the full variant earns its extra sections.

#### Section design (settled by the build's research, 2026-10-12)

Six research dimensions ran on 2026-10-12, before this spec merged, and their verdicts are folded in here rather
than added later as dated notes. They filed 66 sources and 347 quotations. The main loop checked every quotation
against raw page text, and 288 passed as filed. Most failures were formatting: numbered lists joined into one
quotation, and dashes that did not survive extraction. The Umbrex page refused a plain fetch, so it was read in a
browser, and all ten of its quotations passed there. **Four GitHub files that package the North Star Metric as an
agent skill are not structural sources**, because no named publisher stands behind them. The citations are in the
bundle's research log. **Every field name is this library's own wording.** Amplitude's documents are all rights
reserved, so the template does not reproduce Amplitude's worksheet, its field labels, its sidebar heuristics or its
worked examples.

**The full variant is earned.** Each of its four extra sections rests on at least two independent publishers, so the
stop condition in Sizes does not trigger.

| Section | In lean | What it carries | Evidence |
|---|---|---|---|
| **The North Star** | yes | The metric's name and its definition in one statement: the behaviour it counts, who does it, and over what window. The product it covers, where a company has more than one. The operational formula is not here; the section routes it to `kpi-dashboard`'s Metric Definitions | Amplitude's "Our North Star Metric is called X, which we define as Y."; Cut the SaaS's "Pick a metric that counts that action across a sensible time window, like weekly."; Ballpark's "Prefer a definition people can explain, inspect and reproduce." |
| **Why This Metric** | yes | The customer value it expresses, in the customer's terms; why it leads revenue rather than lagging it; why it is not a vanity metric; and what shows it predicts retention or revenue in this product's own data | Amplitude's checklist, "Does it express customer value?" and "Is it a leading indicator of success?"; Amplitude's "Validate that it predicts retention and revenue in your own data."; Koji's "You cannot write this sentence by staring at a dashboard."; Basedash's "Write down the value your product delivers in one sentence." |
| **Input Metrics** | yes | Three to five measures that teams can move and that combine to drive the North Star, each with an owner | Amplitude: "Inputs are a set of three to five influential, complementary factors"; Basedash's "Each input is something a specific team can own and affect directly."; Umbrex, on which teams own which inputs, gives each team one to three. Amplitude's "breadth, depth, frequency, and efficiency" is one vendor's heuristic, and Mixpanel structures inputs in levels instead; the companion reports both |
| **What It Serves** | yes | The product strategy it measures, the vision that strategy serves, and the business outcome it is expected to predict. This library places the North Star after the strategy, and Herbig orders the two the other way; see [the chain position](#the-chain-position-is-contested) | Amplitude's "A metric that serves as a key measure of your current product strategy"; Herbig, for the other order; the worksheet field "What will the impacts to the business be?" |
| **When We Revisit It** | yes | The signal that would trigger a review, and what would change it, not a calendar date | Amplitude's playbook, "What will be your signal to revisit this metric?"; Umbrex, "Only change the NSM when strategy or product fundamentally shifts"; Spotify's Confidence glossary, "Changing the north star is a significant organizational decision." |
| **Candidates Considered** | full only | The other metrics weighed, and why each was rejected | Amplitude's playbook passage on a delivery app that "had considered potential North Star Metrics"; Basedash; Cut the SaaS. Five of the gap dimension's sources carry it |
| **Guardrails** | full only | The measures that must not get worse while the North Star rises | Cut the SaaS, "The fix is pairing your north star with guardrail metrics like retention and gross margin."; Ballpark, "Pair the shared measure with checks for harm or declining quality."; Umbrex's guardrails, "to prevent “hitting the target but missing the point.”" |
| **What It Does Not Tell Us** | full only | The metric's blind spots, how it could be gamed, and what it is too slow to show | Amplitude's playbook, "What doesn't this metric tell you?"; Umbrex, "How do we keep the NSM from being gamed?"; Spotify's Confidence glossary, "North star metrics tend to be high-level and slow-moving." |
| **Definition History** | full only | Each earlier definition, the date it changed, and why, so that a break in the series is explained | Ballpark, "Preserve the old definition and explain the break in the series"; Mixpanel, "Every metric should have clear documentation", including how it is defined and calculated.; Amplitude's own account of moving its North Star from one definition to another, with its reasons |

The lean variant's five sections are a strict ordered subset of the full variant's nine, as contract section 3.2
requires. **Two findings go to the guide, not the template**, under
[decision procedure 12](decision-procedures.md#12-a-property-or-section-is-proposed-for-a-template): the one-sentence
test (Basedash, "Everyone from sales to engineering should be able to say what it means in one sentence.") and the
planning filter (Cut the SaaS, "does this move the north star?"). Both are rubric rows.

**Where the formula lives is the library's POSITION.** No source read addresses whether a North Star document should
carry the metric's precise calculation or leave it to an analytics specification. The sources state a definition with
its behaviour and window wherever they name a North Star, which this bundle keeps. The calculation, data source,
exclusions and refresh go to `kpi-dashboard`, as the maintainer ruled on 2026-10-12.

**The methodology is growth and the North Star Framework, not OKR.** Amplitude's playbook lists "A goal-setting
framework, like objectives and key results (OKRs)" under "What the North Star is not". The growth lineage rests on
Sean Ellis's advocacy, not on a claim that he coined the term. Intercom's interview with him calls the North Star
Metric "Sean’s way of quantifying the point where customers experience the value of your product", and describes it
as "a key cog in a sustainable growth strategy". Neither Amplitude document mentions Ellis. The metadata below keeps
`growth/north-star-framework`.

**What stays out at any size:** the operational formula, the data source and refresh schedule, targets and
thresholds, and a dashboard layout. Those are `kpi-dashboard`'s job. A tree of metrics below the inputs stays out
too: the catalog lists a metric tree as its own type, which places the North Star at its top node.

#### Boundaries with each named neighbour

**Not `kpi-dashboard` (the duplication risk, named plainly).** `kpi-dashboard`'s Metric Definitions section already
carries a headline metric's formula, scope, exclusions and known limitations. This bundle carries one statement line
and routes the rest there. What it adds is the case for choosing the metric and the input metrics, which no bundle
carries. The companion states this division as the library's POSITION.

**Not `product-vision`.** The vision says where the product is going and why. The North Star metric says which number
shows it is getting there. `product-vision_companion.md:271-273` already draws this line, and the new companion cites
it rather than restating it.

**Not `product-strategy`.** The strategy chooses which problems to solve. The North Star metric names the one measure
that shows the strategy is working, so in this library's chain it comes after the strategy. Herbig places it
before, as a persistent goal that influences the strategy, and the companion reports both.

**Not `okrs`.** OKRs are reset each period. A North Star metric persists and is revisited when the product, market or
strategy shifts. Herbig: "OKRs are point-in-time goals that implement that Strategy".

**Not `tracking-plan`.** A tracking plan specifies the events a metric is computed from. This bundle names the metric.

**Not the `product-vision` alias "north star statement".** `product-vision_meta.yaml` carries that alias, in the
metaphor sense. This bundle's aliases must not repeat it, and its `summary` must make the difference clear, because a
search on "north star" returns both.

#### Metadata

| Field | Value | Why |
|---|---|---|
| `family` | `strategy-docs` | ADR 0070 |
| `classification` | `foundation` | Argued and revisited on a trigger, not maintained on a calendar; contract `0.2.0` section 2 |
| `sizes_available` | `[lean, full]` | The maintainer's ruling, 2026-10-12, with the stop condition above |
| `default_size` | `lean` | The admitting source describes one statement and a short worksheet |
| `status` | `beta` | Every bundle |
| `methodology` | `growth/north-star-framework` | Amplitude's playbook lists OKRs under "What the North Star is not", so the catalog's "growth/OKR" is not carried over. Amplitude formalized the framework, and Intercom's interview ties the metric to Sean Ellis's growth practice; see Section design |
| `pairs_with` | `[]` | `tools/known-skills.txt` lists no North Star or metric-definition skill |
| `related_templates` | `[product-vision, product-strategy, okrs, kpi-dashboard, product-roadmap]`, inline | The four existing members, and the dashboard that carries the formula. Inline, because check I drops the first entry of a block list |
| `aliases` | `north star metric`, `nsm`, `north star metric definition` | What practitioners call the document. Not "north star statement", which `product-vision` carries, and not "North Star framework", which names the method rather than the document |
| `catalog_ref` | `8` | Catalog entry 8, `north-star-metric-definition` |

#### The catalog row the build PR corrects

Catalog entry 8 exists and stays `north-star-metric-definition`. Under
[procedure 1](decision-procedures.md#1-a-catalog-call-loses-to-research), the build PR corrects what its research
contradicts. Two fields are already in question. Its `methodology` reads "growth/OKR", and its aliases include "North
Star framework", which names the method rather than the document. `built` and `state` are derived by
`tools/gen-atlas.py`.

#### Risks for the build and the review

1. **The plural id will draw a finding.** The answer is in this spec's second paragraph. A lens that files it anyway
   is pointed here.
2. **Admission rests on one publisher, and that publisher reserves all rights.** The template's field names and
   layout must be original. A review lens that finds Amplitude's wording reproduced as a field label files it as
   blocking.
3. **The duplication with `kpi-dashboard` is the reason this bundle could have been declined.** A template section
   that asks for the formula, the data source or a target duplicates `kpi-dashboard`, and the review files it.
4. **The full variant is where invented structure would enter.** Any full-only section without a logged source must
   say it is the library's POSITION. If none can be sourced, the build stops (see Sizes).
5. **The metaphor and the artifact share a name.** The companion must keep "north star" as a description of a vision
   apart from the North Star metric, as `product-vision`'s companion does.
6. **The templates stage has repeatedly reused the worked example's own scenario in GOOD and WEAK text.** Before the
   review closes, grep both templates for the example's nouns, which the build lists once the example exists, and for
   `Acme`, `Time to Insight` and `Dana Okoro`.

#### What landing this bundle closes elsewhere

1. **The contract's Members line** changes from "not yet built" to the build date.
2. **`README.md`'s `strategy-docs` heading** (`README.md:211` as of `c531d737`) reads "complete, four bundles". It becomes five, and the
   family paragraph gains the North Star metric. `README.md:158` (as of `c531d737`)'s "ten complete families" is false from this spec's
   merge until the build lands, as it was for `discovery-docs`.
3. **The bundle count sweep from 42 to 43.** The classification axis then holds 17 bundles.
4. **The catalog row's corrections**, above.
5. **No existing member's companion changes** (the maintainer's call, 2026-10-12; ADR 0070 states the gap). Whether
   `kpi-dashboard`'s guide gains a routing row, for a reader who needs to choose the headline metric rather than
   define it, is a build decision.
6. **Issue #253 (bundle: north-star-metrics)** closes with the build PR.
7. **This page's Progress table.**

#### The example: Acme's North Star

**A North Star metric for Acme Analytics, dated between 2026-01-29 and 2026-02-10.** That is after the
[product strategy](../../templates/product-strategy/product-strategy_example.md) (2026-01-28) and before the
[product roadmap](../../templates/product-roadmap/product-roadmap_example.md) (2026-02-11), which is where
ADR 0070 places the type in the chain. `tools/check-example-chronology.py` fails a body-prose link to any example
dated later.

**It cannot name "Time to Insight" as Acme's North Star.** Two shipped examples label Time to Insight a lagging
measure: `kpi-dashboard_example.md:53` marks it "lagging", and `product-strategy_example.md:110` lists it under
"Lagging". Amplitude's checklist asks "Is it a leading indicator of success?" An example that adopted Time to Insight
as its North Star would contradict two siblings or fail its own checklist. **The research settled the shape on
2026-10-12: a leading measure of the value an account gets is the North Star, and Time to Insight is the lagging
company goal it is expected to predict.** No source read proposes a time-based measure as a North Star, and the
input-metrics dimension searched for one in analytics products specifically. Every source asks for a measure of
value that leads revenue.

**Facts it may read, all of them Acme's own and dated before the example.** From the vision: the 2029 horizon, the
statement about answering a question "in the time it takes to ask it out loud", and the goal of removing the analytics
team as a bottleneck. From the [problem statement](../../templates/problem-statement/problem-statement_example.md)
(2026-01-09), the [project brief](../../templates/project-brief/project-brief_example.md) (2026-01-16) and the
[business case](../../templates/business-case/business-case_example.md) (2026-01-20): the 31 percent of new accounts
that build a second dashboard view within 14 days, and the segment that stalls. From the product strategy
(2026-01-28): its diagnosis, its leading indicator, and its lagging measures, which are self-serve net revenue
retention and the "Time to Insight" goal. The strategy's leading indicator is the share of new accounts that build a
second view within 14 days, from a 31 percent baseline. The strategy's 50 percent target stays out, because targets
are `kpi-dashboard`'s.

**It must reconcile with the strategy's leading indicator.** The strategy example says "The moment a user builds
their second view is our leading indicator." It adds: "Every team sees the same number, on the same dashboard,
weekly." That shared number is the second-view measure, and a North Star dated after those sentences must account
for it. Either the second-view measure is the North Star, or it is one of the input metrics and the example says how
the North Star relates to the number every team already watches weekly. The build chooses, reports why in the build
PR, and matches every figure it shares with the strategy exactly.

**What it must not cite or contain.**

1. **No document dated after the example cited as existing**: not the roadmap, the OKRs, the PRD, the KPI
   dashboard or the tracking plan. A reader's note in the opening blockquote may point forward, as other
   examples' notes do.
2. **No operational formula, data source or target.** Those are `kpi-dashboard`'s, and the example demonstrates the
   boundary.
3. **No Amplitude example reworded.** That covers its Spotify and do-it-yourself kit cases, and above all Amplitude's
   account of its own North Star, a weekly count of users who query and later of users who share what they learn. It
   is the one analytics-product North Star in the research, it is all rights reserved, and Acme sells an analytics
   product, so the pull to borrow it is strong. Acme's North Star is its own, drawn from Acme's vision.
4. **No figure that contradicts a sibling.** Any number the example shares with an earlier example matches it exactly.

### standing-standards (sixth member): the business continuity plan, with disaster recovery inside it

**`business-continuity-plan`** (bundle id by the maintainer's ruling of 2026-10-13; the catalog id stays
`disaster-recovery-business-continuity-plan`, in the shape `north-star-metrics` kept against its own catalog id
`north-star-metric-definition`) - `standing-standards`, **`classification: tool`** (maintainer's ruling,
2026-10-13; argued in
[ADR 0071](decisions/0071-business-continuity-plan-joins-standing-standards-as-a-tool.md)), sizes
**`[lean, full]`**, methodology set at build from the admitting sources' lineage (the catalog's `ITIL/SOC2` has
no supporting source; see the catalog corrections below), catalog id `disaster-recovery-business-continuity-plan`
(catalog 134, atlas) / catalog.md row 135. Catalog owner: SRE / Risk. Purpose: "Plan recovery from major
disruptions". Contents, per the catalog: "RPO/RTO, scenarios, recovery steps, roles, testing". `size_variant:
M/L`, `rarity: occasional`, `tier_inferred: true`.
**The catalog's own category field disagrees with itself across the two machine artifacts**:
`docs/internal/catalog.md:199` reads "operations/governance", and `atlas/catalog-data.json` index 134 reads
"Operations / Incident". Neither this spec nor ADR 0071 adjudicates that; the catalog corrections subsection
below flags it for the landing PR.

**One bundle, not two, settled by the maintainer.** The Business Continuity Plan is the primary document;
disaster recovery is a section inside it, not a sibling document. This spec does not reopen that call. It
exists to write the bundle the maintainer already decided to build.

#### Demand: prose routing, not a promise tag, from two already-shipped bundles

No `future:` tag points here. A grep of every `_meta.yaml` for a promise tag naming disaster recovery or
continuity returned nothing, so no tag needs correcting. That differs from the `future:launch-checklist` fix
[ADR 0053](decisions/0053-launch-coordination-checklist-joins-standing-standards-as-a-tool.md) made. The demand
is prose, already shipped, in two bundles that each name this type as the thing they are not:

- `templates/runbook/runbook_template-lean.md:34` and `templates/runbook/runbook_template-full.md:41` both state
  the boundary inside the template body itself, not only the guide, in slightly different words. Lean says a
  runbook is "NOT a disaster recovery plan (that recovers one or more systems at an alternate facility after a
  major failure, one register above this)". Full says "NOT a disaster recovery plan (NIST scopes that to
  recovering one or more systems at an alternate facility after a major failure, one register above this)".
  `runbook_guide.md:26` repeats the same routing in the operator card: "You need to recover a whole system at an
  alternate facility after a major failure. That is a disaster recovery plan, one register above what this
  template covers." The routing names a document and does not link to one, because none exists yet.
- `templates/runbook/runbook_companion.md:303-307` and `:377-380` both carry the NIST boundary at length, citing
  the same CSRC glossary definition this sweep independently re-verified. Both also say the vendor usage that
  blurs runbook and DR plan together is left unresolved rather than adjudicated.
- `templates/production-readiness-review/production-readiness-review_example.md:85` defers disaster recovery
  outright: "Backup and disaster recovery for that database is Platform's own standing responsibility, reviewed
  under Platform's own instrument, and is not duplicated here". Line 74's Readiness Criteria row, "Data and
  backup, disaster recovery", is marked Not Applicable on that ground: Platform's own instrument covers it. The
  library ships no bundle for that instrument today.

This is real routing, the same shape `production-readiness-review`'s own demand section described for the
launch-coordination-checklist relationship, not a gate obligation. No check fails today for leaving this type
unbuilt. Building it resolves both forward-references rather than competing with either bundle's existing
content, per [ADR 0041](decisions/0041-maintainer-preference-sets-the-build-order.md)'s rule that the
maintainer's preference sets the build order.

#### Admission: two different strengths for the two halves of the catalog's merged name

**Business Continuity Plan admits decisively, on a literal fill-in federal template.** FEMA, through its Ready
Business program on Ready.gov, ships a four-page Business Continuity Plan PDF template with named sections and
tables. Those tables include a team roster, a vendor and contractor list, and a revision history table. Its
Appendix names "Information Technology Disaster Recovery Plan (if not included in the business continuity
plan)". It also names "Schedule, triggers, and assignments for the periodic review of the business continuity
and IT disaster recovery plan." Both spans passed the recheck against the live PDF. A separate, shorter
Ready.gov page, `ready.gov/business-continuity-plan`, carries the sentence "Organize a business continuity team
and compile a business continuity plan to manage a business disruption." That sentence also passed the
recheck, on that page. The nearly identical phrase inside the PDF template itself failed the recheck, because
the PDF's exact wording did not match. So that sentence is attributed here to the shorter page, never to the
PDF. NIST SP 800-34 Rev. 1 independently defines a Business Continuity Plan as "The documentation of a
predetermined set of instructions or procedures that describe how an organization's mission/business processes
will be sustained during and after a significant disruption." That is a second, independent primary source.
Confidence: high.

**Disaster Recovery Plan's admission is weaker, and rests on a definition, not a template.** NIST SP 800-34
defines a DRP as "A written plan for recovering one or more information systems at an alternate facility in
response to a major hardware or software failure or destruction of facilities." That span passed the recheck.
But NIST's own template-building effort went to a different artifact, the Information System Contingency Plan,
in Appendix A, not to a standalone DRP. NIST's glossary page also carries a second, conflicting definition from
CNSSI 4009-2022. That definition scopes DRP to the whole enterprise rather than to a relocated facility, inside
the same federal page. The admission bar (one named source publishing a type as a written document) reads
disjunctively as definitional-or-template, so a definitional reading clears it. A reader who expected a
template-grade clearance for the DRP half specifically would not find one. Confidence: high that the bar
clears on the definitional reading; the one-document-or-two section below carries the consequence of that
weaker clearance.

#### One document or two: the gap-fill's finding

A 2026-10-12 gap-fill was run specifically to settle whether a standalone, template-grade Disaster Recovery Plan
exists anywhere as a document. Such a document would be distinct from a Business Continuity Plan's own DR
appendix. It returned a high-confidence negative, checked across government, standards and practitioner tiers.

**No named source anywhere in this sweep ships a complete fill-in template titled and scoped as a standalone
"Disaster Recovery Plan."** Of the sources this sweep read, SANS Institute's "Disaster Recovery Plan Policy"
comes closest to publishing the type under that exact name. It undercuts its own standalone reading in its
own text: "The Disaster Recovery Plan is often part of the Business Continuity Plan." That span passed the main
recheck against the SANS-hosted PDF, and the gap-fill checked it again. The page is gone from SANS's live
policy library, which now lists 36 current templates and no DRP-titled one. So the document survives only on a
SANS-hosted CDN asset and third-party mirrors. California's SIMM 5325-A, "Technology
Recovery Plan Instructions," is the one template-grade structure found in the entire sweep. It runs fourteen
numbered sections across two parts. Those parts cover admin information, critical functions and infrastructure,
recovery strategy, backup and offsite storage, recovery procedures, roles, contact information and testing. It
is explicitly not named "Disaster Recovery Plan." California renamed it from "Disaster Recovery Documentation
for Agencies Preparation Instructions" (old SIMM 65A) in September 2013. Specifically, it did so to "change
\"disaster recovery\" to \"technology recovery,\"" a span that passed the recheck. The same document states:
"The TRP is just one portion of contingency planning and business continuity. A complete business continuity
plan includes emergency/disaster management, business resumption, and technology recovery plans." That span
also passed. The governing state policy clause, SAM 5325.1, independently confirms the containment direction:
"As a sub-set of a state agency or entity's Continuity Plan, the Technology Recovery Plan (TRP) is activated
immediately after a significant disruption or disaster." The same clause states the TRP "must be derived from
the state agency or entity's BIA and Continuity Plan." Both spans passed the recheck. Texas's state IT agency
ships no DR or BC template of any kind. Texas DOT's manual is prose guidance telling districts to write their
own plan, not a fill-in template.

**One quotation this spec deliberately does not use, and why.** AWS's whitepaper is widely cited for stating
that a disaster recovery plan should sit inside an organization's business continuity plan rather than stand
alone. That exact sentence failed the recheck against the live AWS page. So the claim appears here only in
paraphrase, never inside quotation marks, until it is re-verified against raw text.

**What this settles for the bundle.** The gap-fill reports that every source in this sweep that takes a position on
the DR-BCP relationship places disaster recovery inside or beneath business continuity. No source in the sweep
ships the two as co-equal, separately structured documents. That is exactly the shape the maintainer's settled
decision already assumes. That shape is one bundle, with the Business Continuity Plan as the primary document and a
disaster recovery section inside it. The research confirms the shape rather than deciding it.

**NIST's impact-tiered scaling and the UK's setting-specific annexes are resolved out of the size axis, at the
research stage, not left open.** NIST's own Information System Contingency Plan templates scale by impact tier
(low, moderate, high). At the high-impact tier, they add sections such as a Data Functionality Testing
subsection, rather than simply expanding prose within a fixed skeleton. The UK's HMPPS framework instead varies
by organizational setting: five distinct annexes for prisons, probation units, approved premises and others. It
does not vary by document size at all. Both are genuine scaling logics the sources support. Both are left out
of this bundle's lean-full size axis, per the maintainer's own resolution. Neither is mixed with the
Ready.gov-scaled, SIMM-structured logic this bundle actually uses.

#### Boundaries: four neighbours the research supports, one it does not

**`runbook`: a clean, already-shipped boundary.** The runbook template states the boundary in its own body,
not only its guide: a runbook is "NOT a disaster recovery plan". The full variant scopes that with NIST's own
definition. A runbook is one operational procedure that this plan's own Disaster Recovery section may call out
to. It is not a replacement for the plan, and the plan is not a bigger runbook.

**`production-readiness-review`: a clean, already-shipped deferral.** The PRR's own worked example defers
disaster recovery outright to "Platform's own standing responsibility, reviewed under Platform's own
instrument". It also marks the Readiness Criteria row Not Applicable on that ground. Landing this bundle gives
that instrument a template. Whether the PRR's companion or example changes to reflect that is a build decision,
not a required edit this spec makes.

**`incident-postmortem`: the temporal inverse, supported by the guide's own framing.** `incident-postmortem` is
written "after, not during," analyzing one event that already happened and already resolved. A business
continuity plan, with its disaster-recovery section, is written and tested before a disruption and activated
during one. The two cannot collapse into each other: one looks backward at a crystallized event, the other
looks forward to one that has not happened yet.

**`risk-register`: future risk versus a designed response to a crystallized risk.** The risk register's own
guide scopes it to "potential future events" and explicitly routes a problem that "has already happened" to an
issue log instead. A business continuity plan is the designed response once a tracked risk (or an untracked
one) actually crystallizes into a disruption. It does not duplicate the register's ongoing tracking of
uncertain events.

**`launch-coordination-checklist`: no boundary argument in the research, and none is invented here.**
Neither the admission sweep, the gap-fill, nor the family-fit research names a collision between this type and
the launch checklist. So this spec draws no boundary with it.

#### Family fit: `standing-standards` as a `tool`, the family's second unforecast member

**Membership.** A business continuity plan maintained and "tested via failover drills" (the catalog's own
phrase) is consulted at the moment of action. That is the same falsifier
[ADR 0053](decisions/0053-launch-coordination-checklist-joins-standing-standards-as-a-tool.md) applied to the
launch checklist. [ADR 0062](decisions/0062-production-readiness-review-joins-standing-standards-as-a-tool.md)
applied it to the production readiness review too: "if a candidate arrives that matches the cadence but is not
consulted at the moment of action, this family has been drawn around the axis rather than around a job"
(`standing-standards.md:108-110`). A plan written for one specific disruption, after the fact, would be an
incident report, excluded on the contract's own analogy at `standing-standards.md:37`. This bundle is the
standing plan, agreed once and consulted (and periodically rehearsed) whenever a disruption or a drill calls
for it.

**Classification: `tool`, on the same three-marker method ADR 0058 and ADR 0062 both applied.** ADR 0058
(definition-of-ready joins standing-standards as a foundation) reached `foundation` with that method, and ADR 0062
(production-readiness-review joins standing-standards as a tool) reached `tool`. The contract's cut is "is it a
standard you judge against, or an instrument you execute?" A business continuity plan's criteria (which functions
are critical, what the recovery strategy is) read as a standard a team might be judged against. That is the honest
`foundation` case. What breaks the parallel is when the plan is used: it is executed under time pressure once a
disruption is declared or a drill begins. That reading is this library's inference from the sources' activation,
recovery and testing content; no single source states it as a classification. NIST's ISCP sample templates carry a
yearly-test attestation line (a structural finding from reading the PDF, not rechecked as a quotation). The plan's
whole Disaster Recovery section describes steps run during an event. **The marker's second half is not cleanly
met.** The contract describes a `tool` as executed "often by someone who did not write it". No source in this sweep
says who activates a plan relative to who wrote it. A business continuity team may both write and run its own plan.
The `tool` call therefore rests on execution under time pressure and on the third marker, which says a tool's
authority comes "from being correct right now". It does not rest on the authorship half.

**This is the family's second member that no forecast named, after `production-readiness-review`.**
`standing-standards.md:46` names only "a coding-standards or engineering-handbook document" as a likely future
member, checked directly against the contract's current text. Neither a business continuity plan nor a disaster
recovery plan appears on that list. That follows
[ADR 0057](decisions/0057-issue-log-joins-governance-docs-as-a-fourth-member.md)'s principle, already applied to
this exact family by ADR 0062. The principle states: "The membership test, not the list of members that happened
to be planned in 2026-07, governs a candidate." So this does not weaken admission. It does mean this ADR, like ADR 0062 before
it, cannot claim a confirmed forecast.

**The cadence tension stays out of the contract, by design, and is handled in the Review Trigger section.**
`standing-standards.md` section 1 states members are "not revised on a calendar." NIST states the "ISCP should be
reviewed for accuracy and completeness at least annually." NIST also states "All ISCPs should be reviewed and
tested at the organization defined frequency (e.g. yearly)." Both passed the recheck. The FFIEC's superseded 2003
Business Continuity Planning booklet states "Testing the BCP at least annually." It was retrieved via an FDIC
mirror, because the current 2019 edition returned a 403 twice. That span also passed. Whether the 2019 edition
keeps this fixed interval or moves to risk-based language, as unverified secondary summaries suggest, is not
settled by this research. **That reads as a calendar cadence, against section 1's own phrase, and this spec does
not propose a contract amendment to resolve it.** Instead, the bundle's Review Trigger section, required by
contract section 4 of every member, states the trigger as a condition rather than a date. Candidate conditions
include a failed test or drill finding, or an actual activation. A third condition is a change named in the FFIEC's
own language: "any changes to key personnel, policies, procedures, facilities, equipment, outsourcing
relationships, vendors, or other components that impact a critical business function." That span also passed the
recheck. The annual exercise is this plan's own named condition restated as a minimum frequency, not a calendar
rewrite of the document. ADR 0071 records the tension as a consequence of admitting this member, as ADR 0062
recorded the honest `foundation` case for the production readiness review. It does not resolve the tension by
widening the contract.

#### Section design

Drawn from the Ready.gov template's own scale for lean and the maintainer's settled model for full. No source
gives one single canonical section list for a merged "DR/BC plan." So the groupings below are this library's
own judgment, sourced per row rather than copied whole from any one document.

| Section | In lean? | What it is |
|---|---|---|
| **Purpose and Scope** | yes | What counts as a disruption here, and what business this plan covers. Sourced to Ready.gov's Program Administration block, the opening section of its four-page template |
| **Business Continuity Team and Roles** | yes | A named team roster and a line of succession, so the plan does not depend on who is reachable. Sourced to Ready.gov's Business Continuity Organization block, which ships a five-column team roster table |
| **Business Impact Analysis Summary** | yes | The critical business processes this plan protects, and their Recovery Time Objectives, drawn from a Business Impact Analysis done separately rather than re-templated here. Sourced to Ready.gov's own prompt, "Identify Recovery Time Objectives for business processes and information technology" (passed the recheck). Also sourced to NIST's and FFIEC's own treatment of the BIA as the plan's upstream input, not the plan itself |
| **Continuity Strategies and Manual Workarounds** | yes | How critical processes keep running without full systems, and what the chosen recovery strategy is at the business-process level. Sourced to Ready.gov's Manual Workarounds and Business Continuity Strategies & Requirements blocks |
| **Activation and Incident Management** | yes | What declares a disruption, who declares it, and the first procedures that follow declaration. Sourced to Ready.gov's Incident Management block and, structurally, to NIST SP 800-34 Appendix A's own "Activation and Notification" section. That section is read directly from its table of contents, not quoted, since this is a structural finding rather than a span to recheck |
| **Training, Testing and Exercising** | yes | The exercise schedule and what a drill actually validates. Sourced to Ready.gov's own Training, Testing & Exercising block. Also sourced to the FFIEC's "Management should ensure recovery testing is conducted at least annually," which passed the recheck. Its warning that "Unmanned recovery testing, where back-up tapes are sent to the recovery site to be run by service provider employees, is not a sufficient test," also passed |
| **Plan Administration** | yes | Vendor and contractor contacts, a revision history, and plan distribution and access. This is a library grouping of Ready.gov's three smaller blocks: a vendor and contractor table, a revision history table, and plan distribution guidance. None of those three is large enough on its own to carry a section. This library labels them here as its own combination, rather than any one source's structure |
| **Disaster Recovery** | **full only** | The maintainer's settled model is a disaster-recovery section inside the plan, structured on California SIMM 5325-A. It covers critical functions and infrastructure, recovery strategy, backup and offsite procedures, recovery procedures, roles, contacts, and testing. SIMM 5325-A's own structure, read directly and raw-checked, runs fourteen numbered subsections across two parts. The seven groupings above are this library's own collapsing of that structure into fewer, broader headings. They are sourced to the same document, rather than to any further source that groups them this way |
| **Review Trigger** | yes | **Contract-mandated** (section 4): a named owner and a condition, not a calendar. Candidate conditions, sourced: a failed test or drill finding; an actual activation; or a change to "key personnel, policies, procedures, facilities, equipment, outsourcing relationships, vendors, or other components that impact a critical business function." That span is from the FFIEC, and it passed the recheck. The annual exercise cadence NIST and the FFIEC both name is this section's own stated condition, restated as a floor. That is not a calendar rewrite of the document, per the family-fit discussion above |

The lean variant's eight sections, in this order, are a strict ordered subset of the full variant's nine, as
contract section 3.2 requires. Full inserts exactly one section, Disaster Recovery, immediately before Review
Trigger.

#### Catalog corrections the landing PR must make

Per [decision-procedures.md procedure 1](decision-procedures.md#1-a-catalog-call-loses-to-research), both
`docs/internal/catalog.md` and `atlas/catalog-data.json`, then regenerate the atlas:

1. **Aliases: correct the synonym framing, sourced.** The catalog currently lists "DR plan," "BCP" and "RPO/RTO
   doc" as if they name one interchangeable thing. The gap-fill reports that every source in the sweep that
   takes a position treats a disaster recovery plan and a business continuity plan as related by containment,
   not as synonyms. NIST SP 800-34's two definitions also scope a DRP more narrowly than a BCP. A DRP
   is narrower and site-relocation-bound. A BCP is the broader mission-sustaining document the DRP (or, in
   California's current naming, the Technology Recovery Plan) sits inside. Keep "DR plan" and "BCP" as aliases
   a reader might actually type, since both are real search terms for this one document. But the catalog's own
   `summary` or a state note should say plainly that the two name a containment relationship. They are not two
   names for the same document. This spec's companion must say the same thing.
2. **Aliases: add three, one sourced and two the library's own.** "Disaster recovery plan" is NIST's own term,
   the fuller form that "DR plan" abbreviates. "Business continuity and disaster recovery plan" and "BC/DR plan"
   appear in no source this sweep read. They are this library's choice, approved by the maintainer on
   2026-10-13, so that a reader who types either phrasing still finds the bundle.
3. **Relationships: append this type to both neighbours that already route to it.** Both fields already name
   other neighbours: `runbook`'s reads `["Production Readiness Review"]`, and `production-readiness-review`'s
   reads `["Launch Coordination Checklist", "Runbook"]`. Append "Disaster Recovery / Business Continuity Plan"
   to each, in the display-name form those fields use, rather than replacing either list. This type's own
   `relationships` field, `[]` today, gains "Runbook" and "Production Readiness Review" in return.
4. **The category discrepancy between the two machine artifacts is flagged, not resolved here.**
   `docs/internal/catalog.md:199` reads "operations/governance"; `atlas/catalog-data.json` index 134 reads
   "Operations / Incident". This spec does not adjudicate which is correct. The landing PR should reconcile
   them, or record why one wins, rather than silently picking one the way the research found it already had
   been.
5. **Methodology: `ITIL/SOC2` has no supporting source.** The admission sweep's critic pass for this candidate
   reports that no research dimension found a named ITIL or SOC2 source publishing this document type. Neither
   name appears among the qualifying or corroborating sources. The landing PR replaces the value with one the
   admitting sources support (NIST SP 800-34 and FEMA's Ready Business program). The contract's
   methodology row is descriptive and not gated, so the choice is the build's, recorded in the meta.

#### `pairs_with`: checked, empty

`gh api repos/product-on-purpose/pm-skills/contents/skills --jq '.[].name'` returned all 68 skill names on
2026-10-13. No name contains "disaster," "continuity," "recovery," "bcp" or "dr-" against this type. The
plausibly adjacent names, `foundation-build-risk-review` and `tool-design-sprint-readiness` /
`tool-foundation-sprint-readiness`, are a build-stage risk review and design/foundation-sprint precondition
checks, unrelated in subject. **`pairs_with: []`**, under the contract's rule for that field: "Verify per
member; claim only what is true of that member" (`standing-standards.md:74`).

#### Risks for the build and review

1. **The one-document-or-two finding is the central risk, and the companion must not round it up.** The
   business continuity half of this bundle admits decisively; the disaster-recovery half admits only
   definitionally. A companion that writes as if both halves cleared admission at the same strength
   overstates the weaker one. State it exactly as the admission section above does: definitional for DRP,
   template-grade for BCP.
2. **The AWS sentence about a DR plan not standing alone from the BCP is a live temptation.** It is the single
   most quotable, most on-point sentence for this bundle's own central argument, and it failed the recheck.
   Carrying it into the companion inside quotation marks, under any paraphrase that keeps the quotation marks,
   fails review on a citation this sweep already flagged.
3. **The SANS quotation needs its provenance carried through, not dropped at the companion stage.** "The
   Disaster Recovery Plan is often part of the Business Continuity Plan" is this bundle's most load-bearing
   single sentence for the one-document decision. It passed the recheck against a SANS-hosted CDN copy of a
   2014 policy template, and the canonical SANS page now returns 404. A companion must cite the CDN copy and say
   the live page is gone, rather than cite the dead URL.
4. **ISO 22301 and ISO/IEC 27031 are not available to cite at any depth.** Both standards are paywalled and were
   never read in either the admission sweep or the gap-fill. Any companion sentence
   about their clause structure must either go unwritten, or be labeled secondary and unverified.
5. **This is the family's second unforecast member, and the cadence tension is a real, recorded consequence,
   not a footnote.** A reviewer who expects every standing-standards member to match a contract forecast, the
   way `launch-coordination-checklist` and `definition-of-ready` did, will not find one here. ADR 0062 already
   set the precedent that the membership test, not the forecast list, governs. The cadence tension is real,
   and ADR 0071 records it as a consequence. That tension is NIST's and the FFIEC's "at least annually" against
   section 1's "not revised on a calendar". A companion or guide that asserts the tension is fully resolved,
   rather than handled by the Review Trigger section's own condition framing, overclaims.
6. **The build workflow's templates stage has repeatedly copied the worked example's own scenario into the
   template's GOOD and WEAK text.** Once an example exists, grep the drafted templates for its proper nouns
   before review. That is the same practice `production-readiness-review`'s own spec names, and the
   north-star-metrics spec repeats it.
7. **The Business Impact Analysis is an upstream input this bundle must not re-template.** NIST and the FFIEC
   both treat the BIA as a separate analysis artifact that feeds a plan's priorities and RTOs. The Business
   Impact Analysis Summary section carries the BIA's output, a few load-bearing figures, not a full BIA
   worksheet.

#### The worked example: a scenario chained onto facts that already exist

**This must not be the Saved Views Sharing launch, the entitlement-audit runbook's own incident, or the SRE
ownership handoff the production-readiness-review example already covers.** Each of those is already a
different document's own scenario; reusing one collapses this example into a sibling's.

**The proposed hook: the instrument the production-readiness-review example names but does not show.**
`production-readiness-review_example.md:85` states that "Backup and disaster recovery for that database is
Platform's own standing responsibility, reviewed under Platform's own instrument". It names `saved_view` and
every other dashboard-service row as living "in the shared main Postgres database", which Platform, not
Reporting, owns. This bundle's worked example can be that instrument: a business continuity plan owned by Acme
Analytics' Platform team. It covers the shared Postgres database and the other infrastructure Platform's
services depend on, and its disaster-recovery section is scoped to that database's alternate-site recovery.

**Chronology: the plan already exists on 2026-08-22.** The PRR example is dated 2026-08-22 and refers to
Platform's own instrument in the present tense, so that instrument must exist by then. The example may show a
later revision, but its revision history must then include an entry on or before 2026-08-22. It must not say
the PRR found no plan, because the PRR example says the opposite. The exact dates are a build decision.

**People: reuse the thread's named roles, in the roles the examples already give them.** Dana Osei (Staff
Engineer, Platform) is the natural owner of a Platform-scoped continuity plan, since Platform owns the shared
database per the PRR example. Ines Halvorsen (Engineer, the new SRE function), the PRR's decision authority,
is a plausible reviewer. That review asked SRE to take standing ownership of a service that depends on
Platform's infrastructure.

**Content it may cite, without restating any sibling's own table rows.** The plan may cite that
dashboard-service and other services share Platform's Postgres database
(`production-readiness-review_example.md:85`). It must not restate the PRR's own Readiness Criteria rows, the
runbook's own entitlement-audit procedure, or any risk-register row. A continuity plan for the database asks a different set of questions:
recovery strategy, offsite backup, activation criteria for the database specifically. Those are not questions
any of those three documents already answer.

**What it must not do.** It must not resolve the chain's own open build-number contradiction (see the
production-readiness-review spec's own note on this). It should cite no build or release number at all, the
same convention that spec settled on, referring only to dated events.

#### Metadata

| Field | Value | Why |
|---|---|---|
| `family` | `standing-standards` | Maintainer ruling, 2026-10-13; argued in ADR 0071 |
| `classification` | `tool` | Maintainer ruling, argued marker-by-marker in ADR 0071 against `standing-standards.md` section 2's cut, on the same reasoning ADR 0062 used for the production readiness review |
| `bundle_id` | `business-continuity-plan` | Maintainer's ruling, 2026-10-13. The catalog id stays `disaster-recovery-business-continuity-plan`; `north-star-metrics` already kept a bundle id distinct from its catalog id (`north-star-metric-definition`), so this is not a new pattern |
| `sizes_available` | `[lean, full]` | The maintainer's settled sizing: lean at Ready.gov's own four-page scale, full adding the SIMM-modeled Disaster Recovery section |
| `status` | `beta` | Every bundle |
| `methodology` | Set at build from the admitting sources' lineage | The catalog's `ITIL/SOC2` has no supporting source (catalog correction 5). The contract's methodology row is descriptive, not gated |
| `pairs_with` | `[]` | Checked against pm-skills `origin/main`, 2026-10-13; no skill produces or consumes this type |
| `related_templates` | `[runbook, production-readiness-review]`, inline | The two neighbours with an existing, unresolved forward-reference to this type. `incident-postmortem` and `risk-register` are named boundaries in the companion, but they carry no existing forward-reference to correct |
| `aliases` | `disaster recovery plan`, `DR plan`, `BCP`, `business continuity and disaster recovery plan`, `BC/DR plan` | See catalog corrections 1 and 2 above. The last two are the library's own, for search, and no source uses them. The companion states the containment relationship rather than treating any pair as synonyms |

#### What landing this bundle closes elsewhere

1. **The `standing-standards` contract's Members line**, from "not yet built" to the build date. The contract
   moves to `0.5.0` in the spec PR, with ADR 0071.
2. **`runbook`'s and `production-readiness-review`'s own forward-references become resolvable.** Neither
   bundle's companion is required to change by this landing. Whether either gains a direct link to the new
   bundle is a build decision. That is the same stance ADR 0062 took toward `launch-coordination-checklist`.
3. **The catalog entry**, per the corrections above, in both `docs/internal/catalog.md` and
   `atlas/catalog-data.json`, then the atlas regenerated.
4. **This page's Progress table.**
5. **Issue #263 (bundle: disaster-recovery-business-continuity-plan)** closes with the build PR.

#### What the build would cost

No build has run for this type. This is projected from the family's own three most recent built members, all
with every agent resolved to Sonnet. `production-readiness-review` cost $15.75 whole (15 build agents),
`launch-coordination-checklist` cost $14.22 whole (15 build agents), and `definition-of-ready` cost $11.69
whole (15 build agents). All are measured figures from `bundle-builds/INDEX.md`. A whole-bundle estimate of
**$12 to $16 at API list rates** is reasonable on that basis. It is a projection, not a measurement, until
`python tools/gen-bundle-build-report.py --ingest` runs against an actual build report.

### decision-docs (fifth member): the trade study, in the technical sense the business-case guide already names

**trade-study** (bundle id; the catalog id stays `trade-study-options-analysis`, as `north-star-metrics` kept
`north-star-metric-definition` and `business-continuity-plan` kept `disaster-recovery-business-continuity-plan`)
- `decision-docs`, **phase develop**, sizes **`[lean, full]`**, methodology recommended **`generic`** (see
Metadata below), catalog id `trade-study-options-analysis` (atlas index 65, catalog_ref 66) / `catalog.md` row
66. Catalog owner: "Architect / BA" (flagged below as unsourced). Catalog purpose: "Evaluate options against
weighted criteria." Issue #259 (bundle: trade-study-options-analysis) tracks this build.

This spec follows the model the maintainer named: the `spike-report` spec (the `decision-docs`
fourth-member section on this page), the family's first
Tier-2 candidate and the only other member admitted under ADR 0022 (adopt the decision-docs family
contract)'s fourth-member clause with no contract edit. It also carries forward the two conventions the
`business-continuity-plan` spec added most recently: a Demand subsection built from prose routing rather than
a `future:` tag, and a sourced Section design table.

#### Demand: no promise tag, and no sibling currently points here at all

A grep of every `templates/*/*_meta.yaml` for a `future:` promise tag naming a trade study or an options
analysis returned nothing. A broader grep of the same files for any live `future:` tag also returned
nothing: no `_meta.yaml` file currently carries one. This spec does not claim to have checked every
tag that was ever retired. It checks only the tags this reading list and this file's own history name:
`future:spike-report`, `future:solution-brief`, `future:design-doc`, `future:rfc`,
`future:technical-design-doc`, and the `launch-coordination-checklist` fix. All of those are accounted for.
ADR 0053 (launch-coordination-checklist joins standing-standards as a tool) corrected that last one to
`future:launch-coordination-checklist` before that bundle was built. So, unlike `launch-coordination-checklist`,
there is no stale tag to correct here, and unlike `business-continuity-plan`, there is no tag to point at in
the first place.

**Unlike `business-continuity-plan`'s demand section, no sibling bundle's `related_templates` field or
`relationships` catalog field currently names this type either.** `adr_meta.yaml`'s `related_templates` reads
`[rfc, sdd, spike-report]`; `rfc_meta.yaml` reads `[adr, sdd]`; `sdd_meta.yaml` reads `[rfc, adr, prd]`;
`business-case_meta.yaml` reads `[product-vision, product-strategy, product-roadmap]`. None lists a trade
study. The demand here is prose, not a field. `business-case_guide.md`'s own routing table sends a reader here by
name. So does `business-case_companion.md` section 8, and both `business-case` templates' own "WHAT A
BUSINESS CASE IS, AND IS NOT" block. `business-case_guide.md:19` reads in full: "you are comparing
technical approaches against weighted criteria, not comparing whether to invest at all. A trade study's output
feeds into Options Considered as one input, it does not replace the case". `business-case_template-lean.md:33-34`
carries the same boundary inside the template body itself, not only the guide: "NOT a trade study (a bounded
technical comparison whose output feeds Options Considered as one input)". `business-case_template-full.md:38-39`
carries it in the full variant, with "an input" in place of "one input". This is the same shape `business-continuity-plan`'s own demand section described for `runbook` and
`production-readiness-review`: real routing, already shipped, that no gate enforces. ADR 0041 (the
maintainer's preference sets the build order) governs when, not whether, that routing gets a bundle.

#### Admission: two independently verified sources, GAO named as a neighbour only

**NASA's Systems Engineering Handbook and the Federal Highway Administration's Systems Engineering for ITS
both independently clear ADR 0030 (templating scope: a named source must publish the type as a written
document)'s bar**, and the bar needs only one. ADR 0048 (one named source clears the admission test) already
settled that a single qualifying source is sufficient; this candidate clears on two.

NASA's Systems Engineering Handbook (SP-2016-6105 Rev 2) states in its own Glossary: "A report written to
document a trade study." The same source adds that "the report may be a simple white paper or a more
formally formatted document," which is the sizing evidence used below. Its Section 6.8 names a template,
headed "Typical Information to Capture in a Decision Report," for the document a trade study produces. All
three spans passed the 2026-10-12 recheck against the raw NASA PDF.

The Federal Highway Administration's Systems Engineering for ITS, section 3.4.5, independently states:
"Select and document the preferred candidate, typically using a trade study matrix that lists the alternatives
on one axis." The same section states that the alternatives are compared on the basis that the evaluator should
"compare the relative merits of alternative approaches," and that the result is a "repository of alternatives"
for stakeholders. It also states that "Sensitivity analysis may also be used, especially with simulation," and
names "Do Nothing" as one of the alternatives a trade study weighs. All of these spans passed the same
recheck.

**GAO's Cost Estimating and Assessment Guide (GAO-20-195G) is a neighbour, not an admitting source, by this
spec's own ruling.** Its quotations were checked in this recheck against the primary `gao.gov` PDF. Every
span returned HTTP 403. No Department of Energy mirror URL survives in this sweep's recorded output for this
spec to cite. So GAO's content appears here only in paraphrase, never inside quotation marks. GAO's guide
describes an Analysis of Alternatives process whose output is typically a single final report. That report,
per GAO, covers roughly ten named content elements, including a sensitivity analysis and the results of an
independent review. Those two paraphrased elements corroborate the Full-size additions below, but do not
themselves admit them. Admission does not depend on GAO at all; two sources already independently clear the
bar.

#### Family fit: the ADR 0022 route, and why no new record is needed

**Settled by the maintainer (decision 5 of the 2026-10-13 sitting): `decision-docs`, no contract change.**
The contract's section 1 states that the "family's three roles are distinct and complementary," which read
alone suggests a fourth role is a problem. ADR 0022 (adopt the decision-docs family contract) answers that
reading directly. Its Consequences state: "a
fourth (a spike report, a solution brief) would join under the same contract with no contract change unless
it declares a different phase or size shape." `spike-report` already joined on exactly that clause, and its
own spec in `tier2-specs.md` carries the warning this spec repeats rather than relearns: "Read the contract
and the ADR together or not at all."

**This bundle declares neither a different phase nor a different size shape.** `phase: develop` matches
`adr`, `rfc`, `sdd` and `spike-report`. `sizes_available: [lean, full]` matches `adr`, `rfc` and `sdd`
exactly (`spike-report` is the family's one single-size exception, for its own sourced reason). So the
ADR 0022 clause applies on the same terms it applied to `spike-report`. This spec recommends no ADR and no
contract edit. The precedent already set is not a one-time exception; it is a route this contract now
supports twice.

**The precedent is verifiable in the contract file itself, not only in a secondary account of it.**
`decision-docs.md` still reads, at the top of the file: "Members at adoption: rfc, adr, sdd". That line was
never updated when `spike-report` joined, and this spec finds no reason it should be updated now. The
contract's own Version line still reads 0.1.0, unchanged since the 2026-07-21 adoption.

**The contract file's history agrees.** Three commits have touched `decision-docs.md`: the 2026-07-21
adoption (`2a2a5fe2`, ADR 0022), a 2026-09-21 rewrite of its status row (`722036be`, ADR 0055, retire the
zero-fills disclosure) that left no change-note entry, and a 2026-10-12 wording clarification (`e1c5b2a1`)
whose entry states: "No version moves, because no obligation changed." None of the three moved the version,
and none concerned membership.

**Two kinds of record, kept apart.** `spike-report` carries ADR 0048 (one named source clears the admission
test), but that record settled its **admission** under ADR 0030, which was genuinely contested: exactly one
source qualified, and the term's own inventors describe a spike's output as throwaway code. It is not a
family-placement record. No member admitted under the ADR 0022 clause carries
a family-placement record, because the clause applies itself. This candidate needs neither kind: its
admission rests on two read sources, so no ADR 0030 ruling is in question, and its placement uses the same
clause `spike-report`'s did.

**Open question, not resolved here.** Two members, `spike-report` and now this one if built, will have
joined `decision-docs` through the ADR 0022 clause, with no family-placement record and no version move.
Whether that stays legible to a future reader once a third such candidate arrives is a judgment this spec
does not make. It is named so the maintainer can decide, rather than let the same pattern repeat by default.

#### Boundaries: adr, rfc, sdd, spike-report, business-case

**`adr` records a decision; this type evaluates the options a decision will be made from.** `adr_companion.md`
describes its Considered Options section as "The alternatives, by title," a prose list with no weighting or
score. A trade study that produces a clear winner may still need an ADR written from it. That mirrors the
relationship the contract already draws between a spike's findings and the ADR that follows. The evaluation
and the record of the decision are not the same document, even when one leads directly to the other.

**`rfc` proposes a decision and asks for feedback; its own Alternatives Considered section is argued prose,
not a scored comparison.** `rfc_companion.md` describes it as "The options you genuinely weighed and why you
are not proposing them, including \"do nothing.\"" The trade study and the RFC can both carry a do-nothing
option, but the trade study's job is the weighted-criteria mechanism itself; an RFC that wants that mechanism
can cite a trade study's output rather than rebuild it in prose.

**`sdd` describes a design; its own Alternatives Considered section is the same prose shape as the RFC's.**
`sdd_companion.md` describes it as "The other designs you genuinely weighed and why you are not proposing
them, including \"do nothing\" or \"the obvious approach\" where those are real options." Where a design
decision is complex enough to need weighted criteria and a scoring matrix rather than an argued paragraph,
the trade study is the document built for that, and the SDD can cite it the way it already cites an ADR for
a significant decision.

**`spike-report` investigates an open question; a trade study scores options that are already named.** The
`spike-report` spec in `tier2-specs.md` describes the family's fourth role, before this one, as a type that
"investigates the question that precedes all three, and hands over evidence plus a proceed-or-not
recommendation." A trade study starts further along: the alternatives are already identified, and the job is
to weigh them against criteria rather than to reduce an unknown. A spike's findings can be one input a later
trade study's criteria or scoring draws on, the same relationship the spike's own spec already draws toward
the ADR that follows it.

**`business-case` is the type that names this one, and explicitly does not do its job.** Covered fully under
Demand above. The boundary is drawn cleanly on both sides: `business-case_companion.md` section 8 states "It
is not a trade study: trade studies are bounded technical comparisons," and this spec's own admission section
above shows the trade study does not do the business case's job either, because it evaluates technical
approaches rather than an investment decision.

#### Section design

Five sections if lean, nine if full, in the order below. Lean's five are a strict ordered subset of full's
nine, as contract section 3.2 requires. Full inserts two sections, Sensitivity Analysis and Risk and
Benefit, before Recommendation, and two more, Dissent or Independent Review and References, after it. The
Risk-and-Benefit-before and Dissent-and-References-after placement follows NASA's own Decision Report order
structurally: NASA's named sections run Risk/Benefits before its recommendation section, and Dissent and
References after. NASA's own template has no sensitivity section at all; placing Sensitivity Analysis beside
Risk and Benefit, also before Recommendation, is this library's own placement, not a structural match to any
one source, since FHWA names the section but gives it no position relative to a recommendation. This table
keeps NASA's relative placement for the three sections NASA does order, rather than grouping all four
full-only sections on one side of Recommendation.

**NASA's Table 6.8-1 is the nearest canonical list, and this design departs from it on purpose.** Per the
research summary of that table (its section names were not themselves raw-checked), NASA's Decision Report
runs: Executive Summary; Problem/Issue Description; Decision Matrix Setup Rationale; Decision Matrix Scoring
Rationale; Final Decision Matrix; Risk/Benefits; Recommendation and/or Final Decision; Dissent; References;
Appendices. This design drops the Executive Summary and the Appendices. It splits the matrix setup into
Criteria and Weights and a separate Alternatives section, so that the do-nothing baseline FHWA names has its
own place. It folds the scoring rationale and the final matrix into one Scoring Matrix section. It adds
Sensitivity Analysis, which NASA's table does not carry and FHWA does name. Each row below gives its source,
on the pattern `business-continuity-plan`'s own Section design table used.

The catalog's own `typical_sections` field reads "options, criteria, weights, scores, recommendation." That
corroborates this shape. It does not name Problem and Decision Framing on its own, but options maps to
Alternatives, criteria and weights map to Criteria and Weights, scores maps to the Scoring Matrix, and
recommendation maps to Recommendation. No catalog correction follows from this; it is a consistency check,
not a conflict.

| Section | In lean? | What it is |
|---|---|---|
| **Problem and Decision Framing** | yes | The decision this trade study exists to inform, and who is waiting on it. Sourced structurally to NASA's own Decision Report template, whose Problem/Issue Description follows an Executive Summary this bundle does not carry, and to FHWA's framing of a trade study as comparing approaches against a named decision |
| **Criteria and Weights** | yes | The named criteria the options will be scored against, and the weight each one carries. Sourced to FHWA's statement that evaluations are merged using weighting factors, and structurally to NASA's own named matrix-setup section, which this library does not quote directly because the section name itself was not part of the recheck-verified spans |
| **Alternatives, Including a Mandatory Do-Nothing Baseline** | yes | Every option genuinely considered, with a named do-nothing or do-minimum option that cannot be dropped even if it is rejected in one line. Sourced to FHWA's own named "Do Nothing" alternative and its description of the matrix as a "repository of alternatives" |
| **Scoring Matrix** | yes | The completed weighted comparison, one row per criterion, one column per option. Sourced to FHWA's instruction to "compare the relative merits of alternative approaches," and structurally to NASA's own final decision-matrix section |
| **Sensitivity Analysis** | **full only** | How much a criterion's weight would have to move before the recommendation changes. Sourced to FHWA's statement that "Sensitivity analysis may also be used, especially with simulation." GAO's guide independently names sensitivity analysis among its required content elements. That is named here as a corroborating neighbour, paraphrased rather than quoted, because its spans did not pass this sweep's recheck |
| **Risk and Benefit** | **full only** | The risk and benefit profile of the recommended option, named separately from the scoring criteria that produced it. Sourced structurally to NASA's own Risk/Benefits section, which NASA places before its recommendation section. GAO's guide independently names risk drivers among its required content elements, named here as a corroborating neighbour, paraphrased rather than quoted |
| **Recommendation** | yes | The option the matrix selects, and the reasoning that depends on specific rows above it rather than restating the whole comparison. Sourced to FHWA's instruction to "Select and document the preferred candidate, typically using a trade study matrix" |
| **Dissent or Independent Review** | **full only** | A named place for a reviewer who disagreed with the recommendation, or for an independent check on the scoring itself. Sourced structurally to NASA's own named Dissent row, which NASA places after its recommendation section. GAO's guide independently requires documenting the results of an independent review, named here as a corroborating neighbour, paraphrased rather than quoted |
| **References** | **full only** | The sources the criteria, weights and scores actually rest on. Sourced structurally to NASA's own References section, the template's last section |

#### Catalog corrections the landing PR must make

Per [decision-procedures.md procedure 1](decision-procedures.md#1-a-catalog-call-loses-to-research), both
`docs/internal/catalog.md` and `atlas/catalog-data.json`, then regenerate the atlas:

1. **`size_variant`: "M" becomes lean and full.** The maintainer's settled sizing, drawn from NASA's own
   statement that the report "may be a simple white paper or a more formally formatted document," and from
   GAO's and NASA's further content (sensitivity, risk and benefit, dissent or independent review, references)
   that supports a heavier second weight.
2. **`relationships`: add RFC and SDD, in both files.** `atlas/catalog-data.json`'s `relationships` list
   currently reads `["ADR", "Business Case"]`; `docs/internal/catalog.md` row 66's own relationships cell
   reads the prose "feeds ADR/Business Case." Both RFC and SDD carry their own prose Alternatives Considered
   section, the shape this type's scored mechanism is the sourced alternative to, so both belong on this list
   the way ADR and Business Case already do. Corrected atlas value: `["ADR", "RFC", "SDD", "Business Case"]`.
   Corrected catalog.md prose (this spec's own proposed wording, not a quotation): `feeds ADR/RFC/SDD/Business Case`.
3. **`owner`: "Architect / BA" is unsourced.** No admitting source in this sweep names a role for who writes
   or owns a trade study. This spec does not invent a replacement; it flags the field as an unverified
   attribution for the landing build to decide, the same posture the research itself took.
4. **The `notes` column's citation, "BABOK 10.16 decision analysis," was never fetched and should not be
   cited as support.** No research pass in this sweep or the 2026-10-12 admission sweep read BABOK's content.
   The landing PR should either remove that citation or replace it with the two sources this spec actually
   verifies: NASA SP-2016-6105 Rev 2 and FHWA's Systems Engineering for ITS, section 3.4.5.
5. **Aliases: do not add `analysis of alternatives`.** That exact phrase names the investment sense in GAO's
   and wider US defense-acquisition usage, the sense this spec and the maintainer's own ruling both exclude
   from this bundle on purpose. Adding it as an alias would route a reader searching for GAO's Analysis of
   Alternatives, or HM Treasury's Green Book options appraisal, to a document that explicitly does not cover
   that ground. The catalog's existing aliases ("trade-off analysis," "decision analysis," "weighted scoring
   matrix") stay as they are; none of them carries the same investment-sense pull.
6. **Aliases: a misplacement worth a maintainer check, not resolved here.** The alias "decision matrix" is
   currently assigned to the unbuilt Decision Log candidate (`decision-log`, atlas index 64, catalog_ref 65),
   not to this type.
   Both sources checked here, NASA (its Final Decision Matrix) and FHWA (its trade study matrix), tie a
   scoring matrix to a trade study, not to a decision log. This spec does not move the
   alias; it names the discrepancy the way `business-continuity-plan`'s spec named its own catalog category
   discrepancy, for the maintainer to adjudicate.
7. **`stage`: checked, and this is not a discrepancy.** `catalog.md`'s row reads "decision/feasibility" in the
   stage column; `atlas/catalog-data.json`'s entry reads `"stage": "decision"`, the first of the two slashed
   terms. `atlas/catalog-data.json`'s own top-level `stages` list is a controlled vocabulary of single
   values, and "decision/feasibility" is not one of them. The same pattern holds for catalog entry 54
   (Interactive Prototype), whose `catalog.md` stage reads "design/validation" and whose atlas entry reads
   `"stage": "design"`, the first term again. `gen-atlas.py`'s own header states that `stage` is
   hand-maintained, not generated from `catalog.md`. So this is not a code-enforced rule. But the same
   first-term convention appears at both rows checked, which argues for an existing convention rather than
   drift specific to this type. No correction follows.
8. **`when_used`, `formality`, `rarity`: checked, no evidence either way.** `when_used` ("major decisions"),
   `formality` ("standard") and `rarity` ("occasional") are not contradicted by anything NASA, FHWA or GAO
   state, and nothing in this sweep supports a more specific claim about any of the three. They are left
   unchanged, as a checked field rather than an unchecked one.
9. **`methodology`: the catalog's "methodology-agnostic" supports `generic` in the meta, not a change to the
   catalog itself.** See Metadata below.

#### `pairs_with`: checked, empty

`tools/known-skills.txt`, the pinned list of pm-skills skill ids this gate checks `pairs_with` against,
carries no entry containing "trade," "options," "analysis," or "decision" in a way that names this type.
A grep of the full 97-line pinned list for those terms returned nothing relevant. **`pairs_with: []`**,
under the same rule `business-continuity-plan`'s spec applied: verify per member, claim only what is true of
that member.

#### Risks for the build and review

1. **GAO is the single most quotable neighbour for this bundle's own argument, and it is exactly the source
   this spec excludes from quotation.** GAO's framing of the AoA team as the party that documents the whole
   process in one place is the cleanest one-sentence statement of why a trade study's output is a document
   at all, and its quotations failed this sweep's recheck against the primary `gao.gov` URL. Carrying any of
   its sentences into the companion inside quotation marks repeats a citation defect this sweep already
   flagged, even under a paraphrase that keeps the quotation marks. Paraphrase it.
2. **The technical-sense boundary against `business-case` is the central argument this bundle has to teach,
   and it must not be rounded up on either side.** This spec's own Boundaries section shows the boundary
   drawn cleanly by sources on both documents' own existing text. A companion that treats the boundary as
   settled by this library's own prior sentence alone, rather than by NASA's and FHWA's independent technical
   framing, overstates how externally grounded the line is.
3. **Four cross-references, not three.** Contract section 4 requires each member's companion to place itself
   correctly against the other members. With a fourth member already admitted (`spike-report`) and this as
   the fifth, this bundle's companion must place itself against `adr`, `rfc`, `sdd` and `spike-report`, not
   only the original three. `spike-report`'s own guide and example both already place it against all three
   original members; this spec has not read `spike-report`'s own companion file directly, so it names the
   pattern its guide and example show, not that file, as the precedent.
4. **The example-independence rule applies, and the scenario proposed below has not been cross-checked for
   proper nouns.** Contract section 4, the distinct-jobs rule, requires decision-docs examples to be
   deliberately independent, each a different real decision, and `tools/check-example-independence.py`
   enforces it. **Correction to a number the `spike-report` spec itself carries wrong**: that spec's own
   "Two things landing this bundle would close elsewhere" subsection cites "Contract section 5" for this same
   rule. Section 5 is the shareable-boundary rule; the distinct-jobs rule, which is what both specs actually
   mean, is section 4. This spec cites it correctly and flags the inbound error rather than repeating it. The
   build workflow's
   templates stage has repeatedly copied a worked example's own scenario into the template's GOOD and WEAK
   text in other bundles; once an example exists for this one, grep the drafted templates for its proper nouns
   before review, the same practice `production-readiness-review`'s and `business-continuity-plan`'s specs
   both name.
5. **The `size_variant` correction is uncontested here but not yet applied anywhere else the catalog repeats
   it.** `docs/internal/buildout-specs.md` or any other spec sheet that still quotes `size_variant: M` for this
   type should be checked and corrected in the same change, per decision-procedures.md procedure 1's own
   instruction to correct every copy.

#### The worked example: an independent scenario, not a chain onto a sibling's

**Contract section 4, the distinct-jobs rule, requires decision-docs examples to be deliberately independent,
each a different real decision, because the family's teaching value is the distinction between roles, not
one thread.**
`spike-report`'s own example already demonstrates this at the family level: it is set at a fictional company,
Riverland Sensing, built specifically so it does not chain onto the Acme Analytics scenario the `adr`, `rfc`
and `sdd` examples share. This spec follows the same rule and proposes a scenario independent of all four
existing members, Acme Analytics and Riverland Sensing both.

**Proposed scenario (this spec's own proposal, not drawn from any source): a fictional logistics company,
working name Thornwell Freight, choosing a message-ingestion technology for GPS telemetry from its truck
fleet.** The decision: replace or keep the current nightly batch upload of GPS pings as flat files, against
three live alternatives (a self-managed Kafka cluster, a managed streaming service, and a third broker). The
mandatory do-nothing baseline is keeping the current nightly batch, named and scored rather than silently
dropped, on the same evidence FHWA names for keeping a do-nothing option in the matrix. Criteria would plausibly
include data latency, durability under node failure, operational burden on a small team, cost at the fleet's
projected scale, and the team's existing familiarity with each option. Full size would add three things. A
sensitivity check on the operational-burden weight, the criterion most likely to move the result. A named
risk and benefit for the recommended option. A one-line dissent from a reviewer who weighted cost higher.

**Why this scenario and not another.** It is technical, scoring-driven, and recognizable to a reader of this
library without requiring unfamiliar domain knowledge, matching the admitting sources' own systems-engineering
and infrastructure register. It does not reuse any sibling's own content: it is not Acme Analytics' Saved
Views chain and not Riverland Sensing's firmware spike. Thornwell Freight is a new, independent fictional
company, invented for this bundle alone. The exact dates, names and figures are a build decision, the same
stance `business-continuity-plan`'s spec took toward its own worked example.

#### Metadata

| Field | Value | Why |
|---|---|---|
| `family` | `decision-docs` | ADR 0022 (adopt the decision-docs family contract)'s fourth-member clause, maintainer decision 5 |
| `phase` | `develop` | Contract-gated; matches all four existing members |
| `sizes_available` | `[lean, full]` | Maintainer's settled sizing; catalog correction 1 above |
| `bundle_id` | `trade-study` | This spec's recommendation, ruled by the maintainer 2026-10-15. The catalog id stays `trade-study-options-analysis`, the shape `north-star-metrics` and `business-continuity-plan` both already kept |
| `status` | `beta` | Every bundle |
| `methodology` | `generic` (recommended) | The catalog's own "methodology-agnostic" supports this value, and it matches `adr`, `rfc` and `sdd`'s declared methodology. The contract's methodology row is descriptive, not gated, so this is a recommendation, not a requirement |
| `pairs_with` | `[]` | Checked against `tools/known-skills.txt`, 2026-10-14; no pinned skill id names this type |
| `related_templates` | `[adr, rfc, sdd, spike-report]`, inline | Its four siblings, the same pattern `spike-report_meta.yaml` used for its own three |
| `aliases` | keep `trade-off analysis`, `decision analysis`, `weighted scoring matrix`; do not add `analysis of alternatives` | Catalog correction 5 above |

#### What landing this bundle closes elsewhere

1. **The catalog entry**, per the corrections above, in both `docs/internal/catalog.md` and
   `atlas/catalog-data.json`, then the atlas regenerated.
2. **This page's Progress table**: the `trade-study` row's Built column, and an inline dated note in the
   2026-10-13 sweep paragraph.
3. **Issue #259 (bundle: trade-study-options-analysis)** closes with the build PR.
4. **No sibling bundle's forward reference is resolved by this landing**, unlike `business-continuity-plan`'s
   landing against `runbook` and `production-readiness-review`. No sibling currently names this type in its
   own `related_templates` field. Whether `adr`, `rfc`, `sdd` or `business-case` gain a direct, reciprocal
   link to this bundle is a build decision this spec does not require.
5. **The hand-maintained family lists, beyond the usual count sweep.** `README.md` line 176 heads the family
   "`decision-docs` (four bundles, the family complete)", and line 178 lists four jobs; both must gain the
   trade study. `templates/README.md` lists the family's four members, and `STATE.md` names the family
   "**complete**" with four members. Each must name the fifth.

#### What the build would cost

No build has run for this type. This is projected from the family's own most recent member and the library's
two most recent two-size builds, all measured figures from `bundle-builds/INDEX.md`. `spike-report`, the
family's only other member admitted under the ADR 0022 (adopt the decision-docs family contract) clause,
cost $33.21 whole (15 agents, single size). The two most recent
two-size builds cost less: `business-continuity-plan` cost $20.57 whole (15 agents), and `problem-statement`
cost $19.97 whole (18 agents). `north-star-metrics`, a two-size floor build, cost $9.73 (9 agents). A
whole-bundle estimate of **$14 to $21 at API list rates** is reasonable on the two-size precedents.
`spike-report`'s higher figure has a recorded cause: `.claude/commands/build-bundle.md` states that it and
`test-summary-report` were "both drafted on Opus by per-bundle scripts that pinned no model", while the
current workflow pins Sonnet. It is a projection, not a measurement, until
`python tools/gen-bundle-build-report.py --ingest` runs against an actual build report.

### delivery-docs (new member, by amendment): the use case specification the user-stories guide routes to

**`use-case-specification`** - `delivery-docs`, **`phase: deliver`**, sizes **`[lean, full]`**, methodology
**`methodology-agnostic`** (set at build from the admitting sources' lineage; see catalog correction 2
below), catalog id `use-case-specification`, catalog name "Use Case specification", aliases `use case`,
`use case model`. Catalog owner: BA. Purpose: "Describe actor-system interactions to achieve a goal"
(`atlas/catalog-data.json`, id `use-case-specification`, and `docs/internal/catalog.md:72`, row 35; both verbatim). GitHub
issue **#254 (bundle: use-case-specification)**.

#### Demand: the sentence this library already ships, with nothing behind it

`templates/user-stories/user-stories_guide.md:15` states, under "When NOT to use": "You need exhaustive
actor-system flows. Use a use-case specification." That sentence is live in the shipped bundle today, and
no bundle named "use-case specification" exists for it to point to. The companion repeats the same boundary
from its own side: `user-stories_companion.md:151-153` states, "A use case documents an actor-system
interaction in full (main and alternate flows); a story is a thin slice that triggers a conversation," and
recommends, "prefer stories for iterative delivery; reserve use cases for contexts that genuinely need
exhaustive flow documentation." The demand is routing prose, not a promise tag: no `future:` tag names
this type (a grep of every `_meta.yaml` for a tag naming "use case" or "use-case" returns nothing), so no tag
needs correcting. The demand is the guide's own sentence, already read by every user of a shipped bundle.

#### Admission: four sources, each already fetched and raw-checked

Every quotation below passed the recheck in
`_local/research/2026-10-12_admission-sweep-5/recheck-out.json` on 2026-10-12.
[ADR 0048 (one named source clears the admission test)](decisions/0048-one-named-source-clears-the-admission-test.md)
requires only one; this candidate clears on four, independent of the family question.

| Source | What it publishes | Quotation (passed the recheck) |
|---|---|---|
| Alistair Cockburn, Basic Use Case Template (HaT TR 96.03a, 1998), University of Otago mirror | A titled, numbered document template, in a plain-text and a table rendering, with a worked example | "You have permission to copy and distribute the documents as long as you reference the source of the originals" |
| Karl E. Wiegers, Use Case Template (Process Impact, 1999, v1.0) | A standalone, field-by-field fill-in template | "Permission is granted to use, modify, and distribute this document" |
| IBM/Rational, Use-Case Specification: \<Use-Case Name\> (Rational Unified Process template), university mirror | A sectioned specification document with named flow sections | section headings "Basic Flow", "Alternative Flows", "Extension Points" |
| Alistair Cockburn, Writing Effective Use Cases, pre-publication draft #3 (dated 2000.02.21; published by Addison-Wesley, 2001) | States the formality scheme directly, in the author's own words | "A casual use case is one written in simple, paragraph, prose style" and "A fully dressed use case is written with one of the full templates" |

**Cockburn's own 1998 field list is read in full, not reconstructed.** The Otago mirror and an independent
second mirror (Bentley University) both confirm the same field set by direct read: a characteristic-information
block (Goal in Context, Scope, Level, Preconditions), a Main Success Scenario, Extensions, and an optional
closing block. The field-name spans "Goal in Context", "Success End Condition", "Failed End Condition",
"Primary Actor", "Trigger", "Sub-Variations", "Superordinate Use Case", and "Minimal Guarantee" each passed
the recheck against one or both mirrors. Scope, Level, Preconditions, and the closing optional block's own
field names (priority, performance target, frequency, channel to actor) were read directly in the full
template text but were not individually submitted to the recheck, so they are reported here without
quotation marks.

**What was never read.** "Use Case 24 Fully Dressed Use Case Template," the heading on pages 119 to 120 of Cockburn's
*Writing Effective Use Cases* (Addison-Wesley, 2001), was never read. Every Internet Archive copy
(`writingeffective0000cock`, `writingeffective00cock`, `writingeffective0000alis`) is a lending-restricted
item, confirmed via `archive.org/metadata`, and no borrow credential was available in either research pass.
A 2026-10-12 gap-fill read a free Pearson sample-pages PDF for the same ISBN instead, which carries the
book's table of contents, index, preface, and chapter 3 body text verbatim, but not the pp.119-120 template
box itself. That PDF confirms, by direct read: the table of contents heading reads "Use Case 24 Fully
Dressed Use Case Template" at page 119; the preface states, in Cockburn's own words, that the 2001 book
"led to the explanations in this book and to the Stakeholders and Interests model, which is a new idea
presented here" (passed the recheck); and the book carries a dedicated section headed "6.2 Minimal
Guarantees" (also passed). The same gap-fill confirmed, by a direct text search of the full 1998 template
(not a search, a full read), that the phrase "Stakeholders and Interests" does not appear there at all,
which corroborates the preface's own "new idea" claim rather than contradicting it. So the fully-dressed
field set used in Section design below rests on this combination: the 1998 template (read in full), the
2001 preface and index (read in full), and converging secondary field lists, not on the literal pp.119-120
box, which this library has never seen. Any companion or research-log entry for this bundle must state
that distinction exactly this way, not round it up to "read."

#### Family fit: the amendment, the sixth verb, and what it admits

**No contract admits this type as written.** A 2026-10-12 research pass tested it against all ten family
contracts. Nine exclude it outright on their own membership clause: `decision-docs`, `discovery-docs`,
`qa-docs`, `governance-docs`, `process-docs`, `standing-standards`, `strategy-docs`,
`experimentation-docs`, and `communication-docs`. Only `delivery-docs` offers even a strained fit, and the
research that found that strain is explicit that a maintainer could just as reasonably read it as
excluding the type too, since none of the five verbs it carried at the time (defines, decomposes, verifies,
changes, announces) cleanly names what the type does. **Admitting it therefore
widens a membership test**, the same shape
[ADR 0060 (change-request joins delivery-docs)](decisions/0060-change-request-joins-delivery-docs.md)
recorded for the fifth verb, "changes". It is the fourth widening of a membership test in the library, after
ADR 0060,
[ADR 0067 (tracking-plan joins governance-docs as a sixth member)](decisions/0067-tracking-plan-joins-governance-docs-as-a-sixth-member.md)
and [ADR 0070 (north-star-metrics joins strategy-docs as a fifth member)](decisions/0070-north-star-metrics-joins-strategy-docs-as-a-fifth-member.md).

**The maintainer chose the verb "elaborates" on 2026-10-13**, after asking whether "extends", "expands" or
"clarifies" would serve better. The membership clause's verbs become, in this order: "defines, decomposes,
elaborates, verifies, changes, or announces a unit of product work." The chain sentence gains one link,
placed after the stories and before the acceptance criteria: a use case specification elaborates one
actor's full path through the system to reach a goal, including alternative and exception flows.

**What "elaborates" admits, and what it does not.** This is the question the maintainer's sitting note
raised ("clarify more what is intended, gained, and the impact of "elaborates"?"), and ADR 0072 answers it
in the shape of ADR 0060's own equivalent passage. Three things, stated plainly:

1. **What the verb is intended to admit.** A document that walks one named actor through a complete
   interaction with the system toward one goal: a main success scenario, stated as a numbered sequence of
   steps, plus the alternative and exception paths that branch off it and either rejoin the main scenario
   or end it. It does not admit a diagram, a board, or a live tool schema; the admission section above
   confirms all four qualifying sources ship a written, sectioned document, not a picture.
2. **What the library gains.** `templates/user-stories/user-stories_guide.md:15` already tells a reader who
   needs "exhaustive actor-system flows" to use a use-case specification. The library gains the one thing
   that sentence has promised and not delivered since the guide shipped: a document that actually carries a
   main success scenario and its numbered extensions, rather than a story's single-sentence goal or a
   checklist of pass/fail criteria.
3. **The impact on existing members.** No existing member's placement or obligations change. The
   membership clause gains one word and the chain sentence gains one clause, the same shape ADR 0060 used
   for "changes"; `user-stories`, `acceptance-criteria`, `epic`, and `prd` keep their own sections,
   obligations, and chain positions exactly as they stand today. Whether any of their companions gains a
   line naming the new neighbour is a build decision, not one this record settles, following the precedent
   [ADR 0067](decisions/0067-tracking-plan-joins-governance-docs-as-a-sixth-member.md) and
   [ADR 0070 (north-star-metrics joins strategy-docs as a fifth member)](decisions/0070-north-star-metrics-joins-strategy-docs-as-a-fifth-member.md)
   both set: neither amendment swept an existing member's companion.

**The nearest neighbour kept out: `user-flow-task-flow`, placement deferred.** Its catalog entry
(`docs/internal/catalog.md:100`, row 57) states its purpose as "Map the steps and decisions a user takes
through a task", at category "Design / Architecture" and stage "design", and its aliases are "flow diagram"
and "wireflow". A naive admission test, "one actor, one goal, step by step", would admit this type too. The
exclusion rests on what the catalog says a user flow is, a design artifact drawn as a diagram, not on the
actor-goal framing. A user flow written out as text is the case this boundary leaves open for that type's
own placement. Nothing in this record places `user-flow-task-flow` anywhere; its family and axis stay open
for a later candidate pass.

**The closest shipped shape kept out: `test-case`.** The contract paragraph also excludes a document that
checks a path rather than specifying it, which `qa-docs` carries as `test-case`. The Boundaries section
below gives the reason.

#### Boundaries: six siblings kept distinct, and one kept out

- **`user-stories`.** The demand source and the closest sibling. `user-stories_companion.md:151-153`
  already states the boundary from its own side (quoted above): a use case documents the interaction in
  full; a story is a thin slice that starts a conversation. The two are not duplicates; a shipped bundle
  already says so.
- **`acceptance-criteria`.** Its full template carries a "Scenarios (Given / When / Then)" section and an
  "Edge cases and negative paths" section (both verbatim headings, `acceptance-criteria_template-full.md`).
  Those are discrete, markable pass/fail conditions, not a sequential actor-system flow with branching
  extensions that rejoin or end a main scenario. A use case specification is the flow those conditions are
  later written against; neither replaces the other, and the worked example below shows the hand-off
  directly.
- **`epic`.** Its full template carries a "Child Stories" table and an "Out of Scope" section (both
  verbatim headings, `epic_template-full.md`). An epic groups a body of work large enough to need
  decomposing; it does not walk one actor through one goal step by step.
- **`prd`.** Its full template's "UX and design" section (verbatim heading, `prd_template-full.md:177`)
  covers key flows and every state (empty, loading, error) for a whole feature, at the altitude of a
  product decision. A use case specification elaborates one actor's one goal at a finer grain, after the
  PRD has already decided what the feature is.
- **`test-case`.** Its full template shares the closest structural shape of any shipped sibling:
  "Preconditions and Test Data," "Steps and Expected Results," and "Postconditions and Teardown" (verbatim
  headings, `test-case_template-full.md`). A test case checks one specific path, written from a test-design
  standpoint; a use case specification elaborates the actor's own goal-directed interaction, and is one
  thing a test case may later be written against. The contract's new paragraph names this exclusion.
- **`sdd`.** Its full template's "The Design" section (verbatim heading, `sdd_template-full.md:81`) documents
  the technical architecture that satisfies a set of requirements: components, data flow, interfaces. A use
  case specification stays at the actor's altitude throughout; it names what the system does for the actor,
  never how the system is built to do it. This is this library's own position, not a sourced finding; no
  source read for this candidate addresses the use-case-versus-design-document boundary directly.
- **`user-flow-task-flow` (kept out, placement deferred).** See Family fit above.

**Distinctness holds on real flow-depth content, but it is genuinely contested, not settled.** A reader
could reasonably argue the overlap with `acceptance-criteria`, `epic`, `prd`, and `test-case` runs deeper
than the paragraphs above allow; none of those four shipped bundles' example content was re-read against
the full fully-dressed field set in this pass. The boundary this spec draws rests on structural comparison
of headings and on the library's own shipped boundary sentence (`user-stories_companion.md`), not on a
fresh content-level audit of all four.

#### Formality and sizes: casual and fully dressed, not brief and not S/M

Cockburn's own sources name three formality levels, not the library's usual lean/full pair. His
pre-publication draft defines the third, lowest one directly: "The brief of a use case is a 2-6 sentence
description of the use case behavior" (passed the recheck). That is a paragraph, not a fillable template at
all, and it sits below any document this library builds. The two that remain are the two the quoted
admission section above already names: "casual" ("written in simple, paragraph, prose style") and "fully
dressed" ("written with one of the full templates"). This bundle ships **`[lean, full]`**: `lean` carries
Cockburn's casual form, `full` carries the fully-dressed field set reconstructed in the Admission section
above. The guide must give Cockburn's own names beside the library's `lean`/`full` labels, the same
accommodation [ADR 0071](decisions/0071-business-continuity-plan-joins-standing-standards-as-a-tool.md)'s
spec made for the library's own section groupings against SIMM 5325-A's fourteen.

**A note on sourcing this naming decision.** An earlier research document in this sweep
(`_local/research/2026-10-12_admission-sweep-5/family-question.md`) describes the catalog's current sizing
as "brief and fully-dressed." That phrase does not appear in either machine artifact: `docs/internal/catalog.md:72`
and `atlas/catalog-data.json` (id `use-case-specification`) both carry the field `size_variant: S/M`, not a brief/fully-dressed
pair. The correction below is unchanged either way: name the two shipped sizes `casual` and `fully dressed`,
sourced to Cockburn directly, not `S/M` and not any brief/fully-dressed pairing this repository's own
catalog files do not actually carry.

#### Section design

| Section | In lean? | What it is, with sourcing |
|---|---|---|
| **Title and Actor** | yes | The use case's name and its Primary Actor, the one role whose goal the case serves. Sourced to Cockburn's 1998 numbered-use-case header and its "Primary Actor" field; the field name passed the recheck |
| **Goal in Context** | yes | What the actor is trying to accomplish, and the circumstance that brings them to it. Sourced to Cockburn's 1998 "Goal in Context" field, read and passed |
| **Scope and Level** | **full only** | Scope: whose system this use case is about (the system under design, or a business process around it). Level: whether this is a summary case or one step inside a larger one. Both are 2001-book-era refinements over the 1998 template's plainer "Scope" field; reconstructed per the Admission section's gap-fill, not read verbatim from pp.119-120 |
| **Preconditions and Trigger** | yes | What must already be true before this case can start, and the event that starts it. Sourced to Cockburn's 1998 "Preconditions" and "Trigger" fields, both read and passed |
| **Main Success Scenario** | yes | The numbered sequence of steps that reaches the goal when nothing goes wrong. Sourced to Cockburn's 1998 Main Success Scenario section and to the RUP template's "Basic Flow" heading, both read and passed |
| **Extensions** | **full only** | Numbered branches off the main scenario: alternative paths that still reach the goal, and exception paths that end the case instead. Sourced to Cockburn's 1998 "Extensions" section and the RUP template's "Alternative Flows" and "Extension Points" headings, all read and passed. Lean folds a short prose note of the most important exception into the Main Success Scenario section rather than carrying a separate section, the same collapsing move `business-continuity-plan`'s spec made for its own lean variant |
| **Postconditions (Success and Failed End Condition)** | yes | What is guaranteed true when the case ends, on the success path and on a failed one. Sourced to Cockburn's 1998 "Success End Condition" and "Failed End Condition" fields, both read and passed. The 2001 book renames these "Minimal Guarantee" and a success guarantee, per the book's own "6.2 Minimal Guarantees" section (read and passed), and the guide names both terms |
| **Related Information** | **full only** | The 1998 template's optional closing block: priority, performance target, frequency, and any superordinate or subordinate use case this one relates to. Sourced to Cockburn's 1998 template's own optional block, read in full; its field names "Sub-Variations" and "Superordinate Use Case" passed the recheck, and the remaining field names in that block (priority, performance target, frequency, channel to actor) were read but not individually submitted to the recheck |
| **Open Issues and Schedule** | **full only** | Anything still undecided about this flow, and, where it matters, a due date. Sourced to the 1998 template's own closing fields of the same name, read in full but not individually submitted to the recheck |

**A related-business-rules section is recommended OMITTED, not labeled as this library's own addition.**
This candidate's own type description, the one the admission sweep researched against, names related
business rules as a core component, but no field by that name appears in any of the four admission
sources, in the 1998 template's full text, or in the 2001 book's index or table of contents; the index's
only "business rules" entry sits under the book's Extensions chapter, about brainstorming alternative
conditions during authoring, not under a template section. The one secondary illustration that uses a
related-business-rules heading at all is a conference slide's own worked example, not a template. Two
options exist: omit it, or carry it labeled explicitly as
this library's own addition. **Recommendation: omit.** Labeling it as the library's own addition would make
this the one section in the whole bundle that rests on no source at all, inside a bundle whose entire
admission case is built on fidelity to four named templates; a reader who needs rule-level detail already
has `epic`'s "Out of Scope" section or `acceptance-criteria`'s "Out of scope and notes" section for it. If a
dedicated business-rules artifact is ever wanted, the library's own precedent for `solution-brief` (the
2026-09-20 note in this page's Progress section) is to let it enter through the front door, a research pass
and a catalog entry, rather than ride in as an unsourced section of a different bundle.

The lean variant's five sections (Title and Actor, Goal in Context, Preconditions and Trigger, Main Success
Scenario, Postconditions) are a strict ordered subset of the full variant's nine, as contract section 3.2
requires. Full inserts Scope and Level, Extensions, Related Information, and Open Issues and Schedule, each
at the point in the sequence the table above places it.

#### Catalog corrections the landing PR must make

Per [decision-procedures.md procedure 1](decision-procedures.md#1-a-catalog-call-loses-to-research), both
`docs/internal/catalog.md` and `atlas/catalog-data.json`, then regenerate the atlas:

1. **`methodology`: `Waterfall/UP/RUP` is incomplete.** No source read for this candidate ties the type to
   Waterfall. Cockburn and Wiegers are both methodology-agnostic practitioner lineage, and Jacobson's
   current edition (Use-Case 3.0, 2024) is explicitly agile. The landing PR replaces the value with one the
   admitting sources support, descriptive rather than gated, per `delivery-docs.md` section 2.
2. **`size_variant`: `S/M` does not name the two sizes this bundle ships.** Three formality levels exist in
   Cockburn's own scheme (brief, casual, fully dressed), and even collapsed to two for this library's
   convention, `S/M` does not map onto `casual` and `fully dressed` without a stated rule. The landing PR
   corrects the field to name the two sizes this bundle actually ships.
3. **`relationships`: empty today, and every boundary source points at one neighbour.** `use-case-specification`'s
   `relationships` field is `[]` in both machine artifacts, while `user-story`'s own entry already carries
   `["Epic", "Sprint Backlog"]`. Every source that discusses the boundary in this sweep contrasts the type
   directly with the user story, including this library's own shipped `user-stories_companion.md`. The
   landing PR adds `"User Story"` to this type's `relationships` field. It does not add a reciprocal entry
   to `user-story`'s own field; that is a build decision, not one this spec settles.
4. **`use case model` stays an alias, with the distinction stated in prose, not resolved by dropping it.**
   The alias most naturally names the UML use-case diagram, which this sweep's sources treat as a separate,
   out-of-scope artifact from the written specification this bundle templates. The same precedent
   `business-continuity-plan`'s spec applied to "DR plan" and "BCP" applies here: keep it, because a reader
   genuinely types it to search for this document, and state the distinction in the companion rather than
   let the alias imply the two are the same artifact.

#### `pairs_with`: checked, empty

`gh api repos/product-on-purpose/pm-skills/contents/skills --jq '.[].name'` returned 68 skill names on
2026-10-14. No name contains "use-case," "use case," "uc-," or "usecase." The closest-sounding names,
`deliver-acceptance-criteria` and `deliver-user-stories`, produce and consume the two siblings this bundle
is distinguished from, not this type, and `tools/known-skills.txt` lists no use-case skill.
**`pairs_with: []`**.

#### Risks for the build and review

1. **The fully-dressed field set is reconstructed, not read verbatim.** The Admission section states this
   exactly; a companion or research-log that writes as if pp.119-120 were read, rather than inferred from
   the TOC, index, preface, and the 1998 template's own confirmed absence of the 2001-era fields, overclaims
   the one thing this candidate's research could not settle.
2. **A related-business-rules section must not be attributed to Cockburn.** No source supports it as a
   named field. If a reviewer or a drafting agent adds it anyway because the type description implied it,
   that is the unsourced-confidence defect this library already tracks, and it fails review on sight.
3. **Family fit is strained, and the companion must say so plainly.** The research that found even a
   strained fit is explicit that a maintainer could as reasonably read `delivery-docs` as excluding this
   type. A companion that presents "elaborates" as an obvious reading, rather than the library's own chosen
   widening, overstates what ADR 0072 actually decided.
4. **Distinctness is contested, not settled, against `acceptance-criteria`, `epic`, `prd`, and `test-case`.**
   The Boundaries section above draws each line from headings and from the library's own shipped boundary
   sentence, not from a fresh content audit of all four siblings' example files. A companion that claims a
   clean, fully resolved boundary with all four overclaims what this pass actually checked.
5. **The build workflow's templates stage has repeatedly copied a worked example's own scenario into a
   template's GOOD and WEAK text.** The same practice named in `production-readiness-review`'s and
   `business-continuity-plan`'s own specs: grep the drafted templates for the example's proper nouns (Saved
   Views, Recurring Analyst, Priya Nair) before review.
6. **The BABOK contradiction from the research must not be cited either way.** One research dimension flags
   BABOK's Use Cases and Scenarios technique `publishes_type_as_written_document: false`; the other flags
   the same unread source `true`. Neither flag should be treated as settled, and BABOK should not appear in
   this bundle's companion as a qualifying or a disqualifying source.

#### The worked example: elaborating a story this library has already shipped twice

**The scenario is the one the delivery-docs family already shares, not a new one.** The use case elaborates
the "set a default saved view" story, the full card in `templates/user-stories/user-stories_example.md`
("As a recurring analyst, I want to set one of my saved views as the default for a dashboard, so that the
dashboard opens the way I work instead of in its generic default state"), which is also the story
`templates/acceptance-criteria/acceptance-criteria_example.md` already writes Given/When/Then scenarios and
edge cases against, and which the epic example reserves as child story `SV-4` ("Set one view as the
dashboard's default (FR-3)").

**Chronology: after the story exists, before the acceptance criteria are written.** `created: "2026-06-20"`,
`updated: "2026-06-30"` (matching the shared `updated` date most of this family's examples carry). That
sits after `user-stories_example.md` (created 2026-06-18, the story this case elaborates) and before
`acceptance-criteria_example.md` (created 2026-06-22, which this case feeds). That ordering matches the
chain position ADR 0072 gives the type: between the point the story exists and the point the acceptance
criteria confirm it.

**Primary Actor: the Recurring Analyst, the same persona `prd_example.md` already names.** Goal in Context:
switch to a saved view and make it the one that loads automatically, so the daily re-filtering tax
disappears. Main Success Scenario: open the Views control, select a saved view, confirm setting it as
default, and on the next dashboard open that view loads instead of the generic default. Extensions, each
tied to a fact a sibling document already states rather than invented fresh: a referenced filter has since
been deleted (`acceptance-criteria_example.md`'s own edge case: "it loads the still-valid filters and shows
a clear message naming the missing filter"); no default is currently set (the same example's second edge
case, loading the generic default with no error).

**What it must not do.** It must not invent a shared-view permission edge for this case. Both
`acceptance-criteria_example.md` ("Does not cover sharing, which has its own story") and the epic example
(sharing is child story `SV-5`, not `SV-4`) scope the default-setting story to the owner's own views only;
a use case for sharing is a separate case, for a later story, not this one's extension.

**Links.** Upstream: the PRD (FR-2, FR-3), the epic (child stories SV-3 and SV-4), and the user story it
elaborates. Downstream: `acceptance-criteria_example.md`, whose Given/When/Then scenarios and edge cases
this case's own extensions feed directly, stated as a link in both directions per contract section 4's
shared-example rule.

#### Metadata

| Field | Value | Why |
|---|---|---|
| `family` | `delivery-docs` | ADR 0072, amending the membership test with the verb "elaborates" |
| `phase` | `deliver` | The only value the contract allows for this family |
| `bundle_id` | `use-case-specification` | Same as the catalog id; no divergence is proposed, unlike `north-star-metrics` or `business-continuity-plan` |
| `sizes_available` | `[lean, full]` | Cockburn's casual and fully dressed; see Formality and sizes above |
| `status` | `beta` | Every bundle |
| `methodology` | `methodology-agnostic` (set at build) | Catalog correction 1 above; no source ties the type to Waterfall |
| `pairs_with` | `[]` | Checked against pm-skills `origin/main`, 2026-10-14; see above |
| `related_templates` | `[user-stories, acceptance-criteria, epic, prd]`, inline | The demand source and boundary sibling, the downstream sibling the worked example feeds, and the two upstream siblings that open the chain before this case elaborates one of their stories |
| `aliases` | `use case` kept; `use case model` kept, with the UML distinction stated in the companion | Catalog correction 4 above |

#### What landing this bundle closes elsewhere

1. **The `delivery-docs` contract's membership clause**, which moves to `0.3.0` and lands with ADR 0072 in
   the same change as this spec.
2. **`templates/user-stories/user-stories_guide.md:15`'s routing sentence becomes resolvable.** The build PR
   must update that line so "use a use-case specification" links to the new bundle rather than naming a
   type the library does not ship. Whether `user-stories_companion.md:151-153` gains the same link is a
   build decision, following the precedent that neither ADR 0067 nor ADR 0070 required an existing
   companion to change.
3. **The catalog entry**, per the four corrections above, in both `docs/internal/catalog.md` and
   `atlas/catalog-data.json`, then the atlas regenerated.
4. **This page's Progress table**: the `use-case-specification` row's Built column, and an inline dated
   note in the 2026-10-13 sweep paragraph.
5. **GitHub issue #254 (bundle: use-case-specification)** closes with the build PR.

#### What the build would cost

No build has run for this type. This is projected from two groups of measured figures in
`bundle-builds/INDEX.md`. Within `delivery-docs` itself: `change-request` cost $14.41 whole (15 agents,
`[lean, full]` provisional), and `announcement-internal-comms` cost $16.99 whole (15 agents, single size).
Among the library's most recent two-size, whole-build Tier-2 members outside this family:
`business-continuity-plan` cost $20.57 whole (15 agents), and `problem-statement` cost $19.97 whole (18
agents). `north-star-metrics`, at $9.73 (9 agents), is excluded from the central estimate because its
report is explicitly a **floor**, covering drafting and review only, not the whole build. On these four
measured, whole-build figures, a projected range of **$14 to $21 at API list rates** is reasonable. It is a
projection, not a measurement, until `python tools/gen-bundle-build-report.py --ingest` runs against an
actual build report.

### governance-docs (seventh member, by amendment): the data dictionary, scoped to what a dataset's fields mean

**`data-dictionary`** - `governance-docs`, **`classification: utility`**, sizes **`[lean, full]`**,
methodology set at build from the admitting sources' lineage (the catalog's `methodology-agnostic` is not
contradicted by anything retrieved; see Catalog corrections), catalog id `data-dictionary` (catalog 141 in
[`catalog.md`](catalog.md); atlas index 140 in
[`atlas/catalog-data.json`](../../atlas/catalog-data.json)), catalog name "Data Dictionary", aliases
(catalog, both flagged for correction below) `metric definitions`, `data catalog entry`. Catalog owner:
`Data / Analytics Eng`. Catalog purpose (flagged below): "Document the meaning and usage of events and
metrics." Catalog contents (flagged below): "event name, description, properties, usage, owner." Catalog
`stage`: measurement. Catalog `formality`: standard. Catalog `rarity`: occasional. Catalog `size_variant`:
`S/M`. Catalog `relationships`: `[Tracking Plan]`. `tier: 2`, `tier_inferred: true`, `must_have: false`,
`built: false`, `state: candidate`.

**The bundle id is `data-dictionary`, the same as the catalog id, with no reason found to differ.** This
follows the same bare-name convention `tracking-plan`, `risk-register`, `raid-log`, `kpi-dashboard` and
`issue-log` already use; it is not a case needing a distinct bundle id the way `change-log`,
`north-star-metrics` and `business-continuity-plan` each needed one.

**Scope, settled by the maintainer before this spec was written, and not reopened here.** This bundle
documents what the fields of a dataset or table mean. Its Purpose and Boundary section, in both sizes,
excludes by name event cataloguing (the tracking plan's job, [ADR 0067](decisions/0067-tracking-plan-joins-governance-docs-as-a-sixth-member.md)
(tracking-plan joins governance-docs as a sixth member)) and metric-formula locking (the KPI dashboard's
own Metric Definitions section). The catalog's own wider framing, its purpose field "Document the meaning
and usage of events and metrics", is not built. This spec does not reopen the scope; it does change, and states plainly that it
changes, the reasoning the scope condition rests on. See the boundary subsection below.

#### Demand: named as an unfilled gap, four times, by the sibling it stands next to

No shipped bundle **routes to** a data dictionary as the one document something else is missing (a `future:` tag or an explicit hand-off); the pattern is
closer to `tracking-plan`'s own demand section than to `change-log`'s, because the gap is named inline
rather than promised by a `future:` tag. A grep across every tracked file in `templates/` and
`docs/internal/` for "data dictionary", run 2026-10-14, returns eleven files. Checked directly:

- `templates/tracking-plan/tracking-plan_template-lean.md:40-48` and the matching lines in
  `tracking-plan_template-full.md` both state, inside the template body itself, that a tracking plan is
  not a single feature's instrumentation slice, a data dictionary, a measurement plan, or the enforced
  schema in a tool, and the GOOD text under Purpose and Boundary (`tracking-plan_template-lean.md:83`)
  reads: "What the warehouse tables mean once these events reach them is the data dictionary's job."
- `templates/tracking-plan/tracking-plan_example.md:50-51` states the same gap in the worked example's own
  Purpose and Boundary section: "It is not the data dictionary, the document that will state what the
  data in these events' destination tables actually means once it is implemented, which this program has
  not yet written." **Landing this bundle makes that sentence false where it stands.** This is a required
  landing-site edit; see What landing this bundle closes elsewhere, below.
- `templates/tracking-plan/tracking-plan_guide.md:30` names the boundary again, in the operator card's
  "When NOT to use" list: "The question is what the data means once it lands in the warehouse. That is the
  data dictionary's job", and continues: "stated in the opposite tense from this plan's forward-looking". The same file's comparison table (`tracking-plan_guide.md:44-48`) gives the data
  dictionary its own column against the tracking plan, the measurement plan, and the KPI dashboard, and its
  quality rubric (`tracking-plan_guide.md:81`) scores a plan on whether it names the data dictionary by
  name as a neighbour it hands content to.
- `templates/tracking-plan/tracking-plan_companion.md:90-104` and `:395-399` carry the same boundary at
  length, citing Wizbrand's tense-based account. **This companion text is the shipped prose the 2026-10-14
  research (below) finds is no longer the soundest statement of the boundary it draws.** It is not wrong
  that the two documents differ; it is the specific reason it gives (tense) that a second look does not
  support as the general rule. This is a recommended, not required, landing-site edit; see the same
  subsection below.
- `templates/experiment-design-doc/experiment-design-doc_guide.md:42-44` and the matching
  `experiment-design-doc_companion.md:504` both route a reader toward a standing instrument rather than a
  one-time test record: "A tracking plan, a data dictionary, or an experiment log is maintained across many
  tests and is never finished." `docs/internal/contracts/experimentation-docs.md:42-45` carries the same
  exclusion inside the family contract that governs that bundle: "A standing measurement instrument is not
  a member, however closely it serves experiments. A tracking plan, a set of metric definitions, a data
  dictionary or an experiment log is maintained across many tests and is never finished, so it belongs to a
  `classification` family."
- `docs/internal/decisions/0067-tracking-plan-joins-governance-docs-as-a-sixth-member.md:28-29` names the
  data dictionary directly: "two neighbours the research named but this record does not place: the
  per-feature measurement plan... and the data dictionary."

**This is the demand-side case for building it: four shipped artifacts already point at a document this
library has not written, and one worked example's own sentence becomes false the longer the gap stays
open.**

#### Admission: it clears on several sources, in two different senses of the term

Every quotation below is checked against raw page text, either in
`_local/research/2026-10-12_admission-sweep-5/recheck-out.json` (gitignored) or, where noted, the
2026-10-14 raw-check file, `_local/research/2026-10-14_prep-research/recheck-out.json` (also gitignored).

| Source | What it says or ships |
|---|---|
| Amplitude | Docs: "A data dictionary is a document that lays out the project's taxonomy." |
| Docsie | Ships a template, "completely free to download in Word (DOCX), PDF, and Markdown formats," with a column set of "Field, Type, Required, Definition, Example, and Notes," review-cadence options "[Monthly / Quarterly / Annual / Event-based]," and a line for "data owner, steward, support channel, and review cadence." |
| Wizbrand | "A Data Dictionary is a structured reference that documents data elements and their meaning." The same page states an ownership and cadence discipline: "Who maintains it, who approves changes, and who is notified," "Ownership should be shared but explicit," and "review it on a cadence (monthly or quarterly)." |
| Basedash | "A data dictionary is a structured reference that defines what every field, table, and metric in your data means." The same page states per-table ownership ("Owners are usually the team that produces the data, not the team that consumes it"), a review cadence ("A short quarterly review where owners confirm or fix their definitions is usually enough"), and field-level content ("the technical facts (name, data type, nullability)" and "Enums, ranges, or units"). |
| OSF / Center for Open Science | "A data dictionary is critical to making your research more reproducible because it allows others to understand your data," and "The purpose of a data dictionary is to explain what all the variable names and values in your spreadsheet really mean." Licensed CC0. Its own retrieval note (not itself a passed quotation) describes a seven-column template: variable name, readable variable name, measurement units, allowed values, definition, optional synonyms, optional longer description. |
| Smithsonian Libraries and Archives | "explains the contents of the dataset," and names "allowable values in a field" as a required element. |
| University of North Carolina (RDMC) | "A codebook is a document that describes an individual data file or a collection of data files," and states that a codebook is "sometimes referred to as a" data dictionary, while flagging "There is no single standard." |
| GDAC (UK government) | A structured glossary entry stating "The content of a data dictionary is usually extracted from the database or modelling tool," distinct from its own separate entries for a Business Glossary ("A repository of approved, governed and maintained compendium of business term names, their definitions") and a Data Catalogue ("An inventory of available data assets supported by a collection of metadata"). |

Docsie alone clears [ADR 0048 (one named source clears the admission test)](decisions/0048-one-named-source-clears-the-admission-test.md),
because it publishes the type as a downloadable written document; the others corroborate the term, not
all in this bundle's sense. **The qualifying sources use the name in two different senses, and the Admission and
Boundary questions must be read together, not separately.** Amplitude's own passing quotation, "a document
that lays out the project's taxonomy," is Amplitude's event-and-property sense, the same sense Mixpanel's
Lexicon uses (see the Boundary subsection below); it is not the sense this bundle builds. OSF, CASRAI (see
Boundary), Docsie, Basedash and GDAC all describe the field-meaning sense of a dataset or table, which is
this bundle's own scope. Admission is not a close call on either sense; which sense the library builds is
the Boundary question, and this spec answers it there.

#### Family fit: `governance-docs` only by a second widening, drawn on subject

**The research tested the contract as it reads today, `0.4.0` after ADR 0067, and the type fails on the
same clause ADR 0067 last widened.** Section 1 admits "a continuously-maintained register, log, or
dashboard that a product or program manager uses to track risk, open items, or performance, or to specify
what the product records so that performance can be tracked." The noun fits without strain: a data
dictionary is a structured reference document, the same shape as a register. The cadence fits too: every
admitting source above that addresses maintenance (Wizbrand, Basedash) describes a document revised as a
schema changes, not written once. The clause that fails is the purpose clause itself: a data dictionary
does not track risk, open items, or performance, and it does not specify what the product records so that
performance can be tracked, which is `tracking-plan`'s own job.

**[ADR 0073](decisions/0073-data-dictionary-joins-governance-docs-as-a-seventh-member.md) (data-dictionary
joins governance-docs as a seventh member) widens that phrase a second time, and the contract moves to
`0.5.0`.** The clause gains "or to document what the fields of a dataset or table mean, so that different
teams compute the same number from them," and no existing word changes. It is the third admission to widen
a membership test, after [ADR 0060 (change-request joins delivery-docs)](decisions/0060-change-request-joins-delivery-docs.md)
and ADR 0067. The roles list gains a seventh bullet and "The six roles" becomes "The seven roles." The
bullet distinguishes the data dictionary from both of its nearest neighbours by subject: the tracking plan
specifies the events and properties a product emits, and the KPI dashboard's own Metric Definitions section
locks one dashboard's metric formulas, neither of which is what a data dictionary's field-meaning entry
does. A dated `0.5.0` change note records all three changes, the pattern ADR 0057, ADR 0061 and ADR 0067
each followed. The exact text is in the [contract](contracts/governance-docs.md) itself.

#### The boundary, on subject rather than tense, and why it changed since the maintainer's sitting

**What the maintainer approved on 2026-10-13.** The sitting that placed this candidate was given a
tense-based scope condition: a tracking plan says what will be recorded, and a data dictionary says what
recorded data means, each drawn from Wizbrand's own account, "A tracking plan describes what you intend to
track," against "A Data Dictionary documents what the data means and how it is structured once
implemented." The maintainer approved the amendment on that basis ("Amend with the scope condition") and,
after a same-day chat exchange, approved the narrow-scope build ("Build, narrow scope"). The sitting's own
follow-up logged one open item: find a second, independent source for the tense line, since Wizbrand was
the only one.

**What the 2026-10-14 research found, answering that open item.** Two independent research passes searched
for a second source on the tense boundary, deliberately excluding Wizbrand and anything citing it. They
found the line **contested**, not confirmed, across sources with no connection to each other. On one side,
the US National Institute of Mental Health's own grant-management guidance names "data collection
instruments (also known as data dictionaries)" that hold "data structures that awardees are expected to
use for new data collection," a forward-looking use of the term from a primary federal source. Temple
University Libraries defines a data dictionary the same way: "a record of each variable and data field
that you are going to collect in your project." On the other side, CASRAI's research-data-management guide
defines a data dictionary as "a structured document, table, or file that defines every variable in a
dataset," "so that anyone other than the person who collected the data can interpret it correctly," which
presupposes the data already exists. Buchanan et al. (2021), a peer-reviewed tutorial, frames its own
worked process as running "from source data (e.g., survey answers on Qualtrics) to an openly shared
dataset accompanied by a data dictionary or codebook," placing the dictionary last. Nazabal et al. (2020) and Phillips et al.
(2024) each describe the same ordering: a data dictionary built from, or after, data a team already holds,
with Phillips et al. placing it as the tenth and final step of a ten-step pipeline. *(2026-10-15, at the
build: Phillips et al. list the data dictionary tenth, and the same paper says "Generation steps often
occur concurrently with one another", so the list position is weaker sequence evidence than "final step"
suggests. The build's research log records the caveat.)* **NIMH and Temple write
a dictionary before collection; CASRAI and Buchanan et al. write one after; so timing is no part of this
boundary.**

**What every one of those sources agrees on, regardless of timing.** Each names the same subject: a data
dictionary defines the variables or fields of a dataset. None of them, on either side of the timing
question, describes a data dictionary as specifying the events and properties a product will emit. Every
tracking-plan source this library already cites (Avo, Twilio Segment, Amplitude, Mixpanel, mParticle)
describes the tracking plan as doing exactly that, and none of them describes it as explaining what a
field means. **The boundary this spec draws is therefore on subject, not on tense: a
tracking plan specifies the events and properties a product emits; a data dictionary documents what the
fields of a dataset or table mean.** This is the same narrow scope the maintainer already approved on
2026-10-13. Only the reason it is the correct scope has changed, and ADR 0073 records that change in full,
under its own headed subsection, so the maintainer reads it as a change from what was approved rather than
discovering it inside a diff that happens to agree with the prior answer.

**One complication the subject-based line does not resolve, and does not need to.** Phillips, Price,
Forbes, Boulange, Mengersen, Reeves and Glauert (2024) and Nazabal et al. (2020) both describe a data
dictionary as filled in from data already collected, which is sequence evidence, not a tense rule stated
as such; this spec weights it as corroboration of the subject-based reading (a dictionary describes
the variables of a dataset), not as a second, independent tense claim. One vendor source,
RudderStack's own whitepaper, lists "Data dictionary/solution design document for analysts or data
consumers to understand how and why data is collected at the source" beside "Instrumentation guide that
tells the responsible dev team how to wire up events within the source," naming both as outputs of the
same tracking-plan process rather than as two documents separated by when each is written. This spec reads that as further support for drawing the line on subject
(what the fields mean, regardless of which document produces that explanation) rather than as a reason to
collapse the two documents into one.

#### Boundaries with each named neighbour

- **Not the tracking plan.** On subject, not tense, per the section above: a tracking plan specifies the
  events and properties a product emits; a data dictionary documents what the fields of a dataset or table
  mean. `tracking-plan`'s own shipped text draws this boundary on tense today
  (`tracking-plan_companion.md:395-399`, `tracking-plan_template-lean.md:69-76`); this spec recommends,
  without requiring, a dated note on that text rather than a rewrite, under What landing this bundle
  closes elsewhere, below.
- **Not the KPI dashboard's own Metric Definitions section.** A data dictionary documents what a field
  means (its name, type, allowed values, and where it lives); the Metric Definitions section
  (`templates/kpi-dashboard/kpi-dashboard_template-full.md:87-109`) locks a derived, computed metric's own
  formula, inclusions, exclusions, grain, owner, and data steward. Basedash's own distinction supports the
  same line: "A data dictionary is a structured reference that defines what every field, table, and metric
  in your data means," naming the field and the metric together as what gets defined, while its own worked
  content (nullability, enums, ranges, units) is entirely field-level, never formula-level. **Falsifier:**
  a source stating that a data dictionary itself locks a metric's formula, inclusions, or exclusions would
  contradict this layering. *(2026-10-15, at the build: the falsifier is met. Wizbrand lists "Calculation
  logic (for metrics): Formulas and inclusion/exclusion rules" among a data dictionary's key components,
  Analytics8 puts "measure names ... their calculations" inside one, and Mixpanel's Lexicon, in the
  event-list sense, documents saved metric formulas. ADR 0073's Considered Option 3 had already weighed
  Wizbrand's language and rejected the wider framing on duplication with the KPI dashboard, so the scope
  stands. The layering is the library's POSITION, not a sourced consensus, and the bundle's companion
  labels it so.)*
- **Not the experiment design doc.** `experiment-design-doc_guide.md`'s own "When NOT to use" list routes
  a reader toward a standing instrument, naming the data dictionary by name: "You need a standing
  instrument, not a one-time record. A tracking plan, a data dictionary, or an experiment log is maintained
  across many tests and is never finished." An experiment design document is written once per test and
  finished when that test's decision is recorded; a data dictionary is never finished in that sense.
- **A business glossary and a data catalogue are named, related concepts this library does not build.**
  GDAC's own glossary distinguishes all three: a Business Glossary is "A repository of approved, governed
  and maintained compendium of business term names, their definitions," a Data Catalogue is "An inventory
  of available data assets supported by a collection of metadata," and a Data Dictionary's content "is
  usually extracted from the database or modelling tool." GDAC's own page lists each of the other two under
  "Confusion over definition and with related concepts", naming the overlap directly rather than leaving it
  implicit. Neither a business glossary nor a data catalogue is a catalog candidate in this sweep's reading
  list, and this spec does not propose
  building either; it names the distinction only so a reader who reaches for "glossary" or "catalog"
  language while filling this bundle does not fold a different document's job into it.
- **Not risk-register, raid-log, issue-log, or change-log.** Same reasoning each of those four boundaries
  already carries in `tracking-plan`'s own companion: none of this sweep's sources connects a data
  dictionary's field-meaning job to risk tracking, RAID quadrants, resolved issues, or baseline change
  requests. **POSITION**, stated for completeness because contract section 1 requires every member to
  state its position against every other member.

#### Routing a product-analytics reader who means the event list, not this bundle

**Mixpanel's own documentation blurs the term, and a reader coming from product analytics will too.**
Mixpanel's Lexicon page states outright, "Lexicon is a data dictionary that stores descriptions of events
and their properties," then describes importing content directly from other vendors' tracking-plan
products into that same "data dictionary": "Import your Segment Plan into Lexicon," and "To import your
data dictionary from Avo.app." Mixpanel treats the two names, "data dictionary" and "tracking plan" or
"Plan," as labels for the same imported artifact under two different product surfaces, not as two documents
separated by subject or by tense. Amplitude's own blog does the same blurring in one sentence: "For user
behavior data, the Data Dictionary or Taxonomy Sheet lists the user actions and descriptions of what each
means."

**This bundle's own Purpose and Boundary section must name that usage and route the reader away from it.**
A reader who searches this library for "data dictionary" meaning the event list that Mixpanel's Lexicon,
Segment's Protocols, or Avo's own tracking plan each already cover should land on `tracking-plan`, not on
this bundle. The Purpose and Boundary section's WHY comment should state this directly, the same way
`tracking-plan`'s own Purpose and Boundary section already rules out four neighbours by name.

**Recommendation for the landing PR, not settled here: give `tracking-plan` the alias "event dictionary."**
No source in this sweep uses that exact phrase, so it would be the library's own choice, for search,
exactly as `business-continuity-plan`'s own spec added two unsourced aliases for the same reason
(`disaster-recovery-business-continuity-plan`'s "Business continuity and disaster recovery plan" and
"BC/DR plan"). The library's own recommendation: add it. This library's own inference is that a reader typing "event dictionary" is most
certainly looking for the event-and-property catalog `tracking-plan` already ships, not for this bundle's
field-meaning document. This is a landing-site edit to a different bundle's catalog row, not an edit this
spec's own catalog corrections make for `data-dictionary` itself; it is listed again under What landing
this bundle closes elsewhere, below, and the maintainer can veto it on reading this spec.

#### Stop rule

**If the worked example's field-level dictionary reads as thin, the build stops, and the decline
alternative (ADR 0073's Considered Option 4) returns to the maintainer.** This is a single test with two
failure readings, both of which this sweep's own confidence work named as live risks:

1. **Duplication, not thinness of prose.** Every field definition in the worked example restates a row
   already present in the tracking-plan catalog or the KPI dashboard's Metric Definitions section, with no
   added field-level fact (a type, a nullability rule, an allowed-value list, a relationship to another
   table) that neither sibling already states. If every row is a restatement, the narrow core this spec
   argues for does not actually exist as separate content, and the honest move is the decline this ADR
   already sketches, not a thinner bundle.
2. **Wrong audience.** The filled example reads as a document a data engineer would write for another data
   engineer, with no field a product manager would ever need to look up (an event's business meaning, a
   metric's input, a privacy flag), rather than a document this library's own readers would reach for.

Neither failure is a row count; stating one would be an invented figure no source in this sweep supports.
Both are a qualitative read of the filled worked example against its two named siblings, done once the
build's own example is drafted, before the build proceeds past it.

#### A deferred, low-value research task for the build's own research phase

**Reading FastSlowMotion's analytics-governance page in a real browser is reserved for the build, not done
here.** Every automated fetch path tried for that page, in this sweep and in the 2026-10-12 gap-fill
targeting it specifically, returned HTTP 403; only a browser-rendered read (not a raw-text-checkable one)
has ever returned its actual content. Its decision value for this bundle is **low**, stated in
`_local/research/2026-10-12_admission-sweep-5/family-question.md` line 533: "if it confirms a split between
a full metric entry and a dashboard snippet, `kpi-dashboard`'s Metric Definitions section already carries
the full entry, so the narrow scope still holds." Reading it would at most corroborate a boundary this spec
already draws on other sources; it would not change the scope decision either way. The build's own
research phase should attempt the browser read once, log whichever of its two possible findings holds, and
move on rather than spend further attempts against a page that has returned 403 to every non-browser path
tried so far.

#### Section design

Drawn from the sources above. No single vendor's exact column list is canonical (see Licences, below), and
the final column set is this library's own tally, converged from several sources rather than copied whole
from any one of them, the same posture `tracking-plan`'s own Structure section took.

| Section | In lean? | What it is, and its sourcing |
|---|---|---|
| **Purpose and Boundary** | yes | What this document covers (the fields of one or more named datasets or tables) and what it rules out by name: event cataloguing (`tracking-plan`'s job), metric-formula locking (`kpi-dashboard`'s Metric Definitions section), the experiment design doc's one-time record, and the event-list sense of "data dictionary" that product-analytics usage (Mixpanel's Lexicon) blurs into this document's own name. Sourced to GDAC's three-way glossary distinction and to the Boundaries subsection above |
| **Field Definitions** | yes | **The load-bearing section.** One row per field: its name, type, definition, allowed values or range, nullability, and owner. Name, type, and definition recur across every admitting source (OSF, Docsie, Basedash, Wizbrand); allowed values and nullability are sourced to Basedash ("the technical facts (name, data type, nullability)" and "Enums, ranges, or units") and to OSF's own retrieval-note tally (not itself a passed quotation; stated here as the library's own convergence, per the same practice `tracking-plan`'s own Structure section used for its single-vendor-sourced columns). A table section, so it carries PRIORITY and ROW HINT |
| **Ownership and Review** | yes | The dataset's or table's own named owner, apart from any individual field, and the review cadence. Sourced to Basedash ("Owners are usually the team that produces the data, not the team that consumes it") and to Wizbrand ("review it on a cadence (monthly or quarterly)"); Docsie's own review-cadence field, "[Monthly / Quarterly / Annual / Event-based]," states no fixed norm, so this section asks the author to name one and say whether it is borrowed or this team's own choice, the same discipline `tracking-plan`'s own Review and Ownership section already applies |
| **Dataset Metadata** | full only | A header naming the dataset or table, its source system, its version, and its effective date, ahead of the field table. Sourced to Docsie's own shipped document skeleton, which opens with a metadata header before its field table, and to Basedash's per-table framing throughout |
| **Relationships** | full only | How this table's fields relate to other tables or datasets: foreign keys, joins, or a field that is itself computed from another table's field. Sourced to Harvard's definition, which describes a data dictionary as outlining "the structure, content, and variable definitions for a dataset or collection of data", implying more than one table is in scope once relationships exist to describe |
| **Validation Rules** | full only | Enum lists, numeric ranges, required-versus-optional fields, and any cross-field rule a loader or a reviewer should check. Sourced to Docsie's own "Required" column and to Basedash's "Enums, ranges, or units" |
| **Review and Sign-off** | full only | A formal record of who reviewed and approved this version, and when, distinct from the shared Ownership and Review section's standing owner and cadence. Sourced to Docsie's own shipped document, which carries a signoff block beyond its basic owner-and-cadence fields, in the same full-only addition shape `tracking-plan`'s own Change Process and Version History section took relative to its shared Review and Ownership section |

The lean variant's three sections, in this order (Purpose and Boundary, Field Definitions, Ownership and
Review), are a strict ordered subset of the full variant's seven, as contract section 3.2 requires. Full
inserts Dataset Metadata between Purpose and Boundary and Field Definitions; Relationships and Validation
Rules between Field Definitions and Ownership and Review; and Review and Sign-off after Ownership and
Review, last. This mirrors the insertion pattern `tracking-plan`'s own lean-to-full growth already uses:
new sections are inserted around the shared ones, never renaming or reordering them.

**This section design is the library's own judgment, not a single source's shipped shape, and the
maintainer may prefer folding Dataset Metadata into frontmatter instead of a full-only section; this spec
states a recommendation the build can still reconsider against the family's own nesting rule.**

#### Catalog corrections the landing PR must make

Per [decision-procedures.md procedure 1](decision-procedures.md#1-a-catalog-call-loses-to-research), both
`docs/internal/catalog.md:208` and `atlas/catalog-data.json` (index 140), then regenerate the atlas, for
each correction accepted:

- **Alias "metric definitions" collides exactly, case-insensitively, with `kpi-dashboard`'s own shipped
  "## Metric Definitions" H2 heading.** A catalog search on that alias today would return the wrong
  artifact once this bundle ships. **Recommend dropping it.**
- **Alias "data catalog entry" names a different, related concept this sweep found independently
  defined.** GDAC's own glossary names a Data Catalogue as "An inventory of available data assets supported
  by a collection of metadata," distinct from a Data Dictionary, and lists each under "Confusion over
  definition and with related concepts" on its own page. **Flag it for the spec author or reviewer; do not
  drop or keep it without a decision**, the same posture `tracking-plan`'s own landing took for its
  contested aliases.
- **The purpose field, "Document the meaning and usage of events and metrics," contradicts the narrow
  scope this sitting approved.** "Events" names `tracking-plan`'s own subject; "metrics" names
  `kpi-dashboard`'s Metric Definitions subject. Neither belongs in this bundle's purpose statement.
  **Recommend** a purpose statement naming what the fields of a dataset or table mean, so that different
  teams compute the same number from them, matching the contract's own amended purpose clause.
- **The contents field, "event name, description, properties, usage, owner," is event-shaped, not
  field-shaped.** It describes a tracking-plan row, not a data dictionary row. **Recommend** a contents
  field naming the field name, type, definition, allowed values, and owner, matching the admitting
  sources' own convergent column set (see Section design, above).
- **`owner: "Data / Analytics Eng"` is well supported and needs no change.** Basedash states the role
  directly: "Owners are usually the team that produces the data, not the team that consumes it." **No
  change recommended.**
- **`stage: "measurement"` should not be corrected**, on the same reasoning `tracking-plan`'s own landing
  gave for its identical field: the catalog's descriptive `stage` is a different question from the
  metadata schema's `phase`/`classification` axis, which this bundle settles independently as
  `classification: utility` in its own `meta.yaml`. **No change recommended.**
- **`size_variant: "S/M"` matches the maintainer's own settled two-size decision and needs no correction**,
  beyond the mechanical step every other `governance-docs` member's landing has taken: setting
  `sizes_available: [lean, full]` in `data-dictionary_meta.yaml` directly, independent of the catalog's own
  shorthand marker.
- **`methodology: "methodology-agnostic"` is not contradicted and should stand.** The admitting sources
  span research-data, enterprise-data-management and product-analytics lineages with no single
  methodology thread running through all of them. **No change recommended.**
- **Relationships: `[Tracking Plan]` should gain `KPI Dashboard`.** The boundary this spec draws against
  the KPI dashboard's Metric Definitions section is as load-bearing as the one against the tracking plan,
  and the catalog's relationships field today names only one of the two. **Recommend adding `KPI Dashboard`
  to this bundle's own relationships field.** `tracking-plan`'s own relationships field, `[Data Dictionary,
  Dashboards]`, already names this bundle and needs no further edit for this bundle's own sake.
- **Formality (`standard`) and rarity (`occasional`) are not contradicted by anything retrieved and can
  stand as-is.**

#### `pairs_with`: checked, empty

`gh api repos/product-on-purpose/pm-skills/contents/skills --jq '.[].name'` returned 68 skill names on
2026-10-14, the same count `business-continuity-plan`'s own landing found on 2026-10-13. No name contains
"dictionary," "glossary," or "catalog" against this type; the closest adjacent name,
`measure-instrumentation-spec`, is an instrumentation plan, the per-feature neighbour this library has
already placed outside this bundle's scope. **`pairs_with: []`**, under the contract's rule for that field:
"Verify per member; claim only what is true of that member" (quoted from `standing-standards.md:74`, the
same clause `business-continuity-plan`'s own spec cites for this check, since `governance-docs.md` states
the identical obligation without repeating the sentence verbatim).

#### Risks for the build and the review

1. **The tense-boundary reversal is the central risk, and the companion must carry it, not smooth it
   over.** A companion written as though the subject-based boundary were the library's first and only
   reading overstates how settled this question is, and a companion that keeps citing only Wizbrand's tense
   line, as `tracking-plan`'s own shipped companion still does, understates what the 2026-10-14 research
   found. State both: the subject-based line this bundle is built on, and the tense-based line a sibling
   bundle still carries, with a note that the two are not the same claim.
2. **The product-analytics usage collision is a live routing risk, not a footnote.** Mixpanel's own
   documentation uses "data dictionary" for exactly the event-list content `tracking-plan` already ships.
   A Purpose and Boundary section that does not name this directly will field support questions from
   readers who wanted `tracking-plan` and found this bundle instead, or the reverse.
3. **The Field Definitions column set is this library's own convergence, not any one vendor's shipped
   list, and must be labeled as such.** OSF's seven-column structure is a retrieval note's own tally, not a
   passed quotation; stating it as if OSF itself published exactly those seven words invents a citation
   this sweep does not support.
4. **No licence was found for any of the four vendor templates read** (Amplitude, Docsie, Wizbrand,
   Basedash). OSF's own page is CC0, and GDAC's UK government content carries no explicit licence
   statement on the page itself. Do not adapt column names or wording from any one vendor's page verbatim,
   and do not state or imply a licence for Amplitude, Docsie, Wizbrand or Basedash.
5. **The shared-scenario rule binds hard here, exactly as it does for every `governance-docs` member.**
   The worked example must chain onto facts the `tracking-plan` and `kpi-dashboard` examples already state,
   and must not invent a parallel warehouse, a parallel event set, or a parallel owner. See The worked
   example, below, for the facts it must agree with.
6. **The build workflow's templates stage has repeatedly copied the worked example's own scenario into the
   template's GOOD and WEAK text.** Once an example exists, grep the drafted templates for its proper nouns
   before review, the same practice `tracking-plan`'s, `business-continuity-plan`'s and
   `north-star-metrics`'s own specs each name.
7. **The stop rule is a qualitative read, not a number, and must stay that way through review.** A reviewer
   who reduces the stop rule to a row count, a word count, or any other invented figure is replacing the
   test this spec states with one no source supports.
8. **`FastSlowMotion`'s page is reserved for one browser read during the build's own research phase, and
   its finding must not be over-weighted.** Its decision value is low, named as such in this spec's own
   deferred-task subsection; a build that treats a confirming read as settling the scope question, rather
   than merely corroborating it, is giving one low-value source more weight than this spec's own reasoning
   assigns it.

#### The worked example: the warehouse tables the tracking plan and the KPI dashboard already imply

**The shared-scenario rule (contract section 4) applies.** The example must carry the same Acme Analytics
Reporting Platform Modernization program every other `governance-docs` member's example uses, and it must
document fields the `tracking-plan` and `kpi-dashboard` examples already imply exist, rather than invent a
parallel dataset.

**`tracking-plan_example.md`'s own Purpose and Boundary section names the gap this example fills**: "It is
not the data dictionary, the document that will state what the data in these events' destination tables
actually means once it is implemented, which this program has not yet written." Those destination tables
are named in the same example's frontmatter and body: events land in Amplitude, and the executive view is
built in Looker (`tracking-plan_example.md:6`, `kpi-dashboard_example.md`'s own frontmatter note, "the live
dashboard is implemented in the Acme BI workspace (Amplitude for product events, Looker for the executive
view)"). Between Amplitude and Looker sits a warehouse those product events land in before Looker reads
them; this example's natural subject is that warehouse table (a fact table of Saved Views and report
events) and the dimension tables its foreign keys point to (an analyst dimension, an account dimension),
not a second copy of either vendor tool.

**Fields this example may document, each one already implied by a sibling fact rather than invented
fresh:**

- The nine events `tracking-plan_example.md`'s own catalog already names (`view_saved`, `view_switched`,
  `view_set_default`, `view_shared`, `view_load_error`, `report_opened`, `report_exported`,
  `report_shared`, `report_annotated`) land as rows in an events fact table. This bundle's own Field
  Definitions entry for that table documents the table's columns, such as `event_name`, `occurred_at`,
  `dashboard_id`, `report_id`, and `recipient_user_id`, not the business reason each event fires; that
  reason stays the tracking plan's own "why" column, and this bundle must not restate it.
- `tracking-plan_example.md`'s own Privacy, Sensitivity and Retention section already states that
  `recipient_user_id` on `view_shared` and `report_shared` is "pii_flag: true" and "Hashed on the way into
  the warehouse". This bundle's own Field Definitions row for that column documents it as hashed, not
  plaintext, agreeing with that sibling fact rather than restating or contradicting it.
- `tracking-plan_example.md`'s own User and Account Properties table already names `analyst_segment` (user)
  and `migration_reconciled` (account) as traits "Set from the entitlements database" and "Set by the
  migration reconciliation job at cutover." This bundle's own dimension-table entries for an analyst and an
  account dimension document those same two fields, agreeing on their type and source rather than
  re-deriving them.
- `kpi-dashboard_example.md`'s own Metric Definitions section states the Time to Insight formula reads
  "timestamp of first logged action on a report" against "timestamp the report was opened". This bundle's
  own Field Definitions entry may name which warehouse column each of those two timestamps is (for example,
  the fact table's own `occurred_at` column, filtered to the relevant event names), without restating the
  formula itself; the formula stays `kpi-dashboard`'s own job.
- The data steward named across `tracking-plan_example.md`'s Event and Property Catalog, **Lee Zhang (Data
  Eng)**, is the natural per-table owner for this bundle's own Ownership and Review section, agreeing with
  the sibling rather than naming a second steward for the same warehouse.

**Dates.** `tracking-plan_example.md` is dated 2026-08-24 and states the program "has not yet written" the
data dictionary. This bundle's own example must be dated after 2026-08-24, and its own version history (in
the full variant's Review and Sign-off section) must not show an entry predating that date, so the two
examples agree on when this document starts existing.

**What the example must not do.** It must not restate the tracking plan's own "why" column for any event,
must not restate the KPI dashboard's own metric formulas, inclusions, or exclusions, and must not invent a
third warehouse, a third tool, or an owner not already named in a sibling example. Per the stop rule above,
if drafting this example surfaces no field-level fact beyond what the two siblings already state, the build
stops rather than ship a document that restates its neighbours under a new heading.

#### Metadata

| Field | Value | Why |
|---|---|---|
| `family` | `governance-docs` | By ADR 0073, a second widening of the contract's purpose phrase |
| `classification` | `utility` | The only value the contract's axis allows; argued in ADR 0073 from the document's maintained, revised-as-the-schema-changes cadence |
| `bundle_id` | `data-dictionary` | Same as the catalog id; no reason found to differ |
| `sizes_available` | `[lean, full]` | The maintainer's settled sizing: lean carries the core field table, full adds a metadata header, relationships, validation rules, and a review-and-signoff section |
| `status` | `beta` | Every bundle |
| `methodology` | Set at build from the admitting sources' lineage | The catalog's `methodology-agnostic` is not contradicted (catalog correction above leaves it unchanged) |
| `pairs_with` | `[]` | Checked against pm-skills `origin/main`, 2026-10-14; no skill produces or consumes this type |
| `related_templates` | `[tracking-plan, kpi-dashboard]`, inline | The two neighbours this spec's own Boundaries section draws against, and the two the catalog's own relationships field should name after the correction above |
| `aliases` | Carried forward from the catalog once the corrections above are applied; "metric definitions" dropped, "data catalog entry" flagged for a reviewer decision rather than kept or dropped by this spec | See Catalog corrections, above |

#### What landing this bundle closes elsewhere

1. **The `governance-docs` contract's Members line**, from not yet built to the build date. The contract
   moves to `0.5.0` in the spec PR, with ADR 0073.
2. **`tracking-plan_example.md:50-51`'s own sentence, "this program has not yet written" [a data
   dictionary], becomes false the moment this bundle's worked example exists.** Whether that example's
   sibling sentence is edited to point at the new example, or left as a dated fact about the state of the
   program at the time it was written, is a build decision this spec does not make; either choice should
   be stated plainly in the build's own report, not left for a reader to notice the contradiction.
3. **`tracking-plan_companion.md:90-104` and `:395-399`, and `tracking-plan_template-lean.md:69-76` /
   `tracking-plan_template-full.md`'s matching lines, still draw the tracking-plan/data-dictionary boundary
   on Wizbrand's tense line alone.** This spec recommends a dated note on that text, in the shape the
   contract's own `0.4.0` and `0.5.0` change notes use, stating that the 2026-10-14 research found a second
   source and a subject-based reading, rather than a rewrite of text that is not itself wrong, only no
   longer the soundest statement available. This is a recommendation, not a required edit; the maintainer
   may veto it on reading this spec.
4. **`experimentation-docs.md:42-45`'s own boundary sentence could gain a pointer to ADR 0073**, the same
   way its existing sentence already points at ADR 0067 for the tracking plan. This is a small, optional
   edit, not required for this bundle's own gate to pass.
5. **The catalog entry**, per the corrections above, in both `docs/internal/catalog.md` and
   `atlas/catalog-data.json`, then the atlas regenerated.
6. **This page's Progress table**: the `data-dictionary` row's Built column, and an inline dated note in
   the 2026-10-13 sweep paragraph.
7. **Recommended, not required: `tracking-plan`'s own catalog aliases gain "event dictionary."** See
   Routing a product-analytics reader, above. This is a different bundle's catalog row, so it is listed
   here rather than in this spec's own catalog corrections, and the maintainer can accept or veto it
   independently of this bundle's own landing.
8. **Issue #255 (bundle: data-dictionary) relabels to `status:built` with the build PR**, not with this
   spec's own PR, which only proposes the amendment.
9. **This page's own `tracking-plan` spec text.** Its Purpose and Boundary design row calls this type "the
   unbuilt data dictionary", and its "Not the data dictionary" boundary rests on Wizbrand's tense-based
   account. Both want a dated note at the build, pointing here.

*(2026-10-15, at the build: items 1, 5, 6, 7 and 9 are done as written. Item 2: the sentence stays as a
dated fact, because the tracking plan's example is dated 2026-08-24 and this bundle's example 2026-09-08,
so it was true on the day it describes; the tracking plan's history records the choice. Item 3: the
companion's two passages carry a dated note, and the templates' guidance comments are unchanged, so the
tracking plan's version stays 0.1.0 with a dated correction in its history. Item 4 is not done: it would
edit a family contract, and every contract edit stops for the maintainer's read. Item 8 follows the PR.
The line citations to the tracking plan's companion in this subsection and the two above it were remapped
to the passages' current lines, because the build's own dated note shifted them, and the first had already
stopped one line short.)*

#### What the build would cost

No build has run for this type. This is projected from the family's own two most recently built members,
both single-size-equivalent two-size builds with every agent resolved to Sonnet, measured in
[`bundle-builds/INDEX.md`](../../bundle-builds/INDEX.md): `tracking-plan` cost $14.88 whole (7,440,790
weighted tokens, 15 agents, 3 rounds), and `change-log` cost $16.95 whole (8,472,610 weighted tokens, 15
agents, 3 rounds). `issue-log`, the family's other single-size build, cost $14.29 whole (7,143,159
weighted tokens). A whole-bundle estimate of **$14 to $20 at API list rates** is reasonable on that basis,
toward the higher end if the full variant's four additional sections (Dataset Metadata, Relationships,
Validation Rules, Review and Sign-off) need more drafting rounds than a single-size member did. It is a
projection, not a measurement, until `python tools/gen-bundle-build-report.py --ingest` runs against an
actual build report.

### standing-standards (seventh member): the test strategy, for an organization or program

**`test-strategy`** (bundle id; the catalog id stays `test-strategy`, since the two already match) -
`standing-standards` (the maintainer's ruling of 2026-10-13), **`classification: foundation`** (recommended;
argued in [ADR 0075](decisions/0075-test-strategy-joins-standing-standards-as-a-foundation.md)), sizes **`[lean]`**
(single size, argued below), methodology `methodology-agnostic` (catalog's own value, not contradicted by
any admitting source), catalog id `test-strategy` (catalog 103 in [`catalog.md`](catalog.md); atlas index
102 in [`atlas/catalog-data.json`](../../atlas/catalog-data.json)). Catalog owner: `QA Manager` (flagged,
not corrected, below). Catalog purpose (flagged below): "Define organization-wide testing approach and
standards." Catalog contents: "levels, types, tools, environments, governance." Catalog `category`:
"QA / Test". Catalog `stage`: "testing". Catalog `formality`: "standard". Catalog `rarity`: "occasional"
(flagged, not corrected, below). Catalog `size_variant`: "M" (corrected below to a single size). Catalog
`relationships`: "parent of Test Plans". Issue #260 (bundle: test-strategy) tracks this build.

This spec follows the model the maintainer named most recently in this family: the `business-continuity-plan`
spec (standing-standards, sixth member), for structure, depth and tone, and adds the data-dictionary spec's
newer convention of a one-size "Section design" table with sourcing in the same column as the section's job.

#### Demand: a routing row and a frontmatter field, in one already-shipped sibling

No `future:` tag names this type. A grep of every tracked file under `templates/` and `docs/internal/` for
"test strategy" or "test_strategy", run 2026-10-16, returns matches only inside `templates/test-plan/`.
The demand is prose, already shipped, inside that one sibling, not a promise tag:

- `templates/test-plan/test-plan_guide.md:36` routes a reader directly here, inside its own "Plan,
  strategy, case, or report?" table: "How this organization tests, in general, across projects" maps to "A
  **test strategy** (standing, rarely changes)". No bundle exists yet for that routing target.
- `templates/test-plan/test-plan_guide.md:41-43` names the scope question this spec settles: "the certification
  bodies put strategy at the organization or programme level, plenty of teams carry it as a section inside
  the plan, and practitioners openly disagree about which is written first."
- `templates/test-plan/test-plan_template-full.md:7` ships a dedicated frontmatter field,
  `test_strategy_ref`, whose only job is to let a filled test plan point at a standing strategy, or declare
  there is none. `test-plan_example.md:7` fills it today: "None. Acme Reporting has no standing test
  strategy document; the Risk-Ranked Approach below is the strategy for this release." That sentence stays
  true at the test plan's own date, 2026-07-06, and this spec does not ask it to change. See the worked
  example below for how a later-dated test strategy coexists with it.
- `templates/test-plan/test-plan_template-full.md:99-106`'s "Test Levels and Types" section and the plan's
  own Risk-Ranked Approach section already do this content's job at the per-project level, when no standing
  strategy exists. This spec's own Boundaries section states exactly how this bundle differs from both.

This is the same shape the `business-continuity-plan` spec found for its own demand: real routing, already
shipped, not a gate obligation. No check fails today for leaving this type unbuilt.

#### Admission: three independent sources, at a cost the research names plainly

Every quotation below passed the recheck against raw source text, filed in one of three checked files:
`_local/research/2026-10-12_admission-sweep-5/recheck-out.json`,
`_local/research/2026-10-14_prep-research/recheck-out.json`, or
`_local/research/2026-10-15_sitting-followup/test-strategy-recheck-out.json` (all gitignored).

**ISTQB's glossary clears admission, with a caveat about where it was read.** An unofficial mirror,
`istqb-glossary.page`, serves the identical definition text under both its "test strategy" and
"organizational test strategy" entries: "A high-level description of the test levels to be performed and
the testing within those levels for an organization or programme (one or more projects)." That span passed
the recheck. The mirror is not ISTQB's own `istqb.org` or `glossary.istqb.org` domain, so a build that wants
the official page should fetch it directly rather than carry this citation forward unchanged. The same
mirror's worked illustration also passed: "An organization that develops and maintains an e-commerce
platform defines a test strategy stating that all projects will perform component, integration, system, and
acceptance testing." *(2026-10-20: the build read ISTQB's official glossary through the API behind its page, and the official definition differs: "A strategy that describes the generic requirements for testing and how to perform testing within an organization." It carries no "programme" or "one or more projects" wording, so the hedge quoted above is the mirror's older text, not ISTQB's current one. The program half of the 2026-10-15 scope ruling now rests on published program strategies: Ofgem's, TfL's, DCC's, and the Fujitsu and Post Office HNG-X testing strategy. See [`test-strategy_research-log.md`](../../templates/test-strategy/test-strategy_research-log.md), Findings 1 and 2.)*

**Process Street publishes the type as a produced, distributed written artefact, on four passing steps.**
All four of its steps quoted by the 2026-10-12 sweep pass the recheck: "Identify objectives of the test
strategy document", "Distribute finalized test strategy document to relevant stakeholders", "Identify test
entry and exit criteria" and "Develop risk mitigation strategy". The page's other steps were never
raw-checked, so this spec paraphrases them and does not quote them. No licence is stated on the
page, so nothing from it may be copied into a template verbatim; it may only inform section naming.

**ISO/IEC/IEEE 29119's own glossary text is weaker than Wikipedia's account of it.** On the imbus mirror of
the 2013 edition, every sentence containing the word "document" failed the recheck, including the sentence
most often quoted for this type. What did pass: "it provides detail on how the testing is to be performed.
It is aligned with the Organizational Test Policy," "An organisation could have more than one Organizational
Test Strategy to cover markedly different project contexts," and "The test strategy is a distinct entity
from the Organizational Test Strategy." Wikipedia's secondary account of the standard's Part 3 structure
passed independently: "Organizational Test Strategy" and "Test Plan (including a Test Strategy)" are named
as separate outputs. **The standard's own current clause text was never reached by any automated fetch in
either research dimension** (iso.org, IEEE Xplore, an iTeh mirror and an ANSI preview page each returned a
403, a paywall or a JS-rendered empty page), per the 2026-10-14 critic's own finding. No sentence in this
spec or its companion may cite ISO/IEC/IEEE 29119-3's own text; every reference to it is to a secondary
account, labelled as secondary.

**One dimension of this sweep's research was lost and later recovered.** The 2026-10-12 admission sweep ran
two research dimensions for this type instead of the usual three; the dedicated named-sources dimension
never ran. A 2026-10-14 follow-up ran it. It found ISTQB's own current (2024) Advanced-Level syllabus,
which passed the recheck on five spans, including "Throughout this syllabus, the organizational test
strategy is taken as given," "A project test strategy (referred to as a "test strategy" in the
ISO/IEC/IEEE 29119-3)," and "it focuses on test management at the project level and not test management at
the organizational level." **That syllabus also names a renaming risk this spec does not resolve**: it
states the organization-level artefact is now "referred to as an "organizational test practice"" in the
standard it teaches toward, which, if true of the current standard's own text, would mean the strongest
org-level sources in this admission case (Wikipedia's account, and an academic 2009 slide deck on a then-draft
of the standard) describe a name the standard may have since dropped. This is recorded as an open question,
not settled here.

**Admission clears on three independent sources, at ADR 0048's one-source bar, several times over.** ISTQB's
glossary (even read through an unofficial mirror), Process Street's own template, and Wikipedia's secondary
account of ISO/IEC/IEEE 29119's structure each independently publish the type as a written document. No
single one of the three needs the others to clear the bar.

#### Scope: organization or program, the maintainer's ruling of 2026-10-15

**The scope question was undecidable from the admission evidence alone.** A 2026-10-14 family-fit critic
found strong, direct, mostly primary evidence that a test strategy is written at program scope (Ofgem's two
Switching Programme documents, TfL's Schedule 4 procurement contract), against evidence for a whole-organization
reading that is real but thinner and more secondary (Wikipedia's account, a 2009 academic slide deck
describing a draft standard, a vendor guide, one unpublished HMRC blog claim). The critic's verdict line was
"undecidable." It also found that `standing-standards.md` section 1's own membership clause, "agreed once
and applied every time... consulted repeatedly without being rewritten," never says "the whole
organization," so an org-wide-only cut is a gloss layered on top of the contract rather than something its
text requires.

**The maintainer ruled on 2026-10-15: the test strategy is scoped to an organization or program, "a
standing strategy used across more than one project," after a follow-up found that no source scopes a test
strategy to a portfolio.** That follow-up checked `istqb-glossary.page`'s own text (hedging "organization or
programme"), ISO/IEC/IEEE 29119-1's own wording (naming only "organization," never "programme," on the
passing fragments above), and government, procurement and job-posting sources for "portfolio" usage. *(2026-10-20: the "organization or programme" hedge is the mirror's older text, not ISTQB's current definition; see the dated note in the admission section above. The 29119-1 wording was read through imbus's secondary account, not the standard itself, which no fetch reached.)*
**No source anywhere in the follow-up scopes a test-strategy document itself to a portfolio.** The one
verified source that uses both words, an Australian public-service job posting (passed recheck), ties the
Test Strategy artefact to "program" scope and reserves "portfolio" for a separate, higher departmental level:
"Manage program testing activities that are correctly prioritised to deliver outcomes that align to the
Departments priorities," and lists Test Strategy among that role's own artefacts, "not limited to Test
Estimation, Test Schedule, Test Strategy, Test Plan, Test Execution Reports, Defect Modelling Reports, and
Test Summary Reports." Per PMI and APM's own definitions, also checked and passed, a portfolio sits above a
programme, as "a collection of projects or programs and other work that are grouped together," whose parts
"may not necessarily be interdependent or directly related." Swapping "portfolio" in for "programme" would
have silently widened this bundle's scope past what the maintainer asked for.

**Spelling: "program" in this library's own voice, "programme" only inside a quotation.** The follow-up
found the library's own original prose (not quoting a source) mostly spells it "program": `test-plan`'s own
Acme example, and the shipped placeholder and guidance text in `status-report`, `raid-log`, `risk-register`
and `kpi-dashboard`, all do. "Programme" in this library's shipped text clusters almost entirely inside
direct quotations of British sources, chiefly ISTQB's glossary and `test-plan_guide.md:42`'s own paraphrase
of "the certification bodies." The library's `organization`-to-`organisation` ratio, 447 to 131 across the
tree, confirms American spelling is the house default. This spec's own prose follows that: "program," never
"programme," outside a quotation mark.

**Why not the per-project sense, again, stated plainly.** The per-project sense of a test strategy is
already shipped, inside `test-plan`'s own Test Levels and Types section and Risk-Ranked Approach section,
and is the sense `test-plan`'s own `test_strategy_ref` field exists to distinguish from a standing one. This
bundle builds only the organization-or-program sense: standing, consulted by more than one project, not
authored per release.

#### Family fit: `standing-standards`, `foundation`, and the third member no forecast named

**Membership is the family's own falsifier, the same one every prior member faced.** A standing test
strategy that one or more projects inherit from, and that a project's own test plan either follows or states
a reasoned deviation from, is consulted at the moment each of those projects' plans is written. Ofgem's own
language, which passed the recheck, states exactly this relationship: "This testing strategy will be
followed by a more detailed programme level Testing Management Plan," and a second Ofgem document adds "a
detailed, programme level Testing Management Plan should be developed during DLS to define the detailed
testing approach for each test phase." A strategy written for one project after the fact, with no further
project ever consulting it, would be the family's own excluded case, the contract's analogy at
`standing-standards.md:37`: "a runbook written for one incident is an incident report." This bundle is the
standing strategy; a filled instance that only ever served one project's own test plan is a different,
narrower artefact this bundle does not template.

**Classification: `foundation`, argued marker by marker, the same method ADR 0058, ADR 0062 and ADR 0071
each used.** The full argument, with the honest `tool` case stated and rejected, is in
[ADR 0075](decisions/0075-test-strategy-joins-standing-standards-as-a-foundation.md). In short: a test
strategy's levels, types, tools and governance are a standard every project's own plan is judged against
or states a reasoned deviation from, changed deliberately and rarely, which Software Testing Help's own
passing quote supports directly: "Test strategy usually will not change once approved." On this library's
own inference, since no research dimension tested it, nobody executes it under time pressure the way a
runbook or a business continuity plan is executed once a disruption or a launch is underway. It is the organization-or-program-level mirror of `definition-of-done`, which is also
`foundation`.

**Why not `qa-docs`, in that contract's own words.** `qa-docs.md` section 1 admits a type whose job is to
"plan, specify, or report the verification of a product increment." Section 2 states the phase case
instrument by instrument: "A test plan is written per release and closed at its exit criteria... Each is
produced at a stage and finished, which is the definition of a phase artifact." A standing, organization-
or-program-level test strategy, read in that sense, is none of these: it is not written per increment, not
closed at any one release's exit criteria, and not finished at a stage. The 2026-10-12 research scored this
reading `excludes` against `qa-docs`, cleanly, for exactly this reason. (The per-project sense would
admit-with-strain, per that same research; this bundle does not build that sense, so the strained reading
never arises here.)

**This is the family's third unforecast member.** `standing-standards.md:46` names only "a coding-standards
or engineering-handbook document" as a likely future member, checked directly against the contract's
current text. Neither a test strategy nor anything resembling one appears there. `production-readiness-
review` (ADR 0062) was the family's first unforecast member and `business-continuity-plan` (ADR 0071) its
second. The same principle both of those records state, from
[ADR 0057](decisions/0057-issue-log-joins-governance-docs-as-a-fourth-member.md), governs here too: "The
membership test, not the list of members that happened to be planned in 2026-07, governs a candidate." This
does not weaken admission. It does mean ADR 0075, like ADR 0062 and ADR 0071 before it, cannot claim a
confirmed forecast.

**The scope ruling interprets the contract's silence; it does not amend the contract's text.** Section 1's
membership clause never says "organization-wide," so the maintainer's organization-or-program ruling reads
a clause that was always open to it, rather than widening a clause that excluded it. This differs from
`business-continuity-plan`'s own admission, where no comparable scope ambiguity existed inside the
contract's own words; ADR 0075 records this as the one respect in which this admission's reasoning differs
from ADR 0071's, even though both conclude a record is needed for the same underlying cause, an unforecast
member whose classification has to be argued.

**The cadence tension, again, routed to Review Trigger rather than resolved by amendment.** Section 1 states
members are "not revised on a calendar." Two sources describe a test strategy as something that is itself
periodically revised: TestRail's "A long-term document that evolves with the organization's needs and
growth" and ReqTest's "The test strategy is a living document and evolves over time." A third source cuts
the other way: Software Testing Help's own "Test strategy usually will not change once approved." **This
spec does not propose a contract amendment to resolve the tension.** Instead, the bundle's own Review
Trigger section, mandated by contract section 4 of every member, states named conditions rather than a
calendar, the same discipline every prior member in this family uses. ADR 0075 records the tension as a
consequence of this admission, as ADR 0062 and ADR 0071 each did for their own members.

#### Boundaries: six neighbours, each stated in that neighbour's own words

- **`test-plan`: the sharpest boundary, and the one this bundle hands off to.** A test plan is scoped to one
  release and is written per increment; a test strategy is standing and spans more than one project. The
  seam is the shipped `test_strategy_ref` field: a plan that inherits from this strategy names it there, and
  states any reasoned deviation from the strategy's levels, types or tooling inside its own Risk-Ranked
  Approach section, rather than this bundle restating either section's content.
- **`definition-of-done`: the closest sibling in form, different in subject.** Both are standing, both are
  `foundation`, both are agreed once and consulted repeatedly. A Definition of Done is a standard every
  increment is judged against, in any discipline; a test strategy is the standing testing-specific standard
  every project's own verification approach either follows or states a deviation from. Neither replaces the
  other; a team may hold both.
- **The qa-docs family (`test-plan`, `test-case`, `test-summary-report`, `bug-report`): a phase boundary, not
  a subject boundary.** Every member of that family plans, specifies or reports the verification of one
  product increment, authored at a stage and finished. This bundle is none of those three things: it is not
  authored per increment and is not finished at any one stage. `qa-docs.md` section 1's own exclusion clause
  draws this line, quoted above.
- **`production-readiness-review`: a different standing instrument, at a different moment.** The PRR asks
  whether one service is ready for standing production ownership to change hands; this bundle sets the
  testing approach every project in scope follows. The PRR's own Readiness Criteria may ask whether a
  project's testing conformed to this strategy, where one exists, without this bundle restating any PRR
  criterion.
- **`definition-of-ready`: an entry-side standard, not a testing-approach standard.** A DoR governs when a
  backlog item is ready to enter a sprint; this bundle governs how testing is approached once work is
  underway. Neither gates the other.
- **The `qa-docs` family contract itself: why the organization-or-program sense is not one of its members.**
  `qa-docs.md` admits a type only if its job is to "plan, specify, or report the verification of a product
  increment" (section 1) and only where the type is "produced at a stage and finished" (section 2). An
  organization-or-program-level test strategy is consulted by many increments across more than one project
  and finishes at none of them, which is the opposite of what that contract's own words require. The
  2026-10-12 research scored this reading a clean `excludes` against `qa-docs`, with no strain needed to
  reach that verdict, unlike the per-project sense's own `admits-with-strain` reading of the same contract.

#### The staleness mechanism: a Review Trigger, the same obligation every member carries

Contract section 4 requires every `standing-standards` member to ship "a review trigger with a named owner
and a condition, not a calendar reminder." `definition-of-done`'s own Review Trigger is a two-field pair,
Trigger and Noticed by, naming an event such as a criterion waived repeatedly. `business-continuity-plan`'s
own Review Trigger is a three-column table, Condition, Owner, and What They Do About It, because that
bundle's own research named several distinct named conditions rather than one. This bundle's own content
argues for the table shape, for the same reason: more than one named condition is already evidenced, and
none should read as the headline rule over the others.

Candidate conditions, drawn from the sources above and labelled as this library's own synthesis where no
single source names the condition outright: a project's own test plan records a deviation from this
strategy's levels, types or tooling in its `test_strategy_ref` field or its Risk-Ranked Approach section,
which is this strategy's own inheritance mechanism signalling a possible drift; the organizational or program
test policy this strategy is "aligned with" (imbus's passing phrase) changes; a test summary report shows a
strategy-mandated level or type was skipped on a real release, which is this strategy's own failure mode
surfacing downstream rather than being noticed at the strategy itself; or a new test level, tool or
environment is adopted across more than one project without this document being revised to say so. The
annual or periodic review language TestRail and ReqTest both use is this document's own named cadence
restated as a floor under the condition-based trigger, not a calendar rewrite of its content, the same
reading `business-continuity-plan`'s own Review Trigger section gives NIST's and the FFIEC's annual-review
language.

#### Section design

Single size, so there is no lean column. Drawn from Process Street's own 20-step structure (four of its
spans passed the recheck; the rest are paraphrased), ISO/IEC/IEEE 29119-1's own content note for the
project-level strategy (read via the imbus mirror's structural listing, not quoted, since the clause text
itself did not pass), the catalog's own "levels, types, tools, environments, governance," and Ofgem's own
two documents' structure. No single source gives one canonical section list for the organization-or-program
sense, so the groupings below are this library's own judgment, sourced per row.

| Section | What it is, and its sourcing |
|---|---|
| **Purpose and Scope** | What counts as "this organization or program" here, which projects it binds, and what it explicitly leaves to each project's own test plan. Sourced to Process Street's "Identify objectives of the test strategy document" (passed) and to the scope discussion above |
| **Test Levels and Types** | The levels (unit, integration, system, acceptance) and types (functional, performance, security, and so on) every project in scope inherits unless its own plan states a reasoned deviation. Sourced to the catalog's own content note and to ISO/IEC/IEEE 29119-1's structural content list, read from the imbus mirror's listing rather than quoted |
| **Standard Tooling and Environments** | The tools and environments every project is expected to use by default. Sourced to the catalog's own "tools, environments" phrase and to Process Street's own environment-and-tools step, paraphrased, not quoted, since no recheck covers that step |
| **Governance and Policy Alignment** | How this strategy relates to any higher test policy, where one exists, and who approves a change to the strategy itself. Sourced to ISO/IEC/IEEE 29119-1's own passing fragment, "it provides detail on how the testing is to be performed. It is aligned with the Organizational Test Policy" |
| **How Project Test Plans Inherit or Deviate** | The seam with `test-plan`'s own `test_strategy_ref` field: a project names this strategy there, inherits its levels, types and tooling as the default, and states any deviation with its reason. Sourced to Ofgem's own passing language, "This testing strategy will be followed by a more detailed programme level Testing Management Plan," and "a detailed, programme level Testing Management Plan should be developed... to define the detailed testing approach for each test phase" |
| **Roles and Responsibilities Across Projects** | Who owns this document at the organization-or-program level, distinct from who executes testing on any one project. Sourced to Process Street's own approval and distribution steps, paraphrased except where quoted above, and to the Australian government posting's passing language tying a Test Strategy artefact to "program" testing activities |
| **Review Trigger** | **Contract-mandated** (section 4), a table of named conditions, owners and actions, per the staleness mechanism above |

#### Catalog corrections the landing PR must make

Per [decision-procedures.md procedure 1](decision-procedures.md#1-a-catalog-call-loses-to-research), both
`docs/internal/catalog.md:161` and `atlas/catalog-data.json` (index 102), then regenerate the atlas:

1. **`size_variant: "M"` becomes a single size, `[lean]`.** Re-checked directly against this sweep's
   research rather than carried forward unread: neither the 2026-10-12 sweep nor the 2026-10-14 follow-up
   names a source describing a short form and a long form of a test strategy. Every structure found, Process
   Street's 20 steps, ISO/IEC/IEEE 29119-1's own content list, Ofgem's own testing-scope structure, the
   catalog's own content note, is one comprehensive shape. **Recommend** `sizes_available: [lean]` in the
   build's own `test-strategy_meta.yaml`, independent of this catalog correction.
2. **`purpose: "Define organization-wide testing approach and standards"` becomes "Define the testing
   approach and standards an organization or program applies across its projects."** The maintainer's
   2026-10-15 ruling is organization-or-program scope, not organization-wide-only; "program" is spelled in
   the library's own house voice rather than "programme." **Recommend.**
3. **Alias `"test approach"` is flagged for the landing PR to route elsewhere, not kept here.** Inside this
   library, "approach" already names the per-project sense: `test-plan`'s own full-variant section is named
   "Risk-Ranked Approach," and `test-plan_guide.md:44-45` states plainly, "your Risk-Ranked Approach section
   **is** your strategy for this release." A reader typing "test approach" is, by this library's own
   vocabulary, more likely searching for that per-project section than for this standing document.
   **Recommend dropping the alias here and considering it for `test-plan` instead, as a separate,
   maintainer-vetoable landing-site edit**, the same posture the `data-dictionary` spec took toward giving
   `tracking-plan` the alias "event dictionary."
4. **Alias `"QA strategy"` has no passing or filed quotation supporting it anywhere in this sweep's three
   recheck files.** It is not contradicted either; no source denies the phrase is used. **Flagged for the
   spec author or reviewer to decide**, the same posture `data-dictionary`'s own landing took for its
   contested "data catalog entry" alias, rather than kept or dropped by this spec unilaterally.
5. **Alias "organizational test strategy" is recommended, added, sourced.** It is ISTQB's own term for
   exactly this bundle's own sense, on the passing quotation above, and a reader who types ISTQB's own
   vocabulary should find this bundle.
6. **`owner: "QA Manager"` is not contradicted and is not corrected.** The one source in this sweep that ties
   a Test Strategy artefact to a named role, an Australian public-service job posting, is titled for a
   program-scoped test-management role and lists the Test Strategy among that role's own artefacts, on the
   passing quotation above ("not limited to Test Estimation, Test Schedule, Test Strategy, Test Plan, Test
   Execution Reports, Defect Modelling Reports, and Test Summary Reports"). The posting's own job title is
   not itself a checked quotation and is not repeated here as one; the passing span is evidence enough that
   a program-scoped testing-management role fits at least as well as the catalog's own generic owner.
   **No change recommended.** *(2026-10-20: the build found one source that contradicts the catalog value. QATestLab says "Project Manager prepares Test Strategy.", and other sources name a function, a committee or a board. The owner stays contested, and the catalog's "QA Manager" stands as one reading among several.)*
7. **`rarity: "occasional"` is flagged, at low confidence, not corrected.** The 2026-10-14 critic observed
   that a document "agreed once" per organization or program and consulted repeatedly, per ISTQB's and this
   family's own framing, is written far less than "occasional" suggests for a single project-facing
   document. No source directly states a correct value. **Flagged for a reviewer's judgment, not changed by
   this spec.**
8. **`stage: "testing"` is not corrected.** Per the same reasoning `data-dictionary`'s own landing gave for
   its identical field: the catalog's descriptive `stage` is a different question from the metadata schema's
   `phase`/`classification` axis, which this bundle settles independently as `classification: foundation` in
   its own `meta.yaml`. **No change recommended.**
9. **`relationships: ["Test Plans"]` needs no correction.** Every admitting and boundary source treats a
   standing strategy, where one exists, as upstream of the plan. **No change recommended.**

#### Landing site: `test-plan_guide.md:36`

`test-plan_guide.md:36`'s own routing row, "How this organization tests, in general, across projects" to "A
**test strategy** (standing, rarely changes)," currently routes to a type this library does not yet ship.
Whether that cell gains a direct link to the new bundle, once built, is a build decision, the same stance
ADR 0062 and ADR 0071 each took toward their own sibling's forward-reference. This spec names the site; it
does not make the edit.

#### `pairs_with`: checked, empty

`gh api repos/product-on-purpose/pm-skills/contents/skills --jq '.[].name'` returned all 68 skill names on
2026-10-16. The only name containing "test," `tool-design-sprint-test-and-score`, is a design-sprint
test-and-score skill, unrelated in subject to a software test strategy. No name contains "qa," "quality" or
"strategy" against this type. **`pairs_with: []`**, under the contract's rule for that field: "Verify per
member; claim only what is true of that member" (quoted from `standing-standards.md:74`, the same clause
`business-continuity-plan`'s and `data-dictionary`'s own specs each cite for this check).

#### Risks for the build and review

1. **"Program," never "portfolio," and "program," not "programme," outside a quotation.** The maintainer's
   scope ruling is specific on both axes. A companion that drifts into "portfolio" anywhere outside a
   quotation of a British source silently widens scope past what was ruled; a companion that writes
   "programme" in its own voice, outside a quotation, contradicts the library's own house spelling, confirmed
   at a 447-to-131 ratio for `organization` over `organisation` across the tree.
2. **ISO/IEC/IEEE 29119-3's own clause text must never be quoted.** No automated fetch in either research
   dimension reached it. Every reference to the standard in this bundle's companion must be to a secondary
   account (Wikipedia, ISTQB's own syllabus describing it), labelled as secondary, never presented as the
   standard's own words.
3. **The "organizational test practice" rename risk is a real, recorded open question, not a settled
   correction.** If a later reader reaches the current ISO/IEC/IEEE 29119-3 text and finds the organization-
   level artefact renamed away from "strategy," that is new information this spec does not have, and the
   bundle's own admission case would need to be revisited, not quietly patched around.
4. **Only four of Process Street's steps are raw-checked.** The four quoted above pass. A companion that
   quotes any of the page's other steps would be citing spans no recheck file carries. Paraphrase those
   instead, exactly as this spec does. *(2026-10-20: retired. The build raw-checked all twenty steps, and all twenty are Quotable lines in the research log.)*
5. **The istqb-glossary.page mirror is unofficial, and serves one entry under two names.** A companion citing
   it must say both facts, the mirror's status and the shared-text finding, rather than presenting it as
   ISTQB's own site or as two independently defined terms.
6. **This bundle must not restate `test-plan`'s own Test Levels and Types section or its Risk-Ranked
   Approach section.** The seam is the `test_strategy_ref` field and a stated inheritance-or-deviation
   relationship, not a duplicate of either section's content.
7. **The 42-percent prevalence statistic `test-plan_companion.md:568` already flagged as unsourced and
   excluded must not recur here.** No source in this sweep or its follow-ups corroborates a prevalence figure
   for how many teams keep a standing test strategy, and none should be invented or carried forward from
   anywhere this library has already distrusted it.
8. **The build workflow's templates stage has repeatedly copied the worked example's own scenario into the
   template's GOOD and WEAK text.** Once an example exists, grep the drafted template for its proper nouns
   before review, the practice `business-continuity-plan`'s and `data-dictionary`'s own specs each name.
9. **The plan/strategy boundary is genuinely unsettled in the practitioner literature, and this bundle's own
   companion must say so rather than resolve it.** `test-plan_companion.md:379-390` already frames the line
   as "genuinely unsettled" across six sources. A companion for this bundle that writes as though ISTQB's
   organization-or-program framing were the single correct answer would misstate research this library has
   already logged, in a sibling bundle's own companion.

#### The worked example: the Reporting Platform Modernization program, after the test plan's own date

**This must chain onto the same Acme Analytics thread `test-plan`, `test-summary-report`,
`definition-of-done`, `kpi-dashboard`, `risk-register` and `raid-log` already use, and it must not retcon any
of their shipped sentences.** `test-plan_example.md:7` states, as of that document's own `last_updated` date,
2026-07-06, that "Acme Reporting has no standing test strategy document." This spec's own worked example
does not edit that sentence and does not need to: it is dated after 2026-07-06, so the test plan's own
sentence stays a true, dated fact about the state of the program on the day it was written, the same
resolution `data-dictionary`'s own build chose for an analogous sentence in `tracking-plan_example.md`.

**The natural subject already exists in the shared scenario: the Reporting Platform Modernization
program.** `kpi-dashboard_example.md` and `risk-register_example.md` already name this program as the
standing container the Saved Views feature's own test plan, test summary report and KPI dashboard all sit
inside, with Marta Reyes named as its Program Manager. A standing test strategy for that program, covering
every project it runs (Saved Views for Dashboards among them, and others not yet shown in any shipped
example), is this bundle's own natural worked instance: a program-level document, not an organization-wide
one, matching the maintainer's own ruling exactly.

**Chronology and a plausible hook, both a build decision to state rather than invent silently.** The test
plan is dated 2026-07-06; `test-summary-report_example.md` records the Saved Views release's own exit review
on 2026-07-17; `definition-of-done_example.md` is dated 2026-07-24. A test strategy adopted after the exit
review and on or before the Definition of Done's own date is one coherent placement, motivated by a program
that has just run one release without a shared testing approach and chooses to write one down before the
next, the same kind of motivating event `business-continuity-plan`'s own example used (a PRR that named an
instrument it did not yet have). The exact date is the build's own decision; this spec states only that it
must land after 2026-07-06 and should not be placed earlier than `test-summary-report`'s own exit review
date without a stated reason.

**People: reuse the thread's named roles.** Anjali Rao (QA Lead, Reporting), already the test plan's own
`plan_owner`, is the natural owner of a program-level standing strategy for the same program; Marta Reyes
(Program Manager), already the KPI dashboard's and the risk register's own program-level owner, is a
plausible approver or reviewer, consistent with Process Street's own named approval step.

**What the example may cite, without restating any sibling's own rows.** It may cite that the Saved Views
release ran under this program (`kpi-dashboard_example.md`, `test-plan_example.md`), and it may name, by
pointer only, that the release's own test summary report recorded defects and a deviation from plan
(`test-summary-report_example.md`), as the kind of experience that motivated writing a standing approach
down. It must not restate any defect row, any Risk-Ranked Approach row, or any Test Levels and Types content
already shipped in `test-plan_example.md` or `test-plan_template-full.md`. A program-level strategy answers
a different question: which levels, types, tools and environments every project in this program uses by
default, and how a project's own plan states a deviation, not which specific risks one release carried.

#### Metadata

| Field | Value | Why |
|---|---|---|
| `family` | `standing-standards` | Maintainer ruling, 2026-10-13, with the scope ruled 2026-10-15; argued in ADR 0075 |
| `classification` | `foundation` | ADR 0075, marker by marker, against the contract's own cut |
| `bundle_id` | `test-strategy` | Same as the catalog id; no reason found to differ |
| `sizes_available` | `[lean]` | Argued above; no source in either research dimension describes a short form and a long form |
| `status` | `beta` | Every bundle |
| `methodology` | `methodology-agnostic` | The catalog's own value; the admitting sources span certification, standards and practitioner lineages with no single methodology thread running through all of them |
| `pairs_with` | `[]` | Checked against pm-skills `origin/main`, 2026-10-16; no skill produces or consumes this type |
| `related_templates` | `[test-plan]`, inline | The one neighbour with an existing, unresolved forward-reference to this type, both in its guide's routing row and in its own `test_strategy_ref` field |
| `aliases` | `organizational test strategy` (added, sourced); `QA strategy` (flagged, undecided); `test approach` (recommended for removal here, considered for `test-plan` instead) | See Catalog corrections, above |

#### What landing this bundle closes elsewhere

1. **The `standing-standards` contract's Members line and Change note**, from "not yet built" to the build
   date, moving the contract to `0.6.0` with [ADR 0075](decisions/0075-test-strategy-joins-standing-standards-as-a-foundation.md).
   **This is a bookkeeping edit to the Members line and a dated change-note paragraph, not an amendment of
   the membership clause itself, and it still stops for the maintainer's read**, per the standing rule that
   every contract edit is read before it is merged.
2. **`test-plan_guide.md:36`'s own routing row may gain a link to the new bundle**, a build decision, not
   required by this spec.
3. **The catalog entry**, per the corrections above, in both `docs/internal/catalog.md` and
   `atlas/catalog-data.json`, then the atlas regenerated.
4. **This page's Progress table.**
5. **Issue #260 (bundle: test-strategy) relabels to `status:built` with the build PR**, not with this spec's
   own PR, which only proposes the record.

#### What the build would cost

No build has run for this type. This is projected from the family's own single-size precedent,
`definition-of-ready`, measured in [`bundle-builds/INDEX.md`](../../bundle-builds/INDEX.md) at 5,846,070
weighted token-equivalents, **$11.69 at API list rates, whole build, 15 agents, high confidence**. The
family's other single-size-equivalent build outside this family, `issue-log`, cost $14.29 whole for the same
15 agents. The family's two-size members, by contrast, ran from $14.22 (`launch-coordination-checklist`) to
$20.57 (`business-continuity-plan`) whole. A single-size `test-strategy` build sits closer to the first
group than the second: a whole-bundle estimate of **$10 to $15 at API list rates** is reasonable on that
basis. It is a projection, not a measurement, until `python tools/gen-bundle-build-report.py --ingest` runs
against an actual build report.

### strategy-docs (sixth member, by amendment): the positioning statement, as product direction

**`positioning-statement`** - `strategy-docs`, **`classification: foundation`** (recommended; see Family fit
below), sizes **`[lean]`** only, default `lean`, catalog entry **13** in `docs/internal/catalog.md`
(atlas index 12 in `atlas/catalog-data.json`), catalog id `positioning-statement`,
`pairs_with: []`. **Settled by the maintainer on 2026-10-15: the library takes on positioning only, as
product direction (sitting decision 7, answer B), and this type is specced next, in `strategy-docs` by
amendment, in a single size (sitting decision 8).** The maintainer's note on decision 8 asked for more
research before the amendment is read; that research ran the same day
(`_local/research/2026-10-15_sitting-followup/positioning.json`, gitignored) and is folded into this section
rather than added later as a dated note. The contract amendment, [`strategy-docs`](contracts/strategy-docs.md)
`0.3.0`, and
[ADR 0076](decisions/0076-positioning-statement-joins-strategy-docs-as-a-sixth-member.md) (positioning-statement
joins strategy-docs as a sixth member) land with this spec, so the metadata below is written against contract
`0.3.0`, and the amendment itself stops for the maintainer's read of the diff. *(2026-10-19: the
maintainer delegated the merge instead, so the diff was accepted without that read; see ADR 0076's
Status.)*

**`messaging-framework` (#258) is not part of this amendment and is not admitted by it.** Sitting decision 7
holds it, with its placement flagged under [decision procedure 10](decision-procedures.md#10-a-family-or-axis-assignment-is-uncertain).
See Scope, below, for what this amendment admits and what it deliberately does not.

#### Demand: the library's own research has twice reached for this boundary without a document behind it

Two earlier `product-vision` research passes already named the positioning statement as the adjacent
artifact `product-vision` is most often confused with, and both left the boundary unsourced
(`product-vision_companion.md:276-280`: "No product management source read draws this boundary", labelled
the library's own first-principles reasoning). Admission sweep 6 (2026-10-14) found the same gap from the
other side: a positioning-statement candidate clears admission on five sources, and its nearest shipped
neighbour's own companion already concedes it cannot source the line between them. The 2026-10-15 follow-up
closed part of that gap (see Boundaries, below) without closing all of it.

#### Admission: five sources, raw-checked, plus a sixth named but not counted

The 2026-10-14 sweep read six candidate sources and raw-checked every quotation against page text
(`_local/research/2026-10-14_admission-sweep-6/recheck-out.json`, gitignored). Five clear
[ADR 0048](decisions/0048-one-named-source-clears-the-admission-test.md)'s
one-named-source bar by shipping the positioning statement as a standalone written document or template,
not merely a formula embedded in a book, slide, or canvas:

| Source | What it says | Weight |
|---|---|---|
| MIT Orbit Knowledgebase (Martin Trust Center for MIT Entrepreneurship) | "forces you to use a one page format" | Academic tier. Ships a six-field, one-page template |
| HubSpot | "For [your target market] who [target market need], [your brand name] provides [main benefit that differentiates your offering from competitors] because [reason why target market should believe your differentiation statement.]"; "A positioning statement is a brief description of a product or service" | Vendor tier. Ships a five-field formula and 16 worked examples |
| eCornell #IMPACT, by Doug Stayman (Cornell SC Johnson College of Business) | "Point of Differentiation"; "For [insert Target Market]" | Academic tier. A five-component formula with a worked 2001 Amazon example |
| Yesware | "For [target market] who [target market need], [brand name] offers [market category]" | Vendor tier. Ships its own template, no Moore citation |
| Product Marketing Alliance | "an internal resource used to influence the way a product, service, or brand is positioned" | Vendor tier. A one-page, five-row `.docx` template, gated behind a free-account signup (confirmed by a direct browser observation on 2026-10-15, correcting an earlier automated-fetch read of the same URL that reported a hard paywall) |

**A sixth source is named but carries no weight toward admission.** Pragmatic Institute's workshop page
names a sectioned "positioning document" and states that section order matters, but the specific sentence
describing that claim failed the 2026-10-14 raw-check against the page it was attributed to
(`pragmaticinstitute.com/workshop/product-positioning/`), and no raw-checked quotation exists for the
companion podcast page either. It is named here as a marginal, uncounted lead, and this spec does not quote
it.

**Admission does not depend on Geoffrey Moore, and the catalog's attribution to him is not confirmed.**
Three independent research passes, two earlier `product-vision` passes and this sweep, could not locate the
"for/who/that" wording inside *Crossing the Chasm* itself, by edition, chapter, or page. The 2026-10-15
follow-up (Q1) improved this somewhat without settling it: a Goodreads reader-highlight note on the book's
own text carries a verbatim fill-in-the-blank template matching the known form, at a 59 percent
reading-progress marker rather than a page number, and an independent blog post cites the same template to
page 186 of the 3rd edition (Harper Business, 2014), a citation not itself verified against the book. No
chapter title or number was found anywhere. **This spec credits admission to the five sources in the table
above, and names Moore only as a widely repeated, still-unverified practitioner attribution** - the same
strength, not a stronger one, than the follow-up found.

#### Scope: positioning only, as product direction, and what stays out

**This amendment admits one type, under one reading.** A positioning statement, as this bundle builds it,
is the internal-facing document that states how this product stands against a named alternative, for a
specific target customer, now. It does not admit:

- **A messaging framework.** April Dunford, read and raw-checked: "Positioning is not the same thing as
  messaging." On the same site, read and raw-checked: "I usually build a messaging document that
  references the positioning template." Aha!, read and raw-checked: "The outcome of product positioning is
  an internal document that informs external messaging." `messaging-framework` (#258) stays held.
- **A battlecard.** Named in the research as a separate, sales-facing, multi-topic document that should
  reflect positioning as an input, not restate it. Not built, and not part of this amendment.
- **A positioning map.** A two-axis chart, out of scope under
  [ADR 0030](decisions/0030-templating-scope-markdown-documents.md) (templating
  scope: Markdown documents) on form grounds, and corrected out of this type's own alias list below; see
  Catalog corrections.
- **Go-to-market documents generally.** Sitting decision 7 answered a narrower question than whether the
  library takes on product marketing as a whole: it takes on this one type, as a product-direction
  artifact, and leaves battlecard, competitive analysis and win-loss analysis unswept.

#### Family fit: the membership sentence fits as written; the closed list needed widening

`strategy-docs` section 1 admits a type that "sets or tracks product direction above the level of any
single deliverable." A positioning statement does that on its face: it is argued and revisited, not
authored per occasion, and it recurs at a repositioning event (a relaunch, a new competitor, a market
shift) rather than being finished once, the same "not phase-bound" reading that let
[ADR 0070](decisions/0070-north-star-metrics-joins-strategy-docs-as-a-fifth-member.md)
(north-star-metrics joins strategy-docs as a fifth member) in on an argued rather than quoted exclusion.
What blocked it, exactly as it blocked the North Star metric, is the closed list of five questions that
follows the membership sentence: the three families the sweep actually tested against the type's own
surface (`strategy-docs`, `discovery-docs`, `standing-standards`) all excluded it, and `strategy-docs`'
exclusion rested on arguing that none of its questions covers positioning, not on a clause that fires on its
face. **This is the smallest honest widening available, following the ADR 0060 and ADR 0070 pattern**: a
sixth bullet, naming the question positioning answers.

**Where it sits.** This spec places the new bullet third, between the product strategy and the North Star
metric (which moves from third to fourth), with proposed wording naming how this product stands against a
named alternative, for a specific customer, now; the exact text is in section 1 of
[`strategy-docs`](contracts/strategy-docs.md). The reasoning is that positioning operationalizes
a choice the strategy has already made (which segments, which problems) into an external-facing stance, and
the North Star metric then measures whether that stance is working for that customer. **No source read
states this exact sequence**, so the link is labelled the library's POSITION, the same labelling convention
ADR 0070 used for the North Star's own chain position. **The considered alternative is second, between
vision and strategy**: Devika Nair (Director of Product Management, Oracle), read and raw-checked in the
2026-10-15 follow-up, frames positioning "as part of the vision" (the fetch tool truncated the sentence at
125 characters; `positioning.json` reports the sentence continues "and decision making," not independently
re-fetched) rather than as strategy's output, which would argue for a place closer to the vision. This spec
recommends third place at
low confidence, on the strategy dependency, and names second as the alternative a maintainer who weights
Nair's framing more heavily could choose instead.

**Only three of ten family contracts were tested on this exact candidate**, per the sweep's own admission
(critics.md: "'All families exclude it' is not supportable from this material; 'the three families tested
exclude it' is"). This spec relies on the narrower claim only.

#### Classification: `foundation`, recommended, on a cadence inference the research does not state directly

The contract's own test is "argued-and-durable versus maintained-and-periodic." **No source read states a
review cadence for the positioning statement itself** - this is a gap this spec names rather than papers
over. Two pieces of indirect evidence point the same direction. First, the sweep's own argument against a
phase-bound exclusion rests on the claim that positioning "recurs at repositioning events" rather than on a
calendar; no single source states this in those words, and this spec reports it as the library's own
inference from the admission case, not a quotation. Second, the catalog's own existing `when_used` column
already carries the free-text note "GTM, repositioning" for this type (`docs/internal/catalog.md:43`), which
names the same trigger-based pattern independently of this sweep, though the catalog is this library's own
prior editorial judgment, not an external source. By contrast, the research found real cadence language for
the held `messaging-framework` candidate (The Starr Conspiracy's specific, single-agency cadence numbers,
"two-to-three years for brand and category, quarterly for audience and product"), and found none that
specific for positioning. **Recommendation: `foundation`, beside `product-vision`, `product-strategy` and
`north-star-metrics`.** It is argued and revisited on a trigger, the same shape the contract already uses to
place the North Star metric, not maintained on a fixed cadence. **The alternative is `utility`**, if a
maintainer judges that a type revisited at every repositioning event (plausibly more often than a vision or
strategy) behaves more like the roadmap or OKRs' standing-instrument shape; this spec does not find source
evidence for either reading's exact frequency and names both. *(2026-10-20: the build's research overturns the premise of this subsection. Three sources state an interval: April Dunford describes a positioning check-in "every six months" and, elsewhere, "a couple of times a year"; Abinanti says "It's a good idea to audit your positioning statement every 12 months." CLIMB says a positioning statement "isn't permanent, but it shouldn't change often." The `foundation` reading stands, on that last point and on the check-in's job, which is "to determine whether or not you need to make a positioning adjustment". The maintainer ruled out `utility` on 2026-10-20. See [`positioning-statement_research-log.md`](../../templates/positioning-statement/positioning-statement_research-log.md), "Revisit cadence and triggers".)*

#### Ownership: the split is real, and this spec states the library's placement as argued, not as the majority reading

**Two product-marketing sources place ownership with product marketing**, one of them by name. Blackblot,
read and raw-checked: "Product positioning statements are created by the product marketer who belongs to
the Product Marketing department," and, on the same page: "irrelevant to the product planner" (Blackblot's
own name for the strategy-side role). A second, independent source, read and raw-checked: "product
positioning is usually owned by the Product Marketing function."

**Strategy-side placement is defensible on two pieces of evidence, and it is the minority reading among the
sources this sweep and its follow-up read.** Aha!, read and raw-checked in the prior sweep, lists "Product
positioning templates" inside its product-strategy guide's own template catalog, separately from "Marketing
positioning templates" on the same page. Devika Nair (Director of Product Management, Oracle), read and
raw-checked: "While product management is also responsible for the positioning, they are looking at it as
part of the vision" (the fetch tool truncated the sentence at 125 characters; the full sentence continues
"and decision making").

**This library places `positioning-statement` in `strategy-docs`, as product direction, on Aha!'s and
Nair's placement, not because they outnumber the product-marketing sources - they do not.** The library's
own reasoning is that a document this library builds for a strategy-docs reader needs to answer a
direction-setting question regardless of which department holds the pen; Aha!'s own catalog split (a
strategy-side template distinct from a marketing-side one) and the catalog's own `stage: strategy` field
support building this reading rather than the product-marketing one.

**Who owns the statement varies by organization, and the sources split, so the catalog's owner becomes
`PMM / PM`** (the maintainer's ruling of 2026-10-17). That is a split-owner form the catalog already uses
for other types. The catalog's `PMM` is sourced, by the two product-marketing sources above, but it records
one camp as though it were the whole. **The guide presents both camps with their sources, then suggests a
default, labelled as this library's own reasoning and not as a sourced finding.** The default this spec
suggests follows from the placement: product management owns the statement as product direction, and
product marketing drafts or co-writes it. No source states that division of work, so it is offered for the
maintainer's read. See Catalog corrections.

#### Boundaries with each named neighbour

**Versus `product-vision`: the weak point, now partly addressed.** `product-vision_companion.md:276-280`
states, in its own voice, that the boundary (present and competitive versus future and aspirational) is "No
product management source read draws this boundary," labelled the library's own first-principles reasoning,
not a citation. The 2026-10-15 follow-up found one practitioner source that does draw it: Sharebird, a
named-practitioner Q&A, read and raw-checked. Mike Flouton (Managing Partner, Boxford Capital): "Product
vision is long-term, aspirational, inspiring, speaks to a broad audience". Poorvi Shrivastav (Senior
Director of Product Management, Meta), on the same page: "A positioning statement, on the other hand,
outlines how a product will be perceived in the market relative to competitors," continuing, "It is more
focused on the present, defining the target audience." **This is not universal practice.** A Rational
Unified Process vision-document template nests a subsection named for the product's position inside a
single Vision document, read and raw-checked: "Provide an overall statement summarizing at the highest level,
the unique position the product intends to fill." The RUP source is a general software-engineering
methodology artifact, not a product-management or product-marketing one, and this spec weights it as a
weaker, adjacent-field data point rather than a peer to Sharebird. The library's own first-principles
boundary stands, now corroborated on time horizon and audience by one named source, and contradicted on
whether the two ever merge into one document by a second, weaker one. `product-vision_companion.md:276-280`
is a required landing-site edit; see What landing this bundle closes elsewhere.

**Versus `product-strategy`.** The strategy chooses which problems to solve and which segments to serve
(its own "Target Segments, and Non-Targets" section). A positioning statement takes that choice and states
how the chosen segment should perceive this product against a named alternative. `product-strategy`'s own
template has no section for the competitive alternative or the differentiation statement, which are
positioning's core; the overlap is partial, on the target and the market, not a duplication.

**Versus `messaging-framework` (held).** Clean and well-sourced, three ways. Dunford: "Positioning is not
the same thing as messaging." The Starr Conspiracy (read in the prior sweep): positioning is "one input...
Lock the positioning statement first." Product Marketing Alliance's own messaging template treats the
positioning statement as its opening line, not a duplicate section. `messaging-framework` is not part of
this amendment; see Scope.

**Versus `north-star-metrics` and `okrs` (siblings in the chain).** No source connects a positioning
statement's target-and-differentiation content to either a North Star metric's choice of measure or an
OKR's period-bound target. This is this spec's own completeness statement, under contract section 1's
requirement that every member state its position against every other member; no citation is claimed for it.

#### Sizes: one, short, under the sweep's own finding, reconfirmed by the follow-up

**One size, lean only.** The Starr Conspiracy, read in the prior sweep: positioning runs "1 to 3 sentences."
MIT and Product Marketing Alliance both cap the artifact at one page. The 2026-10-15 follow-up (Q4) tested
this specifically and did not overturn it: HubSpot's own formula recommends 3 to 5 sentences, consistent
with the same short ceiling, and no source describes a multi-page or multi-section long-form positioning
document as the terminal artifact. April Dunford's own material is genuinely longer (five components plus a
bonus trends component, a 12-page workbook, read and raw-checked in the prior sweep), but the follow-up
confirms it reads as a facilitation process for arriving at the one-page statement, not a second, longer
version of the statement document itself. **This library's own inference, following Dunford's directly
verified critique** - "a sort of 'Mad Libs' fill in the blanks exercise for marketing folks"; "this exercise
is not only pointless but potentially dangerous"; "The only valuable thing we can learn from the statement
is that there are multiple components of positioning" - **is that the lean size pairs the one-sentence
statement with its named components (target, need, category, benefit, named alternative, differentiation)
rather than shipping the bare sentence alone.** Checked against the admitting sources' own field sets: MIT's
template carries six fields (target, need, category, benefit, main competitor, differentiation points).
HubSpot's quoted formula has five bracketed slots. The sweep's research summary of eCornell's page, not a
raw-checked quotation, describes its formula as five components that must all appear
(`_local/research/2026-10-14_admission-sweep-6/sweep6.json`, gitignored). All three name the same shape under different
labels. The component list above is this spec's own convergence across those three, not any one source's
exact wording, the same posture `data-dictionary`'s own Field Definitions section took for its column set.
Dunford's longer workbook material belongs in the guide, as facilitation content, not as a second template
size.

#### Section design

| Section | What it is | Sourcing |
|---|---|---|
| **Purpose and Boundary** | What this document states (the present-tense competitive stance for a named target) and what it rules out by name: messaging, a battlecard, a positioning map, and `product-vision`'s own future-tense content | Sourced to the Boundaries subsection above |
| **The Statement** | The fill-in-the-blank sentence itself: for [target], who [need], [product] is the [category] that [benefit], unlike [named alternative], because [differentiation] | MIT, HubSpot, eCornell, and Yesware all ship a version of this form; the exact field labels are this library's own wording, since HubSpot's and Yesware's own phrasing is their own copyrighted formula text |
| **The Components** | Each named component expanded to a sentence or two: the target, the need, the category, the benefit, the named alternative, and the differentiation | Dunford's directly verified critique of the bare sentence; MIT's six-field template; PMA's five-row document |
| **Why This Positioning** | The evidence behind the differentiation claim: what the named alternative actually does, and why this target should believe the stated benefit over it | HubSpot's "reason why target market should believe your differentiation statement" field |
| **When We Revisit It** | The trigger that would bring the team back to this statement (a new competitor, a market shift, a relaunch), not a calendar date | This spec's own inference from the admission case; see Classification, above. No source states a cadence directly, and the section's guidance comment must say so *(2026-10-20: wrong as stated; three sources give an interval, so the section asks for a last-review date and named triggers, and offers a check-in only as attributed guidance. See the dated note under Classification, above.)* |

**One size, so there is no lean column; every section above ships.** This mirrors the single-size shape
`definition-of-ready` and `announcement-internal-comms` already use, not the lean/full nesting the rest of
`strategy-docs` carries.

#### Catalog corrections the landing PR must make

Per [decision-procedures.md procedure 1](decision-procedures.md#1-a-catalog-call-loses-to-research)
(a catalog call loses to research), against `docs/internal/catalog.md:43` and the matching
`atlas/catalog-data.json` entry (`positioning-statement`):

- **Drop the alias "positioning map."** It names a two-axis chart, a different, out-of-scope artifact, not
  an alternate name for the written statement. Confirmed independently by this sweep; no source treats the
  two as the same document.
- **The owner "PMM" becomes "PMM / PM", by the maintainer's ruling of 2026-10-17.** `PMM` is sourced:
  Blackblot and a second source name product marketing as the owner (see Ownership, above). It is not the
  whole picture: Aha! files a product-positioning template in its product-strategy guide, and Devika Nair
  describes product management as "also responsible for the positioning". Yesware, read and raw-checked: "A
  positioning statement requires input from several different teams." Product Marketing Alliance, read and
  raw-checked (a different page from the admitting template): "share it with stakeholders across the
  organization." `PMM / PM` records the split in a form the catalog already uses, and the guide carries
  both camps and a labelled default, as Ownership, above, states.
- **The named source "Moore's 'for/who/that' template" should be corrected.** Credit the five sources in
  the Admission table instead, and name Moore only as an unverified, widely repeated attribution. See
  Admission, above.
- **The alias "positioning framework (Geoffrey Moore)" carries the same unverified attribution.**
  **Recommend** shortening it to "positioning framework", for the same reason as the named-source
  correction above.
- **`methodology: methodology-agnostic` is not contradicted by anything retrieved and should stand.**
- **`size_variant: S` matches this spec's own single-size call and needs no correction**, beyond the
  mechanical step of setting `sizes_available: [lean]` directly in `positioning-statement_meta.yaml`.
- **`relationships: [Messaging, Battlecard]` is not contradicted**, and names exactly the two neighbours
  this spec also holds out of scope; no change recommended.
- **`stage: strategy` is not contradicted, and supports the family placement this spec recommends.** No
  change recommended.

#### `pairs_with`: checked, empty

`tools/known-skills.txt` (the pinned list; 13 skill IDs as of 2026-10-16) contains no ID with "position" or
"messag" in it. **`pairs_with: []`**, under the contract's rule to claim only what is true of this member.

#### Risks for the build and the review

1. **The chain placement is the one call a maintainer could most easily overturn.** This spec places the
   new bullet third, between strategy and the North Star metric, on an inference no source states, and
   names second (between vision and strategy) as the considered alternative. A reviewer who treats third
   place as settled rather than argued is overstating this spec's own confidence.
2. **The ownership statement must stay an argued library position, never a reported consensus.** Two
   independent sources, one of them by name (Blackblot), place ownership with product marketing. A
   companion or guide sentence that reads as though strategy-side ownership were the majority view
   misstates the sweep's own finding. The guide's suggested default carries the same label: it is this
   library's reasoning, and no source states it.
3. **The vision boundary rests on one practitioner source, not a settled rule.** Sharebird draws the
   present/future, narrow/broad-audience line; a RUP vision template nests positioning inside a vision
   document instead. The companion must carry both, the same way `north-star-metrics`' own companion names
   both camps on its chain position.
4. **Admission must not lean on Geoffrey Moore.** The follow-up found a readable-source quote and an
   independent page citing an edition and a page number, but neither is verified against the book itself,
   and no chapter was found anywhere. State Moore as a named but unverified attribution, at the strength the
   follow-up found, not stronger.
5. **The cadence claim behind `classification: foundation` is this library's own inference.** No source
   states how often a positioning statement is revisited. A companion sentence that cites a source for this
   claim would be inventing one; the Classification subsection above is the full extent of what the research
   supports. *(2026-10-20: retired. The build found sourced intervals and triggers; see the dated note under Classification, above. The bundle's files cite them, and none says that no source states a cadence.)*
6. **The templates stage has repeatedly reused the worked example's own scenario in GOOD and WEAK text**,
   named as a risk in `north-star-metrics`', `data-dictionary`'s and `business-continuity-plan`'s own specs.
   Grep the drafted template for the example's proper nouns before review.

#### The worked example

**The shared-scenario rule (contract section 4) applies.** The example is an Acme Analytics artifact,
chained onto the existing `product-vision` and `product-strategy` examples rather than inventing a parallel
company. It states Acme's positioning against a named competitive alternative, for the target segment the
product strategy example already chose, and it must not contradict either sibling's own stated target,
segment, or differentiation. It must not cite or contain any document dated after it, following the same
rule `north-star-metrics`' own example states. Its date sits after the product strategy example
(2026-01-28) and before the North Star metric example's own window (2026-01-29 through 2026-02-10), under
the chain placement this spec recommends (positioning third in the chain, one step ahead of the North Star
metric's own fourth place). *(2026-10-20: this window holds no whole day, since it runs from after 2026-01-28 to before 2026-01-29. The North Star example is in fact dated 2026-02-04, so the build dated the positioning example 2026-01-30, between the strategy and the North Star examples, and cites neither the North Star nor the roadmap example.)*

#### Metadata

| Field | Value | Why |
|---|---|---|
| `family` | `strategy-docs` | ADR 0076 |
| `classification` | `foundation` | Recommended; argued and revisited on a trigger, not a stated calendar; see Classification, above |
| `sizes_available` | `[lean]` | The sweep's own finding, reconfirmed by the follow-up; see Sizes, above |
| `default_size` | `lean` | The only size |
| `status` | `beta` | Every bundle |
| `methodology` | `methodology-agnostic` | Not contradicted by anything retrieved |
| `pairs_with` | `[]` | `tools/known-skills.txt` lists no positioning or messaging skill |
| `related_templates` | `[product-vision, product-strategy, north-star-metrics, okrs]`, inline | The family's other foundation and utility members; inline, because check I drops the first entry of a block list |
| `aliases` | corrected per Catalog corrections, above | "positioning map" dropped |
| `catalog_ref` | `13` | Catalog entry 13 in `docs/internal/catalog.md`, `positioning-statement` |

#### What landing this bundle closes elsewhere

1. **The contract's Members line** changes from "not yet built" to the build date.
2. **`product-vision_companion.md:276-280`** becomes stale once this bundle ships, citing Sharebird on the
   vision boundary; it needs a dated note, not a silent rewrite, following the correction-versus-supersession
   rule in `docs/internal/decisions/README.md`. Two other `product-vision` files record the same earlier
   finding, `product-vision_research-log.md:813` and `product-vision_history.md:23`. Both are records of what
   a past research pass found, so they stay as they are.
3. **Any routing row that sends a positioning reader to `product-vision`** needs a second destination once
   this bundle exists; the build PR should grep for one.
4. **The catalog row's corrections**, above.
5. **No existing member's companion changes beyond the one named edit above**, following the precedent ADR
   0070 and ADR 0067 each set.
6. **Issue #256 (bundle: positioning-statement)** closes with the build PR.
7. **This page's Progress table.**

#### What the build would cost

No measured figure exists for this exact bundle; this is a forecast from the closest comparisons, not a
quotation. The two built `strategy-docs` siblings with a measured [build report](../../bundle-builds/INDEX.md)
are `north-star-metrics` (lean and full, $9.73 at API list rates, 9 agents, 2 runs, "floor" scope) and
`product-vision` (lean and full, $9.22, 10 agents, 2 runs, "floor" scope). The most recent single-size
builds in the whole library are `definition-of-ready` ($11.69, 15 agents, 3 runs, "whole build" scope) and
`announcement-internal-comms` ($16.99, 15 agents, 3 runs, "whole build" scope). A single-size
`positioning-statement` build sits below both pairs on sections (five, none full-only) and above the
two-size `strategy-docs` siblings on research depth (five admitting sources plus a follow-up, against one
publisher for `north-star-metrics`); this spec does not forecast a dollar figure from that comparison, only
names the four measured points a maintainer can bound it between.

### discovery-docs (fifth member, at `define`): the design brief, in the Design Council's sense

**`design-brief`** - `discovery-docs`, **`phase: define`**, sizes **`[lean, full]`**, default `lean`, methodology
**`methodology-agnostic`**, catalog **entry 209**, no aliases. The maintainer ruled on the spec's ten choices on
2026-10-22, and the rulings close this section. The family decision is [ADR 0079](decisions/0079-design-brief-joins-discovery-docs-at-define.md)
(design-brief joins discovery-docs at define), **accepted 2026-10-22 on the maintainer's delegation**, without
a read of its contract edits. The maintainer confirmed it the same day.

#### The recommendation, and how sure it is

**Build the design brief as the fifth `discovery-docs` member, at `phase: define`, in the Design Council's
concept-handoff sense.** Confidence: medium.

The document converges on one chosen problem and names the one concept chosen for design. It hands both to the
people who will design it. It never says how that concept works, it decides no investment, and it authorizes no
project. The `discovery-docs` 0.4.0 contract already permits that content, in its section 2 phase row and its
section 1 cadence exception. [ADR 0077](decisions/0077-define-ends-with-a-chosen-concept.md) (define ends with a
chosen concept) wrote both clauses on 2026-10-17.

**Sweep 3's verdict no longer governs.** The third Define sweep's digest is dated 2026-10-16. It found a narrow
design brief too thin to build beside `problem-statement`. It tested against ADR 0068 (the define phase means
problem framing), whose rule was that a `define` document names no solution. ADR 0077 superseded that rule the next day, so a chosen concept became legitimate
`define` content. The 2026-10-20 Define re-score then returned the type for this sweep, in the Design Council's
sense, at medium confidence.

**What holds the confidence at medium.** The type clears admission easily. No single source, however, models the
narrow shape this library would build, and D2 (this sweep's second research file) found that at high confidence.
The bundle's section set is therefore the library's own composition from several sources, labelled a POSITION.
The maintainer took nine of the ten recommendations on 2026-10-22. On sizes, the maintainer chose two over one.

#### Demand: an issue, a re-score, and a sibling that routes the type away

- Issue #294 (bundle: design-brief) has carried the candidate since 2026-10-16. It is labelled `phase:define`.
- ADR 0077 named the design brief the first Define spec if the re-score confirmed it. The re-score did.
- `project-brief`'s guide (row 21) routes a reader who is briefing a designer to a creative or design brief.
  Its templates (lean line 39, full line 43) and its companion's section 8 also say a project brief is not a
  design brief. No bundle answers that routing today.
- pm-skills ships no design-brief skill. That is no reason either way, because this library never assumes
  pm-skills is installed.

#### Admission: the type clears on several named sources, and the sense is the library's composition

The main loop checked 53 returned web quotations against raw page text on 2026-10-22. Fifty-one passed, directly
or by a tokenization, Wayback or carried check. Two stayed unverified and are not used. Five more quotations are
this repository's own text, read directly. Every quotation below is one of the 51 or one of the five.

| Source | What it says | Sense | Weight |
|---|---|---|---|
| Design Council, *History of the Double Diamond* | "The result is to create a design brief which clearly defines the challenge based on these insights." | Concept handoff; contents unstated | **Placement only.** It is the one primary source that puts the brief at Define. It was raw-checked in sweeps 2 and 3, and again here |
| Wyn M Jones and Hedda Haugen Askland, *Design Briefs: Is There a Standard?* (Design Society, 2012) | A brief exists "to help the designer to understand the problem by defining the objectives and parameters of the project". The paper also finds "there is no single or correct format for a design brief" | Both | It **admits on its own** under ADR 0048 (one named source clears the admission test). It also says, "A written design brief will clearly articulate the product requirements to all parties involved in a project." That sentence leans toward a specification |
| Peter L. Phillips, *Creating the Perfect Design Brief* (Allworth Press with the Design Management Institute, 2004), checked through Open Library | "A well-written design brief is a written agreement, or contract, between the parties"; "The design brief is also a project-tracking tool." | Commissioning | It **admits on its own**, and it is the genre's main book. Its contract sense is the record the `define` rule bars |
| Wikipedia, *Design brief* | "A design brief is a document for a design project developed by a designer in consultation with a client."; "They usually change over time and are adjusted as the project scope evolves." | Commissioning | It is a reference source, and it supports the cadence exception |
| Kuse, *How to Write a Solid Design Brief: Workflows & Real Examples* | A brief "defines the problem a design needs to solve, the context in which it exists, and the constraints that shape the solution". It lists contents "including problem statement, goals, target users, constraints, and deliverables" | Concept handoff, with deliverables | It is a vendor source, and the closest single description of the narrow sense |
| Heap, *Save Time and Get Aligned With a Design Brief* | "The goal of a Design Brief is to describe, holistically and at a high level, your proposed design solution(s)". Heap separates it from its Problem Brief: "The Problem Brief describes the problem to be solved and the reasons to prioritize it" | Solution | It is a practitioner source with a downloadable written template. Its goal sentence fits a concept. D1 reads its sections as reaching into how the solution works |
| Y Combinator, *Practical Design: Design Brief* | "Good design briefs provide a clear context for a product."; "Have you done any user observations? If yes, will you be able to share the process and the findings?" | Both | It is a practitioner source. D1 reads it as a four-section question tool that ends with how to engage a designer |
| Matej Kaninsky, *The power of a UX project brief (template included)* (UX Collective) | It puts "your initial assumptions, hard facts, goals, and other relevant information into a written form". It is written "before any research and design activities even start" | Both | It is a written template under another name. It is a kickoff brief written before research, so it is a neighbour, not this document |
| Noric Dilanchian, *Use design briefs to shape your projects* (Dilanchian Lawyers & Consultants, 2007) | "A design brief comes early in a process which may lead to deal making, and then onwards towards contracting" | Both | It is a practitioner source. It places the brief before the deal and the contract that commission design work |
| Figma, *How to write a creative brief: five steps for designers* | "A design brief, on the other hand, builds on this foundation with specific technical and visual requirements." | Specification | It is a vendor source. It treats the brief as a visual and technical specification |
| Design Commission for Wales, *Introduction to Brief Writing* (2025) | "The project brief should be the central reference document used in the appointment of a consultant team." | Commissioning | It is built-environment corroboration only. Its running text calls the document a project brief |

**Admission under [ADR 0048](decisions/0048-one-named-source-clears-the-admission-test.md) (one named source clears
the admission test): it passes, with high confidence.** Jones and Askland, Phillips and Wikipedia each define the
design brief as a written document. Heap and Y Combinator each publish a written template under that name.
Kaninsky publishes one under another name. ADR 0078 (written forms of maps, canvases and session records) is not
needed, because no source here is a board.

**The narrow sense is assembled, not found: high confidence.** D2 found no source that confines a brief to a
challenge, a chosen concept and a handoff. Every source that frames the brief as a Define output adds content
beyond problem framing. Every source that names a budget, a time line or deliverables scopes them to the whole
project or design engagement. So the bundle composes its sections from several sources and labels the composition
the library's POSITION. ADR 0048 asked `spike-report` to teach its dispute rather than resolve it. This bundle
carries the same duty for its term's senses.

**Two sources may not be used.** Dani Nordin's article on UX Collective returned HTTP 403, and the Wayback Machine
returned HTTP 429 on three retries. Neither of its two quotations may be cited, and experience brief may not
become an alias. nibusinessinfo.co.uk returned HTTP 403 to sweep 3 and was not read again in this sweep.

**One attributed phrase has no source.** The re-score's first scorer attributes to ADR 0063 (project-brief reopens
discovery-docs) a phrase saying the project brief carries no shaped solution. That phrase appears nowhere in the
repository. This spec does not repeat it, and it states the project-brief boundary from `project-brief`'s own
template instead.

#### Which sense this bundle builds, and what it tells a reader who wanted another

The sources read use the term in four different senses. The count is this spec's own assembly: D1 found three
senses among technology sources at high confidence, and the design world's concept handoff is the fourth.

| Sense | Who uses it | Where it lives in this library |
|---|---|---|
| **Concept handoff.** The chosen challenge and one chosen concept, handed to the people who will design | The Design Council, for placement; Kuse and Jones and Askland, in part | **This bundle** |
| **Commissioning agreement.** Scope, time line, budget and deliverables, agreed between a client and a designer | Phillips, Wikipedia and the Design Commission for Wales; Dilanchian, in part | It is not built. The `define` rule bars the record that authorizes a project, and this sweep tested no other family for it |
| **Solution brief.** A proposed solution's journeys, surfaces and edge cases | Heap, in D1's reading of its sections | It is not built. `solution-brief` was retired on 2026-09-20 with no catalog entry, and it re-enters only through a research pass. It would sit at `develop` |
| **Specification.** Technical and visual requirements | Figma | It is not built as a brief. Its content would sit at `develop` or `deliver`, never at `define` |

**Phillips is bounded, not imported.** His three carried quotations are real. The re-score digest traced an
apparent failure to Open Library's highlight markup. His "written agreement, or contract, between the parties" is
the commissioning record the rule bars. He also names, among the brief's most critical elements, "the sections
dealing with the initial design". Sweep 3's notes complete that phrase as the initial design strategy. A design
strategy that says how the concept works belongs to `develop`, under ADR 0077's table. `backlog.md` records that
this reading is contested, because design-management usage can mean how design serves business objectives. The
bundle keeps only the concept, at the level of the kind of answer.

**The guide routes a reader who wanted another sense.** A team commissioning an outside designer or agency needs
Phillips's agreement, which this library does not build. A team describing a chosen solution's journeys and edge
cases has moved past `define`, and this library builds no solution brief. A team writing visual requirements is
specifying. Each case is a row in the guide's
when-not-to-use table.

#### Phase: `define`, under the 0.4.0 rule as written

The contract's section 2 phase row lets a `define` member name the candidate concepts weighed and "the one concept
chosen for design". It also permits "the scope, time line and budget of handing that concept to the people who will
design it". It holds every `define` member to one bar: "it decides no investment, and it is not the record that
authorizes a project". A design brief meets each clause.

ADR 0077 draws the working line: "A concept names the kind of answer the team will pursue. A specification says how
that answer works or what it must do." The brief carries the first and never the second.

The cadence exception covers the brief's revision while design runs. Phillips writes that "The design brief is also
a project-tracking tool." Wikipedia says briefs "usually change over time and are adjusted as the project scope
evolves". The exception bounds that revision: the brief is finished when the design work it hands off is done.

Check K gates the value and cannot judge it. Whether a filled brief stays at concept level is a review obligation
against section 2. Confidence: high that the rule admits the document as specced. Confidence is medium that filled
briefs will stay at concept level, which the guide's TRAP lines must carry.

#### The family: `discovery-docs`, by a small amendment (ADR 0079)

- **Section 2 needs no change.** The phase row already permits the content, and `[lean, full]` is the sizes
  row's default shape.
- **Section 1's membership sentence does not describe the job cleanly.** It admits a type that exists to decide
  whether to build something, before anyone commits to building it. A design brief carries a concept already
  chosen and hands it on. ADR 0077 added a cadence exception for this document and left that sentence alone.
- **Recommended: widen the sentence by one clause.** Confidence: medium. The new words admit a type that decides
  which concept to design, still before anyone commits to building it. This follows the smallest-honest-widening
  standard that [ADR 0076](decisions/0076-positioning-statement-joins-strategy-docs-as-a-sixth-member.md)
  (positioning-statement joins strategy-docs) applied. The alternative argues that the sentence already fits,
  because design is not building. Confidence in that reading: medium-low.
- **Section 1 also gains a member bullet**, and its cadence exception names `design-brief` as the one member that
  takes it. Section 4 gains a shared-scenario bullet. The change note records version 0.5.0.
- **Why not a define-pinned family.** [ADR 0069](decisions/0069-problem-statement-joins-discovery-docs.md)
  (problem-statement joins discovery-docs) named the condition for one. A second problem-framing candidate must
  clear admission, and the maintainer must want Define bundles on a shelf of their own. This candidate meets the
  first half, and the second half is the maintainer's call. A new family would hold one built member and one spec. Moving
  `problem-statement` would also reopen a built bundle. ADR 0070 (north-star-metrics joins strategy-docs) and
  ADR 0076 each declined a family that no second built member tests. This spec declines the route for now, at
  medium confidence.

#### Where it sits in the chain (POSITION)

**A design brief follows the problem statement and precedes any document that specifies how the solution works or
what it must do.** That order is the library's POSITION, the label ADR 0070 and ADR 0076 gave their own chain
placements. Two sources support part of it.

- Heap pairs the two documents: "the team goes over both Problem and Design Brief with leadership to get input."
  Heap calls the first a Problem Brief, and problem brief is already an alias of `problem-statement`.
- The Eleven Lessons report, quoted in ADR 0077, says "the Define stage would end with final sign-off of the
  concept".

**Dilanchian's early placement, reconciled.** Dilanchian says a design brief "comes early in a process which may
lead to deal making, and then onwards towards contracting". Dilanchian measures early against commissioning deals
and contracts, so a brief may follow a problem statement and a `discover`-phase project brief yet come early. A
`define` member that follows a `discover` member repeats the inversion ADR 0069 already accepted.

**The business case is left unordered.** None of this sweep's or sweep 3's research files orders a design brief
against a business case. The bundle therefore fixes no order between them, at medium-low confidence. A brief
written before a case hands on a concept the case may weigh as one option. A brief written after a funded case
strains the membership sentence, and the guide says so.

#### The line against the Shape Up pitch

The re-score kept Basecamp's pitch out at medium-low confidence. Its score row asked this sweep to resolve the
pitch's collision with the design brief. Catalog entry 45 (Shape Up Pitch) stays a separate, unbuilt candidate. The
line has two parts, and both are the library's POSITION. Confidence that the line can be applied in review: medium.

1. **Altitude.** A design brief names its concept at the level of the kind of answer, as ADR 0077 puts it. A pitch
   arrives shaped. Basecamp writes, "A problem without a solution is unshaped work." Its rabbit holes are "Details
   about the solution worth calling out to avoid problems". Detail about how the solution works belongs to
   `develop`.
2. **The act.** A design brief hands a concept to the people who will design it, and it does not itself commit the
   bet. A pitch exists for the bet: "The purpose of the pitch is to present a good potential bet." The re-score
   digest notes that the betting table's decision commits a team's cycle. That sits close to the investment
   decision the rule excludes.

**Why the exclusion stays at medium-low.** Basecamp's no-gos are "Anything specifically excluded from the concept",
so Basecamp calls shaped work a concept too. The pitch's appetite also reads fairly as the handoff budget the
contract permits. The maintainer may reopen the pitch as its own `define` candidate. If the maintainer does, the
pitch's spec must state this boundary from its own side.

**The guide's message to a Shape Up team.** A document that resolves rabbit holes and goes to a betting table is a
pitch, and this library does not build one.

#### Distinctness from `problem-statement`

**What is distinct: the chosen concept, with the candidates weighed, and the handoff to designers.** Confidence:
medium.

- **The chosen concept is new territory.** `problem-statement`'s companion says plainly, "This document names no
  solution". No built `discovery-docs` member names a concept chosen for design.
- **The handoff is new territory.** `problem-statement`'s Decision This Informs names a decider and a next document.
  It names no reader who will design from it.
- **Design constraints may be distinct, at low confidence.** `problem-statement` routes limits that bound a
  solution, such as a budget, a deadline or a regulation, to `project-brief`. A section on limits to the design work
  itself would duplicate neither bundle. The kinds of limit, though, come from nibusinessinfo.co.uk, which sweep 3
  could not read. Kuse mentions "the constraints that shape the solution", and Heap mentions "the constraints within
  which it exists". The maintainer kept this section on 2026-10-22, in the full size, at low confidence.
- **Success criteria are not distinct.** `problem-statement`'s full size already carries How We Will Know It Is
  Solved. The brief's Challenge section points to those measures rather than restating them.
- **Users and evidence overlap.** `problem-statement` carries Who Is Affected and Evidence. The brief carries a
  short summary for a different reader, the designers, with a pointer back. That choice is the library's POSITION.

#### Boundaries with each named neighbour

- **Not `problem-statement`.** The statement chooses the problem. The brief carries that choice to design, with a
  concept. A team may write a brief with no statement, and its Challenge section then frames the problem in brief.
- **Not `project-brief`.** A project brief asks for authority to start finding out whether and how to proceed,
  before anyone commits to building anything (`project-brief_template-lean.md:32-33`). The spec for its example
  forbids naming the option the business case later chose. A design brief names the chosen concept and asks for no authority.
- **Not `business-case`.** A business case decides whether an investment is worth making, against alternatives
  that include doing nothing. A design brief decides no investment. Its candidates are concepts weighed for design,
  with no costs and no benefits. Where both exist, the concept may enter the case as one option (POSITION).
- **Not `product-vision`.** No source read contrasts the two directly, so D2 rates this boundary low. It is
  inferred: a vision is a standing, whole-product document. A brief is finished when the design work it hands off
  is done.
- **Not the `prd`.** A PRD states what the solution must do in testable detail, which ADR 0077 places in
  `deliver`. uxmagic.ai scopes a design brief to a "Screen or flow" and "One design task", against a PRD's wider
  scope. That source uses the solution sense, so it supports only the order. The brief precedes the PRD and
  carries no requirements.
- **Not `trade-study` or another `develop` bundle.** ADR 0077's table puts comparisons between designed
  alternatives in `develop`. A brief weighs candidate concepts at concept level only.
- **Not the Shape Up pitch (catalog entry 45).** See the section above.
- **Not a creative brief.** Figma separates the two: "In many design workflows, the creative brief informs the
  design brief, ensuring visual decisions support broader project goals." No bundle or catalog row exists for a
  creative brief.
- **Not a Design Sprint brief.** [ADR 0035](decisions/0035-prototype-brief-fails-the-admission-test.md)
  (prototype-brief fails the admission test) found that Google Ventures' Sprint Brief scopes a whole five-day
  sprint. pm-skills' `tool-design-sprint-brief` is a pre-sprint document of that kind.

#### Sizes: two, by the maintainer's ruling

**Ruled 2026-10-22: two sizes, `[lean, full]`, with `lean` the default.** The maintainer chose this over the
spec's recommendation of one size, which is kept below as the record of what was argued. The ground matches
ADR 0069's: the maintainer ruled two sizes for `problem-statement` against that sweep's lean-only finding.

- **Lean** carries four sections: The Challenge, Who It Is For and What We Learned, The Chosen Concept, and The
  Handoff.
- **Full** adds three: Constraints on the Design, Open Questions for Design, and The Handoff's Scope, Time Line
  and Budget. The lean sections keep their names and order inside the full variant, as the contract's nesting
  rule in section 3 requires.
- **The full-only sections rest on the library's construction more than the lean ones do.** Each carries its
  source or the POSITION label in the section table below, and the companion must say so.
- **`default_size: lean`**, as in `problem-statement` and `project-brief`. The lean variant fits a concept handed
  to a team's own designers. The full variant fits a handoff to a separate design team, or one that must set
  limits, open questions, or a time and budget for the design work. That guidance is the library's judgment.

**The recommendation the maintainer overruled, as the spec argued it: a single size, `[lean]`.** Confidence:
medium.

- No source splits a short brief from a long one (D2, medium confidence). Sources scale one brief by the size of
  the organization or the project.
- Dilanchian contrasts Phillips's corporate briefs with small-business templates that are "generally much shorter,
  simpler and focused on specific needs". That is scaling, not two sizes of one template.
- The long form the sources describe is the commissioning agreement, which the `define` rule bars.
- The slice the contract does permit, the handoff's own scope, time line and budget, appears in no source at that
  scope (D2, high confidence). A full size built on it would rest on the library's construction.
- `positioning-statement` shipped in a single size on similar evidence, by the maintainer's ruling of 2026-10-15.

**The alternative is lean plus full.** The full variant would add Constraints on the Design, Open Questions for
Design, and a section on the handoff's scope, time line and budget. The contract permits all three. The precedent
cuts both ways: the maintainer ruled two sizes for `problem-statement` against that sweep's lean-only finding
(ADR 0069). Under two sizes, every full-only section must cite a source or carry the POSITION label.

**What would change the recommendation.** A source that publishes a short and a long concept-handoff brief as one
type would. So would the maintainer's preference for two sizes.

#### Section design (proposed, for the build's research to test)

| Section | What it carries | Sources | Confidence |
|---|---|---|---|
| **The Challenge** | It restates the chosen problem for the people who will design. It says what a good outcome would change, and it points to a problem statement where one exists | The Design Council's brief "clearly defines the challenge"; Kuse's brief "defines the problem a design needs to solve, the context in which it exists"; Jones and Askland's brief exists "to help the designer to understand the problem" | High |
| **Who It Is For and What We Learned** | It summarizes the users the design serves and the research insights the challenge rests on | Kuse lists "target users"; the Design Council's brief is "based on these insights"; Y Combinator asks "Have you done any user observations?" | Medium-high |
| **The Chosen Concept** | It lists the candidate concepts weighed, at concept level. It names the one chosen and why, and what that concept deliberately leaves out | The contract permits it. Heap describes a solution "holistically and at a high level". The Eleven Lessons report ends Define with "final sign-off of the concept". No source publishes a candidates list as a brief section, so that part is POSITION | Medium on the concept; low on the candidates list |
| **Constraints on the Design** *(full only)* | It names limits the design work must respect that a project brief would not carry | Kuse's "the constraints that shape the solution"; Heap's "the constraints within which it exists". The kinds of limit rest on an unread source | Low |
| **Open Questions for Design** *(full only)* | It says what the designers must find out, and what is assumed until they do | Heap's design-brief template lists Open Questions in D1's reading, which was not raw-checked | Medium-low |
| **The Handoff** | It names who will design from the brief and what they receive. It records who approved design to begin, and when. It says how the brief stays current while design runs, and which document takes over. The PRD takes over once the designed concept is specified, and that is the library's POSITION. No `develop` bundle is named, because the designers' own output, such as wireframes and prototypes, is not templated here | Kaninsky's brief aims "to get designers, product managers and software engineers on the same page". Phillips calls the brief "a project-tracking tool" | Medium |
| **The Handoff's Scope, Time Line and Budget** *(full only)* | It states the scope of the design work handed off, when that work should finish, and any budget already set for it. It holds no project budget, no funding request and no commissioning terms | The contract permits "the scope, time line and budget of handing that concept to the people who will design it". No source scopes a time line or a budget to the handoff alone, so the section is the library's POSITION | Low |

**Lean holds the four rows with no size label. Full holds all seven, in the table's order.**

**What stays out at any size.** How the concept works stays out, including a design strategy in that sense. So do
screens, flows and requirements. A commissioning agreement, a whole-project budget and an agency selection stay out. An investment
decision, a funding request and the record that authorizes a project stay out. Figma's visual and technical
requirements stay out too.

**Quality rules go to the guide**, under
[decision procedure 12](decision-procedures.md#12-a-property-or-section-is-proposed-for-a-template). The
concept-versus-specification line and the pitch line become TRAP lines and rubric rows.

#### Metadata

| Field | Value | Why |
|---|---|---|
| `family` | `discovery-docs` | ADR 0079 |
| `phase` | `define` | Contract 0.4.0 section 2 permits it, as ADR 0077 wrote it |
| `sizes_available` | `[lean, full]` | The maintainer's ruling of 2026-10-22. It is the contract's default size shape |
| `default_size` | `lean` | As in `problem-statement` and `project-brief`, the family's other define-adjacent members with two sizes. This is judgment |
| `status` | `beta` | Every bundle starts at `beta` |
| `methodology` | `methodology-agnostic` | The sources span design management, design-council practice, product practice and UX practice. One value would misdescribe at least two. This is judgment |
| `pairs_with` | `[]` | The check is below |
| `related_templates` | `[problem-statement, project-brief, business-case, prd]`, inline | The document before it, two neighbours it must be told apart from, and the specification after it. Inline, because check I drops the first entry of a block list. This is judgment |
| `aliases` | none | The aliases are argued below |

#### Aliases

**Recommended: none.** Confidence: medium. No raw-checked source names the end-of-Define concept handoff under
another name.

- **UX project brief**, Kaninsky's name, is the nearest sourced name. Its own text places the brief "before any
  research and design activities even start", so it names a kickoff brief. The maintainer chose not to add it
  on 2026-10-22.
- **Experience brief**, Nordin's name, is unverified and may not become an alias.
- **Problem brief** is already `problem-statement`'s alias, from Heap. **Pitch** is already an alias of catalog
  entry 45.

The companion carries the four senses, so a reader who searched for another sense learns where it lives.

#### The catalog row the build PR adds

The row is **entry 209**. It goes at the end of `atlas/catalog-data.json`, after entry 208, Cagan's Product
Opportunity Assessment, which the maintainer recorded on 2026-10-22, after this spec first named 208. The row
lands with the build PR, as entry 206 landed with `problem-statement`'s build in PR #271. In
`docs/internal/catalog.md`, entry 209 follows entry 208 at the end of Group 3, where entries 206 to 208 already
sit. The catalog count moves from 208 to 209. The JSON, the pipe row and a field-by-field note on which values are
sourced are in the gitignored working file `_local/research/2026-10-22_design-brief-spec/catalog-row.md`.

#### `pairs_with`: checked, empty

The local pm-skills checkout's skills folder was read on 2026-10-22. No skill addresses a design brief.
`develop-solution-brief` sits at `develop` and describes a proposed solution approach, its key decisions and its
trade-offs, so it is a boundary. `tool-design-sprint-brief` is a pre-sprint brief. `tools/known-skills.txt` needs no
change.

#### Risks for the build and the review

1. **Invented structure is the main risk.** The narrow shape is the library's composition. Every section must cite
   a source the build reads, or carry the POSITION label in the companion and the guide. A lens that finds a
   section presented as sourced without a logged source files it as blocking.
2. **The concept line will be crossed in GOOD text and in the example.** A sentence about what the system proposes
   or what the user clicks is how the concept works. The review must read every GOOD line against ADR 0077's table.
3. **Heap is a collision, not a structural source.** Cite its goal sentence and its Problem Brief pairing only. D1's
   list of its section names is the research agent's reading, not a quotation.
4. **Phillips must be quoted only through the three carried sentences.** The completion of his initial-design
   phrase exists only in sweep 3's notes, and the companion may paraphrase it, labelled as such.
5. **Nordin's article is unverified.** Nothing from it may be quoted, and experience brief is not an alias.
6. **The re-score's unsourced ADR 0063 phrase must not travel.** State the project-brief boundary from that bundle's
   own template.
7. **The templates stage has reused the example's scenario in GOOD and WEAK text before.** Before the review
   closes, grep both template and guide for the example's nouns: Saved Views, Recurring Analyst, Priya Nair,
   friction study and Team Lead.
8. **The pitch line must appear in the guide**, as a when-not-to-use row and a TRAP, not only in the companion.

#### What landing this bundle closes elsewhere

1. **The contract's Members line** changes from not yet built to the build date.
2. **`project-brief` gains a dated note, not a rewrite.** Its guide's row 21 and its two templates, at lean line 39 and full
   line 43, route a design brief away. So do its companion's section 8 and its history's line 32. The companion defines the design brief in Wikipedia's commissioning sense. The note says that
   the library now builds the concept-handoff sense as `design-brief`, and that the commissioning brief remains
   unbuilt.
3. **`README.md`'s `discovery-docs` section** (heading at line 227) says four bundles. It becomes five, and the
   members sentence gains which concept goes to design.
4. **The catalog row**, and the catalog count from 208 to 209 in `catalog.md`'s TL;DR.
5. **Every bundle count moves from 49 to 50, and the phase axis from 28 to 29.** `define` then holds two bundles.
   `tools/check-counts.py` gates the markers. The hard-coded counts in the section and MCP-server tests, and the
   prose counts in `AGENTS.md` and `README.md`, need a sweep by hand.
6. **Issue #294.** Its body names entry 207 and describes a brief written before any solution is chosen. Both
   predate PR #305 and ADR 0077. Its family label moves from unassigned to `discovery-docs`.
7. **`docs/internal/backlog.md`**, sections 2, 4 and 6, and **this page's Progress table**.
8. **The first empty alias list in the catalog.** `tools/meta.schema.json` permits empty aliases. The build must
   still check that the atlas and every catalog reader accept `[]` and the (none) cell.
9. **No change** to `problem-statement`, `business-case`, `tools/known-skills.txt`, `atlas/state-overrides.json` or
   check K. ADR 0076 set the precedent that existing members are not swept for a reciprocal mention.

#### The example: Saved Views, by the maintainer's ruling

**Recommended: a design brief for Saved Views, the Acme feature the delivery thread already specifies.**
Confidence: medium. Priya Nair, PM, Reporting, would write it. It would be dated after the 2026-05 Reporting
friction study and before the Saved Views PRD of 2026-06-12. A date of 2026-06-01 fits. It hands the Saved Views
concept to the people who will design it, and the PRD later specifies that concept.

**Facts it may read, all of them Acme's own and older than the brief.** They come from `prd_example.md`, lines
34-48, 57-61 and 65-68. They include the FY26 Time to Insight goal and the friction study's finding about
re-filtering. They include the study's illustrative interview counts and the two earlier deferrals. They include
per-user preferences storage shipping in Q1. They name the Recurring Analyst as the primary user and the Team Lead
as the secondary user. The PRD's three non-goals become what the concept leaves out. The persona comes from
`user-persona_example.md`.

**What it must not cite or contain.**

1. **No document of the Saved Views delivery thread cited as existing.** The PRD, epic, user stories, acceptance
   criteria, design document and test plan are each dated 2026-06-12 or later.
2. **No description of how the concept works.** The PRD's Views control and its menu are the design's output, not
   the brief's input.
3. **No prototype cited as existing.** The PRD cites one on 2026-06-12, and no sibling dates its creation.
4. **No requirement IDs and no performance targets.** Those are `deliver` content.
5. **No Reporting Platform Modernization program**, unless the build finds a sibling that dates it before the brief.

**The alternative, which the maintainer did not choose, was a Question-First Entry brief.** It would hand that concept to designers after the business
case recommended it on 2026-01-20. The product strategy of 2026-01-28 already names the design capacity question-first
entry needs. But that brief would postdate a funding request, which strains the membership sentence. It would also
be the family's first example dated after the decision it relates to.

#### The maintainer's rulings, 2026-10-22

The maintainer answered all ten choices in one sitting on 2026-10-22. Each choice's options, recommendation and
confidence are in the gitignored working file `_local/research/2026-10-22_design-brief-spec/maintainer-options.md`.

1. **The name:** keep `design-brief`, as recommended.
2. **The aliases:** none, as recommended.
3. **The sizes:** lean and full. This overruled the recommendation of one size.
4. **The membership sentence:** widen it by one clause, as recommended.
5. **The chain position:** after the problem statement and before any specification, with no fixed order against
   a business case, as recommended.
6. **The Shape Up pitch:** keep it out, on the stated line, as recommended. The maintainer may still reopen it.
7. **The design-constraints section:** include it, labelled low confidence, as recommended. Under ruling 3 it sits
   in the full size.
8. **The family:** amend `discovery-docs` to `0.5.0`, as recommended.
9. **The example:** Saved Views, as recommended.
10. **The catalog category and stage:** Research / Discovery, at the `definition` stage, as recommended.

These rulings set the spec. They are not the read the contract amendment needs, which happens on the pull request.

### research-docs (founding members): the user research plan and the user research report

**`user-research-plan`** - `research-docs`, **`phase: discover`**, sizes **`[lean, full]`**, default `lean`,
methodology **`methodology-agnostic`**. Catalog **entry 210**, id `user-research-plan`, name
"User Research Plan", added on 2026-10-23 by PR #315 (the user research plan becomes catalog entry 210). Catalog
aliases: `UX research plan`, `research plan`, `usability test plan`, `research protocol`. Catalog
`size_variant`: S. Tracked as issue #316 (bundle: user-research-plan), at `priority:P2`.

**`user-research-report`** - `research-docs`, **`phase: discover`**, sizes **`[lean, full]`**, default `lean`,
methodology **`methodology-agnostic`**. Catalog **entry 18**, id `user-research-report`, name
"User Research Report". Catalog aliases: `UX research report`, `research readout`, `usability study report`,
`usability test report`. Catalog `size_variant`: S/M/L. Tracked as issue #317 (bundle: user-research-report), at
`priority:P2`.

Both are founding members of `research-docs`, the family that
[ADR 0081](decisions/0081-adopt-research-docs-family-contract.md) (adopt the research-docs family contract)
adopted on 2026-10-23 with no member built. **The maintainer ruled on the spec's ten choices on 2026-10-24,
taking every recommendation.** The rulings close this section. Each choice's options and confidence are in the
gitignored working file `_local/research/2026-10-23_research-docs-spec/maintainer-options.md`. No ADR is needed,
because ADR 0081 left exactly these choices to the specs.

#### The recommendation, and how sure it is

**Build both bundles, the plan first, each in two sizes, and chain both examples onto the 2026-05 Reporting
friction study.** Confidence: medium-high for the report, medium for the plan.

- **The report's shape is the better evidenced of the two.** Dovetail, User Interviews, Maze, UserTesting and NIST
  each give a report a named section list. Dovetail and UserTesting describe one study's findings issued at two
  depths, and DHS scales the write-up to the kind of test.
- **The plan's sections are well evidenced, and its sizes less so.** User Interviews names a minimum plan, and
  digital.gov and 18F publish long ones. No source names a short and a long form of one plan.
- **What holds the plan at medium is the usability block.** The alias "usability test plan" promises a reader that
  the plan covers a usability test. The worked example cannot show that, because the friction study was an
  interview study, so the promise rests on the template and the guide.

#### Demand: four shipped examples cite a study nobody has shown

- **Issues #316 and #317** carry the two types at `priority:P2`. The label's own definition is "Queued, but blocked
  on a spec or a maintainer decision", and this spec is the unblocking step.
- **Four shipped examples cite the 2026-05 Reporting friction study as a document that exists.** The PRD example
  lists "Discovery readout: Reporting friction study, 2026-05 (n=12 analysts, illustrative)." in its appendix. The
  design brief, epic and internal announcement examples cite the same study. No bundle can show that readout today.
- **The spike report's guide routes user research away from itself.** `spike-report_guide.md` line 112 names
  `discover-interview-synthesis`, a pm-skills skill, for exploration that "was user research rather than technical
  feasibility". No bundle in this library takes that reader today.
- **Demand does not schedule anything.** Build order is the maintainer's own preference
  ([ADR 0041](decisions/0041-maintainer-preference-sets-the-build-order.md)).

#### Admission: settled by two sweeps on 2026-10-23

Both types cleared [ADR 0030](decisions/0030-templating-scope-markdown-documents.md) (templating scope: Markdown
documents) and [ADR 0048](decisions/0048-one-named-source-clears-the-admission-test.md) (one named source clears the
admission test) on 2026-10-23. The evidence sits in two gitignored digests:
`_local/research/2026-10-23_research-plan-and-usability-test-plan-sweep/digest.md` and
`_local/research/2026-10-23_user-research-report-sweep/digest.md`. In the plan's sweep, 359 of 372 returned
quotations and headings passed a raw-text check, and so did all 25 quotations the main loop added. In the
report's sweep, 273 of 277 passed. Every quotation in this section was checked against the cached raw page or the
repository file.

| Member | Strongest written-form sources | Weight |
|---|---|---|
| Plan | 18F's `research-plan-template.md` on GitHub, an ungated fill-in template with eleven headings; digital.gov's "How to write a research plan", twelve sections in the document's own order; Nielsen Norman Group's research-plan article | Each **admits on its own**. Dovetail, User Interviews, Maze and dscout corroborate with section lists. NSW Digital Service links a Word template, which was not opened, so it corroborates only |
| Plan, usability case | NN/g's "Checklist for Planning Usability Studies", whose step 8 is "Write a Test Plan"; MeasuringU's "What Goes into a Usability Test Plan?" | NN/g states the identity the catalog row rests on: "When planning a usability test, the research plan is often referred to as a test plan" |
| Report | NIST's NISTIR 7742, an ungated fill-in template built on ISO/IEC 25062; UserTesting's three report structures; Dovetail's six sections; User Interviews' six headings; Maze's five | Each **admits on its own**. DHS's usability kit ships a report template whose file was not opened |

**One lineage trap applies to the report.** NISTIR 7742 customizes the ISO/IEC 25062 Common Industry Format for
testing electronic health records. The contract's section 3.6 forbids presenting that regulatory format as general
product practice. The report may cite NIST for its headings and for the summative case, and must name the lineage
in the same sentence.

#### Family fit: settled by ADR 0081, not re-litigated here

[The contract](contracts/research-docs.md)'s section 1 states the membership test both members must meet: each
"plans or reports on one study of the people a product serves". Section 1 also states the boundary sentences
against the experiment pair, the QA pair and the documents that use the findings. Section 2 fixes the axis at
`phase: discover`, labelled the library's POSITION, with its cost stated: both documents serve studies of shipped
products too. Section 4 fixes the shared scenario. ADR 0081 records why the types are two bundles and why no
existing family admits either one. Nothing in this spec's research contradicts any of it. **This spec's job is
what ADR 0081 left open:** the bundle ids and sizes, the sections, the usability block, the examples, the
`pairs_with` claims and the catalog corrections.

#### Bundle ids: the catalog ids

**Keep `user-research-plan` and `user-research-report`.** Confidence: high. Neither id carries a category
prefix to trim, the way `change-log-governance` became `change-log`. The maintainer approved entry 210's id on
2026-10-23. Its qualifier "user" mirrors entry 18's id and keeps the plan from reading as a market research plan.

#### Build order: the plan first, then the report

**Recommended: two builds, the plan first.** Confidence: medium-high. The report's example reports against the
plan's example, so the plan has to exist first, as `experiment-design-doc` preceded `experiment-readout`. The
plan's `related_templates` names the report as `future:user-research-report`, the exact bundle id, because
`tools/check-bundles.py` resolves a `future:` target by bundle id.

**The alternative is one PR that builds both.** `tracking-plan` and `experiment-readout` landed in one PR. The
cost is a review twice the size, and a defect in the plan's example then reaches the report's example before
anyone reads either.

#### Sizes

**The plan: `[lean, full]`, default `lean`.** Confidence: medium.

- **For two sizes.** User Interviews names a minimum: "At a minimum, your research plan should include:". Its six
  items run from "What: Your research question(s) and goals" to "Next steps". digital.gov and 18F publish long
  forms with sections the minimum lacks, such as "Past research", "Roles and responsibilities" and "Ethical
  considerations".
- **For one size.** Dovetail answers its own question, "How long should a research plan be?", with "One to two
  pages." NN/g says the usability test plan "doesn't need to be lengthy". MeasuringU warns that "Test plans, like
  many documents, can take on a life of their own and become bloated and unnecessarily complex." The plan sweep
  found no source that names a short and a long form of one plan, at medium-high confidence.
- **Why the balance tips to two.** In the design brief's spec, the full-only sections rested on the library's own
  construction. Here every full-only section has a named source, so the full variant is sourced, not invented.
- **What would change it.** A ruling for one size would drop the four full-only sections. The guide would then
  route consent and observers into Participants and Logistics.

**The report: `[lean, full]`, default `lean`.** Confidence: high.

- Dovetail: "Executives want one page with the decision; your product team wants the detail behind it."
- UserTesting gives an "Executive summary report (For Stakeholders and Leadership)" and a "Detailed research report
  (For UX and Product teams)".
- DHS scales the write-up by approach. One approach "may or may not result in a formal report", and another lets a
  team "compile a short report".
- **Not three sizes, at medium confidence.** UserTesting's third form, a "Quick feedback snapshot (For Agile
  teams)", lists four items, and each of them maps to a lean section. The catalog's S/M/L is a hypothesis (finding EC-2
  in `STATE.md`), and this evidence supports two sizes.

**Both defaults are `lean`,** as in every two-size member of `qa-docs` and `experimentation-docs`. The worked
examples use the full variant, as most of this library's examples do.

#### Section design: `user-research-plan` (proposed, for the build's research to test)

| Section | Size | What it carries | Sources | Confidence |
|---|---|---|---|---|
| **Why This Study, and the Decision It Informs** | both | Why the study runs now, and which decision its findings will inform | User Interviews' "Why: Business goals"; Dovetail's "Background explains why the study exists and what decision it informs."; dscout's "Part 1: Background"; digital.gov's "Context" | High |
| **Goals and Research Questions** | both | One or two goals, and the questions the study must answer, stated as what the team needs to learn | User Interviews' "What: Your research question(s) and goals"; NN/g's "Purpose and goals of the research study"; digital.gov's "Research goals and questions"; Dovetail's "Research questions describe what you need to learn, not what you'll ask participants." | High |
| **What We Already Know** *(full only)* | full | Earlier research, existing data, and the assumptions this study tests | digital.gov's "Past research"; User Interviews' "3. Gather available data and existing insights"; 18F's template heading "Assumptions" | Medium-high |
| **Method** | both | The method or methods, why they fit the questions, the session format and length, and what participants will see | User Interviews' "How: Methodology"; NN/g's "Method and procedure"; digital.gov's "Research methods"; Maze's "4. Choose the right research method" | High |
| **Participants and Recruiting** | both | Who qualifies and who does not, how many, how they are recruited, and how they are thanked or paid | User Interviews' "Who: Participants"; NN/g's "Participants"; Dovetail's "participants and recruitment criteria"; digital.gov's "Participants and recruiting" | High |
| **Tasks and Measures** *(usability tests only)* | both | The tasks as scenarios, a success criterion for each task, the task and session measures, and the questions before and after the test. Any other method writes one line saying the study is not a usability test | NN/g's "Tasks" and "Metrics, questionnaires"; MeasuringU's "Task Metrics", "Test Metrics", "Pre-Test Questions" and "Post-Test Questions", and "Task Completion: Determine an objective success criteria for each task."; Maze's "6. Write tasks that match your goals" | High on the content; medium on the conditional placement |
| **Schedule and Logistics** | both | The dates, the session times, the place or tool, and how sessions are recorded and noted | User Interviews' "When and where: Research schedule and logistics"; NN/g's "Logistics: time, dates, location, and format of study"; digital.gov's "Timeline"; GOV.UK's "Plan the session times" and "Arrange recording and note-taking" | High |
| **Roles and Observers** *(full only)* | full | Who moderates, who takes notes, and how the wider team watches sessions | digital.gov's "Roles and responsibilities"; 18F's "Team participation"; GOV.UK's "Invite people to watch the sessions"; NN/g's "9. Motivate Team Members to Observe Sessions" | Medium-high |
| **Consent, Privacy and Ethics** *(full only)* | full | How consent is taken, what personal data is captured and how it is kept, and any legal, accessibility or power concerns | 18F's "Ethical considerations"; 18F's template lines "Participants will need to sign a consent form (see attached)." and "Research team should ensure that no PII data is captured."; digital.gov's "Issues for awareness", which asks for "any legal, ethical, accessibility, bias, or power concerns" | Medium-high |
| **What Happens to the Findings** | both | Which report the study produces, for whom and by when, how the report will be structured, and which decisions the findings feed | User Interviews' "Next steps"; Dovetail's "share-out plan"; Maze's "8. Decide how you'll present your findings"; 18F's "Outputs and outcomes"; MeasuringU's "If possible, try to outline how the report will be structured in the test plan." | High |
| **Related Documents** *(full only)* | full | Links to the session guide, the screener, the consent form, the prototype and earlier reports | NN/g's "Relevant documents", which names "consent forms, recruitment documentation, and facilitator guides"; digital.gov's "Important links"; dscout's "Part 7: Resources/Links to Documentation" | Medium-high |

**Lean holds the seven rows marked both. Full holds all eleven, in the table's order.** The lean set is User
Interviews' six-item minimum plus the usability block. The full set matches the length of digital.gov's twelve
sections and 18F's eleven headings without copying either.

**What stays out of the plan at any size.**

- **The session script.** dscout embeds one ("Part 5: Interview Guide"), and 18F's template carries an "Opening
  script". This library treats the interview guide as catalog entry 25, a separate candidate the contract names
  and does not admit. So the plan links the guide in Related Documents and does not hold it. Dovetail draws the
  same line from the other side, separating a research question from "an interview question that helps answer
  it". Confidence: medium.
- **A standing research plan or a research strategy.** Maze: "While your UX research plan should be based on
  strategy, it's not the same thing." GOV.UK's service-wide research plan is the standing document the contract's
  section 1 excludes.
- **The request for the study.** Dovetail separates the two: "A brief is the request", and "A plan is the
  response". The plan restates the request as goals and does not stand in for it.

#### The usability block: where the alias's promise is kept

ADR 0081 calls the accepted alias a scope promise: "usability test plan" names a document that often runs on a
shipped product. This spec keeps the promise in four places.

1. **The block sits in both sizes,** so a reader who picks the lean plan for a small usability test finds it.
2. **It is one conditional section, not a format.** NN/g's usability content list is its research-plan list with
   the method fixed, plus "Tasks" and "Metrics, questionnaires". That block nests inside the general shape, so
   [ADR 0028](decisions/0028-adopt-a-format-axis.md)'s format axis is not needed. A method that is not a usability test
   writes one line, by the library's convention against deleting sections.
3. **The report mirrors it** with a Task Results section in both sizes, under the same condition.
4. **The guide's first line separates the alias from two near-misses** in `manifest.json`: `test-plan`'s alias
   "test plan" and `experiment-design-doc`'s alias "A/B test plan". The report's guide does the same for
   `test-summary-report`'s aliases "test report" and "test results".

**The worked example cannot exercise the block.** Four sibling examples describe the friction study as interviews,
and the design brief's handoff passes on "the full interview notes". So the plan's example marks Tasks and Measures
not applicable in one line, and the report's example does the same for Task Results. The templates' GOOD text for
both blocks uses a usability test unrelated to the example, which the shareable-boundary rule requires anyway.
Confidence that this demonstrates the alias well enough: medium.

#### Section design: `user-research-report` (proposed, for the build's research to test)

| Section | Size | What it carries | Sources | Confidence |
|---|---|---|---|---|
| **Summary** | both | The answer up front: what the study found and what it recommends, in a few lines | Dovetail's "a summary that states the answer up front"; NIST's "EXECUTIVE SUMMARY"; UserTesting's "Key Takeaways (3-5 bullet points)" | High |
| **Background and Objectives** *(full only)* | full | Why the study ran, the decision it informs, and a link to the plan | Dovetail's "background and objectives (two or three sentences on why the study ran)"; UserTesting's "Background & Objectives"; Maze's "Your introduction should lay out your research goals, plan, and scope." | High |
| **Research Questions and Answers** | both | Each question the plan set, with a short answer and the findings behind it. A question the study could not answer says so | Maze's "Research questions the report is hoping to answer"; UserTesting's "Research Questions"; User Interviews' "Actionable reports should relate back to the initial research question". One answer per question is the library's POSITION, from the contract's "It answers the questions the plan set out." | Medium-high |
| **What We Did** | both | The method, the participants and the dates, the limits of the sample, and one line on anything that ran differently from the plan | Dovetail's "method and participants"; NIST's "METHOD" and "PARTICIPANTS"; UserTesting's "Methodology". The deviation line is the library's POSITION, as in `experiment-readout`'s Context and Setup | High; medium on the deviation line |
| **Key Findings** | both | Each finding, how many participants showed it, and the evidence a reader can follow | Dovetail's "key findings" and "A one-page summary with linked evidence beats a forty-slide deck nobody opens."; Maze's "Key findings"; User Interviews' "Key learnings"; UserTesting's "Use direct quotes or clips to support findings" | High |
| **Task Results** *(usability tests only)* | both | Each task's completion, errors and time, and the questionnaire scores the plan named. Any other method writes one line | NIST's "USABILITY METRICS" and "RESULTS"; UserTesting's "Include quantitative data where applicable (e.g., success rates, charts, QX Score visualizations)"; the plan-side measures this section reports, such as Maze's "Successful task completion" in its usability plan guide | Medium |
| **Recommendations** | both | What the team should do next and why, each recommendation tied to findings. It records no decision | Dovetail's "recommendations"; User Interviews' "Recommendations"; UserTesting's "Prioritized based on impact"; Maze's "Next steps" | High |
| **Open Questions** *(full only)* | full | What the study raised and did not answer, and what research would answer it | Dovetail's "open questions" | Medium |
| **Appendix** *(full only)* | full | The session list, the materials used, and where the raw notes live | Maze's "Appendix"; NIST's "APPENDICES"; UserTesting's "Full responses, session details, additional data" | High |

**Lean holds the six rows marked both. Full holds all nine, in the table's order.** The order follows
UserTesting's detailed report, which puts "Research Questions" before "Methodology". The answers point down to the
findings that support them.

**What stays out of the report at any size.**

- **A decision.** The contract's section 1: "A member here may recommend, but it records no decision."
- **A framed problem or a chosen concept.** Those are `problem-statement` and `design-brief`. A finding may say
  what costs people time. It does not frame that as the problem to solve, or name the concept to design.
- **An aggregate across studies.** Catalog entry 17, the Voice of Customer report, aggregates "ongoing,
  quarterly", and the contract excludes it.
- **A deck format.** NN/g: "Whether the report is a lengthy Word document or a presentation deck, it's meant to be
  consumed asynchronously". No source shows a deck structurally distinct from the written sections, so this spec
  recommends no format under ADR 0028, at medium confidence. The guide may say a deck can carry the same sections.

**A report with no written plan behind it** fills Research Questions and Answers from what the study set out to
learn. The sources tie a report to its plan where both exist. GOV.UK says agile teams often skip a formal report,
and no source was asked how often a report runs without a plan. The guide states that case in one line.

#### Boundaries with each named neighbour

- **The other member.** The plan states the questions before the study runs. The report answers the same
  questions after the study ends, and links back to the plan.
- **The experiment pair (`experimentation-docs`).** Itamar Gilad: "Per this definition an A/B test is an
  experiment, but a usability test is not." Gilad is already logged in `experiment-readout`'s research log. The
  contract holds, as its POSITION, that a study which allocates participants between variants and applies a
  decision rule is an experiment, whatever it is called.
- **The QA pair, `test-plan` and `test-summary-report` (`qa-docs`).** They verify a product increment against a
  specification and grade it. A usability study records how people use a product, and its report holds
  observations, not a verdict. NIST's summative report on a "final product" is the nearest edge, and the report's
  companion must name it.
- **The documents that use the findings (`discovery-docs`).** `user-persona` records an evidence basis,
  `problem-statement` an evidence table, and `design-brief` a short summary for designers. Each takes findings
  and frames or decides. None reports a study.
- **`project-brief`.** NSW Digital Service places the research plan "After you have been given an initial project
  brief, but before you commence any official research activities." The project brief asks for authority to start.
  The plan sets out one study inside that authority.
- **`spike-report` (`decision-docs`).** A spike tests technical feasibility. Its guide sends user research
  elsewhere, at line 112.
- **Catalog entries 25, 26 and 28.** The interview guide (25) and the survey instrument (26) are used during a
  study. The diary study plan (28) is a method-specific sibling of the plan: the 2026-10-23 placement pass read
  NN/g's and User Interviews' diary-study pages, which give it its own structure. The plan's guide names all
  three as unbuilt candidates.
- **Catalog entry 17 and standing research documents.** A Voice of Customer report, a research repository and a
  service-wide research plan are maintained over time. The contract excludes all of them.
- **A retrospective on how the study ran** belongs to `process-docs`.

#### The worked examples: the 2026-05 Reporting friction study

**The plan's example plans the friction study, and the report's example is its readout.** Contract section 4 fixes
the study. Both examples are dated before the design brief of 2026-06-01, which cites the study.

**Facts the two examples must carry, with no contradiction.** Each comes from a shipped sibling example. The report
must be findable by the PRD's own citation, "Discovery readout: Reporting friction study, 2026-05".

| Fact | Value | Where it is stated |
|---|---|---|
| Name and date | "Reporting friction study", 2026-05 | `prd_example.md:12`, `:173`; `design-brief_example.md:16-17` |
| Sample and method | 12 analysts, interviewed | `prd_example.md:44`, `:173`; `design-brief_example.md:62`; `epic_example.md:45` |
| The top finding | Re-filtering was "the single most frequent repeated action in the dashboard, ahead of export and share" | `prd_example.md:35-36`; `design-brief_example.md:33-35`; `epic_example.md:45-46` |
| First count | 9 of 12 described rebuilding filters by hand several times a day | `prd_example.md:44`; `design-brief_example.md:62-63` |
| Second count | 3 kept a personal text file of "the filters I always use" | `prd_example.md:45`; `design-brief_example.md:63-64`; `epic_example.md:47` |
| The cost | Broken flow, and the risk of analysing the wrong slice from a filter set rebuilt from memory | `prd_example.md:46-47`; `design-brief_example.md:64-66` |
| The reframing | The study turned re-filtering from a feature gap into a recurring time tax, after two deferrals because filtering "worked" | `prd_example.md:36-37`; `design-brief_example.md:35-36`; `epic_example.md:44-49` |
| The sharing clause | The pattern found "more often than any other" included rebuilding a setup "because nobody else could reach their saved setup" | `announcement-internal-comms_example.md:66-68` |
| The Team Lead | A second audience Priya Nair named from the study, described only as far as the study went | `design-brief_example.md:53-55`, `:60-61` |
| Questions not asked | Who owns a shared lens, and what a saved lens does when its dashboard changes: "The friction study asked neither question." | `design-brief_example.md:103-106` |
| Coverage | Only the small set of report types the study happened to cover | `design-brief_example.md:110-112` |
| The notes | The full interview notes exist, and the design team receives them on 2026-06-01 | `design-brief_example.md:116-118` |
| Illustrative | The counts are "illustrative counts from a 12-person study" | `prd_example.md:45-46` |

**Facts older than the plan, which the examples may read.** The 2026-01-05 user persona defines the Recurring
Analyst. The FY26 product strategy (2026-01-28) carries the "Time to Insight" goal. The FY26 roadmap
(2026-02-11) has Saved Views in its Now lane, "Being specified now", and shared views across a team in its Next
lane (`product-roadmap_example.md:50-52`, `:63-65`).

**Two traps the examples must route around.**

1. **Two different 12-person studies exist.** The persona rests on interviews held in November and December 2025,
   n=12 (`user-persona_example.md:42`), across nine mid-market customer accounts
   (`problem-statement_example.md:53-54`). In that study 9 of 12 raised re-filtering and 6 of 12 kept a
   spreadsheet (`user-persona_example.md:54`, `:71`). The friction study is a second study, in May 2026, where 3 of 12
   kept a text file. The plan's What We Already Know may cite the persona's study with its own figures. Nothing
   may merge the two sets of figures.
2. **The plan must not presuppose its own finding.** Re-filtering is already known in April 2026: the persona
   lists it, and the roadmap is specifying Saved Views. What the study adds is measurement, and the reframing is a
   finding. So the plan's questions ask where analysts lose time between opening a report and acting on it. They
   may name the deferred request as one thing to probe, and they may not assume the answer.

**The sharing clause is the hardest fact to honour.** The report's top finding has to hold the PRD's "ahead of
export and share" and the announcement's "because nobody else could reach their saved setup" together. One honest
reading is that the only saved setups were personal notes no teammate could see. The build chooses the wording,
and the review checks it against both sentences.

**Recommended dates, chosen rather than read from a sibling.** The plan is dated 2026-04-20. Sessions run from
2026-05-04 to 2026-05-15. The report is dated 2026-05-27, before the design brief of 2026-06-01. Confidence:
medium.

**Recommended author.** Priya Nair, PM, Reporting, writes both, with sessions run by Acme's UX Research function,
which the risk register names as co-owner of risk R-04 (`risk-register_example.md:69`). No new named person is
needed. A build that adds one greps every example for the name first.

**Recommended method.** One-to-one interviews of about an hour, each with a walkthrough of the analyst's own
dashboard. That fits "interviewed" in every sibling, and it lets the report count the repeated action it reports.
A walkthrough of a participant's own work is not a usability test, so the Tasks and Measures block stays not
applicable. Confidence: medium.

**The shipped-product clause applies.** The friction study studies a dashboard customers already use. The
contract's section 2 says a member that serves such a study still declares `discover`, "and its companion must
say why". Both companions explain that clause with this example.

**What the examples must not cite or contain.**

1. **No document dated after the report**, as existing: the design brief, PRD, epic, user stories, test plan,
   announcement and later Saved Views documents.
2. **No concept and no decision.** The design brief of 2026-06-01 weighs candidate concepts and names Saved Views
   as the chosen one. The report recommends a next step, and names no concept as chosen.
3. **No answer to the two questions the study did not ask**, and no claim about report types beyond the small set
   it covered.
4. **No minutes-per-day figure.** The business case templates' GOOD text carries one, which is illustration and
   binds nothing. A report that states its own figure invites a reader to reconcile two numbers that were never
   meant to meet.
5. **No figure from the persona's study presented as the friction study's.**

#### Metadata

| Field | `user-research-plan` | `user-research-report` | Why |
|---|---|---|---|
| `family` | `research-docs` | `research-docs` | ADR 0081 |
| `phase` | `discover` | `discover` | Contract section 2; check K gates it |
| `sizes_available` | `[lean, full]` | `[lean, full]` | See Sizes |
| `default_size` | `lean` | `lean` | As in every two-size member of `qa-docs` and `experimentation-docs`. This is judgment |
| `status` | `beta` | `beta` | Every bundle starts at `beta` |
| `methodology` | `methodology-agnostic` | `methodology-agnostic` | The sources span UX research vendors, government digital services and an ISO reporting format. One lineage would misdescribe the others. The catalog's two values differ from each other and are not carried. This is judgment |
| `pairs_with` | `[]` | `[discover-interview-synthesis]` | See below |
| `related_templates` | `[future:user-research-report, user-persona, problem-statement, design-brief, test-plan, experiment-design-doc]`, inline | `[user-research-plan, user-persona, problem-statement, design-brief, test-summary-report, experiment-readout]`, inline | The other member, the three documents that use the findings, and the two near-miss neighbours. Inline, because check I drops the first entry of a block list. This is judgment |
| `aliases` | the catalog's four | the catalog's four | Both sets were recorded on 2026-10-23 with their sources |

#### `pairs_with`: one honest pairing, for the report

**Recommended: the report pairs with `discover-interview-synthesis`, and the plan pairs with nothing.**
Confidence: medium-high.

- The skill is present in the local pm-skills checkout, as tracked source at
  `skills/discover-interview-synthesis/SKILL.md`, checked on 2026-10-23.
- Its own "When to Use" list names "After usability testing sessions to consolidate observations" and "When
  stakeholders need a summary of research findings". That is the report's job.
- `spike-report_guide.md` line 112 already routes user research to the same skill.
- No pm-skills skill plans a study, so the plan's `[]` is honest, not a gap.
- The ID is not yet in `tools/known-skills.txt`. The report's build adds it, with a verification line in the
  file's own format.

The contract's section 2 allows a pairing "only where that claim is true of that member". This pairing is a claim
about the skill's job, and not a reason to build or rank either bundle.

#### Catalog corrections the landing PRs should check (per decision-procedures.md section 1)

The PR that adds this spec edits no catalog field.

- **Entry 18's `size_variant: S/M/L`.** The evidence supports two sizes, so the report's landing PR corrects it to
  match the shipped `[lean, full]`.
- **Entry 18's relationships, "Personas" and "PRD".** The report's landing PR adds "User Research Plan", which
  entry 210 already names in the other direction.
- **Entry 210's `size_variant: S`.** If the maintainer rules two sizes, the plan's landing PR corrects it.
- **The two owners differ:** "UX Researcher" on entry 18, "UXR / PM" on entry 210. Nothing read settles either.
  This spec recommends no change, and the companions say that either role writes either document.
- **The two methodology values differ**, and the contract makes methodology descriptive. The metadata above
  carries neither, and the catalog rows stay as recorded.

#### Risks for the build and the review

1. **The binding facts are spread across five examples.** A lens that reads only the PRD will miss the
   announcement's sharing clause and the design brief's two unasked questions. The review brief lists the table
   above.
2. **The two 12-person studies invite a merge.** The review greps both examples for "6 of 12" and "spreadsheet".
3. **The plan's example must not know its own answer.** A plan whose questions already name re-filtering as the
   finding reads as written after the study.
4. **The templates stage has reused the example's scenario in GOOD and WEAK text before.** Before the review
   closes, grep both bundles' templates and guides for Saved Views, Recurring Analyst, Priya Nair, friction study,
   Team Lead and re-filter.
5. **The NIST lineage trap.** The report may cite NISTIR 7742's headings, and must say in the same sentence that
   it customizes ISO/IEC 25062 for electronic health records.
6. **The report must recommend without deciding.** "We recommend" is in contract. "The team will build" is not.
7. **No GOOD line may present the usability block as optional detail.** For a usability test it is the core of the
   plan, and NN/g's and MeasuringU's lists put it there.
8. **The two alias near-misses need first lines in each guide**, as `change-request_guide.md` keeps for its own
   `rfc` collision.
9. **The full plan holds eleven sections and may run long.** The MCP server's output cap fails a variant above
   roughly 8,000 approx tokens, and `experiment-readout`'s full variant sits at 6,600. The build checks
   `approx_tokens` for the full plan before landing. If it runs long, trim guidance comments before dropping a
   sourced section.

#### What landing these bundles closes elsewhere

At the first landing:

1. **The contract's "Members at adoption" line** changes to name the built member and its date.
2. **Check K's `research-docs` entry stops being latent.** The gate then checks a real member.
3. **The family count moves from 10 to 11** in `AGENTS.md` (lines 44 and 152), the README badge and its two
   prose counts (lines 158 and 360; 360 is 368 since the plan's landing), and wherever else `tools/check-counts.py` gates a family marker. The README's
   "ten complete families" needs care: a family with one of two members built is not complete.
4. **The README gains a `research-docs` family section,** not just a count change.
5. **Issue #316 or #317** is closed by its landing PR and relabelled to `status:built`. A landing PR closes its
   issue but changes no label, so the relabel is a separate step.

At the report's landing:

6. **`spike-report_guide.md` line 112** gains a dated note routing user research to `user-research-report`, beside
   the pm-skills skill it already names.
7. **`tools/known-skills.txt`** gains `discover-interview-synthesis`, if the maintainer accepts the pairing.
8. **The four examples that cite the friction study** gain no edit. Contract section 4 binds the new examples to
   them, not the reverse, as ADR 0076 set for reciprocal mentions.
9. **The plan's `related_templates` drops the `future:` prefix** from `future:user-research-report`, with a
   history line, in the report's landing PR. `tools/check-bundles.py` raises its stale-reference failure as soon as
   that exact id exists on disk.

#### The maintainer's rulings, 2026-10-24

The maintainer answered all ten choices in one line on 2026-10-24: "I approve your ten choices". Each choice's
options, recommendation and confidence are in the gitignored working file
`_local/research/2026-10-23_research-docs-spec/maintainer-options.md`.

1. **The bundle ids:** keep the catalog ids, `user-research-plan` and `user-research-report`, as recommended.
2. **The plan's sizes:** lean and full, as recommended, over lean only.
3. **The report's sizes:** lean and full, as recommended.
4. **The usability block:** one conditional section in both sizes of each member, as recommended.
5. **The session guide:** the plan links it and does not hold it, as recommended.
6. **`pairs_with`:** the report pairs with `discover-interview-synthesis`, and the plan with nothing, as
   recommended. The ID enters `tools/known-skills.txt` at the report's landing.
7. **The examples:** Priya Nair as author, UX Research running sessions, interviews with a dashboard walkthrough,
   with the plan dated 2026-04-20 and the report 2026-05-27, as recommended.
8. **The build order:** two builds, the plan first, as recommended.
9. **Defaults and methodology:** `lean` for both, and `methodology-agnostic` for both, as recommended.
10. **The catalog corrections:** made at each landing, as listed above, as recommended.

These rulings set the spec. A build is a separate run, and it needs its own go
([ADR 0041](decisions/0041-maintainer-preference-sets-the-build-order.md)).

#### Notes from the plan's build, 2026-10-24

The plan was built on 2026-10-24, on the maintainer's go of the same day. Its research log,
[`user-research-plan_research-log.md`](../../templates/user-research-plan/user-research-plan_research-log.md),
tests this section's sentences against 37 sources in its Finding 11. Six sentences are weaker than this section
states them. They stay as written above, so that line citations into this section keep their targets, and each is
corrected here.

- **digital.gov's "twelve sections"**, in the source table's Plan row and after the section design table. The
  cached page names eleven plan headings, from "Title of research plan" to "Important links". A twelfth heading,
  "Best practices", follows the list and points to other guides, which may be what the count included. Nothing in
  the section design turns on the number. Confidence: medium, because the cached copy is a text extraction.
- **The session script's exclusion.** The log's Finding 3 counts five sources that embed a session script in the
  plan and two that link one. The exclusion stands, carried by catalog entry 25 rather than by the sources. The
  bundle's guide and companion call it this library's POSITION.
- **Gilad's test-and-experiment line**, in the boundary list above and in the contract's section 1. His next
  sentences qualify it: "I realize that this is not the common definition used in the industry - in many cases the
  words test and experiment are used interchangeably." The bundle quotes the line with that qualifier. The
  contract's copy has none, and changing it is the maintainer's call.
- **Nielsen Norman Group's one-study line**, in the contract's section 2. The same article allows that "sometimes,
  a research plan could include numerous studies or phases of research". The contract quotes the first sentence
  without that clause, so its one-study membership test is the library's POSITION against a practice the source
  names. Changing the contract is the maintainer's call.
- **The `project-brief` boundary** rests on Digital NSW alone. No other source the build read places the plan after
  a project brief.
- **The facts older than the plan** are each correct, but two carry a trap. The strategy's goal sentence goes on
  to name later documents' versions of the goal, and the roadmap calls Saved Views the second-view problem. The
  example names the strategy's goal without either later version, and does not cite the roadmap.

#### Notes from the report's build, 2026-10-27

The report was built on 2026-10-27, on the maintainer's go of the same day. Its research log,
[`user-research-report_research-log.md`](../../templates/user-research-report/user-research-report_research-log.md),
tests this section's sentences against 52 sources in its Finding 13. Ten places are weaker than this section states
them. They stay as written above, so that line citations into this section keep their targets, and each is
corrected here.

- **The word "regulatory" for NIST's format**, in the admission paragraph and in the contract's section 3.6. No
  Quotable line in the log supports it. NIST describes an ANSI standard for software procurement and a template
  customized for electronic health records, and the bundle never calls either one regulatory.
- **Background and Objectives as full only**, in the section design table. Every short form with an objective
  line puts it near the top. The bundle keeps the section full only.
- **Maze's span on research questions**, in the same table. It sits in the stored copy but is not a Quotable line.
  The row holds on UserTesting and User Interviews.
- **NIST's and Maze's appendix headings**, in the same table. One was lost in a dropped quotation, and the other
  appears only in lower case. The Appendix row holds on UserTesting's "Full responses, session details, additional
  data".
- **The deck exclusion.** NN/g's span is not a Quotable line in the report's log, and Maze's PAS framework gives a
  deck its own structure. The no-format recommendation stands on other grounds, set out in the log's Finding 6.
- **GOV.UK on agile teams.** This section paraphrases GOV.UK as saying agile teams "often skip a formal report".
  GOV.UK says agile researchers "won't have time to write research reports", and allows brief summaries. The
  word "often" is softer than the source, and the paraphrase drops the qualifier.
- **NIST's "final product" span**, in the boundary list, in the contract's section 2 and in ADR 0081. It is not a
  Quotable line in the report's log. The QA edge holds on NIST's summative lines instead.
- **The boundary list names no debrief.** Two Dovetail articles distinguish a debrief from a report, and Mozilla
  separates a debrief from analysis. The bundle's guide and companion carry the debrief as a neighbour.
- **The binding facts' wording against the epic.** The epic says re-filtering was the most frequent repeated
  action "inside a dashboard" and that three analysts kept "a personal note of" their filters. The example
  follows the PRD's wording and "personal text file", as the binding-facts table does, because the PRD's
  citation is how a reader finds the report.
- **The example's variant beside the plan's promise.** The plan's example promises "a short written readout", and
  the report's example uses the full variant. The full example reads short, at about 130 lines.

Three further notes from the build:

- **Gap candidate 17 changed after the maintainer's hand reads.** A date after which findings should be checked
  again stays out. The product version participants were reacting to entered What We Did as an ASK, on one vendor
  source (Koji), with no field of its own.
- **The meta drifted from the metadata table above, as the plan's had.** The drafting agent replaced the two
  near-miss neighbours in `related_templates` with the example's chain siblings, and swapped two catalog aliases
  for its own. Both were restored to this section's values before landing. No review lens reads the meta or the
  history, so both were checked by hand.
- **The example's title is the PRD's citation**, "Discovery readout: Reporting friction study, 2026-05", so that a
  reader following the PRD finds it. Only the PRD cites the readout by that name; the other three examples cite
  the study.


### discovery-docs (sixth member, at `discover`): the Lean UX Canvas

**`lean-ux-canvas`** - `discovery-docs`, **`phase: discover`**, size **`[lean]`** (recommended), methodology
**`Lean UX`**, no catalog row until the build lands (entry 211), alias **"Lean Product Canvas"** (recommended).
Issue #330 (bundle: lean-ux-canvas), priority P2. The family decision is
[ADR 0082](decisions/0082-lean-ux-canvas-joins-discovery-docs-at-discover.md) (lean-ux-canvas joins
discovery-docs at discover), **proposed 2026-10-30**. It amends the contract, so it stops for the maintainer's
read. Nothing in this section is ruled yet: the choices at its end wait for one answer line.

#### The recommendation, and how sure it is

**Build Jeff Gothelf's Lean UX Canvas as the sixth `discovery-docs` member, at `phase: discover`, in one size.**
Confidence: medium.

The canvas frames one initiative on one page. It links a business problem, the outcomes the business wants, the
users, the outcomes those users want, and the candidate solutions. It turns those links into hypotheses. It then
names the most important thing to learn first and the least work that would learn it. All of that comes before
anyone commits to building.

**What holds the confidence at medium.** Admission is not in doubt. Two things are argued rather than sourced.
The duplication answer rests on the document's job, and admission sweep 7 read the box map the other way. The
cadence exception is the second one this family has taken.

#### Demand: an issue, a sweep, and the maintainer's choice

- Issue #330 opened on 2026-10-27, from the PM resources run of 2026-10-23.
- Admission sweep 7 ran on 2026-10-29 and recommended a decline at medium confidence. Its digest is held locally,
  at `_local/research/2026-10-29_admission-sweep-7/digest.md`.
- On 2026-10-30 the maintainer chose to include the canvas and set its priority to P2. Under
  [ADR 0041](decisions/0041-maintainer-preference-sets-the-build-order.md) (maintainer preference sets the build
  order), that choice is the reason to build. The sections below make sure the build is sound.

#### Admission: settled on the originator's own pages

Every quotation in this section passed a raw-text check on 2026-10-30, after each site's terms were read. The
check is held locally, at `_local/research/2026-10-30_canvases-placement/recheck-out.json`.

- **Check 1, a named source publishes the written form.** Gothelf's
  [Lean UX Canvas V2](https://jeffgothelf.com/blog/leanuxcanvas-v2/) (2019-09-09) gives each of the eight boxes
  a heading, a rationale and a worked example. Under
  [ADR 0078](decisions/0078-maps-canvases-and-session-records-are-templatable-through-their-written-form.md)
  (canvases are templatable through their written form), that is the written form. Dean Peters's
  [`template.md`](https://raw.githubusercontent.com/deanpeters/Product-Manager-Skills/main/skills/lean-ux-canvas/template.md)
  already renders it as Markdown: "Use this template to capture the eight Lean UX Canvas boxes."
- **Check 2, phase fit.** The canvas fits `discover`, not `define`. The argument is in ADR 0082's "Why
  `discover`, not `define`".
- **Check 3, the written form of a canvas.** ADR 0078 admits it.
- **Check 4, no built bundle does its job.** Argued in ADR 0082's duplication section, labelled the library's
  POSITION.
- **Check 5, a software audience.** Gothelf wrote in 2024: "These aren’t prompts specific to UX designers,
  product managers or software engineers." An Atomic Object post says the canvas "can be leveraged at the
  beginning of new software products to help align the team around the problem".

**The terms rule.** jeffgothelf.com has no terms page that a probe of four common paths could find, and its home
page carries no terms link. GitHub's terms permit reading public repositories. Atomic Object's terms were read in
sweep 7 and carry no bar.

#### The name: the canvas has been renamed

**Gothelf renamed the canvas on 2024-11-04.** "The canvas is now called the Lean Product Canvas." He kept its
structure: "fundamentally there was nothing wrong with the canvas in its current state rather its positioning
and prompts had to shift to reflect a broader scope". The same post changed three prompts, by his account.
Box 2 gained the language of his OKR book, Box 4 gained "jobs to be done" language, and Box 7 now points to his
Hypothesis Prioritization Canvas.

**Recommended: id `lean-ux-canvas`, title "Lean UX Canvas", alias "Lean Product Canvas".** Confidence: medium.
The older name is the one issue #330, the third edition of the Lean UX book and every secondary source read use.
The new name must be an alias, so a reader who searches for it finds the bundle. **The alternative** is id
`lean-product-canvas`, which follows the originator's current name and would need issue #330 retitled.

**The build's research must read the 2024 PDF.** Gothelf's post links a download of the Lean Product Canvas. This
spec did not open it. The build should take each box's wording from that PDF where it differs from the 2019
version, and record both in the companion.

#### Phase and family: `discovery-docs`, at `discover`, by a small amendment (ADR 0082)

**The membership sentence admits it as written.** A `discovery-docs` member exists "to decide whether to build
something, or which concept to design, before anyone commits to building it." The canvas ends on Box 7, "What’s
the most important thing we need to learn first?", and Box 8, "What’s the least amount of work to learn the next
most important thing?"

**It is written as an initiative starts.** Gothelf: "We designed these two canvases to help teams have the right
conversations as they set out on new initiatives together."

**It is revised while its experiments run, which needs the second cadence exception.** Gothelf's how-to page
closes the loop after Box 8: "If we should, then we ask the questions again in box number 7." The Atomic Object
post reports that "there came a point where the canvas had enough definition that it was essentially abandoned
in favor of other tools". The exception is bounded the same way: revised while one initiative's experiments run,
finished when the team commits, changes course or stops.

**Not `experimentation-docs`.** That contract admits a document that "plans or reports on one discrete test of a
hypothesis". The canvas frames many hypotheses and plans no test in detail. Gothelf says experiment design
"can’t really be boiled down into a box on a canvas". That contract also excludes "a test run before anything
is built, to decide whether to build it".

#### Where it sits in the chain (POSITION)

**Before `experiment-design-doc`, and before `design-brief` or the PRD.** Box 8 names the least work that would
test the riskiest assumption. When that work is a real experiment, `experiment-design-doc` plans it. When the
team commits to a concept, `design-brief` hands it to designers, or the PRD specifies it. No source states this
sequence, so it is the library's POSITION.

**`problem-statement` may come first, or not at all.** A team that framed its problem in a problem statement can
copy it into Box 1. A team that did not can start from the canvas. Gothelf's how-to page starts there: "We’ll
start off with the business problem statement."

#### Boundaries with each named neighbour

| Neighbour | The line |
|---|---|
| `problem-statement` | A problem statement frames one problem "before anyone names a solution". The canvas names candidate solutions in Box 5 and links them to outcomes in Box 6 |
| `experiment-design-doc` | It plans one test of one hypothesis, with variants, allocation, metrics and a decision rule. The canvas picks which hypothesis to test and sketches the least work in one box |
| `design-brief` | It hands one chosen concept to designers. The canvas has not chosen a concept |
| `product-vision` | Its default `canvas` format states a whole product's direction for years. The Lean UX Canvas frames one initiative for weeks |
| `user-persona` | It is a researched portrait. Box 3 names the users in a line and may point to a persona |
| `lean-canvas` (ADR 0083) | Ash Maurya's canvas models a whole business: channels, revenue, costs. Gothelf's frames one initiative's hypotheses and asks nothing about revenue or cost |
| Jeff Patton's Opportunity Canvas | Not built and not admitted here. Patton's page calls it "the right abstraction level for discussing a new feature idea for an existing product", which overlaps this canvas. The companion should name it and say the library ships one of the two |
| Gothelf's Lean Strategy Canvas | Not admitted here. Gothelf calls it a tool "designed to set up better work using the Lean Product Canvas". It would be its own candidate |
| Product Opportunity Assessment (#312) | Marty Cagan's go or no-go assessment of one opportunity, still a candidate. Its boundary with this canvas is untested |

#### Sizes: one, recommended

**`[lean]`, one size.** Confidence: medium-high. Gothelf publishes one shape, and no source read splits a short
canvas from a long one. **What would change the recommendation:** a source that publishes a short and a long
form of the canvas as one type.

#### Section design (proposed, for the build's research to test)

The eight boxes, in Gothelf's numbering, then one section this library adds.

| # | Section | What it holds | Source |
|---|---|---|---|
| 1 | Business Problem | What changed in the world, and why it is a problem for the business now | Gothelf, Box 1 |
| 2 | Business Outcomes | The change in someone's behaviour the business wants, measurable | Gothelf, Box 2; the 2024 prompt adds OKR language |
| 3 | Users | Who the team is solving for, including admins and buyers, not only end users | Gothelf, Box 3 |
| 4 | User Outcomes and Benefits | What the users want to achieve, and how they will feel; the 2024 prompt adds jobs to be done | Gothelf, Box 4 |
| 5 | Solutions | Candidate solutions, "big, small, innovative and perhaps a bit “weird.”" | Gothelf, Box 5 |
| 6 | Hypotheses | A table, one row per hypothesis, in Gothelf's grammar: business outcome, user, benefit, solution | Gothelf, Box 6 |
| 7 | What We Need to Learn First | The riskiest assumption among the hypotheses, chosen for right now | Gothelf, Box 7 |
| 8 | The Least Work to Learn It | The smallest experiment or research that would test it | Gothelf, Box 8 |
| 9 | Revisions and What Takes Over | A dated row per pass through Boxes 7 and 8: what was learned and which boxes changed. Then the document that takes over when the canvas is finished | The library's POSITION, from the cadence exception and the family's successor obligation |

**What stays out.** A test plan with variants, allocation or a decision rule belongs in `experiment-design-doc`.
A specification of how a solution works belongs in the PRD. A revenue or cost model belongs in `lean-canvas`.

**Section 9 is the library's addition.** No source read gives the canvas a revision log. The cadence exception
needs one, because a canvas revised without a record cannot show what the team learned. The maintainer may
strike it (choice C5).

#### Metadata

| Field | Value |
|---|---|
| `id`, `doc_type` | `lean-ux-canvas` |
| `title` | Lean UX Canvas |
| `family` | `discovery-docs` |
| `phase` | `discover` |
| `sizes_available`, `default_size` | `[lean]`, `lean` |
| `methodology` | Lean UX |
| `aliases` | Lean Product Canvas |
| `pairs_with` | `[]`; no skill in `tools/known-skills.txt` addresses the canvas, checked 2026-10-30 |
| `catalog_ref` | entry 211, added when the bundle lands |

#### The catalog row the build PR adds

Entry 211, **Lean UX Canvas**, alias Lean Product Canvas, category Research / Discovery, owner Product team
(cross-functional), size S. The row's `owner`, `formality`, `rarity` and `category` are this spec's judgment, not
sourced facts, and the row must say so, as entries 208 to 210 do.

#### The licence

Sweep 7 found no Creative Commons licence on Gothelf's pages. The bundle may name the eight boxes and quote
Gothelf briefly with attribution. Every guidance comment must be the library's own words, and no box's prompt
text may be copied whole.

#### The example: collaborative analysis, recommended

**Recommended: a canvas for the roadmap's "Collaborative analysis" item.** Confidence: medium-low. The FY26
roadmap (`product-roadmap_example.md:69-70`) holds it in the Later lane: "Analysts who answer a question get asked
the same question again by someone else. Nobody has shaped it, and it may belong to the support team rather than
to this product." That is an unshaped initiative with no investment behind it, which is the canvas's ground.
Gothelf's Box 5 invites "non-technical solutions", so the support-team option belongs in it.

**Facts the example must carry, with no contradiction.**

- It is dated after the roadmap (February 2026) and cites no later document. The roadmap's Review Trigger
  (`product-roadmap_example.md:112`) sets a review on 15 October 2026, so a date in September 2026 fits.
- Box 2's outcome ladders to the strategy's measure: "the share of new accounts that build a second view within 14
  days, from a 31 percent baseline to 50 percent" (`product-roadmap_example.md:39-40`), or states why it does not.
- Box 3 uses the Recurring Analyst, by that name, as the strategy requires (`product-strategy_example.md:43-47`).
- Its Hypotheses table must not name Saved Views sharing as a new solution. The internal announcement already
  tells the Reporting squad it can "share a saved view with a teammate today"
  (`announcement-internal-comms_example.md:74`).

**The alternative** is the per-vertical modelling defaults, which the strategy lists as an untested assumption
(`product-strategy_example.md:125`). It was rejected because the 2026-01-20 business case already funds
"Question-First Entry and Modelling Defaults", so a canvas would come after the investment decision.

#### Risks for the build and the review

- **The duplication argument could leak into the guide as a sourced claim.** It is the library's POSITION, and
  the guide must say so.
- **The 2024 prompt changes rest on Gothelf's summary.** The build must read the PDF before it uses them.
- **Example reuse.** The templates agent has reused the worked example's scenario in GOOD and WEAK text before.
  Grep the template for "collaborative", "Recurring Analyst" and "support team" before review.
- **The canvas is a facilitation tool.** Gothelf calls it one, and the efficacy record says a session's value
  stays mostly in the room. The companion must not claim the filled canvas is the value.

#### What landing this bundle closes elsewhere

- Issue #330 closes, relabelled `status:built`.
- The catalog gains entry 211, and `check-counts.py`'s markers move.
- [`backlog.md`](backlog.md) sections 2 and 3 move with the counts.
- `discovery-docs`' header Members line changes "not yet built" to the build date.

#### The build plan

**Preconditions, each of which must hold before the build starts:**

1. The maintainer has read ADR 0082 and its contract diff, and accepted or amended them.
2. The maintainer has answered the choices below.
3. Issue #330 carries `status:queued`.
4. The maintainer has asked for the build in their own words, such as "use the workflow". The build runs
   through the `build-bundle` workflow, and a workflow needs that opt-in.

**Build order: `lean-ux-canvas` first, then `lean-canvas`.** Confidence: medium. Its admission was settled by a
full sweep, and its family amendment is the smaller one. The two bundles share no example facts, so either order
works.

**The run.** One PR per bundle, the usual 15 agents on Sonnet: six research dimensions, the drafting stages and
four review lenses. Measured builds cost $12 to $41 each ([`bundle-builds/INDEX.md`](../../bundle-builds/INDEX.md)),
and a single-size bundle is not reliably cheaper.

**The six research dimensions.**

| Key | What it settles |
|---|---|
| `origins` | The canvas's history: version 1, version 2 of 2019, the Lean Product Canvas of 2024, and the Lean UX book's three editions. Read the 2024 PDF |
| `structure` | Each box's wording and hints in both editions, the hypothesis grammar, and how Box 7 uses the Hypothesis Prioritization Canvas |
| `practice` | How software teams fill and revise it: who is in the room, how long it takes, when it is abandoned. Atomic Object is the one read so far |
| `debates` | Box 2 against Box 4, which Gothelf calls the most confused part; the canvas as a facilitation tool or a document; the renaming |
| `relationships` | Patton's Opportunity Canvas, the Lean Strategy Canvas, Maurya's Lean Canvas, experiment design and OKRs |
| `gap` | The standing gap question, per the runbook |

**Sites the research may not read.** Miro hosts many Lean UX Canvas boards, and miro.com bars automated reading.
So do Substack, ProductPlan, Atlassian and the other sites in the runbook's table. Any page needed from them goes
to the maintainer's hand-read list.

#### The maintainer's choices

Answer in one line, such as "C1 A, C2 A, the rest as recommended".

| # | Choice | Recommended | Alternative |
|---|---|---|---|
| C1 | Admit and place the canvas | **A:** `discovery-docs`, `phase: discover`, with the second cadence exception (ADR 0082) | B: decline, as sweep 7 recommended |
| C2 | Id and name | **A:** id `lean-ux-canvas`, title "Lean UX Canvas", alias "Lean Product Canvas" | B: id `lean-product-canvas`, with issue #330 retitled |
| C3 | Box wording | **A:** the 2019 headings, with the 2024 PDF's wording wherever it differs, both recorded in the companion | B: the 2019 version only |
| C4 | Sizes | **A:** `[lean]` | B: `[lean, full]` |
| C5 | Section 9, Revisions and What Takes Over | **A:** keep it, labelled POSITION | B: the eight boxes only |
| C6 | The example | **A:** collaborative analysis, roadmap Later item 6 | B: per-vertical modelling defaults |
| C7 | Build order | **A:** this bundle first, then `lean-canvas` | B: `lean-canvas` first |

### strategy-docs (seventh member, by amendment): the Lean Canvas

**`lean-canvas`** - `strategy-docs`, **`classification: utility`** (recommended), size **`[lean]`**
(recommended), methodology **`Lean Startup`**, catalog **entry 5**, Tier 2. Issue #337 (bundle: lean-canvas),
priority P2. The family decision is
[ADR 0083](decisions/0083-lean-canvas-joins-strategy-docs-as-a-seventh-member.md) (lean-canvas joins
strategy-docs as a seventh member), **proposed 2026-10-30**. It amends the contract, so it stops for the
maintainer's read. Nothing in this section is ruled yet.

#### The recommendation, and how sure it is

**Build Ash Maurya's Lean Canvas as the seventh `strategy-docs` member, at `classification: utility`, in one
size.** Confidence: medium.

The canvas states a product's business model on one page: its customers and early adopters, their problems and
how they solve them today, the unique value proposition, the solution, the channels, the revenue streams, the
cost structure, the key metrics and the unfair advantage. Maurya says it "helps you deconstruct an idea into key
assumptions or beliefs." It is revised as those beliefs are tested.

**What holds the confidence at medium.** Admission is settled on the originator's own page. Three calls are
argued rather than sourced: `utility` over `foundation`, second place in the chain, and the answer to the
duplication finding.

#### Demand: a catalog row, a re-score, and the maintainer's choice

- Catalog entry 5 has carried the type since the catalog was built, under "Strategy / Vision".
- The 2026-10-11 Define sweep and the 2026-10-20 re-score both kept it out of `define`. Neither tested another
  family. Their digests are held locally.
- On 2026-10-30 the maintainer chose to include the canvas, set its priority to P2, and opened issue #337.

#### Admission: re-established on Maurya's own page

**The earlier admission no longer holds.** The 2026-10-11 sweep admitted the canvas on Atlassian's Confluence
template alone, because its two research dimensions disagreed about the form of Maurya's own site. Sweep 7
reported Atlassian's site barred under the terms rule on 2026-10-29. That clause has not yet been checked against
the raw terms page, but no agent reads the site while the report stands.

**Maurya's own page carries admission now.** Every quotation below passed a raw-text check on 2026-10-30.
leanspark.ai's terms page was read first the same day, and it carries no bar on automated reading.

- **Check 1, the written form.** [What is a Lean Canvas?](https://leanspark.ai/learn/what-is-lean-canvas),
  bylined Ash Maurya and dated 2024-09-07, teaches each box in prose. It states the origin: "Lean Canvas was created
  by me, Ash Maurya, and is an adaptation of Alexander Osterwalder’s Business Model Canvas - optimized for the Lean
  Startup methodology." The 2026-10-11 "document or board" dispute was argued under the test that ADR 0078 (canvases are templatable through
  their written form) retired.
- **Check 2, phase fit.** Not applicable: the canvas takes a `classification`.
- **Check 3, the written form of a canvas.** ADR 0078 admits it.
- **Check 4, no built bundle does its job.** Argued in ADR 0083's duplication section, labelled the library's
  POSITION.
- **Check 5, a software audience.** The page lists "Typical SaaS metrics" as examples for the Key Metrics box.

**The block count is settled.** Maurya's [product page](https://leanspark.ai/leancanvas) lists "The 12 blocks of
a Lean Canvas". They are the nine boxes plus three sub-blocks. The page glosses "Existing Alternatives" as "How customers solve
these problems today", "Early Adopters" as "The specific subset of customers you target first", and "High-Level
Concept" as "The X for Y analogy that makes your idea instantly understandable". The teaching page treats each
inside its parent box.

**Pages for the maintainer to read by hand, if wanted.** Atlassian's
[Lean Canvas template](https://www.atlassian.com/software/confluence/templates/lean-canvas) would add a second
named source. It is not needed.

#### Classification: `utility`, recommended

**The contract's test is "argued-and-durable versus maintained-and-periodic".** Maurya describes a canvas kept
current. "Unlike a business plan, the goal with a Lean Canvas isn’t to achieve perfection but to take a
snapshot." "Like everything on the canvas, you start with the best guess and iterate from there." His canvas guide
says "Your canvas is versioned automatically."

**Recommended: `utility`.** Confidence: medium. No originator page read states a calendar interval, so the
revisions follow test results. **The alternative is `foundation`**, for a reader who treats the canvas as a
founder's argued thesis.

#### The family: `strategy-docs`, by amendment (ADR 0083)

**The membership sentence admits it as written.** A member "sets or tracks product direction above the level of
any single deliverable". A business model sits above every deliverable.

**`discovery-docs` cannot take it.** That contract requires each member to be "written once for a decision", and
it sends "a standing instrument revised on a cadence" to a `classification` family.

**A format of a built bundle does not fit either.** `business-case` is written once for one investment.
`product-strategy` is `foundation`, changed on a timescale of years. Either format would break its host's class.

**The `pairs_with` fact is not a placement argument.** The contract's metadata row names a pm-skills
`foundation-lean-canvas` skill. Placement rests on the membership sentence and the axis test alone.

#### Where it sits in the chain (POSITION)

**Second, between the product vision and the product strategy.** Confidence: medium-low. The vision says where
the product is going. The canvas states the business model that could get it there, as beliefs to test. The
strategy commits to the problems and segments those beliefs support. **The alternative** places the canvas after
the strategy, as the strategy's business model kept current beside the roadmap. No source states either sequence.

#### Boundaries with each named neighbour

| Neighbour | The line |
|---|---|
| `business-case` | It justifies one investment and is then finished. The canvas models the whole business and is revised as its beliefs are tested |
| `product-vision` | Its Why Us section asks the unfair-advantage question once, for years. The canvas asks it again whenever the model changes. Pichler names the Lean Canvas as a tool in the same space (`product-vision_companion.md:46-48`) |
| `product-strategy` | It chooses problems and segments and names no revenue stream, channel or cost structure |
| `positioning-statement` | It states how the product stands against a named alternative. The canvas's Existing Alternatives sub-block lists how customers solve the problem today, which may include no product at all |
| `north-star-metrics` | It names one measure of customer value. The canvas lists three to five key metrics that show whether the business model is working |
| `user-persona` | A researched portrait. The canvas names a segment and its early adopters in a line |
| Business Model Canvas, catalog entry 4 | Not built. Maurya names the four boxes he replaced: "key partnerships, key resources, key activities, and customer relationships" |
| `lean-ux-canvas` (ADR 0082) | Frames one initiative's hypotheses and asks nothing about revenue or cost |

#### Sizes: one, recommended

**`[lean]`, one size.** Confidence: medium-high. Maurya publishes one page and says "Embrace a 1-page
constraint". No source read splits a short canvas from a long one.

#### Section design (proposed, for the build's research to test)

Maurya's teaching page takes the boxes in this order, starting from customers. The Markdown template follows it,
because a linear document cannot keep the canvas's grid.

| # | Section | What it holds | Source |
|---|---|---|---|
| 1 | Customer Segments | Who has the problem and who pays, with a line for **Early Adopters** | Maurya's teaching page |
| 2 | Problem | The top one to three problems, with a line for **Existing Alternatives** | Maurya's teaching page |
| 3 | Unique Value Proposition | Why the product is different and worth attention, with a line for the **High-Level Concept** | Maurya's teaching page |
| 4 | Solution | The simplest thing that addresses each problem; Maurya: "Bind a solution to your problem as late as possible." | Maurya's teaching page |
| 5 | Channels | The path to customers, now and at scale | Maurya's teaching page |
| 6 | Revenue Streams | How the product makes money, priced now rather than later | Maurya's teaching page |
| 7 | Cost Structure | What it costs to reach the next milestone, three to six months out | Maurya's teaching page |
| 8 | Key Metrics | Three to five outcome metrics, leading where possible | Maurya's teaching page |
| 9 | Unfair Advantage | What cannot be easily copied or bought | Maurya's product page |
| 10 | Riskiest Beliefs and Next Tests | The beliefs on this canvas to test next, and how | Maurya: "what are the next hypotheses you need to test to move your product forward?" The section itself is the library's POSITION |
| 11 | Versions | A dated row per revision: what changed and why | The library's POSITION, from the `utility` class; Maurya's tool versions canvases automatically |

**What stays out.** A financial model belongs in `business-case`. A strategy's diagnosis and guiding policy belong
in `product-strategy`. One initiative's hypotheses belong in `lean-ux-canvas`.

#### Metadata

| Field | Value |
|---|---|
| `id`, `doc_type` | `lean-canvas` |
| `title` | Lean Canvas |
| `family` | `strategy-docs` |
| `classification` | `utility` (recommended) |
| `sizes_available`, `default_size` | `[lean]`, `lean` |
| `methodology` | Lean Startup |
| `aliases` | none recommended; the catalog's "(Maurya adaptation of BMC)" is a note, not a name |
| `pairs_with` | `[foundation-lean-canvas]`, pinned in `tools/known-skills.txt`; `product-strategy` claims it too, and both claims can stand |
| `catalog_ref` | entry 5 |

#### Catalog corrections the landing PR should check (per decision-procedures.md section 1)

- **The alias.** "(Maurya adaptation of BMC)" moves to the row's notes.
- **The purpose.** "Problem-focused one-pager for startups" understates the solution and business-model content,
  as the 2026-10-11 sweep found. Proposed: "One-page business model, stated as beliefs to test".
- **The stage.** `ideation` is free text, not a phase, and stays as the catalog's older stage word.

#### The licence

A Creative Commons licence appears only on third-party mirrors, and Maurya's own pages state none. The bundle may
name the boxes and quote Maurya briefly with attribution. Every guidance comment must be the library's own words.

#### The example: Acme's embedded-analytics line, recommended

**Recommended: a Lean Canvas for an embedded-analytics OEM line of business.** Confidence: medium-low. The FY26
strategy (`product-strategy_example.md:56-57`) names it a non-target: "Two deals last year, both delivered by the
services team, both requiring a different product than the one above." A different product with different
customers is the canvas's ground. Maurya built the canvas "for startups operating under conditions of extreme
uncertainty", and a new line inside Acme is the closest honest fit to that.

**Facts the example must carry, with no contradiction.**

- It is dated inside FY26, which runs "February 2026 to January 2027" (`product-strategy_example.md:5`), and it
  models the line as a candidate for FY27, never as FY26 work.
- Its Customer Segments are software vendors, because "Embedded-analytics vendors ... sell to the software vendor
  rather than to the operator" (`product-vision_example.md:83-84`).
- It contradicts no sibling. It must not say the strategy has changed, and the positioning statement's
  non-targets (`positioning-statement_research-log.md:567`) stay non-targets.
- Its Versions table shows at least two dated revisions, so the `utility` class is visible.

**The alternatives.** A canvas for Acme's core product would show the format on familiar facts, but Maurya built
it for uncertainty, not for an established line. A canvas for the enterprise data-governance segment would model
the existing revenue base, which the strategy holds rather than explores.

#### Risks for the build and the review

- **The name collides inside the library.** `product-vision_guide.md:69` says "the lean canvas" for that bundle's
  lean-size `canvas` format. The landing PR adds a dated clarification there.
- **Misattribution is this family's named citation hazard.** Many pages repeat the canvas under Maurya's name, and
  some describe a "Leaner Canvas" that the 2026-10-11 sweep could not confirm. Quote Maurya only from his own
  pages or book.
- **The `utility` call could be over-read.** No source states a calendar interval, and the guide must not invent
  one.
- **Example reuse.** Grep the template for "OEM", "embedded" and "software vendor" before review.

#### What landing this bundle closes elsewhere

- Issue #337 closes, relabelled `status:built`.
- Catalog entry 5's `state` becomes `built`, and `check-counts.py`'s markers move.
- [`backlog.md`](backlog.md) sections 2, 3 and 4 move with the counts.
- `strategy-docs`' header Members line changes "not yet built" to the build date.
- `product-vision_guide.md:69` gains its dated clarification.

#### The build plan

**Preconditions, each of which must hold before the build starts:**

1. The maintainer has read ADR 0083 and its contract diff, and accepted or amended them.
2. The maintainer has answered the choices below.
3. Issue #337 carries `status:queued`.
4. The maintainer has asked for the build in their own words, such as "use the workflow".

**Build order:** second, after `lean-ux-canvas`, as recommended in that section's choice C7.

**The run.** One PR, the usual 15 agents on Sonnet, $12 to $41 by the measured range.

**The six research dimensions.**

| Key | What it settles |
|---|---|
| `origins` | Maurya's original blog post, the editions of *Running Lean*, and the move from leanstack.com to leanspark.ai |
| `structure` | Each box and sub-block in Maurya's words, his fill order, and the 20-minute and 1-page rules |
| `practice` | How software teams and founders revise a canvas, and how often, from named sources only |
| `debates` | Startup against established company; canvas against business plan; the solution-first trap Maurya warns about; the unconfirmed "Leaner Canvas" |
| `relationships` | The Business Model Canvas, the Lean UX Canvas, the Product Vision Board, the business case and the North Star |
| `gap` | The standing gap question, per the runbook |

**Sites the research may not read.** Atlassian, Miro, Substack, ProductPlan, Product School and the other sites in
the runbook's table. Many Lean Canvas templates live on them. Any page needed from them goes to the maintainer's
hand-read list.

#### The maintainer's choices

Answer in one line, such as "D1 A, D2 B, the rest as recommended".

| # | Choice | Recommended | Alternative |
|---|---|---|---|
| D1 | Admit and place the canvas | **A:** `strategy-docs`, seventh member (ADR 0083) | B: leave it out |
| D2 | Classification | **A:** `utility` | B: `foundation` |
| D3 | Chain position | **A:** second, between the vision and the strategy | B: after the strategy, beside the roadmap |
| D4 | Sizes | **A:** `[lean]` | B: `[lean, full]` |
| D5 | Sections 10 and 11, Riskiest Beliefs and Versions | **A:** keep both, labelled POSITION | B: the nine boxes only |
| D6 | The example | **A:** the embedded-analytics OEM line | B: Acme's core product; C: the enterprise segment |
| D7 | `pairs_with` | **A:** `[foundation-lean-canvas]` | B: `[]` |
